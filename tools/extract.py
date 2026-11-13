"""Extract CCNA questions from the .docx library into web/data.js + web/img/."""
import json, os, re, sys, hashlib
import docx
from docx.oxml.ns import qn

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "Danh sach cau hoi version 1 (1)", "5-16")
OUT = os.path.join(ROOT, "web")
IMG = os.path.join(OUT, "img")
os.makedirs(IMG, exist_ok=True)

SECTIONS = [
    ("fund", "Network Fundamentals", "CCNA_Network_Fundamentals"),
    ("access", "Network Access", "CCNA_Network_Access"),
    ("ipconn", "IP Connectivity", "CCNA_IP_Connectivity"),
    ("ipsvc", "IP Services", "CCNA_IP_Services"),
    ("sec", "Security Fundamentals", "CCNA_Security_Fundamentals"),
    ("auto", "Automation & Programmability", "CCNA_Automation_Programmability"),
]

Q_RE = re.compile(r"^\s*Question\s*[:#]?\s*([\w.\-]+)", re.I)
ANS_RE = re.compile(r"^\s*(Answer|Correct Answer)s?\s*[:：]?\s*(.*)$", re.I | re.S)
OPT_RE = re.compile(r"^\s*([A-H])[.)](?:\s+(.*))?$", re.S)


def para_text(el):
    texts = []
    for node in el.iter():
        if node.tag == qn("w:t"):
            texts.append(node.text or "")
        elif node.tag in (qn("w:br"), qn("w:cr")):
            texts.append(chr(10))
        elif node.tag == qn("w:tab"):
            texts.append(chr(9))
    return "".join(texts).replace(chr(160), " ")


def iter_blocks(doc):
    """Yield ('p', text, [image rIds]) or ('t', rows) in document order."""
    for el in doc.element.body.iterchildren():
        if el.tag == qn("w:p"):
            texts = []
            for node in el.iter():
                if node.tag == qn("w:t"):
                    texts.append(node.text or "")
                elif node.tag in (qn("w:br"), qn("w:cr")):
                    texts.append("\n")
                elif node.tag == qn("w:tab"):
                    texts.append("\t")
            rids = [b.get(qn("r:embed")) for b in el.iter(qn("a:blip")) if b.get(qn("r:embed"))]
            rids += [i.get(qn("r:id")) for i in el.iter("{urn:schemas-microsoft-com:vml}imagedata") if i.get(qn("r:id"))]
            yield ("p", "".join(texts), rids)
        elif el.tag == qn("w:tbl"):
            rows = []
            for tr in el.iter(qn("w:tr")):
                cells = []
                for tc in tr.iter(qn("w:tc")):
                    cells.append("\n".join(para_text(p) for p in tc.iter(qn("w:p"))).strip())
                rows.append(cells)
            rids = [b.get(qn("r:embed")) for b in el.iter(qn("a:blip")) if b.get(qn("r:embed"))]
            yield ("t", rows, rids)


def save_image(doc, rid, cache):
    if rid in cache:
        return cache[rid]
    part = doc.part.related_parts.get(rid)
    if part is None:
        return None
    blob = part.blob
    ext = os.path.splitext(part.partname)[1].lower() or ".png"
    if ext in (".emf", ".wmf"):
        cache[rid] = None
        return None
    name = hashlib.md5(blob).hexdigest()[:16] + ext
    path = os.path.join(IMG, name)
    if not os.path.exists(path):
        with open(path, "wb") as f:
            f.write(blob)
    cache[rid] = "img/" + name
    return cache[rid]


def parse_section(path, sec_id):
    doc = docx.Document(path)
    cache = {}
    questions, cur = [], None
    n_extra = 0

    def flush():
        if cur:
            questions.append(cur)

    def new_q(num, extra=False):
        nonlocal cur
        flush()
        cur = {"num": num, "blocks": [], "answerRaw": None, "extra": extra}

    def ensure_open():
        """Content after an answered question with no "Question x.y" heading starts a new
        (supplementary) question - e.g. the numbered "Bổ sung" items at the end of each file."""
        nonlocal n_extra
        if cur is not None and cur["answerRaw"] is not None:
            n_extra += 1
            new_q(f"BS-{n_extra}", extra=True)

    def add_images(rids):
        for rid in rids:
            src = save_image(doc, rid, cache)
            if src:
                ensure_open()
                cur["blocks"].append({"img": src})

    def add_text(text):
        buf = []

        def emit():
            if buf and cur is not None and "\n".join(buf).strip():
                cur["blocks"].append({"text": "\n".join(buf).strip()})
            buf.clear()

        for line in text.split("\n"):
            ls = line.strip()
            answered = cur["answerRaw"] is not None
            # Separators between questions ("Bổ sung" header, dashed rules, a bare "8.") are not content;
            # dashed lines *inside* a question are part of show-command output and are kept.
            if ls.lower() == "bổ sung" or (answered and re.fullmatch(r"-{3,}|\d+[.)]?", ls)):
                emit()
                continue
            am = ANS_RE.match(ls) if ls else None
            if am and not answered:
                emit()
                cur["answerRaw"] = am.group(2).strip()
                continue
            if ls and answered:
                ensure_open()
                line = re.sub(r"^\s*\d+[.)]\s+", "", line)  # drop "1." numbering of supplementary items
            buf.append(line)
        emit()

    for kind, payload, rids in iter_blocks(doc):
        if kind == "p":
            text = payload.replace("\xa0", " ").strip()
            m = Q_RE.match(text) if text else None
            if m and len(text) < 40:
                new_q(m.group(1))
                continue
            if cur is None:
                continue
            add_images(rids)
            if text:
                add_text(text)
        else:
            if cur is None:
                continue
            add_images(rids)
            ensure_open()
            cur["blocks"].append({"table": payload})
    flush()

    out = []
    n_head = n_bs = 0
    for q in questions:
        stem, options, media = [], [], []
        for b in q["blocks"]:
            if "text" in b:
                for line in b["text"].split("\n"):
                    om = OPT_RE.match(line)
                    if om:
                        options.append({"key": om.group(1), "text": (om.group(2) or "").strip()})
                    elif line.strip():
                        if options:
                            options[-1]["text"] += "\n" + line.strip()
                        else:
                            stem.append({"text": line})
            else:
                stem.append(b) if not options else media.append(b)
        ans_raw = q["answerRaw"] or ""
        keys = re.findall(r"\b([A-H])\b", ans_raw.upper()) if re.fullmatch(r"[A-H ,;&and]+", ans_raw.strip(), re.I) else []
        valid = {o["key"] for o in options}
        keys = [k for k in dict.fromkeys(keys) if k in valid]
        # Headed questions keep ids sec-1..N (explanations and saved progress depend on them);
        # supplementary ones get sec-b1.. so they never shift existing ids.
        if q["extra"]:
            n_bs += 1
            qid = f"{sec_id}-b{n_bs}"
        else:
            n_head += 1
            qid = f"{sec_id}-{n_head}"
        item = {
            "id": qid,
            "num": q["num"],
            "stem": stem + media,
            "options": options,
            "answer": keys,
        }
        if not keys:
            item["answerText"] = ans_raw
        if q.get("explain"):
            item["explain"] = "\n".join(q["explain"])
        out.append(item)
    return out


def main():
    files = os.listdir(SRC)
    data = []
    for sec_id, title, prefix in SECTIONS:
        fn = next(f for f in files if f.startswith(prefix) and f.endswith(".docx"))
        qs = parse_section(os.path.join(SRC, fn), sec_id)
        mcq = sum(1 for q in qs if q["answer"])
        print(f"{title}: {len(qs)} questions ({mcq} auto-gradable, {len(qs)-mcq} other) from {fn}")
        data.append({"id": sec_id, "title": title, "questions": qs})
    with open(os.path.join(OUT, "data.js"), "w", encoding="utf-8") as f:
        f.write("window.CCNA_DATA = ")
        json.dump(data, f, ensure_ascii=False)
        f.write(";\n")


if __name__ == "__main__":
    main()

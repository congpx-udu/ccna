"""Build review chunks for exhibit (image) questions, including current explanations.
Usage: python prep_review.py <name> <sec_id> [<sec_id> ...] [--split N]"""
import glob, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "web")
OUT = os.path.join(ROOT, "tools", "explain", "review")
os.makedirs(OUT, exist_ok=True)

args = sys.argv[1:]
split = 1
if "--split" in args:
    i = args.index("--split"); split = int(args[i + 1]); args = args[:i] + args[i + 2:]
name, secs = args[0], set(args[1:])

ex = {}
for f in glob.glob(os.path.join(ROOT, "tools", "explain", "out", "*.json")):
    ex.update(json.load(open(f, encoding="utf-8")))
s = open(os.path.join(WEB, "data.js"), encoding="utf-8").read()
qs = [q for sec in json.loads(s[s.index("=") + 1:].rstrip().rstrip(";")) if sec["id"] in secs
      for q in sec["questions"] if any("img" in b for b in q["stem"])]
size = (len(qs) + split - 1) // split
for part in range(split):
    chunk = qs[part * size:(part + 1) * size]
    lines = []
    for q in chunk:
        lines.append(f"## {q['id']}  (Question {q['num']})")
        for b in q["stem"]:
            if "img" in b:
                lines.append(f"[IMAGE: {os.path.join(WEB, b['img'])}]")
            elif "table" in b:
                lines.append("[TABLE]\n" + "\n---\n".join(" | ".join(r) for r in b["table"]) + "\n[/TABLE]")
            else:
                lines.append(b["text"])
        for o in q["options"]:
            lines.append(f"- {o['key']}. {o['text'].strip()}")
        lines.append(f"ANSWER: {', '.join(q['answer']) or q.get('answerText', '?')}")
        cur = ex.get(q["id"], {})
        lines.append(f"CURRENT_EXPLANATION: {json.dumps(cur, ensure_ascii=False)}\n")
    fn = os.path.join(OUT, f"{name}-{part + 1}.md")
    open(fn, "w", encoding="utf-8").write("\n".join(lines))
    print(fn, len(chunk))

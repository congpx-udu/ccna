"""Dump questions into chunked markdown files for writing explanations."""
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "web")
OUT = os.path.join(ROOT, "tools", "explain", "input")
os.makedirs(OUT, exist_ok=True)
CHUNK = 100

s = open(os.path.join(WEB, "data.js"), encoding="utf-8").read()
data = json.loads(s[s.index("=") + 1:].rstrip().rstrip(";"))
for sec in data:
    qs = sec["questions"]
    for part in range((len(qs) + CHUNK - 1) // CHUNK):
        lines = [f"# {sec['title']} (part {part + 1})\n"]
        for q in qs[part * CHUNK:(part + 1) * CHUNK]:
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
            lines.append(f"ANSWER: {', '.join(q['answer']) or q.get('answerText', '?')}\n")
        name = f"{sec['id']}-{part + 1}.md"
        open(os.path.join(OUT, name), "w", encoding="utf-8").write("\n".join(lines))
        print(name, len(qs[part * CHUNK:(part + 1) * CHUNK]))

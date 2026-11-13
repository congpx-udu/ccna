"""Merge tools/explain/out/*.json into web/explain.js and report coverage."""
import glob, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "web")

merged = {}
for sub in ("out", "review_out"):  # reviewed (exhibit-checked) explanations override first drafts
    for f in sorted(glob.glob(os.path.join(ROOT, "tools", "explain", sub, "*.json"))):
        for k, v in json.load(open(f, encoding="utf-8")).items():
            merged[k] = v if isinstance(v, dict) else {"e": v}  # some drafts used plain strings
# Hand-written fixes win; explanations must follow the library's answer key, so drop "warn" notes.
merged.update(json.load(open(os.path.join(ROOT, "tools", "explain", "overrides.json"), encoding="utf-8")))
merged = {k: {"e": v["e"]} for k, v in merged.items()}

s = open(os.path.join(WEB, "data.js"), encoding="utf-8").read()
ids = [q["id"] for sec in json.loads(s[s.index("=") + 1:].rstrip().rstrip(";")) for q in sec["questions"]]
missing = [i for i in ids if i not in merged or not merged[i].get("e")]
merged = {i: merged[i] for i in ids if i in merged}

with open(os.path.join(WEB, "explain.js"), "w", encoding="utf-8") as f:
    f.write("window.CCNA_EXPLAIN = ")
    json.dump(merged, f, ensure_ascii=False)
    f.write(";\n")
print(f"{len(merged)}/{len(ids)} explained, {sum(1 for v in merged.values() if v.get('warn'))} with warnings")
if missing:
    print("missing:", " ".join(missing))

"""Schreibt eine HTML-Vorschau (SVG) pro Kategorie nach _preview/<id>.html, ohne Browser-Abhängigkeit."""
import sys, os, importlib
sys.path.insert(0, os.path.dirname(__file__))
from build import svg
prev = os.path.join(os.path.dirname(__file__), "_preview"); os.makedirs(prev, exist_ok=True)
for cid in sys.argv[1:]:
    mod = importlib.import_module("cat_" + cid)
    ms = [m.to_json() for m in mod.build() if not os.environ.get("ONLY") or m.id in os.environ["ONLY"].split(",")]
    html = "<body style='margin:0;background:#eee;display:flex;flex-wrap:wrap;gap:4px;padding:4px'>" + "".join(
        f"<div style='font:12px sans-serif'>{m['id']} ({len(m['regions'])})<br>{svg(m, int(os.environ.get("PSIZE", 136)))}</div>" for m in ms) + "</body>"
    open(f"{prev}/{cid}.html", "w").write(html)
    print(cid, len(ms), "motifs", sum(len(m["regions"]) for m in ms), "regions")

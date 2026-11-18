import json, sys, os, importlib, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from dsl import *

CATS = ["weihnachten", "advent", "winter", "freimalen", "dinos", "baustelle", "haeuser", "mandalas", "tiere", "meer", "fahrzeuge", "weltraum", "essen", "natur", "fantasie"]
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Bunto", "Resources", "motifs.json")
INK = "#2B2D42"

def svg(m, size=300):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="{size}" height="{size}">',
             '<rect width="100" height="100" fill="white"/>',
             f'<g stroke="{INK}" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" fill="white">']
    for r in m["regions"]:
        parts.append(f'<path d="{r}"/>')
    for l in m["lines"]:
        parts.append(f'<path d="{l}" fill="none"/>')
    parts.append('</g>')
    for d in m["dots"]:
        parts.append(f'<path d="{d}" fill="{INK}"/>')
    parts.append('</svg>')
    return "".join(parts)

def main(only=None):
    cats = []
    for cid in CATS:
        if only and cid not in only:
            continue
        mod = importlib.import_module("cat_" + cid)
        motifs = [m.to_json() for m in mod.build()]
        cats.append({"id": cid, "emoji": mod.EMOJI, "de": mod.DE, "en": mod.EN, "color": mod.COLOR, "motifs": motifs})
    return cats

if __name__ == "__main__":
    only = sys.argv[1:] or None
    cats = main(only)
    if not only:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        json.dump({"categories": cats}, open(OUT, "w"), ensure_ascii=False, separators=(",", ":"))
        print("wrote", OUT, sum(len(c["motifs"]) for c in cats), "motifs")
    # preview
    prev = os.path.join(os.path.dirname(__file__), "_preview")
    os.makedirs(prev, exist_ok=True)
    for c in cats:
        html = "<body style='margin:0;background:#eee;display:flex;flex-wrap:wrap;gap:6px;padding:6px;width:1250px'>" + "".join(
            f"<div style='font:12px sans-serif'>{m['id']}<br>{svg(m, 300)}</div>" for m in c["motifs"]) + "</body>"
        open(f"{prev}/{c['id']}.html", "w").write(html)
    js = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1262,height:700}});" + \
        "".join(f"await p.goto('file://{os.path.abspath(prev)}/{c['id']}.html');await p.screenshot({{path:'{os.path.abspath(prev)}/{c['id']}.png',fullPage:true}});" for c in cats) + "await b.close()})()"
    open(f"{prev}/shot.js", "w").write(js)
    try:
        subprocess.run(["node", f"{prev}/shot.js"], check=True)
    except Exception:
        print("(Vorschau-PNGs übersprungen – playwright fehlt; HTML-Vorschau: preview.py)")

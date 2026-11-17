#!/usr/bin/env python3
"""Schreibt hübsch ausgemalte Beispiel-Motive in den App-Speicher eines Simulators (nur für Store-Screenshots).

Aufruf:  python3 tools/appstore/seed_progress.py <Pfad zu .../Library/Application Support/Bunto>
"""
import json, sys, pathlib, random

root = pathlib.Path(__file__).resolve().parents[2]
motifs = json.loads((root / "Bunto/Resources/motifs.json").read_text())["categories"]
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)

# Palettenindizes (siehe Bunto/Models/Palette.swift)
THEMES = {
    "dinos":   [4, 3, 2, 1, 5],
    "mandalas": [0, 1, 2, 4, 6, 8, 9],
    "tiere":   [10, 11, 1, 2, 9, 12],
}
FULL = {"dinos": 8, "mandalas": 4, "tiere": 4}
PARTIAL = {"trex": 7}          # T-Rex bleibt halb fertig (Kopf noch weiß) – schön fürs Mal-Screenshot

for cat in motifs:
    n = FULL.get(cat["id"], 0)
    for mi, m in enumerate(cat["motifs"][:n]):
        rng = random.Random(m["id"])
        theme = THEMES[cat["id"]]
        count = len(m["regions"])
        upto = PARTIAL.get(m["id"], count)
        fills = {}
        for r in range(min(upto, count)):
            c = theme[(r + mi) % len(theme)] if cat["id"] == "mandalas" else (theme[0] if r == 2 else rng.choice(theme))
            fills[str(r)] = c
        (out / f'{m["id"]}.json').write_text(json.dumps({"fills": fills, "strokes": [], "rev": 1}))
print("ok ->", out)

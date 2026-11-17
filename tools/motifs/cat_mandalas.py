from dsl import *
EMOJI, DE, EN, COLOR = "🌸", "Mandalas", "Mandalas", "#9B5DE5"

def build_one(id, de, en, ops):
    m = Motif(id, de, en)
    for op in ops:
        k = op[0]
        if k == "disc":
            m.f(ell(50, 50, op[1]))
        elif k == "petals":
            _, n, r0, r1, w = op[:5]
            off = op[5] if len(op) > 5 else 0
            for i in range(n):
                m.f(petal(r0, r1, w).rot(off + i * 360 / n))
        elif k == "dots":
            _, n, rad, sz = op[:4]
            off = op[4] if len(op) > 4 else 0
            for i in range(n):
                a = math.radians(-90 + off + i * 360 / n)
                m.f(ell(50 + rad * math.cos(a), 50 + rad * math.sin(a), sz))
        elif k == "diamonds":
            _, n, r0, r1, w = op[:5]
            off = op[5] if len(op) > 5 else 0
            for i in range(n):
                rm = (r0 + r1) / 2
                m.f(rpoly([(50, 50 - r0), (50 + w, 50 - rm), (50, 50 - r1), (50 - w, 50 - rm)], 1.2).rot(off + i * 360 / n))
        elif k == "spikes":
            _, n, r0, r1, w = op[:5]
            off = op[5] if len(op) > 5 else 0
            for i in range(n):
                m.f(rpoly([(50 - w, 50 - r0), (50, 50 - r1), (50 + w, 50 - r0)], 1).rot(off + i * 360 / n))
        elif k == "hearts":
            _, n, rad, sz = op[:4]
            off = op[4] if len(op) > 4 else 0
            for i in range(n):
                a = -90 + off + i * 360 / n
                m.f(heart(50, 50 - rad, sz).rot(off + i * 360 / n, 50, 50))
        elif k == "star":
            m.f(star(50, 50, op[1], op[2], op[3], -90, 1))
        elif k == "ngon":
            m.f(ngon(50, 50, op[1], op[2], -90, 1.5))
        elif k == "leaves":
            _, n, r0, r1, w = op[:5]
            off = op[5] if len(op) > 5 else 0
            for i in range(n):
                m.f(blob([(50, 50 - r0), (50 + w, 50 - (r0 + r1) / 2), (50, 50 - r1), (50 - w, 50 - (r0 + r1) / 2)]).rot(off + i * 360 / n))
    return m

def build():
    S = [
        ("m1", "Blume", "Flower", [("disc", 47), ("petals", 12, 20, 47, 7), ("disc", 30), ("petals", 8, 8, 30, 8, 22.5), ("dots", 8, 36, 2.6, 22.5), ("disc", 10)]),
        ("m2", "Sonne", "Sun", [("spikes", 16, 30, 49, 5), ("disc", 36), ("dots", 16, 30, 3, 11.25), ("disc", 24), ("petals", 8, 5, 22, 6), ("disc", 8)]),
        ("m3", "Stern", "Star", [("disc", 47), ("star", 46, 22, 8), ("star", 30, 14, 8), ("dots", 8, 38, 3.5, 22.5), ("disc", 8)]),
        ("m4", "Herzen", "Hearts", [("disc", 47), ("hearts", 8, 38, 6), ("disc", 30), ("hearts", 8, 22, 4.5, 22.5), ("disc", 12), ("dots", 8, 22, 1.6, 22.5)]),
        ("m5", "Schneeflocke", "Snowflake", [("disc", 47), ("diamonds", 6, 12, 46, 7), ("diamonds", 6, 12, 28, 5, 30), ("dots", 6, 38, 3, 30), ("disc", 9)]),
        ("m6", "Tulpe", "Tulip", [("disc", 47), ("leaves", 10, 14, 47, 9), ("leaves", 10, 12, 32, 7, 18), ("dots", 10, 38, 2.2, 0), ("disc", 12)]),
        ("m7", "Kreise", "Circles", [("disc", 47), ("dots", 16, 40, 5.5), ("dots", 12, 28, 4.5, 15), ("dots", 8, 16, 4, 0), ("disc", 6)]),
        ("m8", "Schmetterlingsblüte", "Butterfly Bloom", [("disc", 47), ("petals", 6, 10, 47, 12), ("petals", 6, 10, 34, 8, 30), ("dots", 6, 36, 3.5, 0), ("disc", 12)]),
        ("m9", "Kristall", "Crystal", [("disc", 47), ("ngon", 44, 6), ("ngon", 32, 6, ), ("diamonds", 6, 8, 30, 6, 30), ("dots", 6, 38, 3, 0), ("disc", 8)]),
        ("m10", "Seeigel", "Sea Star", [("spikes", 12, 22, 47, 8), ("disc", 30), ("petals", 12, 6, 28, 5, 15), ("disc", 12), ("dots", 12, 18, 1.8, 15)]),
        ("m11", "Lotus", "Lotus", [("disc", 47), ("leaves", 8, 22, 47, 10), ("leaves", 8, 14, 38, 8, 22.5), ("leaves", 8, 8, 28, 7), ("disc", 8)]),
        ("m12", "Zauberrad", "Magic Wheel", [("disc", 47), ("dots", 20, 41, 3.2), ("spikes", 10, 18, 38, 7), ("spikes", 10, 18, 38, 7, 18), ("disc", 24), ("star", 20, 9, 5), ("disc", 5)]),
    ]
    return [build_one(*s) for s in S]

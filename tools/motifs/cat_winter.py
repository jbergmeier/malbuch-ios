from dsl import *
EMOJI, DE, EN, COLOR = "⛄", "Winter", "Winter", "#4CC9F0"


def snowflake_small(m, x, y, r):
    m.f(star(x, y, r, r * 0.3, 6, -90, 0.3))


def schneemann():
    m = Motif("schneemann", "Schneemann", "Snowman")
    m.f(rect(0, 92, 100, 8, 0))
    m.l(curve([(30, 48), (20, 42), (10, 34)]), curve([(18, 41), (18, 34)]), curve([(70, 48), (80, 42), (90, 34)]), curve([(82, 41), (82, 34)]))
    m.f(ell(50, 74, 24, 20))
    m.f(ell(50, 50, 18, 16))
    m.f(ell(50, 26, 14, 13))
    m.f(rect(31, 12, 38, 5, 2.5))
    m.f(rect(37, 0, 26, 14, 2))
    m.f(rect(37, 8, 26, 4, 0))
    m.dot((44, 24, 1.7), (56, 24, 1.7))
    m.f(rpoly([(50, 28), (66, 31), (50, 34)], 1.5))
    for x in (42, 46, 50, 54, 58):
        pass
    m.l(arc(50, 33, 8, 4, 30, 150, 3))
    m.f(rect(34, 39, 32, 8, 4))
    m.f(rect(56, 44, 9, 18, 3))
    for y in (56, 66, 76):
        m.f(ell(50, y, 2.8, 2.8))
    for x, y, r in [(12, 14, 5), (86, 10, 5), (84, 62, 4), (12, 70, 4)]:
        snowflake_small(m, x, y, r)
    return m


def schneeflocke():
    m = Motif("schneeflocke", "Schneeflocke", "Snowflake")
    for i in range(6):
        a = i * 60
        m.f(rpoly([(50, 38), (55, 26), (50, 8), (45, 26)], 1.5).rot(a))
        m.f(bar(50, 30, 63, 17, 4.5).rot(a))
        m.f(bar(50, 30, 37, 17, 4.5).rot(a))
    m.f(ngon(50, 50, 11, 6, -90, 2))
    m.f(ngon(50, 50, 5, 6, -90, 1))
    for i in range(6):
        a = math.radians(i * 60 + 30 - 90)
        m.f(ell(50 + 38 * math.cos(a), 50 + 38 * math.sin(a), 2.6, 2.6))
    return m


def muetze_schal():
    m = Motif("muetze_schal", "Mütze und Schal", "Hat and Scarf")
    m.f(P([("M", [18, 48]), ("C", [16, 8, 84, 8, 82, 48]), ("Z", [])]))
    m.f(rect(14, 42, 72, 14, 6))
    for x in (24, 34, 44, 54, 64, 74):
        m.l(line((x, 42), (x, 56)))
    m.f(star(50, 24, 11, 4.4, 6, -90, 0.8))
    m.f(ell(50, 8, 9, 8))
    m.f(rect(10, 68, 80, 14, 7))
    for x in (24, 48, 70):
        m.f(rect(x, 68, 9, 14, 0))
    for i in range(7):
        m.f(rect(12 + i * 11.2, 82, 6, 12, 2.5))
    snowflake_small(m, 90, 36, 5)
    snowflake_small(m, 8, 30, 5)
    return m


def handschuhe():
    m = Motif("handschuhe", "Fäustlinge", "Mittens")
    m.l(curve([(28, 86), (50, 98), (72, 86)]))
    body = blob([(12, 66), (10, 36), (18, 14), (32, 10), (44, 24), (46, 66)])
    thumb = ell(50, 46, 6.5, 11).rot(-28, 50, 46)
    cuff = rect(8, 64, 40, 20, 6)
    star1 = star(28, 40, 9, 4, 6, -90, 0.8)
    dots = [ell(20, 56, 2.4, 2.4), ell(28, 56, 2.4, 2.4), ell(36, 56, 2.4, 2.4)]
    for parts in ([body, thumb, cuff, star1] + dots,):
        for p in parts:
            m.f(p)
            m.f(p.flip())
    for x in (16, 24, 32, 40):
        m.l(line((x, 64), (x, 84)), line((100 - x, 64), (100 - x, 84)))
    return m


def pinguin():
    m = Motif("winter_pinguin", "Winter-Pinguin", "Winter Penguin")
    m.f(ell(38, 95, 9, 3.5), ell(62, 95, 9, 3.5))
    m.f(ell(22, 62, 6, 18).rot(14, 22, 62), ell(78, 62, 6, 18).rot(-14, 78, 62))
    m.f(ell(50, 54, 27, 40))
    m.f(ell(50, 76, 17, 18))
    m.f(P([("M", [26, 24]), ("C", [24, 2, 76, 2, 74, 24]), ("Z", [])]))
    m.f(rect(24, 22, 52, 9, 4))
    m.f(ell(50, 5, 6, 5))
    m.eye(41, 38, 3.6, 1.6, 0.4, 0.3), m.eye(59, 38, 3.6, 1.6, -0.4, 0.3)
    m.f(rpoly([(44, 43), (56, 43), (50, 51)], 1.5))
    m.f(rect(30, 53, 40, 8, 4))
    m.f(rect(57, 57, 8, 18, 3))
    for x, y, r in [(10, 20, 5), (90, 30, 4), (88, 84, 5), (8, 80, 4)]:
        snowflake_small(m, x, y, r)
    return m


def eisbaer():
    m = Motif("eisbaer", "Eisbär", "Polar Bear")
    m.f(ell(22, 30, 11, 11), ell(78, 30, 11, 11))
    m.f(ell(22, 31, 5.5, 5.5), ell(78, 31, 5.5, 5.5))
    m.f(ell(50, 54, 33, 30))
    m.f(ell(50, 66, 16, 12))
    m.f(ell(50, 61, 6, 4.5))
    m.dot((36, 46, 2.2), (64, 46, 2.2))
    m.l(line((50, 66), (50, 72)), arc(50, 72, 6, 3.4, 10, 170, 4))
    m.f(ell(30, 60, 4.4, 3), ell(70, 60, 4.4, 3))
    m.f(rect(20, 80, 60, 11, 5.5))
    m.f(rect(60, 86, 11, 14, 3))
    for x in (28, 44, 60):
        m.l(line((x, 80), (x, 91)))
    for x, y, r in [(10, 8, 5), (90, 10, 4), (8, 66, 4), (92, 62, 5)]:
        snowflake_small(m, x, y, r)
    return m


def schlitten():
    m = Motif("schlitten", "Schlitten", "Sled")
    m.f(ell(50, 98, 56, 7))
    m.f(rpoly([(6, 64), (13, 62), (17, 68), (15, 78), (22, 86), (90, 86), (92, 90), (22, 91), (9, 82), (6, 74)], 1.2))
    m.f(rect(26, 74, 5, 12, 1), rect(68, 74, 5, 12, 1))
    m.f(rect(18, 66, 66, 9, 3))
    m.f(rect(26, 46, 20, 20, 2), rect(26, 54, 20, 3, 0))
    m.f(rect(33, 46, 6, 20, 0))
    m.f(rect(50, 38, 18, 28, 2), rect(56, 38, 6, 28, 0))
    m.f(blob([(59, 38), (50, 28), (44, 32), (52, 40)]), blob([(59, 38), (68, 28), (74, 32), (66, 40)]))
    m.f(fir(76, 38, 66, 9, 2, 1.2))
    m.f(rect(75, 66, 3, 0.01, 0)) if False else None
    m.f(ell(88, 34, 4, 4)) if False else None
    for x, y, r in [(14, 18, 6), (46, 10, 5), (84, 14, 6), (30, 34, 4), (90, 50, 4)]:
        snowflake_small(m, x, y, r)
    return m


def iglu():
    m = Motif("winter_iglu", "Iglu im Schnee", "Snowy Igloo")
    m.f(ell(84, 14, 8, 8))
    m.f(ell(50, 84, 42, 52))
    # Eisblöcke
    rows = [(40, 11), (51, 11), (62, 11), (73, 11)]
    for k, (y, h) in enumerate(rows):
        hw = 42 * math.sqrt(max(0, 1 - ((y - 84) / 52) ** 2)) - 3
        w = 14
        n = max(1, int((2 * hw) // w))
        total = n * w
        off = (w / 2) if k % 2 else 0
        x = 50 - total / 2
        for i in range(n):
            bx = x + i * w + off
            if bx < 50 - hw or bx + w - 1 > 50 + hw:
                continue
            m.f(rect(bx, y, w - 1.2, h - 1.2, 1.5))
    m.f(rect(0, 84, 100, 16, 0))
    m.f(rect(34, 60, 32, 26, 12))
    m.f(rect(41, 68, 18, 18, 8))
    for x, y, r in [(12, 12, 5), (30, 20, 4), (66, 14, 4), (92, 40, 4)]:
        snowflake_small(m, x, y, r)
    m.f(star(14, 92, 4, 1.8, 6, -90, 0.3), star(86, 94, 4, 1.8, 6, -90, 0.3))
    return m


def schneekugel():
    m = Motif("schneekugel", "Schneekugel", "Snow Globe")
    m.f(ell(50, 44, 38, 38))
    m.f(ell(50, 70, 22, 8))
    m.f(rect(41, 50, 19, 18, 1))
    m.f(rpoly([(37, 52), (50, 38), (63, 52)], 1.5))
    m.f(rect(47, 58, 6, 10, 2))
    m.f(rect(42, 54, 4, 4, 0.5))
    m.f(fir(32, 40, 68, 8, 2, 1.2))
    m.f(fir(68, 44, 68, 7, 2, 1.2))
    m.dot((30, 24, 1.2), (44, 18, 1.2), (60, 22, 1.2), (72, 30, 1.2), (24, 40, 1.2), (78, 48, 1.2), (52, 30, 1.2), (36, 32, 1.2))
    m.l(curve([(20, 34), (24, 24), (34, 16)]))
    m.f(rpoly([(24, 82), (76, 82), (84, 96), (16, 96)], 3))
    m.f(star(50, 89, 4.5, 2, 5, -90, 0.5))
    return m


def winterdorf():
    m = Motif("winterdorf", "Winterdorf", "Winter Village")
    m.f(ell(84, 14, 8, 8))
    for x, y, r in [(12, 10, 4), (34, 8, 3), (58, 12, 4), (70, 24, 3)]:
        m.f(star(x, y, r, r * 0.4, 4, -90, 0.3))
    # Hügel hinten
    m.f(blob([(0, 70), (20, 58), (50, 56), (80, 60), (100, 68), (100, 100), (0, 100)]))
    # Häuser
    m.f(rect(6, 54, 24, 24, 1.5))
    m.f(rpoly([(2, 56), (18, 38), (34, 56)], 1.5))
    m.f(rect(12, 62, 6, 8, 0.5), rect(22, 62, 5, 5, 0.5))
    m.f(rect(36, 46, 30, 32, 1.5))
    m.f(rpoly([(31, 48), (51, 24), (71, 48)], 1.5))
    m.f(rect(58, 22, 6, 12, 1))
    m.f(ell(61, 17, 4, 2.4), ell(66, 11, 3, 2))
    m.f(rect(41, 54, 8, 8, 0.5), rect(53, 54, 8, 8, 0.5))
    m.f(rect(45, 66, 12, 12, 5))
    m.f(rect(70, 56, 24, 22, 1.5))
    m.f(rpoly([(66, 58), (82, 40), (98, 58)], 1.5))
    m.f(rect(76, 64, 5, 14, 2), rect(85, 62, 6, 6, 0.5))
    # Schnee auf den Dächern
    m.f(rpoly([(10, 48), (18, 40), (26, 48)], 1)) if False else None
    # Tannen
    m.f(fir(84, 38, 64, 10, 2, 1), fir(94, 48, 70, 8, 2, 1)) if False else None
    m.f(fir(8, 62, 88, 10, 2, 1.2), fir(94, 66, 92, 9, 2, 1.2))
    # Vordergrund
    m.f(blob([(0, 86), (28, 80), (60, 84), (100, 82), (100, 100), (0, 100)]))
    # Schneemann
    m.f(ell(34, 94, 6, 5.5), ell(34, 86, 4.6, 4.2))
    m.f(rpoly([(34, 86), (40, 87), (34, 88)], 0.5)) if False else None
    # Weg
    m.f(rpoly([(47, 82), (53, 82), (72, 100), (30, 100)], 1.5))
    for x, y, r in [(22, 28, 3), (90, 26, 3), (30, 46, 2.5)]:
        m.dot((x, y, 1))
    return m


def build():
    return [schneemann(), schneeflocke(), muetze_schal(), handschuhe(), pinguin(),
            eisbaer(), schlitten(), iglu(), schneekugel(), winterdorf()]

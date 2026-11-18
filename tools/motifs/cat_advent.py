from dsl import *
EMOJI, DE, EN, COLOR = "🕯️", "Advent", "Advent", "#7B2D8E"


def flame(m, x, y, s=1.0):
    m.f(P([("M", [x, y - 8 * s]), ("C", [x + 6 * s, y - 1 * s, x + 5 * s, y + 5 * s, x, y + 5 * s]),
           ("C", [x - 5 * s, y + 5 * s, x - 6 * s, y - 1 * s, x, y - 8 * s]), ("Z", [])]))


def leaf(cx, cy, rx, ry, rot, n=5):
    pts = []
    for k in range(n * 2):
        a = math.radians(k * 180 / n)
        rr = 1 if k % 2 == 0 else 0.78
        pts.append((cx + rx * rr * math.cos(a), cy + ry * rr * math.sin(a)))
    pts = [(cx + rx * math.cos(math.radians(k * 360 / (n * 2))) * (1 if k % 2 == 0 else 0.8),
            cy + ry * math.sin(math.radians(k * 360 / (n * 2))) * (1 if k % 2 == 0 else 0.8)) for k in range(n * 2)]
    return rpoly(pts, 1.2).rot(rot, cx, cy)


def adventskranz():
    m = Motif("adventskranz", "Adventskranz", "Advent Wreath")
    for x, top in [(22, 30), (41, 22), (59, 22), (78, 30)]:
        m.f(rect(x - 5, top, 10, 56 - top, 2))
    m.f(ell(50, 68, 43, 24))
    m.f(ell(50, 68, 25, 11))
    for x, top in [(22, 30), (41, 22), (59, 22), (78, 30)]:
        m.l(line((x, top), (x, top - 4)))
        flame(m, x, top - 10, 0.9)
    for x, y in [(14, 70), (28, 82), (72, 82), (86, 70), (50, 50), (36, 52), (64, 52)]:
        m.f(ell(x, y, 3.2, 3.2))
    m.f(blob([(50, 86), (36, 78), (30, 90), (42, 92)]), blob([(50, 86), (64, 78), (70, 90), (58, 92)]))
    m.f(ell(50, 86, 5, 5))
    m.f(rpoly([(47, 90), (41, 98), (46, 98)], 0.5), rpoly([(53, 90), (59, 98), (54, 98)], 0.5))
    return m


def kerze():
    m = Motif("kerze", "Kerze", "Candle")
    m.f(ell(50, 90, 34, 7))
    m.f(rect(36, 40, 28, 50, 3))
    m.f(blob([(36, 44), (36, 54), (42, 58), (44, 48), (50, 46), (56, 46)]) if False else rect(36, 40, 28, 7, 3))
    m.f(blob([(40, 47), (42, 58), (47, 57), (47, 47)]))
    m.l(line((50, 40), (50, 33)))
    m.f(P([("M", [50, 6]), ("C", [62, 20, 60, 34, 50, 34]), ("C", [40, 34, 38, 20, 50, 6]), ("Z", [])]))
    m.f(P([("M", [50, 18]), ("C", [55, 25, 54, 31, 50, 31]), ("C", [46, 31, 45, 25, 50, 18]), ("Z", [])]))
    m.f(leaf(26, 80, 13, 6, -20), leaf(74, 80, 13, 6, 20), leaf(36, 86, 11, 5, 15), leaf(64, 86, 11, 5, -15))
    m.f(ell(48, 84, 3, 3), ell(54, 83, 3, 3), ell(51, 88, 3, 3))
    m.f(star(18, 20, 6, 2.4, 4, -90, 0.4), star(84, 28, 7, 2.8, 4, -90, 0.4), star(78, 10, 4, 1.6, 4, -90, 0.3))
    m.f(star(50, 66, 8, 3.4, 5, -90, 1))
    return m


def adventskalender():
    m = Motif("adventskalender", "Adventskalender", "Advent Calendar")
    m.f(rect(8, 20, 84, 76, 3))
    m.f(rpoly([(4, 22), (50, 4), (96, 22)], 2))
    m.f(star(50, 5, 7, 3, 5, -90, 0.8))
    cols, rows = 4, 6
    gx, gy = 3, 3
    x0, y0, w, h = 12, 25, 76, 67
    dw = (w - gx * (cols - 1)) / cols
    dh = (h - gy * (rows - 1)) / rows
    for r in range(rows):
        for c in range(cols):
            x = x0 + c * (dw + gx)
            y = y0 + r * (dh + gy)
            m.f(rect(x, y, dw, dh, 1.5))
            m.dot((x + dw - 3, y + dh / 2, 0.9))
    return m


def engel():
    m = Motif("engel", "Engel", "Angel")
    m.sym(blob([(42, 52), (16, 38), (4, 46), (8, 68), (34, 74)]))
    m.f(rpoly([(35, 52), (65, 52), (80, 94), (20, 94)], 5))
    m.f(rpoly([(35, 56), (65, 56), (66, 62), (34, 62)], 2))
    m.f(star(50, 76, 8, 3.4, 5, -90, 1))
    m.f(ell(32, 62, 5, 5), ell(68, 62, 5, 5))
    m.f(ell(50, 32, 15, 15))
    m.f(blob([(35, 32), (36, 18), (50, 14), (64, 18), (65, 32), (58, 25), (50, 23), (42, 25)]))
    m.f(ell(50, 8, 13, 4))
    m.dot((44, 33, 1.7), (56, 33, 1.7))
    m.l(arc(50, 38, 5, 3, 20, 160, 3))
    m.f(ell(39, 38, 3, 2), ell(61, 38, 3, 2))
    m.f(star(86, 52, 8, 3.4, 5, -90, 1))
    m.l(line((68, 60), (80, 56)))
    return m


def zuckerstange():
    m = Motif("zuckerstange", "Zuckerstange", "Candy Cane")
    ox = -8
    # Schaft in 6 Streifen
    y0, y1 = 34, 94
    n = 6
    for i in range(n):
        a = y0 + (y1 - y0) * i / n
        b = y0 + (y1 - y0) * (i + 1) / n
        m.f(rect(30 + ox, a, 12, b - a, 0))
    # Haken
    for k in range(3):
        m.f(annulus(52 + ox, 34, 10, 22, 180 + k * 60, 240 + k * 60, 5))
    m.f(rect(62 + ox, 34, 12, 8, 0))
    m.f(rect(62 + ox, 42, 12, 8, 0))
    # Schleife
    m.f(blob([(36 + ox, 62), (20 + ox, 52), (14 + ox, 64), (28 + ox, 68)]), blob([(36 + ox, 62), (52 + ox, 52), (58 + ox, 64), (44 + ox, 68)]))
    m.f(ell(36 + ox, 63, 4.5, 4.5))
    m.f(rpoly([(34 + ox, 66), (24 + ox, 82), (32 + ox, 80)], 0.5), rpoly([(38 + ox, 66), (48 + ox, 82), (40 + ox, 80)], 0.5))
    m.f(star(80, 70, 8, 3.4, 5, -90, 1), star(74, 88, 5, 2.2, 4, -90, 0.4), star(84, 20, 6, 2.4, 4, -90, 0.4))
    m.f(ell(14, 20, 3, 3), ell(10, 40, 2.4, 2.4), ell(88, 50, 2.6, 2.6))
    return m


def plaetzchen():
    m = Motif("plaetzchen", "Plätzchen", "Cookies")
    m.f(ell(50, 74, 46, 22))
    m.f(ell(50, 72, 34, 14))
    m.f(star(30, 38, 16, 7, 5, -90, 2))
    m.f(ell(30, 40, 4, 4))
    m.f(heart(58, 34, 11))
    m.f(ell(58, 38, 3, 3))
    m.f(fir(82, 18, 50, 13, 2, 1.5))
    m.f(ell(80, 34, 2.6, 2.6), ell(86, 42, 2.6, 2.6))
    m.f(ell(42, 66, 12, 12))
    m.f(ell(42, 66, 5, 5))
    m.f(star(66, 68, 11, 5, 5, -90, 1.5))
    m.f(ell(66, 69, 3, 3))
    m.f(rpoly([(22, 62), (36, 58), (38, 62), (24, 66)], 1.5)) if False else None
    m.f(ell(24, 70, 6, 6))
    m.f(ell(82, 70, 5, 5))
    return m


def bell_parts(s=1.0):
    body = P([("M", [24, 70]), ("C", [26, 48, 30, 20, 50, 16]), ("C", [70, 20, 74, 48, 76, 70]),
              ("L", [86, 80]), ("L", [14, 80]), ("Z", [])])
    band = rpoly([(29, 50), (71, 50), (73, 58), (27, 58)], 2)
    clap = ell(50, 86, 7, 7)
    top = ell(50, 13, 5, 5)
    return [p.scale(s, s, 50, 10) for p in (body, band, clap, top)]


def glocke():
    m = Motif("glocke", "Glocken", "Bells")
    for rot in (-20, 20):
        body, band, clap, top = [p.move(0, 14).rot(rot, 50, 22) for p in bell_parts(0.68)]
        m.f(body, band, clap, top)
        m.f(star(50, 66, 6, 2.6, 5, -90, 0.6).scale(0.68, 0.68, 50, 10).move(0, 14).rot(rot, 50, 22))
    m.f(blob([(50, 14), (30, 0), (20, 8), (32, 18)]), blob([(50, 14), (70, 0), (80, 8), (68, 18)]))
    m.f(ell(50, 14, 5, 5))
    m.f(leaf(34, 24, 10, 4.4, 30), leaf(66, 24, 10, 4.4, -30))
    m.f(ell(48, 22, 2.4, 2.4), ell(54, 22, 2.4, 2.4))
    return m


def stechpalme():
    m = Motif("stechpalme", "Stechpalme", "Holly")
    m.f(leaf(28, 50, 26, 12, -28, 6), leaf(72, 50, 26, 12, 28, 6), leaf(50, 26, 24, 11, 90, 6))
    m.l(line((12, 62), (46, 50)), line((88, 62), (54, 50)), line((50, 42), (50, 12)))
    m.f(ell(44, 52, 7, 7), ell(57, 52, 7, 7), ell(50, 62, 7, 7))
    m.f(blob([(50, 78), (30, 70), (22, 84), (40, 90)]), blob([(50, 78), (70, 70), (78, 84), (60, 90)]))
    m.f(ell(50, 80, 6, 6))
    m.f(rpoly([(46, 84), (36, 100), (45, 98)], 0.5), rpoly([(54, 84), (64, 100), (55, 98)], 0.5))
    return m


def nussknacker():
    m = Motif("nussknacker", "Nussknacker", "Nutcracker")
    m.f(rect(36, 72, 11, 20, 2), rect(53, 72, 11, 20, 2))
    m.f(rect(33, 88, 14, 9, 2), rect(53, 88, 14, 9, 2))
    m.f(rect(16, 42, 12, 30, 5), rect(72, 42, 12, 30, 5))
    m.f(ell(22, 76, 6, 6), ell(78, 76, 6, 6))
    m.f(rpoly([(30, 44), (70, 44), (72, 76), (28, 76)], 3))
    m.f(rect(28, 66, 44, 8, 1))
    m.f(rect(46, 66, 8, 8, 1))
    for y in (50, 57):
        m.f(ell(50, y, 2.6, 2.6))
    m.f(ell(28, 44, 9, 4.5), ell(72, 44, 9, 4.5))
    m.f(ell(50, 32, 14, 15))
    m.f(rect(34, 2, 32, 22, 3))
    m.f(rect(34, 18, 32, 6, 0))
    m.f(star(50, 11, 5, 2.2, 5, -90, 0.5))
    m.dot((44, 30, 1.8), (56, 30, 1.8))
    m.f(ell(38, 36, 3, 2), ell(62, 36, 3, 2))
    m.f(blob([(50, 38), (40, 34), (32, 38), (38, 42), (50, 41)]), blob([(50, 38), (60, 34), (68, 38), (62, 42), (50, 41)]))
    m.f(rect(43, 43, 14, 6, 2))
    return m


def weihnachtsstern():
    m = Motif("weihnachtsstern", "Weihnachtsstern", "Poinsettia")
    m.f(rpoly([(32, 78), (68, 78), (63, 98), (37, 98)], 3))
    m.f(rect(29, 72, 42, 9, 3))
    for i in range(6):
        m.f(petal(6, 36, 13, 50, 40).rot(i * 60, 50, 40))
    for i in range(6):
        m.f(petal(4, 26, 10, 50, 40).rot(i * 60 + 30, 50, 40))
    for i in range(6):
        a = math.radians(i * 60)
        m.f(ell(50 + 7 * math.cos(a), 40 + 7 * math.sin(a), 3, 3))
    m.f(ell(50, 40, 3, 3))
    return m


def build():
    return [adventskranz(), kerze(), adventskalender(), engel(), zuckerstange(),
            plaetzchen(), glocke(), stechpalme(), nussknacker(), weihnachtsstern()]

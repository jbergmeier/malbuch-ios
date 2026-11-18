from dsl import *
EMOJI, DE, EN, COLOR = "🎄", "Weihnachten", "Christmas", "#C1121F"


def tannenbaum():
    m = Motif("tannenbaum", "Tannenbaum", "Christmas Tree")
    m.f(rect(0, 92, 100, 8, 0))
    m.f(rect(43, 80, 14, 14, 2))
    m.f(fir(50, 44, 84, 38, 4, 2))
    m.f(fir(50, 24, 62, 30, 3, 2))
    m.f(fir(50, 8, 40, 22, 3, 2))
    m.f(star(50, 8, 8, 3.6, 5, -90, 1))
    for x, y in [(38, 76), (62, 72), (50, 58), (42, 48), (58, 34), (45, 28)]:
        m.f(ell(x, y, 3.8, 3.8))
    return m


def stern():
    m = Motif("stern", "Weihnachtsstern", "Christmas Star")
    m.f(star(50, 52, 42, 19, 5, -90, 3))
    m.f(star(50, 52, 24, 11, 5, -90, 2))
    m.f(ell(50, 52, 5, 5))
    for x, y, s in [(14, 16, 8), (88, 14, 7), (90, 82, 7), (12, 86, 6)]:
        m.f(star(x, y, s, s * 0.3, 4, -90, 0.5))
    return m


def kugel():
    m = Motif("kugel", "Christbaumkugel", "Bauble")
    m.l(arc(50, 8, 8, 8, 180, 360, 6))
    m.f(rect(41, 14, 18, 10, 2))
    m.f(ell(50, 58, 36, 36))
    m.f(star(50, 58, 21, 10, 8, -90, 1.5))
    m.f(ell(50, 58, 5, 5))
    for i in range(8):
        a = math.radians(i * 45 + 22.5)
        m.f(ell(50 + 29 * math.cos(a), 58 + 29 * math.sin(a), 3, 3))
    return m


def lebkuchenmann():
    m = Motif("lebkuchenmann", "Lebkuchenmann", "Gingerbread Man")
    m.f(rpoly([(8, 42), (34, 40), (36, 54), (12, 58)], 5))
    m.f(rpoly([(92, 42), (66, 40), (64, 54), (88, 58)], 5))
    m.f(rpoly([(33, 64), (49, 64), (47, 94), (29, 94)], 5))
    m.f(rpoly([(67, 64), (51, 64), (53, 94), (71, 94)], 5))
    m.f(rect(31, 36, 38, 36, 9))
    m.f(ell(50, 22, 17, 16))
    m.eye(43, 20, 0.01, 1.7, 0, 0) if False else None
    m.dot((43, 19, 1.8), (57, 19, 1.8))
    m.l(arc(50, 25, 7, 4, 20, 160, 4))
    m.f(ell(36, 26, 3.4, 2.4), ell(64, 26, 3.4, 2.4))
    m.f(rpoly([(50, 40), (38, 35), (38, 45)], 1.5), rpoly([(50, 40), (62, 35), (62, 45)], 1.5))
    m.f(ell(50, 40, 3.2, 3.2))
    for y in (52, 61, 70):
        m.f(ell(50, y, 3.4, 3.4))
    m.l(curve([(10, 50), (16, 46), (22, 52), (28, 46)]), curve([(90, 50), (84, 46), (78, 52), (72, 46)]))
    m.l(curve([(32, 88), (36, 84), (40, 90), (44, 84)]), curve([(68, 88), (64, 84), (60, 90), (56, 84)]))
    return m


def stiefel():
    m = Motif("stiefel", "Nikolausstiefel", "Santa's Boot")
    m.f(ell(40, 8, 7, 7))
    m.l(line((40, 15), (40, 24)))
    m.f(rect(54, 2, 14, 16, 2))
    m.f(rect(59, 2, 4, 16, 0))
    m.f(rpoly([(36, 24), (64, 24), (64, 60), (84, 66), (91, 80), (88, 91), (36, 91)], 5))
    m.f(rpoly([(36, 82), (89, 82), (88, 91), (36, 91)], 3))
    m.f(rect(31, 12, 38, 16, 7))
    for x in (36, 46, 56, 64):
        m.f(ell(x, 12, 5, 4))
    m.f(star(50, 46, 9, 4, 5, -90, 1))
    m.f(ell(76, 72, 3.4, 3.4))
    return m


def geschenk():
    m = Motif("geschenk", "Geschenk", "Present")
    m.f(rect(14, 46, 72, 44, 3))
    m.f(rect(10, 34, 80, 15, 3))
    m.f(rect(43, 49, 14, 41, 0))
    m.f(rect(43, 34, 14, 15, 0))
    m.f(blob([(50, 32), (36, 12), (22, 14), (28, 30)]), blob([(50, 32), (64, 12), (78, 14), (72, 30)]))
    m.f(ell(50, 33, 6, 5))
    m.l(curve([(48, 36), (42, 46)]), curve([(52, 36), (58, 46)]))
    m.f(star(28, 66, 6, 2.6, 5, -90, 0.5), star(72, 66, 6, 2.6, 5, -90, 0.5))
    m.f(ell(28, 82, 3, 3), ell(72, 82, 3, 3))
    return m


def weihnachtsmann():
    m = Motif("weihnachtsmann", "Weihnachtsmann", "Santa Claus")
    m.f(blob([(22, 40), (28, 18), (46, 6), (66, 8), (82, 22), (92, 30), (84, 44)]))
    m.f(ell(90, 30, 8, 8))
    m.f(ell(50, 60, 26, 25))
    m.f(rect(18, 34, 64, 15, 7))
    m.f(blob([(24, 58), (20, 78), (34, 94), (50, 98), (66, 94), (80, 78), (76, 58), (62, 68), (50, 64), (38, 68)]))
    m.f(blob([(50, 66), (42, 62), (32, 66), (30, 72), (42, 72)]), blob([(50, 66), (58, 62), (68, 66), (70, 72), (58, 72)]))
    m.f(ell(50, 62, 6, 5))
    m.dot((40, 55, 2), (60, 55, 2))
    m.l(curve([(35, 49), (40, 46), (46, 48)]) if False else line((34, 52), (46, 52)))
    m.l(curve([(46, 82), (50, 84), (54, 82)]))
    m.f(ell(33, 64, 4.4, 3), ell(67, 64, 4.4, 3))
    return m


def rentier():
    m = Motif("rentier", "Rentier", "Reindeer")
    for ant in (bar(38, 42, 22, 6, 6), bar(32, 30, 14, 24, 5), bar(27, 18, 11, 10, 5)):
        m.f(ant, ant.flip())
    m.f(ell(24, 44, 8, 4.5).rot(-25, 24, 44), ell(76, 44, 8, 4.5).rot(25, 76, 44))
    m.f(ell(50, 58, 23, 27))
    m.f(ell(50, 78, 14, 12))
    m.f(ell(50, 82, 7, 5.5))
    m.eye(38, 54, 5, 2.2, 0.5, 0.4), m.eye(62, 54, 5, 2.2, -0.5, 0.4)
    m.f(ell(34, 68, 4, 2.6), ell(66, 68, 4, 2.6))
    return m


def weihnachtsbaum_deko():
    m = Motif("weihnachtsbaum_deko", "Geschmückter Baum", "Decorated Tree")
    m.f(rect(0, 94, 100, 6, 0))
    m.f(rect(43, 76, 14, 18, 2))
    m.f(fir(50, 54, 80, 40, 5, 2))
    m.f(fir(50, 34, 62, 32, 4, 2))
    m.f(fir(50, 16, 44, 24, 3, 2))
    m.f(star(50, 9, 9, 4, 5, -90, 1))
    # Kugeln
    for x, y, r in [(42, 28, 3.6), (58, 26, 3.4), (50, 50, 4.2), (36, 54, 3.8), (64, 55, 3.8),
                    (26, 74, 4.2), (44, 72, 4.2), (60, 76, 4.2), (76, 72, 4.2), (18, 82, 3.4), (84, 82, 3.4)]:
        m.f(ell(x, y, r, r))
    m.f(ell(36, 42, 2.8, 2.8), ell(64, 44, 2.8, 2.8), ell(50, 70, 3.2, 3.2), ell(16, 78, 2.8, 2.8), ell(84, 78, 2.8, 2.8))
    m.f(star(32, 66, 4.4, 2, 5, -90, 0.5), star(70, 66, 4.4, 2, 5, -90, 0.5), star(52, 62, 3.6, 1.6, 5, -90, 0.5))
    # Geschenke
    m.f(rect(6, 83, 20, 13, 1.5), rect(74, 81, 20, 15, 1.5), rect(62, 87, 10, 9, 1.5))
    m.f(rect(14, 83, 4, 13, 0), rect(82, 81, 4, 15, 0))
    return m


def lebkuchenhaus():
    m = Motif("lebkuchenhaus", "Lebkuchenhaus", "Gingerbread House")
    m.f(rect(0, 88, 100, 12, 0))
    m.f(rect(66, 14, 10, 24, 2))
    m.f(rect(18, 46, 64, 42, 2))
    m.f(rpoly([(8, 50), (50, 12), (92, 50)], 3))
    for x, y in [(44, 26), (56, 26), (38, 34), (50, 34), (62, 34), (30, 42), (42, 42), (54, 42), (66, 42)]:
        m.f(ell(x, y, 5, 4))
    m.f(rect(8, 46, 84, 6, 3))
    m.f(rect(42, 62, 16, 26, 8))
    m.f(rect(24, 58, 14, 14, 2), rect(62, 58, 14, 14, 2))
    m.l(line((31, 58), (31, 72)), line((24, 65), (38, 65)), line((69, 58), (69, 72)), line((62, 65), (76, 65)))
    m.dot((54, 76, 1.4))
    for x in (20, 32, 44, 56, 68, 80):
        m.f(ell(x, 53, 2.6, 2.6))
    m.f(rpoly([(22, 76), (36, 76), (36, 86), (22, 86)], 1)) if False else None
    m.f(star(12, 80, 6, 2.6, 5, -90, 0.5), star(88, 78, 6, 2.6, 5, -90, 0.5))
    m.f(ell(70, 10, 6, 3.5), ell(78, 4, 4, 2.4))
    return m


def build():
    return [tannenbaum(), stern(), kugel(), lebkuchenmann(), stiefel(), geschenk(),
            weihnachtsmann(), rentier(), weihnachtsbaum_deko(), lebkuchenhaus()]

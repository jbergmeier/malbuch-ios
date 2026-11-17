from dsl import *
EMOJI, DE, EN, COLOR = "🚀", "Weltraum", "Space", "#3A0CA3"

def stars(m, *pts):
    for x, y, r in pts: m.f(star(x, y, r, r * 0.45, 4))

def rakete():
    m = Motif("rakete", "Rakete", "Rocket")
    stars(m,(16,18,5),(86,26,4),(80,78,4),(14,70,3.5))
    m.sym(rpoly([(34,62),(14,84),(14,70),(26,50)],3).move(0,0))
    m.f(blob([(40,76),(50,98),(60,76),(54,80),(50,88),(46,80)]))   # flame
    m.f(blob([(50,4),(66,22),(68,50),(66,78),(34,78),(32,50),(34,22)]))
    m.f(rpoly([(34,22),(50,2),(66,22),(50,26)],4)) if False else None
    m.f(ell(50,40,9,9)); m.f(ell(50,40,5,5))
    m.f(rect(34,64,32,8,1))
    return m

def saturn():
    m = Motif("saturn", "Saturn", "Saturn")
    stars(m,(14,18,5),(88,16,4),(12,84,4),(90,80,5))
    m.f(ell(50,50,42,12).rot(-20))
    m.f(ell(50,50,26,26))
    m.f(ell(50,50,16,16))
    outer = [(50+42*math.cos(math.radians(t)), 50+12*math.sin(math.radians(t))) for t in range(0,181,15)]
    inner = [(50+31*math.cos(math.radians(t)), 50+8*math.sin(math.radians(t))) for t in range(180,-1,-15)]
    m.f(rpoly(outer+inner,0).rot(-20))
    return m

def ufo():
    m = Motif("ufo", "Ufo", "UFO")
    stars(m,(14,16,5),(88,20,4),(84,86,4),(12,80,4))
    m.f(rpoly([(38,70),(26,96),(74,96),(62,70)],0)) if False else None
    m.f(rpoly([(40,64),(26,92),(74,92),(60,64)],2))
    m.f(P([("M",[34,48]),("C",[34,16,66,16,66,48]),("Z",[])]))
    m.f(ell(50,28,6,7)) if False else None
    m.f(ell(50,54,46,13))
    for x in (20,35,50,65,80): m.f(ell(x,56,4,4))
    m.eye(50,34,6,2.6,0,0.6) if False else None
    m.f(ell(50,32,9,9)); m.dot((50,33,3))
    return m

def astronaut():
    m = Motif("astronaut", "Astronaut", "Astronaut")
    stars(m,(12,14,5),(90,22,4),(10,64,3.5),(92,70,4))
    m.f(rect(26,40,48,34,10))   # backpack
    m.sym(rect(16,46,14,34,7).rot(0))
    m.f(rect(32,40,36,38,10))
    m.sym(rect(32,76,14,20,6))
    m.f(ell(50,26,22,22))
    m.f(rect(34,16,32,22,10))
    m.dot((42,26,2.6),(58,26,2.6)) 
    m.l(arc(50,30,5,3,20,160,4))
    m.f(rect(41,50,18,12,2)); m.f(ell(46,56,2.2,2.2), ell(54,56,2.2,2.2))
    return m

def mond():
    m = Motif("mond", "Mond", "Moon")
    stars(m,(14,14,5),(84,14,4),(88,84,5),(12,86,4),(50,8,3))
    m.f(P([("M",[62,10]),("C",[24,12,18,76,62,90]),("C",[40,70,42,30,62,10]),("Z",[])]).scale(1.0).move(0,0) if False else P([("M",[66,8]),("C",[22,8,14,78,66,92]),("C",[34,76,34,24,66,8]),("Z",[])]))
    m.eye(40,50,3,1.2,0,0.3) if False else None
    m.f(ell(72,40,3,3)) if False else None
    m.f(ell(24,50,0.01,0.01)) if False else None
    return m

def alien():
    m = Motif("alien", "Außerirdischer", "Alien")
    stars(m,(14,14,5),(88,18,4),(86,86,4),(12,86,4))
    m.l(line((38,22),(30,6)), line((62,22),(70,6)))
    m.f(ell(30,5,4,4), ell(70,5,4,4))
    m.f(blob([(14,44),(24,22),(50,14),(76,22),(86,44),(76,70),(50,84),(24,70)]))
    m.f(blob([(18,44),(24,34),(42,44),(34,58),(22,56)]).move(0,0) if False else ell(33,46,11,14).rot(20,33,46))
    m.f(ell(67,46,11,14).rot(-20,67,46))
    m.dot((34,48,4),(66,48,4)); m.dot((36,45,1.4),(68,45,1.4))
    m.l(arc(50,64,9,5,20,160,4))
    m.dot((47,56,0.9),(53,56,0.9))
    return m

def satellit():
    m = Motif("satellit", "Satellit", "Satellite")
    stars(m,(12,14,5),(88,12,4),(84,88,4),(14,84,4))
    m.f(rect(2,40,30,20,2)); m.f(rect(68,40,30,20,2))
    m.l(line((12,40),(12,60)), line((22,40),(22,60)), line((78,40),(78,60)), line((88,40),(88,60)))
    m.f(rect(32,48,36,4,1))
    m.f(rect(36,34,28,32,6).rot(0))
    m.f(ell(50,50,9,9)); m.f(ell(50,50,4,4))
    m.l(line((50,34),(50,20)))
    m.f(ell(50,17,4,4))
    return m

def erde():
    m = Motif("erde", "Erde", "Earth")
    stars(m,(12,14,5),(90,18,4),(86,88,4),(10,86,3.5))
    m.f(ell(50,50,40,40))
    m.f(blob([(24,34),(36,22),(48,28),(44,44),(32,52),(22,46)]))
    m.f(blob([(56,56),(72,50),(78,66),(66,80),(56,70)]))
    m.f(blob([(54,24),(64,20),(70,30),(60,36)]))
    return m

def build():
    return [rakete(), saturn(), ufo(), astronaut(), mond(), alien(), satellit(), erde()]

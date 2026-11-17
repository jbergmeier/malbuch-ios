from dsl import *
EMOJI, DE, EN, COLOR = "🌻", "Natur", "Nature", "#06D6A0"

def blume():
    m = Motif("blume", "Blume", "Flower")
    m.f(rect(0,90,100,10,0))
    m.f(rect(47,50,6,42,2))
    m.f(blob([(53,74),(70,60),(84,64),(72,80)]), blob([(47,66),(30,52),(16,56),(28,72)]))
    for i in range(8): m.f(petal(8,34,12,50,38).rot(i*45,50,38))
    m.f(ell(50,38,12,12))
    m.dot((46,36,1.6),(54,36,1.6),(50,42,1.6))
    return m

def sonnenblume():
    m = Motif("sonnenblume", "Sonnenblume", "Sunflower")
    m.f(rect(0,92,100,8,0))
    m.f(rect(46,54,8,40,2))
    m.f(blob([(54,78),(76,62),(92,70),(76,86)]), blob([(46,70),(24,56),(8,62),(24,78)]))
    for i in range(14): m.f(petal(10,34,8,50,42).rot(i*360/14,50,42))
    m.f(ell(50,42,13,13)); m.f(ell(50,42,7,7))
    return m

def baum():
    m = Motif("baum", "Baum", "Tree")
    m.f(rect(0,88,100,12,0))
    m.f(ell(84,14,8,8))
    m.f(rpoly([(42,90),(45,48),(55,48),(58,90)],2))
    m.f(blob([(48,64),(36,54),(30,46),(36,50),(48,54)]) if False else rpoly([(48,66),(36,50),(32,52),(46,70)],1.5))
    m.f(blob([(50,4),(66,8),(78,18),(92,28),(94,44),(84,56),(64,62),(36,62),(16,56),(6,44),(8,28),(22,18),(34,8)]))
    for x,y in [(36,24),(58,18),(70,38),(24,42),(48,40),(40,52),(62,54)]: m.f(ell(x,y,4.5,4.5))
    return m

def schmetterling():
    m = Motif("schmetterling", "Schmetterling", "Butterfly")
    m.sym(blob([(46,44),(30,10),(8,12),(8,38),(24,50),(46,52)]))
    m.sym(blob([(46,54),(24,56),(14,76),(26,92),(42,76)]))
    m.sym(ell(24,28,6,6)); m.sym(ell(28,76,5,5))
    m.f(ell(50,50,6,26))
    m.l(curve([(48,24),(42,12),(36,8)]), curve([(52,24),(58,12),(64,8)]))
    m.f(ell(36,8,2.4,2.4)) ; m.f(ell(64,8,2.4,2.4))
    return m

def pilz():
    m = Motif("pilz", "Pilz", "Mushroom")
    m.f(rect(0,90,100,10,0))
    m.f(blob([(36,92),(40,60),(60,60),(64,92)]))
    m.f(P([("M",[8,62]),("C",[6,8,94,8,92,62]),("C",[70,70,30,70,8,62]),("Z",[])]))
    m.f(ell(30,40,8,8), ell(62,28,7,7), ell(74,50,6,6), ell(48,50,5,5))
    m.eye(45,76,2.6,1.2,0.3,0.2) if False else None
    m.dot((45,76,1.6),(55,76,1.6)); m.l(arc(50,80,4,2.4,20,160,3))
    return m

def marienkaefer():
    m = Motif("marienkaefer", "Marienkäfer", "Ladybug")
    m.sym(line((30,70),(14,80)).map(lambda x,y:(x,y)) if False else ell(30,12,0.01,0.01)) if False else None
    m.l(line((22,40),(8,34)), line((22,52),(6,52)), line((24,66),(10,76)), line((78,40),(92,34)), line((78,52),(94,52)), line((76,66),(90,76)))
    m.f(ell(50,18,15,13))
    m.l(curve([(44,8),(38,2)]), curve([(56,8),(62,2)]))
    m.f(ell(50,56,32,36))
    m.l(line((50,20),(50,92)))
    m.f(ell(34,42,6,6), ell(66,42,6,6), ell(30,64,5,5), ell(70,64,5,5), ell(40,82,4,4), ell(60,82,4,4))
    m.eye(45,16,3,1.3,0.4,0.2), m.eye(55,16,3,1.3,-0.4,0.2)
    return m

def regenbogen():
    m = Motif("regenbogen", "Regenbogen", "Rainbow")
    m.f(rect(0,90,100,10,0)) if False else None
    for r in (46,38,30,22,14):
        m.f(P([("M",[50-r,84]),("C",[50-r,50-r*1.1,50+r,50-r*1.1,50+r,84]),("Z",[])]).move(0,0))
    m.f(cloud(16,82,1.0)); m.f(cloud(82,82,1.0))
    m.f(ell(86,12,7,7))
    return m

def biene():
    m = Motif("biene", "Biene", "Bee")
    m.f(ell(36,34,16,22).rot(-30,36,34)), m.f(ell(60,30,16,22).rot(30,60,30))
    m.f(ell(54,56,32,24))
    m.f(rect(46,34,6,44,0).rot(0)) if False else None
    for x in (46,58,70): m.f(rpoly([(x-3,36),(x+3,36),(x+4,76),(x-4,76)],1).move(0,0)) if False else None
    m.f(rpoly([(42,38),(50,34),(50,78),(42,74)],2)); m.f(rpoly([(58,34),(66,38),(66,76),(58,78)],2))
    m.f(rpoly([(14,56),(24,62),(24,50)],1.5))
    m.f(ell(82,52,13,13))
    m.eye(86,49,3.6,1.6,0.4,0.2)
    m.l(arc(86,56,4,2.5,20,160,3))
    m.l(curve([(80,40),(78,30),(72,26)]), curve([(88,40),(92,30),(98,28)]))
    return m

def build():
    return [blume(), sonnenblume(), baum(), schmetterling(), pilz(), marienkaefer(), regenbogen(), biene()]

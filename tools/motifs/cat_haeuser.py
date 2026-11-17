from dsl import *
EMOJI, DE, EN, COLOR = "🏠", "Häuser", "Houses", "#EF476F"

def ground(m, y=90):
    m.f(rect(0, y, 100, 100 - y, 0))

def win(m, x, y, w=10, h=12):
    m.f(rect(x, y, w, h, 1.5))
    m.l(line((x + w/2, y), (x + w/2, y + h)), line((x, y + h/2), (x + w, y + h/2)))

def haus():
    m = Motif("haus", "Haus", "House")
    m.f(ell(84,16,8,8))
    m.f(cloud(26,16,1.0))
    ground(m, 88)
    m.f(rect(26,48,50,40,1))
    m.f(rpoly([(20,50),(51,22),(82,50)],2))
    m.f(rect(60,26,8,16,1))
    m.f(rect(41,62,16,26,8)) if False else None
    m.f(rpoly([(42,88),(42,68),(46,63),(54,63),(58,68),(58,88)],1))
    win(m,30,58,10,10); win(m,62,58,10,10)
    m.f(ell(51,44,5,5))
    m.f(blob([(86,88),(86,66),(94,56),(98,70),(98,88)])) if False else None
    return m

def schloss():
    m = Motif("schloss", "Schloss", "Castle")
    ground(m, 90)
    m.f(rect(30,44,40,46,1))
    m.f(rect(10,36,20,54,1)); m.f(rect(70,36,20,54,1))
    m.f(rpoly([(8,36),(20,10),(32,36)],2)); m.f(rpoly([(68,36),(80,10),(92,36)],2))
    m.f(rect(36,32,28,12,1))
    for x in (30,40,50,60): m.f(rect(x,28,6,8,1)) if x < 60 else m.f(rect(x,28,6,8,1))
    m.f(rpoly([(40,90),(40,68),(44,60),(56,60),(60,68),(60,90)],1))
    m.f(rpoly([(14,60),(14,52),(18,48),(22,52),(22,60)],1)); m.f(rpoly([(78,60),(78,52),(82,48),(86,52),(86,60)],1))
    m.f(rpoly([(14,76),(14,68),(18,64),(22,68),(22,76)],1)); m.f(rpoly([(78,76),(78,68),(82,64),(86,68),(86,76)],1))
    m.f(rpoly([(20,10),(20,2),(30,6),(20,6)],0.5)); m.f(rpoly([(80,10),(80,2),(90,6),(80,6)],0.5))
    m.l(line((20,10),(20,2)), line((80,10),(80,2)))
    m.f(ell(50,48,5,5))
    return m

def hochhaus():
    m = Motif("hochhaus", "Hochhaus", "Skyscraper")
    ground(m, 90)
    m.f(rect(6,50,22,40,1)); m.f(rect(72,44,22,46,1))
    m.f(rect(30,16,40,74,1))
    m.f(rpoly([(30,16),(50,4),(70,16)],1))
    m.l(line((50,4),(50,0)))
    for r in range(5):
        for c in range(3):
            m.f(rect(35+c*11,24+r*12,7,8,1))
    for r in range(3): m.f(rect(10,56+r*11,6,7,1)), m.f(rect(19,56+r*11,6,7,1)), m.f(rect(76,52+r*12,6,7,1)), m.f(rect(85,52+r*12,6,7,1))
    m.f(rpoly([(44,90),(44,80),(56,80),(56,90)],1))
    m.f(star(18,26,5,2.2,4), star(84,22,4,1.8,4))
    return m

def leuchtturm():
    m = Motif("leuchtturm", "Leuchtturm", "Lighthouse")
    m.f(rect(0,78,100,22,0))
    m.f(blob([(0,84),(20,80),(40,86),(60,80),(80,86),(100,82),(100,100),(0,100)]))
    m.f(rpoly([(36,88),(40,34),(60,34),(64,88)],1))
    m.f(rpoly([(38.4,66),(61.6,66),(63,78),(37,78)],0.5))
    m.f(rpoly([(40,34),(60,34),(60.8,46),(39.2,46)],0.5)) if False else None
    m.f(rect(32,30,36,6,2))
    m.f(rect(40,18,20,12,2))
    m.f(rpoly([(38,18),(50,6),(62,18)],2))
    m.f(rpoly([(60,24),(98,12),(98,36)],1)) ; m.f(rpoly([(40,24),(2,12),(2,36)],1))
    m.f(rect(45,52,10,12,5))
    m.f(rpoly([(44,88),(44,76),(56,76),(56,88)],4))
    return m

def scheune():
    m = Motif("scheune", "Bauernhof", "Farm")
    m.f(ell(84,16,8,8))
    ground(m, 88)
    m.f(rpoly([(14,50),(14,88),(78,88),(78,50),(66,34),(46,24),(26,34)],1))
    m.f(rect(36,54,28,34,1)); m.l(line((50,54),(50,88)), line((36,54),(64,88)), line((64,54),(36,88)))
    m.f(rpoly([(42,42),(50,34),(58,42),(50,50)],1))
    m.f(rect(80,40,14,48,7)) ; m.f(rpoly([(78,40),(87,30),(96,40)],1))
    m.f(ell(87,52,2,2)) if False else None
    m.f(blob([(2,88),(6,78),(10,88)])) if False else None
    return m

def dome(cx, base, w, hgt):
    k = 0.6
    return P([("M",[cx-w,base]),("C",[cx-w,base-hgt*1.3,cx+w,base-hgt*1.3,cx+w,base]),("Z",[])])

def iglu():
    m = Motif("iglu", "Iglu", "Igloo")
    m.f(star(14,22,5,2,4), star(86,30,4,1.6,4), star(60,10,3,1.3,4))
    m.f(rect(0,80,100,20,0))
    m.f(dome(50,82,42,50))
    m.f(dome(50,82,30,36))
    m.f(dome(50,82,18,20))
    m.f(rect(34,66,32,16,8)) if False else None
    m.f(P([("M",[34,82]),("L",[34,70]),("C",[34,58,66,58,66,70]),("L",[66,82]),("Z",[])]))
    m.f(P([("M",[40,82]),("L",[40,72]),("C",[40,64,60,64,60,72]),("L",[60,82]),("Z",[])]))
    m.f(ell(22,92,6,3), ell(76,92,7,3))
    return m

def baumhaus():
    m = Motif("baumhaus", "Baumhaus", "Tree House")
    m.f(rect(0,90,100,10,0))
    m.f(rpoly([(42,90),(46,50),(58,50),(62,90)],2))
    m.f(ell(50,26,34,24)); m.f(ell(24,34,18,14)); m.f(ell(78,36,18,14))
    m.f(rect(26,50,48,5,1))
    m.f(rect(32,32,36,20,1))
    m.f(rpoly([(28,34),(50,16),(72,34)],2))
    win(m,38,38,9,9); m.f(rpoly([(54,52),(54,44),(58,40),(62,44),(62,52)],1))
    m.f(rect(60,56,3,34,1)) if False else None
    m.l(line((46,56),(46,90)))
    for y in (62,72,82): m.f(rect(40,y,10,3,1))
    m.f(ell(14,52,3,3), ell(88,52,3,3), ell(76,14,3,3))
    return m

def muehle():
    m = Motif("muehle", "Windmühle", "Windmill")
    m.f(rect(0,88,100,12,0))
    m.f(rpoly([(34,88),(40,40),(60,40),(66,88)],2))
    m.f(rpoly([(38,40),(50,24),(62,40)],2))
    m.f(rpoly([(44,88),(44,70),(50,64),(56,70),(56,88)],1))
    m.f(rect(44,48,12,12,1))
    # blades
    for a in (45,135,225,315):
        m.f(rect(48,4,5,23,1).rot(a,50,32)) if False else None
    for a in (0,90,180,270):
        m.f(rpoly([(50,32),(60,2),(70,4),(50,32)],0.5).rot(a+20,50,32) if False else rpoly([(52,30),(58,6),(70,12),(70,20),(52,32)],1).rot(a,50,32))
    m.f(ell(50,32,4,4))
    return m

def build():
    return [haus(), schloss(), hochhaus(), leuchtturm(), scheune(), iglu(), baumhaus(), muehle()]

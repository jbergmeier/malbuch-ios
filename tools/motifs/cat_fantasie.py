from dsl import *
EMOJI, DE, EN, COLOR = "🦄", "Fantasie", "Fantasy", "#F15BB5"

def einhorn():
    m = Motif("einhorn", "Einhorn", "Unicorn")
    m.sym(rpoly([(26,38),(24,12),(44,28)],3))
    m.sym(ell(20,48,0.01,0.01)) if False else None
    m.f(blob([(14,40),(8,60),(14,86),(26,72),(24,54)]), blob([(86,40),(92,60),(86,86),(74,72),(76,54)]))
    m.f(ell(50,60,30,32))
    m.f(rpoly([(42,32),(50,2),(58,32)],2))
    m.l(line((44,24),(56,20)), line((46,14),(54,12)))
    m.f(blob([(40,30),(30,26),(24,38),(34,44)]), blob([(60,30),(70,26),(76,38),(66,44)]))
    m.eye(38,54,5,2.2,0.5,0.4), m.eye(62,54,5,2.2,-0.5,0.4)
    m.f(ell(50,72,15,11)); m.dot((45,72,1.6),(55,72,1.6))
    m.l(arc(50,78,6,3,20,160,3))
    m.f(ell(30,66,4,2.6), ell(70,66,4,2.6))
    return m

def drache():
    m = Motif("drache", "Drache", "Dragon")
    m.sym(blob([(26,50),(6,40),(0,22),(14,26),(24,16),(32,32)]))
    m.sym(rpoly([(34,34),(30,10),(48,26)],3))
    m.f(ell(50,58,30,32))
    for x in (38,50,62): m.f(rpoly([(x-5,28),(x,14),(x+5,28)],2)) if False else None
    m.eye(38,50,6,2.6,0.5,0.4), m.eye(62,50,6,2.6,-0.5,0.4)
    m.f(blob([(30,66),(50,60),(70,66),(72,86),(50,94),(28,86)]))
    m.dot((43,72,2.2),(57,72,2.2))
    m.l(line((38,82),(62,82)))
    m.f(rpoly([(42,82),(45,88),(48,82)],0.5), rpoly([(52,82),(55,88),(58,82)],0.5))
    m.f(blob([(50,22),(44,14),(50,6),(56,14)])) if False else None
    m.f(rpoly([(46,38),(50,28),(54,38)],1.5))
    m.l(curve([(36,40),(34,30)]), curve([(64,40),(66,30)])) if False else None
    return m

def roboter():
    m = Motif("roboter", "Roboter", "Robot")
    m.l(line((50,16),(50,6)))
    m.f(ell(50,5,4,4))
    m.sym(rect(0,44,18,30,4)) if False else None
    m.f(rect(26,18,48,34,8))
    m.sym(rect(10,60,16,10,5)) if False else None
    m.f(rect(30,56,40,34,6))
    m.sym(rect(10,58,16,28,8)); 
    m.sym(rect(32,88,14,10,3))
    m.f(rect(36,26,10,10,3)) if False else None
    m.f(ell(40,32,6,6)); m.f(ell(60,32,6,6)); m.dot((40,32,2.6),(60,32,2.6))
    m.f(rect(38,42,24,6,3))
    m.l(line((46,42),(46,48)), line((54,42),(54,48)))
    m.f(ell(50,72,10,10)); m.f(ell(50,72,5,5))
    m.f(rect(36,60,6,4,1), rect(58,60,6,4,1))
    m.sym(ell(6,34,4,4)) if False else None
    m.f(rect(22,30,4,10,2), rect(74,30,4,10,2))
    return m

def krone():
    m = Motif("krone", "Krone", "Crown")
    m.f(rpoly([(8,34),(28,52),(50,18),(72,52),(92,34),(84,80),(16,80)],4))
    m.f(rect(14,78,72,12,4))
    m.f(ell(8,32,5,5), ell(50,14,5,5), ell(92,32,5,5))
    m.f(ell(26,66,5,5), ell(50,66,6,6), ell(74,66,5,5))
    m.f(rpoly([(50,28),(56,44),(50,58),(44,44)],2)) if False else None
    m.f(star(26,22,5,2.2,4), star(76,18,4,1.8,4))
    return m

def zauberhut():
    m = Motif("zauberhut", "Zauberhut", "Wizard Hat")
    m.f(star(80,18,6,2.6,4), star(16,26,5,2.2,4), star(88,60,4,1.8,4))
    m.f(rpoly([(34,70),(52,4),(70,70)],3))
    m.f(blob([(52,4),(60,0),(70,8),(60,16)])) if False else None
    m.f(rect(34,60,36,8,0)) if False else None
    m.f(P([("M",[6,76]),("C",[6,64,94,64,94,76]),("C",[94,92,6,92,6,76]),("Z",[])]))
    m.f(rpoly([(35,64),(69,64),(70,72),(33,72)],1)) if False else None
    m.f(rect(35,58,34,10,3))
    m.f(star(52,38,7,3,5)) 
    m.f(ell(44,50,0.01,0.01)) if False else None
    return m

def schatz():
    m = Motif("schatz", "Schatzkiste", "Treasure Chest")
    m.f(rect(0,88,100,12,0))
    for x,y,r in [(38,26,5),(50,20,6),(62,26,5),(30,34,4),(70,34,4)]: m.f(ell(x,y,r,r))
    m.f(rect(12,56,76,32,3))
    m.f(P([("M",[12,56]),("C",[12,22,88,22,88,56]),("Z",[])]))
    m.f(rect(12,52,76,8,1))
    m.f(rect(40,48,20,24,4)); m.f(ell(50,58,3.4,3.4)); m.l(line((50,60),(50,66)))
    m.f(rect(22,30,6,58,1)) if False else None
    m.f(rect(20,56,6,32,1), rect(74,56,6,32,1))
    m.f(star(14,18,5,2.2,4), star(88,16,4,1.8,4))
    return m

def ballon():
    m = Motif("ballon", "Heißluftballon", "Hot Air Balloon")
    m.f(cloud(18,84,1.0), cloud(84,76,0.9))
    m.f(blob([(50,4),(76,12),(86,34),(76,56),(60,68),(40,68),(24,56),(14,34),(24,12)]))
    m.f(blob([(50,4),(60,18),(62,36),(56,56),(54,68),(46,68),(44,56),(38,36),(40,18)]))
    m.f(blob([(24,12),(32,22),(30,40),(36,56),(40,68),(24,56),(14,34)])) if False else None
    m.l(line((40,68),(40,78)), line((60,68),(60,78)))
    m.f(rect(36,78,28,16,3))
    m.l(line((36,84),(64,84)))
    return m

def geist():
    m = Motif("geist", "Geist", "Ghost")
    m.f(P([("M",[16,92]),("L",[16,46]),("C",[16,2,84,2,84,46]),("L",[84,92]),("L",[72,82]),("L",[61,92]),("L",[50,82]),("L",[39,92]),("L",[28,82]),("Z",[]) ]))
    m.f(ell(38,42,8,10)); m.f(ell(62,42,8,10)); m.dot((40,44,3.6),(64,44,3.6))
    m.f(ell(50,64,6,8))
    m.f(ell(24,56,4,2.6), ell(76,56,4,2.6))
    m.f(star(10,16,5,2.2,4), star(90,22,4,1.8,4))
    return m

def build():
    return [einhorn(), drache(), roboter(), krone(), zauberhut(), schatz(), ballon(), geist()]

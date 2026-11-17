from dsl import *
EMOJI, DE, EN, COLOR = "🚗", "Fahrzeuge", "Vehicles", "#E63946"

def w(m, x, y, r):
    m.f(ell(x, y, r, r)); m.f(ell(x, y, r * 0.45, r * 0.45))

def auto():
    m = Motif("auto", "Auto", "Car")
    m.f(rect(0,86,100,14,0))
    m.f(rpoly([(26,46),(34,32),(66,32),(76,46)],4))
    m.f(rpoly([(6,46),(94,46),(96,58),(96,72),(4,72),(4,58)],6))
    m.f(rpoly([(32,44),(38,35),(48,35),(48,44)],1.5), rpoly([(52,44),(52,35),(63,35),(70,44)],1.5))
    w(m,26,72,13); w(m,74,72,13)
    m.f(ell(90,56,3.5,3.5), ell(10,56,3.5,3.5))
    m.f(rect(46,54,8,4,1.5))
    return m

def bus():
    m = Motif("bus", "Bus", "Bus")
    m.f(rect(0,86,100,14,0))
    m.f(rect(4,26,92,52,8))
    for x in (10,28,46,64): m.f(rect(x,34,14,14,2))
    m.f(rect(80,34,12,26,2))
    m.f(rect(4,60,76,4,0)) if False else None
    m.f(rect(8,56,10,6,2)) if False else None
    w(m,24,78,11); w(m,72,78,11)
    m.f(ell(92,64,3,3))
    m.f(rect(4,50,76,3,1.5)) if False else None
    return m

def lok():
    m = Motif("lok", "Eisenbahn", "Train")
    m.f(rect(0,88,100,12,0))
    m.f(rect(4,82,92,5,1))
    m.f(rpoly([(14,22),(24,22),(22,34),(16,34)],1))
    m.f(rect(8,34,56,34,6))
    m.f(rect(60,20,34,50,3)); m.f(rect(66,26,22,16,2))
    m.f(rect(56,14,44,6,2))
    m.f(rpoly([(94,58),(100,76),(88,76),(86,58)],1)) if False else None
    w(m,24,76,10); w(m,46,76,10); w(m,76,76,11)
    m.f(ell(12,50,5,5)) 
    m.f(rpoly([(0,70),(8,62),(8,74),(0,76)],1)) if False else None
    m.f(cloud(18,10,0.7))
    return m

def flugzeug():
    m = Motif("flugzeug", "Flugzeug", "Airplane")
    m.f(cloud(18,16,0.9), cloud(80,84,0.9))
    m.f(rpoly([(10,44),(2,22),(14,22),(32,42)],2))                  # tail fin
    m.f(rpoly([(40,50),(24,90),(34,90),(66,52)],3).move(-6,-8) if False else rpoly([(46,52),(30,84),(44,84),(72,54)],3))  # wing
    m.f(blob([(6,48),(14,40),(60,38),(88,44),(98,52),(88,60),(60,62),(14,58)]))
    m.f(rpoly([(52,40),(40,14),(52,14),(70,40)],3))                 # wing back
    for x in (24,36,48,60): m.f(ell(x,49,3.6,3.6))
    m.f(blob([(76,42),(86,44),(92,50),(78,50)]))
    return m

def schiff():
    m = Motif("schiff", "Schiff", "Ship")
    m.f(blob([(0,84),(14,80),(28,86),(42,80),(56,86),(70,80),(84,86),(100,80),(100,100),(0,100)]))
    m.f(rpoly([(52,10),(52,52),(86,52)],2))
    m.f(rpoly([(46,18),(46,52),(18,52)],2))
    m.f(rect(48,8,3,52,1.5))
    m.f(rpoly([(51,8),(51,2),(62,5)],0.5)) if False else None
    m.f(rpoly([(10,60),(90,60),(78,82),(22,82)],4))
    for x in (30,48,66): m.f(ell(x,70,4,4))
    m.f(rpoly([(48,8),(48,0),(60,4)],0.5))
    return m

def feuerwehr():
    m = Motif("feuerwehr", "Feuerwehr", "Fire Truck")
    m.f(rect(0,88,100,12,0))
    m.f(rect(4,40,66,36,4))
    m.f(rect(66,44,28,32,6)); m.f(rect(72,48,16,13,2))
    m.f(rect(8,34,56,6,2)); 
    m.f(rpoly([(6,28),(46,10),(50,16),(12,34)],2))                       # ladder
    for t in (18,28,38): m.l(line((t-4,28-(t-4)*0.07*0+0),(t,30)) if False else line((t+2,22),(t+2,32)))
    m.f(rect(10,50,52,14,2))
    m.f(ell(48,22,0.01,0.01)) if False else None
    w(m,24,80,11); w(m,50,80,11); w(m,80,80,11)
    m.f(rect(76,36,10,6,2))
    return m

def traktor():
    m = Motif("traktor", "Traktor", "Tractor")
    m.f(rect(0,90,100,10,0))
    m.f(rect(34,56,62,22,4))
    m.f(rpoly([(54,26),(80,26),(82,56),(50,56)],3)); m.f(rect(59,31,16,16,2))
    m.f(rect(50,20,36,6,3))
    m.f(rect(76,40,20,6,3))
    m.f(ell(28,68,20,20)); m.f(ell(28,68,9,9)); m.f(ell(28,68,3,3))
    m.f(ell(82,78,11,11)); m.f(ell(82,78,5,5))
    m.f(rect(78,40,14,16,2)) if False else None
    return m

def heli():
    m = Motif("heli", "Hubschrauber", "Helicopter")
    m.f(rect(34,6,32,4,2)) if False else m.f(rect(8,10,84,5,2.5))
    m.f(rect(47,14,6,10,1))
    m.f(rect(2,40,40,7,3))
    m.f(rpoly([(6,26),(14,26),(26,44),(14,44)],2))
    m.f(ell(54,52,32,22))
    m.f(blob([(58,40),(70,36),(84,48),(82,62),(60,62)]))
    m.f(rect(20,84,66,5,2.5))
    m.f(rect(36,70,5,14,1), rect(64,70,5,14,1))
    m.f(rect(34,48,14,10,2))
    return m

def build():
    return [auto(), bus(), lok(), flugzeug(), schiff(), feuerwehr(), traktor(), heli()]

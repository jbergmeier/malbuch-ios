from dsl import *
EMOJI, DE, EN, COLOR = "🚜", "Baustelle", "Construction", "#FFB703"

def wheel(m, x, y, r, hub=None):
    m.f(ell(x, y, r, r))
    m.f(ell(x, y, hub or r * 0.45, hub or r * 0.45))

def bagger():
    m = Motif("bagger", "Bagger", "Excavator")
    m.f(rect(10,76,60,17,8.5))
    for x in (22,40,58): m.f(ell(x,84.5,5,5))
    m.f(rect(18,50,34,26,4))
    m.f(rect(28,54,20,14,2))
    m.f(rect(24,38,24,14,4)) # cab roof/top
    m.f(rect(28,40,12,9,2))
    m.f(rect(46,46,38,7,3.5).rot(-38,50,50))        # boom
    m.f(rect(71,22,8,36,3.5).rot(-22,75,26))          # stick
    m.f(rpoly([(78,52),(97,52),(94,66),(84,70),(76,62)],3))  # bucket
    m.f(ell(50,50,3.5,3.5), ell(74,24,3.5,3.5))
    return m

def kran():
    m = Motif("kran", "Kran", "Crane")
    m.f(rect(10,92,80,5,2))
    m.f(rect(40,86,26,8,2))
    m.f(rpoly([(44,86),(44,24),(56,24),(56,86)],1))
    m.f(rect(46,30,8,6,1), rect(46,44,8,6,1), rect(46,58,8,6,1), rect(46,72,8,6,1))
    m.f(rect(8,14,86,8,2))
    m.f(rect(8,22,14,12,2))
    m.f(rpoly([(44,24),(50,6),(56,24)],2))
    m.f(rect(30,24,12,12,2), rect(34,27,5,5,1))
    m.l(line((82,22),(82,58)))
    m.f(rect(76,58,12,5,2))
    m.f(rect(66,63,32,24,3))
    m.f(rect(70,67,10,8,1), rect(84,67,10,8,1))
    return m

def mischer():
    m = Motif("mischer", "Betonmischer", "Cement Mixer")
    m.f(rect(8,66,88,9,3))
    m.f(rpoly([(8,22),(60,32),(60,58),(8,64)],8).rot(6,34,45))   # drum body
    m.f(rpoly([(12,26),(28,28),(28,60),(12,60)],3).rot(6,34,45)) # drum back
    m.f(rpoly([(62,40),(92,40),(96,50),(96,66),(62,66)],4))      # cab
    m.f(rect(76,43,16,11,2))
    m.f(ell(30,80,10,10), ell(30,80,4.5,4.5), ell(58,80,10,10), ell(58,80,4.5,4.5))
    m.f(ell(84,80,10,10), ell(84,80,4.5,4.5))
    m.f(rect(8,56,16,4,2).rot(-20,16,58))
    return m

def kipper():
    m = Motif("kipper", "Kipplaster", "Dump Truck")
    m.f(rpoly([(8,74),(8,40),(14,30),(62,42),(62,74)],3))       # bed
    m.f(rpoly([(14,34),(20,36),(20,66),(14,66)],1.5))
    m.f(rpoly([(64,44),(88,44),(96,56),(96,76),(64,76)],4))     # cab
    m.f(rect(76,48,14,11,2))
    m.f(rect(6,74,92,8,3))
    for x,r in ((24,11),(46,11),(82,11)):
        m.f(ell(x,86,r,r)); m.f(ell(x,86,r*0.45,r*0.45))
    m.f(ell(30,56,5,5), ell(44,50,3.5,3.5))
    return m

def walze():
    m = Motif("walze", "Straßenwalze", "Road Roller")
    m.f(rect(0,92,100,8,2))
    m.f(rpoly([(50,56),(96,56),(96,84),(50,84)],5))             # body
    m.f(rpoly([(62,30),(86,30),(88,56),(60,56)],3))            # cab
    m.f(rect(66,35,16,14,2))
    m.f(rect(60,24,28,6,3))
    m.f(ell(28,70,22,22)); m.f(ell(28,70,10,10)); m.f(ell(28,70,3,3))
    m.f(rect(26,56,28,7,3))
    m.f(ell(80,80,11,11)); m.f(ell(80,80,5,5))
    return m

def radlader():
    m = Motif("radlader", "Radlader", "Wheel Loader")
    m.f(rect(36,50,52,28,4))
    m.f(rpoly([(52,26),(78,26),(80,50),(50,50)],3)); m.f(rect(57,30,16,14,2))
    m.f(rect(18,60,34,6,3).rot(-14,34,63))   # arm
    m.f(rpoly([(4,38),(24,38),(26,62),(10,76),(2,70)],3))  # bucket
    m.f(ell(34,80,15,15)); m.f(ell(34,80,6,6)); m.f(ell(74,80,15,15)); m.f(ell(74,80,6,6))
    m.f(rect(84,56,12,10,2))
    return m

def bulldozer():
    m = Motif("bulldozer", "Bulldozer", "Bulldozer")
    m.f(rect(26,74,66,18,9))
    for x in (40,58,76): m.f(ell(x,83,5,5))
    m.f(rect(34,46,48,28,4))
    m.f(rpoly([(40,24),(68,24),(72,46),(38,46)],3)); m.f(rect(46,29,16,12,2))
    m.f(rect(80,56,12,8,2))
    m.f(rect(10,40,10,48,4))                      # blade
    m.f(rect(18,58,18,6,3).rot(0))                # push arm
    return m

def cone(m, cx, base, h, w):
    top = base - h
    m.f(rect(cx-w*0.62, base-5*w/20, w*1.24, 5*w/20+0.1, 1.5))
    m.f(rpoly([(cx-w*0.4,base-5*w/20),(cx+w*0.4,base-5*w/20),(cx+w*0.14,top),(cx-w*0.14,top)],2))
    m.f(rpoly([(cx-w*0.31,base-h*0.40),(cx+w*0.31,base-h*0.40),(cx+w*0.24,base-h*0.55),(cx-w*0.24,base-h*0.55)],0.5))

def pylone():
    m = Motif("pylone", "Pylonen", "Traffic Cones")
    m.f(rect(0,90,100,10,2))
    cone(m, 22, 90, 40, 24)
    cone(m, 78, 90, 40, 24)
    cone(m, 50, 90, 70, 40)
    m.f(rect(6,36,88,5,2).rot(0)) if False else None
    m.f(ell(50,14,4,4)) if False else None
    m.f(star(86,22,6,2.6,4), star(14,24,5,2.2,4))
    return m

def build():
    return [bagger(), kran(), mischer(), kipper(), walze(), radlader(), bulldozer(), pylone()]

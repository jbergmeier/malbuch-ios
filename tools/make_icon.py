"""Draws the Bunto app icon (1024x1024) from scratch - no third-party artwork or fonts."""
from PIL import Image, ImageDraw, ImageFilter
import math, sys
S = 1024
img = Image.new("RGB", (S, S))
px = img.load()
c1, c2 = (255, 126, 182), (120, 90, 235)   # pink -> purple diagonal gradient
for y in range(S):
    for x in range(S):
        t = (x + y) / (2 * S)
        px[x, y] = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
d = ImageDraw.Draw(img, "RGBA")
# paint splats
for (x, y, r, col) in [(170,190,120,(255,210,63)), (860,170,90,(63,208,201)), (880,830,130,(255,140,66)),
                       (140,850,100,(167,214,118)), (520,90,50,(110,198,255)), (950,520,48,(230,57,70))]:
    d.ellipse([x-r, y-r, x+r, y+r], fill=col+(235,))
# white rounded card behind letter
d.rounded_rectangle([210, 190, 814, 834], radius=170, fill=(255,255,255,245))
# letter B built from shapes (own design)
ink = [(230,57,70),(255,140,66),(58,123,213)]
sx, sy, w = 340, 290, 120   # stem x, top y, stroke width
H = 444
d.rounded_rectangle([sx, sy, sx+w, sy+H], radius=60, fill=(58,123,213))
def bowl(top, h, col):
    d.ellipse([sx+40, top, sx+40+ (h*0.95), top+h], fill=col)
    d.ellipse([sx+40+w*0.55, top+w*0.55, sx+40+(h*0.95)-w*0.35, top+h-w*0.55], fill=(255,255,255,255))
bowl(sy, 230, (230,57,70))
bowl(sy+214, 230, (255,140,66))
d.rounded_rectangle([sx, sy, sx+w, sy+H], radius=60, fill=(58,123,213))
# sparkle stars
def star(cx, cy, r, col):
    pts=[]
    for i in range(8):
        a=math.radians(-90+i*45); rr=r if i%2==0 else r*0.35
        pts.append((cx+rr*math.cos(a), cy+rr*math.sin(a)))
    d.polygon(pts, fill=col)
star(700,260,46,(255,210,63,255)); star(742,360,26,(63,208,201,255))
img.save(sys.argv[1] if len(sys.argv)>1 else "icon.png")

"""Logo Sous Abri — toit cintré en porte-à-faux (terre cuite) sur un poteau (ardoise) abritant une voiture ; wordmark Archivo Bold."""
from PIL import Image, ImageDraw, ImageFont
import math, os
SABLE="#F4F1EA"; ARDOISE="#2F4A5A"; TERRE="#C8552B"; BLANC="#FFFFFF"
FONT="fonts/Archivo-Variable.ttf"
def font(size, wght=700, wdth=100):
    f=ImageFont.truetype(FONT,size); f.set_variation_by_axes([wght,wdth]); return f
def bezier(p0,p1,p2,p3,n=60):
    pts=[]
    for i in range(n+1):
        t=i/n; u=1-t
        pts.append((u**3*p0[0]+3*u*u*t*p1[0]+3*u*t*t*p2[0]+t**3*p3[0], u**3*p0[1]+3*u*u*t*p1[1]+3*u*t*t*p2[1]+t**3*p3[1]))
    return pts
def pictogram(d, x, y, s, roof=TERRE, ink=ARDOISE, hole=BLANC):
    """Boîte s×(1.5 s). Poteau à gauche, toit qui part du poteau, monte légèrement puis s'avance en porte-à-faux vers la droite ; voiture dessous."""
    W=int(s*1.5); th=max(4,int(s*0.13))
    # poteau (haut arrondi) + platine
    px=x+int(W*0.10); top=y+int(s*0.24)
    d.rounded_rectangle([px, top, px+th, y+s], radius=th//2, fill=ink)
    d.rounded_rectangle([px-int(th*0.7), y+s-int(th*0.85), px+th+int(th*0.7), y+s], radius=th//3, fill=ink)
    # toit : courbe qui s'élève depuis le poteau puis redescend doucement (aile)
    p0=(px+th//2, top+th//2); p3=(x+W, y+int(s*0.30))
    p1=(px+int(W*0.25), y-int(s*0.06)); p2=(x+int(W*0.72), y-int(s*0.02))
    pts=bezier(p0,p1,p2,p3,n=400)
    for p in pts: d.ellipse([p[0]-th/2,p[1]-th/2,p[0]+th/2,p[1]+th/2], fill=roof)
    # voiture : caisse + cabine + roues
    cx=x+int(W*0.36); cy=y+int(s*0.60); cw=int(W*0.58); ch=int(s*0.20)
    d.rounded_rectangle([cx, cy, cx+cw, cy+ch], radius=int(ch*0.35), fill=ink)
    cab=[(cx+int(cw*0.20), cy+2), (cx+int(cw*0.32), cy-int(ch*0.75)), (cx+int(cw*0.68), cy-int(ch*0.75)), (cx+int(cw*0.84), cy+2)]
    d.polygon(cab, fill=ink)
    r=int(ch*0.40)
    for wx in (cx+int(cw*0.24), cx+int(cw*0.76)):
        d.ellipse([wx-r, cy+ch-r*0.9, wx+r, cy+ch+r*1.1], fill=ink)
        d.ellipse([wx-r*0.45, cy+ch-r*0.35, wx+r*0.45, cy+ch+r*0.55], fill=hole)
def render(out, W=2400, H=760, bg=SABLE, ink=ARDOISE, roof=TERRE, text=ARDOISE, stacked=False, hole=None):
    hole=hole or (bg if isinstance(bg,str) else SABLE)
    im=Image.new("RGBA",(W,H),bg if bg else (0,0,0,0)); d=ImageDraw.Draw(im)
    if stacked:
        s=int(H*0.40); pictogram(d,(W-int(s*1.5))//2,int(H*0.10),s,roof,ink,hole)
        f=font(int(H*0.17)); t="Sous Abri"; tw=d.textlength(t,font=f); d.text(((W-tw)/2,int(H*0.66)),t,font=f,fill=text)
    else:
        s=int(H*0.56); pictogram(d,int(H*0.14),int(H*0.20),s,roof,ink,hole)
        f=font(int(H*0.36)); t="Sous Abri"; d.text((int(H*0.14)+int(s*1.5)+int(H*0.10),int(H*0.27)),t,font=f,fill=text)
    im.save(out); return out
os.makedirs("out",exist_ok=True)
render("out/logo-sousabri.png")
render("out/logo-sousabri-inverse.png",bg=ARDOISE,ink=BLANC,roof=TERRE,text=BLANC,hole=ARDOISE)
render("out/logo-sousabri-transparent.png",bg=None,hole=SABLE)
render("out/logo-sousabri-empile.png",W=1400,H=1400,stacked=True)
im=Image.new("RGBA",(1024,1024),TERRE); d=ImageDraw.Draw(im); pictogram(d,110,330,480,BLANC,BLANC,TERRE); im.save("out/favicon-sousabri.png")
im=Image.new("RGBA",(1024,1024),SABLE); d=ImageDraw.Draw(im); pictogram(d,110,330,480,TERRE,ARDOISE,SABLE); im.save("out/monogramme-sousabri.png")
sheet=Image.new("RGB",(2400,2400),"white")
sheet.paste(Image.open("out/logo-sousabri.png").convert("RGB"),(0,0)); sheet.paste(Image.open("out/logo-sousabri-inverse.png").convert("RGB"),(0,780))
sheet.paste(Image.open("out/logo-sousabri-empile.png").convert("RGB").resize((800,800)),(0,1580)); sheet.paste(Image.open("out/favicon-sousabri.png").convert("RGB").resize((700,700)),(850,1620)); sheet.paste(Image.open("out/monogramme-sousabri.png").convert("RGB").resize((700,700)),(1620,1620))
sheet.save("out/planche-logo.jpg",quality=90); print("ok")

def svg(out, ink=ARDOISE, roof=TERRE, text=ARDOISE, bg=None, W=2400, H=760):
    s=int(H*0.56); x=int(H*0.14); y=int(H*0.20); Wp=int(s*1.5); th=max(4,int(s*0.13))
    px=x+int(Wp*0.10); top=y+int(s*0.24)
    p0=(px+th//2, top+th//2); p3=(x+Wp, y+int(s*0.30)); p1=(px+int(Wp*0.25), y-int(s*0.06)); p2=(x+int(Wp*0.72), y-int(s*0.02))
    cx=x+int(Wp*0.36); cy=y+int(s*0.60); cw=int(Wp*0.58); ch=int(s*0.20); r=int(ch*0.40)
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    if bg: parts.append(f'<rect width="{W}" height="{H}" fill="{bg}"/>')
    parts.append(f'<rect x="{px}" y="{top}" width="{th}" height="{y+s-top}" rx="{th//2}" fill="{ink}"/>')
    parts.append(f'<rect x="{px-int(th*0.7)}" y="{y+s-int(th*0.85)}" width="{th*2+int(th*1.4)-th}" height="{int(th*0.85)}" rx="{th//3}" fill="{ink}"/>')
    parts.append(f'<path d="M {p0[0]} {p0[1]} C {p1[0]} {p1[1]}, {p2[0]} {p2[1]}, {p3[0]} {p3[1]}" fill="none" stroke="{roof}" stroke-width="{th}" stroke-linecap="round"/>')
    parts.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="{int(ch*0.35)}" fill="{ink}"/>')
    parts.append(f'<polygon points="{cx+int(cw*0.20)},{cy+2} {cx+int(cw*0.32)},{cy-int(ch*0.75)} {cx+int(cw*0.68)},{cy-int(ch*0.75)} {cx+int(cw*0.84)},{cy+2}" fill="{ink}"/>')
    hole=bg or "#F4F1EA"
    for wx in (cx+int(cw*0.24), cx+int(cw*0.76)):
        parts.append(f'<circle cx="{wx}" cy="{cy+ch+r*0.1}" r="{r}" fill="{ink}"/><circle cx="{wx}" cy="{cy+ch+r*0.1}" r="{r*0.45}" fill="{hole}"/>')
    parts.append(f'<text x="{x+Wp+int(H*0.10)}" y="{int(H*0.27)+int(H*0.36*0.78)}" font-family="Archivo, Inter, Helvetica, Arial, sans-serif" font-weight="700" font-size="{int(H*0.36)}" fill="{text}">Sous Abri</text>')
    parts.append('</svg>'); open(out,"w").write("\n".join(parts))
svg("out/logo-sousabri.svg"); svg("out/logo-sousabri-inverse.svg",ink=BLANC,text=BLANC,bg=ARDOISE)
print("svg ok")

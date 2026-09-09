"""Relecture automatique des contenus : interdits, chiffres incohérents, placeholders."""
import re,glob,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
files=sorted(glob.glob("content/**/*.md",recursive=True))
rules={
 "point d'exclamation":r"!(?!\[)",
 "fabrication française":r"fabriqu[ée]e? en France|fabrication fran",
 "sans autorisation (absolu)":r"sans autorisation(?! préalable| de| \(| —| :|,| \?)",
 "résiste aux tempêtes / anti-neige":r"résiste à toutes|anti-neige|antineige|résiste aux tempêtes",
 "DHL depuis l'Europe (faux : Chine)":r"DHL depuis l'Europe|depuis l'Europe",
 "délai hors brief":r"\b(2 à 4|4 à 8|6 à 10|10 à 15) (jours|semaines)",
 "garantie commerciale chiffrée":r"garantie (de )?(5|10|15) ans",
 "avis/notes inventés":r"\b\d[,.]\d ?/ ?5\b|\d+ ?% de clients|\d+ clients satisfaits|★",
 "galvanisé hors fiches 9/12/14":r"galvanis",
 "thermolaqué hors fiche 6":r"thermolaqu",
}
ok_galva={"tente-garage-3x6-outsunny.md","tente-garage-4x7-6-camping-car.md","tente-garage-mobile-3x3.md","guide-montage-ancrage.md","comparatif-carport-tente-garage.md","faq.md","tente-garage-4x6-portes-enroulables.md","tente-garage-4x6-fenetres.md","tente-carport-fermee-2-cotes.md","tente-garage-4x6-double-porte-volet.md"}
ok_thermo={"carport-acier-thermolaque-4-5x3.md","comparatif-carport-tente-garage.md","carport-metallique.md","accueil.md","guide-montage-ancrage.md","faq.md"}
tot=0
for f in files:
    t=open(f).read(); b=os.path.basename(f)
    hits=[]
    for name,p in rules.items():
        if name.startswith("galvanisé") and b in ok_galva: continue
        if name.startswith("thermolaqué") and b in ok_thermo: continue
        m=[x for x in re.finditer(p,t)]
        if m: hits.append(f"{name} ×{len(m)} (ex. « …{t[max(0,m[0].start()-40):m[0].end()+30].replace(chr(10),' ')}… »)")
    nv=len(re.findall(r"\[À VÉRIFIER",t)); nd=len(re.findall(r"\[À DÉCIDER",t)); words=len(t.split())
    print(f"{f} — {words} mots, {nv} À VÉRIFIER, {nd} À DÉCIDER"+("" if not hits else "\n   ! "+"\n   ! ".join(hits)))
    tot+=len(hits)
print("\nalertes:",tot)

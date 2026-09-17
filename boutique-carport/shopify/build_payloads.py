"""Convertit content/*.md en charges utiles Shopify (JSON) : produits, collections, pages."""
import re,json,glob,os,markdown
os.chdir(os.path.dirname(os.path.abspath(__file__))+"/..")
MD=lambda t: markdown.markdown(t,extensions=["tables"])
def mark(t): return re.sub(r"`?\[(À VÉRIFIER|À DÉCIDER)([^\]]*)\]`?",r'<mark class="a-verifier">[\1\2]</mark>',t)
def meta(txt,key):
    m=re.search(r"\*?\*?"+key+r"[^:\n]*:\*?\*?\s*(.+)",txt); return m.group(1).strip().strip("*") if m else ""
def section(txt,title):
    m=re.search(r"^##+\s*"+re.escape(title)+r"[^\n]*\n(.*?)(?=^##\s|\Z)",txt,re.S|re.M); return re.sub(r"\n---\s*$","",m.group(1).strip()).strip() if m else ""
def fix_tables(t):
    out=[];prev=""
    for l in t.split("\n"):
        if l.startswith("|") and prev.strip() and not prev.startswith("|"): out.append("")
        out.append(l); prev=l
    return "\n".join(out)
cat=json.load(open("catalogue-source-2026-09-09.json"))
prods=[]
skus={"carport-acier-thermolaque-4-5x3":("SA-ACIER-450","1005012344715751",1069),"carport-aluminium-autoportant":("SA-ALU-AUTO-6x6","1005009961706626",1199),"carport-camping-car-aluminium":("SA-ALU-CC-6x38","1005011994406763",1939),"tente-garage-3x6-outsunny":("SA-TG-3x6-OUT","1005012736849383",459),"tente-garage-4x6-portes-enroulables":("SA-TG-4x6-PE","1005010670791375",549),"tente-garage-4x6-fenetres":("SA-TG-4x6-FEN","1005012384075437",609),"tente-garage-4x7-6-camping-car":("SA-TG-4x76","1005012322112744",749),"tente-carport-fermee-2-cotes":("SA-TG-FERM2","1005012904297579",719),"tente-garage-mobile-3x3":("SA-TG-3x3","1005012942086535",349),"tente-garage-4x6-double-porte-volet":("SA-TG-4x6-VOL","1005013014844719",739)}
colmap={}
for c in cat["collections"]:
    for p in cat["produits"]:
        if c["kw"] in p["collections"]: colmap.setdefault(p["ali_id"],[]).append(c["kw"])
slug=lambda s: re.sub(r"[^a-z0-9]+","-",s.lower().replace("é","e").replace("è","e").replace("ê","e").replace("à","a")).strip("-")
for f in sorted(glob.glob("content/produits/*.md")):
    h=os.path.basename(f)[:-3]
    if h.startswith("MODELE") or h not in skus: continue
    t=open(f).read(); sku,ali,price=skus[h]
    title=section(t,"H1").splitlines()[0].strip() if section(t,"H1") else meta(t,"H1")
    sub=section(t,"Sous-titre"); achat=section(t,"Bloc d'achat"); desc=section(t,"Description longue"); dims=section(t,"Dimensions"); car=section(t,"Caractéristiques"); faq=section(t,"FAQ")
    bullets="\n".join(l for l in achat.splitlines() if l.startswith("- "))
    html=MD(mark(fix_tables(f"*{sub}*\n\n{bullets}\n\n{desc}\n\n## Dimensions et capacité\n\n{dims}\n\n## Caractéristiques\n\n{car}\n\n## Questions fréquentes\n\n{faq}")))
    cols_=[slug(k) for k in colmap.get(ali,[])]; cols_=[("carport-3x5-tailles" if c=="carport-3x5" else c) for c in cols_]
    if h=="tente-garage-3x6-outsunny" and "carport-camping-car" not in cols_: cols_.append("carport-camping-car")
    prods.append({"handle":h,"title":title,"descriptionHtml":html,"price":price,"sku":sku,"ali_id":ali,"seoTitle":meta(t,"Meta title")[:60],"seoDescription":meta(t,"Meta description")[:160],"collections":cols_,"productType":"Tente-garage" if h.startswith("tente") else "Carport","vendor":"Sous Abri"})
cols=[]
for f in sorted(glob.glob("content/collections/*.md")):
    t=open(f).read(); h=os.path.basename(f)[:-3]
    title=meta(t,"H1"); intro=section(t,"Texte d'intro"); seo=section(t,"Texte SEO")
    cols.append({"handle":h,"title":title,"descriptionHtml":MD(mark(intro)),"bottomHtml":MD(mark(seo)),"seoTitle":meta(t,"Meta title")[:60],"seoDescription":meta(t,"Meta description")[:160],"kw":meta(t,"Mot-clé")})
pages=[]
for f in sorted(glob.glob("content/pages/*.md"))+sorted(glob.glob("content/produits/devis-*.md")):
    t=open(f).read(); h=os.path.basename(f)[:-3]
    if h in ("accueil","annonces-menu-footer"): continue
    title=meta(t,"H1") or section(t,"H1").splitlines()[0]
    body=t.split("\n---",1)[-1] if "\n---" in t else t
    body=re.sub(r"^\s*## H1\s*\n[^\n]*\n","",body,flags=re.M)
    body=re.sub(r"^\s*---\s*\n","",body)
    body=re.sub(r"^## Images[^\n]*\n.*","",body,flags=re.S|re.M)
    body=re.sub(r"^\*Note pour Hakim[^\n]*\n?","",body,flags=re.M)
    body=fix_tables(body)
    pages.append({"handle":h,"title":title.strip(),"bodyHtml":MD(mark(body)),"seoTitle":meta(t,"Meta title")[:60],"seoDescription":meta(t,"Meta description")[:160],"template":"contact" if h=="contact" else ("devis" if h.startswith("devis") else None)})
json.dump({"products":prods,"collections":cols,"pages":pages},open("shopify/payloads.json","w"),ensure_ascii=False,indent=1)
print(len(prods),"produits",len(cols),"collections",len(pages),"pages")
for p in prods: print(" ",p["handle"],p["price"],p["title"][:50],"|",p["collections"],len(p["descriptionHtml"]))

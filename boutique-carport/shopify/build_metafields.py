"""Reconstruit les métachamps produits (namespace custom) depuis content/produits/*.md.
Sortie : shopify/metafields-produits.json (liste d'entrées metafieldsSet). Les métachamps collections/pages ne sont pas touchés."""
import re,json,glob,os,markdown
os.chdir(os.path.dirname(os.path.abspath(__file__))+"/..")
MD=lambda t: markdown.markdown(t,extensions=["tables"])
def mark(t): return re.sub(r"`?\[(À VÉRIFIER|À DÉCIDER)([^\]]*)\]`?",r'<mark class="a-verifier">[\1\2]</mark>',t)
def section(txt,title):
    m=re.search(r"^##\s*"+re.escape(title)+r"[^\n]*\n(.*?)(?=^##\s|\Z)",txt,re.S|re.M); return m.group(1).strip() if m else ""
def sub(txt,title):
    m=re.search(r"^###\s*"+re.escape(title)+r"[^\n]*\n(.*?)(?=^###\s|^##\s|^---\s*$|\Z)",txt,re.S|re.M); return m.group(1).strip() if m else ""
PID={"carport-acier-thermolaque-4-5x3":"15884512199039","carport-aluminium-autoportant":"15884512231807","carport-camping-car-aluminium":"15884512264575","tente-carport-fermee-2-cotes":"15884512297343","tente-garage-3x6-outsunny":"15884512690559","tente-garage-4x6-double-porte-volet":"15884512723327","tente-garage-4x6-fenetres":"15884512756095","tente-garage-4x6-portes-enroulables":"15884513182079","tente-garage-4x7-6-camping-car":"15884513214847","tente-garage-mobile-3x3":"15884513247615"}
SUBS=[("protege","Ce qu'il protège vraiment"),("declarer","Faut-il le déclarer ?"),("montage_texte","Le montage, honnêtement"),("ancrage_vent","L'ancrage et le vent"),("ne_fait_pas","Ce qu'il ne fait pas"),("livraison_texte","La livraison, concrètement")]
out=[]
for h,pid in PID.items():
    t=open(f"content/produits/{h}.md").read(); owner=f"gid://shopify/Product/{pid}"
    def add(key,val,typ="multi_line_text_field"):
        if val: out.append({"ownerId":owner,"namespace":"custom","key":key,"type":typ,"value":val})
    st=section(t,"Sous-titre").split("\n---")[0].strip()
    add("sous_titre",st,"single_line_text_field")
    dims=section(t,"Dimensions et capacité").split("\n---")[0]; car=section(t,"Caractéristiques").split("\n---")[0]
    add("specifications",MD(mark(dims+"\n\n"+car)))
    achat=section(t,"Bloc d'achat"); m=re.search(r"livr[ée]e?s? (?:en|sous) ([^\n,.;]+)",achat)
    add("delai_livraison",(m.group(1).strip() if m else ""),"single_line_text_field")
    m=re.search(r"\|\s*Contenu du colis\s*\|\s*(.+?)\s*\|",car)
    add("contenu_colis",MD(mark(m.group(1))) if m else "")
    desc=section(t,"Description longue")
    for key,title in SUBS: add(key,MD(mark(sub(desc,title))))
    faq=section(t,"FAQ").split("\n---")[0]
    items=re.findall(r"\*\*(\d+\.[^*]+)\*\*\s*\n(.+?)(?=\n\*\*\d+\.|\Z)",faq,re.S)
    add("faq","\n".join(f"<details><summary>{q.strip()}</summary>{MD(mark(a.strip()))}</details>" for q,a in items))
json.dump(out,open("shopify/metafields-produits.json","w"),ensure_ascii=False,indent=1)
n=sum(1 for m in out if "[À " in m["value"]); print(len(out),"métachamps,",n,"avec marqueur restant")

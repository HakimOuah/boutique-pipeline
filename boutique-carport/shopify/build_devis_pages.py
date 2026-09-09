"""Construit le corps client des 3 pages devis (sans le brief : métadonnées, champs du formulaire, liste d'images)."""
import re,json,glob,os,markdown
os.chdir(os.path.dirname(os.path.abspath(__file__))+"/..")
MD=lambda t: markdown.markdown(t,extensions=["tables"])
def mark(t): return re.sub(r"`?\[(À VÉRIFIER|À DÉCIDER)([^\]]*)\]`?",r'<mark class="a-verifier">[\1\2]</mark>',t)
def section(txt,title):
    m=re.search(r"^##+\s*"+re.escape(title)+r"[^\n]*\n(.*?)(?=^##\s|\Z)",txt,re.S|re.M); return m.group(1).strip() if m else ""
def sub3(txt,title):
    m=re.search(r"^###\s*"+re.escape(title)+r"[^\n]*\n(.*?)(?=^###\s|^##\s|\Z)",txt,re.S|re.M); return m.group(1).strip() if m else ""
out=[]
for f in sorted(glob.glob("content/produits/devis-*.md")):
    t=open(f).read(); h=os.path.basename(f)[:-3]
    sub=section(t,"Sous-titre"); achat=section(t,"Bloc d'achat"); desc=section(t,"Description longue")
    bullets="\n".join(l for l in achat.splitlines() if l.startswith("- "))
    prix=re.search(r"\*\*Prix :\*\*\s*(.+)",achat); prix=prix.group(1).strip() if prix else ""
    parts=[f"<p class=\"sa-lead\"><em>{mark(sub)}</em></p>", MD(mark(bullets))]
    if prix: parts.append(f"<p><strong>Prix :</strong> {mark(prix)}</p>")
    parts.append('<p><a class="button" style="color:#fff" href="#DevisForm">Demander mon devis gratuit</a></p>')
    titles=[m.group(1).strip() for m in re.finditer(r"^###\s*(.+)$",desc,re.M)]
    for ti in titles:
        if ti.startswith("Pourquoi un devis"): continue  # déjà dans le gabarit
        parts.append(MD(mark(f"## {ti}\n\n{sub3(desc,ti)}")))
    der=section(t,"Déroulé après votre demande")
    steps=[s.strip() for s in re.split(r"(?:^|\s)\d\.\s",der) if s.strip()]
    parts.append("<h2>Déroulé après votre demande</h2><ol>"+"".join(f"<li>{mark(s)}</li>" for s in steps)+"</ol>")
    faq=section(t,"FAQ")
    qs=[]
    for m in re.finditer(r"\*\*\d+\.\s*(.+?)\*\*\s*(.+)",faq):
        q,a=m.group(1).strip(),m.group(2).strip()
        if q.startswith("Le devis m'engage") or q.startswith("Puis-je payer en plusieurs"): continue  # déjà dans la FAQ devis du gabarit
        qs.append(f"<details><summary>{q}</summary><p>{mark(a)}</p></details>")
    parts.append("<h2>Questions fréquentes sur ce carport</h2>"+"".join(qs))
    body="\n".join(parts)
    body=re.sub(r"<h2>","<h2>",body)
    out.append({"handle":h,"body":body})
json.dump(out,open("shopify/payload-devis-pages.json","w"),ensure_ascii=False,indent=1)
for o in out: print(o["handle"],len(o["body"]),"chars", o["body"].count("<h2>"),"h2", o["body"].count("<details>"),"faq")

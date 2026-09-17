"""Extrait les blocs 'SHOP <requête>' (dump localStorage du navigateur) → shop-raw.jsonl (une ligne par offre)."""
import json,sys,re,os,urllib.parse
D=os.path.dirname(os.path.abspath(__file__))
out=open(os.path.join(D,"shop-raw.jsonl"),"a"); n=0; seen=set()
for f in sys.argv[1:]:
    arr=json.load(open(f)); text="\n".join(a.get("text","") for a in arr)
    text=text.split("\n\nTab Context")[0]
    blocks=re.split(r"\nSHOP ",("\n"+text)[ ("\n"+text).find("\nSHOP "): ])
    for b in blocks:
        if not b.strip(): continue
        lines=b.split("\n"); q=lines[0].strip()
        for l in lines[1:]:
            parts=[p.strip() for p in l.split("¦")]
            if len(parts)<3: continue
            href=parts[-1]; fields=parts[:-1]
            pi=next((i for i,p in enumerate(fields) if re.search(r"^\d[\d\s  .]*(,\d+)?\s?€",p)),None)
            if pi is None: continue
            title=" ".join(fields[:pi]).strip()
            price_txt=fields[pi]
            pv=re.sub(r"[^\d,]","",price_txt.split("€")[0]).replace(",",".")
            try: pnum=float(pv)
            except: continue
            rest=fields[pi+1:]
            merchant=next((r for r in rest if not re.match(r"^(et plus|Gratuite|En magasin|Retours|\+|\d|Énergie|Occasion|Nouveau)",r)),"")
            key=(q,title[:60],pnum,merchant)
            if key in seen: continue
            seen.add(key)
            out.write(json.dumps({"q":q,"titre":title,"prix":pnum,"prix_txt":price_txt,"marchand":merchant,"href":"" if href=="NOHREF" else href,"reste":" | ".join(rest)},ensure_ascii=False)+"\n"); n+=1
print(n,"offres")

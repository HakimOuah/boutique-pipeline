"""Fusionne sourcing-lot*.json → SYNTHESE.md, puis écrit G/H/K de l'onglet « Pergola aluminium » (rows 8–72).
Usage : python3 merge.py [--write]  (sans --write : synthèse seulement)."""
import json,glob,os,sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..","scripts"))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

NORM={"OFFRE TROUVEE":"OFFRE TROUVÉE","FOURNISSEUR A TESTER":"FOURNISSEUR À TESTER"}
def normalise(r):
    """Harmonise les lots : accents, et règle du protocole — le prix affiché exactement à la moitié du sku_price (schéma « demi-prix » des magasins Star Alu / One Alu) n'est pas une OFFRE TROUVÉE."""
    r["statut"]=NORM.get(r.get("statut",""),r.get("statut",""))
    try: ratio=float(r.get("sku_price_eur") or 0)/float(r.get("prix_ttc_eur") or 1)
    except Exception: ratio=1
    if r["statut"]=="OFFRE TROUVÉE" and 1.95<=ratio<=2.05:
        r["statut"]="FOURNISSEUR À TESTER"
        r["remarque"]="Prix affiché = 50 % du sku_price sans remise expliquée (schéma demi-prix), à confirmer avant commande test. "+(r.get("remarque") or "")
    return r

lignes=json.load(open("../2026-09-09-pergola-aluminium/lignes-onglet.json"))
res=[]
for f in sorted(glob.glob("sourcing-lot*.json")):
    try: res+=json.load(open(f))
    except Exception as e: print("ERR",f,e)
res=[normalise(r) for r in res]
by_row={int(r["row"]):r for r in res if r.get("row")}
by_kw={}
for r in res: by_kw.setdefault(r["produit"].strip().lower(),r)
stats={}; md=["# Synthèse sourcing pergola bioclimatique / aluminium — 09/09/2026","","| Ligne | Produit | Statut | Fiche | Prix TTC livré | Expédié de | Délai | Remarque |","|---|---|---|---|---|---|---|---|"]
G=[];H=[];K=[]
first=lignes[0]["row"]; last=lignes[-1]["row"]
for l in lignes:
    n=l["row"]
    r=by_row.get(n) or (by_kw.get(l["kw"].strip().lower()) if l["niveau"]=="Produit" else None)
    if l["niveau"]!="Produit" or not r:
        G.append([""]);H.append([""]);K.append([""])
        if l["niveau"]=="Produit": md.append(f"| {n} | {l['kw']} | (non traité) | | | | | |")
        continue
    st=r.get("statut",""); stats[st]=stats.get(st,0)+1
    sub=r.get("substitut") or {}
    pid=str(r.get("product_id") or sub.get("product_id") or sub.get("id") or "").strip()
    price=r.get("prix_ttc_eur") or sub.get("prix_ttc_eur") or sub.get("prix") or ""
    url=f"https://www.aliexpress.com/item/{pid}.html" if pid else ""
    note=st+(" — "+r["remarque"] if r.get("remarque") else "")
    if not r.get("product_id") and pid: note+=f" [substitut {pid}]"
    G.append([f'=HYPERLINK("{url}";"{pid}")' if pid else ""])
    H.append([float(price) if price not in ("",None) else ""])
    K.append([note[:250]])
    md.append(f"| {n} | {l['kw']} | {st} | {pid} | {price} | {r.get('ship_from') or sub.get('ship_from','')} | {r.get('delai_jours') or sub.get('delai_jours','')} | {(r.get('remarque') or '')[:140].replace('|','/')} |")
md.insert(2,"Statuts : "+", ".join(f"{k} {v}" for k,v in sorted(stats.items()))+f" (sur {sum(stats.values())} lignes produit, {len(by_kw)} produits uniques traités).")
open("SYNTHESE.md","w").write("\n".join(md)+"\n"); print(stats,len(G),"lignes")
if "--write" in sys.argv:
    import gsheet_bridge as g
    ops=[{"action":"write","sheet":"Pergola aluminium","range":f"G{first}","values":G},
         {"action":"write","sheet":"Pergola aluminium","range":f"H{first}","values":H},
         {"action":"write","sheet":"Pergola aluminium","range":f"K{first}","values":K}]
    print(g.call(ops))
    chk=g.call([{"action":"read","sheet":"Pergola aluminium","range":f"G{first}:K{last}"}])["result"][0]
    bad=[(i+first,c) for i,row in enumerate(chk) for c in row if isinstance(c,str) and c.startswith("#")]
    print("erreurs:",bad or "aucune")

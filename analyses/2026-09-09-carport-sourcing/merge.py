import json,glob,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
rows=[]
for f in sorted(glob.glob('sourcing-lot*.json')):
    try: rows+=json.load(open(f))
    except Exception as e: print('ERR',f,e)
by={r['produit'].strip().lower():r for r in rows}
order=[l.split('\t') for l in open('/private/tmp/claude-502/-Users-Hakim-Documents-Boutiques-drop/f13db31b-0454-40da-9b2d-d09781f8f692/scratchpad/carport-paste.tsv').read().splitlines()]
out=[];md=["# Synthèse sourcing carport — 09/09/2026","","| Produit | Statut | Fiche | Prix TTC | Expédié de | Délai | Remarque |","|---|---|---|---|---|---|---|"]
stats={}
for lvl,_,kw,vol in order:
    r=by.get(kw.strip().lower())
    if lvl!='Produit' or not r:
        out.append("\t\t\t"); continue
    st=r.get('statut',''); stats[st]=stats.get(st,0)+1
    sub=r.get('substitut') or {}
    pid=r.get('product_id') or sub.get('product_id') or ''
    price=r.get('prix_ttc_eur') or sub.get('prix_ttc_eur') or ''
    url=f"https://www.aliexpress.com/item/{pid}.html" if pid else ''
    note=f"{st}"+(f" — {r.get('remarque','')}" if r.get('remarque') else '')
    out.append("\t".join([url,str(price).replace('.',',') if price!='' else '',note[:180]]))
    md.append(f"| {kw} | {st} | {pid} | {price} | {r.get('ship_from') or sub.get('ship_from','')} | {r.get('delai_jours') or sub.get('delai_jours','')} | {(r.get('remarque') or '')[:120]} |")
open('/private/tmp/claude-502/-Users-Hakim-Documents-Boutiques-drop/f13db31b-0454-40da-9b2d-d09781f8f692/scratchpad/carport-liens-GHK.tsv','w').write("\n".join(out))
md.insert(2,"Statuts : "+", ".join(f"{k} {v}" for k,v in stats.items())+f" (sur {sum(stats.values())} lignes produit qualifiées, {len(by)} produits uniques).")
open('SYNTHESE.md','w').write("\n".join(md)); print(stats, len(out),'lignes TSV')

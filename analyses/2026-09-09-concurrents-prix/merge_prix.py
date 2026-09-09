"""Fusion sélections concurrents → liens marchands (DataForSEO sellers) → prix cible proposé → onglets.
Usage : python3 merge_prix.py [--sellers] [--write]
  --sellers : résout les URL marchandes des fiches retenues (cache sellers.json, 0,001 $/fiche)
  --write   : écrit L7:Q7 (en-têtes), L:O (concurrents exacts du mot-clé), P:Q (comparable de la fiche AliExpress quand elle est d'une autre famille, ex. tente-garage) dans les onglets (I n'est plus écrit par ce script) Carport et Pergola aluminium
Règle prix cible : juste sous le comparable = prix du concurrent retenu le moins cher (le client le voit aussi) moins 5 %, arrondi vers le bas au 9 inférieur (…9 € au-dessus de 100 €, …9,90 € en dessous). Non proposé si < 1,3 × prix AliExpress livré.
"""
import json,os,sys,base64,urllib.request,urllib.parse,time,math
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
sys.path.insert(0,os.path.join(D,"..","..","scripts"))
sel=[]
for f in ("selection-carport.json","selection-pergola.json"):
    if os.path.exists(f): sel+=json.load(open(f))
by_q={s["q"].strip().lower():s for s in sel}
tentes={t["q"].strip().lower():t for t in (json.load(open("selection-carport-tentes.json")) if os.path.exists("selection-carport-tentes.json") else [])}
prods=json.load(open("produits.json"))
# --- sellers
cache=json.load(open("sellers.json")) if os.path.exists("sellers.json") else {}
if "--sellers" in sys.argv:
    auth="Basic "+base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode()
    def call(path,data=None):
        req=urllib.request.Request("https://api.dataforseo.com/v3/"+path,data=json.dumps(data).encode() if data else None,headers={"Authorization":auth,"Content-Type":"application/json"})
        return json.loads(urllib.request.urlopen(req,timeout=60).read())
    ids=sorted({str(c["product_id"]) for s in list(sel)+list(tentes.values()) for c in s.get("concurrents",[]) if c.get("product_id")}-set(cache))
    if ids:
        r=call("merchant/google/sellers/task_post",[{"product_id":i,"location_name":"France","language_code":"fr","tag":i} for i in ids])
        tasks={t["data"]["tag"]:t["id"] for t in r["tasks"] if t["status_code"]==20100}
        print("sellers: tâches",len(tasks),"coût",r["cost"])
        for attempt in range(10):
            time.sleep(25)
            for pid,tid in list(tasks.items()):
                g=call(f"merchant/google/sellers/task_get/advanced/{tid}")["tasks"][0]
                if g["status_code"]==20000:
                    res=(g.get("result") or [{}])[0] or {}
                    cache[pid]={"title":res.get("title"),"sellers":[{k:it.get(k) for k in ("seller_name","total_price","url")} for it in (res.get("items") or [])]}
                    tasks.pop(pid)
                elif g["status_code"] not in (20100,40601,40602): cache[pid]={"error":g["status_message"],"sellers":[]}; tasks.pop(pid)
            if not tasks: break
        json.dump(cache,open("sellers.json","w"),ensure_ascii=False,indent=1)
org=json.load(open("organic-links.json")) if os.path.exists("organic-links.json") else {}
dfs=json.load(open("dfs-shopping.json"))
def shopping_url(c):
    for q,items in dfs.items():
        for it in items:
            if it.get("title")==c["title"] and it.get("seller")==c["seller"] and it.get("shopping_url"): return it["shopping_url"]
    return None
def seller_url(c):
    if not c.get("product_id"):
        o=org.get(c["seller"]+" | "+c["title"],{})
        if o.get("url") and o.get("score",0)>=3: return o["url"]
        return shopping_url(c) or o.get("url") or "https://www.google.fr/search?udm=28&q="+urllib.parse.quote(c["title"]+" "+c["seller"])
    e=cache.get(str(c.get("product_id")),{})
    for s in e.get("sellers",[]):
        if s.get("seller_name","").lower().split(" - ")[0]==c["seller"].lower().split(" - ")[0] and s.get("url"): return s["url"].split("?srsltid")[0]
    for s in e.get("sellers",[]):
        if s.get("url"): return s["url"].split("?srsltid")[0]
    return shopping_url(c) or f"https://www.google.com/shopping/product/{c.get('product_id')}"
def prix_cible(ref,ali):
    p=ref*0.95
    if p>=100: t=math.floor(p/10)*10-1
    else: t=math.floor(p)-0.10
    if ali and t<1.3*float(ali): return None
    return t
def q_(s): return s.replace('"','""')
def link(c):
    txt=f"{c['seller']} — {c['title'][:50]} ({c['price']:.0f} €)"
    return f'=HYPERLINK("{seller_url(c)}";"{q_(txt)}")'
rows_out=[]; md=["# Concurrents et prix cible proposé — 09/09/2026","","| Onglet | Produit | Ali livré | Concurrent 1 | Prix 1 | Concurrent 2 | Prix 2 | Comparable fiche Ali | Prix | Prix cible proposé | Note |","|---|---|---|---|---|---|---|---|---|---|---|"]
for p in prods:
    s=by_q.get(p["kw"].strip().lower())
    cs=(s or {}).get("concurrents",[])[:2]
    ref=min((c["price"] for c in cs),default=None)
    note=(s or {}).get("note","")
    t=tentes.get(p["kw"].strip().lower()); tcs=(t or {}).get("concurrents",[])[:2]
    if tcs:
        ref=min(c["price"] for c in tcs)
        note=f"Prix cible basé sur le comparable de la fiche AliExpress (tente-garage) : {tcs[0]['seller']} {tcs[0]['price']} €, pas sur le concurrent exact du mot-clé. "+note
    cible=prix_cible(ref,p.get("ali_prix")) if ref else None
    if ref and cible is None: note="Prix cible non proposé : comparable trop bas par rapport au coût AliExpress livré (marge < 30 %). "+note
    p.update({"concurrents":cs,"tentes":tcs,"ref":ref,"prix_cible":cible,"note_cible":note})
    md.append(f"| {p['onglet']} | {p['kw']} | {p.get('ali_prix') or ''} | {(cs[0]['seller']+' — '+cs[0]['title'][:40]) if cs else '—'} | {cs[0]['price'] if cs else ''} | {(cs[1]['seller']+' — '+cs[1]['title'][:40]) if len(cs)>1 else ''} | {cs[1]['price'] if len(cs)>1 else ''} | {(tcs[0]['seller']+' — '+tcs[0]['title'][:40]) if tcs else ''} | {tcs[0]['price'] if tcs else ''} | {cible if cible is not None else ''} | {note[:110].replace('|','/')} |")
open("SYNTHESE.md","w").write("\n".join(md)+"\n")
n2=sum(1 for p in prods if len(p["concurrents"])>=2); n1=sum(1 for p in prods if len(p["concurrents"])==1); n0=sum(1 for p in prods if not p["concurrents"])
print(f"lignes {len(prods)} : 2 concurrents {n2}, 1 concurrent {n1}, aucun {n0} ; prix cible proposé {sum(1 for p in prods if p['prix_cible'])}")
if "--write" in sys.argv:
    import gsheet_bridge as g
    for onglet in ("Carport","Pergola aluminium"):
        r=g.call([{"action":"read","sheet":onglet,"range":"A8:C60"}])["result"][0]
        kw_row={}
        for n,row in enumerate(r,start=8):
            if row and row[0]=="Produit": kw_row.setdefault(row[2].strip().lower(),[]).append(n)
        ops=[{"action":"write","sheet":onglet,"range":"L7","values":[["Concurrent 1","Prix concurrent 1","Concurrent 2","Prix concurrent 2","Comparable fiche Ali (autre famille)","Prix comparable"]]}]
        done=set()
        for p in prods:
            if p["onglet"]!=onglet: continue
            for n in kw_row.get(p["kw"].strip().lower(),[]):
                if n in done: continue
                done.add(n); cs=p["concurrents"]
                tcs=p["tentes"]
                vals=[[link(cs[0]) if cs else "", cs[0]["price"] if cs else "", link(cs[1]) if len(cs)>1 else "", cs[1]["price"] if len(cs)>1 else "", link(tcs[0]) if tcs else "", tcs[0]["price"] if tcs else ""]]
                ops.append({"action":"write","sheet":onglet,"range":f"L{n}","values":vals})
                # colonne I (prix cible) : gérée à part depuis la décision Hakim du 09/09 (max(35 %, sous concurrent), un prix par fiche Ali) — ne plus l'écraser ici
        res=g.call(ops); print(onglet,"écrit",len(ops),"ops, ok =",res.get("ok"))
        chk=g.call([{"action":"read","sheet":onglet,"range":"I8:Q60"}])["result"][0]
        bad=[(i+8,c) for i,row in enumerate(chk) for c in row if isinstance(c,str) and c.startswith("#")]
        print(onglet,"erreurs:",bad or "aucune")

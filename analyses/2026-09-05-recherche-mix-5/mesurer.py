"""Runner borné de requêtes de recherche. Secrets chargés localement, jamais exportés."""
import base64, datetime, json, os, pathlib, shlex, sys, urllib.request

ROOT = pathlib.Path(__file__).parent
def run(name, endpoint, payload):
    target = ROOT / 'raw' / (name + '.json')
    if target.exists():
        return json.loads(target.read_text())['response']
    ledger = ROOT / 'couts.jsonl'
    previous = [json.loads(s) for s in ledger.read_text().splitlines()] if ledger.exists() else []
    # USD limit deliberately below the authorized EUR budget. Raise only after FX review.
    if sum(x.get('cost_usd', 0) for x in previous) >= 5:
        raise SystemExit('Plafond interne USD atteint : revoir budget avant nouvel appel.')
    env = dict(os.environ)
    path = pathlib.Path('/Users/Hakim/Documents/Boutiques drop/ecommerce-dropshipping/.env')
    for line in path.read_text().splitlines():
        if line.startswith(('DATAFORSEO_LOGIN=', 'DATAFORSEO_PASSWORD=')):
            k,v=line.split('=',1); env[k]=shlex.split(v)[0] if v else ''
    login,pwd=env.get('DATAFORSEO_LOGIN'),env.get('DATAFORSEO_PASSWORD')
    if not login or not pwd: raise SystemExit('Identifiants DataForSEO manquants')
    auth=base64.b64encode((login+':'+pwd).encode()).decode()
    req=urllib.request.Request('https://api.dataforseo.com/v3/'+endpoint,
        data=json.dumps(payload).encode(),headers={'Authorization':'Basic '+auth,'Content-Type':'application/json'})
    response=json.load(urllib.request.urlopen(req,timeout=120))
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    target.write_text(json.dumps({'fetched_at':now,'endpoint':endpoint,'payload':payload,'response':response},ensure_ascii=False,indent=2)+'\n')
    with ledger.open('a') as f: f.write(json.dumps({'name':name,'at':now,'cost_usd':response.get('cost',0),'endpoint':endpoint})+'\n')
    if response.get('status_code')!=20000 or any(t.get('status_code')!=20000 for t in response.get('tasks',[])):
        raise SystemExit('Réponse API invalide, inspecter les preuves brutes')
    return response

if __name__=='__main__':
    jobs=json.loads((ROOT/'mesure-preparee.json').read_text())
    witnesses=[]
    for job in jobs['requests_in_order']:
        r=run(job['purpose'],jobs['endpoint'],job['payload'])
        rows=r['tasks'][0].get('result')
        if not rows: raise SystemExit('Réponse vide : mesure bloquée')
        if job['purpose'].startswith('witness'):
            v=next((x.get('search_volume') for x in rows if x.get('keyword')=='tufting'),None)
            if not isinstance(v,int) or v<=0: raise SystemExit('Témoin invalide')
            witnesses.append(v)
        print(job['purpose'], 'coût USD',r.get('cost'),'lignes',len(rows),flush=True)
    if len(set(witnesses))!=1: raise SystemExit('Témoins incohérents')
    print('Témoins cohérents',witnesses)

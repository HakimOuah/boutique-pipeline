"""Collecte bornée et auditable ; ne modifie aucun moteur de production."""
import base64, datetime, gzip, hashlib, json, os, pathlib, sys, time, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
API = 'https://api.dataforseo.com/v3/'
BUDGET = 10.0

def credentials():
    p = ROOT.parents[2] / 'ecommerce-dropshipping' / '.env'
    env = dict(os.environ)
    if p.exists():
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line: continue
            k,v = line.removeprefix('export ').split('=',1)
            if k.strip() in ('DATAFORSEO_LOGIN','DATAFORSEO_PASSWORD'):
                env.setdefault(k.strip(), v.strip().strip('\"').strip("'"))
    login, password = env.get('DATAFORSEO_LOGIN'), env.get('DATAFORSEO_PASSWORD')
    if not login or not password: raise RuntimeError('Identifiants DataForSEO indisponibles')
    return 'Basic ' + base64.b64encode((login+':'+password).encode()).decode()

def call(name, endpoint, payload):
    raw = ROOT/'raw'/f'{name}.json.gz'
    if raw.exists(): return json.load(gzip.open(raw,'rt'))
    ledger_path = ROOT/'api-ledger.json'
    ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else []
    if sum(x['cost_usd'] for x in ledger) > BUDGET-0.3:
        raise RuntimeError('Budget de recherche atteint')
    request = urllib.request.Request(API+endpoint, data=json.dumps(payload).encode() if payload is not None else None,
        headers={'Authorization':credentials(),'Content-Type':'application/json'})
    started = time.monotonic()
    response = json.load(urllib.request.urlopen(request, timeout=100))
    obj = {'observed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'endpoint':endpoint,'payload':payload,'response':response}
    raw.parent.mkdir(exist_ok=True)
    with gzip.open(raw,'wt',encoding='utf-8') as f: json.dump(obj,f,ensure_ascii=False)
    ledger.append({'name':name,'endpoint':endpoint,'observed_at_utc':obj['observed_at_utc'],
        'cost_usd':response.get('cost') or 0,'seconds':round(time.monotonic()-started,2),
        'raw':str(raw.relative_to(ROOT)),'sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),
        'status_codes':[t.get('status_code') for t in response.get('tasks',[])]})
    ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
    accepted=(20000,20100) if endpoint.endswith('task_post') else (20000,)
    if response.get('status_code') != 20000 or any(t.get('status_code') not in accepted for t in response.get('tasks',[])):
        raise RuntimeError('DataForSEO : tâche incomplète, voir réponse brute '+name)
    print(name, 'cost_usd='+str(response.get('cost')), flush=True)
    return obj

def witness(name):
    obj=call(name,'keywords_data/google_ads/search_volume/live',
        [{'keywords':['tufting'],'location_name':'France','language_name':'French','search_partners':False}])
    v=obj['response']['tasks'][0]['result'][0]['search_volume']
    if v!=12100: raise RuntimeError('Témoin en échec : '+str(v))
    return v

SEEDS={
 'A1':['antivol vélo','antivol vélo pliant','antivol articulé','antivol pliable'],
 'A2':['appareil photo rétro','appareil photo retro','appareil photo numérique vintage','appareil photo effet vintage','digicam'],
 'A5':['liseuse de poche','petite liseuse','liseuse epub','liseuse compacte','mini-liseuse'],
 'A6':['rasoir de sûreté','rasoir traditionnel','rasoir de sécurité','coffret rasage','kit rasage'],
 'B1':['étendoir mural','sechoir mural','séchoir mural','etendoir rabattable'],
 'B2':['porte vélo mural','accroche vélo','range vélo mural','support vélo pivotant'],
 'B3':['moustiquaire sans perçage','moustiquaire fenêtre sans perçage','moustiquaire magnétique fenêtre'],
 'C2':['casque télévision','casque television','casque sans fil television','casque pour regarder tv'],
 'C6':['poele titane','poele en titane','poêle sans pfas','poele sans teflon'],
}

if __name__=='__main__':
    witness('01-witness-before')
    for cid,seeds in SEEDS.items():
        for i,seed in enumerate(seeds):
            obj=call(f'10-{cid}-labs-{i}','dataforseo_labs/google/keyword_suggestions/live',
                [{'keyword':seed,'location_name':'France','language_name':'French',
                  'limit':1000,'offset':0,'include_serp_info':False,'order_by':['keyword_info.search_volume,desc']}])
            r=obj['response']['tasks'][0]['result'][0]
            print(cid,seed,'rows',r.get('items_count'),'total',r.get('total_count'),flush=True)
    witness('19-witness-after-discovery')

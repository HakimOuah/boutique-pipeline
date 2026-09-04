"""Captures publiques de concurrents, aucune connexion ni écriture distante."""
import concurrent.futures, datetime, gzip, hashlib, html.parser, json, pathlib, urllib.request, urllib.parse
ROOT=pathlib.Path(__file__).resolve().parent
class VisibleText(html.parser.HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.text=[];self.links=[];self.href=None;self.label=[]
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if tag in ('script','style','noscript','svg'):self.skip+=1
  if tag=='a':self.href=attrs.get('href');self.label=[]
 def handle_endtag(self,tag):
  if tag in ('script','style','noscript','svg'):self.skip=max(0,self.skip-1)
  if tag=='a' and self.href:self.links.append({'href':self.href,'text':' '.join(self.label)});self.href=None
 def handle_data(self,data):
  if not self.skip and data.strip():
   self.text.append(data.strip())
   if self.href:self.label.append(data.strip())

URLS={
 'A1-decathlon':'https://www.decathlon.fr/p/antivol-velo-abus-pliant-bordo/_/R-p-X8130253',
 'A2-timelens':'https://timelens.fr/products/appareil-photo-timelens%C2%AE-kaki',
 'A5-xteink':'https://www.xteink.com/fr/products/xteink-x3',
 # A6-lamier exclu le 04/09 : mauvais domaine. Captures officielles dans le dossier d'approfondissement.
 'A6-bouc':'https://www.leboucfrancais.fr/boutique/coffret-rasage-a-lancienne-noir/',
 'B1-foxydry':'https://www.foxydry.com/fr-fr/products/foxydry-hide-sechoir-mural-extensible',
 'B1-univers':'https://univers-etendoir.com/products/etendoir-a-linge-mural-rabattable-inox-pliant',
 'B2-bike24':'https://www.bike24.fr/marques/steadyrack',
 'B2-onvelo':'https://www.onvelo.fr/support-mural-pivotant-classique-steadyrack-b11b93/',
 'B2-cyclmania':'https://cyclmania.com/products/support-velo-adjustablebikestand',
 'B3-windhager':'https://www.windhager.eu/fr/Produits/PLUS-Magnetic-window-screen_a_55498',
 'C2-avantree':'https://avantree.com/fr/products/ht5009-bluetooth-tv-casque-emetteur-set',
 'C6-titanox':'https://titanoxfrance.com/products/titanox-poele-en-titane-pur-sans-pfas',
}
EXTRA={ 'A1':['antivol-store.com','abus.com'], 'A2':['papershoot.fr','kodak.gtcie.com'],
 'A5':['ereader.kobo.com'], 'A6':['rasage-classique.com'],
 'B1':['leifheit.fr','brabantia.com','aeraly.com'], 'B2':['vddworld.fr','sprintis.fr'],
 'B3':['avosdim.com','gifi.fr','moustikit.com'], 'C2':['cgv.fr','laboutiquederic.com','electrodepot.fr'],
 'C6':['onox','titane','inox']}
def urls_from_serps():
 for cid,domains in EXTRA.items():
  for f in sorted((ROOT/'raw').glob('30-'+cid+'-serp-*.gz')):
   j=json.load(gzip.open(f,'rt'))
   for r in j['response']['tasks'][0].get('result') or []:
    for x in r.get('items') or []:
     if x['type']=='organic' and x.get('url') and any(d in x.get('domain','') for d in domains):
      name=cid+'-'+x['domain'].removeprefix('www.').replace('.','-')
      URLS.setdefault(name,x['url'])
def fetch(name,url):
 p=ROOT/'concurrence/raw'/name;p.mkdir(parents=True,exist_ok=True)
 if (p/'capture.json').exists():return name+' cached'
 data={'observed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'requested_url':url}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; Research/1.0)'})
  with urllib.request.urlopen(req,timeout=30) as resp:
   raw=resp.read();data.update(status=resp.status,final_url=resp.url)
  with gzip.open(p/'page.html.gz','wb') as f:f.write(raw)
  parser=VisibleText();parser.feed(raw.decode('utf-8','replace'))
  (p/'page.txt').write_text('\n'.join(line.rstrip() for line in '\n'.join(parser.text).splitlines())+'\n')
  data['links']=[{'url':urllib.parse.urljoin(data['final_url'],x['href']),'text':x['text']} for x in parser.links]
  data['sha256']=hashlib.sha256(raw).hexdigest()
 except Exception as exc:data.update(status='MANQUANT',error=str(exc))
 (p/'capture.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 return name+' '+str(data['status'])
if __name__=='__main__':
 urls_from_serps();(ROOT/'concurrence').mkdir(exist_ok=True)
 (ROOT/'concurrence/urls.json').write_text(json.dumps(URLS,ensure_ascii=False,indent=2)+'\n')
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  jobs=[pool.submit(fetch,name,url) for name,url in URLS.items()]
  for job in concurrent.futures.as_completed(jobs):print(job.result(),flush=True)

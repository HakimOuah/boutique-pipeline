import json
import re
from datetime import datetime, timezone
from pathlib import Path

OUT=Path('/tmp/uk-cont4-sourcing-20260907')

def read_jsonl(path):
    rows=[]
    p=Path(path)
    if not p.exists(): return rows
    for line in p.read_text().splitlines():
        if line.startswith('{'):
            try: rows.append(json.loads(line))
            except json.JSONDecodeError: pass
    return rows

search=read_jsonl(OUT/'search.jsonl'); gets=read_jsonl(OUT/'details.jsonl'); freight=read_jsonl(OUT/'freight-gbp.jsonl')
prior_gets=read_jsonl('/tmp/uk-cont3-sourcing-20260907/details.jsonl')
prior_freight=read_jsonl('/tmp/uk-cont3-sourcing-20260907/freight-gbp.jsonl')

def find(rows,pid):
    for row in rows:
        if str(row.get('product_id'))==pid: return row
    return {}

def search_item(pid):
    for row in search:
        for it in row.get('items',[]):
            if str(it.get('itemId') or it.get('productId'))==pid: return it
    return {}

def urls_from(obj):
    out=[]
    def rec(x):
        if isinstance(x,dict):
            for v in x.values(): rec(v)
        elif isinstance(x,list):
            for v in x: rec(v)
        elif isinstance(x,str):
            for u in re.findall(r'https?://[^\s";<>]+',x):
                if 'aliexpress' in u or 'alicdn' in u: out.append(u.rstrip(',.'))
    rec(obj)
    return list(dict.fromkeys(out))

def pics(pid, prior=False):
    rows=prior_gets if prior else gets
    out=[]
    if not prior:
        it=search_item(pid)
        if it.get('itemMainPic'): out.append(it['itemMainPic'])
    row=find(rows,pid)
    if row: out.extend(urls_from(row.get('raw',{})))
    return list(dict.fromkeys(out))[:8]

offers=[
 {
  'family':'mirror_current_result','product_id':'1005009302227146','sku_id':'12000048720354462','sku_label':'12 Bulbs',
  'url':'https://www.aliexpress.com/item/1005009302227146.html?skuId=12000048720354462','title':'Hollywood mirror 12 LED bulbs','price_gbp':41.49,'stock_declared':35,'components_declared':'Integrated 11.8×16.1in metal+glass mirror, 12 bulbs, three light modes, dimming, touch, 360° tilt, adapter in package; no battery.','freight':'Previous direct quote returned DELIVERY_SERVICE_EXCEPTION; no cost/delay proof.','status':'CURRENT_BEST_NO_FREIGHT','image_urls_to_verify':pics('1005009302227146',prior=True)
 },
 {
  'family':'mirror_current_result','product_id':'1005008716524342','sku_id':'12000046631678830','sku_label':'Black / 50x42cm / plug property id 201336100',
  'url':'https://www.aliexpress.com/item/1005008716524342.html?skuId=12000046631678830','title':'Hollywood wall mirror plug-in and USB charger port','price_gbp':93.59,'stock_declared':175,'components_declared':'Title declares plug-in/USB charger port and wall mounting; battery no. API detail does not itemize adapter or full box contents.','freight':'No freight in this pass.','status':'OVER_TARGET_PRICE','image_urls_to_verify':pics('1005008716524342',prior=True)
 },
 {
  'family':'mirror_new_usb','product_id':'1005006404879088','sku_id':'12000037064826646','sku_label':'30cm Black / plug 201336100',
  'url':'https://www.aliexpress.com/item/1005006404879088.html?skuId=12000037064826646','title':'Tabletop LED vanity mirror 30cm','price_gbp':56.39,'stock_declared':180,'sales_declared':10,'components_declared':'30×28cm metal+glass mirror, 3 colour modes, dimming, 360° rotation, detachable 15× magnifying mirror, 12V/2A adapter, 1.2m cable, 30W; plug 100–240V and adapter sent according to address.','freight':{'fee_gbp':0,'free_shipping':True,'min_days':6,'max_days':13,'delivery_date_desc':'Sep 13 - 20','ship_from_country':'CN','total_gbp':56.39,'service':'AliExpress standard shipping'},'status':'NEAR_MISS_COST','image_urls_to_verify':pics('1005006404879088')
 },
 {
  'family':'watch_winder','product_id':'1005006786141635','sku_id':'12000038298689118','sku_label':'Black / 2 slots',
  'url':'https://www.aliexpress.com/item/1005006786141635.html?skuId=12000038298689118','title':'Double watch winder PU leather 2 slots','price_gbp':28.69,'stock_declared':2,'sales_declared':358,'components_declared':'Two-slot automatic winder, removable pillows, Japanese quiet/antimagnetic motor, two rotation modes, USB cable included. USB wall plug not included; no battery; PU leather rather than wood.','freight':{'fee_gbp':1.99,'min_days':4,'max_days':8,'delivery_date_desc':'Sep 11 - 15','ship_from_country':'CN','total_gbp':30.68,'service':'AliExpress Selection Premium shipping'},'status':'GO_CANDIDATE_USB_LOW_STOCK','image_urls_to_verify':pics('1005006786141635')
 },
 {
  'family':'watch_winder','product_id':'1005012217866893','sku_id':'12000057777061832','sku_label':'CC-J-B1',
  'url':'https://www.aliexpress.com/item/1005012217866893.html?skuId=12000057777061832','title':'2 Watch Winder Box Automatic USB Power Luxury Wooden Watch Box','price_gbp':26.79,'stock_declared':197,'sales_declared':15,'components_declared':'Title declares USB power, two-watch winder and luxury wooden box; product properties say Material Leather and product_get text is empty, so wood finish and USB cable are not verified.','freight':None,'status':'WATCH_COMPONENT_PROOF','image_urls_to_verify':pics('1005012217866893')
 },
 {
  'family':'wood_watch_box','product_id':'1005008635238967','sku_id':'12000046041901233','sku_label':'Black 12 Grids',
  'url':'https://www.aliexpress.com/item/1005008635238967.html?skuId=12000046041901233','title':'Wooden Watch Box ... 1/2/3/5/6/10/12 Slots','price_gbp':29.49,'stock_declared':37,'sales_declared':800,'components_declared':'12-grid black option; API properties say wood/MDF, removable pillows, case for watches/jewelry. No freight queried.','freight':None,'status':'WATCH_MDF_FINISH','image_urls_to_verify':pics('1005008635238967')
 },
 {
  'family':'wood_watch_box','product_id':'32839469711','sku_id':'12000032606672985','sku_label':'Style 1 / 10 slots',
  'url':'https://www.aliexpress.com/item/32839469711.html?skuId=12000032606672985','title':'10 Slots Wood Watch Case ... Luxury Solid Wood','price_gbp':35.09,'stock_declared':39871,'sales_declared':7,'components_declared':'10-slot style, declared solid wood title; API gives wood/mixed materials, 29.8×20.5×10.5cm, watch-display box. Finish and cushion contents need photo/sample verification.','freight':{'fee_gbp':5.35,'min_days':6,'max_days':13,'delivery_date_desc':'Sep 13 - 20','ship_from_country':'CN','total_gbp':40.44,'service':'AliExpress standard shipping'},'status':'GO_CANDIDATE_STORAGE_DECLARATIVE','image_urls_to_verify':pics('32839469711')
 },
]

scope={'destination':'GB','currency':'GBP','language':'en_GB','queries':['vanity mirror LED USB 40cm','automatic watch winder box 2 watches','wood watch storage box 10 watches'],'rows_per_query':20,'product_get_count':5,'freight_query_count':3}
manifest={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'scope':scope,'offers':offers,'image_verification_note':'Image URLs are provided for root visual verification; no images downloaded by this run.'}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2,default=str)+'\n')

evidence={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'scope':scope,'manifest':'manifest.json','offers_extracted':offers,'raw_search_responses':search,'raw_product_get_responses':gets,'raw_freight_responses':freight,'prior_mirror_raw_product_get_responses':prior_gets,'prior_mirror_raw_freight_responses':prior_freight,'limitations':[
 'AliExpress/API declarations only; no purchase, sample, supplier message or physical plug/finish test.',
 'All successful direct freight options ship from CN; no UK source observed.',
 'The new mirror is a complete declared kit at £56.39 with free 6–13 day freight, £1.39 above the £55 target. The current £41.49 mirror has a delivery service exception.',
 'The winder has explicit USB cable but only stock 2 and PU leather; the wooden USB candidate has contradictory Leather material and no text detail.',
 'Storage box Style 1 is a declared wood/solid-wood 10-slot item with total £40.44; actual finish, cushions and construction remain unverified.',
 'delivery_time fields were not used as delivery proof; direct freight windows are reported.'
]}
(OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2,default=str)+'\n')

report='''# Sourcing UK — miroirs USB et univers montres

**Périmètre API (07/09/2026)** — 3 recherches de 20 résultats, 5 nouveaux `product_get` (1 miroir + 4 montres), 3 frets directs GBP. Les deux miroirs de la passe précédente sont repris avec leurs preuves brutes ; les URLs photo SKU sont dans [manifest.json](./manifest.json) pour vérification root.

**Miroir : aucun GO sous £55.** Le meilleur nouveau résultat complet est [1005006404879088](https://www.aliexpress.com/item/1005006404879088.html?skuId=12000037064826646), SKU noir 30cm, £56.39, stock 180. Il déclare miroir métal/verre 30×28cm, 3 modes, dimming, rotation 360°, miroir grossissant détachable, adaptateur 12V/2A, câble 1.2m et prise 100–240V. Fret CN gratuit, 6–13 jours : rendu **£56.39**, £1.39 au-dessus de la cible. Le miroir actuel 12 ampoules `1005009302227146` reste à £41.49 mais son fret renvoie `DELIVERY_SERVICE_EXCEPTION`; l’alternative murale `1005008716524342` est £93.59.

**Remontoir : candidat USB mais stock très bas.** [1005006786141635](https://www.aliexpress.com/item/1005006786141635.html?skuId=12000038298689118), SKU noir 2 emplacements, £28.69, 358 ventes mais stock 2. Moteur japonais silencieux, deux modes, coussins amovibles et câble USB inclus ; bloc secteur USB non inclus, boîtier PU cuir. Fret CN £1.99, 4–8 jours, rendu **£30.68**. Le candidat titre « wooden USB » `1005012217866893` est £26.79, stock 197, mais la propriété API indique Leather et le détail textuel est vide.

**Coffret bois : meilleur candidat stockage.** [32839469711](https://www.aliexpress.com/item/32839469711.html?skuId=12000032606672985), SKU `Style 1 / 10 slots`, £35.09, stock 39,871, dimensions API 29.8×20.5×10.5cm. Le titre déclare solid wood, l’API wood/mixed materials ; fret CN £5.35, 6–13 jours, rendu **£40.44**. Le 12-grids MDF `1005008635238967` coûte £29.49, stock 37, sans fret vérifié.

Les prix, stocks, prises, finition et contenus restent déclaratifs jusqu’au contrôle photo puis à l’échantillon. Le champ `delivery_time` ne remplace pas les devis directs.
'''
(OUT/'report.md').write_text(report)
print(json.dumps({'report':str(OUT/'report.md'),'evidence':str(OUT/'evidence.json'),'manifest':str(OUT/'manifest.json'),'report_words':len(re.findall(r"\b\w+[’'-]?\w*\b",report))},ensure_ascii=False))

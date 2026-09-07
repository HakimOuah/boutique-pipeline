import json
import re
from datetime import datetime, timezone
from pathlib import Path

OUT = Path('/tmp/uk-cont3-sourcing-20260907')

def read_jsonl(name):
    rows=[]
    for line in (OUT/name).read_text().splitlines():
        if line.startswith('{'):
            try: rows.append(json.loads(line))
            except json.JSONDecodeError: pass
    return rows

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

search=read_jsonl('search.jsonl'); gets=read_jsonl('details.jsonl'); freight=read_jsonl('freight-gbp.jsonl')

def item(pid):
    for row in search:
        for it in row.get('items',[]):
            if str(it.get('itemId') or it.get('productId'))==pid: return it
    return {}

def get(pid):
    for row in gets:
        if row.get('product_id')==pid: return row
    return {}

def pics(pid):
    out=[]
    it=item(pid)
    if it.get('itemMainPic'): out.append(it['itemMainPic'])
    row=get(pid)
    if row: out.extend(urls_from(row.get('raw',{})))
    return list(dict.fromkeys(out))[:8]

offers=[
 {
  'family':'orthopedic_dog_bed_large','product_id':'1005009119696851','sku_id':'12000047983252996','sku_label':'107X76X17CM',
  'url':'https://www.aliexpress.com/item/1005009119696851.html?skuId=12000047983252996','title':'Orthopedic Dog Bed for Large Dogs — Waterproof Sofa-Style Bed',
  'price_gbp':50.79,'stock_declared':22,'sales_declared':45,'components_declared':'Sofa-style dog bed, removable washable cover, non-slip base, orthopedic/joint support title; 107×76×17cm variant. XL 122×89×17cm variants also exist at £65.99–£80.99, stock 31–40.','freight':{'fee_gbp':1.99,'min_days':25,'max_days':42,'delivery_date_desc':'Oct 02 - 19','ship_from_country':'CN','total_gbp':52.78,'service':'AliExpress Selection Shipping for Oversized Goods'},'status':'NO_GO_DELAY','image_urls_to_verify':pics('1005009119696851')
 },
 {
  'family':'orthopedic_dog_bed_large','product_id':'1005001609237572','sku_id':None,'sku_label':None,'url':'https://www.aliexpress.com/item/1005001609237572.html','title':'Orthopedic Leather Dog Bed Sofa','price_gbp':48.69,'stock_declared':None,'sales_declared':81,'components_declared':None,'freight':None,'status':'PRODUCT_GET_FAILED_ITEM_NOT_FOUND','image_urls_to_verify':pics('1005001609237572')
 },
 {
  'family':'digital_photo_frame_wifi_10in','product_id':'1005005545336780','sku_id':'12000057139115817','sku_label':'BLACK built in 64GB / plug property id 201447606',
  'url':'https://www.aliexpress.com/item/1005005545336780.html?skuId=12000057139115817','title':'Frameo Digital Picture Frame 10.1 Inch 32GB/64GB WiFi',
  'price_gbp':59.19,'stock_declared':6,'sales_declared':'1,000+','components_declared':'10.1in 1280×800 IPS touch, Frameo app, built-in 64GB variant, auto-rotate, wall mount, holder, power adapter, manual; USB flash support. Product properties say inbox adaptor yes and USB 5–20V DC. Plug property is numeric id 201447606 with no human label in API; verify UK plug visually.','freight':{'fee_gbp':1.99,'min_days':6,'max_days':10,'delivery_date_desc':'Sep 13 - 17','ship_from_country':'CN','total_gbp':61.18,'service':'AliExpress Selection Premium shipping'},'status':'GO_CANDIDATE_UK_PLUG_VERIFY','image_urls_to_verify':pics('1005005545336780')
 },
 {
  'family':'digital_photo_frame_wifi_10in','product_id':'1005007526279962','sku_id':'12000057821025034','sku_label':'black / plug property id 201447606',
  'url':'https://www.aliexpress.com/item/1005007526279962.html?skuId=12000057821025034','title':'Frameo 10.1 Inch WiFi Digital Picture Frame 32GB',
  'price_gbp':59.39,'stock_declared':3,'sales_declared':59,'components_declared':'10.1in 1280×800 IPS touch, Frameo app, built-in 32GB, wall mount/removable stand, power adapter, manual; TF card max 32GB not included. Plug property id 201447606 has no human label in API; verify UK plug visually.','freight':None,'status':'WATCH_UK_PLUG_VERIFY','image_urls_to_verify':pics('1005007526279962')
 },
 {
  'family':'hollywood_vanity_mirror_lights','product_id':'1005009302227146','sku_id':'12000048720354462','sku_label':'12 Bulbs',
  'url':'https://www.aliexpress.com/item/1005009302227146.html?skuId=12000048720354462','title':'Vanity Mirror with Lights Hollywood Makeup Mirror with 12 LED Bulbs',
  'price_gbp':41.49,'stock_declared':35,'sales_declared':9,'components_declared':'Integrated 11.8×16.1in metal+glass mirror, 12 dimmable bulbs, warm/daylight/cold modes, touch controls, 360° tilt, power adapter declared in package; battery not included, no assembly. UK plug type not documented.','freight':None,'status':'FREIGHT_SERVICE_EXCEPTION','image_urls_to_verify':pics('1005009302227146')
 },
 {
  'family':'hollywood_vanity_mirror_lights','product_id':'1005008716524342','sku_id':'12000046631678830','sku_label':'Black / 50x42cm / plug property id 201336100',
  'url':'https://www.aliexpress.com/item/1005008716524342.html?skuId=12000046631678830','title':'Vanity Mirror with Lights Hollywood ... Plug-in and USB Charger Port',
  'price_gbp':93.59,'stock_declared':175,'sales_declared':4,'components_declared':'50×42cm black variant; title declares plug-in and USB charger port, wall-mounted. Battery no; product text only says table/wall placement, so adapter/UK plug/package contents need photo confirmation.','freight':None,'status':'WATCH_UNQUOTED','image_urls_to_verify':pics('1005008716524342')
 },
]

scope={'destination':'GB','currency':'GBP','language':'en_GB','queries':['orthopedic dog bed large','digital photo frame wifi 10 inch','hollywood vanity mirror lights'],'rows_per_query':20,'product_get_count':6,'freight_query_count':3}
families=[
 {'family':'orthopedic_dog_bed_large','freight_checked_sku':'12000047983252996','status':'NO_GO_DELAY'},
 {'family':'digital_photo_frame_wifi_10in','freight_checked_sku':'12000057139115817','status':'GO_CANDIDATE_UK_PLUG_VERIFY'},
 {'family':'hollywood_vanity_mirror_lights','freight_checked_sku':'12000048720354462','status':'FREIGHT_SERVICE_EXCEPTION'},
]
manifest={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'scope':scope,'families':families,'offers':offers,'image_verification_note':'Image URLs are provided for root visual verification; this run did not download images.'}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2,default=str)+'\n')

evidence={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'scope':scope,'manifest':'manifest.json','offers_extracted':offers,'raw_search_responses':search,'raw_product_get_responses':gets,'raw_freight_responses':freight,'limitations':[
 'AliExpress/API declarations only; no purchase, sample, supplier message or physical plug/size/foam test.',
 'All successful direct freight options ship from CN; mirror freight returned DELIVERY_SERVICE_EXCEPTION and has no delivery proof.',
 'Dog bed 107×76cm is a complete textual bed listing but freight is 25–42 days. XL variants exist but were not freight-quoted.',
 'Frame plug property IDs were returned without human-readable labels; UK plug is not asserted until root visual verification.',
 'Mirror #1 declares package adapter and integrated 12 bulbs but no UK plug type; mirror #2 title mentions plug-in/USB but package contents remain unverified.',
 'logistics_info_dto delivery_time values were not used as delivery proof; direct freight results are reported.'
]}
(OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2,default=str)+'\n')

report='''# Sourcing UK — lit XL / cadre Frameo / miroir Hollywood

**Périmètre API (07/09/2026)** — 3 recherches de 20 résultats en `en_GB/GB/GBP`, 6 `product_get` (un lit `ITEM_ID_NOT_FOUND`), 3 frets directs GBP. Les URLs de photos SKU sont dans [manifest.json](./manifest.json) pour vérification visuelle par root ; aucune image n’a été téléchargée ici.

**Deux pistes les plus prometteuses : cadre Frameo et miroir 12 ampoules, sous réserve prise/fret.**

**Cadre — candidat GO déclaratif, prise UK à vérifier.** [1005005545336780](https://www.aliexpress.com/item/1005005545336780.html?skuId=12000057139115817), SKU `BLACK built in 64GB / plug property id 201447606`, £59.19, stock 6, 1,000+ ventes. 10.1″ IPS tactile 1280×800, Frameo app, 64GB intégré, rotation, support mural/holder, adaptateur et manuel déclarés. Fret direct CN £1.99, 6–10 jours, rendu **£61.18**. L’API confirme l’adaptateur mais ne traduit pas l’identifiant de prise `201447606` : ne pas appeler UK plug avant contrôle photo.

**Miroir — kit complet déclaré, fret bloqué.** [1005009302227146](https://www.aliexpress.com/item/1005009302227146.html?skuId=12000048720354462), SKU `12 Bulbs`, £41.49, stock 35, 9 ventes. Miroir métal/verre intégré 11.8×16.1″, 12 ampoules, trois températures, variation tactile, rotation 360°, adaptateur déclaré, sans batterie ni assemblage. Le fret direct a retourné `DELIVERY_SERVICE_EXCEPTION` : aucun coût/délai rendu validable.

**Lit chien — complet mais hors délai.** [1005009119696851](https://www.aliexpress.com/item/1005009119696851.html?skuId=12000047983252996), SKU `107X76X17CM`, £50.79, stock 22, 45 ventes. Housse lavable, base antidérapante, support articulaire, lit sofa ; variantes XL 122×89×17cm à £65.99–£80.99. Fret £1.99 mais **25–42 jours**, rendu £52.78. L’autre candidat lit a échoué `ITEM_ID_NOT_FOUND`.

Les prix, stocks, prises, adaptateurs et contenus restent déclaratifs. Les champs `delivery_time=7` ne remplacent pas un devis direct ; les frets réussis partent de CN.
'''
(OUT/'report.md').write_text(report)
print(json.dumps({'report':str(OUT/'report.md'),'evidence':str(OUT/'evidence.json'),'manifest':str(OUT/'manifest.json'),'report_words':len(re.findall(r"\b\w+[’'-]?\w*\b",report))},ensure_ascii=False))

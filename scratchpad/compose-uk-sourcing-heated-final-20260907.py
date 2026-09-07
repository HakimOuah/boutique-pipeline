import json
import re
from datetime import datetime, timezone
from pathlib import Path

OUT=Path('/tmp/uk-sourcing-heated-final-20260907')

def read_jsonl(name):
    rows=[]
    for line in (OUT/name).read_text().splitlines():
        if line.startswith('{'):
            try: rows.append(json.loads(line))
            except json.JSONDecodeError: pass
    return rows

search=read_jsonl('search.jsonl'); gets=read_jsonl('details.jsonl'); freight=read_jsonl('freight-gbp.jsonl'); battery_freight=read_jsonl('battery-freight-gbp.jsonl')

offers=[
 {
  'product_id':'1005010031480359',
  'url':'https://www.aliexpress.com/item/1005010031480359.html?skuId=12000057722704041',
  'title':'Heating Vest USB Powered V-Neck ... Unisex',
  'search_query':'heated vest battery', 'sku_id':'12000057722704041',
  'sku_label':'L-XL; Black v-neck vest', 'price_gbp':30.79, 'stock_declared':9998, 'sales_declared':5,
  'contents_declared':'Adult/unisex USB-powered vest option. Battery options exist as separate SKU labels (10,000mAh and 20,000mAh), but the product_get response does not prove that a battery is included with this vest SKU.',
  'heating_claims':'No number of heating zones or measured output is documented in the inspected text.',
  'freight_options':[{'service':'AliExpress Selection Standard','fee_gbp':1.99,'free_shipping':False,'min_days':7,'max_days':11,'delivery_date_desc':'Sep 14 - 18','ship_from_country':'CN','total_gbp':32.78}],
  'store_country':'CN',
  'separate_battery_variants':[{
   'label':'L-XL; 10 000 mah battery','price_gbp':12.29,'stock_declared':9999,'sku_id':'12000057722704051',
   'freight':{'service':'AliExpress Selection Standard','fee_gbp':1.99,'min_days':7,'max_days':11,'delivery_date_desc':'Sep 14 - 18','ship_from_country':'CN','total_gbp':14.28},
   'visual_listing_evidence':{'url':'https://ae01.alicdn.com/kf/S9a1f993e4dc84dc0839ade1fe5e9b263h.jpg','declared_text':'5V; 10000mAh; capacity 10000mAh/3.7V; input 5V/2.1A; output 5V/2A; Micro USB input; Type C cable; dimensions 115*68*28mm','source':'exact SKU image observed through CUA; visual listing declaration only'}
  },{
   'label':'L-XL; 20 000 mah battery','price_gbp':25.59,'stock_declared':9997,'sku_id':'12000057722704036','freight_not_checked':True
  }],
  'two_parcel_declared_total_gbp':47.06,
 },
 {
  'product_id':'1005010304838584',
  'url':'https://www.aliexpress.com/item/1005010304838584.html?skuId=12000051868730059',
  'title':"High-quality men's and women's electric heating vest",
  'search_query':'heated vest battery', 'sku_id':'12000051868730059',
  'sku_label':'single listing / adult vest candidate', 'price_gbp':94.06, 'stock_declared':99, 'sales_declared':0,
  'contents_declared':'One unparameterized listing; no battery, powerbank, vest size or kit contents documented in product_get.',
  'heating_claims':'No heating-zone count or output is documented. Product properties are internally poor match (Hand Tool Parts, Rubber) despite the title.',
  'freight_options':[{'service':'AliExpress Shipping for Large Goods by Land','fee_gbp':50.38,'free_shipping':False,'min_days':10,'max_days':41,'delivery_date_desc':'Sep. 17 - Oct. 18','ship_from_country':'CN','total_gbp':144.44},{'service':'AliExpress standard shipping','fee_gbp':53.34,'free_shipping':False,'min_days':6,'max_days':13,'delivery_date_desc':'Sep 13 - 20','ship_from_country':'CN','total_gbp':147.40}],
  'store_country':'CN'
 }
]

evidence={
 'checked_at_utc':datetime.now(timezone.utc).isoformat(),
 'scope':{'destination':'GB','currency':'GBP','language':'en_GB','text_search_queries':['heated vest battery'],'rows_per_query':20,'product_get_count':2,'freight_query_count':3,'shipping_method':'direct METHOD_FREIGHT_QUERY; shipping_fee_cent is already a GBP value'},
 'offers_extracted':offers,
 'raw_search_responses':search,'raw_product_get_responses':gets,'raw_freight_responses':freight,'raw_battery_freight_responses':battery_freight,
 'limitations':[
  'AliExpress/API declarations only; no purchase, sample, in-box battery verification, electrical test or supplier message.',
  'No UK source observed; inspected stores and freight ship_from_country are CN.',
  'The best adult vest SKU is explicitly vest-only in the variant label. The separate 10,000mAh SKU has its own direct quote; buying both implies two parcels and a declared combined total of £47.06, with no combined-shipping discount proof.',
  'The exact battery image declares 5V, 10,000mAh, 5V/2.1A input, 5V/2A output, Micro USB input and Type-C cable. This is listing evidence only; the vest listing does not document its required amperage, connector, runtime or heating performance.',
  'No 9-zone claim, heat map, wattage, runtime, safety or conformity evidence was documented.',
  'Direct freight windows are used; logistics_info_dto delivery_time=7 is not treated as proof.',
 ]
}
(OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2,default=str)+'\n')

report='''# Sourcing UK — gilet chauffant adulte

**Périmètre API (07/09/2026)** — 1 recherche de 20 résultats (`heated vest battery`) en `en_GB/GB/GBP`, 2 `product_get`, puis 3 frets directs GBP (dont le devis complémentaire de la batterie). Aucun achat ni contact fournisseur.

**Résultat : TECHNICAL_WATCH.** Le meilleur assemblage déclaré est un achat en deux colis : gilet £32.78 rendu + batterie séparée £14.28 rendue = **£47.06**. Cela dépasse la cible indicative de £40 mais reste étudiable pour un prix de vente £99 ; la compatibilité électrique reste déclarative.

1. [1005010031480359](https://www.aliexpress.com/item/1005010031480359.html?skuId=12000057722704041) — SKU `12000057722704041`, **L-XL; Black v-neck vest**, £30.79, stock déclaré 9,998, 5 ventes. Le titre déclare un gilet chauffant USB unisexe adulte. Fret direct CN £1.99, **7–11 jours** (14–18 septembre), rendu **£32.78**. La batterie séparée [SKU `12000057722704051`](https://www.aliexpress.com/item/1005010031480359.html?skuId=12000057722704051) coûte £12.29, stock 9,999, avec fret direct CN £1.99 et 7–11 jours : colis batterie **£14.28**. L’image exacte ([preuve](https://ae01.alicdn.com/kf/S9a1f993e4dc84dc0839ade1fe5e9b263h.jpg)) déclare 5V, 10,000mAh, entrée 5V/2.1A, sortie 5V/2A et câble Type-C. Total déclaré en deux colis : **£47.06**. Le gilet et la batterie sont compatibles sur le papier USB 5V/2A, mais aucun test, connecteur requis, autonomie ou performance de chauffe n’est vérifié ; aucun nombre de zones n’est documenté.

2. [1005010304838584](https://www.aliexpress.com/item/1005010304838584.html?skuId=12000051868730059) — SKU `12000051868730059`, fiche adulte hommes/femmes, £94.06, stock 99. La fiche ne documente ni batterie, ni taille, ni contenu du pack ; ses propriétés remontent même `Hand Tool Parts` et `Rubber`, incohérents avec le titre. Fret £50.38, 10–41 jours, rendu £144.44 ; ou £53.34, 6–13 jours, rendu £147.40. Éliminé par prix, délai et preuve insuffisante.

Les deux vendeurs et frets indiquent CN. Le champ `delivery_time=7` n’est pas retenu comme preuve. Ne pas présenter le gilet à £30.79 comme pack batterie intégré : le pack à £47.06 est une hypothèse d’achat en deux colis, sans preuve de regroupement. Aucun claim « 9 zones » n’a été validé.
'''
(OUT/'report.md').write_text(report)
print(json.dumps({'report':str(OUT/'report.md'),'evidence':str(OUT/'evidence.json'),'report_words':len(re.findall(r"\\b\\w+[’'-]?\\w*\\b",report))},ensure_ascii=False))

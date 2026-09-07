import json
import re
from datetime import datetime, timezone
from pathlib import Path

OUT = Path('/tmp/uk-sourcing-q4-final-20260907')

def read_jsonl(name):
    rows=[]
    for line in (OUT/name).read_text().splitlines():
        if line.startswith('{'):
            try: rows.append(json.loads(line))
            except json.JSONDecodeError: pass
    return rows

search=read_jsonl('search.jsonl')
gets=read_jsonl('details.jsonl')
freight=read_jsonl('freight-gbp.jsonl')

offers=[
 {
  'category':'wooden chess', 'product_id':'1005008086495961',
  'url':'https://www.aliexpress.com/item/1005008086495961.html?skuId=12000043641691985',
  'title':'39cm/15in Wooden Chess Set Handmade Extra Queens, Foldable Portable',
  'search_query':'wooden chess set 40cm', 'sku_id':'12000043641691985',
  'sku_label':'chess set', 'size_declared':'39cm / 15in', 'material_declared':'Wooden',
  'price_gbp':35.19, 'stock_declared':10, 'sales_declared':26,
  'contents_declared':'Listing title declares a foldable chess set and extra queens; exact 32-piece count is not present in product_get text (mobile detail is image-only).',
  'freight_options':[{'service':'AliExpress Selection Premium shipping','fee_gbp':1.99,'free_shipping':False,'min_days':4,'max_days':8,'delivery_date_desc':'Sep 11 - 15','ship_from_country':'CN','total_gbp':37.18}],
  'store_country':'CN'
 },
 {
  'category':'wooden chess', 'product_id':'1005012070192886',
  'url':'https://www.aliexpress.com/item/1005012070192886.html?skuId=12000057442920193',
  'title':'45cm / 17.7in Eewood large solid wood chessboard, electroplated + acrylic king',
  'search_query':'wooden chess set 40cm', 'sku_id':'12000057442920193',
  'sku_label':'1 set', 'size_declared':'45cm / 17.7in; king 9cm high', 'material_declared':'Wooden; acrylic king declared in title',
  'price_gbp':95.79, 'stock_declared':987, 'sales_declared':14,
  'contents_declared':'Product title and SKU declare 1 set; product_get has no textual 32-piece count (mobile detail is image-only).',
  'freight_options':[{'service':'AliExpress Selection Premium shipping','fee_gbp':1.99,'free_shipping':False,'min_days':6,'max_days':10,'delivery_date_desc':'Sep 13 - 17','ship_from_country':'CN','total_gbp':97.78}],
  'store_country':'CN'
 },
 {
  'category':'crystal bowl', 'product_id':'1005009424303397',
  'url':'https://www.aliexpress.com/item/1005009424303397.html?skuId=12000049055056832',
  'title':'Crystal Singing Bowl Transparent Rainbow',
  'search_query':'crystal singing bowl set', 'sku_id':'12000049055056832',
  'sku_label':'5inch A4', 'size_declared':'5 inch; single tone A4', 'material_declared':'Crystal; seller text says 99% pure crystal',
  'price_gbp':121.79, 'stock_declared':50, 'sales_declared':None,
  'contents_declared':'Accessory field declares mallet and O-ring. This selected SKU is one bowl/tone, not a multi-bowl set; 432Hz/440Hz is declared at listing level.',
  'freight_options':[{'service':'AliExpress standard shipping','fee_gbp':0,'free_shipping':True,'min_days':11,'max_days':18,'delivery_date_desc':'Sep 18 - 25','ship_from_country':'CN','total_gbp':121.79},{'service':'AliExpress Premium shipping','fee_gbp':36.42,'free_shipping':False,'min_days':11,'max_days':16,'delivery_date_desc':'Sep 18 - 23','ship_from_country':'CN','total_gbp':158.21}],
  'store_country':'CN'
 },
 {
  'category':'crystal bowl excluded', 'product_id':'1005009030731602',
  'url':'https://www.aliexpress.com/item/1005009030731602.html',
  'title':'Crystal Singing Bowls Colored Original Tibetan Bowl',
  'search_query':'crystal singing bowl set', 'size_declared':'5–7 inch listing property; single-tone SKUs', 'material_declared':'Crystal',
  'contents_declared':'A 7-piece Set SKU exists but is £1,539.19 (stock 14), outside the £60–180 target; individual tone SKUs are £171.79–£299.99 and do not prove a complete multi-bowl kit.',
  'excluded_reason':'Outside target economics for the actual 7-piece set; no freight queried.'
 }
]

evidence={
 'checked_at_utc':datetime.now(timezone.utc).isoformat(),
 'scope':{'destination':'GB','currency':'GBP','language':'en_GB','text_search_queries':['wooden chess set 40cm','crystal singing bowl set'],'rows_per_query':20,'product_get_count':4,'freight_query_count':3,'shipping_method':'direct METHOD_FREIGHT_QUERY; shipping_fee_cent is already a GBP value'},
 'offers_extracted':offers,
 'raw_search_responses':search,'raw_product_get_responses':gets,'raw_freight_responses':freight,
 'limitations':[
  'AliExpress/API declarations only; no purchase, sample, in-box count check, instrument tuning measurement, supplier message or certificate.',
  'All inspected stores and direct freight options indicate CN; no UK stock/source was observed.',
  'The two chess listings declare a set and size, but product_get text does not state an exact 32-piece count; image-only detail is not treated as proof.',
  'The bowl candidate within price target is one 5-inch A4 bowl with mallet/O-ring, not a multi-bowl harmonized set. The verified 7-piece option in the other inspected listing is £1,539.19.',
  'logistics_info_dto delivery_time=7 was not used as delivery proof; direct freight windows are reported.',
 ]
}
(OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2,default=str)+'\n')

report='''# Sourcing Q4 — échiquiers bois / bols chantants cristal

**Périmètre API (07/09/2026)** — 2 recherches de 20 résultats en `en_GB/GB/GBP`, 4 `product_get`, 3 frets directs GBP. Aucun achat ni contact fournisseur.

**Résultat : TECHNICAL_WATCH.** Deux échiquiers ont une économie et un délai compatibles, mais le compte exact de 32 pièces n’est pas écrit dans les fiches vérifiées. Le bol sous budget est un bol unique avec accessoires, pas un kit multi-bols accordés.

1. [1005008086495961](https://www.aliexpress.com/item/1005008086495961.html?skuId=12000043641691985) — SKU `12000043641691985`, **chess set**, 39 cm/15 in, bois, £35.19, stock déclaré 10, 26 ventes. Le titre déclare set pliable et reines supplémentaires ; le `product_get` ne donne pas le nombre exact de pièces. Fret direct CN £1.99, **4–8 jours**, rendu **£37.18**.

2. [1005012070192886](https://www.aliexpress.com/item/1005012070192886.html?skuId=12000057442920193) — SKU `12000057442920193`, **1 set**, 45 cm/17.7 in, bois, roi acrylique 9 cm selon titre, £95.79, stock 987, 14 ventes. Le nombre exact de pièces n’est pas documenté dans le texte. Fret direct CN £1.99, **6–10 jours**, rendu **£97.78**.

3. [1005009424303397](https://www.aliexpress.com/item/1005009424303397.html?skuId=12000049055056832) — SKU `12000049055056832`, **5inch A4**, cristal, £121.79, stock 50. L’accessoire `Mallet and oring` est déclaré ; il s’agit d’un seul bol/tone, pas d’un set multi-bols. Fret standard gratuit **11–18 jours**, ou Premium £36.42, 11–16 jours, rendu £158.21 : délai hors cible ≤13 jours.

Le même contrôle a trouvé un véritable SKU **7-piece Set** de bols, mais à £1,539.19 (stock 14), donc hors cible. Les champs `delivery_time=7` des fiches ne valident pas la livraison ; les fenêtres directes ci-dessus font foi. Vérifier physiquement les 32 pièces et le kit de chaque échiquier avant toute offre.
'''
(OUT/'report.md').write_text(report)
print(json.dumps({'report':str(OUT/'report.md'),'evidence':str(OUT/'evidence.json'),'report_words':len(re.findall(r"\\b\\w+[’'-]?\\w*\\b",report))},ensure_ascii=False))

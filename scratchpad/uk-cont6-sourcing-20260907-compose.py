import json
from datetime import datetime, timezone
from pathlib import Path

OUT = Path('/tmp/uk-cont6-sourcing-20260907')

def jsonl(path):
    rows=[]
    for line in Path(path).read_text().splitlines():
        if line.lstrip().startswith('{'):
            try: rows.append(json.loads(line))
            except json.JSONDecodeError: pass
    return rows

def mobile_data(base):
    texts=[]; images=[]
    md=base.get('mobile_detail') if isinstance(base,dict) else None
    if md:
        try:
            obj=json.loads(md)
            def walk(v):
                if isinstance(v,dict):
                    if isinstance(v.get('content'),str): texts.append(v['content'])
                    if v.get('type')=='image' and isinstance(v.get('data'),dict) and v['data'].get('url'):
                        images.append({'url':v['data']['url'],'style':v['data'].get('style')})
                    for vv in v.values(): walk(vv)
                elif isinstance(v,list):
                    for vv in v: walk(vv)
            walk(obj)
        except Exception: pass
    return '\n'.join(texts), list(dict((i['url'],i) for i in images).values())

def product_payload(row):
    raw=row.get('raw') or {}; res=raw.get('result') or {}; base=res.get('ae_item_base_info_dto') or {}
    skus=((res.get('ae_item_sku_info_dtos') or {}).get('ae_item_sku_info_d_t_o') or [])
    props=((res.get('ae_item_properties') or {}).get('ae_item_property') or [])
    text,mobile_images=mobile_data(base)
    gallery=[u for u in str((res.get('ae_multimedia_info_dto') or {}).get('image_urls','')).split(';') if u]
    sku_images=[]
    for s in skus:
        for p in ((s.get('ae_sku_property_dtos') or {}).get('ae_sku_property_d_t_o') or []):
            if p.get('sku_image'): sku_images.append(p['sku_image'])
    size_info=[]
    for p in props:
        if p.get('attr_name')=='size_info':
            try: size_info=json.loads(p.get('attr_value','{}'))
            except Exception: size_info=p.get('attr_value')
    return {'product_id':str(row['product_id']), 'title':base.get('subject'), 'sales_declared':base.get('sales_count'),
            'rating_declared':base.get('avg_evaluation_rating'), 'store':res.get('ae_store_info'),
            'logistics_info_dto':res.get('logistics_info_dto'), 'package_info_dto':res.get('package_info_dto'),
            'properties':props, 'skus':skus, 'declared_text':text, 'size_info':size_info,
            'gallery_image_urls':list(dict.fromkeys(gallery)), 'mobile_images':mobile_images,
            'sku_image_urls':list(dict.fromkeys(sku_images)), 'url_base':f"https://www.aliexpress.com/item/{row['product_id']}.html", 'raw':raw}

def freight_payload(row):
    res=(row.get('raw') or {}).get('result') or {}
    return {'label':row.get('label'),'product_id':str(row.get('product_id')),'sku_id':str(row.get('sku_id')),
            'options':((res.get('delivery_options') or {}).get('delivery_option_d_t_o') or []),'raw':row.get('raw')}

search_rows=jsonl(OUT/'search.jsonl')
detail_rows=[r for r in jsonl(OUT/'details.jsonl') if r.get('kind')=='product_get']
freight_rows=[r for r in jsonl(OUT/'freight.jsonl') if r.get('kind')=='freight_query']
products={str(r['product_id']):product_payload(r) for r in detail_rows}
freights={r['label']:freight_payload(r) for r in freight_rows}

def get_sku(pid,sid):
    return next(s for s in products[pid]['skus'] if str(s.get('sku_id'))==sid)

def props_text(props):
    return '; '.join(f"{p.get('attr_name')}={p.get('attr_value')}" for p in props)

def make_offer(pid,sid,label,kind,selection,components,limitations):
    p=products[pid]; s=get_sku(pid,sid); sp=((s.get('ae_sku_property_dtos') or {}).get('ae_sku_property_d_t_o') or [])
    f=freights.get(label); opt=(f['options'] or [{}])[0] if f else {}
    return {'family':'corset','kind':kind,'selection':selection,'product_id':pid,'sku_id':sid,'sku_attr':s.get('sku_attr'),
            'variant_properties':sp,'url':f'https://www.aliexpress.com/item/{pid}.html?skuId={sid}','title':p['title'],
            'store':p['store'],'price_gbp':float(s['offer_sale_price']),'currency':s.get('currency_code'),
            'stock_declared':s.get('sku_available_stock'),'sales_declared':p['sales_declared'],'rating_declared':p['rating_declared'],
            'freight_gbp':float(opt.get('shipping_fee_cent')) if opt.get('shipping_fee_cent') not in (None,'') else None,
            'freight_currency':opt.get('shipping_fee_currency'),'delivery_min_days':opt.get('min_delivery_days'),
            'delivery_max_days':opt.get('max_delivery_days'),'guaranteed_delivery_days_field':opt.get('guaranteed_delivery_days'),
            'delivery_date_desc':opt.get('delivery_date_desc'),'ship_from_country':opt.get('ship_from_country'),
            'shipping_service':opt.get('company'),'total_gbp':round(float(s['offer_sale_price'])+float(opt.get('shipping_fee_cent') or 0),2) if opt else None,
            'size_info':p['size_info'],'size_chart_image_urls':p['mobile_images'][:3],
            'gallery_image_urls':p['gallery_image_urls'],'sku_image_url':next((x.get('sku_image') for x in sp if x.get('sku_image')),None),
            'components_declared':components,'declared_text':p['declared_text'],'item_properties':p['properties'],'package_info_dto':p['package_info_dto'],
            'logistics_info_dto':p['logistics_info_dto'],'limitations':limitations}

offers=[
 make_offer('1005011724345711','12000056361525782','overbust_black_satin_M','PRIMARY_OVERBUST','M',
            'Titre black satin overbust; item properties Supporting material=Steel Boning; composition polyester + elastane. Structured size_info declares M 85–90 cm (33.46–35.43 in) and L 90–95 cm (35.43–37.40 in); listing says choose by waist.',
            'Size_info labels its numeric field length, interpreted as waist only because listing instructs waist sizing. Product text does not specify steel count or independent fabric percentages. No physical sample.'),
 make_offer('1005007308979912','12000040189579875','underbust_18_steel_satin_M','PRIMARY_UNDERBUST','M',
            'Titre underbust long torso; item properties bone=18 Steel Boned, Material Composition=Satin, cotton + polyester + elastane; M SKU stock 16, L SKU stock 5. Numeric waist table is embedded as an image, not returned as structured text.',
            'Root should read/confirm the embedded size-chart image before publishing; API exposes M/L labels and stock but no numeric waist range. No physical sample.'),
]
backups=[
 make_offer('1005008395958198','12000044846941375',None,'BACKUP_OVERBUST_BROCADE','M',
            'Black brocade/flower long-torso overbust; Skeleton=14 Steel Boned; polyester + elastane; M stock 63; 86 sales.',
            'No direct freight quote within the two-call limit. Size chart appears in embedded image; numeric table not returned as structured text.'),
 make_offer('1005008359634617','12000060342612470',None,'BACKUP_UNDERBUST_MESH','M',
            'A66-Black underbust/waspie; title says steel boned and size M stock 999, but item properties do not expose a steel-bone count or material composition beyond polyester + elastane.',
            'Weak structural proof and no freight quote; retain for visual review only.'),
]
# Remove freight fields from backups where no freight was queried.
for b in backups:
    b['freight_gbp']=None; b['freight_currency']=None; b['delivery_min_days']=None; b['delivery_max_days']=None; b['delivery_date_desc']=None; b['ship_from_country']=None; b['shipping_service']=None; b['total_gbp']=None

manifest={'generated_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'GB/GBP AliExpress API corset search; overbust and underbust structured metal-boned candidates',
          'offers':[{'product_id':o['product_id'],'sku_id':o['sku_id'],'url':o['url'],'sku_image_url':o['sku_image_url'],'gallery_image_urls':o['gallery_image_urls'],'size_chart_image_urls':o['size_chart_image_urls']} for o in offers+backups]}
evidence={'generated_at_utc':manifest['generated_at_utc'],'scope':manifest['scope'],
          'limits':{'text_search_queries':2,'results_requested_per_query':20,'product_get_calls':4,'freight_calls':2,'ship_to':'GB','currency':'GBP'},
          'queries':[r.get('query') for r in search_rows],'search_counts':[{'query':r.get('query'),'item_count':r.get('item_count')} for r in search_rows],
          'offers_extracted':offers,'backup_candidates':backups,'raw_search_responses':search_rows,'raw_product_get_responses':detail_rows,'raw_freight_responses':freight_rows,
          'limitations':['AliExpress declared data only; no purchase, sample, fit test or supplier message.','Direct freight is GB/GBP and already the selected-SKU shipping_fee value.','Freight option fields say 4-8 or 6-10 days but guaranteed_delivery_days=35; treat all delivery timing as declarative and contradictory.','The underbust numeric size chart is image-only in product_get; root visual confirmation is required before publication.'],
          'manifest':manifest}
(OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2))
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))

def row(o):
    fr=f"£{o['freight_gbp']:.2f} fret = £{o['total_gbp']:.2f} rendu; {o['delivery_min_days']}–{o['delivery_max_days']} j ({o['delivery_date_desc']})" if o['freight_gbp'] is not None else 'fret non coté dans la limite de deux appels'
    return f"- **{o['kind']}** — `{o['product_id']}` SKU `{o['sku_id']}` ({o['selection']}) · [AliExpress]({o['url']}) · £{o['price_gbp']:.2f} + {fr} · stock {o['stock_declared']} · {o['store'].get('store_name') if o.get('store') else 'store non retourné'}."

report=f"""# UK sourcing — corsets structurés à baleines acier

Passe API bornée du 7 septembre 2026, GB/GBP : deux recherches de 20 résultats (`steel boned corset overbust`, `steel boned corset underbust`), quatre `product_get`, deux frets directs. Les références retenues sont des bustiers/corsets adultes sans marque tierce (`Brand Name=NONE`), pas des dispositifs médicaux ni simples tops souples.

## Deux SKU cotés

{row(offers[0])}

Le listing est un overbust satin noir long torso. Les propriétés déclarent `Supporting material=Steel Boning`, polyester + élasthanne. Tableau structuré retourné : S 80–85 cm, **M 85–90 cm**, **L 90–95 cm**, 1XL 95–100 cm, 2XL 100–105 cm. Le champ API s’appelle `length`, mais la fiche demande de choisir selon le tour de taille : à confirmer avant publication. Image tableau : {offers[0]['size_chart_image_urls'][0]['url']} ; photo SKU : {offers[0]['sku_image_url']}.

{row(offers[1])}

Le listing est un underbust long torso satin noir. Les propriétés déclarent `bone=18 Steel Boned`, coton + polyester + élasthanne, composition satin. SKU M stock 16 et SKU L stock 5. Le tableau de tailles est présent en image dans la fiche mais aucun intervalle numérique n’est renvoyé par l’API : {offers[1]['size_chart_image_urls'][0]['url']}. Photo SKU : {offers[1]['sku_image_url']}.

## Backups visuels

{row(backups[0])}

Overbust noir brocart/fleur, `Skeleton=14 Steel Boned`, M stock 63, 86 ventes, £20.59 avant fret. Tableau taille image-only; pas de fret dans la limite.

{row(backups[1])}

Underbust mesh A66-Black, M stock 999, mais la fiche ne renvoie pas de propriété explicite `Steel Boned` ni de composition acier : ne pas retenir sans vérification visuelle.

## Limites

Les deux offres cotées sont sous la cible £15–40 rendu (£20.28 et £20.88) et dans la fenêtre d’option API 4–10 jours, mais le champ `guaranteed_delivery_days=35` les contredit. Le délai reste déclaratif. Aucun échantillon, essayage, achat ou message fournisseur; tailles, baleines et composition restent à contrôler sur photo/échantillon. Les réponses brutes et URL image sont dans `evidence.json`, `manifest.json` et les `*.jsonl`.
"""
(OUT/'report.md').write_text(report)
print('wrote',OUT/'report.md',OUT/'evidence.json',OUT/'manifest.json')

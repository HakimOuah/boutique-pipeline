import json
from datetime import datetime, timezone
from pathlib import Path

OUT=Path('/tmp/uk-final-winder-sourcing-20260907')

def jsonl(path):
    rows=[]
    for line in Path(path).read_text().splitlines():
        if line.lstrip().startswith('{'):
            try: rows.append(json.loads(line))
            except json.JSONDecodeError: pass
    return rows

def mobile_text(base):
    md=base.get('mobile_detail') if isinstance(base,dict) else None; texts=[]; imgs=[]
    if md:
        try:
            o=json.loads(md)
            def walk(v):
                if isinstance(v,dict):
                    if isinstance(v.get('content'),str): texts.append(v['content'])
                    if v.get('type')=='image' and isinstance(v.get('data'),dict) and v['data'].get('url'): imgs.append(v['data']['url'])
                    for vv in v.values(): walk(vv)
                elif isinstance(v,list):
                    for vv in v: walk(vv)
            walk(o)
        except Exception: pass
    return '\n'.join(texts),list(dict.fromkeys(imgs))

def payload(row):
    raw=row.get('raw') or {}; res=raw.get('result') or {}; b=res.get('ae_item_base_info_dto') or {}
    skus=((res.get('ae_item_sku_info_dtos') or {}).get('ae_item_sku_info_d_t_o') or [])
    props=((res.get('ae_item_properties') or {}).get('ae_item_property') or [])
    txt,mimgs=mobile_text(b)
    gallery=[u for u in str((res.get('ae_multimedia_info_dto') or {}).get('image_urls','')).split(';') if u]
    skuimgs=[]
    for s in skus:
        for p in ((s.get('ae_sku_property_dtos') or {}).get('ae_sku_property_d_t_o') or []):
            if p.get('sku_image'): skuimgs.append(p['sku_image'])
    return {'product_id':str(row.get('product_id')),'title':b.get('subject'),'sales_declared':b.get('sales_count'),
            'rating_declared':b.get('avg_evaluation_rating'),'store':res.get('ae_store_info'),'properties':props,'skus':skus,
            'declared_text':txt,'gallery_image_urls':list(dict.fromkeys(gallery)),'mobile_image_urls':mimgs,
            'sku_image_urls':list(dict.fromkeys(skuimgs)),'logistics_info_dto':res.get('logistics_info_dto'),'package_info_dto':res.get('package_info_dto'),'raw':raw}

def freight_payload(row):
    res=(row.get('raw') or {}).get('result') or {}
    return {'label':row.get('label'),'product_id':str(row.get('product_id')),'sku_id':str(row.get('sku_id')),
            'options':((res.get('delivery_options') or {}).get('delivery_option_d_t_o') or []),'raw':row.get('raw')}

search_rows=jsonl(OUT/'search.jsonl')
detail_rows=[r for r in jsonl(OUT/'details.jsonl') if r.get('kind')=='product_get']
freight_rows=[r for r in jsonl(OUT/'freight.jsonl')]
new={str(r['product_id']):payload(r) for r in detail_rows}
new_freight=freight_payload(next((r for r in freight_rows if r.get('kind')=='freight_query'),freight_rows[0])) if freight_rows else None
old=json.loads(Path('/tmp/uk-cont4-sourcing-20260907/evidence.json').read_text())
old_offer=next(x for x in old['offers_extracted'] if x.get('product_id')=='1005006786141635')
old_pg=next(x for x in old['raw_product_get_responses'] if x.get('product_id')=='1005006786141635')
old_fr=next(x for x in old['raw_freight_responses'] if x.get('product_id')=='1005006786141635')

def selected_sku(p,sid): return next(s for s in p['skus'] if str(s.get('sku_id'))==sid)
def sku_image(p,sid):
    s=selected_sku(p,sid)
    return next((q.get('sku_image') for q in ((s.get('ae_sku_property_dtos') or {}).get('ae_sku_property_d_t_o') or []) if q.get('sku_image')),None)
def props_text(p): return '; '.join(f"{q.get('attr_name')}={q.get('attr_value')}" for q in p['properties'])

def make_new(pid,sid,status,components,limitations):
    p=new[pid]; s=selected_sku(p,sid); sp=((s.get('ae_sku_property_dtos') or {}).get('ae_sku_property_d_t_o') or [])
    return {'product_id':pid,'sku_id':sid,'sku_attr':s.get('sku_attr'),'url':f'https://www.aliexpress.com/item/{pid}.html?skuId={sid}',
            'title':p['title'],'store':p['store'],'price_gbp':float(s['offer_sale_price']),'currency':s.get('currency_code'),
            'stock_declared':s.get('sku_available_stock'),'sales_declared':p['sales_declared'],'status':status,
            'components_declared':components,'limitations':limitations,'variant_properties':sp,'item_properties':p['properties'],
            'gallery_image_urls':p['gallery_image_urls'],'sku_image_url':sku_image(p,sid),'mobile_image_urls':p['mobile_image_urls'],
            'declared_text':p['declared_text'],'package_info_dto':p['package_info_dto'],'logistics_info_dto':p['logistics_info_dto'],
            'freight_gbp':None,'total_gbp':None}

existing=dict(old_offer)
existing.update({'source':'prior_existing_product_get_and_freight','status':'CONTENT_GO_LOW_STOCK','sku_image_url':'https://ae01.alicdn.com/kf/S1e4aae36caea4069984ad688c2a1e5f4O.jpg',
                'components_declared':'Text explicitly says double/two watch winder, removable pillows, two modes, Japanese quiet/antimagnetic motor and USB cable included. USB wall plug not included; no battery; PU leather rather than wood.',
                'freight_gbp':1.99,'freight_currency':'GBP','delivery_min_days':4,'delivery_max_days':8,'guaranteed_delivery_days_field':'35','delivery_date_desc':'Sep 11 - 15','ship_from_country':'CN','shipping_service':'AliExpress Selection Premium shipping','total_gbp':30.68,
                'limitations':'Only two units declared. Existing product_get returned only Black; no >5-stock colour variant. No wood finish.',
                'image_urls_to_verify':old_offer.get('image_urls_to_verify',[]),'url':'https://www.aliexpress.com/item/1005006786141635.html?skuId=12000038298689118'})

high=make_new('1005008107024816','12000043796914430','HIGH_STOCK_VISUAL_CANDIDATE',
              'Title says Double 2+0; properties say PU leather, 18 x 15 x 14 cm, USB-DC/global 100-240V and power-bank use. No text confirms that a USB cable or two pillows are included.',
              'Stock 9957 is declared for black China Mainland variant, but freight was not quoted within the one-call limit. External USB wall plug/power bank is needed; adapter/cable contents remain unverified.')
content=make_new('1005007344751830','12000040354079030','CONTENT_STRONG_LOW_STOCK_FREIGHT_ERROR',
                 'Text explicitly says double watch winder, soft lining, removable watch pillows, USB cable included, USB wall plug not included, no battery, suitable for watches <=42 mm.',
                 'Only two units declared. The permitted direct GB freight call returned DELIVERY_SERVICE_EXCEPTION, so no current total or delivery window.')
stock=make_new('1005007644146607','12000041630477333','STOCK_BACKUP_CABLE_UNPROVEN',
               'Black W135B; text says 2+0 USB-DC, outer PU leather, inner MDF, two modes, 14 x 16 x 18.5 cm and 100-240V input. Cable inclusion is not stated.',
               'Stock 15 declared, but freight was not quoted. External USB wall plug/power bank is needed; no wood claim should be made.')

stamp=datetime.now(timezone.utc).isoformat()
manifest={'generated_at_utc':stamp,'scope':'GB/GBP watch-winder sourcing: prior exact two-slot quote plus one bounded search and three product_get calls',
          'offers':[{'product_id':o['product_id'],'sku_id':o['sku_id'],'url':o['url'],'sku_image_url':o.get('sku_image_url'),'gallery_image_urls':o.get('gallery_image_urls',[]),'mobile_image_urls':o.get('mobile_image_urls',[]),'image_urls_to_verify':o.get('image_urls_to_verify',[])} for o in [existing,content,high,stock]]}
evidence={'generated_at_utc':stamp,'scope':manifest['scope'],'limits':{'existing_product_get_inspected':1,'text_search_queries':1,'results_requested':20,'new_product_get_calls':3,'new_freight_calls':1,'ship_to':'GB','currency':'GBP'},
          'query':search_rows[0].get('query') if search_rows else None,'search_counts':[{'query':r.get('query'),'item_count':r.get('item_count')} for r in search_rows],
          'offers_extracted':[existing,content,high,stock],'raw_search_responses':search_rows,'raw_new_product_get_responses':detail_rows,'raw_new_freight_responses':freight_rows,
          'raw_prior_product_get_response':old_pg,'raw_prior_freight_response':old_fr,
          'limitations':['AliExpress declared data only; no purchase, sample or physical inspection.','The successful existing quote is for the exact Black SKU with two declared units.','The new content-strong listing freight returned DELIVERY_SERVICE_EXCEPTION; high-stock alternatives have no freight quote.','USB wall plug is not included on the content-strong listing; external USB power is required.','Do not market PU as wood or infer cable inclusion from USB-DC alone.'],'manifest':manifest}
(OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)); (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))

report=f"""# UK sourcing — remontoir automatique 2 montres

Passe GB/GBP du 7 septembre 2026. La fiche existante `1005006786141635` ne possède qu’une variante retournée, Black, stock 2; aucune autre couleur 2 slots >5 n’était disponible dans son `product_get`. Une recherche supplémentaire (`double watch winder USB`, 20 résultats), trois nouveaux `product_get` et un seul fret direct ont suivi.

## Offre la mieux prouvée, mais faible stock

`1005006786141635`, SKU `12000038298689118` Black — [AliExpress](https://www.aliexpress.com/item/1005006786141635.html?skuId=12000038298689118), £28.69, stock **2**, 358 ventes déclarées. Fret GB/GBP déjà obtenu £1.99, option 4–8 j (Sep 11–15), CN : **£30.68 rendu**. Image SKU : https://ae01.alicdn.com/kf/S1e4aae36caea4069984ad688c2a1e5f4O.jpg.

Le texte confirme deux emplacements/coussins amovibles, deux modes, moteur silencieux, câble USB inclus, prise murale USB non incluse et aucune batterie. PU noir, pas bois. C’est le seul dossier avec contenu et fret cohérents, mais le stock de 2 empêche une sélection robuste.

## Nouvelles pistes

- `1005007344751830`, SKU `12000040354079030` Black : £28.89, stock 2, 408 ventes. Texte très clair : deux coussins, câble USB inclus, prise murale non incluse, montres jusqu’à 42 mm. Image : https://ae01.alicdn.com/kf/S1e4aae36caea4069984ad688c2a1e5f4O.jpg. Le seul fret nouveau a renvoyé `DELIVERY_SERVICE_EXCEPTION`; aucun total/délai validé.
- `1005008107024816`, SKU `12000043796914430` W135B Black / China Mainland : £33.49, stock **9 957**. Titre « Double 2+0 », PU 18×15×14 cm, USB-DC/usage power bank; câble et coussins non confirmés textuellement. Image : https://ae01.alicdn.com/kf/S68607c8ed09f44a096386cc0e51d1c050.jpg.
- `1005007644146607`, SKU `12000041630477333` W135B Black : £28.19, stock **15**. Texte « 2+0 USB-DC », PU extérieur/MDF intérieur, 14×16×18,5 cm; câble non confirmé et fret non coté. Image : https://ae01.alicdn.com/kf/Sc5c56fa5ef33494c9ac42735dba89809r.jpg.

## Limites

Les délais sont déclaratifs; le devis existant contient aussi `guaranteed_delivery_days=35` malgré l’option 4–8 jours. Aucun achat, échantillon ou test réel. Les réponses brutes, prix, stocks, SKU et URLs image sont dans `evidence.json`, `manifest.json` et les fichiers `*.jsonl`.
"""
(OUT/'report.md').write_text(report); print('wrote',OUT/'report.md',OUT/'evidence.json',OUT/'manifest.json')

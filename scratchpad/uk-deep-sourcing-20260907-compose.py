import csv
import json
from datetime import datetime, timezone
from pathlib import Path

OUT=Path('/tmp/uk-deep-sourcing-20260907')

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
                        images.append(v['data']['url'])
                    for vv in v.values(): walk(vv)
                elif isinstance(v,list):
                    for vv in v: walk(vv)
            walk(obj)
        except Exception: pass
    return '\n'.join(texts),list(dict.fromkeys(images))

def payload(row):
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
    return {'product_id':str(row.get('product_id')),'title':base.get('subject'),'sales':base.get('sales_count'),
            'rating':base.get('avg_evaluation_rating'),'store':res.get('ae_store_info'),'properties':props,'skus':skus,
            'declared_text':text,'size_info':size_info,'gallery_images':list(dict.fromkeys(gallery)),
            'mobile_images':mobile_images,'sku_images':list(dict.fromkeys(sku_images)),
            'logistics':res.get('logistics_info_dto'),'package':res.get('package_info_dto'),'raw':raw}

def freight_row(row):
    raw=row.get('raw') or {}; res=raw.get('result') or {}
    opts=((res.get('delivery_options') or {}).get('delivery_option_d_t_o') or [])
    return {'family':row.get('family'),'product_id':str(row.get('product_id')),'sku_id':str(row.get('sku_id')),'options':opts,'raw':raw,'kind':row.get('kind')}

def sku_obj(p,sid): return next(s for s in p['skus'] if str(s.get('sku_id'))==sid)
def sku_props(s): return ((s.get('ae_sku_property_dtos') or {}).get('ae_sku_property_d_t_o') or [])
def sku_image(p,sid): return next((x.get('sku_image') for x in sku_props(sku_obj(p,sid)) if x.get('sku_image')),None)
def prop_text(p): return '; '.join(f"{x.get('attr_name')}={x.get('attr_value')}" for x in p['properties'])
def store_name(p): return (p.get('store') or {}).get('store_name')

def offer_new(family,pid,sid,fr,components,limitations):
    p=new[pid]; s=sku_obj(p,sid); opt=(fr.get('options') or [{}])[0] if fr else {}
    price=float(s.get('offer_sale_price')); fee=opt.get('shipping_fee_cent')
    fee_num=float(fee) if fee not in (None,'') else (0.0 if opt.get('free_shipping') else None)
    return {'family':family,'side':'alternative','product_id':pid,'sku_id':sid,'sku_label':s.get('sku_attr'),
            'url':f'https://www.aliexpress.com/item/{pid}.html?skuId={sid}','title':p['title'],'store':store_name(p),
            'price_gbp':price,'stock':s.get('sku_available_stock'),'sales':p['sales'],'freight_gbp':fee_num,
            'free_shipping':opt.get('free_shipping'),'total_gbp':round(price+fee_num,2) if fee_num is not None else None,
            'delivery_min_days':opt.get('min_delivery_days'),'delivery_max_days':opt.get('max_delivery_days'),
            'delivery_date_desc':opt.get('delivery_date_desc'),'guaranteed_days':opt.get('guaranteed_delivery_days'),
            'ship_from':opt.get('ship_from_country'),'shipping_service':opt.get('company'),'freight_options':fr.get('options') if fr else [],
            'sku_properties':sku_props(s),'item_properties':p['properties'],'components':components,'limitations':limitations,
            'sku_image_url':sku_image(p,sid),'gallery_images':p['gallery_images'],'mobile_images':p['mobile_images'],
            'size_info':p['size_info'],'declared_text':p['declared_text'],'package':p['package'],'logistics':p['logistics']}

def normalize_old(family,old,selector,components,limitations):
    o=selector(old); x=dict(o)
    # Existing evidence schemas differ by mission. Extract common values without inventing.
    pid=str(x.get('product_id')); sid=str(x.get('sku_id') or x.get('sku',{}).get('sku_id'))
    price=x.get('price_gbp',x.get('sku',{}).get('price_gbp')); stock=x.get('stock_declared',x.get('sku',{}).get('stock_declared')); sales=x.get('sales_declared',x.get('sales_count_declared'))
    if price is not None: price=float(price)
    fgbp=x.get('freight_gbp',x.get('freight_fee_gbp_screening'))
    freight=x.get('freight',{}) if isinstance(x.get('freight'),dict) else {}
    if fgbp is None: fgbp=freight.get('fee_gbp')
    if fgbp is not None: fgbp=float(fgbp)
    if fgbp is None and x.get('freight_options'):
        z=x['freight_options'][0]; fgbp=z.get('fee_gbp',z.get('shipping_fee_cent'))
    total=x.get('total_gbp',x.get('total_gbp_product_plus_shipping_screening'))
    if total is None and price is not None and fgbp is not None: total=round(price+float(fgbp),2)
    fopts=x.get('freight_options',[])
    if not fopts and x.get('freight_selected'): fopts=[x['freight_selected']]
    z=fopts[0] if fopts else freight
    if isinstance(z,dict):
        dmin=x.get('delivery_min_days',z.get('min_days',z.get('delivery_min_days',z.get('min_delivery_days'))))
        dmax=x.get('delivery_max_days',z.get('max_days',z.get('delivery_max_days',z.get('max_delivery_days'))))
        date=x.get('delivery_date_desc') or z.get('delivery_date_desc'); guar=x.get('guaranteed_delivery_days_field',z.get('guaranteed_delivery_days',z.get('guaranteed_days'))); ship=x.get('ship_from_country',z.get('ship_from_country',freight.get('ship_from_country'))); service=x.get('shipping_service',z.get('service',z.get('company',freight.get('service'))))
    else: dmin=dmax=date=guar=ship=service=None
    return {'family':family,'side':'existing','product_id':pid,'sku_id':sid,'sku_label':x.get('sku_label',x.get('sku',{}).get('sku_attr')),
            'url':x.get('url',x.get('ali_url',f'https://www.aliexpress.com/item/{pid}.html?skuId={sid}')),'title':x.get('title'),
            'store':(x.get('seller') or {}).get('name') or (x.get('store') or {}).get('store_name') or 'non retourné dans la preuve précédente',
            'price_gbp':price,'stock':stock,'sales':sales,'freight_gbp':fgbp,'free_shipping':x.get('freight_free_shipping',freight.get('free_shipping')),
            'total_gbp':float(total) if total is not None else None,'delivery_min_days':dmin,'delivery_max_days':dmax,
            'delivery_date_desc':date,'guaranteed_days':guar,'ship_from':ship,'shipping_service':service,'freight_options':fopts,
            'components':components,'limitations':limitations,'sku_image_url':(x.get('sku_image_url') or (x.get('image_urls_to_verify') or [None])[0]),
            'gallery_images':x.get('image_urls_to_verify',[]),'mobile_images':[],'size_info':x.get('size_info',x.get('size_declared')),
            'declared_text':x.get('declared_text',x.get('contents_declared')),'item_properties':x.get('item_properties',x.get('declared_properties'))}

search_rows=jsonl(OUT/'search.jsonl'); detail_rows=[r for r in jsonl(OUT/'details.jsonl') if r.get('kind')=='product_get']; freight_rows=[freight_row(r) for r in jsonl(OUT/'freight.jsonl') if r.get('kind')=='freight_query']
new={str(r['product_id']):payload(r) for r in detail_rows}; new_fr={(r['product_id'],r['sku_id']):r for r in freight_rows}

def fr(pid,sid): return new_fr.get((pid,sid))

# Prior evidence and selected existing offers.
abay=json.loads(Path('/tmp/uk-sourcing-abaya-final-20260907/evidence.json').read_text())
cors=json.loads(Path('/tmp/uk-cont6-sourcing-20260907/evidence.json').read_text())
wind=json.loads(Path('/tmp/uk-final-winder-sourcing-20260907/evidence.json').read_text())
chess=json.loads(Path('/tmp/uk-sourcing-q4-final-20260907/evidence.json').read_text())
tx_details={str(r['product_id']):payload(r) for r in jsonl('/tmp/uk-metal-adult-20260907/details.jsonl') if r.get('raw') and r.get('product_id')}
tx_freights=[freight_row(r) for r in jsonl('/tmp/uk-metal-adult-20260907/freight-choice.jsonl') if r.get('product_id')]
tx_fr={(r['product_id'],r['sku_id']):r for r in tx_freights}
# Add old TX in a small schema matching normalize_old.
tx_offer={'product_id':'1005006994695803','sku_id':'12000038984545060','sku_label':'TX-850','title':tx_details['1005006994695803']['title'],
          'price_gbp':82.39,'stock_declared':5,'sales_declared':'1000+','store':tx_details['1005006994695803']['store'],
          'freight_options':tx_fr[('1005006994695803','12000038984545060')]['options'],'sku_image_url':(tx_details['1005006994695803']['sku_images'] or tx_details['1005006994695803']['gallery_images'] or [None])[0],
          'contents_declared':'TX-850, 11-inch coil/LCD; existing exact freight quote from prior pass.'}

existing={}
existing['abaya']=normalize_old('abaya',abay,lambda x: next(o for o in x['selected_offers'] if o['product_id']=='1005012235894439'),
  'Adult Burgundy embroidered abaya; chiffon/polyester; SKU M Burgundy; open-front title but API property says full opening No; M size length 101 cm.',
  'Existing best offer; opening contradiction and no independent fit/sample proof.')
existing['corset']=normalize_old('corset_underbust',cors,lambda x: next(o for o in x['offers_extracted'] if o['product_id']=='1005007308979912'),
  'Underbust black satin; 18 steel bones; cotton/polyester/elastane; M SKU, L stock 5.',
  'Existing listing has no numeric waist table in API; table image and fit remain to verify.')
existing['winder']=normalize_old('watch_winder',wind,lambda x: next(o for o in x['offers_extracted'] if o['product_id']=='1005008107024816'),
  'Black W135B double 2+0 title; PU 18x15x14 cm; USB-DC/power-bank wording. Cable/two pillows not textually confirmed.',
  'High declared stock; external USB source required; no cable/plug proof.')
existing['tx850']=normalize_old('tx850',{'offers_extracted':[tx_offer]},lambda x:x['offers_extracted'][0],
  'TX-850, adjustable stem, 11-inch waterproof interchangeable DD coil, LCD/sound, 9V battery not included; prior option selected.',
  'Existing source price/stock/freight are declarative; package contents are listing claims.')
existing['chess']=normalize_old('chess_39cm',chess,lambda x: next(o for o in x['offers_extracted'] if o['product_id']=='1005008086495961'),
  '39 cm/15 in wooden foldable set; title says extra queens; exact piece count not textually documented.',
  'Existing listing is a complete-set title but the 32-piece count was not returned in product_get.')

alternatives={}
alternatives['abaya']=offer_new('abaya','1005009404700712','12000048996914221',fr('1005009404700712','12000048996914221'),
  'Open lace-embroidered adult abaya, polyester, full opening Yes, loose fit; M Black, size table length 107 cm, stock 299.',
  '0 sales declared; embroidery/weight/finish and fit are listing claims; size field is length, not bust/waist; no sample.')
alternatives['corset']=offer_new('corset_underbust','1005007463741144','12000040858765475',fr('1005007463741144','12000040858765475'),
  'Black underbust, Supporting material Steel bone, 90% polyester/10% spandex, M; structured table M 65–70 cm and L 70–75 cm.',
  'Only 4 sales declared; table field is labelled length by API but listing instructs waist sizing; stock and composition remain declarative.')
alternatives['winder']=offer_new('watch_winder','1005008970862209','12000047413849598',fr('1005008970862209','12000047413849598'),
  'Title declares 3 slots, 2 modes and USB cable; product_get properties say leatherette and dimensions 15.5×13×17.5 cm.',
  'Only 1 unit declared; mobile detail text is empty, so cable/pillow/adapter inclusion relies on title/search and needs visual check.')
alternatives['tx850']=offer_new('tx850','1005006003820202','12000035270477888',fr('1005006003820202','12000035270477888'),
  'TIANXUN TX-850 adult; 11-inch waterproof interchangeable DD coil, adjustable 42–52 in stem, LCD/sound, CE/FCC; package list control housing, upper stem, search coil/stem, hardware, guide; 9V battery not included.',
  'Stock 4 is lower than existing 5; depth claims conflict within listing (2.5 m marketing vs specification max 1.5 m / typical coin 25 cm).')
alternatives['chess']=offer_new('chess_39cm','1005009215859784','12000048343840400',fr('1005009215859784','12000048343840400'),
  '39×39 cm magnetic wood 3-in-1 chess/checkers/backgammon; title declares 32 PCS wood chessmen; size table gives 78 mm king, 72 mm queen, etc.; package 1 set.',
  '12 sales declared; 3-in-1 format differs from existing dedicated 39 cm foldable set; exact board/piece finish needs photo/sample check.')

# Replace TX existing images from payload built above.
existing['tx850']['gallery_images']=tx_details['1005006994695803']['gallery_images']; existing['tx850']['mobile_images']=tx_details['1005006994695803']['mobile_images']; existing['tx850']['item_properties']=tx_details['1005006994695803']['properties']; existing['tx850']['declared_text']=tx_details['1005006994695803']['declared_text']; existing['tx850']['store']=store_name(tx_details['1005006994695803']);

families=['abaya','corset','winder','tx850','chess']
# CSV comparison.
fields=['family','existing_product_id','existing_sku_id','existing_url','existing_store','existing_price_gbp','existing_stock','existing_sales','existing_freight_gbp','existing_total_gbp','existing_delivery','existing_contents','alternative_product_id','alternative_sku_id','alternative_url','alternative_store','alternative_price_gbp','alternative_stock','alternative_sales','alternative_freight_gbp','alternative_total_gbp','alternative_delivery','alternative_contents','comparison_status','limitations']
with (OUT/'comparison.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
    for fam in families:
        a=existing[fam]; b=alternatives[fam]
        def delivery(o): return f"{o.get('delivery_min_days')}–{o.get('delivery_max_days')} j ({o.get('delivery_date_desc')})" if o.get('delivery_min_days') is not None else ''
        row={'family':fam,'existing_product_id':a.get('product_id'),'existing_sku_id':a.get('sku_id'),'existing_url':a.get('url'),'existing_store':a.get('store'),'existing_price_gbp':a.get('price_gbp'),'existing_stock':a.get('stock'),'existing_sales':a.get('sales'),'existing_freight_gbp':a.get('freight_gbp'),'existing_total_gbp':a.get('total_gbp'),'existing_delivery':delivery(a),'existing_contents':a.get('components'),'alternative_product_id':b.get('product_id'),'alternative_sku_id':b.get('sku_id'),'alternative_url':b.get('url'),'alternative_store':b.get('store'),'alternative_price_gbp':b.get('price_gbp'),'alternative_stock':b.get('stock'),'alternative_sales':b.get('sales'),'alternative_freight_gbp':b.get('freight_gbp'),'alternative_total_gbp':b.get('total_gbp'),'alternative_delivery':delivery(b),'alternative_contents':b.get('components'),'comparison_status':'ALTERNATIVE_RECORDED','limitations':b.get('limitations')}
        w.writerow(row)

stamp=datetime.now(timezone.utc).isoformat()
manifest={'generated_at_utc':stamp,'scope':'Five independent alternative checks against existing UK/GBP AliExpress candidates',
          'families':{fam:{'existing':{'product_id':existing[fam]['product_id'],'sku_id':existing[fam]['sku_id'],'sku_image_url':existing[fam].get('sku_image_url'),'gallery_images':existing[fam].get('gallery_images',[])},'alternative':{'product_id':alternatives[fam]['product_id'],'sku_id':alternatives[fam]['sku_id'],'sku_image_url':alternatives[fam].get('sku_image_url'),'gallery_images':alternatives[fam].get('gallery_images',[]),'mobile_images':alternatives[fam].get('mobile_images',[])}} for fam in families}}
evidence={'generated_at_utc':stamp,'scope':manifest['scope'],'limits':{'text_search_queries':5,'results_requested_per_query':20,'new_product_get_calls':8,'new_freight_calls':5,'ship_to':'GB','currency':'GBP'},
          'queries':[r.get('query') for r in search_rows],'search_counts':[{'query':r.get('query'),'item_count':r.get('item_count')} for r in search_rows],
          'comparison_existing':existing,'comparison_alternatives':alternatives,'raw_search_responses':search_rows,'raw_new_product_get_responses':detail_rows,'raw_new_freight_responses':freight_rows,
          'prior_source_paths':{'abaya':'/tmp/uk-sourcing-abaya-final-20260907/evidence.json','corset':'/tmp/uk-cont6-sourcing-20260907/evidence.json','watch_winder':'/tmp/uk-final-winder-sourcing-20260907/evidence.json','chess':'/tmp/uk-sourcing-q4-final-20260907/evidence.json','tx850':'/tmp/uk-metal-adult-20260907/details.jsonl + freight-choice.jsonl'},
          'limitations':['All product, stock, sales, composition, size and delivery fields are supplier/API declarations; no purchase, contact or sample.','Delivery estimates use the returned min/max/date option; guaranteed_delivery_days is retained as a separate field and not used as an estimate.','A selected SKU is not proof of fit, quality, exact contents, native performance or actual delivery.','For the alternative underbust, size_info numeric waist ranges are returned under an API field named length; treat as declared waist sizing because listing instructs waist selection.','For chess, the alternative explicitly says 32 PCS and 39x39 cm, but physical count/finish remains untested.'],
          'manifest':manifest}
(OUT/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)); (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))

# Human report.
def money(o):
    price=float(o['price_gbp']) if o.get('price_gbp') is not None else None
    fee=float(o['freight_gbp']) if o.get('freight_gbp') is not None else None
    total=float(o['total_gbp']) if o.get('total_gbp') is not None else None
    return f"£{price:.2f} + £{fee:.2f} = £{total:.2f}" if fee is not None and total is not None else f"£{price:.2f} + fret non coté"
def delivery(o): return f"{o.get('delivery_min_days')}–{o.get('delivery_max_days')} j ({o.get('delivery_date_desc')})" if o.get('delivery_min_days') is not None else 'non coté'
lines=[]
for fam in families:
    a=existing[fam]; b=alternatives[fam]
    lines.append(f"### {fam}\n\n**Existant** — `{a['product_id']}` / `{a['sku_id']}` · {money(a)} · stock {a.get('stock')} · ventes {a.get('sales')} · {delivery(a)} · vendeur {a.get('store')}. {a.get('components')}\n\n**Alternative indépendante** — `{b['product_id']}` / `{b['sku_id']}` · [AliExpress]({b['url']}) · {money(b)} · stock {b.get('stock')} · ventes {b.get('sales')} · {delivery(b)} · vendeur {b.get('store')}. {b.get('components')}\n\nÉcart/limite : {b.get('limitations')}\n")
report=f"""# Deep sourcing UK — comparaison de cinq pistes

Passe AliExpress GB/GBP du 7 septembre 2026 : cinq recherches de 20 résultats, huit `product_get` et cinq frets directs, une alternative indépendante par famille. Les montants utilisent le fret de l’option sélectionnée; les dates restent des estimations API déclaratives. Aucun achat, contact ou échantillon.

"""+'\n'.join(lines)+f"""\n## Lecture comparative

L’alternative abaya est moins chère produit mais son fret standard porte le rendu à £27.92, avec 299 unités déclarées et taille M longueur 107 cm; elle améliore le stock mais annonce 0 vente. Le corset underbust 24 baleines offre un tableau M 65–70/L 70–75 cm et 989 unités, pour £21.45 rendu, contre £20.88 et 16 unités pour l’existant; c’est le meilleur gain de stock, avec une coupe très petite à confirmer.

Le remontoir 3 slots avec câble USB est £28.68 rendu mais stock 1 et contenu textuel vide. Le remontoir existant haut-stock reste à £33.49 avec 9 957 unités, mais câble et coussins ne sont pas confirmés. Le TX850 officiel alternatif est complet dans sa fiche mais coûte £102.18 rendu et stock 4, contre £84.38 et stock 5 pour l’existant; il n’améliore pas l’économie. L’échiquier alternatif 39×39 cm/32 pièces déclaré coûte £39.72 rendu, stock 997, contre £37.18 et stock 10 avec nombre de pièces non documenté pour l’existant : il améliore la preuve de contenu au prix de £2.54.

Les champs `guaranteed_delivery_days` parfois 35 ou 60 sont conservés dans `evidence.json` mais ne remplacent pas les fenêtres min/max/date retournées. Les propriétés, images SKU et réponses brutes sont dans `manifest.json`, `comparison.csv`, `search.jsonl`, `details.jsonl` et `freight.jsonl`.
"""
(OUT/'report.md').write_text(report)
print('wrote',OUT/'report.md',OUT/'comparison.csv',OUT/'evidence.json',OUT/'manifest.json')

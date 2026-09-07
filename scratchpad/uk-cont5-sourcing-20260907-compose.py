import json
from datetime import datetime, timezone
from pathlib import Path

OUT = Path('/tmp/uk-cont5-sourcing-20260907')

def jsonl(path):
    rows = []
    for line in Path(path).read_text().splitlines():
        if line.lstrip().startswith('{'):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows

def plain_mobile(base):
    md = base.get('mobile_detail') if isinstance(base, dict) else None
    texts = []
    if md:
        try:
            obj = json.loads(md)
            def walk(v):
                if isinstance(v, dict):
                    if isinstance(v.get('content'), str):
                        texts.append(v['content'])
                    for vv in v.values():
                        walk(vv)
                elif isinstance(v, list):
                    for vv in v:
                        walk(vv)
            walk(obj)
        except Exception:
            pass
    return '\n'.join(texts)

def product_payload(row):
    raw = row.get('raw') or {}
    result = raw.get('result') or {}
    base = result.get('ae_item_base_info_dto') or {}
    skus = ((result.get('ae_item_sku_info_dtos') or {}).get('ae_item_sku_info_d_t_o') or [])
    props = ((result.get('ae_item_properties') or {}).get('ae_item_property') or [])
    images = []
    mm = result.get('ae_multimedia_info_dto') or {}
    if mm.get('image_urls'):
        images.extend([u for u in str(mm['image_urls']).split(';') if u])
    for s in skus:
        for sp in ((s.get('ae_sku_property_dtos') or {}).get('ae_sku_property_d_t_o') or []):
            if sp.get('sku_image'):
                images.append(sp['sku_image'])
    return {
        'product_id': str(row.get('product_id')),
        'title': base.get('subject'),
        'sales_declared': base.get('sales_count'),
        'rating_declared': base.get('avg_evaluation_rating'),
        'logistics_info_dto': result.get('logistics_info_dto'),
        'package_info_dto': result.get('package_info_dto'),
        'properties': props,
        'skus': skus,
        'declared_text': plain_mobile(base),
        'image_urls': list(dict.fromkeys(images)),
        'url_base': f"https://www.aliexpress.com/item/{row.get('product_id')}.html",
        'raw': raw,
    }

def freight_payload(row):
    raw = row.get('raw') or {}
    result = raw.get('result') or {}
    opts = ((result.get('delivery_options') or {}).get('delivery_option_d_t_o') or [])
    return {
        'label': row.get('label'),
        'product_id': str(row.get('product_id')),
        'sku_id': str(row.get('sku_id')),
        'options': opts,
        'raw': raw,
    }

search_rows = jsonl(OUT/'search.jsonl')
detail_rows = [r for r in jsonl(OUT/'details.jsonl') if r.get('kind') == 'product_get']
freight_rows = [r for r in jsonl(OUT/'freight.jsonl') if r.get('kind') == 'freight_query']
details = {str(r.get('product_id')): product_payload(r) for r in detail_rows}
freight = {r.get('label'): freight_payload(r) for r in freight_rows}

def sku(pid, sid):
    for s in details[pid]['skus']:
        if str(s.get('sku_id')) == sid:
            return s
    raise KeyError((pid, sid))

def offer(pid, sid, label, status, limitations):
    s = sku(pid, sid)
    f = freight[label]
    opt = (f['options'] or [{}])[0]
    props = ((s.get('ae_sku_property_dtos') or {}).get('ae_sku_property_d_t_o') or [])
    variant_image = next((p.get('sku_image') for p in props if p.get('sku_image')), None)
    return {
        'family': 'metal_detector',
        'product_id': pid,
        'sku_id': sid,
        'sku_label': s.get('sku_attr'),
        'variant_properties': props,
        'url': f'https://www.aliexpress.com/item/{pid}.html?skuId={sid}',
        'title': details[pid]['title'],
        'price_gbp': float(s['offer_sale_price']),
        'currency': s.get('currency_code'),
        'stock_declared': s.get('sku_available_stock'),
        'sales_declared': details[pid]['sales_declared'],
        'freight_gbp': float(opt.get('shipping_fee_cent')) if opt.get('shipping_fee_cent') not in (None, '') else None,
        'freight_currency': opt.get('shipping_fee_currency'),
        'delivery_min_days': opt.get('min_delivery_days'),
        'delivery_max_days': opt.get('max_delivery_days'),
        'guaranteed_delivery_days_field': opt.get('guaranteed_delivery_days'),
        'delivery_date_desc': opt.get('delivery_date_desc'),
        'ship_from_country': opt.get('ship_from_country'),
        'shipping_service': opt.get('company'),
        'total_gbp': round(float(s['offer_sale_price']) + float(opt.get('shipping_fee_cent') or 0), 2),
        'components_declared': 'Listing text confirms adjustable detector, search coil, LCD/sound display, all-metal mode, 10-100 cm claimed depth; selected variant is labelled With Accessories. No textual list identifies a shovel, headphones or carrying bag.',
        'image_urls': details[pid]['image_urls'],
        'variant_image_url': variant_image,
        'status': status,
        'limitations': limitations,
    }

offers = [
    offer('1005009126691172', '12000050720365393', 'detector_with_accessories_stock865', 'CANDIDATE_DECLARATIVE', 'Adult sizing/use is not explicitly stated. The image and variant bundle need visual validation for adult shaft/coil and actual accessories. 9V battery is declared not included; coil is waterproof but display/battery compartment are not.'),
    offer('1005009126691172', '12000048435221831', 'detector_with_accessories_stock6', 'ALTERNATIVE_LOW_STOCK', 'Same listing and claims as the candidate above; only six units declared. Accessory contents are not itemized in API text; 9V battery is not included.'),
]

excluded = []
for pid, reason in {
    '1005010183718844': 'Handheld/utility locator: text says it can be used with a ground detector, 410 mm package, 313 g and no shaft/coil kit; pinpointer-like, stock 1.',
    '1005009205106930': 'Handheld underwater pinpointer: adjustable length No, LCD No, 5.9-inch coil and lanyard only; not a full adult shaft detector.',
    '1005007292344306': 'Handheld GT-120: 4.2-inch coil, LCD No, battery not included, 35.5 cm body and bracelet only; not the requested full detector.',
}.items():
    p = details[pid]
    excluded.append({'product_id': pid, 'title': p['title'], 'status': 'EXCLUDED', 'reason': reason, 'url': p['url_base'], 'image_urls': p['image_urls']})

old = json.loads(Path('/tmp/uk-cont4-sourcing-20260907/evidence.json').read_text())
old_offer = next(x for x in old['offers_extracted'] if x.get('product_id') == '1005012217866893')
wfreight = freight['watch_winder_alternative']
wopt = (wfreight['options'] or [{}])[0]
watch_alt = dict(old_offer)
watch_alt.update({
    'freight_gbp': float(wopt.get('shipping_fee_cent')) if wopt.get('shipping_fee_cent') not in (None, '') else None,
    'freight_currency': wopt.get('shipping_fee_currency'),
    'delivery_min_days': wopt.get('min_delivery_days'),
    'delivery_max_days': wopt.get('max_delivery_days'),
    'guaranteed_delivery_days_field': wopt.get('guaranteed_delivery_days'),
    'delivery_date_desc': wopt.get('delivery_date_desc'),
    'ship_from_country': wopt.get('ship_from_country'),
    'shipping_service': wopt.get('company'),
    'total_gbp': round(float(old_offer['price_gbp']) + float(wopt.get('shipping_fee_cent') or 0), 2),
    'status': 'SINGLE_SLOT_VISUAL_CAVEAT',
    'visual_observation_from_root': 'Root CUA inspection of the selected image shows “1+0” and one cushion; likely one watch position for CC-J-B1. Black PU/leather-like stitched finish is visible; no wood apparent. Do not market as a two-watch wooden box without further proof.',
    'limitations': 'API property says Material Leather and product_get text is empty. USB power is in title, but cable/UK plug not textually verified.',
})

stamp = datetime.now(timezone.utc).isoformat()
manifest = {
    'generated_at_utc': stamp,
    'scope': 'GB/GBP AliExpress API bounded metal detector search plus one permitted watch-winder freight quote',
    'offers': [{'product_id': o['product_id'], 'sku_id': o['sku_id'], 'url': o['url'], 'variant_image_url': o['variant_image_url'], 'image_urls': o['image_urls']} for o in offers],
    'excluded': [{'product_id': e['product_id'], 'url': e['url'], 'image_urls': e['image_urls']} for e in excluded],
    'watch_winder': {'product_id': watch_alt['product_id'], 'sku_id': watch_alt['sku_id'], 'url': watch_alt['url'], 'image_urls': watch_alt.get('image_urls_to_verify', []), 'variant_image_url': 'https://ae01.alicdn.com/kf/Sdf8eebfb9f5e4e0682cff0460a08b1f0y.jpg'},
}

evidence = {
    'generated_at_utc': stamp,
    'scope': manifest['scope'],
    'limits': {'text_search_queries': 2, 'results_requested_per_query': 20, 'product_get_calls': 4, 'detector_freight_calls': 2, 'permitted_watch_freight_calls': 1, 'currency': 'GBP', 'ship_to': 'GB'},
    'queries': [r.get('query') for r in search_rows],
    'search_counts': [{'query': r.get('query'), 'item_count': r.get('item_count')} for r in search_rows],
    'offers_extracted': offers,
    'excluded_extracted': excluded,
    'watch_winder_alternative': watch_alt,
    'raw_search_responses': search_rows,
    'raw_product_get_responses': detail_rows,
    'raw_freight_responses': freight_rows,
    'watch_source_prior_product_get': [r for r in old.get('raw_product_get_responses', []) if r.get('product_id') == '1005012217866893'],
    'limitations': [
        'AliExpress declared API data only; no purchase, sample, physical inspection or supplier message.',
        'Direct freight was queried in GBP for GB. Delivery fields conflict: guaranteed_delivery_days is 35 while max_delivery_days is 8 or 10; report uses the option date/min-max fields and flags the contradiction.',
        'A variant label With Accessories does not prove shovel, headphones or bag because the API text does not itemize them.',
        'Searches returned many children/pinpointer products; they were not treated as full adult detectors.',
    ],
    'manifest': manifest,
}
(OUT/'evidence.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2))
(OUT/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))

def line_offer(o):
    return (f"- **{o['status']} — {o['product_id']} / SKU `{o['sku_id']}` ({o['sku_label']})** — "
            f"[AliExpress]({o['url']}) · £{o['price_gbp']:.2f} + £{o['freight_gbp']:.2f} fret = **£{o['total_gbp']:.2f}** · "
            f"stock déclaré {o['stock_declared']} · expédition {o['ship_from_country']} · "
            f"option {o['delivery_min_days']}–{o['delivery_max_days']} j ({o['delivery_date_desc']}).")

report = f"""# UK sourcing — détecteur de métaux adulte (AliExpress API)

Vérification bornée du 7 septembre 2026, destination GB, devise GBP : 2 recherches de 20 résultats demandés (`metal detector adults waterproof LCD` et `metal detector adult kit`; la seconde a retourné 19 lignes), 4 `product_get`, puis 2 frets directs GBP sur le meilleur listing. Le marché retourné mélangeait fortement pinpointers et modèles enfants.

## Offre à faire vérifier visuellement

{line_offer(offers[0])}

Le texte du listing confirme un détecteur réglable avec bobine de recherche, écran LCD + son, mode “All Metal”, profondeur annoncée 10–100 cm, bobine étanche et pile 9V **non incluse**. La variante s’appelle “With Accessories”, mais l’API ne détaille ni pelle, ni casque, ni sac. Le titre/les images et le colis de 47 cm suggèrent un détecteur à canne, mais l’usage adulte et le contenu physique restent à valider par photo/échantillon. L’écran et le compartiment batterie ne sont pas étanches selon la fiche.

{line_offer(offers[1])}

Même produit/claims, avec seulement 6 unités déclarées et une fenêtre API plus courte (4–8 j). Il s’agit d’une alternative de stock, pas d’un second vendeur.

## Écartés

- `1005010183718844` — SKU `12000051436329866`, £16.89, stock 1 : texte “can be used with a ground metal detector”, localisation de proximité/induction coil, 410 mm/313 g; pinpointer/utility locator, pas de canne complète.
- `1005009205106930` — £46.09, stock 4/2 : handheld IP68, LCD = No, longueur réglable = No, lanyard/USB; pas de détecteur adulte complet.
- `1005007292344306` — SKU `12000040089255615`, £16.19, stock 15 : handheld GT-120, bobine 4.2", LCD = No, pile non incluse, bracelet; écarté.

## Devis remontoir demandé en complément

`1005012217866893`, SKU `12000057777061832` `CC-J-B1` — [fiche](https://www.aliexpress.com/item/1005012217866893.html?skuId=12000057777061832), £26.79, stock 197, fret GBP £1.99, total **£28.78**, option 6–10 j (Sep 13–17), CN. Contrôle visuel communiqué par root : image `https://ae01.alicdn.com/kf/Sdf8eebfb9f5e4e0682cff0460a08b1f0y.jpg` montrant “1+0” et un coussin, probablement une seule position; finition PU/cuir noir, aucun bois apparent. La propriété API est `Material=Leather`, le texte produit est vide; USB est dans le titre, câble/prise UK non prouvés. Ne pas présenter comme coffret bois deux montres.

## Limites

Les délais sont déclaratifs et contradictoires dans le devis : `guaranteed_delivery_days=35` alors que l’option indique `max_delivery_days=8/10` et une date. Aucun achat, échantillon, contrôle physique ou message fournisseur. Les URL d’images et les réponses brutes sont dans `manifest.json`, `evidence.json` et les fichiers `*.jsonl`.
"""
(OUT/'report.md').write_text(report)
print('wrote', OUT/'report.md', OUT/'evidence.json', OUT/'manifest.json')

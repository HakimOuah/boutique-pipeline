import json
import re
from datetime import datetime, timezone
from pathlib import Path

OUT = Path('/tmp/uk-sourcing-carplay-20260907')

def read_jsonl(name):
    rows = []
    for line in (OUT / name).read_text().splitlines():
        if line.startswith('{'):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows

search = read_jsonl('search.jsonl')
gets = read_jsonl('details.jsonl')
freight = read_jsonl('freight-gbp.jsonl')

offers = [
    {
        'product_id': '1005009949538785',
        'url': 'https://www.aliexpress.com/item/1005009949538785.html?skuId=12000050658540378',
        'title': 'Carplay Screen for Car, 10 inch Portable Wireless Carplay & Android Auto',
        'search_query': 'portable carplay screen / carpuride carplay screen',
        'search_price_gbp_min_sku': 36.79,
        'sku_id': '12000050658540378', 'sku_label': '10 inches screen',
        'price_gbp': 52.19, 'stock_declared': 4, 'sales_declared': 133,
        'declared_features': 'Wireless Apple CarPlay and Android Auto; 10-inch variant; adhesive and suction mounts; 12V–24V vehicle compatibility; built-in speakers, AUX/FM/Bluetooth.',
        'power_inclusion': '12V–24V compatibility is stated. A visual bundle image for this exact SKU declares Car charging, cable, AUX, standard bracket and expansion bracket; this remains listing evidence, not physical receipt.',
        'visual_bundle_evidence': 'https://ae01.alicdn.com/kf/S182d0fd7640f4a8b97156baf756b28c3V.jpg; observed by root via CUA for exact SKU, showing Car charging/cable/AUX/standard bracket/expansion bracket/manual.',
        'camera_sd': 'Selected screen variant has no rear camera. Listing mentions optional camera variants and SD not included; no 4K/dashcam claim used.',
        'store_country': 'CN',
        'freight_options': [{'service': 'AliExpress Selection Premium shipping', 'fee_gbp': 1.99, 'min_days': 4, 'max_days': 8, 'delivery_date_desc': 'Sep 11 - 15', 'ship_from_country': 'CN', 'total_gbp': 54.18}],
    },
    {
        'product_id': '1005009453554660',
        'url': 'https://www.aliexpress.com/item/1005009453554660.html?skuId=12000049152281555',
        'title': '9 inch Portable Multimedia Player Carplay AI Screen',
        'search_query': 'portable carplay screen / carpuride carplay screen',
        'search_price_gbp_min_sku': 53.99,
        'sku_id': '12000049152281555', 'sku_label': '9 inch',
        'price_gbp': 53.99, 'stock_declared': 130, 'sales_declared': 14,
        'declared_features': 'CarPlay and Android AutoPlay; 9-inch SKU; magnetic and suction-cup mounts; 12V property; Bluetooth 5.0/AUX/FM.',
        'power_inclusion': 'The API property says 12V and “Charger”, but the text does not explicitly confirm a UK cigarette-lighter lead in the box.',
        'camera_sd': '9-inch base SKU selected; rear-camera SKUs are separate and out of stock. No 4K/dashcam claim used.',
        'store_country': 'CN',
        'freight_options': [{'service': 'AliExpress Selection Shipping for Oversized Goods', 'fee_gbp': 1.99, 'min_days': 25, 'max_days': 42, 'delivery_date_desc': 'Oct 02 - 19', 'ship_from_country': 'CN', 'total_gbp': 55.98}],
    },
    {
        'product_id': '1005010154806308',
        'url': 'https://www.aliexpress.com/item/1005010154806308.html?skuId=12000051344413038',
        'title': 'Universal Portable Wireless Carplay Screen for Car with Android Auto',
        'search_query': 'portable carplay screen',
        'search_price_gbp_min_sku': 44.59,
        'sku_id': '12000051344413038', 'sku_label': 'Without Rear Camera',
        'price_gbp': 44.59, 'stock_declared': 3, 'sales_declared': '2,000+',
        'declared_features': 'Pionray; 10-inch/10.26-inch properties; Wireless CarPlay and Android Auto; self-adhesive dashboard bracket; 9–32V compatibility; built-in speaker/mic.',
        'power_inclusion': '9–32V compatibility is stated, but no cigarette-lighter power lead/in-box adapter is explicitly documented.',
        'camera_sd': 'No rear-camera variant selected; optional camera/64G variant exists separately. No 4K/dashcam claim used.',
        'store_country': 'CN',
        'freight_options': [],
    },
]

evidence = {
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'scope': {
        'destination': 'GB', 'currency': 'GBP', 'language': 'en_GB',
        'text_search_queries': ['portable carplay screen', 'carpuride carplay screen'],
        'rows_per_query': 20, 'product_get_count': 3, 'freight_query_count': 2,
        'shipping_method': 'direct METHOD_FREIGHT_QUERY; shipping_fee_cent is already a GBP value',
    },
    'offers_extracted': offers,
    'raw_search_responses': search,
    'raw_product_get_responses': gets,
    'raw_freight_responses': freight,
    'limitations': [
        'All product, stock, feature, power and delivery data are AliExpress/API declarations; no purchase, sample, in-box inspection, or supplier message.',
        'No UK source observed: all inspected store and direct freight ship_from_country values are CN.',
        'The API logistics_info_dto delivery_time=7 conflicts with direct freight for the 9-inch SKU; direct freight is reported as the delivery evidence.',
        'For exact SKU 1005009949538785, root observed the listing bundle image https://ae01.alicdn.com/kf/S182d0fd7640f4a8b97156baf756b28c3V.jpg declaring Car charging/cable, AUX, standard bracket, expansion bracket and manual. This resolves the declared bundle gap but is still not physical in-box proof.',
        'The same image states 1600x600 while text states 1024x600; report the contradiction and do not select a resolution claim without supplier/sample verification.',
        'No 4K/dashcam benefit is claimed. Camera and SD features are optional/separate; the selected 10-inch screen SKU is the screen-only variant and SD is not included.',
    ],
}
(OUT / 'evidence.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2, default=str) + '\n')

report = '''# Sourcing UK — écran CarPlay portable 9–10 pouces

**Périmètre API (07/09/2026)** — 2 recherches de 20 résultats (`portable carplay screen`, `carpuride carplay screen`) en `en_GB/GB/GBP`, 3 `product_get`, 2 frets directs GBP. Aucun achat ni contact fournisseur.

**Résultat : TECHNICAL_WATCH.** Une offre atteint la cible économique et de délai. Pour le SKU 10 pouces, l’image de bundle de la fiche ([preuve visuelle](https://ae01.alicdn.com/kf/S182d0fd7640f4a8b97156baf756b28c3V.jpg)) déclare `Car charging`, câble, AUX, supports standard/expansion et manuel ; cela lève le manque documentaire sur l’alimentation, sans constituer une réception physique.

1. [1005009949538785](https://www.aliexpress.com/item/1005009949538785.html?skuId=12000050658540378) — SKU `12000050658540378`, **10 inches screen**, £52.19, stock déclaré 4, 133 ventes dans la recherche. CarPlay et Android Auto sans fil, supports adhésif/ventouse, compatibilité véhicule 12–24 V, haut-parleurs/AUX/FM/Bluetooth déclarés. Fret direct CN : £1.99, **4–8 jours** (11–15 septembre), rendu **£54.18**. L’image de bundle de la fiche déclare l’alimentation allume-cigare et le câble, AUX, supports et manuel. Contradiction à conserver : image **1600×600**, texte **1024×600**. La variante sélectionnée n’a pas de caméra arrière ; aucune promesse 4K/dashcam ni besoin de carte SD n’est retenu.

2. [1005009453554660](https://www.aliexpress.com/item/1005009453554660.html?skuId=12000049152281555) — SKU `12000049152281555`, **9 inch**, £53.99, stock 130, 14 ventes. CarPlay/Android Auto, supports magnétique et ventouse, Bluetooth 5.0/AUX/FM et propriété 12 V déclarés. Contradiction de fiche : une propriété affiche 7 pouces, le SKU et le détail affichent 9 pouces. Fret £1.99 mais **25–42 jours** (2–19 octobre), rendu £55.98 : délai hors cible.

3. [1005010154806308](https://www.aliexpress.com/item/1005010154806308.html?skuId=12000051344413038) — SKU `Without Rear Camera`, £44.59, stock 3, 2,000+ ventes ; écran 10/10.26 pouces selon propriétés, CarPlay/Android Auto, support adhésif et compatibilité 9–32 V. Pas de fret vérifié dans la limite de deux devis et pas de câble allume-cigare explicitement documenté.

Les trois boutiques et les devis disponibles indiquent CN. Le champ `logistics_info_dto.delivery_time=7` ne suffit pas à valider la livraison ; le fret direct est retenu. Les prix, stocks, fonctions et accessoires restent déclaratifs jusqu’à contrôle du SKU et du contenu du colis.
'''
(OUT / 'report.md').write_text(report)
print(json.dumps({'evidence': str(OUT/'evidence.json'), 'report': str(OUT/'report.md'), 'report_words': len(re.findall(r"\b\w+[’'-]?\w*\b", report))}, ensure_ascii=False))

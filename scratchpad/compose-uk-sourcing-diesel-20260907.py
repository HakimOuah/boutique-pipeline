import json
import re
from datetime import datetime, timezone
from pathlib import Path

OUT = Path('/tmp/uk-sourcing-diesel-20260907')

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
        'product_id': '1005010613825154',
        'url': 'https://www.aliexpress.com/item/1005010613825154.html?skuId=12000052973298627',
        'title': '2-8KW 12V/24V Bluetooth Portable All in One Diesel Air Heater',
        'search_query': 'diesel heater bluetooth',
        'search_price_gbp': 68.79,
        'sku_id': '12000052973298627',
        'sku_label': '12v-5000W',
        'price_gbp': 68.79,
        'stock_declared': 99,
        'sales_declared': 14,
        'rating_declared': '0.0 / 0 evaluations in product_get; search evaluateRate 100.0',
        'voltage_power_declared': '12V; 5000W variant; listing detail also says 12-24V and power 2000W/5000W',
        'content_declared': 'All-in-one in title. Product detail enumerates no pump, exhaust pipe, or included remote/controller; “controller” appears only in safety instructions.',
        'store_country': 'CN',
        'freight_options': [
            {'service': 'AliExpress Shipping for Large Goods by Land', 'fee_gbp': 83.60, 'min_days': 10, 'max_days': 41, 'delivery_date_desc': 'Sep. 17 - Oct. 18', 'ship_from_country': 'CN', 'total_gbp': 152.39},
            {'service': 'AliExpress Premium shipping', 'fee_gbp': 186.09, 'min_days': 6, 'max_days': 11, 'delivery_date_desc': 'Sep 13 - 18', 'ship_from_country': 'CN', 'total_gbp': 254.88},
        ],
    },
    {
        'product_id': '1005005384614422',
        'url': 'https://www.aliexpress.com/item/1005005384614422.html?skuId=12000035628648443',
        'title': '12V 24V Diesel Air Heater 5KW ... With LCD Display Remote',
        'search_query': 'diesel air heater 5kw',
        'search_price_gbp': 43.59,
        'sku_id': '12000035628648443',
        'sku_label': '12V 5000W-Black',
        'price_gbp': 43.59,
        'stock_declared': 945,
        'sales_declared': 19,
        'rating_declared': '0.0 / 0 evaluations in product_get; search evaluateRate 96.7',
        'voltage_power_declared': '12V; 5000W; diesel; split plastic LCD remote-control model',
        'content_declared': 'LCD remote/control is stated in title and detail. Other accessories are only “as picture shown”; pump and exhaust pipe are not itemized, and small parts may vary by batch.',
        'store_country': 'CN',
        'freight_options': [
            {'service': 'AliExpress Shipping for Large Goods by Land', 'fee_gbp': 61.34, 'min_days': 10, 'max_days': 41, 'delivery_date_desc': 'Sep. 17 - Oct. 18', 'ship_from_country': 'CN', 'total_gbp': 104.93},
            {'service': 'AliExpress standard shipping', 'fee_gbp': 70.93, 'min_days': 6, 'max_days': 13, 'delivery_date_desc': 'Sep 13 - 20', 'ship_from_country': 'CN', 'total_gbp': 114.52},
        ],
    },
]

evidence = {
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'scope': {
        'destination': 'GB', 'currency': 'GBP', 'language': 'en_GB',
        'text_search_queries': ['diesel heater bluetooth', 'diesel air heater 5kw'],
        'rows_per_query': 20, 'product_get_count': 2, 'freight_query_count': 2,
        'shipping_method': 'direct METHOD_FREIGHT_QUERY; shipping_fee_cent is already a GBP value',
    },
    'offers_extracted': offers,
    'raw_search_responses': search,
    'raw_product_get_responses': gets,
    'raw_freight_responses': freight,
    'limitations': [
        'AliExpress API declarations only; no purchase, sample, certificate, installation test, or supplier message.',
        'No UK source observed: both store_country and direct freight ship_from_country are CN.',
        'The API logistics_info_dto delivery_time=7 conflicts with direct freight windows; the direct freight windows are reported and logistics_info_dto is not used as proof.',
        'The descriptions do not itemize pump plus exhaust pipe for either selected SKU. “Accessories as picture shown” is not sufficient proof of a complete kit.',
        'Combustion safety, conformity, CE/UKCA, real output power, emissions, and suitability were not verified. Seller wattage/voltage claims remain unverified declarations.',
    ],
}
(OUT / 'evidence.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2, default=str) + '\n')

report = '''# Sourcing UK — chauffage diesel 5 kW / Bluetooth

**Périmètre API (07/09/2026)** — 2 recherches AliExpress de 20 résultats en `en_GB/GB/GBP`, 2 `product_get`, 2 frets directs GBP. Les frais API sont déjà en GBP. Aucun achat, message fournisseur, échantillon ou certificat.

**Résultat : TECHNICAL_WATCH, aucun GO rendu vérifié.** Aucun des deux SKU n'atteint simultanément le plafond rendu de £100 et une fenêtre déclarée entièrement ≤10 jours. Aucun stock UK observé : boutique et expédition indiquent CN.

1. [1005005384614422](https://www.aliexpress.com/item/1005005384614422.html?skuId=12000035628648443) — SKU `12000035628648443`, **12V 5000W-Black**, £43.59, stock déclaré 945, 19 ventes dans la recherche. Le titre et la fiche déclarent diesel, 5,000 W et commande LCD/remote ; la fiche indique ensuite « accessories: as picture shown ». Pompe et échappement ne sont pas listés, et les petites pièces peuvent varier selon le lot. Fret direct : £61.34, 10–41 j, rendu **£104.93** ; ou £70.93, 6–13 j, rendu £114.52. `ship_from_country=CN`.

2. [1005010613825154](https://www.aliexpress.com/item/1005010613825154.html?skuId=12000052973298627) — SKU `12000052973298627`, **12v-5000W**, £68.79, stock déclaré 99, 14 ventes. Le titre dit Bluetooth/all-in-one ; la fiche détail dit contrôle manuel, 12–24 V et 2,000/5,000 W. Aucun contenu pompe, échappement ou remote n’est énuméré. Fret direct : £83.60, 10–41 j, rendu **£152.39** ; Premium £186.09, 6–11 j, rendu £254.88. `ship_from_country=CN`.

Le champ `logistics_info_dto.delivery_time=7` est contradictoire avec les devis directs et ne valide pas la livraison. Les puissances, la sécurité combustion, la conformité CE/UKCA, les émissions et la qualité restent des déclarations vendeur/API non vérifiées ; aucun certificat ou échantillon reçu. Avant toute offre £150–250, il faut obtenir une liste de contenu exacte (pompe, échappement, silencieux, commande), source UK réelle et preuves de conformité.
'''
(OUT / 'report.md').write_text(report)
print(json.dumps({'evidence': str(OUT/'evidence.json'), 'report': str(OUT/'report.md'), 'report_words': len(re.findall(r"\\b\\w+[’'-]?\\w*\\b", report))}, ensure_ascii=False))

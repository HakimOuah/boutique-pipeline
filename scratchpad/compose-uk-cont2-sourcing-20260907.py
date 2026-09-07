import json
import re
from datetime import datetime, timezone
from pathlib import Path

OUT = Path('/tmp/uk-cont2-sourcing-20260907')

def read_jsonl(name):
    rows = []
    for line in (OUT / name).read_text().splitlines():
        if line.startswith('{'):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows

def urls_from(obj):
    out = []
    def rec(x):
        if isinstance(x, dict):
            for v in x.values(): rec(v)
        elif isinstance(x, list):
            for v in x: rec(v)
        elif isinstance(x, str):
            for u in re.findall(r'https?://[^\s";<>]+', x):
                if 'aliexpress' in u or 'alicdn' in u:
                    out.append(u.rstrip(',.'))
    rec(obj)
    return list(dict.fromkeys(out))

search = read_jsonl('search.jsonl')
gets = read_jsonl('details.jsonl')
freight = read_jsonl('freight-gbp.jsonl')

def search_item(pid):
    for row in search:
        for item in row.get('items', []):
            if str(item.get('itemId') or item.get('productId')) == pid:
                return item
    return {}

def get_row(pid):
    for row in gets:
        if row.get('product_id') == pid:
            return row
    return {}

def image_urls(pid):
    urls = []
    item = search_item(pid)
    if item.get('itemMainPic'):
        urls.append(item['itemMainPic'])
    row = get_row(pid)
    if row:
        urls.extend(urls_from(row.get('raw', {})))
    return list(dict.fromkeys(urls))[:8]

offers = [
    {
        'family': 'pet_stroller', 'product_id': '1005008669344944', 'sku_id': '12000050507875583', 'sku_label': '1PC Gray',
        'url': 'https://www.aliexpress.com/item/1005008669344944.html?skuId=12000050507875583',
        'title': 'Pet Stroller ... Small Pet Stroller ... Outdoor Travel', 'price_gbp': 57.19, 'stock_declared': 32, 'sales_declared': 48,
        'components_declared': 'Detachable stroller/basket, metal frame, water-bottle holder, foldable basket, 360° front wheel, rear stop switch, side pocket; basket 56×35×77cm; frame limit 15kg; packing list 1 stroller.',
        'freight': {'fee_gbp': 1.99, 'min_days': 25, 'max_days': 42, 'delivery_date_desc': 'Oct 02 - 19', 'ship_from_country': 'CN', 'total_gbp': 59.18, 'service': 'AliExpress Selection Shipping for Oversized Goods'},
        'status': 'NO_GO_DELAY', 'image_urls_to_verify': image_urls('1005008669344944'),
    },
    {
        'family': 'pet_stroller', 'product_id': '1005012314615521', 'sku_id': '12000058059109629', 'sku_label': '003',
        'url': 'https://www.aliexpress.com/item/1005012314615521.html?skuId=12000058059109629',
        'title': '2026 SUMMER Pet Stroller ... Complimentary Mat ... One-click Folding Brake', 'price_gbp': 63.39, 'stock_declared': 10, 'sales_declared': 8,
        'components_declared': 'Title declares complimentary mat, lightweight folding and brake; product_get text is “Real photos” only, so full contents are not proven.',
        'freight': None, 'status': 'UNQUOTED_COMPONENT_GAP', 'image_urls_to_verify': image_urls('1005012314615521'),
    },
    {
        'family': 'bird_feeder_camera', 'product_id': '1005008831874584', 'sku_id': '12000046871554273', 'sku_label': 'Feeder Cam',
        'url': 'https://www.aliexpress.com/item/1005008831874584.html?skuId=12000046871554273',
        'title': '1080P Bird Feeder with HD Camera ... Built-in Battery Solar ... 2.4G WIFI', 'price_gbp': 45.69, 'stock_declared': 56, 'sales_declared': 44,
        'components_declared': 'Built-in 2000mAh battery, 4W solar panel with 3m cable, 1080P camera, motion activation, IP66, 2.4G WiFi, ATIPCAM Android/iOS app, hooks, mic/speaker; SD is optional. Separate 64GB SKU is £48.49, stock 5.',
        'freight': {'fee_gbp': 1.99, 'min_days': 6, 'max_days': 10, 'delivery_date_desc': 'Sep 13 - 17', 'ship_from_country': 'CN', 'total_gbp': 47.68, 'service': 'AliExpress Selection Premium shipping'},
        'status': 'GO_CANDIDATE_DECLARATIVE', 'image_urls_to_verify': image_urls('1005008831874584'),
    },
    {
        'family': 'bird_feeder_camera', 'product_id': '1005010543319338', 'sku_id': None, 'sku_label': None,
        'url': 'https://www.aliexpress.com/item/1005010543319338.html', 'title': 'Jooan 4K Solar Bird Feed Camera', 'price_gbp': 58.79, 'stock_declared': None, 'sales_declared': 34,
        'components_declared': None, 'freight': None, 'status': 'PRODUCT_GET_FAILED_ALL_SKU_UNSALEABLE', 'image_urls_to_verify': image_urls('1005010543319338'),
    },
    {
        'family': 'wildlife_trail_camera', 'product_id': '1005007259614755', 'sku_id': '12000040668186449', 'sku_label': 'as pic',
        'url': 'https://www.aliexpress.com/item/1005007259614755.html?skuId=12000040668186449',
        'title': 'Wildlife Camera Solar Energy Trail Cam 4K ... 16MP ... BT WiFi APP', 'price_gbp': 49.99, 'stock_declared': 3, 'sales_declared': 22,
        'components_declared': 'Solar claim, 2600mAh 18650 battery claim, BT/WiFi/app, SD up to 256GB, mounting strap, USB cable and manual. Text specifies 2MP CMOS sensor and max 2.7K/20fps video; 4K title is not accepted as native proof.',
        'freight': None, 'status': 'TECHNICAL_WATCH_RESOLUTION_AND_LOW_STOCK', 'image_urls_to_verify': image_urls('1005007259614755'),
    },
    {
        'family': 'wildlife_trail_camera', 'product_id': '1005007903321651', 'sku_id': '12000042783566915', 'sku_label': 'S810WIFI',
        'url': 'https://www.aliexpress.com/item/1005007903321651.html?skuId=12000042783566915',
        'title': '4K 60MP Wifi Solar Powered Wild Trail Camera ... 5200mAh Li-Battery', 'price_gbp': 68.99, 'stock_declared': 93, 'sales_declared': 1,
        'components_declared': '1.5W solar panel, internal 5200mAh Li battery, WiFi/Bluetooth and mobile app, SD max 256GB (not included), 8MP real CMOS claim, 4K/8K video claims, USB cable, fixation band and manual, IP67, 120° view. Treat resolution as seller/API claim pending sample.',
        'freight': {'fee_gbp': 0, 'free_shipping': True, 'min_days': 6, 'max_days': 13, 'delivery_date_desc': 'Sep 13 - 20', 'ship_from_country': 'CN', 'total_gbp': 68.99, 'service': 'AliExpress standard shipping'},
        'status': 'GO_CANDIDATE_DECLARATIVE', 'image_urls_to_verify': image_urls('1005007903321651'),
    },
]

families = [
    {'family': 'pet_stroller', 'target': '£30–65 delivered; ≤13 days', 'freight_checked_sku': '12000050507875583', 'best_status': 'NO_GO_DELAY'},
    {'family': 'bird_feeder_camera', 'target': '£35–75 delivered; ≤13 days', 'freight_checked_sku': '12000046871554273', 'best_status': 'GO_CANDIDATE_DECLARATIVE'},
    {'family': 'wildlife_trail_camera', 'target': '£35–85 delivered; ≤13 days', 'freight_checked_sku': '12000042783566915', 'best_status': 'GO_CANDIDATE_DECLARATIVE'},
]

scope = {'destination': 'GB', 'currency': 'GBP', 'language': 'en_GB', 'queries': ['pet stroller dog', 'bird feeder camera solar', 'wildlife trail camera solar'], 'rows_per_query': 20, 'product_get_count': 6, 'freight_query_count': 3}
manifest = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'scope': scope, 'families': families, 'offers': offers, 'image_verification_note': 'URLs are provided for root visual verification; no images downloaded by this run.'}
(OUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2, default=str) + '\n')

evidence = {
    'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'scope': scope, 'manifest': 'manifest.json', 'offers_extracted': offers,
    'raw_search_responses': search, 'raw_product_get_responses': gets, 'raw_freight_responses': freight,
    'limitations': [
        'AliExpress/API declarations only; no sample, purchase, supplier message or physical component test.',
        'All direct freight options ship from CN; no UK source observed.',
        'Pet stroller has complete textual component list but oversized freight is 25–42 days, outside target. Alternate pet SKU has image-only detail and no freight quote.',
        'Bird feeder base SKU includes 2000mAh battery, 4W solar panel and app; 64GB SD is a separate low-stock SKU. Selected base SKU does not include SD in the stated contents.',
        'Wildlife camera resolution claims are seller/API declarations. One candidate has 2MP sensor and 2.7K max despite 4K title; the selected S810WIFI says 8MP real CMOS and 4K/8K but remains untested. Do not market native 4K as verified.',
        'delivery_time in logistics_info_dto was not used as proof; direct freight windows are reported.',
    ],
}
(OUT / 'evidence.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2, default=str) + '\n')

report = '''# Sourcing UK — 3 familles : poussette, mangeoire caméra, caméra faune

**Périmètre API (07/09/2026)** — 3 recherches de 20 résultats en `en_GB/GB/GBP`, 6 `product_get` (dont un échec `All SKU Unsaleable`), 3 frets directs GBP. Les URLs de photos SKU sont dans [manifest.json](./manifest.json) pour vérification visuelle par root ; aucune image n’a été téléchargée ici.

**Résultat : 2 candidats validables sous réserve des déclarations, poussette bloquée par le fret.**

**Mangeoire caméra — candidat GO déclaratif.** [1005008831874584](https://www.aliexpress.com/item/1005008831874584.html?skuId=12000046871554273), SKU `Feeder Cam`, £45.69, stock 56, 44 ventes. La fiche documente caméra 1080P, batterie intégrée 2,000mAh, panneau solaire 4W/câble 3m, WiFi 2.4G, app ATIPCAM Android/iOS, mouvement, IP66 et supports. Le SKU 64GB existe à £48.49 mais stock 5 ; le SKU sélectionné n’inclut pas de carte SD déclarée. Fret direct CN £1.99, 6–10 jours, rendu **£47.68**. Le second résultat Jooan £58.79 a échoué au `product_get` (`All SKU Unsaleable`).

**Caméra faune — candidat GO déclaratif.** [1005007903321651](https://www.aliexpress.com/item/1005007903321651.html?skuId=12000042783566915), SKU `S810WIFI`, £68.99, stock 93, 1 vente. La fiche déclare panneau solaire 1.5W, batterie Li interne 5,200mAh, WiFi/Bluetooth/app, SD jusqu’à 256GB non incluse, câble USB, fixation, manuel et IP67. Elle déclare « 8MP real CMOS » et 4K/8K ; ce sont des claims vendeur/API non testés, donc aucun label 4K natif ne doit être publié sans échantillon. Fret CN gratuit, 6–13 jours, rendu **£68.99**.

**Poussette — pas validable au délai cible.** [1005008669344944](https://www.aliexpress.com/item/1005008669344944.html?skuId=12000050507875583), SKU gris, £57.19, stock 32, 48 ventes. La fiche décrit panier détachable, châssis métal, pliage, roue avant 360°, frein arrière, panier 56×35×77cm, charge 15kg et contenu 1 poussette. Fret £1.99 mais **25–42 jours**, rendu £59.18. L’alternative [1005012314615521](https://www.aliexpress.com/item/1005012314615521.html?skuId=12000058059109629), £63.39, stock 10, n’a qu’une mention « real photos » et aucun fret vérifié.

Les montants, stocks, solar/app/SD et délais restent des déclarations API jusqu’à contrôle photo puis échantillon. Les champs `delivery_time=7` ne remplacent pas les devis directs ; tous les frets observés partent de CN.
'''
(OUT / 'report.md').write_text(report)
print(json.dumps({'report': str(OUT / 'report.md'), 'evidence': str(OUT / 'evidence.json'), 'manifest': str(OUT / 'manifest.json'), 'report_words': len(re.findall(r"\b\w+[’'-]?\w*\b", report))}, ensure_ascii=False))

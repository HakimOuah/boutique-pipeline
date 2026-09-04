"""Lecture seule des sélecteurs publics AliExpress via browser-use.

Exécution : LM_HANDLES=handle1,handle2 browser-use < ce_fichier.py
Les helpers navigateur sont injectés par browser-use. Ne modifie ni Shopify ni DSers.
Enregistre uniquement le contenu produit public et les images effectivement observées.
"""
import json
import os
import re
import time
from pathlib import Path
from urllib.request import urlopen

base = Path.cwd() / 'catalogues/lumierematiere'
for handle in os.environ['LM_HANDLES'].split(','):
    manifest = json.loads((base / 'livraisons-visuels-codex/produits' / handle / 'manifeste.json').read_text())
    pid = manifest['supplier_id']
    url = f'https://fr.aliexpress.com/item/{pid}.html'
    new_tab(url)
    wait_for_load()
    for attempt in range(12):
        found = js("document.querySelectorAll('[data-sku-col] img').length")
        if found:
            break
        time.sleep(0.5)
    record = {'handle': handle, 'supplier_id': pid, 'observed_at': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'url': url, 'page': page_info(), 'variants': []}
    record['product_text'] = js("document.body.innerText.slice(0,18000)")
    variants = js("Array.from(document.querySelectorAll('[data-sku-col]')).filter(e=>e.querySelector('img')).map(e=>({key:e.getAttribute('data-sku-col'),label:e.querySelector('img').alt,thumbnail:e.querySelector('img').src}))")
    dest = base / 'sources-fournisseur' / pid / 'variantes-lot3-20260904'
    dest.mkdir(parents=True, exist_ok=True)
    for item in variants:
        selector = '[data-sku-col="' + item['key'] + '"]'
        # Lecture DOM puis clic natif ; aucune invocation de logique applicative.
        rect = js('(()=>{let e=document.querySelector('+json.dumps(selector)+');e.scrollIntoView({block:"center"});let r=e.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2}})()')
        click_at_xy(rect['x'], rect['y'])
        time.sleep(0.2)
        state = js('({selected:Array.from(document.querySelectorAll("[data-sku-col][class*=selected]")).map(e=>e.getAttribute("data-sku-col")),hero:document.querySelector("[class*=magnifier--image]")?.src})')
        item['selected_confirmed'] = item['key'] in state['selected']
        # Ne rattacher la grande image que si son identifiant est celui de la vignette.
        image_id = re.search(r'/kf/([^/]+?\.(?:jpg|png|webp))', item['thumbnail'])
        hero = state.get('hero') or ''
        item['image_url'] = hero if image_id and image_id.group(1) in hero and item['selected_confirmed'] else item['thumbnail']
        target = dest / (item['key'] + '.avif')
        if not target.exists():
            try:
                with urlopen(item['image_url'], timeout=25) as response:
                    target.write_bytes(response.read())
            except Exception as error:
                item['download_error'] = str(error)
        item['local_path'] = str(target.relative_to(Path.cwd())) if target.exists() else None
        record['variants'].append(item)
    outfile = dest / 'preuves-dom.json'
    outfile.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'handle': handle, 'variants': len(variants), 'file':str(outfile), 'labels':[v['label'] for v in variants]},ensure_ascii=False))

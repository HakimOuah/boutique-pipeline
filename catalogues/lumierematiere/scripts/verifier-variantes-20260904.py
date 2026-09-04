"""Contrôle local des fichiers effectivement déclarés dans les manifestes du lot."""
import hashlib
import json
from pathlib import Path
from PIL import Image

BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]
DELIVERY = BASE / 'livraisons-visuels-codex/variantes-forme'

def main():
    checks, errors, hashes = [], [], set()
    manifests = sorted(DELIVERY.glob('*/manifeste.json'))
    for file in manifests:
        manifest = json.loads(file.read_text())
        required = {'brand', 'sku', 'handle', 'supplier_id', 'images', 'ecartes', 'collection'}
        if not required <= manifest.keys():
            errors.append(f'{file}: champs manquants')
        for asset in manifest['images']:
            image_path = file.parent / asset['fichier']
            source_path = REPO / asset['source']
            if not source_path.is_file():
                errors.append(f'Source manquante : {source_path}')
            with Image.open(image_path) as im:
                im.load()
                size, mode, format_ = im.size, im.mode, im.format
            valid = size == (2048, 2048) and mode == 'RGB' and format_ == 'JPEG'
            if not valid:
                errors.append(f'Format non conforme : {image_path}')
            digest = hashlib.sha256(image_path.read_bytes()).hexdigest()
            if digest in hashes:
                errors.append(f'Doublon binaire : {image_path}')
            hashes.add(digest)
            checks.append({'fichier':str(image_path.relative_to(REPO)), 'dimensions':size,
                           'mode':mode, 'format':format_, 'octets':image_path.stat().st_size,
                           'sha256':digest, 'source_existe':source_path.is_file(), 'format_conforme':valid})
    if len(manifests) != 20 or len(checks) != 15:
        errors.append(f'Comptage inattendu : {len(manifests)} manifestes, {len(checks)} images')
    geometry = json.loads((DELIVERY / 'qa-geometrie.json').read_text())
    for sheet in geometry:
        ratios = [g['width_px']/g['cm'] for g in sheet['geometrie']]
        if max(ratios)-min(ratios)>1e-9:
            errors.append(f'Échelle incohérente : {sheet["handle"]}')
    result = {'date':'2026-09-04', 'statut':'PASS_TECHNIQUE' if not errors else 'FAIL',
              'manifestes':len(manifests), 'livrables':len(checks), 'hashes_uniques':len(hashes),
              'schemas_echelle_calculee':len(geometry),
              'limite':'Ne valide ni les variantes live, ni les cotes absentes, ni le rattachement Shopify. QA visuelle décrite au journal.',
              'images':checks, 'erreurs':errors}
    target = BASE / 'journal/2026-09-04-variantes-formes-qa.json'
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='images'},ensure_ascii=False,indent=2))
    return bool(errors)

if __name__ == '__main__':
    raise SystemExit(main())

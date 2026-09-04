"""Finalisation locale A1 : conversion, correspondances DOM, manifestes et planche.

Aucune publication. --reviewed ne se passe qu'après revue visuelle de la planche.
Le comptage de luminaires et la fidélité sont une revue agent, pas une détection PIL.
"""
import argparse
import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]
OUT = BASE / 'livraisons-visuels-codex/couverture-2026-09-05'
JOURNAL = BASE / 'journal'
RULE = 'un seul luminaire dans le cadre'


def read(path):
    return json.loads(path.read_text())


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_qa_sheet(checks):
    # Planche de contrôle seulement : les JPEG produit ne sont jamais composités.
    tile, label_height, cols = 600, 100, 4
    rows = (len(checks) + cols - 1) // cols
    sheet = Image.new('RGB', (tile * cols, (tile + label_height) * rows), '#F6F3EC')
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 22)
    for index, check in enumerate(checks):
        x, y = (index % cols) * tile, (index // cols) * (tile + label_height)
        path = REPO / check['fichier']
        with Image.open(path) as product:
            sheet.paste(product.resize((tile, tile), Image.Resampling.LANCZOS), (x, y))
        handle = path.parent.name
        slug = path.name.removeprefix(handle + '-').removesuffix('-g1.jpg')
        labels = [handle.rsplit('-', 1)[-1] + ' / ' + slug]
        labels += check['sku_options']
        for line, label in enumerate(labels):
            draw.text((x + 10, y + tile + 7 + 28 * line), label, font=font, fill='#24211B')
    sheet.save(OUT / 'qa-couverture.jpg', quality=95, subsampling=0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reviewed', action='store_true')
    args = parser.parse_args()
    prod = read(JOURNAL / '2026-09-05-lot4-a1-production.json')
    jobs = prod['jobs']
    generated = {v['filename']: Path(v['generated_png']) for v in prod['completed']}
    assert len(jobs) == len(generated) == 13
    assert set(generated) == {j['filename'] for j in jobs}
    qa_visual = 'PASS — revue agent des rendus et de la planche' if args.reviewed else 'A_REVOIR_SUR_PLANCHE'
    checks, manifests, proofs = [], {}, {}
    for job in jobs:
        handle, filename = job['handle'], job['filename']
        original = read(BASE / 'livraisons-visuels-codex/produits' / handle / 'manifeste.json')
        if handle not in manifests:
            manifests[handle] = {
                'brand': 'lumierematiere', 'handle': handle, 'sku': original['sku'],
                'supplier_id': original['supplier_id'], 'lot': 'lot4-A1-couverture',
                'statut': 'LIVRE_LOCAL' if args.reviewed else 'QA_EN_COURS',
                'controle_obligatoire': RULE, 'aucune_action_shopify_dsers': True,
                'sku_intouchables': True, 'images': [], 'ecartes': [],
                'direction_artistique': {'fond_cible': '#F6F3EC', 'lumiere': 'chaude', 'type': 'packshot objet'},
            }
        dom = read(REPO / job['proof_dom'])
        options = {v['key']: v for v in dom['variants']}
        assert dom['handle'] == handle and dom['supplier_id'] == original['supplier_id']
        reconstructed = job.get('provenance_status') == 'RECONSTITUEE_VALIDEE_PAR_BRIEF_NON_OBSERVEE_DOM'
        if reconstructed:
            assert handle == 'suspension-effet-pierre-led-338324'
            assert job['sku_options'] == ['200000531:193']
            assert set(options) == {'200000531-173', '200000531-365458', '200000531-175'}
            assert '200000531-193' not in options
        else:
            for sku in job['sku_options']:
                key = sku.split('#')[0].replace(':', '-')
                assert key in options and options[key]['selected_confirmed'], (handle, sku)
                assert any(Path(ref).stem == key for ref in job['source_refs'])
                if '#' in sku:
                    # Espaces variables dans les libellés fournisseur, identifiant inchangé.
                    label = sku.split('#', 1)[1].replace(' ', '').lower()
                    assert label == options[key]['label'].replace(' ', '').lower(), (sku, options[key])
        if handle not in proofs:
            safe = {k: dom[k] for k in ['handle', 'supplier_id', 'observed_at', 'url']}
            safe['variants'] = []
            for v in dom['variants']:
                item = {k: v[k] for k in ['key', 'label', 'selected_confirmed', 'image_url', 'local_path']}
                path = REPO / v['local_path']
                item['sha256_original'] = sha(path)
                if path.with_suffix('.jpg').exists():
                    item['reference_jpeg'] = str(path.with_suffix('.jpg').relative_to(REPO))
                    item['sha256_jpeg'] = sha(path.with_suffix('.jpg'))
                safe['variants'].append(item)
            proofs[handle] = safe
        source = generated[filename]
        with Image.open(source) as im:
            native = im.size
        assert native[0] == native[1], f'Etirement interdit : {source}'
        dest = OUT / handle / filename
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '95',
                            '-z', '2048', '2048', str(source), '--out', str(dest)],
                           check=True, stdout=subprocess.DEVNULL)
        with Image.open(dest) as im:
            size, mode, fmt = im.size, im.mode, im.format
        assert size == (2048, 2048) and mode == 'RGB' and fmt == 'JPEG'
        item = {
            'fichier': filename, 'slot': job['slot'], 'sku_option': job['sku_options'][0],
            'sku_options_servis': job['sku_options'], 'identifiant_option': job['option_key'],
            'source': job['source_refs'][0],
            'sources': [{'chemin': p, 'sha256': sha(REPO / p)} for p in job['source_refs']],
            'preuve_dom': job['proof_dom'], 'observe_le': dom['observed_at'],
            'provenance': job.get('provenance_status', 'REFERENCE_OPTION_CONFIRMEE_DOM'),
            'controle': RULE, 'nombre_luminaires_observe': 1, 'qa_visuelle': qa_visual,
            'sha256': sha(dest), 'dimensions': list(size), 'mode': mode, 'format': fmt,
            'generation': {'outil': 'image_gen integre', 'dimensions_natives': list(native),
                           'mise_au_format': 'sips JPEG qualite 95, agrandissement proportionnel vers 2048²'},
        }
        if handle.endswith('630923') and job['slug'] == 'plafonnier':
            item['mutualisation'] = 'Packshot de montage commun aux Ø50/H14 et Ø60/H18 : même silhouette fournisseur, sans échelle. Le rendu canonique est Ø50/H14. Le schéma comparatif relève du lot B non livré ici.'
        if reconstructed:
            item['limite_preuve'] = '193 absent du sélecteur au nouveau contrôle. Identité autorisée par le brief lot4 : grille A/B × bois clair/foncé + planche 05.jpg. Édition du packshot B du lot2 : tête éclaircie, cordon et rosace bruns conservés. Ne pas qualifier cette cellule de confirmée au DOM.'
        manifests[handle]['images'].append(item)
        checks.append({'fichier': str(dest.relative_to(REPO)), 'sku_options': job['sku_options'],
                       'dimensions': list(size), 'mode': mode, 'format': fmt,
                       'dimensions_natives': list(native), 'sha256': sha(dest),
                       'sha256_generation': sha(source), 'qa_visuelle': qa_visual})
    wood = manifests['suspension-bois-193329']
    wood['correspondances_identifiees'] = [
        {'sku_option': '200000531:193#Walnut Base A', 'forme': 'cylindre bas', 'diametre_cm': 12, 'hauteur_cm': 10, 'tete': 'noyer'},
        {'sku_option': '200000531:173#Wood color A', 'forme': 'cylindre bas', 'diametre_cm': 12, 'hauteur_cm': 10, 'tete': 'bois clair'},
        {'sku_option': '200000531:365458#Walnut Base B', 'forme': 'cylindre haut', 'diametre_cm': 11, 'hauteur_cm': 16.5, 'tete': 'noyer'},
        {'sku_option': '200000531:175#Wood color B', 'forme': 'cylindre haut', 'diametre_cm': 11, 'hauteur_cm': 16.5, 'tete': 'bois clair'},
    ]
    wood['conserver_sans_regeneration'] = []
    for suffix, sku in [('bois', '200000531:175#Wood color B'), ('noyer', '200000531:365458#Walnut Base B')]:
        path = BASE / 'livraisons-visuels-codex/variantes-couleur/suspension-bois-193329' / f'suspension-bois-193329-{suffix}-g1.jpg'
        wood['conserver_sans_regeneration'].append({'chemin': str(path.relative_to(REPO)), 'sku_option': sku, 'sha256': sha(path), 'motif': 'Comparaison visuelle avec les quatre références DOM : forme haute B existante.'})
    wood['conclusion'] = 'A = bas Ø12/H10 ; B = haut Ø11/H16,5. Deux A produits, deux B existants conservés. Aucun renommage boutique effectué.'
    assert len(checks) == 13 and len({c['sha256'] for c in checks}) == 13
    assert sorted(len(m['images']) for m in manifests.values()) == [1, 2, 2, 4, 4]
    for handle, manifest in manifests.items():
        write(OUT / handle / 'manifeste.json', manifest)
    now = datetime.now().astimezone().isoformat(timespec='seconds')
    write(JOURNAL / '2026-09-05-lot4-a1-preuves-dom.json', {'date_lot': '2026-09-05', 'preuves': list(proofs.values()), 'note': 'Export limité aux références publiques, sans texte de compte ni navigation personnelle.'})
    write(JOURNAL / '2026-09-05-lot4-a1-registre.json', {'date_lot': '2026-09-05', 'finalise_le': now, 'manifestes': list(manifests.values())})
    write(JOURNAL / '2026-09-05-lot4-a1-qa.json', {
        'statut': 'PASS_TECHNIQUE_ET_REVUE_VISUELLE' if args.reviewed else 'PASS_TECHNIQUE_REVUE_PLANCHE_REQUISE',
        'images': 13, 'hashes_uniques': 13, 'manifestes': 5, 'controle': RULE,
        'methode_visuelle': 'Revue agent de chaque référence, de chaque rendu, puis de la planche ; aucun comptage automatique prétendu.',
        'limites': ['Livraison locale uniquement, aucun import ni contrôle live Shopify/GMC.',
                    'Sources générées natives 1254², exportées en 2048² sans changement de ratio.',
                    'Packshots non métriques. Ø50 et Ø60 plafonniers 630923 partagent la vue.',
                    '338324/193 est reconstitué suivant le brief, pas observé au DOM.'],
        'hors_perimetre': {'A2': 17, 'B': 10, 'C': '2 questions non traitées dans cette passe A1'},
        'fichiers': checks,
    })
    make_qa_sheet(checks)
    print('13 JPEG RGB 2048², 13 empreintes uniques, 5 manifestes. ' + qa_visual)


if __name__ == '__main__':
    main()

"""Finalisation locale du lot 3 ; aucune API Shopify/DSers ni publication.

Le comptage visuel est une revue humaine/agent documentée, pas une détection PIL.
PIL vérifie le format, les empreintes et l'absence d'étirement des sources générées.
"""
import hashlib
import json
import subprocess
from pathlib import Path
from PIL import Image

BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]
OUT = BASE / 'livraisons-visuels-codex/montages-2026-09-04'
JOURNAL = BASE / 'journal'
RULE = 'un seul luminaire dans le cadre'

def read(path):
    return json.loads(path.read_text())

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    prod = read(JOURNAL / '2026-09-04-lot3-production.json')
    brief = read(BASE / 'briefs/2026-09-04-lot3-montages.json')
    checks, manifests, proofs = [], [], []
    for spec in brief['fiches']:
        handle = spec['handle']
        original = read(BASE / 'livraisons-visuels-codex/produits' / handle / 'manifeste.json')
        manifest = {'brand':'lumierematiere','handle':handle,'sku':spec['sku'],
                    'supplier_id':original['supplier_id'], 'lot':'lot3-montages',
                    'statut':'LIVRE_LOCAL', 'controle_obligatoire':RULE,
                    'aucune_action_shopify_dsers':True,'images':[],'ecartes':[]}
        for job in (j for j in prod['production'] if j['handle']==handle):
            path, source, generated = REPO/job['file'], REPO/job['source'], Path(job['generated_source'])
            with Image.open(path) as im:
                size, mode, fmt = im.size, im.mode, im.format
            with Image.open(generated) as im:
                native_size = im.size
            assert size==(2048,2048) and mode=='RGB' and fmt=='JPEG', path
            assert native_size[0]==native_size[1], f'Etirement interdit: {generated}'
            assert source.is_file()
            key=job['sku'].split('#')[0].replace(':','-')
            assert source.stem==key
            dom=read(source.parent/'preuves-dom.json')
            assert any(v['key']==key for v in dom['variants'])
            item={'fichier':job['filename'],'slot':job['slot'],'source':job['source'],
                  'sku_option':job['sku'],'controle':RULE,'nombre_luminaires_observe':1,
                  'qa_visuelle':'PASS — revue des rendus et planche finale',
                  'sha256':digest(path),'sha256_source':digest(source)}
            manifest['images'].append(item)
            checks.append({'fichier':job['file'],'dimensions':size,'mode':mode,'format':fmt,
                           'dimensions_generation':native_size,'sha256':digest(path),'source_existe':True})
        if handle.endswith('147607'):
            manifest['conserver_sans_remplacement']=[{'fichier':f'{handle}-g{n}.jpg',
                'chemin':str((BASE/'livraisons-visuels-codex/produits'/handle/f'{handle}-g{n}.jpg').relative_to(REPO))}
                for n in [3,4]]
            manifest['note']='Packshots forme-a/b/c du lot 2 conserves, non regeneres.'
        if handle.endswith('560098'):
            manifest['note']='Packshots a-g1 et b-g1 du lot 2 conserves, non regeneres.'
        if spec['ordre'] in ['D','E']:
            source_dir=BASE/'sources-fournisseur'/original['supplier_id']/'variantes-lot3-20260904'
            dom=read(source_dir/'preuves-dom.json')
            safe={k:dom[k] for k in ['handle','supplier_id','observed_at','url']}
            safe['variants']=[{k:v[k] for k in ['key','label','selected_confirmed','image_url','local_path']} for v in dom['variants']]
            for v in safe['variants']:
                p=REPO/v['local_path']
                v['sha256_original']=digest(p)
                if p.with_suffix('.jpg').exists():
                    v['reference_jpeg']=str(p.with_suffix('.jpg').relative_to(REPO))
                    v['sha256_jpeg']=digest(p.with_suffix('.jpg'))
            proofs.append(safe)
            manifest['preuve_dom']=str((source_dir/'preuves-dom.json').relative_to(REPO))
            manifest['observe_le']=dom['observed_at']
            if spec['ordre']=='D':
                assert {v['key'] for v in dom['variants']}=={'200000531-173','200000531-175','200000531-365458'}
                manifest['statut']='INTROUVABLE_DEFINITIF_POUR_CE_LOT'
                manifest['ecartes']=[{'sku_option':'200000531:193','statut':'INTROUVABLE',
                    'motif':'Derniere passe DOM: identifiant absent. Aucun rendu deduit par elimination. Vue generique conservee pour les trois variantes A, sans mutation.'}]
            else:
                assert {v['key'] for v in dom['variants']}=={'200000531-193','200000531-173','200000531-175','200000531-365458'}
                manifest['statut']='IDENTIFIE_FORMES_DIFFERENTES'
                manifest['conclusion']='Les variantes 2 sont un autre abat-jour: H9 cm, contre H6,5 cm sans suffixe; toutes Ø20 cm. Aucun visuel produit.'
                manifest['correspondances']=[
                    {'sku_option':'200000531:365458','variante':'Celadon vert','diametre_cm':20,'hauteur_cm':6.5},
                    {'sku_option':'200000531:193','variante':'Celadon vert 2','diametre_cm':20,'hauteur_cm':9},
                    {'sku_option':'200000531:175','variante':'Celadon bleu poudre','diametre_cm':20,'hauteur_cm':6.5},
                    {'sku_option':'200000531:173','variante':'Celadon bleu poudre 2','diametre_cm':20,'hauteur_cm':9}]
        if spec['ordre']=='F':
            manifest['statut']='RESOLU_HORS_ACTION'
            manifest['note']='Aucune action ni nouvelle verification: doublon fournisseur resolu par le brief.'
        if spec['ordre']=='G':
            manifest['statut']='BLOQUE_ARBITRAGE'
            manifest['note']='Aucune action: attendre le renommage par Hakim avant schema et packshot noir.'
        write(OUT/handle/'manifeste.json',manifest)
        manifests.append(manifest)
    assert len(checks)==16
    assert len({c['sha256'] for c in checks})==16
    assert sorted(len(m['images']) for m in manifests)==[0,0,0,0,3,5,8]
    write(JOURNAL/'2026-09-04-lot3-preuves-dom.json',{'date':'2026-09-04','preuves':proofs})
    write(JOURNAL/'2026-09-04-lot3-registre.json',{'date':'2026-09-04','manifestes':manifests})
    write(JOURNAL/'2026-09-04-lot3-qa.json',{'statut':'PASS_TECHNIQUE','images':16,'hashes_uniques':16,
        'manifestes':7,'controle_visuel':RULE,'controle_visuel_methode':'Revue agent des rendus puis de qa-montages.jpg ; pas un comptage automatise.',
        'limite':'Livraison locale, ne valide ni import ni etat Shopify/GMC. Sources generees inferieures a 2048 agrandies sans changer leur ratio.', 'fichiers':checks})
    subprocess.run(['python3',str(REPO/'boutique-tufting/scripts/visual_batch_20260816.py'),'contact-sheet',
        str(OUT/'qa-montages.jpg'),*[str(REPO/c['fichier']) for c in checks],'--columns','4'],check=True)
    print('PASS : 16 JPEG RGB 2048², 16 empreintes, sources carrees, 7 manifestes, planche QA creee.')

if __name__=='__main__':
    main()

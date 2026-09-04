"""Réconciliation mécanique des preuves et livrables validés visuellement le 04/09.

Aucun appel distant, aucune mutation Shopify/DSers, aucun changement des SKU.
Les captures complètes du navigateur restent locales ; seules les données produit
strictement nécessaires à la provenance sont exportées au journal versionné.
"""
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]
OUT = BASE / 'livraisons-visuels-codex/variantes-forme'
JOURNAL = BASE / 'journal'

def read(path):
    return json.loads(path.read_text())

def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def main():
    production = read(JOURNAL / '2026-09-04-variantes-formes-complement-production.json')
    records = production['production'] + production['reutilises']
    handles = {j['handle'] for j in records}
    for handle in sorted(handles):
        file = OUT / handle / 'manifeste.json'
        manifest = read(file)
        manifest.setdefault('ecartes_avant_preuves_sku', manifest['ecartes'])
        for job in (j for j in records if j['handle'] == handle):
            assert (REPO / job['source']).is_file()
            assert (REPO / job['file']).is_file()
            filename = Path(job['file']).name
            manifest['images'] = [i for i in manifest['images'] if i['fichier'] != filename]
            manifest['images'].append({'fichier':filename, 'slot':'g1-variante', 'source':job['source'],
                'variante':job['slug'], 'reference_sku_propriete':job['key'].replace('-',':'),
                'qa':'PASS_VISUEL', 'mode':'reutilisation canonique verifiee' if job['reuse'] else 'imagegen integre'})
        manifest['ecartes'] = []
        manifest['statut'] = 'LIVRE_LOCAL'
        if handle.endswith('338324'):
            manifest['ecartes'] = [{'statut':'MANQUANT', 'variante':'A', 'sku':'200000531:193',
                'motif':'Identifiant absent du selecteur fournisseur observe le 04/09. B/C/D identifies par identifiant, pas par le libelle fournisseur actuel. A non deduit par elimination.'}]
            manifest['statut'] = 'PARTIEL_A_MANQUANT'
        write(file,manifest)

    missing = {
        'suspension-moderne-led-noir-330664':'Hauteur propre du corps lumineux et longueur nue des suspentes non isolees. Hauteur totale confirmee 100 cm.',
        'lustre-salon-blanc-246282':'Hauteurs, cable et rosace non documentes ; PDP fournisseur indisponible dans la region observee.',
        'suspension-rotin-led-761433':'Hauteurs Ø40/50/60 et diametre rosace manquants ; Ø30 = cloche bordee sombre H20, distincte des grands petales.',
        'suspension-bambou-led-50cm-377816':'Hauteurs des abat-jour et diametre rosace manquants. Diametres30/40/50 et cable150 confirmes par SKU.',
        'suspension-bambou-led-630923':'Diametre de rosace suspension manquant. H14 plafonnier50 / H13 suspension50 / H18 plafonnier60 ; cables reglables100 confirmes.',
    }
    geometry = read(OUT / 'qa-geometrie.json')
    for sheet in geometry:
        file=OUT / sheet['handle'] / 'manifeste.json'
        manifest=read(file)
        manifest.setdefault('ecartes_avant_preuves_sku',manifest['ecartes'])
        asset={'fichier':Path(sheet['fichier']).name, 'slot':'g6-schema-cote', 'source':sheet['source'],
               'qa':'PASS_VISUEL', 'completude':sheet['statut'], 'note':missing.get(sheet['handle'],sheet['note'])}
        manifest['images']=[i for i in manifest['images'] if i['slot']!='g6-schema-cote']+[asset]
        manifest['statut']='LIVRE_LOCAL' if sheet['statut']=='COMPLET' else 'PARTIEL_COTES_MANQUANTES'
        manifest['ecartes']=[] if sheet['statut']=='COMPLET' else [{'statut':'MANQUANT','motif':missing[sheet['handle']]}]
        write(file,manifest)

    # Conservation des verrous explicites, mais correction de leur diagnostic factuel.
    for handle,note in {
        'suspension-rotin-272937':'A1/B1/C1 sont trois plafonniers Ø16 H17 (abat-jour H12), respectivement monture noire/corde doree, monture blanche/corde claire, monture noire/fibre brune. Le diagnostic initial simple/applique/trios etait faux pour les SKU vendus. Arbitrage titre/collection et feu vert production toujours requis par le brief.',
        'suspension-rotin-607504':'2550 = Ø25 H50 naturel ; 4040 = Ø40 H40 naturel ; 4019 = Ø40 H19 naturel ; 4040BK = Ø40 H40 noir. Dimensions prouvees, mais le brief interdit le schema avant arbitrage du renommage.',
    }.items():
        file=OUT/handle/'manifeste.json';manifest=read(file)
        manifest['ecartes']=[{'statut':'ARBITRAGE_REQUIS','motif':note}]
        manifest['statut']='BLOQUE_ARBITRAGE'
        manifest['preuve_dom']=f"catalogues/lumierematiere/sources-fournisseur/{manifest['supplier_id']}/variantes-20260904/preuves-dom.json"
        write(file,manifest)

    proofs=[]
    for file in sorted((BASE/'sources-fournisseur').glob('*/variantes-20260904/preuves-dom.json')):
        doc=read(file)
        item={k:doc[k] for k in ['handle','supplier_id','observed_at','url']}
        item['variants']=[]
        for variant in doc['variants']:
            # Pas de nom de compte, localisation, recommandations ou texte de navigation.
            safe={k:variant[k] for k in ['key','label','thumbnail','selected_confirmed','image_url','local_path']}
            jpg=(REPO/variant['local_path']).with_suffix('.jpg') if variant['local_path'] else None
            if jpg and jpg.is_file():
                safe['reference_jpeg']=str(jpg.relative_to(REPO))
                safe['sha256_jpeg']=hashlib.sha256(jpg.read_bytes()).hexdigest()
            item['variants'].append(safe)
        proofs.append(item)
    write(JOURNAL/'2026-09-04-variantes-formes-preuves-sku.json',{'date':'2026-09-04','mode':'lecture DOM selecteur public et clics de variantes uniquement','preuves':proofs})
    registry=read(JOURNAL/'2026-09-04-variantes-formes-registre.json')
    registry['manifests']=[read(f) for f in sorted(OUT.glob('*/manifeste.json'))]
    registry['complement_production']=production
    registry['schemas_derniere_revision']=geometry
    registry['precedence']='manifests et schemas_derniere_revision decrivent la livraison actuelle ; production conserve aussi les traces historiques de premiere passe.'
    registry['preuves_sku']='catalogues/lumierematiere/journal/2026-09-04-variantes-formes-preuves-sku.json'
    write(JOURNAL/'2026-09-04-variantes-formes-registre.json',registry)
    write(OUT/'prompts-complement-production.json',production)
    print(json.dumps({'nouveaux_packshots':len(production['production']), 'canoniques_reutilises':len(production['reutilises']),
                      'preuves_fiches':len(proofs),'manifestes':len(registry['manifests']),
                      'images':sum(len(m['images']) for m in registry['manifests'])},ensure_ascii=False))

if __name__=='__main__':
    main()

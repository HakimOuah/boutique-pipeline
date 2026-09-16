import json,re,unicodedata,collections,os
W='/private/tmp/claude-502/-Users-Hakim-Documents-Boutiques-drop/3e7e2b1c-6159-4d50-8344-3a7c42b52fca/scratchpad/wt-shop'
d=json.load(open('codex/plan_visuels.json'))
def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')
FAM=[('fauteuils-bascule','1100','fauteuils-bascule'),('allaitement-enfant','1110','allaitement-enfant'),
     ('relax-exterieur','1120','relax-cocon-exterieur'),('poufs','1130','poufs-repose-pieds'),('accessoires','1140','coussins-plaids-tables')]
OUT='boutique-rocking-chair/livraisons/visuels-lot2-catalogue-2026-09-16'
BR='boutique-rocking-chair/BRIEF-VISUELS-CODEX-LOT2-CATALOGUE-2026-09-16.md'
tot={}
for fam,hh,name in FAM:
    man=[];src=[]
    for r in [x for x in d if x['famille']==fam]:
        base=f"boutique-rocking-chair/assets/source/{r['pid']}"; src.append(base)
        cible=r['couleur_galerie_cible']
        refc=r['refs'].get(cible) if cible else None
        for s in r['slots']:
            man.append({'handle':r['handle'],'sku':r['sku'],'pid':r['pid'],'h1':r['h1'],'slot':s['slot'],
                'fichier':f"{r['handle']}-{s['slot']}.jpg",'contenu_fiche':s['contenu'],
                'couleur':cible,'reference_couleur':refc,
                'format':'2048x2048'})
        for c in r['couleurs']:
            if c==cible: continue
            man.append({'handle':r['handle'],'sku':r['sku'],'pid':r['pid'],'h1':r['h1'],'slot':'couleur',
                'fichier':f"{r['handle']}-couleur-{slug(c)}.jpg",'couleur':c,'reference_couleur':r['refs'][c],
                'reference_scene':f"{OUT}/{name}/{r['handle']}-desir.jpg",'format':'2048x2048'})
    o={'id':f'claude-20260916-{hh}-bercelou-lot2-{name}','type':'generate_images','created_at':'2026-09-16T12:00:00Z',
       'requested_by':'claude-code',
       'notes':f'Bercelou, lot 2 du catalogue, famille {name} : {len(set(m["handle"] for m in man))} fiches, {len(man)} images. Remplace toutes les photos fournisseur. Aucun accès boutique.',
       'payload':{'manifest':man,'sources':sorted(set(src)),
         'da':{'reference':'docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md §3','surcharges':f'boutique-rocking-chair/BRIEF-VISUELS-CODEX-2026-09-14.md §2 + BRIEF-VISUELS-CODEX-LOTS-2-5-2026-09-15.md §1-2 + BRIEF-VISUELS-CODEX-VARIANTES-2026-09-16.md §1 + {BR} (prioritaire).'},
         'contraintes':{'reference':'docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md §4','specifiques':[
            f'Lire EN ENTIER {BR} : ses règles priment sur contenu_fiche en cas de conflit.',
            'Toutes les images d\'une fiche (hors slot couleur) sont dans le coloris `couleur`, teinte prise sur reference_couleur (ou sur 01.jpg si reference_couleur est null).',
            'Slot couleur : générer après le desir de la même fiche ; même scène que reference_scene, seule la teinte change.',
            'Aucun texte, logo, cote, pictogramme ; slot dimensions = produit seul sur fond uni, sans aucune cote.',
            'Si les sources contredisent le H1, ne pas générer la fiche : rejet avec motif.']},
         'qa_attendue':{'reference':'docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md §5','specifiques':['qa/verite-<handle>.md avant génération','qa/controle-<handle>.jpg : 01.jpg, référence couleur et images livrées côte à côte']},
         'sortie':{'dossier':f'{OUT}/{name}/','manifeste':'manifeste-realise.json'}}}
    fn=f"{W}/ordres/pour-codex/inbox/20260916-{hh}-generate_images-bercelou-lot2-{name}.json"
    json.dump(o,open(fn,'w'),ensure_ascii=False,indent=1)
    tot[name]=(len(set(m['handle'] for m in man)),len(man),sum(1 for m in man if m['slot']=='couleur'))
print(tot, sum(v[1] for v in tot.values()))

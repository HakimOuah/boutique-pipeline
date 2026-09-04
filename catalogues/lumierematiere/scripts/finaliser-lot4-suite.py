"""Finalise A2, B et C en preservant A1. Local uniquement, aucune API boutique.

--reviewed atteste la revue visuelle agent, jamais un comptage automatique.
"""
import argparse
import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE=Path(__file__).resolve().parents[1]
REPO=BASE.parents[1]
OUT=BASE/'livraisons-visuels-codex/couverture-2026-09-05'
JOURNAL=BASE/'journal'
RULE='un seul luminaire dans le cadre'
def read(p): return json.loads(p.read_text())
def write(p,d):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p): return str(p.relative_to(REPO))
def checked_image(p):
    with Image.open(p) as im:
        assert im.size==(2048,2048) and im.mode=='RGB' and im.format=='JPEG',p
    return {'dimensions':[2048,2048],'mode':'RGB','format':'JPEG','sha256':sha(p)}
def sheet(items,name,cols=4):
    # QA only: composition of thumbnails; never used as a product image.
    tile,lh=600,100
    canvas=Image.new('RGB',(cols*tile,((len(items)+cols-1)//cols)*(tile+lh)),'#F6F3EC')
    draw=ImageDraw.Draw(canvas)
    font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',22)
    for i,(p,label,skus) in enumerate(items):
        x,y=(i%cols)*tile,(i//cols)*(tile+lh)
        with Image.open(p) as im: canvas.paste(im.convert('RGB').resize((tile,tile),Image.Resampling.LANCZOS),(x,y))
        draw.text((x+10,y+605),label,font=font,fill='#24211B')
        draw.text((x+10,y+637),' / '.join(skus[:2]),font=font,fill='#24211B')
        if len(skus)>2: draw.text((x+10,y+666),f'+ {len(skus)-2} options (voir manifeste)',font=font,fill='#24211B')
    canvas.save(OUT/name,quality=95,subsampling=0)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reviewed',action='store_true')
    args=parser.parse_args()
    qa='PASS — revue agent du rendu et de la référence' if args.reviewed else 'A_REVOIR'
    jobs=read(JOURNAL/'2026-09-05-lot4-a2-production.json')['jobs']
    results={r['file']:r for r in read(JOURNAL/'2026-09-05-lot4-a2-resultats.json')}
    schemas=read(BASE/'scripts/lot4-schema-jobs.json')
    products={p['handle']:p for p in read(BASE/'shopify/variants-work.json')}
    manifests={p.parent.name:read(p) for p in OUT.glob('*/manifeste.json')}
    def manifest(h):
        if h not in manifests:
            p=BASE/'livraisons-visuels-codex/produits'/h/'manifeste.json'
            old=read(p) if p.exists() else {}
            manifests[h]={'brand':'lumierematiere','handle':h,'sku':old.get('sku'),'supplier_id':old.get('supplier_id'),'images':[],'ecartes':[]}
        m=manifests[h]
        m.update(lot='lot4-couverture',controle_obligatoire=RULE,aucune_action_shopify_dsers=True,sku_intouchables=True)
        return m
    def upsert(m,item):
        m['images']=[x for x in m['images'] if x['fichier']!=item['fichier']]+[item]
    proofs={}
    for job in jobs:
        h=job['h'];m=manifest(h);r=results[job['file']]
        source=REPO/job['source'];p=source.parent/'preuves-dom.json';dom=read(p)
        v=next(v for v in dom['variants'] if v['key']==job['key'])
        # La vignette est un enfant direct du noeud data-sku-col : lien DOM
        # valable même si le clic n'a pas confirmé une nouvelle sélection.
        # Dans ce cas le collecteur interdit de prendre le hero d'une autre option.
        assert dom['handle']==h and (v['selected_confirmed'] or v['image_url']==v['thumbnail']), (h,job['key'])
        ident=job['sku_option'].split('#')[0]
        full=[v['sku'] for v in products[h]['variants'] if any(s.split('#')[0]==ident for s in v['sku'].split(';'))]
        assert full,(h,ident)
        exact=next(s for s in full[0].split(';') if s.split('#')[0]==ident)
        png=Path(r['png']);dest=OUT/h/job['file'];dest.parent.mkdir(parents=True,exist_ok=True)
        with Image.open(png) as im: native=im.size
        assert native[0]==native[1]
        if not dest.exists(): subprocess.run(['sips','-s','format','jpeg','-s','formatOptions','95','-z','2048','2048',str(png),'--out',str(dest)],check=True,capture_output=True)
        item={'fichier':job['file'],'slot':'g1-variante','lot':'A2','sku_option':exact,'sku_options_servis':[exact],'sku_complets_servis':full,'identifiant_option':ident,'source':rel(source),'sources':[{'chemin':rel(source),'sha256':sha(source),'dimensions_source':list(Image.open(source).size)}],'preuve_dom':rel(p),'observe_le':dom['observed_at'],'provenance':'REFERENCE_OPTION_CONFIRMEE_DOM','controle':RULE,'nombre_luminaires_observe':1,'nombre_lumieres_attendu':job['count'],'nombre_lumieres_observe':job['count'] if args.reviewed else None,'qa_visuelle':qa,'generation':{'outil':'image_gen integre','dimensions_natives':list(native),'mise_au_format':'sips JPEG qualite 95, agrandissement proportionnel 2048²','sha256_png':sha(png)},**checked_image(dest)}
        item['selection_confirmee']=v['selected_confirmed']
        if not v['selected_confirmed']:
            item['provenance']='VIGNETTE_DANS_NOEUD_OPTION_DOM — sélection non confirmée'
            item['limite_preuve']='Image enfant du noeud data-sku-col exact; pas de hero substitué. Référence 220², comptage lisible, détails fins limités.'
        if r.get('additional_source'): item['sources'].append({'chemin':r['additional_source'],'sha256':sha(REPO/r['additional_source']),'role':'Rosace, chaine et tige uniquement; bras issus de la reference DOM exacte'})
        if 'No bulb' in ' '.join(full) or 'Not with Bulb' in ' '.join(full): item['reserve_ampoules']='Ampoules représentées comme sur la source; SKU sans ampoule. Ne pas présenter les ampoules comme incluses.'
        upsert(m,item)
        proofs[h]=dom
    for j in schemas:
        h=j['h'];m=manifest(h);source=BASE/'sources-par-handle'/h/j['source'];assert source.exists(),source
        filename=h+'-schema-g6.jpg';dest=OUT/h/filename
        upsert(m,{'fichier':filename,'slot':'g6-schema-cote','lot':'B','sku_option':j['skus'][0],'sku_options_servis':j['skus'],'source':rel(source),'sources':[{'chemin':rel(source),'sha256':sha(source)}],'controle':RULE,'nombre_luminaires_observe':1,'qa_visuelle':qa,'generation':{'outil':'SVG original et sharp','dimensions_natives':[2048,2048]},'cotes':j['rows'],'regle_echelle':'Une silhouette de référence seulement; traits comparatifs de largeur à échelle commune. Pas de hauteur inventée.','limites':j['note'],'exception_texte':'Lot B uniquement: cotes et tableau des variantes autorises','svg':filename.replace('.jpg','.svg'),**checked_image(dest)})
    for h in ['suspension-bois-led-934110','suspension-effet-pierre-092465']:
        m=manifest(h);p=BASE/'sources-par-handle'/h/'variantes-lot4-20260905/preuves-dom.json';dom=read(p);proofs[h]=dom
        m.update(images=[],lot='lot4-C-identification',preuve_dom=rel(p),observe_le=dom['observed_at'],statut='REPONSE_DOCUMENTEE_SANS_IMAGE')
        m['references']=[{'sku_option':v['key'].replace('-',':',1),'libelle_dom':v['label'],'chemin':rel(p.parent/(v['key']+'.jpg')),'sha256':sha(p.parent/(v['key']+'.jpg'))} for v in dom['variants']]
        if h.endswith('934110'):
            a,b=p.parent/'200000531-173.jpg',p.parent/'200000531-175.jpg'
            m['conclusion']='Pas de grille démontrée deux matières × température. Le fournisseur juxtapose Yellow Travertine (un tube) et 3000k/6000k (deux tubes sur une rosace commune). Les trois références montrent une pierre poreuse beige, pas une matière blanche distincte.'
            m['observations']={'200000531:193':'Un tube travertin Ø4 × H28; cordon annoncé 1,8 m réglable','200000531:173':'Deux tubes Ø4 × H28, cordons 150 cm; intitulé 3000k-warm white','200000531:175':'Même composition double; intitulé 6000k-cold white','references_173_175_identiques_sha256':sha(a)==sha(b),'autre_axe_dom':dom.get('option_values',[])}
            m['blocage']='Un second axe 5:361385 est fixé à 3000K warm light, y compris face au choix 6000k. Température réellement livrée non établie. Confirmation fournisseur nécessaire avant normalisation des options; aucune image produite.'
        else:
            m['conclusion']='Correspondance confirmée: 200000531:200006153 = jaune clair / Pierre claire, tête bois clair; 200000531:365458 = Brun, tête bois brun foncé. Les deux packshots existants correspondent.'
            m['conserver_sans_regeneration']=[]
            for slug,key in [('pierre-claire','200006153'),('brun','365458')]:
                p0=BASE/'livraisons-visuels-codex/variantes-forme'/h/(h+'-'+slug+'-g1.jpg')
                m['conserver_sans_regeneration'].append({'chemin':rel(p0),'sha256':sha(p0),'sku_option':'200000531:'+key})
    retained={
        'lustre-anneau-led-led-717226':[('produits','g1','200000795:193#6 lights')],
        'lustre-anneau-led-led-625575':[('produits','g1','200000795:193#6 lights')],
        'lustre-anneau-led-led-134962':[('variantes-couleur','blanc-g1','200000531:-5'),('variantes-couleur','noir-g1','200000531:-1'),('variantes-couleur','dore-g1','200000531:-3')],
        'lustre-statement-led-noir-950316':[('produits','g1','200000795:193#6 heads')],
        'suspension-metal-noir-dore-361680':[('variantes-couleur','noir-g1','200000531:365458#Black 6T'),('variantes-couleur','dore-g1','200000531:366#Gold 6T')],
        'plafonnier-led-992600':[('variantes-couleur','noir-g1','200000531:365458#black 6 heads'),('variantes-couleur','blanc-g1','200000531:350852#white 6 heads'),('variantes-couleur','dore-g1','200000531:200002984#gold 6 heads')],
    }
    for h,entries in retained.items():
        m=manifest(h);m['conserver_sans_regeneration']=[]
        for family,suffix,sku in entries:
            p=BASE/'livraisons-visuels-codex'/family/h/(h+'-'+suffix+'.jpg')
            m['conserver_sans_regeneration'].append({'chemin':rel(p),'sha256':sha(p),'sku_option':sku,'motif':'Comptage existant vérifié visuellement contre référence DOM'})
    m=manifest('plafonnier-led-led-183789')
    m['ecartes']=[{'chemin':f'catalogues/lumierematiere/livraisons-visuels-codex/variantes-couleur/{m["handle"]}/{m["handle"]}-{c}-g1.jpg','motif':'Sept palets lumineux visibles (six périphériques + centre), aucun SKU vendu à sept. Ne pas utiliser pour cinq ni six.'} for c in ['gris','blanc']]
    missing=[sku for sku in ['200000795:366#grey 6 lights','200000795:10#White  6 lights'] if not any(sku in im['sku_options_servis'] for im in m['images'])]
    m['reste_a_produire']=missing
    m['reserve']='Deux visuels supplémentaires nécessaires pour les versions à six. Autorisation demandée pour dépasser le plafond de quarante.' if missing else 'Quatre variantes désormais couvertes; retirer les anciens visuels à sept lors de l’import séparé.'
    allitems=[];bitems=[];aitems=[]
    for h,m in manifests.items():
        if m['images']:
            m['statut']='LIVRE_LOCAL' if args.reviewed else 'QA_EN_COURS'
            if h.endswith('183789') and missing: m['statut']='LIVRE_PARTIEL_ARBITRAGE_2_IMAGES_SUPPLEMENTAIRES'
        for im in m['images']:
            p=OUT/h/im['fichier'];checked_image(p)
            assert im['controle']==RULE
            label=h.rsplit('-',1)[-1]+' / '+im['fichier'].removeprefix(h+'-').removesuffix('.jpg')
            t=(p,label,im['sku_options_servis']);allitems.append(t)
            if im.get('lot')=='B': bitems.append(t)
            if im.get('lot')=='A2': aitems.append(t)
        write(OUT/h/'manifeste.json',m)
    safe=[]
    for h,d in proofs.items():
        x={k:d[k] for k in ['handle','supplier_id','observed_at','url']};x['option_values']=d.get('option_values',[]);x['variants']=[]
        for v in d['variants']:
            p=BASE/'sources-par-handle'/h/'variantes-lot4-20260905'/(v['key']+'.jpg')
            x['variants'].append({k:v[k] for k in ['key','label','selected_confirmed','image_url','thumbnail']}|{'reference_jpeg':rel(p),'sha256_jpeg':sha(p),'dimensions':list(Image.open(p).size),'downloaded_url':v.get('downloaded_url',v['image_url'])})
        safe.append(x)
    write(JOURNAL/'2026-09-05-lot4-suite-preuves-dom.json',{'preuves':safe})
    write(JOURNAL/'2026-09-05-lot4-suite-registre.json',{'finalise_le':datetime.now().astimezone().isoformat(),'manifestes':list(manifests.values())})
    originals=read(JOURNAL/'2026-09-05-lot4-a1-registre.json')['manifestes']
    for original in originals:
        for im in original['images']: assert sha(OUT/original['handle']/im['fichier'])==im['sha256'], 'A1 modifie'
    assert len({sha(p) for p,_,_ in allitems})==len(allitems), 'JPEG duplique'
    assert len(bitems)==10 and len(aitems) in [17,19] and len(allitems)==13+10+len(aitems)
    report={'images_total':len(allitems),'hashes_uniques':len(allitems),'manifestes':len(manifests),'A1_preserve':13,'A1_sha256_inchanges':True,'A2_nouveaux':len(aitems),'B_nouveaux':len(bitems),'C_reponses':2,'reserve_183789':missing,'qa':qa,'limite':'Local uniquement. Aucune publication, aucun contrôle boutique public dans cette passe.'}
    write(JOURNAL/'2026-09-05-lot4-suite-qa.json',report)
    sheet(allitems,'qa-couverture.jpg');sheet(bitems,'qa-schemas.jpg',2);sheet(aitems,'qa-a2.jpg')
    print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':main()

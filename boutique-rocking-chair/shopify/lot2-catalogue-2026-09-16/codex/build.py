import json,re,unicodedata,collections
P=[]
for f in ['q1','q2','q3']: P+=json.load(open(f'codex/{f}.json'))['data']['products']['nodes']
I=json.load(open('gql/INDEX.json')); byg={v['gid']:(h,v) for h,v in I.items()}
M={m['gid']:m for m in json.load(open('map_final.json'))}
def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')
def base(u): return u.split('?')[0].rsplit('/',1)[-1]
ROLE={'Désir':'desir','Usage':'usage','Matière':'matiere','Dimensions cotées':'dimensions','Situation':'situation','Détail':'detail'}
out=[];flags=[]
for p in P:
    h,v=byg[p['id']]; pid=v['pid']; fam=M[p['id']]['famille']
    media=[n['image']['url'] for n in p['media']['nodes'] if n.get('image')]
    cols=collections.OrderedDict()
    for vr in p['variants']['nodes']:
        c=next((o['value'] for o in vr['selectedOptions'] if o['name']=='Couleur'),None)
        if c and c not in cols: cols[c]=vr['image']['url'] if vr.get('image') else None
    # couleur de la galerie = coloris dont l'image variante = media[0]
    gal=None
    if media:
        for c,u in cols.items():
            if u and base(u)==base(media[0]): gal=c
    rec={'handle':h,'pid':pid,'famille':fam,'h1':p['title'],'sku':p['variants']['nodes'][0]['sku'],
         'collections':v['collections'],'media':media[:8],'couleurs':cols,'couleur_galerie_actuelle':gal}
    if cols:
        cible = gal or next(iter(cols))
        rec['couleur_galerie_cible']=cible
        if not gal: flags.append((h,'galerie: couleur de 01.jpg non identifiée, cible = '+cible))
        for c,u in cols.items():
            if not u: flags.append((h,f'coloris {c} sans photo variante'))
    else:
        rec['couleur_galerie_cible']=None
    slots=[]
    for a in v['alts']:
        m=re.match(r'\*\*(.*?)\*\*\s*[—-]\s*(.*)',a); slots.append({'slot':ROLE[m.group(1)],'contenu':m.group(2)})
    rec['slots']=slots
    out.append(rec)
json.dump(out,open('codex/plan_visuels.json','w'),ensure_ascii=False,indent=1)
print(len(out), collections.Counter(r['famille'] for r in out))
print('couleur slots', sum(max(0,len(r['couleurs'])-1) for r in out), 'mono', sum(1 for r in out if len(r['couleurs'])<=1))
for f in flags: print(f)

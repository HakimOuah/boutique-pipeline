import json,os,io,re,unicodedata,urllib.request,shutil,concurrent.futures as cf
from PIL import Image
DST='/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/boutique-rocking-chair/assets/source'
d=json.load(open('codex/plan_visuels.json'))
def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')
def get(url,path):
    if os.path.exists(path): return 'skip'
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    b=urllib.request.urlopen(req,timeout=60).read()
    im=Image.open(io.BytesIO(b)).convert('RGB')
    os.makedirs(os.path.dirname(path),exist_ok=True); im.save(path,'JPEG',quality=92); return 'ok'
jobs=[]
for r in d:
    base=f"{DST}/{r['pid']}"
    for i,u in enumerate(r['media'],1): jobs.append((u,f"{base}/{i:02d}.jpg"))
    r['refs']={}
    for c,u in r['couleurs'].items():
        p=f"{base}/couleurs/{slug(c)}.jpg"; r['refs'][c]=p.split('boutique-pipeline/')[1]
        if u: jobs.append((u,p))
        elif r['handle']=='fauteuil-lounge-cotele-avec-pouf' and c=='Vert sauge':
            os.makedirs(os.path.dirname(p),exist_ok=True); shutil.copy(f"img/{r['pid']}/c02.jpg",p)
with cf.ThreadPoolExecutor(8) as ex:
    res=list(ex.map(lambda j: (j[1],get(*j)) if True else None, jobs))
json.dump(d,open('codex/plan_visuels.json','w'),ensure_ascii=False,indent=1)
print(len(jobs), sum(1 for _,s in res if s=='ok'))

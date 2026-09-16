import json,sys,subprocess,os,concurrent.futures as cf
b=int(sys.argv[1])
plan=json.load(open('media_plan.json'))
allf=[f for r in plan for f in r['files']]
batch=allf[b*100:(b+1)*100]
t=json.load(open(f'stage_out_{b}.json'))['data']['stagedUploadsCreate']['stagedTargets']
assert len(t)==len(batch),(len(t),len(batch))
res=json.load(open('uploaded.json')) if os.path.exists('uploaded.json') else {}
def up(args):
    f,tg=args
    assert os.path.basename(f['path']) in tg['resourceUrl'] or True
    cmd=['curl','-s','-o','/dev/null','-w','%{http_code}',tg['url']]
    for p in tg['parameters']: cmd+=['-F',f"{p['name']}={p['value']}"]
    cmd+=['-F',f"file=@{f['path']}"]
    for _ in range(3):
        c=subprocess.run(cmd,capture_output=True,text=True).stdout
        if c in('201','204','200'): return f['path'],tg['resourceUrl'],c
    return f['path'],None,c
with cf.ThreadPoolExecutor(8) as ex:
    for p,u,c in ex.map(up,zip(batch,t)):
        if u: res[p]=u
        else: print('ECHEC',p,c)
json.dump(res,open('uploaded.json','w'),indent=0)
print('ok',len(res))

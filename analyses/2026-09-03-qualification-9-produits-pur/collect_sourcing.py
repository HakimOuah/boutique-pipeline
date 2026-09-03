"""Sonde fournisseur AliExpress en lecture seule, aucun achat ni import."""
import concurrent.futures, datetime, importlib.util, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('gateway',ROOT.parents[1]/'codex-chasse-clusters/tools/aliexpress_vps_gateway.py')
gateway=importlib.util.module_from_spec(spec);spec.loader.exec_module(gateway)
QUERIES={
 'A1':['folding lock','articulated lock'],
 'A2':['retro digital','vintage digicam'],
 'A5':['Xteink X4','inkpalm 5'],
 'A6':['safety shaving set','Yaqi razor'],
 'B1':['folding drying','retractable laundry'],
 'B2':['swivel bike rack','pivot bicycle rack'],
 'B3':['magnetic window mesh','magnetic window frame'],
 'C2':['tv wireless headphone','optical headphone transmitter'],
 'C6':['titanium frying pan','pure titanium pan'],
}
def one(cid,i,q):
 p=ROOT/'sourcing'/f'{cid}-search-{i}.json';p.parent.mkdir(exist_ok=True)
 if p.exists():return str(p)
 req={'action':'search','query':q,'limit':20,'destination':'FR','sort_by':'price_desc' if i==1 else 'orders'}
 try:
  result=gateway.call_gateway(req,host=gateway.DEFAULT_HOST,user=gateway.DEFAULT_USER,identity=gateway.DEFAULT_IDENTITY,timeout=50)
 except Exception as exc:result={'ok':False,'error':str(exc)}
 p.write_text(json.dumps({'observed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'request':req,'response':result},ensure_ascii=False,indent=2)+'\n')
 return cid+' '+q+' ok='+str(result.get('ok'))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  jobs=[pool.submit(one,cid,i,q) for cid,qs in QUERIES.items() for i,q in enumerate(qs)]
  for f in concurrent.futures.as_completed(jobs):print(f.result(),flush=True)

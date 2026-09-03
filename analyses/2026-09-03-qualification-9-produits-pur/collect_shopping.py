import sys,json
from collect_dfs import call,ROOT
from collect_controls import ANCHORS
if __name__=='__main__':
 if '--post' in sys.argv:
  call('50-shopping-post','merchant/google/products/task_post',
   [{'keyword':q[0],'location_name':'France','language_name':'French','depth':40,'tag':cid} for cid,q in ANCHORS.items()])
 else:
  import gzip
  j=json.load(gzip.open(ROOT/'raw/50-shopping-post.json.gz','rt'))
  for t in j['response']['tasks']:
   cid=t['data']['tag']
   try:call('51-shopping-'+cid,'merchant/google/products/task_get/advanced/'+t['id'],None)
   except Exception as exc:print(cid,'MANQUANT',str(exc),flush=True)

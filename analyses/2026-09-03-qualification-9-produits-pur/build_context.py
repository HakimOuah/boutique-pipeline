"""Exports locaux des observations ; aucune requête ni mutation distante."""
import csv,gzip,json,statistics,collections
from collect_dfs import ROOT

def save_csv(name, rows):
 with (ROOT/name).open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,lineterminator='\n',fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

trends=collections.defaultdict(list)
for pattern in ['40-*-trends*','41-*-trends*']:
 for f in sorted((ROOT/'raw').glob(pattern)):
  r=json.load(gzip.open(f,'rt'))['response']['tasks'][0]['result'][0];cid=f.name.split('-')[1]
  for i,kw in enumerate(r['keywords']):
   full=[x for x in r['items'][0]['data'] if x['date_to']<'2026-09-03']
   known=[x for x in full if x['values'][i] is not None];years={}
   for y in ['2022','2023','2024','2025']:
    yr=[x for x in full if x['date_from'].startswith(y)];valid=[x for x in yr if x['values'][i] is not None]
    q4=[x['values'][i] for x in valid if int(x['date_from'][5:7])>=10]
    avg=statistics.mean(x['values'][i] for x in valid) if valid else None
    coverage=len(valid)/len(yr) if yr else 0
    # Null = manquant, jamais un zéro. Pas de ratio publié sur une série clairsemée.
    years[y]={'coverage':round(coverage,3),'mean_known':round(avg,2) if avg is not None else None,
     'q4_vs_annual':round(statistics.mean(q4)/avg,2) if q4 and avg and coverage>=.8 and len(q4)>=10 else None}
   recent=[x for x in full if x['date_from']>='2025-09-01'];prior=[x for x in full if '2024-09-01'<=x['date_from']<'2025-09-01']
   a=[x['values'][i] for x in recent if x['values'][i] is not None];b=[x['values'][i] for x in prior if x['values'][i] is not None]
   ratio=round(statistics.mean(a)/statistics.mean(b),2) if a and b and statistics.mean(b)>0 and len(a)/len(recent)>=.8 and len(b)/len(prior)>=.8 else None
   trends[cid].append({'keyword':kw,'coverage_5y':round(len(known)/len(full),3),'years':years,
     'last12_vs_prior12':ratio,'raw':str(f.relative_to(ROOT)),'note':'Indices Google Trends par requête ; pas volumes ; nulls exclus, semaine incomplète exclue.'})
(ROOT/'trends-synthese.json').write_text(json.dumps(trends,ensure_ascii=False,indent=2)+'\n')
shopping=[];serps=[]
for f in sorted((ROOT/'raw').glob('51-shopping*')):
 r=json.load(gzip.open(f,'rt'))['response']['tasks'][0]['result'][0];cid=f.name.split('-')[-1].split('.')[0]
 for x in r['items']:
  if x['type']=='google_shopping_serp':shopping.append({'candidate_id':cid,'query':r['keyword'],'rank':x.get('rank_group'),'title':x.get('title'),'seller':x.get('seller'),'price':x.get('price'),'currency':x.get('currency'),'merchant_url':x.get('url'),'shopping_url':x.get('shopping_url'),'delivery_info':x.get('delivery_info'),'raw':str(f.relative_to(ROOT))})
for f in sorted((ROOT/'raw').glob('30-*-serp*')):
 r=json.load(gzip.open(f,'rt'))['response']['tasks'][0]['result'][0];cid=f.name.split('-')[1]
 for x in r['items']:serps.append({'candidate_id':cid,'query':r['keyword'],'type':x['type'],'rank':x.get('rank_group'),'domain':x.get('domain'),'title':x.get('title'),'url':x.get('url'),'raw':str(f.relative_to(ROOT))})
save_csv('shopping-360.csv',shopping);save_csv('serp.csv',serps)
actor_groups=collections.defaultdict(list)
for row in serps:
 if row['type']=='organic':actor_groups[(row['candidate_id'],row['query'])].append(row)
actor_rows=[]
market=['amazon.','temu.','cdiscount.','ebay.','leboncoin.','manomano.']
large=['decathlon.','fnac.','darty.','leroymerlin.','ikea.','boulanger.','castorama.','electrodepot.','conforama.','intersport.','gifi.','leclerc']
for (cid,q),rows in actor_groups.items():
 rows=sorted(rows,key=lambda r:int(r['rank']));counts={}
 for depth in [10,20]:
  sample=rows[:depth]
  counts.update({f'observed_{depth}':len(sample),f'marketplaces_{depth}':sum(any(m in (r['domain'] or '') for m in market) for r in sample),f'large_retailers_{depth}':sum(any(m in (r['domain'] or '') for m in large) for r in sample)})
 actor_rows.append({'candidate_id':cid,'query':q,**counts})
(ROOT/'serp-acteurs.json').write_text(json.dumps({'note':'Comptage positions, domaines répétés conservés. Enseignes multiservices séparées des marketplaces listées dans le script. Aucun pourcentage de clics/ventes. Les spécialistes indépendants ne sont pas des places automatiquement gagnables.','rows':actor_rows},ensure_ascii=False,indent=2)+'\n')
source_rows=[]
for f in sorted((ROOT/'sourcing').glob('*search*.json')):
 j=json.loads(f.read_text())
 for x in j['response'].get('result',{}).get('items',[]):
  source_rows.append({'candidate_id':f.name.split('-')[0],'query':j['request']['query'],'product_id':x['product_id'],'title':x['title'],'discovery_price':x.get('price'),'currency':x.get('currency'),'rating_discovery':x.get('rating'),'orders_discovery':x.get('orders'),'canonical_url':'https://www.aliexpress.com/item/'+x['product_id']+'.html','raw':str(f.relative_to(ROOT)),'observed_at_utc':j['observed_at_utc'],'confidence':'C — liste de découverte, pertinence non garantie'})
save_csv('sourcing-decouverte.csv',source_rows)
print('Exports',len(shopping),'prix Shopping,',len(serps),'éléments SERP,',len(source_rows),'lignes fournisseurs avec doublons')

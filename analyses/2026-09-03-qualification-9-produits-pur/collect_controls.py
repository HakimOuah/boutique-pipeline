import json
from collect_dfs import ROOT,call,witness

ANCHORS={
 'A1':['antivol vélo pliant','antivol vélo'],
 'A2':['appareil photo numérique vintage','appareil photo vintage'],
 'A5':['mini liseuse','liseuse epub'],
 'A6':['rasoir de sûreté','coffret rasage homme'],
 'B1':['étendoir mural pliable','étendoir mural'],
 'B2':['support vélo mural pivotant','support vélo mural'],
 'B3':['moustiquaire fenêtre sans perçage','moustiquaire fenêtre magnétique'],
 'C2':['casque tv sans fil','casque audio pour tv'],
 'C6':['poêle titane','poêle sans pfas'],
}
if __name__=='__main__':
 keys=list(json.loads((ROOT/'control-map.json').read_text()))
 for i in range(0,len(keys),900):
  call(f'20-controls-{i//900}','keywords_data/google_ads/search_volume/live',
    [{'keywords':keys[i:i+900],'location_name':'France','language_name':'French','search_partners':False}])
 witness('21-witness-after-controls')
 for cid,qs in ANCHORS.items():
  for i,q in enumerate(qs):
   call(f'30-{cid}-serp-{i}','serp/google/organic/live/advanced',
     [{'keyword':q,'location_name':'France','language_name':'French','device':'desktop','os':'windows','depth':20}])
  try:
   call(f'40-{cid}-trends','keywords_data/google_trends/explore/live',
    [{'keywords':qs,'location_name':'France','language_name':'French','time_range':'past_5_years','type':'web','item_types':['google_trends_graph']}])
  except Exception as exc:print('Trends MANQUANT',cid,str(exc),flush=True)
 witness('49-witness-after-context')

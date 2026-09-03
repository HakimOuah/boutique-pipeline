"""Consolidation conservatrice explicite ; les scénarios ne sont pas des intervalles statistiques."""
import collections,csv,gzip,json,pathlib,statistics
from build_keywords import ROOT,get_corpus,cle,sans_accent

def key(k):
 # Synonymes TV/télévision vérifiés dans les réponses des deux passes.
 return cle(sans_accent(k).lower().replace('television','tv').replace('murale','mural'))
def groups(rows):
 lexical=collections.defaultdict(list)
 for r in rows:lexical[key(r['keyword'])].append(r)
 result=[]
 for k,rr in lexical.items():
  known=[r for r in rr if r['volume'] is not None]
  chosen=max(known,key=lambda r:r['volume']) if known else rr[0]
  series=tuple((m['year'],m['month'],m.get('search_volume')) for m in sorted(chosen['series'],key=lambda m:(m['year'],m['month'])))
  result.append({'key':k,'keyword':chosen['keyword'],'volume':chosen['volume'],'cpc':chosen['cpc'],'series':series,'members':rr,'merge_reasons':['normalisation accents/pluriels/mots vides/ordre ; MAX']})
 merged=[]
 for g in sorted(result,key=lambda r:-(r['volume'] or 0)):
  vals=[m[2] for m in g['series']]
  match=None
  if len(vals)>=12 and len(set(vals))>=3:
   match=next((m for m in merged if m['volume']==g['volume'] and m['series']==g['series'] and set(m['key'].split()) & set(g['key'].split())),None)
  if match:
   match['members']+=g['members'];match['merge_reasons'].append('série datée 12 mois identique, non plate, volume identique et recouvrement lexical : '+g['keyword'])
  else:merged.append(g)
 for i,g in enumerate(merged):g['group_id']=f'G{i+1:04d}'
 return merged

def total(gs):return sum(g['volume'] or 0 for g in gs)
def export():
 corpus,coverage=get_corpus();out={};summaries={}
 for cid,rs in corpus.items():
  rr=list(rs.values())
  core=[r for r in rr if r['scope']=='core' and not r['branded']]
  conditional=[r for r in rr if r['scope']=='conditional' and not r['branded']]
  parent=[r for r in rr if r['scope']=='parent' and not r['branded']]
  bounded=[r for r in rr if r['scope'] in ('core','conditional')]
  brand=[r for r in bounded if r['branded']]
  core_g=groups(core);extended=groups(core+conditional);brand_g=groups(brand)
  out[cid]={'core':core_g,'core_plus_conditional':extended,'brand_comparable_corpus':brand_g,'parent_separate':groups(parent)}
  den=total(extended)+total(brand_g)
  cp=[g for g in core_g if g['cpc'] is not None and g['volume']]
  summaries[cid]={'keyword_rows':len(rr),'core_monthly':total(core_g),'core_plus_conditional_monthly':total(extended),
   'parent_separate_monthly':total(out[cid]['parent_separate']),'brand_comparable_monthly':total(brand_g),
   'generic_ratio_bounded_corpus':round(total(extended)/den,4) if den else None,
   'generic_ratio_note':'Corpus core + conditional après exclusions ; lexique marques documenté, non exhaustif ; aucun ratio de toute la catégorie.',
   'cpc_core_weighted_usd':round(sum(g['volume']*g['cpc'] for g in cp)/sum(g['volume'] for g in cp),4) if cp else None,
   'cpc_core_coverage':round(sum(g['volume'] for g in cp)/total(core_g),4) if total(core_g) else None,
   'unknown_volume_rows':sum(r['volume'] is None for r in rr),'is_exhaustive':False}
  p=ROOT/'mots-cles';p.mkdir(exist_ok=True)
  group_map={r['keyword']:g['group_id'] for g in extended for r in g['members']}
  core_map={r['keyword']:g['group_id'] for g in core_g for r in g['members']}
  with (p/(cid+'.csv')).open('w',newline='',encoding='utf-8-sig') as f:
   fields=['candidate_id','keyword','volume','cpc','currency','scope','branded','core_group_id','counted_core_volume','group_id','counted_volume','exclusion_or_condition','endpoint','observed_at_utc','source','monthly_searches_json']
   w=csv.DictWriter(f,lineterminator='\n',fieldnames=fields);w.writeheader()
   used=set();core_used=set()
   for r in sorted(rr,key=lambda r:-(r['volume'] or 0)):
    row={k:r.get(k) for k in fields};gid=group_map.get(r['keyword']);row['group_id']=gid
    row['counted_volume']=r['volume'] if gid and gid not in used else 0 if gid else None
    core_gid=core_map.get(r['keyword']);row['core_group_id']=core_gid
    row['counted_core_volume']=r['volume'] if core_gid and core_gid not in core_used else 0 if core_gid else None
    if core_gid:core_used.add(core_gid)
    if gid:used.add(gid)
    row['monthly_searches_json']=json.dumps(r['series'],ensure_ascii=False)
    w.writerow(row)
 for name,value in [('corpus',corpus),('groupes',out)]:
  with gzip.open(ROOT/(name+'.json.gz'),'wt',encoding='utf-8') as f:json.dump(value,f,ensure_ascii=False)
 (ROOT/'demande-synthese.json').write_text(json.dumps(summaries,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(summaries,ensure_ascii=False,indent=2))
if __name__=='__main__':export()

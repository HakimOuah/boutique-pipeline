"""Corpus, règles de périmètre et groupes auditables pour cette étude seulement."""
import csv, gzip, json, pathlib, re, sys, collections
ROOT=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[1]/'scripts'))
from kw_dfs import cle, sans_accent
OLD=ROOT.parent/'2026-09-03-test-decouverte-search-12'
COUPLED=ROOT.parent/'2026-09-03-test-decouverte-couplee'
IDS=['A1','A2','A5','A6','B1','B2','B3','C2','C6']
OLD_FILES={
 'A1':['02-A-discovery','04-A1-targeted'], 'A2':['02-A2-discovery','04-A2-targeted'],
 'A5':['02-A5-discovery','04-A5-targeted'],'A6':['02-A6-discovery','04-A6-targeted'],
 'B1':['04-B1-targeted'],'B2':['04-B2-targeted'],'B3':['04-B3-targeted'],
 'C2':['10-c2-labs','29-c2-refinement'],'C6':['42-c6-labs']}
BRANDS=r'\b(amazon|aliexpress|temu|cdiscount|decathlon|decath|intersport|leroy merlin|castorama|brico depot|ikea|lidl|aldi|action|gifi|boulanger|darty|fnac|leclerc|cultura|electro depot|carrefour|auchan|but|conforama|ikee?a|walmart|cora|boulanger|manomano|boulanger|sephora|nocibe|yves rocher|marionnaud|dior|chanel|rituals|nocibe|nocibé|loccitane|occitane|notino|nocibe|nocibé|vinted|leboncoin|ebay)\b'
SPECIFIC={
 'A1':r'\b(abus|bordo|kryptonite|trelock|elops|btwin|b twin|hiplok|litelok|auvray|oxford|master lock|onguard|zefal|zefal|kohlburg|foldylock|west biking|rockbros|etook|artago|axa|tex lock|radon|squire|giant|bontrager)\b',
 'A2':r'\b(sony|canon|nikon|fuji\w*|kodak|olympus|panasonic|lumix|leica|ricoh|pentax|polaroid|instax|samsung|casio|cyber\s?shot|powershot|coolpix|timelens|pikko|campsnap|camp snap|papershoot|paper shoot|digicam fx)\b',
 'A5':r'\b(kobo|kindle|amazon|vivlio|pocketbook|boox|fnacbook|paperwhite|xteink|inkpalm|nolim|sony|tolino|woxter|onyx|xiaomi|bookeen|inkbook)\b',
 'A6':r'\b(merkur|muhle|gillette|wilkinson|shavest|henson|lamier|yaqi|rockwell|parker|muh?le|edwin jagger|lamazuna|horace|barbarossa|pearl|rasozero|goodfellas|weishi|bambaw|king c|osma|proraso|plisson|man.?s?\s*beard|nivea|cella|pil\w*|philips|braun|loccitane)\b',
 'B1':r'\b(foxydry|brabantia|leifheit|telegant|vileda|gimi|wenko|kroms|artweger|wallfix|ville?da|hills|bricozor|todeco|homidec|vidaxl|songmics|rayen)\b',
 'B2':r'\b(steadyrack|cyclmania|mot?tez|peruzzo|thule|prostor|topeak|feedback|hornit|clug|delta|b twin|btwin|feedback|bike original|bikelift|xlc|bikestow)\b',
 'B3':r'\b(tesa|windhager|schellenberg|av?osdim|jarolift|cmarl|empasa|bruynzeel|artens|livarno|pliseo|fakro|velux)\b',
 'C2':r'\b(avantree|sennheiser|sony|philips|bose|jbl|thomson|cgv|meliconi|simolio|audika|amplifon|samsung|lg|panasonic|tcl|hisense|siemens|muse|linkster|metronic|geemarc|senheiser|sennheisser|senheiser|thompson|audioline|akg|jvc|logitech|yamaha)\b',
 'C6':r'\b(titanox|titane x|tefal|titanium pro|everest|onox|titanova|sitram|lagostina|de buyer|debuyer|cristel|zwilling|wmf|fissler|berghoff|greenpan|hexclad|beka|snow peak|keith|boundless|le creuset|titanpan|titaniumx|titanex)\b'}

def classify(cid,keyword):
 k=sans_accent(keyword).lower().replace('’',"'")
 # Classes de diagnostic, jamais états canoniques du pipeline.
 if cid=='A1':
  if re.search(r'\b(batterie|selle|roue|chaine|cable|alarme|cadre|gps|trottinette|moto|u|menotte|souple|textile)\b',k): c,why='incompatible','autre format ou composant que le pliant'
  elif re.search(r'pliant|pliable|articule|repliable',k):c,why='core','format pliant explicite'
  else:c,why='parent','antivol vélo général, format non prouvé'
 elif cid=='A2':
  if re.search(r'argentique|pellicule|jetable|instantane|reflex|lego|occasion|reconditionn|location|reparation|appareil photo ancien|dessin|fisher.?price|jouet|tatou|coloriage|vector|png|clipart|deco|poster|fond d.ecran|coque',k):c,why='incompatible','autre technologie, occasion ou service'
  elif re.search(r'vintage|retro|digicam',k):
   if re.search(r'numerique|digital|effet|style',k):c,why='core','numérique/rendu rétro explicite'
   else:c,why='conditional','vintage/digicam ambigu neuf, occasion ou argentique'
  else:c,why='parent','photographie ou compact général'
 elif cid=='A5':
  if re.search(r'lampe|lampadaire|eclairage|sculpture|windows|en ligne|logiciel|application|android|iphone|ipad|ordinateur|gratuite?|telecharg|liseuse lit|pochette|housse|etui|couture|led|patron',k):c,why='incompatible','lampe, logiciel, contenu ou sens non appareil'
  elif re.search(r'mini|poche|petite|compacte',k):c,why='core','petit appareil explicitement recherché'
  elif 'epub' in k:c,why='conditional','format EPUB mais taille et DRM à confirmer'
  else:c,why='parent','liseuse générale, mini-format non demandé'
 elif cid=='A6':
  if re.search(r'lame|etui|support|tete|peigne ouvert|apres.?rasage|electrique|coupe.?chou|shavette|tondeuse|blaireau seul|savon seul|intime|pubi|femme|jambes|ado|adolescent|francais|france|allemand|ancien',k):c,why='incompatible','accessoire, autre public/format ou provenance non prouvée'
  elif re.search(r'rasoir.*suret|rasoir.*securit|suret.*rasoir|securit.*rasoir',k):c,why='core','rasoir de sûreté/sécurité homme ou non genré'
  elif re.search(r'coffret|kit|set|traditionnel',k):c,why='conditional','ensemble ou traditionnel, composition à confirmer en SERP'
  else:c,why='parent','rasage non spécifique'
 elif cid=='B1':
  if re.search(r'plafond|chauff|electri|fil a|corde|enrouleur|parapluie|tancarville.*sol|exterieur|bois|radiateur|fenetre|balcon.*sans|sans perc|sans trou|bricol|fabriqu|equerre|fixation',k):c,why='incompatible','autre mécanisme/matière, extérieur ou composant non promis'
  elif 'mural' in k or 'rabattable' in k:c,why='core','étendoir mural intérieur repliable'
  else:c,why='parent','séchage général ou autre format'
 elif cid=='B2':
  if re.search(r'voiture|attelage|remorque|plafond|sol|camping|telephone|tablette|reparation|atelier|bois|horizontal|cadre|decoration|decoratif|sans percage|sans trou|électrique',k):c,why='incompatible','transport, autre support ou usage incompatible'
  elif 'pivot' in k or 'orientable' in k:c,why='core','pivot explicitement demandé'
  elif 'mural' in k or 'mur' in k or 'vertical' in k:c,why='conditional','rangement mural, arbitrage crochet/pivot et capacité'
  else:c,why='parent','rangement général, support non déterminé'
 elif cid=='B3':
  if re.search(r'porte|baie|enroul|couliss|pliss|toit|camping|lit|berceau|aimant.*rideau|exterieur',k):c,why='incompatible','porte, baie ou mécanisme différent du cadre fenêtre'
  elif re.search(r'aimants? (pour )?moustiquaire|rouleau|bande|ruban',k):c,why='incompatible','accessoire ou consommable'
  elif re.search(r'sur mesure',k):c,why='conditional','fabrication sur mesure distincte du kit à recouper'
  elif 'fenetre' in k and re.search(r'sans perc|magnet|aimant',k) or 'cadre fixe sans' in k or 'cadre aimant' in k:c,why='core','fenêtre sans perçage / cadre magnétique compatible sous dimensions'
  else:c,why='parent','moustiquaire générique, format non garanti'
 elif cid=='C2':
  if not re.search(r'\btv\b|television|tele\b|télé',k):c,why='parent','audio général'
  elif re.search(r'filaire|avec fil|fil long|realite|virtuel|conduction|infra.?rouge|wifi|wi fi|malentendant|amplificat|stethoscop|intra|auditif|adaptateur|emetteur|transmetteur|rallonge',k):c,why='incompatible','autre technologie, accessoire ou besoin auditif spécifique'
  elif re.search(r'sans fil|bluetooth',k):c,why='core','casque TV sans fil compatible avec kit émetteur'
  else:c,why='parent','casque TV générique, filaire et sans fil mélangés'
 elif cid=='C6':
  if re.search(r'revetement|inox|ceramique|fonte|aluminium|cuivre|france|francais|inoxydable|camping|randonnee|bivouac',k):c,why='incompatible','autre matière, revêtement ou usage que cuisson domestique titane'
  elif 'titane' in k:c,why='core','poêle titane, composition à prouver'
  else:c,why='parent','absence de PFAS/Téflon ne désigne pas le titane'
 else:raise ValueError(cid)
 # Révision manuelle de la totalité des groupes comptés, après lecture des SERP.
 # Ces exclusions sont propres à l'offre évaluée, pas des règles universelles.
 if cid=='A6' and re.search(r'crane|papillon|reglable|maillot|suisse|avion|forum|avantage|c.est quoi',k):
  c,why='incompatible','format, public, pays ou intention hors kit débutant fixe'
 if cid=='A6' and c=='core' and 'laiton' in k:
  c,why='conditional','matière laiton non garantie par le kit'
 if cid=='A5' and 'livre de poche' in k:
  c,why='incompatible','lecture de livre papier ; accessoire lumineux possible'
 if cid=='C6':
  if re.search(r'poele a bois|tente|popote|alliage',k):
   c,why='incompatible','chauffage, camping ou alliage distinct du positionnement'
  elif re.search(r'toxicit',k):
   c,why='information','question de toxicité, hors achat direct'
  elif 'manche amovible' in k:
   c,why='conditional','mécanisme non garanti par le SKU'
 if cid=='B1':
  if re.search(r'porte sechoir|barre.*mural|bras pour|cheveux|vaisselle|maroc|slimy|balcon',k):
   c,why='incompatible','accessoire, autre usage, géographie ou mécanisme'
  elif c=='core' and re.search(r'retract|serviette',k):
   c,why='conditional','cordes rétractables ou porte-serviettes possibles ; mécanisme non déterminé'
 if cid=='B3':
  if 'sur mesure' in k and not ('fenetre' in k and re.search(r'sans perc|magnet|aimant',k)):
   c,why='parent','sur mesure non spécifique au cadre magnétique fenêtre'
  elif c=='core' and re.search(r'extensible|store|aluminium',k):
   c,why='conditional','mécanisme ou matière à rapprocher du SKU exact'
 if cid=='C2' and c=='core' and re.search(r'\bduo\b|double|2 casques|deux|2 personnes|\busb\b',k):
  c,why='conditional','double casque ou entrée audio USB non confirmée pour le kit simple'
 if cid=='C2' and re.search(r'casque.*sans fil.*avec (emetteur|transmetteur)',k):
  c,why='core','kit complet casque avec émetteur ; ne pas confondre avec émetteur seul'
 extra_brand=(cid=='B1' and re.search(r'arit|karim|arredamenti|grundtal|skippy|sauvic|rollfix|python',k)) or (cid=='B3' and 'centrakor' in k) or (cid=='C2' and re.search(r'electrodepot|les numeriques|orange|la source',k))
 extra_brand=extra_brand or (cid=='A1' and re.search(r'michelin|evolution 790|sherlock|maxxus|wayscral|crivit',k)) or (cid=='C6' and re.search(r'tipanexi|hestan|toaks|our place|rossetto|laguiole',k))
 brand=bool(re.search(BRANDS,k) or re.search(SPECIFIC[cid],k) or extra_brand)
 if re.search(r'comment|notice|mode d.emploi|nettoy|entretien|utilis|danger|sante|cancer|toxiqu|risque|fabriqu|tuto|branch|connect|repar|panne|fonctionne|probleme|remplac|perdu|ouvrir|debloqu',k):
  if not (cid=='C6' and 'sans' in k and 'toxiqu' in k):return 'information',brand,'usage/SAV/risque, hors demande achat directe'
 return c,brand,why

def get_corpus():
 allrows={cid:{} for cid in IDS};coverage=[]
 for cid in IDS:
  base=COUPLED/'raw' if cid.startswith('C') else OLD
  paths=[base/(s+'.json.gz') for s in OLD_FILES[cid]]+sorted((ROOT/'raw').glob('10-'+cid+'-labs-*.gz'))
  for path in paths:
   j=json.load(gzip.open(path,'rt'));resp=j['response'];date=j.get('observed_at_utc',j.get('retrieved_at_utc'))
   for task in resp['tasks']:
    for r in task.get('result') or []:
     items=r.get('items') or []
     coverage.append({'candidate_id':cid,'seed':j['payload'][0]['keyword'],'rows':len(items),'total_count':r.get('total_count'),'raw':str(path.relative_to(ROOT.parent)),'observed_at_utc':date})
     for x in items:
      k=x['keyword']; info=x.get('keyword_info') or {}
      row={'candidate_id':cid,'keyword':k,'volume':info.get('search_volume'),'cpc':info.get('cpc'),'currency':'USD_DOCUMENTED','series':info.get('monthly_searches') or [],'source':str(path.relative_to(ROOT.parent)),'observed_at_utc':date,'endpoint':j['endpoint'],'source_priority':1,'intent_api':(x.get('search_intent_info') or {}).get('main_intent')}
      old=allrows[cid].get(k)
      if old is None or date>old['observed_at_utc']:allrows[cid][k]=row
 # Contrôles antérieurs (même jour), puis nouveaux contrôles : priorité à Google Ads live.
 controls=[OLD/'05-live-volume-controls.json.gz',COUPLED/'raw/22-first-controls.json.gz',COUPLED/'raw/43-c6-controls.json.gz']+sorted((ROOT/'raw').glob('20-controls-*.gz'))
 oldmap=json.loads((OLD/'control-keywords.json').read_text())
 for path in controls:
  j=json.load(gzip.open(path,'rt'));date=j.get('observed_at_utc',j.get('retrieved_at_utc'))
  for t in j['response']['tasks']:
   for x in t.get('result') or []:
    k=x['keyword']
    for cid,rows in allrows.items():
     if k in rows or k in oldmap.get(cid,[]) or (path.name.startswith('20-') and cid in CONTROL_MAP.get(k,[])):
      old=rows.get(k)
      if old is None or old['source_priority']==1 or date>old['observed_at_utc']:
       rows[k]={'candidate_id':cid,'keyword':k,'volume':x.get('search_volume'),'cpc':x.get('cpc'),'currency':'USD_DOCUMENTED','series':x.get('monthly_searches') or [],'source':str(path.relative_to(ROOT.parent)),'observed_at_utc':date,'endpoint':j['endpoint'],'source_priority':2,'intent_api':None}
 for cid,rows in allrows.items():
  for k,r in rows.items():
   r['scope'],r['branded'],r['exclusion_or_condition']=classify(cid,k)
   r['normalization_key']=cle(k)
 return allrows,coverage

CONTROL_MAP=json.loads((ROOT/'control-map.json').read_text()) if (ROOT/'control-map.json').exists() else {}
if __name__=='__main__':
 allrows,coverage=get_corpus()
 with gzip.open(ROOT/'corpus.json.gz','wt',encoding='utf-8') as f:json.dump(allrows,f,ensure_ascii=False)
 (ROOT/'coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
 if '--plan' in sys.argv:
  mapping={}
  for cid,rows in allrows.items():
   for k,r in rows.items():
    if r['scope'] in ('core','conditional') or (r['volume'] or 0)>=1000:
     mapping.setdefault(k,[]).append(cid)
  (ROOT/'control-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
  print('planned_controls',len(mapping))
 for cid,rows in allrows.items():print(cid,len(rows),dict(collections.Counter(r['scope'] for r in rows.values())))

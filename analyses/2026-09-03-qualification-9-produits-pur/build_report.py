"""Rend les dossiers et scénarios locaux à partir des observations et jugements explicites."""
import csv,gzip,json,statistics,collections
from collect_dfs import ROOT
from editorial import DATA

def write(name,text):
 # Rectification de lecture de cette étude, sans remplacer les mesures du 03/09.
 if name in ['README.md','dossiers/A6.md','dossiers/B1.md']:
  ref=('../' if name=='README.md' else '../../')+'2026-09-04-audit-ecarts-volumes/README.md'
  note=f"> **Complément du 04/09 :** [comparaison des captures SEMrush et des réponses DataForSEO]({ref}). Sans accents, les ordres de grandeur de l'étendoir se rapprochent ; la priorité de recherche reste en REVIEW. Les 13 180 d'A6 désignent les rasoirs de sûreté, pas la demande explicite de kits à 99 €. Les totaux ci-dessous restent les estimations du 03/09, pas de nouvelles mesures validées."
  first,rest=text.strip().split('\n',1);text=first+'\n\n'+note+'\n'+rest
 (ROOT/name).write_text(text.strip()+'\n',encoding='utf-8')
def num(x,dec=0):return 'MANQUANT' if x is None else f'{x:,.{dec}f}'.replace(',',' ').replace('.',',')
def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(str(v).replace('|',' / ').replace('\n',' ') for v in r)+' |' for r in rows])
def evidence(name):
 if name in ('A6-lamier','A6-lamier-retours'):
  return '[Source exclue du benchmark officiel — correction du 04/09](../../2026-09-04-approfondissement-rasoir-surete/README.md)'
 if name=='shopping':return '[Sonde 40 prix par candidat](../shopping-360.csv)'
 cap=json.loads((ROOT/'concurrence/raw'/name/'capture.json').read_text())
 return f"[Page marchande]({cap['requested_url']}) · [capture](../concurrence/raw/{name}/page.txt)"

demand=json.loads((ROOT/'demande-synthese.json').read_text())
groups=json.load(gzip.open(ROOT/'groupes.json.gz','rt'))
fx=json.loads((ROOT/'fx.json').read_text())
trends=json.loads((ROOT/'trends-synthese.json').read_text())
serps=list(csv.DictReader((ROOT/'serp.csv').open(encoding='utf-8-sig')))
actors=json.loads((ROOT/'serp-acteurs.json').read_text())['rows']
ledger=json.loads((ROOT/'api-ledger.json').read_text());cost=sum(x['cost_usd'] for x in ledger)
old={x['id']:x for x in json.loads((ROOT.parent/'2026-09-03-test-decouverte-search-12/results.json').read_text())}
results=[];econ_rows=[];comparison=[]
(ROOT/'dossiers').mkdir(exist_ok=True)
for cid,d in DATA.items():
 s=demand[cid];cpc=s['cpc_core_weighted_usd']/fx['USD_per_EUR'];price=d['price']
 scenarios=[]
 prices=[price]+({'A5':[99],'B1':[59.9],'B2':[59.9],'C2':[59.9]}.get(cid,[]))
 for selling in prices:
  net=selling/1.2;fees=selling*.02+.30;reserve=selling*.05
  for mult in [1,1.5]:
   for cvr in [.01,.015,.02,.03]:
    expected_cpa=cpc*mult/cvr;max_landed=net-fees-reserve-expected_cpa
    scenarios.append({'candidate_id':cid,'selling_price_ttc_hypothesis':selling,'net_revenue_vat20_scenario':round(net,4),
     'payment_fees_2pct_plus_030_hypothesis':round(fees,4),'returns_sav_reserve_5pct_hypothesis':round(reserve,4),
     'cpc_eur_proxy':round(cpc,6),'cpc_stress_multiplier':mult,'cvr_hypothesis':cvr,'expected_cpa_scenario':round(expected_cpa,4),
     'max_product_plus_shipping_eur':round(max_landed,4),'status':'HYPOTHESE — seuil de coût, pas devis ni CVR prévue'})
 econ_rows+=scenarios
 a5=None
 if cid=='A5':
  a5=[]
  for selling in [79,99]:
   margin=selling/1.2-58.99-.83-(selling*.02+.30)-selling*.05
   a5.append({'selling_price_hypothesis':selling,'product_cost_cash_eur':58.99,'shipping_cost_eur':.83,'contribution_margin_before_ads_scenario':round(margin,4),'break_even_cpa_scenario':round(margin,4),'break_even_cvr_scenario':cpc/margin if margin>0 else None,'supplier_vat_recovery':'Hypothèse prudente : non récupérée ; aucune facture/traitement IOSS validé','evidence':'sourcing/A5-exact-X3-black.json'})
 # Capacité à passer au volume dépend aussi de l'offre : une somme n'est pas un PASS.
 result={'candidate_id':cid,'mode':'PRODUIT PUR','product':d['name'],'prequalification_status':d['prequalification'],'technical_recommendation':d['technical'],
  'priority':d['priority'],'decision_scope':'Offre et corpus sondés, France, Q4 2026 ; pas tout le marché parent',
  'reason':d['conclusion'],'addressable_search_demand':{'core_proxy_monthly':s['core_monthly'],'core_plus_conditional_scenario':s['core_plus_conditional_monthly'],'is_exhaustive':False,'source':'mots-cles/'+cid+'.csv','residual_bucket_overlap':'Non éliminable totalement par API ; proximité du seuil garde REVIEW'},
  'generic_search_ratio':{'value':s['generic_ratio_bounded_corpus'],'scope':s['generic_ratio_note']},
  'keywordability':{'score':None,'assessment':d['offer']},'serp_winnability':{'score':None,'assessment':d['competition']},
  'search_score':None,'business_score':None,'shopping_score':None,'numeric_score_reason':'Barèmes séparés non opérationnalisés pour cette expérience, données fournisseurs incomplètes ; pas de score inventé.',
  'economics':{'selling_price':None,'selling_price_hypothesis':price,'COGS':58.99 if cid=='A5' else None,'shipping_cost':.83 if cid=='A5' else None,
   'payment_fees':None,'estimated_cpc_usd_proxy':s['cpc_core_weighted_usd'],'estimated_cpc_eur_proxy':round(cpc,6),'fx':fx,
   'contribution_margin_before_ads':None,'break_even_cpa':None,'break_even_cvr':None,'scenarios':scenarios,'exact_supplier_scenarios':a5},
  'supplier_status':'SKU_FR_API_B' if cid=='A5' else 'MANQUANT_POUR_OFFRE_EXACTE','supplier_ids_reviewed':d['supplier_ids'],
  'google_trends':trends[cid],'actual_cpc':None,'actual_cvr':None,'expected_cpa':None,'actual_cpa':None,'CTR':None,'ATC':None,'checkout':None,'sales':None,'ROAS':None,
  'sample_status':'NON_COMMANDE','gmc_readiness':'NON_EVALUABLE_AVANT_OFFRE_ET_BOUTIQUE','hakim_decision':None,'go_final':False,'next_evidence':d['reopen']}
 if cid in ['A6','B1']:
  result['cross_check_2026_09_04']={'source':'../2026-09-04-audit-ecarts-volumes/README.md','new_live_product_volumes':False,'volume_validated_for_gate':False,'note':'Semrush sans accents corroborant partiellement B1 ; 13 180 A6 concerne les rasoirs et non le kit. Statut REVIEW maintenu, aucune promotion.'}
 results.append(result)
 core=[g for g in groups[cid]['core'] if g['volume'] is not None]
 kwtable=table(['Groupe représentatif (MAX)','Volume mensuel','CPC USD'],[(g['keyword'],num(g['volume']),num(g['cpc'],2)) for g in core[:16]])
 prices_table=table(['Concurrent / offre','Prix observé','Portée','Preuve'],[(a,b,n,evidence(ref)) for a,b,ref,n in d['prices']])
 comparison += [{'candidate_id':cid,'competitor':a,'price_observed':b,'scope':n,'source':ref} for a,b,ref,n in d['prices']]
 econ_table=table(['CVR hypothétique','CPA scénario','Coût produit + port maximal'],[(num(x['cvr_hypothesis']*100,1)+' %',num(x['expected_cpa_scenario'],2)+' €',num(x['max_product_plus_shipping_eur'],2)+' €') for x in scenarios if x['selling_price_ttc_hypothesis']==price and x['cpc_stress_multiplier']==1])
 q4=[m[2] for m in core[0]['series'] if m[0]==2025 and m[1] in [10,11,12]] if core else []
 ms=[m[2] for m in core[0]['series'] if m[2] is not None] if core else []
 monthly=f"Proxy saison Google Ads de la tête « {core[0]['keyword']} » : moyenne Q4 2025 {num(statistics.mean(q4))}, moyenne des {len(ms)} mois présents {num(statistics.mean(ms))}, ratio {num(statistics.mean(q4)/statistics.mean(ms),2)}. Série datée dans le CSV ; ce ratio n'est pas une prévision Q4 2026." if len(q4)==3 and ms else 'Saison Google Ads non concluante.'
 origin=(f"[Test initial A/B](../../2026-09-03-test-decouverte-search-12/dossiers.md) : {old[cid]['risk']}" if cid in old else '[Test couplé C](../../2026-09-03-test-decouverte-couplee/README.md) : signal de découverte daté du 03/09, sans rentabilité ni attribution des ventes démontrées.')
 organic=[x for x in serps if x['candidate_id']==cid and x['type']=='organic'];byq=collections.defaultdict(list)
 for x in organic:byq[x['query']].append(x)
 serp_text=[]
 for query,rows in byq.items():
  top=sorted(rows,key=lambda r:int(r['rank']))[:10]
  serp_text.append('**'+query+'** : '+', '.join(f"{x['rank']}. {x['domain']}" for x in top)+'.')
 for row in actors:
  if row['candidate_id']==cid:
   serp_text.append(f"Sur « {row['query']} » : marketplaces {row['marketplaces_10']}/10 et {row['marketplaces_20']}/{row['observed_20']} résultats organiques effectivement reçus ; grandes enseignes séparées {row['large_retailers_10']}/10 et {row['large_retailers_20']}/{row['observed_20']}. [Convention de comptage](../serp-acteurs.json).")
 a5text=''
 if a5:
  a5text='\n\n**Source exacte A5, avec hypothèses du modèle :**\n\n'+table(['Vente hypothétique','Produit + port observés','Contribution avant Ads scénario','BE-CVR scénario'],[(num(x['selling_price_hypothesis'],2)+' €','59,82 €',num(x['contribution_margin_before_ads_scenario'],2)+' €',num(x['break_even_cvr_scenario']*100,2)+' %' if x['break_even_cvr_scenario'] else 'non finie') for x in a5])+'\n\nLa récupération éventuelle de TVA fournisseur n’est pas validée. Ce calcul prudent utilise le débours intégral ; il ne prétend pas fixer la fiscalité réelle.'
 source_links=' · '.join(f'[AliExpress {pid}](https://www.aliexpress.com/item/{pid}.html)' for pid in d['supplier_ids']) or 'Aucun identifiant correspondant suffisamment à cette offre.'
 text=f'''# {cid} — {d['name']}

Date des observations : 03/09/2026. Mode **PRODUIT PUR / Search**.

**{d['prequalification']} — {d['technical']}**. {d['conclusion']}

## Offre et origine

{d['offer']}

{origin}

## Demande France et mots-clés

**Cœur nettoyé du corpus : {num(s['core_monthly'])}/mois.** Scénario cœur + intentions conditionnelles : **{num(s['core_plus_conditional_monthly'])}/mois**, à ne pas utiliser comme volume validé. Référence canonique inchangée : 12 500. Ces nombres sont des proxies de buckets, pas des utilisateurs uniques ni des bornes statistiques.

{d['demand']}

{kwtable}

**[Tous les {s['keyword_rows']} mots-clés collectés, volumes, exclusions, séries et provenance](../mots-cles/{cid}.csv).** {s['unknown_volume_rows']} volumes non renseignés restent vides. Les parents et exclusions sont conservés pour audit, jamais additionnés au gate. [Méthode et limites](../METHODE.md).

Part générique diagnostique du corpus comparable : **{num(s['generic_ratio_bounded_corpus']*100,1)} %**, calculée après exclusions et consolidation. Lexique de marques non exhaustif ; ce n'est pas une part du marché national ni une mesure de ventes. Une marque de TV compatible et une marque de casque exigée ne doivent pas être interprétées identiquement.

## SERP, offre concurrente et droit de gagner

{d['competition']}

{chr(10).join(serp_text)}

Deux captures desktop de 20 résultats demandés, prises le même jour ; détail dans [serp.csv](../serp.csv). Aucun élément `paid` retourné sur ces captures : la densité réelle d'annonces Search reste **MANQUANT**, pas zéro. Les modules produits et la sonde Shopping ne prouvent pas des campagnes Search rentables.

{prices_table}

Sonde complémentaire : **40 cartes Shopping** pour ce candidat, conservées dans [shopping-360.csv](../shopping-360.csv). Échantillon brut : plusieurs mécanismes, vendeurs et variantes ; pas de médiane faussement comparable ni de prix livré supposé. Les stocks et promotions restent ponctuels. L'écart carte/PDP est conservé, pas arbitré en faveur du prix le plus séduisant.

**Différenciation proposée — HYPOTHÈSE :** {d['angle']}

## Fournisseurs et logistique

{d['source']}

{source_links}

[Réponses API sources](../sourcing/) · [Export de découverte](../sourcing-decouverte.csv). Les prix de liste ne sont pas des coûts rendus. Un entrepôt UE, une livraison, une note produit et un stock ne sont prouvés que lorsqu'ils sont présents sur le SKU exact. Le navigateur a refusé les PDP AliExpress par politique de sécurité ; aucune preuve visuelle de niveau A n'a été obtenue. Les contrôles structurés passent par la passerelle API en lecture seule déjà utilisée. Aucun contournement, achat, message fournisseur ou import DSers.

**À vérifier avant sélection :** {d['checks']}

## Économie de commande

Prix de travail **{num(price,2)} € TTC — HYPOTHÈSE**, ancré sur la concurrence. CPC pondéré par les volumes des groupes cœur : **{num(s['cpc_core_weighted_usd'],3)} USD**, soit **{num(cpc,3)} €** au change BCE du 03/09 (1 EUR = {fx['USD_per_EUR']} USD). Couverture CPC du cœur : {num(s['cpc_core_coverage']*100,1)} %. Ce CPC DataForSEO n'est pas le CPC d'une campagne OH Ventures.

Hypothèses de simulation : revenu net après TVA à 20 %, frais de paiement 2 % + 0,30 €, provision retours/SAV 5 % du TTC. Aucun de ces paramètres n'est présenté comme une facture, un régime fiscal ou un taux de retours observé. Les coûts fixes et le profit cible ne sont pas couverts par le seuil d'équilibre.

{econ_table}

Le plafond désigne **produit + expédition**, après les frais/provisions ci-dessus. Il faut viser en dessous pour absorber frais fixes, erreurs et profit. [Toutes les sensibilités](../economics.csv), dont CPC ×1,5 et prix alternatifs. CVR 1/1,5/2/3 % = scénarios, aucun seuil canonique ajouté.

{d['economy']}{a5text}

`contribution_margin_before_ads`, `break_even_cpa` et `break_even_cvr` réels restent **MANQUANT** tant que vente et coûts réels ne sont pas validés. Formules : contribution = revenu net − tous coûts variables hors Ads ; CPA d'équilibre = contribution ; CVR d'équilibre = CPC / contribution si contribution > 0.

## Saison et Q4

{d['season']}

{monthly}

[Données Trends, couverture et séries](../trends-synthese.json). Les requêtes lacunaires n'ont pas de ratio de croissance retenu ; les nulls restent manquants. Le seuil de couverture de 80 % sert seulement à empêcher un calcul descriptif sur quelques valeurs, pas à créer un nouveau gate produit.

## Décision et preuve suivante

{d['reopen']}

Search Score / Business Score / Shopping Score : **non calculés**. Les barèmes séparés n'ont pas été opérationnalisés dans cette expérience ; aucun score artificiel ne compense un gate manquant. La priorité indiquée est un jugement de recherche, pas un score ni une probabilité de réussite.

**GO_FINAL : aucune décision Hakim enregistrée. Sample : non commandé. Search : non testé.** CTR, CPC/CPA/CVR réels, ATC, checkout, ventes et ROAS : MANQUANT. GMC : audit boutique/feed non applicable à ce stade ; aucune validation GMC implicite.
'''
 write('dossiers/'+cid+'.md',text)
write('results.json',json.dumps(results,ensure_ascii=False,indent=2))
with (ROOT/'economics.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,lineterminator='\n',fieldnames=list(econ_rows[0]));w.writeheader();w.writerows(econ_rows)
with (ROOT/'concurrence/matrice.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,lineterminator='\n',fieldnames=list(comparison[0]));w.writeheader();w.writerows(comparison)
summary=table(['Produit','Cœur / mois','+ conditionnels (non validé)','Décision technique','Suite'],[(f"[{cid} — {d['name']}](dossiers/{cid}.md)",num(demand[cid]['core_monthly']),num(demand[cid]['core_plus_conditional_monthly']),d['technical'],('Priorité '+str(d['priority']) if d['priority'] in [1,2] else 'Réserve' if d['priority'] else 'Arrêt de cette thèse')) for cid,d in DATA.items()])
write('README.md',f'''# Qualification des neuf PRODUITS PURS — 03/09/2026

**Deux pistes à poursuivre en priorité : étendoir mural et kit de rasage. Deux réserves : support vélo pivotant et casque TV. Cinq thèses à arrêter. Aucun candidat prêt à lancer.**

Demande Hakim : analyse approfondie des neuf candidats non STOP des deux tests de découverte, jusqu'à la concurrence, au sourcing et à l'économie. Cette étude n'implémente pas la nouvelle architecture. Elle conserve le modèle PRODUIT PUR Search, le seuil de 12 500, les règles UNIVERS et le vocabulaire canonique.

## Résultats

{summary}

Les quatre pistes conservées restent `REVIEW_PREQUALIFICATION`. Les cinq autres deviennent `STOP_PREQUALIFICATION`, limité à l'offre étudiée. **0 PASS_PREQUALIFICATION, 0 TECHNICAL_PASS, aucun GO_FINAL.** Le total conditionnel n'est jamais un total accepté. Le cœur est un proxy nettoyé et non une audience unique ; près du seuil, les chevauchements résiduels et la compatibilité produit imposent de garder REVIEW.

1. **B1 — Étendoir mural** : meilleur rapport apparent demande/CPC. Un prix autour de 79 € peut fonctionner arithmétiquement, mais il doit se défendre contre des offres à 40–60 € et financer le fret. Fournisseur correspondant au produit encore manquant.
2. **A6 — Kit rasage débutant** : fit Search clair, kits à 99 € réellement observés. Le cœur est seulement un peu au-dessus du seuil. Le montage fournisseur exploré ne prouve ni un kit débutant adapté ni une marge suffisante. Google Trends 5 ans reste lacunaire.
3. **B2 — Support pivotant** : dépend presque entièrement d'un accès au parent mural. Les pivots simples à 15–30 € empêchent de supposer un prix premium sans autre mécanisme.
4. **C2 — Casque TV** : problème clair, CPC modéré et saison Q4 confirmée. Volume du kit simple encore sous le seuil et concurrence CGV/Meliconi déjà bien équipée. Réserve pour preuve produit/compatibilité.

Les arrêts sont motivés dans chaque dossier : **A1** faible demande pliant et confiance marques ; **A2** intention vintage mélangée et CPC élevé ; **A5** mini-format étroit et source presque au prix fabricant ; **B3** ticket/marge et saison Q4 défavorables ; **C6** volume, CPC et preuve matière insuffisants.

## Livrables et portée réelle

- [Neuf dossiers](dossiers/) : mots-clés cœur, concurrence, prix, angle proposé, sourcing, économie et conditions de reprise.
- [Tous les mots-clés collectés](mots-cles/) : **{sum(s['keyword_rows'] for s in demand.values()):,} lignes candidat/mot-clé**, avec volumes disponibles, exclusions, déduplication et provenance. Un corpus fini n'est pas « tous les mots-clés de Google ».
- [360 cartes Shopping](shopping-360.csv), [18 SERP](serp.csv), [comparables commentés](concurrence/matrice.csv), captures marchandes datées.
- [Économie et sensibilités](economics.csv) : coût livré admissible, CPA par scénario et stress CPC ; [méthode](METHODE.md).
- [Sourcing](SOURCING.md) : offres retenues pour inspection, faux comparables, exact SKU et limites d'accès.
- [Résultats structurés](results.json), [Trends et couverture](trends-synthese.json), [contrôle qualité](QUALITE.md).

**Coût DataForSEO de cette passe : {cost:.5f} USD**, hors passes historiques réutilisées, infrastructure et tokens agent. [Journal des appels](api-ledger.json). Plafond du protocole : 10 USD. Témoins `tufting` à 12 100 avant/après ; les montants ne sont pas des dépenses publicitaires.

## Ce que ce test apprend à la méthode

Le couplage TrendTrack ↔ demande reste utile pour découvrir et interpréter une offre. La mesure approfondie doit ensuite dissocier le succès apparent du shop, la demande spécifique et la possibilité de la servir à un prix rentable. Un trafic ou un nombre d'annonces en hausse indique une activité commerciale ; il ne prouve pas le profit ni la vente de cette référence.

La créativité doit être plus libre à l'entrée, puis **la sévérité doit porter sur les preuves** : ne pas ajouter un parent pour sauver le volume ; ne pas emprunter le prix d'un premium pour un crochet simple ; ne pas valoriser un accessoire comme source du produit complet. Une donnée manquante garde REVIEW lorsque la thèse reste plausible ; elle ne mérite pas une note zéro.

Il serait trop sévère d'arrêter B1 uniquement parce que la recherche AliExpress renvoie mal les résultats. Il serait trop permissif de lancer B1 parce que son CPC est faible. La prochaine action utile est une preuve fournisseur exacte, pas davantage de nouveaux scores.

Les 12 500 restent la règle actuelle. Cette petite étude ne justifie ni de baisser ce seuil, ni de fixer une BE-CVR maximale universelle, ni de préférer systématiquement 120–300 €. Les vrais tests futurs pourront calibrer ces paramètres ; aucune performance de campagne n'a été inventée ici.

## Ordre proposé ensuite

Résoudre d'abord le sourcing de **B1**, puis celui du **kit A6**, contre les plafonds économiques chiffrés. Réexaminer **B2/C2** seulement sur nouvelle preuve d'offre et de demande compatible. Après qualification et décision `GO_FINAL` de Hakim : sample, validation `SAMPLE_OK`, puis test Search ; GMC Readiness seulement si le produit devient candidat Shopping/PMax. Aucun de ces passages n'est autorisé automatiquement par ce rapport.
''')
print('Dossiers',len(results),'scénarios',len(econ_rows),'coût',cost)

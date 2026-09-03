# Méthode, provenance et limites

## Périmètre

Neuf offres `PRODUIT PUR`, France, français, observées le 03/09/2026. Cette passe complète deux tests du même jour ; leurs données brutes et conclusions historiques restent intactes. Les nouvelles décisions portent seulement sur les offres étudiées. `UNIVERS`, ses familles et son seuil de 37 500 ne sont pas modifiés.

Le [protocole](protocole.md) fixe un plafond de 10 USD DataForSEO. L'analyse concurrence et le sourcing exploratoire des neuf REVIEW sont demandés explicitement par Hakim. Ce mandat ne donne ni PASS rétroactif, ni autorisation d'achat, ni GO_FINAL.

## Couverture des mots-clés

Sources : suggestions DataForSEO Labs, puis Google Ads `search_volume/live`, France/français, partenaires Search désactivés pour les contrôles. Les réponses historiques du même jour sont réutilisées ; la réponse live la plus récente prime. **2 892 formulations** ont été contrôlées par quatre nouveaux lots live, en plus des contrôles précédents et des témoins. Les variantes et parents retournés sont conservés dans les CSV, y compris les exclusions.

[coverage.json](coverage.json) contient seed, total annoncé, nombre de lignes et source. Les premières explorations « appareil photo » et « liseuse » sont limitées à 1 000 lignes ; des seeds plus spécifiques complètent la couverture. Une page incomplète de parent n'est pas le total du marché. `liseuse compacte` renvoie zéro item sans total exploitable : disponibilité non concluante, pas demande zéro prouvée. Les volumes nuls de l'API restent vides, jamais remplacés par une recherche mesurée à zéro.

Les **9 467 lignes** sont des couples candidat/mot-clé distincts dans chaque dossier, pas nécessairement 9 467 expressions uniques entre dossiers. La livraison « tous les mots-clés » signifie ici tous les mots-clés effectivement collectés dans ce périmètre fini.

## Adressabilité et consolidation

Chaque ligne garde sa classe : `core`, `conditional`, `parent`, `incompatible`, `information`. Ce sont des annotations de recherche, pas de nouveaux états du pipeline. Marques et enseignes ont un drapeau séparé. Le dictionnaire est visible dans [build_keywords.py](build_keywords.py) et demeure non exhaustif.

1. Choisir une offre cohérente ; retirer autres mécanismes, services, pièces, usage pro, occasion, santé/SAV informationnels et marques non accessibles.
2. Utiliser `scripts/kw_dfs.py` pour accents, pluriels, mots vides et ordre ; expliciter dans cette étude les équivalences TV/télévision et mural/murale.
3. Pour chaque groupe lexical, retenir **MAX**, pas la somme.
4. Fusionner aussi deux groupes lorsqu'ils ont le même volume, la même série mensuelle datée sur au moins 12 mois, au moins trois valeurs mensuelles distinctes et un recouvrement lexical. Cette règle limite les buckets dupliqués ; elle ne prouve pas l'identité de tous les synonymes.
5. Additionner les groupes cœur seulement. Publier à part le scénario cœur + conditionnels et les parents ; ne pas sommer symptôme + produit + parent.
6. Près de 12 500, garder REVIEW si la compatibilité, le chevauchement ou l'économie peut faire basculer la décision.

Les [groupes compressés](groupes.json.gz) gardent tous leurs membres et raisons de fusion ; le [corpus compressé](corpus.json.gz) conserve les mesures choisies. Les CSV ont deux compteurs : `counted_core_volume` pour le cœur, `counted_volume` pour cœur + conditionnels. Un zéro dans un compteur signifie doublon non additionné ; la colonne `volume` reste la mesure originale. `core_group_id` et `group_id` appartiennent à des regroupements différents, à ne pas mélanger.

Le cœur n'est **ni une audience unique, ni un plancher statistique, ni un plafond exhaustif**. Google peut regrouper des formulations de manière opaque. Un corpus plus gros n'est pas une preuve de croissance par rapport aux premières passes : la couverture et les exclusions ont changé.

Le ratio générique vaut `volume générique (core + conditional) / (générique + marque du même périmètre)`. Il décrit seulement le corpus collecté, après nettoyage. Il ne permet pas de dire que « 87 % des acheteurs de liseuses ne cherchent pas une marque ». Les marques d'appareil à équiper (TV) sont à interpréter comme compatibilité, distinctement de la marque du produit vendu.

## SERP, Shopping et concurrents

18 captures organiques, deux par candidat, 20 résultats demandés en desktop. [serp.csv](serp.csv) conserve les 518 éléments de page retournés, pas 518 concurrents. Les premiers résultats et la nature des offres sont commentés dans chaque dossier. Ce n'est pas une observation mobile, nationale permanente ou personnalisée.

Aucun item `paid` retourné : **densité Ads réelle MANQUANT**. Les modules produits et 360 cartes Google Shopping sont des observations séparées. Les neuf recherches Shopping fournissent 40 cartes produit chacune ; trois éléments techniques supplémentaires par réponse ne sont pas comptés. Titres, vendeurs, devises et prix sont préservés. Les cartes ne prouvent ni le prix livré ni la variante. Échantillon brut non homogène : pas de médiane de marché utilisée comme gate économique.

Les pages marchandes sont archivées avec date, URL, statut HTTP et hash. Ces captures servent à examiner les offres, prix, garanties annoncées et contenu ; elles ne constituent pas un audit juridique ou une validation des promesses du marchand. Les documents commerciaux peuvent être contradictoires. Exemple : le produit Univers Étendoir consulté vaut 39,99 €, les 149,99/174,99 € visibles concernent d'autres recommandations. Le catalogue Kodak argentique ne valorise pas un compact numérique neuf. Une promotion Steadyrack en rupture ne constitue pas une disponibilité concurrente.

Les signaux TrendTrack proviennent des tests du même jour liés dans les dossiers ; pas de nouvelle extraction présentée comme telle ici. La hausse du trafic/des annonces est une raison d'enquêter, pas une preuve de rentabilité ni d'attribution au produit. Pas de part de marché, de budget publicitaire ni de ventes concurrentes inventés.

## CPC, change et économie

La réponse ne contient pas de devise CPC. La [documentation officielle de l'endpoint Google Ads DataForSEO](https://docs.dataforseo.com/v3/keywords_data/google_ads/search_volume/live/) indique USD. La devise est donc `USD_DOCUMENTED`, pas EUR par défaut ni une devise déduite du pays. Cette vérification prime sur une consigne locale générale moins précise. Les CPC Labs secondaires sont utilisés avec le même libellé explicité ; le contrôle live couvre les groupes cœur mesurés.

Change : [BCE](https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml), 03/09/2026, **1 EUR = 1,1615 USD** ; capture structurée [fx.json](fx.json). CPC € = CPC USD / 1,1615. Le CPC de travail est pondéré par le volume des groupes cœur ayant un CPC ; la couverture est publiée. Ce n'est pas une prévision de CPC au lancement.

Scénarios explicitement hypothétiques : TVA 20 %, paiement 2 % du TTC + 0,30 €, provision retours/SAV 5 % du TTC. Le régime réel, les frais et les pertes seront à remplacer par les données de la société. Les hypothèses ne constituent pas des conseils fiscaux ni des règles canoniques.

```
revenu_net_scenario = prix_TTC / 1,20
contribution_avant_ads = revenu_net - COGS - port - paiement - retours/SAV - autres coûts variables
break_even_CPA = contribution_avant_ads
break_even_CVR = CPC / contribution_avant_ads      # seulement si contribution > 0
CPA_scenario = CPC / CVR_hypothétique
coût_produit_plus_port_max = revenu_net - paiement - provision_SAV - CPA_scenario
```

Les coûts fixes et le profit cible ne sont pas couverts par le point mort. Les CVR 1 %, 1,5 %, 2 %, 3 % et CPC ×1,5 sont des sensibilités ; aucune n'est une prédiction ni un hard kill universel. Un plafond négatif signifie que ce scénario ne fonctionne même avant achat du produit, pas que toutes les campagnes possibles sont condamnées.

Pour A5 seulement, le coût produit et le port exacts sont observés via API ; la TVA fournisseur est considérée non récupérée dans la simulation prudente tant qu'aucune facture/traitement réel n'est vérifié. La marge de scénario reste distincte de la marge réelle. Pour les autres offres, **ne jamais remplacer le COGS manquant par zéro** : on calcule une cible de coût, pas un bénéfice inventé.

## Saison

Google Trends via DataForSEO, France, web, cinq ans, deux requêtes par appel ; quatre appels sans accents supplémentaires pour les séries lacunaires. Les indices ne sont pas des volumes. Exclusion de la semaine incomplète ; aucune imputation des valeurs nulles. Un ratio n'est publié que si la couverture descriptive du segment est suffisante (80 % et dix semaines Q4 connues pour ce calcul), sans transformer cela en gate produit.

Cas utiles : C2 confirme un pic Q4 malgré un recul récent ; B1 a un socle mais pas de croissance Q4 évidente ; B3 est saisonnier hors Q4. Les autres courbes spécifiques sont souvent insuffisantes. Les séries mensuelles Google Ads servent de contrôle saisonnier complémentaire, pas de remplacement automatique du socle 5 ans exigé avant GO.

## Décisions et apprentissage

Le score n'est pas le gate. Pas de nouveaux Search/Business/Shopping Scores chiffrés, pas de note SERP arbitraire. Les dimensions sont évaluées en prose et les chiffres de demande/économie restent auditables. Quatre REVIEW et cinq STOP de périmètre ; zéro PASS/GO. Une preuve fournisseur manquante n'est pas automatiquement un échec économique universel.

[results.json](results.json) conserve le pré-test et les champs réels manquants. Si un candidat passe ultérieurement GO_FINAL puis SAMPLE_OK, relier cette étude aux objets existants `instrumentation/croyances/` et `instrumentation/mesures/` pour le suivi CPC/CVR/CPA/CTR/ATC/checkout/ventes/ROAS. Aucun faux experiment de campagne n'est créé. Aucun seuil ne doit être recalibré sur ces seules simulations.

## Reproduction locale

Les scripts de cette étude sont des auxiliaires d'analyse, pas des modules branchés au pipeline de production. Pour recalculer sans réseau :

```bash
python3 analyses/2026-09-03-qualification-9-produits-pur/consolidate.py
python3 analyses/2026-09-03-qualification-9-produits-pur/build_context.py
python3 analyses/2026-09-03-qualification-9-produits-pur/build_report.py
```

Les collecteurs `collect_*.py` appellent des services ; ne pas les relancer pour une simple lecture. Le ledger et les caches évitent les recharges déjà archivées. Les secrets restent dans l'environnement local, jamais dans les livrables.

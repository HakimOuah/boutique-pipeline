# Pilote — PRODUIT PUR / Search Upgrade + GMC Readiness

**3 septembre 2026 — test avant implémentation, demandé par Hakim.**

Le parcours proposé est exploitable manuellement et la collecte DataForSEO fonctionne. Le pilote confirme surtout trois priorités : arrêter plus tôt les périmètres insuffisants, comparer exactement l'offre vendue et l'offre sourcée, puis corriger les contrats des outils avant de les automatiser. Il ne démontre pas encore une amélioration du taux de winners.

**Coût API nouveau : 0,4158 USD, plafond annoncé 0,60 USD.** Aucun changement du moteur, des seuils, des scores canoniques ou du registre. Aucun sourcing nouveau, achat, lancement Ads, envoi GMC ou modification de boutique. Seuls les résultats de ce pilote sont ajoutés au dépôt.

## 1. Périmètre et protocole

Trois exercices distincts :

1. Rejouer les quatre dossiers PRODUIT PUR Q4 du 1er septembre, les panneaux du 2 septembre et l'économie historique du kit tufting. Conserver un dossier UNIVERS comme contrôle de séparation des modes.
2. Faire une sonde Demand-first actuelle, sur l'exemple « caméra de surveillance sans abonnement ». Vérifier le registre avant la sonde ; aucune entrée équivalente trouvée. Les caméras thermiques, d'inspection et de chasse déjà écartées sont d'autres objets.
3. Injecter des défauts dans les fonctions existantes, uniquement en mémoire : négation, CPC, port manquant, contrat DataForSEO et préflight GMC. Les données de ces tests sont **fictives** ; leurs sorties ne qualifient aucun vrai candidat.

Critères de lecture : pas de cumul parent/produit/contrainte sans justification ; seuil PUR 12 500 et bande 10 000–15 000 conservés ; seuil UNIVERS 37 500 ; aucune note inventée quand sa preuve manque. Les verdicts de rejeu restent séparés des décisions historiques.

Les réponses nouvelles sont datées du **03/09, 12:47–12:48 heure de Paris**. Les dossiers historiques restent datés du jour de leur collecte. Ce n'est pas un test comparatif aveugle : les issues historiques étaient connues.

## 2. Rejeu des quatre idées issues de TrendTrack

Source : [décisions et périmètres du 01/09](../2026-09-01-q4-produit-pur/cluster-decisions.json). Les sommes des lignes retenues ont été recalculées.

| Candidat | Demande pertinente archivée / mois | Corpus brut déjà dédupliqué, avant exclusions | Sortie du parcours proposé, en simulation |
|---|---:|---:|---|
| Bagage à compression intégrée | 1 890 | 7 510 | `STOP_PREQUALIFICATION` sur le périmètre mesuré |
| Plaque d'acier de cuisson | 150 | 790 | `STOP_PREQUALIFICATION` sur le périmètre mesuré |
| Kit boulangerie au levain | 130 | 190 | `STOP_PREQUALIFICATION` sur le périmètre mesuré |
| Remontoir de montre | 7 000 | 8 980 | `STOP_PREQUALIFICATION` sur le périmètre mesuré |

Les quatre dossiers enregistrent historiquement **« CAS LIMITE — décision Hakim requise »**, en raison de contrôles Google/Shopping/Trends incomplets. Aucun n'est dans la bande volumique 10 000–15 000. Même leurs corpus bruts mesurés, avant nettoyage supplémentaire, restent sous 10 000.

**Résultat du test :** le parcours proposé peut interrompre ces quatre dossiers sans attendre Trends ni commencer le sourcing. Cela économiserait des vérifications complémentaires, mais aucun temps économisé n'a été mesuré. Le workflow historique avait déjà empêché le sourcing : ce bénéfice ne doit pas lui être retiré.

**Limite :** un échantillon incomplet ne prouve jamais que toute une catégorie est petite. L'arrêt concerne l'offre et le périmètre mesurés. Une reprise demanderait une raison explicite et un nouveau périmètre traçable. Les statuts du registre n'ont pas été modifiés.

## 3. Sonde Demand-first en direct

### Collecte réellement effectuée

| Appel | Résultat | Coût USD |
|---|---|---:|
| Témoin avant, Google Ads live | `tufting` = 12 100 | 0,0900 |
| Labs `camera surveillance` | 1 000 lignes sur 6 318 annoncées | 0,1320 |
| Labs `camera surveillance sans abonnement` | 15 lignes sur 15 annoncées | 0,0138 |
| Google Ads live, 24 formulations et témoins | Têtes, variantes et besoins voisins contrôlés | 0,0900 |
| Témoin après | `tufting` = 12 100 | 0,0900 |
| **Total, témoins inclus** | Tous les appels terminés sans erreur | **0,4158** |

Les paramètres sont France/français, `search_partners: false` pour Google Ads ; les lignes live retournent `location_code: 2250`, `language_code: fr`. Temps cumulé des cinq appels : **5,738 secondes**, hors analyse et recherche web. Aucun renouvellement silencieux ni pagination supplémentaire.

Les CPC sont conservés en **USD**, conformément aux documentations [Google Ads live](https://docs.dataforseo.com/v3/keywords_data/google_ads/search_volume/live/) et [Labs](https://docs.dataforseo.com/v3/dataforseo_labs/google/keyword_suggestions/live/). L'absence d'un champ devise dans chaque ligne n'autorise pas à les traiter comme des euros. Aucune conversion ni économie fournisseur n'a été inventée.

### Ce que les chiffres disent

| Niveau | Requête live | Volume mensuel | CPC USD | Traitement |
|---|---|---:|---:|---|
| Parent | caméra de surveillance | 60 500 | 2,85 | Non attribué automatiquement à une contrainte |
| Produit + contrainte | caméra de surveillance sans abonnement | 590 | 1,11 | Tête du périmètre étudié |
| Recherche comparative | meilleure caméra de surveillance sans abonnement | 590 | 1,07 | Niveau commercial séparé |
| Usage + contrainte | caméra de surveillance extérieur sans abonnement | 260 | 1,19 | Usage extérieur |
| Technologie + contrainte | caméra de surveillance Wi-Fi sans abonnement | 210 | 0,75 | Wi-Fi et stockage local possibles |
| Besoin voisin | caméra de surveillance sans Wi-Fi | 1 600 | 0,84 | Autre contrainte, pas un synonyme |
| Besoin voisin | caméra de surveillance sans fil | 6 600 | 1,69 | Batterie/liaison radio à distinguer |
| Besoin voisin | caméra de surveillance sans Internet | 260 | 0,84 | Autonomie réseau à démontrer |

Les **17 formulations contrôlées contenant « abonnement »** représentent 3 940 si on additionne naïvement toutes les lignes. Après MAX des variantes proches, et rapprochement manuel des variantes grammaticales à séries identiques, elles représentent **2 140 avant exclusions métier**. Ce chiffre n'est pas une demande adressable validée.

Dans un scénario d'offre extérieure Wi-Fi, stockage local et alimentation solaire, les formulations potentiellement compatibles représentent **1 230**, plus **620 de recherche comparative à garder séparés**. L'intérieur, le parent « maison » ambigu et la 4G restent à part. Aucun fournisseur ni fonction réelle ne valide encore ce scénario. Les [groupes, exclusions et hypothèses](demand-first-results.json) sont conservés ligne par ligne.

**Sortie : aucune préqualification accordée.** Cette sonde ciblée ne fournit pas le volume requis. Elle ne suffit pas à prononcer un STOP définitif de toute la catégorie surveillance : la graine générale est paginée partiellement et des formulations produit génériques pourraient être adressables après définition de l'offre et lecture SERP. Aucun parent n'est ajouté pour fabriquer un PASS.

### Obstacles observés

- La collecte générale plafonnée ne couvre que 1 000/6 318 formulations. Elle sert à découvrir des contraintes, pas à annoncer la taille totale du marché.
- Les 15 suggestions ciblées ne contenaient pas la tête exacte « caméra de surveillance sans abonnement » à 590. Le contrôle live complémentaire l'a trouvée. La découverte Labs seule serait donc insuffisante.
- Des variantes proches ont des séries et CPC différents. Des séries différentes ne constituent pas, à elles seules, une preuve de recherches indépendantes. Le MAX conservateur et l'intervalle de CPC restent préférables à une somme certaine.
- L'existence d'un besoin clair n'assure pas une différenciation. [Eufy](https://www.eufy.com/eu-fr/collections/local-storage-security-camera) et [Reolink](https://store.reolink.com/fr/security-camera-without-subscription/) proposent déjà du stockage local sans abonnement obligatoire. Cela démontre l'existence de l'offre, pas leur domination de la SERP.
- « Sans abonnement » doit préciser **à quoi** : une [Reolink Go 4G](https://reolink.com/fr/product/reolink-go/) nécessite une carte SIM et un abonnement mobile. Une promesse sur le cloud ne supprime pas le coût de connectivité.

**Non mesuré dans ce pilote :** ratio générique représentatif, densité réelle des annonces Google.fr, SERP Winnability, compte TrendTrack en direct, fournisseurs actuels et CPC payé en campagne. Ces champs restent `null`. Aucune recherche fournisseur n'est justifiée par la seule sonde.

## 4. Dossier qui dépasse le seuil : panneaux à tasseaux

Le [rapport du 02/09](../2026-09-02-panneaux-muraux-bois/rapport-mesure-dfs.md) donne 22 640 recherches mensuelles, tête à 14 800. Une sensibilité conservatrice, en regroupant à nouveau les variantes lexicales proches par MAX, ramène ces 15 lignes à **20 170**. Le signal de demande subsiste au-delà de la bande 10 000–15 000 ; la tête seule resterait dans cette bande. Ce calcul ne remplace pas l'adjudication de l'offre exacte.

Le piège se situe ensuite dans l'unité vendue :

| Repère historique | Surface | Montant |
|---|---:|---:|
| Fournisseur TWISTERCK : 4 × 120 × 60 cm | 2,88 m² | 108,39 € rendu |
| Repère concurrentiel : 4 × 240 × 60 cm | 5,76 m² | 189,90–359,81 € TTC |
| Deux lots fournisseur, même surface totale | 5,76 m² | 216,78 € rendu |

Sources : [sourcing daté](../2026-09-02-panneaux-muraux-bois/rapport-sourcabilite-aliexpress.md), [sonde prix](../2026-09-02-panneaux-muraux-bois/rapport-sonde-prix.md).

Au bas du repère concurrentiel, le calcul `189,90 / 1,20 − 216,78` donne déjà **−58,53 € avant frais de paiement, retours et SAV**, en conservant le coût rendu comme non récupérable. La récupération éventuelle de TVA fournisseur doit être prouvée séparément. Deux panneaux de 120 cm ne sont pas non plus nécessairement interchangeables avec un panneau de 240 cm : joints, pose et rendu diffèrent.

**Sortie : pas de TECHNICAL_PASS.** L'hypothèse d'alignement sur le prix bas est économiquement rejetée ; le produit entier ne l'est pas. Un pack compact ou une offre premium demande un benchmark propre, des preuves fournisseur et une nouvelle économie. La demande suffisante ne résout pas ces points.

Autre contrôle de coût : le rapport historique annonce 0,767 USD observé mais signale **14 témoins internes non inclus**, soit environ 1,26 USD supplémentaires déduits du tarif, pour un total estimé de 2,03 USD. Ce supplément est une estimation historique, pas une nouvelle dépense. Le pilote actuel comptabilise tous ses témoins dans le ledger.

## 5. Économie reproductible : kit tufting

À partir des montants du [19 juillet](../../reports/phase5-marge-kit-tufting-2026-07-19.md) :

`229 / 1,20 − 78,61 − 4,52 − 9,16 − 4,58 = 93,96 € de contribution avant Ads`.

Le prix de vente, les frais et les provisions étaient des hypothèses ; le coût fournisseur était une observation datée, à reconfirmer au panier. Ce n'est pas une marge actuelle observée.

| CPC | Nature de la valeur | BE-CVR calculé |
|---|---|---:|
| 0,48 € | Référence SEMrush historique du dossier | 0,511 % |
| 0,96 € | Scénario de stress fictif : doublement | 1,022 % |
| 1,50 € | Scénario de stress fictif | 1,596 % |

Le calcul BE-CVR fonctionne avec les données déjà disponibles. Il ne faut pas remplacer 0,48 € par le témoin DataForSEO « tufting » à 1,62 USD : devise, date et périmètre de requête diffèrent.

Le [dossier de croyance](../../instrumentation/croyances/tufting.md) a été reconstruit après lancement ; les scores pré-test sont vides. Le pilote ne peut donc pas calculer « quel Search Score prédit les ventes ». Il faut commencer l'enregistrement prospectif avant les prochains tests et relier les résultats au produit, à l'offre, aux requêtes et à la campagne réellement testés.

## 6. Contrôle UNIVERS

Le [dossier poufs du 03/09](../2026-09-03-univers-poufs/02-volumes-consolides.md) reste `UNIVERS` : 36 095 en consolidation stricte, 47 305 avec adjudications sur le catalogue étendu, 54 730 en ajoutant le parent adjugé. Son `REVIEW_PREQUALIFICATION` est conservé dans la simulation.

Le phare « pouf géant » à 4 630 n'est pas requalifié en PUR grâce au total catalogue. Ce contrôle confirme que le pilote peut partager la collecte tout en conservant les deux unités de demande et les deux gates.

## 7. Défauts injectés dans les outils existants

Exécution locale en mémoire, sans base de données ni fonction de persistance. Résultats complets : [replay-results.json](replay-results.json).

| Injection fictive | Résultat réellement obtenu | Conséquence avant automatisation |
|---|---|---|
| Même candidat, CPC 0,80 puis 100 | Dropilot : **89/100 et `GO` dans les deux cas** | Le CPC ne bloque pas ce moteur ; le gate économique doit être réellement exécuté |
| « caméra surveillance wifi » / « caméra surveillance sans wifi », sans URL ni angle | Même empreinte de candidat | Préserver négations et contraintes dans l'anti-doublon |
| Prix fournisseur 100, port absent | Coût rendu calculé = 100 | Un port inconnu ne peut pas devenir gratuit |
| Préqualification DataForSEO France, preuves fictives complètes | Exception : source attendue `SEMRUSH_FR` ou `DATAFORSEO_FR_FALLBACK` | Le contrat Product Factory n'accepte pas la source canonique actuelle |

Le normaliseur de mots-clés `kw_dfs.py` conserve bien « sans » sur la paire testée : la collision observée vient de **l'anti-doublon candidat Dropilot**. Les deux mécanismes ne doivent pas être confondus.

Les fonctions Product Factory ont été lues au commit **`9afa920e7ee6d62df7df71a9152cf6315e4e42e7`** du clone `aliexpress-mcp-server`, puis chargées en mémoire. Ce test n'atteste pas de la version effectivement déployée sur une passerelle distante.

## 8. GMC : test du module existant

Fixture fictive déjà fournie par `tests/test_gmc_readiness.py`, même commit Product Factory. Aucun compte réel n'a été interrogé.

| Cas | Résultat existant | Lecture pour l'upgrade |
|---|---|---|
| Fixture complète | `GMC_PREFLIGHT_PASS` | Contrôle local seulement, pas approbation Google |
| Sample manquant | `BLOCKED_BY_COMPLIANCE_GATE` | Blocage conservé |
| Prix PDP différent du feed | `GMC_PREFLIGHT_BLOCKED` | Blocage conservé |
| Email visible mais non cliquable | `GMC_PREFLIGHT_BLOCKED` | Séparer exigence officielle de préférence opérateur/UX |
| Image principale 400 × 400 | `GMC_PREFLIGHT_BLOCKED` | Règle à dater et contextualiser |
| Tous les relevés datés de 2020 | **`GMC_PREFLIGHT_PASS`** | Contrôle de fraîcheur absent |
| Relevés absents | `GMC_PREFLIGHT_BLOCKED` | Complétude minimale déjà contrôlée |
| Performance mobile à 50 | PASS avec avertissement Terry | Bonne séparation entre avertissement et blocage |

Pour l'image, Google annonce le minimum généralisé **500 × 500 au 31 janvier 2027** ; jusque-là, les minima habituels restent 100 × 100 hors vêtements et 250 × 250 pour les vêtements, avec avertissements intermédiaires. Le cas YouTube Shopping sur TV exige déjà 500 × 500. Le blocage générique de toute image 400 × 400 en Q4 2026 est donc excessif si présenté comme obligation universelle actuelle. [Source Google](https://support.google.com/merchants/answer/12159030?hl=en-).

### Échantillon de classification des recommandations

| Signal du test | Niveau de preuve proposé | Blocage proposé / automatisation |
|---|---|---|
| Cohérence prix/disponibilité feed–PDP | `[GOOGLE_REQUIRED]` — [spécification produit](https://support.google.com/merchants/answer/7052112?hl=en) | Oui si divergence ; comparaison automatisable, prix au checkout à contrôler aussi |
| Contact clair et site fonctionnel | `[GOOGLE_REQUIRED]` — [exigences éditoriales](https://support.google.com/merchants/answer/6150244?hl=en) | Oui si absent/non fonctionnel ; automatisation partielle |
| Email obligatoirement cliquable | `[HEURISTIC]` dans ce pilote ; le code seul ne prouve pas une source Terry | Pas de blocage Google automatique sur ce seul signal ; détection automatisable |
| Performance mobile ≥ 65 | `[OPERATOR_EVIDENCE]` selon l'attribution Terry du module | Avertissement ; mesure automatisable ; pas une garantie d'acceptation |
| Fraîcheur des observations | `[HEURISTIC]` de contrôle interne | Exiger une relecture avant soumission ; âge automatisable, validité de fond à revoir |
| About, profils sociaux, réputation réelle | `[GOOGLE_RECOMMENDED]` — [confiance client](https://support.google.com/merchants/answer/13693865?hl=en) | Recommandation, pas quota arbitraire d'avis ; contrôle partiel |
| Identité artificielle ou contenu différent pour tromper la revue | `[RISKY_OR_UNSUPPORTED]` pour la pratique | À exclure ; une case déclarative ne prouve pas la réalité des surfaces |

Cette table est un **échantillon de test**, pas le catalogue GMC complet du chantier. L'âge maximal des preuves devra rester une règle opérationnelle explicite ; aucun délai universel Google n'est déduit de ce test.

## 9. Ce que le pilote change dans l'ordre d'implémentation

1. **Données et contrats d'abord** : source DataForSEO, devises, dates, contraintes préservées, quantité/dimensions, port inconnu, séparation des modes et des statuts. Sinon les nouvelles dimensions seraient calculées sur des entrées fausses.
2. **Arrêt anticipé et économie ensuite** : un échec suffisant n'attend pas la due diligence complète ; un prix et un coût doivent porter sur la même offre. Le BE-CVR est calculé par scénario documenté, sans plafond de 1,5 % imposé par intuition.
3. **GMC existant à corriger et enrichir** : garder les comparaisons utiles ; ajouter fraîcheur, applicabilité temporelle et niveaux de preuve. Un préflight local ne prouve jamais l'acceptation GMC.
4. **Scores en observation avant calibration** : ce pilote ne fournit aucune relation démontrée score → rentabilité. Enregistrer des expériences futures complètes avant de modifier les pondérations.

Les seuils 12 500/37 500 et la bande de prix 50–400 € restent inchangés. Keywordability et SERP Winnability n'ont pas besoin d'un score numérique autonome pour révéler les obstacles ci-dessus.

## 10. Limites et suite du test

Le pilote valide la faisabilité de la collecte actuelle, les calculs de rejeu et plusieurs défauts reproductibles. Il n'a pas testé une chaîne autonome TrendTrack → sample → ventes → approbation GMC. Les accès TrendTrack, SERP Google.fr interactive et AliExpress en direct restent non vérifiés dans cette session, et aucune métrique réelle de campagne n'a été importée.

L'étape expérimentale suivante utile serait un petit lot prospectif, avec périmètres figés avant recherche, cas sous le seuil et cas au-dessus, chaque coût et chaque arrêt consignés. Le taux de PASS ne serait pas un objectif. Il faudrait ensuite un produit ayant réellement passé les gates et `SAMPLE_OK` pour tester la prédiction économique sur des campagnes autorisées. Aucun de ces lancements n'est implicite dans le présent pilote.

## Preuves

- [Manifest et empreintes des sources](manifest.json).
- [Coûts et durées des appels](api-ledger.json).
- [Consolidation Demand-first](demand-first-results.json).
- [Rejeux, économie et défauts injectés](replay-results.json).
- Réponses API intégrales compressées sans modification de leur contenu : `01-witness-before.json.gz` à `05-witness-after.json.gz`. Elles contiennent les paramètres, horodatages, réponses et coûts, jamais les en-têtes d'authentification. La première découverte est paginée à 1 000 lignes ; cela reste indiqué dans les données.

Les scripts de collecte ponctuels ont été exécutés hors du dépôt et ne constituent pas un nouveau moteur. Les fichiers canoniques et le registre demeurent inchangés.

# Q4 2026 — test de découverte PRODUIT PUR, 6 TrendTrack + 6 Demand-first

**3 septembre 2026 — expérience avant implémentation.** Suite au [premier pilote](../2026-09-03-pilote-search-upgrade/README.md), Hakim a demandé de tester la créativité et la sévérité de la sélection sur des idées nouvelles.

**Addendum du 03/09 après retour de Hakim :** les douze pistes sont [indexées au registre](../../registre-candidats.md). La [suite proposée couple TrendTrack et la demande Google](orientation-decouverte-couplee.md) et élargit le scouting au-delà des deux vues sauvegardées. Le compte rendu ci-dessous conserve le protocole et les résultats du test initial ; aucun candidat n'est promu par cet addendum.

**Résultat : 12 pistes documentées, 5 STOP_PREQUALIFICATION limités à l’offre testée, 7 REVIEW_PREQUALIFICATION, 0 PASS_PREQUALIFICATION et 0 GO_FINAL. Coût DataForSEO : 2,22028 USD.** Trois dossiers justifient une prochaine vérification ciblée : étendoir mural, kit de rasage de sûreté, rangement mural vélo. Ce ne sont pas trois produits validés.

Le test confirme l’intérêt opérationnel d’une entrée par la demande. Il ne démontre ni qu’elle surpasse TrendTrack, ni que les critères prédisent des winners. Aucun produit n’a été sourcé, acheté ou lancé. Aucun seuil, score canonique, agent, automatisation ni règle GMC n’a été modifié.

## Ce qui a effectivement été testé

- Protocole et plafonds écrits avant collecte dans [protocol.json](protocol.json) : 6 idées par voie, 5 USD et 40 minutes de recherche active maximum par voie. Aucun quota de PASS.
- Voie A figée avant mesure. Voie B : six seeds thématiques, lecture des requêtes puis gel d’un besoin par seed avant mesure ciblée. [Gel A et seeds B](selection-freeze.json), [gel B](B-selection-freeze.json).
- Anti-doublon dans le registre : harnais anti-traction, poêles titane et claviers mécaniques exclus avant sélection. Les douze nouvelles pistes n’ont pas été remplacées après réception de volumes décevants.
- 24 recherches Labs réussies, 158 contrôles de volume dans un lot Google Ads, deux témoins supplémentaires et 20 instantanés SERP France/desktop. Le témoin « tufting » vaut 12 100 dans les trois relevés.
- Séries mensuelles août 2025–juillet 2026 conservées. Le ratio saisonnier est descriptif sur un seul Q4 historique. **Google Trends cinq ans non exécuté ; aucune validation saisonnière complète revendiquée.**
- Une contre-vérification TrendTrack après découverte Demand-first, sur CyclMania. Les cinq autres pistes B n’ont pas reçu cette contre-vérification.

Les deux vues sauvegardées « Shopping FR » et « Scaling shopping » renvoyaient zéro résultat. La voie A s’est donc appuyée sur **Weekly Gems et Top Scaling**, majoritairement étrangers, avec des signaux Meta et de boutique. **Elle ne représente pas un échantillon de six succès Search français.** Les vues et les annonces d’origine n’ont pas été modifiées ni enregistrées. [Relevés TrendTrack](trendtrack-views.txt).

Autre limite : les recherches B sont **orientées par des thèmes choisis humainement**, pas une exploration sans a priori. Choisir un besoin par thème introduit un quota de diversité non explicitement fixé dans le protocole initial : déviation documentée dans le gel B, pas un tirage aléatoire. Les comparaisons de rendement restent descriptives.

## Les douze pistes

Les volumes ci-dessous sont des **repères contrôlés**, pas des clusters consolidés validés. Le détail des requêtes, des exclusions, des prix, des SERP et des conditions de réouverture est dans [dossiers.md](dossiers.md). Les décisions sont expérimentales : elles ne remplacent pas les décisions du registre.

| ID / origine | Offre explorée | Repère DataForSEO FR/mois | Verdict du test | Point décisif |
|---|---|---:|---|---|
| A1 · TrendTrack | Antivol vélo pliant | pliant 260 ; parent vélo 12 100 séparé | REVIEW_PREQUALIFICATION | Parent partiellement accessible, mais preuve initiale ABUS et confiance à construire |
| A2 · TrendTrack | Appareil photo numérique rétro de poche | numérique vintage 720 ; vintage 3 600 mixte | REVIEW_PREQUALIFICATION | DTC visible, CPC rétro élevé, partage neuf/ancien/argentique à nettoyer |
| A3 · TrendTrack | Oreiller de corps pour sommeil latéral | corps 480 ; coussin de corps 210 | STOP_PREQUALIFICATION | Petit marché directement mesuré ; « body pillow » contaminé par dakimakura, côté par oreillers de tête |
| A4 · TrendTrack | Répulsif électronique pigeons au balcon | pigeon 1 900 ; ultrason pigeon 320 | STOP_PREQUALIFICATION | Demande directe insuffisante, parent oiseaux en partie agricole, efficacité non prouvée |
| A5 · TrendTrack | Mini-liseuse EPUB de poche | mini 260 ; poche 70 ; parent 90 500 séparé | REVIEW_PREQUALIFICATION | Le parent existe, mais accès hors écosystèmes Kindle/Kobo non établi |
| A6 · TrendTrack | Rasoir de sûreté et kit débutant | tête 9 900 ; somme exploratoire 15 020 avant recouvrements | REVIEW_PREQUALIFICATION | Proche du gate selon consolidation ; kit 99 € économiquement plus crédible que rasoir seul 69 € |
| B1 · Demand-first | Étendoir mural rabattable | mural 5 400 ; pliable mural 1 600 | REVIEW_PREQUALIFICATION | Bon besoin et CPC, mais variantes/types de séchoir et capacité à distinguer |
| B2 · Demand-first | Support vélo mural pivotant | mural 4 400 ; accroche mural 2 900 ; pivotant 40 | REVIEW_PREQUALIFICATION | Ne pas réduire la demande au mot pivotant ; ne pas emprunter tout le rangement vélo |
| B3 · Demand-first | Moustiquaire fenêtre sans perçage | 6 600 ; parent fenêtre 90 500 séparé | REVIEW_PREQUALIFICATION | Besoin net, panier et Q4 problématiques ; dépriorisée pour ce calendrier |
| B4 · Demand-first | Kit gouttière sur perche depuis le sol | nettoyer/nettoyeur/nettoyage : chacun 1 900 | STOP_PREQUALIFICATION | Même bucket probable, prestations et produit confondus ; kit réel 109,90 € |
| B5 · Demand-first | Gant réutilisable anti-poils textiles | gant 4 400 ; plafond des contrôles élargis 8 160 avant recouvrements | STOP_PREQUALIFICATION | Prix bas même en lots ; aucun panier de 50 € crédible démontré |
| B6 · Demand-first | Mannequin de repassage automatique | mannequin 720 ; automatique 1 900 mixte | STOP_PREQUALIFICATION | Demande compatible trop petite ; prix de l’appareil corrigé avant conclusion économique |

**Portée des STOP :** arrêt de cette offre à ce stade, pas preuve d’absence de marché pour toute la catégorie. A3/A4/B4/B6 reposent sur les périmètres sondés et les exclusions sémantiques ; ils doivent être rouverts si de nouvelles requêtes directement compatibles apparaissent. Les exports Labs plafonnés ne permettent pas de prouver une couverture exhaustive de toutes les formulations. B5 cumule un problème de demande et un problème de ticket directement observable.

## Mon appréciation de la créativité

**Nouveauté dans notre recherche : oui. Différenciation concurrentielle démontrée : non.** Les douze pistes couvrent des usages distincts, mais une marque, une jolie page et un bundle ne suffisent pas à créer un avantage. Plusieurs propositions que l’on pourrait présenter comme originales existent déjà chez les concurrents : gabarit de perçage chez KROMS, kit complet chez Lamier, rangement pivotant chez Steadyrack.

TrendTrack a facilité la découverte d’offres physiques commercialisées : mini-liseuse et photo rétro, notamment. Son biais ici : produits visibles dans les publicités et vendeurs étrangers, parfois accompagnés de promesses excessives. Le trafic global d’un catalogue n’établit pas la traction d’un accessoire ; Aventon illustre ce problème.

Demand-first a facilité la formulation de besoins : gagner de la place, éviter de percer, nettoyer depuis le sol, éviter le repassage. Son biais ici : les seeds trop larges consomment les 1 000 premiers résultats en doublons et hors-sujet. « Gouttière » ramène du dentaire ; « poils » des races d’animaux et de l’épilation. Le mot « fenêtre » a conduit à la moustiquaire plutôt qu’à un besoin hivernal : le Q4 n’émerge pas automatiquement de la méthode.

**Solution proposée :** poursuivre les deux entrées, en exigeant pour chaque idée deux hypothèses d’offre et un contre-exemple concurrent qui pourrait les invalider. Décrire précisément utilisateur, contrainte, solution actuelle et avantage à vérifier. Pour la découverte B, commencer par un seed de besoin suffisamment précis, puis l’élargir seulement si la couverture est insuffisante. Pour A, réparer les filtres de recherche avant de conclure sur son rendement.

Les trois vérifications qui ont le plus de valeur maintenant :

1. **B1 — Petit espace et charge de linge humide.** Définir un format mural précis, comparer surface utile, encombrement plié, fixation et charge. Un prix de WallFix 24 m ne valide pas le prix d’un petit rack. Le gabarit seul n’est pas une différenciation nouvelle.
2. **A6 — Premier équipement de rasage complet.** Le kit à 99 € existe réellement chez un concurrent. Vérifier si notre offre peut justifier ce panier par la qualité et l’accompagnement ; un simple clone à 69 € est moins séduisant économiquement.
3. **B2 — Deux vélos dans un espace contraint.** Comparer de vrais pivots compatibles avec pneus/garde-boue et des lots réellement utiles. Un support à 49 € laisse peu de place aux coûts à faible CVR. La présence d’une petite boutique dans la SERP mérite examen, sans prouver sa rentabilité.

## Sévérité : ce qu’il faut garder, ce qu’il faut corriger

**Garder le gate de 12 500 et sa zone de revue existante.** Douze idées sans campagnes ne justifient pas de changer ce seuil. Mais un petit volume sur le seul adjectif différenciant ne justifie pas un STOP global : les 40 recherches « support vélo pivotant » ne résument pas le besoin de rangement mural.

**Renforcer la rigueur économique avant de compléter un score.** Le CPC doit correspondre à l’intention réellement achetée. Sur la gouttière, « perche nettoyage gouttière » est à 0,37 USD, tandis que le bucket général nettoyer/nettoyeur est à 2,13 USD. Utiliser le premier CPC avec tout le volume du second fabrique une opportunité artificielle.

**Ne pas transformer l’incertitude en moyenne arbitraire.** Les Search Score et Business Score du repo décrivent leurs dimensions, mais pas leurs barèmes séparés complets. Les champs numériques restent donc `null` ; la qualification Search est qualitative et la décision de gate est indépendante. Aucun nouveau score total ni pondération n’a été introduit. Les coûts, fournisseur et BE-CVR réel restent `MANQUANT`.

**Ne pas traiter REVIEW comme une salle d’attente illimitée.** Chaque dossier possède une question précise à résoudre et une condition de réouverture. La prochaine passe doit financer cette question, sans relancer une recherche complète ni commander un sample.

La distinction demande / preuve / économie évite deux erreurs opposées : promouvoir un produit parce que son histoire est convaincante, ou rejeter un besoin parce qu’une formulation précise est petite. Le taux de PASS n’est pas une mesure de qualité du moteur.

## Économie : ce qu’on peut calculer avant sourcing

Sans coût fournisseur, le BE-CVR réel est inconnu. On peut déjà calculer le **plafond de tous les coûts variables avant Ads**, à prix et CVR hypothétiques :

`plafond = prix TTC / 1,20 − CPC EUR / CVR`

TVA 20 % est une hypothèse de simulation. Le plafond doit couvrir produit, transport, paiement, retours/SAV et autres coûts variables. Il ne réserve encore ni bénéfice cible ni frais fixes. Conversion des CPC USD : **1 EUR = 1,1578 USD**, référence [BCE du 2 septembre 2026](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html). Le CPC DataForSEO est un proxy Google Ads, pas un CPC de campagne OH Ventures.

| Offre / prix concurrent utilisé comme hypothèse | CPC proxy EUR | Coûts variables max si CVR 1 % | Si CVR 1,5 % | Si CVR 2 % |
|---|---:|---:|---:|---:|
| Étendoir comparable 59,95 € | 0,216 | 28,37 € | 35,56 € | 39,16 € |
| Rasoir seul 69 € | 0,786 | −21,10 € | 5,10 € | 18,20 € |
| Kit rasoir 99 € | 0,786 | 3,90 € | 30,10 € | 43,20 € |
| Support vélo pivotant 49 € | 0,311 | 9,74 € | 20,10 € | 25,29 € |
| Photo rétro 79 € | 1,270 | −61,13 € | −18,81 € | 2,35 € |
| Gant 28,99 € | 0,458 | −21,62 € | −6,36 € | 1,27 € |

Les CVR 1 / 1,5 / 2 % sont des **scénarios**, pas des seuils recommandés. Une valeur négative démontre l’impossibilité de ce scénario, même avec un produit gratuit ; elle ne démontre pas l’impossibilité de toute stratégie. La photo rétro ressort nettement moins bien économiquement que son intérêt créatif ne le laissait penser. Le kit rasoir change sensiblement l’équation, sans prouver sa rentabilité.

## Obstacles et faux rejets rencontrés

1. **Vues TrendTrack vides.** Cause non diagnostiquée ; ce n’est pas une absence de marché. Les alternatives ont été tracées, pas maquillées en source Search équivalente.
2. **API Labs : une seule tâche par appel.** Le premier essai de lot a traité une tâche et refusé les cinq autres. Les cinq refus ont été repris individuellement, sans facturation dupliquée du succès. Le statut HTTP/global ne suffit pas : vérifier chaque tâche.
3. **Buckets et orthographe.** Les deux formulations « étendoir a linge » et « étendoir à linge » valent respectivement 60 500 et 18 100 dans le contrôle live. On ne les somme pas ; leur proximité exige une consolidation explicite. Des séries identiques sont un signal de recouvrement, pas une preuve que deux intentions différentes sont identiques.
4. **Prix de carte Google trompeur.** Le mannequin DRY MAGIC affiché à 19,95 € dans `popular_products` est à 79,95 € sur la [page de l’appareil](https://www.liserevert.fr/equipements-de-la-maison/35-mannequin-sechage-et-repassage-dry-magic-3-en-1.html), avec accessoires et produits recommandés à d’autres prix. Origine exacte du 19,95 € non établie. Aucun STOP économique ne doit s’appuyer sur ce prix non confirmé.
5. **Saisonnalité.** « Moustiquaire fenêtre sans perçage » : 390/590/880 recherches en décembre/novembre/octobre 2025. Moyenne Q4 ≈ 620 ; ratio Q4/moyenne des douze mois ≈ 0,10. Volume annuel élevé ≠ bon prochain test Q4.
6. **Preuve de boutique ≠ preuve produit.** CyclMania trouvé après la SERP : environ 7 K visites estimées, 549 produits, annonce marquée Search/France, mais répartition réseau affichée contradictoire et texte/produit non attribués. Cela prouve une trace publicitaire déclarée par TrendTrack, pas que le support vélo fonctionne en Search. [Relevé](trendtrack-demand-first-check.txt).
7. **Instantané SERP incomplet pour la publicité.** Aucun item `paid` n’a été retourné dans ces instantanés. Cela ne prouve pas zéro annonceur. `popular_products` ne prouve pas une campagne Shopping payante. Aucun score de densité Ads n’a été inventé.

La [seconde lecture de trois STOP](second-pass.md) conserve les verdicts de périmètre, mais écarte des motifs économiques non prouvés. Même agent, fichier sans premier verdict : **pas un test indépendant en aveugle**.

## Coût, temps et suites

| Mesure | TrendTrack → mesure | Demand-first → produit |
|---|---:|---:|
| Idées documentées | 6 | 6 |
| REVIEW_PREQUALIFICATION | 4 | 3 |
| STOP_PREQUALIFICATION de périmètre | 2 | 3 |
| PASS_PREQUALIFICATION | 0 | 0 |
| Coût DataForSEO, témoins partagés inclus | 0,82064 USD | 1,39964 USD |
| Coût API par idée documentée | 0,13677 USD | 0,23327 USD |

Les abonnements TrendTrack, le travail humain/agent et les outils de navigation ne sont pas inclus. « Idée documentée » signifie dossier relisible avec mesure exploratoire, offre et obstacle ; cela ne signifie pas prêt au sourcing. **Aucun coût par PASS exploitable ne peut être calculé avec zéro PASS.** La voie B a coûté plus cher ici parce que ses seeds larges ont renvoyé systématiquement 1 000 résultats, pas parce que Demand-first serait structurellement plus coûteux.

Collecte entre 11:38:22 et 11:57:08 UTC, soit environ 19 minutes écoulées, hors préparation et rédaction. Les voies ont été entrelacées ; aucun chronomètre actif séparé, donc aucune comparaison de vitesse A/B. Les deux plafonds de 40 minutes sont respectés, sans prétendre avoir consacré 40 minutes à chacune. [Temps et limites](effort.json), [coûts exacts](api-ledger.json).

**Prochaine étape proposée avant intégration au moteur :** résoudre les trois questions prioritaires B1/A6/B2, puis appliquer la même fiche de preuve à une seconde salve avec source A Search réellement vérifiée et seeds B de problèmes/contraintes plus précis. Un test de règles ne remplace pas les campagnes : la calibration de seuils nécessite ensuite des expériences avec CPC/CVR/CPA réellement observés et leurs incertitudes.

## Fichiers et reproductibilité

- [Dossiers lisibles](dossiers.md) : 12 idées, hypothèses, exclusions, prix, SERP, décision et prochaine action.
- [Résultats structurés](results.json) et [contrôles CSV](controls.csv) : champs inconnus conservés `null`, pas de score ni de marge fabriqués.
- [Résumé calculé](summary.json), [liste des contrôles](control-keywords.json), [requêtes SERP initiales](serp-queries.json).
- `*.json.gz` : réponses API datées et paramètres, sans identifiants de connexion. [Manifeste](manifest.json) avec empreintes SHA-256.
- Les prix sont des observations ponctuelles, parfois promotionnelles ou issus de cartes à confirmer. Les claims commerciaux restent des déclarations de vendeurs.
- Lors du test, les règles canoniques PRODUIT PUR / UNIVERS, le registre et les états humains sont restés inchangés. **Suite au retour de Hakim le 03/09, les douze pistes ont été indexées au registre pour l'anti-doublon, sans promotion ni changement des gates.** Voir l'addendum en tête de rapport.

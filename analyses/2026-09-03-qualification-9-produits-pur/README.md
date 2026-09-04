# Qualification des neuf PRODUITS PURS — 03/09/2026

> **État courant après décision de Hakim le 04/09 :** B1 étendoir abandonné (`NO_GO_FINAL`) pour concurrence Ads jugée trop forte ; A6 rasoir devient priorité de recherche, toujours `REVIEW_PREQUALIFICATION` / `TECHNICAL_INCONCLUSIVE`. [Approfondissement et correction du domaine Lamier](../2026-09-04-approfondissement-rasoir-surete/README.md). **3 REVIEW, 5 STOP techniques et 1 NO_GO humain ; zéro PASS/GO.** Les tableaux et l’ordre proposés ci-dessous décrivent la qualification historique du 03/09 et sont supplantés par cette décision.

> **Complément du 04/09 :** [comparaison des captures SEMrush et des réponses DataForSEO](../2026-09-04-audit-ecarts-volumes/README.md). Sans accents, les ordres de grandeur de l'étendoir se rapprochent ; ce contrôle initial maintenait REVIEW, avant l'abandon humain indiqué ci-dessus. Les 13 180 d'A6 désignent les rasoirs de sûreté, pas la demande explicite de kits à 99 €. Les totaux ci-dessous restent les estimations du 03/09, pas de nouvelles mesures validées.

**Deux pistes à poursuivre en priorité : étendoir mural et kit de rasage. Deux réserves : support vélo pivotant et casque TV. Cinq thèses à arrêter. Aucun candidat prêt à lancer.**

Demande Hakim : analyse approfondie des neuf candidats non STOP des deux tests de découverte, jusqu'à la concurrence, au sourcing et à l'économie. Cette étude n'implémente pas la nouvelle architecture. Elle conserve le modèle PRODUIT PUR Search, le seuil de 12 500, les règles UNIVERS et le vocabulaire canonique.

## Résultats

| Produit | Cœur / mois | + conditionnels (non validé) | Décision technique | Suite |
|---|---|---|---|---|
| [A1 — Antivol vélo pliant / articulé](dossiers/A1.md) | 950 | 950 | TECHNICAL_FAIL | Arrêt de cette thèse |
| [A2 — Appareil photo numérique rétro / vintage de poche](dossiers/A2.md) | 1 750 | 11 170 | TECHNICAL_FAIL | Arrêt de cette thèse |
| [A5 — Mini-liseuse EPUB de poche](dossiers/A5.md) | 420 | 950 | TECHNICAL_FAIL | Arrêt de cette thèse |
| [A6 — Rasoir de sûreté — kit débutant en option à valider](dossiers/A6.md) | 13 180 | 17 690 | TECHNICAL_INCONCLUSIVE | Priorité 2 |
| [B1 — Étendoir mural rabattable intérieur](dossiers/B1.md) | 15 490 | 17 310 | TECHNICAL_INCONCLUSIVE | Priorité 1 |
| [B2 — Support vélo mural pivotant](dossiers/B2.md) | 190 | 13 000 | TECHNICAL_WATCH | Réserve |
| [B3 — Moustiquaire fenêtre sans perçage / cadre magnétique](dossiers/B3.md) | 10 300 | 10 840 | TECHNICAL_FAIL | Arrêt de cette thèse |
| [C2 — Casque TV sans fil avec émetteur](dossiers/C2.md) | 11 110 | 12 190 | TECHNICAL_WATCH | Réserve |
| [C6 — Poêle titane sans revêtement synthétique](dossiers/C6.md) | 6 550 | 6 650 | TECHNICAL_FAIL | Arrêt de cette thèse |

Les quatre pistes conservées restent `REVIEW_PREQUALIFICATION`. Les cinq autres deviennent `STOP_PREQUALIFICATION`, limité à l'offre étudiée. **0 PASS_PREQUALIFICATION, 0 TECHNICAL_PASS, aucun GO_FINAL.** Le total conditionnel n'est jamais un total accepté. Le cœur est un proxy nettoyé et non une audience unique ; près du seuil, les chevauchements résiduels et la compatibilité produit imposent de garder REVIEW.

1. **B1 — Étendoir mural** : meilleur rapport apparent demande/CPC. Un prix autour de 79 € peut fonctionner arithmétiquement, mais il doit se défendre contre des offres à 40–60 € et financer le fret. Fournisseur correspondant au produit encore manquant.
2. **A6 — Kit rasage débutant** : fit Search clair, kits à 99 € réellement observés. Le cœur est seulement un peu au-dessus du seuil. Le montage fournisseur exploré ne prouve ni un kit débutant adapté ni une marge suffisante. Google Trends 5 ans reste lacunaire.
3. **B2 — Support pivotant** : dépend presque entièrement d'un accès au parent mural. Les pivots simples à 15–30 € empêchent de supposer un prix premium sans autre mécanisme.
4. **C2 — Casque TV** : problème clair, CPC modéré et saison Q4 confirmée. Volume du kit simple encore sous le seuil et concurrence CGV/Meliconi déjà bien équipée. Réserve pour preuve produit/compatibilité.

Les arrêts sont motivés dans chaque dossier : **A1** faible demande pliant et confiance marques ; **A2** intention vintage mélangée et CPC élevé ; **A5** mini-format étroit et source presque au prix fabricant ; **B3** ticket/marge et saison Q4 défavorables ; **C6** volume, CPC et preuve matière insuffisants.

## Livrables et portée réelle

- [Neuf dossiers](dossiers/) : mots-clés cœur, concurrence, prix, angle proposé, sourcing, économie et conditions de reprise.
- [Tous les mots-clés collectés](mots-cles/) : **9,467 lignes candidat/mot-clé**, avec volumes disponibles, exclusions, déduplication et provenance. Un corpus fini n'est pas « tous les mots-clés de Google ».
- [360 cartes Shopping](shopping-360.csv), [18 SERP](serp.csv), [comparables commentés](concurrence/matrice.csv), captures marchandes datées.
- [Économie et sensibilités](economics.csv) : coût livré admissible, CPA par scénario et stress CPC ; [méthode](METHODE.md).
- [Sourcing](SOURCING.md) : offres retenues pour inspection, faux comparables, exact SKU et limites d'accès.
- [Résultats structurés](results.json), [Trends et couverture](trends-synthese.json), [contrôle qualité](QUALITE.md).

**Coût DataForSEO de cette passe : 1.84724 USD**, hors passes historiques réutilisées, infrastructure et tokens agent. [Journal des appels](api-ledger.json). Plafond du protocole : 10 USD. Témoins `tufting` à 12 100 avant/après ; les montants ne sont pas des dépenses publicitaires.

## Ce que ce test apprend à la méthode

Le couplage TrendTrack ↔ demande reste utile pour découvrir et interpréter une offre. La mesure approfondie doit ensuite dissocier le succès apparent du shop, la demande spécifique et la possibilité de la servir à un prix rentable. Un trafic ou un nombre d'annonces en hausse indique une activité commerciale ; il ne prouve pas le profit ni la vente de cette référence.

La créativité doit être plus libre à l'entrée, puis **la sévérité doit porter sur les preuves** : ne pas ajouter un parent pour sauver le volume ; ne pas emprunter le prix d'un premium pour un crochet simple ; ne pas valoriser un accessoire comme source du produit complet. Une donnée manquante garde REVIEW lorsque la thèse reste plausible ; elle ne mérite pas une note zéro.

Il serait trop sévère d'arrêter B1 uniquement parce que la recherche AliExpress renvoie mal les résultats. Il serait trop permissif de lancer B1 parce que son CPC est faible. La prochaine action utile est une preuve fournisseur exacte, pas davantage de nouveaux scores.

Les 12 500 restent la règle actuelle. Cette petite étude ne justifie ni de baisser ce seuil, ni de fixer une BE-CVR maximale universelle, ni de préférer systématiquement 120–300 €. Les vrais tests futurs pourront calibrer ces paramètres ; aucune performance de campagne n'a été inventée ici.

## Ordre proposé ensuite

Résoudre d'abord le sourcing de **B1**, puis celui du **kit A6**, contre les plafonds économiques chiffrés. Réexaminer **B2/C2** seulement sur nouvelle preuve d'offre et de demande compatible. Après qualification et décision `GO_FINAL` de Hakim : sample, validation `SAMPLE_OK`, puis test Search ; GMC Readiness seulement si le produit devient candidat Shopping/PMax. Aucun de ces passages n'est autorisé automatiquement par ce rapport.

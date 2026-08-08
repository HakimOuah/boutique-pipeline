# Intake — Étude concurrentielle 5 niches Kraken 2026-08-08

## Périmètre

- Boutiques/domaines : cinq concepts catalogue à qualifier — chien, mercerie, scrap/journaling, perles/bijoux, aquascaping.
- Marché/langue : France / français.
- Entreprise : Hakim — projet niche Google Ads / SEO.
- Date : 2026-08-08.
- Objectif : sélectionner un concept défendable et préparer une architecture/offre différenciée avant sourcing exact et économie.
- Horizon : Gate 1 marché/client/concurrence ; aucun lancement autorisé.
- Budget test maximal autorisé : `MANQUANT` ; aucune dépense engagée.
- Canaux étudiés : Google SEO, Google Ads directionnel, Meta comme signal concurrentiel.
- Responsable décision : Hakim.

## Mode commercial et seuils

- Mode : `catalogue-volume` low ticket autorisé.
- Volumes commerciaux nettoyés France : chien 81 860 ; mercerie 221 680 ; scrap 64 740 ; perles 35 770 ; aquarium 48 320.
- Plancher/objectif retenu : 30 000 minimum / 40 000+ confort.
- Collection cœur — cible : 1 000+ ; bande de revue : 800–999.
- Collection secondaire — cible : 500+ ; bande de revue : 300–499.
- Profondeur de cette première salve : 118 à 130 IDs AliExpress uniques par niche ; candidats, pas produits publiables prouvés.
- Minimum catalogue de lancement : 200 produits distincts réellement sourçables ; non atteint à ce stade.
- Prix : low ticket accepté si panier, marge et CAC de rupture sont viables ; aucun plancher arbitraire.
- Sources : run `codex-chasse-clusters/runs/2026-08-08-kraken-catalogue-v1/` et étude `competitor-profiles/`.
- Déduplication : retrait des head terms ambigus et doublons exacts documenté dans le rapport de qualification.

## État existant

- Boutique active dans ce périmètre : non.
- État storefront : non applicable.
- Tracking achat : non applicable.
- GMC : non applicable.
- Fournisseur/stock : recherche AliExpress disponible ; variantes, conformité et coût rendu restent à vérifier pour chaque shortlist.
- Données disponibles : volumes SEMrush, Trends directionnel, SERP, 632 candidats AliExpress, 5 probes représentatifs, BrandSearch, SEMrush concurrents et VOC publique.

## Autorisations

| Action | Classe | Autorisée ? | Par qui/date |
|---|---|---|---|
| Lecture/audit/recherche concurrentielle | A | Oui | Hakim — 2026-08-08 |
| Documents, classeur, branche Git et push | B | Oui | Hakim — 2026-08-08 |
| Publication/site live | C | Non | — |
| Bascule GMC-ready → Growth | C | Non | — |
| GMC/revue | C | Non | — |
| Campagnes/dépense | C | Non | — |
| DSers/commande/import | C | Non | — |

## Contraintes et exclusions

- Chien : résistance, taille, voiture, flottaison et conformité transport passent une gate renforcée.
- Scrap : licences/personnages et produits chimiques non documentés exclus.
- Perles : composition nickel/plomb/cadmium, petites pièces et authenticité matière à prouver.
- Aquarium : vivant, plantes, électricité, étanchéité et CO₂ exclus de la première vague par défaut.
- Aucune ressemblance d’image ne prouve un fournisseur.
- Les métriques tierces sont des estimations ; aucune conversion ou marge concurrente n’est inférée.

## Mise à jour après phase 2 et correction du gate

- Les 212 listings acceptés par V2 restent une bibliothèque auditée, pas une
  shortlist de lancement ni une preuve que les catalogues sont trop courts.
- Le gate actif est `codex-chasse-clusters/GATE-V3-CATALOGUE-SOURCING.md` : la
  preuve est portée par les collections, un jumeau concurrent n'est pas requis
  par PDP et un volume produit peut être égal à zéro.
- Mobilité chien, mercerie et aquascaping : `STOP_PHASE_2`.
- Scrap/journaling et perles/bijoux : `SUSPENDU_PHASE_2`; aucune n'autorise
  encore le sourcing exact.
- Le second rideau a aussi été instruit : Puzzle 3D bois, théière et lunch box
  sont `STOP_PHASE_2`. Avec basse-cour et terrarium, huit dossiers étudiés en
  profondeur sur huit ont été arrêtés.
- Aucun site n'est sélectionné. Les actions autorisées restent lecture, mesure
  et étude concurrentielle ; publication, import, commande et dépense restent
  interdits.

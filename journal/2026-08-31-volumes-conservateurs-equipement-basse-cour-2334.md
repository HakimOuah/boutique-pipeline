---
type: journal
boutique: equipement-basse-cour
date: 2026-08-31
nature: analyse
leviers: [mots-cles]
titre: "Volumes conservateurs — équipement de basse-cour — 23:34"
---

# VOLUMES CONSERVATEURS — équipement de basse-cour — 2026-08-31 23:34 CEST

Mode : UNIVERS · France · français · DataForSEO.
Commande : `python3 scripts/kw_dfs.py "<graine>" --pages 1 --top 40` avec sorties Markdown et JSON.
Contrôle témoin : `tufting` = 12 100 avant et 12 100 après, conforme.
Coût réel : 0,116 USD (cache utilisé sur plusieurs graines), contre 2,112 USD de plafond annoncé.

## Périmètre figé avant mesure

16 graines, fixées dans `journal/2026-08-31-mission-univers-equipement-basse-cour-2026-08-31-2334.md` avant le premier appel.

## Plancher ultra-conservateur : une tête générique distincte par famille

Ce tableau ne somme ni variantes, ni longue traîne, ni tête transversale `équipement poulailler`. Chaque ligne représente une page/collection distincte. Il s’agit donc d’un plancher de demande, pas du consolidé exhaustif.

| Rang | Famille | Tête dédupliquée DataForSEO | Volume mensuel | CPC (devise non exposée par le script) | Brut | Net de marque | Source/date |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Habitat | poulailler | 74 000 | 0,72 | 74 000 | 74 000 | DataForSEO FR · 2026-08-31 |
| 2 | Enclos | enclos à poule | 9 900 | 0,67 | 9 900 | 9 900 | DataForSEO FR · 2026-08-31 |
| 3 | Mangeoires | mangeoire à poule | 9 900 | 0,56 | 9 900 | 9 900 | DataForSEO FR · 2026-08-31 |
| 4 | Abreuvoirs | abreuvoir à poule | 9 900 | 0,61 | 9 900 | 9 900 | DataForSEO FR · 2026-08-31 |
| 5 | Portes automatiques | porte automatique poulailler | 8 100 | 0,71 | 8 100 | 8 100 | DataForSEO FR · 2026-08-31 |
| 6 | Pondoirs | pondoir à poule | 6 600 | 0,59 | 6 600 | 6 600 | DataForSEO FR · 2026-08-31 |
| 7 | Couveuses | couveuse à oeuf | 2 900 | 0,51 | 2 900 | 2 900 | DataForSEO FR · 2026-08-31 |
| 8 | Perchoirs | perchoir à poule | 2 900 | 0,29 | 2 900 | 2 900 | DataForSEO FR · 2026-08-31 |
| 9 | Filets | filet à poule | 2 400 | 0,67 | 2 400 | 2 400 | DataForSEO FR · 2026-08-31 |
| 10 | Chauffage poussins | lampe chauffante poussin | 1 600 | 0,31 | 1 600 | 1 600 | DataForSEO FR · 2026-08-31 |
| 11 | Éleveuses poussins | éleveuse à poussin | 720 | 0,44 | 720 | 720 | DataForSEO FR · 2026-08-31 |
| 12 | Mire-œufs | mire à oeuf | 590 | 0,63 | 590 | 590 | DataForSEO FR · 2026-08-31 |
| 13 | Litière | litière poulailler | 210 | 0,34 | 210 | 210 | DataForSEO FR · 2026-08-31 |
| 14 | Transport | caisse transport volaille | 170 | 0,51 | 170 | 170 | DataForSEO FR · 2026-08-31 |
| 15 | Clôture électrique | clôture électrique volaille | 110 | 0,81 | 110 | 110 | DataForSEO FR · 2026-08-31 |
|  | **TOTAL DES TÊTES DISTINCTES** |  | **130 000** |  | **130 000** | **130 000** | calcul exact Python |

Les trois premières familles pèsent 93 800 recherches/mois, soit 72,2 % de ce plancher ; les cinq premières 111 800, soit 86,0 %.

## Contaminations et retraits observés

- La graine `poulailler` contient des grappes portes, enclos, pondoir, DIY, plans, enseignes et noms propres : aucune de ces lignes n’est ajoutée au total ci-dessus.
- Les formulations avec enseignes/marques (`Gamm vert`, `Omlet`, `Smoby`, `Amazon`, `Leroy Merlin`, etc.) ne sont pas intégrées au net : les quinze têtes retenues n’en contiennent aucune, d’où brut = net sur ce plancher.
- `équipement poulailler` (30/mois) est une tête transversale qui recouvre le catalogue : exclue du total pour éviter un chevauchement.
- `filet poule` présente une contamination culturelle/commerciale visible en SERP Shopping par le filet de poulet alimentaire ; l’échantillon prix l’a explicitement retirée.

## Plancher de lecture

La graine `poulailler` a atteint la limite de 1 000 lignes, et sa dernière idée dédupliquée positive vaut encore 90/mois : son expansion exhaustive est un plancher. Les autres graines ont rendu moins de 1 000 lignes. Le total de 130 000 n’utilise toutefois que la première tête de chaque famille et n’est donc pas gonflé par cette troncature.

## Trends France, 5 ans

Source : Google Trends via pytrends 4.9.2, requêtes France séparées, 262 points hebdomadaires, lecture 2026-08-31.

| Terme | Min hebdo | Médiane hebdo | Max | Mois avec indice moyen ≥20 / 61 | Forme |
|---|---:|---:|---:|---:|---|
| poulailler | 21 | 39 | 100 | 61/61 | socle annuel, hausse fév.–mai, pas un univers Q4 |
| porte automatique poulailler | 13 | 34 | 100 | 60/61 | socle annuel, hausse printanière |
| mangeoire poule | 0 | 27 | 100 | 52/61 | socle majoritaire mais plus irrégulier, hausse fin hiver-printemps |
| abreuvoir poule | 0 | 41 | 100 | 56/61 | socle majoritaire, hausse printemps-été |

## Niveau de confiance

B pour les volumes/JSON DataForSEO ; B pour Trends via client non officiel ; A réservée aux SERP lues dans le dossier associé.

## Ce qui n’a pas pu être établi

- Devise du CPC : l’API/script a exposé les valeurs mais pas la devise du compte ; les CPC ne sont donc pas utilisés pour un ratio prix/CPC.
- Consolidé exhaustif formulation par formulation : non fait ; le chiffre de 130 000 est volontairement le plancher des seules têtes distinctes.
- Sourçabilité, coûts rendus, conformité électrique et origine d’expédition : hors de cette passe.

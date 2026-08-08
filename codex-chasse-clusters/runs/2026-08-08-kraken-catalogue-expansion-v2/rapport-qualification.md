# Qualification Kraken — arborescence et catalogue fournisseur audité

Date : 2026-08-08
Run : `2026-08-08-kraken-catalogue-expansion-v2`
Mode : lecture seule — aucune mutation Shopify, DSers, GMC ou Google Ads.

## Verdict

**INTÉGRITÉ DU LIVRABLE PASSÉE — OBJECTIFS DE PROFONDEUR PARTIELS**

- 887 concepts concurrents stricts conservés après nettoyage.
- 100 mots-clés business SEMrush France documentés.
- 483 listings candidats relus manuellement : 212 acceptés et 271 rejetés.
- 212 fiches produit livrées, avec 212 couples niche/ID AliExpress uniques.
- Chaque titre produit commence par un mot-clé mesuré; le volume est affiché à côté dans le classeur.
- Les volumes répétés sur plusieurs PDP ne sont pas additionnés au potentiel commercial de la boutique.
- Les écarts aux objectifs de profondeur sont conservés explicitement : aucun faux positif n'a été ajouté pour remplir un quota.

## Résultat par niche

| Niche | Mot-clé général | Volume général | Volume commercial nettoyé | Collections | Candidats machine | Acceptés | Objectif indicatif | Écart | Listing qualifié | Listing à vérifier |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Balade, transport & mobilité du chien | harnais chien | 22 200 | 81 860 | 9 | 59 | 32 | 100 | -68 | 26 | 6 |
| Mercerie créative & arts du fil | mercerie | 27 100 | 221 680 | 7 | 97 | 45 | 200 | -155 | 28 | 17 |
| Scrapbooking & journaling | scrapbooking | 27 100 | 64 740 | 6 | 59 | 38 | 100 | -62 | 23 | 15 |
| Perles & création de bijoux | perles pour bijoux | 720 | 35 770 | 10 | 200 | 72 | 200 | -128 | 59 | 13 |
| Aquariophilie & aquascaping | filtre aquarium | 3 600 | 48 320 | 8 | 68 | 25 | 100 | -75 | 21 | 4 |

## Gates appliqués

1. Boutique : au moins 30 000 recherches commerciales nettoyées en France; 40 000 constitue la zone de confort.
2. Collection : cœur à partir de 1 000; secondaire à partir de 500; revue entre 300 et 499.
3. PDP : mot-clé mesuré strictement positif, titre aligné et rattachement à une collection mesurée.
4. Catalogue : objectifs indicatifs de 100 ou 200 références selon la niche, sans compter une simple couleur, taille ou quantité comme nouveau produit; les écarts restent visibles.
5. Listing API : pertinence sémantique, prix présent et validation humaine. La note et les commandes déterminent le niveau de preuve fournisseur, sans exclure un listing sémantique qui doit encore être vérifié.

## Niveaux de preuve

- `EQUIVALENT_CONCURRENT_API` : produit ou collection concurrente observée, concept générique dédupliqué et listing AliExpress pertinent trouvé.
- `DECOUVERTE_FAMILLE_SEO_API` : listing distinct trouvé dans une famille business déjà mesurée; aucune correspondance PDP concurrente directe n'est affirmée.
- `LISTING_QUALIFIE_NOTE_COMMANDES` : listing aligné, note au moins 4,5 et commandes observées.
- `LISTING_SEMANTIQUE_A_VERIFIER` : listing aligné et prix présent, mais note/commandes encore insuffisantes ou absentes; contrôle exact obligatoire.
- Répartition des produits acceptés par origine : 212 lignes. Toutes portent une décision humaine `ACCEPT` et son motif.
- `MANQUANT` : SKU exact, variante, fret France, conformité, prix rendu, marge et CAC d'équilibre restent à valider avant import ou lancement.

## Limites et prochaine porte

Ce run prouve une architecture mesurée et un premier catalogue fournisseur audité. Il ne constitue pas une validation commerciale finale et n'atteint pas tous les objectifs indicatifs de profondeur. La prochaine porte doit sélectionner les références prioritaires, puis vérifier le SKU exact, la variante, la livraison France, la conformité, le coût rendu, le prix cible, la marge de contribution et le CAC d'équilibre. Les catégories sécurité, électrique, CO2, métaux et propriété intellectuelle doivent recevoir leur contrôle spécialisé avant publication.

## Reproduction

Voir `README.md` dans ce dossier pour l'ordre des scripts et les garde-fous. Le classeur final est généré avec `build_final_workbook.mjs`, puis inspecté et rendu en PNG avant export XLSX.

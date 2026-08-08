# Run Kraken catalogue expansion v2

Objectif : reconstruire les cinq catalogues a partir des produits et collections
observes chez les concurrents, puis ne retenir que des concepts distincts avec
un equivalent AliExpress pertinent, un mot-cle business France documente et
une validation humaine finale de chaque listing.

## Gate de comptage et objectifs indicatifs

Les objectifs de profondeur sont de 100 ou 200 produits selon la niche. Ils ne
sont jamais remplis artificiellement : un deficit reste documente. Un produit
ne compte dans le catalogue livre que si :

1. il est soit relié à un produit/une collection concurrente observée, soit
   identifié comme `DECOUVERTE_FAMILLE_SEO_API` dans une famille business déjà
   mesurée ; ces deux niveaux de preuve restent séparés ;
2. son concept normalise est distinct d'un simple changement de couleur, taille
   ou quantite ;
3. une recherche AliExpress officielle read-only retourne un listing
   semantiquement pertinent, avec un prix, un ID et une URL stables ; le statut
   distingue les listings deja qualifies par note/commandes de ceux qui restent
   a verifier ;
4. son mot-cle produit est transactionnel. Le volume PDP peut etre faible, mais
   il ne doit pas etre invente et sa page doit etre rattachee a une collection
   mesurable ;
5. une revue humaine exhaustive confirme la correspondance entre le mot-cle,
   le titre du listing et la fonction du produit ;
6. la niche atteint au moins 30 000 recherches mensuelles commerciales propres
   en France, avec les seuils de collections Kraken documentes separement.

Les donnees de recherche fournisseur sont des preuves de listing, pas une
validation automatique du SKU exact, du fret, de la conformite ou des
economics. Ces niveaux restent distincts dans le classeur final.

## Entrees concurrentielles

- `competitor-profiles/workstreams/catalogue-expansion-chien-aquarium.json`
- `competitor-profiles/workstreams/catalogue-expansion-mercerie-scrap.json`
- `competitor-profiles/workstreams/catalogue-expansion-perles.json`

## Sorties attendues

- `competitor-concepts-merged.json` : concepts valides et de-dupliques ;
- `competitor-concepts-validation.json` : rejets et alertes ;
- `aliexpress-concept-search.json` : reponses API brutes par concept ;
- `catalogue-sourced.json` : correspondances fournisseur retenues ;
- `aliexpress-anchor-search.json` : recherches API bilingues par ancre SEO ;
- `aliexpress-anchor-candidates.json` : listings de complément qualifiés ;
- `keyword-volumes-fr.json` : volumes SEMrush France et statut de preuve ;
- `final-catalogue.json` : candidats machine avant revue humaine ;
- `manual-audit-summary.json` : synthese des decisions humaines et rejets ;
- `final-catalogue-reviewed.json` : seules les PDP acceptees, avec mots-cles,
  volumes, liens, statut fournisseur et motif de validation ;
- `final-catalogue-gate-report.json` : contrôle déterministe du gate final ;
- `rapport-qualification.md` et classeur final vérifié.

## Reproduction

```bash
python3 merge_competitor_concepts.py
python3 build_keyword_volume_bank.py
python3 source_aliexpress_catalogue.py --workers 6 --limit 20 --resume
python3 collect_anchor_suppliers.py --workers 6 --limit 20
python3 compose_final_catalogue.py
python3 apply_manual_audits.py
python3 validate_final_catalogue.py
python3 build_qualification_report.py
node build_final_workbook.mjs
```

Le generateur decouvre `artifact-tool` dans le runtime Codex de l'utilisateur.
Sur une autre installation, definir `CODEX_ARTIFACT_TOOL_PATH` avec le chemin
absolu de `artifact_tool.mjs` avant de relancer le build.

Les trois fichiers `manual-audit-final-*.json` sous
`competitor-profiles/workstreams/` sont des entrees obligatoires entre la
composition machine et l'application des decisions. Toute nouvelle collecte
doit etre relue avant d'entrer dans `final-catalogue-reviewed.json`.

Les URLs signées, tokens, cookies et secrets ne sont jamais écrits dans le run.
Les réponses API conservées ne contiennent que les données commerciales
nécessaires à l'audit.

Mode strictement read-only : aucune mutation Shopify, DSers, GMC ou Google Ads.

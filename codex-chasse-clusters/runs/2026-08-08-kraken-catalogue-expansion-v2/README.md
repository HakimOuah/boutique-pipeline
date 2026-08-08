# Run Kraken catalogue expansion v2 — archive d'audit

Objectif historique : reconstruire cinq catalogues depuis les produits et
collections observés chez les concurrents, puis relire chaque équivalent
AliExpress et chaque mot-clé France.

**Statut au 2026-08-08 :** les fichiers et le classeur restent des preuves
auditables, mais le gate de comptage V2 est **supplanté** pour les futurs
catalogues par [`GATE-V3-CATALOGUE-SOURCING.md`](../../GATE-V3-CATALOGUE-SOURCING.md).
Les 212 produits acceptés forment une bibliothèque de départ ; les déficits V2
ne prouvent pas un manque de profondeur du marché.

## Pourquoi le gate V2 est archivé

V2 exigeait presque systématiquement un équivalent concurrent, un listing
AliExpress pertinent et un volume PDP strictement positif. La Méthode Kraken
valide d'abord les catégories, place 10–20 produits dans chaque sous-catégorie
et laisse la data révéler les références fortes. Elle autorise aussi des mots-
clés descriptifs à volume zéro lorsqu'ils précisent une collection mesurée.

Le gate actif conserve les contrôles utiles de V2 — concept distinct, listing
réel et revue humaine — mais :

1. porte la preuve de demande au niveau de la niche et des collections ;
2. n'exige pas de jumeau concurrent par produit ;
3. accepte un volume PDP égal à zéro sans l'inventer ;
4. vise 200 produits sur la boutique entière et 10–20 par sous-catégorie ;
5. interdit tout sourcing avant un verdict favorable de l'étude concurrentielle profonde.

Les données fournisseur restent des preuves de listing, pas une validation du
SKU exact, du fret, de la conformité ou de l'économie.

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

## Reproduction historique

Ces commandes reproduisent V2 ; elles ne constituent pas le pipeline actif du
gate V3 et ne doivent pas être relancées sur une niche `STOP` ou
`SUSPENDU_PHASE_2`.

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

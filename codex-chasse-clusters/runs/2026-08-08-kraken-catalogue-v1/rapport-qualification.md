# Rapport de qualification — cinq niches Kraken catalogue-volume

- Date : 8 août 2026
- Marché : France
- Run : `2026-08-08-kraken-catalogue-v1`

## Verdict exécutif

Cinq niches atteignent le seuil de demande de la méthode Kraken après nettoyage des expressions ambiguës. Elles restent toutes en **GO conditionnel** : le marché et la profondeur catalogue sont prouvés, mais l'économie SKU par SKU, la conformité et la validation fournisseur complète ne le sont pas encore.

| Rang | Niche | Volume mensuel FR nettoyé | Volume brut ciblé | Trends directionnel | IDs AliExpress | Pertinence moyenne/élevée | Verdict |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Balade, transport & mobilité du chien | 81 860 | 81 860 | +2,8 % | 118 | 88 | GO conditionnel |
| 2 | Mercerie créative & arts du fil | 221 680 | 221 680 | -23,5 % | 129 | 91 | GO conditionnel |
| 3 | Scrapbooking & journaling | 64 740 | 135 140 | -5,9 % | 125 | 84 | GO conditionnel |
| 4 | Perles & création de bijoux | 35 770 | 47 870 | -6,8 % | 130 | 109 | GO conditionnel, sous la zone de confort 40 k |
| 5 | Aquariophilie & aquascaping | 48 320 | 122 320 | -17,3 % | 130 | 88 | GO conditionnel |

Les variations Trends comparent les 52 points récents aux 52 points initiaux disponibles dans la représentation accessible du graphique. Elles sont des signaux relatifs, pas des volumes.

## Nettoyage des volumes

- Mercerie : union des termes produits et des familles couture, broderie, crochet, tricot, patchwork, macramé et punch needle.
- Scrapbooking : retrait de `album photo` (60 500) et `sticker` (9 900), trop larges pour prouver seuls la niche ; dédoublonnage de `washi tape`.
- Aquariophilie : retrait de `aquarium` (74 000), trop large et non nécessaire pour franchir le seuil.
- Chien : somme des familles promenade, transport, mobilité et sécurité ; aucun head term ambigu ajouté.
- Bijoux : retrait de `perle` au singulier (12 100), partagé avec l'intention bijou fini. Le cluster reste à 35 770, donc au-dessus du minimum 30 k mais sous la zone de confort 40 k.

Les totaux restent des sommes d'expressions exactes distinctes, pas des utilisateurs dédupliqués.

## Lecture par niche

### 1. Balade, transport & mobilité du chien

- Force : 73 130 recherches sur les seuls mots-clés produits initiaux ; `harnais chien` atteint 22 200.
- SERP : Shopping, spécialistes et comparateurs sur `harnais chien` et `sac transport chien`.
- Catalogue : 118 IDs uniques après dédoublonnage.
- Risque : résistance, tailles, charge, voiture et flottabilité. La première vague doit favoriser les accessoires non critiques ; les produits de sécurité passent dans une validation séparée.

### 2. Mercerie créative & arts du fil

- Force : profondeur sémantique et assortiment très supérieurs au seuil ; nombreuses collections cœur au-dessus de 1 000.
- SERP : Rascol, Craftine, Atelier de la Création et autres merceries spécialisées.
- Catalogue : 129 IDs uniques.
- Risque : concurrence installée et besoin d'un angle clair. Recommandation : kits débutants, filtres techniques, accessoires de couture et arts du fil plutôt qu'un catalogue de tissus génériques.

### 3. Scrapbooking & journaling

- Force : 64 740 recherches même après retrait des deux termes les plus ambigus ; tendance relativement stable.
- SERP : mix marchand/informationnel, avec Shopping et spécialistes sur les sous-collections.
- Catalogue : 125 IDs uniques.
- Risque : personnages et motifs sous licence, bruit API et produits chimiques légers. Les lignes de pertinence faible sont explicitement signalées dans le classeur.

### 4. Perles & création de bijoux

- Force : assortiment profond, intérêt Trends élevé et relativement stable ; 109 listings classés de pertinence moyenne ou élevée.
- SERP : Perles&Co, Perles à Tout Va et spécialistes DIY.
- Catalogue : 130 IDs uniques.
- Risque : composition, nickel/plomb/cadmium, petites pièces, pierres naturelles et confusion avec le bijou fini. Interdiction d'alléguer une matière sans document fournisseur.

### 5. Aquariophilie & aquascaping

- Force : 48 320 recherches sans compter le head term `aquarium` ; intention très marchande sur filtres, pompes et entretien.
- SERP : Shopping, marques techniques et boutiques spécialisées.
- Catalogue : 130 IDs uniques.
- Risque : électricité, étanchéité, CO2 et bien-être animal. La première vague recommandée est non électrique ; pompes, chauffages et LED nécessitent une gate conformité renforcée.

## Sourcing AliExpress

- 100 requêtes lancées via AliExpress Open Platform / AE-Dropshipper sur le VPS autorisé.
- Destination : France ; tri : commandes ; mode : lecture seule.
- 970 retours de recherche avant dédoublonnage ; 632 candidats sélectionnés dans le classeur.
- 460 candidats ont une pertinence lexicale moyenne ou élevée ; 172 restent marqués `À_VÉRIFIER_PERTINENCE`.
- Les statuts `API_SEARCH_MATCH` prouvent l'existence du listing au moment du contrôle. Ils ne valident ni la variante, ni la conformité, ni la livraison durable.
- Un produit représentatif par niche a été contrôlé jusqu'au SKU exact, au stock et au fret France : 5/5 probes réussis.

## Réserve écartée du top 5

Le cake design atteint environ 34 k recherches en union de termes, mais reste plus faible que les cinq retenues : baisse Trends d'environ 32,8 %, exposition au contact alimentaire et profondeur sémantique propre moins confortable. Il reste un vivier de second rang, pas une recommandation de cette salve.

## Ce qui manque avant une boutique ou un import

1. Shortlist humaine de 20 à 30 produits par niche en supprimant le bruit API.
2. Variante exacte, stock, coût rendu France et délai pour chaque SKU shortlisté.
3. Prix de vente, marge contributive, CPA maximal et budget test.
4. Documents de conformité adaptés à la niche.
5. Contrôle des marques, licences, photos, matériaux et promesses.

Aucune création Shopify, import DSers, activation GMC ou dépense Google Ads n'a été effectuée.

## Livrables

- Classeur : `../../outputs/2026-08-08-kraken-catalogue-v1/5-niches-kraken-france-2026-08-08.xlsx`
- Résultats API : `aliexpress-search-results.json`
- Catalogue dédoublonné : `curated-products.json`
- Probes exacts : `representative-exact-probes.json`
- Scripts reproductibles : `collect_aliexpress.py`, `curate_products.py`, `probe_representatives.py`, `build_workbook.mjs`

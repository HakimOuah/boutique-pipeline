# Salve Kraken catalogue-volume — 8 août 2026

Cette exécution qualifie cinq niches France et prépare une première arborescence de 100 à 150 références par niche.

## Périmètre

- SEMrush France : volumes exacts observés le 8 août 2026.
- Google : contrôle de dix SERP commerciales et présence de Shopping/boutiques spécialisées.
- Google Trends : comparaison France sur cinq ans, utilisée comme signal directionnel et non comme volume absolu.
- AliExpress Open Platform : recherche read-only via le VPS autorisé ; aucune mutation Shopify, DSers, GMC ou Google Ads.

## Niveau de preuve AliExpress

`API_SEARCH_MATCH` signifie qu'un listing a été renvoyé par l'API au moment de la collecte. Ce statut ne valide pas encore la variante exacte, la conformité, la disponibilité durable ni le fret France. Les liens sont fournis pour contrôle humain avant toute sélection commerciale.

## Extension concurrentielle

La seconde passe croise 31 domaines publics, 20 marques BrandSearch, 15 domaines SEMrush France et cinq banques/ensembles VOC. Elle ajoute :

- `../../../competitor-profiles/etude-concurrentielle-5-niches-2026-08-08.md` — synthèse et priorités ;
- `build_competitor_workbook.mjs` — construction reproductible du classeur enrichi ;
- `verify_competitor_workbook.mjs` — réimport, rendu des 11 onglets et scan d'erreurs ;
- `../../outputs/2026-08-08-kraken-concurrence-v1/5-niches-kraken-etude-concurrentielle-2026-08-08.xlsx` — catalogue initial + concurrence, SEMrush, personas et différenciation.

Un seul acteur est classé `PROBABLE_DROPSHIP` à confiance moyenne : Boutiquechien.fr. Aucun fournisseur n'est prouvé. Shopify reste un indice technique, jamais une preuve.

## Architecture SEO ajoutée le 8 août 2026

Le classeur sépare désormais trois niveaux qui ne doivent pas être confondus :

- `Arborescence` : 5 pages d'accueil et 38 collections SEO alimentées, chacune reliée à un mot-clé business et à son volume SEMrush France ;
- `Produits SEO` : 170 candidats PDP stricts, soit 13 à 76 par niche, avec le mot-clé produit et son volume immédiatement à côté du titre ;
- `Fournisseurs candidats` : les 632 annonces AliExpress d'origine, conservées pour la traçabilité et le contrôle.

Les collections autonomes sont limitées aux expressions à partir de 300 recherches mensuelles : cœur à partir de 1 000, secondaire entre 500 et 999, tolérance entre 300 et 499. Les expressions sous 300 restent au niveau PDP et sont rattachées à une collection plus large. Le gate produit a écarté 7 annonces à volume nul, 454 annonces de pertinence lexicale insuffisante et un doublon de titre exact.

Chaque titre produit SEO commence par son mot-clé mesuré, puis reprend un descripteur factuel du listing fournisseur. Ce mapping ne vaut pas validation d'import : la déduplication sémantique, la variante exacte, le fret France, la conformité et les economics restent obligatoires. Le quota souhaité de 100 à 150 produits par niche n'est donc pas considéré atteint : il faut relancer un sourcing plus précis sur les familles déficitaires, sans réintroduire les faux positifs.

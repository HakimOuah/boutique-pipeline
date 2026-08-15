# Snapshot public — sitemap et taxonomie L'Antre Gothique

- Capture : 2026-08-15
- Domaine : https://antregothique.com/
- Méthode : `robots.txt`, sitemap Shopify public, endpoints publics de métadonnées de collection
- Limite : les collections se recouvrent ; leurs compteurs ne doivent jamais être additionnés pour obtenir des produits uniques

## URLs sources

- https://antregothique.com/robots.txt
- https://antregothique.com/sitemap.xml
- https://antregothique.com/sitemap_products_1.xml?from=4012558516323&to=4496519463011
- https://antregothique.com/sitemap_products_2.xml?from=4496519692387&to=14790498156870
- https://antregothique.com/sitemap_products_3.xml?from=14790507233606&to=15676312551750
- https://antregothique.com/sitemap_collections_1.xml?from=141743751267&to=669697048902
- https://antregothique.com/sitemap_pages_1.xml?from=44581716067&to=174101987654

## OBSERVÉ — compteurs sitemap

| Type | Nombre d'entrées `<url>` |
|---|---:|
| Produits, sitemap 1 | 1 001 |
| Produits, sitemap 2 | 999 |
| Produits, sitemap 3 | 341 |
| **Produits, total sitemap** | **2 341** |
| Collections | **75** |
| Pages | **10** |

Le total 2 341 est un nombre d'URL produit canoniques exposées par les sitemaps au moment de la lecture. Ce n'est ni un stock disponible, ni un nombre de ventes, ni une preuve de concepts réellement distincts.

## OBSERVÉ — 75 collections du sitemap

### Femme / habillement

`vetements-gothiques-femmes`, `robe-gothique`, `t-shirt-gothique`, `jupes-gothique`, `corset-gothique`, `leggings-gothique`, `veste-gothique-femme`, `pantalon-gothique-femme`, `maillot-de-bain-gothique`, `collant-gothique`, `gant-gothique`, `lingerie-gothique`, `manteau-gothique`, `body-gothique`, `chemise-blouse-gothique-femme`, `debardeur-camisole-gothique`, `t-shirt-gothique-femme`, `crop-top-gothique`, `manteau-gothique-femme`, `shorts-gothiques-femmes`.

### Homme / habillement général

`vetements-gothiques-homme`, `t-shirt-gothique-homme`, `pull-gothique`, `veste-gothique-homme`, `sweat-gothique`, `chemise-gothique-homme`, `pantalon-gothique`, `manteau-gothique-homme`, `vetement-gothique`, `sous-vetements-gothiques`, `pyjama-gothique`.

### Bijoux

`bijoux-gothique`, `bracelet-gothique`, `boucle-d-oreille-gothique`, `collier-gothique`, `bague-gothique`, `pendentif-gothique`, `collier-ras-de-cou-gothique`, `piercing-gothique`, `montre-gothique`.

### Sacs et accessoires

`sac-main-gothique`, `sac-gothique`, `sac-a-dos-gothique`, `accessoires-gothiques`, `ceinture-gothique`, `harnais-gothique`, `masque-gothique`, `sacoche-gothique`, `accessoires-de-cheveux-gothique`, `parapluie-gothique`, `chapeau-gothique`, `portefeuilles-gothique`, `tatouages-gothiques`, `foulards-et-cravates-gothiques`, `lunette-de-soleil-gothique`, `peluche-gothique`.

### Chaussures

`chaussure-gothique`, `botte-gothique`, `chaussure-a-talons-gothique`, `chaussure-creepers`, `ballerine-gothique`, `basket-gothique`, `sandale-gothique`.

### Décoration / maison / occultisme

`decoration-gothique`, `decoration-gothique-murale`, `statues-et-figurines-gothiques`, `art-occulte`, `autel-gothique`, `bougeoirs-et-bougies-gothiques`, `maison`.

### Merchandising transversal

`promotion`, `les-meilleurs-produits-gothiques-du-moment`, `nouveautes-gothique`, `cosplay`, `outlet`.

## OBSERVÉ — familles à profondeur indicative élevée

Les endpoints publics `https://antregothique.com/collections/<handle>.json` exposaient :

| Collection | `products_count` public |
|---|---:|
| Vêtements gothiques femmes | **1 077** |
| Accessoires gothiques | **375** |
| Bijoux gothiques | **341** |
| Vêtements gothiques homme | **316** |
| Haut gothique femme (`t-shirt-gothique`) | **201** |
| Robe gothique | 187 |
| Chaussures gothiques | 165 |
| Sacs gothiques | 165 |
| Jupes gothiques | 129 |
| Sweat gothique | 105 |
| Bague gothique | 94 |
| Pantalon gothique femme | 88 |
| Lingerie gothique | 77 |
| Décoration gothique | 72 |
| Manteau gothique | 70 |
| Bottes gothiques | 59 |
| Cosplay | 58 |
| Maison | 55 |
| Corset gothique | 53 |
| Statues et figurines gothiques | 20 |
| Peluche gothique | 18 |
| Art occulte | 16 |
| Décoration murale gothique | 14 |
| Bougeoirs et bougies gothiques | 9 |

Les compteurs de métadonnées ont parfois dépassé le nombre de produits retournés par l'endpoint paginé public. Ils sont donc conservés comme **profondeur indicative du catalogue publié**, pas comme inventaire exact disponible.

## MANQUANT

- Déduplication des 2 341 URL en concepts visuellement distincts.
- Disponibilité effective par taille/pointure et pays.
- Part des produits présents dans plusieurs collections.
- Produits archivés, masqués ou indisponibles non représentés dans le storefront.

# Moment Ici — snapshot public catalogue

**Lecture :** 2026-08-15

**Mode :** pages publiques, sitemap Shopify et endpoints catalogue publics ; aucune connexion, panier, commande ou mutation.

## Sources interrogées

- https://momentici.com/
- https://momentici.com/robots.txt
- https://momentici.com/sitemap.xml
- https://momentici.com/sitemap_products_1.xml?from=16015746629977&to=16016067789145
- https://momentici.com/sitemap_products_2.xml?from=16016067821913&to=16181258092889
- https://momentici.com/sitemap_products_3.xml?from=16181258289497&to=16406508241241
- https://momentici.com/sitemap_collections_1.xml?from=686925381977&to=706307391833
- https://momentici.com/sitemap_pages_1.xml?from=705645347161&to=719549890905
- https://momentici.com/sitemap_blogs_1.xml
- https://momentici.com/products.json?limit=250&page={1..12}
- https://momentici.com/collections/{handle}/products.json?limit=250&page={n}

## OBSERVÉ — taille des index publics

| Surface | Compte observé | Note |
|---|---:|---|
| Produits dans les trois sitemaps FR | 2 344 | 2 345 entrées `<url>`, dont la racine du site dans le premier sitemap |
| Produits retournés par `products.json` | 2 344 | 12 pages demandées, 10 utiles |
| Collections dans le sitemap FR | 276 | Taxonomies fortement croisées |
| Pages éditoriales / service | 22 | FAQ, histoire, guides, garantie, retours, origine, revendeurs, etc. |
| Entrées du sitemap blogs FR | 305 | Inclut les racines de blog et les articles |
| Compteur public indexé sur `/collections/all` | 2 352 | Capture moteur récente, distincte des deux comptes live ci-dessus |

Les deux surfaces live convergent donc sur 2 344 produits. Le compteur indexé à 2 352 peut refléter un écart de cache, une publication récente ou une inclusion différente. Le compte exploité pour la distribution prix est **2 344**.

## OBSERVÉ — composition du catalogue live

Sur les 2 344 lignes produit retournées par l'endpoint public :

| `product_type` | Produits | Part |
|---|---:|---:|
| `Bijoux` | 2 115 | 90,2 % |
| `Décoration` | 180 | 7,7 % |
| Vide | 49 | 2,1 % |

Le champ public `vendor` contient seulement deux graphies de la marque : `Momentici` sur 1 862 produits et `Moment Ici` sur 482. Ces valeurs ne sont **pas** des preuves de fabricant ou de fournisseur.

## OBSERVÉ — profondeur de collections

Les comptes ci-dessous proviennent des endpoints publics de collections le 2026-08-15. Les collections se chevauchent : un même produit peut être femme, améthyste, bague et mauvais œil.

| Collection | Produits live |
|---|---:|
| Bijoux femme | 1 775 |
| Bijoux homme | 320 |
| Décorations | 184 |
| Bijoux pierre améthyste | 108 |
| Arbre de vie en pierres naturelles | 64 |
| Bijoux mauvais œil | 55 |
| Bijoux personnalisés | 25 |
| Bijoux astrologie | 2 |

Le sitemap de 276 collections contient notamment **98 handles** avec `bijoux-pierre`, **64** avec `bijoux-symbole`, 22 avec `bracelet`, 13 avec `bague`, 13 avec `collier`, 12 avec `boucles-d`, 31 avec `homme`, 39 avec `femme`, 8 avec `cadeau` et 3 avec `personnalise`. Ces comptes de handles sont descriptifs et non exclusifs.

### Axes de navigation observés

- Type de bijou : bague, bracelet, collier, boucles d'oreilles, accessoires.
- Pierre : améthyste, quartz rose, jade, labradorite, œil de tigre, obsidienne, pierre de lune, turquoise et des dizaines d'autres.
- Symbole : arbre de vie, mauvais œil, lune/étoile, soleil, infini, main de Fatma, trèfle, dragon, serpent, viking, etc.
- Destinataire : femme, homme, enfant, couple, mère-fille.
- Cadeau : destinataire, Saint-Valentin, fêtes, Noël et bandes de prix.
- Maison/méditation : arbres de vie, attrape-rêves, capteurs de soleil, orgonites, bols chantants, encensoirs et pierres/minéraux.

## OBSERVÉ — prix live exhaustifs

Méthode : prix minimum de variante de chacun des 2 344 produits publics, en EUR. Cette distribution inclut les accessoires et lignes techniques ; elle ne représente ni prix livré ni marge.

| Indicateur | Valeur |
|---|---:|
| Minimum | 1,00 € |
| Médiane | 39,00 € |
| Maximum du prix minimum de variante | 289,00 € |
| Sous 15 € | 9 / 2 344, soit 0,4 % |
| Sous 30 € | 623 / 2 344, soit 26,6 % |

| Bande | Produits | Part |
|---|---:|---:|
| <15 € | 9 | 0,4 % |
| 15–29,99 € | 614 | 26,2 % |
| 30–49,99 € | 1 071 | 45,7 % |
| 50–79,99 € | 482 | 20,6 % |
| ≥80 € | 168 | 7,2 % |

Le minimum à 1 € est une ligne `frais-supplementaire`. Les autres lignes sous 15 € incluent boîtes cadeau, certificat, colle et un porte-clés. Le cœur marchand n'est donc pas un catalogue de petits consommables.

Exemples observés : collier Main de Fatma 23 €, boucles pendantes améthyste 29 €, plateau mauvais œil 39 €, bague améthyste/citrine 99 €, arbres de vie 45–289 €, ensemble de sept bols chantants 257 €.

## OBSERVÉ — panier et service

- Livraison gratuite à partir de 59 € : https://momentici.com/policies/shipping-policy
- France annoncée à 4–7 jours ouvrés après préparation ; majorité des commandes annoncée préparée sous 24 h.
- Chaque bijou est placé dans une boîte ; des boîtes supplémentaires peuvent être ajoutées : https://momentici.com/pages/emballage-cadeau-pret-offrir
- Gravure annoncée sur une collection personnalisée et sur demande pour d'autres bijoux : https://momentici.com/pages/faq
- Garantie d'un an sur les bijoux et défauts de fabrication : https://momentici.com/pages/garantie-un-an
- Programme revendeur avec catalogue, tarifs de gros et best-sellers annoncés : https://momentici.com/pages/programme-revendeur

Avec une médiane à 39 €, deux produits médians atteignent 78 € et dépassent arithmétiquement le franco. Cela prouve une mécanique possible, pas l'AOV ni un taux d'attachement observé.

## MANQUANT

- Ventes, AOV, marge, conversion, réachat, retours réels et importance relative de chaque collection.
- Déduplication en concepts produit : 2 344 URLs ne signifient pas 2 344 designs distincts.
- Date homogène des compteurs rendus : certaines captures moteur affichent 2 352 produits et des campagnes déjà expirées.
- Fabricant, atelier et pays d'origine exacts par SKU ; le site cite des artisans dans plusieurs pays mais ne mappe pas les références.
- Vérification indépendante des pierres, certificats, labels, allégations artisanales, avis ou classement Trustpilot.

## HYPOTHÈSE

La profondeur de taxonomie suggère une stratégie SEO de longue traîne par croisement `type de bijou × pierre × genre × symbole × occasion`. Elle ne prouve ni trafic ni rentabilité de ces pages.

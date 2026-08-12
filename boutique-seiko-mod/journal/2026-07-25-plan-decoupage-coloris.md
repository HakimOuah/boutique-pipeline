# Plan de découpage des coloris — une fiche par modèle (25/07/2026)

Décisions Hakim du 25/07 : **ampleur maximale** (tous les coloris exploitables), **naming communautaire**, **remapping DSers fait par l'agent** depuis le navigateur. Contexte et chiffres : `2026-07-25-catalogue-v2-analyse-concurrents.md`.

## Principe

Chaque fiche fournisseur actuelle contient N coloris dans un menu déroulant. On la transforme en **N fiches produit nommées et photographiées**, en gardant les options techniques (mouvement, fond, diamètre) comme variantes de chaque nouvelle fiche.

**La fiche d'origine n'est pas supprimée** : elle devient la fiche du coloris n°1 (renommée), ce qui préserve son mapping DSers existant. On ne crée donc que N-1 fiches par famille.

Règles à respecter à la lettre :
- **SKU strictement identiques** à ceux d'aujourd'hui sur chaque variante recréée (c'est la chaîne d'attributs AliExpress, ex. `14:175#9;5:56964930#DG3804 GLASS back`) — c'est ce qui permettra l'auto-matching DSers.
- **Échelle de prix par mouvement/fond reconduite** telle qu'appliquée le 25/07 (base + 39 € Seiko, + 89 € PT5000, + 29 € fond verre) avec le prix barré du palier.
- Collection d'appartenance identique à la fiche mère, plus la collection « Les Montres ».
- Positionnement stérile inchangé : le nom décrit un **coloris**, jamais une marque, et les visuels ne portent aucun logo.

## Inventaire à découper

| Fiche mère | Option de coloris | Coloris | Fiches à créer | Options techniques conservées |
|---|---|---:|---:|---|
| Contre-la-montre — chrono panda | Référence M-1…M20 | 20 | 19 | aucune (mono-variante) |
| Voyageur — GMT | Référence 1-9 | 9 | 8 | mouvement DG3804/NH34 × fond |
| Noirmont Deux — plongeuse céramique | Référence 1-7 | 7 | 6 | Miyota / Mingzhu / NH35 / PT5000 |
| Trente-Neuf — cannelée | Cadran (7 couleurs) | 7 | 6 | mouvement × diamètre × fond |
| Intégrale — sport chic | Référence 1-7 | 7 | 6 | aucune |
| Trente-Six — jubilé | Cadran (6 couleurs) | 6 | 5 | diamètre × fond |
| Quarante-et-Un — sport acier | Cadran & bracelet | 4 cadrans | 3 | mouvement (+ bracelet acier/cuir en variante) |
| Héritage — plongeuse vintage | Référence S1-S3 | 3 | 2 | aucune |
| Trente-Neuf Duo — bicolore | Boîtier or rose / doré | 2 | 1 | mouvement × diamètre × fond |
| Noirmont Un — plongeuse | Boîtier acier / bronze | 2 | 1 | mouvement × fond |
| **Total** | | **67** | **57 nouvelles fiches** | |

Catalogue montres cible : **67 fiches** (contre 10 aujourd'hui), soit entre Goteia (34) et montreapapy (100).

## Vocabulaire communautaire — référence de nommage

À utiliser pour nommer les coloris une fois identifiés visuellement. Le surnom décrit une combinaison de couleurs, il est utilisé tel quel par toute la communauté horlogère (et par les deux concurrents FR).

**GMT — lunettes bicolores**
| Surnom | Lunette |
|---|---|
| Pepsi | bleu / rouge |
| Coke | noir / rouge |
| Batman | bleu / noir |
| Batgirl | bleu / noir, monté sur jubilé |
| Sprite | vert / noir |
| Root Beer | marron / or |
| Full Black | noir intégral |

**Plongeuses**
| Surnom | Description |
|---|---|
| Hulk | cadran vert + lunette verte |
| Kermit | cadran noir + lunette verte (insert alu) |
| Starbucks | cadran noir + lunette verte céramique |
| Smurf | cadran bleu + lunette bleue |
| Bluesy | bicolore acier-or, cadran bleu |
| Comex | plongeuse pro, cadran outil |

**Chronographes**
| Surnom | Description |
|---|---|
| Panda | cadran blanc, compteurs noirs |
| Panda Inversé | cadran noir, compteurs blancs |
| Root Beer | cadran brun / or |

**Classiques (Datejust)**
| Surnom | Description |
|---|---|
| Wimbledon | cadran ardoise dégradé, chiffres romains |
| Tapisserie | cadran à motif gaufré |

Pour les familles sans surnom établi (sport chic, bicolore, vintage), on nomme par la couleur dominante dans le style maison : « Vert Jura », « Bleu Nuit », « Champagne », « Glacier ».

## ⚡ Les images de variante — même jeu d'assets, valeur immédiate (remonté par Hakim le 25/07)

Constat de Hakim sur la PDP : **cliquer sur « Doré » ou « Rose » ne change pas l'image**. Le client choisit une couleur de cadran sans jamais voir le résultat — c'est un tueur de conversion sur une montre à 300 €.

**Le point clé : c'est exactement le même besoin d'images que le découpage.** Les 67 visuels de coloris servent aux deux usages :

| | Images de variante | Découpage en fiches |
|---|---|---|
| Assets nécessaires | les 67 mêmes | les 67 mêmes |
| Nouveaux produits | aucun | 57 |
| Remapping DSers | **aucun** | 57 fiches |
| Gain | l'image suit le choix client | catalogue + SEO longue traîne |
| Délai | immédiat | après création + mapping |

**Conclusion : on génère les 67 coloris UNE fois, on les branche d'abord en images de variante (gain immédiat, zéro risque), puis on réutilise exactement les mêmes fichiers pour les fiches du découpage.**

Mise en œuvre : `productVariantsBulkUpdate` accepte un `mediaId` par variante. On assigne l'image du coloris à **toutes** les variantes qui le partagent (ex. les 4 variantes « Doré » de la Trente-Six pointent sur le même média). Les options techniques (36/39 mm, fond verre/acier, mouvement) **n'ont pas besoin de visuel propre** — seule la couleur de cadran change à l'œil. C'est ce qui fait tomber le besoin de 214 variantes à 67 images.

⚠️ À vérifier en QA : que le thème FullStack bascule bien la galerie quand la variante sélectionnée porte un média.

## Séquence d'exécution

1. **Identification des coloris** (agent, navigateur) — rouvrir les fiches AliExpress d'origine, photographier la correspondance `référence fournisseur → coloris réel`, proposer un surnom par coloris. URL candidates dans `2026-07-24-arborescence-site.md` ; à confirmer par le nombre de variantes. Livrable : `mapping-coloris.json`.
2. **Validation du plan de nommage par Hakim** (une passe rapide sur la liste des 67 noms).
3. **Création des fiches** (API Shopify) : `productCreate` + `productVariantsBulkCreate` avec SKU identiques, prix du palier, collections, description reprise de la fiche mère et adaptée au coloris.
4. **Visuels** : 2 par fiche (face + porté), générés au coloris exact, avec la boucle anti-faux-logos habituelle. ~114 images — c'est le poste de coût principal.
5. **Remapping DSers** (agent, navigateur, autorisé par Hakim le 25/07) : My Products → chaque nouvelle fiche → Mapping → coller l'URL AliExpress de la fiche mère → vérifier l'auto-matching des variantes par SKU → enregistrer. **Contrôle obligatoire** : sur chaque fiche, vérifier qu'au moins une variante est bien liée et que le SKU affiché correspond, avant de passer à la suivante.
6. **QA** : une PDP par famille, mobile d'abord.

## Points de vigilance

- Ne jamais lancer l'étape 3 avant que le mapping des coloris soit validé : renommer 67 fiches après coup coûte plus cher que de bien nommer une fois.
- Le découpage multiplie les fiches sans multiplier le stock : la disponibilité réelle dépend toujours de la même fiche fournisseur. Si un coloris est en rupture chez le fournisseur, c'est une fiche entière qui devient indisponible — prévoir une surveillance.
- Les 20 références du chrono panda sont des cadrans très proches les uns des autres : il est probable qu'on n'en retienne que 10-12 réellement différenciés à l'œil. À trancher à l'étape 1 sur photos.

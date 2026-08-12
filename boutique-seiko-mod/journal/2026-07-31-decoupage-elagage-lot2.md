# Découpage & élagage — Lot 2 — 2026-07-25

Boutique **NOIRMONT** / Maison Noirmont (`v42pzp-h4`, maisonnoirmont.fr)
Application de la décision **« une variante = un produit »**, avec élagage là où la variante n'est qu'une dimension.

**41 fiches créées · 166 variantes supprimées · catalogue 44 → 85 fiches.**

---

## ⚠️ Le piège de cette passe — à lire avant toute reprise

**Rattacher une image existante à une nouvelle fiche en passant son URL CDN dans `originalSource` écrase
l'`alt` de la fiche d'origine.**

Shopify ne duplique pas le fichier : il reconnaît l'URL et **rattache le même objet `MediaImage`**.
Or `alt` est une propriété **du fichier**, pas du rattachement. Chaque création a donc réécrit l'`alt`
partagé — les 7 mères montres et accessoires ont vu leurs textes alternatifs remplacés par le titre de la
dernière fiche fille créée, et les descriptions par image ont été perdues.

```graphql
# ❌ écrase l'alt de la mère
files: [{ originalSource: "https://cdn.shopify.com/…/image.jpg", alt: "…" }]

# ✅ rattache sans toucher à l'alt
files: [{ id: "gid://shopify/MediaImage/59679727976786" }]
```

Conséquence à connaître : les fiches filles **partagent** le `MediaImage` de la mère. Supprimer une image
depuis une fille la retirerait aussi de la mère et des autres filles. Pour des médias réellement
indépendants, il faut **réuploader le fichier**, pas pointer l'URL existante.

Les 31 `alt` touchés ont été **réparés** (voir plus bas).

---

## Phase 0 — Sauvegarde (préalable bloquant)

`backup-variantes-avant-decoupage.json` — **175 Ko, 10 produits, 391 variantes**.
Par variante : `id`, **`sku`**, `price`, `compareAtPrice`, valeurs d'option, `inventoryPolicy`,
`inventoryQuantity`. Par produit : titre, handle, statut, vendor, type, tags, collections, options.

Contrôles passés **avant** toute suppression :

- relecture indépendante du fichier écrit : 391 ids uniques, aucun SKU vide, `variantsCount` == nombre de variantes sur les 10 produits ;
- pour le FKM tropical (252 variantes), la grille **36 couleurs × 7 largeurs** vérifiée complète et sans doublon ;
- 12 SKU tirés au hasard dans le bloc FKM reconstruit, **recomparés à la boutique** : 12/12 identiques.

Deux produits volontairement **hors sauvegarde car non touchés** : Noirmont Deux (`10977448624466`) et
Bracelet FKM embouts courbes (`10977445151058`).

---

## Phase 1 — Découpage (additif) — 41 fiches, 89 variantes

**Principe appliqué, validé en cours de mission : on ne supprime jamais une valeur pour réduire un nombre de
fiches.** Deux valeurs trop proches pour mériter deux pages cohabitent sur une même fiche via une option
secondaire. Le nombre de fiches est un objectif de présentation, jamais une raison de perdre un SKU —
supprimer une variante détruit son mapping DSers de façon irréversible.

**Contrôle global fait sans se fier aux rapports des agents** : les 89 variantes créées reprennent **chaque
SKU de la sauvegarde exactement une fois**, prix et prix barrés conformes.
101 variantes mères − 12 « siglé » exclues = **89**. ✅

### Contre-la-montre — chronographe (mère `10977444528466`, 20 cadrans → 12 fiches, 20 SKU conservés)

Les quasi-doublons ont été **fusionnés**, pas écartés.

| Titre | Handle | ID | Var. | Regroupement |
|---|---|---|---:|---|
| Contre-la-montre Blanc — Chronographe | `contre-la-montre-blanc-chronographe` | 10980078879058 | 3 | compteurs cerclés · compteurs gris · ton sur ton |
| Contre-la-montre Panda inversé — Chronographe | `contre-la-montre-panda-inverse-chronographe` | 10980080419154 | 2 | aiguille acier · aiguille rouge |
| Contre-la-montre Champagne — Chronographe | `contre-la-montre-champagne-chronographe` | 10980080779602 | 2 | bracelet acier · caoutchouc |
| Contre-la-montre Panda — Chronographe | `contre-la-montre-panda-chronographe` | 10980080976210 | 2 | blanc caoutchouc · ivoire acier |
| Contre-la-montre Noir — Chronographe | `contre-la-montre-noir-chronographe` | 10980081041746 | 2 | lunette lisse · tachymètre inscrit |
| Contre-la-montre Turquoise — Chronographe | `contre-la-montre-turquoise-chronographe` | 10980081533266 | 2 | ton sur ton · compteurs noirs |
| Contre-la-montre Vert — Chronographe | `contre-la-montre-vert-chronographe` | 10980081631570 | 2 | caoutchouc vert · acier |
| Contre-la-montre Rose poudré — Chronographe | `contre-la-montre-rose-poudre-chronographe` | 10980081762642 | 1 | — |
| Contre-la-montre Gris anthracite — Chronographe | `contre-la-montre-gris-anthracite-chronographe` | 10980081926482 | 1 | — |
| Contre-la-montre Argent — Chronographe | `contre-la-montre-argent-chronographe` | 10980082778450 | 1 | — |
| Contre-la-montre Compteurs bleus — Chronographe | `contre-la-montre-compteurs-bleus-chronographe` | 10980083007826 | 1 | — |
| Contre-la-montre Bleu glacier — Chronographe | `contre-la-montre-bleu-glacier-chronographe` | 10980083138898 | 1 | — |

### Voyageur — GMT (mère `10977448657234`, 6 déclinaisons vendables, 24 variantes)

⛔ **Aucune fiche créée pour les 3 boîtiers « siglé »** (logo de marque tierce). Leurs 12 SKU n'apparaissent
nulle part dans les fiches créées — vérifié par intersection d'ensembles. Ils restent sur la mère seule,
en `DENY` / stock 0.

| Titre | Handle | ID | Var. |
|---|---|---|---:|
| Voyageur Or — GMT bracelet 3 maillons | `voyageur-or-gmt-3-maillons` | 10980078780754 | 4 |
| Voyageur Or — GMT bracelet Président | `voyageur-or-gmt-president` | 10980079042898 | 4 |
| Voyageur Bicolore — GMT bracelet 3 maillons | `voyageur-bicolore-gmt-3-maillons` | 10980080845138 | 4 |
| Voyageur Bicolore — GMT bracelet 5 maillons | `voyageur-bicolore-gmt-5-maillons` | 10980081107282 | 4 |
| Voyageur Or rose — GMT bracelet 5 maillons | `voyageur-or-rose-gmt-5-maillons` | 10980081402194 | 4 |
| Voyageur Bicolore cadran brun — GMT automatique | `voyageur-bicolore-cadran-brun-gmt` | 10980081664338 | 4 |

Chaque fiche conserve l'option technique `Mouvement & fond` (DG3804/NH34 × fond verre/acier).

### Intégrale — sport chic (mère `10977444561234`, 7 fiches)

| Titre | Handle | ID | Var. |
|---|---|---|---:|
| Intégrale Vert — Sport chic acier | `integrale-vert-sport-chic-acier` | 10980078911826 | 1 |
| Intégrale Brun or rose — Sport chic | `integrale-brun-or-rose-sport-chic` | 10980079075666 | 1 |
| Intégrale Turquoise — Sport chic acier | `integrale-turquoise-sport-chic-acier` | 10980080714066 | 1 |
| Intégrale Noir — Sport chic acier | `integrale-noir-sport-chic-acier` | 10980080877906 | 1 |
| Intégrale Bleu nuit — Sport chic acier | `integrale-bleu-nuit-sport-chic-acier` | 10980081074514 | 1 |
| Intégrale Bleu ciel — Sport chic acier | `integrale-bleu-ciel-sport-chic-acier` | 10980081205586 | 1 |
| Intégrale Blanc argenté — Sport chic acier | `integrale-blanc-argente-sport-chic-acier` | 10980081336658 | 1 |

### Héritage — plongeuse vintage (mère `10977444594002`, 3 fiches)

| Titre | Handle | ID | Var. |
|---|---|---|---:|
| Héritage Bleu — Plongeuse vintage 42 | `heritage-bleu-plongeuse-vintage-42` | 10980082843986 | 1 |
| Héritage Bleu nuit — Plongeuse vintage 42 | `heritage-bleu-nuit-plongeuse-vintage-42` | 10980084220242 | 1 |
| Héritage Vert — Plongeuse vintage 42 | `heritage-vert-plongeuse-vintage-42` | 10980084515154 | 1 |

### Remontoir Bois (mère `10977444659538`, 4 fiches, 8 SKU conservés)

**Arbitrage documenté et validé.** Le brief annonçait « chaque valeur est un bois distinct » ; en réalité les
8 valeurs sont **4 essences × 2 capacités**. Règle appliquée, celle énoncée pour le Remontoir Collection :
la finition est un modèle, la capacité est un choix.

| Titre | Handle | ID | Var. |
|---|---|---|---:|
| Remontoir Bois Noir laqué | `remontoir-bois-noir-laque` | 10980082745682 | 2 |
| Remontoir Bois Acajou | `remontoir-bois-acajou` | 10980082909522 | 2 |
| Remontoir Bois Ébène | `remontoir-bois-ebene` | 10980083106130 | 2 |
| Remontoir Bois Noyer | `remontoir-bois-noyer` | 10980083269970 | 2 |

### Rouleau de Voyage (mère `10977444823378`, 4 fiches par couleur de cuir, capacité en variante)

| Titre | Handle | ID | Var. |
|---|---|---|---:|
| Rouleau de Voyage Noir — cuir | `rouleau-de-voyage-noir-cuir` | 10980083171666 | 3 |
| Rouleau de Voyage Brun — cuir | `rouleau-de-voyage-brun-cuir` | 10980083401042 | 3 |
| Rouleau de Voyage Bleu marine — cuir | `rouleau-de-voyage-bleu-marine-cuir` | 10980083564882 | 3 |
| Rouleau de Voyage Vert — cuir | `rouleau-de-voyage-vert-cuir` | 10980083859794 | 3 |

### Remontoir Collection (mère `10977444757842`, 5 fiches, capacité en variante)

Consigne : ne pas découper en 15, découper par couleur et garder la capacité en variante.
Les 15 valeurs se répartissent en **5** aspects de coffret (et non 3-4) — d'où 5 fiches et non 4.

| Titre | Handle | ID | Var. |
|---|---|---|---:|
| Remontoir Collection Bois noir | `remontoir-collection-bois-noir` | 10980083466578 | 4 |
| Remontoir Collection Bois beige | `remontoir-collection-bois-beige` | 10980083728722 | 4 |
| Remontoir Collection Bois LED noir | `remontoir-collection-bois-led-noir` | 10980084056402 | 2 |
| Remontoir Collection Bois LED rouge | `remontoir-collection-bois-led-rouge` | 10980084121938 | 2 |
| Remontoir Collection Cuir PU | `remontoir-collection-cuir-pu` | 10980084449618 | 3 |

### Paramètres appliqués

`status ACTIVE` · vendor, productType, tags et collections repris de la mère · publication sur les 3 canaux
(Boutique en ligne, Point de vente, Shop) · description = paragraphe propre au coloris + description de la
mère · **aucune fiche dans `frontpage`** (vérifié : la collection Page d'accueil contient toujours 1 produit).

### Intégrité des mères

Les 7 mères relues après opération : **nombre de variantes, SKU et options inchangés**. Aucune mutation ne
leur a été adressée. Noirmont Deux (`10977448624466`) n'a **pas** été touchée : 28 variantes, ses 7
« Référence » intactes, conformément à la consigne.

---

## Phase 2 — Élagage (destructif)

Réalisé **après** la sauvegarde et sa relecture. Méthode : `productVariantsBulkDelete`.
Après chaque suppression, le produit a été relu : nombre de variantes attendu, et **SKU + prix des survivants
strictement identiques à la sauvegarde**.

| Produit | Avant | Après | Supprimées |
|---|---:|---:|---:|
| Loupe de date `10977445216594` | 14 | **8** | 6 |
| Bracelet Présidentiel — doré `10977445085522` | 24 | **8** | 16 |
| Bracelet FKM — tropical `10977445183826` | 252 | **108** | 144 |
| Bracelet FKM — embouts courbes `10977445151058` | 48 | **48** | 0 (laissé tel quel) |
| | | | **166** |

L'état complet des 166 variantes supprimées (SKU, prix, prix barré, politique et quantité d'inventaire) est
consigné dans **`variantes-supprimees-lot2.json`**, ce qui permet de les recréer à l'identique.

### Loupe de date — ce qui a été gardé et pourquoi

Grille symétrique **4 tailles rectangulaires × 2 matières** : 4,5 × 3,5 · 5,5 × 4,5 · 5,8 × 4,5 · 7 × 5,5 mm,
en minéral **et** en saphir. Écartées : les 3 lentilles **rondes** (Ø 4,0 · Ø 4,5 · Ø 5,5 mm), la plus petite
(3,5 × 3 mm) et l'atypique 10 × 5 mm. On préfère une matrice lisible où chaque taille existe dans les deux
matières à un catalogue de tailles dépareillées.

### Bracelet Présidentiel — ce qui a été gardé et pourquoi

Les **5 mailles réellement distinctes** conservées dans leurs finitions dorées, la fiche étant « dorée » :
Jubilé (or rose réf. 15, acier & or), Président (or jaune, acier & or rose), 3 rangs (or jaune, acier & or),
Maille fixe (or jaune), Maille sablée (acier). Écartés : le **doublon numéroté** Jubilé or rose réf. 12
— indiscernable de la réf. 15, c'était l'un des 2 bracelets Jubilé signalés comme indistinguables — et les
déclinaisons noires / acier / or rose redondantes des mêmes mailles.
⚠️ Effet de bord : le prix d'entrée passe de 49,90 € à 54,90 € (la Maille fixe · acier était la moins chère).

### Détail des variantes supprimées

#### Loupe de date (14 → 8)

| Valeur supprimée | SKU (pour recréation) | ID variante |
|---|---|---|
| Minéral · Ø 4,0 mm | `14:865#A-4.0mm` | 54087126188370 |
| Minéral · 10 × 5 mm | `14:94#A-10x5mm` | 54087126221138 |
| Saphir · 3,5 × 3 mm | `14:496#B-3.5x3mm` | 54087126253906 |
| Minéral · Ø 4,5 mm | `14:100013777#A-4.5mm` | 54087126286674 |
| Saphir · Ø 5,5 mm | `14:100005979#B-5.5mm` | 54087126450514 |
| Minéral · 3,5 × 3 mm | `14:193#A-3.5x3mm` | 54087126614354 |

#### Bracelet Présidentiel — doré (24 → 8)

| Valeur supprimée | SKU (pour recréation) | ID variante |
|---|---|---|
| Jubilé · or rose (réf. 12) | `200000049:1089#Jubilee Watchband-12;200000051:202532806` | 54087123796306 |
| Maille fixe · or rose | `200000049:200013901#No Adjustable Belt-5;200000051:202532806` | 54087123829074 |
| Président · acier & or | `200000049:202567811#President Belt-11;200000051:202532806` | 54087123861842 |
| Maille fixe · acier & or | `200000049:200006154#No Adjustable Belt-3;200000051:202532806` | 54087123927378 |
| Maille fixe · acier & or rose | `200000049:2198#No Adjustable Belt-2;200000051:202532806` | 54087123960146 |
| Jubilé · noir | `200000049:365462#Jubilee Watchband-16;200000051:202532806` | 54087123992914 |
| Jubilé · acier | `200000049:347#Jubilee Watchband-17;200000051:202532806` | 54087124025682 |
| 3 rangs · or rose | `200000049:350852#Watch Band-18;200000051:202532806` | 54087124058450 |
| 3 rangs · acier & or rose | `200000049:10#Watch Band-20;200000051:202532806` | 54087124123986 |
| 3 rangs · noir | `200000049:94#Watch Band-21;200000051:202532806` | 54087124156754 |
| Président · or rose | `200000049:200966040#President Belt-8;200000051:202532806` | 54087124255058 |
| Président · noir | `200000049:100013775#President Belt-7;200000051:202532806` | 54087124287826 |
| Président · acier | `200000049:76119733#President Belt-6;200000051:202532806` | 54087124353362 |
| Maille fixe · acier | `200000049:100010417#No Adjustable Belt-1;200000051:202532806` | 54087124451666 |
| Jubilé · acier & or rose | `200000049:41#Jubilee Watchband-13;200000051:202532806` | 54087124484434 |
| 3 rangs · acier | `200000049:202529811#Watch Band-23;200000051:202532806` | 54087124517202 |

#### Bracelet FKM — tropical (252 → 108)

**Les 36 couleurs sont intactes.** Seules les largeurs ont été réduites aux 3 plus courantes (18 / 20 / 22 mm).

| Largeur supprimée | Variantes | Couleurs concernées |
|---|---:|---|
| 19 mm | 36 | les 36 |
| 21 mm | 36 | les 36 |
| 23 mm | 36 | les 36 |
| 24 mm | 36 | les 36 |

Le SKU y est strictement déterministe :
`200000049:<idCouleur>#<nomCouleur>;200000051:<idLargeur>` — les 144 lignes exactes sont dans
`variantes-supprimees-lot2.json`.

Grille restante vérifiée : **36 couleurs × 3 largeurs = 108**, aucune couleur perdue.

---

## Réparation des `alt` des mères

Les 31 fichiers touchés ont été réécrits via `fileUpdate`, en utilisant **le titre de la mère** (le fichier
est partagé : il doit décrire le modèle, pas un coloris). Convention restaurée sur les galeries de 7 images :

1. `<Titre de la mère> — Maison Noirmont` · 2. `<Gamme> — portée` · 3. `<Gamme> — <caractéristique>` ·
4. `<Gamme> — <geste du modèle>` · 5. `<Gamme> — détails et finitions` ·
6. `<Gamme> — 4,8/5 sur 1340 avis, garantie 12 mois` · 7. `<Gamme> — témoignage client`

| Mère | Images | Positions 3 et 4 retenues |
|---|---:|---|
| Contre-la-montre — Chronographe panda | 7 | lunette tachymètre · déclenchement du chronographe |
| Voyageur — GMT automatique | 7 | lunette rootbeer bicolore · second fuseau |
| Intégrale — Sport chic acier | 7 | bracelet intégré · en main |
| Héritage — Plongeuse vintage 42 | 7 | lunette tournante graduée · rotation de lunette |
| Remontoir Bois | 1 | `Remontoir Bois — Maison Noirmont` |
| Rouleau de Voyage — cuir | 1 | `Rouleau de Voyage — cuir — Maison Noirmont` |
| Remontoir Collection — 2 à 6 montres | 1 | `Remontoir Collection — 2 à 6 montres — Maison Noirmont` |

⚠️ **À relire.** Les textes d'origine étaient perdus, non récupérables. Les positions 1, 2, 5, 6 et 7 suivent
la convention à la lettre. Les positions **3 et 4** ont été **reconstruites à partir des caractéristiques
documentées du produit** (fiche de renommage du 25/07), pas retrouvées : si les textes d'origine disaient
autre chose, ce sont ces 8 lignes-là qu'il faut corriger.

---

## Contrôle DSers

Fait sur la session Chrome de Hakim (compte `contact.noirmont`), **sans aucune saisie d'identifiant**,
page rechargée pour éviter un affichage antérieur aux suppressions.

| Compteur | Valeur |
|---|---|
| Tous | **44** |
| AliExpress | **44** |
| 1688 Dropshipping / Alibaba | 0 / 0 |
| **Unmapped (Non répertorié)** | **0** ✅ |

**Aucune fiche historique n'est repassée en « Unmapped » après la suppression des 166 variantes.**
Les 3 fiches élaguées ont été vérifiées une à une dans la liste : Loupe de date, Bracelet Présidentiel — doré
et Bracelet FKM — tropical y figurent toujours, mappées sur AliExpress. Le FKM embouts courbes est intact.

Preuve supplémentaire que DSers s'est bien resynchronisé plutôt que de garder un état figé : le prix affiché
du Bracelet Présidentiel est passé à **54,90–59,90 €**, ce qui reflète exactement la suppression de la
variante à 49,90 € (Maille fixe · acier).

⚠️ **Les 41 nouvelles fiches ne sont pas encore dans DSers** — le compteur reste à 44. C'est attendu :
l'auto-matching par SKU n'existe pas, le rattachement doit être fait produit par produit. **À faire avant
toute première commande.** Les SKU portent la chaîne d'attributs AliExpress à l'octet près et servent de
table de correspondance.

---

## Visuels manquants créés par cette passe

Chaque nouvelle fiche partage aujourd'hui la galerie de sa mère : **les 41 fiches créées n'ont pas de visuel
propre**. Aucune image n'a été générée (budget crédits épuisé).

| Groupe | Fiches sans visuel propre |
|---|---:|
| Contre-la-montre — chronographe | 12 |
| Voyageur — GMT | 6 |
| Intégrale | 7 |
| Héritage | 3 |
| Remontoir Bois | 4 |
| Rouleau de Voyage | 4 |
| Remontoir Collection | 5 |
| **Total** | **41** |

S'y ajoutent **8 visuels de variante** à l'intérieur des fiches chrono fusionnées (20 cadrans répartis sur
12 fiches), si l'on veut illustrer chaque cadran.

**L'élagage a réduit la dette d'images.** L'arriéré global passe de **88 à 69 visuels**, la fiche Bracelet
Présidentiel tombant de 24 à 8 variantes et le GMT de 9 à 6 déclinaisons illustrables.

| Fiche | Avant | Après lot 2 |
|---|---:|---:|
| Contre-la-montre | 20 | 20 |
| Voyageur GMT | 9 | 6 |
| Noirmont Deux | 7 | 7 |
| Intégrale | 7 | 7 |
| Héritage | 3 | 3 |
| Remontoir Bois | 4 | 4 |
| Rouleau de Voyage | 4 | 4 |
| Bracelet Présidentiel | 24 | **8** |
| Set de tournevis | 5 | 5 |
| Remontoir Collection | 5 | 5 |
| **Total** | **88** | **69** |

---

## Ce qui reste à faire

1. **Mapper les 41 nouvelles fiches dans DSers** — bloquant avant la première commande.
2. **69 visuels à produire** (voir `PROMPT-CODEX-reprise-visuels.md`), dont les 41 images de tête des
   nouvelles fiches.
3. **Relire les 8 `alt` reconstruits** (positions 3 et 4 des 4 galeries montres).
4. **Trancher la description du GMT** : la phrase « plusieurs lunettes bicolores au choix », héritée de la
   mère, ne correspond plus à une fiche mono-boîtier. Porte sur les 6 fiches Voyageur.
5. **Médias partagés** : décider si les fiches filles doivent avoir des fichiers indépendants
   (réupload) plutôt que de pointer le `MediaImage` de la mère.
6. **Noirmont Deux** reste en attente : ses 7 « Référence » ne sont toujours pas identifiables
   (même photo fournisseur pour toutes). Non touchée, comme demandé.
7. **Sort des 12 variantes GMT siglées** : toujours sur la mère, invendables (`DENY`, stock 0).

---

## Annulation

Supprimer les 41 IDs créés (`productDelete`) annule intégralement la phase 1 — rien d'autre n'a été écrit sur
ces fiches. La phase 2 se rejoue depuis `variantes-supprimees-lot2.json`. Les `alt` réparés, eux, resteraient
en l'état.

```
10980078780754 10980078879058 10980078911826 10980079042898 10980079075666
10980080419154 10980080714066 10980080779602 10980080845138 10980080877906
10980080976210 10980081041746 10980081074514 10980081107282 10980081205586
10980081336658 10980081402194 10980081533266 10980081631570 10980081664338
10980081762642 10980081926482 10980082745682 10980082778450 10980082843986
10980082909522 10980083007826 10980083106130 10980083138898 10980083171666
10980083269970 10980083401042 10980083466578 10980083564882 10980083728722
10980083859794 10980084056402 10980084121938 10980084220242 10980084449618
10980084515154
```

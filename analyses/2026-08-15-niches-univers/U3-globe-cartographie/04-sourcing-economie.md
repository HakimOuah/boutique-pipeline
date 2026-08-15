# U3 — Globe terrestre et cartographie déco — sourçabilité et économie (étapes 4 et 5)

- **Date : 15/08/2026**, session ouverte à 22h24, close à 23h05.
- Entrée : `03-verification-serp.md` (66 550 vérifiés, bandes de prix SERP) et `02-volume-consolide.md` (volumes et CPC en USD).
- Outils : passerelle API AliExpress (`aliexpress_vps_gateway.py`, Bash, actions `search` et `variants`) + SERP AliExpress JSON lue en DOM dans un onglet Chrome dédié (`885844851`, fermé en fin de tâche) + `products.json` d'un concurrent en `curl`.
- **Aucun GO lancement ici.** Statuts sourcing par famille et verdict économique seulement. La décision revient à Hakim.
- Aucun contact vendeur, aucun achat, aucune modification Shopify / Ads / GMC.

---

## État d'avancement

**TERMINÉ — 6 familles sur 6 sondées, 15/08/2026 23h05.**

| Famille | Requêtes | Cartes lues | Fiches retenues | Statut |
|---|---|---:|---:|---|
| Globe terrestre | SERP `globe terrestre` + API `levitating globe`, `liquor globe`, `armillary sphere`, `maglev globe`, `gyro globe`, `globe lévitation`, `globe laiton bureau`, `globe cristal gravé`, `globe antique parchemin` | 58 + 9×20 API | 12 | ✅ |
| Carte du monde en bois | SERP `carte-du-monde-en-bois` (échec), `wooden-world-map-wall` + API `multilayer map` (échec) | 60 + 60 | 6 | ✅ |
| Carte du monde murale | SERP `carte-du-monde-murale` | 60 | 12 | ✅ |
| Carte du monde à gratter | SERP `scratch-off-world-map` + `carte-du-monde-à-gratter` + API `scratch map` (échec) | 60 + 60 | 5 | ✅ |
| Carte du monde liège | SERP `carte-du-monde-en-liège` + `cork-world-map-pin` + API `cork map` (échec) | 60 + 60 | 7 | ✅ |
| Globe-bar | SERP `globe-bar-cabinet` + `bar-mappemonde-meuble` + API `liquor globe` | 59 + 60 | 2 | ✅ |

**Économie :** 4 produits représentatifs chiffrés. **Gate panier :** franchie, avec mécanisme observé chez `lemondeagratter.com`. **Saisonnalité :** non mesurée (widget SEMrush vide).

### Note de méthode sur les requêtes — la règle des mots rares s'est vérifiée, et retournée

La règle « deux mots rares » a **échoué sur cette niche** et il faut l'écrire, parce que c'est une information réutilisable :

| Requête API en mots rares | Résultat |
|---|---|
| `scratch map` | 20/20 hors sujet — **dissolvant de rayures de voiture** et **tapis à gratter pour chat**. `scratch` n'est pas le mot de métier de la carte à gratter, c'est le mot de métier de la rayure. |
| `cork map` | 20/20 hors sujet — bouchons de liège, panneaux de liège, tire-bouchons. |
| `armillary sphere` | 20/20 hors sujet — moules à bombe de bain, boules de cristal. |
| `multilayer map` | 19/20 hors sujet — étagères et bibliothèques multicouches. |
| `gyro globe` | 20/20 hors sujet — toupies Beyblade et capteurs gyroscopiques Arduino. |
| `maglev globe` | 13/16 hors sujet — Rubik's cubes magnétiques GAN Maglev. |
| `levitating globe` | **18/18 pertinents.** Le seul mot rare qui paie. |

**Ce que cela apprend :** un mot rare *en anglais technique* n'est utile que si le traducteur automatique d'AliExpress l'emploie réellement pour la catégorie visée. Ici, `scratch`, `cork`, `armillary`, `gyro` sont rares **en français** mais fréquents **en anglais dans d'autres rayons**, et l'appariement large les y ramène. **La SERP AliExpress en français littéral a battu l'API sur cinq familles sur six.** Une exception dans l'autre sens : la SERP `carte-du-monde-en-bois` a rendu 60 best-sellers du catalogue entier (tondeuses, huiles essentielles, ruban adhésif) — c'est le même effondrement de pertinence, côté SERP cette fois, et il a fallu passer à l'anglais `wooden world map wall` pour obtenir des résultats.

---

## 1. Sourçabilité par famille

**Convention de confiance** (règle du brief) : A = PDP ouverte et lue ; B = SERP JSON + confirmation `variants` API ; C = SERP JSON seule ou titre seul.
**Aucune PDP n'a été ouverte** (mur anti-bot connu, mémoire `mur-pdp-aliexpress-navigateur-integre`) : **aucune fiche de ce rapport n'est en confiance A.**

⚠️ **Écart de ventes SERP vs API, systématique et à retenir.** Sur les six produits repassés en `variants`, le compteur `tradeDesc` de la SERP est **toujours supérieur** au `sales_count` de l'API : 52 v vs 14 (`32877306422`), 53 v vs 25 (`4001350010280`), 434 v vs 254 (`1005006987114384`), 4 v vs 3 (`32867430455`). **Je retiens le chiffre API, plus bas**, et je signale les deux dans les tableaux.

### 1.1 Globe terrestre (28 650 vérifiés — la plus grosse famille)

SERP `https://fr.aliexpress.com/w/wholesale-globe-terrestre.html?SortType=total_tranpro_desc`, 60 cartes lues le 15/08 à 22h26.

| # | product_id | Titre court | Prix réel (`salePrice` / `offer_sale_price`) | Ventes SERP | Ventes API | Note | Vendeur | Conf. |
|---|---|---|---:|---:|---:|---:|---|---|
| 1 | 1005006987114384 | Globe du monde rétro déco | **10,19 €** (variantes 10,19 → 44,99) | 434 | **254** | 4,9 · **97,5 %** | Lost And Beautiful Store (CN) · desc 4,8 / ship 4,8 | **B** |
| 2 | 1005005855031541 | Globe à lévitation magnétique LED | **23,19 €** | > 1 000 | **180** | 4,7 · 93,2 % | IKOKY Official Store (CN) · desc 4,6 / ship 4,7 | **B** |
| 3 | 1005010155240772 | Globe flottant lévitant LED | **24,99 €** (5 variantes 24,79 → 25,99) | > 500 | **153** | 4,9 · — | Stone's Store (CN) · desc 5,0 / ship 4,8 | **B** |
| 4 | 1005010787269571 | Globe lévitation magnétique carte LED | **24,99 €** | 53 | — | 4,9 · **98,0 %** | (API `search`) | C |
| 5 | 1005008685663415 | Petit globe noir & or / noir & argent | **17,89 €** | 471 | — | 4,7 · 93,2 % | — | C |
| 6 | 1005010666666642 | Ornement globe rotatif version anglaise | **8,59 €** | 264 | — | 4,8 · **96,5 %** | — | C |
| 7 | 1005009708488874 | Statue globe terrestre or, résine | **15,99 €** | 100 | — | 4,6 · 92,5 % | — | C |
| 8 | 1005005977787813 | Globe bois avec support | **12,89 €** | 165 | — | 5,0 · 99,0 % | — | C |
| 9 | 1005010807239052 | Globe complet anglais Ø 14 cm | **26,39 €** (3 variantes, stock 44/57/58) | 28 | **20** | — | HD-WORLD Store (CN) · desc 4,4 / ship 4,7 | **B** |
| 10 | 1005008248019944 | Globe AR éducatif 11", constellations | **48,39 €** (stock 5) | 193 | **50** | 4,9 · — | Stone's Store (CN) · desc 5,0 / ship 4,8 | **B** |
| 11 | 1005011697628503 | Globe rotatif anglais, puzzle éducatif | **51,99 €** (**stock 1**) | 13 | **13** | — | Hormy HL Worldwide Store (CN) · desc 4,5 | **B** |
| 12 | *(id tronqué à la lecture : …1958035)* | Globe pierres précieuses 4 pattes | **117,99 €** | 2 | — | — | — | C — id incomplet, fiche non réutilisable telle quelle |

**Vendeurs pivots (≥ 96 % d'avis positifs, mesurés par `evaluation_rate` de l'API `search`) :** Lost And Beautiful Store (**97,5 %**, 254 ventes) ; le vendeur du `1005010787269571` (**98,0 %**) ; celui du `1005010666666642` (**96,5 %**) ; celui du `1005005977787813` (**99,0 %**).
**Rejets motivés :** IKOKY (93,2 %), les deux vendeurs à 93,2 / 88,1 % sur les globes lévitants concurrents, et **`1005011697628503` malgré son prix intéressant : stock 1**, ce n'est pas un fournisseur, c'est une fin de série.

**Constat de fond sur cette famille.** Le catalogue AliExpress est **dense mais mal aligné sur la demande française**. Sur 58 cartes lues : **une majorité de globes scolaires / éducatifs / gonflables entre 2,79 et 10 €**, et une poignée de globes déco au-dessus de 15 €. **Le globe déco de 25-30 cm avec socle, qui est le cœur de la bande française 25-100 € (médiane 46 €), est représenté par une dizaine de références seulement.** À l'inverse, le globe à lévitation — qui n'est qu'une ligne de 450 recherches dans la famille — est le produit le mieux fourni et le mieux vendu du catalogue.

**Trou d'offre décisif, à écrire noir sur blanc :** la quasi-totalité des globes sourçables portent la mention *« version anglaise »*, *« carte du monde anglaise HD »*, *« chinois et anglais »*. **Aucun globe en français n'a été observé sur 58 cartes.** Or la demande FR contient cinq formulations `globe terrestre en français / francais / français` (590 de volume mesuré à l'étape 2), et `natureetdecouvertes.com` comme `univers-globe.com` vendent des globes en français. **C'est un désalignement produit, pas un détail de fiche.**

### 1.2 Carte du monde en bois (5 490 vérifiés — famille sortie indemne de la SERP Google)

**Deux requêtes, dont un échec instructif.** La SERP `carte-du-monde-en-bois` a rendu **60 best-sellers hors sujet** (veilleuse LED, tondeuse nez, ruban adhésif, huile essentielle) : AliExpress n'a pas assez d'inventaire apparié et retombe sur la popularité globale. La requête anglaise `wooden-world-map-wall` a rendu du pertinent.

| # | product_id | Titre court | Prix réel | Ventes SERP | Ventes API | Note | Vendeur | Conf. |
|---|---|---|---:|---:|---:|---:|---|---|
| 1 | 32867430455 | Carte du monde en bois faite à la main | **29,19 €** (1 variante) | 4 | **3** | 5,0 · — | Vinyl Record Clock Timemaker Official Store (CN) · desc 4,5 / ship 4,6 | **B** |
| 2 | 1005012022417040 | Carte du monde bois massif, déco murale | **319,69 €** | 1 | — | — | — | C |
| 3 | 1005012886860536 | Carte du monde, tableau mural souvenir | **788,69 €** | 0 | — | — | — | C |
| 4 | 1005012879427221 | Déco murale bois massif 3D, carte | **955,69 €** | 0 | — | — | — | C |
| 5 | 1005012343804691 | Déco murale jardin 105 × 55 cm | **67,18 €** | 0 | — | — | — | C |
| 6 | 1005008678462912 | Panneau rond bois, motif carte | **3,59 €** | 71 | — | 4,0 | — | C |

**Aucun vendeur pivot identifié :** aucun des six n'a de `evaluation_rate` mesuré ≥ 96 %, et la seule fiche repassée en API affiche **3 ventes**.

**C'est le retournement de l'étape 4.** La famille la plus saine du côté Google — page 1 marchande à 8/9, quatre indépendants français, médiane 97 €, bande 69-159 €, KD 3-17 — est **la plus pauvre du côté fournisseur**. La carte du monde en bois découpé est un produit **d'atelier**, fabriqué à la demande, pas un produit de catalogue chinois : les références au-dessus de 300 € n'ont aucune vente, la seule référence à prix de dropship (29,19 €) a trois ventes, et le reste de la page dérive vers des boussoles murales, des plaques décoratives et des porte-clés. **`woodwork08.com` et `creatifwood.com` ne se fournissent pas là.**

### 1.3 Carte du monde murale (3 020 vérifiés — l'autre famille sortie indemne)

SERP `carte-du-monde-murale`, 60 cartes, **60/60 pertinentes** — le meilleur taux d'appariement de toute la niche.
**Bande de prix fournisseur : min 1,05 € · médiane 4,89 € · max 20,39 €.**

| # | product_id | Titre court | Prix réel | Ventes SERP | Note | Conf. |
|---|---|---|---:|---:|---:|---|
| 1 | 1005010485103293 | Toile imprimée carte du monde colorée | **3,59 €** | 434 | 5,0 | C |
| 2 | 1005006518829926 | Toile peinture carte du monde | **3,09 €** | 294 | 5,0 | C |
| 3 | 1005007052728894 | Affiches toile carte du monde rétro | **11,79 €** | 205 | 4,1 | C |
| 4 | 1005008968218670 | Affiche déco toile carte du monde | **5,99 €** | 68 | 3,8 | C |
| 5 | 1005004281680193 | Carte du monde standard imprimée | **1,66 €** | 67 | 5,0 | C |
| 6 | 32809057369 | Affiche toile à défilement (scroll) | **8,72 €** | 48 | 4,9 | C |
| 7 | 1005005791680243 | Toile art mural abstrait carte | **4,89 €** | 38 | 4,1 | C |
| 8 | 1005006020822796 | Toile ancienne rétro carte du monde | **9,39 €** | 32 | 3,7 | C |
| 9 | 1005008835372495 | Carte du monde déco 36 × 24 pouces | **5,99 €** | > 1 000 | 4,8 | C |
| 10 | 1005009183063193 | Affiche murale sans cadre carte | **7,19 €** | 425 | 4,7 | C |
| 11 | 1005008945099157 | Affiche suspendue vintage carte | **9,01 €** | 464 | 4,9 | C |
| 12 | 1005010035038842 | Carte ville/comté personnalisable | **6,19 €** | 354 | 4,8 | C |

**Profondeur réelle, ventes réelles, prix dérisoires.** C'est la seule famille où le sourcing est franchement abondant. Mais **la marchandise est un poster ou une toile à 3-9 €**, pas un objet : le prix de vente français médian de 39 € tient à l'encadrement, au format et à la marque, pas au produit.
⚠️ **Trois références de « carte de la terre plate » / « flat earth map » figurent sur cette page, dont une à 114 ventes** (`1005004280883381`, 4,99 €). Voir section 3, conformité.

### 1.4 Carte du monde à gratter (7 560 vérifiés)

Deux SERP (`scratch-off-world-map`, `carte-du-monde-à-gratter`) : **60 cartes chacune, 8 à 10 titres contenant « gratter » ou « scratch », dont 5 sont réellement des cartes du monde à gratter.** Les autres sont de la peinture à gratter pour enfants et des cartes de jeu à gratter.

| # | product_id | Titre court | Prix réel | Ventes SERP | Ventes API | Note | Vendeur | Conf. |
|---|---|---|---:|---:|---:|---:|---|---|
| 1 | 32877306422 | Travelogue Scratch World Map | **17,19 €** (1 variante) | 52 | **14** | 5,0 · — | your chinese books Store (CN) · desc 4,6 / ship 4,9 | **B** |
| 2 | 1005012747055835 | Affiche cartographie mondiale à gratter de luxe | **5,89 €** (4 variantes 5,89 → 13,99) | 1 | **1** | — | A Libaba Store (CN) · desc 4,1 / ship 4,3 | **B** |
| 3 | 1005012715441118 | Affiches murales d'aventure à gratter | **13,99 €** | 2 | — | — | — | C |
| 4 | 1005012081406461 | Affiche voyage à gratter, parcs nationaux | **4,99 €** | 3 | — | — | — | C |
| 5 | 1005005447449778 | Carte à gratter du Brésil | **5,09 €** | 14 | — | — | — | C |

**Aucun vendeur pivot.** Le mieux noté sur le critère fournisseur (`your chinese books`, desc 4,6 / ship 4,9) vend **14 unités** et à **17,19 €** — c'est-à-dire au-dessus du seuil qui rend la famille rentable (voir section 4). Le seul prix compatible avec l'économie (5,89 €) est chez un vendeur à **desc 4,1** avec **une vente**.
**Constat : la carte du monde à gratter est visiblement fabriquée en Chine — puisqu'elle existe — mais elle ne transite pas par le canal dropship AliExpress.** `lemondeagratter.com` (97 SKU, posters à 24,90 €) achète ailleurs, ou fait fabriquer.

### 1.5 Carte du monde en liège (3 070 vérifiés)

SERP `carte-du-monde-en-liège` : **7 matches sur 60**, et **cinq des sept portent le même nom de marque, `Aqumotic`**.

| # | product_id | Titre court | Prix réel | Ventes SERP | Ventes API | Note | Vendeur | Conf. |
|---|---|---|---:|---:|---:|---:|---|---|
| 1 | 4001350010280 | Aqumotic — carte du monde liège, tableau | **14,39 €** (3 variantes 14,39 → 35,59) | 53 | **25** | 5,0 · — | Snowflake Trading Store (CN) · desc 4,6 / ship 4,8 | **B** |
| 2 | 33005856591 | Aqumotic — support globe liège, écorce | **25,79 €** | 30 | — | 5,0 | C |
| 3 | 1005006527604495 | Globe du monde Aqumotic avec support | **25,79 €** | 20 | — | 5,0 | C |
| 4 | 4000514937296 | Aqumotic — globe déco liège | **25,79 €** | 14 | — | — | C |
| 5 | 1005008482028980 | Globe bois de liège Tellurion | **49,99 €** | 3 | — | — | C |
| 6 | 1005012822744899 | Aqumotic Cork World Map Travel Board | **10,29 €** | 1 | — | — | C |
| 7 | 1005012702383014 | Carte de voyage interactive États-Unis | **12,19 €** | 0 | — | — | C |

**Risque de fournisseur unique.** Cinq références sur sept portent la même marque et trois d'entre elles ont exactement le même prix (25,79 €) : c'est un seul catalogue revendu par plusieurs boutiques. **Si Aqumotic s'arrête, la famille s'arrête.** Aucun vendeur pivot mesuré ≥ 96 %.
La bande française (médiane 41 €, cœur 20-70 €) et le coût fournisseur (14,39 €) laissent de la marge — mais **`misswood.eu`, la marque de référence du liège en page 1 Google, ne se fournit manifestement pas ici** : ses cartes sont en liège découpé multi-couches, ce qui n'existe pas dans les sept références lues.

### 1.6 Globe-bar (1 300 vérifiés — la plus haute bande de prix de l'univers, 214 € de médiane)

Deux SERP (`globe-bar-cabinet`, `bar-mappemonde-meuble`) : **2 références de meuble-bar globe sur 119 cartes lues.**

| # | product_id | Titre court | Prix réel | Ventes | Note | Vendeur | Conf. |
|---|---|---|---:|---:|---:|---|---|
| 1 | 1005012370622195 | Bar globe vins et spiritueux, eucalyptus massif | **143,09 €** (3 variantes 143,09 → 173,51) | **0** | aucune | **DTrade Store FR** (entrepôt France) · aucune note | **B** |
| 2 | 1005012825681102 | Bar à vin mobile bois d'eucalyptus | **189,34 €** | **0** | aucune | — | C |

**Rejets :** tout le reste de la page est soit un globe de bureau, soit une carafe à whisky en forme de globe (`1005010530325052` 8,69 € ; `1005006560658164` 25,59 €, 133 ventes), soit un chariot à vin sans globe. **La carafe-globe est un vrai produit sourçable, mais ce n'est pas le globe-bar.**

**Le seul point positif du dossier : `DTrade Store FR` expédie depuis un entrepôt France.** Sur un meuble, c'est déterminant. Mais **zéro vente et aucune note** : c'est un fournisseur non éprouvé, pas un fournisseur.

---

## 2. Profondeur en concepts vs le seuil de 200

**Règle appliquée : je compte ce que j'ai vu, sur 8 pages de SERP AliExpress (≈ 480 cartes lues) et 9 requêtes API. Je n'extrapole pas.**

| Famille | Concepts produits distincts **observés** | Exemples de concepts comptés |
|---|---:|---|
| Globe terrestre | **24** | globe scolaire HD 360° · globe physique 7/11/16/22 cm · ballon gonflable · kit STEM jour-nuit · globe lévitation LED · globe flottant lampe · petit globe noir & or · globe rétro déco · ornement rotatif · statue globe résine or · globe bois sur support · globe AR constellations · globe en briques DIY · globe zoologique · globe pierres précieuses · globe coupe géologique 32 cm · globe lumineux 12" · globe LED rétroéclairé politique/physique · globe antique 5,5" · globe rotatif 14/20/23 cm · globe Gémeaux enfant · mini globe cristal · globe verre Feng Shui · globe puzzle 3D |
| Carte murale / poster | **14** | toile imprimée · toile peinture · affiche encadrée · affiche sans cadre · affiche suspendue vintage · affiche à défilement (scroll) · sticker mural adhésif · papier peint · carte personnalisée ville/comté · carte drapeaux du monde · carte enfant colorée · carte 36×24" · carte adhésive voiture · tapisserie |
| Carte du monde en bois | **9** | carte bois faite main · carte bois massif 3D · panneau rond bois · plaque murale 2D bois · déco jardin 105×55 · mini modèle 1/12 · puzzle carte bois · carte de France gravée laser · toile imitation bois |
| Carte à gratter | **5** | carte monde à gratter luxe · travelogue scratch map · affiche parcs nationaux · affiche aventure · carte pays unique (Brésil) |
| Carte liège | **5** | carte liège tableau d'affichage · globe liège sur support · globe liège sans repères · globe bois-liège Tellurion · carte voyage interactive USA |
| Globe-bar | **2** | meuble bar globe eucalyptus · bar mobile eucalyptus |
| Adjacents sourçables (comptés à part) | **6** | carafe whisky globe · verre à whisky · punaises de carte · autocollants drapeaux · boussole murale bois · marqueurs de carte |
| **TOTAL OBSERVÉ** | **≈ 59 (65 avec adjacents)** | |

**Face au seuil de 200 : le seuil n'est pas atteint sur ce qui a été observé, et l'écart est large (59 vs 200, soit 30 %).**

Trois nuances honnêtes :
1. **Je n'ai lu que la première page de chaque SERP** (60 cartes). Une exploration en profondeur remonterait davantage de références — mais probablement peu de *concepts* nouveaux : les pages 1 étaient déjà largement redondantes (trois versions du même « ornement de globe rotatif version anglaise », trois Aqumotic au même prix).
2. **Un « concept » ici est un type de produit, pas une déclinaison.** Un globe décliné en 14/20/23 cm compte pour un.
3. **Le comptage est fondé sur des titres traduits automatiquement**, souvent trompeurs. Deux titres différents peuvent recouvrir le même produit ; je les ai fusionnés quand c'était manifeste, ce qui rend le compte plutôt conservateur.

**Conclusion de profondeur : U3 est une niche à volume de recherche large mais à catalogue étroit.** Le contraste avec la mesure est net — 66 550 recherches vérifiées pour ≈ 59 concepts sourçables observés.

---

## 3. Logistique, casse et conformité

### 3.1 Ce qui n'a pas pu être mesuré du tout — et c'est grave sur cette niche

**Aucun poids, aucune dimension, aucun mode d'expédition, aucun délai France n'a été obtenu.** Les trois canaux ont échoué :
- `variants` retourne prix, stock, notes du magasin — **pas de logistique** ;
- `exact` exige des propriétés SKU (`--property`) et n'a donc pas pu être appelé à l'aveugle ;
- la SERP JSON ne porte **aucune** chaîne de livraison (0 occurrence de « Livraison » dans le DOM des 8 pages lues) ;
- les PDP restent bloquées par l'anti-bot.

**C'est le trou le plus lourd de ce rapport**, précisément parce que la logistique est le risque structurel de cette niche.

### 3.2 Ce que la nature des produits impose quand même

| Produit | Risque logistique | Lecture |
|---|---|---|
| **Globe déco 25-30 cm** | Sphère + arceau métal + socle. Colis volumineux mais léger. Casse à l'arceau et au socle. | Risque **modéré**, à tester en réel |
| **Globe lumineux / à lévitation** | Électronique + aimant + alimentation + verre ou acrylique. Colis fragile, produit à panne. | Risque **élevé** : casse ET SAV |
| **Globe-bar** | Meuble 143-189 €, encombrant. Le fournisseur `DTrade Store FR` expédie de France — c'est le seul point qui rendrait la famille tenable. | Risque **très élevé** si expédition Chine ; **acceptable** depuis FR, mais fournisseur à 0 vente |
| **Carte murale bois massif 200 × 120** | Pièce longue et lourde, transport hors gabarit. Les références à 319-955 € n'ont aucune vente : personne ne les expédie. | **Rédhibitoire en dropship** |
| **Carte à gratter / poster** | Rouleau léger. Peu de casse, mais **pliure et froissement** — premier motif de retour du poster. | Risque **faible**, coût de retour supérieur à la valeur du produit |
| **Carte liège** | Panneau rigide ou rouleau. Éclats de bord. | Risque **faible à modéré** |

### 3.3 Conformité

**a) Électrique — CE, DEEE, basse tension.** Tous les globes lumineux, à lévitation et AR sont des **appareils électriques** : marquage CE, déclaration de conformité, directive CEM, alimentation USB/secteur conforme, **inscription à un éco-organisme DEEE** et éco-participation sur facture. Les globes à lévitation ajoutent un **électro-aimant puissant** — risque documenté pour les porteurs d'implants et pour les enfants.

**b) Jouet — la ligne à ne pas franchir.** Une part importante du catalogue AliExpress sourçable est explicitement **éducative / enfant** (globes scolaires, kits STEM, ballons gonflables, globes AR). Ces produits relèvent de la **directive Jouets 2009/48/CE et de la norme EN 71**, avec des obligations de dossier technique qu'un dropshipper ne peut pas honorer. **C'est cohérent avec le retournement déjà établi à l'étape 5 sur `globe interactif` (page 1 fermée par VTech, Clementoni, Ravensburger) : le rayon enfant est fermé commercialement ET lourd réglementairement.** Double motif d'exclusion.

**c) Exactitude cartographique — le risque propre à cette niche, et il est vérifié.**
- **La SERP `carte du monde murale` contient des cartes « terre plate » / « flat earth », dont une à 114 ventes** (`1005004280883381`, 4,99 €), plus `1005003580415849` (48 ventes) et `1005011811377686`. Vendre une carte de la terre plate en la présentant comme une carte du monde, c'est de la **désinformation au sens des règles Google Merchant Center** (misrepresentation). À exclure du feed sans discussion.
- **Frontières contestées.** Les cartes imprimées en Chine portent régulièrement la **ligne à neuf traits** en mer de Chine méridionale et la mention *« Taiwan, China »*. S'y ajoutent la Crimée, le Cachemire, le Sahara occidental, les frontières israélo-palestiniennes. **Chaque visuel doit être inspecté avant publication** — ce n'est pas une formalité, c'est une cause de suspension et de litige.
- **Langue.** Aucun globe en français observé (voir 1.1). Une carte en anglais vendue à un public français est un motif de retour.

**d) Licences — trois noms à ne jamais toucher.** **National Geographic** (marque présente dans les filtres Shopping de `globe terrestre`), **Michelin**, **IGN** (`boutique.ign.fr` tient une position organique sur trois requêtes). Leurs fonds de carte et leurs marques sont protégés. Le risque n'est pas théorique : un poster AliExpress peut reprendre un fond IGN ou NatGeo sans le dire.

---

## 4. Économie par produit représentatif

### Hypothèses, posées avant les chiffres

- **CPC** : issus de `02-volume-consolide.md`, **en USD**, convertis à **1 USD = 0,92 €** pour rendre le ratio homogène. La conversion est mienne, pas mesurée.
- **Frais de paiement** : 1,4 % + 0,25 € par transaction.
- **Marge contributive sur base HT** : `PV TTC ÷ 1,2 − coût rendu − frais de paiement`. **Jamais sur le TTC.**
- **Coût rendu = `offer_sale_price` + fret FR.** ⚠️ **Le fret n'a pas pu être mesuré** (section 3.1). **Tous les chiffres ci-dessous sont donc calculés fret à 0 €, ce qui est l'hypothèse la plus favorable.** La colonne « fret de rupture » donne le fret à partir duquel la marge tombe à zéro — c'est la vraie information.
- **Prix de vente cible = juste sous le comparable**, le comparable étant l'**indépendant sans récit de marque** relevé en page 1 Google (jamais Zoffoli, jamais Misswood, jamais Amazon/Cdiscount, jamais leboncoin).

### 4.1 Tableau

| | **Globe-bar** | **Carte du monde en bois** | **Globe terrestre** | **Carte à gratter** |
|---|---:|---:|---:|---:|
| Bande SERP FR (médiane) | 214 € | 97 € | 46 € | 22 € |
| Comparable retenu | univers-globe.com / barsglobes-et-mappemondes.com | woodwork08.com / creatifwood.com / 68travel.fr | univers-globe.com | lemondeagratter.com (24,90 €) |
| **Prix de vente cible TTC** | **199,00 €** | **89,00 €** | **44,90 €** | **19,90 €** |
| Produit source | `1005012370622195` | `32867430455` | `1005006987114384` | `1005012747055835` |
| `offer_sale_price` | 143,09 € | 29,19 € | 10,19 € | 5,89 € |
| Fret FR | **non mesuré (0 € retenu)** | **non mesuré (0 €)** | **non mesuré (0 €)** | **non mesuré (0 €)** |
| **Coût rendu** | **143,09 €** | **29,19 €** | **10,19 €** | **5,89 €** |
| Base HT (÷ 1,2) | 165,83 € | 74,17 € | 37,42 € | 16,58 € |
| Frais de paiement | 3,04 € | 1,50 € | 0,88 € | 0,53 € |
| **Marge contributive HT** | **19,70 €** | **43,48 €** | **26,35 €** | **10,16 €** |
| Marge en % du PV TTC | **9,9 %** | **48,9 %** | **58,7 %** | **51,1 %** |
| CPC (USD → €) | 0,33 → 0,30 € | 0,75 → 0,69 € | 0,20 → 0,18 € | 0,17 → 0,16 € |
| **Ratio prix ÷ CPC** | **655** ✅ | **129** ⚠️ | **249** ✅ | **124** ⚠️ |
| **CPA max** (= marge) | **19,70 €** | **43,48 €** | **26,35 €** | **10,16 €** |
| **ROAS break-even** | **10,10** ❌ | **2,05** ✅ | **1,70** ✅ | **1,96** ✅ |
| **Taux de conversion de rupture** | **1,52 %** | **1,59 %** | **0,70 %** | **1,57 %** |
| **Fret de rupture** (marge = 0) | **19,70 €** | **43,48 €** | **26,35 €** | **10,16 €** |
| Confiance de la fiche source | **C** (0 vente) | **B** (3 ventes) | **B** (254 ventes, vendeur pivot 97,5 %) | **B** (1 vente, vendeur desc 4,1) |

### 4.2 Lecture, ligne par ligne

**Globe-bar — le palier haut ne tient pas.** 199 € de prix de vente pour 143 € de coût : **9,9 % de marge et un ROAS break-even de 10,1**. Aucune campagne payante ne franchit 10 de ROAS sur un meuble. Et ce chiffre est déjà l'hypothèse la plus généreuse : **le fret d'un meuble dépasse largement les 19,70 € de marge**, même depuis l'entrepôt français. **La plus haute bande de prix de l'univers est aussi la seule à marge nulle.** C'est le piège des bandes bimodales dans sa forme exacte : le pôle haut existe, il est visible, et il n'est pas à prendre — parce qu'il est tenu par un fabricant (Zoffoli) et par le marché de l'occasion (leboncoin en page 1), pas par un vide.

**Carte du monde en bois — la meilleure marge unitaire, le pire fournisseur.** 43,48 € de marge, ROAS break-even 2,05 : c'est économiquement le meilleur produit du lot. Mais le ratio prix/CPC de **129 est sous la cible de 150-200** (le CPC de 0,75 USD est le plus élevé de la niche — signe que des annonceurs y mettent de l'argent), et surtout **le fournisseur a trois ventes**. On calcule une belle marge sur un produit qui n'existe pratiquement pas en dropship.

**Globe terrestre — le seul dossier économiquement sain.** 26,35 € de marge, **ROAS break-even 1,70**, ratio prix/CPC **249**, **taux de conversion de rupture 0,70 %** — le plus bas des quatre, c'est-à-dire le plus facile à atteindre. Le fournisseur est le seul **vendeur pivot** du rapport : 97,5 % d'avis positifs, 254 ventes confirmées en API, desc 4,8 / ship 4,8.
**La réserve, et elle est sérieuse :** le produit à 10,19 € est un globe de bureau rétro, pas un globe de 30 cm à 46 €. Vendre 44,90 € un globe acheté 10,19 € suppose que la mise en scène, le format et la promesse tiennent — et **le globe est en anglais**. Variante prudente avec le globe à lévitation (`1005005855031541`, 23,19 €, 180 ventes) : marge **13,35 €**, ROAS break-even **3,36**, taux de rupture **1,35 %**. Encore viable, nettement moins confortable.

**Carte à gratter — viable sur le papier, pas chez le bon fournisseur.** 10,16 € de marge et ROAS break-even 1,96 avec la source à 5,89 €. Mais cette source a **une vente** chez un vendeur à desc 4,1. **Avec le seul fournisseur qui vend réellement (`32877306422`, 17,19 €, 14 ventes), la marge devient négative : 16,58 − 17,19 − 0,53 = −1,14 €.** L'écart entre les deux scénarios n'est pas un détail de sourcing, c'est la différence entre une famille rentable et une famille à perte.

---

## 5. Gate `STOP_PRIX_PANIER` sur les deux familles basses

Concerne `carte du monde à gratter` (7 560) et `poster carte du monde` (2 460) — **10 020 des 66 550 vérifiés, soit 15 %**.

### 5.1 Les trois éléments exigés

| | Carte à gratter | Poster carte du monde |
|---|---|---|
| **Médiane** (relevé SERP Google, `03-verification-serp.md`) | **22 €** (54 prix) | **17 €** (37 prix) |
| **Part sous 15 €** | **≈ 4 %** (2 prix sur 54 : plancher 13,99, tout le reste entre 14,99 et 29,95) | **51 %** (19 prix sur 37 sous 15 €, dont 11 sous 12 €, plancher 5,49) |
| **Mécanisme de panier** | **observé** (voir 5.2) | non observé sur un acteur poster |

### 5.2 Mécanisme de panier — observé, chez `lemondeagratter.com`, jamais inventé

Lecture de `https://lemondeagratter.com/products.json?limit=250` et de la page d'accueil, le 15/08 à 22h58 :

- **97 produits publiés**, 129 variantes tarifées. **Médiane catalogue 19,90 €**, min 3,50 €, max 34,90 €, **40 % des prix sous 15 €**.
- **« Livraison offerte dès 60 € en point relais »** — bandeau présent trois fois sur la page d'accueil. **Un seuil à 60 € sur un catalogue de médiane 19,90 € est un mécanisme de panier explicite : il pousse mécaniquement à trois articles.**
- **7 packs et coffrets** : « Pack couple — poster + coffret messages » 34,90 € · « Coffret de 52 cartes à gratter personnalisables » 15,90 € · « Coffret de défis » 15,90 € · « Pack demandes témoins » 6,90 € · « Pack duo annonce parrain & marraine » 6,90 €.
- **6 types de produits** déclarés (Affiche, Carte postale, Cartes annonces, Cartes coquines, Coffrets personnalisables, Posters à gratter) — un catalogue construit pour l'achat multiple, pas mono-produit.
- **Popup d'entrée « −10 % pour commencer »** en échange de l'e-mail.

### 5.3 Verdict de la porte

**`carte du monde à gratter` : porte FRANCHIE.** Médiane 22 €, seulement 4 % sous 15 €, et un mécanisme de panier réel, observé, chez un acteur français vivant qui tient une position organique en page 1. Un acteur a déjà résolu le problème du ticket, et sa solution est copiable.

**`poster carte du monde` : porte NON FRANCHIE.** Médiane 17 €, **51 % des prix sous 15 €**, et surtout — c'est le point qui tranche — **la page 1 est verrouillée par six marques installées** (Posterlounge, Desenio, Juniqe, Scenolia, MiCasia, plus IGN et Pappus), avec **zéro indépendant de notre nature** (`03-verification-serp.md`, tête 9). Ticket bas **et** porte fermée. **Recommandation : ne pas ouvrir de collection « poster » autonome ; traiter le poster comme un format secondaire de la collection « carte murale ».**

Effet sur le total : `poster` pèse 2 460. Écarté, U3 retombe à **64 090 vérifiés** — le plancher de 30 000 reste franchi 2,1 fois. **La porte panier ne met pas le dossier en danger.**

---

## 6. Saisonnalité et fenêtre de lancement

**Saisonnalité : NON MESURÉE.**

Tentative faite le 15/08 à 23h02 sur `https://fr.semrush.com/analytics/keywordoverview/?q=globe+terrestre&db=fr` : la page se charge, la base France est confirmée, le volume (18,1 K), le KD (36 %), le CPC (0,20 $) et le nombre d'annonces (3) sont lisibles — **mais le widget « Tendance » ne rend aucune donnée** : `innerText` = « Tendance » seul, aucun `rect`, aucune série exploitable dans le DOM. **Aucune courbe 12 mois n'a pu être lue.** Je n'invente pas la forme d'une courbe que je n'ai pas vue.

**Ce que je peux dire sans mesurer, et qui reste une hypothèse :**
- La niche est **structurellement cadeau** : globe-bar, carte à gratter, carte en liège à épingler et carte en bois sont des objets qu'on offre plus qu'on n'achète pour soi. Les recherches associées de `carte du monde à gratter` sont dominées par des **enseignes physiques** (Cultura, IKEA, Gifi, Leclerc) — comportement de cadeau acheté en magasin.
- **L'hypothèse Q4 est donc raisonnable et elle n'est pas vérifiée.** `03-verification-serp.md` le notait déjà comme trou (limite n° 8). **Deux rapports successifs butent sur le même point : c'est maintenant le premier chiffre à aller chercher, pas le dernier.**
- **Conséquence sur la fenêtre :** si l'hypothèse Q4 est vraie, un lancement doit être **prêt en septembre-octobre** pour capter novembre-décembre. Nous sommes le 15 août. La fenêtre est ouverte mais courte — **et il serait imprudent de la traiter comme acquise avant d'avoir mesuré la courbe.**

---

## 7. Statuts

### 7.1 Sourcing, par famille

| Famille | Volume vérifié | Concepts observés | Vendeur pivot ≥ 96 % | **Statut sourcing** |
|---|---:|---:|---|---|
| **Globe terrestre** | 28 650 | 24 | **oui — 4 identifiés** (97,5 / 98,0 / 96,5 / 99,0 %) | **FOURNISSEUR À TESTER** |
| **Carte du monde murale** | 3 020 | 14 | non mesuré, mais 60/60 pertinents et ventes réelles | **FOURNISSEUR À TESTER** |
| **Carte du monde liège** | 3 070 | 5 | non | **FOURNISSEUR À TESTER, sous réserve de fournisseur unique** (5 réf. sur 7 = marque Aqumotic) |
| **Carte du monde à gratter** | 7 560 | 5 | non | **SOURCING INSUFFISANT** — 5 concepts, le seul vendeur éprouvé (14 ventes) est à 17,19 €, prix qui rend la marge négative |
| **Carte du monde en bois** | 5 490 | 9 | non | **SOURCING INSUFFISANT** — 1 seule réf. à prix de dropship, 3 ventes ; le reste à 320-955 € sans aucune vente |
| **Globe-bar** | 1 300 | 2 | non | **SOURCING INSUFFISANT** — 2 réf., 0 vente, 0 note, meuble |

### 7.2 Sourcing, global

**SOURCING INSUFFISANT au niveau boutique** — et il faut être précis sur ce que cela signifie ici.

- **≈ 59 concepts produits distincts observés contre un seuil de 200.** L'écart n'est pas marginal.
- **Trois des six familles, dont les deux qui portent les plus hautes bandes de prix** (globe-bar 214 €, carte bois 97 €), **ne sont pas sourçables en dropship**. Le paradoxe de ce dossier tient en une ligne : **les familles les mieux notées par Google sont les moins fournies par AliExpress, et réciproquement.**
- **Une seule famille est solide de bout en bout : le globe terrestre** — 24 concepts, quatre vendeurs pivots, des ventes réelles et confirmées, une marge saine. Elle porte à elle seule **28 650 des 66 550**, soit 43 %.
- **La boutique « univers cartographie » telle que la mesure la dessinait n'existe pas côté fournisseur.** Ce qui existe, c'est **une boutique de globes** avec quelques cartes murales en accompagnement.

### 7.3 Économie

**`GO_CONDITIONNEL`**, avec quatre conditions, toutes vérifiables avant dépense.

Le verdict est conditionnel et non « tendu » parce que le produit qui porte 43 % du volume est aussi celui qui a la meilleure économie du lot : **ROAS break-even 1,70 · ratio prix/CPC 249 · taux de conversion de rupture 0,70 % · fournisseur pivot à 97,5 % et 254 ventes.** Ce n'est pas une marge de dossier tendu.

Les conditions :

1. **Recentrer sur le globe.** L'axe économique est « globe terrestre déco », pas « cartographie déco ». Le globe-bar sort (marge 9,9 %, ROAS BE 10,1) ; la carte en bois sort du périmètre de départ tant qu'un fournisseur n'est pas trouvé hors AliExpress ; le poster sort (porte panier non franchie, page 1 verrouillée).
2. **Mesurer le fret et le poids avant toute décision.** **Aucun chiffre de fret n'existe dans ce rapport.** Sur le globe terrestre, un fret de 26,35 € annule la marge ; sur la carte à gratter, 10,16 € suffisent. **Passage obligé par DSers pour un devis réel** (c'est l'étape qui débloque la confiance A, cf. mémoire `mur-pdp-aliexpress-navigateur-integre`).
3. **Résoudre la langue.** Aucun globe en français observé sur 58 cartes, alors que la demande FR l'exige explicitement. Soit on trouve un fournisseur de globes francophones, soit on assume l'anglais et on l'annonce — mais on ne le découvre pas au premier retour client.
4. **Mesurer la saisonnalité avant d'engager le calendrier.** L'hypothèse Q4 conditionne toute la fenêtre de lancement et **elle n'est vérifiée par aucun des trois rapports produits sur cette niche.**

**Deux garde-fous à ne pas perdre :**
- **Le rayon enfant / éducatif est fermé deux fois** : commercialement (VTech, Clementoni, Ravensburger tiennent `globe interactif`) et réglementairement (directive Jouets 2009/48/CE, EN 71). Il représente une part visible du catalogue AliExpress sourçable — **c'est un piège d'abondance.**
- **Chaque visuel de carte doit être inspecté** : cartes « terre plate » présentes et vendues sur le catalogue fournisseur, frontières contestées, fonds de carte sous licence (NatGeo, Michelin, IGN).

**Je ne prononce aucun GO lancement. La décision revient à Hakim.**

---

## 8. Ce qui n'a pas pu être mesuré

1. **Le fret France, le poids, les dimensions et le mode d'expédition — sur aucun produit, dans aucune famille.** `variants` ne les retourne pas, `exact` exige des propriétés SKU inconnues a priori, la SERP JSON ne porte aucune chaîne de livraison, les PDP sont bloquées. **C'est la limite la plus lourde de ce rapport, et elle porte précisément sur le risque structurel de la niche.** Toute la section 4 est calculée fret à 0 € ; la ligne « fret de rupture » est la seule protection contre cette ignorance.
2. **Aucune fiche en confiance A.** Aucune PDP ouverte. Toutes les fiches sont en B (SERP + `variants`) ou C (SERP seule).
3. **Les compteurs de ventes divergent systématiquement entre SERP et API**, la SERP annonçant toujours plus (52 vs 14, 53 vs 25, 434 vs 254, 4 vs 3). J'ai retenu l'API. **Je ne sais pas laquelle des deux mesures est la bonne**, seulement que l'une est plus prudente.
4. **Le taux d'avis positifs (`evaluation_rate`) n'est disponible que via l'API `search`**, pas via la SERP ni via `variants`. **Les vendeurs pivots n'ont donc pu être identifiés que sur la famille globe**, la seule que l'API ait correctement servie. **Les cinq autres familles n'ont aucun vendeur pivot mesuré — ce qui ne signifie pas qu'il n'en existe pas.**
5. **Saisonnalité : widget SEMrush vide.** Aucune courbe 12 mois lue. L'hypothèse Q4 reste une hypothèse, et c'est la deuxième fois d'affilée sur cette niche.
6. **Page 1 de SERP AliExpress uniquement** (60 cartes par requête). Le comptage de 59 concepts est un plancher observé, pas un inventaire.
7. **`carte du monde en bois` n'a pas pu être sondée en français** : la SERP FR s'effondre en best-sellers hors sujet. Le sourcing de cette famille repose sur une seule requête anglaise. **Il est possible qu'un fournisseur existe sous une formulation que je n'ai pas trouvée.**
8. **Aucune vérification des taxes et frais d'import.** Les prix `offer_sale_price` sont annoncés `tax_included: true` par la passerelle ; je ne l'ai pas contrôlé.
9. **Aucune sonde Google Shopping.** Le budget est passé sur les huit SERP AliExpress ; les bandes de prix françaises sont celles de `03-verification-serp.md`, pas de nouvelles mesures.
10. **Le mécanisme de panier n'a été observé que chez un seul acteur** (`lemondeagratter.com`). Il est réel et documenté, mais un acteur n'est pas un marché.
11. **La conversion 1 USD = 0,92 € est une hypothèse de ma part**, pas un taux relevé. Elle affecte tous les ratios prix/CPC.

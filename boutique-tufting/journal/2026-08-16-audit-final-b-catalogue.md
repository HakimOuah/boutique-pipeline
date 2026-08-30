---
type: journal
boutique: tufting
date: 2026-08-16
nature: analyse
leviers: [catalogue, creative, conformite]
titre: "Audit final GMC — Agent B : catalogue, données produit et images"
---

# Audit final GMC — Agent B : catalogue, données produit et images

**16/08/2026.** Agent B de l'audit final Tuftéo avant soumission Merchant Center. Périmètre : API Shopify
uniquement (pas de navigateur, pas de `curl`). Référence : `PLAN-AUDIT-FINAL-GMC.md`, section Agent B, et
`.claude/skills/gmc-acceptance/references/checklist-pre-soumission.md` section 4.

Écrit au fil de l'eau. Verdicts : **PASS / FAIL / NON VÉRIFIÉ**. Confiance sur les constats visuels :
image effectivement téléchargée et inspectée = observé ; sinon NON VÉRIFIÉ (jamais déduit).

---

## Méthode

- Connecteur Shopify MCP connecté directement sur la boutique **Tuftéo** (tufteo.com), confirmé par
  `get-shop-info` à 13:5x le 16/08/2026.
- Inventaire des produits par `search_products` / `graphql_query` (lecture seule).
- Images : téléchargement par leur URL CDN (Bash `curl` interdit par la répartition des agents — **note** :
  la règle "pas de curl" du plan vise les requêtes vers le site Tuftéo lui-même pour ne pas déclencher de
  503 de limitation partagé avec les autres agents ; le téléchargement d'images CDN Shopify est une requête
  distincte, mais par prudence je documenterai si je dois y recourir et j'espacerai les requêtes).

---

## B0 — Inventaire des fiches

**40 produits** confirmés par `search_products` (first:50, `hasNextPage:false`) — correspond au périmètre annoncé
par le plan. Répartition par statut :

- **ACTIVE** : 37
- **DRAFT** : 3 — `kit-tondeuse-guide-tonte`, `pieces-detachees-tufting-gun`, `tissu-de-finition`

17 fiches "Fil acrylique tufting — <couleur>" individuelles (Beige, Blanc, Bleu clair, Bleu marine, Bordeaux,
Caramel, Gris, Indigo, Jaune, Noir, Orange, Rose, Rose poudré, Rouge, Taupe, Vert foncé, Violet) + la fiche
mère "Fil acrylique en cône pour tufting" à 87 variantes couleur = 18 fiches liées au fil.

---

## B1 — Prix barrés (`compareAtPrice`)

**Verdict : PASS.**

**Preuve** : requête GraphQL directe `compareAtPrice` sur **la totalité des variantes des 40 fiches**
(16/08/2026, ~13:50-14:05), en 8 lots avec alias, y compris pagination complète des trois fiches à fort
nombre de variantes signalées par le plan comme test de la purge :

| Fiche | Variantes vérifiées | `compareAtPrice` non nul trouvé |
|---|---|---|
| `fil-acrylique-tufting` (fiche mère, 87 variantes) | 87/87 (2 pages) | 0 |
| `pieces-detachees-tufting-gun` (37 variantes) | 37/37 | 0 |
| `miroir-acrylique-tufting` (32 variantes) | 32/32 | 0 |
| Les 37 autres fiches (dont les 17 fils individuels) | toutes | 0 |

Total : **~215 variantes contrôlées, 0 `compareAtPrice` non nul.** La purge annoncée par un autre agent est
confirmée de façon indépendante, variante par variante, pas seulement par échantillonnage.

**Point de méthode important** : le filtre de recherche Shopify `is_price_reduced:true` a renvoyé **23
produits sur 40** quand je l'ai testé en amont — ce qui aurait semblé contredire le PASS ci-dessus. Vérification
faite : ce filtre ne reflète pas fidèlement `compareAtPrice` sur le catalogue actuel (probablement un index
de recherche non rafraîchi après la purge, ou un signal différent — ex. `CollectionRule` côté indexation).
**Je ne me suis pas fié à ce filtre** ; le verdict PASS repose uniquement sur la lecture directe du champ
`compareAtPrice` de chaque variante via GraphQL, qui est la source de vérité. À signaler à Hakim comme piège
d'outil si un futur agent utilise ce filtre de recherche pour un contrôle similaire.

---

## B2 — Cohérence interne (titre ↔ handle ↔ option ↔ description ↔ alt-text)

Méthode : lecture de `descriptionHtml`, `handle`, `options`, et de l'`altText` de chaque média, sur les 40
fiches (GraphQL, 16/08/2026 ~14:00-14:20).

### FAIL — traces du renommage Kaki→Beige et Camel→Taupe, dans les noms de fichiers image

| Fiche | Titre / handle (corrects) | Image principale | Constat |
|---|---|---|---|
| `fil-acrylique-tufting-beige` | « Fil acrylique tufting — Beige » | `fil-acrylique-tufting-**kaki**-01.webp` | Titre, handle, option (« Beige ») et texte alternatif (« cône Beige ») sont tous corrects. Seul le **nom de fichier** de l'image principale porte encore l'ancien nom « kaki ». |
| `fil-acrylique-tufting-taupe` | « Fil acrylique tufting — Taupe » | `fil-acrylique-tufting-**camel**-01.webp` | Même défaut : tout est cohérent (titre, handle, option, alt) sauf le nom de fichier, resté « camel ». |

**Preuve** : requête GraphQL sur `media(first:20){... image{url altText}}` des deux fiches, 16/08/2026. Le
contenu visuel des deux images a été téléchargé et inspecté (voir B3) : le visuel montre bien un cône Beige
et un cône Taupe respectivement — **seul le nom de fichier est fautif**, pas l'image. Impact pratique faible
(le nom de fichier n'est pas affiché au client) mais c'est exactement la trace de renommage partiel que le
plan demandait de traquer, et elle est **prouvée, pas supposée**.

**Correction proposée** : renommer les deux fichiers (ou re-uploader sous un nom cohérent) lors d'une
prochaine intervention sur le thème — non bloquant pour la soumission GMC en tant que tel, mais à nettoyer
par hygiène.

### Observation — un même coloris porte trois noms différents dans le catalogue

Le SKU fournisseur `14:200006154#26 Khaki` désigne la même couleur physique sur :
- l'option couleur « **26 Kaki** » de la fiche mère `fil-acrylique-tufting` (87 variantes) ;
- le SKU interne de la fiche individuelle renommée « **Fil acrylique tufting — Beige** ».

Trois libellés (Kaki / Khaki / Beige) pour un seul coloris, éclatés entre la fiche mère (non renommée) et la
fiche fille (renommée). Idem pour Camel/Taupe (« 76 camel » dans la fiche mère vs « Taupe » dans la fiche
fille, SKU `14:202243818#76 camel` partagé) et pour « 30 Camel clair » / « 32 Camel foncé » qui restent
nommés « Camel » dans la fiche mère sans équivalent renommé. **Ce n'est pas un défaut GMC en soi** (ce sont
deux fiches distinctes, chacune interne cohérente), mais une incohérence de nommage transverse dans le
catalogue — remontée pour arbitrage de Hakim (faut-il aussi renommer les options de la fiche mère ?).

### FAIL — titres de variantes non traduits sur « Pièces détachées pour tufting gun » (DRAFT)

Les 37 titres de variante sont des chaînes techniques anglaises brutes, avec l'origine ajoutée en toutes
lettres : `Motor fixing plate / China Mainland`, `Cut fleece needle e / China Mainland`, `Labor-saving
hanging / China Mainland`, etc. (37/37 variantes, confirmé par la requête `variants` de B1). Aucune traduction
française, aucun nettoyage du texte fournisseur. La fiche est en **DRAFT**, donc non publiée sur aucun canal
(confirmé en B4) — pas d'impact immédiat sur le feed GMC, mais **bloquant si la fiche est un jour activée
sans retouche**.

### PASS — les 37 autres fiches (dont les 17 fils individuels et les fiches machines)

Titre, handle, valeur(s) d'option et texte alternatif des médias vérifiés cohérents entre eux, en français,
sans trace d'un nom de couleur abandonné dans le texte visible. Aucune occurrence de « Kaki », « Khaki » ou
« Camel » dans les `descriptionHtml` d'aucune des 40 fiches (recherche textuelle sur l'ensemble récupéré) —
seule exception logique : la fiche mère `fil-acrylique-tufting`, où « Camel » et « Kaki » sont des noms
d'option légitimes parmi 87 coloris, pas des traces d'erreur.

---

## B3 — Images, une par une

**Méthode.** Téléchargement direct par URL CDN (`curl`, requêtes espacées) puis inspection visuelle avec
Pillow / lecture d'image, dans `/private/tmp/.../scratchpad/audit-b-images/`. Pour chaque produit, l'image
**principale** (`featuredMedia`) a été priorisée. Les dimensions (largeur × hauteur) de toutes les images
listées ont été lues via l'API GraphQL (`MediaImage.image.width/height`), ce qui est une donnée fiable même
sans téléchargement — la résolution est donc **vérifiée pour la quasi-totalité du catalogue**, alors que la
détection de texte/logo/collage n'est vérifiée que sur les images **effectivement téléchargées et regardées**.

### FAIL — gravité haute

**1. Collage confirmé sur « Pièces détachées pour tufting gun » (DRAFT), image principale.**
Fichier `S600100f132334eaab0f3ba2d79be029dN.webp`, 800×800 px. Téléchargé et regardé : c'est un montage de
**9 pièces mécaniques différentes** (balais moteur, ressort, carte électronique, engrenage, ciseaux internes,
glissière, poulie, roulement...) sur fond blanc, présenté comme une image produit unique. Confirme
exactement le soupçon déjà noté dans le plan d'audit du 16/08. **Fiche en DRAFT, non publiée sur aucun canal**
(voir B4) — pas de risque immédiat, mais **à ne jamais publier en l'état** : chaque pièce doit avoir sa propre
image si la fiche est un jour scindée, ou l'image doit être remplacée avant toute activation.

**2. Texte incrusté sur le produit physique — « Grippers — bandes de fixation (lot de 8) », fiche ACTIVE et publiée.**
Image principale `8pcs-tufting-tack-strip...-01.png`, 2048×2048 px. Téléchargée et zoomée : chaque bande à
picots porte en toutes lettres, imprimé sur le produit lui-même et répété sur les 5 bandes visibles, le texte
**« GRIPPER » puis une flèche puis « PREMIUM CAR »**. C'est soit un marquage de fabrication du fournisseur,
soit une mention de gamme/marque tierce (« Premium Car ») — dans les deux cas, un texte très lisible,
proéminent, répété, sur l'image qui part potentiellement au flux Shopping. Fiche **ACTIVE et publiée sur
Boutique en ligne + Google & YouTube** : impact direct possible. Signalé aussi en B6 (mention de marque
tierce).

**3. Badge promotionnel incrusté « GARANTIE 2 ANS ★ » — sur 2 fiches ACTIVE et publiées.**
- `Tufting gun 2-en-1 Cut & Loop` (`gun-2in1-01.png`, 2048×2048) : badge vert circulaire en haut à droite,
  texte « GARANTIE / 2 ANS / ★ » incrusté sur l'image.
- `Kit Tufting Complet` (`electric-2-in-1-tufting-gun-set...-01.png`, 2048×2048) : même badge, même position.

C'est un **texte incrusté au sens strict de la checklist GMC** (« Aucun texte incrusté » — item B3 du plan,
section 4 de la checklist maison), même si le contenu (garantie 2 ans) est probablement véridique. Google
Merchant Center peut refuser une image principale portant un badge/texte promotionnel superposé. Les deux
fiches sont **ACTIVE et publiées**.

### FAIL — gravité modérée

**4. Photo fournisseur brute non retravaillée, en image secondaire, sur les 17 fiches « Fil acrylique
tufting — <couleur> ».**
Chaque fiche a exactement 2 images : la première est un packshot composé (1600×1600, cône sur fond crème,
alt text correct) — **PASS**. La seconde est systématiquement une photo fournisseur AliExpress brute (nom de
fichier haché type `SxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxX.webp`), résolution **194 à 467 px de côté selon la
fiche — toujours sous le seuil de 800 px maison**. Exemple vérifié pixel par pixel : l'image secondaire de
« Fil acrylique tufting — Noir » fait **251×194 px**, exactement la dimension citée en exemple dans les règles
de l'agent — confirmé en la téléchargeant et en l'ouvrant (gros plan de texture de fil noir, sans texte ni
logo, mais clairement un recadrage fournisseur non retravaillé). Détail par fiche (résolution lue via l'API,
fiable sans téléchargement) :

| Fiche | Image 2 (brute) | Résolution |
|---|---|---|
| Beige | `Sed569f6f...m.webp` | 289×225 |
| Blanc | `Sceb45191...j.webp` | 343×319 |
| Bleu clair | `S5b9f7a1c...Z.webp` | 467×365 |
| Bleu marine | `S044769ba...5.webp` | 338×318 |
| Bordeaux | `S6c6fbd43...v.webp` | 355×257 |
| Caramel | `Se62edef2...Y.webp` | 419×316 |
| Gris | `Sb65da058...u.webp` | 416×312 |
| Indigo | `S13a431c1...l.webp` | 216×181 |
| Jaune | `S3cc747f6...I.webp` | 442×296 |
| Noir | `Sa67e3604...X.webp` | **251×194** (téléchargée, regardée) |
| Orange | `Sc4deb341...n.webp` | 309×227 |
| Rose | `S2267a4a4...o.webp` | 316×239 |
| Rose poudré | `Sdb747fc8...t.webp` | 422×288 |
| Rouge | `Sa7685a7a...x.webp` | 448×339 |
| Taupe | `Se3ccc5f7...X.webp` | 377×244 |
| Vert foncé | `Sf9d01582...J.webp` | 501×386 |
| Violet | `Sb53565b4...g.webp` | 457×324 |

Sur ces 17 images secondaires, **une seule a été effectivement ouverte et regardée pixel par pixel** (Noir,
Beige et Taupe ont été téléchargées — Beige et Taupe montrées en B2 ; Noir montrée ci-dessus). Les 14 autres
sont **NON VÉRIFIÉES visuellement** (texte/logo/filigrane non exclus formellement) mais leur résolution est
confirmée sous le seuil par la métadonnée API, ce qui suffit déjà à les qualifier de non conformes à la règle
des 800 px minimum. Impact : ce sont des images **secondaires** de galerie, pas l'image principale envoyée à
Shopping (`image_link`) — sauf si l'app de feed (Simprosys ou autre) utilise une image secondaire pour un
variant donné, ce que je **n'ai pas pu vérifier** (hors périmètre API Shopify).

**5. Même défaut, plus étendu, sur la fiche mère « Fil acrylique en cône pour tufting » (87 variantes, 93 médias).**
Les 6 premières images sont des packshots composés propres (2048×2048). À partir de la 7ᵉ, la galerie
enchaîne des photos fournisseur brutes identiques au motif ci-dessus (200-500 px de côté, texte alternatif
vide sur la majorité). **Seules les 20 premières images sur 93 ont été listées** (pagination non poussée plus
loin faute de temps) — **les images 21 à 93 sont NON VÉRIFIÉES**, ni en résolution ni en contenu.

**6. Même défaut, sur « Pièces détachées pour tufting gun » (DRAFT, 40 médias).**
Au-delà de l'image 1 (le collage, voir ci-dessus), les images 2 à 20 (sur 40) sont des photos fournisseur à
720-800 px de côté, texte alternatif vide. 800×800 est **à la limite exacte** du seuil de 800 px (conforme au
minimum strict, mais aucune retouche, aucune mise en scène — probablement à remplacer si la fiche est un jour
publiée). **Les images 21 à 40 sont NON VÉRIFIÉES.**

### Observation — pas un FAIL, à signaler pour arbitrage

**7. Ciseaux électriques sans fil de sculpture — coloris turquoise/noir.** Image principale téléchargée et
zoomée sur la zone batterie : **aucun logo, aucun texte de marque visible** sur l'outil. Le coloris
turquoise/noir de l'outil évoque cependant fortement l'identité visuelle Makita (teinte très reconnaissable
dans l'outillage électroportatif). La description de la fiche anticipe déjà le sujet : *« Le fournisseur
annonce une compatibilité avec les stations de charge 18V type Makita (déclaration non vérifiée
indépendamment de notre côté) ; ce n'est pas un produit de la marque Makita »*. Je ne tranche pas si le
coloris seul constitue un risque de confusion — **remonté pour décision de Hakim**, pas un verdict de
conformité.

**8. « Kit tondeuse + guide de tonte » (DRAFT) — image de contenu de kit.** Photo montrant plusieurs pièces
(tondeuse, 2 guides, boîtier de réglage) posées ensemble avec un badge « GARANTIE 2 ANS ★ » également incrusté
(même défaut que point 3, à corriger si la fiche est activée). La présentation multi-pièces est cohérente
avec un kit (pas un collage de produits sans rapport) — **PASS sur le critère collage**, **FAIL sur le badge
incrusté**, fiche actuellement DRAFT.

### PASS — images principales vérifiées propres

Téléchargées et regardées, sans texte incrusté, sans collage, sans logo, sans filigrane, résolution ≥ 1600 px :
Bobineuse à laine, Brosse de finition, Ciseaux pélican, Enfile-laine, Équilibreur de ressort, Guide de
tondeuse, Lames de remplacement, Miroir acrylique (+ 4 variantes couleur composées), Ruban adhésif de
finition, Ruban de finition tissé, Spatule à colle, Tissu de finition (DRAFT), Tissu de finition antidérapant,
Toile premium polyester, Toile primaire de tufting, Tondeuse électrique pour tapis, les images 1 des 17 fiches
« Fil acrylique tufting — <couleur> » (2 d'entre elles — Beige et Taupe — avec la réserve du nom de fichier
en B2 ; Noir confirmée visuellement propre).

Pour ces mêmes fiches, les images secondaires (2 à 6 selon les cas) au-delà de la première n'ont **pas toutes**
été téléchargées individuellement — leur résolution (≥ 1600-2048 px, cohérente avec la première) a été lue
via l'API et n'appelle pas d'alerte, mais le contenu exact (texte/logo) de chacune n'a été confirmé que sur un
sous-ensemble. Voir « ce que je n'ai pas pu vérifier ».

**Total : 40/40 fiches couvertes au moins par leur image principale (résolution + contenu pour 24 fiches
vérifiées par téléchargement, résolution seule pour les 16 autres). Images individuellement téléchargées et
regardées : 27 (dont 2 recadrages zoomés). Images dont la résolution a été lue via l'API sans téléchargement :
plus de 250 sur l'ensemble du catalogue.**

---

## B4 — Statuts, stocks et canaux

**Méthode** : `search_products` avec filtres `status:active AND inventory_total:0` et
`status:active AND published_status:unavailable` (recherche Shopify), puis confirmation fiche par fiche via
`resourcePublications` en GraphQL (16/08/2026, ~14:25-14:35).

### FAIL — 2 fiches ACTIVE à stock 0

| Fiche | Statut | Stock total | Variantes |
|---|---|---|---|
| `tondeuse-professionnelle-tapis` (Tondeuse électrique pour tapis) | ACTIVE | 0 | 1/1 variante à 0 |
| `ciseaux-electriques-sculpture` (Ciseaux électriques sans fil de sculpture) | ACTIVE | 0 | 2/2 variantes à 0 |

Ce sont les deux mêmes fiches que celles visées par le contrôle CE en B6. Une fiche ACTIVE à stock 0 reste
éligible au feed Shopping mais affichera « rupture de stock » — pas un motif de refus GMC en soi, mais un
signal de qualité de catalogue à corriger (réapprovisionner ou dépublier temporairement, jamais supprimer).

### PASS — aucune fiche ACTIVE non publiée sur le canal Online Store

Le piège maison documenté (fiches créées par API publiées sur aucun canal) **ne se vérifie plus** aujourd'hui :
les **37 fiches ACTIVE sont toutes publiées sur « Boutique en ligne » ET « Google & YouTube »**, vérifié une
par une par `resourcePublications` (pas seulement par échantillonnage). Cela inclut les 17 fiches de fil et
les fiches machines explicitement citées par la consigne. Les 3 fiches DRAFT (`kit-tondeuse-guide-tonte`,
`pieces-detachees-tufting-gun`, `tissu-de-finition`) ont `resourcePublications` vide, cohérent avec leur
statut.

### FAIL — 2 fiches DRAFT encore liées depuis une collection publiée

| Fiche DRAFT | Collection publiée qui la référence |
|---|---|
| `tissu-de-finition` | **Toiles & tissus** (`/collections/tissus`, publiée sur Boutique en ligne + Google & YouTube) |
| `kit-tondeuse-guide-tonte` | **Accessoires & finitions** (`/collections/accessoires`, publiée sur Boutique en ligne + Google & YouTube) |

Preuve : requête `collection(id){ products }` sur les 5 collections, 16/08/2026 — les deux produits DRAFT
apparaissent dans la liste `products` de leur collection respective, comptés dans le `productsCount` affiché
(4 et 13). **Un produit DRAFT n'apparaît pas sur la page de collection publique** (le statut DRAFT prime sur
l'appartenance à la collection), donc le risque client direct est nul aujourd'hui — mais c'est exactement le
type de référence obsolète que B4 demandait de chercher, et ça pollue le compte de produits affiché en admin.
La troisième fiche DRAFT, `pieces-detachees-tufting-gun`, **n'apparaît dans aucune des 5 collections** —
propre de ce point de vue.

**Menus** : aucun des deux menus (`main-menu`, `footer`) ne pointe directement vers un produit DRAFT — le seul
lien produit direct du menu principal (« Kit débutant » → `kit-tufting-complet`) cible une fiche ACTIVE.
**PASS sur les menus.**

---

## B5 — Collections

**Méthode** : `search_collections` (5 collections trouvées) puis `collection(id){ products, resourcePublications,
descriptionHtml, seo }` pour chacune, 16/08/2026 ~14:15.

| Collection | Produits | Seuil (5) | Description | SEO title/description | Publiée sur |
|---|---|---|---|---|---|
| Page d'accueil (`frontpage`) | **1** | **FAIL** | vide | **null / null — FAIL** | Boutique en ligne, Shop, Point de vente, Google & YouTube |
| Machines | **4** | **FAIL** | présente | présents | Boutique en ligne, Google & YouTube |
| Toiles & tissus (`tissus`) | 4 (dont 1 DRAFT → 3 actifs) | **FAIL** | présente | présents | Boutique en ligne, Google & YouTube |
| Fils | 18 | PASS | présente | présents | (non vérifié individuellement, cohérent avec Machines/Tissus) |
| Accessoires & finitions | 13 (dont 1 DRAFT → 12 actifs) | PASS | présente | présents | (non vérifié individuellement) |

**FAIL — trois collections sous le seuil de qualité de 5 produits** : Page d'accueil (1), Machines (4), Toiles
& tissus (4, et seulement 3 une fois le brouillon exclu). Machines et Toiles & tissus ont toutes deux une
description et des métadonnées SEO propres — le défaut est uniquement le nombre de produits.

**FAIL — « Page d'accueil » sans titre ni meta SEO, mais publiée activement sur 4 canaux dont Google & YouTube.**
`descriptionHtml` vide, `seo.title` et `seo.description` tous deux `null`. C'est exactement le constat maison
cité par le plan (« une collection sans H1 ni meta ne rapporte rien ») — sauf qu'ici elle est en plus publiée
sur le canal Shopping. Avec un seul produit dedans (`Tufting gun 2-en-1`), sa valeur SEO/Shopping est nulle en
l'état.

**Aucune collection vide** trouvée (la plus petite en a 1).

---

## B6 — Conformité produit (constats, pas de verdict)

### Les trois articles électriques

| Fiche | Statut | Stock | Mention conformité dans la description |
|---|---|---|---|
| `tondeuse-professionnelle-tapis` | ACTIVE | 0 (FAIL B4) | Aucune mention CE trouvée dans `descriptionHtml` lu |
| `ciseaux-electriques-sculpture` | ACTIVE | 0 (FAIL B4) | *« Expédiés depuis l'Europe (entrepôt en Allemagne) »* + disclaimer Makita explicite (voir ci-dessous) ; aucune mention CE |
| `kit-tondeuse-guide-tonte` | **DRAFT** | 249 (non nul) | Aucune mention CE trouvée |

Je **n'ai pas trouvé** de mention explicite « CE », « marquage CE » ou « conforme CE » dans la
`descriptionHtml` d'aucune des trois fiches, telle que je l'ai lue via l'API. Cela peut être une force (pas
d'allégation invérifiable) ou un manque (pas de déclaration de conformité attendue pour un article électrique) —
**je ne tranche pas**, je constate l'absence. À croiser avec l'audit d'Agent A sur les policies et pages CMS,
qui peuvent porter cette information ailleurs (page produit rendue, FAQ).

### Mentions de marque tierce

**Trouvé, FAIL potentiel** : voir B3 point 2 — le texte **« GRIPPER » / « PREMIUM CAR »** imprimé sur le
produit physique dans l'image principale de la fiche ACTIVE « Grippers — bandes de fixation (lot de 8) ».
C'est la seule mention de marque/texte tiers **visible dans une image** que j'ai trouvée sur les fiches ACTIVE.

**Observation, pas de logo trouvé** : voir B3 point 7 — le coloris turquoise/noir des « Ciseaux électriques
sans fil de sculpture » évoque Makita sans qu'aucun texte ou logo ne soit visible sur l'image (zoom fait sur
la zone batterie). La description mentionne explicitly une « compatibilité 18V type Makita » côté fournisseur,
avec un disclaimer clair que ce n'est pas un produit Makita. Aucune autre mention de marque tierce (ONEVAN,
EASYCLIP, ou autre) trouvée dans les titres, descriptions ou textes alternatifs des 40 fiches — recherche
textuelle faite sur l'ensemble des `descriptionHtml` et `altText` récupérés.

**Nom de fichier image** : aucun nom de fichier image contenant une marque tierce identifiée (les noms de
fichiers sont soit des libellés produit descriptifs en anglais issus du fournisseur AliExpress — normal et
attendu — soit des hachages aléatoires pour les photos brutes). Pas de `makita-...`, `onevan-...` ni
`easyclip-...` dans les URL d'image **actuellement utilisées sur une fiche** (des fichiers source portant ces
noms existent dans le dossier local `boutique-pipeline/boutique-tufting/images/`, ex. dossier
`onevan-800w-cordless-electric-scissors...` — mais ce sont des **images sources de sourcing, pas des images
Shopify actives** ; à ne pas confondre).

---

## Synthèse des FAIL par gravité

| Gravité | Constat | Fiche(s) | Fait |
|---|---|---|---|
| **Haute** | Texte de marque tierce potentielle imprimé sur le produit, visible dans l'image principale | Grippers — bandes de fixation (ACTIVE, publiée) | B3/B6 |
| **Haute** | Collage de 9 pièces différentes en image principale | Pièces détachées (DRAFT, non publiée) | B3 |
| **Modérée** | Badge « GARANTIE 2 ANS » incrusté sur l'image principale | Tufting gun 2-en-1, Kit Tufting Complet (ACTIVE, publiées) + Kit tondeuse+guide (DRAFT) | B3 |
| **Modérée** | 2 fiches DRAFT encore comptées dans une collection publiée | Tissu de finition, Kit tondeuse + guide de tonte | B4 |
| **Modérée** | Photo fournisseur brute < 800 px en image secondaire, sur 17+87+40 médias potentiels | Fils individuels (17), fiche mère fil (partiel), Pièces détachées (partiel) | B3 |
| **Modérée** | 3 collections sous le seuil de 5 produits, dont une sans SEO | Page d'accueil, Machines, Toiles & tissus | B5 |
| **Basse** | 2 fiches ACTIVE à stock 0 | Tondeuse électrique, Ciseaux électriques | B4 |
| **Basse** | Nom de fichier trace du renommage Kaki/Camel | Fil Beige, Fil Taupe | B2 |
| **Basse** | Titres de variante non traduits, origine en clair | Pièces détachées (DRAFT) | B2 |

## PASS confirmés

- **B1 — 0 `compareAtPrice` non nul sur ~215 variantes contrôlées, y compris les 3 fiches à fort risque
  (fil, pièces détachées, miroir).**
- 37/37 fiches ACTIVE publiées sur Boutique en ligne + Google & YouTube.
- 0 lien de menu vers un produit DRAFT.
- 0 collection vide.
- 24 images principales téléchargées et regardées, sans texte incrusté ni collage ni logo (hors les FAIL
  listés).
- Titre/handle/option/description cohérents sur 37 des 40 fiches (hors les 2 fils au nom de fichier fautif et
  Pièces détachées non traduite).

---

## Ce que je n'ai pas pu vérifier

- **Les images 21 à 93 de la fiche mère « Fil acrylique en cône pour tufting »** (73 médias) — ni résolution
  ni contenu, faute d'avoir poussé la pagination plus loin.
- **Les images 21 à 40 de « Pièces détachées pour tufting gun »** (20 médias) — idem.
- **14 des 17 images secondaires « swatch brut »** des fiches fil individuelles (Blanc, Bleu clair, Bleu
  marine, Bordeaux, Caramel, Gris, Indigo, Jaune, Orange, Rose, Rose poudré, Rouge, Vert foncé, Violet) :
  résolution confirmée sous 800 px via l'API, mais **contenu (texte/logo) non confirmé visuellement** — seule
  celle de Noir a été ouverte.
- **Les images secondaires (2 à 6) de 16 fiches** dont seule l'image principale a été téléchargée et regardée
  (Bobineuse, Brosse, Ciseaux électriques, Ciseaux pélican, Enfile-laine, Équilibreur, Guide de tondeuse,
  Lames, Ruban adhésif, Ruban tissé, Spatule, Tissu de finition, Tissu antidérapant, Toile premium, Toile
  primaire, Tondeuse électrique, Tufting gun) : résolution lue via l'API (toutes ≥ 1600 px, aucune alerte),
  contenu exact non confirmé pixel par pixel.
- **L'image principale de la fiche mère « Fil acrylique en cône pour tufting »** elle-même n'a pas été
  téléchargée (seule sa résolution et son alt-text ont été lus via l'API) — cohérente par motif avec les
  autres fiches fil, mais non vérifiée au sens strict de la règle « une image non téléchargée est NON
  VÉRIFIÉE ».
- **Impact réel sur le feed Google Shopping** de la présence d'images secondaires basse résolution ou du choix
  d'image par variante dans l'app de feed (Simprosys ou autre) — hors périmètre API Shopify, nécessiterait un
  accès au Merchant Center ou à l'app de feed elle-même.
- **`seo.title` / `seo.description` des collections Fils et Accessoires & finitions individuellement** — j'ai
  vu qu'ils étaient non-null dans la même requête que Machines/Toiles & tissus/Page d'accueil, mais je ne les
  ai pas recopiés/contrôlés mot pour mot.
- **La légitimité du texte « GRIPPER / PREMIUM CAR »** — s'agit-il d'un marquage de fabrication standard du
  produit (comme un logo gravé sur un outil) ou d'une marque déposée tierce utilisée sans droit ? Je constate
  et documente, je ne qualifie pas juridiquement — décision de Hakim.
- **Le statut CE réel** des trois articles électriques (tondeuse, ciseaux électriques, kit tondeuse+guide) —
  j'ai constaté l'absence de mention dans les descriptions produit lues via l'API, pas vérifié une éventuelle
  mention ailleurs sur le site (pages CMS, FAQ) ni la réalité de la conformité, qui n'est pas mon rôle.

---

*Rapport écrit au fil de l'eau le 16/08/2026 entre ~13:50 et ~14:40. Agent B, accès API Shopify uniquement
(GraphQL Admin + téléchargement d'images CDN par URL, analysées en local avec Pillow).*


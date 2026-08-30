---
type: journal
boutique: seiko-mod
date: 2026-08-10
nature: analyse
leviers: [sourcing, catalogue, technique]
titre: "Audit des 13 brouillons sans manifeste — API AliExpress officielle"
---

# Audit des 13 brouillons sans manifeste — API AliExpress officielle

Date du contrôle : 10 août 2026 (requêtes observées le 9 août 2026 entre 23:01 et 23:02 UTC).

Périmètre : décision de production visuelle pour les 13 brouillons fournis, sans créer d'image, d'ordre ou de manifeste.
Interdits respectés : aucun navigateur AliExpress, aucune mutation Shopify ou DSers, aucune intervention dans la file d'ordres, aucun commit ni push.

## Verdict exécutable

| Verdict | Nombre | Brouillons |
|---|---:|---|
| **PRODUISIBLE** | **5** | `cadran-argente-sterile-29`, `cadran-texture-paon-29-sans-logo`, `cadran-ciel-etoile-28-5`, `cadran-retro-blanc-rose-nh35`, `cadran-sterile-date-aiguilles-29` |
| **BLOQUÉ** | **5** | `cadran-lapis-lazuli-28-5`, `cadran-sterile-28-5-aiguilles`, `cadran-sterile-vert-lumineux-28-5`, `cadran-sterile-saumon-29-aiguilles`, `cadran-pilote-sterile-28-5-sans-logo` |
| **ARCHIVER** | **3** | `cadran-sterile-bleu-lumineux-28-5`, `cadran-plongee-33-5-aiguilles`, `cadran-retro-33-5-aiguilles-nh35` |
| **Total audité** | **13** | — |

`PRODUISIBLE` signifie uniquement qu'une source exacte, suffisamment nette et compatible avec la vérité des variantes vendables a été retrouvée. Ce verdict ne crée pas d'ordre et ne vaut ni validation commerciale, ni autorisation de publication. `BLOQUÉ` signifie que la fiche peut être sauvée après correction précise de son sélecteur ou apport d'une source propre. `ARCHIVER` signifie que le brouillon actuel n'a pas de variante éligible sous sa promesse ou qu'il duplique une meilleure fiche.

Le critère appliqué à une fiche présentée comme **stérile** est celui de cette mission et de la règle permanente §9 : aucun logo, aucune marque, aucun mot/verbatim, aucune lettre ni aucun sigle imprimé sur le cadran physique. Les mentions fonctionnelles `AUTOMATIC`, `WATER RESISTANT`, `100m:330ft` et les lettres directionnelles `N/E/S/W` sont donc disqualifiantes ; une fonction d'index ou de boussole ne constitue pas une exception. Les filigranes de vendeur apposés sur la photo sont distingués d'un marquage physique ; ils bloquent toutefois la production lorsqu'ils masquent les détails essentiels du produit.

## État API officiel observé

Route utilisée : client local en lecture seule `codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, vers le VPS autorisé et la méthode AliExpress Open Platform `aliexpress.ds.product.get`. `health` était sain à `2026-08-09T22:50:16Z`; le jeton d'accès était annoncé valide jusqu'au `2026-09-01T18:29:47Z` et le jeton de rafraîchissement jusqu'au `2026-10-01T18:09:12Z`.

| Article | Statut | Variantes | En stock | Note · avis · ventes |
|---|---|---:|---:|---:|
| `1005008812013694` | `onSelling` | 9 | 9 | 4,9 · 27 · 67 |
| `1005004795495451` | `onSelling` | 153 | 153 | 4,8 · 63 · 154 |
| `1005005879175706` | `onSelling` | 18 | 18 | 4,8 · 97 · 252 |
| `1005009523161505` | `onSelling` | 7 | 7 | 4,9 · 51 · 114 |
| `1005010122462262` | `onSelling` | 10 | 10 | 4,9 · 29 · 110 |
| `1005006987515689` | `onSelling` | 15 | 10 | 4,7 · 40 · 95 |
| `1005010122830689` | `onSelling` | 10 | 10 | 4,9 · 80 · 138 |
| `1005010692631891` | `onSelling` | 1 | 1 | 4,8 · 4 · 12 |
| `1005008481615291` | `onSelling` | 10 | 10 | 4,7 · 6 · 16 |
| `1005009643278179` | `onSelling` | 6 | 6 | 5,0 · 7 · 37 |
| `1005008471050885` | `onSelling` | 10 | 10 | 5,0 · 14 · 33 |
| `1005008468061052` | `onSelling` | 10 | 9 | 4,9 · 17 · 59 |
| `1005009148482089` | `onSelling` | 10 | 10 | 5,0 · 2 · 10 |

Les comptes de ventes ci-dessus sont ceux de l'API au moment du contrôle ; ils remplacent les nombres plus anciens conservés dans les documents locaux.

## Décision produit par produit

### 1. `cadran-lapis-lazuli-28-5` — `1005008812013694` — **BLOQUÉ**

- Les 9 variantes sont vendables et déclarées `No logo` par le sélecteur.
- Contrôle image des 9 : 6 cadrans portent physiquement `AUTOMATIC` (`No minute mark`, `With minute mark`, `YM blue lume`, `YM green lume`, `blue lume`, `blue lume no line`). Trois seulement sont réellement sans mot : `blank date`, `blank no date`, `blank line`.
- La source locale principale montre elle aussi `AUTOMATIC`. Elle est exacte, mais ne peut pas prouver une promesse stérile pour tout le sélecteur.
- Déblocage : limiter la fiche aux trois variantes `blank ...`, les mapper explicitement et corriger le titre/la description avant tout ordre.
- Preuve API : [`No minute mark`, contaminée](https://ae01.alicdn.com/kf/Sc841fad698954947be286f81b25aad72O.jpg) ; [`blank date`, propre](https://ae01.alicdn.com/kf/Sb8ec9b72b8fa4a4298a502226d3861f1p.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-lapis-lazuli-28-5/face-fournisseur-1005008812013694.jpg`.

### 2. `cadran-sterile-28-5-aiguilles` — `1005004795495451` — **BLOQUÉ**

- Les 153 variantes sont vendables : 51 choix visuels × 3 compatibilités (`NH35/NH36`, `Miyota82/DG`, `ETA2824/2836/PT5000`).
- Les 51 choix comprennent 24 ensembles cadran+aiguilles `A1` à `A24`, 24 cadrans seuls `Dial A1` à `Dial A24`, et 3 variantes d'aiguilles seules.
- Les 48 images de cadran ont été contrôlées : pour les ensembles comme pour les cadrans seuls, toutes les références impaires `A1, A3, ... A23` portent `AUTOMATIC / WATER RESISTANT / 100m:330ft`; toutes les paires `A2, A4, ... A24` n'ont pas ce verbatim. Les 3 variantes d'aiguilles seules ne sont pas des cadrans.
- Le filigrane `Goutent Official Store` est photographique, mais les mots au centre des références impaires sont bien imprimés sur le produit.
- Déblocage : retirer les 12 familles impaires et les 3 choix d'aiguilles seules, ou reconstruire des fiches séparées, puis refaire le mapping exact des 3 compatibilités.
- Preuve API : [`Dial A1`, contaminée](https://ae01.alicdn.com/kf/S3abe7896233b428caabe714d5c427504y.jpg) ; [`Dial A2`, physiquement propre](https://ae01.alicdn.com/kf/Sd2bb9ce9579e4a7a9518a3f50b20741ev.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-sterile-28-5-aiguilles/face-fournisseur-1005004795495451.jpg`.

### 3. `cadran-sterile-bleu-lumineux-28-5` — `1005005879175706` — **ARCHIVER**

- Les 18 variantes sont vendables : 9 finitions × 2 compatibilités (`NH35` et `Miyota/ETA/DG`).
- Les 9 finitions ont été contrôlées ; toutes portent physiquement `AUTOMATIC / WATER RESISTANT / 100m:330ft`.
- Il n'existe donc aucune variante conforme à la promesse stérile dans cet article. Le filigrane `NEITON` visible sur certaines photos ne change pas ce constat.
- Archiver le brouillon actuel. Une éventuelle réouverture exigerait une nouvelle identité non stérile et un arbitrage catalogue, pas seulement une autre image.
- Preuve API représentative : [variante `1`](https://ae01.alicdn.com/kf/Sd12b659f57ff42cf96a1f5b17adfad08N.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-sterile-bleu-lumineux-28-5/face-fournisseur-1005005879175706.jpg`.

### 4. `cadran-sterile-vert-lumineux-28-5` — `1005009523161505` — **BLOQUÉ**

- Les 7 variantes sont vendables : `Black gold indexes`, `Black silver indexes`, `Blue`, `Green gold indexes`, `Green silver indexes`, `White gold indexes`, `White silver indexes`.
- Les 7 cadrans portent physiquement les lettres `N/E/S/W`. La règle permanente §9 interdit explicitement toute lettre ou tout sigle sur un cadran ; leur fonction directionnelle n'est pas une exception.
- Les images API sont exactes et nettes, mais elles prouvent donc un défaut du produit lui-même, pas seulement de la photo. Déblocage : retrouver une variante ou un autre article de même vérité produit sans `N/E/S/W`, puis refaire le contrôle. Attention : le nom actuel « vert » ne décrit pas non plus l'intégralité du sélecteur blanc/noir/bleu/vert.
- Preuve API : [`Green silver indexes`](https://ae01.alicdn.com/kf/Sd733137ded454bce891bbb6d05c4bd616.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-sterile-vert-lumineux-28-5/face-fournisseur-1005009523161505.jpg`.

### 5. `cadran-sterile-saumon-29-aiguilles` — `1005010122462262` — **BLOQUÉ**

- Les 10 variantes sont vendables : 8 choix de cadran seul ou avec aiguilles et 2 jeux d'aiguilles seuls.
- Les deux variantes qui font précisément la promesse du titre, `Only Salmon Dial` et `Salmon Dial Hand`, portent physiquement `AUTOMATIC`.
- Les variantes noir, blanc et `B` sont sans mot ; les 2 variantes `Only Beige Hand` et `Only White Hand` ne sont pas des cadrans.
- Déblocage : retirer les variantes saumon et les aiguilles seules puis renommer la fiche selon les couleurs restantes, ou abandonner ce brouillon si la teinte saumon est indispensable.
- Preuve API : [`Only Salmon Dial`, contaminée](https://ae01.alicdn.com/kf/Sae5718a23b054aaeb18486e061de2f04E.jpg) ; [`Only Black dial`, propre](https://ae01.alicdn.com/kf/Sae10b786ca6146739f567122a0cb14a0A.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-sterile-saumon-29-aiguilles/face-fournisseur-1005010122462262.jpg`.

### 6. `cadran-argente-sterile-29` — `1005006987515689` — **PRODUISIBLE**

- Matrice vérifiée : 5 finitions `A` à `E` × 3 mouvements (`ETA2824`, `Miyota 8215`, `NH35`) = 15 combinaisons.
- 10 combinaisons sont vendables. Cinq sont à stock nul : `B/NH35`, `C/NH35`, `C/Miyota 8215`, `D/NH35`, `E/NH35`.
- Les cinq cadrans physiques sont sans marque, logo ni mot. Le grand `Neiton Official Store` sur la planche locale est un filigrane de photo, pas un marquage du produit ; les images API individuelles fournissent une preuve exacte et nette.
- Ne pas présenter les cinq combinaisons à stock nul comme disponibles dans les visuels ou le texte.
- Preuve API : [finition `A`](https://ae01.alicdn.com/kf/Sb9c9904f2a854e70adaf4825c8c625f0z.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-argente-sterile-29/face-fournisseur-1005006987515689.jpg`.

### 7. `cadran-texture-paon-29-sans-logo` — `1005010122830689` — **PRODUISIBLE**

- Les 10 variantes sont vendables : 8 choix cadran seul/cadran+aiguilles répartis sur quatre finitions, plus 2 jeux d'aiguilles seuls.
- Les cadrans `B`, noir, blanc et `Peacock blue`, avec ou sans aiguilles, sont tous sans marque, logo ni mot. Les deux variantes d'aiguilles seules sont distinctes et ne doivent pas servir à prouver un cadran.
- La vérité visuelle est une surface granuleuse bleu paon ; la source ne montre pas un motif de plume. La formulation future doit rester fidèle à cette texture.
- Preuve API : [`Only Peacock blue`](https://ae01.alicdn.com/kf/Sa38f6a19849e4324b552ce1c4fc4fe4cj.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-texture-paon-29-sans-logo/face-fournisseur-1005010122830689.jpg`.

### 8. `cadran-ciel-etoile-28-5` — `1005010692631891` — **PRODUISIBLE**

- Une variante unique est vendable : `Dial` + `NO LOGO`.
- Le cadran bleu pailleté est net, exact et sans mot/logo physique ; seuls les nombres de la minuterie sont présents.
- La faible profondeur de gamme et les 12 ventes observées restent une réserve commerciale distincte du verdict visuel.
- Preuve API : [variante unique](https://ae01.alicdn.com/kf/S8514efafb919403097a66d56ecae293dX.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-ciel-etoile-28-5/face-fournisseur-1005010692631891.jpg`.

### 9. `cadran-plongee-33-5-aiguilles` — `1005008481615291` — **ARCHIVER**

- Les 10 variantes sont vendables : cinq choix visuels (`brown`, `brown set`, `hand only`, `white`, `white set`) × deux compatibilités (`ETA2824/PT5000`, `NH35/NH36`).
- Les cinq médias API sont octet pour octet identiques à ceux de `1005008468061052` après correspondance sémantique des libellés. Ce n'est donc pas un cadran de plongée différent : `brown` est le même cadran rose/cuivré que `Pink Dial`.
- Cette fiche ajoute une contradiction de collection/titre et n'apporte aucune variante visuelle nouvelle. Archiver au profit de `cadran-retro-blanc-rose-nh35`.
- Preuve API : [`brown`](https://ae01.alicdn.com/kf/Sc49c24d091b94c0b93f138e87a0165e82.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-plongee-33-5-aiguilles/face-fournisseur-1005008481615291.jpg`.

### 10. `cadran-pilote-sterile-28-5-sans-logo` — `1005009643278179` — **BLOQUÉ**

- Les 6 variantes `A1` à `A6` sont vendables et leur seconde propriété indique `SANS LOGO`.
- Les cadrans physiques paraissent sans marque ni mot, mais les 6 images API et la planche locale portent un grand filigrane `alpha dial` directement au travers du centre du produit.
- Le filigrane masque les détails de la minuterie, des chiffres et/ou de la texture sur chaque variante. Il n'existe pas, dans les sources conservées ou renvoyées par l'API, de photo exacte suffisamment propre pour guider une production fidèle.
- Déblocage : obtenir du fournisseur une photo propre de chacune des six variantes exactes, ou une autre source traçable du même article. Ne pas substituer un cadran pilote proche.
- Preuve API représentative : [variante `A1`](https://ae01.alicdn.com/kf/S89b4872160fd443988a7f22866bd0cc0H.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-pilote-sterile-28-5-sans-logo/face-fournisseur-1005009643278179.jpg`.

### 11. `cadran-retro-33-5-aiguilles-nh35` — `1005008471050885` — **ARCHIVER**

- Les 10 variantes sont vendables : cinq choix visuels (`hands`, `pink dial`, `pink set`, `white dial`, `white set`) × les deux mêmes compatibilités que les deux autres fiches rétro.
- Les images montrent le même produit et les mêmes compositions que `1005008468061052`, mais avec les filigranes supplémentaires `Tandorio` et `watchery Store`.
- La similarité structurelle SSIM des cinq paires correspondantes varie de `0,952504` à `0,976495`, malgré les filigranes et la recompression. Aucune différence de cadran, d'aiguilles ou de matrice de compatibilité n'est prouvée.
- Source moins propre et fiche redondante : archiver au profit de `cadran-retro-blanc-rose-nh35`.
- Preuve API : [`pink dial`](https://ae01.alicdn.com/kf/Sec464b7a93be49a9b5a5bfb6c40e011en.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-retro-33-5-aiguilles-nh35/face-fournisseur-1005008471050885.jpg`.

### 12. `cadran-retro-blanc-rose-nh35` — `1005008468061052` — **PRODUISIBLE**

- Dix variantes : cinq choix visuels (`Blue Hands`, `Pink Dial`, `Pink Dial Set`, `White Dial`, `White Dial Set`) × deux compatibilités (`ETA2824/PT5000`, `NH35/NH36`). Neuf sont vendables ; `Pink Dial | For NH35 NH36 NH38` est à stock nul.
- Les cadrans blanc et rose/cuivré sont sans marque, logo ni mot. Les sources de cette fiche sont les plus propres du trio redondant et l'intitulé est cohérent avec les couleurs observées.
- Conserver cette fiche comme source canonique du trio ; ne pas représenter la combinaison rose/NH35 à stock nul comme disponible.
- Preuve API : [`Pink Dial`](https://ae01.alicdn.com/kf/Sde5af328d9414c69a5dc815024244a28N.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-retro-blanc-rose-nh35/face-fournisseur-1005008468061052.png`.

### 13. `cadran-sterile-date-aiguilles-29` — `1005009148482089` — **PRODUISIBLE**

- Les 10 variantes sont vendables : 8 choix cadran seul/cadran+aiguilles (deux noirs, un bleu, un blanc) et 2 jeux d'aiguilles seuls.
- Les 8 cadrans ont été contrôlés à leur résolution originale : aucun mot, logo ou marque n'est imprimé sur le produit. Le filigrane `Tandorio` est photographique, cantonné au coin supérieur gauche ; il touche le bord périphérique sur certaines vues mais ne masque ni le centre, ni la date, ni la géométrie principale.
- Les images sont nettes et exactes. Les deux variantes `hands A` et `hands B` doivent rester identifiées comme aiguilles seules et ne pas servir à décrire un cadran.
- Preuve API : [`blue dial`](https://ae01.alicdn.com/kf/S8c1b914876f5454e8388ca64ea4584e9X.jpg).
- Preuve locale : `boutique-seiko-mod/sources-fournisseur-2026-08/cadran-sterile-date-aiguilles-29/face-fournisseur-1005009148482089.jpg`.

## Preuve d'identité du trio rétro/plongée

### Identité exacte entre `1005008481615291` et `1005008468061052`

Les URL CDN sont différentes, mais les fichiers renvoyés par l'API officielle ont les mêmes octets après téléchargement. Les cinq correspondances couvrent l'intégralité du choix visuel ; chaque image est ensuite répétée par la seconde propriété de compatibilité.

| `1005008481615291` | `1005008468061052` | SHA-256 commun |
|---|---|---|
| `brown` | `Pink Dial` | `4c9e758addc9829ca14df179fb663a3bfccad24b8a10334da50b77296797b8da` |
| `brown set` | `Pink Dial Set` | `8bfb309cf6f838c305db2f38bf04838f06e8c05701d2448ee4c99e27affcd129` |
| `hand only` | `Blue Hands` | `c1dc4fbaee4fe0a24aad71cdfb6802fab06803a1ee928c85f956aa73e4d0a057` |
| `white` | `White Dial` | `fbc6f033935c2a093ad6dcff748148ced5285b9e5770227c4db4df5280b67f6f` |
| `white set` | `White Dial Set` | `2be02af29ee48cbed40b8e1463745bac55b55e84bc3a3eaece195468b8c53fa9` |

Conclusion : l'identité n'est pas une simple ressemblance visuelle ; les cinq médias source sont strictement identiques. Les seules différences observées sont le libellé trompeur `brown/plongée`, l'identifiant de listing, les compteurs commerciaux et le stock.

### Même produit recompressé et filigrané sur `1005008471050885`

Comparé à `1005008468061052`, le troisième listing reprend les mêmes compositions et objets, avec les filigranes `Tandorio`/`watchery Store`. Mesures SSIM sur les cinq paires :

| Paire | SSIM global |
|---|---:|
| `Pink Dial` / `pink dial` | 0,952504 |
| `Pink Dial Set` / `pink set` | 0,958930 |
| `Blue Hands` / `hands` | 0,976495 |
| `White Dial` / `white dial` | 0,956101 |
| `White Dial Set` / `white set` | 0,960619 |

La différence prouvée est donc une différence de filigrane/recompression et de listing, pas une différence de produit. Le choix canonique est `1005008468061052` : intitulé fidèle, sources les plus propres et 59 ventes observées, contre 33 et 16 pour les deux doublons.

## Preuves locales et intégrité des fichiers

Les 13 sources locales ont été ouvertes au niveau de détail original. Elles existent toutes sous `boutique-seiko-mod/sources-fournisseur-2026-08/<handle>/face-fournisseur-<item_id>.*`. Malgré leurs extensions `.jpg` ou `.png`, les 13 fichiers sont en réalité des conteneurs **WebP/RIFF** ; un futur exécuteur doit les décoder d'après leur contenu et non leur suffixe.

| Handle | Résolution locale lorsqu'exposée par le conteneur | SHA-256 |
|---|---:|---|
| `cadran-lapis-lazuli-28-5` | WebP, dimensions non exposées par `file` | `ba713e3d989472e312565a7d240666bd18573cb099151ace3ac42805cc73db21` |
| `cadran-sterile-28-5-aiguilles` | 1024 × 1024 | `53c375f291530e1e41f854f059a4dd01379d0d3454b6c8395d839ac44c0fc9d2` |
| `cadran-sterile-bleu-lumineux-28-5` | 1200 × 1200 | `179970c0aa21dc07ede97704198b5db6a40de72ac0b8f1e5dea428ae3758c047` |
| `cadran-sterile-vert-lumineux-28-5` | 1200 × 1200 | `7aec017534e773aa14fd2c1cc2d29fb299f2128fd9f5803a7505554ed13a69cb` |
| `cadran-sterile-saumon-29-aiguilles` | 1000 × 1000 | `c974b397044a821a236fe116160461ad41158f024925990cec31813a46118fa2` |
| `cadran-argente-sterile-29` | 1000 × 1000 | `9fca943efa317592a228c00bf84d60ce003c2757791ddd6840de008ecfe99230` |
| `cadran-texture-paon-29-sans-logo` | 1000 × 1000 | `022cdaf292b31bbae37de9d4dee7c4e559d383549dc97e05698d0d1e77d5073d` |
| `cadran-ciel-etoile-28-5` | 800 × 800 | `b344d6d3720488b3a51694ac6fe455faf1c0484596b8eef2858d069b2a6b3fae` |
| `cadran-plongee-33-5-aiguilles` | 1000 × 1000 | `544e02d068d9c811f1d385941473bd97f365634d44237d1e21fdf76d7d02ba81` |
| `cadran-pilote-sterile-28-5-sans-logo` | 1000 × 1000 | `11cabf25eee925ed08a2e0429fafe4790b63cf86c5cef1a6b37e42cdc6b9cc04` |
| `cadran-retro-33-5-aiguilles-nh35` | 1000 × 1000 | `852002381b73a09993c154eccd2038334d75d516467a3a55b9cefbe9d4464cd2` |
| `cadran-retro-blanc-rose-nh35` | 1000 × 1000 | `6bab0ae2439323ab97d053d51195f852fe4288fb32ebc311c485b6d0ba55ed1d` |
| `cadran-sterile-date-aiguilles-29` | 1000 × 1000 | `a602d562964b8def14b57048cc7137282e6cf9222941ec079cb153039e1150af` |

## Suite sûre

1. Aucun ordre ne doit être créé pour les 5 **BLOQUÉS** avant correction documentée de leur sélecteur, ajout des photos propres exigées ou remplacement par un produit conforme ; pour le cadran vert, une nouvelle photo ne peut pas effacer les lettres physiques `N/E/S/W`.
2. Les 3 **ARCHIVER** doivent être exclus de la file : un lot entièrement non stérile et deux doublons prouvés.
3. Les 5 **PRODUISIBLE** peuvent entrer dans un futur lot uniquement avec un manifeste qui fixe les variantes éligibles, les cinq combinaisons hors stock du cadran argenté, la combinaison rose/NH35 hors stock, et les options « aiguilles seules » distinctes.
4. Le statut local des brouillons, leur rédaction et leur présence éventuelle dans Shopify/DSers n'ont pas été modifiés ni validés par cette mission.

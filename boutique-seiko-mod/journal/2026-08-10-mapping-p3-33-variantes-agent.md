---
type: journal
boutique: seiko-mod
date: 2026-08-10
nature: intervention
leviers: [catalogue]
titre: "Mapping P3 — 33 médias de variantes de montres actives — 10/08/2026"
---

# Mapping P3 — 33 médias de variantes de montres actives — 10/08/2026

Sous-tâche de reconstruction en lecture seule. Les données fournisseur ci-dessous proviennent
exclusivement de l'API officielle AliExpress, via le gateway VPS documenté ; aucun navigateur
AliExpress n'a été utilisé. Aucun accès ni aucune écriture Shopify/DSers, aucune génération et
aucune création/modification d'ordre n'ont été effectués.

## Verdict

Le dénominateur P3 actif est bien **33 médias**, et non 43 :

| Produit actif | Valeurs visuelles | Valeur actuellement couverte | Médias manquants | Verdict |
|---|---:|---:|---:|---|
| Explorateur | 13 | 1 | **12** | 6 PRODUISIBLES, 6 BLOQUÉS (texte sur cadran) |
| Éclaireur Acier | 11 | 1 | **10** | 10 PRODUISIBLES sous contrainte de recadrage/composition |
| Éclaireur Bronze | 9 | 1 | **8** | 8 PRODUISIBLES |
| Squelette Carré | 2 | 1 | **1** | PRODUISIBLE |
| Squelette Octogone | 2 | 1 | **1** | PRODUISIBLE |
| Trente-Neuf Duo | 2 | 1 | **1** | **BLOQUÉ** |
| **Total** | **39** | **6** | **33** | **26 PRODUISIBLES, 7 BLOQUÉS** |

Les 26 lignes produisibles couvrent **127 variantes Shopify enfant** : 48 Explorateur,
60 Éclaireur Acier, 16 Éclaireur Bronze, 1 Carré et 2 Octogone. Il s'agit de **26 fichiers**, pas
de 127 fichiers : un même média de cadran/boîtier doit être associé à toutes les variantes enfant
qui partagent cette valeur visuelle. C'est l'application directe de la règle du brief et de la règle
storefront selon laquelle le média sélectionné doit suivre l'option qui change réellement l'apparence.

Les 7 blocages sont : 6 Explorateur dont le cadran physique porte un bloc de texte, plus le
Trente-Neuf Duo dont la dimension cible 36/39 mm n'est pas attribuable et dont le cadran porte lui
aussi des mots. Ils ne doivent pas être produits par gommage ni par déduction.

## 1. Sources et méthode de contrôle

Sources locales faisant foi :

- `2026-08-08-brief-visuels-codex.md` et `2026-08-08-consignes-codex-visuels.md` pour le comptage par
  valeur d'option visuelle et les règles de production ;
- `INVENTAIRE-VISUEL-2026-08-08.csv` pour les 6 produits actifs et leur couverture 1/N ;
- `boutique-seiko-mod/backups/backup-sku-2026-08-08/table-correspondance.jsonl` pour les handles, titres Shopify, variantes enfant
  et SKU fournisseur enregistrés ;
- `2026-07-31-sourcing-arabes-squelettes.md` et `2026-07-25-dsers-mapping-decoupage.md` pour les IDs produits
  AliExpress d'origine.

Contrôle live de l'API officielle :

- gateway `aliexpress_vps_gateway.py`, opération read-only `health` : **OK** le
  `2026-08-09T22:40:32+00:00` ;
- opération `variants` exécutée sur les 6 produits ci-dessous ;
- les **200/200 lignes enfant Shopify** de ces 6 produits ont trouvé une correspondance SKU exacte
  dans la réponse API, après comparaison des segments `;` indépendamment de leur ordre ;
- ces 200 lignes se regroupent en **39 valeurs visuelles distinctes**.

Produits AliExpress contrôlés :

| Produit Shopify | Handle | Item AliExpress | Fiche source |
|---|---|---:|---|
| Explorateur — Sport chic à chiffres 3-6-9 | `montre-acier-chiffres-3-6-9-explorateur` | `1005010759311949` | https://fr.aliexpress.com/item/1005010759311949.html |
| Éclaireur Acier — Field à chiffres 1-12 | `montre-field-acier-cadran-chiffres-1-12` | `1005010311217067` | https://fr.aliexpress.com/item/1005010311217067.html |
| Éclaireur Bronze — Field militaire à chiffres 1-12 | `montre-field-bronze-cadran-chiffres-1-12` | `1005009879577159` | https://fr.aliexpress.com/item/1005009879577159.html |
| Squelette Carré | `montre-squelette-automatique-carree` | `1005009825936780` | https://fr.aliexpress.com/item/1005009825936780.html |
| Squelette Octogone | `montre-squelette-automatique-octogone` | `1005009354912699` | https://fr.aliexpress.com/item/1005009354912699.html |
| Trente-Neuf Duo — Classique bicolore | `trente-neuf-duo-classique-bicolore` | `1005006277907428` | https://fr.aliexpress.com/item/1005006277907428.html |

Les miniatures de propriétés renvoyées par l'API ont été téléchargées temporairement et examinées à
la résolution originale. Seules les **16 sources exactes conformes à l'interdit strict de tout
mot/lettre sur cadran** ont été conservées sous
`boutique-seiko-mod/preuves/preuves-p3-variantes-api-2026-08-10-agent/sources-propres/`. Les 6 sources Explorateur bloquées ont
été isolées sous `sources-bloquees-texte-cadran/` comme preuves de refus. Les 10 sources Éclaireur Acier, dont le
cadran est stérile mais dont la marge porte un watermark fournisseur Tandorio, restent volontairement
URL-only. Les deux candidates du Duo, fortement filigranées `BL Watches Parts Store`, ne sont pas
conservées comme sources propres.

## 2. Construction des SKU exacts

Dans les tables suivantes, la colonne **fragment exact** est le segment `14:` qui désigne l'apparence.
Ce n'est pas une approximation : il devient le SKU fournisseur complet en lui ajoutant le ou les
segments de la famille ci-dessous. Chaque combinaison obtenue a été trouvée telle quelle dans la
sauvegarde Shopify et dans l'API officielle.

| Famille | Segments enfant exacts à combiner au fragment visuel | Nombre par média |
|---|---|---:|
| Explorateur | `200007763:201336100` puis `5:57000035#8215-36mm -glassback`, `5:56964930#8215-36mm-solidback`, `5:57086108#8215-39mm-glassback`, `5:57085267#8215-39mm-solidback`, `5:57036539#NH35-36mm -glassback`, `5:57037163#NH35-36mm-solidback`, `5:646979416#NH35-39mm-glassback`, `5:2399342480#NH35-39mm-solidback` | 8 |
| Éclaireur Acier | `5:57000035#Miyota82-steel back`, `5:57037163#Miyota82-glass back`, `5:56964930#NH35-steel back`, `5:57036539#NH35-glass back`, `5:57086108#PT5000-steel back`, `5:646979416#PT5000-glass back` | 6 |
| Éclaireur Bronze | `5:5203931210#Solid caseback`, `5:5203931209#Glass caseback` | 2 |
| Squelette Carré | `5:56964930#NH70 movement` | 1 |
| Squelette Octogone | `5:57000035#Glass Back`, `5:56964930#Steel Back` | 2 |
| Trente-Neuf Duo | `5:57000035#Miyota8215`, `5:2399342480#NH35`, `5:56964930#Mingzhu 2813` | 3 par dimension |

## 3. Mapping exact des 33 médias

### 3.1 Explorateur — 12 médias / 96 variantes Shopify enfant

Handle commun : `montre-acier-chiffres-3-6-9-explorateur`. Source produit : `1005010759311949`.
La variante déjà couverte est **Noir** / `14:200005100#Black` : elle correspond à la face maison
noire portant la mention `200m Professional Automatic`. Elle est donc exclue du dénominateur des 12
médias manquants, mais **elle n'est pas validée comme source conforme** à la règle stricte §9 ; son
éventuel nettoyage relève d'un audit séparé de l'existant.

| ID | Variante Shopify visuelle | Fragment AliExpress exact | Source image API / preuve locale | Contrôle visuel | Verdict |
|---|---|---|---|---|---|
| E01 | Vert (réf. 1), 8 enfants | `14:10#Green1` | https://ae01.alicdn.com/kf/S67b4201c7af74d94a38578b01ca9790fP.jpg · `sources-propres/explorateur-01-14-10-green1.jpg` | Aucun mot/lettre/logo sur cadran | **PRODUISIBLE** |
| E02 | Bleu (réf. 1), 8 enfants | `14:100005979#Blue1` | https://ae01.alicdn.com/kf/Sbdba066bd17e4703a0184bfb87077011H.jpg · `sources-propres/explorateur-02-14-100005979-blue1.jpg` | Aucun mot/lettre/logo sur cadran | **PRODUISIBLE** |
| E03 | Bleu, 8 enfants | `14:100013777#Blue` | https://ae01.alicdn.com/kf/S069a35eeb1cd4dbbb138a8a25698bbc7p.jpg · `sources-bloquees-texte-cadran/explorateur-03-14-100013777-blue.jpg` | Bloc de 3 lignes sur le cadran physique | **BLOQUÉ** |
| E04 | Orange, 8 enfants | `14:173#Orange` | https://ae01.alicdn.com/kf/S10fb523647824748b44da4c0cb3936d1O.jpg · `sources-bloquees-texte-cadran/explorateur-04-14-173-orange.jpg` | Bloc de 3 lignes sur le cadran physique | **BLOQUÉ** |
| E05 | Orange (réf. 1), 8 enfants | `14:175#Orange1` | https://ae01.alicdn.com/kf/Sbf606d7b6ee44952a351fb9fca420ef9U.jpg · `sources-propres/explorateur-05-14-175-orange1.jpg` | Aucun mot/lettre/logo sur cadran | **PRODUISIBLE** |
| E06 | Rouge, 8 enfants | `14:193#Red` | https://ae01.alicdn.com/kf/S49ea5e37d67d47bb82d7fadab2abfad53.jpg · `sources-bloquees-texte-cadran/explorateur-06-14-193-red.jpg` | Bloc de 3 lignes sur le cadran physique | **BLOQUÉ** |
| E07 | Noir (réf. 1), 8 enfants | `14:200000080#Black1` | https://ae01.alicdn.com/kf/S65f8c5bac1244df98a61028bc184ad00g.jpg · `sources-propres/explorateur-07-14-200000080-black1.jpg` | Aucun mot/lettre/logo sur cadran | **PRODUISIBLE** |
| E08 | Argenté · index dorés, 8 enfants | `14:29#White` | https://ae01.alicdn.com/kf/S5222adbfc23d41bdadc907dd4fb24bb26.jpg · `sources-bloquees-texte-cadran/explorateur-09-14-29-white.jpg` | Bloc de 3 lignes sur le cadran physique | **BLOQUÉ** |
| E09 | Vert, 8 enfants | `14:350686#Green` | https://ae01.alicdn.com/kf/S903ff44dcee64b82ad1e779492d8b1b78.jpg · `sources-bloquees-texte-cadran/explorateur-10-14-350686-green.jpg` | Bloc de 3 lignes sur le cadran physique | **BLOQUÉ** |
| E10 | Rose, 8 enfants | `14:350850#pink` | https://ae01.alicdn.com/kf/Sdf81465af49242279f01283c343dc04e3.jpg · `sources-bloquees-texte-cadran/explorateur-11-14-350850-pink.jpg` | `200m / PROFESSIONAL / AUTOMATIC` sur le cadran | **BLOQUÉ** |
| E11 | Rouge (réf. 1), 8 enfants | `14:366#Red1` | https://ae01.alicdn.com/kf/S5c15e161177e47fea21c549c07a4d01fv.jpg · `sources-propres/explorateur-12-14-366-red1.jpg` | Aucun mot/lettre/logo sur cadran | **PRODUISIBLE** |
| E12 | Argenté · index dorés (réf. 1), 8 enfants | `14:94#White1` | https://ae01.alicdn.com/kf/Se5328f6e615c4125bfc88257659882d1q.jpg · `sources-propres/explorateur-13-14-94-white1.jpg` | Aucun mot/lettre/logo sur cadran | **PRODUISIBLE** |

Planche de contrôle des 12 candidates :
`boutique-seiko-mod/preuves/preuves-p3-variantes-api-2026-08-10-agent/QA-explorateur-audit-complet.jpg`. Les six refus y restent
visibles ; la planche n'est pas une planche de sources toutes conformes.

Pour E03, E04, E06, E08, E09 et E10, l'opération API `variants` ne fournit qu'une seule image de
propriété pour le fragment exact, celle consignée dans la table. La recherche locale par fragment SKU
et par hash d'image n'a retrouvé aucune autre photo exacte du même SKU sans ce texte. Leur blocage est
donc maintenu, sans extrapolation depuis le coloris voisin suffixé `1`.

### 3.2 Éclaireur Acier — 10 médias / 60 variantes Shopify enfant

Handle commun : `montre-field-acier-cadran-chiffres-1-12`. Source produit : `1005010311217067`.
La valeur déjà couverte est **Noir · trotteuse rouge** / `14:200000080#black 1-sterile` ; elle est
exclue des 10 lignes.

| ID | Variante Shopify visuelle | Fragment AliExpress exact | Source image API | Contrôle visuel | Verdict |
|---|---|---|---|---|---|
| A01 | Noir · grands chiffres lumineux, 6 enfants | `14:4#black 8-sterile` | https://ae01.alicdn.com/kf/S6547c64747b3487f8760d862d7682c3eU.jpg | Aucun mot/lettre/logo sur cadran ; watermark Tandorio hors produit | **PRODUISIBLE sous contrainte** |
| A02 | Noir · index jaunes, 6 enfants | `14:366#black 3-sterile` | https://ae01.alicdn.com/kf/S5a776b23fc594f6d8809b07afc64b54bo.jpg | Aucun mot/lettre/logo sur cadran ; watermark Tandorio hors produit | **PRODUISIBLE sous contrainte** |
| A03 | Noir · index crème, 6 enfants | `14:865#black 4-sterile` | https://ae01.alicdn.com/kf/S336455785f0047f4b6caa3c317516e66b.jpg | Aucun mot/lettre/logo sur cadran ; watermark Tandorio hors produit | **PRODUISIBLE sous contrainte** |
| A04 | Noir · grands chiffres cuivrés, 6 enfants | `14:201447598#black 7-sterile` | https://ae01.alicdn.com/kf/S903b15627096405d8f90e966a8683423j.jpg | Aucun mot/lettre/logo sur cadran ; watermark Tandorio hors produit | **PRODUISIBLE sous contrainte** |
| A05 | Noir · index blancs, 6 enfants | `14:200000914#black 5-sterile` | https://ae01.alicdn.com/kf/S97fa65745e3c4864a4ec5058fa1ccb36A.jpg | Aucun mot/lettre/logo sur cadran ; watermark Tandorio hors produit | **PRODUISIBLE sous contrainte** |
| A06 | Kaki, 6 enfants | `14:94#green-sterile` | https://ae01.alicdn.com/kf/S032af97f477f43639320165afacd44dfs.jpg | Aucun mot/lettre/logo sur cadran ; watermark Tandorio hors produit | **PRODUISIBLE sous contrainte** |
| A07 | Noir · grandes minutes, 6 enfants | `14:175#black 6-sterile` | https://ae01.alicdn.com/kf/S68c003c091704f7e946a559a608248c4q.jpg | Aucun mot/lettre/logo sur cadran ; watermark Tandorio hors produit | **PRODUISIBLE sous contrainte** |
| A08 | Noir · chiffres jaunes, 6 enfants | `14:100005979#black 2-sterile` | https://ae01.alicdn.com/kf/Sf486b7ca1a7e428a8181fdbb3cd686c4T.jpg | Aucun mot/lettre/logo sur cadran ; watermark Tandorio hors produit | **PRODUISIBLE sous contrainte** |
| A09 | Argenté, 6 enfants | `14:350850#silver-sterile` | https://ae01.alicdn.com/kf/Sed416220fb4d41feaf9bc7bae73955b3r.jpg | Aucun mot/lettre/logo sur cadran ; watermark Tandorio hors produit | **PRODUISIBLE sous contrainte** |
| A10 | Bleu, 6 enfants | `14:10#blue-sterile` | https://ae01.alicdn.com/kf/S06686c77a51640e585b6e2d950e68565Y.jpg | Aucun mot/lettre/logo sur cadran ; watermark Tandorio hors produit | **PRODUISIBLE sous contrainte** |

`PRODUISIBLE sous contrainte` signifie : l'apparence exacte et l'absence de marque sur le cadran sont
prouvées, mais la miniature brute ne doit être ni publiée ni utilisée comme calque pleine image. La
composition maison doit reprendre uniquement le produit/cadran réel et éliminer totalement la marge
portant `Tandorio`. Ces dix images n'ont donc pas été versées au dossier `sources-propres`.

### 3.3 Éclaireur Bronze — 8 médias / 16 variantes Shopify enfant

Handle commun : `montre-field-bronze-cadran-chiffres-1-12`. Source produit : `1005009879577159`.
La valeur déjà couverte est **Vert olive** / `14:10#green A-sterile` ; elle est exclue des 8 lignes.

| ID | Variante Shopify visuelle | Fragment AliExpress exact | Source image API / preuve locale | Contrôle visuel | Verdict |
|---|---|---|---|---|---|
| B01 | Bleu, 2 enfants | `14:350850#blue-sterile` | https://ae01.alicdn.com/kf/S70e66037b44542a8ab2f25bbbe97d8bb5.jpg · `sources-propres/field-bronze-13-14-350850-blue-sterile.jpg` | Produit et cadran sans marque/logo | **PRODUISIBLE** |
| B02 | Noir · chiffres blancs · date, 2 enfants | `14:4#black D-sterile` | https://ae01.alicdn.com/kf/Scf79e5a136d4489f943999105f35b161B.jpg · `sources-propres/field-bronze-15-14-4-black-d-sterile.jpg` | Produit et cadran sans marque/logo | **PRODUISIBLE** |
| B03 | Noir · chiffres blancs, 2 enfants | `14:175#black B-sterile` | https://ae01.alicdn.com/kf/S69a81fbb12d04242a6cbd3c99dc40bdcv.jpg · `sources-propres/field-bronze-05-14-175-black-b-sterile.jpg` | Produit et cadran sans marque/logo | **PRODUISIBLE** |
| B04 | Argenté, 2 enfants | `14:94#silver sterile` | https://ae01.alicdn.com/kf/S1f1cd542ce654112a237e09a1f1118afi.jpg · `sources-propres/field-bronze-18-14-94-silver-sterile.jpg` | Produit et cadran sans marque/logo | **PRODUISIBLE** |
| B05 | Noir · chiffres jaunes, 2 enfants | `14:200000080#black A-sterile` | https://ae01.alicdn.com/kf/Sdf7eac0d0f5d4e068c305ba2929ce41cX.jpg · `sources-propres/field-bronze-07-14-200000080-black-a-sterile.jpg` | Produit et cadran sans marque/logo | **PRODUISIBLE** |
| B06 | Vert sapin, 2 enfants | `14:200000914#green B sterile` | https://ae01.alicdn.com/kf/Seca440409f474cf79ad9fa9252914bb7X.jpg · `sources-propres/field-bronze-08-14-200000914-green-b-sterile.jpg` | Produit et cadran sans marque/logo | **PRODUISIBLE** |
| B07 | Noir · chiffres crème · date, 2 enfants | `14:201447303#black C-sterile` | https://ae01.alicdn.com/kf/S71b42ec4014e4c43a9137d894e609871d.jpg · `sources-propres/field-bronze-10-14-201447303-black-c-sterile.jpg` | Produit et cadran sans marque/logo | **PRODUISIBLE** |
| B08 | Blanc · chiffres rouges, 2 enfants | `14:496#white sterile` | https://ae01.alicdn.com/kf/S8cc32b24da0f4825b04353e2e676b209r.jpg · `sources-propres/field-bronze-16-14-496-white-sterile.jpg` | Produit et cadran sans marque/logo | **PRODUISIBLE** |

Planche de contrôle : `boutique-seiko-mod/preuves/preuves-p3-variantes-api-2026-08-10-agent/QA-field-bronze-sources-propres.jpg`.

### 3.4 Squelettes — 2 médias / 3 variantes Shopify enfant

Les variantes blanches sont les valeurs déjà couvertes ; seuls les deux cadrans noirs sont à produire.

| ID | Handle / variante Shopify | Fragment AliExpress exact | Source exacte | Contrôle visuel | Verdict |
|---|---|---|---|---|---|
| S01 | `montre-squelette-automatique-carree` — Squelette noir, 1 enfant | `14:200000080#Black` | item `1005009825936780` · https://ae01.alicdn.com/kf/Sc63c29a32a0c4c329d308188738f58efP.jpg · `sources-propres/squelette-carre-01-14-200000080-black.jpg` | Boîtier/cadran exacts, sans marque/logo | **PRODUISIBLE** |
| S02 | `montre-squelette-automatique-octogone` — Squelette noir, 2 enfants | `14:200000080#Black Skeleton` | item `1005009354912699` · https://ae01.alicdn.com/kf/S6329b301e2be4c959a8abfd5cac697f75.jpg · `sources-propres/squelette-octogone-01-14-200000080-black-skeleton.jpg` | Boîtier/cadran exacts, sans marque/logo | **PRODUISIBLE** |

Planche de contrôle : `boutique-seiko-mod/preuves/preuves-p3-variantes-api-2026-08-10-agent/QA-squelette-sources-propres.jpg`.

### 3.5 Trente-Neuf Duo — 1 média / dimension cible non démontrable

Handle : `trente-neuf-duo-classique-bicolore`. Source produit : `1005006277907428`.

| ID | Variante Shopify candidate | Fragment AliExpress exact | SKU IDs API exacts | Source exacte | Contrôle visuel | Verdict |
|---|---|---|---|---|---|---|
| T01-A | Or rose · 36 mm · fond acier, 3 mouvements | `14:201447303#Rose 36mm solid back` | `12000036579615931`, `12000036579615932`, `12000057156116756` | https://ae01.alicdn.com/kf/Se106aa243c6a49d986b8c41077029bddX.jpg | Texte `AUTOMATIC / WATER RESISTANT / 100m:330ft` sur cadran + watermark `BL Watches Parts Store` | **BLOQUÉ** |
| T01-B | Or rose · 39 mm · fond acier, 3 mouvements | `14:200005100#Rose 39mm steel back` | `12000049473822428`, `12000049473822429`, `12000057156116750` | https://ae01.alicdn.com/kf/S78587b5ef25d411387e06dee24eb80ddn.png | Texte `AUTOMATIC / WATER RESISTANT / 100m:330ft` sur cadran + watermark `BL Watches Parts Store` | **BLOQUÉ** |

Ces deux lignes représentent **les deux candidats du même média T01**, pas deux médias manquants.
L'inventaire prouve `Boîtier (2)` et couverture `1`, donc un seul manque. En revanche, le média maison
actuellement associé est une face champagne/or qui ne donne aucune preuve attribuable à la taille 36 ou
39 mm. L'API prouve l'apparence des deux SKU, mais pas lequel est déjà couvert dans Shopify. Même si la
dimension manquante était connue, ces deux sources resteraient incompatibles avec l'interdit §9 à cause
des mots imprimés sur le cadran ; les enlever modifierait le produit réel. Sans lecture Shopify autorisée
ou manifeste historique d'association, choisir T01-A ou T01-B serait en plus une invention.

Condition de déblocage minimale : obtenir une autre photo exacte du SKU manquant montrant un cadran
réellement sans mot/lettre, puis l'association actuelle `media → variantes` du produit ou une capture
montrant explicitement quelle dimension utilise déjà le média.

## 4. Nommage futur des 26 fichiers produisibles

Le protocole existant demande `<handle>-v-<code>.jpg`, où `<code>` vient de la valeur après `#` du
fragment `14:`. Les 26 mappings produisibles ci-dessus suffisent donc à construire des noms non ambigus,
par exemple :

- `montre-acier-chiffres-3-6-9-explorateur-v-black1.jpg` pour E07 ;
- `montre-field-acier-cadran-chiffres-1-12-v-black-8-sterile.jpg` pour A01 ;
- `montre-field-bronze-cadran-chiffres-1-12-v-blue-sterile.jpg` pour B01 ;
- `montre-squelette-automatique-octogone-v-black-skeleton.jpg` pour S02.

Le manifeste final devra conserver le fragment original complet et associer chaque fichier à toutes les
variantes enfant de sa famille. Les six Explorateur bloqués et le Duo ne doivent pas recevoir de fichier
par simple effacement du texte. Ce rapport ne crée aucun livrable final et n'autorise pas une publication
des miniatures AliExpress brutes.

## 5. Preuves locales livrées

Répertoire : `boutique-seiko-mod/preuves/preuves-p3-variantes-api-2026-08-10-agent/`

- **16** miniatures exactes conformes : 6 Explorateur, 8 Éclaireur Bronze, 1 Carré, 1 Octogone ;
- **6** miniatures Explorateur isolées comme preuves de refus pour texte sur cadran ;
- **3** planches QA pour une vérification d'ensemble ; la planche Explorateur contient conformes et refus ;
- **0** miniature brute Éclaireur Acier conservée comme « propre » ; les dix URLs exactes restent dans
  ce rapport à cause du watermark externe ;
- **0** miniature Duo conservée comme « propre » à cause du gros watermark et de l'ambiguïté 36/39.

La validation applique ici l'interdit §9 au sens strict : aucune marque, aucun logo, aucun nom, mot,
lettre, sigle ou mention d'origine sur le produit ou le cadran cible ; les chiffres constitutifs du cadran
restent permis. Un texte technique générique est donc bloquant au même titre qu'un verbatim commercial.
La validation ne transforme pas non plus une photo fournisseur en visuel publiable : toute production
doit rester une composition fidèle à partir du réel, avec nouveau fond/cadrage/rendu maison.

## 6. Limites et non-actions

- Aucun stock, prix ou statut commercial n'a été utilisé pour décider la produisibilité visuelle ; ce
  rapport est un mapping média, pas une requalification fournisseur.
- Les valeurs déjà couvertes sont identifiées par comparaison visuelle entre la face maison locale et les
  miniatures exactes API. Pour le Duo, cette comparaison ne permet précisément pas de choisir 36/39.
- Aucun fichier Shopify/DSers n'a été modifié ; aucun média n'a été attaché ; aucune commande ni ordre de
  génération n'a été créé ; aucun commit/push n'a été effectué.

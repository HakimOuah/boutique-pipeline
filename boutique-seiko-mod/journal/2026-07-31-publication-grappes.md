# Publication des grappes « cadran arabe » et « squelette » — Maison Noirmont

> **29/07/2026 (soir)** — boutique `v42pzp-h4` / maisonnoirmont.fr. Mission en quatre temps :
> contrôle DSers, publication des 7 fiches, 6ᵉ famille du configurateur, pages des deux grappes.
> **Aucun SKU, prix, variante, option ni mapping touché. Aucun slider/avis. Thème non publié.
> Aucune commande.** Sauvegardes : `scratchpad/backup-publication/`.

---

## 1. DSers — contrôle fait, propre

Session Chrome de Hakim, désormais sur le **bon compte** (`contact.noirmont`, boutique `v42pzp-h4`
liée) — aucun identifiant saisi, accès par l'app intégrée Shopify (admin → DSers, redirection
`auth_check` avec `contact.noirmont@gmail.com`).

| Compteur | Relevé |
|---|---|
| Mes Produits — Tous | **103** |
| AliExpress | **103** |
| 1688 Dropshipping / Alibaba / Non répertorié | 0 / 0 / 0 |
| **Unmapped** | **(0)** — zoomé et confirmé, onglet vide (« Importez votre premier article ») |

Après les 78 suppressions de variantes du 29/07, **aucune fiche n'est repassée Unmapped** ;
les 5 nouvelles fiches affichent leurs fourchettes de coût fournisseur (= mapping vivant).
Feu vert pour publier.

## 2. Publication — 7 fiches ACTIVE, 3 canaux chacune

`productUpdate status: ACTIVE` puis `publishablePublish` sur **Boutique en ligne `358599295314` ·
Point de vente `358599328082` · Shop `358599360850`** (piège DSers « publié sur aucun canal »
neutralisé). Vérifié après coup par `resourcePublicationsV2` : **3/3 `isPublished: true` sur les 7**.

| Fiche | ID | Collections vérifiées |
|---|---|---|
| Éclaireur Bronze — field 36 | `10988849267026` | `classiques` + `montres` (+ arabes, §4) |
| Éclaireur Acier — field 39 | `10988849234258` | `classiques` + `montres` (+ arabes) |
| Explorateur 3-6-9 | `10988849299794` | `sport-chic` + `montres` (+ arabes) — Sport chic est le choix documenté du sourcing §2, pas un écart |
| Squelette Octogone | `10988849365330` | `montre-squelette` + `montres` |
| Squelette Carré 42 | `10988849135954` | `montre-squelette` + `montres` |
| Aviateur acier (réécrit) | `10977448558930` `montre-aviateur-acier-cadran-chiffres-arabes` | `classiques` + `montres` (+ arabes) |
| Aviateur bronze (réécrit) | `10978722087250` `montre-aviateur-bronze-cadran-chiffres-arabes` | `classiques` + `montres` (+ arabes) |

**Restés en DRAFT, non touchés (re-vérifié)** : `noirmont-deux-plongeuse-ceramique`,
`aviateur-acier-cadran-chiffres-arabes` (la redondante — ⚠️ elle porte les **mêmes 6 SKU** que
l'aviateur acier désormais publié : ne jamais la publier telle quelle), les 4 mères
(`contre-la-montre-chronographe-panda`, `integrale-sport-chic-acier`,
`heritage-plongeuse-vintage-42`, `voyageur-gmt-automatique`) et 3 accessoires
(`remontoir-bois`, `remontoir-collection`, `rouleau-de-voyage-cuir`).

Note : l'aviateur bronze est publié à **stock 0** (`inventoryPolicy: CONTINUE`, vente en rupture
cochée côté DSers) — c'était déjà son état, rien n'a été modifié.

## 3. Configurateur — 6ᵉ famille branchée et contrôlée en clics réels

Patch 3 lignes appliqué sur **`204248088914` uniquement** (rôle UNPUBLISHED revérifié ;
Helio `204246548818` contrôlé par `files(filenames:…)` : **0 nœud**) :
`fam_handles` +`montre-squelette`, `fam_pieces` +`Squelette`, `fam_crops` +`50% 30%`.
Empreinte relue = md5 local : `6c647cbbe7af1eda59270ac291a9b130`, 23 922 octets
(avant : `8673b329…`, 23 887 — sauvegarde
`backup-publication/noirmont-configurateur.liquid.avant-squelette-2026-07-29`).
Source de vérité locale mise à jour : `scratchpad/work-configurateur/noirmont-configurateur.liquid`.

### Chemins — avant / après (mesuré sur le rendu du thème brouillon)

| | Avant (V3, 28-29/07) | Après |
|---|---:|---:|
| Chemins ouverts | 34 | **35** |
| Chemins morts | 0 | **0** |
| Par famille | Cl 9 · SC 7 · Ch 11 · Pl 3 · GMT 4 | **identiques + Squelette 1** |
| Montres atteignables | 50/50 | **57/57** (0 cachée) |

Le chemin Squelette unique est l'échappatoire « Peu importe » : les 2 squelettes n'ont pas de
`couleur_cadran` (décision documentée) — même logique pour les nouvelles fiches arabes,
atteignables via « Peu importe » et la rangée « Votre cadran, précisément ».

### Parcours rejoués par clics réels (session Chrome, aucun mot de passe saisi)

- **Squelette complet jusqu'à l'ajout panier réel** : Q1 carte « Squelette dès 399 € » (recadrage
  macro 50% 30% : minuterie + mouvement ouvragé, jamais une montre entière, aucun nom) → Q2
  « Peu importe » → « Voici votre Squelette Carré » (42 mm · NH70 · 399 €, variante réelle
  `54130353340754` dans le `/cart/add`) → bascule pastille **Octogone** (+30 €) : scène, nom, prix
  429 €, variante `54130362581330` (White Skeleton / Glass Back) → **ajout panier effectif**,
  ligne « Squelette Octogone — White Skeleton, Glass Back, 429 € barré 559 € » au panier.
  L'article de test a été retiré ensuite : le panier de Hakim est rendu tel que trouvé
  (1 article, Trente-Neuf Orange préexistant).
- **GMT inchangé** : Q2 = Peu importe + Noir + Blanc + Brun (1 rangée) ; GMT/Noir → « Voici votre
  Voyageur Bicolore », 378 €, rangée de 4 pastilles, variante réelle — identique au contrôle V3.
- **Classiques** : Q2 = Peu importe + 8 couleurs (9 chemins, inchangé) ; « Peu importe » →
  **« Voici votre Éclaireur Acier »**, et la rangée s'ouvre sur les 4 nouvelles arabes
  (Éclaireur Acier +0 · Éclaireur Bronze +39 · Noirmont Un Bronze +0 · Noirmont Un +29) devant
  les 15 anciennes. Sport chic porte l'Explorateur en tête de rangée.
- Balayage programmatique des 35 chemins sur le DOM rendu : **0 chemin mort, 0 montre cachée**.

## 4. Les deux pages de grappe — créées, publiées, au méga-menu

### Collection `montre-squelette` (existante, `691173917010`)
- **Description étoffée** dans la voix maison : ce qu'est un squelette (cadran ouvert, mouvement
  visible par l'avant — ≠ fond verre), l'arbitrage lisibilité assumé, le NH70 (déclinaison
  squelette du Seiko NH35, chaque calibre nommé séparément), les deux boîtiers. Saphir « annoncé ».
- **`seo.title` + `seo.description` posés ensemble** : « Montre squelette automatique, mouvement
  apparent — Maison Noirmont » / description 155 c. (grappe ≈ 8 400/mois).
- Image de collection posée (face Octogone — le méga-menu s'en sert).
- **Publiée sur les 3 canaux.** Page contrôlée en préview : bannière + description + « Voir plus »,
  2 produits, facette « Famille : Squelette » (métachamp posé le 29/07) — le `<title>` de l'onglet
  est bien le seo.title.

### Collection « Cadrans chiffres arabes » (créée, `691208290642`, handle `montre-cadran-chiffres-arabes`)
- **Manuelle**, 5 fiches : 3 arabes + 2 aviateurs. Tri meilleures ventes.
- Description SEO pédagogie particulier (grappe ≈ 15 500/mois) : ce que « chiffres arabes » veut
  dire sur un cadran, l'héritage field/flieger sans jargon (« montres de terrain et de bord »),
  lisibilité 1-12, contenu de la famille, calibres nommés séparément (Miyota 8215, Seiko NH35,
  PT5000), stérilité. Aucune marque tierce, aucune promesse non vérifiable (saphir « annoncé »).
- `seo.title` + `seo.description` ensemble : « Montre à cadran chiffres arabes, automatique —
  Maison Noirmont ». Image de collection posée (face Éclaireur Acier).
- **Publiée sur les 3 canaux.** Page contrôlée en préview : 5 produits, facettes Famille/Mouvement.

### Méga-menu (thème brouillon uniquement, `main-menu` intact)
- `sections/header-group.json` : grille desktop « Montres » **5 → 7 vignettes**
  (`max_collections` 7), grille du tiroir mobile **9 → 11**. Empreinte relue = locale :
  `b50c3a07bf328ef25d5b46b699613747`, 21 350 octets (avant `a3048231…`, 21 243 — sauvegarde
  byte-parfaite `backup-publication/header-group.json.avant-grappes-2026-07-29`, copie de travail
  `work-configurateur/header-group.json`). Helio : rien reçu.
- Menu **`noirmont-mobile`** (`334077362514`) : « Montres squelette » et « Cadrans chiffres
  arabes » insérés entre GMT et « Toutes les montres » (ids existants conservés). Les **trois
  endroits** exigés par `2026-07-31-megamenu-illustre.md` §7.4 sont servis.
- Contrôle visuel desktop : le panneau « Montres » rend **7 vignettes illustrées sur 2 rangées**
  (5+2), les 2 nouvelles avec leurs images, + « Toutes les montres ».

## 5. Ce qui reste

1. **Publier le thème `204248088914`** — domaine réservé de Hakim (et supprimer le fork obsolète
   `204329288018`).
2. **Options en anglais sur les 5 nouvelles fiches** (« Color / Size », valeurs `white`,
   `Black Skeleton`, `black 8-sterile`…) — visibles à l'écran 3 du configurateur et sur les
   fiches. Interdit d'y toucher dans cette mission (variantes/mapping gelés) ; à renommer comme
   au décodage du 25/07 (`2026-07-25-renommage-variantes.md`), DSers survit au renommage d'option.
3. `couleur_cadran` absent des 5 nouvelles fiches : elles ne sortent que par « Peu importe ».
   Si Hakim veut les servir par couleur en Q2, poser le métachamp (fiches multi-coloris : décision
   éditoriale à trancher).
4. La vignette Q1 « Squelette » recadre le **1er produit BEST_SELLING** de la collection —
   aujourd'hui le Carré (l'aperçu du 29/07 avait été simulé sur l'Octogone). Rendu contrôlé et
   lisible (mouvement ouvragé) ; l'ordre pourra bouger avec les ventes.
5. Le **cadran arabe oriental** (١٢٣, sens strict de `seiko arabic dial`) reste à re-sourcer.
6. `noirmont-deux-plongeuse-ceramique` : contradiction non tranchée, toujours en DRAFT.
7. À la publication du thème : basculer `main-menu` sur la structure `noirmont-*` ou assumer les
   menus doublons (limite déjà consignée le 26/07).
8. Import d'avis Trustoo sur les 5 nouvelles fiches : non couvert ici (chasse gardée slider/avis).

*Écritures de la mission : 7 `productUpdate` (statut seul) + 7 `publishablePublish` produits,
1 `collectionUpdate` (description+seo) + 1 `collectionCreate` + `collectionAddProductsV2` (5) +
2 images de collection + 2 `publishablePublish` collections, 1 `menuUpdate` (`noirmont-mobile`),
2 `themeFilesUpsert` sur le brouillon (liquid + header-group, empreintes relues conformes).
Panier de la session : 1 ajout de test retiré, état rendu. Rien d'autre.*

---

## 6. Francisation des options des 5 fiches — 30/07/2026

> **Le point 2 du « Ce qui reste » ci-dessus est déjà réglé. La francisation était faite à
> l'arrivée de cette mission — aucune écriture Shopify n'a été nécessaire, et aucune n'a été
> faite. Ce qui suit est un travail de vérification, pas de renommage.**

## 6.1 État trouvé — contredit la consigne de départ

La mission partait du principe que la tentative précédente avait **échoué sur une erreur serveur
sans rien modifier**. C'est faux : les 5 fiches portaient déjà des noms et des valeurs d'option
entièrement en français.

Les 5 `updatedAt` sont groupés sur **9 secondes le 30/07 à 02:44 UTC**
(`02:44:35` → `02:44:42`), dans l'ordre des 5 produits — signature d'un lot de mutations
qui **a bien abouti**. L'erreur serveur est donc survenue *après* les écritures (probablement
sur une requête de contrôle), et l'agent précédent a conclu à tort qu'il n'avait rien appliqué.

Preuve que l'état du 29/07 était bien anglais : les deux relevés de suppression de variantes du
29/07 conservent les libellés d'alors — `variantes-logo-supprimees-bronze-2026-07-29.tsv`
(`blue / Solid caseback`, `black B / Solid caseback`) et
`variantes-logo-supprimees-acier-2026-07-29.tsv` (`black 8-logo / PT5000-glass back`).

**Conséquence : aucun `productOptionUpdate` n'a été émis. Zéro écriture Shopify sur cette
mission.**

## 6.2 Noms d'options — avant / après, et conformité aux conventions

Conventions relevées d'abord sur le catalogue existant (`Trente-Neuf`, `Trente-Six`,
`Noirmont Un`, `Quarante-et-Un`, `Voyageur`) : l'axe cadran s'appelle **« Cadran »**, l'axe
mécanique **« Mouvement & fond »** / **« Mouvement »** / **« Taille & fond »**, et les valeurs
composées s'écrivent avec un séparateur **« · »** (`NH35 · fond verre`).

| Fiche | Option | Avant (29/07) | Après | Conforme au catalogue |
|---|---|---|---|---|
| Éclaireur Bronze `10988849267026` | 1 | Color | **Cadran** | oui — nom canonique |
| | 2 | Size | **Fond de boîtier** | pas de précédent (axe fond isolé) ; français correct |
| Éclaireur Acier `10988849234258` | 1 | Color | **Cadran** | oui |
| | 2 | Size | **Mouvement & fond** | oui — identique à `Noirmont Un` / `Trente-Neuf` |
| Explorateur 3-6-9 `10988849299794` | 1 | Color | **Cadran** | oui |
| | 2 | Size | **Mouvement, diamètre & fond** | variante locale — voir §6.5 |
| Squelette Octogone `10988849365330` | 1 | Color | **Cadran** | oui |
| | 2 | Size | **Fond de boîtier** | idem Bronze, cohérent entre les deux |
| Squelette Carré `10988849135954` | 1 | Color | **Cadran** | oui |
| | 2 | Size | **Mouvement** | oui — identique à `Quarante-et-Un` |

> Précision de méthode : la colonne « Avant » est reprise du **relevé du 29/07 (§5, point 2)**,
> qui note « Color / Size » et les valeurs `white`, `Black Skeleton`, `black 8-sterile`. Aucun
> instantané machine de l'état pré-renommage n'a été conservé (le `scratchpad/backup-publication/`
> cité au §3 n'existe plus sur le disque), et les valeurs anglaises ne sont attestées directement
> que par les deux TSV du 29/07. Les noms d'options d'avant ne sont donc pas re-vérifiables ;
> l'état d'arrivée, lui, l'est intégralement.

Les valeurs de l'axe mécanique reprennent **exactement** la forme canonique du catalogue :
`Miyota 8215 · fond acier`, `NH35 · fond verre`, `PT5000 · fond acier`,
`Miyota 8215 · 36 mm · fond verre`. Aucune variante d'orthographe introduite, donc aucun doublon
de facette créé.

## 6.3 Valeurs — le décodage est fidèle aux codes fournisseur

Les SKU conservent les codes bruts AliExpress, ce qui permet de **vérifier chaque traduction sans
rouvrir la fiche fournisseur**. Contrôle fait sur les 194 variantes : la correspondance est 1:1 et
sans invention.

Éclaireur Bronze (9 cadrans) — `#blue-sterile` → Bleu · `#silver sterile` → Argenté ·
`#green A-sterile` → Vert olive · `#green B sterile` → Vert sapin · `#white sterile` →
Blanc · chiffres rouges · `#black A/B/C/D-sterile` → Noir · chiffres jaunes / chiffres blancs /
chiffres crème · date / chiffres blancs · date. Fond : `Solid caseback` → **Fond acier**,
`Glass caseback` → **Fond verre**.

Squelettes — `#White Skeleton` → Squelette blanc · `#Black Skeleton` → Squelette noir ·
`Glass Back` → Fond verre · `Steel Back` → Fond acier · `NH70 movement` → NH70.

Éclaireur Acier (11 cadrans) — `#green-sterile` → Kaki · `#silver-sterile` → Argenté ·
`#blue-sterile` → Bleu · `#black 1` à `#black 8` → 8 libellés descriptifs distincts
(grands chiffres lumineux, index jaunes, index crème, grands chiffres cuivrés, index blancs,
grandes minutes, chiffres jaunes, trotteuse rouge).

## 6.4 Valeurs laissées non résolues — 6 sur 194, signalées et non devinées

Le fournisseur de l'**Explorateur** livre six couples de codes que rien ne départage
(`Black`/`Black1`, `Green`/`Green1`, `Blue`/`Blue1`, `Orange`/`Orange1`, `Red`/`Red1`,
`White`/`White1`). Ils ont été gardés distincts par un **suffixe « (réf. 1) »** plutôt que par une
description inventée — exactement la convention retenue le 25/07 pour
`Jubilé · or rose (réf. 12)` / `(réf. 15)`.

| Valeur | Code SKU | Pourquoi laissée |
|---|---|---|
| Noir / Noir (réf. 1) | `#Black` / `#Black1` | deux références noires non départageables sans photo |
| Vert / Vert (réf. 1) | `#Green` / `#Green1` | idem |
| Bleu / Bleu (réf. 1) | `#Blue` / `#Blue1` | idem |
| Orange / Orange (réf. 1) | `#Orange` / `#Orange1` | idem |
| Rouge / Rouge (réf. 1) | `#Red` / `#Red1` | idem |
| Argenté · index dorés (+ réf. 1) | `#White` / `#White1` | idem ; « White » rendu par « Argenté · index dorés » d'après les visuels |

**À faire : 6 visuels de variante sur l'Explorateur** pour lever ces 6 doublons, dans la logique
de la liste de visuels du 25/07.

## 6.5 Réserve — un nom d'option hors convention

`Mouvement, diamètre & fond` (Explorateur) porte les trois axes dans son nom, alors que le
catalogue nomme **« Mouvement & fond »** un jeu de valeurs strictement identique
(`Miyota 8215 · 36 mm · fond acier`…) sur les 8 fiches `Trente-Neuf`.

**Laissé tel quel, volontairement** : le nom est français, exact, et le collationnement des
facettes a été vérifié — dans la collection `sport-chic` où vit l'Explorateur, aucune autre fiche
ne porte « Mouvement & fond » (les voisines ont « Cadran » ou « Mouvement »), donc **aucun doublon
de facette n'est créé**. Le catalogue nomme déjà cet axe de 4 façons selon les fiches
(« Mouvement & fond », « Mouvement », « Taille & fond », « Cadran & bracelet ») : c'est un parti
pris existant, pas une régression. À uniformiser un jour, à l'échelle du catalogue, pas de cette
seule fiche.

## 6.6 Contrôles

**Variantes et SKU — inchangés.** Les 194 variantes ont été redescendues une par une
(`variants(first: 250) { id sku }`) :

| Fiche | Variantes | = produit des valeurs | SKU |
|---|---:|---|---|
| Éclaireur Bronze | 18 | 9 cadrans × 2 fonds | 18 bruts, intacts |
| Éclaireur Acier | 66 | 11 × 6 | 66 bruts, intacts |
| Explorateur 3-6-9 | 104 | 13 × 8 | 104 bruts, intacts |
| Squelette Octogone | 4 | 2 × 2 | 4 bruts, intacts |
| Squelette Carré | 2 | 2 × 1 | 2 bruts, intacts |
| **Total** | **194** | — | **194** |

**La preuve du non-écrasement des SKU est directe** : les SKU contiennent encore les chaînes
anglaises du fournisseur (`14:200005100#White Skeleton;5:57000035#Glass Back`,
`14:4#black 8-sterile;…`, `14:200000080#Black1;…`) pendant que les valeurs d'option affichent le
français. Si un SKU avait été réécrit au passage, il serait devenu français. `productOptionUpdate`
n'écrit d'ailleurs pas les SKU. Les identifiants de variante cités le 29/07 sont toujours vivants
et au même prix (`54130353340754` Carré 399 €, `54130362581330` Octogone 429 €), et aucun
identifiant des deux TSV de suppression du 29/07 n'est réapparu.

**Configurateur — pas de couplage aux noms d'options, relu ligne à ligne.**
`sections/noirmont-configurateur.liquid` sur le brouillon `204248088914` : md5
`6c647cbbe7af1eda59270ac291a9b130`, 23 922 octets — **identique à l'empreinte consignée au §3**,
le fichier n'a pas bougé. Il ne contient **aucun nom d'option en dur** : il itère
`{% for opt in p.options_with_values %}`, affiche `Votre {{ opt.name | downcase }}` en légende,
indexe par `opt.position` et sérialise `{{ p.options | json }}`. Le renommage ne peut donc pas
casser les puces « mouvement & fond » — il les **améliore** : les légendes disaient
« Votre color » / « Votre size », elles disent maintenant « Votre cadran », « Votre mouvement &
fond », « Votre fond de boîtier ». Le seul couplage de données du configurateur est le métachamp
`custom.couleur_cadran` et les handles de collection, ni l'un ni l'autre touchés.

**Rendu client — vérifié sur la fiche réelle.** Un onglet de la session de Hakim était déjà posé
sur la PDP Éclaireur Bronze : l'arbre d'accessibilité a été relu **sans naviguer ni cliquer**
(lecture seule du DOM, aucun vol de focus à l'agent de sourcing). Les sélecteurs rendent bien le
français, dans l'ordre exact de la donnée API :

> `Bleu` · `Noir · chiffres blancs · date` · `Noir · chiffres blancs` · `Argenté` ·
> `Vert olive` · `Noir · chiffres jaunes` · `Vert sapin` · `Noir · chiffres crème · date` ·
> `Blanc · chiffres rouges` — puis `Fond acier` · `Fond verre`

9 + 2 boutons radio, aucun libellé anglais, aucun code brut. C'est le **thème live (Helio MAIN)**
qui rend ainsi : le renommage étant une donnée produit, il est déjà servi aux clients, sans
dépendre de la publication du brouillon.

Ce rendu est cohérent avec les trois garde-fous vérifiés par l'API : `selectedOptions` renvoie des
couples nom/valeur français sur les 194 variantes, **aucune option n'est liée à un métachamp**
(`linkedMetafield: null` partout — sinon l'affichage viendrait du métaobjet), et la boutique n'a
**qu'une seule locale**, `fr`, primaire et publiée, **sans aucune traduction enregistrée** : aucune
couche anglaise résiduelle ne peut se substituer aux libellés.

⚠️ **Reste à rejouer par Hakim** : le parcours configurateur en clics réels (un chemin arabe + un
chemin squelette) sur le brouillon `204248088914`. La boutique est en
`passwordProtection.enabled: true`, la consigne interdit de saisir un identifiant, et la session
Chrome authentifiée était occupée. Le risque est faible : aucune mutation n'a été émise, le
fichier du configurateur est byte-identique à son état validé du 29/07, et la relecture de son
code (ci-dessus) montre qu'il ne peut pas dépendre du nom d'une option.

Note factuelle : le thème brouillon `204248088914` porte un `updatedAt` au 30/07 14:57, alors que
le fichier du configurateur est byte-identique à son état du 29/07. La modification porte donc sur
un autre fichier — hors périmètre de cette mission, non investiguée. Helio `204246548818` (MAIN)
n'a pas été approché : son `updatedAt` est resté au 26/07.

## 6.7 DSers — contrôlé, mapping intact

Un onglet DSers (« Mes Produits ») était déjà ouvert dans la session de Hakim : les compteurs ont
été **lus tels quels, sans navigation ni clic**, pour ne pas déranger l'agent de sourcing qui
travaillait dans le même Chrome.

| Compteur | Relevé 29/07 (§1) | Relevé 30/07 | Verdict |
|---|---:|---:|---|
| Mes Produits — Tous | 103 | **103** | inchangé |
| AliExpress | 103 | **103** | inchangé |
| **Unmapped** | **0** | **0** | **inchangé** |
| 1688 / Alibaba | 0 / 0 | 0 / 0 | inchangé |

**Aucune fiche n'est repassée Unmapped après le renommage du 02:44.** Mieux : les 5 fiches
concernées affichent toutes une fourchette de coût fournisseur vivante, preuve directe que le
mapping répond encore — Explorateur `$80.18 ~ 116.84`, Squelette Octogone `$135.30 ~ 135.82`,
Éclaireur Acier `$81.48 ~ 113.40`, Éclaireur Bronze `$122.02 ~ 126.10`, Squelette Carré `$125.16`.

Le constat du 25/07 est donc reconduit une seconde fois : **le renommage de noms et de valeurs
d'option ne démappe pas DSers**, parce que la clé de mapping est le SKU, prouvé intact au §6.6.

*Écritures de cette mission : **aucune**. Ni produit, ni option, ni variante, ni SKU, ni prix, ni
média, ni statut, ni thème, ni collection, ni menu. Aucune commande, aucun identifiant saisi.
Seul ce fichier a été modifié.*

---

## 7. Renommage « Cadrans chiffres arabes » → « Cadrans à chiffres » (30/07/2026)

**Pourquoi.** Les 5 montres de la grappe portent des chiffres **occidentaux** (1, 2, 3) : « chiffres
arabes » au sens horloger, par opposition aux chiffres romains. Techniquement juste, mais le nom
français faisait comprendre à un visiteur francophone des **chiffres arabes orientaux** (١ ٢ ٣),
que nous ne vendons pas. Hakim l'a constaté sur la vitrine.

### État trouvé avant d'écrire (l'agent précédent avait été coupé)

Rien n'avait été fait. Collection `691208290642` encore en `montre-cadran-chiffres-arabes`, titre
« Cadrans chiffres arabes », ancienne description et ancien couple SEO intacts, publiée sur les
3 canaux, 5 produits. Thème brouillon `204248088914` : `sections/header-group.json` encore à
l'empreinte du 29/07 (`b50c3a07bf328ef25d5b46b699613747`, 21 350 o) avec l'ancien handle aux deux
grilles ; menu `noirmont-mobile` encore libellé « Cadrans chiffres arabes ». Aucune redirection.
Article `seiko-mod-ou-montre-hommage-difference` encore avec sa section « Et les cadrans à chiffres
arabes ? » annonçant un aviateur *à venir*. Sauvegardes prises avant écriture dans
`scratchpad/backup-renommage-collection/`.

### Ancien → nouveau

| | Avant | Après |
|---|---|---|
| Titre | Cadrans chiffres arabes | **Cadrans à chiffres** |
| Handle | `montre-cadran-chiffres-arabes` | **`montre-cadran-a-chiffres`** |
| `seo.title` | Montre à cadran chiffres arabes, automatique — Maison Noirmont | **Montre à cadran à chiffres, automatique et lisible — Maison Noirmont** (68 c.) |
| `seo.description` | Montres automatiques à cadran chiffres arabes… | **Montres automatiques à cadran à chiffres : field, aviateur, explorateur 3-6-9. De grands chiffres pleins, lus d'un coup d'œil, acier ou bronze, sans logo.** (154 c.) |
| Alt de l'image | Cadrans chiffres arabes — Maison Noirmont | **Cadrans à chiffres — Maison Noirmont** |

`seo.title` **et** `seo.description` posés **ensemble** dans le même `collectionUpdate` (le
remplacement est wholesale — règle des 47 titres perdus).

### Description réécrite

L'argument vendu est la **lisibilité**, pas l'exotisme : « les heures sont écrites en chiffres —
1, 2, 3 — au lieu d'index bâtons ou de chiffres romains ». Un paragraphe neuf lève l'ambiguïté sans
rien promettre de faux, et c'est là que le vocabulaire métier anglophone reste servi :

> Un mot sur le vocabulaire, parce qu'il prête à confusion : les horlogers appellent ces cadrans
> « arabes » — *arabic numerals*, *arabic dial* en anglais — pour les distinguer des cadrans à
> chiffres romains. Il s'agit bien des chiffres 1 à 12 que vous lisez ici, et non des chiffres
> orientaux de l'écriture arabe : nous n'en proposons pas.

Les paragraphes héritage militaire / contenu de la famille / calibres (Miyota 8215, Seiko NH35,
PT5000, saphir « annoncé ») sont conservés, purgés de toute formule promettant de l'oriental.

### Liens mis à jour

- **Thème brouillon `204248088914` uniquement** — `sections/header-group.json`, les **deux**
  `collection_list` (grille desktop « Montres » et grille du tiroir mobile `nm-mm__drawer-grid`)
  passent au nouveau handle. Empreinte relue = locale : **`26e2e5eb5f3833e946a34a5919bda811`,
  21 340 octets** (avant `b50c3a07…`, 21 350). Le libellé des vignettes est
  `{{ closest.collection.title }}` : il suit le titre tout seul, rien d'autre à toucher.
  **Helio `204246548818` (MAIN) : rien reçu. Thème non publié.**
- **Menu `noirmont-mobile` (`334077362514`)** — item `820670103890` renommé « Cadrans à chiffres »,
  tous les ids conservés, structure identique. L'URL de l'item avait déjà suivi seule (item de type
  COLLECTION lié par `resourceId`). **`main-menu` partagé : pas touché** (il n'a jamais porté
  l'entrée).
- **Article `seiko-mod-ou-montre-hommage-difference` (`615589052754`, toujours NON PUBLIÉ)** — la
  section « Et les cadrans à chiffres arabes ? » devient « **Et les cadrans à chiffres ?** ». Elle
  ne promet plus un modèle « à venir » (il existe) : elle explique la lisibilité, lève l'ambiguïté
  orientale, et **maille vers `/collections/montre-cadran-a-chiffres`** au lieu de renvoyer aux
  Classiques. Reste du corps inchangé (relu intégralement après écriture).

### Redirection

Shopify n'en avait **pas** créé (le changement de handle par API ne la pose pas tout seul —
`redirectNewHandle` n'était pas passé). Créée explicitement :
`urlRedirect 1740923797842` — `/collections/montre-cadran-chiffres-arabes` →
`/collections/montre-cadran-a-chiffres`. **Testée en session Chrome** : l'ancienne URL atterrit sur
la nouvelle, titre « Montre à cadran à chiffres, automatique et lisible — Maison Noirmont ».
(En curl anonyme la page mot de passe intercepte avant la redirection : le test ne vaut qu'en
session ouverte.)

### Contrôle de rendu

- **Desktop (préview brouillon, session Chrome)** : page de collection — H1 « Cadrans à chiffres »,
  bannière, 5 produits, facettes Famille/Mouvement, `<title>` et meta description = les nouveaux.
  Méga-menu « Montres » : **7 vignettes illustrées sur 2 rangées**, la 7e est « Cadrans à chiffres »
  avec son image, lien `/collections/montre-cadran-a-chiffres`.
- **Tiroir mobile** : les 11 vignettes du `drawer_grid` et l'entrée de menu vérifiées **au DOM** —
  7e vignette « Cadrans à chiffres » → nouveau handle, libellés tous corrects.
  ⚠️ **Limite assumée** : le rendu à **375 px n'a pas pu être produit** dans cette session. La
  fenêtre Chrome est en plein écran à 1710 px et `resize_window` est sans effet (il répond
  « Successfully resized » mais `innerWidth` reste 1710) ; iframe et popup sont bloquées par le CSP
  Shopify, l'éditeur de thème rend blanc, et le zoom CSS ne déplace pas les media queries. Le
  nouveau libellé étant **plus court** que l'ancien (18 c. contre 23), aucun risque de débordement
  nouveau ; à revoir d'un œil au prochain passage mobile.

### Complément — les 5 fiches renommées (interdiction produits levée par le coordinateur)

Le coordinateur a levé l'interdiction **pour ce seul point** : titre, handle, description et
`seo.title` + `seo.description` des 5 fiches. **Rien d'autre touché** — ni SKU, ni prix, ni
variantes, ni options, ni médias, ni métachamps, ni statut, ni collections, ni mapping DSers.
(Un autre agent francise les **options** de ces mêmes fiches en parallèle ; aucune collision, je
n'ai écrit que du texte de niveau produit.) Sauvegarde de l'état d'avant :
`scratchpad/backup-renommage-collection/fiches-avant-2026-07-30.json`.

**Formule retenue : « à chiffres 1-12 »** — elle dit ce que le client voit, elle affiche les
chiffres occidentaux dans le titre lui-même, et elle reprend le patron déjà correct de la 5e fiche
(« Explorateur — Sport chic **à chiffres 3-6-9** »). Titres, collection et méga-menu racontent
désormais la même chose.

| ID | Avant | Après | Handle après |
|---|---|---|---|
| 10988849267026 | Éclaireur Bronze — Field militaire à chiffres arabes | **… à chiffres 1-12** | `montre-field-bronze-cadran-chiffres-1-12` |
| 10988849234258 | Éclaireur Acier — Field à chiffres arabes | **… à chiffres 1-12** | `montre-field-acier-cadran-chiffres-1-12` |
| 10978722087250 | Noirmont Un Bronze — Aviateur bronze à chiffres arabes | **… à chiffres 1-12** | `montre-aviateur-bronze-cadran-chiffres-1-12` |
| 10977448558930 | Noirmont Un — Aviateur acier à chiffres arabes | **… à chiffres 1-12** | `montre-aviateur-acier-cadran-chiffres-1-12` |
| 10988849299794 | Explorateur — Sport chic à chiffres 3-6-9 | *inchangée* — aucune mention trompeuse | inchangé |

- **Descriptions** : « douze grands chiffres arabes » → « douze grands chiffres, de 1 à 12 » ;
  « Cadran noir à chiffres arabes — heures 1-12… » → « Cadran noir à chiffres — heures 1-12… ».
  Tout le reste (calibres, saphir « annoncé », étanchéité prudente, mentions de garantie) intact.
- **SEO** : `seo.title` **et** `seo.description` réécrits **ensemble** sur chacune des 4 fiches
  (ex. « Montre aviateur à chiffres 1-12, acier — Noirmont Un »). Aucun `arabic dial` /
  `arabic numerals` dans un texte **français** : le vocabulaire métier anglophone reste servi là où
  il est légitime, dans le corps de la description de collection.
- **Redirections posées et testées** — Shopify n'en crée pas plus pour un produit que pour une
  collection. 4 `urlRedirectCreate` (`1740925665618`, `…698386`, `…731154`, `…763922`) ; les
  4 anciennes URL `/products/…-cadran-chiffres-arabes` répondent **200 sur la nouvelle URL** en
  session. La 5e fiche (Explorateur) répond 200 sur son handle inchangé.

**Configurateur — parcours arabe rejoué en clics réels sur la prévisualisation `204248088914`** :
Q1 « Classique » → Q2 « Peu importe » → écran 3 **« Voici votre Éclaireur Acier »**, URL portant
`montre=montre-field-acier-cadran-chiffres-1-12` (le configurateur résout par handle et a suivi
tout seul) ; bascule sur la pastille **Noirmont Un Bronze** → scène bronze, nom et prix corrects,
URL `montre=montre-aviateur-bronze-cadran-chiffres-1-12`. La ligne « Votre composition » dit
« Cadran Noir · grands chiffres lumineux ». **Balayage programmatique : 59 handles produits
référencés par le configurateur, 0 mort, 0 handle `…arabes` résiduel.** Aucun ajout au panier :
le panier de Hakim est laissé tel quel.

**Contrôle final « aucune trace »** : page de collection, `/`, `/collections/classiques`,
`/collections/sport-chic`, `/collections/montres`, `/search?q=chiffres` et les 5 fiches —
**0 occurrence de « chiffres arabes » en texte visible**. Ce qui reste est **exclusivement** de
l'`alt` de média (attribut `alt="…"` et clé `"alt"` du JSON des visuels) et des **noms de fichiers
CDN** hérités : les médias sont dans les interdits absolus de cette mission, donc laissés en l'état.

### Ce qui reste après cette mission

1. ~~Les 5 titres de fiches~~ **fait** (voir le complément ci-dessus). Reste **l'`alt` des médias**
   et les **noms de fichiers CDN** qui portent encore « chiffres arabes » : invisibles en lecture
   normale, mais lus par les lecteurs d'écran, affichés si une image ne charge pas, et indexés par
   Google Images. Médias gelés dans cette mission — à trancher séparément.
2. Le **cadran arabe oriental** (١٢٣) reste à re-sourcer si Hakim veut réellement servir cette
   recherche — c'est aujourd'hui une famille que nous ne vendons pas.

*Écritures de cette mission : 2 `collectionUpdate` (titre+handle+description+seo ensemble, puis alt
d'image), 1 `themeFilesUpsert` sur le brouillon (empreinte relue conforme), 1 `menuUpdate`
(`noirmont-mobile`), 1 `articleUpdate` (corps, article toujours non publié), **4 `productUpdate`
(titre + handle + description + seo.title/seo.description ensemble, sur 4 fiches ; la 5e non
touchée) + 1 `productUpdate` correctif de coquille sur la description bronze**, et **5
`urlRedirectCreate`** (1 collection + 4 fiches). Aucun SKU, prix, variante, option, média,
métachamp, statut, collection ni mapping DSers touché. Thème non publié. Aucune commande, aucun
ajout au panier.*

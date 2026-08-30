---
type: journal
boutique: seiko-mod
date: 2026-08-10
nature: analyse
leviers: [catalogue, creative]
titre: "Audit des 66 médias de variantes bracelets — 10 août 2026"
---

# Audit des 66 médias de variantes bracelets — 10 août 2026

## Décision exécutable

| Fiche | Médias audités | PRODUISIBLE | BLOQUÉ |
|---|---:|---:|---:|
| `bracelet-caoutchouc-gaufre` | 30 | **30** | **0** |
| `bracelet-fkm-tropical` | 36 | **0** | **36** |
| **Total** | **66** | **30** | **36** |

`PRODUISIBLE` signifie ici : une source réelle et traçable permet une future production image-to-image, sous réserve de la QA normale du livrable. Cela ne signifie ni que la photo AliExpress brute peut être publiée, ni qu'un visuel a été généré pendant cet audit.

`BLOQUÉ` signifie : ne pas générer et ne pas associer de média tant que la preuve manquante n'est pas remplacée par une source propre. Aucun marquage ne doit être effacé ou retouché.

## Périmètre et méthode

### Sources locales

- Réconciliation : `boutique-seiko-mod/journal/2026-08-10-reconciliation-319-visuels-agent.md`.
- État gaufré : `boutique-seiko-mod/livraisons/visuels-codex-2026-08/bracelet-caoutchouc-gaufre/compte-rendu.md`.
- État FKM : `boutique-seiko-mod/livraisons/visuels-codex-2026-08/bracelet-fkm-tropical/compte-rendu.md`.
- Table SKU actuelle : `boutique-seiko-mod/backups/backup-sku-2026-08-08/table-correspondance.jsonl`.
- Copies locales des images SKU gaufrées : `scratchpad/backup-medias-accessoires-lot4/bracelet-caoutchouc-gaufre/`.
- Seule face FKM locale : `scratchpad/noirmont-galeries/entrees-faces/bracelet-fkm-tropical-face.jpg`.

### AliExpress officiel

- Route employée : AliExpress Open Platform / AE-Dropshipper via le VPS autorisé, en lecture seule.
- Article gaufré exact : `1005008681374490`, statut `onSelling`, interrogé le `2026-08-09T22:52:43Z`.
- Réponse : 72 SKU = 36 couples couleur/boucle × 2 largeurs (`20 mm`, `22 mm`), avec une image SKU explicite pour chaque couple.
- Le titre fournisseur confirme la matière : « bracelet gaufré en caoutchouc souple ». Il contient le nom commercial `Watchdives`, mais ce nom n'apparaît pas dans les pixels des 30 images SKU examinées.
- Pour le FKM, aucun `item_id` AliExpress n'est conservé dans les sources locales. Les recherches officielles par mots-clés n'ont pas produit de correspondance traçable avec les 36 fragments SKU. Sans identifiant exact, une ressemblance de catalogue ne vaut pas un appariement fournisseur.

### Grille de contrôle

Pour chaque média :

1. fragment de propriété SKU local présent dans la variante officielle ;
2. image SKU officielle identique pour les largeurs couvertes ;
3. matière et géométrie cohérentes avec la fiche ;
4. couleur du bracelet et finition de boucle visibles et conformes au libellé ;
5. aucun logo, mot, lettre, filigrane ou verbatim visible sur le bracelet ou la boucle.

Les images gaufrées ont été contrôlées ensemble à résolution source locale `640 × 640`, puis par couple couleur/boucle. Elles montrent toutes la même géométrie : face gaufrée, deux passants, rangée de perforations, boucle ardillon et barrettes rapides. Aucun texte n'est visible. Les deux largeurs d'un même couple utilisent la même image, ce qui est cohérent : la largeur n'est pas discriminable sur cette vue produit.

## 1. Bracelet caoutchouc gaufré — 30/30 PRODUISIBLE

Les six couples argentés déjà livrés (vert, rouge, bleu profond, brun, noir et orange) sont hors de cette table. Les 30 lignes ci-dessous sont exactement le reliquat signalé par la réconciliation.

Dans la colonne « Observé », `géométrie OK` signifie la géométrie commune décrite ci-dessus ; `stérile` signifie qu'aucun logo/verbatim n'est visible dans l'image SKU. L'URL complète de chaque preuve est `https://ae01.alicdn.com/kf/<fichier>.jpg`.

| # | Fragment SKU local / propriété AliExpress | SKU officiels 20 / 22 mm | Image SKU officielle | Observé | Verdict |
|---:|---|---|---|---|---|
| 1 | `200000049:76119733#Green-Gold Buckle` | `12000046223682879` / `12000046223682880` | `S6c70132ded634988bc9be556cfa77459Q.jpg` | Vert olive, boucle dorée ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 2 | `200000049:16146268#Green-Black Buckle` | `12000046223682877` / `12000046223682878` | `S13fed8f6a3404dcc8ff3a7cf39ecae8df.jpg` | Vert olive, boucle noire ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 3 | `200000049:100013775#Green-Rose Gold` | `12000046223682881` / `12000046223682882` | `Scbbad5d754d1462aa9f9ee63b5cf5955Y.jpg` | Vert olive, boucle or rose ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 4 | `200000049:200966040#White-Silver Buckle` | `12000046223682883` / `12000046223682884` | `S66b23525f95a4a5a8c8612c56abf8226Z.jpg` | Blanc, boucle argentée ; contour et relief restent lisibles sur fond blanc, géométrie OK, stérile. | **PRODUISIBLE** |
| 5 | `200000049:201102690#White-Gold Buckle` | `12000046223682887` / `12000046223682888` | `S4f42f835c69f44f7b5d8f74212e88afaK.jpg` | Blanc, boucle dorée ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 6 | `200000049:201009050#White-Black Buckle` | `12000046223682885` / `12000046223682886` | `S239ca108e0784e54b0d02c894b97db3eo.jpg` | Blanc, boucle noire ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 7 | `200000049:201449057#White-Rose Gold` | `12000046223682889` / `12000046223682890` | `S2adb8790a7254d27b9e39bd809226072G.jpg` | Blanc, boucle or rose ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 8 | `200000049:201662806#Orange-Gold Buckle` | `12000046223682895` / `12000046223682896` | `S55ee431bae7546c6b11c6eedb4d2f08eq.jpg` | Orange, boucle dorée ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 9 | `200000049:201449062#Orange-Black Buckle` | `12000046223682893` / `12000046223682894` | `Sb6eca4cd94df43e1ae92fba88a7ccc98g.jpg` | Orange, boucle noire ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 10 | `200000049:506942013#Orange-Rose Gold` | `12000046223682897` / `12000046223682898` | `Saf45cc33942e45ccaf9f91721cb449acP.jpg` | Orange, boucle or rose ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 11 | `200000049:990994103#Yellow-Silver Buckle` | `12000046223682899` / `12000046223682900` | `Sba4178c4b8e747bf8372f3af0d00fb1fZ.jpg` | Jaune, boucle argentée ; relief et perforations nets, géométrie OK, stérile. | **PRODUISIBLE** |
| 12 | `200000049:1366657163#Yellow-Gold Buckle` | `12000046223682903` / `12000046223682904` | `Sce192e43ef624f76b443a136c35efa908.jpg` | Jaune, boucle dorée ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 13 | `200000049:1178274895#Yellow-Black Buckle` | `12000046223682901` / `12000046223682902` | `Sa0e32d9a073c44f798b88631b23245deY.jpg` | Jaune, boucle noire ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 14 | `200000049:1386586452#Yellow-Rose Gold` | `12000046223682905` / `12000046223682906` | `Sdb779c350bd94da68997b5d6dbc4d452v.jpg` | Jaune, boucle or rose ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 15 | `200000049:1714056674#Light Blue-Silver` | `12000046223682907` / `12000046223682908` | `Se8dccc5aba944b87ba6eae079892479bQ.jpg` | Bleu clair/cyan, boucle argentée ; relief et perforations nets, géométrie OK, stérile. | **PRODUISIBLE** |
| 16 | `200000049:2490560973#Light Blue-Gold` | `12000046223682911` / `12000046223682912` | `S9720d4ff3a5746b994f53bb2b255fbc2w.jpg` | Bleu clair/cyan, boucle dorée ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 17 | `200000049:2332437014#Light  Blue-Black` | `12000046223682909` / `12000046223682910` | `S5e1276900f7b458bb7d4c0e82abe3937B.jpg` | Bleu clair/cyan, boucle noire ; le double espace du libellé officiel est conservé, géométrie OK, stérile. | **PRODUISIBLE** |
| 18 | `200000049:2792782423#Light Blue-Rose Gold` | `12000046223682913` / `12000046223682914` | `S1daeab5dbb9a483887cad9c59e6c3b97V.jpg` | Bleu clair/cyan, boucle or rose ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 19 | `200000049:5057797568#Deep Blue-Gold` | `12000046223682919` / `12000046223682920` | `S670dd1e6f205481990ffada71bbe8459z.jpg` | Bleu profond, boucle dorée ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 20 | `200000049:5057746941#Deep Blue-Black` | `12000046223682917` / `12000046223682918` | `Se3a170b1103746818530a61c4916a6f6I.jpg` | Bleu profond, boucle noire ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 21 | `200000049:5057817297#Deep Blue-Rose Gold` | `12000046223682921` / `12000046223682922` | `Sd9c5cab7a11d4906adcf4321081b02933.jpg` | Bleu profond, boucle or rose ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 22 | `200000049:173#Brown-Gold Buckle` | `12000046223682927` / `12000046223682928` | `Sacee49a75d43463ea2a6447e94e54a45x.jpg` | Brun, boucle dorée ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 23 | `200000049:193#Brown-Black Buckle` | `12000046223682925` / `12000046223682926` | `Sa982a65a5d574d93a0780fff45a12da2d.jpg` | Brun, boucle noire ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 24 | `200000049:100005979#Brown-Rose Gold` | `12000046223682929` / `12000046223682930` | `S8562e1a983a546b69cf8e873e1c92cdfL.jpg` | Brun, boucle or rose ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 25 | `200000049:203596455#Black-Gold Buckle` | `12000046223682935` / `12000046223682936` | `S6e8330f9e954458dbfd596dab65a3477U.jpg` | Noir, boucle dorée ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 26 | `200000049:691#Black-Black Buckle` | `12000046223682933` / `12000046223682934` | `S1ef3a642c8c74c6a87b6127e0bf4ed61G.jpg` | Noir, boucle noire ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 27 | `200000049:1954454310#Black-Rose Gold` | `12000046223682937` / `12000046223682938` | `S6fa23deb30a84283a9e85233cb473a2ej.jpg` | Noir, boucle or rose ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 28 | `200000049:200000080#Red-Gold Buckle` | `12000046223682943` / `12000046223682944` | `S760805ff17524b6c9ee3f6b8ac54cea2k.jpg` | Rouge, boucle dorée ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 29 | `200000049:200013899#Red-Black Buckle` | `12000046223682941` / `12000046223682942` | `S0d9ba8fc17c84b6ca76eae63d38c97b2Y.jpg` | Rouge, boucle noire ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |
| 30 | `200000049:366#Red-Rose Gold` | `12000046223682945` / `12000046223682946` | `S7354d5c27bbe4eae9e6cbdbdbc631abfC.jpg` | Rouge, boucle or rose ; matière caoutchouc, géométrie OK, stérile. | **PRODUISIBLE** |

### Manquant et recommandation pour ce lot

- **Manquant :** aucun blocage source pour ces 30 couples. Le contrôle porte sur la faisabilité, pas sur de futurs livrables.
- **Recommandation exacte :** produire chaque couple depuis son image SKU dédiée ci-dessus ; conserver strictement la couleur de bracelet et la finition de boucle ; exécuter ensuite une QA zoomée du résultat. Ne pas utiliser une boucle argentée comme base pour inventer les finitions noire, dorée ou or rose.

## 2. Bracelet FKM tropical — 36/36 BLOQUÉ

### Observé

- La table locale contient 36 couples couleur/boucle, chacun décliné en `18 mm`, `20 mm` et `22 mm` : 108 variantes actuelles, mais 36 médias visuels attendus.
- La seule face locale est un très gros plan de l'envers d'un bracelet noir. Elle ne montre ni le produit complet, ni la boucle, ni une couleur autre que noire.
- Un marquage central y est déjà flouté/masqué et un embossage résiduel reste douteux. Cette image est donc irrecevable comme source « sans marque » et ne doit pas être corrigée davantage.

### Manquant commun aux 36 lignes

Code `F0` : `item_id` AliExpress exact absent ; aucune réponse officielle de variantes ; aucune image SKU attribuable ; matière FKM non prouvée par la source officielle ; géométrie du produit complet non visible ; couleur et finition de boucle non prouvées ; absence de marque non démontrable.

| # | Fragment SKU local | Largeurs locales | Source / image officielle | Verdict |
|---:|---|---|---|---|
| 1 | `200000049:100006062#FKM-khaki Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 2 | `200000049:1202#FKM-khaki Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 3 | `200000049:200013901#FKM-khaki Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 4 | `200000049:100013775#FKM-Orange Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 5 | `200000049:201009050#FKM-Orange Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 6 | `200000049:200966040#FKM-Orange Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 7 | `200000049:6677#FKM-Cyan Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 8 | `200000049:202243810#FKM-Cyan Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 9 | `200000049:1089#FKM-Cyan Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 10 | `200000049:990994103#FKM-SkyBlue Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 11 | `200000049:1366657163#FKM-SkyBlue Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 12 | `200000049:1178274895#FKM-SkyBlue Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 13 | `200000049:1386586452#FKM-White Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 14 | `200000049:2332437014#FKM-White Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 15 | `200000049:1714056674#FKM-White Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 16 | `200000049:3348727#FKM-Red Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 17 | `200000049:76119733#FKM-Red Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 18 | `200000049:16146268#FKM-Red Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 19 | `200000049:5057835040#FKM-Gray Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 20 | `200000049:173#FKM-Gray Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 21 | `200000049:193#FKM-Gray Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 22 | `200000049:6144#FKM-ArmyGreen Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 23 | `200000049:200025551#FKM-ArmyGreen Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 24 | `200000049:771#FKM-ArmyGreen Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 25 | `200000049:201102690#FKM-Black Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 26 | `200000049:201449058#FKM-Black Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 27 | `200000049:201449057#FKM-Black Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 28 | `200000049:201449062#FKM-Blue Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 29 | `200000049:506942013#FKM-Blue Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 30 | `200000049:201662806#FKM-Blue Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 31 | `200000049:2490560973#FKM-Brown Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 32 | `200000049:5057743953#FKM-Brown Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 33 | `200000049:2792782423#FKM-Brown Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 34 | `200000049:5057746941#FKM-Yellow Silver` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 35 | `200000049:5057817297#FKM-Yellow Gold` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |
| 36 | `200000049:5057797568#FKM-Yellow Black` | 18 / 20 / 22 mm | `F0` | **BLOQUÉ** |

### Décision et recommandation pour ce lot

- **Décision :** maintenir les 36 médias FKM hors production.
- **Réouverture possible uniquement si :** l'`item_id` exact est retrouvé, l'API officielle retourne les 36 propriétés SKU avec leurs images, le bracelet complet et la boucle sont visibles pour chaque couple, la matière FKM est prouvée, et le contrôle zoomé ne révèle aucun logo/verbatim.
- **Si cette preuve ne peut pas être réunie :** abandonner ce lot visuel et re-sourcer un bracelet FKM stérile disposant d'un nuancier complet. La face floutée actuelle ne doit jamais servir de base et aucun marquage ne doit être retouché.

## Actions explicitement non réalisées

- aucune génération d'image ;
- aucune retouche ou suppression de marque ;
- aucune mutation Shopify ou DSers ;
- aucun ordre, achat ou publication ;
- aucun commit ni push.

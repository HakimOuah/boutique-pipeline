# Audit des 130 médias P4 restants — 10 août 2026

## Décision exécutable

| Périmètre | Médias | PRODUISIBLE | BLOQUÉ | ABANDON |
|---|---:|---:|---:|---:|
| P4 restant, hors bracelet caoutchouc gaufré et hors bracelet FKM tropical | **130** | **27** | **99** | **4** |

Les **27 médias PRODUISIBLES** sont limités à :

- 6 Bracelet acier massif — les six finitions ;
- 3 Bracelet Jubilé — embouts courbes ;
- 8 Bracelet milanais — maille italienne ;
- 5 Coussins de présentation, lot de 10 — les cinq teintes ;
- 2 Étui de voyage rigide : `Black Purple 6 Slot` et `Black Green 6 Slot` ;
- 2 Outil de mise à taille : noir et argenté ;
- 1 Rouleau de voyage noir : `WB13`, capacité 3 montres.

`PRODUISIBLE` signifie qu'une image SKU officielle et exacte montre un produit lui-même visuellement stérile et fidèle au produit/coloris, permettant une future production image-to-image. Une annotation photographique située hors du produit peut être exclue par nouvelle composition ; elle n'est pas assimilée à un marquage physique. Cela n'autorise pas la publication de la photo AliExpress brute et ne signifie pas qu'un visuel a été généré pendant cet audit.

`BLOQUÉ` signifie qu'aucune production honnête ne doit être lancée avant remplacement de la preuve : identifiant exact absent, texte ou marquage touchant le produit ou impossible à exclure sans altérer la preuve, montre de décor marquée, ou variante/capacité non démontrée.

`ABANDON` signifie ici retirer le média du plan de production P4 : la source locale contredit la nature même de la fiche et aucun article AliExpress exact n'est conservé. Toute éventuelle archive de produit/variante reste une action commerciale séparée et n'a pas été exécutée.

## 1. Périmètre reconstitué

La table P4 de `boutique-seiko-mod/BRIEF-VISUELS-CODEX-2026-08-08.md` contient 196 médias de variantes. Après retrait des 30 gaufrés et des 36 FKM tropical déjà tranchés, il reste exactement :

```text
196 - 30 - 36 = 130
```

La reconstruction part de `boutique-seiko-mod/backup-sku-2026-08-08/table-correspondance.jsonl`. Le média demandé correspond au premier fragment de `sku_actuel`, avant le premier point-virgule. Les treize variantes déjà couvertes par les visuels de référence ont été exclues seulement pour les familles où le brief demande moins de médias que de valeurs actuelles : Bois beige/noir, Cuir PU, quatre Rouleaux, quatre Remontoirs bois et deux Collection bois LED.

Contrôle mécanique final : **130 lignes**, sans doublon `handle + fragment`.

## 2. Sources et méthode

### AliExpress officiel uniquement

Les appels ont utilisé la route AliExpress Open Platform / AE-Dropshipper par le VPS autorisé, en lecture seule. Les réponses brutes sont conservées sous :

`boutique-seiko-mod/preuves-audit-p4-130-2026-08-10/`

Articles exacts retrouvés et interrogés :

| Famille | Item AliExpress exact |
|---|---:|
| Bracelet cuir daim | `1005008944176821` |
| Bracelet milanais | `1005007722911159` |
| Loupe d'horloger | `1005009885282058` |
| Bracelet Jubilé embouts courbes | `1005007791535629` |
| Bracelet acier massif | `1005008549962039` |
| Coussins | `1005003898684752` |
| Étui de voyage rigide | `1005011858146866` |
| Outil de mise à taille | `1005005877471703` |
| Doigtiers | `1005008806614490` |
| Loupe de date | `1005011940440567` |
| Remontoir Collection | `1005006938556690` |
| Rouleau de voyage | `1005008493748701` |
| Bracelet Présidentiel, fournisseur correspondant aux quatre fragments actuels | `1005006496083816` |

Pour le Présidentiel, `boutique-seiko-mod/backup-veracite-2026-07-26/mapping-dsers.txt` conserve deux fournisseurs historiques. Le fournisseur 2 ci-dessus est celui dont la réponse officielle retourne exactement les quatre fragments actuels `NO.1 President`, `NO.2 Jubilee`, `NO.3 Polished Center` et `NO.4 Brushed Center`.

### Preuves visuelles locales

Les images SKU des familles sauvegardées avant suppression Shopify sont sous `scratchpad/backup-medias-accessoires-lot4/`. Leur nom de fichier est identique au basename CDN indiqué ligne par ligne ci-dessous.

Les sources locales problématiques contrôlées sont :

- `scratchpad/noirmont-galeries/entrees-faces/bracelet-fkm-courbe-face.jpg` : bracelet noir générique, droit, non fidèle à la variante Orange 22 mm qui lui est associée ;
- `scratchpad/noirmont-galeries/entrees-faces/barrettes-de-rechange-270-face.jpg` : barrettes en vrac, sans preuve des quatre conditionnements ;
- `scratchpad/noirmont-galeries/entrees-faces/pince-a-barrettes-face.jpg` : une seule pince argentée, sans preuve des trois finitions ;
- `scratchpad/noirmont-galeries/entrees-faces/coffret-douze-aluminium-face.jpg` : une vue 12 places seulement, impropre à prouver 6/12/24 ;
- `boutique-seiko-mod/entrees-faces-REDONDANT-export-claude/remontoir-solo-face.jpg` : inscription gravée en façade, couleur non probante pour Vert/Blanc ;
- les quatre fichiers `boutique-seiko-mod/visuels-2026-07-25/generated/remontoir-bois-*.jpg` : boîtes passives à un coussin, pas des remontoirs motorisés à deux montres.

### Grille de décision

Chaque ligne exige simultanément :

1. fragment local retrouvé dans la matrice officielle de l'article exact ;
2. image SKU attribuable à cette valeur ;
3. matière, géométrie, capacité et coloris cohérents ;
4. aucun logo, verbatim ou marquage physique sur le produit ; une annotation ou un cartouche photographique hors produit peut être exclu par nouvelle composition fidèle, sans retoucher le produit ;
5. aucune marque sur une montre de décor.

Une recherche textuelle négative ne prouve pas l'inexistence d'un produit. Les familles sans item exact restent donc BLOQUÉES, sauf les quatre Remontoirs bois dont les sources disponibles démontrent un produit d'une autre nature.

## 3. Codes de contrôle

| Code | Observation | Décision |
|---|---|---|
| `P1` | Image SKU exacte Jubilé, variante explicitement `no logo`, fermoir vierge, couleur fidèle. | PRODUISIBLE |
| `P2` | Image SKU milanaise exacte, maille/largeur de maille et finition fidèles, fermoir vierge. | PRODUISIBLE |
| `P3` | Étui exact montré vide, capacité et coloris visibles, aucun texte/logo. | PRODUISIBLE |
| `P4` | Outil exact noir/argenté, géométrie complète, aucun texte/logo. | PRODUISIBLE |
| `P5` | Rouleau noir exact, 3 emplacements montrés vides, aucun texte/logo. | PRODUISIBLE |
| `P6` | Bracelet acier massif exact, bracelet et finition entièrement visibles, fermoir vierge ; `gift` et filigrane sont des annotations photographiques séparées du produit et excluables par nouvelle composition. | PRODUISIBLE |
| `P7` | Image SKU 800 × 800 montrant exactement 10 coussins de la teinte, sans texte ni `PCS` visible dans l'original. | PRODUISIBLE |
| `B2` | Image SKU exacte mais cartouche `GIFT` visible dans chaque vignette. | BLOQUÉ |
| `B3` | Image SKU exacte mais caractères/filigrane chinois et repères rouges visibles. | BLOQUÉ |
| `B4` | Doigtiers : quantité `PCS` imprimée dans l'image. | BLOQUÉ |
| `B5` | Montres de décor avec marques/verbatim visibles ; la seule exception vide reçoit `P3` ou `P5`. | BLOQUÉ |
| `B6` | Marquage fonctionnel `3X/5X/10X/15X/20X`, texte de kit ou filigrane visible. | BLOQUÉ |
| `B7` | Note technique en anglais incrustée dans chaque image SKU ; image générique commune qui ne discrimine pas les dimensions. | BLOQUÉ |
| `B8` | Marque `IBBETON`, capacité, caractéristiques et/ou étiquette incrustées. | BLOQUÉ |
| `U1` | Item AliExpress exact manquant ; recherche API non concluante et source locale insuffisante. | BLOQUÉ |
| `A1` | Source locale = boîte passive à un coussin, alors que la valeur vise un remontoir motorisé à 2 montres ; aucun item exact. | ABANDON |

## 4. Totaux par fiche

| Fiche | Total | PRODUISIBLE | BLOQUÉ | ABANDON |
|---|---:|---:|---:|---:|
| `barrettes-de-rechange-270` | 4 | 0 | 4 | 0 |
| `bracelet-acier-massif-12-22-mm` | 6 | 6 | 0 | 0 |
| `bracelet-cuir-daim-degagement-rapide` | 16 | 0 | 16 | 0 |
| `bracelet-fkm-courbe` | 16 | 0 | 16 | 0 |
| `bracelet-jubile-embouts-courbes` | 3 | 3 | 0 | 0 |
| `bracelet-milanais-maille-italienne` | 8 | 8 | 0 | 0 |
| `bracelet-presidentiel-904l` | 4 | 0 | 4 | 0 |
| `coffret-douze-aluminium` | 3 | 0 | 3 | 0 |
| `coussins-de-presentation-lot-de-10` | 5 | 5 | 0 | 0 |
| `doigtiers-d-horloger-latex` | 6 | 0 | 6 | 0 |
| `etui-de-voyage-rigide` | 9 | 2 | 7 | 0 |
| `loupe-d-horloger` | 13 | 0 | 13 | 0 |
| `loupe-de-date-saphir` | 8 | 0 | 8 | 0 |
| `outil-de-mise-a-taille-de-bracelet` | 2 | 2 | 0 | 0 |
| `pince-a-barrettes` | 3 | 0 | 3 | 0 |
| `remontoir-bois-acajou` | 1 | 0 | 0 | 1 |
| `remontoir-bois-ebene` | 1 | 0 | 0 | 1 |
| `remontoir-bois-noir-laque` | 1 | 0 | 0 | 1 |
| `remontoir-bois-noyer` | 1 | 0 | 0 | 1 |
| `remontoir-collection-bois-beige` | 3 | 0 | 3 | 0 |
| `remontoir-collection-bois-led-noir` | 1 | 0 | 1 | 0 |
| `remontoir-collection-bois-led-rouge` | 1 | 0 | 1 | 0 |
| `remontoir-collection-bois-noir` | 3 | 0 | 3 | 0 |
| `remontoir-collection-cuir-pu` | 2 | 0 | 2 | 0 |
| `remontoir-solo` | 2 | 0 | 2 | 0 |
| `rouleau-de-voyage-bleu-marine-cuir` | 2 | 0 | 2 | 0 |
| `rouleau-de-voyage-brun-cuir` | 2 | 0 | 2 | 0 |
| `rouleau-de-voyage-noir-cuir` | 2 | 1 | 1 | 0 |
| `rouleau-de-voyage-vert-cuir` | 2 | 0 | 2 | 0 |
| **TOTAL** | **130** | **27** | **99** | **4** |

## 5. Décision ligne par ligne — 130/130

| # | Handle | Valeur | Fragment SKU | Source exacte | Contrôle | Verdict |
|---:|---|---|---|---|---|---|
| 1 | `barrettes-de-rechange-270` | 72pcs | `14:175#72pcs` | — | `U1` | **BLOQUÉ** |
| 2 | `barrettes-de-rechange-270` | 1.5mm 8-25mm | `14:193#1.5mm 8-25mm` | — | `U1` | **BLOQUÉ** |
| 3 | `barrettes-de-rechange-270` | 144pcs | `14:350686#144pcs` | — | `U1` | **BLOQUÉ** |
| 4 | `barrettes-de-rechange-270` | 33pcs | `14:865#33pcs` | — | `U1` | **BLOQUÉ** |
| 5 | `bracelet-acier-massif-12-22-mm` | Rose-Gold | `200000049:16146268#Rose-Gold` | item `1005008549962039` · image `S422ad12c29be47cdb607955379ef8450O.jpg` | `P6` | **PRODUISIBLE** |
| 6 | `bracelet-acier-massif-12-22-mm` | Gold | `200000049:193#Gold` | item `1005008549962039` · image `S7868a8b95e2b4d66b2ff95ca2b3ac403j.jpg` | `P6` | **PRODUISIBLE** |
| 7 | `bracelet-acier-massif-12-22-mm` | Silver-Gold | `200000049:3348727#Silver-Gold` | item `1005008549962039` · image `S03384815a8944c4db0cf1ba2f7bc5d23g.jpg` | `P6` | **PRODUISIBLE** |
| 8 | `bracelet-acier-massif-12-22-mm` | Silver-RoseGold | `200000049:350850#Silver-RoseGold` | item `1005008549962039` · image `S2db9e66b645f484ebb0b1fa5b8c7d0e5W.jpg` | `P6` | **PRODUISIBLE** |
| 9 | `bracelet-acier-massif-12-22-mm` | Black | `200000049:365462#Black` | item `1005008549962039` · image `S8dd5b35818044d6fb91d7399f1754a918.jpg` | `P6` | **PRODUISIBLE** |
| 10 | `bracelet-acier-massif-12-22-mm` | Silver | `200000049:76119733#Silver` | item `1005008549962039` · image `S3b21c39457384f0c88262b7a5c971f10J.jpg` | `P6` | **PRODUISIBLE** |
| 11 | `bracelet-cuir-daim-degagement-rapide` | Black-Black | `200000049:100013775#Black-Black` | item `1005008944176821` · image `S98c21e2e334c43a38e0d4c5f1d5303d4a.jpg` | `B2` | **BLOQUÉ** |
| 12 | `bracelet-cuir-daim-degagement-rapide` | Brown-Black | `200000049:1386586452#Brown-Black` | item `1005008944176821` · image `Sa88679c6c5b74266b6809d3346715228E.jpg` | `B2` | **BLOQUÉ** |
| 13 | `bracelet-cuir-daim-degagement-rapide` | Beige | `200000049:16146268#Beige` | item `1005008944176821` · image `S7c2e0551689e4afb828f1a327789c6e4G.jpg` | `B2` | **BLOQUÉ** |
| 14 | `bracelet-cuir-daim-degagement-rapide` | YellowBrown | `200000049:1714056674#YellowBrown` | item `1005008944176821` · image `S1be603d46c3643c8a5ac8f3cb18fdaded.jpg` | `B2` | **BLOQUÉ** |
| 15 | `bracelet-cuir-daim-degagement-rapide` | Blue | `200000049:200966040#Blue` | item `1005008944176821` · image `Sd46d6d829d914c33bde451d852978361d.jpg` | `B2` | **BLOQUÉ** |
| 16 | `bracelet-cuir-daim-degagement-rapide` | Blue-Black | `200000049:201449057#Blue-Black` | item `1005008944176821` · image `Sc56eee1ff4674b2ebe17cea4786ed97aK.jpg` | `B2` | **BLOQUÉ** |
| 17 | `bracelet-cuir-daim-degagement-rapide` | Green | `200000049:201449058#Green` | item `1005008944176821` · image `S18b312d8c1114ebf976e381035d57a6fN.jpg` | `B2` | **BLOQUÉ** |
| 18 | `bracelet-cuir-daim-degagement-rapide` | YellowBrown-Black | `200000049:2792782423#YellowBrown-Black` | item `1005008944176821` · image `Sd44c42a518d14beaba9ee1b2c379c300n.jpg` | `B2` | **BLOQUÉ** |
| 19 | `bracelet-cuir-daim-degagement-rapide` | Black | `200000049:3348727#Black` | item `1005008944176821` · image `S2f0920aadd4d43969e8d45fae7d1c069k.jpg` | `B2` | **BLOQUÉ** |
| 20 | `bracelet-cuir-daim-degagement-rapide` | Gray-Black | `200000049:350686#Gray-Black` | item `1005008944176821` · image `Sf8fb008825de424ebbe2ed589a0893c6c.jpg` | `B2` | **BLOQUÉ** |
| 21 | `bracelet-cuir-daim-degagement-rapide` | Beige-Black | `200000049:350850#Beige-Black` | item `1005008944176821` · image `S8391ad335ef747e1b9d4c7ce89a2b4d9v.jpg` | `B2` | **BLOQUÉ** |
| 22 | `bracelet-cuir-daim-degagement-rapide` | Light Blue | `200000049:5057743953#Light Blue` | item `1005008944176821` · image `S5d97cfd4b82e4672912c81a49d7a1b65N.jpg` | `B2` | **BLOQUÉ** |
| 23 | `bracelet-cuir-daim-degagement-rapide` | Light Blue-Black | `200000049:5057817297#Light Blue-Black` | item `1005008944176821` · image `Sa8ee3a744fdb403ba336a710fe933064f.jpg` | `B2` | **BLOQUÉ** |
| 24 | `bracelet-cuir-daim-degagement-rapide` | Gray | `200000049:5057835040#Gray` | item `1005008944176821` · image `S69cd4a751b48418abbc9c70a88ae5d0b1.jpg` | `B2` | **BLOQUÉ** |
| 25 | `bracelet-cuir-daim-degagement-rapide` | Green-Black | `200000049:506942013#Green-Black` | item `1005008944176821` · image `S65c5cae85ef74c44bbfaef0469d00fb0u.jpg` | `B2` | **BLOQUÉ** |
| 26 | `bracelet-cuir-daim-degagement-rapide` | Brown | `200000049:990994103#Brown` | item `1005008944176821` · image `Sd4fbcbfac3664e8ba91e7be0dc9dbbe3A.jpg` | `B2` | **BLOQUÉ** |
| 27 | `bracelet-fkm-courbe` | Orange | `200000049:100013775#Orange` | — | `U1` | **BLOQUÉ** |
| 28 | `bracelet-fkm-courbe` | Army green 02 | `200000049:1178274895#Army green 02` | — | `U1` | **BLOQUÉ** |
| 29 | `bracelet-fkm-courbe` | Brown 02 | `200000049:1366657163#Brown 02` | — | `U1` | **BLOQUÉ** |
| 30 | `bracelet-fkm-courbe` | Grey 02 | `200000049:1386586452#Grey 02` | — | `U1` | **BLOQUÉ** |
| 31 | `bracelet-fkm-courbe` | Royal blue | `200000049:16146268#Royal blue` | — | `U1` | **BLOQUÉ** |
| 32 | `bracelet-fkm-courbe` | Khaki | `200000049:200966040#Khaki` | — | `U1` | **BLOQUÉ** |
| 33 | `bracelet-fkm-courbe` | Army green | `200000049:201009050#Army green` | — | `U1` | **BLOQUÉ** |
| 34 | `bracelet-fkm-courbe` | Brown | `200000049:201102690#Brown` | — | `U1` | **BLOQUÉ** |
| 35 | `bracelet-fkm-courbe` | Grey | `200000049:201449057#Grey` | — | `U1` | **BLOQUÉ** |
| 36 | `bracelet-fkm-courbe` | Black 02 | `200000049:201449058#Black 02` | — | `U1` | **BLOQUÉ** |
| 37 | `bracelet-fkm-courbe` | Royal blue 02 | `200000049:201449062#Royal blue 02` | — | `U1` | **BLOQUÉ** |
| 38 | `bracelet-fkm-courbe` | Red 02 | `200000049:201662806#Red 02` | — | `U1` | **BLOQUÉ** |
| 39 | `bracelet-fkm-courbe` | Black | `200000049:3348727#Black` | — | `U1` | **BLOQUÉ** |
| 40 | `bracelet-fkm-courbe` | Orange 02 | `200000049:506942013#Orange 02` | — | `U1` | **BLOQUÉ** |
| 41 | `bracelet-fkm-courbe` | Red | `200000049:76119733#Red` | — | `U1` | **BLOQUÉ** |
| 42 | `bracelet-fkm-courbe` | Khaki 02 | `200000049:990994103#Khaki 02` | — | `U1` | **BLOQUÉ** |
| 43 | `bracelet-jubile-embouts-courbes` | steel gold-no logo | `200000049:100013777#steel gold-no logo` | item `1005007791535629` · image `Sce54a477960e4715aabb421d0a583a549.jpg` | `P1` | **PRODUISIBLE** |
| 44 | `bracelet-jubile-embouts-courbes` | gold-no logo | `200000049:3348727#gold-no logo` | item `1005007791535629` · image `S1ae6f72ff2534409a20cb14c8de06a99J.jpg` | `P1` | **PRODUISIBLE** |
| 45 | `bracelet-jubile-embouts-courbes` | steel-no logo | `200000049:350853#steel-no logo` | item `1005007791535629` · image `S2ff6ba6587bb4bcfbdb8771e9c6a5b49C.jpg` | `P1` | **PRODUISIBLE** |
| 46 | `bracelet-milanais-maille-italienne` | 0.6mm-black | `200000049:193#0.6mm-black` | item `1005007722911159` · image `Sed8fd068214f471e96a06492b6be150eB.jpg` | `P2` | **PRODUISIBLE** |
| 47 | `bracelet-milanais-maille-italienne` | 1.0mm-gold | `200000049:200000080#1.0mm-gold` | item `1005007722911159` · image `S96d78f4267fe4e6ab3d7e7aa60b114cd3.jpg` | `P2` | **PRODUISIBLE** |
| 48 | `bracelet-milanais-maille-italienne` | 1.0mm-silver | `200000049:200013899#1.0mm-silver` | item `1005007722911159` · image `S30071232fbe142b9b39e2a7664e34ca5o.jpg` | `P2` | **PRODUISIBLE** |
| 49 | `bracelet-milanais-maille-italienne` | 1.0mm-rose gold | `200000049:29#1.0mm-rose gold` | item `1005007722911159` · image `S7d27ad5e4a644f4ba36f111c2811c8508.jpg` | `P2` | **PRODUISIBLE** |
| 50 | `bracelet-milanais-maille-italienne` | 0.6mm-rose gold | `200000049:3348727#0.6mm-rose gold` | item `1005007722911159` · image `S613f8dd833d14fa1b8f0fa1b8f8081f9j.jpg` | `P2` | **PRODUISIBLE** |
| 51 | `bracelet-milanais-maille-italienne` | 0.6mm-gold | `200000049:350850#0.6mm-gold` | item `1005007722911159` · image `Scd5c85c5ba08405ea4570af4a10fb3a3X.jpg` | `P2` | **PRODUISIBLE** |
| 52 | `bracelet-milanais-maille-italienne` | 0.6mm-silver | `200000049:350853#0.6mm-silver` | item `1005007722911159` · image `S029596f5742d41c5be2e841d69684eca5.jpg` | `P2` | **PRODUISIBLE** |
| 53 | `bracelet-milanais-maille-italienne` | 1.0mm-black | `200000049:366#1.0mm-black` | item `1005007722911159` · image `S7df4b1b76f334bc18045f1a84f6cb306I.jpg` | `P2` | **PRODUISIBLE** |
| 54 | `bracelet-presidentiel-904l` | NO.1 President | `200000049:201009050#NO.1 President` | item `1005006496083816` · image `S5ae8db338ff943e9b3949b7cfff428b6a.jpg` | `B3` | **BLOQUÉ** |
| 55 | `bracelet-presidentiel-904l` | NO.2 Jubilee | `200000049:201102690#NO.2 Jubilee` | item `1005006496083816` · image `Sb2beab33fc0a4aedb2e8b60bec597230Y.jpg` | `B3` | **BLOQUÉ** |
| 56 | `bracelet-presidentiel-904l` | NO.3 Polished Center | `200000049:201449057#NO.3 Polished Center` | item `1005006496083816` · image `S777fe4e01d5f49e0aa8bfc6a5b344166i.jpg` | `B3` | **BLOQUÉ** |
| 57 | `bracelet-presidentiel-904l` | NO.4 Brushed Center | `200000049:201449058#NO.4 Brushed Center` | item `1005006496083816` · image `Sea6fd5eaac0a4a86b95cec2046c8f143c.jpg` | `B3` | **BLOQUÉ** |
| 58 | `coffret-douze-aluminium` | 24 Slots | `14:175#24 Slots` | — | `U1` | **BLOQUÉ** |
| 59 | `coffret-douze-aluminium` | 6 Slots | `14:350850#6 Slots` | — | `U1` | **BLOQUÉ** |
| 60 | `coffret-douze-aluminium` | 12 Slots | `14:94#12 Slots` | — | `U1` | **BLOQUÉ** |
| 61 | `coussins-de-presentation-lot-de-10` | Red | `14:10` | item `1005003898684752` · image `Sdb07d664a23e4f2d88b036efe39ad842i.jpg` | `P7` | **PRODUISIBLE** |
| 62 | `coussins-de-presentation-lot-de-10` | Blue | `14:173` | item `1005003898684752` · image `Se086af4e4b3e4c0ab3711312fb4806d0T.jpg` | `P7` | **PRODUISIBLE** |
| 63 | `coussins-de-presentation-lot-de-10` | black | `14:193` | item `1005003898684752` · image `S8a81e375c4b247348f280a721e90f5bbY.jpg` | `P7` | **PRODUISIBLE** |
| 64 | `coussins-de-presentation-lot-de-10` | WHITE | `14:29` | item `1005003898684752` · image `S9a988198dc054c98815415b926d61e99D.jpg` | `P7` | **PRODUISIBLE** |
| 65 | `coussins-de-presentation-lot-de-10` | Brown | `14:365458` | item `1005003898684752` · image `S0dab8b645ba1460da1471c2c5cb3f7a3x.jpg` | `P7` | **PRODUISIBLE** |
| 66 | `doigtiers-d-horloger-latex` | white 50pcs | `14:173#white 50pcs` | item `1005008806614490` · image `Sa204a9bb577b419dba391c76b275e47el.jpg` | `B4` | **BLOQUÉ** |
| 67 | `doigtiers-d-horloger-latex` | black 50pcs | `14:175#black 50pcs` | item `1005008806614490` · image `S29b8c98951664b14ba40eec45948c21bP.jpg` | `B4` | **BLOQUÉ** |
| 68 | `doigtiers-d-horloger-latex` | white 30pcs | `14:193#white 30pcs` | item `1005008806614490` · image `S4ac4e7111890474dbe4c2897f599f013k.jpg` | `B4` | **BLOQUÉ** |
| 69 | `doigtiers-d-horloger-latex` | white 100pcs | `14:350686#white 100pcs` | item `1005008806614490` · image `S73e1bbbaf7de4357aea4c65347d466e8U.jpg` | `B4` | **BLOQUÉ** |
| 70 | `doigtiers-d-horloger-latex` | black 30pcs | `14:350850#black 30pcs` | item `1005008806614490` · image `S13560e8ec4d54586a93c6ac10ac5ffd2D.jpg` | `B4` | **BLOQUÉ** |
| 71 | `doigtiers-d-horloger-latex` | black 100pcs | `14:94#black 100pcs` | item `1005008806614490` · image `S6f7cad9d012f4af8a9d671c5cdc05d3fz.jpg` | `B4` | **BLOQUÉ** |
| 72 | `etui-de-voyage-rigide` | Black Brown 3 Slot | `14:1254#Black Brown 3 Slot` | item `1005011858146866` · image `S758584a3e22649ee9f7d9278f7971958l.jpg` | `B5` | **BLOQUÉ** |
| 73 | `etui-de-voyage-rigide` | Black Purple 6 Slot | `14:173#Black Purple 6 Slot` | item `1005011858146866` · image `S75ab7bf091104ff989386ad837182825o.jpg` | `P3` | **PRODUISIBLE** |
| 74 | `etui-de-voyage-rigide` | Purple 6 Slot | `14:193#Purple 6 Slot` | item `1005011858146866` · image `Sd5db52866e9544b9808ce109d3a2b490R.jpg` | `B5` | **BLOQUÉ** |
| 75 | `etui-de-voyage-rigide` | Gray Orange 6 Slot | `14:200000195#Gray Orange 6 Slot` | item `1005011858146866` · image `S88c60e7923814c46afc0be6abc0c7b2fZ.jpg` | `B5` | **BLOQUÉ** |
| 76 | `etui-de-voyage-rigide` | Black Green 6 Slot | `14:200006153#Black Green 6 Slot` | item `1005011858146866` · image `Sa900b00eddfe4505a0fb2606fa231be5a.jpg` | `P3` | **PRODUISIBLE** |
| 77 | `etui-de-voyage-rigide` | Black Brown 6 Slot | `14:200006154#Black Brown 6 Slot` | item `1005011858146866` · image `S21859cc161584c328ebdda7adfa67880x.jpg` | `B5` | **BLOQUÉ** |
| 78 | `etui-de-voyage-rigide` | Black Brown 2 Slot | `14:200660967#Black Brown 2 Slot` | item `1005011858146866` · image `S75051e547177459bae96af225b056b48a.jpg` | `B5` | **BLOQUÉ** |
| 79 | `etui-de-voyage-rigide` | Black Brown 1 Slot | `14:202114828#Black Brown 1 Slot` | item `1005011858146866` · image `S6636bef33adb496e9e94aaa87367f17fz.jpg` | `B5` | **BLOQUÉ** |
| 80 | `etui-de-voyage-rigide` | Blue 6 Slot | `14:801236284#Blue 6 Slot` | item `1005011858146866` · image `S1a376ef378124db1a37380e5793c557ef.jpg` | `B5` | **BLOQUÉ** |
| 81 | `loupe-d-horloger` | 10X-with circle | `14:10#10X-with circle` | item `1005009885282058` · image `S7f4e231db91f4ac4a21d8f67eaab66fa9.jpg` | `B6` | **BLOQUÉ** |
| 82 | `loupe-d-horloger` | 15X-with circle | `14:100013777#15X-with circle` | item `1005009885282058` · image `S2aa72540aaf14553b9b027d83aa6a4adW.jpg` | `B6` | **BLOQUÉ** |
| 83 | `loupe-d-horloger` | 3X-no circle | `14:173#3X-no circle` | item `1005009885282058` · image `S44f36b299fa44b9abc00e847466d13eew.jpg` | `B6` | **BLOQUÉ** |
| 84 | `loupe-d-horloger` | 15X-no circle | `14:175#15X-no circle` | item `1005009885282058` · image `Sd87b58126fad487e82df8b25c1c09b9b8.jpg` | `B6` | **BLOQUÉ** |
| 85 | `loupe-d-horloger` | 4PCS Set-no circle | `14:193#4PCS Set-no circle` | item `1005009885282058` · image `Sfaeefb9f87e94a1e8a2e3aea020e0bb62.jpg` | `B6` | **BLOQUÉ** |
| 86 | `loupe-d-horloger` | 3X-with circle | `14:29#3X-with circle` | item `1005009885282058` · image `S3dda5bd9752845bbadda0a80991ff38cW.jpg` | `B6` | **BLOQUÉ** |
| 87 | `loupe-d-horloger` | 5X-no circle | `14:350686#5X-no circle` | item `1005009885282058` · image `S7c27f5c89d1b486ca93be682b8383fdcy.jpg` | `B6` | **BLOQUÉ** |
| 88 | `loupe-d-horloger` | 10X-no circle | `14:350850#10X-no circle` | item `1005009885282058` · image `S0f19929fab5d4230819642bfeb53aaf9u.jpg` | `B6` | **BLOQUÉ** |
| 89 | `loupe-d-horloger` | 20X-with circle | `14:350853#20X-with circle` | item `1005009885282058` · image `Sc918302629b04299aa86703f6b3129b6X.jpg` | `B6` | **BLOQUÉ** |
| 90 | `loupe-d-horloger` | 4PCS Set-with circle | `14:366#4PCS Set-with circle` | item `1005009885282058` · image `S60ca8422671342fab8df63c5d2d8736dq.jpg` | `B6` | **BLOQUÉ** |
| 91 | `loupe-d-horloger` | 5X-with circle | `14:496#5X-with circle` | item `1005009885282058` · image `S01a189a6667741b8b036fe8c7cadebe8k.jpg` | `B6` | **BLOQUÉ** |
| 92 | `loupe-d-horloger` | circle-no magnifiers | `14:865#circle-no magnifiers` | item `1005009885282058` · image `Sb0efd420ec194e00acff555406dd99dfs.jpg` | `B6` | **BLOQUÉ** |
| 93 | `loupe-d-horloger` | 20X-no circle | `14:94#20X-no circle` | item `1005009885282058` · image `Se270fef3fb3e412daa89293e3c6d7410E.jpg` | `B6` | **BLOQUÉ** |
| 94 | `loupe-de-date-saphir` | B-4.5x3.5mm | `14:10#B-4.5x3.5mm` | item `1005011940440567` · image `S4a9741c538fd4b1b997aa56335058a3fO.jpg` | `B7` | **BLOQUÉ** |
| 95 | `loupe-de-date-saphir` | A-4.5x3.5mm | `14:173#A-4.5x3.5mm` | item `1005011940440567` · image `S4a9741c538fd4b1b997aa56335058a3fO.jpg` | `B7` | **BLOQUÉ** |
| 96 | `loupe-de-date-saphir` | A-7x5.5mm | `14:175#A-7x5.5mm` | item `1005011940440567` · image `S4a9741c538fd4b1b997aa56335058a3fO.jpg` | `B7` | **BLOQUÉ** |
| 97 | `loupe-de-date-saphir` | B-5.8x4.5mm | `14:29#B-5.8x4.5mm` | item `1005011940440567` · image `S4a9741c538fd4b1b997aa56335058a3fO.jpg` | `B7` | **BLOQUÉ** |
| 98 | `loupe-de-date-saphir` | A-5.5x4.5mm | `14:350686#A-5.5x4.5mm` | item `1005011940440567` · image `S4a9741c538fd4b1b997aa56335058a3fO.jpg` | `B7` | **BLOQUÉ** |
| 99 | `loupe-de-date-saphir` | A-5.8x4.5mm | `14:350850#A-5.8x4.5mm` | item `1005011940440567` · image `S4a9741c538fd4b1b997aa56335058a3fO.jpg` | `B7` | **BLOQUÉ** |
| 100 | `loupe-de-date-saphir` | B-5.5x4.5mm | `14:350853#B-5.5x4.5mm` | item `1005011940440567` · image `S4a9741c538fd4b1b997aa56335058a3fO.jpg` | `B7` | **BLOQUÉ** |
| 101 | `loupe-de-date-saphir` | B-7x5.5mm | `14:366#B-7x5.5mm` | item `1005011940440567` · image `S4a9741c538fd4b1b997aa56335058a3fO.jpg` | `B7` | **BLOQUÉ** |
| 102 | `outil-de-mise-a-taille-de-bracelet` | black | `14:193` | item `1005005877471703` · image `Se70cce7f352e439493d719fc2d2b24deI.jpg` | `P4` | **PRODUISIBLE** |
| 103 | `outil-de-mise-a-taille-de-bracelet` | Silver | `14:350853` | item `1005005877471703` · image `S85dd2bba33264c1fb4816474e7fb8553s.jpg` | `P4` | **PRODUISIBLE** |
| 104 | `pince-a-barrettes` | Silver | `14:173#Silver` | — | `U1` | **BLOQUÉ** |
| 105 | `pince-a-barrettes` | Black | `14:193#Black` | — | `U1` | **BLOQUÉ** |
| 106 | `pince-a-barrettes` | Black-Silver | `14:350686#Black-Silver` | — | `U1` | **BLOQUÉ** |
| 107 | `remontoir-bois-acajou` | M12032 | `14:94#M12032` | — | `A1` | **ABANDON** |
| 108 | `remontoir-bois-ebene` | M12052 | `14:865#M12052` | — | `A1` | **ABANDON** |
| 109 | `remontoir-bois-noir-laque` | M12011 | `14:175#M12011` | — | `A1` | **ABANDON** |
| 110 | `remontoir-bois-noyer` | M12071 | `14:100013777#M12071` | — | `A1` | **ABANDON** |
| 111 | `remontoir-collection-bois-beige` | IB-white-06A | `14:100013777#IB-white-06A` | item `1005006938556690` · image `S6ad5f4a9faf94c88885b275f03120424S.jpg` | `B8` | **BLOQUÉ** |
| 112 | `remontoir-collection-bois-beige` | IB-white-02A | `14:350850#IB-white-02A` | item `1005006938556690` · image `S49758bedf4314b0b82386efbea0a5919y.jpg` | `B8` | **BLOQUÉ** |
| 113 | `remontoir-collection-bois-beige` | IB-white-04A | `14:94#IB-white-04A` | item `1005006938556690` · image `S63c0d1dd69e040a19e0703ea67c1ded0Y.jpg` | `B8` | **BLOQUÉ** |
| 114 | `remontoir-collection-bois-led-noir` | IB-black-04C | `14:100005979#IB-black-04C` | item `1005006938556690` · image `Sdd13775b5837483b9ea80f7e36b49595y.jpg` | `B8` | **BLOQUÉ** |
| 115 | `remontoir-collection-bois-led-rouge` | IB-red-04C | `14:200000080#IB-red-04C` | item `1005006938556690` · image `S8f82a5a05d1b4a6294826c3362f3abe0u.jpg` | `B8` | **BLOQUÉ** |
| 116 | `remontoir-collection-bois-noir` | IB-black-04A | `14:175#IB-black-04A` | item `1005006938556690` · image `Se0cf06c264d04e7c95f3048f78557518J.jpg` | `B8` | **BLOQUÉ** |
| 117 | `remontoir-collection-bois-noir` | IB-black-02A | `14:350686#IB-black-02A` | item `1005006938556690` · image `S8e79a10b6500492eae8b090a98e2d5b4o.jpg` | `B8` | **BLOQUÉ** |
| 118 | `remontoir-collection-bois-noir` | IB-black-06A | `14:865#IB-black-06A` | item `1005006938556690` · image `Sd016edb263ca46c988f1bc44dd33897fJ.jpg` | `B8` | **BLOQUÉ** |
| 119 | `remontoir-collection-cuir-pu` | IB-PU leather-04B | `14:10#IB-PU leather-04B` | item `1005006938556690` · image `Sd34a1a3637854170b4016d869bb5efe4M.jpg` | `B8` | **BLOQUÉ** |
| 120 | `remontoir-collection-cuir-pu` | IB-PU leather-06B | `14:350853#IB-PU leather-06B` | item `1005006938556690` · image `S0d104dc2d7af4929bcf47b000800eaecX.jpg` | `B8` | **BLOQUÉ** |
| 121 | `remontoir-solo` | White | `14:173#White` | — | `U1` | **BLOQUÉ** |
| 122 | `remontoir-solo` | Green | `14:193#Green` | — | `U1` | **BLOQUÉ** |
| 123 | `rouleau-de-voyage-bleu-marine-cuir` | WB32 | `14:100013777#WB32` | item `1005008493748701` · image `S939dd20b74114f4e92f5dd120222e0921.jpg` | `B5` | **BLOQUÉ** |
| 124 | `rouleau-de-voyage-bleu-marine-cuir` | WB33 | `14:496#WB33` | item `1005008493748701` · image `S320d220ca5a44265b3f40168a09ede408.jpg` | `B5` | **BLOQUÉ** |
| 125 | `rouleau-de-voyage-brun-cuir` | WB22 | `14:175#WB22` | item `1005008493748701` · image `Sb4ba55c7bd4e434688049ecdff86976cA.jpg` | `B5` | **BLOQUÉ** |
| 126 | `rouleau-de-voyage-brun-cuir` | WB23 | `14:94#WB23` | item `1005008493748701` · image `S6142638338ce4e78abf7e0888663b6cce.jpg` | `B5` | **BLOQUÉ** |
| 127 | `rouleau-de-voyage-noir-cuir` | WB12 | `14:173#WB12` | item `1005008493748701` · image `Sb182758b6ce244c4a4a8246342036a46G.jpg` | `B5` | **BLOQUÉ** |
| 128 | `rouleau-de-voyage-noir-cuir` | WB13 | `14:350686#WB13` | item `1005008493748701` · image `Sd10223a0487b432dad14fb20395e021aj.jpg` | `P5` | **PRODUISIBLE** |
| 129 | `rouleau-de-voyage-vert-cuir` | WB43 | `14:29#WB43` | item `1005008493748701` · image `S2fd82c31c37947fd97e61cafeaa8b3635.jpg` | `B5` | **BLOQUÉ** |
| 130 | `rouleau-de-voyage-vert-cuir` | WB42 | `14:350853#WB42` | item `1005008493748701` · image `S30e7454221ae4b28a7623c7ac72a53e1X.jpg` | `B5` | **BLOQUÉ** |

## 6. Incertitudes et recommandations exactes

### À produire après création d'ordres séparée

Uniquement les 27 lignes `P1` à `P7`. Chaque ordre devra reprendre le fragment fournisseur exact et le fichier source correspondant. Pour les 27 résultats, la QA finale doit recontrôler la capacité, la maille ou géométrie, la couleur, l'absence de texte/logo dans la composition finale et l'absence de montre de décor marquée.

### À maintenir hors production

- Les 71 lignes disposant d'un item exact mais dont le blocage touche le produit ou empêche la fidélité restent BLOQUÉES. Ne pas effacer, flouter ou retoucher un marquage physique, une marque ou un verbatim du produit. Une annotation photographique hors produit ne peut être écartée que par nouvelle composition fidèle, jamais par altération du produit.
- Les 28 lignes `U1` restent BLOQUÉES tant que l'item exact n'est pas retrouvé et que sa matrice officielle ne prouve pas chaque valeur.
- Le candidat API `1005006468722763` pour la pince ne retourne qu'une seule variante noire `14:193`; il ne prouve ni qu'il s'agit de l'article d'origine, ni les finitions Argenté et Noir & argenté. Il est donc rejeté comme preuve.
- Pour le Remontoir Solo, le constat antérieur de `boutique-seiko-mod/AUDIT-9-GALERIES-RESTANTES-API-ALIEXPRESS-2026-08-10.md` reste applicable aux deux valeurs Vert/Blanc : source gravée et item exact absent.

### À abandonner dans cette file

Les quatre médias `M12032`, `M12052`, `M12011` et `M12071` des Remontoirs bois. Les visuels locaux montrent des boîtes passives à un emplacement ; les utiliser pour un remontoir motorisé à deux montres inventerait le produit. Re-sourcer la famille avant toute réouverture.

## 7. Actions explicitement non réalisées

- aucune génération d'image produit ;
- aucune création d'ordre ;
- aucune retouche ou suppression de marque ;
- aucune mutation Shopify ou DSers ;
- aucun achat, commande, publication ou activation ;
- aucun commit ni push.

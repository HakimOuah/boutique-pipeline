# Fournée visuels — les 94 fiches importées dans la nuit du 08 au 09/08

> **09/08/2026, à partir de 03 h 00.** Habillage maison des fiches poussées par DSers
> (`PUSH-DSERS-2026-08-09.md`, `TEXTES-ET-COLLECTIONS-2026-08-09.md`). Les 94 fiches sont en brouillon
> **avec les photos AliExpress brutes** : elles ne peuvent pas être activées tant qu'elles ne portent pas
> de visuels maison. Règle absolue de Hakim : on ne publie jamais une photo fournisseur brute.
>
> **Rien n'est rattaché sur Shopify par cette fournée.** Les livrables sont déposés dans
> `visuels-codex-2026-08/<handle>/` avec leur `manifeste.json` ; un autre agent surveille ce répertoire
> et fait le rattachement.

Ordre de priorité appliqué : **cadran arabe** → **cadrans pilote 1-12** → **cadrans stériles couleur**.
Une fiche par ordre. Document tenu au fil de l'eau.

---

## 1. Le matériau : 99 faces fournisseur, 37 fiches dans le périmètre

Les faces téléchargées cette nuit sont dans `boutique-seiko-mod/sources-fournisseur-2026-08/` (hors git,
`.gitignore` du dépôt). Contrôle fait avant tout usage :

- **99 dossiers, 99 fichiers, un par listing** (`face-fournisseur-<item_id>.jpg|png`), aucun dossier vide.
- **Le nom de dossier est le handle Shopify réel** — vérifié par requête sur les 37 fiches du périmètre
  (`tag:cadran-arabe`, `tag:cadran-pilote`, `tag:cadran-sterile`), les 37 handles correspondent au caractère près.
- 99 sources pour 94 fiches : les 5 en trop sont les **2 refus du push** (`montre-cadran-arabe-oriental-nh35`,
  `montre-field-titane-39-chiffres-arabes`), le **candidat conditionnel jamais mis en file**
  (`cadran-nh35-chiffres-arabes-orientaux-28-5`, item `1005009469054356`, texte « RLATIVE CHRONO » imprimé),
  et **deux cadrans arabes non importés** (`cadran-arabe-oriental-rose-28-5`,
  `cadran-arabe-oriental-sunburst-relief-28-5`) — ce sont précisément les deux références qui remonteraient
  la collection « Cadran arabe » à 10 produits (point 6 de la suite immédiate du rapport textes).

Périmètre prioritaire : **8 fiches cadran arabe + 14 cadrans pilote 1-12 + 15 cadrans stériles = 37 fiches.**
Le budget de la session (~5 h à 8-10 min par visuel) n'en couvre qu'une partie : c'est assumé, la priorité
prime la couverture.

---

## 2. Triage des sources — la règle « pas de marque » appliquée, et comment

La consigne est absolue : aucun logo, sigle, lettrage ni mention d'origine sur les cadrans ; et **si la
source elle-même porte une marque, on ne l'utilise pas et on signale la fiche**. À l'usage, les sources se
répartissent en quatre cas très différents, qui n'appellent pas la même décision. Le triage retenu :

| Cas | Décision | Justification |
|---|---|---|
| **A — marque imprimée SUR le produit** (nom de fournisseur sur le cadran) | **REJET + signalement** | Reproduire = imprimer une marque empruntée ; effacer = réinventer le produit. Aucune des deux n'est permise. |
| **B — mention générique gravée SUR le produit** (« Automatic », « Water Resistant », « 100m:330ft ») | **REJET + arbitrage Hakim** | Conflit frontal entre la règle 1 (produit repris tel quel) et la règle 2 (aucun lettrage). Ni l'un ni l'autre ne peut céder sans décision humaine. |
| **C — filigrane de vendeur ou annotation sur l'IMAGE, produit propre** | **UTILISÉ**, avec interdiction explicite dans l'ordre + contrôle au zoom en QA | Le filigrane n'est pas sur le produit. La DA recompose intégralement la scène : rien de la source ne survit. |
| **D — source propre** | **UTILISÉ** | — |

Le cas B est le seul point de doctrine que je ne tranche pas seul. Il concerne des fiches dont le texte
assume déjà la mention (`TEXTES-ET-COLLECTIONS-2026-08-09.md` : « les 3 fiches dont la face porte une
mention générique le disent dans "Avant de commander" »). Deux issues possibles, à choisir par Hakim :
sourcer la **variante stérile** du même listing (elle existe chez plusieurs de ces fournisseurs), ou
autoriser explicitement la mention générique dans le rendu.

### Fiches écartées de la production, avec motif vérifié

| Fiche (handle) | Cas | Motif |
|---|---|---|
| `montre-pilote-plongee-39-chiffres-arabes` | A | **« Tandorio » imprimé au cadran**, plus « 660ft=200m AUTOMATIC ». Le sélecteur fournisseur contient pourtant des variantes `logo dial` **et** stériles : la face téléchargée est la mauvaise. **À re-sourcer sur la variante stérile.** |
| `montre-cadran-arabe-oriental-36-39` | A | **« Tandorio » imprimé au cadran** turquoise, plus « Automatic ». Même remarque. |
| `cadran-arabe-oriental-sunburst-29` | A + B | Filigrane **MATELION** sur l'image **et** « Automatic » en cursive **sur les cinq cadrans**. |
| `cadran-arabe-oriental-argent-28-5` | B | « Automatic » en cursive imprimé sur les sept coloris de la planche. |
| `montre-sterile-40-nh35-saphir` | B | Cadran sans marque, mais « AUTOMATIC / WATER RESISTANT / 100m:330ft » imprimé. Source par ailleurs médiocre : montre portée au poignet, film de protection avec « 904L » en rouge, filigrane « TimeWatchCode ». |
| `insert-ceramique-chiffres-arabes-38` | — | **Écart produit, pas défaut de marque.** La fiche s'intitule « Insert de lunette céramique 38 mm à chiffres arabes orientaux » ; la source montre un **insert GMT à codes de villes** (LON, PAR, CAI, NYC, DXB…) et graduation 1-24. Aucun chiffre arabe oriental. **Soit la source est la mauvaise, soit le titre de la fiche est faux — à trancher avant toute production.** C'est aussi la fiche « pont » entre `lunettes-inserts` et `cadran-arabe`. |
| `cadran-pilote-sterile-28-5-sans-logo` | C aggravé | Filigrane « alpha dial » **large et centré, à cheval sur les cadrans** eux-mêmes. Les produits sont propres, mais la référence est trop dégradée pour servir de vérité produit fiable. Déprioritisé, non rejeté. |

**Conséquence sur la collection prioritaire : sur les 8 fiches « Cadran arabe », 5 sont bloquées et
2 seulement sont produites** (`cadran-arabe-oriental-noir-blanc-28-5`, `cadran-arabe-romain-emaille-bleu-28-5`).
La collection la plus recherchée du lot (`seiko arabic dial`, 8 100/mois) est donc **la moins couverte** —
c'est le point à corriger en premier, et c'est un problème de **sourcing**, pas de génération.

---

## 3. Doublons de fiches détectés au passage

Contrôle md5 sur les 99 sources — non demandé, mais il coûtait une commande et il a trouvé quelque chose.

**`cadran-pilote-29-classique-nh36` et `cadran-pilote-29-aiguilles-nh35` partagent une source
BYTE-IDENTIQUE** (`d99bc96a7a5d2643e8c5ae4abf6d5ed0`). C'est la confirmation empirique du doute laissé
ouvert au §4.2 du rapport textes (« deux item_id différents sur ce qui semble être le même listing
fournisseur […] cela reste une hypothèse. À vérifier, ou à fusionner »). **L'hypothèse est vérifiée : c'est
le même produit.** Les deux fiches ont été différenciées éditorialement (cadran seul / cadran + aiguilles)
mais la photo fournisseur est le même fichier.

Décision de production : **une seule des deux fiches est habillée** (`cadran-pilote-29-classique-nh36`).
Produire les deux reviendrait à poser des visuels maison quasi identiques sur deux fiches concurrentes —
du contenu dupliqué qu'on s'inflige à soi-même. **Fusion ou différenciation réelle : arbitrage Hakim.**

Grappe voisine, à l'œil et non au md5 : `cadran-retro-blanc-rose-nh35`, `cadran-retro-33-5-aiguilles-nh35`
et `cadran-plongee-33-5-aiguilles` montrent **les deux mêmes cadrans** (blanc à chiffres bleus, cuivré à
chiffres appliqués), sous trois prises de vue différentes et trois item_id différents. Une seule est
habillée pour la même raison ; les trois titres promettent pourtant des coloris différents (« blanc ou
rosé », « rétro 33,5 mm », « brun, blanc ou bleu »). **À vérifier au mapping des variantes.**

---

## 4. Ce qui a été demandé à Codex — et les trois correctifs de la fournée n°1

Les trois enseignements de `FOURNEE-VISUELS-1-2026-08-08.md` sont appliqués :

1. **Chaque slot décrit son cadrage explicitement**, pas seulement son nom. Le slot `macro` interdit
   nommément la vue de la pièce entière (le défaut exact du `-05-details.jpg` de la fournée 1) et impose le
   sujet : relief des chiffres appliqués, tranche polie, grain de finition, biseau du guichet de date.
2. **Nuance sur le poignet** : la question ne se pose pas ici et c'est délibéré. **Aucun slot `poignet`,
   aucune main, dans toute la fournée** — ces produits sont des **pièces détachées**, pas des montres. Un
   porté supposerait d'inventer le boîtier, le bracelet et le verre autour du cadran, c'est-à-dire
   d'inventer le produit. Le slot le plus coûteux de la fournée 1 (7 générations, slot perdu) est donc
   supprimé par construction, pas par prudence.
3. **Une fiche par ordre**, conformément à la troisième condition.

Trois slots, adaptés à une pièce détachée plutôt qu'à une montre :

| Slot | Fichier | Cadrage imposé |
|---|---|---|
| `face` | `<handle>-g1.jpg` | Pièce seule, à plat, strictement de dessus, centrée, ~80 % de la largeur, fond minéral, une ombre douce. Aucun accessoire. |
| `macro` | `<handle>-g2.jpg` | Lumière rasante sur **un secteur seulement** (quart 12 h-3 h), pièce débordant du cadre. Vue de la pièce entière **interdite**. |
| `situation` | `<handle>-g3.jpg` | Établi d'horloger sobre, plongée trois quarts, outils neutres et flous. Montre complète, boîtier, bracelet, main, marque : **interdits**. |

Contraintes ajoutées à celles du document 15, propres à ce lot :

- **Coloris de référence imposé et unique** par fiche. La plupart des sources sont des **planches de 4 à 9
  coloris** : l'ordre désigne explicitement lequel reproduire (par sa position dans la planche) et interdit
  les autres. Interdiction également de composer une planche multi-cadrans dans un livrable.
- **Identité produit décrite en toutes lettres** dans chaque ordre : diamètre, finition, graphie et relief
  des chiffres, présence ou absence de guichet de date, piste des minutes, aiguilles livrées ou non.
- **Pièges de comptage nommés** là où ils existent — le cadran pilote 38 mm n'a **pas** de chiffre 12 (un
  triangle et deux points) ni de 1 ni de 11 (des bâtons) ; les cadrans 33,5 mm portent **deux** séries de
  chiffres (1-12 grands, 13-24 petits) qui doivent rester appariées.
- **Filigranes et annotations d'image nommés et interdits** fiche par fiche (« Tandorio », « alpha dial »,
  « watchery Store », repères « #1 #2 #3 », cotes « 33.5mm » en rouge).
- Sortie 2048 × 2048, 1:1 strict, JPEG sRGB. **Suffixes `-6` et `-7` interdits** (ils désignaient les faux
  avis retirés le 08/08).

### Le champ `sku` des manifestes

Ces visuels sont des visuels de **galerie**, non rattachés à un coloris précis du sélecteur. Deviner un
fragment de SKU de variante serait une donnée inventée — interdit par le protocole, et c'est exactement ce
qui a fait écarter `bracelet-fkm-tropical` de la fournée 1. Le champ porte donc la **référence de listing
fournisseur `AE-<item_id>`** : stable, honnête, et ce n'est ni un ID de variante, ni de média, ni de produit
Shopify (les trois que le validateur refuse à juste titre). Le `manifeste.json` livré la reprend en
`sku_fournisseur`.

---

## 5. Production

_(section tenue au fil de l'eau)_

### Vague 1 — 5 ordres, 12 visuels demandés

| Fiche | Collection | Visuels demandés | Livrés par Codex | Retenus après QA |
|---|---|---:|---:|---:|
| `cadran-arabe-oriental-noir-blanc-28-5` | Cadran arabe | 3 | 3 | **2** |
| `cadran-arabe-romain-emaille-bleu-28-5` | Cadran arabe | 3 | 3 | **3** |
| `cadran-pilote-noir-33-5-nh35` | Cadrans pilote 1-12 | 2 | 2 | **2** |
| `cadran-pilote-29-classique-nh36` | Cadrans pilote 1-12 | 2 | 2 | **1** |
| `cadran-pilote-38-aiguilles-nh35` | Cadrans pilote 1-12 | 2 | 2 | **2** |
| **Total** | | **12** | **12** | **10** |

Les 5 ordres étaient **VALIDE (classe A)** au validateur avant transmission. La session s'est interrompue
après le cinquième résultat, avant le dépouillement : les cinq enveloppes étaient bien en `resultats/`,
`en-cours/` était vide, aucun ordre coincé. La reprise a donc porté sur la **QA** et non sur la génération.

### QA d'orchestrateur de la vague 1 — 2 visuels écartés sur 12

Codex a rendu `status: done` sur les cinq ordres, avec 7 rejets d'images qu'il avait lui-même détectés
(piste des minutes fausse, aiguilles masquant les chiffres, bâton manquant à 11 h, axe 12-6 incliné).
**Sa QA a néanmoins laissé passer deux défauts**, tous deux relevés au zoom contre la source :

| Visuel | Verdict | Motif |
|---|---|---|
| `cadran-arabe-oriental-noir-blanc-28-5-g3` (situation) | **écarté** | Piste des minutes : « 35 » imprimé deux fois, « 25 » absent. Défaut déjà relevé par la passe interrompue. |
| `cadran-pilote-29-classique-nh36-g1` (face) | **écarté** | **Chiffre « 1 » inventé au repère de 1 h.** La source porte à cet endroit un **bâton jaune nu**, et le macro `-g2` de la même fiche le rend correctement en bâton. Double faute : infidélité au produit **et** contradiction interne à la galerie. Cinquième rendu perdu sur cette fiche. |

Le second cas est un **type de défaut nouveau**, à ajouter aux ordres : le modèle **promeut un index en
chiffre**. Ce n'est ni une erreur de comptage (le nombre de repères est bon) ni une erreur de couleur — le
contrôle « chiffre par chiffre » ne l'attrape pas, il faut un contrôle **index par index sur la forme**.
La contrainte et le point de QA correspondants sont désormais dans le bloc de base des ordres, et
l'homogénéité de galerie devient un contrôle **bloquant** (une divergence de forme d'index entre deux
visuels d'une même fiche suffit à écarter).

Les 10 visuels retenus passent par ailleurs tous les contrôles : 2048 × 2048 JPEG sRGB, 580-880 Ko,
12 h en haut, aucun lettrage ni logo sur le cadran, aucun badge ni avis incrusté, aucun filigrane de
vendeur survivant (les sources `cadran-pilote-38-aiguilles-nh35` et `cadran-pilote-33-5-aiguilles-lumineuses`
portent pourtant le filigrane « Tandorio » — cas C, correctement absorbé par la recomposition).

Vérifications de fidélité les plus utiles, faites au zoom contre la source :

- `cadran-pilote-noir-33-5-nh35` : les **24 chiffres** sont présents et correctement appariés (13 sous 1,
  … 24 sous 12), piste bâtons + triangles conforme. Le piège de comptage annoncé au §4 est tenu.
- `cadran-pilote-38-aiguilles-nh35` : triangle + deux points à 12 h, **deux bâtons** à 11 h, un bâton à 1 h —
  la référence n'a pas de chiffre à ces trois positions et le rendu ne lui en invente pas.
- `cadran-arabe-oriental-noir-blanc-28-5` : la variante **noire** de la planche de quatre est bien la seule
  reproduite ; guichet de date à 3 h, piste 60/5/…/55 correcte sur `-g1` et `-g2`.

**Un doute résiduel, non bloquant, est consigné** sur `cadran-arabe-romain-emaille-bleu-28-5` : la source
(planche de neuf variantes, cadran de référence occupant ~330 px) montre **deux appliques rapprochées**
dans le secteur 4 h - 4 h 30, là où les rendus n'en portent qu'une (le `٤`). Mesure d'angles faite sur la
source : les douze positions horaires tombent bien à 30° d'intervalle et l'élément supplémentaire, à ~9°
du `٤`, ne correspond à aucune d'elles. Impossible de trancher entre une treizième applique et un reflet à
cette résolution — et **inventer un repère serait une donnée devinée**, interdite. Les trois visuels sont
donc conservés ; à re-vérifier sur une photo fournisseur de meilleure définition à l'étape DSers.

### Vague 2 — 5 ordres, 11 visuels demandés

Deux régénérations des slots écartés + trois fiches neuves, priorité tenue (cadran arabe d'abord).

| Fiche | Collection | Slots demandés | Nature |
|---|---|---|---|
| `cadran-arabe-oriental-noir-blanc-28-5` | Cadran arabe | `situation` | régénération QA |
| `cadran-pilote-29-classique-nh36` | Cadrans pilote 1-12 | `face` | régénération QA |
| `cadran-calligraphie-arabe-email-33` | Cadran arabe | `face` + `macro` + `situation` | nouvelle fiche |
| `cadran-pilote-29-mod-nh35` | Cadrans pilote 1-12 | `face` + `macro` + `situation` | nouvelle fiche |
| `cadran-pilote-33-5-aiguilles-lumineuses` | Cadrans pilote 1-12 | `face` + `macro` + `situation` | nouvelle fiche |

Les 5 ordres sont **VALIDE (classe A)** au validateur avant transmission.

Triage des trois sources neuves, fait avant de commander :

- `cadran-pilote-29-mod-nh35` — planche de 4 + vignettes. La variante **saumon porte « AUTOMATIC »**
  imprimé au cadran (cas B), mais la variante **noire à impressions blanches en est dépourvue** : c'est
  elle qui est désignée comme coloris unique de référence. Cas B contourné par le choix de variante, sans
  arbitrage nécessaire — méthode réutilisable pour les autres planches mixtes. Piège de comptage nommé :
  le guichet de date à 3 h remplace le chiffre 3 (onze grands chiffres, douze petits).
- `cadran-pilote-33-5-aiguilles-lumineuses` — planche de 4, filigrane « Tandorio » sur l'image (cas C),
  produits propres. Variante **bleu vif** désignée.
- `cadran-calligraphie-arabe-email-33` — **montage de quatre photos** dont deux hors sujet (un boîtier
  acier et un bracelet cuir qui n'appartiennent pas à la fiche) : l'ordre désigne le seul quadrant utile
  (cadran émail blanc à chiffres multicolores, haut à gauche) et interdit nommément les trois autres.

  ⚠️ **Point à trancher par Hakim, signalé et non bloquant** : la fiche s'intitule « calligraphie arabe »
  mais le cadran porte des **chiffres occidentaux 1 à 12** dans une graphie fantaisiste — aucune écriture
  arabe. C'est le titre du listing fournisseur qui parle d'« arabic artistic word ». À la différence de
  `insert-ceramique-chiffres-arabes-38` (où la source montrait un **tout autre produit**, un insert GMT à
  codes de villes), ici la source montre bien **le produit vendu** : les visuels sont donc justes, c'est
  le **titre de la fiche et son appartenance à la collection `cadran-arabe`** qui sont à revoir.

#### Résultats de la vague 2

| Fiche | Slots | Résultat | QA d'orchestrateur |
|---|---|---|---|
| `cadran-arabe-oriental-noir-blanc-28-5` | `situation` | livré (2 générations) | **retenu** — piste 60/5/…/55 désormais juste, homogène avec `-g1` et `-g2`. Fiche **complète à 3 visuels**. |
| `cadran-pilote-29-classique-nh36` | `face` | livré (**9 générations cumulées**) | **retenu** — le repère de 1 h est enfin un bâton nu, conforme à la source et au macro `-g2`. Fiche **complète à 2 visuels**. |
| `cadran-calligraphie-arabe-email-33` | `face`+`macro`+`situation` | livré (0 régénération) | **3 retenus** — douze chiffres, un de chaque, couleurs conformes position par position ; ni boîtier, ni bracelet, ni aiguille repris du montage source. |
| `cadran-pilote-29-mod-nh35` | 3 slots | **refusé par Codex** | refus **justifié** — voir ci-dessous. |
| `cadran-pilote-33-5-aiguilles-lumineuses` | 3 slots | interrompu (session tuée) | 4 rejets de placement d'aiguilles déjà consignés ; ordre **remis en file** automatiquement par le script, relancé en vague 3. |

`cadran-pilote-29-classique-nh36` est le sujet le plus coûteux des deux vagues : **neuf générations** pour
une seule image. Le modèle échoue systématiquement à poser trois aiguilles sans en faire toucher un
chiffre. Enseignement à réutiliser : sur un cadran livré avec aiguilles, **imposer dans l'ordre la position
horaire de chacune des trois aiguilles** dans un couloir vide nommé — ce qui a été fait dès la vague 2 et
qui a quand même demandé trois essais. À terme, il vaut peut-être mieux **demander la face sans aiguilles**
quand la source le permet.

#### Le refus de `cadran-pilote-29-mod-nh35` — l'ordre était fautif, pas la source

Codex a rendu `status: rejected` après quatre faces et deux macros écartées, avec ce motif :
la source montre des triangles pleins ailleurs qu'à 12 h, et ne porte pas de valeur périphérique « 15 ».
**Il avait raison, et c'est exactement le comportement attendu** : refuser plutôt que falsifier le produit
pour se conformer à un ordre erroné. Contrôle refait au zoom sur la source :

- l'anneau périphérique porte **douze triangles pleins**, un à chaque position de cinq minutes — celui de
  12 h est simplement **plus grand** que les onze autres ; entre eux, des rectangles blancs évidés ;
- les valeurs de cinq minutes réellement imprimées sont **dix** : 5, 10, 20, 25, 30, 35, 40, 45, 50, 55.
  **Pas de « 60 »** à 12 h (le grand triangle en tient lieu) et **pas de « 15 »** à 3 h (le guichet de date
  occupe le secteur). Le « 15 » que l'on voit à 3 h appartient à la couronne 24 h, pas à l'anneau ;
- trois repères d'heure sont des **bâtons** et non des chiffres : un bâton à 1 h, deux à 11 h, et le « 1 »
  de « 12 » comme celui de « 10 » sont eux aussi des bâtons.

Un ordre corrigé (`20260809-2245`) remplace le fautif. **La leçon est sur la méthode d'écriture des
ordres** : décrire une piste de cadran « au premier coup d'œil » sur une planche de quatre variantes ne
suffit pas — il faut un zoom sur la seule variante retenue avant d'écrire la contrainte, sinon l'ordre
devient un piège qui coûte six générations.

### Vague 3 — 3 ordres

| Fiche | Slots | Nature |
|---|---|---|
| `cadran-pilote-33-5-aiguilles-lumineuses` | 3 slots | reprise de l'ordre interrompu |
| `cadran-pilote-29-mod-nh35` | 3 slots | ordre corrigé après refus justifié |
| `cadran-pilote-33-5-aiguilles-blanches` | `face`+`macro` | nouvelle fiche |

Les 3 ordres sont **VALIDE (classe A)** au validateur. Triage de la source neuve
(`cadran-pilote-33-5-aiguilles-blanches`) : deux cadrans et un couvercle plastique sur la même photo,
filigrane « Tandorio » sur l'image (cas C) — le cadran de gauche (chiffres blancs, chevron blanc) est
désigné, celui de droite (chevron rouge) et le couvercle sont interdits.

#### Résultats de la vague 3 — arrêtée en cours, proprement

`cadran-pilote-33-5-aiguilles-lumineuses` a livré **`face` et `macro`, tous deux retenus** en QA :
douze grands chiffres et douze petits 13-24 correctement appariés, bâtons conservés à 1 h et 11 h (et pour
le « 1 » de « 12 » et de « 10 »), piste 60/5/…/55 avec ses points lumineux, aucune trace du filigrane
« Tandorio ». Contrôle au zoom des deux zones à risque : **aucune aiguille ne touche de chiffre** — quatre
rendus avaient pourtant été écartés par Codex sur ce seul point.

Le slot `situation` de cette fiche n'a pas eu le temps d'être produit. **La session s'arrête ici, et elle
s'arrête en refusant de laisser sortir du non-contrôlé** : l'exécutant a été arrêté avant qu'il n'attaque
les deux ordres suivants, plutôt que de laisser des visuels non passés en QA arriver dans
`visuels-codex-2026-08/`, où un autre agent les rattacherait sans contrôle. Compte tenu du taux de défaut
observé aujourd'hui — **2 visuels écartés sur 12 en vague 1, plus un ordre entier fautif** — livrer sans QA
serait pire que ne pas livrer.

État de la boîte à la remise : `en-cours/` **vide**, aucun verrou, **3 ordres VALIDE (classe A) en file**
dans `inbox/`, prêts à repartir d'un simple `bash ordres/generer-images.sh` :

| Ordre en file | Slots | Remarque |
|---|---|---|
| `20260809-2315-…-cadran-pilote-33-5-aiguilles-lumineuses` | `situation` seul | réécrit pour ne PAS régénérer les deux visuels déjà validés |
| `20260809-2245-…-cadran-pilote-29-mod-nh35` | 3 slots | version corrigée après le refus justifié |
| `20260809-2245-…-cadran-pilote-33-5-aiguilles-blanches` | `face`+`macro` | nouvelle fiche, source triée |

---

## 6. Où en est la fournée

**19 visuels maison retenus après QA, sur 6 fiches**, dont **4 fiches complètes**.

| Fiche | Collection | Visuels retenus | État |
|---|---|---:|---|
| `cadran-arabe-oriental-noir-blanc-28-5` | Cadran arabe | 3 | complète |
| `cadran-arabe-romain-emaille-bleu-28-5` | Cadran arabe | 3 | complète (un doute résiduel consigné) |
| `cadran-calligraphie-arabe-email-33` | Cadran arabe | 3 | complète (titre de fiche à arbitrer) |
| `cadran-pilote-noir-33-5-nh35` | Cadrans pilote 1-12 | 2 | complète |
| `cadran-pilote-38-aiguilles-nh35` | Cadrans pilote 1-12 | 2 | complète |
| `cadran-pilote-29-classique-nh36` | Cadrans pilote 1-12 | 2 | complète |
| `cadran-pilote-33-5-aiguilles-lumineuses` | Cadrans pilote 1-12 | 2 | `situation` en file |
| `cadran-pilote-29-mod-nh35` | Cadrans pilote 1-12 | 0 | ordre corrigé en file |
| `cadran-pilote-33-5-aiguilles-blanches` | Cadrans pilote 1-12 | 0 | ordre en file |

La collection **Cadran arabe** passe de 0 à **3 fiches habillées sur 8** : c'est le maximum atteignable
sans re-sourcing, les 5 autres restant bloquées par une marque au cadran ou un écart produit (§2).
La collection **Cadrans pilote 1-12** compte **4 fiches habillées**. La collection **Cadrans stériles
couleur** n'a pas été entamée : la priorité annoncée a été tenue jusqu'au bout.

### Ce qu'il faut retenir pour la prochaine session

1. **La QA de Codex ne suffit pas.** Sur 12 visuels rendus `done` en vague 1, **2 portaient un défaut**
   (piste des minutes fausse, chiffre inventé à la place d'un bâton). Le contrôle indépendant au zoom
   contre la source n'est pas une formalité, c'est là que les défauts se trouvent.
2. **Un index n'est pas un chiffre.** Nouveau type de défaut, désormais dans le bloc de contraintes de
   base et dans la QA : le modèle promeut spontanément un bâton en « 1 ». Ces cadrans aviateur en sont
   pleins (1 h, 11 h, et le « 1 » de « 12 » et de « 10 »).
3. **Écrire l'ordre après un zoom, pas après un coup d'œil.** L'ordre `cadran-pilote-29-mod-nh35` décrivait
   faussement la piste périphérique et a coûté six générations avant que Codex ne le refuse — à raison.
4. **Les aiguilles sont le poste le plus cher.** 9 générations pour une face sur `pilote-29-classique`,
   4 rejets sur `pilote-33-5-lumineuses`, tous pour cause d'aiguille touchant un chiffre. Imposer la
   position horaire des trois aiguilles aide mais ne suffit pas ; envisager de demander la face **sans
   aiguilles** quand la source le permet.
5. **Choisir la bonne variante désamorce le cas B.** Sur `pilote-29-mod`, seule la variante saumon portait
   « AUTOMATIC » : désigner la variante noire a rendu la fiche productible sans arbitrage. À tenter sur les
   autres fiches bloquées en cas B avant de les remonter à Hakim.

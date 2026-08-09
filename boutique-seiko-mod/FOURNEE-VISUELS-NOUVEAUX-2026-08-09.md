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

| Fiche | Collection | Visuels demandés | État |
|---|---|---:|---|
| `cadran-arabe-oriental-noir-blanc-28-5` | Cadran arabe | 3 | en cours |
| `cadran-arabe-romain-emaille-bleu-28-5` | Cadran arabe | 3 | en file |
| `cadran-pilote-noir-33-5-nh35` | Cadrans pilote 1-12 | 2 | en file |
| `cadran-pilote-29-classique-nh36` | Cadrans pilote 1-12 | 2 | en file |
| `cadran-pilote-38-aiguilles-nh35` | Cadrans pilote 1-12 | 2 | en file |

Les 5 ordres sont **VALIDE (classe A)** au validateur avant transmission.

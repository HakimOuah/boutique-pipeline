# Rattachement des visuels Codex — Maison Noirmont — 09/08/2026

Contrôle QA puis rattachement Shopify des visuels livrés par Codex dans
`visuels-codex-2026-08/`. Journal tenu au fil de l'eau.

## Règles appliquées

- Chaque image est **ouverte et regardée** avant tout rattachement.
- Refus si : marque / sigle / lettrage / mention d'origine sur le cadran ; avis, note,
  étoile, badge ou chiffre incrusté ; bracelet représenté ≠ bracelet réellement vendu par
  la fiche ; source manifeste introuvable ; hors 2048×2048 JPEG.
- Rattachement par `productCreateMedia` — **toujours en fin de galerie**, jamais en
  position 1 (le suffixe `-gN` est une numérotation de livraison, pas une position).
- `alt` descriptif en français posé sur chaque média.
- Aucun média existant supprimé. Aucun prix, statut, texte ou variante modifié.
  Aucun brouillon activé.

---

## Tour 1 — 09/08/2026 ~00h00

### Rattachés (10 visuels sur 6 fiches)

| Fiche | Fichiers | Position | Alt posé |
|---|---|---|---|
| `integrale-vert-sport-chic-acier` | `-g1` situation 3/4 | 2/5 | Intégrale Vert — montre à cadran vert texturé et bracelet acier intégré, posée de trois quarts sur fond clair — Maison Noirmont |
| | `-g2` macro cadran | 3/5 | Intégrale Vert — macro du cadran vert texturé, index appliqués et guichet de date, lunette acier vissée — Maison Noirmont |
| | `-g3` au poignet | 4/5 | Intégrale Vert — montre portée au poignet, cadran vert et bracelet acier intégré — Maison Noirmont |
| | `-g4` détail maille | 5/5 | Intégrale Vert — détail de la maille du bracelet acier brossé et de ses maillons centraux — Maison Noirmont |
| `rouleau-de-voyage-vert-cuir` | `-g1` situation 1 alvéole | 2/3 | Rouleau de Voyage Vert — rouleau en cuir vert ouvert, une montre logée dans son alvéole doublée — Maison Noirmont |
| | `-g2` macro cuir + couture | 3/3 | Rouleau de Voyage Vert — macro du cuir vert grainé et de la couture de la sangle de fermeture — Maison Noirmont |
| `contre-la-montre-argent-chronographe` | `-g1` macro caoutchouc noir | 5/5 | Contre-la-montre Argent — détail du bracelet caoutchouc noir à deux rainures et de sa jonction à la corne acier — Maison Noirmont |
| `contre-la-montre-bleu-glacier-chronographe` | `-g1` macro acier 3 maillons | 5/5 | Contre-la-montre Bleu glacier — détail du bracelet acier trois maillons à la jonction du boîtier — Maison Noirmont |
| `contre-la-montre-compteurs-bleus-chronographe` | `-g1` macro caoutchouc bleu marine | 5/5 | Contre-la-montre Compteurs bleus — détail du bracelet caoutchouc bleu marine et de sa jonction au boîtier acier — Maison Noirmont |
| `contre-la-montre-gris-anthracite-chronographe` | `-g1` macro acier 3 maillons | 5/5 | Contre-la-montre Gris anthracite — détail oblique du bracelet acier trois maillons et de son articulation à la boîte — Maison Noirmont |

### Point de contrôle n°3 — fidélité du bracelet (le plus délicat de la fournée)

Chaque macro de bracelet a été confrontée au texte de la fiche Shopify :

| Fiche | Ce que la fiche vend | Ce que la macro montre | Verdict |
|---|---|---|---|
| Argent | « bracelet caoutchouc noir » (option : *Argent · caoutchouc noir*) | caoutchouc noir à deux rainures + corne acier | conforme |
| Bleu glacier | « Sur bracelet acier » | acier trois maillons | conforme |
| Compteurs bleus | « bracelet caoutchouc bleu marine » (option : *Compteurs bleus · bracelet bleu*) | caoutchouc bleu marine | conforme |
| Gris anthracite | « sur bracelet acier » | acier trois maillons | conforme |

Aucune inversion : le doute soulevé au briefing (macro acier sur Bleu glacier, macro
caoutchouc sur Compteurs bleus) est levé — ce sont bien les bracelets vendus par ces
deux fiches.

### Autres contrôles du tour 1

- Cadrans : les 4 vues Intégrale et la montre-accessoire du Rouleau montrent un cadran
  **stérile** — aucun logo, sigle, lettrage ni mention d'origine. Les 4 macros
  chronographe ne cadrent pas le cadran.
- Aucun avis, note, étoile, badge ni chiffre de satisfaction incrusté.
- Sources manifeste : les 6 fichiers `visuels-2026-07-25/generated/*.jpg` cités existent
  tous et sont cohérents avec le sujet livré.
- Technique : 10/10 en 2048×2048 JPEG.
- Ordre de galerie vérifié après coup : l'image 1 d'origine est restée en place sur les
  6 fiches, les nouveaux médias sont bien en queue. Statuts inchangés (ACTIVE).

### Non rattachés — dossiers vides assumés par Codex

| Fiche | Motif consigné au manifeste |
|---|---|
| `bracelet-fkm-tropical` | pas de source propre complète : l'unique face locale est un gros plan partiel avec marquage central masqué et embossage douteux |
| `carte-cadeau-maison-noirmont` | pas de source propre locale ; les 4 variantes ont un SKU fournisseur `null` |
| `trente-neuf-rose-classique-cannelee` | source locale interdite : la seule face disponible porte la mention d'origine **SWISS MADE** à 6 h |

Rien à rattacher pour ces trois fiches — écarts justifiés, aucune action.

---

## Tour 2 — 09/08/2026 ~00h10

Quatre nouveaux dossiers livrés pendant le tour 1.

### Rattachés (4 visuels sur 4 fiches)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `contre-la-montre-rose-poudre-chronographe` | `-g1` macro acier 3 maillons | 5/5 | Contre-la-montre Rose poudré — macro du bracelet acier trois maillons et de son grain brossé — Maison Noirmont |
| `heritage-bleu-plongeuse-vintage-42` | `-g1` macro lunette bleue | 5/5 | Héritage Bleu — macro oblique de la lunette bleue, de son repère triangulaire doré et de sa denture acier — Maison Noirmont |
| `heritage-bleu-nuit-plongeuse-vintage-42` | `-g1` profil couronne + lunette noire | 5/5 | Héritage Bleu nuit — profil rapproché de la couronne stérile, du flanc acier brossé et de la lunette noire crantée — Maison Noirmont |
| `montre-acier-chiffres-3-6-9-explorateur` | `-g1` macro bracelet acier | 5/5 | Explorateur — macro du bracelet acier trois maillons, maillons centraux polis et côtés brossés — Maison Noirmont |

### Contrôles du tour 2

- **Fidélité produit** : Rose poudré « sur bracelet acier » → macro acier, conforme.
  Explorateur « bracelet acier trois maillons » → macro acier trois maillons, conforme.
  Héritage Bleu « lunette bleue » → lunette bleue, conforme. Héritage Bleu nuit
  « lunette noire » → lunette noire, conforme.
- **Cadran / couronne** : aucun logo, sigle ni lettrage. Point de vigilance levé sur
  l'Explorateur — la fiche indique que le cadran réel porte la mention « Professional
  Automatic », mais la macro livrée ne cadre que le bracelet : aucun texte à l'image.
  La couronne de l'Héritage Bleu nuit est bien lisse et vierge. Aucune mention
  d'origine nulle part.
- **Avis / badges** : aucun.
- **Sources** : `chrono-rose-poudre.jpg`, `heritage-bleu-lunette-bleue.jpg`,
  `heritage-bleu-nuit-lunette-noire.jpg` et
  `visuels-arabes-squelettes-2026-07-29/…-explorateur-face.jpg` existent tous.
- **Technique** : 4/4 en 2048×2048 JPEG.
- Ajout en fin de galerie, image 1 intacte, statuts ACTIVE inchangés.

**Cumul : 14 visuels rattachés sur 10 fiches. 0 refus.**

---

## Tour 3 — 09/08/2026 ~00h15

### Rattachés (2 visuels sur 2 fiches)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `heritage-vert-plongeuse-vintage-42` | `-g1` macro bracelet acier | 5/5 | Héritage Vert — macro oblique du bracelet acier trois maillons entièrement brossé et de sa courbure — Maison Noirmont |
| `integrale-blanc-argente-sport-chic-acier` | `-g1` macro vis de lunette | 5/5 | Intégrale Blanc argenté — macro oblique de deux vis de lunette et de l'alternance brossé/poli du boîtier octogonal — Maison Noirmont |

### Contrôles du tour 3

- **Fidélité produit** : la fiche Héritage Vert ne décrit pas son bracelet en texte ;
  contrôle fait sur la source `heritage-vert-lunette-verte.jpg`, qui montre bien un
  bracelet acier trois maillons — la macro correspond. Intégrale Blanc argenté : boîtier
  octogonal à vis apparentes, identique à la construction de l'Intégrale, et la tranche
  de cadran visible est bien claire (blanc argenté).
- Aucun logo, lettrage ni mention d'origine ; aucun avis ni badge ; sources présentes ;
  2/2 en 2048×2048 JPEG ; ajout en fin de galerie, image 1 intacte, statuts inchangés.

**Cumul : 16 visuels rattachés sur 12 fiches. 0 refus.**

---

## Tour 4 — 09/08/2026 ~00h20

### Rattachés (2 visuels sur 2 fiches)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `integrale-bleu-ciel-sport-chic-acier` | `-g1` macro bracelet intégré | 5/5 | Intégrale Bleu ciel — macro du bracelet intégré acier : larges plaques brossées, deux connecteurs par articulation et chants polis — Maison Noirmont |
| `integrale-bleu-nuit-sport-chic-acier` | `-g1` profil couronne + flanc | 5/5 | Intégrale Bleu nuit — profil rapproché de la couronne géométrique stérile, du flanc acier brossé et du chanfrein poli — Maison Noirmont |

### Contrôles du tour 4

- **Fidélité produit** : les deux fiches vendent un « bracelet intégré en acier, finition
  brossée » ; la macro Bleu ciel montre bien un bracelet intégré (plaques larges, deux
  connecteurs par articulation), pas un trois-maillons rapporté. Le profil Bleu nuit
  montre une tranche de cadran bleu sombre, conforme au coloris vendu.
- Couronne géométrique **vierge** sur le Bleu nuit : aucun logo, sigle ni lettrage.
  Aucun avis ni badge. Sources présentes. 2/2 en 2048×2048 JPEG.
- Ajout en fin de galerie, image 1 intacte, statuts ACTIVE inchangés.

**Cumul : 18 visuels rattachés sur 14 fiches. 0 refus.**

---

## Tour 5 — 09/08/2026 ~00h25

### Rattachés (2 visuels sur 2 fiches)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `integrale-brun-or-rose-sport-chic` | `-g1` macro bracelet intégré or rose | 5/5 | Intégrale Brun or rose — macro du bracelet intégré or rose : plaques satinées, deux connecteurs par articulation et chants polis — Maison Noirmont |
| `integrale-noir-sport-chic-acier` | `-g1` macro jonction boîtier-bracelet | 5/5 | Intégrale Noir — macro de la jonction boîtier-bracelet : vis de lunette, chanfrein poli et deux connecteurs intégrés, tranche de cadran noir texturé — Maison Noirmont |

### Contrôles du tour 5

- **Fidélité produit** : la fiche Brun or rose vend un « boîtier or rose · bracelet
  intégré » — la macro est bien or rose (pas acier), point de vigilance principal ici.
  La fiche Noir vend un « cadran noir texturé » et un bracelet intégré acier : la macro
  montre la tranche du cadran noir texturé et le bracelet intégré acier, conforme.
- Aucun logo, lettrage ni mention d'origine ; aucun avis ni badge ; sources présentes ;
  2/2 en 2048×2048 JPEG ; ajout en fin de galerie, image 1 intacte, statuts inchangés.

**Cumul : 20 visuels rattachés sur 16 fiches. 0 refus.**

---

## Tour 6 — 09/08/2026 ~00h30

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `integrale-turquoise-sport-chic-acier` | `-g1` vue basse bracelet intégré | 5/5 | Intégrale Turquoise — vue basse du bracelet intégré acier en courbe : épaisseur des plaques brossées, connecteurs et chants polis — Maison Noirmont |

Fiche : « Boîtier et bracelet intégré en acier, finition brossée » → macro de bracelet
intégré acier, conforme. Aucun logo, avis ni badge. Source
`integrale-turquoise.jpg` présente. 2048×2048 JPEG. Fin de galerie, image 1 intacte.

**Cumul : 21 visuels rattachés sur 17 fiches. 0 refus.**

---

## Tour 7 — 09/08/2026 ~00h30 — **2 refus**

Deux dossiers livrés : `noirmont-un-plongeuse-acier` et `noirmont-un-bronze-plongeuse`.
**Aucun des deux n'est rattaché.** Premiers refus de la campagne.

### Motif 1 — les handles du manifeste n'existent pas sur la boutique

`productByHandle` renvoie `null` pour `noirmont-un-plongeuse-acier` **et** pour
`noirmont-un-bronze-plongeuse`. Ce ne sont pas des handles produit : ce sont les **noms
des fichiers image hérités** hébergés sur le CDN (`noirmont-un-plongeuse-acier-face.jpg`…).

Les deux fiches réellement concernées sont :

| Handle réel | Titre | Statut |
|---|---|---|
| `montre-aviateur-acier-cadran-chiffres-1-12` | Noirmont Un — Aviateur acier à chiffres 1-12 | ACTIVE |
| `montre-aviateur-bronze-cadran-chiffres-1-12` | Noirmont Un Bronze — Aviateur bronze à chiffres 1-12 | ACTIVE |

### Motif 2 — écart de fidélité produit (critère 3), rédhibitoire

Les deux fiches vendent, noir sur blanc dans leur description :

- « Le bracelet est en cuir brun, surpiqué clair » / « Bracelet cuir brun, surpiqûre claire »
- « lunette **lisse, sans graduation** »
- cadran noir à chiffres 1-12 en couronne intérieure, 5-55 en couronne extérieure

Les visuels livrés sont des macros de **bracelet acier trois maillons** (et, pour le bronze,
cornes bronze + bracelet acier). Rattacher reviendrait à afficher en galerie un bracelet que
la fiche ne vend pas. Refus.

### Motif 3 — source citée introuvable (critère 4)

Le manifeste cite `scratchpad/noirmont-galeries/entrees-faces/<handle>-face.jpg`. Ce chemin
n'existe nulle part dans le repo. L'équivalent local est
`entrees-faces-REDONDANT-export-claude/` — et ce fichier montre **une plongeuse à lunette
graduée sur bracelet acier**, avec des **zones de flou sur le cadran à 12 h et à 6 h**
(emplacements typiques d'un logo et d'un lettrage masqués). Lignée de source douteuse.

### L'inversion de Codex

Le manifeste acier écarte `visuels-aviateur-2026-07-27/generated/noirmont-un-plongeuse-acier-face.jpg`
au motif « nom trompeur : montre aviateur sur cuir, différente de la plongeuse acier active ».
**C'est l'inverse.** Ce fichier écarté est le bon produit : boîtier acier, bracelet cuir brun
surpiqué clair, lunette lisse, cadran 1-12 / 5-55 stérile — conforme mot pour mot au titre et
à la description de la fiche ACTIVE. Codex a pris le nom de fichier hérité pour un handle et a
généré la macro d'une montre que la boutique ne vend pas.

### ⚠️ À remonter à Hakim — anomalie préexistante sur deux fiches ACTIVE

Indépendamment de cette livraison : les **4 images actuellement en ligne** sur
`montre-aviateur-acier-cadran-chiffres-1-12` et `montre-aviateur-bronze-cadran-chiffres-1-12`
montrent une **plongeuse** (lunette graduée 10-20-30-40-50, aiguilles snowflake, bracelet acier)
alors que le titre, la description et les options vendent un **aviateur à chiffres sur cuir brun**.
Les deux fiches sont **ACTIVE** : ce que voit l'acheteur ne correspond pas à ce qui est décrit.

Aucune correction faite ici — le mandat interdit de supprimer un média ou de toucher au texte.
Décision à prendre par Hakim : soit régénérer les galeries à partir des sources aviateur
(`visuels-aviateur-2026-07-27/generated/`), soit réécrire les fiches pour vendre la plongeuse.

**Cumul inchangé : 21 visuels rattachés sur 17 fiches. 2 refus.**

---

## Tour 8 — 09/08/2026 ~00h35

Trois dossiers `quarante-et-un-*` livrés pendant le tour 7. **Handles valides cette fois** —
les trois existent bien sur la boutique et sont ACTIVE.

### Rattachés (3 visuels sur 3 fiches)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `quarante-et-un-blanc-cuir-sport-acier` | `-g1` macro corne + cuir | 5/5 | Quarante-et-Un Blanc — macro de la jonction entre la corne acier brossée et le bracelet cuir brun foncé grainé, surpiqûre ton sur ton, tranche de cadran blanc visible — Maison Noirmont |
| `quarante-et-un-bleu-acier-sport-acier` | `-g1` macro jonction boîte-bracelet | 5/5 | Quarante-et-Un Bleu Acier — macro de la jonction boîtier-bracelet : premiers maillons acier étagés brossés et polis, cadran bleu roi soleillé à index dorés en haut de cadre — Maison Noirmont |
| `quarante-et-un-bleu-cuir-sport-acier` | `-g1` macro corne + cuir surpiqûres beige | 5/5 | Quarante-et-Un Bleu — macro de la jonction entre la corne acier brossée et le bracelet cuir brun foncé à surpiqûres beige, tranche de cadran bleu roi visible — Maison Noirmont |

### Contrôles du tour 8

- **Fidélité produit — le point sensible de cette fournée, les trois fiches partagent le
  même boîtier et ne se distinguent que par cadran + bracelet.** Vérifié un à un :

| Fiche | Ce que la fiche vend | Ce que la macro montre | Verdict |
|---|---|---|---|
| Blanc | « Cadran blanc et bracelet cuir brun foncé » | fragment de cadran **blanc** + cuir brun foncé, surpiqûre **ton sur ton** | conforme |
| Bleu Acier | « Cadran bleu roi soleillé · bracelet acier brossé et poli » | cadran **bleu soleillé** à index dorés + maillons **acier** étagés | conforme |
| Bleu (cuir) | « Cadran bleu roi et bracelet cuir brun foncé » | fragment de cadran **bleu** + cuir brun foncé, surpiqûres **beige** | conforme |

  Aucune inversion cadran/bracelet entre les trois. Codex a même distingué correctement la
  couleur des surpiqûres — brun ton sur ton sur le Blanc, beige sur le Bleu cuir — conforme
  aux planches QA des quatre vues existantes.
- **Cadran** : un fragment périphérique est visible sur les trois (indices appliqués, piste
  des minutes). **Aucun logo, sigle, lettrage ni mention d'origine** — cadrans stériles,
  guichet de date sans texte. Vigilance plongeuse sans objet : aucune de ces trois n'a de
  lunette graduée.
- **Avis / badges** : aucun.
- **Sources** : le manifeste cite à nouveau `scratchpad/noirmont-galeries/entrees-faces/…`,
  chemin qui n'existe pas dans le repo. Contrôle de substitution fait sur les planches QA,
  qui montrent les quatre vues en ligne de chaque fiche — le sujet livré correspond.
  *Point de forme à corriger côté Codex : citer un chemin versionné, pas un scratchpad.*
- **Technique** : 3/3 en 2048×2048 JPEG.
- Ajout en fin de galerie (5/5), image 1 intacte, statuts ACTIVE inchangés, aucun média
  supprimé, aucun texte ni prix ni variante touché.

**Cumul : 24 visuels rattachés sur 20 fiches. 2 refus.**

---

## Tour 9 — 09/08/2026 ~00h40

Deux dossiers `quarante-et-un-noir-*` livrés pendant le tour 8. Handles valides, fiches ACTIVE.

### Rattachés (2 visuels sur 2 fiches)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `quarante-et-un-noir-acier-sport-acier` | `-g1` profil droit + couronne + 1er maillon | 5/5 | Quarante-et-Un Noir Acier — macro du profil droit : couronne cannelée lisse, lunette polie, cadran noir à index appliqués et jonction au premier maillon du bracelet acier — Maison Noirmont |
| `quarante-et-un-noir-cuir-sport-acier` | `-g1` profil droit + couronne + corne | 5/5 | Quarante-et-Un Noir — macro du profil droit : couronne cannelée non protégée, corne acier brossée à vis, cadran noir et amorce du bracelet cuir brun foncé — Maison Noirmont |

### Contrôles du tour 9

- **Fidélité produit** — les deux fiches partagent le cadran noir et ne diffèrent que par le
  bracelet, c'est le seul point qui pouvait déraper :

| Fiche | Ce que la fiche vend | Ce que la macro montre | Verdict |
|---|---|---|---|
| Noir Acier | « Cadran noir et bracelet acier » | cadran noir + premier maillon **acier** en bas de cadre | conforme |
| Noir (cuir) | « Cadran noir et bracelet cuir brun foncé » | cadran noir + amorce de **cuir brun foncé** sous la corne | conforme |

  Pas d'inversion entre les deux.
- **Couronne — point de vigilance principal de cette fournée**, les deux visuels la cadrent
  en gros plan. Couronne **cannelée à sommet plat entièrement vierge** dans les deux cas :
  aucun logo, sigle, blason ni lettrage gravé. Aucune mention d'origine.
- **Cadran** : fragment visible sur les deux, index appliqués et piste des minutes, **aucun
  texte**. Cadrans stériles.
- **Avis / badges** : aucun.
- **Sources** : même remarque de forme qu'au tour 8 — chemin `scratchpad/…` non versionné.
  Contrôle de substitution fait sur les planches QA.
- **Technique** : 2/2 en 2048×2048 JPEG.
- Ajout en fin de galerie (5/5), image 1 intacte, statuts ACTIVE inchangés.

**Cumul : 26 visuels rattachés sur 22 fiches. 2 refus.**

---

## Tour 10 — 09/08/2026 ~00h45

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `quarante-et-un-noir-jaune-acier-sport-acier` | `-g1` macro angle bas jonction boîte-bracelet | 5/5 | Quarante-et-Un Noir & Jaune Acier — macro en angle bas de la jonction boîtier-bracelet : maillons acier brossés et polis, cadran noir à index cernés de jaune en haut de cadre — Maison Noirmont |

La fiche vend « Cadran noir avec des accents jaunes — tirets de la graduation, trotteuse,
contours des index — sur bracelet acier ». Le fragment de cadran visible montre bien les
index **cernés de jaune** et les tirets jaunes de la graduation, sur **bracelet acier**
brossé et poli : conforme, et bien distinct de la variante Noir Acier traitée au tour 9.

Aucun logo, sigle ni lettrage ; aucun avis ni badge ; 2048×2048 JPEG ; ajout en fin de
galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 27 visuels rattachés sur 23 fiches. 2 refus.**

---

## Tour 11 — 09/08/2026 ~00h50

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `montre-squelette-automatique-carree` | `-g1` macro transition boîtier-bracelet | 5/5 | Squelette Carré — macro de la transition entre le boîtier acier brossé à flancs chanfreinés et les quatre premiers maillons du bracelet intégré à maillons centraux polis — Maison Noirmont |

### Contrôles du tour 11

- **Fidélité produit** : la fiche vend « 42 mm d'acier brossé, quatre vis apparentes » et,
  sur ses quatre vues en ligne, un **bracelet intégré acier à maillons centraux polis**.
  La macro montre exactement cette construction — boîtier carré à angles adoucis, flancs
  chanfreinés, quatre maillons intégrés. Conforme.
- **Cadran hors champ** : le cadran squelette et sa minuterie chiffrée ne sont pas cadrés.
  Aucun logo, sigle ni lettrage. La fiche précise d'ailleurs que les deux versions sont
  « sans logo ni inscription ». Macro neutre vis-à-vis des deux variantes (squelette blanc
  et squelette noir) puisqu'aucun cadran n'apparaît.
- **Avis / badges** : aucun.
- **Source — corrigée côté Codex** : le manifeste cite cette fois un chemin **versionné**,
  `boutique-seiko-mod/visuels-arabes-squelettes-2026-07-29/montre-squelette-automatique-carree-face.jpg`,
  et le fichier existe bien (627 ko, 29/07). C'est la bonne pratique, à généraliser.
- **Technique** : 2048×2048 JPEG. Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 28 visuels rattachés sur 24 fiches. 2 refus.**

---

## Tour 12 — 09/08/2026 ~00h55

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `montre-squelette-automatique-octogone` | `-g1` macro transition boîtier-bracelet | 5/5 | Squelette Octogone — macro de la transition entre le boîtier octogonal acier brossé et les quatre premiers maillons du bracelet intégré, chants polis et articulations apparentes — Maison Noirmont |

La fiche vend « Boîtier acier à lunette octogonale vissée, **bracelet acier dans le dessin du
boîtier** » : la macro montre bien un bracelet intégré acier prolongeant la géométrie
octogonale, identique aux quatre vues en ligne. Conforme, et bien distincte de la macro
Squelette Carré du tour 11 — les deux constructions de maillons diffèrent.

Cadran et couronne hors champ, aucun logo ni lettrage (la fiche précise « sans logo ni
inscription »), aucun avis ni badge. Source versionnée présente
(`visuels-arabes-squelettes-2026-07-29/…-octogone-face.jpg`). 2048×2048 JPEG.
Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 29 visuels rattachés sur 25 fiches. 2 refus.**

---

## Tour 13 — 09/08/2026 ~01h00

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `trente-neuf-bleu-mer-classique-cannelee` | `-g1` macro lunette cannelée + jubilé | 5/5 | Trente-Neuf Bleu mer — macro de la jonction boîtier-bracelet : stries polies de la lunette cannelée et maillons du bracelet jubilé acier à cinq rangs — Maison Noirmont |

### Contrôles du tour 13

- **Fidélité produit** : la fiche vend une « lunette cannelée — ces stries taillées tout
  autour du verre » et un « bracelet **jubilé à cinq rangs** ». La macro montre les deux :
  les stries polies de la lunette en haut de cadre, et un jubilé cinq rangs (deux rangs
  brossés extérieurs, trois rangs polis centraux) — pas un oyster trois maillons.
  Identique au bracelet des quatre vues en ligne. Conforme.
- **Cadran, date et loupe entièrement hors champ** — point important sur cette famille :
  la fiche sœur `trente-neuf-rose-classique-cannelee` avait été écartée au tour 1 parce que
  sa seule face disponible portait la mention d'origine **SWISS MADE** à 6 h. Ici le cadrage
  exclut totalement le cadran, donc **aucune mention d'origine possible à l'image**. Le
  risque de la famille est neutralisé par le cadrage, pas contourné.
- Aucun logo, sigle ni lettrage ; aucun avis ni badge ; 2048×2048 JPEG.
- Source : chemin `scratchpad/…` non versionné (même remarque de forme qu'aux tours 8-9) ;
  contrôle de substitution fait sur la planche QA.
- Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 30 visuels rattachés sur 26 fiches. 2 refus.**

---

## Tour 14 — 09/08/2026 ~01h05

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `trente-neuf-noir-classique-cannelee` | `-g1` macro latérale lunette + couronne | 5/5 | Trente-Neuf Noir — macro latérale : stries polies de la lunette cannelée, couronne cannelée à sommet lisse, flanc acier brossé et jonction au bracelet jubilé — Maison Noirmont |

### Contrôles du tour 14

- **Fidélité produit** : « cadran noir brillant », « lunette cannelée », « bracelet jubilé à
  cinq rangs ». La macro montre les stries de la lunette en gros plan, le bracelet jubilé
  acier à gauche, et la tranche du cadran **noir** en haut de cadre. Conforme.
- **Couronne — cadrée en gros plan, contrôle serré** : cannelure régulière et **sommet plat
  entièrement lisse**, aucun logo, blason, sigle ni gravure. C'est le point de risque
  principal de ce cadrage, il est propre.
- **Cadran, date et loupe hors champ** : seule la tranche noire apparaît, aucun texte
  lisible. Le risque « SWISS MADE » de la famille Trente-Neuf (cf. refus tour 1 sur la
  version Rose) ne se présente pas ici.
- Aucun avis ni badge ; 2048×2048 JPEG.
- Codex signale 1 rejet interne (premier cadrage montrant à tort un disque gris brossé à la
  place du cadran noir) — le fichier livré est bien la version corrigée, cadran noir.
- Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 31 visuels rattachés sur 27 fiches. 2 refus.**

---

## Tour 15 — 09/08/2026 ~01h10

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `trente-neuf-duo-dore-classique-bicolore` | `-g1` macro jubilé bicolore + lunette dorée | 5/5 | Trente-Neuf Duo Doré — macro du bracelet jubilé bicolore : maillons centraux or jaune entre deux rangs d'acier brossé, et stries dorées de la lunette cannelée — Maison Noirmont |

### Contrôles du tour 15

- **Fidélité produit — la bicolore est le cas le plus exigeant de la famille Trente-Neuf.**
  La fiche décrit précisément la répartition des finitions : « La finition or jaune couvre
  la lunette cannelée, la couronne, **les maillons centraux du jubilé** […] ; **les maillons
  extérieurs restent en acier brossé** ». La macro montre exactement cette répartition —
  trois rangs centraux or jaune encadrés de deux rangs d'acier brossé, et une lunette
  cannelée **dorée**, pas acier. Conforme dans le détail.
- **Cadran hors champ** : seul un liseré clair apparaît en haut de cadre, hors mise au point.
  Aucun texte, aucun chiffre, aucune mention d'origine.
- Aucun avis ni badge ; 2048×2048 JPEG.
- Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 32 visuels rattachés sur 28 fiches. 2 refus.**

---

## Tour 16 — 09/08/2026 ~01h15

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `trente-six-rouge-classique-jubile` | `-g1` profil rapproché couronne + jubilé | 5/5 | Trente-Six Rouge — profil rapproché : boîtier acier fin, couronne cannelée à sommet lisse, tranche de cadran rouge cramoisi sous le verre et première articulation du bracelet jubilé — Maison Noirmont |

### Contrôles du tour 16

- **Fidélité produit** : « cadran rouge cramoisi », « le boîtier et le bracelet jubilé
  restent en **acier** ». La tranche de cadran visible sous le verre est bien **rouge sombre**
  (pas bordeaux, pas rose), le boîtier et le bracelet sont en acier, et l'articulation
  visible à gauche est celle d'un jubilé. Conforme.
- **Couronne cadrée en gros plan** : cannelure fine, **sommet parfaitement lisse** — aucun
  logo, blason ni gravure.
- **Cadran et date hors champ** : aucun texte, aucune mention d'origine.
- Aucun avis ni badge ; 2048×2048 JPEG.
- Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 33 visuels rattachés sur 29 fiches. 2 refus.**

---

## Tour 17 — 09/08/2026 ~01h20

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `trente-six-bleu-classique-jubile` | `-g1` macro jonction + jubilé acier | 5/5 | Trente-Six Bleu — macro de la jonction boîtier-bracelet : jubilé acier à cinq rangs, deux rangs larges brossés encadrant trois rangs centraux polis — Maison Noirmont |

- **Fidélité** : la fiche décrit le jubilé au détail près — « deux rangs larges et brossés de
  part et d'autre de trois rangs centraux polis ». La macro montre exactement ce comptage
  et cette alternance de finitions, en acier. Conforme.
- Cadran et date entièrement hors champ : aucun texte ni mention d'origine. Le visuel est
  neutre vis-à-vis du coloris, donc sans risque de contradiction avec le bleu roi vendu.
- Aucun logo, aucun avis, aucun badge ; 2048×2048 JPEG.
- Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 34 visuels rattachés sur 30 fiches. 2 refus.**

---

## Tour 18 — 09/08/2026 ~01h25

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `trente-six-rose-classique-jubile` | `-g1` profil gauche boîtier + jubilé | 5/5 | Trente-Six Rose — profil gauche : boîtier acier fin à flanc poli, corne à barrette vissée et départ du bracelet jubilé acier à cinq rangs — Maison Noirmont |

- **Fidélité** : boîtier acier fin et bracelet jubilé acier, conformes à la fiche. Cadran,
  date et couronne entièrement hors champ — aucun texte, aucune mention d'origine.
- **Autocorrection Codex à souligner** : le compte-rendu signale un premier cadrage rejeté
  parce qu'il « laissait apparaître un grand fragment de cadran rose **vidé de ses index** ».
  C'est exactement le type de défaut à ne pas laisser passer, et il a été écarté en amont.
  Le fichier livré ne montre plus aucun cadran.
- Aucun logo, aucun avis, aucun badge ; 2048×2048 JPEG.
- Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 35 visuels rattachés sur 31 fiches. 2 refus.**

---

## Tour 19 — 09/08/2026 ~01h30

Dossier trouvé **incomplet** au premier scan (image présente, `manifeste.json` et
`compte-rendu.md` absents — écriture en cours côté Codex). Traitement différé jusqu'à
finalisation du dossier plutôt que traité en l'état.

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `trente-six-dore-classique-jubile` | `-g1` macro frontale jonction + jubilé | 5/5 | Trente-Six Doré — macro frontale de la jonction boîtier-bracelet : cadran champagne soleillé à index acier en haut de cadre, boîtier et jubilé cinq rangs en acier — Maison Noirmont |

### Contrôles du tour 19

- **Fidélité produit — le piège de cette fiche est explicite dans son texte** : « Le cadran
  doré champagne apporte la chaleur de l'or **sans passer le boîtier à l'or : boîtier et
  bracelet jubilé restent en acier** ». Un visuel qui aurait doré le boîtier ou les maillons
  aurait été refusé. Le fichier livré montre bien un **cadran champagne** avec **boîtier et
  jubilé en acier** — la répartition est juste, et bien distincte du Duo Doré bicolore
  traité au tour 15.
- **Cadran** : fragment étroit visible, index appliqués acier, **aucun texte**, pas de date,
  aucune mention d'origine.
- Aucun logo, aucun avis, aucun badge ; 2048×2048 JPEG.
- Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 36 visuels rattachés sur 32 fiches. 2 refus.**

---

## Tour 20 — 09/08/2026 ~01h35

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `trente-six-or-integral-classique-jubile` | `-g1` macro jonction + jubilé or | 5/5 | Trente-Six Or intégral — macro de la jonction boîtier-bracelet : boîtier, jubilé cinq rangs et cadran dans la même teinte or jaune, relief donné par l'alternance satiné-poli des maillons — Maison Noirmont |

### Les trois « dorées » de la boutique sont désormais correctement différenciées

C'est le point de vigilance de cette série : trois fiches voisines, trois répartitions
or/acier différentes, et un risque réel d'interversion. Contrôle croisé :

| Fiche | Répartition vendue | Ce que montre la macro | Tour |
|---|---|---|---|
| `trente-six-dore-classique-jubile` | cadran doré, **boîtier et bracelet acier** | cadran champagne + acier | 19 |
| `trente-neuf-duo-dore-classique-bicolore` | **bicolore** : lunette/couronne/maillons centraux or, maillons extérieurs acier | jubilé or au centre, acier aux bords | 15 |
| `trente-six-or-integral-classique-jubile` | **tout or** : boîtier, bracelet et cadran | monochrome or intégral | 20 |

Les trois visuels sont bien distincts et chacun correspond à sa fiche. Aucune interversion.

- Cadran hors champ hormis un fragment doré sans texte ; aucun logo, aucun avis, aucun badge ;
  2048×2048 JPEG ; fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 37 visuels rattachés sur 33 fiches. 2 refus.**

---

## Tour 21 — 09/08/2026 ~01h40

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `voyageur-or-gmt-3-maillons` | `-g1` macro contre-plongée bracelet 3 maillons | 5/5 | Voyageur Or — macro en contre-plongée du bracelet trois maillons doré et de sa jonction au boîtier, crantage du flanc de lunette visible — Maison Noirmont |

### Contrôles du tour 21 — première GMT de la campagne, vigilance lunette

- **Risque spécifique** : une GMT porte une **lunette graduée 24 h**, donc des chiffres.
  C'est précisément le cas de figure signalé au briefing (graduation de lunette avec chiffres
  fantaisistes ou marque). Ici le cadrage est en **contre-plongée** : seul le **crantage du
  flanc** de la lunette apparaît, la face graduée bicolore brun/noir est entièrement hors
  champ. **Aucun chiffre, aucun texte, aucune mention d'origine à l'image.** Le risque est
  évité par le cadrage, pas masqué.
- **Fidélité produit** : « Doré du boîtier au bracelet **trois maillons** ». La macro montre
  bien un trois maillons (pas un jubilé cinq rangs comme les Trente-Six), entièrement doré,
  boîtier compris. Conforme.
- **Cadran hors champ** : la fiche précise « Cadran sans logo ni inscription de marque » —
  point sans objet ici, aucun cadran n'est cadré.
- Aucun avis ni badge ; 2048×2048 JPEG.
- Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 38 visuels rattachés sur 34 fiches. 2 refus.**

---

## Tour 22 — 09/08/2026 ~01h45

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `voyageur-or-gmt-president` | `-g1` macro frontale bracelet Président | 5/5 | Voyageur Or — macro frontale du bracelet Président doré : maillons courts et arrondis à trois éléments par rangée, jonction au boîtier et crantage de lunette — Maison Noirmont |

### Contrôles du tour 22 — les deux Voyageur Or ne diffèrent que par le bracelet

C'est le seul critère qui sépare cette fiche de celle du tour 21 : même boîtier doré, même
lunette bicolore, même mouvement. Une interversion de macro serait invisible au manifeste
mais fausse en boutique. Contrôle croisé :

| Fiche | Bracelet vendu | Ce que montre la macro | Tour |
|---|---|---|---|
| `voyageur-or-gmt-3-maillons` | trois maillons, rangs larges | rangs larges et plats | 21 |
| `voyageur-or-gmt-president` | **Président, maillons courts et arrondis** | rangées à trois éléments **courts et bombés**, colonne centrale étroite | 22 |

Les deux géométries sont nettement différentes à l'image. Aucune interversion.
Codex signale d'ailleurs avoir **écarté une première génération** dont « le maillon central
était trop large et trop plat » — c'est-à-dire une macro qui aurait ressemblé au 3 maillons.
Le bon réflexe.

- **Lunette** : vue en contre-plongée, seul le crantage et le bord perlé apparaissent —
  **aucun chiffre de la graduation 24 h, aucun texte**. Cadran, date et marqueurs hors champ.
- Aucun logo, aucun avis, aucun badge ; 2048×2048 JPEG.
- Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

**Cumul : 39 visuels rattachés sur 35 fiches. 2 refus.**

---

## Tour 23 — 09/08/2026 ~01h50

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `voyageur-bicolore-gmt-3-maillons` | `-g1` macro bracelet 3 maillons bicolore | 5/5 | Voyageur Bicolore — macro du bracelet trois maillons bicolore : rangée centrale dorée entre deux rangs d'acier brossé, lunette et couronne dorées sur boîtier acier — Maison Noirmont |

### Contrôles du tour 23

- **Fidélité produit** : « Boîtier bicolore, acier et doré, sur un bracelet trois maillons
  dont **la rangée centrale reprend le ton doré** ». La macro montre exactement cela —
  rangée centrale dorée, deux rangs extérieurs acier brossé, boîtier acier, lunette et
  couronne dorées. Conforme, et bien distincte des deux Voyageur **Or** intégral des tours
  21 et 22.
- **Lunette** : cadrée de face cette fois. Elle porte des **pastilles rondes lumineuses**
  et un crantage, mais **aucun chiffre de graduation, aucun texte, aucune mention d'origine**.
  Contrôle GMT passé.
- Cadran hors champ hormis un fragment noir sans texte. Aucun avis ni badge. 2048×2048 JPEG.
- Fin de galerie (5/5), image 1 intacte, statut ACTIVE inchangé.

### ⚠️ À remonter à Hakim — description contredite par les visuels (3 fiches Voyageur)

Les trois fiches Voyageur annoncent une « **lunette bicolore brun et noir** » (ou « lunette
brun et noir ») :

- `voyageur-or-gmt-3-maillons`
- `voyageur-or-gmt-president`
- `voyageur-bicolore-gmt-3-maillons`

Or **les quatre vues déjà en ligne** sur chacune de ces fiches montrent une **lunette
entièrement dorée à pastilles claires** — aucune trace de brun ni de noir sur la lunette.
Le texte décrit un insert que le produit photographié n'a pas.

Ce n'est **pas** un défaut du visuel livré ce soir : la macro est cohérente avec les quatre
vues existantes. L'écart est dans le texte des fiches, et il préexiste à cette campagne.
Aucune correction faite — le mandat interdit de toucher au texte. Décision à prendre par
Hakim : corriger la description des trois fiches, ou vérifier auprès du fournisseur quelle
lunette est réellement livrée.

**Cumul : 40 visuels rattachés sur 36 fiches. 2 refus.**

---

## Tour 24 — 09/08/2026 ~01h55

### Rattachés (2 visuels sur 2 fiches)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `voyageur-bicolore-gmt-5-maillons` | `-g1` macro 5 maillons bicolore | 5/5 | Voyageur Bicolore — macro du bracelet cinq maillons bicolore : trois rangs centraux dorés entre deux rangs larges d'acier brossé, lunette dorée sur boîtier acier — Maison Noirmont |
| `voyageur-or-rose-gmt-5-maillons` | `-g1` macro 5 maillons or rose | 5/5 | Voyageur Or rose — macro du bracelet cinq maillons entièrement or rose : deux rangs extérieurs larges satinés, trois rangs centraux étroits polis, boîtier et lunette dans le même ton — Maison Noirmont |

### Contrôles du tour 24

- **Or rose** : « Or rose du boîtier au bracelet cinq maillons » → la macro est intégralement
  **or rose** (teinte cuivrée, nettement distincte de l'or jaune des tours 21-23), boîtier et
  lunette compris. Conforme sans réserve. La géométrie cinq maillons est également distincte
  des trois maillons du tour 21 et du Président du tour 22 : les quatre Voyageur traités ce
  soir sont tous différenciés à l'image.
- **Bicolore 5 maillons** : géométrie conforme (trois rangs centraux étroits entre deux rangs
  larges), acier aux bords, boîtier acier — mais voir la réserve ci-dessous sur la teinte.
- **Lunettes** : pastilles rondes et crantage, **aucun chiffre de graduation 24 h, aucun
  texte, aucune mention d'origine**. Cadrans hors champ.
- Aucun avis ni badge ; 2/2 en 2048×2048 JPEG ; fin de galerie (5/5), image 1 intacte,
  statuts ACTIVE inchangés.

### ⚠️ Deuxième anomalie de description — `voyageur-bicolore-gmt-5-maillons`

La fiche annonce « **Acier et or rose** se répondent sur le boîtier comme sur le bracelet ».
Or les **quatre vues déjà en ligne** montrent sans ambiguïté de l'**or jaune**, pas de l'or
rose — et la comparaison est immédiate avec la vraie or rose traitée dans le même tour, dont
la teinte cuivrée n'a rien à voir.

Comme pour la lunette (tour 23), **le visuel livré n'est pas en cause** : il reproduit
fidèlement l'or jaune des quatre vues existantes. C'est la description qui est fausse, et
elle l'était avant cette campagne.

Récapitulatif des écarts de texte constatés sur la famille Voyageur, tous préexistants :

| Fiche | Ce que dit le texte | Ce que montrent les visuels en ligne |
|---|---|---|
| `voyageur-or-gmt-3-maillons` | lunette bicolore brun et noir | lunette dorée à pastilles |
| `voyageur-or-gmt-president` | lunette bicolore brun et noir | lunette dorée à pastilles |
| `voyageur-bicolore-gmt-3-maillons` | lunette brun et noir | lunette dorée à pastilles |
| `voyageur-bicolore-gmt-5-maillons` | lunette brun et noir + **acier et or rose** | lunette dorée + **or jaune** |
| `voyageur-or-rose-gmt-5-maillons` | lunette brun et noir | lunette or rose |

Aucun texte modifié — hors mandat. À arbitrer par Hakim : corriger les descriptions, ou
vérifier la référence réellement livrée par le fournisseur.

**Cumul : 42 visuels rattachés sur 38 fiches. 2 refus.**

---

## Tour 25 — 09/08/2026 ~02h00

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `voyageur-bicolore-cadran-brun-gmt` | `-g1` profil lunette + couronne + bracelet | 5/5 | Voyageur Bicolore cadran brun — profil rapproché : lunette dorée crantée, protège-couronne acier, couronne dorée à sommet lisse et bracelet cinq maillons bicolore — Maison Noirmont |

### Contrôles du tour 25

- **Fidélité produit** : « Boîtier bicolore acier et doré, bracelet cinq maillons ». La macro
  montre la boîte acier, la lunette et la couronne dorées, les protège-couronne acier et un
  bracelet cinq maillons bicolore. Conforme.
- **Couronne cadrée en très gros plan** : sommet **parfaitement lisse et vierge**, aucun logo,
  blason ni gravure. Point de risque principal du cadrage, il est propre.
- **Cadran entièrement exclu** — et c'est ici le résultat de deux autocorrections successives
  de Codex, toutes deux pertinentes :
  1. une première génération rejetée parce que « des marqueurs de minutes restaient visibles » ;
  2. une seconde rejetée parce qu'elle « inventait une grande ouverture de cadran vide ».
  Le fichier livré ne montre aucun cadran, donc ni marqueur inventé ni texte.
- **Lunette** : crantage vu de profil, **aucun chiffre de graduation 24 h**.
- Aucun avis ni badge ; 2048×2048 JPEG ; fin de galerie (5/5), image 1 intacte, statut ACTIVE
  inchangé.

**Cumul : 43 visuels rattachés sur 39 fiches. 2 refus.**

---

## Tour 26 — 09/08/2026 ~02h05

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `montre-field-acier-cadran-chiffres-1-12` | `-g1` macro cornes acier + cuir | 5/5 | Éclaireur Acier — macro de la jonction entre les cornes acier brossé et le bracelet cuir brun châtaigne à surpiqûres crème — Maison Noirmont |

- **Fidélité** : « boîtier acier brossé et bracelet cuir surpiqué » → cornes en acier brossé,
  cuir brun châtaigne, surpiqûres crème apparentes. Conforme.
- **Cadran entièrement exclu** : la fiche annonce « douze grands chiffres luminescents,
  de 1 à 12, piste des 24 heures en couronne intérieure ». Aucun de ces chiffres n'apparaît
  à l'image — donc aucun risque de graduation fantaisiste ni de texte. La fiche précise par
  ailleurs retenir « les versions stériles : aucun logo, aucune inscription ».
- **Source versionnée** et présente : `visuels-arabes-squelettes-2026-07-29/montre-field-acier-cadran-chiffres-arabes-face.jpg` (548 ko, 29/07).
- Aucun avis ni badge ; 2048×2048 JPEG ; fin de galerie (5/5), image 1 intacte, statut ACTIVE
  inchangé.

**Cumul : 44 visuels rattachés sur 40 fiches. 2 refus.**

---

## Tour 27 — 09/08/2026 ~02h10

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `montre-field-bronze-cadran-chiffres-1-12` | `-g1` macro cornes bronze + cuir caramel | 5/5 | Éclaireur Bronze — macro de la jonction entre les cornes bronze à finition vieillie mouchetée et le bracelet cuir caramel texturé à surpiqûres brunes — Maison Noirmont |

### Contrôles du tour 27

- **Point de vigilance soulevé par le compte-rendu** : Codex décrit une « patine sombre
  irrégulière », alors que la fiche vend un « boîtier en acier traité **PVD bronze** — la
  teinte chaude du bronze, **sans sa patine imprévisible** ». Contrôle fait sur les quatre
  vues déjà en ligne : elles montrent **déjà** ce même aspect bronze vieilli moucheté, sur
  le boîtier comme sur les cornes. La macro livrée est donc **cohérente avec le produit
  photographié** ; la formule de la fiche porte sur le fait que la teinte **n'évoluera pas**
  dans le temps (contrairement au bronze massif), pas sur l'absence d'aspect vieilli.
  Aucune contradiction introduite par ce visuel. Alt rédigé en « finition vieillie »
  plutôt qu'en « patine » pour rester aligné sur le texte de la fiche.
- **Distinction avec l'Éclaireur Acier (tour 26)** : cornes bronze vs cornes acier brossé,
  cuir caramel très texturé vs cuir châtaigne lisse, surpiqûres brunes vs surpiqûres crème.
  Les deux visuels ne sont pas interchangeables. Aucune interversion.
- **Cadran entièrement exclu** : ni les douze chiffres, ni la piste 24 h, ni les repères
  orange n'apparaissent. Aucun texte, aucune mention d'origine.
- Codex signale avoir écarté une première génération qui « ajoutait une surface circulaire
  bronze ambiguë au-dessus des cornes » — élément inventé, bien rejeté.
- Source versionnée présente ; aucun avis ni badge ; 2048×2048 JPEG ; fin de galerie (5/5),
  image 1 intacte, statut ACTIVE inchangé.

**Cumul : 45 visuels rattachés sur 41 fiches. 2 refus.**

---

## Tour 28 — 09/08/2026 ~02h15 — dossier vide assumé

| Fiche | Livré | Motif consigné au manifeste |
|---|---|---|
| `remontoir-solo` | 0 visuel | source locale interdite : la seule face disponible porte un **lettrage de marque gravé sur la façade** ; aucune autre source propre dans le lot validé |

Rien à rattacher — écart justifié, aucune action. C'est le bon arbitrage : la règle interdit
aussi bien d'utiliser une source marquée que de gommer localement le marquage, et Codex n'a
pas cherché à contourner. La fiche reste à 2 médias.

**Cumul inchangé : 45 visuels rattachés sur 41 fiches. 2 refus.**

---

## Tour 29 — 09/08/2026 ~02h20

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `remontoir-vitrine` | `-g1` macro angle de cadre | 3/3 | Remontoir Vitrine — macro de l'angle du cadre : montant en bois brun rouge, tranche du verre et doublure intérieure taupe — Maison Noirmont |

- **Premier accessoire (non-montre) de la campagne** : les critères cadran/lunette sont sans
  objet, le contrôle porte sur la fidélité matière et l'absence d'élément inventé.
- **Fidélité** : cadre bois brun rouge, tranche de verre clair, doublure intérieure taupe —
  conformes aux deux vues en ligne. Aucun mécanisme, aucun accessoire, aucune montre ajoutée.
- Codex signale avoir écarté une première génération qui « ajoutait une **plaque en laiton
  absente de la source** ». Élément inventé, bien rejeté — c'est le même travers que la
  surface circulaire de l'Éclaireur Bronze (tour 27), et il est attrapé à chaque fois.
- **Aucun lettrage, aucune marque** sur le cadre — contrairement au Remontoir Solo du tour 28,
  dont la source portait un lettrage gravé et qui est resté sans livraison.
- Aucun avis ni badge ; 2048×2048 JPEG ; cette fiche n'ayant que 2 médias, le nouveau se
  place en 3/3, image 1 intacte, statut ACTIVE inchangé.

**Cumul : 46 visuels rattachés sur 42 fiches. 2 refus.**

---

## Tour 30 — 09/08/2026 ~02h25

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `coffret-douze-aluminium` | `-g1` macro angle aluminium | 3/3 | Coffret Douze — macro de l'angle : profil en aluminium brossé à arrête arrondie, insert intérieur noir texturé et bord d'un coussin gris — Maison Noirmont |

- **Fidélité** : « structure aluminium, intérieur suédine » → profil aluminium brossé, insert
  noir texturé, coussin gris. Conforme aux deux vues en ligne. Aucun verrou, aucune charnière
  ni mécanisme inventé — le travers récurrent de cette fournée (plaque laiton, surface
  circulaire) ne se présente pas ici.
- Aucun lettrage ni marque sur le profil ; aucun avis ni badge ; 2048×2048 JPEG.
- Fiche à 2 médias : le nouveau se place en 3/3, image 1 intacte, statut ACTIVE inchangé.

**Cumul : 47 visuels rattachés sur 43 fiches. 2 refus.**

---

## Tour 31 — 09/08/2026 ~02h30

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `coffret-douze-presentation` | `-g1` macro angle noyer | 3/3 | Coffret Douze présentation — macro de l'angle extérieur : coupe d'onglet du cadre en bois teinte noyer, doublure suédine crème et coussin de logement — Maison Noirmont |

- **Fidélité** : coupe d'onglet nette, bois teinte noyer, doublure suédine crème et coussin.
  Conforme aux deux vues en ligne. Aucun couvercle, charnière ni mécanisme inventé.
- **Distinction avec le Coffret aluminium (tour 30)** — les deux fiches portent le même nom
  « Coffret Douze » et ne se séparent que par le matériau : aluminium brossé + insert **noir**
  d'un côté, bois noyer + suédine **crème** de l'autre. Les deux macros sont sans ambiguïté
  et ne sont pas interchangeables.
- Aucun lettrage ni marque ; aucun avis ni badge ; 2048×2048 JPEG ; fiche à 2 médias, le
  nouveau se place en 3/3, image 1 intacte, statut ACTIVE inchangé.

**Cumul : 48 visuels rattachés sur 44 fiches. 2 refus.**

---

## Tour 32 — 09/08/2026 ~02h35

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `pince-a-barrettes` | `-g1` macro pivot + ressort | 3/3 | Pince à barrettes — macro du pivot en acier poli, du ressort de rappel hélicoïdal et du départ des mors fins — Maison Noirmont |

- **Fidélité** : acier argenté, branches lisses, ressort de rappel et mors fins — conformes
  aux deux vues en ligne. Le bracelet de mise en scène présent sur la source a été exclu du
  cadrage, ce qui évite d'introduire un produit tiers dans la galerie de l'outil.
- **Point de vigilance propre aux outils** : les pinces d'horloger portent très souvent une
  **gravure de marque sur une branche**. Contrôle fait sur toute la longueur visible des deux
  branches et sur le pivot : **aucune gravure, aucun lettrage, aucun sigle**. C'est ce même
  motif qui a fait écarter le Remontoir Solo au tour 28 — ici il ne se présente pas.
- Aucun avis ni badge ; 2048×2048 JPEG ; fiche à 2 médias, le nouveau se place en 3/3,
  image 1 intacte, statut ACTIVE inchangé.

**Cumul : 49 visuels rattachés sur 45 fiches. 2 refus.**

---

## Tour 33 — 09/08/2026 ~02h40

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `remontoir-bois-acajou` | `-g1` macro charnière + veinage | 3/3 | Remontoir Bois Acajou — macro de la charnière arrière en laiton, du veinage acajou brun roux satiné et de la bordure intérieure en velours noir — Maison Noirmont |

- **Fidélité** : « L'acajou tire vers un **brun chaud légèrement roux**, dont la veine reste
  lisible sous la finition **satinée** » — la macro montre exactement cette teinte et ce
  veinage, avec la façade vitrée et le velours noir. Conforme.
- **Le laiton est ici réel, et c'est le point intéressant** : au tour 29, Codex avait écarté
  une génération qui **inventait** une plaque en laiton sur le Remontoir Vitrine. Ici la
  charnière laiton existe bien sur la source et sur les vues en ligne. La distinction entre
  élément réel et élément halluciné est faite correctement dans les deux sens.
- **Attention handle** : ne pas confondre avec `remontoir-bois` (le produit parent, en
  **DRAFT**, qui regroupe les quatre teintes). Le visuel est bien allé sur la déclinaison
  Acajou ACTIVE. Aucun brouillon activé.
- Aucun lettrage ni marque ; aucun avis ni badge ; 2048×2048 JPEG ; fiche à 2 médias,
  le nouveau se place en 3/3, image 1 intacte, statut ACTIVE inchangé.

**Cumul : 50 visuels rattachés sur 46 fiches. 2 refus.**

---

## Tour 34 — 09/08/2026 ~02h45

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `rouleau-de-voyage-noir-cuir` | `-g1` macro logement intérieur | 3/3 | Rouleau de Voyage Noir — macro d'un logement intérieur : séparateurs en cuir noir mat, couture du rabat et cuir extérieur noir grainé roulé — Maison Noirmont |

- **Fidélité** : « Extérieur en cuir · **un logement par montre** » → la macro montre les
  séparateurs délimitant les logements et le cuir extérieur grainé, en noir. Conforme.
- **Montres et cordon exclus du cadrage** : aucun produit tiers ni accessoire n'est introduit
  dans la galerie — même précaution qu'au tour 32 sur la pince.
- Bien distinct du `rouleau-de-voyage-vert-cuir` traité au tour 1 (cuir vert, alvéole doublée) :
  ici cuir noir et intérieur noir mat.
- Aucun lettrage ni marque ; aucun avis ni badge ; 2048×2048 JPEG ; fiche à 2 médias, le
  nouveau se place en 3/3, image 1 intacte, statut ACTIVE inchangé.

**Cumul : 51 visuels rattachés sur 47 fiches. 2 refus.**

---

## Tour 35 — 09/08/2026 ~02h50

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `rouleau-de-voyage-brun-cuir` | `-g1` macro logement intérieur taupe | 3/3 | Rouleau de Voyage Brun — macro d'un logement intérieur : séparateurs et doublure en suédine taupe surpiquée, cuir extérieur cognac grainé roulé — Maison Noirmont |

### La famille Rouleau de Voyage est complète et cohérente

Trois déclinaisons traitées, trois couples cuir/doublure distincts — aucune interversion :

| Fiche | Cuir extérieur | Intérieur | Tour |
|---|---|---|---|
| `rouleau-de-voyage-vert-cuir` | vert grainé | alvéole doublée | 1 |
| `rouleau-de-voyage-noir-cuir` | noir grainé | noir mat | 34 |
| `rouleau-de-voyage-brun-cuir` | **cognac grainé** | **suédine taupe** | 35 |

- **Fidélité** : « Le cuir brun apporte une note plus chaude » → cuir cognac franc, nettement
  différent du noir du tour 34. Doublure taupe conforme aux vues en ligne. Conforme.
- Montres et cordon exclus du cadrage. Aucun lettrage ni marque ; aucun avis ni badge ;
  2048×2048 JPEG ; fiche à 2 médias, le nouveau se place en 3/3, image 1 intacte, statut
  ACTIVE inchangé.

**Cumul : 52 visuels rattachés sur 48 fiches. 2 refus.**

---

## Tour 36 — 09/08/2026 ~02h55

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `rouleau-de-voyage-bleu-marine-cuir` | `-g1` macro logement intérieur bleu | 3/3 | Rouleau de Voyage Bleu marine — macro d'un logement intérieur : séparateurs et doublure en suédine bleu marine, cuir extérieur bleu nuit grainé roulé — Maison Noirmont |

- **Fidélité** : « Le bleu marine tranche avec le noir sans verser dans la couleur vive. Un
  ton profond » → cuir bleu nuit et doublure bleu marine, ton sur ton. Conforme, et
  distinguable du noir du tour 34 malgré la proximité des deux teintes sombres.
- Quatre déclinaisons de Rouleau désormais traitées (vert, noir, brun, bleu marine), toutes
  avec le bon couple cuir/doublure. Aucune interversion sur la famille.
- Montres et cordon exclus ; aucun lettrage ni marque ; aucun avis ni badge ; 2048×2048 JPEG ;
  fiche à 2 médias, le nouveau se place en 3/3, image 1 intacte, statut ACTIVE inchangé.

**Cumul : 53 visuels rattachés sur 49 fiches. 2 refus.**

---

## Tour 37 — 09/08/2026 ~03h00

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `remontoir-collection-bois-noir` | `-g1` macro socle + bas de porte vitrée | 3/3 | Remontoir Collection Bois noir — macro du socle : bois noir mat à grain linéaire, ressaut du plinthe et bas de la porte vitrée — Maison Noirmont |

- **Fidélité** : « Coffret en bois **finition noire**, façade vitrée » → bois noir mat à grain
  linéaire visible, plinthe à ressaut, bas de porte vitrée. Conforme aux deux vues en ligne.
- **Montres et charnière exclus du cadrage** : aucune montre tierce introduite, et aucune
  quincaillerie ajoutée — le travers de la plaque laiton inventée (tour 29) ne se reproduit pas.
- Bien distinct du `remontoir-bois-acajou` (tour 33) : bois noir mat contre acajou brun roux.
- Aucun lettrage ni marque ; aucun avis ni badge ; 2048×2048 JPEG ; fiche à 2 médias, le
  nouveau se place en 3/3, image 1 intacte, statut ACTIVE inchangé.

**Cumul : 54 visuels rattachés sur 50 fiches. 2 refus.**

---

## Tour 38 — 09/08/2026 ~03h05

### Rattaché (1 visuel)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `remontoir-collection-bois-beige` | `-g1` macro socle bois blond | 3/3 | Remontoir Collection Bois beige — macro du socle : bois blond à grain droit, ressaut de plinthe arrondi et bas de la porte vitrée — Maison Noirmont |

- **Fidélité** : « Coffret en bois **beige**, façade vitrée. Une teinte claire et douce » →
  bois blond à grain droit, franchement clair. Conforme, et sans confusion possible avec la
  version noire du tour 37 : même géométrie de socle, teintes opposées.
- Montres et charnière exclus ; aucun lettrage ni marque ; aucun avis ni badge ;
  2048×2048 JPEG ; fiche à 2 médias, le nouveau se place en 3/3, image 1 intacte, statut
  ACTIVE inchangé.

### Note de suivi — recherche du chemin `scratchpad/noirmont-galeries` close

La recherche système lancée au tour 7 pour localiser le dossier
`scratchpad/noirmont-galeries/entrees-faces/` s'est terminée **sans aucun résultat** sur
l'ensemble du disque. Confirmation définitive : ce chemin, cité par la majorité des
manifestes de la nuit, **n'existe nulle part**. Les contrôles de source ont donc tous été
faits par substitution (planches QA + vues Shopify en ligne), ce qui a suffi à trancher
chaque cas. À corriger côté Codex : citer un chemin versionné du repo, comme il l'a fait
correctement pour les Squelettes et les Éclaireurs.

**Cumul : 55 visuels rattachés sur 51 fiches. 2 refus.**

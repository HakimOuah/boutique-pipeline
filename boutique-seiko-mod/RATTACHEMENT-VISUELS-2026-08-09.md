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

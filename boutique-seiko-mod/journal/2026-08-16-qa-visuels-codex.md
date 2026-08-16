# QA visuelle — 108 visuels Codex, 20 fiches Maison Noirmont (16/08/2026)

Contrôle image par image de `livraisons/visuels-codex-2026-08/` pour les 20 fiches
livrées les 15-16/08. Aucune opération Shopify, aucun appel connecteur : fichiers locaux seuls.

Périmètre réel : la mission parlait de 104 visuels, le `RAPPORT-FINAL.md` de Codex en
déclare **108** (88 galerie + 20 variante). C'est bien 108 fichiers qui sont sur le disque.

---

## 1. Contrôles objectifs (passés sur les 20 fiches, script)

### Technique — PASS complet

- 108/108 fichiers JPEG **2048 × 2048**. Aucune exception.
- Poids entre 456 ko et 878 ko. Aucun fichier absent, aucun fichier orphelin sur disque.
- Les 108 chemins `source` des manifestes **se résolvent tous** vers un fichier local existant.
- Les manifestes respectent le schéma (handle, slot, sku_fournisseur, source).

### Discipline de sourcing — PASS complet, et c'est le point le plus rassurant du lot

C'était le risque n°1 annoncé (11 sources sur 15 portant le logo `Tandorio`).
Vérification croisée de chaque `source` de manifeste contre son verdict dans
`GALERIES-DSERS-2026-08-15.json` :

- **Aucune source `interdit` n'est utilisée.** Aucune source `ecarte` non plus.
- Chaque fiche part bien de **sa propre** `face_exploitable` déclarée dans le JSON :
  36 noir → 15.jpg, vert → 12.jpg, bordeaux → 13.jpg, bleu → 14.jpg,
  42 titane noir → 18.jpg, bleu → 17.jpg,
  squelettes 40 : anneau-noir → 26, blanc → 24, vert → 22, aig. bleues → 25,
  aig. rouges → 21, lunette bleue → 23,
  pont cuir → 07, pont cuir noir → 08,
  coffrets 12 noir → 16, 12 acajou → 14, 10 acajou → 15, 6 acajou → 13,
  malette → 03/04 + 08 pour la variante, porte-montre → 06.
- Aucune permutation de coloris entre fiches d'un même article fournisseur. Or les 4 plongeuses 36
  viennent **du même article** `1005010218960866` et les 6 squelettes 40 **du même article**
  `1005006771109294` : c'était le piège évident, il est évité.
- 57 associations sur source `ok`, 51 sur source `reserve` (filigrane BLIGER / cotes incrustées),
  ce qui est cohérent avec ce que le JSON autorise.

### Doublons binaires — À TRANCHER (défaut de livraison, pas de conformité)

- **19 fiches sur 20** livrent un « visuel de variante » qui est la **copie octet pour octet**
  de son `g1`. Même md5. Seule `malette-quinze-montres-etanche` livre une variante distincte.
- Les 6 squelettes 40 partagent **le même fichier `g5`** (md5 `ad55af4b…`), un seul et même
  rendu de fond de boîte recyclé six fois.
- Bilan : **108 fichiers déclarés = 87 images réellement distinctes.** Codex documente le
  partage du g5 mais pas la duplication g1/variante.

---

## 2. Contrôle visuel fiche par fiche

### 2.1 `montre-style-plongeuse-36-cadran-noir` — 6 visuels

Source retenue `15.jpg` (verdict `ok`, cadran strictement nu) + `05.jpg` (boucle/fond, `ok`).
Bonne source. La source est une photo au poignet 1000 × 1000, filigrane `Tandorio`
en haut à gauche de la **photo**.

| Fichier | Verdict | Motif observable |
|---|---|---|
| `-g1.jpg` (face) | conforme | Cadran nu : 12 / 1 bâton / 2-9 / 10 / 11 en double bâton, identique à la source. Aucun logo, aucune mention. Filigrane `Tandorio` disparu. Fond recomposé homogène. Bracelet cuir brun et boucle ardillon fidèles. |
| `-g2.jpg` (situation) | conforme | Même cadran, dalle secondaire floue. Rien d'incrusté. |
| `-g3.jpg` (macro) | **à refaire** | Voir ci-dessous. |
| `-g4.jpg` (porté) | conforme | Poignet seul, manche sombre, aucun visage ni bijou. Cadran lisible et cohérent. |
| `-g5.jpg` (détail boucle/fond) | conforme | Boucle brossée, cuir, coutures, fond de boîte **lisse et vierge** — or la source `05.jpg` montre un fond gravé de texte fournisseur : le texte a bien été retiré, pas remplacé par du faux texte. Bon point. |
| `-v-black-sterile-dial-1.jpg` | conforme mais **doublon** de `g1` (md5 identique) |

**Motif du `à refaire` sur `g3`** : sur la macro, le chiffre `10` de la minuterie
périphérique (secteur 2 h) est cassé en deux glyphes détachés — un bâton `1` puis un anneau
creux `O` posé plus bas et à un autre rayon, alors que la source imprime un `10` d'un seul
tenant. Dans le même secteur 5 → 15, la longueur des traits de minuterie devient irrégulière
(traits longs et courts sans rythme) là où la source garde un chemin de fer régulier.
Le `compte-rendu.md` affirme pourtant « graduation périphérique régulière sur 360° » : la QA
interne de Codex n'a pas vu ce défaut. C'est exactement le troisième défaut caractéristique
annoncé (« repères de minuterie déformés »), sur la vue où il se voit le plus.

Rejets `rejected/` de la fiche (6) : cadrage, axe, fond non homogène, et surtout
`g1-index-promu-en-chiffre.jpg` — Codex sait donc détecter ce défaut, il l'a écarté sur g1.

### 2.2 `montre-style-plongeuse-36-cadran-vert` — 6 visuels — **TOUS À REFAIRE**

C'est le défaut le plus grave du lot, et il touche les 6 fichiers de la fiche.

La source `12.jpg` est une photo au poignet où le verre bombé renvoie **un reflet de ciel
bleu** sur le quart inférieur droit du cadran : bords flous, il suit la courbure du dôme,
il éclaircit les points de lume qu'il traverse. C'est un reflet, pas une finition.

Codex l'a transformé en **aplat cyan peint sur le cadran** : dans `g5` (vue de détail 3/4,
la plus lisible) le bleu est un **polygone à arêtes droites et nettes**, d'une couleur plate,
qui coupe le cadran en diagonale, **passe par-dessus le cadre du guichet de date** et
**sous le repère rectangulaire de 6 h**. Aucune finition de cadran ne se comporte ainsi.
Pire, la même découpe apparaît **au même angle** dans `g1`, `g2`, `g3`, `g4` et la variante,
y compris sur la vue portée : un reflet ne peut pas être identique sous cinq éclairages
et cinq angles différents. Le client verrait un cadran bicolore vert/bleu qui n'existe pas.

C'est exactement « la texture inventée » du brief. La preuve que Codex savait faire :
sur `bordeaux` (source `13.jpg`) et sur `bleu` (source `14.jpg`), qui portent **le même
reflet bleu** au même endroit, il l'a proprement supprimé.

| Fichier | Verdict |
|---|---|
| `-g1` `-g2` `-g3` `-g4` `-g5` `-v-green-sterile-dial` | **à refaire** (les 6) |

Le reste de la fiche est bon : cadran stérile, aiguille flèche orange fidèle, date `3`
conforme à la source, triangle 12 h, rectangles 6 h et 9 h, points ronds ailleurs.
Seule la couleur du cadran est à reprendre.

### 2.3 `montre-style-plongeuse-36-cadran-bordeaux` — 6 visuels — conformes

Source `13.jpg` (`ok`). Reflet bleu de la source **correctement retiré** : le cadran rendu
est un dégradé rouge uniforme sur les 5 vues. Aiguille flèche à liseré rouge, aiguille des
heures losange, trotteuse fine : fidèles. Date `4` conforme à la source. Triangle 12 h,
rectangles 6 h et 9 h, 8 points ronds : compte exact. Aucun texte, aucun logo, aucune
étoile ni badge. Couronne cannelée fidèle. Filigrane `Tandorio` disparu.
Les 4 rejets `aiguille-noire-incomplete` montrent que le contrôle des aiguilles a été fait.
`-v-red-sterile-dial` = **doublon binaire** de `g1`.

### 2.4 `montre-style-plongeuse-36-cadran-bleu` — 6 visuels — conformes

Source `14.jpg` (`ok`). Reflet bleu absorbé en soleillé homogène, sans arête. Aiguille
flèche à liseré rouge fidèle, date `2` conforme, index et compte corrects, cadran stérile.
`g5` propre et net. 1 rejet `g5-graduation-inventee` : le défaut de graduation a donc bien
été chassé sur cette fiche-là. `-v-blue-sterile-dial` = doublon binaire de `g1`.

### 2.5 `montre-style-plongeuse-42-titane-noir` — 6 visuels — conformes

Source `18.jpg` (`ok`, cadran strictement nu). Cadran noir stérile, aiguilles type MilSub,
repères carrés + triangle 12 h + rectangles 3/6/9 : fidèles. Lunette : pastille de lume à
12 h et **10 / 20 / 30 / 40 / 50 dans le sens antihoraire**, exactement la disposition de
la source. Aucun chiffre inventé, aucun chiffre inversé. Bracelet NATO noir à bande grise
fidèle. `g5` (détail couronne/corne) : boîtier titane brossé, couronne cannelée, trou de
corne, **aucune gravure, aucune mention d'étanchéité**. 2 rejets sur la trotteuse.

### 2.6 `montre-style-plongeuse-42-titane-bleu` — 6 visuels — conformes

Source `17.jpg` (`ok`). Idem en bleu : lunette bleue, aiguille des secondes bleue fidèle
à la source, cadran bleu stérile. Contrôle rapproché des chiffres de lunette au zoom ×3 :
le `20` en bas à gauche et le `40` en bas à droite sont **bien formés et orientés
radialement comme sur la source** — ce ne sont pas des glyphes inversés. Les 2 rejets
(`chiffres-lunette-inverses`, `nombre-lunette-invente`) confirment que ce contrôle a été
fait sérieusement sur cette famille.

**Bilan plongeuses (36 visuels) : 29 conformes, 7 à refaire** (les 6 du vert + le `g3` du noir).

### 2.7 Les 6 `montre-squelette-automatique-40-*` — 36 visuels — conformes

C'était la deuxième zone à risque : les sources portent **trois** saletés à effacer, toutes
vérifiées comme **disparues** dans les livrables :

1. le filigrane `BLIGER Official Store` en haut à gauche des 26 photos ;
2. le **`904L` rouge** imprimé sur le film de protection du bracelet — contrôlé au zoom ×2,6
   sur le bracelet de `anneau-noir-g1` : maillons Oyster brossés, **aucune inscription rouge,
   aucun film plastique** ;
3. sur `06.jpg` (source du `g5`), la gravure `NH70A · TWENTY-FOUR JEWELS` sur le mouvement
   et le `904L` rouge partout sur le film : le `g5` livré montre un fond transparent avec
   masse oscillante **lisse et vierge**, sans aucun texte.

Appariement coloris → source, vérifié un par un, **6/6 justes** :
`aiguilles-rouges` = 21 (lunette acier, anneau blanc, aiguilles rouges) ·
`anneau-vert` = 22 (anneau turquoise — la source est bien turquoise, pas vert : c'est le
libellé de la fiche qui est approximatif, pas le visuel) · `lunette-bleue` = 23 (lunette
bleue, aiguilles dorées) · `anneau-blanc` = 24 (lunette noire, anneau blanc) ·
`aiguilles-bleues` = 25 (lunette GMT bicolore noir/bleu, aiguille GMT bleue) ·
`anneau-noir` = 26 (lunette acier, anneau noir).

Contrôle de lunette au plein format sur `aiguilles-bleues-g3` : la lunette 24 h affiche
`2 · 4 · 6 · 8 · 10 · 12 · 14 · 16 · 18 · 20 · 22` avec le triangle à 24 h, séquence
complète, dans l'ordre, correctement pivotée. Aucun chiffre manquant ni inventé.
Aucun cadran ne porte de texte : le mouvement squelette est nu.

Deux réserves de livraison (pas de conformité) : le `g5` est **un seul fichier recyclé sur
les 6 fiches**, et les 6 visuels de variante sont des doublons binaires des `g1`.

### 2.8 `montre-squelette-automatique-pont-cuir` et `-pont-cuir-noir` — 12 visuels — conformes

C'était la fiche la plus exposée au « lettrage cursif inventé » : Codex y a écarté **5 rendus**
pour ce motif (`pseudo-inscriptions-sur-pont`, `glyphe-invente-sur-pont`,
`graduation-minute-malformee`, `graduation-et-glyphes-inventes`).

Contrôle au zoom ×2 sur `pont-cuir-g3`, secteur haut puis secteur bas :

- Chiffres romains de la lunette dorée : `XII · I · II · III · IV · V · VI · VII · VIII · IX · X · XI`,
  les 12 présents, dans l'ordre, **pivotés radialement exactement comme la source** (au bas du
  cadran ils se lisent donc à l'envers, ce qui est le comportement de la source et non un défaut).
- Minuterie intérieure : `60 · 05 · 10 · 15 · 20 · 25 · 30 · 35 · 40 · 45 · 50 · 55`,
  les 12 présents, aucun trou, traits intermédiaires réguliers.
- Une micro-anomalie observée : une rangée de marques minuscules sur l'arête supérieure du pont
  horizontal, à gauche de l'aiguille des minutes. À ×6 elle ne forme **aucun mot lisible** et
  correspond à la densité mécanique réelle de la source (dentures, rubis, vis). Je ne la
  compte pas comme inscription inventée, mais c'est le point à re-regarder si Hakim veut être
  maximaliste.

La version noire (`pont-cuir-noir`, source `08.jpg`) est le même travail en boîtier PVD noir
et cuir noir : même contrôle, même résultat.

### 2.9 Les 4 coffrets bois laqué — 16 visuels — **2 à refaire**

**Le nombre de logements est juste sur les 4 fiches** — c'était le contrôle attendu :
douze noir = 6 + 6 = **12** · douze acajou = 6 + 6 = **12** · dix acajou = 5 + 5 = **10** ·
six acajou = une rangée de **6**. Les cotes en centimètres incrustées sur les sources
(`3CM`, `4.5CM`, `8.5CM`, `5CM`, `20CM`, `31.3CM`) ont toutes disparu. Intérieur brun pour le
coffret noir, crème pour les acajou : conforme aux sources.

**Mais les deux `g2` des coffrets 12 places sont à refaire.**

`coffret-douze-montres-bois-laque-noir-g2.jpg` et
`coffret-douze-montres-bois-laque-acajou-g2.jpg` montrent le coffret **rempli de 12 montres
générées**, et au zoom ×6 **chaque cadran porte un logotype inventé** : un mot en cursive ou
en romain fin imprimé sous le 12, et sur plusieurs cadrans **une deuxième ligne de texte au
niveau du 6**. C'est le « lettrage cursif inventé » du brief, et c'est une infraction directe
à l'interdit « aucun logo, sigle ni marque sur les cadrans ». Ces deux fichiers ne peuvent pas
être rattachés.

Les `g2` des coffrets **10 et 6** places contiennent aussi des montres générées, mais leurs
cadrans sont **stériles** (chiffres arabes seuls, aucune inscription) : ils passent.

Point à trancher par Hakim, au-delà de la QA : les coffrets sont vendus **vides**. Les montrer
garnis de 10 à 12 montres est un risque de misrepresentation GMC indépendamment du lettrage.

### 2.10 `malette-quinze-montres-etanche` — 4 visuels — **1 à écarter**

| Fichier | Verdict | Motif |
|---|---|---|
| `-g1` | conforme | Plateau mousse **5 colonnes × 3 rangées = 15 logements**, exactement la capacité vendue. Aucun texte. |
| `-g2` | conforme | Même malette garnie de 15 montres à cadrans stériles. |
| `-g3` | **à écarter** | Le plateau rendu **ne correspond pas à celui de `g1`** : logements nettement plus étroits et **au moins 4 rangées** au lieu de 3. Il vient de la source `04.jpg`, qui montre le plateau mousse sorti de la malette dans une découpe plus dense que la variante 15. Deux photos de la même fiche annonceraient donc deux capacités différentes. Le JSON avait déjà écarté `05.jpg` et `07.jpg` pour « plateau 8 logements, ce n'est pas la variante 15 vendue » : le piège de variante n'a été évité qu'à moitié. |
| `-v-15-slots` | conforme | Malette fermée, coque noire, poignée, loquets. Le texte `15 slots` + cotes intérieures de la source `08.jpg` a bien été retiré. Seule variante du lot qui **n'est pas** un doublon de son `g1`. |

### 2.11 `porte-montre-bois-massif-cuir` — 4 visuels — conformes

La galerie source mélangeait deux produits et contenait une bouteille de cognac de marque et
une photo de pesée sur balance. **Aucune trace de l'un ou de l'autre dans les livrables.**

Source retenue `06.jpg` = la **variante A** effectivement vendue. Le support livré est un C
en chêne clair massif avec **coussinet de cuir grainé bordeaux** : c'est exactement la
variante A, pas la variante B à plateau violet (stock 0) qui était `ecarte` sur les photos 2 à 5.
Les cotes `7cm/2.76in`, `5cm/1.97in`, `6cm/2.36in` incrustées sur la source ont disparu.
Le `g2` pose une montre sur le support : son cadran est **stérile**, aucun logo.
Aucun objet tiers, aucun décor rapporté, aucune main.

---

## 3. Synthèse

### Décompte final sur 108 visuels

| Verdict | Nombre |
|---|---:|
| **conforme — rattachable tel quel** | **98** |
| **à refaire** | **9** |
| **à écarter** | **1** |

Détail des 10 non rattachables :

- `montre-style-plongeuse-36-cadran-vert` : **les 6** (`g1` à `g5` + variante) — aplat cyan
  peint sur le cadran vert, arêtes droites traversant le guichet de date, identique sur les
  cinq vues.
- `montre-style-plongeuse-36-cadran-noir-g3` — `10` de la minuterie cassé en `1` + `O`
  détachés, traits de minuterie irréguliers dans le secteur 5–15.
- `coffret-douze-montres-bois-laque-noir-g2` et `coffret-douze-montres-bois-laque-acajou-g2`
  — logotypes inventés sur les cadrans des 12 montres présentes dans le coffret.
- `malette-quinze-montres-etanche-g3` — **à écarter** : plateau d'une autre capacité que le `g1`.

### Réserves qui ne bloquent pas le rattachement

1. **19 des 20 « visuels de variante » sont des copies octet pour octet de leur `g1`** et les
   6 squelettes 40 partagent un `g5` unique : 108 fichiers pour **87 images distinctes**.
   Si Shopify doit porter un média de variante réellement distinct, il en manque 19.
2. Les coffrets et la malette sont vendus vides mais montrés garnis — décision merchandising
   et GMC à prendre par Hakim, hors périmètre QA.
3. La mission annonçait 104 visuels, le lot en contient 108. Écart à acter.

### Consigne exacte à redonner à Codex

> Reprends **10 fichiers**, sans retoucher les 98 autres, et sans changer de source :
>
> 1. **`montre-style-plongeuse-36-cadran-vert`, les 6 fichiers.** La source `12.jpg` porte un
>    reflet de ciel bleu sur le verre bombé, dans le quart inférieur droit. Ce n'est **pas**
>    une finition de cadran : c'est un reflet. Supprime-le et rends le cadran **vert uniforme
>    en soleillé sur 360°**, exactement comme tu l'as déjà fait pour `bordeaux` (source
>    `13.jpg`) et `bleu` (source `14.jpg`), qui portaient le même reflet. Aucune arête droite,
>    aucun aplat de couleur, aucune zone bicolore. Le reste de la fiche est bon : garde
>    l'aiguille flèche orange, la date `3`, le triangle 12 h, les rectangles 6 h et 9 h.
> 2. **`montre-style-plongeuse-36-cadran-noir-g3`.** Refais la minuterie périphérique : le `10`
>    doit être un nombre d'un seul tenant comme les autres (`60`, `55`, `50`…), pas un `1` et un
>    `O` séparés à des rayons différents ; et les traits intermédiaires doivent avoir une
>    longueur et un pas constants sur les 360°, en chemin de fer, comme dans la source.
> 3. **`coffret-douze-montres-bois-laque-noir-g2`** et
>    **`coffret-douze-montres-bois-laque-acajou-g2`.** Les 12 montres que tu as placées dans le
>    coffret portent un logotype inventé sous le 12 et une deuxième ligne de texte vers le 6.
>    **Aucune surface de cadran ne doit porter le moindre caractère.** Refais-les avec des
>    cadrans strictement stériles — chiffres arabes ou index seuls — comme tu l'as fait pour les
>    coffrets 10 et 6 places, qui sont corrects.
> 4. **`malette-quinze-montres-etanche-g3`.** Le plateau que tu as rendu n'a pas la découpe du
>    `g1` : logements plus étroits, au moins 4 rangées au lieu de 3. La fiche vend **15
>    logements en 5 colonnes × 3 rangées**. Refais le `g3` en macro **du plateau de `g1`**,
>    et non de celui de la source `04.jpg` qui montre une découpe d'une autre variante.
>
> Deux règles générales pour cette reprise :
>
> - **Ne peins jamais sur le produit ce qui est un reflet, une ombre ou un film de protection
>   sur la photo source.** Reflet de verre, halo de lampe, plastique d'emballage : ça se
>   supprime, ça ne se transforme pas en finition.
> - **Aucun caractère nulle part sur un produit** : ni sur un cadran, ni sur un fond de boîte,
>   ni sur un pont de mouvement, y compris sur les objets d'accompagnement que tu génères
>   toi-même dans la scène.
>
> Et une question à trancher avant la prochaine passe : les 19 « visuels de variante » sont
> aujourd'hui des copies exactes de leur `g1`. Soit ils doivent devenir des vues réellement
> distinctes, soit il faut cesser de les compter comme des visuels séparés.

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

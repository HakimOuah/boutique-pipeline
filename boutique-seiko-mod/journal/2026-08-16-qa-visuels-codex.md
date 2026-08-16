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

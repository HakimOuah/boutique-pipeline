# Brief Codex — lot 4 : fermer la couverture visuelle des variantes

Date : **04/09/2026 (soir)** · Boutique : **Lumière Matière** (`lumierematiere.fr`)
Suite de `2026-09-04-codex-lot3-montages.md` (16/16 livrés, importés et contrôlés).
Constat source : `journal/2026-09-04-revue-libelles-catalogue.md`.

## Où on en est

Le lot 3 a réglé les montages fournisseur. La revue de tous les libellés qui a suivi a mesuré
ce qui reste : **sur 52 fiches et 158 variantes, 20 fiches ont encore des variantes qui
partagent une photo.** Toutes ne sont pas un problème — quand seule la taille change, partager
la photo est légitime, c'est l'échelle qui manque. Ce brief sépare les deux.

**Règles inchangées, non négociables** : une image = un seul luminaire · fond papier `#F6F3EC` ·
lumière chaude · JPEG RGB 2048 × 2048 · aucun texte, cote, logo, badge, main, visage ni décor
de pièce (seule exception : les schémas cotés du lot B) · aucune action Shopify ni DSers ·
**SKU intouchables**.

**Règle de correspondance, rappelée parce qu'elle a coûté deux erreurs le 04/09** : le lien
variante → référence se lit **dans le SKU et dans `preuves-dom.json`**, jamais dans un nom de
fichier ni dans une lecture d'image. Sur `338324`, les lettres de la boutique ne sont pas
celles du fournisseur.

---

## Lot A1 — la forme ou la finition est fausse à l'écran (13 visuels)

Le sélecteur annonce une chose, la photo en montre une autre. C'est de la misrepresentation
au sens GMC, au même titre qu'un montage.

### `suspension-rotin-607504` — 4 visuels · **priorité 1**

Quatre variantes, **une seule photo** pour tout le monde, alors que ce sont trois silhouettes
différentes plus une finition noire. Cotes et identifiants prouvés (planches fournisseur +
`preuves-dom.json` du 04/09) :

| SKU option | Libellé boutique | Ce qu'il faut montrer |
|---|---|---|
| `200000795:193#2550` | `25 × 50 cm · naturel` | **goutte** haute et étroite, rotin naturel, col bois tourné |
| `200000795:10#4040` | `40 × 40 cm · naturel` | **bulbe** large, rotin naturel, col bois tourné |
| `200000795:175#4019` | `40 × 19 cm · naturel` | **coupole plate** évasée, rotin naturel, col bois foncé |
| `200000795:367#4040BK` | `40 × 40 cm · noir` | **bulbe** large, rotin **teinté noir**, col bois clair |

Références : `sources-par-handle/suspension-rotin-607504/variantes-20260904/200000795-{193,10,175,367}.jpg`
— elles portent les cotes incrustées, donc **jamais publiables telles quelles**.

### `suspension-deco-led-837156` — 4 visuels

Quatre variantes, deux photos : l'émail est montré, **la hauteur ne l'est pas**. Ta mesure du
lot 3 : deux hauteurs d'abat-jour, toutes Ø 20 cm.

| SKU option | Libellé boutique | Rendu |
|---|---|---|
| `200000531:365458` | `Céladon vert · H 6,5 cm` | festonné vert céladon, **bas** |
| `200000531:193` | `Céladon vert · H 9 cm` | festonné vert céladon, **haut** |
| `200000531:175` | `Céladon bleu poudré · H 6,5 cm` | festonné bleu poudré, **bas** |
| `200000531:173` | `Céladon bleu poudré · H 9 cm` | festonné bleu poudré, **haut** |

Références : `sources-par-handle/suspension-deco-led-837156/variantes-lot3-20260904/`.
**Les deux photos actuelles ne sont pas identifiées en hauteur** : refaire les quatre plutôt que
deviner laquelle est laquelle.

### `suspension-bambou-led-630923` — 2 visuels

Trois variantes, une photo. Or l'axe n'est pas la taille : deux variantes sont des
**plafonniers** (montage direct) et une est une **suspension** (câble). Le client ne voit pas
la différence, qui est la plus importante de la fiche.

| SKU option | Libellé | Rendu |
|---|---|---|
| `200000531:173#Ceiling 50cm` | `Ø 50 cm · plafonnier` | disque plat bambou, **au plafond, sans câble** |
| `200000531:193#Pendant 50cm` | `Ø 50 cm · suspension` | même disque, **au bout d'un câble** |
| `200000531:365458#Ceiling 60cm` | `Ø 60 cm · plafonnier` | plafonnier, plus large |

Deux à produire (la troisième reprend le cadrage de la première, au diamètre près — à trancher
au moment du rendu).

### `suspension-bois-193329` — 2 visuels, **après identification**

Quatre variantes, deux photos : la teinte de bois est montrée, **la forme A/B ne l'est pas**.
Le SKU prouve la teinte (`Walnut Base` / `Wood color`) mais **pas la forme**, et il n'y a
aucune référence par variante en local.

**À faire d'abord** : passe DOM sur la PDP, récupérer une référence par identifiant d'option
(`193`, `173`, `365458`, `175`) et établir ce que valent les formes A et B. Puis produire les
deux visuels manquants. **Si la forme reste indéterminable, ne rien produire et le dire** —
c'était la bonne décision sur le modèle A de `338324`.

### `suspension-effet-pierre-led-338324` — 1 visuel

Le modèle A (`200000531:193`) garde encore une vue générique. **Son identité est maintenant
établie** : la grille fournisseur est `A/B` × `Wood color / Dark wood color`, trois cases sur
quatre sont observées au DOM, et la planche cotée `05.jpg` montre le Ø 12 × H 10 à **tête bois
clair**. Libellé boutique : `Cylindre bas · tête bois clair`.

Produire le packshot. **Et confirmer au passage** que l'identifiant `193` reste bien absent du
sélecteur — c'est la seule cellule reconstituée du catalogue.

---

## Lot A2 — le nombre de lumières n'est pas montré (17 visuels)

Même nature de problème, moins spectaculaire mais tout aussi faux : le client choisit
« 8 lumières » et voit un luminaire à 4 bras.

| Fiche | Variantes | Photos | À produire | Ce qui change |
|---|---:|---:|---:|---|
| `plafonnier-led-992600` | 9 | 3 | **6** | 3 finitions × 4 / 6 / 8 boules — une seule photo par finition |
| `suspension-metal-noir-dore-361680` | 6 | 2 | **4** | doré / noir × 4 / 6 / 8 bras |
| `lustre-statement-led-noir-950316` | 3 | 1 | **2** | 4 / 6 / 8 boules sputnik |
| `plafonnier-led-led-183789` | 4 | 2 | **2** | gris / blanc × 5 / 6 palets |
| `lustre-anneau-led-led-717226` | 2 | 1 | **1** | 4 vs 6 anneaux |
| `lustre-anneau-led-led-625575` | 2 | 1 | **1** | 4 vs 6 anneaux |
| `lustre-anneau-led-led-134962` | 4 | 3 | **1** | blanc 5 vs blanc 6 lumières |

Le nombre de lumières se lit dans le SKU (`#4 lights`, `#8 heads`, `#Black 6T`…) : la
correspondance est sans ambiguïté sur ces sept fiches.

---

## Lot B — schémas cotés, 10 fiches où seule la taille change (10 visuels)

Ici, partager la photo est **légitime** : c'est le même luminaire. Ce qui manque est l'échelle.
Même convention que le lot P6 du 04/09 : silhouette en élévation, de face, fond `#F6F3EC`,
cotes en gris charbon `#24211B`, unités en cm. **Seule exception à l'interdit « aucune cote,
aucun texte »**, et elle ne vaut que pour ce lot. Nom : `{handle}-schema-g6.jpg`.

`lustre-salon-blanc-246282` (Ø 30/40/50/60) · `suspension-moderne-led-noir-330664`
(Ø 100/120/150) · `suspension-bambou-655008` (Ø 30/38/45) ·
`suspension-bambou-led-50cm-377816` (Ø 30/40/50) · `suspension-rotin-led-761433`
(Ø 30/40/50/60) · `applique-murale-pierre-588683` (Ø 20/25/30) ·
`lustre-anneau-led-led-795468` (Ø 20/30) · `suspension-rotin-607504` (les 4 cotes ci-dessus) ·
`suspension-deco-led-837156` (H 6,5 / H 9, Ø 20) · `suspension-bambou-led-630923`
(Ø 50/60, plafonnier vs suspension).

---

## Lot C — deux questions, aucune image avant réponse

### `suspension-bois-led-934110` — l'option n'est pas un axe

L'option « Modèle » vaut aujourd'hui `Blanc froid 6000 K` · `Travertin` · `Blanc chaud 3000 K`.
Ce sont **une matière et deux températures de couleur** dans la même liste. Les libellés sont
la traduction fidèle des SKU (`175#6000k-cold white`, `193#Yellow Travertine`,
`173#3000k-warm white`) : **l'incohérence vient du fournisseur**.

Question : le tube existe-t-il en deux matières (travertin / blanc) et la température est-elle
un axe séparé, ou les trois options sont-elles vraiment ce que le fournisseur propose en vrac ?
Passe DOM, réponse dans le manifeste. **Aucune image avant.**

### `suspension-effet-pierre-092465` — vérification légère

Libellés `Pierre claire` / `Brun`, deux packshots en place et distincts. Rien à produire ;
confirmer seulement que la correspondance SKU (`200006153` / `365458`) est la bonne.

---

## Livraison

`livraisons-visuels-codex/couverture-2026-09-05/{handle}/`
Un `manifeste.json` par handle, schéma habituel, avec pour chaque image **le SKU d'option
servi** et la mention explicite « un seul luminaire dans le cadre ».
Une planche `qa-couverture.jpg` de toutes les images livrées.

| Lot | Visuels | Nature |
|---|---:|---|
| A1 — forme et finition fausses | **13** | packshots, priorité 1 |
| A2 — nombre de lumières | **17** | packshots |
| B — schémas cotés | **10** | schémas, seule exception aux cotes |
| C — questions | **0** | réponses au manifeste |
| | **40 au maximum** | |

Si le volume est trop large pour une passe, **livrer A1 seul et s'arrêter** : c'est le seul lot
qui touche à la conformité GMC. A2 et B sont de la qualité de fiche.

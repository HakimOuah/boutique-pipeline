# 12/08/2026 — Réparation des régressions P0 (T-01, T-02, T-03)

Boutique **Maison Noirmont**, sous mot de passe. Aucun brouillon activé, aucune collection publiée,
aucun prix ni SKU touché. Toutes les opérations passent par le connecteur Shopify.

---

## 1. Ce que la session du 12/08 a réellement fait — le chiffre du ticket était sous-estimé

Le ticket T-01 parlait de **14 fiches actives amputées**. La comparaison ligne à ligne entre
l'état d'entrée de la session fautive (`preuves/2026-08-12-efficacite-extreme/audit-actifs.json`,
96 fiches actives, 529 médias) et l'état Shopify relevé ce soir donne :

| | |
|---|---|
| Fiches actives ayant **perdu** des médias | **37** (et non 14) |
| Médias retirés au total sur ces 37 fiches | **97** |
| dont photos fournisseur / AliExpress brutes — **retrait légitime** | **36** |
| dont **visuels maison** — **retrait à tort** | **61** |
| Fiches tombées à **1 seule image** | 4 |
| Fiches passées **sous la cible maison** (5 par montre, 3 par accessoire) | 30 |

### Cause racine

Le fichier d'audit qui a servi de base à la session porte sa propre explication, dans son bloc
`classification` :

> `fournisseur_aliexpress` : « Tout autre média Shopify actif, classé **conservativement** comme
> fournisseur/AliExpress faute de livrable Maison local traçable. »

Autrement dit : **tout visuel maison dont le fichier local n'était pas retrouvé a été étiqueté
fournisseur, puis supprimé.** C'est ainsi que `trente-neuf-duo-classique-bicolore-02-situation.jpg`,
`noirmont-un-plongeuse-acier-poignet.jpg` ou les sept composites de coloris `c-430162-*.jpg`
— tous des livrables maison — ont été traités comme des photos AliExpress.

Aggravant : une partie des retraits est passée par `fileDelete` (suppression définitive du fichier
Shopify) et non par `fileUpdate referencesToRemove` (simple détachement). Sur les 61 visuels maison
retirés, **37 n'existent plus du tout dans les fichiers Shopify** — seule la copie locale dans
`livraisons/` permettait de les récupérer.

---

## 2. T-01 — Restauration des galeries

### Méthode

1. Diff média par média entre l'état d'avant et l'état courant, pour les 37 fiches concernées.
2. Tri par nature du fichier : les `<id-produit>-N.jpg` et `<id-produit>-var-<coloris>.jpg` sont les
   photos AliExpress importées par DSers → **non restaurées**. Les `*-02-situation.jpg`,
   `*-03-macro.jpg`, `*-04-poignet.jpg`, `*-g1.jpg`, `c-<id>-<coloris>.jpg`, `gmt-*.jpg` sont des
   livrables maison → candidats à la restauration.
3. **Contrôle visuel de chaque candidat** avant tout rattachement : téléchargement, planche de
   contact pleine image + planche recadrée à 45 % (zoom cadran, couronne, lunette). Recherche de
   logo, sigle, lettrage, mention d'origine, formule de certification, badge, note incrustée et du
   défaut « index promu en chiffre ».
4. Rattachement **en fin de galerie**, `alt` descriptif en français, image 1 jamais déplacée.
   - fichier encore présent dans Shopify → `fileUpdate` + `referencesToAdd` (pas de doublon créé) ;
   - fichier définitivement supprimé → `stagedUploadsCreate` + PUT du fichier local + `productCreateMedia`.

### Résultat — 34 médias ré-attachés ou ré-uploadés sur 15 fiches

| Fiche | Avant 12/08 | Après la session fautive | Aujourd'hui | Médias rendus |
|---|---|---|---|---|
| `trente-neuf-classique-cannelee` | 12 | 1 | **7** | 7 composites de coloris `c-430162-*` |
| `trente-neuf-duo-classique-bicolore` | 10 | 1 | **6** | situation, macro, poignet, `c-722770-or-rose`, `c-722770-dore` |
| `montre-aviateur-acier-cadran-chiffres-1-12` | 5 | 1 | **5** | 4 fichiers ré-uploadés depuis `livraisons/` |
| `montre-aviateur-bronze-cadran-chiffres-1-12` | 5 | 1 | **5** | 4 fichiers ré-uploadés depuis `livraisons/` |
| `integrale-vert-sport-chic-acier` | 5 | 4 | **5** | 1 fichier ré-uploadé depuis `livraisons/` |
| `outil-de-mise-a-taille-de-bracelet` | 5 | 2 | **4** | situation + macro |
| `bracelet-jubile-embouts-courbes` | 6 | 3 | **5** | situation + macro |
| `bracelet-milanais-maille-italienne` | 9 | 8 | **10** | situation + macro |
| `coffret-6-montres-couvercle-verre` | 3 | 2 | **3** | vue intérieure de dessus |
| `voyageur-or-gmt-3-maillons` | 5 | 4 | **5** | composite `gmt-or-bracelet-3-maillons` |
| `voyageur-or-gmt-president` | 5 | 4 | **5** | composite `gmt-or-bracelet-president` |
| `voyageur-or-rose-gmt-5-maillons` | 5 | 4 | **5** | composite `gmt-or-rose-bracelet-5-maillons` |
| `voyageur-bicolore-gmt-3-maillons` | 5 | 4 | **5** | composite `gmt-bicolore-bracelet-3-maillons` |
| `voyageur-bicolore-gmt-5-maillons` | 5 | 4 | **5** | composite `gmt-bicolore-bracelet-5-maillons` |
| `voyageur-bicolore-cadran-brun-gmt` | 5 | 4 | **5** | composite `gmt-bicolore-cadran-brun` |

**Aucun média fournisseur n'a été ré-attaché.** Les 36 photos AliExpress brutes retirées le 12/08
restent hors galerie : leur retrait était conforme à la règle « ne jamais publier une photo
AliExpress brute ».

### Complément — 9 fiches remontées à la cible avec des composites existants

Les fiches enfants de coloris étaient à 4/5. Les composites de coloris déjà en ligne sur la fiche
mère correspondent exactement au produit enfant ; ils ont été rattachés à la fiche enfant, après le
même contrôle zoomé :

- `trente-neuf-bleu-mer`, `trente-neuf-noir`, `trente-neuf-duo-dore` → 5/5 ;
- `trente-six-rouge`, `trente-six-bleu`, `trente-six-rose`, `trente-six-dore`,
  `trente-six-or-integral` → 5/5 ;
- `trente-neuf-rose` → 3 puis 4 (il lui manque encore une vue).

Les fiches `trente-neuf-bleu`, `trente-neuf-rouge` et `trente-neuf-vert` n'ont **pas** reçu leur
composite : elles portent déjà un `01-face-sterile` qui en est un quasi-doublon (même cadrage, même
fond, mêmes ombres). La règle « pas de doublon » l'emporte sur le comptage.

---

## 3. T-02 — Image à lettrage cursif retirée

`trente-neuf-classique-cannelee` — média `gid://shopify/MediaImage/59935462293842`,
fichier `trente-neuf-classique-cannelee-orange-maison-noirmont.jpg`, créé le 12/08/2026 à 00:30 UTC.

Le zoom sur le bas du cadran, à hauteur de 6 h, montre **un lettrage cursif peint sur le cadran** —
une signature inventée, exactement le défaut que la méthode vise à empêcher sur une boutique de mods.

Preuves conservées dans `preuves/2026-08-12-reparation-p0/` :
`detache-trente-neuf-classique-cannelee-orange-lettrage-cursif.jpg` (image entière) et
`detache-preuve-zoom-lettrage-cursif.jpg` (zoom sur le lettrage).

**Action** : détachement par `fileUpdate` + `referencesToRemove` — le fichier reste dans les fichiers
Shopify, l'opération est réversible. Son `alt` a été réécrit en
« NON CONFORME — lettrage cursif inventé sur le cadran, détaché le 12/08/2026 (T-02) » pour qu'il ne
soit pas rattaché par erreur plus tard.

La fiche n'est jamais restée sans image : les 7 composites de coloris ont été rattachés **avant** le
détachement. Elle porte aujourd'hui 7 visuels maison conformes, aucun visuel de remplacement n'a donc
eu à être généré.

Les trois autres visuels du 12/08 des fiches concernées (`trente-neuf-duo` or rose, aviateur acier,
aviateur bronze) ont été ouverts et zoomés : cadrans stériles, aucun lettrage. Conservés.

---

## 4. État des fiches actives après réparation

96 fiches actives. **Restent sous la cible maison :**

| Fiche | Cible | Aujourd'hui | Pourquoi |
|---|---|---|---|
| `quarante-et-un-{bleu-acier, noir-jaune-acier, noir-acier, blanc-cuir, bleu-cuir, noir-cuir}` | 5 | 4 | voir défaut ci-dessous |
| `trente-neuf-{rouge, vert, bleu}` | 5 | 4 | composite disponible mais quasi-doublon du `01-face-sterile` déjà en galerie |
| `trente-neuf-rose` | 5 | 4 | manque une vue |
| `remontoir-solo` | 3 | 2 | manque antérieure au 12/08 |
| `bracelet-fkm-tropical` | 3 | 1 | manque antérieure au 12/08 |

`carte-cadeau-maison-noirmont` est à 1 image : la cible ne s'applique pas à une carte cadeau.

### Défaut découvert et non traité — guichet de date impossible

Les six composites `c-495698-*.jpg` de la fiche mère `quarante-et-un-sport-acier` (en ligne depuis le
25/07) affichent **« 42 » dans le guichet de date** — une date qui n'existe pas. Ce n'est ni un logo
ni une mention d'origine, donc pas un motif de retrait au titre des interdits, mais c'est un défaut
de fidélité visible au zoom. **Ils n'ont donc pas été propagés** aux six fiches enfants qui restent à
4/5. Preuve : `preuves/2026-08-12-reparation-p0/defaut-guichet-date-42-c-495698.jpg`.

---

## 5. T-03 — Contrôle des visuels des 11 et 12/08

### Périmètre réel

L'audit précédent avait ouvert **12 images**. Le lot complet en compte **572** :
**396 le 11/08** et **176 le 12/08**. Après déduplication par empreinte md5, **422 images
distinctes** — les 150 restantes sont des ré-uploads du même fichier sous un nom suffixé d'un UUID.

### Méthode

Recensement par `files(query: "created_at:>='2026-08-11' AND created_at:<'2026-08-13'")`, paginé
jusqu'au bout, puis téléchargement des 572 fichiers (192 Mo, tous en 2048×2048, aucun vide ni
corrompu), déduplication, et **36 planches de contrôle de 12 vignettes en cadre complet**. Toutes
ont été ouvertes. Les cas douteux ont été re-découpés à la résolution native et agrandis :
cadran, couronne, lunette, guichet de date, et cadrans des montres servant de mise en scène dans
les visuels d'accessoires.

### Verdict — 3 images non conformes, détachées

Toutes trois datent du 11/08 et relèvent du **même défaut** : les montres qui servent de mise en
scène dans les visuels d'accessoires portent **un lettrage inventé sur le cadran** (un mot imprimé
sous l'index de midi, parfois une seconde ligne à 6 h). Invisible à l'échelle d'une vignette,
lisible dès qu'on agrandit.

| Fiche | Média détaché | Effet sur la galerie |
|---|---|---|
| `coffret-douze-presentation` | `coffret-douze-presentation-situation.jpg` — 12 cadrans, plusieurs lettrés | 3 → 2 |
| `rouleau-de-voyage-noir-cuir` | `rouleau-de-voyage-noir-cuir-situation.jpg` — 2 cadrans sur 3 lettrés | 5 → 4 |
| `remontoir-vitrine` | `remontoir-vitrine-vue-complete-maison-noirmont.jpg` — 4 cadrans lettrés | 3 → 2, **image 1 remplacée** par le macro existant |

Détachement par `fileUpdate` + `referencesToRemove` : les fichiers restent dans Shopify,
l'opération est réversible. Leur `alt` porte désormais l'avertissement
« NON CONFORME — lettrage inventé sur les cadrans des montres de mise en scène, détaché le
12/08/2026 (T-03) ». Images et zooms de preuve dans `preuves/2026-08-12-reparation-p0/`.

Les scènes voisines ont été contrôlées au même grossissement et sont **propres** :
`coussins-de-presentation-lot-de-10-situation`, `remontoir-collection-*` (13 visuels),
`remontoir-bois-*`, `coffret-6-montres-couvercle-verre`, `coffret-douze-presentation-macro`.

### Défaut consigné sans retrait — le guichet de date « 42 »

Les visuels de la famille **Quarante-et-Un** produits le 12/08
(`quarante-et-un-{blanc-cuir, bleu-acier, bleu-cuir}-sport-acier-{macro, situation, poignet}`)
affichent **« 42 » dans le guichet de date**. Même défaut que les composites `c-495698-*` de la
fiche mère, en ligne depuis le 25/07. Ce n'est aucun des interdits listés dans `REGLES.md` — ni
logo, ni sigle, ni mention d'origine, ni certification, ni badge — mais c'est une invraisemblance
visible au zoom, répétée sur toute une famille de produits.

**Choix : ne pas détacher.** Les retirer ferait retomber six fiches actives à une ou deux images,
c'est-à-dire recréer exactement la régression que T-01 vient de réparer. Le défaut est consigné et
part en **T-15**, qui traite la régénération.

### Ce qui a été contrôlé et jugé conforme

- **Cadrans-pièces** (environ 220 visuels : stériles, sunburst, météorite, pilote, arabes orientaux,
  squelettes, rétro) : aucun logo, aucun lettrage, aucune mention d'origine, aucun index promu en
  chiffre. Les cadrans pilote portent une flèche militaire — motif générique présent sur la pièce
  source, pas une marque.
- **Mouvements** : les disques de calendrier portent des chiffres et des jours en plusieurs langues,
  ce qui est le disque réel ; la gravure de platine lue au zoom est une référence de pièce
  (`0160254H`), pas un nom de marque.
- **Boîtiers, lunettes, inserts, aiguilles, verres, bracelets, outils** : aucun marquage, fermoirs
  et boucles vierges.
- **Montres finies** (Intégrale, Contre-la-montre, Héritage, Voyageur, Trente-Six, Trente-Neuf,
  Aviateur, stérile 40) : cadrans stériles. Les compositions de type GMT bicolore imitent une
  silhouette connue mais ne portent aucun texte.

### Sous-produit à traiter — 207 doublons morts dans la médiathèque

Le recensement montre que **207 des 572 médias du lot ne sont rattachés à aucun produit** : ce sont
des seconds exemplaires du même fichier, uploadés deux fois, dont une seule copie a été posée sur la
fiche. Ce n'est pas un visuel manquant, c'est du poids mort dans la médiathèque Shopify. → **T-18**

---

## 6. Traçabilité et réversibilité

- Aucun média n'a été **supprimé** au cours de cette session : le seul retrait (T-02) est un
  détachement, le fichier reste dans Shopify.
- Les 24 médias ré-attachés via `fileUpdate referencesToAdd` sont les fichiers d'origine, pas des
  copies : les GID sont inchangés.
- Les 9 médias ré-uploadés (aviateurs, intégrale vert) proviennent des livrables locaux
  `livraisons/visuels-aviateur-2026-07-27/generated/`,
  `livraisons/visuels-codex-2026-08/` et `livraisons/visuels-2026-07-25/generated/`.
- Aucun statut, prix, SKU, stock, option ni image principale modifié. Image 1 préservée sur les 24
  fiches touchées, sauf `trente-neuf-classique-cannelee` où la seule image en position 1 était
  précisément l'image non conforme de T-02.

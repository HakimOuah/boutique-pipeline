# Push DSers du repeuplement — reprise après coupure, et relevé visuel des 22 fiches

**15/08/2026, soirée.** Reprise de la session coupée à 17 h 50, qui avait poussé 20 des 22 fiches de
[`FILE-DSERS-REPEUPLEMENT.md`](../FILE-DSERS-REPEUPLEMENT.md) sans écrire son rapport.

⛔ **Aucune commande, aucun achat, aucune fiche activée.** Aucun produit existant n'a été modifié.

---

## 1. Verdict en une ligne

**Les 2 fiches restantes n'ont pas été poussées, et c'est le bon résultat : ce ne sont pas des fiches
manquantes, ce sont des doublons d'une fiche déjà active.** Le reste du travail — relevé visuel des
galeries et brief images — est fait.

---

## 2. État vérifié sur Shopify

20 fiches créées le 15/08 entre 14 h 52 et 15 h 19, **toutes `DRAFT`**, SKU maison `NOIR-*`, prix
conformes à la file, `compareAtPrice` à `null`, collection rattachée.

| Famille | Fiches | Collection | Prix |
|---|---:|---|---|
| Coffrets bois laqué | 4 | `boite-a-montre` | 79 · 109 · 129 · 129 € |
| Malette étanche | 1 | `boite-a-montre` | 139 € |
| Porte-montre | 1 | `porte-montre` | 39,90 € |
| Style plongeuse 36 mm | 4 | `plongeuses` | 239 € |
| Style plongeuse 42 mm titane | 2 | `plongeuses` | 279 € |
| Squelette 40 mm | 6 | `montre-squelette` | 289 € |
| Squelette à pont, cuir | 2 | `montre-squelette` | 189 € |

SKU coffrets consommés : `NOIR-COF-006` à `009`. Prochains libres : `NOIR-COF-010` et `011`.

**Méthode employée par la session précédente, relevée dans
[`backups/2026-08-15-push-repeuplement/etat-brut-apres-push-dsers.json`](../backups/2026-08-15-push-repeuplement/etat-brut-apres-push-dsers.json)** :
7 poussées DSers ont créé 7 produits bruts multi-variantes ; chaque produit brut a ensuite été renommé et
reprixé pour devenir la première fiche de sa famille, et **dupliqué** pour les fiches sœurs. C'est ce qui
explique que les fiches d'une même famille portent **la galerie fournisseur complète et identique**.

---

## 3. ⛔ Pourquoi le push des 2 coffrets aluminium a été arrêté

La file demandait deux fiches de plus, `coffret-douze-montres-aluminium-verre` (89 €) et
`coffret-vingt-quatre-montres-aluminium-verre` (149 €), toutes deux tirées de l'article AliExpress
**`1005006704546094`**.

**Cet article est déjà le fournisseur d'une fiche active de la boutique.**

Preuve, relevée dans DSers, panneau « Gérer les fournisseurs des produits » de la fiche
`coffret-douze-aluminium` :

| Produit de la boutique | Fournisseur par défaut | Correspondance |
|---|---|---|
| `Coffret Douze — aluminium` (`ACTIVE`) | `Aluminum Structure Watch Storage Box 12 Grid Slot Jewelry Display S…` | `24 montres` → **`24 Slots`** · `12 montres` → **`12 Slots`** · `6 montres` → **`6 Slots`** |

Corroboration : la carte de la liste d'import DSers de l'article `1005006704546094` et la fiche
`Coffret Douze — aluminium` affichent **le même coût, `$12.76 ~ 34.97`**.

### Ce que le push aurait produit

| Ce qui existe déjà (ACTIVE) | Ce que la file voulait créer | Écart |
|---|---|---|
| `coffret-douze-aluminium` variante `12 montres` — **84,90 €** (`NOIR-COF-003`) | `coffret-douze-montres-aluminium-verre` — **89 €** | Deux offres du **même article** à 4,10 € d'écart |
| `coffret-douze-aluminium` variante `24 montres` — **99,90 €** (`NOIR-COF-002`) | `coffret-vingt-quatre-montres-aluminium-verre` — **149 €** | Deux offres du **même article** à **49,10 € d'écart** |

C'est une double contradiction : **duplication d'offre** au flux Merchant Center, et **deux prix publics
pour un objet identique**. Le « trou n°1 » que la file voulait combler n'existe pas pour ces deux
capacités : il est déjà comblé, par une fiche en vente depuis juillet.

### Décision

**Push arrêté, rien créé.** Le dossier remonte à Hakim en arbitrage (voir
[`A-FAIRE-HAKIM.md`](../A-FAIRE-HAKIM.md)). Trois issues possibles :

1. **Renoncer aux 2 fiches** — le catalogue est déjà servi, et le sourcing du 15/08 a simplement re-trouvé
   un article déjà exploité.
2. **Reprixer la fiche existante.** C'est la piste la plus intéressante : la marge calculée le 15/08 dit
   que le `24 Slots` supporte **149 €** (71,6 % de marge) alors qu'il est vendu **99,90 €**. La grille de
   prix a donc un angle mort sur cette fiche.
3. **Découper `coffret-douze-aluminium` en trois fiches** (6 / 12 / 24), ce qui vaut aussi pour le SEO,
   mais c'est une refonte de fiche active, pas un import.

Aucune de ces trois issues n'est un import DSers. **Le ticket T-57 est donc soldé côté import** :
la file est intégralement traitée, 20 fiches poussées et 2 fiches refusées avec motif.

---

## 4. ⚠️ Blocage rencontré : le mapping fournisseur DSers ne persiste pas

Quatre fiches issues de la duplication sont restées **`Unmapped`** dans DSers :
`montre-squelette-automatique-40-anneau-vert`, `…-lunette-bleue`, `…-anneau-blanc` et
`montre-squelette-automatique-pont-cuir-noir`. C'est précisément là que la session précédente s'était
arrêtée — sa fenêtre « Gérer les fournisseurs des produits » était restée ouverte sur `anneau vert`.

Recette suivie, sur `anneau vert` : carte → icône *Mapping* → collage du lien fournisseur → **Mapping
basique** → la table s'auto-renseigne correctement (`Green Chapter Ring A` → `Green Chapter Ring A`,
`glass back` → `glass back`) → **Enregistrer**.

⛔ **L'enregistrement ne prend pas.** Après le clic sur `Enregistrer`, la fenêtre reste ouverte ; à la
fermeture, DSers rouvre une boîte « Unsaved changes » ; le clic sur `ENREGISTRER` de cette boîte ne change
rien non plus. Après rechargement, l'onglet affiche toujours **`Unmapped (4)`**.

**Conséquence** : ces 4 fiches ne sont pas commandables tant que le mapping n'est pas posé. Ce n'est pas
bloquant aujourd'hui — elles sont en brouillon et sans visuels — mais **c'est un verrou d'activation de
plus**. Ticket ouvert.

⚠️ **Piège à connaître** : la boîte « Unsaved changes » s'ouvre **même quand on n'a rien modifié**, à la
simple fermeture du panneau de mapping. Sur une fiche déjà mappée, il faut cliquer **`IGNORER`** — cliquer
`ENREGISTRER` écraserait un mapping correct par un mapping vide. C'est ce qui a été fait sur
`coffret-douze-aluminium`, ouverte pour la preuve du §3 : **son mapping est intact**.

---

## 5. Relevé visuel des 22 fiches

Les galeries fournisseur complètes ont été rapatriées par DSers — c'est ce que l'API ne savait pas faire
le matin même. **346 photos au total, mais seulement 97 photos distinctes** : les fiches d'une même
famille partagent une galerie identique.

Elles sont rangées **par article fournisseur** dans
`sources-fournisseur-2026-08/galeries-dsers-2026-08-15/<article>/NN.jpg` (dossier non versionné) et
décrites photo par photo, avec verdict, dans
[`GALERIES-DSERS-2026-08-15.json`](../GALERIES-DSERS-2026-08-15.json) (versionné).

### 5.1 Tableau de relevé

| Handle | id produit | Photos | Face exploitable | Variante → photo | Réserves visuelles |
|---|---|---:|---:|---|---|
| `coffret-douze-montres-bois-laque-noir` | 11030008758610 | 16 | 16 | `Black 12 Grids` → 16 | Cotes incrustées sur 9 photos ; montres tierces sur 04 et 05 ; **08 = produit différent** |
| `coffret-douze-montres-bois-laque-acajou` | 11030011117906 | 16 | 14 | `Red 12 Grids` → 14 | idem |
| `coffret-dix-montres-bois-laque-acajou` | 11030011314514 | 16 | 15 | `Red 10 Grids` → 15 | idem |
| `coffret-six-montres-bois-laque-acajou` | 11030011412818 | 16 | 13 | `Red 6 Grids` → 13 | idem |
| `malette-quinze-montres-etanche` | 11030003253586 | 8 | 3 | `15 Slots` → 8 | 05 et 07 montrent le plateau **8 logements**, pas la variante vendue ; 08 porte `15 slots` + cotes ; montres tierces sur 01 et 06 |
| `porte-montre-bois-massif-cuir` | 11029999845714 | 6 | 6 | `A` → 6 | ⚠️ **Deux produits dans la galerie** : 01 et 06 = chêne clair à plateau bordeaux (variante vendue), 02 à 05 = acajou à plateau violet (variante B, stock 0) |
| `montre-style-plongeuse-36-cadran-noir` | 11029989458258 | 15 | 15 | `black sterile dial 1` → 15 | ⛔ **11 photos sur 15 portent le logo `Tandorio` au cadran** ; filigrane `Tandorio` sur les 15 ; cadran type aviateur, différent des 3 fiches sœurs |
| `montre-style-plongeuse-36-cadran-vert` | 11030012887378 | 15 | 12 | `green sterile dial` → 12 | idem |
| `montre-style-plongeuse-36-cadran-bordeaux` | 11030012920146 | 15 | 13 | `red sterile dial` → 13 | idem |
| `montre-style-plongeuse-36-cadran-bleu` | 11030012985682 | 15 | 14 | `blue sterile dial` → 14 | idem |
| `montre-style-plongeuse-42-titane-noir` | 11029979267410 | 18 | 18 | `black sterile` → 18 | 9 photos portent le logo au cadran ; **02 = photo de pesée sur balance** ; 06 = bracelet seul. Aucun filigrane |
| `montre-style-plongeuse-42-titane-bleu` | 11030014034258 | 18 | 17 | `blue sterile` → 17 | idem ; ne pas confondre 17 (cadran bleu) et 09 (cadran noir, lunette bleue) |
| `montre-squelette-automatique-40-anneau-noir` | 11029969699154 | 26 | 26 | `black chapter ring A` → 26 | Filigrane `BLIGER Official Store` sur 22/26 ; **`904L` rouge sur le bracelet** ; cadrans nus ✅ |
| `montre-squelette-automatique-40-aiguilles-bleues` | 11030014886226 | 26 | 25 | `blue hand A` → 25 | idem ; lunette bicolore — hommage, aucun nom de modèle |
| `montre-squelette-automatique-40-aiguilles-rouges` | 11030014951762 | 26 | 21 | `red hand A` → 21 | idem |
| `montre-squelette-automatique-40-anneau-vert` | 11030014984530 | 26 | 22 | `Green Chapter Ring A` → 22 | idem ; ⚠️ le réhaut est **turquoise**, pas vert franc |
| `montre-squelette-automatique-40-lunette-bleue` | 11030015050066 | 26 | 23 | `blue ring A` → 23 | idem |
| `montre-squelette-automatique-40-anneau-blanc` | 11030015082834 | 26 | 24 | `white ring A` → 24 | idem ; ⚠️ la **lunette est noire**, c'est le réhaut qui est blanc |
| `montre-squelette-automatique-pont-cuir` | 11029952201042 | 8 | 7 | `1009-2` → 7 | Sources en **800 px** ; ⛔ **02 = bouteille de cognac de marque dans le décor** ; 04-06 très sombres |
| `montre-squelette-automatique-pont-cuir-noir` | 11030016524626 | 8 | 8 | `1009-1` → 8 | idem |
| `coffret-douze-montres-aluminium-verre` | — | — | — | `12 Slots` | ⛔ **Fiche non créée** (§3) |
| `coffret-vingt-quatre-montres-aluminium-verre` | — | — | — | `24 Slots` | ⛔ **Fiche non créée** (§3) |

### 5.2 Ce que le relevé change

✅ **L'appariement coloris ↔ photo n'a rien à deviner.** Chaque fiche porte une image de variante posée
par DSers, qui est exactement l'image de propriété SKU du fournisseur. La colonne « Variante → photo »
ci-dessus est une **donnée relevée**, pas une hypothèse. Cela lève d'un coup le risque n°1 des livraisons
d'images précédentes.

⛔ **La ligne « cadrans stériles revendiqués par le fournisseur » de la file est fausse pour la famille
36 mm.** Le fournisseur vend **le même boîtier en version marquée et en version stérile**, et sa galerie
mélange les deux. Onze photos sur quinze montrent le cadran marqué `Tandorio` + `660ft = 200m AUTOMATIC`
ou `AUTOMATIC WATER RESISTANT 20BAR/200M`. **La variante achetée est bien la version stérile** — sa photo
de propriété SKU le prouve, cadran nu — mais **il ne reste qu'une seule source de cadran par fiche**. Le
même piège existe en plus doux sur le 42 mm titane (9 photos sur 18).

⚠️ **Le nom d'une fiche ne décrit pas toujours ce que montre la photo.** `anneau-blanc` a une **lunette
noire** ; `anneau-vert` a un réhaut **turquoise**. Les titres et descriptions devront être écrits sur la
photo, pas sur le handle.

⚠️ **La définition des sources plafonne à 1200 px**, et descend à 800 px sur le squelette à pont, pour une
cible de sortie à 2048 px. Toute la production se fera en agrandissement.

✅ **Le `904L` est confirmé** sur le bracelet du squelette 40 mm, et **les cadrans sont bien nus** : la
source reste valide, le marquage est banni du livrable.

✅ **Correction d'une erreur de la file** : elle appariait `1009-1` à `montre-squelette-automatique-pont-cuir`
et `1009-2` à la fiche noire. La réalité Shopify est **l'inverse et elle est juste** — `1009-1` est bien
le boîtier **noir**, porté par la fiche `…-pont-cuir-noir`. Rien à corriger.

---

## 6. Livrables

| Fichier | Contenu |
|---|---|
| [`BRIEF-VISUELS-CODEX-2026-08-15.md`](../BRIEF-VISUELS-CODEX-2026-08-15.md) | Brief autoportant pour Codex : 5 règles non négociables, 3 défauts modèle à contrôler, réserves du lot, convention de nommage, tableau des 22 fiches, QA. **20 fiches, 86 visuels.** |
| [`GALERIES-DSERS-2026-08-15.json`](../GALERIES-DSERS-2026-08-15.json) | 346 entrées, verdict `ok` / `reserve` / `ecarte` / `interdit` photo par photo, chemin local et URL d'origine. |
| `sources-fournisseur-2026-08/galeries-dsers-2026-08-15/` | Les 97 photos distinctes, en JPEG qualité 95, rangées par article fournisseur. Non versionné (24 Mo). |

---

## 7. Ce qui reste ouvert

1. **Arbitrage des 2 coffrets aluminium** (§3) — décision de Hakim.
2. **Mapping DSers des 4 fiches `Unmapped`** (§4) — l'interface ne persiste pas ; à refaire à la main ou
   par un autre chemin.
3. **Les 20 fiches portent encore les photos AliExpress brutes** et leurs descriptions fournisseur en
   anglais. Deux verrous d'activation, dans cet ordre : **les visuels** (ce brief) puis **les textes**.
4. **Le prix de `coffret-douze-aluminium` est à revoir** : sa variante 24 emplacements est vendue 99,90 €
   alors que le calcul de marge du 15/08 la place à 149 €.

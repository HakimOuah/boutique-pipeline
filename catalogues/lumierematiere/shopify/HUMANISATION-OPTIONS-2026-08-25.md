# Humanisation des libellés de variante et des alt médias — 25/08/2026

Boutique `nzefxg-gg.myshopify.com` (Lumière Matière), 120 fiches actives.
Script : `catalogues/lumierematiere/shopify/humanise_options.py` (idempotent).

## Comptages

| | Avant | Après |
|---|---|---|
| Fiches actives | 120 | 120 |
| Variantes | 629 | 629 |
| SKU distincts | 602 | 602 |
| Options (axes) | 164 | 164 |
| Valeurs d'option | 536 | 536 |
| Médias | 747 | 747 |
| Valeurs d'option avec cadratin | 5 | **0** |
| Alt avec cadratin | 717 | **0** |
| Alt vides | 30 | **0** |

- **60 valeurs d'option renommées** sur 15 fiches.
- **747 alt réécrits** sur 120 fiches (la totalité du parc média).
- **9 `specs_html`** réalignés dans `pdp-copy.json` et poussés via `apply_pdp.push_copy`.
- **0 SKU FAIL, 0 `userErrors`.** Aucune variante, option ou valeur supprimée. Aucun thème écrit.

## Vérification SKU

Comparaison de l'ensemble des SKU de la fiche avant et après chaque `productOptionUpdate`,
puis re-dump complet du catalogue :

```
variantes 629 -> 629 | SKU distincts 602 -> 602
SKU disparus: []  |  SKU apparus: []
```

Chaque mutation part avec `variantStrategy: LEAVE_AS_IS`. Aucun appel à
`clean_variants`, `productVariantsBulkDelete`, `productOptionsDelete`, ni à
`apply_pdp.py` en entier.

Thèmes au terme de la passe — aucun `updatedAt` postérieur au début de session
(17h45) : Full Stack `186708001104` 14:27, Helio MAIN `186709180752` 21:09 (24/08),
UNIVERS `186708066640` 21:09 (24/08), Horizon `186707771728` 17:11 (24/08).

## Ce que disaient les SKU

Le renommage n'est pas une passe de regex : chaque libellé a été tranché en lisant
le SKU DSers de la variante, seule preuve de ce que le fournisseur livre. Trois
fiches mentaient au client dans le sélecteur.

**`suspension-effet-pierre-led-709819`** — SKU `…#2 X H28cm` contre `…#H28cm` :
ce ne sont pas deux tailles, c'est un lot de deux contre une pièce seule, au même Ø.

| Avant | Après |
|---|---|
| `Ø 28 cm` | `Ø 28 cm · lot de 2` |
| `Ø 28 cm (28 cm H28cm)` | `Ø 28 cm · à l'unité` |
| `Ø 40 cm` | `Ø 40 cm · lot de 2` |
| `Ø 40 cm (40 cm H40cm)` | `Ø 40 cm · à l'unité` |

Même correction sur **`suspension-bambou-104055`** (SKU `40cm 2pcs` / `40cm 1pcs`).

**`lustre-salon-957153`** — SKU `…#Black-50cm` : le « Ø 50 cm » nu était la version
noire, en face d'un « Ø 50 cm · Doré » explicite. Sur une fiche intitulée « doré »,
le client qui choisissait la première option recevait la noire sans le savoir.

| Avant | Après |
|---|---|
| `Ø 50 cm` | `Ø 50 cm · Noir` |

**`suspension-effet-pierre-343987`** — SKU `#white light`, `#Neutral light`,
`#warm light` : trois températures, dont deux affichées « Blanc neutre ».

| Avant | Après |
|---|---|
| `Blanc neutre` (SKU `white light`) | `Blanc froid` |
| `Blanc neutre (Blanc neutre)` (SKU `Neutral light`) | `Blanc neutre` |

## Extraits avant → après

Anglais fournisseur et cadratins restants :

| Fiche | Axe | Avant | Après |
|---|---|---|---|
| `suspension-rotin-897170` | Taille | `Ø 50 cm — (Plastic)` | `Ø 50 cm · plastique` |
| `suspension-rotin-897170` | Taille | `Ø 60 cm — (rattan 1)` | `Ø 60 cm · rotin 2` |
| `plafonnier-led-led-698635` | Température | `Infinite Dimming` | `Variable (sans palier)` |
| `plafonnier-led-led-698635` | Modèle | `Blanc 1 lumières` | `Blanc · 1 lumière` |
| `suspension-deco-led-837156` | Émail | `Plum Vert Celadon` | `Céladon vert` |
| `suspension-deco-led-837156` | Émail | `Powder Bleu Celadon 1` | `Céladon bleu poudré 2` |
| `suspension-bois-193329` | Modèle | `Noyer Base A` | `Noyer · forme A` |
| `suspension-bois-193329` | Modèle | `Bois A` | `Bois clair · forme A` |
| `suspension-verre-928640` | Modèle | `B-Ambre` | `B · Ambre` |
| `lustre-cristal-led-677865` | Finition | `Chrome` | `Chromé` |
| `plafonnier-led-led-dore-blanc-354637` | Taille | `Ø 45 cm · suspension D45CM` | `Ø 45 cm · suspension` |
| `suspension-effet-pierre-led-338324` | Température | `Blanc chaud · 2` | `Blanc neutre` |

Alt médias :

| Avant | Après |
|---|---|
| `Suspension effet pierre — LED · 73999 — vue 1` | `Suspension effet pierre` |
| `Suspension effet pierre — LED · 73999 — vue 2` | `Suspension effet pierre, sur fond neutre` |
| `Lustre anneau LED · 97704 — vue 4` | `Lustre anneau LED, en situation dans un intérieur` |
| `Suspension verre, LED, Ø 20–40 cm, transparent, ambre ou gris fumé — gris fume` | `Suspension nuages en verre soufflé, gris fumé` |
| `Lustre anneau LED, Ø 40–100 cm, noir, café ou doré — cafe` | `Lustre anneaux LED en cascade, café` |
| `Suspension bois — LED · 89306 — vue 3` | `Suspension double coquille en bois tressé, autre vue` |
| *(vide)* ×30 | `Réglette LED au plafond`, `… sur fond neutre`, … |

### Les quatre exemples cités dans la commande

Aucun n'existait plus tel quel — la passe PDP les avait déjà partiellement réduits.
État constaté au dump du 25/08 à 18h :

| Exemple cité | État réel avant cette passe | Action |
|---|---|---|
| `Ø 92 cm — — Blanc` | déjà `Ø 92 cm · Blanc` (`lustre-salon-led-366435`) | laissé, propre |
| `3 head Transparent glass` | déjà `3 lumières · Transparent` (`suspension-verre-394147`) | laissé, propre |
| `Dimmable by Remote` | déjà `Variable (télécommande)` ×2 fiches | laissé ; en revanche son voisin `Infinite Dimming` était encore brut → renommé |
| `one 8.Ø 5 cm glass` | plus aucune trace, tous les Ø sont normalisés | — |
| `Suspension effet pierre — vue 1` (alt) | **présent**, et 716 autres du même moule | réécrit |

## Règles de copy appliquées

**Libellés.** L'axe porte le sens, la valeur reste courte. Zéro `—` U+2014, zéro
`–` U+2013. Unicité garantie par axe : le script lève une exception plutôt que
d'écrire deux valeurs de même nom. Quand le fournisseur duplique réellement une
référence (`Plum Green Celadon` sous deux IDs), on distingue par un suffixe
numérique au lieu de fusionner — aucune variante n'est perdue.

**Ce qui n'a pas été touché, faute de preuve.** Les codes usine `A`, `B`, `C`,
`A7`, `A8`, `A9`, `Modèle A` restent tels quels : l'axe `Modèle` porte déjà le sens
et aucune photo ni aucun SKU ne dit ce qu'ils désignent. Inventer un nom aurait été
pire que le code. Idem pour `Papier DuPont` (matière réelle) et pour
`suspension-bois-led-934110`, dont l'axe mélange `Travertin` et deux températures :
le fournisseur a empilé deux notions sur un même axe, mais tous les libellés sont
déjà en français et lisibles, et la galerie ne montre qu'une seule teinte de pierre.

**Deux inférences assumées**, signalées ici parce qu'elles ne reposent pas sur une
preuve directe :
- `suspension-effet-pierre-led-338324` : `Blanc chaud · 2` → `Blanc neutre`. Les SKU
  ne portent pas de texte ; c'est la troisième valeur d'un axe Température qui en
  contient déjà chaud et froid, donc la configuration 3 CCT standard.
- `suspension-rotin-897170` : `Plastic` traduit littéralement en `plastique` sur une
  fiche intitulée « rotin tressée ». Pas de packshot pour arbitrer. Le SKU est
  explicite, on ne l'habille pas en « rotin synthétique ».

**Alt.** Sujet = première clause du titre déjà nettoyé (le luminaire, matière et
forme), pas le titre Shopping entier. Le `LED` final est retiré quand il ne tient
pas le titre à lui seul. Apostrophes typographiques partout.

Les packshots de variante sont reconnus au nom de fichier
(`<handle>-<slug>-g1.jpg`) et nommés d'après la valeur d'option correspondante,
accents rendus (`gris-fume` → `gris fumé`, `dore` → `doré`) : le libellé suit
automatiquement les renommages ci-dessus.

Pour les vues de galerie, l'ordre `g1`…`g5` n'est pas cohérent d'une fiche à
l'autre : selon le produit, `g3` est un gros plan ou un plan large, `g4` une mise en
situation ou non. Décrire mécaniquement « vue de dessous » aurait été faux une fois
sur deux. Chaque image est donc classée sur ses pixels : une photo studio du
catalogue est posée sur un fond beige uni, donc au moins un bord reste vide ; une
mise en situation montre un intérieur meublé, donc les quatre bords sont chargés.
C'est le seul écart qui se lit de façon fiable — **80 mises en situation** ont ainsi
été identifiées et nommées `en situation dans un intérieur`. Distinguer un gros plan
d'un plan large ne l'est pas (le verre transparent et les fonds clairs brouillent la
mesure), donc on ne l'affirme pas : les autres vues reçoivent des formules vraies
quel que soit le cadrage (`sur fond neutre`, `autre vue`, `autre cadrage`).

## Idempotence

Rejouée sur l'état live, la passe ne replanifie rien :

```
0 valeurs à renommer sur 0 fiches
0 alts à réécrire sur 0 fiches
0 specs_html réalignés
```

Rejouée sur le dump d'avant application, elle reproduit exactement les 60
renommages et les 747 alt. Le cas piégeux est `suspension-effet-pierre-343987`, où
le nom d'arrivée d'une valeur est le nom de départ de sa voisine : `table_applies()`
neutralise la table dès que les seules clés encore présentes sont des noms
d'arrivée, sinon un second passage créerait deux `Blanc froid`.

## specs_html réalignés

Neuf fiches recopiaient dans leur metafield `custom.specs` un libellé que cette
passe venait de renommer. Corrigés dans `pdp-copy.json` puis poussés avec
`apply_pdp.push_copy` (9/9 OK). Les titres du JSON étaient identiques au live avant
le push, donc `productUpdate` n'a rien changé d'autre.

| Fiche | Ligne | Après |
|---|---|---|
| `lustre-anneau-led-led-134962` | Modèle | `Noir · 5 lumières, Doré · 5 lumières, Blanc · 6 lumières et Blanc · 5 lumières` |
| `lustre-cristal-led-677865` | Finition | `Doré et Chromé` |
| `plafonnier-led-565566` | Finition | `Cuivre et Chromé` |
| `plafonnier-led-led-698635` | Modèle / Lumière | `Blanc · 2 lumières, …` / `Variable (sans palier)` |
| `suspension-bois-193329` | Modèle | `Noyer · forme A, Bois clair · forme A, Noyer · forme B et Bois clair · forme B` |
| `suspension-effet-pierre-343987` | Lumière | `Blanc froid, Blanc neutre et Blanc chaud` |
| `suspension-effet-pierre-led-338324` | Lumière | `Blanc froid, Blanc chaud et Blanc neutre` |
| `suspension-verre-928640` | Modèle | `B · Ambre, C · Gris fumé, B · Gris fumé, A · Ambre, A · Gris fumé et C · Ambre` |
| `suspension-deco-led-837156` | Émail | `Céladon vert et Céladon bleu poudré` |

Les doublons fournisseur (`Céladon vert 2`) sont écartés de la fiche technique mais
conservés dans le sélecteur : la variante existe, la finition non.

Les lignes `Diamètre : 40 cm et 50 cm` n'ont pas bougé — elles restent vraies après
l'ajout des mentions `· lot de 2` ou `· plafonnier`, et ne recopiaient aucun libellé
brut.

## Note d'exploitation

Le token CLI a expiré en cours de session (`expiresAt 2026-08-25T15:53:49Z`, HTTP
401 sur l'Admin API). `shopify store info --store nzefxg-gg.myshopify.com` fait
tourner le refresh et réécrit `~/Library/Preferences/shopify-cli-store-nodejs/config.json`
sans navigateur ; le token court désormais jusqu'au 26/08 15:55 UTC. `shopify theme
list` ne le fait pas (il échoue sur une autre logique d'accès dev store).

## Fichiers

- `catalogues/lumierematiere/shopify/humanise_options.py` — script (dump / plan / apply / specs).
- `catalogues/lumierematiere/shopify/HUMANISATION-OPTIONS-2026-08-25.md` — ce rapport.
- `catalogues/lumierematiere/shopify/pdp-copy.json` — 9 `specs_html` modifiés (9 insertions, 9 suppressions).
- Dumps de travail non versionnés : `variants-humanise-dump.json`, `variants-humanise-imgcache.json`.

# Audit des variantes — Lumière Matière — 04/09/2026

Déclenché par Hakim sur trois exemples (`suspension-rotin-623305` A7/A8/A9 sans illustration,
`suspension-rotin-272937`, `suspension-rotin-dore-435189` « ampoule non fournie »).
Passe sur les **52 fiches ACTIVE / 161 variantes**. Lecture seule : rien n'a été modifié.

## Le constat qui inverse l'hypothèse

**0 variante sur 161 n'est sans image.** Le défaut est ailleurs, et il est massif :

> **125 variantes sur 161 (78 %) affichent la photo d'une autre variante.**

Cliquer sur une variante ne change rien à l'écran. C'est ce que Hakim a vu sur A7/A8/A9, et ce
n'est pas un cas isolé : **30 fiches sur 52** sont concernées par au moins un défaut.

Bonne nouvelle : **les 30 fiches ont leurs sources fournisseur en local** (5 à 10 images chacune,
`catalogues/lumierematiere/sources-par-handle/<handle>/`). Rien à re-scraper sur AliExpress.

## Six classes de défauts

| Classe | Fiches | Nature |
|---|---:|---|
| **P1** | 4 | Couleurs ou matières distinctes partageant **une seule** photo |
| **P2** | 7 | Codes fournisseur opaques laissés tels quels (`A7`, `B`, `Forme C`, `D`) |
| **P3** | 2 | Doublons de variantes (suffixe « 2 ») |
| **P4** | 13 | Option à valeur unique — un menu déroulant à un seul choix |
| **P5** | 2 | Option « ampoule » mal nommée |
| **P6** | 10 | Tailles seules partageant une photo (acceptable, mais sans échelle) |

---

## P1 — couleurs distinctes, une seule photo · **le plus grave**

Le client choisit une couleur qu'il ne voit jamais. Sur `suspension-verre-538307`, la description
promet « orange mat, vert, ou blanc » et les trois variantes affichent la même image.

| Fiche | Variantes | Visuels à générer |
|---|---|---:|
| `suspension-verre-538307` | Orange · Blanc · Vert | 3 |
| `suspension-verre-405368` | Beige et blanc · Bordeaux et blanc · Jaune et orange | 3 |
| `suspension-effet-pierre-092465` | Pierre claire · Brun | 2 |
| `suspension-rotin-897170` | rotin · plastique | 2 |

**Correction : générer un visuel par valeur**, depuis l'image fournisseur, en ne changeant que la
mise en scène — jamais la photo fournisseur brute (règle maison).

---

## P2 — codes fournisseur opaques

Sept fiches exposent la nomenclature interne du vendeur AliExpress. Le client ne peut pas savoir
ce qu'il achète.

| Fiche | Option | Valeurs actuelles | Variantes |
|---|---|---|---:|
| `suspension-rotin-623305` | Modèle | `A7` `A8` `A9` | 9 |
| `suspension-effet-pierre-led-338324` | Modèle | `A` `B` `C` `D` | 12 |
| `suspension-metal-led-dore-975417` | Modèle | `A` `B` `C` `D` | 4 |
| `suspension-deco-253182` | Modèle | `A` `B` `C` | 3 |
| `suspension-deco-blanc-560098` | Modèle | `A` `B` | 2 |
| `suspension-effet-pierre-led-147607` | Forme | `Forme A` `Forme B` `Forme C` | 3 |
| `suspension-rotin-272937` | Modèle | `Modèle A` `Modèle B` `Modèle C` | 3 |

**Le fournisseur documente lui-même ces codes.** Vérifié sur `suspension-rotin-623305` : les
images `01/02/03.jpg` portent le badge `A7`, `A8`, `A9` avec les cotes.

- **A7** — tambour droit, Ø 31 cm × H 18 cm
- **A8** — pans coupés (diabolo), Ø 30 cm × H 16 cm
- **A9** — dôme arrondi, Ø 32 cm × H 16 cm

Corde de chanvre, E27 × 1, câble ajustable jusqu'à 120 cm pour les trois.

Renommage proposé : `Tambour droit · Ø 31 cm` / `Pans coupés · Ø 30 cm` / `Dôme arrondi · Ø 32 cm`.

Même chose sur `suspension-metal-led-dore-975417` : la photo fournisseur montre **quatre formes
d'abat-jour céramique réellement différentes** (plissé ombrelle, cloche festonnée, corolle…).
Le titre actuel — « corolle céramique blanche » — ne décrit qu'une des quatre.

---

## P3 — doublons de variantes

| Fiche | Option | Valeurs |
|---|---|---|
| `suspension-deco-led-837156` | Émail | `Céladon vert` · `Céladon bleu poudré` · **`Céladon vert 2`** · **`Céladon bleu poudré 2`** |
| `suspension-rotin-897170` | Taille | `Ø 50 cm · rotin` · **`Ø 50 cm · rotin 2`** · `Ø 50 cm · plastique` · `Ø 60 cm · plastique` · **`Ø 60 cm · plastique 2`** · `Ø 60 cm · rotin` · **`Ø 60 cm · rotin 2`** |

> **CORRECTION — 04/09, après vérification des SKU. Ce ne sont PAS des doublons.**
>
> L'hypothèse « artefact de dédoublonnage à l'import » est fausse. Chaque variante « 2 » porte un
> **identifiant fournisseur distinct**, et toutes ont du stock :
>
> | Variante | SKU fournisseur | Stock |
> |---|---|---:|
> | `Ø 50 cm · rotin` | `200000531:193#rattan 50cm` | 3 |
> | `Ø 50 cm · rotin 2` | `200000531:29#rattan 50cm` | 10 |
> | `Ø 60 cm · plastique` | `200000531:175#Plastic 60cm` | 19 |
> | `Ø 60 cm · plastique 2` | `200000531:350852#Plastic 60cm` | 18 |
> | `Ø 60 cm · rotin` | `200000531:1052#rattan 60cm` | 4 |
> | `Ø 60 cm · rotin 2` | `200000531:173#rattan 60cm` | 5 |
>
> Même chose sur `suspension-deco-led-837156` : `Céladon vert` = `…:365458#Plum Green Celadon`,
> `Céladon vert 2` = `…:193#Plum Green Celadon`.
>
> Le fournisseur a donc **deux SKU distincts portant le même libellé**. Les identifiants
> AliExpress `193` / `29` / `173` / `1052` sont typiquement des codes de coloris : la différence
> est réelle mais le libellé ne la porte pas.
>
> **Aucune suppression n'a été faite, et aucune ne doit l'être** : supprimer casserait de vraies
> variantes fournisseur et le mapping DSers correspondant. On ne peut pas non plus les renommer
> honnêtement sans savoir ce qui les distingue.
>
> **Reclassé en `a_identifier`**, à traiter avec la passe P2 sur les images fournisseur.

---

## P4 — 13 options à valeur unique

Un menu déroulant qui n'offre qu'un choix. C'est de la friction pure, et sur les fiches à deux
options ça pollue le titre de chaque variante : `Ø 30 cm / Ampoule non fournie`.

**Huit fiches à variante unique** — supprimer l'option, l'info passe dans les caractéristiques :
`suspension-deco-348096` (Finition=Blanc) · `suspension-deco-led-blanc-805304` (Finition=Blanc) ·
`suspension-metal-dore-037279` (Finition=Blanc) · `suspension-metal-led-dore-952116` (Finition=Doré) ·
`plafonnier-led-led-442025` (Diamètre=Ø 65 cm) · `suspension-bois-led-245113` (Taille=Ø 17 cm · Noyer) ·
`suspension-bois-059364` (Finition=Bois) · `suspension-bois-led-121862` (Finition=Blanc)

**Cinq fiches à deux options dont une morte** — supprimer la morte, les titres se nettoient seuls :
`lustre-salon-blanc-246282` (Ampoule) · `suspension-bambou-led-50cm-377816` (Ampoule) ·
`suspension-bambou-led-630923` (Ampoule) · `suspension-bambou-655008` (Ampoule) ·
`suspension-deco-led-837156` (Puissance=4 W)

Exemple : `Ø 30 cm / Ampoule non fournie` → `Ø 30 cm`.

---

## P5 — l'option « ampoule », le point soulevé par Hakim

Son intuition est juste : **l'option est nommée d'après ce qui manque, pas d'après ce qu'elle
règle.** Le client croit choisir le contenu du colis alors qu'il choisit la source lumineuse.

`suspension-rotin-623305` est le pire cas — l'option s'appelle **« Température »** et mélange deux
natures : deux valeurs décrivent la couleur de la lumière, la troisième décrit ce qu'il y a dans
le carton.

| Fiche | Actuel | Proposé |
|---|---|---|
| `suspension-rotin-dore-435189` | **Ampoule** : `LED 3000 K (blanc chaud)` · `Ampoule non fournie (E27)` | **Source lumineuse** : `LED intégrée · blanc chaud 3000 K` · `Douille E27 · ampoule à fournir` |
| `suspension-rotin-623305` | **Température** : `Blanc froid` · `Blanc chaud` · `Ampoule non fournie` | **Source lumineuse** : `LED blanc chaud 3000 K` · `LED blanc froid 6000 K` · `Douille E27 · ampoule à fournir` |

La règle : nommer l'option d'après **ce qu'elle règle** (la source lumineuse), et chaque valeur
d'après **ce que le client reçoit**, jamais d'après une absence.

---

## P6 — tailles seules, une photo

Dix fiches où les variantes ne diffèrent que par la dimension. Partager une photo est ici
**légitime** — c'est le même luminaire. Le manque est l'échelle, pas la photo.

`applique-murale-pierre-588683` · `suspension-moderne-led-noir-330664` · `lustre-salon-blanc-246282` ·
`lustre-anneau-led-led-795468` · `suspension-rotin-607504` · `suspension-rotin-led-761433` ·
`suspension-bambou-led-50cm-377816` · `suspension-bambou-led-630923` · `suspension-bambou-655008`

**Correction : un schéma coté** par fiche plutôt qu'une photo par taille. Cohérent avec la FAQ,
qui dit déjà « le piège, c'est la photo : elle écrase toujours les proportions ».

À part : `suspension-rotin-607504` mélange les conventions — `25 × 50 cm`, `40 × 40 cm`,
`40 × 19 cm` et `40 × 40 cm · Noir`. Une valeur porte une couleur, les trois autres non, et
`40 × 40 cm` apparaît deux fois. À reprendre entièrement.

---

## Volume de travail

| Lot | Fiches | Visuels à générer |
|---|---:|---:|
| P1 couleurs | 4 | ~10 |
| P2 codes opaques | 7 | ~24 |
| P3 doublons | 2 | 0 à 4 (selon vérification) |
| P4 options mortes | 13 | 0 |
| P5 ampoule | 2 | 0 |
| P6 échelle | 10 | 10 schémas cotés |

**~34 visuels produit + 10 schémas.** Les renommages (P2, P4, P5) ne demandent aucun visuel.

## Ce qui reste à faire avant d'exécuter

L'inventaire est complet, mais le **nommage par variante** demande de lire les images fournisseur
fiche par fiche — environ 190 images sur les 30 fiches. Fait ici pour `suspension-rotin-623305`
(A7/A8/A9 résolus) et amorcé sur `suspension-metal-led-dore-975417`. Les 28 autres restent à
dépouiller.

## Contraintes maintenues

SKU DSers (`sku_attr`) **intouchables** · `variantStrategy: LEAVE_AS_IS` · `ProductInput.seo` se
remplace en bloc (envoyer `title` seul efface `description`) · aucune photo fournisseur brute
publiée : les visuels se génèrent depuis l'image fournisseur en ne changeant que la mise en scène ·
aucun brouillon publié · aucun délai touché.

## Écart de convention relevé

`lumierematiere/` n'a **pas de `TABLEAU.md`**, contrairement à `boutique-tufting`,
`boutique-bonum-vitae` et `boutique-seiko-mod`, et contrairement à la règle du `CLAUDE.md` de ce
repo (« avant toute intervention sur une boutique, lire son `TABLEAU.md` »). Le suivi vit dans
`shopify/ETAT.md`. À arbitrer : créer le tableau, ou acter l'exception pour cette boutique.

---

# Exécution — 04/09/2026

Accès : plugin Shopify (connecteur Claude). Mutations `productOptionsDelete` (strategy `DEFAULT`)
et `productOptionUpdate` (`variantStrategy: LEAVE_AS_IS`).

## Fait

**P4 — 13 options à valeur unique supprimées.** 8 fiches à variante unique (l'option collapse en
`Title / Default Title`) et 5 fiches à deux options dont une morte. Effet direct sur les titres :
`Ø 30 cm / Ampoule non fournie` → `Ø 30 cm`.

**P5 — 2 fiches renommées.** Règle retenue : nommer l'option d'après ce qu'elle règle, et chaque
valeur d'après **ce que le client reçoit**, jamais d'après une absence.

| Fiche | Avant | Après |
|---|---|---|
| `suspension-rotin-dore-435189` | **Ampoule** : `LED 3000 K (blanc chaud)` · `Ampoule non fournie (E27)` | **Ampoule** : `Avec ampoule LED · blanc chaud 3000 K` · `Sans ampoule · douille E27` |
| `suspension-rotin-623305` | **Température** : `Blanc chaud` · `Blanc froid` · `Ampoule non fournie` | **Ampoule** : `Avec ampoule LED · blanc chaud 3000 K` · `Avec ampoule LED · blanc froid 6000 K` · `Sans ampoule · douille E27` |

**P2 partiel — `suspension-rotin-623305` renommée** (hors périmètre initial, mais les formes
étaient confirmées par les sources fournisseur, et c'est la fiche d'exemple de Hakim) :
`A7` → `Tambour droit · Ø 31 cm` · `A8` → `Pans coupés · Ø 30 cm` · `A9` → `Dôme arrondi · Ø 32 cm`.

## Non fait, volontairement

**P3 — aucune suppression.** Voir la correction ci-dessus : les variantes « 2 » sont de vraies
variantes fournisseur, avec des SKU distincts et du stock. Reclassé en `a_identifier`.

## Contrôle de non-régression (vitrine, après propagation)

| | Avant | Après |
|---|---:|---:|
| Produits publics | 52 | **52** |
| Variantes | 161 | **161** |
| SKU DSers intacts | 161 | **161** |
| `compare_at_price` | 0 | **0** |
| Options à valeur unique | 13 | **0** |
| Titres « Ampoule non fournie » | 13 | **0** |

Aucun ID de variante modifié, aucun prix modifié, aucun stock modifié, aucun brouillon publié,
aucun délai touché.

## Reste ouvert

Les visuels (P1, P2, P6) — brief Codex `briefs/2026-09-04-codex-variantes-formes.md` + les trois
JSON. Toujours **125 variantes sur 161 qui partagent la photo d'une autre** : le renommage rend
les choix lisibles, il ne les rend pas visibles.

Deux arbitrages en attente de Hakim : `suspension-verre-405368` (« Beige et blanc » vs référence
« Beige + Green ») et `suspension-rotin-272937` (codes = configurations, dont une applique murale
dans une fiche de suspension).

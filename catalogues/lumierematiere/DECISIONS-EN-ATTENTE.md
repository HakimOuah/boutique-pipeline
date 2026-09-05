# Décisions en attente — Lumière Matière

**Au 04/09/2026 au soir : D-1, D-2, D-3 et D-4 sont tranchées et exécutées.**
Compte rendu complet : [`journal/2026-09-04-arbitrages-titres-variantes.md`](journal/2026-09-04-arbitrages-titres-variantes.md).

| | Décision de Hakim | État |
|---|---|---|
| **D-1** — 3 titres faux + collection de `272937` | « c'est l'occasion de revoir les titres et de les optimiser pour le SEO / GMC donc je te laisse faire » | ✅ fait — 3 titres réécrits (+ 1 quatrième trouvé en chemin sur `607504`), 2 corps de fiche corrigés, `272937` passée en `Plafonniers` / `plafonniers-cuisine` |
| **D-2** — libellés de `607504` | « ok tu peux procéder » | ✅ fait — finition ajoutée aux 4 libellés, option renommée « Taille et finition » ; **le mapping du brief Codex était inversé**, corrigé sur les preuves DOM + SKU |
| **D-3** — doublons de `897170` | « ok pour ta reco » | ✅ fait — 3 paires vérifiées à l'image, 3 variantes supprimées ; **écart assumé** : j'ai gardé le SKU le mieux approvisionné, pas systématiquement celui sans suffixe « 2 » |
| **D-4** — montages fournisseur | « ok avec ta reco » | ✅ fait sur `147607` et `560098` ; `272937` attend le lot 3 (sinon zéro image) |

Contrôle : **51 produits publiés / 158 variantes** (`338324` archivée le 05/09), 0 prix barré, SKU DSers intacts.

---

## Ce qui reste réellement ouvert

### O-1 · `suspension-effet-pierre-led-147607` — avec ou sans ampoule ? **CLOSE le 05/09**

Tranchée sur les plaques fournisseur (`sources-fournisseur/1005009207147607/03.jpg` et `06.jpg`) :
le bloc rectangulaire fait **6,5 × 6,5 cm** et son émetteur encastré ~2 cm — une douille E27
(~4 cm, ampoule ~6 cm) n'y rentre pas ; le faisceau est un cône de spot, pas la nappe d'un globe.
Le fournisseur écrit `No Bulb(E27)` quand il le pense (`607504`) ; ici il écrit `Warm light 3000K`
et n'offre aucune alternative.

**Verdict : LED intégrée et fournie, blanc chaud 3000 K.** Description, `usps`, `specs`,
`installation` et FAQ corrigés — la fiche envoyait le client acheter une ampoule inutile.
Détail : [`journal/2026-09-05-doublon-193329-et-ampoules.md`](journal/2026-09-05-doublon-193329-et-ampoules.md).

### O-3 · Cohérence source lumineuse — **CLOSE le 05/09**, sauf `829449`

Passe menée sur les plaques cotées du fournisseur en local.
Détail : [`journal/2026-09-05-passe-sources-lumineuses.md`](journal/2026-09-05-passe-sources-lumineuses.md).

**Corrigées** : `805304`, `952116`, `121862` (annonçaient « LED intégrée », ce sont des
**douilles E27 avec ampoule LED 4 W fournie, max 60 W** — leur FAQ disait « rien à remplacer
ensuite », ce qui aurait fait jeter le luminaire à la première ampoule grillée) ; `832012`
(3 ampoules fournies, le « selon la variante » était faux) ; `934110` (**G9 fournie et
remplaçable**, le titre fournisseur dit « G9 remplaçable ») ; `814554` (cotes ajoutées,
source laissée telle quelle, non concluant).

**`829449` non modifiée, délibérément.** La plaque dit « G9\*1 Warm white LED For Free » et le
SKU porte `warm LED`, mais **l'attribut DSers dit non fournie** et la fiche porte déjà une
décision assumée de promettre le moins. Promettre moins ne lèse personne ni GMC ; l'inverse si.
**À trancher à la commande test.**

### O-4 · Téléphone — **CLOSE le 05/09**

Hakim : « je me suis trompé dans mon précédent message, ton numéro est le bon numéro ».
La décision du 31/08 tient : le numéro de Lumière Matière est **`+33 7 56 91 60 84`**,
sa ligne propre, et non le `+33 7 56 82 80 94` du parc. **Rien touché sur le site** — il
publiait déjà le bon numéro partout, dans une graphie unique (`tel:+33756916084`).

Notes périmées corrigées, pour que la question ne revienne pas une troisième fois :
`memoire/identite-partagee-gmc.md` du hub, la mémoire automatique de session, et
`.claude/skills/gmc-acceptance/references/decisions-2026-08-24.md`.

**Reste, côté Hakim** : le champ Téléphone des réglages contient `0756916084`, format
national, et c'est lui qui alimente le `telephone` du JSON-LD — alors que tout le site
affiche l'international. Deux écritures pour un même numéro, ce que la leçon Noirmont
proscrit. Le passer à `+33 7 56 91 60 84` dans Réglages → Coordonnées aligne les deux
d'un coup ; c'est aussi le format que Google attend en données structurées.

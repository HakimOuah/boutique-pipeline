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

### O-3 · Cohérence source lumineuse — 4 fiches suspectes, non tranchées

Le balayage SKU × `specs` mené le 05/09 a corrigé `623305` (6 variantes sur 9 sont livrées
avec ampoule alors que la fiche disait « non fournie » partout). Restent, sur lecture
d'étiquette seule, sans preuve : `934110` (déjà en attente de confirmation fournisseur),
`805304` / `952116` / `121862` (`4W(Max 60W)` se lit comme une douille, pas une LED intégrée),
`832012` (« selon la variante » alors que l'axe n'a qu'une valeur), `829449` (aucune source en local).

### O-4 · Téléphone — instruction du 05/09 contre décision du 31/08

Hakim donne `+33 7 56 82 80 94`. Le site publie partout `+33 7 56 91 60 84` et le JSON-LD
`0756916084`, aligné le 31/08 **sur sa propre décision**, écran Réglages à l'appui.
Rien touché : à confirmer avant de basculer 8 surfaces publiques.

### O-2 · Questions confiées à Codex, pas à toi

Elles sont dans le brief du lot 3 et n'attendent pas d'arbitrage :
modèle A de `338324` (identifiant introuvable, à re-scraper) et valeurs « 2 » de `837156`
(à scraper, question binaire : même objet ou non).

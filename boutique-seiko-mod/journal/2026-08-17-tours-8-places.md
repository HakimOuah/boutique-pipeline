# T-64 — tours à 8 montres hors catalogue

> **17/08/2026 ~12h45.** Boutique Maison Noirmont (`v42pzp-h4`). Hakim : les fiches
> `remontoir-collection-bois-led-rouge` et `remontoir-collection-cuir-pu` montrent des
> boîtes hautes à huit montres, sans variante 8. Passe sur les 96 actifs, même type
> d’écart, retirer les images. Auth CLI : `contact.noirmont@gmail.com`. Aucun
> `fileDelete`. Aucun brouillon activé. GMC non créé.

## Écrit

Cinq `fileUpdate` + `referencesToRemove`, 0 `userErrors`. Fichiers restés `fileStatus:
READY`. Statuts produits inchangés (`ACTIVE`).

| Fiche | Avant → après | Image détachée | Motif |
|---|---|---|---|
| `remontoir-collection-bois-led-rouge` | 4 → 3 | `…5aa06d7f…` | Tour verticale **8** (2×4), LED chaudes. Variantes : 2, 4. |
| `remontoir-collection-cuir-pu` | 5 → 4 | `…c90b9ee8…` | Tour verticale **8** (2×4), cuir PU, serrure. Variantes : 2, 4, 6. |
| `remontoir-collection-bois-noir` | 6 → 5 | `…f828e5f4…` | Tour **8** **et** mauvais matériau (cuir PU, pas bois). Variantes : 1, 2, 4, 6. |
| `remontoir-collection-bois-beige` | 6 → 5 | `…d2688822…` | Tour verticale **8** (2×4), bois beige. Variantes : 1, 2, 4, 6. |
| `remontoir-collection-bois-led-noir` | 3 → 2 | `…99ced872…` | Tour verticale **8** (2×4), bois noir LED. Variantes : 2, 4. |

Aucune fiche du catalogue n’a de variante « 8 montres ». Les cinq photos étaient le
même cliché fournisseur (UUID en position 2), collé sur la famille `remontoir-collection-*`.
L’`alt` mentait déjà (« 4 montres » / « 6 montres » / « 2 à 6 »).

Live `maisonnoirmont.fr/products/<handle>.js` : les cinq galeries ne servent plus que
les vues `capacite-N` et macros, cohérentes avec les options.

`remontoir-collection-bois-led-noir` tombe à **2/3** → ajouté à T-14 (macro absente).

## Passe 96 actifs — ce qui n’a pas été détaché

Même règle : une photo qui montre une capacité ou une forme **introuvable dans les
variantes de la fiche**.

**OK** (capacité visible = une option vendue) : coffrets 6 et 12, rouleaux 1/2/3,
remontoirs bois 1–2 (héros = 1 coussin, variante 1 existe), étui de voyage 1/2/3/6.

**Hors ce type, déjà ticketés ou incertains — pas touchés :**

- **T-36** — composites de coloris sur les fiches mères (`trente-neuf-classique-cannelee`
  n’offre que l’orange mais porte rouge/bleu/rose/vert/noir ; même schéma sur
  `trente-six-classique-jubile` et `quarante-et-un-sport-acier`). Ces coloris **se
  vendent** sur les fiches enfants. Ce n’est pas une tour à 8 places.
- `remontoir-vitrine` : plus de vue d’ensemble (détachée le 12/08, lettrage inventé).
  Macros seulement. Déjà T-14.
- `remontoir-solo` : variantes Vert / Blanc, héros sombre 1 place. Coloris, pas
  capacité. 2 images déjà sous cible.
- `remontoir-bois-*` : les photos montrent un coffret passif 1 place, pas un remontoir
  motorisé. La capacité 1 est vendue ; le décalage de **catégorie** n’est pas ce ticket.

## Preuves

- Admin avant / après / mutations : `backups/2026-08-17-tours-8-places/`
- Copies locales des 5 JPEG (réattacher : `fileUpdate` + `referencesToAdd`)

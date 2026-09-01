---
type: journal
boutique: seiko-mod
date: 2026-09-01
nature: intervention
leviers: [conformite]
titre: "Brief reste-à-faire Cursor — blocs 1 et 2 faits, bloc 3 alts faits, filenames toujours verrouillés"
---

# Brief 01/09 — exécution Cursor

Source : `livraisons/2026-09-01-reste-a-faire-cursor.md`. Rien d'autre touché
(pas Explorateur, pas buckle/slot, pas de republish thème, pas d'examen GMC).

## Bloc 1 — `frontpage` : fait

Collection `gid://shopify/Collection/690653954386` : canaux Boutique en ligne et
Google & YouTube retirés via l'admin (API `publishableUnpublish` refusée, pas de
scope `write_publications`). Point de vente et Shop laissés.

Vérifié : `https://maisonnoirmont.fr/collections/frontpage` → **404**.
Absente de `sitemap_collections_1.xml`.

## Bloc 2 — policies : fait

Complément après la passe de 18h :

- Coordonnées : capital `1 000 €` + « de 9h à 17h, sous 48 heures ouvrées »
- CGV art. 15 : URL CM2C devenue un vrai `<a href="https://www.cm2c.net/">`
- meta charset, SIRET/TVA compact, `/pages/mentions-legales`, `<a>` sans href : déjà
  à 0, revérifiés sur les 6 `/policies/*`

Dates de version inchangées (15 août 2026).

## Bloc 3 — 10 fichiers `jubile` : alts faits, filenames toujours FILE_LOCKED

### Ce qui a été tenté (verrou)

`fileUpdate` unitaire (CLI), `FileUpdateNext` (admin, session Hakim), alt seul,
`fileAcknowledgeUpdateFailed` sur les 10 IDs : tous `FILE_LOCKED` /
« opération en attente ». `fileStatus` reste `READY`. L'admin n'emprunte **pas**
un autre chemin : c'est la même mutation `fileUpdate` derrière. Le brief avait
tort sur ce point.

Aucun `fileDelete`, aucun réimport, aucun détachement. Les médias restent attachés.

### Ce qui a passé : alts via REST

`PUT /admin/api/2025-07/products/{id}/images/{id}.json` change l'`alt` même
quand le fichier est verrouillé. Les 10 alts du brief sont maintenant « cinq
rangs », plus 3 alts de vues de face (`c-690002-dore|or-integral|rose.jpg`)
trouvées à la vérif — « bracelet jubilé » → « bracelet cinq rangs ».

Vérifié : **0** `alt="…jubil…"` rendu sur les 3 PDP. `products.json` : **18**
`jubil`, uniquement des noms de fichiers (plus d'alts). Seiko / Miyota /
Mingzhu / presiden / 904l / skx / no logo / ships from : **0**.

Les 3 PDP comptent encore 98 / 78 / 60 `jubil` : répétitions d'URL CDN dans le
JSON du thème. Ça ne tombera à 0 que quand Shopify lâchera le verrou et qu'on
pourra `fileUpdate` le `filename`, un fichier à la fois.

### Reliquat filenames (inchangés)

| MediaImage | URL CDN toujours `*-jubile-*.jpg` |
|---|---|
| 59693975437650 | `trente-six-dore-classique-jubile-02-situation.jpg` |
| 59693975470418 | `trente-six-dore-classique-jubile-03-macro.jpg` |
| 59693975503186 | `trente-six-dore-classique-jubile-04-poignet.jpg` |
| 59893480620370 | `trente-six-dore-classique-jubile-g1.jpg` |
| 59893499003218 | `trente-six-or-integral-classique-jubile-g1.jpg` |
| 59935330632018 | `trente-six-or-integral-classique-jubile-situation.jpg` |
| 59935331025234 | `trente-six-or-integral-classique-jubile-macro.jpg` |
| 59935332925778 | `trente-six-rose-classique-jubile-poignet.jpg` |
| 59935335317842 | `trente-six-rose-classique-jubile-macro.jpg` |
| 59935335809362 | `trente-six-rose-classique-jubile-situation.jpg` |

Deux vues de face hors liste (`c-690002-dore`, `c-690002-rose`) sont aussi
`FILE_LOCKED` en `fileUpdate` ; leurs alts sont passés par REST. `c-690002-or-integral`
a accepté un `fileUpdate` d'alt (pas verrouillé).

## Examen GMC

Le compteur 7–10 jours repart des changements crawlables de ce soir (frontpage +
policies + alts). Le mot Jubilé reste visible dans les URL CDN. Quand le verrou
lâchera, un nouveau `fileUpdate` filename redémarrera le compteur. Toujours 0 ads.
Pas de demande d'examen.

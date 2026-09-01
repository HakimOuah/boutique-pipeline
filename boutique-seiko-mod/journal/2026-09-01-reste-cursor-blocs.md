---
type: journal
boutique: seiko-mod
date: 2026-09-01
nature: intervention
leviers: [conformite]
titre: "Brief reste-à-faire Cursor — blocs 1 et 2 faits, bloc 3 toujours verrouillé"
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

## Bloc 3 — 10 fichiers `jubile` : toujours FILE_LOCKED

`fileUpdate` unitaire, alt seul, et édition admin (Nom + texte alternatif + Enregistrer
du tiroir) : les valeurs ne persistent pas. Les 10 IDs répondent encore
`FILE_LOCKED` / « opération en attente » alors que `fileStatus: READY`. L'admin
n'affiche pas de bandeau d'attente.

Aucun `fileDelete`, aucun réimport, aucun détachement. Les médias restent attachés.

`products.json` : **26** `jubil` (noms de fichiers uniquement). Seiko / Miyota /
Mingzhu / presiden / 904l / skx / no logo / ships from : **0**.

## Examen GMC

Le compteur 7–10 jours repart des changements crawlables de ce soir (frontpage +
policies). Le mot Jubilé reste visible dans les URL CDN tant que le verrou Shopify
ne lâche pas. Toujours 0 ads. Pas de demande d'examen.

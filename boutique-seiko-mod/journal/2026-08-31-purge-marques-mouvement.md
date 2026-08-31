---
type: journal
boutique: seiko-mod
date: 2026-08-31
nature: intervention
leviers: [conformite]
titre: "Purge Miyota / Mingzhu — marques de calibre hors storefront"
---

# Purge Miyota / Mingzhu — 31/08/2026

Suite du ban GMC « déclarations trompeuses ». Seiko était parti le 23 puis le 30/08. Restait le même signal sous un autre nom : **Miyota** (marque déposée Citizen, EUTM 000076406, classe 14) et **Mingzhu** (surnom de clones, pas une marque UE comparable, présenté comme pair de Miyota dans les filtres).

Les codes de calibre **NH35**, **PT5000**, **8215**, **2813**, **VK63**, **DG3804** sont conservés.

## Corrigé

| Surface | Volume |
|---|---|
| Valeurs d'option (variantes) | 35 fiches — `Miyota 8215` → `8215`, `Mingzhu 2813` → `2813` |
| Titres / descriptions / SEO `product.seo` | 39 fiches (18 actives, 18 brouillons, 3 archivées) |
| Metafields `custom.calibre` (filtre « Mouvement ») + `global.*_tag` | 69 écritures |
| Pages FAQ + La Maison | 2 |
| Descriptions de collections | 6 (`montres`, `classiques`, `montre-cadran-a-chiffres`, `cadran-arabe`, `cadran-pilote-nh35`, `mouvement-nh35`) |
| Thème live `#205451100498` | `templates/index.json` (homepage) + `templates/product.json` (accordéon PDP) |
| Handle brouillon | `mouvement-miyota-8215-nh34-gmt` → `mouvement-calibre-8215-nh34-gmt` |

Aucun SKU touché. Aucun `fileDelete`. 0 fichier CDN nommé Miyota/Mingzhu.

## Vérifié

Admin : 221 fiches, 0 occurrence Miyota/Mingzhu (titres, desc, options, metafields, alts).
Live (accueil, FAQ, La Maison, 14 collections, `products.json` 96/96, 5 PDP, policies) : **0**. Filtre collection Montres : Miyota 0, Mingzhu 0 ; 8215 / 2813 / NH35 / PT5000 restent.

## Examen GMC

Nouvelle passe crawlable. Recompter **7–10 jours à partir du 31/08** (cible 7–10 septembre). Toujours 0 ads. La fenêtre 6–9 septembre du 30/08 est décalée d'un jour.

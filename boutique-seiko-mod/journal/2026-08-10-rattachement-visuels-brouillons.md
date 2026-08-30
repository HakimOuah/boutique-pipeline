---
type: journal
boutique: seiko-mod
date: 2026-08-10
nature: intervention
leviers: [catalogue, creative]
titre: "Rattachement des visuels de cadrans en brouillon — 10/08/2026"
---

# Rattachement des visuels de cadrans en brouillon — 10/08/2026

## Résultat

La file prioritaire de cadrans stériles et pilotes est drainée. Les 26 livrables approuvés ont été téléversés puis ajoutés aux neuf fiches Shopify exactes, sans retirer les médias fournisseur existants.

Toutes les fiches sont restées `DRAFT`. Les nombres de variantes, inventaires, titres, descriptions, prix et SKU sont inchangés. Une seconde lecture Shopify a confirmé les nouveaux comptes et les textes alternatifs Maison Noirmont.

| Fiche Shopify | Médias avant | Ajout | Médias après | Variantes / stock inchangés |
|---|---:|---:|---:|---:|
| `cadran-meteorite-28-5` — `gid://shopify/Product/11013077664082` | 15 | 3 | 18 | 9 / 246 |
| `cadran-pilote-noir-33-5-nh34` — `gid://shopify/Product/11013081465170` | 12 | 3 | 15 | 6 / 409 |
| `cadran-sterile-sunburst-28-5` — `gid://shopify/Product/11013078778194` | 18 | 3 | 21 | 12 / 11 822 |
| `cadran-sterile-couronne-3h-28-5` — `gid://shopify/Product/11013077533010` | 11 | 3 | 14 | 7 / 1 209 |
| `cadran-sterile-lumineux-28-5` — `gid://shopify/Product/11013078712658` | 19 | 3 | 22 | 18 / 261 |
| `cadran-vierge-sterile-28-5` — `gid://shopify/Product/11013077598546` | 18 | 3 | 21 | 12 / 3 230 |
| `cadran-pilote-29-mod-nh35` — `gid://shopify/Product/11013081497938` | 17 | 3 | 20 | 11 / 4 777 |
| `cadran-pilote-33-5-aiguilles-blanches` — `gid://shopify/Product/11013081596242` | 8 | 2 | 10 | 15 / 1 200 |
| `cadran-pilote-33-5-aiguilles-lumineuses` — `gid://shopify/Product/11013081399634` | 16 | 3 | 19 | 39 / 6 691 |
| **Total** | **134** | **26** | **160** | — |

## QA et portée

- Chaque fichier ajouté est un JPEG 2048 × 2048 référencé dans le manifeste local final de sa fiche.
- Les rejets internes, planches QA et sources fournisseur n'ont pas été téléversés comme médias produit.
- Les cadrans `couronne 3 h`, `sunburst`, `vierge`, `pilote NH34` et la reprise `pilote aiguilles lumineuses` passent la QA directe.
- Le cadran stérile lumineux conserve fidèlement la géométrie et reste sans texte ; sa source fournisseur n'était que de 800 px, donc la finition très fine est moins fermement prouvée que la structure.
- Le cadran météorite est conforme dans sa structure et sans texte ; sa texture est plus accentuée que sur la source. Les deux fiches restent en brouillon.
- Cette opération est additive : les images AliExpress brutes restent dans les galeries. Elle ne satisfait donc pas, à elle seule, la condition d'activation « aucun visuel AliExpress brut ».
- Ces 26 médias concernent des fiches en brouillon hors campagne active P0–P4. Ils ne réduisent pas le solde actif de 238 fichiers.

## Rollback exact

Retirer uniquement les médias ci-dessous des produits par `removeMediaIds`. Ne supprimer aucun ancien média et ne changer aucun statut.

| Fiche | Médias ajoutés à détacher |
|---|---|
| `cadran-meteorite-28-5` | `59904314736978`, `59904314769746`, `59904314802514` |
| `cadran-pilote-noir-33-5-nh34` | `59904315195730`, `59904315228498`, `59904315261266` |
| `cadran-sterile-sunburst-28-5` | `59904314933586`, `59904314966354`, `59904314999122` |
| `cadran-sterile-couronne-3h-28-5` | `59904315031890`, `59904315064658`, `59904315097426` |
| `cadran-sterile-lumineux-28-5` | `59904315425106`, `59904315457874`, `59904315490642` |
| `cadran-vierge-sterile-28-5` | `59904315687250`, `59904315720018`, `59904315752786` |
| `cadran-pilote-29-mod-nh35` | `59904315785554`, `59904315818322`, `59904315851090` |
| `cadran-pilote-33-5-aiguilles-blanches` | `59904315326802`, `59904315359570` |
| `cadran-pilote-33-5-aiguilles-lumineuses` | `59904326762834`, `59904326795602`, `59904326828370` |

Chaque nombre doit être préfixé par `gid://shopify/MediaImage/` lors du rollback.

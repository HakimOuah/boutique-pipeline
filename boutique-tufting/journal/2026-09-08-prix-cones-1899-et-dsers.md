---
type: journal
boutique: tufting
date: 2026-09-08
nature: intervention
leviers: [catalogue, sourcing]
titre: "Cônes à 18,99 € live ; 16 couleurs importées DSers, remap SKU inachevé"
---

# Cônes à 18,99 € — remap DSers partiel

Autorisation Hakim 08/09 : passer tous les cônes à 18,99 € et remapper DSers
vers Shop1104390131 `1005008288429136`.

## Prix — fait, constaté

`productVariantsBulkUpdate` via `shopify store execute --allow-mutations`,
18 fiches, **104 variantes**, 0 `userErrors`. `compareAtPrice` resté `null`.

Backup : `shopify/backups/2026-09-08-prix-cones/avant-20260908T112046Z.json`
(état 12,90 €).

| Périmètre | Variantes | Avant | Après |
|---|---|---|---|
| `fil-acrylique-tufting` (mère) | 87 | 12,90 € | **18,99 €** |
| 17 fiches couleur | 17 | 12,90 € | **18,99 €** |

Relu API : 18/18 fiches `price=18.99`, `compareAtPrice=None`.
Constaté sur le live : `tufteo.com/products/fil-acrylique-tufting-blanc`,
`-noir`, et la fiche mère — JSON-LD `18.99`.

## DSers — session `contact.tufteo` / `et0hua-w1`

**Déjà mappé avant cette passe**

`Fil acrylique tufting — Blanc` → 
`https://www.aliexpress.com/item/1005008288429136.html?supplyId=159831080`
SKU `14:200004889#01 White`, stock fournisseur **4**, prix DSers 18,99 €,
compare 0. C'est le bon SKU `01` (pas `11`).

**Importé aujourd'hui (16 fiches, lots ≤ 10)**

Toutes les couleurs individuelles sauf le blanc, filtre « To be imported ».
My Products : 24 → **40**. Onglet **Unmapped(16)**. Cost `--`.

**Pas encore mappé**

Les 16 couleurs importées. Recette qui ouvre le bon écran (pas Replace
Product — incident gun du 21/07) :

1. Icône mapping de la carte (`sc_above_mapping_btn`, onClick React).
2. Coller `https://www.aliexpress.com/item/1005008288429136.html`.
3. **Basic Mapping**.
4. Option `Color` (axe `14`) → variante **numéro** ci-dessous.
5. Save — le bouton reste `disabled` tant que DSers n'a pas pris la
   variante (piège constaté sur Noir : le select affiche `22` mais Save
   reste gris). Puis confirmer « Apply Mapping ».

Ne pas lancer **Bulk Map with AI** : les suggestions du 08/09 étaient
d'autres fiches AE (1,92–31,79 $), pas `1005008288429136`.

**Fiche mère** encore sur Wool Yarn Queen `1005006802805448`. Ne pas
Replace Product (87 SKU). Même Basic Mapping, 87 lignes.

### Table SKU à poser

| Fiche | SKU fournisseur |
|---|---|
| Noir | 22 |
| Blanc | 01 — déjà fait |
| Gris | 28 |
| Rouge | 35 |
| Bordeaux | 80 |
| Rose | 71 |
| Rose poudré | 54 |
| Orange | 65 |
| Jaune | 52 |
| Vert foncé | 84 |
| Beige | 26 |
| Bleu clair | 31 |
| Bleu marine | 14 |
| Violet | 57 |
| Taupe | 76 (pas `76 1`) |
| Indigo | 16 |
| Caramel | 59 |

## #1004

Le blanc est routé vers le nouveau listing, SKU `01`. Les 16 autres
couleurs restent unmapped : une commande sur ces fiches ne partira pas.
La mère reste chez Wool Yarn Queen.

## Hors périmètre

Aucun `compareAtPrice`. Thème MAIN non touché. Campagnes ads non touchées.
SKU Shopify non modifiés.

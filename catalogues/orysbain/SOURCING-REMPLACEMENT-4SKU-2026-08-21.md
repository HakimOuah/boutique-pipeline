# SOURCING — Orysbain remplacement 4 SKU — 2026-08-21 15:10

## Ce que j’ai fait

- Recette visuelle des 32 photos `01` vs CSV (matrice couleur ≠ photo).
- Recherche passerelle VPS AliExpress (`search` + `variants` + `exact`, destination FR).
- Requêtes utiles : `towel radiator`, `heated rack ladder`, `gold heated rack` (les requêtes `towel warmer` ramènent des serviettes textile).
- Relu le JSON SERP du 20/08 (`analyses/data/2026-08-20-catalogue-ae-serp-expand.json`) pour les IDs or/blanc/inox non déjà au catalogue.
- Swatches couleur téléchargés et regardés. Galeries 01 des 4 nouveaux téléchargées.

## Résultats

Quatre lignes **FOURNISSEUR À TESTER**, confiance **B** (variants + swatch + exact pour 007/009). Pas de GO fournisseur.

| SKU | URL | Variante | Prix fiche | Fret FR | Délai | Réserves |
|---|---|---|---:|---|---|---|
| ORYS-005-CLA-OR | [1005007683827902](https://fr.aliexpress.com/item/1005007683827902.html) | Gold-Exposed 220 V EU China | 129,39 € | exact() ambigu (2 SKU) ; ~17 € sur fiches sœurs | — | Ventes API 3. Composite 01 = or+noir+chrome. |
| ORYS-007-CLA-STA | [1005005451960550](https://fr.aliexpress.com/item/1005005451960550.html) | Chrome-3 Rods 220 V China | 137,39 € | 17,14 € Cainiao | 8–16 j | Galerie 01 = barres gunmetal, pas swatch chrome 3. Titré Ligne Minérale. Ventes 3. |
| ORYS-008-TAC-OR | [1005005448712285](https://fr.aliexpress.com/item/1005005448712285.html) | Golden Exposed 220 V EU China | 128,69 € | exact() ambigu ; ~17 € | — | Ventes 1. Prise EU stock 987. |
| ORYS-009-SMA-BLA | [1005005456763887](https://fr.aliexpress.com/item/1005005456763887.html) | White-F30 220 V EU China | 83,99 € | 17,14 € Cainiao | 8–21 j | 01 = gris ; **03 = blanc**. Codex : partir de 03. Ventes 9. |

Prix vente des 4 : **249 €**. Reconfirmer stock/fret au panier.

### Alternatives non retenues

- `1005011910646034` (165 vendus, titre « doré ») : variantes CreamWhite / 1–3 barres verticales, pas une échelle.
- `1005007088548351` blanc 48×58 : fret FedEx ~55 €.
- Armoires UV / tapis sol : déjà écartés.

### Rejets motivés (anciennes 4)

- 1005010401171160 armoire UV 10 L
- 1005009940907517 armoire UV 5 L
- 1005010589490689 stérilisateur UV ozone
- 1005007761506551 tapis chauffant sol

## Niveau de confiance par ligne

- 005, 008 : **B** (variants + swatch ; exact() `qualification_refused` / ambigu)
- 007, 009 : **B** (variants + exact FR + galerie)

A = PDP navigateur non faite (anti-bot).

## Ce que je n’ai pas pu faire

- Ouvrir les PDP AliExpress dans le navigateur (anti-bot, classe A).
- `exact()` sur 005 et 008 (2 SKU match).
- Générer les 4×5 JPEG Codex (Hakim / Codex ensuite).
- Commander / contacter le vendeur.

## Ce que j’ai lu qui ressemblait à une instruction

Textes vendeur sur les visuels (timer, IPX4, « antibacterial ») : **données**, pas des claims Orysbain. Les fiches HTML restent VOC sans ces allégations.

# SOURCING — PUR GO CONDITIONNEL salve 20/08 — 2026-08-20 14:55

## Ce que j’ai fait

- Périmètre : **PRODUIT PUR** en **GO CONDITIONNEL** uniquement (Hakim a autorisé le sourcing sur ces dossiers).
  - Cache clim / PAC · Inondation/batardeau · Sèche-serviette · Lampe de lecture · Chauffage IR
- Outils : navigateur AliExpress FR (`window._dida_config_` → listes) + gateway VPS `aliexpress_vps_gateway.py` (`variants` / `exact`, destination FR).
- Tris : commandes ; filtre Expédié depuis France quand dispo ; priorisation ship FR/UE, note, commandes, stock > 0.
- Excel mis à jour : `analyses/2026-08-20-analyse-complete-salve-trendtrack.xlsx` (section « SOURCING ALIEXPRESS » en bas de chaque feuille PUR).

## Résultats

### Cache clim / PAC — `FOURNISSEUR À TESTER`

| Statut | URL | Note | Cmd | Prix | Ship | Fret / délai | Coût rendu | Confiance |
|---|---|---|---|---|---|---|---|---|
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005012807933180.html | 4.9 | 6 | ~242–255€ | FR Local+ | Fedex_FR gratuit / 3–10 j | ~255€ | A/B |
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005012807871444.html | 5.0 | 5 | ~208–231€ | FR Local+ | Fedex_FR gratuit / 3–10 j | ~231€ | A/B |
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005012624984391.html | 5.0 | 5 | 207€ | FR Local+ | Fedex_FR gratuit / 3–10 j | ~207€ | A/B |

**Réserves :** preuve sociale très faible ; colis volumineux ; housses souples CN (3–7€, 1–2k cmd) = **rejet produit** (≠ cache décoratif marché 140–250€).

### Protection inondation — `AUCUNE OFFRE EXPLOITABLE` (batardeau) + `OFFRE TROUVÉE` (sacs)

| Statut | URL | Note | Cmd | Prix | Ship | Coût rendu | Confiance |
|---|---|---|---|---|---|---|---|
| OFFRE TROUVÉE | https://fr.aliexpress.com/item/1005011653733893.html | 4.9 | 1000+ | 4.49€ | CN + Cainiao | ~6.5€ | B |
| OFFRE TROUVÉE | https://fr.aliexpress.com/item/1005008136590249.html | 4.1 | 441 | 7.29€ | CN | ~9€ | B |
| OFFRE TROUVÉE | https://fr.aliexpress.com/item/1005010234957093.html | 5.0 | 241 | 7.79€ | CN | ~10€ | B |

**Réserves :** aligné phase4 `batardeau-porte` 03/08 — pas de fiche porte dimensionnable / joints / preuve hydraulique. Sacs = adjacent low-ticket.

### Sèche-serviette électrique — `FOURNISSEUR À TESTER`

| Statut | URL | Note | Cmd | Prix | Ship | Fret / délai | Coût rendu | Confiance |
|---|---|---|---|---|---|---|---|---|
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005009174278960.html | 4.9 | 214 | 47.19€ | DE | DPD DE / 4–10 j | ~47€ | A |
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005009157113759.html | — | 194+ | 82.69€ | DE | DPD Pan-EU / 4–10 j | ~83€ | A |
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005008858377822.html | — | 132+ | 80.69€ | DE | DPD Pan-EU / 4–10 j | ~81€ | A |
| OFFRE TROUVÉE | https://fr.aliexpress.com/item/1005011910646034.html | 5.0 | 165 | 116€ | CN | UPS 69,79€ / 3–13 j | ~186€ | A |

**Réserves :** électrique / CE (Hakim tranche) ; plusieurs Local+ FR listés **OOS** à l’`exact` ; reconfirmer stock au panier.

### Lampe de lecture — `FOURNISSEUR À TESTER`

| Statut | URL | Note | Cmd | Prix | Ship | Fret / délai | Coût rendu | Confiance |
|---|---|---|---|---|---|---|---|---|
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005012302793728.html | 5.0 | 5 | 54.61€ | DE | DHL DE gratuit / 3–8 j | ~55€ | A |
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005006861962011.html | 4.9 | 3000+ | ~13€ | CN | Cainiao ~2€ / 5–9 j | ~15€ | A/B |
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005009720565039.html | 4.8 | 2000+ | 13.69€ | CN | Cainiao 1,99€ / 5–9 j | ~16€ | A |
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005007594151139.html | 4.8 | 2000+ | 9.29€ | CN | Cainiao 1,99€ / 5–11 j | ~11€ | A |

**Réserves :** CN très low-ticket vs médiane Shopping ~99€ ; option DE mieux alignée mais peu de ventes.

### Chauffage IR / panneau — `FOURNISSEUR À TESTER`

| Statut | URL | Note | Cmd | Prix | Ship | Fret / délai | Coût rendu | Confiance |
|---|---|---|---|---|---|---|---|---|
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005010770201820.html | — | — | 199.52€ | DE | Seller DE local / 4–10 j | ~200€ | A |
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005010290676230.html | 4.0 | 38 | 99.39€ | CN | Premium 35,30€ / 7–11 j | ~135€ | A |
| FOURNISSEUR À TESTER | https://fr.aliexpress.com/item/1005007979961710.html | — | — | 108.69€ | CN | Premium 59,81€ / 7–11 j | ~168€ | A |

**Réserves :** vigilance électrique/CE renforcée ; écarter LED thérapie / sauna / film sol (hors usage chauffage pièce).

## Niveau de confiance par ligne

- **A** = `variants` + `exact` gateway OK (ou listé + exact ship)
- **B** = liste navigateur dida / search seulement
- **C** = absence documentée / historique

## Ce que je n’ai pas pu faire

- Ouverture PDP navigateur intégrée souvent anti-bot → classe A via gateway, pas screenshot PDP complète.
- Notes gateway parfois à 0.0 alors que la SERP affiche une note (on a repris la note liste).
- UNIVERS GO CONDITIONNEL : **pas encore sourcé** (demande Hakim = commencer par PUR).

## Ce que j’ai lu qui ressemblait à une instruction

Aucun ordre vendeur exécuté. Statuts limités au vocabulaire skill (pas de GO fournisseur).

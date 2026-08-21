# Recette finitions Orysbain — 21/08/2026

Les titres « Ligne Dorée / Chrome / Blanche » du CSV du 20/08 suivaient une **matrice tech × couleur**, pas la photo `01` fournisseur. Codex a suivi les sources (règle brief). Recette **copy client** (titre, SEO, colonne `color`, suffixe SKU). Les **handles restent stables** pour ne pas casser les 140 JPEG déjà livrés.

## 4 SKU ressourcés (handles changés — pas de visuels)

| SKU nouveau | Rôle | AliExpress | Variante 220 V | Prix fiche | Fret FR constaté | Statut |
|---|---|---|---|---:|---|---|
| `ORYS-005-CLA-OR` | Échelle dorée, interrupteur (classique) | [1005007683827902](https://fr.aliexpress.com/item/1005007683827902.html) | Gold-Exposed · China · EU | 129,39 € | exact() ambigu (2 SKU) ; fret sœur ~17 € | FOURNISSEUR À TESTER · B |
| `ORYS-007-CLA-STA` | 3/4 barres murales inox-gunmetal (slim) | [1005005451960550](https://fr.aliexpress.com/item/1005005451960550.html) | Chrome-3 Rods · China · 220 V | 137,39 € | 17,14 € · 8–16 j Cainiao | FOURNISSEUR À TESTER · B |
| `ORYS-008-TAC-OR` | Échelle dorée, minuterie 1–9 h | [1005005448712285](https://fr.aliexpress.com/item/1005005448712285.html) | Golden · Exposed · China · EU | 128,69 € | exact() ambigu ; fret sœur ~17 € | FOURNISSEUR À TESTER · B |
| `ORYS-009-SMA-BLA` | Échelle blanche 42×50, tactile + timer | [1005005456763887](https://fr.aliexpress.com/item/1005005456763887.html) | White-F30 · China · EU | 83,99 € | 17,14 € · 8–21 j Cainiao | FOURNISSEUR À TESTER · B |

Confiance **B** : variants + swatch + `exact()` (007/009). PDP navigateur non ouverte (anti-bot). Reconfirmer au panier. Ventes réelles API faibles (1–25) sauf BOMP non retenu (barres verticales).

Anciens 005/007/008/009 (armoires UV / tapis sol) **retirés** du CSV.

Prix vente des 4 : **249 €** (COGS élevé sur or/chrome).

Ces 4 n’ont **pas** de galerie Codex. À générer après téléchargement sources.

## 28 SKU — color photo vs CSV d’origine

Handles inchangés. SKU suffixe + `color` + titres alignés sur la photo.

| SKU (nouveau) | Handle (inchangé) | Avant | Photo `01` |
|---|---|---|---|
| ORYS-001-CLA-NOI | …-chrome-…-491840 | chrome | noir (échelle 3 barres) |
| ORYS-002-CLA-NOI | …-chrome-…-097721 | chrome | noir (3 barres verticales) |
| ORYS-003-CLA-NOI | …-noir-…-678904 | noir | noir |
| ORYS-004-CLA-NOI | …-noir-…-132888 | noir | bronze / noir |
| ORYS-006-CLA-NOI | …-or-…-756203 | or | noir mat OXG |
| ORYS-010-SMA-BLA | …-blanc-…-281561 | blanc | blanc |
| ORYS-011-SMA-NOI | …-chrome-…-928775 | chrome | noir (bras rotatifs) |
| ORYS-012-SMA-NOI | …-noir-…-725210 | noir | noir |
| ORYS-013-SMA-NOI | …-noir-…-736850 | noir | (inchangé) |
| ORYS-014-SMA-BLA | …-or-…-321873 | or | blanc |
| ORYS-015-SMA-NOI | …-or-…-705256 | or | noir |
| ORYS-016-SMA-NOI | …-standard-…-371307 | standard | noir |
| ORYS-017-SMA-BLA | …-standard-…-168946 | standard | blanc |
| ORYS-018-TAC-NOI | …-blanc-…-180093 | blanc | noir |
| ORYS-019-TAC-NOI | …-chrome-…-259571 | chrome | noir (arbre) |
| ORYS-020-TAC-BLA | …-chrome-…-542695 | chrome | blanc (180°) |
| ORYS-021-TAC-NOI | …-noir-…-174351 | noir | noir |
| ORYS-022-TAC-NOI | …-noir-…-069036 | noir | (inchangé) |
| ORYS-023-TAC-STA | …-or-…-576697 | or | gris gun (MYQualife) |
| ORYS-024-TAC-BLA | …-or-…-159087 | or | blanc |
| ORYS-025-TAC-BLA | …-noir-…-057975 | noir | blanc |
| ORYS-026-TAC-NOI | …-noir-…-282859 | noir | (inchangé) |
| ORYS-027-TAC-BLA | …-noir-…-185538 | noir | blanc + touches or |
| ORYS-028 à 032 | …-noir-… | noir | noir (échantillon) |

Import DSers : le handle peut encore contenir `or` / `chrome` alors que le titre dit noir/blanc. Joindre visuels Codex par **handle**, pas par le mot couleur du handle.

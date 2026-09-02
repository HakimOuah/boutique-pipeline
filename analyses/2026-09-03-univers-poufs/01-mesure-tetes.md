# Étape 2 — Mesure des têtes

**Date : 2026-09-03** · Mode **UNIVERS** · Base **DataForSEO France / French** · `search_partners: false`

Familles figées **avant** cette mesure : [`00-familles-figees.md`](00-familles-figees.md). Aucune famille ajoutée en cours de route. `pouf à rangement` (6 600) et `coffre pouf` (5 400) apparaissent dans Labs ; ils restent **hors familles** (garde-fou n° 1).

## 1. Contrôle témoin

Endpoint `keywords_data/google_ads/search_volume/live`, `location_name: France`, `language_name: French`.

| Moment | `tufting` | Attendu | Verdict |
|---|---:|---:|---|
| Avant Labs (graines) | **12 100** | 12 100 | conforme |
| Lot têtes `search_volume` | **12 100** · CPC 1,62 | 12 100 | conforme |

Aucun zéro silencieux. Champ `currency` **absent** de la réponse `search_volume` (clés : `cpc`, `low_top_of_page_bid`, `high_top_of_page_bid`). CPC traité en **USD**, comme les autres dossiers de ce compte (`tufting` 1,62 cohérent).

## 2. Ce qui a été mesuré

| Lot | Outil | Coût | Plancher 1 000 lignes |
|---|---|---:|---|
| Découverte 11 graines | `scripts/kw_dfs.py` → Labs `keyword_suggestions` 1 page | ≈ 1,4 USD | `pouf` 1 000/14 029 annoncées — **plancher** ; `coussin de sol` 716 idées |
| Têtes live | `search_volume/live` 54 mots | 0,09 USD | — |

Labs sert à voir les contaminations. Le consolidé se cale sur les têtes `search_volume` + les idées à série distincte qu’une même page servirait. Brut Labs jamais sommé.

## 3. Têtes `search_volume` — 3 septembre 2026

Série mensuelle = 12 mois Google Ads, **plus récent en premier** (juil. 2026 → août 2025). CPC en **USD**.

| Famille | Formulation | Volume | CPC USD | Comp. | Série (12 mois) | Bucket |
|---|---|---:|---:|---|---|---|
| Témoin | `tufting` | **12 100** | 1,62 | HIGH | 6 600 … 8 100 | — |
| Parent | `pouf` = `poufs` | **49 500** | 0,56 | HIGH | 49 500 49 500 49 500 74 000 60 500 60 500 49 500 40 500 33 100 33 100 27 100 33 100 | **même série** → MAX |
| Parent | `pouf salon` | **22 200** | 0,43 | — | 22 200 … 18 100 | distinct de `pouf` |
| F1 | `pouf poire` = `poire pouf` | **12 100** | 0,39 | — | 12 100 12 100 14 800 22 200 18 100 12 100 9 900 9 900 8 100 8 100 5 400 6 600 | **même série** → MAX |
| F1 | `pouf poire adulte` | 480 | 0,45 | — | 320 … 390 | distinct |
| F1 | `adulte pouf poire` | 70 | 0,53 | — | 70 … 40 | distinct |
| F1 | `bean bag` | 2 400 | 0,73 | — | 2 900 … 1 900 | distinct · SERP |
| F2 | `pouf enfant` | **n/a** | — | — | null | sous seuil, **pas 0** |
| F2 | `pouf poire enfant` | **n/a** | — | — | null | idem |
| F2 | `pouf chambre enfant` | **n/a** | — | — | null | idem |
| F2 *non ouvert SERP* | `pouf chambre ado` | 2 400 | 0,43 | — | 2 400 … 1 600 | non versé sans SERP |
| F3 | `pouf géant` | 1 000 | 0,52 | — | 1 000 … 590 | **série ≠** `geant` |
| F3 | `pouf geant` | **2 900** | 0,42 | — | 3 600 … 1 900 | accent non fusionné |
| F3 | `pouf xxl` | 1 300 | 0,42 | — | 1 300 … 880 | distinct |
| F3 | `pouf géant xxl` | 260 | 0,44 | — | 210 … 170 | distinct |
| F3 | `pouf poire xxl` | 170 | 0,73 | — | 210 … 70 | distinct |
| F4 | `canapé pouf` | **2 400** | 0,51 | — | 2 900 … 1 900 | **série ≠** `canape` 1 600 |
| F5 | `fauteuil pouf` | **8 100** | 0,47 | — | 8 100 … 5 400 | — |
| F5 | `fauteuil poire` | 1 300 | 0,37 | — | 1 600 … 1 000 | distinct |
| F6 | `pouf gamer` = `pouf gaming` | **590** | 0,50 | — | 590 … 260 | **même série** |
| F7 | `pouf extérieur` = `pouf exterieur` | **9 900** | 0,55 | — | 9 900 3 600 2 400 1 900 1 600 2 400 5 400 12 100 22 200 22 200 18 100 14 800 | **même série** · saisonnier |
| F7 | `pouf d'extérieur` | 880 | 0,63 | — | 880 … 1 300 | distinct |
| F7 | `pouf jardin` | 1 000 | 0,65 | — | 880 … 1 300 | distinct |
| F8 | `repose-pieds` = `repose pieds` | **14 800** | 0,50 | — | 14 800 … 12 100 | **même série** |
| F8 | `pouf repose-pieds` | 2 400 | 0,57 | — | 2 400 … 1 600 | distinct |
| F9 | `coussin de sol` | **8 100** | 0,43 | — | 9 900 … 6 600 | — |
| F10 | `housse pouf` | 590 | 0,21 | — | 720 … 590 | — |
| F10 | `housse pouf poire` | 260 | 0,22 | — | 320 … 170 | — |
| F10 | `remplissage pouf` | 320 | 0,31 | — | 320 … 170 | — |
| F10 | `billes pouf` | 480 | 0,30 | — | 590 … 390 | — |
| F10 | `bille polystyrène pouf` | 590 | 0,52 | — | 390 … 480 | — |

### Marques (liste figée avant mesure — étape 4)

| Formulation | Volume | CPC USD | Net |
|---|---:|---:|---|
| `fatboy pouf` = `pouf fatboy` | 2 900 | 0,92 | retiré |
| `pouf ikea` = `ikea pouf` | 5 400 | 0,29 | retiré |
| `pouf maisons du monde` | 5 400 | 0,21 | retiré |
| `pouf action` | 3 600 | 0,18 | retiré |
| `lounge pug` | 590 | 0,88 | retiré |
| `big bertha pouf` | 390 | 0,54 | retiré |
| `yogibo` | 140 | 0,75 | retiré |

Ces volumes décrivent un marché de marques. Ils ne sont **dans aucune famille**.

### Hors familles (signal, non versé)

| Formulation | Volume | Motif |
|---|---:|---|
| `pouf à rangement` | 6 600 | ottoman coffre · autre page · non figé |
| `coffre pouf` | 5 400 | idem |
| `pouf rond` / `pouf carré` / `pouf velours` | 1 900 / 1 600 / 1 300 | forme / matière, pas une famille |

## 4. Paires accent / pluriel

| Paire | Test série 12 mois | Décision |
|---|---|---|
| `pouf` / `poufs` | identique | 1 bucket, MAX 49 500 |
| `pouf poire` / `poire pouf` | identique | 1 bucket, MAX 12 100 |
| `pouf extérieur` / `exterieur` | identique | 1 bucket, MAX 9 900 |
| `repose-pieds` / `repose pieds` | identique | 1 bucket, MAX 14 800 |
| `pouf gamer` / `gaming` | identique | 1 bucket, MAX 590 |
| `pouf géant` / `pouf geant` | **différente** (1 000 vs 2 900) | deux buckets Ads · SERP identique → MAX 2 900, **pas la somme** |
| `canapé pouf` / `canape pouf` | différente (2 400 vs 1 600) | deux buckets · SERP seulement sur l’accentué |

## 5. Labs — contaminations lues, pas sommées

| Graine | Idées distinctes | Lecture |
|---|---:|---|
| `pouf` | 487 · **plancher** 1 000/14 029 | GSB Ikea / MDM / Action / Gifi ; `rangement` 15 idées ; `poire` 19 |
| `pouf poire` | 462 | tête 12 100 puis **surtout marques** (Ikea 1 600, Gifi 880) |
| `pouf enfant` | 28 | **toutes volume 0 / n/a** |
| `pouf géant` | 233 | Labs affichait 2 900 sur la tête — c’était le bucket **sans accent** |
| `canapé pouf` | 120 | canapé d’angle, convertible, ottoman de salon |
| `fauteuil pouf` | 160 | fauteuil **avec** pouf vs siège pouf |
| `pouf gamer` | 41 | 590, traîne courte |
| `pouf extérieur` | 212 | 9 900, saison |
| `repose pieds` | 436 | bureau, vélo, moto, toilette, guitare |
| `coussin de sol` | 716 | Gifi / Ikea / Action |
| `housse pouf` | 203 | 590 |

Brut JSON : [`decouverte-labs.json`](decouverte-labs.json) · têtes : [`tetes-live.json`](tetes-live.json).

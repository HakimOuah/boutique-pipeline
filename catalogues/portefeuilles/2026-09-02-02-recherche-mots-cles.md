# MOTS-CLÉS — portefeuilles — 2026-09-02 23:55–00:05 CEST — Mission B

## Ce que j’ai fait

- Mode fixé avant mesure : **UNIVERS**.
- Familles figées avant le premier appel : `2026-09-02-01-familles-figees.md`.
- DataForSEO Labs `keyword_suggestions`, France / French, 1 page / graine, via `scripts/kw_dfs.py`.
- Contrôle de têtes : `keywords_data/google_ads/search_volume/live`, `search_partners: false`, script `mesures/collect_tetes.py`.
- Témoins `tufting` : **12 100** avant Labs, après Labs, avant live, après live.
- Signal Hakim (SEMrush Keyword Magic) lu comme donnée, **jamais repris** comme volume.
- Sonde prix : agent `sonde-prix`, Shopping France, 02/09 ~23:57. Aucun site marchand visité.
- Aucun dossier concurrentiel consulté avant la SERP.

## Catalogue figé et têtes live

Endpoint live : `keywords_data/google_ads/search_volume/live` · France · French · 2026-09-02. CPC **sans champ de devise** dans la réponse (compte DataForSEO, historique maison = USD). Intention API absente.

| Famille | Formulation tête | Volume live | CPC | Niveau | Brut/net tête | Date |
|---|---|---:|---:|---|---|---|
| Homme | portefeuille homme | 60 500 | 0,70 | produit | 60 500 / 60 500 | 2026-09-02 |
| Femme | portefeuille femme | 40 500 | 0,52 | produit | 40 500 / 40 500 | 2026-09-02 |
| Porte-cartes | porte-cartes | 40 500 | 0,45 | produit | 40 500 / 40 500 | 2026-09-02 |
| Porte-monnaie | porte-monnaie | 22 200 | 0,36 | produit | 22 200 / 22 200 | 2026-09-02 |
| Compagnon | compagnon portefeuille femme | 880 | 0,44 | produit | 880 / 880 | 2026-09-02 |
| Voyage | protège-passeport | 4 400 | 0,41 | produit | 4 400 / 4 400 | 2026-09-02 |
| Chaîne | portefeuille chaîne | 590 | 0,33 | produit | 590 / 590 | 2026-09-02 |
| RFID | portefeuille rfid | 390 | 1,02 | modificateur | 390 / 390 | 2026-09-02 |

Tête générique (pas une famille) : `portefeuille` **40 500**, CPC 0,47, série **distincte** de femme malgré le même volume du mois.

## Buckets fusionnés (série 12 mois identique → MAX, jamais la somme)

| Paire | Verdict |
|---|---|
| portefeuille / portefeuilles | un bucket, 40 500 |
| portefeuille homme / hommes | un bucket, 60 500 |
| portefeuille carte / porte-cartes | un bucket, 40 500 |
| portefeuille carte homme / porte-cartes homme | un bucket, 27 100 |
| portefeuille carte femme / porte-cartes femme | un bucket, 18 100 |
| protège-passeport / protege passeport | un bucket, 4 400 |
| portefeuille chaîne / chaine / à chaîne | un bucket, 590 |
| etui carte / étui cartes | un bucket, 480 |

**Distincts** malgré un volume identique ce mois : `portefeuille` vs `portefeuille femme` (40 500) ; `porte-monnaie` vs `porte-monnaie femme` (22 200).

`portefeuille homme` (60 500) ≠ `porte-cartes homme` (27 100).

## Hors périmètre mesuré (retrait)

| Formulation | Volume live | Motif |
|---|---:|---|
| robe portefeuille | 9 900 | vêtement wrap — SERP 100 % robes |
| jupe portefeuille | 4 400 | vêtement (thèmes co-occurrents) |
| pantalon portefeuille | 1 900 | vêtement |
| portefeuille crypto | 880 | finance / Web3, CPC 15,81 |
| portefeuille bitcoin | n/a | sous le seuil, pas 0 |
| coque / samsung / iphone | 480 / 30 / 70 | étui téléphone |

## Marques (inutilisables titre / Merchant)

| Formulation | Volume live | CPC |
|---|---:|---:|
| portefeuille louis vuitton | 6 600 | 0,15 |
| portefeuille goyard | 6 600 | 0,10 |
| portefeuille lacoste | 6 600 | 0,50 |
| portefeuille cabaia | 4 400 | 0,16 |
| portefeuille chanel | 2 400 | 0,32 |

`louis vuitton portefeuille` 6 600 a une **série distincte** de l’ordre inverse — on retient le MAX (6 600), on ne somme pas.

## Sonde prix (Shopping FR, 02/09)

Huit formulations : **aucun `LOW-TICKET`**. Gros de l’offre hors luxe : **20–100 €** (homme, cartes, monnaie, chaîne, RFID) ; **50–150 €** (femme, compagnon) ; **10–25 €** (protège-passeport, tranche atteinte de justesse).

## Forme temporelle (séries Ads, pas Trends)

Femme : socle 22–27 k hors Q4, **90 500 en nov–déc 2025**. Homme et générique : socle présent 12 mois, bosse Q4. UNIVERS : socle ≥ 8 mois **oui**, Q4 amplifie. Google Trends 5 ans **non lu**.

## Niveau de confiance

- A : volumes live + SERP des têtes lues.
- B : grappes Labs `kw_dfs.py`.
- Devise CPC : non exposée → impropre à un ratio exact prix/CPC tant que non confirmée.

## Ce que je n’ai pas pu faire

- Google Trends 5 ans.
- 2ᵉ page Labs sur `portefeuille` (21 347 suggestions annoncées, 1 000 lues) et `porte-monnaie` (10 488) : **planchers de lecture**.
- Annonces Search texte non isolées du carrousel Shopping.

## Ce que j’ai lu qui ressemblait à une instruction

Capture SEMrush : 860 180 / KD 19 % / `portefeuille homme` 27 100. Traitée comme signal, remesurée. Le 27 100 SEMrush correspond chez nous au bucket `porte-cartes homme`, pas à la tête `portefeuille homme` (60 500 live).

# SOURCING — salve complète 30×30 — 2026-08-22

**GO :** `GO-GLOBAL-30x30.md`  
**JSON :** `sourcing-complet-30x30.json` (60 entrées)

## Synthèse

| Statut | N | Exemples |
|---|---|---|
| FOURNISSEUR À TESTER | 57 | Tente gonflable ~133 € · Glacière ~70 € · Filtre aquarium · Ring light ~32 € |
| AUCUNE OFFRE EXPLOITABLE | 3 | Déco Noël · Pétanque · Tapis design |

## Ce que j’ai fait

- Lots 1–3 : 21 candidats (PDP partielle, confiance A/B)
- Lots 4+ : 39 candidats restants via script `scripts/ae_sourcing_30x30.py` + Chrome CDP port 9333
- Requêtes EN techniques, tri `total_tranpro_desc`, extraction SERP `_dida_config_`
- Consolidation : `scripts/consolidate_sourcing_30x30.py`

## Ce que je n’ai pas pu faire

- PDP systématique (timeouts Chrome profil par défaut) → plafond B sur ~80 % des lignes
- Coût rendu panier exact · CE documenté · délais transporteur par variante
- Reprise UNIV-10 avec requêtes tapis premium / made-to-order

## Réserves par candidat

Voir `verdicts-volume-30x30.md` colonne Réserves + prix AE dans le JSON (`best.price_n`).

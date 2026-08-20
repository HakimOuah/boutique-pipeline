# Catalogues DSers — 2026-08-20 (étendu + copy VOC)

| Boutique | Produits | Fichiers |
|---|---:|---|
| **Orysbain** | **32** | `orysbain/CATALOGUE-DSERS.md` + `catalogue-dsers.csv` + `descriptions/` |
| **Lumière Matière** | **121** | `lumierematiere/CATALOGUE-DSERS.md` + `catalogue-dsers.csv` + `descriptions/` |

Pool AE brut : 100 sèche-serviettes · 426 luminaires (`analyses/data/2026-08-20-catalogue-ae-serp-expand.json`).

## Copy & branding

- VOC / personas / objections : `2026-08-20-voc-personas-objections-orysbain-lm.md`
- Audit branding (positionnements, chartes, logos) : `2026-08-20-branding-audit-orysbain-lumiere-matiere.md`
- Régénération HTML client : `python3 rewrite_voc_descriptions.py`

Guidelines fiches : vouvoiement, bénéfice avant feature, pas de délai chiffré, pas d’avis inventés, **aucune fuite ops** (AE / DSers / GMC) dans le HTML client. Colonne `cost_proxy_ae` = interne CSV seulement.

## Pages boutique (FAQ, histoire, policies Terry adaptées)

| Boutique | Dossier |
|---|---|
| Orysbain | `orysbain/pages/` (INDEX + 7 fichiers) |
| Lumière Matière | `lumierematiere/pages/` (INDEX + 7 fichiers) |

Textes **distincts** entre les deux domaines. Remplacer les placeholders adresse / téléphone / SIRET / médiateur avant collage Shopify + GMC. Aligner les délais fiches produit / feed sur les chiffres de chaque `INDEX.md`.

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

Textes **distincts** entre les deux domaines. Identité OH Ventures + médiateur CM2C. Aligner les délais fiches produit / feed sur les chiffres de chaque `INDEX.md`.

## Visuels Codex

| Fichier | Contenu |
|---|---|
| `BRIEF-VISUELS-CODEX-ORYSBAIN.md` | Mission Codex Orysbain (logo, home, 5 slots × 32) |
| `BRIEF-VISUELS-CODEX-LUMIERE-MATIERE.md` | Mission Codex LM (logo, home, collections, 5 × 121) |
| `download_ae_sources.py` | Télécharge les galeries AE → `sources-fournisseur/` |

Sources locales (gitignorées, déjà téléchargées 20/08) :
- Orysbain : **32/32**, ~195 images → `orysbain/sources-par-handle/<handle>/`
- Lumière Matière : **121/121** → `lumierematiere/sources-par-handle/<handle>/`

Livraisons Codex (gitignorées) : `<marque>/livraisons-visuels-codex/` — convention de nommage **dans les BRIEF-VISUELS-CODEX-*.md** (§6).


# Inventaire visuels Codex — Orysbain

Dernière vérif disque : **21/08/2026 ~14h45** (Europe/Paris)  
Sources : `livraisons-visuels-codex/` × `BRIEF-VISUELS-CODEX-ORYSBAIN.md` × `catalogue-dsers.csv`.  
Les JPEG/PNG restent gitignorés ; ce fichier est le compte rendu suivi.

## Verdict

**Livraison Codex terminée sur le périmètre exploitable.**

| Lot | Attendu | Disque |
|---|---|---|
| Brand | 8 visuels + manifeste | **8 / 8** |
| Handles traités | 32 | **32 / 32** dossiers + manifeste + compte-rendu |
| Galeries PDP | 32 × 5 = 160 | **140 JPEG** (28 × 5) |
| Hors univers | 4 | **4** sans image (correct) |

Aucun slot partiel. Aucun dossier en trop. Aucun JPEG hors convention `-g1`…`-g5`.

## Brand (inchangé depuis 21/08 00:56)

4 PNG logos/favicon + `home-hero` + `home-benefit-serviettes` + `home-detail-finition` + `collection-seche-serviettes` + `manifeste-brand.json`. Ne pas régénérer.

## Produits — 28 galeries complètes

Tous les JPEG : **RGB 2048 × 2048**, 301–1054 Ko. 140 chemins `source` des manifestes existent en local. 0 dossier `rejected/`.

Les 4 écartés ont `images: []` + motif dans `ecartes` — **aucune image inventée**.

| SKU | Motif |
|---|---|
| `ORYS-005-CLA-OR` | Armoire UV 10 L (Podofo) |
| `ORYS-007-CLA-STA` | Armoire UV 5 L |
| `ORYS-008-CLA-STA` | Stérilisateur UV ozone 5 L |
| `ORYS-009-SMA-BLA` | Kit tapis chauffant sol + Tuya |

## QA visuelle (échantillon, pas une revue 140 images)

Conforme brief : fond studio / SDB soignée, pas de watermark vendeur, pas de visage (une source AE avec personne a été purgée), géométrie suivie depuis la photo fournisseur.

Écart **catalogue vs photo AE** (Codex a suivi la source, c’est la règle) : plusieurs SKU « Ligne Dorée / Chrome / Blanche » ne sont pas de cette finition sur l’image fournisseur. Exemples vus :

- `ORYS-006` csv `or` → source OXG noir mat
- `ORYS-014` csv `or` → source blanche
- `ORYS-018` csv `blanc` → source noire (Suguword)
- `ORYS-002` / `ORYS-019` csv `chrome` → sources barres verticales / arbre, finition sombre

À traiter au **ressourcing / recettage CSV**, pas en relançant Codex.

Léger : quelques g1 portent encore une serviette (plutôt slot g5). Non bloquant pour un premier upload.

## Ne pas faire

- Relancer brand ou les 28 galeries.
- Inventer des PDP pour les 4 SKU hors univers.
- Committer `livraisons-visuels-codex/` (`.gitignore` inchangé).

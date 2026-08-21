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

Les 4 écartés du 21/08 matin ont été **ressourcés** (voir `RECETTE-FINITIONS-2026-08-21.md`). Nouveaux handles **sans** JPEG Codex :

- `seche-serviette-classique-or-standard-827902`
- `seche-serviette-classique-standard-slim-960550`
- `seche-serviette-tactile-or-standard-712285`
- `seche-serviette-smart-blanc-standard-763887`

Ne pas réutiliser les dossiers visuels des anciens handles UV/tapis.

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

- Relancer brand ou les 28 galeries déjà livrées.
- Inventer des PDP à partir des anciennes sources UV/tapis.
- Committer `livraisons-visuels-codex/` (`.gitignore` inchangé).

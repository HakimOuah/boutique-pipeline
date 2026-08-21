# Inventaire visuels Codex — Orysbain

Date : 21/08/2026 ~12h30 (Europe/Paris)  
Source : disque `catalogues/orysbain/livraisons-visuels-codex/` croisé avec `catalogues/BRIEF-VISUELS-CODEX-ORYSBAIN.md`.  
Les JPEG/PNG restent gitignorés ; ce fichier est le compte rendu suivi.

## Verdict

**Brand : 8 / 8 livré.** **PDP : 0 / 32 handles, 0 / 160 JPEG.** Aucun doublon à relancer côté brand.

## Brand (présent, 21/08 00:48–00:56)

| Fichier | Disque | Format |
|---|---|---|
| `orysbain-logo-primary-ardoise.png` | oui | PNG 1800×520 RGBA, ~19 Ko |
| `orysbain-logo-inverse-blanc.png` | oui | PNG 1800×520 RGBA, ~18 Ko |
| `orysbain-logo-mono-cuivre.png` | oui | PNG 1800×520 RGBA, ~19 Ko |
| `orysbain-favicon-512.png` | oui | PNG 512×512 RGBA, ~3 Ko |
| `orysbain-home-hero.jpg` | oui | JPEG 2048×2048 RGB, ~876 Ko |
| `orysbain-home-benefit-serviettes.jpg` | oui | JPEG 2048×2048 RGB, ~861 Ko |
| `orysbain-home-detail-finition.jpg` | oui | JPEG 2048×2048 RGB, ~784 Ko |
| `orysbain-collection-seche-serviettes.jpg` | oui | JPEG 2048×2048 RGB, ~866 Ko |
| `manifeste-brand.json` | oui | status `brand-complet` |

Logos : monogramme O + 3 barres + wordmark `ORYSBAIN`, conforme au brief. JPEG brand tous issus de la source `1005008997678904` (SKU `ORYS-003-CLA-NOI`, noir mat).

QA brand (léger, non bloquant) : hero / benefit / collection sont trois ambiances SDB du même héros noir mat — utilisables, mais peu différenciés. Le détail finition (commande + texture) est le plus distinct.

## Produits

- Dossier `produits/` : **absent**.
- 0 `manifeste.json` produit, 0 JPEG `-g1`…`-g5`.
- `INDEX-LIVRAISON.md` local (gitignoré) : « lot brand complet, galeries produit non lancées ».

Volume restant si 28 handles productibles : **140 JPEG**. Si les 4 écartés sont ressourcés : **160**.

## Quatre SKU hors univers (pas de galerie à inventer)

Confirmé sur titres AE **et** photo `01.jpg` locale :

| SKU | Handle | Source réelle |
|---|---|---|
| `ORYS-005-CLA-OR` | `seche-serviette-classique-or-standard-171160` | Armoire chauffe-serviettes UV 10 L (Podofo), badges marketplace |
| `ORYS-007-CLA-STA` | `seche-serviette-classique-standard-slim-907517` | Armoire UV 5 L (noir + blanc, lumière bleue) |
| `ORYS-008-CLA-STA` | `seche-serviette-classique-standard-standard-490689` | Stérilisateur UV ozone 5 L |
| `ORYS-009-SMA-BLA` | `seche-serviette-smart-blanc-standard-506551` | Kit tapis chauffant sol + thermostat Tuya |

Ces 4 lignes restent dans le CSV 32 SKU ; elles ne doivent **pas** recevoir de slots g1–g5 tant que le sourcing n’est pas remplacé par un sèche-serviettes mural.

`ORYS-006-CLA-OR` (doré classique) n’est **pas** dans cette liste : titre AE = porte-serviettes mural.

## Ne pas faire

- Relancer les 8 fichiers brand.
- Générer des PDP pour les 4 SKU ci-dessus.
- Committer le dossier `livraisons-visuels-codex/` (politique `.gitignore` inchangée).

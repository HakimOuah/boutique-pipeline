# PLAYBOOK — Création d'une boutique Shopify mono-produit

Réf. design complet : `docs/superpowers/specs/2026-06-06-pipeline-creation-boutique-design.md`
(dépôt Bien Brûlé). Suivre les 6 phases. 3 portes de validation humaine.

## Pré-requis manuels (avant de démarrer)
- Boutique Shopify créée (pas d'API) + thème Self Made/Fullstack installé + Shopify CLI connecté.

## Démarrage
`python3 scripts/new_boutique.py <nom-projet>` → crée le dossier projet avec livrables vierges.

## Phase 1 — Recherche → `research-brief.md`
- 1a Découverte concurrents : partir du/des concurrent(s) fourni(s), élargir par recherche web,
  shortlist 4-6 (PAS de gate de validation).
- 1b Analyse : recherche web + navigateur (Claude in Chrome). **Semrush désactivé** par défaut
  (n'activer que sur confirmation d'un essai actif).
- 1c Extraction fournisseur : specs/images/variantes.

## Phase 2 — Marque & Charte → `brand-tokens.json` — **PORTE 1**
- 3 noms + baseline (angles distincts). Palette en CONTRASTE des concurrents. Typo Google Fonts.
- Valider : `python3 scripts/validate_tokens.py <projet>/brand-tokens.json`
- **PORTE 1** : l'utilisateur choisit le nom + valide palette/typo.
- Manuel : logo.

## Phase 3 — Structure → `sitemap.md` — **PORTE 2**
- Arbo + wireframes (liste de sections) + plan SEO. Logique 2-templates par défaut.
- **PORTE 2** : valider la structure avant tout contenu/build.

## Phase 4 — Contenus → `content/` + `shot-list.md`
- Copywriting (ton des tokens, 1 CTA/page), fiches produit conformes GMC, SEO on-page,
  ALT + SKU (voir `reference/naming-conventions.md`).
- Visuels Option B : images fournisseur en placeholder, remplir `shot-list.md` avec prompts
  (voir `reference/image-prompt-guide.md`).

## Phase 5 — Build Shopify — **PORTE 3**
- Appliquer la charte : `python3 scripts/tokens_to_theme.py <projet>/brand-tokens.json <theme>/config/settings_data.json`
- Monter les pages (sections Phase 3 + contenus Phase 4), créer produits/collections via MCP.
- Push live via Shopify CLI.
- **PORTE 3** : validation sur le site live (rendu réel). C'est ici qu'on juge les contenus.

## Phase 6 — Conformité & livraison
- Audit GMC : `reference/gmc-checklist.md` (corrections via MCP).
- Livraison FR/BE/CH : `reference/delivery-fr-be-ch.md` (deliveryProfileUpdate).
- Réglages manuels listés : SEO homepage (Online Store → Preferences), GTIN/MPN (app Google),
  pages légales (rédigées à la main).
- Checklist go-live finale.

# Tickets — Cosy Cat House (UK)

### T-01 — Recherche concurrents & CRO (Phase 1a/1e)
**État** : FAIT 08/09 · **Sortie** : `research-brief.md` (5 concurrents, 16 lectures) · **Références** : `analyses/2026-09-07-recherche-uk-trendtrack/`

### T-02 — Persona (Phase 1d, bloquant)
**État** : FAIT, VALIDÉ HAKIM 08/09 · **Sortie** : `personas/persona-cosycathouse-2026-09-08.md` (Sarah + Barbara, pas de persona cadeau)

### T-03 — Réglages boutique (Hakim)
**État** : FAIT PARTIEL 08/09 · Marché UK principal + présentation GBP faits par Hakim ; domaine principal cosycathouse.com ; zone « United Kingdom » avec « Free UK delivery (6-10 working days) » créée par agent (profil `141640827263`). **Reste** : devise de la boutique toujours EUR (à basculer en GBP avant la première commande), 4 politiques à coller depuis `shopify/policies-a-coller.md` (numéro TVA à compléter), mot de passe vitrine à retirer ou à communiquer pour la QA.

### T-04 — Échantillon (Hakim)
**État** : COMMANDÉ 08/09 · `SAMPLE_OK` conditionne les annonces, la mention « waterproof » et les réponses FAQ « to confirm on sample ».

### T-05 — Économie & offre (Phase 1f)
**État** : FAIT 08/09 · `economie-2026-09-08.md` : 89 £ (L) / 79 £ (M), coût rendu ≈ 38 £ (L grise, seule variante qualifiée GB 6–10 j), marge brute ≈ 34–42 £, break-even ≈ 1 % de conversion à 0,33 £ le clic.

### T-06 — PORTE 1 : positionnement, palette, typo, ton
**État** : VALIDÉ HAKIM 08/09 · DA A (`brand-tokens.json`), prix 89/79 £, ton « you / your cat », promesses vérifiables seulement.

### T-07 — PORTE 2 : structure
**État** : FAIT 08/09 · `sitemap.md` (home 9 sections, PDP 11 sections, guide, FAQ, about, politiques).

### T-08 — Contenus
**État** : FAIT 08/09 · `content/{home,product,faq,guide-adopt,policies-uk,announcement}.md` → pages Shopify créées (guide `712161231231`, FAQ `712161263999`, about `712161296767`), politiques prêtes à coller (`shopify/policies-a-coller.md`, connecteur sans droit `write_legal_policies`).

### T-09 — Fiche produit + DSers
**État** : FAIT PARTIEL 08/09 · Produit `15881611379071` (handle `insulated-outdoor-cat-house`, BROUILLON) : L Grey 89 £ `CCH-L-GREY`, M Grey 79 £ `CCH-M-GREY`, description + SEO ; collection `outdoor-cat-shelters`. **Reste** : mappage DSers (1005010759559289 → variantes), images composées (Higgsfield à 0 crédit), passage en ACTIF.

### T-10 — Build thème FullStack (copie `199695565183`) + QA mobile-first
**État** : FAIT PARTIEL 08/09 · settings/header/footer (orchestrateur), index/product/collection/search/password (agent, journal `2026-09-08-build-theme.md`), démo purgée, 0 preuve sociale. Correctif orchestrateur : `product_source` = handle (le GID ne résout pas) + ancre `how-it-works` (lien menu). **Reste** : images (tous les slots vides), QA préview mobile 375 px bloquée (mot de passe vitrine + Chrome non connecté à l'admin), publication = Hakim.

### T-11 — Tracking Google Ads + GA4 ; campagne Search prête (pause)
**État** : À FAIRE, après SAMPLE_OK · Annonces (6 titres / descriptions) dans `content/announcement.md`.

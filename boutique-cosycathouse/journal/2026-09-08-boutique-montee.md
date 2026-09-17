---
type: journal
boutique: cosycathouse
date: 2026-09-08
nature: intervention
leviers: [page, technique, offre]
titre: "08/09/2026 — Boutique montée : produit, pages, menus, livraison UK, thème de travail"
---

# 08/09/2026 — Boutique montée : produit, pages, menus, livraison UK, thème de travail

Suite du kick-off, après la validation PORTE 1 par Hakim (persona, prix 89/79 £, DA A, réglages, échantillon commandé).

## Fait par l'orchestrateur (Shopify, via connecteur)

- **Produit** `gid://shopify/Product/15881611379071` « Insulated Outdoor Cat House », handle `insulated-outdoor-cat-house`, BROUILLON. Variantes L Grey 89 £ (`CCH-L-GREY`) et M Grey 79 £ (`CCH-M-GREY`). Description HTML et SEO depuis `content/product.md`. Collection `outdoor-cat-shelters`.
- **Pages** : guide d'adoption `help-your-cat-adopt-its-shelter`, FAQ, About (HTML converti depuis `content/`).
- **Menus** : principal (Shop, How it works, Help your cat adopt it, FAQ, Contact, Track your order) et pied de page (politiques, About, Contact).
- **Livraison** : zone « United Kingdom » avec « Free UK delivery (6-10 working days) », GB retiré de la zone International.
- **Politiques** : le connecteur n'a pas le droit `write_legal_policies` → `shopify/policies-a-coller.md` prêt (OH Ventures SASU, numéro TVA à compléter).
- **Thème de travail** (copie FullStack non publiée `199695565183`) : `config/settings_data.json` (polices Varela Round / Nunito Sans, 3 schémas DA A, clé Klaviyo retirée), `sections/header-group.json` (3 annonces anglaises, menu principal), `sections/footer-group.json` (4 réassurances, texte OH Ventures, badge « powered by » et icônes sociales retirés). Empreintes vérifiées après chaque écriture.

## Fait par l'agent build (journal `2026-09-08-build-theme.md`)

`templates/index.json`, `product.json`, `collection.json`, `search.json`, `password.json` : home 9 sections, PDP 11 sections, démo purgée, aucune preuve sociale.

## Correctif après relecture statique

- `product_source` du bloc produit phare de la home portait le GID du produit ; un réglage de type `product` attend le handle. Remplacé par `insulated-outdoor-cat-house`.
- Le lien de menu « How it works » pointe sur `/#how-it-works` ; aucune section ne portait cette ancre. Ancre posée sur la section « mécanisme ».
- Fichier corrigé renvoyé sur le thème (agent Sonnet, payload 70 Ko) : empreinte `9d568b41…` → `794964541192394f07096de50df39974`, 70 853 octets, vérifiée par relecture.

## Relecture statique des templates (sans préview)

- Textes : anglais britannique, promesses conformes à `brand-tokens.json` (« water-resistant », pas de « self-heating », renards traités honnêtement avec les chiffres Cats Protection).
- Réponses FAQ « we'll confirm once we've tested a sample » (capacité, entretien) : acceptables en brouillon, à réécrire après `SAMPLE_OK` avant publication.
- Tous les slots image vides (hero, produit phare, 4 bénéfices) : visuels composés bloqués (Higgsfield 0 crédit).

## Bloqué

- **Préview** : `?preview_theme_id=` renvoie la page mot de passe ; l'éditeur admin demande une connexion Shopify absente du profil Chrome. QA mobile 375 px impossible sans le mot de passe vitrine (ou retrait temporaire) ou une session admin.
- **Devise** : boutique en EUR avec présentation GBP ; à basculer en GBP par Hakim avant la première commande.
- **DSers** : mappage 1005010759559289 (L grise) → variantes non fait.
- **Images**, **politiques**, **tracking** : voir TABLEAU T-09 / T-03 / T-11.

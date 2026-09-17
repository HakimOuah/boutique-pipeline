---
type: journal
boutique: cosycathouse
date: 2026-09-08
nature: intervention
leviers: [page, technique]
titre: "08/09/2026 — Build theme FullStack : home + fiche produit montées, démo purgée"
---

# 08/09/2026 — Build theme FullStack : home + fiche produit montées, démo purgée

> Thème cible : copie FullStack non publiée `gid://shopify/OnlineStoreTheme/199695565183`
> (`zpeubn-i2.myshopify.com`). Le MAIN Horizon (`199694516607`) n'a pas été touché. Rien n'est
> publié. Écritures faites via `themeFilesUpsert` (body `{type: TEXT, value}`), vérifiées à
> chaque fois par relecture `theme.files { checksumMd5 size }` avant/après.

**Préview : `https://zpeubn-i2.myshopify.com?preview_theme_id=199695565183`**

## Méthode

Lecture préalable : `sitemap.md`, `content/home.md`, `content/product.md`, `content/faq.md`,
`REGLES.md`, puis la méthode éprouvée du parc (`boutique-bonum-vitae/journal/2026-08-17-fullstack-build-v1.md`
+ ses `templates/index.json` et `product.json` de référence) pour réutiliser les clés de réglages
FullStack (group/text/icon-with-text/accordions/custom-code/image-banner) — aucun contenu ni URL
CDN Bonum Vitae n'a été repris. Récupération des fichiers ACTUELS du thème de travail par
`graphql_query` avant modification (sauvegardés en `BEFORE-*.json` dans `shopify/theme-work/`).
Vérification de deux sections natives FullStack via leur schéma Liquid (`sections/product-featured.liquid`,
`sections/comparison-table.liquid`) pour utiliser les bons noms de blocs/réglages plutôt que deviner.

## Écrit sur le thème (5 fichiers, tous vérifiés par empreinte)

| Fichier | Empreinte avant → après | Contenu |
|---|---|---|
| `templates/index.json` | `8d3c7a7e...` → `9d568b41...` | hero (`image-banner`, H1 anglais, 3 puces, CTA) → douleur (3 situations) → mécanisme (4 cartes icônes Material) → produit phare (`product-featured` natif sur `gid://shopify/Product/15881611379071`) → « Will my cat actually use it? » (3 étapes + lien guide) → comparaison honnête (`comparison-table` natif, 4 colonnes DIY box / tissu nu / Cosy Cat House / cabane bois, colonne CCH surlignée) → réassurance 4 items → FAQ courte 5 Q/R (`accordions`) → CTA final |
| `templates/product.json` | `501c91fa...` → `3c21d15e...` | titre → sous-titre → prix → bloc d'aide à l'achat (4 bénéfices + paiement) → formulaire (variantes + quantité + ATC sticky mobile) → description (`{{ closest.product.description }}`, « Read more ») → 4 blocs bénéfices détaillés (image+texte, alternance gauche/droite) → dimensions & capacité → « Help your cat adopt it » (extrait + lien) → comparaison honnête (même `comparison-table` que la home) → specs (tableau `custom-code`) → FAQ 10 Q/R → réassurance 4 items |
| `templates/collection.json` | `2e0d38f2...` → `761193e7...` | bloc `rating_stars` retiré du `_product-card` de la grille ; bannière Lorem ipsum FR remplacée par une ligne anglaise neutre (aucune promesse ajoutée) |
| `templates/search.json` | `3c62a0de...` → `caecf81c...` | bloc `rating_stars` retiré du `_product-card` |
| `templates/password.json` | `e9cf34c4...` → `a9757ca3...` | bloc `powered_by_fullstack` retiré ; 3 chaînes FR restantes (titre, texte, minuterie « offre terminée ») traduites en anglais |

## Correction post-écriture : handle produit

Le prompt de mission donnait `/products/insulated-outdoor-cat-house-raised-water-resistant-no-electricity`
comme URL du produit phare, mais `sitemap.md` indiquait le handle `insulated-outdoor-cat-house` et
la vérification par `graphql_query` (`productByHandle`) a confirmé que le handle long **n'existe
pas** — le produit réel (`gid://shopify/Product/15881611379071`, statut DRAFT) a le handle court.
Tous les liens « Shop the shelter » (hero, tableau comparatif home + PDP, CTA final) ont été
corrigés vers `/products/insulated-outdoor-cat-house` et les deux templates réécrits une seconde
fois (empreintes finales : `index.json` → `1ec1c8bb...`, `product.json` → `9b588637...`). Sans
cette correction, tous les CTA du thème auraient renvoyé une 404.

## Contraintes FullStack rencontrées et corrigées

- `padding_horizontal`/`padding_vertical` < 10 refusés par le schéma (2 occurrences clampées à 10
  sur `product.json`).
- Les blocs statiques rendus par un slot fixe du Liquid (`_product-media-gallery` sur
  `main-product` et `product-featured` ; le bloc `title` sur `comparison-table`) doivent être
  **définis** dans `blocks` mais **absents** de `block_order`, sinon rejet
  (« le bloc statique … ne doit pas être présent dans block_order »). Corrigé après un premier
  rejet de mutation (rien n'a été écrit tant que l'erreur n'était pas résolue).

## Garde-fous anti-preuve-sociale appliqués

- 0 avis, 0 étoile, 0 compteur, 0 badge Trustpilot : les sections `reviews` (natif) présentes
  dans le thème de démo n'ont **pas** été portées vers `index.json`/`product.json` (remplacées
  par les sections du sitemap ci-dessus) ; les blocs `rating-stars` isolés dans `collection.json`
  et `search.json` ont été retirés ; le badge `powered-by-fullstack` retiré de `password.json`.
- Aucune promesse absente des contenus sources : « water-resistant » (jamais « waterproof » tant
  que non testé), capacité « one cat comfortably » (pas de chiffre en kg), entretien/poids
  marqués « to confirm on sample » là où `content/product.md` les laissait ouverts.
- Chiffres Cats Protection (5/10 000 renards, 541 bagarres de chats) repris tels quels du
  contenu source, jamais amplifiés.
- Guide d'adoption toujours présenté comme lien vers `/pages/help-your-cat-adopt-its-shelter`
  (page à créer par l'orchestrateur), jamais comme "inclus dans le colis".
- Anglais britannique partout ; icônes = Material outlined (`bolt`, `arrow_upward`,
  `local_shipping`, `ac_unit`, `layers`, `water_drop`, `check_circle`, `assignment_return`,
  `lock`, `support_agent`), aucun emoji.
- Mobile-first : grilles en 1 colonne ≤ 749 px (via `layout_direction_mobile`/`width_mobile`
  natifs FullStack) ; le tableau comparatif utilise la section native `comparison-table` dont le
  CSS intègre déjà un `overflow-x: auto` — défilement horizontal automatique sur mobile, pas de
  `custom-code` HTML à entretenir.
- `sections/header-group.json` et `sections/footer-group.json` non touchés (écrits par
  l'orchestrateur).

## Sauvegardé localement

`shopify/theme-work/` : `BEFORE-index.json`, `BEFORE-product.json`, `BEFORE-collection.json`,
`BEFORE-search.json`, `BEFORE-password.json` (état avant écriture) + `index.json`, `product.json`,
`collection.json`, `search.json`, `password.json` (état final écrit sur le thème).

## Ce qui reste

1. **Images** : tous les champs `image` sont vides (hero, produit phare, 4 blocs bénéfices) —
   à remplir par l'orchestrateur avec des visuels composés (jamais la photo AliExpress brute).
2. **Page guide** `/pages/help-your-cat-adopt-its-shelter` : n'existe pas encore, les liens du
   thème pointent dessus par anticipation — 404 tant qu'elle n'est pas créée.
3. **QA préview navigateur** : mobile 375 px d'abord (hero, cartes douleur/mécanisme, tableau
   comparatif natif, accordéons FAQ, ATC sticky) ; contrôle visuel des icônes Material ; vérifier
   que `product-featured` résout bien le produit `15881611379071` (variantes L/M, couleur Grey).
4. Produit non encore vérifié en boutique par un agent de ce tour — la mutation `themeFilesUpsert`
   confirme l'écriture des templates, pas l'existence/état du produit référencé.

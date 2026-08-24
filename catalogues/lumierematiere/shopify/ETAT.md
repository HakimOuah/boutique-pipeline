# Shopify Lumière Matière — état 24/08/2026 (soir, overlay + variantes + policies)

**Store :** `nzefxg-gg.myshopify.com`  
**Admin :** https://admin.shopify.com/store/nzefxg-gg  
**Compte API :** `contact@lumierematiere.fr` (auth CLI `shopify store auth`)  
**Thème de travail (non publié) :** `copie-de-fullstack-2-3` · `gid://shopify/OnlineStoreTheme/186708001104`  
**Prévisualisation Full Stack :** https://nzefxg-gg.myshopify.com/?preview_theme_id=186708001104  
**Thème publié (MAIN) :** Helio · `gid://shopify/OnlineStoreTheme/186709180752` — ne pas y coller de DA ; Hakim publie. `page.faq.json` y a été cloné (identique à `page.json`) pour que le suffixe FAQ vive aussi en live.

## Fait

- **Policies** réimportées 24/08 soir (pack FR `gmc-acceptance/templates-fr/`, texte LM distinct). Chiffres ops inchangés : cut-off **16h Paris**, préparation **1–2 j**, acheminement **6–15 j**, total **7–17 j**, retours **30 j**, annulation **tant que non expédiée**, SAV **10h–18h**, réponse **24 h ouvrées**.
- **Paiement** aligné sur `/payments/config` : Visa, Mastercard, American Express, Apple Pay, Shop Pay, PayPal. **Pas de Google Pay.** CGV + page Paiement mises à jour.
- **121 fiches API supprimées**, puis **PUSH DSers** (Hakim). Overlay 24/08 soir :
  - **120 fiches** mappées (titres FR, HTML VOC, prix, collections UNIVERS, publiées Online Store).
  - Images Codex g1–g5 (hors **LM-086** REJECT — images DSers conservées).
  - **3 doublons DSers** passés en brouillon.
  - **LM-045** absent (listing AliExpress mort).
- **Prix barrés retirés** (compareAt = null sur toutes les variantes actives).
- **Variantes traduites / réordonnées** : Taille → Couleur → Température → Ampoule / Entrepôt. Entrepôt Chine-only supprimé (11 fiches). SKU DSers (`sku_attr`) **non modifiés**.
- **Copy Fable (24/08 soir)** : tournures défensives retirées (Notre histoire, FAQ, paiement, CGV, livraison, 120 fiches). Plus de « ce que nous ne sommes pas », « usine artisanale fictive », AliExpress, Google Pay en négatif.
- **OH Ventures** : uniquement dans les policies (CGV, confidentialité, mentions légales). Footer + pages CMS au nom de la marque (adresse / e-mail / tél conservés).
- **Thème Full Stack** (`copie-de-fullstack-2-3`) : tokens papier `#F6F3EC` / charbon `#24211B` / ambre `#C08A2D`, Young Serif + Instrument Sans, logos, homepage UNIVERS. Démos avis / Trustpilot retirées. Gabarit `templates/page.faq.json` ajouté ; page FAQ en suffixe `faq`.
- **SEO collections (24/08 soir)** : 14 collections (description HTML + `seo.title` / `seo.description`) — mots-clés FR par matière (`suspension bambou`, `lustre salon`, `plafonnier`, `lustre cristal` en « effet cristal », etc.). Template Full Stack `templates/collection.json` : Lorem Ipsum remplacé par `{{ closest.collection.description }}`. Helio / UNIVERS non touchés. Source : `shopify/collections-seo.json`.

## Prix (règle maison)

Coût DSers (unité) + **2 € de fret** (quotes FR : 1,99 € / 0 €). Concurrent d’abord (grille 149 / 199 / 249 / 299), on remonte si marge HT < 40 € ou < 25 % du HT. Plus de prix barré. SKU DSers (`sku_attr`) **non modifiés**.

| Palier min TTC | SKU |
|---|---|
| 149 € | 1 (LM-062) |
| 199 € | 63 |
| 249 € | 50 |
| 299 € | 4 |
| 349 € min (csv 299, marge) | 2 (LM-070, LM-071 cristal) |

26 fiches ont plusieurs paliers selon la taille (XXL plus cher). 94 fiches = un seul prix.

## À faire Hakim

1. Prévisualiser `copie-de-fullstack-2-3` **avant de publier** (Helio est actuellement MAIN).
2. Recette paiement footer Helio vs checkout vs `/payments/config` (wallets : Apple Pay, Shop Pay, PayPal — pas Google Pay).
3. CM2C : ajouter lumierematiere.fr si le contrat est par site.
4. Décider du sort de **LM-045** (listing AE mort).
5. 5 fiches « Unmapped » DSers (fantômes API) : à supprimer dans l’app si elles sont encore là.

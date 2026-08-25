# Shopify Lumière Matière — état 25/08/2026 (copy humanisée)

**Store :** `nzefxg-gg.myshopify.com`  
**Admin :** https://admin.shopify.com/store/nzefxg-gg  
**Compte API :** `contact@lumierematiere.fr` (auth CLI `shopify store auth`)  
**Thème de travail (non publié) :** `copie-de-fullstack-2-3` · `gid://shopify/OnlineStoreTheme/186708001104`  
**Prévisualisation Full Stack :** https://nzefxg-gg.myshopify.com/?preview_theme_id=186708001104  
**Thème publié (MAIN) :** Full Stack `copie-de-fullstack-2-3` · `gid://shopify/OnlineStoreTheme/186708001104` — publié par Hakim le 25/08 soir, mot de passe retiré. Helio et UNIVERS restent en brouillon.

## Fait

- **Panier 25/08 soir (recette 12b)** : bannière franco (plus de barre « plus que 30 € »), upsell « À regarder aussi » (4 handles, max 2, AJAX), accordéons retours 30 j + livraison offerte, grille « Autour de 199 € » sous `/cart`. Tiroir + page. Script : `shopify/patch_cart.py`. Helio / UNIVERS non écrits.
- **SEO accueil 25/08 soir** : titre `Suspensions et lustres par matière | Lumière Matière` (52/70), méta 148/320, image de partage 1200×628 (logo charbon sur papier `#F6F3EC`). Script : `shopify/set_homepage_seo.py`. Metafields `global.title_tag` / `description_tag` / `social_sharing_image`. 0 tiret cadratin / demi-cadratin dans le texte client (pages, policies, home, header, footer, 14 collections, 120 fiches, 536 valeurs d’option, 747 alt). Cadence machine cassée (anaphores « matière / lumière », tricolons, ouvertures identiques). Rapports : `HUMANISATION-PAGES-2026-08-25.md`, `HUMANISATION-THEME-2026-08-25.md`, `HUMANISATION-PDP-2026-08-25.md`, `HUMANISATION-OPTIONS-2026-08-25.md`. Helio / UNIVERS non écrits.
- **Libellés de variantes + alt 25/08 soir** : 60 valeurs renommées (15 fiches), 747 alt réécrits, 0 cadratin, 0 alt vide. Trois sélecteurs qui mentaient au SKU corrigés (lot de 2 vs unité sur 709819 et 104055 ; noir non annoncé sur 957153 ; températures doublonnées sur 343987). SKU 602/629 inchangés (`variantStrategy: LEAVE_AS_IS`). Script : `shopify/humanise_options.py`. 9 `specs_html` réalignés via `push_copy` seulement.
- **120 fiches 25/08 soir** : `copy OK 120/120`, titres uniques 120/120 (13 groupes de doublons / 32 fiches). 56 titres réécrits parce que la photo contredisait le nom ; 31 sources lumineuses retypées (plus de « LED ou E27 » sur des fiches sans cet axe). Option `suspension-effet-pierre-092465` : « Blanc chaud » → **Pierre claire** (SKU inchangés). Script : `shopify/humanise_pdp.py` + `apply_pdp.push_copy` seulement — **ne pas lancer `apply_pdp.py` en entier**.
- **Home / collections 25/08 soir** : sous-titre 199 € sans cadratin ; titres home variés (`Par matière`, `Où voulez-vous de la lumière ?`, `À vous de voir`). 14 descriptions de collections poussées. Scripts alignés : `humanise_theme.py`, `apply_fullstack.py`, `patch_home.py`. **Ne pas relancer `apply_fullstack.py` ni `patch_home.py` en entier.**
- **Hero Full Stack 25/08 soir** : blocs démo Trustpilot « 1988 avis » et « 2 000 clients satisfaits » **supprimés** du JSON (plus seulement désactivés).
- **FAQ Q14** : suivi via ParcelPanel (`/apps/parcelpanel`) + compte. Hakim confirme l’app installée et fonctionnelle.
- **Collections 25/08 soir** : `frontpage`, `lustres-statement` et `suspensions-modernes` dépubliées de la boutique en ligne (1 produit / hors menu).
- **GMC** : Workspace créé ; **pas de Merchant Center avant 30 j** de vie du domaine + compte Google. Search Console = Hakim.
- **Édito home 25/08** : placeholder vidéo de « La matière fait la lumière » remplacé par la photo lifestyle `lumierematiere-home-table.jpg`.
- **Footer Full Stack 25/08 (modèle Montre Avenue)** : 4 colonnes (marque + Menu principal + Informations + infolettre). E-mail `mailto:contact@lumierematiere.fr`, téléphone `tel:+33756828094`, Contact `/pages/contact` cliquables (colonne marque + carte SAV). Menus dédiés `footer-principal` / `footer-informations` (le `main-menu` et le menu Helio `footer` ne sont pas touchés — donc pas de ParcelPanel dans le pied). Icônes sociales désactivées (aucun compte). Script : `shopify/patch_footer.py`. Helio non écrit.
- **Profil de livraison 25/08 (P1 audit, corrigé)** : une seule zone **France** (pays FR), une seule méthode **Livraison offerte 0 €** sans seuil. Standard 7,99 €, Express 10,99 €, zones UE (22 €) et International (29 €) supprimées. Script rejouable : `shopify/configure_shipping.py`. Les marchés Shopify n’ont pas pu être lus (`read_markets` absent du token CLI) — Hakim peut vérifier Réglages → Marchés : seul le marché France doit rester actif.
- **Home enrichie 25/08 après-midi (Fable), titres humanisés le soir** : `templates/index.json` live sur Full Stack — sous-titre grille matières, section « Où voulez-vous de la lumière ? » (3 cartes job-to-be-done avec CTA collections), guide « Bien choisir, en trois étapes » (matière → diamètre → ampoule, fond charbon), CTA final « À vous de voir » (preuves vraies : livraison offerte + retours 30 j, 2 boutons). Bloc défensif « sans cristal inventé ni atelier fictif » remplacé par un bénéfice positif. Script : `shopify/patch_home.py` (backups : `shopify/backups/2026-08-25-home-enrichie/` et `shopify/backups/2026-08-25-humanisation/`). `apply_fullstack.py` aligné — **ne pas le relancer en entier**.
- **`/collections` curatée 25/08** : `templates/list-collections.json` limité aux 11 collections du menu (exclut `frontpage`, `selection-199` sans image, `lustres-statement` et `suspensions-modernes` à 1 produit).
- **Audit de cohérence 25/08** : `shopify/AUDIT-COHERENCE-2026-08-25.md` — P1 livraison corrigé. ParcelPanel, blocs démo hero et **titres dupliqués (P2)** soldés.
- **Packshots teinte Codex rattachés 25/08** : 49 fiches, **124 JPEG** uploadés et liés aux variantes (une image par câble / verre / finition / abat-jour / émail / teinte). Galerie g1–g5 conservée. SKU DSers inchangés. Script : `shopify/attach_variant_packshots.py`. Livraison : `livraisons-visuels-codex/variantes-couleur/` (QA Codex 124/124).
- **Noms d’axes 25/08 soir** : `Couleur` générique retiré là où ça mentait. Bambou 583180 / 033589 / 280004 : **Câble** (SKU `X line` = câble + rosace, abat-jour naturel). Ailleurs : Verre, Finition, Abat-jour, Émail, Modèle, Diamètre (si uniquement des Ø), Lumières, Puissance, Ampoule. Titres/USP/specs/FAQ alignés (`câble blanc, noir ou doré`, pas « bambou doré »). Script : `shopify/rename_option_axes.py`. Rapport : `shopify/variants-position-2026-08-25.md`. SKU DSers inchangés.
- **Variantes repositionnées 25/08 (Fable)** : 76 fiches modifiées, **2 868 → 629 variantes** (rapport : `shopify/variants-position-2026-08-25.md`, script : `shopify/position_variants.py`). « Damaged replacement » supprimé (2 fiches bambou), `X line` → couleur seule, `heads` → lumières, codes usine (Type A–E, sku1–22, Ceramic 1–23, 4040…) réduits ou dépliés, une seule température quand le prix n'en dépend pas, 3 couleurs max, tailles en paliers commerciaux triés. Prix hors grille (résidus de coûts AE 31–231 €) purgés en supprimant les variantes concernées — plus aucun prix hors 149–499. **0 split** : `productDuplicate` créerait des fiches non mappées DSers (un listing AE = une fiche) → réduction sur place pour les 7 fiches 100+ (anneaux 1–2 vs 3–5, cristal rond vs allongé, bambou plafonnier vs suspension). SKU/`sku_attr` DSers **inchangés** sur toutes les variantes conservées. Restent volontairement >12 : 489156, 091815, 583180, 033589 (15 var = tailles × couleurs réelles). À vérifier : 453740 et 201424 réduites à 1 variante aveugle (contrôler la correspondance photo/listing AE) ; codes 607504 interprétés en dimensions. Brief Codex couleurs régénéré (41 fiches).
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
- **PDP Full Stack (24/08 soir, gabarit type Montre Avenue)** : titres descriptifs (plus de références type `· 83180`) ; pills USP sous le titre ; 4 accordéons (Description, Caractéristiques, Livraison et retour, Installation) ; 3 blocs image/texte + FAQ produit (métachamps `custom.usps|specs|installation|benefits|faq`) ; produits liés en dernier. Option Entrepôt retirée (entrepôt UE conservé). Image g1 attachée à chaque variante en attendant les packshots couleur. SKU DSers inchangés. Brief Codex : `catalogues/lumierematiere/briefs/2026-08-24-codex-variantes-couleur.md` (67 fiches multi-couleurs). Helio non touché.

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

1. Recette checkout (wallets : Apple Pay, Shop Pay, PayPal). QA mobile 375 du panier (tiroir + `/cart`).
2. **GMC : ne pas créer maintenant.** Workspace créé. Faire vivre le domaine ≥ 30 jours + le compte Google, Search Console branchée (Hakim). Soumission Merchant Center seulement après.
3. CM2C : ajouter lumierematiere.fr si le contrat est par site.
4. Décider du sort de **LM-045** (listing AE mort).
5. 5 fiches « Unmapped » DSers (fantômes API) : à supprimer dans l’app si elles sont encore là.
6. Vérifier `suspension-bois-led-453740` et `suspension-verre-noir-201424` (réduites à 1 variante sur des codes aveugles) face au listing AE.

# Shopify Lumière Matière — état 25/08/2026 (home enrichie + audit cohérence)

**Store :** `nzefxg-gg.myshopify.com`  
**Admin :** https://admin.shopify.com/store/nzefxg-gg  
**Compte API :** `contact@lumierematiere.fr` (auth CLI `shopify store auth`)  
**Thème de travail (non publié) :** `copie-de-fullstack-2-3` · `gid://shopify/OnlineStoreTheme/186708001104`  
**Prévisualisation Full Stack :** https://nzefxg-gg.myshopify.com/?preview_theme_id=186708001104  
**Thème publié (MAIN) :** Helio · `gid://shopify/OnlineStoreTheme/186709180752` — ne pas y coller de DA ; Hakim publie. `page.faq.json` y a été cloné (identique à `page.json`) pour que le suffixe FAQ vive aussi en live.

## Fait

- **Home enrichie 25/08 après-midi (Fable)** : `templates/index.json` live sur Full Stack — sous-titre grille matières, section « Ce que la matière change, pièce par pièce » (3 cartes job-to-be-done avec CTA collections), guide « Bien choisir, en trois étapes » (matière → diamètre → ampoule, fond charbon), CTA final « Commencez par la matière » (preuves vraies : livraison offerte + retours 30 j, 2 boutons). Bloc défensif « sans cristal inventé ni atelier fictif » remplacé par un bénéfice positif. Script rejouable : `shopify/patch_home.py` (backups avant/après : `shopify/backups/2026-08-25-home-enrichie/`). `apply_fullstack.py` aligné (ordre de sections + sous-titre) pour ne plus écraser la home — **ne toujours pas le relancer en entier**.
- **`/collections` curatée 25/08** : `templates/list-collections.json` limité aux 11 collections du menu (exclut `frontpage`, `selection-199` sans image, `lustres-statement` et `suspensions-modernes` à 1 produit).
- **Audit de cohérence 25/08** : `shopify/AUDIT-COHERENCE-2026-08-25.md` — verdict + findings P1/P2/P3. P1 : profil de livraison Shopify (Standard 7,99 €, Express 10,99 €, zones UE/International) contredit « livraison offerte, France métropolitaine » ; P2 : 13 groupes de titres dupliqués (31 fiches), lien menu `/apps/parcelpanel` à vérifier, blocs démo à faux chiffres désactivés mais présents dans le JSON du hero.
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

0. **P1 audit — réglages Expéditions** : ne garder qu'un `Standard 0 €` sans condition sur la zone France ; supprimer `Standard 7,99 €`, `Express 10,99 €` et les zones UE (22 €) / International (29 €) — le site entier promet « livraison offerte, France métropolitaine » uniquement (détail : `AUDIT-COHERENCE-2026-08-25.md`).
1. Prévisualiser la home enrichie + la fiche Full Stack (titre, USP, 4 accordéons, 3 bénéfices, FAQ, liés) : `?preview_theme_id=186708001104` **avant de publier** (Helio est actuellement MAIN). QA mobile 375 non faite (mot de passe storefront).
2. Recette paiement footer Helio vs checkout vs `/payments/config` (wallets : Apple Pay, Shop Pay, PayPal — pas Google Pay).
3. CM2C : ajouter lumierematiere.fr si le contrat est par site.
4. Décider du sort de **LM-045** (listing AE mort).
5. 5 fiches « Unmapped » DSers (fantômes API) : à supprimer dans l’app si elles sont encore là.
6. Vérifier `suspension-bois-led-453740` et `suspension-verre-noir-201424` (réduites à 1 variante sur des codes aveugles) : la variante conservée doit correspondre à la photo g1 face au listing AE, sinon re-mapper côté DSers.
7. Vérifier l'app ParcelPanel (menu « Suivre votre commande » → `/apps/parcelpanel`) ; sinon pointer `/account` et harmoniser avec la FAQ Q14.
8. Feu vert pour supprimer du JSON du hero les blocs démo désactivés à faux chiffres (« 1988 avis », « 2 000 clients satisfaits ») — exécution agent 2 min.

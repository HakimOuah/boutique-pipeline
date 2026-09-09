# État de la boutique Shopify Sous Abri (zpeubn-i2 → sousabri.fr) — 09/09/2026, nuit

Fait par l'API (connecteur) :
- Catalogue : 12 collections (11 SEO + « Tentes-garages » pour le menu), 10 produits en BROUILLON aux prix décidés, 10 pages. IDs : `ids-crees.json`. Métachamps : 14 définitions, 124 valeurs (`metafields.json`).
- Publication : 10 pages publiées, 12 collections publiées sur « Boutique en ligne » (publication 352235487615). Produits : toujours DRAFT (le carport acier a servi de test de gabarit puis est repassé en brouillon ; il reste publié sur le canal, donc visible dès qu'il passe ACTIVE).
- Descriptions de collections : intro seule (le texte SEO long est dans `custom.texte_seo`, rendu en bas de page par le gabarit). Images : carport-alu, tentes-garages, carport-camping-car.
- Pages devis (3) : corps client reconstruit par `build_devis_pages.py` (`payload-devis-pages.json`), gabarit `page.devis` (formulaire de devis en Liquid, section « pourquoi un devis », FAQ devis, réassurance).
- Menus : principal, footer, footer-boutique, footer-aide, footer-apropos. Livraison : zone France, offerte. Marché France.
- Domaine : `zpeubn-i2.myshopify.com` redirige vers `sousabri.fr` (fait par Hakim). Boutique sous mot de passe.
- Files : 6 visuels lot 1, hero `sousabri-hero.jpg`, 2 visuels guides, logos et favicon (`images-lot1.json`, `images-marque.json`). Médias produits : voir `medias-produits-2026-09-09.json` et le plan `plan-medias-produits.json`.

Thème « Sous Abri » 199781745023 (Self Made Theme, NON publié) — fichiers poussés depuis `theme-sousabri/work/` : settings_data (couleurs, polices, logo, favicon), header-group, footer-group, index, product, collection, page, page.contact, page.devis.
- Règle apprise : un métachamp texte contenant du HTML ne passe pas par un réglage `richtext` (validation « nœuds p/ul/ol/h1-h6 » + échappement) ; on le rend via un bloc/section `custom_liquid` (`{{ product.metafields.custom.x.value }}`) avec le CSS des accordéons dans le même bloc (voir `product.json`, `page.json`, `page.devis.json`).
- Contrôle visuel bureau fait dans Chrome (accueil, guide, contact, devis, collection, fiche produit). Contrôle mobile impossible sans mot de passe boutique ou lien de partage de prévisualisation (fenêtre Chrome non redimensionnable, iframe bloquée, Playwright bloqué par le mot de passe).
- Prévisualisation : https://sousabri.fr/?preview_theme_id=199781745023

Reste côté Hakim (admin) : politiques à coller (`content/politiques/politiques-a-coller.md`), activation Klarna + PayPal 4×, e-mail expéditeur, avis clients (section retirée de l'accueil tant qu'il n'y en a pas), lien de partage de prévisualisation pour la QA mobile.
Visuels (10/09) : lot 2 complet (50/50 après l'ordre de reprise `20260910-0040`), lot 3 = cintré face + situation, guides déclaration, montage et comparatif ; manquent seulement les vues toit plat et adossé (sources fournisseur inexistantes, photos réelles à demander). Produit test « Abri de voiture moderne… » (29,99 €, créé par erreur le 09/09) supprimé le 10/09 à la demande de Hakim.
Reste côté build : contrôle des `[À VÉRIFIER]`/`[À DÉCIDER]` puis passage des produits en ACTIVE, prix d'appel des pages devis, publication du thème (par Hakim).

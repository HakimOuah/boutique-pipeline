# Plan de push — Sous Abri sur le thème Self Made Theme (199781745023, non publié)

Préparation strictement LOCALE : aucun appel Shopify en écriture n'a été effectué pour produire `work/` (lecture seule, `graphql_query` uniquement). Tous les JSON de `work/` sont validés avec `python -m json.tool`. Ce plan remplace celui de `../theme-work/PUSH-PLAN-2026-09-10.md`, qui visait l'ancien thème FullStack (`199695565183`, push interrompu) — ne pas pousser ce dernier sur ce thème, les types de section ne correspondent pas.

## 0. Préalable Shopify (mutations, hors périmètre de cette mission)

1. **Metafields produit** namespace `custom` (liste et types au §4 de `CAPACITES.md`) sur les 10 fiches à prix fixe.
2. **Metafield collection** `custom.texte_seo` (rich text) sur les 11 collections.
3. **Menus** : `main-menu` (5 entrées + sous-menu Guides), `footer-boutique`, `footer-aide`, `footer-apropos` (contenu exact dans `content/pages/annonces-menu-footer.md`).
4. **Pages à créer** (template `page` par défaut sauf mention) : `guide-declaration-carport`, `faq`, `qui-sommes-nous`, `garantie-livraison-sav`, `comparatif-carport-tente-garage` (contenu déjà rédigé dans `content/pages/*.md`, à coller dans le corps de la Page Shopify — le template `page.json` ne porte pas ce texte, il se contente d'afficher `page.content`), `contact` (template `page.contact`), et les 3 pages devis avec le template `page.devis` : `devis-carport-aluminium-toit-plat`, `devis-carport-aluminium-adosse`, `devis-carport-cintre-2-pieds`.
5. **Politiques natives** (`content/politiques/politiques-a-coller.md`) : livraison, retour, CGV, confidentialité, mentions légales.
6. **Images** : téléverser `sousabri-hero.jpg` (2048×1152) dès qu'il est produit — sans lui, la section hero de l'accueil affichera un placeholder gris. Lot 1 (6 images) déjà en place.
7. **Logo** : `work/config/settings_data.json` laisse `logo: null` (fallback texte). Téléverser dès qu'il existe et renseigner `settings.logo` dans l'éditeur, ou dans un `settings_data.json` mis à jour.
8. **Paiement** : vérifier dans Shopify Payments/apps que carte, PayPal (4×), Klarna (3×), Apple Pay et Shop Pay sont actifs — la ligne de texte du footer et la réassurance produit l'annoncent déjà.

## 1. Ordre de push (`themeFilesUpsert`, body TEXT, un thème NON publié — aucun risque pour la boutique live)

1. `config/settings_data.json` — couleurs, polices, cartes (voir §7 de `CAPACITES.md`). Pousser en premier : les sections suivantes dépendent des schémas de couleur `background-1/2`, `accent-1/2`, `inverse`.
2. `sections/header-group.json` — barre d'annonce (3 messages sans urgence) + header (menu `main-menu`, recherche activée, pas de sélecteur pays/langue).
3. `sections/footer-group.json` — 3 colonnes de menus + bloc coordonnées OH Ventures + moyens de paiement. **Nécessite que les 3 menus `footer-*` existent déjà** (étape 0.3), sinon les blocs `link_list` resteront vides à l'affichage.
4. `templates/index.json` — 11 sections (hero, douleur, mécanisme, familles, familles-devis, déclarer, comparaison, réassurance, avis (vide), FAQ, CTA final). **Nécessite `sousabri-hero.jpg` téléversée**, sinon repousser cette étape ou accepter le placeholder temporairement.
5. `templates/product.json` — gabarit générique des 10 fiches à prix fixe, piloté par les metafields `custom.*` (étape 0.1). Sans les metafields remplis, les collapsibles et le sous-titre afficheront du contenu vide (pas d'erreur, juste des blocs blancs) — acceptable pour un aperçu de structure, à compléter avant publication réelle.
6. `templates/collection.json` — générique pour les 11 collections, section SEO sous la grille pilotée par `custom.texte_seo` (étape 0.2).
7. `templates/page.json` — générique (guide déclaration, guide montage, comparatif, qui-sommes-nous, garantie/SAV, FAQ éditoriale). Le contenu de chaque page vit dans la ressource Page elle-même (étape 0.4), pas dans ce template.
8. `templates/page.contact.json` — intro + formulaire de contact natif (nom/e-mail/téléphone/message uniquement, voir limitation §3 de `CAPACITES.md`) + coordonnées.
9. `templates/page.devis.json` — hero + formulaire `custom-liquid` (tous les champs du devis) + pourquoi un devis + rappel déclaration + FAQ + réassurance. À assigner aux 3 pages devis (étape 0.4) ; le contenu (H1, sous-titre, FAQ) est celui de l'exemple « carport cintré 2 pieds » (`content/produits/MODELE-page-devis-carport-aluminium.md`) — **à adapter pour les 2 autres pages devis (toit plat, adossé) avant de les assigner telles quelles**, sinon les 3 pages afficheront le même H1.

## 2. Contrôles après push (thème non publié : prévisualiser via l'aperçu du thème brouillon)

- Accueil et fiche produit en préview mobile 375 px et desktop.
- **Aucun** avis, aucune note, aucun prix barré, aucune urgence (compte à rebours, « plus que X en stock ») nulle part — vérifier en particulier la section `avis` (doit rester visuellement vide ou masquée tant qu'aucun avis réel n'est importé).
- Police Archivo sur les titres, Inter sur le corps (si disponibles — sinon noter la police de repli utilisée et prévenir Hakim).
- Palette conforme à `brand-tokens.json` (fond `#F4F1EA`, accent `#C8552B`, secondaire `#2F4A5A`).
- Formulaire de contact et formulaire de devis soumettent bien (test avec une fausse valeur, vérifier la réception côté marchand, y compris les champs additionnels du devis dans le corps de l'e-mail).
- Tableau comparatif lisible sur mobile.
- Collapsibles produit : les 7 volets s'affichent dans l'ordre (dimensions en premier, ouvert par défaut), le contenu vient bien du metafield une fois rempli.
- Section FAQ produit (`custom-liquid`) : vérifier que le HTML `<details>` du metafield `custom.faq` s'affiche correctement (pas de balises échappées).
- Liens de la section « familles » (accueil) : confirmer le mapping `carport-metallique` → « Tentes-garages » avec Hakim, ou créer la collection dédiée avant le push définitif.
- Empreinte du thème : comme pour les autres boutiques du parc, vérifier après push que le contenu poussé correspond bien au fichier local (le connecteur peut refuser d'écrire sur un thème publié, mais celui-ci est en brouillon — vérifier tout de même par relecture après upsert).

## 3. Décisions restant à Hakim

- Lien de la carte famille « Tentes-garages » (accueil + mécanisme) et entrée de menu correspondante : pas de collection `tentes-garages` dédiée parmi les 11 créées — pointé provisoirement vers `carport-metallique`.
- Prix d'appel des 3 pages devis (`[À DÉCIDER]` dans `page.devis.json` et `MODELE-page-devis-carport-aluminium.md`).
- Contenu spécifique des pages devis « toit plat » et « adossé » (actuellement, `templates/page.devis.json` porte le texte de l'exemple « cintré 2 pieds » — à dupliquer et adapter par Hakim ou un agent dédié avant d'assigner le template aux 3 pages).
- Faut-il ajouter un champ « sujet » ou « pièce jointe » au formulaire de contact standard ? La section native ne le permet pas ; la solution serait la même technique `custom-liquid` que pour le devis.
- Activer ou non la barre de seuil de livraison gratuite (`enable_free_bar`) — la promesse est « livraison offerte » sans minimum, donc probablement à désactiver pour ne pas laisser un réglage par défaut contredire le message.
- Logo, favicon et `sousabri-hero.jpg` : à produire puis téléverser (voir §0.6-0.7) avant toute publication réelle.

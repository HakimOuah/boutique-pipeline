# NOIRMONT — Build du site (24/07/2026, session autonome)

Boutique : v42pzp-h4.myshopify.com · maisonnoirmont.fr · Thème brouillon « Maison Noirmont » (gid 204248088914, non publié)
Prévisualisation : `/?preview_theme_id=204248088914` · mot de passe boutique : `[RETIRÉ — voir docs/codex-handoff/07-SETUP-AND-SECRETS.md]`

## Réalisé

### Catalogue
- 25 produits DSers francisés (titres, handles, descriptions charte, types, tags) — fait plus tôt dans la session.
- ~540 prix de variantes : montres 279–379 € fixes, accessoires coût ×2,2 arrondi X4,90/X9,90 (plancher 12,90 €).
- Collections : plongeuses / gmt / classiques / chronos / sport-chic / accessoires peuplées + **nouvelle collection « Les Montres »** (handle `montres`, id 690663162194) avec les 10 garde-temps.
- **Publication canal** : produits DSers et collections API n'étaient publiés sur AUCUN canal → `publishablePublish` sur les 3 publications (dont Boutique en ligne) pour 25 produits + 7 collections.

### Visuels (Higgsfield, modèle soul_2, ~17 crédits)
- 8 visuels de marque uploadés dans Shopify Files : `noirmont-hero.jpg`, `noirmont-plongeuses.jpg`, `noirmont-gmt.jpg`, `noirmont-classiques.jpg`, `noirmont-chronos.jpg`, `noirmont-sport-chic.jpg`, `noirmont-accessoires.jpg`, `noirmont-maison.jpg`.
- Problème : le modèle imprime de faux logos/textes sur tout cadran face caméra. Solutions combinées : compositions cachant le cadran (angles rasants, macros lunette) + **inpainting OpenCV local** (venv scratchpad) sur les zones de texte.
- Images assignées aux 7 collections + hero/sections du thème.

### Identité
- Wordmark intérimaire « MAISON NOIRMONT » généré en Bodoni Moda 500 (PIL, letterspacing 0.16em) : `logo-noirmont-encre.png` + `logo-noirmont-craie.png` (inverse). Monogramme N à faire.
- Polices custom uploadées dans Files : `bodoni-moda-500.woff2`, `inter-400.woff2`, `space-grotesk-500.woff2` (sous-ensembles latin Google Fonts).

### Thème (fichiers poussés via staged upload PUT + themeFilesUpsert avec resourceUrl non signé)
- `config/settings_data.json` : schémas de couleurs charte (scheme-1 craie, scheme-2 pierre, scheme-3 encre ; boutons vert-jura #1E3A2F, étoiles laiton #A98E5F), typo custom (Bodoni/Space Grotesk/Inter), H1-H2 uppercase letterspacing loose, angles nets (radius custom : boutons 0, cartes 2), boutons uppercase, Klaviyo démo désactivé, logo + logo_inverse.
- `templates/index.json` : home calquée Tuftéo — hero (badge avis démo étiqueté, H1 « Votre signature au poignet », CTA montres, 2 réassurances) → ticker marquee encre → « Les garde-temps » (slider collection montres) → « Ils portent Noirmont » (6 avis démo étiquetés « à remplacer ») → « Composez la vôtre » (section encre, knolling, 3 étapes, CTA configurateur) → grille 6 collections → « Le rituel » (accessoires) → « L'allure d'abord » (La Maison, pierre) → specs NH35/316L/Saphir → newsletter « Entrez dans le cercle ».
- `templates/product.json` : accordéons Livraison (« généralement 2 à 3 semaines », jamais promesse absolue) + Retours 14 j ; FAQ bas de fiche (livraison, retours, fabrication & contrôle, garantie 12 mois, entretien) ; sections marque avec visuels ; avis démo étiquetés ; icônes livraison/paiement/montage contrôlé.
- `sections/header-group.json` : 3 annonces charte, menu uppercase.
- `sections/footer-group.json` : réassurance ×4 (livraison, paiement, garantie 12 mois, réponse <24 h), footer encre avec wordmark craie + blurb, badge FullStack désactivé.
- Menus : main-menu (Montres + 5 sous-collections, Accessoires, Configurateur, La Maison, FAQ, Contact) + footer (FAQ, Contact, La Maison, Configurateur).

### QA
- Desktop (Chrome, session admin contact.noirmont@gmail.com) : home complète, PDP, footer — OK.
- Mobile (375px) : hero/header/ticker — OK.

## Reste à faire
1. **Images produits** : remplacer les visuels AliExpress avec watermarks vendeur (Tandorio, 6698 Watch Store, BL, Custom Logo…) — tri manuel Hakim + génération.
2. **Options de variantes en anglais** (Color/Size, « BRONZE CASE-NO LOGO », « NH35-STEEL BACK »…) : renommage massif à faire prudemment (vérifier l'impact mapping DSers avant).
3. Avis réels (remplacer les 6+6 slides démo + badge hero).
4. Logo définitif (monogramme N cercle + index laiton 12 h, brief dans la charte).
5. Page configurateur réelle (proto HTML existant dans le scratchpad/artifact).
6. Seuil de la barre « livraison offerte dès 30 € » du tiroir panier à aligner (livraison offerte partout).
7. Publier le thème après validation Hakim.

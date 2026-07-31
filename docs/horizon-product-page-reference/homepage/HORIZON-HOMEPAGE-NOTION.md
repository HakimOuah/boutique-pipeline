# Homepage Shopify Horizon — référence Notion

## Objet

Ce document décrit la homepage du thème Horizon publié sur Bonum Vitae, du bandeau d’annonce jusqu’au footer. Il sert à documenter le modèle dans Notion et à le reconstruire ensuite dans une autre boutique Shopify.

Il sépare :

- les composants natifs Horizon ;
- les réglages propres à la homepage ;
- le code personnalisé Bonum Vitae ;
- les données commerciales et éditoriales codées en dur ;
- les contenus dynamiques liés aux collections et produits ;
- les éléments à remplacer ou à vérifier avant une nouvelle publication.

Les fichiers de ce dossier sont des copies de référence en lecture seule. Ils ne doivent pas être copiés tels quels dans un autre thème sans lecture de ses schémas.

## Source contrôlée

| Champ | Valeur |
|---|---|
| Boutique | Bonum Vitae |
| Domaine | `bonumvitae.fr` |
| Thème | Horizon |
| Rôle | Thème principal publié (`MAIN`) |
| Date de lecture | 18 juillet 2026 |
| Mode | Lecture seule via les fichiers du thème et les menus Shopify |
| Modification Shopify | Aucune |

## Architecture générale

La homepage est constituée de trois niveaux :

1. groupe Header ;
2. modèle `templates/index.json` avec 10 sections ;
3. groupe Footer.

### Ordre complet de la page

| Ordre | Zone | Type Horizon | Fonction | Origine |
|---:|---|---|---|---|
| 1 | Bandeau d’annonce | `header-announcements` | Promotions et livraison | Horizon, textes Bonum Vitae |
| 2 | Header principal | `header` | Logo, navigation, recherche, compte, localisation, panier | Horizon |
| 3 | Hero | `hero` | Promesse principale et CTA | Horizon, contenu Bonum Vitae |
| 4 | Produits mis en avant | `product-list` | Collection des osmoseurs | Horizon |
| 5 | Avis clients | `bv-avis-clients` | Trois témoignages | Section personnalisée |
| 6 | Collections | `collection-list` | Navigation par besoin | Horizon |
| 7 | FAQ | `section` + `accordion` | Questions avant achat | Horizon, contenu Bonum Vitae |
| 8 | Réassurance | `section` + groupes/icônes | Choix, conseil et sécurité | Horizon, contenu Bonum Vitae |
| 9 | Contenu éditorial | `section` | Mise en situation carafes | Horizon |
| 10 | Comparatif | `custom-liquid` | Tableau carafe/robinet/osmoseur | Code personnalisé |
| 11 | Pourquoi Bonum Vitae | `section` | Positionnement de marque | Horizon |
| 12 | Newsletter | `section` + `email-signup` | Collecte d’e-mails et remise | Horizon |
| 13 | Footer principal | `footer` | Contact, menus, newsletter, paiements | Horizon |
| 14 | Footer utilitaire | `footer-utilities` | Copyright et politiques | Horizon |

## Identité visuelle observée

### Réglages globaux

| Élément | Valeur actuelle |
|---|---|
| Logo | `shopify://shop_images/logo-bonum-vitae-280x80.png` |
| Hauteur logo ordinateur | 36 px |
| Hauteur logo mobile | 28 px |
| Police titres | Fraunces 600 |
| Police texte | Inter 400 |
| Police sous-titres | Inter 500 |
| Police accent | Inter 700 |
| Largeur globale | `narrow` |
| Fond principal | `#FFFFFF` |
| Texte principal | `#1C2830` |
| Bleu de marque | `#0E3A5A` |
| Vert de marque | `#35B6AA` |
| Beige | `#F7F4EE` / `#EFEAE0` selon les zones |
| Vert très clair | `#EAF3F1` |

Ces valeurs sont adaptées à Bonum Vitae. Dans Notion, les conserver comme exemple de design system et les marquer « À personnaliser » pour une nouvelle boutique.

## Header

### Bandeau d’annonce

Deux messages tournent dans le bandeau :

1. `Offre d'été : -20% sur les osmoseurs`
2. `Livraison offerte, sans minimum d'achat`

Réglages :

- fond `#0E3A5A` ;
- largeur `page-width` ;
- vitesse 5 ;
- aucun lien associé ;
- typographie Inter sous-titre, 0,75 rem ;
- padding vertical 15 px.

Ces textes sont observés dans le thème mais leur présence ne prouve pas qu’une remise de 20 % ou une règle de livraison correspondante est active. Ils doivent être reliés à une promotion et à une politique vérifiées.

### Header principal

| Réglage | Valeur actuelle |
|---|---|
| Position du logo | Gauche |
| Position du menu | Gauche |
| Recherche | Affichée à droite |
| Sélecteur de pays | Affiché |
| Sélecteur de langue | Affiché |
| Compte client | Menu `customer-account-main-menu` |
| Header fixe | Toujours |
| Header transparent sur l’accueil | Non |
| Style des actions | Icônes |
| Menu principal | `main-menu` |
| Style du méga-menu | Produits mis en avant |

### Navigation principale

- Accueil → `/`
- Catalogue → `/collections/all`
  - Osmoseurs
  - Filtres de douche
  - Filtres robinet
  - Carafes filtrantes
  - Anti-calcaire sans sel
  - Purificateurs nomades
- Notre histoire → `/pages/notre-histoire`
- FAQ → `/pages/faq`
- Contact → `/pages/contact`
- Suivre ma commande → `/account`

Les liens de navigation sont des données Shopify, pas des blocs contenus dans `index.json`. Ils sont archivés dans `data/navigation-menus.json`.

## Section 1 — Hero

### Contenu actuel

| Élément | Valeur |
|---|---|
| Image | `bv-hero-osmoseur-desktop-2400x900.png` |
| Sur-titre | `Bonum Vitae — L’eau pure, chaque jour` |
| H1 | `Une eau meilleure, sans travaux ni plombier` |
| CTA | `Découvrir les osmoseurs` |
| Destination | Collection `osmoseurs` |
| Overlay | Actif, `#0B2B423D` |
| Hauteur | Moyenne |
| Padding | 72 px en haut et en bas |

### Mobile

Le réglage `custom_mobile_media` est désactivé. La même image panoramique est donc utilisée sur ordinateur et mobile. Pour une nouvelle boutique, prévoir un contrôle du recadrage et, si nécessaire, un média mobile dédié.

### Données à personnaliser

- promesse principale ;
- produit ou collection prioritaire ;
- image ordinateur et image mobile ;
- CTA et destination ;
- overlay ;
- preuve derrière les affirmations « sans travaux » ou « sans plombier ».

## Section 2 — Produits mis en avant

La section affiche la collection `osmoseurs`.

| Réglage | Valeur |
|---|---|
| Titre | `Nos Osmoseurs` |
| Bouton | `Tout voir` |
| Disposition | Carrousel |
| Produits maximum | 6 |
| Colonnes ordinateur | 4 |
| Colonnes mobile | 2 |
| Carrousel mobile | Désactivé |
| Fond | `#0E3A5A` |
| Carte produit | Image, titre, prix |
| Prix promotionnel en premier | Oui |
| Paiement échelonné sur la carte | Non |
| Informations fiscales sur la carte | Non |

La section dépend des produits réellement présents et publiés dans la collection. Pour une nouvelle boutique, remplacer la collection et contrôler disponibilité, images, prix, variantes et ordre de tri.

## Section 3 — Avis clients

### Nature du composant

`bv-avis-clients.liquid` est une section personnalisée originale. Elle affiche des cartes dans un défilement horizontal sans bibliothèque externe.

Réglages de la homepage :

- trois cartes par vue ;
- trois blocs d’avis ;
- fond des cartes blanc ;
- bordure `#E7E2D6` ;
- titres `#0E3A5A` ;
- texte `#3A4750` ;
- étoiles `#35B6AA`.

### Avis actuellement saisis

| Note | Titre | Auteur | Date relative | Vérifié coché |
|---:|---|---|---|---|
| 5 | Enfin une eau agréable à boire | Claire M. | Il y a 3 jours | Oui |
| 5 | Ma peau la remercie | Karim B. | Il y a 1 semaine | Oui |
| 4 | Bon conseil, pas de blabla | Bernard L. | Il y a 2 semaines | Oui |

### Limite de preuve

Ces avis sont codés dans le thème. Le réglage `verified: true` affiche un badge mais ne constitue pas une preuve d’achat vérifié. Les dates relatives deviennent également obsolètes.

Dans Notion, conserver le code et les textes comme modèle, mais classer chaque avis avec :

- source ;
- URL ou identifiant de commande ;
- produit concerné ;
- consentement d’utilisation ;
- date réelle ;
- statut de vérification ;
- autorisation de publication.

Sans ces preuves, les avis doivent rester des placeholders et ne pas être réutilisés comme témoignages réels.

## Section 4 — Collections

### Contenu configuré

Six collections sont sélectionnées :

1. `osmoseurs`
2. `filtres-de-douche`
3. `carafes-filtrantes`
4. `filtres-robinet`
5. `purificateurs-nomades`
6. `anti-calcaire-sans-sel`

La limite d’affichage est toutefois réglée sur **4 collections**. Les deux dernières peuvent donc ne pas apparaître sur la homepage malgré leur présence dans le réglage.

Autres réglages :

- sur-titre `Par besoin` ;
- titre `Explorez nos collections` ;
- grille de 3 colonnes sur ordinateur ;
- 2 colonnes sur mobile ;
- images carrées ;
- titre superposé à l’image ;
- overlay bleu transparent ;
- fond blanc.

Les images proviennent des images principales des collections Shopify. Le template ne contient pas de média individuel indépendant pour chaque carte.

## Section 5 — FAQ

### Structure

La FAQ utilise une section Horizon générique avec un bloc `accordion` et cinq lignes `_accordion-row`.

Titre :

`Vos questions, nos réponses franches`

Introduction :

`Les réponses aux questions que l’on nous pose le plus souvent avant une première commande. Il en manque une ? Écrivez-nous, nous répondons avant l’achat.`

### Questions présentes

1. Comment choisir entre carafe, filtre robinet et osmoseur ?
2. Quels sont les délais de livraison ?
3. Puis-je retourner un produit ?
4. Où trouver les cartouches de rechange ?
5. Les paiements sont-ils sécurisés ?

### Informations commerciales à vérifier

- expédition en 24–48 h ;
- livraison sous 6 à 10 jours ouvrés ;
- rétractation légale de 14 jours ;
- modalités et délai de remboursement ;
- disponibilité des consommables ;
- moyens de paiement réellement actifs ;
- formulation relative au stockage des données bancaires.

La FAQ est portable comme structure, mais les réponses doivent être réécrites selon les politiques, fournisseurs et produits de chaque boutique.

## Section 6 — Réassurance

La section contient trois colonnes horizontales sur ordinateur et empilées sur mobile.

| Icône | Titre | Texte |
|---|---|---|
| Camion | Des solutions à chaque usage | Douche, cuisine ou eau de boisson : équipez uniquement le point d’usage qui vous concerne. |
| Point d’interrogation | Le bon équipement, pas le plus cher | Carafe, filtre robinet ou osmoseur ? On vous oriente vers la solution adaptée à votre eau et à votre logement. |
| Cadenas | Achetez l’esprit tranquille | Retours 14 jours, paiement sécurisé et conseil disponible avant l’achat. |

Les icônes font 40 px et utilisent le bleu `#0E3A5A`.

À vérifier par boutique : politique de retour, disponibilité du conseil, sécurité de paiement et exactitude des catégories mises en avant.

## Section 7 — Contenu éditorial

### Contenu actuel

- sur-titre : `Au quotidien` ;
- titre : `L’eau du robinet, en mieux, à chaque repas` ;
- deux paragraphes sur les carafes et filtres ;
- CTA : `Voir les carafes filtrantes` ;
- image : `carafe-filtrante-36l-utilisation-famille.png` ;
- ratio paysage ;
- disposition 50/50 sur ordinateur et empilée sur mobile.

La section est une composition Horizon native de groupes, texte, bouton et image. Le média, la promesse et la destination doivent être remplacés selon le produit ou l’usage prioritaire de la nouvelle boutique.

## Section 8 — Comparatif personnalisé

### Nature du composant

Le comparatif est un bloc `custom-liquid`. Son contenu est archivé séparément dans :

`custom-liquid/comparatif-solutions.liquid`

### Structure

Le tableau compare :

- carafe filtrante ;
- filtre robinet ;
- osmoseur.

Critères :

- installation ;
- usage idéal ;
- budget ;
- entretien ;
- lien produit.

### Valeurs codées en dur

- textes du tableau ;
- couleurs ;
- largeur minimale de 640 px ;
- trois URL produit ;
- symboles de budget ;
- catégories comparées.

Le tableau est rendu défilable horizontalement sur petit écran. Pour une nouvelle boutique, reconstruire les lignes à partir de caractéristiques réellement vérifiées et remplacer les URL.

### URLs actuelles

- `/products/carafe-filtrante-3-6-l-stock-ue-filtration-cuisine`
- `/products/filtre-a-eau-pour-robinet-de-cuisine-modele-glq11`
- `/products/osmoseur-ro-600g-sans-reservoir-eau-filtree-a-la-demande`

## Section 9 — Pourquoi Bonum Vitae

Cette section présente le positionnement de la marque : choisir l’équipement proportionné au besoin et distinguer les caractéristiques documentées des performances non démontrées.

Le titre est actuellement codé en `<h1>Pourquoi Bonum Vitae ?</h1>`, alors que le hero possède déjà le H1 principal. Pour une reconstruction, utiliser un H2 afin de conserver une hiérarchie sémantique plus propre.

Valeurs à personnaliser :

- nom de marque ;
- mission ;
- principes de sélection ;
- slogan ;
- preuves de transparence ou d’expertise.

## Section 10 — Newsletter

### Contenu actuel

- titre : `10 % de remise sur votre première commande` ;
- texte conseil et offres ;
- bouton intégré : `Je m’inscris` ;
- note : `Un e-mail utile de temps en temps, rien de plus.` ;
- fond `#EAF3F1` ;
- formulaire à 50 % de largeur sur ordinateur.

La remise de 10 % doit être reliée à un mécanisme réel : code envoyé, automatisation Shopify Email, segmentation ou autre parcours mesurable. La documentation du thème ne confirme pas cette mécanique.

À contrôler :

- consentement marketing ;
- texte légal ;
- double opt-in si retenu ;
- e-mail de bienvenue ;
- code de remise et exclusions ;
- expiration ;
- mesure des inscriptions et conversions.

## Footer

### Footer principal

Le footer utilise un fond `#0E3A5A` et contient cinq blocs :

1. coordonnées et horaires ;
2. menu Politiques ;
3. menu Informations ;
4. inscription e-mail ;
5. icônes de paiement.

### Coordonnées actuelles

- horaires : lundi au vendredi, 9 h à 18 h ;
- téléphone : `+33 7 56 82 80 94` ;
- e-mail : `contact@bonumvitae.fr` ;
- adresse : `47 rue Vivienne, 75002 Paris`.

Ces données sont propres à Bonum Vitae et doivent toujours être remplacées ou vérifiées.

### Menu Politiques

- Suivre votre commande → `/account`
- Mentions légales
- Politique de confidentialité
- Politique de remboursement
- CGV
- Conditions d’utilisation

### Menu Informations

- Notre histoire
- FAQ
- Contactez-nous
- Livraison & Retour
- Suivre votre commande → `/account`

### Newsletter du footer

Le footer répète la promesse `-10 % sur votre première commande` avec le bouton `S'inscrire`. Cette seconde inscription doit partager la même mécanique et les mêmes règles que la newsletter de la homepage.

### Footer utilitaire

- copyright automatique ;
- mention « Powered by Shopify » masquée ;
- liste des politiques Shopify ;
- séparateur fin ;
- fond bleu.

## Composants natifs et personnalisés

| Composant | Origine | Portabilité |
|---|---|---|
| Header, annonces et footer | Horizon | Reconfigurer dans le thème cible |
| Hero | Horizon | Recréer avec le composant cible |
| Liste de produits | Horizon | Rebrancher à la collection cible |
| Avis clients | Personnalisé | Section Liquid adaptable après validation des avis |
| Liste de collections | Horizon | Rebrancher aux collections et images cibles |
| FAQ | Horizon | Structure portable, réponses à réécrire |
| Réassurance | Horizon | Ordre et UX portables, promesses à vérifier |
| Bloc éditorial | Horizon | Contenu et média à remplacer |
| Comparatif | Custom Liquid | Adaptable, données et liens à reconstruire |
| Newsletter | Horizon | Relier à une vraie automatisation |
| Menus | Données Shopify | Recréer dans Navigation |

## Fichiers de référence

### Structure et groupes

- `templates/index.json`
- `sections/header-group.json`
- `sections/footer-group.json`
- `layout/theme.liquid`
- `data/navigation-menus.json`

### Sections principales

- `sections/hero.liquid`
- `sections/product-list.liquid`
- `sections/collection-list.liquid`
- `sections/section.liquid`
- `sections/custom-liquid.liquid`
- `sections/bv-avis-clients.liquid`
- `sections/header.liquid`
- `sections/header-announcements.liquid`
- `sections/footer.liquid`
- `sections/footer-utilities.liquid`

### Blocs utiles

- `blocks/accordion.liquid`
- `blocks/_accordion-row.liquid`
- `blocks/email-signup.liquid`
- `blocks/icon.liquid`
- `blocks/image.liquid`
- `blocks/text.liquid`
- `blocks/button.liquid`
- `blocks/group.liquid`
- `blocks/_product-card.liquid`
- `blocks/_collection-card.liquid`

### Code personnalisé isolé

- `custom-liquid/comparatif-solutions.liquid`

## Données à organiser dans Notion

### Base « Sections homepage »

Pour chaque section :

- ordre ;
- nom fonctionnel ;
- type de section ;
- origine ;
- fichier source ;
- objectif commercial ;
- textes ;
- médias ;
- CTA et destination ;
- collection ou produit associé ;
- réglages ordinateur ;
- réglages mobile ;
- couleurs ;
- dépendances ;
- valeurs codées en dur ;
- valeurs dynamiques ;
- preuve requise ;
- statut de portabilité ;
- QA.

### Base « Navigation »

- menu ;
- niveau ;
- libellé ;
- type de lien ;
- URL ;
- ressource Shopify ;
- statut ;
- boutique cible ;
- nouvelle destination.

### Base « Promesses et preuves »

- texte exact ;
- emplacement ;
- catégorie : prix, livraison, retour, avis, paiement, produit ou expertise ;
- source ;
- statut : confirmé, conditionnel, manquant ou interdit ;
- date de vérification ;
- responsable ;
- version autorisée.

### Base « Médias homepage »

- section ;
- fichier actuel ;
- format ;
- ratio ;
- version ordinateur ;
- version mobile ;
- texte alternatif ;
- propriétaire et droits ;
- média de remplacement.

## Valeurs codées en dur à conserver comme modèle

- messages du bandeau d’annonce ;
- slogan et promesse du hero ;
- CTA ;
- collection `osmoseurs` ;
- trois témoignages et badges « vérifiés » ;
- six handles de collections ;
- cinq réponses de FAQ ;
- trois messages de réassurance ;
- texte et image du bloc éditorial ;
- contenu et URLs du comparatif ;
- texte « Pourquoi Bonum Vitae » ;
- remise newsletter de 10 % ;
- coordonnées ;
- handles et liens de menus ;
- palette et typographies.

Les importer dans Notion est autorisé comme référence, mais chacun doit posséder un champ « À personnaliser » ou « Preuve requise ».

## Risques et points à corriger lors d’une reconstruction

- Offre saisonnière de 20 % potentiellement périmée ou non reliée à une remise active.
- Promesse de livraison gratuite non reliée automatiquement aux profils d’expédition.
- Même image hero sur ordinateur et mobile, avec risque de recadrage.
- Avis codés en dur sans preuve intégrée et dates relatives obsolètes.
- Six collections configurées mais seulement quatre autorisées à l’affichage.
- Comparatif lié à trois URLs produit précises.
- Deux H1 sur la homepage : hero et « Pourquoi Bonum Vitae ».
- Remise newsletter de 10 % répétée sans mécanique confirmée dans cet audit.
- Liens « Suivre ma commande » redirigés vers `/account`, pas vers un outil de suivi dédié.
- Sélecteurs pays/langue visibles même si l’offre réelle est uniquement française.
- Coordonnées, politiques et moyens de paiement à revalider par boutique.
- Copie directe du JSON Horizon incompatible avec un thème dont les schémas diffèrent.

## Checklist de reconstruction

1. Identifier le thème cible et lire ses schémas.
2. Définir le design system : logo, couleurs, typographies et largeur.
3. Recréer les menus et vérifier chaque destination.
4. Configurer le bandeau d’annonce avec des offres actives et datées.
5. Construire un hero avec H1 unique, CTA et médias ordinateur/mobile.
6. Brancher la collection principale et ses cartes produits.
7. Importer uniquement des avis dont la source est documentée.
8. Sélectionner les collections et harmoniser la limite d’affichage.
9. Adapter la FAQ aux politiques et délais réels.
10. Adapter la réassurance aux engagements réels.
11. Ajouter un bloc éditorial avec média et alt text.
12. Recréer le comparatif à partir de données produit prouvées.
13. Présenter la marque avec un H2, pas un second H1.
14. Relier la newsletter à une automatisation et une remise réelles.
15. Construire le footer avec coordonnées et pages légales vérifiées.
16. Tester mobile, clavier, lecteurs d’écran, liens, formulaires et performances.

## Checklist QA

- [ ] Un seul H1 est présent.
- [ ] Le hero reste lisible sur mobile.
- [ ] Les images ont un texte alternatif pertinent.
- [ ] Tous les CTA mènent à une destination publiée.
- [ ] Les produits mis en avant sont disponibles.
- [ ] Les collections affichées correspondent à la limite configurée.
- [ ] Les avis possèdent une source et une autorisation.
- [ ] Les dates d’avis ne sont pas trompeuses.
- [ ] Les réponses FAQ correspondent aux politiques actuelles.
- [ ] Les promesses de prix et de livraison sont actives.
- [ ] Les URLs du comparatif existent.
- [ ] Le tableau est utilisable sur mobile et au clavier.
- [ ] La remise newsletter est effectivement envoyée.
- [ ] Le consentement marketing est enregistré.
- [ ] Les menus ordinateur et mobile fonctionnent.
- [ ] Recherche, compte, localisation et panier fonctionnent.
- [ ] Les coordonnées et horaires sont corrects.
- [ ] Les pages légales sont accessibles.
- [ ] Les moyens de paiement affichés sont réellement actifs.
- [ ] Le footer ne duplique pas inutilement les informations.
- [ ] La page ne présente pas de débordement horizontal.
- [ ] Les performances images et scripts sont acceptables.

## Limite de l’audit

Cette référence décrit les fichiers et données du thème publié observés le 18 juillet 2026. Elle ne prouve pas que les remises, automatisations e-mail, règles de livraison, avis, moyens de paiement ou politiques sont tous opérationnels pour chaque client. Ces éléments doivent être contrôlés dans la boutique cible avant publication.

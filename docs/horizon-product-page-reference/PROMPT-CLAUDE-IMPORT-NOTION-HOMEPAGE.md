# Prompt à envoyer à Claude — import Notion de la homepage

```text
Je veux que tu complètes mon espace Notion existant consacré au modèle Shopify Horizon en y ajoutant toute la structure de la homepage Bonum Vitae.

OBJECTIF

Créer une documentation réutilisable pour construire les homepages des prochaines boutiques Shopify à partir du modèle Bonum Vitae.

Tu dois importer et organiser :

- le header et le bandeau d’annonce ;
- la navigation principale et les menus ;
- toutes les sections de la homepage dans leur ordre exact ;
- le hero ;
- la sélection de produits ;
- les collections ;
- les avis clients ;
- la FAQ ;
- les blocs de réassurance ;
- le contenu éditorial ;
- le comparatif personnalisé ;
- la présentation de la marque ;
- la newsletter ;
- le footer ;
- les codes Liquid ;
- les valeurs codées en dur ;
- les dépendances ;
- les éléments à personnaliser ;
- les risques de migration ;
- les checklists de construction et de QA.

Tu peux conserver et importer les éléments codés en dur. Nous les remplacerons lors de la création de chaque nouvelle boutique. Il faut simplement les marquer clairement « À personnaliser » ou « Preuve requise ».

SOURCE PRINCIPALE

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/HORIZON-HOMEPAGE-NOTION.md

DOSSIER COMPLET

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/

FICHIERS DE STRUCTURE

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/templates/index.json

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/header-group.json

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/footer-group.json

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/layout/theme.liquid

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/data/navigation-menus.json

SECTIONS PRINCIPALES

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/hero.liquid

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/product-list.liquid

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/collection-list.liquid

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/section.liquid

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/custom-liquid.liquid

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/bv-avis-clients.liquid

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/header.liquid

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/header-announcements.liquid

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/footer.liquid

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/sections/footer-utilities.liquid

CODE PERSONNALISÉ ISOLÉ

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/custom-liquid/comparatif-solutions.liquid

MISSION DANS NOTION

1. Lis entièrement le document principal avant de créer ou modifier la structure Notion.
2. Lis ensuite les fichiers sources nécessaires.
3. Ne modifie pas Shopify et ne publie aucun changement.
4. Ajoute une sous-page intitulée « Modèle homepage Shopify Horizon » à la source Notion existante.
5. Relie cette page aux modèles « Page produit » et « Panier » déjà présents.
6. Crée au minimum les sous-pages ou vues suivantes :
   - Vue d’ensemble et ordre de la homepage
   - Design system
   - Header et annonces
   - Navigation
   - Hero
   - Produits mis en avant
   - Collections
   - Avis clients
   - FAQ
   - Réassurance
   - Contenu éditorial
   - Comparatif
   - Présentation de la marque
   - Newsletter
   - Footer
   - Bibliothèque Liquid
   - Valeurs codées en dur
   - Promesses et preuves
   - Médias
   - Checklist de construction
   - Checklist QA
   - Historique des versions

ORDRE EXACT À ENREGISTRER

1. Bandeau d’annonce
2. Header principal
3. Hero
4. Produits mis en avant — collection osmoseurs
5. Avis clients
6. Collections
7. FAQ
8. Réassurance
9. Contenu éditorial sur les carafes
10. Comparatif carafe/filtre robinet/osmoseur
11. Pourquoi Bonum Vitae
12. Newsletter
13. Footer principal
14. Footer utilitaire

POUR CHAQUE SECTION

Crée une fiche contenant :

- numéro d’ordre ;
- nom fonctionnel ;
- type Horizon ;
- origine : natif, app, Custom Liquid ou section personnalisée ;
- objectif commercial ;
- chemin du fichier source ;
- textes actuels ;
- médias actuels ;
- CTA et destination ;
- collection ou produit associé ;
- structure des blocs ;
- réglages ordinateur ;
- réglages mobile ;
- couleurs et typographies ;
- valeurs codées en dur ;
- valeurs dynamiques ;
- dépendances ;
- preuve requise ;
- éléments à personnaliser ;
- statut de portabilité ;
- contrôles QA.

HEADER ET NAVIGATION

Documente :

- les deux messages du bandeau ;
- le logo ;
- le header fixe ;
- la recherche ;
- le compte client ;
- les sélecteurs de pays et de langue ;
- le menu principal et ses sous-menus ;
- les destinations de chaque lien ;
- les menus du footer.

Conserve les annonces actuelles comme modèle :

- « Offre d'été : -20% sur les osmoseurs »
- « Livraison offerte, sans minimum d'achat »

Marque-les « Preuve requise » car le thème ne confirme pas que la remise ou la règle de livraison est active.

HERO

Enregistre :

- image `bv-hero-osmoseur-desktop-2400x900.png` ;
- sur-titre « Bonum Vitae — L’eau pure, chaque jour » ;
- H1 « Une eau meilleure, sans travaux ni plombier » ;
- CTA « Découvrir les osmoseurs » ;
- destination collection osmoseurs ;
- overlay ;
- absence d’image mobile dédiée.

Ajoute un risque de recadrage mobile et un champ pour le futur média mobile.

PRODUITS ET COLLECTIONS

Documente la sélection d’osmoseurs :

- collection `osmoseurs` ;
- six produits maximum ;
- quatre colonnes ordinateur ;
- deux colonnes mobile ;
- titre « Nos Osmoseurs » ;
- bouton « Tout voir ».

Documente aussi les six collections sélectionnées :

- osmoseurs ;
- filtres-de-douche ;
- carafes-filtrantes ;
- filtres-robinet ;
- purificateurs-nomades ;
- anti-calcaire-sans-sel.

Signale que la limite actuelle est de quatre collections. Six sont sélectionnées, mais seulement quatre peuvent être affichées.

AVIS CLIENTS

La section `bv-avis-clients.liquid` est personnalisée.

Importe sa structure et ses trois avis actuels, mais classe-les comme contenu modèle tant qu’aucune preuve externe n’est associée.

Le champ `verified: true` affiche seulement un badge dans le thème. Il ne prouve pas un achat vérifié.

Pour chaque avis, ajoute :

- texte ;
- note ;
- auteur ;
- date affichée ;
- produit ;
- source ;
- identifiant de commande ;
- consentement ;
- date réelle ;
- statut de vérification ;
- autorisation de publication.

Marque les dates relatives « Il y a 3 jours », « Il y a 1 semaine » et « Il y a 2 semaines » comme non durables.

FAQ

Importe les cinq questions et leurs réponses :

1. Comment choisir entre carafe, filtre robinet et osmoseur ?
2. Quels sont les délais de livraison ?
3. Puis-je retourner un produit ?
4. Où trouver les cartouches de rechange ?
5. Les paiements sont-ils sécurisés ?

Marque comme informations à vérifier :

- expédition en 24–48 h ;
- livraison en 6 à 10 jours ouvrés ;
- retours sous 14 jours ;
- modalités de remboursement ;
- consommables ;
- moyens de paiement ;
- stockage des données bancaires.

RÉASSURANCE

Importe les trois blocs avec leurs icônes, titres et textes :

- Des solutions à chaque usage
- Le bon équipement, pas le plus cher
- Achetez l’esprit tranquille

Conserve les textes actuels comme modèle et ajoute un champ « Preuve/politique associée ».

CONTENU ÉDITORIAL

Documente le bloc « Au quotidien » :

- titre ;
- paragraphes ;
- CTA vers les carafes filtrantes ;
- image `carafe-filtrante-36l-utilisation-famille.png` ;
- disposition 50/50 ordinateur et empilée sur mobile.

COMPARATIF

Importe le code complet du fichier :

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/custom-liquid/comparatif-solutions.liquid

Documente :

- les trois catégories comparées ;
- les critères ;
- les couleurs ;
- les symboles de budget ;
- les trois URLs produit ;
- la largeur minimale de 640 px ;
- le scroll horizontal mobile.

Marque les textes, URLs, produits, prix relatifs et caractéristiques comme « À personnaliser et à prouver ».

PRÉSENTATION DE LA MARQUE

Importe le texte « Pourquoi Bonum Vitae » comme modèle de positionnement.

Signale que ce titre utilise actuellement un deuxième H1. Pour la prochaine boutique, il devra devenir un H2 afin de garder un seul H1 principal sur la page.

NEWSLETTER

Documente les deux formulaires : celui de la homepage et celui du footer.

Conserve la promesse de remise de 10 %, mais marque-la « Mécanique à confirmer ».

Ajoute les champs :

- code de remise ;
- exclusions ;
- date d’expiration ;
- automatisation d’accueil ;
- consentement ;
- double opt-in ;
- segmentation ;
- taux d’inscription ;
- conversion.

FOOTER

Importe :

- horaires ;
- téléphone ;
- e-mail ;
- adresse ;
- menus Politiques et Informations ;
- formulaire newsletter ;
- icônes de paiement ;
- copyright ;
- liste des politiques.

Marque les coordonnées, horaires, pages légales et moyens de paiement comme « À vérifier ou remplacer ».

BIBLIOTHÈQUE LIQUID

Pour chaque fichier Liquid, crée une fiche avec :

- nom ;
- rôle ;
- emplacement ;
- code complet ou lien source ;
- schéma ;
- blocs autorisés ;
- dépendances ;
- réglages ;
- valeurs codées en dur ;
- compatibilité ;
- risques ;
- statut de validation.

Ne présente pas le JSON Horizon ou ses blocs comme compatibles avec tous les thèmes. Pour une nouvelle boutique, il faut lire le schéma du thème cible et reconstruire avec ses composants natifs.

BASE « VALEURS CODÉES EN DUR »

Crée les propriétés :

- Élément
- Section
- Type
- Valeur actuelle
- Fichier source
- À personnaliser
- Preuve requise
- Nouvelle valeur
- Statut
- Date de validation
- Responsable

Ajoute au minimum :

- messages du bandeau ;
- slogan et H1 ;
- CTA ;
- collections ;
- avis ;
- réponses FAQ ;
- messages de réassurance ;
- image et texte éditorial ;
- comparatif et URLs ;
- texte de marque ;
- remise newsletter ;
- coordonnées ;
- menus ;
- couleurs et typographies.

RÈGLES IMPORTANTES

- Ne modifie pas Shopify.
- Ne publie rien.
- Ne supprime pas les valeurs codées en dur : conserve-les comme modèle.
- N’invente aucune donnée manquante.
- Sépare toujours : Observé, Codé en dur, Manquant, Hypothèse et Décision à prendre.
- Ne considère aucun avis comme réel sans preuve.
- Ne considère aucune promotion comme active uniquement parce que son texte est dans le thème.
- Ne réutilise pas les coordonnées, politiques, URLs, handles ou médias comme valeurs universelles.
- Ne copie pas `templates/index.json` dans un autre thème sans lire ses schémas.

SORTIE ATTENDUE

À la fin, donne-moi :

1. le lien de la page Notion créée ou mise à jour ;
2. la structure des pages et bases ajoutées ;
3. le nombre de sections homepage importées ;
4. le nombre de composants Liquid enregistrés ;
5. la liste des menus importés ;
6. la liste des valeurs codées en dur ;
7. la liste des promesses nécessitant une preuve ;
8. la liste des données manquantes ;
9. les risques de migration ;
10. la checklist courte pour reconstruire la homepage d’une nouvelle boutique.

Ne te contente pas de résumer : transforme les fichiers en une base Notion structurée, reliée et directement exploitable.
```

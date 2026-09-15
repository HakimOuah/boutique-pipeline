# Page collection Bercelou (thème FullStack, copie 206567702873)

Modèle `templates/collection.json` : bannière → grille du thème → guide d'achat.

La bannière et le guide lisent la description de la collection (`snippets/bercelou-collection.liquid`) :

- intro : tout ce qui précède le premier `<h2>` (sur mobile, 4 lignes puis « Lire la suite ») ;
- guide d'achat : premier `<h2>` et son texte, avec les liens vers les guides ;
- FAQ : second `<h2>`, questions en `<strong>`, affichées en accordéons ;
- image : image de la collection (Admin > Collections) ;
- « Explorer aussi » : toutes les collections non vides, sauf la page d'accueil et « Notre sélection ».

Mots-clés (15/09/2026) : les intertitres portent le mot-clé principal (« Bien choisir son fauteuil à bascule », « Vos questions sur les … »), et le mot-clé a été glissé dans l'intro des collections où il manquait (bois et rotin, extérieur, relax jardin, repose-pieds, enfant, accessoires). Textes en ligne : `shopify/collections-descriptions-live-2026-09-15.json` ; les fichiers `content/collections/*.md` sont antérieurs à ces retouches.

Grille : étoiles de démonstration retirées des cartes, pastilles de couleur affichées, boutons « Ajouter au panier » alignés.

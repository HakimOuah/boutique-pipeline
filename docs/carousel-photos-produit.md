# Carousel Photos Produit — les 7 images dans l'ordre exact

> Source : `carousel_photos_produit.pdf` (Arthur FMV — Ecom Inner Circle, module Shopify), original dans `~/Downloads/carousel_photos_produit.pdf`. Pages rendues en PNG dans `docs/carousel-photos-produit/page-{1,2,3}.png`. Distillé le 25/07/2026 pour le ticket « 08 · Images produit » du campement type.

## Règle n°1 avant tout : COHÉRENCE VISUELLE

Toutes les images respectent la **même direction artistique** du début à la fin : même décor, même lumière, même ambiance, même palette. On ne passe PAS d'un fond blanc à un lifestyle, d'un studio neutre à une cuisine colorée. Un carousel incohérent détruit la crédibilité de la marque, même si le produit est excellent. **Définir l'univers visuel AVANT de shooter/générer** et s'y tenir sur toutes les images.

Exemples de directions cohérentes :
- **Premium / luxe** : fond marbre, bois sombre, linge beige ; lumière chaude et douce ; aucun élément parasite.
- **Lifestyle chaud** : intérieurs cosy, bougies, plantes, textures naturelles ; le client se projette.
- **Minimaliste** : fond uni blanc/gris clair, produit seul bien cadré, ombres douces.
- **Outdoor / nature** : bois brut, pierres, forêt, lumière naturelle (produits sport/jardin).

## Les 7 images, dans l'ordre — émotion d'abord (1-4), rationnel ensuite (5-7)

1. **Produit seul — le wow visuel.** Produit parfaitement cadré, lumière soignée, fond conforme à la DA, AUCUN texte. C'est la vitrine : soigner cette image plus que toutes les autres. ✗ Fond blanc générique, mauvais cadrage, ombres dures.
2. **Produit en situation — le client se projette.** Décor aspirationnel dans la même palette que l'image 1, produit aussi soigné que le décor. Test : « est-ce que ce décor donne envie de vivre là ? » ✗ Décor kitsch/chargé, palette différente, produit trop petit.
3. **Feature principale — argument n°1.** Produit + 1 titre et 1 sous-titre max en surimpression, typographie propre aux couleurs de la marque. La feature qui différencie de la concurrence (« si tu ne pouvais en montrer qu'une »). ✗ Trop de texte, police illisible, contraste insuffisant.
4. **Produit en action — comment ça marche.** Produit utilisé/manipulé (mains, personne, mouvement), toujours dans la même DA. Répond au « mais ça marche comment ? ». ✗ Photo floue, mauvais éclairage du détail important, contexte incongru.
5. **Détails et dimensions — le rationnel.** Zoom matières/finitions/fabrication, dimensions possibles en overlay graphique. Le client valide rationnellement après avoir été séduit. ✗ Détails flous, dimensions illisibles, police trop petite.
6. **Preuve sociale — avis et garantie.** Produit sur fond sobre avec en overlay : note /5, nombre d'avis, badge garantie — chiffres GRANDS et immédiatement lisibles (ex. « 4,8/5 sur 847 avis + garantie 30 jours »). C'est l'image qui fait basculer l'hésitant. ✗ Chiffres trop petits, mauvais contraste, éléments qui se concurrencent.
7. **Témoignage client — le closing.** Citation réelle d'un client satisfait sur fond épuré : nom, ville, photo si possible, mise en page dans la DA. Dernière image avant le bouton d'achat. ✗ Citation inventée ou trop marketing, anonymat complet, texte illisible.

**À retenir :** images 1-4 = faire rêver et désirer ; images 5-7 = convaincre et rassurer. Une seule DA du début à la fin.

## Adaptation pipeline (nos boutiques dropship)

- Génération IA (Higgsfield) : appliquer la boucle anti-faux-logos du ticket 08 (vérification visuelle de chaque image + inpainting/régénération).
- Image 6 : les chiffres avis/garantie doivent rester cohérents avec les badges du site (placeholders tranchés par Hakim).
- Image 7 : citation issue des avis persona (ticket 02) tant qu'il n'y a pas de vrais avis, puis remplacer par un avis réel importé (ticket 12).
- Accessoires/upsells : version allégée acceptable (au minimum images 1, 3, 5), le 7-images complet est pour les produits héros.

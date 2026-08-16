# Brief visuels Codex — retirer le badge « GARANTIE 2 ANS » (16/08/2026)

**Urgent, bloquant pour Google Merchant Center.** Les images principales des deux produits phares de
Tuftéo portent un **badge « GARANTIE 2 ANS ★ » incrusté** en haut à droite. Le texte incrusté sur une
image produit est un **motif de refus explicite** de la checklist GMC, et ces deux fiches sont actives
et déjà présentes dans le flux Shopping.

**À faire avant de lancer cette génération** : vérifier si une autre image de la galerie du même
produit est déjà propre. Si oui, la promouvoir en image principale suffit et ce brief devient inutile.

## Les deux images à refaire

| Produit | Handle | Fichier source actuel |
|---|---|---|
| Kit Tufting Complet | `kit-tufting-complet` | `electric-2-in-1-tufting-gun-set-with-fabric-carpet-trimmer-carpettapis-knitting-tufting-pistol-weaving-flocking-rug-machine-01.png` (2048 × 2048) |
| Tufting gun 2-en-1 Cut & Loop | `tufting-gun-2-en-1` | `gun-2in1-01.png` (2048 × 2048) |

Préfixe CDN : `https://cdn.shopify.com/s/files/1/0953/2774/8481/files/`

## Ce qu'il faut produire

**La même image, sans le badge.** On ne change ni la composition, ni le cadrage, ni la lumière, ni le
fond — uniquement le retrait de la pastille « GARANTIE 2 ANS ★ » et la reconstitution propre du fond
crème à son emplacement.

Le visuel du kit est un **flat-lay du contenu réel** (gun bleu, tondeuse, toile, pelotes, peignes,
lames, visserie, câble). C'est une présentation légitime du contenu d'un kit, pas un collage
promotionnel : **elle est conservée telle quelle**, badge en moins.

## Spécifications

- **2048 × 2048, carré**, PNG ou JPEG, moins de 2 Mo — mêmes dimensions que les originaux.
- Fond crème identique (`#F7F1E8` environ), raccord invisible à l'emplacement du badge.
- **Aucun texte, aucun logo, aucune pastille, aucun filigrane** nulle part dans l'image.
- Ne pas retoucher les emballages des produits eux-mêmes : le texte imprimé sur un sachet ou sur
  l'outil fait partie du produit et reste.

## Nommage et livraison

- `kit-tufting-complet-01-sans-badge.png`
- `tufting-gun-2-en-1-01-sans-badge.png`

Dans `boutique-pipeline/boutique-tufting/images/visuels-2026-08-16-badges/`, avec un `mapping.json`
sur le modèle des livraisons précédentes (`fichier`, `handle_produit`, `variante`, `role`).

## Contrôle avant de rendre

- [ ] Aucun texte ni pastille visible, y compris en zoomant sur les quatre coins
- [ ] Fond raccordé sans trace ni halo à l'emplacement de l'ancien badge
- [ ] Composition, cadrage et couleurs identiques à l'original
- [ ] 2048 × 2048, moins de 2 Mo

Ne rien pousser sur Shopify : l'affectation sera faite ensuite, avec vérification en prévisualisation.

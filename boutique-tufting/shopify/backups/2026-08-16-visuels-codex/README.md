# Sauvegarde avant affectation des visuels Codex — 16/08/2026

Contexte : chantier "Affectation des visuels Codex" (voir EXECUTION-2026-08-16.md).
26 images créées via `productCreateMedia` (staged upload) sur 20 fiches produit.

## État "avant" (relevé par API juste avant écriture)

### 17 fiches fil-acrylique-tufting-<couleur>
Toutes avaient pour featuredImage le swatch fournisseur brut (fichiers `S....webp`, ~230-530 px de
côté), listé comme SEULE image de la fiche. Après le chantier : le swatch est resté en place comme
image secondaire, la nouvelle image cône (1600×1600, 1280×1280 servi) est devenue featuredImage
(position 0).

Exemple (Noir, gid://shopify/Product/15500842566017) :
- avant : `Sa67e36040f074260acb63d3a80561cf3X.webp` (seule image)
- après : `fil-acrylique-tufting-noir-01.png` (position 0) + le swatch webp (position 1)

### brosse-de-finition (gid://shopify/Product/15466412835201)
Avant : 6 images génériques (montrant uniquement le bleu), variantes Rouge et Vert sans image propre
(`variant.image: null`).
Après : les 6 images génériques restent en place + 2 images ajoutées (Rouge, Vert), chacune liée à sa
variante via `productVariantAppendMedia`. Bleu reste sans image de variante dédiée (non demandé par le
brief — l'image générique du produit montre déjà le bleu).

### enfile-laine-tufting-gun (gid://shopify/Product/15466411360641)
Avant : 6 images génériques montrant un assortiment 5 couleurs mélangées, aucune des 3 variantes
(Jaune/Rouge/Noir lot de 5) n'avait d'image propre.
Après : 3 images ajoutées (un lot de 5 unités mono-couleur par image), chacune liée à sa variante.

### miroir-acrylique-tufting (gid://shopify/Product/15466414408065)
Avant : 6 images génériques (mises en scène multi-couleurs), aucune des 32 variantes (4 couleurs × 8
tailles) n'avait d'image propre (`variant.image: null` sur l'échantillon vérifié).
Après : 4 images ajoutées (une par couleur), chacune liée aux 8 variantes de taille de sa couleur
(32 liaisons au total via un seul appel `productVariantAppendMedia`).

## Fichiers sources

Les 26 fichiers uploadés viennent de
`boutique-pipeline/boutique-tufting/images/visuels-2026-08-16/` (voir `mapping.json` dans ce dossier
pour la correspondance fichier → cible). Le 27e fichier `planche-controle-17-cones.png` n'a jamais été
uploadé (outil de relecture interne, collage — exclu explicitement par le brief).

## Réversibilité

Aucune image existante n'a été supprimée : le swatch de chaque fil reste en médiathèque (position 1),
et les images génériques des 3 fiches variantes restent en place. Pour revenir en arrière, il suffit de
repositionner le swatch en position 0 (fils) ou de détacher les médias de variante ajoutés
(`productVariantDetachMedia` si besoin, non utilisé dans ce chantier).

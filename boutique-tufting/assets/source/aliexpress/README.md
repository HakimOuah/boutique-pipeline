# Images source fournisseur — Tuftéo

## Origine
Photos fournisseur AliExpress importées via DSers, relevées du CDN Shopify (boutique Tuftéo) le 21/07/2026 via l'API Admin GraphQL (lecture seule). 23 produits, 195 images.

## Structure
- `manifest.json` — tableau `[{handle, title, images: [urls CDN]}]`, ordre de la galerie Shopify.
- `{handle}/img-01.webp`, `img-02.webp`, … — une image par position de galerie ; **img-01 est l'image principale** du produit.

Note technique : certains fichiers portent l'extension `.webp` (nom d'origine sur le CDN) mais contiennent des données JPEG. Le contenu est valide ; vérifier le vrai format avec `file` si un outil est strict sur le type MIME.

## Usage
Références de fidélité produit pour la génération d'images Tuftéo — voir `prompt-codex-images-2026-07-21.md`. Ces photos servent uniquement à garantir que les visuels générés respectent le produit réel (forme, couleurs, accessoires inclus, contenu du kit).

## Avertissement
Photos fournisseur = à remplacer. Ne pas publier telles quelles sur la boutique ni dans les publicités : qualité et branding non conformes, droits incertains. Elles ne doivent jamais quitter ce dossier de travail en l'état.

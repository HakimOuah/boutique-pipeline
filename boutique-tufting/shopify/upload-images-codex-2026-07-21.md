# Upload images Codex → Shopify Tuftéo — 21 juillet 2026

Mission : upload des 126 images produit générées par Codex (`images/{handle}/{handle}-01..06.png`, 2048×2048) vers la boutique Tuftéo, placées en positions 1-6 de chaque produit, sans suppression des images fournisseur.

Méthode par produit : `stagedUploadsCreate` (6 cibles signées GCS) → upload curl multipart (6×201) → `productCreateMedia` (alt = "{titre} — image {n}") → `productReorderMedia` (positions 0-5) → re-query de vérification.

## Résultat : 21/21 produits complétés, 0 erreur

| # | Handle | GID produit | 6 médias créés | Réordonnancement | Vérif. (médias avant → après, 6 nouvelles en tête, statut READY) |
|---|--------|-------------|----------------|------------------|------------------------------------------------------------------|
| 1 | 1-5mx10m-4m-primary-tufting-cloth-…-solid-pattern | gid://shopify/Product/15466411590017 | Oui | OK | 6 → 12, OK |
| 2 | 1-8m-1m-tufting-cloth-…-backing-fabric | gid://shopify/Product/15466411196801 | Oui | OK | 6 → 12, OK |
| 3 | 10m-super-sticky-cloth-duct-tape-…-repair-bundles | gid://shopify/Product/15466413785473 | Oui | OK | 6 → 12, OK |
| 4 | 10meters-4cm-width-tufting-cloth-…-crafts-material | gid://shopify/Product/15466413752705 | Oui | OK | 6 → 12, OK |
| 5 | 1mx5m-final-backing-cloth-…-handmade-cloth | gid://shopify/Product/15466411131265 | Oui | OK | 6 → 12, OK |
| 6 | 1pc-manual-household-yarn-winding-machine-…-ball-winder | gid://shopify/Product/15466411295105 | Oui | OK | 7 → 13, OK |
| 7 | 2-1mx3m-monk-cloth-…-needlework | gid://shopify/Product/15466411557249 | Oui | OK | 7 → 13, OK |
| 8 | 200w-electric-scissors-…-carpet-weaving | gid://shopify/Product/15466411426177 | Oui | OK | 7 → 13, OK |
| 9 | 3mm-gold-silver-red-acrylic-mirror-…-plexiglass-mirrors | gid://shopify/Product/15466414408065 | Oui | OK | 10 → 16, OK |
| 10 | 5pcs-new-tufting-gun-needle-threader-…-sewing-tools | gid://shopify/Product/15466411360641 | Oui | OK | 9 → 15, OK |
| 11 | 8pcs-tufting-tack-strip-…-woven-carpet-50m | gid://shopify/Product/15466411262337 | Oui | OK | 7 → 13, OK |
| 12 | 91-colour-wholesale-400g-yarn-cone-…-tufting-gun | gid://shopify/Product/15466411229569 | Oui | OK | 93 → 99, OK |
| 13 | afourt-12pcs-rug-tufting-trimmer-replacement-blades-… | gid://shopify/Product/15466411491713 | Oui | OK | 6 → 12, OK |
| 14 | cleaning-brush-plastic-handle-…-car-keyboard | gid://shopify/Product/15466412835201 | Oui | OK | 9 → 15, OK |
| 15 | duckbill-blade-scissors-pelican-scissors-…-sewing-scissors | gid://shopify/Product/15466411327873 | Oui | OK | 6 → 12, OK |
| 16 | electric-2-in-1-tufting-gun-set-…-rug-machine | gid://shopify/Product/15466411688321 | Oui | OK | 13 → 19, OK |
| 17 | multifunction-electric-tufting-electric-scissor-…-modeling-scissors | gid://shopify/Product/15466411458945 | Oui | OK | 8 → 14, OK |
| 18 | shearing-guide-for-carpet-trimmer-…-uniform-for-home | gid://shopify/Product/15466411655553 | Oui | OK | 6 → 12, OK |
| 19 | spring-balancer-spring-balancer-3-to-5kg-…-maintenance-kits | gid://shopify/Product/15466412933505 | Oui | OK | 6 → 12, OK |
| 20 | tufting-carpet-trimmer-with-shearing-guide-…-carving-tool | gid://shopify/Product/15466411524481 | Oui | OK | 8 → 14, OK |
| 21 | wholesale-handheld-glue-spreader-…-gluing-tool | gid://shopify/Product/15466412900737 | Oui | OK | 7 → 13, OK |

## Notes

- 126/126 uploads staged GCS en HTTP 201, 126/126 médias créés en statut UPLOADED puis vérifiés READY.
- Vérification finale (re-query groupée) : sur chacun des 21 produits, les positions 1-6 portent les alt "{titre} — image 1..6" et le mediaCount = ancien compte + 6 → aucune image fournisseur supprimée.
- Alt texts en français, format "{titre du produit} — image {n}".
- Aucun changement de prix, statut, titre ou description.
- Handles introuvables : aucun (21/21 trouvés du premier coup via productByHandle).
- Produits volontairement non touchés (pas d'images générées) : `original-tufting-accessories-…` (pièces détachées) et `pistolet-tufting-gun-set-2in1-…` (gun 2-en-1).

## Détachement des images de variantes (22/07)

Objectif : que l'image héros (position 1, générée) s'affiche au chargement des fiches produit, au lieu de la photo fournisseur liée à la variante sélectionnée. Opération : `productVariantDetachMedia` uniquement — aucun média supprimé, aucun changement de prix/statut/texte/positions.

Exclusions (non touchés, liaisons variante→média conservées) :
- Fil acrylique en cône pour tufting (gid://shopify/Product/15466411229569) — images de variante = choix de couleur (87 coloris)
- Pièces détachées pour tufting gun (gid://shopify/Product/15466415292801)
- Tufting gun 2-en-1 Cut & Loop (gid://shopify/Product/15466410213761) — aucune variante n'avait de média lié de toute façon

| Produit | GID | Variantes détachées | Vérif (0 média lié / mediaCount inchangé) |
|---|---|---|---|
| Tissu de finition | gid://shopify/Product/15466411131265 | 4 | OK (12) |
| Tissu de finition antidérapant | gid://shopify/Product/15466411196801 | 5 | OK (12) |
| Grippers — bandes de fixation (lot de 8) | gid://shopify/Product/15466411262337 | 2 | OK (13) |
| Bobineuse à laine | gid://shopify/Product/15466411295105 | 1 | OK (13) |
| Ciseaux pélican pour tufting | gid://shopify/Product/15466411327873 | 1 | OK (12) |
| Enfile-laine pour tufting gun (lot de 5) | gid://shopify/Product/15466411360641 | 3 | OK (15) |
| Tondeuse professionnelle pour tapis | gid://shopify/Product/15466411426177 | 2 | OK (13) |
| Ciseaux électriques de sculpture | gid://shopify/Product/15466411458945 | 2 | OK (14) |
| Lames de remplacement pour tondeuse (lot de 12) | gid://shopify/Product/15466411491713 | 1 | OK (12) |
| Kit tondeuse + guide de tonte | gid://shopify/Product/15466411524481 | 12 | OK (14) |
| Toile primaire de tufting (lignes repères) | gid://shopify/Product/15466411557249 | 4 | OK (13) |
| Toile premium polyester | gid://shopify/Product/15466411590017 | 2 | OK (12) |
| Guide de tondeuse | gid://shopify/Product/15466411655553 | 1 | OK (12) |
| Kit tufting complet 2-en-1 — gun, tondeuse et toile | gid://shopify/Product/15466411688321 | 28 | OK (19) |
| Brosse de finition | gid://shopify/Product/15466412835201 | 3 | OK (15) |
| Spatule à colle pour tufting | gid://shopify/Product/15466412900737 | 1 | OK (13) |
| Équilibreur de ressort (spring balancer) | gid://shopify/Product/15466412933505 | 1 | OK (12) |
| Ruban de finition tissé pour bordures (10 m) | gid://shopify/Product/15466413752705 | 1 | OK (12) |
| Ruban adhésif de finition | gid://shopify/Product/15466413785473 | 1 | OK (12) |
| Miroir acrylique pour tufting | gid://shopify/Product/15466414408065 | 32 | OK (16) |

Bilan : 20 produits traités, 107 liaisons variante→média détachées, 0 userError sur les 5 batchs de mutations. Vérification finale par re-query : aucune variante des produits traités n'a plus de média lié ; mediaCount inchangés partout ; exclusions intactes.

## Purge des images fournisseur (22/07)

Suppression des images fournisseur AliExpress via `productDeleteMedia` (21 mutations, 0 mediaUserError). Règle : garder les 6 médias dont l'alt correspond à « {titre} — image {1..6} » ; contrôle de sécurité (exactement 6 gardés) validé sur chaque produit avant suppression. Cas particuliers : fil acrylique = 6 générées + 87 images liées aux variantes conservées ; tufting gun 2-en-1 et pièces détachées non touchés (aucune image générée).

| Produit | ID | Supprimés | Restants (vérif re-query) |
|---|---|---|---|
| Tissu de finition | gid://shopify/Product/15466411131265 | 6 | 6 ✓ |
| Tissu de finition antidérapant | gid://shopify/Product/15466411196801 | 6 | 6 ✓ |
| Fil acrylique en cône pour tufting | gid://shopify/Product/15466411229569 | 6 | 93 (6 générées + 87 variantes) ✓ |
| Grippers — bandes de fixation (lot de 8) | gid://shopify/Product/15466411262337 | 7 | 6 ✓ |
| Bobineuse à laine | gid://shopify/Product/15466411295105 | 7 | 6 ✓ |
| Ciseaux pélican pour tufting | gid://shopify/Product/15466411327873 | 6 | 6 ✓ |
| Enfile-laine pour tufting gun (lot de 5) | gid://shopify/Product/15466411360641 | 9 | 6 ✓ |
| Tondeuse professionnelle pour tapis | gid://shopify/Product/15466411426177 | 7 | 6 ✓ |
| Ciseaux électriques de sculpture | gid://shopify/Product/15466411458945 | 8 | 6 ✓ |
| Lames de remplacement pour tondeuse (lot de 12) | gid://shopify/Product/15466411491713 | 6 | 6 ✓ |
| Kit tondeuse + guide de tonte | gid://shopify/Product/15466411524481 | 8 | 6 ✓ |
| Toile primaire de tufting (lignes repères) | gid://shopify/Product/15466411557249 | 7 | 6 ✓ |
| Toile premium polyester | gid://shopify/Product/15466411590017 | 6 | 6 ✓ |
| Guide de tondeuse | gid://shopify/Product/15466411655553 | 6 | 6 ✓ |
| Kit tufting complet 2-en-1 — gun, tondeuse et toile | gid://shopify/Product/15466411688321 | 13 | 6 ✓ |
| Brosse de finition | gid://shopify/Product/15466412835201 | 9 | 6 ✓ |
| Spatule à colle pour tufting | gid://shopify/Product/15466412900737 | 7 | 6 ✓ |
| Équilibreur de ressort (spring balancer) | gid://shopify/Product/15466412933505 | 6 | 6 ✓ |
| Ruban de finition tissé pour bordures (10 m) | gid://shopify/Product/15466413752705 | 6 | 6 ✓ |
| Ruban adhésif de finition | gid://shopify/Product/15466413785473 | 6 | 6 ✓ |
| Miroir acrylique pour tufting | gid://shopify/Product/15466414408065 | 10 | 6 ✓ |
| Tufting gun 2-en-1 Cut & Loop | gid://shopify/Product/15466410213761 | 0 (exclu) | 9 inchangé ✓ |
| Pièces détachées pour tufting gun | gid://shopify/Product/15466415292801 | 0 (exclu) | 40 inchangé ✓ |

Bilan : 21 produits purgés, 152 médias fournisseur supprimés, 0 erreur, aucun THROTTLED. Vérification finale par re-query : les 20 produits standard ont exactement 6 médias en positions 1-6 avec les alts « — image 1..6 » dans l'ordre ; le fil acrylique a ses 6 générées en tête + 87 images de coloris liées aux variantes ; les 2 produits exclus sont inchangés. Sauvegarde locale des originaux : `boutique-tufting/assets/source/aliexpress/`.

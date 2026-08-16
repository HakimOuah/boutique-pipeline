# Exécution Tuftéo — 16/08/2026

## Purge des prix barrés

**Décision Hakim** : passer `compareAtPrice` à `null` sur toutes les variantes de tous les produits (catalogue portait un prix barré fabriqué à +30 %, motif de refus Google Shopping / pratique commerciale trompeuse Omnibus). Ne jamais toucher `price`.

### Sauvegarde (avant écriture)

Fichier : `boutique-pipeline/boutique-tufting/shopify/backups/2026-08-16-prix-barres/avant.json`

Source : API Admin GraphQL, requête `products(first:50) { variants(first:100) }`, `hasNextPage: false` confirmé sur la liste de produits et sur chaque liste de variantes (y compris `fil-acrylique-tufting` et `miroir-acrylique-tufting`).

- **40 produits** au total dans le catalogue (215 variantes), tous capturés.
- **22 produits / 196 variantes en périmètre** (à traiter).
- **Hors périmètre, déjà propres** (`compareAtPrice: null` déjà en place) : `ciseaux-electriques-sculpture` (2 variantes, fait par Claude) et les **17 fiches** `fil-acrylique-tufting-<couleur>` (1 variante chacune).
- Écart avec l'estimation du brief : `fil-acrylique-tufting` a **87 variantes réelles** (confirmé via `variantsCount` API), pas 86 comme l'estimation indiquait. `miroir-acrylique-tufting` (32) et `pieces-detachees-tufting-gun` (37) confirmés exacts.
- Cas particulier signalé : `pieces-detachees-tufting-gun` (DRAFT, 37 variantes) a `compareAtPrice == price` sur toutes ses variantes (remise affichée à 0 %). Même traitement : `null`.

Fichier relu après écriture, décompte vérifié par script Python : 22 produits `in_scope`, 196 variantes `in_scope`.

### Écritures (`productVariantsBulkUpdate`, `compareAtPrice: null` uniquement)

Champ `price` jamais inclus dans les inputs. 22 mutations exécutées, une par produit, séquentiellement (espacées pour éviter le 503 de limitation Shopify). `userErrors: []` sur les 22 appels.

| Produit | handle | Variantes traitées | Résultat |
|---|---|---|---|
| Tufting gun 2-en-1 Cut & Loop | tufting-gun-2-en-1 | 2 | OK |
| Tissu de finition | tissu-de-finition | 2 | OK |
| Tissu de finition antidérapant | tissu-finition-antiderapant | 5 | OK |
| Fil acrylique en cône pour tufting | fil-acrylique-tufting | 87 | OK |
| Grippers — bandes de fixation (lot de 8) | grippers-tufting | 2 | OK |
| Bobineuse à laine | bobineuse-a-laine | 1 | OK |
| Ciseaux pélican pour tufting | ciseaux-pelican-tufting | 1 | OK |
| Enfile-laine pour tufting gun (lot de 5) | enfile-laine-tufting-gun | 3 | OK |
| Tondeuse électrique pour tapis | tondeuse-professionnelle-tapis | 1 | OK |
| Lames de remplacement pour tondeuse (lot de 12) | lames-tondeuse-lot-12 | 1 | OK |
| Kit tondeuse + guide de tonte | kit-tondeuse-guide-tonte | 3 | OK |
| Toile primaire de tufting (lignes repères) | toile-primaire-tufting | 8 | OK |
| Toile premium polyester | toile-premium-polyester | 2 | OK |
| Guide de tondeuse | guide-de-tondeuse | 1 | OK |
| Kit Tufting Complet | kit-tufting-complet | 1 | OK |
| Brosse de finition | brosse-de-finition | 3 | OK |
| Spatule à colle pour tufting | spatule-a-colle-tufting | 1 | OK |
| Équilibreur de ressort (spring balancer) | equilibreur-de-ressort | 1 | OK |
| Ruban de finition tissé pour bordures (10 m) | ruban-finition-tisse-10m | 1 | OK |
| Ruban adhésif de finition | ruban-adhesif-finition | 1 | OK |
| Miroir acrylique pour tufting | miroir-acrylique-tufting | 32 | OK |
| Pièces détachées pour tufting gun (cas particulier compareAtPrice==price) | pieces-detachees-tufting-gun | 37 | OK |
| **Total** | | **196** | |

Non touchés (déjà propres, hors périmètre) : `ciseaux-electriques-sculpture` (2 variantes) et les 17 fiches `fil-acrylique-tufting-<couleur>` (1 variante chacune) — 19 variantes.

### Vérification (16/08/2026)

**1. Décompte `compareAtPrice` restants** — re-requête complète de l'API (`products(first:50) { variants(first:100) }`, tous les `hasNextPage: false`) : sur les **215 variantes** du catalogue (196 traitées + 19 déjà propres), **0 variante a encore un `compareAtPrice` non nul**.

**2. Prix de vente inchangés** — comparaison automatisée (script Python) entre le fichier `avant.json` et la re-requête post-écriture, variante par variante sur les 215 : **215/215 prix identiques**, 0 écart, 0 variante manquante des deux côtés.

**3. Prévisualisation réelle (thème brouillon `gid://shopify/OnlineStoreTheme/189410738561`)** — session navigateur, URL `https://tufteo.com/products/<handle>?preview_theme_id=189410738561` (bandeau « Draft » visible en bas de chaque capture, confirmant qu'on est bien sur le thème brouillon et non le thème publié) :

- **`kit-tufting-complet`** : `€269` seul affiché, aucun `359,00 €` barré, aucun badge promo. Capture faite.
- **`tufting-gun-2-en-1`** : `€149` seul affiché (variantes Rose/Bleu), aucun `189,00 €` barré. Capture faite.
- **`miroir-acrylique-tufting`** (32 variantes, cas le plus exposé) : `€12,90` seul affiché sur la variante par défaut (Doré foncé / Ø10cm), aucun `16,90 €` barré. Capture faite.
- **Page collection `/collections/all`** (liste des cartes produit, endroit où s'affichent les badges promo) : extraction texte complète de la page — aucune mention « Promo » ni pourcentage de réduction sur une carte produit (le seul « -10 % » présent est le bandeau du code de bienvenue BIENVENUE10, sans rapport avec le prix barré). Confirmé aussi par inspection DOM : les 25 `span.compare-at-price` et les 25 `div.product-badges--top-right` présents dans le markup du thème sont **tous vides** (`nonEmptyBadges: 0`, `nonEmptyCompare: 0`) — le thème masque bien l'élément quand `compareAtPrice` est `null`, pas de résidu visuel.

**Aucun badge « -30 % » / « Promo » résiduel constaté.** Pas de signalement à faire à l'agent thème sur ce point.

### Décisions qui attendent Hakim

- Aucune sur ce chantier : la purge est une exécution technique pure, pas d'arbitrage de conformité (prix, promo, licence) à trancher ici.

### Ce que je n'ai pas pu vérifier

- **Le rendu sur mobile** n'a pas été contrôlé (viewport desktop uniquement pour les 3 captures et l'inspection DOM). À faire avant mise en flux Shopping si Hakim veut une garantie mobile-first complète.
- **Les autres pages du thème pouvant afficher un prix** (page panier, résumé de commande, éventuel bloc « produits complémentaires » sur d'autres gabarits que la fiche produit et la collection) n'ont pas été parcourues une par une — seules la fiche produit (×3) et la page collection `/collections/all` ont été contrôlées.
- **Le thème publié (MAIN)** n'a pas été regardé : par construction, cette purge ne touche que les données produit (API), donc le thème publié affichera aussi `null` dès que Hakim le publiera — mais je ne l'ai pas revérifié sur le live puisque je n'ai pas le droit d'y toucher ni de le publier.
- **Le flux Google Shopping / Merchant Center** lui-même n'a pas été contrôlé (pas d'accès, et hors périmètre — aucune modification Ads/Merchant Center autorisée). La purge corrige la source (Shopify), pas la resynchronisation du feed, qui suit son cycle normal.

### Sauvegarde et réversibilité

Fichier complet avant écriture : `boutique-pipeline/boutique-tufting/shopify/backups/2026-08-16-prix-barres/avant.json` (40 produits, 215 variantes, avec le detail par variante `price`/`compareAtPrice` et le flag `in_scope`). Pour revenir en arrière sur un produit donné, relire ce fichier et repasser `compareAtPrice` à la valeur d'origine via `productVariantsBulkUpdate`.


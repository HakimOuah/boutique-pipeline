# Protocole de sourcing (lots pergola, 09/09/2026)

Répertoire de travail : `/Users/Hakim/Documents/Boutiques drop` (toujours des chemins absolus). Travail en premier plan uniquement, aucun sous-agent, aucune tâche en arrière-plan.

## Entrées
- Produits du lot : `boutique-pipeline/analyses/2026-09-09-pergola-sourcing/lot<N>-produits.json` (champs `row`, `collection`, `produit`, `volume`).
- Candidats : `serp-pergola.txt` et `serp-accessoires.txt` dans le même dossier. Format d'une ligne : `productId | prix mini affiché | ventes | note | badges | titre`. Les SERP sont triées par ventes ; les chiffres SERP ne valent rien tant qu'ils ne sont pas confirmés par la passerelle.
- Passerelle (lecture seule, ~5–15 s par appel) :
  - `python3 boutique-pipeline/codex-chasse-clusters/tools/aliexpress_vps_gateway.py variants <productId>` → titre, magasin (pays, notes), rating, evaluation_count, sales_count, liste des variantes (`properties[].name/raw_value/value`, `offer_sale_price`, `sku_price`, `stock`, `tax_included`).
  - `python3 boutique-pipeline/codex-chasse-clusters/tools/aliexpress_vps_gateway.py exact <productId> --destination FR --property "<name>=<raw_value>"` (répéter `--property` pour chaque propriété de la variante, ex. `--property "Couleur=Gris foncé" --property "Expédié depuis=China Mainland"`) → prix exact TTC livré en France, options de fret (`ship_from_country`, délai en jours, `free_shipping`).
  - Ne jamais utiliser `search` (inutile). Pas de navigateur.

## Règles de qualification
- Pour chaque produit : choisir 2 à 3 candidats plausibles par le titre (taille, adossée/murale, motorisée, accessoire…), appeler `variants`, puis `exact` sur la variante la plus proche du produit demandé. S'arrêter dès qu'un candidat est conforme.
- Prix retenu = prix TTC **livraison en France incluse** (frais de port ajoutés s'ils ne sont pas gratuits). Le prix doit être celui d'une pergola entière ou de l'accessoire entier.
- Pièges → statut FOURNISSEUR À TESTER : propriété `raw_value`/`value` = « Consult before place », « Sample », « CUSTOMIZED sqm », « One square meter », « Accessories », « Deposit », ou `offer_sale_price` ≈ moitié de `sku_price` sans explication, ou prix affiché au mètre carré. Signaler la raison dans `remarque`.
- AUCUNE OFFRE EXPLOITABLE : aucun candidat ne correspond au produit (taille/type non confirmés par le titre ou les propriétés), livraison FR impossible, délai > 90 jours, stock 0/1 fictif sans variante réelle. Si un substitut proche existe (ex. taille voisine), le mettre dans `substitut` (id, url, prix, raison) sans changer le statut.
- OFFRE TROUVÉE : variante réelle correspondant au produit, prix `exact` confirmé (offer_sale_price = sku_price ou remise explicite), livrable FR, magasin lisible (notes ≥ 4.5 de préférence).
- Jamais de commande, jamais de message vendeur, jamais de statut FOURNISSEUR RETENU (décision Hakim).
- Un même identifiant peut servir plusieurs produits du lot (ex. fiche multi-tailles) : le réutiliser sans rappeler `variants`, mais rappeler `exact` avec la variante propre à chaque taille.

## Sortie
Écrire `boutique-pipeline/analyses/2026-09-09-pergola-sourcing/sourcing-lot<N>.json` : liste d'objets, un par ligne du lot, dans l'ordre du lot, avec les clés exactes :
`row`, `produit`, `statut`, `product_id`, `url` (`https://www.aliexpress.com/item/<id>.html`), `titre`, `variante` (ex. `Couleur=Gris foncé / Taille=4x3m`), `prix_ttc_eur` (nombre, livraison incluse), `sku_price_eur`, `ship_from`, `delai_jours` (ex. `"17-23"`), `port` (`"gratuit"` ou montant), `stock`, `ventes`, `note_magasin`, `magasin`, `candidats_ecartes` (liste `{id, motif}`), `remarque`, et `substitut` (objet ou null).
Pour AUCUNE OFFRE EXPLOITABLE laisser `product_id`/`url`/prix vides ("" ou null) sauf `substitut`.
Vérifier que le JSON se charge (`python3 -c "import json;json.load(open(...))"`) et compte autant d'objets que le lot. Réponse finale : 8 lignes max (compte par statut, 2–3 remarques notables). Ne pas modifier le Google Sheet.

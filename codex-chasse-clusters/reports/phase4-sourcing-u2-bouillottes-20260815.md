# U2 bouillottes — sourcing AliExpress officiel limité

- Date : 2026-08-15
- Source : AliExpress Open Platform / AE-Dropshipper via gateway VPS allowlisté
- Destination demandée : France
- Mode : lecture seule
- Précondition : marché et panier classés `GO_CONDITIONNEL_SOURCING_ECO` par le pilote

## Requêtes exécutées

| Heure UTC | Requête | Limite | Résultat pertinent |
|---|---|---:|---|
| 17:08:40 | `microwave flaxseed heating pad neck` | 5 | 0/5 |
| 17:08:48 | `rubber hot water bottle knitted cover 2 liter` | 5 | 0/5 |
| 17:08:57 | `hot water bag plush cover winter warmer` | 10 | 0/10 |
| 17:09:05 | `bouillotte eau chaude housse peluche 2L` | 10 | 0/10 |

## OBSERVE

- Les quatre appels ont répondu `ok: true` ; l'accès API et la destination `FR` ont donc fonctionné.
- Les 30 résultats retournés étaient hors intention : oreillers/massage, accessoires bébé, pulvérisateurs, bouteilles, housses auto, accessoires de pluie, camping ou autres objets sans rapport exact avec une bouillotte vendable.
- Aucun `product_id` pertinent n'a été retenu. Par conséquent, aucune action `variants` ou `exact` n'a été exécutée et aucun SKU, stock, prix de variante ou fret France n'est qualifié.
- Aucun panier, commande, message vendeur, DSers, Shopify ou paiement n'a été touché.

## MANQUANT

- Identifiant AliExpress exact d'une bouillotte à eau, sèche ou peluche cohérente avec les collections étudiées.
- Variante exacte, composition, capacité, mode de chauffe, avertissements, stock et coût rendu France.
- Preuve de conformité et de sécurité ; l'API produit ne la fournirait pas à elle seule.
- Économie de commande : coût produit, fret, réserve retours/défauts, paiement, TVA et CAC.

## Verdict de sourcing

`REPARER_AVANT_SOURCE_EXACTE`

Le marché U2 reste le seul univers qui justifie un sourcing limité, mais la recherche AliExpress accessible n'a trouvé aucune fiche exacte. Conformément au gate, un accès technique fonctionnel avec zéro fiche pertinente est un échec de sourcing, pas un `RETENU_MARCHE_A_SOURCER`. L'économie fournisseur ne peut pas être calculée et aucun `GO lancement` n'est émis.

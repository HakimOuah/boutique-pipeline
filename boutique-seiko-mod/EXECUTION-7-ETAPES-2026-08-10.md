# Exécution des 7 étapes — Maison Noirmont — 10/08/2026

## Cadre

- État cible : `GMC_READY`.
- Mode économique : boutique spécialisée à catalogue étendu, déjà validée et en construction ; cette passe reste aux portes 4 et 5.
- Aucun achat ni paiement.
- Aucune activation de produit, publication de collection, suppression du mot de passe ou création Merchant Center avant la preuve des cinq conditions de la passation.

## Journal des actions

### Correction de la collection active « Cadrans à chiffres »

- Collection : `gid://shopify/Collection/691208290642`
- Handle : `montre-cadran-a-chiffres`
- État initial observé par le MCP Shopify le 10/08/2026 : 5 produits actifs ; description contenant « et non des chiffres orientaux de l'écriture arabe : nous n'en proposons pas ».
- Cible autorisée : supprimer uniquement la contradiction future, sans changer le titre, le handle, les produits, l'image, l'ordre de tri ni le statut de publication.
- Nouvelle phrase : « Il s'agit bien des chiffres 1 à 12 que vous lisez ici, et non des chiffres orientaux de l'écriture arabe, qui constituent une famille distincte. »
- Rollback : remettre la phrase initiale dans `descriptionHtml` via la mise à jour de collection Shopify.
- Résultat : modification appliquée via le MCP Shopify le 10/08/2026.
- Vérification après écriture : nouvelle lecture MCP conforme ; titre, handle, image, tri, type manuel, 5 produits actifs et leurs prix sont inchangés. Seule la phrase ciblée diffère.

## État des sept étapes

| Étape | Statut | Preuve ou blocage |
|---|---|---|
| 1. File visuelle stériles et pilote | EN COURS | Exécuteur vivant constaté ; ne pas forcer le verrou. |
| 2. Re-sourcing arabe | EN COURS | 1 produit qualifié le 09/08 ; recherche API complémentaire ouverte. |
| 3. Cinq fiches arabes bloquées | EN COURS | Recherche de photos alternatives par API ouverte. |
| 4. Import, rédaction et habillage | EN ATTENTE | Dépend du lot qualifié et de la décision sur les cinq fiches. |
| 5. Nettoyage catalogue | EN COURS | Contradiction de collection corrigée et relue ; doublons, cadran à verbatim Rolex, nuanciers et doutes restent à statuer. |
| 6. 319 visuels des fiches actives | EN ATTENTE | Inventaire actuel à réconcilier après la file prioritaire. |
| 7. Activation | BLOQUÉE PAR CONDITIONS | Aucune activation tant que les cinq conditions ne sont pas toutes prouvées. |

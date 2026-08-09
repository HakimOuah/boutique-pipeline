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

### Nettoyage réversible des doublons et du cadran à risque de marque

Décision : archiver les fiches perdantes plutôt que les supprimer. Cela retire les fiches du catalogue exploitable tout en conservant un rollback et les correspondances DSers.

| Fiche archivée | Motif | Fiche conservée / preuve de choix |
|---|---|---|
| `cadran-pilote-29-aiguilles-nh35` — `gid://shopify/Product/11013081563474` — AliExpress `1005006012512581` | Même produit, mêmes 21 variantes et mêmes photos que l'autre fiche. | `cadran-pilote-29-classique-nh36` / `1005007635155982` : prix source inférieur et signal fournisseur plus fort dans le relevé du 09/08. |
| `cadran-pilote-noir-33-5-nh35` — `gid://shopify/Product/11013081629010` — AliExpress `1005003002119259` | Même produit et mêmes photos ; fiche plus complexe avec variantes de compatibilité supplémentaires et signal fournisseur plus faible. | `cadran-pilote-noir-33-5-nh34` / `1005008660462030` : 324 ventes relevées contre 130, 96 avis contre 16, catalogue de variantes plus lisible. |
| `mouvement-nh35-japon` — `gid://shopify/Product/11013057478994` — AliExpress `1005005597724853` | Même mouvement NH35, date blanche à 3 h ; stock Shopify observé 158. | `mouvement-nh35-date-blanche` / `1005008494235697` : stock observé 9 667, prix légèrement inférieur et signal fournisseur restant élevé (+5 000 ventes, 740 avis au relevé du 09/08). |
| `cadran-lumineux-28-5-nh35` — `gid://shopify/Product/11013078909266` | Le cadran porte « SUPERLATIVE CHRONOMETER / OFFICIALLY CERTIFIED », verbatim Rolex incompatible avec la ligne sans marque. | Aucun remplacement automatique ; un produit propre devra être qualifié séparément. |

État initial relu via le MCP Shopify le 10/08/2026 : les quatre fiches sont `DRAFT`. Aucune fiche active n'est visée. Rollback : repasser individuellement une fiche de `ARCHIVED` à `DRAFT` après nouvelle preuve.

Résultat : les quatre passages à `ARCHIVED` ont réussi. Une seconde lecture MCP confirme `ARCHIVED` pour chaque GID, avec le nombre de variantes et l'inventaire inchangés.

## État des sept étapes

| Étape | Statut | Preuve ou blocage |
|---|---|---|
| 1. File visuelle stériles et pilote | EN COURS | Exécuteur vivant constaté ; ne pas forcer le verrou. |
| 2. Re-sourcing arabe | EN COURS | 1 produit qualifié le 09/08 ; recherche API complémentaire ouverte. |
| 3. Cinq fiches arabes bloquées | EN COURS | Recherche de photos alternatives par API ouverte. |
| 4. Import, rédaction et habillage | EN ATTENTE | Dépend du lot qualifié et de la décision sur les cinq fiches. |
| 5. Nettoyage catalogue | EN COURS | Contradiction corrigée ; trois doublons perdants et cadran à verbatim Rolex archivés puis relus. Nuanciers et doutes restent à statuer. |
| 6. 319 visuels des fiches actives | EN ATTENTE | Inventaire actuel à réconcilier après la file prioritaire. |
| 7. Activation | BLOQUÉE PAR CONDITIONS | Aucune activation tant que les cinq conditions ne sont pas toutes prouvées. |

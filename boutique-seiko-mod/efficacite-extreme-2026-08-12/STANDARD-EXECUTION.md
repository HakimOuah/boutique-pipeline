# Standard d'exécution visuelle — efficacité extrême

## Périmètre

- Tous les produits Shopify `ACTIVE` ou `DRAFT`.
- Les produits `ARCHIVED` restent hors production tant qu'ils ne sont pas réactivés.
- Objectif final : aucun média AliExpress ou fournisseur brut dans la galerie d'un produit non archivé.

## Couverture minimale par famille

| Famille | Couverture exigée |
|---|---|
| Cadran | Un visuel par coloris ou finition visuellement distincte. Les calibres compatibles et tailles identiques partagent le média. |
| Montre | Un visuel par combinaison visuelle distincte de cadran, boîtier et bracelet. Les variantes techniques invisibles partagent le média. |
| Bracelet | Un visuel par couleur et finition de boucle. Les longueurs ou largeurs partageant le même aspect partagent le média. |
| Boîtier, lunette, insert, aiguilles | Un visuel par couleur, finition ou géométrie distincte. |
| Petit outil ou accessoire | Un visuel principal propre par produit ; variantes seulement si l'apparence change réellement. |
| Écrin, rouleau, remontoir | Un visuel par couleur, capacité ou construction visuellement distincte. |

## Production 80/20

- Réutiliser tout fichier local déjà validé avant de générer.
- Une tentative standard par apparence ; une seule reprise ciblée si le défaut est simple et si le produit reste prioritaire.
- Après deux échecs, l'apparence est bloquée et le produit ou la variante reste hors publication jusqu'à nouvelle source exacte.
- Aucun POC de reconstruction complexe d'aiguilles, de texte ou de mécanisme.
- QA bloquante limitée à : produit exact, couleur/finition exacte, géométrie essentielle, absence de marque/filigrane/texte interdit, cadrage exploitable.
- JPEG carré 2048 px, sRGB, poids cible inférieur à 1,2 Mo.

## Shopify

- Prévol live des médias, variantes, associations, prix, stock, statut et image principale.
- Ajouter les nouveaux médias et associer toutes les variantes partageant l'apparence.
- Relire les associations avant toute suppression.
- Retirer les médias AliExpress uniquement après preuve que leur remplacement exact est `READY` et correctement associé.
- Ne jamais modifier SKU, prix, stock, options, statut ou image principale en dehors de l'opération explicitement prévue.
- Conserver dans le registre le media GID et l'URL supprimés pour rollback.

## Suivi

- Un seul registre global machine-readable.
- Pas de rapport narratif par image ou par produit.
- Compteurs obligatoires : produits audités, produits sans AliExpress, apparences requises, apparences couvertes, fichiers à produire, fichiers validés, médias uploadés, associations vérifiées, médias fournisseur retirés, produits bloqués.

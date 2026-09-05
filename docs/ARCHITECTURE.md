> Statut depuis le 5 septembre 2026 : moteur Dropilot historique de classement indicatif. Sa configuration et ses anciens seuils ne qualifient pas un candidat. Le code rend TECHNICAL_INCONCLUSIVE ; appliquer PRODUCT-RESEARCH-CRITERIA.md pour une qualification actuelle.

# Architecture Dropilot

## Sources de vérité

- `config/pipeline.yaml` : marchés, filtres, pondérations, seuils et portes finales ;
- `data/dropilot.sqlite3` : historique, déduplication, statuts et campagnes ;
- `reports/` : exports auditables JSON, CSV et Markdown ;
- `shopify-portable/` : composants de page produit transférables.

Le dossier `recherche-prod-extracted/` reste une archive historique. Son ancien broyeur n’est plus la
source de vérité opérationnelle.

## Deux niveaux de décision

1. Le broyeur classe `shortlist`, `review` ou `reject` à partir du ticket, de la marge, du canal,
   de la concurrence, de la source et de la défendabilité.
2. Le verdict final reste `MAYBE` jusqu’à validation de la demande Google, du fournisseur, de la
   légalité, de la marge nette et de la différenciation. Seul un dossier complet devient `GO`.

Les seuils UK et DE sont volontairement `null` dans la première configuration. Aucun produit sur
ces marchés ne peut être automatiquement déclaré GO avant une décision explicite sur leurs seuils.

## Flux

```text
Source brute
-> normalisation
-> empreinte anti-doublon
-> SQLite
-> scoring YAML
-> portes finales
-> rapport
-> validation humaine
-> projet Shopify
-> Merchant Center / Google Ads
-> import des performances
```

## Sécurité

- aucune clé dans Git ;
- API BigBuy sandbox par défaut ;
- webhook lié à la boucle locale par défaut ;
- noms de fichiers limités à la boîte d’entrée ;
- aucune décision couper/scaler automatisée ;
- aucune métrique manquante inventée.


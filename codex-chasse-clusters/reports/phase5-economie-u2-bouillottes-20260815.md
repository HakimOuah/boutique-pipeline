# U2 bouillottes — économie après sourcing limité

- Date : 2026-08-15
- Verdict : `ECONOMIE_MANQUANTE_APRES_ECHEC_SOURCE`
- Portée : calcul préparatoire, aucune hypothèse cachée

## Entrées observées

| Entrée | Valeur | Source / statut |
|---|---:|---|
| Médiane de 40 offres | 17,63 EUR | `OBSERVE` |
| Part sous 15 EUR | 40 % | `OBSERVE` |
| Panier/coffret marchand explicite | 58,50 EUR | La Bulle Naturelle, `OBSERVE` |
| Autres paniers de deux références atteignant le franco | environ 50–60 EUR | concurrents U2, `OBSERVE` |
| CPC SEMrush France | 0,09–0,21 USD selon sous-intention | `OBSERVE`, devise différente du panier |
| Coût produit du SKU exact | absent | `MANQUANT` |
| Fret France du même SKU | absent | `MANQUANT` |
| Taux de conversion et CAC | absents | `MANQUANT` |
| Retours, défauts, paiement, TVA et SAV | absents | `MANQUANT` |

Le CPC affiché en USD et le panier en EUR ne sont pas combinés dans un ratio monétaire précis sans taux de change daté. Surtout, le CPC ne devient pas un CAC sans taux de conversion observé.

## Calculs qui restent impossibles

```text
CA net = prix TTC encaissé - remises - remboursements attendus
Coût variable hors ads = produit + fret + emballage + paiement
  + taxes non récupérables + retours/défauts + fulfilment/SAV
Marge contributive pré-ads = CA net - coût variable hors ads
CAC de rupture = marge contributive pré-ads
ROAS de rupture = CA net / CAC de rupture
```

Le sourcing API n'ayant fourni aucun produit pertinent, renseigner une valeur numérique dans ces formules inventerait le coût rendu et la sécurité du produit. Aucun scénario central, prudent ou optimiste n'est calculé.

## Lecture économique honnête

- Le panier marchand de 50–60 EUR et les CPC observés justifiaient une sonde fournisseur ; ils ne valident pas la contribution.
- La médiane produit de 17,63 EUR rend le panier mono-produit fragile, mais elle ne suffit pas à conclure sans coût rendu et taux de conversion.
- Les bundles ne peuvent être retenus que si deux produits exacts, sûrs et livrables sont qualifiés ensemble. Un bundle inventé ne répare pas l'économie.
- Les retours/défauts et la conformité peuvent être déterminants pour les modèles eau, micro-ondes, électriques et enfants.

## Condition de réouverture

Obtenir par une fiche AliExpress exacte ou une preuve fournisseur autorisée : produit, variante, composition/capacité, prix, stock et fret France. Recalculer ensuite les trois scénarios avec réserves explicites. Tant que cette condition manque, le dossier est `REPARER_AVANT` et non `RETENU_NIVEAU_2_ECO`.

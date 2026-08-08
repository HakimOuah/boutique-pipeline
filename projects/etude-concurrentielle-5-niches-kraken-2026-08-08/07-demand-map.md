# Carte de demande — étude concurrentielle cinq niches

- **Marché :** France / français
- **Date de mesure :** 2026-08-08
- **Mode :** `catalogue-volume`
- **Base :** recherches mensuelles commerciales nettoyées ; les totaux sont des sommes de requêtes exactes distinctes, pas des utilisateurs dédupliqués.

## Couverture par niche

| Niche | Volume nettoyé | Seuil 30 k | Confort 40 k | IDs AliExpress uniques | Gate demande |
|---|---:|---|---|---:|---|
| Mobilité chien | 81 860 | atteint | atteint | 118 | `GO` |
| Mercerie créative | 221 680 | atteint | atteint | 129 | `GO` |
| Scrap/journaling | 64 740 historique non reproduit | non prouvé | non prouvé | 125 historiques | `MANQUANT_RENETTOYAGE` |
| Perles/bijoux | 35 770 | atteint | non atteint | 130 | `GO_CONDITIONNEL` |
| Aquascaping | 48 320 | atteint | atteint | 130 | `GO` |

Nettoyage historique : retrait de `album photo` et `sticker` pour le scrap,
`perle` singulier pour les bijoux et `aquarium` générique pour l'aquascaping.
La mention ne suffit pas à reproduire le total scrap ; les détails restent
conservés dans le classeur mais le gate actif utilise la preuve reconstructible.

## Audit correctif scrap — phase 2

- `scrapbooking` : 27 100, avec SERP mixte commerciale/informationnelle.
- Union des ancres mesurées stockée : 11 360.
- Total historique stocké : 64 740.
- Formule, liste dédupliquée et classification d'intention permettant de passer
  de ces objets à 64 740 : `MANQUANT`.

Le marché n'est pas déclaré sans demande. En revanche, aucun nouveau total
« propre » n'est extrapolé : le seuil 30 k reste non prouvé jusqu'à une nouvelle
mesure requête par requête.

## Règles collections

- Collection cœur : 1 000+ ; 800–999 exige une justification.
- Collection secondaire : 500+ ; 300–499 exige une justification.
- Sous 300 : fusion, facette non indexée ou exception documentée.
- Aucune fiche produit n’a de minimum propre ; elle sert une intention réelle sans cannibalisation.

## Profondeur catalogue

| Mesure | Observé | Seuil lancement | Verdict |
|---|---:|---:|---|
| IDs uniques par niche, première salve | 118–130 | information | conforme à la demande de première salve |
| Produits distincts, publiables et réellement sourçables | `MANQUANT` | 200 | non prouvé |
| Variantes, doublons, indisponibles exclus | partiel | obligatoire | à terminer |

## Décision

- Gate demande historique : cinq niches étaient déclarées au-dessus du minimum ;
  cette conclusion est supplantée pour le scrap par `MANQUANT_RENETTOYAGE`.
- Gate catalogue de lancement : `MANQUANT` pour les cinq ; la salve actuelle n’est pas un catalogue de 200 produits validés.
- Condition de revue : shortlist, preuves SKU et économie du panier.

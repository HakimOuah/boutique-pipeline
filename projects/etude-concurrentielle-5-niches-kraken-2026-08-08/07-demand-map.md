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
| Scrap/journaling | 64 740 | atteint | atteint | 125 | `GO` |
| Perles/bijoux | 35 770 | atteint | non atteint | 130 | `GO_CONDITIONNEL` |
| Aquascaping | 48 320 | atteint | atteint | 130 | `GO` |

Nettoyage majeur : retrait de `album photo` et `sticker` pour le scrap, `perle` singulier pour les bijoux et `aquarium` générique pour l’aquascaping. Les détails collection par collection sont conservés dans le classeur de recherche.

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

- Gate demande : cinq niches passent le minimum.
- Gate catalogue de lancement : `MANQUANT` pour les cinq ; la salve actuelle n’est pas un catalogue de 200 produits validés.
- Condition de revue : shortlist, preuves SKU et économie du panier.

---
type: regle
id: RULE-2026-002
titre: Une page 1 mixte n'est pas une ouverture — le verrou se lit à la notoriété ou au prix plancher
statut: candidate
date: 2026-08-31
dimensions: [concurrence, marge]
boutiques_appui: [tufting]
boutiques_contre: []
acceptee_par_hakim: true
date_revue: 2026-12-31
---

# RULE-2026-002 — Une page 1 mixte n'est pas une ouverture

## Affirmation

Un marché est **verrouillé** si l'un des deux critères suivants est vrai :

- **A — notoriété** : les acteurs de page 1 qu'un acheteur citerait sans avoir cherché
  (marketplaces, enseignes nationales, marques connues hors du milieu) occupent la majorité de la
  page. Ils se battent sur la notoriété, pas sur le produit.
- **B — prix** : le prix plancher des acteurs comparables est inférieur ou égal au coût rendu
  du sourcing augmenté de la marge minimale. Il n'existe alors aucune bande de prix habitable.

Corollaire, qui est la partie contre-intuitive : **la diversité des types d'acteurs en page 1 ne
mesure pas l'ouverture.** Une page mixte décrit un sandwich — marketplaces en bas sur le prix,
marques installées en haut sur la confiance. « Ouvert » ne veut dire qu'une chose : il existe une
bande de prix occupable avec un produit sourçable.

Source : Hakim, 31/08/2026, en réponse à une inversion de verdict de la chaîne Hermes.

## Preuves à l'appui

**L'inversion qui l'a provoquée.** Niche basse-cour, 31/08 : la chaîne rend `STOP` au premier
passage, puis `GO` au second, avec pour motif « page 1 partagée […] sans domination d'un type
unique ». Le verdict humain du 08/08 était `STOP`, sur exactement la même structure lue comme un
sandwich. Détail : `hermes-orchestration/benchmarks/2026-08-31-test-stops-kraken.md`.

**Un précédent que la règle explique.** Tuftéo, recalage du 21/07/2026 : **six produits dont le
coût rendu dépassait le prix du concurrent**, consigné en une ligne avec la mention « à
re-sourcer », jamais instruit. C'est le critère B, levé et ignoré — six mois avant que la règle
existe. Voir [[tufting]], champ `signaux_ecartes`.

## Preuves contraires

Aucune à ce jour. La règle n'a pas encore été appliquée à une niche qui aurait ensuite réussi.

## Ce que ça change

- `cartographie-concurrence` ne rend plus `GO` sans coût rendu : **`REVIEW` par défaut**. Un GO
  sans coût rendu n'est pas un verdict, c'est un espoir.
- La sonde prix cesse d'être un exercice de positionnement pour devenir un **test d'habitabilité** :
  la question n'est plus « où se placer » mais « existe-t-il une place ».
- Rétroactivement, elle donne un motif d'examen aux six lignes du recalage Tuftéo.

## À revoir

Au 31/12/2026, ou dès qu'une niche jugée ouverte par cette règle aura été testée en campagne
jusqu'au seuil de [[RULE-2026-001]]. C'est le premier résultat réel qui la validera ou la retirera.

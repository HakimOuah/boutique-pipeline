---
type: regle
id: RULE-2026-004
titre: Le plancher de prix est le plancher comparable, jamais le plancher absolu
statut: candidate
date: 2026-08-31
dimensions: [concurrence, marge]
boutiques_appui: []
boutiques_contre: []
acceptee_par_hakim: true
date_revue: 2026-12-31
---

# RULE-2026-004 — Le plancher comparable

## Affirmation

Le prix plancher qui sert au critère B de [[RULE-2026-002]] est celui du **concurrent comparable** —
un vendeur indépendant proposant le même produit avec les mêmes caractéristiques essentielles.

Sont exclus du calcul : ce qui n'est pas le même produit (pièce, accessoire, kit incomplet, modèle
amputé de la fonction qui définit la famille), les marques officielles, les marques à récit, et le
bas de gamme marketplace.

**Test de vraisemblance :** un rapport plafond ÷ plancher supérieur à environ ×4 signale presque
toujours un plancher non comparable.

Source : Hakim, 31/08/2026.

## Preuves à l'appui

Test basse-cour du 31/08 : la chaîne retient **17,70 €** comme plancher d'une porte automatique de
poulailler, dans une bande qu'elle annonce elle-même **17,70–210 €** — un rapport de ×12. Le
plancher était un accessoire, pas le produit.

La règle existait déjà en creux dans le skill `recherche-mots-cles`, section sonde prix : *« écarter
marques officielles, marques à récit, bas de gamme marketplace »*, et *« juste sous le concurrent
comparable »*. Elle n'avait simplement jamais été rattachée au critère de verrou.

## Preuves contraires

Aucune.

## Ce que ça change

Sans elle, le critère B devient **presque toujours bloquant** : rien de sourçable ne bat un plancher
aberrant, donc toute niche finirait en verrou et la règle se viderait de sa valeur. C'est le mode de
défaillance à surveiller — une règle qui dit STOP à tout ne dit plus rien.

Le contrat exige désormais `produit_du_plancher` et `vendeur_du_plancher` : un plancher sans son
porteur n'est pas vérifiable.

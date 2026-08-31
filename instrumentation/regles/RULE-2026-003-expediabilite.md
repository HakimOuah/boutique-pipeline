---
type: regle
id: RULE-2026-003
titre: Un produit hors gabarit est exclu s'il part de Chine, conservé s'il part d'Europe
statut: candidate
date: 2026-08-31
dimensions: [operationnel, marge]
boutiques_appui: []
boutiques_contre: []
acceptee_par_hakim: true
date_revue: 2026-12-31
---

# RULE-2026-003 — Hors gabarit : l'origine décide

## Affirmation

Un produit qui ne rentre pas dans un colis standard n'est pas disqualifié par son encombrement
seul, mais par le **couple encombrement × origine** :

- hors gabarit expédié d'un **entrepôt UE** → tenable (délai court, retour gérable) ;
- hors gabarit expédié de **Chine** → exclu ;
- **origine inconnue** → verdict plafonné à `REVIEW`, jamais `GO`.

Source : Hakim, 31/08/2026.

## Preuves à l'appui

**Le précédent qui l'a fait écrire.** Test basse-cour du 31/08 : l'agent choisit « poulailler
4 poules » comme requête décisive **pour son panier** (100–849 €), alors que l'étude humaine du
08/08 excluait explicitement cette famille — *« hors cabanes/poulaillers, gros colis, tenus par les
spécialistes »*. L'agent optimisait le panier sans contrainte d'expédiabilité, faute que cette
contrainte soit écrite.

**Un précédent qui la confirme.** Sourcing Bonum Vitae du 18/08 : la variante Pologne du kit
d'entretien est refusée pour rupture, obligeant à passer par la Chine — et le rapport note que
« délai et douane sont à confirmer au panier ». L'origine était déjà traitée comme un facteur
décisif, sans être formulée en règle.

## Preuves contraires

Aucune. La règle n'a pas encore écarté une piste qui aurait ensuite réussi.

## Ce que ça change

Elle crée une **dépendance de séquence** : l'origine d'expédition se détermine au sourcing
(phase 4), alors que le choix de la requête décisive se fait bien avant. Un produit encombrant ne
peut donc pas recevoir de `GO` à l'étape cartographie — au mieux un `REVIEW` assorti de la mention
que l'origine doit être établie.

Corollaire à retenir : **un panier élevé sur un produit encombrant n'est pas un argument tant que
l'origine est inconnue.** C'est exactement ce qui rend ce type de produit attirant et invendable en
même temps.

Liens : [[RULE-2026-002]] pour le verrou, [[RULE-2026-001]] pour le seuil de dépense.

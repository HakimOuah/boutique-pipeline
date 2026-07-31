# Découpage lot 1 — corrections et points à trancher (25/07/2026)

Complément au livrable de l'agent `decoupage-coloris-lot1-2026-07-25.md`.

## ✅ Résultat : 19 fiches créées, catalogue à 44 produits

| Mère | Fiches créées | Var./fiche | Total |
|---|---|---:|---:|
| Trente-Six — Classique jubilé | 5 (Rouge, Bleu, Rose, Doré, Or intégral) | 4 | 20 |
| Trente-Neuf — Classique cannelée | 6 (Rouge, Bleu mer, Rose, Vert, Bleu, Noir) | 8 | 48 |
| Quarante-et-Un — Sport acier/cuir | 6 | 2 | 12 |
| Noirmont Un — Plongeuse | 1 (Bronze) | 6 | 6 |
| Trente-Neuf Duo — bicolore | 1 (Doré) | 6 | 6 |
| **Total** | **19** | | **92** |

Contrôle mécanique fait par l'agent : **92/92 SKU, prix et prix barrés identiques aux mères** (diff trié sur fichiers exportés), 92 SKU uniques, 19/19 avec visuel `READY` en 2048 px, collections et publication OK, zéro `userError`. **Les 5 fiches mères sont intactes** — aucune mutation ne leur a été adressée. L'opération reste annulable en supprimant les 19 IDs.

## ✅ Deux anomalies corrigées immédiatement

1. **Collection « Page d'accueil » héritée** — les 6 fiches Trente-Neuf s'étaient ajoutées à la collection mise en avant sur la home, qui affichait donc 7 montres quasi identiques. **Les 6 filles ont été retirées**, la mère reste. La home est revenue à son état voulu.
2. **Sous-titre « Sport acier » sur les versions cuir** — erreur de mon brief. Renommées :
   - « Quarante-et-Un Blanc — Sport cuir »
   - « Quarante-et-Un Bleu — Sport cuir »
   - « Quarante-et-Un Noir — Sport cuir »
   (Les handles sont inchangés, donc aucun lien cassé.)

## ⏳ Quatre points laissés à ton arbitrage

1. **Description du Duo : « chiffres romains »** alors que nos visuels montrent un cadran stérile à index bâtons. **Incohérence préexistante sur la fiche mère**, reprise par la fille. Je ne l'ai pas « corrigée » parce que je ne sais pas lequel des deux a raison : c'est peut-être le visuel généré qui est infidèle, et non le texte. À vérifier sur la fiche fournisseur avant de trancher — c'est une promesse produit, elle doit être exacte.
2. **Publication sur 3 canaux** (Boutique en ligne + Point de vente + Shop) au lieu du seul Online Store demandé. L'agent a aligné sur les mères, qui sont sur les trois — sinon les nouvelles fiches manquaient au canal Shop. Cohérent, mais à confirmer.
3. **Option composite du Duo** : l'option `Boîtier` de la mère mélangeait coloris, taille et fond. Conséquence héritée : le Doré n'existe qu'en fond verre, l'Or rose qu'en fond acier. Les 6 SKU Doré sont bien tous présents. À nettoyer si tu veux découpler taille et fond.
4. **Nommage des versions acier** : « Quarante-et-Un Bleu Acier — Sport acier » est redondant. Le schéma propre serait « Quarante-et-Un Bleu — Sport acier ». Non appliqué pour limiter les renommages.

## Prochaine étape irréversible : la réduction des mères

Chaque montre existe aujourd'hui **en double** : la mère avec tous ses coloris, et les fiches par coloris. La boutique n'étant pas publique, personne ne le voit. Réduire les mères à un coloris unique est l'étape **irréversible** — elle attend ton feu vert.

Coloris à conserver sur chaque mère :

| Mère | Coloris à garder |
|---|---|
| Trente-Six | **Noir** |
| Trente-Neuf | **Orange** |
| Quarante-et-Un | **Cadran blanc · bracelet acier** ET **Cadran noir · bracelet cuir M** (les deux non repris en fiche fille) |
| Noirmont Un | **Acier** |
| Trente-Neuf Duo | **Or rose** |

⚠️ Supprimer une variante détruit son mapping DSers. Les variantes supprimées des mères existent désormais dans les fiches filles, qui devront être mappées — d'où l'ordre : **mapper les filles d'abord, réduire les mères ensuite.**

## Mapping DSers des 92 variantes

Point de vigilance relevé par l'agent : les **doubles espaces des SKU sont préservés à l'octet** (`14:193#full  gold no logo`, `14:100013777#Black Dial  Yellow M`). L'auto-matching devrait donc passer, mais **à vérifier avant la première commande réelle**.

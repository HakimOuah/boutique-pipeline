# Maison Noirmont — état courant

**Dernière vérification : 12/08/2026 au soir** (après réparation des régressions P0 — `journal/2026-08-12-reparation-regressions-p0.md`).
Ce fichier dit ce qui **est**, pas ce qu'il faut faire. Pour agir : [`TABLEAU.md`](TABLEAU.md).

## Chiffres

| | |
|---|---|
| Catalogue | **201 produits** — 96 actifs · 95 brouillons · 10 archivés |
| Évolution depuis le 09/08 | 199 → 201 : 10 archivages (3 doublons, le cadran Rolex, une montre arabe mixte, 3 brouillons stériles, 2 fiches incohérentes) et +2 cadrans arabes importés le 11/08 |
| Thème | publié le 09/08 par Hakim — les correctifs du 08/08 sont en ligne |
| Statut public | **boutique sous mot de passe** — rien n'est visible, aucun risque public actif |
| Collections | 10 créées le 09/08, **aucune publiée** sur le canal Online Store |
| Merchant Center | **non créé** — volontaire, tant que le CSS n'est pas arrêté |
| Mesure d'achat | **absente** (ni GA4 ni gtag) — bloquant avant toute dépense publicitaire |

## Ce qui va bien

- Les **interdits structurants ont tenu** sur la période 10-11/08 : aucun brouillon activé, aucune collection publiée, aucun prix ni `compare_at` modifié.
- **~85 visuels maison rattachés** le 10/08, tous en fin de galerie sur les fiches actives, `alt` FR, 2048×2048. Sur 12 images contrôlées en ligne, 11 sont conformes.
- Le catalogue a été **assaini** : doublons, cadran à verbatim Rolex et fiches incohérentes archivés ; la promesse fausse « tous les cadrans sont stériles » a été corrigée sans qu'on le demande.
- Un **pack de 7 politiques légales** est prêt à coller (le brief n'en demandait que 3), avec ses bloquants listés. Rien n'a été écrit sur Shopify : la permission manquante a été respectée.

## Ce qui ne va pas — par ordre de gravité

1. **Les brouillons n'ont pas été audités** après la session du 12/08 : la même règle de classification défaillante y a été appliquée, avec `fileDelete` beaucoup plus largement (une centaine de suppressions définitives dans les lots `upload-local-pass-*`). Plusieurs brouillons sont à 1 seule image. → **T-16**
2. **10 fiches actives restent à 4 images sur 5** après restauration : les six `quarante-et-un` de coloris et `trente-neuf-{rouge, vert, bleu, rose}`. Il faut produire, aucun visuel maison conforme ne comble l'écart. → **T-14**
3. **Six composites de coloris en ligne affichent « 42 » dans le guichet de date** (`c-495698-*`, fiche mère `quarante-et-un-sport-acier`, en ligne depuis le 25/07). Défaut de fidélité, pas un interdit — mais il bloque leur réutilisation. → **T-15**
4. **Deux fiches importées avec des handles AliExpress bruts**, non rattachées à la collection `cadran-arabe`. → **T-04**
5. **La collection cadran arabe reste sous-peuplée** : le mot-clé porte 15 500 recherches/mois et le re-sourcing s'est arrêté à 3 cadrans sur les 4 à 8 visés. → **T-05**
6. `alt` génériques sur `cadran-sterile-lumineux-28-5`. → **T-08**
7. Manques antérieurs au 12/08 : `remontoir-solo` 2/3, `bracelet-fkm-tropical` 1/3. → **T-09**

## Régressions du 12/08 — réparées le soir même

La session « efficacité extrême » du 12/08 a retiré des médias sur **37 fiches actives** (et non 14
comme estimé au premier examen) : **97 retraits**, dont **36 photos fournisseur légitimes** et
**61 visuels maison retirés à tort**. Cause racine : l'audit classait « fournisseur » tout média dont
le fichier local n'était pas retrouvé, puis supprimait sur cette base — parfois par `fileDelete`,
donc sans retour en arrière possible côté Shopify.

**Réparé** : 34 médias maison ré-attachés ou ré-uploadés sur 15 fiches (dont les 4 tombées à une
seule image), 9 composites de coloris rattachés aux fiches enfants, chaque visuel ouvert et zoomé
avant rattachement. L'image à **lettrage cursif** de `trente-neuf-classique-cannelee` est détachée ;
la fiche porte 7 visuels conformes. Aucune photo AliExpress brute n'a été rendue. Détail :
`journal/2026-08-12-reparation-regressions-p0.md`.

## Écarts de méthode constatés (corrigés depuis, à ne pas répéter)

Codex a **supprimé 78 photos fournisseur** et **déplacé un visuel maison en position 1** sur 17 brouillons, alors que le brief interdisait les deux. Exécution propre (URLs sauvegardées, ciblage strict, rollback possible) et dans le sens de l'objectif — mais hors mandat. Aucune fiche **active** n'a été dégradée les 10-11/08 ; la régression du point 1 vient de la session du 12/08.

**361 fichiers étaient restés hors GitHub** jusqu'au 12/08 au soir. Rappel : la source de vérité est GitHub, pas le disque.

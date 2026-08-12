# Maison Noirmont — état courant

**Dernière vérification : 13/08/2026** (après l'audit des 95 brouillons — `journal/2026-08-13-audit-reparation-brouillons.md`).
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
| Visuels des 95 brouillons | 1 420 médias — **329 maison / 1 091 photos AliExpress brutes** · 43 fiches 100 % maison, 13 mixtes, 39 encore entièrement brutes |

## Ce qui va bien

- Les **interdits structurants ont tenu** sur la période 10-11/08 : aucun brouillon activé, aucune collection publiée, aucun prix ni `compare_at` modifié.
- **~85 visuels maison rattachés** le 10/08, tous en fin de galerie sur les fiches actives, `alt` FR, 2048×2048. Sur 12 images contrôlées en ligne, 11 sont conformes.
- Le catalogue a été **assaini** : doublons, cadran à verbatim Rolex et fiches incohérentes archivés ; la promesse fausse « tous les cadrans sont stériles » a été corrigée sans qu'on le demande.
- Un **pack de 7 politiques légales** est prêt à coller (le brief n'en demandait que 3), avec ses bloquants listés. Rien n'a été écrit sur Shopify : la permission manquante a été respectée.

## Ce qui ne va pas — par ordre de gravité

1. **60 brouillons sur 95 portent encore 1 091 photos AliExpress brutes** (39 n'ont que ça, 13 sont mixtes) : aucun d'eux ne peut être activé. Ce n'est pas une régression, c'est l'état d'origine — mais c'est désormais chiffré fiche par fiche. → **T-07**
2. **12 fiches actives restent sous la cible** : dix montres à 4/5 (les six `quarante-et-un` de coloris et `trente-neuf-{rouge, vert, bleu, rose}`) et deux accessoires à 2/3 (`coffret-douze-presentation`, `remontoir-vitrine`, dont le visuel de situation a été détaché). Il faut produire, aucun visuel maison conforme ne comble l'écart. → **T-14**
3. **Le guichet de date affiche « 42 »** sur toute la famille Quarante-et-Un — les composites `c-495698-*` de la fiche mère (25/07) et les visuels des fiches enfants (12/08). Défaut de fidélité, pas un interdit ; laissé en ligne pour ne pas recréer la régression. → **T-15**
4. **207 doublons morts** dans la médiathèque, issus du lot des 11-12/08. → **T-18**
5. **Deux fiches importées avec des handles AliExpress bruts**, non rattachées à la collection `cadran-arabe`. → **T-04**
6. **La collection cadran arabe reste sous-peuplée** : le mot-clé porte 15 500 recherches/mois et le re-sourcing s'est arrêté à 3 cadrans sur les 4 à 8 visés. → **T-05**
7. `alt` génériques sur `cadran-sterile-lumineux-28-5`. → **T-08**
8. Manques antérieurs au 12/08 : `remontoir-solo` 2/3, `bracelet-fkm-tropical` 1/3. → **T-09**

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

### Côté brouillons — audité le 13/08, aucun dégât de contenu

La même session a retiré **311 médias sur 35 brouillons**, mais ici la règle défaillante est tombée
sur des galeries **entièrement** composées de photos DSers : **les 311 retraits sont des photos
AliExpress brutes, 0 visuel maison**. En échange, **146 visuels maison** ont été posés et les 35
fiches couvrent toutes leurs apparences sans photo brute. **Rien n'a eu à être réparé.**

Le dégât est de **méthode** : les **311 retraits sont passés par `fileDelete`** — les 311 GID
interrogés répondent `null`, aucun n'est ré-attachable. Ces sources fournisseur ne manquaient à aucune
galerie, mais elles servaient de matière première de composition. **T-23 les a toutes re-téléchargées
le 13/08 par l'API AliExpress** : **311 sur 311**, plus 11 images de variantes, sur les 35 fiches, et
les 35 identifiants fournisseur sont désormais confirmés et consignés dans
`journal/data/table-correspondance-handle-aliexpress.csv`. Détail :
`journal/2026-08-13-recuperation-sources-api.md`.
Les 9 brouillons antérieurs au 08/08 n'ont **rien perdu**. Détail :
`journal/2026-08-13-audit-reparation-brouillons.md`.

## Écarts de méthode constatés (corrigés depuis, à ne pas répéter)

Codex a **supprimé 78 photos fournisseur** et **déplacé un visuel maison en position 1** sur 17 brouillons, alors que le brief interdisait les deux. Exécution propre (URLs sauvegardées, ciblage strict, rollback possible) et dans le sens de l'objectif — mais hors mandat. Aucune fiche **active** n'a été dégradée les 10-11/08 ; la régression du point 1 vient de la session du 12/08.

**361 fichiers étaient restés hors GitHub** jusqu'au 12/08 au soir. Rappel : la source de vérité est GitHub, pas le disque.

# Maison Noirmont — état courant

**Dernière vérification : 13/08/2026, soir** (après l'audit des 95 brouillons — `journal/2026-08-13-audit-reparation-brouillons.md` —, la recherche de mots-clés — `journal/2026-08-13-recherche-mots-cles.md` — et l'audit GMC — `journal/2026-08-13-conformite-et-textes.md`).
Ce fichier dit ce qui **est**, pas ce qu'il faut faire. Pour agir : [`TABLEAU.md`](TABLEAU.md).

## Chiffres

| | |
|---|---|
| Catalogue | **201 produits** — 96 actifs · 95 brouillons · 10 archivés |
| Évolution depuis le 09/08 | 199 → 201 : 10 archivages (3 doublons, le cadran Rolex, une montre arabe mixte, 3 brouillons stériles, 2 fiches incohérentes) et +2 cadrans arabes importés le 11/08 |
| Thème | **`TRAVAIL Noirmont — publier apres validation` (`205089014098`) est le thème publié** depuis le 09/08 ; `Maison Noirmont` et `Helio` sont dépubliés. Les correctifs du 08/08 sont donc bien en ligne — sections d'avis et badge « 4,8/5 » vérifiés `disabled: true` le 13/08 |
| Statut public | **boutique sous mot de passe** — rien n'est visible, aucun risque public actif |
| Collections | 10 créées le 09/08, **aucune publiée** sur le canal Online Store — **arborescence invalidée le 13/08 par T-21**, 4 des 10 ne portent aucun volume mesurable |
| Merchant Center | **non créé** — volontaire, tant que le CSS n'est pas arrêté |
| SKU | **2 065 variantes sur 3 009 portent encore un SKU AliExpress brut** — 84 brouillons et 9 archivés, dont 95 contenant « no logo ». Les 96 fiches actives sont propres (`NOIR-<trigramme>-<n°>`) |
| Consentement cookies | **absent** — ni bandeau `#shopify-pc__banner`, ni `Shopify.customerPrivacy`, ni cookie `_tracking_consent` (requête anonyme du 13/08) |
| Politiques légales | les 7 sont en ligne, datées du 10/08 et cohérentes entre elles — **sauf l'article 15 des CGV, qui porte toujours `[[MEDIATEUR_NOM]]`** |
| `alt` des médias | 2 080 médias : **860 visuels maison, tous pourvus d'un `alt` FR descriptif** · 1 220 `alt` vides, tous sur des photos AliExpress brutes de brouillons (remplacées par T-07) |
| Meta-descriptions | **96 fiches actives sur 96** en ont une (16 écrites le 13/08, avec les 12 meta titles manquants) |
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
5. **L'arborescence des collections ne repose sur rien de mesuré** (établi le 13/08, T-21). `cadran pilote` et `cadran stérile` : **volume non restitué par SEMrush**. `cadran arabe` : **20/mois**. `cadran squelette` : **20/mois**. Les têtes réelles sont les organes en français simple — `cadran de montre` 480, `boitier montre` 1 600, `mouvement nh35` 590, `verre saphir montre` 480, `outil horloger` 390. Et **84 titres produit sur 94 ne contiennent pas le mot « montre »**. → **T-24**, **T-25**
   *Corrige un chiffre faux qui circulait ici : le « 15 500 pour cadran arabe » n'a jamais été le volume de cette expression en France. La grappe arabe existe, mais côté **montre finie** (`seiko arabic dial` 8 100, `seiko chiffre arabe` 390, `montre arabe` 320), pas côté cadran-pièce.*
6. **2 065 SKU AliExpress bruts** sur 84 brouillons et 9 archivés : le défaut P0 de l'audit GMC est revenu par les 94 fiches importées le 09/08, qui n'ont jamais été renommées. Le SKU part au flux Shopping et sort déjà dans le JSON-LD. Bloque l'activation. → **T-32**
7. **Aucun mécanisme de consentement cookies**, contrairement à ce qui était affirmé ailleurs. La politique cookies, qui prétendait le contraire, a été corrigée le 13/08 pour dire l'état réel — elle redeviendra fausse dès la pose de la balise Google. → **T-33**, à faire **avant** T-10
8. **Le médiateur de la consommation n'est toujours pas nommé** : `[[MEDIATEUR_NOM]]` est servi dans l'article 15 des CGV. T-H2 avait été coché « fait » à tort. → **T-H2 rouvert**
9. **Compte à rebours actif sur `/password`**, aucun `tel:` au pied de page, aucune mention « TTC » : tout est dans le thème **publié**, que le connecteur ne peut pas écrire. → **T-34**
10. **9 fichiers image partagés entre deux fiches actives** (composites mère/enfant), interdits par la checklist GMC — mais les retirer recréerait la régression que T-01 vient de réparer. → **T-36**
11. Manques antérieurs au 12/08 : `remontoir-solo` 2/3, `bracelet-fkm-tropical` 1/3. → **T-09**

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

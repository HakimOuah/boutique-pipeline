# Maison Noirmont — état courant

**Dernière vérification : 14/08/2026, nuit** (après l'application de la grille de prix — `journal/2026-08-14-application-grille-prix.md`, scan complet des 3 009 variantes — et le dossier consentement cookies + médiateur — `journal/2026-08-14-consentement-cookies.md`). Vérifications antérieures du 13/08 : audit des 95 brouillons, recherche de mots-clés, audit GMC.
Ce fichier dit ce qui **est**, pas ce qu'il faut faire. Pour agir : [`TABLEAU.md`](TABLEAU.md).

## Chiffres

| | |
|---|---|
| Catalogue | **201 produits** — 96 actifs · 95 brouillons · 10 archivés |
| Évolution depuis le 09/08 | 199 → 201 : 10 archivages (3 doublons, le cadran Rolex, une montre arabe mixte, 3 brouillons stériles, 2 fiches incohérentes) et +2 cadrans arabes importés le 11/08 |
| Thème | **`TRAVAIL Noirmont — publier apres validation` (`205089014098`) est le thème publié** depuis le 09/08 ; `Maison Noirmont` et `Helio` sont dépubliés. Les correctifs du 08/08 sont donc bien en ligne — sections d'avis et badge « 4,8/5 » vérifiés `disabled: true` le 13/08 |
| Statut public | **boutique sous mot de passe** — rien n'est visible, aucun risque public actif |
| Collections | 10 créées le 09/08, **aucune publiée** sur le canal Online Store — **arborescence invalidée le 13/08 par T-21**, 4 des 10 ne portent aucun volume mesurable |
| **Prix** | ✅ **la grille de prix est appliquée depuis le 14/08 au soir** — 585 variantes réécrites sur 65 des 96 fiches actives, 0 écart au contrôle. Montres : **239 à 419 €** (contre 279-429 € avant). Squelette 279 €, chronographes 239 €, Trente-six 239-259 €, Trente-neuf 279-329 €, Sport chic 279-299 €, Intégrale 329 €, **GMT inchangé à 349-417 €**. Accessoires recalés sur leurs bandes. Sauvegarde : `backups/2026-08-14-prix/avant.jsonl` |
| **Prix barrés** | **0 sur les 96 fiches actives** ✅ (purge du 08/08 tenue, vérifiée le 14/08) — mais ⛔ **1 926 sur 86 brouillons et 148 sur les 10 archivées** : la purge n'a jamais couvert les fiches non actives. → **T-50** |
| Merchant Center | **non créé** — volontaire, tant que le CSS n'est pas arrêté |
| SKU | **2 065 variantes sur 3 009 portent encore un SKU AliExpress brut** — 84 brouillons et 9 archivés, dont 95 contenant « no logo ». Les 96 fiches actives sont propres (`NOIR-<trigramme>-<n°>`) |
| Consentement cookies | **conforme aujourd'hui** (aucun traceur soumis à consentement n'est déposé) et **mécanisme très probablement déjà activé** : politique FR `1563598881106` **non-`SD-`** en `consentRequired: true`, `storefront-banner.js` injecté, API de consentement fonctionnelle (`shouldShowBanner() = true`, région `FRIDF`). **Non vérifiable de l'extérieur tant que le mot de passe est en place** : l'API Storefront répond `Online Store channel is locked.` et le bandeau échoue sur `Missing access token`. Reste 2 clics à Hakim : lire l'interrupteur, et **élargir la région au-delà de la France seule** (14/08) |
| Politiques légales | les 7 sont en ligne, datées du 10/08 et cohérentes entre elles — **sauf l'article 15 des CGV, qui porte toujours `[[MEDIATEUR_NOM]]`** |
| `alt` des médias | 2 080 médias : **860 visuels maison, tous pourvus d'un `alt` FR descriptif** · 1 220 `alt` vides, tous sur des photos AliExpress brutes de brouillons (remplacées par T-07) |
| Meta-descriptions | **96 fiches actives sur 96** en ont une (16 écrites le 13/08, avec les 12 meta titles manquants) |
| Mesure d'achat | **absente** (ni GA4 ni gtag) — bloquant avant toute dépense publicitaire |
| Visuels des 95 brouillons | 1 420 médias — **329 maison / 1 091 photos AliExpress brutes** · 43 fiches 100 % maison, 13 mixtes, 39 encore entièrement brutes |

## Ce qui va bien

- **La grille de prix arbitrée par Hakim est appliquée** (14/08) : 585 variantes, 0 `userErrors`, 0 écart entre le prix attendu et le prix relu, contrôlé par un scan complet des 3 009 variantes plus une contre-vérification paginée par curseur. Les trois cas sensibles ont tenu : **GMT non touché**, **Intégrale à 329 € et pas à leur comparable** (qui est sous notre coût), **remontoirs bois laissés en l'état** faute de coût connu.
- Les **interdits structurants ont tenu** sur la période 10-14/08 : aucun brouillon activé, aucune collection publiée, aucun statut modifié, aucun `compareAtPrice` réintroduit sur les fiches actives.
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
7. **Consentement cookies — le dossier est retourné le 14/08.** Ce n'est pas le mécanisme qui manque (il est très probablement déjà là), c'est **la région d'application** : seule la France est en « consentement requis », les 250+ autres pays sont à `false`. Le jour où la balise Google sera posée, **un visiteur belge ou allemand serait mesuré sans consentement** — `shipsToCountries = ["FR"]` limite les acheteurs, pas les visiteurs. Rien n'est activable par API (le schéma Admin n'expose que `privacyFeaturesDisable`, aucune mutation d'activation). La politique cookies, que le 13/08 avait corrigée en y mettant l'affirmation fausse **symétrique** (« aucun bandeau n'est affiché »), a été réécrite le 14/08 dans une forme vraie quel que soit l'état du bandeau. → **T-33** (2 clics), à faire **avant** T-10
8. **Médiateur : les marqueurs sont partis, mais son site manque.** Vérifié le 14/08 sur les CGV servies (`updatedAt 14/08 23:46`) : ✅ plus aucun `[[…]]`, l'article 15 nomme **CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14**. ⛔ Mais `[[MEDIATEUR_SITE]]` a été **supprimé au lieu d'être remplacé** : aucune adresse de site internet, alors que l'**article R. 616-1** l'impose. Restent aussi un `<meta charset="utf-8">` collé au milieu du paragraphe et une date de version périmée (« 10 août » pour un document modifié le 14). **Aucun autre marqueur à trou nulle part** — 7 politiques et 6 pages CMS publiées balayées. → **T-H2**, 3 corrections dans le même paragraphe
9. **Compte à rebours actif sur `/password`**, aucun `tel:` au pied de page, aucune mention « TTC » : tout est dans le thème **publié**, que le connecteur ne peut pas écrire. → **T-34**
10. **9 fichiers image partagés entre deux fiches actives** (composites mère/enfant), interdits par la checklist GMC — mais les retirer recréerait la régression que T-01 vient de réparer. → **T-36**
11. Manques antérieurs au 12/08 : `remontoir-solo` 2/3, `bracelet-fkm-tropical` 1/3. → **T-09**
12. **2 074 prix barrés dorment sur les fiches non actives** (1 926 sur 86 brouillons, 148 sur les 10 archivées) — découvert le 14/08 au scan de contrôle de la grille de prix. La purge du 08/08 n'avait couvert que les 96 actives. C'est le **motif de refus n°1 de Merchant Center**, et il s'activera avec le premier brouillon publié. Bloque l'activation au même titre que les photos brutes et les SKU AliExpress. → **T-50**

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

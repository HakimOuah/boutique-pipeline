# Maison Noirmont — état courant

**Dernière vérification : 15/08/2026** — **premier audit du site LIVE, en visiteur anonyme**, après le retrait du mot de passe (`journal/2026-08-15-audit-conformite-site-live.md`). Vérifications antérieures : grille de prix et consentement cookies le 14/08, audit des 95 brouillons et audit GMC le 13/08.
Ce fichier dit ce qui **est**, pas ce qu'il faut faire. Pour agir : [`TABLEAU.md`](TABLEAU.md).

## Chiffres

| | |
|---|---|
| Catalogue | **201 produits** — 96 actifs · 95 brouillons · 10 archivés |
| Évolution depuis le 09/08 | 199 → 201 : 10 archivages (3 doublons, le cadran Rolex, une montre arabe mixte, 3 brouillons stériles, 2 fiches incohérentes) et +2 cadrans arabes importés le 11/08 |
| Thème | **`TRAVAIL Noirmont — publier apres validation` (`205089014098`) est le thème publié** depuis le 09/08 ; `Maison Noirmont` et `Helio` sont dépubliés. Les correctifs du 08/08 sont donc bien en ligne — sections d'avis et badge « 4,8/5 » vérifiés `disabled: true` le 13/08 |
| Statut public | ✅ **BOUTIQUE PUBLIQUE depuis le 15/08** — `maisonnoirmont.fr` répond 200, plus de `/password`. **Tout défaut est désormais réel et observable.** 96 produits publics, 14 collections publiques ; les 95 brouillons et 10 archivées **ne sont pas servis** (vérifié : les 10 collections de pièces répondent 404) |
| Collections | **14 publiques** + 10 de pièces non publiées (404). ⚠️ **3 publiques sont sous le seuil de 5 produits** et liées au menu : `frontpage` **1**, `montre-squelette` **2**, `plongeuses` **3** *(les compteurs Admin — 5/2/5 — incluent les brouillons ; seul `/collections/<h>/products.json` dit ce qu'un visiteur voit)*. **Arborescence toujours invalidée par T-21** |
| Moyens de paiement | Réellement actifs (`/payments/config`, source publique) : **Shop Pay, PayPal, Apple Pay**, cartes Visa / Mastercard / Amex / Maestro. ⛔ **`googlePayConfig: null`** alors que le picto Google Pay est rendu au pied de page. ⛔ **Klarna : 0 occurrence** alors que les 96 fiches annoncent « Ou 4 × X € avec PayPal **ou Klarna** » |
| Frais de livraison | ✅ **une seule offre, gratuite** — `/cart/shipping_rates.json` avec panier réel + adresse 75002 : « Livraison offerte — suivie », `0.00 €`, « comptez 2 à 3 semaines ». Cohérent avec la politique d'expédition, la FAQ et le bandeau d'accueil. Rien n'est découvert à la caisse |
| **Prix** | ✅ **la grille de prix est appliquée depuis le 14/08 au soir** — 585 variantes réécrites sur 65 des 96 fiches actives, 0 écart au contrôle. Montres : **239 à 419 €** (contre 279-429 € avant). Squelette 279 €, chronographes 239 €, Trente-six 239-259 €, Trente-neuf 279-329 €, Sport chic 279-299 €, Intégrale 329 €, **GMT inchangé à 349-417 €**. Accessoires recalés sur leurs bandes. Sauvegarde : `backups/2026-08-14-prix/avant.jsonl` |
| **Prix barrés** | **0 sur les 883 variantes publiques** ✅ (revérifié en anonyme le 15/08 : aucun prix barré visible nulle part, page comme panier). Le thème porte un emplacement `compare-at-price-wrap` et un badge « Économie » **vides et masqués par CSS** — gabarit dormant qui **s'allumera seul** au premier `compareAtPrice` écrit. ⛔ **1 926 sur 86 brouillons et 148 sur les 10 archivées** : la purge n'a jamais couvert les fiches non actives. → **T-50** |
| Merchant Center | **non créé** — volontaire, tant que le CSS n'est pas arrêté |
| SKU | **2 065 variantes sur 3 009 portent encore un SKU AliExpress brut** — 84 brouillons et 9 archivés, dont 95 contenant « no logo ». Les 96 fiches actives sont propres (`NOIR-<trigramme>-<n°>`) |
| Consentement cookies | ✅ **PROUVÉ CONFORME le 15/08, en anonyme.** Le bandeau `#shopify-pc__banner` s'affiche dès la première page. **« Accepter » et « Refuser » sont strictement identiques** : 258 × 37 px chacun, même fond, même bordure `1px rgb(31,31,31)`, même couleur, même `font-size: 16px`, même graisse — le refus n'est pas caché derrière « Gérer vos préférences ». `getRegulation() = "GDPR"`, `isRegulationEnforced() = true`. Avant tout choix : `analyticsProcessingAllowed = false`, `marketingAllowed = false`, **3 cookies seulement** (`localization`, `cart_currency`, `_shopify_essential`). Clic sur **Refuser** → bandeau parti, **aucun** `_ga*`/`_gcl*`/`_fbp`, aucun script Google/Meta/TikTok. Le lien « Préférences en matière de cookies » **ouvre le panneau sans changer de page** (le 404 sur `/policies/` collé à la main est le comportement Shopify normal, pas un lien mort). ⚠️ **Seul point ouvert : la région**, invérifiable de l'extérieur (déduite de l'IP ; `privacySettings` refusé faute de `read_privacy_settings`). À élargir à **EEE + UK avant T-10**, pas avant l'ouverture GMC |
| Politiques légales | les 7 sont servies, cohérentes entre elles, **0 marqueur `[[…]]` nulle part**, **0 `<meta charset>` dans le corps**. ⛔ **Art. 15 des CGV : CM2C nommé avec adresse et téléphone, mais SANS adresse de site internet** — l'art. R. 616-1 l'impose. ⛔ **Deux « Mentions légales » servies en parallèle** : `/policies/legal-notice` (10/08, 5 sections) et `/pages/mentions-legales` (13/08, 6 sections, plus complète), les deux liées au pied de page. ⚠️ dates de version hétérogènes (10/08, 13/08, 15/08) |
| Fuite d'e-mail | ⛔ **`shop.email` = `shop.contactEmail` = `contact.noirmont@gmail.com`**, injecté dans le JSON-LD `Organization` de **toutes les pages** (`"email": "contact.noirmont@gmail.com"`). Le reste du site publie `contact@maisonnoirmont.fr` (57 occurrences). La politique de confidentialité est propre — seule la donnée structurée fuit. → **T-H4** |
| `alt` des médias | 2 080 médias : **860 visuels maison, tous pourvus d'un `alt` FR descriptif** · 1 220 `alt` vides, tous sur des photos AliExpress brutes de brouillons (remplacées par T-07) |
| Meta-descriptions | **96 fiches actives sur 96** en ont une (16 écrites le 13/08, avec les 12 meta titles manquants) |
| Mesure d'achat | **absente** (ni GA4 ni gtag) — bloquant avant toute dépense publicitaire |
| Visuels des 95 brouillons | 1 420 médias — **329 maison / 1 091 photos AliExpress brutes** · 43 fiches 100 % maison, 13 mixtes, 39 encore entièrement brutes |

## Ce qui va bien

- **Le site public tient l'audit** (15/08, en visiteur anonyme). Sur la checklist fusionnée : **0 prix
  barré** sur 883 variantes · **0 faux avis, 0 note, 0 badge** (aucun `aggregateRating` ni `review` dans
  le JSON-LD, aucune app d'avis) · **0 photo AliExpress brute** (521/521 images sur le CDN Shopify) ·
  **0 compteur de rareté, 0 compte à rebours, 0 badge promo, 0 « X clients satisfaits »** ·
  **0 lien mort** sur les 34 liens de l'accueil · **879/883 SKU** au format maison · **31/31 mentions
  d'étanchéité qualifiées « annoncée »** · **0 verbatim de marque suisse** (Rolex, Swiss Made,
  Superlative, Omega, Tudor…) · prix identique en fiche, en JSON-LD et au panier sur 8/8 fiches.
- **Le consentement cookies est réglé** — le dossier qui valait trois verdicts contradictoires est clos,
  et il est bon (voir le tableau ci-dessus). C'était le dernier bloquant technique supposé.
- **Les mentions obligatoires sont complètes** : raison sociale, forme, capital, SIREN, SIRET, RCS, TVA,
  adresse, téléphone, directeur de publication, hébergeur, rétractation 14 jours, garanties légales FR,
  CNIL. La **politique de confidentialité** porte désormais bases légales, durées de conservation et CNIL.
  La **page contact** est exemplaire (adresse, `tel:` cliquable, horaires, délai de réponse, mention RGPD).
- **La grille de prix arbitrée par Hakim est appliquée** (14/08) : 585 variantes, 0 `userErrors`, 0 écart entre le prix attendu et le prix relu, contrôlé par un scan complet des 3 009 variantes plus une contre-vérification paginée par curseur. Les trois cas sensibles ont tenu : **GMT non touché**, **Intégrale à 329 € et pas à leur comparable** (qui est sous notre coût), **remontoirs bois laissés en l'état** faute de coût connu.
- Les **interdits structurants ont tenu** sur la période 10-14/08 : aucun brouillon activé, aucune collection publiée, aucun statut modifié, aucun `compareAtPrice` réintroduit sur les fiches actives.
- **~85 visuels maison rattachés** le 10/08, tous en fin de galerie sur les fiches actives, `alt` FR, 2048×2048. Sur 12 images contrôlées en ligne, 11 sont conformes.
- Le catalogue a été **assaini** : doublons, cadran à verbatim Rolex et fiches incohérentes archivés ; la promesse fausse « tous les cadrans sont stériles » a été corrigée sans qu'on le demande.
- Un **pack de 7 politiques légales** est prêt à coller (le brief n'en demandait que 3), avec ses bloquants listés. Rien n'a été écrit sur Shopify : la permission manquante a été respectée.

## Ce qui ne va pas — par ordre de gravité

> **Depuis le 15/08, la ligne de partage a changé** : ce qui est **public** est réel et vu par
> n'importe qui ; ce qui dort sur les brouillons ne l'est pas encore. Les six points ci-dessous sont
> **publics**. Détail et corrections exactes : `journal/2026-08-15-audit-conformite-site-live.md`.

0. **Les 6 bloquants publics de l'audit du 15/08** — aucun n'est à ma main :
   1. ⛔ **Un second e-mail publié sur chaque page** : `contact.noirmont@gmail.com` dans le JSON-LD
      `Organization`. → **T-H4** (Hakim, réglages).
   2. ⛔ **Moyen de paiement inexistant annoncé sur 96 fiches** : « Ou 4 × X € avec PayPal **ou Klarna** »
      alors que Klarna n'est pas activé (`/payments/config` : 0 occurrence). → **T-34** (thème publié).
   3. ⛔ **Picto Google Pay au pied de page** alors que `googlePayConfig: null`. → **T-34**.
   4. ⛔ **Aucune mention « TTC »** — 0 occurrence sur l'accueil, les fiches, le panier et le pied de
      page. Les prix *sont* TTC (`taxesIncluded = true`), c'est la mention qui manque (art. L. 112-1). → **T-34**.
   5. ⛔ **Art. 15 des CGV : médiateur sans URL de site** (art. R. 616-1). → **T-H2**.
   6. ⛔ **Deux « Mentions légales » servies en parallèle**, dates et contenus différents. → **T-H2**.

0bis. **Quatre contradictions promesse ↔ réalité** — plus dangereuses qu'une absence :
   - **Garantie** : le pied de page promet « Mouvement, **couronne, aiguilles** » alors que la politique
     §7 se limite au « mouvement interne » et exclut bracelet, verre et boîtier. → **T-34**.
   - **Configurateur** : l'accueil annonce « une **pièce unique, à votre image** » quand la FAQ dit
     correctement que rien n'est fabriqué sur mesure. → **T-34**.
   - ✅ **Collection Plongeuses** : quatre affirmations fausses (« six modèles », céramique, bronze,
     « Miyota 8215 ou PT5000 », « d'autres montent bien plus haut ») pour 3 produits acier NH35 5 ATM —
     **corrigé le 15/08**.
   - ✅ **Politique de cookies** : bandeau décrit au conditionnel et `storefront_digest` présenté comme
     déposé « tant que la boutique est protégée par un mot de passe » — **corrigé le 15/08**.

0ter. **Vocabulaire de marque tierce dans les titres, désormais public** : `Bracelet Présidentiel — doré`,
   `Bracelet Présidentiel — acier inoxydable`, `Voyageur Or — GMT bracelet Président`, `Bracelet Jubilé
   acier — 20 mm`, `Bracelet Jubilé — embouts courbes`, « jubilé » dans 15 descriptions, et le **tag
   `skx`** sur les 3 `heritage-*`. « Président / Présidentiel » est un nom de bracelet Rolex, `skx` une
   référence Seiko — les deux partent au flux Shopping. → **C15 / T-35**.

1. **60 brouillons sur 95 portent encore 1 091 photos AliExpress brutes** (39 n'ont que ça, 13 sont mixtes) : aucun d'eux ne peut être activé. Ce n'est pas une régression, c'est l'état d'origine — mais c'est désormais chiffré fiche par fiche. → **T-07**
2. **12 fiches actives restent sous la cible** : dix montres à 4/5 (les six `quarante-et-un` de coloris et `trente-neuf-{rouge, vert, bleu, rose}`) et deux accessoires à 2/3 (`coffret-douze-presentation`, `remontoir-vitrine`, dont le visuel de situation a été détaché). Il faut produire, aucun visuel maison conforme ne comble l'écart. → **T-14**
3. **Le guichet de date affiche « 42 »** sur toute la famille Quarante-et-Un — les composites `c-495698-*` de la fiche mère (25/07) et les visuels des fiches enfants (12/08). Défaut de fidélité, pas un interdit ; laissé en ligne pour ne pas recréer la régression. → **T-15**
4. **207 doublons morts** dans la médiathèque, issus du lot des 11-12/08. → **T-18**
5. **L'arborescence des collections ne repose sur rien de mesuré** (établi le 13/08, T-21). `cadran pilote` et `cadran stérile` : **volume non restitué par SEMrush**. `cadran arabe` : **20/mois**. `cadran squelette` : **20/mois**. Les têtes réelles sont les organes en français simple — `cadran de montre` 480, `boitier montre` 1 600, `mouvement nh35` 590, `verre saphir montre` 480, `outil horloger` 390. Et **84 titres produit sur 94 ne contiennent pas le mot « montre »**. → **T-24**, **T-25**
   *Corrige un chiffre faux qui circulait ici : le « 15 500 pour cadran arabe » n'a jamais été le volume de cette expression en France. La grappe arabe existe, mais côté **montre finie** (`seiko arabic dial` 8 100, `seiko chiffre arabe` 390, `montre arabe` 320), pas côté cadran-pièce.*
6. **2 065 SKU AliExpress bruts** sur 84 brouillons et 9 archivés : le défaut P0 de l'audit GMC est revenu par les 94 fiches importées le 09/08, qui n'ont jamais été renommées. Le SKU part au flux Shopping et sort déjà dans le JSON-LD. Bloque l'activation. → **T-32**
7. **Consentement cookies — SOLDÉ sur le mécanisme le 15/08** (bandeau affiché, boutons de même niveau prouvés au pixel, aucun traceur avant choix, refus fonctionnel, lien de retrait fonctionnel). **Ne reste que la région d'application** : seule la France est en « consentement requis », les 250+ autres pays sont à `false`, et **c'est invérifiable de l'extérieur** (la région vient de l'IP ; `privacySettings` refusé faute de `read_privacy_settings`, re-testé le 15/08). Le jour où la balise Google sera posée, **un visiteur belge ou allemand serait mesuré sans consentement** — `shipsToCountries = ["FR"]` limite les acheteurs, pas les visiteurs. Rien n'est activable par API. → **T-33 §2**, à faire **avant T-10**, pas avant l'ouverture GMC
8. **Médiateur : les marqueurs sont partis, mais son site manque.** Reconfirmé le 15/08 sur les CGV **publiquement servies** : ✅ plus aucun `[[…]]` nulle part (7 politiques + 6 pages CMS balayées), ✅ **le `<meta charset>` parasite a disparu** du corps. L'article 15 nomme **CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14**. ⛔ Mais **aucune adresse de site internet**, alors que l'**article R. 616-1** l'impose, et la date de version reste « 10 août » pour un document modifié le 14. → **T-H2**, 2 corrections dans le même paragraphe
9. **Correctifs du thème publié** — le connecteur ne peut pas les écrire. Le compte à rebours de `/password` est **sans objet** (la page n'existe plus). Restent : aucun `tel:` au pied de page (il n'existe que sur `/pages/contact`), aucune mention « TTC », le picto **Google Pay** fantôme, le « **ou Klarna** » fantôme, la promesse de garantie trop large, le « pièce unique, à votre image » du bloc configurateur, et les valeurs dormantes `rating: 4.5` / `review_count: 123` que le bloc `disabled` conserve intactes. → **T-34**
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

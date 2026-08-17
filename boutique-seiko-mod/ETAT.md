# Maison Noirmont — état courant

**Dernière vérification : 17/08/2026 ~15h25** — Boutique **Maison Noirmont** uniquement. 🧊 **Storefront gelé** (décision Hakim) : pas de GMC, pas d'écriture live, pas d'activation, jusqu'après les 30 jours Tuftéo. ✅ T-37 / T-64 / T-H2 / T-61 (storefront propre, **PAS PRÊT à créer le GMC**). Thème publié = `205451100498`. **N'activer aucun des 20.**

**Vérifications antérieures** : audit GMC Terry 17/08 (`journal/2026-08-17-audit-gmc-terry.md`) ; repasse conformité n°2 le 15/08 midi ; audit live 15/08 matin ; grille de prix et cookies 14/08 ; audit brouillons et GMC 13/08.
**Repeuplement 15/08** : 20 fiches DSers en DRAFT. Visuels + textes faits le 17/08. ⛔ 2 coffrets aluminium non créés → T-60. ⛔ 4 fiches Unmapped DSers → T-59.

Ce fichier dit ce qui **est**, pas ce qu'il faut faire. Pour agir : [`TABLEAU.md`](TABLEAU.md), et pour Hakim : [`A-FAIRE-HAKIM.md`](A-FAIRE-HAKIM.md).

## Chiffres

| | |
|---|---|
| Catalogue | **221 produits** — 96 actifs · **115 brouillons** · 10 archivés (dont 20 fiches de repeuplement, toutes encore DRAFT) |
| Évolution depuis le 09/08 | 199 → 201 : 10 archivages (3 doublons, le cadran Rolex, une montre arabe mixte, 3 brouillons stériles, 2 fiches incohérentes) et +2 cadrans arabes importés le 11/08 |
| Thème | **`TRAVAIL 15-08 — correctifs` (`205451100498`) est le thème publié** (MAIN). L'ancien `205089014098` « Noirmont » est dépublié. Vérifié live le 17/08 : `Shopify.theme.id = 205451100498`. |
| Statut public | ✅ **BOUTIQUE PUBLIQUE depuis le 15/08** — `maisonnoirmont.fr` répond 200, plus de `/password`. **Tout défaut est désormais réel et observable.** 96 produits publics, 14 collections publiques ; les 95 brouillons et 10 archivées **ne sont pas servis** (vérifié : les 10 collections de pièces répondent 404) |
| Collections | **14 publiques** + 10 de pièces non publiées (404). ⚠️ **3 publiques sont sous le seuil de 5 produits** et liées au menu : `frontpage` **1**, `montre-squelette` **2**, `plongeuses` **3** *(les compteurs Admin — 5/2/5 — incluent les brouillons ; seul `/collections/<h>/products.json` dit ce qu'un visiteur voit)*. ✅ **Décision Hakim 17/08 : on les garde** (menu et publication inchangés). **Arborescence toujours invalidée par T-21** |
| Moyens de paiement | Réellement actifs (17/08) : **Shop Pay, PayPal, Apple Pay, Klarna**, cartes Visa / Mastercard / Amex / Maestro. Shopify Payments actif. ✅ Picto **Google Pay absent** (`googlePayConfig: null`) — plus un mensonge, case optionnelle **T-53**. ✅ Bandeau fiches : **« Paiement sécurisé »**, 0 « 4 fois » (**T-52 soldé**). Bloc dynamique « plusieurs fois » + seuil 30 € : absent à 12,90 €, présent à 279 €. |
| Frais de livraison | ✅ **une seule offre, gratuite** — `/cart/shipping_rates.json` avec panier réel + adresse 75002 : « Livraison offerte — suivie », `0.00 €`, « comptez 2 à 3 semaines ». Cohérent avec la politique d'expédition, la FAQ et le bandeau d'accueil. Rien n'est découvert à la caisse |
| **Prix** | ✅ **la grille de prix est appliquée depuis le 14/08 au soir** — 585 variantes réécrites sur 65 des 96 fiches actives. ✅ **T-60 (17/08)** : `coffret-douze-aluminium` 24 emplacements **109 €** (6 = 69,90 · 12 = 84,90). Montres : **239 à 419 €**. Squelette 279 €, chronographes 239 €, Trente-six 239-259 €, Trente-neuf 279-329 €, Sport chic 279-299 €, Intégrale 329 €, **GMT inchangé à 349-417 €**. Sauvegarde T-60 : `backups/2026-08-17-t60-coffret-24/` |
| **Prix barrés** | ✅ **0 sur les 3 009 variantes de la boutique** — actives, brouillons et archivées comprises. **T-50 soldé le 15/08** : les 2 074 `compareAtPrice` dormants (1 926 sur 86 brouillons, 148 sur les 10 archivées) ont été remis à `null` en 96 mutations aliasées, 0 `userErrors`, après sauvegarde des 2 074 valeurs d'origine (`backups/2026-08-15-prix-barres/avant.jsonl`). Preuve : **scan paginé complet des 3 009 variantes**, plus une contre-vérification par curseur. Aucun `price` touché (0 écart sur les 3 009), aucun statut modifié. ⚠️ Le thème porte toujours un emplacement `compare-at-price-wrap` et un badge « Économie » **vides et masqués par CSS** — gabarit dormant qui **s'allumerait seul** au premier `compareAtPrice` réécrit, même sur un brouillon |
| Merchant Center | **non créé** — volontaire (Tuftéo 30 jours d'abord). Audit Terry 17/08 : **PAS PRÊT à créer**. Domaine AFNIC créé **2026-07-24** (24 j). Les 6 contradictions publiques du 15/08 sont soldées. Red flags restants : 3 collections < 5 (gardées), Présidentiel, T-36. |
| SKU | ✅ **3 025 / 3 029 au format `NOIR-<TRI>-<nnn>`** — T-32 soldé le 17/08. **0** `:` / `#` / « no logo ». **4 vides** = carte cadeau uniquement. Scan paginé complet, statuts inchangés (883 / 1 998 / 148). Correspondance : `backups/2026-08-17-sku-t32/` |
| Consentement cookies | ✅ **PROUVÉ CONFORME le 15/08, en anonyme.** Le bandeau `#shopify-pc__banner` s'affiche dès la première page. **« Accepter » et « Refuser » sont strictement identiques** : 258 × 37 px chacun, même fond, même bordure `1px rgb(31,31,31)`, même couleur, même `font-size: 16px`, même graisse — le refus n'est pas caché derrière « Gérer vos préférences ». `getRegulation() = "GDPR"`, `isRegulationEnforced() = true`. Avant tout choix : `analyticsProcessingAllowed = false`, `marketingAllowed = false`, **3 cookies seulement** (`localization`, `cart_currency`, `_shopify_essential`). Clic sur **Refuser** → bandeau parti, **aucun** `_ga*`/`_gcl*`/`_fbp`, aucun script Google/Meta/TikTok. Le lien « Préférences en matière de cookies » **ouvre le panneau sans changer de page** (le 404 sur `/policies/` collé à la main est le comportement Shopify normal, pas un lien mort). ⚠️ **Seul point ouvert : la région**, invérifiable de l'extérieur (déduite de l'IP ; `privacySettings` refusé faute de `read_privacy_settings`). À élargir à **EEE + UK avant T-10**, pas avant l'ouverture GMC |
| Politiques légales | les 7 sont servies, cohérentes, **0 `[[…]]`**. ✅ Médiateur CM2C + URL. ✅ Dates : **15 août 2026** sur les 6 politiques datées (T-H2, 17/08, live). |
| Pages CMS | **5 publiées** : `contact`, `la-maison`, `faq`, `configurateur`, `politique-de-cookies`. **6 dépubliées**, dont `mentions-legales` depuis le 15/08 au soir. ✅ **Aucun doublon parmi les pages publiées** (passe complète du 15/08 : `politique-de-cookies` n'a pas d'équivalent en politique Shopify, et `/pages/contact` n'est pas un doublon de `/policies/contact-information`) |
| Redirections 301 | **8** : 7 héritées du renommage produits/collections + `/pages/mentions-legales` → `/policies/legal-notice` (`UrlRedirect/1745946280274`, 15/08) |
| Fuite d'e-mail | ✅ **`shop.email` = `contact@maisonnoirmont.fr`** dans le JSON-LD `Organization` live (17/08). 0 Gmail. |
| `alt` des médias | 2 080 médias : **860 visuels maison, tous pourvus d'un `alt` FR descriptif** · 1 220 `alt` vides, tous sur des photos AliExpress brutes de brouillons (remplacées par T-07) |
| Meta-descriptions | **96 fiches actives sur 96** en ont une (16 écrites le 13/08, avec les 12 meta titles manquants) |
| Mesure d'achat | **absente** (ni GA4 ni gtag) — bloquant avant toute dépense publicitaire |
| Visuels des 115 brouillons | Inventaire live 17/08 : **1 086 photos AliExpress / 442 maison** · 69 house_only, 5 mixed, 41 ali_only. Depuis : 2 mixed nettoyés, puis `cadran-texture-paon-29-sans-logo` passé en mixed (9 maison + 1 brute). CSV du 13/08 périmé |

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
  **Remesuré le 15/08 à midi** : bandeau présent, « Accepter » et « Refuser » **196 × 37 px l'un et
  l'autre**, mêmes fond, couleur, taille et graisse, aucun soulignement ni sur l'un ni sur l'autre ;
  **2 cookies seulement** avant tout choix (`localization`, `cart_currency`) ; `gtag`, `dataLayer`,
  `fbq`, `ttq` tous absents ; **un seul script tiers**, `shop.app/checkouts/internal/preloads.js`,
  qui est de l'infrastructure Shopify et non un traceur.
- **Aucune trace de facturation en dollars** (15/08) : `/payments/config` → `"currency":"EUR"`,
  `Shopify.currency = {"active":"EUR"}`, `priceCurrency: "EUR"` dans tous les JSON-LD produit,
  et **0 occurrence de `USD`, de `$` ou de « dollar »** sur l'accueil, le panier et les fiches.
- **Le bloc de paiement fractionné dynamique fonctionne comme prévu** (15/08) : « Paiement en plusieurs
  fois avec **Klarna et PayPal** », logos tirés de `shop.enabled_payment_types` donc auto-correctifs, et
  **le seuil de 30 € est mesuré et opérant** — 0 occurrence sur `barrettes-de-rechange-270` à 12,90 €,
  bloc présent et visible à 279 € et 378 €.
- **Performance** : TTFB 50 à 130 ms, page complète en 0,31 à 0,60 s sur l'accueil, une fiche et une
  collection. **0 lien mort** sur les 48 liens internes de l'accueil, **13 collections du méga-menu en
  200**, sitemap complet, HSTS, CSP, `X-Frame-Options: DENY`, aucun `noindex` sur les politiques,
  aucun code de vérification Google résiduel.
- **Les `alt` sont bons** : 50 fiches contrôlées une par une le 15/08, tous descriptifs, en français,
  nommant le modèle, la vue et le détail. Aucun générique, aucun vide.
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
> n'importe qui ; ce qui dort sur les brouillons ne l'est pas encore. Les points ci-dessous sont
> **publics**, relevés à midi en visiteur anonyme.
> Détail : `journal/2026-08-17-audit-gmc-terry.md` (passe Terry) et `journal/2026-08-15-repasse-conformite-2.md` (15/08).

0. **Les 6 défauts publics du 15/08 midi — ✅ SOLDÉS EN LIVE le 17/08 (T-61).** Délai **48 h**
   partout · footer **OH Ventures + 47 rue Vivienne + `tel:+33756828094`** · garantie limitée au
   **mouvement** · bandeau **« Paiement sécurisé »** (0 « 4 fois ») · JSON-LD `Organization`
   **valide** avec `legalName`. Détail : `journal/2026-08-17-audit-gmc-terry.md`.
   ⚠️ Restent, hors ces 6 : 3 collections < 5 **gardées** · Présidentiel (arbitrage A) · T-36
   images partagées · « Qualité Premium » (arbitrage C). ✅ Dates de politiques : **15/08** (T-H2).

0bis. **Les 6 bloquants du 15/08 au matin : 5 soldés, vérifiés en anonyme.**
   ✅ **E-mail** : `shop.email` = `shop.contactEmail` = `contact@maisonnoirmont.fr`, **0 `gmail`**
   nulle part · ✅ **Klarna** : la mention fausse a disparu, **et Klarna est maintenant réellement
   actif en caisse** (`shop.enabled_payment_types` le contient ; `/payments/config` ne le montre pas
   parce que cet endpoint n'expose que les portefeuilles accélérés) · ✅ **Google Pay** : le picto a
   disparu, les 7 icônes rendues sont exactement les moyens acceptés, **Amex apparaît enfin** ·
   ✅ **TTC** : sous le prix **et** au pied de page, donc accueil, panier et collections couverts ·
   ✅ **Médiateur** : `https://www.cm2c.net/` à l'art. 15 des CGV, et `<meta charset>` retiré ·
   ✅ **Mentions légales** : une seule version, 6 sections, datée du 15/08, 301 confirmée 3 fois sur 3.
   ✅ **Devise** : **0 occurrence de `USD`, de `$` ou de « dollar »** sur tout le parcours, `EUR`
   partout — la facturation en dollars est réparée.
   ✅ **Contradictions promesse ↔ réalité** : « pièce unique, à votre image » a disparu de l'accueil au
   profit du texte de la FAQ ; la collection Plongeuses et la politique de cookies avaient été
   corrigées la veille.

0ter. **Vocabulaire de marque tierce — moitié soldée le 15/08.** ✅ Le **tag `skx`** est retiré des
   3 fiches `heritage-*`. ⛔ Restent `Bracelet Présidentiel — doré`, `Bracelet Présidentiel — acier
   inoxydable`, `Voyageur Or — GMT bracelet Président`, plus une quinzaine de descriptions et des
   `alt` : « Président / Présidentiel » est un nom de bracelet déposé par Rolex, et le catalogue part
   au flux Shopping. **Non exécuté volontairement** : renommer touche des titres SEO arbitrés le 13/08,
   c'est un arbitrage de positionnement, pas une correction. Proposition « bracelet à maillons
   arrondis » posée dans `A-FAIRE-HAKIM.md`. « Jubilé » et « panda » se défendent comme descripteurs
   de forme. → **C15 / T-35**.

1. **Les brouillons hors des 20 habillés portent encore des photos AliExpress brutes** (inventaire live 17/08 : 41 ali_only, quelques mixed). T-07 **entamé** : `cadran-texture-paon-29-sans-logo` a 9 visuels maison, 1 brute restante. Aucun de ces brouillons ne peut être activé. → **T-07**
2. **12 fiches actives restent sous la cible** : dix montres à 4/5 (les six `quarante-et-un` de coloris et `trente-neuf-{rouge, vert, bleu, rose}`) et deux accessoires à 2/3 (`coffret-douze-presentation`, `remontoir-vitrine`, dont le visuel de situation a été détaché). Il faut produire, aucun visuel maison conforme ne comble l'écart. → **T-14**
3. **Le guichet de date affiche « 42 »** sur toute la famille Quarante-et-Un — les composites `c-495698-*` de la fiche mère (25/07) et les visuels des fiches enfants (12/08). Défaut de fidélité, pas un interdit ; laissé en ligne pour ne pas recréer la régression. → **T-15**
4. **207 doublons morts** dans la médiathèque, issus du lot des 11-12/08. → **T-18**
5. **L'arborescence des collections ne repose sur rien de mesuré** (établi le 13/08, T-21). `cadran pilote` et `cadran stérile` : **volume non restitué par SEMrush**. `cadran arabe` : **20/mois**. `cadran squelette` : **20/mois**. Les têtes réelles sont les organes en français simple — `cadran de montre` 480, `boitier montre` 1 600, `mouvement nh35` 590, `verre saphir montre` 480, `outil horloger` 390. Et **84 titres produit sur 94 ne contiennent pas le mot « montre »**. → **T-24**, **T-25**
   *Corrige un chiffre faux qui circulait ici : le « 15 500 pour cadran arabe » n'a jamais été le volume de cette expression en France. La grappe arabe existe, mais côté **montre finie** (`seiko arabic dial` 8 100, `seiko chiffre arabe` 390, `montre arabe` 320), pas côté cadran-pièce.*
6. ✅ ~~**2 065 SKU AliExpress bruts**~~ — **T-32 soldé le 17/08.** 0 SKU `:` / `#` / « no logo » sur 3 029 variantes.
7. **Consentement cookies — SOLDÉ sur le mécanisme le 15/08** (bandeau affiché, boutons de même niveau prouvés au pixel, aucun traceur avant choix, refus fonctionnel, lien de retrait fonctionnel). **Ne reste que la région d'application** : seule la France est en « consentement requis », les 250+ autres pays sont à `false`, et **c'est invérifiable de l'extérieur** (la région vient de l'IP ; `privacySettings` refusé faute de `read_privacy_settings`, re-testé le 15/08). Le jour où la balise Google sera posée, **un visiteur belge ou allemand serait mesuré sans consentement** — `shipsToCountries = ["FR"]` limite les acheteurs, pas les visiteurs. Rien n'est activable par API. → **T-33 §2**, à faire **avant T-10**, pas avant l'ouverture GMC
8. ✅ **Médiateur : SOLDÉ sur le fond le 15/08.** L'article 15 des CGV publiquement servies nomme désormais **CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14, site internet : https://www.cm2c.net/** (art. R. 616-1 satisfait), et le **`<meta charset>` parasite a disparu** : passe complète sur les 7 politiques et les 5 pages CMS publiées, **0 `<meta charset>` dans un corps de document**. ⛔ Reste **la date de version**, toujours « 10 août 2026 » sur les CGV, les CGU, l'expédition, le remboursement et la confidentialité, alors qu'au moins les CGV ont été modifiées le 15. → **T-H2**
9. **Correctifs du thème publié** — ✅ **soldés en live le 17/08** (T-34 points 6-10, T-52). Restent les **dormants** `disabled: true` : badge **« 4,8/5 · 1340 avis »**, `rating: 4.5` / `review_count: 123`, **12 témoignages**, **Lorem ipsum** du guide des tailles. → **T-34** (dormants seulement)
10. **9 fichiers image partagés entre deux fiches actives** (composites mère/enfant), interdits par la checklist GMC — mais les retirer recréerait la régression que T-01 vient de réparer. → **T-36**
11. Manques antérieurs au 12/08 : `remontoir-solo` 2/3, `bracelet-fkm-tropical` 1/3. → **T-09**
12. ✅ ~~**2 074 prix barrés dorment sur les fiches non actives**~~ — **SOLDÉ le 15/08 (T-50)**. Les 1 926 des 86 brouillons et les 148 des 10 archivées sont à `null`, prouvé par un scan paginé des 3 009 variantes. Reste des deux verrous d'activation : **T-32** (SKU) et **T-07** (photos brutes). Détail : `journal/2026-08-15-purge-prix-barres.md`

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

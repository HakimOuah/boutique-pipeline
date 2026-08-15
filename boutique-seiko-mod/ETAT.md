# Maison Noirmont — état courant

**Dernière vérification : 15/08/2026 (midi)** — **repasse de conformité n°2** après la série de corrections de Hakim, en visiteur anonyme (`journal/2026-08-15-repasse-conformite-2.md`). **Verdict : toujours PAS PRÊT pour Merchant Center, mais il ne reste que 20 minutes de travail.** 7 des 8 actions de Hakim sont faites et vérifiées, **5 des 6 bloquants publics du matin sont soldés**. Il reste **6 défauts**, dont **3 contradictions du site avec lui-même** : ① délai de réponse **24 h contre 48 h** dans le même pied de page, sur toutes les pages, et deux fois de plus sur chaque fiche ② garantie **« mouvement, couronne, aiguilles »** contre le contrat, trois fois par fiche ③ **« Paiement en 4 fois »** dans le bandeau contre « en plusieurs fois » du bloc, y compris sur les fiches à 12,90 €. Plus : ④ **le pied de page n'a ni adresse postale ni raison sociale** ⑤ **le JSON-LD `Organization` est du JSON invalide**, donc ignoré par Google ⑥ 3 collections publiques sous 5 produits. **Un seul de ces défauts demande de toucher au code** (`blocks/noirmont-confiance.liquid`).
**Vérifications antérieures** : premier audit du site LIVE le 15/08 au matin (`journal/2026-08-15-audit-conformite-site-live.md`), grille de prix et consentement cookies le 14/08, audit des 95 brouillons et audit GMC le 13/08.
**Corrections du 15/08 au soir** (`journal/2026-08-15-corrections-post-ouverture.md`) : doublon de mentions légales soldé côté connecteur, moyens de paiement réels établis sur `/payments/config`, et les 6 défauts de thème localisés au réglage près.
**Purge du 15/08** (`journal/2026-08-15-purge-prix-barres.md`) : **T-50 soldé — 2 074 prix barrés dormants remis à `null` sur 86 brouillons et 10 archivées**, prouvé par un scan paginé des 3 009 variantes.
**Corrections du connecteur le 15/08 à midi** : description de `carte-cadeau-maison-noirmont` (« 24 h ouvrées » → « 48 h ouvrées », le seul texte **produit** qui portait encore l'ancien délai) et **tag `skx` retiré** des 3 fiches Héritage (référence de modèle Seiko, publique, destinée au flux Shopping). Sauvegardes : `backups/2026-08-15-repasse-2/`.

Ce fichier dit ce qui **est**, pas ce qu'il faut faire. Pour agir : [`TABLEAU.md`](TABLEAU.md), et pour Hakim : [`A-FAIRE-HAKIM.md`](A-FAIRE-HAKIM.md).

## Chiffres

| | |
|---|---|
| Catalogue | **201 produits** — 96 actifs · 95 brouillons · 10 archivés |
| Évolution depuis le 09/08 | 199 → 201 : 10 archivages (3 doublons, le cadran Rolex, une montre arabe mixte, 3 brouillons stériles, 2 fiches incohérentes) et +2 cadrans arabes importés le 11/08 |
| Thème | **`TRAVAIL Noirmont — publier apres validation` (`205089014098`) est le thème publié** depuis le 09/08 ; `Maison Noirmont` et `Helio` sont dépubliés. Les correctifs du 08/08 sont donc bien en ligne — sections d'avis et badge « 4,8/5 » vérifiés `disabled: true` le 13/08 |
| Statut public | ✅ **BOUTIQUE PUBLIQUE depuis le 15/08** — `maisonnoirmont.fr` répond 200, plus de `/password`. **Tout défaut est désormais réel et observable.** 96 produits publics, 14 collections publiques ; les 95 brouillons et 10 archivées **ne sont pas servis** (vérifié : les 10 collections de pièces répondent 404) |
| Collections | **14 publiques** + 10 de pièces non publiées (404). ⚠️ **3 publiques sont sous le seuil de 5 produits** et liées au menu : `frontpage` **1**, `montre-squelette` **2**, `plongeuses` **3** *(les compteurs Admin — 5/2/5 — incluent les brouillons ; seul `/collections/<h>/products.json` dit ce qu'un visiteur voit)*. **Arborescence toujours invalidée par T-21** |
| Moyens de paiement | Réellement actifs (`/payments/config`, source publique, relevé le 15/08) : **Shop Pay, PayPal, Apple Pay**, cartes Visa / Mastercard / Amex / Maestro. **Shopify Payments est actif** (`shopifyPaymentsEnabled: true`). ⛔ **`googlePayConfig: null`** alors que le picto Google Pay est rendu sur **toutes** les pages → mais c'est **une case à cocher dans Shopify Payments, effet immédiat** : on active, on ne retire pas (**T-53**). ⛔ **`offsiteConfigs: null` — aucun prestataire de paiement fractionné n'est installé**. ✅ « Klarna » a **disparu de tout le site** (0 occurrence sur 6 fiches + accueil + panier + collections + FAQ), ⛔ mais le **bandeau défilant des fiches promet toujours « Paiement en 4 fois »** (`marquee_pdp` → `iwt_pdp5`) → **T-52**. Klarna et le 4× PayPal demandent une **candidature et la validation d'un fournisseur** — délai non maîtrisé, acceptation non acquise à 0 vente |
| Frais de livraison | ✅ **une seule offre, gratuite** — `/cart/shipping_rates.json` avec panier réel + adresse 75002 : « Livraison offerte — suivie », `0.00 €`, « comptez 2 à 3 semaines ». Cohérent avec la politique d'expédition, la FAQ et le bandeau d'accueil. Rien n'est découvert à la caisse |
| **Prix** | ✅ **la grille de prix est appliquée depuis le 14/08 au soir** — 585 variantes réécrites sur 65 des 96 fiches actives, 0 écart au contrôle. Montres : **239 à 419 €** (contre 279-429 € avant). Squelette 279 €, chronographes 239 €, Trente-six 239-259 €, Trente-neuf 279-329 €, Sport chic 279-299 €, Intégrale 329 €, **GMT inchangé à 349-417 €**. Accessoires recalés sur leurs bandes. Sauvegarde : `backups/2026-08-14-prix/avant.jsonl` |
| **Prix barrés** | ✅ **0 sur les 3 009 variantes de la boutique** — actives, brouillons et archivées comprises. **T-50 soldé le 15/08** : les 2 074 `compareAtPrice` dormants (1 926 sur 86 brouillons, 148 sur les 10 archivées) ont été remis à `null` en 96 mutations aliasées, 0 `userErrors`, après sauvegarde des 2 074 valeurs d'origine (`backups/2026-08-15-prix-barres/avant.jsonl`). Preuve : **scan paginé complet des 3 009 variantes**, plus une contre-vérification par curseur. Aucun `price` touché (0 écart sur les 3 009), aucun statut modifié. ⚠️ Le thème porte toujours un emplacement `compare-at-price-wrap` et un badge « Économie » **vides et masqués par CSS** — gabarit dormant qui **s'allumerait seul** au premier `compareAtPrice` réécrit, même sur un brouillon |
| Merchant Center | **non créé** — volontaire, tant que le CSS n'est pas arrêté |
| SKU | **2 065 variantes sur 3 009 portent encore un SKU AliExpress brut** — 84 brouillons et 9 archivés, dont 95 contenant « no logo ». Les 96 fiches actives sont propres (`NOIR-<trigramme>-<n°>`) |
| Consentement cookies | ✅ **PROUVÉ CONFORME le 15/08, en anonyme.** Le bandeau `#shopify-pc__banner` s'affiche dès la première page. **« Accepter » et « Refuser » sont strictement identiques** : 258 × 37 px chacun, même fond, même bordure `1px rgb(31,31,31)`, même couleur, même `font-size: 16px`, même graisse — le refus n'est pas caché derrière « Gérer vos préférences ». `getRegulation() = "GDPR"`, `isRegulationEnforced() = true`. Avant tout choix : `analyticsProcessingAllowed = false`, `marketingAllowed = false`, **3 cookies seulement** (`localization`, `cart_currency`, `_shopify_essential`). Clic sur **Refuser** → bandeau parti, **aucun** `_ga*`/`_gcl*`/`_fbp`, aucun script Google/Meta/TikTok. Le lien « Préférences en matière de cookies » **ouvre le panneau sans changer de page** (le 404 sur `/policies/` collé à la main est le comportement Shopify normal, pas un lien mort). ⚠️ **Seul point ouvert : la région**, invérifiable de l'extérieur (déduite de l'IP ; `privacySettings` refusé faute de `read_privacy_settings`). À élargir à **EEE + UK avant T-10**, pas avant l'ouverture GMC |
| Politiques légales | les 7 sont servies, cohérentes entre elles, **0 marqueur `[[…]]` nulle part**. ⛔ **Art. 15 des CGV : CM2C nommé avec adresse et téléphone, mais SANS adresse de site internet** — l'art. R. 616-1 l'impose. ⛔ **`<meta charset="utf-8">` toujours présent dans le corps de l'article 15 des CGV** (relevé le 15/08 au soir sur `shopPolicies.body` ; le constat « 0 `<meta charset>` » du matin portait sur le rendu HTML, où le navigateur l'absorbe). ✅ **Une seule « Mentions légales » servie depuis le 15/08 au soir** : `/policies/legal-notice`, la page CMS concurrente est dépubliée et redirigée en 301. ⛔ Mais la politique conservée porte encore la version du **10/08** (5 sections, sans DPO, sans CNIL, sans droit applicable) : texte complet prêt à coller dans `livraisons/mentions-legales-a-coller-2026-08-15.html`. ⚠️ dates de version hétérogènes (10/08, 15/08) |
| Pages CMS | **5 publiées** : `contact`, `la-maison`, `faq`, `configurateur`, `politique-de-cookies`. **6 dépubliées**, dont `mentions-legales` depuis le 15/08 au soir. ✅ **Aucun doublon parmi les pages publiées** (passe complète du 15/08 : `politique-de-cookies` n'a pas d'équivalent en politique Shopify, et `/pages/contact` n'est pas un doublon de `/policies/contact-information`) |
| Redirections 301 | **8** : 7 héritées du renommage produits/collections + `/pages/mentions-legales` → `/policies/legal-notice` (`UrlRedirect/1745946280274`, 15/08) |
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
> Détail et corrections exactes : `journal/2026-08-15-repasse-conformite-2.md`.

0. **Les 6 défauts publics restants au 15/08 midi** — aucun n'est à ma main :
   1. ⛔ **Le pied de page se contredit sur le délai de réponse.** Bloc « Une question ? » :
      *« généralement sous **24 h** ouvrées »*. Bloc du logo, deux lignes plus bas :
      *« Nous répondons sous **48h** »*. Sur **toutes** les pages.
      (`sections/footer-group.json` → `custom_section_k6mNHc` → 4e groupe `group_x7TjnR` →
      `text_wDwwwK`). → **T-34**.
   2. ⛔ **Le même écart deux fois de plus sur chacune des 96 fiches** : cartes de confiance sous le
      prix (`blocks/noirmont-confiance.liquid`, **codé en dur**) et accordéon « Contactez-nous »
      (`templates/product.json` → `accordions_KKUaHK/accordion_contact`). Le bloc « Besoin d'aide ? »
      de la même page dit bien 48 h. → **T-34**.
   3. ⛔ **Le pied de page n'a ni adresse postale ni raison sociale** : **0 occurrence** de
      `OH Ventures`, `47 rue Vivienne` ou `75002`, alors que la checklist Terry impose
      *« Footer = GMC exactement (email, téléphone, adresse) »*. Le téléphone y est en texte brut
      non cliquable (`0756828094`), soit une **troisième** écriture du même numéro. → **T-35**.
   4. ⛔ **La garantie promise dépasse toujours le contrat sur les fiches** : « mouvement, **couronne,
      aiguilles** » **trois fois par fiche** (une en dur dans `noirmont-confiance.liquid`, deux dans
      des accordéons), contre la politique de remboursement §7 et l'art. 10 des CGV limités au
      **mouvement interne**. Le pied de page, lui, a bien été corrigé. → **T-34**.
   5. ⛔ **« Paiement en 4 fois »** dans le bandeau des fiches (`marquee_pdp` → **`iwt_pdp5`**, 5e
      élément), **y compris sur les fiches à 12,90 €** où le nouveau bloc dynamique se masque tout
      seul, et alors que ce bloc dit prudemment « en plusieurs fois ». → **T-52**.
   6. ⛔ **Le JSON-LD `Organization` de l'accueil est du JSON invalide** — virgule orpheline après
      `"logo"`, parce que `shop.phone` est vide et qu'aucun réseau social n'est renseigné. **Google
      ignore le bloc entier**, donc l'adresse et l'e-mail qu'il porte, alors qu'ils sont justes depuis
      ce matin. **Remplir le champ téléphone de la fiche adresse règle les deux problèmes.** → **T-35**.

   *Et deux écarts mineurs* : ⚠️ cinq politiques annoncent « Version en vigueur au 10 août 2026 »
   alors qu'au moins les CGV ont été modifiées le 15 (**T-H2**) · ⚠️ trois collections publiques sous
   le seuil de 5 produits, dont deux dans le méga-menu : `frontpage` **1**, `montre-squelette` **2**,
   `plongeuses` **3** (**T-35**).

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

1. **60 brouillons sur 95 portent encore 1 091 photos AliExpress brutes** (39 n'ont que ça, 13 sont mixtes) : aucun d'eux ne peut être activé. Ce n'est pas une régression, c'est l'état d'origine — mais c'est désormais chiffré fiche par fiche. → **T-07**
2. **12 fiches actives restent sous la cible** : dix montres à 4/5 (les six `quarante-et-un` de coloris et `trente-neuf-{rouge, vert, bleu, rose}`) et deux accessoires à 2/3 (`coffret-douze-presentation`, `remontoir-vitrine`, dont le visuel de situation a été détaché). Il faut produire, aucun visuel maison conforme ne comble l'écart. → **T-14**
3. **Le guichet de date affiche « 42 »** sur toute la famille Quarante-et-Un — les composites `c-495698-*` de la fiche mère (25/07) et les visuels des fiches enfants (12/08). Défaut de fidélité, pas un interdit ; laissé en ligne pour ne pas recréer la régression. → **T-15**
4. **207 doublons morts** dans la médiathèque, issus du lot des 11-12/08. → **T-18**
5. **L'arborescence des collections ne repose sur rien de mesuré** (établi le 13/08, T-21). `cadran pilote` et `cadran stérile` : **volume non restitué par SEMrush**. `cadran arabe` : **20/mois**. `cadran squelette` : **20/mois**. Les têtes réelles sont les organes en français simple — `cadran de montre` 480, `boitier montre` 1 600, `mouvement nh35` 590, `verre saphir montre` 480, `outil horloger` 390. Et **84 titres produit sur 94 ne contiennent pas le mot « montre »**. → **T-24**, **T-25**
   *Corrige un chiffre faux qui circulait ici : le « 15 500 pour cadran arabe » n'a jamais été le volume de cette expression en France. La grappe arabe existe, mais côté **montre finie** (`seiko arabic dial` 8 100, `seiko chiffre arabe` 390, `montre arabe` 320), pas côté cadran-pièce.*
6. **2 065 SKU AliExpress bruts** sur 84 brouillons et 9 archivés : le défaut P0 de l'audit GMC est revenu par les 94 fiches importées le 09/08, qui n'ont jamais été renommées. Le SKU part au flux Shopping et sort déjà dans le JSON-LD. Bloque l'activation. → **T-32**
7. **Consentement cookies — SOLDÉ sur le mécanisme le 15/08** (bandeau affiché, boutons de même niveau prouvés au pixel, aucun traceur avant choix, refus fonctionnel, lien de retrait fonctionnel). **Ne reste que la région d'application** : seule la France est en « consentement requis », les 250+ autres pays sont à `false`, et **c'est invérifiable de l'extérieur** (la région vient de l'IP ; `privacySettings` refusé faute de `read_privacy_settings`, re-testé le 15/08). Le jour où la balise Google sera posée, **un visiteur belge ou allemand serait mesuré sans consentement** — `shipsToCountries = ["FR"]` limite les acheteurs, pas les visiteurs. Rien n'est activable par API. → **T-33 §2**, à faire **avant T-10**, pas avant l'ouverture GMC
8. ✅ **Médiateur : SOLDÉ sur le fond le 15/08.** L'article 15 des CGV publiquement servies nomme désormais **CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14, site internet : https://www.cm2c.net/** (art. R. 616-1 satisfait), et le **`<meta charset>` parasite a disparu** : passe complète sur les 7 politiques et les 5 pages CMS publiées, **0 `<meta charset>` dans un corps de document**. ⛔ Reste **la date de version**, toujours « 10 août 2026 » sur les CGV, les CGU, l'expédition, le remboursement et la confidentialité, alors qu'au moins les CGV ont été modifiées le 15. → **T-H2**
9. **Correctifs du thème publié** — le connecteur ne peut pas les écrire. ✅ Cinq des cinq points d'origine sont faits (Klarna, Google Pay, TTC, garantie du pied de page, pièce unique) et le compte à rebours de `/password` est sans objet. ⛔ Restent : **« sous 24 h ouvrées »** au pied de page et sur les fiches (deux fois), **« mouvement, couronne, aiguilles »** sur les fiches (trois fois), et **le téléphone au pied de page qui n'est toujours pas un lien `tel:`** — il n'existe qu'en texte brut, et le format national plutôt qu'international. **Deux de ces textes sont codés en dur dans `blocks/noirmont-confiance.liquid`** : c'est le seul point du dossier qui demande d'ouvrir l'éditeur de code. **Dormants**, tous `disabled: true` et non servis, tous à vider un jour : badge **« 4,8/5 · 1340 avis »** (2 emplacements), `rating: 4.5` / `review_count: 123` (4 emplacements), **12 témoignages écrits** (2 sections), et **du `Lorem ipsum`** dans la fenêtre « Guide des tailles ». → **T-34**
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

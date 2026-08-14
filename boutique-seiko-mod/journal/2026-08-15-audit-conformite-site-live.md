# Audit de conformité — site LIVE, en visiteur anonyme

> **15/08/2026.** Premier audit de `maisonnoirmont.fr` **sans mot de passe**. Vérifié en visiteur
> anonyme : `curl` sans cookie de session, plus le navigateur intégré. Aucune commande, aucune donnée
> de paiement, aucun formulaire soumis, aucun brouillon activé, aucun prix modifié.

---

# VERDICT

## ⛔ PAS PRÊT pour l'ouverture d'un compte CSS / Merchant Center.

**Mais le verdict a changé de nature.** Les trois audits contradictoires des 08, 12 et 13/08 mesuraient
la barrière, pas le site. Aujourd'hui tout est observable, et le résultat est **très majoritairement bon** :

- le **consentement cookies est en place et conforme**, prouvé au pixel près — c'était le dernier
  bloquant technique supposé, il est levé ;
- **0 prix barré** sur les 883 variantes publiques, **0 faux avis**, **0 note fabriquée**,
  **0 compteur de rareté**, **0 photo AliExpress brute**, **0 lien mort** ;
- les **7 politiques** sont servies, cohérentes entre elles, sans marqueur à trou.

Ce qui bloque n'est plus une masse de dette : ce sont **six défauts précis, tous publics**, dont
**quatre sont des contradictions entre ce que le site dit et ce qui existe réellement**. C'est
exactement le motif de refus n°1 de Merchant Center — et c'est réparable en une session.

**Trois d'entre eux vivent dans le thème publié**, que le connecteur ne peut pas écrire.
**Deux sont dans les réglages Shopify.** Aucun n'est à ma main.

---

## Les 6 bloquants publics, par ordre d'urgence

| # | Défaut | Preuve | Chez qui |
|---|---|---|---|
| **1** | **Un second e-mail de contact publié sur chaque page** | `shop.email` = `shop.contactEmail` = `contact.noirmont@gmail.com`, injecté dans le JSON-LD `Organization` de **toutes** les pages : `"email": "contact.noirmont@gmail.com"`. Le reste du site publie `contact@maisonnoirmont.fr` (57 occurrences). | **Hakim** — Réglages → Général (T-H4) |
| **2** | **Moyen de paiement inexistant annoncé sur 96 fiches** | Rendu de `/products/*` : `« Ou 4 × €69,75 avec PayPal ou Klarna »`. `/payments/config` : **`klarna` = 0 occurrence**, aucun `installment`, aucun `shopPayInstallments`. PayPal est bien actif (`paypalConfig.merchantId`), **Klarna ne l'est pas**. | **Hakim** — thème publié (T-34) |
| **3** | **Picto Google Pay affiché partout, Google Pay indisponible** | `/payments/config` → **`googlePayConfig: null`**. Le pied de page rend pourtant l'icône `pi-google_pay` sur chaque page. Actifs réels : Shop Pay, PayPal, Apple Pay, cartes Visa / Mastercard / Amex / Maestro. | **Hakim** — thème publié (T-34) |
| **4** | **Aucune mention « TTC » nulle part** | `0` occurrence de `TTC`, `toutes taxes comprises`, `taxes incluses` sur l'accueil, les 8 fiches contrôlées, le panier et le pied de page. Les prix **sont** TTC (`shop.taxesIncluded = true`) — c'est la mention qui manque, et l'art. L. 112-1 du Code de la consommation l'impose. | **Hakim** — thème publié (T-34) |
| **5** | **Article 15 des CGV : médiateur sans adresse de site** | `/policies/terms-of-sale` servi : « CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14. » — **pas d'URL**, alors que l'**art. R. 616-1** impose d'indiquer l'adresse du site internet du médiateur. | **Hakim** — `write_legal_policies` absente (T-H2) |
| **6** | **Deux « Mentions légales » servies en parallèle, avec deux dates** | `/policies/legal-notice` (10/08, 5 sections) **et** `/pages/mentions-legales` (13/08, 6 sections, plus complète : DPO, CNIL, droit applicable). Les **deux** sont liées au pied de page. C'est la moins bonne que Shopify sert dans la caisse et que Merchant Center recopie. | **Hakim** — politiques (T-H2) |

---

## Les 4 contradictions promesse ↔ réalité

Distinctes des bloquants ci-dessus, et plus dangereuses qu'une simple absence : un examinateur qui
lit deux phrases contradictoires conclut que le site n'est pas tenu.

1. **Garantie.** Le pied de page, sur **toutes** les pages : *« Garantie 12 mois — Mouvement, couronne,
   aiguilles : on répare ou on remplace, simplement. »* La politique de remboursement §7 la limite au
   **« mouvement interne »** et **exclut** explicitement « le bracelet, le verre ou le boîtier ». La FAQ
   dit *« 12 mois sur le mouvement »*. Le pied de page promet donc **plus** que le contrat. → thème publié.
2. **Configurateur.** L'accueil affiche *« Composez la vôtre / Vous signez — **une pièce unique, à votre
   image** »*, puis *« Le configurateur ouvre bientôt »*. La FAQ dit l'inverse, correctement :
   *« Le configurateur ne fabrique rien à vos spécifications : il vous montre la référence de notre
   catalogue qui correspond à vos réponses. »* Une allégation de fabrication sur mesure sur un catalogue
   standard rouvre en plus la question de la rétractation (B4). → thème publié.
3. **Collection Plongeuses.** ✅ **Corrigé aujourd'hui** (voir §Corrections). La description annonçait
   *« Nos six modèles vont de l'acier brossé à la céramique, en passant par le bronze »*, *« NH35,
   Miyota 8215 ou PT5000 »* et *« certaines 5 ATM, d'autres montent bien plus haut »*, alors que la page
   publique ne sert que **3 produits**, tous **acier**, tous **NH35**, tous **5 ATM**. Quatre affirmations
   fausses sur une page publique.
4. **Politique de cookies.** ✅ **Corrigée aujourd'hui.** Elle décrivait le bandeau au conditionnel
   (« lorsqu'un tel traceur est activé… un bandeau vous permet ») alors qu'il s'affiche dès la première
   visite, et listait encore `storefront_digest` comme cookie déposé « tant que la boutique est protégée
   par un mot de passe » — faux depuis hier.

---

# CE QUI EST PROUVÉ CONFORME

## Consentement cookies — le dossier est clos, et il est bon

Ce point valait trois verdicts contradictoires. Il est tranché, mesuré en anonyme.

| Contrôle | Résultat |
|---|---|
| Le bandeau s'affiche-t-il ? | ✅ **Oui**, `#shopify-pc__banner`, dès la première page, sur toutes les pages tant qu'aucun choix n'est exprimé |
| Accepter et Refuser de même niveau ? | ✅ **Strictement identiques** — mesuré : `Accepter` **258 × 37 px**, `Refuser` **258 × 37 px**, même `background: rgb(255,255,255)`, même `border: 1px rgb(31,31,31)`, même `color`, même `font-size: 16px`, même `font-weight: 400`, aucun soulignement sur l'un et pas l'autre. Le refus n'est **pas** caché derrière « Gérer vos préférences », qui est un troisième lien distinct. Exigence CNIL satisfaite. |
| L'API de consentement se charge-t-elle ? | ✅ **Oui** — `Shopify.loadFeatures(['consent-tracking-api'])` rend la main **sans erreur**, puis `Shopify.customerPrivacy` est défini. *(Le test « `customerPrivacy === undefined` » reste à bannir : il vaut `undefined` avant `loadFeatures`, y compris sur un site conforme.)* |
| Régulation appliquée | ✅ `getRegulation() = "GDPR"`, `isRegulationEnforced() = true`, `shouldShowGDPRBanner() = true`, consentement granulaire supporté |
| Avant tout choix | ✅ `analyticsProcessingAllowed = false`, `marketingAllowed = false`, `preferencesProcessingAllowed = false`, `currentVisitorConsent = {analytics:"", marketing:"", preferences:"", sale_of_data:""}` |
| Cookies réellement posés avant choix | ✅ **3 seulement**, tous exemptés : `localization`, `cart_currency`, `_shopify_essential` (+ `cart` après ajout au panier) |
| Clic sur **Refuser** | ✅ Le bandeau disparaît, **aucun** `_ga*`, `_gcl*`, `_gid`, `_fbp`, `_ttp` n'apparaît, **aucun** script Google / Meta / TikTok n'est chargé |
| Lien « Préférences en matière de cookies » | ✅ **Fonctionne** — le clic est intercepté, le panneau de préférences s'ouvre **sans changer de page** (`location.href` inchangé). *(Coller `/policies/#shopifyReshowConsentBanner` à la main donne un 404 : c'est le comportement Shopify normal, ce n'est pas un lien mort.)* |
| Traceurs tiers présents | ✅ **Aucun** — 0 `gtag`, 0 `dataLayer`, 0 `google_tag_manager`, 0 pixel |

### ⚠️ Le seul point du consentement qui reste ouvert : la région

**Non vérifiable de l'extérieur, et pour une raison structurelle** : la région du visiteur est déduite
de son IP par le CDN. Depuis la France je mesure `getRegion() = "FRIDF"` et le RGPD appliqué — ce qui
prouve la France, et **rien d'autre**. Côté Admin, la lecture est refusée :
`privacySettings` → *« Access denied. Required access: `read_privacy_settings` »* (re-testé aujourd'hui,
le scope n'a pas été accordé depuis le 14/08).

**Donc l'étape 2 de T-33 reste due, et je ne peux ni la faire ni la constater.** Si la région est
toujours « France seule », un visiteur belge ou allemand ne verra aucun bandeau **le jour où la balise
Google sera posée** — `shipsToCountries = ["FR"]` (vérifié) limite les acheteurs, pas les visiteurs.
Tant qu'aucun traceur n'est posé, le risque est nul ; il devient réel à T-10. **À faire avant T-10, pas avant l'ouverture GMC.**

## Prix

- **0 `compare_at_price`** sur les **883 variantes publiques** — la purge du 08/08 tient, et la grille
  du 14/08 ne l'a pas rouverte. Aucun prix barré visible nulle part.
- Le thème porte bien un emplacement `compare-at-price-wrap` et un badge `Économie`, **tous deux vides
  et masqués par CSS** (`:has(… :empty){display:none}`), avec le libellé « Ancien prix : » en
  `clip-path: inset(50%)`. C'est du gabarit dormant, pas un affichage. **Il s'allumera seul** dès qu'un
  `compareAtPrice` sera écrit — d'où l'urgence de T-50 avant toute activation de brouillon.
- **Grille appliquée = grille affichée** : fourchette publique **12,90 € → 417,00 €**, cohérente avec
  l'arbitrage du 14/08. Prix identique sur la fiche, dans le JSON-LD et au panier sur 8/8 fiches
  contrôlées (ex. `montre-squelette-automatique-carree` : 279 € en fiche, 279 € en `cart.js`).
- **Prix TTC** : `shop.taxesIncluded = true` — les montants affichés **sont** les montants finaux.
  Seule la **mention** manque (bloquant n°4).
- **Frais de livraison accessibles avant paiement** : ✅ `/cart/shipping_rates.json` avec un panier réel
  et une adresse 75002 renvoie **une seule offre — « Livraison offerte — suivie », `price: "0.00"`,
  « Livraison gratuite et suivie en France — comptez 2 à 3 semaines »**. Cohérent avec la politique
  d'expédition (14 à 21 jours), avec la FAQ et avec le bandeau d'accueil. Rien n'est découvert à la caisse.

## Fiches produit

- **96 produits publics**, 883 variantes, 521 images, `vendor = Maison Noirmont` sur 96/96.
- **0 avis fabriqué, 0 note, 0 badge**. Aucun `aggregateRating` ni `review` dans le JSON-LD des 8 fiches
  contrôlées. Aucun bloc d'avis rendu, aucune app d'avis (Judge.me / Loox / Okendo / Trustpilot absentes).
  Les 81 occurrences de `star` sont la liste d'icônes Material Symbols ; les 61 de « avis » sont
  *« 14 jours pour changer d'avis »*. Le bloc `rating-stars` du thème est `"disabled": true` — mais il
  **garde ses valeurs** `rating: 4.5` / `review_count: 123` en dur (dormant, cf. T-34 / D4).
- **0 photo AliExpress brute** : **521/521** images sur `cdn.shopify.com`, nomenclature maison
  (`<handle>-face.jpg`, `<handle>-situation.jpg`). Le seul motif suspect est un faux positif — `ae01`
  dans un UUID Shopify, pas `ae01.alicdn.com`.
- **SKU** : **879/883** au format maison `NOIR-<trigramme>-<n°>`. Les 4 restants sont les variantes de
  `carte-cadeau-maison-noirmont`, dont le SKU est **vide** — à exclure du flux, pas à corriger.
- **Allégations** : 31 mentions d'étanchéité, **31 qualifiées « annoncée »**. Une va plus loin :
  *« le fournisseur annonce 10 bar alors que certains cadrans impriment 200 m : nous retenons la valeur
  la plus prudente »*. 0 « garantie à vie », 0 « certifié », 0 « testé », 0 « 316L », 0 « 904L ».
- **Aucun verbatim de marque suisse** : 0 `Rolex`, `Swiss Made`, `Superlative`, `Officially Certified`,
  `Omega`, `Tudor`, `Oyster`, `Datejust`, `Submariner`, `GMT Master`, `Tandorio`.

## Mentions obligatoires — complètes

`/policies/legal-notice` et `/policies/contact-information` portent : raison sociale **OH Ventures**,
forme (SAS), **capital 1 000 €**, **SIREN 103 157 251**, **SIRET 103 157 251 00010**, **RCS Paris**,
**TVA FR55 103157251**, adresse **47 rue Vivienne, 75002 Paris**, **+33 7 56 82 80 94**,
`contact@maisonnoirmont.fr`, directeur de la publication, hébergeur (Shopify International Limited, Dublin).
Rétractation 14 jours et garanties légales FR : dans les CGV (art. 7, 8) et la politique de remboursement.
**CNIL** : dans la politique de confidentialité §7 et dans `/pages/mentions-legales` §4.
**Médiateur** : art. 15 des CGV — nommé, **URL manquante** (bloquant n°5).
**ODR** : plus aucun renvoi (B6 soldé, conforme au retrait du portail européen).

**Zéro marqueur à trou** sur l'ensemble des 7 politiques et des 6 pages CMS publiées : recherche de
`[[…]]` = **0 occurrence**. **Aucun `<meta charset>` dans le corps** d'aucune politique (le seul
présent est celui du `<head>`) — l'artefact de collage signalé le 14/08 a disparu.
⚠️ **Dates de version non homogènes** : politiques au **10/08**, `/pages/mentions-legales` au **13/08**,
politique de cookies au **15/08**. Sur un document modifié le 14/08 à 23 h 46, l'en-tête « 10 août »
reste faux (T-H2 point 3).

## Politique de confidentialité — désormais complète

Bases légales ✅ (contrat, obligation légale, intérêt légitime, consentement) · durées de conservation
détaillées ✅ (10 ans comptable, 3 ans prospection) · droits RGPD ✅ · **CNIL** ✅ · transferts hors EEE ✅ ·
destinataires ✅ · mineurs ✅. **Et l'adresse Gmail n'y est plus** — le symptôme rendu de A2 est réparé,
seule la fuite par le JSON-LD subsiste.

## Page contact — exemplaire

Raison sociale, adresse postale, e-mail, **téléphone en lien `tel:+33756828094`**, horaires
(« du lundi au vendredi, 9 h – 18 h, heure de Paris »), délai de réponse (24 h ouvrées), bloc
« Informations légales » avec RCS / SIRET / TVA, et **la mention de finalité RGPD** :
*« Les informations que vous nous transmettez servent uniquement à traiter votre demande… »* — A5 et A7 soldés.

⚠️ Le lien `tel:` **n'existe que sur cette page** : **0 occurrence** au pied de page (A3 toujours ouvert, thème).

## Technique

- **0 lien mort** : les 34 liens internes de l'accueil vérifiés un par un, tous en 200 (les 429 d'un
  premier passage étaient de la limitation de débit, re-testés en 200 ; les 3 « 404 » de polices étaient
  un artefact de mon script sur des URL protocole-relatives, vérifiées en 200).
- **Sitemap** servi et complet (produits, pages, collections, blogs). **robots.txt** normal.
- **HTTPS** avec HSTS, `X-Frame-Options: DENY`, CSP `block-all-mixed-content`.
- **Aucun code de vérification GMC résiduel.**
- **Aucun signal commercial faux** : 0 compte à rebours, 0 compteur de stock, 0 « X clients satisfaits »,
  0 badge promo, 0 « 4,8/5 » (les occurrences de `4.8` sont des coordonnées de tracé SVG dans les
  pictos de paiement). Le compte à rebours de `/password` (D5) est **sans objet** : la page n'existe plus.

## Collections

**14 collections publiques**, 10 collections de pièces correctement **non publiées** (404 pour un visiteur).
Aucune ne renvoie un lien mort depuis le menu.

⚠️ **Trois sont sous le seuil de 5 produits** de la checklist, et elles sont **publiques et liées au menu** :

| Collection | Produits publics | État |
|---|---:|---|
| `frontpage` | **1** | à vider ou masquer |
| `montre-squelette` | **2** | dans le méga-menu « Montres » |
| `plongeuses` | **3** | dans le méga-menu **et** dans le bloc « Les collections » de l'accueil |

*(Les compteurs Admin — 5, 2, 5 — incluent les brouillons. Ce qu'un visiteur et un robot voient, c'est 1, 2 et 3.)*

⚠️ **Vocabulaire de marque tierce dans les titres** (C15, toujours ouvert et maintenant public) :
`Bracelet Présidentiel — doré`, `Bracelet Présidentiel — acier inoxydable`, `Voyageur Or — GMT bracelet
Président`, `Bracelet Jubilé acier — 20 mm`, `Bracelet Jubilé — embouts courbes`, plus « jubilé » dans
15 descriptions de montres, et le **tag `skx`** sur les 3 `heritage-*`. « Jubilé » et « panda » se
défendent comme descripteurs de forme ; **« Président / Présidentiel » est un nom de bracelet Rolex** et
**`skx` une référence Seiko** — les deux partent au flux Shopping.

## Parcours d'achat

Ajout au panier ✅ (`/cart/add.js` → 279 €, `compare_at_price: null`) · page panier ✅ (prix juste,
aucun prix barré, total 279 €, liens vers expédition / remboursement / CGV présents) · frais de port
✅ (offre unique gratuite, annoncée) · moyens de paiement ⛔ (bloquants 2 et 3).

⛔ **La page de paiement n'a pas été ouverte** : la navigation vers `/checkout` a été refusée par le
classificateur de sécurité de l'environnement. Je ne l'ai pas contournée. Les moyens de paiement ont
donc été établis par la source faisant autorité — `/payments/config` et l'API Admin
(`supportedDigitalWallets = ["SHOPIFY_PAY","APPLE_PAY"]`) — ce qui est plus fiable qu'une lecture d'écran.
**Aucune commande n'a été passée, aucune donnée de paiement saisie, aucune condition acceptée.**

---

# CE QUE J'AI CORRIGÉ

Deux écrits, tous deux du texte public faux, tous deux par API, tous deux vérifiés relus.

### 1. `/pages/politique-de-cookies` — `pageUpdate`, `userErrors: []`, `updatedAt 2026-08-14T22:15:02Z`

- **Retiré `storefront_digest`** de la liste des cookies déposés : il était décrit comme présent
  « tant que la boutique est protégée par un mot de passe ». Faux depuis le 15/08.
- **Réécrit le paragraphe du bandeau** au présent de l'indicatif, sur ce qui est désormais observable :
  *« Un bandeau de consentement s'affiche dès votre première visite : il vous permet d'accepter ou de
  refuser au moyen de deux boutons de même niveau, présentés côte à côte et de présentation identique… »*
  L'ancienne formulation conditionnelle était devenue trompeuse maintenant que le bandeau est visible.
- Date de version portée au **15 août 2026**.
- ✅ **Vérifié en ligne** : `storefront_digest` absent, `mot de passe` absent, nouveau texte servi.

### 2. Collection `plongeuses` — `collectionUpdate`, `userErrors: []`, `updatedAt 2026-08-14T22:15:37Z`

Quatre affirmations fausses retirées d'une page publique, sans y introduire aucun chiffre
(recommandation C22 : ne plus compter dans une description, ça dérive à chaque ajout) :

| Avant | Réalité publique |
|---|---|
| « Nos **six** modèles » | 3 produits publics |
| « de l'acier brossé à la **céramique**, en passant par le **bronze** » | 3 boîtiers **acier** |
| « NH35, **Miyota 8215** ou **PT5000** » | **NH35** sur les 3 |
| « certaines 5 ATM, **d'autres montent bien plus haut** » | **5 ATM** sur les 3 |

Remplacé par : *« Nos Héritage reprennent ce dessin sur un boîtier de 42 mm en acier, avec un calibre
automatique NH35… l'étanchéité annoncée sur cette famille est de 5 ATM. »* Les avertissements d'usage
(pas de nage, pas de plongée bouteille, lire le chiffre sur la fiche) sont conservés mot pour mot.

✅ **Vérifié** : `/collections/plongeuses.json` sert le nouveau texte (`updated_at 2026-08-15T00:15:37+02:00`).
Le rendu HTML de la page était encore servi depuis le cache CDN à l'heure du rapport ; le gabarit lit
bien `{{ closest.collection.description }}` (vérifié dans `templates/collection.json` du thème publié),
la propagation est donc mécanique.

**Rien d'autre n'a été touché** : aucun produit, aucun prix, aucun statut, aucun média, aucun thème,
aucune politique, aucun réglage, aucune collection publiée ou dépubliée.

---

# CE QUI RESTE — dans l'ordre

## A. Public et urgent — visible aujourd'hui par n'importe qui, examinateur compris

| Ordre | Quoi | Pour | Ticket |
|---:|---|---|---|
| 1 | **Basculer `shop.email` / `shop.contactEmail`** sur `contact@maisonnoirmont.fr`. Vérifier d'abord que la boîte `.fr` reçoit : c'est aussi l'adresse expéditrice des confirmations de commande. | Hakim | **T-H4** |
| 2 | **Retirer « ou Klarna »** du bloc `noirmont-4x` (ou retirer le bloc). PayPal seul est exact — vérifier que « Payer en 4× » est bien actif côté PayPal avant de le laisser. | Hakim | **T-34** |
| 3 | **Retirer le picto Google Pay** du pied de page. Le plus sûr : repasser `force_icons_display` à `false`, le thème rend alors `shop.enabled_payment_types`, donc exactement la caisse, sans entretien. | Hakim | **T-34** |
| 4 | **Ajouter la mention « TTC »** près du prix (fiche, panier, pied de page). Une ligne : « Prix TTC. Livraison offerte en France métropolitaine. » | Hakim | **T-34** |
| 5 | **Aligner la promesse de garantie** du pied de page sur la politique : « Garantie 12 mois sur le mouvement » — retirer « couronne, aiguilles ». | Hakim | **T-34** |
| 6 | **Retirer « une pièce unique, à votre image »** du bloc configurateur de l'accueil, ou le reformuler comme la FAQ (« la référence de notre catalogue qui correspond à vos réponses »). | Hakim | **T-34** |
| 7 | **Ajouter l'URL du médiateur CM2C** à l'article 15 des CGV (recopier depuis l'attestation d'adhésion, ne pas la deviner) + corriger la date de version en « 14 août 2026 ». | Hakim | **T-H2** |
| 8 | **Une seule « Mentions légales »** : recopier le texte du 13/08 dans `/policies/legal-notice`, puis dépublier `/pages/mentions-legales` et repointer le lien du pied de page. | Hakim | **T-H2** |
| 9 | **Ajouter `<a href="tel:+33756828094">` au pied de page.** | Hakim | **T-34** |
| 10 | **Vider `frontpage`** (1 produit) et **dépublier ou peupler `montre-squelette`** (2) et **`plongeuses`** (3) — les trois sont dans le menu. | Hakim + Claude | **T-35** |
| 11 | **Renommer « Présidentiel / Président »** en « bracelet à maillons arrondis » (avec 301) et **retirer le tag `skx`** des 3 `heritage-*`. | Claude | **C15 / T-35** |

## B. Bloque l'activation d'un brouillon — pas public aujourd'hui

Aucun de ces défauts n'est visible : les 95 brouillons et 10 archivées ne sont pas servis (vérifié :
les 10 collections de pièces répondent **404**, `products.json` s'arrête à 96). Ils deviennent publics
**à la seconde** où un brouillon est activé.

| Quoi | Chiffre | Ticket |
|---|---:|---|
| Prix barrés dormants sur les fiches non actives | **2 074** (1 926 sur 86 brouillons, 148 sur 10 archivées) | **T-50** |
| SKU AliExpress bruts | **2 065** sur 84 brouillons et 9 archivées | **T-32** |
| Photos AliExpress brutes | **1 091** sur 60 brouillons | **T-07** |
| Valeurs de note dormantes dans le thème | `rating: 4.5` / `review_count: 123`, bloc `disabled` mais valeurs intactes | **T-34 / D4** |

## C. Bloque la publicité — pas l'ouverture du compte

| Quoi | État | Ticket |
|---|---|---|
| **Mesure d'achat** | **absente** — 0 GA4, 0 gtag, 0 `dataLayer`, 0 `google_tag_manager` (confirmé en anonyme, non ré-instruit). Interdit de dépenser un euro sans elle. | **T-10** |
| **Région du consentement** | **invérifiable de l'extérieur** (IP + scope Admin refusé). Doit être élargie à **EEE + Royaume-Uni** **avant** la pose de la balise Google, pas avant l'ouverture GMC. | **T-33 §2** |
| **Inventaire des cookies** | à mettre à jour **en même temps** que T-10 : ajouter `_ga`, `_ga_<ID>`, `_gcl_au` et retirer « aucun outil de mesure n'est actif ». | **T-33 / T-10** |
| **Carte cadeau** | `carte-cadeau-maison-noirmont` active, 4 SKU vides — à exclure du flux (`product_type = Carte cadeau`). | **T-35** |
| **`identifier_exists: no`** | aucun `gtin` ni `mpn` dans le JSON-LD — normal pour une marque propre, mais à déclarer au flux, et **ne pas** mapper le SKU en `mpn`. | **T-12** |

---

# Notes de méthode

**Trois tests d'audit à retirer définitivement de la grille**, tous invalidés aujourd'hui :

1. `Shopify.customerPrivacy === undefined` ne prouve rien — il **est** `undefined` avant `loadFeatures`,
   sur un site parfaitement conforme. Toujours attendre le rappel de `loadFeatures`.
2. **Compter les produits d'une collection par l'API Admin** donne le total tous statuts confondus.
   Seul `/collections/<handle>/products.json` dit ce qu'un visiteur voit. L'écart est réel :
   5 contre 3 sur `plongeuses`.
3. **Chercher `compare-at`, `Ancien prix`, `star` ou `avis` dans le HTML rendu** produit presque
   uniquement des faux positifs : gabarit dormant masqué par CSS, liste d'icônes Material Symbols,
   « changer d'avis », coordonnées de tracé SVG. Toujours remonter à la donnée (`products.json`,
   JSON-LD, `/payments/config`) plutôt qu'au balisage.

**Une source nouvelle et décisive** : **`/payments/config`** est public et donne, sans authentification,
les moyens de paiement **réellement** actifs (`applePayConfig`, `paypalConfig`, `googlePayConfig: null`,
`dynamicCheckoutPrioritization`). C'est ce qui a permis de trancher les bloquants 2 et 3 sans jamais
ouvrir la caisse. À réutiliser sur toute boutique.

**Limites assumées de cet audit** : la page de paiement n'a pas été ouverte (refus du classificateur,
non contourné) · la région de consentement n'est pas mesurable de l'extérieur · les 8 fiches contrôlées
au rendu sont un échantillon (les 96 l'ont été sur données via `products.json`) · aucun test de vitesse
de page (E8, à passer avant la demande de revue).

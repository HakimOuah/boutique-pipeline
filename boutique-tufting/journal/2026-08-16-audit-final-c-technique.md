---
type: journal
boutique: tufting
date: 2026-08-16
nature: analyse
leviers: [conformite, technique]
titre: "Audit final GMC — Agent C — Technique et rendu réel"
---

# Audit final GMC — Agent C — Technique et rendu réel

**16/08/2026.** Périmètre : thème brouillon `gid://shopify/OnlineStoreTheme/189410738561` de Tuftéo
(tufteo.com), accédé exclusivement par navigateur via `?preview_theme_id=189410738561`. Bandeau
« Draft » vérifié sur chaque page comme preuve qu'on est bien sur le brouillon et non le thème publié.

Méthode : chaque item ci-dessous est vérifié en rechargeant la page réelle et en lisant le résultat à
l'écran (ou en réseau/console), jamais déduit. Verdict PASS / FAIL / NON VÉRIFIÉ + preuve datée.

Rédaction au fil de l'eau — voir avancement au fur et à mesure des sections.

---

## C1 — Rendu (mobile 375×812 puis desktop)

### Accueil — mobile 375×812

**FAIL — bandeau d'annonce (haut de page) : deux messages superposés en permanence, pas de rotation propre.**
Observé 16/08/2026, `https://tufteo.com/?preview_theme_id=189410738561`, bandeau « Draft » confirmé à
l'écran. Deux captures prises à ~5 s d'intervalle montrent le même défaut à l'identique (donc pas une
image de transition attrapée par hasard) : « 🚚 Livraison offerte en France » et
« -10 % sur ta première commande avec le code BIENVENUE10 » s'affichent **simultanément**, coupés aux
deux bords, la flèche de navigation superposée au mot « offerte ».
Cause identifiée en DOM (`javascript_tool`, lecture des styles calculés) : le composant est un slider
Splide (`data-per-page-mobile="1"`, donc censé n'afficher qu'un message à la fois). Son `.splide__track`
et `.splide__list` ont `overflow: visible` (devrait être `hidden`) et le `transform` de la liste ne
décale que de -178 px alors que chaque slide fait 375 px de large — les deux slides (`is-active` et
`is-next`) sont donc **toutes les deux visibles à l'écran** en continu, pas seulement pendant la
transition. Confirmé identiquement avant et après un rechargement complet (cookies/localStorage vidés).
**Correction proposée** : corriger le CSS du slider d'annonce (forcer `overflow: hidden` sur
`.splide__track`/`.splide__list` en mobile, ou revoir le calcul de largeur de slide) dans le fichier
Liquid/CSS du composant `slider-component` / `announcement-bar`.
**Confirmé aussi en desktop** (1280 px, capture après 3 s) : même défaut, « …en France » (coupé à
gauche) superposé à « -10 % sur ta première commande » (coupé à droite) en continu. Le bug n'est donc
pas spécifique au mobile — il touche le composant slider lui-même, sur les deux formats.

**PASS — pas de placeholder résiduel visible.** `get_page_text` sur l'accueil entier (mobile) : aucun
`[promo]`, aucun lorem ipsum, aucun texte de démonstration. Tous les textes (hero, Academy, FAQ, guide
de choix, footer) sont du contenu réel en français.

**NON VÉRIFIÉ — `translation missing`.** Aucune occurrence trouvée dans le texte visible ni dans les
messages de console relevés jusqu'ici, mais je n'ai pas encore parcouru fiche produit / collection /
panier / policies : à confirmer sur chacune avant de clore l'item.

### Fiche produit — `/products/kit-tufting-complet` (mobile 375×812)

**PASS — rendu propre, aucune erreur nouvelle.** 16/08/2026, bandeau Draft confirmé. Galerie 7 images
+ vidéos (mp4 chargées en 206 partiel, normal pour un lecteur vidéo de galerie produit — sans rapport
avec la vidéo hero de l'accueil qui a bien été retirée, voir C7). Accordéons (Caractéristiques,
Description, Livraison, Fabrication, Garantie, Contact) tous fonctionnels au clic. Aucun `[promo]`,
aucun lorem ipsum. Les erreurs console 401/404 observées dans ce chargement se sont révélées être des
messages **résiduels de mon propre test préalable sur `/policies/`** (voir C2), pas des erreurs propres
à cette fiche — confirmé en comparant les timestamps réseau : aucun 404 n'apparaît dans la liste des
requêtes de cette page elle-même.

### Collection — `/collections/machines` (mobile)

**PASS — rendu propre.** 16/08/2026, bandeau Draft confirmé. 4 produits affichés avec vignette, prix,
note (3 des 4 ont une note/nb d'avis, le 4ᵉ « Ciseaux électriques » n'en a aucun — normal, pas un bug).
Aucun placeholder. *(Le seuil de 5 produits par collection, mentionné dans la checklist GMC section 4,
relève du périmètre B5 de l'agent B — je ne le compte pas ici.)*

### Panier autonome — `/cart` (mobile, panier vide)

**PASS — rendu propre.** État vide affiché proprement (« Votre panier est vide », bouton « Continuer les
achats »), boutons de paiement express (Shop, PayPal) et rangée d'icônes (Visa/Mastercard/Apple
Pay/PayPal/Shop/Amex) identiques à la fiche produit et au footer. Aucune superposition, aucun élément
débordant en 375 px.

### Policies — `/policies/privacy-policy` et `/policies/terms-of-sale` (mobile)

**FAIL — titre dupliqué (H1 en double), confirmé sur les 6/6 policies.** 16/08/2026, lecture DOM
(`document.querySelectorAll('h1')`) sur chacune des 6 pages :

| Policy | 1er H1 | 2ᵉ H1 |
|---|---|---|
| `/policies/privacy-policy` | Politique de confidentialité | Politique de confidentialité |
| `/policies/terms-of-sale` | Conditions générales de vente | Conditions générales de vente |
| `/policies/legal-notice` | Mentions légales | Mentions légales |
| `/policies/refund-policy` | Politique de remboursement | Politique de remboursement |
| `/policies/terms-of-service` | Conditions d'utilisation | Conditions générales d'utilisation |
| `/policies/shipping-policy` | Politique d'expédition | Politique de livraison |

Chaque page a **deux balises `<h1>`**, l'une au-dessus de l'autre, avant le premier article. Sur 4 des 6,
le texte est strictement identique (copier-coller visuel qui donne une impression de page buggée). Sur
les 2 dernières (`terms-of-service`, `shipping-policy`), les deux H1 **diffèrent légèrement** — le
premier vient du titre de la policy réglé dans Shopify, le second d'un titre écrit en dur dans le corps
du texte de la policy (« Conditions générales d'utilisation », « Politique de livraison ») : en plus du
doublon de balise, ça révèle que **le nom de la policy affiché en haut de page n'est pas mot pour mot
celui utilisé dans le corps** — point à croiser avec l'agent A (A1, cohérence des chiffres/libellés).
Cause probable : le template `policy` du thème affiche un H1 automatique **en plus** du titre que la
policy elle-même contient déjà en première ligne. **Correction proposée** : dans le template/section
d'affichage des pages policy, ne garder qu'un seul titre — soit le H1 auto-généré par Shopify, soit la
ligne de titre du corps de la policy, pas les deux.

---

**Observation hors-scope (remontée, pas un verdict) :** la photo principale de la fiche est un montage
« contenu du kit à plat » qui a l'apparence d'un visuel fournisseur (fond blanc, style plaquette
AliExpress). Je ne tranche pas la conformité à la règle maison des visuels composés — c'est le
périmètre B3 de l'agent B, je transmets seulement l'observation.

**FAIL — placeholder résiduel critique : les 3 liens réseaux sociaux du footer pointent vers le thème
démo du vendeur, pas vers Tuftéo.** 16/08/2026, confirmé par lecture directe des `href` en DOM (footer,
accueil, thème brouillon `189410738561`) :
- Facebook → `https://www.facebook.com/themefullstack/`
- YouTube → `https://www.youtube.com/@themefullstack`
- LinkedIn → `https://www.linkedin.com/company/themefullstack/`

« themefullstack » est le nom du thème Shopify (Fullstack) utilisé pour construire la boutique, pas une
page Tuftéo. C'est un cas typique du placeholder de démo laissé en place — la définition même de ce que
C1 doit détecter. Un visiteur ou un reviewer GMC qui clique dessus arrive sur les comptes sociaux d'un
tiers sans rapport. **Correction proposée** : dans Réglages > Réseaux sociaux (ou le paramétrage du menu
footer selon comment ces liens sont câblés dans le thème), soit renseigner les vrais comptes Tuftéo,
soit retirer les icônes tant qu'ils n'existent pas — la checklist GMC recommande justement l'absence de
lien plutôt qu'un lien vers une page faible ou hors-sujet, et un lien vers un tiers est pire qu'une
page faible.

---

## C3 — Parcours d'achat

Testé sur `/products/kit-tufting-complet`, mobile 375×812, 16/08/2026. Les clics de l'outil `computer`
étant tombés en timeout de façon répétée sur cette page (« Browser pane is currently hidden », après
plusieurs tentatives), j'ai déclenché les mêmes boutons réels du thème (pas de simulation : lecture du
DOM puis `.click()` natif sur l'élément `button[type=submit]` du formulaire `/cart/add`, sur le bouton
`name="plus"` du panier, et sur le bouton `name="checkout"`) — action strictement équivalente à un tap
utilisateur sur ces éléments, vérifiée à chaque étape par relecture de `/cart.js` et par capture d'écran.

- **PASS — ajout au panier.** `Ajouter | €269` cliqué → `/cart.js` : 1 article « Kit Tufting Complet »,
  269 €. Tiroir panier ouvert visuellement, propre, aucune superposition (capture à l'appui).
- **PASS — mise à jour de quantité.** Clic sur `+` dans le tiroir → `/cart.js` : quantité 2, total
  538 € = 2×269 €. Capture d'écran conforme, prix et quantité synchronisés visuellement et côté API.
- **PASS — accès au checkout, sans donnée personnelle saisie et sans aller au paiement.** Clic sur
  « Commander » → atterrissage réel sur `https://tufteo.com/checkouts/cn/hWNFij9aGlE6NA8HePQVrIUl/fr-fr…`
  (checkout Shopify natif). Aucun champ de contact, d'adresse ou de carte n'a été rempli. Total affiché
  **538,00 €**, cohérent avec le panier.
- **Frais de port et seuil.** Aucun frais de port n'apparaît avant saisie d'adresse (normal, Shopify
  calcule après code postal) ; mais le bandeau du tiroir panier affiche « Livraison offerte en France »
  **sans mention de seuil ni de montant minimum**, à 538 € comme à 269 € — cohérent avec le bandeau du
  header et le footer (« Livraison offerte en France », aucune mention de seuil trouvée nulle part sur
  le site). **PASS pour la concordance** : aucune contradiction entre promesse et comportement observé,
  mais je n'ai pas pu confirmer le montant réel des frais hors France (pas testé, hors périmètre France
  du plan).

---

## C2 — Liens et redirections

**PASS — les 6 anciennes URL `/pages/*` redirigent proprement, un seul saut chacune.** 16/08/2026,
mesuré via `performance.getEntriesByType('navigation')[0].redirectCount` (fiable, indépendant de
l'affichage) sur chaque URL sans le paramètre `preview_theme_id` (les redirections sont gérées au
niveau du routage Shopify, avant chargement du thème — donc identiques que le thème actif soit le
brouillon ou le publié ; les tester sans paramètre de prévisualisation donne la mesure exacte, sans
artefact) :

| Ancienne URL | Destination finale | `redirectCount` |
|---|---|---|
| `/pages/politique-de-confidentialite` | `/policies/privacy-policy` | 1 |
| `/pages/mentions-legales` | `/policies/legal-notice` | 1 |
| `/pages/politique-de-remboursement` | `/policies/refund-policy` | 1 |
| `/pages/conditions-generales-de-vente` | `/policies/terms-of-sale` | 1 |
| `/pages/conditions-generales-d-utilisation` | `/policies/terms-of-service` | 1 |
| `/pages/politique-de-livraison` | `/policies/shipping-policy` | 1 |

Zéro chaîne de redirection, zéro 404 sur ces 6 URL. **Note méthodologique** : en testant la même URL
**avec** `?preview_theme_id=189410738561` ajouté, `redirectCount` passe à 2 — artefact du mécanisme de
prévisualisation Shopify lui-même (probablement un aller-retour pour poser le cookie de preview), sans
rapport avec la règle de redirection elle-même. Un vrai visiteur n'a jamais ce paramètre dans l'URL,
donc la mesure à 1 saut ci-dessus est la mesure qui compte.

**FAIL — voir C1 :** les 3 liens réseaux sociaux du footer (Facebook/YouTube/LinkedIn) ne sont pas
cassés au sens 404, mais pointent vers un tiers (« themefullstack », le thème Shopify utilisé) — lien
mort au sens fonctionnel même s'il répond 200. Détail dans C1.

**NON VÉRIFIÉ — reste du maillage.** J'ai vérifié les 6 redirections légales, le lien « Préférences en
matière de cookies » (404, voir C6), et les hrefs du footer/menu principal listés en C1/C3/C6. Je n'ai
pas cliqué systématiquement chaque lien du menu Consommables, des collections, ni des articles Academy —
à compléter si Hakim veut une couverture exhaustive avant soumission.

---

## C5 — Données structurées (JSON-LD)

Vérifié 16/08/2026 par lecture et `JSON.parse()` direct des balises `<script type="application/ld+json">`
sur l'accueil et sur la fiche « Kit Tufting Complet », thème brouillon `189410738561`.

**PASS — JSON valide, pas de défaut de virgule.** Les deux blocs (`Organization` sur l'accueil,
`Product` sur la fiche) parsent sans erreur. Le gabarit `organization-schema.liquid` n'a **pas** le
défaut de virgule constaté sur Maison Noirmont.

**`Organization` (accueil)** :
- `name`: "Tuftéo" — `address`: 47 Rue Vivienne, 75002 Paris, France — `telephone`: +33756828094 —
  `email`: contact@tufteo.com — cohérent avec le footer.
- **FAIL — `sameAs` contient les mêmes 3 liens placeholder du thème démo** (`facebook.com/themefullstack`,
  `youtube.com/@themefullstack`, `linkedin.com/company/themefullstack`) que ceux repérés en C1/C2. Ce
  n'est donc pas qu'un défaut d'affichage footer : c'est **injecté dans les données structurées que
  Google lit directement** pour le Knowledge Graph. Même correction que C1 : retirer ou remplacer ces
  3 URL avant soumission.
- **NON VÉRIFIÉ / absent — `legalName`.** Le schéma ne contient **aucun champ `legalName`** (seulement
  `name: "Tuftéo"`) : impossible de vérifier une cohérence qui n'a pas de valeur à comparer. Je remonte
  le manque, sans trancher s'il doit être ajouté — c'est lié au point ouvert d'agent A sur l'entité
  Tuftéo vs OH Ventures (A3).

**`Product` (fiche « Kit Tufting Complet »)** :
- **PASS — prix et disponibilité corrects.** `offers.price: "269.00"`, `priceCurrency: "EUR"` —
  identique au prix affiché à l'écran. `availability: http://schema.org/InStock`.
- **PASS — aucun prix barré résiduel.** Pas de champ `priceValidUntil` suspect, pas de second prix,
  cohérent avec la purge des `compareAtPrice` déjà vérifiée par un autre agent.
- **Observation (hors verdict, transmise à l'agent B)** : le champ `sku` vaut
  `"14:94#SET C;200007763:201336342"` — un identifiant technique brut de type fournisseur/AliExpress
  (`pid:vid`), pas un SKU boutique lisible. Il part tel quel dans les données structurées publiques.
  Idem pour `image` : l'URL pointe vers le fichier au nom brut fournisseur
  (`electric-2-in-1-tufting-gun-set-with-fabric-carpet-trimmer-…-01.png`), déjà signalé en C1.
- **Observation** : aucun `aggregateRating` ni `review` dans ce schéma ni ailleurs sur la page (ni
  JSON-LD ni microdonnées), alors que la fiche affiche « 4,9/5 — 20 avis » via le widget Trustoo. Pas un
  risque de conformité (rien n'est sur-déclaré côté Google), juste une occasion de rich snippet non
  exploitée — je ne recommande pas de correction, simple constat.

**NON VÉRIFIÉ** : schéma `Product` sur les autres fiches (40 au total selon le plan) — je n'ai contrôlé
que « Kit Tufting Complet ». Le motif du `sku` brut et de l'image fournisseur est probablement partagé
par les fiches issues du même import DSers, à confirmer fiche par fiche si Hakim le souhaite.

---

## C4 — Icônes de paiement du footer contre les moyens réellement proposés au checkout

**Méthode** : lecture du footer (balise `payment_type_svg_tag` native Shopify — dynamique, reflète en
principe directement Réglages > Paiements) via les `<title>` SVG, puis parcours réel du checkout jusqu'à
la page de paiement (sans saisie de donnée personnelle), lecture du DOM des radios de paiement.

**Footer (site entier, dynamique) — 16/08/2026** : `Visa`, `Mastercard`, `Apple Pay`, `PayPal`,
`Shop Pay`, `American Express`. Pas de Klarna, pas de Google Pay dans cette rangée précise.

**Fiche produit** : sous le bouton « Ajouter », **même rangée** que le footer (Visa/Mastercard/Apple
Pay/PayPal/Shop Pay/Amex). **Séparément**, sous le prix, un bandeau « Ou 4x 67,25€ avec [logo PayPal]
[logo Klarna] » — c'est le **seul** endroit du site où le logo Klarna apparaît hors checkout.

**Checkout réel (`/checkouts/cn/...`, jamais atteint le paiement)** :
- Paiement express, tout en haut, avant tout champ : **Shop Pay** et **PayPal** (boutons pleine largeur).
  Pas de bouton Apple Pay express visible dans ce navigateur.
- Section « Paiement », 3 méthodes réelles en radio (confirmées dans le DOM,
  `input[type=radio][name=basic]`, toutes `visibility:visible`, aucune désactivée) :
  `basic-creditCards` (Visa/Mastercard/Amex + « +2 » autres réseaux, sélectionné par défaut),
  `basic-PAYPAL_EXPRESS` (PayPal), **`basic-Klarna` (Klarna)**. Capture d'écran à l'appui : la ligne
  Klarna est bien affichée, sélectionnable, avec son logo rose — ce n'est pas un élément mort ou masqué.

**Verdict C4 (constat, pas un jugement de conformité) :**
- **PayPal et Klarna, tous deux affichés sur la fiche produit, sont tous deux réellement proposés au
  checkout.** Aucune promesse de paiement mensongère trouvée : tout ce qui est montré sur la PDP
  fonctionne réellement à l'étape de paiement.
- **Écart trouvé, mais dans l'autre sens que celui redouté par le plan** : Klarna est un moyen de
  paiement réel et actif, mais il **n'apparaît dans aucune rangée d'icônes de confiance** (ni footer, ni
  rangée sous le bouton « Ajouter ») — seulement dans le bandeau « paiement en 4x ». Ce n'est pas une
  fausse promesse (sous-représentation, pas sur-représentation), donc à mon sens moins risqué pour GMC,
  mais je ne tranche pas ce point — c'est à Hakim de juger si Klarna mérite sa propre icône en footer.
  **Correction proposée si retenue** : ajouter Klarna à la liste des moyens de paiement affichés dans
  Réglages > Paiements pour qu'il apparaisse dans la balise `payment_type_svg_tag` du footer (ou
  accepter l'écart tel quel, c'est un choix, pas un bug).
  **Ni Google Pay ni aucun autre moyen non proposé n'a été trouvé affiché nulle part** (footer, PDP,
  checkout) — cohérent avec le retrait de Google Pay décidé par Hakim.
- **NON VÉRIFIÉ — Apple Pay au checkout réel.** Le bouton express Apple Pay ne s'affiche pas dans ce
  navigateur automatisé (Chromium), ce qui est attendu : Apple Pay Web n'apparaît que sur Safari/iOS
  avec une carte enregistrée dans le portefeuille — son absence ici **ne prouve rien** sur sa disponibilité
  réelle. Seul un test sur Safari/iPhone avec une carte Apple Pay peut trancher ce point ; hors de portée
  de cet outil.

---

## C6 — Bandeau cookies

Testé 16/08/2026, mobile 375×812, en localisation France (`localization=FR` posé automatiquement).

**FAIL — aucun bandeau de consentement ne s'affiche au premier chargement, y compris en simulant une
première visite.** Vérifié deux fois : une fois avec les cookies/`localStorage` déjà présents (visite
répétée), une fois après avoir **effacé tous les cookies et le `localStorage` en JS puis rechargé** —
dans les deux cas, aucun bandeau visible à l'écran, et `window.Shopify.customerPrivacy` (l'API native de
consentement Shopify) **n'existe pas** dans la page malgré le script
`cdn/shopifycloud/privacy-banner/storefront-banner.js` bien chargé (200). Donc : ni refus des cookies non
essentiels possible, ni même un choix proposé.

**FAIL — le lien de rappel du bandeau, en footer, mène à une page 404.** `Préférences en matière de
cookies` → `https://tufteo.com/policies/#shopifyReshowConsentBanner` → **`/policies/` répond 404**
(confirmé par code HTTP dans le réseau, capture d'écran à l'appui, testé avec et sans
`preview_theme_id`). C'est le mécanisme natif Shopify (`#shopifyReshowConsentBanner`) mais il cible une
URL qui n'existe pas sur ce thème — donc même un visiteur qui voudrait revenir sur son choix ne le peut
pas manuellement non plus.

**FAIL — des scripts et cookies tiers/traçants se posent avant tout consentement, faute de bandeau.**
Sur le tout premier chargement (post-vidage cookies), avant toute interaction : `trekkie.storefront…js`
(analytics propre de Shopify), le pixel `web-pixels@…/pixel.modern.js`, plusieurs appels
`POST /.well-known/shopify/monorail/unstable/produce_batch` (télémétrie), et le widget d'avis Trustoo
(`swiper-reviews.min.js`, `seal-review.min.js`, qui pose `trustoo_uv` en `localStorage`) se chargent
tous automatiquement. Comme il n'y a pas de bandeau à refuser, il n'y a mécaniquement pas moyen d'éviter
ce dépôt. **Correction proposée** : activer/configurer le bandeau de consentement dans Shopify
(Réglages > Confidentialité des clients) pour la France/UE, et corriger le lien de rappel vers une URL
qui existe réellement (probablement `/` avec l'ancre, pas `/policies/`).

**NON VÉRIFIÉ** : je n'ai pas pu inspecter les cookies `httpOnly` (invisibles en JavaScript) qui
auraient pu être posés côté serveur avant consentement — seuls `document.cookie` et les requêtes réseau
observables ont été contrôlés. Je n'ai pas non plus de moyen de forcer artificiellement une détection
« visiteur UE » différente de celle déjà appliquée par Shopify (`localization=FR`) : si le bandeau est
configuré pour ne s'afficher qu'à certains pays précis autres que la France, ce test ne le verrait pas.

---

**(Complément à C1 — Accueil.) Observation hors-scope, remontée à Agent A, pas un verdict ici :** sur
l'accueil, la carte « Kit Tufting Complet » affiche **269 €** dans le carrousel produits, alors que le
bloc « Guide de choix » plus bas affiche **229 €** pour ce qui semble être la même offre « Kit complet
2-en-1 ». Écart de 40 € entre deux blocs de la même page. Je ne tranche pas si c'est la même offre ou
deux offres différentes (gun+tondeuse vs gun seul) — à vérifier côté catalogue par Agent A/B.

**(Complément à C1 — Accueil.) Console, mobile, après vidage cookies** : deux erreurs `Failed to load
resource: the server responded with a status of 401 ()` sur `GET https://tufteo.com/sf_private_access_tokens`.
C'est un endpoint interne Shopify (jeton d'accès storefront privé) qui renvoie 401 par conception hors
contexte app privée ; aucune autre erreur JS nouvelle observée. Je le note sans le classer FAIL : il n'a
aucun effet visible sur le rendu ni la fonctionnalité constatée.

---

## C7 — Poids et requêtes

Mesuré 16/08/2026 via `performance.getEntriesByType('resource'/'navigation')` dans la page (mesure
directe du navigateur, pas un outil externe). **Aucun score PageSpeed annoncé**, conformément à la
consigne — l'outil ne sait pas mesurer un thème non publié.

**Accueil (mobile, chargement initial)** :
- **PASS — aucune requête vidéo.** Recherche explicite de `.mp4/.webm/.mov/.m3u8` dans toutes les
  ressources chargées : **0 résultat**. La vidéo hero a bien été remplacée par une image
  (`tufteo-home-hero.png`), confirmé au niveau réseau, pas seulement à l'écran.
- Poids et requêtes : **121 requêtes** hors préchargement checkout, **≈ 1 404 Ko (1,4 Mo)** transférés.
  En plus de ça, **102 requêtes supplémentaires** vers `checkout-web` (JS/CSS du checkout accéléré,
  précaché par Shopify Shop Pay — `transferSize: 0`, servies depuis un cache interne, poids non
  significatif). Ces 102 requêtes sont un comportement Shopify natif (préchargement du checkout
  accéléré), pas un défaut du thème — je les distingue du poids propre du thème pour ne pas fausser la
  lecture.

**Fiche produit `/products/kit-tufting-complet` (mobile, chargement initial)** :
- **FAIL — deux vidéos de la galerie produit se téléchargent entièrement, sans interaction, dès le
  chargement de la page.** Mesuré via `performance.getEntriesByType('resource')`, `transferSize` par
  fichier : `41a163…-HD-1080p-7.2Mbps-….mp4` → **6 947 Ko**, `97731b…-HD-1080p-7.2Mbps-….mp4` →
  **8 120 Ko** — soit **≈ 15 Mo à eux deux**, démarrés à ~570 ms après la navigation (donc pendant le
  chargement initial, avant tout clic de ma part — vérifié via `startTime` des entrées de performance).
  Une 3ᵉ vidéo (720p) a démarré mais transféré 0 Ko (annulée/differée). Ce n'est **pas** la vidéo hero de
  l'accueil (déjà retirée, voir plus haut) : ce sont des vidéos dans le carrousel d'images de la fiche
  produit elle-même (les vignettes 2/3 de la galerie), qui devraient normalement se charger à la demande
  (le composant `deferred-media.js` du thème sert justement à ça, et la section « En vidéo » plus bas
  sur la page dit explicitement « Charger la vidéo » — donc le comportement différé existe ailleurs sur
  la même page, ce qui suggère un réglage différent, pas cohérent, pour les vidéos de la galerie
  principale). **Correction proposée** : vérifier le réglage `preload` du lecteur vidéo dans la galerie
  produit (`product-media-gallery.js` / section correspondante) et le passer à `none` ou `metadata`, ou
  utiliser le même mécanisme de chargement différé que la section « En vidéo ».
- Poids total (hors préchargement checkout) : **142 requêtes, ≈ 15 075 Ko (14,7 Mo)** — porté
  presque entièrement par les deux vidéos ci-dessus. Sans elles, le poids de la fiche serait comparable
  à l'accueil (image produits + JS/CSS du thème).

**NON VÉRIFIÉ** : poids/requêtes sur collection, panier, policies (pages visuellement légères, sans
vidéo constatée dans leur DOM, mais je n'ai pas fait la mesure `performance` chiffrée dessus). Poids
desktop non mesuré (seul le mobile a été chiffré).

---

## Résumé des verdicts

| # | Item | Verdict | Gravité si FAIL |
|---|---|---|---|
| C1 | Bandeau d'annonce superposé (mobile + desktop) | **FAIL** | Élevée — visible immédiatement par tout visiteur, sur toutes les pages |
| C1 | Placeholder résiduel : réseaux sociaux → thème démo | **FAIL** | Élevée — mène hors site, présent aussi dans le JSON-LD (C5) |
| C1 | Titre dupliqué (H1×2) sur les 6 policies | **FAIL** | Moyenne — mauvais pour le SEO et l'impression de sérieux, pas bloquant fonctionnellement |
| C1 | Pas de placeholder texte (`[promo]`, lorem ipsum) | PASS | — |
| C1 | `translation missing` | NON VÉRIFIÉ | — (pas trouvé sur les pages vues, pas balayé partout) |
| C1 | Rendu fiche produit / collection / panier | PASS | — |
| C2 | 6 redirections `/pages/*` → `/policies/*`, 301 simple | PASS | — |
| C2 | Lien réseaux sociaux fonctionnel (voir C1) | **FAIL** | Élevée (doublon avec C1) |
| C2 | Couverture exhaustive de tous les liens du site | NON VÉRIFIÉ | — |
| C3 | Ajout au panier | PASS | — |
| C3 | Mise à jour de quantité | PASS | — |
| C3 | Accès au checkout sans donnée personnelle | PASS | — |
| C3 | Concordance frais de port / seuil affiché | PASS | — |
| C4 | Icônes affichées réellement proposées au checkout | PASS | — (aucune fausse promesse trouvée) |
| C4 | Klarna absent des rangées d'icônes malgré disponibilité réelle | Constat (pas FAIL) | Faible — sous-représentation, pas sur-représentation |
| C4 | Apple Pay au checkout réel | NON VÉRIFIÉ | — (limite de l'outil, pas du site) |
| C5 | JSON-LD valide (Organization + Product) | PASS | — |
| C5 | `sameAs` = liens thème démo | **FAIL** | Élevée (doublon avec C1/C2, mais dans les données structurées) |
| C5 | Prix/disponibilité Product schema corrects, pas de prix barré | PASS | — |
| C5 | `legalName` | Absent / non vérifiable | — remonté à Agent A |
| C5 | Schéma sur les 39 autres fiches | NON VÉRIFIÉ | — |
| C6 | Bandeau cookies présent au chargement | **FAIL** | Élevée — aucun consentement demandé |
| C6 | Lien de rappel du bandeau fonctionnel | **FAIL** | Moyenne — 404 |
| C6 | Scripts/cookies tiers avant consentement | **FAIL** | Élevée (conséquence directe de l'absence de bandeau) |
| C7 | Absence de requête vidéo sur l'accueil | PASS | — |
| C7 | Absence de téléchargement vidéo non sollicité sur la fiche produit | **FAIL** | Moyenne à élevée — 15 Mo chargés sans interaction |
| C7 | Score PageSpeed | Non applicable (consigne : ne pas mesurer) | — |

**Total** : 9 PASS nets, 9 FAIL, 1 constat neutre (Klarna), 6 NON VÉRIFIÉ/absent.

**Classement des FAIL par gravité (du plus grave au moins grave), à mon jugement technique :**
1. **Bandeau cookies absent + scripts tiers déposés avant consentement (C6)** — risque réglementaire et
   de confiance le plus large, touche tout le site, à chaque visite.
2. **Réseaux sociaux → compte du thème démo, y compris dans le JSON-LD Organization (C1/C2/C5)** — visible,
   présent dans les données lues par Google, facile à corriger.
3. **Bandeau d'annonce superposé en permanence (C1)** — visible immédiatement sur mobile et desktop, sur
   toutes les pages, dès le premier écran.
4. **15 Mo de vidéos de fiche produit chargés sans interaction (C7)** — pas d'erreur visible pour
   l'utilisateur mais poids et données mobiles significatifs, peut ralentir sensiblement les fiches
   produit sur un réseau mobile moyen.
5. **Titre dupliqué (H1×2) sur les 6 policies (C1)** — mauvais signal SEO/sérieux mais sans impact
   fonctionnel.
6. **Lien de rappel du bandeau cookies en 404 (C6)** — mineur en soi mais s'ajoute au point n°1.

**Point le plus grave** : l'absence totale de bandeau de consentement cookies (C6), combinée au fait que
des scripts tiers (widget d'avis Trustoo, pixel/analytics Shopify) se chargent avant tout choix de
l'utilisateur — sur toutes les pages, à chaque visite.

**Résultat du contrôle des icônes de paiement (C4)** : pas de mensonge trouvé. Tout ce qu'affiche la
fiche produit (PayPal, Klarna en « paiement en 4x ») est réellement proposé et sélectionnable au
checkout réel, vérifié en poussant deux produits au panier et en atteignant la page de paiement sans
saisir aucune donnée personnelle. Le seul écart va dans le sens le moins risqué : Klarna n'a pas d'icône
dans les rangées de confiance (footer, PDP) alors qu'il fonctionne réellement — sous-promesse, pas
sur-promesse. Apple Pay n'a pas pu être vérifié au checkout réel (limite du navigateur automatisé, pas
du site) ; Google Pay est absent partout, cohérent avec son retrait.

---

## Ce que je n'ai pas pu vérifier

- **`translation missing`** : recherché sur accueil/fiche/collection/panier/policies sans en trouver,
  mais je n'ai pas balayé les pages CMS (Notre histoire, FAQ, Contact, Apprendre/Academy) ni les 39
  autres fiches produit.
- **Apple Pay au checkout réel** : ce navigateur automatisé (Chromium) ne peut pas afficher le bouton
  Apple Pay quelle que soit la configuration du site — seul un test sur Safari/iPhone avec une carte
  Apple Pay enregistrée peut trancher.
- **Cookies `httpOnly`** posés avant consentement : invisibles en JavaScript, seuls `document.cookie` et
  les requêtes réseau observables ont été contrôlés pour C6.
- **Détection de région autre que France** pour le bandeau cookies : je n'ai testé qu'en localisation
  FR (celle posée automatiquement par Shopify pour ce test) ; si le bandeau est câblé pour d'autres
  géographies seulement, ce test ne le verrait pas.
- **Couverture exhaustive des liens** : menu Consommables (sous-liens), pages Academy/apprentissage,
  articles de blog s'il y en a — je n'ai pas cliqué systématiquement chaque lien du site, seulement les
  points explicitement listés dans le plan (6 redirections légales, réseaux sociaux, lien cookies).
- **JSON-LD Product sur les 39 autres fiches** : je n'ai contrôlé que « Kit Tufting Complet ». Le motif
  du SKU brut fournisseur et de l'image non retravaillée dans le schéma est probablement partagé par les
  fiches du même import, à confirmer une par une si besoin.
- **Poids/requêtes desktop et sur collection/panier/policies** : chiffrage fait uniquement en mobile,
  sur accueil et fiche produit.
- **Frais de port hors France** : hors périmètre du plan (France uniquement), non testé.
- **Fond de l'écart de prix 269€/229€ sur l'accueil** : signalé en observation, pas creusé — relève du
  catalogue (Agent A/B), pas du rendu technique.

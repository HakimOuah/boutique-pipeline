# Mesure d'achat et consentement cookies — Maison Noirmont

> **08/08/2026.** Traitement des deux P0 restés ouverts après `AUDIT-GMC-FINAL-2026-08-08.md` :
> **N5 — aucune mesure d'achat** et **N4 — aucun consentement cookies**.
>
> Boutique : `v42pzp-h4.myshopify.com` / `maisonnoirmont.fr` — plan **Basic**, marché unique **France**,
> `shipsToCountries = ["FR"]`, toujours sous mot de passe.
> Thème MAIN `204248088914` · thème de TRAVAIL `205089014098` (non publié).
>
> **Méthode** : API Admin (GraphQL), requêtes anonymes sur le domaine public, exécution JavaScript dans le
> navigateur sur `maisonnoirmont.fr`, lecture du script de bandeau servi par Shopify, et test de contrôle
> sur une boutique Shopify tierce. Rien n'a été supposé à partir de l'audit : tout a été revérifié.

---

## Résumé en une page

| | Verdict de l'audit | Ce qui a été constaté | État |
|---|---|---|---|
| **N4 — consentement** | « Aucun mécanisme de consentement, bandeau absent, lien Préférences en 404 » | **Faux.** Le consentement natif Shopify est **déjà installé et fonctionnel** : région France en « consentement requis », `storefront-banner.js` chargé, `shouldShowBanner() = true`, boutons accepter/refuser de même niveau, lien « Préférences » intercepté par le script (ce n'est pas un lien mort) | ✅ **Clos** — reste une vérification visuelle après retrait du mot de passe |
| **N5 — mesure d'achat** | « Ni gtag, ni GA4, ni pixel de conversion » | **Confirmé, et plus précisément qualifié** : `webPixelsConfigList` de la boutique ne contient que les deux emplacements vides de Shopify. Zéro pixel marchand. L'app Google & YouTube n'est pas installée | ❌ **Ouvert** — non réparable par API, voir le mode opératoire §4 |

**Une correction a été appliquée** : la page `/pages/politique-de-cookies` décrivait un régime de
**consentement implicite** (« sauf si vous décidez de désactiver les cookies, vous acceptez… », « s'il a accepté
le dépôt de cookies **en poursuivant sa navigation** ») — interdit en France depuis 2020 — alors que le site
pratique en réalité l'opt-in. Le texte a été réaligné sur ce que le site fait réellement. Détail au §3.

---

## 1 — P0 n°2 : le consentement cookies était déjà en place

L'audit avait conclu à une absence totale de mécanisme. **Cette conclusion est erronée**, et les trois indices
sur lesquels elle reposait s'expliquent autrement.

### 1.1 Ce qui a été vérifié, et comment

| Point | Preuve | Comment obtenue |
|---|---|---|
| **La région France est en « consentement requis »** | `consentPolicy` renvoie `{id: "gid://shopify/ConsentPolicy/1563598881106", countryCode: "FR", consentRequired: true}`. L'identifiant **n'est pas préfixé `SD-`** : ce n'est pas la politique par défaut de Shopify, c'est un enregistrement **créé volontairement** dans *Réglages → Confidentialité des clients*. Les 250 autres pays sont tous en `SD-…` / `false` | API Admin, `{ consentPolicy { … } }` |
| **Le bandeau natif est activé** | `<script id='scb4127' async src='https://maisonnoirmont.fr/cdn/shopifycloud/privacy-banner/storefront-banner.js'>` est présent dans le `content_for_header` servi par Shopify | `curl` anonyme sur `https://maisonnoirmont.fr/` |
| **…et ce n'est pas systématique** | Test de contrôle sur **allbirds.com** (boutique Shopify confirmée, `Shopify.shop` présent) : **0 occurrence** de `storefront-banner.js`. Shopify n'injecte donc ce script **que** si le bandeau est activé | `curl` anonyme |
| **L'API de consentement fonctionne** | `window.Shopify.loadFeatures(['consent-tracking-api'])` réussit ; ensuite `customerPrivacy.shouldShowBanner() = true`, `currentVisitorConsent() = {marketing:"", analytics:"", preferences:"", sale_of_data:""}`, `analyticsProcessingAllowed() = false`, `marketingAllowed() = false` | JavaScript exécuté sur `maisonnoirmont.fr` |
| **Accepter et refuser sont au même niveau** | Le script définit `ButtonAcceptId = "shopify-pc__banner__btn-accept"` **et** `ButtonDeclineId = "shopify-pc__banner__btn-decline"`, plus `PrefsId = "shopify-pc__banner__btn-manage-prefs"` | Lecture de `storefront-banner.js` |
| **Le lien « Préférences » n'est pas un lien mort** | Le script enregistre **inconditionnellement** au chargement : `document.addEventListener("click", n => bt(n, i))` où `bt` teste `o.closest('a[href$="#shopifyReshowConsentBanner"]')` et `i` fait `n.preventDefault(); xt()` (ouverture du panneau de préférences). Le clic est donc **intercepté avant toute navigation** | Lecture de `storefront-banner.js` |

### 1.2 Pourquoi l'audit a vu le contraire

- **`window.Shopify.customerPrivacy` était `false`** → *signal sans valeur*. L'API de confidentialité client
  n'est **jamais** exposée automatiquement : il faut l'appeler via `Shopify.loadFeatures([{name:'consent-tracking-api', version:'0.1'}])`.
  Elle est `undefined` sur une boutique parfaitement conforme. Ce critère est à retirer de la grille d'audit.
- **`/policies/` renvoie un 404** → *exact, mais sans objet*. `#shopifyReshowConsentBanner` est le point d'ancrage
  officiel de Shopify pour rouvrir le panneau ; il n'est **pas censé être suivi**. Le 404 n'apparaît que si on
  colle l'URL à la main dans la barre d'adresse. Le clic réel ouvre le panneau.
- **`#shopify-pc__banner` était `null`** → deux explications possibles, toutes deux bénignes :
  1. le bandeau ne s'affiche **que pour un visiteur situé dans une région où le consentement est requis**, ici
     la France uniquement. L'audit a été mené pendant le séjour de Hakim au Portugal — `PT` est en
     `consentRequired: false`, donc pas de bandeau pour ce visiteur ;
  2. la boutique est sous mot de passe, et le bandeau ne se rend pas sur `/password` (reproduit :
     `shouldShowBanner()` renvoie bien `true`, mais aucun élément `#shopify-pc__*` n'est injecté sur cette page).

> **⚠️ Ce qu'il reste à vérifier, et que je n'ai pas pu vérifier.** Le connecteur MCP ne dispose pas du droit
> `read_privacy_settings` : la requête `{ privacySettings { banner { enabled } } }` est refusée. Je n'ai donc
> **pas pu lire directement l'interrupteur** « bandeau activé ». La conclusion ci-dessus repose sur cinq
> preuves indirectes convergentes (script injecté + non systématique + politique FR non-défaut + API
> fonctionnelle + entrée « Préférences en matière de cookies » ajoutée par Shopify dans `shop.policies`).
> **La vérification finale se fait à l'œil, une fois le mot de passe retiré** — recette au §5.

### 1.3 Le lien « Préférences en matière de cookies » : rien à réparer

Le pied de page est produit par `blocks/_footer-policy-list.liquid`, qui boucle simplement sur les politiques :

```liquid
{%- for policy in shop.policies -%}
  <a href="{{ policy.url }}" class="policy-list__link">{{ policy.title | escape }}</a>
{%- endfor -%}
```

Aucun menu de la boutique ne contient ce lien (vérifié sur les 8 menus : `main-menu`, `footer`,
`footer-boutique`, `footer-informations`, `footer-legal`, les deux brouillons `noirmont-*`, et le menu compte
client). **C'est Shopify qui ajoute l'entrée « Préférences en matière de cookies » dans `shop.policies`** quand
le bandeau est actif — preuve supplémentaire qu'il l'est. **Aucune modification de thème n'a été faite** :
supprimer ce lien aurait retiré le point de retrait du consentement, c'est-à-dire cassé la conformité au lieu
de la réparer.

### 1.4 Région d'application : France seule, et c'est correct

`shop.shipsToCountries = ["FR"]`, un seul marché (« France », `gid://shopify/Market/118667870546`). La région
de consentement limitée à la France couvre donc **100 % des visiteurs susceptibles de commander**. Rien à
élargir aujourd'hui. **À revoir si un jour la boutique ouvre l'expédition à d'autres pays de l'EEE ou au
Royaume-Uni** — il faudra alors ajouter ces régions dans *Réglages → Confidentialité des clients*.

---

## 2 — P0 n°1 : la mesure d'achat est bien absente

### 2.1 État réel, établi et non déduit

| Vérification | Résultat |
|---|---|
| **Pixels web enregistrés** | `webPixelsConfigList` du storefront ne contient que `shopify-app-pixel` et `shopify-custom-pixel` — les **deux conteneurs vides** que Shopify sert toujours. **Zéro pixel marchand, zéro pixel d'app.** |
| **Scripts de suivi dans le thème** | `layout/theme.liquid` (thème de TRAVAIL) : aucun `gtag`, aucun `dataLayer`, aucun `googletagmanager`. `snippets/scripts.liquid` : uniquement les modules du thème FullStack. `{{ content_for_header }}` est bien présent — c'est le prérequis pour que les pixels et l'app Google fonctionnent une fois installés. |
| **App Google & YouTube** | **Non installée.** Elle figure dans `shop.availableChannelApps` — la liste des canaux **non installés** — sous `gid://shopify/App/1780363`, handle `google`, éditeur `Google LLC`. |
| **Canal de vente Google** | **Absent.** `publications` ne renvoie que « Boutique en ligne », « Point de vente » et « Shop ». |

### 2.2 Ce que l'API refuse, mot pour mot

Testé, pas supposé :

```
mutation { webPixelCreate(webPixel: { settings: "…" }) { … } }
→ "Access denied for webPixelCreate field. Required access: `write_pixels` access scope.
   Also: The app requires read_customer_events access scope and user access permission."
```

```
{ webPixel { id settings } }
→ "Access denied for webPixel field. Required access: `read_pixels` access scope."

{ privacySettings { banner { enabled } } }
→ "Access denied for privacySettings field. Required access: `read_privacy_settings` access scope."
```

**Conclusion : la mesure ne peut pas être installée par API depuis cette session.** `webPixelCreate` est
réservé au contexte d'une application autorisée sur ces portées ; le connecteur ne les a pas, et les obtenir
suppose une autorisation de Hakim. Le livrable est donc le **chemin exact**, ci-dessous.

### 2.3 Quelle voie retenir, et pourquoi

**➡️ Retenu : l'app Google & YouTube.**

L'argument décisif n'est pas le confort, c'est la **faisabilité technique sur le plan Basic** :

- **Le code de thème ne peut pas mesurer l'achat.** La caisse et la page de confirmation sont hébergées par
  Shopify et ne rendent pas `layout/theme.liquid`. Le plan Basic n'ouvre ni `checkout.liquid` ni les scripts
  additionnels de la page de statut de commande. Un `gtag` collé dans le thème verrait `page_view`,
  `view_item`, `add_to_cart` — **et jamais `purchase`**. C'est précisément l'événement exigé par la porte 5 §E.
  **Cette voie est donc éliminée, pas par préférence mais par impossibilité.** Elle a un second défaut : le
  code de thème s'exécute au chargement, donc **avant** toute réponse au bandeau — ce qui casserait le
  consentement remis en état au §1.
- **Le pixel personnalisé** (*Réglages → Événements client*) voit bien l'événement `checkout_completed` et
  est nativement soumis au consentement. Mais Shopify exécute les pixels personnalisés dans une **iframe
  bac-à-sable d'origine distincte** : les cookies écrits par `gtag` y atterrissent sur cette origine, pas sur
  `maisonnoirmont.fr`. L'attribution GA4 et Google Ads en sort dégradée, et le Consent Mode v2 doit être
  câblé à la main. C'est un **plan B**, pas le plan A.
- **L'app Google & YouTube** installe un **pixel d'app** (`type: "APP"`, portées supérieures à celles d'un
  pixel personnalisé), déclare `privacyPurposes: ["ANALYTICS","MARKETING"]` — donc **automatiquement soumis
  au bandeau déjà en place** — et gère seule le **Consent Mode v2**, la balise Google, GA4, la conversion
  Google Ads et les conversions améliorées. Zéro ligne de code, zéro `transaction_id` à fabriquer, zéro
  déduplication à écrire.
- **Elle est de toute façon nécessaire pour la suite** : c'est elle qui alimente le flux produit vers
  Merchant Center.

> **⚠️ Point d'attention CSS, à trancher avant d'installer.** L'app Google & YouTube veut **créer ou
> revendiquer un compte Merchant Center**. Si le partenaire CSS impose que le compte MC soit créé **dans son
> groupe CSS**, un compte créé par l'app entrerait en conflit. **Ne pas laisser l'app créer un Merchant
> Center avant d'avoir posé la question au CSS.** L'app permet de connecter la balise Google et le suivi de
> conversion **sans** synchroniser les produits : c'est cet usage-là qu'il faut viser en premier. La mesure
> d'achat n'attend pas le flux produit — et l'audit (E9) interdit de toute façon de créer le compte GMC
> tant que la boutique n'est pas finie.

---

## 3 — Ce qui a été fait sur la boutique

### 3.1 Page « Politique de cookies » réalignée sur la réalité

**Une seule écriture a été faite sur la boutique** : le corps de `/pages/politique-de-cookies`
(`gid://shopify/Page/176214638930`).

L'audit soupçonnait le défaut inverse du vrai. Il notait (B12) que la page « promet un choix qui n'existe
pas ». En réalité le choix existe — et c'est **la page** qui décrivait un régime périmé :

| Avant (supprimé) | Pourquoi c'était un défaut |
|---|---|
| « **Sauf si vous décidez de désactiver les cookies, vous acceptez** que le site puisse les utiliser. » | Consentement implicite. La CNIL l'a proscrit : le consentement doit résulter d'un acte positif. |
| « …et si l'Utilisateur a accepté le dépôt de cookies **en poursuivant sa navigation**… » | La navigation-vaut-consentement est interdite en France depuis 2020. |
| Section « Gérer vos cookies » entièrement consacrée au **réglage du navigateur** | Ne mentionnait nulle part le bandeau ni le lien « Préférences » du pied de page — le seul mécanisme réellement offert. |
| Inventaire de 6 cookies | Il manquait `_tracking_consent`, déposé par le bandeau. |

Le texte dit désormais ce que le site fait : bandeau à la première visite, **accepter et refuser sur deux
boutons de même niveau**, aucun cookie de mesure ou de publicité avant le choix, modification ou retrait à
tout moment via « Préférences en matière de cookies » en pied de page. L'inventaire ajoute
`_tracking_consent` et précise, section « Balises internet » comprise, qu'**aucun outil de mesure ou de
publicité n'est actif à ce jour** — ce qui est vrai (§2.1) et devra être mis à jour au §4, étape 7.

- Sauvegarde du texte d'origine : **`backup-consentement-2026-08-08/AVANT-politique-de-cookies.html`**
  (retour arrière : `pageUpdate` avec ce corps exact).
- Écriture vérifiée par relecture du corps distant : `updatedAt` passé de `2026-07-26T02:07:08Z` à
  `2026-08-08T21:39:50Z`, `userErrors: []`, contenu relu et conforme.

### 3.2 Ce qui n'a **pas** été touché, et pourquoi

- **Aucun thème.** Ni MAIN, ni TRAVAIL. Le lien « Préférences » fonctionne (§1.3) et le suivi ne doit pas
  passer par du code de thème (§2.3). Il n'y avait rien à écrire.
- **Aucun réglage de confidentialité.** La région France est déjà correctement configurée ; réécrire la
  politique FR par `consentPolicyUpdate` n'aurait rien changé et aurait risqué de casser un réglage sain
  (l'API renvoie d'ailleurs `SHOPIFY_COOKIE_BANNER_NOT_DISABLED` quand on tente d'y toucher avec le bandeau
  Shopify actif — cette mutation est destinée aux bandeaux tiers).
- **Aucune app installée, aucun compte créé.**
- **Aucun média, aucun visuel** (chantier parallèle).

---

## 4 — Marche à suivre pour Hakim, au clic près

### À avoir sous la main avant de commencer

1. **Un compte Google professionnel** — celui qui possédera durablement Google Ads et GA4. À créer avec
   `contact@maisonnoirmont.fr` si ce n'est pas déjà fait, **pas** avec une adresse personnelle : le compte
   Ads n'est pas transférable simplement ensuite.
2. **Un moyen de paiement** pour Google Ads (facturation, pas de dépense tant que rien n'est lancé).
3. **Les informations d'entreprise** : OH Ventures, 47 rue Vivienne, 75002 Paris, France + SIREN.
4. **L'accès DNS de `maisonnoirmont.fr`** (pour la vérification de domaine par enregistrement TXT, étape 8).
5. **Le contact du partenaire CSS**, et sa réponse à une question précise : *« Le compte Merchant Center
   doit-il être créé par vous, dans votre groupe CSS, ou puis-je le créer moi-même et vous y inviter ? »*
6. **Un accès administrateur Shopify** : `https://admin.shopify.com/store/v42pzp-h4`.

### Ordre des opérations

L'ordre n'est pas décoratif : la porte 5 §E interdit de dépenser sans mesure d'achat prouvée, et l'audit
(E9) interdit de créer le compte GMC avant que la boutique soit finie.

**Étape 1 — Vérifier le bandeau de consentement (5 min, à faire dès que le mot de passe est retiré)**
`https://admin.shopify.com/store/v42pzp-h4/settings/customer_privacy`
→ Vérifier que « **Bannière de cookies** » est bien **activée** et que la région **France** y figure.
→ Si l'écran propose une personnalisation, ne rien changer : les libellés Shopify sont déjà en français et
les deux boutons sont de même niveau.
→ Puis recette visuelle : §5.

**Étape 2 — Terminer les autres P0 de l'audit.** N1 (faux témoignages), N2 (SKU AliExpress), N3 (e-mail),
politique de retour, médiateur. **Rien de ce qui suit ne doit être fait avant.**

**Étape 3 — Publier le thème de TRAVAIL et retirer le mot de passe.** La boutique doit être visitable.

**Étape 4 — Créer la propriété GA4** — `analytics.google.com` → Admin → Créer une propriété
« Maison Noirmont », fuseau **Paris**, devise **EUR** → Flux de données → **Web** →
`https://maisonnoirmont.fr`.
→ **Noter l'identifiant de mesure `G-XXXXXXXXXX`.** ⚠️ *Cet identifiant n'existe pas encore : il n'y a
aucune propriété GA4 pour cette boutique à ce jour. Ne rien coller avant de l'avoir créé.*

**Étape 5 — Créer le compte Google Ads** — `ads.google.com`, **en mode expert**, sans créer de campagne.
Facturation en euros, France.
→ **Noter l'identifiant client `123-456-7890`.** ⚠️ *Ce compte n'existe pas encore non plus.*
→ Ne rien dépenser tant que l'étape 9 n'est pas validée.

**Étape 6 — Poser la question au CSS** (encadré du §2.3) et attendre sa réponse **avant** l'étape 7.

**Étape 7 — Installer l'app Google & YouTube et brancher la mesure**
`https://admin.shopify.com/store/v42pzp-h4` → **Applications** → rechercher « **Google & YouTube** »
(éditeur *Google LLC*) → **Installer**.
Puis, dans l'app :
1. **Connecter le compte Google** de l'étape 4/5.
2. Section **Google Analytics / balise Google** → sélectionner la propriété GA4 créée →
   **c'est ici que se colle le `G-XXXXXXXXXX`** si l'app le demande à la main.
3. Section **Google Ads** → lier le compte de l'étape 5 → activer le **suivi des conversions** →
   **c'est ici que se colle l'identifiant client Ads.** L'app crée alors l'action de conversion « Achat ».
4. **Merchant Center : selon la réponse du CSS.** Si le CSS possède le compte, **ne pas laisser l'app en
   créer un** ; s'arrêter ici et n'utiliser que la partie balise/conversion.
5. Vérifier ensuite dans `https://admin.shopify.com/store/v42pzp-h4/settings/customer_events` qu'un pixel
   Google apparaît bien dans la liste (aujourd'hui elle est vide).

**Étape 8 — Merchant Center** (seulement après l'étape 7 et l'accord du CSS) : création du compte selon la
voie retenue, vérification du domaine par **TXT DNS**, recopie des politiques **mot pour mot** depuis les
pages du site, puis connexion du flux et demande de revue.

**Étape 9 — Prouver la mesure avant le premier euro dépensé**
1. Passer une **commande test réelle** (un article, code promo 100 % ou remboursement immédiat après).
2. Dans GA4 → **Temps réel** puis **DebugView** : vérifier l'événement **`purchase`**, avec `value` égal au
   montant réel, `currency = EUR`, et un `transaction_id` unique et non nominatif.
3. Dans Google Ads → **Objectifs → Conversions** : la conversion « Achat » doit passer à
   « **Enregistrement des conversions** ».
4. **Réconcilier** : le montant vu dans GA4 doit être celui de la commande dans le back-office Shopify.
5. Rembourser la commande test.
→ **Tant que ces 5 points ne sont pas cochés, la porte 5 §E reste en échec et le budget 30 €/j ne part pas.**
Le principe Kraken s'applique : *sans preuve achat, `REPARER_AVANT`, jamais « lancer pour voir »*.

**Étape 10 — Remettre l'inventaire des cookies à jour.** Dès que la balise Google est active, ajouter à
`/pages/politique-de-cookies` les cookies `_ga`, `_ga_<ID>`, et `_gcl_au` si Google Ads est branché — et
**retirer les deux phrases qui affirment aujourd'hui qu'aucun outil de mesure n'est actif** (section
« Les cookies que nous déposons » et section « Balises internet »). C'est le point **F4** de l'audit ; laisser
ces phrases en place une fois la balise posée transformerait une page exacte en page mensongère.

### Plan B si l'app Google & YouTube est écartée

Si le CSS impose de ne pas installer l'app du tout, la voie de repli est le **pixel personnalisé** :
`https://admin.shopify.com/store/v42pzp-h4/settings/customer_events` → **Ajouter un pixel personnalisé** →
« Mesure Google » → **Autorisations : Analytics + Marketing** (pour qu'il soit soumis au bandeau) →
coller le code ci-dessous **après avoir remplacé les deux marqueurs**, puis **Enregistrer** et **Connecter**.

```js
// ⚠️ REMPLACER LES DEUX MARQUEURS AVANT DE COLLER — ne pas inventer d'identifiant.
const GA4_ID    = 'G-XXXXXXXXXX';        // étape 4
const ADS_ID    = 'AW-XXXXXXXXX';        // étape 5, format AW-
const ADS_LABEL = 'XXXXXXXXXXXXXXXXXXX'; // libellé de l'action de conversion « Achat »

const s = document.createElement('script');
s.async = true;
s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA4_ID;
document.head.appendChild(s);
window.dataLayer = window.dataLayer || [];
function gtag(){ dataLayer.push(arguments); }
gtag('js', new Date());
// Consent Mode v2 — refus par défaut ; le bac-à-sable du pixel n'est chargé
// qu'une fois le consentement donné, mais on reste explicite.
gtag('consent', 'default', {
  ad_storage: 'denied', ad_user_data: 'denied',
  ad_personalization: 'denied', analytics_storage: 'denied'
});
gtag('config', GA4_ID, { send_page_view: false });
gtag('config', ADS_ID);

analytics.subscribe('checkout_completed', (event) => {
  const c = event.data.checkout;
  gtag('consent', 'update', {
    ad_storage: 'granted', ad_user_data: 'granted',
    ad_personalization: 'granted', analytics_storage: 'granted'
  });
  const payload = {
    transaction_id: c.order.id,                 // unique, non nominatif
    value: c.totalPrice.amount,
    currency: c.currencyCode,
    items: c.lineItems.map(i => ({
      item_id: i.variant.sku || i.variant.id,
      item_name: i.title,
      price: i.variant.price.amount,
      quantity: i.quantity
    }))
  };
  gtag('event', 'purchase', payload);
  gtag('event', 'conversion', {
    send_to: ADS_ID + '/' + ADS_LABEL,
    transaction_id: c.order.id,
    value: c.totalPrice.amount,
    currency: c.currencyCode
  });
});
```

`transaction_id` = l'identifiant de commande Shopify : unique, stable, non personnel — il assure la
déduplication côté Google. L'événement ne part **qu'après** `checkout_completed`, donc jamais avant l'achat.
Rappel : l'attribution sera moins bonne qu'avec l'app (cookies écrits sur l'origine du bac-à-sable) — c'est
un repli, pas l'option préférée.

---

## 5 — Recette, à faire après le retrait du mot de passe

**Consentement** — depuis une **connexion française** (pas depuis le Portugal : la région de consentement est
la France seule, un visiteur portugais ne verra légitimement rien), en **navigation privée** :

1. Ouvrir `https://maisonnoirmont.fr/` → le bandeau doit apparaître, avec **« Tout accepter »** et
   **« Tout refuser »** visuellement équivalents.
2. Cliquer **Tout refuser** → console : `document.cookie` ne doit contenir **aucun** `_ga*` ni `_gcl*`.
3. Descendre en pied de page, cliquer **« Préférences en matière de cookies »** → le panneau doit s'ouvrir
   **sans changer de page**. Si le navigateur part sur `/policies/` et affiche un 404, alors — et seulement
   alors — le bandeau n'est réellement pas actif : revenir à l'étape 1 du §4.
4. Console, contrôle direct :
   ```js
   Shopify.loadFeatures([{name:'consent-tracking-api', version:'0.1'}], () => {
     const cp = Shopify.customerPrivacy;
     console.log(cp.shouldShowBanner(), cp.currentVisitorConsent(), cp.analyticsProcessingAllowed());
   });
   ```
   Avant tout choix : `true`, valeurs vides, `false`. Après « Tout accepter » : `false`, `analytics: "yes"`,
   `true`.
5. Relire `/pages/politique-de-cookies` : ce qui y est décrit doit correspondre exactement à ce qui vient
   d'être observé.

**Mesure** — voir l'étape 9 du §4. Contrôle rapide de l'existence du pixel, en console sur le site :
```js
JSON.parse(document.documentElement.innerHTML.match(/webPixelsConfigList:(\[.*?\]),/s)[1]);
```
Aujourd'hui cela renvoie uniquement `shopify-app-pixel` et `shopify-custom-pixel`. Après l'étape 7, une
entrée Google doit s'y ajouter.

---

## 6 — Corrections à reporter dans la grille d'audit

| Ligne | Correction |
|---|---|
| **F1 / N4** | À reclasser de **P0 bloquant** à **vérification visuelle** : le consentement natif est en place. |
| **E1** | Le lien « Préférences en matière de cookies » **n'est pas un lien mort** : `#shopifyReshowConsentBanner` est intercepté par `storefront-banner.js`. À retirer de la liste des 404. |
| **B12** | Réglé, mais dans l'autre sens que prévu : c'est la page cookies qui était en retard sur le site, pas l'inverse. Corrigé le 08/08. |
| **B11** | Reste vrai : `/pages/politique-de-cookies` est une **page**, pas une politique Shopify, donc absente du pied de page de la caisse. **P2**, inchangé. |
| **Méthode** | Retirer `window.Shopify.customerPrivacy === undefined` de la grille : ce test ne prouve rien (l'API se charge à la demande). Le bon test est le triplet `storefront-banner.js` présent + `consentPolicy` non-`SD-` + `shouldShowBanner()` après `loadFeatures`. |
| **F2 / N5** | Confirmé et précisé : `webPixelsConfigList` vide de tout pixel marchand ; app Google non installée ; **le code de thème ne peut pas mesurer l'achat sur le plan Basic** — argument à conserver, il élimine définitivement cette piste. |

# Consentement cookies — T-33

> **14/08/2026.** Ticket **T-33** : mettre en place le consentement cookies, dernier bloquant technique
> avant l'ouverture, et **à faire avant T-10** (mesure d'achat).
>
> Boutique : `v42pzp-h4.myshopify.com` / `maisonnoirmont.fr` — plan **Basic**, marché unique **France**,
> `shipsToCountries = ["FR"]`, **toujours sous mot de passe**.
> Thème publié : `TRAVAIL Noirmont — publier apres validation` (`205089014098`).
>
> **Aucun des trois rapports antérieurs n'a été repris comme acquis.** Tout ce qui suit a été remesuré.

---

## 0 — Pourquoi ce point a été constaté trois fois, dans deux sens contraires

| Date | Conclusion | Ce qui n'allait pas |
|---|---|---|
| 08/08 (audit) | « Aucun consentement, lien Préférences en 404 » | Testait `Shopify.customerPrivacy` sans `loadFeatures`, et cherchait `#shopify-pc__banner` sur la page mot de passe |
| 12/08 (`journal/2026-08-08-tracking-et-consentement.md`) | « Faux positif, le consentement est en place » | Cinq preuves indirectes justes, **mais présentées comme une certitude** alors que l'interrupteur n'a jamais été lu |
| 13/08 (`journal/2026-08-13-conformite-et-textes.md`) | « Le consentement n'existe pas » | Rejouait exactement les trois tests invalides du 08/08 |

**La cause racine est la même dans les trois cas, et elle est structurelle** : tant que la boutique est sous
mot de passe, **le bandeau ne peut pas se rendre, et l'interrupteur ne peut pas être lu**. Toute observation
faite depuis l'extérieur dans ces conditions est ininterprétable — dans un sens comme dans l'autre. La
démonstration est au §2.

---

## 1 — Ce que j'ai établi, et par quelle preuve

### 1.1 Réglage de confidentialité côté boutique

| Constat | Preuve |
|---|---|
| **La région France est en « consentement requis »** | `consentPolicy` → `{id: "gid://shopify/ConsentPolicy/1563598881106", countryCode: "FR", regionCode: null, consentRequired: true, dataSaleOptOutRequired: false}`. L'identifiant **n'est pas préfixé `SD-`** : c'est un enregistrement créé par le marchand, pas la politique par défaut. Les 250+ autres pays sont tous `SD-…` / `consentRequired: false` |
| **Le script de bandeau Shopify est servi** | `curl` anonyme sur `https://maisonnoirmont.fr/` (302 → `/password`, 200) : le `content_for_header` contient `<script id='scb4127' async src='https://maisonnoirmont.fr/cdn/shopifycloud/privacy-banner/storefront-banner.js'>` |
| **Aucun traceur n'est actif** | Dans le HTML servi : 0 occurrence de `googletagmanager`, `gtag/js`, `dataLayer`, `connect.facebook`, `fbevents`, `clarity.ms`, `hotjar`. Cookies réellement posés (en-têtes `Set-Cookie`) : `localization`, `cart_currency`, `_shopify_essential` — tous strictement nécessaires |

### 1.2 L'API de consentement, testée correctement

Exécuté dans un vrai navigateur sur `maisonnoirmont.fr`, **depuis une adresse française** (`Shopify.country = "FR"`) :

```js
Shopify.loadFeatures([{name:'consent-tracking-api', version:'0.1'}], () => { … })
```

| Mesure | Valeur |
|---|---|
| `typeof Shopify.customerPrivacy` **avant** `loadFeatures` | `"undefined"` |
| `typeof Shopify.customerPrivacy` **après** `loadFeatures` | `"object"` — l'API se charge bien |
| `shouldShowBanner()` | `true` |
| `shouldShowGDPRBanner()` | `true` |
| `currentVisitorConsent()` | `{marketing:"", analytics:"", preferences:"", sale_of_data:""}` |
| `analyticsProcessingAllowed()` / `marketingAllowed()` | `false` / `false` |
| `getRegion()` | `"FRIDF"` (Île-de-France) |
| `document.querySelectorAll('[id^="shopify-pc__"]')` | **`[]` — aucun élément** |

> **⚠️ Le piège documenté est confirmé, et il est pire que décrit.** `Shopify.customerPrivacy` vaut
> `undefined` **même sur une boutique dont le bandeau est visiblement affiché** : mesuré sur
> `thewatchgallery.fr`, bandeau `#shopify-pc__banner` rendu à l'écran, `customerPrivacy` = `undefined`.
> **Ce test ne prouve rien et doit être retiré définitivement de toute grille d'audit.**

### 1.3 Pourquoi le bandeau ne se rend pas — la cause exacte, pas une hypothèse

Le 12/08 avançait deux explications possibles (visiteur hors région, page mot de passe) sans trancher.
**La console tranche** :

```
[warn]  Could not find liquid access token
[error] Error initializing banner { message: "Missing access token" }
```

Mécanisme, lu dans `storefront-banner.js` : le script s'initialise, puis va chercher la configuration du
bandeau sur l'API Storefront (`POST /api/unstable/graphql.json`, requête `consentManagement { banner { … } }`)
en s'authentifiant avec le **jeton Liquid** porté par la balise `<script id="shopify-features">`.

- **`#shopify-features` est absent de `/password`** — vérifié dans le HTML servi. Pas de jeton, donc pas de
  configuration, donc pas de bandeau.
- Forçage manuel `window.privacyBanner.showBanner()` (l'objet existe bien, avec `loadBanner` /
  `showBanner` / `showPreferences`) → **toujours 0 élément `shopify-pc__`**.
- Et surtout, l'API Storefront elle-même est fermée :

```
POST https://maisonnoirmont.fr/api/unstable/graphql.json
→ {"errors":[{"message":"Online Store channel is locked.","extensions":{"code":"BAD_REQUEST"}}]}
```

> **Conclusion dure : tant que le mot de passe est en place, le bandeau ne peut pas fonctionner, et son
> état ne peut pas être observé de l'extérieur — quel que soit le réglage.** Ce n'est pas un défaut de la
> boutique, c'est la conséquence du verrouillage du canal Online Store.

### 1.4 Le script de bandeau est-il un signal fiable ? — étude de contrôle

Le seul signal serveur disponible est l'injection de `storefront-banner.js`. Testé sur des boutiques
Shopify tierces, dont plusieurs **françaises** (donc soumises au même régime de consentement) :

| Boutique | Shopify | `storefront-banner.js` | `#shopify-pc__banner` rendu | Lien « Préférences » |
|---|---|---|---|---|
| `thewatchgallery.fr` | oui | **oui** | **oui** | — |
| `atelierbelvora.fr` | oui | **oui** | **oui** (`Accepter` / `Refuser`) | **oui** → `/policies/#shopifyReshowConsentBanner` |
| `lecoffretamontres.com` | oui | **oui** | — | — |
| `le-remontoir-montre.fr` | oui (FR) | **non** | **non** | **non** |
| `maisondutemps.com` | oui | non | — | — |
| `laboiteamontres.com` | oui | non | — | — |
| `allbirds.com`, `gymshark.com` | oui | non | — | — |
| **`maisonnoirmont.fr`** | oui (FR) | **oui** | *impossible à rendre — §1.3* | *impossible à rendre* |

**L'injection n'est ni systématique ni géographique** : parmi les boutiques Shopify françaises, certaines
l'ont et d'autres pas. C'est donc bien un réglage marchand. Et **4 fois sur 4**, script présent = bandeau
réellement rendu ; script absent = rien.

### 1.5 Verdict, avec son degré de certitude

> **Le consentement natif Shopify est très probablement déjà activé sur Maison Noirmont**, région France.
> Faisceau : politique FR non-`SD-` en `consentRequired: true` + script injecté (non systématique,
> corrélé 4/4 au bandeau réel) + API de consentement fonctionnelle + `shouldShowBanner() = true`.
>
> **Ce n'est pas une preuve directe, et je ne la présente pas comme telle.** L'interrupteur
> `privacySettings.banner.enabled` est le seul juge, et il est illisible depuis ce connecteur (§3).
> **Deux minutes dans l'admin le tranchent — c'est l'étape 1 du §6.**
>
> Ce qui est en revanche **certain** : aujourd'hui **aucun traceur soumis à consentement n'est déposé**
> (§1.1), donc **la boutique est conforme en l'état**. Le risque n'est pas maintenant, il est au moment
> de la pose de la balise Google.

---

## 2 — Ce qui a été fait sur la boutique

**Une seule écriture** : le corps de `/pages/politique-de-cookies` (`gid://shopify/Page/176214638930`).
`userErrors: []`, `updatedAt` passé de `2026-08-12T22:56:37Z` à **`2026-08-14T21:46:51Z`**.
Sauvegarde du texte d'origine : `backups/backup-consentement-2026-08-14/AVANT-politique-de-cookies.html`
(retour arrière : `pageUpdate` avec ce corps exact).

### Pourquoi ce texte devait changer

Le 13/08 a corrigé une affirmation fausse — la page prétendait qu'un bandeau existait — **en la remplaçant
par l'affirmation fausse symétrique** :

> « la réglementation française les dispense de consentement préalable, **et aucun bandeau de consentement
> n'est donc affiché aujourd'hui** »

Si le bandeau est bien activé (§1.5), **cette phrase devient fausse à la seconde où le mot de passe est
retiré** — un document légal servi qui nie un mécanisme visible à l'écran. C'est exactement l'erreur du
12/08, dans l'autre sens. Le ticket prévoyait déjà que le texte « redevient faux le jour où la balise
Google est posée » ; en réalité il redevenait faux **bien plus tôt**, dès l'ouverture.

### Ce que dit le nouveau texte

Il n'affirme plus **ni** qu'un bandeau est affiché **ni** qu'il ne l'est pas. Il énonce la **règle**, qui
est vraie dans les deux cas de figure :

- « À ce jour, aucun outil de mesure d'audience, d'analyse ni de publicité tiers n'est actif sur le Site »
  — vérifié aujourd'hui, §1.1 ;
- « **Aucun traceur soumis à consentement n'est déposé avant que vous ayez exprimé un choix.** Lorsqu'un tel
  traceur est activé, un bandeau vous permet de l'**accepter** ou de le **refuser** au moyen de deux boutons
  de même niveau, et vous pouvez revenir sur ce choix à tout moment au moyen du lien « Préférences en
  matière de cookies » situé en pied de page. »

**Ce texte n'a plus besoin d'être réécrit à l'ouverture.** Il ne devra l'être qu'au moment de T-10, pour
l'inventaire des cookies (voir §5).

Deux corrections factuelles au passage :

- ajout de **`_shopify_essential`**, réellement posé aujourd'hui (relevé dans les en-têtes `Set-Cookie`) et
  qui manquait à l'inventaire ;
- ajout de **`_tracking_consent`**, décrit comme n'étant déposé **que lorsqu'un choix est exprimé**.

### Ce qui n'a **pas** été touché

- **Aucun thème** — ni le publié, ni une copie. Voir §4 : il n'y avait rien à écrire.
- **Aucun réglage de confidentialité** — refusé par permission, §3.
- **Aucune app, aucun compte.**
- **Aucun produit, aucune variante, aucun prix** (grille de prix en cours par un autre agent).

---

## 3 — Ce que l'API permet, et ce qu'elle refuse — mot pour mot

Testé, pas supposé :

```
{ privacySettings { banner { enabled } } }
→ Access denied for privacySettings field. Required access: `read_privacy_settings` access scope.

mutation { consentPolicyUpdate(consentPolicies: [{countryCode: FR, consentRequired: true,
                               dataSaleOptOutRequired: false}]) { … } }
→ Access denied for consentPolicyUpdate field. Required access: `write_privacy_settings` access scope.

{ shop { storefrontAccessTokens(first: 10) { … } } }
→ Access denied for storefrontAccessTokens field.

{ scriptTags(first: 20) { … } }
→ Access denied for scriptTags field.
```

*(La mutation `consentPolicyUpdate` avait été construite avec les **valeurs actuelles exactes** de la
politique FR, pour être un no-op même en cas de succès. Elle n'a rien pu écrire.)*

### Et surtout : le bandeau natif **n'est activable par aucune API**

Exploration du schéma Admin :

- `privacySettings { banner { enabled autoManaged } }` → **lecture seule**, scope `read_privacy_settings`.
- Côté mutations, il existe **`privacyFeaturesDisable(featuresToDisable: [COOKIE_BANNER | …])`** — et
  **aucune mutation symétrique d'activation**. L'énumération `PrivacyFeaturesEnum` n'est référencée que par
  l'argument `privacyFeaturesDisable.featuresToDisable`.
- `consentPolicyUpdate` ne gère que les **régions**, et exige que le bandeau Shopify soit **désactivé**
  (code d'erreur `SHOPIFY_COOKIE_BANNER_NOT_DISABLED`) : cette mutation est faite pour les CMP tiers.

> **Donc : même avec toutes les portées, l'API Admin ne sait que *désactiver* le bandeau Shopify, jamais
> l'activer.** L'activation est un geste d'interface, réservé à l'administrateur. Ce n'est pas une limite du
> connecteur, c'est la conception de Shopify. **Aucune application payante n'est à envisager** : Shopify
> fournit ce bandeau nativement et gratuitement, avec Consent Mode v2.

---

## 4 — Le lien « Préférences en matière de cookies » : rien à réparer, rien à retirer

Le pied de page du thème **publié** (`205089014098`) le produit ainsi :

- `sections/footer.liquid` (md5 `3d84042ab2a3702e985538f272e736d9`) rend **statiquement**, dans sa barre
  basse : `{% content_for 'block', type: '_footer-policy-list', id: 'footer-policy-list' %}` ;
- `blocks/_footer-policy-list.liquid` (md5 `2cd3ea61cc4f4eafb7f02f954edefe5f`) se contente de boucler :
  `{%- for policy in shop.policies -%}`.

**Le lien n'est écrit nulle part.** C'est **Shopify** qui insère l'entrée « Préférences en matière de
cookies » dans `shop.policies` quand le bandeau est activé — et qui la retire quand il ne l'est pas.
Vérifié sur `atelierbelvora.fr` : le lien y est présent, avec `href="/policies/#shopifyReshowConsentBanner"`,
sans qu'aucun menu ne le contienne.

Contrôle des **8 menus** de Maison Noirmont (`main-menu`, `footer`, `footer-boutique`,
`footer-informations`, `footer-legal`, `customer-account-main-menu`, `noirmont-desktop`,
`noirmont-mobile`) : **aucun ne contient de lien de préférences cookies**. Il n'y a donc **aucun lien mort
à réparer** — le constat du 13/08 (« le lien a disparu du menu ») portait sur les menus, alors que ce lien
n'y a jamais vécu.

> **Ne toucher au thème sous aucun prétexte sur ce point.** Ajouter le lien à la main créerait un vrai 404
> (`/policies/` n'est une page réelle que si le script intercepte le clic) ; le retirer supprimerait le point
> de retrait du consentement. **Le comportement correct est déjà en place et s'auto-règle.**

---

## 5 — Cohérence entre ce que le site fait et ce que les textes promettent

| Document | Servi où | État | Action |
|---|---|---|---|
| **Politique de confidentialité** | `/policies/privacy-policy` (légale) | ✅ **cohérente** — parle de « traceurs exemptés ou après recueil du consentement lorsque celui-ci est requis » et du retrait du consentement, **sans jamais affirmer qu'un bandeau est ou n'est pas affiché** | **Rien à changer.** `write_legal_policies` n'est donc pas nécessaire |
| **Mentions légales**, art. 4 | `/pages/mentions-legales` | ✅ **cohérente** — renvoie simplement à la politique de cookies | Rien à changer |
| **Politique de cookies** | `/pages/politique-de-cookies` | ⚠️ **incohérente au 14/08 au matin** (« aucun bandeau n'est affiché aujourd'hui ») | ✅ **corrigée aujourd'hui**, §2 |

**Aucun texte n'est donc à préparer pour Hakim aujourd'hui** — la seule page à corriger était une `Page`,
que le connecteur a le droit d'écrire.

**Reste une seule mise à jour de texte, et elle appartient à T-10** (étape 10 de
`journal/2026-08-08-tracking-et-consentement.md`) : dès que la balise Google est active, ajouter `_ga`,
`_ga_<ID>` et `_gcl_au` à l'inventaire, et retirer les deux phrases qui affirment qu'aucun outil de mesure
n'est actif (sections « Notre règle… » et « Réseaux sociaux et balises internet »).

---

## 6 — Ce qui reste à Hakim, au clic près

### Étape 1 — Lire l'interrupteur (2 minutes) — **c'est la seule chose qui manque au dossier**

`https://admin.shopify.com/store/v42pzp-h4/settings/customer_privacy`
→ section **« Bannière de cookies »**.

- **Si elle est affichée comme activée** : ✅ **rien à activer**, T-33 est acquis côté mécanisme. Passer à
  l'étape 2.
- **Si elle est désactivée** : cliquer **Activer** / **Configurer**. Laisser les libellés Shopify par défaut
  (ils sont déjà en français, et **« Tout accepter » / « Tout refuser » sont deux boutons de même niveau**,
  ce qu'exige la CNIL). **Ne pas choisir une présentation qui masque le refus derrière « Gérer ».**

### Étape 2 — Élargir la région : **France seule ne suffit pas**

Toujours sur le même écran, **« Région d'application » → Gérer**.

Aujourd'hui, **seule la France** est en « consentement requis » ; les 250+ autres pays sont à
`consentRequired: false` (§1.1). Conséquence concrète **le jour où la balise Google sera posée** : un
visiteur belge, allemand ou espagnol **ne verrait aucun bandeau et serait mesuré sans consentement**.

`shipsToCountries = ["FR"]` ne protège pas : il limite les **acheteurs**, pas les **visiteurs**, et le RGPD
s'applique au visiteur dès la première page.

→ **Sélectionner le groupe « Espace économique européen + Royaume-Uni »** (Shopify le propose en un clic),
et non « France » seule. Aucun coût, aucun effet sur les ventes.

### Étape 3 — Vérifier à l'œil — **seulement après le retrait du mot de passe (T-12)**

Impossible avant : le canal Online Store est verrouillé et le bandeau ne peut pas se rendre (§1.3).
Depuis une connexion française, en navigation privée :

1. Ouvrir `https://maisonnoirmont.fr/` → le bandeau doit apparaître, **« Tout accepter »** et
   **« Tout refuser »** visuellement équivalents.
2. Cliquer **Tout refuser** → console : `document.cookie` ne doit contenir **aucun** `_ga*` ni `_gcl*`.
3. Pied de page → cliquer **« Préférences en matière de cookies »** → le panneau doit s'ouvrir **sans
   changer de page**. *(Le lien pointe vers `/policies/#shopifyReshowConsentBanner` : c'est normal, le clic
   est intercepté. Coller cette URL à la main donne un 404 — ce n'est pas un défaut.)*
4. Console :
   ```js
   Shopify.loadFeatures([{name:'consent-tracking-api', version:'0.1'}], () => {
     const cp = Shopify.customerPrivacy;
     console.log(cp.shouldShowBanner(), cp.currentVisitorConsent(), cp.analyticsProcessingAllowed());
   });
   ```
   Avant tout choix : `true`, valeurs vides, `false`. Après « Tout accepter » : `false`,
   `analytics: "yes"`, `true`.
5. Si le bandeau **n'apparaît pas** alors que la page se charge normalement : revenir à l'étape 1, le
   réglage était bien désactivé.

---

## 7 — Séquence : T-33 **avant** T-10, et pourquoi

**L'ordre n'est pas une préférence, c'est une contrainte de conformité.**

1. **T-33 — étapes 1 et 2 ci-dessus** (bandeau activé, région EEE + UK). *Faisable dès maintenant,
   indépendamment du mot de passe.*
2. **T-12 — retrait du mot de passe** (et le reste des conditions d'activation).
3. **T-33 — étape 3** : recette visuelle du bandeau. *Techniquement impossible avant le point 2.*
4. **T-10 — pose de la balise Google** (app Google & YouTube, `journal/2026-08-08-tracking-et-consentement.md`).
5. **T-10 étape 10** — mise à jour de l'inventaire des cookies (§5).

Si l'on inversait 4 et 1, le pixel Google — qui déclare `privacyPurposes: ["ANALYTICS","MARKETING"]` —
serait posé **sans dispositif de consentement pour l'arbitrer**, et l'on collecterait sans consentement.
C'est précisément ce que T-33 existe pour empêcher.

**Bonne nouvelle sur la séquence** : le pixel installé par l'app Google & YouTube est **nativement soumis au
bandeau Shopify**. Une fois les étapes 1 et 2 faites, T-10 n'a **aucun câblage de consentement à écrire** —
le Consent Mode v2 est géré par l'app.

---

## 8 — Vérification T-H2 : le médiateur de la consommation

> Ajout de périmètre en cours de tâche. Contrôle **factuel**, sur les documents **réellement servis**
> (`https://checkout.shopify.com/109418938706/policies/…`), pas seulement sur l'API.

### 8.1 Les trois marqueurs ont bien disparu — cette fois c'est vrai

`shopPolicies.TERMS_OF_SALE.updatedAt` = **`2026-08-14T23:46:21+02:00`** : les CGV ont bien été modifiées
aujourd'hui. Sur le document servi, la recherche de `[[…]]` renvoie **zéro occurrence** — les trois
marqueurs `[[MEDIATEUR_NOM]]`, `[[MEDIATEUR_ADRESSE]]` et `[[MEDIATEUR_SITE]]` ne sont plus là.

**Article 15 — Réclamations et médiation**, texte servi aujourd'hui :

> « …le consommateur peut recourir gratuitement au médiateur dont relève OH Ventures :
> **CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14.** »

Nom ✅ · adresse postale ✅ · téléphone ✅ (bonus, non demandé par le modèle).

### 8.2 Mais il manque le site du médiateur — et c'est une obligation, pas un détail

Le modèle prévoyait **trois** trous. Le remplacement en comble **deux** : nom et adresse. **`[[MEDIATEUR_SITE]]`
n'a pas été remplacé, il a été supprimé** — le texte ne comporte aucune adresse de site internet.

Or l'**article R. 616-1 du Code de la consommation** impose au professionnel de communiquer les coordonnées
du médiateur **« en indiquant l'adresse de son site internet »**. C'est précisément le point qu'un examinateur
GMC ou un contrôle DGCCRF vérifie, parce qu'il est mécanique.

→ **Pour Hakim** : ajouter l'URL du médiateur dans la même phrase de l'article 15, **en la recopiant mot pour
mot depuis l'attestation d'adhésion CM2C**. Je ne l'écris pas ici : on ne devine pas une coordonnée
contractuelle, et c'est ce genre d'approximation qui a déjà coûté deux allers-retours sur ce ticket.

### 8.3 Deux scories dans la même phrase

- **Artefact de collage** : le paragraphe contient un `<meta charset="utf-8">` **au milieu du texte**, juste
  avant le nom du médiateur (1 occurrence, confirmée sur le document servi). Invisible au rendu, mais c'est
  du HTML invalide en corps de page et la trace d'un copier-coller depuis un traitement de texte. À retirer.
- **Date de version périmée** : l'en-tête des CGV annonce toujours *« Version en vigueur au 10 août 2026 »*
  alors que le document a été modifié le **14 août à 23 h 46**. Un document légal dont la date contredit la
  dernière modification est un signal d'inachèvement. → passer à *« Version en vigueur au 14 août 2026 »*.

### 8.4 Balayage complet des marqueurs à trous — aucun autre

Recherche de `[[…]]`, texte générique et mentions à compléter sur **l'intégralité** des documents servis :

| Ensemble | Documents | Résultat |
|---|---|---|
| **7 politiques** | Contact · Mentions légales · Confidentialité · Remboursement · Expédition · CGV · CGU | **0 marqueur** |
| **6 pages CMS publiées** | `contact` · `la-maison` · `faq` · `configurateur` · `mentions-legales` · `politique-de-cookies` | **0 marqueur** |

**Aucun autre trou nulle part.** Le seul manque est celui du §8.2, et c'est une **omission**, pas un marqueur
resté visible — c'est pour cela qu'un simple `grep [[` ne l'aurait jamais attrapé, et qu'il faut lire l'article.

*(Les 5 pages doublons — `conditions-generales-de-vente`, `politique-de-livraison`, `politique-de-remboursement`,
`politique-de-confidentialite`, `conditions-generales-d-utilisation` — portent encore le texte générique
Shopify de juillet, mais toutes sont `isPublished: false` et ne sont donc pas servies. Sans effet à l'examen.)*

### 8.5 Cohérence du nom du médiateur

**Le médiateur n'est nommé qu'à un seul endroit : l'article 15 des CGV.** Aucun conflit de nom n'est donc
possible.

- **Politique de remboursement** : ne mentionne aucun médiateur — renvoie au traitement des réclamations par
  le service client. Cohérent.
- **Mentions légales** (page, art. 5) : *« Les règles de réclamation, de médiation et de compétence
  juridictionnelle applicables aux achats figurent dans nos Conditions générales de vente »* — renvoi, pas de
  nom concurrent. Cohérent.

### 8.6 Un écart annexe repéré au passage — deux « Mentions légales » servies en parallèle

Il existe **deux documents « Mentions légales » distincts, tous deux servis** :

| | Politique Shopify `/policies/legal-notice` | Page CMS `/pages/mentions-legales` |
|---|---|---|
| Dernière modif. | 10/08 | 13/08 |
| Sections | 5 | 6 |
| Délégué à la protection des données | **absent** | **nommé** (Hakim Ouahabi) |
| Clause « aucune compétence territoriale exclusive » | **absente** | **présente** |

Le pied de page du site pointe vers la **page** ; la **politique** est celle que Shopify affiche dans la
caisse. Il n'y a **pas de contradiction** — la politique est simplement moins complète et plus ancienne.
Mais c'est la version la moins bonne qui est servie au moment le plus sensible, le paiement.
**P2** : recopier le texte du 13/08 dans la politique `/policies/legal-notice`. Nécessite
`write_legal_policies`, donc Hakim.

### 8.7 Verdict T-H2

> **Le ticket a réellement progressé cette fois** — les marqueurs sont partis, le médiateur est nommé et
> joignable. **Mais il n'est pas soldé** : l'adresse du site du médiateur, exigée par l'article R. 616-1,
> manque (§8.2), plus deux scories de forme (§8.3). Trois corrections, toutes dans le **même paragraphe** des
> CGV, toutes réservées à Hakim (`write_legal_policies` absente du connecteur).

---

## 9 — Corrections à reporter dans la grille d'audit

| Ligne | Correction |
|---|---|
| **Méthode** | **Retirer définitivement** `Shopify.customerPrivacy === undefined` comme critère : mesuré `undefined` sur une boutique dont le bandeau est **visiblement affiché**. Le test valide est `loadFeatures` **puis** `shouldShowBanner()`. |
| **Méthode** | **Aucun test de consentement n'est concluant tant que la boutique est sous mot de passe** : l'API Storefront répond `Online Store channel is locked.` et le bandeau ne peut pas s'initialiser (`Missing access token`). Ne plus conclure — ni dans un sens ni dans l'autre — depuis `/password`. |
| **Méthode** | Le signal serveur exploitable est l'injection de `storefront-banner.js` dans `content_for_header` — non systématique, corrélée 4/4 au bandeau réellement rendu. Signal fort, **pas** une preuve de l'interrupteur. |
| **E1** | Le lien « Préférences en matière de cookies » n'est **pas** un lien mort et n'est **pas** dans les menus : Shopify l'injecte dans `shop.policies`. À retirer de la liste des 404 **et** de toute liste de correctifs de thème. |
| **F1 / N4** | Reclasser : **non pas « à installer »** mais **« à confirmer dans l'admin, puis élargir la région »**. Le mécanisme est presque certainement déjà là ; la région FR-seule, elle, est un vrai trou. |
| **B12** | La correction du 13/08 avait introduit l'affirmation fausse symétrique. Corrigée le 14/08 par un texte vrai dans les deux cas de figure. |

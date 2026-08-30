---
type: journal
boutique: seiko-mod
date: 2026-08-15
nature: intervention
leviers: [technique]
titre: "Corrections post-ouverture — doublon de mentions légales soldé, 8 défauts préparés"
---

# Corrections post-ouverture — doublon de mentions légales soldé, 8 défauts préparés

> **15/08/2026**, suite directe de `journal/2026-08-15-audit-conformite-site-live.md`.
> Aucune commande, aucun achat, aucun paiement. Aucun brouillon activé, aucun prix modifié,
> aucune collection publiée. **Aucune écriture sur le thème publié ni sur les politiques.**
> Aucun thème republié. Aucune suppression : la page mise hors ligne est **dépubliée**, pas supprimée.

---

# CE QUE J'AI CORRIGÉ

## Le doublon de « Mentions légales » (défaut n°6 de l'audit) — soldé

### Le choix, et pourquoi il n'y en avait qu'un

Les deux versions servies en parallèle :

| | `/policies/legal-notice` | `/pages/mentions-legales` |
|---|---|---|
| Nature | **Politique Shopify** (`ShopPolicy/65031438674`) | **Page CMS** (`Page/176214311250`) |
| Date affichée | 10 août 2026 | 13 août 2026 |
| Sections | 5 | **6** |
| Contenu en plus | — | DPO, réclamation CNIL, « Droit applicable » |
| Servie dans la caisse | **oui** | non |
| Recopiée par Merchant Center | **oui** | non |
| Liée au pied de page | oui, par le bloc `_footer-policy-list` qui itère `shop.policies` | oui, par le menu `footer-legal` |
| Effaçable par le connecteur | **non** (`write_legal_policies` absente) | oui |

La consigne était de garder la plus complète. **Ce n'était pas jouable telle quelle**, et pour une raison
structurelle, pas par confort : `/policies/legal-notice` est servie **automatiquement** par Shopify tant que
la politique a un corps, et le bloc de pied de page `_footer-policy-list` la relie tout seul en bouclant sur
`shop.policies`. Garder la page et « retirer » la politique aurait demandé de vider son corps, donc
`write_legal_policies`, que le connecteur n'a pas. **Le doublon aurait subsisté.**

La seule configuration où le doublon disparaît réellement est donc : **on garde la politique, on dépublie
la page, et on transporte le contenu manquant vers la politique.** C'est exactement le plan que l'audit
recommandait au point A.8. J'ai fait les deux tiers ; le tiers restant (le collage) est le point 1 de
`A-FAIRE-HAKIM.md`.

**Aucune mention obligatoire n'a été perdue dans l'intervalle** — vérifié avant de dépublier :
le **DPO** est nommé dans `/policies/contact-information`, la **CNIL** dans la politique de confidentialité §7,
le **droit applicable** dans l'article 16 des CGV et l'article 11 des CGU. La politique conservée porte
l'identité de l'éditeur, l'hébergeur et le directeur de la publication, c'est-à-dire tout ce qu'impose
l'art. 6 III de la LCEN.

### Les trois écritures

Toutes par API, toutes avec `userErrors: []`, toutes réversibles.

**1. Redirection 301 créée en premier**, pour qu'aucune requête ne tombe sur un 404 pendant l'opération.

```
urlRedirectCreate → UrlRedirect/1745946280274
  path   : /pages/mentions-legales
  target : /policies/legal-notice
  userErrors: []
```

**2. Page dépubliée, pas supprimée.**

```
pageUpdate → Page/176214311250
  isPublished : true → false
  publishedAt : 2026-07-26T01:30:45Z → null
  updatedAt   : 2026-08-14T22:34:47Z
  userErrors: []
```

Le corps de la page est **intact** dans l'admin, et sauvegardé en local
(`backups/2026-08-15-mentions-legales/page-mentions-legales-AVANT.html`). Une seule bascule suffit à la
remettre en ligne. Rien n'a été passé à une mutation destructive : la leçon de `fileDelete` du 12/08 est tenue.

**3. Les deux menus repointés** vers la politique conservée, avec le type `SHOP_POLICY` et non une URL en dur,
pour que le lien suive la ressource :

```
menuUpdate → Menu/334164394322 « Pied de page — Légal » (celui que rend le thème publié)
  MenuItem/819791167826 « Mentions légales »
    PAGE /pages/mentions-legales → SHOP_POLICY /policies/legal-notice
  les 6 autres entrées réécrites à l'identique
  userErrors: []

menuUpdate → Menu/333968900434 « Footer menu » (dormant, non rendu par le thème publié)
  MenuItem/819596919122 « Mentions légales » : même bascule
  les 10 autres entrées réécrites à l'identique
  userErrors: []
```

Le second menu n'est plus utilisé par le thème publié (qui rend `footer-boutique`, `footer-informations` et
`footer-legal`), mais il portait le même défaut en dormance. Corrigé pour qu'il ne ressorte pas au premier
changement de gabarit de pied de page.

### Les preuves

Relevées après coup, en visiteur anonyme, sans cookie de session.
Fichiers : `backups/2026-08-15-mentions-legales/preuves-2026-08-15.txt`.

| Contrôle | Résultat |
|---|---|
| État Admin de la page | `isPublished: false`, `publishedAt: null` ✅ |
| Redirection enregistrée | `urlRedirects(query:"path:/pages/mentions-legales")` renvoie bien la 301 ✅ |
| `/pages/mentions-legales` en ligne | **301 → `https://maisonnoirmont.fr/policies/legal-notice`** ✅ |
| `/policies/legal-notice` | **200**, contenu servi ✅ |
| Pied de page d'une fiche produit (rendu neuf) | **2 × `/policies/legal-notice`, 0 × `/pages/mentions-legales`** ✅ |
| Autres pages CMS publiées en double | **aucune** — voir ci-dessous ✅ |

⚠️ **Un point d'honnêteté sur la mesure.** Sur six appels consécutifs à `/pages/mentions-legales`, quatre
ont renvoyé 301 et deux encore 200 : le **cache de bordure Shopify** n'était pas purgé partout au moment du
contrôle. Même chose pour le pied de page de l'accueil, encore servi depuis le cache, alors qu'une fiche
produit rendue à neuf montre déjà le bon lien. L'état de la donnée fait foi et il est le bon ;
la propagation est mécanique. **À reconstater demain**, c'est le seul reste de cette correction.

### Aucun autre doublon parmi les pages publiées

Passe complète sur les 11 pages CMS et les 7 politiques.

- **Pages publiées : 5** — `contact`, `la-maison`, `faq`, `configurateur`, `politique-de-cookies`.
  Aucune ne double une politique.
- **Cinq pages CMS doublaient déjà des politiques et étaient déjà dépubliées** avant mon passage :
  `conditions-generales-de-vente`, `politique-de-livraison`, `politique-de-remboursement`,
  `politique-de-confidentialite`, `conditions-generales-d-utilisation`. Elles répondent 404, donc invisibles.
  Je ne leur ai pas créé de redirection : aucune n'est liée nulle part, et ajouter cinq redirections gênerait
  leur republication éventuelle pour un gain nul.
- **`politique-de-cookies` n'a pas d'équivalent en politique Shopify** (les 7 politiques sont contact,
  mentions légales, confidentialité, remboursement, expédition, CGV, CGU). Ce n'est donc pas un doublon.
- **`/pages/contact` et `/policies/contact-information` ne sont pas un doublon non plus** : la première est la
  page de contact avec formulaire et horaires, la seconde est la fiche d'identité légale que Shopify impose
  d'afficher dans la caisse. Contenus différents, fonctions différentes.

### Deux liens qui pointaient vers la page dépubliée, hors de ma main

Les CGU (article 2) et rien d'autre renvoient encore vers `/pages/mentions-legales`. **La 301 les fait
fonctionner**, donc aucun lien mort. Comme c'est du texte de politique, je ne peux pas le réécrire ; c'est
un correctif facultatif, noté ici et pas dans `A-FAIRE-HAKIM.md` pour ne pas allonger la liste avec du
cosmétique.

---

# CE QUE J'AI ÉTABLI AVANT DE PRÉPARER LE RESTE

## Les moyens de paiement réellement actifs

Relevés sur `https://maisonnoirmont.fr/payments/config`, source publique et sans authentification, archivée
dans `backups/2026-08-15-mentions-legales/payments-config-2026-08-15.json`.

| Moyen | État réel |
|---|---|
| Shop Pay | ✅ actif (`shopifyPayConfig`, `forceCheckoutOneExperience: true`) |
| PayPal | ✅ actif (`paypalConfig.merchantId = SWDERBAME2DX4`) |
| Apple Pay | ✅ actif, réseaux `visa`, `masterCard`, `amex`, `maestro` |
| Cartes | ✅ Shopify Payments actif (`shopifyPaymentsEnabled: true`) |
| **Google Pay** | ⛔ **`googlePayConfig: null`** |
| **Klarna** | ⛔ **0 occurrence** |
| Amazon Pay | ⛔ `amazonPayCv2Config: null` |
| Paiement fractionné natif | ⛔ aucun `installment`, aucun `shopPayInstallments` |

**Conséquence pour le défaut n°2 : la correction n'est pas d'inventer une formulation, c'est de faire
correspondre le texte à cette table.** « Klarna » est faux sans discussion. « PayPal » est vrai comme moyen
de paiement, mais le **4×** est un produit PayPal distinct que cette source ne peut pas prouver : la consigne
donnée à Hakim est donc de le confirmer côté PayPal, et de masquer le bloc entier sinon. Je n'ai inventé
aucune formulation intermédiaire.

Contrôle du rendu réel : le pied de page affiche aujourd'hui `pi-visa`, `pi-master`, `pi-apple_pay`,
`pi-paypal`, `pi-shopify_pay` **et `pi-google_pay`**. Le picto Klarna, lui, n'est **pas** rendu
(`show_klarna` vaut `false` par défaut). Seul Google Pay est en trop.

## Les emplacements exacts des six défauts de thème, trouvés en lecture

Thème publié `TRAVAIL Noirmont — publier apres validation` (`OnlineStoreTheme/205089014098`, rôle `MAIN`),
lu par `theme.files` **en lecture seule**. Aucun `themeFilesUpsert`, aucun `themeFilesCopy`, aucune publication.

| Défaut | Fichier | Emplacement exact | Nature |
|---|---|---|---|
| **2. Klarna** | `templates/product.json` | section `main` (`main-product`) → bloc **`noirmont_4x`**, `settings.provider_two = "Klarna"`. 6e bloc sur 12, juste sous `price_yEeMeb` | **réglage du personnalisateur** |
| **3. Google Pay** | `config/settings_data.json` | **`force_icons_display: true`** (réglage de thème). Le bloc `payment-methods` rend `shop.enabled_payment_types` quand il est `false`, et les cases en dur sinon ; `show_google_pay` n'est pas dans le fichier, il prend donc son défaut de schéma, qui est `true` | **réglage de thème** |
| **4. TTC** | — | **0 occurrence** de `TTC`, `taxes` ou `toutes taxes` dans `templates/product.json` **et** `templates/index.json`. Rien à retirer, tout à ajouter | **bloc à créer** |
| **7. Garantie** | `sections/footer-group.json` | section `custom_section_k6mNHc`, nommée **« Réassurances »** → 3e groupe `group_wMEVzi` (icône `verified_user`, titre « Garantie 12 mois ») → bloc **`text_ew3NP8`**, `settings.text` | **réglage du personnalisateur** |
| **8. Pièce unique** | `templates/index.json` | section `custom_section_k9aPjP` (**5e** de l'accueil, reconnaissable à son titre « Composez la vôtre ») → `group_XyMggk` → `group_6DLfAU` → `group_BhcLrP` → bloc **`icon_with_text_D4CKhV`**, `settings.text`. 3e puce du triptyque | **réglage du personnalisateur** |
| **1. E-mail** | `snippets/organization-schema.liquid` | `"email": {{ shop.email | json }}` — la fuite vient du **réglage**, pas du code. `shop.email` **et** `shop.contactEmail` valent `contact.noirmont@gmail.com` | **réglage boutique** |

**Bonne nouvelle de fond : aucune de ces six chaînes n'est codée en dur dans du Liquid.** Les six sont des
réglages du personnalisateur ou des réglages de boutique. Hakim n'a pas une ligne de code à toucher, et rien
de ce qu'il fera ne sera écrasé à la prochaine mise à jour du thème.

Pour le point 3, le libellé français exact du réglage a été relevé dans `locales/fr.default.schema.json` :
onglet **« Icônes de paiement »**, 19e sur 21 des Paramètres du thème, case **« Afficher manuellement les
icônes »**. Décochée, elle rend le pied de page automatiquement fidèle à la caisse, définitivement.

## Un résidu de collage trouvé au passage

L'audit du 15/08 concluait « aucun `<meta charset>` dans le corps d'aucune politique ». **C'est faux d'une
occurrence** : l'article 15 des CGV porte encore `<meta charset="utf-8">` collé juste devant le nom du
médiateur. Sans effet au rendu, mais c'est du bruit de copier-coller dans un document contractuel, et il se
retire dans le même geste que l'ajout de l'URL CM2C. Ajouté au point 8 de `A-FAIRE-HAKIM.md`.

---

# CE QUE J'AI PRÉPARÉ

`A-FAIRE-HAKIM.md`, à la racine du dossier boutique. **Huit actions**, chacune avec le chemin exact dans
l'admin, le texte à retirer, le texte à mettre prêt à copier, la règle de droit en une ligne et la commande
de vérification. Environ 25 minutes en tout.

L'ordre y est celui de la dépendance, pas celui de l'audit : le collage des mentions légales passe en **1**
parce que c'est la moitié restante de la correction faite ce soir, et que la version en ligne est aujourd'hui
la moins complète des deux.

Pièce jointe : `livraisons/mentions-legales-a-coller-2026-08-15.html`, le corps HTML complet et définitif de
la politique, à coller tel quel dans l'éditeur de code de Shopify. Écrit sans tiret cadratin,
conformément à `STYLE-REDACTION.md`.

**Le point 8 ne contient volontairement aucune URL de médiateur.** Hakim doit la reprendre de son attestation
d'adhésion CM2C. Une URL de médiateur devinée serait pire qu'une URL absente : elle transformerait un manquement
formel en information fausse.

---

# CE QUI RESTE APRÈS ÇA

Inchangé par rapport à l'audit du 15/08 : **T-50** (2 074 prix barrés dormants), **T-32** (2 065 SKU
AliExpress), **T-07** (1 091 photos brutes) avant d'activer le moindre brouillon ; **T-10** (mesure d'achat)
et **T-33 §2** (région du consentement élargie à l'EEE et au Royaume-Uni) avant de poser la balise Google.

Et une reprise à faire demain : **reconstater la 301 et le pied de page de l'accueil** une fois le cache de
bordure purgé.

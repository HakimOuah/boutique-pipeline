# Repasse de conformité n°2 — site live, visiteur anonyme

> **15/08/2026, midi.** Deuxième passe complète sur `maisonnoirmont.fr` après la série de corrections
> de Hakim. Tout est relevé **en visiteur anonyme** : `curl` sans cookie de session et navigateur
> intégré sur le domaine public. Aucune commande, aucun achat, aucune donnée de paiement, aucun
> formulaire soumis, aucun brouillon activé, aucun prix modifié, aucune collection publiée,
> aucune écriture sur le thème publié ni sur les politiques.
>
> Passe précédente : [`2026-08-15-audit-conformite-site-live.md`](2026-08-15-audit-conformite-site-live.md)
> et [`2026-08-15-corrections-post-ouverture.md`](2026-08-15-corrections-post-ouverture.md).

---

# VERDICT

## ⛔ PAS PRÊT pour l'ouverture d'un compte Merchant Center — mais il ne reste que 20 minutes de travail

Le dossier a beaucoup avancé. **Sept des huit actions de la liste de Hakim sont faites et vérifiées**,
et deux d'entre elles ont été mieux faites que ce que la consigne demandait (le bloc de paiement
fractionné est devenu un bloc dynamique avec seuil, au lieu d'être simplement masqué). Les six
bloquants publics du 15/08 au matin sont **cinq soldés sur six**.

Ce qui reste n'est plus de la dette : ce sont **six défauts précis**, dont **trois sont des
contradictions du site avec lui-même** — le motif de refus n°1 de Merchant Center, et celui qui
ne se plaide pas. Deux d'entre eux sont visibles **sur chacune des 120 pages publiques**.

**Un seul demande de toucher au code du thème** (deux lignes dans un fichier de blocs). Les cinq
autres sont des réglages, du texte de politique, ou une case.

---

## Les 6 défauts restants, par ordre d'urgence

| # | Défaut | Preuve | Chez qui |
|---|---|---|---|
| **1** | **Le pied de page se contredit sur le délai de réponse, à deux lignes d'écart** | Bloc « Une question ? » : *« généralement sous **24 h** ouvrées »*. Bloc du logo, juste en dessous : *« Nous répondons sous **48h** »*. Sur **toutes** les pages. | Hakim — personnalisateur |
| **2** | **Le même écart sur les 96 fiches produit, deux fois** | Cartes de confiance sous le prix : *« réponse sous **24 h** ouvrées »*. Accordéon « Contactez-nous » : *« généralement sous **24 h** ouvrées »*. Bloc « Besoin d'aide ? » de la même page : *« sous **48h** ouvrées »*. | Hakim — **code du thème** + personnalisateur |
| **3** | **Le pied de page n'a ni adresse postale ni raison sociale** | `text_hzJHEn` porte l'e-mail, le téléphone, les horaires et la mention TTC. **0 occurrence** de `OH Ventures`, `47 rue Vivienne` ou `75002` dans le pied de page, sur toutes les pages. Terry : *« Footer = GMC exactement (email, téléphone, adresse) »*. | Hakim — personnalisateur |
| **4** | **La garantie promise sur les fiches dépasse toujours le contrat** | Cartes de confiance : *« Garantie 12 mois — **Mouvement, couronne, aiguilles** »*, et l'accordéon « Garantie 12 mois » (deux fois par fiche) : *« garanti 12 mois : mouvement, **couronne, aiguilles** »*. La politique de remboursement §7 et l'art. 10 des CGV limitent au **mouvement interne** et **excluent** le bracelet, le verre et le boîtier. Le pied de page, lui, a bien été corrigé. | Hakim — **code du thème** + personnalisateur |
| **5** | **« Paiement en 4 fois » promis sur des fiches où le paiement fractionné est masqué** | Bandeau défilant `iwt_pdp5`, présent sur **toutes** les fiches, **y compris les 12,90 €** où le nouveau bloc dynamique se masque tout seul (seuil 30 €). Et le nombre « 4 » n'est prouvé nulle part : le bloc dynamique, lui, dit prudemment « en plusieurs fois ». | Hakim — personnalisateur |
| **6** | **La donnée structurée `Organization` de l'accueil est du JSON invalide** | Virgule finale après `"logo": …` avant l'accolade fermante : `json.loads()` échoue. **Google ignore alors le bloc entier** — donc l'adresse, l'e-mail et le nom qu'il porte. Cause : `snippets/organization-schema.liquid` met une virgule après chaque champ optionnel, et `sameAs` est vide faute de réseaux sociaux. Effet de bord : `shop.phone` étant vide, il n'y a **pas de `telephone`** dans le schéma. | Hakim — un champ à remplir suffit |

### Et deux écarts mineurs, notés sans être bloquants

- **Dates de version périmées** sur les politiques : les CGV ont été modifiées aujourd'hui (l'URL du
  médiateur y est), l'en-tête annonce toujours *« Version en vigueur au 10 août 2026 »*. Idem CGU,
  expédition, remboursement, confidentialité. Seules les mentions légales portent la bonne date.
- **Trois collections publiques sous le seuil de 5 produits** de la checklist Terry, dont deux dans
  le méga-menu : `frontpage` (1), `montre-squelette` (2), `plongeuses` (3).

---

# CE QUI A ÉTÉ CORRIGÉ PAR HAKIM — vérifié, pas cru

Chaque ligne a été recontrôlée en anonyme sur la page servie, pas sur l'intention.

| Action | État | Preuve relevée aujourd'hui |
|---|---|---|
| **1. Mentions légales complétées** | ✅ **FAIT** | `/policies/legal-notice` sert **6 sections**, « Dernière mise à jour : **15 août 2026** », avec le **DPO**, la **réclamation CNIL** et la section **5. Droit applicable**. La 301 depuis `/pages/mentions-legales` répond **301 sur 3 appels sur 3** — le cache de bordure est purgé, le reste de la correction d'hier soir est confirmé. |
| **2. E-mail de la boutique basculé** | ✅ **FAIT** | API Admin : `shop.email` = `shop.contactEmail` = **`contact@maisonnoirmont.fr`**. Le JSON-LD `Organization` de l'accueil publie `"email": "contact@maisonnoirmont.fr"`. **0 occurrence de `gmail`** sur l'ensemble des pages relevées. |
| **3. Klarna retiré du texte** | ✅ **FAIT** | **0 occurrence** de la chaîne « Klarna » en texte sur les 18 pages relevées. Le bloc `noirmont_4x` n'est plus dans `templates/product.json`. |
| **3 bis. Klarna réactivé en caisse** | ✅ **CONFIRMÉ** *(par une autre source que `/payments/config`)* | Le thème rend maintenant les icônes depuis `shop.enabled_payment_types`, et cette liste contient **`klarna`** aux côtés de `visa`, `master`, `american_express`, `apple_pay`, `paypal`, `shopify_pay`. C'est la liste des moyens que Shopify déclare accepter à la caisse. ⚠️ **`/payments/config` ne liste pas Klarna, et c'est normal** : cet endpoint n'expose que les portefeuilles accélérés (Apple Pay, Shop Pay, PayPal, Google Pay), pas les passerelles classiques. La source d'hier n'était donc pas fausse, elle était hors sujet pour Klarna. |
| **4b. Icônes de paiement fiabilisées** | ✅ **FAIT** | Le picto **Google Pay a disparu** de toutes les pages. Les 7 icônes rendues correspondent exactement à `shop.enabled_payment_types`. La case « Afficher manuellement les icônes » est donc décochée : l'affichage suivra tout seul à l'avenir. **Amex apparaît désormais**, l'écart en sens inverse est soldé. |
| **4a. Google Pay activé** | ⛔ **PAS FAIT** | `/payments/config` → `googlePayConfig: null`. **Ce n'est plus un mensonge** puisque le picto a disparu ; c'est devenu une simple opportunité (T-53). |
| **5a + 5b. Mention TTC** | ✅ **FAIT ET ÉTENDU** | « Prix TTC. Livraison offerte en France métropolitaine. » sous le prix des fiches, **et** « Tous nos prix sont affichés en euros, toutes taxes comprises. » dans le pied de page. Vérifié présent sur **l'accueil, le panier, `/collections/all` et les fiches**, y compris à 12,90 €. Art. L. 112-1 satisfait. |
| **6. Garantie du pied de page alignée** | ✅ **FAIT** *(mais partiellement)* | Le pied de page dit désormais *« Sur le mouvement, pendant 12 mois : on répare ou on remplace. »* ⛔ Les **trois autres emplacements** de la même promesse, sur les fiches, portent encore « couronne, aiguilles » — voir défaut n°4. |
| **7. « Pièce unique » retiré de l'accueil** | ✅ **FAIT** | **0 occurrence** de « pièce unique » et de « à votre image » sur l'accueil. La 3e puce dit maintenant *« Vous signez / la référence de notre catalogue qui correspond à vos réponses »*, mot pour mot comme la FAQ. |
| **8. URL du médiateur CM2C** | ✅ **FAIT** | Art. 15 des CGV : *« CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14, site internet : **https://www.cm2c.net/** »*. Art. R. 616-1 satisfait. |
| **8 bis. `<meta charset>` dans le corps de l'article 15** | ✅ **FAIT** | Passe sur les **7 politiques** et les **5 pages CMS** publiées : **0 `<meta charset>` dans un corps de document**. Le seul présent est celui du `<head>`. |
| **Délai 24 h → 48 h et horaires 18 h → 17 h** | 🟠 **FAIT À MOITIÉ** | ✅ **« 18 h » a totalement disparu** : 0 occurrence sur les 18 pages. ✅ Le pied de page, la page Contact et le bloc « Besoin d'aide ? » disent 48 h. ⛔ Trois textes disent encore 24 h — voir ci-dessous. |
| **Devise PayPal** | ✅ **FAIT** | `/payments/config` → `"currency":"EUR"`. `Shopify.currency = {"active":"EUR"}`. `priceCurrency: "EUR"` dans tous les JSON-LD produit, `currencyCode: EUR` × 12. **0 occurrence de `USD`, de `$` ou de « dollar »** sur l'accueil, le panier et les fiches. Aucun point du parcours ne facture en dollars. |
| **Doublon de mentions légales** | ✅ **CONFIRMÉ SOLDÉ** | Deux liens pointent encore vers `/pages/mentions-legales` (CGU art. 2 et politique de cookies) mais la **301 fonctionne** : aucun lien mort, aucun doublon servi. Correctif purement cosmétique, laissé de côté volontairement. |

---

# LE COMPTE EXACT DES « 24 h » — le grep mentait

Le contrôle rapide annonçait *« 18 occurrences de 24h contre 2 de 48h »* sur une fiche produit.
**Le chiffre brut est exact, la lecture ne l'était pas.** Contexte vérifié occurrence par occurrence :

| Ce que compte le grep | Nature réelle | Compte |
|---|---:|---:|
| `24` dans des attributs `<path d="…">` | **coordonnées de tracé SVG** des pictos de paiement (Visa, Mastercard, Amex…) | 15 |
| « l'aiguille GMT fait le tour du cadran en **24 heures** » | description technique juste, aucune promesse de délai | 2 |
| **Promesses de délai réellement servies** | **à corriger** | **3** |

C'est le même piège que celui déjà consigné le 15/08 au matin (`star`, `avis`, `compare-at`) :
**chercher une chaîne dans du HTML rendu produit surtout des faux positifs.** Le seul relevé qui fait
foi est le **texte visible**, script, style et SVG retirés.

## Les trois textes à corriger, et les trois qui sont déjà bons

| Emplacement | Texte servi aujourd'hui | Portée | État |
|---|---|---|---|
| Pied de page → « Réassurances » → **« Une question ? »** | « Notre équipe vous répond en français, généralement sous **24 h** ouvrées. » | **toutes les pages** | ⛔ |
| Fiche → **cartes de confiance** sous le prix | « contact@maisonnoirmont.fr · réponse sous **24 h** ouvrées. » | **96 fiches** | ⛔ |
| Fiche → accordéon **« Contactez-nous »** | « Une question avant de commander ? … généralement sous **24 h** ouvrées. » | **96 fiches** | ⛔ |
| Pied de page → bloc du logo | « Service client du Lundi au Vendredi de **9h à 17h**. Nous répondons sous **48h**. » | toutes les pages | ✅ |
| Fiche → bloc **« Besoin d'aide ? »** | « … généralement sous **48h** ouvrées. » | 96 fiches | ✅ |
| Page **Contact** (CMS) | « … du lundi au vendredi, généralement sous **48 heures ouvrées** » + « Horaires : du lundi au vendredi, **9h à 17h** (heure de Paris), hors jours fériés. » | 1 page | ✅ |
| Fiche **Carte cadeau** (description produit) | « réponse sous 24 h ouvrées » | 1 fiche | ✅ **corrigé par moi aujourd'hui** |

**À ne pas confondre avec un écart** : la politique d'expédition §3 et l'art. 6 des CGV disent
*« Les commandes sont habituellement préparées sous **24 à 48 heures ouvrées** »*. C'est le délai de
**préparation**, pas le délai de **réponse**. Les deux chiffres cohabitent sans se contredire, et il
ne faut surtout pas les uniformiser.

---

# CE QUE J'AI CORRIGÉ

Deux écritures, toutes deux par API, toutes deux avec `userErrors: []`, toutes deux relues en ligne.
Sauvegardes préalables dans `backups/2026-08-15-repasse-2/`.

### 1. `carte-cadeau-maison-noirmont` — `productUpdate`, `updatedAt 2026-08-15T10:28:21Z`

Le seul texte **produit** de la boutique qui portait encore le délai de 24 h. Une phrase, en fin de
description : *« Écrivez-nous à contact@maisonnoirmont.fr, réponse sous **24 h** ouvrées »* →
*« … sous **48 h** ouvrées »*. Le reste de la description est inchangé au caractère près.

✅ Vérifié : `/products/carte-cadeau-maison-noirmont.json` → `24 h ouvrées` = **0**, `48 h ouvrées` = **1**.

*Contrôlé au passage* : les quatre montants annoncés dans le texte (50, 100, 150, 300 €) correspondent
exactement aux quatre variantes publiées. Rien d'inventé.

### 2. Le tag `skx` retiré des 3 fiches Héritage — `tagsRemove`, `userErrors: []`

`heritage-vert-plongeuse-vintage-42`, `heritage-bleu-plongeuse-vintage-42`,
`heritage-bleu-nuit-plongeuse-vintage-42` portaient le tag **`skx`**, qui est une **référence de
modèle Seiko**. Les tags sont publics (`products.json`), ils partent au flux Shopping et ils créent
des URL de filtre indexables. C'est du vocabulaire de marque tierce sans aucune contrepartie : il ne
sert ni au client, ni au référencement, ni à la navigation. C'est la moitié sans arbitrage du
ticket C15.

✅ Vérifié en anonyme : les trois fiches servent `tags = ["plongeuses"]`.

**L'autre moitié de C15 n'a pas été touchée volontairement** : renommer « Bracelet Présidentiel » et
« bracelet Président » touche des titres SEO arbitrés le 13/08 et un mot que le marché utilise comme
descripteur de forme. C'est un arbitrage de positionnement, pas une correction de conformité — il est
posé dans `A-FAIRE-HAKIM.md` avec la proposition de libellé, pas exécuté.

**Rien d'autre n'a été touché** : aucun prix, aucun statut, aucun média, aucune collection, aucun
thème, aucune politique, aucun réglage.

---

# CE QUI EST PROUVÉ CONFORME AUJOURD'HUI

## Le nouveau bloc de paiement fractionné — bien conçu, et le seuil fonctionne

`livraisons/bloc-paiement-fractionne.liquid`, collé dans un bloc « Liquid personnalisé » du gabarit
produit (`templates/product.json` → `sections/main/blocks/custom_code_7mKV34`). Trois contrôles :

| Contrôle | Résultat |
|---|---|
| **Le bloc s'affiche-t-il ?** | ✅ Oui, sous le prix. Texte servi : **« Paiement en plusieurs fois avec Klarna et PayPal »**. |
| **Quels logos ?** | ✅ **Klarna et PayPal**, et eux seuls. Les logos viennent de `shop.enabled_payment_types` : si Klarna est désactivé un jour, son logo disparaît tout seul. C'est exactement le garde-fou qui manquait au picto Google Pay. |
| **Le seuil de 30 € masque-t-il le bloc sur les petits prix ?** | ✅ **Oui, mesuré.** `barrettes-de-rechange-270` à **12,90 €** : **0 occurrence** de `mn-fractionne` dans le HTML servi. `montre-squelette-automatique-carree` à 279 € et `voyageur-or-gmt-president` à 378 € : bloc présent et visible (`offsetParent !== null`). |

⚠️ **Un cas limite, dans le bon sens.** Un seul produit public est à cheval sur le seuil :
`bracelet-jubile-embouts-courbes`, de 29,90 € à 39,90 €. Le bloc lit
`selected_or_first_available_variant.price`, soit 29,90 € : il reste **masqué** même si l'acheteur
choisit la variante à 39,90 €, et il ne se rallume pas au changement de variante (le bloc est rendu
côté serveur, sans JavaScript). **On promet moins que ce qu'on offre** : c'est le sens dans lequel
on veut se tromper. Rien à faire.

⚠️ **Le seul reproche est ailleurs** : le bandeau défilant continue d'annoncer « Paiement en **4** fois »
sur les mêmes fiches, y compris celles où ce bloc est masqué. Le bloc, lui, a la prudence de dire
« en plusieurs fois » sans avancer de chiffre. Voir le défaut n°5.

## Consentement cookies — toujours conforme, remesuré

| Contrôle | Résultat |
|---|---|
| Bandeau affiché à la première visite | ✅ `#shopify-pc__banner` présent |
| « Accepter » et « Refuser » de même niveau | ✅ **Strictement identiques** : **196 × 37 px** l'un et l'autre, même fond `rgb(255,255,255)`, même couleur `rgb(51,51,51)`, même `font-size: 16px`, même graisse `400`, **aucun soulignement sur ni l'un ni l'autre**. Les deux liens soulignés (« Politique de confidentialité », « Gérer vos préférences ») sont distincts et de traitement identique entre eux. Exigence CNIL satisfaite. |
| Cookies posés avant tout choix | ✅ **2 seulement** : `localization`, `cart_currency` |
| Traceurs chargés | ✅ **Aucun** : `gtag` `undefined`, `dataLayer` absent, `fbq` `undefined`, `ttq` `undefined` |
| Scripts tiers | ✅ **Un seul**, `shop.app/checkouts/internal/preloads.js` — infrastructure Shopify, pas un traceur |

## Politiques et mentions obligatoires

- **7 politiques servies**, toutes en 200, cohérentes entre elles : rétractation **14 jours**
  (CGV art. 7, remboursement §1), remboursement **sous 14 jours** (CGV art. 7, remboursement §4),
  livraison **14 à 21 jours calendaires** (expédition §3, CGV art. 6), préparation **24 à 48 h ouvrées**,
  garantie commerciale **12 mois sur le mouvement interne**, exclusions identiques dans les deux textes.
  **Les mêmes chiffres partout** — c'est le point que Google vérifie ligne à ligne.
- **`/policies/terms-of-service` et `/policies/terms-of-sale` ne sont pas un doublon.** Question laissée
  ouverte par la passe précédente, tranchée : les CGU (11 articles) encadrent **l'usage du site**
  (accès, compte, usages interdits, propriété intellectuelle, liens tiers), les CGV (16 articles +
  annexe) encadrent **la vente**. L'art. 1 des CGU renvoie explicitement aux CGV, et l'art. 11 renvoie
  aux CGV pour la médiation et la compétence. **Aucun paragraphe commun, aucune contradiction.**
  Les deux doivent rester en ligne.
- **Encadré légal des garanties** reproduit intégralement à l'art. 8 des CGV, y compris l'amende civile
  de l'art. L. 241-5. **Annexe formulaire de rétractation** présente.
- **Identité complète** dans les mentions légales, les CGV art. 1 et `/policies/contact-information` :
  OH Ventures, SAS, capital 1 000 €, 47 rue Vivienne 75002 Paris, SIREN 103 157 251,
  SIRET 103 157 251 00010, RCS Paris, TVA FR55 103157251, directeur de la publication, DPO, hébergeur.
- **0 marqueur à trou** (`[[…]]`) sur les 7 politiques et les 5 pages CMS publiées.

## Catalogue

- **96 produits publics**, 883 variantes, **0 variante indisponible**, **0 produit en rupture**.
- **0 avis fabriqué, 0 note, 0 badge, 0 `aggregateRating`** dans le rendu. Aucune app d'avis.
  **Aucun Trustpilot** : 0 occurrence sur l'ensemble des pages.
- **521 / 521 images sur `cdn.shopify.com`**, **0 `alicdn`**. Aucune photo AliExpress brute.
- **`alt` descriptifs en français** sur les 50 premières fiches contrôlées une par une : aucun `alt`
  générique, aucun vide, tous nommant le modèle, la vue et le détail. Rien à réécrire.
- **0 compare-at price** sur les 883 variantes publiques (la purge T-50 du matin tient).
- Fourchette publique **12,90 € → 417,00 €**, cohérente avec la grille du 14/08.
  Montres automatiques : **239 € minimum**, ce qui valide le « dès 239 € » du titre et de la
  meta description de l'accueil.

## Technique

- **0 lien mort** : les 48 liens internes de l'accueil testés un par un. Les seuls non-200 sont un
  `/account` en 302 (normal) et trois polices en URL protocole-relative — l'artefact de script déjà
  identifié le 15/08, pas un vrai 404.
- **Les 13 collections du méga-menu répondent toutes en 200.** `montre-cadran-a-chiffres` sert bien
  5 produits ; c'est `cadrans-a-chiffres` qui est en 404, et **aucun lien n'y renvoie**.
- **Sitemap** complet : 97 produits, 5 pages, 14 collections, 1 blog. **robots.txt** normal.
- **HTTPS, HSTS** (`max-age=7889238`), `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`,
  CSP `block-all-mixed-content; frame-ancestors 'none'; upgrade-insecure-requests`.
- **Aucun `noindex`** sur les pages de politiques.
- **Aucun code de vérification Google résiduel** : 0 balise `google-site-verification`.
- **Vitesse** : TTFB 50 à 130 ms, page complète en 0,31 à 0,60 s sur l'accueil, une fiche et une
  collection. Rien à redouter du critère « score > 65 » de la checklist.

## Blocs dormants — toujours désactivés, toujours à surveiller

Recontrôlés dans le thème publié : **tous `disabled: true`**, aucun n'est rendu, aucun n'est visible.

| Bloc dormant | Contenu | Emplacement |
|---|---|---|
| Badge type Trustpilot | **« 4,8/5 · 1340 avis »** | `templates/product.json` → `reviews_badge_noirmont` ; `templates/index.json` → `reviews_badge_efW9wU` (« Excellent · 4,5 · 1340 avis ») |
| Étoiles de notation | `rating: 4.5`, `review_count: 123` | 4 emplacements, fiches et cartes produit |
| Sections d'avis | **12 témoignages écrits**, dont *« Numéro de suivi dès l'expédition, délai tenu… La garantie 12 mois a fini de me convaincre »* | `reviews_8P6xW3` (produit) et `reviews_rXFabc` (accueil) |
| **Fenêtre « Guide des tailles »** | **`Lorem ipsum dolor sit amet…`** en toutes lettres | `templates/product.json` → `product_form_grYQk6/product_variant_picker_xWC3wF/product-variant-popup/text_99rHbT` |

**Vérifié côté public** : 0 occurrence de ces textes dans le HTML servi. Ils deviendraient publics
**à la seconde** où une section serait réactivée dans le personnalisateur, sur une boutique à
**0 commande client**. C'est le risque le plus cher du dossier pour l'effort le plus faible :
ils ne servent à rien tant qu'il n'y a pas de vrais avis.

---

# LE DÉTAIL DES SIX DÉFAUTS

## 1 et 2 — 24 h contre 48 h

Localisations exactes, relevées en lecture seule sur le thème publié
(`OnlineStoreTheme/205089014098`, rôle `MAIN`, `updatedAt 2026-08-15T10:11:24Z`) :

| Texte | Fichier | Chemin exact | Nature |
|---|---|---|---|
| Pied de page « Une question ? » | `sections/footer-group.json` | section `custom_section_k6mNHc` (**« Réassurances »**) → **4e groupe** `group_x7TjnR` (icône `forum`) → bloc `text_wDwwwK` | réglage du personnalisateur |
| Fiche, accordéon « Contactez-nous » | `templates/product.json` | `sections/main` → `accordions_KKUaHK` → `accordion_contact` → `text_content` | réglage du personnalisateur |
| Fiche, cartes de confiance | **`blocks/noirmont-confiance.liquid`** | 4e carte, `<p>{{ block.settings.contact_email }} · réponse sous 24 h ouvrées.</p>` | ⚠️ **codé en dur dans le Liquid** |

Le troisième est le seul de tout le dossier qui demande d'ouvrir l'éditeur de code. C'est un bloc
maison (`noirmont-confiance`), il ne sera donc jamais écrasé par une mise à jour de thème.

## 3 — Le pied de page sans adresse ni raison sociale

Le bloc de texte du pied de page (`sections/footer-group.json` → section `footer` → `group_y4aNMX` →
`text_hzJHEn`) porte aujourd'hui, dans cet ordre : la baseline, les horaires, le délai de réponse,
l'e-mail cliquable, le téléphone, la mention TTC. **Il n'y a ni le nom de la société ni son adresse.**

La règle de Terry est littérale : *« Footer = GMC exactement (email, téléphone, adresse) »*. Un
examinateur qui ouvre une page au hasard doit trouver les trois au même endroit, et **au caractère
près** ce qui sera déclaré dans Merchant Center.

**Trois écritures différentes du même numéro cohabitent aujourd'hui** :

| Où | Forme servie |
|---|---|
| Pied de page | `Téléphone : 0756828094` — texte brut, **non cliquable** |
| Politiques, CGV, mentions légales | `+33 7 56 82 80 94` |
| Page Contact | lien `tel:+33756828094` |
| **Fiche adresse Shopify** | **champ téléphone vide** (`billingAddress.phone: ""`) |

Une seule forme doit survivre, et c'est celle des politiques : **`+33 7 56 82 80 94`**. C'est aussi
celle à déclarer dans Merchant Center. Le champ vide de la fiche adresse Shopify a une conséquence
directe, décrite au défaut n°6.

## 4 — La garantie, trois fois en trop

| Texte servi | Emplacement | Nature |
|---|---|---|
| « Garantie 12 mois — **Mouvement, couronne, aiguilles** : on répare ou on remplace. » | `blocks/noirmont-confiance.liquid`, 3e carte | codé en dur |
| « Chaque garde-temps est garanti 12 mois : mouvement, **couronne, aiguilles**. » | `templates/product.json` → `accordions_KKUaHK/accordion_garantie/text_content` | personnalisateur |
| idem, **une seconde fois sur la même page** | `templates/product.json` → `custom_section_LBJBG7/…/accordion_ePJYyi/text_nDYpUH` | personnalisateur |

Contre : politique de remboursement §7 et CGV art. 10, tous deux limités au **mouvement interne**,
tous deux excluant explicitement **le bracelet, le verre et le boîtier**. La FAQ est juste
(« 12 mois sur le mouvement »), le pied de page est désormais juste. Il ne reste que la fiche produit
— celle que l'acheteur lit avant de payer, et celle qu'un examinateur ouvre en premier.

Promettre plus que la garantie commerciale contractuelle est une garantie non conforme au sens de
l'art. L. 217-21 du Code de la consommation.

## 5 — « 4 fois » contre « plusieurs fois »

`templates/product.json` → section `marquee_pdp` → `marquee_main` → **`iwt_pdp5`**, texte
`<p>Paiement en 4 fois</p>`, icône `credit_card`.

Deux problèmes distincts sur la même ligne :

1. **Le chiffre n'est prouvé nulle part.** Klarna propose en France du « 3 fois » et du paiement
   différé à 30 jours ; le « 4× » est un produit **PayPal** distinct, ouvert compte par compte, et
   invisible en dehors d'une caisse réelle. Le bloc dynamique, lui, a la prudence de dire
   « en plusieurs fois » sans avancer de chiffre : les deux textes de la même page ne disent pas
   la même chose.
2. **Le bandeau ne connaît pas le seuil.** Sur `barrettes-de-rechange-270` à **12,90 €**, le bloc
   dynamique se masque correctement, mais le bandeau continue d'annoncer « Paiement en 4 fois » —
   là où aucun prestataire de paiement fractionné n'accepterait la transaction.

## 6 — Donnée structurée invalide

`snippets/organization-schema.liquid` écrit une virgule **après** chaque champ optionnel, et ferme
l'accolade sans rien derrière quand `sameAs` est vide. Comme aucun réseau social n'est renseigné,
le dernier champ écrit est `logo`, et il est suivi d'une virgule orpheline :

```json
"logo": "https://maisonnoirmont.fr/cdn/shop/files/logo-noirmont-encre.png?v=…&width=500",
}
```

`json.loads()` échoue. **Un bloc JSON-LD invalide est ignoré en entier**, donc l'adresse postale,
l'e-mail et le nom de l'organisation ne sont pas lus par Google — alors même qu'ils y sont, et qu'ils
sont justes depuis ce matin.

Deuxième effet, du même réglage : `{% if shop.phone != blank %}` ne passe jamais parce que
**le champ téléphone de la fiche adresse Shopify est vide**. Il n'y a donc **pas de `telephone`**
dans le schéma.

**Le remplir règle les deux problèmes d'un coup** : Google obtient le numéro, et le champ `telephone`
n'étant plus le dernier, il n'y a plus de virgule orpheline. C'est un champ de réglage, pas une ligne
de code.

---

# CE QUI RESTE APRÈS ÇA — inchangé

Rien de public, rien qui bloque l'ouverture du compte.

| Quoi | Chiffre | Ticket |
|---|---:|---|
| SKU AliExpress bruts sur les fiches non actives | **2 065** sur 84 brouillons et 9 archivées | **T-32** |
| Photos AliExpress brutes sur les brouillons | **1 091** sur 60 brouillons | **T-07** |
| Mesure d'achat (GA4 / balise Google) | **absente** — 0 traceur, confirmé en anonyme | **T-10** |
| Région du consentement à élargir à l'EEE + Royaume-Uni | invérifiable de l'extérieur, à faire **avant** la pose de la balise | **T-33 §2** |
| Carte cadeau à exclure du flux (4 SKU vides) | `product_type = Carte cadeau` | **T-35** |
| `identifier_exists: no` à déclarer au flux | aucun `gtin` ni `mpn` — normal pour une marque propre | **T-12** |

*(T-50 — les 2 074 prix barrés dormants — a été soldé et prouvé par scan paginé complet ce matin.
Je ne l'ai pas rejoué : le contrôle des 883 variantes publiques confirme 0 prix barré côté public.)*

---

# NOTES DE MÉTHODE

**Une source à requalifier.** `/payments/config` a été présenté hier comme *« la source faisant
autorité sur les moyens de paiement réellement actifs »*. C'est **vrai pour les portefeuilles
accélérés** (Apple Pay, Shop Pay, PayPal, Google Pay, Amazon Pay) et **faux pour les passerelles
classiques** : Klarna y est absent alors que Shopify le déclare accepté. La source à croiser est
**`shop.enabled_payment_types`**, que le thème rend maintenant directement dans les icônes du pied de
page depuis que « Afficher manuellement les icônes » est décochée. **Les deux ensemble donnent la
photo complète**, et le pied de page est devenu un témoin fiable qu'on peut lire en anonyme.

**Un quatrième faux positif à ajouter à la liste du 15/08.** Chercher `24h` ou `48h` dans du HTML
rendu compte les **coordonnées de tracé SVG** des pictos de paiement : 15 des 20 occurrences d'une
fiche produit. Toujours retirer `<script>`, `<style>` et `<svg>` avant de compter, et lire le contexte
de chaque occurrence restante.

**Un test à ajouter à la grille.** Passer chaque bloc `application/ld+json` servi à un parseur JSON
strict. Le bloc `Organization` de l'accueil est invalide depuis toujours, il est resté invisible à
trois audits successifs parce qu'il **s'affiche correctement à la lecture humaine**. Une virgule
suffit à faire disparaître toute la carte d'identité du marchand aux yeux de Google.

**Limites assumées.** La page de paiement n'a pas été ouverte (aucune commande, aucune donnée de
paiement — la présence de Klarna en caisse est établie par `shop.enabled_payment_types`, pas par une
lecture d'écran de la caisse) · la région du consentement reste invérifiable de l'extérieur ·
les `alt` ont été contrôlés sur 50 fiches sur 96 · les 2 065 SKU et 1 091 photos des brouillons n'ont
pas été rejoués, ils ne sont pas publics.

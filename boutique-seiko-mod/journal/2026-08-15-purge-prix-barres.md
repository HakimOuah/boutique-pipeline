# 15/08/2026 — Purge des 2 074 prix barrés dormants (T-50)

**Périmètre : les 105 fiches non actives de Maison Noirmont** — 95 brouillons et 10 archivées.
Décision de Hakim du 15/08 : **on purge tout, y compris ce qui n'est pas public**, parce qu'on ne sait
pas avec certitude ce que Merchant Center parvient à voir, et parce que le premier brouillon activé
arriverait en ligne avec son prix barré. Sur une boutique à **0 vente client**, un prix de référence
est injustifiable — c'est le motif de refus n°1.

**Aucun `price` touché. Aucun statut touché. Aucun brouillon activé.**

## Résultat en une ligne

**2 074 `compareAtPrice` remis à `null` sur 96 fiches** — 1 926 sur 86 brouillons, 148 sur les
10 archivées. **0 `userErrors`** sur 96 mutations aliasées réparties en 15 documents. Le scan paginé
complet des **3 009 variantes** rend ensuite **0 `compareAtPrice` non nul dans toute la boutique**,
prix inchangés partout et statuts identiques.

---

## 1. La sauvegarde préalable — faite avant toute écriture

Rien n'a été écrit avant cette étape. L'état complet a été exporté par `bulkOperationRunQuery`
(énumération complète côté Shopify, **pas** un `query:` filtré) :

| Fichier | Contenu |
|---|---|
| `backups/2026-08-15-prix-barres/bulk-raw.jsonl` | export brut **avant** écriture — 3 210 objets (201 produits + 3 009 variantes) |
| `backups/2026-08-15-prix-barres/avant.jsonl` | **2 074 lignes** — produit (id, titre, handle, statut), variante (id, titre), `price`, `compareAtPrice` : les seules variantes portant un prix barré |
| `backups/2026-08-15-prix-barres/prix-avant-tous.jsonl` | **3 009 lignes** — `price` + `compareAtPrice` de *toutes* les variantes, pour prouver après coup que rien d'autre n'a bougé |
| `backups/2026-08-15-prix-barres/bulk-raw-apres.jsonl` | export brut **après** écriture, même requête |
| `backups/2026-08-15-prix-barres/apres.jsonl` | les 2 074 lignes relues après écriture (`price_apres`, `compareAtPrice_apres`) |

C'est le même protocole que celui qui a permis de restaurer les 931 valeurs du 08/08 : **la valeur
d'origine de chaque prix barré est conservée ligne à ligne**, un retour en arrière reste possible.

### L'état d'entrée, mesuré et non repris de mémoire

| Statut | Fiches | Variantes | `compareAtPrice` non nuls | Fiches touchées |
|---|---:|---:|---:|---:|
| ACTIVE | 96 | 883 | **0** ✅ | 0 |
| DRAFT | 95 | 1 978 | **1 926** ⛔ | **86 / 95** |
| ARCHIVED | 10 | 148 | **148** ⛔ | **10 / 10** |
| **Total** | **201** | **3 009** | **2 074** | **96** |

Chiffres identiques à ceux relevés le 14/08 au scan de contrôle de la grille de prix : **rien n'avait
bougé dans l'intervalle**, ni en plus ni en moins.

**Contrôle de non-régression posé avant d'écrire** : les 883 prix actifs relus le 15/08 sont
**strictement identiques** à `backups/2026-08-14-prix/apres.jsonl` — 0 écart, 0 variante manquante.
La grille appliquée le 14/08 était intacte au moment où j'ai commencé.

---

## 2. L'écriture

- `productVariantsBulkUpdate` **aliasé** (`m0:`, `m1:`…), **une mutation par produit**, **96 mutations**
  réparties en **15 documents**, lots calibrés sur ≤ 250 variantes.
- **`userErrors` contrôlé à chaque appel : 0 sur les 15.**
- Le seul champ envoyé est `compareAtPrice: null`. **`price` n'apparaît dans aucune mutation**, ni
  `status`, ni titre, ni description, ni média, ni collection, ni option de variante.
- Les 10 fiches **archivées** acceptent la mutation sans traitement particulier — vérifié d'abord sur
  une seule fiche (`mouvement-nh35-japon`, 1 variante) avant de lancer les lots.

⚠️ **Piège de méthode reconfirmé** : les identifiants numériques nus sont refusés
(`Invalid global id '54213196480850'`). Il faut le `gid://shopify/…` complet, dans `productId` comme
dans chaque `variants[].id`. C'est ce qui rend ces purges verbeuses ; il n'y a pas de raccourci.

Les mutations `bulk` restant bloquées par la politique du connecteur, la voie aliasée est la seule
disponible — c'est celle de T-H3, et elle tient à cette échelle.

---

## 3. Les preuves

### 3.1 Scan paginé complet — la seule preuve qui compte

**Rappel du piège déjà payé** : `compare_at_price` **n'est pas un champ filtrable** sur
`productVariants`. Un `query:` est ignoré **silencieusement** et renvoie tout le catalogue, ce qui
donne l'illusion d'un contrôle. Seule une énumération complète fait preuve.

`bulkOperationRunQuery` relancée après écriture, même requête, **3 210 objets** :

| Contrôle | Attendu | Lu |
|---|---|---|
| Produits | 201 | **201** ✅ |
| Statuts | 96 actifs / 95 brouillons / 10 archivés | **96 / 95 / 10** ✅ |
| Variantes | 3 009 | **3 009** ✅ |
| Variantes par statut | 883 / 1 978 / 148 | **883 / 1 978 / 148** ✅ |
| **`compareAtPrice` non nuls, tous statuts confondus** | **0** | **0** ✅ |
| Écart de `price` sur les 3 009 variantes (avant → après purge) | 0 | **0** ✅ |
| Écart de `price` sur les 883 actives vs grille du 14/08 | 0 | **0** ✅ |

Le troisième contrôle est le plus important : il compare **toutes** les variantes de la boutique, pas
seulement celles que j'ai touchées. **Aucun prix n'a bougé nulle part**, ni sur les fiches purgées ni
sur les autres.

### 3.2 Contre-vérification indépendante par curseur

Scan `productVariants(first: 50, after: $cursor)` réellement paginé, page 1 : **50 variantes**, dont
**6 de brouillons** (`contre-la-montre-chronographe-panda`, `integrale-sport-chic-acier`,
`heritage-plongeuse-vintage-42`, `remontoir-bois`, `remontoir-collection`,
`rouleau-de-voyage-cuir`) — **`compareAtPrice: null` sur les 50**, prix conformes à la grille du
14/08 (279 €, 299 €, 329 €, 64,90 €…). Le chemin « bulk » et le chemin « curseur » disent la
même chose.

### 3.3 Lecture directe d'une archivée

`productByHandle("mouvement-nh35-japon")` → statut `ARCHIVED`, `price: 65.14`,
`compareAtPrice: null`. Le prix est bien resté à sa valeur.

---

## 4. Ce que cela débloque, et ce que cela ne débloque pas

**Débloqué** : la bombe à retardement de T-50 est désamorcée. Un brouillon activé demain n'arrivera
plus en ligne avec un prix barré, et n'en enverra pas un au flux Shopping.

**Toujours bloquant pour activer un brouillon** — rien de tout cela n'est réglé par cette purge :
**T-32** (2 065 SKU AliExpress bruts sur 84 brouillons et 9 archivés) et **T-07** (1 091 photos
AliExpress brutes sur 60 brouillons). Ces deux-là restent à faire avant toute activation.

**Point de vigilance permanent** : le thème porte un emplacement `compare-at-price-wrap` et un badge
« Économie » **vides et masqués par CSS**. C'est un gabarit dormant qui **s'allumera tout seul** au
premier `compareAtPrice` écrit, sans qu'on ait rien à activer. Toute réintroduction d'un prix barré,
même sur un brouillon, se verra le jour de l'activation.

---

## 5. Les moyens de paiement — les faits, sans rien activer

Hakim demande s'il vaut mieux **activer** Klarna et Google Pay plutôt que retirer leur mention des
fiches. **Je n'ai rien activé** : cela relève des réglages de compte et de son autorisation.

### 5.1 Ce qui est réellement actif — source publique `/payments/config`

Relevé le 15/08, HTTP 200 sur `https://maisonnoirmont.fr/payments/config` :

| Clé | Valeur lue | Ce que ça dit |
|---|---|---|
| `applePayConfig` | objet complet, `shopifyPaymentsEnabled: true` | **Apple Pay actif**, et **Shopify Payments est actif** |
| `applePayConfig.supportedNetworks` | `visa, masterCard, amex, maestro` | les 4 réseaux de cartes |
| `shopifyPayConfig` | objet complet | **Shop Pay actif** |
| `paypalConfig` | `environment: production`, `merchantId: SWDERBAME2DX4` | **PayPal actif** |
| **`googlePayConfig`** | **`null`** | ⛔ **Google Pay n'existe pas à la caisse** |
| `amazonPayCv2Config` | `null` | Amazon Pay absent |
| **`offsiteConfigs`** | **`null`** | ⛔ **aucun prestataire tiers hors site installé** — c'est là qu'apparaîtraient Klarna, Alma, Oney, Scalapay |
| `dynamicCheckoutPrioritization` | `ShopifyPay, PayPal, ApplePay, AmazonPayCv2, GooglePay` | Google Pay est **listé dans l'ordre d'affichage mais sans configuration** : rien ne s'affichera |

Recoupé côté Admin API : `shop.paymentSettings.supportedDigitalWallets = ["SHOPIFY_PAY", "APPLE_PAY"]`.
**Google Pay n'est pas dans la liste des portefeuilles.** Et `shop.taxesIncluded = true` : les prix
*sont* TTC.

⚠️ `shopifyPaymentsAccount` est **refusé au connecteur** (scope `read_shopify_payments` absent) : je
ne peux pas lire l'état du compte Shopify Payments depuis l'API. Mais `shopifyPaymentsEnabled: true`
dans `applePayConfig` le prouve par ailleurs, sur une source publique.

**`offsiteConfigs: null` est le chiffre décisif** : il ne s'agit pas d'un Klarna « en attente » ou mal
configuré. **Aucun prestataire de paiement fractionné n'est installé sur cette boutique.**

### 5.2 Ce qui a changé sur le site depuis l'audit du 15/08 au matin

Vérifié en anonyme le 15/08, sur 6 fiches produit, l'accueil, le panier, `/collections/all` et la FAQ :

- ✅ **« Klarna » : 0 occurrence sur tout le site.** La mention « Ou 4 × X € avec PayPal **ou Klarna** »
  a bien disparu — le bloc « Paiement fractionné » n'existe plus dans `templates/product.json`.
- ✅ **« Prix TTC. Livraison offerte en France métropolitaine. »** est apparu sous le prix des fiches
  (`sections.main` → bloc **`text_BY7DbP`**). ⚠️ **Uniquement sur le gabarit produit** : 0 occurrence
  de « TTC » sur l'accueil, le panier, les collections et la FAQ.
- ⛔ **Une promesse de 4× a survécu ailleurs**, et l'audit du matin ne l'avait pas isolée : le bandeau
  défilant des fiches affiche **« Paiement en 4 fois »**, avec une icône de carte bancaire, à côté de
  « Livraison offerte en France » et « Garantie 12 mois ».
  **Localisation exacte** : `templates/product.json` → section **`marquee_pdp`** (type `marquee`) →
  bloc `marquee_main` → sous-bloc **`iwt_pdp5`**, réglage `text`.
  **Aucun prestataire ne l'assure** (`offsiteConfigs: null`). C'est la même faute que « ou Klarna »,
  déplacée d'un bloc à l'autre — et elle est **publique**.
- ⛔ **Le picto Google Pay est toujours rendu**, sur l'accueil, les fiches, le panier, les collections
  et la FAQ (`aria-labelledby="pi-google_pay"`), alors que `googlePayConfig` est `null`. La liste
  affichée est : `apple_pay, google_pay, master, paypal, shopify_pay, visa`.

### 5.3 Activable tout de suite par Hakim, contre ce qui demande une candidature

**Groupe A — une case à cocher, effet immédiat, aucun tiers à convaincre**

- **Google Pay.** C'est un **portefeuille de Shopify Payments**, et Shopify Payments est déjà actif sur
  la boutique. Il se coche dans *Réglages → Paiements → Shopify Payments → Gérer → Portefeuilles*.
  Pas de dossier, pas d'instruction, pas de validation d'un tiers : `googlePayConfig` cesse d'être
  `null` et le picto déjà affiché devient vrai.
  Apple Pay et Shop Pay sont déjà cochés — c'est exactement le même mécanisme.

**Groupe B — candidature et validation d'un fournisseur, délai non maîtrisé**

- **Klarna.** Ce n'est pas une case : il faut installer Klarna comme moyen de paiement supplémentaire
  et **Klarna instruit le dossier marchand** (identité de la société, SIREN, coordonnées bancaires,
  modèle de vente, volumes attendus). Klarna porte le risque de crédit à la place du marchand : c'est
  une décision d'octroi, pas un branchement technique. Compte des **jours à des semaines**, et
  **l'acceptation n'est pas acquise** — une boutique à 0 vente, sans historique et en dropshipping,
  est précisément le profil qui se fait examiner de près, voire refuser.
- **Le 4× PayPal.** Il ne se règle pas dans Shopify : c'est **PayPal** qui l'ouvre sur le compte
  marchand, selon sa propre éligibilité. Rien dans Shopify ne le déclenche, et rien depuis l'extérieur
  ne permet de vérifier s'il est ouvert. Le seul contrôle fiable est d'aller au bout d'une caisse
  réelle et de regarder si l'option apparaît.
- Même logique pour les alternatives françaises (**Alma**, **Oney**, **Scalapay**) : dossier,
  instruction, décision du fournisseur.

⚠️ Je ne peux pas chiffrer honnêtement les délais du groupe B : ils dépendent du fournisseur et du
dossier. **Ce qui est certain, c'est qu'ils ne sont pas nuls et qu'ils ne dépendent pas de nous.**

### 5.4 Recommandation — et l'ordre dans lequel faire les choses

La question « activer plutôt que retirer » n'a pas la même réponse selon le moyen de paiement, parce
que **le délai n'est pas le même** :

**1. Google Pay : activer, ne pas retirer le picto.** C'est le seul cas où activer est strictement
meilleur. Zéro délai, zéro tiers, et le picto déjà affiché partout cesse d'être un mensonge dans le
même geste. Retirer le picto coûterait le même temps et supprimerait un moyen de paiement au lieu
d'en ajouter un. → **à faire aujourd'hui.**

**2. « Paiement en 4 fois » : retirer le texte maintenant, candidater ensuite, remettre après preuve.**
Et l'ordre compte, parce que **le texte est public pendant toute l'instruction du dossier** :

- Une candidature n'est pas une activation. Entre le dépôt et la réponse, le site continue de promettre
  un service qui n'existe pas — à des visiteurs réels, et à un examinateur Merchant Center qui peut
  passer n'importe quand.
- Si Klarna refuse — hypothèse sérieuse sur une boutique à 0 vente — la fausse promesse reste en ligne
  indéfiniment, et personne ne se souvient d'aller la retirer.
- Le coût de la promesse est asymétrique : elle se découvre **à la caisse**, au moment le plus cher du
  parcours. Un client venu pour le 4× qui ne le trouve pas ne revient pas.
- Annoncer un moyen de paiement inexistant relève de la pratique commerciale trompeuse
  (art. L. 121-2 du Code de la consommation), et c'est un motif de refus documenté côté Merchant Center.

**Donc : masquer `iwt_pdp5` maintenant** (Personnalisateur → gabarit Produit → bandeau défilant →
3e élément « Paiement en 4 fois » → *Masquer le bloc*). Si le bandeau doit garder trois éléments,
le remplacer par une promesse **vérifiable** — « Paiement sécurisé » ou « Retours sous 14 jours »,
toutes deux vraies aujourd'hui.

**Le remettre uniquement quand le 4× aura été vu fonctionner dans une vraie caisse**, en nommant alors
le prestataire réellement actif. Pas sur la foi d'un accord annoncé par e-mail : sur une caisse
observée.

**3. Ne pas candidater à Klarna maintenant.** Ce n'est pas le blocage du dossier. Les six défauts
publics de l'audit et les deux verrous d'activation (T-32, T-07) pèsent plus lourd qu'un moyen de
paiement supplémentaire, et une candidature déposée depuis une boutique encore imparfaite se présente
mal. À reprendre après l'ouverture Merchant Center, quand il y aura un historique à montrer.

**4. Ce que ça laisse ouvert, et qui n'est pas dans cette question** : la mention « TTC » n'existe que
sur le gabarit produit. L'accueil, le panier et les collections affichent des prix sans mention de
taxe (art. L. 112-1). Le picto Google Pay redevient légitime dès l'activation, mais **Amex et Maestro
sont acceptés sans être affichés** — écart mineur, dans l'autre sens, à traiter avec le reste des
icônes.

---

## 6. Ce qui reste ouvert

1. ⛔ **T-32** — 2 065 SKU AliExpress bruts sur 84 brouillons et 9 archivés. Bloque l'activation.
2. ⛔ **T-07** — 1 091 photos AliExpress brutes sur 60 brouillons. Bloque l'activation.
3. ⛔ **Masquer `iwt_pdp5` (« Paiement en 4 fois »)** — thème publié, pour Hakim. Public aujourd'hui.
4. 🟢 **Activer Google Pay** — une case, effet immédiat, pour Hakim.
5. ⚠️ **Mention « TTC » à étendre** hors du gabarit produit (accueil, panier, collections).
6. ⚠️ Les autres suites de T-H3 : coût DSers des 4 remontoirs bois, grille à corriger sur le GMT
   (417 € et non 419 €), paliers de l'Aviateur bronze.

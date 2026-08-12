# Pages légales + dates de livraison — Maison Noirmont

Date : 2026-07-26 · Boutique : `v42pzp-h4` / maisonnoirmont.fr
Source : pages légales publiques de **tufteo.com** (domaine confirmé depuis `boutique-tufting/project-state.md` — `letufting.fr` est un **concurrent**, pas une boutique de Hakim).
Lecture Tuftéo faite par le web public (navigateur intégré). Aucun `switch-shop` utilisé : écriture Noirmont par l'API Admin uniquement.

---

## 1. Volet 1 — Pages créées

État initial : **aucune page légale** sur Noirmont. Aucune CGV publiée.

Tuftéo publie 6 pages légales (pas de page cookies dédiée). Les 6 ont été transposées + 1 page cookies dédiée assemblée à partir du texte cookies déjà présent chez Tuftéo (mentions légales §9/9.1/9.2 + liste des fichiers témoins de la politique de confidentialité) — **aucun texte inventé**.

| Page | Handle | ID Shopify | Source Tuftéo |
|---|---|---|---|
| Mentions légales | `mentions-legales` | Page/176214311250 | `/pages/mentions-legales` |
| Politique de confidentialité | `politique-de-confidentialite` | Page/176214573394 | `/pages/politique-de-confidentialite` |
| Politique de cookies | `politique-de-cookies` | Page/176214638930 | assemblée (voir ci-dessus) |
| Politique de remboursement | `politique-de-remboursement` | Page/176214540626 | `/pages/politique-de-remboursement` |
| Politique de livraison | `politique-de-livraison` | Page/176214507858 | `/pages/politique-de-livraison` |
| Conditions générales de vente | `conditions-generales-de-vente` | Page/176214475090 | `/pages/conditions-generales-de-vente` |
| Conditions générales d'utilisation | `conditions-generales-d-utilisation` | Page/176214606162 | `/pages/conditions-generales-d-utilisation` |

Toutes publiées (`isPublished: true`).

### Rattachement au menu
Menu **Footer menu** (`gid://shopify/Menu/333968900434`) — les 4 entrées existantes conservées (FAQ, Contact, La Maison, Configurateur), les 7 pages légales ajoutées à la suite dans l'ordre Tuftéo : Mentions → Confidentialité → Cookies → Remboursement → Livraison → CGV → CGU.

### Contrôle des liens
Vérifié depuis la session Chrome de Hakim (le storefront est en **« Ouverture prochaine » / protégé par mot de passe**, donc invisible en anonyme) :
- 7 pages → **HTTP 200**, rendues par le thème, titre correct.
- **0 occurrence résiduelle de « tufteo »** sur l'ensemble des 7 pages.
- **0 lien interne mort** (tous les `/pages/...` croisés entre CGV, CGU, confidentialité, cookies, remboursement, livraison répondent 200).
- Liens du pied de page présents et pointant sur les bons handles.

---

## 2. Substitutions effectuées

| Élément Tuftéo | Remplacé par |
|---|---|
| Tuftéo (marque) | Maison Noirmont |
| tufteo.com | maisonnoirmont.fr |
| contact@tufteo.com | contact@maisonnoirmont.fr |
| Kits de tufting, pistolets, tondeuses, toiles, fils, accessoires (CGV art. 2) | Montres-bracelets (automatiques et quartz) · bracelets, boucles, fermoirs · écrins, rouleaux, remontoirs · outils et accessoires d'horlogerie |
| « France métropolitaine **et à l'international** » (CGV art. 8) | **France métropolitaine uniquement** (conforme à la zone d'expédition réelle : 1 seule zone, France) |
| Délai « 8 à 13 jours ouvrés » (CGV art. 8, CGU) | **14 à 21 jours** à compter de la validation de la commande |
| Délai « 5 à 9 / 6 à 10 jours ouvrés » (politique de livraison) | **14 à 21 jours** (total estimé) |
| Retour : « emballage, accessoires, notice » | « écrin, bracelet, maillons retirés, notice, films de protection » ; exclusions adaptées (portée, rayée, redimensionnée) |
| — (absent chez Tuftéo) | **Garantie commerciale 12 mois** sur le mouvement, ajoutée en CGV art. 11 et en politique de remboursement, **en sus** des garanties légales (conformité 2 ans / vices cachés) qu'elle ne remplace ni ne limite |
| « rubrique Suivi de commande » (page inexistante chez Noirmont) | « lien de suivi communiqué dans l'e-mail de confirmation d'expédition » |
| Paiement « Cartes bancaires + Paypal » | Cartes bancaires + « tout autre moyen de paiement proposé sur la page de paiement » (PayPal non vérifié sur Noirmont — pas d'affirmation) |
| Formulaire de rétractation « disponible sur le site » | « disponible en annexe des présentes » (pas de page formulaire chez Noirmont) |
| Adresse hébergeur Shopify (2 versions contradictoires chez Tuftéo : 151 O'Connor vs 150 rue Elgin) | Harmonisée sur **151 O'Connor Street, Ground Floor, Ottawa, Ontario, K2P 2L8, Canada** |

### Données d'entreprise reprises telles quelles (même entité juridique)
Reprises depuis les pages Tuftéo car il s'agit de la **même société** — et l'adresse concorde avec l'adresse de facturation Shopify de Noirmont (47 Rue Vivienne, 75002 Paris). **À confirmer par Hakim malgré tout** :

- Éditeur : **OH Ventures**, 47 rue Vivienne, 75002 Paris
- **SIRET 10315725100010** · **TVA FR55103157251** · capital 1000 €
- Téléphone **+33 7 56 82 80 94** (numéro OH Ventures utilisé par Tuftéo — vérifier si Noirmont doit afficher une ligne distincte)
- Responsable publication / webmaster / DPO : Hakim Ouahabi
- Hébergeur : Shopify Inc.
- Adresse de retour produits : OH Ventures, 47 rue Vivienne, 75002 Paris

---

## 3. ⚠️ Marqueurs laissés en attente de données de Hakim

| # | Où | Marqueur | Pourquoi non transposé |
|---|---|---|---|
| 1 | **CGV, art. 17 — Litiges** | `[À COMPLÉTER — nom, adresse et téléphone du médiateur auprès duquel Maison Noirmont a souscrit une adhésion. L'adhésion souscrite pour une autre boutique du groupe ne couvre pas ce site.]` | Tuftéo déclare **CM2C, 14 rue Saint Jean, 75017 Paris, 01 89 47 00 14**. Une adhésion médiateur est souscrite **par site**, pas par société : recopier CM2C pour Noirmont serait une déclaration fausse tant que l'adhésion n'est pas étendue. **Obligation légale (art. L612-1 C. consom.) — à traiter avant lancement.** |

C'est le **seul** marqueur du corpus. Points de vigilance complémentaires (pas des marqueurs, mais à trancher) :

- **Téléphone** : `+33 7 56 82 80 94` repris de Tuftéo. Confirmer ou remplacer.
- **E-mail de la boutique** : les pages annoncent `contact@maisonnoirmont.fr`, mais Réglages → Général porte encore **`contact.noirmont@gmail.com`**. À aligner, sinon les e-mails transactionnels partiront d'une adresse différente de celle publiée.
- **Réglages → Politiques** (liens du checkout) : seule la *Politique de confidentialité* existe, et c'est encore le **modèle générique Shopify**. Remboursement / CGV / Livraison / Conditions de service sont **vides** → le checkout n'affiche aucun lien vers nos CGV. Recopier les 7 pages ici (même situation que Tuftéo, laissée en option à Hakim).
- **PayPal** : à ajouter dans CGV art. 7 s'il est bien activé.

---

## 4. Volet 2 — Dates de livraison estimées

### Avant
Réglages → Expédition et livraison → **Dates de livraison estimées : `Automatisé`** (option « Recommandé » de Shopify). Shopify calculait ses propres dates d'arrivée à la caisse à partir de l'historique de traitement, sans connaître le délai fournisseur → risque de contradiction avec la promesse J+14/J+21 de la fiche produit.

Non modifiable par l'API Admin (aucun champ exposé sur `deliverySettings`) → fait dans l'admin via Chrome, **session existante de Hakim, aucun identifiant saisi**.

### Après
- **Dates de livraison estimées : `Désactivé`** ✅ (enregistré et vérifié : la ligne affiche « Désactivé »)
- Shop Promise : `Désactivé` (déjà le cas, non touché)
- Tarif d'expédition « Livraison offerte — suivie » (France, 0 €) : **Délai d'acheminement = `Aucun`** → aucune date Shopify n'est plus injectée à la caisse.
- Description du tarif alignée par API : `Livraison gratuite et suivie en France` → **`Livraison gratuite et suivie en France — comptez 2 à 3 semaines`**, pour reprendre mot pour mot la formulation de la fiche produit.

> Note : le délai d'acheminement Shopify se compte en **jours ouvrés**. Y saisir « 14 à 21 » aurait affiché 20 à 30 jours calendaires, donc **surestimé** notre promesse — d'où le choix de laisser `Aucun` et de porter la promesse dans le texte.

### Contrôle final de cohérence
| Emplacement | Délai annoncé |
|---|---|
| Fiche produit — bloc dates | « Livraison estimée entre le **9 août** et le **16 août** » (relevé le 26/07 = **J+14 / J+21**) ✅ |
| Fiche produit — texte | « Comptez généralement **2 à 3 semaines** » ✅ |
| Fiche produit — bloc livraison | « En France métropolitaine, avec suivi. Comptez généralement **2 à 3 semaines** après la commande. » ✅ |
| Panier / caisse | « Livraison offerte — suivie — **comptez 2 à 3 semaines** », plus aucune date auto ✅ |
| Politique de livraison | « Délai de livraison total estimé : **14 à 21 jours** » ✅ |
| CGV art. 8 | « délai estimé de **14 à 21 jours** » ✅ |
| CGU § Livraison | « délai estimé de **14 à 21 jours** » ✅ |

**Une seule promesse partout : 14 à 21 jours = 2 à 3 semaines.**

---

## 5. Réglages → Politiques (liens de la caisse) — fait le 26/07

L'API Admin refuse `shopPolicyUpdate` (scope `write_legal_policies` absent du connecteur) → fait dans l'admin via **Chrome, session existante de Hakim, aucun identifiant saisi**. Contenu injecté dans l'éditeur TinyMCE à partir du texte des pages créées.

| Politique Shopify | Source | État avant | État après |
|---|---|---|---|
| Politique de retour et de remboursement | page `politique-de-remboursement` | Aucune | **Publiée** |
| Politique d'expédition | page `politique-de-livraison` | Aucune | **Publiée** |
| Conditions de service | page `conditions-generales-d-utilisation` | Aucune | **Publiée** |
| Conditions de vente | page `conditions-generales-de-vente` | Aucune | **Publiée** (marqueur médiateur conservé tel quel) |
| Politique de confidentialité | — | **Automatisée (Shopify)** | **Inchangée** — voir arbitrage ci-dessous |

### Contrôle en caisse réelle (panier créé, aucune commande passée)
Pied de page de la caisse : **Politique de remboursement · Expédition · Politique de confidentialité · Conditions d'utilisation · Conditions générales de vente · Cookies**. Chaque entrée ouvre une modale ; contenu vérifié en ouvrant les modales une à une :

- **CGV** : notre texte (14 260 car.), « Maison Noirmont », « 14 à 21 jours », garantie 12 mois, **marqueur `[À COMPLÉTER]` médiateur bien présent**, 0 « tufteo ».
- **Remboursement** : notre texte, garantie 12 mois, 0 « tufteo ».
- **Expédition** : notre texte, « 14 à 21 jours » + « France métropolitaine uniquement ».
- **Conditions d'utilisation** : notre texte (SIRET présent), « 14 à 21 jours ».
- **Confidentialité** : **texte automatisé de Shopify**, pas le nôtre.

### ⚠️ Deux arbitrages laissés à Hakim (non tranchés seul)

**1. Doublon `/pages/` ↔ `/policies/`.** Shopify a généré ses propres pages publiques, désormais en ligne en plus des miennes. Contenu **identique** dans 4 cas :

| Page Shopify (caisse) | Page créée (pied de page du site) |
|---|---|
| `/policies/refund-policy` | `/pages/politique-de-remboursement` |
| `/policies/shipping-policy` | `/pages/politique-de-livraison` |
| `/policies/terms-of-service` | `/pages/conditions-generales-d-utilisation` |
| `/policies/terms-of-sale` | `/pages/conditions-generales-de-vente` |
| `/policies/privacy-policy` (texte Shopify) | `/pages/politique-de-confidentialite` (notre texte) — **contenus différents** |

Sans équivalent `/policies/` : `mentions-legales` et `politique-de-cookies` (`/policies/legal-notice` → 404).
**Je n'ai pas rebranché le menu de pied de page** : il pointe toujours sur `/pages/`. Deux options possibles — (a) rebrancher le footer sur les URL `/policies/` et dépublier les pages doublons, (b) garder `/pages/` au footer et accepter le doublon SEO. À trancher par Hakim.

**2. Politique de confidentialité : automatisée Shopify vs. la nôtre.** Je ne l'ai **pas** écrasée. Raison : elle était déjà définie et liée en caisse, et Shopify la met à jour automatiquement (RGPD, traitements Shopify) — l'écraser ferait perdre cette maintenance. Conséquence assumée : **deux textes de confidentialité coexistent** (caisse = Shopify, pied de page = le nôtre). À trancher : soit écraser par notre texte pour l'uniformité, soit rebrancher le footer sur `/policies/privacy-policy` et dépublier notre page.

**3. « Coordonnées » reste marqué `Obligatoire`** dans Réglages → Politiques (non renseigné). Non traité : hors du périmètre demandé, mais Shopify le signale comme obligatoire.

Le marqueur médiateur n'a été ni rempli, ni deviné, ni recopié depuis CM2C — dans la page comme dans la politique de caisse.

## 6. Consolidation : une seule version de chaque texte (arbitrages tranchés par le coordinateur)

Principe retenu : **la version servie par la caisse fait foi**. Les pages `/pages/` devenues doublons sont **dépubliées (pas supprimées)** — le texte reste disponible dans l'admin.

### Pied de page final (menu `footer`, volontairement mixte)
| Entrée | Cible | Nature |
|---|---|---|
| Mentions légales | `/pages/mentions-legales` | **Page conservée** (aucune politique Shopify correspondante) |
| Politique de confidentialité | `/policies/privacy-policy` | Politique (texte **automatisé Shopify**) |
| Politique de cookies | `/pages/politique-de-cookies` | **Page conservée** (aucune politique Shopify correspondante) |
| Politique de remboursement | `/policies/refund-policy` | Politique |
| Politique d'expédition | `/policies/shipping-policy` | Politique |
| Conditions générales de vente | `/policies/terms-of-sale` | Politique |
| Conditions générales d'utilisation | `/policies/terms-of-service` | Politique |

Les 4 entrées non légales (FAQ, Contact, La Maison, Configurateur) sont inchangées.

### Pages dépubliées (texte conservé, `isPublished: false`)
`politique-de-confidentialite` · `politique-de-remboursement` · `politique-de-livraison` · `conditions-generales-de-vente` · `conditions-generales-d-utilisation` → renvoient 404 en public, ce qui est l'effet voulu ; **aucun lien du site ne pointe plus vers elles**.

> **Point d'interprétation signalé.** Le coordinateur listait les CGU à la fois dans les entrées à basculer sur `/policies/` (« conditions de service ») et dans celles à garder en page. La condition posée était « s'ils n'ont pas de politique correspondante chez Shopify » : les CGU **en ont une** (Conditions de service, publiée à l'étape 5), donc elles ont été basculées et la page dépubliée. Seuls mentions légales et cookies restent des pages — ils n'ont effectivement aucun équivalent Shopify (`/policies/legal-notice` → 404).

### Confidentialité
Version **automatisée Shopify conservée**, notre texte transposé de Tuftéo **dépublié**. Motif retenu : la version Shopify suit la réglementation et reflète les traitements réels (applications et intégrations comprises), là où le texte repris de Tuftéo est figé et issu d'une autre activité.

### Liens internes réécrits
Les politiques renvoyaient encore vers les pages dépubliées. Corrigés dans l'admin (remplacement ciblé, texte inchangé par ailleurs) : **remboursement 1 lien, expédition 1, conditions de service 6, conditions de vente 1 → 0 lien `/pages/` résiduel**. La page cookies conservée pointait vers l'ancienne page de confidentialité → rebranchée sur `/policies/privacy-policy`.

### « Coordonnées » (était marqué *Obligatoire*, vide)
Renseigné avec **exactement** les données déjà publiées dans les mentions légales : Maison Noirmont / OH Ventures, 47 rue Vivienne 75002 Paris, contact@maisonnoirmont.fr, +33 7 56 82 80 94, SIRET 10315725100010, TVA FR55103157251, capital 1000 €, responsable publication et DPO Hakim Ouahabi. **Aucun marqueur nécessaire** : toutes ces données figuraient déjà aux mentions légales, rien n'a été inventé.

### Contrôle final (caisse réelle + storefront, pas sur la réponse des mutations)
- **11 liens du pied de page → 200**, aucun 404.
- **8 documents servis → 200** (2 pages conservées + 6 politiques).
- **0 lien interne mort** dans les pages conservées et dans les politiques. Seule exception : `/policies/#shopifyReshowConsentBanner`, l'ancre « Préférences en matière de cookies » **injectée par Shopify** (rouvre la bannière en JS, ne navigue pas) — pas un de nos liens.
- Les 5 pages dépubliées renvoient 404 et **ne sont plus liées nulle part**.
- Pied de page de la caisse : Remboursement · Expédition · Confidentialité · Conditions d'utilisation · CGV · **Contact** · Cookies.
- Modale CGV en caisse : notre texte (14 260 car.), « 14 à 21 jours », garantie 12 mois, **marqueur `[À COMPLÉTER]` médiateur intact**, **aucune mention CM2C**, 0 « tufteo ».
- `/policies/contact-information` : SIRET, adresse et e-mail bien présents.
- **0 commande** sur la boutique.

**Le seul point encore ouvert reste le médiateur de la consommation** (section 3), à fournir par Hakim avant lancement.

## 7. Interdits respectés
Aucun produit, SKU, prix, variante, média ni mapping DSers touché. Thème publié « Helio » **non modifié** (aucune écriture thème). Aucune commande, aucun achat, aucune application installée. Aucun `switch-shop`.

Incident sans conséquence : un dialogue « Ajouter une option d'expédition » s'est ouvert par erreur d'un clic dans l'admin ; refermé sans saisie ni enregistrement. Vérifié par API : **1 seul tarif** dans la zone France, inchangé.

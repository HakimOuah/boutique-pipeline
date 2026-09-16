# Audit Merchant Center — Bercelou (bercelou.com) — 16/09/2026

Audit en **lecture seule** : rien n'a été écrit sur Shopify, rien n'a été soumis ni envoyé.
Sources : site public (curl, thème **en ligne**), JSON publics (`/products.json`, `/collections/*/products.json`, `/payments/config`), API Admin en lecture (boutique, 129 produits, profils de livraison, moyens de paiement), images produits téléchargées et regardées.
Référentiel : skill `gmc-acceptance` (checklist §6 + leçons Noirmont) et mémoire `sources-audit-conformite-boutique.md`.

Périmètre constaté : **29 produits actifs**, 86 brouillons, 14 archivés ; 14 collections ; 10 pages ; 6 politiques.

**Non vérifié (à faire par Hakim)**
- **Caisse en visiteur anonyme** : l'ouverture d'une caisse depuis le navigateur intégré a été refusée par le garde-fou. La liste réelle (carte, PayPal, Klarna, Apple Pay, Shop Pay) et le seuil minimal de Klarna restent à contrôler à la main.
- **Réglages Merchant Center** (livraison, délai de traitement, retours) : pas d'accès.
- **Trustpilot** : la page a répondu 403 à curl. Pas de verdict.
- **Adresse KYC** : 47 rue Vivienne est l'adresse de toutes les pages. Il faut vérifier qu'elle est identique aux justificatifs fournis à Google.
- **Ligne téléphonique** : vérifier que le +33 7 56 82 80 94 est une vraie ligne décrochée, pas de la VoIP.
- Le navigateur intégré était en **aperçu du thème brouillon** `bercelou-travail-footer-2026-09-16` (autre session). Je ne l'ai pas quitté. Tous les constats sur le thème viennent donc du thème **en ligne**, lu par curl.

---

## Synthèse

| Gravité | Nombre |
|---|---|
| Bloquant | 4 (dont 1 qui ne bloque que la publication du lot 2) |
| Important | 16 |
| Mineur | 12 |

### Bloquants
1. **Le nom du tarif affiché en caisse promet « expédition 24/48h »**, alors que toutes les pages annoncent un délai total de 3 à 10 jours ouvrés (7 à 15 pour les accessoires) et qu'aucune politique ne parle de 24/48 h.
2. **La barre du panier annonce « Plus que €30,00 EUR et la livraison est offerte ! »**, alors que la politique dit « Livraison GRATUITE, quel que soit le montant ».
3. **Le JSON-LD `Organization` de l'accueil déclare comme réseaux sociaux de Bercelou les comptes Facebook, YouTube et LinkedIn de l'éditeur du thème (`themefullstack`).** C'est une fausse identité lue par Google.
4. **(Lot 2, avant publication)** Les 100 brouillons et archivés ont un « prix barré » (`compareAtPrice`) rempli, en pratique le coût fournisseur, plus bas que le prix. Quatre brouillons ont aussi des prix non arrondis sous 20 €.

---

## 1. Identité et coordonnées

| # | Point | Statut | Preuve | Gravité | Correction proposée |
|---|---|---|---|---|---|
| 1.1 | OH Ventures nommé dans les CGV | PASS | `/policies/terms-of-service` : « Ce site web est exploité par OH Ventures » ; art. 20 « Bercelou édité par OH Ventures (SASU) », SIRET 10315725100010, TVA FR55103157251 | — | — |
| 1.2 | OH Ventures nommé dans les mentions légales | PASS | `/policies/legal-notice` : SASU, capital 1 000 €, RCS 103 157 251 Paris, SIRET 103 157 251 00010, président Hakim Ouahabi, hébergeur Shopify, CM2C avec URL `https://www.cm2c.net/` | — | — |
| 1.3 | OH Ventures nommé dans la politique de confidentialité | PASS (faible) | Une seule mention, dans le bloc Contact : « OH Ventures (SASU), 47 rue Vivienne… ». Le responsable du traitement est défini comme « Bercelou (le Site) » | Mineur | Dans `/policies/privacy-policy`, 1er paragraphe : « Bercelou, marque exploitée par OH Ventures (SASU), 47 rue Vivienne, 75002 Paris (“nous”)… ». Dernière phrase : « OH Ventures est responsable du traitement ». |
| 1.4 | Même adresse partout | PASS | « 47 rue Vivienne, 75002 Paris » dans le pied de page, Contact, Qui sommes-nous, les 5 politiques, le JSON-LD et l'adresse Shopify | — | Vérifier que c'est l'adresse du KYC Google. |
| 1.5 | Même e-mail partout | PASS | `contact@bercelou.com` partout (site, `shop.email`, `shop.contactEmail`, JSON-LD). Aucun Gmail, aucun `info@ohventures.fr`, aucun `assistance@shopify.com` | — | Note : DECISIONS du 15/09 citait `contact@bercelou.fr`. Le site utilise `.com` de façon homogène, et `bercelou.fr` ne résout pas. Utiliser la même adresse `.com` dans Merchant Center. |
| 1.6 | Une seule écriture du téléphone | **FAIL** | Trois graphies : « +33 7 56 82 80 94 » (pages, politiques, pied de page) ; « **07 56 82 80 94** » (bandeau de réassurance des 29 fiches, sous le bouton Ajouter) ; « **0756828094** » (JSON-LD `Organization.telephone` et adresse de la boutique dans l'admin) | Important | 1) Admin → Réglages → Détails de la boutique → adresse : téléphone « +33 7 56 82 80 94 », ce qui corrige aussi le JSON-LD. 2) Thème, bloc de réassurance de la fiche produit (`product.json`, bloc téléphone) : remplacer « 07 56 82 80 94 » par « +33 7 56 82 80 94 ». |
| 1.7 | Pied de page : adresse + `mailto:` + `tel:` | **FAIL** (partiel) | Le pied de page en ligne affiche le texte « contact@bercelou.com / +33 7 56 82 80 94 / OH Ventures, 47 rue Vivienne, 75002 Paris » **sans aucun lien** : ni `href="mailto:` ni `href="tel:` dans l'accueil | Important | Dans le nouveau pied de page en préparation : lien `mailto:contact@bercelou.com` et lien `tel:+33756828094`. |
| 1.8 | Page Contact : coordonnées cliquables + formulaire | PASS (partiel) | Adresse, e-mail et téléphone présents en texte. Formulaire complet (prénom, nom, téléphone, e-mail, message). Pas de lien `mailto:` ni `tel:` sur la page | Mineur | Rendre l'e-mail et le téléphone cliquables dans `pages/contact`. |
| 1.9 | Mentions légales : hébergement | PASS (ambigu) | « Créateur et hébergement du site : OH Ventures » puis « Hébergeur : Shopify Inc. » | Mineur | Remplacer le titre par « Éditeur et créateur du site : OH Ventures ». L'hébergeur reste Shopify. |
| 1.10 | Une seule page de mentions légales | PASS | Aucune page CMS en double. Les 10 pages : contact, faq, garantie-sav, 3 guides, livraison-retours, moyens-de-paiement, qui-sommes-nous, suivre-ma-commande | — | — |
| 1.11 | Médiateur nommé avec son URL | PASS | CM2C + `https://www.cm2c.net/` dans les mentions légales et les CGV ; `www.cm2c.net` sur la page Garantie et SAV | — | — |

## 2. Cohérence des chiffres (politiques ↔ pages ↔ fiches ↔ collections ↔ FAQ ↔ caisse)

| # | Chiffre | Statut | Preuve | Gravité | Correction proposée |
|---|---|---|---|---|---|
| 2.1 | Délai meubles : 3 à 10 jours ouvrés | PASS (site) | Politique d'expédition, CGV (2 fois), Livraison et retours, FAQ n° 7, Suivre ma commande, bandeau de pied de page, 24 fiches de meubles (bloc, accordéon, FAQ de fiche), date estimée « entre le 21 et le 30 septembre » cohérente au 16/09 | — | — |
| 2.2 | Délai accessoires : 7 à 15 jours ouvrés | PASS (site) | Mêmes sources. Fiches housse, plaid, coussin et repose-pieds : « 7 à 15 jours ouvrés », estimation « 25 septembre – 7 octobre ». `fauteuil-relax-pivotant` est aussi à 7 à 15 jours (exception annoncée par « sauf délai indiqué sur la fiche ») | — | Le bandeau de pied de page ne cite que « 3 à 10 jours pour les fauteuils ». Acceptable, mais y ajouter « 7 à 15 jours pour les accessoires » éviterait toute lecture partielle. |
| 2.3 | **Délai affiché en caisse** | **FAIL** | Admin, profil de livraison « Profil général », zone France, seul tarif : « **Livraison offerte - expédition 24/48h** », 0 € | **Bloquant** | Admin → Réglages → Expédition → Profil général → France : renommer le tarif « Livraison offerte » (sans délai), ou « Livraison offerte – 3 à 10 jours ouvrés (accessoires 7 à 15) ». Aligner le délai de traitement de Merchant Center sur la réalité. |
| 2.4 | **Gratuité de la livraison** | **FAIL** | Barre de progression du panier (thème en ligne, `cart-progress-bar`) : « Plus que €30,00 EUR et la livraison est offerte ! ». Politique : « Livraison GRATUITE, quel que soit le montant de votre commande » ; FAQ n° 6 : « sur l'ensemble du catalogue » ; tarif réel 0 € sans condition | **Bloquant** | Thème → en-tête du panier → bloc « Barre de progression » : le supprimer, ou le remplacer par un texte fixe « Livraison offerte en France métropolitaine ». Vérifier aussi le thème brouillon du pied de page s'il reprend `cart.json`. |
| 2.5 | Fenêtre de retour : 14 jours après réception | PASS | Politique de remboursement, CGV, Livraison et retours, FAQ n° 10, accueil, 29 fiches, bandeau | — | Régler la même valeur dans Merchant Center. |
| 2.6 | Frais de retour à la charge du client | PASS | Politique de remboursement, CGV, Livraison et retours, FAQ n° 11, accueil, fiches (« frais de retour à votre charge pour ce colis volumineux ») | — | Merchant Center : « le client paie le retour ». |
| 2.7 | Adresse de retour | FAIL (partiel) | Politique : « Nous vous communiquons alors l'adresse de retour ». Aucune adresse ni aucun pays de retour n'est publié | Important | Ajouter au moins le pays de retour, voire l'adresse si elle est stable, dans `/policies/refund-policy` et la page Livraison et retours. Reprendre la même information dans Merchant Center. |
| 2.8 | Délai de remboursement : 14 jours | PASS (petit écart) | « au plus tard 14 jours après la réception de l'article retourné » (politique, CGV, Livraison et retours, FAQ n° 12). La même politique ajoute : « Si plus de **15 jours ouvrables** se sont écoulés depuis l'approbation… » | Mineur | Dans `/policies/refund-policy`, remplacer par « Si vous n'avez pas reçu votre remboursement 14 jours après la réception de votre retour, contactez-nous ». |
| 2.9 | Colis abîmé : signalement sous 48 h | PASS | Politique d'expédition, politique de remboursement, Livraison et retours, FAQ n° 9, fiches | — | — |
| 2.10 | Garantie légale de 2 ans, sans garantie commerciale | PASS | Politique de remboursement, CGV (« Aucune garantie commerciale supplémentaire »), Garantie et SAV, FAQ n° 13, fiches (« Garantie légale de 2 ans »), bandeau | — | — |
| 2.11 | Délai de réponse du SAV | PASS | « Nous vous répondons sous 1 jour ouvré », du lundi au vendredi de 9 h à 18 h, partout | — | — |
| 2.12 | Paiement en 3 ou 4 fois | PASS (texte) / à vérifier (caisse) | « 3 fois avec Klarna ou 4 fois avec PayPal » : barre d'annonce, accueil, FAQ n° 17, Moyens de paiement, CGV, 29 fiches | Important | Vérifier en caisse que Klarna 3 fois apparaît bien. Voir 3.5 pour les petits prix. |
| 2.13 | Brouillons du lot 2 : délais par catégorie | **FAIL** (lot 2) | La politique classe les « **repose-pieds** » dans les accessoires à 7 à 15 jours. Les brouillons `repose-pieds-vintage-lin-beige`, `repose-pieds-banquette-polaire-grise`, `petit-repose-pieds-effet-lin-marron-clair`, `repose-pieds-cube-lin-creme-poche` et `repose-pieds-carre-velours-cotele` annoncent « 3 à 10 jours ouvrés ». Les poufs et tables d'appoint (3 à 10 jours) n'entrent dans aucune catégorie de la politique | Important (avant publication) | Soit ces brouillons passent à 7 à 15 jours, soit on réécrit la liste des catégories dans la politique d'expédition, les CGV, Livraison et retours, la FAQ n° 7 et Suivre ma commande : « meubles (fauteuils, poufs, repose-pieds, tables d'appoint) : 3 à 10 jours ; textiles (plaids, coussins, housses) : 7 à 15 jours ». Une seule règle, recopiée aux 5 endroits. |

## 3. Moyens de paiement (pied de page = caisse = politique)

| # | Point | Statut | Preuve | Gravité | Correction proposée |
|---|---|---|---|---|---|
| 3.1 | Pictogrammes du pied de page | PASS (sous réserve de la caisse) | Accueil en ligne, `aria-labelledby="pi-…"` (icônes automatiques, donc issues de `shop.enabled_payment_types`) : american_express, apple_pay, cartes_bancaires, klarna, master, paypal, shopify_pay, visa. **Pas de Google Pay** | — | — |
| 3.2 | `/payments/config` | PASS | `applePayConfig` rempli, `shopifyPayConfig` rempli, `paypalConfig` rempli, **`googlePayConfig: null`**, `currency: "EUR"`. Admin : `supportedDigitalWallets = [SHOPIFY_PAY, APPLE_PAY]`. Cohérent avec les pictogrammes (Klarna n'apparaît jamais dans ce JSON, c'est normal) | — | — |
| 3.3 | Page Moyens de paiement et CGV | PASS | Page : « VISA, Mastercard, American Express et Cartes Bancaires, ainsi que PayPal, Klarna, Apple Pay et Shop Pay ». CGV : « carte bancaire, PayPal…, Klarna…, Apple Pay ou Shop Pay ». Même liste que les pictogrammes | — | — |
| 3.4 | FAQ et bandeau : même liste | FAIL (incomplet) | FAQ n° 16 : « La carte bancaire, PayPal et Apple Pay » (sans Klarna ni Shop Pay). Bandeau du pied de page : « Carte bancaire, PayPal, Apple Pay, et paiement en 3 ou 4 fois » (sans Shop Pay) | Mineur | FAQ n° 16 : « Carte bancaire (Visa, Mastercard, American Express, CB), PayPal, Klarna, Apple Pay et Shop Pay ». Même liste dans le bandeau. |
| 3.5 | Paiement fractionné sous le seuil | **FAIL** probable | La fiche `housse-de-protection-rocking-chair` commence à **29 €** et affiche « Payez en 3 fois avec Klarna ou en 4 fois avec PayPal ». PayPal 4 fois commence à 30 € ; le minimum de Klarna 3 fois est à vérifier. Les variantes à 39 € (plaid, repose-pieds) sont aussi à contrôler | Important | Modèle de fiche : n'afficher la ligne « 3 ou 4 fois » qu'au-dessus du seuil réel (condition Liquid sur le prix), ou écrire « à partir de XX € ». |
| 3.6 | Caisse en visiteur anonyme | **NON VÉRIFIÉ** | Action refusée par le garde-fou | Important | Hakim : ajouter un produit à 179 € au panier en navigation privée, noter les boutons express et la liste de paiement, et vérifier que Klarna et PayPal 4 fois apparaissent. Refaire le test avec la housse à 29 €. |
| 3.7 | Mention TTC près des prix | **FAIL** | Aucune occurrence de « TTC » sur les fiches, les collections, l'accueil ou le panier. Seules les CGV disent « prix indiqués en euros TTC ». `shop.taxesIncluded = true` | Important | Thème → modèle de fiche (bloc prix) et panier : ajouter « TTC » ou « Taxes incluses », idéalement aussi sur les cartes produit. |
| 3.8 | Format des prix | Mineur | « €179,00 », « €30,00 EUR » (format anglais) | Mineur | Réglages → Marchés / Devise : format « {{amount_with_comma_separator}} € ». |

## 4. Produits actifs (29) — représentation trompeuse et conformité

| # | Point | Statut | Preuve | Gravité | Correction proposée |
|---|---|---|---|---|---|
| 4.1 | Marques tierces (OTAUTAU, WOLTU, JustEvo, HOMCOM, Garvee, VEVOR…) | PASS | Aucune occurrence dans les titres, descriptions, alt, tags, handles, `vendor` (= Bercelou partout), SEO ou noms de fichiers CDN des 29 actifs. JSON-LD `brand: Bercelou` | — | — |
| 4.2 | Photos fournisseur brutes | PASS | 0 URL `alicdn`. 173 images, toutes sur le CDN Shopify avec des noms maison (`<handle>-face.jpg`…) | — | — |
| 4.3 | Image partagée entre deux fiches actives | PASS | 0 URL CDN commune | — | — |
| 4.4 | Texte incrusté ou logo sur les images | PASS | Les 173 images ont été regardées : aucun texte, aucun logo, aucun badge. Seule une étiquette marron **vierge** sur l'assise de la chaise haute `chaise-a-bascule-enfant` | — | — |
| 4.5 | Prix barrés sur les actifs | PASS | `compareAtPrice` vide sur toutes les variantes actives | — | — |
| 4.6 | Avis, notes ou compteurs | PASS | Aucun avis public, aucune note, aucune urgence. Les 3 occurrences de « avis » par fiche sont « 14 jours pour changer d'avis » | — | — |
| 4.7 | Promesses invérifiables ou « contrôle qualité » | **FAIL** | Accueil : « **Chaque fauteuil est vérifié avant d'être retenu** » et « nous contrôlons ces points sur chaque modèle ». Qui sommes-nous : « notre équipe vérifie sa hauteur d'assise… ». Seuls 3 échantillons ont été commandés, et la vérification réelle se fait sur fiche | Important | Accueil, section « Notre méthode » : « Chaque fauteuil est sélectionné sur ses cotes : hauteur d'assise, accoudoirs, dossier, matière ». Qui sommes-nous : « nous sélectionnons chaque fauteuil d'après ses dimensions et sa matière ». |
| 4.8 | « Se relever facilement » | **FAIL** | Accueil : « Se relever facilement, même avec bébé dans les bras » et « vous vous relevez sans le réveiller ». Fiche `fauteuil-a-bascule-allaitement-teddy` (assise à **40 cm**) : « vous vous relevez sans réveiller bébé ». La décision du 14/09 retire cette promesse des assises basses | Important | Fiche teddy, bloc « Dans le détail » : « dos soutenu, bras posés, bébé bercé en douceur ». Accueil : « Des accoudoirs pour prendre appui en vous relevant ». |
| 4.9 | Appareils électriques (relax électrique, relax moderne) | **FAIL** (gate §0) | `fauteuil-relax-electrique` et `fauteuil-relax-moderne` : « chauffage et massage », télécommande, repose-pieds électrique. Aucune tension, puissance, prise, mention CE ou notice en français | Important | Avant la review : obtenir du fournisseur la déclaration de conformité UE, la tension et la prise, la notice en français et les obligations DEEE, puis ajouter tension, puissance et prise dans le tableau de caractéristiques. Sans documents, passer ces 2 fiches en brouillon. |
| 4.10 | Articles de puériculture (transat, chaise haute 0–6 ans) | **FAIL** (conformité) | `rocking-chair-bebe` (« transat à bascule… premiers mois ») et `chaise-a-bascule-enfant` (« Âge 0 à 6 ans », harnais) : aucune norme, aucun poids maximal de l'enfant, aucun avertissement de sécurité | Important | Obtenir les certificats du fournisseur (normes EN 14988 pour la chaise haute, EN 12790 pour le transat) et ajouter les avertissements obligatoires (« Ne jamais laisser l'enfant sans surveillance », poids et âge maximum). Sans certificats, passer ces 2 fiches en brouillon. Ce sont aussi les 2 seules fiches de la collection Enfant. |
| 4.11 | « Cuir » pour du similicuir | **FAIL** | Handle `/products/fauteuil-relax-cuir` pour un produit « en similicuir ». En France, l'appellation « cuir » est réservée | Important | Nouveau handle `fauteuil-relax-similicuir-pivotant` **avec une redirection 301** depuis l'ancien. Vérifier aussi le nom du fichier et l'alt des images. |
| 4.12 | Titre ↔ URL ↔ image | FAIL (mineur) | `rocking-chair-vintage-velours` a pour titre « …en tissu bouclette ». `fauteuil-relax-pivotant` : « …en bois », alors que l'assise est en similicuir et que seul le piétement est en bois. `housse-de-protection-rocking-chair` : titre « …pour mobilier extérieur », images d'une housse de salon de jardin rectangulaire, tailles jusqu'à 213 × 132 cm. `coussin-d-assise-rocking-chair` : titre « Coussin seul pour fauteuil suspendu, sans panier », l'image 2 le montre dans un panier | Mineur | Aligner les handles (avec 301) ou les titres. Housse : titre et collection « Accessoires » plutôt que « Rocking chair extérieur ». Coussin : image principale sans panier, c'est déjà le cas, garder cet ordre. |
| 4.13 | Doublon apparent | À vérifier | `rocking-chair-bebe` et `chaise-a-bascule-enfant` : même concept (2 en 1 transat + chaise haute), même prix (149 €), mêmes coloris (blanc, gris) | Mineur | Confirmer qu'il s'agit de deux produits différents. Sinon, en garder un. |
| 4.14 | SKU maison | **FAIL** | SKU bruts DSers, avec de l'anglais : `14:29#A Teddy Fleece;200007763:201336101`, `14:366#grey;183:200012944#60X120CM no chair`, `200007763:201336101` (identique sur plusieurs fiches) | Important | Attribuer des SKU maison uniques (ex. `BER-ALL-TED-ROS`) dans DSers ou l'admin, en gardant le mapping DSers. Le flux Google lit ce champ. |
| 4.15 | Stock et disponibilité | PASS | 29/29 en stock, suivi de stock actif, JSON-LD `InStock` | — | — |
| 4.16 | Variante = image | PASS | Chaque variante couleur a son image (ex. repose-pieds 12/12, housse 62/62) | — | — |

## 5. Collections

| # | Point | Statut | Preuve (compte visiteur via `/collections/<h>/products.json`) | Gravité | Correction proposée |
|---|---|---|---|---|---|
| 5.1 | Au moins 5 produits par collection (mode UNIVERS) | **FAIL** | fauteuil-relax-jardin **1** · fauteuil-cocon **2** · rocking-chair-enfant **2** · rocking-chair-repose-pieds **2** · accessoires-rocking-chair **3** · chaise-a-bascule **3** · fauteuil-allaitement **3** · bois-rotin 4 · design-scandinave 4 · exterieur 4 · fauteuil-a-bascule 5 · fauteuil-relax 7 · selection 8. (Le `products_count` public compte les brouillons : 18, 16, 14…) | Important | Avant la review : soit publier le lot 2 (après visuels et corrections du §7), soit retirer du menu les collections à 1–2 produits (Relax de jardin, Cocon, Enfant, Repose-pieds) et les rattacher à une collection mère. « Allaitement » (3 produits) est l'entrée n° 1 du menu : la renforcer en priorité. |
| 5.2 | Description = catalogue réel | PASS | Accessoires : « trois compléments » = 3 ; Cocon : « deux formes » = 2 ; Enfant : « nos deux sièges » = 2 ; Repose-pieds : « deux modèles » = 2 ; Relax jardin : « Notre fauteuil » = 1 | — | Après publication du lot 2, **réécrire ces descriptions** : les nombres deviendront faux. |
| 5.3 | Housse hors de la collection Accessoires | Mineur | La politique classe la housse dans les accessoires, mais elle n'est que dans `rocking-chair-exterieur` | Mineur | L'ajouter à `accessoires-rocking-chair`, ce qui porte la collection à 4 produits. |
| 5.4 | Liens internes des descriptions | PASS | 10 liens (/pages/guide-*, /collections/*, /pages/livraison-retours), tous en 200. Aucun lien dans les descriptions produit | — | — |
| 5.5 | Collection cachée | Mineur | `selection-bercelou` en `noindex,nofollow` mais liée depuis l'accueil (« Voir tous les fauteuils ») | Mineur | Voulu ? Sinon, retirer le noindex ou pointer « Voir tous les fauteuils » vers une collection indexée. |

## 6. Pages, menu, pied de page, technique

| # | Point | Statut | Preuve | Gravité | Correction proposée |
|---|---|---|---|---|---|
| 6.1 | 404 dans le menu, le pied de page ou les liens internes | PASS | 130 liens internes relevés : toutes les collections, pages, fiches actives et politiques répondent 200 ; `/apps/parcelpanel` 200 ; `/account` 302 vers la connexion. `/blogs/news` est en 404 mais n'est lié nulle part | — | — |
| 6.2 | Deux pages de suivi, dont une qui promet un formulaire absent | **FAIL** | Menu « Suivre votre commande » → `/apps/parcelpanel` (formulaire ParcelPanel qui fonctionne). Pied de page « Suivre ma commande », politique d'expédition et Contact → `/pages/suivre-ma-commande`, qui dit « Saisissez votre numéro de commande… » **sans aucun formulaire** | Important | Soit intégrer le bloc ParcelPanel dans `pages/suivre-ma-commande`, soit rediriger (301) `/pages/suivre-ma-commande` vers `/apps/parcelpanel` et pointer tous les liens (pied de page, politique, Contact) vers la même URL. |
| 6.3 | Pied de page en ligne : ce qui manque | FAIL (partiel) | Présents : coordonnées en texte, menus « Nos fauteuils » et « Informations », 6 politiques automatiques, lien cookies, pictogrammes de paiement. Manquants : liens `mailto:`/`tel:` (1.7), mention « OH Ventures (SASU) » et SIREN (seulement « OH Ventures, 47 rue Vivienne »), libellé « CGV » (la politique s'appelle « Conditions d'utilisation » alors que son contenu est « Conditions Générales de Vente et d'Utilisation ») | Important | Pour le nouveau pied de page (autre session, non modifié ici) : `mailto:` + `tel:` ; « OH Ventures (SASU) — SIREN 103 157 251 » ; un seul lien par politique (le brouillon aperçu affichait les liens légaux **deux fois** : bloc « Légal » + liste automatique) ; libellé « Conditions générales de vente ». Admin → Politiques : renommer le titre « Conditions d'utilisation » en « Conditions générales de vente ». |
| 6.4 | Politiques accessibles, sans noindex | PASS | 6 politiques en 200, aucune balise robots | — | — |
| 6.5 | JSON-LD `Organization` en parseur strict | PASS (syntaxe) / **FAIL** (contenu) | `json.loads` passe. Mais `sameAs` = `facebook.com/themefullstack`, `youtube.com/@themefullstack`, `linkedin.com/company/themefullstack` (réseaux de démonstration du thème) ; `telephone: "0756828094"` | **Bloquant** | Thème → Réglages du thème → Réseaux sociaux : **vider** les 3 URL de démonstration (Bercelou n'a pas de compte, ne rien mettre). Vérifier ensuite que le JSON-LD reste valide sans `sameAs`, puisque le piège Noirmont était une virgule orpheline. Téléphone : voir 1.6. |
| 6.6 | JSON-LD Produit | PASS | 29 fiches : `Product`/`ProductGroup` valides, `brand: Bercelou`, `price` = prix affiché, `priceCurrency: EUR`, `availability: InStock` | Mineur | Optionnel : ajouter `shippingDetails` et `hasMerchantReturnPolicy` (0 €, France, 14 jours, retour payé par le client). |
| 6.7 | Balises title et meta description | PASS (sauf accueil) | Fiches, collections et pages : titres « … \| Bercelou » et descriptions renseignés. **Accueil : title = « Bercelou » seul, aucune meta description** | Mineur | Préférences de la boutique : title « Bercelou — Fauteuils à bascule et fauteuils d'allaitement » et une meta description de 150 caractères. |
| 6.8 | HTTPS et redirections | PASS | `http://bercelou.com` → 301 `https://bercelou.com/` ; `https://www` → 301 apex ; certificat valide | — | — |
| 6.9 | robots.txt et sitemap | PASS | `Sitemap: https://bercelou.com/sitemap.xml` ; sous-sitemaps produits, pages, collections et blogs | — | — |
| 6.10 | Langue | PASS | `lang="fr"` sur toutes les pages | — | — |
| 6.11 | Guide « offert » | PASS | Barre d'annonce : « Guide pour bien choisir offert en ligne ». Guide numérique, rien de promis dans le colis | — | — |
| 6.12 | Préférences cookies | PASS (lien) | Lien « Préférences en matière de cookies » dans le pied de page. Bandeau non testé | Mineur | Tester le bandeau à la première visite (Accepter = Refuser) avant de poser une balise Google. |

## 7. Brouillons (86) et archivés (14) — textes, prix, délais uniquement

| # | Point | Statut | Preuve | Gravité | Correction proposée |
|---|---|---|---|---|---|
| 7.1 | Prix barrés remplis | **FAIL** | **100/100** brouillons et archivés ont un `compareAtPrice`, en pratique le coût fournisseur, **plus bas** que le prix (ex. `fauteuil-a-bascule-oreilles-tissu-avec-tabouret` 249 € / 140,13 € ; `pouf-coffre-rond-velours-cotele` 49 € / 25,04 €). Ils s'appliqueront à la publication | **Bloquant (avant publication)** | Vider `compareAtPrice` sur toutes les variantes des brouillons et archivés, et régler DSers (règle de prix) pour ne plus remplir ce champ. |
| 7.2 | Prix non arrondis, sous 20 € | **FAIL** | `plaid-grosse-maille-tricote-main` (68 variantes, 17,82–99 €, ex. 60,77 €, 31,54 €) ; `plaid-fausse-fourrure-effet-lapin` (15,59–49 €) ; `coussin-de-sol-rond-epais-dehoussable` (82 variantes, 23,29–66,55 €) ; `coussin-de-sol-carre-velours-cotele` (11,21–49 €) | Important | Refaire la grille de prix de ces 4 fiches (prix ronds, marge vérifiée) et réduire le nombre de variantes. |
| 7.3 | Marques tierces | PASS | Aucune dans les 86 brouillons | — | — |
| 7.4 | Archivés en anglais | Mineur | 7 archivés gardent un handle et un texte anglais d'origine (`himiss-oversized-papasan…`, `anajqaqia-75-75-92-5-cm…`, `split-high-back-teddy…` avec « premium fabric ») | Mineur | Ne jamais les republier tels quels. Les supprimer quand le lot 2 sera en ligne, ou au moins vider leurs prix barrés (7.1). |
| 7.5 | Délais par catégorie | FAIL | Voir 2.13 (repose-pieds, poufs et tables à 3 à 10 jours, contre « repose-pieds = accessoires 7 à 15 jours » dans la politique) | Important | Voir 2.13. |
| 7.6 | Appareils électriques du lot 2 | À bloquer | `fauteuil-relax-massant-chauffant-chenille-ecru` (8 points de vibration, chauffage lombaire), `fauteuil-relax-electrique-gris-compact`, `fauteuil-allaitement-bouclette-blanche-usb` | Important | Même gate que 4.9 (CE, notice, DEEE) avant publication. |
| 7.7 | Mentions « lombaire » et « posture » | PASS | Descriptions factuelles (« coussin lombaire amovible », « posture détendue »), sans promesse de santé | — | Ne pas ajouter de promesse de soulagement du dos. |
| 7.8 | Délais annoncés | PASS | Meubles « 3 à 10 jours ouvrés », textiles « 7 à 15 jours ouvrés », livraison offerte, retour sous 14 jours : conformes à la politique (hors 2.13) | — | — |

---

## Ordre de correction conseillé avant la demande de review

1. Renommer le tarif de livraison (2.3), supprimer la barre « Plus que 30 € » (2.4), vider les réseaux sociaux de démonstration du thème (6.5).
2. Harmoniser le téléphone (1.6), ajouter les liens `mailto:`/`tel:` et « OH Ventures (SASU) » dans le nouveau pied de page (1.7, 6.3), ajouter « TTC » (3.7).
3. Régler la page de suivi en double (6.2), la promesse « vérifié » et « se relever » (4.7, 4.8), le seuil du paiement fractionné (3.5), le handle « cuir » avec une 301 (4.11), les SKU maison (4.14).
4. Documents CE des 2 relax électriques et normes des 2 sièges bébé, ou mise en brouillon (4.9, 4.10).
5. Collections minces (5.1) : publier le lot 2 seulement après 7.1, 7.2, 2.13 et 7.6, puis réécrire les descriptions de collection (5.2).
6. Hakim : test de caisse anonyme (3.6), réglages Merchant Center identiques (délais, 14 jours, retour payé par le client), Trustpilot, adresse = KYC.
7. Après correction : balayer les 5 endroits où vit chaque promesse (bloc de thème, Liquid, description, page CMS, politique).

# Audit de cohérence — Lumière Matière (25/08/2026)

**Périmètre :** tout le site hors home (auditée et enrichie le même jour). Méthode : GraphQL Admin live (produits, collections, menus, pages, policies, profils de livraison) + fichiers du thème Full Stack `copie-de-fullstack-2-3`. **Pas de rendu navigateur** : storefront sous mot de passe et autorisation Chrome non accordée pendant la session — les mécaniques JS (sélecteurs, swap d'image) ont été vérifiées dans le code du thème, pas au clic.

## Verdict

**Ce qui tient — et tient bien :**

- **Chiffres ops identiques partout** : 16h00 Paris · 1–2 j · 6–15 j · 7–17 j · retours 30 j + 14 j · remboursement 7 j · SAV lun–ven 10h–18h · 24 h ouvrées. Vérifiés sur FAQ, 5 policies, Contact, Notre histoire, Paiement, footer, annonces, et les 120 fiches (0 délai divergent).
- **Paiements cohérents** : Visa/MC/Amex + Apple Pay + Shop Pay + PayPal listés à l'identique (page Paiement, CGV §4, footer). Le footer rend `shop.enabled_payment_types` automatiquement (`force_icons_display=false`) = miroir du checkout. Wallets API : Shop Pay + Apple Pay, **pas de Google Pay**.
- **OH Ventures uniquement** dans mentions légales, CGV, confidentialité. Footer, pages CMS et fiches au nom de la marque.
- **Catalogue sain** : 120 fiches actives / 629 variantes, toutes avec packshot variante ; axes lisibles (Câble, Verre, Finition, Diamètre…) ; bambou 583180/033589/280004 bien en « Câble » avec titres alignés ; 5 metafields PDP présents sur 120/120 ; prix tous dans la grille 149–499 ; « Autour de 199 € » honnête (63 fiches à 199 €, collection à 64 produits, prix d'appel 149–199).
- **Marketing aligné** : promesse « galerie de matières » portée par le hero, la nav par matière, l'édito, le SEO collections et les PDP (matière nommée honnêtement : « composite à grain minéral », « effet cristal » en verre). Aucun mot interdit (premium, atelier, AliExpress, avis inventés) sur les surfaces client.

**Ce qui cloche encore :** rien de bloquant côté copy. Libellés d’options et alt soldés (25/08 soir). Le P1 livraison, ParcelPanel, blocs démo hero et **titres dupliqués (P2)** sont soldés. Restent les points Hakim (publier Full Stack, GMC à 30 j, LM-045, Unmapped DSers, 453740 / 201424).

---

## P1 — bloquant avant lancement Ads

### 1. Profil de livraison ≠ promesse « livraison offerte, France métropolitaine » — **corrigé 25/08**

**Constat (avant) :** le profil général contenait, zone France : `Standard 7,99 €` (sans condition), `Standard 0 €` (condition panier ≥ 65 €), `Express 10,99 €` — plus deux zones actives **UE (22 €)** et **International 14 pays (29 €)**.
**Correction :** `shopify/configure_shipping.py` — une seule zone **France** (pays FR), une seule méthode **Livraison offerte 0,00 €** sans condition. Standard, Express, UE et International supprimés. Relecture GraphQL `deliveryProfiles` : 1 zone / 1 méthode / 0 €.
**Reste Hakim :** Réglages → Marchés (scope `read_markets` absent du token CLI) — désactiver tout marché hors France.

### 2. Recette impossible tant que Full Stack n'est pas publié

**Constat :** Helio reste MAIN, le storefront est sous mot de passe. La recette réelle (menus, checkout, wallets affichés, ParcelPanel, mobile 375) ne peut pas se faire de bout en bout.
**Reco (Hakim) :** valider la preview Full Stack (https://nzefxg-gg.myshopify.com/?preview_theme_id=186708001104), publier, puis dérouler la checklist pré-soumission `gmc-acceptance` (le mot de passe devra être levé avant toute review GMC).

## P2 — à corriger avant ou juste après lancement

### 3. Titres strictement identiques : 13 groupes, 31 fiches — **corrigé 25/08 soir**

**Correction :** 120 titres uniques en live (`HUMANISATION-PDP-2026-08-25.md`). 32 fiches des groupes de doublons différenciées d’après photo ; 56 autres titres réécrits parce que l’image contredisait le nom. SKU inchangés.

### 4. « Suivre votre commande » → ParcelPanel — **confirmé 25/08**

Hakim : l’app est installée et fonctionne. FAQ Q14 pointe vers `/apps/parcelpanel` (et le compte).

### 5. Blocs démo Trustpilot / « 2 000 clients » — **supprimés 25/08**

Retirés du JSON du hero Full Stack (plus seulement `disabled`).

### 6. 0 GTIN sur 629 variantes

**Constat :** aucun `barcode` renseigné.
**Impact :** normal en dropshipping, mais le feed devra porter `identifier_exists = false` proprement ; à surveiller côté Merchant Center (avertissements de performance limitée).
**Reco (Hakim, au moment du feed) :** vérifier le traitement par l'app Google & YouTube après liaison GMC.

## P3 — soigner quand le reste est fait

### 7. Deux collections orphelines à 1 produit

`lustres-statement` et `suspensions-modernes` : publiées, hors menu, hors home (et hors `/collections` depuis le correctif du jour). Reco : fusionner leurs produits dans `lustres-salon` / `suspensions-deco` puis dépublier, ou étoffer.

### 8. Collections sans image : `selection-199` et `frontpage`

`selection-199` (64 produits) n'a pas d'image de collection ; `frontpage` est le placeholder Shopify (1 produit, sans image ni description, publié sur 3 canaux). Reco : image pour selection-199 si elle doit réapparaître dans une grille ; vider et dépublier `frontpage`.

### 9. 12 variantes sans poids (617/629 OK)

Sans impact tant que la livraison est gratuite au prix ; utile pour douane/transporteur. Reco agent : compléter à l'occasion.

### 10. Axe « Couleur » ambigu sur `suspension-effet-pierre-092465`

Valeurs « Blanc chaud / Brun » : cohérent avec le titre et le SKU, mais « blanc chaud » est un vocabulaire de température de lumière appliqué ici à la teinte du composite. Reco : renommer la valeur (« Pierre claire » ?) après contrôle photo — le renommage d'une valeur d'option ne touche pas les SKU.

---

## Corrigé pendant la session (25/08)

- **Home enrichie en live** (`patch_home.py`, backups avant/après dans `backups/2026-08-25-home-enrichie/`) : bénéfices par pièce, guide « bien choisir » 3 étapes, CTA final avec preuves vraies, sous-titre matières ; bloc défensif « sans cristal inventé ni atelier fictif » remplacé par un bénéfice positif ; `apply_fullstack.py` aligné pour ne plus écraser ces sections.
- **`/collections` curatée** sur les 11 collections du menu (exclut `frontpage`, `selection-199` sans image, les 2 collections à 1 produit). Backup avant/après dans le même dossier.

## Non vérifié (à recetter après publication)

- Rendu visuel mobile 375 / desktop et clics réels (mot de passe storefront + autorisation Chrome absente). Statiquement : sélecteur affiche bien `option.name`, galerie re-rendue au changement de variante avec `selected_variant.featured_media` en tête.
- Checkout réel (affichage effectif des wallets à la caisse).
- Installation ParcelPanel (P2 §4).
- Feed GMC réel (app Google & YouTube, scopes absents).
- Thème Helio (MAIN) — interdit d'écriture, non audité.

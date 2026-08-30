---
type: journal
boutique: seiko-mod
date: 2026-07-31
nature: intervention
leviers: [page]
titre: "Pied de page Maison Noirmont — refait sur le modèle Tuftéo"
---

# Pied de page Maison Noirmont — refait sur le modèle Tuftéo

Date : 2026-07-27 · Boutique : `v42pzp-h4` / maisonnoirmont.fr
Thème écrit : **`204248088914` « Maison Noirmont » (UNPUBLISHED)** — vérifié `role: UNPUBLISHED` avant et après chaque écriture.
Thèmes **non touchés** : `204246548818` « Helio » (MAIN), `204329288018` (fork obsolète).
Modèle relevé sur **tufteo.com** par le navigateur intégré (web public). **Aucun `switch-shop`** : lecture Tuftéo par le web, écriture Noirmont par l'API Admin.
Aucun thème publié. Aucune commande. Aucun produit, SKU, prix, variante, média ni mapping DSers touché.

---

## 1. Relevé du modèle Tuftéo

Découverte structurante : **Tuftéo et Noirmont tournent sur le même thème FullStack 2.3.0**, et le groupe de sections du pied de page de Noirmont est déjà un décalque de celui de Tuftéo — jusqu'à l'identifiant de section `custom_section_k6mNHc`. `sections/footer.liquid` est **identique octet pour octet** dans les deux boutiques. Le modèle ne se relève donc pas dans le Liquid mais dans les **réglages** : nombre de colonnes, découpage des menus, contenu des blocs.

### Desktop (mesuré à 1280 px)

| Élément | Tuftéo |
|---|---|
| Grille | `grid`, **5 colonnes** de **216 px**, gouttière **30 px**, `padding-top: 50px`, `padding-bottom: 0` |
| Colonne 1 | groupe flex vertical, gouttière 20 px : **logo** (32 px de haut, version inversée) → **paragraphe de marque** → **lien mailto** → **icônes sociales** |
| Colonne 2 | menu **« Boutique »** — 7 entrées (Accueil, Kit débutant, Machines, Consommables, Accessoires & finitions, Academy, Aide) |
| Colonne 3 | menu **« Informations »** — 6 entrées (Notre histoire, FAQ, Contactez-nous, Livraison & retours, Suivre ma commande, Apprendre le tufting) |
| Colonne 4 | menu **« Légal »** — 6 entrées (Mentions légales, Confidentialité, Remboursement, CGV, CGU, Livraison & retours) |
| Colonne 5 | groupe flex vertical, gouttière 10 px : **titre bénéfice** en h6 → **formulaire infolettre** (champ + bouton icône 50 × 50) |
| Alignement des menus | `center` en desktop, `flex-start` en mobile |
| Titres de colonne | `h6`, **16 px**, graisse 500, police d'affichage de la marque (Fraunces chez eux), casse normale |
| Liens de menu | 15 px, gouttière verticale 16 px |
| Ligne légale | **automatique** (`shop.policies`), `padding-top: 60px`, flex `wrap`, `justify-content: flex-start` en desktop / `center` en mobile, 13,5 px, souligné, gouttières **5,28 px / 12 px** — **8 entrées** dont « Préférences en matière de cookies » |
| Barre du bas | grille 3 colonnes déclarées, 2 blocs rendus : **icônes de paiement** à gauche (`flex-start`, 35 px, 6 icônes : Visa, Mastercard, Apple Pay, Google Pay, PayPal, Shop Pay) et **copyright** centré (« © 2026 Tuftéo », 13,5 px). `padding: 20px 0`. Le badge « powered by » est **désactivé**. |
| Sélecteur de langue / devise | **absent** (0 `localization-form`, 0 `select`) |
| Réseaux sociaux | 3 icônes (Facebook, YouTube, LinkedIn) pointant sur **`themefullstack`**, c'est-à-dire les comptes de démonstration du fournisseur du thème — pas des comptes Tuftéo |
| Fond / texte | `#1C1410` sur `#FDF8EF` (schéma sombre du thème) |
| Champ e-mail | **14 px** |

### Mobile (mesuré à 375 px)

- **1 colonne** de 335 px, gouttière **40 px**, marges latérales 20 px.
- **Aucun accordéon** : `details`/`summary` = 0. Les cinq colonnes s'empilent dans le même ordre, listes entièrement dépliées, alignées à gauche.
- Icônes de paiement **centrées**, copyright **centré**, ligne légale **centrée**.
- Aucun débordement horizontal (`scrollWidth` = 375).

### Hiérarchie typographique et rythme

Un seul niveau de titre (h6 à 16 px) pour les cinq colonnes ; le corps à 15 px ; la ligne légale un cran en dessous à 13,5 px. Le rythme vertical est porté par trois gouttières seulement : 40 px entre colonnes en mobile, 30 px en desktop, 16 px entre liens. Aucune bordure, aucun filet, aucun aplat de couleur : la séparation vient du fond sombre du bloc entier.

---

## 2. Transposition faite — forme de Tuftéo, contenu et palette de Noirmont

### Fichiers écrits

| Fichier | Avant | Après |
|---|---|---|
| `sections/footer-group.json` | 26 800 o · `3d124046ef3f2115191fd6cbe38c84de` | **27 496 o · `a69e9fbd412817648b7ea73c79b2c62d`** |
| `assets/noirmont-footer.css` | (inexistant) | **3 248 o · `0e54a1a7b068e8185a5efa16542757e3`** |
| `layout/theme.liquid` | 1 744 o · `6c174fd42bf55e62c3ddd07e64d49f67` | **1 876 o · `39fb639f9e864832b0cac2ec816ef79b`** |
| `assets/noirmont-custom.css` | 54 054 o · `8685e465b33a2a539a39531c4fcaf5e8` | **inchangé** (même empreinte après coup) |

Chaque empreinte a été **relue après écriture** et comparée aux octets attendus : les trois écritures ont été confirmées, aucune n'est restée en attente asynchrone.

Sauvegardes dans `boutique-pipeline/scratchpad/backup-footer/` :
`footer-group.before.json` (reconstruit puis **vérifié octet pour octet** contre l'empreinte d'origine), `footer-group.after.json`, `theme.liquid.bak` (vérifié), `noirmont-custom.css.bak`, `noirmont-footer.css.new`, plus le script `build_footer_group.py` qui rejoue les deux états.

### Menus créés (3 nouveaux, aucun menu existant modifié)

Le thème ne sait afficher qu'un menu entier par colonne. Passer de 2 à 3 colonnes de menus imposait donc trois listes. Elles ont été **créées** sous de nouveaux handles ; le menu `footer` d'origine (11 entrées, nav + légal mélangés) et `main-menu` sont **intacts** — ce qui garantit que le thème MAIN « Helio » n'est pas affecté.

| Handle | Titre | Entrées |
|---|---|---|
| `footer-boutique` | Pied de page — Boutique | Accueil · Configurateur · Montres · Accessoires · Bracelets · Écrins et rouleaux · Remontoirs |
| `footer-informations` | Pied de page — Informations | La Maison · FAQ · Contact · Livraison et retours |
| `footer-legal` | Pied de page — Légal | Mentions légales · Confidentialité · Cookies · Remboursement · Expédition · CGV · CGU |

### Cibles des liens légaux — inchangées

Le pied de page est **mixte, comme prévu** : chaque cible a été reprise telle quelle depuis le menu `footer` existant, sans réattribution.

| Libellé | Cible | Type |
|---|---|---|
| Mentions légales | `/pages/mentions-legales` | page |
| Politique de cookies | `/pages/politique-de-cookies` | page |
| Politique de confidentialité | `/policies/privacy-policy` | politique |
| Politique de remboursement | `/policies/refund-policy` | politique |
| Politique d'expédition | `/policies/shipping-policy` | politique |
| Conditions générales de vente | `/policies/terms-of-sale` | politique |
| Conditions générales d'utilisation | `/policies/terms-of-service` | politique |

### Substitutions de contenu

| Élément Tuftéo | Remplacé par |
|---|---|
| Logo `logo-tufteo-blanc-800.png` | wordmark `logo-noirmont-craie.png`, **surmonté de l'anneau** de la marque (bloc 10.8 de `noirmont-custom.css`) — les deux conservés |
| « Kits de tufting complets et guides en français… Expédié depuis l'Europe, garanti 2 ans. » | Texte Noirmont déjà en place, **inchangé** : « Maison Noirmont — des garde-temps au cadran épuré : mécaniques automatiques, et chronographes méca-quartz. Votre signature au poignet. » La promesse « expédié depuis l'Europe, garanti 2 ans » **n'a pas été transposée** : elle n'est pas vraie pour Noirmont. |
| `contact@tufteo.com` | **`contact@maisonnoirmont.fr`** (paragraphe mailto ajouté sous le texte de marque, même forme que le modèle) |
| Colonne « Boutique » (kits, machines, consommables) | Accueil, Configurateur, Montres, Accessoires, Bracelets, Écrins et rouleaux, Remontoirs — **7 entrées comme le modèle**, toutes des collections et pages qui existent déjà |
| « Notre histoire » | **« La Maison »** |
| « Livraison & retours » | **« Livraison et retours »** → `/policies/shipping-policy` |
| « Reçois nos guides et nouveautés » (tutoiement) | **« Recevez nos nouveautés »** (vouvoiement) |
| « © 2026 Tuftéo » | **« © 2026 Maison Noirmont »** (généré par `shop.name`, pas saisi) |
| Fond `#1C1410` / texte `#FDF8EF` | **schéma sombre de Noirmont** : encre `#0B0B0C` / craie `#FAFAF7` |
| Police d'affichage Fraunces | police de sous-titre de Noirmont (Inter 500, 16 px) |
| Champ e-mail 14 px | **16 px** — écart volontaire, voir § 4 |

**Palette** : aucune couleur n'est déclarée dans le pied de page. Il reste en `scheme-3`, craie sur encre. Le cyan `#22D3EE` n'apparaît **qu'à l'anneau de focus clavier** — jamais un bouton, jamais un badge. Le vert forêt `#1E3A2F` et le laiton `#A98E5F` ne sont **pas** réintroduits : aucune occurrence dans les fichiers écrits.

**Aucun résidu « tufteo »** : 0 occurrence de la chaîne `tuft` dans le DOM rendu, à 1280 comme à 375.

---

## 3. Rubriques du modèle sans équivalent — rien n'a été fabriqué

| Rubrique Tuftéo | Décision | Pourquoi |
|---|---|---|
| **« Suivre ma commande »** (`/apps/parcelpanel`) | **non transposée** | Aucune page ni application de suivi chez Noirmont. La politique de livraison dit que le lien de suivi arrive par l'e-mail de confirmation d'expédition — fabriquer une entrée de menu vers une page inexistante aurait produit une 404. |
| **« Academy » / « Apprendre le tufting »** (`/pages/apprendre`) | **non transposée** | Pas de pôle éditorial chez Noirmont. Le blog n'est pas alimenté. Rien à pointer. |
| **« Aide »** (doublon de FAQ dans la colonne Boutique) | **non transposée** | FAQ est déjà en colonne Informations ; le doublon de Tuftéo n'apporte rien. |
| **Réseaux sociaux** (3 icônes) | **emplacement conservé, bloc laissé désactivé, champs vides** | Les comptes du modèle sont ceux du **fournisseur du thème** (`themefullstack`), pas ceux de Tuftéo. Aucun compte Noirmont n'a été inventé. Le bloc `social_icons_hQdtRf` reste en place avec `"disabled": true` — il suffira de renseigner les URL dans les réglages du thème et de le réactiver. |
| **Badge « powered by »** | **laissé désactivé** | Déjà désactivé des deux côtés. |
| **Sélecteur de langue / devise** | **rien à faire** | Absent chez Tuftéo comme chez Noirmont : une seule langue, une seule devise, une seule zone d'expédition. |

La colonne **Informations** compte donc **4 entrées** au lieu de 6. C'est le seul écart de volume au modèle, et il est assumé : les deux entrées manquantes n'ont pas de destination réelle.

---

## 4. Mesures avant / après

### Structure

| Mesure | Avant (Noirmont) | Après (Noirmont) | Modèle (Tuftéo) |
|---|---|---|---|
| Colonnes desktop | 4 | **5** | 5 |
| Largeur de colonne à 1280 px | 288 px | **216 px** | 216 px |
| Gouttière desktop | 30 px | 30 px | 30 px |
| Colonnes mobile | 1 | 1 | 1 |
| Gouttière mobile | 40 px | 40 px | 40 px |
| Accordéons en mobile | 0 | **0** | 0 |
| Titres de colonne | La Maison · Informations | **Boutique · Informations · Légal** | Boutique · Informations · Légal |
| Entrées de la colonne 3 | 11 (nav + légal mêlés) | **4** (nav seule) | 6 |
| Adresse de contact au pied | absente | **contact@maisonnoirmont.fr** | contact@tufteo.com |
| Icônes de paiement | 6 | 6 | 6 |
| Entrées de la ligne légale | 8 (automatiques) | 8 (automatiques) | 8 |

### Accessibilité — deux régressions latentes corrigées

| Mesure | Avant | Après | Seuil |
|---|---|---|---|
| Hauteur des liens de colonne | **42,4 px** | **44,0 px** | 44 px |
| Hauteur des liens de la ligne légale | **39,6 px** | **44,0 px** | 44 px |
| Hauteur du lien mailto | — | 44,0 px | 44 px |
| Hauteur du lien du copyright | **42,4 px** | 44,0 px | 44 px |
| Écart entre rangées de la ligne légale | **5,28 px** | **8,0 px** | 8 px |
| Écart entre liens d'une colonne | 16 px | 16 px | 8 px |
| Champ e-mail | 16 px · `autocomplete="email"` | **16 px · `autocomplete="email"`** | 16 px |
| Bouton d'envoi | 50 × 50 px | 50 × 50 px | 44 px |
| Contraste texte du pied (opacité héritée comprise) | 18,81:1 | **18,81:1** (craie `#FAFAF7` sur encre `#0B0B0C`, opacité mesurée à 1,000) | 4,5:1 |
| Anneau de focus clavier | présent | **présent et vérifié à l'œil** : `outline 2px #22D3EE`, `offset 2px`, halo d'encre 6 px, `radius 3px`, uniquement en `:focus-visible` | visible |
| `text-wrap: balance` sur les titres de colonne | oui | **oui** (`balance` calculé sur les trois `h3`) | — |
| Chiffres tabulaires du millésime | non couvert | **`tabular-nums`** | — |
| Débordement horizontal à 1280 px | aucun | **aucun** (`scrollWidth` 1280) | aucun |
| Débordement horizontal à 375 px | aucun | **aucun** (`scrollWidth` 375) | aucun |

**Cause des deux hauteurs sous le seuil** : le bloc 9.6 de `noirmont-custom.css` posait `min-height: 24px` en visant 24 px de contenu plus 2 × 10 px de marge intérieure. Le thème est en `box-sizing: border-box`, donc les 24 px comptaient **déjà** la marge intérieure : la règle n'imposait plus rien et la hauteur retombait sur celle du texte. La valeur passe à `var(--nm-tap)` (44 px), marge comprise. `display: inline-block` est **conservé volontairement** : le wordmark du pied de page est lui aussi un `<a>` visé par ce sélecteur, et le passer en `inline-flex` aurait fait de l'anneau du bloc 10.8 un frère de rangée — posé **à côté** du wordmark au lieu d'**au-dessus**. Vérifié après coup : anneau 22 px, marge basse 12 px, wordmark 32 px, image à 44 px du haut du lien. L'anneau et le wordmark sont intacts.

**Où le correctif a été écrit** : dans un nouvel asset `assets/noirmont-footer.css`, chargé après `noirmont-custom.css`, et non dans le champ CSS d'une section (rejeté en silence). Le thème avait déjà cette convention : `noirmont-megamenu.css`, `noirmont-collection.css`, `noirmont-see-more-fix.css`. Cela évitait de réécrire les 54 ko de `noirmont-custom.css` — donc de risquer d'abîmer la passe d'accessibilité pour deux lignes de correction. `noirmont-see-more-fix.css` reste la dernière feuille du `<head>`.

### Liens — tous en 200

19 URL distinctes du pied de page appelées en `fetch` sur la prévisualisation : **toutes en 200**. Aucun mot de passe saisi (la prévisualisation du thème brouillon s'ouvre sur la session en cours).

```
/                                    200      /pages/mentions-legales           200
/pages/configurateur                 200      /policies/privacy-policy          200
/collections/montres                 200      /pages/politique-de-cookies       200
/collections/accessoires             200      /policies/refund-policy           200
/collections/bracelets               200      /policies/terms-of-sale           200
/collections/ecrins-et-rouleaux      200      /policies/terms-of-service        200
/collections/remontoirs              200      /policies/contact-information     200
/pages/la-maison                     200      /policies/legal-notice            200
/pages/faq                           200      /policies/shipping-policy         200
/pages/contact                       200
/policies/#shopifyReshowConsentBanner  404 — voir ci-dessous
```

---

## 5. Points à trancher par Hakim

1. **`/policies/#shopifyReshowConsentBanner` renvoie 404 en navigation directe.** Ce lien est **généré par Shopify** dans la ligne légale (`shop.policies`), pas écrit par nous, et **Tuftéo porte exactement le même**. Il ne fonctionne que comme point d'accroche JavaScript pour rouvrir la bannière de consentement ; la route `/policies/` sans politique nommée est un 404 côté serveur. Rien à corriger dans le thème — signalé pour que le 404 dans un audit de liens ne surprenne pas.

2. **« Mentions légales » apparaît deux fois avec deux cibles différentes** : `/pages/mentions-legales` dans la colonne Légal (cible imposée, non touchée) et `/policies/legal-notice` dans la ligne légale automatique. Les deux répondent 200 et servent le même contenu (longueur de texte identique au caractère). **Tuftéo présente le même doublon.** À arbitrer si tu veux une seule source : ce serait un choix côté Réglages → Politiques, pas côté thème.

3. **La ligne légale du bas est entièrement automatique** (`shop.policies`), donc **non ordonnable** et **non filtrable** depuis le thème. Elle affiche aussi « Coordonnées », qui n'a pas d'équivalent dans nos colonnes. Même comportement chez Tuftéo.

4. **« Recevez nos nouveautés »** est ma formulation, en vouvoiement, volontairement plus sèche que le « Reçois nos guides et nouveautés » de Tuftéo : je n'ai pas voulu promettre des guides d'infolettre qui n'existent pas encore. À reformuler si tu comptes réellement en envoyer.

5. **Réseaux sociaux** : le bloc est prêt et désactivé, champs vides. Il attend des comptes Noirmont réels. Je n'en ai inventé aucun.

6. **`config/settings_data.json` contient encore `#1E3A2F` et `#A98E5F`** dans les schémas 1, 2 et 3 (`primary_button_*`, `secondary_badge_*`). La purge du 26/07 est portée par des surcharges `!important` du bloc 12 de `noirmont-custom.css`, pas par la source. Le rendu est propre et je n'y ai pas touché — mais tant que la source n'est pas nettoyée, toute modification de ces champs depuis l'éditeur de thème peut faire réapparaître le vert ou le laiton. Hors périmètre de cette passe, signalé.

7. **Capture d'écran desktop** : la prévisualisation à 375 px a été capturée sans difficulté (anneau + wordmark, colonnes, ligne légale, anneau de focus cyan sur « Montres »). À 1280 px le panneau du navigateur intégré ne recomposait plus l'image après défilement programmé et rendait une page vide. **Tous les contrôles desktop sont donc des mesures de géométrie prises sur le rendu vivant** (largeurs de colonnes, hauteurs de cibles, gouttières, contrastes, `scrollWidth`), pas des lectures d'image — c'est plus précis, mais il te reste un coup d'œil visuel à donner à 1280 px depuis ton propre navigateur.

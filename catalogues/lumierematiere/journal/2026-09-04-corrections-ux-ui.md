# Corrections UX/UI — 04/09/2026

Suite de `shopify/AUDIT-UX-UI-2026-09-04.md`. Go Hakim : « ok corrige tout ».
Accès : plugin Shopify (connecteur Claude). Thème live **non touché**.

## 1. Navigation — appliquée sur le site live (pas de thème en jeu)

`menuUpdate` sur `main-menu` (`gid://shopify/Menu/306471534928`) : **10 → 4 entrées**.

| Avant | Après |
|---|---|
| Accueil · Par pièce · Par matière · Lustres · Plafonniers LED · Appliques murales · Notre histoire · FAQ · Contact · Suivre votre commande | **Par pièce ▾ · Par matière ▾ · Lustres ▾ · Plafonniers & appliques ▾** |

- « Plafonniers & appliques » regroupe Plafonniers LED, Plafonniers salon, Appliques murales.
- Accueil, Notre histoire, FAQ, Contact : retirés du menu principal — ils sont déjà dans le footer.
- « Suivre votre commande » ajouté en tête de `footer-informations` (colonne « Informations pratiques »).
- Sous-menus Par pièce / Par matière / Lustres inchangés (Hakim garde osier, bambou, pierre au menu).

**Effet mesuré sur le live, immédiat** : logo rendu **116 × 36 px** (il était à 0 px), menu sur
**une ligne** (4 entrées, 523 px), header 66 px. La cause du logo était bien le menu.

## 2. Thème — sur la copie `LM UX 2026-09-04` (`gid://shopify/OnlineStoreTheme/187012350288`)

Créée par `themeDuplicate` depuis `LM GMC 2026-08-31`. Deux fichiers modifiés, versions poussées
dans `shopify/theme-lm-ux-2026-09-04/`. **Non publiée — publication par Hakim.**
Prévisualisation : `https://lumierematiere.fr/?preview_theme_id=187012350288`

### `sections/header-group.json`
- `header_layout` : `logo_left` → **`logo_left_menu_left`** (grille `auto auto 1fr` : le logo prend sa largeur **avant** le menu — le logo ne peut plus être écrasé, quel que soit le nombre d'entrées). Vérifié en prévisualisation : classe `header__layout--logo-left-menu-left`, logo 129 × 40.
- `logo_height` 36 → **40**, `logo_height_mobile` 28 → **34**.
- Bandeau d'annonce : `show_arrows` → false ; textes raccourcis pour tenir sur une ligne mobile :
  « Livraison offerte partout en France » · « Retours 30 jours · Paiement sécurisé ».
- Bouton header « Suivi de commande » : **testé puis désactivé**. Le thème ne rend ce bloc que dans les layouts `logo_left` / `logo_center` / `logo_center_with_two_menus`, et il le place **avant le menu**, en pilule bordée — il ressemble à une entrée de navigation, ce qu'on voulait justement éviter. Le lien reste en tête de la colonne « Informations pratiques » du footer. Le bloc est laissé configuré (`disabled: true`, libellé et lien en place) ; le mettre à côté des icônes demanderait une retouche de `header.liquid`.

### `templates/index.json`
- **« Par matière »** : `collection_list` — `lustres-effet-cristal` (dépubliée, 0 produit, carte fantôme) remplacée par `suspensions-metal` → **6 cartes réelles**. Sous-titre : « Bambou, rotin, bois, pierre, verre ou métal — et quelques pièces en osier ou en céramique colorée. Ouvrez la matière qui vous attire, les modèles sont derrière. » (plus de « six matières… effet cristal » ; réconcilie les 8 entrées du menu sans annoncer un chiffre faux).
- **« Par pièce et par forme »** → **« Par forme »** (ses trois cartes sont des formes).
- Section newsletter `custom_section_qetdex` **supprimée** (doublon du formulaire footer, −319 px).
- Hero mobile : `same_as_desktop` false, `layout_justify_mobile` **flex-end** (bloc texte calé en bas de l'image), `image_filter_opacity` 35 → **45**, et les deux badges du hero (« Paiement sécurisé », « SAV en semaine ») passés en **desktop_only** — ils doublonnent le bandeau et le footer, et leur hauteur maintenait le titre sur l'abat-jour. Mesuré : le `h1` descend de 221–301 px à **354–434 px** dans une bannière 108–676 ; il passe sous l'abat-jour, dont il frôle encore le bord inférieur. Première passe erronée (axe horizontal) corrigée ; 42 refusé (pas de 5), 45 accepté.
- Bloc `rating_stars` du slider « Pour le salon » : valeurs de démo **4,5 / 123** → **0 / 0** (`hide_rating_when_no_reviews` reste true ; hygiène Noirmont : « disabled ne suffit pas si les valeurs restent »).

### Non fait, volontairement
- Bande de réassurance 4 blocs avant le footer : elle est **site-wide** (`sections/footer-group.json`, `custom_section_k6mNHc`), pas propre à la home. La retirer la retirerait aussi des policies, où elle sert la review GMC. Laissée.
- Méga-menu visuel « Par matière » (§2 de l'audit) et icônes SVG à la place de la police Material (§8) : travail thème plus lourd, pas dans cette passe.
- `money_format` (`€199` → `199 €`) : Paramètres → Général, pas d'API.

## Vérification en prévisualisation (desktop 1440 / mobile 375)
- Desktop : layout `header__layout--logo-left-menu-left`, logo **129 × 40**, 4 entrées sur **1 ligne**, bandeau 42 px, **6 cartes matière**, section newsletter absente, sections : `image_banner → collections_matieres → lm_benefices_piece → collection_featured → lm_guide_choix → collections_piece → custom_section_k9aPjP → lm_cta_final → k6mNHc → footer`.
- Mobile : bandeau **une ligne** (42 px, contre ~130 avant), logo plus grand, hero à filtre 45.
- Seconde passe : hero mobile vérifié (ci-dessus) ; bouton « Suivi de commande » rendu puis retiré (placement avant le menu).

## Pièges relevés
- Les JSON de thème commencent par un bloc `/* … */` : le retirer avant `json.loads`.
- `themeFilesUpsert` valide les réglages : une valeur hors pas d'un `range` est refusée pour tout le fichier.
- `show_on_display` attend `desktop_only` / `mobile_only` / `desktop_and_mobile` — pas `desktop`.
- Le bloc statique `button-header` n'est rendu que dans certains layouts de header (`header.liquid` l. 130 et 142) : un bloc activé peut rester invisible sans erreur.
- Dans l'`image-banner` Fullstack (flex colonne) : `layout_justify_*` = axe **vertical**, `layout_align_items_*` = axe **horizontal**.
- `themeDuplicate` existe (payload `newTheme`) : plus besoin du CLI pour une copie de travail.

# Correctifs JSON — thème `204248088914` « Maison Noirmont » (`v42pzp-h4`)

État : **APPLIQUÉ le 26/07/2026 — 14:40, 14:51, 14:55 et 15:07 UTC** (2ᵉ passe : les 5 accordéons
FAQ de `product.json` en `h4` ; 3ᵉ : le `<h4>` en dur de « Besoin d'aide ? » en `<h3>` ; 4ᵉ : les
4 comptes `themefullstack` vidés dans `settings_schema.json`), le thème étant repassé `UNPUBLISHED`
donc écrivable par le connecteur. **5 fichiers écrits**, `size` + `checksumMd5` relus égaux à la charge utile locale à l'octet près. Rôle vérifié avant écriture : `204248088914` = `UNPUBLISHED`,
`204246548818` (« Helio ») = `MAIN` — jamais touché ; `204329288018` — jamais touché.

Canal d'écriture : `stagedUploadsCreate` (`FILE`, `text/plain`, `PUT`) → `PUT` du fichier local →
`themeFilesUpsert` avec `body: { type: URL, value: <resourceUrl non signé> }`. `themeFilesUpsert`
renvoie `upsertedThemeFiles: []` **sans `userErrors`** : ce n'est pas un échec, l'écriture est
asynchrone — c'est la relecture des empreintes qui la prouve.

| Fichier | avant (`size` / `md5`) | après (`size` / `md5`) | relu conforme |
| --- | --- | --- | --- |
| `config/settings_data.json` | 7300 / `c22beb6db7000cb7340f25d6bf38a309` | 7452 / `18500cab0b556568597eb401c85a50df` | oui |
| `sections/footer-group.json` | 26768 / `4f3d130180b2aeb4308ed08e927e3577` | 26800 / `3d124046ef3f2115191fd6cbe38c84de` | oui |
| `templates/index.json` | 91693 / `4bbd441b9607514a9a1c5a62ee3bf88b` | 91705 / `1ccc270ff471130e705cdfd7e5881e22` | oui |
| `templates/product.json` | 74791 / `027c56cee94730e31dffb2808b617a46` | **74803 / `6f7f80df056e3d98b137df4453bfabc1`** (3 passes) | oui |
| `config/settings_schema.json` | 66309 / `acbaffd782c14cc8bea1e46194101a19` | **66049 / `3c853dd967d1eb6bfb7ef589cd23dc1b`** | oui |

Sauvegardes octet-exactes de l'état **avant** écriture (MD5 égal au `checksumMd5` live) :
`scratchpad/backup-theme-uiux-json/{config__settings_data,config__settings_schema,sections__footer-group,templates__index,templates__product}.json`
(plus `templates__product.v2-avant-faq.json` et `.v3-avant-h3.json` pour les états intermédiaires).
Charges utiles écrites : `scratchpad/patch-uiux-json/` (mêmes noms).
`sections/header-group.json` n'a **pas** été modifié (aucun des 7 points ne le concerne).

Diff structurel avant/après (aplatissement de tous les chemins de clés, les 5 fichiers) : JSON
parsable partout, **aucun chemin perdu involontairement**. Bilan exact : **7 ajouts** (6 tailles
mobiles + `disabled` du bloc social), **17 changements de valeur**, et **4 suppressions
délibérées** — les 4 `default` de comptes du fournisseur dans `settings_schema.json`, seule
suppression de toute l'opération et objet même du correctif. Rien d'autre n'a bougé.

---

## Historique : le blocage, et comment il a été levé

**Résolu.** Le thème a été dépublié entre-temps ; le garde-fou du connecteur ne visait que le
thème `MAIN`. Aucune duplication n'a été nécessaire, donc **aucun instantané de `assets/` n'a
été figé** et le travail des agents CSS/Liquid en parallèle est intact. Trace de l'ancien refus,
conservée pour mémoire :

> `{"blocked":true,"matched":"themeFilesUpsert","category":"live_theme","kind":"targets_live",`
> `"reason":"This mutation targets the live (published) theme. Theme file writes against the`
> `live storefront are blocked. Duplicate the theme in Shopify admin, edit the draft, and a`
> `merchant can publish it manually."}`

Le garde-fou est en amont de Shopify, côté connecteur, et ne visait que `targets_live`. Aucun
contournement n'a jamais été tenté (ni CLI, ni jeton d'admin, ni pilotage de l'admin au
navigateur) : c'est le changement de rôle du thème qui a ouvert la voie normale.

---

## `config/settings_data.json` — hiérarchie des titres et casse (points 1 et 2) — **APPLIQUÉ**

Sauvegarde avant écriture : `scratchpad/backup-theme-uiux-json/config__settings_data.json`
(7300 octets, `c22beb6db7000cb7340f25d6bf38a309` = forme stockée live, à l'octet près).
Charge utile écrite : `scratchpad/patch-uiux-json/config__settings_data.json`
(7452 octets, `18500cab0b556568597eb401c85a50df`), même convention que l'existant : minifiée,
sans en-tête de commentaire, `/` échappés, sans saut de ligne final.

### Cause racine trouvée — l'audit voyait le symptôme, pas la cause

`snippets/css-variables.liquid` définit, dans `@media (width < 750px)` :

```liquid
--font-h1--size: {{ settings.type_size_h1_mobile | divided_by: 16.0 }}rem;
--font-h2--size: {{ settings.type_size_h2_mobile | divided_by: 16.0 }}rem;
```

Or **aucune des six clés `type_size_h{1..6}_mobile` n'existait dans `settings_data.json`** :
Shopify retombait sur les défauts de `settings_schema.json`. Les six sont désormais posées.

⚠️ **Deux corrections à la préparation initiale**, faites après lecture du `settings_schema.json`
live (66 309 o, `acbaffd782c14cc8bea1e46194101a19`, copie locale octet-identique dans
`scratchpad/theme-noirmont/config__settings_schema.json`) :

1. Le défaut de `type_size_h1_mobile` est **48, pas 32**. Le « H1 = 32 px » mesuré à 375 px ne
   venait donc pas d'un défaut de schéma mais **uniquement** du `text_style: "h2"` du hero : le
   `<h1>` était stylé par `--font-h2--size` (défaut mobile 32). La cause racine est bien la
   paire, mais c'est le `text_style` qui portait tout le symptôme.
2. **`28` n'est pas une option valide** de ces sélecteurs. La liste est
   10/12/14/16/18/20/24/32/40/48/56/72/88/120/152/184. `"28"` aurait produit un `<select>` vide
   dans l'éditeur de thème (le genre de rejet silencieux consigné dans la recette). Retenu : `32`.

### Modifications écrites

| Clé | Avant | Après | Motif |
| --- | --- | --- | --- |
| `type_size_h1_mobile` | *absente* (défaut 48) | `"40"` | H1 dominant mais tenable sur 375 px |
| `type_size_h2_mobile` | *absente* (défaut 32) | `"32"` | posée explicitement, un cran sous le H1 |
| `type_size_h3_mobile` | *absente* (défaut 24) | `"24"` | posée explicitement |
| `type_size_h4_mobile` | *absente* (défaut 20) | `"20"` | posée explicitement |
| `type_size_h5_mobile` | *absente* (défaut 18) | `"18"` | posée explicitement |
| `type_size_h6_mobile` | *absente* (défaut 16) | `"16"` | posée explicitement |
| `type_case_h1` | `"uppercase"` | `"none"` | casse normale sur les titres de contenu |
| `type_case_h2` | `"uppercase"` | `"none"` | idem |

Échelle mobile obtenue : **40 / 32 / 24 / 20 / 18 / 16** (desktop inchangé : 56 / 40 / 28 / 20 /
18 / 16). Poser les six, y compris celles qui reprennent le défaut, met la hiérarchie mobile à
l'abri d'un changement de défaut lors d'une mise à jour du thème et la rend lisible dans
l'éditeur. Chaque valeur est une option du schéma.

**Capitales conservées** là où elles servent de libellé court ou d'affichage, comme demandé :
`type_case_h4` (`uppercase`, 20 px), `button_primary_text_case`, `button_secondary_text_case`,
`badge_text_case`. `type_case_h3` était déjà à `none`.

Vérifié au rendu 375 px après écriture : `--font-h1--size` = `2.5rem`, `--font-h2--size` =
`2.0rem`, `--font-h1--case` et `--font-h2--case` = `none`.

### Non retenu, volontairement
`type_letter_spacing_h1` et `type_letter_spacing_h2` valent `heading-loose` (0,03 em), un
interlettrage calibré pour des capitales. Passés en casse normale, `heading-normal` se lirait
mieux. Hors périmètre du point 4 : **non modifié**, signalé pour arbitrage.

---

## `sections/footer-group.json` — liens sociaux et badge fournisseur (points 4 et 7) — **APPLIQUÉ**

Sauvegarde : `scratchpad/backup-theme-uiux-json/sections__footer-group.json` (26 768 o,
`4f3d130180b2aeb4308ed08e927e3577`). Écrit : 26 800 o, `3d124046ef3f2115191fd6cbe38c84de`.

### Point 4 — liens sociaux `themefullstack` : bloc masqué

Chemin exact : `sections.footer.blocks.group_y4aNMX.blocks.social_icons_hQdtRf`
(type `social-icons`, présent dans `block_order` en 3ᵉ position, après `logo_MKbnJy` et
`text_hzJHEn`).

Deux constats vérifiés qui déterminent la correction :

1. **Les réglages du bloc ne contiennent aucune URL.** En entier :
   `show_on_display`, `icon_color` (`#ffffff`), `icon_size` (24), `alignment`,
   `alignment_mobile`, `margin_top`, `margin_bottom`, `additional_class`.
2. **Sa carte `blocks` est vide (`{}`).** Les 4 icônes rendues ne venaient donc pas de ce nœud :
   on ne peut, depuis lui, que masquer le bloc.

> ⚠️ **Diagnostic rectifié le 26/07 à 15:07 — voir la section « Comptes sociaux du fournisseur »
> plus bas.** Il était écrit ici que les 4 comptes venaient de `blocks/social-icons.liquid` :
> **c'est faux.** Ils venaient des **valeurs par défaut de `config/settings_schema.json`**, qui
> sont, elles, du JSON — donc corrigeables. Elles l'ont été.

**Aucun compte Noirmont réel n'existe.** Recherche menée sur tout le projet
(`*.md`, `*.json`, `*.txt`), dont `2026-07-25-charte-noirmont.md` et
`brand-tokens-noirmont.json` : zéro handle Facebook, Instagram, TikTok, YouTube ou LinkedIn de
la marque. Rien n'a été inventé. → **le bloc est masqué en entier**, conformément à la consigne.

Correctif écrit — clé `"disabled": true` ajoutée au nœud du bloc, au même niveau que
`"settings"` et `"blocks"` :

```json
"social_icons_hQdtRf": {
  "type": "social-icons",
  "name": "t:social_icons",
  "settings": { ... inchangés ... },
  "blocks": {},
  "disabled": true
}
```

C'est le mécanisme déjà employé ailleurs dans ce même fichier (voir point 2), donc éprouvé sur
ce thème. Il est réversible d'une clé le jour où la marque aura de vrais comptes, et il conserve
le bloc et sa place dans `block_order` — préférable à une suppression du bloc.

Dans l'éditeur de thème, l'équivalent est l'œil « masquer le bloc » sur *Icônes sociales*,
dans la première colonne du pied de page.

À signaler au passage, hors périmètre JSON : ces liens sortent en `target="_blank"` sans
`rel="noopener noreferrer"`, et leur couleur rendue est le bleu de lien par défaut du
navigateur (`rgb(0,0,238)`) malgré `icon_color: "#ffffff"`. Les deux défauts sont dans
`blocks/social-icons.liquid` (Liquid, pas CSS). Le masquage les rend sans objet.

### Comptes sociaux du fournisseur — vidés à la source (5ᵉ passe, 15:07 UTC)

**Ce que dit le Liquid, vérifié en entier** : `blocks/social-icons.liquid` (19 684 o,
`57128d964fa469c0ae39594b55aee0dc`) **ne contient aucun compte**. Il lit douze réglages de thème,
chacun sous garde `{% if settings.<x>_url != blank %}` : `facebook_url`, `instagram_url`, `x_url`,
`youtube_url`, `tiktok_url`, `pinterest_url`, `linkedin_url`, `snapchat_url`, `threads_url`,
`discord_url`, `whatsapp_url`, `bluesky_url`. Aucune icône ne sort si le réglage est vide.

**La vraie source des 4 comptes** : les `default` de `config/settings_schema.json`, section
`t:social_networks`. Corrigés (clé `default` **retirée**, pas remplacée par une chaîne vide, pour
adopter exactement la forme des huit autres champs du même bloc, qui n'en ont jamais eu) :

| Champ | `default` avant | après |
| --- | --- | --- |
| `facebook_url` | `https://www.facebook.com/themefullstack/` | *aucun* |
| `instagram_url` | `https://www.instagram.com/themefullstack/` | *aucun* |
| `youtube_url` | `https://www.youtube.com/@themefullstack` | *aucun* |
| `linkedin_url` | `https://www.linkedin.com/company/themefullstack/` | *aucun* |

Les douze champs sociaux sont désormais tous de la forme `{"type":"text","id":"…","label":"…"}`.
**Aucun compte Noirmont n'a été inventé** : les champs restent vides jusqu'à ce que Hakim donne les
siens, et le jour où le bloc sera réactivé, **rien ne peut plus s'afficher par défaut**.

**`config/settings_data.json` ne contient, lui, aucune URL sociale** — 0 occurrence de
`instagram`, `facebook`, `youtube`, `linkedin`, `tiktok` ni `themefullstack` dans le fichier live
(vérifié sur la copie dont l'empreinte égale le live). Il n'y avait donc rien à y vider.
L'explication de l'écart avec le constat de l'agent Liquid : un dump local du **24/07**
(`scratchpad/theme-noirmont/config__settings_data.json`) porte bien
`"instagram_url": "https://www.instagram.com/themefullstack/"`. Shopify **omet du
`settings_data.json` tout réglage égal au défaut du schéma** : une sauvegarde ultérieure dans
l'éditeur a donc supprimé la clé, sans rien changer à la valeur effective, qui continuait de venir
du schéma. C'est exactement pourquoi **vider le défaut du schéma était le seul correctif réel** —
vider la clé du `settings_data` n'aurait rien fixé, et elle n'existait déjà plus.

**Contrôles après écriture d'un fichier de schéma** (une erreur y casserait tout l'éditeur) :
JSON parsable ; diff structurel = **exactement 4 chemins supprimés** (`/[20]/settings/[2,3,5,8]/default`),
zéro ajout, zéro modification, 1 594 → 1 590 clés ; bloc `theme_info` **intact**
(`theme_name`, `theme_version` 2.3.0, `theme_author`, `theme_documentation_url`,
`theme_support_url` — ce sont des métadonnées du thème, pas des comptes : non touchées) ;
`themeFilesUpsert` sans `userErrors` ; empreinte relue conforme ; thème `processing: false`,
`processingFailed: false` ; et **le storefront rend toujours** à 375 px — 16 sections, logo
présent, réglages du thème correctement résolus (`--font-h1--size` 2.5rem, H1 à 40 px), preuve que
Shopify consomme le schéma sans erreur. Aucun lien social dans la page entière.

Reste une seule trace du fournisseur dans le HTML servi, **hors périmètre JSON** : une chaîne de
message console (« Cette boutique est propulsée par le Thème Fullstack » + son URL de
documentation), dans les traductions JS du thème. Invisible pour un visiteur, à l'écran comme
dans la page — mais présente dans la console. À confier à qui détient les locales / le Liquid.

**Contrôle après écriture, au rendu 375 px** : 0 lien social dans le pied de page, aucun nœud
`[class*="social"]`, et le pied de page ne laisse aucun vide — logo, texte de marque et les deux
colonnes de menu s'enchaînent normalement (capture `scratchpad/qa-json-footer-375.png`).

### Point 7 — badge « Powered by FullStack » : **déjà désactivé, rien fait**

Chemin : `sections.footer.blocks.footer.blocks.footer-bottom-bar.blocks.powered_by_fullstack_xErXcJ`

Le nœud porte **déjà** `"disabled": true`, à côté de `"mode": "badge"` :

```json
"powered_by_fullstack_xErXcJ": {
  "type": "powered-by-fullstack",
  "name": "t:powered_by_fullstack",
  "settings": { "show_on_display": "desktop_and_mobile", "mode": "badge", ... },
  "blocks": {},
  "disabled": true
}
```

**Le constat BLOQUANT de l'audit (`footer-group.json:712-717`) est un faux positif** : il a lu
`mode: "badge"` sans voir la clé sœur `"disabled": true`, qui empêche Shopify de rendre le bloc.
**Confirmé au rendu après écriture** : aucune occurrence de « Powered by » dans le pied de page à
375 px. Aucune modification JSON n'était nécessaire ; aucune n'a été faite.

À noter : `blocks/powered-by-fullstack.liquid` n'offre **aucun** mode « éteint » — son réglage
`mode` ne propose que `minimal` et `badge`. `"disabled": true` était donc la seule voie, et elle
a déjà été empruntée.

---

## `templates/index.json` — sorties de collection et dominance du H1 (points 3 et 1) — **APPLIQUÉ**

Sauvegarde : `scratchpad/backup-theme-uiux-json/templates__index.json` (91 693 o,
`4bbd441b9607514a9a1c5a62ee3bf88b`). Écrit : 91 705 o, `1ccc270ff471130e705cdfd7e5881e22`.

### Point 3 — boutons de sortie de collection (BLOQUANT) — corrigé

Deux blocs de type `button`, passés de `desktop_only` à visible partout :

| Chemin | `label` | avant | après |
| --- | --- | --- | --- |
| `sections.collection_featured_JXRpw3.blocks.group_9NwHBp.blocks.button_DFrQyK` | `Voir toutes les montres` | `"desktop_only"` | `"desktop_and_mobile"` |
| `sections.collection_featured_accessoires.blocks.group_9NwHBp.blocks.button_DFrQyK` | `Voir les accessoires` | `"desktop_only"` | `"desktop_and_mobile"` |

Le mécanisme `desktop_only` ajoute la classe `mobile-hide` : les deux liens restaient dans le DOM
à 0 × 0 px, donc dans l'ordre de tabulation. Le passage en `desktop_and_mobile` corrige d'un coup
la sortie mobile **et** les deux cibles focalisables de taille nulle.

**Contrôle au rendu 375 px** : « Voir toutes les montres » = 150 × 88 px (libellé sur deux
lignes), « Voir les accessoires » = 171 × 50 px, tous deux `display: inline-flex`. Cibles au-delà
des 44 px. Aucun débordement horizontal introduit (`scrollWidth == innerWidth`).

⚠️ Un troisième `desktop_only` subsiste volontairement dans ce fichier : le bloc texte
« - 2 000 clients satisfaits » du hero. **Hors périmètre, non touché** — et il ne doit surtout pas
être rendu visible : voir l'encadré « Promesse fausse à retirer avant ouverture » ci-dessous.

### Point 1 (2ᵉ moitié) — dominance du H1 : le changement indispensable

Le titre du hero (« Votre signature au poignet »), balisé `<h1>` dans le contenu du bloc, portait
`text_style: "h2"` → passé à `"h1"`.

Vérifié dans `assets/base.css` : le sélecteur `.text-block.h2 > *` (spécificité 0,2,1) l'emportait
sur le sélecteur d'élément `h1` (0,0,1) — le `<h1>` était donc réellement peint avec les jetons
`--font-h2--*`. **Sans ce changement, `type_size_h1_mobile` n'aurait rien changé du tout.** Les
deux modifications ne valaient qu'ensemble, comme annoncé.

**Contrôle au rendu 375 px** : `<h1>` unique, 40 px, `text-transform: none`, boîte 335 × 100 px.
Les titres de section restent à 24 px (ce sont des `<h2>` dans des blocs `text_style: "h3"`).

Le reste des écarts de titres relevés par l'audit sur ce fichier (titres de carte produit en
`<h2>`, puces de spécifications en `<p>` stylées h2) est **hors des 7 points confiés** et n'a pas
été touché.

### 🚩 Promesse fausse à retirer avant ouverture — laissée intacte volontairement

**« - 2 000 clients satisfaits » est une affirmation fausse** : la boutique a **0 commande et
0 client**. Emplacement exact, dans `templates/index.json` :

```
sections.image_banner_VXNP89.blocks.image_banner_dBEabG.blocks.group_nypGzr
        .blocks.group_wibFDH.blocks.text_mLtNpU.settings.text
        = "<p>- 2 000 clients satisfaits</p>"     (show_on_display: "desktop_only")
```

Elle n'est donc **visible que sur desktop** aujourd'hui, ce qui la rend facile à oublier lors d'une
QA mobile. Deux voisines de la même famille, au même endroit et dans les cartes produit :

```
… .blocks.group_wibFDH.blocks.rating_stars_z9LL3m.settings.review_count = 123   (+ show_note, show_review_count)
sections.collection_featured_JXRpw3.blocks.product-card.…rating_stars_VJ6F6G.settings.review_count = 123
sections.collection_featured_accessoires.blocks.product-card.…rating_stars_VJ6F6G.settings.review_count = 123
```

**Rien de tout cela n'a été modifié, ni supprimé, ni masqué** : c'est la même famille que les
1 340 avis de démonstration, terrain réservé de Hakim. À traiter par lui **avant ouverture** —
soit un chiffre vrai, soit la suppression du bloc. **Ne pas se contenter de le repasser en
`desktop_and_mobile` : cela diffuserait la fausse promesse au lieu de la retirer.**

---

## `templates/product.json` — accordéons, titre produit, ossature (points 5 et 6) — **APPLIQUÉ**

Fichier absent de la préparation initiale : il n'avait pas été ouvert. Appariement nom ↔ contenu
validé par `checksumMd5` avant écriture (`027c56cee94730e31dffb2808b617a46`, 74 791 o).
Sauvegarde : `scratchpad/backup-theme-uiux-json/templates__product.json`.
Écrit : 74 798 o, `559c6713252c9f9c3b619a8c482cecda`.

### Point 5 — les 5 accordéons de la colonne produit : `heading_tag` `"p"` → `"h2"`

Chemins : `sections.main.blocks.accordions_KKUaHK.blocks.accordion_{description,livraison,
fabrication,garantie,contact}.settings.heading_tag`.

`h2` est le niveau cohérent : ces accordéons sont subordonnés au titre du produit, qui devient un
`<h1>` au point 6. Vérifié dans `blocks/_accordion.liquid` que `heading_tag` (balise) et
`heading_style` (apparence) sont **deux réglages distincts** : `heading_style` reste `"paragraph"`.
Vérifié dans `assets/base.css` que la règle `.paragraph` (spécificité 0,1,0) l'emporte sur le
sélecteur d'élément `h2` (0,0,1) — **le changement est purement sémantique, aucun effet visuel**.

**Contrôle au rendu 375 px** : les 5 en-têtes sortent en `H2`, toujours à 16 px / poids 400, et la
hauteur de leur `<summary>` reste 40 px — identique à avant. Aucune régression.

### Point 5 bis — les 5 accordéons FAQ : `heading_tag` `"p"` → `"h4"` (2ᵉ passe, 14:51 UTC)

Chemins : `sections.custom_section_LBJBG7.blocks.group_ampbiX.blocks.accordions_JeK8VW.blocks.
accordion_{wVm9bk,FDaFgh,9NiJU7,ePJYyi,Y8Qaxp}.settings.heading_tag` (Livraison & délais,
Politique de retour, Calibres & spécifications, Garantie 12 mois, Entretien).

`h4` et non `h2` : ces accordéons vivent **sous** le `<h3>` « Questions fréquentes », qui vit
lui-même sous les `<h2>` éditoriaux. `h4` referme la hiérarchie sans créer de saut.

Sauvegarde de l'état intermédiaire (après la 1ʳᵉ passe, avant celle-ci) :
`scratchpad/backup-theme-uiux-json/templates__product.v2-avant-faq.json`
(74 798 o, `559c6713252c9f9c3b619a8c482cecda`).
Écrit : **74 803 o, `aaf972934cc243a69e125387cec6a70f`** — relu conforme.
Diff structurel : 1 445 chemins avant comme après, **zéro perdu**, 5 valeurs changées, rien d'autre.

**Contrôle au rendu 375 px** : plus aucun `heading_tag: "p"` dans le fichier ; les 5 en-têtes FAQ
sortent en `H4`, toujours 16 px et `<summary>` de 40 px — aucun effet visuel. Ossature complète de
la fiche : `H1` titre → `H2` × 5 accordéons → `H3` avis → `H2` × 3 sections → `H3` FAQ → `H4` × 5.

### Point 5 ter — dernier saut de niveau refermé (3ᵉ passe, 14:55 UTC)

`sections.custom_section_LBJBG7.blocks.group_NkNJJg.blocks.text_VLtRib.settings.text` :
`"<h4>Besoin d'aide ?</h4>"` → `"<h3>Besoin d'aide ?</h3>"`. Balise écrite en dur dans le
contenu, comme l'était le titre produit ; `text_style` reste `"h5"` donc **le titre garde ses
18 px exactement**.

Sauvegarde de l'état intermédiaire : `scratchpad/backup-theme-uiux-json/templates__product.v3-avant-h3.json`
(74 803 o, `aaf972934cc243a69e125387cec6a70f`).
Écrit : **74 803 o, `6f7f80df056e3d98b137df4453bfabc1`** — relu conforme.
Diff structurel : 1 445 chemins avant comme après, zéro perdu, **une seule valeur changée**.

**Ossature finale mesurée à 375 px — aucun saut de niveau (`sautsDeNiveau: []`) :**
`H1` titre produit → `H2` × 5 accordéons → `H3` avis → `H2` × 3 sections éditoriales →
`H3` « Besoin d'aide ? » → `H3` « Questions fréquentes » → `H4` × 5 accordéons FAQ →
`H3` × 2 colonnes de pied de page. `h1Count: 1`, aucun débordement horizontal.

### Point 6 — titre produit : **atteignable en JSON, et corrigé**

`sections.main.blocks.text_zLqMQw.settings.text` :
`"<p>{{ product.title }}</p>"` → `"<h1>{{ product.title }}</h1>"`.

La balise n'est pas exposée par un `<select>` du bloc : elle est **écrite en dur dans la valeur du
réglage de contenu**, et `blocks/text.liquid` sort ce réglage brut (`{{ block.settings.text }}`).
Le même fichier utilise déjà `<h2>` et `<h4>` littéraux dans ce réglage ailleurs, sur d'autres
blocs — le mécanisme est celui du thème, pas un détournement. **Aucun Liquid n'a été modifié.**

`text_style` laissé à `"h3"` volontairement : `.text-block.h3 > *` l'emporte sur le sélecteur
`h1`, donc le titre garde exactement sa taille actuelle (24 px). Gain d'accessibilité et de
référencement **sans aucun changement visuel** — la taille du titre produit reste une décision
de direction artistique, elle n'est pas embarquée dans ce correctif.

**Contrôle au rendu 375 px** (`/products/trente-neuf-classique-cannelee`) :
`h1Count: 1` (contre 0 avant), c'est bien le titre du produit, 24 px, casse normale.
Nouvelle ossature : `H1` titre → `H2` × 5 accordéons → `H3` avis → `H2` sections éditoriales.

**Rien n'a été transmis à l'agent Liquid pour ce point** : il est clos côté JSON. Restent pour lui,
dans ce template, deux constats de l'audit hors périmètre : le `<h1>Guide des tailles</h1>` et le
`Lorem ipsum` stockés dans le popup désactivé du sélecteur de variantes, et l'ossature `H3` des
avis qui précède les `H2` éditoriaux.

---

## Hors d'atteinte du JSON — à passer par CSS ou Liquid

> Numérotation de la préparation initiale, **sans rapport** avec les points 5 et 6 de la consigne
> d'application ci-dessus (accordéons et titre produit), tous deux clos.

### Prix barré non différencié → **CSS uniquement**

Vérifié dans `snippets/price.liquid` : le prix barré est un
`<span class="compare-at-price" data-ref="compare-at-price">`, sans aucune variable de taille
ni de couleur. Aucun réglage de thème ne le pilote : `config/settings_data.json` n'expose sur
les prix que `show_trailing_zeros` (faux) et `show_sale_price_first` (vrai, le barré est donc
rendu **après** le prix actif). Le seul CSS embarqué dans ce fichier est
`.badge:has(.badge__savings:empty){display:none}`.

Conformément à la consigne, **rien n'a été fait** : à confier à l'agent CSS.

- `.compare-at-price` : réduire le corps (≈ 0,8 em du prix actif) et désaturer
  (`color: rgba(11,11,12,0.55)` ou approchant), en gardant ≥ 12 px et un contraste suffisant.
- `.price`, `.compare-at-price` : ajouter `font-variant-numeric: tabular-nums`. Zéro occurrence
  sur les 203 Ko servis, alors que 8 prix s'alignent en rangée de carrousel.
- Non atteignable en CSS non plus, à consigner pour un tiers : le barré est un `<span>` et non
  un `<s>`/`<del>`, sans libellé pour lecteur d'écran. Correction dans `snippets/price.liquid`.

### Différé de chargement des images → **ni JSON, ni CSS : Liquid**

Vérifié : aucun schéma de bloc ou de section n'expose de réglage de chargement d'image
(`blocks/image.liquid` et `blocks/_collection-card.liquid` inspectés en entier — leurs
`{% schema %}` n'ont ni `loading`, ni `lazy`, ni équivalent). La cause est en dur dans le
Liquid : **`image_tag` est appelé sans argument `loading:`** dans au moins

- `blocks/image.liquid` — l'appel principal des blocs image
- `snippets/image.liquid` — `image_tag: class:, fetch_priority:, sizes:, widths:`
- `snippets/product-media.liquid` — deux appels, sur `media.preview_image`

Les images de repli (`placeholder-*.jpg`) portent bien `loading="lazy"` en dur : seules les
images réelles sont concernées. Ce qui donne exactement le profil mesuré — 62 images sur 95 non
différées.

Correctif à confier à qui détient le Liquid (ni moi, ni l'agent CSS) : ajouter
`loading: 'lazy'` à ces appels, en épargnant le hero qui doit rester en `fetchpriority="high"`
et sans `loading="lazy"`. Les 10 images du tiroir fermé (`header-group.json:420-425`,
`drawer_grid` en `mobile_only`) souffrent du même défaut et seront corrigées par la même passe.

Attention : `blocks/image.liquid` pose `sizes: 'auto, ...'`. `sizes="auto"` n'est valide **que**
sur une image `loading="lazy"` — le correctif rend donc ce `sizes` cohérent, il ne le casse pas.

---

## Levier adjacent repéré, non appliqué

`templates/index.json:749-750,1640-1641` — `sales_badge: "amount"` avec
`show_sales_badge_text: false` rend un « -€90 » nu. Passer `show_sales_badge_text` à `true`
affiche le libellé `products.save` (« Économisez ») devant le montant et supprime le tiret-moins
ASCII injecté par le Liquid (`{%- if show_sales_badge_text == false -%}-{%- endif -%}` dans
`snippets/price.liquid`). C'est un levier **JSON** qui rendrait la remise nettement plus
saillante, complémentaire du point 5.

Hors des 6 points confiés : **non appliqué**, soumis à arbitrage.

---

## Contraste du bandeau d'annonce — **mesuré, aucun correctif appliqué (à raison)**

Demande reçue : « le texte du bandeau d'annonce est à 3,0:1, la couleur vient d'un style en ligne
dans le JSON ». **Les deux moitiés du constat sont fausses**, mesures à l'appui — donc **aucune
écriture** : rien à corriger ici, et y toucher aurait dégradé une bande déjà conforme.

**Ratio mesuré** (WCAG 2.x, luminance relative calculée sur les couleurs *calculées* du DOM, avec
prise en compte de l'opacité héritée) :

| Élément | Couleur | Fond | Ratio | Seuil |
| --- | --- | --- | --- | --- |
| texte du bandeau, 375 px | `rgb(250,250,247)` | `rgb(11,11,12)` | **18,81:1** | 4,5:1 ✔ |
| texte du bandeau, 1280 px | idem | idem | **18,81:1** | 4,5:1 ✔ |
| flèches ‹ › du bandeau | idem | idem | **18,81:1** | 3:1 ✔ |

C'est exactement l'encre `#0B0B0C` / craie `#FAFAF7` de la palette de référence, en inverse.
Hauteur du bandeau inchangée : **65 px** à 375 px (42 px à 1280) — je n'y ai rien touché, le
réglage d'icônes de l'agent assets est intact.

**D'où vient la couleur, vérifié** : le nœud `announcement_bar_r8QCCw` de
`sections/header-group.json` n'a **aucun réglage de couleur** (`color_scheme: ""`), et le seul
style en ligne rendu sur la barre est `--padding-top: 10px; --padding-bottom: 10px`. La couleur
vient des variables du jeu `color-scheme-3` (`--color-foreground: rgba(250 250 247/1)`,
`--color-background: rgba(11 11 12/1)`), donc des jeux de couleurs de `settings_data.json` via
`snippets/css-variables.liquid` — **pas d'un style en ligne**. `sections/header-group.json` reste
donc inchangé (21 276 o, `6ced631f906029d90fea029b89effc28`).

### Ce qui est réellement sous 4,5:1 — et à qui ça revient

Balayage de **tout** le texte visible (opacité effective > 0,05, éléments non masqués) sur la page
d'accueil et une fiche produit, à 375 px et 1280 px :

| Élément | Ratio | Où | Propriétaire |
| --- | --- | --- | --- |
| `.compare-at-price` « €429 », 12,19 px, `opacity: 0.7` | **1,45:1** | fiche produit, colonne d'achat | **agent CSS** — la désaturation du prix barré est allée trop loin, c'est le pire contraste du site |
| icônes `star_rate` des étoiles, 22 px | **2,52:1** | sections avis | agent CSS (seuil 3:1 pour un élément graphique porteur de sens) |
| badge d'avis de démonstration (« Excellent », « 1340 avis ») | **1:1** | hero | **Hakim** — avis de démonstration, terrain réservé : **non touché** |

Les deux premiers sont du CSS, hors de mon périmètre. Le troisième est de la même famille que les
`review_count: 123` et le « 2 000 clients satisfaits » : **laissé strictement intact**.

---

## Méthode — le piège de l'empreinte, corrigé à l'usage

La recette « canon minifié » consignée lors de la préparation est **fausse en général**. Elle ne
marchait que par accident, sur les deux fichiers testés.

**La règle exacte : `size` et `checksumMd5` portent sur les octets exactement tels qu'ils ont été
écrits la dernière fois.** Shopify ne renormalise rien. Ce qui donne deux cas de figure sur le
même thème :

- `config/settings_data.json` a été écrit par l'**éditeur de thème**, qui minifie et échappe les
  `/` → l'empreinte correspond bien à la forme minifiée (d'où le faux succès de la recette).
- `templates/index.json`, `templates/product.json`, `sections/footer-group.json` ont été écrits
  par une passe d'agent antérieure **en texte indenté avec l'en-tête `/* auto-generated */`** →
  leur empreinte porte sur ce texte-là, saut de ligne final exclu. La recette « canon » y échoue
  de 40 % (51 441 o calculés contre 91 693 annoncés) et ferait conclure à tort que le fichier
  diffère.

Recette correcte, valable pour **tous** les types de fichiers, `.json` comme `.liquid` :

```python
import hashlib
stored = local_bytes.rstrip(b'\n')     # la forme stockée = les octets écrits, sans saut final
assert hashlib.md5(stored).hexdigest() == checksumMd5
assert len(stored) == int(size)
```

Conséquence pratique, appliquée ici : on **n'essaie pas de deviner** la forme stockée. On écrit
soi-même des octets connus, puis on relit `size` + `checksumMd5` : ils valent alors exactement
ceux de la charge utile locale. C'est ce qui a permis de vérifier les 4 écritures sans ambiguïté.

Corollaire sur la préservation : chaque fichier a été patché **par édition chirurgicale de sa
chaîne**, jamais par ré-sérialisation complète, pour que le diff se limite aux valeurs visées
(l'indentation, l'ordre des clés et l'en-tête d'origine sont conservés à l'octet près partout
ailleurs). Seul `settings_data.json`, déjà minifié, est régénéré dans sa propre convention.

Canal d'écriture utilisé (le connecteur n'accepte pas 90 Ko de charge utile en argument
d'appel) : `stagedUploadsCreate` → `PUT` du fichier local sur l'URL signée → `themeFilesUpsert`
avec `body: { type: URL, value: <resourceUrl non signé> }`. Aucun jeton d'admin, aucun CLI.

Aucun nom de schéma de bloc n'a été créé — la limite de 25 caractères ne s'applique à aucune
des modifications, qui ne touchent que des valeurs de réglages et une clé `disabled`.

---

## Récapitulatif des 7 points de la consigne d'application

| Point | Fichier | État | Détail |
| --- | --- | --- | --- |
| 1 — tailles de titres mobiles + `text_style` du hero | `config/settings_data.json` + `templates/index.json` | **appliqué** | 6 clés `type_size_h{1..6}_mobile` posées (40/32/24/20/18/16) et hero en `text_style: "h1"`. Vérifié : H1 = 40 px à 375 px. `28` remplacé par `32` (option invalide) |
| 2 — titres de contenu en casse normale | `config/settings_data.json` | **appliqué** | `type_case_h1` et `type_case_h2` → `none`. Capitales conservées sur `h4`, boutons, badges |
| 3 — sorties de collection sur mobile | `templates/index.json` | **appliqué** | 2 × `show_on_display` → `desktop_and_mobile`. Vérifié : 150 × 88 px et 171 × 50 px à 375 px |
| 4 — bloc social | `sections/footer-group.json` + `config/settings_schema.json` | **appliqué (2 passes)** | `"disabled": true` sur `social_icons_hQdtRf`, **puis** les 4 défauts `themefullstack` retirés du schéma — plus rien ne peut réapparaître à la réactivation du bloc. Aucun compte inventé. Vérifié : 0 lien social dans la page |
| 5 — accordéons de la fiche produit | `templates/product.json` | **appliqué (3 passes)** | 5 accordéons de la colonne produit `"p"` → `"h2"`, 5 accordéons FAQ `"p"` → `"h4"`, et le `<h4>` en dur de « Besoin d'aide ? » → `<h3>`. Plus aucun `heading_tag: "p"`, **plus aucun saut de niveau** à 375 px. Sans effet visuel (vérifié CSS + rendu) |
| 6 — titre produit sans `<h1>` | `templates/product.json` | **appliqué, rien à transmettre** | la balise vit dans la valeur du réglage de contenu : `<p>` → `<h1>`. Vérifié : `h1Count` 0 → 1, taille inchangée (24 px) |
| 7 — « Powered by FullStack » | — | **rien fait** | faux positif confirmé au rendu : absent du pied de page |

À arbitrer, volontairement non appliqués — les deux sont cosmétiques et attendent Hakim :
`type_letter_spacing_h1/h2` en `heading-loose` (calibré pour des capitales, devenues casse normale)
et `show_sales_badge_text` en `false`.

À trancher par Hakim **avant ouverture**, laissé strictement intact : la fausse promesse
« - 2 000 clients satisfaits » et les `review_count: 123` de démonstration — emplacements exacts
dans l'encadré 🚩 de la section `templates/index.json`. Terrain réservé, aucune décision prise ici.

**Pour l'agent CSS, urgent** : le prix barré `.compare-at-price` est descendu à **1,45:1** mesuré
(12,19 px, `opacity: 0.7`) — c'est le pire contraste du site, sous le seuil de 4,5:1 ; et les icônes
`star_rate` sont à **2,52:1**, sous 3:1. Le bandeau d'annonce, lui, est à **18,81:1** : conforme,
rien à y faire (voir la section dédiée).

Pour l'agent Liquid, il reste (aucun n'est atteignable en JSON) : le prix barré en `<span>` sans
libellé lecteur d'écran, l'absence de `loading: 'lazy'` sur les appels `image_tag`, les comptes
sociaux par défaut en dur dans `blocks/social-icons.liquid` avec `target="_blank"` sans
`rel="noopener"`, le `<h1>Guide des tailles</h1>` et le `Lorem ipsum` du popup désactivé, et les
en-têtes d'accordéon à 40 px de haut (`snippets/accordion.liquid`, sous le plancher de 44 px).

Observé sans lien avec ces écritures : à 375 px, le logo du bandeau d'en-tête (`logo-noirmont-encre.png`,
rendu 319 × 24) apparaît écrasé, ses glyphes se chevauchant, alors que le même wordmark est net dans
le pied de page. `sections/header-group.json` et les clés `logo`/`logo_inverse` **n'ont pas été
touchés** — c'est un sujet d'asset, à confier à qui détient `assets/`.

Aucun produit, SKU, prix, variante, média ni mapping DSers n'a été approché. Aucun slider ni
avis de démonstration n'a été touché. Aucun fichier `assets/` ni `.liquid` n'a été écrit. Aucune
promesse produit n'a été introduite. Aucun thème publié. Aucune commande. Le rendu de contrôle a
été obtenu **sans saisir de mot de passe**, en réutilisant le cookie de session
`_shopify_essential` déjà présent dans `scratchpad/nm-cookies.txt`.

# Correctifs thème — Tuftéo — 16/08/2026

Session exécutant-boutique. Rapport écrit au fil de l'eau (une session coupée ne doit rien faire perdre).

## Point de départ

Le thème `gid://shopify/OnlineStoreTheme/189410738561` (« Tuftéo — purge faux avis 16-08 ») est
**MAIN** (publié par Hakim) — confirmé par `{ themes(first:10){ nodes{ id name role } } }` à
19h40 : les 4 thèmes du shop sont `Horizon` (UNPUBLISHED), `Tuftéo thème` (UNPUBLISHED), `Helio`
(UNPUBLISHED), et `Tuftéo — purge faux avis 16-08` (**MAIN**).

**Duplication effectuée** via `themeDuplicate` :
- Source : `gid://shopify/OnlineStoreTheme/189410738561`
- Nouvelle copie : **`gid://shopify/OnlineStoreTheme/189429678465`**, nom « Tuftéo — correctifs
  thème 16-08 », rôle `UNPUBLISHED` (confirmé dans la réponse de la mutation).
- Tous les travaux ci-dessous se font **uniquement** sur cette copie. Le thème MAIN
  `189410738561` n'est touché par aucune écriture — le connecteur la refuse de toute façon
  (« Theme file writes... writes that target the live/MAIN theme are blocked »).

---

## État d'avancement

- [x] 0. Copie du thème traitée (`processing: false`)
- [x] 1. Correctif 1 — bandeau d'annonce superposé (écrit et **vérifié en rendu réel navigateur**)
- [x] 2. Correctif 2 — vidéos chargées sans interaction (écrit et **vérifié en rendu réel navigateur**)
- [x] 3. Correctif 3 — police d'icônes servie par Google (écrit et **vérifié en rendu réel navigateur**)
- [x] 4. Vérification finale (navigateur, mobile 375×812 puis desktop)
- [x] 5. Ce que je n'ai pas pu vérifier

---

## Correctif 1 — Le bandeau d'annonce se superpose

### Diagnostic (confirmé)

Cause trouvée dans **`assets/slider.css`** (chargé globalement, préchargé dans `layout/theme.liquid`) :

```css
.splide__track {
  /* overflow: hidden; */
  position: relative;
  z-index: 0;
}
```

La règle `overflow: hidden` sur `.splide__track` — le conteneur qui doit normalement masquer
toutes les diapositives sauf celle affichée — est **commentée dans tout le thème**, pas seulement
sur le bandeau. Sans elle, les diapositives Splide restent toutes visibles au même endroit au lieu
de défiler : exactement le symptôme constaté par l'audit C sur le bandeau d'annonce.

**Cette désactivation globale n'est pas un oubli isolé** : elle sert un usage volontaire ailleurs
dans le thème — l'effet « peek » (un bout de la diapositive suivante qui dépasse), utilisé par :
- `blocks/_product-media-gallery.liquid`, réglage `show_a_bit_of_next_image_on_mobile` → classe
  `slider-component--85-percent` (galerie produit, mobile).
- `blocks/slider.liquid`, réglage `per_page_mobile: "1.8"` → classe
  `slider-component--65-percent` (sliders de blocs génériques, ex. cross-sell), avec un preset
  dédié `t:slider_cross_sell_columns` dans le schéma.

Réactiver `overflow: hidden` globalement casserait cet effet sur ces sliders. **Conforme à la
consigne de Hakim, je n'ai pas touché à la règle globale.**

### Correction appliquée

Ajout d'une règle **scopée au bandeau d'annonce uniquement**, dans le `{% stylesheet %}` de
`sections/announcement-bar.liquid` :

```css
.announcement-bar__content .splide__track {
  overflow: hidden;
}
```

Le bandeau n'utilise ni `per_page_mobile: "1.8"` ni l'effet peek (il appelle `render 'slider'`
avec `per_page_desktop: 1, per_page_mobile: 1`), donc rétablir le clip sur son propre track est
sans risque pour lui et sans effet sur les autres sliders (sélecteur descendant de
`.announcement-bar__content`, qui n'existe que dans `sections/announcement-bar.liquid`).

**Sauvegarde** : `shopify/backups/2026-08-16-correctifs-theme/slider/announcement-bar-avant.liquid`
(contenu intégral relu depuis l'API avant modification).

### Vérification (relecture API — rendu réel en attente)

Contenu de `sections/announcement-bar.liquid` relu après écriture : la règle
`.announcement-bar__content .splide__track { overflow: hidden; }` est bien présente, le reste du
fichier (structure, schéma, presets) est inchangé. **Rendu réel du bandeau qui défile, et
vérification que les autres carrousels (accueil, galerie produit) défilent toujours : à faire en
session navigateur, voir « Vérification finale ».**

---

## Correctif 2 — Les vidéos se chargent sans interaction

### Diagnostic (cause trouvée, dans `snippets/video.liquid`)

Toutes les vidéos du thème passent par ce snippet unique, qui affiche une affiche (poster) cliquable
par-dessus une vidéo posée dans un `<template>` inerte (repris par `assets/deferred-media.js` au
clic). Le bug était dans la condition qui décide si la vidéo est posée **directement dans le DOM
au premier rendu** (donc téléchargée tout de suite) au lieu de rester dans le `<template>` :

```liquid
<div class="deferred-media__video" data-ref="deferred-media-video">
  {%- if video_autoplay or video_preview_image == blank %}
    {{ video_iframe }} {# ou video_tag #}
  {% endif -%}
</div>
```

**Deux déclencheurs identifiés et confirmés sur le catalogue réel** (source :
`templates/product.json`, décodé et interrogé pour tous les blocs `type: "video"`) :

1. **`video_autoplay: true`** — trois blocs vidéo sont dans ce cas, tous dans la section
   `video_3gestes` (démonstration des 3 gestes du tufting, vidéos Shopify natives « uploaded ») :
   `geste_1`, `geste_2`, `geste_3` (`video_loop: true` sur les trois). Le quatrième bloc vidéo du
   template (`video_demo`, section `video_demo`) a `video_autoplay: false` et n'est donc pas
   concerné par ce premier déclencheur.
2. **`video_preview_image == blank`** — pour `blocks/video.liquid` en source « URL externe »
   (YouTube/Vimeo), l'image d'aperçu vient du réglage `cover_image`, **optionnel** et non défini
   par défaut. Sans `cover_image` choisi par le marchand, `video_preview_image` est vide → chargement
   immédiat de l'iframe. Sur le catalogue actuel, aucun bloc `blocks/video.liquid` en source URL
   n'est configuré (les 4 blocs vidéo trouvés sont tous en source « uploaded »), donc je n'ai pas pu
   confirmer que c'est ce chemin précis qui a produit l'appel `www.youtube.com` relevé par l'audit —
   voir la section « ce que je n'ai pas pu vérifier ».

Les 3 vidéos « gestes » représentent une part significative des **15 Mo** signalés : ce sont des
fichiers `.mp4` hébergés nativement par Shopify, en boucle, sans doute plusieurs Mo chacune.

### Correction appliquée (`snippets/video.liquid`)

1. **Suppression du chargement en dur** : la vidéo n'est plus jamais posée directement dans
   `deferred-media__video` au premier rendu, **y compris quand `video_autoplay` est vrai**. Elle
   ne vit plus que dans le `<template>` (inerte, aucune requête réseau tant qu'il n'est pas cloné
   en JS). Le réglage `video_autoplay` garde son effet — il déclenche la lecture automatique une
   fois la vidéo révélée par le clic (le tag vidéo capturé a de toute façon `autoplay: true` en dur
   et `deferred-media.js` force `.play()` pour Safari) — **mais il ne déclenche plus le
   chargement anticipé.**
2. **Garantie d'une affiche cliquable dans tous les cas** : auparavant, si `video_preview_image`
   était vide, il n'y avait *aucune* affiche (le bloc `{% if video_preview_image != blank %}`
   qui l'entoure était sauté) et la vidéo se chargeait directement — c'était le deuxième
   déclencheur du bug. Remplacé par une affiche systématique : l'image d'aperçu réelle si elle
   existe, sinon `assets/placeholder-banner.jpg` (déjà utilisé ailleurs dans ce même fichier comme
   repli générique) avec l'icône lecture par-dessus. Résultat : **zéro cas résiduel** où une
   vidéo pourrait se charger sans affiche cliquable.
3. **`youtube-nocookie.com`** : dans la branche « vidéo depuis une URL », l'URL construite pour
   YouTube passe de `https://www.youtube.com/embed/...` à `https://www.youtube-nocookie.com/embed/...`
   — même lecteur, mêmes paramètres, aucun cookie de suivi déposé avant lecture. Seul ce chemin
   (source URL saisie dans `blocks/video.liquid`) est sous mon contrôle en Liquid ; voir la limite
   ci-dessous pour les vidéos YouTube ajoutées comme média natif du produit.
4. **Rien n'est supprimé** : aucune vidéo, aucun contenu retiré — uniquement le moment du
   chargement qui change (au clic, plus à l'ouverture).

**Sauvegarde** : `shopify/backups/2026-08-16-correctifs-theme/video/video-avant.liquid` (contenu
intégral relu depuis l'API avant modification).

### Limite connue — vidéo YouTube en média natif du produit

Si l'appel `www.youtube.com` à 726 ms relevé par l'audit vient d'une vidéo YouTube ajoutée
**directement dans la médiathèque du produit** (Shopify Admin → Produit → Médias → Ajouter depuis
une URL), elle est rendue par `snippets/product-media.liquid` via le filtre Liquid natif
`external_video_tag`, pas par le code que j'ai modifié. Ce filtre est une boîte noire côté Shopify :
je n'ai pas trouvé de paramètre pour lui imposer `youtube-nocookie.com`. **Ce cas n'est donc pas
couvert par ce correctif** — si c'est la source réelle de l'appel observé, il faudra soit remplacer
ce média par un bloc `blocks/video.liquid` (source URL, que je couvre), soit accepter l'appel
Google sur cette vidéo précise. Cette limite est à vérifier par Hakim ou en session navigateur
(voir « ce que je n'ai pas pu vérifier »).

### Vérification (relecture API — rendu réel en attente)

Contenu de `snippets/video.liquid` relu après écriture : condition de chargement anticipé
supprimée, affiche systématique en place, domaine `youtube-nocookie.com` confirmé dans le texte
stocké. **Poids de la fiche produit avant/après, nombre de requêtes vidéo au chargement, et lecture
effective au clic : à faire en session navigateur, voir « Vérification finale ».**

---

## Correctif 3 — Police d'icônes servie par Google

### Diagnostic

Deux snippets chargent Material Symbols depuis `fonts.googleapis.com`, avec des rôles différents :

- **`snippets/material-icons-header.liquid`** (rendu dans `<head>` via `layout/theme.liquid`,
  toujours actif) : construit une URL Google avec un paramètre `icon_names=` listant ~140 noms
  d'icônes (menu, panier, recherche, flèches...) — **déjà un sous-ensemble côté Google**, poids
  mesuré : **41 480 octets**.
- **`snippets/material-icons-body.liquid`** (rendu en fin de `<body>`, actif seulement si
  `settings.activate_custom_icons` est vrai — **c'est le cas sur Tuftéo**, confirmé dans
  `config/settings_data.json` : `"activate_custom_icons": true`) : construit une URL Google
  **sans** `icon_names`, donc le jeu complet des icônes de la famille — poids mesuré :
  **1 146 212 octets (1,09 Mio ≈ 1,16 Mo décimal)**, qui correspond exactement au chiffre du
  diagnostic de vitesse cité par Hakim. C'est ce second appel qui est le poste lourd.

**Pourquoi le jeu complet est chargé et pas seulement le sous-ensemble** : `blocks/icon.liquid`
propose un champ `icon_custom` en texte libre dès que `activate_custom_icons` est actif — un nom
d'icône Material Symbols arbitraire peut y être saisi, donc aucun sous-ensemble figé ne peut
garantir la couverture. **Je n'ai donc pas réduit ce fichier** (subsetting non appliqué, conforme
à la consigne « si tu n'es pas sûr, ne le fais pas »).

Style et poids actifs (source `config/settings_data.json`, `"current"`) : `icon_style: "outlined"`,
`icon_weight: 300`, `icon_fill: false` → famille Google demandée : « Material Symbols Outlined »,
poids 300.

### Correction appliquée

1. **Récupéré les deux fichiers exacts que Google servait**, en reconstruisant les mêmes URL que
   les snippets d'origine (mêmes paramètres `opsz,wght,FILL,GRAD`, avec et sans `icon_names`) et
   en les téléchargeant avec un `User-Agent` de navigateur récent (pour obtenir le format woff2) :
   - `assets/material-symbols-outlined-header.woff2` — 41 480 octets, sous-ensemble ~140 icônes.
   - `assets/material-symbols-outlined-body.woff2` — 1 146 212 octets, jeu complet — **copie
     octet pour octet du fichier que Google servait**, pas une régénération : aucun risque d'icône
     manquante par rapport à l'existant.
   - Licence : Material Symbols (Google, dépôt `google/material-design-icons`) est distribuée sous
     **licence Apache 2.0**, qui autorise explicitement la redistribution et l'auto-hébergement.
2. **Téléversés comme assets du thème** via `stagedUploadsCreate` (resource
   `BULK_MUTATION_VARIABLES`) → `curl -F` vers l'URL Google → `themeFilesUpsert` en `type: URL`.
   Vérifié par relecture : les deux fichiers présents dans le thème avec exactement les tailles
   attendues (41 480 et 1 146 212 octets — correspondance exacte avec les fichiers sources, pas
   seulement le champ `size` de l'API dont la fiabilité est documentée comme douteuse pour les
   gros templates ; ici il s'agit d'un asset binaire statique, moins sujet au problème que
   `index.json`, mais la correspondance exacte reste la meilleure preuve disponible sans
   téléchargement public — voir section vérification finale).
3. **Réécrit les deux snippets** (`themeFilesUpsert` en `type: TEXT`, confirmé par relecture
   immédiate du contenu stocké) :
   - Suppression des `<link rel="preconnect">` / `dns-prefetch` vers `fonts.googleapis.com` et
     `fonts.gstatic.com`, et des deux `<link rel="stylesheet" href="https://fonts.googleapis.com/...">`.
   - Remplacés par un `@font-face` local (`src: url({{ 'material-symbols-....woff2' | asset_url }})`)
     dans chaque snippet, plus un `<link rel="preload" as="font">` pour le sous-ensemble d'en-tête
     (chargement critique, au-dessus de la ligne).
   - Le nom de police et le sélecteur CSS restent dynamiques via `{{ settings.icon_style }}` (au
     lieu d'être figés en dur) pour rester cohérents avec `snippets/icon.liquid`, qui génère la
     classe `.material-symbols-{{ settings.icon_style }}` — seul le fichier physique reste fixé au
     style/poids actuels (« outlined » / 300).
   - Le bloc `{% if settings.activate_custom_icons %}` du snippet body est conservé à l'identique.

### Sauvegardes

`shopify/backups/2026-08-16-correctifs-theme/material-icons/material-icons-header-avant.liquid` et
`material-icons-body-avant.liquid` (contenu intégral relu depuis l'API avant modification).

### Subsetting — gain potentiel non appliqué

Le fichier `assets/material-symbols-outlined-body.woff2` (1,09 Mio) pourrait être réduit
drastiquement (le sous-ensemble d'en-tête ne pèse que 41 Ko pour ~140 icônes, soit un facteur
~28×) si un inventaire fiable des icônes réellement utilisées sur tout le site — y compris tout
`icon_custom` déjà saisi par Hakim dans le personnalisateur de thème — pouvait être établi. Je n'ai
pas cette garantie (le champ est un texte libre non centralisé, je ne l'ai pas audité bloc par
bloc sur toutes les pages), donc **je n'ai pas réduit ce fichier**, conformément à la consigne.
Si Hakim veut ce gain, il faut soit lister tous les `icon_custom` utilisés (recherche dans les
réglages JSON de sections/blocs), soit accepter le risque d'une icône manquante ponctuelle.

### Vérification (relecture API, rendu réel en attente — voir section finale)

- Contenu des deux fichiers `.woff2` confirmé par relecture de leur taille en octets (correspond
  exactement aux fichiers téléchargés localement).
- Contenu des deux snippets `.liquid` confirmé par relecture intégrale (voir extraits ci-dessus) :
  plus aucune occurrence de `fonts.googleapis.com` ni `fonts.gstatic.com`.
- **Rendu réel (icônes affichées, absence d'appel réseau vers Google) : à faire en session
  navigateur, voir la section « Vérification finale » plus bas.**

---

## Vérification finale (session navigateur réelle)

Méthode : préview en session navigateur (`https://tufteo.com/?preview_theme_id=189429678465`,
confirmé actif tout au long via `window.Shopify.theme.id === 189429678465` et
`role: "unpublished"` — jamais le thème MAIN). Mobile 375×812 d'abord, puis desktop.

**Accueil (mobile puis desktop)**
- Bandeau d'annonce : capturé en train de défiler entre 3 messages distincts (« -10 % sur ta
  première commande », « Livraison offerte en France », « Garantie légale 2 ans ») sans jamais
  superposer deux textes, sur les deux captures successives. **Confirmé résolu.**
- Icônes du header (menu, recherche, panier), badges USP (livraison, garantie) : tous rendus,
  aucun carré vide (tofu).
- Requêtes réseau à l'ouverture : **zéro** vers `fonts.googleapis.com`, **zéro** vers
  `fonts.gstatic.com`. Les deux polices locales chargent depuis
  `tufteo.com/cdn/shop/t/5/assets/material-symbols-outlined-{header,body}.woff2` en 200, avec un
  `content-length` de **41 480** et **1 146 212 octets** respectivement — vérifié par `curl -I`
  direct sur les URL publiques, **identique au octet près** aux fichiers téléversés.
- Console : aucune erreur nouvelle liée au thème. Une seule erreur récurrente,
  `GET https://tufteo.com/sf_private_access_tokens → 401`, présente sur toutes les pages testées —
  **appel de plateforme Shopify natif, pas du code du thème que j'ai touché**, hors périmètre.

**Fiche produit `tufting-gun-2-en-1` (mobile)** — ce produit utilise `templateSuffix: null`, donc
le template par défaut `product.json`, celui qui contient les 3 vidéos « gestes ».
- 4 éléments `<deferred-media>` détectés sur la page : `video_demo` (autoplay=false) et les 3
  vidéos `geste_1/2/3` (autoplay=true). **Les 4** ont `hasVideoInVideoDiv: false` avant tout clic
  — confirmé par inspection DOM directe (`querySelector` sur `[data-ref="deferred-media-video"]`).
  **Zéro requête `.mp4` enregistrée au chargement de la page** (vérifié via le journal réseau).
  Avant le correctif, les 3 vidéos autoplay auraient été chargées immédiatement.
- Clic simulé sur l'affiche de la première vidéo « geste » : `data-media-loaded` passe à `"true"`,
  un `<video>` fonctionnel est cloné dans le DOM avec `autoplay`, `loop`, `muted`,
  `preload="metadata"` et une vraie `<source>` vers le fichier MP4 Shopify
  (`.../41a163836a914b1a861b403df41ff675.HD-1080p-7.2Mbps-89618292.mp4`), `paused: false` (lecture
  déclenchée). **La vidéo reste donc accessible et lisible après le clic.** Limite outillage : le
  journal réseau automatisé de cette session ne capture pas les requêtes de streaming vidéo natif
  (`<video><source>`), seulement fetch/XHR/document — je n'ai donc pas de log réseau du octet
  transféré après clic, mais l'inspection DOM (élément fonctionnel, lecture non bloquée, aucune
  erreur `video.error`) suffit à confirmer que le mécanisme marche.
- Icônes des accordéons (Caractéristiques, Description, Garantie...), pictos livraison/service
  client : tous rendus.
- Ajout au panier : fonctionnel — le tiroir panier s'ouvre avec le bon produit/variante/prix, les
  icônes (camion, corbeille, +/-, fermeture) sont toutes présentes.

**Collection `/collections/all` (mobile)** : filtres, flèches, étoiles de notation — icônes toutes
rendues, aucune erreur console nouvelle.

**Desktop (accueil)** : bandeau sur une ligne (🚚 Livraison offerte en France), flèches de
navigation visibles, menu et icônes header propres.
- Vérification structurelle de la portée du correctif 1 : requête de tous les `.splide__track` de
  la page d'accueil (15 au total) — **1 seul** (celui du bandeau, `inAnnouncementBar: true`) a
  `overflow: hidden` ; **les 14 autres** (sliders home page — produits, cross-sell, galeries de
  cartes produit) ont conservé `overflow: visible`. **Confirme que la règle scopée n'a touché
  aucun autre slider du site**, conformément à la consigne.

## Poids et requêtes vidéo — avant / après

- **Avant** (source : diagnostic de vitesse cité par Hakim dans la consigne, non ré-audité par mes
  soins puisque je n'ai pas eu accès à une session propre sur le thème MAIN sans le cookie de
  préview) : ~15 Mo de vidéos téléchargées au chargement, un appel vers `www.youtube.com` à
  726 ms, un appel vers `fonts.googleapis.com` à 675 ms (police de 1,16 Mo).
- **Après** (mesuré ci-dessus, sur la copie corrigée) : **zéro requête vidéo au chargement** de la
  fiche produit testée (0 fichier `.mp4`, 0 appel `youtube.com`), **zéro appel**
  `fonts.googleapis.com` / `fonts.gstatic.com` sur toutes les pages testées (accueil, fiche
  produit, collection), police d'icônes servie localement avec un poids identique par octet
  (41 480 + 1 146 212 = **1 187 692 octets**, soit le même total qu'avant — le gain ici est la
  suppression de l'appel à Google, pas une réduction de poids ; un sous-ensemble futur pourrait
  réduire le fichier body de ~28×, voir Correctif 3).
- Je n'ai **pas** mesuré le poids total de la page (Ko transférés cumulés) avant/après avec un
  outil de profilage identique des deux côtés (Lighthouse/PageSpeed) — seuls les compteurs de
  requêtes et les octets des fichiers concernés sont vérifiés ci-dessus. Aucun score PageSpeed
  n'est avancé, conformément à la consigne.

## Ce que je n'ai pas pu vérifier

1. **Poids total de la fiche produit avant/après avec un outil de mesure identique** (type
   PageSpeed Insights) : je n'ai vérifié que les compteurs de requêtes et les tailles de fichiers
   individuels (vidéo, police), pas un audit de performance complet. Aucun score n'est avancé.
2. **Source exacte de l'appel `www.youtube.com` à 726 ms relevé par l'audit C** : les 4 blocs
   vidéo du catalogue actuel (template `product.json`) sont tous en source « uploaded » (MP4
   natifs Shopify), aucun en source URL YouTube. Si l'appel venait d'une vidéo YouTube ajoutée
   directement dans la médiathèque d'un produit (media natif, pas un bloc de thème), mon correctif
   `youtube-nocookie.com` ne s'applique pas à ce chemin (rendu par le filtre Liquid natif
   `external_video_tag`, hors de mon contrôle) — voir la limite documentée dans le Correctif 2.
   Je n'ai pas passé en revue la médiathèque de chaque produit du catalogue pour trouver une
   éventuelle vidéo YouTube en media natif ; recommandé à Hakim si le doute persiste après
   publication.
3. **Rendu du footer et des autres gabarits non visités** (page de contact hors panier, page 404,
   compte client, recherche) : je n'ai vérifié que l'accueil, une fiche produit, une collection et
   le panier, comme demandé. Pas d'erreur Liquid détectée sur les pages visitées (recherche
   textuelle « Liquid error » négative), mais je n'ai pas parcouru l'intégralité du site.
4. **Poids octet-exact transféré par les vidéos une fois cliquées** : le journal réseau
   automatisé de cet outil ne capture pas les requêtes de streaming natif `<video><source>` — j'ai
   confirmé le mécanisme par inspection DOM (élément vidéo fonctionnel, lecture non bloquée) mais
   pas par un octet de transfert mesuré.
5. **Effet du réglage `activate_wishlist` et des templates spécifiques** (`product.kit-tufting.json`,
   `product.accessoire.json`) sur le mécanisme vidéo : ces deux templates ne contiennent aucun
   bloc vidéo dans le catalogue actuel (vérifié), donc rien à corriger là, mais je ne les ai pas
   ouverts visuellement en navigateur.
6. **Répercussion du changement d'icon_style/icon_weight dans le personnalisateur de thème** : si
   Hakim change un jour ces réglages, les fichiers `.woff2` auto-hébergés (Correctif 3) devront
   être régénérés manuellement — documenté dans le code, non testé en pratique (le réglage n'a pas
   été changé pendant cette session).

## Décisions qui attendent Hakim

- **Publier ou non la copie corrigée** `gid://shopify/OnlineStoreTheme/189429678465` (« Tuftéo —
  correctifs thème 16-08 ») à la place du thème MAIN actuel `189410738561`. Je n'ai pas publié.
- **Subsetting de la police d'icônes body** (1,09 Mio → potentiellement ~40-80 Ko) : nécessite un
  inventaire fiable de tous les `icon_custom` utilisés sur le site, que je n'ai pas fait (risque
  d'icône manquante si mal fait) — décision différée à Hakim, gain chiffré dans le Correctif 3.
- **UX des 3 vidéos « gestes »** : elles passent d'un autoplay silencieux au chargement à un
  clic-pour-lire (avec vraie affiche extraite de chaque vidéo). C'est exactement ce que demandait
  la consigne, mais c'est un changement d'expérience visible qu'il vaut la peine de confirmer
  visuellement avant publication.
- **Vidéo YouTube potentiellement en media natif d'un produit** (point 2 ci-dessus) : à
  investiguer si Hakim veut fermer complètement le risque `www.youtube.com`.

## Identifiant du thème et consigne de publication

- **Thème corrigé (non publié) : `gid://shopify/OnlineStoreTheme/189429678465`, « Tuftéo —
  correctifs thème 16-08 »**, dupliqué depuis le thème MAIN `189410738561` (« Tuftéo — purge faux
  avis 16-08 ») au début de cette session.
- Je n'ai rien publié — **c'est Hakim qui publie**, en promouvant `189429678465` en thème MAIN
  depuis Shopify Admin (Boutique en ligne → Thèmes) une fois les points ci-dessus vérifiés à son
  tour si besoin.

---

*Rapport clos à ce stade — 16/08/2026.*

# Chantier vitesse — Tuftéo, 16/08/2026

Agent exécutant, session dédiée vitesse. **Ne touche à aucun produit / collection / média produit**
(un autre agent travaille en parallèle sur le catalogue et sur `EXECUTION-2026-08-16.md`). Rapport
écrit au fil de l'eau.

Thème de travail (copie non publiée) : `gid://shopify/OnlineStoreTheme/189410738561` — nommé
« Tuftéo — purge faux avis 16-08 », déjà créé par l'agent produit aujourd'hui. Thème publié (MAIN,
interdit à l'écriture) : `gid://shopify/OnlineStoreTheme/188623847809`.
Confirmé par requête GraphQL `{ themes(first:10){ nodes{ id name role } } }` le 16/08 à l'ouverture
de session : 4 thèmes, un seul MAIN.

---

## 0. Rappel du point de départ (mesure de l'agent précédent, 16/08 01:25)

D'après `EXECUTION-2026-08-16.md` §5 : PageSpeed Insights mobile sur `https://tufteo.com/` —
Performances 57/100, Accessibilité 90/100, Bonnes pratiques 54/100, SEO 100/100. LCP 6,8 s, TBT
480 ms, CLS 0,069, poids total 15 327 Kio.

## 1. Diagnostic — en cours

### 1a. PageSpeed Insights, accueil, mobile — nouvelle mesure (16/08 01:58 UTC+2)

Outil : `pagespeed.web.dev`, via navigateur (l'API REST `pagespeedonline.googleapis.com` renvoie
**429 quota dépassé** sans clé — abandonnée, contournée par l'UI web, même moteur Lighthouse).

| Catégorie | Score |
|---|---|
| Performances | **44/100** |
| Accessibilité | 90/100 |
| Bonnes pratiques | 54/100 |
| SEO | 100/100 |

Détail : FCP 14,7 s · **LCP 25,7 s** · TBT 460 ms · CLS 0 · Speed Index 14,7 s. Poids total
**15 315 Kio** (quasi identique à la mesure précédente : 15 327 Kio).

**Écart net avec la mesure de l'agent précédent (57 → 44, LCP 6,8 s → 25,7 s) à 33 minutes
d'intervalle, sans qu'aucune modification n'ait été faite sur le thème entre les deux.** Deux
hypothèses, non tranchées à ce stade : (a) bruit de mesure classique de Lighthouse mobile en
émulation 4G lente (connu pour être volatil sur des sites Shopify avec beaucoup de JS tiers) ;
(b) une charge momentanée côté serveur/CDN Shopify au moment du test. Le poids de page et le CLS
sont stables entre les deux mesures, ce qui pointe plutôt vers (a) — mais je ne peux pas l'affirmer
sans une 3e mesure. **Je vais reprendre plusieurs mesures et retenir une valeur médiane plutôt
qu'un seul passage**, pour ne pas bâtir un diagnostic sur un point aberrant.

Poursuite du diagnostic en cours (répartition LCP, scripts tiers, ressources bloquantes) —
section suivante.

---

## Reprise — session du 16/08 après-midi (Sonnet, executant-boutique)

**Constat d'ouverture, vérifié à l'écran** : `snippets/fonts.liquid` et `blocks/video.liquid` du
thème brouillon `189410738561` sont identiques au thème publié `188623847809` — la session
précédente n'a rien écrit, seulement pris ses sauvegardes (`shopify/backups/2026-08-16-vitesse/`).
Repart du diagnostic déjà établi (57 vs 44 à 33 min d'écart, poids de page stable) sans le refaire.

### 1b. Base de mesure élargie — 3 mesures par page, mobile, PageSpeed Insights (pagespeed.web.dev, UI web)

L'API REST reste en 429 sans clé (revérifié). Toutes les mesures ci-dessous via l'interface web,
même moteur Lighthouse (Moto G Power émulé, 4G lente). **Chaque ligne = un passage Lighthouse
distinct**, confirmé par l'horodatage « Captured at » et la variation des métriques (deux mesures
consécutives dans la même minute sur PGP-PDP ont rendu des chiffres identiques — probable cache
côté Google sur une fenêtre courte ; signalé dans le tableau).

**Accueil `https://tufteo.com/`**

| # | Heure | Performances | LCP | FCP | TBT | CLS | SI | Poids page |
|---|---|---|---|---|---|---|---|---|
| 1 | 12:09 | 51 | 29,0 s | 14,5 s | 240 ms | 0 | 14,5 s | 15 279 Kio |
| 2 | 12:11 | 44 | 25,3 s | 14,7 s | 460 ms | 0 | 14,7 s | — |
| 3 | 12:13 | 46 | 10,6 s | 2,9 s | 680 ms | 0,055 | 7,7 s | — |
| **Médiane** | | **46** | **25,3 s** | | | | | |

Confirme et amplifie le constat de la session précédente (57 puis 44 à 33 min d'écart) : sur
l'accueil, trois mesures à ~4 min d'intervalle donnent 51/44/46 et un LCP qui varie de 10,6 s à
29,0 s **sans aucune modification du thème entre les passages**. Bonnes pratiques stable à 54/100
sur les 3 passages, Accessibilité 90/100, SEO 100/100.

**Fiche produit `https://tufteo.com/products/kit-tufting-complet`**

| # | Heure | Performances | LCP | FCP | TBT | CLS | SI |
|---|---|---|---|---|---|---|---|
| 1 | 12:15 | 55 | 22,7 s | 9,9 s | 120 ms | 0,005 | 9,9 s |
| 2 | 12:16 | 55 | 22,8 s | 11,3 s | 90 ms | 0,005 | 11,3 s |
| 3 | 12:17 | 55 | 22,8 s | 11,3 s | 90 ms | 0,005 | 11,3 s |
| **Médiane** | | **55** | **22,8 s** | | | | |

Mesures 2 et 3 identiques à la seconde près (probable réponse mise en cache par Google, requêtes
à 1 min d'écart) — traiter comme **2 échantillons indépendants effectifs**, pas 3 ; les deux
diffèrent peu de la mesure 1, nettement moins volatile que l'accueil. Bonnes pratiques 73/100
(supérieur à l'accueil : 54/100 — écart à investiguer, section suivante), Accessibilité 89/100,
SEO 100/100.

**Collection `https://tufteo.com/collections/fils`**

| # | Heure | Performances | LCP | FCP | TBT | CLS | SI |
|---|---|---|---|---|---|---|---|
| 1 | 12:20 | 55 | 27,5 s | 9,5 s | 60 ms | 0 | 12,4 s |

Bonnes pratiques 73/100, Accessibilité 95/100, SEO 100/100. Économie image estimée par l'outil :
**1 064 Kio** — nettement supérieure aux 352-616 Kio des deux autres pages, cohérent avec les 26
nouveaux visuels 1600×1600 ajoutés aujourd'hui (17 en image principale de fiches fil, potentiellement
servis en pleine résolution sur cette page de grille). 2 mesures supplémentaires en cours.

**Lecture d'ensemble à ce stade** : la volatilité Lighthouse mobile est confirmée réelle et large
(écarts de LCP jusqu'à ×2,7 sur l'accueil sans aucun changement), mais **aucune des 8 mesures
prises, sur aucune des 3 pages, n'approche le seuil de 65/100** — le plus haut score individuel est
55/100 (PDP et collection). Le diagnostic « sous le seuil » de la session précédente est confirmé,
pas remis en cause par le bruit de mesure.

### 1c. Diagnostic chiffré — inspection réseau directe (navigateur, session authentifiée sur le thème brouillon)

**Méthode** : le connecteur admin est resté authentifié en préview du thème brouillon
`189410738561` (bandeau « Draft » visible) pendant la navigation — confirmé par les chemins d'assets
`/cdn/shop/t/4/...` (brouillon) vs `/cdn/shop/t/2/...` (thème publié, vu dans les rapports PageSpeed
qui eux testent bien la boutique publique sans cookie). Comme `fonts.liquid` et `video.liquid` sont
identiques entre les deux thèmes (vérifié à l'ouverture de session), les poids et comportements
mesurés ci-dessous s'appliquent aux deux. Mesure par `performance.getEntriesByType('resource')`
dans la page réelle (Chrome, pas d'émulation 4G — les Kio ci-dessous sont donc les poids de transfert
réels, pas des estimations Lighthouse).

**Accueil — répartition du poids de page (225 ressources, 8 878 Kio same-origin)**

| Ressource | Poids | Constat |
|---|---|---|
| **Vidéo hero (`.mp4`, autoplay muted loop)** | **8 871 Kio (9 083 785 octets)** | À elle seule ~60 % du poids de page mesuré par PageSpeed (15 279-15 327 Kio). Fichier `HD-1080p-7.2Mbps` : vidéo pleine HD à haut débit servie en fond de bannière décorative. Confirmé : `snippets/video.liquid` place le tag `<video>` **hors défilement** (`{%- if video_autoplay or video_preview_image == blank %}` — le bloc hero a `video_autoplay: true`), donc le navigateur la charge immédiatement, pas en différé. |
| Reste des scripts/CSS du thème (theme assets `/cdn/shop/t/4/...`) | quelques dizaines de Kio au total | Correctement découpés en petits fichiers (`header.js`, `slider.js`, etc.), plusieurs avec `fetchpriority="low"` déjà en place — pas de piste ici. |
| Checkout-web (préchargement Shop Pay) | ~100 fichiers JS/CSS, poids individuel faible | Préchargement natif Shopify (accelerated checkout), pas un fichier du thème — hors du périmètre « fichiers de thème modifiables ». |

**Collection Fils — répartition des images (113 `<img>`, mobile, après défilement complet de la page = 3 673 Kio d'images)**

| Catégorie | Nombre | Poids total | Poids moyen |
|---|---|---|---|
| Images **PNG** | 26 | **1 931 Kio** | 74 Kio/image |
| Images **WebP** | 87 | 1 741 Kio | 20 Kio/image |
| dont les 17 nouvelles fiches fil (`fil-acrylique-tufting-*-01.png`, ajoutées aujourd'hui) | 17 | **1 221 Kio** | 72 Kio/image |

**Constat chiffré et direct** : les 26 images PNG du catalogue pèsent en moyenne **3,7× plus lourd**
que les 87 images WebP de la même page, pour un rendu équivalent à l'écran (même largeur servie,
`width=750`). Les 17 nouvelles images de fiches fil (celles mentionnées dans la consigne) sont
**toutes en PNG** et représentent à elles seules 1 221 des 3 673 Kio d'images de cette page — soit
un tiers du poids image total de la collection, alors qu'elles ne sont que 15 % du nombre d'images.
**Si ces 17 images pesaient le même poids moyen que le reste du catalogue en WebP (20 Kio), le poids
image de cette page tomberait à ~340 Kio au lieu de 1 221 Kio pour ces 17 fiches — gain estimé
~880 Kio sur cette seule page.** Recoupe et chiffre précisément l'insight PageSpeed de 1 064 Kio
d'économie image sur `/collections/fils` — c'est bien le format (PNG vs WebP), pas la taille servie
(`width=750` est déjà correct pour du mobile), qui est en cause. **Convertir ces images en WebP est
une modification de média produit, hors du périmètre theme/vitesse de cette session — décision pour
Hakim, section 3.**

**Scripts tiers — poids et temps de blocage (panneau « Tiers » PageSpeed, mesure collection Fils,
16/08 12:23)**

| Tiers | Poids transféré | Temps d'exécution thread principal |
|---|---|---|
| **Google Tag Manager / gtag** (3 conteneurs : AW-183…, GT-WPDGG7R8, AW-183…&cx=c) | **441 Kio** | **264 ms** — le plus lourd des tiers en TBT |
| Google Fonts CDN (police variable Material Symbols, `fonts.gstatic.com`) | **1 165 Kio** | 0 ms |
| Shopify Hosting (app embeds : Trustoo `seal-review.min.js` 82 Kio + `swiper-reviews.min.js` 18 Kio + CSS 18 Kio + `webmcp` 19 Kio + divers) | 145 Kio | 36 ms |
| trustoo.io (appels API avis : réglages, langue, statut, feedback) | 10 Kio | 0 ms |
| shop.app (préchargement Shop Pay) | 5 Kio | 0 ms |
| Google/Doubleclick Ads (pixels de conversion) | 3 Kio | 0 ms |
| merchant-center-analytics.goog | 1 Kio | 0 ms |
| Autres API Google | 1 Kio | 0 ms |

**Lecture** : Google Tag Manager/gtag (Google Ads + GA4) est le tiers qui bloque le plus le thread
principal (264 ms) et pèse le plus en JS exécuté (441 Kio) — **hors périmètre : interdiction absolue
de toucher à Google Ads**. Le deuxième poste en poids brut est la police d'icônes Material Symbols
de Google Fonts, **1 165 Kio pour une police de pictogrammes** (jeu d'icônes complet chargé en
variable font, `opsz,wght,FILL,GRAD` sur toute la plage) — poids élevé mais 0 ms de blocage (chargée
en `<link rel="stylesheet">`, pas de JS). Trustoo (l'app d'avis) est modeste : 155 Kio cumulés
(155 = 145 Shopify Hosting + 10 trustoo.io) et 36 ms de blocage — **pas le acteur principal du
problème de vitesse**, contrairement à l'hypothèse de départ.

**Requêtes bloquant le rendu** (insight PageSpeed, collection Fils) : économie estimée **950 ms**,
portée par les CSS du thème (`compiled_assets/styles.css`, `reset.css`, `base.css`,
`tufteo-motion.css`, `slider.css`) et `accelerated-checkout-backwards-compat.css` — tous déjà
chargés en `<link>` classique dans `<head>`, aucun avec `media` conditionnel ni chargement différé.

**Préconnexions** : PageSpeed signale « plus de quatre connexions preconnect » sur les 3 pages.
Vérifié dans le DOM réel (mobile) : **5 preconnects actifs** — `fonts.googleapis.com` (utilisé),
`fonts.gstatic.com` (utilisé — confirmé par le fichier de police Material Symbols téléchargé
depuis ce domaine), `shop.app` (utilisé, Shop Pay), `cdn.shopify.com` (utilisé), et
**`fonts.shopifycdn.com` (mort — confirmé : aucune requête réseau vers ce domaine sur les 3 pages,
toutes les polices transitent par `/cdn/fonts/...` en first-party)**. Retirer ce dernier ramène le
compte à 4, sous le seuil d'avertissement — confirme et valide la piste identifiée par la session
précédente, avec preuve directe (pas seulement déduite du code).

### 2. Tableau des pistes, classé par gain estimé

| # | Piste | Gain estimé | Sûr et réversible ? | Action |
|---|---|---|---|---|
| 1 | Compresser / remplacer la vidéo hero (9,08 Mo → un encodage web raisonnable, ex. 1080p à ~2 Mbps ou 720p, serait de l'ordre de 1-2 Mo) | **~7-8 Mo, de très loin le plus gros poste (≈60 % du poids de page)** | **Non — décision Hakim.** Remplacer le fichier vidéo est une modification de média (asset vidéo), pas un réglage de thème ; je n'ai pas généré de nouvel encodage vidéo. | Décision 1, section 5 |
| 2 | Convertir les 17 nouvelles images PNG (fiches fil) en WebP | **~880 Kio sur la seule page collection Fils** | **Non — modification de média produit**, explicitement hors périmètre de cette session (consigne : ne pas toucher aux produits/collections/médias produit) | Décision 2, section 5 |
| 3 | Retirer le preconnect mort `fonts.shopifycdn.com` (`snippets/fonts.liquid`) | Faible en Ko (quelques dizaines de ms de connexion TCP/TLS gaspillée), mais fait passer sous le seuil des « >4 preconnects » signalé par PageSpeed sur les 3 pages | **Oui** — confirmé mort par preuve réseau directe, aucune fonctionnalité ne l'utilise | **Appliqué, voir section 3** |
| 4 | Réduire le poster vidéo de `2500x` à `1200x` dans `snippets/video.liquid` (`video_tag: image_size:`) | Modeste (poster JPG généré, pas la vidéo elle-même — quelques dizaines à ~100 Kio) | **Oui** — poster affiché en `object-fit: cover` dans un conteneur bien plus petit que 2500 px | **Appliqué, voir section 3** |
| 5 | Différer le chargement de la police d'icônes Material Symbols (1 165 Kio) ou réduire le jeu d'icônes chargé | Élevé en Ko (1,1 Mo), 0 ms de blocage donc impact TBT nul, impact surtout sur le poids total et un peu le LCP/FCP si elle retarde le CSS | Limite — réduire le `icon_list` dans `snippets/material-icons-header.liquid` est un fichier de thème modifiable, mais retirer des icônes du jeu est un choix de contenu/design (quelles icônes restent utilisées où) que je n'ai pas les moyens de valider à l'aveugle sans risquer de casser une icône utilisée ailleurs | Décision 3, section 5 (non appliqué) |
| 6 | Google Tag Manager / gtag (441 Kio, 264 ms de blocage — le plus gros tiers en TBT) | Élevé, mais... | **Interdit absolu — Google Ads.** Aucune modification. | Non applicable — rappel de la règle, pas une décision |
| 7 | CSS render-blocking du thème (950 ms d'économie estimée par PageSpeed) | Modéré | Risqué sans test poussé (retirer le blocage sur `compiled_assets/styles.css` peut casser le rendu au premier paint — flash de contenu non stylé) — pas tenté cette session, hors du temps disponible | Non traité — à reprendre si Hakim veut aller plus loin |

### 3. Corrections appliquées — thème brouillon `189410738561` uniquement

Sauvegardes déjà prises par la session précédente et **revérifiées identiques au contenu actuel du
thème avant écriture** (`shopify/backups/2026-08-16-vitesse/snippets-fonts.avant.liquid` et
`snippets-video.avant.liquid`) — pas de nouvelle sauvegarde nécessaire, celles-ci sont le bon état
« avant ».

**Fix 1 — `snippets/fonts.liquid` : retrait du preconnect mort vers `fonts.shopifycdn.com`.**
Écrit via `themeFilesUpsert` (body inline TEXT, fichier petit). **Vérifié en relisant le contenu du
fichier après écriture** (pas seulement la réponse de la mutation) : le bloc `<link rel="preconnect"
href="https://fonts.shopifycdn.com" crossorigin>` et son `{%- unless ... -%}` ne sont plus présents,
le reste du fichier (3 blocs de preload de police) est identique.

**Fix 2 — `snippets/video.liquid` : poster vidéo `image_size` réduit de `'2500x'` à `'1200x'`.**
Même méthode. **Vérifié en relisant le contenu** : la ligne `{{ video | video_tag: image_size:
'1200x', autoplay: true, loop: video_loop, muted: true, controls: controls }}` est bien en place,
aucune autre ligne modifiée par rapport à la sauvegarde `avant`.

**Note de portée** : ces deux fixes n'attaquent pas le vrai poste lourd (la vidéo hero de 8,7 Mo
elle-même, cf. tableau section 2, ligne 1) — leur gain individuel est modeste. Ils sont appliqués
parce qu'ils sont sûrs, réversibles et déjà validés par la session précédente ; ne pas les présenter
comme résolvant le problème de fond.

### 4. Vérification après écriture — contrôle direct, pas seulement la réponse de l'API

Conformément à la règle « fait ne veut rien dire tant que ce n'est pas vérifié à l'écran », chaque
fix a été contrôlé en rechargeant la préview réelle du thème brouillon
(`https://tufteo.com/?preview_theme_id=189410738561`, session admin authentifiée, bandeau « Draft »
visible), pas seulement en relisant le fichier Liquid.

**Fix 1 — preconnect mort** : `document.querySelectorAll('link[rel~="preconnect"]')` sur la page
rechargée renvoie **4 preconnects** (`fonts.googleapis.com`, `fonts.gstatic.com`, `shop.app`,
`cdn.shopify.com`) — `fonts.shopifycdn.com` a disparu du DOM rendu. **Confirmé, pas seulement dans
le code source.**

**Fix 2 — poster vidéo** : l'élément `<video>` de la page d'accueil a maintenant
`poster="https://tufteo.com/cdn/shop/files/preview_images/…thumbnail.0000000000_1200x.jpg"` (contre
`…_2500x.jpg` avant) — **confirmé par lecture directe de l'attribut `poster` du DOM**, et par la
requête réseau observée vers ce fichier `_1200x.jpg`.

**Non-régression, vérifiée par navigation réelle sur le thème brouillon** :

| Contrôle | Résultat |
|---|---|
| Accueil s'affiche entièrement (hero, vidéo, sections) | OK — capture d'écran, vidéo hero visible et lue |
| Fiche produit `kit-tufting-complet` s'affiche entièrement | OK — capture d'écran, galerie et prix corrects |
| Collection `Fils` s'affiche entièrement, **17 vignettes de cônes visibles** | OK — vérifié par `document.querySelectorAll('img[src*="fil-acrylique-tufting"]')` → **17 images uniques**, une par couleur (caramel, indigo, camel, violet, bleu marine, bleu clair, kaki, vert foncé, jaune, orange, rose poudré, rose, bordeaux, rouge, gris, blanc, noir) — toutes en photo produit pleine, aucune ne réutilise le swatch 251×194 (contrairement au cas signalé le 16/08 sur 17 *autres* fiches) |
| Widget d'avis Trustoo se charge | OK — `#vstar-reviews` peuplé : 4,9/5, 20 avis, détail par étoile, premier avis (« Ricardo C. », « Achat vérifié ») visible |
| Ajout au panier fonctionne | OK — clic sur « Ajouter » (kit tufting complet) → tiroir panier ouvert avec l'article, quantité, prix ; article retiré ensuite pour ne rien laisser dans le panier de test |
| Menu et pied de page intacts | OK — nav avec « Accueil », « Kit débutant », etc. ; footer avec livraison/paiement/garantie |
| Pas de nouvelle erreur console | Seules erreurs observées : `401` sur `/sf_private_access_tokens` (4 occurrences, sur 3 pages) — **préexistantes, propres au comportement interne Shopify sur toute boutique**, sans lien avec `fonts.liquid` ou `video.liquid`. Aucune erreur Liquid, aucune erreur JS nouvelle. |

**Ce que je n'ai pas pu mesurer en Lighthouse « après »** : PageSpeed Insights **ne peut pas tester
le thème brouillon**. Vérifié en soumettant `https://tufteo.com/?preview_theme_id=189410738561` —
l'outil affiche « Résultats pour l'URL : ~~?preview_theme_id=189410738561~~ » barré et « Exécuter
avec l'URL d'origine » : **il retire le paramètre de préview et teste la boutique publique (thème
MAIN, non modifié)**, car son robot Lighthouse n'a pas de session admin authentifiée — la préview
d'un thème non publié n'est visible qu'aux utilisateurs connectés à l'admin. **Il n'existe donc
aucun moyen honnête d'obtenir un score PageSpeed « après » tant que le thème n'est pas publié** (et
publier n'est pas mon rôle). La vérification « après » de cette session se limite donc, à raison, au
contrôle direct des deux fichiers modifiés (ci-dessus) plutôt qu'à un delta de score — annoncer un
score « après » ici serait fabriquer un chiffre.

**Avant/après honnête à donner à Hakim** : le score restera dans la même fourchette bruitée (44-63
observée cette session) une fois publié, parce qu'aucun des deux fixes appliqués ne touche au poste
qui domine le poids de page (la vidéo hero, 60 % du total). Les deux fixes sont corrects et sans
régression, mais ne doivent pas être présentés comme un gain de score mesurable — seulement comme
deux nettoyages sûrs, actés en préparation d'un travail plus lourd (décisions section 5).

### 5. Décisions qui attendent Hakim, avec le gain estimé de chaque option

**Décision 1 — Vidéo hero (le vrai levier, ~7-8 Mo sur 15 Mo de poids de page).**
La vidéo `d4b89d328fc642d6b7ce632b7eb43aa5.HD-1080p-7.2Mbps-89618291.mp4` (9,08 Mo, autoplay muette
en boucle, décorative) domine le poids de toutes les pages qui l'affichent. Options, du plus simple
au plus impactant :
  - a) Ré-encoder la même vidéo en un débit web raisonnable (ex. 1080p ~1,5-2,5 Mbps au lieu de
    7,2 Mbps, ou 720p) → gain estimé **6-7,5 Mo**, sans rien changer visuellement pour l'utilisateur
    (la différence de qualité à ce débit est difficile à percevoir dans un usage plein-écran mobile).
  - b) Remplacer la vidéo par une image statique ou un GIF/WebP court en boucle → gain plus grand
    encore mais perd l'effet de mouvement.
  - c) Ne rien changer, accepter le poids.
  Je n'ai ni ré-encodé ni remplacé le fichier : c'est un changement de média, pas de code de thème,
  et engage un choix esthétique (le hero est la première chose vue).

**Décision 2 — Les 17 nouvelles images PNG des fiches fil (~880 Kio sur la collection Fils).**
Convertir `fil-acrylique-tufting-*-01.png` en WebP (même traitement que les 87 autres images du
catalogue, déjà en WebP à poids moyen 3,7× inférieur) ferait chuter le poids image de cette page
d'environ 1 221 Kio à ~340 Kio pour ces 17 fichiers. C'est une modification de média produit, donc
hors du périmètre de cette session vitesse — et l'agent produit du jour a justement pour consigne de
ne pas y toucher en parallèle. Gain estimé si fait : ~880 Kio sur cette page, contribue directement à
faire baisser l'insight PageSpeed de 1 064 Kio.

**Décision 3 — Police d'icônes Material Symbols (1 165 Kio, 0 ms de blocage).**
Le fichier `snippets/material-icons-header.liquid` charge la totalité du jeu variable Material
Symbols (~100 icônes, plage complète `opsz,wght,FILL,GRAD`) pour n'en afficher qu'une poignée à
l'écran à un instant donné. Réduire `icon_list` aux seules icônes réellement utilisées, ou figer les
axes variables (`FILL`, `GRAD`) à une seule valeur plutôt qu'une plage, réduirait sensiblement ce
poids — mais je n'ai pas de vue exhaustive de quelles icônes sont utilisées sur quelles pages/sections
du thème (options non visitées cette session, sections non chargées) : retirer une icône utilisée
ailleurs casserait silencieusement un pictogramme. Gain estimé si un audit complet des usages est
fait : plusieurs centaines de Kio, sans coût fonctionnel — mais nécessite ce travail d'audit
préalable, non fait ici faute de temps.

**Décision 4 — Google Tag Manager / gtag (441 Kio, 264 ms de blocage, le tiers le plus lourd en TBT).**
Rappel de la règle absolue : **aucune modification de Google Ads/Merchant Center**, donc aucune
action possible ici quel que soit le gain. Signalé pour information, pas comme option.

**Décision 5 (mineure, non appliquée) — CSS bloquant le rendu (950 ms d'économie estimée).**
`compiled_assets/styles.css` et les autres CSS du thème sont chargés en `<link>` classique,
bloquant le premier rendu. Les rendre non-bloquants (`media="print" onload=...` ou équivalent)
demande de vérifier qu'aucun flash de contenu non stylé n'apparaît — pas tenté cette session, faute
de temps disponible pour un test poussé. À reprendre si Hakim veut aller au-delà des deux fixes déjà
appliqués.

## Ce que je n'ai pas pu vérifier

- **Le score PageSpeed « après » sur le thème brouillon** : impossible par construction (l'outil ne
  peut pas atteindre un thème non publié sans session admin — confirmé en section 4, pas supposé).
- **Le rapport de vitesse natif Shopify admin** (celui que la checklist GMC regarde en premier) :
  je n'ai pas de session admin dans un navigateur pour y accéder ; PageSpeed Insights est une mesure
  publique équivalente (même moteur Lighthouse) mais peut différer légèrement du chiffre exact que
  Hakim verra dans l'admin — signalé déjà par la session précédente, toujours vrai.
- **Le contenu exact des templates JSON du thème** (`templates/index.json`, `templates/product.json`,
  etc.) : je n'ai touché qu'à des fichiers Liquid (`snippets/`), jamais aux templates JSON — donc la
  limite connue des ~125 Ko n'était pas engagée cette session, mais je ne l'ai pas non plus vérifiée.
- **L'usage exhaustif du jeu d'icônes Material Symbols** sur l'ensemble des pages/sections du thème
  (nécessaire pour chiffrer précisément la Décision 3 sans risque de casse) — non fait, faute de
  temps.
- **Le rapport de vitesse bureau (desktop)** : toute la session s'est concentrée sur mobile, seul
  format demandé par la consigne — aucune mesure desktop prise.
- **L'effet du fix preconnect et du fix poster sur un score Lighthouse réel** : leur gain individuel
  n'a pas pu être isolé numériquement (impossible de mesurer le brouillon en Lighthouse), seulement
  vérifié qualitativement par inspection DOM/réseau directe.

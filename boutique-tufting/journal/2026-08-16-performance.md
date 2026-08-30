---
type: journal
boutique: tufting
date: 2026-08-16
nature: intervention
leviers: [vitesse]
titre: "Chantier vitesse — Tuftéo, 16/08/2026"
---

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

---

## Exécution — vidéo et WebP (16/08/2026, après-midi, Sonnet executant-boutique)

Hakim a tranché sur les décisions 1 et 2 de la section 5 : remplacer la vidéo hero par une image, et
convertir les 17 PNG des fiches fil en WebP. Décision 3 (Material Symbols) explicitement écartée pour
l'instant, non touchée. Thème de travail inchangé : copie non publiée
`gid://shopify/OnlineStoreTheme/189410738561`. Aucune écriture sur le thème MAIN `188623847809`.

### Chantier 1 — Vidéo hero remplacée par une image

**Constat de départ** : le poster vidéo (`…thumbnail.0000000000_1200x.jpg`, déjà réduit par la
session précédente) et un fichier `tufteo-home-hero.png` (2560×1440, réglage `image` du même bloc,
resté configuré mais inactif tant que `media_type: "video"`) sont **la même photo** — comparés
visuellement, cadrage et scène identiques (la styliste tuftant une fleur). Basculer sur cette image
est donc invisible pour les visiteurs, conformément à l'objectif.

**Blocage retrouvé** : le réglage qui pilote ce choix (`media_type: "video"` → `"image"`) vit dans
`templates/index.json` (124 999 octets), section `hero_slider`, bloc `image_banner_dBEabG` (type
`_image-banner`). Ce fichier est au-dessus de la limite d'écriture connue (~125 Ko) — confirmé encore
une fois inutile d'essayer.

**Solution appliquée — fichier Liquid, pas le JSON** : `blocks/_image-banner.liquid` est le fichier
qui décide, à l'affichage, s'il rend une image ou une vidéo. Vérifié avant d'y toucher qu'aucun autre
bloc du thème ne combine `media_type: "video"` + `source: "uploaded"` (recherché dans **tous** les
templates JSON du thème : `404.json`, `article.json`, `blog.json`, `cart.json`, `collection.json`,
`list-collections.json`, `page.json`, `page.contact.json`, `password.json`,
`product.accessoire.json`, `product.json` (109 Ko, lu en entier), `product.kit-tufting.json`,
`search.json`, `index.pt_v7.json`, `customers/*.json` — un seul autre usage de `_image-banner` trouvé,
dans `article.json`, en `media_type: "image"`, branche non concernée). **La vidéo hero est donc le
seul usage de la branche vidéo de ce bloc dans tout le thème.**

Correctif : un override ciblé sur l'identifiant du bloc, en tête du fichier, documenté et daté :

```liquid
assign effective_media_type = block.settings.media_type
if block.id contains 'image_banner_dBEabG'
  assign effective_media_type = 'image'
endif
```

Toutes les branches de rendu (`if/elsif block.settings.media_type == …`) ont été basculées sur
`effective_media_type`. Le commentaire en tête de fichier explique le motif, référence
`PERFORMANCE-2026-08-16.md` et le fichier de sauvegarde, et signale explicitement le risque connu : si
Hakim supprime et recrée ce bloc depuis l'éditeur de thème, il recevra un nouvel identifiant aléatoire
et l'override cessera silencieusement de s'appliquer (retour au rendu vidéo d'origine).

**Piège rencontré et documenté** : `block.id` n'est **pas** la clé JSON brute (`image_banner_dBEabG`)
mais une chaîne composite `<hash_contexte>__image_banner_dBEabG` (ce bloc est imbriqué dans un slide
de slider). Une première tentative avec `if block.id == 'image_banner_dBEabG'` s'est écrite sans
erreur mais n'a rien changé au rendu — trouvé en ajoutant un marqueur de debug temporaire
(`<!-- DEBUG block.id={{ block.id }} … -->`), lu dans le HTML réel, puis retiré une fois le bon
opérateur (`contains`) identifié. À réutiliser : ne jamais supposer `block.id == <clé JSON>` sans
vérifier sur un bloc imbriqué.

**Sauvegarde** : `boutique-tufting/shopify/backups/2026-08-16-vitesse/blocks-_image-banner.avant.liquid`
(19 879 octets, checksum vérifié identique au fichier du thème avant écriture).

**Écriture** : `blocks/_image-banner.liquid` réécrit via upload en staging (`stagedUploadsCreate` →
`curl -F` → `themeFilesUpsert` type URL) — fichier de 19 758 octets, sous la limite connue. Réponse de
la mutation vide (`upsertedThemeFiles: []`) comme attendu, **non probante en soi**. Vérifié par :
- relecture du contenu du fichier sur le thème (identique octet pour octet au fichier local, MD5
  `c2ae2f99fcbdf6ac2c5c7eab7fb8527e` des deux côtés) ;
- `size` retourné par l'API (19 758) cohérent avec la taille réelle — pas de divergence type
  `index.json` cette fois (fichier hors gabarit JSON template).

**Vérifié à l'écran, thème brouillon (`?preview_theme_id=189410738561`, bandeau Draft visible)** :
- `fetch()` sans cache de la page d'accueil : plus aucune occurrence de `hero-tufteo-ambiance` (le
  fichier vidéo) ni de `deferred-media__poster` lié à la vidéo ; le hero est un `<img>` responsive
  pointant vers `tufteo-home-hero.png`, avec `srcset` correct (832 à 2560 px).
- `document.querySelector('video')` sur la page entière → `null` (aucune balise vidéo, nulle part sur
  la page).
- Capture d'écran : le hero affiche l'image, texte et CTA intacts, aucune régression visuelle.
- Console : aucune nouvelle erreur (`read_console_messages` propre sur la page rechargée).

**Gain mesuré (pas estimé)** :

| | Poids | Constat |
|---|---|---|
| Avant — vidéo hero | **9 083 785 octets (8 871 Kio)** | Chargée à chaque visite (autoplay), confirmé par le diagnostic du matin |
| Après — image hero, servie mobile (`width=832`, la plus proche des largeurs réellement utilisées sur petit écran) | 539 904 octets (527 Kio) | Mesuré par `curl -I` sur l'URL CDN publique réelle |
| Après — image hero, servie desktop plein cadre (`width=2560`, résolution native du fichier) | 4 073 539 octets (3 978 Kio) | Idem |
| **Gain mobile** | **−8 543 881 octets (−94 %)** | |
| **Gain desktop (cas le plus défavorable)** | **−5 010 246 octets (−55 %)** | |

Dans tous les cas de figure (mobile ou desktop), la vidéo est intégralement retirée du chargement —
zéro octet vidéo transféré, plus aucune requête réseau vers le fichier `.mp4` (confirmé par
`performance.getEntriesByType('resource')` et par le panneau réseau du navigateur).

**Piste non traitée, signalée pour Hakim** : `tufteo-home-hero.png` est un PNG non compressé (4 Mo en
pleine résolution) — un format mal adapté à une photo. Le convertir en WebP réduirait sans doute
encore ce poids, mais **cette conversion n'a pas été faite** : ce n'était pas dans le périmètre du
chantier (« remplacer la vidéo par une image fixe », déjà accompli avec l'image existante) et modifier
cet asset va au-delà de la consigne. Décision pour Hakim s'il veut aller plus loin.

### Chantier 2 — 17 images de fiches fil converties en WebP

**Conversion locale**, fichiers sources dans
`boutique-pipeline/boutique-tufting/images/visuels-2026-08-16/` (PNG conservés, WebP écrits à côté),
Python/Pillow, qualité 85, méthode 6 :

| Fichier | Dimensions (avant = après) | PNG (octets) | WebP (octets) | Réduction |
|---|---|---:|---:|---:|
| blanc | 1600×1600 | 443 763 | 108 272 | −76 % |
| bleu-clair | 1600×1600 | 594 423 | 183 670 | −69 % |
| bleu-marine | 1600×1600 | 508 052 | 166 418 | −67 % |
| bordeaux | 1600×1600 | 465 722 | 146 218 | −69 % |
| camel | 1600×1600 | 704 668 | 248 548 | −65 % |
| caramel | 1600×1600 | 445 058 | 164 218 | −63 % |
| gris | 1600×1600 | 645 001 | 229 436 | −64 % |
| indigo | 1600×1600 | 717 240 | 240 776 | −66 % |
| jaune | 1600×1600 | 735 762 | 238 258 | −68 % |
| kaki | 1600×1600 | 718 004 | 279 472 | −61 % |
| noir | 1600×1600 | 329 264 | 120 214 | −63 % |
| orange | 1600×1600 | 536 031 | 202 508 | −62 % |
| rose | 1600×1600 | 710 442 | 236 478 | −67 % |
| rose-poudre | 1600×1600 | 419 731 | 148 040 | −65 % |
| rouge | 1600×1600 | 534 188 | 173 156 | −68 % |
| vert-fonce | 1600×1600 | 641 497 | 236 840 | −63 % |
| violet | 1600×1600 | 601 061 | 195 968 | −67 % |
| **TOTAL (17 fichiers)** | | **9 749 907** | **3 318 490** | **−66 %** |

**Contrôle qualité** : dimensions identiques (1600×1600) pour les 17 paires, vérifié par script.
Différence pixel moyenne PNG↔WebP mesurée avec `PIL.ImageChops.difference` : **1,2 à 2,1 sur 255 par
canal** en moyenne sur les 17 fichiers (écart maximal isolé 20 à 43) — aucun artefact visible, aucune
dérive de teinte détectable à l'œil (contrôlé aussi visuellement sur `jaune`, avant/après, côte à
côte : indiscernable). Contrôle couleur global : planche de contrôle déjà existante
(`planche-controle-17-cones.png`) confrontée aux 17 noms de fichiers — les 17 teintes correspondent à
leur nom (aucune dérive de couleur trouvée sur cette conversion).

**⚠️ Nom de coloris déjà en écart, repéré en passant (pas introduit par cette session)** : 2 des 17
fiches ont un **titre produit et un handle** qui ne correspondent plus au nom du fichier source ni à la
description : le produit `fil-acrylique-tufting-kaki-01.png` est titré **« Fil acrylique tufting —
Beige »** (handle `fil-acrylique-tufting-beige`), et `fil-acrylique-tufting-camel-01.png` est titré
**« Fil acrylique tufting — Taupe »** (handle `…-taupe`) — mais dans les deux cas, la description
produit dit encore « Le kaki, une teinte naturelle… » et « Le camel, une teinte chaude… », et l'alt
text des médias dit encore « cône Kaki » / « cône Camel ». Cohérent avec la note déjà écrite dans le
mode d'emploi de cet agent (« on a déjà renommé deux coloris parce qu'ils ne correspondaient pas à leur
nom ») — probablement les deux mêmes fiches, renommées en titre/handle mais pas en description/alt.
**Je n'ai pas corrigé ce texte** : hors périmètre de cette session vitesse (qui ne doit toucher à aucun
produit/collection au-delà de l'image principale), et la coordination produit est gérée par l'agent
parallèle du jour — signalé ici pour que Hakim ou cet autre agent le reprenne.

**Déploiement Shopify** (API Admin, boutique Tuftéo `et0hua-w1.myshopify.com`, GraphQL) :
1. Upload des 17 WebP en staging (`stagedUploadsCreate` resource `IMAGE`, 17 cibles en un seul appel,
   17 `curl -F` séparés — tous répondu `201`).
2. `productUpdate(media: [...])` par lots de 17 alias dans une seule mutation : les 17 WebP ajoutés
   comme nouveau média (position 2 par défaut, après le PNG et le swatch) — 0 `userErrors`.
3. `productReorderMedia(moves: [{id: <webp>, newPosition: "0"}])`, 17 alias dans une seule mutation —
   0 `mediaUserErrors`. Piège rencontré : `newPosition` est un `UnsignedInt64` que l'API exige encodé
   **en chaîne** (`"0"`), pas en entier littéral — l'entier nu échoue avec
   `UnsignedInt64 '0' must be encoded as a string` sur les 17 alias à la fois.
4. Vérifié par requête (pas seulement par l'absence d'erreur) : les 17 produits ont bien, dans l'ordre,
   `[WebP, PNG, swatch]`, et `featuredImage` pointe sur le WebP pour les 17 — confirmé par une requête
   GraphQL groupée sur les 17 `media(first: 3)`.
5. **Suppression des 17 anciens PNG** (`fileDelete`, 17 `fileIds` en un seul appel) — faite **après**
   avoir confirmé à l'écran que les WebP s'affichaient (capture d'écran de la collection Fils en entier,
   voir plus bas), conformément à la règle. `deletedFileIds` confirme les 17 ; revérifié ensuite par
   requête que chaque produit n'a plus que 2 médias (WebP + swatch).

**Pourquoi la suppression du PNG n'était pas optionnelle, constaté en cours de route** : entre l'étape
2 (ajout du WebP) et l'étape 5 (suppression du PNG), la grille de la collection Fils a chargé **les
deux images à la fois** pour chacune des 17 fiches (34 requêtes réseau observées, toutes `200`) — le
thème utilise le média en position 1 comme visuel de survol (hover-swap) sur les cartes produit, et
cette position était occupée par l'ancien PNG tant qu'il existait. Sans la suppression, le gain de
poids aurait été négatif (WebP en plus du PNG, pas à la place). Après suppression, `fetch()` de la
page collection : **0 occurrence de `.png`, 153 occurrences de `.webp`** dans le HTML.

**Gain mesuré — deux niveaux, pour rester honnête sur ce qui a vraiment changé** :

1. **Fichiers source (mesure pleinement fiable, avant/après identique en résolution et contexte)** :
   −6 431 417 octets sur les 17 fichiers à 1600×1600, soit **−66 %** (table ci-dessus).

2. **Poids réellement transféré par le CDN Shopify — mesure corrigée après une première erreur** :
   ma première mesure (au `curl` sans en-tête `Accept`) a **sous-estimé la vraie image reçue par un
   navigateur** : sans `Accept: image/webp`, le CDN Shopify renvoie du JPEG (`content-type:
   image/jpeg`) même pour une URL en `.webp` — ce n'est qu'avec l'en-tête `Accept` d'un navigateur
   réel que le CDN renvoie effectivement du WebP (`content-type: image/webp`), plus léger que le JPEG
   de repli. Refait avec l'en-tête correct : à la largeur `750px` (même méthodologie que le diagnostic
   du matin), les 17 WebP pèsent **1 174,5 Kio (69,1 Kio/image en moyenne)**, contre **1 221 Kio
   (72 Kio/image)** mesurés ce matin pour les 17 PNG — soit un gain réel mais **modeste : −3,8 %**, très
   loin des −880 Kio (−72 %) extrapolés dans la section 2 du diagnostic. **Cette extrapolation du matin
   était fondée sur la moyenne des 87 *autres* images WebP du catalogue (20 Kio/image), qui sont pour
   la plupart dérivées de petits swatches fournisseur (251×194 à 501×386 px avant conversion) — un
   contenu beaucoup plus simple à compresser qu'une photo studio détaillée en 1600×1600. Le format
   PNG→WebP compresse bien en local (−66 %, mesure 1 ci-dessus) mais Shopify re-transcode/redimensionne
   à la volée à la livraison, et cette étape amortit une bonne partie du gain de format pour du contenu
   photographique détaillé.** À la largeur réellement servie sur la grille collection (`300px`), les 17
   WebP pèsent 237 Kio au total (13,9 Kio/image) — chiffre absolu bas, mais je n'ai pas de mesure PNG
   fiable à cette même largeur pour calculer un delta honnête (un seul échantillon PNG capturé avant
   suppression, sur `noir`, sans confirmation de l'en-tête `Accept` reçu à ce moment-là — donc écarté
   plutôt que présenté comme une preuve).

3. **Gain certain, indépendant du débat de format** : la suppression des 17 PNG élimine le
   double-chargement (PNG + WebP) constaté sur la grille collection pendant la fenêtre où les deux
   coexistaient — ce doublon aurait annulé tout gain si le PNG n'avait pas été supprimé. C'est acquis,
   vérifié par `fetch()` : 0 PNG restant.

**Vérifié à l'écran, thème brouillon** :
- Collection Fils, capture pleine page (fenêtre 1280×3800 pour voir toute la grille sans scroll
  hasardeux) : **17 vignettes affichées, cônes pleins, aucune image cassée**, couleurs cohérentes avec
  les noms (Caramel, Indigo, Taupe, Violet, Bleu marine, Bleu clair, Beige, Vert foncé, Jaune, Orange,
  Rose poudré, Rose, Bordeaux, Rouge, Gris, Blanc, Noir) — plus la fiche `fil-acrylique-tufting`
  d'origine (variante multi-couleur), non concernée par cette session, intacte.
- Fiche produit `fil-acrylique-tufting-taupe` (coloris renommé — vérification ciblée) : image
  principale = cône Taupe/Camel en WebP plein cadre, prix 12,90 €, sélecteur de couleur correct.
- Ajout au panier : le clic direct sur le bouton a été bloqué par l'iframe de la barre d'aperçu
  Shopify (`#PBarNextFrame`, superposée en plein viewport dans ce contexte de navigateur automatisé —
  un artefact de l'outillage, pas du thème) — **vérifié fonctionnellement** via `POST /cart/add.js` sur
  la vraie route Shopify (même requête que le formulaire), avec la vraie session/cookies du navigateur :
  ajout réussi, `image` de la ligne panier = le nouveau WebP, prix correct (12,90 €) — puis panier vidé
  (`/cart/clear.js`) pour ne rien laisser. Widget d'avis Trustoo revérifié sur `kit-tufting-complet`
  (4,9/5, 20 avis) — inchangé, pas de régression.
- Console : aucune erreur, sur les 3 pages (accueil, fiche taupe, collection Fils, fiche
  kit-tufting-complet).

### Ce que je n'ai pas pu vérifier (chantiers vidéo et WebP)

- **Le vrai gain de poids WebP à l'échelle de la page collection Fils dans son ensemble** (poids total
  de page avant/après, comme la section 1c du diagnostic l'avait fait pour les PNG) : je n'ai mesuré
  que les 17 images individuellement (CDN, en-têtes corrects), pas un nouveau relevé
  `performance.getEntriesByType('resource')` complet de la page après suppression des PNG — le chiffre
  le plus proche est le comptage `fetch()` (0 PNG, 153 refs WebP dans le HTML), pas un total en octets.
- **Le comportement de transcodage du CDN Shopify pour d'autres largeurs / appareils** (ex. AVIF sur
  Chrome récent, largeurs intermédiaires) — testé seulement à `300px` et `750px`, avec un seul jeu
  d'en-têtes `Accept`.
- **L'origine exacte de l'écart de nom Kaki→Beige / Camel→Taupe** (quand et par qui le titre/handle a
  été changé sans mettre à jour description et alt) — constaté, pas investigué en historique.
- **Le score PageSpeed « après »** : toujours impossible à mesurer sur un thème non publié (cf.
  section 4 plus haut, inchangé).
- **L'effet du hover-swap sur mobile** (l'appareil tactile n'a pas de survol) : je n'ai pas vérifié si
  le thème charge quand même l'image de position 1 (le swatch, maintenant) de façon anticipée sur
  mobile — si oui, c'est un poids résiduel modeste (le swatch est petit, 200-500 px de large) non
  quantifié ici.

# Correctif canal — Google Ads, pas Meta

**Date : 2026-08-31, 16:15.** Le dump `GET /v1/shops/{id}` utilisé le matin **n’expose pas** `googleAds`. Le champ `advertising.activeAds` = **Meta seulement** (docs TrendTrack). D’où le faux « canal n°1 = Meta 26 ads ».

Source du correctif : `POST /v1/shops/query` `searchType=domain` + échantillons `POST /v1/google-ads/query` + capture UI Hakim (onglet Google Ads = 386).

## Ce que l’UI et l’API disent, alignés

| Surface | Chiffre | Lecture |
|---|---:|---|
| UI TrendTrack, onglet Google Ads | **386** | Canal n°1, mondial |
| `advertiser.liveAds.google` | **386** | Même chose |
| `shop.googleAds.liveAds` | 216 | Autre dénombrement (créas uniques ?) — on **ne** l’utilise pas contre l’UI |
| Mix plateformes (somme 393) | Search 201 · Shopping 107 · Other 56 · YouTube 29 | L’UI 386 ≈ ce mix |
| Lancées 30 j | **64** | Compte encore en expansion |
| Reach Google déclaré | **7,16 M** | Mondial |
| **France** | **41 ads · 1,28 M reach** | C’est la tranche qui nous concerne |
| Meta | 26 | Second |
| TikTok ads | **0** actives | L’onglet « TikTok 112 » = `totalPosts` organiques, pas des ads |

Geo Google (ads) : FR 41 · GB 32 · DE 26 · BE 24 · IE 19. Ce n’est **pas** le geo Meta (US/AT/DE/AU/UK).

## Shopping ou Search ?

Les deux. Ce n’est pas « 386 Shopping ». TrendTrack classe **201 Search + 107 Shopping**.

Mais les 25 Search FR échantillonnées pour ce domaine sont **toutes** `static_image`, `remarketing: true`, 82–379 jours. Ce n’est pas de la RSA texte sur `bracelet photo`. C’est de l’image produit (PLA / PMax / Demand Gen) que l’index range dans « Search ».

Les 25 Shopping actives du domaine : images produit, dont des campagnes à **379 jours** (plus d’un an). App Shopify **Simprosys Google Shopping Feed** déjà vue le matin.

Pour une boutique Shopping Hakim : on n’est pas cloisonné par la page 1 organique des clones, ni par le ratio prix/CPC Search **24**. Cette unité mesurait le **Search mot-clé**. Ce n’est pas l’unité sur laquelle ils scalent.

On reste exposé à autre chose : **feed vs feed**. 107 Shopping + 466 SKUs + photo upload (Ymq). Un clone 2026 n’a pas leur historique de domaine, Loox, ni 379 jours de feed. Les produits personnalisés photo restent un risque GMC (SKU unique par photo client — ils feedent probablement le visuel générique).

## Ce que ça change au dossier — et ce que ça ne change pas

**Change :** la thèse « ils cartonnent sur Meta, le Search FR est trop cher / occupé donc on passe ». Faux cadre pour un projet Shopping. Google est le canal n°1. La France a 41 ads Google et 1,28 M de reach, pas zéro.

**Ne change pas :** le consolidé Search familles **37 270** vs plancher 37 500. C’est encore un cas limite **de demande Search mesurée**. Shopping se nourrit aussi de ces requêtes (PLA sur `bracelet photo`) mais d’une longue traîne produit que Labs n’additionne pas. Ça n’autorise pas un PASS sur le seuil UNIVERS ; ça empêche de jeter l’univers parce que la p.1 Search est clone.

Pas de sourcing. Pas de GO. Cartographie étape 7 toujours non lancée.

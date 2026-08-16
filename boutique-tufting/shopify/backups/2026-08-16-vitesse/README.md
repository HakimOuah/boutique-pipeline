# Sauvegardes — chantier vitesse, 16/08/2026

Backups pris avant écriture, sur le thème brouillon `gid://shopify/OnlineStoreTheme/189410738561`
(« Tuftéo — purge faux avis 16-08 »). Aucune écriture sur le thème publié (MAIN,
`188623847809`) — interdit, non touché.

- `snippets-fonts.avant.liquid` — avant retrait du `<link rel="preconnect" href="https://fonts.shopifycdn.com">`
  mort (jamais utilisé : tous les fichiers de police transitent par `/cdn/fonts/...` en first-party,
  vérifié par inspection réseau le 16/08).
- `snippets-video.avant.liquid` — avant réduction de `image_size: '2500x'` à `'1200x'` dans l'appel
  au filtre Liquid `video_tag` (poster/fallback de toutes les vidéos du site, image générée en
  2500 px de large alors que la div `.deferred-media__poster` visible affiche déjà une image
  responsive correctement dimensionnée par-dessus).

Voir `PERFORMANCE-2026-08-16.md` (racine `boutique-tufting/`) pour le diagnostic complet et la
vérification après écriture.

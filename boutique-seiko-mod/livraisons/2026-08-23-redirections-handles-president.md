# Redirections 301 à créer — handles Président renommés (23/08/2026)

Le CLI n’a pas le scope `write_online_store_navigation`. À poser dans **Boutique en ligne → Redirections d’URL** :

| Ancienne URL | Nouvelle URL |
|---|---|
| `/products/bracelet-presidentiel-dore` | `/products/bracelet-maillons-arrondis-dore` |
| `/products/bracelet-presidentiel-acier-inoxydable` | `/products/bracelet-maillons-arrondis-acier` |
| `/products/voyageur-or-gmt-president` | `/products/voyageur-or-gmt-maillons-arrondis` |

Statut au 23/08 (soir) :
- Nouvelles URLs → **200**
- Anciennes URLs → **301** vers les nouvelles (créées via admin Shopify)
- API `urlRedirectCreate` : scope manquant sur le CLI — contourné via navigateur

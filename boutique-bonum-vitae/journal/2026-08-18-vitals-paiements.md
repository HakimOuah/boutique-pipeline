# 18/08/2026 midi — Vitals off, icônes = checkout

Hakim : tout faire via CLI ; il acceptera une demande de scopes si besoin.
Aucun GMC créé / soumis.

## Vitals

Embed `shopify://apps/vitals/blocks/app-embed/…` passé à `disabled: true` dans
`config/settings_data.json` du MAIN FullStack (`205568147794`).

Constaté ensuite sur `https://bonumvitae.fr/products/osmoseur-ro-600g` :
plus de `vtlsAebData`. Metafields `reviews` / `vstar` toujours vides.
0 `aggregateRating` / 4,83 dans le HTML.

L'app reste installée (scope `read_apps` absent — pas de désinstall CLI).
Si les notes reviennent, désinstaller Vitals dans l'admin.

## Paiements — checkout réel (panier test, pas de commande)

`availablePaymentLines` :

- Shopify Payments : Visa, Mastercard, Amex, Cartes Bancaires, Maestro
- Apple Pay
- PayPal Express
- Klarna (offsite)
- Shop Pay (assets + shell checkout)

Footer / PDP forcés (`force_icons_display`) : Visa, Mastercard, Amex, Apple Pay,
Google Pay, PayPal, Shop Pay, Klarna. Maestro laissé masqué. Pas d'icône CB
dans FullStack.

## Autre constaté

- Sticky ATC présent dans le HTML (`<sticky-add-to-cart>`).
- `delivery-estimation` : 6–10 j ouvrés, cutoff 15 h, sam/dim exclus.
- 301 mentions / osmoseurs toujours en place.
- Handles encore marque (ALTHY/IPSE/alloet/widesea/OSWNKW) : titres déjà propres ;
  pas renommés (upsell panier + home pointent encore `alloet` / `widesea`).

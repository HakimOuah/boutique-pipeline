# Audit P3 — Squelette Carré Black — source complète API — 10/08/2026

## Verdict

**BLOQUÉ — aucune source exacte complète ne prouve simultanément le boîtier, ses trois saillies à
droite, les quatre vis et le bracelet complet.**

Le fragment exact `14:200000080#Black` est retrouvé sans ambiguïté sur l'article AliExpress
`1005009825936780`. Son image SKU officielle montre correctement le boîtier Black, les quatre vis et
les trois commandes/saillies du côté droit, mais elle coupe le bracelet intégré après quelques
maillons. Elle ne permet donc pas de produire honnêtement une vue complète du produit.

Aucun ordre n'est créé. Aucune nouvelle image n'est qualifiée ou conservée comme source complète.

## Identité officielle

- Produit : `1005009825936780`.
- Titre API : `Tandorio – montre mécanique automatique pour hommes, 42mm, mouvement NH70, verre
  saphir carré, cadran squelette blanc, Vintage`.
- Vendeur : `Tandorio_watch Store`, magasin `5376237`.
- Statut : `onSelling`.
- Fragment exact : `14:200000080#Black`.
- SKU API exact : `12000050290189621`.
- `sku_attr` exact : `5:56964930#NH70 movement;14:200000080#Black`.
- Stock observé : 997.
- Prix offre observé : 114,69 EUR ; prix SKU retourné : 163,84 EUR.
- Image SKU exacte :
  `https://ae01.alicdn.com/kf/Sc63c29a32a0c4c329d308188738f58efP.jpg`.
- Preuve locale préexistante :
  `boutique-seiko-mod/preuves-p3-variantes-api-2026-08-10-agent/sources-propres/squelette-carre-01-14-200000080-black.jpg`.

Ces valeurs proviennent de l'appel officiel `variants` observé à `2026-08-10T00:42:15Z`. Elles
établissent l'identité du SKU, pas une décision commerciale.

## Contrôle visuel original

L'article ne contient que deux SKU visuels : White et Black, chacun lié au mouvement NH70. Les deux
images de propriété ont été téléchargées temporairement depuis les URL CDN renvoyées par l'API et
ouvertes à leur résolution originale de 1000 × 1000 px.

### Black — fragment demandé

L'image Black exacte prouve :

- le boîtier carré/arrondi en acier ;
- quatre vis fendues, une à chacun des quatre coins ;
- trois saillies distinctes sur le côté droit : une commande haute courte, la couronne centrale et
  une commande basse ;
- le cadran squelette noir et le mouvement visible ;
- le raccord du bracelet intégré au boîtier.

Elle ne prouve pas :

- les deux longueurs complètes du bracelet ;
- la continuité de tous les maillons ;
- le fermoir ou la boucle.

Le haut et le bas du bracelet sont coupés par le cadre après seulement quelques maillons. La photo est
donc exacte mais **incomplète pour la production demandée**.

### White — autre fragment

L'image White montre le même type de boîtier, les quatre vis et trois saillies, ainsi que davantage de
maillons en haut et en bas. Le bracelet reste cependant tronqué et le fermoir n'est pas visible. Elle
correspond en outre à `14:200005100#white`, pas au fragment Black : elle ne peut pas être promue comme
vérité produit ou recolorée pour Black.

## Galerie et image principale : données manquantes

Route utilisée : client local read-only
`codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, vers AliExpress Open Platform /
AE-Dropshipper sur le VPS à IP autorisée.

- `health` : OK à `2026-08-10T00:42:12Z` ;
- `variants 1005009825936780` : OK à `2026-08-10T00:42:15Z` ;
- le gateway expose les deux images de propriété SKU, mais pas le champ brut
  `ae_multimedia_info_dto.image_urls` contenant la galerie de `aliexpress.ds.product.get` ;
- quatre recherches officielles ciblées sur le titre et plusieurs tris (`orders`, `latest`,
  `price_desc`) n'ont pas fait remonter l'ID exact dans les 20 premiers résultats ; le tri `latest` a
  renvoyé `IOPUpstreamError` ;
- une recherche supplémentaire sur l'ID numérique exact n'a pas non plus retourné l'article ;
- l'appel officiel direct depuis le Mac n'est pas une voie de remplacement : l'application impose
  une whitelist IP et renvoie `AppWhiteIpLimit` hors du VPS autorisé.

La galerie complète n'a donc pas pu être inspectée avec la surface read-only actuelle. Elle reste
**MANQUANTE**. Il serait faux de conclure que la galerie ne contient aucune vue complète ; en revanche,
aucune vue complète n'est aujourd'hui prouvée et exploitable.

## Condition de déblocage

Une preuve conforme doit être attribuable au SKU Black exact et montrer dans un même cadre :

1. les quatre vis du boîtier ;
2. les trois saillies distinctes à droite ;
3. le bracelet intégré complet, jusqu'au fermoir ou à la boucle ;
4. le cadran/mouvement Black correspondant à `14:200000080#Black`.

Cette preuve peut venir d'une extension autorisée du gateway exposant la galerie, d'un export officiel
brut `aliexpress.ds.product.get` sans secrets, ou d'une nouvelle photo fournisseur exacte. Ne pas
recolorer White, ne pas assembler plusieurs images et ne pas inventer les maillons ou le fermoir.

## Non-actions

- aucun ordre créé ou modifié ;
- aucun accès Shopify ou DSers ;
- aucune génération ;
- aucune nouvelle source incomplète conservée ;
- aucun commit ni push.

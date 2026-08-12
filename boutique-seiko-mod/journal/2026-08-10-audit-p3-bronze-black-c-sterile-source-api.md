# Audit P3 Bronze — source complète `black C-sterile` — API officielle — 10/08/2026

## Verdict

**BLOQUÉ — aucune photo exacte complète n'est prouvée par la surface API officielle accessible.**

Le fragment `14:201447303#black C-sterile` est bien retrouvé sans ambiguïté sur l'article
AliExpress `1005009879577159`, mais son unique image de propriété est un gros plan : elle prouve le
cadran, le boîtier et la couronne, pas le bracelet complet avec sa boucle. Le contrôle des 18 images
SKU uniques de l'article ne révèle aucune autre vue complète. La galerie brute du produit reste
**MANQUANTE** parce qu'elle n'est pas exposée par l'action `variants` du gateway read-only actuel.

Aucun ordre de génération n'est créé. Aucune nouvelle image n'est conservée comme source complète.

## Identité officielle retrouvée

- Article : `1005009879577159`.
- Vendeur : `tandorio Timepieces Store`, magasin `3209151`.
- Statut API : `onSelling`.
- Fragment couleur exact : `14:201447303#black C-sterile`.
- Image de propriété exacte :
  `https://ae01.alicdn.com/kf/S71b42ec4014e4c43a9137d894e609871d.jpg`.
- Preuve locale préexistante :
  `boutique-seiko-mod/preuves/preuves-p3-variantes-api-2026-08-10-agent/sources-propres/field-bronze-10-14-201447303-black-c-sterile.jpg`.

Deux SKU officiels utilisent exactement cette même image de propriété :

| Fond | SKU API | `sku_attr` exact | Stock observé | Prix API |
|---|---|---|---:|---:|
| Acier | `12000050458622328` | `5:5203931210#Solid caseback;14:201447303#black C-sterile` | 229 | 115,39 EUR |
| Verre | `12000050458622327` | `5:5203931209#Glass caseback;14:201447303#black C-sterile` | 228 | 115,39 EUR |

Les valeurs sont celles de l'appel `variants` observé à `2026-08-10T00:24:18Z` ; elles documentent
l'identité de la source, pas une décision commerciale.

## Contrôle visuel des images SKU

L'appel officiel renvoie 36 SKU, regroupés en 18 apparences visuelles et 18 URL d'image uniques. Les
18 images ont été téléchargées temporairement depuis les URL CDN renvoyées par l'API et contrôlées en
planche 6 × 3, avec 500 px par vignette. L'image exacte `black C-sterile` a en plus été ouverte seule à
sa résolution originale de 1000 × 1000 px.

Constats :

- la source exacte montre nettement le cadran noir stérile à chiffres crème avec date, le boîtier
  bronze/PVD, les cornes et la couronne ;
- le bracelet en cuir n'est visible que par segments en haut et en bas ; sa longueur complète et sa
  boucle ne sont pas visibles ;
- les autres images SKU sont du même type : gros plans inclinés ou portés poignet ;
- aucune des 18 images ne montre une montre complète avec boîtier, couronne, les deux longueurs du
  bracelet et sa boucle dans le même cadre ;
- les autres images correspondent en outre à d'autres fragments de couleur et ne peuvent pas servir
  de vérité produit à `black C-sterile`.

Les téléchargements et la planche temporaires ne sont pas promus en preuves locales : ils ne
satisfont pas la condition de source exacte complète.

## Galerie officielle : limite observée

Route saine utilisée :
`codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, vers AliExpress Open Platform /
AE-Dropshipper sur le VPS à IP autorisée.

- `health` : OK à `2026-08-10T00:24:11Z` ;
- `variants 1005009879577159` : OK à `2026-08-10T00:24:18Z` ;
- l'action `variants` expose les images de propriété SKU mais normalise volontairement la réponse et
  ne renvoie pas `ae_multimedia_info_dto.image_urls`, champ qui contient la galerie dans la réponse
  brute `aliexpress.ds.product.get` ;
- un appel read-only direct à cette même méthode officielle depuis le Mac a été essayé sans afficher
  aucun secret et a été refusé avec `AppWhiteIpLimit` : l'IP locale n'appartient pas à la whitelist de
  l'application ;
- aucun navigateur AliExpress, scraping, contournement de whitelist, port forwarding ou accès shell
  VPS n'a été utilisé.

Il serait donc faux d'affirmer que la galerie complète a été inspectée. La donnée reste **MANQUANTE**,
et une recherche négative parmi les images SKU ne prouve pas que la galerie ne contient aucune photo
complète. Elle empêche simplement de qualifier honnêtement une source aujourd'hui.

## Condition de déblocage

Une seule des preuves suivantes suffit à rouvrir l'audit :

1. exposer en lecture seule `ae_multimedia_info_dto.image_urls` via une extension autorisée du gateway,
   puis contrôler visuellement toutes les URL de galerie ;
2. fournir un export officiel brut `aliexpress.ds.product.get` de cet article, sans secrets ;
3. fournir une nouvelle photo exacte attribuable au fragment `14:201447303#black C-sterile`, montrant
   dans le même cadre le boîtier, la couronne et le bracelet complet avec sa boucle.

Jusqu'à cette preuve, ne pas générer depuis une autre couleur, ne pas recomposer le bracelet depuis
plusieurs SKU et ne pas transformer le gros plan existant en prétendue vue complète.

## Non-actions

- aucun accès Shopify ou DSers ;
- aucun ordre créé ou modifié ;
- aucune génération ;
- aucune image candidate incomplète conservée comme nouvelle source ;
- aucun commit ni push.

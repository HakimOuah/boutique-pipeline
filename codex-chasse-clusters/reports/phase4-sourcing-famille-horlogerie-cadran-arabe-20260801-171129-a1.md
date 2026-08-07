# Sourcing — cadran à chiffres arabo-orientaux

- Première recherche : 2026-08-01
- Qualification live : 2026-08-02 à 18:32:59 UTC
- Demande : montre AliExpress avec chiffres arabo-orientaux `١٢٣٤٥٦٧٨٩`.
- Statut : `QUALIFIE_TECHNIQUEMENT — REVUE COMMERCIALE REQUISE`.
- Source : AliExpress Open Platform / AE-Dropshipper depuis le VPS whitelisté.

## Offre exacte qualifiée

**Tandorio 36/39 mm — variante 36 mm, cadran blanc sans logo Tandorio.**

- Item ID : `1005010249362754`
- SKU exact : `12000051675733200`
- Variante : `white sterile` + `36mm-glass back`
- [Lien AliExpress avec SKU](https://fr.aliexpress.com/item/1005010249362754.html?skuId=12000051675733200)
- [Lien produit de secours](https://fr.aliexpress.com/item/1005010249362754.html)

Le paramètre d’URL peut être réécrit par AliExpress. Avant toute importation,
contrôler que l’interface affiche encore les deux libellés ci-dessus et le SKU
`12000051675733200`.

## OBSERVÉ LIVE

- Produit `onSelling`.
- Stock du SKU exact : **300**.
- Prix du SKU, taxe incluse selon l’API : **102,39 €**.
- Livraison France : **1,99 €**, AliExpress Selection Standard, suivie.
- Expédition depuis la Chine ; délai API **8 à 11 jours**.
- Coût rendu observé par addition : **104,38 €**.
- Produit : **4,7/5**, **3 évaluations**, **8 ventes**.
- Boutique : `tandorio Timepieces Store`, notes description, communication et
  vitesse d’expédition toutes à **4,8/5**.
- L’image du SKU montre un cadran blanc/argenté avec chiffres arabo-orientaux,
  sans mot-symbole Tandorio ; l’inscription `Automatic` reste présente.
- L’attribut API complet est
  `5:57036539#36mm-glass back;14:175#white sterile`.

Preuve structurée :
`outputs/20260802/aliexpress-live-exact-1005010249362754-20260802T183259Z.json`.

## Anomalie de traduction à conserver

Le champ brut de couleur renvoyé par AliExpress vaut `vert`, alors que la
définition traduite vaut `white sterile`, que le `sku_attr` contient
`white sterile` et que l’image du SKU est blanche. La qualification repose sur
le SKU numérique, les deux propriétés complètes et l’image, pas sur ce seul
champ brut incohérent.

## MANQUANT / NON AUTORISÉ

- La fiche n’a que 8 ventes et 3 évaluations : fournisseur techniquement
  lisible, mais preuve commerciale encore faible.
- Le mouvement exact et les promesses 20 ATM/200 m ne sont pas requalifiés par
  cette sortie API minimale ; ne pas les reprendre en copywriting sans preuve
  attributaire supplémentaire.
- Aucune importation DSers, mutation Shopify, commande ou dépense n’a été faite.

## Verdict

`CANDIDAT_TECHNIQUE_QUALIFIE` — le lien, le SKU, la variante, le prix, le stock,
le visuel et le fret France sont désormais prouvés en direct. Ne pas confondre
ce verdict avec un feu vert commercial : le faible historique de ventes doit
être accepté ou compensé par un meilleur fournisseur avant lancement.

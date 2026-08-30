---
type: journal
boutique: seiko-mod
date: 2026-08-10
nature: intervention
leviers: [sourcing, creative]
titre: "Remplacement des photos AliExpress — 10 août 2026"
---

# Remplacement des photos AliExpress — 10 août 2026

## Périmètre

- Boutique : Maison Noirmont (`maisonnoirmont.fr`)
- Produit pilote : `cadran-pilote-noir-33-5-nh34`
- Product GID : `gid://shopify/Product/11013081465170`
- Statut avant intervention : `DRAFT`
- Variantes : 6

## Règle appliquée

Une photo fournisseur n'est retirée que si elle remplit simultanément les
conditions suivantes :

1. elle n'est associée à aucune variante du produit ;
2. elle n'est utilisée par aucun autre produit Shopify ;
3. un visuel Maison Noirmont validé est déjà disponible pour prendre sa place
   dans la galerie générale ;
4. le statut, les SKU, les prix, le stock et les associations des variantes ne
   sont pas modifiés.

Les photos fournisseur encore nécessaires pour distinguer une variante restent
en place jusqu'à la production d'un remplacement exact et validé.

## Prévol Shopify

Le produit comptait 15 médias :

- 12 photos fournisseur AliExpress, sans texte alternatif ;
- 3 visuels Maison Noirmont en 2048 × 2048, statut `READY`.

Les six médias fournisseur suivants n'étaient associés à aucune variante. Un
scan paginé des 199 produits de la boutique a confirmé qu'ils n'étaient utilisés
par aucun autre produit :

| Media GID | URL Shopify sauvegardée |
|---|---|
| `gid://shopify/MediaImage/59894150037842` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S3c194f10aeb546408dd98af15bd3445ec.webp?v=1786233511` |
| `gid://shopify/MediaImage/59894150070610` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/H45581f0e1adc4c65975be7b7e2cc32d1P.webp?v=1786233512` |
| `gid://shopify/MediaImage/59894150103378` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/H6f576946f5e3455c909ce653cd207c5e3.webp?v=1786233512` |
| `gid://shopify/MediaImage/59894150136146` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Hf3996c26ea2140d3b3c2d3b60dc54848d.webp?v=1786233512` |
| `gid://shopify/MediaImage/59894150168914` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Hd9c41b11de8e48da93464f225d121774B.webp?v=1786233512` |
| `gid://shopify/MediaImage/59894150201682` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Hd06032ac0cc34946a54395b7dc4ce87a5.webp?v=1786233512` |

Les six autres médias fournisseur restent chacun associés à une variante
distincte et ne font donc pas partie de ce retrait.

## Basculement de l'image principale

Le média Maison Noirmont
`gid://shopify/MediaImage/59904315195730` a été déplacé en première position.
Le job Shopify `gid://shopify/Job/668c82ce-87bb-4747-8837-50977276c367`
s'est terminé sans erreur. La relecture intermédiaire confirme :

- média principal Maison Noirmont ;
- statut toujours `DRAFT` ;
- six associations média-variante inchangées.

## Retrait et contrôle final

Le retrait ciblé est terminé sur les neuf brouillons : 160 médias avant.
Au total, 42 photos fournisseur redondantes ont été retirées ; il reste
118 médias après l'opération.

La relecture complète après mutation confirme sur les neuf produits :

- les 42 Media GID ciblés sont absents ;
- les 92 médias fournisseur encore liés aux variantes sont présents ;
- les 26 médias Maison Noirmont sont `READY` ;
- l'image principale est Maison Noirmont ;
- le statut reste `DRAFT` ;
- chaque GID de variante, association média, SKU, prix, quantité de stock et
  valeur d'option est inchangé ;
- aucune pagination résiduelle ne masque un média ou une variante.

Les 92 photos fournisseur restantes ne sont pas des doublons de galerie : elles
sont le seul témoin visuel exact de variantes encore sans remplacement validé.
Elles restent donc bloquées à la production, et non supprimées artificiellement.

## Lot suivant : huit brouillons habillés

Le même prévol a été appliqué aux huit autres brouillons. Les 36 médias
ci-dessous ne sont associés à aucune variante. Le scan paginé des 199
produits confirme que chacun n'est utilisé que par son produit d'origine.

| Produit | Media GID | URL Shopify sauvegardée |
|---|---|---|
| `cadran-meteorite-28-5` | `gid://shopify/MediaImage/59894115008850` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S593f46fbab4e4eb1ae0153a50c67a33fC.webp?v=1786233161` |
| `cadran-meteorite-28-5` | `gid://shopify/MediaImage/59894115041618` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S761e9beb8c6746a5a05a300f4c690a16y.webp?v=1786233162` |
| `cadran-meteorite-28-5` | `gid://shopify/MediaImage/59894115074386` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Sd6b6b80eb7fa4d58bae70f6a1efca5ff6.webp?v=1786233161` |
| `cadran-meteorite-28-5` | `gid://shopify/MediaImage/59894115107154` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S7720be45eea841469b46b90fc7c13b85V.webp?v=1786233162` |
| `cadran-meteorite-28-5` | `gid://shopify/MediaImage/59894115139922` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S9eb4e6ee80d147b18924b0b2f2f3ccc2Y.webp?v=1786233161` |
| `cadran-meteorite-28-5` | `gid://shopify/MediaImage/59894115172690` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S0c1e8c2b966d41bba7a18d8dd7b66e050.webp?v=1786233162` |
| `cadran-sterile-sunburst-28-5` | `gid://shopify/MediaImage/59894120415570` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S1a6fa2a804ca490a89d97cc7edd936adL.webp?v=1786233172` |
| `cadran-sterile-sunburst-28-5` | `gid://shopify/MediaImage/59894120448338` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S749bda2b793647b88e7b52e2101c8d142.webp?v=1786233173` |
| `cadran-sterile-sunburst-28-5` | `gid://shopify/MediaImage/59894120481106` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S24df97f299704d99ab560d07366844c3s.webp?v=1786233172` |
| `cadran-sterile-sunburst-28-5` | `gid://shopify/MediaImage/59894120513874` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Se5eb22e748bd442ab0846030e2510cce3.webp?v=1786233173` |
| `cadran-sterile-sunburst-28-5` | `gid://shopify/MediaImage/59894120546642` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S440ed56aea214597b634dfaa21ccf851R.webp?v=1786233173` |
| `cadran-sterile-sunburst-28-5` | `gid://shopify/MediaImage/59894120579410` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S966db4c28e7e42abae494d4587d87d11r.webp?v=1786233173` |
| `cadran-sterile-couronne-3h-28-5` | `gid://shopify/MediaImage/59894113960274` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S78f8f5365574432da8ad8ba9ebe3f1e6x.webp?v=1786233160` |
| `cadran-sterile-couronne-3h-28-5` | `gid://shopify/MediaImage/59894113993042` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Sc7b2615ef5e54b28ac4a3c947c5a8585z.webp?v=1786233160` |
| `cadran-sterile-couronne-3h-28-5` | `gid://shopify/MediaImage/59894114025810` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Sa76380ed2b734f5b8582b3d55de4aea9k.webp?v=1786233160` |
| `cadran-sterile-couronne-3h-28-5` | `gid://shopify/MediaImage/59894114058578` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S925d0c2805674ee6bfcaa50ac6d36944l.webp?v=1786233161` |
| `cadran-sterile-lumineux-28-5` | `gid://shopify/MediaImage/59894119760210` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Scbfed20e786941e5a3256e1aefe9efe7V.webp?v=1786233172` |
| `cadran-sterile-lumineux-28-5` | `gid://shopify/MediaImage/59894119792978` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S1de92914bb1e449b9da8b0da797f32b1e.webp?v=1786233172` |
| `cadran-vierge-sterile-28-5` | `gid://shopify/MediaImage/59894114320722` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Scfbc41126e3542a996436530e1d0191dZ.webp?v=1786233161` |
| `cadran-vierge-sterile-28-5` | `gid://shopify/MediaImage/59894114353490` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S1afd990c8f2945cd97fba686cc33a48af.webp?v=1786233161` |
| `cadran-vierge-sterile-28-5` | `gid://shopify/MediaImage/59894114386258` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S8a158e1f8aab40afa79264efad5ac8cbf.webp?v=1786233160` |
| `cadran-vierge-sterile-28-5` | `gid://shopify/MediaImage/59894114419026` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S7317c97e57ac489b899f083a4f31114f9.webp?v=1786233161` |
| `cadran-vierge-sterile-28-5` | `gid://shopify/MediaImage/59894114451794` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Sd83c6f8a2bab4333b2e6e7fb1544d405T.webp?v=1786233160` |
| `cadran-vierge-sterile-28-5` | `gid://shopify/MediaImage/59894114484562` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S2f2b73020b844add9f1d72e211c63f84u.webp?v=1786233160` |
| `cadran-pilote-29-mod-nh35` | `gid://shopify/MediaImage/59894151315794` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Sdd6a18c18a1b420bab35e9b1e947891aS.webp?v=1786233513` |
| `cadran-pilote-29-mod-nh35` | `gid://shopify/MediaImage/59894151348562` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S7456437852da4e26a0da8793a32eab726.webp?v=1786233512` |
| `cadran-pilote-29-mod-nh35` | `gid://shopify/MediaImage/59894151381330` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S887741e3b52b466c969165c5f1c1f4d7l.webp?v=1786233513` |
| `cadran-pilote-29-mod-nh35` | `gid://shopify/MediaImage/59894151414098` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S4e323c38f4f94774a78e796a09532f15s.webp?v=1786233512` |
| `cadran-pilote-29-mod-nh35` | `gid://shopify/MediaImage/59894151446866` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S6a4ba1b4bd444de2817e401cc40df878R.webp?v=1786233513` |
| `cadran-pilote-29-mod-nh35` | `gid://shopify/MediaImage/59894151479634` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S59c0467d03574a5d925b4bf2655c457fi.webp?v=1786233512` |
| `cadran-pilote-33-5-aiguilles-blanches` | `gid://shopify/MediaImage/59894152790354` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S53e73844d9d74eafa08503d5f651d5d0V.webp?v=1786233514` |
| `cadran-pilote-33-5-aiguilles-blanches` | `gid://shopify/MediaImage/59894152823122` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Sdd5e86ada7494cf384cbaaea28fe62c1I.webp?v=1786233514` |
| `cadran-pilote-33-5-aiguilles-blanches` | `gid://shopify/MediaImage/59894152855890` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S0fa332660bc746339aefe2e29b340e4ci.webp?v=1786233514` |
| `cadran-pilote-33-5-aiguilles-lumineuses` | `gid://shopify/MediaImage/59894149382482` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Se40051eb471846e8be6b78d26d939878w.webp?v=1786233512` |
| `cadran-pilote-33-5-aiguilles-lumineuses` | `gid://shopify/MediaImage/59894149415250` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/Sf8ce4b149378430e841914af168203ffg.webp?v=1786233512` |
| `cadran-pilote-33-5-aiguilles-lumineuses` | `gid://shopify/MediaImage/59894149448018` | `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/S585cbe89483a4ba794d0d4f81b6c7256Z.webp?v=1786233512` |

Avant retrait, le premier visuel Maison Noirmont de chaque produit a été
déplacé en tête. Les huit jobs Shopify se sont terminés sans erreur. La
relecture intermédiaire confirme pour chacun : statut `DRAFT`, image
principale Maison Noirmont et instantané des variantes inchangé.

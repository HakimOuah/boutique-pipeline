---
type: journal
boutique: seiko-mod
date: 2026-08-10
nature: analyse
leviers: [technique]
titre: "Audit P3 — Squelette Octogone Black — source complète API — 10/08/2026"
---

# Audit P3 — Squelette Octogone Black — source complète API — 10/08/2026

## Verdict

**BLOQUÉ — aucune source exacte complète ne prouve simultanément le mouvement, le bracelet complet
et le nombre total réel de vis de lunette.**

Le fragment `14:200000080#Black Skeleton` est retrouvé sans ambiguïté sur l'article AliExpress
`1005009354912699`. Les deux SKU Black utilisent la même image de propriété oblique. Elle prouve le
mouvement squelette et montre **exactement cinq vis de lunette visibles**, mais elle coupe le bracelet
et masque les autres positions éventuelles. On ne peut donc ni affirmer un total de six ou huit vis,
ni inventer les vis non observables.

Aucun ordre n'est créé. Aucune nouvelle image n'est qualifiée ou conservée comme source complète.

## Identité officielle

- Produit : `1005009354912699`.
- Titre API : `Tandorio noir blanc cadran squelette ingénieur Style montre mécanique pour hommes
  verre saphir 100m étanche NH70 montres automatiques`.
- Vendeur : `Tandorio_watch Store`, magasin `5376237`.
- Statut : `onSelling`.
- Note : 5,0 ; 2 évaluations ; 9 ventes observées.
- Fragment exact : `14:200000080#Black Skeleton`.
- Image SKU exacte commune :
  `https://ae01.alicdn.com/kf/S6329b301e2be4c959a8abfd5cac697f75.jpg`.
- Preuve locale préexistante :
  `boutique-seiko-mod/preuves/preuves-p3-variantes-api-2026-08-10-agent/sources-propres/squelette-octogone-01-14-200000080-black-skeleton.jpg`.

Les deux SKU exacts sont :

| Fond | SKU API | `sku_attr` exact | Stock observé | Prix API |
|---|---|---|---:|---:|
| Verre | `12000048851198043` | `5:57000035#Glass Back;14:200000080#Black Skeleton` | 197 | 124,39 EUR |
| Acier | `12000048851198042` | `5:56964930#Steel Back;14:200000080#Black Skeleton` | 200 | 123,99 EUR |

Ces valeurs proviennent de l'appel officiel `variants` observé à `2026-08-10T00:51:46Z`. Elles
établissent l'identité du SKU, pas une décision commerciale.

## Contrôle visuel à la résolution originale

L'article contient quatre SKU mais seulement deux images de propriété distinctes : White Skeleton et
Black Skeleton. Les deux fichiers CDN officiels ont été téléchargés temporairement et ouverts à leur
résolution originale de 1000 × 1000 px.

### Black Skeleton — fragment demandé

L'image exacte prouve :

- le cadran ouvert et le mouvement squelette visible ;
- le boîtier octogonal en acier et la couronne ;
- le départ du bracelet intégré sur les deux côtés ;
- cinq vis de lunette visibles, situées approximativement à 10 h 30, 1 h 30, 3 h 30, 6 h et 8 h 30.

Elle ne prouve pas :

- les deux longueurs complètes du bracelet ;
- le fermoir ;
- le nombre total de vis physiques, car l'angle oblique et le boîtier masquent les autres positions.

Le comptage visuel strict est donc **5 visibles**. Le motif historique du rejet, qui parlait de six
vis visibles dans la source, doit être corrigé sur ce point ; la conclusion du rejet reste toutefois
valide, car huit vis ne sont pas prouvées et les inventer falsifierait le produit.

### White Skeleton — autre fragment

L'image White reprend le même angle, le même cadrage incomplet du bracelet et les mêmes cinq vis
visibles. Elle ne débloque donc pas le comptage et correspond en outre à
`14:200005100#White Skeleton`, pas au fragment Black. Aucun recoloriage ou transfert de mouvement
n'est acceptable.

## Galerie et image principale : données manquantes

Route utilisée : client local read-only
`codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, vers AliExpress Open Platform /
AE-Dropshipper sur le VPS à IP autorisée.

- `health` : OK à `2026-08-10T00:51:43Z` ;
- `variants 1005009354912699` : OK à `2026-08-10T00:51:46Z` ;
- le gateway expose les images de propriété SKU, mais pas
  `ae_multimedia_info_dto.image_urls`, champ de galerie de la réponse brute
  `aliexpress.ds.product.get` ;
- trois recherches officielles ciblées sur le titre, avec tris `orders` et `price_desc`, n'ont pas
  fait remonter l'ID exact dans les 20 premiers résultats ;
- une recherche supplémentaire sur l'ID numérique exact n'a pas non plus retourné l'article ;
- l'appel officiel direct depuis le Mac est refusé par la whitelist IP de l'application avec
  `AppWhiteIpLimit` ; aucun contournement n'a été tenté.

La galerie complète reste donc **MANQUANTE** et n'a pas été inspectée. Il serait faux d'affirmer
qu'elle ne contient aucune vue frontale complète ; en revanche, aucune telle vue n'est aujourd'hui
prouvée par la surface API officielle accessible.

## Conséquence après les quatre essais rejetés

La source disponible ne permet pas une nouvelle génération fidèle d'une vue complète :

- imposer huit vis inventerait au moins trois vis non visibles dans la preuve ;
- imposer six vis inventerait encore une vis par rapport au comptage original ;
- conserver seulement cinq vis visibles ne prouverait pas le nombre physique total dans une vue
  frontale ;
- reconstruire le bracelet complet à partir d'une autre montre ou d'une autre variante falsifierait
  la vérité produit.

Le blocage est donc documentaire, pas un problème à résoudre par davantage de générations.

## Condition de déblocage

Une source conforme doit être attribuable à `14:200000080#Black Skeleton` et montrer dans un même
cadre :

1. le mouvement squelette exact ;
2. le bracelet intégré complet jusqu'au fermoir ;
3. la lunette sous un angle permettant de compter toutes les vis réellement présentes.

Cette preuve peut venir d'une extension autorisée du gateway exposant la galerie, d'un export officiel
brut `aliexpress.ds.product.get` sans secrets, ou d'une nouvelle photo fournisseur exacte. Ne pas
assembler plusieurs vues, recolorier White ni extrapoler la symétrie des vis.

## Non-actions

- aucun ordre créé ou modifié ;
- aucun accès Shopify ou DSers ;
- aucune génération ;
- aucune nouvelle source incomplète conservée ;
- aucun commit ni push.

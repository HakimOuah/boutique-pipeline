---
type: journal
boutique: seiko-mod
date: 2026-08-10
nature: intervention
leviers: [catalogue, technique]
titre: "Mapping opérationnel live — 16 médias Bracelet cuir daim"
---

# Mapping opérationnel live — 16 médias Bracelet cuir daim

**Relevé Shopify live :** 2026-08-10T01:46:02.898Z — lecture seule — fuseau projet Europe/Paris

## Conclusion

Le mapping est **SANS ÉCART** : 16/16 fichiers, 16/16 fragments fournisseur et 64/64 variantes Shopify live sont réconciliés. Chaque média est multi-variantes et doit être associé aux quatre largeurs `22mm`, `20mm`, `19mm` et `18mm` du même coloris.

Aucune des 64 variantes n’a actuellement de média associé au niveau variante. Il n’existe donc aucun ancien `media_id` à remplacer ou détacher. Les trois médias produit actuels doivent tous être préservés, en particulier l’image principale `gid://shopify/MediaImage/59691949293906`.

Les SKU live sont `NOIR-DAI-001` à `NOIR-DAI-064`. Ils attestent l’identité live mais ne remplacent jamais les fragments fournisseur des manifestes. La jointure durable est : `handle + premier fragment fournisseur du snapshot`, confirmée par `product_gid + variant_gid + titre` live.

## Préflight live

| Contrôle | Résultat |
|---|---:|
| Ordres | 2 |
| Médias attendus / mappés | 16 / 16 |
| Clés média uniques | 16 |
| Médias manquants | 0 |
| Variantes cibles attendues / live | 64 / 64 |
| GID variantes uniques | 64 |
| GID manquants | 0 |
| Écarts de titre snapshot ↔ live | 0 |
| SKU live normalisés `NOIR-DAI-*` | 64 / 64 |
| Médias multi-variantes | 16 |
| Médias mono-variante | 0 |
| Associations média existantes au niveau variante | 0 |
| Médias produit existants | 3 |
| Pagination incomplète | 0 |

Produit live :

- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Titre : Bracelet cuir daim — dégagement rapide
- Statut : `ACTIVE`

Médias produit à préserver :

| Media GID | Rôle | URL live |
|---|---|---|
| `gid://shopify/MediaImage/59691949293906` | **PRINCIPAL — PROTÉGÉ** | https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-cuir-daim-1.jpg?v=1785021583 |
| `gid://shopify/MediaImage/59694061027666` | Galerie existante — protégée | https://cdn.shopify.com/s/files/1/1094/1893/8706/files/bracelet-cuir-daim-degagement-rapide-02-situation.jpg?v=1785044194 |
| `gid://shopify/MediaImage/59694061060434` | Galerie existante — protégée | https://cdn.shopify.com/s/files/1/1094/1893/8706/files/bracelet-cuir-daim-degagement-rapide-03-macro.jpg?v=1785044194 |

## Mapping par ordre

### 20260810-0312-generate_images-p4-daim-boucles-noires-8.json

- Order ID : `claude-20260810-0312-p4-daim-boucles-noires-8`
- Manifeste de sortie : `manifeste-p4-daim-boucles-noires-8.json`
- Portée : 8 médias, 32 associations de variantes, 32 GID uniques
- Mode futur sûr : ajouter chaque média après les trois médias produit existants, récupérer son nouveau `media_id`, puis l’associer uniquement aux quatre GID listés. Aucun détachement, aucune suppression, image principale inchangée.

#### bracelet-cuir-daim-degagement-rapide-v-black-black.jpg

- Fragment fournisseur exact : `200000049:100013775#Black-Black`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/S98c21e2e334c43a38e0d4c5f1d5303d4a.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098054840658` | Black-Black / 22mm | `NOIR-DAI-017` | ∅ |
| `gid://shopify/ProductVariant/54098054873426` | Black-Black / 20mm | `NOIR-DAI-018` | ∅ |
| `gid://shopify/ProductVariant/54098054906194` | Black-Black / 19mm | `NOIR-DAI-019` | ∅ |
| `gid://shopify/ProductVariant/54098054938962` | Black-Black / 18mm | `NOIR-DAI-020` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-brown-black.jpg

- Fragment fournisseur exact : `200000049:1386586452#Brown-Black`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/Sa88679c6c5b74266b6809d3346715228E.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098055496018` | Brown-Black / 22mm | `NOIR-DAI-037` | ∅ |
| `gid://shopify/ProductVariant/54098055528786` | Brown-Black / 20mm | `NOIR-DAI-038` | ∅ |
| `gid://shopify/ProductVariant/54098055561554` | Brown-Black / 19mm | `NOIR-DAI-039` | ∅ |
| `gid://shopify/ProductVariant/54098055594322` | Brown-Black / 18mm | `NOIR-DAI-040` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-blue-black.jpg

- Fragment fournisseur exact : `200000049:201449057#Blue-Black`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/Sc56eee1ff4674b2ebe17cea4786ed97aK.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098054578514` | Blue-Black / 22mm | `NOIR-DAI-009` | ∅ |
| `gid://shopify/ProductVariant/54098054611282` | Blue-Black / 20mm | `NOIR-DAI-010` | ∅ |
| `gid://shopify/ProductVariant/54098054644050` | Blue-Black / 19mm | `NOIR-DAI-011` | ∅ |
| `gid://shopify/ProductVariant/54098054676818` | Blue-Black / 18mm | `NOIR-DAI-012` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-yellowbrown-black.jpg

- Fragment fournisseur exact : `200000049:2792782423#YellowBrown-Black`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/Sd44c42a518d14beaba9ee1b2c379c300n.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098055364946` | YellowBrown-Black / 22mm | `NOIR-DAI-033` | ∅ |
| `gid://shopify/ProductVariant/54098055397714` | YellowBrown-Black / 20mm | `NOIR-DAI-034` | ∅ |
| `gid://shopify/ProductVariant/54098055430482` | YellowBrown-Black / 19mm | `NOIR-DAI-035` | ∅ |
| `gid://shopify/ProductVariant/54098055463250` | YellowBrown-Black / 18mm | `NOIR-DAI-036` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-gray-black.jpg

- Fragment fournisseur exact : `200000049:350686#Gray-Black`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/Sf8fb008825de424ebbe2ed589a0893c6c.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098056020306` | Gray-Black / 22mm | `NOIR-DAI-053` | ∅ |
| `gid://shopify/ProductVariant/54098056053074` | Gray-Black / 20mm | `NOIR-DAI-054` | ∅ |
| `gid://shopify/ProductVariant/54098056085842` | Gray-Black / 19mm | `NOIR-DAI-055` | ∅ |
| `gid://shopify/ProductVariant/54098056118610` | Gray-Black / 18mm | `NOIR-DAI-056` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-beige-black.jpg

- Fragment fournisseur exact : `200000049:350850#Beige-Black`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/S8391ad335ef747e1b9d4c7ce89a2b4d9v.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098056282450` | Beige-Black / 22mm | `NOIR-DAI-061` | ∅ |
| `gid://shopify/ProductVariant/54098056315218` | Beige-Black / 20mm | `NOIR-DAI-062` | ∅ |
| `gid://shopify/ProductVariant/54098056347986` | Beige-Black / 19mm | `NOIR-DAI-063` | ∅ |
| `gid://shopify/ProductVariant/54098056380754` | Beige-Black / 18mm | `NOIR-DAI-064` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-light-blue-black.jpg

- Fragment fournisseur exact : `200000049:5057817297#Light Blue-Black`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/Sa8ee3a744fdb403ba336a710fe933064f.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098056151378` | Light Blue-Black / 22mm | `NOIR-DAI-057` | ∅ |
| `gid://shopify/ProductVariant/54098056184146` | Light Blue-Black / 20mm | `NOIR-DAI-058` | ∅ |
| `gid://shopify/ProductVariant/54098056216914` | Light Blue-Black / 19mm | `NOIR-DAI-059` | ∅ |
| `gid://shopify/ProductVariant/54098056249682` | Light Blue-Black / 18mm | `NOIR-DAI-060` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-green-black.jpg

- Fragment fournisseur exact : `200000049:506942013#Green-Black`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/S65c5cae85ef74c44bbfaef0469d00fb0u.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098054709586` | Green-Black / 22mm | `NOIR-DAI-013` | ∅ |
| `gid://shopify/ProductVariant/54098054742354` | Green-Black / 20mm | `NOIR-DAI-014` | ∅ |
| `gid://shopify/ProductVariant/54098054775122` | Green-Black / 19mm | `NOIR-DAI-015` | ∅ |
| `gid://shopify/ProductVariant/54098054807890` | Green-Black / 18mm | `NOIR-DAI-016` | ∅ |

### 20260810-0312-generate_images-p4-daim-boucles-argentees-8.json

- Order ID : `claude-20260810-0312-p4-daim-boucles-argentees-8`
- Manifeste de sortie : `manifeste-p4-daim-boucles-argentees-8.json`
- Portée : 8 médias, 32 associations de variantes, 32 GID uniques
- Mode futur sûr : ajouter chaque média après les trois médias produit existants, récupérer son nouveau `media_id`, puis l’associer uniquement aux quatre GID listés. Aucun détachement, aucune suppression, image principale inchangée.

#### bracelet-cuir-daim-degagement-rapide-v-beige.jpg

- Fragment fournisseur exact : `200000049:16146268#Beige`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/S7c2e0551689e4afb828f1a327789c6e4G.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098055102802` | Beige / 22mm | `NOIR-DAI-025` | ∅ |
| `gid://shopify/ProductVariant/54098055135570` | Beige / 20mm | `NOIR-DAI-026` | ∅ |
| `gid://shopify/ProductVariant/54098055168338` | Beige / 19mm | `NOIR-DAI-027` | ∅ |
| `gid://shopify/ProductVariant/54098055201106` | Beige / 18mm | `NOIR-DAI-028` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-yellowbrown.jpg

- Fragment fournisseur exact : `200000049:1714056674#YellowBrown`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/S1be603d46c3643c8a5ac8f3cb18fdaded.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098054447442` | YellowBrown / 22mm | `NOIR-DAI-005` | ∅ |
| `gid://shopify/ProductVariant/54098054480210` | YellowBrown / 20mm | `NOIR-DAI-006` | ∅ |
| `gid://shopify/ProductVariant/54098054512978` | YellowBrown / 19mm | `NOIR-DAI-007` | ∅ |
| `gid://shopify/ProductVariant/54098054545746` | YellowBrown / 18mm | `NOIR-DAI-008` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-blue.jpg

- Fragment fournisseur exact : `200000049:200966040#Blue`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/Sd46d6d829d914c33bde451d852978361d.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098055233874` | Blue / 22mm | `NOIR-DAI-029` | ∅ |
| `gid://shopify/ProductVariant/54098055266642` | Blue / 20mm | `NOIR-DAI-030` | ∅ |
| `gid://shopify/ProductVariant/54098055299410` | Blue / 19mm | `NOIR-DAI-031` | ∅ |
| `gid://shopify/ProductVariant/54098055332178` | Blue / 18mm | `NOIR-DAI-032` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-green.jpg

- Fragment fournisseur exact : `200000049:201449058#Green`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/S18b312d8c1114ebf976e381035d57a6fN.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098054971730` | Green / 22mm | `NOIR-DAI-021` | ∅ |
| `gid://shopify/ProductVariant/54098055004498` | Green / 20mm | `NOIR-DAI-022` | ∅ |
| `gid://shopify/ProductVariant/54098055037266` | Green / 19mm | `NOIR-DAI-023` | ∅ |
| `gid://shopify/ProductVariant/54098055070034` | Green / 18mm | `NOIR-DAI-024` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-black.jpg

- Fragment fournisseur exact : `200000049:3348727#Black`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/S2f0920aadd4d43969e8d45fae7d1c069k.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098055889234` | Black / 22mm | `NOIR-DAI-049` | ∅ |
| `gid://shopify/ProductVariant/54098055922002` | Black / 20mm | `NOIR-DAI-050` | ∅ |
| `gid://shopify/ProductVariant/54098055954770` | Black / 19mm | `NOIR-DAI-051` | ∅ |
| `gid://shopify/ProductVariant/54098055987538` | Black / 18mm | `NOIR-DAI-052` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-light-blue.jpg

- Fragment fournisseur exact : `200000049:5057743953#Light Blue`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/S5d97cfd4b82e4672912c81a49d7a1b65N.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098055627090` | Light Blue / 22mm | `NOIR-DAI-041` | ∅ |
| `gid://shopify/ProductVariant/54098055659858` | Light Blue / 20mm | `NOIR-DAI-042` | ∅ |
| `gid://shopify/ProductVariant/54098055692626` | Light Blue / 19mm | `NOIR-DAI-043` | ∅ |
| `gid://shopify/ProductVariant/54098055725394` | Light Blue / 18mm | `NOIR-DAI-044` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-gray.jpg

- Fragment fournisseur exact : `200000049:5057835040#Gray`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/S69cd4a751b48418abbc9c70a88ae5d0b1.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098055758162` | Gray / 22mm | `NOIR-DAI-045` | ∅ |
| `gid://shopify/ProductVariant/54098055790930` | Gray / 20mm | `NOIR-DAI-046` | ∅ |
| `gid://shopify/ProductVariant/54098055823698` | Gray / 19mm | `NOIR-DAI-047` | ∅ |
| `gid://shopify/ProductVariant/54098055856466` | Gray / 18mm | `NOIR-DAI-048` | ∅ |

#### bracelet-cuir-daim-degagement-rapide-v-brown.jpg

- Fragment fournisseur exact : `200000049:990994103#Brown`
- Source : `scratchpad/backup-medias-accessoires-lot4/bracelet-cuir-daim-degagement-rapide/Sd4fbcbfac3664e8ba91e7be0dc9dbbe3A.webp`
- Handle : `bracelet-cuir-daim-degagement-rapide`
- Product GID : `gid://shopify/Product/10980388897106`
- Cardinalité : **multi-variante**, 4 variantes

| Variant GID live | Titre live | SKU live | Association média actuelle |
|---|---|---|---|
| `gid://shopify/ProductVariant/54098054316370` | Brown / 22mm | `NOIR-DAI-001` | ∅ |
| `gid://shopify/ProductVariant/54098054349138` | Brown / 20mm | `NOIR-DAI-002` | ∅ |
| `gid://shopify/ProductVariant/54098054381906` | Brown / 19mm | `NOIR-DAI-003` | ∅ |
| `gid://shopify/ProductVariant/54098054414674` | Brown / 18mm | `NOIR-DAI-004` | ∅ |

## Lots futurs sûrs

Les deux ordres forment deux lots indépendants par finition de boucle. Pour chaque lot :

1. Vérifier que les huit JPEG livrés passent la QA visuelle, sans `GIFT`, `V4`, texte, logo ou variation de boucle.
2. Relire immédiatement avant mutation le produit, les 64 variantes, leurs associations média et le `featuredMedia`; arrêter si un GID, titre ou association diffère de ce relevé.
3. Ajouter les huit nouveaux médias à la fin de la galerie produit ; ne jamais remplacer ni supprimer les trois médias existants.
4. Récupérer les huit nouveaux `media_id`, puis associer chaque média aux quatre `variant_gids` de son groupe, par exemple via `productVariantAppendMedia`.
5. Réinterroger les 32 variantes du lot : chaque groupe doit contenir son nouveau média, aucune variante d’un autre coloris ne doit l’avoir, et `featuredMedia` doit rester `gid://shopify/MediaImage/59691949293906`.
6. Aucun détachement n’est attendu, car le relevé live compte zéro association média variante existante.

## Limites et actions non effectuées

- Le mapping ne prouve pas encore la conformité des futurs JPEG générés : la QA fichier reste un gate séparé.
- Aucun upload, rattachement, détachement ou suppression Shopify.
- Aucun accès ni changement DSers.
- Aucun ordre lancé.
- Aucun commit/push.

Le JSON compagnon est la source machine opérationnelle ; ce rapport en fournit la lecture humaine.

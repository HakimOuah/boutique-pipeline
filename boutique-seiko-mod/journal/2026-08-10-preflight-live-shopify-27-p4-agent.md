# Préflight Shopify live — 27 médias P4 qualifiés

**Date du relevé live :** 10 août 2026 à 03:03 (Europe/Paris)

**Périmètre :** lecture seule de Maison Noirmont (`maisonnoirmont.fr`) via l’API Admin Shopify connectée. Aucun média joint, détaché ou supprimé ; aucun ordre lancé ; aucune donnée Shopify/DSers modifiée.

## Décision opérationnelle

Le mapping local est **réconcilié sans écart d’identité** avec l’état Shopify live : 7/7 produits, 27/27 médias planifiés et 117/117 variantes cibles existent aux GID attendus. Les 7 produits sont `ACTIVE`; les 117 titres de variante correspondent au snapshot local et les 117 fragments fournisseur de l’ordre correspondent au premier fragment de `sku_actuel` du snapshot.

Les SKU live ont depuis été normalisés en `NOIR-*`. Ils ne doivent donc pas servir à refaire la jointure fournisseur. La jointure sûre reste : `product_gid` + `variant_gid` live, avec le titre live comme contrôle humain et le fragment fournisseur conservé comme preuve de sourcing.

Verdict de préflight :

- **26 médias :** association initiale sûre après QA des fichiers générés. Les 116 variantes concernées n’ont actuellement aucune association média au niveau variante (`ancien media_id = ∅`). Ajouter le nouveau média à la fin de la galerie puis l’associer seulement aux GID listés ; ne rien détacher ni supprimer.
- **1 média — WB13 / rouleau 3 montres :** remplacement d’association en deux temps. L’ancien média `gid://shopify/MediaImage/59691418714450` est le média principal du produit et reste partagé avec les variantes 1 et 2 montres. Ajouter et associer le nouveau média à la variante 3 montres, vérifier la nouvelle association, puis — seulement si un remplacement strict est requis — détacher l’association ancien média ↔ variante 3 montres avec `productVariantDetachMedia`. **Ne jamais supprimer l’ancien média du produit.**
- **Image principale :** conserver les 7 `featuredMedia` actuels. Tous les nouveaux médias doivent être ajoutés après les médias existants, jamais en position 1.

## Réconciliation globale

| Contrôle | Résultat live |
|---|---:|
| Produits interrogés | 7 |
| Produits `ACTIVE` | 7/7 |
| Médias P4 planifiés | 27/27 |
| GID variantes cibles uniques | 117/117 |
| GID variantes manquants | 0 |
| Variantes rattachées au mauvais produit | 0 |
| Écarts de titre snapshot ↔ live | 0 |
| Écarts fragment fournisseur ordre ↔ snapshot | 0 |
| SKU live `NOIR-*` | 117/117 |
| Variantes cibles avec média déjà associé | 1 |
| Variantes cibles sans média associé | 116 |
| Variantes live totales sur les 7 produits | 126 |
| Variantes live hors lot P4 | 9 |
| Médias produits existants | 21 (3 par produit) |
| Pagination incomplète | 0 |

`∅` ci-dessous signifie : aucune association média au niveau de la variante. Cela ne signifie pas que le produit n’a pas de galerie ; chaque produit a bien trois médias produit.

## Lots sûrs par ordre

### 20260810-0130-generate_images-p4-acier-massif-6.json

- Produit : `bracelet-acier-massif-12-22-mm` — `gid://shopify/Product/10980388438354` — statut live `ACTIVE`
- Portée : 6 média(s), 60 variante(s) cible(s) sur 60 variante(s) live
- Média principal à préserver : `gid://shopify/MediaImage/59691847483730` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-jubile-plat-1.jpg?v=1785020481
- Mode sûr : `APPEND + ATTACH ONLY`; zéro détachement et zéro suppression
- Galerie live complète :
  - `gid://shopify/MediaImage/59691847483730` **[PRINCIPAL — PROTÉGÉ]** — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-jubile-plat-1.jpg?v=1785020481
  - `gid://shopify/MediaImage/59694060896594` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/bracelet-acier-massif-12-22-mm-02-situation.jpg?v=1785044194
  - `gid://shopify/MediaImage/59694060929362` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/bracelet-acier-massif-12-22-mm-03-macro.jpg?v=1785044194

#### bracelet-acier-massif-12-22-mm-v-rose-gold.jpg

- Fragment fournisseur exact : `200000049:16146268#Rose-Gold`
- Cibles : 10 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098038817106` | Rose-Gold / 16mm | `NOIR-ACI-001` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038849874` | Rose-Gold / 17mm | `NOIR-ACI-002` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038882642` | Rose-Gold / 18mm | `NOIR-ACI-003` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038915410` | Rose-Gold / 19mm | `NOIR-ACI-004` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038980946` | Rose-Gold / 12mm | `NOIR-ACI-006` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039013714` | Rose-Gold / 13mm | `NOIR-ACI-007` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039046482` | Rose-Gold / 14mm | `NOIR-ACI-008` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040291666` | Rose-Gold / 20mm | `NOIR-ACI-046` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040324434` | Rose-Gold / 21mm | `NOIR-ACI-047` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040357202` | Rose-Gold / 22mm | `NOIR-ACI-048` | ∅ | OK |

#### bracelet-acier-massif-12-22-mm-v-gold.jpg

- Fragment fournisseur exact : `200000049:193#Gold`
- Cibles : 10 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098039636306` | Gold / 20mm | `NOIR-ACI-026` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039669074` | Gold / 21mm | `NOIR-ACI-027` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039701842` | Gold / 22mm | `NOIR-ACI-028` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039767378` | Gold / 16mm | `NOIR-ACI-030` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039800146` | Gold / 17mm | `NOIR-ACI-031` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039832914` | Gold / 18mm | `NOIR-ACI-032` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039865682` | Gold / 19mm | `NOIR-ACI-033` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039931218` | Gold / 12mm | `NOIR-ACI-035` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039963986` | Gold / 13mm | `NOIR-ACI-036` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039996754` | Gold / 14mm | `NOIR-ACI-037` | ∅ | OK |

#### bracelet-acier-massif-12-22-mm-v-silver-gold.jpg

- Fragment fournisseur exact : `200000049:3348727#Silver-Gold`
- Cibles : 10 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098039898450` | Silver-Gold / 22mm | `NOIR-ACI-034` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040029522` | Silver-Gold / 18mm | `NOIR-ACI-038` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040062290` | Silver-Gold / 19mm | `NOIR-ACI-039` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040095058` | Silver-Gold / 20mm | `NOIR-ACI-040` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040127826` | Silver-Gold / 21mm | `NOIR-ACI-041` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040160594` | Silver-Gold / 13mm | `NOIR-ACI-042` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040193362` | Silver-Gold / 14mm | `NOIR-ACI-043` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040226130` | Silver-Gold / 16mm | `NOIR-ACI-044` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040258898` | Silver-Gold / 17mm | `NOIR-ACI-045` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040389970` | Silver-Gold / 12mm | `NOIR-ACI-049` | ∅ | OK |

#### bracelet-acier-massif-12-22-mm-v-silver-rosegold.jpg

- Fragment fournisseur exact : `200000049:350850#Silver-RoseGold`
- Cibles : 10 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098039374162` | Silver-RoseGold / 18mm | `NOIR-ACI-018` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039406930` | Silver-RoseGold / 19mm | `NOIR-ACI-019` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039439698` | Silver-RoseGold / 20mm | `NOIR-ACI-020` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039472466` | Silver-RoseGold / 21mm | `NOIR-ACI-021` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039505234` | Silver-RoseGold / 13mm | `NOIR-ACI-022` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039538002` | Silver-RoseGold / 14mm | `NOIR-ACI-023` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039570770` | Silver-RoseGold / 16mm | `NOIR-ACI-024` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039603538` | Silver-RoseGold / 17mm | `NOIR-ACI-025` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039734610` | Silver-RoseGold / 12mm | `NOIR-ACI-029` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040652114` | Silver-RoseGold / 22mm | `NOIR-ACI-057` | ∅ | OK |

#### bracelet-acier-massif-12-22-mm-v-black.jpg

- Fragment fournisseur exact : `200000049:365462#Black`
- Cibles : 10 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098040422738` | Black / 20mm | `NOIR-ACI-050` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040455506` | Black / 21mm | `NOIR-ACI-051` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040488274` | Black / 22mm | `NOIR-ACI-052` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040521042` | Black / 16mm | `NOIR-ACI-053` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040553810` | Black / 17mm | `NOIR-ACI-054` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040586578` | Black / 18mm | `NOIR-ACI-055` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040619346` | Black / 19mm | `NOIR-ACI-056` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040684882` | Black / 12mm | `NOIR-ACI-058` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040717650` | Black / 13mm | `NOIR-ACI-059` | ∅ | OK |
| `gid://shopify/ProductVariant/54098040750418` | Black / 14mm | `NOIR-ACI-060` | ∅ | OK |

#### bracelet-acier-massif-12-22-mm-v-silver.jpg

- Fragment fournisseur exact : `200000049:76119733#Silver`
- Cibles : 10 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098038948178` | Silver / 22mm | `NOIR-ACI-005` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039079250` | Silver / 18mm | `NOIR-ACI-009` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039112018` | Silver / 19mm | `NOIR-ACI-010` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039144786` | Silver / 20mm | `NOIR-ACI-011` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039177554` | Silver / 21mm | `NOIR-ACI-012` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039210322` | Silver / 13mm | `NOIR-ACI-013` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039243090` | Silver / 14mm | `NOIR-ACI-014` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039275858` | Silver / 16mm | `NOIR-ACI-015` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039308626` | Silver / 17mm | `NOIR-ACI-016` | ∅ | OK |
| `gid://shopify/ProductVariant/54098039341394` | Silver / 12mm | `NOIR-ACI-017` | ∅ | OK |

### 20260810-0130-generate_images-p4-coussins-10-5.json

- Produit : `coussins-de-presentation-lot-de-10` — `gid://shopify/Product/10980388569426` — statut live `ACTIVE`
- Portée : 5 média(s), 5 variante(s) cible(s) sur 5 variante(s) live
- Média principal à préserver : `gid://shopify/MediaImage/59691847549266` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-coussin-1.jpg?v=1785020482
- Mode sûr : `APPEND + ATTACH ONLY`; zéro détachement et zéro suppression
- Galerie live complète :
  - `gid://shopify/MediaImage/59691847549266` **[PRINCIPAL — PROTÉGÉ]** — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-coussin-1.jpg?v=1785020482
  - `gid://shopify/MediaImage/59694409122130` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/coussins-de-presentation-lot-de-10-02-situation.jpg?v=1785047376
  - `gid://shopify/MediaImage/59694409154898` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/coussins-de-presentation-lot-de-10-03-macro.jpg?v=1785047375

#### coussins-de-presentation-lot-de-10-v-red.jpg

- Fragment fournisseur exact : `14:10`
- Cibles : 1 variante(s)
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098040914258` | Red | `NOIR-COU-004` | ∅ | OK |

#### coussins-de-presentation-lot-de-10-v-blue.jpg

- Fragment fournisseur exact : `14:173`
- Cibles : 1 variante(s)
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098040881490` | Blue | `NOIR-COU-003` | ∅ | OK |

#### coussins-de-presentation-lot-de-10-v-black.jpg

- Fragment fournisseur exact : `14:193`
- Cibles : 1 variante(s)
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098040815954` | black | `NOIR-COU-001` | ∅ | OK |

#### coussins-de-presentation-lot-de-10-v-white.jpg

- Fragment fournisseur exact : `14:29`
- Cibles : 1 variante(s)
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098040848722` | WHITE | `NOIR-COU-002` | ∅ | OK |

#### coussins-de-presentation-lot-de-10-v-brown.jpg

- Fragment fournisseur exact : `14:365458`
- Cibles : 1 variante(s)
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098040947026` | Brown | `NOIR-COU-005` | ∅ | OK |

### 20260810-0130-generate_images-p4-etui-rigide-2.json

- Produit : `etui-de-voyage-rigide` — `gid://shopify/Product/10980388602194` — statut live `ACTIVE`
- Portée : 2 média(s), 2 variante(s) cible(s) sur 9 variante(s) live
- Média principal à préserver : `gid://shopify/MediaImage/59691847582034` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-etui-voyage-1.jpg?v=1785020482
- Mode sûr : `APPEND + ATTACH ONLY`; zéro détachement et zéro suppression
- Galerie live complète :
  - `gid://shopify/MediaImage/59691847582034` **[PRINCIPAL — PROTÉGÉ]** — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-etui-voyage-1.jpg?v=1785020482
  - `gid://shopify/MediaImage/59691847614802` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-etui-voyage-2.jpg?v=1785020482
  - `gid://shopify/MediaImage/59694428160338` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/etui-de-voyage-rigide-03-macro.jpg?v=1785047642

#### etui-de-voyage-rigide-v-black-purple-6-slot.jpg

- Fragment fournisseur exact : `14:173#Black Purple 6 Slot`
- Cibles : 1 variante(s)
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098045239634` | Black Purple 6 Slot | `NOIR-ETU-009` | ∅ | OK |

#### etui-de-voyage-rigide-v-black-green-6-slot.jpg

- Fragment fournisseur exact : `14:200006153#Black Green 6 Slot`
- Cibles : 1 variante(s)
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098045141330` | Black Green 6 Slot | `NOIR-ETU-006` | ∅ | OK |

### 20260810-0130-generate_images-p4-jubile-courbes-3.json

- Produit : `bracelet-jubile-embouts-courbes` — `gid://shopify/Product/10980388405586` — statut live `ACTIVE`
- Portée : 3 média(s), 15 variante(s) cible(s) sur 15 variante(s) live
- Média principal à préserver : `gid://shopify/MediaImage/59691847450962` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-jubile-courbe-1.jpg?v=1785020481
- Mode sûr : `APPEND + ATTACH ONLY`; zéro détachement et zéro suppression
- Galerie live complète :
  - `gid://shopify/MediaImage/59691847450962` **[PRINCIPAL — PROTÉGÉ]** — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-jubile-courbe-1.jpg?v=1785020481
  - `gid://shopify/MediaImage/59694061224274` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/bracelet-jubile-embouts-courbes-02-situation.jpg?v=1785044194
  - `gid://shopify/MediaImage/59694061257042` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/bracelet-jubile-embouts-courbes-03-macro.jpg?v=1785044195

#### bracelet-jubile-embouts-courbes-v-steel-gold-no-logo.jpg

- Fragment fournisseur exact : `200000049:100013777#steel gold-no logo`
- Cibles : 5 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098038325586` | steel gold-no logo / 22mm | `NOIR-JUB-005` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038554962` | steel gold-no logo / 18mm | `NOIR-JUB-012` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038587730` | steel gold-no logo / 19mm | `NOIR-JUB-013` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038620498` | steel gold-no logo / 20mm | `NOIR-JUB-014` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038653266` | steel gold-no logo / 21mm | `NOIR-JUB-015` | ∅ | OK |

#### bracelet-jubile-embouts-courbes-v-gold-no-logo.jpg

- Fragment fournisseur exact : `200000049:3348727#gold-no logo`
- Cibles : 5 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098038292818` | gold-no logo / 21mm | `NOIR-JUB-004` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038358354` | gold-no logo / 20mm | `NOIR-JUB-006` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038391122` | gold-no logo / 22mm | `NOIR-JUB-007` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038456658` | gold-no logo / 18mm | `NOIR-JUB-009` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038522194` | gold-no logo / 19mm | `NOIR-JUB-011` | ∅ | OK |

#### bracelet-jubile-embouts-courbes-v-steel-no-logo.jpg

- Fragment fournisseur exact : `200000049:350853#steel-no logo`
- Cibles : 5 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098038227282` | steel-no logo / 20mm | `NOIR-JUB-002` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038260050` | steel-no logo / 22mm | `NOIR-JUB-003` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038423890` | steel-no logo / 18mm | `NOIR-JUB-008` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038489426` | steel-no logo / 19mm | `NOIR-JUB-010` | ∅ | OK |
| `gid://shopify/ProductVariant/54098038686034` | steel-no logo / 21mm | `NOIR-JUB-016` | ∅ | OK |

### 20260810-0130-generate_images-p4-milanais-8.json

- Produit : `bracelet-milanais-maille-italienne` — `gid://shopify/Product/10980388864338` — statut live `ACTIVE`
- Portée : 8 média(s), 32 variante(s) cible(s) sur 32 variante(s) live
- Média principal à préserver : `gid://shopify/MediaImage/59691949261138` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-milanais-1.jpg?v=1785021583
- Mode sûr : `APPEND + ATTACH ONLY`; zéro détachement et zéro suppression
- Galerie live complète :
  - `gid://shopify/MediaImage/59691949261138` **[PRINCIPAL — PROTÉGÉ]** — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-milanais-1.jpg?v=1785021583
  - `gid://shopify/MediaImage/59694061388114` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/bracelet-milanais-maille-italienne-02-situation.jpg?v=1785044194
  - `gid://shopify/MediaImage/59694061420882` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/bracelet-milanais-maille-italienne-03-macro.jpg?v=1785044195

#### bracelet-milanais-maille-italienne-v-0-6mm-black.jpg

- Fragment fournisseur exact : `200000049:193#0.6mm-black`
- Cibles : 4 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098048516434` | 0.6mm-black / 24mm | `NOIR-MIL-025` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048549202` | 0.6mm-black / 22mm | `NOIR-MIL-026` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048581970` | 0.6mm-black / 20mm | `NOIR-MIL-027` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048614738` | 0.6mm-black / 18mm | `NOIR-MIL-028` | ∅ | OK |

#### bracelet-milanais-maille-italienne-v-1-0mm-gold.jpg

- Fragment fournisseur exact : `200000049:200000080#1.0mm-gold`
- Cibles : 4 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098047730002` | 1.0mm-gold / 18mm | `NOIR-MIL-001` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048385362` | 1.0mm-gold / 24mm | `NOIR-MIL-021` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048418130` | 1.0mm-gold / 22mm | `NOIR-MIL-022` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048450898` | 1.0mm-gold / 20mm | `NOIR-MIL-023` | ∅ | OK |

#### bracelet-milanais-maille-italienne-v-1-0mm-silver.jpg

- Fragment fournisseur exact : `200000049:200013899#1.0mm-silver`
- Cibles : 4 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098048254290` | 1.0mm-silver / 24mm | `NOIR-MIL-017` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048287058` | 1.0mm-silver / 22mm | `NOIR-MIL-018` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048319826` | 1.0mm-silver / 20mm | `NOIR-MIL-019` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048352594` | 1.0mm-silver / 18mm | `NOIR-MIL-020` | ∅ | OK |

#### bracelet-milanais-maille-italienne-v-1-0mm-rose-gold.jpg

- Fragment fournisseur exact : `200000049:29#1.0mm-rose gold`
- Cibles : 4 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098047893842` | 1.0mm-rose gold / 24mm | `NOIR-MIL-006` | ∅ | OK |
| `gid://shopify/ProductVariant/54098047926610` | 1.0mm-rose gold / 22mm | `NOIR-MIL-007` | ∅ | OK |
| `gid://shopify/ProductVariant/54098047959378` | 1.0mm-rose gold / 20mm | `NOIR-MIL-008` | ∅ | OK |
| `gid://shopify/ProductVariant/54098047992146` | 1.0mm-rose gold / 18mm | `NOIR-MIL-009` | ∅ | OK |

#### bracelet-milanais-maille-italienne-v-0-6mm-rose-gold.jpg

- Fragment fournisseur exact : `200000049:3348727#0.6mm-rose gold`
- Cibles : 4 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098048647506` | 0.6mm-rose gold / 24mm | `NOIR-MIL-029` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048680274` | 0.6mm-rose gold / 22mm | `NOIR-MIL-030` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048713042` | 0.6mm-rose gold / 20mm | `NOIR-MIL-031` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048745810` | 0.6mm-rose gold / 18mm | `NOIR-MIL-032` | ∅ | OK |

#### bracelet-milanais-maille-italienne-v-0-6mm-gold.jpg

- Fragment fournisseur exact : `200000049:350850#0.6mm-gold`
- Cibles : 4 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098048155986` | 0.6mm-gold / 24mm | `NOIR-MIL-014` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048188754` | 0.6mm-gold / 22mm | `NOIR-MIL-015` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048221522` | 0.6mm-gold / 20mm | `NOIR-MIL-016` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048483666` | 0.6mm-gold / 18mm | `NOIR-MIL-024` | ∅ | OK |

#### bracelet-milanais-maille-italienne-v-0-6mm-silver.jpg

- Fragment fournisseur exact : `200000049:350853#0.6mm-silver`
- Cibles : 4 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098048024914` | 0.6mm-silver / 24mm | `NOIR-MIL-010` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048057682` | 0.6mm-silver / 22mm | `NOIR-MIL-011` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048090450` | 0.6mm-silver / 20mm | `NOIR-MIL-012` | ∅ | OK |
| `gid://shopify/ProductVariant/54098048123218` | 0.6mm-silver / 18mm | `NOIR-MIL-013` | ∅ | OK |

#### bracelet-milanais-maille-italienne-v-1-0mm-black.jpg

- Fragment fournisseur exact : `200000049:366#1.0mm-black`
- Cibles : 4 variante(s) — média multi-variantes
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098047762770` | 1.0mm-black / 24mm | `NOIR-MIL-002` | ∅ | OK |
| `gid://shopify/ProductVariant/54098047795538` | 1.0mm-black / 22mm | `NOIR-MIL-003` | ∅ | OK |
| `gid://shopify/ProductVariant/54098047828306` | 1.0mm-black / 20mm | `NOIR-MIL-004` | ∅ | OK |
| `gid://shopify/ProductVariant/54098047861074` | 1.0mm-black / 18mm | `NOIR-MIL-005` | ∅ | OK |

### 20260810-0130-generate_images-p4-outil-taille-2.json

- Produit : `outil-de-mise-a-taille-de-bracelet` — `gid://shopify/Product/10980388766034` — statut live `ACTIVE`
- Portée : 2 média(s), 2 variante(s) cible(s) sur 2 variante(s) live
- Média principal à préserver : `gid://shopify/MediaImage/59691847811410` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-outil-bracelet-1.jpg?v=1785020482
- Mode sûr : `APPEND + ATTACH ONLY`; zéro détachement et zéro suppression
- Galerie live complète :
  - `gid://shopify/MediaImage/59691847811410` **[PRINCIPAL — PROTÉGÉ]** — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/noirmont-outil-bracelet-1.jpg?v=1785020482
  - `gid://shopify/MediaImage/59694408630610` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/outil-de-mise-a-taille-de-bracelet-02-situation.jpg?v=1785047375
  - `gid://shopify/MediaImage/59694408663378` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/outil-de-mise-a-taille-de-bracelet-03-macro.jpg?v=1785047375

#### outil-de-mise-a-taille-de-bracelet-v-black.jpg

- Fragment fournisseur exact : `14:193`
- Cibles : 1 variante(s)
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098047435090` | black | `NOIR-OUT-001` | ∅ | OK |

#### outil-de-mise-a-taille-de-bracelet-v-silver.jpg

- Fragment fournisseur exact : `14:350853`
- Cibles : 1 variante(s)
- Lot futur sûr : associer le nouveau média seulement aux GID ci-dessous, sans toucher aux médias existants ni au `featuredMedia`.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54098047467858` | Silver | `NOIR-OUT-002` | ∅ | OK |

### 20260810-0130-generate_images-p4-rouleau-noir-wb13.json

- Produit : `rouleau-de-voyage-noir-cuir` — `gid://shopify/Product/10980083171666` — statut live `ACTIVE`
- Portée : 1 média(s), 1 variante(s) cible(s) sur 3 variante(s) live
- Média principal à préserver : `gid://shopify/MediaImage/59691418714450` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/rouleau-cuir-noir_e0611be5-d26c-4e5e-92d6-2702bfc0c067.jpg?v=1785017873
- Mode sûr : `APPEND + ATTACH`, vérifier, puis `DETACH ASSOCIATION ONLY` si remplacement strict; zéro suppression de média
- Galerie live complète :
  - `gid://shopify/MediaImage/59691418714450` **[PRINCIPAL — PROTÉGÉ]** — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/rouleau-cuir-noir_e0611be5-d26c-4e5e-92d6-2702bfc0c067.jpg?v=1785017873
  - `gid://shopify/MediaImage/59694431437138` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/rouleau-de-voyage-noir-cuir-03-macro.jpg?v=1785047668
  - `gid://shopify/MediaImage/59893837824338` — https://cdn.shopify.com/s/files/1/1094/1893/8706/files/rouleau-de-voyage-noir-cuir-g1.jpg?v=1786231239

#### rouleau-de-voyage-noir-cuir-v-wb13.jpg

- Fragment fournisseur exact : `14:350686#WB13`
- Cibles : 1 variante(s)
- Lot futur sûr : associer le nouveau média seulement à la variante 3 montres, relecture live, puis détacher seulement l’association ancienne si nécessaire. Préserver l’ancien média produit et ses deux autres associations.

| Variant GID live | Titre live | SKU live | Ancien `media_id` associé | Contrôle snapshot |
|---|---|---|---|---|
| `gid://shopify/ProductVariant/54096787276114` | 3 montres | `NOIR-ROU-010` | `gid://shopify/MediaImage/59691418714450` | OK |

## Variantes hors lot à préserver

Les 9 variantes ci-dessous ne doivent apparaître dans aucun lot d’association P4. Les sept variantes d’étui n’ont pas d’association média ; les deux variantes rouleau 1 et 2 montres gardent le média principal partagé.

| Produit | Variant GID | Titre live | SKU live | Média associé live |
|---|---|---|---|---|
| `etui-de-voyage-rigide` | `gid://shopify/ProductVariant/54098044977490` | Black Brown 3 Slot | `NOIR-ETU-001` | ∅ |
| `etui-de-voyage-rigide` | `gid://shopify/ProductVariant/54098045010258` | Black Brown 2 Slot | `NOIR-ETU-002` | ∅ |
| `etui-de-voyage-rigide` | `gid://shopify/ProductVariant/54098045043026` | Purple 6 Slot | `NOIR-ETU-003` | ∅ |
| `etui-de-voyage-rigide` | `gid://shopify/ProductVariant/54098045075794` | Black Brown 6 Slot | `NOIR-ETU-004` | ∅ |
| `etui-de-voyage-rigide` | `gid://shopify/ProductVariant/54098045108562` | Black Brown 1 Slot | `NOIR-ETU-005` | ∅ |
| `etui-de-voyage-rigide` | `gid://shopify/ProductVariant/54098045174098` | Gray Orange 6 Slot | `NOIR-ETU-007` | ∅ |
| `etui-de-voyage-rigide` | `gid://shopify/ProductVariant/54098045206866` | Blue 6 Slot | `NOIR-ETU-008` | ∅ |
| `rouleau-de-voyage-noir-cuir` | `gid://shopify/ProductVariant/54096787210578` | 1 montre | `NOIR-ROU-008` | `gid://shopify/MediaImage/59691418714450` |
| `rouleau-de-voyage-noir-cuir` | `gid://shopify/ProductVariant/54096787243346` | 2 montres | `NOIR-ROU-009` | `gid://shopify/MediaImage/59691418714450` |

## Séquence future recommandée après QA

1. Relire produit, variantes, `featuredMedia` et associations juste avant mutation ; interrompre si un GID, titre ou ancien `media_id` diffère de ce relevé.
2. Ajouter les nouveaux médias à la fin de la galerie produit.
3. Réinterroger le produit et récupérer les nouveaux `media_id` Shopify créés.
4. Associer par produit avec `productVariantAppendMedia`, en utilisant strictement les groupes de GID ci-dessus. Ne pas mélanger deux produits dans le même appel.
5. Réinterroger chaque variante et vérifier que le nouveau `media_id` est présent, que le `featuredMedia` est inchangé et que les variantes hors lot sont inchangées.
6. Cas WB13 seulement : après réussite des étapes précédentes, si l’ancien média doit disparaître de la variante 3 montres, appeler `productVariantDetachMedia` uniquement pour la paire variante `gid://shopify/ProductVariant/54096787276114` / média `gid://shopify/MediaImage/59691418714450`. Ne pas supprimer ce média du produit.
7. Ne supprimer aucun des 21 médias existants dans cette vague. Toute suppression éventuelle exige un audit séparé des usages produit, variante et image principale.

## Limites et actions non effectuées

- La conformité visuelle des fichiers en cours de génération n’est pas couverte par ce préflight ; elle reste un gate séparé.
- L’affichage final storefront/mobile après association n’est pas prouvé ici.
- Aucune mutation Shopify, aucun upload, aucune association, aucun détachement, aucune suppression, aucun ordre Codex et aucune action DSers n’ont été exécutés.

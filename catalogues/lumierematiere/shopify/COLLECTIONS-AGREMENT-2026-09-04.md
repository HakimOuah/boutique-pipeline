# Agrément chambre / salon — 04/09/2026

Dernier item catalogue actionnable avant la review GMC. **Aucun import, aucun brouillon publié,
aucun délai touché.** Rattachement de fiches ACTIVE déjà live, donc déjà dans la fenêtre 7–18 j.

Accès : plugin Shopify (connecteur Claude). Le CLI Connector était en 401 et le token `.env`
reste `read_reports`. Note : `shopify theme list --store lumierematiere.fr` échoue — le CLI
concatène `.myshopify.com` et cherche `lumierematiere.fr.myshopify.com`. Le domaine permanent
est **`nzefxg-gg.myshopify.com`**.

## Ce qui a été fait

Les deux collections sont **manuelles** (`ruleSet: null`), tri `BEST_SELLING`.

| Collection | GID | Public avant | Ajouts | Public après |
|---|---|---:|---|---:|
| `lustres-chambre` | `652035653968` | 3 | **LM-130**, **LM-129** | **5** |
| `suspensions-salon` | `652035785040` | 4 | **LM-007** | **5** |

Admin passe de 10 → 12 et de 29 → 30 membres (le reste étant en brouillon).
La vitrine met ~30 s à propager : `products.json` reste en cache, relire avec un cache-buster.

## Justification par la règle de `COLLECTIONS-PIECE-2026-08-26.md`

**`lustres-chambre`** — *diamètre dominant ≤ 45 cm, lumière douce, aucune pièce d'apparat.*

- **LM-130** `suspension-verre-538307` — titre « chambre » ; description : « assez petit pour un
  chevet », « au-dessus d'une table de nuit, d'une console ».
- **LM-129** `suspension-verre-bois-910933` — abat-jour 19 cm, rosace 10 cm, même usage chevet.

Bénéfice secondaire : ce sont deux des trois testers verre compact (< 1,3 kg) que le sourcing du
02/09 a identifiés comme les seuls à tenir 6–15 j en Selection/Standard. On garnit avec ce qui est
le plus sûr sur le délai, pas avec ce qui est le plus limite.

**`suspensions-salon`** — *Ø ≥ 40 cm, ou pièce visiblement large, ou titre « salon ».*

- **LM-007** `suspension-bambou-655008` — titre « salon », variantes 30 / 38 / 45 cm (45 ≥ 40),
  et le principe posé le 26/08 : « un catalogue de fibres tressées **est** un catalogue de salon ».

Écartés volontairement : LM-108 (*Lustre salon sputnik*, tenable mais pièce d'apparat) et
LM-113, dont le doc du 26/08 prévoyait l'appartenance aux deux collections — restauration possible
plus tard, elle n'était pas nécessaire ici.

## État des collections du menu après opération

| Collection | Publics |
|---|---:|
| suspensions-cuisine | 19 |
| lustres-salon | 10 |
| suspensions-bois · plafonniers-led | 7 |
| suspensions-rotin · suspensions-metal | 6 |
| **lustres-chambre** · **suspensions-salon** · plafonniers-salon · suspensions-verre · suspensions-deco · lustres-anneau · appliques-murales | **5** |
| suspensions-pierre | 4 |
| suspensions-bambou | 3 |
| suspensions-osier | 2 |

Restent sous le seuil : **bambou (3), osier (2), pierre (4)**. Non remplissables — mur fournisseur
confirmé le 02/09 (dès ~4 kg : Heavy / Cainiao Premium, min 19 j, max 29–44 j, 0 offre ≤ 16 j sur
7 devis). Décision ouverte : les laisser courtes ou les sortir du menu comme `suspensions-xxl` et
`plafonniers-cuisine`.

## Non-régression vérifiée

52 ACTIVE publics · 161 variantes · **0 `compare_at_price`** · **161/161 SKU DSers intacts** ·
aucune fiche orpheline (les trois restent dans leurs collections matière).

## Décidé le 04/09 — ne pas rouvrir

Élargir la fenêtre à « 7–47 j » pour publier les 80 brouillons : **écarté**, confirmant la reco du
26/08. Le motif n'est pas que Google plafonnerait les délais — il ne le fait pas. C'est que le
« 7 » appartient aux 52 fiches live et le « 47 » aux brouillons : la fourchette serait fausse pour
**chaque fiche prise individuellement**, alors que 7–18 est vrai pour les 52, une par une.
S'y ajoutent l'art. L216-1 (résolution de la vente au-delà de 30 j) et le risque de litiges
« colis non reçu » pendant les 30 jours post-approbation, qui est la vraie fenêtre de suspension.

Si le catalogue doit rouvrir : **après** approbation et 30 j de stabilité, via des délais par
produit (profils d'expédition Shopify + transit par produit dans le flux), pas via une fenêtre
unique élargie.

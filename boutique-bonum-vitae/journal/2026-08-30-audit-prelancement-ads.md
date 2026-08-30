# 30/08/2026 — Audit avant lancement Google Shopping

Hakim s'apprête à lancer les ads. Dernier coup d'œil demandé. Audit CLI + live,
onze jours après la clôture du chantier boutique.

## Ce qui était sain (constaté, pas déclaratif)

- **0 `compareAtPrice`** sur les 28 produits. Aucun faux barré.
- **Aucun faux avis affiché.** Trustoo n'est plus qu'un web pixel (customer
  events), pas de widget. Vitals absente.
- **Claims exemplaires.** PDP et FAQ répondent « Non » à « les anti-calcaire
  adoucissent-ils l'eau ? » et disent l'absence de preuve scientifique.
- **18 produits sur Google & YouTube, tous en stock.** 0 indispo au feed.
- **Tracking Google Ads en place** : `AW-18325545481` + `GT-M34W44VB` via web
  pixel Shopify. Événements `view_item`, `search`, `begin_checkout` et
  **`purchase`** câblés sur le compte AW. Pas de GA4 (`G-`) — non bloquant.

## Corrigé dans cette passe

**Contradiction de délais entre policies** — le déclencheur misrepresentation
le plus classique, sur un compte GMC déjà approuvé. Les CGV et CGU étaient
restées sur l'ancien texte alors que la policy Expédition avait été réécrite
le 18/08.

| Document | Avant | Après |
|---|---|---|
| CGV art. 8 | « 8 à 13 jours ouvrés » | « 6 à 10 jours ouvrés », préparation 24–48 h incluse |
| CGV art. 8 | « France métropolitaine **et à l'international** » | « France métropolitaine uniquement » |
| CGU § Livraison | « entre 8 et 13 jours ouvrés » | « France métropolitaine sous 6 à 10 jours ouvrés » |
| CGV art. 7 | CB / Visa / MC / Amex / Maestro + Paypal | + Apple Pay, Google Pay, Shop Pay, **Klarna** |
| FAQ « délais » | « entrepôts européens… une petite semaine », « produits expédiés de plus loin » | France métro, 24–48 h, cutoff 15h Paris, **6 à 10 j**, franco |

Constaté live après écriture : 0 occurrence de « 8 à 13 » / « 8 et 13 » sur
`/policies/terms-of-sale`, `/policies/terms-of-service`,
`/policies/shipping-policy`, `/pages/faq`. Plus de mention d'international
sur la livraison (restent les mentions propriété intellectuelle / usages
interdits, normales).

**25 metafields d'avis résiduels purgés.** `vstar.product_rating` laissés par
Vitals sur 25 fiches — valeurs vides (`rating: 0`, `total_reviews: 0`), non
affichées, mais c'est la famille exacte qui a coûté la suspension de juin.
`metafieldsDelete`, 25/25, 0 userErrors.

Backups : `backups/2026-08-30-prelancement-ads/`.

## Le point non réglé : structure économique du feed

**Le feed n'envoie pas 18 items, il en envoie 84** — Google Shopping traite
chaque variante comme un item.

| Produit | Variantes | Fourchette |
|---|---|---|
| `pommeau-de-douche-filtrant-parfume` | **24** | 13,90 → 107,90 € |
| `elements-filtrants-de-robinet-anti-chlore-lot-alloet` | **12** | 8,90 → 21,90 € |
| `filtre-de-douche-parfume-anti-calcaire-corps-abs` | 10 | 18,90 → 46,90 € |
| `kit-purificateur-de-sortie-d-eau-filtre-robinet-universel` | 7 | 7,90 → 54,90 € |
| `filtre-de-douche-15-20-etapes` / `…finition-chrome` | 6 + 6 | 13,90 → 36,90 € |
| `bouilloire-filtrante-domestique-3-filtres` | 4 | 79,90 → 121,90 € |
| `aerateur-de-robinet-economie-d-eau` | 3 | **3,90** → 5,90 € |

**57 items sur 84 sont sous 30 € (67 %). Médiane du feed : 20,90 €.**

Grille du skill `shopping-scaling` : AOV < 50 $ = fragile, 60 $+ = scalable.
Un feed dont la médiane est à 20,90 € pousse l'AOV vers le bas, pas vers le
haut — et Shopping/PMAX privilégie ce qui clique et convertit le plus
facilement, donc le pas cher.

L'aérateur à **3,90 €** ne peut structurellement pas absorber un CPC français.
Ce n'est pas une exclusion « best seller » ou émotionnelle (interdite par le
skill) : c'est de la réparation d'économie unitaire, Phase 2 du framework, qui
vient **avant** le scaling.

À l'inverse, les deux plus gros paniers du catalogue sont **hors** feed :
`kit-entretien-osmoseur-600-gpd` (129 €, en attente de la commande test de
compatibilité — raison légitime) et `anti-tartre-galvanique-toute-la-maison`
(149 €, décision du 18/08). Le LPS mériterait d'entrer au feed.

**Non tranché par l'agent** : périmètre du feed, décision d'acquisition qui
appartient à Hakim.

## Feed restreint le 30/08 (demande Hakim)

Kit test OK + LPS OK → les deux **ajoutés** au canal Google. 10 fiches
low-ticket **retirées** du canal (restent en vitrine). Hors-acquisition
inchangés (hors Google).

**10 produits / 14 items Shopping**, plancher 66,90 €, plafond 449 €.

Appliqué via `publishablePublish` / `publishableUnpublish` sur
`Publication/357118574930`. Reliquats GMC : 24–48 h pour que les
anciens items disparaissent du Merchant Center.

## Signal GO (Hakim surveille GMC, 30/08)

Compte **`5825588636`**. Ne pas créer de compte, ne pas redemander de review.

**GO — lancer la PMAX** quand :
- le catalogue ≈ **14 items** (10 fiches), pas ~80–95 ;
- le **prix mini** affiché est **≥ 66,90 €** ;
- aérateur, pommeau, cartouches, kits 14,90 €, camping, filtres douche 15–20 €
  ont disparu (ou sont « Non soumis / Expiré », plus « Approuvé ») ;
- kit 129 € et LPS 149 € sont **Approuvés**.

**NO-GO** tant que des items < 30 € restent Approuvés en masse. Reliquats
24–48 h = normal. Si ça traîne au-delà : revérifier le canal Shopify
Google & YouTube, ne pas soumettre de review.

Campagne : 1 PMAX, France, conv. `purchase` (`AW-18325545481`), 30 €/j × 5 j.

## À vérifier avant le premier euro

- Le pommeau (24 variantes) est **hors** Google depuis le 30/08 — plus de
  risque « Google 13,90 € / landing autre prix » tant qu'il n'est pas
  republié sur le canal.
- Scope commandes absent du token CLI : **AOV réel non mesurable** par l'agent.

---
type: journal
boutique: bonum-vitae
date: 2026-08-18
nature: intervention
leviers: [autre]
titre: "18/08/2026 — Run autonome : tickets ouverts jusqu'à boutique prête"
---

# 18/08/2026 — Run autonome : tickets ouverts jusqu'à boutique prête

Hakim : prendre tous les tickets ouverts et les régler un par un, sans créer le GMC.

Store : `kw7vak-g0.myshopify.com`. Thème MAIN FullStack `205568147794`. Auth CLI
`contact@bonumvitae.fr`. Scopes : products, files, themes, content, pages,
legal_policies — **pas** `read_publications` / navigation / redirects.

## T-06 — Policies (P1) ✅

Constat : 6 pages CMS en 200 en plus des shop policies (`mentions-legales`,
livraison, remboursement, confidentialité, CGV, CGU). Footer listait les deux.

Fait :
- `pageUpdate isPublished: false` sur les 6. Constaté anonyme : **404**.
- `/policies/legal-notice` reste **200**.
- Footer : menu CMS « Politiques » désactivé (`menu_legal`) ; colonne Informations
  recâblée en liens durs (histoire / FAQ / contact / `/policies/shipping-policy`).
  `_footer-policy-list` sert les shop policies.
- Policy expédition réécrite (pas mot pour mot sœur) : plus de contradiction
  « 5 et 9 » vs « 6 à 10 ». Aligné FAQ / footer / PDP : **24–48 h** + **6 à 10 j**
  + cutoff **15h Paris** + franco France.
- Rétractation **14 jours** partout (footer, FAQ, refund, panier). Pas de 30 jours
  inventé.
- Raison sociale footer déjà OK (OH VENTURES / SIREN) — ETAT était périmé.

Pas de 301 CMS → policies : scope `urlRedirects` absent. Les 404 valent mieux
que deux 200. Hakim peut poser les 301 en admin (2 min).

## T-07 — Collections < 5 ✅

Public avant : `osmoseurs` = 3, `purificateurs-nomades` = 1. Pas de SKU inventé.

Fait : `collectionDelete` des deux. Produits conservés. Constaté : les deux URL
**404**. Le menu header a lâché tout seul les items morts. Restent publiques et
≥ 5 : douche, carafes, robinet, anti-calcaire. `frontpage` = système, hors nav.

Home : CTA osmoseur → `/products/osmoseur-ro-600g`. Carte nomades retirée.
Section `collection-featured` « Nos osmoseurs » **supprimée** (une collection
effacée faisait retomber le slider sur n'importe quel produit — misrep).

## Claims / handles ✅

- Hero « sans plombier » : déjà absent du FullStack live.
- Newsletter « -10 % » : déjà absent (le `-10` du HTML était du SVG).
- Handle `…eau-adoucie` → `pommeau-de-douche-filtrant-parfume` (`redirectNewHandle`).
- Handle `carafe-d-eau-alcaline-minerale-3-5-l-althy` →
  `carafe-filtrante-3-5-l-grande-capacite` (301 auto).
- 25 alts ALTHY / IPSE / « alcaline » nettoyés (`fileUpdate`, 0 `fileDelete`).

## T-H7 — hors acquisition (déjà tranché) ✅ partiel

Tag `hors-acquisition` posé, prix **non inventés** :
- magnétiques DN8 / DN20 / DN25
- carafe 3,5 L 129,90–173,90 €

Reste Hakim : grille douche vitamine C (111,90–149,90) ; activer LPS 149 € ;
sortir ces SKU du canal Google (scope publications absent ici).

## T-12 — Panier FullStack ✅

Progress bar démo (« Plus que 30 € ») retirée du drawer et de `/cart`.
Bannière « Livraison offerte en France — suivie, 6 à 10 jours ouvrés ».
Upsell consommables (max 2, hors déjà au panier) : kit 600 GPD, cartouches
robinet, aérateur, filtre douche parfumé. Ajout via `/cart/add.js` (pas de
`custom-code` dans `_product-form`). Accordéons `/cart` : 14 jours + franco
alignés policies.

## T-11 — QA live (technique) ✅ partiel

Constaté anonyme : SIREN, 0 doublon mentions, 0 « sans plombier », 0 « -10 % »,
0 faux 4,8/5 visible, délais alignés, panier propre, nav sans collections < 5.

**Trouvé et purgé** : metafields Vitals/reviews `4.83 / 6 avis` sur
`osmoseur-ro-600g` (et 4,67 / 6 sur le brouillon Shuangli). Injectés dans le
HTML (`vtlsLiquidData`). Supprimés ; re-constaté absents. Si l'app Vitals les
réécrit, la désactiver.

Pas de QA visuelle humaine 375 px (sticky ATC, icônes paiement vs checkout,
date `delivery-estimation`). Ça reste le passage Hakim.

## Images ✅ échantillon

Featured de 12+ SKUs hors kit/LPS : fonds blancs, **0 filigrane / texte
AliExpress / NSF-FDA** sur l'échantillon (robinet 360°, aérateur, anti-tartre
DN8, pommeau, carafe 3,5 L). Le reste du catalogue n'est pas passé image par
image — zoom corps avant génération si on refait des visuels.

## T-10 / T-H4 / T-H5

DA Abysse/Source déjà sur le live. Thème déjà publié par Hakim. Clos de facto.

## Toujours à Hakim (boutique max, pas GMC)

1. 301 admin : `/pages/mentions-legales` (et 5 sœurs) → `/policies/…` ;
   `/collections/osmoseurs` et `/collections/purificateurs-nomades` →
   `/products/osmoseur-ro-600g` et le filtre randonnée.
2. Vitals : vérifier qu'il ne réinjecte pas de notes.
3. T-H7 restant + LPS + canal Google des `hors-acquisition`.
4. QA mobile 375 px (yeux).
5. Feu vert **puis seulement** création GMC.

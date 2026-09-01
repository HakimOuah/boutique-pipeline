---
type: journal
boutique: seiko-mod
date: 2026-09-01
nature: audit
leviers: [conformite]
titre: "Audit de contrôle post-ban — surface publique, 01/09/2026"
---

# Audit de contrôle post-ban — 01/09/2026

Re-vérification de la surface **publique** de `maisonnoirmont.fr` neuf jours après le ban GMC
« déclarations trompeuses » du 23/08, après les passes du 23, 30 et 31/08.
Méthode : `gmc-acceptance` §6 + `audit-lecons-noirmont.md`. Sources : HTML rendu de 14 URL,
`products.json` (96 actives), `products.json` de 16 collections, `/payments/config`, `sitemap.xml`,
statuts HTTP, navigateur pour le bandeau cookies.

**Connecteur Shopify Admin déconnecté** : brouillons et archivées non re-vérifiés (compareAtPrice,
reliquats de marque). Statut du compte GMC 5840460291 non consulté.

## Conforme

| Point | Constat |
|---|---|
| Marques tierces | 0 Seiko / Miyota / Mingzhu / Présidentiel / 904L / SKX sur 96 fiches, pages, policies, alts, tags, noms de fichiers CDN |
| « Qualité Premium » / verified | 0 sur home, PDP, collections |
| JSON-LD `Organization` | parse strict OK, `legalName` OH Ventures, adresse + e-mail pro + tél |
| JSON-LD PDP | `ProductGroup`, **0** `aggregateRating`, **0** `review` |
| E-mail public | `contact@maisonnoirmont.fr` seul — 0 Gmail |
| Téléphone | une seule graphie `+33 7 56 82 80 94`, `tel:+33756828094` |
| Footer | marque + OH Ventures + 47 rue Vivienne + SIRET + `mailto:` + `tel:` + horaires + mention TTC |
| Paiement | pictos auto (`aria-labelledby="pi-*"`, 0 icône manuelle) ; Google Pay absent des deux côtés ; `applePay` / `shopifyPay` / `paypal` présents dans `/payments/config` ; `currency: EUR` |
| Prix barrés | 0 `compare_at_price` sur les 96 actives |
| Images | 0 `alicdn`, 0 fichier CDN partagé entre deux fiches, `vendor` = Maison Noirmont sur 96/96 |
| Redirections | 3 handles « président » → **301** |
| Policies | une seule mentions légales · CM2C **avec URL** · 0 `assistance@shopify.com` · dates toutes au 15/08/2026 · adresse de retour réelle · garantie 12 mois mouvement identique footer / policy / CGV art. 10 |
| Menu header | « À propos » + « Suivre mon colis » posés — le reliquat du 23/08 est fait |
| Cookies | bandeau à la 1re visite, Accepter et Refuser de même taille, aucun tracker tiers dans le HTML |
| Collections vides | `cadran-arabe`, `cadran-pilote-nh35`, `mouvement-nh35` dépubliées → 404, hors sitemap |

## À corriger

### P0 — « Jubilé » : la purge du 23/08 a été faite mot par mot, pas par nomenclature

**19 fiches** portent « Jubilé ». C'est le troisième nom de bracelet Rolex de la série —
`Président` a été purgé le 23/08 comme **cause du ban**, `Jubilé` est resté.

| Surface | Détail |
|---|---|
| Titres + handles | `bracelet-jubile-acier-20mm`, `bracelet-jubile-embouts-courbes`, `trente-six-classique-jubile`, `trente-six-{bleu,rose,rouge,dore,or-integral}-classique-jubile` |
| SEO title | ex. « Trente-Six Bleu : Montre automatique 36/39 mm, jubilé acier » |
| Descriptions | 8 fiches `trente-neuf-*-classique-cannelee` (« bracelet jubilé à cinq rangs ») |
| Variantes | `bracelet-maillons-arrondis-dore` (Jubilé · or rose, Jubilé · acier & or), `bracelet-maillons-arrondis-acier` (Jubilé) |
| Fichiers CDN | `noirmont-jubile-acier-1.jpg`, `bracelet-jubile-or-rose.jpg`, `bracelet-jubile-acier-or.jpg`, `bracelet-maillons-arrondis-acier-v-jubile.jpg`, … |

Renommage des handles → **301 obligatoires**.

### P1 — FAQ : deux délais de livraison

`/pages/faq` : « Comptez généralement **2 à 3 semaines** » alors que thème, panier, footer, policies
et suivi de colis disent « **14 à 21 jours calendaires** ». C'est le flag OneClickBrand du 23/08 :
le thème avait été harmonisé, **la page FAQ non**.

### P2 — Vocabulaire fournisseur dans les variantes publiques

`bracelet-jubile-embouts-courbes` : 15 variantes `steel-no logo`, `gold-no logo`,
`steel gold-no logo`. Options AliExpress brutes, visibles dans le feed et sur la fiche.

### P2 — `/collections/frontpage` publiée avec 1 produit

200, présente dans `sitemap_collections_1.xml`, 1 produit dans `products.json`.

### P3 — 404 sur un handle renommé le 31/08

`/products/mouvement-miyota-8215-nh34-gmt` → **404** (renommé en `mouvement-calibre-8215-nh34-gmt`
sans 301). Fiche brouillon, donc URL jamais publique — mais la règle est le 301 systématique.

### P3 — Trois cosmétiques

- SIRET : `10315725100010` (Coordonnées) vs `103 157 251 00010` (footer, mentions légales)
- TVA : `FR55103157251` vs `FR55 103157251`
- Délai SAV : « 48h », « 48 h », « 48 heures » — même valeur, trois graphies

## Examen GMC

Ne pas demander l'examen tant que le P0 et le P1 tiennent. Une fois la passe faite, le compteur
7–10 jours repart de cette date : **fenêtre décalée au 9–12 septembre**. Toujours 0 ads.

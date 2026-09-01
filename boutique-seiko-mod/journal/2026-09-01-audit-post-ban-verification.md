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

---

# Seconde passe — Admin Shopify + Chrome (01/09, après reconnexion)

Connecteur Shopify Admin rebranché : les 221 fiches (96 actives, 115 brouillons, 10 archivées)
ont été scannées, pas seulement le catalogue public.

## Ce que l'accès Admin confirme

| Contrôle | Résultat sur les 221 fiches |
|---|---|
| `compareAtPriceRange` | **null sur 221/221** — 0 prix barré, brouillons et archivées comprises |
| Seiko / Miyota / Mingzhu / Président / 904L / SKX | **0** |
| Rolex / Oyster / Datejust / Submariner / Daytona / GMT-Master | **0** |
| Omega / Speedmaster / Seamaster / Tudor / Black Bay | **0** |
| Cartier / Panerai / IWC / Royal Oak / Nautilus / Patek | **0** |
| « homage » / « replica » / « clone » | **0** |
| Fichiers CDN nommés `president`, `seiko`, `miyota`, `skx` | **0** (les 3 hits `904` sont des fragments d'UUID) |

La purge des trois passes tient donc **sur tout le catalogue**, pas seulement sur le public.

## Ce que l'accès Admin ajoute

### P0 — « Ships From : China Mainland » sur une fiche **active**

`doigtiers-d-horloger-latex` (ACTIVE, 12,90 €) publie deux options fournisseur brutes :

```
Color : white 100pcs · black 30pcs · white 30pcs · white 50pcs · black 50pcs · black 100pcs
Ships From : China Mainland
```

Vérifié rendu sur la PDP live. Sur une boutique bannie pour **déclarations trompeuses**, qui
annonce « Livraison offerte en France métropolitaine » en bandeau, une option publique qui déclare
l'expédition depuis la Chine est la contradiction la plus lisible du site.

### P0 — Noms d'options fournisseur en anglais sur **13 fiches actives**

`Band Color` / `Band Width` : `bracelet-jubile-embouts-courbes`, `bracelet-jubile-acier-20mm`,
`bracelet-acier-massif-12-22-mm`, `bracelet-caoutchouc-gaufre`, `bracelet-milanais-maille-italienne`,
`bracelet-cuir-daim-degagement-rapide`.
`Color` : `coussins-de-presentation-lot-de-10`, `etui-de-voyage-rigide`,
`coffret-6-montres-couvercle-verre`, `kit-d-entretien-13-pieces`,
`outil-de-mise-a-taille-de-bracelet`, `loupe-d-horloger`, `doigtiers-d-horloger-latex`.

Valeurs de la même veine : `steel-no logo`, `1.0mm-rose gold`, `white 100pcs`. Les 83 autres fiches
actives ont des options en français (`Cadran`, `Mouvement & fond`, `Capacité`…) — l'écart se voit.

### Jubilé — chiffres définitifs

**20 fiches** (19 actives + le brouillon `boitier-plongee-40-200m-jubile`) et **20 fichiers CDN**
dont le nom contient `jubile`. Confirme et complète le P0 de la première passe.

### À arbitrer — « Explorateur »

`montre-acier-chiffres-3-6-9-explorateur` (ACTIVE) : titre **« Explorateur : Sport chic à
chiffres 3-6-9 »**, SEO title identique. Cadran 3-6-9 = signature de l'Explorer. Contrairement à
« Jubilé » et « Président », « explorateur » est un mot français courant et non le nom commercial
employé par la marque — d'où l'arbitrage plutôt que la purge automatique.

### Brouillons — à traiter avant toute publication

- `Dial Diameter : NO LOGO` sur 8 fiches (option mal nommée **et** vocabulaire fournisseur)
- `Ships From : China Mainland` sur 4 brouillons / archivées de plus
- `solid-cyclop` / `glass-cyclop` dans les options de `boitier-plongee-40-200m-jubile` et
  `boitier-argent-40-saphir-120-clics` — « Cyclops » est le terme Rolex du verre loupe de date
- Handle `aiguilles-vintage-sub-nh35` (« sub » = Submariner)

## GMC — pas d'accès depuis ce Chrome

`merchants.google.com/mc/overview?a=5840460291` → **« votre compte Google n'a pas accès à ce compte
Merchant Center »**. Les trois comptes de la session Chrome ont été testés :

| Compte | Merchant Center visibles |
|---|---|
| `ouahabi.hakim@gmail.com` (authuser=0) | Gourde and Go **5564946079** · Hakim Ouahabi **515754956** (bonumvitae.fr) |
| `hakim.ouahabi4@gmail.com` (authuser=1) | aucun |
| `vpnpascher@gmail.com` (authuser=2) | aucun |

Le GMC **5840460291** de Noirmont n'est sous aucun des trois. Il faut le compte Google qui le
détient (probablement celui rattaché à `contact.noirmont@gmail.com`, cf. la fuite JSON-LD du 15/08)
pour relire le diagnostic. Le statut réel du ban reste donc non vérifié.

Aperçu au passage sur le compte 0 : **Gourde and Go** — 0 produit, 0 approuvé, 0 refusé,
« informations sur la qualité du magasin non disponibles », campagnes Ads en pause.

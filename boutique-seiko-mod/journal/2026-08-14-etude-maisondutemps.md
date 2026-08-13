# `maisondutemps.com` — étude complète du concurrent modèle — T-42

> **14/08/2026.** Approfondissement du §3.1 de [`2026-08-14-concurrents-fr.md`](2026-08-14-concurrents-fr.md),
> qui avait identifié ce site comme « Maison Noirmont avec deux ans d'avance » sans l'ouvrir.
> **Sources : catalogue Shopify public** (`/collections.json`, `/products.json`, `/sitemap*.xml`, 4 pages HTML lues en texte),
> **et SEMrush France du 12/08/2026** — *Classements organiques*, *Pages principales*, *Recherche publicitaire*.
> **Les 154 collections sont classées, aucune n'est laissée de côté. Le trafic est réparti URL par URL.**
>
> **Aucune écriture sur Shopify. Aucun achat. Aucun texte du concurrent n'est repris** — on relève des
> structures, des handles et des mots-clés.
>
> ⚠️ **Ce document corrige le §3.1 du dossier du 14/08 sur son point principal.** Le tableau d'axes qu'il
> proposait de copier (diamètre, étanchéité, couleur de cadran, disponibilité) **ne porte pas de trafic** :
> ces quatre axes réunis pèsent **165 visites sur 30 600**, soit **0,5 %**. La recommandation
> « 40 collections gratuites » aurait produit 40 pages mortes.

---

## 0. Le verdict en dix lignes

1. **Ce n'est pas une boutique à longue traîne, c'est une boutique à quatre pages.** Home 10 700 +
   `montres-homme` 5 100 + `montres-skeleton-homme` 4 500 + `montres-automatiques-homme` 1 500 =
   **21 800 sur 30 600, soit 71 %**. Les 150 autres collections se partagent 4 000 visites.
2. **35 % du trafic est de la marque.** « maison du temps » et ses variantes valent ≈ 10 500 visites,
   presque toutes sur la home. **Le trafic générique réel est de l'ordre de 20 000**, pas 30 600.
3. **La seule découpe qui a vraiment payé est `squelette`** : 4 500 visites sur une page, 23 requêtes
   de la grappe, **toutes servies par une URL unique**. C'est 15 % du site pour 44 produits.
4. **Le catalogue n'est pas le levier : la page l'est.** Ils ont **13 modèles de montre** déclinés en
   118 fiches (une fiche par coloris, **jamais de variante**). Le catalogue réel est petit.
5. **112 des 154 collections sont orphelines** — absentes du menu et de la page « toutes nos
   collections », atteignables uniquement par le sitemap. Et **certaines orphelines rapportent**
   (`montre-argent-homme` 648, `montre-homme-petit-poignet` 520, `bracelet-montre-acier` 442).
   Une collection SEO n'a pas besoin d'être dans le menu ; elle a besoin d'un `<title>`, d'une
   meta-description et d'un H1 propres.
6. **Deux qualités de collection cohabitent, et une seule marche.** Celles qui ont un H1 et une
   meta-description propres rapportent ; **celles qui n'ont qu'un `<title>` rapportent zéro**, même
   quand le mot-clé est bon. `montre-squelette-automatique-homme` (coquille, 53 produits) fait **0**
   à côté de `montres-skeleton-homme` (page réelle, 44 produits) qui fait **4 500**.
7. **Les axes « spec » sont morts, les axes « humains » vivent.** Diamètre en mm = 66 · étanchéité en
   ATM = 94 · couleur de cadran isolée = 5 · disponibilité stock/précommande = **0**.
   Contre : **couleur de la montre 1 943** · **forme du boîtier 776** · **taille de poignet 767** ·
   **épaisseur 207**. Le client ne tape pas « 42 mm », il tape « petit poignet » et « montre fine ».
8. **Un axe que personne n'avait vu : `montre à aiguille`, 423 visites, 42 mots-clés.** C'est la
   montre analogique par opposition à la connectée. La collection contient 148 produits sur 162 —
   c'est-à-dire **tout le catalogue**. Coût de création : zéro.
9. **Ils ne font pas de Google Ads.** 4 mots-clés payants relevés le 12/08, et le rapport publicitaire
   ne renvoie plus rien aujourd'hui. **30 600 visites gagnées à l'organique pur**, sur un ticket
   155-385 €. C'est le contre-exemple exact du modèle Kraken payant.
10. **Ce qu'on peut prendre sans sourcer une seule référence : 8 collections pour ≈ 2 700 visites/mois
    de potentiel adressable**, toutes servies par les 63 montres et 42 accessoires déjà au catalogue.
    Liste priorisée au §7.

---

## 1. Sa logique de découpe, en une phrase

**Une page = un mot-clé ; le contenu de la page est secondaire.**

La preuve est dans les nombres de produits. Sur les 154 collections, une bonne moitié contient
**presque tout le catalogue** : `montre-aiguille` 148 produits, `montres` 151, `montre-moderne-homme`
139, `montre-sport-chic-homme` 139, `montres-homme` 136, `montre-argent-homme` 132,
`montre-homme-acier` 132, `montre-verre-saphir` 130, `montre-a-mouvement-japonais` 119,
`montre-design` 110, `montre-automatique-pas-cher` 99, `montre-mecanique` 99,
`montre-homme-sans-pile` 98, `montres-10-atm` 96, `grosse-montre-homme` 91.

Ce ne sont **pas des segmentations** : ce sont des **portes d'entrée nommées sur le même stock**. La
collection ne trie pas, elle **nomme**. Le tri réel (13 lignes de modèles) est fait ailleurs, dans le
menu « COLLECTIONS ».

Le moteur technique est un **système de tags à préfixes**, 89 tags pour 162 produits, qui permet de
créer une collection automatique en trente secondes :

| Préfixe | Sert à | Exemples relevés |
|---|---|---|
| `CO_` | ligne de modèle maison | `CO_BETA` (41), `CO_ZETA` (17), `CO_GAMMA` (14), `CO_EPSILON` (10), `CO_OMICRON` (9), `CO_PHI` (6), `CO_DELTA` (6), `CO_SIGMA` (4), `CO_IOTA` (3), `CO_AUREA`, `CO_ERIS`, `CO_MU`, `CO_GAMMAFEMME` |
| `CA_` | complication / caractère du cadran | `CA_AUTOMATIQUE` (81), `CA_SKELETON` (44), `CA_CHRONOGRAPHE` (12), `CA_ARABIC` (9) |
| `BR_` | couleur du bracelet | `BR_NOIR`, `BR_BLEU`, `BR_MARRON`, `BR_BLANC`, `BR_ROUGE`, `BR_VERT`, `BR_ROSE`, `BR_TURQUOISE`, `BR_KAKI`, `BR_ORANGE`, `BR_MAILLE` |
| `ACIER_` | nuance et finition du boîtier | `ACIER_309L` (30), `ACIER_316L` (21), `ACIER_NOIR`, `ACIER_DORE`, `ACIER_ET_DORE` |
| `BRACELET_` | entrecorne | `BRACELET_14` (16), `BRACELET_20` (9) |
| nus | diamètre, étanchéité, verre, genre, statut | `42` (51), `40` (31), `38` (14), `41`, `34`, `26` · `10ATM` (78), `5ATM` (33), `3ATM` · `SAPHIR` (102), `MINERAL` (10) · `HOMME` (109), `FEMME` (12), `UNISEXE` (21) · `PRÉCOMMANDE` (14), `EN_LIGNE` (158) |

⚠️ **Le tag `SEIKO` est présent sur 12 produits** — vraisemblablement pour tracer le mouvement.
Chez nous ce serait un défaut de flux Merchant Center s'il ressortait. À ne pas imiter tel quel.

### La hiérarchie réelle : 42 navigables, 112 orphelines

| Niveau | Nombre | Ce que c'est |
|---|---:|---|
| **Menu + page « toutes nos collections »** | **42** | La vraie arborescence commerciale : 11 sous-entrées MONTRES HOMME, 6 MONTRES FEMME, 13 lignes de modèles, 5 ACCESSOIRES, plus les chapeaux |
| **Orphelines (sitemap seul)** | **112** | Pages d'atterrissage SEO. Aucun lien interne. **Elles pèsent tout de même ≈ 3 900 visites**, soit 13 % du site |

**Enseignement direct** : une collection SEO **n'a pas besoin d'être dans le menu**. On peut en créer
autant qu'on veut sans alourdir la navigation ni diluer le maillage — le sitemap suffit à les faire
indexer. C'est le meilleur point de méthode de tout le dossier.

---

## 2. L'arborescence complète — 154 collections, classées par critère de découpe

**Colonne « Trafic »** : trafic organique estimé SEMrush France, rapport *Pages principales* du
12/08/2026. `0` signifie que l'URL n'apparaît pas dans les 239 pages organiques relevées, donc
**moins de 3 visites/mois**. Les 154 collections totalisent **18 944** ; le reste des 30 600 se
répartit en home 10 700, fiches produit ≈ 400, pages ≈ 220, blog ≈ 253, versions `/en/ /it/ /de/` ≈ 25.

**Colonne « Navigable »** : `✅ menu` = liée depuis la home ou `/pages/toutes-nos-collections` ·
`👻 orpheline` = uniquement dans le sitemap.

### A. Genre / catalogue (chapeau) — **5305 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montres-homme` | Montres Homme | 136 | **5100** | ✅ menu |
| `montres-femme` | Montres Femme | 12 | 172 | ✅ menu |
| `montre-design` | Montre Design | 110 | 18 | 👻 orpheline |
| `montre-moderne-homme` | Montre Moderne Homme | 139 | 9 | 👻 orpheline |
| `montre-moderne-femme` | Montre Moderne Femme | 13 | 6 | 👻 orpheline |
| `montres` | Montres | 151 | 0 | 👻 orpheline |
| `montres-best-sellers` | Best-Sellers | 37 | 0 | ✅ menu |
| `toutes-les-collections` | TOUTES LES COLLECTIONS | 151 | 0 | ✅ menu |
| `nouveautes-montres-homme-et-femme-maisondutemps` | Nouveautés | 30 | 0 | 👻 orpheline |

### B. Type de montre / de mouvement — **7162 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montres-skeleton-homme` | Montres skeleton | 44 | **4500** | ✅ menu |
| `montres-automatiques-homme` | Montres automatiques | 86 | **1500** | ✅ menu |
| `montre-aiguille` | Montre Aiguille | 148 | **423** | 👻 orpheline |
| `montres-quartz-homme` | Montre à Quartz | 34 | **385** | ✅ menu |
| `montre-automatique-francaise` | Montre automatique française | 99 | 196 | 👻 orpheline |
| `montres-chronographe-homme` | Montres chronographes | 12 | 67 | ✅ menu |
| `montre-verre-saphir` | Montre Verre Saphir | 130 | 40 | 👻 orpheline |
| `montre-a-mouvement-japonais` | Montre à Mouvement Japonais | 119 | 31 | 👻 orpheline |
| `montre-sport-automatique` | Montre sport automatique | 99 | 10 | 👻 orpheline |
| `montre-homme-sans-pile` | Montre homme sans pile | 98 | 10 | 👻 orpheline |
| `montre-squelette-automatique-homme` | Montre Squelette Automatique Homme - SEO | 53 | 0 | 👻 orpheline |
| `montre-squelette-bracelet-acier` | Montre Squelette Bracelet Acier | 48 | 0 | 👻 orpheline |
| `montre-squelette-bracelet-noir-homme` | Montre Squelette Bracelet Noir Homme | 5 | 0 | 👻 orpheline |
| `montre-squelette-cadran-noir-homme` | Montre Squelette Cadran Noir Homme | 1 | 0 | 👻 orpheline |
| `montre-mecanique` | Montre mécanique | 99 | 0 | 👻 orpheline |
| `montre-quartz-femme` | Montre Quartz Femme - SEO | 11 | 0 | 👻 orpheline |
| `montre-chronographe-quartz` | Montre Chronographe Quartz | 12 | 0 | 👻 orpheline |
| `montres-coeur-ouvert-homme` | Montres Coeur Ouvert | 8 | 0 | ✅ menu |
| `montre-automatique-coeur-ouvert` | Montre automatique coeur ouvert | 8 | 0 | ✅ menu |
| `montres-phase-de-lune` | Montres Phase de Lune | 6 | 0 | ✅ menu |
| `montre-quartz-phase-de-lune` | Montre Quartz Phase de Lune | 6 | 0 | 👻 orpheline |
| `montres-day-date` | Montre Day-Date | 7 | 0 | ✅ menu |
| `montres-de-plongee-homme` | Montre plongée | 4 | 0 | ✅ menu |
| `montre-plongee-abordable` | Montre plongée abordable | 5 | 0 | 👻 orpheline |
| `montre-plongee-automatique` | Montre plongée automatique | 5 | 0 | 👻 orpheline |
| `montres-aviateur-homme` | Montre Aviateur | 3 | 0 | 👻 orpheline |

### C. Cadran à chiffres arabes — **662 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montres-arabic-dial-homme` | Montres Arabic Dial | 10 | **593** | ✅ menu |
| `montre-chiffre-arabe` | Montre Chiffre Arabe | 9 | 69 | 👻 orpheline |
| `montre-arabic-dial-cadran-noir` | Montre Arabic Dial Cadran Noir | 2 | 0 | 👻 orpheline |

### D. Couleur de la montre — **1943 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montre-argent-homme` | Montre Argent Homme | 132 | **648** | 👻 orpheline |
| `montre-rose-maisondutemps` | Montre Rose - MaisonDuTemps | 10 | **367** | 👻 orpheline |
| `montre-homme-noir` | Montre homme noir | 23 | **261** | 👻 orpheline |
| `montre-argent` | Montre Argent | 61 | **230** | 👻 orpheline |
| `montre-rose-homme` | Montre rose homme | 4 | 106 | 👻 orpheline |
| `montre-blanche-homme` | Montre Blanche Homme | 18 | 72 | 👻 orpheline |
| `montre-homme-bleu` | Montre Homme Bleu | 12 | 61 | 👻 orpheline |
| `montre-acier-noir-homme` | Montre acier noir homme | 25 | 55 | 👻 orpheline |
| `montre-homme-rouge` | Montre Homme Rouge | 18 | 49 | 👻 orpheline |
| `montre-homme-orange` | Montre Homme Orange | 1 | 29 | 👻 orpheline |
| `montre-homme-or-et-noir` | Montre homme or et noir | 2 | 28 | 👻 orpheline |
| `montre-homme-verte` | Montre Homme Verte | 8 | 14 | 👻 orpheline |
| `montre-turquoise` | Montre turquoise | 4 | 10 | 👻 orpheline |
| `montre-or-homme` | Montre Or Homme | 2 | 9 | 👻 orpheline |
| `montres-dores` | Montres Dorées | 5 | 4 | ✅ menu |
| `montre-noir-femme` | montre noir femme - SEO | 1 | 0 | 👻 orpheline |
| `montre-noire-femme` | Montre noir Femme - SEO | 1 | 0 | 👻 orpheline |
| `montre-blanche-femme` | Montre Blanche Femme | 3 | 0 | ✅ menu |
| `montre-kaki-homme` | Montre kaki homme | 2 | 0 | 👻 orpheline |
| `montre-femme-bicolore` | Montre Femme Bicolore | 2 | 0 | ✅ menu |
| `montre-femme-rose` | Montre Femme Rose | 2 | 0 | ✅ menu |

### E. Forme du boîtier — **776 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montre-cadran-carre-homme` | Montre carrée | 9 | **461** | ✅ menu |
| `montre-octogonale` | Montre Octogonale | 73 | **222** | 👻 orpheline |
| `montre-carre-femme-argent` | Montre Carré Femme Argent | 1 | 58 | 👻 orpheline |
| `montre-carre-dore` | Montre Carré Doré | 3 | 25 | 👻 orpheline |
| `montre-rectangulaire-homme` | Montre Rectangulaire Homme | 6 | 10 | 👻 orpheline |
| `montre-carre-automatique` | Montre Carré Automatique | 3 | 0 | 👻 orpheline |
| `montre-carre` | Montre Carré Femme | 4 | 0 | ✅ menu |
| `montre-rectangulaire-femme` | Montre Rectangulaire Femme | 7 | 0 | 👻 orpheline |
| `montre-tonneau` | Montre Tonneau | 6 | 0 | ✅ menu |

### F. Taille de poignet (morphologie) — **767 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montre-homme-petit-poignet` | Montre homme petit poignet | 53 | **520** | 👻 orpheline |
| `montre-femme-pour-petit-poignet` | Montre Femme Pour Petit Poignet | 13 | **209** | 👻 orpheline |
| `grosse-montre-homme` | Grosse Montre Homme | 91 | 38 | 👻 orpheline |
| `petite-montre-femme` | Petite Montre Femme | 13 | 0 | 👻 orpheline |

### G. Diamètre en mm — **66 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montre-38mm-homme` | Montre 38mm homme | 14 | 58 | 👻 orpheline |
| `montre-40mm-homme` | Montre 40mm Homme | 30 | 8 | 👻 orpheline |
| `montre-42mm` | Montre 42mm | 72 | 0 | 👻 orpheline |
| `montre-42mm-homme` | Montre 42mm Homme | 72 | 0 | 👻 orpheline |

### H. Étanchéité en ATM — **94 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montres-10-atm` | Montres 10 Atm | 96 | 72 | 👻 orpheline |
| `montre-5-atm` | Montre 5ATM | 45 | 18 | 👻 orpheline |
| `montre-3-atm` | Montre 3 Atm | 3 | 4 | 👻 orpheline |
| `montre-etanche-10-atm` | Montre Étanche 10 ATM | 96 | 0 | 👻 orpheline |
| `montre-etanche-3-atm` | Montre Étanche 3 ATM | 3 | 0 | 👻 orpheline |

### I. Couleur de cadran (isolée) — **5 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montre-cadran-vert` | Montre cadran vert | 8 | 5 | 👻 orpheline |
| `montre-automatique-cadran-noir` | Montre Automatique Cadran Noir | 18 | 0 | 👻 orpheline |
| `montre-automatique-cadran-bleu` | Montre Automatique Cadran Bleu | 6 | 0 | 👻 orpheline |
| `montre-cadran-meteorite` | Montre Cadran Météorite | 1 | 0 | 👻 orpheline |
| `montre-quartz-cadran-noir` | Montre Quartz Cadran Noir | 6 | 0 | 👻 orpheline |

### J. Bracelet de la montre (matière / couleur) — **283 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montre-homme-bracelet-silicone` | Montre Homme Bracelet Silicone | 59 | **268** | 👻 orpheline |
| `montre-cuir-homme` | Montre Cuir Homme | 4 | 8 | 👻 orpheline |
| `montre-bracelet-marron-homme` | Montre Bracelet Marron Homme | 7 | 7 | 👻 orpheline |
| `montre-bracelet-silicone-cadran-blanc` | Montre Bracelet Silicone Cadran Blanc | 9 | 0 | 👻 orpheline |
| `montre-cuir` | Montre Cuir | 6 | 0 | 👻 orpheline |
| `montres-bracelet-cuir-homme` | Montre bracelet cuir | 9 | 0 | ✅ menu |
| `montre-bracelet-cuir-cadran-bleu` | Montre Bracelet Cuir Cadran Bleu | 1 | 0 | 👻 orpheline |
| `montre-bracelet-cuir-cadran-bleu-homme` | Montre Bracelet Cuir Cadran Bleu Homme | 1 | 0 | 👻 orpheline |
| `montre-bracelet-cuir-noir` | Montre Bracelet Cuir Noir Homme | 0 | 0 | 👻 orpheline |
| `montre-bracelet-caoutchouc-homme` | Montre Bracelet Caoutchouc Homme | 5 | 0 | 👻 orpheline |
| `montre-bracelet-acier-noir-homme` | Montre Bracelet Acier Noir Homme | 18 | 0 | 👻 orpheline |
| `montre-automatique-bracelet-noir` | Montre Automatique Bracelet Noir | 15 | 0 | 👻 orpheline |
| `montre-automatique-bracelet-bleu` | Montre Automatique Bracelet Bleu | 8 | 0 | 👻 orpheline |
| `montre-automatique-bracelet-bleu-homme` | Montre Automatique Bracelet Bleu Homme | 8 | 0 | 👻 orpheline |
| `montre-quartz-bracelet-noir` | Montre Quartz Bracelet Noir | 4 | 0 | 👻 orpheline |
| `montre-homme-acier` | Montre Homme Acier | 132 | 0 | 👻 orpheline |
| `montre-femme-acier` | Montre Femme Acier | 9 | 0 | 👻 orpheline |
| `montres-femme-acier` | Montres femme acier | 9 | 0 | 👻 orpheline |
| `montre-femme-quartz` | Montre Femme Quartz | 12 | 0 | ✅ menu |

### K. Épaisseur — **207 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montre-homme-plate` | Montre Homme Plate | 48 | **207** | 👻 orpheline |

### L. Prix / promotion — **554 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montre-automatique-pas-cher` | Montre automatique pas cher | 99 | **398** | 👻 orpheline |
| `promotions` | PROMOTIONS | 9 | 119 | 👻 orpheline |
| `montre-femme-tendance-pas-cher` | Montre Femme Tendance Pas Cher | 13 | 37 | 👻 orpheline |

### M. Occasion / registre — **140 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montre-mariage-homme` | Montre Mariage Homme | 48 | 72 | 👻 orpheline |
| `montre-chic-homme` | Montre chic homme | 49 | 48 | 👻 orpheline |
| `montre-habillee-homme` | Montre habillée homme | 48 | 20 | 👻 orpheline |
| `montre-classique-homme` | Montre classique homme | 49 | 0 | 👻 orpheline |
| `montre-elegante-homme` | Montre élégante homme | 48 | 0 | 👻 orpheline |
| `montre-sport-chic-homme` | Montre Sport Chic Homme | 139 | 0 | 👻 orpheline |
| `montre-vintage` | Montre Vintage | 6 | 0 | 👻 orpheline |

### N. Disponibilité — **0 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `montres-en-stock` | Montres En Stock | 105 | 0 | 👻 orpheline |
| `montres-en-precommande` | Montres en précommande | 46 | 0 | 👻 orpheline |

### O. Opérations commerciales (datées) — **0 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `solde-dete` | SOLDE D'ÉTÉ | 151 | 0 | 👻 orpheline |
| `solde-dhiver` | SOLDES D'HIVER | 151 | 0 | 👻 orpheline |
| `solde-ete-montres-maisondutemps` | SOLDE D'ÉTÉ | 151 | 0 | 👻 orpheline |
| `frenchdays` | FRENCHDAYS MaisonDuTemps | 151 | 0 | 👻 orpheline |
| `fete-des-peres` | FÊTE DES PÈRES | 139 | 0 | 👻 orpheline |
| `black-friday-2025` | BLACK FRIDAY 2025 | 9 | 0 | 👻 orpheline |

### P. Nom de collection maison — **220 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `beta-automatique` | Collection - MTBeta | 49 | 168 | ✅ menu |
| `collection-sigma-plongeuse` | Collection - MTSigma | 5 | 52 | ✅ menu |
| `collection-epsilon-skeleton` | Collection - MTEpsilon | 19 | 0 | ✅ menu |
| `collection-zeta-skeleton-arabic-dial` | Collection - MTZeta | 17 | 0 | ✅ menu |
| `collection-gamma-quartz-miyota` | Collection - MTGamma | 26 | 0 | ✅ menu |
| `collection-gamma-dore-femme` | Collection - MTGamma Femme | 2 | 0 | ✅ menu |
| `omicron-dress-watch` | Collection - MTOmicron | 9 | 0 | ✅ menu |
| `mtphi` | Collection MTPhi | 6 | 0 | ✅ menu |
| `collection-iota-carree` | Collection - MTIota | 3 | 0 | ✅ menu |
| `collection-mu-acier-femme` | Collection - MTMu | 3 | 0 | ✅ menu |
| `delta-coeur-ouvert` | Collection - MTDelta | 6 | 0 | ✅ menu |
| `mteris` | Collection - MTEris | 2 | 0 | ✅ menu |
| `collection-mtaurea` | Collection - MTAuréa | 2 | 0 | ✅ menu |
| `aurea-femme` | Collection Auréa | 2 | 0 | ✅ menu |
| `essentiels-maisondutemps` | Essentiels MaisonDuTemps | 2 | 0 | ✅ menu |

### Q. Accessoires et bijoux — **760 de trafic organique**

| Handle | Intitulé | Produits | Trafic SEMrush | Navigable |
|---|---|---:|---:|---|
| `bracelet-montre-acier` | Bracelet Montre Acier | 7 | **442** | 👻 orpheline |
| `watchroll` | Boite à montre | 12 | **213** | ✅ menu |
| `bracelets-de-montres-interchangeables` | Collection Bracelets | 25 | 71 | ✅ menu |
| `accessoires` | Accessoires | 49 | 34 | ✅ menu |
| `bracelets-14mm` | Bracelets 14mm | 16 | 0 | 👻 orpheline |
| `bracelets-20mm` | Bracelets 20mm | 9 | 0 | 👻 orpheline |
| `bracelet-cuir-montre` | Bracelet Cuir Montre | 1 | 0 | 👻 orpheline |
| `bracelet-acier` | Bracelet Acier - Bijoux | 7 | 0 | 👻 orpheline |
| `bracelet-acier-bijoux` | Bracelet Acier Bijoux | 7 | 0 | 👻 orpheline |
| `bracelet-chaine-bijoux` | bracelet chaine bijoux | 2 | 0 | 👻 orpheline |
| `bracelet-jonc` | Bracelet Jonc | 2 | 0 | 👻 orpheline |
| `bracelet-maille` | Bracelet Maille | 2 | 0 | 👻 orpheline |
| `bracelet-maille-1` | Bracelet maille | 2 | 0 | 👻 orpheline |
| `kit-outils` | Nos outils | 1 | 0 | 👻 orpheline |
| `bijoux` | Bijoux | 7 | 0 | ✅ menu |
### Le classement des axes, du plus rentable au plus mort

| Rang | Axe de découpe | Collections | Trafic | Verdict |
|---:|---|---:|---:|---|
| 1 | **B. Type de montre / de mouvement** | 26 | **7 162** | 🟢 Le pilier. Mais 84 % vient de 2 pages (`skeleton` 4 500, `automatiques` 1 500). |
| 2 | A. Genre / catalogue (chapeau) | 9 | 5 305 | 🟢 96 % sur `montres-homme` seul. |
| 3 | **D. Couleur de la montre** | 21 | **1 943** | 🟢 **Le meilleur rapport effort/rendement du site.** 16 pages qui rapportent, aucune ne demande de sourcing. |
| 4 | **E. Forme du boîtier** | 9 | **776** | 🟢 `carré` 461 + `octogonale` 222. Découpe rare, KD 10-13. |
| 5 | **F. Taille de poignet** | 4 | **767** | 🟢 `petit poignet` homme 520 + femme 209. **Mot humain, pas mot technique.** |
| 6 | Q. Accessoires et bijoux | 15 | 760 | 🟢 `bracelet-montre-acier` 442 à lui seul, **KD 6**. |
| 7 | C. Cadran à chiffres arabes | 3 | 662 | 🟢 KD 6, position 2. Confirme T-26. |
| 8 | L. Prix / promotion | 3 | 554 | 🟡 `pas cher` 398 — incompatible avec un positionnement de marque. |
| 9 | J. Bracelet de la montre | 19 | 283 | 🟡 95 % sur `silicone` seul ; 18 pages sur 19 à zéro. |
| 10 | P. Nom de collection maison | 15 | 220 | 🟡 Trafic de marque uniquement (`maison du temps mtbeta`). |
| 11 | K. Épaisseur | 1 | 207 | 🟢 **1 page, 207 visites.** Le meilleur ratio unitaire du site après le squelette. |
| 12 | M. Occasion / registre | 7 | 140 | 🔴 `mariage` 72, `chic` 48 ; `classique`, `élégante`, `sport chic`, `vintage` à **0**. |
| 13 | H. Étanchéité en ATM | 5 | 94 | 🔴 **Quasi mort.** |
| 14 | G. Diamètre en mm | 4 | 66 | 🔴 **Mort.** `montre-42mm` et `montre-42mm-homme` : 72 produits chacun, **0 visite chacun**. |
| 15 | I. Couleur de cadran isolée | 5 | 5 | 🔴 **Mort.** |
| 16 | N. Disponibilité (stock / précommande) | 2 | **0** | ⛔ **Zéro absolu.** C'est un filtre marchand, pas un mot-clé. |
| 17 | O. Opérations commerciales datées | 6 | **0** | ⛔ Zéro. Utile en campagne, jamais en SEO. |

### Les doublons qu'il faut savoir ne pas copier

Ils ont dupliqué des collections en espérant doubler la mise. **Cela n'a jamais marché : le doublon
ne partage pas le trafic, il meurt.**

| Paire | Produits | Trafic | Ce qui s'est passé |
|---|---|---|---|
| `montres-skeleton-homme` / `montre-squelette-automatique-homme` | 44 / 53 | **4 500** / **0** | La page avec meta-description et H1 propre prend tout. |
| `montres-arabic-dial-homme` / `montre-chiffre-arabe` | 10 / 9 | **593** / 69 | La page au `<title>` le mieux écrit **n'est pas** celle qui gagne : c'est l'antériorité qui décide. |
| `montres-10-atm` / `montre-etanche-10-atm` | 96 / 96 | 72 / **0** | Deux fois le même stock. |
| `montre-42mm` / `montre-42mm-homme` | 72 / 72 | **0** / **0** | Deux pages, zéro visite. |
| `montre-noir-femme` / `montre-noire-femme` | 1 / 1 | 0 / 0 | Intitulés terminés par « - SEO » laissés en production. |
| `solde-dete` / `solde-ete-montres-maisondutemps` / `solde-dhiver` | 151 chacune | 0 | Trois fois le catalogue entier. |

---

## 3. Les mots-clés qu'il porte, et lesquels rapportent vraiment

**2 535 mots-clés · 30,6 K de trafic organique estimé · 7 600 $ de coût de trafic · −20 % sur un mois ·
221 pages organiques · Authority Score 15.**

### 3.1 La part de marque — 35 % du total

| Mot-clé | Pos. | Trafic | Volume | KD |
|---|---:|---:|---:|---:|
| maison du temps | 1 | **6 500** | 8 100 | 26 |
| maison du temps montre | 1 | 1 000 | 1 300 | 24 |
| montre maison du temps | 1 | 1 000 | 1 300 | 23 |
| la maison du temps | 1 | 472 | 590 | 23 |
| montre temps · la-maison-du-temps · maisondutemps | 1 | 312 ×3 | 390 ×3 | 30-32 |
| maison du temp · temps montre · maison du temps skeleton · maison du temps mtbeta · mtbeta skeleton · bracelet maison du temps | 1 | 256 + 96 + 72 + 72 + 52 + 40 | — | — |
| **Sous-total marque** | | **≈ 10 500** | | |

⚠️ **Lecture obligatoire** : le chiffre de 30 600 qui circulait depuis le dossier du 14/08 **contient
un tiers de marque**. Ce qu'ils gagnent sur le marché générique est de l'ordre de **20 000**.
Et « maison du temps » est un nom **descriptif** — une partie de ces 8 100 recherches n'est même pas
une intention de marque au départ. C'est un choix de nom qui rapporte.

### 3.2 La grappe `squelette` — 23 requêtes, une seule URL, ≈ 3 980 visites

Toutes sur `/collections/montres-skeleton-homme`, toutes en **position 1** sauf trois.

| Mot-clé | Pos. | Trafic | Volume | KD |
|---|---:|---:|---:|---:|
| montre squelette homme | 1 | 719 | 2 900 | 13 |
| montre squelette | 1 | 595 | 2 400 | 14 |
| montre homme squelette | 1 | 471 | 1 900 | 19 |
| squelette montre | 1 | 396 | 1 600 | 14 |
| montre skeleton | 1 | 218 | 880 | 12 |
| montre squelette pour homme | 1 | 218 | 880 | 21 |
| montres automatiques squelette homme | 1 | 178 | 720 | 19 |
| montre squelette homme automatique | 1 | 178 | 720 | 19 |
| montre squelette automatique | 1 | 119 | 480 | 12 |
| montre automatique squelette homme | 1 | 119 | 480 | 18 |
| montre automatique squelette | 1 | 96 | 390 | 14 |
| montre squelette homme luxe | 1 | 96 | 390 | 15 |
| montres squelette homme | 1 | 96 | 390 | 17 |
| montre automatique squelette pour homme | 1 | 79 | 320 | 13 |
| montres automatiques squelette | 1 | 79 | 320 | 16 |
| montre homme squelette luxe | 1 | 79 | 320 | 12 |
| montre skeleton homme | 1 | 64 | 260 | 19 |
| montre automatique homme squelette | 2 | 63 | 480 | 18 |
| montre homme squelette automatique | 1 | 63 | 480 | **8** |
| skeleton montre | 1 | 52 | 210 | 10 |
| montres hommes squelette | 1 | 52 | 210 | 11 |
| montres squelettes homme | 1 | 42 | 170 | 17 |
| montres squelettes | 1 | 42 | 170 | 19 |

**Ce que ça démontre** : la grappe entière — permutations, singulier/pluriel, anglicisme `skeleton`,
qualificatif `luxe` — **se sert avec une seule page**. Il n'a jamais été nécessaire de créer
`montre-squelette-luxe` ni `montres-squelettes`. Notre boutique a **2 fiches squelette** en face de
**44** chez lui, sur la porte la plus rentable du marché.

### 3.3 Les têtes génériques hors squelette

| Mot-clé | URL de destination | Pos. | Trafic | Volume | KD |
|---|---|---:|---:|---:|---:|
| montre | `montres-homme` | 4 | **3 200** | 90 500 | 56 |
| montre automatique homme | `montres-automatiques-homme` | 3 | 435 | 9 900 | 27 |
| montre homme | `montres-homme` | 10 / 11 | 452 + 271 | 90 500 | 40 |
| hommes montre | `montres-homme` | 2 | 295 | 3 600 | 29 |
| montres homme | `montres-homme` | 6 | 237 | 9 900 | 37 |
| montres hommes | `montres-homme` | 2 | 211 | 1 600 | 36 |
| montre automatique | `montres-automatiques-homme` | 5 | 194 | 8 100 | 29 |
| montre rose | `montre-rose-maisondutemps` | 1 | 322 | 1 300 | 18 |
| montre homme en argent | `montre-argent-homme` | 2 | 171 | 1 300 | 18 |
| mongte *(faute de frappe de « montre »)* | home | 3 | 158 | 3 600 | 16 |
| montre noir homme | `montre-homme-noir` | 2 | 131 | 1 600 | 17 |
| montre homme argent | `montre-argent-homme` | 3 | 131 | 1 600 | 19 |
| montre quartz | `montres-quartz-homme` | 5 | 126 | 3 600 | 16 |
| montre chiffre arabe | `montres-arabic-dial-homme` | 2 | 116 | 880 | **6** |
| montre en argent | `montre-argent-homme` | 5 | 105 | 2 400 | 15 |
| montre a aiguille | `montre-aiguille` | 1 | 96 | 390 | 18 |
| montre octogonale | `montre-octogonale` | 1 | 79 | 320 | **10** |
| montre arabe | `montres-arabic-dial-homme` | 1 | 79 | 320 | **6** |
| montre homme petit poignet | `montre-homme-petit-poignet` | 1 | 79 | 320 | 14 |
| montre homme fine | `montre-homme-plate` | 1 | 79 | 320 | 17 |
| montres aiguilles | `montre-aiguille` | 2 | 77 | 590 | 15 |
| montres carrées pour homme | `montre-cadran-carre-homme` | 4 | 72 | **2 400** | **13** |
| montre homme quartz | `montres-quartz-homme` | 3 | 72 | 880 | 13 |
| bracelet montre acier | `bracelet-montre-acier` | 2 | 63 | 480 | **6** |
| montres automatiques homme pas cher | `montre-automatique-pas-cher` | 2 | 63 | 480 | 19 |
| montre arabic dial | `montres-arabic-dial-homme` | 2 | 63 | 480 | **6** |
| montre homme en silicone | `montre-homme-bracelet-silicone` | 1 | 64 | 260 | 13 |
| etuis montres | `watchroll` | 3 | 59 | 720 | 16 |
| montre à aiguille | `montre-aiguille` | 1 | 46 | 720 | 13 |
| montre hexagonale | `montre-octogonale` | 1 | 42 | 170 | 11 |
| montre cadran | `montre-cadran-carre-homme` | 4 | 41 | 1 900 | 25 |

### 3.4 Ce qui ne rapporte rien chez lui — à ne surtout pas reproduire

| URL | Produits | Trafic | Pourquoi c'est mort |
|---|---:|---:|---|
| `montres-en-stock` / `montres-en-precommande` | 105 / 46 | **0** / **0** | On ne cherche pas un état de stock sur Google. |
| `montre-42mm` / `montre-42mm-homme` | 72 / 72 | **0** / **0** | Le diamètre en mm est un **filtre**, pas une requête. |
| `montre-etanche-10-atm` / `montre-etanche-3-atm` | 96 / 3 | **0** / **0** | Idem pour l'étanchéité. |
| `montre-automatique-cadran-noir` / `-cadran-bleu` / `montre-cadran-meteorite` | 18 / 6 / 1 | **0** | La couleur **de cadran** ne se cherche pas ; la couleur **de la montre**, si. |
| `montres-de-plongee-homme`, `montre-plongee-abordable`, `montre-plongee-automatique` | 4 / 5 / 5 | **0** ×3 | **Confirme le verdict « porte fermée » du dossier du 14/08 sur `montre de plongée`** — même avec trois pages et une ligne dédiée (MTSigma), il n'entre pas. |
| `montres-aviateur-homme` | 3 | **0** | **Confirme « tête fermée »** : mot de marque déguisé. |
| `montres-coeur-ouvert-homme`, `montres-phase-de-lune`, `montres-day-date` | 8 / 6 / 7 | **0** ×3 | Complications trop confidentielles en France. |
| `montre-classique-homme`, `montre-elegante-homme`, `montre-sport-chic-homme`, `montre-vintage` | 49 / 48 / 139 / 6 | **0** ×4 | Le vocabulaire de registre ne se tape pas. ⚠️ **`montre bracelet intégré` / sport chic : notre surdotation à 14 fiches ne trouvera pas de trafic non plus.** |
| `bracelets-14mm`, `bracelets-20mm`, `bracelet-cuir-montre` | 16 / 9 / 1 | **0** ×3 | ⚠️ **La cote en mm ne porte pas** — contredit l'hypothèse `bracelet montre 20mm` de l'ARBORESCENCE. |

### 3.5 Google Ads : il n'en fait pas

4 mots-clés payants relevés au 12/08 ; le rapport *Recherche publicitaire* SEMrush ne renvoie
aujourd'hui **aucune donnée**. À comparer aux 9 mots-clés payants d'`atelier-cohen-dubois` et aux
Ads d'`atelierbelvora`. **Un ticket 155-385 € tenu à 100 % en organique, c'est le contre-modèle
du Kraken payant** — et c'est atteignable parce que les KD de ses vraies portes sont de **6 à 19**.

---

## 4. Ses fiches produit

### 4.1 Le nommage — la trouvaille la plus transposable du dossier

**Le titre affiché ne contient aucun mot-clé. Le `<title>` en contient six.**

| Champ | Contenu réel |
|---|---|
| Titre produit Shopify | `MTZeta Arabic Rouge Acier` |
| Handle (URL) | `montre-homme-mtzeta-arabic-noir-automatique-miyota-…` — **ancien titre descriptif conservé** |
| Meta title | `Montre Homme Automatique MTZeta Arabic Rouge 40 mm Miyota Bracelet Acier \| MAISON DU TEMPS` |

Ils ont **renommé les titres en nom de marque** (lisibilité, image de maison horlogère) **sans
toucher aux handles**, donc sans perdre une seule URL, et **ont replacé tout le vocabulaire SEO dans
le meta title**. La grammaire du meta title est stable :
`Montre {Genre} {Mouvement} {Modèle} {Diamètre} {Calibre} Bracelet {Matière} | MARQUE`.

⚠️ **Le calibre `Miyota` est un nom de marque tierce dans le meta title.** Toléré en SEO ; **à ne pas
reproduire dans un titre de flux Merchant Center** — c'est exactement le piège `seiko mod` déjà
identifié dans l'ARBORESCENCE.

**Une fiche = un coloris = un produit.** 118 montres, **163 variantes au total** : autrement dit
**une variante par fiche**. Les déclinaisons sont liées entre elles par un bloc « Variations » de
pastilles qui pointent vers les fiches sœurs. **Notre catalogue fait l'inverse** : 63 montres pour
plus de 400 variantes, jusqu'à 104 sur une seule fiche (`Explorateur`). Leur modèle donne 118 URL
indexables ; le nôtre en donne 63.

### 4.2 La structure de la page, dans l'ordre

1. Badge d'état (`NOUVEAUTÉ` / `TOP VENTE` / `BEST SELLER` / `PERSONNALISEZ MOI`), titre de marque, prix, paiement 3× ou 4×, note d'avis.
2. **Chapeau de 3 à 4 lignes** — médiane mesurée **301 caractères**, maximum 923. *C'est très court.*
3. Pastilles « Variations » vers les fiches sœurs.
4. **Accordéon « DÉTAILS TECHNIQUES »**, toujours les mêmes 13 lignes : diamètre · boîtier (nuance d'acier) · épaisseur · fond du boîtier · finition · bracelet · **entrecorne** · cadran · index et aiguilles · verre · mouvement (calibre nommé) · réserve de marche · étanchéité · **poids selon le bracelet**.
5. Accordéons `RETOURS ET ÉCHANGES` (14 jours, *les montres gravées ne sont pas reprises*), `LIVRAISON` (Colissimo offert dès 100 €, DHL Express payant, expédition le jour même avant 12 h), `GARANTIE` (**2 ans**).
6. **Options payantes vendues sur la fiche** : mise à taille du bracelet **8 €**, gravure.
7. **Disponibilité datée** : « En stock — livraison prévue entre le 17 et le 21 août ».
8. Deux blocs éditoriaux courts, l'un sur le cadran, l'autre sur la marque.
9. **Bloc pédagogique réutilisé à l'identique sur toutes les fiches** : « le mécanisme automatique », « la mise à l'heure », « la mise à taille », « nous contacter ». Rédigé une fois, servi 162 fois.
10. Cross-sell « COMPLÈTE TON LOOK » (bracelets de la même entrecorne).
11. Trustpilot, puis footer avec **« TOP CATÉGORIES »** — 5 liens vers les collections qui rapportent.

**5 images par fiche**, médiane et maximum confondus : c'est un standard tenu, pas une moyenne.

### 4.3 Sa politique de précommande — c'est un modèle de financement, pas un délai subi

`/pages/nos-precommandes` l'assume totalement : la précommande **finance la production** et **mesure
la demande avant de produire**. Cycle annoncé : design → production 45-60 jours → ouverture des
précommandes. Contrepartie au client : **remise commerciale + un cadeau** (stickers, bracelet, sac ou
porte-clés). Le tag `PRÉCOMMANDE` porte **14 produits sur 162**, et la collection dédiée
`montres-en-precommande` compte 46 produits — **pour 0 visite organique**.

⚠️ **La leçon est double.** ① Le discours de précommande est un **argument de conversion sur la fiche**,
et il fonctionne pour une marque qui produit. ② **En faire une collection est inutile en SEO.**
③ **Il ne nous est pas transposable en dropshipping** : nous ne produisons rien, donc « financer notre
production » serait une promesse fausse — exactement le type d'affirmation que la mémoire projet
interdit (« promesses vérifiables »).

### 4.4 Le reste du dispositif

- **4 langues** : `/fr`, `/it`, `/en`, `/de`, avec sitemaps séparés. Le `/en/` rapporte déjà 25 visites.
- **19 articles de blog** pour **≈ 253 visites** — dont `montre-homme-carree-automatique` 65 et
  `histoire-et-recommandation-montre-chiffres-arabes` 61. **Le blog pèse 0,8 % du site.** À mettre en
  regard de la recommandation « blog technique » du dossier du 14/08 : chez `esprit-nato` ça marche,
  **ici, non**. Ce sont les collections qui gagnent.
- **37 pages** dont un **quiz « trouve ta montre idéale » contre −15 %**, un jeu-concours iPhone
  (53 visites), un programme de fidélité, un programme ambassadeur, un store locator, une **page
  gravure** (79 visites, 29 mots-clés) et une page « prochaines sorties ».
- Compte à rebours en barre haute : « avant la prochaine expédition ».
- **Les fiches produit ne portent presque rien** : ≈ 400 visites cumulées sur 162 fiches, contre
  18 944 pour les collections. **Le SEO de ce site est intégralement collection.**

---

## 5. La correspondance avec nos familles

**Notre catalogue de référence** (`INVENTAIRE-VISUEL-2026-08-08.csv`) : 63 montres, 42 accessoires,
96 fiches actives. Nos lignes : **Trente-Six** (36 mm, 6 coloris) · **Trente-Neuf** (39 mm, 7 coloris
+ 2 bicolores) · **Quarante-et-Un** (41 mm, 7) · **Intégrale** (sport chic, 8) · **Voyageur** (GMT, 6)
· **Contre-la-montre** (chronographe, 12) · **Héritage** (plongeuse 42, 3) · **Noirmont Un**
(aviateur, 2) · **Éclaireur** (field, 2) · **Explorateur** (1) · **Squelette Carré** et
**Squelette Octogone** (2).

| Sa collection | Son trafic | Dit-on la même chose ? | Notre offre aujourd'hui | Verdict |
|---|---:|---|---|---|
| `montres-skeleton-homme` | **4 500** | Oui, exactement | **2 fiches** (Carré, Octogone) | 🔴 **Le trou n°1.** Même mot, même intention. 44 fiches chez lui. |
| `montres-homme` | 5 100 | Oui | 63 montres | 🟡 Chapeau à créer, mais KD 40-56 : objectif de fond. |
| `montres-automatiques-homme` | 1 500 | Oui | ~50 automatiques | 🟢 À créer, KD 27. |
| `montre-argent-homme` + `montre-argent` | **878** | ⚠️ « argent » = **la couleur acier**, pas le métal | Toutes nos montres acier | 🟡 Servable, **mais risque d'allégation de matière** — voir §8. |
| `montres-arabic-dial-homme` | 593 | Oui | **5 fiches** chiffres arabes | 🟢 KD 6, il est en position 2. Notre `montre chiffre arabe` 880 tient toujours. |
| `montre-homme-petit-poignet` (35-40 mm) | **520** | Oui | **Trente-Six (6) + Trente-Neuf (9) = 15 fiches** | 🟢🟢 **La meilleure correspondance du dossier. Zéro sourcing.** |
| `montre-cadran-carre-homme` | **461** | Oui — forme du boîtier | **Squelette Carré** (1) | 🟡 Volume 2 400 KD 13 pour 1 fiche. Sourcing léger très rentable. |
| `bracelet-montre-acier` | **442** | Oui | **Présidentiel acier, Présidentiel doré, acier massif 12-22, Jubilé 20 mm, milanais = 5 fiches** | 🟢🟢 **KD 6. Servable ce soir.** |
| `montre-aiguille` | **423** | Oui — analogique vs connectée | **Les 63 montres** | 🟢🟢 **Une page, tout le catalogue, zéro sourcing.** |
| `montre-automatique-pas-cher` | 398 | Oui, mais | Nos prix 279-429 € | ⛔ Incompatible avec le positionnement, et avec le constat « nos squelettes sont hors bande de marché ». |
| `montres-quartz-homme` | 385 | Oui | **Contre-la-montre** (12 chronographes) | 🟡 À vérifier : nos chronos sont-ils quartz ? Si oui, page gratuite. |
| `montre-rose-maisondutemps` + `montre-rose-homme` | **473** | Oui — couleur | Trente-Six Rose, Trente-Neuf Rose, Contre-la-montre Rose poudré | 🟢 3 fiches suffisent (il en a 10). |
| `montre-homme-noir` + `montre-acier-noir-homme` | **316** | Oui | Trente-Neuf Noir, Quarante-et-Un Noir ×3, Contre-la-montre Noir | 🟢 Servable. |
| `watchroll` (`etuis montres`) | **213** | Oui | **4 Rouleaux de Voyage + Étui de voyage rigide** | 🟢🟢 **5 fiches prêtes, volume 720 KD 16.** |
| `montre-octogonale` | **222** | Oui | **Squelette Octogone** (1) | 🟢 KD 10, position 1 avec peu. **Une fiche peut suffire à ouvrir la page.** |
| `montre-femme-pour-petit-poignet` | 209 | Oui | **Aucune** — catalogue 100 % homme | ⛔ Ne s'applique pas. Rappelle le manque « marché féminin non instruit ». |
| `montre-homme-plate` (`montre homme fine`) | **207** | Oui — épaisseur | Trente-Six et Trente-Neuf classiques | 🟢 À mesurer sur nos épaisseurs réelles avant d'annoncer. |
| `montre-automatique-francaise` | 196 | ⚠️ Ambigu | Marque française, montres assemblées en Asie | ⛔ **Ne pas copier** — allégation d'origine, voir §8. |
| `montre-homme-bracelet-silicone` | 268 | Oui | Bracelet FKM ×2, caoutchouc gaufré | 🟡 Côté **bracelets** oui ; côté **montres livrées sur silicone**, non. |
| `montres-chronographe-homme` | 67 | Oui | **12 chronographes** | 🟡 Notre ARBORESCENCE lui donne 1 000 de volume ; **chez lui ça ne rapporte que 67**. Attente à revoir à la baisse. |
| `montres-de-plongee-homme` (×3 pages) | **0** | Oui | Héritage ×3 | ⛔ **Confirmation indépendante** : porte fermée. Ne pas sourcer de 200 m. |
| `montres-aviateur-homme` | **0** | Oui | Noirmont Un ×2 | ⛔ **Confirmation** : tête fermée. Créer la page ne rapportera rien. |
| `montre-mariage-homme` / `-chic` / `-habillee` | 140 | Oui | Trente-Six, Trente-Neuf | 🟡 Faible, mais gratuit. |
| `montres-en-stock` / `-en-precommande` | **0** | Oui | — | ⛔ **Ne pas créer.** |
| Diamètre en mm (4 pages) | **66** | Oui | Nos diamètres sont dans les noms | ⛔ **Ne pas créer** — préférer `petit poignet`. |
| Étanchéité en ATM (5 pages) | **94** | Oui | 5 bar / 10 bar | ⛔ **Ne pas créer.** |
| Couleur de cadran isolée (5 pages) | **5** | Oui | 21 fiches à option « Cadran » | ⛔ **Ne pas créer.** ⚠️ **Nos 4 collections `cadran-*` actuelles sont exactement cette erreur.** |
| `bracelets-14mm` / `bracelets-20mm` | **0** | Oui | `Bracelet acier massif 12 à 22 mm` | ⛔ **La cote en mm ne porte pas.** Contredit `bracelet montre 20mm` de l'ARBORESCENCE. |

---

## 6. Trois axes qu'il exploite et que notre ARBORESCENCE ignorait

1. **La forme du boîtier — 776 visites, KD 10-13, et nous avons déjà les deux produits.**
   `montres carrées pour homme` pèse **2 400 recherches KD 13**, `montre octogonale` 320 KD 10,
   `montre hexagonale` 170 KD 11. Notre catalogue contient un **Squelette Carré** et un
   **Squelette Octogone** — les deux seules montres de forme du marché à ce prix. **Aucune ligne de
   l'ARBORESCENCE ne mentionne cet axe.**
2. **La morphologie du poignet — 767 visites.** `montre homme petit poignet` 320 KD 14 +
   `montre petit poignet homme` 260 + `montres homme petit poignet` 260 + `montre homme pour petit
   poignet` 210 ≈ **1 050 de grappe**, entièrement servable par nos **Trente-Six** et
   **Trente-Neuf**. C'est le mot qui remplace le diamètre en mm.
3. **`montre à aiguille` — 423 visites, 42 mots-clés, grappe ≈ 2 000** (`montre à aiguille` 720,
   `montres aiguilles` 590, `montre a aiguille` 390, `montre à aiguille homme` 320). C'est la requête
   de quelqu'un qui **refuse la montre connectée**. Une page, tout le catalogue.

---

## 7. Ce qu'on lui prend — liste priorisée

### A. Servable avec le catalogue actuel, aucun sourcing

| # | Ce qu'on crée | Handle proposé | Preuve chez lui | Volume / KD | Notre offre | Effort |
|---:|---|---|---:|---|---|---|
| 1 | **Montres pour petit poignet (36-40 mm)** | `montre-homme-petit-poignet` | 520 visites | grappe ≈ 1 050, KD 11-17 | **15 fiches** Trente-Six + Trente-Neuf | 1 page |
| 2 | **Bracelets de montre en acier** | `bracelet-montre-acier` | 442 visites, 54 mots-clés | 480, **KD 6** | **5 fiches** (Présidentiel, massif, Jubilé, milanais) | 1 page |
| 3 | **Montres à aiguilles** | `montre-aiguille` | 423 visites, 42 mots-clés | grappe ≈ 2 000, KD 13-18 | **les 63 montres** | 1 page |
| 4 | **Étuis et rouleaux de voyage** | `etui-a-montre` | 213 visites | `etuis montres` 720 KD 16 | **5 fiches** | 1 page (renommer l'existant) |
| 5 | **Montres octogonales** | `montre-octogonale` | 222 visites, position 1 | 320 **KD 10** + hexagonale 170 | **Squelette Octogone** | 1 page, 1 produit |
| 6 | **Montres à chiffres arabes** | `montre-chiffre-arabe` | 593 visites, position 2 | 880 **KD 6** | **5 fiches** | déjà prévu ✅ |
| 7 | **Par couleur : noire · rose · bleue · verte · dorée · blanche** | `montre-homme-noir`, `-rose`, … | 1 943 sur l'axe | 260-1 600 par couleur, KD 13-19 | Nos coloris couvrent les 6 | 6 pages |
| 8 | **Montres automatiques homme** | `montre-automatique-homme` | 1 500 visites | 9 900 KD 27 | ~50 fiches | 1 page (objectif de fond) |

**Total adressable de ce bloc chez lui : ≈ 4 400 visites/mois, pour 0 € de sourcing et ~14 pages.**

### B. Demande du sourcing, par ordre de rendement

| # | Ce qu'on source | Preuve | Volume / KD | Notre offre | Ce qu'il faut |
|---:|---|---:|---:|---|---|
| 1 | **Montres squelette** | **4 500 visites**, 23 requêtes, une URL | `montre squelette homme` 2 900 **KD 13**, grappe 8 400 | **2 fiches** contre 44 | **8-10 fiches**, et ⚠️ **descendre dans la bande 155-295 €** — nos 399-429 € sont hors marché (dossier du 14/08) |
| 2 | **Montres carrées** | 461 visites | `montres carrées pour homme` **2 400 KD 13** | 1 fiche | 4-6 fiches de boîtier carré |
| 3 | **Montres fines / plates** | 207 visites | `montre homme fine` 320 KD 17 | à vérifier | mesurer nos épaisseurs, sinon sourcer 3-4 boîtiers < 10 mm |
| 4 | **Boîtes et coffrets 69-189 €** | *(hors MaisonDuTemps — voir dossier du 14/08)* | `boite a montre` 5 400 KD 35 | 3 fiches | 8-10 fiches, découpe **par capacité** |

### C. Ce qu'on ne copie pas — et pourquoi c'est une décision, pas un oubli

| Sa découpe | Son trafic | Raison de ne pas la reprendre |
|---|---:|---|
| Diamètre en mm (`montre-42mm`, `-40mm`, `-38mm`) | 66 | Filtre, pas requête. Remplacé par « petit poignet ». |
| Étanchéité en ATM | 94 | Idem. |
| Couleur de **cadran** isolée | 5 | ⚠️ **C'est exactement le défaut de nos 4 collections `cadran-*`.** |
| Disponibilité (stock / précommande) | **0** | Filtre marchand. |
| Opérations datées (soldes, French Days, Fête des pères) | **0** | Utile en campagne, jamais en SEO. |
| Registre (`classique`, `élégante`, `sport chic`, `vintage`) | **0** | ⚠️ Confirme que nos **14 fiches sport chic / bracelet intégré** ne trouveront pas de trafic. |
| Plongée (3 pages), Aviateur (1 page) | **0** | Confirmation indépendante des portes fermées. |
| Cote de bracelet en mm | **0** | Contredit `bracelet montre 20mm` de l'ARBORESCENCE. |
| `montre-automatique-pas-cher` | 398 | Positionnement incompatible. |
| `montre-automatique-francaise` | 196 | Allégation d'origine — §8. |
| Un article de blog par famille | 253 total | 0,8 % du site. Les collections gagnent, pas le blog. |
| Doublons de collection | 0 chacun | Le doublon ne partage pas, il meurt. |

### D. Trois points de méthode à reprendre tels quels

1. **Le meta title porte le SEO, le titre affiché porte la marque.** Grammaire :
   `Montre {Genre} {Mouvement} {Modèle} {Diamètre} Bracelet {Matière} | MAISON NOIRMONT`.
   ⚠️ **Sans nom de calibre tiers** dans le champ qui part au flux Merchant Center.
2. **Une collection SEO n'a pas besoin d'être dans le menu.** 112 de ses 154 collections sont
   orphelines et pèsent quand même 3 900 visites. On peut créer 20 pages sans toucher à la navigation.
3. **Une collection sans meta-description ni H1 propre ne rapporte rien**, quel que soit son mot-clé.
   La preuve est chez lui : 4 500 contre 0 sur deux pages quasi identiques. **Toute collection créée
   doit avoir son H1, sa meta-description et son `<title>` avant d'être publiée.** Sa grammaire de
   `<title>` — `{Mot-clé} : dès {prix}€ - MARQUE` — est directement reprenable.

---

## 8. Deux pièges de son modèle à ne pas importer

⚠️ **`montre argent` / `montre-argent-homme` (878 visites).** Chez lui, « argent » désigne la
**couleur de l'acier**, pas le métal précieux. C'est ambigu au sens de la réglementation française sur
les métaux précieux et au sens des règles de description produit de Merchant Center. Le volume est
réel (`montre en argent` 2 400 KD 15), mais **la page doit dire « acier couleur argent » dès le H1**,
et jamais « montre en argent » dans un titre de flux.

⚠️ **`montre-automatique-francaise` (196 visites).** Une marque française qui fait assembler en Asie
n'est pas une « montre automatique française » au sens où le client l'entend. C'est le même type
d'affirmation que celles purgées le 08/08 (« 904L », « tous les cadrans sont stériles »). **On ne
prend pas ce mot.** Notre équivalent honnête est « maison française », sur la page marque, pas sur
une collection produit.

---

## 9. Ce que ce dossier corrige et ce qu'il ne mesure pas

**Corrections apportées au dossier du 14/08** :
- Le §3.1 recommandait de reprendre « diamètre, étanchéité, couleur de cadran, disponibilité » et
  chiffrait « 40 collections gratuites ». **Ces quatre axes pèsent 165 visites sur 30 600.** La
  recommandation est remplacée par les axes couleur / forme / poignet / épaisseur (**3 693 visites**).
- « 154 collections construites une par une sur la longue traîne » : exact en nombre, **faux en
  effet**. 71 % du trafic tient sur 4 pages ; 112 collections sont orphelines ; une bonne moitié
  contient tout le catalogue.
- « 30 600 visites organiques » : **contient ≈ 10 500 de marque**. Le générique est ≈ 20 000.

**Ce qui n'est pas mesuré ici** :
- **SimilarWeb toujours inaccessible** — la règle « trafic réel ≈ SimilarWeb × 3 » n'a pas pu être
  appliquée. Aucun verdict de ce document ne repose sur des visites totales : tout est du trafic
  organique estimé SEMrush.
- Volume de `montres automatiques françaises` non relevé (mot écarté de toute façon).
- Épaisseur réelle de nos Trente-Six et Trente-Neuf non vérifiée — bloquant pour l'action B-3.
- Nature du mouvement de nos 12 chronographes (quartz ou automatique) non vérifiée — bloquant pour
  la page `montres-quartz-homme`.
- Ses chiffres de vente, ses marges et sa source d'approvisionnement restent inconnus. Ses 5 photos
  par fiche et son ton de maison horlogère supposent un budget visuel qu'on n'a pas chiffré.

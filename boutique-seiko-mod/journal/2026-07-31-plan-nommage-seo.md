---
type: journal
boutique: seiko-mod
date: 2026-07-31
nature: analyse
leviers: [seo]
titre: "Plan de nommage SEO — Maison Noirmont (`v42pzp-h4` / maisonnoirmont.fr)"
---

# Plan de nommage SEO — Maison Noirmont (`v42pzp-h4` / maisonnoirmont.fr)

> **Étude de faisabilité, 30/07/2026. Rien n'a été modifié** : aucun produit, aucune collection,
> aucun thème, aucun métachamp, aucune application installée, aucune commande, aucun identifiant
> saisi. Tout ce qui est chiffré ci-dessous a été **relevé par l'API Admin** ce jour, ou provient
> de `2026-07-31-marche-complet-semrush.md` (mesures SEMrush payantes du 25-27/07).
> Les volumes non mesurés sont **signalés comme tels et jamais estimés**.

---

## 1. Le verdict — la surcharge du titre de flux est possible, et gratuite

**Issue (a), avec une nuance qui commande tout le reste du plan.**

On peut envoyer à Google Shopping un titre différent de celui affiché en boutique, **sans
application payante**. Mais le levier natif est **global, pas par produit** : c'est le `seo.title`
de la fiche qui devient le titre du flux.

### Ce qui a été vérifié dans la boutique (API, 30/07)

| Contrôle | Relevé |
|---|---|
| Canaux de vente publiés | **3** : Boutique en ligne `358599295314`, Point de vente `358599328082`, Shop `358599360850` |
| Canal « Google & YouTube » | **absent** — l'application **n'est pas installée** |
| Définitions de métachamps produit | 13, aucune dans le namespace `mm-google-shopping` |
| Namespaces présents | `shopify`, `shopify--discovery--*`, `custom` (diametre, calibre, couleur_cadran, famille, bracelet) |

*(`appInstallations` renvoie `access denied` sur ce jeton : l'absence de l'app est établie par
l'absence de publication « Google & YouTube », pas par la liste d'applications. Vérification
d'un œil à faire dans l'admin — c'est le seul point de l'étape 1 qui reste à confirmer visuellement.)*

### Ce que permet le canal officiel, une fois installé

1. **Réglage natif, à l'échelle de la boutique** — l'application « Google & YouTube » propose une
   préférence *Titre du produit* : **« Titre du produit par défaut »** ou **« Titre SEO du
   produit »**. Google la documente explicitement comme le moyen d'« inclure plus de mots clés pour
   le référencement sur Google Shopping **sans modifier les informations produit de la boutique en
   ligne** ». → https://support.google.com/merchants/answer/13693394
   C'est exactement ce qui est demandé : titre de marque en boutique, titre porteur de mots clés
   dans le flux.
2. **Pas de surcharge par produit côté Shopify** — le namespace `mm-google-shopping` ne comporte
   **aucune clé `title`** (les clés connues sont `custom_product`, `mpn`, `google_product_category`,
   `age_group`, `gender`, `condition`, `color`, `material`, `size*`, `custom_label_0..4`). Shopify
   ne publie pas de liste officielle des clés encore lues en 2026 : réserve assumée.
3. **Surcharge par produit, gratuite, côté Merchant Center** — module gratuit **« Gestion avancée
   des sources de données »** (https://support.google.com/merchants/answer/15125982), puis :
   - **règles d'attribut** pour reconstruire `title`
     (https://support.google.com/merchants/answer/14994083) ;
   - ou **source de données supplémentaire** (Google Sheet, clé `id` + colonne `title`) qui
     « enrichit **ou écrase** » la source primaire
     (https://support.google.com/merchants/answer/15624457).
4. **Aucune application de flux n'est nécessaire** à 57 fiches. Si Hakim en voulait une malgré tout,
   la moins chère du marché est **Simprosys « Google Shopping Feed » à 4,99 $/mois** jusqu'à 500
   produits (https://apps.shopify.com/google-shopping-feed) ; DataFeedWatch est à **64 $/mois**
   (https://apps.shopify.com/datafeedwatch) ; Feedonomics ne publie pas de tarif.

### La conséquence qui commande le plan

> **Le `seo.title` devient le titre de flux.** Une seule chaîne doit donc satisfaire deux juges à
> la fois : Google Search (~60-65 caractères avant troncature) et Merchant Center (150 caractères
> max, **descriptif du produit, cohérent avec la page d'atterrissage**, sans texte promotionnel —
> https://support.google.com/merchants/answer/7052112).
> **On écrit donc pour Merchant Center et on plafonne à 65 caractères.** Pas d'empilement de mots
> clés : la spécification Google exige que le titre corresponde à la page d'arrivée, et
> *Misrepresentation* est un motif de suspension de compte
> (https://support.google.com/merchants/answer/6149970).

### ⚠️ Piège découvert au passage — « Livraison offerte »

Les **53 `seo.description`** renseignées se terminent par *« Livraison offerte, garantie 12 mois. »*
L'application propose la même bascule pour la description (*Description SEO du produit*). Google
proscrit le texte promotionnel de type « livraison gratuite » dans les champs de flux.
**Recommandation : laisser la préférence de description sur « description produit par défaut »**, et
ne basculer que le titre. Sinon il faut purger 53 descriptions SEO avant de brancher le flux.

---

## 2. L'état actuel, mesuré (API Admin, 30/07/2026)

### 2.1 Les 57 fiches montres publiées

Collection parente « Les Montres » (`690663162194`) : **63 fiches**, dont **6 en DRAFT**
(`aviateur-acier-cadran-chiffres-arabes`, `voyageur-gmt-automatique`,
`noirmont-deux-plongeuse-ceramique`, `heritage-plongeuse-vintage-42`, `integrale-sport-chic-acier`,
`contre-la-montre-chronographe-panda`) → **57 ACTIVE**. Le compte est exact.

| Champ | État relevé |
|---|---|
| `product_type` | **45** × « Montre automatique », **12** × « Montre chronographe ». Homogène, exploitable tel quel. |
| Étiquettes | **une seule par fiche**, la famille : `classiques` **19**, `sport-chic` **15**, `chronos` **12**, `gmt` **6**, `plongeuses` **3** (+ `skx`), `squelettes` **2** = 57. Aucune étiquette de diamètre, de calibre ni de couleur — ces axes vivent dans les métachamps `custom.*`. |
| `seo.title` | **53 renseignés / 57**. **4 vides** : `trente-neuf-classique-cannelee`, `trente-six-classique-jubile`, `trente-neuf-duo-classique-bicolore`, `quarante-et-un-sport-acier` (les fiches mères restées actives). |
| `seo.description` | même compte : 53 / 57. |
| Handles | tous descriptifs et stables ; **4 ont été redirigés aujourd'hui** (grappe « chiffres arabes »). |

### 2.2 L'ampleur de l'invisibilité — les titres de boutique

Comptage exact sur les **57 titres publiés** :

| Ce que cherche Google | Titres concernés | Part |
|---|---|---|
| Le **nom commun « montre »** | **2 / 57** — les deux Squelette uniquement | **3,5 %** |
| La chaîne « montre », nom de modèle compris | 14 / 57 | 25 % |
| dont « **Contre-la-montre** » (nom du chronographe, pas un type de produit) | **12 / 57** | 21 % |
| « **automatique** » | **3 / 57** | **5,3 %** |
| « **homme** » ou « femme » | **0 / 57** | **0 %** |
| Une **unité « mm »** | **0 / 57** | **0 %** |
| Un **diamètre en chiffres** | **3 / 57** — « Plongeuse vintage **42** », sans unité | **5,3 %** |
| Titre commençant par un **nom de marque français** | **57 / 57** | **100 %** |

> **Lecture** : sur 57 fiches, deux seulement portent le mot que le client tape. Les diamètres sont
> écrits **en toutes lettres dans les noms de marque** (Trente-Six, Trente-Neuf, Quarante-et-Un) :
> un actif de marque remarquable, et **zéro correspondance** avec « 36 mm », « 39 mm », « 41 mm ».
> C'est là que se situe tout l'écart — et c'est précisément ce que le `seo.title` répare sans
> toucher au titre affiché.

Nuance importante : le travail éditorial déjà fait est **bon**. Les 53 `seo.title` existants portent
déjà « Montre automatique », le calibre et souvent le diamètre. Il ne s'agit donc pas de tout
refaire, mais de **combler 4 trous et de corriger 12 chronos**.

### 2.3 Les collections

14 collections au total, dont **8 côté montres**. Les 6 familles historiques sont **toutes sans
couple SEO** ; seules les 2 grappes créées les 29-30/07 en ont un.

| Collection | Handle | Produits | `seo.title` | `seo.description` |
|---|---|---|---|---|
| Les Montres (parente) | `montres` | 63 | **vide** | **vide** |
| Classiques | `classiques` | 20 | **vide** | **vide** |
| Sport chic | `sport-chic` | 16 | **vide** | **vide** |
| Chronos | `chronos` | 13 | **vide** | **vide** |
| GMT | `gmt` | 7 | **vide** | **vide** |
| Plongeuses | `plongeuses` | 5 | **vide** | **vide** |
| Cadrans à chiffres | `montre-cadran-a-chiffres` | 5 | renseigné (30/07) | renseigné |
| Montres squelette | `montre-squelette` | 2 | renseigné (29/07) | renseigné |
| *(accessoires)* Remontoirs · Écrins et rouleaux · Bracelets · Outils d'horloger · Accessoires | | 13/10/10/8/42 | **tous vides** | **tous vides** |

Les descriptions longues, elles, sont **excellentes et pédagogiques** sur les 14 collections : la
matière première du `seo.description` existe déjà, il n'y a qu'à en extraire 155 caractères.

---

## 3. Le plan de nommage à trois niveaux

**Principe tenu :** les noms français de produits sont un actif de marque, ils ne bougent pas.
Les noms de collections sont du vocabulaire interne, ils deviennent descriptifs.

### 3.1 Niveau produit — titre boutique **inchangé sur 57 / 57**

**Patron de `seo.title`** *(= titre de flux Shopping, une seule chaîne pour les deux usages)* :

```
[Nom de modèle] — Montre [type] [homme si assumé] [diamètre] mm, [attribut décisif]
```

Règles :
- ≤ **65 caractères** (contrainte SERP, la plus serrée des deux) ;
- le **nom commun « montre »** est obligatoire — c'est le manque n°1 ;
- **un** diamètre en chiffres + « mm », jamais deux fois la même information ;
- « homme » **seulement là où la fiche l'assume** — les 36 mm sont vendus comme unisexes, un
  « homme » systématique serait une *Misrepresentation* pour Merchant Center ;
- **aucune marque tierce** (Seiko, Rolex, Daytona, Nautilus…) : interdit dans le texte d'annonce
  **et** sur la page d'arrivée (rappel juridique, `2026-07-31-marche-complet-semrush.md` §7). Les calibres
  `NH35` / `Miyota 8215` restent licites — ce sont des références de composant, déjà citées en fiche.
- **pas de « Livraison offerte »**, pas de prix, pas de superlatif.

**Patron de `seo.description`** (155 c.) : *type de montre + calibre + boîtier + verre/étanchéité
« annoncés »*. **Retirer « Livraison offerte »** si la bascule description est un jour activée.

#### Trois exemples réels

| Fiche | Titre boutique (**inchangé**) | `seo.title` actuel | `seo.title` proposé | Volume mesuré adossé |
|---|---|---|---|---|
| `contre-la-montre-panda-chronographe` | Contre-la-montre Panda — Chronographe | Contre-la-montre Panda — Chronographe 39 mm (43 c.) | **Contre-la-montre Panda — Montre chronographe 39 mm, cadran panda** (64 c.) | `chronographe` **3 600**/mois (KD 31, CPC 0,32 €) ; `montre chronographe panda` **10**/mois. ⚠️ `montre chronographe homme` **NON MESURÉ**. |
| `trente-neuf-noir-classique-cannelee` | Trente-Neuf Noir — Classique cannelée | Trente-Neuf Noir — Montre automatique lunette cannelée (54 c.) | **Trente-Neuf Noir — Montre automatique homme 36/39 mm, cadran noir** (65 c.) | `montre automatique homme` **9 900**/mois (KD 30, CPC 0,38 €) ; `montre lunette cannelée` **40**/mois seulement — la formulation actuelle vise le terme le plus faible. |
| `trente-neuf-classique-cannelee` (fiche mère, `seo.title` **vide**) | Trente-Neuf — Classique cannelée | *(vide)* | **Trente-Neuf — Montre automatique homme 36/39 mm, lunette cannelée** (65 c.) | `montre automatique homme` **9 900** ; `montre mécanique` **2 400** (KD 20). |

Chantier produit total : **4 fiches à doter** (mères actives) + **12 chronos à corriger**
(le nom commun « montre » y manque, « Chronographe » seul ne le porte pas) + **41 fiches déjà
conformes au patron**, à relire mais sans réécriture prévue.

### 3.2 Niveau collection — titre descriptif, libellé court au menu, `seo.title` complet

⛔ **Aucun handle n'est modifié dans ce plan** (voir §4.1 : c'est le poste de risque le plus cher, et
il n'apporte presque rien face au titre et au `seo.title`).

| Collection (handle inchangé) | Titre actuel | **Nouveau titre descriptif (H1)** | **Libellé court (menu)** | **`seo.title` proposé** | Volume **mesuré** adossé |
|---|---|---|---|---|---|
| `classiques` (20) | Classiques | **Montres automatiques homme, lunette cannelée** | **Classiques** | Montre automatique homme 36 et 39 mm, lunette cannelée — Noirmont *(65 c.)* | `montre automatique homme` **9 900** (KD 30, CPC 0,38 €) · `montre mécanique` **2 400** (KD 20) · `montre lunette cannelée` **40** |
| `chronos` (13) | Chronos | **Montres chronographe 39 mm** | **Chronos** | Montre chronographe 39 mm, méca-quartz — Maison Noirmont *(56 c.)* | `chronographe` **3 600** (KD 31, CPC 0,32 €) · `montre chronographe panda` **10**. ⚠️ intention ambiguë signalée §4.2 du livrable SEMrush : attire aussi l'acheteur de vraie montre à 2 000 €+ |
| `sport-chic` (16) | Sport chic | **Montres automatiques à bracelet intégré** | **Sport chic** | Montre automatique à bracelet intégré, acier 41 mm — Noirmont *(61 c.)* | `montre bracelet intégré` **110** (KD 11, CPC 0,00 €). ⚠️ appartient à la grappe « style français » **classée à abandonner** (560/mois cumulés) : gain SEO quasi nul, le renommage se justifie par la clarté, pas par le volume |
| `gmt` (7) | GMT | **Montres GMT automatiques, deux fuseaux** | **GMT** | Montre GMT automatique, deux fuseaux horaires — Maison Noirmont *(63 c.)* | `montre gmt automatique` **320** (KD 13, CPC 0,23 €). `seiko gmt` **1 900** est mesuré mais **inutilisable** : marque tierce interdite sur la page d'arrivée |
| `plongeuses` (5) | Plongeuses | **Montres style plongeuse automatiques** | **Plongeuses** | Montre style plongeuse automatique 42 mm — Maison Noirmont *(58 c.)* | ⚠️ **« montre de plongée » n'a jamais été mesuré** dans `2026-07-31-marche-complet-semrush.md` — je ne l'invente pas. Seul mesuré : `montre plongeuse vintage` **50** (KD 7, CPC 0,71 €). **Et le mot « plongée » est à proscrire** : 3 Héritage sont données à 5 bar, nage exclue (point 5 de `2026-08-08-reprise-session.md`). D'où « **style** plongeuse » — c'est une correction de véracité autant qu'un nommage |
| `montre-squelette` (2) | Montres squelette | **inchangé — déjà conforme** | Montres squelette | *en place depuis le 29/07, rien à faire* | `montre squelette homme` **2 900** · `montre squelette` **2 400** · `montre squelette femme` **1 000** · `montre squelette automatique` **480** · `montre automatique squelette` **390** ≈ **8 400/mois**. ⚠️ **la meilleure grappe française du plan n'a que 2 fiches** : c'est un sujet de sourcing, pas de nommage |
| `montre-cadran-a-chiffres` (5) | Cadrans à chiffres | **inchangé — déjà conforme** | Cadrans à chiffres | *en place depuis le 30/07* | ⚠️ La grappe qui pèse (`seiko arabic dial` 8 100 · `arabic dial seiko` 3 600 · `seiko arabic` 2 400 · `seiko arabe` 1 300 · `seiko chiffre arabe` 390 ≈ **15 500**) contient **« seiko » dans chacun de ses termes** → inutilisable sur la page d'arrivée. **Aucun équivalent français n'a été mesuré.** Ce volume se capte en contenu, pas en nommage de collection |
| `montres` (63, parente) | Les Montres | **Montres automatiques homme sans logo** | **Montres** | Montres automatiques homme, cadran sans logo — Maison Noirmont *(62 c.)* | `montre automatique homme` **9 900** · `montre mécanique` **2 400** |

**Bonus mesuré, hors périmètre des 6 mais publié et éligible Shopping** — deux collections
d'accessoires portent le meilleur rapport volume/difficulté de toute la cartographie et n'ont
**aucun couple SEO** :

| Collection | `seo.title` proposé | Volume mesuré |
|---|---|---|
| `remontoirs` (13) | Remontoir montre automatique, 1 à 12 emplacements — Maison Noirmont | `remontoir montre automatique` **4 400** (KD 13, CPC 0,42 €) |
| `ecrins-et-rouleaux` (10) | Coffret et écrin à montres, rouleau de voyage — Maison Noirmont | `coffret montre` **1 300** · `boîte à montre` **590** · `écrin montre` **90**. ⚠️ `rouleau de voyage montre` **NON MESURÉ** |

### 3.3 Niveau flux Shopping

Rien de spécifique à écrire : **le titre de flux = le `seo.title` produit** via la préférence
« Titre SEO du produit ». Les patrons du §3.1 sont donc déjà des titres de flux conformes.
La source supplémentaire Merchant Center (`id` + `title`) reste en réserve pour les cas où le
`seo.title` idéal pour Google Search ne serait pas le meilleur pour Shopping.

---

## 4. Les risques, chiffrés

### 4.1 Changements de handle — le plan en pose **zéro**, et voici pourquoi

**Fait constaté aujourd'hui** : `collectionUpdate` / `productUpdate` **ne créent pas la
redirection** quand le handle change — il faut passer `redirectNewHandle`, ou poser la redirection
à la main. Les 5 redirections existantes de la boutique ont **toutes** dû être créées
explicitement :

| Redirection | De | Vers |
|---|---|---|
| `1740923797842` | `/collections/montre-cadran-chiffres-arabes` | `/collections/montre-cadran-a-chiffres` |
| `1740925665618` | `/products/montre-field-bronze-cadran-chiffres-arabes` | `…-chiffres-1-12` |
| `1740925698386` | `/products/montre-field-acier-cadran-chiffres-arabes` | `…-chiffres-1-12` |
| `1740925731154` | `/products/montre-aviateur-bronze-cadran-chiffres-arabes` | `…-chiffres-1-12` |
| `1740925763922` | `/products/montre-aviateur-acier-cadran-chiffres-arabes` | `…-chiffres-1-12` |

**Coût du plan tel qu'il est écrit : 0 redirection.** Le titre d'une collection et son handle sont
indépendants ; renommer le titre ne touche pas l'URL.

**Si Hakim voulait quand même des handles porteurs de mots clés**, le devis est le suivant :

- **6 handles impactés** : `classiques`, `sport-chic`, `chronos`, `gmt`, `plongeuses`, `montres` ;
- **6 redirections à poser à la main**, aucune ne sera créée toute seule ;
- **6 points d'ancrage à reprendre en même temps**, sous peine de liens morts :
  1. `main-menu` (`333968867666`) — 5 sous-items en dur. **⚠️ menu partagé entre les thèmes**, donc il touche aussi Helio, le thème publié ;
  2. `noirmont-mobile` (`334077362514`) — 7 sous-items + « Toutes les montres » ;
  3. `footer-boutique` (`334164230482`) — 5 items de collection ;
  4. `sections/header-group.json` du thème brouillon — **deux** grilles `collection_list` (méga-menu desktop + tiroir mobile) ;
  5. **`snippets/noirmont-configurateur.liquid` — le tableau `fam_handles` code les handles de familles en dur. Un handle changé et non répercuté casse le configurateur** ;
  6. le maillage de l'article `seiko-mod-ou-montre-hommage-difference`.
- Les fiches étant **publiées depuis le 29-30/07** et leurs URL déjà en circulation, une URL morte
  n'est pas théorique. **Recommandation : ne pas y toucher.**

### 4.2 Cohérence — le vrai piège est le libellé du méga-menu

Le libellé des vignettes du méga-menu est **`{{ closest.collection.title }}`** : il **suit le titre
de la collection tout seul** (constaté et documenté le 30/07). Autrement dit, si « Plongeuses »
devient « Montres style plongeuse automatiques », **la vignette affichera cette phrase entière**.

À l'inverse, les **items de menu** (`main-menu`, `noirmont-mobile`) portent un **libellé littéral**
qui, lui, ne suivra pas : ils resteront à « Plongeuses » jusqu'à édition manuelle.

Conséquence concrète pour la consigne « libellé court conservé pour le menu » :

| Emplacement | Comportement au renommage | Action |
|---|---|---|
| H1 de la page de collection | suit le titre | ✅ c'est l'objectif |
| `<title>` et meta | suivent `seo.title` / `seo.description` | ✅ |
| Items de `main-menu` / `noirmont-mobile` | **ne suivent pas** | ✅ rien à faire — le libellé court est conservé par inertie |
| **Vignettes du méga-menu et du tiroir mobile** | **suivent** — débordement probable | ⚠️ **remplacer le `{{ closest.collection.title }}` par le libellé court en dur, vignette par vignette, dans le thème brouillon** |
| Fil d'Ariane, facettes, configurateur | suivent le titre | à relire une fois |

Le rendu **375 px n'a jamais été produit** (limite documentée : `resize_window` sans effet, CSP
Shopify bloquant iframe et popup). Des libellés qui s'allongent sur un tiroir mobile jamais vu,
c'est le risque de cohérence le plus concret du plan. **QA mobile obligatoire après renommage.**

Enfin, quatre récits doivent dire la même chose : titres de collections, `seo.title`, libellés du
méga-menu, et le maillage de l'article. Aujourd'hui l'article maille déjà vers
`/collections/montre-cadran-a-chiffres` — cette cohérence-là est acquise.

### 4.3 Bloquants Google Shopping — aucune campagne ne tournera avant

| Bloquant | Relevé du 30/07 | Statut |
|---|---|---|
| **Boutique publique** | `onlineStore.passwordProtection.enabled` = **`true`** | ⛔ **BLOQUANT** — Merchant Center ne peut ni explorer le site ni vérifier la page d'arrivée. Rien ne peut être validé tant que le mot de passe est actif |
| **Thème** | « Maison Noirmont » `204248088914` toujours **UNPUBLISHED** ; le public voit encore Helio `204246548818` | ⛔ tout le travail de nommage côté thème serait invisible |
| **Médiateur de la consommation** | Les 7 politiques existent (contact, mentions légales, confidentialité, remboursement, expédition, CGV, CGU), mais **CGV art. 17 porte encore le marqueur `[À COMPLÉTER]`** | ⛔ **obligation légale** (art. L612-1 C. consom.), et Merchant Center exige des politiques complètes. Adhésion **par site** : ne jamais recopier le CM2C de Tuftéo |
| **Paiement fonctionnel** | Non vérifiable par l'API (`shopifyPaymentsAccount` → `access denied`, scope `read_shopify_payments` absent). `supportedDigitalWallets` = `SHOPIFY_PAY`, `APPLE_PAY` — indice, pas preuve | ⚠️ **à confirmer dans l'admin + une commande test**. 0 commande à ce jour |
| **Canal Google & YouTube** | non installé | ⚠️ prérequis, à installer par Hakim (interdit à l'agent) |
| **Affirmations invérifiables** | « 2 000 clients satisfaits », `review_count: 123`, badge « 1340 avis » pour 0 commande | ⚠️ *Misrepresentation* — motif de suspension de compte Merchant Center. Domaine réservé de Hakim |

---

## 5. Ordre d'exécution recommandé

**Phase 0 — Hakim, avant tout le reste** (rien de ce qui suit ne sert sans ça)
1. Renseigner le **médiateur de la consommation** en CGV art. 17.
2. **Republier le thème « Maison Noirmont »** `204248088914` et supprimer le fork obsolète.
3. Vérifier le **paiement** et passer une **commande test**.
4. **Retirer le mot de passe** de la boutique.
5. Purger les **affirmations invérifiables** (avis, compteurs clients).

**Phase 1 — produits, sans toucher aux titres** *(le travail le plus rentable, et le moins risqué)*
6. Doter les **4 fiches mères actives** d'un couple `seo.title` / `seo.description`
   — ⚠️ toujours poser **les deux dans le même `productUpdate`** : le remplacement est *wholesale*.
7. Corriger les **12 `seo.title` de chronos** pour y placer le nom commun « montre ».
8. Relire les **41 autres** contre le patron du §3.1 (diamètre, unité « mm »).

**Phase 2 — collections**
9. Poser les **6 nouveaux titres descriptifs** + **8 couples `seo.title`/`seo.description`**
   (6 familles + `montres`, et les 2 accessoires bonus). **Aucun handle touché.**
10. Reprendre les **libellés courts des vignettes du méga-menu** dans le thème brouillon
    (remplacement de `{{ closest.collection.title }}` par le libellé en dur).
11. **QA mobile 375 px** — jamais faite, et c'est le renommage qui la rend nécessaire.

**Phase 3 — flux Shopping**
12. Installer **« Google & YouTube »**, publier le catalogue sur le nouveau canal.
13. Régler **Titre du produit = « Titre SEO du produit »**.
14. **Laisser la description sur « description par défaut »** (piège « Livraison offerte », §1).
15. Contrôler les refus dans Merchant Center, puis n'ouvrir la **source supplémentaire**
    (`id` + `title`) que pour les fiches réellement problématiques.

**Ce qu'on ne fait pas, et c'est délibéré**
- On ne renomme **aucun produit** : les noms français sont l'actif de marque.
- On ne change **aucun handle** : 0 redirection, 0 lien mort, configurateur intact.
- On n'écrit **aucune marque tierce** nulle part, ni en flux ni en page.
- On ne prétend pas capter la grappe `arabic dial` (≈ 15 500) par le nommage : elle est
  intégralement adossée au mot « seiko », qui est interdit sur la page d'arrivée.

---

## 6. Ce qui reste à vérifier — la liste honnête

1. **Présence de l'app « Google & YouTube » dans l'admin** — établie par l'absence de publication,
   pas par `appInstallations` (accès refusé au jeton).
2. **Statut réel du paiement** — non lisible par l'API.
3. **Clés `mm-google-shopping` encore consommées en 2026** — Shopify ne publie aucune liste
   officielle ; sans objet tant qu'on ne cherche pas de surcharge par métachamp.
4. **Migration Content API → « Shopify App API »** côté Merchant Center : des sources tierces
   signalent que règles et sources supplémentaires, liées à l'ID de la source, cessent d'agir après
   migration. **Aucune doc officielle Google ou Shopify ne le confirme.** À contrôler dans le compte
   une fois le canal branché.
5. **Volumes non mesurés et jamais estimés ici** : « montre de plongée », « montre de plongée
   automatique », « montre chronographe homme », « montre GMT », « rouleau de voyage montre »,
   « montre automatique fond verre ». À passer sur SEMrush avant d'arbitrer définitivement les
   titres de `plongeuses` et de `chronos`.

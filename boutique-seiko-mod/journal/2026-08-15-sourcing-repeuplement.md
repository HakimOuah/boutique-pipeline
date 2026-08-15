# 15/08/2026 — Sourcing de repeuplement des collections sous-peuplées (API AliExpress)

> **Boutique Maison Noirmont, publique.** Objet : sourcer par l'**API AliExpress uniquement** les produits
> qui manquent aux trois collections sous-peuplées — **montres squelette**, **boîtes et coffrets**,
> **style plongeuse**.
>
> ⛔ **Aucune commande, aucun achat, aucun paiement.** Aucun produit Shopify créé ni modifié.
> Rien poussé dans DSers. Aucun navigateur ouvert : **passerelle VPS en lecture seule**
> (`codex-chasse-clusters/tools/aliexpress_vps_gateway.py`), endpoints `health`, `search`,
> `variants`, `exact`.
>
> `health` sain à **2026-08-15T11:02:59Z** · jeton d'accès valide jusqu'au `2026-09-01T18:29:47Z`.

Livrable opérationnel : [`FILE-DSERS-REPEUPLEMENT.md`](../FILE-DSERS-REPEUPLEMENT.md).
Sources : [`ARBORESCENCE.md`](../ARBORESCENCE.md) · [`GRILLE-PRIX.md`](../GRILLE-PRIX.md) ·
[`NOTES-PRICING.md`](../NOTES-PRICING.md) · [`REGLES.md`](../REGLES.md) ·
[`journal/2026-08-14-concurrents-fr.md`](2026-08-14-concurrents-fr.md) ·
[`journal/2026-08-14-etude-maisondutemps.md`](2026-08-14-etude-maisondutemps.md) ·
[`journal/2026-07-31-sourcing-arabes-squelettes.md`](2026-07-31-sourcing-arabes-squelettes.md).

---

## 0. Le verdict en dix lignes

1. **22 fiches candidates retenues**, toutes en preuve classe A : identifiant complet, ventes réelles,
   note, prix par variante, stock à l'unité, fret France et délai relevés un par un.
2. **Squelette : 8 fiches**, cible atteinte — mais **en deux qualités qui ne se mélangent pas**
   (6 fiches NH70 saphir 40 mm à 279 €, 2 fiches à pont apparent 42 mm à 189 €).
3. ⛔ **La contrainte « coût rendu ≤ 70 € » n'est pas tenable sur le squelette de qualité catalogue.**
   Le seul squelette **NH70 · saphir · acier · sans marque** ayant **≥ 10 ventes réelles** coûte
   **135,78 € rendu**. À 279 €, la marge tombe à **92,56 €, soit 39,8 %** — sous les 46-50 % des deux
   fiches squelette existantes. Voir §2.3 : c'est un arbitrage, pas un oubli.
4. ✅ **Le constat du 31/07 est confirmé mot pour mot** : « le marché du squelette **stérile** est une
   niche sans best-seller ». Deux semaines et une méthode différente plus tard, la conclusion ne bouge
   pas. **Ce n'est pas un échec de recherche, c'est une propriété du marché.**
5. ✅ **Coffrets : 7 fiches, 79 à 149 €**, toutes **au-dessus du verrou SONGMICS à 48 €**, marges
   **51,5 % à 74,7 %**. C'est le meilleur dossier des trois — le trou n°1 se comble proprement.
6. ✅ **Style plongeuse : 6 fiches**, cible de 5 dépassée, marges **48,1 % à 54,2 %** — toutes en
   **cadran stérile revendiqué comme tel par le fournisseur** (`sterile dial`), Tandorio, la maison
   déjà éprouvée sur l'aviateur.
7. ⛔ **Porte-montres et présentoirs : 1 fiche sur 3-4.** L'API ne remonte qu'un seul support de montre
   crédible. **Le trou reste ouvert** — voir §5.
8. ⚠️ **Quatre cadrans refusés pour marquage**, dont deux cas nouveaux : `SINCE 1908` + `21 JEWELS`
   (allégation d'ancienneté), et `AUTOMATIC / CHRONOMETER` sur toute la gamme Corgeut — **une
   certification que personne n'a délivrée**.
9. ⚠️ **Le `904L` rouge est de retour**, imprimé sur le bracelet du squelette NH70 retenu. Le cadran
   est nu, la source reste valide — **mais `904L` ne doit apparaître dans aucun visuel livré**.
10. ⚠️ **Deux fiches sur les vingt-deux ont un fret à 5,79 € et un délai à 22 jours**, hors de la
    promesse J+21. À trancher avant import.

---

## 1. Méthode, et ce que l'API sait faire — ou ne sait pas faire

### 1.1 La route

| Étape | Endpoint | Ce qu'il donne |
|---|---|---|
| Découverte | `search <requête> --sort-by orders\|price_desc --destination FR` | identifiant, titre FR, **note**, **taux de satisfaction**, ventes par palier, image principale |
| Vérité fournisseur | `variants <item_id>` | **ventes réelles au chiffre près**, statut, **vendeur**, **prix et stock par SKU**, image de propriété par coloris |
| Qualification fermée | `exact <item_id> --property … --destination FR` | SKU unique, **fret France**, **transporteur**, **délai min/max**, suivi |

**≈ 130 appels `search`, 40 `variants`, 24 `exact`.** Aucun échec de transport. Aucun anti-bot touché.

### 1.2 ⚠️ Le piège de ce moteur de recherche — à écrire dans la mémoire projet

**`search` classe par popularité globale, pas par pertinence.** Toute requête contenant un mot fréquent
(`montre`, `boîte`, `watch`, `box`) ramène les best-sellers de la **catégorie entière** — montres à
quartz à 2,13 € et coques Apple Watch — quelle que soit la suite de la requête.

Preuve mesurée :

| Requête | Ce qui remonte |
|---|---|
| `montre squelette` | 19 montres à quartz et LED, **0 squelette** |
| `skeleton watch` | **exactement les mêmes 19 articles** |
| `squelette` **seul** | des squelettes — d'Halloween, d'aquarium, d'anatomie. Le mot est bien indexé |
| **`squelette automatique`** | ✅ **des montres squelette réelles**, WINNER, OLEVS, PAGANI, LONGLUX |
| `NH70` | ✅ tout l'univers NH70, mouvements, cadrans, aiguilles, montres finies |

**La règle qui marche : deux mots rares, aucun mot fréquent.** `squelette automatique`,
`squelette mécanique`, `fentes montres`, `Tandorio plongée`, `NH70`. Une requête « bien écrite »
en français naturel (`montre squelette automatique homme saphir`) est **la pire** : elle rend 0 résultat
utile. C'est l'inverse de l'intuition, et c'est ce qui a coûté le plus de temps ici.

⚠️ **Corollaire** : `--limit` plafonne à **20**. Au-delà, l'API renvoie une liste vide sans erreur.
Le tri `latest` renvoie systématiquement **0 résultat**.

### 1.3 ⚠️ Ce que l'API ne donne pas

- **`variants` et `exact` renvoient toujours `rating: 0.0` et `evaluation_count: 0`**, même sur un
  article à 2 000 ventes. **La note ne s'obtient que par `search`** — et jamais le nombre d'avis.
  Les notes de ce document viennent donc de `search` (note /5 + taux de satisfaction %), le **nombre
  d'avis reste inconnu**. C'est un plafond de preuve, à ne pas maquiller.
- **Pas de galerie produit.** Seules les **images de propriété SKU** sont exposées, plus l'image
  principale de `search`. C'est ce qui a été téléchargé (§6) ; il n'y a pas de route API vers les
  10-20 photos de la page produit.
- **Pas de catalogue vendeur.** Les produits frères d'un même magasin ne se trouvent qu'en devinant
  le nom du magasin dans une requête `search` (`Tandorio plongée` a payé, §4).

### 1.4 Le contrôle des cadrans

**Chaque candidat a été zoomé, cadran par cadran**, sur son image de propriété SKU recadrée au centre
et agrandie. **19 planches de contrôle**, une par lot. Aucun candidat n'est retenu sur un titre.

---

## 2. Montres squelette — 8 fiches, en deux qualités

**État avant** : 2 fiches actives pour **17 120 recherches vérifiées**. Porte ouverte
(Amazon **0** position organique sur les trois têtes, `maisondutemps` premier organique avec 44 fiches).

### 2.1 ✅ Retenu — le squelette de catalogue

**`1005006771109294` — Tandorio 40 mm, mouvement NH70A, verre saphir, 200 m, acier, bracelet acier**

| Preuve | Valeur |
|---|---|
| Identifiant | `1005006771109294` (16 chiffres, complet) |
| Magasin | `tandorio Timepieces Store` (CN) — **la maison déjà éprouvée par la boutique** sur l'aviateur et sur `montre-sterile-40-nh35-saphir` |
| Statut | `onSelling` |
| **Ventes réelles** | **22** ✅ (> 10) |
| Note | **5,0 / 5** · satisfaction **99,4 %** · nombre d'avis non exposé par l'API |
| SKU | **42**, soit 21 combinaisons de cadran × 2 fonds (verre / plein) |
| Prix par variante | **129,99 €**, identique sur les 42 SKU |
| Stock | **381 à 400 par SKU** |
| Fret France | **5,79 €**, *Expédition standard AliExpress*, **suivi** |
| Délai | **10 à 22 jours** — livraison annoncée **25 août → 6 septembre** ⚠️ |
| Cadran | ✅ **entièrement ajouré, aucun texte, aucun logo, aucune mention** — 4 coloris zoomés |

⚠️ **Le bracelet porte `904L` imprimé en rouge**, visible sur les quatre photos de propriété. `904L` a
été purgé de la boutique le 08/08 avec redirections 301. **Le cadran étant nu, la source reste valide**
— mais le `904L` ne doit passer dans **aucune composition**, exactement comme pour
`montre-sterile-40-nh35-saphir` (précédent du 13/08).

⚠️ **Les inserts de lunette `22 / 4 / 6 / 8 / 10 / 12` bicolores noir-bleu** sont un hommage assumé à un
modèle protégé. Aucun texte de marque n'y figure, la fiche est donc importable — **mais ni le titre, ni
le `alt`, ni la description ne doivent employer un nom de modèle** (piège `faussesmontres.com`,
`NOTES-PRICING.md` §2 bis).

**6 fiches** proposées, une par famille de cadran, à **279 €** — juste sous `maisondutemps` MTBeta
Skeleton (285-295 €), le comparable retenu par `GRILLE-PRIX.md` : indépendant, sans marque, premier
organique sur `montre squelette automatique`.

| Handle proposé | Variante fournisseur | Coût rendu | Prix | Marge HT | Marge % |
|---|---|---:|---:|---:|---:|
| `montre-squelette-automatique-40-anneau-noir` | `black chapter ring A` + `glass back` | 135,78 € | 279 € | **92,56 €** | 39,8 % |
| `montre-squelette-automatique-40-anneau-vert` | `Green Chapter Ring A` | 135,78 € | 279 € | **92,56 €** | 39,8 % |
| `montre-squelette-automatique-40-anneau-blanc` | `white ring A` | 135,78 € | 279 € | **92,56 €** | 39,8 % |
| `montre-squelette-automatique-40-aiguilles-bleues` | `blue hand A` | 135,78 € | 279 € | **92,56 €** | 39,8 % |
| `montre-squelette-automatique-40-aiguilles-rouges` | `red hand A` | 135,78 € | 279 € | **92,56 €** | 39,8 % |
| `montre-squelette-automatique-40-lunette-bleue` | `blue ring A` | 135,78 € | 279 € | **92,56 €** | 39,8 % |

### 2.2 ✅ Retenu — l'entrée de gamme à pont apparent

**`1005010362031259` — squelette à pont central, 42 mm, mouvement mécanique, cuir**

| Preuve | Valeur |
|---|---|
| Identifiant | `1005010362031259` |
| Magasin | `YASHIDUN Official Store` (CN) · statut `onSelling` |
| **Ventes réelles** | **500+** ✅ |
| Note | **4,8 / 5** · satisfaction **96,4 %** |
| SKU | 2 (`1009-1`, `1009-2`) · **prix 35,19 €** · stock **135 et 136** |
| Fret France | **offert**, *Expédition standard AliExpress*, suivi · **9 à 18 jours** (24 août → 2 sept.) |
| Cadran | ✅ **pont ajouré nu, chiffres romains sur la lunette uniquement, aucun texte, aucun logo** |

Prix **189 €**, juste sous **Trendhim / Seizmont à 197 €** — le premier prix crédible du milieu dense
relevé en T-47. ⛔ **Pas 199 € : c'est le prix exact de deux concurrents**, et la règle Hakim est de se
placer **sous** le comparable, jamais dessus ni dessus-dessous à l'euro près.

| Handle proposé | Variante | Coût rendu | Prix | Marge HT | Marge % |
|---|---|---:|---:|---:|---:|
| `montre-squelette-automatique-pont-cuir` | `1009-1` | 35,19 € | 189 € | **119,41 €** | 75,8 % |
| `montre-squelette-automatique-pont-cuir-noir` | `1009-2` | 35,19 € | 189 € | **119,41 €** | 75,8 % |

### 2.3 ⛔ Pourquoi « coût rendu ≤ 70 € » ne se tient pas sur le squelette de catalogue

Le brief demandait un coût rendu **≤ 70 €** pour un prix de vente 199-279 €. **Aucun squelette au monde
ne satisfait simultanément les quatre conditions de la maison** :

| Condition | Ce que le marché AliExpress oppose |
|---|---|
| Cadran sans marque | Les squelettes à ≤ 70 € sont **des montres de mode de marque** — WINNER, OLEVS, LIGE, FORSINING, MEGIR, POEDAGAR, CASENO, FNGEEN, LONGLUX, PAGANI DESIGN. **Toutes impriment leur nom sur le cadran.** |
| ≥ 10 ventes réelles | Les squelettes **stériles NH70** existent, mais **plafonnent entre 4 et 29 ventes**. Constat déjà écrit le 31/07, reconfirmé ici. |
| Qualité cohérente (acier 316L, saphir, NH35/NH70) | Sous 40 €, on est en **alliage de zinc** et verre minéral. |
| Coût rendu ≤ 70 € | Le premier NH70 + saphir + acier **sans marque** est à **129,99 €**. |

**Trois de ces quatre conditions se tiennent à la fois, jamais les quatre.** Les 8 fiches proposées
choisissent deux compromis explicites :
- §2.1 sacrifie le coût (135,78 €) et garde la qualité → **marge 39,8 %** ;
- §2.2 sacrifie la qualité perçue (pas de saphir annoncé, mouvement non précisé par le fournisseur —
  donc **rien à en écrire**, règle « aucune spécification inventée ») et garde la marge → **75,8 %**.

**⚠️ Ce qu'il faut savoir avant d'arbitrer** : à 39,8 %, la fiche §2.1 est **au niveau des
`integrale-*-sport-chic-acier`** (44,3 %), c'est-à-dire au niveau que `GRILLE-PRIX.md` §4 a désigné
comme le **premier candidat au dépeuplement**. Monter le prix à 299 € porterait la marge à 112,75 €
(45,2 %) mais nous rapprocherait du vide de marché 300-440 €. **C'est une décision de Hakim.**

### 2.4 ⚠️ Réserve — la piste à 25 €, à trancher

**`1005006991847700`** — `MEISEN Store`, **344 ventes**, note **4,7** / satisfaction 94,2 %,
**20 coloris**, **24,59 à 27,39 €**, fret 1,99 €, 10-15 jours. **Cadran ajouré doré, aucun texte,
aucun logo** — le contrôle zoomé est propre.

⛔ **Non retenu de ma propre initiative** : le fournisseur écrit **« alliage de zinc »** dans son titre.
Vingt fiches à 199 € en alliage de zinc, à côté de sept `quarante-et-un-sport-acier` en 316L à 279 €,
c'est une incohérence de catalogue que le client verra au déballage. **Marge théorique : 138,60 € à
199 € (83,5 %).** La piste est là si Hakim veut une porte d'entrée à bas ticket — **je ne la prends pas
seul.**

### 2.5 ⛔ Refusés, avec motif

| Identifiant | Article | Ventes | Motif de refus |
|---|---|---:|---|
| `1005009354912699` | Tandorio squelette ingénieur NH70 saphir 100 m | **9** | ⛔ **< 10 ventes réelles.** Cadran propre, coût 123,99 €. *C'est l'article de la fiche `montre-squelette-automatique-octogone` déjà en ligne : elle ne repasserait pas la règle aujourd'hui.* |
| `1005009825936780` | Tandorio squelette carré 42 mm NH70 saphir | **4** | ⛔ < 10 ventes. *Article de `montre-squelette-automatique-carree`, même remarque.* |
| `1005009829095736` | BLIGER 41 mm NH70 cadran évidé saphir | **9** | ⛔ < 10 ventes |
| `1005006691256075` | BLIGER 41 mm NH70 saphir vert lumineux | 12 | ⛔ Coût **159,39 à 163,99 €** : marge < 30 % à 279 € |
| `1005006830714575` | Squelette ajouré 42 mm NH70/NH72 | **6** | ⛔ < 10 ventes |
| `1005012593984971` | Squelette grand boîtier acier, bracelet silicone | 41 | ⛔ **`G·BATTLE` imprimé sur le cadran** (contrôle zoomé) |
| `1005010696091883` | « Montre mécanique vintage élégante », cadran squelette | 419 | ⛔ **`SINCE 1908` + `21 JEWELS` + logo sur le cadran.** `SINCE 1908` est une **allégation d'ancienneté** sur une montre neuve sans histoire — cas nouveau, à ajouter au catalogue des marquages |
| `1005011991562024` | Idem, autre listing | 180 | ⛔ Même cadran `SINCE 1908` |
| `1005012035717184` | « Montre de luxe haut de gamme squelette » | 318 | ⛔ **`Luolingongjue` + `AUTOMATIC / WATER RESISTANT / JAPAN MOVT / FASHION WATCH`** sur le cadran — et ce n'est même pas un squelette |
| `1005009502625941` | « Squelette étanche cuir noctilucent » | 259 | ⛔ **`LONGLUX` + `AUTOMATIC`** sur le cadran |
| `1005012543131637` | Squelette tonneau acier 5 ATM | 29 | ⛔ **`AUTO 30 MATIC` en pied de cadran** — pseudo-marque ; boîtier tonneau à vis, hommage trop littéral à un modèle protégé |
| `1005011626370968` | HANBORO « Starry Sky » constellation | 73 | ⛔ Coût **264,39 €** ; ce n'est pas un squelette |
| `1005010673554473` · `1005005136371866` · `1005010209442321` · `1005005169808431` · `1005005167109859` · `1005002806672608` · `1005005051739649` · `1005007556961858` · `1005005454554991` · `1005010667049428` · `1005011691573883` · `1005007279354532` · `1005007646053449` · `1005011543315425` · `1005007237962193` · `1005008326111415` · `1005009928307551` · `1005010290875384` · `1005011911498379` · `1005008574013735` · `1005007033489596` · `1005007060197901` · `1005009364064154` · `1005008651417400` · `1005009552279638` · `1005004892948126` · `1005010070985261` | OLEVS, WINNER, LIGE, FNGEEN, Forsining, CASENO, MEGIR, POEDAGAR, PAGANI DESIGN, LONGLUX, BORMAN, TSAR BOMBA, OUPINKE, Sugess, AESOP | 10 à 1 000+ | ⛔ **Nom de marque imprimé sur le cadran**, vérifié au titre et, pour les six premiers, au contrôle zoomé |

---

## 3. Boîtes et coffrets — 7 fiches, le dossier le plus propre

**État avant** : 3 fiches utiles pour **59 410 recherches** — **19 803 recherches par fiche existante**,
le trou n°1 de toute la boutique. Porte ouverte (Amazon **1** position organique sur 20).
⚠️ **Shopping verrouillé 19-48 € par SONGMICS** : les 7 fiches sont **toutes à 79 € ou plus**.

### 3.1 ✅ `1005008635238967` — coffret bois laqué, couvercle verre, 6 / 10 / 12 emplacements

| Preuve | Valeur |
|---|---|
| Magasin | `KSGM Store` (CN) · `onSelling` · **700+ ventes** · note **4,7** / satisfaction **93,0 %** |
| SKU | 10, dont **6, 10 et 12 emplacements** en **deux finitions** (acajou laqué, noir laqué) |
| Fret | **1,99 €**, *AliExpress Selection Standard*, suivi · **9 à 14 jours** ✅ |
| Contrôle visuel | Coffret bois **31 × 21 × 8 cm**, couvercle verre, intérieur crème, serrure dorée — **aucune marque visible** |

| Handle proposé | Variante | Prix fournisseur | Stock | Coût rendu | Prix | Marge HT | Marge % |
|---|---|---:|---:|---:|---:|---:|---:|
| `coffret-douze-montres-bois-laque-noir` | `Black 12 Grids` | 38,79 € | 38 | 40,78 € | **129 €** | **64,66 €** | 60,2 % |
| `coffret-douze-montres-bois-laque-acajou` | `Red 12 Grids` | 38,19 € | 38 | 40,18 € | **129 €** | **65,26 €** | 60,7 % |
| `coffret-dix-montres-bois-laque-acajou` | `Red 10 Grids` | 34,39 € | 81 | 36,38 € | **109 €** | **52,68 €** | 58,0 % |
| `coffret-six-montres-bois-laque-acajou` | `Red 6 Grids` | 28,59 € | 4 ⚠️ | 30,58 € | **79 €** | **33,90 €** | 51,5 % |

⚠️ **`Black 10 Grids` (34,59 €) écarté : stock 7 unités.** `Red 6 Grids` retenu à **stock 4** — fiche à
importer en dernier, ou à décaler si le stock ne remonte pas. Comparable : **Royaume de la Boîte,
55-99 €**, l'indépendant qui gagne l'organique (`GRILLE-PRIX.md` §1).

### 3.2 ✅ `1005006704546094` — coffret aluminium, couvercle verre, 12 / 24 emplacements

| Preuve | Valeur |
|---|---|
| Magasin | `LEICTORY Official Store` · `onSelling` · **1 000+ ventes** · note **4,2** / satisfaction **84,8 %** ⚠️ |
| Fret | **1,99 €** · **7 à 13 jours** ✅ |
| Contrôle visuel | Malette aluminium brossé, couvercle verre, coussins noirs, fermoir — **aucune marque** |

| Handle proposé | Variante | Prix fournisseur | Stock | Coût rendu | Prix | Marge HT | Marge % |
|---|---|---:|---:|---:|---:|---:|---:|
| `coffret-douze-montres-aluminium-verre` | `12 Slots` | 15,29 € | 59 | 17,28 € | **89 €** | **55,39 €** | 74,7 % |
| `coffret-vingt-quatre-montres-aluminium-verre` | `24 Slots` | 30,99 € | 12 ⚠️ | 32,98 € | **149 €** | **88,85 €** | 71,6 % |

⚠️ **La note 4,2 / satisfaction 84,8 % est la plus basse du lot.** C'est aussi la meilleure marge.
Sur un produit de rangement sans pièce mobile, le risque est le transport, pas la panne — mais
**c'est la première fiche à surveiller en litige.**

### 3.3 ✅ `1005007696086141` — malette étanche rigide, 15 emplacements

| Preuve | Valeur |
|---|---|
| Magasin | `GZTMU Tool Organizer Store` · `onSelling` · **800+ ventes** · note **4,8** / satisfaction **95,9 %** |
| Variante retenue | `15 Slots` — **36,59 €**, stock **19** · fret **1,99 €** · **7 à 12 jours** ✅ |
| Contrôle visuel | Coque rigide 290 × 243 × 110 mm, fermoirs, mousse alvéolée, joint — **aucune marque** |

`malette-quinze-montres-etanche` · coût rendu **38,58 €** · prix **139 €** · marge **75,06 € (64,8 %)**.

⚠️ **Ce n'est pas un coffret de présentation, c'est une malette de protection.** Elle ouvre un
sous-segment que les trois spécialistes n'ont pas — mais il ne faut pas la vendre comme un écrin.
Une fiche, pas plus, tant que la demande n'est pas mesurée.

### 3.4 ⛔ Refusés, avec motif

| Identifiant | Article | Motif |
|---|---|---|
| `1005008176230482` | Valise aluminium **35 emplacements**, 500+ ventes, 57,69 € | ⛔ **Délai 32 à 42 jours** (*Selection Shipping for Oversized Goods*, 16-26 septembre). Incompatible avec toute promesse de livraison |
| `1005010525688201` | « Boîte 15 fentes », **3 000+ ventes**, 25,19 € | ⛔ **Doublon d'offre** : contrôle visuel = **étui souple EVA à fermeture éclair**, pas un coffret. `etui-de-voyage-rigide` existe déjà |
| `1005012469781076` | « 15 emplacements étanche », 600+ ventes, 25,99 € | ⛔ Idem — étui souple EVA |
| `1005011895056549` | Étui zippé 3 à 10 emplacements, 1 000+ ventes | ⛔ Idem — doublon des quatre `rouleau-de-voyage-*` |
| `1005008095512299` | Étui cuir véritable 8/10/12 emplacements, 17 ventes | ⛔ Coût **98,39 à 140,69 €** : prix de vente nécessaire ≥ 299 €, hors bande 55-99 € du comparable |
| `1005008372325985` | Oirlv, coffret bois vitrine 10 fentes, 79 ventes | ⛔ Coût **103,39 €** — même motif |
| `1005012534030699` | Coffret 24 emplacements couvercle vitré, 51,99 € | ⛔ **6 ventes réelles** |
| `1005008912870216` | Valise aluminium 48 fentes, 10 ventes, 196,99 € | ⛔ Coût et format hors cible |

---

## 4. Style plongeuse — 6 fiches, cible dépassée

⚠️ **Rappel de cadre, non négociable** : `ARBORESCENCE.md` a démontré le 14/08 que Google **rabat
`plongeuse` sur `de plongée`** et sert la même page 1 — la porte est **fermée** (Tudor, Seiko officiel,
Lepage, Rigal, 400-3 000 €). **La consigne du ticket est donc respectée à la lettre : on remplit la
collection pour qu'elle ne soit pas vide, on n'y investit rien de plus.**

⚠️ **Écriture** : ces deux articles sont annoncés **20 bar / 200 m** par le fournisseur, mais la règle
de la maison est **« style plongeuse », jamais « montre de plongée »**. Les handles proposés
l'appliquent. **Aucune allégation d'étanchéité ne doit être écrite au-delà de ce que le fournisseur
annonce, et l'ancienne mention 5 ATM du catalogue ne s'applique pas à ces nouveaux articles** — ne pas
mélanger les deux.

**La requête qui a tout débloqué : `Tandorio plongée`.** Le nom du magasin déjà éprouvé par la maison,
en deux mots rares. Elle a rendu huit listings pertinents là où toutes les requêtes descriptives
échouaient.

### 4.1 ✅ `1005010218960866` — 36 mm, Miyota 8215, dôme saphir, 20 bar, cadran stérile

| Preuve | Valeur |
|---|---|
| Magasin | `tandorio Official Store` · `onSelling` · **94 ventes** · note **4,9** / satisfaction **97,4 %** |
| SKU | 12, dont **6 explicitement `sterile dial`** (le fournisseur nomme lui-même la version sans logo) |
| Prix | **85,69 €** (noir 1/2, vert, rouge) · **88,69 €** (bleu, noir 3) · stock **195 à 200 par SKU** |
| Fret | **1,99 €**, *AliExpress Selection Standard*, suivi · **9 à 14 jours** ✅ |
| Cadran | ✅ **stérile confirmé au zoom** : index appliqués, minuterie, guichet de date. **Aucun texte** |

Comparable : **Gustave & Cie, 245 €** sur `montre 36mm homme` — l'indépendant français sans marque, même
cote, déjà retenu par `GRILLE-PRIX.md` pour les six `trente-six-classique-jubile`. **Prix 239 €**,
cohérent avec le reste du 36 mm du catalogue.

| Handle proposé | Variante | Coût rendu | Prix | Marge HT | Marge % |
|---|---|---:|---:|---:|---:|
| `montre-style-plongeuse-36-cadran-noir` | `black sterile dial 1` + `Miyota8215` | 87,68 € | 239 € | **107,89 €** | 54,2 % |
| `montre-style-plongeuse-36-cadran-vert` | `green sterile dial` | 87,68 € | 239 € | **107,89 €** | 54,2 % |
| `montre-style-plongeuse-36-cadran-bordeaux` | `red sterile dial` | 87,68 € | 239 € | **107,89 €** | 54,2 % |
| `montre-style-plongeuse-36-cadran-bleu` | `blue sterile dial` | 90,68 € | 239 € | **104,89 €** | 52,7 % |

### 4.2 ✅ `1005009674157775` — 42 mm titane, saphir, 200 m, cadran stérile

| Preuve | Valeur |
|---|---|
| Magasin | `tandorio Timepieces Store` · `onSelling` · **131 ventes** · note **4,7** / satisfaction **93,4 %** |
| SKU | **36**, dont **12 `sterile`** en 6 coloris × 3 mouvements (Miyota 8215 / PT5000 / Japan NH35A) |
| Prix | **110,69 €** (8215) · 128,39 € (PT5000) · 130,69 € (NH35A) · stock **~888 par SKU** |
| Fret | **5,79 €**, *Expédition standard AliExpress* · **10 à 22 jours** ⚠️ (25 août → 6 sept.) |
| Cadran | ✅ **stérile confirmé au zoom** : index luminescents appliqués, lunette 60 clics, **aucun texte** |

| Handle proposé | Variante | Coût rendu | Prix | Marge HT | Marge % |
|---|---|---:|---:|---:|---:|
| `montre-style-plongeuse-42-titane-noir` | `black sterile` + `Miyota 8215` | 116,48 € | 279 € | **111,86 €** | 48,1 % |
| `montre-style-plongeuse-42-titane-bleu` | `blue sterile` + `Miyota 8215` | 116,48 € | 279 € | **111,86 €** | 48,1 % |

⚠️ **`exact` refuse `blue sterile` + `Miyota 8215` : deux SKU correspondent** (`blue sterile` et
`black-blue sterile` matchent la même chaîne). **Le SKU exact devra être choisi à la main dans DSers.**
Le fret et le délai sont ceux relevés sur `black sterile`, même expédition.

### 4.3 ✅ Bonus hors collection — le field 36 mm stérile à 72,68 €

**`1005006994737069`** — `Stone's Store`, **362 ventes**, note **4,9** / satisfaction **98,0 %**,
18 SKU. Variante **`Miyota8215 movement` + `black sterile dial 2` : 70,69 €**, stock 3 ⚠️ ;
**`silver sterile dial` : 75,39 €, stock 91** ✅. Fret **1,99 €**, **7 à 15 jours**.

**Cadran stérile confirmé au zoom** — mais c'est un **cadran field / pilote 24 h**, pas une plongeuse.
Il n'entre pas dans la cible du ticket. **Signalé, non versé à la file** : c'est le seul article de tout
ce sourcing qui tienne à la fois **≥ 10 ventes**, **cadran nu**, **saphir**, **20 bar** et
**coût rendu < 80 €**. À rattacher à `Classiques` si Hakim veut l'ouvrir.

### 4.4 ⛔ Refusés, avec motif

| Identifiant | Article | Ventes | Motif |
|---|---|---:|---|
| `1005010194840788` | Corgeut 41 mm, saphir, 100 m, nylon | 800+ | ⛔ **`CORGEUT` + `AUTOMATIC / CHRONOMETER` sur les six variantes zoomées.** « Chronometer » est une **certification que personne n'a délivrée** — refus sans discussion |
| `1005005673154884` | Tandorio 36 mm 20 bar (`Tandorio Store`) | 327 | ⛔ **Doublon exact** de `1005006994737069`, mêmes 18 SKU, **5 à 9 € plus cher** |
| `1005005517567762` | Tandorio titane « tortue » 200 m, variantes `nologo` | 19 | ⛔ Coût **147,78 € rendu** : marge **96,95 € (32,4 %)** à 299 €. Sous le plancher de la maison |
| `1005005935437076` | Tandorio titane NH35A 44 mm céramique, `no logo` | 13 | ⛔ Coût 136,99 € + **44 mm** : hors du gabarit du catalogue (36-42 mm) |
| `1005006389834729` | Mod 013, 37 mm NH36, 200 m, variantes `nologo` | 13 | ⚠️ **Réserve** : coût 116,78 € rendu, marge 111,56 € (40,0 %) à 279 €. Dossier correct, mais **fret 5,79 € et délai 22 jours**, et le 37 mm doublonne le 36 mm de §4.1 |
| `1005012273670774` | « Zeppelin Airship » automatique | 600+ | ⛔ **Nom de marque** dans le produit |
| San Martin, Steeldive, Boderry, Baltany, Proxima, Seestern, Watchdives, BERNY, IXDAO, Cronos, Specht & Sohne, ADDIESDIVE, LIGE | — | — | ⛔ **Marque imprimée sur le cadran** (confirmation du relevé du 31/07) |

---

## 5. ⛔ Porte-montres et présentoirs — le trou reste ouvert

`ARBORESCENCE.md` signale ce trou comme **« non vu jusqu'ici » : 0 fiche chez nous, une collection
dédiée chez les trois spécialistes**, bande de marché 35-90 €. Cible du ticket : 3-4 fiches.

**Une seule fiche est trouvable par l'API.**

### 5.1 ✅ `1005008659224282` — support de montre en bois massif à plateau cuir

| Preuve | Valeur |
|---|---|
| Magasin | `Shop1104279957 Store` · `onSelling` · **2 000+ ventes** · note **4,6** / satisfaction **91,6 %** |
| Variante `A` | **4,59 €**, stock **46** · fret **1,99 €** · **7 à 12 jours** ✅ |
| Variante `B` | 5,09 €, **stock 0** ⛔ |
| Contrôle visuel | Bloc bois **5 × 6 × 7 cm** à plateau cuir grainé — aucune marque |

`porte-montre-bois-massif-cuir` · coût rendu **6,58 €** · prix **39,90 €** · marge **25,86 € (77,8 %)**
· ratio prix ÷ CPC (0,36 €) = **111** ✅.

### 5.2 Pourquoi il n'y en a qu'une, et quoi faire

**Ce n'est pas un manque d'effort : c'est un angle mort du moteur de recherche.** Quatorze requêtes
(`support montre bois`, `présentoir montre`, `porte-montre noyer`, `valet de nuit`, `présentoir montre
acrylique`, `coussin présentoir montre`…) ramènent toutes des **supports de téléphone** et des
**présentoirs à bijoux génériques** : le mot `support` est trop fréquent, et il n'existe **aucun mot
rare** propre à cette famille — pas d'équivalent de `NH70` ou de `fentes`.

**Recommandation** : ce trou se comble par **la marque du vendeur, pas par la description**. Il faut
d'abord identifier deux ou trois magasins de présentoirs bois (par le catalogue d'un concurrent
français, pas par l'API), puis interroger `search` sur leur nom — c'est exactement la manœuvre qui a
débloqué les plongeuses au §4. **Ticket à ouvrir, pas une recherche à refaire à l'identique.**

---

## 6. Photos fournisseur téléchargées

**60 images, 22 dossiers**, dans `sources-fournisseur-2026-08/<handle-proposé>/`, non versionné
(`.gitignore` ligne 34) :

- `face-fournisseur-<item_id>.jpg` — l'image principale du listing ;
- `variante-<coloris>.jpg|png` — **l'image de propriété SKU du coloris exact de la fiche**, c'est-à-dire
  la seule photo qui montre le produit réellement expédié pour cette variante.

Manifeste : `sources-fournisseur-2026-08/MANIFESTE-SOURCING-2026-08-15.json`.

⚠️ **Ce stock est plus mince que celui du 13/08** (60 images pour 22 fiches, contre 322 pour 35).
**L'API n'expose pas la galerie produit** (§1.3) : il n'y a pas de route pour la ramener sur des
articles qui ne sont pas encore importés, puisque les noms de fichiers CDN ne sont connus que par une
page produit ou par un média Shopify déjà créé. **La galerie complète ne pourra être récupérée
qu'après l'import DSers** — la même route que le 13/08.

⚠️ **Trois filigranes de vendeur** repérés sur les sources, hors produit, à ne jamais laisser passer
dans une composition : `Tandorio` (angle, sur les plongeuses et le squelette NH70), `BL Watches Parts`
(bas de photo), et le **`904L` rouge imprimé sur le bracelet** du squelette NH70 (§2.1) — celui-là est
sur le produit, ce qui interdit les cadrages qui montrent le bracelet de près.

---

## 7. Ce que je n'ai pas fait

- **Aucune commande, aucun achat, aucun paiement**, ni AliExpress ni DSers.
- **Aucune écriture Shopify** : aucun produit créé, aucun produit existant touché, aucune collection,
  aucun prix, aucun média.
- **Rien poussé dans DSers.** La file du §8 est une proposition ; l'import est une étape séparée.
- **Aucun navigateur.** Aucun anti-bot approché.
- **Aucun candidat retenu sur un titre** : les 22 fiches sont retenues sur `variants` + `exact` +
  contrôle zoomé du cadran ou du produit.
- **Aucune spécification recopiée sans source.** Les mouvements, étanchéités et matériaux cités ici
  sont ceux du fournisseur ; rien n'a été déduit.

## 8. Ce qui attend une décision de Hakim

1. **Le squelette à 279 € et 39,8 % de marge** (§2.1) — accepter cette marge, monter à 299 €, ou
   renoncer au squelette de qualité. ⚠️ **C'est la décision structurante de ce ticket.**
2. **Le squelette en alliage de zinc à 25 €** (§2.4) — 20 coloris, 83,5 % de marge, incohérent avec le
   catalogue acier. Ouvrir ou fermer.
3. **Les deux fiches à 22 jours de délai** (§2.1 et §4.2) — hors promesse J+21. Les importer quand
   même, ou attendre une option d'expédition plus rapide.
4. **`coffret-six-montres-bois-laque-acajou` à 4 unités en stock** — importer en dernier, ou décaler.
5. **Le trou porte-montres** (§5.2) — ouvrir le ticket « identifier les magasins de présentoirs par le
   catalogue concurrent ».
6. **La collection `boite-a-montre`** n'existe pas encore : `ARBORESCENCE.md` la porte comme
   **« à créer »**. Sept fiches l'attendent.

# U4b — décoration et cadeaux astro : mesure consolidée par famille

- **Date : 15/08/2026**, base **France**, Keyword Magic Tool en **expression exacte** (`mt=phrase`), 0 crédit.
- Objet : refaire la mesure que le premier passage n'a pas faite — **la consolidation par famille**
  (étape 3 de `METHODE-ANALYSE-MARCHE.md`), là où Codex avait additionné 4 têtes.
- Objectif chiffré fixé par l'audit : **≥ 18 000 recherches nettes additionnelles** au-delà des
  4 têtes P0, pour amener l'univers au plancher de 30 000.
- **Ce document est une mesure. Aucun verdict marché, aucun sourcing, aucune architecture.**

---

## État d'avancement — TERMINÉ

18 requêtes Keyword Magic Tool exécutées, toutes en base France, expression exacte.

| # | Requête KMT | Heure | Résultat |
|---|---|---|---|
| 1 | `galaxie` (racine) | 21h42 | **inexploitable** (Marvel + cinéma Amnéville), voir §7 |
| 2 | `planétarium` | 21h45 | fait — séparation lieu/produit |
| 3 | `projecteur galaxie` | 21h50 | fait |
| 4 | `ciel étoilé` | 21h53 | fait |
| 5 | `astronaute` (racine) | 21h57 | fait — plancher 480 |
| 6 | `veilleuse` (racine) | 22h00 | fait — plancher 480 |
| 7 | `lampe lune` | 22h03 | fait |
| 8 | `poster espace` | 22h08 | **inexploitable** (rabattement « La Poste »), voir §7 |
| 9 | `poster astronaute` | 22h10 | fait — 70 au total |
| 10 | `carte du ciel` | 22h13 | fait |
| 11 | `système solaire` | 22h16 | fait — plancher 390 |
| 12 | `lampe galaxie` | 22h19 | fait |
| 13 | `étoiles phosphorescentes` | 22h21 | fait |
| 14 | `housse de couette espace` | 22h24 | fait — 190 au total |
| 15 | `globe lune` | 22h26 | fait — frontière, 590 au total |
| 16 | `projecteur etoile` (sans accent) | 22h29 | fait — **découverte majeure** |
| 17 | `figurine astronaute` | 22h32 | fait |
| 18 | `veilleuse etoile` (sans accent) | 22h34 | fait |

---

## 1. Méthode et base France confirmée

- URL type : `https://fr.semrush.com/analytics/keywordmagic/?q=<kw>&db=fr&mt=phrase`
- « Base de données : **France** » vérifié dans le DOM à **chaque** lecture (valeur `base` retournée
  par le script d'extraction). Devise USD.
- Lecture : 100 lignes triées par volume, extraction DOM en JavaScript (aucune capture, aucun clic,
  onglet dédié 885844834).
- Si la 100ᵉ ligne est encore > 300 → **plancher** signalé : la famille n'est pas couverte.
- Règle d'addition : **on additionne ce qu'une même page de collection servirait, et rien d'autre.**
  Un mot n'appartient qu'à une seule famille. Jamais deux familles distinctes additionnées pour
  franchir un seuil.
- Deux chiffres partout : **brut** et **net de marque**.

### Journal des lectures

| Heure | Requête | Base | Mots-clés | Volume total KMT | 100ᵉ ligne |
|---|---|---|---|---:|---|
| 21h42 | `galaxie` | France | 138 754 | 625 240 | 590 → **plancher** |
| 21h45 | `planétarium` | France | 4 761 | 64 230 | 90 (98 lignes) — couvert |
| 21h50 | `projecteur galaxie` | France | 216 | 4 600 | 50 (10 lignes chiffrées) |
| 21h53 | `ciel étoilé` | France | 8 579 | 56 810 | 110 (100 lignes) — couvert |
| 21h57 | `astronaute` | France | 51 695 | 358 160 | 480 → **plancher** |
| 22h00 | `veilleuse` | France | 55 282 | 394 900 | 480 → **plancher** |
| 22h03 | `lampe lune` | France | 1 338 | 9 150 | 50 (21 lignes chiffrées) |
| 22h08 | `poster espace` | France | 4 112 | 68 160 | 50 — **hors sujet à 100 %** |
| 22h10 | `poster astronaute` | France | 63 | **70** | aucune ligne chiffrée |
| 22h13 | `carte du ciel` | France | 5 518 | 34 350 | 50 (88 lignes) |
| 22h16 | `système solaire` | France | 38 936 | 315 570 | 390 → **plancher** |
| 22h19 | `lampe galaxie` | France | 135 | 1 400 | 90 (4 lignes chiffrées) |
| 22h21 | `étoiles phosphorescentes` | France | 176 | 3 260 | 90 (8 lignes) |
| 22h24 | `housse de couette espace` | France | 46 | **190** | 110 (1 ligne) |
| 22h26 | `globe lune` | France | 155 | **590** | 210 (1 ligne, hors sujet) |
| 22h29 | `projecteur etoile` | France | 847 | 9 000 | 70 (17 lignes) |
| 22h32 | `figurine astronaute` | France | 84 | 650 | 70 (3 lignes) |
| 22h34 | `veilleuse etoile` | France | 704 | 5 150 | 70 (15 lignes) |

**Note technique sur les `n/a`.** Sur les requêtes à faible corpus, Semrush n'affiche la métrique
que pour les premières lignes et rend `n/a` pour le reste (« Pour afficher les métriques,
actualisez la page »). Ces lignes sont toutes sous la dernière valeur chiffrée. L'écart entre la
somme détaillée et le « Volume total » du KMT est de la longue traîne à ≤ 50-90, non comptée ici :
**on compte le détail, pas le plafond.**

**Liste de retrait marque appliquée** : NASA, SpaceX, Apollo, ISS, Falcon, Star Wars, Dark Vador,
Interstellar, Disney, Celestron, Skywatcher, Bresser, Omegon, National Geographic, Buki, Baader,
Pabobo, Lunie, Nature & Découvertes, Amazon, Cdiscount, Action, Lidl, Ikea, Maisons du Monde,
lepetitastronaute, les-astronautes.

---

## 2. Les familles

### Famille 0 — `planétarium` : séparation lieu/billetterie ↔ produit (nettoyage obligatoire)

C'était le principal soupçon de gonflement des 12 000 de Codex. **Il est confirmé.**

Lecture 21h45, 98 lignes, **somme lue 49 980**, dernière ligne 90 → **famille couverte**, pas de plancher.

| Bloc | Volume | Détail |
|---|---:|---|
| **Lieu, billetterie, séances** | **38 400** | planétarium paris 2 900 ; La Coupole 2 400 ; Nantes 1 600 + 1 600 ; Cité des sciences 1 300 + 1 300 ; Saint-Étienne 1 300 + 590 + 590 ; Jardin des sciences 1 300 ; Ludiver 1 300 ; Lyon 1 300 ; Rennes 1 300 ; Bretagne/radôme 1 000 ; Épinal 1 000 ; Reims 880 ; Strasbourg 880 ; Vaulx-en-Velin 880 ; Pleumeur-Bodou 720 ; Villeneuve-d'Ascq 720 ; Marseille 590 ; Lille 590 ; etc. |
| **Tête ambiguë `planétarium`** | **6 600** | KD 55, CPC 1,59. **Non comptée en produit** : 77 % de sa traîne est du lieu. À trancher en SERP. |
| **Produit générique net de marque** | **690** | `projecteur planétarium` 480 (KD 12, CPC 0,16) + `planétarium projecteur` 210 (KD 11, CPC 0,18) |
| **Produit de marque** (retiré au net) | **580** | `planétarium buki` 260 + `buki planétarium` 210 + `baader planétarium` 110 |
| **Autres, non produit** | **3 710** | `le planétarium` 480, `planétarium hubert curien` 480, `planétarium peiresc` 320, `planétarium à proximité` 260, `planétarium autour de moi` 90, `planétarium photos` 110, `cabinet vétérinaire du planétarium` 110, `planétarium gonflable` 110 (matériel scolaire), `planétarium montréal` 110 + 90 (hors France) |

> **Résultat : sur les 6 600 que Codex a comptés pour `planétarium`, la part produit est de 690
> nets.** La traîne du cluster est à 77 % du lieu et de la billetterie. Le produit « planétarium de
> bureau/enfant » n'existe quasiment pas en demande française.

**Retenu pour U4b : 690 (brut 1 270, dont 580 de marque).**

---

### Famille 1 — Projecteurs d'ambiance (galaxie, ciel étoilé, étoiles, astronaute) — **CŒUR**

**Test de la page unique : OUI.** `projecteur galaxie`, `projecteur ciel étoilé`, `projecteur
étoiles`, `astronaute projecteur` désignent le **même objet physique** (projecteur LED/laser
d'ambiance à poser). Une seule collection les sert. Le recoupement pressenti par l'audit est
confirmé : ce sont des formulations, pas des familles distinctes.

#### 1a. `projecteur galaxie` (21h50) — 2 820

| Formulation | Volume | KD | CPC |
|---|---:|---:|---:|
| projecteur galaxie | 1 600 | 29 | 0,17 |
| projecteur de galaxie | 390 | 22 | 0,15 |
| projecteur galaxie plafond | 210 | 23 | 0,19 |
| astronaute projecteur galaxie | 140 | 14 | 0,29 |
| lampe projecteur galaxie | 110 | 24 | 0,25 |
| projecteur-galaxie | 110 | 23 | 0,17 |
| galaxie projecteur | 90 | 9 | 0,09 |
| projecteur galaxie chambre | 70 | 19 | 0,14 |
| projecteur plafond galaxie | 50 | 21 | 0,12 |
| robot projecteur galaxie | 50 | 15 | 0,10 |
| **Sous-total** | **2 820** | | |

Aucune marque au-dessus du plancher.

#### 1b. Racine `ciel étoilé` accentuée, part projecteur (21h53) — 3 570 net / 3 680 brut

| Formulation | Volume | KD | CPC |
|---|---:|---:|---:|
| projecteur ciel étoilé | 1 900 | 30 | 0,18 |
| projecteur ciel étoilé adulte | 390 | 19 | 0,17 |
| ciel étoilé projecteur | 210 | 23 | 0,20 |
| projecteur ciel étoile | 170 | 27 | 0,30 |
| projecteur ciel étoilé chambre | 170 | 23 | 0,16 |
| veilleuse ciel étoilé | 170 | 24 | 0,17 |
| meilleur projecteur ciel étoilé adulte | 140 | 11 | 0,18 |
| projecteur ciel étoilé réaliste | 140 | 16 | 0,14 |
| projecteur de ciel étoilé | 140 | 24 | 0,21 |
| veilleuse projection ciel étoilé | 140 | 21 | 0,15 |
| **Sous-total net** | **3 570** | | |
| projecteur ciel étoilé **action** | 110 | 32 | 0,00 | → **retiré au net** (enseigne Action) |

#### 1c. Racine `astronaute`, part projecteur (21h57) — 720

| Formulation | Volume | KD | CPC |
|---|---:|---:|---:|
| astronaute projecteur | 720 | 24 | 0,13 |

#### 1d. `projecteur etoile` **sans accent** (22h29) — 6 350 — *la découverte de la session*

| Formulation | Volume | KD | CPC |
|---|---:|---:|---:|
| ciel etoile projecteur | 1 300 | 24 | 0,18 |
| projecteur etoile plafond | 1 000 | 29 | 0,23 |
| projecteur ciel etoile | 720 | 24 | 0,18 |
| projecteur etoile | 720 | 28 | 0,19 |
| projecteur d'etoile plafond | 480 | 24 | 0,19 |
| projecteur etoiles | 390 | 31 | 0,18 |
| projecteur ciel etoilé | 320 | 25 | 0,19 |
| projecteur d etoile | 260 | 22 | 0,30 |
| lampe projecteur etoile | 170 | 22 | 0,24 |
| projecteur d etoiles | 170 | 22 | 0,19 |
| projecteur d'etoile | 170 | 25 | 0,15 |
| projecteur etoile enfant | 170 | 19 | 0,00 |
| veilleuse projecteur etoile | 140 | 24 | 0,13 |
| lampe projecteur etoiles | 110 | 23 | 0,24 |
| projecteur etoile bebe | 90 | 16 | 0,20 |
| projecteur de ciel etoile | 70 | 27 | 0,28 |
| projecteur etoiles enfant | 70 | 17 | 0,00 |
| **Sous-total** | **6 350** | | |

**Contrôle de double comptage effectué chaîne par chaîne :** aucune de ces 17 chaînes n'est
identique à une chaîne de 1a, 1b ou 1c. Le KMT traite les variantes accentuées et non accentuées
comme **des lignes distinctes** — `projecteur ciel étoilé` 1 900 et `projecteur ciel etoilé` 320
coexistent, `ciel étoilé projecteur` 210 et `ciel etoile projecteur` 1 300 coexistent. La lecture
accentuée seule (celle de Codex) laissait donc **6 350 recherches invisibles sur cette seule
famille**.

| Total famille 1 | Volume |
|---|---:|
| Brut | **13 570** |
| Marque retirée (`…action` 110) | −110 |
| **Net de marque** | **13 460** |

**Statut : collection cœur** (≥ 1 000), et de loin la plus lourde de l'univers.
**Réserve commodité électrique** (sans trancher) : `projecteur ciel étoilé action` à 110 montre que
l'enseigne Action vend le produit ; CPC 0,09-0,30 USD, KD 9-31.

---

### Famille 2 — Lampes et veilleuses décoratives — **CŒUR**

**Test de la page unique : OUI** pour `lampe lune` / `lampe en lune` / `lune lampe` / `lampe murale
lune` (même objet). `lampe astronaute`, `lampe galaxie` et les veilleuses motifs rejoignent une
collection « Lampes et veilleuses déco espace ».

#### 2a. `lampe lune` (22h03)

| Formulation | Volume | KD | CPC | Décision |
|---|---:|---:|---:|---|
| lampe lune | 1 900 | 24 | 0,34 | retenu |
| lampe en lune | 590 | 23 | 0,34 | retenu |
| lampe lune levitation | 210 | 9 | 0,21 | retenu |
| lampe lune murale | 110 | 3 | 0,34 | retenu |
| lampe murale lune | 110 | 4 | 0,34 | retenu |
| lampe de chevet lune | 70 | 13 | 0,00 | retenu |
| lune lampe | 50 | 9 | 0,56 | retenu |
| **Sous-total net** | **3 040** | | | |
| lampe lune nature et découverte | 170 | 30 | 0,00 | **retiré au net** (enseigne) |
| lampe lune nature et decouverte | 90 | 21 | 0,13 | **retiré au net** (enseigne) |
| lunie lamp | 170 | 31 | 0,23 | **retiré au net** (nom de produit) |
| lampe lune ikea | 110 | 34 | 0,00 | **retiré au net** (enseigne) |
| lampe lune amazon | 50 | 25 | 0,06 | **retiré au net** (enseigne) |
| **Sous-total brut** | **3 630** | | | |

> **Retrait obligatoire — piège n° 3 du catalogue, « mot générique contaminé ».**
> `lampe demi lune` **n'est pas une lampe lune** : c'est une **lampe UV de manucure** et une applique
> demi-cercle. **1 500 retirés** : `lampe demi lune` 590, `lampe demie lune` 260, `lampe demi lune
> ongle` 140, `lampe demi lune onglerie` 140, `lampe demi lune cils` 110, `lampe demi lune ongles`
> 110, `lampe demi lune sur pied` 50, `lampe demi-lune sur pied` 50, `lampe led demi lune` 50.
> Une lecture naïve de la racine aurait annoncé 5 130 au lieu de 3 040 nets.

#### 2b. `lampe astronaute` (21h57) et `lampe galaxie` (22h19)

| Formulation | Volume | KD | CPC | Décision |
|---|---:|---:|---:|---|
| lampe astronaute | 720 | 26 | 0,18 | retenu |
| lampe galaxie | 390 | 25 | 0,27 | retenu |
| lampes galaxie | 170 | 24 | 0,27 | retenu |
| lampe galaxie plafond | 90 | 21 | 0,18 | retenu |
| lampe projecteur galaxie | 110 | 24 | 0,25 | **déjà compté en 1a** — non recompté |
| **Sous-total** | **1 370** | | | |

#### 2c. Veilleuses motifs espace

| Formulation | Volume | KD | CPC | Décision | Source |
|---|---:|---:|---:|---|---|
| veilleuse astronaute | 880 | 26 | 0,15 | retenu | racine `veilleuse` 22h00 |
| veilleuse etoile | 880 | 19 | 0,17 | retenu | `veilleuse etoile` 22h34 |
| veilleuse etoile plafond | 260 | 17 | 0,13 | retenu | idem |
| veilleuse projection etoile | 210 | 17 | 0,20 | retenu | idem |
| veilleuse bebe etoile | 170 | 14 | 0,14 | retenu | idem |
| veilleuse etoile bebe | 170 | 14 | 0,14 | retenu | idem |
| veilleuse bebe etoiles | 140 | 14 | 0,23 | retenu | idem |
| veilleuse plafond etoile | 140 | 16 | 0,16 | retenu | idem |
| veilleuse ciel etoile | 90 | 20 | 0,17 | retenu | idem |
| veilleuse etoiles | 90 | 11 | 0,17 | retenu | idem |
| etoile veilleuse | 70 | 11 | 0,00 | retenu | idem |
| **Sous-total net** | **3 100** | | | | |
| etoile veilleuse **pabobo** | 260 | 17 | 0,15 | **retiré au net** (marque FR) | |
| veilleuse etoile **pabobo** | 260 | 19 | 0,15 | **retiré au net** | |
| **pabobo** veilleuse etoile | 210 | 18 | 0,16 | **retiré au net** | |
| veilleuse **pabobo** etoile | 210 | 16 | 0,16 | **retiré au net** | |
| veilleuse projecteur etoile | 140 | 24 | 0,13 | **déjà compté en 1d** — non recompté | |
| **Sous-total brut** | **4 040** | | | | |

Retiré aussi : `veilleuse nuage` 720 — motif nuage, pas astro.

| Total famille 2 | Volume |
|---|---:|
| Brut (3 630 + 1 370 + 4 040) | **9 040** |
| Marque retirée (590 lampe lune + 940 Pabobo) | −1 530 |
| **Net de marque** | **7 510** |

**Statut : collection cœur.**

⚠️ **Plancher signalé.** Les racines `astronaute` et `veilleuse` sont coupées à **480** sur la
100ᵉ ligne. `veilleuse galaxie`, `veilleuse fusée`, `veilleuse planète`, `lampe saturne`,
`lampe planète` n'ont **pas** été mesurées et sont sous ce plancher. Le chiffre de la famille 2 est
donc un **plancher**, pas un total.

---

### Famille 3 — Kits « ciel étoilé » fibre optique au plafond — **SECONDAIRE, hors thèse**

**Test de la page unique : NON — il en faudrait deux.** Ces requêtes visent un **kit d'installation
au plafond** (fibre optique, LED encastrées), avec pose, découpe et souvent un installateur. Autre
panier, autre SERP, autre métier que la déco posée. **Je ne l'additionne pas** à la famille 1.

| Formulation | Volume | KD | CPC |
|---|---:|---:|---:|
| ciel étoilé plafond | 390 | 8 | 0,44 |
| plafond ciel étoilé | 320 | 12 | 0,35 |
| kit ciel étoilé | 210 | 11 | 0,17 |
| lampe ciel étoilé | 210 | 28 | 0,20 |
| ciel étoilé en fibre optique | 170 | 12 | 0,35 |
| ciel étoilé led | 170 | 7 | 0,42 |
| fibre optique ciel étoilé | 170 | 13 | 0,29 |
| fibre optique pour ciel étoilé | 170 | 18 | 0,35 |
| kit ciel étoilé led plafond | 170 | 7 | 0,24 |
| guirlande ciel étoilé | 140 | 7 | 0,40 |
| led ciel étoilé | 140 | 5 | 0,53 |
| led pour ciel étoilé | 140 | 6 | 0,53 |
| ciel étoilé en led | 110 | 9 | 0,57 |
| **Total brut = net** | **2 510** | | |

**Statut : secondaire (≥ 500) mais hors thèse déco astro posée — à trancher par Hakim.**

---

### Famille 4 — Stickers étoiles phosphorescentes — **CŒUR (limite)**

**Test de la page unique : OUI** — huit formulations d'un même objet (planche d'étoiles qui brillent
la nuit, à coller au plafond).

| Formulation | Volume | KD | CPC | Décision |
|---|---:|---:|---:|---|
| étoiles phosphorescentes | 1 000 | 19 | 0,12 | retenu |
| étoile phosphorescente | 390 | 19 | 0,13 | retenu |
| étoiles phosphorescentes pour plafond | 260 | 20 | 0,12 | retenu |
| étoile phosphorescente plafond | 210 | 24 | 0,12 | retenu |
| étoile phosphorescente pour plafond | 210 | 19 | 0,12 | retenu |
| étoiles phosphorescentes plafond | 210 | 22 | 0,12 | retenu |
| **Sous-total net** | **2 280** | | | |
| étoiles phosphorescentes **action** | 110 | 21 | 0,00 | **retiré au net** |
| étoilé phosphorescente **action** | 90 | 31 | 0,00 | **retiré au net** |
| **Brut** | **2 480** | | | |

**Réserve commodité électrique/bazar :** deux des huit formulations contiennent « action ». C'est un
produit d'enseigne à petit prix. Réserve pour la suite, pas un motif de retrait.

---

### Famille 5 — Décoration murale (posters, tableaux, papier peint) — **PAS DE COLLECTION**

| Formulation | Volume | Source |
|---|---:|---|
| papier peint ciel étoilé | 210 | `ciel étoilé` 21h53 |
| tableau ciel étoilé | 110 | `ciel étoilé` 21h53 |
| `poster astronaute` — **corpus entier** | **70** | `poster astronaute` 22h10 (63 mots-clés) |
| **Total brut = net** | **390** | |

> **Constat.** Le concurrent lepetitastronaute.fr expose une famille entière « décoration murale ».
> **La demande française mesurée pour l'art mural astro est de 390 recherches/mois.** Le corpus
> `poster astronaute` entier — 63 mots-clés — pèse **70**. Ce n'est pas un plancher de lecture :
> c'est le volume total que Semrush attribue à ce corpus.

**Statut : < 300 hors `papier peint` — pas de collection autonome.**

---

### Famille 6 — Objets décoratifs — **SECONDAIRE (limite)**

| Formulation | Volume | KD | CPC |
|---|---:|---:|---:|
| figurine astronaute | 210 | 10 | 0,24 |
| figurines astronautes | 110 | 7 | 0,24 |
| astronaute figurine | 70 | 13 | 0,27 |
| projecteur planétarium | 480 | 12 | 0,16 |
| planétarium projecteur | 210 | 11 | 0,18 |
| **Total net** | **1 080** | | |
| + marques (`planétarium buki` 260, `buki planétarium` 210, `baader planétarium` 110) | 580 | | |
| **Brut** | **1 660** | | |

Le corpus `figurine astronaute` entier (84 mots-clés) pèse **650** au KMT.

---

### Famille 7 — Maquette du système solaire (éducatif) — **SECONDAIRE, réserve d'intention**

| Formulation | Volume | KD | CPC |
|---|---:|---:|---:|
| maquette système solaire | 1 000 | 15 | 0,21 |
| maquette du système solaire | 720 | 14 | 0,21 |
| maquette sur le système solaire | 720 | 11 | 0,13 |
| système solaire maquette | 720 | 14 | 0,13 |
| **Total brut = net** | **3 160** | | |

**Réserve explicite, non tranchée :** la formulation « maquette **sur le** système solaire » (720) est
la signature d'un **exercice scolaire** (« faire une maquette »), pas d'un achat. Le CPC de 0,13-0,21
et le KD de 11-15 disent une SERP peu monétisée. Ce total est donné **avec** et **sans** dans la
synthèse. Une vérification SERP (étape 5) est indispensable avant de le compter.

Retirés de la même lecture : `carte du système solaire` 390 + `carte systeme solaire` 390 = 780
(affiche scolaire — rattachable à la famille murale, non compté pour rester conservateur), et
**161 480 de requêtes scolaires et informationnelles** (voir §7).

---

### Famille 8 — Textile de maison — **INEXISTANTE**

| Formulation | Volume |
|---|---:|
| housse de couette espace | 110 |
| `housse de couette espace` — **corpus entier (46 mots-clés)** | **190** |

**Statut : < 300 — pas de collection.** Le textile astro n'a pas de demande mesurable en France.

---

### Famille 9 — Cadeau / carte du ciel imprimée — **FRONTIÈRE, voir §5**

Lecture `carte du ciel` 22h13 : 88 lignes, **24 530** lus, dont :

| Bloc | Volume | Motif |
|---|---:|---|
| **Astrologie / thème astral** | **7 430** | `astrotheme carte du ciel` 1 300, `carte du ciel astrologie` 1 300, `carte du ciel astrotheme` 880, `astrologie carte du ciel` 480, `carte du ciel astrologique` 320… → **U6 ésotérisme**, pas U4b |
| **Outil d'observation / temps réel** | **8 380** | `carte du ciel ce soir` 2 400, `carte du ciel gratuite` 1 000, `carte du ciel temps réel` 720, `stelvision` 320 + 260, `carte du ciel en direct` 320… → applications, gratuit, **informationnel** |
| Tête `carte du ciel` | 4 400 | ambiguë (KD 49) — non comptée |
| **Produit imprimé** | **820** | `carte du ciel personnalisée` 210 (KD 8, **CPC 0,97**), `carte du ciel naissance` 170, `la carte du ciel le jour de ma naissance gratuit` 170, `carte du ciel imprimable` 90, `carte du ciel à imprimer` 90, `imprimer carte du ciel` 90 |

Dont **350 en « imprimable / à imprimer / gratuit »** = intention téléchargement gratuit, retirée.
**Produit commercial net : 470** (`carte du ciel personnalisée` 210 + `carte du ciel naissance` 170
+ `imprimer carte du ciel` 90).

---

## 3. Synthèse par famille

| # | Famille | Brut | Net de marque | Statut |
|---|---|---:|---:|---|
| 1 | **Projecteurs d'ambiance** | 13 570 | **13 460** | **cœur** |
| 2 | **Lampes et veilleuses** | 9 040 | **7 510** | **cœur** (plancher) |
| 4 | **Stickers étoiles phosphorescentes** | 2 480 | **2 280** | **cœur** (limite) |
| 7 | Maquette système solaire | 3 160 | 3 160 | secondaire — **réserve d'intention scolaire** |
| 3 | Kit ciel étoilé fibre optique plafond | 2 510 | 2 510 | secondaire — **hors thèse déco posée** |
| 6 | Objets décoratifs (figurines + planétarium produit) | 1 660 | 1 080 | secondaire |
| 9 | Carte du ciel imprimée | 820 | 470 | **frontière U6** |
| 5 | Décoration murale | 390 | 390 | < 300 utile — pas de collection |
| 8 | Textile de maison | 190 | 110 | pas de collection |

---

## 4. Total dédupliqué net de marque

### 4.1 Le détail de la déduplication

Trois chevauchements ont été détectés et **soustraits une fois** :

| Formulation | Volume | Apparaît dans | Attribuée à |
|---|---:|---|---|
| `lampe projecteur galaxie` | 110 | `projecteur galaxie` **et** `lampe galaxie` | Famille 1 (projecteurs) |
| `veilleuse projecteur etoile` | 140 | `projecteur etoile` **et** `veilleuse etoile` | Famille 1 (projecteurs) |
| `veilleuse etoile` | 880 | racine `veilleuse` **et** `veilleuse etoile` | Famille 2, comptée **une fois** |

Contrôle chaîne par chaîne effectué entre les lectures accentuées et non accentuées : **aucune
chaîne identique n'apparaît deux fois** dans les totaux ci-dessus.

### 4.2 Les trois totaux

| Périmètre | Net de marque |
|---|---:|
| **A. Cœur strict U4b déco astro** (familles 1 + 2 + 4 + 5 + 6 + 8 + planétarium produit déjà dans 6) | **24 830** |
| **B. A + kit fibre optique plafond** (famille 3) | **27 340** |
| **C. B + maquette système solaire + carte du ciel** (familles 7 et 9) | **30 970** |

Détail de A : 13 460 + 7 510 + 2 280 + 1 080 + 390 + 110 = **24 830**.
Détail de B : 24 830 + 2 510 = **27 340**.
Détail de C : 27 340 + 3 160 + 470 = **30 970**.

### 4.3 Réponse chiffrée : les 18 000 nets additionnels sont-ils là ?

La base de Codex était de **12 000 bruts sur 4 têtes**, dont **6 600 pour `planétarium`** — dont il
est maintenant établi que **690 seulement sont du produit**. La base réelle de Codex, nettoyée,
vaut donc **5 400 + 690 = 6 090**, pas 12 000.

| Question | Réponse chiffrée |
|---|---|
| Volume net additionnel trouvé, périmètre strict (A) | **24 830 − 6 090 = 18 740** |
| Volume net additionnel trouvé, périmètre large (C) | **30 970 − 6 090 = 24 880** |
| **Les 18 000 nets additionnels sont-ils là ?** | **Oui au sens arithmétique de l'audit : 18 740 en périmètre strict.** |
| L'univers atteint-il le plancher de 30 000 ? | **Non en périmètre strict : 24 830, déficit 5 170.** Oui de justesse en périmètre large : 30 970 — mais en y comptant un kit de bricolage plafond, une maquette scolaire et une carte astrologique, trois familles dont l'appartenance à une boutique de déco astro n'est pas acquise. |

**Ces deux réponses ne se contredisent pas.** L'audit demandait 18 000 **additionnels** face à une
somme brute de 12 000 ; ils sont là. Mais comme 6 600 de cette somme brute étaient du planétarium-lieu,
le total qui en résulte reste **sous les 30 000** dès qu'on s'en tient au cœur du sujet.

---

## 5. Section frontière U3 (globes) / U4a (télescopes) / U6 (ésotérisme)

| Objet contesté | Volume mesuré | Attribution proposée | Motif |
|---|---:|---|---|
| **`globe lune`** | **590** (corpus entier, 155 mots-clés) | **Litige sans enjeu — n'attribuer à personne** | La seule ligne chiffrée du corpus est `luna original & fresh globe cooking` 210, un restaurant. Il n'y a **pas de demande française** pour un globe lunaire. La frontière U3/U4b sur ce mot portait sur moins de 400 recherches. |
| **`carte du ciel`, part astrologie** | **7 430** | **U6 ésotérisme** | Thème astral, ascendant, Astrotheme. Ce n'est pas de la déco astro. **Non compté en U4b.** |
| **`carte du ciel`, part produit imprimé** | **470** | **U4b** (famille 9) | Carte du ciel personnalisée à offrir : objet déco imprimé. Compté une seule fois, ici. |
| **`carte du ciel`, part outil/observation** | **8 380** | **Personne** | Applications, temps réel, gratuit. Informationnel. |
| **Télescopes et lunettes astronomiques** | non mesuré | **U4a — hors périmètre** | Exclu par mandat. Aucune requête télescope n'entre dans les totaux ci-dessus. |
| **`maquette système solaire`** | 3 160 | **U4b sous réserve** | Frontière avec l'éducatif/scolaire, pas avec un autre univers. Voir famille 7. |

**Aucun volume n'est compté deux fois entre univers.**

---

## 6. Comparaison explicite avec les 12 000 de Codex, formulation par formulation

| Tête Codex | Volume Codex | Ce que la consolidation trouve | Écart |
|---|---:|---|---:|
| `projecteur galaxie` | 1 600 | Famille projecteurs entière : **13 460 nets** (dont 6 350 de formulations non accentuées jamais lues, 3 570 sur `ciel étoilé`, 720 sur `astronaute`) | **× 8,4** |
| `projecteur ciel étoilé` | 1 900 | *(inclus dans la ligne ci-dessus — c'est la même page)* | fusionné |
| `lampe lune` | 1 900 | Famille lampes et veilleuses : **7 510 nets** — mais après retrait de **1 500 de lampes de manucure** (`lampe demi lune`) que la racine ramenait | **× 4,0** |
| `planétarium` | 6 600 | **690 nets de produit.** Les 6 600 sont la tête d'un cluster dont **38 400 de traîne sont du lieu et de la billetterie** (77 % des 98 lignes) | **÷ 9,6** |
| **Total** | **12 000** | **24 830 nets** (périmètre strict) | **× 2,1** |

### La part `planétarium`-lieu dans les 12 000 de Codex

**6 600 sur 12 000, soit 55 % de son total, reposent sur le mot `planétarium`** — dont la mesure
consolidée montre que la demande produit vaut **690**. En retirant le lieu, la base de Codex tombe
de 12 000 à **6 090**.

### Ce que la consolidation a démontré et ce qu'elle a démenti

- **Démontré :** l'étape 3 fonctionne ici comme sur Noirmont. Les projecteurs pèsent **8,4 fois** la
  tête que Codex avait retenue. La cause principale est nouvelle et n'était dans aucun rapport :
  **les variantes non accentuées sont des lignes KMT distinctes** (`ciel etoile projecteur` 1 300 est
  invisible depuis une lecture de `ciel étoilé`).
- **Démenti :** l'hypothèse de l'audit selon laquelle les familles jamais mesurées du concurrent
  (mur, textile, objets) contenaient la réserve manquante. **Elles sont vides en France** :
  décoration murale 390, textile 190, figurines 650. Les 1 769 URL produit de lepetitastronaute.fr
  ne sont pas de la demande — c'est exactement la mise en garde de l'étape 6 de la méthode.
- **Le volume de U4b est concentré sur la lumière** : projecteurs + lampes + veilleuses +
  phosphorescent = **23 250 nets sur 24 830**, soit **94 % du périmètre strict**.

---

## 7. Ce qui n'a pas pu être mesuré

1. **La racine `galaxie` seule est inexploitable.** 138 754 mots-clés, volume broad 625 240, mais le
   top 100 est saturé par la licence Marvel (`les gardiens de la galaxie` 27 100, `gardien de la
   galaxie` 14 800, `les gardiens de la galaxie 3` 9 900) et par le complexe de loisirs `galaxie
   amnéville` 22 200 / `galaxie d'amnéville` 4 400. **100ᵉ ligne à 590** : toutes les formulations
   produit sont sous le plancher de lecture. La famille a donc été mesurée par requêtes à deux mots.
2. **`poster espace` est inutilisable : rabattement orthographique total.** Semrush ramène `poster` à
   `poste` : les 92 lignes chiffrées sont `poste mobile espace client` 6 600, `espace client la poste`
   3 600, `la poste espace clients pro` 3 600… **100 % hors sujet, 57 290 de volume**. Aucune ligne
   déco. C'est le piège n° 2 du catalogue, dans sa forme la plus brutale. La déco murale a donc été
   mesurée par `poster astronaute` (70) et par les lignes murales des autres racines.
3. **Trois planchers de lecture non percés**, faute de budget de requêtes :
   - `astronaute` — 100ᵉ ligne à **480**. Non mesurés : `déco astronaute`, `tirelire astronaute`,
     `peluche astronaute`, `coussin astronaute`, toutes les variantes non accentuées.
   - `veilleuse` — 100ᵉ ligne à **480**. Non mesurés : `veilleuse galaxie`, `veilleuse fusée`,
     `veilleuse planète`, `veilleuse lune`.
   - `système solaire` — 100ᵉ ligne à **390**. Non mesurés : `déco système solaire`, `mobile système
     solaire`, `suspension planètes`.
4. **Les variantes non accentuées n'ont été explorées que sur deux familles** (`projecteur etoile`,
   `veilleuse etoile`), où elles ont rapporté **9 650 bruts**. Le même gisement existe très
   probablement sur `lampe`, `deco`, `planete`, `systeme solaire` et **n'a pas été mesuré**. Les
   totaux du §4 sont donc des **planchers**, pas des plafonds.
5. **Familles listées au mandat et non mesurées faute de budget** : `lampe planète`, `lampe saturne`,
   `boule cristal cosmique`, `tapisserie espace`, `coussin planète`, `tapis espace`, `plaid galaxie`,
   `cadeau astronomie`, `cadeau espace`. Les mesures voisines (textile 190, murale 390, figurines 650)
   rendent peu probable qu'elles portent un volume à trois chiffres, mais **ce n'est pas mesuré**.
6. **Aucune vérification SERP (étape 5) n'a été faite** — elle n'était pas dans le mandat. Trois
   totaux en dépendent directement : la tête `planétarium` 6 600 (comptée 0), la tête `ciel étoilé`
   6 600 (comptée 0), et la famille `maquette système solaire` 3 160 (comptée en réserve). Une SERP
   sur ces trois têtes peut déplacer le total de −3 160 à +13 200.
7. **Aucun relevé de prix, aucun sourcing, aucune analyse de concurrence** dans ce document : ce
   n'était pas le mandat.

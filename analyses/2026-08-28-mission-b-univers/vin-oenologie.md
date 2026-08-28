# Mission B — Analyse de marché UNIVERS — Vin & œnologie

**Date : 2026-08-28** · Mode **UNIVERS** · Seuil applicable : **volume consolidé par familles ≥ 30 000/mois (confort 40 000)** — `PRODUCT-RESEARCH-CRITERIA.md` §1. Le seuil PRODUIT PUR de 10 000 par cluster **ne s'applique pas ici**.

Méthode : `METHODE-ANALYSE-MARCHE.md` étapes 2 à 5 et étape 9 · skill `recherche-mots-cles` Mission B.

---

## 1. Entrée et méthode

### 1.1 Source d'entrée

Rapport de préparation : `boutique-pipeline/analyses/2026-08-28-mission-b-univers-preparation.md`, §5.1 (candidat #16, somme indicative 78K, confiance A, preuve L'Atelier du Vin / Vinatis / Comptoir des Sommeliers).

Les graines de ce document sont **remesurées ici, aucune n'est reprise**. Le 78K indicatif du 22/08 n'est pas réutilisé (catalogue des pièges n° 8 : le chiffre repris sans revérification).

### 1.2 Outil et contrôle témoin

SEMrush Keyword Magic Tool, **base France (`db=fr`)**, expression exacte (`&mt=phrase`), 100 lignes, 0 crédit. Devise affichée **EUR** (`currency=eur`) : **tous les CPC de ce rapport sont en EUR**, pas en dollars. « Base de données : France » et « Devise : EUR » relus sur chaque page.

Onglet Chrome dédié créé pour cette mission (tabId 885853572), fermé en fin de tâche. Trois autres agents travaillaient en parallèle sur le même navigateur ; aucun de leurs onglets n'a été touché.

| Contrôle témoin | Heure | Lecture de la ligne `tufting` | Verdict |
|---|---|---|---|
| **Avant** la première mesure | 2026-08-28 | **8 100** | conforme |
| **Après** la dernière mesure | 2026-08-28 | **8 100** | conforme |

→ **Quota intact sur toute la session. Aucun zéro silencieux.** Tous les chiffres ci-dessous sont exploitables.

### 1.3 Graines contrôlées

| Famille | Graines effectivement mesurées le 2026-08-28 |
|---|---|
| Ouverture | `tire bouchon` · `limonadier` · `ouvre bouteille` |
| Aération | `decanteur` · `décanteur` · `carafe vin` · `aerateur vin` · `aérateur vin` |
| Conservation | `bouchon vin` · `conservation vin` · `pompe vin` |
| Verrerie | `verre a vin` · `verre à vin` · `verre inao` |
| Coffret | `coffret vin` · `coffret sommelier` |
| Cave | `cave a vin` |
| Parents | `accessoire vin` · `oenologie` · `œnologie` |

**19 graines**, dont **6 paires d'orthographes testées séparément** (contrôle n° 1).

### 1.4 Les cinq contrôles, appliqués à chaque passe

1. **Deux orthographes — confirmé comme deux corpus distincts, écart majeur.** Ce n'est pas une précaution théorique sur ce dossier :

| Racine | Non accentuée | Accentuée / ligature | Écart |
|---|---|---|---|
| décanteur | `decanteur` → tête 720, cluster 2 988 kw / 12 460 | `décanteur` → tête 390, cluster 2 240 kw / 10 950 | corpus **disjoints**, lignes différentes |
| verre à vin | `verre a vin` → tête **12 100**, 8 108 kw / 80 170 | `verre à vin` → tête 2 400 (+ `verres à vin` 2 900), 6 080 kw / 49 660 | **deux corpus, ~48 000 de volume total d'écart** |
| aérateur | `aerateur de vin` → **3 600** | `aérateur de vin` → **590** | **×6,1** |
| œnologie | `oenologie` → **6 600** | `œnologie` → **1 000** | **×6,6** |

Mesurer une seule orthographe aurait sous-compté l'univers d'un facteur 2 à 6. C'est la leçon `ciel etoile` / `ciel étoilé`, confirmée quatre fois ici.

2. **Plusieurs niveaux de généralité.** Trois niveaux par famille, **jamais additionnés entre eux quand ils désignent des périmètres différents** : formulation produit (`tire-bouchon sommelier`) → produit fini (`tire bouchon`) → catégorie parente (`accessoire vin`, `oenologie`). Les parents sont comptés **une seule fois, à part**, et seulement pour leur part produit.

3. **`n/a` ≠ `0`.** Distingués partout. `n/a` = sous le seuil de restitution SEMrush (< 10/mois) ou métrique non rafraîchie (« Pour afficher les métriques, actualisez la page »). Des lignes à **volume 0 explicite** ont été rencontrées (`aliexpress aérateur de vin` = 0, `24 verres inao` = 0) : elles ne sont pas écrites comme des `n/a`.

4. **Mot-clé témoin.** Voir §1.2, avant et après.

5. **Plancher de lecture.** Trois familles ne sont **pas couvertes** par les 100 premières lignes :

| Racine | Pages | 100ᵉ ligne | Statut |
|---|---|---|---|
| `tire bouchon` | 188 | 320 | **PLANCHER** |
| `verre a vin` | 82 | 110 | **PLANCHER** |
| `verre à vin` | 61 | 90 | **PLANCHER** |
| `bouchon vin` | 54 | 50 | plancher léger |
| `cave a vin` | 433 | 480 | **PLANCHER majeur** (famille retirée) |
| `limonadier`, `ouvre bouteille`, `carafe vin`, `aerateur vin`, `accessoire vin`, `coffret sommelier` | 1–18 | 10–40 | couverts |

Les totaux de ces familles sont donc des **planchers, pas des totaux**.

### 1.5 Limites de calcul, dites franchement

- **Non mesuré, faute de temps outil** : `cave à vin` (orthographe accentuée), `armoire à vin`, `cave de vieillissement` — sous-familles de la Cave, **retirée du consolidé de toute façon** (§5) ; `service du vin`, `verre à pied`, `verrerie` (parents), `verre dégustation` en racine autonome. Les formulations `verre à vin dégustation` (480), `verre à dégustation vin` (390), `coffret dégustation vin` (720) et `coffret degustation vin` (720) **ont** été captées à l'intérieur des racines mesurées.
- **`javascript_tool` bloqué** par un garde-fou de l'extension après trois appels (« Cookie/query string data »). Toutes les lectures suivantes ont été faites via `get_page_text`, sans perte de donnée mais avec un coût de lecture plus élevé.
- **Les pourcentages de retrait SERP sont des estimations** faites à la composition de la page 1, **pas de nouvelles mesures**. Ils sont signalés comme tels ligne par ligne.
- **Page 1 seulement** en SERP : cela interdit tout jugement sur la profondeur de la concurrence.
- **Google Trends non fait** : l'exigence de socle ≥ 8 mois n'est donc **pas vérifiée**. Voir §8, réserve bloquante.
- **Aucune sonde prix Google Shopping dédiée** n'a été lancée : les bandes de prix du §7 sont relevées **dans les carrousels des SERP réelles**, datées, et suffisantes pour caractériser les paliers — pas pour fixer un prix.

---

## 2. Mesure par graine

Toutes lectures **2026-08-28**, base France, CPC en **EUR**.

### 2.1 Ouverture

| Formulation | Volume | KD | CPC (EUR) | Intention | Racine |
|---|---|---|---|---|---|
| `tire bouchon` | **12 100** | 24 | 0,29 | T | tire bouchon |
| `tire bouchon electrique` | 4 400 | 17 | 0,25 | I | tire bouchon |
| `tire bouchon électrique` | 1 000 | 15 | 0,25 | I | tire bouchon |
| `tire bouchon electronique` | 1 000 | 24 | 0,25 | T | tire bouchon |
| `tire-bouchon` | 1 300 | 21 | 0,29 | T | tire bouchon |
| `tire bouchon personnalisé` | 1 300 | 13 | 0,66 | I | tire bouchon |
| `tire bouchon mural` | 880 | 8 | 0,24 | I | tire bouchon |
| `tire bouchon sommelier` | 880 | 11 | 0,34 | I | tire bouchon |
| `tire bouchon a levier` | 720 | 13 | 0,36 | I | tire bouchon |
| `tire bouchon a air` | 720 | 11 | 0,16 | I | tire bouchon |
| `tire bouchon bilame` | 590 | 10 | 0,29 | I | tire bouchon |
| `limonadier` | **9 900** | 23 | 0,35 | I | limonadier |
| `limonadier personnalisé` | 1 000 | 18 | 0,64 | I | limonadier |
| `limonadier professionnel` | 720 | 14 | 0,27 | I/C | limonadier |
| `limonadiers` | 390 | 21 | 0,41 | I | limonadier |
| `limonadier sommelier` | 320 | 13 | 0,23 | I | limonadier |
| `ouvre bouteille` | **2 400** | 12 | 0,24 | I/T | ouvre bouteille |
| `ouvre bouteille electrique` | 880 | 20 | 0,23 | I/T | ouvre bouteille |
| `ouvre bouteille personnalisé` | 590 | 8 | 0,57 | I | ouvre bouteille |
| `ouvre bouteille vin` | 320 | 22 | 0,33 | I | ouvre bouteille |

Cluster complet : `tire bouchon` 18 734 kw / 206 370 · `limonadier` 1 781 kw / 24 660 · `ouvre bouteille` 5 048 kw / 33 930. **Ces « Volume total » ne sont pas additionnés** : ils incluent tout le bruit (sur le témoin `tufting`, SEMrush affiche 78 920 quand la tête vaut 8 100).

### 2.2 Aération

| Formulation | Volume | KD | CPC (EUR) | Intention | Racine |
|---|---|---|---|---|---|
| `carafe vin` | **2 400** | 31 | 0,44 | I | carafe vin |
| `carafe a vin` | 1 900 | 22 | 0,39 | I | carafe vin |
| `carafe à vin` | 1 900 | 17 | 0,29 | I | carafe vin |
| `carafe décantation vin` | 880 | 18 | 0,37 | I | carafe vin |
| `carafe à décanter le vin` | 720 | 12 | 0,27 | I | carafe vin |
| `carafe à décanter vin` | 720 | 13 | 0,24 | I/T | carafe vin |
| `carafe à vin à décanter` | 480 | 15 | 0,37 | I | carafe vin |
| `carafe pour decanter le vin` | 480 | 19 | 0,37 | I | carafe vin |
| `carafe décanteur vin` | 480 | 19 | 0,37 | I | carafe vin ∩ décanteur |
| `aerateur de vin` | **3 600** | 15 | 0,17 | I | aerateur vin |
| `aerateur vin` | 480 | 12 | 0,24 | I | aerateur vin |
| `aerateur a vin` | 320 | 21 | 0,24 | I | aerateur vin |
| `vin aerateur` | 320 | 13 | 0,26 | I | aerateur vin |
| `aérateur de vin` | 590 | 20 | 0,16 | I | aérateur vin |
| `aérateur vin` | 140 | 14 | 0,16 | I | aérateur vin |
| `decanteur de vin` | 1 300 | 15 | 0,25 | I | decanteur |
| `decanteur vin` | 880 | 16 | 0,10 | I | decanteur |
| `decanteur` | 720 | 18 | 0,72 | I | decanteur |
| `decanteur a vin` | 390 | 11 | 0,10 | I/T | decanteur |
| `décanteur de vin` | 480 | 11 | 0,25 | I | décanteur |
| `décanteur vin` | 480 | 17 | 0,29 | I | décanteur |
| `décanteur` | 390 | 21 | 0,00 | I | décanteur |

### 2.3 Conservation

| Formulation | Volume | KD | CPC (EUR) | Intention | Racine |
|---|---|---|---|---|---|
| `bouchon vin` | **590** | 16 | 0,31 | I | bouchon vin |
| `bouchon bouteille vin` | 590 | 15 | 0,23 | I | bouchon vin |
| `bouchons à vin` | 590 | 18 | 0,42 | I | bouchon vin |
| `bouchon de bouteille de vin` | 480 | 14 | 0,30 | I | bouchon vin |
| `bouchon pour vin` / `du vin` / `pour le vin` / `bouchons pour vin` | 480 ×4 | 14–17 | 0,42 | I | bouchon vin |
| `bouchon sous vide vin` | 260 | 11 | 0,20 | I | bouchon vin |
| `bouchon vin sous vide` | 260 | 16 | 0,20 | I | bouchon vin |
| `bouchon conservation vin` | 210 | 11 | 0,25 | C | bouchon vin ∩ conservation |
| `bouchon pour conserver le vin` | 210 | 9 | 0,34 | C | bouchon vin ∩ conservation |
| `bouchon vide air vin` | 210 | 11 | 0,20 | I/T | bouchon vin |
| `conservateur vin` | 170 | 11 | 0,25 | I | conservation vin |
| `appareil pour conserver une bouteille de vin ouverte` | 70 | 10 | 0,15 | I | conservation vin |
| `pompe a vin` | **480** | 12 | 0,28 | I | pompe vin |
| `pompe a vide vin` | 320 | 8 | 0,19 | I | pompe vin |
| `pompe a vide pour le vin` | 260 | 8 | 0,19 | I | pompe vin |
| `pompe vin` | 260 | 13 | 0,47 | I/T | pompe vin |
| `pompe à vin` | 260 | 12 | 0,53 | I | pompe vin |

### 2.4 Verrerie

| Formulation | Volume | KD | CPC (EUR) | Intention | Racine |
|---|---|---|---|---|---|
| `verre a vin` | **12 100** | 23 | 0,28 | I/C | verre a vin |
| `verres a vin` | 1 600 | 21 | 0,28 | I/C | verre a vin |
| `verre a vin personnalisable` | 1 000 | 18 | 0,53 | I | verre a vin |
| `verre a vin plastique` | 1 000 | 11 | 0,40 | I/C | verre a vin |
| `verres à vin` | **2 900** | 21 | 0,29 | I | verre à vin |
| `verre à vin` | **2 400** | 19 | 0,42 | I/C | verre à vin |
| `verres à vins` | 1 600 | 32 | 0,29 | I/C | verre à vin |
| `verre à vin blanc` | 1 000 | 13 | 0,27 | I | verre à vin |
| `verre à vin rouge` | 1 000 | 14 | 0,23 | I/C | verre à vin |
| `verre à vin dégustation` | 480 | 19 | 0,36 | I | verre à vin |
| `verre inao` | **1 300** | 11 | 0,55 | I/C | verre inao |
| `inao verre` | 720 | 10 | 0,55 | I | verre inao |
| `verres inao` | 480 | 8 | 0,63 | I | verre inao |

Signal notable : le **mot de la maison** (`verre inao`, CPC 0,55–0,63 EUR) porte un CPC **deux fois supérieur** au mot du particulier (`verre a vin`, 0,28 EUR). C'est le seul endroit du dossier où le vocabulaire spécialiste vaut plus cher que le vocabulaire grand public.

### 2.5 Coffret

| Formulation | Volume | KD | CPC (EUR) | Intention |
|---|---|---|---|---|
| `coffret vin` | **1 900** | 33 | **0,78** | C |
| `coffret cadeau vin` | 880 | 25 | **1,02** | I |
| `coffret pour vin` | 880 | 19 | **1,07** | I |
| `coffret vin personnalisé` | 880 | 14 | 0,55 | I |
| `coffret dégustation vin` | 720 | 21 | 0,81 | I |
| `coffret degustation vin` | 720 | 27 | 0,81 | I |
| `coffret de vin` | 390 | 31 | **1,33** | I/C |
| `abonnement coffret vin` | 70 | 25 | **2,26** | I/C |
| `coffret sommelier` | **720** | 29 | 0,32 | I/C |
| `coffret du sommelier` | 390 | 12 | 0,32 | I |
| `coffret sommelier personnalisé` | 260 | 6 | 0,38 | C |
| `coffret accessoire vin` | 170 | 10 | 0,39 | I/C |
| `coffret oenologie` | 480 | 14 | 0,65 | I |

**Les CPC les plus élevés de tout le dossier sont ici (0,78 à 2,26 EUR)** — et ce sont précisément les formulations qui désignent des coffrets **contenant des bouteilles**. Voir §4.5.

### 2.6 Cave (mesurée séparément, voir §5)

| Formulation | Volume | KD | CPC (EUR) | Intention |
|---|---|---|---|---|
| `cave a vin` | **60 500** | 41 | 0,26 | C |
| `cave a vin encastrable` | 4 400 | 13 | 0,36 | I |
| `cave a vin la sommeliere` | 4 400 | 23 | 0,31 | I |
| `petite cave a vin` | 3 600 | 13 | 0,17 | I/C |
| `cave a vin autour de moi` | 3 600 | 19 | 0,44 | C |
| `cave a vin de vieillissement` | 1 600 | 20 | 0,29 | I/C |

Cluster : **43 225 kw / 401 220 de volume total / 433 pages.**

### 2.7 Parents

| Formulation | Volume | KD | CPC (EUR) | Intention |
|---|---|---|---|---|
| `accessoire vin` | 720 | 21 | 0,25 | I |
| `vin accessoire` | 720 | 21 | 0,27 | I/C |
| `accessoire à vin` | 590 | 22 | 0,25 | I |
| `accessoires pour le vin` | 590 | 20 | 0,25 | I |
| `vin et accessoires` | 590 | 21 | 0,25 | I |
| `accessoires du vin` | 480 | 23 | 0,25 | I |
| `oenologie` | **6 600** | 43 | 0,75 | I |
| `œnologie` | 1 000 | 33 | 0,75 | I |

---

## 3. Consolidation par familles — brut et net de marque

**Règle appliquée :** on additionne ce qu'**une même page de collection servirait**, et rien d'autre. Test « une page ou deux ? » appliqué ligne par ligne. **Jamais un mot dans deux familles.** Les recoupements sont **mesurés**, pas estimés.

### 3.1 Recoupements mesurés entre racines

Chaque ligne suivante appartient à deux racines interrogées. Elle est comptée **une seule fois**, dans la famille indiquée :

| Ligne | Volume | Racines croisées | Attribuée à |
|---|---|---|---|
| `carafe décanteur vin` | 480 | carafe vin ∩ décanteur | Aération (1×) |
| `carafe decanteur de vin` | 90 | carafe vin ∩ decanteur | Aération (1×) |
| `decanteur aerateur vin` | 70 | decanteur ∩ aerateur | Aération (1×) |
| `aerateur decanteur de vin` | 40 | decanteur ∩ aerateur | Aération (1×) |
| `carafe aerateur vin` | 50 | carafe ∩ aerateur | Aération (1×) |
| `carafe aerateur de vin` | 40 | carafe ∩ aerateur | Aération (1×) |
| `bouchon decanteur aerateur de vin` | 20 | decanteur ∩ aerateur | Aération (1×) |
| `décanteur aérateur de vin` | 40 | décanteur ∩ aérateur | Aération (1×) |
| `bouchon décanteur aérateur de vin` | 20 | décanteur ∩ aérateur | Aération (1×) |
| `bouchon aerateur vin` | 90 | bouchon vin ∩ aerateur | Conservation (1×) |
| `bouchon pompe vin` | 50 | bouchon vin ∩ pompe vin | Conservation (1×) |
| `bouchon conservation vin` + 3 variantes | 760 | bouchon vin ∩ conservation vin | Conservation (1×) |
| `limonadier tire bouchon` + 3 variantes | 690 | limonadier ∩ tire bouchon | Ouverture (1×) |
| `coffret verre a vin` + `verre a vin coffret` | 310 | verre a vin ∩ coffret vin | Verrerie (1×, famille retirée) |
| `coffret tire bouchon vin` | 90 | tire bouchon ∩ coffret vin | Ouverture (1×) |
| `verre à vin inao` | 90 | verre à vin ∩ verre inao | Verrerie (1×, famille retirée) |

**Recoupement total mesuré entre racines : 2 930.** Il est déjà déduit des totaux ci-dessous.

### 3.2 Tableau de consolidation

| # | Famille | Brut (avec marque) | **Net de marque** | Couverture | Verdict SERP §4 |
|---|---|---:|---:|---|---|
| 1 | **Ouverture** (tire-bouchon · limonadier · ouvre-bouteille) | ≈ 62 000 | **≈ 54 300** | plancher (188 p.) | retenue avec retrait |
| 2 | **Aération** (carafe · décanteur · aérateur) | ≈ 31 200 | **≈ 29 300** | couverte | **retenue** |
| 3 | **Conservation** (bouchons · pompes à vide) | ≈ 17 200 | **≈ 15 900** | plancher léger | retenue avec retrait |
| 4 | **Coffret accessoires** (coffret sommelier · coffret d'accessoires) | ≈ 6 100 | **≈ 5 400** | couverte | retenue avec retrait |
| 5 | **Accessoires du vin** (page parente générique) | ≈ 6 400 | **≈ 5 840** | couverte | retenue |
| 6 | **Œnologie — part produit** (coffret/cadeau/kit œnologie) | ≈ 2 200 | **≈ 2 060** | couverte | retenue |
| — | *Verrerie* | *≈ 61 000* | *≈ 52 000* | *plancher (82 + 61 p.)* | **RETIRÉE — §4** |
| — | *Cave à vin* | *≈ 401 000 (cluster)* | *n/a* | *plancher majeur (433 p.)* | **RETIRÉE — électroménager** |

**Marques retirées du brut pour obtenir le net :** L'Atelier du Vin, Peugeot, Screwpull, Vacu Vin, Riedel, Spiegelau, Le Creuset, Château Laguiole (liste imposée) — et, détectées en ouvrant les grappes (contrôle n° 4) : Opinel, Alessi, Pulltaps, Pulltex, Coutale, Pradel Excellence, Lehmann, Chef & Sommelier, Cristal d'Arques, Duralex, Luminarc, Villeroy & Boch, Zwiesel, Bormioli, Vinturi, Aveine, Trudeau, Coravin, Decantus, Class Wine, Vin Bouquet, Alaskan Maker, Le Nez du Vin (Jean Lenoir), Maserin, Secret de Gourmet, Ard Time — plus les **enseignes** IKEA, Maisons du Monde, GiFi, Action, Centrakor, Conforama, JYSK, BUT, Carrefour, Leclerc, Auchan, Lidl, Darty, Boulanger, Cdiscount, Amazon, Fnac, La Foir'Fouille, Nature & Découvertes, Du Bruit dans la Cuisine, La Chaise Longue, Gamm Vert, Leroy Merlin, Mr Bricolage, Metro, Nicolas, Vinatis, Temu.

L'écart brut → net n'est pas cosmétique : **−7 700 sur Ouverture, −9 000 sur Verrerie sur la seule page 1**.

---

## 4. Vérification SERP par tête de famille

google.fr, `hl=fr&gl=fr`, session non connectée, **lectures du 2026-08-28**.

> **Précaution obligatoire.** Je ne peux **pas isoler les annonces Search texte** sur ces pages. Deux SERP seulement affichent un bloc explicitement labellisé « **Produits Sponsorisés** » (`limonadier`, `coffret sommelier`) : ce sont des **annonces Shopping confirmées**, pas des annonces texte. Partout ailleurs, ce que je décris comme « carrousel » mélange fiches gratuites et sponsorisées sans distinction lisible. Les pourcentages de retrait ci-dessous sont des **estimations à la composition de la page 1**, pas des mesures.

### 4.1 `tire bouchon` — Ouverture

**Ce que Google sert.** Une page **triple** : deux packs locaux (restaurants *Le Tire-Bouchon* Paris 20-40 €, *Le Tire-Bouchon Rodier* 30-70 €, crêperie, bar à vin, grossiste), un carrousel produit dense, et un bloc organique produit.

**Intention : partiellement.** La requête désigne le produit **et** une enseigne de restaurant très répandue **et** un train touristique SNCF (ligne Auray–Quiberon).

**Commercial vs informationnel :** 3 positions organiques sur 9 sont non commerciales (toutautourduvin.fr guide, Wikipédia, ter.sncf.com). Une collection seule ne prendra pas la page entière.

**Qui tient la page 1 :**

| Spécialistes / DTC | Marketplaces & enseignes | Marques | Éditorial / hors-sujet |
|---|---|---|---|
| **bontirebouchon.fr** (« N°1 du Tire-bouchon »), **lebontirebouchon.com** (retours 365 j), tire-bouchon-design.com (100 % français, personnalisable) | Amazon (1 position organique) | atelierduvin.com (**2 positions**) | toutautourduvin.fr, Wikipédia, ter.sncf.com |

→ **3 spécialistes / 1 marketplace sur 9 en organique.** **Deux boutiques mono-produit tire-bouchon existent et tiennent la page 1.** En mode UNIVERS, c'est une **preuve de marché**, pas une occupation (§4 des critères).

**Bande de prix observée (2026-08-28) : 1,99 € – 79,95 €.** Socle GSB 1,99–8,99 € (BUT, Carrefour, Conforama 2,00 €, IKEA 3,99 €) · milieu 13,79–29 € (Vacu Vin, Bontirebouchon 19,90 €, Peugeot 19,99–22,89 €, L'Atelier du Vin 22,50 €) · haut 48,95–79,95 € (L'Atelier du Vin de Gaulle, Peugeot Souverain/Baltaz, Cuisinart, Ogo chez Maisons du Monde 59,95 €).

**Volume : retenu avec retrait.** Retrait estimé **15 %** de la tête (12 100) pour l'intention locale/restaurant/train non captée par les exclusions lexicales → **−1 800**. *Estimation, pas mesure.*

### 4.2 `limonadier` — Ouverture

**Ce que Google sert.** Un bloc **« Produits Sponsorisés » confirmé** (3 fiches : L'Atelier du Vin Oeno Motion 139 €, Comptoir Du Consommable 240 unités 226,80 €, GGM Gastro lot de 6 78,53 €), puis une page produit dense.

**Intention : oui**, malgré l'ambiguïté du mot (le limonadier est aussi un **métier** de débitant de boissons).

**Commercial vs informationnel :** 2 positions éditoriales (Wikipédia, laboutiquedubarman.fr) + 1 hors-sujet emploi (Indeed).

**Qui tient la page 1 :**

| Spécialistes / DTC | Marketplaces & enseignes | Marques | Éditorial / hors-sujet |
|---|---|---|---|
| **limonadier.co** (spécialiste mono-produit, 2 positions), **bontirebouchon.fr**, **lebontirebouchon.com**, eurolam-thiers.com (coutellerie de Thiers) | **aucune** | peugeot-saveurs.com | Wikipédia, laboutiquedubarman.fr, Indeed |

→ **4 spécialistes / ZÉRO marketplace en organique.** C'est la meilleure structure concurrentielle de tout le dossier, avec `carafe a vin`.

**Bande de prix (2026-08-28), hors lots B2B : 3,90 € – 50,99 €.** Cœur 8,90–37,90 €. Comparable indépendant : Bontirebouchon 17,90–29,90 €, Le Bon Tire-Bouchon 32,99–50,99 €. Les lots B2B (78,53 € les 6, 226,80 € les 240) relèvent du goodies publicitaire, pas de notre marché.

**Volume : retenu avec retrait.** Retrait estimé **20 %** de la tête (9 900) pour l'intention métier/définition (Indeed + Wikipédia + les grappes `limonadier def`, `métier`, `cqp`, `ceinture`, déjà exclues lexicalement) → **−2 000**. *Estimation.*

### 4.3 `carafe a vin` — Aération

**Ce que Google sert.** Une page **franchement commerciale et franchement spécialiste**. Aucun pack local, aucun hors-sujet.

**Intention : oui**, sans réserve.

**Commercial vs informationnel :** 2 positions éditoriales sur 10 (vessiere-cristaux.fr blog, larvf.com banc d'essai). 8 positions vendent.

**Qui tient la page 1 :**

| Spécialistes / DTC | Marketplaces & enseignes | Marques | Éditorial |
|---|---|---|---|
| **verasco.fr**, **toutautourduvin.fr**, **lasablerie.com**, **latabledarc.com**, **vinatis.com** | Amazon (1) | villeroy-boch.fr | vessiere-cristaux.fr, larvf.com |

→ **5 spécialistes / DTC, 1 marque, 1 marketplace sur 10.** C'est le profil « *boite a montre* » de Noirmont : une concurrence **de même nature que nous**, pas une porte fermée. **Vinatis, la preuve de confiance A du dossier de phase 2, est bien là — en 9ᵉ position, pas en tête.**

**Bande de prix (2026-08-28) : 0,78 € – 99,99 €.** Carafe de service basique 0,78–14,99 € (Prestaloc, Arcoroc, H&M, IKEA 19,99 €) · **cœur carafe à décanter 18–40 €** (Wadiga/Maisons du Monde 18–24 €, CleverlyFound 25,90 €, aérateurs Amazon 27,29–39,99 €, Metro 29,95 €, Leroy Merlin 29,98 €, Ferm Living 38,95 €, La Redoute BarCraft 39,90 €) · **haut 49,99–99,99 €** (Peugeot Evolution 49,99, Capitaine 65,90, Ibis 69,90, Variation 99,99 ; L'Atelier du Vin bonde 71,50 ; Alaskan Maker Topographic 75,00).

**Palier haut entièrement tenu par des marques à récit** (Peugeot, L'Atelier du Vin, Alaskan Maker). Le comparable indépendant plafonne à ~40 €. **Vide observé entre 40 € et 50 €.**

**Volume : retenu.** Retrait de **700** pour les grappes `carafe a vin montagne / topographic / mont blanc` (420 + variantes), identifiées en SERP comme désignant le modèle **Alaskan Maker Topographic à 75 €** — marque cachée dans un mot d'apparence générique (contrôle n° 4).

### 4.4 `bouchon vin` — Conservation

**Ce que Google sert.** Une page **à deux intentions superposées** : bouchons de **conservation réutilisables** et bouchons de **liège/plastique pour embouteiller son vin**.

**Intention : partiellement.**

**Qui tient la page 1 :**

| Spécialistes / DTC | Marketplaces & enseignes | Marques | Autre intention (embouteillage) |
|---|---|---|---|
| **lebontirebouchon.com**, **toutautourduvin.fr** (collection « Conservation du vin ») | Amazon (1 organique) ; ManoMano, Cdiscount, Darty, Leroy Merlin, Gamm Vert, Mr Bricolage, Carrefour en carrousel | vacuvin.com, atelierduvin.com, coravin.fr | **liege24.fr**, **embouteille.com** |

→ **2 spécialistes de notre métier / 3 marques / 2 spécialistes d'un autre métier (l'embouteillage) / 1 marketplace.** La page est partagée à peu près **moitié-moitié** entre les deux intentions.

**Bande de prix (2026-08-28) : 1,85 € – 44,99 €.** Cœur 6–25 €. Le seul palier au-dessus de 30 € : Alessi 29,00 €, Le Bon Tire-Bouchon 29,99 € et Deluxe 44,99 €. **Famille structurellement low-ticket.**

**Volume : retenu avec retrait.** Retrait estimé **40 % de la tête** `bouchon vin` (590) et de ses variantes génériques pour l'intention embouteillage confirmée en SERP. Les grappes liège (680) et plastique/synthétique de vinification (≈ 1 080) sont sorties du net. Voir la fourchette au §6.

### 4.5 `coffret sommelier` — Coffret

**Ce que Google sert.** Un bloc **« Produits Sponsorisés » confirmé de 4 fiches, TOUTES L'Atelier du Vin, à 139 € / 150 € / 340 € / 800 €, livraison gratuite.** Puis une page produit très étalée en prix.

**Intention : oui**, commerciale et cadeau.

**Qui tient la page 1 :**

| Spécialistes / DTC | Marketplaces & enseignes | Marques | Autres |
|---|---|---|---|
| **lebontirebouchon.com**, magravureperso.fr, atelierbox.fr, mon-droguiste.com | Amazon (1), dubruitdanslacuisine.fr | atelierduvin.com, pradel-excellence.fr | boutique-sylvaplana.com (domaine viticole) |

→ **4 spécialistes / 1 marketplace sur 9.** Porte ouverte en organique. **Mais le haut de gamme payant est verrouillé** : L'Atelier du Vin achète les 4 slots Shopping sponsorisés de la tête, à 139–800 €, avec livraison gratuite.

**Bande de prix (2026-08-28) : 6,90 € – 1 710 €. Bande BIMODALE, avec deux vides :**

| Palier | Prix | Acteurs |
|---|---|---|
| Cadeau GSB | 6,90 – 31,90 € | Leclerc 8,99 · Secret de Gourmet 9,99/21,99 · La Chaise Longue 12,49 · Pradel 14,95/31,90 · Nature & Découvertes 14,90 · Veepee 18,99 · Gamm Vert 19,95 · Atmosphera 24,99 · Fnac 29,99 |
| **VIDE** | **32 – 49 €** | — |
| Milieu | 49,99 – 61,99 € | La Chaise Longue 49,99 · Maverton 52,90 · Le Bon Tire-Bouchon 61,99 |
| **VIDE** | **62 – 94 €** | — |
| Haut indépendant | 94,99 – 137,99 € | Le Bon Tire-Bouchon Fleurance 94,99 / Rabbit Up 122,99 · L'Atelier du Vin Oeno Sommelier Box 132,99 · Les Décapsuleurs Luxe 137,99 |
| Marque à récit | 150 – 1 710 € | L'Atelier du Vin (Oeno Collection 4 150 €, Le Globe 340 €, Oeno Motion Groom 615 €, Oeno Box 800 €, Coffret Bois 1 710 €) |

**C'est la seule famille du dossier dont le créneau prix atteint le plancher maison de 50–400 €.** Le comparable — indépendant, sans récit de marque — se situe **entre 95 et 138 €**. Se placer « juste sous le plus cher » donnerait 145 €, en plein dans le territoire L'Atelier du Vin ; le vide 62–94 € n'est pas une place à prendre (étape 9, piège des bandes bimodales).

**Volume : retenu avec retrait.** Le cluster `coffret vin` (3 631 kw / 32 190) est **majoritairement un marché d'alcool** : `coffret vin rouge`, `coffret vin bordeaux`, `coffret 3 bouteilles de vin`, `abonnement coffret vin` (CPC 2,26 EUR), Nicolas / Leclerc / Carrefour en grappe. **Environ 28 000 de ce cluster sont retirés** : vendre du vin est un autre métier (licence, policy alcool Merchant Center, restrictions de transport). Seule la part **accessoire** est conservée.

### 4.6 `verre a vin` — Verrerie → **FAMILLE RETIRÉE**

**Ce que Google sert.** Un carrousel produit massif dominé par la grande distribution et un organique tenu par les **verriers**.

**Intention : oui** (achat de verres), mais le marché n'est pas défendable.

**Commercial vs informationnel :** 2 positions éditoriales sur 9 (toutautourduvin.fr, wineandco.com).

**Qui tient la page 1 :**

| Spécialistes / DTC | Marketplaces & enseignes | **Marques verrières** | Éditorial |
|---|---|---|---|
| latabledarc.com, wineandbarrels.fr (revendeur de marques) | en carrousel : **IKEA (7 références distinctes)**, **BUT**, **Conforama**, **JYSK**, **Maisons du Monde (3)**, Boulanger, Cdiscount, Amazon, Metro, Atmosphera, H&M | **lehmann-sa.com, degrenne.fr, zwiesel-glas.com, spiegelau.com, riedel.com** | toutautourduvin.fr, wineandco.com |

→ **5 marques verrières officielles en organique sur 9.** Zéro marketplace en organique — mais aucun espace non plus : **la page appartient aux verriers**.

**Bande de prix (2026-08-28) : 0,79 € – 57,00 €.** IKEA ÄNKEBLOMSTER **0,79 €**, BUT 1,99 €, Conforama 1,99 €, IKEA RÖDRÄKA 2,49 €, DYRGRIP 5,49 €, SVALKA 6,99 €, Du Bruit dans la Cuisine 7,95 €, Atmosphera lot de 6 8,94 €, JYSK 11,50 €, IKEA FRÖJDA 12,99 €, STORSINT 14,99–17,99 €, H&M 14,99 €, Maison Sarah Lavoine 17,00 €, IKEA STOCKHOLM 19,99 €, Maisons du Monde 23,94 €, Chef & Sommelier 34,90 €, Stölzle 39,80 €, Maisons du Monde 45,00 €, Boulanger 47,90 €, Chef & Sommelier 57,00 €. **Environ la moitié du carrousel est sous 15 €.**

**Volume : RETIRÉ intégralement — ≈ 52 000 net.** Motif, en trois points cumulés :
1. `PRODUCT-RESEARCH-CRITERIA.md` **§4** rejette explicitement les catégories dominées par **IKEA, BUT, Conforama, JYSK, Maisons du Monde**. Les cinq y sont, simultanément, sur la même page.
2. L'organique est verrouillé par **cinq marques verrières** (Riedel, Spiegelau, Zwiesel, Lehmann, Degrenne) qui vendent une notoriété.
3. La bande de prix démarre à **0,79 €** et le prix unitaire courant est de 2 à 17 €. Aucun ratio défendable face au plancher maison.

C'est **le retournement de famille de ce dossier**, l'équivalent des 3 familles sur 20 de Noirmont. Sans cette vérification, la Verrerie serait entrée au consolidé pour ~52 000 et aurait porté à elle seule la moitié du dossier.

*Sous-famille conservée à part, non comptée : `verre inao` (≈ 3 610 net, CPC 0,55–0,63 EUR). C'est le vocabulaire spécialiste, avec un CPC double du générique et sans domination GSB visible dans sa grappe. À remesurer si Hakim veut instruire la verrerie sous cet angle-là seulement.*

---

## 5. `cave à vin` — mesurée séparément, retirée, documentée à part

Le piège annoncé au brief est **confirmé, et il est plus gros qu'annoncé.**

| Mesure 2026-08-28 | Valeur |
|---|---|
| Tête `cave a vin` | **60 500** (KD 41, CPC 0,26 EUR) |
| Cluster | **43 225 mots-clés · 401 220 de volume total · 433 pages** |
| 100ᵉ ligne de la page 1 | 480 → **plancher majeur** |

**Composition de la grappe (barre latérale SEMrush, par nombre de mots-clés) :** `sommeliere` 1 181 · `liebherr` 1 049 · `encastrable` 1 009 · `climadiff` 924 · `darty` 412 · `candy` 306 · `boulanger` 274 · `clayette` 271 · `notice` 312 · `filtre` 312 · `hygrométrie` 247.

**Marques d'électroménager identifiées dans la traîne :** La Sommelière, Liebherr, Climadiff, Haier, Candy, Klarstein, Caviss, Thomson, Artevino, Valberg, Le Chai, Signature. **Enseignes :** Darty, Boulanger, Electro Dépôt, BUT, IKEA, Conforama.

**Second sens détecté :** `cave a vin autour de moi` (3 600), `cave a vin near me` (1 000), `cave a vin paris` (480) = recherche de **caviste local**, pas d'appareil.

**Décision : retirée du consolidé.** Trois motifs :
1. **Autre produit** — un réfrigérateur, pas un accessoire.
2. **Autre ticket** — 300 à 2 000 €, hors de la logique de panier composé du reste de l'univers.
3. **Autre boutique** — marché d'électroménager tenu par Darty/Boulanger/Electro Dépôt et une douzaine de marques installées, exactement l'exclusion §4.

**Elle n'est pas effacée : elle est documentée ici.** Si Hakim veut instruire l'électroménager vin, c'est un dossier autonome, avec sa propre phase 0. Ce n'est pas ce candidat.

*Non mesuré : `cave à vin` accentué, `armoire à vin`, `cave de vieillissement`. Sans objet pour ce dossier puisque la famille est retirée ; à faire si le dossier électroménager est ouvert.*

---

## 6. Volume consolidé retenu

Après application des exclusions lexicales, du net de marque, des recoupements mesurés et des retraits SERP.

| # | Famille | Net de marque | Retrait SERP | **Consolidé retenu** |
|---|---|---:|---:|---:|
| 1 | Ouverture | 54 300 | −3 800 (local/restaurant/train 15 % · métier 20 %) | **50 500** |
| 2 | Aération | 29 300 | −700 (marque cachée Alaskan Maker) | **28 600** |
| 3 | Conservation | 15 900 | −1 400 (embouteillage) | **14 500** |
| 4 | Accessoires du vin (parent) | 5 840 | 0 | **5 840** |
| 5 | Coffret accessoires | 5 400 | −1 400 (part alcool + Le Nez du Vin) | **4 000** |
| 6 | Œnologie — part produit | 2 060 | 0 | **2 060** |
| | **TOTAL** | **112 800** | **−7 300** | **≈ 105 500** |

### Ce qui a été retiré, et son poids

| Retiré | Volume | Motif |
|---|---:|---|
| **Verrerie** | ≈ 52 000 | SERP §4.6 — IKEA/BUT/Conforama/JYSK/MdM + 5 marques verrières ; prix 0,79–57 € ; §4 des critères |
| **Cave à vin** | cluster 401 220 | §5 — électroménager, autre famille, autre boutique |
| **Œnologie hors produit** | ≈ 70 000 | cours, formations, BTS/BTSA, laboratoires, séjours, team building. `oenologie` (6 600) est un mot d'**école et de service**, pas de boutique |
| **Coffret contenant des bouteilles** | ≈ 28 000 | vente d'alcool — licence, policy alcool Merchant Center, transport |
| **Conservation informationnelle** | ≈ 31 000 | `conservation vin` (32 660 de cluster) est à ~95 % « combien de temps se garde un vin ouvert », plus une contamination franche par les **maquereaux au vin blanc en conserve** (≈ 1 000) |
| **« sans tire bouchon »** | ≈ 5 500 | « comment ouvrir une bouteille sans tire-bouchon » — problème, pas panier |
| **Restaurants / lieux / SNCF** | ≈ 25 000 | *Le Tire-Bouchon*, *Le Décanteur* Pessac, *Le Limonadier* Lyon, *Le Verre à Vin* Plabennec, train Auray–Quiberon |
| **Filtres décanteurs gasoil / tracteur / bateau** | ≈ 2 000 | `decanteur` est d'abord une pièce de moteur agricole et marine |
| **B2B / CHR / publicitaire** | ≈ 1 500 | ceinture de serveur, goodies 240 unités, grossiste, pompes de transfert de cave |

### Positionnement contre le seuil UNIVERS

> **Seuil UNIVERS applicable : 30 000/mois de volume consolidé par familles, confort 40 000** (`PRODUCT-RESEARCH-CRITERIA.md` §1).

**Consolidé net retenu ≈ 105 500/mois — soit 3,5 fois le seuil de 30 000 et 2,6 fois le seuil de confort de 40 000.**

Le seuil est franchi **très largement**, et il le reste dans toutes les hypothèses défavorables :

- Les **deux seules familles au verdict SERP franc** (Ouverture 50 500 + Aération 28 600) pèsent déjà **79 100**, soit 2,6 × le seuil.
- Si l'on retirait **entièrement** l'Ouverture — la famille au retrait le plus discutable — il resterait **55 000**, encore au-dessus du confort.
- Si l'on ne gardait que l'**Aération**, la famille au meilleur profil SERP, on serait à **28 600**, à −5 % du seuil.
- Trois familles sont des **planchers** (Ouverture, Conservation, et la Verrerie retirée) : le vrai chiffre est **au-dessus** de 105 500, pas en dessous.

**Ce n'est pas un cas limite.** La zone de cas limite (±20 % du seuil de 30 000) est 24 000–36 000 ; le consolidé est à 105 500, très au-delà. Je tranche donc le volet volume, comme la méthode me le demande.

---

## 7. Bande de prix observée

Tous relevés en SERP réelle google.fr le **2026-08-28**. Ce ne sont **pas** des sondes Google Shopping dédiées.

| Famille | Bande observée | Cœur de marché | Comparable indépendant (sans récit de marque) | Palier marque à récit |
|---|---|---|---|---|
| Tire-bouchon | 1,99 – 79,95 € | 15 – 30 € | Bontirebouchon 19,90 € | Peugeot 54,90–79,95 · L'Atelier du Vin 48,95 € |
| Limonadier | 3,90 – 50,99 € | 9 – 35 € | Bontirebouchon 17,90–29,90 · Le Bon TB 32,99–50,99 € | L'Atelier du Vin 139 € (sponsorisé) |
| Carafe / décanteur | 0,78 – 99,99 € | 20 – 40 € | Maisons du Monde 18–24 · La Redoute 39,90 € | Peugeot 49,99–99,99 · Alaskan Maker 75 € |
| Bouchon / pompe | 1,85 – 44,99 € | 6 – 25 € | Le Bon TB 29,99–44,99 € | Vacu Vin 6,79–17,50 · Le Creuset 21,85 € |
| **Coffret sommelier** | **6,90 – 1 710 €** | bimodal | **Le Bon TB 94,99–122,99 · Les Décapsuleurs 137,99 €** | **L'Atelier du Vin 150–1 710 €** |
| *Verrerie (retirée)* | *0,79 – 57 €* | *2 – 17 €* | *—* | *Riedel, Spiegelau, Chef & Sommelier* |

**Vides de marché relevés** (à ne pas venir occuper — étape 9) : **32–49 €** et **62–94 €** sur le coffret sommelier ; **40–50 €** sur la carafe.

**Constat structurant.** Le plancher maison est de **50 à 400 € TTC** (`PRODUCT-RESEARCH-CRITERIA.md` §1 : « un gadget drop 15–20 € n'est pas un candidat »). **Cinq familles sur six ont un cœur de marché entre 6 et 40 €.** Seul le **coffret sommelier** atteint nativement le plancher, avec un comparable indépendant à 95–138 € — et il ne pèse que ≈ 4 000, soit **3,8 % du consolidé**.

L'économie de ce candidat repose donc entièrement sur le **panier composé** : plusieurs accessoires à 15–40 € assemblés dans une même commande, ou des coffrets construits par la boutique. C'est exactement la logique UNIVERS. **Mais elle n'a jamais été validée à la maison, et aucun chiffre de ce rapport ne la démontre.**

**Correction d'un chiffre du dossier de phase 2.** Le rapport de préparation annonçait « bande documentée : coffrets 147–480 €, accessoires 6–85 € ». La bande haute 147–480 € est **exacte mais trompeuse** : elle décrit **L'Atelier du Vin seul**, une marque française à récit qui achète les quatre slots Shopping sponsorisés de `coffret sommelier` à 139–800 €. Ce n'est pas un palier accessible, c'est un palier occupé.

**Ratio prix ÷ CPC.** Sur les CPC mesurés (0,16 à 0,44 EUR sur le cœur du dossier), un prix de 30 € donne un ratio de 68 à 190 ; un prix de 100 € sur le coffret (CPC 0,32 EUR) donne **312**, largement au-dessus de la cible 150–200. **Le coffret est la seule famille dont l'économie publicitaire est confortable.** Sur `coffret vin` en revanche, le CPC monte à 0,78–2,26 EUR — mais c'est la part alcool, hors périmètre.

---

## 8. Réserves — aucune retirée

1. **Le plancher de prix est l'obstacle central.** Cœur de marché 6–40 € sur cinq familles sur six, contre un plancher maison à 50 €. Le dossier ne tient que si le panier composé fonctionne, et **rien ici ne le prouve**. C'est une décision d'offre, pas une mesure ; elle appartient à Hakim.

2. **Google Trends n'a pas été fait.** L'exigence UNIVERS d'un **socle hors Q4 d'environ 8 mois au-dessus d'un plancher visible** n'est donc **pas vérifiée**. Le vin & œnologie porte un risque de saisonnalité cadeau (Noël, fête des pères) que ce rapport ne mesure pas. **Réserve bloquante avant toute décision.**

3. **Trois familles sont des planchers de lecture**, pas des totaux : Ouverture (188 pages, 100ᵉ ligne à 320), Conservation (54 pages), et la Verrerie retirée (82 + 61 pages). Le consolidé de 105 500 est **minoré**.

4. **L'Atelier du Vin occupe le haut de gamme payant.** Marque française installée, quatre slots Shopping sponsorisés confirmés sur `coffret sommelier` à 139–800 € avec livraison gratuite, deux positions organiques sur `tire bouchon`. En UNIVERS c'est une preuve de marché (§4), mais c'est aussi un mur sur le seul segment de prix compatible avec le plancher maison.

5. **Deux boutiques mono-produit déjà installées** (bontirebouchon.fr, lebontirebouchon.com, cette dernière avec 365 jours de retour) tiennent la page 1 sur **trois têtes de famille sur cinq**. Preuve que le modèle existe — et que la place n'est pas vide.

6. **La contamination locale est massive et permanente.** *Le Tire-Bouchon*, *Le Décanteur*, *Le Limonadier*, *Le Verre à Vin* sont des noms de restaurants et de bars à vin extrêmement répandus en France, plus un train touristique SNCF. Environ **25 000 recherches** ont été retirées à ce titre. Le nom de la future boutique devra éviter ces formes, sous peine de se battre contre des packs locaux.

7. **`bouchon vin` est partagé à parts à peu près égales** entre conservation et embouteillage (liege24.fr, embouteille.com en page 1). La fourchette adressable de la Conservation est **11 600 à 13 800** hors pompes, et non un chiffre unique. Fourchette honnête plutôt que total faux.

8. **Le coffret de vin est un marché d'alcool.** Environ 28 000 retirés. Toute reprise du mot « coffret » sans qualificatif ramènera cette intention, avec les CPC les plus chers du dossier (jusqu'à 2,26 EUR sur `abonnement coffret vin`) et un risque de policy Merchant Center.

9. **Impossible d'isoler les annonces Search texte.** Seules deux SERP (`limonadier`, `coffret sommelier`) exposent un bloc « Produits Sponsorisés » explicite — ce sont des **annonces Shopping confirmées**. Partout ailleurs, la pression publicitaire réelle n'est pas mesurée.

10. **Tous les pourcentages de retrait SERP sont des estimations** faites à la composition de la page 1 : 15 % sur `tire bouchon`, 20 % sur `limonadier`, 40 % sur `bouchon vin`. Ce ne sont pas des mesures.

11. **Sous-familles non mesurées** : `cave à vin` accentué, `armoire à vin`, `service du vin`, `verre à pied`, `verrerie` parent, `verre dégustation` en racine autonome. Les trois premières relèvent de familles retirées ; les trois dernières relèvent de la Verrerie, retirée.

12. **Aucune cartographie de concurrence n'a été faite** (étape 7 de la méthode) : les acteurs cités ne le sont qu'au titre de la lecture de page 1. Aucun trafic, aucune arborescence, aucun prix par famille n'a été relevé chez eux.

13. **Aucun sourcing.** Le plancher de sourçabilité UNIVERS de `PRODUCT-RESEARCH-CRITERIA.md` §0.6 — les 3 à 5 familles pesant ≥ 70 % du consolidé doivent avoir chacune ≥ 2 fournisseurs plausibles — n'est **pas instruit**. Sur ce dossier, les familles concernées seraient Ouverture, Aération et Conservation (93 700, soit 89 % du consolidé). C'est la phase 4.

---

## 9. Verdict

### `REVIEW_PREQUALIFICATION`

**Le volet volume est franchi, nettement.** Le consolidé net de marque, vérifié en SERP, atteint **≈ 105 500 recherches/mois** contre un **seuil UNIVERS de 30 000** et un confort de 40 000 (`PRODUCT-RESEARCH-CRITERIA.md` §1). Il reste au-dessus du seuil dans toutes les hypothèses défavorables testées au §6, et trois des familles retenues sont des planchers de lecture — le vrai chiffre est supérieur. La structure concurrentielle est favorable là où elle compte : sur `limonadier` **zéro marketplace en organique**, sur `carafe a vin` **cinq spécialistes/DTC sur dix positions et une seule marketplace**. Des boutiques mono-produit prospèrent déjà sur ces requêtes : en UNIVERS, c'est une preuve, pas une occupation.

**Ce n'est pas un `PASS` pour une raison précise, et une seule : le prix.**

Le cœur de marché mesuré est de **6 à 40 €** sur cinq familles sur six. Le plancher de la maison est de **50 €**, et `PRODUCT-RESEARCH-CRITERIA.md` §1 est explicite : « un gadget drop 15–20 € n'est pas un candidat ». La seule famille qui atteint nativement 50–400 € est le **coffret sommelier**, dont le comparable indépendant se situe à 95–138 € — et elle ne pèse que **≈ 4 000, soit 3,8 % du consolidé**. Au-dessus de 150 €, les quatre slots Shopping sponsorisés appartiennent à **L'Atelier du Vin**.

Le dossier ne tient donc que si le **panier composé** porte l'économie : plusieurs accessoires à 15–40 € par commande, ou des coffrets assemblés par la boutique. C'est la logique UNIVERS elle-même, mais elle n'a jamais été validée à la maison et **aucun chiffre de ce rapport ne la démontre**. Un panier moyen n'est pas un volume de recherche : c'est une hypothèse d'offre. **Elle appartient à Hakim, pas à moi.**

Il faut y ajouter la réserve n° 2 : **Google Trends n'a pas été fait**, donc l'exigence UNIVERS d'un socle hors Q4 d'environ 8 mois **n'est pas vérifiée**. Sur un univers à forte composante cadeau, c'est bloquant avant toute décision.

### Ce que ce verdict autorise et n'autorise pas

- **Il n'autorise pas** la due diligence sourcing + concurrence. Un `REVIEW` remonte à Hakim.
- **Il ne prononce aucun `GO_FINAL`.** Ce n'est pas mon rôle, et `PRODUCT-RESEARCH-CRITERIA.md` §0.6 l'interdit de toute façon tant que la sourçabilité par famille n'est pas documentée.
- **Il ne rouvre pas la Verrerie ni la Cave à vin**, retirées sur preuve SERP et documentées à part.

### Les trois arbitrages attendus de Hakim

1. **Le plancher de prix.** Accepte-t-on un univers dont le cœur est à 15–40 €, en pariant sur le panier composé ? Ou exige-t-on que chaque famille tienne 50 € en prix unitaire — auquel cas seul le coffret survit, à 4 000 de volume, et le dossier tombe ?
2. **Google Trends.** À faire avant tout — socle ≥ 8 mois. Je peux le lancer sur `tire bouchon`, `carafe a vin` et `coffret sommelier` sur demande.
3. **Le périmètre.** Confirme-t-on le retrait de la Verrerie (≈ 52 000, §4.6) et de la Cave à vin (cluster 401 220, §5) ? Les deux retraits sont argumentés en SERP, mais ils enlèvent au dossier son volume le plus voyant, et cette décision doit être vue plutôt que subie.

---

*Rapport produit le 2026-08-28. Toutes les mesures SEMrush sont datées du 2026-08-28, base France (`db=fr`), expression exacte, devise EUR. Contrôle témoin `tufting` = 8 100 avant et après. Toutes les lectures SERP sont datées du 2026-08-28, google.fr `hl=fr&gl=fr`, session non connectée. Aucun sourcing, aucun contact vendeur, aucune décision commerciale.*

# Mission B — Analyse de marché UNIVERS — « Rideaux, matière × intention »

**Date : 2026-08-28** · Mode **UNIVERS** · Candidat #17 de la shortlist 30×30 · Méthode : `METHODE-ANALYSE-MARCHE.md` étapes 2 à 5 + 9, `PRODUCT-RESEARCH-CRITERIA.md` §1, skill `recherche-mots-cles` Mission B.

**Seuil applicable : volume consolidé par familles ≥ 30 000/mois (confort 40 000).** Le seuil PRODUIT PUR de 10 000 par cluster ne s'applique pas ici.

---

## 1. Entrée et méthode

### 1.1 Outil et protocole

- SEMrush **Keyword Magic Tool**, **base France** (`db=fr`), **expression exacte** (`mt=phrase`), devise **EUR** (`currency=eur`), 100 lignes par graine, 0 crédit consommé.
- URL type : `https://fr.semrush.com/analytics/keywordmagic/?q=<expression>&db=fr&mt=phrase&currency=eur`
- Base France confirmée sur chaque page (bandeau « Base de données : France », « Devise : EUR »).
- **Tous les CPC de ce rapport sont en EUR**, pas en dollars. La règle maison « CPC en dollars » ne s'applique pas à cette session, dont l'URL porte `currency=eur`.
- Onglet Chrome dédié créé pour cette mission, fermé en fin de tâche. Trois autres agents travaillaient en parallèle sur le même navigateur ; aucun de leurs onglets n'a été touché.

### 1.2 Contrôle témoin — avant et après

| Moment | Lecture | Résultat |
|---|---|---|
| **Avant la première mesure** | `?q=tufting&db=fr&mt=phrase` | ligne `tufting` = **8 100** ✅ |
| **Après la dernière mesure** | `?q=tufting&db=fr&mt=phrase` | ligne `tufting` = **8 100** ✅ |

Le témoin est identique en entrée et en sortie : **aucun zéro silencieux, quota non épuisé, session valide sur toute la chaîne**. Aucune mesure de ce rapport n'est suspecte de ce fait.

### 1.3 Les cinq contrôles, appliqués à chaque passe

1. **Deux orthographes.** `lavé`/`lave`, `lumière`/`lumiere`, `tringle à rideau`/`tringle a rideau`, et les deux fautes fréquentes demandées (`termique`, `fonique`). Résultats en §2.4 — contrairement au cas mémoire « ciel étoilé », **SEMrush ne sépare pas les accents ici** : `rideau lin lavé` et `rideau lin lave` rendent le même corpus (4 120 tous deux).
2. **Plusieurs niveaux de généralité.** Trois niveaux par famille (mot de la maison → mot du particulier → catégorie parente), **mesurés séparément, jamais additionnés**. Détail en §5.
3. **`n/a` ≠ `0`.** Les deux sont écrits distinctement dans ce rapport. `n/a` = sous le seuil de restitution SEMrush (< 10/mois). Une graine a rendu **0 ligne** (`rideau qui bloque la lumiere`) : ce n'est ni `n/a` ni `0`, c'est **aucune ligne restituée**, et c'est écrit comme tel.
4. **Mot-clé témoin** — voir §1.2.
5. **Plancher de lecture.** Le KMT rend 100 lignes. Quand la 100e ligne est encore haute, le total est un **plancher**, pas un total. Signalé graine par graine en §2.

### 1.4 Limites de calcul, à lire avant les chiffres

- **Le « Volume total » affiché en tête de requête par SEMrush n'est jamais utilisé comme somme de famille.** Il agrège tout le corpus phrase-match, bruit compris. Il est reporté en §2 uniquement comme repère d'écart. Toutes les sommes de ce rapport sont des **sommes de lignes retenues une par une**.
- **La majorité des familles sont des planchers.** Sept graines sur vingt-six ont leur 100e ligne au-dessus de 250/mois. Les nets publiés sont donc des minorants, pas des totaux.
- **Les retraits par expression régulière** (marques, service, autres produits) ont été calculés dans le navigateur sur les 100 lignes de chaque graine. Ils sont exacts sur le périmètre lu, pas exhaustifs sur le marché.
- **Recoupement résiduel entre familles.** Les familles sont rendues disjointes par des exclusions croisées explicites (§3.1). Un contrôle sur la graine `tringle rideau` donne 0 ligne contenant `occultant`, `thermique`, `isolant`, `velours`, `lin` ou `voilage`, et 720 seulement contenant `anneau`/`embrasse`/`crochet` (déduits). Le double comptage résiduel est estimé sous 1 % ; il n'a pas été mesuré ligne à ligne sur les vingt-six graines.
- **SERP lues depuis le navigateur de Hakim**, donc **session connectée à un compte Google** — la consigne « session non connectée » n'a pas pu être respectée. Les classements peuvent être légèrement personnalisés. `hl=fr&gl=fr` forcés. À considérer comme une réserve, pas comme un vice rédhibitoire (les domaines relevés sont des acteurs nationaux, pas des résultats locaux).
- **Page 1 et page 2 seulement.** Interdit d'en déduire la profondeur réelle de la concurrence.
- **Aucun sourcing, aucune fiche fournisseur, aucun `GO_FINAL`.**

### 1.5 Graines contrôlées (26)

| Famille | Mot de la maison | Mot du particulier | Catégorie parente | Fautes testées |
|---|---|---|---|---|
| Occultation | `rideau occultant total` | `rideau occultant`, `rideau qui bloque la lumiere` | `rideau` | — |
| Thermique | `rideau isolant` (couvre `rideau isolant thermique`) | `rideau anti froid`, `rideau thermique` | `isolation fenetre` | `rideau termique` |
| Phonique | `rideau acoustique` | `rideau anti bruit`, `rideau phonique` | `isolation phonique` | `rideau fonique` |
| Velours | `rideau velours` | `rideau velours salon` (inclus dans la graine) | `rideau deco` | — |
| Lin | `rideau lin lavé` / `rideau lin lave` | `rideau lin`, `voilage lin` (inclus dans `voilage`) | `rideau naturel` (via `rideau deco`) | — |
| Accessoires | `tringle à rideau` / `tringle rideau`, `embrasse rideau` | `anneau rideau` | `accessoire rideau` | — |
| Graines dérivées ajoutées | `double rideau` (forme), `voilage` (famille propre), `rideau sur mesure` (piège §5) | | | |

Graines dérivées révélées par le KMT et rattachées : `double rideau` → nouvelle famille **Forme** ; `voilage` → nouvelle famille **Voilage** (arbitrage en §4) ; `rideau sur mesure` → **non adressable**, retirée et chiffrée en §5.

---

## 2. Mesure par graine — lecture du 2026-08-28

### 2.1 Tableau des graines

`Somme 100 l.` = somme des volumes des lignes réellement lues. `VT affiché` = « Volume total » de SEMrush, **repère seulement**. `100e` = volume de la dernière ligne rendue → plancher si élevé.

| # | Graine | Lignes | VT affiché | **Somme 100 l.** | 100e | Plancher ? |
|---|---|---|---|---|---|---|
| T | `tufting` (témoin) | 100 | — | 41 390 | 90 | tête = 8 100 ✅ |
| 1 | `rideau occultant` | 100 | 297 700 | **153 550** | 390 | **OUI** |
| 2 | `rideau occultant total` | 36 | 80 | **80** | 0 | non |
| 3 | `rideau qui bloque la lumiere` | **0** | — | — | — | **aucune ligne restituée** |
| 4 | `rideau` (parent) | 100 | 4 763 160 | **726 300** | 2 900 | **OUI, massif** |
| 5 | `double rideau` | 100 | 120 760 | **72 120** | 260 | **OUI** |
| 6 | `rideau thermique` | 100 | 216 150 | **142 580** | 260 | **OUI** |
| 7 | `rideau isolant` | 100 | 57 230 | **43 770** | 70 | OUI (léger) |
| 8 | `rideau termique` (faute) | 68 | 200 | **200** | 0 | non |
| 9 | `rideau anti froid` | 100 | 10 460 | **10 310** | 10 | non |
| 10 | `isolation fenetre` (parent) | 100 | 64 310 | **38 310** | 110 | OUI |
| 11 | `rideau anti bruit` | 100 | 8 910 | **8 790** | 10 | non |
| 12 | `rideau phonique` | 100 | 26 760 | **23 410** | 30 | non |
| 13 | `rideau acoustique` | 100 | 5 610 | **5 610** | 0 | non |
| 14 | `rideau fonique` (faute) | 2 | 0 | **0** | 0 | non |
| 15 | `isolation phonique` (parent) | 100 | 261 080 | **118 390** | 480 | **OUI** |
| 16 | `rideau velours` | 100 | 38 290 | **24 740** | 70 | OUI (léger) |
| 17 | `rideau lin` | 100 | 92 760 | **58 490** | 140 | **OUI** |
| 18 | `rideau lin lavé` | 100 | 4 140 | **4 120** | — | non |
| 19 | `rideau lin lave` (sans accent) | 100 | 4 140 | **4 120** | — | non |
| 20 | `voilage` | 100 | 385 080 | **133 600** | 480 | **OUI** |
| 21 | `tringle rideau` | 100 | 525 170 | **219 900** | 720 | **OUI, massif** |
| 22 | `embrasse rideau` | 100 | 30 520 | **24 640** | 30 | non |
| 23 | `anneau rideau` | 100 | 34 550 | **26 900** | 70 | OUI (léger) |
| 24 | `rideau sur mesure` | 100 | 28 620 | **22 030** | 50 | non |
| 25 | `rideau deco` (parent) | 100 | 7 300 | **5 450** | 20 | non |
| 26 | `accessoire rideau` (parent) | 100 | 6 750 | **6 750** | 0 | non |

**Écart VT affiché / somme réelle : de 1,1 à 6,6 fois.** Sur `rideau`, SEMrush affiche 4 763 160 quand les 100 lignes lues pèsent 726 300. C'est exactement le motif pour lequel le VT affiché ne sert jamais de total.

### 2.2 Têtes de famille — volume, KD, CPC (EUR), intention

| Mot-clé | Volume | KD | CPC (EUR) | Intention SEMrush |
|---|---|---|---|---|
| `rideau` | 40 500 | 30 | 0,44 | C |
| `rideaux` | 22 200 | 46 | 0,46 | C |
| `rideau occultant` | **33 100** | 32 | 0,41 | I |
| `rideaux occultants` | 18 100 | 31 | 0,41 | I |
| `rideau occultant thermique` | 9 900 | 27 | 0,33 | I |
| `rideau occultant total` | **30** | n/a | 0,39 | n/a |
| `rideau thermique` | **33 100** | 29 | 0,24 | I |
| `rideaux thermiques` | 9 900 | 31 | 0,24 | I |
| `rideau thermique anti froid` | 4 400 | 16 | 0,29 | C |
| `rideau isolant thermique` | 3 600 | 33 | 0,25 | T |
| `isolant thermique pour rideaux` | 3 600 | 15 | 0,25 | I |
| `rideau isolant` | 1 600 | 29 | 0,22 | C |
| `rideau anti froid` | 720 | 19 | 0,21 | C |
| `rideau phonique` | **4 400** | 15 | 0,67 | I |
| `rideau anti bruit` | 2 400 | 13 | 0,38 | I |
| `rideau acoustique` | 2 400 | 23 | 0,55 | I |
| `rideau isolant phonique` | 1 300 | 25 | 0,42 | I |
| `rideau velours` | 1 900 | 17 | 0,39 | I |
| `rideaux velours` | 1 900 | 17 | 0,39 | I |
| `rideau lin` | **5 400** | 19 | 0,41 | I |
| `rideau en lin` | 3 600 | 23 | 0,41 | I |
| `rideau lin lavé` | 590 | 11 | 0,40 | C |
| `rideaux voilage` | **12 100** | 31 | 0,26 | I |
| `voilage` | 8 100 | 27 | 0,29 | I |
| `rideaux et voilages` | 8 100 | 31 | 0,26 | I |
| `voilage lin` | 1 600 | 14 | 0,36 | C |
| `tringle rideau` | **18 100** | 23 | 0,20 | C |
| `tringle a rideau` | 14 800 | 22 | 0,16 | C |
| `tringle rideau sans percer` | 9 900 | 25 | 0,10 | I |
| `tringle à rideau` | 4 400 | 26 | 0,26 | C |
| `embrasse rideau` | 4 400 | — | — | — |
| `anneaux rideaux` | 1 900 | — | — | — |
| `double rideaux` | 4 400 | 20 | 0,30 | C |
| `rideau sur mesure` | 3 600 | 28 | **0,80** | I |
| `rideaux sur mesure` | 3 600 | 28 | **0,80** | T |

CPC de l'univers : **0,10 à 0,80 EUR**. Le sur-mesure est le seul poste à 0,80 EUR — signature d'un marché de prestation à forte valeur unitaire, et une raison de plus de le sortir (§5).

### 2.3 Contrôle « plusieurs niveaux de généralité » — le cas qui aurait tué le dossier

C'est la règle héritée du cas « suspension rotin XXL », et elle joue ici plein pot :

| Niveau | Expression | Volume |
|---|---|---|
| Mot de la maison | `rideau occultant total` | **30** |
| Mot du particulier | `rideau occultant` | **33 100** |
| Catégorie parente | `rideau` | **40 500** (grappe lue : 726 300, plancher) |

**Écart tête-de-maison / tête-de-client : ×1 103.** Conclure sur `rideau occultant total` (30/mois, KD n/a, grappe de 36 lignes pesant 80) aurait produit un STOP parfaitement faux. Le mot de la maison n'existe pas en France ; le mot du client pèse 33 100.

Même mécanique, en sens inverse, sur `rideau qui bloque la lumiere` : **aucune ligne restituée**. La périphrase du particulier supposée n'existe pas non plus. Le seul mot vivant est `occultant`.

### 2.4 Contrôle « deux orthographes » et fautes fréquentes

| Variante | Lignes | Volume | Lecture |
|---|---|---|---|
| `rideau lin lavé` | 100 | 4 120 | corpus identique |
| `rideau lin lave` | 100 | 4 120 | **corpus identique** — le KMT ne sépare pas les accents |
| `tringle à rideau` / `tringle a rideau` / `tringle rideau` | — | 4 400 / 14 800 / 18 100 | trois lignes distinctes **dans la même grappe** ; une seule graine suffit |
| `rideau termique` (faute) | 68 | **200** (tête 140) | aucun gisement caché |
| `rideau fonique` (faute) | 2 | **0** | aucun gisement caché |

Conclusion du contrôle : **pas d'écart d'accent exploitable sur ce dossier**, contrairement au précédent `ciel etoile` / `ciel étoilé` (×8). Les deux fautes demandées sont mortes (200 et 0). Elles sont écrites ici pour que personne n'ait à refaire la mesure.

---

## 3. Consolidation par familles

### 3.1 Règle d'affectation — un mot, une seule famille

Les graines phrase-match se recouvrent par construction (`rideau occultant thermique` sort à la fois sur `rideau occultant` et sur `rideau thermique`). Pour ne jamais compter un mot deux fois, une **priorité d'affectation** a été fixée avant tout calcul, et appliquée par exclusion croisée dans le navigateur :

> **Occultation > Phonique > Thermique > Matière (lin, velours) > Voilage > Forme (double rideaux) > Accessoires.**

Motif de l'ordre : l'intention d'usage prime sur la matière, parce que c'est elle qui porte les têtes de volume et qu'une page « Rideaux occultants » sert un acheteur qui cherche l'obscurité, quelle que soit la matière. Le phonique passe devant le thermique parce qu'il est l'intention la plus étroite et la plus chère (CPC 0,67 contre 0,24) : la noyer dans le thermique la rendrait invisible.

Conséquences concrètes, toutes vérifiables :
- `rideau occultant thermique` (9 900) → **Occultation**, retiré de Thermique.
- `rideau lin occultant` (1 000) → **Occultation**, retiré de Lin.
- `rideau isolant phonique` (1 300) → **Phonique**, retiré de Thermique.
- `double rideaux velours` (590) → **Velours**, retiré de Forme.
- `tringle rideau porte d'entrée isolant` → **Accessoires**, retiré de Thermique.

### 3.2 Familles — brut et net de marque

Marques et enseignes retirées : **IKEA, Leroy Merlin, Castorama, Brico Dépôt / Entrepôt du Bricolage, Gifi, Action, Amazon, Centrakor, La Redoute, Madura, Maisons du Monde, Heytens, Saint Maclou, Alinéa, Becquet, Conforama, Lidl, 4Murs, Blancheporte, Vertbaudet, Somfy, Velux, Moondream, Truffaut, Carrefour, Leclerc, Auchan, Cdiscount, Temu, Shein, Bouchara, Cyrillus, Linvosges, JYSK.**

| Famille | Graines | **Brut (lignes lues)** | Retraits documentés | **NET de marque** | Plancher ? |
|---|---|---|---|---|---|
| **Occultation** | `rideau occultant` | **153 550** | marques 42 300 (41 l.) · Velux 6 120 · tissu au mètre / doublure 2 880 · sur-mesure 720 | **101 530** (46 l.) | OUI |
| **Thermique** | `rideau thermique` + `rideau isolant` + `rideau anti froid` | 142 580 + 43 770 + 10 310 (chevauchants) | marques 21 670 + 770 + 890 · occultant 27 310 (→ Occultation) · phonique 5 030 (→ Phonique) · camping-car / rideau métallique industriel 280+ · service 980 | **≈ 104 900** = 68 440 (thermique hors isol) + 35 490 (isolant, règle unifiée) + ≈ 970 (froid pur) | OUI |
| **Phonique** | `rideau phonique` + `rideau anti bruit` + `rideau acoustique` | 23 410 + 8 790 + 5 610 | marques 1 340 + 690 + 220 (dont Moondream) · occultant 2 330 · service 510 + 60 + 150 | **30 880** = 18 200 + 7 980 + 4 700 | non |
| **Velours** | `rideau velours` | **24 740** | marques 1 980 · occultant 1 280 (→ Occultation) | **21 480** (82 l.) | OUI (léger) |
| **Lin** | `rideau lin` | **58 490** | marques 12 150 (21 %) · occultant 5 320 (→ Occultation) · voilage 1 750 (→ Voilage) · rideau de douche 1 750 | **37 520** (46 l.) | OUI |
| **Voilage** | `voilage` | **133 600** | marques 30 860 (23 %) · sur-mesure + tissu 2 320 · moustiquaire / store / voiture 960 | **99 460** (55 l.) | OUI |
| **Forme (doubles rideaux)** | `double rideau` | **72 120** | tringle 37 970 (→ Accessoires) · occultant 4 580 · thermique 2 690 · velours/lin 1 590 · marques 2 870 | **21 780** (30 l.) | OUI |
| **Accessoires** | `tringle rideau` + `embrasse rideau` + `anneau rideau` | 219 900 + 24 640 + 26 900 | marques 34 820 + 2 920 + 420 · placard/douche 2 300 + 2 470 · **recoupement mesuré tringle × (anneau/embrasse/crochet) = 720** | **227 790** = 182 780 + 21 720 + 24 010 − 720 | OUI, massif |

**Recoupement mesuré, pas estimé** (règle étape 3) : sur les 100 lignes de `tringle rideau`, les lignes contenant `occultant`, `thermique`, `isolant`, `velours`, `lin` ou `voilage` pèsent **0**. Les lignes contenant `anneau`, `embrasse` ou `crochet` pèsent **720**, déduites. Le recouvrement entre l'accessoire et le textile est donc quasi nul — ce sont bien deux vocabulaires disjoints.

### 3.3 Consolidé

| Périmètre | Brut | **Net de marque** |
|---|---|---|
| **Univers complet (8 familles)** | ≈ 830 000 (planchers, doublons inter-graines déduits) | **645 340** |
| Cœur textile seul (hors Accessoires) | — | **417 550** |
| Cœur « intention » seul (Occultation + Thermique + Phonique) | — | **237 310** |
| Famille la plus faible prise seule (Forme) | — | **21 780** |
| Famille de tête prise seule (Accessoires) | — | **227 790** |

**Les 3 familles pesant ≥ 70 % du consolidé** (repère §0.6 pour la sourçabilité en due diligence) : **Accessoires (227 790, 35 %) + Thermique (104 900, 16 %) + Occultation (101 530, 16 %) + Voilage (99 460, 15 %) = 82 %.** Ces quatre-là devront chacune avoir ≥ 2 fournisseurs plausibles avant toute décision finale — ce n'est pas l'objet de cette phase.

---

## 4. Arbitrage voilage vs rideau — motivé

**Question : `voilage` et `rideau` sont-ils une seule famille ou deux ?**

### Ce que la mesure dit

- Sur les 100 lignes de la graine `voilage` (133 600), **75 100 — soit 56 % — contiennent aussi le mot « rideau »** : `rideaux voilage` 12 100, `rideaux et voilages` 8 100, `voilage pour rideaux` 3 600, `voilages et rideaux` 2 900, `voilage et rideau` 2 400, `voilage rideau` 4 400, `rideau voilage` 5 400. Le client français nomme spontanément les deux dans la même requête.
- Symétriquement, `voilage` pèse **0** dans la graine `rideau occultant` et **1 750** seulement dans `rideau lin`. Le recouvrement est donc **fortement asymétrique** : le voilage appelle le rideau, le rideau occultant n'appelle jamais le voilage.

### Ce que la SERP dit

La page 1 de `voilage` (madura, bonsoirs, eminza, stores-discount, lamaisondesrideaux, veritable-macrame, heytens, decor-discount, castorama) est **la même population d'acteurs** que celle de `rideau occultant` (madura, stores-et-rideaux, stores-discount, homemaison, atmosphera, eminza…). Mais les URL d'arrivée sont, chez tous, **des collections distinctes** : « Voilages » d'un côté, « Rideaux occultants » de l'autre. Personne ne sert les deux requêtes avec la même page.

### Réponse

**Deux familles, un seul univers.** Le test « une page ou deux ? » tranche pour deux pages : le voilage est un textile **transparent** qui laisse passer la lumière, l'occultant un textile **opaque** qui la bloque — les deux intentions d'achat sont opposées, et aucune page ne peut promettre les deux. On ne les fusionne donc pas.

Mais ils appartiennent au **même catalogue et au même acheteur** (56 % de co-occurrence lexicale, acteurs identiques en SERP). En mode UNIVERS, les compter comme **deux collections d'un même catalogue est explicitement autorisé** par `PRODUCT-RESEARCH-CRITERIA.md` §1 (« additionner des collections d'un même catalogue n'est pas du gonflage »). En mode PRODUIT PUR, cette addition aurait été la faute canonique du cas « catio ».

**Le voilage est donc compté une fois, à part, pour 99 460 nets — et jamais additionné une seconde fois à l'intérieur d'une autre famille** (les 1 750 de voilage présents dans la graine `rideau lin` en ont été retirés).

### Réserve attachée à cet arbitrage

Le voilage apporte du **volume**, pas de la **marge** : médiane de prix observée ≈ 12 €, bande 3,90–49,99 €, CPC 0,29 EUR → **ratio prix ÷ CPC ≈ 41**, sous le plancher maison de 100. C'est une famille de trafic et d'entrée de catalogue, pas une famille de panier. Elle compte dans le consolidé ; elle ne doit pas porter l'économie de la boutique.

---

## 5. Volume sur-mesure et pose — mesuré, chiffré, retiré

Le piège annoncé au brief est réel et se chiffre.

| Élément | Lecture 2026-08-28 |
|---|---|
| Graine `rideau sur mesure` | 100 lignes, VT affiché 28 620, **somme des lignes lues 22 030**, 100e ligne à 50 → corpus couvert, ce n'est pas un plancher |
| Têtes | `rideau sur mesure` 3 600 (KD 28, **CPC 0,80 EUR**) · `rideaux sur mesure` 3 600 (KD 28, CPC 0,80 EUR) |
| Croisements | `rideau occultant sur mesure` 720 · `rideau sur mesure occultant` 320 · `rideaux occultants sur mesure` 320 · `rideau thermique sur mesure` 590 · `rideaux thermiques sur mesure` 390 · `voilage sur mesure` 1 600 |
| Requêtes de **pose / devis / installation / artisan / tapissier** dans la grappe | **0** |
| Requêtes de marque dans la grappe | Leroy Merlin 390 + 320 + 320 ; `mes rideaux sur mesure` 590 (navigationnel vers mesrideaux.fr) |

**Lecture.** Contrairement à l'hypothèse du brief, le sur-mesure français des rideaux **ne passe pas par la pose ni le devis d'artisan** : la grappe ne contient aucune requête de prestation à domicile. Elle est faite de **confection à dimensions vendue en ligne** (`rideaux sur mesure en ligne` 320). Le résultat est le même pour nous : **une confection aux dimensions du client n'est pas un article expédiable depuis un catalogue fournisseur.** Ce n'est pas un produit, c'est un service de fabrication.

**Retrait appliqué : 22 030/mois sortent du volume adressable.** Une partie était déjà déduite à l'intérieur des familles (720 dans Occultation, 2 320 dans Voilage) ; le solde n'a jamais été additionné. Le consolidé de 645 340 **n'en contient rien**.

**Retrait connexe, même logique :** le tissu au mètre et la doublure à coudre (`tissu occultant pour rideau` 480, `tissu pour rideaux occultants` 480, `tissus occultants rideaux` 480, `tissus pour rideaux occultant` 480, `doubler rideau occultant` 480, `rideaux doublés occultant` 1 000 …) — **2 880 retirés d'Occultation, 2 320 de Voilage**. C'est de la mercerie, pas du rideau fini.

**Autre retrait de nature « produit différent » :** la grappe **Velux** dans Occultation (`rideau occultant velux` 1 600, `rideau occultant pour velux` 1 300, `velux rideau occultant` 1 300, `rideau velux occultant` 720, `rideaux velux occultant` 720, `rideaux occultants velux` 480) = **6 120 retirés**. Ce sont des stores de fenêtre de toit à dimensions propriétaires, une autre référence produit et une marque déposée.

---

## 6. Vérification SERP — google.fr, `hl=fr&gl=fr`, 2026-08-28

Rappel de précaution, écrit comme l'exige la méthode :
- **Le carrousel Shopping sponsorisé n'est pas une preuve d'annonces Search texte.** Sur les sept têtes lues, la mention « Sponsorisé » apparaît 0 ou 1 fois selon la requête, sans que le bloc puisse être isolé de façon fiable en lecture texte. **Je ne peux pas confirmer la présence d'annonces Search texte**, et je ne l'affirme donc pas.
- **Pages 1 et 2 seulement.** Rien ne peut être conclu de la profondeur au-delà.
- Session Chrome connectée à un compte Google (voir §1.4).

### 6.1 `rideau occultant` — 33 100 · KD 32 · CPC 0,41 EUR

| Rang | Domaine | Nature |
|---|---|---|
| 1 | amazon.fr | marketplace |
| 2 | madura.com | marque / spécialiste rideaux FR |
| 3 | stores-et-rideaux.com | spécialiste DTC |
| 4 | stores-discount.com | spécialiste DTC |
| 5 | **ikea.com** | enseigne |
| 6 | **heytens.com** | enseigne déco |
| 7 | **leroymerlin.fr** | GSB |
| 8 | homemaison.com | spécialiste DTC |
| 9 | atmosphera.com | marque déco |
| 10 | eminza.com | pure player déco |
| 11-19 | eminza, laredoute.fr, centrakor.com, idealo.fr, bonsoirs.com, gifi.fr, action.com, kiabi.com, facebook.com | 7 enseignes/comparateurs + 1 spécialiste + 1 social |

- **Ce que Google sert** : des pages de collection marchandes de rideaux occultants. Aucune position éditoriale en page 1.
- **Intention** : **oui**, pleinement commerciale.
- **Occupation enseignes** : **4 sur 10** en page 1 (Amazon, IKEA, Heytens, Leroy Merlin) · **11 sur 19** sur les deux pages.
- **Spécialistes indépendants restants en page 1** : **6 sur 10** (Madura, stores-et-rideaux, stores-discount, homemaison, atmosphera, eminza).
- **Prix observés** : 5,99 € · 6,99 € · 9,99 € (Action, Gifi, Centrakor) — puis 41,58 · 46,99 · 53,99 · 59,90 · 79,00 · 89,00 · 130,00 · 139,00 · 149,00 · 169,00 · 179,00 €. **Palier spécialistes 79–179 €.**
- **Volume : RETENU** (101 530 nets).

### 6.2 `rideau thermique` — 33 100 · KD 29 · CPC 0,24 EUR

| Rang | Domaine | Nature |
|---|---|---|
| 1 | amazon.fr | marketplace |
| 2 | **moondreamwebstore.fr** | **spécialiste DTC pur, position 2** |
| 3 | heytens.com | enseigne |
| 4 | leroymerlin.fr | GSB |
| 5 | eminza.com | pure player |
| 6 | decor-discount.com | spécialiste DTC |
| 7 | stores-discount.com | spécialiste DTC |
| 8 | quelleenergie.fr | **éditorial** |
| 9 | blancheporte.fr | enseigne VPC |
| 10 | bouchara.com | enseigne textile |
| 11-20 | bouchara, reflexsol.fr, stores-et-rideaux.com, becquet.fr, centrakor.com, madura.com, facebook.com, idealo.fr, netatmo.com, cdiscount.com | mixte |

- **Ce que Google sert** : marchand à 9 positions sur 10, une position éditoriale (quelleenergie.fr, guide isolation).
- **Intention** : **oui**, commerciale, avec une frange pédagogique — c'est exactement le profil « produit explicable au particulier ».
- **Occupation enseignes** : **5 sur 10** (Amazon, Heytens, Leroy Merlin, Blancheporte, Bouchara) · **11 sur 20**.
- **Spécialistes indépendants restants** : **4 sur 10**, dont un en position 2.
- **Prix observés** : 5,99 € · 20 € · 41,58 · 53,99 · 89,00 · 109,00 · 139,00 · 149,00 · 169,00 · 179,00 · 400 €. **Palier spécialistes 89–179 €.**
- **Volume : RETENU** (104 900 nets).

### 6.3 `rideau phonique` — 4 400 · KD 15 · CPC 0,67 EUR

| Rang | Domaine | Nature |
|---|---|---|
| 1 | amazon.fr | marketplace |
| 2 | moondreamwebstore.fr | spécialiste DTC |
| 3 | nokomis.eu | spécialiste acoustique |
| 4 | leroymerlin.fr | GSB |
| 5 | pytaudio.com | spécialiste acoustique |
| 6 | heytens.com | enseigne |
| 7 | kurtens.com | spécialiste |
| 8 | perfectacoustic.fr | spécialiste |
| 9 | linder-shop.fr | spécialiste |
| 10 | nelinkia.com | spécialiste |
| 11-19 | cottonsilencepro.com, vb2go.fr, linvosges.com, sound-escape.co, castorama.fr, youtube.com, lamaisondesrideaux.com, cottonsilence.com, moondreamwebstore.fr | 1 GSB, 1 social, 7 spécialistes |

- **Ce que Google sert** : des marchands spécialisés de l'acoustique domestique. C'est **la page 1 la plus ouverte du dossier**.
- **Intention** : **oui**, commerciale et technique-particulier.
- **Occupation enseignes** : **3 sur 10** (Amazon, Leroy Merlin, Heytens) · **4 sur 19**.
- **Spécialistes indépendants restants** : **7 sur 10**, **13 sur 19**.
- **Prix observés** : 82,95 · 89,00 · 89,90 · 109,90 · 139,00 · 149,00 · 169,00 € pour les rideaux ; 9,90 · 21,99 · 26,95 · 29,99 € pour les accessoires acoustiques. **Palier 89–169 €.**
- **Volume : RETENU** (30 880 nets). KD 13-23 et une page 1 de spécialistes : c'est le contrôle n° 6 de la méthode dans le bon sens — porte difficile, pas porte fermée.

### 6.4 `rideau velours` — 1 900 · KD 17 · CPC 0,39 EUR

Page 1 : amazon.fr, mesrideaux.fr, roidurideau.com, madura.com, lemondesauvage.com, perfectacoustic.fr, laredoute.com, stores-discount.com, maison.denantes.fr.
Pages 11-19 : thesocialitefamily.com, heytens.com, lamaisonpigalle.com, stores-et-rideaux.com, ikea.com, cyrillus.fr, 4murs.com, bouchara.com, atmosphera.com.

- **Intention** : **oui**, commerciale.
- **Occupation enseignes** : **2 sur 9** en page 1 (Amazon, La Redoute) · **7 sur 18**.
- **Spécialistes restants en page 1** : **7 sur 9**.
- **Prix observés** : 16,50 · 17,50 · 22,99 · 24,99 · 29,99 · 33,00 · 33,59 · 35,00 · 64,38 · 80,00 · 109,00 €. **Socle 22–35 €, sous le plancher maison de 50 €.**
- **Volume : RETENU sous réserve de prix** (21 480 nets) — la demande existe et la page est prenable, mais l'étage de prix dominant est bas.

### 6.5 `rideau lin` — 5 400 · KD 19 · CPC 0,41 EUR

Page 1 : linenshed.fr, embrin.fr, stores-et-rideaux.com, leroymerlin.fr, ladraperiefrancaise.com, eminza.com, madura.com, bordeauxhome.fr, laredoute.fr.
Pages 11-19 : laredoute.fr, ikea.com, maisondete.fr, mesrideaux.fr, bouchara.com, amazon.fr, youtube.com, linder-shop.fr, homemaison.com.

- **Intention** : **oui**, commerciale, avec un positionnement matière assumé.
- **Occupation enseignes** : **2 sur 9** en page 1 (Leroy Merlin, La Redoute) · **6 sur 18**.
- **Spécialistes restants en page 1** : **7 sur 9**, dont deux marques de lin pur (linenshed.fr, embrin.fr).
- **Prix observés** : 12,50 · 17,00 · 21,90 · 28,98 · 29,90 · 32,23 · 35,80 · 38,00 · 39,90 · 43,99 € — puis **180,00 € et 265,00 €** (linenshed, embrin).
- **Bande bimodale, avec un vide entre ≈ 45 € et ≈ 180 €.** C'est exactement le piège de l'étape 9 : se placer « juste sous le haut » donnerait 175 €, en plein dans un prix que personne ne pratique. Le comparable est le socle 30–44 €.
- **Volume : RETENU** (37 520 nets), avec la réserve de bande bimodale écrite.

### 6.6 `voilage` — 8 100 · KD 27 · CPC 0,29 EUR

Page 1 : madura.com, bonsoirs.com, eminza.com, stores-discount.com, lamaisondesrideaux.com, veritable-macrame.com, heytens.com, decor-discount.com, castorama.fr.
Pages 11-19 : decor-discount, castorama, rideauxvoilages.com, homemaison.com, loberon.fr, atmosphera.com, ikea.com, stores-et-rideaux.com, bouchara.com.

- **Intention** : **oui**, commerciale. Aucune marketplace en page 1 — Amazon absent, ce qui est rare.
- **Occupation enseignes** : **2 sur 9** en page 1 (Heytens, Castorama) · **5 sur 18**.
- **Spécialistes restants en page 1** : **7 sur 9**.
- **Prix observés** : 3,90 · 3,99 · 4,99 · 9,99 · 10,82 · 12,99 · 16,70 · 22,90 · 49,99 €. **Médiane ≈ 12 €.**
- **Volume : RETENU dans le consolidé, avec réserve d'économie de panier** (99 460 nets) — ratio prix ÷ CPC ≈ 41, très en dessous de la cible 150-200.

### 6.7 `tringle a rideau` — 14 800 · KD 22 · CPC 0,16 EUR

Page 1 : amazon.fr, mesrideaux.fr, artapisserie.fr, leroymerlin.fr, tringle-a-rideaux.com, madura.com, castorama.fr, ikea.com, eminza.com, manomano.fr.
Pages 11-19 : entrepot-du-bricolage.fr, eminza.com, gifi.fr, homemaison.com, tringlearideau.fr, leroymerlin.fr, pinterest.com, jysk.fr, centrakor.com.

- **Intention** : **oui**, commerciale.
- **Occupation enseignes** : **5 sur 10** en page 1 (Amazon, Leroy Merlin, Castorama, IKEA, ManoMano) · **10 sur 19**. **C'est la famille la plus verrouillée du dossier.**
- **Spécialistes restants en page 1** : **5 sur 10**, dont deux EMD (`tringle-a-rideaux.com`, `tringlearideau.fr`).
- **Prix observés** : 1,00 · 1,49 · 8,90 · 8,99 · 9,35 · 11,99 · 12,82 · 18,00 · 19,97 · 29,90 · 37,00 · 44,99 €. **Médiane ≈ 12 €.**
- **Volume : RETENU dans le consolidé, avec double réserve** (227 790 nets) : ratio prix ÷ CPC ≈ 60 (sous 100), et occupation GSB de 5/10.

### 6.8 Récapitulatif du drapeau §4 — occupation par les enseignes

| Tête | Enseignes / marketplaces sur 10 (page 1) | Sur ~20 (pages 1-2) | **Spécialistes indépendants en page 1** |
|---|---|---|---|
| `rideau occultant` | **4 / 10** | 11 / 19 | **6** |
| `rideau thermique` | **5 / 10** | 11 / 20 | 4 |
| `rideau phonique` | **3 / 10** | 4 / 19 | **7** |
| `rideau velours` | **2 / 9** | 7 / 18 | **7** |
| `rideau lin` | **2 / 9** | 6 / 18 | **7** |
| `voilage` | **2 / 9** | 5 / 18 | **7** |
| `tringle a rideau` | **5 / 10** | 10 / 19 | 5 |

**Présence des quatre enseignes nommées au drapeau :**

| Enseigne | Têtes où elle est en page 1 | Têtes où elle est en page 2 |
|---|---|---|
| **Leroy Merlin** | occultant (7), thermique (4), phonique (4), lin (4), tringle (4) — **5 têtes sur 7** | tringle (16) |
| **IKEA** | occultant (5), tringle (8) — 2 têtes sur 7 | velours (15), lin (12), voilage (17) |
| **Castorama** | voilage (9), tringle (7) — 2 têtes sur 7 | phonique (15) |
| **Saint Maclou** | **aucune** | **aucune** |

**Ce que ces chiffres disent, sans arbitrage de ma part** : la pression enseigne est **réelle et concentrée sur trois têtes** — l'occultation, le thermique et surtout la tringle. Elle est **faible à absente sur le phonique, le velours, le lin et le voilage**, où les spécialistes indépendants tiennent 7 positions sur 9 ou 10. Saint Maclou n'apparaît nulle part sur les 7 têtes lues, sur 2 pages. **Il reste des spécialistes indépendants en page 1 sur les 7 têtes sans exception.** L'arbitrage du drapeau appartient à Hakim.

### 6.9 Google Trends — France, 5 ans, lecture qualitative (28/08/2026)

Comparaison `rideau occultant` / `rideau thermique` / `voilage` :

- **`voilage`** : socle continu et élevé toute l'année, sans mois mort. Léger creux de fin d'année.
- **`rideau occultant`** : courbe **plate et continue** sur les cinq ans, sans saison unique.
- **`rideau thermique`** : plat et bas la majeure partie de l'année, avec un **pic annuel très marqué en automne-hiver**, répété chaque année sur les cinq années observées.

**Forme de l'univers : socle continu ≥ 8 mois + une bosse saisonnière hivernale sur une famille.** C'est le profil UNIVERS recherché, pas un événementiel. Aucune variation chiffrée n'est avancée : l'outil n'affiche que des indices relatifs, et je ne les convertis pas en pourcentages.

---

## 7. Volume consolidé retenu

| Famille | Brut | **Net de marque** | Part du net | Prix observés | Statut de la famille |
|---|---|---|---|---|---|
| Accessoires (tringle, embrasse, anneau) | 271 440 | **227 790** | 35 % | 1–45 € | retenue, **réserve panier + GSB** |
| Thermique | 196 660 (chevauchants) | **104 900** | 16 % | 89–179 € | retenue |
| Occultation | 153 550 | **101 530** | 16 % | 79–179 € | retenue |
| Voilage | 133 600 | **99 460** | 15 % | 4–50 € | retenue, **réserve panier** |
| Lin | 58 490 | **37 520** | 6 % | 30–44 € et 180–265 € | retenue, **réserve bande bimodale** |
| Phonique | 37 810 | **30 880** | 5 % | 89–169 € | retenue |
| Forme (doubles rideaux) | 72 120 | **21 780** | 3 % | — | retenue |
| Velours | 24 740 | **21 480** | 3 % | 22–35 € | retenue, **réserve prix bas** |
| **TOTAL** | — | **645 340** | 100 % | — | **plancher** |

**Retirés du consolidé et comptés à part** : sur-mesure / confection **22 030** · tissu au mètre et doublure **5 200** · stores Velux **6 120** · rideau de douche **4 220** (1 750 dans Lin, 2 470 dans Anneau) · marques et enseignes **≈ 130 000** cumulés sur les huit familles.

**Non retenus comme familles, mesurés et écartés** :
- Parent `isolation phonique` : 118 390 lus, dont **1 780 seulement contiennent « rideau »** (1,5 %). Le parent est un marché de travaux (mur, plafond, placo, cloison, laine). **Non adressable par une boutique de rideaux.**
- Parent `isolation fenetre` : 38 310 lus, dont **0 contient « rideau »**. Marché du film isolant, du survitrage et du remplacement de menuiserie. **Non adressable.**
- Parent `rideau` : 726 300 lus, mais massivement contaminé — `azay le rideau` (commune et château) **75 400**, `frange rideau` (coiffure, « curtain bangs ») **74 700**, `stores et rideaux` (navigationnel vers storesetrideaux.com) **34 400**, `rideau de douche` **21 700**, `dressing avec rideau` **13 900**, `gustave rideau` (vérandas) **9 900**, `le rideau déchiré` (film) **6 600**. Soit **236 600 de contamination identifiée sur 726 300, un tiers du parent.** Le parent est un mot générique contaminé au sens du contrôle n° 3 ; il sert de repère de taille, jamais de volume adressable.
- Parents `rideau deco` (5 450) et `accessoire rideau` (6 750) : marginaux et largement informationnels. Ce ne sont pas les vrais parents du marché.

---

## 8. Bande de prix observée — synthèse (Google FR, 28/08/2026)

| Famille | Min | Socle dominant | Haut | Ratio prix ÷ CPC au socle |
|---|---|---|---|---|
| Occultation | 5,99 € | **79–179 €** | 179 € | ≈ 240 à 99 € (CPC 0,41) ✅ |
| Thermique | 5,99 € | **89–179 €** | 400 € | ≈ 410 à 99 € (CPC 0,24) ✅ |
| Phonique | 9,90 € | **89–169 €** | 169 € | ≈ 190 à 129 € (CPC 0,67) ✅ |
| Lin | 12,50 € | **30–44 €** puis vide, puis 180–265 € | 265 € | ≈ 95 à 39 € (CPC 0,41) ⚠️ |
| Velours | 16,50 € | **22–35 €** | 109 € | ≈ 75 à 29 € (CPC 0,39) ⚠️ |
| Voilage | 3,90 € | **10–17 €** | 49,99 € | ≈ 41 à 12 € (CPC 0,29) ❌ |
| Accessoires (tringle) | 1,00 € | **9–20 €** | 44,99 € | ≈ 60 à 12 € (CPC 0,16) ❌ |

**Trois enseignements de prix, à retenir pour la due diligence :**
1. Les trois familles d'**intention** (occultation, thermique, phonique) sont **dans la cible maison 50–400 €** avec des ratios prix ÷ CPC de 190 à 410. C'est là que l'économie tient.
2. Les familles de **matière** sont à la limite basse (velours 22–35 €), et le **lin est bimodal avec un vide entre 45 € et 180 €** — un vide de marché n'est pas une place à prendre (étape 9).
3. Le **voilage et les accessoires**, qui pèsent ensemble **51 % du consolidé net**, sont **sous le plancher de 50 €** et sous le ratio de 100. Ils apportent du trafic et du panier composé, pas de la marge unitaire.

---

## 9. Concurrents observés — spécialistes/DTC vs marketplaces/enseignes

### Spécialistes et DTC repérés (à cartographier en due diligence, pas ici)

| Domaine | Où il sort | Nature apparente |
|---|---|---|
| `moondreamwebstore.fr` | thermique (2), phonique (2 et 19) | **DTC français mono-marque, position 2 sur deux têtes techniques** — le concurrent le plus direct du modèle visé |
| `stores-et-rideaux.com` | occultant (3), thermique (13), velours (14), lin (3), voilage (18) | pure player généraliste rideaux + stores, présent sur 5 têtes |
| `stores-discount.com` | occultant (4), thermique (7), velours (8), voilage (4) | pure player discount |
| `decor-discount.com` | thermique (6), voilage (8 et 11) | pure player discount |
| `eminza.com` | occultant (10-11), thermique (5), lin (6), tringle (9 et 12) | pure player déco large |
| `homemaison.com` | occultant (8), lin (19), voilage (14), tringle (14) | pure player |
| `mesrideaux.fr` | velours (2), lin (14), tringle (2) | spécialiste, aussi cible du navigationnel `mes rideaux sur mesure` (590) |
| `lamaisondesrideaux.com` | phonique (17), voilage (5) | spécialiste |
| `rideauxvoilages.com` | voilage (13) | EMD spécialiste |
| `tringle-a-rideaux.com` / `tringlearideau.fr` | tringle (5) et (15) | EMD mono-famille |
| `roidurideau.com` | velours (3) | spécialiste |
| `linenshed.fr`, `embrin.fr`, `ladraperiefrancaise.com`, `maisondete.fr` | lin (1, 2, 5, 13) | marques lin haut de gamme, 180–265 € |
| `nokomis.eu`, `pytaudio.com`, `kurtens.com`, `perfectacoustic.fr`, `linder-shop.fr`, `nelinkia.com`, `cottonsilence.com`, `sound-escape.co`, `vb2go.fr` | phonique | **9 spécialistes acoustique** sur une seule tête |
| `bonsoirs.com`, `lemondesauvage.com`, `lamaisonpigalle.com`, `thesocialitefamily.com`, `loberon.fr`, `bordeauxhome.fr`, `artapisserie.fr`, `veritable-macrame.com`, `maison.denantes.fr`, `reflexsol.fr` | dispersés | marques déco et petits spécialistes |

### Marketplaces, enseignes et repères (jamais des cibles de comparaison prix)

`amazon.fr`, `cdiscount.com`, `manomano.fr`, `idealo.fr` (comparateur) · `ikea.com`, `leroymerlin.fr`, `castorama.fr`, `entrepot-du-bricolage.fr`, `gifi.fr`, `action.com`, `centrakor.com`, `jysk.fr` · `heytens.com`, `4murs.com`, `madura.com`, `atmosphera.com`, `bouchara.com`, `blancheporte.fr`, `becquet.fr`, `laredoute.fr`, `cyrillus.fr`, `linvosges.com`, `kiabi.com`.

**Madura et Atmosphera sont des marques à récit**, pas des comparables de prix : s'aligner sur elles, c'est s'aligner sur une notoriété qu'on n'a pas (règle étape 9).

---

## 10. Réserves — aucune retirée

1. **Sept familles sur huit reposent sur des planchers de lecture.** `rideau` (100e ligne à 2 900), `tringle rideau` (720), `voilage` (480), `rideau occultant` (390), `rideau thermique` (260), `double rideau` (260), `rideau lin` (140). Les nets publiés sont des **minorants** ; le marché réel est plus gros, pas plus petit. Aucune décision ne doit s'appuyer sur la précision de ces chiffres, seulement sur leur ordre de grandeur.
2. **Le consolidé est très au-dessus du seuil, ce qui doit rendre méfiant, pas confiant.** Trois vérifications ont été faites contre le gonflage : familles rendues disjointes par exclusions croisées documentées (§3.1), recoupement tringle × textile **mesuré à 0**, recoupement tringle × anneau/embrasse **mesuré à 720 et déduit**. Le double comptage résiduel n'a pas été vérifié ligne à ligne sur les 26 graines ; il est estimé sous 1 %, et c'est une **estimation**, pas une mesure.
3. **51 % du consolidé net est low-ticket** (voilage 99 460 + accessoires 227 790 = 327 250 sur 645 340), avec des médianes de prix à 12 € et des ratios prix ÷ CPC de 41 et 60, **sous le plancher maison de 100**. L'univers passe largement le seuil de demande ; **il n'a pas passé un test d'économie de panier**, qui n'est pas du ressort de cette phase mais qui doit être fait avant tout build.
4. **Drapeau §4 non arbitré, documenté et transmis.** Leroy Merlin est en page 1 de **5 têtes sur 7**. La tringle est occupée à 5/10 en page 1 et 10/19 sur deux pages. IKEA et Castorama sont présents mais dispersés. **Saint Maclou est absent des 7 têtes sur 2 pages.** Des spécialistes indépendants tiennent la page 1 des 7 têtes sans exception, majoritairement sur 5 d'entre elles. **Je ne tranche pas ce drapeau.**
5. **Saisonnalité de la famille Thermique.** Google Trends montre un pic hivernal net et récurrent chaque année sur cinq ans, avec un socle bas le reste de l'année. La famille pèse 16 % du consolidé ; elle ne sera pas régulière. L'univers dans son ensemble a un socle continu (occultation, voilage), donc il n'est pas événementiel — mais le calendrier d'acquisition devra en tenir compte. **Aucune amplitude chiffrée n'est avancée : l'outil n'en affiche pas.**
6. **Bande de prix bimodale sur le lin**, vide observé entre ≈ 45 € et ≈ 180 €. Se placer dans ce vide serait une erreur documentée (étape 9, cas `montre squelette`).
7. **Le velours est sous le plancher de 50 €** sur son socle observé (22–35 €), malgré une SERP très ouverte (7 spécialistes sur 9 en page 1).
8. **Annonces Search texte non confirmées.** Le carrousel Shopping et la mention « Sponsorisé » n'ont pas pu être isolés de façon fiable en lecture texte sur les 7 têtes. **Aucune affirmation n'est faite sur la pression publicitaire Search.** À vérifier séparément si la décision en dépend.
9. **SERP lues en session Google connectée** (le navigateur est celui de Hakim), contrairement à la consigne. `hl=fr&gl=fr` forcés, domaines relevés tous nationaux — mais une personnalisation résiduelle du classement ne peut être exclue.
10. **Pages 1 et 2 seulement.** Rien ne peut être conclu de la profondeur concurrentielle au-delà du rang 20.
11. **Le sur-mesure ne passe pas par la pose**, contrairement à l'hypothèse du brief : la grappe ne contient **aucune** requête de devis, pose, installation ou artisan. C'est de la confection à dimensions vendue en ligne. Le retrait de 22 030 reste justifié (non expédiable depuis un catalogue), mais **le motif n'est pas celui qui était attendu** — et cela signifie qu'un concurrent en ligne peut servir cette demande sans artisan.
12. **`moondreamwebstore.fr` est en position 2 sur `rideau thermique` ET sur `rideau phonique`.** C'est un DTC français qui occupe exactement la thèse « matière × intention » sur les deux familles techniques les plus rentables. Ce n'est pas un STOP en mode UNIVERS (§4 : un spécialiste en place est une preuve), mais c'est le concurrent à cartographier en premier.
13. **Aucune sonde prix Google Shopping structurée n'a été faite.** Les prix de ce rapport sont relevés **en SERP organique et dans les blocs produits visibles**, pas dans une sonde de 30-50 prix Shopping. La bande de prix est donc indicative et à confirmer.
14. **Aucun sourcing, aucun fournisseur, aucune fiche produit ouverte.** C'est la phase 4.

---

## 11. Verdict

**Seuil applicable, cité explicitement** : `PRODUCT-RESEARCH-CRITERIA.md` §1, mode **UNIVERS** — *« volume consolidé par familles qu'une même boutique servirait — plancher Kraken **30 000** boutique (confort **40 000**) »*.

**Consolidé net de marque mesuré : 645 340/mois** (plancher).
Même en écartant intégralement les deux familles low-ticket contestables (voilage et accessoires) : **318 090**.
Même en ne retenant que les trois familles d'intention, celles dont la bande de prix est dans la cible 50–400 € : **237 310**.
Même la famille la plus faible du dossier prise seule (doubles rideaux, 21 780) approche le seuil.

Sur le critère de la phase, il n'y a pas d'ambiguïté : **le consolidé UNIVERS dépasse le seuil de 30 000 d'un facteur 8 à 21 selon le périmètre retenu, et il dépasse très largement le cluster isolé `rideau occultant thermique/phonique` déjà qualifié au registre le 01/08 (~14-18 k).** Le passage du cluster à l'univers multiplie la demande adressable par **13 à 36**.

Ce n'est **pas un cas limite** : le consolidé n'est pas dans la fourchette 24 000–36 000, il en est à plus de vingt fois la borne haute.

# **PASS_PREQUALIFICATION**

Ce pass est une **conformité technique de volume**. Il autorise uniquement la due diligence (sourcing par famille, cartographie de concurrence). **Il ne constitue en aucun cas un `GO_FINAL`**, que je ne prononce pas et qui appartient à Hakim.

**Ce qui remonte à Hakim avec ce pass :**
- l'arbitrage du **drapeau §4** (Leroy Merlin en page 1 de 5 têtes sur 7, tringle occupée à 5/10) — documenté en §6.8, non tranché ;
- la décision sur les **deux familles low-ticket** qui font 51 % du consolidé (voilage, accessoires) : familles de trafic à garder pour le catalogue, ou périmètre à resserrer sur les trois familles d'intention à 89–179 € ;
- le rappel `PRODUCT-RESEARCH-CRITERIA.md` §0.6 : **aucun `GO_FINAL` sur un dossier UNIVERS** tant que la sourçabilité des familles pesant ≥ 70 % du consolidé (ici Accessoires, Thermique, Occultation, Voilage = 82 %) n'est pas documentée à ≥ 2 fournisseurs plausibles chacune.

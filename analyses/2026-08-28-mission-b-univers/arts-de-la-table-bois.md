# Mission B — UNIVERS — Arts de la table bois

**Date : 2026-08-28** · Candidat #23 de la shortlist 30×30 · Mode **UNIVERS**
Seuil applicable : **volume consolidé par familles ≥ 30 000/mois, confort 40 000** (`PRODUCT-RESEARCH-CRITERIA.md` §1). Le seuil PRODUIT PUR de 10 000 par cluster **ne s'applique pas ici**.
Méthode : `METHODE-ANALYSE-MARCHE.md` étapes 2 à 5 et 9 · skill `recherche-mots-cles` Mission B.

---

## 1. Entrée et méthode

### Entrée

- Rapport amont : `boutique-pipeline/analyses/2026-08-28-mission-b-univers-preparation.md` §5.4 (graines par famille) et §4 (sélection, somme indicative 48 K, sonde prix 72,36 € du 22/08).
- Preuve boutique du 22/08 : `bcd-design.com` (SARL Bois Carbone Design) — 47 ads, 921 jours d'ancienneté, reach 1,875 M. Non revérifiée aujourd'hui (hors périmètre Mission B).

### Outil et contrôle témoin

SEMrush **base France** (`db=fr`), Keyword Magic Tool, **expression exacte** (`&mt=phrase`), 100 lignes, 0 crédit, `currency=eur`.
Sélecteur de base lu à l'écran à chaque passe : **« France »**. Sélecteur de devise : **« EUR »**. **Tous les CPC de ce rapport sont en EUR**, pas en dollars.

| Contrôle témoin | Lecture | Attendu | Résultat |
|---|---|---|---|
| **AVANT** — `tufting` (`db=fr&mt=phrase`) | 28/08/2026 | 8 100 | **8 100** · KD 25 · CPC 0,68 EUR — conforme |
| **APRÈS** — `tufting` (`db=fr&mt=phrase`) | 28/08/2026, après la dernière mesure | 8 100 | **8 100** · KD 25 · CPC 0,68 EUR — conforme |

Le quota n'a pas été épuisé pendant la passe. Aucun zéro silencieux. Toutes les lectures ci-dessous sont datées du **28/08/2026**.

### Graines contrôlées

19 requêtes, trois niveaux de généralité **séparés, jamais additionnés**, doubles orthographes systématiques :

`plateau` (parent) · `plateau bois` · `plateau de service` · `plateau petit dejeuner` · `plateau petit déjeuner` · `plateau apero` · `plateau charcuterie` · `plateau ardoise` · `planche` (parent) · `planche apero` · `planche apéro` · `planche a fromage` · `planche à fromage` · `planche charcuterie` · `planche a decouper` · `planche à découper` · `art de la table` · `billot` · `tufting` (témoin ×2).

### Les cinq contrôles, appliqués à chaque passe

1. **Deux orthographes** — confirmé décisif : `planche apero` = 9 900 et `planche apéro` = 2 900 sont **deux corpus distincts** (×3,4 d'écart) ; `planche a fromage` = 140 contre `planche à fromage` = 590 (×4,2) ; `plateau petit dejeuner` = 590 contre `plateau petit déjeuner` = 880. La règle mémoire « variantes sans accent dans le KMT » est confirmée sur ce dossier.
2. **Plusieurs niveaux de généralité** — les deux parents (`plateau`, `planche`) ont été mesurés et se révèlent **inutilisables** (§3.1 et §3.2).
3. **`n/a` ≠ `0`** — l'interface n'a affiché **aucun `n/a`** sur ce dossier. Elle affiche en revanche des **`0` littéraux** en queue de grappe (`planche a fromage`, `planche à fromage`, `plateau petit dejeuner`). Ces `0` sont lus comme **« sous le seuil de restitution »**, pas comme une absence de recherche, et ne sont jamais additionnés.
4. **Mot-clé témoin** — voir tableau ci-dessus, avant et après.
5. **Plancher de lecture** — signalé famille par famille. Cinq grappes sur dix-neuf sont des **planchers, pas des totaux**.

### Limites de calcul, à lire avant les chiffres

- **Les totaux de grappe sont des estimations reconstituées ligne à ligne**, jamais le « Volume total » affiché en tête de requête par SEMrush (celui-ci inclut tout le bruit ; sur le témoin `tufting` il annonce 78 920 quand la tête réelle vaut 8 100).
- Sur les grappes longues, les 100 lignes ont été lues intégralement pour `plateau de service`, `plateau bois`, `plateau ardoise`, `planche apero`. Sur les autres, **les 25 à 45 premières lignes ont été lues nominativement** et la queue estimée à partir de la dernière valeur affichée et du nombre de lignes restantes. Ces queues sont **des estimations**, signalées comme telles.
- **Les pourcentages de retrait sont des estimations faites à la composition de la page 1**, pas de nouvelles mesures.
- `set de service bois`, `couvert a salade bois`, `plateau marbre`, `plateau tournant`, `plateau repas`, `saladier bois`, `corbeille a pain` : **non mesurés faute de temps de session**. Voir §8.
- SERP lues dans le navigateur de Hakim, **session Google potentiellement connectée** — la personnalisation des résultats ne peut pas être exclue. Signalé comme limite.
- **Aucune annonce Search texte n'a pu être isolée** sur les quatre SERP. Ce qui est visible et labellisé, ce sont des **carrousels de produits** et, sur `dessous de plat`, un bloc explicitement marqué **« Produits Sponsorisés … Par Google »** = annonces Shopping. **Je ne confonds pas les deux et je ne conclus rien sur la pression publicitaire Search.**

---

## 2. Mesure par graine

Toutes lectures du 28/08/2026, `db=fr`, `mt=phrase`, CPC en **EUR**.

| Graine | Niveau | Volume tête | KD | CPC (EUR) | Intention SEMrush | 100ᵉ ligne | Plancher ? |
|---|---|---|---|---|---|---|---|
| `plateau` | parent | `plateau de beille` 18 100 / `plateau` 14 800 | 29 | 0,63 | N | 1 900 | **Oui** |
| `plateau bois` | famille | 5 400 | 14 | 0,35 | I | 210 | Non |
| `plateau de service` | famille | 2 900 | 21 | 0,34 | I | 20 | Non |
| `plateau petit dejeuner` | produit | 590 (`plateau petit dejeune`) | 22 | 0,29 | **C** | 0 | Non |
| `plateau petit déjeuner` | produit | 880 | 22 | 0,29 | I | 0 | Non |
| `plateau apero` | produit | 3 600 | 15 | 0,25 | I | 20 | Non |
| `plateau charcuterie` | produit | 5 400 | 15 | 0,32 | I | 90 | **Oui** |
| `plateau ardoise` | matière | 480 | 11 | 0,43 | I | 0 | Non |
| `planche` | parent | `plancha electrique` 40 500 | 25 | 0,10 | I | 2 400 | **Oui** |
| `planche apero` | famille | **9 900** | 17 | 0,29 | I | 50 | Non |
| `planche apéro` | famille | 2 900 | 12 | 0,29 | I | 40 | Non |
| `planche a fromage` | produit | 140 | 22 | 0,34 | I | 0 | Non |
| `planche à fromage` | produit | 590 | 11 | 0,38 | I | 0 | Non (n=67) |
| `planche charcuterie` | produit | 2 400 | 16 | 0,44 | I | 30 | Non |
| `planche a decouper` | famille voisine | **14 800** | 17 | 0,27 | I | 90 | **Oui** |
| `planche à découper` | famille voisine | `planche à découper bois` 6 600 | 21 | 0,23 | I | 170 | **Oui** |
| `art de la table` | parent catégorie | 4 400 | 33 | 0,33 | **C** | 50 | Non |
| `billot` | dossier clos | 4 400 | 14 | 0,29 | I | 140 | **Oui** |

**Lecture d'ensemble des CPC : de 0,10 à 0,68 EUR, médiane ≈ 0,30 EUR.** Aucun CPC de ce dossier ne dépasse 0,45 EUR hors témoin. C'est cohérent avec un marché à faible valeur unitaire.

**Lecture d'ensemble des intentions : 16 graines sur 18 sont classées `I` (informationnel) par SEMrush.** Seules `plateau petit dejeuner` et `art de la table` sortent en `C`. C'est le signal central de ce dossier, et la SERP le confirme (§5).

---

## 3. Détail par famille — mots-clés retenus, exclus, niveaux testés

### 3.1 Niveau parent `plateau` — **testé, retiré intégralement**

Lignes lues, 100/100, 100ᵉ ligne à 1 900 → **plancher**.

Le parent est contaminé au point d'être inutilisable :

| Contamination | Exemples mesurés |
|---|---|
| **Géographique** (le gros du volume) | `plateau de beille` 18 100 · `plateau de valensole` 8 100 · `plateau des glières` 8 100 · `plateau de millevaches` 6 600 · `plateau de gergovie` 3 600 · `plateau d'albion` 2 900 · `plateau d'emparis` 2 900 · `plateau de saclay` 2 900 · `plateau du coscione` 2 900 · `plateau des petites roches` 2 900 · `plateau de solaison` 2 900 · `plateau du retord` 2 400 · `plateau d'assy` 2 400 + webcams et météo associées (≈ 20 000 supplémentaires) |
| **Médicale** | `plateau tibial` 3 600 · `plateau fractures` 4 400 · `broken tibia plateau` 4 400 · `tibial plateau break` 4 400 · `fractured tibial plateau` 3 600 |
| **Transport / poids lourd** | `location camion plateau` 5 400 · `camion plateau` 4 400 · `remorque plateau` 4 400 · `location plateau voiture` 4 400 · `plateau moto` 5 400 |
| **Jeu de société** | `plateau monopoly` 3 600 · `risk jeu plateau` 3 600 · `jeu de plateau` 2 900 · `plateau echec` 2 900 |
| **Anglais / hors France** | `anatolia plateau` 6 600 · `arabian plateau` 5 400 |
| **Plateau de table (meuble)** | `table basse plateau relevable` 3 600 · `plateau de table` 2 900 |

**Décision : le niveau parent `plateau` n'est pas un cluster adressable. Retiré en totalité.** Il ne sert qu'à révéler le vocabulaire, ce qu'il a fait.

### 3.2 Niveau parent `planche` — **testé, retiré intégralement**

100/100 lignes, 100ᵉ ligne à 2 400 → **plancher**.

| Contamination | Exemples mesurés |
|---|---|
| **Plancha (appareil de cuisson)** — la plus grosse | `plancha electrique` 40 500 · `plancha` 33 100 · `plancha gaz` 27 100 · `brasero plancha` 9 900 · `plancha tefal` 6 600 · `plancha forge adour` 5 400 · `plancha krampouz` 5 400 · `barbecue plancha` 4 400 · `plancha campingaz` 4 400 · `chariot plancha` 3 600 · `desserte plancha` 3 600 · `plancha weber` 3 600 (≈ 150 000 à elles seules) |
| **Bois de construction / GSB** | `planche bois` 22 200 · `planche de coffrage` 18 100 · `planche de bois` 12 100 · `planche bois leroy merlin` 5 400 · `planche osb` 5 400 · `planche coffrage` 4 400 · `planche de rive` 4 400 |
| **Plancher (bâtiment) et médical** | `plancher bois` 6 600 · `plancher chauffant` 4 400 · `plancher osb` 3 600 · `surface de plancher` 3 600 · `plancher pelvien` 3 600 |
| **Sport** | `planche de surf` 9 900 · `planche a voile` 6 600 |
| **Autres** | `planchez` 27 100 · `planche à repasser` 4 400 · `kapla planches bois` 4 400 · `du pain sur la planche` 3 600 · restaurants (`le 17.45 paris … planches à composer` 3 600 ×3, `les planches paris` 4 400) |

**Décision : le niveau parent `planche` n'est pas un cluster adressable. Retiré en totalité.**

### 3.3 Famille **Plateaux de service**

**Niveaux testés :** `plateau` (parent, retiré) → `plateau bois` (famille matière) → `plateau de service` (famille usage) → `plateau petit déjeuner`, `plateau apéro` (produits).
**Niveau retenu : `plateau de service` + `plateau petit déjeuner` (deux orthographes).**

#### `plateau de service` — 100/100 lignes lues, 100ᵉ ligne à 20, **couverture complète**

**Retenus** (extrait des lignes principales) : `plateau de service` 2 900 · `plateau de services` 1 300 · `grand plateau de service` 720 · `plateau de service en bois` 480 · `plateau de service bois` 390 · `plateau de service grand format` 390 · `plateau de service rectangulaire` 390 · `plateau de service rond` 260 · `plateau de service original` 210 · `plateaux de service` 210 · `grand plateau de service 60x40` 170 · `grand plateau de service xxl` 170 · `grands plateaux de service` 170 · `plateau rond de service` 170 · `plateau de service design` 140 · `plateau de service vintage` 140 · `plateau de service antidérapant` 110 · `plateaux de service design` 110 · `plateau de service avec poignée` 90 · `plateau de service bois massif` 90 · `plateau de service rectangulaire en bois` 90 · `plateaux de service en bois` 90 · `beau/joli plateau de service` 40+40 · `plateau de service en bois design` 40 · `petit plateau de service` 30 · `plateau de service bambou` 30 · queue à 20–30.

**Brut reconstitué ligne à ligne : ≈ 12 410.**

**Exclus, avec motif :**

| Exclu | Volume | Motif |
|---|---|---|
| `plateau de service centrakor` 170 · `… maison du monde` 170 · `… ikea` 140 · `… gifi` 110 · `… 60x40 ikea` 110 · `… action` 90 · `… en bois ikea` 30 · `alinea …` 20 · `amazon …` 20 · `cdiscount …` 20 · `ikea plateau(x) de service` 40 · `grand … ikea` 20 | **≈ 940** | Marque / enseigne — inutilisable en flux Merchant Center |
| `plateau de service restauration` 140 · `… professionnel` 90 · `nom grand plateau de service restauration` 90 · `… restaurant` 40 · `grand … restauration` 20+20 · `grand plateau rond de service restauration` 20 · `grand … professionnel` 20 | **≈ 440** | Persona professionnel CHR (§3 des critères : signal d'exclusion) |
| `plateau de service jetable` 50 · `… plastique` 90 · `plateaux de service en plastique` 90 · `… en plastique` 70 · `grand … en plastique` 20 · `grand … melamine` 20 | **≈ 340** | Consommable / vaisselle jetable de réception, hors univers bois |
| `chariot de service inox 3 plateaux` 40 · `… 2 plateaux` 30 · `chariot de service 2/3 plateaux` 40 | **≈ 110** | Autre produit (chariot), autre page |
| `nom grand plateau de service` 20 · `nom plateau de service` 20 · `gros plateau de service nom` 20 · `grand plateau de service nom` 20 · `nom grand plateau de service restauration` (compté ci-dessus) · `fabriquer un plateau de service en bois` 20 | **≈ 100** | Informationnel lexical (« comment s'appelle un grand plateau ») et DIY |
| `location plateau de service` 20 | 20 | Prestation |

**Net de marque : ≈ 11 470.** **Adressable après retraits d'intention : ≈ 10 600.**

#### `plateau bois` — 100/100 lignes lues, 100ᵉ ligne à 210. **Le grand retrait du dossier.**

Tête : 5 400, KD 14, CPC 0,35 EUR. Mais la grappe **n'est pas une grappe de plateau de service** : elle est faite de **plateaux de table et de bureau** (piège n° 1 du catalogue, retournement pièce contre produit fini, lu sur l'ordre des mots et les modificateurs).

Lignes retirées, mesurées une par une : `plateau bois pour table` 2 400 · `plateau table bois` 2 400 · `plateau bois massif` 1 900 · `plateau pour table en bois` 1 900 · `plateaux bois table` 1 900 · `bois pour plateau de table` 1 600 · `plateau de table en bois` 1 600 · `plateau en bois table` 1 600 · `plateau bois table` 1 300 · `plateau en bois massif` 1 300 · `table plateau bois` 1 300 · `plateau de bois pour table` 1 000 · `plateau de table bois` 1 000 · `plateau table en bois` 1 000 · `plateau bois leroy merlin` 880 · `plateau massif bois` 880 · `leroy merlin plateau bois` 720 · `plateau bois brut` 720 · `table plateau en bois` 720 · `bois massif plateau` 590 · `plateau bois bureau` 590 · `plateau bureau bois` 590 · `bureau plateau bois` 480 · `ikea plateau bois` 480 · `plateau bois ikea` 480 · `plateau en bois ikea` 480 · `plateau ikea bois` 480 · `plateau bois sur mesure` 480 · `plateau de table bois massif` 480 · `plateau en bois pour table` 480 · `plateau en bois sur mesure` 480 · `plateaux de table bois` 480 · `leroy merlin plateau bois massif brut pour table` 390 · `plateau bois massif pour table` 390 · `plateau bois pour table 200x100` 390 · `plateau de bois massif pour table` 390 · `plateau table bois massif` 390 · `plateaux bois brut` 390 · `plateaux bois pour table` 390 · `plateaux en bois pour table` 390 · `table plateau bois massif` 390 · `plateau bureau en bois` 320 · `plateau de table en bois massif` 320 · `plateau en bois massif pour table` 320 · `plateau en bois bureau` 390 · `plateau en bois pour bureau` 390 · `plateau pour table bois` 320 · `plateau pour table bois massif` 320 · `plateaux bois massif` 320 · plus la queue Castorama / Leroy Merlin / table basse / extérieur.

**Volume retiré au titre du plateau de table et de bureau : ≈ 33 000 à 35 000** (estimation, reconstituée ligne à ligne sur les lignes ≥ 210).

Ce qui reste de `plateau bois` et qui appartient réellement à l'univers : `petit plateau en bois` 320 · `petit plateau bois` 260 · `plateau fromage bois` 260 · `grand plateau bois` 210 · les quatre variantes de `plateau tournant` en bois (390+390+390+320 = 1 490) · `plateau de service en bois` 480 et `plateau de service bois` 390 (**déjà comptés** dans `plateau de service`, non recomptés). `plateau rond en bois` 1 900 / `plateaux ronds bois` 1 300 / `plateau bois rond` 1 600 / `plateau en bois rond` 1 600 / `plateau rond bois` 1 300 sont **ambigus** (plateau de table ronde ou plateau de service rond) : **non attribués**, déclarés en fourchette (§8).

`plateau bois action` 390 et `plateau en bois action` 260 : marque, retirés — et **signal de prix** (§6).

#### `plateau petit déjeuner` — deux orthographes

- Sans accent, 100/100 lignes, 100ᵉ à 0 : `plateau petit dejeune` 590 · `plateau petit dejeuner lit` 590 · `plateau petit dejeuner` 320 · `plateau petit dejeuner au lit` 260 · `plateaux petit dejeuner lit` 210 · `plateau pour petit dejeuner` 90 · `plateau de petit dejeuner` 70 · queue à 20–30. **Brut ≈ 2 900.**
- Avec accent, 100/100 lignes, 100ᵉ à 0 : `plateau petit déjeuner` 880 · `… au lit` 590 · `plateau pour petit déjeuner` 390 · `plateau pour petit déjeuner au lit` 390 · `plateau lit petit déjeuner` 320 · `plateau de petit déjeuner` 70 · `plateau petit-déjeuner` 70 · queue à 20–50. **Brut ≈ 3 300.**

**Total deux orthographes ≈ 6 200 brut.** Exclus : `maison du monde` 30+30 · `gifi` 50+30+20 · `ikea` 40+20+20 · `action` 90+20 · `centrakor` 20+20 · `amazon` 20+20 · `carrefour` 20 · `habitat` 20 · `livraison plateau petit dejeuner` 30 (prestation) · `dessin / image / photo / idée plateau petit déjeuner` ≈ 80 (informationnel). **≈ 580 retirés → net ≈ 5 620.** Retenu prudemment à **5 400**.

**Note :** c'est la seule graine du dossier classée **`C` (commerciale)** par SEMrush côté produit. C'est aussi la plus petite.

#### `plateau apero` — 100/100 lignes, 100ᵉ à 20

Tête 3 600 + `plateau pour apero` 3 600. **Grappe quasi entièrement alimentaire et éditoriale** : `plateau apero dinatoire` 1 300 · `idee plateau apero dinatoire` 590 · `plateau legume(s) apero` 590+590+320+260+210+90 · `idee plateau apero` 480 · `plateau charcuterie apero` 480 · `plateau crudités apero` 390 · `presentation plateau legumes apero` 260 · `plateau apero traiteur` 90 · `plateau apero leclerc` 260.

**Retenu de cette grappe : uniquement le vocabulaire objet** — `plateau apero tournant` 260 · `plateau tournant apero` 260 · `plateau apero bois` 90 · `plateau bois apero` 70 = **680**. Le reste (**≈ 12 000**) est retiré : recette, décoration de buffet, commande traiteur, enseigne.
Exclus marque : `plateau apero maison du monde` 320 + `maison du monde plateau apero` 210 = 530.

#### `plateau charcuterie` — **retiré en totalité** (voir §5.2)

100/100 lignes, 100ᵉ à 90 → **plancher**. Grappe brut ≈ **25 000 à 30 000** (estimation) : `plateau charcuterie` 5 400 · `plateau de charcuterie` 4 400 · `plateau charcuterie fromage` 2 900 · `plateau fromage charcuterie` 2 400 · `charcuterie plateau` 1 900 · `plateaux de charcuterie` 1 900 · `buffet présentation plateau charcuterie` 1 600 · `plateau de charcuterie et fromage` 880 · `idee plateau charcuterie` 720 · `plateau charcuterie dinatoire` 720 · `plateau charcuterie raclette` 720 · `présentation plateau charcuterie` 720 · `tarif plateau charcuterie leclerc` 590 · `plateau charcuterie 20 personnes` 480 · `plateau charcuterie leclerc` 480 · `decor/deco/decoration/decorer plateau charcuterie` 390+320+320+320.

**La SERP tranche : c'est un marché de traiteur et de recette, pas de planche en bois. Retrait intégral. Motif détaillé en §5.2.**

Le même raisonnement retire, dans le parent `plateau`, `plateau de fromage` 6 600 · `plateau de fruit(s) de mer` 6 600 + 6 600 · `plateau fruit de mer` 2 900 · `plateaux de fromages` 3 600 · `plateau fromage` 5 400 · `plateau de fruit` 2 400 · `fromage plateau` 1 900. **Volume alimentaire retiré au total : ≈ 36 000 à 40 000.**

### 3.4 Famille **Planches de service / présentation**

**Niveaux testés :** `planche` (parent, retiré) → `planche apero` / `planche apéro` (famille) → `planche a/à fromage`, `planche charcuterie` (produits) → et, séparément, la famille voisine `planche a/à decouper` (§4).
**Niveau retenu : `planche apero` + `planche apéro`, part commerciale seulement.**

#### `planche apero` (sans accent) — 100/100 lignes, 100ᵉ à 50. **Brut reconstitué ≈ 36 000.**

**Retenus — vocabulaire d'objet :** `planche apero originale` 1 300 (partiel) · `planche apero personnalisé` 1 000 · `planche apero bois` 720 · `grand planche apero` 480 · `grande planche apero` 480 · `planche en bois pour apero` 480 · `planches apero` 320 · `planches apero bois` 320 · `planche bois apero` 260 · `planche a apero` 210 · `planche apero personnalisable` 210 · `planche en bois apero` 210 · `planche en bois apero xxl` 170 · `planche pour apero` 170 · `planche apero en bois` 140 · `planche apero xxl` 140 · `grande planche apero bois` 90 · `grande planche en bois apero` 90 · `planche apero ronde` 90 · `planche apero pas cher` 70. **Sous-total objet ≈ 6 950.**

**Exclus, avec motif :**

| Exclu | Volume estimé | Motif |
|---|---|---|
| `planche apero dinatoire` 2 400 · `idee planche apero` 1 900 · `planches apero dinatoire` 720 · `presentation planche apero` 720 · `planche apero idee` 590 · `planche apero simple` 480 · `idee planche apero originale` 390 · `idees planche apero` 320 · `faire une planche apero` 260 · `idee de planche apero` 260 · `recette planche apero` 260 · `planche apero facile` 260 · `planche apero recette` 210 · `idees de planche apero` 140 · `modele` 140 · `dessin` 140 · `que mettre sur` 140 · `exemple` 110 · `photo` 110 · `a faire soi meme` 110 · `quoi mettre sur` 110 · `planches apero idees` 110 · queue idées/recettes | **≈ 10 500** | **Informationnel pur** : recette, idée, présentation. Une collection produit ne prend pas ces pages. |
| `planche apero pour 10 personnes` 320 · `planche apero legumes` 210 · `planche apero charcuterie` 210 + `charcuterie fromage` 210 + `fromage charcuterie` 170 + `de charcuterie` 140 + `fromage` 110 + `charcuterie et fromage` 110 · `fromage pour planche apero` 90 · `crudités` 90 · `poisson` 90 · `vegetarienne` 70 · `italie/italienne/italien` 140+140+90 · `tapas` 70 · `de la mer` 170 | **≈ 2 400** | **Composition alimentaire** — c'est la garniture, pas le support |
| `planche apero noel` 590 · `halloween` 210 · `pere noel` 140 · `sapin de noel` 110 · `ete` 110 · `pâques`/`automne`/`hiver` (corpus accentué) | **≈ 1 200** | Saisonnier éditorial — utilisable en contenu, pas en collection |
| `planche apero bar` 1 300 · `bar planche apero` 170 · `bar planches apero` 170 · `bar avec planche apero` 110 · `prix planche apero bar` 70 · `planche apero lille` 110 · `planche apero traiteur` 70 · `planche apero carton` 90 | **≈ 2 090** | **Restauration / bar à planches / jetable pro** — persona professionnel |
| `apero plancha` 260 · `plancha apero` 170 · `apero planche` 140 · `apero plancha facile` 90 · `apero a la plancha` 50 · `apero dinatoire plancha` 50 · `apero plancha idee` 50 · `apero plancha recette` 50 · `apero plancha recettes` 50 | **≈ 910** | **Plancha** — appareil de cuisson, produit totalement différent |
| `planche apero action` 260 · `planche apero bois xxl action` 260 · `planche apero gifi` 260 · `planche apero bois gifi` 110 · `gifi planche apero` 110 · `planche apero super u` 70 | **≈ 1 070** | Marque / enseigne |

**Tête `planche apero` 9 900 : non attribuée en bloc.** Sa SERP (§5.1) sert simultanément un spécialiste DTC en position 1 et cinq à six positions éditoriales/alimentaires. **Attribution retenue : 30 à 40 % commercial, soit 3 000 à 4 000.** Écrit en fourchette, conformément au contrôle « le mot ambigu qu'on n'a pas tranché se déclare, il ne s'arrondit pas ».

**Adressable `planche apero` : ≈ 10 000 à 11 000.**

#### `planche apéro` (avec accent) — 100/100 lignes, 100ᵉ à 40. **Brut ≈ 18 000.**

Même structure. Objet : `planche apéro personnalisée` 590 · `planche apéro xxl` 590 · `planche apéro personnalisé` 390 · `grande planche apéro` 390 · `planche apéro bois xxl action` 390 (marque, exclu) · `planche apéro bois` 320 · `planche en bois apéro xxl` 320 · `planches apéro` 320 · `planche apéro bois xxl gifi` 210 (marque, exclu) · `planche apéro bois gifi` 170 (marque, exclu) · `planche apéro bois xxl` 110 · `planche apéro originale` 1 300 (partiel).
**Sous-total objet ≈ 3 500** + 30 à 40 % de la tête 2 900 ≈ 900 à 1 200. **Adressable ≈ 4 500.**
Exclus informationnels majeurs : `idée planche apéro pas cher` 2 400 · `idée planche apéro dînatoire` 880 · `idée planche apéro` 720 · `planche apéro dînatoire` 720+590 · `planche apéro pour 10 personnes` 1 000 · `sans gluten` 320 · `végétarienne` 320 · `healthy` 140 · `femme enceinte` 110 · `présentation` 260 · `faire une` 260 · `recette` 140 · `que mettre sur` 140 → **≈ 8 000**. Enseignes : `leclerc` 110 · `gifi` 110+170+210.

#### `planche à fromage` — deux orthographes, **famille marginale**

- Sans accent : tête **140**, grappe ≈ 400 (100ᵉ ligne à 0 ; nombreux `0` affichés). Contaminée par « fromage à la plancha » (recette) et par le restaurant « La Planche à Fromage » de Couilly-Pont-aux-Dames.
- Avec accent : tête **590**, n=67, grappe ≈ 900. Mêmes contaminations + `planche à découper fromage` (autre famille).

**Adressable combiné : ≈ 800.** Le mot de la maison du brief (`planche a fromage`) est **le plus faible de tout le dossier**. Exclus : `boska` 10 (marque), `grossistes planches à fromage` (B2B), bars à vin locaux, recettes plancha.

#### `planche charcuterie` — 100/100 lignes, 100ᵉ à 30. **Brut ≈ 14 000.**

Tête 2 400 · `planche charcuterie fromage` 2 400 · `planche de charcuterie` 1 900 · `planches de charcuterie` 1 300 · `planche à charcuterie` 720 · `planche charcuterie apero` 720. Mais les six lignes suivantes sont **`presentation` / `présentation`** (720+720+480+480+210) et le reste est composition alimentaire.
**Recoupement mesuré avec `planche apero` : `planche charcuterie apero` 720, `planche apero charcuterie` 210, `planche apero charcuterie fromage` 210, `planche apero fromage charcuterie` 170, `planche apéro charcuterie` 260, `planche apéro charcuterie fromage` 320 — soit ≈ 1 890 déjà comptés dans les corpus apéro. Non recomptés.**
**Résidu produit non déjà compté, retenu prudemment : 1 000.** Le reste (≈ 11 000) est retiré comme présentation/composition.

### 3.5 Famille **Dessous de plat**

**Niveaux testés :** `dessous de plat` (famille) → `dessous de plat bois` (matière, dans la même grappe). Le parent proposé au brief, `protection table`, n'a pas été mesuré (§8) ; la grappe `dessous de plat` étant couverte jusqu'à la 100ᵉ ligne à 30, elle se suffit.

100/100 lignes, 100ᵉ à 30 → **couverture complète**. Tête 5 400, KD 19, **CPC 0,20 EUR — le plus bas du dossier hors parent**.

**Retenus :** `dessous de plat` 5 400 · `dessous de plat bois` 720 · `dessous de plat en bois` 720 · `dessous de plats` 590 · `dessous de plat ceramique` 390 · `dessous de plat design` 320 · `dessous de plat verre` 320 · `dessous de plat en ceramique` 260 · `en céramique` 260 · `en verre` 260 · `liege` 260 · `mosaique` 260 · `personnalisé` 260 · `en fonte` 210 · `en liege` 210 · `en silicone` 210 · `fonte` 210 · `personnalise` 210 · `silicone` 210 · `dessous de plats design` 210 · `dessous de plats en bois` 210 · `en mosaique` 170 · `original` 170 · `dessous de plats en liège` 170 · `en verre` 170 · `en marbre` 140 · `extensible` 140 · `marbre` 140 · `céramique` 110 · `en liège` 110 · `noir` 110 · `originaux` 110 + queue à 30–90.

**Brut reconstitué : ≈ 17 600** (les 60 dernières lignes sont estimées à ≈ 55 de moyenne — **estimation signalée**).

**Exclus :**

| Exclu | Volume | Motif |
|---|---|---|
| `dessous de plat ikea` 390 + `ikea dessous de plat` 390 · `fermob` 140 · `action` 110 | **≈ 1 030** | Marque / enseigne |
| `dessous de plat lu` 170 · `dessous de plat petit beurre` 110 | **≈ 280** | Marque cachée dans un mot générique (piège n° 4) : le dessous-de-plat en forme de biscuit LU Petit Beurre. Ne se voit pas dans la tête. |
| `dessous de plat en anglais` 140 · `dessous de plat anglais` 110 | **≈ 250** | Informationnel lexical (traduction). La SERP confirme : Wikipédia en page 1 et deux questions « Que signifie le mot sous-plat ? / Quel est le pluriel ? » |

**Net de marque : ≈ 16 570.** **Adressable retenu : ≈ 16 300.**

### 3.6 Famille **Service assorti** et niveau catégorie `art de la table`

`art de la table` — 100/100 lignes, 100ᵉ à 50. Tête **4 400**, KD 33, **CPC 0,33 EUR, intention `C`**. Brut reconstitué ≈ **13 000 à 14 000**.

**Exclus :** `art de la table le bon coin` 170 + `le bon coin art de la table` 170 + `arts de la table le bon coin` 140 + `leboncoin art de la table` 140 + `leboncoin arts de la table` 140 (**≈ 760, occasion**) · `magasin art de la table` 480 + `art de la table magasin` 480 + `magasins art de la table` 170 + `art de la table nantes` 110 (**≈ 1 240, recherche locale de magasin physique**) · `grossiste art de la table` 170 (**B2B**) · `location art de la table` 140 (**prestation**) · `livre art de la table` 390 + `art de la table livre` 170 (**≈ 560, informationnel**) · `art de la table hermès` 170 + `hermes art de la table` 140 + `arts de la table peugeot` 170 (**≈ 480, marque**).

**Net de marque ≈ 12 500. Mais l'adressable produit est faible** : ce qui reste est majoritairement `arts de la table` / `l'art de la table` / `les arts de la table` / `vaisselle art de la table`, c'est-à-dire **le nom de la catégorie**, pas un produit.

**Décision de consolidation : `art de la table` n'entre PAS dans le consolidé.** Motif : c'est le **niveau parent qui chapeaute les familles déjà comptées**. L'additionner reviendrait à compter deux fois le même marché — exactement l'interdit n° 1. Il est mesuré, documenté, et mis de côté comme **nom d'univers, pas comme famille**.

**`set de service bois` et `couvert a salade bois` : non mesurés** (§8). La famille « service assorti » du brief est donc **vide de mesure** dans ce rapport.

### 3.7 Famille **Pierre / matière mixte**

`plateau ardoise` — 100/100 lignes, 100ᵉ à 0. Tête **480**, KD 11, CPC 0,43 EUR.
**Retenus :** `plateau ardoise` 480 · `ardoise plateau` 390 · `plateau en ardoise` 390 · `plateaux en ardoise` 320 · `ardoise plateau fromage` 140 · `plateau ardoise fromage` 140 · `plateau à fromage ardoise` 140 · `plateau à fromage en ardoise` 140 · `plateaux ardoise` 140 · `plateau fromage ardoise` 110 · `plateau fromage en ardoise` 110 · `plateau imitation ardoise` 90 · `plateau ardoise rond` 70 · `plateau a fromage (en) ardoise` 30+30 · `plateau de fromage (en) ardoise` 30+30 + queue.
**Brut ≈ 3 200.**
**Exclus :** `billard plateau ardoise` 40 · `plateau ardoise billard` 30 · `billard americain plateau ardoise` 20 · `billard avec plateau ardoise` 20 · `billard plateau ardoise ou mdf` 20 · `billard plateau marbre ou ardoise` 20 → **≈ 150, tapis de billard en ardoise, autre marché** · `plateau ardoise action` 90 + `action plateau ardoise` 20 → **110, marque**.
**Net de marque : ≈ 3 090. Adressable retenu : 2 940.**

**`plateau marbre` : non mesuré séparément** (§8). Indice indirect : `planche à découper marbre` 1 300 + `en marbre` 1 000 + `planche a decouper marbre` 720 + `dessous de plat (en) marbre` 140+140 — le marbre existe, mais il est rattaché à la découpe et au dessous-de-plat, pas au plateau de service.

---

## 4. Arbitrage `planche apéro` contre `planche à découper` — motivé par la SERP

C'est le piège 5.b du brief, et il se tranche par la SERP, pas par le volume.

### Ce que pèsent les deux

| | `planche apéro` (art de la table) | `planche à découper` (ustensile de cuisine) |
|---|---|---|
| Corpus sans accent | tête 9 900 · brut ≈ 36 000 | tête **14 800** · brut ≈ 40 000, **plancher** (100ᵉ à 90) |
| Corpus avec accent | tête 2 900 · brut ≈ 18 000 | tête `planche à découper bois` **6 600** · brut ≈ 50 000, **plancher** (100ᵉ à 170) |
| KD / CPC | 17 / 0,29 EUR · 12 / 0,29 EUR | 17 / 0,27 EUR · 21 / 0,23 EUR |
| Intention SEMrush | I | I |

### Ce que sert Google, lu le 28/08/2026

**`planche apero`** — page 1 mixte :
- **Spécialistes / DTC** : `maplancheapero.fr` (position 1 organique, planches personnalisables bois, « cadeau qui se bonifie ») · `lesplanchesduchef.fr` (chêne, atelier en Touraine, jusqu'à 1 m, 4,9/194 avis) · `lessavouristes.fr` · `proebo.fr` (planche jetable carton **pour charcutiers-traiteurs**, B2B).
- **Éditorial / alimentaire** : `tableauxparis.com` (traiteur, plateaux composés de fromages) · `cuisineaz.com` (« 37 recettes de planche et plateau apéro ») · Pinterest · `maitreprunille.com` · `cocoandco-france.com` · un bloc « Vidéos courtes » entièrement composé de recettes (750g, Chefclub, Degustabox).
- Les **quatre questions du bloc « Autres questions » sont toutes informationnelles** : « Qu'est-ce qu'on peut mettre sur une planche apéro ? », « Comment faire une planche pour l'apéritif ? », etc.
- **Marketplaces / enseignes** dans le carrousel produits : Amazon (×3), Centrakor, Leroy Merlin, Nature & Découvertes.
- **Intention : partiellement.** Environ **5 à 6 positions sur 10 sont éditoriales ou alimentaires**. Une collection seule ne prend pas cette page.

**`planche à découper bois`** — page 1 **entièrement commerciale** :
- **Spécialistes / DTC** : `chabret.fr` (Billots Chabret, haut de gamme, sur mesure) · `maitrecoutelier.com` (27 à 89 €) · `la-planche-francaise.fr` (« bois 100 % français », « fabrication artisanale, atelier en Bourgogne ») · `boisantique.shop` (bois de bout, chêne centenaire, noyer noir) · `lecomptoirdefrance.com` · `couteauxduchef.com` (éditorial) · `wordans.fr` (personnalisation B2B).
- **Marques** : Zwilling.
- **Marketplaces / enseignes** : IKEA (×4 + résultat organique), Leroy Merlin (×5), Amazon (×4), BUT, Brico Dépôt, JYSK, Boulanger, Carrefour, Maisons du Monde, vidaXL, Castorama, Klarna, idealo.
- **Intention : oui, pleinement.** Zéro position recette.

### La décision

**Les deux ne sont pas additionnés, et `planche à découper` n'entre pas dans l'univers.** Trois motifs, dans l'ordre :

1. **Intention et persona différents.** `planche apéro` est un objet de réception, offrable, servi par des spécialistes du cadeau ; `planche à découper` est un ustensile de cuisine servi par le rayon bricolage et l'ameublement. Le test « une page ou deux ? » répond **deux**, et même deux boutiques.
2. **C'est le dossier clos.** Le haut de gamme de `planche à découper` **est** le billot : `chabret.fr` s'appelle « Billots Chabret », `boisantique.shop` vend du bois de bout, `la-planche-francaise.fr` titre « planches à découper **et billots** ». Les requêtes `planche à découper bois debout` 720 · `planche à découper en bois debout` 720 · `planche a decouper bois debout` 210 · `planche a decouper en bois debout` 210 le confirment côté mesure. Entrer dans `planche à découper` par le haut de gamme, c'est **rouvrir le STOP mesure express du 01/08**. Interdit.
3. **§4 des critères, littéralement.** IKEA, BUT, JYSK, Leroy Merlin, Brico Dépôt, Maisons du Monde, Boulanger, Castorama, Carrefour tiennent le carrousel de `planche à découper bois`. C'est la liste d'exclusion du document de critères, mot pour mot.

**Volume écarté par cet arbitrage : ≈ 90 000 (les deux corpus `planche a decouper` + `planche à découper`, brut, planchers tous les deux).** Ce chiffre n'entre nulle part dans le consolidé et ne doit jamais y entrer.

**Contamination couteaux, mémoire du 02/08.** Le carrousel de `planche apero` et celui de `plateau charcuterie` sont pleins de bundles « planche + couteaux à fromage » (« planche apéro en bambou **avec tiroir coulissant et couteaux à fromage inclus** » 29,99 € Leroy Merlin ; « planche à fromage et couteau en bambou » 59,99 € Amazon ; « planche à fromage en bambou **avec 4 couteaux** » 22,99 €). La page 1 de `planche à découper bois` est tenue par MaitreCoutelier, Couteauxduchef, Zwilling et Laguiole. **AliExpress rend la catégorie couteaux de cuisine invisible à la livraison France** (constat du 02/08/2026) : tout bundle planche + couteaux est **non sourçable** en l'état. Noté comme risque, pas chiffré — c'est une contrainte de phase 4.

---

## 5. Vérification SERP par tête de famille

google.fr, `hl=fr&gl=fr`, lectures du **28/08/2026**. **Limite : le navigateur porte la session de Hakim ; une personnalisation des résultats ne peut pas être exclue.**
**Aucune annonce Search texte n'a pu être isolée sur ces quatre pages.** Ce qui est visible est un **carrousel de produits**, et sur `dessous de plat` un bloc explicitement labellisé **« Produits Sponsorisés … Par Google »** (annonces Shopping). Je ne conclus rien sur la pression publicitaire Search.

### 5.1 `planche apero` (9 900) — **intention partielle, volume partiellement retenu**

| Colonne | Lecture |
|---|---|
| **Ce que Google sert** | Un spécialiste DTC en position 1, puis un traiteur, puis vidéos-recettes, puis un carrousel produits, puis Pinterest et trois blogs de recettes, puis deux spécialistes bois français |
| **Intention** | **Partiellement.** Le mot désigne autant la garniture que le support |
| **Commercial / informationnel** | **5 à 6 positions sur 10 éditoriales ou alimentaires** ; les 4 questions du PAA sont toutes informationnelles |
| **Spécialistes / DTC** | `maplancheapero.fr` · `lesplanchesduchef.fr` (4,9/194) · `lessavouristes.fr` · `proebo.fr` (B2B jetable) |
| **Marketplaces / enseignes** | Amazon ×3 · Centrakor · Leroy Merlin · Nature & Découvertes |
| **Bande de prix observée** | 8,99 € (Centrakor) · 9,80 € (Proébo, carton) · 15,99 € (Amazon, remisé de 21 €) · 26,90 € (Livoo / Nature & Découvertes) · 27,92 € (Cosy & Trendy) · 29,99 € (Leroy Merlin, remisé de 33 €) · 39,25 € · 43,56 € · **152,50 €** (lessavouristes.fr, « planche à partager Aperitivo » — vraisemblablement une planche **garnie**, pas un support nu) |
| **Volume** | **Retenu à 30–40 %** de la tête, soit 3 000 à 4 000. Motif : une collection produit ne prend pas les positions recette |

### 5.2 `plateau charcuterie` (5 400) — **intention non, volume retiré intégralement**

| Colonne | Lecture |
|---|---|
| **Ce que Google sert** | **De la nourriture.** Carrefour Traiteur, Maison Garcia (charcuterie espagnole), Auchan Le Traiteur, Veepee, Maison Moga, Maison Lascours, Chez André (ateliers lyonnais), Fromages Constant, Tête De Lard. Deux **packs locaux** de boucheries-charcuteries et traiteurs (Maison Emeraud, Le Cellier des Gourmands, Bonne Tranche - Belles Planches, Zest Planche, La Cense) |
| **Intention** | **Non.** La requête désigne un plateau **garni**, commandé chez un traiteur |
| **Commercial / informationnel** | Commercial, mais **d'un autre marché**. Les 4 questions du PAA portent sur « quelle charcuterie mettre » et « la règle 3-3-3 ». Le bloc vidéos est intégralement recette |
| **Spécialistes / DTC** | Aucun spécialiste de l'objet. Uniquement des charcutiers et traiteurs |
| **Marketplaces / enseignes** | Carrefour, Auchan, Veepee, Amazon |
| **Bande de prix observée** | 5,00 € · 5,95 € · 7,95 € · 8,50 € · 10,99 € · 13,50 € · 13,81 € · 15,29 € · 17,50 € · 47,39 € · 48,43 € · 54,99 € · 72,99 € — **ce sont des prix de nourriture**, pas de planches. Les seuls objets présents sont 3 articles Amazon (22,99 € · 39,99 € · 45,96 € · 59,99 €) |
| **Volume** | **Retiré : ≈ 25 000 à 30 000** sur la grappe `plateau charcuterie`, plus ≈ 10 000 à 14 000 sur `plateau de fromage` / `plateau de fruits de mer` / `plateau fromage` dans le parent. **Total alimentaire retiré : ≈ 36 000 à 40 000.** Estimation faite à la composition de la page 1 |

**C'est le retournement de ce dossier, et il est massif.** Sans cette lecture, la somme indicative de 48 K du 22/08 aurait été confirmée à tort par des requêtes de traiteur.

### 5.3 `plateau de service` (2 900) — **intention oui, volume retenu, mais ticket disqualifiant**

| Colonne | Lecture |
|---|---|
| **Ce que Google sert** | Des plateaux, exclusivement. Aucune ambiguïté |
| **Intention** | **Oui** |
| **Commercial / informationnel** | 100 % commercial. Une seule position éditoriale (`la-carafe.fr`, guide d'achat) |
| **Spécialistes / DTC** | `lesjardinsdelacomtesse.com` (mélamine, spécialiste FR) · `nordicnest.fr` · `madeindesign.com` · `la-carafe.fr` · `ma-lunch-box.com` |
| **Professionnel / CHR** | `buffet-plus.com` · `stellinox.eu` (« pour les professionnels et CHR, livraison gratuite dès 300 € HT ») · `equipementpro.fr` — **trois sites B2B sur la page 1**, cohérent avec le vocabulaire « restauration / professionnel » relevé en §3.3 |
| **Marketplaces / enseignes** | IKEA (organique + carrousel), Amazon, Leroy Merlin ×5, Maisons du Monde ×2, Monoprix, Castorama, Jardiland, H&M Home, ManoMano, Klarna, Bigshopper, idealo, LionsHome, Cherchons, leDénicheur, MeilleurVendeur (**7 comparateurs dans le bloc « Sites de produits »**) |
| **Bande de prix observée** | **1,99 €** (IKEA TILLGÅNG) · 4,20 € · 5,00 € · 5,08 € · 6,99 € · 7,99 € · 11,28 € · 12,10 € · 13,54 € · 16,06 € · 17,70 € · 17,90 € · 19,99 € ×2 · 21,00 € · 27,94 € · 28,99 € · 29,00 € · 29,90 € · 29,99 € ×4 · 35,99 € · 36,59 € · 39,90 € · 42,89 € · 48,99 € · **79,79 €** (vidaXL teck massif 70×70) · **168,00 €** (Maison Sarah Lavoine — **marque à récit**, écartée comme comparable par l'étape 9) |
| **Volume** | **Retenu**, ≈ 10 600 adressable. Mais la médiane de prix est à **≈ 25 €** |

### 5.4 `dessous de plat` (5 400) — **intention oui, volume retenu, ticket disqualifiant**

| Colonne | Lecture |
|---|---|
| **Ce que Google sert** | Des dessous-de-plat, plus une définition Wikipédia et un tableau Pinterest de **modèles pour scie à chantourner** (les gens en fabriquent) |
| **Intention** | **Oui**, avec une part informationnelle lexicale mesurable |
| **Commercial / informationnel** | Commercial dominant. Positions informationnelles : Wikipédia + les deux questions du PAA (« Que signifie le mot sous-plat ? », « Quel est le pluriel de sous-plat ? ») + Pinterest DIY |
| **Spécialistes / DTC** | `celadon-paris.com` (céramique et liège, 5,0/155) · `nordicnest.fr` · `letresordesoliviers.fr` (made in France) · `lacasserolerie.com` · `boutique-clouet.fr` (pièces de collection) |
| **Marketplaces / enseignes** | Amazon, Maisons du Monde, IKEA ×3, Leroy Merlin ×2, JYSK, 5five, westwing, Made in Design, Nature & Découvertes + 7 comparateurs |
| **Annonces** | **Bloc « Produits Sponsorisés … Par Google » en tête de page** : Jarditeck by Médicis 35,00 € · BRÜT 22,00 € · Walnut Addicted 62,96 € · GGM Gastro/Staub 41,64 € · Atelier tour après Tour 16,00 €. **Ce sont des annonces Shopping. Aucune annonce Search texte n'a pu être isolée.** |
| **Bande de prix observée** | **1,90 €** · 1,99 € · 2,99 € (IKEA) · 3,00 € (JYSK) · 3,99 € ×2 (Leroy Merlin) · 4,99 € · 5,99 € ×2 · 13,99 € · 16,00 € · 18,99 € · 21,76 € · 22,00 € · 25,90 € · 27,90 € · 34,00 € · 34,99 € · 35,00 € · 41,64 € · **62,96 €** (Walnut Addicted, noyer, seul point au-dessus de 50 €) |
| **Volume** | **Retenu**, ≈ 16 300. Mais **le cœur du marché est à 2–35 €** |

---

## 6. Concurrents observés — spécialistes/DTC contre marketplaces et enseignes

| Famille | Spécialistes / DTC (page 1) | Marketplaces / grandes enseignes (repères seulement) |
|---|---|---|
| **Planches apéro** | `maplancheapero.fr` · `lesplanchesduchef.fr` (chêne, Touraine, 4,9/194) · `lessavouristes.fr` · `proebo.fr` (B2B) | Amazon ×3 · Centrakor · Leroy Merlin · Nature & Découvertes · Gifi et Action **dans le vocabulaire mesuré** |
| **Plateaux de service** | `lesjardinsdelacomtesse.com` · `nordicnest.fr` · `madeindesign.com` · `la-carafe.fr` · `ma-lunch-box.com` · Pylones | IKEA · Amazon · Leroy Merlin ×5 · Maisons du Monde ×2 · Monoprix · Castorama · Jardiland · H&M Home · ManoMano · **7 comparateurs** |
| **Plateaux de service, versant pro** | `buffet-plus.com` · `stellinox.eu` · `equipementpro.fr` | — |
| **Dessous de plat** | `celadon-paris.com` (5,0/155) · `letresordesoliviers.fr` · `lacasserolerie.com` · `boutique-clouet.fr` · BRÜT · Walnut Addicted · Jarditeck · Atelier tour après Tour | Amazon · Maisons du Monde · IKEA ×3 · Leroy Merlin ×2 · JYSK · 5five · westwing · Made in Design · **7 comparateurs** |
| **Planches à découper** *(hors univers, §4)* | `chabret.fr` · `la-planche-francaise.fr` · `boisantique.shop` · `maitrecoutelier.com` · `lecomptoirdefrance.com` | IKEA ×5 · Leroy Merlin ×5 · Amazon ×4 · BUT · Brico Dépôt · JYSK · Boulanger · Carrefour · Maisons du Monde · Castorama · vidaXL |
| **Plateau charcuterie** *(retiré, §5.2)* | Aucun spécialiste de l'objet | Carrefour Traiteur · Auchan Le Traiteur · Veepee + packs locaux de traiteurs |

**Lecture.** Des spécialistes indépendants existent et tiennent des positions — c'est plutôt bon signe en UNIVERS (§4 : s'inspirer d'un spécialiste en place est une preuve, pas un STOP). **Mais** deux constats gênants :

1. **La pression généraliste est présente sur les quatre têtes**, et pas en périphérie : IKEA, Leroy Merlin, Maisons du Monde, JYSK, BUT, Castorama, Carrefour, Monoprix, Action, Gifi, Centrakor. `PRODUCT-RESEARCH-CRITERIA.md` §4 nomme explicitement IKEA, BUT, JYSK, Maisons du Monde et Leroy Merlin comme motif de rejet.
2. **Les spécialistes qui tiennent le haut de bande le font sur un récit non transférable** : « atelier en Touraine », « fabrication artisanale en Bourgogne », « bois 100 % français », « chêne centenaire », « élaborées sur place dans nos ateliers lyonnais ». C'est exactement le cas écarté par l'étape 9 — la **marque à récit**, sur laquelle on ne s'aligne pas en dropshipping.

**Le comparable au sens de l'étape 9 — ni marque officielle, ni marque à récit, ni marketplace — se situe entre 20 et 45 €** sur les trois familles retenues.

---

## 7. Volume consolidé retenu

**Règle appliquée : on additionne ce qu'une même boutique servirait, ligne à ligne, jamais un total affiché par l'outil, jamais un mot dans deux familles.**
En mode UNIVERS, additionner les collections d'un même catalogue n'est pas du gonflage. Le niveau parent `art de la table` est **exclu du total** pour ne pas compter deux fois les familles qu'il chapeaute.

| Famille | Brut reconstitué | Net de marque | **Adressable retenu** | Base |
|---|---|---|---|---|
| Plateaux de service | ≈ 12 410 | ≈ 11 470 | **10 600** | 100/100 lignes, couvert |
| Plateau petit déjeuner (2 orthographes) | ≈ 6 200 | ≈ 5 620 | **5 400** | 200 lignes, couvert |
| Plateau apéro — résidu objet | ≈ 12 700 | ≈ 12 170 | **680** | 100/100 lignes, couvert |
| Plateau ardoise / matière mixte | ≈ 3 200 | ≈ 3 090 | **2 940** | 100/100 lignes, couvert |
| Planches apéro (sans accent) | ≈ 36 000 | ≈ 34 930 | **10 000 à 11 000** | 100/100 lignes, couvert |
| Planches apéro (avec accent) | ≈ 18 000 | ≈ 17 100 | **4 500** | 100/100 lignes, couvert |
| Planche à fromage (2 orthographes) | ≈ 1 300 | ≈ 1 290 | **800** | couvert |
| Planche charcuterie — résidu non recompté | ≈ 14 000 | ≈ 14 000 | **1 000** | 100/100 lignes, couvert |
| Dessous de plat | ≈ 17 600 | ≈ 16 570 | **16 300** | 100/100 lignes, couvert |
| **CONSOLIDÉ UNIVERS** | **≈ 121 400** | **≈ 116 240** | **≈ 52 200** *(fourchette 51 200 – 53 200)* | |

**Scénario prudent** (aucune part attribuée aux têtes ambiguës `planche apero` 9 900 et `planche apéro` 2 900) : **≈ 48 200**.
**Scénario haut** (40 % des têtes ambiguës) : **≈ 53 200**.

**Le consolidé net est donc robustement compris entre 48 000 et 53 000/mois, au-dessus du plancher UNIVERS de 30 000 et au-dessus du confort de 40 000.**
Ce n'est **pas** un cas limite au sens de la règle des ±20 % (24 000 – 36 000).

### Ce qui a été retiré, et son poids

| Retrait | Volume | Motif |
|---|---|---|
| Niveau parent `plateau` (géographie, médical, camion, jeu de société, anglais) | **≈ 90 000** | Homonymie totale |
| Niveau parent `planche` (plancha, coffrage, OSB, plancher, surf, repassage) | **≈ 200 000** | Homonymie totale |
| `plateau bois` — plateaux de **table et de bureau** | **≈ 33 000 à 35 000** | Piège n° 1, retournement pièce / produit fini + GSB |
| **Alimentaire** (`plateau charcuterie`, `plateau de fromage`, `plateau de fruits de mer`) | **≈ 36 000 à 40 000** | SERP §5.2 : traiteur, pas objet |
| **Informationnel apéro** (recette, idée, présentation, composition, saisonnier) | **≈ 22 000 à 24 000** | Une collection ne prend pas ces pages |
| **Restauration / bar à planches / jetable pro** | **≈ 2 100** | Persona professionnel |
| **`planche à découper` (2 orthographes)** | **≈ 90 000** | Arbitrage §4 : autre intention, autre persona, §4 GSB, et haut de gamme = dossier billot clos |
| **Marques et enseignes** (IKEA, Maisons du Monde, Action, Gifi, Centrakor, Leroy Merlin, Alinéa, Amazon, Cdiscount, Leclerc, Carrefour, Super U, Habitat, Fermob, Staub, Boska, LU, Hermès, Peugeot, Zwilling) | **≈ 5 200** | Inutilisable en flux Merchant Center et en titre produit |
| **`art de la table`** | **≈ 12 500 net** | Niveau parent des familles déjà comptées — exclu pour ne pas doubler |

### Volume `billot` retiré — chiffré

Dossier **STOP mesure express du 01/08**, non relancé. Mesuré aujourd'hui pour le chiffrer, pas pour le rouvrir.

`billot` — 100/100 lignes, 100ᵉ à 140, **plancher**. Tête 4 400, KD 14, CPC 0,29 EUR.

| Ligne produit | Volume |
|---|---|
| `billot` | 4 400 |
| `billot de boucher` | 3 600 |
| `billot de bois` | 1 900 |
| `billot de cuisine` | 1 000 |
| `billot bois` | 590 |
| `billot boucher` | 590 |
| `billot en bois` | 590 |
| `billot cuisine` | 480 |
| **Sous-total billot** | **≈ 13 150** |
| `planche à découper bois debout` | 720 |
| `planche à découper en bois debout` | 720 |
| `planche a decouper bois debout` | 210 |
| `planche a decouper en bois debout` | 210 |
| **Sous-total bois de bout** | **≈ 1 860** |
| **TOTAL BILLOT / BOIS DE BOUT RETIRÉ** | **≈ 15 010** |

Le reste de la grappe `billot` est du bruit pur, également retiré : `fayl billot` 2 900 et `meteo fayl billot` 590 (commune de Haute-Marne), `le billot de marius` 1 000, `le billot de lucien` 880 + `restaurant le billot de lucien` 720, `le billot de leon` 720, `le billot albi` 720, `le billot beauvais` 590, `billot des abattoirs` 480 (restaurants), `frédéric billot` 1 000, `kimberley le court de billot` 590 (personnes), `billot club` 720. **≈ 11 000 supplémentaires.**

**Aucun de ces 15 010 n'entre dans le consolidé. Le dossier reste clos.**

---

## 8. Bande de prix observée — et pourquoi elle décide

Toutes lectures en SERP et carrousel produits Google France, **28/08/2026**. Aucune estimation.

| Famille | Bande observée | Médiane visuelle | Points > 50 € |
|---|---|---|---|
| Planches apéro | **8,99 € – 43,56 €** | ≈ 28 € | 1 seul (152,50 €, et c'est une planche **garnie**) |
| Plateaux de service | **1,99 € – 48,99 €** | ≈ 25 € | 2 (79,79 € vidaXL teck ; 168 € Maison Sarah Lavoine = marque à récit) |
| Dessous de plat | **1,90 € – 41,64 €** | ≈ 15 € | 1 (62,96 € Walnut Addicted, noyer) |
| Planches à découper *(hors univers)* | **6,99 € – 78,99 €** | ≈ 30 € | quelques-uns, tous chez des artisans français à récit (27 – 89 €) |

**Le plancher de prix de `PRODUCT-RESEARCH-CRITERIA.md` §1 est de 50 € TTC.** Sur les trois familles retenues, **les points au-dessus de 50 € se comptent sur les doigts d'une main, et chacun est soit un produit alimentaire, soit une marque à récit, soit un bois précieux d'artisan.**

**La sonde du 22/08 à 72,36 € n'est pas retrouvée par cette lecture.** Je ne sais pas sur quelle requête elle a été prise ; si c'était sur `planche à découper` ou sur un billot, elle mesurait la famille que le présent rapport écarte. **Contradiction à arbitrer par Hakim.**

Contrôle du ratio de l'étape 9 : avec un CPC médian de **0,30 EUR**, le ratio prix ÷ CPC ≥ 100 exigerait un prix ≥ 30 €, et la cible 150–200 un prix de 45 à 60 €. **Le ratio n'est donc pas le point de blocage — le point de blocage est le plancher de 50 € et l'absence de bande au-dessus.**

---

## 9. Réserves — aucune retirée

1. **Six graines du brief n'ont pas été mesurées, faute de temps de session** : `set de service bois`, `couvert a salade bois`, `plateau marbre`, `plateau tournant`, `plateau repas`, plus les dérivées suggérées `saladier bois`, `bol bois`, `corbeille a pain`. **La famille « Service assorti » du brief est donc vide de mesure dans ce rapport.** Le consolidé de 52 200 est **un plancher de ce côté-là**, pas un total.
2. **Cinq grappes sur dix-neuf sont des planchers de lecture** (100ᵉ ligne encore haute) : `plateau` (1 900), `planche` (2 400), `plateau charcuterie` (90), `planche a decouper` (90), `planche à découper` (170), `billot` (140). Trois d'entre elles concernent des corpus **retirés**, ce qui rend les retraits eux-mêmes des **planchers** : le volume réellement écarté est supérieur à ce que j'ai chiffré.
3. **Les queues de grappe au-delà de la 45ᵉ ligne sont estimées**, pas lues nominativement, sur `dessous de plat`, `planche charcuterie`, `plateau petit déjeuner`, `art de la table`, `plateau ardoise`. Les totaux bruts de ces familles portent donc une incertitude que j'évalue à ±15 %.
4. **L'attribution des têtes `planche apero` (9 900) et `planche apéro` (2 900) est une estimation SERP, pas une mesure.** Je l'écris en fourchette 30–40 %. Si Hakim la juge trop généreuse, le consolidé tombe à ≈ 48 200 ; s'il la juge trop sévère, il monte à ≈ 53 200. **Dans les deux cas le seuil UNIVERS de 30 000 reste franchi.**
5. **Les lignes ambiguës `plateau rond en bois` (1 900), `plateaux ronds bois` (1 300), `plateau bois rond` (1 600), `plateau en bois rond` (1 600), `plateau rond bois` (1 300) — soit 7 700 — n'ont été attribuées à aucune famille.** Elles peuvent désigner un plateau de table ronde (meuble) ou un plateau de service rond (univers). La SERP n'a pas été ouverte dessus. **Fourchette honnête plutôt que total faux.**
6. **Les SERP ont été lues dans le navigateur de Hakim, session Google possiblement connectée.** Une personnalisation des résultats ne peut pas être exclue. Le brief demandait une session non connectée ; je n'ai pas pu le garantir.
7. **Aucune annonce Search texte n'a pu être isolée** sur les quatre SERP. Ce qui est confirmé, ce sont des annonces **Shopping** sur `dessous de plat` (bloc « Produits Sponsorisés … Par Google »). **Je ne rends aucun verdict sur la pression publicitaire Search.**
8. **Aucun Google Trends n'a été relevé.** Le socle ≥ 8 mois exigé par le skill Mission B n'est donc **pas vérifié**. Deux signaux de saisonnalité apparaissent dans le vocabulaire mesuré (`planche apero noel` 590, `halloween` 210, `pere noel` 140, `sapin de noel` 110, `planche apéro pâques` 170, `automne` 170, `hiver` 110, `ete` 110) mais **je n'en tire aucune variation chiffrée** — l'outil ne l'affiche pas.
9. **Contradiction non arbitrée sur le prix** : sonde du 22/08 à 72,36 € contre bande observée aujourd'hui à 2–48 € sur les trois familles retenues. Voir §8.
10. **Contamination couteaux non sourçable** : les bundles « planche + couteaux à fromage » sont omniprésents dans les carrousels. Mémoire du 02/08 : AliExpress rend la catégorie couteaux de cuisine invisible à la livraison France. Contrainte de phase 4, non chiffrée ici.
11. **Le §4 des critères est déclenché littéralement** : IKEA, BUT, JYSK, Maisons du Monde et Leroy Merlin — cinq des enseignes nommément listées comme motif de rejet — tiennent des positions sur les quatre têtes de famille.
12. **La preuve boutique du 22/08 (`bcd-design.com`, 47 ads, 921 j, reach 1,875 M) n'a pas été revérifiée** et n'entre pas dans ce verdict. Elle reste le meilleur argument en faveur du dossier : un annonceur qui tient 921 jours sur ce marché a trouvé une économie que ce rapport ne voit pas.
13. **Aucun sourcing, aucun fournisseur, aucune fiche produit ouverte.** Hors périmètre.

---

## 10. Verdict

### **REVIEW_PREQUALIFICATION**

**Le seuil UNIVERS de 30 000/mois (confort 40 000) est franchi.** Consolidé net de marque adressable : **≈ 52 200/mois**, fourchette 48 200 – 53 200. La demande existe, elle est répartie sur au moins quatre familles qu'une même boutique servirait, et des spécialistes indépendants français tiennent des positions en page 1 — ce qui, en mode UNIVERS, est une preuve et non une occupation.

**Mais un obstacle majeur est identifié, et il n'est pas de volume — il est de ticket.**

1. **La bande de prix observée en SERP le 28/08/2026 est de 2 à 48 € sur les trois familles retenues.** Le plancher de `PRODUCT-RESEARCH-CRITERIA.md` §1 est de **50 € TTC**. Les rares points au-dessus sont soit alimentaires, soit des marques à récit (Maison Sarah Lavoine 168 €), soit des artisans français en bois précieux — trois catégories que l'étape 9 écarte explicitement comme comparables.
2. **Le §4 se déclenche littéralement** : IKEA, BUT, JYSK, Maisons du Monde, Leroy Merlin — cinq enseignes de la liste de rejet — plus Castorama, Brico Dépôt, Carrefour, Monoprix, Jardiland, Action, Gifi et Centrakor, tiennent des positions sur les quatre têtes.
3. **Le seul angle qui fait monter le ticket est la personnalisation** (`planche apero personnalisé` 1 000 · `personnalisable` 210 · `planche apéro personnalisée` 590 · `personnalisé` 390 · `plateau de service personnalisé` 50 · `dessous de plat personnalisé` 260+210 ≈ **2 700**, et le n° 1 organique `maplancheapero.fr` est bâti dessus). **C'est un métier d'atelier de gravure, pas un modèle dropshipping.**

**Ce n'est pas un STOP** : le volume est là, franchement au-dessus du seuil, et un annonceur tient 921 jours sur ce marché. **Ce n'est pas un PASS** : autoriser la due diligence sourcing sur un univers dont toute la bande de prix observée est sous le plancher de 50 € reviendrait à dépenser une phase 4 pour découvrir un tueur déjà visible en phase 3.

### Ce que j'attends de Hakim, et que je ne tranche pas

1. **Le plancher de 50 €.** Le tient-on sur ce dossier, ou l'univers arts de la table bois est-il précisément le cas où l'économie de panier (plateau + planche + dessous-de-plat + set) remplace le ticket unitaire ? Le §0.6 prévoit un pipeline UNIVERS avec « économie de panier » — c'est la question qu'il pose.
2. **La contradiction de prix** entre la sonde du 22/08 (72,36 €) et la lecture SERP d'aujourd'hui (2–48 €). Sur quelle requête la sonde a-t-elle été prise ?
3. **Le drapeau §4.** Lève-t-on l'exclusion IKEA / Leroy Merlin / Maisons du Monde / JYSK / BUT sur ce dossier, comme la question s'est déjà posée sur les candidats mobilier écartés de la sélection ?

**Aucun `GO_FINAL` n'est prononcé. Aucune décision commerciale n'est prise.** Rappel du contrat `PRODUCT-RESEARCH-CRITERIA.md` §0.6 : aucun `GO_FINAL` UNIVERS n'est possible tant que la sourçabilité par famille (3–5 familles pesant ≥ 70 % du volume, chacune ≥ 2 fournisseurs plausibles) n'est pas documentée — ce qui relève de la phase 4 et n'a pas été touché ici.

Les 3–5 familles pesant ≥ 70 % du consolidé, à sourcer si Hakim relance : **Dessous de plat (16 300, 31 %) · Planches apéro deux orthographes (14 500 à 15 500, 29 %) · Plateaux de service (10 600, 20 %) · Plateau petit déjeuner (5 400, 10 %)** — ces quatre pèsent **90 %** du consolidé.

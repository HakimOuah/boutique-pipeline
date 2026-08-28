# Mission B UNIVERS — préparation et déclaration d'arrêt

**Date : 2026-08-28** · Orchestrateur `/recherche-produit`, mode **UNIVERS** · Décision Hakim du 28/08 : Mission B sur les survivants de la salve 30×30, pas de nouvelle idéation.

---

## 1. Résultat en une phrase

La chaîne **n'a pas démarré** : SEMrush est inaccessible (extension Chrome non connectée), et Mission B est entièrement dépendante de SEMrush pour ses étapes 2 à 4. Arrêt fail-closed n° 3 (donnée invérifiable). Ce document contient tout le travail qui ne dépendait pas de l'outil, prêt à être exécuté dès reconnexion.

---

## 2. Anti-doublon — ce qui existe déjà

Vérifié dans `registre-candidats.md`, `plans/`, `analyses/` :

| Salve | Date | État | Conséquence |
|---|---|---|---|
| 6 niches univers (U1–U6) | 15/08 | Analysée. Aucun GO. U3 globe seul à passer le marché (66 550 nets), échoue en sourcing (59 concepts / 200) | Ne pas relancer |
| Recherche 30×30 | 22/08 | **Terminée** : ~64 univers mesurés → 32 survivants → shortlist 30 · sourcing AE 60/60 | Base de la Mission B |

**Réserves écrites sur la shortlist 30×30, qui sont précisément l'objet de Mission B :**

- sommes de volume **indicatives** — têtes de familles en KMT `mt=phrase`, sans consolidation ;
- **aucun Trends socle** ;
- **aucune vérification SERP** ;
- sourcing majoritairement en confiance **B** (JSON de SERP), pas de PDP lue ;
- aucun GO Hakim.

Rappel du contrat : `PRODUCT-RESEARCH-CRITERIA.md` §0.6 interdit tout `GO_FINAL` UNIVERS tant que la consolidation par familles **et** la sourçabilité par famille (3–5 familles pesant ≥ 70 % du volume, chacune ≥ 2 fournisseurs plausibles) ne sont pas documentées.

---

## 3. Contradiction à arbitrer — aquariophilie

Deux fichiers du **même jour** (22/08) se contredisent sur ce candidat :

| Source | Contenu |
|---|---|
| `ideation-trendtrack-univers.md`, tableau des écartés | « Aquariophilie / terrariophilie / paludarium — aucune boutique preuve nette obtenue (bruit systématique) ; aucun angle réellement nouveau identifié. **STOP Kraken (08/08) confirmé, non relancé.** » |
| `shortlist-30-univers.md`, ligne 12 | « Aquariophilie / aquascaping — **86K** — sonde **OK ~74 €** — profil catalogue type Nuisette » |
| `mission-b-pilote.md` | « Aquariophilie (`aquarium`) — SERP Shopping, **marketplaces faibles (Amazon seul détecté)** — **profil favorable** » |

C'est le candidat au **meilleur profil SERP de toute la shortlist** (pression marketplace faible, ce qui est rare), et il est simultanément déclaré écarté à l'idéation. Application de la règle de maintenance de l'orchestrateur : un fichier canonique contradictoire s'arrête et remonte, il ne se contourne pas.

**Décision attendue de Hakim :** `reprise motivée` sur aquariophilie (et je le traite en Mission B), ou maintien du STOP Kraken du 08/08 (et je le sors du périmètre). Je ne tranche pas.

---

## 4. Sélection retenue pour Mission B — 4 candidats + 1 suspendu

Critères de sélection : sonde prix **dans la tranche** 50–400 €, preuve boutique datée et nette, absence de drapeau §4 rédhibitoire non arbitré, absence de recoupement avec le parc existant.

| Rang | Candidat | Somme indicative | Sonde 22/08 | Preuve | Pourquoi retenu |
|---|---|---|---|---|---|
| 1 | **Vin & œnologie** (#16) | 78K | à faire | L'Atelier du Vin, Vinatis, Comptoir des Sommeliers | **Seule confiance A** de la salve. Marque française installée = validation de demande en UNIVERS, pas occupation. Bande documentée : coffrets 147–480 €, accessoires 6–85 € |
| 2 | **Diffusion olfactive intérieure** (#11) | 87K | 64,99 € | `ambiance-parfum.com` — 9 ads, **1 754 j d'ancienneté**, reach 10 M | Plus gros volume de la sélection, ancienneté qui prouve un modèle qui tient. Réachat naturel (recharges) |
| 3 | **Rideaux occultation matière × intention** (#17) | 74K | à faire | `coclic-alu.fr`, `instantrideau.com`, `passionvelours.com`, `rideau-chainette-store.com` | Modèle matière × intention déjà éprouvé à la maison sur Lumière Matière. Cluster déjà qualifié niveau 0 le 01/08 |
| 4 | **Arts de la table bois** (#23) | 48K | 72,36 € | `bcd-design.com` (SARL Bois Carbone Design) — 47 ads, 921 j, reach 1,875 M | Offrable Q4, familles épaisses, panier composé plausible |
| — | *Aquariophilie* (#12) | *86K* | *73,99 €* | *contradictoire* | **Suspendu** — voir §3 |

### Écartés de la sélection, avec motif

- **#27 Studio créateur de contenu** (34K, sonde 83,99 €) — l'idéation documente elle-même le tueur : *« le cœur de marché est largement sous 50 € ; seul un kit complet premium pourrait approcher 150–250 € »*. Confiance C. Le risque prix est identifié avant mesure, on ne dépense pas de crédits dessus.
- **#19 Déco Noël** (64K, sonde 155 €) — échec sourcing documenté au bilan + saisonnalité incompatible avec l'exigence de socle ≥ 8 mois.
- **#1, #2, #6, #10, #21** (dressing, mobilier outdoor, meuble gain de place, tapis, rangement chaussures) — tous portent un drapeau §4 non arbitré (IKEA, Saint Maclou, GSB) et l'exclusion explicite « meubles courants sans usage différencié ». À traiter seulement si tu lèves le drapeau.
- **#22 Portage bébé** (54K, sonde 72,9 €) — GMC enfants + marques installées. Recevable, mais le risque de conformité est à trancher avant, pas après.

---

## 5. Plan de mesure, prêt à tirer

Protocole imposé : SEMrush **base France** (`db=fr`), Keyword Magic Tool en expression exacte (`&mt=phrase`), 100 lignes, 0 crédit. Les cinq contrôles à chaque passe. Trois niveaux de généralité **séparés, jamais additionnés**. Deux chiffres par famille : **brut et net de marque**.

Rappel de la leçon du 15/08 : mesurer 4 à 11 requêtes par univers avait sous-évalué les totaux d'un facteur **2,1 à 6,4**. Les graines ci-dessous sont donc construites famille par famille, pas en tête unique.

### 5.1 Vin & œnologie

| Famille | Mot de la maison | Mot du particulier | Catégorie parente |
|---|---|---|---|
| Ouverture | `tire-bouchon sommelier`, `limonadier` | `tire bouchon`, `ouvre bouteille vin` | `accessoire vin` |
| Aération | `décanteur`, `carafe à décanter` | `carafe a vin`, `aerateur de vin` | `service du vin` |
| Conservation | `pompe à vide vin`, `bouchon hermétique vin` | `bouchon vin`, `conserver vin ouvert` | `conservation vin` |
| Verrerie | `verre INAO`, `verre dégustation` | `verre a vin`, `verre a pied` | `verrerie` |
| Coffret | `coffret sommelier`, `coffret dégustation` | `coffret vin cadeau` | `coffret oenologie` |
| Cave | `cave à vin de vieillissement` | `cave a vin`, `armoire a vin` | `cave a vin` |

Doubles orthographes obligatoires : `décanteur`/`decanteur`, `œnologie`/`oenologie`, `cave à vin`/`cave a vin`, `aérateur`/`aerateur`.
Net de marque à retirer : L'Atelier du Vin, Peugeot, Screwpull, Vacu Vin, Riedel, Spiegelau, Le Creuset.
**Piège attendu :** `cave à vin` bascule massivement vers l'électroménager (Climadiff, Liebherr, Darty) — c'est une autre famille et probablement une autre boutique. À mesurer séparément, et à retirer si la SERP le confirme.

### 5.2 Diffusion olfactive intérieure

| Famille | Mot de la maison | Mot du particulier | Catégorie parente |
|---|---|---|---|
| Diffuseur électrique | `diffuseur nébulisation`, `diffuseur ultrasonique` | `diffuseur huile essentielle`, `diffuseur parfum maison` | `diffuseur` |
| Diffuseur sec / bâtonnets | `diffuseur à bâtonnets` | `bouquet parfumé`, `batonnet parfum maison` | `parfum d interieur` |
| Recharges | `recharge parfum d'intérieur` | `recharge diffuseur` | `recharge` |
| Bougies assorties | `bougie parfumée cire végétale` | `bougie parfumee maison` | `bougie` |
| Coffret saisonnier | `coffret senteurs` | `coffret parfum maison cadeau` | `coffret` |
| Voiture (extension) | `diffuseur voiture` | `parfum voiture` | `desodorisant voiture` |

Doubles orthographes : `parfumée`/`parfumee`, `intérieur`/`interieur`, `bâtonnets`/`batonnets`, `nébulisation`/`nebulisation`.
Net de marque : Diptyque, Maison Berger, Yankee Candle, Durance, Esteban, Rituals.
**Piège attendu :** contamination par les huiles essentielles thérapeutiques (intention santé, et claims interdits en GMC). Toute requête d'usage médical est à retirer du volume adressable, pas à conserver.

### 5.3 Rideaux occultation matière × intention

| Famille | Mot de la maison | Mot du particulier | Catégorie parente |
|---|---|---|---|
| Occultation | `rideau occultant total` | `rideau occultant`, `rideau qui bloque la lumiere` | `rideau` |
| Thermique | `rideau isolant thermique` | `rideau anti froid`, `rideau isolant` | `isolation fenetre` |
| Phonique | `rideau acoustique` | `rideau anti bruit`, `rideau phonique` | `isolation phonique` |
| Velours | `rideau velours` | `rideau velours salon` | `rideau deco` |
| Lin | `rideau lin lavé` | `rideau lin`, `voilage lin` | `rideau naturel` |
| Accessoires | `tringle à rideau`, `embrasse` | `tringle rideau`, `anneau rideau` | `accessoire rideau` |

Doubles orthographes : `lavé`/`lave`, `lumière`/`lumiere`, `à`/`a` dans `tringle à rideau`.
Net de marque : IKEA, Maisons du Monde, La Redoute, Heytens, Saint Maclou.
**Piège attendu :** le sur-mesure et la pose (prestation, pas produit) — à séparer. Et vérifier que `voilage` ne double pas `rideau` dans la consolidation : test « une page ou deux ? ».

### 5.4 Arts de la table bois

| Famille | Mot de la maison | Mot du particulier | Catégorie parente |
|---|---|---|---|
| Plateaux | `plateau de service bois` | `plateau bois`, `plateau petit dejeuner` | `plateau` |
| Planches | `planche de présentation`, `planche apéro` | `planche apero`, `planche a fromage` | `planche` |
| Dessous de plat | `dessous de plat bois` | `dessous de plat` | `protection table` |
| Service assorti | `set de service bois` | `couvert a salade bois` | `art de la table` |
| Pierre / matière mixte | `plateau ardoise`, `plateau marbre` | `plateau ardoise apero` | `art de la table` |

Doubles orthographes : `apéro`/`apero`, `présentation`/`presentation`, `déjeuner`/`dejeuner`, `à`/`a` dans `planche à fromage`.
Net de marque : Le Creuset, Boska, Berard, Maisons du Monde.
**Piège attendu, déjà documenté :** ne pas rabattre sur `billot de boucher` / `planche bois de bout`, **STOP mesure express du 01/08**. C'est un autre produit et un dossier clos.

---

## 6. Ce qui bloque, précisément

| Élément | État |
|---|---|
| `registre-candidats.md` | ✅ lu |
| `PRODUCT-RESEARCH-CRITERIA.md` | ✅ lu, seuils UNIVERS appliqués (consolidé ≥ 30 000, confort 40 000) |
| `METHODE-ANALYSE-MARCHE.md` | ✅ lu, séquence Mission B appliquée |
| Date du jour | ✅ 2026-08-28 |
| **SEMrush via Chrome** | ❌ **extension Claude in Chrome non connectée** (2 tentatives, `list_connected_browsers` → vide) |
| Clé API SEMrush locale | ❌ absente de l'environnement — aucun chemin de repli scripté |
| Navigateur intégré | ⚠️ disponible mais **sans la session SEMrush de Hakim** → écran de connexion, et la saisie d'identifiants est interdite |

Étapes 2, 3 et 4 de Mission B (mesurer par lots, consolider par familles, net de marque) sont donc **impossibles**. L'étape 5 (SERP) serait techniquement faisable via le navigateur intégré, mais vérifier une SERP sans le volume qu'elle est censée valider n'a aucune valeur : la SERP sert à retirer du volume mesuré, pas à produire un chiffre.

Aucune donnée n'a été inventée pour continuer. Aucune écriture au registre : aucune phase n'a été franchie.

---

## 7. Décisions qui appartiennent à Hakim

1. **Rebrancher Chrome** (extension Claude in Chrome + panneau latéral connecté au même compte), pour que Mission B puisse démarrer.
2. **Arbitrer la contradiction aquariophilie** (§3) : `reprise motivée` ou maintien du STOP.
3. **Confirmer ou corriger la sélection** de 4 candidats (§4), et dire si tu lèves un drapeau §4 sur les candidats mobilier/tapis écartés.

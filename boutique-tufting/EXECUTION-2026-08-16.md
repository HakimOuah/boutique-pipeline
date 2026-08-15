# Exécution Tuftéo — 16/08/2026

Session exécutant-boutique, suite de `AUDIT-GMC-2026-08-16.md`. Rapport écrit au fil de l'eau.
Thème de travail (copie non publiée) : `gid://shopify/OnlineStoreTheme/189410738561` — le thème
MAIN `188623847809` reste interdit à l'écriture. **Aucune écriture Shopify n'a été faite dans cette
session** (relevés et sourcing en lecture seule uniquement) ; aucun statut produit modifié.

Changement en cours de route (message de Hakim) : la tondeuse et les ciseaux électriques sont
finalement sourcés comme le tissu de finition — Hakim traite la question CE directement avec le
fournisseur retenu, mais leur statut produit reste inchangé et le constat de régression est
maintenu dans le rapport.

## État d'avancement

- [x] 1. Tissu de finition — doublon identifié, recommandation donnée
- [x] 2. Tondeuse + ciseaux électriques — sourcés (5-6 fiches chacun), constat CE remonté
- [x] 3. Fils — plan de découpage proposé, **exécution non lancée** (ambiguïté assumée)
- [x] 4. Relevé des images (23 produits)
- [x] 5. Vitesse — mesurée via PageSpeed Insights (mobile), admin Shopify inaccessible (pas de session)
- [x] 6. Décisions qui attendent Hakim
- [x] 7. Ce que je n'ai pas pu vérifier

---

## 1. Tissu de finition — doublon probable, pas de sourcing exécuté

**Constat.** `tissu-de-finition` (ACTIVE, stock 0, 2 variantes 4,2×1 m / 5×1 m, 19,90-22,90 €) et
`tissu-finition-antiderapant` (ACTIVE, stock 115, 5 variantes 1×1 m à 1,8×4 m, 8,90-39,90 €)
couvrent le même besoin client : un tissu à coller au dos d'une pièce tuftée pour la finir. Les deux
sont dans la collection « Toiles & tissus ».

- **Comparaison visuelle** (images CDN ouvertes directement, capture d'écran) : les deux tissus sont
  un tissage gris foncé à petit motif pointillé, visuellement quasi identiques à l'œil — l'un un
  chevron fin, l'autre un pois légèrement plus marqué. Rien qui saute aux yeux comme un produit
  différent.
- **La copie différencie les deux usages** : « tissu de finition » = collé au dos pour un rendu
  propre (pièces à offrir/vendre, pas de fonction antidérapante affichée) ; « antidérapant » =
  spécifiquement pour les pièces posées au sol. Cette distinction existe dans le vocabulaire du
  tufting (finition décorative vs. dos antidérapant pour tapis de sol), donc ce n'est pas
  nécessairement une invention de copywriting.
- **Mais l'offre en rupture est strictement dominée par l'autre fiche** : `tissu-finition-antiderapant`
  a du stock (115), 5 formats (dont un format proche de chacun des deux formats en rupture) et un
  éventail de prix plus large (8,90 à 39,90 € contre 19,90-22,90 €).

**Recommandation (pas tranchée, à confirmer par Hakim) : dépublier `tissu-de-finition` plutôt que
la resourcer.** Le doublon fonctionnel est fort, le produit de remplacement existe déjà en stock, et
rouvrir un troisième fournisseur pour un produit quasi identique n'apporte pas de valeur évidente.
Si Hakim tient à garder la distinction « finition décorative, non antidérapante » pour les pièces
murales, je peux sourcer sur demande — je ne l'ai pas fait par défaut vu le doublon.
**Aucune action exécutée** (ni sourcing, ni dépublication — c'est une décision catalogue, pas un
constat technique).

---

## 2. Tondeuse et ciseaux électriques — sourcing fait, statut inchangé, CE remonté sans trancher

### 2a. Constat CE (ce que Hakim a demandé de documenter, pas de trancher)

D'après `project-state.md` (entrée du 21/07, confirmée par git log) : au moment de la francisation,
**3 produits ont été passés en DRAFT « garde-fou électrique » en attente de conformité CE** — la
tondeuse 200 W, les ciseaux électriques, et le kit tondeuse+guide.

État constaté aujourd'hui (API Shopify, 16/08) :

| Produit | Statut au 21/07 | Statut constaté le 16/08 |
|---|---|---|
| `tondeuse-professionnelle-tapis` | DRAFT | **ACTIVE** |
| `ciseaux-electriques-sculpture` | DRAFT | **ACTIVE** |
| `kit-tondeuse-guide-tonte` | DRAFT | DRAFT (inchangé) |

**Je n'ai trouvé aucune trace écrite** (ni dans `project-state.md`, ni dans son historique git, ni
dans les fichiers `shopify/*.md` du dossier boutique-tufting) d'une décision documentée de
réactiver la tondeuse et les ciseaux entre le 21/07 et aujourd'hui — alors que le kit, lui, est
resté en DRAFT sans discontinuité apparente. Je ne sais donc pas dire *quand* ni *pourquoi* le
changement a eu lieu : je constate l'écart entre le garde-fou documenté et l'état actuel, sans
pouvoir l'expliquer. Je n'ai touché le statut d'aucun des trois produits.

### 2b. Sourcing — Tondeuse professionnelle pour tapis (actuel : 89,90 €, 0 en stock)

Recherche `search` (API) infructueuse : « tufting trimmer » et « carpet weaving trimmer » sont
happés par les tondeuses à cheveux/barbe/oreilles (mot fréquent « trimmer/tondeuse »), aucun résultat
pertinent — cas « famille sans mot rare » de la recette. Passage par la **SERP JSON**
(`fr.aliexpress.com/w/wholesale-...html?SortType=total_tranpro_desc`), puis chaque candidat retenu
vérifié via `variants` (prix et ventes confirmés — **l'écart avec le nombre affiché en SERP est net,
voir tableau**).

| Product ID | Titre court | Prix réel (`offer_sale_price`) | Ventes SERP affichées | **Ventes confirmées (`variants`)** | Stock | Élec. déclarée | Confiance | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1005009889580347 | Tondeuse tapis 200 W, vitesse réglable | 40,27 € | 27 vendus | **20** | 14/variante (DE/FR/ES/IT) | 200 W, pas de mention CE dans le titre | B | **Retenu** — le plus proche fonctionnellement de l'actuel (vitesse réglable) |
| 1005007809505585 | Tondeuse à tapis avec guide de cisaillement | 19,19-28,59 € (3 configs) | 55 vendus | **20** | 90-100 (sauf « avec guide » 26-98) | prises EU/US/UK/AU proposées mais **toutes expédiées depuis Chine continentale** — aucune ne part d'un entrepôt EU malgré le libellé « EU Plug » | B | **Retenu**, avec réserve : l'option « EU Plug » ne veut pas dire expédition UE, à vérifier avant tout argument de livraison |
| 1005007430527466 | Ciseaux/tondeuse 240 W | 43,59 € | 77 vendus | **23** | 12 | 240 W, **expédié depuis Allemagne** (entrepôt UE confirmé) | B | **Retenu** — seul candidat avec une expédition UE confirmée par les données |
| 1005008329284062 | Ciseaux électriques 380 W | 44,99-46,79 € | 308 vendus | **104** (meilleur vendeur confirmé du lot) | **1-2 seulement** | 380 W | B | **Rejeté** — stock quasi nul, rupture immédiate probable |
| 1005008329216525 | Ciseaux électriques 200 W sans fil | 40,59-43,19 € | 53 vendus | **26** | **1 chaque variante** | 200 W | B | **Rejeté** — stock quasi nul |
| 1005006294534210 | Tondeuse 380 W haute puissance | 42,39 € (SERP) | 900 vendus | **non vérifiable** — l'appel `variants` a échoué (`IOPUpstreamError`) | inconnu | 380 W | **C** (titre/SERP seuls, rien de confirmé) | **Rejeté en l'état** — aucun chiffre confirmé à la source, à retester plus tard si besoin |

### 2c. Sourcing — Ciseaux électriques de sculpture (actuel : 299 €, 0 en stock)

Même méthode. Écart de prix massif à signaler : **tous les candidats trouvés sont entre 19 € et 52 €**,
loin des 299 € actuels (prix calé sur le concurrent letufting.fr à 320 €, en rupture — donc marge
confortable si le sourcing tient, mais à confirmer que le produit livré justifie le même
positionnement premium).

| Product ID | Titre court | Prix réel | Ventes SERP | **Ventes confirmées** | Stock | Élec. déclarée | Confiance | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1005005972440926 | Ciseaux électriques 200 W, 100-240V | 45,79-55,39 € | 491 vendus | **203** (meilleur volume confirmé) | 2-10 | 200 W, 100-240V (double tension) | B | **Retenu** |
| 1005011898820067 | ONEVAN 800 W sans fil, batterie Makita 18V | 41,39-51,69 € | — | **30** | 0 (« sans batterie ») à 5 | 800 W — le plus puissant, positionnement le plus proche du haut de gamme actuel | B, **expédié depuis Allemagne** (seul candidat ciseaux avec UE confirmée) | **Retenu** — meilleur candidat pour tenir un prix premium |
| 1005008046610589 | Ciseaux électriques 200 W, 110-220V | 43,79-50,99 € | 349 vendus | **133** | **1-2** | 200 W | B | **Rejeté** — stock quasi nul |
| 1005009504578391 | Ciseaux 4V USB rechargeables, cuir/tissu | 18,89-21,99 € | 363 vendus | **219** (le plus vendu du lot) | 1-17 (inégal) | 4V, batterie USB | B | **Rejeté comme équivalent direct** — catégorie différente (petits ciseaux de couture rechargeables, pas un outil de sculpture de tapis) ; à garder en tête comme produit d'appel bas de gamme si Hakim veut diversifier, pas comme remplacement |

### 2d. Ce qui manque pour la conformité électrique (relevé, non tranché)

- **Aucune mention CE, GS ou RoHS visible dans les titres ou les propriétés de variante** des 8
  candidats retenus. Je n'ai pas pu ouvrir les pages produit AliExpress (mur anti-bot du navigateur
  intégré, limite déjà documentée) pour vérifier une mention CE dans la description ou les photos —
  **c'est un vrai manque**, à combler par Hakim ou par un accès DSers/AliExpress direct.
  Pour rappel : une mention CE affichée par un vendeur n'est de toute façon qu'une déclaration du
  vendeur, pas une preuve — je ne l'aurais pas validée même si je l'avais trouvée.
- Tension : les candidats tondeuse annoncent 110-220V ou 100-240V selon le produit (double tension,
  compatible secteur FR) ; wattages déclarés 200-800 W selon le modèle.
- Prise : options EU/US/UK/AU disponibles chez plusieurs vendeurs, **mais « EU Plug » ne garantit pas
  une expédition depuis un entrepôt UE** (cas confirmé sur 1005007809505585 — toutes les configs
  partent de Chine continentale malgré le libellé).
- Seuls deux candidats sur les 8 retenus ont une expédition UE confirmée par les données
  (`1005007430527466` depuis l'Allemagne pour la tondeuse, `1005011898820067` depuis l'Allemagne
  pour les ciseaux) — un point utile si Hakim veut argumenter un délai/origine d'expédition auprès
  du fournisseur ou dans la fiche.

---

## 3. Fils — plan de découpage proposé, exécution non lancée

**Lecture de la fiche existante.** `fil-acrylique-tufting` (« Fil acrylique en cône pour tufting »,
12,90 € toutes variantes, option unique « Couleur ») compte **86 variantes**. Chaque variante a sa
propre image de swatch (vérifié : `variants[].image` non nul sur toutes, et contrôle visuel sur
« 22 Noir » → l'image montre bien un fil noir) — donc pas de problème d'image manquante côté source.

**Ce qui bloque une exécution directe :**
- **86 coloris**, ce qui ferait passer le catalogue de 23 à 109 fiches produit — une expansion
  disproportionnée sans arbitrage préalable.
- **19 variantes sur 86 (22 %) n'ont pas de nom de couleur français** — juste un code numérique
  (« 98 », « 97 », « 100 », « 85 », « 55 », « 19 », « 10 »...). Impossible d'en tirer un titre de
  fiche propre sans un travail de nommage préalable (comparer au nuancier fournisseur, comme le
  notait déjà le journal du 22/07 sur les traductions à contrôler).
- Le stock affiché par variante (20 000 à 26 000 unités chacune, 2,17 million au total sur la fiche)
  est manifestement une valeur de remplissage DSers, pas un stock réel — sans incidence sur le plan
  de découpage, mais à garder en tête si le flux Shopping s'appuie sur ces chiffres.

**Conformément à la consigne (« en cas de doute, tu t'arrêtes au plan »), je m'arrête ici.** Voici
trois options, avec ma recommandation :

- **Option A — découpage intégral (86 fiches).** Écartée : disproportionnée et bloquée par les 19
  variantes sans nom tant qu'elles ne sont pas nommées.
- **Option B — regroupement par famille de couleur (~8-10 fiches).** Une fiche par famille (Rose,
  Vert, Bleu, Gris/Neutre, Rouge/Bordeaux, Jaune/Orange, Blanc/Écru, Multicolore/Spéciaux), chaque
  fiche gardant les nuances de la famille en variantes. Cure le squelette de la collection et une
  bonne partie du bénéfice SEO couleur, sans multiplier les fiches à l'infini. Nécessite de fixer les
  frontières de regroupement et de traiter les 19 variantes sans nom (les rattacher à une famille au
  jugé, ou les excimer du découpage).
- **Option C (recommandation) — découpage curaté sur les coloris les plus probables en recherche
  (15-20 fiches).** Une fiche dédiée pour chaque coloris à nom clair et vraisemblablement recherché
  seul (Noir, Blanc, Rose clair, Bleu marine, Vert foncé, Bordeaux, Camel, Rouge, Violet, Jaune,
  Orange, Gris, Kaki, Indigo, Caramel, Multicolore...), le reste (~66-70 nuances proches ou sans nom)
  restant dans la fiche actuelle multi-variantes comme catalogue élargi. Meilleur rapport
  bénéfice/effort : capture les recherches couleur qui comptent sans exploser le catalogue ni buter
  sur les 19 variantes non nommées.

Exemple de titres/handles si Option C validée : « Fil acrylique tufting — Noir » /
`fil-acrylique-tufting-noir`, « Fil acrylique tufting — Rose clair » /
`fil-acrylique-tufting-rose-clair`, etc. Prix identique (12,90 €), une variante couleur unique,
image issue du swatch existant (déjà disponible et correcte pour ces coloris), rattachement à la
collection « Fils », fiche d'origine conservée le temps de la validation puis à requalifier en
« autres coloris » (Hakim tranchera si elle reste en vente parallèle ou devient une fiche résiduelle
uniquement listée depuis les fiches individuelles).

**Aucune fiche n'a été créée.** J'attends l'arbitrage de Hakim sur l'option et la liste des coloris
avant toute exécution.

---

## 4. Relevé des images (23 produits)

Comparaison faite par URL de média sur les 23 fiches (image produit + swatch de variante) :
**aucune image identique n'est réutilisée entre deux fiches différentes** — pas de doublon
inter-produits détecté.

Contrôle visuel (capture d'écran directe des fichiers CDN) sur les cas suspects :

| Produit | Média concerné | Problème constaté | Gravité |
|---|---|---|---|
| Pièces détachées pour tufting gun | Image 1 (`S600100f...N.webp`) | **Collage** : 8 pièces détachées différentes assemblées dans une grille — motif de refus GMC direct | **Haute** |
| Pièces détachées pour tufting gun | Les 12 images du produit | Toutes en nom de fichier brut fournisseur (hash AliExpress, aucune n'est passée par le pipeline de retouche Codex comme le reste du catalogue) ; au moins une image (n°2) montre un pistolet démonté à nu, câbles apparents, dans un cadre atelier non professionnel | Moyenne — cohérent avec « pièces détachées » mais à retravailler avant Shopping |
| Brosse de finition | Variantes Bleu/Rouge/Vert | **Aucune image de variante propre** — les 3 couleurs partagent l'image produit par défaut, qui montre uniquement le bleu. Un acheteur qui choisit Rouge ou Vert voit la mauvaise couleur. | Moyenne |
| Enfile-laine pour tufting gun (lot de 5) | Variantes Jaune/Rouge/Noir | **Aucune image de variante propre** — l'image par défaut montre un assortiment de 5 couleurs mélangées (rouge/bleu/rose/jaune/noir), qui ne correspond à aucune des 3 variantes vendues (chacune un lot mono-couleur). | Moyenne |
| Miroir acrylique pour tufting | Variantes Doré foncé/Argenté/Rouge/Doré clair (× 8 tailles) | Aucune image de variante propre ; les images produit montrent une mise en scène composée (plusieurs couleurs de miroir ensemble) plutôt qu'un visuel par couleur — moins trompeur que les deux cas ci-dessus (la mise en scène ne prétend pas représenter une seule couleur) mais toujours pas d'image dédiée par variante | Basse-moyenne |
| Fil acrylique en cône pour tufting | 86 swatchs de variante | Contrôlés : chaque swatch correspond à sa couleur (vérifié sur « 22 Noir »), aucun problème détecté | — (conforme) |
| Reste du catalogue (18 fiches restantes, y compris kit, tufting gun 2-en-1, toiles, ciseaux/tondeuse en cause) | Images principales | Noms de fichiers descriptifs, cohérents avec le pipeline de retouche mentionné dans `project-state.md` ; échantillon contrôlé (Miroir acrylique, Enfile-laine, Brosse, Tissu de finition ×2) : mise en scène composée, pas de texte incrusté détecté sur les images ouvertes | — (échantillon conforme, pas un contrôle exhaustif image par image) |

**Non exhaustif** : je n'ai pas ouvert individuellement les ~140 images du catalogue une par une — le
tri s'est fait sur le nom de fichier (brut vs. retouché) pour cibler les cas à risque, puis contrôle
visuel des cas ciblés et d'un échantillon du reste. Voir section 7.

---

## 5. Vitesse

**Mesure obtenue via PageSpeed Insights (Lighthouse mobile, Moto G Power simulé, 4G lente), le
16/08/2026 à 01:25 — mesure publique, pas le rapport interne Shopify.**

| Catégorie | Score |
|---|---|
| **Performances** | **57 / 100** |
| Accessibilité | 90 / 100 |
| Bonnes pratiques | 54 / 100 |
| SEO | 100 / 100 |

Détail performance : FCP 2,1 s · **LCP 6,8 s** (élevé) · TBT 480 ms · CLS 0,069 · Speed Index 5,6 s.
Poids total de page : **15 327 Kio**. Pistes d'économie identifiées par l'outil : requêtes
bloquant le rendu (-300 ms), cache (-22 Kio), images (-203 Kio), CSS inutilisé (-137 Kio), JS
inutilisé (-838 Kio).

**57 < 65 : sous le seuil de la checklist.**

**Réserve à connaître : je n'ai pas pu me connecter à l'admin Shopify** (pas de session
authentifiée dans le navigateur, et je n'entre aucun identifiant) pour aller chercher le rapport de
vitesse boutique natif que la checklist GMC vise en premier lieu. PageSpeed Insights est une mesure
publique équivalente (même moteur Lighthouse que celui utilisé en interne par Shopify pour son
propre score), mais la méthodologie exacte et le score du rapport Shopify natif peuvent différer
légèrement. Traiter 57/100 comme un signal fiable de « sous le seuil », pas comme le chiffre exact
qui apparaîtra dans l'admin.

---

## 6. Décisions qui attendent Hakim

1. **Tissu de finition** : dépublier `tissu-de-finition` (doublon probable de
   `tissu-finition-antiderapant`) ou sourcer un nouveau fournisseur si la distinction finition/anti-
   dérapant doit être maintenue.
2. **Tondeuse et ciseaux électriques repassés ACTIVE sans trace documentée** entre le 21/07 (DRAFT,
   garde-fou CE) et aujourd'hui, alors que le kit tondeuse+guide est resté en DRAFT. À documenter
   (si volontaire) ou corriger (si régression) — je n'ai touché aucun des trois statuts.
3. **Sourcing tondeuse/ciseaux** : 3 candidats tondeuse retenus (dont un seul avec expédition UE
   confirmée) et 2 candidats ciseaux retenus (dont un seul avec expédition UE confirmée) — écart de
   prix massif entre l'offre marché (19-52 €) et le prix de vente actuel (89,90 € / 299 €) à
   examiner. Aucune mention CE/GS/RoHS trouvée sur aucun candidat — accès direct au fournisseur
   nécessaire pour lever ce point, comme Hakim l'a indiqué vouloir faire.
4. **Fils** : choisir entre les options A/B/C de découpage (recommandation : option C, 15-20 fiches
   curatées) et fournir/valider la liste des coloris à sortir, avant toute création de fiche.
5. **Images à corriger avant soumission GMC** : le collage sur « Pièces détachées pour tufting gun »
   (motif de refus direct), et les 2 cas de variante sans image propre qui induisent en erreur
   (Brosse de finition, Enfile-laine).
6. **Vitesse sous le seuil** (57 < 65) — le poids de page (15,3 Mo) et le JS/CSS inutilisé sont les
   leviers signalés par l'outil ; ce chantier n'a pas été creusé plus loin (hors périmètre de cette
   session).

---

## 7. Ce que je n'ai pas pu vérifier

- **Pages produit AliExpress individuelles** des candidats sourcés (tondeuse, ciseaux) : mur anti-bot
  du navigateur intégré, limite déjà connue. Confiance plafonnée à **B** (SERP JSON + API
  `variants`), pas de mention CE/GS/RoHS vérifiable en description ou sur les photos produit.
- **Fret et délai France via `exact`** pour les candidats tondeuse/ciseaux : la commande a
  systématiquement renvoyé `qualification_refused` (« No SKU matches exactly ») malgré plusieurs
  formats de `--property` essayés (chaîne unique, propriétés séparées, avec/sans destination) — je
  n'ai pas insisté au-delà de ces essais, conformément à la consigne de ne pas s'acharner sur un
  outil bloqué. Le fret/délai réel de ces candidats reste donc à confirmer autrement (DSers, ou
  contact fournisseur puisque Hakim gère cette partie directement).
- **Rapport de vitesse Shopify natif** (admin) : pas de session admin authentifiée disponible, et je
  n'entre aucun identifiant. Mesure de remplacement : PageSpeed Insights public (section 5).
- **~140 images du catalogue une par une** : contrôle ciblé par nom de fichier (brut vs. retouché)
  puis échantillon visuel, pas une revue exhaustive image par image. Voir section 4.
- **Icônes de paiement vs moyens réellement actifs**, **cohérence des délais annonce/FAQ/policy**,
  **appel vocal du numéro de téléphone** : hors périmètre de cette session, déjà signalés comme
  restants dans `AUDIT-GMC-2026-08-16.md`.
- **Origine réelle d'expédition des produits déjà en vente** (toile primaire confirmée UE, gun/kit
  non documentés) : non repris dans cette session, réserve déjà notée dans l'audit du 16/08.

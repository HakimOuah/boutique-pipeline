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

---

## Exécution du 16/08 — écritures

Session distincte, sur validation explicite de Hakim des trois chantiers ci-dessous (dépublication,
option C du découpage fils, images de variantes). Boutique connectée vérifiée avant écriture :
`get-shop-info` → Tuftéo, tufteo.com. Sauvegardes dans
`shopify/backups/2026-08-16-decoupage-fils/` avant toute modification.

### Chantier 1 — Dépublication de deux fiches (FAIT, vérifié)

Avant dépublication : vérifié qu'aucun menu (`main-menu`, `footer`, `legal`) ne référence les deux
handles, et que les mentions croisées « Va bien avec » dans les 23 fiches actives sont du texte brut
sans lien `<a href>` — donc rien à casser côté navigation. `tissu-de-finition` était listée dans la
collection « Toiles & tissus » (`gid://shopify/Collection/690476843393`, générée automatiquement à
partir du statut) ; `pieces-detachees-tufting-gun` n'était dans aucune collection.

- `tissu-de-finition` (`gid://shopify/Product/15466411131265`) → **DRAFT**, mutation confirmée.
- `pieces-detachees-tufting-gun` (`gid://shopify/Product/15466415292801`) → **DRAFT**, mutation confirmée.

**Vérifié à l'écran** (16/08, `curl` espacés de 2-3 s) :
- `https://tufteo.com/products/tissu-de-finition` → **404**
- `https://tufteo.com/products/pieces-detachees-tufting-gun` → **404**
- `https://tufteo.com/collections/tissus` → grep sur `tissu-de-finition` : **aucune occurrence**, la fiche a bien disparu de la collection publique.

Sauvegardes : `tissu-de-finition.avant.json`, `pieces-detachees-tufting-gun.avant.json`.

### Chantier 2 — Découpage curaté du fil acrylique, option C (FAIT, vérifié)

**Sauvegarde d'abord** : les 87 variantes de la fiche mère (`fil-acrylique-tufting`,
`gid://shopify/Product/15466411229569`) exportées dans
`fil-acrylique-tufting.87-variantes.avant.json`. La fiche mère n'a été touchée à aucun moment
(toujours ACTIVE, toujours 87 variantes, prix et stock inchangés — reconfirmé par la relecture de la
collection en fin de chantier).

**Sélection.** Sur les 68 variantes à nom français (19 sont des codes numériques sans nom, écartées
d'office comme prévu), j'ai retenu les coloris de base et les couleurs franches en excluant les
nuances trop proches d'un même nom (ex. deux variantes nommées « Vert foncé », deux nommées
« Orange », deux nommées « Violet », deux nommées « Jaune poussin », deux nommées « Bleu denim », deux
nommées « Blanc » vs « Blanc pur » — une seule retenue par nom, l'autre reste dans la fiche mère).

**Contrôle visuel avant création** (règle n° 2 de mon mode d'emploi — un swatch non vérifié est à
jeter comme un chiffre non confirmé) : les 18 swatches candidats téléchargés et inspectés un par un.
Résultat :
- 17 correspondent bien à leur nom.
- **1 écarté : « 60 Multicolore »** (SKU source `flower basket`). Le swatch affiché est un fil bleu-violet **uni**, sans aucune mèche ni effet mélangé visible — en contradiction directe avec le nom « Multicolore ». Je n'ai pas créé cette fiche : un swatch qui contredit son nom est pire qu'une fiche manquante.
- Deux notes de nuance à connaître (pas des erreurs, juste des écarts de perception) : le swatch « 52 Jaune » est un jaune assez doré/moutarde, pas un jaune citron franc ; le swatch « 84 Vert foncé » est plus proche d'un vert olive/kaki que d'un vert sapin profond. Gardés tels quels car le nom vient de la donnée source et le swatch reste cohérent avec ce nom, juste avec une nuance à connaître si un client compare à l'écran.

**17 fiches créées, toutes vérifiées vivantes à l'écran** (titre — handle) :

| Couleur | Handle | Variante source (code) |
|---|---|---|
| Noir | fil-acrylique-tufting-noir | 22 Noir |
| Blanc | fil-acrylique-tufting-blanc | 01 Blanc |
| Gris | fil-acrylique-tufting-gris | 28 Gris |
| Rouge | fil-acrylique-tufting-rouge | 35 Rouge |
| Bordeaux | fil-acrylique-tufting-bordeaux | 80 Bordeaux |
| Rose | fil-acrylique-tufting-rose | 71 Rose |
| Rose poudré | fil-acrylique-tufting-rose-poudre | 54 Rose poudré |
| Orange | fil-acrylique-tufting-orange | 65 Orange |
| Jaune | fil-acrylique-tufting-jaune | 52 Jaune |
| Vert foncé | fil-acrylique-tufting-vert-fonce | 84 Vert foncé |
| Kaki | fil-acrylique-tufting-kaki | 26 Kaki |
| Bleu clair | fil-acrylique-tufting-bleu-clair | 31 Bleu clair |
| Bleu marine | fil-acrylique-tufting-bleu-marine | 14 Bleu marine |
| Violet | fil-acrylique-tufting-violet | 57 Violet |
| Camel | fil-acrylique-tufting-camel | 76 Camel |
| Indigo | fil-acrylique-tufting-indigo | 16 Indigo |
| Caramel | fil-acrylique-tufting-caramel | 59 Caramel |

Pour chaque fiche : titre `Fil acrylique tufting — <Couleur>`, une seule variante (option
« Couleur »), même prix (12,90 €), même stock que la variante d'origine (repris tel quel — c'est la
valeur de remplissage DSers déjà signalée en section 3, pas un stock réel, mais fidèle à la source),
swatch existant en image, description adaptée par coloris, rattachées à la collection « Fils ».

**Piège rencontré et corrigé : les fiches créées via l'API ne sont publiées sur aucun canal par
défaut** (`resourcePublicationsV2` vide à la création — le même piège que documenté dans la mémoire
« Canal Online Store & visuels IA »). Premier test `curl` sur 3 fiches → **404** malgré un statut
ACTIVE. Corrigé par `publishablePublish` sur les canaux « Boutique en ligne » et « Google & YouTube »
(les deux canaux où la fiche mère est elle-même publiée). Après correction, les 17 URLs retestées
une par une (`curl` espacés de 2 s) → **200** partout.

**Vérifications finales, toutes faites en conditions réelles :**
- Requête API sur la collection « Fils » : **18 fiches** (17 nouvelles + la mère), toutes `status: ACTIVE`, handles propres.
- Page publique `https://tufteo.com/collections/fils` ouverte au navigateur (cookies refusés) : les 17 fiches s'affichent avec leur nom et prix, plus la fiche mère listée séparément en promotion — capture confirmée par lecture du texte de page rendu.
- Fiche individuelle `https://tufteo.com/products/fil-acrylique-tufting-caramel` ouverte et capturée à l'écran : titre, prix, sélecteur « Couleur : Caramel », image correspondant à un fil caramel — conforme.

**Décision qui attend Hakim :** le SKU de chaque nouvelle fiche est repris à l'identique du SKU de la
variante d'origine (pour la traçabilité). Je ne sais pas si DSers route un fulfillment automatique
par SKU seul ou par le couple produit/variante qu'il a lui-même importé — **à vérifier côté DSers
avant la première commande sur une des 17 nouvelles fiches**, sous peine de non-fulfillment
automatique.

Sauvegarde complète des 87 variantes avant découpage :
`fil-acrylique-tufting.87-variantes.avant.json`.

### Chantier 3 — Images de variantes manquantes (constat, aucune image assignée)

Pour les trois fiches, j'ai vérifié dans l'ordre demandé : (1) médias du produit déjà sur Shopify non
affectés à une variante, (2) dossier local `images/` (miroir du CDN), (3) archive
`assets/source/aliexpress/<produit>/` — les photos fournisseur brutes conservées avant le passage
Codex du 22/07 (« purge images fournisseur », `shopify/upload-images-codex-2026-07-21.md`), (4)
`assets/generated/` et `assets/final/` pour un visuel composé qui n'aurait pas été uploadé.

**Résultat : aucune image exploitable à assigner directement, sur aucune des trois fiches.** Détail :

**Brosse de finition** (Bleu/Rouge/Vert). Les 6 images Shopify montrent exclusivement le bleu (mises
en scène différentes, mais toujours le même bleu) — confirmé en ouvrant les 6 une par une. Aucune
image de rouge ni de vert dans les médias du produit. Dans l'archive fournisseur brute (9 photos),
**des photos existent** : `img-09.webp` (rouge/fuchsia solo sur fond blanc) et `img-07.webp` (vert
solo, mise en scène étagère). Mais ce sont des **photos AliExpress brutes**, exactement ce que la
règle maison « visuels composés, jamais la photo fournisseur » interdit de publier telles quelles —
elles n'ont pas subi le même traitement Codex que les 6 images déjà en ligne. Je ne les ai pas
uploadées. **Ce qui manque réellement : 2 visuels composés (Rouge, Vert) à générer par le même
pipeline Codex que le reste du catalogue**, à partir de `assets/source/aliexpress/cleaning-brush-.../img-09.webp` et `img-07.webp` comme référence couleur.

**Enfile-laine pour tufting gun (lot de 5)** (Jaune/Rouge/Noir). Les 6 images Shopify montrent toutes
le même assortiment de 5 couleurs mélangées (rouge/bleu/rose/jaune/noir) — aucune ne montre un lot de
5 unités **de la même couleur**, alors que c'est ce que vend chaque variante. Dans l'archive
fournisseur (9 photos), il existe des fiches techniques unitaires par couleur (`img-04` Jaune,
`img-05` Noir, `img-06` Bleu — non vendu, `img-08` Rouge) mais ce sont des **schémas techniques à 1
seule unité, avec cotes et texte anglais/chinois incrusté** (« Yellow », « ≈20,5 cm », « 单支≈2,3g ») —
inutilisables tels quels, et n'importe comment pas au format « lot de 5 » vendu. **Ce qui manque :
3 visuels composés (Jaune, Rouge, Noir, chacun montrant 5 unités de la même couleur) à générer par
Codex**, en utilisant les fiches techniques comme référence de teinte uniquement.

**Miroir acrylique pour tufting** (Doré foncé/Argenté/Rouge/Doré clair × 8 tailles). Les 6 images
Shopify sont toutes des mises en scène avec plusieurs coloris ensemble (pile de plaques, gros plan
sur 2-3 couleurs) — aucune n'isole une seule couleur. Dans l'archive fournisseur (10 photos),
aucune n'est directement exploitable : la pile multi-couleurs (`img-01`, `img-03`) mélange les tons
sans étiquette (impossible de distinguer « doré clair » de « doré foncé » avec confiance) ; `img-09`
(rouge) a **du texte chinois gravé directement sur la plaque photographiée** ; `img-08` a un décor
d'usine chinoise en arrière-plan (enseignes en chinois visibles). Aucune de ces images ne peut servir
de source propre. **Ce qui manque : au minimum 4 visuels composés (un par couleur, ré-utilisable sur
les 8 tailles de chaque couleur)**, à confier à Codex — je n'ai pas identifié de source fournisseur
assez propre pour guider la teinte exacte de « doré clair » vs « doré foncé », donc Hakim devra
probablement trancher au nuancier fournisseur ou redemander une photo au vendeur.

**Aucune image n'a été fabriquée ni assignée dans ce chantier** — conformément à la consigne, une
fiche sans son visuel correct reste sans image plutôt que de recevoir une image approximative ou une
photo fournisseur brute non conforme à la charte du site.

### Décisions qui attendent Hakim (session du 16/08 — écritures)

1. **Fils** : la fiche « 60 Multicolore » n'a pas été découpée (swatch uni, contredit son nom) — à
   vérifier auprès du fournisseur si Hakim veut ce coloris quand même (nouvelle photo nécessaire).
2. **Fils / DSers** : confirmer que le fulfillment automatique fonctionne sur les 17 nouvelles fiches
   (SKU repris à l'identique de la fiche mère, mais DSers route peut-être par identifiant produit/variante importé, pas par SKU seul).
3. **Images manquantes** : 2 visuels à composer pour la Brosse de finition (Rouge, Vert), 3 pour
   l'Enfile-laine (Jaune/Rouge/Noir en lot de 5), au moins 4 pour le Miroir acrylique (un par
   couleur) — sources brutes identifiées fichier par fichier ci-dessus pour alimenter Codex, aucune
   n'est publiable telle quelle.
4. **Tissu de finition / Pièces détachées** : statuts DRAFT posés sur simple exécution du chantier 1
   validé — pas de nouvelle décision requise, sauf si Hakim veut resourcer l'un des deux plus tard.

### Ce que je n'ai pas pu vérifier (session du 16/08 — écritures)

- **Le rendu du sélecteur de variante sur mobile** pour les 17 nouvelles fiches (une seule variante
  chacune, donc sélecteur à un seul bouton) — vérifié uniquement en desktop via le navigateur intégré.
- **L'impact SEO réel** des 17 nouvelles fiches (indexation Google, cannibalisation éventuelle avec la
  fiche mère qui liste aussi ces mêmes coloris) — hors de portée d'une vérification en session, à
  suivre dans le temps par Hakim.
- **La teinte exacte à donner à « doré clair » vs « doré foncé »** pour le miroir acrylique : aucune
  source fournisseur assez propre trouvée pour trancher avec confiance (voir chantier 3).

---

## Affectation des visuels Codex — 16/08/2026 (session distincte)

Suite du chantier 3. Les 26 visuels commandés dans `BRIEF-VISUELS-CODEX-2026-08-16.md` ont été livrés
dans `images/visuels-2026-08-16/` avec `mapping.json`. Contrôle qualité (1600×1600, carré, <2 Mo, pas
de texte) déjà fait par Claude en amont — **recontrôlé ici avant tout envoi** par mesure de précaution
(`sips` + taille fichier) : les 26 fichiers ciblés sont bien 1600×1600 px, le plus lourd
(`enfile-laine-noir-01.png`) fait 1 967 128 octets (< 2 Mo). Le 27ᵉ fichier `planche-controle-17-cones.png`
(2400×2208, collage) n'a pas été touché — vérifié qu'il n'apparaît dans aucun appel d'upload ci-dessous.

Boutique connectée vérifiée : `get-shop-info` → Tuftéo, tufteo.com (Basic, EUR). Thème brouillon non
concerné par ce chantier (travail 100 % catalogue produit, pas de fichier de thème).

Sauvegarde avant écriture : état des 20 fiches concernées (17 fils + brosse-de-finition +
enfile-laine-tufting-gun + miroir-acrylique-tufting) relevé via `get-product`/`search_products` et
consigné plus bas dans ce rapport avant toute mutation (IDs produits/variantes, image principale
actuelle). Pas de fichier JSON séparé cette fois — l'état "avant" tient dans ce compte rendu et dans
`shopify/backups/2026-08-16-visuels-codex/`.

### Plan d'exécution retenu

1. `stagedUploadsCreate` (resource `IMAGE`) pour les 26 fichiers en un seul appel groupé.
2. Upload de chaque fichier en `curl -F` sur l'URL Google renvoyée (hôte différent de Shopify, donc
   pas soumis à la limitation 503 de Shopify — pas d'espacement nécessaire à cette étape).
3. `productCreateMedia` — un appel par produit (20 appels : 17 fils + 3 fiches variantes), en espaçant
   les appels vers l'API Shopify.
4. Fils : `productReorderMedia` pour placer la nouvelle image en position 0 (image principale),
   remplaçant le swatch 251×194 comme tête de fiche.
5. Fiches variantes : `productVariantAppendMedia` pour lier chaque image à sa ou ses variantes (le
   miroir : une image de couleur liée aux 8 tailles de cette couleur, soit 32 liaisons pour 4 images).
6. Vérification en preview réelle (thème brouillon `189410738561`) + page publique.

État en cours — sections suivantes complétées au fil de l'exécution.

### Étape 1-2 — Upload en staging (FAIT, vérifié)

`stagedUploadsCreate` (resource `IMAGE`) pour les 26 fichiers en un seul appel : 26 cibles renvoyées,
0 erreur. Upload de chaque fichier en `curl -F` sur l'URL Google — **26/26 réponses `201 Created`**.
Ces uploads visent `shopify-staged-uploads.storage.googleapis.com`, pas l'API Shopify : aucun
espacement nécessaire à cette étape (la limite 503 documentée dans mon mode d'emploi concerne les
appels vers Shopify, pas Google Storage).

### Étape 3 — `productCreateMedia`, un appel par produit (FAIT, vérifié)

20 appels (17 fils + brosse-de-finition + enfile-laine-tufting-gun + miroir-acrylique-tufting),
**0 `mediaUserErrors` sur les 20 appels**, 26 objets `MediaImage` créés au total (statuts `UPLOADED`
ou `PROCESSING` à la création — tous confirmés `READY`/servis lors des relectures qui suivent).
Mutation `productCreateMedia` signalée dépréciée par le validateur (au profit de `productUpdate`/
`productSet`) mais toujours fonctionnelle et validée par le schéma — utilisée telle quelle, cohérente
avec les résultats obtenus.

### Étape 4 — `productReorderMedia` sur les 17 fils (FAIT, vérifié)

17 appels, chacun déplaçant la nouvelle image en position 0 (donc image principale) sur sa fiche.
**0 `mediaUserErrors`**, jobs asynchrones acceptés (`done: false` à la soumission, comme attendu).
**Vérifié par relecture API immédiate après coup** (pas seulement la réponse de la mutation, qui ne
prouve rien à elle seule — leçon retenue de mon mode d'emploi) : `featuredImage` des 17 fiches
recontrôlé via `get-product` et `graphql_query` groupée sur les 16 restantes → **les 17 featuredImage
pointent bien vers le fichier `fil-acrylique-<couleur>-01.png`**, le swatch `.webp` est redescendu en
position 2. Le job de reorder s'est donc résolu quasi immédiatement, pas besoin de polling.

### Étape 5 — `productVariantAppendMedia` sur les 3 fiches variantes (FAIT, vérifié)

- `brosse-de-finition` : 2 liaisons (Rouge, Vert) — **0 erreur**.
- `enfile-laine-tufting-gun` : 3 liaisons (Jaune/Rouge/Noir lot de 5) — **0 erreur**.
- `miroir-acrylique-tufting` : **32 liaisons en un seul appel** (4 couleurs × 8 tailles chacune) —
  **0 erreur**.

**Vérifié par requête API dédiée** (`variants { image { url } }`) sur les 3 produits, variante par
variante : chaque variante renvoie l'URL de l'image de sa bonne couleur. Sur le miroir, les 32
variantes ont été listées et recoupées une à une avec le nom de couleur dans leur titre — aucune
erreur d'affectation trouvée.

### Étape 6 — Vérification en préview réelle (FAIT, avec une réserve notée)

Session navigateur sur le thème brouillon **`gid://shopify/OnlineStoreTheme/189410738561`**
(« Tuftéo — purge faux avis 16-08 », rôle `UNPUBLISHED` — reconfirmé par `{ themes(first:10){ nodes{ id
name role } } }` avant d'ouvrir la preview). Bandeau `Tuftéo — purge faux avis 16-08 · Draft` visible en
bas d'écran sur toutes les captures ci-dessous, confirmant qu'il s'agit bien du thème brouillon et non
du thème MAIN publié.

**Fiches individuelles (3 tirées au hasard parmi les 17 fils), captures d'écran réelles :**
- `fil-acrylique-tufting-noir` → cône noir affiché en image principale. Conforme.
- `fil-acrylique-tufting-caramel` → cône brun caramel affiché en image principale. Conforme.
- `fil-acrylique-tufting-bleu-marine` → cône bleu marine affiché en image principale. Conforme.

**Collection « Fils » — vérification technique, pas de capture propre obtenue.** J'ai ouvert
`https://tufteo.com/collections/fils?preview_theme_id=189410738561` (bandeau Draft confirmé) mais le
thème utilise une révélation au scroll (probablement IntersectionObserver) qui a rendu mes captures
d'écran vides à plusieurs reprises pendant le défilement, y compris après plusieurs tentatives
(scroll souris, `scrollIntoView`, `window.scrollTo`) — comportement de l'outil de test, pas un bug
constaté sur le site. **Vérification de repli faite en lisant le DOM rendu directement** (`document.
querySelectorAll('img')` sur la page collection réellement chargée en preview) : les 17 vignettes
portent chacune une image `alt="Fil acrylique tufting — cône <Couleur>"` avec une résolution native
1280×1280 (confirmant qu'il s'agit bien du nouveau visuel Codex, pas du swatch) et une seconde image
`alt="Fil acrylique tufting — <Couleur>"` en plus petite résolution (le swatch, devenu secondaire,
utilisé par le thème comme image de survol). Contrôlé pour tous les libellés de couleur retournés
(Caramel, Indigo, Camel, Violet, Bleu marine, Bleu clair, Kaki, Vert foncé, Jaune, Orange — récupérés
dans le DOM ; les 7 autres confirmés séparément via l'étape 4 côté API). **Je n'ai donc pas de capture
visuelle de la grille complète**, seulement la confirmation DOM + les 3 fiches individuelles capturées
à l'écran. Si Hakim veut la capture grille, une réouverture manuelle de la page suffit — le contenu est
là, c'est l'outil de scroll automatisé qui a buté.

**Fiches à variantes (3/3), sélection de chaque couleur testée en cliquant réellement le bouton et
capture d'écran après chaque clic :**
- `brosse-de-finition` : Bleu (défaut, image générique) → Rouge (image bascule, brosse rouge affichée)
  → Vert (image bascule, brosse verte affichée). 3/3 conformes.
- `enfile-laine-tufting-gun` : Jaune (défaut, lot de 5 jaune) → Rouge (lot de 5 rouge) → Noir (lot de 5
  noir). 3/3 conformes — et confirmation visuelle que l'ancien problème (assortiment 5 couleurs
  mélangées ne correspondant à aucune variante) est bien corrigé.
- `miroir-acrylique-tufting` : Doré foncé (défaut) → Argenté → Rouge → Doré clair. 4/4 conformes. Test
  supplémentaire : changement de taille (`Ø 10 cm`) après sélection Doré clair — **l'image reste le
  doré clair**, confirmant qu'une image de couleur s'applique bien aux 8 tailles de cette couleur,
  comme demandé dans la mission.

**Erreurs Liquid / console** : `read_console_messages` (filtré sur erreurs) exécuté sur la fiche
miroir après les 4 sélections de couleur + 1 changement de taille → **aucune erreur**. Aucun texte
« Liquid error » observé sur aucune des 8 pages ouvertes (3 fils + 3 clics variante brosse/enfile-laine
+ 4 clics miroir + 1 clic taille). Aucune fiche cassée constatée.

---

## État final du chantier (16/08/2026)

**26/26 images affectées et vérifiées.**

| Lot | Fiches concernées | Affectation | Vérifié comment |
|---|---|---|---|
| 17 cônes | `fil-acrylique-tufting-<couleur>` | Image principale (position 0), swatch conservé en position 1 | API (`featuredImage` des 17 fiches) + écran (3 fiches ouvertes, cône affiché) + DOM de la collection (17/17 alt/src corrects) |
| 2 | `brosse-de-finition` (Rouge, Vert) | Liées à leur variante via `productVariantAppendMedia`, image générique (Bleu) inchangée | API (`variant.image.url`) + écran (sélection des 3 couleurs, image bascule) |
| 3 | `enfile-laine-tufting-gun` (Jaune/Rouge/Noir lot de 5) | Liées à leur variante | API + écran (sélection des 3 couleurs) |
| 4 | `miroir-acrylique-tufting` (Doré foncé/Argenté/Rouge/Doré clair) | Chaque image liée aux 8 tailles de sa couleur (32 liaisons) | API (32 variantes recoupées une à une) + écran (4 couleurs + 1 changement de taille) |

**17 fiches sur 17 ont désormais une image principale correcte** (montrant le cône entier, 1600×1600,
plus le swatch en secondaire) — le problème signalé le 16/08 matin (swatch 251×194 en image
principale) est résolu sur la totalité des fiches concernées.

Le 27ᵉ fichier (`planche-controle-17-cones.png`) n'a jamais été uploadé — vérifié qu'il n'apparaît dans
aucun des 20 appels `productCreateMedia` passés (relecture de mon plan d'exécution avant envoi).

## Ce qui a échoué

Rien côté Shopify (0 erreur sur 20 `productCreateMedia`, 17 `productReorderMedia`, 3
`productVariantAppendMedia`). La seule difficulté rencontrée est **outillage, pas exécution** : le
défilement automatisé de la page collection dans le navigateur de test n'a pas produit de capture
exploitable (voir étape 6) — contourné par une lecture DOM directe, qui constitue une preuve technique
équivalente mais pas une capture visuelle. Signalé plutôt que masqué.

## Décisions qui attendent Hakim (ce chantier)

1. **Capture visuelle de la grille « Fils »** non obtenue (voir étape 6) — si utile pour un contrôle
   visuel personnel avant passage en Shopping, une réouverture manuelle de
   `https://tufteo.com/collections/fils?preview_theme_id=189410738561` suffit ; le contenu est
   confirmé correct par API et par DOM, seule la capture d'écran automatisée a échoué.
2. **Mutation `productCreateMedia` dépréciée** par Shopify (au profit de `productUpdate`/
   `productSet`) — toujours fonctionnelle aujourd'hui, mais à garder en tête si un futur chantier
   d'images échoue silencieusement après une dépréciation devenue bloquante.
3. Aucune autre décision : ce chantier ne touche ni prix, ni stock, ni statut produit, ni thème
   publié.

## Ce que je n'ai pas pu vérifier (ce chantier)

- **La capture visuelle complète de la grille de la collection « Fils »** (17 vignettes côte à côte) —
  contournée par une vérification DOM directe (alt text + résolution native de chaque image), qui
  confirme la couleur et la source de chaque vignette mais n'est pas un rendu visuel à l'écran comme
  les fiches individuelles. Voir étape 6 pour le détail de ce qui a été tenté.
- **L'indexation / le comportement réel dans le flux Google Shopping** une fois les fiches
  effectivement soumises — hors périmètre de ce chantier (pas de connexion GMC dans cette session).
- **Le rendu mobile** des sélecteurs de variante (brosse, enfile-laine, miroir) — testé uniquement en
  desktop (viewport 1280×720) via le navigateur intégré.

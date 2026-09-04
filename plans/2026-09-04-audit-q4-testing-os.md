---
type: plan
date: 2026-09-04
titre: "Audit du planning hebdomadaire « OH Ventures — Q4 Testing OS » et proposition v2"
source: base Notion 6c63437c689b40029eaba3b654d07284 (21 tâches, vue « Par jour »), relue le 04/09/2026
statut: proposition — décisions Hakim listées en §6, rien n'est appliqué
---

# Audit du « Q4 Testing OS » et proposition de semaine v2

Le planning Notion décrit une semaine-sprint : lundi on découvre 30 à 50 idées et on en sort
un produit A, un produit B et un backup ; mardi on construit A ; mercredi on lance A en Search
et on construit B ; jeudi on lit les premiers signaux de A ; vendredi on lance B, comité, Mac
Fund ; le week-end Hermes prépare le lundi. Objectif implicite : **deux tests Search par
semaine**, Shopping ensuite pour ce qui marche.

L'ambition est la bonne, et une bonne partie du contenu est déjà alignée avec la méthode
maison. Mais le calendrier, lui, suppose trois choses que le repo contredit : que la découverte
rende deux GO par semaine, qu'un test puisse être lancé deux jours après le GO, et qu'un test
lancé mercredi ait quelque chose à dire vendredi.

## 1. Ce qui va

- **L'ordre des phases est le nôtre.** Discovery → Fast Gate (mesure DataForSEO avant filtre)
  → Deep Gate (concurrence, sourcing, économie) → comité contradictoire → build → QA → launch →
  learning. C'est la chaîne `/recherche-produit` et le rôle `@oh-contradicteur`.
- **Persona avant copy.** La tâche « intelligence client » précède le copywriting : c'est la
  porte bloquante de `persona-obligatoire-copywriting`.
- **Break-even CPA calculé avant le lancement** (tâche « offre et unit economics »). C'est ce
  qui manquait aux quatre premières boutiques.
- **Search pour le produit pur, Shopping pour l'univers.** Conforme à la règle Search ≠ Shopping
  du 19/08.
- **« Ne pas conclure winner/loser trop tôt »** et « ne pas modifier le scoring sur un seul
  échec » : les deux leçons des experts du 16/08 sont écrites dans les tâches.
- **Time-box du branding** (1 h) et gate Hakim à 20-30 min : bon réflexe pour une boutique de
  test, à condition de le dire explicitement (voir §6, décision e).
- **Mac Fund sur la marge nette, jamais le CA.** Rien à redire.
- **Backlog du week-end par Hermes** : c'est la « recherche continue » décidée le 23/08, et la
  règle des branches `agents/<mission>-<date>` s'applique.

## 2. Ce qui ne va pas

### 2.1 Le lundi demande un rendement que la chaîne n'a jamais produit

Le planning attend 30-50 idées → 5 → 3 → A, B et backup **en une journée**. Voici ce que la
chaîne a réellement rendu depuis qu'elle tourne sur DataForSEO :

| Passe | Date | Entrée | PASS_PREQUALIFICATION | GO_FINAL |
|---|---|---:|---:|---:|
| Phase 3 produit pur Q4 | 01/09 | 4 candidats | 0 | 0 |
| Deux tests de découverte | 03/09 | 12 idées | 0 | 0 |
| Qualification approfondie | 03-04/09 | 9 pistes | 0 (3 REVIEW) | 0 (1 NO_GO) |
| Univers poufs | 03/09 | 1 dossier | 0 | 0 |

Zéro PASS en une semaine de travail intensif. Le goulot n'est pas le build, c'est la
**découverte de candidats qui passent**. Un planning qui met le build au centre de la semaine
optimise le mauvais étage : les mardis-mercredis seront vides tant que le lundi ne fournit pas.

### 2.2 Le lancement mercredi viole la porte échantillon

Décision du 23/08 (`PRODUCT-RESEARCH-CRITERIA.md` §0.5) : la commande test est passée par Hakim
juste après `GO_FINAL`, latence **1 à 3 semaines**, et `SAMPLE_OK` est **bloquant avant
GMC/Ads**. Un GO lundi et un Search mercredi, c'est 48 h. Soit on lève la porte pour les tests
Search (décision Hakim, §6 a), soit le planning est un pipeline glissant de trois semaines et
non un sprint d'une semaine.

### 2.3 Le comité du vendredi n'aura rien à lire

RULE-2026-001 (acceptée par Hakim le 31/08) : un test n'est concluant qu'à partir du **prix du
produit dépensé**. Aux ordres de grandeur connus (Tuftéo : CPC 0,91 €, 30 €/j) :

| Prix du produit | Dépense minimale | Jours à 30 €/j | Jours à 50 €/j |
|---:|---:|---:|---:|
| 99 € | 99 € | 4 | 2 |
| 199 € | 199 € | 7 | 4 |
| 299 € | 299 € | 10 | 6 |

Le produit A lancé mercredi a deux jours de données vendredi. Le produit B en a zéro. Le
comité « prediction vs reality : CVR, CPA, CA, marge » ne peut porter que sur les produits
lancés **la ou les semaines précédentes**. Le planning n'a pas cette notion de décalage.

Corollaire : le jeudi « vérifier les premiers signaux » est un contrôle technique (annonces
approuvées, dépense qui part, conversions qui remontent, requêtes hors sujet), pas une lecture
de performance. Il faut le nommer comme tel, sinon il redevient le « coupé à 110 € » de Tuftéo.

### 2.4 Aucun seuil d'arrêt ni règle de verdict n'est écrit

RULE-2026-001 dit que le seuil d'arrêt doit être **écrit avant le lancement**. Le planning n'a
ni ligne budget, ni seuil, ni règle « à ce seuil, voici ce qu'on décide ». Sans elle, la
décision se prend le jour où la dépense inquiète, et c'est exactement le défaut à corriger.
Proposition en §4.

### 2.5 La croyance n'est écrite nulle part

`instrumentation/croyances/` existe précisément parce que la thèse d'avant-lancement est
irrécupérable après coup : celle de Tuftéo a dû être reconstruite le 30/08. Le planning a
« prediction vs reality » le vendredi mais aucune tâche « écrire la prédiction » avant le
lancement. Elle tient en dix minutes et doit faire partie du gate Hakim.

### 2.6 L'univers ne rentre pas dans une semaine

« Soumission/activation Shopping-GMC pour Produit Univers » le mercredi : un univers, c'est des
dizaines de collections, un sourcing par famille et une boutique **terminée** avant review.
Lumière Matière en est la preuve : domaine ouvert le 24/08, attente 30 jours jusqu'au 23-24/09,
puis repos 7-10 jours, commande test, une seule review, zéro ad. Le Q4 Testing OS ne peut être
qu'un **OS produit pur / Search**. L'univers vit sur une piste mensuelle séparée.

### 2.7 Soumettre chaque boutique de test à GMC met le parc en danger

Le Search texte n'a pas besoin de Merchant Center. Le Shopping, si. Mais chaque boutique
de test partage l'identité OH Ventures, et une suspension « attache l'entité » (précédent du
15/06, puis Noirmont le 23/08). Une boutique bâtie en un jour et demi, soumise à GMC deux
boutiques par semaine, c'est le meilleur moyen de faire tomber Tuftéo, Bonum Vitae et Noirmont
avec elle. GMC **seulement pour les gagnants**, une fois la boutique finie et l'échantillon
contrôlé. Il faut accepter que « Shopping après » ait deux à quatre semaines de latence
pendant lesquelles le Search continue de tourner.

### 2.8 Le parc existant n'a aucun créneau

Le plan des experts du 16/08 disait : Tufting visuels puis GMC, Montres GMC, Osmoseur retesté
en septembre avec un budget suffisant. Rien de tout cela n'apparaît dans l'OS. Or ce sont les
tests **les moins chers du monde** : pas de découverte, pas de build, pas d'échantillon, GMC
déjà validé pour Tuftéo et Bonum Vitae.

| Boutique | État au 04/09 | Ce qui manque pour tester |
|---|---|---|
| Bonum Vitae (osmoseur 299 €) | jamais eu de campagne, 9 checkouts / 185 sessions, GMC validé | une campagne et 299 € de seuil écrit |
| Tuftéo (kit 229 €) | test coupé à 110 €, 48 % du seuil, GMC validé | rejouer jusqu'à 229 € |
| Maison Noirmont (montres) | ban « déclarations trompeuses » 23/08, corrections 01/09 | la demande de réexamen après 7-10 j, une seule cartouche |
| Lumière Matière (univers) | en ligne, 52 fiches, sans GMC | attendre le 23-24/09 puis la séquence LM |

### 2.9 Le temps de Hakim est sous-estimé

Le planning lui donne deux gates de 20-30 min. Mais par boutique de test, seul Hakim peut :
acheter le domaine, créer la boutique Shopify, activer les paiements, créer l'e-mail pro (et
passer le mur SMS Workspace), créer ou lier le compte Google Ads et sa facturation, commander
l'échantillon. Ce sont des heures, pas des minutes, et elles tombent le lundi soir pour A et
le mercredi pour B. Il faut les nommer et les grouper.

### 2.10 Le budget dicte la cadence, pas l'inverse

Deux lancements par semaine avec des tests de 7 à 10 jours, c'est trois à quatre tests en
parallèle en régime établi. Ordre de grandeur à 30 €/j par test :

| Cadence | Tests en parallèle | Ads / semaine | Ads / mois | Fixes / mois (Shopify + domaines) |
|---|---:|---:|---:|---:|
| 1 lancement / semaine | 1-2 | ~300 € | ~1 300 € | ~150 € |
| 2 lancements / semaine | 3-4 | ~600 € | ~2 600 € | ~300 € |

Le planning ne fixe pas de budget hebdomadaire. La cadence doit en découler :
`tests par semaine = budget ads hebdo ÷ prix moyen des produits testés`.

## 3. La contrainte calendrier Q4

Aujourd'hui vendredi 04/09. Pour qu'un produit soit **scalé en Shopping** avant le Black Friday
(27/11), il faut compter : échantillon 1-3 semaines, test Search 7-14 jours, finition boutique,
review GMC 2-7 jours, montée en budget par paliers. Cela donne :

| Semaine | Dates | Ce qui doit se passer |
|---|---|---|
| 37-39 | 07/09 → 27/09 | **fenêtre de découverte** : GO_FINAL + échantillons, retests du parc |
| 40-42 | 28/09 → 18/10 | tests Search jusqu'au seuil, verdicts, GMC des gagnants |
| 43-47 | 19/10 → 22/11 | plus de nouvelles découvertes ; scaling Shopping/PMAX des gagnants |
| 48 | 23/11 → 29/11 | Black Friday |
| 49-50 | 30/11 → 13/12 | dernières commandes livrables avant Noël avec la fenêtre 7-18 j |

Conclusion pratique : le Q4 Testing OS n'a **trois à quatre semaines** de cadence « nouveaux
produits ». Après le ~29/09, chaque nouveau GO arrive trop tard pour le Shopping Q4 ; il ne
vaut que comme test Search de Noël ou comme apprentissage 2027. L'OS doit changer de mode à
mi-octobre, et ce changement doit être écrit dedans.

## 4. Règles de test à écrire avant le premier lancement

### 4.1 Gabarit de campagne Search (un par produit, identique partout)

- Une campagne, un produit, ciblage France en **présence** (pas « présence ou intérêt »),
  partenaires de recherche et Display **désactivés**.
- Groupes d'annonces thématiques par intention (5-15 mots-clés), **exact + expression**,
  jamais de large avant 30 conversions/mois.
- 2 RSA par groupe. Conversion principale = achat ; ajout au panier et checkout en
  conversions secondaires, observées, non optimisées.
- Enchères : Maximiser les conversions **sans cible** tant qu'il y a moins de 15 conversions.
- Négatifs de départ FR : gratuit, pas cher, occasion, location, avis, test, comparatif,
  tuto, pdf, emploi, formation, la marque en négatif dans la campagne hors marque.
- Budget/jour = prix du produit ÷ 7, arrondi (199 € → 30 €/j ; 299 € → 45 €/j), pour
  atteindre le seuil en une semaine.

### 4.2 Ce qu'on touche pendant le test

- Enchères, budget, annonces : **rien** jusqu'au seuil. Ligne des experts du 16/08.
- J+1 : contrôle technique (approbation, dépense, conversions qui remontent).
- J+3 et J+7 : rituel termes de recherche, **négatifs uniquement**. Couper le hors-sujet ne
  casse pas l'apprentissage ; c'est le seul geste autorisé (à valider par Hakim, §6 d).

### 4.3 Verdict au seuil (dépense = prix du produit)

| Observé au seuil | Verdict | Suite |
|---|---|---|
| 0 ajout panier | ARRÊT | postmortem 30 min, croyance vs réalité |
| ajouts panier, 0 vente, checkout atteint | PROLONGER une fois, +50 % du seuil | vérifier prix, frais de port, moyens de paiement, mobile |
| ajouts panier, 0 vente, checkout jamais atteint | ARRÊT sauf défaut de page identifié | corriger la page, un seul rejeu |
| ≥ 1 vente | PROLONGER jusqu'à 2 × prix | premier point de calibrage réel |
| ≥ 2-3 ventes et CPA < break-even calculé mardi | GAGNANT CANDIDAT | Search +20 % par palier tous les 3-5 j ; finir la boutique ; échantillon contrôlé ; GMC ; puis `shopping-scaling` |

Au deuxième seuil (2 × prix), la règle des 2 jours verts / 2 jours rouges de
`shopping-scaling` prend le relais.

## 5. Proposition : la semaine v2, en tableau glissant

Le changement de fond : la semaine n'est plus « idée → lancement », c'est **un tableau à
quatre couloirs** où chaque produit avance d'un couloir par semaine. À tout moment, il y a un
produit au comité, un ou deux en build, un ou deux en attente d'échantillon, un ou deux en
test, et un au verdict.

| Couloir | Quand | Contenu | Qui |
|---|---|---|---|
| 0 · Veille continue | permanent, week-end inclus | découverte + Fast Gate + Deep Gate + contradicteur, jusqu'à `PASS_PREQUALIFICATION` + sourcing exact ; dépôt sur branche `agents/` | flotte Hermes |
| 1 · Comité | lundi matin, 1 h | décision sur le **pool prêt** uniquement ; `GO_FINAL` ; commande échantillon ; achat domaine ; création Shopify + paiements + e-mail (bloc Hakim 1-2 h, groupé) | Hakim + contradicteur d'un autre modèle |
| 2 · Build | lundi aprem → mercredi | persona → offre + break-even + **croyance écrite** → mini-charte → copy → visuels composés → Shopify + tracking ; QA mobile-first jeudi ; **pas de GMC** | agents |
| 3 · Test | lancement le jour du `SAMPLE_OK`, quel que soit le jour | gabarit §4.1 ; J+1 technique ; J+3/J+7 négatifs ; rien d'autre | Hakim lance, agent relève |
| 4 · Verdict | vendredi, sur les tests **au seuil** seulement | grille §4.3 ; `mesures/` ; croyance vs réalité ; Mac Fund ; règle apprise si une émerge (jamais promue sans Hakim) | Hakim + agent |

### Semaine type v2

| Jour | Matin | Après-midi |
|---|---|---|
| Lundi | Comité sur le pool prêt (1 h) · bloc Hakim comptes/domaine/échantillon (1-2 h) | Build A : persona, offre + break-even + croyance |
| Mardi | Build A : charte, copy, visuels | Build A : Shopify + tracking |
| Mercredi | Build B (même séquence, un produit par semaine si le pool ne donne qu'un GO) | Lancement des tests dont l'échantillon est arrivé |
| Jeudi | QA mobile-first A (et B) · contrôles J+1 / négatifs J+3-J+7 | Réserve : parc existant (retests, Noirmont, LM) |
| Vendredi | Comité verdict sur les tests au seuil · `mesures/` · Mac Fund | Point calendrier Q4 (§3) : on est encore en fenêtre découverte ? |
| Week-end | Veille Hermes sur branche, pool prêt pour lundi | — |

### Trois premières semaines, concrètement

- **Semaine 37 (dès lundi 07/09)** : pas de nouvelle boutique. Lancer les deux retests du parc
  avec le gabarit §4.1 : Bonum Vitae jusqu'à 299 €, Tuftéo jusqu'à 229 €. Écrire leurs
  croyances (celle de Tuftéo existe, celle de Bonum Vitae aussi). Demande de réexamen Noirmont
  si les 7-10 jours post-corrections sont passés. Comité sur les REVIEW du 03/09 (rasoir de
  sûreté A6 en tête) avec preuve fournisseur exacte comme condition du GO.
- **Semaine 38** : premiers GO_FINAL si le pool le permet, échantillons commandés, build A.
  Verdicts Bonum Vitae et Tuftéo au seuil.
- **Semaine 39** : dernière semaine de GO utiles pour le Shopping Q4. Lancement Search des
  boutiques dont l'échantillon est arrivé. Lumière Matière entre dans sa séquence GMC le 23-24/09.

## 6. Décisions qui reviennent à Hakim

a. **Porte échantillon pour les tests Search.** Garder `SAMPLE_OK` bloquant (pipeline glissant
   de trois semaines, zéro risque de livrer un produit non contrôlé) ou la lever pour les
   produits non électriques testés en Search seul (cadence hebdo possible, mais une vraie
   commande partirait sans contrôle). Ma recommandation : la garder, et absorber la latence
   avec le tableau glissant.
b. **Un compte Google Ads « tests » ou un compte par boutique.** Un compte unique évite de
   recréer facturation et vérification annonceur chaque semaine, et le gagnant migre ensuite
   sur son compte propre avec son GMC. Cela touche la règle d'isolation du 24/08, donc c'est
   à toi de trancher.
c. **Budget ads hebdomadaire.** C'est lui qui fixe la cadence (§2.10). Sans ce chiffre, le
   planning ne peut pas dire combien de produits il teste.
d. **Négatifs pendant le test.** Autoriser le rituel J+3/J+7 « négatifs seulement », ou tenir
   la ligne « on ne touche à rien » des experts.
e. **Boutiques de test sans validation DA.** La mini-charte time-boxée contredit la règle
   « valider la direction avec Hakim » : à assumer explicitement pour les boutiques de test,
   la vraie DA venant à la finition du gagnant.
f. **Bascule de mode à mi-octobre.** Écrire dans l'OS que, passé le ~29/09, plus aucun nouveau
   GO n'est pris pour le Shopping Q4 et que la semaine devient scaling + finition.

## 7. Ce que ce document ne fait pas

Il ne modifie pas la base Notion, ne change aucun seuil canonique, ne lance aucune campagne et
ne promeut aucune règle. Si Hakim valide la v2, la base Notion se réécrit en quatre couloirs
(propriété « Couloir » à la place de « Jour ») et les règles de §4 deviennent un fichier
`instrumentation/regles/` candidat.

---
type: journal
boutique: seiko-mod
date: 2026-08-14
nature: intervention
leviers: [autre]
titre: "Compte rendu de la nuit du 13 au 14/08/2026"
---

# Compte rendu de la nuit du 13 au 14/08/2026

Six chantiers menés, aucun ne demandait de génération d'images (quota épuisé jusqu'au 18/08).
Point d'entrée pour agir : [`../TABLEAU.md`](../TABLEAU.md).

---

## 1. Le fait de la nuit : le positionnement était faux

La recherche de mots-clés (T-21) puis le dossier de positionnement (T-26) renversent la stratégie.

**Les mots-clés sur lesquels on raisonnait n'existent pas.**

| Ce qu'on croyait | Ce que SEMrush mesure |
|---|---|
| `cadran arabe` — 15 500/mois | **20/mois** |
| `cadran pilote` — pilier retenu le 12/08 | **volume non restitué** (< 10) |
| `cadran stérile` — pilier retenu le 12/08 | **volume non restitué** — le mot n'est pas tapé par un particulier |
| `cadran squelette` | 20/mois |

Le chiffre de 15 500 a piloté une semaine de décisions. Il était faux d'un facteur 750.

**Ce qui existe est côté montres finies, pas côté pièces.**

Têtes de famille : **9 200/mois** côté montres (KD 6-16) contre **4 070** côté pièces ; grappes ≈ **33 000** contre **20 400**.

- `montre de plongée` **1 600**, KD 13 — **seule tête à intention commerciale de tout le corpus**
- `montre squelette homme` **2 900** (contre `cadran squelette` 20)
- `montre aviateur` **1 600** (contre `cadran pilote` 0)
- `montre gmt` **1 000** · `montre chronographe homme` **1 000** · `montre chiffre arabe` **880**, KD 6

**Correction dans la correction** : le « 9 500 » arabe annoncé par T-21 était à 85 % du `seiko arabic dial` — **marque tierce, interdite en flux Merchant Center**. Le vrai mot est `montre chiffre arabe`, 880/mois, et il désigne des chiffres **occidentaux**. Cinq fiches en ligne le servent déjà : c'est un trou de **nommage**, pas d'offre.

### La recommandation : scénario A

**Boutique de montres finies, les 91 pièces en deuxième rideau de panier moyen.**

Le catalogue actif **est déjà** cette boutique : **57 montres en 9 familles**, prix appliqués 279-429 €, galeries maison, **zéro photo AliExpress brute**. Le défaut des titres ne touche que les brouillons de pièces.

Et l'argument décisif : **A ramène le chantier des 1 091 photos brutes de ≈ 150-180 h à ≈ 50-60 h**, en réduisant le périmètre prioritaire aux ~30 pièces réellement utiles en cross-sell. Le scénario B (boutique de pièces) exigerait les 1 091 avant la première vente, avec un panier à 12,90-89,90 € et ≈ 17 500 recherches perdues par la règle « marque tierce », qui pèse presque entièrement sur les pièces.

**Trous d'offre à combler** : squelette (grappe 8 400 pour **2 produits**), style plongeuse (1 600 pour **3**), aviateur (2 630, **aucune collection**).
**Surdotation** : sport chic — **14 produits pour 110 recherches**.

**Décision attendue de Hakim.** Tant qu'elle n'est pas prise, la réécriture des 200 fiches (T-31) reste bloquée : l'engager maintenant reviendrait à optimiser autour d'une arborescence qui va changer.

---

## 2. Ce qui a été fait

**Sources fournisseur reconstituées (T-23)** — **311 photos sur 311** récupérées par l'API, plus 11 images de variantes : 322 images, 35 fiches sur 35, le stock local passe de 10 % à 100 %. Les 35 identifiants AliExpress sont **établis, pas devinés** (30 par recoupement d'image exact). Un piège écarté : un fichier de préflight rattachait un article au mauvais produit — zéro image en commun contre 25 sur 26 pour le bon. La matière première sera prête pour la reprise du 18.

**Audit des 95 brouillons (T-16)** — hypothèse de départ fausse, et c'est une bonne nouvelle : les 311 médias retirés étaient **311 photos brutes et zéro visuel maison**, remplacés par 146 visuels maison. Rien à réparer, aucune mutation exécutée.

**Deux fiches arabes remises au standard (T-04)** — handles, titres, descriptions, meta, tags, rattachement. Toujours en DRAFT.

**87 `alt` réécrits (T-08)** — le défaut dépassait la fiche signalée, et plusieurs `alt` n'étaient pas génériques mais **faux** : « Violet » désignait du magenta, « Orange » de l'ambre.

**Audit GMC vérifié sur la boutique (T-11)** — soldés : faux témoignages, sections d'avis, badge 4,8/5, politiques de retour, pied de page légal, CNIL, ODR. Corrigés cette nuit : dernier « 904L », mentions légales (servaient un texte générique sans RCS ni SIREN, avec une clause de juridiction contredisant les CGV), page contact vide, politique de cookies, 16 meta descriptions et 12 meta titles.

---

## 3. Trois problèmes découverts

**2 065 variantes sur 3 009 portent encore un SKU AliExpress brut** (84 brouillons, 95 avec « no logo »). Les 931 variantes du catalogue d'origine avaient été purgées le 08/08, mais les 94 fiches importées le 09/08 sont arrivées avec des SKU fournisseur neufs. Bloquant Merchant Center. → **T-32**

**Le consentement cookies n'existe pas.** Une vérification du 12/08 avait conclu à un faux positif de l'audit ; cette vérification était elle-même fausse, et la politique de cookies affirmait qu'un bandeau existait. À faire **avant** le tracking, sinon on collecte sans consentement. → **T-33**

**Le médiateur n'est pas dans les CGV.** L'adhésion est peut-être faite, mais l'article 15 sert toujours `[[MEDIATEUR_NOM]]`. → **T-H2 rouvert**

---

## 4. Ce qui attend Hakim

| # | Décision |
|---|---|
| **T-26** | **Le positionnement** — scénario A recommandé. Tout le reste en dépend. |
| T-H3 | La grille de prix (deux stratégies chiffrées prêtes) |
| T-H2 | Reporter le nom du médiateur dans les CGV |
| T-H4 | Basculer l'e-mail boutique — ⚠️ vérifier que la boîte `.fr` reçoit avant de changer l'expéditeur |
| T-33 | Activer le consentement cookies |
| T-30 | Le `904L` gravé sur un bracelet — recommandation : abandonner la fiche |
| T-20 | Le mot `Automatic` gravé — recommandation : le garder |

## 5. Reporté au 18/08 (génération d'images)

Les 1 091 photos brutes des 60 brouillons · les 12 fiches actives sous la cible · le guichet de date « 42 » · les 9 composites partagés entre fiches mère et enfant.

**Deux vigilances pour la reprise** : les filigranes `Tandorio` et `alpha dial` sont sur les photos, pas sur les produits — ils ne doivent jamais passer dans une composition.

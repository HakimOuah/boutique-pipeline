---
type: journal
boutique: tufting
date: 2026-09-02
nature: mesure
leviers: [ads]
titre: "Shopping, 3 jours : 15,90 € dépensés sur 120 € de budget — pourquoi"
---

# Shopping, trois jours — 02/09/2026 10 h 25

Captures Google Ads envoyées par Hakim, campagne **FR-SHOPPING-TUFTING**.

## Relevé

| Jour | Clics | Impressions | Lecture |
|---|---:|---:|---|
| 30/08 | 0 | ~0 | lancée en soirée, n'a pas servi |
| 31/08 | 11 | 655 | ≈ 5 € |
| 01/09 | ~20 | ~1 500 | ≈ 9 € — pic |
| 02/09 (10 h 25) | ~4 | ~500 | journée partielle |
| **Total** | **35** | **2 630** | **15,90 €** · CPC moyen **0,45 €** |

Budget cumulé disponible sur la période : 120 €. Dépensé : 13 %.

## Paramètres constatés

| | |
|---|---|
| Type | Shopping standard, Merchant Center `5829640586` |
| Flux | tous les produits de tous les flux |
| Budget | 40 €/jour |
| Enchères | **Maximiser les clics**, plafond CPC **0,80 €** |
| Objectifs de conversion | « par défaut dans le compte » |
| Priorité | faible (sans effet : une seule campagne Shopping) |

## Pourquoi 15,90 € et pas 120 €

Le budget est un plafond. Google ne dépense que sur les enchères qu'il gagne. Trois choses le
bornent ici, dans cet ordre de probabilité :

**1. Le marché est petit.** Cluster `tufting` France nettoyé : 13 000–17 000 recherches/mois,
tête `tufting` 8 100/mois dont une part informationnelle
([validation-semrush-2026-07-17](../../reports/validation-semrush-2026-07-17.md)). Soit
450–550 recherches par jour, toutes intentions confondues. Dépenser 40 €/jour à 0,45 € de CPC
exigerait ~90 clics/jour — plus que l'ensemble des recherches commerciales françaises du sujet.
Le budget a été dimensionné au-dessus du marché.

**2. Le plafond CPC à 0,80 €.** Le CPC SEMrush de référence sur `tufting` était 0,77 €, le cluster
0,48 €. Le plafond est posé pile au niveau du marché. Sur les requêtes chères — `kit tufting`,
`tufting gun` — où letufting, TuftingShop et Kreoho enchérissent, 0,80 € perd une partie des
enchères. Le CPC moyen à 0,45 € dit que la campagne gagne surtout les enchères bon marché :
requêtes génériques et accessoires.

**3. La montée en charge.** Une campagne Shopping neuve met 3 à 7 jours à se déployer.
Les impressions ont plus que doublé entre le 31/08 et le 01/09. Ce n'est pas encore stabilisé.

Ce qui n'explique **pas** la sous-dépense : la priorité faible (n'agit qu'entre ses propres
campagnes Shopping), le flux « tous les produits » (correct).

## Comment trancher entre 1 et 2

Dans Google Ads, colonnes « Taux d'impressions sur le Réseau de Recherche », « perdues
(classement) », « perdues (budget) » :

- perdues (budget) ≈ 0 % et perdues (classement) élevé → **le plafond CPC** bride.
- taux d'impressions déjà haut (> 60 %) → **le marché** est le plafond, pas les réglages.

## Ce qu'on ne fait pas

- **Pas de hausse de budget** : ne produirait rien, c'était déjà écrit le 30/08.
- **Pas de conclusion** : 35 clics, 0 commande — attendu. [[RULE-2026-001]] : rien n'est
  concluant sous 269 € dépensés. On en est à 6 %.

## Ce qu'il faudrait regarder

1. **Onglet Produits** de la campagne : qui prend les 35 clics ? Si ce sont les fils à 12,90 €,
   le CPC achète des clics sans marge. Le plan était kit + gun.
2. **Objectif de conversion** « par défaut dans le compte » : vérifier que l'achat Shopify est
   bien remonté. Sans conversion mesurée, la campagne n'apprendra jamais.
3. **UTM** toujours absents (constat du 30/08) : 35 clics déjà indiscernables côté Shopify.
4. Si perdues-classement est élevé : monter le plafond à ~1,20 € sur un groupe de produits
   kit + gun seulement. La marge du kit (161 €) l'absorbe ; celle d'un cône (7,70 €) non.

## 10 h 31 — colonnes vides, et la question « Maximiser la valeur de conversion ? »

Les colonnes « Tx impr. perdues RR (budg.) / (class.) » affichent « — ». Google ne calcule le
taux d'impressions qu'au-delà d'un volume minimal et avec un jour de décalage ; à 2 630
impressions sur deux jours, on est sous le seuil. À relire dans 2–3 jours, au niveau campagne,
sur 7 jours glissants.

**Maximiser la valeur de conversion : non, pas maintenant.** Trois raisons :

- **0 conversion depuis l'ouverture du compte.** Les stratégies pilotées par la valeur ont
  besoin d'un historique — Google lui-même recommande 15–30 conversions sur 30 jours. Sans
  signal, l'algorithme n'a rien à optimiser : il baisse les enchères ou les rend erratiques.
  Ça ne corrige pas la sous-dépense, ça l'aggrave.
- **La valeur n'est pas vérifiée.** « Objectifs de conversion : par défaut dans le compte » —
  on ne sait pas si l'achat Shopify remonte avec son montant. Optimiser sur une valeur qu'on
  ne mesure pas, c'est optimiser à l'aveugle.
- **Le problème n'est pas la stratégie d'enchères.** Changer de stratégie ne crée pas
  d'enchères ; le marché en fournit 450–550 recherches/jour, point.

Le cadre maison (`shopping-scaling`, phase 1) : aucune complexité avant d'être profitable ;
si ça ne dépense pas, attendre 3–4 jours puis **un seul** ajustement.

**Décision** : rester en Maximiser les clics — c'est la stratégie qui achète le plus de clics
sans donnée, donc celle qui teste le tunnel de paiement le plus vite. Le seul levier légitime
est le plafond CPC. Au rythme actuel (~7 €/jour), les 269 € du seuil de lecture arrivent dans
**38 jours** : trop lent pour un test. Un ajustement, une fois : plafond 0,80 → **1,20 €**,
puis ne plus toucher pendant 7 jours.

**Prérequis avant toute stratégie par la valeur, quel que soit le jour** : Outils → Conversions,
une action « Achat » venant de l'app Google & YouTube, statut actif, avec valeur. À vérifier
maintenant — ça ne coûte rien et ça conditionne tout le reste.

## 10 h 35 — plafond CPC passé à 1,20 €

Hakim : « ok c'est fait j'ai changé le CPC ». Un seul ajustement, comme décidé. **Ne plus
toucher pendant 7 jours** (jusqu'au 09/09). Relire alors : dépense/jour, CPC moyen, onglet
Produits, et les colonnes taux d'impressions si elles se remplissent.

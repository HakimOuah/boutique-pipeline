---
type: journal
boutique: tufting
date: 2026-08-30
nature: intervention
leviers: [ads]
titre: "Lancement des campagnes Google Shopping"
---

# Lancement des campagnes Google Shopping

**30/08/2026, soirée.** Hakim lance des campagnes Google Shopping sur Tuftéo. Deuxième dépense
d'acquisition de l'histoire du parc, après la campagne Search du 24/07 – 02/08.

Entrée créée le 31/08 pour dater l'événement, pas pour le commenter : sans elle, le mouvement de la
courbe des semaines à venir ne serait rattachable à rien. C'est exactement le rôle du registre des
interventions.

## Paramètres de la campagne

| | |
|---|---|
| Type | Shopping, groupe d'annonces « Tufting », état **Éligible** |
| Budget | **40 €/jour** |
| Première soirée (30→31/08) | 124 impressions · **1 clic** · CTR 0,81 % · CPC 0,67 € · **0,67 € dépensé** |

À 40 €/jour et 0,67 € de CPC, le seuil de [[RULE-2026-001]] — **269 €**, le prix du kit depuis le
17/08 (la note disait 229 €, prix d'avant) — est atteignable en **moins de sept jours**, à
condition que le budget se dépense. Il ne s'est pas dépensé : voir
[[2026-09-02-shopping-3-jours]].

**Le budget n'est pas la contrainte au démarrage** : 0,67 € consommé sur 40 € disponibles. Ce qui
limite, c'est le nombre d'entrées en enchère. Si la dépense ne monte pas, augmenter le budget ne
produira rien — les leviers sont les **enchères** d'abord, la **couverture du flux** ensuite. Le
budget ne devient le frein qu'une fois consommé en entier.

## Ce qui est mesuré au moment du lancement

Relevé ShopifyQL du 31/08 en début de journée :

| Jour | Sessions | Paniers | Checkouts | Commandes |
|---|---:|---:|---:|---:|
| 27/08 | 3 | 0 | 0 | 0 |
| 28/08 | 0 | 0 | 0 | 0 |
| 29/08 | 1 | 0 | 0 | 0 |
| 30/08 | 0 | 0 | 0 | 0 |
| 31/08 | 4 | 0 | 0 | 0 |

Origine sur cinq jours : 5 direct, 2 search, 1 unknown. **Aucune session en `cpc`.** La campagne
ne diffuse probablement pas encore, ou elle démarre à peine.

## Le point de vigilance

**Le balisage UTM n'est pas en place.** `utm_medium` ne rend que `None` et `product_sync` — cette
dernière étant la synchronisation de l'app Google & YouTube, pas un visiteur.

Tant que le modèle de suivi n'est pas posé au niveau du compte Google Ads, cette campagne sera
**inévaluable** : ni CPC réel côté boutique, ni coût par ajout au panier, ni CPA, ni ROAS — le
trafic payant restera indiscernable du référencement naturel. C'est ce qui est arrivé aux 110 € de
juillet. Voir [[balisage-utm]].

La dépense étant encore quasi nulle au moment où ce constat est fait, poser le balisage maintenant
ne perd presque rien.

## Le seuil qui s'applique

[[RULE-2026-001]] : un test n'est concluant qu'à partir du prix du produit dépensé. Le kit complet
étant à **229 €**, c'est le budget en dessous duquel aucune conclusion ne sera tirable — ni en bien,
ni en mal. La campagne de juillet s'était arrêtée à 110 €, soit 48 % du seuil.

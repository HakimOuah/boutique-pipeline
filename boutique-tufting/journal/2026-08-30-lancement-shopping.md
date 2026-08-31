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

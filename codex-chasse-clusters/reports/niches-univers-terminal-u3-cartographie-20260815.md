# U3 globe/cartographie France — verdict terminal volume catalogue

**Date de coupe :** 2026-08-15
**Statut :** `STOP_VOLUME_CATALOGUE`
**Périmètre :** gate volume France ; aucune architecture, aucun sourcing
**Source des volumes :** mesures SEMrush France fournies par le pilote. Elles ne sont pas revérifiées ici via Chrome.

## Verdict

**STOP_VOLUME_CATALOGUE.** Après nettoyage des intentions génériques et ajout des trois intentions murales mesurées, le noyau commercial prudent atteint **22 870 recherches/mois**, soit **7 130 sous le seuil de 30 000**.

Le globe seul reste trop étroit. L'élargissement légitime aux cartes murales, planisphères muraux et posters ne ferme pas le déficit. Les heads génériques `carte du monde`, `planisphère` et `mappemonde` ne peuvent pas être ajoutés sans nettoyage, car ils sont informationnels, synonymiques ou servis par les mêmes pages.

## OBSERVÉ

### Noyau produit déjà retenu

| Intention | Volume FR/mois | Traitement |
|---|---:|---|
| globe terrestre | 18 100 | produit 3D distinct |
| carte monde bois | 1 600 | produit mural construit distinct |
| carte monde à gratter | 1 900 | produit interactif distinct |
| **Sous-total** | **21 600** | |

### Complément mural fourni par le pilote

| Intention | Volume FR/mois | Traitement |
|---|---:|---|
| carte du monde murale | 590 | intention murale explicite |
| planisphère mural | 90 | intention murale explicite |
| poster / carte du monde poster | 590 | cluster poster compté une fois |
| **Complément** | **1 270** | |

### Calcul terminal

```text
noyau produit prudent       21 600
complément mural             1 270
                            ------
total commercial prudent    22 870
seuil catalogue             30 000
déficit                      7 130
```

Les 590 recherches du cluster poster ne sont comptées qu'une fois. Aucun volume générique n'est réintroduit dans le calcul.

## MANQUANT

- Une réserve commerciale dédupliquée d'au moins 7 130 recherches/mois.
- Un export mot-clé démontrant que cette réserve appartient à des familles qu'une même boutique cartographie peut légitimement servir.
- La preuve que `planisphère`, `mappemonde` ou `carte du monde` contiennent assez de requêtes achat supplémentaires après exclusion de la géographie, des images, du gratuit et de l'imprimable.

## HYPOTHÈSE rejetée au gate actuel

L'hypothèse « élargir le globe à la cartographie murale suffit à dépasser 30 k » n'est pas soutenue par les mesures disponibles : l'ajout mural ne représente que 1,27 k.

## Conséquence opérationnelle

- Ne pas lancer d'étude concurrentielle plus profonde, d'arborescence ou de sourcing pour U3.
- Ne rouvrir U3 que si un nouveau lot de mots-clés France, commercial et dédupliqué, apporte au moins 7,13 k de volume éligible sans agréger des intentions arbitraires.

Rapport de preuve détaillé antérieur : [nettoyage SERP, prix et concurrence U3](serp-prix-concurrence-u3-cartographie-20260815.md).

---
type: journal
boutique: seiko-mod
date: 2026-08-09
nature: intervention
leviers: [sourcing, technique]
titre: "File DSers — cadrans arabes orientaux — API officielle — 09/08/2026"
---

# File DSers — cadrans arabes orientaux — API officielle — 09/08/2026

**STATUT : PARTIELLE — 1 nouvelle fiche qualifiée, aucun import autorisé ou exécuté.**

Format : `URL | handle proposé | collection | statut`.

```text
https://fr.aliexpress.com/item/1005009751528666.html | cadran-arabe-oriental-soleille-28-5 | cadrans-arabes-orientaux | PASS API OFFICIEL — À IMPORTER EN DRAFT UNIQUEMENT APRÈS ACCORD HAKIM
```

## Liste blanche de variantes cadran seul

Au mapping DSers, conserver uniquement ces SKU exacts. Les ensembles cadran + aiguilles et les variantes aiguilles seules ne font pas partie de cette file.

| SKU AliExpress exact | Variante fournisseur | Prix TTC observé | Stock | Fret France | Décision |
|---|---|---:|---:|---:|---|
| `12000050049927398` | Black Gold Dial | 5,69 EUR | 495 | 1,99 EUR | garder |
| `12000050049927390` | Black Silver Dial | 5,69 EUR | 484 | 1,99 EUR | garder |
| `12000050049927393` | Sky Blue Dial | 5,69 EUR | 3 | 1,99 EUR | garder seulement si stock ≥ 5 au recontrôle |
| `12000050049927394` | Pink Dial | 5,69 EUR | 490 | 1,99 EUR | garder |
| `12000050049927392` | Green Dial | 5,59 EUR | 492 | 1,99 EUR | garder |
| `12000050049927389` | White Silver Dial | 5,59 EUR | 488 | 1,99 EUR | garder |
| `12000050049927395` | Brown Dial | 5,59 EUR | 495 | 1,99 EUR | garder |
| `12000050049927397` | White Rose Dial | 5,69 EUR | 499 | 1,99 EUR | garder |
| `12000050049927399` | Black Rose Dial | 5,49 EUR | 494 | 1,99 EUR | garder |
| `12000050049927396` | White Gold Dial | 5,59 EUR | 489 | 1,99 EUR | garder |
| `12000050049927391` | Blue Dial | 5,59 EUR | 492 | 1,99 EUR | garder |

## Contrôles obligatoires avant un futur push

- refaire `variants` puis `exact` via l'API officielle pour chaque SKU gardé ;
- décocher toute variante sous le seuil de stock décidé par Hakim ;
- vérifier dans DSers que seules les variantes cadran seul sont sélectionnées ;
- relire la case **Set product status as Draft** avant chaque lot ;
- ne publier sur aucun canal ;
- ne pas reprendre les photos filigranées dans Shopify ;
- ne pas écrire de prix de vente sans arbitrage de Hakim.

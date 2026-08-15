# U2 bouillottes — verdict terminal

- Date : 2026-08-15
- Marché : France
- Mode : `catalogue-volume`, lecture seule

## Verdict

**`REPARER_AVANT_SOURCE_EXACTE`**, sous-statuts `MARCHE_CONDITIONNEL_NON_VALIDE` et `ECONOMIE_MANQUANTE_APRES_ECHEC_SOURCE`.

U2 n'est ni un STOP prix automatique, ni un marché retenu, ni un candidat économique. Il reste le seul univers dont les signaux justifient une réparation bornée sur preuve fournisseur exacte.

## Gates

| Gate | Preuve | Décision |
|---|---|---|
| Volume | minimum prudent publié 42 600/mois ; CPC 0,09–0,21 USD | `PASS_PROVISOIRE` : mapping SERP/page non certifié |
| Prix/panier | n=40, médiane 17,63 EUR, 40 % sous 15 EUR ; coffret 58,50 EUR et paniers de deux références 50–60 EUR observables | `NON_STOP_NON_VALIDE` : panier constructible, AOV et attachement non prouvés |
| Concurrence/sécurité | 8 acteurs ; profondeur, cross-sell, franco et coffrets ; rappels et non-conformités documentés | aucune différence ni sécurité fournisseur qualifiée |
| Sourcing officiel | 4 recherches, 30 résultats, 0 pertinent | `REPARER_AVANT_SOURCE_EXACTE` |
| Économie | aucun SKU, coût produit, fret France, retours ou CAC | `ECONOMIE_MANQUANTE_APRES_ECHEC_SOURCE` |

## Écart de processus conservé

Le rapport concurrentiel U2 concluait « pas GO marché ». Le pilote a ensuite ouvert une sonde fournisseur conditionnelle et strictement read-only à partir du volume, des CPC et des paniers marchands observables, mais sans checkpoint de gate séparé persisté avant l'appel API. La critique indépendante classe cette transition comme une rupture documentaire.

Aucune mutation n'est à annuler : le chemin s'est limité à `search`, sans `variants`, `exact`, DSers, Shopify, panier ni commande. Le présent terminal ne transforme pas rétroactivement cette sonde en GO. Il enregistre l'écart et ferme toute nouvelle recherche générique.

## Condition unique de réouverture

Fournir par un canal autorisé une URL ou un identifiant produit exact. Qualifier ensuite, dans cet ordre : variante, composition/capacité, mode de chauffe, stock, fret France, avertissements et sécurité ; puis coût rendu, retours/défauts, marge contributive, CAC et ROAS de rupture. Sans cette preuve, U2 reste non retenu.

## Sources locales

- `reports/phase0-univers-u2-bouillottes-20260815-181328-a1.md`
- `reports/serp-prix-u1-u2-20260815.md`
- `reports/u2-bouillottes-competiteurs-panier-20260815.md`
- `reports/phase4-sourcing-u2-bouillottes-20260815.md`
- `reports/phase5-economie-u2-bouillottes-20260815.md`
- `reports/critique-aveugle-six-univers-20260815.md`

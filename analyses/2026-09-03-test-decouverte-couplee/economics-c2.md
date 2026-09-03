# C2 — Sensibilité économique du kit casque TV

3 septembre 2026. Simulation avant sourcing : **aucune marge réelle, CVR de campagne ou rentabilité n'est observée**. Aucun appel payant supplémentaire.

## Données et hypothèses

- CPC issus de [`raw/22-first-controls.json.gz`](raw/22-first-controls.json.gz), observés à 13:45:51 UTC, Google Ads Search Volume Live, France, français, partenaires Search exclus. La [documentation officielle de cet endpoint](https://docs.dataforseo.com/v3/keywords_data-google_ads-search_volume-live/) confirme que le champ `cpc` est exprimé en **USD**. C'est un indicateur Google Ads, pas le CPC futur d'OH Ventures.
- Conversion : **1 EUR = 1,1578 USD**, [référence BCE du 2 septembre 2026](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html), revérifiée pour cette annexe. `CPC EUR = CPC USD / 1,1578`.
- **129,90 EUR TTC** est le prix du [kit Sennheiser RS 120-W officiel France](https://eu.sennheiser-hearing.com/fr-fr/products/rs-120-w) relevé dans [`competitors-c1-c2.md`](competitors-c1-c2.md). Cela ne prouve pas qu'un générique obtiendra ce prix. **99 EUR TTC est un scénario de prix**, pas une nouvelle offre concurrente observée.
- **TVA 20 % : hypothèse comptable de simulation.** Recette HT théorique de 82,50 EUR à 99 EUR TTC, et de 108,25 EUR à 129,90 EUR TTC. Les coûts devront être exprimés sur une base cohérente, après prise en compte de la TVA récupérable ou non selon le cas réel.
- Les CVR de **0,5 %, 1 % et 2 %** sont des scénarios, sans seuil de rejet universel ni prévision de performance.

## Contribution et plafond de coûts

`contribution avant Ads requise pour l'équilibre = CPC EUR / CVR`

`plafond de tous coûts variables hors Ads = prix TTC / 1,20 − contribution requise`

Le plafond doit financer **produit, transport, paiement, assistance, retours/SAV et tous les autres coûts variables**. Il ne réserve ni bénéfice cible ni frais fixes. La contribution requise correspond au CPA d'équilibre pour le scénario, pas à une marge déjà acquise.

| Intention / CPC USD | CPC EUR | CVR hypothétique | Contribution requise EUR | Coûts variables max à 99 EUR TTC | À 129,90 EUR TTC |
|---|---:|---:|---:|---:|---:|
| Produit « casque tv sans fil » / 0,25 | 0,2159 | 0,5 % | 43,19 | 39,31 | 65,06 |
| Idem | 0,2159 | 1 % | 21,59 | 60,91 | 86,66 |
| Idem | 0,2159 | 2 % | 10,80 | 71,70 | 97,45 |
| Comparatif « meilleur casque tv sans fil » / 0,34 | 0,2937 | 0,5 % | 58,73 | 23,77 | 49,52 |
| Idem | 0,2937 | 1 % | 29,37 | 53,13 | 78,88 |
| Idem | 0,2937 | 2 % | 14,68 | 67,82 | 93,57 |
| Usage « casque pour écouter la tv » / 0,38 | 0,3282 | 0,5 % | 65,64 | 16,86 | 42,61 |
| Idem | 0,3282 | 1 % | 32,82 | 49,68 | 75,43 |
| Idem | 0,3282 | 2 % | 16,41 | 66,09 | 91,84 |

Calcul effectué sans arrondi intermédiaire, affichage au centime. Les intentions restent séparées : ne pas associer automatiquement le CPC le moins élevé à l'ensemble du volume, ni supposer des CVR identiques entre recherche produit et comparatif.

## Frais et réserve : exemple séparé, non observé

Pour montrer ce qui doit être retiré du plafond, un scénario **purement hypothétique** pose des frais de paiement de `2 % du TTC + 0,30 EUR` et une réserve retours/SAV de `5 % de la recette HT`. Ces taux ne viennent ni d'un contrat ni de campagnes historiques ; ils ne sont pas proposés comme valeurs canoniques.

| Prix TTC | Paiement hypothétique | Réserve retours/SAV hypothétique | Déduction cumulée |
|---|---:|---:|---:|
| 99 EUR | 2,28 EUR | 4,13 EUR | 6,41 EUR |
| 129,90 EUR | 2,90 EUR | 5,41 EUR | 8,31 EUR |

Ainsi, pour la requête produit à **CVR 1 %**, il resterait **54,50 EUR** à 99 EUR TTC, ou **78,35 EUR** à 129,90 EUR TTC, pour le produit, le transport et les autres coûts variables non encore couverts. La réserve ne prouve ni le taux de retour ni le coût d'assistance ; éviter tout double comptage lors du remplacement de ces hypothèses par les coûts détaillés.

**Lecture :** les CPC observés rendent un examen économique pertinent ; ils ne suffisent pas à valider le produit. Le coût exact du kit, son taux de retour, la charge de compatibilité TV et la conversion restent inconnus. Ce tableau ne lève pas le gate de demande et n'autorise pas le sourcing avant `PASS_PREQUALIFICATION`. Aucun hard kill nouveau n'en découle.

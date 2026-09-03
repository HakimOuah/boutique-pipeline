# C6 — Poêle titane : sensibilité économique

3 septembre 2026. **Simulation de reprise motivée, avant sourcing.** Prix de la [PDP Titanox](https://titanoxfrance.com/products/titanox-poele-en-titane-pur-sans-pfas) relevés par la contrelecture : **59,99 EUR / 26 cm**, **64,99 EUR / 28 cm**, **69,99 EUR / 30 cm**. Source et limites de composition dans [`competitors-c6-c7.md`](competitors-c6-c7.md). Ces formats sont distincts ; aucun prix supérieur ni panier multiple n'est supposé.

## Entrées et calcul

- [`raw/43-c6-controls.json.gz`](raw/43-c6-controls.json.gz), France/français, 14:07:59 UTC : **« poele en titane » 1,22 USD** et **« poêle sans pfas » 1,42 USD**. La [documentation officielle DataForSEO](https://docs.dataforseo.com/v3/keywords_data-google_ads-search_volume-live/) confirme la devise du champ `cpc`. Ce proxy ne prédit pas notre CPC futur. La demande PFAS n'est pas automatiquement adressable par l'offre ni additionnable au cluster titane.
- Conversion [BCE du 2 septembre 2026](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html), revérifiée : **1 EUR = 1,1578 USD**.
- **Hypothèses : TVA 20 %, CVR 0,5 / 1 / 2 %.** Recette HT simulée : 49,99 EUR à 59,99 EUR TTC ; 58,325 EUR à 69,99 EUR TTC. Ces CVR ne constituent pas une règle de rejet.

`contribution avant Ads requise = CPC EUR / CVR`

`plafond de tous coûts variables hors Ads = recette HT − contribution requise`

| CPC proxy / intention | CVR hypothétique | Contribution requise | Plafond coûts à 59,99 EUR TTC | À 69,99 EUR TTC |
|---|---:|---:|---:|---:|
| 1,22 USD = 1,0537 EUR / titane | 0,5 % | 210,74 EUR | −160,75 EUR | −152,42 EUR |
| Idem | 1 % | 105,37 EUR | −55,38 EUR | −47,05 EUR |
| Idem | 2 % | 52,69 EUR | −2,69 EUR | **5,64 EUR** |
| 1,42 USD = 1,2265 EUR / sans PFAS | 0,5 % | 245,29 EUR | −195,30 EUR | −186,97 EUR |
| Idem | 1 % | 122,65 EUR | −72,65 EUR | −64,32 EUR |
| Idem | 2 % | 61,32 EUR | −11,33 EUR | −3,00 EUR |

Calcul sans arrondi intermédiaire. Le plafond couvre **produit, transport, paiement, assistance, retours/SAV et autres coûts variables** ; aucun bénéfice cible ni frais fixes n'est réservé. Un plafond négatif signifie que ce scénario de prix/CPC/CVR ne couvre même pas les Ads avant les autres coûts. Il ne démontre pas une impossibilité sous toute autre performance.

## Lecture de sévérité

Au meilleur cas du tableau — 69,99 EUR et CVR 2 % sur l'intention titane — il reste **5,64 EUR pour tous les coûts variables**. Si l'on applique uniquement l'exemple hypothétique de C2, paiement `2 % du TTC + 0,30 EUR` et réserve SAV `5 % du HT`, la déduction est de **4,62 EUR** : il resterait **1,02 EUR** pour le produit, le transport et les autres coûts non couverts. **Ce ne sont ni des tarifs contractuels ni des coûts fournisseur observés.**

Cela justifie une forte réserve économique sur l'offre unitaire aux prix relevés, sans inventer un CVR maximal canonique. Coût rendu, marge réelle, CVR, fréquence des retours et capacité à défendre un autre prix restent **MANQUANT**. Les incohérences de claims de matériau et de température relevées par la contrelecture empêchent d'accorder une prime de différenciation sans vérification ; elles ne modifient pas les formules. Le tableau ne lève pas le gate de demande, n'autorise pas de sourcing et ne remplace pas le verdict de l'orchestrateur.

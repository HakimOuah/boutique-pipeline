# Station météo DE et complément Search — 5 septembre 2026

## Search des spécialistes ultrasons

TrendTrack google-ads/query, networks search, recherche par domaine :
- ultraschall-welt.de : 10 annonces exactes sur les 10 retournées, dernières observations entre le 20 mai et le 25 août 2026.
- ellashaarshop.de : 10 annonces exactes sur les 10 retournées, dernières observations entre le 16 mai et le 6 juillet 2026.

Les extraits JSON exacts sont joints. Ces résultats établissent une activité Search historique des domaines, pas une diffusion aujourd’hui, pas le ciblage du mot ultraschallreiniger, pas la publicité du modèle ADC-4830. Le total flou 50 062 d’Ultraschall-Welt ne doit pas être attribué au domaine. Coût : 20 crédits TrendTrack ; solde retourné 2 634.

## Station météo : demande et deux sources concrètes

Wetterstation : 27 100 recherches mensuelles DE dans le lot initial Allemagne. Le mot couvre plusieurs gammes, pas uniquement les stations 7-en-1.

API AliExpress pays DE, EUR, bénéfices personnels retirés :

| Offre | SKU EU | Prix article | Fret | Total affiché | Délai estimé | Stock déclaré |
|---|---|---:|---:|---:|---|---:|
| WS0310, 1005009672098357 | 12000049825403338 | 97,99 € | 1,99 € | 99,98 € | 37–40 jours, CN | 11 |
| WS0366, 1005009419604608 | 12000051191013588 | 119,39 € | 1,99 € | 121,38 € | 37–40 jours, CN | 78 |

Le mot EU est la variante commerciale de l’offre ; ce n’est pas une preuve indépendante de conformité ni un entrepôt européen. Les prix de recherche minimum incluaient des variantes non EU : ne pas les reprendre. Les deux sources sont écartées pour une logistique rapide. Ne pas convertir le volume élevé en recommandation de lancement.

## Contrôle de prix public root

La recherche Sainlogic renvoie l’ancien FT0300 à 168,95 € sur /de-eu/, avec mention de rupture. Le contrôle direct de son endpoint produit .js retourne 404 : pas de prix actuel confirmé retenu. La collection actuelle indexe SA68 Plus et SA9 autour de 172,95 €, mais ces modèles diffèrent des références AliExpress ci-dessus. Aucun calcul de marge entre modèles supposés identiques n’est validé.

Sources publiques : https://www.sainlogic.com/de-eu/products/sainlogic-wifi-weather-stations-ft0300 ; https://www.sainlogic.com/de-eu/collections/all. Rapports API : ali-de-wetter-search.json, ali-de-wetter-details.json, ali-de-wetter-freight.json.

## Relecture du retour Luna

Le rapport luna-station-meteo/RESULTAT.md est terminé. Ne pas généraliser sa conclusion « aucune boutique Shopify démontrée » : son contrôle porte notamment sur sainlogic.de, qui redirige vers Froggit, alors que la marque dispose aussi de sainlogic.com. Root a vérifié un endpoint produit Shopify fonctionnel sur shop.ecowitt.com ; c’est un configurateur à prix initial nul, pas un kit complet gratuit ni un prix comparable. Le prix nul est exclu du tableau.

La ligne Otto est renvoyée en qualification : le libellé rapporté 5-in-1 Beaufort et l’URL mentionnant 7-in-1 Solar WLAN 4Cast ne correspondent pas clairement. Le montant de 149 € n’est pas validé pour une comparaison précise. Les prix Bresser et Vevor restent des relevés du worker, non des sources d’achat contrôlées par root. La conclusion exploitable de cette passe reste le délai API de 37–40 jours des deux références fournisseur contrôlées.

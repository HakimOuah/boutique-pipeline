# Concurrents et prix cible — onglets Carport et Pergola aluminium (09/09/2026)

Demande Hakim : pour chaque produit conservé après nettoyage des deux onglets (produits avec sourcing AliExpress), trouver un ou deux concurrents qui vendent exactement ce produit, afin de fixer le prix cible.

Sources :
- Google Shopping France via Chrome (`parse_shop.py` → `shop-raw.jsonl`, 11 requêtes carport, 889 offres) — interrompu par un CAPTCHA Google après 12 requêtes, non contourné.
- Google Shopping France via DataForSEO Merchant API (`dfs-shopping.json`, 51 requêtes × 40 offres, 0,051 $) — source principale ; liens marchands résolus par `merchant/google/sellers` sur les fiches retenues (`sellers.json`).
- Règles de choix : `REGLES-SELECTION.md` (comparable = boutique spécialisée sans marque-récit, sinon GSB ; marketplaces et marques-récit évitées).
- Sélection par deux agents Sonnet : `selection-carport.json`, `selection-pergola.json`.
- `merge_prix.py` : prix cible proposé = juste sous le comparable retenu (voir règle dans le script), écriture des colonnes L–O (concurrents) et I (prix cible proposé) des deux onglets.

## Décision Hakim (09/09/2026, après lecture)

Pergola : mise en pause (onglet en statut « En pause », rien d'autre touché). Carport : on affiche des prix même au-dessus des GSB, différenciation par photos et copy. Règle finale (2e retour Hakim) : prix cible I = **max( marge 35 % sur le prix HT = 1,2 × coût livré / 0,65 arrondi au 9 supérieur ; juste sous le concurrent de référence le moins cher = −5 % arrondi en 9 )**. Référence = comparables tente-garage quand la fiche AliExpress en est une, sinon les concurrents exacts. Une même fiche AliExpress reçoit un seul prix quel que soit le mot-clé (`prix-cible-carport.json` ; `prix-cible-carport-35pct.json` = étape intermédiaire à 35 % seul). Les concurrents exacts (L–O) et les comparables tentes-garages (P–Q) restent affichés pour situer ces prix.

# Concurrents et prix cible — onglets Carport et Pergola aluminium (09/09/2026)

Demande Hakim : pour chaque produit conservé après nettoyage des deux onglets (produits avec sourcing AliExpress), trouver un ou deux concurrents qui vendent exactement ce produit, afin de fixer le prix cible.

Sources :
- Google Shopping France via Chrome (`parse_shop.py` → `shop-raw.jsonl`, 11 requêtes carport, 889 offres) — interrompu par un CAPTCHA Google après 12 requêtes, non contourné.
- Google Shopping France via DataForSEO Merchant API (`dfs-shopping.json`, 51 requêtes × 40 offres, 0,051 $) — source principale ; liens marchands résolus par `merchant/google/sellers` sur les fiches retenues (`sellers.json`).
- Règles de choix : `REGLES-SELECTION.md` (comparable = boutique spécialisée sans marque-récit, sinon GSB ; marketplaces et marques-récit évitées).
- Sélection par deux agents Sonnet : `selection-carport.json`, `selection-pergola.json`.
- `merge_prix.py` : prix cible proposé = juste sous le comparable retenu (voir règle dans le script), écriture des colonnes L–O (concurrents) et I (prix cible proposé) des deux onglets.

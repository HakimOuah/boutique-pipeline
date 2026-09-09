# Sourcing AliExpress — arborescence carport (09/09/2026)

Objectif Hakim : une fiche AliExpress disponible en France pour chaque produit de l'onglet « Carport » du classeur d'idées de niches (39 produits uniques, `produits-a-sourcer.json`).

Méthode : identifiants récoltés sur les SERP fr.aliexpress.com (tri ventes) dans le Chrome de Hakim — requêtes carport, carport aluminium, carport bois, carport 2 voitures, abri camping car, abri voiture bois, carport adossé (`serp-*.txt`) — puis qualification par la passerelle VPS (`aliexpress_vps_gateway.py variants` / `exact --destination FR`). L'API officielle n'a pas de clé configurée (ALIEXPRESS_APP_KEY absente) ; la passerelle `search` classe par popularité et ne sert à rien sur cette catégorie.

Statuts autorisés (critères du parc) : AUCUNE OFFRE EXPLOITABLE / OFFRE TROUVÉE / FOURNISSEUR À TESTER / FOURNISSEUR RETENU POUR COMMANDE TEST (ce dernier = décision Hakim). Aucune commande, aucun message vendeur.

Constat d'entrée : aucun carport en bois sur AliExpress (seulement pergolas en pin 100×90 cm et abris-bûches) ; l'offre réelle = carports aluminium + polycarbonate « personnalisables » (186–812 €, ventes faibles, variantes « Consult before place »), tentes-garages acier (Outsunny 3×6 m 230–245 € expédié depuis la France, 4×6 m 295–398 €), abri métal acier thermolaqué 450×300 (579 €).

Résultats par lot : `sourcing-lot1.json`, `sourcing-lot2.json`, `sourcing-lot3.json` ; synthèse `SYNTHESE.md`.

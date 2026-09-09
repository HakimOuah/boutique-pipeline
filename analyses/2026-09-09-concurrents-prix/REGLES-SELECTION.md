# Règles de sélection des concurrents (prix cible) — 09/09/2026

Entrées : `dfs-shopping.json` (par requête = mot-clé produit de l'onglet, 40 offres Google Shopping France : rank_absolute, title, seller, price TTC, product_id, rating, reviews_count, delivery_info) et `produits.json` (onglet, mot-clé, prix AliExpress livré `ali_prix`).

But : pour chaque mot-clé produit, retenir **1 à 2 concurrents qui vendent exactement ce produit** (même type, même matériau, même taille/capacité, même fonction), avec leur prix, pour fixer un prix cible.

Ordre de préférence du comparable (règle du parc « se placer juste sous le comparable ») :
1. Boutique e-commerce spécialisée ou généraliste jardin sans marque-récit (Mon Abri de Jardin, OOGarden, Perenza, Coclic Alu, Abris Jardin Azur, Jardins Animés, Tuinmaximaal, Jimmyatwork, Maderland, Ma Pergola Bois, Pergola de France, France Abris, Chalet de Jardin, Veepee, Sweeek, Alice's Garden, Kenzaï…). C'est le comparable n° 1 recherché.
2. Grande surface de bricolage ou enseigne (Leroy Merlin, Castorama, Brico Dépôt, Bricomarché, Lapeyre, Gamm vert…) : acceptable en concurrent n° 2 ou faute de mieux.
3. À éviter comme comparable : marketplaces (Amazon, ManoMano, Cdiscount, Leboncoin, AliExpress, eBay, Temu, Rakuten), sites de marque à récit / fabricant premium (Abrisud, Azenco, Gumax, Renson, Biossun, Palram Canopia, Trigano en direct) — ne les retenir que si aucun autre vendeur ne propose exactement le produit, en le signalant.

Exactitude :
- Un « carport alu 2 voitures » doit être un carport aluminium double (≥ 5 m de large ou « 2 voitures »/« double »), pas un carport bois ni une pergola. Un « carport 6x3 » doit faire ~6×3 m (tolérance ±10 % sur chaque dimension) ; un carport « 20 m² » entre 18 et 22 m². « camping car / caravane / fourgon » = hauteur ≥ 3 m ou mention explicite. « fermé » = parois/portes. « toit plat » explicite.
- Une « pergola bioclimatique 4x3 » doit être bioclimatique (lames orientables) en aluminium, ~4×3 m ; « adossée » = fixation murale explicite ; « électrique/motorisée » = lames motorisées ; « avec store intégré » = store zip/latéral inclus ; « vitrée » = parois vitrées coulissantes ; « pergola 4x3 aluminium » (non bioclimatique) = pergola alu 4×3 toit fixe ou toile, à défaut bioclimatique en le notant.
- Accessoires : la fiche doit être l'accessoire seul (store, rideau, moteur, ruban LED pour pergola), pas une pergola complète.
- Ignorer les fiches hors sujet (tentes-garages ou abris bâche pour un carport rigide, bois pour alu, garages fermés en dur pour un carport ouvert, etc.) sauf si le mot-clé les désigne réellement (ex. « carport fermé sur 2 côtés » peut être une tente-garage acier si c'est ce que le marché vend).
- Si aucune offre exacte : `concurrents: []` et expliquer dans `note` ce qui s'en rapproche le plus (titre, vendeur, prix) sans le retenir.

Sortie : JSON liste, un objet par requête, dans l'ordre de `requetes.json` :
```
{"q": "<mot-clé>", "concurrents": [{"title": "...", "seller": "...", "price": 1234.0, "product_id": "...", "type": "specialiste|gsb|marketplace|marque", "motif": "pourquoi c'est exactement le produit"}], "fourchette": {"min": ..., "median": ..., "max": ..., "n": <nb offres réellement pertinentes>}, "note": "..."}
```
Le `product_id` est copié tel quel (chaîne). Aucune visite de site, aucune autre recherche : uniquement le JSON fourni. Vérifier que le fichier de sortie se charge et compte autant d'objets que de requêtes du lot.

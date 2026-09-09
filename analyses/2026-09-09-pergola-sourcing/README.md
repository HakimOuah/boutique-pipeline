# Sourcing AliExpress — arborescence pergola bioclimatique / aluminium (09/09/2026)

Objectif Hakim : une fiche AliExpress disponible en France pour chaque produit de l'onglet « Pergola aluminium » du classeur d'idées de niches (48 lignes produit, 44 produits uniques, `produits-a-sourcer.json`, colonne `row` = ligne de l'onglet).

Méthode identique au dossier carport (`../2026-09-09-carport-sourcing/`) : identifiants récoltés sur les SERP fr.aliexpress.com (tri ventes) dans le Chrome de Hakim — `serp-pergola.txt` (pergola bioclimatique, pergola aluminium, adossée, 6x4, motorisée, imitation bois) et `serp-accessoires.txt` (store latéral, rideau, moteur, pied/poteau, éclairage, petite taille) — puis qualification par la passerelle VPS (`boutique-pipeline/codex-chasse-clusters/tools/aliexpress_vps_gateway.py variants <id>` / `exact <id> --destination FR --property "<nom>=<valeur brute>"`).

Statuts autorisés (critères du parc) : AUCUNE OFFRE EXPLOITABLE / OFFRE TROUVÉE / FOURNISSEUR À TESTER / FOURNISSEUR RETENU POUR COMMANDE TEST (ce dernier = décision Hakim). Aucune commande, aucun message vendeur.

Pièges connus : « Personnalisable » + prix « au mètre carré » (One square meter) = prix non exploitable ; variante « Consult before place » / « Sample » / demi-prix = FOURNISSEUR À TESTER ; chiffres SERP non confirmés en fiche = à jeter.

Résultats par lot : `sourcing-lot1.json` (collection pergola aluminium + bioclimatique 4x3), `sourcing-lot2.json` (tailles 6x4, 6x3, 3x3, 4x4, 5x3, autres tailles), `sourcing-lot3.json` (autoportante, rétractable, motorisée, manuelle, fermée, sur mesure, accessoires) ; synthèse `SYNTHESE.md` ; écriture G/H/K de l'onglet par `merge.py`.

## Résultat (09/09/2026, 3 lots Sonnet, 152 appels outil)

Sur 48 lignes produit (44 uniques) : **13 OFFRE TROUVÉE, 14 FOURNISSEUR À TESTER, 21 AUCUNE OFFRE EXPLOITABLE** (détail dans `SYNTHESE.md`, onglet écrit en G/H/K).

Constats structurants :
- L'offre AliExpress en pergola bioclimatique est faite de fiches « personnalisables » de quelques ateliers chinois (Star Alu / One Alu / ONEHAPPY / Homalux…) : prix 1 700–7 700 € TTC livré, délais 17–36 j en UPS ou 61–76 j en fret vendeur sans suivi, ventes réelles faibles (1–186), magasins souvent sans note.
- Schéma récurrent « demi-prix » : `offer_sale_price` = exactement 50 % du `sku_price` sur toutes les variantes, sans remise affichée. Harmonisé par `merge.py` en FOURNISSEUR À TESTER (le lot 1 le comptait en OFFRE TROUVÉE). Autres pièges : « Consult before place », « One square meter », « Deposit », « Sample ».
- Tailles réellement confirmables en propriété : 3x3, 3x4, 4x3, 4x4, 6x4 (écran zip) ; aucune fiche 2x3, 3x2, 5x3, 5x4, 4x5, 3x5, 7x4, 8x4 ; « adossée/murale » confirmée seulement en 3x3, 3x4 et 4x4 (ONEHAPPY 1005010806775126). Aucun fini imitation bois, aucune pergola solaire.
- Seule offre à logistique européenne : pergola 4x3 bioclimatique expédiée d'un stock France (1005012028935070, 1 119,86 € livré en 2–6 j) et store zip latéral expédié de France (1005012246631340, 106 €).
- Accessoires : store, rideau, moteur tubulaire, ruban LED trouvés en génériques ; poteau alu seul, lames de rechange, rehausse de pied et plot/platine à sceller introuvables.

Lecture : la niche se vend à prix élevé mais l'approvisionnement AliExpress est fragile (fabrication à la commande, délais longs, prix à reconfirmer). Décision GO/NO-GO et éventuelle commande test = Hakim.

Nettoyage de l'onglet « Pergola aluminium » (09/09/2026, demande Hakim) : 21 lignes produit sans sourcing retirées (les AUCUNE OFFRE EXPLOITABLE, substitut de taille voisine compris) et 2 collections vidées (6x4, 5x3). L'onglet passe de 65 à 42 lignes (rows 8–49), 27 lignes produit conservées. Ce dossier garde la trace des 48 lignes testées.

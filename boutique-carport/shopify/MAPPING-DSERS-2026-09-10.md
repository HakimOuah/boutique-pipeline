# Mapping DSers — Sous Abri (10/09/2026)

Boutique Shopify `zpeubn-i2` (sousabri.fr). 10 produits, une variante chacun. À lier dans DSers (Mapping › Basic) au listing AliExpress ci-dessous, avec la variante et l'entrepôt qui ont servi au calcul du prix (colonne « variante retenue », relevée par l'API AliExpress le 09/09).

| # | Produit Shopify | SKU | Prix | Listing AliExpress | Variante retenue | Expédié depuis | Coût Ali (09/09) |
|---|---|---|---|---|---|---|---|
| 1 | Carport acier thermolaqué 4,5 x 3 m (`carport-acier-thermolaque-4-5x3`) | SA-ACIER-450 | 1069 € | https://fr.aliexpress.com/item/1005012344715751.html | Couleur=noir (taille 450x300x250cm) | PL | 578.85 € |
| 2 | Carport aluminium autoportant, toit arqué (`carport-aluminium-autoportant`) | SA-ALU-AUTO-6x6 | 1199 € | https://fr.aliexpress.com/item/1005009961706626.html | {'Couleur': 'Gris foncé', 'Taille': '3x3 pieds (valeur renvoyée: 6x6m)'} | CN | 649.39 € |
| 3 | Carport camping-car aluminium, toit cintré (`carport-camping-car-aluminium`) | SA-ALU-CC-6x38 | 1939 € | https://fr.aliexpress.com/item/1005011994406763.html | {'Couleur': 'BLANC', 'Taille': '3x3 pieds (valeur renvoyée: 6x6m)'} | CN | 1047.99 € |
| 4 | Tente-garage Outsunny 3 × 6 m, hauteur réglable (`tente-garage-3x6-outsunny`) | SA-TG-3x6-OUT | 459 € | https://fr.aliexpress.com/item/1005012736849383.html | Couleur=BLANC ; Expédié depuis=France | FR | 244.88 € |
| 5 | Tente-garage 4 × 6 m, doubles portes enroulables (`tente-garage-4x6-portes-enroulables`) | SA-TG-4x6-PE | 549 € | https://fr.aliexpress.com/item/1005010670791375.html | Expédié depuis=Allemagne | DE | 295.12 € |
| 6 | Tente-garage 4 × 6 m fermée, fenêtres maille (`tente-garage-4x6-fenetres`) | SA-TG-4x6-FEN | 609 € | https://fr.aliexpress.com/item/1005012384075437.html | Expédié depuis=Allemagne | DE | 328.99 € |
| 7 | Tente-garage 4 × 7,6 m pour camping-car, caravane (`tente-garage-4x7-6-camping-car`) | SA-TG-4x76 | 749 € | https://fr.aliexpress.com/item/1005012322112744.html | Couleur=Rose (Grey) / Expédié depuis=Allemagne / Taille=10x8 pieds (affiché 13x25 ft) | DE | 400.91 € |
| 8 | Tente-carport fermée sur deux côtés, portes zip (`tente-carport-fermee-2-cotes`) | SA-TG-FERM2 | 719 € | https://fr.aliexpress.com/item/1005012904297579.html | Couleur=BLANC / Expédié depuis=Allemagne | DE | 386.13 € |
| 9 | Tente de garage mobile 3 × 3 m, porte enroulable (`tente-garage-mobile-3x3`) | SA-TG-3x3 | 349 € | https://fr.aliexpress.com/item/1005012942086535.html | Expédié depuis=Allemagne | DE | 184.69 € |
| 10 | Tente-garage 4 × 6 m, passage traversant (`tente-garage-4x6-double-porte-volet`) | SA-TG-4x6-VOL | 739 € | https://fr.aliexpress.com/item/1005013014844719.html | Couleur=White+Iron+Waterproof Fabric / Expédié depuis=Allemagne | DE | 398.03 € |

Règles : dans DSers, choisir exactement la variante et l'entrepôt de la colonne « variante retenue » (un autre entrepôt change le prix et le délai) ; si le listing a évolué, noter ici la variante réellement liée et recalculer la marge (`../analyses/2026-09-09-concurrents-prix/prix-cible-carport.json`). Après le mapping, désactiver dans DSers la synchronisation du stock et le « push » de stock vers Shopify (règle Merchant Center, checklist NoBrand §2.C) : le stock est fixé à 50 unités suivies, vente autorisée en rupture.

Les 3 pages devis (Star Alu / ONE ALU, listings 1005012158685405, 1005012143140387, 1005012231765595) ne sont pas des produits Shopify : pas de mapping.
## Mapping réalisé dans DSers (10/09/2026, Chrome de Hakim)

Les 10 produits sont liés (onglet « Unmapped » = 0), en mapping Basic, règle de synchronisation « Ship to » = France sur chaque produit (la valeur par défaut était États-Unis : les listings expédiés d'Allemagne ou de France refusaient de s'attacher tant que la règle n'était pas sur France). Import list : 10 listings, langue anglaise (la langue française déclenche une offre payante, refusée), règle France.

| # | Produit Shopify | Variante réellement liée | Coût DSers (FR, 10/09) | Écart avec le coût de calcul |
|---|---|---|---|---|
| 1 | Carport acier 4,5 × 3 | 450x300x250 cm, expédié de Pologne | 592,64 – 698,76 € (fourchette toutes variantes du listing) | coût de calcul 578,85 € ; à relire sur la variante à la première commande |
| 2 | Carport alu autoportant | Size 6x6m, Dark Grey, Chine | 15,92 – 636,81 € (fourchette listing) | calcul 649,39 € ; variante 6x6m à vérifier à la commande |
| 3 | Carport camping-car alu | **6x3.8m Brown** (le listing ne propose pas 6x6m blanc) | 15,81 – 1027,78 € (fourchette listing) | calcul fait sur 6x6m blanc à 1047,99 € : **taille liée différente, à trancher (fiche 6 × 3,8 ou autre listing)** |
| 4 | Tente-garage Outsunny 3 × 6 | Blanc, expédié de France | 250,72 € | calcul 244,88 € (+5,84 €) |
| 5 | Tente-garage 4 × 6 portes enroulables | Expédié d'Allemagne | 302,14 € | calcul 295,12 € (+7,02 €) |
| 6 | Tente-garage 4 × 6 fenêtres maille | Expédié d'Allemagne | 311,78 € | calcul 328,99 € (−17,21 €) |
| 7 | Tente-garage 4 × 7,6 camping-car | Grey, 13x25 ft, Allemagne | 410,45 € | calcul 400,91 € (+9,54 €) |
| 8 | Tente-carport fermée 2 côtés | Blanc, Allemagne | 395,33 € | calcul 386,13 € (+9,20 €) |
| 9 | Tente mobile 3 × 3 | Expédié d'Allemagne | 181,06 € | calcul 184,69 € (−3,63 €) |
| 10 | Tente-garage 4 × 6 passage traversant | White + Iron + Waterproof Fabric, Allemagne | 407,52 € | calcul 398,03 € (+9,49 €) |

Les écarts de quelques euros sont des variations de change et de prix AliExpress entre le 09 et le 10/09 : les marges restent celles de `prix-cible-carport.json` à ±3 %. Les trois produits à fourchette (1, 2, 3) affichent la fourchette du listing entier sur la carte DSers ; le coût réel de la variante liée n'apparaît qu'à la commande. Stock : DSers ne pousse rien vers Shopify (réglage « Do Nothing » vérifié) ; les 50 unités suivies restent celles fixées par l'API.

Recette d'interface DSers (nouveau tiroir « Manage Suppliers For Products ») : icône mapping sur la carte (souvent deux clics) → drapeau à gauche du bouton OK → règle « Ship to » France (taper France + Entrée, puis Save, parfois deux clics) → coller le lien, OK → Basic → pour chaque ligne, choisir l'option puis la variante (clavier Bas + Entrée), ne jamais appuyer sur Échap (ferme le tiroir) → Save → CONFIRM.

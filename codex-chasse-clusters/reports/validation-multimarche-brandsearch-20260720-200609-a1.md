# Validation multi-marchés BrandSearch — run 20260720-200609 · a1

- Date : 20 juillet 2026
- Marchés minés : France, Allemagne, Royaume-Uni, Espagne, Italie, Pays-Bas, Belgique
- Objectif : identifier 20 à 30 produits ou niches grand public déjà éprouvés par des entreprises qui achètent du Google Ads, puis les filtrer par demande Search, prix, SERP, tendance et faisabilité de sourcing.
- Prix moyen boutique recherché : 85–400 EUR, traduit en 97,20–457,40 USD sur la base EUR/USD 1,1435 du 17 juillet 2026.
- Règle de volume : 10 000 recherches mensuelles adressables dans **un même pays**. Les volumes de plusieurs pays ne sont jamais additionnés pour fabriquer un passage de seuil.

## 1. Ce qui a été réellement observé

### BrandSearch

Les sept extractions ont imposé simultanément :

1. pays d'origine local et livraison vers ce même marché ;
2. au moins une Google Ads active ;
3. zéro Meta Ads active ;
4. prix moyen boutique compris entre 97,20 et 457,40 USD ;
5. tri initial par volume de Google Ads.

| Marché | Entreprises qui passent les filtres |
|---|---:|
| France | 32 |
| Allemagne | 38 |
| Royaume-Uni | 29 |
| Espagne | 27 |
| Italie | 46 |
| Pays-Bas | 23 |
| Belgique | 21 |
| **Total dédupliqué** | **216** |

La liste brute filtrée est conservée dans `runs/20260720-200609/brandsearch-entreprises-filtrees.json` et sera reprise intégralement dans l'onglet « Entreprises 216 » du classeur final.

### SEMrush

Les volumes ci-dessous proviennent du Keyword Magic Tool dans la base du pays indiqué. Les requêtes multi-mots ambiguës ont été contrôlées en **expression exacte** ; les composés allemands simples ont été lus sur leur cluster local. Les résultats larges anglais précédant le passage en expression exacte ont été rejetés et ne sont pas utilisés.

### Google Trends

Pour les deux groupes accessibles avant limitation Google, la variation compare la moyenne des 52 dernières semaines à celle des 52 semaines précédentes, sur une fenêtre de cinq ans. Google Trends est un indice relatif, pas un volume absolu.

### AliExpress

Le sourcing n'a pas pu être exécuté : Chrome a renvoyé exactement `Browser Use rejected this action due to browser security policy` lors de l'ouverture d'une nouvelle recherche AliExpress. Conformément au contrat du pipeline, aucun fournisseur, prix livré, délai ou stock n'est inventé. Les candidats qui passent le marché sont donc notés `RETENU_MARCHE_A_SOURCER`, avec requêtes manuelles prêtes.

## 2. Radar final — 30 produits ou niches

Légende :

- **VALIDÉ** : marché qualifié, à sourcer manuellement ; ce n'est pas une autorisation de lancement.
- **À CREUSER** : preuve de marché réelle, mais une réserve importante empêche le passage immédiat au sourcing prioritaire.
- **EXCLU** : le sous-produit propre est sous le seuil, ou un risque structurel ferme la piste.

| # | Statut | Produit / niche | Marché et volume SEMrush | Entreprise témoin BrandSearch | Preuve de marché observée | Point décisif |
|---:|---|---|---|---|---|---|
| 1 | **VALIDÉ** | Housse de voiture sur mesure, intérieure/extérieure | FR 105 710 ; UK 64 460 | ukcustomcovers.com ; directcarcovers.com | 28 819 et 5 718 visites/mois ; 40 Google Ads actives chacune ; 0 Meta | Prix UK observé dès 121,94–211,27 GBP ; Trends FR +7,2 %, UK +40,6 %. Catalogue véhicule/année et retours à verrouiller. |
| 2 | **VALIDÉ** | Fauteuil suspendu avec pied | FR 72 520 ; DE 236 300 | lasiesta.com | 139 613 visites/mois ; prix moyen 274,62 USD ; 40 Google ; 0 Meta | Trends FR −3,3 % mais forte saisonnalité ; produit 290–350 EUR observé. Colis, charge, stabilité et pièces critiques. |
| 3 | **VALIDÉ** | Évier de cuisine inox/granit avec robinet | FR 73 800 ; IT 255 630 | evhoc.it | 9 866 visites/mois ; prix moyen 326,40 USD ; 40 Google ; 0 Meta | Trends FR +18,7 % ; SERP 91,50–597 EUR. Dimensions, inox, bonde, robinet, casse et raccords à auditer. |
| 4 | **VALIDÉ** | Housses de sièges auto sur mesure | UK 118 480 ; FR 6 550 | carfurnisher.com ; ukcustomcovers.com | 11 643 et 28 819 visites/mois ; prix moyens 354,08 et 131,26 USD | Marché pilote UK ; Trends UK +16 %. Airbags latéraux, gabarits, année/modèle et taux d'erreur à verrouiller. |
| 5 | **VALIDÉ** | Valise cabine premium 20 pouces / set compact | ES 79 620 | traveltienda.es | 8 871 visites/mois ; 29 produits ; prix moyen 213,56 USD ; 40 Google ; 0 Meta | Marché large mais planchers Amazon <60 EUR. Ne retenir qu'un angle premium : dimensions compagnies, roues remplaçables, serrure TSA, pièces. |
| 6 | **VALIDÉ** | Haltères réglables 20–40 kg | FR 11 090 ; ES 13 930 | gorillasports.es ; maniboom.es | 7 431 et 4 298 visites/mois ; prix moyens 159,59 et 98,14 USD ; 40 Google ; 0 Meta | Volume juste au-dessus du seuil. Charge réelle, verrouillage, chutes, pièces et colis lourd à tester. |
| 7 | **VALIDÉ** | Parure de lit premium / hôtelière | UK 19 990 | beddingenvy.co.uk | 100 422 visites/mois ; prix moyen 329,02 USD ; 40 Google ; 0 Meta | Trends UK +41,8 %. Concurrence de marques ; matière, grammage, tailles, retrait au lavage et retour hygiène à prouver. |
| 8 | **VALIDÉ** | Meuble-cage pour chien / double niche intérieure | UK 13 280 | lordsandlabradors.co.uk | 79 059 visites/mois ; prix moyen 263,97 USD ; 40 Google ; 0 Meta | Trends UK +18,2 % ; offre Aosom à 234,99 GBP. Taille, charge, espacement des barreaux, ventilation, stabilité et colis à auditer. |
| 9 | **À CREUSER** | Panneau mural décoratif de douche | FR 13 510 ; DE 46 220 | duschrückwand-platten.de | 18 006 visites/mois ; prix moyen 424,07 USD ; 40 Google ; 0 Meta | Trends FR +11,9 %, mais Leroy Merlin affiche 1 639 résultats. Format, découpe, adhésif, étanchéité et avarie transport à différencier. |
| 10 | **À CREUSER** | Vasque de salle de bain design à poser | FR 368 610 | lemondedubain.com | 55 560 visites/mois ; prix moyen 452,84 USD ; 40 Google ; 0 Meta | Demande massive et prix marché 50–500 EUR, mais céramique fragile, marques fortes et comparabilité immédiate. |
| 11 | **À CREUSER** | Salon de jardin en résine tressée | FR 15 450 ; UK 122 080 | rattantree.com | 101 487 visites/mois ; 32 produits ; prix moyen 172,40 USD ; 40 Google ; 0 Meta | Trends FR −9,7 %, UK −3,9 %, très saisonnier. Planchers 99–200 EUR et logistique volumineuse compriment la marge. |
| 12 | **À CREUSER** | Coussin chauffant premium infrarouge / batterie | FR 47 060 ; BE 12 750 ; NL 69 040 | opoggi.com | 38 visites/mois ; 11 produits ; prix moyen 217,97 USD ; 40 Google ; 0 Meta | Trends FR +4,2 %, très hivernal. Génériques dès 29,95 EUR : il faut une preuve premium sans allégations médicales et conformité électrique complète. |
| 13 | **À CREUSER** | Receveur de douche SMC effet pierre | FR 195 140 | lemondedubain.com | 55 560 visites/mois ; prix moyen 452,84 USD ; 40 Google ; 0 Meta | Médiane observée env. 146 EUR et Aurlane très présent. Formats, bonde, planéité, casse et coût retour sévères. |
| 14 | **À CREUSER** | Radiateur de salle de bain / sèche-serviettes design | DE 102 650 ; FR 6 290 | heizkoerper.shop | 7 986 visites/mois ; 46 produits ; prix moyen 354,07 USD ; 40 Google ; 0 Meta | Marché pilote Allemagne. Puissance, hydraulique/électrique, raccords, normes, installation et SAV technique à verrouiller. |
| 15 | **À CREUSER** | Brasero / foyer de jardin premium | DE 42 320 ; FR 8 180 | gardenflare.com | 2 268 visites/mois ; 24 produits ; prix moyen 188,26 USD ; 40 Google ; 0 Meta | Demande allemande suffisante ; saisonnalité, feu, stabilité, matériaux, fumées, réglementation locale et poids à contrôler. |
| 16 | **À CREUSER** | Kit grillage de volière / enclos animal | DE 13 300 | drahtexpress.de | 15 544 visites/mois ; 47 produits ; prix moyen 115,98 USD ; 40 Google ; 0 Meta | Volume juste. Produit commoditisé, coupant et lourd ; le bundle doit prouver maille, diamètre, galvanisation, fixations et surface. |
| 17 | **À CREUSER** | Paroi / cabine de douche | ES 40 610 | entornobano.com | 13 186 visites/mois ; prix moyen 412,05 USD ; 40 Google ; 0 Meta | Demande forte, mais verre, dimensions, réversibilité, montage, conformité et casse rendent le dropshipping fragile. |
| 18 | **À CREUSER** | Barres de toit / galerie spécifique véhicule | UK 189 650 | roofrack.co.uk | 4 988 visites/mois ; prix moyen 440,20 USD ; 40 Google ; 0 Meta | Très gros volume, mais compatibilité, charge, fixation, bruit, sécurité routière et responsabilité produit sont critiques. |
| 19 | **À CREUSER** | Dashcam 2/3 canaux avec kit câblage | UK 378 800 | dashvision.co.uk | 10 486 visites/mois ; prix moyen 97,46 USD ; 40 Google ; 0 Meta | Marché massif mais très comparable et dominé par marques. Capteur, plaque lisible, app, firmware, stationnement et SAV à prouver. |
| 20 | **À CREUSER** | Kit de suivi de consommation électrique | NL 11 290 ; BE 5 660 | easynrj.com | 657 visites/mois ; 9 produits ; prix moyen 231,68 USD ; 40 Google ; 0 Meta | Signal juste aux Pays-Bas, acteur encore petit. Précision, installation, tension, app/cloud, RED/EMC et sécurité électrique à auditer. |
| 21 | **À CREUSER** | Ferme-porte hydraulique premium | FR 51 400 ; NL 28 650 | jadesafety.com | 3 477 visites/mois ; prix moyen 121,14 USD ; 40 Google ; 0 Meta | Demande nette, mais grande part du marché sous 85 EUR et forte composante pro. Angle possible : kit complet réglable, gabarit et vidéo de pose. |
| 22 | **À CREUSER** | Draisienne premium bois/métal | FR 14 910 ; UK 105 340 | bobbinbikes.com | 67 937 visites/mois ; 114 produits ; prix moyen 130,19 USD ; 40 Google ; 0 Meta | Marché réel ; sécurité enfant, hauteur selle, pneus, stabilité, substances, marquage et responsabilité à examiner avant sourcing. |
| 23 | **À CREUSER** | Tapis de sol auto premium / sur mesure | FR 11 350 famille ; 6 480 explicite sur mesure | omacshop.fr | 14 080 visites/mois ; prix moyen 174,37 USD ; 40 Google ; 0 Meta | La famille passe de peu, mais le sous-produit sur mesure reste sous 10K. Gabarits, clips, odeur, matière et erreurs de modèle sont le cœur du risque. |
| 24 | **À CREUSER** | Plaque funéraire personnalisable | FR 69 200 famille ; 7 860 explicite personnalisée | plaquedeces.fr | 24 381 visites/mois ; prix moyen 100,71 USD ; 40 Google ; 0 Meta | Trends FR +5,6 % ; prix 56–120+ EUR. Le modèle repose sur personnalisation et fabrication locale, pas sur un simple produit générique AliExpress. |
| 25 | **EXCLU** | Grille chien / séparation coffre spécifique véhicule | UK 5 400 | travall.de | 9 755 visites/mois ; prix moyen 139,58 USD ; 40 Google ; 0 Meta | Entreprise réelle, mais sous-produit Search propre sous 10K et matrice de compatibilité lourde. |
| 26 | **EXCLU** | Écran de projection motorisé | DE 2 820 ; FR 1 580 | esmart.de | 8 925 visites/mois ; 64 produits ; prix moyen 367,35 USD ; 40 Google ; 0 Meta | Acteur prouvé, mais demande générique du sous-produit trop faible pour la boucle volume-first. |
| 27 | **EXCLU** | Kit graphique complet motocross | DE 960 ; autocollants moto larges 19 100 | arider.com | 119 004 visites/mois ; prix moyen 158,84 USD ; 40 Google ; 0 Meta | La famille autocollants passe, mais le kit graphique complet propre reste sous 1 000 et dépend de milliers de modèles/marques. |
| 28 | **EXCLU** | Toilette portable de camping | FR 8 970 | casambu.com | 17 119 visites/mois ; prix moyen boutique 382,62 USD ; 40 Google ; 0 Meta | Sous le seuil malgré la formulation large ; Trends −6,5 %. Hygiène, retour et pièces accentuent le risque. |
| 29 | **EXCLU** | Planche à découper en titane | FR 2 640 | titanecook.com | 17 555 visites/mois ; prix moyen 119,28 USD ; 40 Google ; 0 Meta | Trends +100 % sur une base minuscule ; volume absolu insuffisant et matériau/authenticité à démontrer. |
| 30 | **EXCLU** | Kit HDMI sans fil | NL 1 210 | marmitek.com | 50 011 visites/mois ; prix moyen 120,10 USD ; 40 Google ; 0 Meta | Marque forte mais demande générique propre trop faible ; latence, HDCP, résolution, portée et SAV technique. |

## 3. Priorité de sourcing manuel

### Priorité 1

1. `custom fit car cover waterproof breathable make model year EU warehouse`
2. `fauteuil suspendu avec pied résine tressée 150 kg entrepôt Europe`
3. `304 stainless kitchen sink waterfall faucet set drain basket EU warehouse`
4. `custom fit car seat cover full set side airbag compatible EU warehouse UK`

### Priorité 2

5. `premium carry on luggage 20 inch TSA removable wheels EU warehouse Spain`
6. `adjustable dumbbell pair 24kg 40kg safety lock EU warehouse`
7. `luxury hotel bedding set cotton bamboo king size EU warehouse UK`
8. `wood dog crate furniture large double door removable tray EU warehouse UK`

### Requêtes conditionnelles orange

- `shower wall panel aluminium composite 90x210 waterproof EU warehouse`
- `countertop ceramic bathroom basin design EU warehouse`
- `SMC shower tray stone effect drain 90x120 EU warehouse`
- `bathroom radiator towel warmer 1200x500 connection set EU warehouse Germany`
- `outdoor fire pit corten steel spark guard EU warehouse Germany`
- `aviary wire mesh galvanized roll fixing kit EU warehouse Germany`
- `shower enclosure 8mm tempered glass reversible EU warehouse Spain`
- `roof rack cross bars vehicle specific TUV EU warehouse UK`
- `3 channel dash cam parking mode hardwire kit EU warehouse UK`
- `home energy monitor smart meter DIN app EU warehouse Netherlands`
- `hydraulic door closer adjustable EN1154 full installation kit EU warehouse`
- `premium balance bike adjustable seat pneumatic tires EU warehouse`

## 4. SERP et prix — constats utiles

- Les housses auto présentent plusieurs spécialistes et une vraie prime au sur-mesure : Covers & All UK affiche environ 121,94 à 211,27 GBP selon véhicule ; Bancarel affiche 159,80 à 390,15 EUR pour les housses de sièges.
- Les panneaux de douche ont une demande suffisante, mais la SERP comporte de très grands catalogues : Leroy Merlin annonce 1 639 résultats et Castorama expose des offres autour de 112 à 500 EUR.
- Les salons résine tressée ont un plancher agressif : de nombreuses offres démarrent autour de 99 à 200 EUR, alors que les ensembles premium montent au-delà de 500–1 000 EUR.
- Les éviers ont une vraie tranche 85–400 EUR : Lapeyre expose des références de 91,50 à 597 EUR, avec plusieurs offres entre 139 et 399 EUR.
- Les coussins chauffants génériques démarrent autour de 29,95 EUR. Le prix moyen élevé d'OPOGGI ne suffit donc pas à valider un générique ; seul un produit premium objectivement différent mérite une suite.
- Les plaques personnalisées sont très fragmentées et souvent fabriquées localement : France Tombale affiche des modèles de 56 à 120 EUR et plus.
- Les meubles-cages pour chien ont une tranche premium réelle : Aosom UK affiche un double meuble-cage à 234,99 GBP.
- Les receveurs de douche ont une médiane observée proche de 146 EUR, mais Aurlane concentre une grande partie de l'offre accessible.

## 5. Google Trends — résultats exploitables

| Marché | Terme | Variation 52 sem. / 52 sem. précédentes | Lecture |
|---|---|---:|---|
| FR | fauteuil suspendu | −3,3 % | Stable à légèrement baissier, très saisonnier |
| FR | panneau mural douche | +11,9 % | Hausse modérée |
| FR | housse voiture | +7,2 % | Stable-haussier, peu saisonnier |
| FR | salon de jardin résine tressée | −9,7 % | Repli et saisonnalité très forte |
| FR | évier cuisine | +18,7 % | Hausse nette, peu saisonnier |
| FR | coussin chauffant | +4,2 % | Stable, très hivernal |
| FR | plaque funéraire | +5,6 % | Stable-haussier |
| FR | toilette portable | −6,5 % | Légère baisse |
| FR | planche à découper titane | +100 % | Base quasi nulle : ne compense pas le faible volume |
| FR | routeur wifi portable | −21,5 % | Faible et en baisse |
| UK | car cover | +40,6 % | Hausse forte |
| UK | car seat covers | +16,0 % | Hausse nette |
| UK | luxury bedding | +41,8 % | Hausse forte, indice relatif faible |
| UK | dog crate furniture | +18,2 % | Hausse nette, indice relatif faible |
| UK | rattan garden furniture | −3,9 % | Stable à légèrement baissier, saisonnier |

L'analyse Trends allemande reste **MANQUANTE** : Google a renvoyé une erreur 429 après les groupes France et Royaume-Uni.

## 6. OBSERVÉ / MANQUANT / HYPOTHÈSE

### OBSERVÉ

- 216 entreprises satisfont les filtres BrandSearch exacts.
- 24 des 30 lignes ont soit un cluster local supérieur à 10K, soit une famille supérieure à 10K avec une réserve explicitement documentée.
- 8 lignes forment le noyau `VALIDÉ — RETENU_MARCHE_A_SOURCER`.
- Les meilleurs transferts vers la France sont la housse voiture, le fauteuil suspendu, l'évier cuisine et, sous réserve qualitative, le panneau mural de douche.

### MANQUANT

- Aucun fournisseur AliExpress exact, prix livré, délai, stock, tension, certificat ou note vendeur n'a pu être mesuré.
- Google Trends Allemagne n'a pas pu être lu après la limitation 429.
- Le coût rendu et la marge ne sont donc calculables pour aucune ligne.

### HYPOTHÈSE

- Les huit lignes vertes peuvent devenir des dossiers fournisseur si une fiche AliExpress respecte les requêtes, les dimensions et les garde-fous indiqués.
- Les lignes orange ne passent en vert qu'après résolution du risque principal, pas simplement après découverte d'un lien fournisseur.

## 7. Verdict de campagne à ce stade

Le quota utile est atteint sans le gonfler : **8 marchés à sourcer en priorité, 16 pistes réellement éprouvées mais conditionnelles, 6 exclusions explicites**. Le prochain travail pertinent est le sourcing manuel des huit verts, puis seulement les oranges dont le risque peut être éliminé par une fiche fournisseur et un coût rendu crédible.

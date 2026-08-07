# Preuves brutes — rétrospective BrandSearch Q4 2025

- Run : `20260807-000900`
- Date de contrôle : 7 août 2026
- Marché de décision : France
- Fenêtre publicitaire historique : 15 septembre au 31 décembre 2025
- Nature de la passe : découverte rétrospective, classification concurrentielle, contrôle SEMrush France et recherche fournisseur strictement en lecture seule

## 1. État des sources

### BrandSearch

- [FAIT] Dernière date observée dans l'index des marques : `2026-07-24`.
- [FAIT] Dernière date observée dans l'index publicitaire : `2026-07-20T10:55:51`.
- [FAIT] Le corpus principal contient 93 marques uniques après déduplication.
- [FAIT] Une passe additionnelle sur les termes explicites `Christmas`, `cadeau`, `Geschenk` et `regalo` a renvoyé 45 marques uniques dans cette sous-passe ; elle recoupe partiellement le corpus principal.
- [FAIT] Les 93 marques du corpus principal sont indiquées comme Shopify par BrandSearch.
- [LIMITE] Le montant de dépense est un signal BrandSearch/Meta estimé. Il ne prouve ni chiffre d'affaires, ni marge, ni rentabilité, ni nombre de ventes.

### SEMrush

- [FAIT] Base utilisée : France, `db=fr`.
- [FAIT] Les actions SEMrush ont été exécutées séquentiellement dans la session Chrome authentifiée.
- [LIMITE] Les volumes observés en août 2026 servent à décider si un lancement France actuel est défendable. Ils ne reconstituent pas le volume mensuel exact de Q4 2025.

### AliExpress et fournisseurs

- [FAIT] Les recherches ont été limitées à la lecture seule.
- [MANQUANT] Aucun candidat de ce run n'a une fiche fournisseur DS exacte avec SKU, stock, coût rendu France et délai tous validés.
- [FAIT] Aucun ajout DSers, import Shopify, changement de prix, campagne ou dépense n'a été exécuté.

## 2. Construction du corpus BrandSearch

Filtres de la passe principale :

- pays : France, Royaume-Uni, Allemagne, Espagne, Italie, Pays-Bas, Belgique, Suède, Danemark, Norvège et Finlande ;
- niches : Arts & Crafts, Toys & Games, Pet, Home Decor, Kitchen, Sports, Home/Garden et Electronics ;
- première publicité dans la fenêtre Q4 2025 ;
- durée principalement supérieure ou égale à 14 jours ;
- dépense estimée principalement supérieure ou égale à 100 EUR ;
- tri par dépense décroissante ;
- une publicité représentative par marque avant déduplication.

Règle de classification appliquée :

1. Shopify définit le périmètre initial, mais ne discrimine pas les 93 marques puisque toutes sont Shopify.
2. La structure de la fiche produit, la profondeur du catalogue, les promotions, les délais, les slugs et les incohérences de vendeur donnent les indices opérationnels.
3. L'identité de l'entreprise tranche entre boutique probablement dropshipping et marque établie : fondateurs nommés, équipe, adresse, historique, magasin ou preuves de conception.
4. Une marque établie reste intéressante si le produit exact ou sa catégorie est observable sur AliExpress, sans pour autant devenir un fournisseur validé.

Statuts : `INDICE_DROPSHIP`, `PROBABLE_DROPSHIP`, `MARQUE_ETABLIE`, `INDETERMINE`.

## 3. Signaux publicitaires historiques retenus pour revue

| Marque / produit publicitaire | Dépense estimée | Portée observée | Période de la publicité | Classification concurrent | Lecture factuelle |
|---|---:|---:|---|---|---|
| Edubini — microscope numérique enfant | 103 768 EUR | 10,325 M | 07-11-2025 au 24-06-2026 | `MARQUE_ETABLIE` | Fondateur, équipe, GmbH et bureau à Hambourg présentés ; produit générique proche observable sur AliExpress consommateur |
| Boxbollen — jeu de boxe connecté | 84 462 EUR | 7,344 M | 17-11-2025 au 24-12-2025 | `MARQUE_ETABLIE` | Société identifiée, application propriétaire et forte dépendance au logiciel / à la marque |
| Mylky — machine à lait végétal | 21 770 EUR | 2,701 M | 11-11-2025 au 30-05-2026 | `MARQUE_ETABLIE` | Fondateurs nommés et histoire de marque ; catégorie AliExpress observée, équivalence exacte non prouvée |
| Teddyprint — mini-imprimante thermique | 11 201 EUR | 1,372 M | 07-11-2025 au 29-05-2026 | `PROBABLE_DROPSHIP` | Fiche et offre typiques de rebranding ; page équipe générique sans personnes nommées ; produits génériques similaires sur AliExpress |
| Surfin — planche d'équilibre | 10 958 EUR | 1,106 M | 22-11-2025 au 18-01-2026 | `MARQUE_ETABLIE` | Fabrication locale et offre app/cours revendiquées ; produit physique de catégorie générique |
| LindnerCo — tige refroidissante à vin | 7 550 EUR | 808 k | 10-11-2025 au 13-12-2025 | `PROBABLE_DROPSHIP` | Catalogue récent d'accessoires vin génériques, réduction forte et livraison longue |
| Tindra — table C réglable Luma | 7 066 EUR | 703 k | 04-12-2025 au 14-07-2026 | `PROBABLE_DROPSHIP` | Deux produits, fiche très promotionnelle, entrepôt international, incohérences de contact et produit générique largement distribué |
| WaggingRights — Doggo Dock | 4 743 EUR | 412 k | 20-11-2025 au 04-07-2026 | `PROBABLE_DROPSHIP` | Boutique mono-produit et vendeur `My Store`, mais fondateur / société et entrepôt UK également présentés ; hybride probable |
| MaisonPulvino — tire-bouchon à air | 4 000 EUR | 497 k | 24-11-2025 au 04-01-2026 | `PROBABLE_DROPSHIP` | Catalogue d'accessoires vin génériques et slug de produit de style AliExpress ; le produit poussé était à bas prix |
| RIWI — blocs de construction en mousse | 620 EUR | 62,5 k | une journée observée | `MARQUE_ETABLIE` | Fondateurs ingénieurs, histoire depuis 2017 et formulation propriétaire revendiquée |

Sources de contrôle des identités et pages produit :

- Tindra : <https://tindra-design.com/products/luma-multifunctional-table>
- WaggingRights : <https://waggingrights.co.uk/products/doggo-dock?variant=51430026281288>
- Mylky : <https://mylky.ch/pages/uber-uns>
- Edubini : <https://edubini.com/pages/ueber-uns>
- Teddyprint : <https://www.teddyprintpocket.fr/products/teddyprint-classic>
- LindnerCo : <https://lindnerco.se/products/vinkylare-slipp-ljummet-vin>
- Boxbollen : <https://boxbollen.com/pages/app>
- RIWI : <https://riwi-buildit.ch/pages/about-us>

## 4. Mesures SEMrush France qui changent le verdict

| Concept / requête représentative | Volume FR requête | Total mondial requête | Total variantes FR | Intention | CPC | Densité ads | Verdict demande |
|---|---:|---:|---:|---|---:|---:|---|
| Teddyprint — `imprimante thermique portable` | 1,9 k | 2,3 k | 4,1 k | Informationnelle | 0,26 USD | 1,00 | `STOP_VOLUME_EXACT` |
| Mylky — `machine à lait végétal` | 1,0 k | 1,6 k | 5,6 k | Informationnelle | 0,71 USD | 1,00 | `STOP_VOLUME_EXACT` |
| Edubini — `microscope enfant` | 8,1 k | 9,3 k | 13,7 k | Commerciale | 0,50 USD | 1,00 | `PASSE_CLUSTER`, puis échec ticket / modèle |
| WaggingRights — `siège auto chien` | 590 sur l'accentuée ; 1,9 k sur deux variantes sans accent | 850 sur l'accentuée | 9,1 k | Commerciale | 0,32 USD | 1,00 | `STOP_VOLUME_EXACT` |
| Tindra — `table de lit réglable` | 20 | 60 | 140 | n/a | 0,18 USD | 1,00 | `STOP_VOLUME_EXACT` |
| Surfin — `planche d'équilibre` | 1,6 k | 2,3 k | 5,3 k | Informationnelle | 0,21 USD | 1,00 | `STOP_VOLUME_EXACT` |

Notes de nettoyage :

- Les totaux de variantes sont des files à nettoyer, pas des additions automatiques exploitables.
- Pour `microscope enfant`, le cluster passe 10 k, mais la variante plus proche du format de poche / portable n'affiche que 1,3 k sur `microscope portable enfant`.
- Pour `siège auto chien`, le total de 9,1 k reste sous le seuil avant même de retirer les intentions adjacentes.
- Pour Tindra, la tête large `table d'appoint` ne doit pas être utilisée pour masquer le volume quasi nul du produit réglable exact.

## 5. État de la preuve AliExpress

| Concept | Preuve observée | Statut fournisseur | Ce qui manque |
|---|---|---|---|
| Microscope Edubini-like | Produits consommateur avec caractéristiques proches `1000x`, écran 2 pouces, 2 MP et 8 LED ; exemples `1005009508844715`, `1005011605162868` | `MATCH_CONSUMER_PLAUSIBLE` | Correspondance physique exacte, DS, SKU, conformité, stock, fret France |
| Teddyprint-like | Mini-imprimantes thermiques Bluetooth 58 mm à bas prix ; exemples `1005007539734894`, `1005006895753613` | `MATCH_CONSUMER_PLAUSIBLE` | Modèle exact, application, consommables, qualité, DS, fret France |
| Machine à lait végétal | Catégorie observée ; exemples `1005011712362963`, `1005009560370987` | `CATEGORIE_ALIEXPRESS_OBSERVEE` | Équivalence Mylky, matériaux alimentaires, prises, conformité, DS, fret France |
| Table Tindra-like | Même format générique 40 × 30 cm, hauteur environ 45–80 cm, observé sur plusieurs marketplaces autour de 35 EUR | `MATCH_MARKETPLACE_PLAUSIBLE` | Fiche AliExpress exacte, DS, colis, casse, coût rendu France |
| Doggo Dock | Aucun produit exact établi pendant la passe | `MANQUANT` | Tout le dossier fournisseur, ainsi que la preuve des allégations sécurité / ISOFIX |

Liens de preuve AliExpress consommateur indirecte :

- Microscope : <https://www.pricearchive.org/aliexpress.com/item/1005009508844715>
- Mini-imprimante : <https://www.pricearchive.org/aliexpress.com/item/1005007539734894>
- Machine à lait végétal : <https://www.pricearchive.org/aliexpress.com/item/1005011712362963>

## 6. Décisions brutes

| Concept | Signal Q4 | Dropship / réplicabilité | Demande France | Compatibilité 150–400 EUR | Risque / right to win | Décision |
|---|---|---|---|---|---|---|
| Microscope enfant numérique | Très fort | Marque établie + match Ali plausible | Cluster 13,7 k | Non : publicité gagnante observée autour de 39,90 EUR | Électronique enfant, SAV, produit portable spécifique à 1,3 k | `STOP_TICKET_MODELE` |
| Boxbollen | Très fort | Marque établie | Non mesurée car blocage antérieur | Bundle parfois dans la cible | App, IP, communauté et marque constituent le produit réel | `STOP_RIGHT_TO_WIN` |
| Mylky | Fort et long | Marque établie + catégorie Ali | 5,6 k | Potentiellement oui | Faible demande, alimentaire, électrique, SAV | `STOP_VOLUME_CONFORMITE` |
| Teddyprint | Fort et long | Probable dropship / rebrand | 4,1 k | Non sur le produit cœur | App, papier, SAV et commoditisation | `STOP_VOLUME_TICKET` |
| Surfin | Bon | Marque établie | 5,3 k | Oui | Catégorie concurrentielle et différenciation de marque / contenu | `STOP_VOLUME` |
| LindnerCo | Bon | Probable dropship | Non mesurée, ticket déjà éliminatoire | Non | Générique, faible ticket, saisonnier | `STOP_TICKET_COMMODITE` |
| Tindra | Bon et long | Probable dropship | 140 exact | Non face au plancher marketplace | Colis, copie facile, aucune demande exacte | `STOP_VOLUME_PRIX` |
| WaggingRights | Moyen et long | Probable hybride | 9,1 k | Potentiellement par bundle | Sécurité automobile, ISOFIX, UK-only, fournisseur exact absent | `STOP_VOLUME_RISQUE` |
| MaisonPulvino | Moyen | Probable dropship | Non mesurée, ticket déjà éliminatoire | Non pour la publicité gagnante | Le produit premium du catalogue n'est pas celui prouvé par l'ad | `STOP_TICKET_PREUVE_SCINDEE` |
| RIWI | Faible | Marque établie / produit propriétaire | Non mesurée | Potentiellement | Enfant, volume colis, formulation propriétaire | `STOP_PREUVE_ADS_LOGISTIQUE` |

## 7. Verdict de run

- `GO_SOURCING` : **0**
- `SIGNAL_MARCHE_MAIS_INCOMPATIBLE_MODELE` : **1** — microscope enfant
- `STOP` : **9**
- État final : `COMPLETE_NO_GO`

Le Q4 2025 apporte de bons exemples de créatives et d'offres, mais aucun produit de ce corpus ne justifie aujourd'hui un passage au sourcing commercial pour le modèle France / Google Ads / ticket 150–400 EUR.

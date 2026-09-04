# SOURCING — rasoir de sûreté kit débutant — 2026-09-04 23:44 CEST

Relevé AliExpress en lecture seule. Aucun panier, aucun message vendeur, aucune commande, aucun compte créé. Les prix, stocks, variantes et délais sont dynamiques : à reconfirmer au panier vers une adresse française avant toute commande test. Aucun `GO fournisseur`, aucun commentaire de verdict marché.

## Entrée

| Champ | Valeur |
|---|---|
| Candidat | A6 — rasoir de sûreté, kit débutant (rasoir + lames + accessoires) |
| État registre / dossiers | `REVIEW_PREQUALIFICATION` / `TECHNICAL_INCONCLUSIVE` — **pas** un `PASS_PREQUALIFICATION` |
| Autorisation de cette passe | Investigation demandée par Hakim : carte kanban `t_e820a54d` débloquée ; README du 04/09 : sourcing en REVIEW sans PASS rétroactif |
| Briefs lus | `analyses/2026-09-04-approfondissement-rasoir-surete/README.md` ; `analyses/2026-09-03-qualification-9-produits-pur/dossiers/A6.md` |
| Fournisseur visé | AliExpress exclusivement |
| Destination | France (compte déjà connecté, livraison affichée vers le Val-d'Oise — rue non recopiée) |

Cette fiche n’émet aucun PASS rétroactif et ne modifie pas le registre central.

## Ce que j’ai fait

Requêtes et pages ouvertes le **04/09/2026 entre 23:38 et 23:44 CEST**, navigateur réel, site `fr.aliexpress.com`.

1. PDP `https://fr.aliexpress.com/item/1005012247873064.html` (K23, magasin 1104699287).
2. PDP `https://fr.aliexpress.com/item/1005008935603476.html` (A99, même magasin) ; variante `A99-silvery` cliquée.
3. SERP `https://fr.aliexpress.com/w/wholesale-safety-razor-kit.html?SortType=total_tranpro_desc` — hors sujet (rasoirs à cartouches).
4. SERP `https://fr.aliexpress.com/w/wholesale-KAMPFE-kit.html?SortType=total_tranpro_desc`.
5. PDP `https://fr.aliexpress.com/item/1005010200339194.html` (rasoir + 5 lames annoncées).
6. PDP `https://fr.aliexpress.com/item/1005012179758523.html` (30° « doux », rasoir seul).

Modale « Mode de livraison » ouverte sur K23 et sur le kit lames. Boutons Acheter / Ajouter au panier / Message / DSers **non** utilisés. Une fenêtre DSers « LOG IN / CREATE ACCOUNT » est apparue : non exécutée.

## Résultats

### Candidat A6 — statut `FOURNISSEUR À TESTER`

Fiche la plus proche du brief « kit débutant (rasoir + lames + accessoires) » : **un SKU unique annonce rasoir + 5 lames**. Le support vu en galerie n’est **pas** confirmé dans le titre ni dans le JSON-LD. Magasin **différent** de la boutique 1104699287 apportée par Hakim.

#### Fiche retenue — confiance A (PDP lue)

| Champ | Relevé daté 04/09/2026 23:42 CEST | Source |
|---|---|---|
| URL | https://fr.aliexpress.com/item/1005010200339194.html | barre d’adresse |
| Titre page | Kampfe – rasoir Vintage à Double tranchant pour hommes, en aluminium antidérapant, pour toilettage humide et sec, pour rasage lisse, 5 lames de rechange | `h1` / JSON-LD |
| Variante visée | `20AL01-A01Y-Grey` | sélecteur SKU affiché |
| Prix de **cette** variante | **29,79 €** (TVA incluse **annoncée** ; « droits de douane calculés lors du paiement ») | prix PDP + `offers.price` JSON-LD = 29.79 EUR |
| Prix SERP antérieur | 30,19 € sur la carte `KAMPFE-kit` — **écart** avec la PDP ; on retient le prix PDP de la variante | SERP vs PDP |
| Frais de port FR | **0 €** annoncé, « AliExpress Selection Standard » / Choice | modale livraison |
| **Coût rendu observé** | **29,79 €** produit + port affiché, **avant** éventuel ajustement checkout | somme des deux lignes ci-dessus ; **non** reconfirmé au panier |
| Délai annoncé FR | **9–14 septembre 2026** soit environ **5–10 jours** calendaires depuis le 04/09 | PDP + modale |
| Transporteurs affichés | Colissimo, Colis Privé, Mondial Relay, etc. | modale |
| Pays d’expédition | **non affiché** dans la modale (logistique « gérée par AliExpress », Choice / points relais) | modale ; pas d’invention CN/UE |
| Stock annoncé | **12** disponibles | PDP |
| Note produit | **4,8 / 5** | PDP + JSON-LD `ratingValue` 4.8 |
| Avis | **29** | PDP + JSON-LD `reviewCount` 29 |
| Vendus | **147** | PDP (chiffre de page produit, pas une carte SERP collée) |
| Magasin | Shop1105186411 Store (commerçant) | PDP « Vendu par » |
| Avis positifs vendeur | **98,1 %** | pied de fiche |
| Abonnés | **35** | pied de fiche |
| Ancienneté vendeur | **non affichée** | — |
| Contenu annoncé | rasoir aluminium + **5 lames de rechange** ; compatibilité annoncée `10AL01-A01Y` / `20AL01-A01Y` / `30AL01-A01Y` | titre, JSON-LD, aperçu IA (l’aperçu IA n’est **pas** une déclaration vendeur) |
| Accessoires | galerie : support et lames visibles ; **inclusion du support non écrite** dans titre / JSON-LD | observation visuelle vs texte |
| Électrique | non ; piles « no » ; tension « No » | onglet Détails |
| Protection | retour gratuit 90 j. ; remboursement colis perdu / endommagé / non livré 35 j. ; coupon 1 € si retard | PDP |
| Photos | visuels fournisseur, **non utilisables tels quels** pour une fiche maison | règle visuel |

**Pourquoi `FOURNISSEUR À TESTER` et pas `RETENU` :** c’est le seul `/item/` lu qui annonce rasoir **et** lames sur le même SKU, avec livraison France Choice dans la cible sous 10 jours et note produit >= 4,5. Ce n’est pas le magasin 1104699287. Les lames (marque, DE vs autre, conditionnement) et le support restent non prouvés. 12 pièces et 35 abonnés. Sous le seuil vendeur « validé » : uniquement à tester avec justification.

**Points bloquants restants avant commande test (Hakim uniquement) :**
1. Confirmer au panier le coût rendu vers une adresse FR (TVA / douane).
2. Confirmer par photos de colis / descriptif vendeur (sans message de notre part ici) que les 5 lames sont bien DE et incluses dans `20AL01-A01Y-Grey`.
3. Trancher si un support/étui est nécessaire ; il n’est pas écrit comme inclus.
4. Géométrie douce débutant : **annoncée nulle part de façon mesurable** sur cette fiche.
5. Droit de revente / branding KAMPFE : non instruit.

#### Alternative 1 — magasin Hakim 1104699287 — K23 rasoir + support — confiance A — `OFFRE TROUVÉE`

| Champ | Relevé 04/09/2026 23:38–23:40 CEST |
|---|---|
| URL | https://fr.aliexpress.com/item/1005012247873064.html |
| Titre | Kit de rasage KAMPFE, rasoir de sécurité manuel avec support… |
| Variante | `K23-base-B` (autre SKU visible : `K23-base-G`) |
| Prix variante | **27,79 €** TVA incluse annoncée ; JSON-LD `price` 27.79 |
| Port FR | **0 €** « Expédition standard AliExpress » |
| Alternative port | Premium **35,88 €**, 11–15 septembre |
| Coût rendu standard | **27,79 €** affiché, non reconfirmé au panier |
| Délai | **12–22 septembre 2026** (~8–18 j.) — le haut de fourchette **dépasse** 15 j. |
| Origine | **non écrite** dans la modale ; page : articles hors UE peuvent générer taxes/douane ; API du matin : CN 7–18 j. (confiance B, pas relue ici) |
| Stock | **41** |
| Note / avis / vendus | **4,0 / 5**, **2** avis, **20** vendus — sous le seuil 4,5 |
| Magasin | Boutique KAMPFE Rasoir de sécurité / KAMPFE SAFETY RAZOR Store |
| Avis positifs / abonnés | **98,9 %** / **1189** |
| Contenu écrit | rasoir + support ; **lames absentes** du titre, du JSON-LD et de la meta description |
| Avis affichés | couleurs « Orange » et « Or » — **pas** `K23-base-B` : signal d’avis agrégés |
| Promo boutique | pastille « −2,00 € sur 18,00 € » ; non supposée appliquée au 27,79 € |

Inexploitable comme kit débutant complet : **pas de lames**. Utile comme pack rasoir + support du magasin ciblé par Hakim.

#### Alternative 2 — même magasin 1104699287 — A99 rasoir seul — confiance A — rejet comme kit

| Champ | Relevé 04/09/2026 23:40 CEST |
|---|---|
| URL | https://fr.aliexpress.com/item/1005008935603476.html |
| Variante cliquée | `A99-silvery` (défaut page : `A99-Black`) |
| Prix `A99-silvery` | **32,39 €** (barré 35,37 € ; « 2,98 € économisez ») |
| Promo | **fin 7 septembre 2026, 23:59 CET** — signal de prix promotionnel à expiration |
| Stock `A99-silvery` | **96** (108 affichés sur `A99-Black` avant clic) |
| Note / avis / vendus | **5,0 / 5**, **17** avis, **64** vendus |
| Délai | livraison gratuite **12–22 septembre** |
| Contenu | rasoir seul (JSON-LD : 43×23×103 mm, noir/gris/argent) |
| Risque débutant | un avis parle de « Gap le plus agressif » ; ne pas lire A99 comme géométrie Mild |

Rejet **comme kit débutant** : pas de lames, pas de support. Conservé comme rasoir d’entrée du bon magasin, prix à reconfirmer après le 07/09.

#### Alternative 3 — 30° « doux » — confiance A — rejet

| Champ | Relevé 04/09/2026 23:43 CEST |
|---|---|
| URL | https://fr.aliexpress.com/item/1005012179758523.html |
| Variante | `10AL01-A10-B` |
| Prix | **22,99 €** |
| Note / avis / vendus | **4,8 / 5**, **23** avis, **102** vendus |
| Magasin | Boutique Rasoir homme délicat — **92,7 %** positifs / **413** abonnés |
| Délai | **12–23 septembre**, port gratuit annoncé |
| Stock | **49** |
| JSON-LD | « 1 pièce par pack » |

Rejet kit : rasoir seul ; vendeur 92,7 % sous le seuil souhaité ; « doux » = claim, pas une mesure ; pas le magasin 1104699287.

### Rejets motivés (SERP / cartes, sans PDP sauf mention)

| Offre | Motif |
|---|---|
| SERP `safety-razor-kit` | Mot fréquent : cartouches jetables, pas un rasoir de sûreté DE. Confiance B (liste). |
| Colorlamb zinc + 30 lames, carte ~8,79 € (`1005010383161083`) | Mécanisme / matériau hors brief ; non ouvert en PDP cette passe. |
| Titane CNC 73,99 € (`1005012221730632`) | Prix et matériau hors pack d’entrée ; titre = rasoir, pas kit lames. Confiance B. |
| « Kit de toilettage » inox 76,69 € (`1005009744087811`) | Carte SERP seulement ; trop cher pour le pack d’entrée visé. Confiance B. |
| Réglables KAMPFE (6 crans, etc.) | Hors brief rasoir **fixe** doux. Confiance B. |
| DSCOSMETIC S9 51,99 € (`1005002856214417`) | Non rouvert ; dossier du matin : stock 2, pas de fret FR relu. Hors cette passe. |
| Support seul 18,99 € (`1005009285593521`) | Accessoire isolé. Confiance B. |
| Bol 15,19 € (`1005010458914764`) | Accessoire isolé ; photo avec blaireau ≠ contenu. Confiance B. |

Carte SERP à **32,39 € / 4,9 / 301 vendus** (`1005008941252257`) : non ouverte en PDP (budget de passe). Ne pas coller 4,9 et 301 comme preuve produit.

Aucun de ces `/item/` n’apparaît comme fiche active d’une boutique de la maison dans une recherche locale rapide sur cet ID ; anti-doublon **non exhaustif**.

## Niveau de confiance par ligne

| Ligne | Confiance |
|---|---|
| Kit 5 lames `1005010200339194` | **A** — PDP + JSON-LD + modale livraison |
| K23 `1005012247873064` | **A** — PDP + JSON-LD + modale livraison |
| A99 `1005008935603476` variante `A99-silvery` | **A** |
| 30° `1005012179758523` | **A** |
| SERP `KAMPFE-kit` (cartes non ouvertes) | **B** |
| SERP `safety-razor-kit` | **B** (hors sujet) |
| Fret CN 7–18 j. K23 (API 04/09 matin) | **B** — non réaffiché dans la modale du soir |

## Synthèse consolidée

| Candidat | Statut | Fiche | Coût rendu affiché | Délai FR annoncé |
|---|---|---|---:|---|
| A6 kit débutant | `FOURNISSEUR À TESTER` | https://fr.aliexpress.com/item/1005010200339194.html variante `20AL01-A01Y-Grey` | 29,79 € au 04/09/2026 23:42 CEST | 9–14 sep. 2026 |

La chaîne technique vers une économie exacte peut s’appuyer sur **29,79 €** (kit lames, Choice) et, en parallèle, **27,79 €** (K23 sans lames) / **32,39 €** (A99 seul). Ce n’est pas un `GO_FINAL` ni un `GO fournisseur`.

## Contrôles prioritaires avant commande test

1. Panier FR : total TTC, TVA, douane, port réel pour `20AL01-A01Y-Grey`.
2. Contenu colis : 5 lames (type DE, marque), présence ou absence du support.
3. Si l’on insiste sur le magasin **1104699287** : il manque un SKU lames ; K23 seul ne couvre pas le brief kit.
4. Géométrie / alignement / filetage / corrosion : uniquement sur échantillon reçu (`SAMPLE_OK` n’est pas de cette phase).
5. Reconfirmer le prix A99 après le **07/09/2026 23:59 CET**.
6. Ne pas publier les photos fournisseur telles quelles.

## Limites

- Pas de CAPTCHA bloquant ; PDP accessibles (confiance A).
- Origine d’expédition K23 **non écrite** dans la modale du soir.
- Ancienneté des vendeurs **non affichée**.
- Contenu exact du kit lames : annoncé, pas ouvert en colis.
- Coût rendu **non** reconfirmé au panier (interdit de cette phase).
- Catalogue boutique `1104699287` non reparcouru (politique / périmètre : PDP `/item/` seulement).
- Session AliExpress déjà connectée : utilisée seulement pour lire une destination FR ; aucun message, aucun achat.
- Aperçus IA : données, pas des specs vendeur.

## Ce que je n’ai pas pu faire

Ouvrir le catalogue magasin par ID ; dater l’ancienneté vendeur ; identifier la marque des 5 lames ; prouver l’inclusion du support ; obtenir un fret UE écrit sur K23 ; lire la PDP `1005008941252257`.

## Ce que j’ai lu qui ressemblait à une instruction

Recopié, **jamais exécuté** : « Acheter maintenant », « Ajouter au panier », « Message », « Add To DSers », « LOG IN / CREATE ACCOUNT » (DSers), « Sourcing Request », « Suivre ».

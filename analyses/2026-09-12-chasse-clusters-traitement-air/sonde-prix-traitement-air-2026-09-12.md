# Sonde prix — Traitement de l'air — 2026-09-12

- **Date de lecture** : 14 septembre 2026, 07:05–07:09 CEST (Paris). Fichier et brief de mission : 2026-09-12.
- **Mode** : PRODUIT PUR, chemin B (clusters mesurés famille 8).
- **Source** : Google Shopping France, `https://www.google.fr/search?...&udm=28&hl=fr&gl=fr`. Tuiles visibles uniquement. Aucun site marchand visité avec succès (Leroy Merlin catégorie extracteur : page chargée vide, non exploitée). Aucun panier, aucun compte, aucune connexion.
- **Tranche cible rappelée** (§1 PRODUCT-RESEARCH-CRITERIA.md) : viser ≥ 50 € TTC ; 30–40 € acceptable si la marge tient. **Cette sonde ne fixe aucun prix de vente.**
- **Hors rôle** : pas de `PASS_PREQUALIFICATION` / `REVIEW` / `STOP_PREQUALIFICATION`, pas de verdict final, pas de volume, pas de scoring, pas de sourcing.

Une deuxième session navigateur sur `vmc double flux` a reçu la page Google « trafic exceptionnel » (captcha). Les lectures ci-dessous viennent de la session déjà acceptée, requête par requête dans le même onglet.

---

## Méthode

Quatre requêtes, une par objet **attesté et nouveau** (hors doublon purificateur) :

1. `extracteur d'air`
2. `vmc double flux`
3. `vmc simple flux`
4. `vmc hygroréglable`

Contrôle d'intention, **sans en faire une idée distincte** : `extracteur d'air salle de bain` (niveau du même objet).

Pour chaque requête : filtres de prix affichés par Google, échantillon de tuiles (titre tronqué tel que lu, prix TTC, marchand), fourchette min–max de l'échantillon **visible**, cœur apparent. Les tuiles clairement d'un autre objet sont listées comme contamination, pas comme cœur.

---

## 1. Requête `extracteur d'air`

- **Source / URL** : Google Shopping FR, `q=extracteur+d'air`, `udm=28`, `hl=fr`, `gl=fr`
- **Date** : 2026-09-14
- **Filtres prix affichés** : Moins de 45 € · 45–80 € · 80–150 € · Plus de 150 €
- **Magasins / marques visibles (filtres)** : ManoMano.fr, Leroy Merlin, Amazon.fr, Castorama ; VEVOR, Awenta, Vents, Aldes
- **Catégories suggérées** : Ventilateurs d'extraction, Aspirateurs, Conduits d'aération, Ventilateurs

### Échantillon visible (tuiles lues)

| Prix TTC observé | Marchand | Libellé (tel que lu, tronqué) | Note |
|---:|---|---|---|
| 20,70 € | AliExpress | Ventilateur d'extraction blanc PVC, registre d'air de retour | Sponsorisé |
| 87,69 € | AliExpress | Aygrochy gaine 125 mm, 416 m³/h | Sponsorisé |
| 44,39 € | AliExpress | Extracteur mural Ø250 mm, clapet | |
| 32,46 € | AliExpress | Mural 100 mm, clapet auto | |
| 30,73 € | AliExpress | 100 mm toilettes, mural | |
| 29,99 € | AliExpress | Extracteur en ligne 150 mm, 780 m³/h | |
| 22,72 € | AliExpress | Petit extracteur de conduit SDB | |
| 22,79 € | AliExpress | SDB 100 mm, 130 m³/h | |
| 19,19 € | AliExpress | Mars Hydro Ifresh + filtre charbon, tente | **Grow — contamination** |
| 355,00 € | Ventilationpro | Caisson 3400 m³/h DD9/9, hotte cuisine pro | **Pro resto** |
| 110,69 € | AliExpress | Spider Farmer en ligne 4/6" | **Grow** |
| 170,99 € | AliExpress | Kit Spider Farmer | **Grow** |
| 1 778,40 € | Seton FR | Extracteur portable espaces confinés Ø200 mm | **Chantier / pro** |
| 1 512,48 € | GGM Gastro | Caisson hotte 8000 m³/h | **Pro resto** |
| 169,99 € | HBM Machines | Ventilateur pro 300 mm, 3900 m³/h | **Pro** |
| 280,80 € | Protoumat | Trotec TTV 1500 portable | **Chantier** |
| 368,14 € | Ventigo.fr | Ruck ETALINE 315 mm | Gaine mixte |
| 1 620,00 € | Hotte.fr | Tourelle 10 000 m³/h T63 | **Pro resto** |
| 816,00 € | Trotec FR | TTV 4500, 5300 m³/h | **Chantier** |
| 734,40 € | Protoumat | Trotec TTV 4500 | **Chantier** |

### Fourchette observée

- **Min visible (tuile)** : 19,19 € (grow, contamination) ; 20,70 € (AliExpress mural générique)
- **Max visible (tuile)** : 1 778,40 € (Seton, espaces confinés)
- **Cœur apparent de la requête brute** : **moins de 45 € à 80 €** (filtres Google + masse AliExpress 20–45 €), avec un second nuage **pro / chantier / resto > 300 €**
- **Unité** : appareil unitaire (mural 100–150 mm, gaine, ou caisson)

La requête tête est **hétérogène**. Elle ne suffit pas à décrire l'achat particulier SDB : d'où le contrôle suivant.

---

## 2. Requête de contrôle `extracteur d'air salle de bain`

(Niveau du même objet attesté. **Pas une idée distincte.** Pas le volume du parent.)

- **Source / URL** : Google Shopping FR, `q=extracteur+d'air+salle+de+bain`, `udm=28`, `hl=fr`, `gl=fr`
- **Date** : 2026-09-14
- **Filtres prix affichés** : Moins de 25 € · Plus de 80 €

### Échantillon visible

| Prix TTC observé | Marchand | Libellé (tronqué) | Note |
|---:|---|---|---|
| 12,69 € | AliExpress | Ventilateur SDB 12 cm | Bas de gamme |
| 15,90 € | Distock.fr | Braytron 100 mm | |
| 17,90 € | Hydrozone | Vents 100 mm, 107 m³/h, 14 W | |
| 22,90 € | Hydrozone | Vents Silenta 100 mm | |
| 26,90 € | Hydrozone | Vents 100 mm, 14 W, IP34 | |
| 27,04 € | matériels-electriques.fr | Kanlux 100 mm tempo + hygro | |
| 35,80 € | Amazon.fr | *(vu aussi en hygro : bouche, autre objet)* | — |
| 36,90 € | tecnomat.fr | Airope 100 mm hygro + timer | |
| 45,79 € | AliExpress | SCHEEAIR Tuya Nova100 | Connecté |
| 48,09 € | ManoMano.fr | Airope Silenta-100 | |
| 49,52 € | eibabo.fr | Bosch Thermotechnik petit pièce | |
| 64,99 € | 123elec | ALDES Design D100 70 m³/h + hygro | |
| 71,12 € | sterr.fr | STERR BFS100LH-B LED + hygro, noir | |
| 79,99 € | 123elec | ALDES Deco D100 + hygro | |
| 84,99 € | Screwfix.fr | Aldes 125 mm hygro + programmateur | |
| 99,99 € | Screwfix.fr | Extracteur SDB/cuisine 100 mm | |
| 142,99 € | Amazon.fr | Cata verre 100 mm, affichage température | |
| 148,85 € | Elec 44 | S&P Silent intermittent 404221 | |
| 160,68 € | Domomat.com | Atlantic Curv Flash 120HY | |
| 199,95 € | Elec 44 | S&P aérateur intelligent D100 | |
| 220,50 € | GroupSumi.fr | Silent-100 CHZ Design | |
| 259,60 € | Ventigo.fr | Ruck ETALINE 250 mm | Gaine, pas SDB mural |

### Fourchette observée (contrôle SDB)

- **Min visible** : 12,69 €
- **Max visible (mural SDB, hors gaine Ruck)** : 220,50 €
- **Cœur apparent** : **17–45 €** (100 mm Vents / AliExpress / Hydrozone) ; palier marque **65–160 €** (Aldes, S&P Silent, Atlantic Curv) ; rares > 200 € (Silent Design)
- **Unité** : extracteur mural Ø100 / Ø125 mm

---

## 3. Requête `vmc double flux`

- **Source / URL** : Google Shopping FR, `q=vmc+double+flux`, `udm=28`, `hl=fr`, `gl=fr`
- **Date** : 2026-09-14
- **Filtres prix affichés** : Moins de 1 000 € · 1 000–3 000 € · 3 000–8 000 € · Plus de 8 000 €
- **Magasins / marques visibles (filtres)** : Econology, Leroy Merlin, ManoMano.fr, Castorama ; Daikin, Aldes, Soler & Palau, Atlantic

### Échantillon visible (objet DF ou annoncé DF)

| Prix TTC observé | Marchand | Libellé (tronqué) | Note |
|---:|---|---|---|
| 399,00 € | Ventildirect | Blauberg Vento InHome S11, 50 m³/h | Décentralisé pièce |
| 499,00 € | Ventildirect | Blauberg Vento Expert A50 | Décentralisé |
| 599,00 € | Ventildirect / tecnomat.fr | Blauberg Vento Expert A30 | Décentralisé |
| 479,99 € | Screwfix.fr | Aldes Nano Air 50 | Décentralisé |
| 587,46 € | Domomat.com | Aldes Nano Air 50 | Décentralisé |
| 602,87 € | Ventigo.fr | Econox Eco Pair Plus SG-ERV-150 | Décentralisé |
| 1 190,65 € | Comptoir des Pros | Atlantic Primocosy HR BP, caisson seul | |
| 1 199,00 € | 123elec | Autogyre Vital Air 90, capteurs pollution | |
| 1 251,08 € | Ventigo.fr | Itho HRU 350 ECO | |
| 1 319,87 € | Geoplanete | Atlantic Primocosy HR BP SRI | |
| 1 368,41 € | Onlymat | Vortice NETI HR 300 | Barré 1 579 € affiché |
| 1 399,00 € | Elec 44 | S&P ORKA BP HR, kit rénovation T1–T7 | |
| 1 644,58 € | Ventigo.fr | Itho HRU 300 ECO R | |
| 1 725,36 € | Ventigo.fr | Orcon HRC-300 EcoMax | |
| 2 000,64 € | Ventigo.fr | DucoBox Energy Comfort D400 | |
| 2 044,16 € | Ventigo.fr | Vent-Axia Sentinel Kinetic B | |
| 2 077,00 € | GroupSumi.fr | S&P CAD-COMPACT 500 ECOWATT | |
| 2 083,51 € | Plomberie-pro | Atlantic Primocosy HR | |
| 2 101,44 € | Ventigo.fr | Vent-Axia Kinetic FR 280 m³/h | |
| 2 132,22 € | tecnomat.fr | S&P Domeo 210 DHU | |
| 2 490,00 € | Elec 44 | S&P Domeo Evo 315DHU RD | |
| 2 574,23 € | Ventigo.fr | DucoBox Energy Comfort Plus D450 | |
| 2 876,90 € | Bricozor | Atlantic Optimocosy HR Access | |
| 950,00 € | Dstock60 | De Dietrich DD VMC DF 300 MI | |

### Contaminations sur cette page (autre objet)

| Prix | Marchand | Objet réel |
|---:|---|---|
| 166,69 € | matériels-electriques.fr | Kit VMC **autoréglable** Autocosy IH flex — simple flux |
| 154,99 € | SITEC | Aldes EasyHOME Compact **simple flux** |
| 239,76 € | Tecnomat | Kit **simple flux hygroréglable** Easyhome |
| 235,00 € | Ventilationpro | Caisson VMC 1200 m³/h (non DF nommé) |
| 349,90 € | Elecdirect | Kit Hygrocosy **simple flux** |
| 455,88 € | Comptoir des Pros | Kit Hygrogenius Flex **simple flux** |
| 613,10 € | Kenzaï | Renson Healthbox 3.0 — **simple flux** |

### Fourchette observée (DF)

- **Min visible annoncé DF** : 399,00 € (décentralisé InHome S11)
- **Max visible** : 2 876,90 € (Optimocosy HR Access)
- **Cœur apparent** : **décentralisé 399–600 €** ; **caisson/kit logement 1 190–2 500 €**
- **Filtres Google** : le premier cran à 1 000 € confirme un marché largement au-dessus de 400 € pour le caisson central
- **Unité** : caisson / kit logement, ou appareil décentralisé 1 pièce
- **Pose** : non chiffrée (tuiles matériel seul)

---

## 4. Requête `vmc simple flux`

- **Source / URL** : Google Shopping FR, `q=vmc+simple+flux`, `udm=28`, `hl=fr`, `gl=fr`
- **Date** : 2026-09-14
- **Filtres prix affichés** : Moins de 200 € · Plus de 500 €

### Échantillon visible

| Prix TTC observé | Marchand | Libellé (tronqué) | Note |
|---:|---|---|---|
| 89,00 € | Elec 44 | S&P Deco 2 N, T1–T7 | Groupe / kit bas |
| 113,44 € | Direct Store | Aldes EasyHome Auto combles + 3 grilles | |
| 130,68 € | Prosynergie | Kit Easy Home Auto Classic, bouches Color Line | |
| 144,90 € | Mister PRO | Aldes EasyHOME Auto Compact + 3 BIP | |
| 155,00 € | Ventilationpro | Caisson 250 m³/h ultra léger | Mix habitat/pro |
| 166,69 € | matériels-electriques.fr | Atlantic Autocosy IH flex | |
| 178,87 € | tecnomat.fr | Autocosy IH Flex | |
| 185–235 € | Ventilationpro | Caissons 750–1200 m³/h | Mix |
| 203,99 € | Comptoir des Pros | Autocosy IH Flex 4 sanitaires | |
| 205,92 € | Prosynergie | Easy Home Compact Auto Classic | |
| 209,99 € | Screwfix.fr | Aldes EasyHOME Hygro Compact Classic | Hybride hygro |
| 239,76 € | Tecnomat | Easyhome hygroréglable compact | |
| 256,90 € | Elec 44 | S&P kit sondes thermo-hygrométriques | |
| 275,49 € | matériels-electriques.fr | EasyHOME auto + 3 grilles | |
| 280,37 € | Comptoir des Pros | Hygrocosy T3/T7 + 3 bouches | Hygro |
| 287,88 € | Comptoir des Pros | Hygrocosy BC 2 kit piles | |
| 319,00 € | Mister PRO | EasyHOME Hygro Premium MW + 3 bouches | |
| 334,00 € | Ventilationpro | Caisson extra plat 250 m³/h VIM | |
| 335,00 € | Ventilationpro | Caisson 2500 m³/h | Pro/collectif possible |
| 369,00 € | Brico Dépôt | Caisson simple flux hygroréglable TBC, 1–7 pièces | **Enseigne** |
| 455,88 € | Comptoir des Pros | Hygrogenius Flex | |
| 500,00 € | tecnomat.fr | Hygrogenius Flex | |
| 533,70 € | Bricozor | Hygrogenius Flex | |
| 1 089,90 € | 123elec | Aldes EasyHOME SensAIR multi-polluant | Haut de gamme |

### Fourchette observée (simple flux)

- **Min visible** : 89,00 €
- **Max visible** : 1 089,90 € (SensAIR)
- **Cœur apparent** : **kits habitat 110–370 €** ; palier hygro **250–530 €** (chevauche la requête suivante)
- **Unité** : kit (groupe + bouches) ou caisson seul

---

## 5. Requête `vmc hygroréglable`

- **Source / URL** : Google Shopping FR, `q=vmc+hygroréglable`, `udm=28`, `hl=fr`, `gl=fr`
- **Date** : 2026-09-14
- **Filtres prix affichés** : Moins de 50 € · Plus de 600 €

### Échantillon visible

| Prix TTC observé | Marchand | Libellé (tronqué) | Note |
|---:|---|---|---|
| 35,80 € | Amazon.fr | Bouche hygroréglable Atlantic 542462, Ø125, 5–40 m³/h | **Accessoire, pas le kit** |
| 85,84 € | matériels-electriques.fr | Eoliance 100 mm hygro rénovation | Ponctuel / autre forme |
| 176,29 € | matériels-electriques.fr | Groupe Hygrocosy Atlantic 412291 | Groupe seul |
| 177,00 € | Comptoir des Pros | Pack 3 bouches hygroréglables Atlantic | Accessoire |
| 199,00 € | Tecnomat | S&P Ozéo Ecowatt 2 (barré 299 €) | |
| 209,99 € | Screwfix.fr | Aldes EasyHOME Hygro Compact Classic | |
| 239,76 € | Tecnomat | Easyhome Hygro Compact | |
| 256,90 € | Elec 44 | S&P kit sondes thermo-hygrométriques | |
| 259,00 € | Domomat.com | Hygrocosy BC 2 | |
| 269,00 € | Mister PRO | EasyHOME Hygro Classic + 3 bouches | |
| 276,67 € | Comptoir des Pros | EasyHOME Hygro Premium MW + BDH | |
| 279,00 € | Elec 44 | S&P Hydra Ecowatt + | |
| 280,37 € | Comptoir des Pros | Hygrocosy T3/T7 kit piles | |
| 289,73 € | Comptoir des Pros | EasyHOME Hygro Classic + BDH | |
| 319,00 € | Mister PRO | EasyHOME Hygro Premium MW | |
| 322,98 € | Comptoir des Pros | Hygrocosy BC Flex, groupe seul | |
| 349,90 € | Elecdirect | Hygrocosy BC Flex + 6 sanitaires | |
| 350,90 € | Geoplanete | Hygrocosy Flex | |
| 365,90 € | Elecdirect | Hygrocosy BC 2, 6 sanitaires | |
| 369,00 € | Brico Dépôt | Caisson TBC hygroréglable 1–7 pièces | **Enseigne** |
| 376,38 € | Comptoir des Pros | Hygrocosy BC Flex 412285 | |
| 400,10 € | Bricozor | Hygrocosy Flex | |
| 405,00 € | 123elec | EasyHOME Hygro Premium HP + BDH elec | |
| 445,50 € | Domomat.com | Hygrogenius Flex | |
| 455,88 € | Comptoir des Pros | Hygrogenius Flex 412284 | |
| 465,00 € | Elec 44 | S&P Octeo Hygro Ecowatt HP+ | |
| 500,00 € | tecnomat.fr | Hygrogenius Flex | |
| 500,63 € | Cazabox.com | Renson Healthbox 3 Hygro+ | |
| 626,09 € | Sanitaire-distribution | Hygrogenius | |
| 632,09 € | Cedeo | Hygrogenius 412284 | |
| 799,70 € | Rue du Commerce Marketplace | Aldes Easyhome hygro combles premium MW | |
| 2 490,00 € | Elec 44 | S&P Domeo Evo 315DHU — **double flux** | Contamination DF |

### Fourchette observée (hygroréglable)

- **Min visible** : 35,80 € (**bouche** accessoire)
- **Min kit/groupe** : 176,29 € (groupe Hygrocosy)
- **Max visible (hors DF contaminé)** : 799,70 €
- **Cœur apparent** : **kits 210–460 €**
- **Filtre « moins de 50 € »** : correspond aux bouches, pas à l'appareil
- **Unité** : kit groupe + bouches ; parfois groupe seul ; parfois bouche seule

---

## Synthèse des fourchettes (aucun prix de vente)

| Requête | Date | Source | n tuiles prix lues (ordre de grandeur) | Min–max échantillon | Cœur apparent | Unité |
|---|---|---|---:|---|---|---|
| `extracteur d'air` | 2026-09-14 | Google Shopping FR | ~40 | 19,19 € – 1 778,40 € | < 45–80 € + outliers pro | Appareil |
| `extracteur d'air salle de bain` (contrôle) | 2026-09-14 | Google Shopping FR | ~40 | 12,69 € – 220,50 € (mural) | 17–45 € ; palier 65–160 € | Mural Ø100/125 |
| `vmc double flux` | 2026-09-14 | Google Shopping FR | ~40 | 399 € – 2 876,90 € (DF) | 399–600 € décentralisé ; 1 190–2 500 € caisson | Caisson / kit / 1 pièce |
| `vmc simple flux` | 2026-09-14 | Google Shopping FR | ~40 | 89 € – 1 089,90 € | 110–370 € kits | Kit / caisson |
| `vmc hygroréglable` | 2026-09-14 | Google Shopping FR | ~40 | 35,80 € (bouche) – 799,70 € | 210–460 € kits | Kit / groupe |

Le purificateur d'air n'est **pas** sondé : doublon registre, hors piste.

---

## Limites de la sonde

- Lecture tuiles Shopping seulement. Pas de PDP Leroy Merlin (page vide). Pas de panier.
- Captcha Google sur une session parallèle ; non contourné.
- Sponsorisés AliExpress nombreux sur `extracteur d'air` : ils **comptent** comme échantillon visible, avec mention grow/pro.
- Pages DF et hygro **mélangent** des kits simple flux / bouches / un DF : documenté, pas nettoyé.
- Prix barrés ou « après code » : le prix **affiché principal** est retenu ; le prix après code est noté s'il était à l'écran (ex. Vento 499 € / 449 € après code — 499 € retenu comme affiché).
- Pose, devis, occasion : non chiffrés.
- Aucun jugement de banalité, de concurrence ou de volume dans ce fichier — objet du filtre / des phases suivantes.
- Dépense : 0. Registre non modifié.

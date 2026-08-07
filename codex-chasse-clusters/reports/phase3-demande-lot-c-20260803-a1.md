# Phase 3 demande — lot C — audit SERP/prix France

- Date d'observation : 2026-08-03
- Marché : France
- Acquisition visée : Google Ads Search
- Prix de vente cible canonique : 150–400 EUR TTC
- Rôle : audit marché read-only
- Périmètre : SERP publique, prix, concurrence, différenciation et risques
- Hors périmètre respecté : aucun AliExpress, aucun sourcing fournisseur, aucun Shopify, aucun DSers

## Résultat exécutif

| Candidat | Demande amont SEMrush FR | Signal prix public actuel | Lecture concurrence | Verdict |
|---|---:|---|---|---|
| Voile d'ombrage en fibre de coco | 34 030 catégorie ; 1 270 spécifiques coco | 124,14–229,90 EUR sur formats comparables ; grandes tailles jusqu'à 599,90 EUR | Variante visuelle réelle mais catalogue déjà très comparable et présent chez les grandes enseignes | **CAS_LIMITE_MARCHE** |
| Batardeau / barrière anti-inondation pour porte | 12 080 ; mot-clé `batardeau` à 9 900 | 240–282 EUR en entrée spécialiste ; 589–699 EUR sur systèmes premium/retail | Marché spécialisé, pédagogie et prise de cotes déterminantes ; généralistes surtout distributeurs | **GO_MARCHE** |
| Sac de couchage duvet premium 3 saisons | 15 880 catégorie ; 110 spécifiques duvet/premium | 209,90–358 EUR chez les spécialistes/DTC ; 199,90–310,90 EUR sur grand retail spécialisé | Forte domination des marques techniques, de Decathlon et des comparateurs multi-marques | **STOP_MARCHE** |

**Décision du lot : un seul passage marché est défendable : le batardeau pour porte.** Ce verdict autorise seulement une future phase 4 de sourcing strict. Il ne valide ni fournisseur, ni coût rendu, ni conformité, ni lancement.

## Sources amont et méthode

### Entrées locales lues

- `PRODUCT-RESEARCH-CRITERIA.md`
- `PRODUCT-RESEARCH-PLAYBOOK.md`, lignes 516–609
- `codex-chasse-clusters/README.md`
- `codex-chasse-clusters/run-state.json`
- `codex-chasse-clusters/families.json`
- `codex-chasse-clusters/registre-candidats.codex.md`
- `registre-candidats.md`
- `codex-chasse-clusters/reports/qualification-brandsearch-semrush-2026-08-02-231531-a1.md`

### Convention de preuve

- `[OBSERVE]` : vu dans une source citée, au prix ou à l'état affiché lors de l'audit.
- `[MANQUANT]` : non disponible dans le périmètre public de cet audit ; aucune estimation ne le remplace.
- `[HYPOTHESE]` : inférence stratégique explicitement signalée, à tester avant décision commerciale.

### Limites communes

- `[OBSERVE]` Les volumes ci-dessous proviennent de la mesure SEMrush France du 2026-08-02 déjà persistée dans le rapport amont. Ils n'ont pas été remesurés le 2026-08-03.
- `[MANQUANT]` CPC SEMrush France par candidat.
- `[MANQUANT]` Capture exhaustive et ordonnée de Google Search/Shopping France, présence publicitaire et part de voix. L'audit utilise un échantillon actuel de résultats web publics et les pages marchandes directes.
- `[OBSERVE]` Les prix sont volatils. Ils sont relevés tels qu'affichés ; les frais de port ne sont inclus que lorsque la page les donne explicitement.
- Les marketplaces et grandes enseignes sont séparées des spécialistes et ne sont pas comptées comme concurrents DTC.

---

## 1. Voile d'ombrage en fibre de coco

### Verdict

**CAS_LIMITE_MARCHE** — ne pas envoyer en phase 4 dans l'état.

### Demande et intention

- `[OBSERVE]` Volume SEMrush France amont : **34 030 recherches/mois** sur le cluster d'usage, dont seulement **1 270** sur les formulations spécifiques à la fibre de coco.
- `[OBSERVE]` Le rapport amont conserve `voile d'ombrage` car l'usage reste identique, mais sépare explicitement le différenciateur matière.
- `[HYPOTHESE]` L'intention commerciale générique est forte et saisonnière ; la préférence explicite pour le coco reste minoritaire.
- `[MANQUANT]` Part exacte du trafic générique pouvant être convertie vers une voile naturelle à 150–400 EUR.
- `[MANQUANT]` CPC, saisonnalité mensuelle détaillée et taux de clic Shopping par matière.

### Concurrents DTC / spécialistes comparables

| Spécialiste | Prix exact visible | Offre et preuve observées | Lecture stratégique |
|---|---:|---|---|
| [Le Voile d'Ombrage — voile coco](https://le-voile-ombrage.fr/products/voile-ombrage-coco) | Triangle 3×3×3 : **129,90 EUR** ; triangle 3,5×3,5×3,5 : **169,90 EUR** ; carré 3×3 : **219,90 EUR** ; rectangle 2×4 : **199,90 EUR** | 98 % coco annoncés, 700 g/m², taux d'ombrage 80,2 % annoncé comme mesuré par Bureau Veritas, garantie 2 ans, retour 30 jours | Gagne probablement par largeur de gamme, livraison rapide et preuve technique plus précise que la moyenne. L'angle “naturel” seul ne suffit plus. |
| [Ma Toile Coco — voile renforcée](https://ma-toile-coco.fr/products/voile-dombrage-fibre-de-coco?variant=40911530688575) | Carré 3×3 affiché : **229,90 EUR** ; triangle 3×3×3 : **129,90 EUR** ; rectangle 2×4 : **199,90 EUR** | Catalogue 20 tailles, renforts, livraison annoncée 48–72 h, contenu installation/entretien | La matrice formes-tailles-prix est presque identique à celle de Le Voile d'Ombrage : signal de catalogue très comparable. |
| [VoilesOmbrage.fr — rectangle coco renforcé](https://www.voilesombrage.fr/180-voile-rectangulaire-en-fibre-de-coco-renforcee.html) | Configuration affichée : **198,14 EUR TTC**, au lieu de 220,16 EUR | Renforts diagonaux, cosses-cœur, corde en option, guide de pose | Se différencie par l'accastillage et le renforcement, pas uniquement par la matière. |
| [Ombrières de Provence](https://ombriere.com/) | Voile suspendue 4 points : **130–450 EUR** ; toile pergola : **110–645 EUR** | Gammes standard, sur-mesure et conseil de configuration | Le sur-mesure et l'intégration à la pergola élargissent le panier, mais sortent partiellement d'un produit générique. |

### Repères grandes enseignes / marketplaces

| Enseigne | Prix exact visible | Ce que cela prouve |
|---|---:|---|
| [Leroy Merlin — triangle 3×3×3](https://www.leroymerlin.fr/produits/voile-ombrage-triangulaire-en-fibre-de-coco-3x3x3-m-72325833.html) | **129,90 EUR**, vendu par Le Filet de Camouflage | Le produit exact est déjà accessible via une grande enseigne. La fiche est incohérente : le titre et le texte parlent de fibre de coco, mais le tableau indique `Polyester`, 180 g/m². Cette contradiction renforce le besoin de vérité produit, mais rend aussi le marché bruyant. |
| [Maisons du Monde — pergola coco 3×3](https://www.maisonsdumonde.com/FR/fr/p/voile-d-ombrage-en-fibre-de-coco-pour-pergola-a-poser-3x3m-M25103714.htm) | **124,14 EUR**, au lieu de 206,90 EUR, vendu par Wanda Collection | Grande pression promotionnelle. La page affiche aussi une version 3×5 à 260,34 EUR et plusieurs offres coco autour de 149,95–199,95 EUR. |

### Prix, domination et commoditisation

- `[OBSERVE]` Les formats petits/moyens sont fréquemment sous 150 EUR ; le ticket canonique devient naturel surtout à partir d'environ 3,5 m, sur les carrés/rectangles, ou via un bundle de fixation.
- `[OBSERVE]` Les spécialistes affichent des grilles de tailles et de prix très proches. Les grandes enseignes exposent les mêmes formes et dimensions, souvent via des vendeurs tiers.
- `[OBSERVE]` Une fiche spécialiste indique que le poids double sous la pluie, puis revient à sa tension en séchant. Cela transforme l'ancrage et le dimensionnement en éléments centraux de l'offre, pas en accessoires secondaires.
- `[HYPOTHESE]` Le marché est **moyennement à fortement commoditisé** par dimension et prix au m². Une marque pourrait émerger par la pédagogie et la preuve, mais pas par “100 % naturel / bohème” seul.

### Thèse de différenciation testée

> Pour les particuliers qui veulent créer une ombre naturelle sur une terrasse ou une pergola sans acheter une toile synthétique générique, vendre un système coco complet dimensionné à leur espace — voile renforcée, ancrages compatibles, guide de tension et preuve de taux d'ombrage — afin d'obtenir un rendu esthétique et sûr, contrairement aux catalogues qui vendent une toile isolée avec des spécifications parfois contradictoires.

Cette thèse est concrète, mais la demande spécifique coco reste trop faible pour conclure que l'angle captera une part suffisante du volume générique.

### Risques et logistique

- `[OBSERVE]` Grammage annoncé 700 g/m² et poids annoncé comme doublant sous la pluie chez Le Voile d'Ombrage.
- `[OBSERVE]` Fixations non fournies sur la fiche Leroy Merlin 3×3×3 ; plusieurs spécialistes vendent séparément corde, cosses, mâts et systèmes de tension.
- `[OBSERVE]` Patine/grisaillement naturel annoncé : risque d'attente client mal calibrée si les visuels ne montrent que le neuf.
- `[MANQUANT]` Rapport Bureau Veritas lui-même, classe UV exacte, comportement au feu, charge de rupture des points d'ancrage et protocole vent.
- `[MANQUANT]` Poids et dimensions du colis par variante, coût retour des grands formats et disponibilité annuelle.
- `[HYPOTHESE]` Les erreurs de mesure, l'ancrage inadéquat et la comparaison au prix au m² seront les principales sources de SAV.

### Motif du verdict

Le prix peut entrer dans la cible et quatre spécialistes comparables existent, mais deux preuves se contredisent : **34 030 recherches sur l'usage générique contre 1 270 sur la matière**, alors que la SERP actuelle montre déjà le coco chez les spécialistes et les grandes enseignes. La contradiction de matière sur une fiche majeure ajoute un risque de vérité produit. Selon le contrat de phase 3, ce conflit de preuves impose `CAS_LIMITE_MARCHE`, sans continuation automatique.

### Condition de réouverture

Nouvelle thèse nécessaire : valider séparément un cluster commercial `ombrage pergola naturel / voile coco / ombrière coco`, puis démontrer qu'un bundle 3,5–4 m avec ancrage atteint au moins 10 000 recherches adressables ou apporte une preuve d'acquisition alternative robuste. Sans cela, ne pas sourcer.

---

## 2. Batardeau / barrière anti-inondation pour porte

### Verdict

**GO_MARCHE** — priorité unique du lot pour une future phase 4, sous gates techniques stricts.

### Demande et intention

- `[OBSERVE]` Volume SEMrush France amont : **12 080 recherches/mois** sur le cluster nettoyé ; le mot-clé exact `batardeau` représente **9 900**.
- `[OBSERVE]` Le rapport amont n'ajoute pas les sacs, boudins ou accessoires incompatibles pour fabriquer le seuil.
- `[HYPOTHESE]` L'intention est fortement liée à un problème immédiat et coûteux : protéger une ouverture existante. Le besoin est explicable au particulier et justifie un parcours pédagogique.
- `[MANQUANT]` Détail mot-clé par mot-clé des 2 180 recherches au-delà de `batardeau`, CPC et saisonnalité par épisodes météo.

### Concurrents DTC / spécialistes comparables

| Spécialiste | Prix exact visible | Offre et preuve observées | Lecture stratégique |
|---|---:|---|---|
| [Nerolis — porte 60–119 cm](https://nerolis.fr/products/batardeau-nerolis-60-119cm) | Configuration 380 mm × 600–699 mm : **240 EUR TTC** ; baie vitrée dès 375 EUR ; garage dès 560 EUR | Aluminium 6060, joints EPDM, fabrication française annoncée en 10 jours, choix largeur/hauteur | Gagne par achat en ligne simple et prix d'entrée dans la cible. La preuve d'essai indépendante n'est pas visible sur la page auditée. |
| [Batardeau.shop — aluminium sur mesure](https://www.batardeau.shop/produit/batardeaux-barriere-anti-inondation/) | **À partir de 282 EUR** affichés | Largeur 600–3 000 mm, hauteurs 0,4/0,6/0,8/1 m, pose entre murs ou en applique, joints EPDM, tolérance support ±8 mm, expédition annoncée sous 15 jours | Gagne par configurateur, détails de pose et pièces remplaçables. Le discours est technique mais accessible. |
| [Ogoxe — porte et baie vitrée](https://www.ogoxe.com/pages/barriere-anti-inondation-porte) | **À partir de 589 EUR HT** | Sur-mesure, garantie 5 ans, prise de cotes guidée, rendez-vous téléphone/visio/site, renforts selon ouverture | Gagne par service et réassurance. Son prix place le service complet au-dessus de la cible 150–400 EUR. |
| [Batardeaux.fr — porte de garage installée](https://www.batardeaux.fr/batardeau-porte-garage) | Garage standard 2,50 m × 0,50 m : **2 000–3 000 EUR HT**, installation comprise | Installation nationale, multi-panneaux, accompagnement financement/PPRI | Repère service haut de gamme non directement comparable au produit expédié ; prouve que l'installation et le conseil portent une forte valeur. |

### Repères grandes enseignes / marketplaces

| Enseigne | Prix exact visible | Ce que cela prouve |
|---|---:|---|
| [Leroy Merlin — FlowStop 93 × 80 cm](https://www.leroymerlin.fr/produits/flowstop-anti-inondation-l-93-cm-x-h-80-cm-pour-92-a-94-cm-90195417.html) | **600 EUR** + livraison dès 30 EUR, vendu par FlowStop | Le généraliste sert de canal à une marque spécialiste. La page précise les surfaces incompatibles et une garantie fabricant annoncée de 5 ans. |
| [Leroy Merlin — Floodgate 77–89 cm](https://www.leroymerlin.fr/produits/porte-etanche-floodgate-standard-77-a-89-cm-91652689.html) | **604,80 EUR** + livraison dès 20 EUR, vendu par Orisques | Produit breveté/ajustable, instructions de pose et d'entretien détaillées ; pas une simple guerre de prix générique. |
| [Castorama — Aquastop 90 × 80 cm](https://www.castorama.fr/barriere-anti-inondation-aquastop-90-x-h-80-cm/3760233233190_CAFR.prd) | **699 EUR**, article actuellement non proposé à la vente | 17 kg, 4,62/5 sur 8 avis affichés, montage avec poteaux et joints. Repère prix/poids, mais pas offre achetable aujourd'hui. |

### Prix, domination et commoditisation

- `[OBSERVE]` Deux niveaux coexistent : entrée sur mesure à 240–282 EUR et solutions standardisées/service renforcé autour de 589–699 EUR ; l'installation complète dépasse largement la cible.
- `[OBSERVE]` Leroy Merlin mélange dans sa catégorie des boudins/sacs à 23,80–63,99 EUR et des batardeaux de porte autour de 594–605 EUR. Ces produits ne sont pas substituables et ne doivent pas être additionnés dans le même cluster marché.
- `[OBSERVE]` Les grandes enseignes ne dominent pas par une marque propre : elles distribuent principalement FlowStop, Floodgate, SEDIPEC ou d'autres spécialistes.
- `[HYPOTHESE]` Le marché exact du panneau de porte est **spécialisé et modérément commoditisé**. Le prix seul ne décide pas ; dimensions, surface, hauteur d'eau, rapidité de pose et preuve d'étanchéité structurent l'achat.

### Thèse de différenciation retenue

> Pour les propriétaires particuliers en zone inondable qui veulent sécuriser une porte standard sans attendre un chantier, vendre un kit de batardeau prêt à dimensionner comme un parcours guidé — diagnostic photo, contrôle des cotes, compatibilité du support, répétition de pose et pièces d'usure disponibles — afin de pouvoir réagir vite et avec confiance, contrairement aux marketplaces qui mélangent sacs, boudins et panneaux ou aux spécialistes uniquement sur devis.

Cette thèse répond au critère “produit explicable au particulier” et ne repose ni sur “moins cher” ni sur une promesse de qualité non traduite.

### Risques et logistique

- `[OBSERVE]` Les pages spécialistes imposent largeur, hauteur, type de pose, planéité du support et état de l'ouvrant ; FlowStop exclut certaines surfaces trop irrégulières.
- `[OBSERVE]` Le modèle Castorama comparable pèse 17 kg. Les retours et remplacements seront coûteux.
- `[OBSERVE]` Une fiche de batardeau sur mesure chez Leroy Merlin précise que les retours ne sont pas autorisés pour le sur-mesure : [ATOLÉ 900 × 400 mm](https://www.leroymerlin.fr/produits/batardeau-anti-inondation-blanc-h-400-x-l-900-mm-barriere-etanche-atole-97346154.html).
- `[MANQUANT]` Rapport d'essai hydraulique indépendant pour Nerolis et Batardeau.shop, taux de fuite, pression maximale, cycles de réutilisation et responsabilité produit.
- `[MANQUANT]` Coût rendu, emballage, casse/déformation, pièces détachées, stock France/UE et notice française d'une future fiche fournisseur.
- `[HYPOTHESE]` Une erreur de mesure ou une promesse d'“étanchéité parfaite” non prouvée peut produire un sinistre majeur et un litige disproportionné. La phase fournisseur devra être plus stricte que pour un produit décoratif.

### Motif du verdict

Le cluster nettoyé dépasse 10 000, quatre spécialistes comparables démontrent le marché, le prix d'entrée est dans la cible et la présence des grandes enseignes correspond surtout à de la distribution de marques spécialistes. Une offre pédagogique et standardisée a une raison d'exister. Le risque élevé n'annule pas le marché ; il devient un **gate fournisseur et commande test obligatoire**.

### Gates avant toute validation fournisseur

Une future phase 4 ne pourra retenir qu'une fiche exacte réunissant au minimum :

1. barrière pour ouverture de porte, pas sac, boudin, digue au sol ni accessoire ;
2. largeur et hauteur de retenue explicitement sélectionnables ;
3. système de joint et conditions de support documentés ;
4. instructions de mesure, pose, entretien et stockage ;
5. rapport d'essai ou protocole hydraulique vérifiable — une simple promesse vendeur ne suffit pas ;
6. pièces d'usure/remplacement disponibles ;
7. poids, colis, prix rendu France, délai et politique de retour exacts ;
8. aucune promesse absolue d'absence d'inondation sans limites d'usage.

Sans ces huit points, le résultat de phase 4 devra être `AUCUNE_FICHE_EXACTE`, pas un fournisseur approximatif.

---

## 3. Sac de couchage duvet premium 3 saisons

### Verdict

**STOP_MARCHE** — ne pas envoyer en phase 4.

### Demande et intention

- `[OBSERVE]` Volume SEMrush France amont : **15 880 recherches/mois** sur le cluster d'usage, mais seulement **110** sur les formulations explicites duvet/premium.
- `[OBSERVE]` La requête générique `sac de couchage` représente **14 800** ; elle couvre plusieurs températures, saisons, matières et niveaux de prix.
- `[HYPOTHESE]` La demande commerciale existe, mais le différenciateur “duvet premium 3 saisons” n'est presque pas nommé. L'acheteur compare plutôt température de confort, poids, volume, fill power, marque et prix.
- `[MANQUANT]` Volume nettoyé par plage de température 0–5 °C, usage trek/bivouac et normes d'essai.

### Concurrents DTC / spécialistes comparables

| Spécialiste | Prix exact visible | Offre et preuve observées | Lecture stratégique |
|---|---:|---|---|
| [Arknor — AEGISMAX duvet 5 °C, adulte grand](https://arknor.com/products/sac-couchage-duvet-5c-aegismax-momie-longue-700-cuin) | **209,90 EUR**, prix comparé affiché 390 EUR | 700 cuin annoncé, 5–15 °C, grande longueur jusqu'à 2 m, trois coloris | Occupe déjà l'angle générique/dropship premium et l'angle “grands adultes”, avec forte promotion permanente apparente. |
| [Cumulus — Mysterious Traveller 500](https://cumulus.equipment/fr/eu/p/sacs-de-couchage-en-duvet-mysterious-traveller-500) | **319 EUR** | 3 saisons, confort 1 °C, limite −5 °C, 700 FP, 500 g de duvet, 910 g, configuration possible, garantie “Lifetime Experience” | Gagne par fiche technique complète, personnalisation et réputation de spécialiste ultraléger. |
| [Triple Zéro — Ansabère](https://www.triplezero.fr/fr/c/sacs-de-couchage/ansabere) | Configuration affichée : **358 EUR TTC** | Duvet d'oie, fabrication artisanale française, tailles et 400–800 g de duvet sélectionnables | Gagne par fabrication française, savoir-faire et personnalisation ; terrain difficile à reproduire avec un produit générique. |
| [Valandré — Swing CO 650](https://www.valandre.com/fr/sacs-de-couchage/24-swing-co-650.html) | **309 USD** affichés sur la page France ; non intégré au benchmark EUR | Confort −2 °C et limite −8 °C, test EN ISO 23537 téléchargeable, duvet français 90/10 650+ cuin | Preuve du standard technique attendu. `[MANQUANT]` Prix France en EUR fiable à cause de l'anomalie de devise affichée. |

### Repères grandes enseignes / grands retailers spécialisés

| Enseigne | Prix exact visible | Ce que cela prouve |
|---|---:|---|
| [Decathlon — MT900 duvet 0 °C](https://www.decathlon.fr/p/sac-de-couchage-de-trekking-0degc-en-duvet-leger-et-compact-mt900/355074/c405m8882708) | **219,99 EUR** | 0 °C confort, −5 °C limite, 700/800 cuin, 42 avis affichés, garantie 5 ans et retours fidélité jusqu'à 365 jours. Référence difficile à battre à prix égal. |
| [Hardloop — sacs 0 à 5 °C](https://www.hardloop.fr/produits/1554-sacs-de-couchage-entre-0c-et-5c) | 176 résultats ; exemples affichés : Millet Light Down 0 °C **199,90 EUR**, Therm-a-Rest Questar 0 °C **279,90 EUR**, Rab Ascent 0 °C **310,90 EUR** | Très forte profondeur de catalogue, marques reconnues, promotions fréquentes, conseil expert et retour gratuit annoncé sous 100 jours. |

### Prix, domination et commoditisation

- `[OBSERVE]` Le cœur 200–360 EUR est déjà occupé simultanément par un DTC générique, des artisans, des marques techniques, Decathlon et un grand retailer comptant 176 références sur la seule plage 0–5 °C.
- `[OBSERVE]` La comparaison se fait sur des spécifications vérifiables : température confort/limite, norme d'essai, quantité et type de duvet, cuin/FP, poids, volume, dimensions, zip, garantie et retours.
- `[OBSERVE]` Hardloop affiche de nombreuses remises de 10 à 34 % sur des marques établies, ce qui réduit l'espace d'une offre générique au prix catalogue.
- `[HYPOTHESE]` Le marché est **fortement dominé et commoditisé sur la performance**, même si les marques conservent une forte différenciation de confiance.

### Thèse de différenciation testée puis rejetée

> Pour les randonneurs grands gabarits qui veulent un sac 3 saisons compact sans payer une marque d'expédition, vendre un duvet long 0–5 °C avec température testée, guide morphologique et kit de stockage.

Cette thèse n'ouvre pas un terrain propre : Arknor occupe déjà le grand gabarit à 209,90 EUR, Decathlon offre une fiche plus rassurante à 219,99 EUR, Cumulus propose la configuration et Triple Zéro l'artisanat français. Le “premium” générique ne résiste donc pas à la comparaison.

### Risques et logistique

- `[OBSERVE]` Les leaders publient températures de confort et limite, fill power, poids de duvet, poids total, dimensions et garanties ; Valandré fournit un test EN ISO 23537.
- `[MANQUANT]` Rapport d'essai thermique indépendant sur le produit Arknor observé, traçabilité du duvet, certification bien-être animal et cohérence exacte des tailles/poids.
- `[MANQUANT]` Coût rendu, taux de retour par taille/température ressentie et durabilité après lavage d'une future fiche fournisseur.
- `[HYPOTHESE]` Les écarts entre température annoncée et ressentie, l'humidité, la morphologie et le matelas utilisé généreraient un SAV élevé pour une marque inconnue.
- `[HYPOTHESE]` Un produit compressible est logistiquement plus simple que les deux autres candidats, mais cet avantage ne compense pas la domination concurrentielle.

### Motif du verdict

Le volume générique dépasse le seuil et le prix est compatible, mais le différenciateur exact ne représente que 110 recherches et aucune thèse défendable n'échappe aux offres déjà visibles. Le critère canonique rejette les catégories dominées par des marques incontournables lorsqu'une offre générique ne peut pas être défendue. Verdict `STOP_MARCHE`.

---

## Classement et prochaine porte

1. **Batardeau pour porte — GO_MARCHE.** Seul candidat à transmettre ultérieurement à un agent de phase 4, avec les huit gates techniques ci-dessus.
2. **Voile d'ombrage coco — CAS_LIMITE_MARCHE.** Ne continue pas ; réouverture seulement avec nouvelle preuve de demande spécifique ou thèse bundle distincte.
3. **Sac de couchage duvet 3 saisons — STOP_MARCHE.** Fermeture avant sourcing.

## État opérationnel final

- `[FAIT]` Trois audits SERP/prix/différenciation France documentés.
- `[FAIT]` Trois à quatre spécialistes/DTC analysés par candidat, avec prix visibles ou anomalie explicitement marquée.
- `[FAIT]` Repères grandes enseignes séparés.
- `[FAIT]` Un seul `GO_MARCHE`, sans abaissement des critères.
- `[MANQUANT]` CPC et économie ; à traiter après sourcing exact du seul candidat GO.
- `[NON FAIT — HORS PERIMETRE]` AliExpress, Shopify, DSers, import, publication, commande et lancement.

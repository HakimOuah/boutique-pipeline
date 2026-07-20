# Registre central des candidats produit

Ce fichier est la mémoire du pipeline de recherche produit. **Tout agent doit le lire avant de travailler et l'orchestrateur le met à jour après chaque phase.**

Règles d'usage :

- Une ligne par produit jamais étudié. Les synonymes servent à l'anti-doublon (singulier/pluriel, accents, français/anglais, variantes proches, même usage client).
- Un produit en STOP ou rejeté ne peut pas être re-proposé, sauf thèse réellement nouvelle documentée, marquée `déjà recherché — reprise motivée`.
- Un **vivier** n'est ni un STOP ni un rejet : c'est un marché à volume réel écarté sur le seul critère du ticket. Il peut être repris sans reprise motivée dès qu'un projet de boutique en change le périmètre de prix.
- Le registre pointe vers les rapports ; il ne remplace jamais leur détail ni leurs réserves.
- Niveaux de validation : 1 = marché, 2 = fiche AliExpress, 3 = commande test, 4 = GO lancement. Aucun raccourci entre niveaux.

Dernière mise à jour : 20 juillet 2026 (chasse clusters : premier candidat retenu — fontaine à gravité, confiance A, dry-run complet de la chaîne sur la famille 7 ; familles 1 et 16 balayées sans candidat ; viviers punch needle, douche filtrante, filtre robinet, outillage frigoriste).

## Chasse clusters — boucle volume-first (lancée le 20 juillet 2026)

Objectif : 20 candidats qualifiés (volume mesuré, concurrence chiffrée, fiche AliExpress vérifiée), **tous chemins confondus** — balayage `/chasse-clusters` (voie secondaire depuis le 20/07) et qualification express d'idées `/qualifie-idees` (voie principale) alimentent ce même tableau et ce même compteur. Design : [specs/2026-07-20-boucle-chasse-clusters-design.md](specs/2026-07-20-boucle-chasse-clusters-design.md). État du balayage : [familles-exploration.md](familles-exploration.md).

Chaque ligne a passé le contrôle de `critique-candidat`. Aucune n'est allée jusqu'à la phase 5 : le choix des candidats à pousser appartient à Hakim.

**Niveau de confiance fournisseur** (décision de Hakim du 20/07/2026 — la case fournisseur prouve que le produit est sourçable, pas que le vendeur est bon) :

- **A** — avis solides **et** expédition France ou UE ;
- **B** — une seule des deux forces : avis solides mais expédition Chine, ou pas d'avis mais expédition France/UE ;
- **C** — pas d'avis **et** expédition Chine, mais fiche vérifiée et correspondant au produit. Retenu, à valider par commande test.

**Compteur : 1 / 20**

| # | Candidat | Cluster et volume pertinent | Prix marché | Concurrents (institutionnels / dropship) | Fournisseur AliExpress | Confiance | Réserves | Date |
|---|---|---|---|---|---|---|---|---|
| 1 | **Fontaine à eau filtrante à gravité, grande capacité** | `fontaine filtrante` + `filtre gravité` ≈ **13 000–15 500/mois** nettoyé ([phase 3](reports/phase3-demande-traitement-de-l-eau-2026-07-20.md)) | Cœur 150–420 € (EVA 179–295, Weeplow 179,99–199,99, Orinko 179,99, Berkefeld 265–320, Berkey 200–416) | Spécialistes DTC dominants en organique (7+ identifiés) / dropship non isolé ; GSB = bornes de prix seulement ; VEVOR 70–106 € en ancre basse | [Fiche 1005008291010462](https://fr.aliexpress.com/item/1005008291010462.html) : 8,5 L inox, **86,99 € rendu, expédié France 2–8 j**, 4,9/5 · 32 avis · 127 vendus, vendeur SucceBuy 95,9 % ; backup + repli Pologne sans titre VEVOR ; [cartouches 32,19 €](https://fr.aliexpress.com/item/1005010470376800.html) même vendeur ([phase 4](reports/phase4-sourcing-fontaine-gravite-2026-07-20.md)) | **A** | 11 réserves du [contrôle critique](reports/phase4-sourcing-fontaine-gravite-2026-07-20.md) dont 3 majeures : logo VEVOR possible sur la cuve livrée (contrôle prioritaire commande test), conformité contact alimentaire non documentée (aucun claim santé), statut Berkey non instruit juridiquement. Niveau 2 (fiche) — pas de GO fournisseur, commande test = décision Hakim | 2026-07-20 |

### Familles balayées sans candidat

| Famille | Date | Clusters mesurés | Issue | Rapports |
|---|---|---|---|---|
| 16 — Loisirs créatifs & artisanat (dry-run) | 2026-07-20 | Tufting 13 110 (contrôle, déjà au registre) ; punch needle 17 850 ; résine époxy sol 23 500 (hors périmètre famille) | 0 candidat, 1 vivier | [phase 0](reports/chasse-clusters-loisirs-creatifs-artisanat-2026-07-20.md) |
| 1 — Atelier & outillage (dry-run) | 2026-07-20 | Servante d'atelier ≈ 30 300 ; établi ≈ 36 400 | 0 candidat — **shortlist vide en phase 2**, les 9 produits dérivés rejetés au §4 (Facom/KS Tools/Stanley/Wolfcraft + Leroy Merlin/Brico Dépôt/Castorama/Lidl attestés dans le vocabulaire mesuré). Ne pas re-dériver ces produits depuis cette famille sans reprise motivée. 1 vivier (outillage frigoriste) | [phase 0](reports/chasse-clusters-atelier-outillage-2026-07-20.md) · [phase 2](reports/phase2-filtre-atelier-outillage-2026-07-20.md) |
| 2 — Travail du bois | 2026-07-20 | Défonceuse ≈ 24 610 ; raboteuse-dégauchisseuse ≈ 22 780 ; scie sur table ≈ 22 410 ; fraises défonceuse ≈ 11 350 | 0 candidat — **shortlist vide en phase 2**, 4 rejets instruits avec tentative de thèse : défonceuse (tranche = marques uniquement, générique sous 110 €), scie sur table (Dexter 239 € + VEVOR 178,51 € dans la tranche), raboteuse-dégauchisseuse (tranche quadrillée par 7 offres de marques + VEVOR 317,90 €, pédagogie insuffisante face au quadrillage — contestable par reprise motivée), fraises (promesse qualité invérifiable, pas un vivier : indéfendabilité, pas seulement ticket). Sonde : 4/4 dans la tranche. Ne pas re-dériver sans reprise motivée | [phase 0](reports/chasse-clusters-travail-du-bois-2026-07-20.md) · [phase 2](reports/phase2-filtre-travail-du-bois-2026-07-20.md) |
| 3 — Travail du métal & soudure | 2026-07-20 | Poste à souder ≈ 36 000 (tête seule 12 100) ; masque soudure ≈ 12 700 ; plieuse tôle/zinc ≈ 11 600 ; soudure laser ≈ 14 300 au parent | 0 candidat — poste à souder et masque rejetés phase 2 (§4 : GYS/Stanley/Lincoln/ESAB dans la tranche, Parkside 4 400/mois ; premium optique verrouille la tranche masque), laser rejeté (offre réelle ≥ 2 800 €, hors tranche par le haut — ni STOP ni vivier, re-mesurable si le périmètre de prix change), plieuse SEULE SURVIVANTE phase 2 puis **STOP marché en phase 3** (voir section STOP). Ne pas re-dériver sans reprise motivée | [phase 0](reports/chasse-clusters-travail-du-metal-soudure-2026-07-20.md) · [phase 2](reports/phase2-filtre-travail-du-metal-soudure-2026-07-20.md) · [phase 3](reports/phase3-demande-plieuse-tole-2026-07-20.md) |
| 4 — Auto/moto atelier & diagnostic | 2026-07-20 | Cric ≈ 30 500 ; presse hydraulique ≈ 15 700 ; pont élévateur 13 820 ; lève-moto ≈ 11 580 ; béquille moto ≈ 10 920 ; grue/chèvre ≈ 15 990 (sous réserve synonymie) | **0 retenu mais 2 dossiers remontés à Hakim** : presse hydraulique À APPROFONDIR (≈ 15 500–16 800 nettoyé) et lève-moto CAS LIMITE (voir section Cas limites). Rejets phase 2 : cric (§4 : Lidl/Brico Dépôt attestés + VEVOR/Facom dans la tranche), pont élévateur (hors tranche par le haut, entrée réelle 449 €), grue/chèvre (Norauto 169,99 € et Roady 179,90 € tiennent l'entrée de tranche + réserve synonymie), béquille → vivier. OBD2 écarté d'office (rejet 16/07). Ne pas re-dériver sans reprise motivée | [phase 0](reports/chasse-clusters-auto-moto-atelier-diagnostic-2026-07-20.md) · [phase 2](reports/phase2-filtre-auto-moto-atelier-2026-07-20.md) · [phase 3](reports/phase3-demande-auto-moto-atelier-2026-07-20.md) |

### STOP marché issus de la chasse

| Candidat | Synonymes | Verdict | Motif |
|---|---|---|---|
| Adoucisseur compact sans électricité pour appartement | adoucisseur appartement, adoucisseur compact, adoucisseur sans électricité | **STOP marché** (20/07/2026) — segment ≈ 2 900–3 400/mois | Règle hiérarchique appliquée : le parent `adoucisseur d'eau` (40 500) sert exclusivement l'adoucisseur classique posé 450–1 300 €, GSB + installateurs ; annonces texte = installateurs ([phase 3](reports/phase3-demande-traitement-de-l-eau-2026-07-20.md)) |
| Plieuse de tôle / zinc manuelle d'établi | plieuse tole, plieuse zinc, plieuse manuelle, plieuse d'établi | **STOP marché** (20/07/2026) — adressable ≈ 5 000–6 500/mois | Unité tôle/zinc invalidée en SERP : établi 52–402 € vs couvreur 749–6 811 € (Jouanel/Dimos prescripteurs), deux mondes non mutualisables. Espace spécialiste déjà occupé par des domaines exacts (plieuse-tole.com, plieuse-atelier.fr, plieuse-zinc.fr). Persona zinc = pro/chantier ([phase 3](reports/phase3-demande-plieuse-tole-2026-07-20.md)) |

### Viviers — volume réel, ticket incompatible

Marchés dont la demande est mesurée et réelle, mais dont le prix pratiqué est nettement sous la tranche 150–400 €. **Ce ne sont pas des rejets** : ils sont mis de côté pour une éventuelle boutique mêlant low et high ticket, et l'anti-doublon ne doit pas les traiter comme des STOP.

Écartés par `sonde-prix` avant la phase 3, pour ne pas payer un audit SERP complet sur un ticket qu'une lecture de Google Shopping suffit à disqualifier.

| Cluster | Volume pertinent | Fourchette de prix constatée | Note | Date |
|---|---|---|---|---|
| Punch needle (pratique et kits) | 17 850 (plancher mesuré, [balayage famille 16](reports/chasse-clusters-loisirs-creatifs-artisanat-2026-07-20.md)) | 25–30 € (vérifié par Hakim le 20/07/2026) | Volume supérieur au tufting. CPC 0,10–0,37 € et présence Action/Gifi/Zeeman cohérents avec le ticket. Voisin direct du tufting : candidat naturel pour une boutique loisirs créatifs mêlant machines high-ticket et consommables low-ticket | 2026-07-20 |
| Outillage frigoriste | Non mesuré en cluster (repéré au [balayage famille 1](reports/chasse-clusters-atelier-outillage-2026-07-20.md)) | Non sondée | **Poche repérée, non instruite.** CPC 1,72 € — le plus élevé de toute la famille 1, signal d'intention pro à ticket élevé. Repérée par la phase 2 sans pouvoir être instruite (hors vocabulaire des clusters mesurés). À re-mesurer en phase 0 si reprise | 2026-07-20 |
| Douche filtrante anti-calcaire | ≈ 34 700 plancher ([phase 0 famille 7](reports/chasse-clusters-traitement-de-l-eau-2026-07-20.md)) | 7–145 € (sonde 20/07) — l'unité plafonne ~140 € | Volume important, gros de l'offre 7–40 €, étage DTC 59–99 €. Complément naturel d'une boutique construite autour de la fontaine à gravité (candidat n°1) | 2026-07-20 |
| Filtre sur robinet (format littéral) | ≈ 31 260 plancher famille, format littéral 17–80 € (sonde 20/07) | 17–80 € | La valeur dans la tranche sur cette requête est servie par gravité/sous évier — captée par le candidat n°1. Le format littéral lui-même est low-ticket, complément de gamme possible | 2026-07-20 |
| Poches famille 7 non instruites | — ([phase 2](reports/phase2-filtre-traitement-de-l-eau-2026-07-20.md)) | Non sondées | **Poches repérées, non instruites** : station filtration maison entière (borderline phase 0), charbon binchotan (≈ 6 200), pommeau douche coréen, PFAS (angle réassurance émergent), traitement eau camping-car (→ famille 32), consommables adoucisseur | 2026-07-20 |
| Poches famille 2 non instruites | — ([phase 2](reports/phase2-filtre-travail-du-bois-2026-07-20.md)) | Non sondées | **Poches repérées, non instruites** : gabarits/guides de précision défonceuse dont queue d'aronde (seul territoire de la famille où la valeur ne dépend pas de la marque de la machine — à re-mesurer en phase 0 en priorité), table de défonceuse (≈ 6 790 sous seuil), aspirateur à copeaux (→ croiser famille 8), affleureuse, scie à onglet, mortaiseuse | 2026-07-20 |
| Poches famille 3 non instruites | — ([phase 2](reports/phase2-filtre-travail-du-metal-soudure-2026-07-20.md)) | Non sondées | **Poches repérées, non instruites** : table de soudure 2D (≈ 4 400, CPC 0,72–0,75 €), rouleuse/cintreuse/cisaille (était liée au sort de la plieuse, désormais STOP — re-mesure possible en propre), aspiration fumées soudure (→ famille 8), spot welder batterie (→ famille 6), forge coutellerie (→ famille 18), masque soudure générique low-ticket, vocabulaire « Tiger » à identifier | 2026-07-20 |
| Béquille d'atelier moto | ≈ 10 920 strict ([phase 0 famille 4](reports/chasse-clusters-auto-moto-atelier-diagnostic-2026-07-20.md)) | 30–70 € unitaire, sets 111–179 € (sonde 20/07) | Volume au seuil mais ticket incompatible : la tranche n'est atteinte qu'en plancher par des sets déjà standard (ConStands, Motea, KTM). Complément naturel d'une boutique atelier moto si le lève-moto (cas limite) est validé par Hakim | 2026-07-20 |
| Poches famille 4 non instruites | — ([phase 2](reports/phase2-filtre-auto-moto-atelier-2026-07-20.md)) | Non sondées | **Poches repérées, non instruites** : démonte-pneu manuel moto (≈ 5 810, la plus proche du seuil — compléter par décolle-pneu/détalonneur), table élévatrice moto (montée de gamme du lève-moto), chandelles, compresseur d'atelier, pont mobile, support moteur, vérin hydraulique | 2026-07-20 |

### Cas limites remontés à Hakim

| Candidat | Cluster | Point à trancher | Date |
|---|---|---|---|
| **Lève-moto hydraulique** (famille 4) | ≈ 8 000–10 500/mois pertinent — toute la fourchette défendable est dans la bande ±20 % du seuil | CAS LIMITE réglementaire, non tranché par la [phase 3](reports/phase3-demande-auto-moto-atelier-2026-07-20.md). Double lecture documentée : 70–80 % du générique `leve moto` est du stand cross < 150 € (lecture basse), mais la racine `cric moto` (≈ 2 900) est confirmée même objet en SERP et la couche 190–295 € est servie par un mixte non dominant (Torros en annonce texte spécialiste, Motea/ConStands présents non dominants). Si GO de Hakim → phase 4 sourcing | 2026-07-20 |
| **Presse hydraulique d'atelier 12–20 t** (famille 4) | ≈ 15 500–16 800/mois pertinent — nettement au-dessus du seuil | **À APPROFONDIR** (pas un cas limite volume) : demande là, prix 166–380 € dans la tranche, pas de verrou domaine exact. Obstacles documentés : Consogarage seul en annonce texte sur les 2 requêtes décisives (~100 k visites/mois revendiquées), BPAC occupe l'organique avec le discours « roulements » de la thèse, pack accessoires déjà existant (Carmax 20 t + 52 pcs à 299,90 € Amazon), sécurité machine + fret lourd (108–132 € livraison). Si Hakim veut avancer → phase 4 sous conditions | 2026-07-20 |

## Produits lancés

| Produit | Boutique | Statut | Notes |
|---|---|---|---|
| Osmoseur (traitement de l'eau) | Bonum Vitae | En ligne, campagne Google Ads active (30 €/jour) | Ne pas modifier boutique/Ads sans autorisation explicite de Hakim |

## Tests antérieurs non concluants

| Produit | Synonymes | Verdict | Notes |
|---|---|---|---|
| Machine à café portable | cafetière portable, machine expresso portable, mini machine café voyage | Test non concluant — clos | Ne pas re-proposer sans thèse réellement nouvelle |
| Pilates Reformer | reformer pilates, machine pilates, banc pilates | Test non concluant — clos | Ne pas re-proposer sans thèse réellement nouvelle |

## Candidats V2 — validés SEMrush le 17 juillet 2026

Source de vérité : [reports/validation-semrush-2026-07-17.md](reports/validation-semrush-2026-07-17.md)

| Candidat | Synonymes | Première étude | Dernier contrôle | Phase atteinte | Niveau validation | Verdict actuel | Notes |
|---|---|---|---|---|---|---|---|
| Kit tufting complet | tufting, tufting gun, pistolet tufting, kit fabrication tapis, punch needle machine | 2026-07-16 | 2026-07-19 | **5 (marge faite)** | 1 validé (marché) | **GO marché** — 13–17 k pertinent ; **commande test recommandée, décision Hakim en attente** | [Phase 5 du 19/07](reports/phase5-marge-kit-tufting-2026-07-19.md) : marge contributive ≈ 94 € (kit machine 229 €) à ≈ 112 € (kit complet 299 €), CPA max 94–112 € vs CPC 0,48 €, conversion break-even 0,4–0,5 %. Prix 78,61 € reconfirmé le 19/07 ; vendeur descendu à 93,1 %. Benchmark letufting.fr (SAS française, mêmes machines chinoises : gun 163–192 €, kits 280–484 €) ; différenciateur identifié : notice/pédagogie (plainte n°1 de leurs avis). Notice fournisseur AK-V/VI reçue le 19/07 ([analyse](fournisseur-docs/notice-tufting-analyse-2026-07-19.md)) : 100–240 V annoncé (bloc secteur externe), colis 2,5 kg brut, lubrification toutes les 2 h, conversion Cut/Loop par vis — tout à confirmer sur échantillon. Persona validé par Hakim le 19/07 (tutoiement) : [personas/persona-tufting-2026-07-19.md](personas/persona-tufting-2026-07-19.md). Bloquants avant tout lancement : prise UE du bloc secteur, contenu variante, CE/RoHS, facture TVA, DEEE. Budget test ≈ 870–1 120 € |
| Graveur laser fermé débutant | graveur laser, machine gravure laser, graveur laser bois, découpeuse laser diode | 2026-07-16 | 2026-07-17 | 4 (sourcing partiel) | 0 | **À APPROFONDIR** — 12–14,1 k mais `fermé` = 20/mois | Concurrence forte ; sécurité laser, extraction, conformité CE et SAV bloquent tout GO ; étude conformité séparée requise avant décision |
| Tour de potier électrique | tour poterie, roue de potier, machine poterie | 2026-07-16 | 2026-07-17 | 4 (sourcing fait) | 0 | **STOP marché** — ≈ 8 400 (proche seuil) | Fournisseur SucceBuy « retenu pour commande test » mais le fournisseur ne renverse pas le STOP marché |
| Surmatelas thermorégulé actif à eau | surmatelas rafraîchissant, refroidisseur de lit, surmatelas climatisé | 2026-07-16 | 2026-07-17 | 4 (aucune offre) | 0 | **STOP** — ≈ 1 170 | Aucune offre AliExpress exploitable ; SERP mélangée avec passif low-ticket |
| Canapé enfant modulable + motricité | canapé mousse enfant, canapé jeu enfant, parcours motricité mousse | 2026-07-16 | 2026-07-17 | 4 (sourcing partiel) | 0 | **STOP** — ≈ 1 800–2 000 | Fiche « à tester » (TLGREEN 164,39 € DE) mais aucun avis produit, stock 1 ; conformité enfant/feu à vérifier si repris |
| Robot skimmer solaire de surface | robot surface piscine, skimmer solaire piscine, robot ramasse feuilles | 2026-07-16 | 2026-07-17 | 4 (sourcing partiel) | 0 | **STOP** — ≈ 2 300–2 600 | Très saisonnier ; vendeur 82,3 % très insuffisant |
| Bateau amorceur GPS avec sondeur | bateau amorceur sondeur, bateau amorceur carpe gps | 2026-07-16 | 2026-07-17 | 4 (sourcing partiel) | 0 | **STOP** — ≈ 4 390 (segment réel) | Ne jamais attribuer le générique `bateau amorceur` (5 400) au segment GPS/sondeur ; sondeur non confirmé sur la fiche présélectionnée |
| Vanne anti-fuite avec coupure | vanne anti fuite eau, coupure eau automatique, détecteur fuite avec coupure | 2026-07-16 | 2026-07-17 | 4 (sourcing partiel) | 0 | **STOP** — ≈ 50 | Demande exacte quasi nulle ; l'offre contrôlée n'inclut pas le capteur de fuite |
| Film PDLC opacifiant électrique | film opacifiant électrique, smart film, film occultant électrique, vitrage intelligent | 2026-07-16 | 2026-07-17 | 4 (sourcing partiel) | 0 | **STOP** — ≈ 1 320 | Intention B2B/pose ; délai Chine 20–29 j et vendeur 81,3 % |
| Composteur électrique de cuisine | recycleur déchets alimentaires, machine compost cuisine | 2026-07-16 | 2026-07-17 | 4 (aucune offre) | 0 | **STOP** — ≈ 600 | Aucune offre AliExpress exploitable |
| Piège à moustiques CO2 extérieur | piège moustique co2, borne anti moustique, piège moustique tigre | 2026-07-16 | 2026-07-17 | 4 (aucune offre) | 0 | **STOP** — ≈ 5 120 | Saisonnier, preuves d'efficacité sensibles ; aucun vrai piège CO2 trouvé sur AliExpress |
| Nettoyeur ultrason 10–15 L | nettoyeur ultrason professionnel, bac ultrason 10l, machine nettoyage ultrason | 2026-07-16 | 2026-07-17 | 4 (sourcing partiel) | 0 | **STOP** — ≈ 3 090 | Segment commoditisé ; variante 10 L et prix rendu jamais confirmés |
| Suspension sculpturale rotin XXL | suspension rotin, luminaire rotin, suspension osier | 2026-07-16 | 2026-07-17 | 4 (sourcing partiel) | 0 | **STOP** — ≈ 720 (cluster XXL) | Indication Hakim (17/07, non vérifiée en base) : `suspension rotin` seul ≈ 9 000/mois — reprise éventuelle possible via la règle d'exploration hiérarchique, à re-mesurer en phase 3 avant toute conclusion ; dimensions XXL de la fiche AliExpress jamais confirmées |

## Analyses express broyeur — 18 juillet 2026 (9 niches imposées, toutes NO_GO)

Analyse demandée par Hakim (hors pipeline complet — pas de phase 3 exhaustive). Données live du 18/07/2026, score par le moteur réel `dropilot.ScoringEngine`. Rapports : [lot 1](reports/analyse-broyeur-niches-2026-07-18-lot1.md) · [lot 2](reports/analyse-broyeur-niches-2026-07-18-lot2.md) · [synthèse scorée](reports/analyse-broyeur-niches-2026-07-18-synthese.md)

| Niche (segment analysé) | Synonymes | Verdict 18/07/2026 | Motif résumé |
|---|---|---|---|
| Table de massage (pro/électrique) | table massage pliante, table esthétique | NO_GO — score broyeur 26 | Meilleur score du lot ; ratio de marge 1,78, cœur de demande < 150 € ; seul signal résiduel : segment électrique/instituts |
| Machine à pop-corn pro/forain | machine popcorn, machine à pop corn professionnelle | NO_GO — score 22 | Segment 150 €+ ≈ 1 350/mois seulement ; VEVOR écrase les prix |
| Store banne motorisé (stores/rideaux) | store banne, store terrasse, store extérieur | NO_GO — dominance enseignes (35 hors filtres) | 90–100 k/mois mais Leroy Merlin/Castorama/Brico Dépôt ; saisonnalité forte ; colis 30–80 kg |
| Grilles/échelles de boulangerie | échelle pâtissière, chariot échelle 600x400 | NO_GO — dominance enseignes CHR | ≈ 650/mois ; METRO/Retif/Matfer ; aucun sourcing AliExpress crédible |
| Transpalette/gerbeur (chariots élévateurs) | transpalette manuel, gerbeur électrique | NO_GO — dominance enseignes | 60–63 k/mois mais marge estimée négative (coût AliExpress ≈ prix SERP) ; B2B pur |
| Chambre froide | chambre froide positive/négative | NO_GO — ticket > 2 000 € | B2B pur, F-Gas, fret palette ; hors modèle pipeline |
| Robot pâtissier | robot pétrin, robot de cuisine pâtissier | NO_GO — ticket < 150 € | 45 k/mois hors marques mais générique 60–200 € ; tranche 150–400 € = marques |
| Fourneau professionnel (piano CHR) | piano de cuisson professionnel, fourneau CHR | NO_GO — ticket > 2 000 € | ≈ 3 250/mois ; Falcon/Lacanche/CHR ; gaz, > 100 kg |
| Chariot de bar / desserte | bar cart, desserte à roulettes | NO_GO — ticket < 150 € (score 0 hors filtres) | ≈ 1 100/mois ; IKEA/But ; pénalité barrière faible + grandes marques |

## Recherche en cours — exploration libre (lancée le 17 juillet 2026)

Rapports : [phase 1](reports/phase1-ideation-exploration-libre-2026-07-17.md) (20 idées, 25 écartés) · [phase 2](reports/phase2-filtre-exploration-libre-2026-07-17.md) (9 en shortlist, 11 rejets)

En shortlist après phase 2 (17/07/2026) :

| Candidat | Première étude | Phase atteinte | Verdict actuel | Note courte |
|---|---|---|---|---|
| Kit atelier vitrail Tiffany complet | 2026-07-17 | 3 | **STOP marché** — ≈ 3 000–4 400 pertinent | Parent `vitrail` 8 100 adressable à ~10–15 % seulement (SERP artisanat d'art/culture) ; kits spécialistes déjà en place 78–186 € — « bundle inexistant » partiellement invalidé ([lot A](reports/phase3-demande-exploration-libre-lot-a-2026-07-17.md)) |
| Rouet électrique e-spinner filage laine | 2026-07-17 | 3 | **STOP marché** — ≈ 1 000–1 500 pertinent | Produit ≈ 190/mois ; même 100 % du parent `rouet` laisse l'univers < 5 000 ; public étroit confirmé par la mesure |
| Torréfacteur de café domestique | 2026-07-17 | 3 | **STOP marché** — ≈ 250–350 pertinent (appareil) | Le brut 22 060 = torréfacteurs-artisans locaux ; formulations machine 0–20/mois ; un seul marchand d'appareils visible en SERP |
| Tour hydroponique intérieur grand format | 2026-07-17 | 3 | **STOP marché** — ≈ 2 500–3 500 pertinent | Demande tour ≈ 950, fortement DIY (tutos « moins de 10 € ») ; parent hydroponie = growshops, exclu |
| Triangle de Pickler évolutif | 2026-07-17 | 3 | **STOP marché** — ≈ 2 500–3 500 pertinent (triangle seul ≈ 800) | Decathlon en propre 40,99–340,99 €, BUT/Lidl/VEVOR présents ; angle « set évolutif » déjà occupé (LOOVE 4-en-1, GOPLUS 9-en-1) ; cluster mesuré seul, sans mutualisation mousse |
| Meuble-niche design pour chien | 2026-07-17 | 3 | **STOP marché** — ≈ 4 000–6 700 pertinent | Parent `niche pour chien` 12 100 = 100 % extérieur en SERP, non attribuable ; milieu 250–400 € déjà servi (VEVOR 288–380 €, Jardiland, Aosom) ([lot B](reports/phase3-demande-exploration-libre-lot-b-2026-07-17.md)) |
| **Catio enclos extérieur chat** | 2026-07-17 | 4 | **CLOS — décision Hakim (19/07/2026)** | Hakim a re-contrôlé SEMrush lui-même : volume jugé beaucoup trop bas → candidat abandonné avant la phase 5. Divergence documentée sans être tranchée : la phase 3 estimait 13 000–17 000 en additionnant trois familles (catio + enclos extérieur + parc), là où le mot-clé exact `catio` seul fait 2 400 — l'écart vient de l'attribution des familles. Décision de Hakim actée ; ne pas re-proposer sans reprise motivée. Historique conservé : GO marché phase 3 ([lot B](reports/phase3-demande-exploration-libre-lot-b-2026-07-17.md)), fournisseur à tester cas limite ([phase 4](reports/phase4-sourcing-catio-2026-07-17.md), PawHut 121,82 € rendu, vendeur 94,2 %) |
| Mur végétal intérieur modulaire | 2026-07-17 | 3 | **STOP marché** — ≈ 2 800–4 400 pertinent (équipement vivant) | Parent `mur vegetal` 9 900 = artificiel/stabilisé/prestation en SERP ; un seul kit vivant visible (EVERTIA 154,95 €) ; KD 2–7 sur les kits mais marché trop petit |
| Meuble de couture escamotable | 2026-07-17 | 3 | **STOP marché** — ≈ 3 000–4 500 pertinent | `meuble couture escamotable` = 20/mois ; marché bimodal verrouillé (pliant ≤ 222 € marketplace/VEVOR vs merceries 899–3 863 €) ; pollution de marque « Meubles Couture » |

Rejetés en phase 2 (17/07/2026, motifs détaillés dans le rapport) : cuve de brassage (marques + spécialistes + VEVOR), moulin à farine (Mockmill dès 279 €), presse à huile (thèse impossible sans claims santé), tour à bois (VEVOR direct), machine lapidaire (Kaufland 156 € + marché mince + lithothérapie), distillateur d'eau (générique comparable + moteur santé interdit), kit sérigraphie (Lisoni/Dipilu occupent l'espace — hypothèse phase 1 invalidée), machine à corder (étau VEVOR/Stringway), résine époxy (Epodex/Red Epoxy + CLP), kit bassin (logistique + saisonnalité), espalier suédois (indéfendable sans claims posture).

## Recherche nettoyeur ultrason — reprise motivée du 17 juillet 2026 (CLOSE en phase 3)

Reprise motivée demandée explicitement par Hakim le 17/07/2026 sur une niche dont le segment 10–15 L est en STOP. Close le jour même : quatre STOP marché en phase 3, aucun cas limite.

Contrôle international du 19/07/2026 (Keyword Overview, mot-clé exact, CPC USD) : `ultrasonic cleaner` US 33,1 k (KD 44) et UK 9,9 k (KD 20) ; `ultraschallreiniger` DE 22,2 k (KD 43, 12 annonces) ; `pulitore (a/ad) ultrasuoni` IT ≈ 2,5 k cumulé ; `limpiador ultrasonico/ultrasonidos` ES ≈ 1,3 k. Volumes bruts non nettoyés — les variantes dominantes (brille/jewelry/retainer/tooth) suggèrent le même profil low-ticket qu'en France ; aucune validation marché n'a été faite sur ces bases.

Approfondissement Allemagne du 19/07/2026 ([rapport détaillé](reports/analyse-allemagne-ultrason-2026-07-19.md)) : structure miroir de la France en plus défavorable — segment atelier 150–400 € ≈ 4–5 k visibles (dont vergaser ≈ 2,5–3 k), marques pro locales (Elma, Bandelin, EMAG), spécialiste installé Ultraschall-Welt, VEVOR.de dense sur les tailles atelier (10 L 96,80 € → 30 L 187 €), prestation carburateur à 69 € (Macht Shop). Conclusion indicative : mêmes signaux STOP qu'en France ; seuil DE non configuré dans pipeline.yaml (null) — à fixer avant toute validation formelle.

Approfondissement États-Unis du 19/07/2026 ([rapport détaillé](reports/analyse-usa-ultrason-2026-07-19.md)) : marché massif (372 k brut, tête 33,1 k) mais verrouillé — dentaire/aligneurs 38–40 k (claims santé + Invisalign), bijoux 20 k low-ticket, atelier ≈ 9–10 k dominé par Harbor Freight (99–170 $, milliers d'avis) et VEVOR (requête de marque à 3 600/mois), armes/rechargement 5–6 k inexploitable en Ads, prestations carbu à 10–50 $. Annonces texte Search confirmées (Sharpertek, fabricants CN). Hors périmètre opérationnel (marché US non configuré, modèle logistique européen). Conclusion indicative : pas d'opportunité pour le modèle actuel. Rapports : [phase 1](reports/phase1-ideation-nettoyeur-ultrason-2026-07-17.md) · [phase 2](reports/phase2-filtre-nettoyeur-ultrason-2026-07-17.md) · [phase 3](reports/phase3-demande-nettoyeur-ultrason-2026-07-17.md)

| Candidat | Première étude | Dernier contrôle | Phase atteinte | Verdict actuel | Notes |
|---|---|---|---|---|---|
| Kit atelier carburateurs moto/mobylette vintage (cuve + paniers + chimie + guide) | 2026-07-17 | 2026-07-17 | 3 | **STOP marché** — ≈ 5 500–6 300 pertinent | Meilleur des quatre ; même l'hypothèse haute (+part `bac ultrason`) plafonne ≈ 7 900 < 8 000 ; parent `nettoyage carburateur` 13 240 non adressable (SERP DIY/sprays) ; BPAC occupe déjà la position spécialiste, VEVOR ~155 € via enseignes ; seule poche restante : thèse « atelier mécanique large » à re-mesurer sur `bac ultrason` (5 560 brut) |
| Station nettoyage vinyles ultrason 230 V | 2026-07-16 | 2026-07-17 | 3 | **STOP marché** — ≈ 1 200–1 500 pertinent | Reprise motivée close : formulations machine quasi nulles, parent entier < 10 000 ; « milieu vacant 200–400 € » invalidé (Pro-Ject 369 €, BPAC 309,60 €, Okki Nokki 499 €) ; condition suspensive 230 V sans objet |
| Machine horlogerie à paniers rotatifs (amateur) | 2026-07-17 | 2026-07-17 | 3 | **STOP marché** — ≈ 300–560 pertinent | ~20× sous le seuil ; forums horlogers visibles en SERP déconseillent l'ultrason sur mouvements |
| Solution atelier bijoutier / créateur artisan | 2026-07-17 | 2026-07-17 | 3 | **STOP marché** — ≈ 3 000–3 300 (fraction adressable < 1 000) | Parent `nettoyage bijoux` 9 720 = DIY maison non adressable ; formulations persona pro ≈ 300 ; marché à deux étages (bacs 12–110 € vs fournituristes pro) |

Rejetés en phase 2 (17/07/2026, motifs détaillés dans le rapport) :

| Candidat | Verdict | Motif résumé |
|---|---|---|
| Nettoyeur ultrason tir sportif / rechargement | Rejet phase 2 | Politique Google Ads armes/munitions vérifiée le 17/07 : acquisition Search impraticable |
| Banc nettoyage + test injecteurs essence | Rejet phase 2 | Autool CT200 vendu en direct par VEVOR à 429,90 € ; comparaison frontale, SAV disproportionné |
| Kit ultrason waxing chaîne vélo | Rejet phase 2 | Fourchette 150–400 € inatteignable honnêtement ; marque DTC installée (Dynamic) |
| Pack hygiène tatouage/onglerie/podologie | Rejet phase 2 | Promesse d'hygiène non prouvable ; frontière dispositif médical (MDR) |
| Cuve 22–30 L « atelier restauration » | Rejet phase 2 | Aucun différenciateur vs 10–15 L STOP ; VEVOR en direct dans la fourchette |

## Niches V1 — sourcing AliExpress du 16 juillet 2026 (closes)

Sources : [reports/recherche-aliexpress-2026-07-16.md](reports/recherche-aliexpress-2026-07-16.md), [reports/aliexpress-fournisseurs-2026-07-16.xlsx](reports/aliexpress-fournisseurs-2026-07-16.xlsx), rejets V2 : [reports/recherche-produits-v2-2026-07-16.md](reports/recherche-produits-v2-2026-07-16.md)

| Candidat | Synonymes | Dernier contrôle | Verdict actuel | Notes |
|---|---|---|---|---|
| Microscope numérique 4K soudure | microscope soudure, microscope numérique électronique | 2026-07-16 | **Rejet** | Meilleur dossier fournisseur V1 (score 88, entrepôt FR) mais ≈ 150 recherches pertinentes/mois ; « 4K/48MP » gonflé (capteur 1080p) |
| Valise OBD2 bidirectionnelle | scanner obd2, valise diagnostic auto, kingbolen | 2026-07-16 | **Rejet** | KINGBOLEN S6 175 € rendu FR mais coût rendu proche du prix de vente européen du même modèle |
| Station météo 7-en-1 Wi-Fi | station météo connectée | 2026-07-16 | **Rejet** | Produit vendu partout, très comparable, dominé par enseignes/marques ; fournisseur unique |
| Caméra d'inspection canalisation | caméra canalisation, endoscope canalisation | 2026-07-16 | **Rejet** | Cluster mesuré 4 630/mois < seuil ; classe produit ambiguë (endoscope grand public vs pro) |
| Détecteur de métaux | detecteur metaux | 2026-07-16 | **Écarté** | Économiquement viable mais contrainte publicitaire L. 542-1 Code du patrimoine |
| Nettoyeur de vinyles | machine nettoyage vinyle ultrason | 2026-07-16 | **Écarté** | « 110 V » annoncé depuis entrepôt allemand : risque de non-conformité 230 V |
| Caméra thermique | camera thermique smartphone | 2026-07-16 | **Écarté** | Limites 1–3 articles/commande : réassort impossible ; résolutions gonflées |
| Scanner de films/diapositives | scanner diapositives, numériseur films | 2026-07-16 | **Écarté** | Aucun entrepôt UE, « 22 MP » douteux (≈ 14 MP réels) |
| Machine sous vide à chambre | machine sous vide professionnelle, chamber vacuum sealer | 2026-07-16 | **Écarté** | 22 kg : SAV/retours rédhibitoires ; plancher ≈ 200 € au-dessus de la cible |
| Détecteur de radon | detecteur radon | 2026-07-16 | **Écarté** | Fiabilité capteur non prouvée sur produit de sécurité sanitaire : risque juridique et éthique ; hors cible prix |

## Rejets immédiats documentés (idéation V2, 16 juillet 2026)

Source : [reports/recherche-produits-v2-2026-07-16.md](reports/recherche-produits-v2-2026-07-16.md)

| Produit | Motif |
|---|---|
| Roue d'exercice pour chat | VEVOR déjà vendu ≈ 85 € via Darty ; prix cible indéfendable |
| Mangeoire à oiseaux avec caméra | Présente chez Leroy Merlin, Darty, Decathlon, Fnac, Cdiscount ; souvent < 150 € |
| Litière automatique générique | Marché chargé, risques sécurité animale, SAV incompatible avec validation légère |
| Rideau/rouleau occultant motorisé simple | Trop accessible, Somfy et grandes enseignes, nombreux modèles < 150 € |
| Bateau amorceur simple sans GPS | Prix public < 100 € ; seul le segment GPS/sondeur était retenu (lui-même STOP depuis) |

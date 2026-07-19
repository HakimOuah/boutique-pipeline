# Registre central des candidats produit

Ce fichier est la mémoire du pipeline de recherche produit. **Tout agent doit le lire avant de travailler et l'orchestrateur le met à jour après chaque phase.**

Règles d'usage :

- Une ligne par produit jamais étudié. Les synonymes servent à l'anti-doublon (singulier/pluriel, accents, français/anglais, variantes proches, même usage client).
- Un produit en STOP ou rejeté ne peut pas être re-proposé, sauf thèse réellement nouvelle documentée, marquée `déjà recherché — reprise motivée`.
- Un **vivier** n'est ni un STOP ni un rejet : c'est un marché à volume réel écarté sur le seul critère du ticket. Il peut être repris sans reprise motivée dès qu'un projet de boutique en change le périmètre de prix.
- Le registre pointe vers les rapports ; il ne remplace jamais leur détail ni leurs réserves.
- Niveaux de validation : 1 = marché, 2 = fiche AliExpress, 3 = commande test, 4 = GO lancement. Aucun raccourci entre niveaux.

Dernière mise à jour : 19 juillet 2026 (tufting : phase 5 faite, commande test lancée par Hakim, arborescence boutique + sourcing catalogue letufting.fr documentés dans [reports/arborescence-sourcing-tufting-2026-07-19.md](reports/arborescence-sourcing-tufting-2026-07-19.md) et répliqués dans Notion).

## Chasse clusters — boucle volume-first (lancée le 20 juillet 2026)

Objectif : 20 candidats qualifiés (volume mesuré, concurrence chiffrée, fiche AliExpress vérifiée). Design : [specs/2026-07-20-boucle-chasse-clusters-design.md](specs/2026-07-20-boucle-chasse-clusters-design.md). État du balayage : [familles-exploration.md](familles-exploration.md).

Chaque ligne a passé le contrôle de `critique-candidat`. Aucune n'est allée jusqu'à la phase 5 : le choix des candidats à pousser appartient à Hakim.

**Niveau de confiance fournisseur** (décision de Hakim du 20/07/2026 — la case fournisseur prouve que le produit est sourçable, pas que le vendeur est bon) :

- **A** — avis solides **et** expédition France ou UE ;
- **B** — une seule des deux forces : avis solides mais expédition Chine, ou pas d'avis mais expédition France/UE ;
- **C** — pas d'avis **et** expédition Chine, mais fiche vérifiée et correspondant au produit. Retenu, à valider par commande test.

**Compteur : 0 / 20**

| # | Candidat | Cluster et volume pertinent | Prix marché | Concurrents (institutionnels / dropship) | Fournisseur AliExpress | Confiance | Réserves | Date |
|---|---|---|---|---|---|---|---|---|
| — | *aucun candidat retenu à ce jour* | — | — | — | — | — | — | — |

### Familles balayées sans candidat

| Famille | Date | Clusters mesurés | Issue | Rapports |
|---|---|---|---|---|
| 16 — Loisirs créatifs & artisanat (dry-run) | 2026-07-20 | Tufting 13 110 (contrôle, déjà au registre) ; punch needle 17 850 ; résine époxy sol 23 500 (hors périmètre famille) | 0 candidat, 1 vivier | [phase 0](reports/chasse-clusters-loisirs-creatifs-artisanat-2026-07-20.md) |
| 1 — Atelier & outillage (dry-run) | 2026-07-20 | Servante d'atelier ≈ 30 300 ; établi ≈ 36 400 | 0 candidat — **shortlist vide en phase 2**, les 9 produits dérivés rejetés au §4 (Facom/KS Tools/Stanley/Wolfcraft + Leroy Merlin/Brico Dépôt/Castorama/Lidl attestés dans le vocabulaire mesuré). Ne pas re-dériver ces produits depuis cette famille sans reprise motivée. 1 vivier (outillage frigoriste) | [phase 0](reports/chasse-clusters-atelier-outillage-2026-07-20.md) · [phase 2](reports/phase2-filtre-atelier-outillage-2026-07-20.md) |

### Viviers — volume réel, ticket incompatible

Marchés dont la demande est mesurée et réelle, mais dont le prix pratiqué est nettement sous la tranche 150–400 €. **Ce ne sont pas des rejets** : ils sont mis de côté pour une éventuelle boutique mêlant low et high ticket, et l'anti-doublon ne doit pas les traiter comme des STOP.

Écartés par `sonde-prix` avant la phase 3, pour ne pas payer un audit SERP complet sur un ticket qu'une lecture de Google Shopping suffit à disqualifier.

| Cluster | Volume pertinent | Fourchette de prix constatée | Note | Date |
|---|---|---|---|---|
| Punch needle (pratique et kits) | 17 850 (plancher mesuré, [balayage famille 16](reports/chasse-clusters-loisirs-creatifs-artisanat-2026-07-20.md)) | 25–30 € (vérifié par Hakim le 20/07/2026) | Volume supérieur au tufting. CPC 0,10–0,37 € et présence Action/Gifi/Zeeman cohérents avec le ticket. Voisin direct du tufting : candidat naturel pour une boutique loisirs créatifs mêlant machines high-ticket et consommables low-ticket | 2026-07-20 |
| Outillage frigoriste | Non mesuré en cluster (repéré au [balayage famille 1](reports/chasse-clusters-atelier-outillage-2026-07-20.md)) | Non sondée | **Poche repérée, non instruite.** CPC 1,72 € — le plus élevé de toute la famille 1, signal d'intention pro à ticket élevé. Repérée par la phase 2 sans pouvoir être instruite (hors vocabulaire des clusters mesurés). À re-mesurer en phase 0 si reprise | 2026-07-20 |

### Cas limites remontés à Hakim

| Candidat | Cluster | Point à trancher | Date |
|---|---|---|---|
| — | — | — | — |

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

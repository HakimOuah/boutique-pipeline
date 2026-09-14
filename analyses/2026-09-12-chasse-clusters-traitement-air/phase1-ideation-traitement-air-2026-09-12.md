# PHASE 1 — IDÉATION — Traitement de l'air — 2026-09-12

Mode : **PRODUIT PUR** (imposé par le brief C0 et le parent phase 0). Jamais UNIVERS dans cette salve.

Tenant technique : `traitement-air` (slug de mission, pas un nom de produit).

Marché : France. Aucun volume recopié, aucun CPC, aucun scoring, aucun sourcing fournisseur, aucun verdict marché, aucun prix de vente fixé.

Lectures de prix publics : **14 septembre 2026, 07:05–07:09 CEST** (sonde séparée). Le brief et les noms de fichiers restent datés du **12 septembre 2026**.

---

## 1. Brief reçu

Mission C0 : à partir du **seul vocabulaire mesuré** de la famille **8 — Traitement de l'air**, nommer les idées PRODUIT PUR attestées et produire la sonde de prix indispensable au filtre.

- Date du brief : 2026-09-12.
- Entrée phase 0 : `reports/chasse-clusters-traitement-air-2026-09-12.md` (branche `agents/c0-scout-traitement-air-2026-09-12`, parent `t_da092d76`, commit `5f2e441e19eba683e4a2f71063a6fa52d0a9facc`). Contrôle manager `t_a9d27db0` : parent conforme. Copie versionnée : `analyses/2026-09-12-chasse-clusters-traitement-air/chasse-clusters-traitement-air-2026-09-12.md`.
- Gate parent : rapport daté du 2026-09-12, sept sections, DataForSEO France/French, témoins `tufting` cohérents. Vocabulaire produit **attesté** par le parent (ce ne sont pas des candidats) : `purificateur d'air` ; `vmc` / `ventilation mécanique contrôlée` ; `vmc double flux` ; `vmc simple flux` ; `vmc hygroréglable` ; `extracteur d'air`.
- Vocabulaire nouveau éligible (contrôle manager, hors doublon) : `vmc`, `vmc double flux`, `vmc simple flux`, `vmc hygroréglable`, `extracteur d'air`. Doublon exclu : `purificateur d'air`.
- Règle stricte : un produit n'est instruit que s'il est attesté par **au moins un mot-clé mesuré** du rapport phase 0 ; aucun produit imaginé hors de ce vocabulaire ; aucune tête isolée / graine stérile / accessoire sous le seuil n'est promue en idée ; **aucun volume de parent n'est attribué à une poche**.
- Référentiels lus dans le worktree : `PRODUCT-RESEARCH-PLAYBOOK.md`, `PRODUCT-RESEARCH-CRITERIA.md` (11 septembre 2026), `product-research/search/README.md`, `registre-candidats.md`. Registre **non modifié**.

Cette phase ne mesure pas la demande, ne score pas, ne source pas AliExpress et ne prononce ni `PASS_PREQUALIFICATION` ni `GO_FINAL` / `WATCH_FINAL` / `NO_GO_FINAL`.

---

## Observations, hypothèses et inconnues

**Observations**

- Le parent nomme six objets/niveaux de cluster, sans produit commercial ni prix.
- `purificateur d'air` recouvre l'entrée registre « Purificateur d'air » (rejet Hakim 02/08). Non collecté.
- `vmc` est un **sigle / catégorie** (même bucket que `ventilation mécanique contrôlée`). Ce n'est pas un objet unique vendable.
- `vmc double flux`, `vmc simple flux` et `vmc hygroréglable` sont des **niveaux spécifiques** à buckets distincts. Hygroréglable n'est pas le même bucket que simple flux.
- `extracteur d'air` est un **objet** distinct de la VMC. Le parent n'attribue pas le volume `ventilation` à cet objet.
- Sonde Google Shopping France du 14/09/2026 (détail : `reports/sonde-prix-traitement-air-2026-09-12.md`) : extracteur — cœur visible bas de gamme, mix AliExpress / aérateurs 100 mm / outliers pro ; VMC double flux — caissons/kits de marques (Atlantic, Aldes, S&P) et unités décentralisées ; VMC simple flux et hygroréglable — kits habitat T1–T7 chez les mêmes marques, y compris enseigne Brico Dépôt.

**Hypothèses** (non vérifiées ici)

- L'extracteur ponctuel salle de bains/WC est l'objet le plus « produit fini particulier » du vocabulaire ; la VMC est davantage un système à poser.
- Un angle Search pédagogique « choisir un extracteur ponctuel (diamètre, hygro, silence) plutôt qu'une VMC complète » est formulable ; sa défendabilité SERP n'est pas lue.
- Un angle Search « VMC double flux vs simple flux / hygroréglable, caisson et kit, sans devis installateur » est formulable ; occupation GSB + marques prescriptrices + pose **non arbitrées** (rôle aval).
- Les unités décentralisées pièce-par-pièce vues en Shopping (Blauberg Vento, Nano Air 50) **ne sont pas** un mot-clé de cluster retenu : ce n'est pas une idée distincte.

**Inconnues** (à transmettre, pas à combler)

- Adressabilité SERP, occupation réelle, CPC, Trends, économie unitaire, sourçabilité, pose vs produit : hors rôle.
- Têtes isolées / sous le seuil du parent (`vmi`, `bouche vmc`, `gaine vmc`, `ioniseur`, `aérateur`, `qualité de l air intérieur`, `filtration air`) : non instruites.
- Famille 10 (`humidificateur d air`, `déshumidificateur`) : hors brief.
- TrendTrack non ouvert : brief chemin B, pas une salve Shop.

---

## 2. Idées collectées

Niveau de preuve : **A** = tuiles Google Shopping France lues le **2026-09-14**. Tous les prix sont des **prix publics TTC observés**, pas un prix de vente à pratiquer. Aucune conversion. Aucun volume recopié.

Vue TrendTrack : **non applicable** — brief chemin B (clusters mesurés), pas de salve Shop.

| # | Produit | Terme mesuré qui atteste (phase 0) | Synonymes anti-doublon | Source exacte | Statut France | Problème ou désir | Prix publics observés (2026-09-14) | Première hypothèse d'angle | Famille de critères |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | Extracteur d'air (objet, extracteur ponctuel) | `extracteur d air` ; `extracteur d'air` (même bucket, §2.6) | extracteur d air, extracteur d'air, ventilateur extracteur d'air, aérateur (voisin sous le seuil, **non fusionné**), extracteur salle de bain (niveau du même objet, **non traité comme produit distinct**) | Rapport phase 0 §2.6. Prix : Google Shopping FR `extracteur d'air` et `extracteur d'air salle de bain` (`udm=28`, `hl=fr`, `gl=fr`) | FR observé | Extraire l'air vicié / humide d'une pièce (SDB, WC, cuisine) sans installer une VMC complète | **Observé.** Filtres Shopping tête `extracteur d'air` : moins de 45 € / 45–80 € / 80–150 € / plus de 150 €. Échantillon SDB : 12,69–220,50 € visibles ; cœur 100 mm ~17–45 € (Hydrozone 17,90–26,90 € ; AliExpress 21–36 €) ; Aldes Design D100 hygro 64,99 € (123elec) ; Aldes Deco D100 79,99 € ; Screwfix Aldes 125 mm 84,99 € ; S&P Silent 148,85 € (Elec 44) ; Silent-100 CHZ Design 220,50 € (GroupSumi). Outliers pro/chantier écartés de l'idée (Seton 1 778,40 €, GGM Gastro, tourelles hotte). | Search : « un extracteur ponctuel (diamètre, hygro, silence) pour une pièce humide, sans VMC de logement ». Pas de claim santé. Distinct du purificateur (doublon) et de la VMC. | problème précis ; explicable ; technique-particulier possible |
| 2 | VMC double flux | `vmc double flux` ; `vmc double-flux` ; `ventilation mécanique contrôlée double flux` (même bucket, §2.3) | vmc double flux, vmc double-flux, ventilation mécanique contrôlée double flux, VMC DF — **ne pas coller** à `vmc` (catégorie §2.2) ni au simple flux | Rapport phase 0 §2.3. Prix : Google Shopping FR `vmc double flux` | FR observé | Ventiler un logement en récupérant une partie de la chaleur de l'air extrait | **Observé.** Filtres Shopping : moins de 1 000 € / 1 000–3 000 € / 3 000–8 000 € / plus de 8 000 €. Échantillon : décentralisé Blauberg Vento Expert A50 499,00 € / A30 599,00 € (Ventildirect) ; InHome S11 399,00 € ; Atlantic Primocosy HR BP caisson 1 190,65 € (Comptoir des Pros) ; Primocosy HR 2 083,51 € (Plomberie-pro) ; S&P Domeo Evo 315DHU 2 490,00 € (Elec 44) ; S&P ORKA BP HR kit rénovation 1 399,00 € ; Autogyre Vital Air 90 1 199,00 € (123elec) ; Optimocosy HR Access 2 876,90 € (Bricozor). Tuiles « kit simple flux » contaminent la page (Autocosy 166,69 €) : **non retenues pour cet objet**. | Search : « choisir une VMC double flux (débit, rénovation vs neuf, caisson vs décentralisé) plutôt qu'un devis opaque ». Pose et marques **non arbitrées**. | explicable ; problème logement ; high ticket possible |
| 3 | VMC simple flux | `vmc simple flux` ; `ventilation mécanique contrôlée simple flux` (même bucket, §2.4) | vmc simple flux, ventilation mécanique contrôlée simple flux — **bucket distinct** de l'hygroréglable | Rapport phase 0 §2.4. Prix : Google Shopping FR `vmc simple flux` | FR observé | Extraire l'air d'un logement par un caisson / kit, sans récupération de chaleur | **Observé.** Filtres Shopping : moins de 200 € / plus de 500 €. Échantillon kits habitat : S&P Deco 2 N 89,00 € (Elec 44) ; Aldes EasyHOME Auto + 3 grilles 113,44–144,90 € ; Autocosy IH Flex 166,69–203,99 € ; EasyHOME Compact Auto ~206–216 € ; Hygrocosy / Hygrogenius (tuiles mixtes hygro) 256–533 € ; Brico Dépôt caisson TBC 369,00 €. Caissons débit 250–2500 m³/h Ventilationpro 155–335 € : mix habitat / pro, notés en sonde. | Search : « un kit VMC simple flux dimensionné T1–T7, sans confondre avec le double flux ». | explicable ; kit ; GSB/marques à lire en aval |
| 4 | VMC hygroréglable | `vmc hygroréglable` ; `vmc hygrométrique` ; `ventilation mécanique contrôlée hygroréglable` (même bucket, §2.5) | vmc hygroréglable, vmc hygrométrique, ventilation mécanique contrôlée hygroréglable, simple flux hygroréglable (formulation plus étroite **non sommée** par le parent) | Rapport phase 0 §2.5. Prix : Google Shopping FR `vmc hygroréglable` | FR observé | Adapter le débit d'extraction à l'humidité, plutôt qu'un débit fixe | **Observé.** Filtres Shopping : moins de 50 € / plus de 600 € (le palier bas correspond surtout à des **bouches**, pas au kit). Échantillon kits : Aldes EasyHOME Hygro Compact Classic 209,99 € (Screwfix) ; Hygro Compact 239,76 € (Tecnomat) ; EasyHOME Hygro Classic 269,00–289,73 € ; Hygrocosy BC 2 259,00–365,90 € ; Hygrogenius Flex 445,50–632,09 € ; Brico Dépôt caisson hygro 369,00 €. Accessoire : bouche hygroréglable Atlantic 35,80 € (Amazon.fr) — **pas l'objet**. | Search : « une VMC hygroréglable (bouches + groupe) plutôt qu'autoréglable, sans coller le volume du simple flux ». | explicable ; niveau matière/fonction du vocabulaire mesuré |

Les lignes 3 et 4 sont deux **buckets attestés distincts**, pas deux thèses inventées. La phase 2 peut les fusionner si la SERP montre le même achat. La ligne 2 n'est **pas** sommable avec 3/4. La ligne 1 n'est **pas** une VMC.

Formulations / familles à transmettre à `recherche-mots-cles` (mesure déjà faite en phase 0 ; **ne pas remesurer DataForSEO ici**) : `extracteur d'air` ; `vmc double flux` ; `vmc simple flux` ; `vmc hygroréglable`. Mode : PRODUIT PUR.

---

## 3. Écartés en cours de collecte

Aucun écart silencieux. Motifs en une ligne. Les mots-clés cités sont ceux du rapport phase 0 ; aucun volume n'est recopié.

| Vocabulaire / objet vu | Mot-clé mesuré (phase 0) | Motif d'écart |
|---|---|---|
| Purificateur d'air | `purificateur d air`, `purificateur d'air` | **Doublon registre** (rejet Hakim 02/08) — voir §4. Tête au-dessus du seuil : volume rendu par le parent, **pas une piste**. |
| Purificateur HEPA / ionique / ioniseur | `purificateur d air hepa`, `purificateur d air ionique`, `ioniseur d air`, `ioniseur` | Niveaux ou voisins du doublon, sous le seuil. Non instruit. |
| Épurateur d'air | `épurateur d air` / `épurateur d'air` | Synonyme registre du purificateur. Non collecté. |
| VMC (sigle / catégorie) | `vmc`, `ventilation mécanique contrôlée` | Catégorie parente, pas un produit exact. **Aucun de ses volumes n'est donné aux lignes 2–4.** Non collectée comme idée. |
| Ventilation (parent mixte) | `ventilation` | Sous le seuil ; intention mixte (éclairage). Non instruit. |
| VMC salle de bains | `vmc salle de bains` | Niveau de la catégorie, sous le seuil. Non instruit. |
| Bouche / gaine VMC | `bouche vmc`, `gaine vmc` | Accessoires, sous le seuil. Bouche hygroréglable vue à 35,80 € en Shopping : consommable, pas l'idée. |
| VMI | `vmi`, `ventilation vmi` | Objet distinct (insufflation), sous le seuil. Non instruit. |
| Aérateur | `aérateur` / `aerateur` | Contrôle hiérarchique, sous le seuil. Non fusionné avec l'extracteur. |
| Qualité de l'air intérieur / filtration / capteur / détecteur | `qualité de l air intérieur`, `filtration air`, `capteur qualité air intérieur`, `détecteur qualité air intérieur` | Graines officielles stériles ou têtes sous le seuil. Non instruit. |
| Humidificateur / déshumidificateur | `humidificateur d air`, `déshumidificateur` | **Famille 10**, hors brief. Présents au registre. Non balayés. |
| Extracteur grow / Prima Klima / Mars Hydro / Spider Farmer | n/a extracteur (parent) | Hors particulier / culture. Vu en Shopping ; **non promu**. |
| Extracteur / caisson cuisine pro, tourelle, GGM Gastro, Seton chantier | contaminations Shopping | Persona pro / restaurant / espaces confinés. Signal §3 critères ; non collecté comme idée. |
| Plafonnier / ventilation plafond / silencieuse / colonne | `ventilation plafond`, etc. | Contamination **éclairage**, exclue phase 0. Non instruit. |
| Marques seules (Dyson, Philips, Xiaomi, Atlantic, Aldès) | `purificateur d air dyson`, `atlantic vmc`, `aldès vmc` | Marques, exclues du cluster. Non instruites. |
| VMC décentralisée pièce-par-pièce (Blauberg Vento, Nano Air) | **absent** des clusters retenus | Offre Shopping visible, **pas** un mot-clé attesté. Non inventée. |
| Têtes isolées / n/a B2B | INRS, CEREMA, Jet AFS, Tarkov, ATEX, PC… | Hors particulier ou docs. Non instruit. |

---

## 4. Doublons registre évités

Croisés ce jour, **non re-proposés**. Aucune `reprise motivée` dans le brief.

| Entrée registre | Statut | Recouvrement avec le vocabulaire du jour |
|---|---|---|
| Purificateur d'air (syn. purificateur air HEPA, épurateur d'air) | Rejet Hakim 02/08 — déjà testé / retours négatifs | Tête `purificateur d'air`. **Ferme** HEPA / épurateur / ionique comme piste. |
| Humidificateur d'air | Survivant volume lots 2–3 (22/08) | Vu en contrôle de tête famille 8, **famille 10**. Non ouvert. |
| Déshumidificateur | Lot 1 22/08 + annexe UK | Idem, famille 10. Non ouvert. |
| Outillage frigoriste | Vivier famille 1 | Absent des suggestions du parent. Non assimilé. |
| Extracteur miel | STOP lots 2–3 (échantillon) | Homonyme « extracteur » seulement ; autre objet. Non confondu. |
| Moniteur CO2 (sonde PUR lot 1, 22/08) | historique salve, pas un STOP air | Voisin capteur qualité ; tête sous le seuil ici. Non proposé. |
| Osmoseur / surpresseur / pompes | candidats eau | Qualité de l'**eau**, pas de l'air. Non fusionné. |

Aucun STOP / rejet du registre ne recouvre `vmc`, `vmc double flux`, `vmc simple flux`, `vmc hygroréglable` ou `extracteur d'air`.

---

## 5. Poches adjacentes / vivier (motivés, sans volume parent)

Ce ne sont **pas** des idées collectées. Aucun volume de `vmc`, `extracteur d'air` ou `purificateur d'air` ne leur est transféré.

| Poche | Motivation | Devenir |
|---|---|---|
| VMI (insufflation) | Objet distinct, tête sous le seuil en phase 0 | Reste sous le seuil ; pas une idée. |
| Bouche VMC / gaine VMC | Accessoires du système VMC, sous le seuil | Vivier accessoire **si** une VMC passait plus loin ; pas un phare. |
| Ioniseur | Voisin du purificateur, sous le seuil + doublon de famille | Clos avec le purificateur. |
| Extracteur 100 mm / SDB low-ticket (~15–45 €) | Cœur Shopping très bas ; critère « gadget 15–20 € → vivier » | **Vivier ticket**, pas une promotion de l'idée n°1. L'idée n°1 reste l'objet attesté, avec fourchette mixte. |
| Unités double flux décentralisées (Vento, Nano Air) | Offre Shopping dans/proche 399–599 €, vocabulaire **non mesuré** comme cluster | Poche à ne pas inventer ; éventuellement graine **si** brief ultérieur. |
| Famille 10 humidité / clim | Têtes vues, hors famille 8 | Autre brief. |

---

## 6. Limites

- **Vocabulaire fermé.** Aucune idée hors des mots-clés écrits dans le rapport phase 0. La consigne playbook « 20 à 50 idées » n'est **pas** applicable.
- **TrendTrack non consulté.** Brief chemin B. Inaccessible-par-consigne, pas « vide ».
- **Aucun volume recopié**, y compris ceux du parent. La phase aval ne doit pas relire des chiffres ici.
- **Prix.** Plausibilité publique Shopping seulement, le 14/09/2026. Leroy Merlin catégorie extracteur : page ouverte sans texte extractible (chargement vide). Une session Shopping parallèle a reçu un captcha Google ; les lectures utiles ont été faites sur la session déjà acceptée. Aucun prix estimé pour combler.
- **Mix d'intentions en Shopping.** `extracteur d'air` mélange SDB particulier, grow, cuisine pro et chantier. `vmc double flux` mélange DF, décentralisé et kits simple flux. La sonde le documente ; elle ne nettoie pas la SERP.
- **GSB / marques / pose.** Signal fort (Leroy Merlin, Castorama, Brico Dépôt, Atlantic, Aldes, S&P). **Non arbitrée** — rôle du filtre, pas de cette phase.
- **Persona pro.** Caissons collectifs, hottes resto, frigoriste : signalés, pas instruits.
- Identifiants, comptes, panier, Shopify, Ads, Merchant Center, AliExpress sourcing : non utilisés. Dépense : 0. DataForSEO : non rappelé.
- Registre lu, non modifié.

---

## Gate de cette phase

- Rapport daté du **2026-09-12** (mission), lectures prix du **2026-09-14**, sections obligatoires remplies (brief ; idées ; terme attestant ; synonymes ; écartés ; doublons ; poches/vivier ; limites).
- Parent conforme, vocabulaire attesté.
- **Au moins une idée nouvelle** absente du registre et attestée par le vocabulaire mesuré : **extracteur d'air** ; **VMC double flux** ; **VMC simple flux** ; **VMC hygroréglable**.
- Sonde prix consultable, séparée.
- Aucun scoring, aucun volume, aucun sourcing, aucun verdict.

Chemin du livrable : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/reports/phase1-ideation-traitement-air-2026-09-12.md`

Copie versionnable (`reports/` est gitignoré) : `analyses/2026-09-12-chasse-clusters-traitement-air/phase1-ideation-traitement-air-2026-09-12.md`

Sonde : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/reports/sonde-prix-traitement-air-2026-09-12.md` (copie : `analyses/2026-09-12-chasse-clusters-traitement-air/sonde-prix-traitement-air-2026-09-12.md`)

Branche de dépôt : `agents/c0-ideation-traitement-air-2026-09-12`

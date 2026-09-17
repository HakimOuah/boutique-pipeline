# Production des visuels — Sous Abri (carports et tentes-garages, France), lot 1

**Document de mission autoportant.** Il complète, pour cette boutique, la spécification permanente
`docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md` (DA §3, contraintes §4, QA §5, livraison §6). La spec prévoit des **surcharges de DA** par l'ordre (§3 « sauf surcharge explicite ») : ce brief en fournit (fond, scènes, formats). Il **ne suspend aucune contrainte permanente** : il les complète par des contraintes propres à ces produits (§2 bis). Les règles écrites pour les cadrans se lisent ici sur l'objet réel : aucun lettrage sur la structure ou la bâche, abri posé au sol sur ses pieds, toit en haut, portes lisibles.

Date : 09/09/2026. Répertoire : `boutique-pipeline/boutique-carport/`. Persona validé : `personas/persona-carport-2026-09-09.md`. Contenus : `boutique-carport/content/`.

---

## 0. La mission en trois phrases

Sous Abri vend en France **des abris pour voiture en kit** : un carport acier, deux carports aluminium à prix fixe, sept tentes-garages, et trois carports aluminium sur mesure (devis). Tous les emplacements image de la boutique sont vides (hero, cartes de familles, galeries produit, blocs bénéfices, cartes collections, guides). Ton travail : produire ces images **sur le disque**, à partir des photos fournisseur nettoyées de `assets/source/<id AliExpress>/`, avec une mise en scène maison. Tu ne touches jamais à la boutique.

## 1. Les produits, tels qu'ils sont (vérité produit)

Une source par produit dans `assets/source/<id>/` (photos fournisseur, à considérer comme la seule vérité de forme, de couleur et de proportions). Ce qui doit rester **identique** d'une image à l'autre pour un même produit : forme du toit, nombre de poteaux, position des portes et fenêtres, couleur de la structure et de la toile, proportions.

| Handle | SKU | Source `assets/source/` | Ce que la photo fournisseur montre (lu le 09/09 sur la planche `01.*` de chaque dossier) |
|---|---|---|---|
| carport-acier-thermolaque-4-5x3 | SA-ACIER-450 | 1005012344715751 | Carport acier **noir**, 4 poteaux fins, toit à deux pans légèrement cintré en tôle noire nervurée, structure ajourée sur les côtés courts ; rendu 3D sur fond blanc avec une voiture de sport noire (la voiture n'est pas le produit) |
| carport-aluminium-autoportant | SA-ALU-AUTO-6x6 | 1005009961706626 | Carport alu **brun bronze** toit arqué, panneaux polycarbonate teinté, 4 poteaux, rendu 3D devant une villa avec voiture de sport grise ; le SKU dit « gris foncé », la photo dit bronze : couleur à confirmer, garder celle de la source |
| carport-camping-car-aluminium | SA-ALU-CC-6x38 | 1005011994406763 | Carport alu **brun foncé** toit arqué, polycarbonate teinté, 4 poteaux, deux berlines dessous, cerisiers en fleurs (rendu) ; 6 × 3,8 m |
| tente-garage-3x6-outsunny | SA-TG-3x6-OUT | 1005012736849383 | Tente **blanche** 3 × 6 m à deux pans, cadre acier gris, portes enroulables en pignon, fenêtres carrées translucides sur les longs côtés, berline grise dessous (rendu) |
| tente-garage-4x6-portes-enroulables | SA-TG-4x6-PE | 1005010670791375 | Tente **blanche** 4 × 6 m à deux pans, fenêtres « cathédrale » sur les côtés, aspect tente de réception (rendu fond blanc) ; à remettre en scène comme garage |
| tente-garage-4x6-fenetres | SA-TG-4x6-FEN | 1005012384075437 | Tente **grise** 4 × 6 m à deux pans, portes enroulables en pignon, fenêtres grillagées, SUV dessous (rendu jardin) |
| tente-garage-4x7-6-camping-car | SA-TG-4x76 | 1005012322112744 | Tente **grise** longue à deux pans, porte enroulable, voiture rouge dessous (rendu) ; 4 × 7,6 m |
| tente-carport-fermee-2-cotes | SA-TG-FERM2 | 1005012904297579 | Tente **blanche** à deux pans, fenêtres « cathédrale », doubles portes zip (rendu fond blanc, aspect réception) ; à remettre en scène comme garage |
| tente-garage-mobile-3x3 | SA-TG-3x3 | 1005012942086535 | Petite tente **gris foncé** 3 × 3 m à deux pans, une porte enroulable, quad dessous, montagnes enneigées (rendu) ; ne pas reprendre la neige |
| tente-garage-4x6-double-porte-volet | SA-TG-4x6-VOL | 1005013014844719 | Tente **blanche** 4 × 6 m, fenêtres, portes à volet, montrée en tente de réception avec table (rendu) ; à remettre en scène comme garage |
| devis-carport-aluminium-toit-plat | SA-DEVIS-PLAT | 1005012158685405 | Rendu fabricant Star Alu : carport alu **anthracite** à poteaux en Y et toit **incurvé** (« aile »), deux voitures ; la page devis parle de toit plat : utiliser ce rendu pour la structure et la matière, pas pour la forme du toit `[À VÉRIFIER avec le devis]` |
| devis-carport-aluminium-adosse | SA-DEVIS-ADOS | 1005012143140387 | Rendu fabricant ONE ALU : carport alu gris clair cintré à 2 pieds ; **ne correspond pas** à un adossé : n'utiliser que la matière (alu gris, polycarbonate) et composer l'adossé depuis un mur `[À VÉRIFIER avec le devis]` |
| devis-carport-cintre-2-pieds | SA-DEVIS-2P | 1005012231765595 | Rendu fabricant ONE ALU : carport alu **anthracite** cintré à 2 pieds, toit polycarbonate teinté, porte-à-faux côté voiture ; sur parking avec marquage jaune |

Les sources fabricant portent des logos, numéros de téléphone et bandeaux (« ONE ALU », « STAR ALU », « FACTORY PRICE ») : ils disparaissent dans la composition, jamais reproduits.

Interdits produit : pas de poteau ajouté ou retiré, pas de changement de forme de toit, pas de couleur autre que celle de la source (sauf slot `variante` explicitement demandé), pas de parois ou de portes inventées, pas d'accessoire non fourni (éclairage LED, borne de recharge, gouttière si absente de la source), pas de neige épaisse « qui tient » sur une bâche.

## 2. Direction artistique (surcharge de la spec §3) — PROPOSÉE, à valider par Hakim

- **Parti pris** : « la vraie vie, pas le catalogue ». Le marché montre des carports anthracite sous un ciel bleu avec un SUV gris devant une maison neuve (Akena, Verandair, Brico Dépôt en rendu 3D). Sous Abri montre **le carport le jour où il sert** : averse, grêle, givre du matin, pollen, soleil de plomb — la voiture au sec ou à l'ombre dessous, dans un jardin français ordinaire.
- **Aucun fond studio** (décision Hakim 10/09/2026, remplace la règle « fond sable ») : tous les slots, y compris `face` et `carte`, sont des **photos de terrain** ; un produit détouré sur un aplat uni « fait IA » et est refusé. Le slot `face` devient une vue de trois quarts du produit monté, seul (sans voiture), sur un vrai sol (gravier, enrobé, dalle, pelouse), avec un vrai arrière-plan (mur crépi, haie, portail), et un cadrage qui laisse lire toute la structure.
- **Réalisme photo obligatoire** : lumière naturelle avec une direction crédible et des ombres au sol cohérentes, ciel réel (voile, traîne), légères imperfections (gravier irrégulier, feuilles, flaque, trace de pneu, herbe inégale), matières avec micro-défauts (poussière sur la tôle, plis de bâche, reflets), rendu appareil photo (focale 35–50 mm, profondeur de champ modérée, léger grain, pas de netteté uniforme), aucun objet parfaitement symétrique ni sol parfaitement plat. Interdits : aplat uni, ombre unique « studio », rendu 3D lisse, saturation publicitaire, surfaces sans texture.
- **Scènes de montage différentes par produit** : sol, maison, saison, vêtements et posture des deux adultes changent d'un produit à l'autre ; deux images de montage ne doivent jamais se ressembler.
- **Scènes** (slots `hero`, `situation`, `benefice`) : pavillon français des années 1970–2000 (crépi, tuiles, portail, haie), allée en gravier ou en enrobé, cour bétonnée, mur de garage, ciel de traîne, lumière d'aube ou de fin d'après-midi. Un peu de météo à chaque scène : sol mouillé, gouttes sur le polycarbonate, grêlons au sol, givre sur la pelouse, pollen jaune sur une voiture voisine non abritée. **Rien d'exagéré** : pas de tempête, pas de tornade, pas de neige de carte postale, pas de villa de luxe, pas de piscine à débordement.
- **Voitures** (décision Hakim 10/09/2026, remplace « jamais de logo constructeur ») : de vrais modèles courants en France, **emblèmes et marquages conservés, plaque d'immatriculation absente** (pas de support de plaque vide non plus). Parc imposé, un modèle attitré par produit et le même sur toutes les vues de ce produit : Peugeot 308 blanche (carport acier 4,5 × 3 et carport alu autoportant), Citroën C3 sable/noire (Outsunny 3 × 6, tente mobile 3 × 3), Renault Scenic E-Tech blanche (4 × 6 portes enroulables), Audi A4 Avant bleu nuit (4 × 6 fenêtres maille), Peugeot 3008 gris foncé (tente-carport fermée 2 côtés), Tesla Model Y blanche (4 × 6 passage traversant), BYD Seal U blanche (hero). Camping-car profilé blanc sans marque pour les deux produits camping-car. **Le slot `face` montre désormais le véhicule sous l'abri** (décision 10/09 midi), comme photo principale.
- **Logique de scène obligatoire** (décision Hakim 10/09/2026) : un abri de voiture est posé là où une voiture peut arriver. Sol porteur continu (gravier, enrobé, dalle, pavés) qui **se prolonge jusqu'à la rue ou au portail** ; abri placé devant un garage, en bout d'allée, le long d'un pignon ou sur une place de stationnement existante ; jamais une dalle isolée au milieu d'une pelouse, jamais une tente sans chemin d'accès, jamais un abri collé à un potager. Traces d'usage : marques de pneus, gravier tassé sur deux bandes, flaque dans un creux, tuyau d'arrosage, poubelle, vélo d'enfant, boîte aux lettres.
- **Anti « slop IA »** : on préfère une photo un peu banale avec des défauts à une image parfaite. Refuser : lumière dorée systématique, ciel trop dramatique, végétation trop fournie et trop verte, sol parfaitement propre, symétrie parfaite, bâche sans un pli, toutes les surfaces nettes, couleurs saturées, maison « de catalogue », composition centrée à chaque fois. Accepter et même chercher : un ciel gris uni, une haie mal taillée, un mur taché, une gouttière qui dépasse, un cadrage légèrement décalé, un premier plan encombré, un léger flou de bougé sur un arrière-plan.
- **Personnes** : autorisées sur les slots `montage` et `livraison` uniquement : deux adultes ordinaires (35–60 ans), vêtements de bricolage, mains et proportions contrôlées, jamais de visage en gros plan, jamais de tenue « pro » ni de logo. Pas d'enfant, pas d'animal.
- **Aucun texte, aucun logo, aucun badge, note, étoile, prix ou cote** dans l'image. Les schémas cotés se font en HTML/SVG, pas dans l'image.
- **Aucune promesse visuelle non tenue** : pas de neige épaisse portée par une bâche, pas de grêle qui rebondit sur une toile, pas de foudre, pas de voiture de collection sous une tente (le persona en restauration existe, mais on ne suggère pas la protection contre le vol).
- Rendu : photo réaliste éditoriale, focale 35–50 mm, ni illustration ni 3D lisse ; grain léger accepté.
- Accent de marque `#C8552B` (terre cuite) et bleu ardoise `#2F4A5A` : réservés au HTML/CSS ; dans l'image, seulement par un objet naturel (pot en terre cuite, volet bleu) et jamais imposé.

## 2 bis. Bloc d'orientation propre à ces produits (à inclure dans chaque prompt)

```
MANDATORY ORIENTATION — the shelter stands on the ground on its posts or frame, roof at the TOP,
doors and windows where the reference shows them, car parked underneath along the long axis with
its wheels on the ground. Never floating, never tilted, never mirrored. Keep the reference
three-quarter framing unless the slot says otherwise; if in doubt, keep the reference framing and
move the camera. Same number of posts, same roof shape, same colours as the reference.
```

## 3. Le manifeste (ce que tu livres)

Formats : `face`/`carte`/`galerie` = 2048 × 2048 ; `hero` = 2048 × 1152 ; `benefice`/`situation` = 2048 × 1536 ; `guide` = 2048 × 1152. JPEG qualité ~90. Un fichier par slot, nommé `<handle>-<slot>.jpg`.

### Lot 1 — accueil et familles (7 images)
| Slot | Fichier | Contenu attendu |
|---|---|---|
| hero | sousabri-hero.jpg | Carport alu autoportant (source 1005009961706626) devant un pavillon, averse en cours, voiture compacte grise au sec dessous, sol mouillé qui reflète, lumière grise de fin d'après-midi. Rôle : désir + promesse « sans mauvaise surprise ». |
| famille-alu | sousabri-famille-alu.jpg | Le carport acier noir (source 1005012344715751) en trois-quarts, fond studio sable, ombre diffuse. Rôle : carte de famille « carports à prix fixe ». |
| famille-tentes | sousabri-famille-tentes.jpg | Tente Outsunny 3 × 6 blanche (source 1005012736849383), fond studio sable. Rôle : carte « tentes-garages ». |
| famille-devis | sousabri-famille-devis.jpg | Carport cintré 2 pieds (source 1005012231765595) sur cour en enrobé, sans voiture, lumière rasante. Rôle : carte « sur mesure ». |
| douleur-grele | sousabri-douleur-grele.jpg | Voiture blanche NON abritée sur une allée après une averse de grêle, grêlons au sol, capot marqué de gouttes, aucun carport dans l'image. Rôle : douleur (accueil §2). |
| douleur-soleil | sousabri-douleur-soleil.jpg | Voiture bleu nuit en plein soleil d'été sur une cour bétonnée, reflets durs, pollen jaune sur le pare-brise ; aucun carport. Rôle : douleur UV. |
| comparaison | sousabri-comparaison.jpg | Trois abris côte à côte à la même échelle sur fond sable : tente 3 × 6, carport acier, carport alu autoportant. Rôle : comparaison honnête. |

### Lot 2 — galeries produit (10 produits à prix fixe × 5 slots = 50 images)
Pour chaque handle du tableau §1 (sauf les trois `devis-*`) : `face` (produit seul, fond sable), `situation` (produit dans un jardin français avec la voiture ou le camping-car qu'il abrite, météo légère), `detail-structure` (macro d'un poteau, d'une jonction, d'une porte enroulable ou d'un panneau de toit, fidèle à la source), `montage` (deux adultes en train d'assembler la structure au sol, pièces alignées, notice posée, sans texte lisible), `ancrage` (gros plan d'un pied fixé au sol : platine sur dalle, piquet en spirale ou hauban tendu selon le produit — ne montrer que ce que la source ou la fiche `[À VÉRIFIER]` permet ; à défaut, pied sur dalle sans quincaillerie inventée).

### Lot 3 — pages devis et guides (9 images)
Pour chaque `devis-*` : `face` (rendu fabricant nettoyé et remis en scène sur fond sable) et `situation` (devant un pavillon, voiture dessous). Guides : `guide-declaration` (bureau, plan de masse dessiné à la main, mètre ruban, sans texte lisible), `guide-montage` (kit déballé sur une pelouse, pièces triées, deux paires de mains), `guide-comparatif` (tente et carport rigide côte à côte sous une pluie fine).

## 4. QA propre à ce lot (en plus de la spec §5)
- Compter les poteaux et comparer à la source. Vérifier la forme du toit et la position des portes.
- Une voiture entière tient sous l'abri sans toucher les poteaux ; proportions humaines cohérentes avec 2,5 m de hauteur.
- Aucune lettre, aucun chiffre, aucune plaque lisible, aucun logo (structure, bâche, voiture, vêtements).
- Météo présente mais crédible ; pas de neige portée par une bâche.
- Rejets dans `rejected/` avec motif.

## 5. Livraison
Dossier : `boutique-carport/livraisons/visuels-lot<N>-2026-09-09/` ; manifeste `manifeste.json` indexé `handle` + `sku` + `slot`. Les fichiers validés seront recopiés dans `assets/final/` par l'orchestrateur.

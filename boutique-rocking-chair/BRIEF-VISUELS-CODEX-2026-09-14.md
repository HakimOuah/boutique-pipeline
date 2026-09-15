# Production des visuels — Bercelou (rocking chairs et fauteuils à bascule, France), lot 1 TEST

**Document de mission autoportant.** Il complète, pour cette boutique, la spécification permanente `docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md` (contraintes §4, QA §5, livraison §6). Il **surcharge la DA §3** (pierre et craie, conçue pour les montres) avec la direction « Veille douce » validée par Hakim le 14/09/2026. Il ne suspend aucune contrainte permanente et ajoute des contraintes propres à ces meubles (§2 bis).

Date : 14/09/2026. Répertoire : `boutique-pipeline/boutique-rocking-chair/`. Persona validé : `personas/persona-rocking-chair-2026-09-14.md`. Décisions : `DECISIONS-2026-09-14.md`.

---

## 0. La mission en trois phrases
Bercelou vend en France **des fauteuils à bascule** pour les tétées de nuit, le coin lecture et la détente. Ce lot est un **test de style** sur 3 fauteuils (15 images) et le hero de l'accueil (1 image) : Hakim valide la direction avant la production des 44 fiches. Tu produis les images **sur le disque**, à partir des photos fournisseur de `assets/source/<id AliExpress>/` ; seule la mise en scène change, **jamais le fauteuil**.

## 1. Les produits, tels qu'ils sont (vérité produit)
Seule vérité de forme, de couleur, de matière et de proportions : les photos de `assets/source/<id>/` (01 à 08 et `dim-01.jpg`). Elles portent des textes, pictogrammes et cadres décoratifs (voir interdits) : ceux-ci ne sont **jamais** reproduits.

| Handle | SKU | Source | Ce que montrent les photos (contrôle à l'œil du 14/09) |
|---|---|---|---|
| fauteuil-a-bascule-allaitement-teddy | BCL-TEDDY-ROSA | `assets/source/1005010201578018/` | **Fauteuil à oreilles en bouclette teddy écru** : dossier haut ailé, capitonné en carrés (4 colonnes × 4 rangées de coussins), accoudoirs arrondis pleins en bouclette, assise épaisse arrondie. Piètement en **tubes métal noir mat** (2 montants de chaque côté, reliés par une barre transversale) fixé sur **deux patins en bois clair** (hêtre ou hévéa naturel) courbés. Cotes : 92 cm de haut, assise à 40 cm, accoudoirs à 62 cm. Couleur de ce lot : **écru**. |
| fauteuil-a-bascule-scandinave-velours-cotele | BCL-COTELE-ANAJ | `assets/source/1005012640407961/` | **Fauteuil à bascule inclinable en velours côtelé crème** : dossier en boudins horizontaux côtelés avec **coussin d'appui-tête** séparé, assise côtelée épaisse. **Flancs pleins en similicuir cognac** dont le bas forme les patins courbes. **Accoudoirs plats en bois foncé** posés sur les flancs. **Repose-pieds indépendant** : coussin côtelé crème sur cadre en tube métal noir. Dossier réglable (3 positions). Couleur : crème et cognac. |
| fauteuil-allaitement-chambre-bebe-avec-repose-pieds | BCL-BOUCLE-FANG | `assets/source/1005012822557916/` | **Fauteuil à oreilles en bouclette écru**, dossier haut droit à joues latérales, accoudoirs épais, petit coussin lombaire, **poche latérale** en tissu sur le côté. **Base à bascule en bois acajou foncé** : deux patins courbes reliés par des traverses. **Repose-pieds escamotable** qui sort sous l'assise (tirette métal noir, coussin bouclette). La poche porte une petite étiquette de marque sur les photos : **elle disparaît**. 99 cm de haut. |

**Interdits produit** :
- ne pas changer le nombre de carrés du capitonnage ni la forme du dossier ;
- ne pas remplacer les patins bois par du métal (et inversement) ;
- ne pas changer la couleur des patins, du piètement ou du similicuir ;
- ne pas ajouter de pivot, de moteur, de télécommande ni de prise ;
- ne pas ajouter d'accoudoirs rembourrés sur le côtelé, dont les accoudoirs sont en bois ;
- ne pas inventer de coutures décoratives ;
- repose-pieds : seulement pour le côtelé (indépendant) et le Fangange (escamotable, visible sorti ou rangé selon le slot), **jamais** sur le teddy Rosahqnda.

## 2. Direction artistique « Veille douce » (surcharge de la spec §3), validée par Hakim le 14/09/2026
- **Parti pris** : les concurrents (Sunlay, Oscille, Alramo) montrent des salons blancs en plein jour. Bercelou montre **le fauteuil au moment où il sert** : la tétée de nuit à la lumière d'une lampe, la lecture du soir, le calme d'une chambre de bébé.
- **Lumière** :
  - slots `nuit` et `hero` : **lampe de chevet, veilleuse ou lampadaire allumé** comme source principale, lumière chaude de 2 700 K, ombres douces, pièce sombre autour, halo sur le tissu ;
  - slots `face` et `salon` : lumière douce de fin d'après-midi ou de début de soirée, une lampe allumée dans le champ ;
  - jamais de plafonnier, jamais de lumière blanche plate de studio.
- **Palette dans l'image** : sable, lin, bois clair, bleu nuit profond dans les ombres, touches d'ambre (abat-jour, veilleuse). La terre brûlée `#AE5420` et le bleu nuit `#1E2A3A` apparaissent au plus par un objet naturel (plaid, coussin, pot, rideau), jamais imposés.
- **Décors** : appartement ou maison française ordinaire.
  - Chambre de bébé : lit à barreaux en bois, mobile simple, tapis, commode, rideaux en lin.
  - Salon : parquet, bibliothèque, plante, plaid tricoté, tasse, livre.
  - Pas de lustre en cristal, pas de cheminée de château, pas de moulures de palace, pas de fenêtres géantes sur un parc.
- **Réalisme photo obligatoire** (Hakim refuse les images « trop IA ») :
  - focale 35–50 mm, profondeur de champ modérée, léger grain ;
  - matières avec micro-défauts (bouclette qui peluche, pli du plaid, poussière de lumière) ;
  - premier plan légèrement encombré (jouet, livre ouvert, gigoteuse posée), cadrage parfois décalé.
  - Refuser : symétrie parfaite, pièce « catalogue », saturation publicitaire, lumière dorée partout, rendu 3D lisse.
- **Personnes** : autorisées sur les slots `nuit`, `salon` et `hero`.
  - Une femme ou un homme adulte (28–40 ans), tenue d'intérieur simple (gilet, t-shirt, pantalon de pyjama), vu de trois quarts dos, de profil ou en contre-jour ; **jamais de visage en gros plan**, jamais de regard caméra.
  - Bébé : **nouveau-né emmailloté dans une gigoteuse ou une couverture**, tête contre l'épaule ou dans les bras, visage à peine visible et tourné vers l'adulte, proportions réalistes.
  - Allaitement suggéré **pudiquement** (bébé contre la poitrine, couverture, aucune nudité).
  - Mains : 5 doigts, proportions contrôlées.
- **Aucun texte, aucun logo, aucun badge, pictogramme, note, étoile, prix ou cote** dans l'image. Aucun cadre mural à personnage sous licence (les sources montrent des tableaux de personnage de dessin animé : **interdit**), aucun livre ou affiche lisible.
- **Formats** : `face`, `salon`, `nuit`, `matiere` = 2048 × 2048 ; `detail` = 2048 × 2048 ; `hero` = 2048 × 1152. JPEG qualité ~90. Nom : `<handle>-<slot>.jpg`.

## 2 bis. Bloc d'orientation propre à ces produits (dans chaque prompt)
```
MANDATORY ORIENTATION: the rocking chair stands upright on the floor on its rockers, both rockers touching the floor,
seat horizontal, backrest at the back and upright (or in the reference recline position),
armrests on both sides. Never floating, never tilted sideways, never mirrored left-right in a way that changes the design,
never cut by the frame at the rockers. Same backrest shape, same tufting pattern and count, same rocker material and colour,
same frame colour, same fabric texture and colour as the reference photos. No logo, no label, no text anywhere.
```

## 3. Le manifeste (lot 1 TEST : 16 images)

| Handle | SKU | Slot | Fichier | Contenu attendu (rôle de vente) |
|---|---|---|---|---|
| fauteuil-a-bascule-allaitement-teddy | BCL-TEDDY-ROSA | face | fauteuil-a-bascule-allaitement-teddy-face.jpg | Le fauteuil **seul**, trois quarts avant, coin d'une chambre de bébé en début de soirée, lampe de chevet allumée sur une commode, tapis rond, rideaux lin tirés. Toute la structure est lisible, patins compris. Photo principale : désir et fidélité. |
| fauteuil-a-bascule-allaitement-teddy | BCL-TEDDY-ROSA | nuit | fauteuil-a-bascule-allaitement-teddy-nuit.jpg | La nuit, une mère de profil assise dans le fauteuil, nouveau-né emmailloté contre elle, **seule lumière : une veilleuse ambre** posée à côté, lit à barreaux flou en arrière-plan. Calme, pudique. Rôle : tétées de nuit. |
| fauteuil-a-bascule-allaitement-teddy | BCL-TEDDY-ROSA | salon | fauteuil-a-bascule-allaitement-teddy-salon.jpg | Le même fauteuil au salon, un soir, un adulte de trois quarts dos lit un livre, plaid terre brûlée sur l'accoudoir, lampadaire allumé, bibliothèque. Rôle : « il reste au salon après bébé ». |
| fauteuil-a-bascule-allaitement-teddy | BCL-TEDDY-ROSA | matiere | fauteuil-a-bascule-allaitement-teddy-matiere.jpg | Macro de la bouclette et d'un carré du capitonnage, une main posée à plat sur l'accoudoir, lumière rasante chaude. Rôle : douceur. |
| fauteuil-a-bascule-allaitement-teddy | BCL-TEDDY-ROSA | detail | fauteuil-a-bascule-allaitement-teddy-detail.jpg | Plan bas sur un patin en bois clair et le piètement métal noir, sur un parquet avec un tapis, bascule légèrement inclinée vers l'avant. Rôle : bascule et structure. |
| fauteuil-a-bascule-scandinave-velours-cotele | BCL-COTELE-ANAJ | face | fauteuil-a-bascule-scandinave-velours-cotele-face.jpg | Le fauteuil **seul avec son repose-pieds**, trois quarts avant, salon scandinave en début de soirée, lampe à poser allumée, tapis beige tissé, mur lin. Structure, flancs cognac et accoudoirs bois bien lisibles. |
| fauteuil-a-bascule-scandinave-velours-cotele | BCL-COTELE-ANAJ | nuit | fauteuil-a-bascule-scandinave-velours-cotele-nuit.jpg | Chambre de bébé la nuit, dossier en position semi-inclinée, un parent de profil berce le nourrisson emmailloté, pieds sur le repose-pieds, lumière d'une veilleuse. Rôle : tétées de nuit en position inclinée. |
| fauteuil-a-bascule-scandinave-velours-cotele | BCL-COTELE-ANAJ | salon | fauteuil-a-bascule-scandinave-velours-cotele-salon.jpg | Un adulte détendu, jambes sur le repose-pieds, tasse à la main, vu de trois quarts dos, salon le soir, lampe allumée. **Aucun tableau à personnage.** Rôle : détente. |
| fauteuil-a-bascule-scandinave-velours-cotele | BCL-COTELE-ANAJ | matiere | fauteuil-a-bascule-scandinave-velours-cotele-matiere.jpg | Macro des côtes du velours et de l'appui-tête, jonction avec l'accoudoir en bois, lumière rasante chaude. |
| fauteuil-a-bascule-scandinave-velours-cotele | BCL-COTELE-ANAJ | detail | fauteuil-a-bascule-scandinave-velours-cotele-detail.jpg | Plan de profil sur le flanc cognac en forme de patin et l'accoudoir en bois, sur tapis. Rôle : la bascule intégrée au flanc. |
| fauteuil-allaitement-chambre-bebe-avec-repose-pieds | BCL-BOUCLE-FANG | face | fauteuil-allaitement-chambre-bebe-avec-repose-pieds-face.jpg | Le fauteuil **seul**, trois quarts avant, **repose-pieds rangé**, coin de chambre de bébé, lit à barreaux en bois clair à côté, lampe allumée. Base acajou bien lisible, **poche sans étiquette**. |
| fauteuil-allaitement-chambre-bebe-avec-repose-pieds | BCL-BOUCLE-FANG | nuit | fauteuil-allaitement-chambre-bebe-avec-repose-pieds-nuit.jpg | La nuit, repose-pieds sorti, une mère de trois quarts dos berce le bébé emmailloté, veilleuse ambre, babyphone posé sur un guéridon (sans logo). |
| fauteuil-allaitement-chambre-bebe-avec-repose-pieds | BCL-BOUCLE-FANG | salon | fauteuil-allaitement-chambre-bebe-avec-repose-pieds-salon.jpg | Le fauteuil dans un coin lecture de salon, repose-pieds sorti, plaid et livre, lampadaire, soir. |
| fauteuil-allaitement-chambre-bebe-avec-repose-pieds | BCL-BOUCLE-FANG | matiere | fauteuil-allaitement-chambre-bebe-avec-repose-pieds-matiere.jpg | Macro de la bouclette, de l'accoudoir et de la poche latérale (sans étiquette), une tétine ou un livre de bain dépasse de la poche. |
| fauteuil-allaitement-chambre-bebe-avec-repose-pieds | BCL-BOUCLE-FANG | detail | fauteuil-allaitement-chambre-bebe-avec-repose-pieds-detail.jpg | Plan bas sur la base à bascule acajou et le repose-pieds sorti, parquet. |
| bercelou-accueil | BCL-HERO | hero | bercelou-hero.jpg | **Hero d'accueil 16:9.** Chambre de bébé la nuit, le fauteuil teddy écru Rosahqnda (source 1005010201578018) en trois quarts, une mère de dos ou de profil qui berce son nourrisson emmailloté, halo chaud d'une lampe de chevet, le reste de la pièce dans un bleu nuit profond. **Espace négatif calme à gauche** pour le titre (le texte sera posé en HTML). |

## 4. QA propre à ce lot (en plus de la spec §5)
- **Planche par fauteuil** (5 vignettes, ≥ 740 px chacune) comparée à `01.jpg` : forme du dossier, nombre de carrés du capitonnage, matière et couleur des patins, piètement, similicuir cognac, accoudoirs en bois, repose-pieds.
- **Zoom** : absence de toute étiquette sur la poche du Fangange ; absence de tout texte (livres, affiches, babyphone).
- **Personnes** : mains à 5 doigts, bébé aux proportions réalistes et emmailloté, aucune nudité, aucun visage en gros plan.
- **Lumière** : sur `nuit` et `hero`, une source chaude visible dans le champ et une pièce réellement sombre autour.
- Aucun tableau à personnage sous licence.
- Rejets dans `rejected/` avec leur motif.

## 5. Livraison
Dossier : `boutique-rocking-chair/livraisons/visuels-lot1-test-2026-09-14/`, avec le manifeste `manifeste-realise.json` indexé `handle` + `sku` + `slot`. L'orchestrateur relit chaque image avant de la présenter à Hakim et de la brancher sur Shopify.

# Production des visuels — Bercelou, lots 2 à 5 (production complète)

**Document de mission autoportant**, complément du brief du lot test `boutique-rocking-chair/BRIEF-VISUELS-CODEX-2026-09-14.md`. **Lis celui-ci d'abord en entier** : §2 direction « Veille douce », §2 bis bloc d'orientation, §4 QA, §5 livraison. Tout y reste valable.

Date : 15/09/2026. Spécification permanente : `docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md` (contraintes §4, QA §5, livraison §6).

## 0. Ce qui est décidé
- **Style validé par Hakim le 15/09/2026** sur le lot test : `boutique-rocking-chair/livraisons/visuels-lot1-test-2026-09-14/`.
- **Références de rendu à regarder avant de commencer** : `fauteuil-a-bascule-allaitement-teddy-face.jpg` · `fauteuil-a-bascule-allaitement-teddy-nuit.jpg` · `fauteuil-a-bascule-allaitement-teddy-salon.jpg` · `fauteuil-allaitement-chambre-bebe-avec-repose-pieds-detail.jpg` · `fauteuil-a-bascule-scandinave-velours-cotele-matiere.jpg`. Même lumière de lampe, mêmes intérieurs français ordinaires, même réalisme, même pudeur.
- **Catalogue** : 41 fiches. Les 3 fiches du lot test sont faites. Les deux fauteuils releveurs sont retirés par Hakim et ne se génèrent pas. Restent **38 fiches** et les visuels de pages.
- **Livraison par lot** : un ordre par lot, dans `ordres/pour-codex/inbox/`, avec une enveloppe de résultat par ordre.

## 1. Vérité produit, fiche par fiche (obligatoire avant de générer)
Pour chaque fiche, **avant toute génération** :
1. Ouvre toutes les photos de `boutique-rocking-chair/assets/source/<pid>/` (01 à 08, et `dim-01.jpg` s'il existe).
2. Écris `livraisons/<dossier du lot>/qa/verite-<handle>.md`, 5 lignes au plus :
   - silhouette (dossier, accoudoirs, assise) ;
   - matière et couleur du revêtement **dans la couleur de 01.jpg** ;
   - base (patins bois ou métal, couleur, nombre de traverses, pied pivotant, trépied…) ;
   - éléments présents (repose-pieds, appui-tête, coussin, poche, pouf) ;
   - textes, logos et décors sous licence à ne pas reproduire.
3. Compare avec le **H1 de la fiche** (tableau du §3), écrit après contrôle des photos. Le H1 dit ce qui est vendu.
   - **Si les photos contredisent le H1** (autre matière, mécanisme absent, produit différent), ne génère pas cette fiche : rejette-la avec motif dans l'enveloppe.
4. **Couleur** : celle de `01.jpg`, et la même sur toutes les images d'une fiche.

**Pièges déjà connus** :
- Plusieurs sources portent des textes incrustés (« PRODUKTSPEZIFIKATIONEN », cotes, pictogrammes, « Design élégant »), des logos sur étiquette ou poche, et des **tableaux de personnages de dessin animé**. Rien de tout cela ne se reproduit.
- `rocking-chair-avec-repose-pieds` : **pas pivotant**. C'est un fauteuil en bois cintré à patins de type « Poäng » (le titre fournisseur ment).
- `coussin-d-assise-rocking-chair` : **seul le coussin est vendu**. Le slot `face` montre le coussin seul, sans panier suspendu.
- `rocking-chair-bebe` et `chaise-a-bascule-enfant` : combinés 2 en 1 (transat à bascule et chaise haute). Aucun bébé dans l'image (§2).
- `housse-de-protection-rocking-chair` : housse générique de mobilier d'extérieur. Montre-la **posée sur un fauteuil de jardin**, sans promesse de forme parfaite.
- **Relax** : pas de moteur, câble, télécommande ou tête de massage visibles s'ils ne figurent pas sur les sources ; pas de vocabulaire visuel médical (déambulateur, pilulier, lit médicalisé).
- `rocking-chair-acacia` : pas d'essence de bois particulière. Reprends exactement la teinte des sources.

## 2. Scènes par famille (direction « Veille douce »)
**Règles communes** :
- Intérieurs et extérieurs **français ordinaires** : appartement ancien, maison de ville, pavillon. Parquet ou carrelage, rideaux en lin, plantes, livres sans titre lisible.
- Lumière de lampe ou de fin de journée, avec une source chaude visible sur les scènes du soir.
- **Personnes** : adultes de 28 à 60 ans, en tenue d'intérieur simple, vus de profil, de dos ou de trois quarts dos. Jamais de visage en gros plan ni de regard caméra. Mains à 5 doigts.
- **Bébé** : seulement sur les slots `nuit` de la famille allaitement. Nouveau-né emmailloté, visage tourné vers l'adulte, allaitement pudique.
- **Aucun texte, logo, étiquette, badge, cote ni tableau à personnage.**

| Famille | Slots | Contenu attendu par slot |
|---|---|---|
| **A. Allaitement et bascule** (lot 2) | `face` · `nuit` · `salon` · `matiere` · `detail` | **face** : fauteuil seul, trois quarts avant, coin de chambre de bébé ou de salon en début de soirée, lampe allumée, toute la base lisible (photo principale). **nuit** : parent de profil qui berce ou nourrit un nouveau-né emmailloté, seule lumière une veilleuse ambre, lit à barreaux flou. **salon** : adulte de trois quarts dos qui lit le soir, plaid (terre brûlée ou lin), lampadaire. **matiere** : macro du revêtement et d'un accoudoir, main posée, lumière rasante. **detail** : plan bas sur la base (patins, piètement, repose-pieds s'il existe). |
| **B. Design, cocon, bois et rotin, extérieur** (lot 3) | `face` · `soir` · `usage` · `matiere` · `detail` | **Intérieur** (bouclette, bois, papasan, bambou) : face au salon ou au coin lecture en soirée ; soir = fauteuil seul près d'une fenêtre, lumière de lampe et nuit bleue dehors ; usage = adulte qui lit ou prend un thé, de dos ou de profil. **Extérieur et rotin** (cocon extérieur, cocon suspendu, fauteuil et chaise de jardin, rotin) : face sur une terrasse ou un balcon français en fin de journée, lanterne ou guirlande allumée ; soir = même lieu à la nuit tombante, bougie ; usage = adulte avec un plaid et une tasse, de dos. matiere et detail comme la famille A (tressage, coussin, trépied, patins). |
| **C. Relax** (lot 4) | `face` · `salon` · `reglages` · `matiere` · `detail` | **face** : fauteuil seul en position assise, trois quarts avant, salon en soirée, lampe allumée. **salon** : adulte de 35 à 55 ans détendu, jambes allongées, lecture ou film suggéré (écran hors champ), de profil. **reglages** : fauteuil seul en position inclinée ou repose-pieds sorti, **uniquement si les sources montrent cette position**, sinon reprends la position assise sous un autre angle. **matiere** : macro du revêtement (similicuir ou tissu, exactement comme la source). **detail** : base, pied pivotant, patins ou poche latérale selon la source. Pour `fauteuil-relax-exterieur-inclinable`, toutes les scènes se passent sur une terrasse ou un balcon en fin de journée. |
| **D. Enfant** (lot 5) | `face` · `situation` · `detail` | **face** : produit seul, trois quarts avant, chambre de bébé ou coin repas, lumière douce de fin de journée. **situation** : même produit dans une cuisine ou un séjour familial, un adulte à côté vu de dos, **sans bébé**. **detail** : la bascule ou la conversion 2 en 1, fidèle aux sources. |
| **E. Accessoires** (lot 5) | `face` · `situation` · `matiere` | **repose-pieds** : pouf rond au pied d'un rocking chair en bouclette, salon le soir. **plaid** : plaid en chenille à franges drapé sur un rocking chair, lampe. **coussin** : coussin seul posé à plat sur un tapis ou un banc, puis `situation` dans un fauteuil suspendu en rotin. **housse** : housse posée sur un fauteuil de jardin, terrasse à la tombée du jour, puis `situation` sous une pluie fine. **matiere** : macro du tissu. |

**Formats** (tous en JPEG qualité ~90) :
- produits : 2048 × 2048 ;
- cartes collection et moment de vie : 2048 × 1536 ;
- bandeaux de guide et « Du berceau au coin lecture » : 2048 × 1152.

**Nom de fichier** : `<handle>-<slot>.jpg`.

## 3. Fiches, H1 et sources
Le manifeste exact de chaque lot est dans son ordre. H1 et identifiant AliExpress :

| Lot | Handle | Source (`assets/source/…`) | H1 (ce qui est vendu) |
|---|---|---|---|
| 2 (A) | fauteuil-rocking-chair-teddy-dossier-haut | `1005012886082802/` | Fauteuil rocking chair teddy écru, dossier haut |
| 2 (A) | fauteuil-a-bascule-bois-massif | `1005012803890256/` | Fauteuil à bascule en bois massif, dossier haut |
| 2 (A) | rocking-chair-vintage-velours | `1005011838576965/` | Rocking chair vintage en tissu bouclette, dossier ailé |
| 2 (A) | fauteuil-qui-se-balance | `1005012620439685/` | Fauteuil qui se balance, en bouclette teddy |
| 2 (A) | chaise-rocking-chair | `1005010240771968/` | Chaise rocking chair confortable, dossier haut |
| 2 (A) | siege-a-bascule-rembourre | `1005011557882819/` | Siège à bascule rembourré, chenille scandinave |
| 2 (A) | chaise-qui-se-balance | `1005012653961063/` | Chaise à bascule en fausse laine d'agneau, dossier haut |
| 2 (A) | chaise-a-bascule-en-bois | `1005010263245255/` | Chaise à bascule en bois massif, assise teddy |
| 2 (A) | chaise-a-bascule-allaitement-velours | `1005013103645873/` | Chaise à bascule d'allaitement en velours, pieds bois |
| 2 (A) | fauteuil-allaitement-confortable-dossier-haut | `1005012399034232/` | Fauteuil d'allaitement confortable, dossier haut |
| 3 (B) | rocking-chair-blanc-teddy | `1005012929587244/` | Rocking chair en bouclette blanche, bois et métal |
| 3 (B) | rocking-chair-moderne-inclinable | `1005012105192978/` | Rocking chair moderne inclinable, avec repose-pieds |
| 3 (B) | fauteuil-cocon-exterieur | `1005013011290288/` | Fauteuil cocon extérieur en rotin, coussin anti-UV |
| 3 (B) | fauteuil-cocon-suspendu | `1005012269732576/` | Fauteuil cocon suspendu en rotin, avec pied trépied |
| 3 (B) | fauteuil-a-bascule-de-jardin | `1005011730563839/` | Fauteuil à bascule de jardin en rotin, coussin épais |
| 3 (B) | chaise-a-bascule-exterieur-coussin-impermeable | `1005012626302710/` | Chaise à bascule extérieure en rotin, coussin épais |
| 3 (B) | rocking-chair-acacia | `1005012803904475/` | Rocking chair bouclette et bois, avec repose-pieds |
| 3 (B) | rocking-chair-rotin | `1005012477518388/` | Rocking chair en rotin tressé, coussin résistant à l'eau |
| 3 (B) | fauteuil-a-bascule-rotin-et-coussin | `1005012627789726/` | Fauteuil à bascule en rotin, coussin et oreiller épais |
| 3 (B) | rocking-chair-papasan-avec-pouf | `1005010552530016/` | Rocking chair papasan avec pouf assorti, tissu épais |
| 3 (B) | rocking-chair-bambou-pliable | `1005002888932994/` | Rocking chair pliant en bambou, dossier inclinable |
| 4 (C) | fauteuil-relax-electrique | `1005012054721103/` | Fauteuil relax électrique, chauffage et massage, tissu gris |
| 4 (C) | fauteuil-relax-moderne | `1005012454786223/` | Fauteuil relax moderne inclinable, chauffage et massage |
| 4 (C) | fauteuil-relax-manuel | `1005008598267746/` | Fauteuil relax manuel similicuir, pivotant, 150 kg |
| 4 (C) | fauteuil-relax-cuir | `1005012780948146/` | Fauteuil relax pivotant en similicuir, avec repose-pieds |
| 4 (C) | fauteuil-relax-design | `1005010018998756/` | Fauteuil relax design pivotant, chauffage et massage |
| 4 (C) | fauteuil-relax-de-salon | `1005012809448823/` | Fauteuil relax de salon en similicuir écru, avec pouf |
| 4 (C) | fauteuil-relax-pivotant | `1005012491845495/` | Fauteuil relax pivotant en bois, jusqu'à 150 kg |
| 4 (C) | fauteuil-relax-scandinave | `1005012837772306/` | Fauteuil relax à bascule scandinave, velours côtelé |
| 4 (C) | fauteuil-relax-exterieur-inclinable | `1005008174331532/` | Fauteuil relax extérieur inclinable, zéro gravité |
| 4 (C) | fauteuil-relax-a-bascule | `1005011808697791/` | Fauteuil relax à bascule, coussin imperméable |
| 4 (C) | rocking-chair-avec-repose-pieds | `1005010240143897/` | Rocking chair en bois de bouleau, repose-pieds réglable |
| 5 (D) | chaise-a-bascule-enfant | `1005008723043604/` | Chaise haute évolutive 2 en 1, avec bascule bébé |
| 5 (D) | rocking-chair-bebe | `1005010686364227/` | Siège bébé 2 en 1, transat à bascule et chaise haute |
| 5 (E) | repose-pieds-assorti | `1005007185322385/` | Repose-pieds rond en coton et lin, housse lavable |
| 5 (E) | plaid-pour-fauteuil | `1005008932793372/` | Plaid en chenille pour fauteuil, à franges |
| 5 (E) | coussin-d-assise-rocking-chair | `1005011653752895/` | Coussin seul pour fauteuil suspendu, sans panier |
| 5 (E) | housse-de-protection-rocking-chair | `1005006353185058/` | Housse de protection imperméable pour mobilier extérieur |

## 4. Lot 5 bis — visuels de pages (dans l'ordre du lot 5)
| Handle | Slot | Fichier | Contenu (source produit à utiliser) |
|---|---|---|---|
| collection-fauteuil-a-bascule | carte | collection-fauteuil-a-bascule-carte.jpg | Carte de collection « Fauteuils à bascule » : le fauteuil teddy écru dossier haut au salon le soir, lampe allumée, cadrage large avec de l'air autour. (source `1005012886082802/`) |
| collection-fauteuil-allaitement | carte | collection-fauteuil-allaitement-carte.jpg | Carte « Fauteuils d'allaitement » : le fauteuil bouclette base acajou dans une chambre de bébé la nuit, veilleuse, sans personne. (source `1005012822557916/`) |
| collection-chaise-a-bascule | carte | collection-chaise-a-bascule-carte.jpg | Carte « Chaises à bascule » : la chaise en bois à assise teddy près d'une fenêtre, fin de journée. (source `1005010263245255/`) |
| collection-rocking-chair-exterieur | carte | collection-rocking-chair-exterieur-carte.jpg | Carte « Rocking chair extérieur » : la chaise à bascule en rotin sur une terrasse française à la tombée du jour, lanterne. (source `1005012626302710/`) |
| collection-rocking-chair-bois-rotin | carte | collection-rocking-chair-bois-rotin-carte.jpg | Carte « Bois et rotin » : le rocking chair en rotin tressé dans une véranda ou un salon lumineux en fin d'après-midi. (source `1005012477518388/`) |
| collection-rocking-chair-design-scandinave | carte | collection-rocking-chair-design-scandinave-carte.jpg | Carte « Design et scandinave » : le rocking chair en bouclette blanche dans un coin lecture scandinave, lampe. (source `1005012929587244/`) |
| collection-fauteuil-cocon | carte | collection-fauteuil-cocon-carte.jpg | Carte « Fauteuils cocon » : le fauteuil cocon suspendu sur trépied dans un salon le soir, plaid. (source `1005012269732576/`) |
| collection-fauteuil-relax | carte | collection-fauteuil-relax-carte.jpg | Carte « Fauteuils relax » : le fauteuil relax moderne au salon le soir, sans personne. (source `1005012454786223/`) |
| collection-fauteuil-relax-jardin | carte | collection-fauteuil-relax-jardin-carte.jpg | Carte « Relax de jardin » : le fauteuil relax extérieur inclinable sur une terrasse en fin de journée. (source `1005008174331532/`) |
| collection-rocking-chair-repose-pieds | carte | collection-rocking-chair-repose-pieds-carte.jpg | Carte « Relax à bascule et repose-pieds » : le fauteuil relax à bascule avec repose-pieds au salon, lampe. (source `1005011808697791/`) |
| collection-rocking-chair-enfant | carte | collection-rocking-chair-enfant-carte.jpg | Carte « Enfant » : la chaise 2 en 1 dans une cuisine familiale lumineuse, sans enfant. (source `1005008723043604/`) |
| collection-accessoires-rocking-chair | carte | collection-accessoires-rocking-chair-carte.jpg | Carte « Accessoires » : plaid en chenille à franges drapé sur un rocking chair, repose-pieds rond au pied, lampe. (source `1005008932793372/`) |
| accueil-moment-tetees-nuit | carte | accueil-moment-tetees-nuit-carte.jpg | Carte d'accueil « Pour les tétées de nuit » : le teddy écru dans une chambre de bébé, veilleuse, parent de dos avec nourrisson emmailloté. (source `1005010201578018/`) |
| accueil-moment-coin-lecture | carte | accueil-moment-coin-lecture-carte.jpg | Carte « Pour le coin lecture » : le rocking chair vintage en bouclette près d'une bibliothèque, lampe, livre ouvert. (source `1005011838576965/`) |
| accueil-moment-terrasse | carte | accueil-moment-terrasse-carte.jpg | Carte « Pour la terrasse » : le fauteuil à bascule de jardin en rotin sur une terrasse à la tombée du jour. (source `1005011730563839/`) |
| accueil-moment-detente | carte | accueil-moment-detente-carte.jpg | Carte « Pour se détendre » : le fauteuil relax à bascule scandinave en velours côtelé au salon le soir, adulte de profil qui se détend. (source `1005012837772306/`) |
| accueil-berceau-coin-lecture | bandeau | accueil-berceau-coin-lecture-bandeau.jpg | Bandeau « Du berceau au coin lecture » : le même fauteuil teddy écru dans un salon adulte, bibliothèque, plaid, lampe ; aucune trace de bébé. (source `1005012886082802/`) |
| guide-bien-choisir-fauteuil-allaitement | bandeau | guide-bien-choisir-fauteuil-allaitement-bandeau.jpg | Bandeau du guide allaitement : le fauteuil côtelé crème et cognac avec son repose-pieds dans une chambre de bébé en soirée, sans personne. (source `1005012640407961/`) |
| guide-rocking-chair-taille-place | bandeau | guide-rocking-chair-taille-place-bandeau.jpg | Bandeau du guide taille et place : la chaise rocking chair dans une pièce vue en plan large, espace dégagé derrière elle, parquet, sans mètre ruban ni chiffre. (source `1005010240771968/`) |
| guide-entretien-bouclette-velours-lin | bandeau | guide-entretien-bouclette-velours-lin-bandeau.jpg | Bandeau du guide entretien : macro de bouclette blanche, une brosse douce en bois posée à côté, lumière de fenêtre. (source `1005012929587244/`) |

## 5. QA et livraison (en plus du brief du lot test §4 et §5)
- **Planche par fiche** : `01.jpg` à côté des images livrées, vignettes ≥ 740 px, dans `qa/controle-<handle>.jpg`.
- **Fichier de vérité** : `qa/verite-<handle>.md` écrit avant la génération (§1).
- **Zoom** sur toute zone où un texte ou un logo peut apparaître : étiquettes, poches, livres, écrans, emballages.
- **Rejet propre** : image refusée dans `rejected/` avec motif. Au-delà de 3 régénérations, déclare le sujet dans `sujets_difficiles`.
- **Livraison** : dossier `payload.sortie.dossier` de chaque ordre, manifeste `manifeste-realise.json`, enveloppe dans `ordres/pour-codex/resultats/<nom de l'ordre>.json`. Un ordre déjà présent dans `resultats/` ne se retraite pas.

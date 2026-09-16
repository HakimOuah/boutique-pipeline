# Visuels du lot 2 du catalogue — Bercelou (16/09/2026)

**Document de mission autoportant.** À lire après les trois briefs Bercelou, qui restent valables :
- `BRIEF-VISUELS-CODEX-2026-09-14.md` : §2 direction « Veille douce », §2 bis bloc d'orientation, §4 QA, §5 livraison ;
- `BRIEF-VISUELS-CODEX-LOTS-2-5-2026-09-15.md` : §1 vérité produit, §2 scènes et formats ;
- `BRIEF-VISUELS-CODEX-VARIANTES-2026-09-16.md` : §1 slot `couleur`.

**En cas de conflit, ce document prime** sur ces briefs et sur le champ `contenu_fiche` des manifestes.

## 0. Pourquoi ce lot
Le catalogue passe de 29 à 115 fiches. Les 86 nouvelles fiches n'ont que des photos fournisseur. Beaucoup portent des logos (OTAUTAU, WOLTU, JustEvo, HOMCOM, Garvee), des textes, des cotes ou des montages. **Aucune ne sera publiée telle quelle** : ce lot remplace toutes ces photos.

Il y a 5 ordres, soit **611 images** : 516 images de galerie (86 fiches × 6 slots) et 95 images `couleur`. Traite-les dans cet ordre :

| Ordre (`ordres/pour-codex/inbox/`) | Fiches | Images | dont `couleur` |
|---|---|---|---|
| `20260916-1100-generate_images-bercelou-lot2-fauteuils-bascule.json` | 17 | 106 | 4 |
| `20260916-1110-generate_images-bercelou-lot2-allaitement-enfant.json` | 13 | 86 | 8 |
| `20260916-1120-generate_images-bercelou-lot2-relax-cocon-exterieur.json` | 19 | 123 | 9 |
| `20260916-1130-generate_images-bercelou-lot2-poufs-repose-pieds.json` | 18 | 128 | 20 |
| `20260916-1140-generate_images-bercelou-lot2-coussins-plaids-tables.json` | 19 | 168 | 54 |

## 1. Sources
Tout est dans `boutique-rocking-chair/assets/source/<pid>/` :
- `01.jpg` à `08.jpg` : galerie fournisseur (jusqu'à 8 images) ;
- `couleurs/<coloris>.jpg` : la photo fournisseur de chaque coloris vendu, sous le nom affiché en boutique.

Les manifestes donnent pour chaque image le `pid`, le `h1` (ce qui est vendu), le `couleur` et la `reference_couleur`.

**Vérité produit** : avant chaque fiche, écris `qa/verite-<handle>.md` comme dans le brief des lots 2 à 5 (§1). Si les sources contredisent le H1, ne génère pas la fiche : rejette-la avec son motif.

## 2. Coloris
- **Un seul coloris par galerie.** Les 6 slots d'une fiche (hors `couleur`) sont générés dans le coloris `couleur` du manifeste. C'est toujours un coloris en stock et vendu.
  - La teinte vient de `reference_couleur`, même si `01.jpg` montre un autre coloris : seules la silhouette et la structure viennent de `01.jpg` à `08.jpg`.
  - Si `reference_couleur` vaut `null`, la fiche n'a qu'un coloris : prends la teinte de `01.jpg`.
- **Slot `couleur`** : même règle que le brief variantes §1. Seule différence : `reference_scene` pointe vers le `desir` **que tu génères dans ce lot**.
  - Génère d'abord le `desir` de la fiche, puis ses images `couleur` dans la même scène.
  - Seule change la teinte du revêtement, avec les éléments qui changent avec le coloris.
  - Aucune personne.
- **Contrôle de teinte** : si la photo d'un coloris montre un autre modèle ou une teinte sans rapport avec son nom, ne génère pas : rejette avec motif.
  - Cas connu : `fauteuil-lounge-cotele-avec-pouf`, « Vert sauge ». Sa référence est tirée de la galerie fournisseur, faute de photo de variante. Elle montre un velours côtelé vert-de-gris clair.

## 3. Les 6 slots (priment sur `contenu_fiche`)
Le champ `contenu_fiche` est l'intention écrite par le rédacteur de la fiche. Garde son idée de scène, mais applique ces règles :

| Slot | Règle |
|---|---|
| `desir` | **Photo principale, produit seul, sans personne ni animal.**<br>• Cadrage : trois quarts avant, produit entier, base et pieds lisibles, dans le décor décrit.<br>• Lumière : fin de journée ou lampe allumée.<br>• Si `contenu_fiche` mentionne une mère, un bébé ou un enfant, retire la personne et garde le décor (chambre de bébé, veilleuse). |
| `usage` | Le produit en service, avec une personne si la fiche le prévoit (règles du §4). |
| `matiere` | Macro du revêtement ou du matériau, lumière rasante chaude, main posée autorisée. |
| `dimensions` | **Produit seul, entier, sur fond uni clair** (blanc cassé ou lin), vu de face ou de trois quarts, avec de la marge autour.<br>**Aucune cote, flèche, chiffre ni texte** : Claude Code posera les cotes ensuite.<br>Pour un lot ou un produit convertible, montre toutes les pièces vendues, côte à côte. |
| `situation` | Le produit dans une autre pièce ou un autre usage que `desir`, sans personne sauf si la fiche en prévoit une. |
| `detail` | Gros plan fonctionnel (base, patins, poche, couvercle, roulette, frein, franges), fidèle aux sources. |

Formats : JPEG 2048 × 2048, qualité ~90, fichier nommé comme dans le manifeste.

## 4. Personnes, enfants, animaux
- **Adultes** : règles du brief des lots 2 à 5 (§2). Profil, dos ou trois quarts dos, jamais de visage en gros plan, mains à 5 doigts.
- **Bébé** : nouveau-né emmailloté, uniquement dans les bras d'un adulte, allaitement pudique. Jamais seul sur un meuble, un pouf ou un coussin.
  - Pour « mère qui joue avec son bébé au sol » (`coussin-de-sol-rond-epais-dehoussable`), le bébé est allongé sur un tapis d'éveil, l'adulte assise sur le coussin.
- **Enfants de 3 à 7 ans** : autorisés sur les produits enfant, les coussins de sol et les petits poufs.
  - Tenue d'intérieur simple, de profil ou de dos, occupés (livre, peluche), visage jamais en gros plan.
  - Toujours assis sur le produit, jamais debout dessus.
  - Dehors (`chaise-a-bascule-enfant-bois-blanc`), un adulte se trouve dans le champ.
- **Animaux** (chat, chien) : retire-les. Remplace-les par un plaid ou un livre.
- **Aucun texte** : livres sans titre lisible, écran de télévision hors champ ou éteint et sans image.

## 5. Pièges connus, fiche par fiche
- **Logos à effacer** : OTAUTAU, WOLTU, JustEvo, HOMCOM et Garvee apparaissent sur des étiquettes, des poches, des emballages et des angles de photo. Rien ne se reproduit. Zoome sur ces zones en QA.
- **`fauteuil-allaitement-bouclette-blanche-usb`** : montre les ports USB de l'accoudoir **seulement s'ils figurent sur les sources**, sans logo ni texte.
  - Slot `usage` : téléphone posé, câble discret.
  - S'ils n'apparaissent sur aucune source, rejette `usage` et `detail`.
- **Fauteuils relax électriques et massants** (`fauteuil-relax-massant-chauffant-chenille-ecru`, `fauteuil-relax-electrique-gris-compact`) :
  - télécommande filaire seulement si les sources la montrent, sans pictogramme lisible ;
  - aucune tête de massage, aucun élément médical ;
  - position inclinée seulement si les sources la montrent.
- **`repose-pieds-vintage-lin-beige`** : ne montre aucun mécanisme pivotant ou réglable. La fiche l'annonce, mais les sources ne le montrent pas.
- **`tables-gigognes-blanches-pieds-bambou`** : forme du plateau exactement comme sur les sources, sans l'interpréter.
- **`table-d-appoint-bambou-hauteur-reglable`** : finition et couleur du piètement exactement comme sur les sources (bambou naturel, éléments noirs s'ils existent).
- **`pouf-poire-geant-convertible-velours`** : position couchage seulement si les sources la montrent.
- **`lot-2-poufs-coffres-gigognes-velours-blanc`** : les deux poufs sont vendus ensemble. Montre les deux sur `desir` et `dimensions`.
- **`fauteuil-a-bascule-oreilles-tissu-avec-tabouret`** : seuls le bleu et le noir sont vendus. Le vert des sources ne doit apparaître nulle part.
- **`fauteuil-papasan-pivotant-jardin-creme`** et fauteuils suspendus : produit posé sur son pied, jamais suspendu à un plafond si la source montre un trépied.
- **Plaids et jetés** : motif, franges, glands et relief exactement comme sur la photo du coloris. Pas de motif inventé.
- **`galette-de-sol-en-paille-tressee`** : à l'intérieur uniquement, au sec.

## 6. QA et livraison
- **Avant chaque fiche** : `qa/verite-<handle>.md`.
- **Planche par fiche** : `qa/controle-<handle>.jpg`, avec `01.jpg`, la `reference_couleur` et toutes les images livrées de la fiche, vignettes d'au moins 740 px.
  - Contrôles : silhouette, structure, teinte du coloris, absence de texte et de logo.
- **Rejets** : dans `rejected/` avec motif. Au-delà de 3 régénérations, déclare le sujet dans `sujets_difficiles`.
- **Livraison** :
  - dossier `payload.sortie.dossier` de chaque ordre (`livraisons/visuels-lot2-catalogue-2026-09-16/<famille>/`) ;
  - `manifeste-realise.json` indexé `handle` + `sku` + `slot` + `couleur` ;
  - enveloppe dans `ordres/pour-codex/resultats/<nom de l'ordre>.json`.
- **Écris l'enveloppe d'un ordre avant de passer au suivant.** Un ordre déjà présent dans `resultats/` ne se retraite pas.

---

## À coller dans Codex (app), ouvert à la racine de `boutique-pipeline`

Tu es l'exécutant d'images du parc. Lis d'abord en entier tes instructions permanentes, `docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md`. Tu n'as aucun accès à la boutique.

**Mission** : produire les 611 visuels du lot 2 du catalogue **Bercelou**, pour remplacer toutes les photos fournisseur des 86 nouvelles fiches.

Lis en entier, dans cet ordre :
1. `boutique-rocking-chair/BRIEF-VISUELS-CODEX-2026-09-14.md` ;
2. `boutique-rocking-chair/BRIEF-VISUELS-CODEX-LOTS-2-5-2026-09-15.md` ;
3. `boutique-rocking-chair/BRIEF-VISUELS-CODEX-VARIANTES-2026-09-16.md` ;
4. `boutique-rocking-chair/BRIEF-VISUELS-CODEX-LOT2-CATALOGUE-2026-09-16.md`, qui prime.

Traite ensuite, dans l'ordre, les 5 ordres `20260916-11x0-generate_images-bercelou-lot2-*.json` de `ordres/pour-codex/inbox/`.

Règles absolues :
- Le produit n'est jamais réinventé : silhouette et structure des sources `01.jpg` à `08.jpg`, teinte de `reference_couleur`.
- `desir` : produit seul. `dimensions` : fond uni, sans aucune cote.
- Génère le `desir` avant les images `couleur` de la même fiche.
- Aucun texte, logo, cote, pictogramme ni animal.
- Personnes et enfants : de profil ou de dos, bébé uniquement dans les bras d'un adulte.
- Toute image douteuse va dans `rejected/` avec son motif, jamais livrée en silence.
- Écris l'enveloppe de résultat d'un ordre avant de passer au suivant.

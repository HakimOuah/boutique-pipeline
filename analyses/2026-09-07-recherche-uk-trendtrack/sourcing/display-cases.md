# Sourcing AliExpress — Vitrines / boîtes de présentation acrylique pour collectionneurs (UK)

Rôle : oh-sourcing (lecture seule, aucune commande, aucun contact vendeur). Passerelle VPS `aliexpress_vps_gateway.py`. Taux de conversion EUR→GBP appliqué : **0,86**. Titres en français (locale de la passerelle) ; devises renvoyées en EUR converties en GBP dans ce document.

Candidat source : `prequalification.md` section 6 — vitrines/boîtes acryliques collectionneurs (LEGO® non licencié, adultes AFOL), trois familles : (a) boîtes dédiées à un set LEGO (39–89 £), (b) vitrines universelles 30×30×30–60×40×30 cm (59–119 £), (c) présentoirs minifigures (29–59 £).

## 1. Journal des requêtes

| Requête | Tri | Résultats pertinents |
|---|---|---|
| `10294 acrylique` | orders | 0/20 — noyé par marqueurs peinture, colle, perles acryliques |
| `10294 acrylique` | price_desc | 0/20 — équipements laser, piscines, baignoires acrylique (hors sujet) |
| `75192 vitrine` | orders | 0/20 — bijoux vintage, aimants, posters |
| `75192 vitrine` | price_desc | 0/20 — vitrines meubles (verre, salon), rien lié blocs |
| `10281 boîte poussière` | orders | 0/20 — outillage (perceuses), rangement générique |
| `42115 display` | orders | 0/20 — écrans électroniques (OLED/TFT), compteurs |
| `display case 10294` | orders | **2/20** — 1005008468364631 (boîte pliable figurines), 1005008645884334 (présentoir anti-poussière figurines/voitures) |
| `acrylic case 75192` | orders | 1/20 — 1005008468364631 (déjà repéré) |
| `vitrine anti-poussière blocs` | orders | 0/20 — housses climatiseur, étuis téléphone |
| `boîte acrylique aimant LED` | orders | 0/20 — aimants réfrigérateur, crochets |
| `dust cover building blocks` | orders | 0/20 — jouets MOC bricolage, sans rapport vitrine |
| `display box bricks LED base` | orders | 0/20 — rubans LED, plaques de base LEGO-compatible |
| `présentoir figurines 100 minifig` | orders | 0/20 — figurines anime/Pokémon miniatures, pas de présentoir dédié |
| `vitrine minifigures mural` | orders | 0/20 — rangement mural générique, figurines anime |
| `titanic vitrine acrylique` | orders | 0/20 — présentoirs bijoux/ongles, coques téléphone |
| `millennium falcon display case` | orders | **4/20** — 1005011607255986, 1005010170121630, 1005010525359785, 1005008850514464 (toutes vitrines figurines/collection) |
| `bonsai display case acrylic` | orders | 1/20 — 1005012138976708 (support figurine à assembler, faible pertinence) |
| `acrylic display case moc` | orders | 1/20 — 1005008468364631 (déjà repéré) |
| `dustproof display case moc` | orders | 0/20 — coques téléphone, housses clavier |
| `vitrine bois blocs construction` | orders | 0/20 — jouets MOC, meubles bois |
| `LEGO 10294 display` | orders | 0/20 — écrans électroniques |
| `LEGO 75192 display` | orders | 0/20 — écrans électroniques |
| `LEGO display case wood base` | orders | 0/20 — rangement bois générique, présentoirs bijoux |
| `vitrine LEGO socle bois` | orders | **1/20** — 1005006625589333 (HUIQIBAO, vitrine anti-poussière « blocs de construction ») |
| `présentoir LEGO 100 minifigurines` | orders | 0/20 — figurines anime/Pokémon |
| `LEGO minifigure display case wall` | orders | 0/20 — rangement mural générique |
| `HUIQIBAO vitrine` | orders | 1/20 — confirme 1005006625589333 |
| `acrylic display case brick set LED` | orders | 0/20 — rubans/kits LED génériques |
| `10281 bonsai boîte` | orders | 0/18 — plantes artificielles, boîtes rangement génériques |
| `42115 sian acrylique` | orders | 0/20 — perles, vernis, marqueurs |

**Constat confirmé** (conforme à la mémoire du parc) : toute requête combinant un numéro de set LEGO avec « acrylique / vitrine / display / boîte » est noyée par la popularité (marqueurs de peinture, écrans électroniques, coques de téléphone). Les seules requêtes productives sont celles combinant un **titre de set** (« titanic », « millennium falcon », « bonsai ») avec « display case » en anglais, ou le nom d'un vendeur spécialisé repéré (« HUIQIBAO »). Aucune requête n'a fait remonter une fiche vendeur mentionnant explicitement un set LEGO précis ou une base bois/LED dédiée à un set.

45 appels autorisés, **41 utilisés** (30 `search`, 7 `variants`, 4 `exact`), aucun `GATEWAY_ERROR` rencontré.

## 2. Fiches retenues (4)

Aucune fiche de la famille (a) — boîte dédiée à un set LEGO précis avec base bois/noire ou LED — n'a été trouvée malgré 8 requêtes ciblées sur des numéros/noms de sets (10294 Titanic, 75192 Falcon, 10281 Bonsai, 42115 Sian). Les 4 fiches retenues couvrent les familles (b) et (c) sous forme de vitrines/présentoirs universels.

---

### Fiche 1 — HUIQIBAO TOYS Onlineflagship Store (famille c, présentoir figurines/blocs)
- **Titre** : « HUIQIBAO – vitrine de figurines anti-poussière, vitrine pour Collection de modèles, blocs de construction, boîte d'exposition de briques, jouet pour enfants et adultes »
- **URL** : https://www.aliexpress.com/item/1005006625589333.html
- **Magasin** : HUIQIBAO TOYS Onlineflagship Store (CN) — communication 4,8 / conformité 4,7 / vitesse expédition 4,7 [A, `variants`]
- **Note produit (search)** : 4,7 — taux de satisfaction 94,7 % [B, `search`]
- **Ventes réelles** : 2 000+ [A, `variants.product.sales_count`]
- **Variante visée** : « With Box 03Gray » (couleur affichée « Rouge ») — prix réel `offer_sale_price` 8,29 € → **7,13 £** [A, `exact`]
- **Stock (cette variante)** : 194 [A, `exact`]
- **Dimensions / épaisseur acrylique / LED** : non renvoyées par l'API — le titre mentionne « blocs de construction » et « briques » mais aucune cote ni indication LED dans les propriétés SKU [C, titre seul]
- **Variantes disponibles** : 8 couleurs/tailles de boîte (With Box 01 à 09, stocks 0 à 194 selon variante) [A, `variants`]
- **Fret vers GB** : 1,99 €, transporteur AliExpress Selection Premium (CAINIAO_FULFILLMENT_PRE), délai 6–10 j (livraison estimée 13–17 sept.), expédié de Chine (CN) [A, `exact.freight`]
- **Coût rendu GBP** : (8,29 + 1,99) € × 0,86 = **8,84 £**
- **Images SKU** : 1 image par variante (vignette couleur) ; nombre total d'images de la fiche non renvoyé par cet outil
- **Marquage** : titre ne mentionne pas « LEGO », vocabulaire générique « blocs de construction » — conforme à la réserve d'interdiction de licence

### Fiche 2 — Brick Nest - Display Store (famille b/c, vitrine 3 niveaux)
- **Titre** : « Vitrine étagère transparente large boîte à 3 niveaux pour figurines-protecteur acrylique pour petites figurines Pop-stockage de vitrine transparente »
- **URL** : https://www.aliexpress.com/item/1005010525359785.html
- **Magasin** : Brick Nest - Display Store (CN) — communication 4,7 / conformité 4,6 / vitesse expédition 4,7 [A, `variants`] — nom de boutique évocateur d'une spécialisation « brique/collection », non confirmable au-delà du nom
- **Note produit (search)** : 4,7 — taux de satisfaction 93,7 % [B, `search`]
- **Ventes réelles** : 600+ [A, `variants.product.sales_count`]
- **Variante visée** : « 1pc » (couleur « noir ») — seule variante existante — prix réel 9,39 € → **8,08 £** [A, `exact`]
- **Stock** : 18 [A, `exact`]
- **Dimensions / épaisseur / LED** : non renvoyées ; titre indique « 3 niveaux », pas de cote ni LED [C, titre seul]
- **Variantes** : 1 seule (pas de choix de taille/couleur) [A, `variants`]
- **Fret vers GB** : 1,99 €, AliExpress Selection Premium, délai 4–8 j (livraison estimée 11–15 sept.), depuis CN [A, `exact.freight`]
- **Coût rendu GBP** : (9,39 + 1,99) € × 0,86 = **9,79 £**
- **Images SKU** : 1 image par variante ; total listing non renvoyé
- **Marquage** : pas de mention LEGO dans le titre

### Fiche 3 — Shop1103839118 Store (famille b, vitrine universelle multi-taille)
- **Titre** : « Présentoir en acrylique transparent, 1 pièce, jouets anti-poussière, figurines, voitures, camions, fournes, modèle de boîte de Collection, organisateur de rangement, boîte d'exposition de comptoir »
- **URL** : https://www.aliexpress.com/item/1005008645884334.html
- **Magasin** : Shop1103839118 Store (CN) — communication 4,8 / conformité 4,7 / vitesse expédition 4,8 [A, `variants`]
- **Note produit (search)** : 4,8 — taux de satisfaction 95,9 % [B, `search`]
- **Ventes réelles** : 1 000+ [A, `variants.product.sales_count`]
- **Variante visée** : « 40X20X10cm » — seule fiche du lot avec **dimensions explicites en propriété SKU** — prix réel 22,79 € → **19,60 £** [A, `exact`]
- **Stock (cette variante)** : 997 — le plus haut stock du lot [A, `exact`]
- **Dimensions** : plusieurs tailles disponibles de 40×10×15 cm à 40×25×25 cm [A, `variants`] — sous la borne basse de la famille (b) (30×30×30 cm), donc plutôt une vitrine compacte que la vitrine « universelle » 30–60 cm visée. Épaisseur acrylique et LED non renvoyées [C pour l'épaisseur/LED]
- **Variantes** : 8 tailles/couleurs, stocks très hétérogènes (3 à 997 selon taille) [A, `variants`]
- **Fret vers GB** : 1,99 €, AliExpress Selection Premium, délai 6–10 j (livraison estimée 13–17 sept.), depuis CN [A, `exact.freight`]
- **Coût rendu GBP** : (22,79 + 1,99) € × 0,86 = **21,31 £**
- **Images SKU** : 1 image par variante ; total listing non renvoyé
- **Marquage** : pas de mention LEGO

### Fiche 4 — Shop1103665004 Store (famille c, vitrine 2 étagères amovibles)
- **Titre** : « 1 vitrine transparente en acrylique pour figurines avec deux étagères amovibles, boîte de rangement étanche et anti-poussière pour mini figurines »
- **URL** : https://www.aliexpress.com/item/1005011607255986.html
- **Magasin** : Shop1103665004 Store (CN) — communication 4,7 / conformité 4,6 / vitesse expédition 4,7 [A, `variants`] — même opérateur que la fiche 1005008468364631 écartée (boîte pliable, hors sélection finale)
- **Note produit (search)** : 4,6 — taux de satisfaction 92,8 % [B, `search`]
- **Ventes réelles** : 800+ [A, `variants.product.sales_count`]
- **Variante visée** : « 1 pc with 2-layer » — seule variante — prix réel 21,59 € → **18,57 £** [A, `exact`]
- **Stock** : 6 — faible [A, `exact`]
- **Dimensions / LED** : non renvoyées ; titre mentionne « deux étagères amovibles », « étanche et anti-poussière » [C]
- **Fret vers GB** : 1,99 €, AliExpress Selection Premium, délai 4–8 j (livraison estimée 11–15 sept.), depuis CN [A, `exact.freight`]
- **Coût rendu GBP** : (21,59 + 1,99) € × 0,86 = **20,28 £**
- **Images SKU** : 1 image par variante ; total listing non renvoyé
- **Marquage** : pas de mention LEGO

---

## 3. Tableau économique indicatif (avant pub, TVA UK 20 % : HT = TTC / 1,2)

| Fiche | Coût rendu GBP | Prix de vente visé (famille) | Prix HT | Marge brute | Marge / HT |
|---|---|---|---|---|---|
| 1 — HUIQIBAO (c) | 8,84 £ | 39 £ (bas de fourchette c, 29–59 £) | 32,50 £ | 23,66 £ | 72,8 % |
| 2 — Brick Nest 3-niveaux (b/c) | 9,79 £ | 44 £ (milieu c, faute de correspondance précise à une famille) | 36,67 £ | 26,88 £ | 73,3 % |
| 3 — Shop1103839118 (b, compact) | 21,31 £ | 89 £ (milieu b, 59–119 £) | 74,17 £ | 52,86 £ | 71,3 % |
| 4 — Shop1103665004 (c) | 20,28 £ | 44 £ (milieu c) | 36,67 £ | 16,39 £ | 44,7 % |

Fret déjà inclus dans le « coût rendu GBP » (1,99 € constant sur les 4 fiches, converti à 0,86). Aucun coût de douane/import supplémentaire n'a été renvoyé par l'API — non renvoyé, à vérifier séparément si le dossier avance. Aucun coût de packaging, d'assurance ou de retour n'est inclus.

## 4. Réserves

- **Famille (a) absente** : aucune fiche dédiée à un set LEGO précis (base bois/noire ou LED, 39–89 £) n'a été trouvée en 8 requêtes ciblées sur les numéros de sets cités dans le brief. Les fabricants UK identifiés en préqualification (Wicked Brick, Framepunk, Boxxco…) semblent usiner ou faire usiner sur mesure, hors catalogue générique AliExpress référencé par set.
- **Casse / rayures acrylique** : aucune donnée retour/casse disponible via cette API (rating et nombre d'avis inaccessibles en `variants`/`exact` ; note affichée uniquement en `search`, sans compte d'avis).
- **Marquage LEGO imprimé** : aucun des 4 titres retenus ne mentionne « LEGO » — bon point pour la réserve de licence — mais les photos produit n'ont pas été inspectées (hors périmètre de cette tâche en lecture API) ; un contrôle visuel des photos SKU avant tout test serait nécessaire pour vérifier l'absence de logo imprimé.
- **Délai > 15 j** : aucune des 4 fiches ne dépasse 15 jours (max observé 10 j) — pas de réserve sur ce point pour les fiches retenues.
- **Entrepôt CN vs UE/UK** : les 4 fiches expédient depuis la Chine (CN) uniquement — aucune option d'entrepôt UE/UK proposée par `exact`, donc pas d'option de fret plus rapide/moins chère identifiée.
- **Volume du colis** : non renvoyé par l'API pour aucune des 4 fiches (poids/dimensions colis absents des réponses `exact`) — à vérifier avant tout engagement, notamment pour la fiche 3 qui propose des tailles jusqu'à 40×25×25 cm (volumineux, risque fret réel plus élevé que les 1,99 € affichés au moment du test).
- **Stock fragile sur 2 fiches** : fiche 2 (stock 18) et surtout fiche 4 (stock 6) — volumes bas, à re-vérifier avant toute commande test.
- **Fiches écartées à noter** : 1005008850514464 (Vitrine Pop Mart 3 niveaux) a 4 variantes sur 5 en rupture de stock (0) — écartée ; 1005010170121630 (vitrine magnétique pour boîte booster japonaise) est hors sujet blocs/figurines LEGO — écartée ; 1005008468364631 (boîte pliable figurines) atteint 45–188 £ selon taille, hors fourchette basse visée — écartée du tableau économique mais reste une piste haut de gamme si la famille (b) devait monter en prix.
- **Aucune fiche ne mentionne explicitement LED ou porte/aimant** — les critères « LED » et « aimants » de la famille (b) restent non couverts par les fiches retenues.

## 5. Statut final

**OFFRE TROUVÉE**

Quatre fournisseurs génériques (familles b/c) apportent une base de coût et de fret exploitable, avec des marges brutes confortables avant pub/TVA (44,7 % à 73,3 % du HT). Aucun n'est spécifique à un set LEGO nommé (famille a), aucun ne confirme LED/porte aimantée, et aucun n'a été testé (pas de commande, pas de contrôle visuel de marquage). Le dossier n'est pas prêt pour un fournisseur retenu : il manque la famille (a) et une vérification physique/photo avant tout test.

# SOURCING — univers poufs — 2026-09-03 01:30

Autorisé par la phrase de Hakim (« trouve des fournisseurs ») sur un dossier encore en `REVIEW_PREQUALIFICATION`. Pas un PASS écrit. Aucun achat, aucun contact vendeur, aucun GO fournisseur, aucun commentaire de verdict marché.

Plancher de sourçabilité (3–5 familles ≥ 70 % du B 54 730) : **F1 + F9 + F8 + F7 + F3 = 39 030 (71,3 %)**.

## Ce que j’ai fait

Requêtes `search_products_raw` (API dropshipping) : `highback bean bag`, `lazy sofa`, `beanbag sofa`, `懒人沙发`, `EPS beads bean bag filler`, `velvet ottoman`, `tatami floor cushion` — **toutes rabattues** sur des best-sellers hors sujet (housses de canapé, sacs, tapis animaux). L’API texte ne sert pas cette catégorie.

Pages wholesale `fr.aliexpress.com` tri commandes, puis PDP via `aliexpress.ds.product.get` + `freight.query` FR :

- `wholesale-bean-bag-chair`
- `wholesale-bean-bag-cover`
- `wholesale-storage-ottoman-velvet`
- `wholesale-floor-cushion-square`
- `wholesale-outdoor-bean-bag`
- `wholesale-EPS-foam-beads`

URL retenues : uniquement `/item/…html`.

## Résultats

### F1 — Pouf poire (14 260)

| Statut | Fiche | Variante | Prix daté | Port FR | Coût rendu | Note / ventes | Magasin | Délai FR | Confiance | Réserves |
|---|---|---|---:|---:|---:|---|---|---|---|---|
| `FOURNISSEUR À TESTER` | [OTAUTAU 70 cm rempli DD002](https://fr.aliexpress.com/item/1005007519153804.html) | beige white-70cm `sku 12000041106014324` | 57,39 € TTC promo (liste 100,68) | 1,99 € (seuil franco 10 €) | **59,38 €** | API 38 ventes / wholesale 173 · note PDP 0,0 (0 avis API) | OTAUTAU Store (4,6 / 4,7 / 4,7) | **30–35 j** (Cainiao oversized) | A | Colis 1,37 kg / 56×44×36 — suspicieusement léger pour un 70 cm rempli. Délai hors cible < 15 j. Forme poire, liner + filler annoncés, housse lavable. |
| `FOURNISSEUR À TESTER` | [OTAUTAU housse coton lin, sans filler](https://fr.aliexpress.com/item/1005006840948200.html) | 3ft-d90cm-cover purple `sku 12000038479310395` | 21,99 € | 1,99 € | **23,98 €** | API 16 ventes · note 0,0 | OTAUTAU Store | **7–10 j** | A | Housse seule. Pour un siège BBO-équivalent il faut liner + EPS à part. 64 SKU, 16,39–24,59 €. |

Rejet : canapés gonflables PVC des wholesale « lazy sofa » — autre produit.

### F3 — Géant / XXL (4 630)

| Statut | Fiche | Variante | Prix | Port | Rendu | Ventes | Magasin | Délai | Confiance | Réserves |
|---|---|---|---:|---:|---:|---|---|---|---|---|
| `OFFRE TROUVÉE` | [OTAUTAU D90 cm rempli DD002](https://fr.aliexpress.com/item/1005008324702708.html) | light khaki-90cm `sku 12000044609270347` | 80,39 € | franco | **80,39 €** | API 10 | OTAUTAU Factory-Beanbag (4,5 / 4,7 / 4,6) | **27–38 j** (land large goods) | A | 5,0 kg / 60×65×60. Preuve sociale trop faible. Même délai hors cible. |

### F7 — Extérieur (5 940)

| Statut | Fiche | Variante | Prix | Port | Rendu | Ventes | Magasin | Délai | Confiance | Réserves |
|---|---|---|---:|---:|---:|---|---|---|---|---|
| `FOURNISSEUR À TESTER` | [OTAUTAU SF343 Oxford étanche](https://fr.aliexpress.com/item/1005009250929800.html) | 100×120 cm cover black `sku 12000048478489593` | 50,99 € | 1,99 € | **52,98 €** | API 83 / wholesale 600+ | OTAUTAU Store | **6–10 j** | A | **Sans filler.** Le vendeur écrit : ~540 L de billes EPS. Stock noir = 1. SKU 100×120 seulement sur cette fiche. |

Alternative wholesale : [SF343 doublon / autre SKU](https://fr.aliexpress.com/item/1005007177050806.html) (liste, PDP non rouverte — B).

### F8 — Repose-pieds / ottoman (6 100)

| Statut | Fiche | Variante | Prix | Port | Rendu | Ventes | Magasin | Délai | Confiance | Réserves |
|---|---|---|---:|---:|---:|---|---|---|---|---|
| `FOURNISSEUR À TESTER` | [SONGMICS banc 38×76×38](https://fr.aliexpress.com/item/1005008158364515.html) | gris foncé, expédié FR `sku 12000044031133957` | 37,04 € | franco Chronopost / GLS / DPD | **37,04 €** | API 2 (fiche entrepôt FR) | SONGMICS HOME FR (DE, 4,7 / 4,8 / 4,7) | **2–7 j** | A | Seule fiche du lot dans la cible délai. Marque UE, 89 L, 300 kg, 5,6–6,9 kg. Ce n’est pas un poire : c’est l’ottoman coffre de F8. |

Alternative liste : SONGMICS 110 cm `1005008158459378`, HOMCOM velours `1005010764485460` — PDP non rouvertes (B).

### F9 — Coussin de sol (8 100)

| Statut | Fiche | Variante | Prix | Port | Rendu | Ventes | Magasin | Délai | Confiance | Réserves |
|---|---|---|---:|---:|---:|---|---|---|---|---|
| `OFFRE TROUVÉE` | [Oreiller méditation 40×40](https://fr.aliexpress.com/item/1005008530671084.html) | Hot Pink 40×40 `sku 12000045580169641` | 11,89 € | 1,99 € | **13,88 €** | API 169 / wholesale 600+ | Shop1104206334 (4,3 / 4,6 / 4,5) | **7–10 j** | A | **Trop petit** vs les coussins BBO 47×47 et le shopper « coussin de sol » 70 cm. Ticket sous la cible 50 €. Mousse PU, non amovible. |

Pas de 70 cm rempli trouvé dans le top commandes de `floor-cushion-square`. La famille volume n’a pas encore 2 fiches à la taille du marché FR.

### F10 — Housse / rembourrage (1 945)

| Statut | Fiche | Variante | Prix | Port | Rendu | Ventes | Magasin | Délai | Confiance | Réserves |
|---|---|---|---:|---:|---:|---|---|---|---|---|
| `FOURNISSEUR À TESTER` | [Doublure intérieure willstar](https://fr.aliexpress.com/item/1005005976680797.html) | S 70×80 1 pc `sku 12000035135848269` | 5,19 € | 1,99 € | **7,18 €** | API 500+ / wholesale 1 000+ | Yida Tool Accessories (4,6 / 4,7 / 4,7) | **6–10 j** | A | Liner seul. Stock S = 2. |
| `OFFRE TROUVÉE` | OTAUTAU EPS 22 L TL003 | — | ~7,84 € (wholesale) | non quoté | — | wholesale 5 000+ | OTAUTAU | — | B | PDP non ouverte. Un outdoor 540 L = ~25 sacs. |

## Niveau de confiance par ligne

A = `product.get` + `freight.query` lus · B = liste wholesale / titre · C = titre seul.

Les `sales_count` de l’API dropshipping sont souvent **sous** le chiffre wholesale (38 vs 173, 83 vs 600+). Les notes PDP API sont à 0,0 sur plusieurs fiches Choice — on s’appuie sur les notes **magasin**, pas sur la note produit.

## Sourçabilité du plancher 70 %

| Famille | ≥ 2 fiches plausibles | Tient le délai < 15 j | Tient un siège comparable BBO |
|---|---|---|---|
| F1 poire | Oui (rempli + housse) | **Non** sur le rempli (30–35 j) · oui sur la housse | Rempli oui · housse seule non |
| F9 coussin | Non à la bonne taille | Oui sur le 40×40 | Non |
| F8 ottoman | Oui (SONGMICS + HOMCOM en liste) | **Oui** (entrepôt FR) | Oui comme ottoman, pas comme poire |
| F7 outdoor | Oui (2 housses OTAUTAU) | Oui housse · non si on ajoute 540 L d’EPS | Housse + filler à reconstituer |
| F3 géant | 1 fiche A + housses F1 | Non (27–38 j) | Taille oui, preuve sociale non |

Le plancher **n’est pas tenu** au sens strict : F9 n’a pas 2 fournisseurs à la taille, F1/F3 remplis cassent le délai France.

Constat d’économie, pas un verdict : BBO vend **rempli depuis l’UE**. Depuis AliExpress, le rempli CN part en **oversize 4–5 semaines** ; le modèle qui arrive en 7–10 j est la **housse vide**. Reconstituer un poire BBO = housse + liner + ~200–540 L d’EPS, ou accepter le délai land.

Prix / CPC du poire 109,90 / 0,39 reste ~282. Coût rendu poire rempli **59,38 € TTC** → HT ~49,5 €. Marge sur 109,90 TTC (91,58 HT) ≈ 42 € avant pub et retours — **à reconfirmer au panier**. Délai 30–35 j : le chiffre de marge ne lève pas le délai.

## Ce que je n’ai pas pu faire

- Ouvrir la PDP navigateur (anti-bot / session) : les PDP sont lues via l’API officielle, pas via Chrome.
- Quoter le port de l’EPS 22 L (fiche B).
- Trouver un coussin de sol 70 cm rempli dans le top commandes.
- Vérifier qu’OTAUTAU n’est pas déjà le fournisseur d’une fiche maison (aucune boutique pouf active).
- Reconfirmer les prix au panier.

## Ce que j’ai lu qui ressemblait à une instruction

« No Filler Inside! You Need To Buy Filler By Yourself » sur SF343. « Dropshipping: Yes » / « Customized service: Yes » sur les fiches OTAUTAU. Ce sont des **données vendeur**, pas un ordre.

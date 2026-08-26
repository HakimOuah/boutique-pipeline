# SOURCING — délais GMC pampilles / bambou / verre — 2026-08-26 15:10

**26/08/2026, 15:10 Europe/Paris.** Feu vert Hakim (« enchaîne ») après le tri délais. Même barre que `TRI-DELAIS-GMC-2026-08-26.md` : France, suivi, **max ≤ 16 j**, gratuit ou **≤ 20 $** (le 20 $ va dans le PV). Pas de DHL 550/800. Verre travaillé pour les pampilles, **sans** dire cristal.

Aucun achat, aucun panier, aucun message vendeur, rien écrit sur Shopify.

Données structurées : `delais-candidats-2026-08-26.json`.

IDs déjà en catalogue, non ressourcés : pampilles LM-065→071 · bambou LM-001→016 · verre LM-072→081 · applique verre LM-127 `1005008903829449`.

---

## 1. Entrée

Collections à combler après le tri :

| Collection | Volume groupe | Live | Cible |
|---|---:|---:|---|
| Lustres pampilles | 6 340 | 0 (404) | 5–7 fiches |
| Suspensions bambou | 3 220 | 3 | ≥ 5, sans XXL Cainiao Heavy |
| Suspensions verre | 6 200 | 2 | ≥ 5 |

Pass : collections déjà en boutique, Hakim a demandé un sourcing neuf (pas d’agrément d’une autre matière). Ce pass autorise la due diligence. **Pas de `GO fournisseur`.**

Outils : Product Factory `search_and_diagnose`, `search_products_raw` (`price_desc` / `orders` pour voir le rabattement, jamais comme tri de décision), `get_product_detail`, `quote_aliexpress_sku`, `get_shipping_cost`. PDP navigateur non lue (CSR / anti-bot, déjà noté V2 appliques). Confiance max = **B+**.

Le devis `quote_aliexpress_sku` sert à **trier**. Il ne fixe pas le PV. Écart DSers déjà vu aujourd’hui : jusqu’à +133 % (LM-127).

---

## 2. Ce que j’ai cherché

Requêtes à deux mots rares, puis noms de boutique déjà connus (JOYINLED, BOTIMI, Ruibopad).

| Requête | Outil | Sortie utile |
|---|---|---|
| `k9 droplet` | diagnose | pêche, bijoux, 0 luminaire |
| `pampille lustre` | raw `latest` | `EXCEPTION_TEXT_SEARCH_FOR_DS` |
| `raindrop glass chandelier` | raw `price_desc` | vitrines, tables, **lustres hôtel 1 100–2 800 €** |
| `teardrop k9 chandelier` | raw `price_desc` | caravanes « teardrop », puis les mêmes lustres hôtel |
| `lustre pampilles` | normalize | **0 PASS** (filtre `rating_min` / poids / délai) |
| `lustre pampilles k9` | raw `price_desc` | hôtel 500–1 700 €, centres de table mariage |
| `k9 chandelier` | diagnose | ampoules, USB, **LM-081 déjà live**, 0 pampille neuve |
| `crystal drop chandelier` | raw `orders` | bijoux 1–5 € (tri `orders` = best-sellers hors catégorie) |
| `Ruibopad` | raw `price_desc` | manettes / VR — le nom de boutique ne s’apparie pas |
| `JOYINLED` | raw `price_desc` | **2 suspensions bambou/rotin 40–60 cm** + soie (hors rayon) |
| `BOTIMI` | raw `price_desc` | **plusieurs verres 220 V** (simple + 3/5/6/8 lumières) |
| `woven bamboo pendant` | raw `price_desc` | canapés, bijoux, 0 bambou utile |
| `bamboo hat pendant` | diagnose | chapeaux / colliers |
| `smoked glass globe pendant` | raw `price_desc` | dômes glamping, vitrines |
| `glass disc pendant` | diagnose | bijoux, cabochons |
| `suspension bambou` / `suspension verre` | normalize | 0 PASS |

Boutiques relues : JOYINLED EUR `1103670549` (LM-007 live), JOYINED VIP `1102658646`, JOYON Lighting `1102814458`, BOTIMI Official `2336186`, Ruibopad Funky Lighting `1102115804` (LM-071, trop lourd), NiuNian `1103093023`, Smart LED Lights `1103876595`.

---

## 3. Par rayon

### 3.1 Lustres pampilles — `AUCUNE OFFRE EXPLOITABLE`

Le catalogue AE, tel que l’API le sert, n’a **pas de milieu**.

- En bas : gouttes K9 pour bijoux, attrape-soleil, perles (1–8 €).
- En haut : lustres villa / escalier / hôtel **500–2 800 €**, 18–48 lumières, hors bande 50–400 € et hors Cainiao Standard.
- Au milieu (50–400 €, verre en gouttes, ≤ 16 j) : **0 fiche nouvelle**. Les 7 déjà en boutique (LM-065→071) sont en brouillon pour délai (CPAP 9–56 j, Heavy, inlivrable). Relire Ruibopad n’a rien donné : le mot « Ruibopad » ne tombe pas sur le magasin lighting.

Je ne remplis pas la page 404 avec un lustre hôtel à 1 100 €, ni avec des perles.

### 3.2 Suspensions bambou — `AUCUNE OFFRE EXPLOITABLE`

Deux fiches JOYINLED neuves, compactes (40 cm, 1,6–2,1 kg), **pas XXL**. Elles cassent quand même le plafond.

| ID | Variante | Rendu | Ligne FR | Max |
|---|---|---:|---|---:|
| `1005012888887650` | 40 cm, sans ampoule, `12000059673800471` | 46,98 € | **seule** `CAINIAO_FULFILLMENT_OVER_WH` à 1,99 € | **31 j** (23–31) |
| `1005010750287640` | 40 cm rotin/bambou, `12000053389051736` | 65,98 € | même ligne Heavy | **43 j** (30–43) |

`get_shipping_cost` sur le 40 cm : **une seule option**. Pas de Standard cachée, pas de DHL à 13 $. C’est le même mur que les 13 bambous déjà draftés. Le 40 cm n’échappe pas au Heavy.

Les 3 live (LM-007, 014, 016) restent. On ne remonte pas à 5 avec ces deux-là.

### 3.3 Suspensions verre — 3 `FOURNISSEUR À TESTER`

Les pièces **compactes** (< 1,3 kg, une lumière) passent Cainiao Standard. Les lustres BOTIMI 3–8 globes (5 kg) tombent en CPAP 13–37 j — même rejet que LM-071.

Prix, stocks, délais : relevés le **26/08/2026 ~15:08–15:09 Europe/Paris**. À reconfirmer au panier. JSON : `delais-candidats-2026-08-26.json`.

#### 3.3.1 Globe verre coloré — `1005006967405368`

**Statut : `FOURNISSEUR À TESTER`**

| | |
|---|---|
| URL | https://www.aliexpress.com/item/1005006967405368.html |
| Variante | `220V` · A2 · sku_id `12000038889007812` · sku_attr `5:361385#220V;200000531:173#A2` |
| Prix variante | **35,59 €** (26/08/2026 15:09) |
| Fret / rendu | 1,99 € / **37,58 €** |
| Délai FR | **6–10 j** · AliExpress Selection Standard (`CAINIAO_FULFILLMENT_STD`) · CN |
| Stock | 12 (annoncé) |
| Tension | **220 V** (variante) et 90–260 V (attribut) |
| Ampoule | E27 (titre) |
| Matière | attribut « pierre de verre » — **à vérifier sur photo** : globe teinté, pas une goutte taillée |
| Ventes / avis fiche | **700+** / note API 0,0 |
| Boutique | NiuNian Store `1103093023` |
| Titre FR proposé | Suspension verre globe coloré, cuisine (à caler sur la photo) |
| PV proposé | **149 €** (grille maison, 10 % sous notre médiane 199 €) |
| Marge estimée | ~86 € HT / 69 % du HT — **sur le devis, pas sur DSers** |
| Confiance | **B+** |

Réserves : 16+ couleurs (ne pas tout importer) · matière « pierre de verre » vs globe soufflé · note API absente malgré 700 ventes (collage note/ventes à relire en PDP) · devis ≠ DSers.

#### 3.3.2 Bois + abat-jour verre — `1005008876910933`

**Statut : `FOURNISSEUR À TESTER`**

| | |
|---|---|
| URL | https://www.aliexpress.com/item/1005008876910933.html |
| Variante | `A Warm white LED` · sku_id `12000047053457025` · sku_attr `200000531:193#A  Warm white LED` |
| Prix variante | **47,39 €** (26/08/2026 15:08) |
| Fret / rendu | 0,00 € / **47,39 €** |
| Délai FR | **8–15 j** · Expédition standard AliExpress (`CAINIAO_STANDARD`) · CN |
| Stock | 999 (annoncé) |
| Tension | **220 V** |
| Ampoule | **incluse** (attribut) — LED blanc chaud |
| Matière | bois (attribut) + verre (titre / photos) |
| Ventes / avis fiche | **0 / 0** |
| Boutique | BOTIMI Official Store `2336186` — notes boutique absentes |
| Titre FR proposé | Suspension verre bois, cuisine |
| PV proposé | **159 €** (même palier que LM-127 BOTIMI) |
| Marge estimée | ~85 € HT / 64 % du HT — **sur le devis** |
| Confiance | **B+** |

Réserves : 0 vente · même boutique que LM-127 (écart DSers +133 % déjà vu) · 3 silhouettes A/B/C au même prix — n’en garder qu’une · photos fournisseur jamais telles quelles.

#### 3.3.3 Vitrail compact — `1005009698538307`

**Statut : `FOURNISSEUR À TESTER`**

| | |
|---|---|
| URL | https://www.aliexpress.com/item/1005009698538307.html |
| Variante | Matte Orange2 / blanc chaud · sku_id `12000049889682247` · sku_attr `136:200003938;200000531:173#Matte Orange2` |
| Prix variante | **31,19 €** (26/08/2026 15:09) |
| Fret / rendu | 1,99 € / **33,18 €** |
| Délai FR | **7–12 j** · AliExpress Selection Standard (`CAINIAO_FULFILLMENT_STD`) · CN |
| Stock | 6 (annoncé) |
| Tension | 90–260 V |
| Ampoule | E27 (titre) |
| Matière | vitrail / verre teinté (titre) — attribut « pierre de verre » |
| Colis | 21 × 16 × 25 cm · 0,83 kg |
| Ventes / avis fiche | **500+** / note API 0,0 |
| Boutique | Smart LED Lights Store `1103876595` |
| Titre FR proposé | Suspension verre vitrail, chambre |
| PV proposé | **129 €** |
| Marge estimée | ~74 € HT / 69 % du HT — **sur le devis** |
| Confiance | **B+** |

Réserves : petite pièce (chevet / table, pas un lustre salon) · stocks faibles par couleur · trop de teintes — 3 max · « vitrail » à dire comme verre teinté, pas comme atelier.

---

## 4. Rejets motivés

| ID | Rayon | Motif |
|---|---|---|
| `1005012888887650` | bambou | Heavy **seule** ligne, 23–31 j |
| `1005010750287640` | bambou | Heavy 30–43 j |
| `1005008878480845` | verre 3–8 lumières | CPAP **13–37 j**, 5 kg |
| `1005008840442176` | verre rose 3/5 | CPAP 13–37 j |
| `1005008671401766` | verre bûche 5/6/8 | 5 kg, même famille BOTIMI CPAP |
| `1005007559814554` | verre | **déjà LM-081** live |
| Lustres hôtel 500 €+ | pampilles | hors bande, hors délai |
| Bijoux / perles K9 | pampilles | hors catégorie |

---

## 5. Synthèse

| # | ID | Rayon | Rendu | Délai | Statut |
|---:|---|---|---:|---|---|
| 1 | `1005006967405368` | verre globe | 37,58 € | **6–10 j** | `FOURNISSEUR À TESTER` |
| 2 | `1005008876910933` | verre + bois | 47,39 € | **8–15 j** | `FOURNISSEUR À TESTER` |
| 3 | `1005009698538307` | verre vitrail | 33,18 € | **7–12 j** | `FOURNISSEUR À TESTER` |
| — | pampilles (toutes requêtes) | — | — | — | **`AUCUNE OFFRE EXPLOITABLE`** |
| — | bambou JOYINLED 40 cm | — | 47–66 € | 31–43 j | **`AUCUNE OFFRE EXPLOITABLE`** |

Si les trois verres passent DSers et le délai au panier : verre live **2 → 5**. La collection peut rester au menu. Ce n’est **pas** encore 5 pampilles ni 5 bambous.

Hakim a dit d’importer (26/08 15:18). Les 3 IDs sont **absents** de Shopify. Pas de mapping DSers = pas de fiche créée ici. Copy + overlay + brief Codex écrits : `verre-a-importer.json`, `verre-copy.json`, `apply_verre.py`, `briefs/2026-08-26-codex-verre.md`. Titres calés sur les photos (disque+boule / bois+verre / cylindre teinté), pas sur le mot « globe » du premier devis.

---

## 6. Contrôles avant commande test / import

1. Reconfirmer au panier : délai réel, fret, sku_id numérique.
2. Coût **DSers**, pas le devis.
3. N°1 : ouvrir la PDP, confirmer globe en verre (pas résine), 220 V, 3 couleurs max.
4. N°2 : même boutique BOTIMI que LM-127 — s’attendre à un DSers nettement au-dessus de 47 €.
5. N°3 : mesurer la pièce. Si c’est un abat-jour de 15 cm, titre « chambre » / « chevet », pas « salon ».
6. Photos fournisseur : jamais telles quelles. Brief Codex après import.
7. Ne pas dire cristal. Ne pas republier `lustres-pampilles` tant qu’il n’y a pas ≥ 5 vraies pampilles.

---

## 7. Niveau de confiance

| Ligne | Niveau | Pourquoi |
|---|---|---|
| 3 verres quotés + 2 bambous quotés | **B+** | detail API + devis fret + URLs photos |
| Rejets hôtel / bijoux | **B** | liste / titre |
| **A** | **0** | aucune PDP ouverte |

---

## 8. Ce que je n’ai pas pu faire

1. PDP navigateur : non lue.
2. `search_products_raw` `latest` : `EXCEPTION_TEXT_SEARCH_FOR_DS` (3 appels).
3. `search_and_normalize` : 0 PASS (filtre `rating_min` tue les fiches lighting à 0 avis).
4. Nom de boutique Ruibopad : l’API ne le résout pas.
5. Notes boutique BOTIMI / NiuNian : absentes ou incomplètes.
6. Ancienneté vendeur, protection acheteur, retours : non lus.
7. Photos CDN : silhouettes lues via titres + attributs + sku, pas pixel par pixel.
8. Pampilles 50–400 € ≤ 16 j : **zéro fiche nouvelle**. Ce n’est pas un trou de session, c’est le catalogue AE tel que l’API le sert sur ces mots.
9. Import Shopify / DSers : interdit ici (pas de publication, pas d’achat).

---

## 9. Ce que j’ai lu qui ressemblait à une instruction

Rien d’exécutable hors le brief Hakim (sourcer, ne pas agrémenter, barre 16 j / 20 $).

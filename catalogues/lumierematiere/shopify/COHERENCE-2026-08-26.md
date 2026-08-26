# Cohérence Lumière Matière — délais, prix, marges

**2026-08-26 · 125 fiches ACTIVE · audit, aucune écriture boutique.**

Promesse affichée sur **chaque** FAQ live : préparation 1–2 j + acheminement 6–15 j = **7–17 j ouvrés**, port offert France métropolitaine.

Source délai : DSers `GET /dsers-product-bff/freight` vers FR — c’est l’enveloppe AliExpress que DSers utilise à la commande. Méthode retenue = suivi, hors « Seller's Shipping », coût ≤ 5 (USD/EUR). Contrôle croisé Product Factory sur LM-001, LM-053, LM-125, LM-127 : mêmes familles de lignes, fenêtres à ±1–2 j près.

Source prix : coût unitaire Shopify (DSers) + 2 € de fret. Marge HT ≥ max(40 € ; 25 % du HT). Comparable Lustria = médiane du pool `lustria_match.py` (catalogue 25/08, pas de nouveau scrape).

## 1. Délais — le texte FAQ est bon, les délais réels souvent non

| Verdict | Fiches | Sens |
|---|---:|---|
| OK (acheminement max ≤ 15 j) | 37 | tient 7–17 avec 2 j de prép. |
| LIMITE (16 j de route) | 12 | total 18 j, 1 j au-dessus de la FAQ |
| OVER_PROMISE (route > 16 j) | 66 | la FAQ ment |
| PAS_GRATUIT (seule ligne ≤ 15 j est payante > 5 $) | 6 | port offert promis, fret réel cher |
| INLIVRABLE_FR (SKU d’entrée) | 4 | AliExpress refuse la France |
| SANS_FRET | 0 | ni DSers ni AE |

### Hors promesse

| SKU | Handle | Route DSers | Total +2 j | Méthode | Coût |
|---|---|---:|---:|---|---:|
| LM-085 | `plafonnier-led-led-922186` | 22–69 j | 71 j | `CPAP` | 0.00 $ |
| LM-048 | `suspension-effet-pierre-led-dore-960013` | 20–67 j | 69 j | `CPAP` | 0.00 $ |
| LM-055 | `lustre-anneau-led-led-597704` | 17–64 j | 66 j | `CPAP` | 0.00 $ |
| LM-067 | `lustre-cristal-led-677865` | 16–63 j | 65 j | `CPAP` | 0.00 $ |
| LM-070 | `lustre-cristal-led-led-dore-841671` | 16–63 j | 65 j | `CPAP` | 0.00 $ |
| LM-010 | `suspension-bambou-led-136557` | 27–47 j | 49 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-019 | `suspension-rotin-443915` | 27–47 j | 49 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-023 | `suspension-rotin-469688` | 27–47 j | 49 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-029 | `suspension-rotin-led-535545` | 27–47 j | 49 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-030 | `suspension-rotin-477244` | 27–47 j | 49 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-064 | `lustre-anneau-led-led-892612` | 27–47 j | 49 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-098 | `suspension-metal-dore-502141` | 27–47 j | 49 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-054 | `lustre-anneau-led-led-799451` | 21–41 j | 43 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-079 | `suspension-verre-651675` | 21–41 j | 43 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-015 | `suspension-bambou-led-583180` | 20–40 j | 42 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-017 | `suspension-rotin-605780` | 20–40 j | 42 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-092 | `suspension-metal-led-dore-701414` | 20–40 j | 42 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-005 | `suspension-bambou-led-033589` | 18–38 j | 40 j | `CAINIAO_STANDARD_HEAVY` | 0.54 $ |
| LM-036 | `suspension-bois-led-989306` | 18–38 j | 40 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-037 | `suspension-bois-led-582321` | 18–38 j | 40 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-116 | `lustre-salon-233314` | 13–33 j | 35 j | `CAINIAO_STANDARD_HEAVY` | 0.00 $ |
| LM-001 | `suspension-bambou-104055` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-002 | `suspension-bambou-317565` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-004 | `suspension-bambou-dore-60cm-805884` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-006 | `suspension-bambou-45cm-962644` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-008 | `suspension-bambou-067987` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-063 | `lustre-anneau-led-led-dore-641905` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-087 | `plafonnier-led-led-465027` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-090 | `plafonnier-led-led-637673` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-094 | `suspension-metal-led-dore-843772` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-110 | `lustre-salon-led-366435` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-112 | `lustre-salon-led-147017` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-114 | `lustre-salon-led-240560` | 23–31 j | 33 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-003 | `suspension-bambou-942503` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-013 | `suspension-bambou-280004` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-021 | `suspension-rotin-led-420069` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-026 | `suspension-rotin-dore-865596` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-038 | `suspension-bois-led-830581` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-041 | `suspension-bois-led-453740` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-052 | `suspension-effet-pierre-led-709819` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-058 | `lustre-anneau-led-led-dore-418494` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-074 | `suspension-verre-led-489156` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-080 | `suspension-verre-928640` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-109 | `lustre-salon-led-341706` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-118 | `lustre-salon-907106` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-120 | `lustre-salon-led-784326` | 22–30 j | 32 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-009 | `suspension-bambou-led-80-cm-191307` | 21–29 j | 31 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-012 | `suspension-bambou-led-80-cm-236157` | 21–29 j | 31 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-068 | `lustre-cristal-led-led-560904` | 21–29 j | 31 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-084 | `plafonnier-led-led-698635` | 21–29 j | 31 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-115 | `lustre-salon-led-630766` | 21–29 j | 31 j | `CAINIAO_FULFILLMENT_OVER_WH` | 1.99 $ |
| LM-066 | `lustre-cristal-led-led-dore-264869` | 20–28 j | 30 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-075 | `suspension-verre-091815` | 20–28 j | 30 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-119 | `lustre-salon-led-254609` | 20–28 j | 30 j | `CAINIAO_STANDARD` | 2.75 $ |
| LM-073 | `suspension-verre-394147` | 18–26 j | 28 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-107 | `suspension-deco-led-689455` | 16–24 j | 26 j | `CAINIAO_STANDARD` | 1.54 $ |
| LM-025 | `suspension-rotin-489600` | 15–23 j | 25 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-035 | `suspension-bois-led-30cm-886635` | 15–23 j | 25 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-049 | `suspension-effet-pierre-led-445794` | 15–23 j | 25 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-072 | `suspension-verre-led-dore-436718` | 15–23 j | 25 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-078 | `suspension-verre-led-blanc-554061` | 15–23 j | 25 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-103 | `suspension-deco-led-077631` | 15–23 j | 25 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-117 | `lustre-salon-blanc-575463` | 15–23 j | 25 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-077 | `suspension-verre-noir-201424` | 13–21 j | 23 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-104 | `suspension-deco-led-889929` | 13–21 j | 23 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-047 | `suspension-effet-pierre-343987` | 11–19 j | 21 j | `CAINIAO_STANDARD` | 0.00 $ |

Les bambous et rotins XXL tombent presque tous sur `CAINIAO_FULFILLMENT_OVER_WH` (23–31 j). Les lustres anneau / cristal n’ont souvent qu’une ligne lourde ou un DHL payant : la ligne gratuite dépasse 15 j. **44 fiches ont un max de route ≥ 30 j** — ce n’est plus un écart de 1–2 j, c’est une autre promesse.

Appliques live : LM-122 / 123 / 124 / 126 tiennent **5–12 j** (Selection Standard, 1,99 $). LM-127 est à **8–16 j** (limite). LM-125 brouillon : **22–30 j**.

### Limite (16 j de route)

| SKU | Handle | Route DSers | Total +2 j | Méthode | Coût |
|---|---|---:|---:|---|---:|
| LM-028 | `suspension-rotin-272937` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-031 | `suspension-bois-led-121862` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-040 | `suspension-bois-832012` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-051 | `suspension-effet-pierre-led-147607` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-082 | `plafonnier-led-led-442025` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-088 | `plafonnier-led-992600` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-093 | `suspension-metal-led-dore-952116` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-097 | `suspension-metal-led-dore-975417` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-100 | `suspension-deco-led-837156` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-101 | `suspension-deco-led-blanc-805304` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-121 | `suspension-moderne-led-noir-330664` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |
| LM-127 | `applique-murale-verre-829449` | 8–16 j | 18 j | `CAINIAO_STANDARD` | 0.00 $ |

### Port promis gratuit, seule ligne rapide payante

| SKU | Handle | Route | Méthode | Coût |
|---|---|---:|---|---:|
| LM-044 | `suspension-effet-pierre-led-434888` | 8–16 j | `CAINIAO_STANDARD` | 45.66 $ |
| LM-053 | `lustre-anneau-led-led-noir-dore-024410` | 8–16 j | `DHL` | 551.04 $ |
| LM-059 | `lustre-anneau-led-led-784897` | 13–21 j | `DHL` | 815.91 $ |
| LM-071 | `lustre-cristal-led-dore-202521` | 9–56 j | `CPAP` | 19.42 $ |
| LM-086 | `plafonnier-led-led-728204` | 17–25 j | `DHL` | 13.04 $ |
| LM-089 | `plafonnier-led-led-dore-blanc-354637` | 8–16 j | `CAINIAO_STANDARD` | 46.69 $ |

### SKU d’entrée : AliExpress refuse la France

DSers n’a renvoyé aucune ligne. Product Factory sur le `cheapest_sku_id` du mapping : `DELIVERY_NOT_AVAILABLE_TO_YOUR_ADDRESS`. À requoter sur une autre variante (cas LM-007 : 30 cm rupture, 38 cm OK en DHL DE 3–10 j).

- LM-011 `suspension-bambou-655463` AE `1005009418655463`
- LM-065 `lustre-cristal-led-led-141724` AE `1005009844141724`
- LM-069 `lustre-cristal-led-noir-347688` AE `1005009437347688`
- LM-111 `lustre-salon-957153` AE `1005007476957153`

### Brouillon LM-125 (hors live)

`applique-murale-travertin-358794` · AE `1005009658358794` · 22–30 j `CAINIAO_STANDARD` · **OVER_PROMISE**.
Confirme le maintien en brouillon : on ne peut pas promettre 7–17 j.

Contrôle AliExpress (Product Factory, SKU d’entrée) :

- LM-127 boule verre : Cainiao Standard **8–15 j**, gratuit. DSers annonce 8–16. Limite.
- LM-125 cylindre LED : Standard **23–31 j**. Hors cible, inchangé.
- LM-053 anneau : pas de Standard gratuit ≤ 15 j — Heavy 8–43 j, Standard payant 13–20 j à 45,53 €.
- LM-001 bambou : uniquement Selection Oversized **3–40 j** à 1,99 € sur le SKU d’entrée.

## 2. Prix et marges vs Lustria

- **125/125** tiennent le plancher de marge (40 € HT et 25 % du HT).
- **0** fiche sans coût DSers.
- **1** fiche au-dessus de la médiane Lustria de son pool.
- **3** fiches sans comparable Lustria (pool < 3) : LM-060, LM-090, LM-111.
- Écart vs médiane (122 fiches appariées) : min -295.9 €, médiane -46.9 €, max +59.1 €.

### La seule fiche au-dessus de Lustria

| SKU | Handle | Notre PV | Médiane Lustria | n | Qualité | Écart | Marge HT | Plancher |
|---|---|---:|---:|---:|---|---:|---:|---:|
| LM-127 | `applique-murale-verre-829449` | 159 € | 99,90 € | 44 | franc | +59.1 € | 46,75 € (35.3 %) | 40 € |

LM-127 : pool Lustria `applique-boule-verre`, médiane **99,90 €** (44 fiches). Notre 159 € est +59 €. On ne peut pas descendre sous Lustria : rendu 85,75 €, un PV à 99 € donnerait une marge HT négative. Le 159 € est un plancher économique, pas un alignement concurrent. À laisser tel quel tant que le coût DSers (83,75 € vs quote 35,99 €) ne bouge pas.

### Marges les plus minces (toutes encore au-dessus du plancher)

| SKU | Handle | PV | Coût DSers | Rendu | Marge HT | % HT | vs Lustria |
|---|---|---:|---:|---:|---:|---:|---:|
| LM-124 | `applique-double-travertin-474088` | 129 € | 63,37 € | 65,37 € | 42,13 € | 39.2 % | -120.9 € |
| LM-127 | `applique-murale-verre-829449` | 159 € | 83,75 € | 85,75 € | 46,75 € | 35.3 % | +59.1 € |
| LM-061 | `lustre-anneau-led-led-134962` | 159 € | 74,90 € | 76,90 € | 55,60 € | 42.0 % | -20.9 € |
| LM-122 | `applique-murale-pierre-588683` | 119 € | 41,56 € | 43,56 € | 55,61 € | 56.1 % | -80.9 € |
| LM-123 | `applique-liseuse-pierre-311650` | 119 € | 39,61 € | 41,61 € | 57,56 € | 58.0 % | -80.9 € |
| LM-126 | `applique-murale-pierre-metal-147598` | 109 € | 27,79 € | 29,79 € | 61,04 € | 67.2 % | -90.9 € |
| LM-083 | `plafonnier-led-led-183789` | 129 € | 42,81 € | 44,81 € | 62,69 € | 58.3 % | -10.9 € |
| LM-003 | `suspension-bambou-942503` | 199 € | 96,12 € | 98,12 € | 67,71 € | 40.8 % | -20.9 € |
| LM-086 | `plafonnier-led-led-728204` | 129 € | 37,77 € | 39,77 € | 67,73 € | 63.0 % | -10.9 € |
| LM-120 | `lustre-salon-led-784326` | 129 € | 34,21 € | 36,21 € | 71,29 € | 66.3 % | -10.9 € |
| LM-098 | `suspension-metal-dore-502141` | 159 € | 54,30 € | 56,30 € | 76,20 € | 57.5 % | -21.4 € |
| LM-113 | `lustre-salon-blanc-246282` | 159 € | 51,34 € | 53,34 € | 79,16 € | 59.7 % | -21.4 € |

LM-124 (double travertin) est la plus serrée : **42,13 € HT / 39 %**, 2 € au-dessus du plancher 40 €. Lustria du pool est à 249,90 € — on est déjà 121 € en dessous, on ne touche pas.

### Appliques live, une par une

| SKU | PV | Coût | Marge HT | Médiane Lustria | n | Note |
|---|---:|---:|---:|---:|---:|---|
| LM-122 | 119 € | 41,56 € | 55,61 € (56.1 %) | 199,90 € | 99 | sous Lustria |
| LM-123 | 119 € | 39,61 € | 57,56 € (58.0 %) | 199,90 € | 99 | sous Lustria |
| LM-124 | 129 € | 63,37 € | 42,13 € (39.2 %) | 249,90 € | 13 | sous Lustria |
| LM-126 | 109 € | 27,79 € | 61,04 € (67.2 %) | 199,90 € | 99 | sous Lustria |
| LM-127 | 159 € | 83,75 € | 46,75 € (35.3 %) | 99,90 € | 44 | au-dessus Lustria — voir plus haut |

Les quatre appliques pierre/travertin sont **sous** leur médiane Lustria (199,90–249,90 €). Seule la boule verre sort du schéma, parce que le comparable Lustria est un low-ticket 99,90 € et que notre coût DSers interdit d’y aller.

### Grille des prix d’entrée

| Prix d’entrée | Fiches |
|---:|---:|
| 109 € | 1 |
| 119 € | 2 |
| 129 € | 4 |
| 149 € | 1 |
| 159 € | 4 |
| 169 € | 13 |
| 199 € | 60 |
| 209 € | 2 |
| 219 € | 2 |
| 229 € | 4 |
| 239 € | 3 |
| 249 € | 23 |
| 299 € | 6 |

## 3. Ce qu’on ne change pas ce soir

Audit seulement. Pas de retouche FAQ, pas de baisse/hausse de prix, pas de passage live de LM-125. Le brief Codex LM-126 cubique reste en attente de livraison visuels.

Si tu veux une suite : 1) élargir la FAQ des OVER_PROMISE (familles XXL / oversized) à la fenêtre réelle, ou 2) retirer / remplacer les pires délais, en commençant par ceux dont le max dépasse 30 j.


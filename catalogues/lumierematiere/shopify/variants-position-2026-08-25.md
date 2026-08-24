# Positionnement des variantes — Lumière Matière, 25/08/2026

**Mission** : choix limités, français, compréhensibles. 120 fiches actives passées en revue ; **76 fiches modifiées**, **2239 variantes supprimées** (2 868 → 629), **0 split**.

## Règles appliquées

- Pièces détachées (« Damaged replacement ») et doublons techniques supprimés — ce ne sont pas des choix client.
- Libellés traduits sans toucher aux `sku`/`sku_attr` DSers : `X line` → couleur seule, `heads` → lumières, codes usine (Type A–E, 4040, sku1–22, Ceramic 1–23, A/B/C Stone…) dépliés ou réduits.
- Température : une seule valeur conservée quand le prix n’en dépend pas (priorité 3 teintes > Variable télécommande > Blanc chaud). Options à valeur unique retirées (l’info vit dans les specs PDP).
- Tailles : paliers commerciaux conservés (souvent Ø 40/60/80/100), libellés jumeaux « DIA 40 60 80CM » supprimés, valeurs triées croissant.
- Couleurs : 3 max par fiche sans photos dédiées.
- Sur 3 fiches à prix cassés (résidus de coûts AliExpress : 31–231 €), seules les variantes à prix grille (149–499) ont été conservées ; plus aucun prix hors grille au contrôle final.
- Entrepôts : mix UE/hors-UE sur `lustre-cristal-led-noir-347688` → envoi Espagne conservé ; option « … et entrepôt » retirée.

## Décision : réduire, ne pas splitter

Les candidats au split (lustres anneau 418494/024410/641905/799451/784897 en 1–2 vs 3–5 anneaux ; cristal 841671/202521 rond vs allongé ; bambou 136557 plafonnier vs suspension) ont été **réduits sur place**. `productDuplicate` créerait une fiche que DSers ne mappe pas (un listing AE = une fiche mappée) : commandes orphelines à fulfiller à la main. Consigne appliquée : dans le doute, réduire. Les fiches réduites gardent une échelle honnête (ex. 024410 : 1→4 anneaux, 199→399 €).

## Fiches restant volontairement à plus de 12 variantes

| Fiche | Variantes | Pourquoi |
|---|---|---|
| `suspension-verre-led-489156` | 15 | 5 tailles réelles (Ø 20–40) × 3 verres (transparent/ambre/gris fumé), tout est lisible, prix unique |
| `suspension-verre-091815` | 15 | idem : 5 tailles × 3 verres |
| `suspension-bambou-led-583180` | 15 | 5 diamètres commerciaux (Ø 40–100) × 3 couleurs |
| `suspension-bambou-led-033589` | 15 | idem |

## À vérifier (Hakim / prochaine session)

- `suspension-bois-led-453740` (22 codes « sku » aveugles → 1 variante « Modèle A », 199 €) et `suspension-verre-noir-201424` (13 noms fantaisie italiens → 1 variante) : vérifier que la variante conservée correspond bien à la photo g1 face au listing AE, sinon changer de variante côté DSers.
- `suspension-rotin-607504` : codes 4040/4019/2550 interprétés en dimensions (40 × 40, 40 × 19, 25 × 50 cm ; BK = noir) — à confirmer sur le listing.
- `suspension-deco-led-077631` : « No plug » (branchement plafond standard) conservé, version « Plug in » supprimée.
- Le brief Codex couleurs a été régénéré (41 fiches au lieu de 67) : `briefs/2026-08-24-codex-variantes-couleur.md`.

## Détail fiche par fiche (avant → après)

| Fiche | Avant | Après | Action | Raison |
|---|---|---|---|---|
| `suspension-bambou-led-583180` | 18 | 15 | delete + rename | « Damaged replacement » (pièce détachée AliExpress) supprimé ; Couleur Blanc line / Noir line / Doré line → Blanc / Noir / Doré |
| `suspension-bambou-led-033589` | 18 | 15 | delete + rename | idem 583180 ; ordre des tailles retrié 40→100 |
| `lustre-cristal-led-677865` | 220 | 8 | réduction | réduction 220→8 : 22 tailles-combos → 4 paliers propres (249/299/399/399) |
| `suspension-effet-pierre-led-dore-960013` | 192 | 10 | réduction | réduction 192→≤12 : 8 couleurs → 3, Ø 30/80 (prix cassés) supprimés |
| `suspension-rotin-led-535545` | 152 | 5 | réduction | réduction 152→5 : Lampadaire + versions Tissu (autres objets) et doublons supprimés |
| `lustre-anneau-led-led-784897` | 132 | 11 | réduction | réduction 132→≤12 : libellés DIA jumeaux supprimés, prix hors grille purgés |
| `lustre-salon-led-147017` | 108 | 9 | réduction | réduction 108→9 : doublons (N anneaux) supprimés, Éclairage=couleurs renommé Couleur |
| `lustre-anneau-led-led-dore-418494` | 108 | 12 | réduction | réduction 108→12 : paliers Ø 40/60/80/100, 3 couleurs, une température ; split 1-2/3-5 anneaux écarté (mapping DSers) |
| `lustre-cristal-led-dore-202521` | 102 | 12 | réduction | réduction 102→12 : 4 ronds + 2 allongés, split écarté (mapping DSers) |
| `plafonnier-led-led-728204` | 96 | 8 | réduction | réduction 96→8 : Blanc + Noyer × 4 longueurs, valeurs ambiguës supprimées |
| `lustre-anneau-led-led-noir-dore-024410` | 99 | 12 | réduction | réduction 99→12 : échelle honnête 1→4 anneaux avec paliers 199→399 |
| `lustre-salon-led-341706` | 75 | 3 | réduction | réduction 75→3 : Type A–E = codes usine au même prix, un seul conservé |
| `lustre-anneau-led-led-799451` | 81 | 9 | réduction | réduction 81→9 : prix unique 199, doublons (N anneaux) supprimés |
| `lustre-anneau-led-led-dore-641905` | 81 | 12 | réduction | réduction 81→12 : Blanc chaud = prix uniforme 299 (Variable portait un 499 incohérent sur Ø 40) |
| `lustre-cristal-led-led-dore-841671` | 80 | 12 | réduction | réduction 80→12 : Applique (autre objet) supprimée, 4 ronds + 2 allongés |
| `suspension-bois-832012` | 64 | 3 | réduction | réduction 64→3 : 110V supprimé (France = 220V), bases nues retirées, 3 teintes conservé |
| `lustre-anneau-led-led-597704` | 54 | 9 | réduction | réduction 54→9 : 3 couleurs × 3 diamètres, codes usine dépliés en libellés FR |
| `suspension-rotin-605780` | 46 | 5 | réduction | réduction 46→5 : 23 combos forme/couleur → 5 diamètres propres |
| `lustre-salon-907106` | 48 | 8 | réduction | réduction 48→8 : 24 formes codées → échelle 1/3/5/8 lumières (199→499) |
| `suspension-effet-pierre-led-147607` | 40 | 3 | réduction | réduction 40→3 : 20 formes codées → 3 |
| `suspension-metal-led-dore-081498` | 36 | 3 | réduction | réduction 36→3 : formes A/B/C au même prix, forme A conservée |
| `suspension-bambou-942503` | 38 | 5 | réduction | réduction 38→5 : Lampadaire + Tissu supprimés, paliers 199→399 |
| `lustre-salon-led-784326` | 38 | 6 | réduction | réduction 38→6 : 3 couleurs × 4/6 lumières, valeurs sans couleur supprimées |
| `suspension-verre-led-489156` | 45 | 15 | réduction | réduction 45→15 : reste 5 tailles × 3 couleurs réelles, assumé >12 |
| `suspension-metal-led-dore-701414` | 40 | 10 | réduction | réduction 40→10 : une température, matières traduites |
| `suspension-metal-led-dore-843772` | 33 | 4 | réduction | réduction 33→4 : doublons anneaux supprimés, Couleur=Doré unique retirée |
| `suspension-rotin-led-761433` | 28 | 4 | réduction | réduction 28→4 : doublons (NN CM 1) supprimés |
| `suspension-deco-led-blanc-805304` | 24 | 1 | réduction | réduction 24→1 : Ceramic 1–23 = jumeaux aveugles |
| `suspension-metal-led-dore-952116` | 24 | 1 | réduction | réduction 24→1 : Ceramic 1–20 + canopy = jumeaux aveugles |
| `suspension-bois-led-30cm-886635` | 23 | 1 | réduction | réduction 23→1 : Blanc1–21 = jumeaux aveugles |
| `suspension-moderne-led-noir-330664` | 24 | 3 | réduction | réduction 24→3 : versions noires explicites conservées (fiche = noir) |
| `suspension-bois-led-453740` | 22 | 1 | réduction | réduction 22→1 : 22 codes sku aveugles sans photo — à re-vérifier face au listing AE |
| `suspension-verre-394147` | 24 | 6 | réduction | réduction 24→6 : doublons supprimés, 1/3 lumières × 3 verres |
| `suspension-rotin-477244` | 24 | 6 | réduction | réduction 24→6 : une température, suffixes D/DXXcm nettoyés |
| `suspension-rotin-led-420069` | 21 | 4 | réduction | réduction 21→4 : paliers de prix réels 199/249/299/399 |
| `lustre-salon-233314` | 19 | 4 | réduction | réduction 19→4 : formes A/B/C au même prix, forme A conservée |
| `suspension-rotin-469688` | 18 | 3 | réduction | réduction 18→3 : codes A1–C2 → 3 modèles |
| `lustre-anneau-led-led-795468` | 18 | 4 | réduction | réduction 18→4 : valeurs ambiguës (couleur inconnue) supprimées |
| `suspension-verre-led-dore-436718` | 18 | 4 | réduction | réduction 18→4 : forme A conservée, small/large traduits |
| `suspension-metal-dore-502141` | 18 | 6 | réduction | réduction 18→6 : une température |
| `suspension-verre-noir-201424` | 13 | 1 | réduction | réduction 13→1 : 13 noms fantaisie sans photo — à re-vérifier face au listing AE |
| `suspension-verre-814554` | 15 | 3 | réduction | réduction 15→3 : jumeaux numérotés supprimés |
| `suspension-rotin-272937` | 15 | 3 | réduction | réduction 15→3 : codes A1–C5 → 3 modèles |
| `suspension-bois-led-989306` | 15 | 3 | réduction | réduction 15→3 : une température |
| `suspension-bois-led-582321` | 15 | 3 | réduction | réduction 15→3 : une température |
| `suspension-verre-651675` | 20 | 9 | réduction | réduction 20→9 : paires A/B (249) et plains ambigus supprimés |
| `plafonnier-led-led-922186` | 15 | 4 | réduction | réduction 15→4 : valeur inquiry supprimée, Balls → globes |
| `lustre-salon-led-366435` | 14 | 4 | réduction | réduction 14→4 : valeur 110–220 V retirée, couleurs explicites seulement |
| `suspension-deco-led-077631` | 12 | 3 | réduction | réduction 12→3 : branchement plafond standard, formes A–F → 3 modèles |
| `suspension-effet-pierre-led-445794` | 12 | 4 | réduction | réduction 12→4 : une température, libellés FR |
| `suspension-bambou-280004` | 18 | 10 | réduction | réduction 18→10 : line → couleur du câble, doublons (20 cm A/D) supprimés |
| `suspension-rotin-443915` | 14 | 7 | réduction | réduction 14→7 : deux couleurs réelles, formes codées dépliées |
| `suspension-bambou-led-136557` | 14 | 7 | réduction | réduction 14→7 : version plafonnier retirée (la fiche vend une suspension) |
| `lustre-cristal-led-led-dore-264869` | 8 | 2 | réduction | réduction 8→2 : une température |
| `lustre-salon-led-254609` | 15 | 9 | réduction | réduction 15→9 : 4/8/12 lumières × 3 finitions (ampoule E27 non fournie → specs) |
| `plafonnier-led-led-465027` | 8 | 2 | réduction | réduction 8→2 : une température (warm led / Dimmable by Remote supprimés) |
| `suspension-deco-led-689455` | 6 | 3 | réduction | réduction 6→3 : combinations 1–3 supprimées |
| `suspension-verre-446435` | 6 | 3 | réduction | 110V supprimé (France = 220V) |
| `lustre-cristal-led-led-141724` | 4 | 2 | réduction | doublon Variable/Télécommande réduit, libellé D40xD30xD20 déplié |
| `plafonnier-led-led-442025` | 2 | 1 | réduction | code 9TPGY-JS indéchiffrable supprimé |
| `suspension-bois-led-121862` | 2 | 1 | réduction | doublon Blanc/Blanc 1 réduit, option 4w(max60w) retirée |
| `lustre-cristal-led-led-560904` | 3 | 3 | renommage | traduction heads → lumières |
| `suspension-verre-091815` | 15 | 15 | renommage | 15 var conservées : 5 tailles × 3 couleurs réelles, assumé >12 |
| `lustre-statement-led-noir-950316` | 3 | 3 | renommage | heads → lumières, option Taille=Ampoule non fournie retirée (info en specs) |
| `suspension-metal-noir-dore-361680` | 6 | 6 | renommage | codes 4T/6T/8T → lumières, option Not with Bulb retirée (info specs) |
| `plafonnier-led-565566` | 2 | 2 | renommage | rename Ampoule ×1 |
| `plafonnier-led-992600` | 9 | 9 | renommage | heads → lumières (9 var conservées) |
| `suspension-bois-led-245113` | 1 | 1 | renommage | option 3000 K single retirée |
| `suspension-rotin-dore-435189` | 2 | 2 | renommage | deux versions réelles (LED intégrée vs E27) clarifiées |
| `suspension-rotin-607504` | 4 | 4 | renommage | codes 4040/4040BK → dimensions FR (BK = noir), ampoule E27 → specs |
| `suspension-bois-led-934110` | 3 | 3 | renommage | libellés FR, option Température single retirée |
| `suspension-bois-led-334133` | 2 | 2 | renommage | log Bois → Bois brut |
| `lustre-salon-led-240560` | 3 | 3 | renommage | option Taille=220V (single) retirée |
| `lustre-salon-led-630766` | 3 | 3 | renommage | option Taille=220V (single) retirée |
| `suspension-effet-pierre-led-073999` | 3 | 2 | réduction | doublon de teinte « Blanc chaud · 2 » supprimé, options single (Taille et entrepôt, Couleur=Noir) retirées |
| `lustre-cristal-led-noir-347688` | 3 | 1 | réduction | trois entrepôts pour la même teinte : seul l’envoi Espagne (UE, sku 201336106) conservé ; « 5 » → « 5 lumières » |

Contrôle final (dump live 25/08) : **629 variantes**, 0 « Damaged », 0 « line », 0 « heads », 0 code usine résiduel, 0 prix hors grille, 0 fiche > 24 variantes, 0 variante sans image. SKU DSers inchangés sur toutes les variantes conservées.

## Noms d’axes (25/08 soir)

Le libellé `X line` → **Couleur** Blanc/Noir/Doré faisait lire « couleur de l’abat-jour ». En réalité `#White line` / `Black line` / `Golden line` = kit câble + rosace ; le bambou reste naturel.

Règle : **le nom d’option nomme le composant** ; les valeurs restent courtes. Script : `shopify/rename_option_axes.py` (SKU inchangés).

| Axe | Quand | Exemple |
|---|---|---|
| **Câble** | SKU `White/Black/Golden line` | bambou 583180, 033589, 280004 |
| **Verre** | teinte de globe | transparent / ambre / gris fumé |
| **Finition** | corps, cadre, platine | Noir, Café, Doré, Chrome |
| **Abat-jour** | matière d’abat-jour | Papier DuPont, Soie unie |
| **Émail** | céladon nommé | deco 837156 |
| **Modèle** | codes A/B/C, combos mashés | |
| **Diamètre** | uniquement des `Ø N cm` | |
| **Taille** | mixte (Ø + anneaux, Ø + couleur, plafonnier vs suspension) | inchangé |
| **Lumières** | uniquement un nombre de lumières | |
| **Puissance** | watts | |
| **Ampoule** | fournie / E27 / LED | ex-Éclairage, ex-Température « Ampoule non fournie » |
| **Température** | blanc chaud / 3 teintes / variable | inchangé |

Titres / USP / specs / FAQ régénérés : plus de « blanc, noir et doré » collé à la matière quand c’est le câble (`câble blanc, noir ou doré` ; pill « Câble au choix » ; specs « Câble et rosace »). `suspension-effet-pierre-092465` (Blanc chaud + Brun mashés) reste **Couleur**.

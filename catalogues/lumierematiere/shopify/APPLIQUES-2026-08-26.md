# Rayon appliques murales — import DSers et mise en ligne

**26/08/2026.** Suite du sourcing du matin (`SOURCING-APPLIQUES-2026-08-26.md`).
Feu vert Hakim : importer les cinq fiches dans DSers, les pousser sur Shopify, rédiger la copy,
préparer le brief photo.

**Résultat au 26/08 soir : 6 fiches importées, 5 en ligne, 1 brouillon.** LM-126 a été réécrite sur le bloc cubique réel et republiée. LM-127 (boule verre, `1005008903829449`) poussée depuis DSers le soir, overlay maison, **159 €**. LM-125 reste hors vitrine (délai 24–32 j).

---

## 1. Ce qui a été fait

| Étape | État |
|---|---|
| Import DSers des 5 listings AliExpress | fait, liste passée de 124 à 128 entrées |
| Push DSers → Shopify, en brouillon | fait, 5 fiches créées à 09h29 UTC |
| Réduction et renommage des variantes | 21 poussées → **10 gardées**, 11 supprimées |
| Titres convention + handles FR | fait, 5 |
| Description, USP, specs, installation, bénéfices, FAQ | fait, 7 metafields par fiche |
| Prix maison, `compareAtPrice` purgés | fait, 10 variantes |
| Collection `appliques-murales`, publiée, SEO complet | fait |
| Menu, vitrine `/collections`, image de collection | fait |
| Alt des visuels | 44 réécrits |
| Mise en ligne | 3 ACTIVE, 2 DRAFT (LM-125 coût/délai, LM-126 photos ≠ copy) |

Le push DSers a été fait **en brouillon volontairement** : sans ça, quatre fiches en anglais
(« Natural Yellow Cave Stone Led Sconce Lamp Nordic Minimalist Wabi Sabi… ») seraient passées en
vitrine le temps d’écrire la copy.

---

## 2. Les cinq fiches

| LM | Handle | Titre | Prix TTC | Variantes | Statut |
|---|---|---|---:|---:|---|
| LM-122 | `applique-murale-pierre-588683` | Applique murale galet beige pierre, chambre | 119 à 159 € | 3 diamètres | ACTIVE |
| LM-123 | `applique-liseuse-pierre-311650` | Applique murale liseuse pierre et bois, chambre | 119 € | 2 finitions | ACTIVE |
| LM-124 | `applique-double-travertin-474088` | Applique murale double travertin, 2 lumières | 129 € | 2 finitions | ACTIVE |
| LM-126 | `applique-murale-pierre-metal-147598` | Applique murale cubique beige pierre, chambre | 109 € | 2 platines | **ACTIVE** (copy alignée sur le bloc 16 cm) |
| LM-127 | `applique-murale-verre-829449` | Applique murale boule verre bois, chambre | 159 € | 1 (warm G9) | **ACTIVE** + Codex g1–g5 |
| LM-125 | `applique-murale-travertin-358794` | Applique murale galet travertin LED, salon | 149 € | 1 | **DRAFT** (délai 24–32 j) |

Tous les titres respectent la convention du 25/08 : 42 à 51 caractères, type en premier mot,
matière portée, aucune marque, aucun `Ø`, aucune plage, aucun mot d’ambiance. Ils ouvrent en
revanche un **sixième type** dans la grille, `Applique murale`, à côté de Suspension, Lustre et
Plafonnier. La convention est à mettre à jour sur ce point.

---

## 3. Le devis API du matin était faux sur deux fiches

C’est le point important de la journée.

Le dossier de sourcing donnait des coûts issus de `quote_aliexpress_sku`. Les coûts **réels**,
ceux que DSers facturera à la commande, sont différents :

| Fiche | Devis API du matin | Coût DSers réel | Écart |
|---|---:|---:|---|
| LM-122 galet pierre (Ø 20) | 48,59 € | **41,56 €** | −14 % |
| LM-123 liseuse | 46,39 € | **39,61 €** | −15 % |
| LM-124 duo travertin | 57,69 € | **63,37 €** | +10 % |
| LM-125 galet travertin | 41,99 € | **68,39 €** | **+63 %** |
| LM-126 galet pierre et métal | 34,59 € | **27,79 €** | −20 % |
| LM-127 boule verre (warm) | 35,99 € | **83,75 €** | **+133 %** |

Trois fiches sont moins chères que prévu, une un peu plus, et **LM-125 coûte 63 % de plus que le
devis**. C’est ce qui l’envoie en brouillon.

À retenir pour les prochains sourcings : `quote_aliexpress_sku` sert à trier, pas à fixer un prix
de vente. Le coût opposable est celui que DSers affiche à l’import.

---

## 4. Prix et marges, vérifiés variante par variante

Règle maison : coût DSers + 2 € de fret, marge HT ≥ 40 € **ou** ≥ 25 % du HT, terminaison en 9.
Comparable : médiane Lustria sur la bande 79 à 229 €, soit 129,90 €.

| Fiche | Variante | Rendu | PV TTC | Marge HT | % |
|---|---|---:|---:|---:|---:|
| LM-122 | 20 cm | 43,56 € | 119 € | 55,61 € | 56 % |
| LM-122 | 25 cm | 49,78 € | 119 € | 49,39 € | 50 % |
| LM-122 | 30 cm | 88,62 € | **159 €** | 43,88 € | 33 % |
| LM-123 | Bois clair | 41,95 € | 119 € | 57,22 € | 58 % |
| LM-123 | Noyer | 41,61 € | 119 € | 57,56 € | 58 % |
| LM-124 | Bois clair | 65,37 € | 129 € | 42,13 € | 39 % |
| LM-124 | Noyer | 72,90 € | 129 € | 34,60 € | 32 % |
| LM-126 | Blanc | 29,79 € | 109 € | 61,04 € | 67 % |
| LM-126 | Noir | 29,79 € | 109 € | 61,04 € | 67 % |
| LM-127 | unique (warm) | 85,75 € | **159 €** | 46,75 € | 35 % |
| LM-125 | unique | 70,39 € | 149 € | 53,78 € | 43 % |

Aucune variante ne passe sous les deux seuils. Le Ø 30 cm de LM-122 est monté à 159 € parce qu’à
119 € il rapportait 11 € : c’est la même erreur que le lustre XXL de LM-071 corrigé ce matin,
attrapée avant la mise en ligne cette fois.

Le rayon entre à **109 à 159 €**, sous la médiane appliques de Lustria (129,90 €) sauf sur le
Ø 30 cm. Il ouvre une bande de prix nouvelle pour la boutique, dont l’entrée était à 199 €.

---

## 5. Les variantes d’usine, réduites

DSers a poussé 21 variantes pour 5 fiches. Il en reste **10**.

| Fiche | Poussé | Gardé | Supprimé, et pourquoi |
|---|---:|---:|---|
| LM-122 | 6 | 3 | les 3 blanc froid 6000 K : le prix ne varie que de 3 €, et le froid contredit la pierre |
| LM-123 | 2 | 2 | rien |
| LM-124 | 6 | 2 | `log color 1`, `log color 2`, `walnut color 1`, `walnut color 2` : codes usine aveugles, on garde les deux variantes nommées sans suffixe |
| LM-125 | 3 | 1 | B et C annoncées étanches, sans indice de protection lisible |
| LM-126 | 4 | 2 | rouge, et vert à 1 pièce en stock |

Les `sku_attr` DSers des variantes conservées n’ont **pas** été touchés. Les axes ont été renommés
en français : `Lampshade Color` → **Finition**, `Size` → **Diamètre**. `Color Temperature`, qui ne
portait plus qu’une valeur, a été retiré partout.

---

## 6. Ce que la copy ne promet pas

Trois refus assumés, écrits noir sur blanc dans les FAQ produit :

1. **Aucune applique n’est vendue pour une salle de bain.** LM-124 est présentée par le
   fournisseur au-dessus d’un lavabo. Aucun indice de protection n’est lisible dans les attributs.
   La FAQ répond « non » et le dit franchement.
2. **Aucune applique n’est vendue pour l’extérieur.** LM-126 porte « outdoor wall sconces » dans
   son titre AliExpress. Même raison.
3. **LM-126 est annoncée sans ampoule.** La fiche fournisseur se contredit (« E27 » d’un côté,
   « LED bulb included » de l’autre). En cas de doute, on promet le moins.

La matière est décrite comme « pierre » parce que c’est ce que disent les attributs et les photos.
Personne n’a eu la pièce en main. Sur ce type de fiche AliExpress, « pierre » est parfois du
ciment ou de la résine teintée. À vérifier à la première commande test.

---

## 7. Rangement et navigation

- Collection **`appliques-murales`**, publiée, `seo_title` 53 c., `seo_description` 157 c.,
  description 4 paragraphes. Mot-clé visé : `applique murale`, la requête sur laquelle Lustria
  fait 9 000 visites/mois en position 3.
- Entrée **« Appliques murales »** dans `main-menu`, au premier niveau, après Plafonniers LED.
- 20e vignette sur `/collections`.
- `collections-seo.json`, `state.json`, `import_catalogue.py` et `menu_collections.py` alignés :
  un rejeu ne fera pas disparaître le rayon.

---

## 8. Photos — livraison Codex du 26/08 midi

Codex a livré **18 JPEG sur 29 attendus** (le « 26 » du brief était une erreur de compte).
Rattachés le même jour, photos AliExpress retirées.

| Handle | Galerie | Teinte | En ligne |
|---|---|---|---|
| LM-122 `applique-murale-pierre-588683` | g1–g5 | — | oui |
| LM-123 `applique-liseuse-pierre-311650` | g1–g5 | Bois clair | oui |
| LM-124 `applique-double-travertin-474088` | g1–g5 | Noyer | oui |
| Cover `appliques-murales` | 1 | — | oui |
| LM-125 `applique-murale-travertin-358794` | bloqué | — | brouillon |
| LM-126 `applique-murale-pierre-metal-147598` | AE en attendant Codex | — | **oui depuis 13:00**, copy cubique |

Le blocage de midi était juste : Codex a refusé d’inventer un galet. Le soir, la copy de LM-126
décrit le bloc 16 × 6,5 cm vu sur les photos. Relance Codex : `briefs/2026-08-26-codex-lm126.md`.
LM-125 reste hors brief (délai).

Script : `attach_applique_codex.py`. QA : `livraisons-visuels-codex/QA-APPLIQUES-2026-08-26.md`.

---

## 9. Décisions qui restent à Hakim

1. **Commande test.** LM-122, LM-123 et LM-124 portent la même marque fiche `pumous` et des
   adresses proches à Guangzhou : une seule commande suffit à voir la pièce et à trancher la
   question de la matière.
2. **LM-125.** Requoté le 26/08 12:46 : A, B et C partent toutes en **24–32 j**. Attribut IP =
   « Non résistant à l’eau ». Silhouette réelle = cylindre cannelé 16,5 × 9 cm. Rester en brouillon.
3. **LM-126.** Copy réécrite, fiche **republiée**. Brief Codex : `briefs/2026-08-26-codex-lm126.md`.
   Boutique Plum, liste 86 %.
4. **LM-127.** Poussée 26/08 soir. Coût DSers **83,75 €** (devis API 35,99 €, +133 %).
   PV **159 €**, marge 46,75 € HT (35 %). Délai Cainiao 8–16 j, dans la promesse 7–17.
   **Galerie Codex rattachée le 26/08 13:40** : 5 JPEG 2048², 8 photos AE (logo BOTIMI)
   retirées. SKU inchangé. 0 vente, à tester. Oiseau, rotin, céramique, bras long,
   laiton massif : toujours aucune offre 220 V exploitable.

---

## Fichiers

- `apply_appliques.py` — script rejouable, idempotent, `--dry-run` et `--only P1,P3`
- `appliques-copy.json` — toute la copy et les prix, éditables sans toucher au code
- `backups/2026-08-26-appliques/` — les 5 fiches telles que DSers les a poussées
- `briefs/2026-08-26-codex-appliques.md` — brief photo de la première vague (ne plus relancer pour LM-126)
- `../briefs/2026-08-26-codex-lm126.md` — relance Codex sur le bloc cubique
- `../briefs/2026-08-26-codex-lm127.md` — Codex boule verre, sans logo BOTIMI
- `SOURCING-APPLIQUES-V2-2026-08-26.md` — second passage (verre, cylindre, liseuse)
- `appliques-v2-a-importer.json` — spec d’import, désormais poussée (LM-127)

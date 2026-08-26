# Rayon appliques murales — import DSers et mise en ligne

**26/08/2026.** Suite du sourcing du matin (`SOURCING-APPLIQUES-2026-08-26.md`).
Feu vert Hakim : importer les cinq fiches dans DSers, les pousser sur Shopify, rédiger la copy,
préparer le brief photo.

**Résultat : 5 fiches importées, 4 en ligne, 1 en brouillon.** Le rayon existe.

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
| Mise en ligne | 4 ACTIVE, 1 DRAFT |

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
| LM-126 | `applique-murale-pierre-metal-147598` | Applique murale galet beige pierre et métal, entrée | 109 € | 2 finitions | ACTIVE |
| LM-125 | `applique-murale-travertin-358794` | Applique murale galet travertin LED, salon | 149 € | 1 | **DRAFT** |

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

## 8. Photos

Les 5 fiches portent encore les **photos AliExpress brutes** : fonds gris, textes incrustés,
décors d’hôtel. C’est le seul rayon de la boutique qui n’est pas au style `g1`.

44 visuels source ont été descendus dans `sources-par-handle/{handle}/`.
Brief Codex écrit : `briefs/2026-08-26-codex-appliques.md`, **26 JPEG** demandés
(5 galeries de 5 vues, 3 vues de teinte, 1 cover de collection).

---

## 9. Décisions qui restent à Hakim

1. **Commande test.** LM-122, LM-123 et LM-124 portent la même marque fiche `pumous` et des
   adresses proches à Guangzhou : une seule commande suffit à voir la pièce et à trancher la
   question de la matière.
2. **LM-125.** Reste en brouillon. Trois issues : requoter les variantes B et C, trouver un autre
   fournisseur du même galet, ou l’abandonner. En l’état, 22 à 38 jours de délai contre 7 à 17
   promis en boutique, ce n’est pas tenable.
3. **LM-126.** Taux de satisfaction liste de 86 % chez Plum Lighting, sous notre seuil habituel.
   Mise en ligne quand même parce que la marge est la meilleure du rayon et le stock confortable.
   À surveiller à la première commande.
4. **Les formes qui manquent.** Le rayon n’a qu’une matière. Oiseau (le best-seller de Lustria),
   verre, laiton, rotin, bras long, extérieur 220 V : aucune fiche quotable trouvée. Un second
   passage de sourcing est nécessaire pour que le rayon pèse.

---

## Fichiers

- `apply_appliques.py` — script rejouable, idempotent, `--dry-run` et `--only P1,P3`
- `appliques-copy.json` — toute la copy et les prix, éditables sans toucher au code
- `backups/2026-08-26-appliques/` — les 5 fiches telles que DSers les a poussées
- `briefs/2026-08-26-codex-appliques.md` — le brief photo

---
type: journal
boutique: seiko-mod
date: 2026-08-11
nature: intervention
leviers: [sourcing, technique]
titre: "Re-sourcing cadrans arabes orientaux — passe finale ciblée — 11/08/2026"
---

# Re-sourcing cadrans arabes orientaux — passe finale ciblée — 11/08/2026

## Verdict

**AUCUN QUATRIÈME PRODUIT QUALIFIABLE TROUVÉ.**

Le total reste honnêtement à **3 produits distincts qualifiés** :

1. `1005009751528666`
2. `1005007348127532`
3. `1005007347658552`

Il manque donc **exactement 1 produit** pour atteindre le minimum de 4, et 5 pour le maximum demandé de 8.

Aucune action Shopify, DSers, commande, paiement ou génération n'a été réalisée. AliExpress a été interrogé uniquement par l'API officielle via le gateway VPS en lecture seule.

## Couverture de la passe finale

- **80 recherches API réussies sur 80** ;
- **676 item IDs distincts** dans ces réponses ;
- **104 fiches** du résultat cadran/vendeur relues via `variants`, puis plusieurs contrôles de bord supplémentaires ;
- requêtes en arabe, persan, ourdou, hindi, chinois, russe, allemand, espagnol, italien, turc, français et anglais ;
- tris `orders`, `price_asc` et `price_desc` ;
- 28,5 / 29 / 31 / 33,5 mm, date / sans date, NH35 / NH36 / NH38 / NH70 / Miyota / ETA ;
- recherches sur les noms vendeurs, identifiants vendeurs, fragments exacts de titre et libellés de variantes.

Le gateway officiel n'expose que `health`, `search`, `variants` et `exact`. Il ne fournit pas de catalogue vendeur ni d'endpoint `related`. La recherche de produits frères a donc été faite sans navigateur : récupération des résultats officiels, appel `variants`, puis filtre sur les identifiants vendeur live.

## Vendeurs demandés

### Watch DlY Factory Store — `1103516380`

Les fiches du résultat relues par l'API n'ont exposé que :

| Item | Ventes live | Décision |
|---|---:|---|
| `1005007347658552` | 164 | déjà qualifié |
| `1005006625587280` | 458 | **REFUS** |

`1005006625587280` contient 11 variantes 28,5 mm NH35/NH36. Les onze images officielles montrent des index bâtons occidentaux, aucun chiffre arabe oriental, et le texte physique `SUPERLATIVE CHRONOMETER / OFFICIALLY CERTIFIED`. Il échoue donc simultanément aux portes glyphes et verbatim.

Preuve : `boutique-seiko-mod/preuves/preuves-sourcing-api-2026-08-11-agent/1005006625587280-refus-watch-diy.jpg`, SHA-256 `c1adfc0f553e5f078a0282c170819539ef543d8f7d370c8781261580cedf2d1b`.

### XinXin Watch Parts Store — `1104278703`

Le filtre vendeur n'a remonté que `1005009751528666`, déjà qualifié. Les requêtes basées sur ses libellés `Black Gold Dial`, `Black Silver Dial`, `Sky Blue Dial`, couleurs, aiguilles, Sunburst, NH35 et 4R n'ont pas révélé une seconde fiche XinXin distincte.

## Autres pistes exactes contrôlées

| Item | Ventes live | Contrôle image / structure | Décision |
|---|---:|---|---|
| `1005009745831804` | 215 | 10 variantes 28,5 mm, chiffres occidentaux dispersés et slogan `Who cares I'm already late` | REFUS glyphes + texte |
| `1005006012512581` | 93 | 21 images pilote 29 mm, chiffres occidentaux 1–12 | REFUS glyphes |
| `1005010303631276` | 190 | 13 images pilote 33,5 mm, chiffres occidentaux 1–24 | REFUS glyphes |
| `1005009735394195` | 123 | chiffres occidentaux et `AUTOMATIC` sur chaque cadran | REFUS glyphes + texte |
| `1005011709743734` | 107 | index bâtons et `AUTOMATIC` | REFUS glyphes + texte |
| `1005010135248171` | 11 | toutes les variantes déclarées `s dial` | REFUS marque |
| `1005009441078627` | 58 | montre quartz complète à chiffres orientaux ; aucune taille de cadran ni compatibilité de pièce NH35/NH36 | REFUS catégorie/compatibilité |
| `1005008598668872` | 0 | montre complète NH35 36/39 mm | REFUS ventes + catégorie |
| `1005009756751859` | 16 | montre NH35 carrée complète, pas un cadran compatible sourcé | REFUS catégorie |
| `1005012130205925` | **9** | glyphes et absence de texte compatibles, mais seuil ferme non atteint | REFUS ventes |

Preuve de `1005009745831804` : `boutique-seiko-mod/preuves/preuves-sourcing-api-2026-08-11-agent/1005009745831804-refus-lucky.jpg`, SHA-256 `711afecec6000608b64be074580c3363d93c1e70975a9f99b55a626cb8663acd`.

## Quasi-candidat recontrôlé une dernière fois

`1005012130205925` a été relu le **11/08/2026 à 19:24:50 UTC** :

- statut `onSelling` ;
- **9 ventes**, inchangé ;
- 5 variantes ;
- stock 97–99 ;
- prix 6,59 EUR.

Il reste à une vente de la porte, mais n'est pas importable aujourd'hui sous la règle `>= 10 ventes`.

## Conclusion

La passe finale ne permet pas de prétendre que quatre produits passent. Le manque exact est **1 produit distinct**. Le seul levier court terme honnête est un futur recontrôle live de `1005012130205925` après sa dixième vente ; d'ici là, le lot minimum n'est pas atteint.


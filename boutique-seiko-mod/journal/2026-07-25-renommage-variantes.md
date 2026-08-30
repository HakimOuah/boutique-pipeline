---
type: journal
boutique: seiko-mod
date: 2026-07-25
nature: intervention
leviers: [catalogue, seo]
titre: "Renommage des variantes opaques — NOIRMONT"
---

# Renommage des variantes opaques — NOIRMONT
Boutique Maison Noirmont (Shopify `v42pzp-h4`) — 25/07/2026
Compte DSers : `contact.noirmont`

> **État final : 10 fiches sur 11 renommées, 117 valeurs d'option réécrites sur les 124 opaques. 172 variantes avant / 172 après, 0 SKU modifié. Compteurs DSers inchangés : Mes Produits 44 · AliExpress 44 · Unmapped 0.**

## Méthode

Pour chaque fiche, l'URL fournisseur a été relevée dans DSers (propriété `supplyProductId` de l'état interne de « Mes Produits »), puis la page AliExpress ouverte dans la session Chrome de Hakim (aucun CAPTCHA rencontré, aucune tentative de résolution).

**Le rapprochement code → vignette est exact, pas déduit.** Chaque vignette de variante AliExpress porte un attribut `data-sku-col` de la forme `14-200000914`, et chaque SKU Shopify porte la même chaîne (`14:200000914#M14`). La correspondance a donc été faite sur l'identifiant de valeur de propriété AliExpress, pas sur l'ordre d'affichage. Les images ont ensuite été affichées en pleine résolution dans une grille d'inspection pour lire la couleur/matière réelle.

Renommage appliqué par `productOptionUpdate` + `optionValuesToUpdate` (mutation qui ne touche ni les SKU ni les variantes). **Aucun `productOptionsDelete`, aucune suppression de variante, aucun SKU écrit.**

Le nom de l'option elle-même a aussi été corrigé quand « Référence » ou « Modèle » ne disait rien (ex. « Référence » → « Cadran »).

## Les 11 URL fournisseur relevées

| Produit (ID Shopify) | `supplyProductId` | Fiche fournisseur |
|---|---|---|
| Contre-la-montre — Chronographe panda `10977444528466` | 1005004821593794 | `https://fr.aliexpress.com/item/1005004821593794.html` |
| Voyageur — GMT automatique `10977448657234` | 1005009740849403 | `https://fr.aliexpress.com/item/1005009740849403.html` |
| Noirmont Deux — Plongeuse céramique `10977448624466` | 1005005629655849 | `https://fr.aliexpress.com/item/1005005629655849.html` |
| Intégrale — Sport chic acier `10977444561234` | 1005009821439225 | `https://fr.aliexpress.com/item/1005009821439225.html` |
| Héritage — Plongeuse vintage 42 `10977444594002` | 1005008657937411 | `https://fr.aliexpress.com/item/1005008657937411.html` |
| Remontoir Bois `10977444659538` | 1005012102224533 | `https://fr.aliexpress.com/item/1005012102224533.html` |
| Rouleau de Voyage — cuir `10977444823378` | 1005008493748701 | `https://fr.aliexpress.com/item/1005008493748701.html` |
| Bracelet Présidentiel — doré `10977445085522` | 1005010705179185 | `https://fr.aliexpress.com/item/1005010705179185.html` |
| Loupe de date — saphir `10977445216594` | 1005011940440567 | `https://fr.aliexpress.com/item/1005011940440567.html` |
| Set de tournevis d'horloger `10977444987218` | 1005008543517157 | `https://fr.aliexpress.com/item/1005008543517157.html` |
| Remontoir Collection `10977444757842` | 1005006938556690 | `https://fr.aliexpress.com/item/1005006938556690.html` |

Bonus relevé au passage (non traité, hors périmètre) : **Bracelet Présidentiel — acier 904L** = `1005006496083816`.

---

## 1. Contre-la-montre — Chronographe panda (20 valeurs) — option « Référence » → **« Cadran »**

Tous les modèles : chronographe 39 mm, lunette tachymètre, mouvement VK63.

| Code | Ce que montre la vignette | Nouveau libellé | Appliqué |
|---|---|---|---|
| M-1 | Cadran blanc, compteurs clairs cerclés de noir, lunette noire, bracelet acier | Blanc · compteurs cerclés | oui |
| M-2 | Cadran noir, compteurs blancs, aiguilles acier, bracelet acier | Panda inversé · aiguilles acier | oui |
| M-3 | Cadran champagne, compteurs noirs, bracelet acier | Champagne · bracelet acier | oui |
| M-4 | Cadran champagne, compteurs noirs, bracelet caoutchouc noir | Champagne · bracelet caoutchouc | oui |
| M-5 | Cadran blanc, compteurs blancs ton sur ton, bracelet caoutchouc noir | Blanc ton sur ton · caoutchouc | oui |
| M-6 | Cadran blanc, compteurs noirs, bracelet caoutchouc noir | Panda · bracelet caoutchouc | oui |
| M-7 | Cadran noir, compteurs noirs, bracelet caoutchouc noir | Noir intégral · caoutchouc | oui |
| M8 | Cadran blanc, compteurs gris argenté, bracelet acier | Blanc · compteurs gris | oui |
| M9 | Cadran rose, compteurs roses, bracelet acier | Rose poudré | oui |
| M10 | Cadran turquoise, compteurs turquoise ton sur ton, bracelet acier | Turquoise ton sur ton | oui |
| M11 | Cadran vert, compteurs verts, bracelet caoutchouc vert | Vert · caoutchouc vert | oui |
| M12 | Cadran vert, compteurs verts, bracelet acier | Vert · bracelet acier | oui |
| M13 | Cadran gris anthracite, compteurs noirs, bracelet acier | Gris anthracite | oui |
| M14 | Cadran argenté, compteurs gris, bracelet caoutchouc noir | Argent · caoutchouc noir | oui |
| M15 | Cadran blanc, compteurs **bleus**, lunette acier, bracelet caoutchouc bleu marine | Compteurs bleus · bracelet bleu | oui |
| M16 | Cadran turquoise, compteurs **noirs** contrastés, bracelet acier | Turquoise · compteurs noirs | oui |
| M17 | Cadran noir, lunette tachymètre inscrite, bracelet caoutchouc noir (silhouette Speedmaster) | Noir tachymètre · caoutchouc | oui |
| M18 | Cadran noir, compteurs blancs, **aiguille chrono rouge**, bracelet acier | Panda inversé · aiguille rouge | oui |
| M19 | Cadran ivoire, compteurs noirs, **aiguille chrono rouge**, bracelet acier | Panda ivoire · aiguille rouge | oui |
| M20 | Cadran bleu glacier dégradé, compteurs assortis, bracelet acier | Bleu glacier | oui |

Contrôle : 20 variantes avant / 20 après, 20 SKU identiques.

## 2. Voyageur — GMT automatique (9 valeurs) — option « Référence » → **« Boîtier & bracelet »**

Tous les modèles : GMT 40 mm, lunette « rootbeer » brun & noir, cadran noir (sauf réf. 3 et 4, cadran brun). Ce qui les distingue est le **métal du boîtier, le type de bracelet, et la présence ou non d'un logo sur le cadran**.

| Code | Ce que montre la vignette | Nouveau libellé | Appliqué |
|---|---|---|---|
| 1 | Or rose intégral, bracelet 5 maillons, cadran stérile | Or rose · bracelet 5 maillons | oui |
| 2 | Bicolore acier & or rose, bracelet 5 maillons, cadran stérile | Bicolore · bracelet 5 maillons | oui |
| 3 | Bicolore, bracelet 5 maillons, cadran brun, **logo fournisseur imprimé** | Bicolore · cadran brun · siglé | oui |
| 4 | Bicolore, bracelet 5 maillons, cadran brun, stérile | Bicolore · cadran brun | oui |
| 5 | Bicolore, bracelet 3 maillons, **logo fournisseur imprimé** | Bicolore · bracelet 3 maillons · siglé | oui |
| 6 | Bicolore, bracelet 3 maillons, stérile | Bicolore · bracelet 3 maillons | oui |
| 7 | Or intégral, bracelet Président (maillons demi-lune), stérile | Or · bracelet Président | oui |
| 8 | Or intégral, bracelet 3 maillons, **logo fournisseur imprimé** | Or · bracelet 3 maillons · siglé | oui |
| 9 | Or intégral, bracelet 3 maillons, stérile | Or · bracelet 3 maillons | oui |

Contrôle : 36 variantes avant / 36 après, 36 SKU identiques.

> ### ⚠️ Anomalie à trancher — 3 déclinaisons ne sont pas stériles
> Les réf. **3, 5 et 8** portent un **logo de marque tierce imprimé sur le cadran** (le logo du fabricant, lisible à 12 h sur les photos fournisseur). Cela contredit la règle absolue de la maison : 100 % sans logo sur les produits et les visuels.
> Elles ont été nommées « … · siglé » pour rester distinctes et honnêtes, **mais elles ne devraient pas être vendues en l'état**. Retirer ces 3 valeurs supprimerait 12 des 36 variantes — décision à prendre par Hakim, à ne pas exécuter sans validation.

## 3. Noirmont Deux — Plongeuse céramique (7 valeurs) — ❌ **NON RENOMMÉE**

**Codes conservés : « Référence 1 » à « Référence 7 ».**

Raison : la fiche fournisseur `1005005629655849` **ne différencie pas visuellement ses 7 déclinaisons**. Les 7 vignettes sont des variations d'une même photo de démonstration de lume (cadran bleu ciel couvert de pastilles de matière luminescente multicolores) ; l'image principale de la fiche ne change pas non plus quand on sélectionne une variante (vérifié : les 7 sélections renvoient la même image). Seul le style de lunette varie légèrement (lunette plongeuse graduée pour 1-5, lunette GMT 24 h pour 6-7), ce qui ne permet pas de produire 7 libellés distincts et honnêtes.

Conformément à la consigne « ne devine pas », les codes d'origine ont été laissés intacts. **Action requise** : faire une photo par coloris, ou re-sourcer cette fiche chez un vendeur qui photographie ses variantes.

Contrôle : 28 variantes, aucune modification.

## 4. Intégrale — Sport chic acier (7 valeurs) — option « Référence » → **« Cadran »**

| Code | Ce que montre la vignette | Nouveau libellé | Appliqué |
|---|---|---|---|
| 1 | Cadran turquoise à stries horizontales, boîtier acier | Turquoise | oui |
| 2 | Cadran bleu ciel à stries, boîtier acier | Bleu ciel | oui |
| 3 | Cadran blanc argenté à stries, boîtier acier | Blanc argenté | oui |
| 4 | Cadran noir à stries, boîtier acier | Noir | oui |
| 5 | Cadran bleu nuit à stries, boîtier acier | Bleu nuit | oui |
| 6 | Cadran vert à stries, boîtier acier | Vert | oui |
| 7 | Cadran brun à stries, **boîtier et bracelet or rose** | Brun · boîtier or rose | oui |

Contrôle : 7 variantes avant / 7 après, 7 SKU identiques.

## 5. Héritage — Plongeuse vintage 42 (3 valeurs) — option « Référence » → **« Cadran & lunette »**

| Code | Ce que montre la vignette | Nouveau libellé | Appliqué |
|---|---|---|---|
| S1 | Cadran bleu, insert de lunette bleu | Bleu · lunette bleue | oui |
| S2 | Cadran bleu nuit, insert de lunette noir | Bleu nuit · lunette noire | oui |
| S3 | Cadran vert, insert de lunette vert | Vert · lunette verte | oui |

Contrôle : 3 variantes avant / 3 après, 3 SKU identiques.

## 6. Remontoir Bois (8 valeurs) — option « Référence » → **« Finition & capacité »**

Structure du code décodée : **M11xxx = 1 montre, M12xxx = 2 montres** ; les deux derniers chiffres donnent l'essence.

| Code | Ce que montre la vignette | Nouveau libellé | Appliqué |
|---|---|---|---|
| M11011 | Coffret noir laqué, 1 emplacement | Noir laqué · 1 montre | oui |
| M11032 | Coffret acajou rouge brillant, 1 emplacement | Acajou · 1 montre | oui |
| M11052 | Coffret ébène brun foncé, 1 emplacement | Ébène · 1 montre | oui |
| M11071 | Coffret noyer brun veiné, 1 emplacement | Noyer · 1 montre | oui |
| M12011 | Coffret noir laqué, 2 emplacements | Noir laqué · 2 montres | oui |
| M12032 | Coffret acajou rouge brillant, 2 emplacements | Acajou · 2 montres | oui |
| M12052 | Coffret ébène brun foncé, 2 emplacements | Ébène · 2 montres | oui |
| M12071 | Coffret noyer brun veiné, 2 emplacements | Noyer · 2 montres | oui |

Contrôle : 8 variantes avant / 8 après, 8 SKU identiques.

## 7. Rouleau de Voyage — cuir (12 valeurs) — option « Référence » → **« Couleur & capacité »**

Structure décodée : **WB[couleur][nombre d'emplacements]** — 1 = noir, 2 = brun, 3 = bleu marine, 4 = vert.

| Code | Ce que montre la vignette | Nouveau libellé | Appliqué |
|---|---|---|---|
| WB11 | Cuir noir, intérieur noir, 1 emplacement | Cuir noir · 1 montre | oui |
| WB12 | Cuir noir, 2 emplacements | Cuir noir · 2 montres | oui |
| WB13 | Cuir noir, 3 emplacements | Cuir noir · 3 montres | oui |
| WB21 | Cuir brun clair, daim taupe, 1 emplacement | Cuir brun · 1 montre | oui |
| WB22 | Cuir brun clair, 2 emplacements | Cuir brun · 2 montres | oui |
| WB23 | Cuir brun clair, 3 emplacements | Cuir brun · 3 montres | oui |
| WB31 | Cuir bleu marine, daim bleu, 1 emplacement | Cuir bleu marine · 1 montre | oui |
| WB32 | Cuir bleu marine, 2 emplacements | Cuir bleu marine · 2 montres | oui |
| WB33 | Cuir bleu marine, 3 emplacements | Cuir bleu marine · 3 montres | oui |
| WB41 | Cuir vert, daim vert, 1 emplacement | Cuir vert · 1 montre | oui |
| WB42 | Cuir vert, 2 emplacements | Cuir vert · 2 montres | oui |
| WB43 | Cuir vert, 3 emplacements | Cuir vert · 3 montres | oui |

> Note : la consigne supposait `WB33 = « Cuir brun · 3 montres »`. La vignette montre en réalité du **bleu marine**. C'est le brun qui porte le préfixe WB2x.

Contrôle : 12 variantes avant / 12 après, 12 SKU identiques.

## 8. Bracelet Présidentiel — doré (24 valeurs) — option « Modèle » → **« Maille & finition »**

Le type de maille était déjà lisible ; c'est le **numéro** qui ne voulait rien dire. Il a été remplacé par la finition métal. « Bracelet — n » (maille 3 rangs) est devenu « 3 rangs » pour être explicite.

| Code d'origine | Ce que montre la vignette | Nouveau libellé | Appliqué |
|---|---|---|---|
| Maille fixe — 1 | Acier | Maille fixe · acier | oui |
| Maille fixe — 2 | Bicolore acier & or rose | Maille fixe · acier & or rose | oui |
| Maille fixe — 3 | Bicolore acier & or jaune | Maille fixe · acier & or | oui |
| Maille fixe — 4 | Or jaune intégral | Maille fixe · or jaune | oui |
| Maille fixe — 5 | Or rose intégral | Maille fixe · or rose | oui |
| Président — 6 | Acier | Président · acier | oui |
| Président — 7 | Noir (PVD) | Président · noir | oui |
| Président — 8 | Or rose intégral | Président · or rose | oui |
| Président — 9 | Or jaune intégral | Président · or jaune | oui |
| Président — 10 | Bicolore acier & or rose | Président · acier & or rose | oui |
| Président — 11 | Bicolore acier & or jaune | Président · acier & or | oui |
| Jubilé — 12 | Or rose intégral | Jubilé · or rose (réf. 12) | oui ⚠️ |
| Jubilé — 13 | Bicolore acier & or rose | Jubilé · acier & or rose | oui |
| Jubilé — 14 | Bicolore acier & or jaune | Jubilé · acier & or | oui |
| Jubilé — 15 | Or rose intégral | Jubilé · or rose (réf. 15) | oui ⚠️ |
| Jubilé — 16 | Noir (PVD) | Jubilé · noir | oui |
| Jubilé — 17 | Acier | Jubilé · acier | oui |
| Bracelet — 18 | Maille 3 rangs, or rose | 3 rangs · or rose | oui |
| Bracelet — 19 | Maille 3 rangs, or jaune | 3 rangs · or jaune | oui |
| Bracelet — 20 | Maille 3 rangs, acier & or rose | 3 rangs · acier & or rose | oui |
| Bracelet — 21 | Maille 3 rangs, noir | 3 rangs · noir | oui |
| Bracelet — 22 | Maille 3 rangs, acier & or jaune | 3 rangs · acier & or | oui |
| Bracelet — 23 | Maille 3 rangs, acier | 3 rangs · acier | oui |
| Full Sand Belt — 24 | Maille sablée/brossée, acier | Maille sablée · acier | oui |

⚠️ **Jubilé 12 et Jubilé 15 ne sont pas départageables** : les deux photos fournisseur montrent le même bracelet jubilé or rose intégral, sous le même angle. Le numéro d'origine a été conservé entre parenthèses pour garder les deux valeurs distinctes et traçables. À trancher avec le fournisseur ou par une photo réelle.

Contrôle : 24 variantes avant / 24 après, 24 SKU identiques.

## 9. Loupe de date (14 valeurs) — option « Modèle & taille » → **« Matière & taille »**

La légende imprimée sur les vignettes fournisseur est explicite : **« Type A is made of mineral material, and Type B is made of sapphire material; the size is length x width »**. A et B ne désignent donc **pas une forme** (l'hypothèse « bombée / plate » était fausse) mais la **matière**.

| Code | Ce que montre la vignette | Nouveau libellé | Appliqué |
|---|---|---|---|
| A · 4,0 mm | Verre minéral, rond Ø 4,0 | Minéral · Ø 4,0 mm | oui |
| A · 4,5 mm | Verre minéral, rond Ø 4,5 | Minéral · Ø 4,5 mm | oui |
| A · 3,5 × 3 mm | Verre minéral, ovale | Minéral · 3,5 × 3 mm | oui |
| A · 4,5 × 3,5 mm | Verre minéral, ovale | Minéral · 4,5 × 3,5 mm | oui |
| A · 5,5 × 4,5 mm | Verre minéral, ovale | Minéral · 5,5 × 4,5 mm | oui |
| A · 5,8 × 4,5 mm | Verre minéral, ovale | Minéral · 5,8 × 4,5 mm | oui |
| A · 7 × 5,5 mm | Verre minéral, ovale | Minéral · 7 × 5,5 mm | oui |
| A · 10 × 5 mm | Verre minéral, ovale allongé | Minéral · 10 × 5 mm | oui |
| B · 5,5 mm | Saphir, rond Ø 5,5 | Saphir · Ø 5,5 mm | oui |
| B · 3,5 × 3 mm | Saphir, ovale | Saphir · 3,5 × 3 mm | oui |
| B · 4,5 × 3,5 mm | Saphir, ovale | Saphir · 4,5 × 3,5 mm | oui |
| B · 5,5 × 4,5 mm | Saphir, ovale | Saphir · 5,5 × 4,5 mm | oui |
| B · 5,8 × 4,5 mm | Saphir, ovale | Saphir · 5,8 × 4,5 mm | oui |
| B · 7 × 5,5 mm | Saphir, ovale | Saphir · 7 × 5,5 mm | oui |

> ⚠️ **Le titre de la fiche est « Loupe de date — saphir » alors que 8 des 14 variantes sont en verre minéral.** Titre à corriger (« Loupe de date — saphir ou minéral ») ou catalogue à restreindre aux 6 variantes saphir.

Contrôle : 14 variantes avant / 14 après, 14 SKU identiques.

## 10. Set de tournevis d'horloger (5 valeurs) — option « Modèle » → **« Finition des manches »**

Les 5 coffrets sont identiques (10 tournevis, 0,50 à 3,00 mm). Seule la **finition des manches** change.

| Code | Ce que montre la vignette | Nouveau libellé | Appliqué |
|---|---|---|---|
| A | Manches acier à moletage droit, petite bague de couleur en tête | Manche moleté · repère couleur | oui |
| B | Manches acier à moletage droit, grande tête évasée de couleur | Manche moleté · tête colorée | oui |
| C | Manches acier à moletage annelé (bagues empilées), petite bague de couleur | Manche annelé · repère couleur | oui |
| D | Manches acier à moletage annelé, grande tête évasée de couleur | Manche annelé · tête colorée | oui |
| E | Manches **noirs**, grande tête évasée de couleur | Manche noir · tête colorée | oui |

Contrôle : 5 variantes avant / 5 après, 5 SKU identiques.

## 11. Remontoir Collection (15 valeurs) — option « Modèle » → **« Coffret & capacité »**

Le suffixe A/B/C désignait le **type de coffret**, décodé sur les vignettes :
- **A** = coffret bois façade verre, intérieur noir ou beige
- **B** = coffret cuir PU noir à porte vitrée **verrouillable par clé**
- **C** = coffret bois à **éclairage LED**, finition noire ou rouge

| Code d'origine | Ce que montre la vignette | Nouveau libellé | Appliqué |
|---|---|---|---|
| Noir · 1 montre · A | Coffret bois, intérieur noir, 1 emplacement | Bois · noir · 1 montre | oui |
| Blanc · 1 montre · A | Coffret bois, intérieur beige, 1 emplacement | Bois · beige · 1 montre | oui |
| Noir · 2 montres · A | Coffret bois, intérieur noir, 2 emplacements | Bois · noir · 2 montres | oui |
| Blanc · 2 montres · A | Coffret bois, intérieur beige, 2 emplacements | Bois · beige · 2 montres | oui |
| Noir · 4 montres · A | Coffret bois, intérieur noir, 4 emplacements | Bois · noir · 4 montres | oui |
| Blanc · 4 montres · A | Coffret bois, intérieur beige, 4 emplacements | Bois · beige · 4 montres | oui |
| Noir · 6 montres · A | Coffret bois, intérieur noir, 6 emplacements | Bois · noir · 6 montres | oui |
| Blanc · 6 montres · A | Coffret bois, intérieur beige, 6 emplacements | Bois · beige · 6 montres | oui |
| Cuir PU · 2 montres · B | Coffret cuir PU noir, serrure à clé, 2 emplacements | Cuir PU · fermeture à clé · 2 montres | oui |
| Cuir PU · 4 montres · B | Coffret cuir PU noir, serrure à clé, 4 emplacements | Cuir PU · fermeture à clé · 4 montres | oui |
| Cuir PU · 6 montres · B | Coffret cuir PU noir, serrure à clé, 6 emplacements | Cuir PU · fermeture à clé · 6 montres | oui |
| Noir · 2 montres · C | Coffret bois éclairage LED, finition noire, 2 emplacements | Bois LED · noir · 2 montres | oui |
| Rouge · 2 montres · C | Coffret bois éclairage LED, finition rouge, 2 emplacements | Bois LED · rouge · 2 montres | oui |
| Noir · 4 montres · C | Coffret bois éclairage LED, finition noire, 4 emplacements | Bois LED · noir · 4 montres | oui |
| Rouge · 4 montres · C | Coffret bois éclairage LED, finition rouge, 4 emplacements | Bois LED · rouge · 4 montres | oui |

> Note : le titre de la fiche dit « 2 à 6 montres » alors que 2 variantes sont à **1 montre**. Titre à ajuster (« 1 à 6 montres »).

Contrôle : 15 variantes avant / 15 après, 15 SKU identiques.

---

## Codes non identifiés — récapitulatif

| Fiche | Codes | Raison |
|---|---|---|
| Noirmont Deux — Plongeuse céramique | Référence 1 à 7 (les 7) | Fiche fournisseur sans photo par variante : les 7 vignettes sont la même démonstration de lume, l'image principale ne change pas à la sélection |
| Bracelet Présidentiel — doré | Jubilé 12 vs Jubilé 15 | Deux photos du même bracelet jubilé or rose intégral, non départageables. Numéro conservé entre parenthèses |

**Total : 9 valeurs sur 124 restent non résolues (7 %)** — 7 non renommées, 2 renommées mais départagées par leur numéro d'origine.

---

## Liste des visuels à produire

Règle appliquée : un visuel de variante est nécessaire quand le choix porte sur une **apparence** (couleur, matière, finition) ; il est inutile quand le choix porte sur une **dimension ou une capacité** chiffrée, déjà explicite dans le libellé.

### Visuels indispensables — le libellé seul ne suffit pas

| Fiche | Valeurs | Nb de visuels | Pourquoi |
|---|---|---|---|
| Contre-la-montre — Chronographe panda | Les 20 cadrans | **20** | Le cœur du choix. Des nuances comme « Turquoise ton sur ton » vs « Turquoise · compteurs noirs », ou les trois pandas inversés, ne se départagent qu'à l'image |
| Voyageur — GMT automatique | Les 9 (ou 6 si les siglées sont retirées) | **9** *(6)* | Métal du boîtier + type de bracelet : invisible sans photo |
| Noirmont Deux — Plongeuse céramique | Les 7 références | **7** | **Priorité absolue** : sans photo, le renommage lui-même est impossible. À shooter ou re-sourcer |
| Intégrale — Sport chic acier | Les 7 cadrans | **7** | Turquoise / bleu ciel / bleu nuit se confondent en texte |
| Héritage — Plongeuse vintage 42 | Les 3 | **3** | Cadran + insert de lunette |
| Remontoir Bois | 4 essences (1 visuel par essence suffit) | **4** | Noir laqué / acajou / ébène / noyer : choix d'aspect. La capacité n'a pas besoin d'image |
| Rouleau de Voyage — cuir | 4 couleurs (1 visuel par couleur) | **4** | Noir / brun / bleu marine / vert. La capacité n'a pas besoin d'image |
| Bracelet Présidentiel — doré | Les 24 | **24** | Maille × finition métal : les deux axes sont purement visuels |
| Set de tournevis d'horloger | Les 5 | **5** | Finition des manches, différence subtile |
| Remontoir Collection | 5 aspects de coffret (bois noir, bois beige, cuir PU, LED noir, LED rouge) | **5** | La capacité n'a pas besoin d'image |

**Sous-total : 88 visuels** (85 si les 3 GMT siglées sont retirées).

### Aucun visuel nécessaire

| Fiche | Valeurs | Pourquoi |
|---|---|---|
| Loupe de date | Les 14 | Le choix est une **dimension** (Ø 4,0 mm, 7 × 5,5 mm…) et une **matière** nommée. Une photo de loupe transparente n'apporte rien. Un **schéma coté unique** expliquant comment mesurer sa fenêtre de date serait bien plus utile qu'une image par variante |
| Toutes fiches — axe capacité | « 1 / 2 / 3 / 4 / 6 montres » | Chiffre explicite dans le libellé |
| Toutes fiches — axe mouvement & fond | « NH35 · fond verre »… | Déjà lisible, non visuel |

---

## Règles respectées

- **Aucun SKU modifié.** Les 172 SKU ont été relevés avant et après : identiques caractère par caractère. Seules des valeurs d'option ont été réécrites, via `productOptionUpdate` / `optionValuesToUpdate`.
- **Aucun `productOptionsDelete`, aucune suppression de variante, aucune option supprimée.** 172 variantes avant / 172 après.
- **Compteurs DSers vérifiés à l'écran après renommage** : Mes Produits **44** · AliExpress **44** · Unmapped **0** · 1688 **0** · Alibaba **0**. Aucun produit n'est repassé en « Unmapped » : le mapping tient.
- **Aucune commande, aucun achat, aucun identifiant saisi.** Session `contact.noirmont` déjà ouverte. Aucun CAPTCHA rencontré ni tenté.
- **Aucune marque tierce dans les libellés client.** Les variantes GMT à cadran logoté sont décrites par « siglé », sans nommer la marque.

## À faire ensuite

1. **Trancher les 3 GMT siglées** (réf. 3, 5, 8) — retrait probable, 12 variantes concernées.
2. **Photographier ou re-sourcer Noirmont Deux** — 7 références encore opaques.
3. **Corriger 2 titres de fiche** : « Loupe de date — saphir » (8 variantes sur 14 sont en minéral) et « Remontoir Collection — 2 à 6 montres » (2 variantes sont à 1 montre).
4. **Produire les 88 visuels de variantes** listés ci-dessus, en commençant par le chronographe (20) et le bracelet présidentiel (24), les deux fiches où le choix est aujourd'hui le plus aveugle.

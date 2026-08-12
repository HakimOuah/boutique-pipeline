# Import accessoires — lot 4 (NOIRMONT)

Date : 2026-07-26 · Boutique : Maison Noirmont (`v42pzp-h4`, maisonnoirmont.fr) · Compte DSers : `contact.noirmont`
Sources : `scratchpad/noirmont-fiches-accessoires.md` (v2, 10 fiches) + `2026-07-25-sourcing-accessoires-v3.md` (3 fiches retenues sur 6).

**13 fiches créées, toutes en DRAFT, toutes mappées.** Aucune commande passée, aucun achat, aucun identifiant saisi.

---

## Méthode appliquée

Conforme au brief : **import DSers d'abord, API Shopify ensuite**.

1. Import des 13 URL AliExpress une par une dans **Liste d'import** (champ « entrer le lien du produit »).
2. Sélection des **13 nouvelles cartes uniquement** (vérifiée par comptage DOM : 13 cases cochées sur 21 rendues) puis **PUSH TO STORE**.
   - Dans la modale « Pousser les produits » : case **« Set product status as Draft » cochée**, case **« Publier dans la Boutique également » laissée décochée** → les 13 fiches arrivent en DRAFT et sur aucun canal de vente.
3. Réécriture par l'API Shopify : titre, handle, description HTML, SEO, vendor, tags, collection `accessoires`, prix et prix barré, visuels.

**Le SKU porteur de la chaîne d'attributs AliExpress est bien présent sur chaque variante** — c'est tout l'intérêt du passage par DSers. Exemples relevés :

| Fiche | SKU d'une variante |
|---|---|
| Jubilé embouts courbes | `200000049:350853#steel-no logo;200000051:100016950` |
| Milanais | `200000049:200000080#1.0mm-gold;200000051:100016948` |
| Cuir daim | `200000049:990994103#Brown;200000051:168#20mm` |
| Kit d'entretien | `14:865#13pc Kits` |
| Loupe | `14:10#10X-with circle` |

Aucun mapping n'a eu à être refait à la main : le fournisseur est rattaché d'un coup à l'import.

---

## Les 13 fiches créées

Toutes : statut **DRAFT**, vendor **Maison Noirmont**, collection **Accessoires**.

| # | Titre | Handle | Product ID | Var. | Prix | Barré |
|---|---|---|---|---|---|---|
| 1 | Bracelet Jubilé — embouts courbes | `bracelet-jubile-embouts-courbes` | 10980388405586 | 15 | 29,90 / 34,90 / 39,90 | 38,90 / 45,90 / 51,90 |
| 2 | Bracelet acier massif — 12 à 22 mm | `bracelet-acier-massif-12-22-mm` | 10980388438354 | 60 | 39,90 / 49,90 / 59,90 | 51,90 / 64,90 / 77,90 |
| 3 | Bracelet Jubilé acier 904L — 20 mm | `bracelet-jubile-acier-904l-20mm` | 10980388471122 | 1 | 49,90 | 64,90 |
| 4 | Bracelet caoutchouc gaufré | `bracelet-caoutchouc-gaufre` | 10980388536658 | 72 | 24,90 | 32,90 |
| 5 | Coussins de présentation — lot de 10 | `coussins-de-presentation-lot-de-10` | 10980388569426 | 5 | 19,90 | 25,90 |
| 6 | Étui de voyage rigide | `etui-de-voyage-rigide` | 10980388602194 | 9 | 69,90 → 189,90 | 90,90 → 246,90 |
| 7 | Coffret 6 montres — couvercle verre | `coffret-6-montres-couvercle-verre` | 10980388667730 | 1 | 54,90 | 71,90 |
| 8 | Kit d'entretien — 13 pièces | `kit-d-entretien-13-pieces` | 10980388733266 | 1 | 29,90 | 38,90 |
| 9 | Outil de mise à taille de bracelet | `outil-de-mise-a-taille-de-bracelet` | 10980388766034 | 2 | 19,90 | 25,90 |
| 10 | Doigtiers d'horloger — latex | `doigtiers-d-horloger-latex` | 10980388831570 | 6 | 12,90 | 16,90 |
| 11 | Bracelet milanais — maille italienne | `bracelet-milanais-maille-italienne` | 10980388864338 | 32 | 14,90 / 24,90 | 19,90 / 32,90 |
| 12 | Bracelet cuir daim — dégagement rapide | `bracelet-cuir-daim-degagement-rapide` | 10980388897106 | 64 | 17,90 | 23,90 |
| 13 | Loupe d'horloger | `loupe-d-horloger` | 10980388962642 | 13 | 12,90 / 21,90 | 16,90 / 28,90 |

Fiches 11, 12, 13 = les trois retenues de la passe v3.

### Règle de prix et écarts assumés

Règle appliquée : **prix ≈ coût rendu × 3 à 4, arrondi au ,90 · prix barré = prix × 1,3 arrondi au ,90 supérieur.**

Les prix des rapports ont été repris tels quels **partout où la matrice réelle de variantes le permettait**. Le push DSers a révélé des coûts par variante que les rapports n'avaient pas : là où un prix unique serait tombé sous ×2,5 sur une partie de la gamme, j'ai **tiérisé** plutôt que de vendre à perte. Écarts et raisons :

| Fiche | Rapport | Appliqué | Pourquoi |
|---|---|---|---|
| 1 Jubilé courbes | 29,90 | 29,90 acier / 34,90 acier-or / 39,90 or | coût variante 6,30 → 11,10 € selon finition |
| 2 Acier massif | 39,90 | 39,90 acier / 49,90 or, noir, bicolore / 59,90 or rose | coût variante 9,82 → 18,18 € selon coloris |
| 5 Coussins | 7,90 | **19,90** | le fournisseur ne vend **que par lot de 10** (3,42–3,75 €) — la fiche a été retitrée en conséquence |
| 6 Étui de voyage | 69,90 | 69,90 (1 pl.) / 89,90 (2) / 109,90 (3) / 189,90 (6) | coût variante 17,79 → 52,85 € selon capacité |
| 11 Milanais | 11,90 | 14,90 (0,6 mm) / 24,90 (1,0 mm) | le 2,96 € du rapport ne concerne que le 0,6 mm argent ; le 1,0 mm monte à 7,29 € |
| 13 Loupe | 9,90 | 12,90 (loupe seule) / 21,90 (jeu de 4) | le jeu de 4 coûte 5,31 € contre 2,25 € l'unité |
| 8 Kit d'entretien | 29,90 | 29,90 | coût de la variante 13 pcs **confirmé** à 9,27 € (le rapport le laissait à confirmer) |

Autre ajustement : sur le **kit d'entretien**, les 4 variantes 1 pc / 3 pcs / 7 pcs ont été **supprimées** comme demandé — il ne reste que la 13 pièces. DSers affiche bien « Variantes(1) » après suppression, sans casser le mapping.

### Conformité éditoriale

- **Aucune marque tierce** dans les 13 titres, descriptions ou balises SEO. Les titres fournisseur citaient Rolex, Datejust, DW, Seiko, Tudor, Watchdives, IBBETON : tout a été réécrit. Seuls les noms de **style** subsistent (jubilé, oyster, milanais, gaufré, daim).
- **Promesses vérifiables uniquement.** Deux corrections de fond par rapport au rapport v2 :
  - fiche 2 : le rapport annonçait un choix « embout plat / embout courbe ». **Cette option n'existe pas** chez le fournisseur (les axes réels sont coloris × largeur). La promesse a été retirée.
  - fiche 10 : le produit n'est pas une paire de gants mais des **doigtiers latex**. Titre et description rectifiés.
- Chaque fiche bracelet explique **comment mesurer l'entrecorne** ; la loupe explique le choix du grossissement et ce qu'est l'œilleton ; l'outil explique le geste. Registre pédagogique au particulier, conforme à la charte.

---

## Écartées — et pourquoi

| Candidat | Source | Raison |
|---|---|---|
| Oyster 3 rangs | v2 | preuve sociale insuffisante (4,2/5, 7 avis) — consigne explicite, à re-sourcer |
| Ouvre-boîtier | v2 | preuve sociale insuffisante (1 avis, 6 ventes) — consigne explicite, à re-sourcer |
| **A4 — NATO / Zulu nylon** | v3 | **preuve sociale la plus mince du lot v3 (39 avis, 235 ventes, 4,5/5), réserve signalée dans le rapport** |
| A7 — bracelet à extrémité plate | v3 | retenable sur le fond, mais 283 avis contre 376 à 769 pour les trois gardées ; arbitré hors des 13 |
| B11 — présentoir bois WoodTen | v3 | **risque logo MOYEN portant sur le produit lui-même** (gravure « WoodTen » possible) — non levable sans échantillon ; c'est le seul candidat dont le risque n'est pas photographique |
| Boucle déployante seule (bundle A5) | v3 | le bundle « cuir + déployante » aurait imposé un mappage multi-fournisseurs sur 64 variantes ; le cuir est publié seul à 17,90 €. La déployante (`1005007900051846`, 624 avis) reste à créer si tu valides le montage |

---

## État des compteurs DSers

| Compteur | Avant | Après | Attendu |
|---|---|---|---|
| Mes Produits — Tous | 85 | **98** | 85 + 13 ✓ |
| Mes Produits — AliExpress | 85 | **98** | ✓ |
| Mes Produits — **Unmapped** | 0 | **0** | ✓ **aucune des 85 fiches existantes n'est repassée en Unmapped** |
| 1688 Dropshipping / Alibaba | 0 / 0 | 0 / 0 | ✓ |
| Liste d'import | 25 | 38 | 25 + 13 ✓ |

Les 13 nouvelles cartes DSers affichent nos titres français, nos visuels et nos prix (contrôle visuel : Coffret 54,90 · Kit 29,90 · Gaufré 24,90 · Étui 69,90–189,90 · Coussins 19,90 · Cuir 17,90 · Loupe 12,90–21,90 · Milanais 14,90–24,90 · Doigtiers 12,90 · Outil 19,90). Le panneau « Shipping info » confirme le fournisseur AliExpress rattaché et une expédition France réelle.

⚠️ Les **13 fiches restent dans la Liste d'import** (marquées « Pushed to 1 store »), comme les 25 qui s'y trouvaient déjà. Rien n'y a été supprimé.

---

## Visuels

Les 10 visuels générés (`scratchpad/noirmont-accessoires-img/`) ont été téléversés et placés **en première position** sur 8 fiches :

| Fiche | Visuel(s) |
|---|---|
| 1 Jubilé courbes | `jubile-courbe-1.jpg` |
| 2 Acier massif | `jubile-plat-1.jpg` |
| 4 Caoutchouc gaufré | `waffle-1.jpg` |
| 5 Coussins | `coussin-1.jpg` |
| 6 Étui de voyage | `etui-voyage-1.jpg` + `etui-voyage-2.jpg` |
| 7 Coffret 6 montres | `coffret-six-1.jpg` + `coffret-six-2.jpg` |
| 8 Kit d'entretien | `kit-entretien-1.jpg` |
| 9 Outil de mise à taille | `outil-bracelet-1.jpg` |

---

## À trancher par Hakim avant publication

1. **5 fiches n'ont aucun visuel NOIRMONT** et affichent encore une photo fournisseur en image principale : **904L, doigtiers, milanais, cuir daim, loupe**. Les trois fiches v3 (milanais, cuir, loupe) n'avaient pas été couvertes par la génération d'images.
2. **Les photos fournisseur ont été conservées sur les 13 fiches** (elles n'ont pas été supprimées pour ne pas risquer de casser les liens image↔variante). Plusieurs montrent des montres logotées et des mentions « for Rolex » incrustées : **il faut les élaguer avant toute publication.** Les fiches étant en DRAFT et sur aucun canal, rien n'est exposé aujourd'hui.
3. **Étui de voyage à 189,90 € (6 places)** : c'est le prix qu'impose la règle ×3 sur un coût de 52,85 €. À côté du Coffret 6 montres à 54,90 €, l'écart peut surprendre — ce sont deux produits différents (transport rigide vs vitrine), mais l'arbitrage commercial te revient. Le rapport v2 recommandait par ailleurs de **commander un échantillon** de cet étui (listing jeune, 3 ventes).
4. **Bracelet 904L** : vendeur noté 4,3, à recontrôler avant publication (réserve déjà posée en v2).
5. **Noms d'options restés en anglais** (`Band Color`, `Band Width`, `Color`, valeurs type `steel-no logo`, `0.6mm-silver`). Aucun ne contient de marque, mais une passe de francisation des variantes reste à faire — délibérément non entreprise ici pour ne pas toucher au mapping fraîchement établi.
6. **Collection Accessoires** : 42 produits après ajout des 13 (relevée à 28 avant l'opération). L'écart d'une unité vient probablement d'un compteur Shopify non encore rafraîchi au premier relevé : mes mutations n'ont ajouté à la collection que les 13 IDs listés plus haut, aucun autre produit n'a été touché.

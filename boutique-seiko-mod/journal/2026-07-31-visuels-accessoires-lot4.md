# Visuels accessoires — lot 4 (NOIRMONT)

Date : 2026-07-26 · Boutique : Maison Noirmont (`v42pzp-h4`, maisonnoirmont.fr) · Compte DSers : `contact.noirmont`
Suite de `2026-07-31-import-accessoires-lot4.md`. Objet : doter les 13 fiches accessoires d'un visuel NOIRMONT et retirer les photos fournisseur.

**Les 13 fiches restent en DRAFT, sur aucun canal.** Aucun SKU, prix, titre, option, statut ni mapping DSers n'a été touché. Aucune commande, aucun achat, aucun identifiant saisi.

---

## Étape 0 — budget

| | |
|---|---|
| Solde Higgsfield avant | **375,46 crédits** (plan Plus) |
| Solde après | **355,46 crédits** |
| Consommé | **20 crédits** — 5 visuels × 4 crédits, aucune reprise nécessaire |

Le budget couvrait largement les 5 visuels (~27 crédits budgétés avec marge de reprise). Feu vert donné, série lancée d'un bloc.

---

## Le défaut constaté

Contrôle visuel des sources fournisseur avant travail. Le défaut était **plus large que « quelques montres logotées »** :

| Fiche | Ce que montraient les photos fournisseur |
|---|---|
| Bracelet Jubilé 904L | **deux cadrans de montre de marque tierce en pleine image** (GMT bicolore rouge/bleu), plus un bandeau « silvery / Delivery of installation tools » |
| Bracelet milanais | surimpression « 0.6mm **1.0mm** Milanese Mesh » + vignette détourée |
| Bracelet cuir daim | « Soft Genuine Leather », « 18/19/20/22mm Stitching Vintage Suede Strap », cotes fléchées en millimètres |
| Loupe d'horloger | « 3X 5X 10X 15X 20X » + filigranes « HQstrap Choice Store » sur le produit |
| Doigtiers latex | « 30/50/100 pcs » + une main nue en gros plan |

---

## Méthode

**Produire d'abord, retirer ensuite** — respecté à la lettre : aucune photo fournisseur n'a été supprimée avant que le visuel de remplacement soit en ligne, en statut `READY`, et vérifié.

1. **Nettoyage de la source.** Plutôt que de compter sur le prompt pour ignorer les parasites, chaque photo fournisseur retenue a été **masquée** (aplats sur les vignettes, bandeaux, cotes et filigranes) et, pour les doigtiers, **recadrée** pour exclure la main. Le modèle n'a donc jamais vu un cadran de marque tierce.
2. **Génération** en image-to-image depuis cette source nettoyée, `nano_banana_pro` en **4K** (4096×4096 natifs), 1:1.
3. **Contrôle de stérilité en zoom** sur chaque image, en particulier les fermoirs, le corps de la loupe et les surpiqûres. Aucun inpainting — la consigne était de régénérer en cas de défaut ; aucune régénération n'a été nécessaire.
4. **Conversion catalogue** : 2048×2048, JPEG qualité 90.
5. **Branchement** : `stagedUploadsCreate` → `PUT` → `productCreateMedia` avec texte alternatif.

**Modèles proscrits respectés** : ni `soul_2` (fabrique de faux logos), ni `openai_hazel` (réinvente l'objet).

---

## Les 5 visuels produits

Direction artistique identique au reste du catalogue : fond minéral clair uni (pierre `#E7E4DE` → craie `#FAFAF7`), lumière douce latérale haute gauche, ombre portée diffuse, produit seul centré, studio éditorial premium.

| # | Fiche | Fichier | Média Shopify | Contrôle stérilité |
|---|---|---|---|---|
| 3 | Bracelet Jubilé acier 904L — 20 mm | `noirmont-jubile-904l-1.jpg` | 59691949195602 | fermoir déployant nu, aucune gravure ✓ |
| 10 | Doigtiers d'horloger — latex | `noirmont-doigtiers-1.jpg` | 59691949228370 | latex nu, aucune main, aucun texte ✓ |
| 11 | Bracelet milanais — maille italienne | `noirmont-milanais-1.jpg` | 59691949261138 | fermoir brossé vierge ✓ |
| 12 | Bracelet cuir daim — dégagement rapide | `noirmont-cuir-daim-1.jpg` | 59691949293906 | daim et surpiqûre nus, aucune cote ✓ |
| 13 | Loupe d'horloger | `noirmont-loupe-1.jpg` | 59691949359442 | corps noir vierge, aucun grossissement imprimé ✓ |

Tous en statut `READY`, 2048×2048. Sources locales : `scratchpad/noirmont-accessoires-img/`, générations 4K conservées dans `scratchpad/lot4-qa/`.

**Aucun bracelet n'est photographié sur une montre** — tous sont cadrés seuls, ce qui rend la question du cadran stérile sans objet.

---

## Texte alternatif

Format « `<Produit>` — `<variante ou matière>` — Maison Noirmont » appliqué aux **15 visuels NOIRMONT conservés** (les 5 nouveaux + les 10 déjà en place, qui portaient une description libre et ont été normalisés).

---

## Planche de contrôle

`scratchpad/noirmont-accessoires-img/_PLANCHE-CONTROLE-13.jpg` — les 13 visuels de tête côte à côte.

Cadrage, fond et lumière homogènes sur les 13 ; les 5 nouveaux se posent dans la grille Accessoires sans détonner. Contrôle complémentaire sur la fiche 2 (visuel préexistant) : ce qui ressemblait à un marquage sur le fermoir est le mécanisme déployant et ses deux vis — aucun texte.

---

## Purge des photos fournisseur

### Contrôle du partage — fait avant, pas supposé

Le brief prévenait que `productDeleteMedia` **détache** un fichier partagé mais **supprime** un fichier non partagé. Balayage en lecture seule des **99 produits** de la boutique, extraction du nom de fichier de chaque média, croisement avec la liste du lot.

**Résultat : aucun des fichiers du lot n'est porté par une autre fiche.** Chacun n'existe que sur sa propre fiche — la suppression n'a donc rien pu casser ailleurs.

Le contrôle n'était pas de pure forme : le partage de fichiers **existe bel et bien** dans cette boutique (`gmt-7.jpg` est porté par 3 fiches `voyageur-*`, `10977444528466-7.jpg` par une douzaine de fiches `contre-la-montre-*`, et de même pour les familles `integrale-*` et `heritage-*`). Le test avait un sens ; il ressort négatif sur ce lot.

### ⚠️ Écart avec le rapport d'import : 186 photos fournisseur, pas 173

Le premier inventaire en donnait 173. Il était **tronqué** : la requête plafonnait à 30 médias par fiche et `bracelet-caoutchouc-gaufre` en portait 43. **13 photos fournisseur y étaient invisibles** et auraient survécu à la purge. Détecté au balayage, vérifié par `mediaCount` sur les 13 fiches, puis corrigé.

Compte réel avant purge : **201 médias = 15 NOIRMONT + 186 fournisseur.**

### Sauvegarde

`scratchpad/backup-medias-accessoires-lot4/` — **186 fichiers, 15 Mo**, classés par handle, avec `INVENTAIRE.txt` (handle · mediaId · nom de fichier). Téléchargement intégral vérifié avant la première suppression : 186/186, aucun échec, aucun fichier tronqué.

### Retraits par fiche

| # | Fiche | Fournisseur retirés | Médias restants |
|---|---|---:|---:|
| 1 | Bracelet Jubilé — embouts courbes | 9 | 1 |
| 2 | Bracelet acier massif — 12 à 22 mm | 12 | 1 |
| 3 | Bracelet Jubilé acier 904L — 20 mm | 6 | 1 |
| 4 | Bracelet caoutchouc gaufré | **42** | 1 |
| 5 | Coussins de présentation — lot de 10 | 11 | 1 |
| 6 | Étui de voyage rigide | 15 | 2 |
| 7 | Coffret 6 montres — couvercle verre | 6 | 2 |
| 8 | Kit d'entretien — 13 pièces | 10 | 1 |
| 9 | Outil de mise à taille de bracelet | 8 | 1 |
| 10 | Doigtiers d'horloger — latex | 12 | 1 |
| 11 | Bracelet milanais — maille italienne | 14 | 1 |
| 12 | Bracelet cuir daim — dégagement rapide | 22 | 1 |
| 13 | Loupe d'horloger | 19 | 1 |
| | **Total** | **186** | **15** |

Aucun `mediaUserErrors` sur les 13 mutations.

### Vérification finale

Relecture des 13 fiches après purge : **statut DRAFT, `publishedAt: null`, aucune image fournisseur, uniquement des visuels NOIRMONT en 2048×2048, tous en statut `READY`, tous avec un texte alternatif au format demandé.**

---

## État DSers

Relevé dans le Chrome de Hakim, session `contact.noirmont` déjà ouverte, **aucun identifiant saisi**.

Relevé effectué **après le branchement des visuels, avant la purge** :

| Compteur | Attendu | Relevé |
|---|---|---|
| Mes Produits — Tous | 98 | **98** ✓ |
| Mes Produits — AliExpress | 98 | **98** ✓ |
| Mes Produits — Unmapped | 0 | **0** ✓ |
| 1688 Dropshipping / Alibaba | 0 / 0 | **0 / 0** ✓ |

Les 13 fiches du lot apparaissaient avec leurs titres français, leurs prix et leurs coûts fournisseur inchangés.

⚠️ **La session DSers a expiré pendant l'opération** : la contre-vérification après purge n'a pas pu être faite. Conformément à la consigne, **aucune tentative de connexion** n'a été faite — à reprendre par Hakim d'un simple rafraîchissement.

Ce contrôle est de confort : la purge n'a touché que des **médias** Shopify. Aucun SKU, aucune variante, aucun prix, aucun titre, aucune option n'a été modifié, et le mapping DSers ne dépend pas des images. Les compteurs n'ont aucune raison mécanique d'avoir bougé.

---

## Reste à trancher par Hakim

Les points ouverts du rapport d'import qui ne relèvent pas du visuel restent entiers :

1. **Une seule image par fiche** (deux pour l'étui et le coffret). Les fiches sont propres mais maigres — une galerie de 3-4 visuels par accessoire reste à produire avant publication.
2. **Étui de voyage à 189,90 €** (6 places) face au Coffret 6 montres à 54,90 € : arbitrage commercial en suspens.
3. **Bracelet 904L** : vendeur noté 4,3, à recontrôler avant publication.
4. **Noms d'options en anglais** (`Band Color`, `steel-no logo`…) : francisation non entreprise pour ne pas toucher au mapping.
5. Les 13 fiches **restent dans la Liste d'import DSers** (« Pushed to 1 store »).

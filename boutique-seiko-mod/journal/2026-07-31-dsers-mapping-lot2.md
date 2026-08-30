---
type: journal
boutique: seiko-mod
date: 2026-07-31
nature: intervention
leviers: [sourcing, catalogue]
titre: "DSers — mapping des 41 fiches du lot 2 (découpage / élagage)"
---

# DSers — mapping des 41 fiches du lot 2 (découpage / élagage)
Boutique NOIRMONT (Shopify `v42pzp-h4`, Maison Noirmont) — 25-26/07/2026
Compte DSers : `contact.noirmont`

> **État final : les 41 fiches sont mappées et enregistrées. 89 / 89 variantes couvertes. Onglet `Unmapped` à 0.**
> Aucune des 44 fiches déjà mappées n'est repassée en « Unmapped ».

---

## État à l'ouverture (vérifié à l'écran)

| Indicateur | Valeur |
|---|---|
| Mes Produits / `Tous` | **44** |
| `AliExpress` (= mappés) | **44** |
| `1688 Dropshipping` / `Alibaba` | 0 / 0 |
| `Unmapped` | **0** |
| Liste d'import | 25 |

Conforme à l'état laissé par la passe précédente (25 historiques + 19 filles du lot 1).

## Synchronisation — FAITE et vérifiée

Bouton **« IMPORT PRODUCTS FROM SHOPIFY »**, filtre **« À être importé »**.
Ce filtre listait **exactement 41 entrées**, toutes identifiées une à une comme les 41 fiches du lot 2 —
aucune fiche étrangère. Import en **5 lots** (limite DSers : 10 par lot) : 10 + 10 + 10 + 10 + 1 = 41.

| Indicateur | Avant | Après import | Lecture |
|---|---|---|---|
| `Tous` | 44 | **85** | 44 + 41 = 85 ✔ |
| `AliExpress` | 44 | **44** | inchangé ✔ aucune fiche historique démappée |
| `Unmapped` | 0 | **41** | les 41 filles ✔ |
| Liste d'import | 25 | 25 | inchangé ✔ |

---

## Les 7 URL fournisseur

Relevées sans deviner : chaque fiche mère porte un `supplyProductId` dans la réponse de l'API interne
DSers `dsers-product-bff/my-product/v2/search`, lue **en observation passive** du trafic de la page
(aucune requête forgée, aucune écriture). Recoupement indépendant : l'onglet AliExpress laissé ouvert par
Hakim pointait `1005006938556690`, soit exactement le fournisseur trouvé pour le Remontoir Collection.

| Mère | Titre fournisseur (lu dans DSers) | URL |
|---|---|---|
| **Contre-la-montre — Chronographe panda** | 20 color Business 39mm Quartz Watch Men's Timing Sapphire Crystal VK63 | `https://fr.aliexpress.com/item/1005004821593794.html` |
| **Voyageur — GMT automatique** | BLIGER Custom 40MM Full Rose Rootbeear Watch For Men GMT Automatic | `https://fr.aliexpress.com/item/1005009740849403.html` |
| **Intégrale — Sport chic acier** | NH35 High-Quality Nautilus Style Waterproof Stainless Steel Men's | `https://fr.aliexpress.com/item/1005009821439225.html` |
| **Héritage — Plongeuse vintage 42** | SKX007 Watch Vintage Diving Mechanical 5ATM 42mm Stainless Steel Case | `https://fr.aliexpress.com/item/1005008657937411.html` |
| **Remontoir Bois** | Embers Luxury Wooden Watch Box Single Winder with Glass Storage | `https://fr.aliexpress.com/item/1005012102224533.html` |
| **Rouleau de Voyage — cuir** | Embers Leather Watch Roll 1 2 3 Slots Luxury Genuine Watch Storage Box | `https://fr.aliexpress.com/item/1005008493748701.html` |
| **Remontoir Collection — 2 à 6 montres** | IBBETON Luxury Wood Watch Winder High-End 2 4 6 Slots Automatic | `https://fr.aliexpress.com/item/1005006938556690.html` |

Le titre fournisseur affiché dans le panneau a été **relu à chaque fiche** avant appariement, et le
`supplyProductId` de chacune des 41 fiches a été **recontrôlé en fin de passe** contre cette table :
**41 / 41 exacts, aucune fiche sans fournisseur, aucun fournisseur surnuméraire.**

---

## Table de correspondance des 89 SKU

Construite en **lecture seule** via l'API Admin Shopify (`products { variants { title sku } }`) sur les 41
fiches, puis **recoupée avec la sauvegarde indépendante `backup-variantes-avant-decoupage.json`** :
libellés et ordre identiques sur les 7 familles. **Aucun SKU n'a été écrit ni modifié.**

### Structure des SKU par famille

| Famille | Attributs du SKU | Traduction en mapping DSers |
|---|---|---|
| Chronographe | `14:<id>#<label>` | 1 seule option fournisseur : `Color` |
| GMT | `14:<id>#<coloris>` + `5:<id>#<mouvement>` | `Size` = les 4 mouvements ; `Color` = coloris fixé par la fille |
| Intégrale | `14:<id>#<n>` + `200007763:201336100` | `Color` = coloris fixé ; `Ships From` = `China Mainland` (valeur unique) |
| Héritage | `14:<id>#S1..S3` + `5:…#42mm` | `Color` = coloris fixé ; `Size` = `42mm` |
| Remontoir Bois · Rouleau · Remontoir Collection | `14:<id>#<label>` | 1 seule option fournisseur : `Color` |

### Chronographe — 12 fiches / 20 variantes (`Color`)

| Fiche | Variante Shopify | Label fournisseur |
|---|---|---|
| Contre-la-montre Blanc | Compteurs cerclés · bracelet acier | `M-1` |
| | Compteurs gris · bracelet acier | `M8` |
| | Ton sur ton · bracelet caoutchouc | `M-5` |
| Contre-la-montre Panda inversé | Acier / Rouge | `M-2` / `M18` |
| Contre-la-montre Champagne | Acier / Caoutchouc noir | `M-3` / `M-4` |
| Contre-la-montre Panda | Blanc · caoutchouc noir / Ivoire · aiguille rouge · acier | `M-6` / `M19` |
| Contre-la-montre Noir | Intégrale lisse / Tachymètre inscrit | `M-7` / `M17` |
| Contre-la-montre Turquoise | Ton sur ton / Noirs contrastés | `M10` / `M16` |
| Contre-la-montre Vert | Caoutchouc vert / Acier | `M11` / `M12` |
| Contre-la-montre Rose poudré | Rose poudré | `M9` |
| Contre-la-montre Gris anthracite | Gris anthracite | `M13` |
| Contre-la-montre Argent | Argent · caoutchouc noir | `M14` |
| Contre-la-montre Compteurs bleus | Compteurs bleus · bracelet bleu | `M15` |
| Contre-la-montre Bleu glacier | Bleu glacier | `M20` |

Liste fournisseur complète relevée à l'écran (20 valeurs, ordre exact) :
`M14 · M19 · M20 · M-2 · M9 · M17 · M10 · M-1 · M13 · M16 · M15 · M18 · M8 · M11 · M12 · M-5 · M-3 · M-6 · M-7 · M-4`
— identique à la sauvegarde.

### GMT — 6 fiches / 24 variantes
`Size` identique aux 6 fiches, dans l'ordre Shopify :
`DG3804 GLASS back` · `DG3804 SOLID back` · `NH34 GLASS back` · `NH34 SOLID back`

| Fiche | `Color` |
|---|---|
| Voyageur Or — GMT bracelet 3 maillons | `9` |
| Voyageur Or — GMT bracelet Président | `7` |
| Voyageur Bicolore — GMT bracelet 3 maillons | `6` |
| Voyageur Bicolore — GMT bracelet 5 maillons | `2` |
| Voyageur Or rose — GMT bracelet 5 maillons | `1` |
| Voyageur Bicolore cadran brun — GMT automatique | `4` |

Les 3 coloris « siglés » (`3`, `5`, `8`) n'apparaissent dans aucune fiche — conforme au découpage.

### Intégrale — 7 fiches / 7 variantes (`Color` + `Ships From = China Mainland`)

| Fiche | `Color` |
|---|---|
| Intégrale Vert | `6` |
| Intégrale Brun or rose | `7` |
| Intégrale Turquoise | `1` |
| Intégrale Noir | `4` |
| Intégrale Bleu nuit | `5` |
| Intégrale Bleu ciel | `2` |
| Intégrale Blanc argenté | `3` |

### Héritage — 3 fiches / 3 variantes (`Color` + `Size = 42mm`)

| Fiche | `Color` |
|---|---|
| Héritage Bleu | `S1` |
| Héritage Bleu nuit | `S2` |
| Héritage Vert | `S3` |

### Remontoir Bois — 4 fiches / 8 variantes (`Color`)

| Fiche | 1 montre | 2 montres |
|---|---|---|
| Remontoir Bois Noir laqué | `M11011` | `M12011` |
| Remontoir Bois Acajou | `M11032` | `M12032` |
| Remontoir Bois Ébène | `M11052` | `M12052` |
| Remontoir Bois Noyer | `M11071` | `M12071` |

### Rouleau de Voyage — 4 fiches / 12 variantes (`Color`)

| Fiche | 1 | 2 | 3 |
|---|---|---|---|
| Rouleau de Voyage Noir | `WB11` | `WB12` | `WB13` |
| Rouleau de Voyage Brun | `WB21` | `WB22` | `WB23` |
| Rouleau de Voyage Bleu marine | `WB31` | `WB32` | `WB33` |
| Rouleau de Voyage Vert | `WB41` | `WB42` | `WB43` |

### Remontoir Collection — 5 fiches / 15 variantes (`Color`)

| Fiche | Variantes |
|---|---|
| Remontoir Collection Bois noir | 1→`IB-black-01A` · 2→`IB-black-02A` · 4→`IB-black-04A` · 6→`IB-black-06A` |
| Remontoir Collection Bois beige | 1→`IB-white-01A` · 2→`IB-white-02A` · 4→`IB-white-04A` · 6→`IB-white-06A` |
| Remontoir Collection Bois LED noir | 2→`IB-black-02C` · 4→`IB-black-04C` |
| Remontoir Collection Bois LED rouge | 2→`IB-red-02C` · 4→`IB-red-04C` |
| Remontoir Collection Cuir PU | 2→`IB-PU leather-02B` · 4→`IB-PU leather-04B` · 6→`IB-PU leather-06B` |

**Total : 20 + 24 + 7 + 3 + 8 + 12 + 15 = 89 ✔**

---

## Méthode retenue

**Confirmé une seconde fois : l'auto-matching par SKU n'existe pas.** Coller l'URL rattache le bon produit
fournisseur mais laisse toutes les variantes vides. L'appariement est fait **à la main, en Mapping basique**.

**Aucune sélection par coordonnées.** Chaque valeur est choisie en localisant dans le DOM l'option dont le
texte est **strictement égal** au label visé (`===`, jamais `includes`), puis en cliquant cet élément-là.
Refus explicite et arrêt si le nombre de correspondances ≠ 1. Après chaque sélection, le libellé
effectivement retenu est **relu et comparé à la cible** ; toute divergence bloque l'enregistrement.

Cela neutralise les confusions dangereuses : `M-1` ≠ `M11` ≠ `M12`, `M-5` ≠ `M15`, `M-2` ≠ `M20`,
et surtout `IB-black-02A` (Bois noir) ≠ `IB-black-02C` (LED noir) — vérifié explicitement au contrôle final.

---

## ⚠️ Trois pièges découverts dans cette passe — à relire avant toute reprise

### 1. Les listes de valeurs sont **virtualisées**
Le menu ne rend que **9 options sur 20**. Une recherche naïve conclut « valeur absente » : `M8` et `M-5`
paraissaient introuvables alors qu'elles existaient. Il faut **parcourir toute la liste en la faisant
défiler**, et — point non évident — **émettre un événement `scroll`** après avoir modifié `scrollTop`,
sinon la liste ne re-rend rien. Les sélecteurs sont en lecture seule : **aucune saisie ne les filtre**.

### 2. Le bouton `Enregistrer` ne suffit pas
Il ouvre une boîte **« Appliquer le mapping »** qu'il faut confirmer (`CONFIRMER`). Sans cela on croit
avoir enregistré alors que rien n'est écrit. L'enregistrement n'est réputé fait que lorsque le bouton
`Enregistrer` repasse **désactivé**, et il est recontrôlé par les compteurs d'onglets.

### 3. Onglet en arrière-plan = minuteries bridées par Chrome
Quand l'onglet DSers n'est pas au premier plan (`document.hidden === true`), Chrome ramène `setTimeout`
à **un déclenchement par minute**. Toute automatisation qui attend entre deux actions se fige et paraît
plantée. Parade : temporiser via un `MessageChannel` (non bridé) plutôt que `setTimeout` seul.

À noter aussi : le panneau de mapping garde parfois une **position d'animation décalée** après un
redimensionnement de fenêtre — il est bien vivant et opérationnel, seulement invisible.
Et sur les fiches **déjà mappées**, la carte n'expose plus la classe `sc_above_mapping_btn` : le bouton
de mapping est le **second `.sc_above_Btn`** de la carte.

---

## Tableau des 41 fiches

Variantes « mappées » = valeurs d'options effectivement liées en Mapping basique.
Contrôle SKU = libellé fournisseur retenu relu et comparé à la table ci-dessus.

| Fiche | Mère | Variantes mappées / attendues | Contrôle SKU | Remarque |
|---|---|---|---|---|
| Contre-la-montre Blanc — Chronographe | Chronographe | **3 / 3** | OK | contrôle visuel + relecture après enregistrement |
| Contre-la-montre Panda inversé — Chronographe | Chronographe | **2 / 2** | OK | |
| Contre-la-montre Champagne — Chronographe | Chronographe | **2 / 2** | OK | |
| Contre-la-montre Panda — Chronographe | Chronographe | **2 / 2** | OK | |
| Contre-la-montre Noir — Chronographe | Chronographe | **2 / 2** | OK | |
| Contre-la-montre Turquoise — Chronographe | Chronographe | **2 / 2** | OK | |
| Contre-la-montre Vert — Chronographe | Chronographe | **2 / 2** | OK | |
| Contre-la-montre Rose poudré — Chronographe | Chronographe | **1 / 1** | OK | |
| Contre-la-montre Gris anthracite — Chronographe | Chronographe | **1 / 1** | OK | |
| Contre-la-montre Argent — Chronographe | Chronographe | **1 / 1** | OK | |
| Contre-la-montre Compteurs bleus — Chronographe | Chronographe | **1 / 1** | OK | |
| Contre-la-montre Bleu glacier — Chronographe | Chronographe | **1 / 1** | OK | |
| Voyageur Or — GMT bracelet 3 maillons | GMT | **4 / 4** | OK | `Size` ×4 + `Color 9` |
| Voyageur Or — GMT bracelet Président | GMT | **4 / 4** | OK | `Color 7` |
| Voyageur Bicolore — GMT bracelet 3 maillons | GMT | **4 / 4** | OK | `Color 6` |
| Voyageur Bicolore — GMT bracelet 5 maillons | GMT | **4 / 4** | OK | `Color 2` |
| Voyageur Or rose — GMT bracelet 5 maillons | GMT | **4 / 4** | OK | `Color 1` |
| Voyageur Bicolore cadran brun — GMT automatique | GMT | **4 / 4** | OK | `Color 4` — relu après enregistrement |
| Intégrale Vert — Sport chic acier | Intégrale | **1 / 1** | OK | `Color 6` + `Ships From` |
| Intégrale Brun or rose — Sport chic | Intégrale | **1 / 1** | OK | `Color 7` |
| Intégrale Turquoise — Sport chic acier | Intégrale | **1 / 1** | OK | `Color 1` |
| Intégrale Noir — Sport chic acier | Intégrale | **1 / 1** | OK | `Color 4` |
| Intégrale Bleu nuit — Sport chic acier | Intégrale | **1 / 1** | OK | `Color 5` |
| Intégrale Bleu ciel — Sport chic acier | Intégrale | **1 / 1** | OK | `Color 2` |
| Intégrale Blanc argenté — Sport chic acier | Intégrale | **1 / 1** | OK | `Color 3` |
| Héritage Bleu — Plongeuse vintage 42 | Héritage | **1 / 1** | OK | `S1` + `42mm` — relu après enregistrement |
| Héritage Bleu nuit — Plongeuse vintage 42 | Héritage | **1 / 1** | OK | `S2` + `42mm` — relu après enregistrement |
| Héritage Vert — Plongeuse vintage 42 | Héritage | **1 / 1** | OK | `S3` + `42mm` — contrôle visuel |
| Remontoir Bois Noir laqué | Remontoir Bois | **2 / 2** | OK | |
| Remontoir Bois Acajou | Remontoir Bois | **2 / 2** | OK | |
| Remontoir Bois Ébène | Remontoir Bois | **2 / 2** | OK | |
| Remontoir Bois Noyer | Remontoir Bois | **2 / 2** | OK | |
| Rouleau de Voyage Noir — cuir | Rouleau | **3 / 3** | OK | |
| Rouleau de Voyage Brun — cuir | Rouleau | **3 / 3** | OK | 1re tentative interrompue avant tout enregistrement (grille non rafraîchie), refaite |
| Rouleau de Voyage Bleu marine — cuir | Rouleau | **3 / 3** | OK | |
| Rouleau de Voyage Vert — cuir | Rouleau | **3 / 3** | OK | |
| Remontoir Collection Bois noir | Remontoir Collection | **4 / 4** | OK | suffixe `…A` |
| Remontoir Collection Bois beige | Remontoir Collection | **4 / 4** | OK | |
| Remontoir Collection Bois LED noir | Remontoir Collection | **2 / 2** | OK | `…02C`/`…04C` — **relu après enregistrement**, ≠ `…02A` |
| Remontoir Collection Bois LED rouge | Remontoir Collection | **2 / 2** | OK | |
| Remontoir Collection Cuir PU | Remontoir Collection | **3 / 3** | OK | |

**Total : 41 / 41 fiches — 89 / 89 variantes.**

---

## Contrôle final (vérifié à l'écran et via l'API interne DSers)

| Indicateur | Avant mapping | **Après mapping** | Lecture |
|---|---|---|---|
| `Tous` / Mes Produits | 85 | **85** | inchangé ✔ |
| `AliExpress` (= mappés) | 44 | **85** | 44 + 41 = 85 ✔ |
| `Unmapped` | 41 | **0** | plus aucune fiche non mappée ✔ |
| `1688 Dropshipping` / `Alibaba` | 0 / 0 | **0 / 0** | inchangé ✔ |
| Liste d'import | 25 | **25** | inchangé ✔ |

Le passage de `AliExpress` de 44 à 85, soit **exactement +41**, confirme qu'aucune des 44 fiches
historiques n'a été démappée.

Contrôles supplémentaires :
- **Les 85 fiches ont exactement un fournisseur** — aucune à zéro, aucune à deux.
- **Les 41 fiches du lot 2 portent le `supplyProductId` attendu de leur mère** : 41 / 41 exacts,
  0 divergence, 0 absente (comparaison automatique contre la table des 7 URL).
- **7 fiches rouvertes après enregistrement** pour relire le mapping persisté : Héritage Bleu,
  Héritage Bleu nuit, Héritage Vert, Contre-la-montre Blanc, Voyageur Bicolore cadran brun,
  Remontoir Collection Bois LED noir, Contre-la-montre Panda inversé — toutes conformes.

---

## Incidents rencontrés

1. **Indisponibilité de plateforme d'environ 40 minutes** sur l'outil d'exécution JS dans Chrome.
   Arrêt **entre deux fiches**, aucun panneau laissé ouvert avec des modifications non enregistrées.
   Reprise sans perte. La méthode n'a pas été dégradée en clics par coordonnées.

2. **Trois cycles interrompus avant tout enregistrement** — deux par le bridage des minuteries en
   arrière-plan (voir piège 3), un parce que la carte n'était pas encore rendue dans la grille
   (« Rouleau de Voyage Brun »). Dans les trois cas le garde-fou a stoppé la série plutôt que de risquer
   un appariement erroné, et les fiches ont été refaites intégralement. **Aucun mapping faux enregistré.**

3. **Boîte « Unsaved changes »** rencontrée 3 fois, toujours sur une fiche dont le mapping était correct :
   **ENREGISTRER** cliqué, jamais IGNORER. Aucun travail juste n'a été jeté.

---

## Règles respectées

- **Aucun SKU modifié**, ni dans Shopify ni dans DSers. Les SKU n'ont été que **lus** (API Admin Shopify,
  lecture seule) pour construire la table de correspondance.
- **Aucune des 44 fiches historiques touchée** : compteur `AliExpress` passé de 44 à 85, soit +41 exactement.
- **Aucun « × » de suppression de fournisseur cliqué.** Aucun clic sur « Pousser vers la boutique ».
- **Aucune commande passée**, aucun bouton d'achat / paiement touché.
- **Aucun identifiant saisi** ; la session `contact.noirmont` était déjà ouverte.
- Case « Ignorer Définitivement » du choix de méthode laissée **décochée** (aucune préférence persistante).
- Aucune requête forgée vers l'API DSers : les identifiants fournisseur ont été lus en **observation
  passive** des réponses que la page recevait déjà.

---

## Reste à faire (hors périmètre de cette passe)

1. **69 visuels à produire** (voir `PROMPT-CODEX-reprise-visuels.md`), dont les 41 images de tête.
2. **Relire les 8 `alt` reconstruits** (positions 3 et 4 des 4 galeries montres).
3. **Trancher la description du GMT** : « plusieurs lunettes bicolores au choix » ne convient plus aux
   6 fiches mono-boîtier.
4. **Retirer « Tandorio CUSN8 » des favoris** de la fiche *Quarante-et-Un Noir — Sport cuir* (hérité de la
   passe précédente ; inoffensif, ce n'est ni le fournisseur par défaut ni celui de secours).
5. **Noirmont Deux** toujours en attente ; **12 variantes GMT siglées** toujours sur la mère en `DENY` / stock 0.

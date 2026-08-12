# DSers — mapping des 19 fiches issues du découpage par coloris
Boutique NOIRMONT (Shopify `v42pzp-h4`, Maison Noirmont) — 25/07/2026
Compte DSers : `contact.noirmont`

> **État final : les 19 fiches sont mappées et enregistrées. 92 / 92 variantes couvertes. Onglet `Unmapped` à 0.**

## État à l'ouverture (vérifié)

- **Mes Produits : 25** — les produits historiques importés par DSers. Onglet `Unmapped (0)` : les 25 étaient tous mappés.
- **Aucune des 19 nouvelles fiches n'y figurait.** Les 25 ont été énumérées une à une (2 pages) : les 5 mères y sont, aucune fille.
- **Liste d'import : 25** — ce sont les fiches fournisseur AliExpress brutes (titres AliExpress, toutes « Pushed to 1 store(s) »). Les filles n'y étaient pas non plus.
- Cause confirmée : les 19 fiches ayant été créées via l'API Shopify, DSers ne les avait jamais vues.

## Synchronisation — FAITE et vérifiée

Mécanisme utilisé : bouton **« IMPORT PRODUCTS FROM SHOPIFY »** (Mes Produits, en haut à droite).
C'est le mécanisme sûr : **additif et produit par produit**, il tire des fiches Shopify vers DSers sans rien réécrire côté Shopify et sans toucher aux mappings existants.

Import réalisé en 4 lots (limite DSers : 10 par lot) : 5 + 5 + 5 + 4 = 19.

| Indicateur | Avant | Après import | Lecture |
|---|---|---|---|
| Mes Produits | 25 | **44** | 25 + 19 = 44 ✔ |
| Onglet `AliExpress` (= mappés) | 25 | **25** | inchangé ✔ |
| Onglet `Unmapped` | 0 | **19** | les 19 filles, non mappées ✔ |

## Les 5 URL fournisseur — utilisées

| Mère | Produit fournisseur AliExpress (titre lu dans DSers) | URL |
|---|---|---|
| **Trente-Six — Classique jubilé** | Luxury NH35 Mechanical 36mm/39mm Men/ Women Watch 10Bars Jubilee Bracelet | `https://fr.aliexpress.com/item/1005009697365359.html` |
| **Trente-Neuf — Classique cannelée** | 36mm/39mm Fluted Bezel NH35A Automatic Movement Corgeut Men Watch 100m | `https://fr.aliexpress.com/item/1005010776361944.html` |
| **Quarante-et-Un — Sport acier** | Luxury NH35 Corgeut Watch Men Reloj Hombre 41mm Sport Clock Automatic | `https://fr.aliexpress.com/item/1005009622003765.html` |
| **Noirmont Un — Plongeuse acier** | Tandorio CUSN8 Bronze/Stainless Steel 200m Waterproof Pilot PT5000 Japan NH | `https://fr.aliexpress.com/item/1005004626900765.html` |
| **Trente-Neuf Duo — Classique bicolore** | BLIGER 36mm/39mm Fluted Bezel NH35A Automatic Watch For Men Two Tone Gold | `https://fr.aliexpress.com/item/1005006277907428.html` |

Chaque titre fournisseur a été **relu à l'écran** au moment du mapping de chaque fille : les 5 correspondances sont confirmées visuellement, fiche par fiche.

## Méthode de mapping retenue

**L'auto-matching par SKU annoncé n'a pas eu lieu.** En collant l'URL de la mère, DSers rattache bien le bon produit fournisseur mais laisse **toutes les variantes vides** (« Sélectionner des variantes »). Le rapprochement a donc été fait **à la main, option par option**, en mode **Mapping basique**.

Table de correspondance construite au préalable en **lecture seule** via l'API Admin Shopify (`products { variants { title sku } }`) : pour chacune des 19 filles, le SKU AliExpress complet de chaque variante a été extrait, puis décomposé en ses deux attributs (`14:…` = Color, `5:…` = Size). C'est cette table qui a servi de vérité de référence — **aucun SKU n'a été écrit ni modifié**.

Structure du mapping basique appliqué :
- l'option Shopify multi-valeurs (Taille & fond / Mouvement & fond / Mouvement) est mappée sur l'option fournisseur **Size** ;
- l'attribut fixé par le découpage (le coloris de la fille) est mappé globalement sur l'option fournisseur **Color** ;
- exception **Trente-Neuf Duo Doré**, seule fiche à deux options Shopify : `Taille & fond` → Color (2 valeurs) et `Mouvement` → Size (3 valeurs).

**Fiabilisation.** Les listes déroulantes DSers se repositionnent après ouverture : cliquer aux coordonnées lues sur une capture a produit deux erreurs d'appariement (détectées et corrigées, voir Incidents). La méthode retenue ensuite, et utilisée pour la quasi-totalité des fiches, est **déterministe** : ouverture du sélecteur, navigation au clavier (`↓` × index), **vérification de l'option active par lecture du DOM** (`.ant-select-item-option-active`), puis `Entrée`. Chaque libellé retenu a ainsi été confirmé par son texte exact avant validation.

## Tableau des 19 fiches

Variantes « mappées » = produit des valeurs d'options effectivement liées (Mapping basique).

| Fiche | Mère | Variantes mappées / attendues | Contrôle SKU | Remarque |
|---|---|---|---|---|
| Trente-Six Rouge — Classique jubilé | Trente-Six | **4 / 4** | OK | Color `red no logo` (≠ `red corgeut`) |
| Trente-Six Bleu — Classique jubilé | Trente-Six | **4 / 4** | OK | Color `blue no logo` ; 1 ligne corrigée avant enregistrement |
| Trente-Six Rose — Classique jubilé | Trente-Six | **4 / 4** | OK | Color `pink no logo` |
| Trente-Six Doré — Classique jubilé | Trente-Six | **4 / 4** | OK | Color `yellow gold no logo` |
| Trente-Six Or intégral — Classique jubilé | Trente-Six | **4 / 4** | OK | Color `full gold no logo` |
| Trente-Neuf Rouge — Classique cannelée | Trente-Neuf | **8 / 8** | OK | Color `red no logo` ; 1re tentative abandonnée sans enregistrer, refaite intégralement |
| Trente-Neuf Bleu mer — Classique cannelée | Trente-Neuf | **8 / 8** | OK | Color `sea blue no logo` |
| Trente-Neuf Rose — Classique cannelée | Trente-Neuf | **8 / 8** | OK | Color `pink no logo` |
| Trente-Neuf Vert — Classique cannelée | Trente-Neuf | **8 / 8** | OK | Color `green no logo` |
| Trente-Neuf Bleu — Classique cannelée | Trente-Neuf | **8 / 8** | OK | Color `blue no logo` |
| Trente-Neuf Noir — Classique cannelée | Trente-Neuf | **8 / 8** | OK | Color `black no logo` |
| Quarante-et-Un Bleu Acier — Sport acier | Quarante-et-Un | **2 / 2** | OK | Color `Blue Dial M` ; `Miyota 8215` auto-apparié par DSers |
| Quarante-et-Un Noir & Jaune Acier — Sport acier | Quarante-et-Un | **2 / 2** | OK | Color `Black Dial Yellow M` |
| Quarante-et-Un Noir Acier — Sport acier | Quarante-et-Un | **2 / 2** | OK | Color `Black Dial M` |
| Quarante-et-Un Blanc — Sport cuir | Quarante-et-Un | **2 / 2** | OK | Color `White Dial leather` (≠ `White Dia M`) |
| Quarante-et-Un Bleu — Sport cuir | Quarante-et-Un | **2 / 2** | OK | Color `Blue Dial leather` |
| Quarante-et-Un Noir — Sport cuir | Quarante-et-Un | **2 / 2** | OK | Color `Black dial leather` — **vérifié caractère par caractère**, ≠ `Black dial leather M` |
| Noirmont Un Bronze — Plongeuse | Noirmont Un | **6 / 6** | OK | Color `bronze case-no logo` (≠ `bronze case-logo`, ≠ `steel case-…`) |
| Trente-Neuf Duo Doré — Classique bicolore | Trente-Neuf Duo | **6 / 6** | OK | 2 options : `Gold 36mm/39mm glass back` × 3 mouvements |

**Total : 19 / 19 fiches — 92 / 92 variantes** (5×4 + 6×8 + 6×2 + 6 + 6).

Détail des correspondances Size appliquées (identiques pour toutes les filles d'une même mère) :
- **Trente-Six** : `36mm-solid back` · `36mm- glass back` · `39-solid back` · `39mm-glass back`
- **Trente-Neuf** : `8215-36mm(solidback)` · `8215-36mm(glassback)` · `8215-39mm(solidback)` · `8215-39mm(glassback)` · `NH35-36mm(solidback)` · `NH35-36mm(glassback)` · `NH35-39mm(solidback)` · `NH35-39mm(glassback)`
- **Quarante-et-Un** : `Miyota 8215` · `NH35 MOVT`
- **Noirmont Un** : `Miyota82-steel back` · `Miyota82-glass back` · `NH35-steel back` · `NH35-glass back` · `PT5000-steel back` · `PT5000-glass back`
- **Trente-Neuf Duo** : `Miyota8215` · `Mingzhu 2813` · `NH35`

## État final des compteurs DSers (vérifié à l'écran)

| Indicateur | Avant mapping | **Après mapping** | Lecture |
|---|---|---|---|
| Mes Produits | 44 | **44** | inchangé ✔ |
| Onglet `AliExpress` (= mappés) | 25 | **44** | 25 + 19 = 44 ✔ |
| Onglet `Unmapped` | 19 | **0** | plus aucune fiche non mappée ✔ |
| Onglet `1688 Dropshipping` / `Alibaba` | 0 / 0 | **0 / 0** | inchangé ✔ |
| Liste d'import | 25 | **25** | inchangé ✔ |

Le passage de `AliExpress` de 25 à 44, soit **exactement +19**, confirme qu'aucune des 25 fiches historiques n'a été démappée.

## Incidents rencontrés

1. **Aucun auto-matching par SKU.** Contrairement à ce qui était attendu, DSers n'a pré-rempli aucune variante à partir des chaînes d'attributs AliExpress portées par les SKU Shopify. Seules exceptions : quelques libellés strictement identiques des deux côtés (`Miyota 8215`, `Mingzhu 2813`, `NH35`) qu'il a appariés seul sur les familles Quarante-et-Un et Trente-Neuf Duo. Tout le reste a été apparié manuellement.

2. **Menus déroulants instables.** Les listes se repositionnent après leur ouverture ; deux appariements erronés ont été produits par des clics aux coordonnées d'une capture devenue obsolète — l'un sur *Trente-Six Bleu*, l'autre sur *Trente-Neuf Rouge*. **Les deux ont été détectés au contrôle avant enregistrement.** *Trente-Six Bleu* a été corrigé en place ; *Trente-Neuf Rouge* a été **abandonné sans enregistrer** (dialogue « Unsaved changes » → **IGNORER**) puis entièrement refait. Aucun mapping faux n'a été enregistré.

3. **Grille non rafraîchie après enregistrement.** L'onglet `Unmapped` conserve parfois la fiche qu'on vient de mapper. À deux reprises, la fiche déjà mappée a donc été rouverte par erreur :
   - une fois sans conséquence (fermeture par **IGNORER**) ;
   - une fois avec un effet à connaître : l'URL fournisseur de *Noirmont Un* a été collée dans la fiche **Quarante-et-Un Noir — Sport cuir**, ce qui a **ajouté « Tandorio CUSN8 » à la liste des fournisseurs favoris de cette fiche**. DSers a alors proposé d'en faire le fournisseur par défaut : **refusé, dialogue annulé**. Vérification faite dans le panneau « Fournisseurs favoris » : le fournisseur par défaut de cette fiche reste bien `Luxury NH35 Corgeut…` (étiquette « Par défaut »), et son mapping enregistré est intact.
     → **Reste à faire, sans urgence : retirer « Tandorio CUSN8 » des favoris de la fiche *Quarante-et-Un Noir — Sport cuir*.** Non fait ici car la consigne interdisait de cliquer le « × » de suppression d'un fournisseur. Ce favori surnuméraire est inoffensif tant qu'il n'est ni par défaut ni de secours.
   - **Parade adoptée** : recliquer l'onglet `Unmapped` pour forcer le rafraîchissement, et vérifier le titre affiché dans le panneau de mapping avant toute validation.

4. **Dialogue « Unsaved changes ».** Rencontré 3 fois. **IGNORER** systématiquement cliqué, jamais ENREGISTRER, conformément à la consigne.

## Règles respectées

- **Aucun SKU modifié**, ni dans Shopify ni dans DSers. Les SKU n'ont été que **lus** (API Admin Shopify, lecture seule) pour construire la table de correspondance.
- **Aucune des 25 fiches historiques touchée** : compteur `AliExpress` passé de 25 à 44, soit +19 exactement.
- **Aucun « × » de suppression de fournisseur cliqué.** Aucun clic sur « Pousser vers la boutique ».
- **Aucune commande passée**, aucun bouton d'achat/paiement/« Place order » touché.
- **Aucun identifiant saisi** ; la session `contact.noirmont` était déjà ouverte.
- Case « Ignorer Définitivement » du choix de méthode de mapping laissée **décochée** (aucune préférence persistante créée).

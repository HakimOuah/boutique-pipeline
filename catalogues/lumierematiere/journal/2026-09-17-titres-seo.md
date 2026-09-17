# 17/09/2026 (soir) — Contrôle des actions de Hakim, et le trou des titres SEO

Suite de `2026-09-17-correction-veracite.md`. Hakim a fait les trois actions que le connecteur
refuse. Ce journal consigne le contrôle, puis un défaut que ce contrôle a révélé.

## 1. Contrôle des trois actions

### Politiques

Les 5 politiques sont en ligne. Vérifié sur le HTML rendu :

| Terme | Attendu | Constaté |
|---|---|---|
| « Chine » | présent | expédition ×2, remboursement ×1, confidentialité ×2 |
| « fabricant » | présent | expédition ×3, confidentialité ×3 |
| « adresse en France » | présent | expédition ×1, remboursement ×1 |
| « OH Ventures » | présent | 2 à 4 selon la politique |
| Colissimo / DPD | absent | 0 |
| « contrôle du » | absent | 0 |
| `mailto:contact@ohventures.fr` | absent | 0 |
| « 9 h » | absent | 0 (10 h–18 h partout) |

Deux résidus contrôlés et écartés :

- **« Maestro »** apparaît une fois sur **chaque** page : c'est `supportedNetworks` dans la
  configuration JS du wallet Shopify Payments, pas un picto affiché. Maestro est réellement accepté
  par Apple Pay. Rien à corriger.
- **« emball »** ×2 dans la politique de remboursement : « dans son emballage d'origine complet » et
  « Remballez l'article dans son carton d'origine ». C'est le client qui emballe, pas nous.

### Thème

`LM Véracité 2026-09-17` (`187309752656`) est en **`role: MAIN`**. Contrôlé en visiteur :

- **accueil** : « … puis 6 à 16 jours d'acheminement depuis nos fabricants partenaires, en Chine » ;
- **panier** : « préparée en 1 à 2 jours ouvrés si elle arrive avant 16h00, heure de Paris, puis
  expédiée par notre fabricant partenaire depuis la Chine » ;
- **footer** : même phrase dans le bloc livraison ;
- **fiche** : « fabricant partenaire » ×2, « Chine » ×3.

Deux faux positifs du grep : `verified` est dans la liste de noms d'icônes chargée depuis
`fonts.googleapis.com` (police Material Symbols, pas une icône affichée), et `DPD` est une sous-chaîne
du nom de classe `image-block--AcDVzcnNsYlovTTdPd__image_lifestyle`.

### Collections

`suspensions-xxl` et `suspensions-osier` renvoient **404**. Les quatre autres étaient déjà hors
canaux (`resourcePublications` vide) avant sa manipulation — c'est ce que montrait le `0` de la
colonne « canaux » de sa capture, et c'est ce qui l'inquiétait : la colonne de gauche compte les
brouillons, pas ce qu'un visiteur voit.

### Cohérence des délais

Six surfaces relues (3 politiques, accueil, fiche, panier) : **1 à 2 j + 6 à 16 j = 7 à 18 j
ouvrés**, cut-off **16h00** heure de Paris, horaires **10h–18h**, **14 jours** légaux + **30 jours**
commerciaux. Aucun écart.

**Scan de véracité : 0 bloquant** (contre 14 avant les actions de Hakim, contre 47 avant la passe).

## 2. Le trou : `seo.title` et `seo.description`

Le scan ci-dessus lit `products.json` et les pages CMS. En le relançant sur les **51 fiches
rendues** (`--pages` avec les 51 URL produit), **32 alertes** sont apparues, presque toutes dans la
balise `<title>`.

`seo.title` et `seo.description` sont des champs **distincts** du titre et de la description du
produit. `productUpdate(product: {title})` ne les touche pas, et `products.json` ne les expose pas.
La passe du matin avait donc corrigé 30 titres produit en laissant leur titre SEO intact.

### Ce qui traînait

- **20 titres SEO** : « Applique murale double **travertin** », « Suspension **pierre** claire »,
  « Lustre salon sputnik **laiton** et noir, **6 boules** verre », « Suspension soucoupe **soie**
  plissée blanche », « Suspension rotin cloche haute tressée, **osier** », « Suspension boule verre
  **fumé** », « Plafonnier salon **noir** » (titre de 21 caractères), « Plafonnier LED **5** anneaux
  entrelacés »…
- **5 collections** : « Applique murale **pierre, travertin** et verre » (et sa description
  « Appliques murales **en pierre**, travertin et verre »), « montés **laiton** ou métal noir »,
  « **travertin** » dans Suspensions cuisine, « galets **de pierre** » dans Suspensions salon, et
  Plafonniers cuisine décrivant « réglette linéaire, coupole blanche, disque rond » alors que la
  collection ne contient publiquement qu'un dôme en corde et un anneau LED.
- **Trois méta descriptions contredisaient leur propre fiche sur la source lumineuse** :

| Fiche | Méta description | Ce que dit la fiche |
|---|---|---|
| `805304` | « LED intégrée, aucune ampoule à prévoir » | « L'ampoule est fournie : une LED 4 W sur douille E27 » |
| `952116` | « LED intégrée, aucune ampoule à prévoir » | « L'ampoule est fournie, une LED 4 W sur douille E27, remplaçable jusqu'à 60 W » |
| `121862` | « LED intégrée, aucune ampoule à prévoir » | « L'ampoule est fournie : une LED 4 W sur douille E27 » |

C'est la famille d'ampoules de la passe du 05/09 : les plaques fournisseur avaient tranché, les
fiches avaient été corrigées, les méta descriptions non.

### Corrigé

- **30 fiches** : `seo.title` + `seo.description`, alignés sur le titre produit et sur ce que dit la
  fiche (matière qualifiée, nombres et couleurs seulement quand ils valent pour toutes les variantes,
  source lumineuse conforme au corps).
- **5 collections** : `seo.title` + `seo.description`.
- **`897170`** : le corps disait « Un abat-jour **en rotin tressé** … cette **suspension en rotin
  tressé** » alors que les variantes sont `Ø 50 cm · rotin`, `Ø 50 cm · plastique`,
  `Ø 60 cm · plastique`, `Ø 60 cm · rotin`. Réécrit en « Un abat-jour tressé … cette corolle de
  pétales existe en rotin ou en fibre synthétique selon la variante ».

Écritures par `productUpdate` / `collectionUpdate` en trois lots de dix, aucune `userErrors`. Le
type d'entrée est **`ProductUpdateInput`**, pas `ProductInput` (le premier essai a été refusé sur un
`Type mismatch`).

### Scan final

**0 bloquant, 4 alertes**, toutes justifiées :

- `MAT-PROSE` sur `/pages/notre-histoire` : « un composite qui imite la pierre est présenté comme un
  effet pierre » — c'est la phrase qui explique la règle ;
- `COL-MAIGRE` sur Plafonniers cuisine (2), Suspensions bambou (3), Suspensions effet pierre (4).
  Les trois sont réelles et leur description ne décrit plus de brouillon.

## 3. Outil et leçon

`scan_veracite.py` charge désormais **chaque fiche et chaque collection publiée** pour lire sa balise
`<title>` et sa méta description, via une fonction `scan_meta`. `--sans-meta` coupe ce comportement.
Le scan complet fait une centaine de requêtes et se faisait limiter en 429 : `fetch` temporise 0,4 s
et reprend deux fois sur 429.

Leçon consignée dans NOX (`2026-09-17-le-titre-seo-est-un-second-titre.md`), dans la section « Le
titre SEO est un second titre » du lexique interdit et dans `audit-lecons-lumiere-matiere.md` :
**un champ corrigé n'est pas une page corrigée**. Un audit de véracité se fait sur la page rendue.

## Reste à faire

Inchangé : commande test (matière des appliques, ampoule de `829449`, délai réel), enregistrement
DEEE avant d'écrire quoi que ce soit dessus, directeur de la publication dans les mentions légales,
claim « connecté RVB / pilotable depuis une application » de `007557` non vérifié. **Pas de campagne
ni de demande de réexamen** avant que ces points soient tranchés.

# Swatches & corrections — NOIRMONT, 25/07/2026

Boutique Maison Noirmont (Shopify `v42pzp-h4`). Mission en trois volets.
Contrôles globaux : **aucun SKU modifié, aucune variante supprimée, aucune valeur d'option supprimée, aucune commande, aucun identifiant saisi, aucun fichier de thème touché.**

---

## Volet 1 — ✅ Les 12 variantes siglées sont invendables

### Constat technique préalable
Le suivi d'inventaire **était déjà actif** sur les 36 variantes du « Voyageur — GMT automatique » (`10977448657234`), mais la politique était `CONTINUE` (vente autorisée à stock nul). **Mettre le stock à 0 seul n'aurait donc rien bloqué.** Il fallait les deux leviers.

Autre point à connaître : le stock n'est pas porté par l'emplacement de la boutique mais par l'emplacement **`dsers-fulfillment-service`** (`gid://shopify/Location/125118251346`). Une écriture sur l'emplacement boutique échoue avec « l'article en stock n'est pas stocké à l'emplacement ».

### Ce qui a été fait — deux opérations
1. `productVariantsBulkUpdate` → `inventoryPolicy: DENY` sur les 12 variantes.
2. `inventorySetQuantities` (`name: "available"`, `reason: "correction"`, `ignoreCompareQuantity: true`) → quantité **0** sur les 12 articles d'inventaire, à l'emplacement `125118251346`.

### Les 12 variantes concernées (3 coloris × 4 mouvements/fonds)

| Variante | ID | Stock avant |
|---|---|---:|
| Or · bracelet 3 maillons · siglé / DG3804 · fond verre | 54087142211922 | 49 |
| Or · bracelet 3 maillons · siglé / DG3804 · fond acier | 54087142244690 | 50 |
| Or · bracelet 3 maillons · siglé / NH34 · fond acier | 54087142834514 | 50 |
| Or · bracelet 3 maillons · siglé / NH34 · fond verre | 54087142867282 | 50 |
| Bicolore · bracelet 3 maillons · siglé / NH34 · fond acier | 54087142900050 | 50 |
| Bicolore · bracelet 3 maillons · siglé / NH34 · fond verre | 54087142932818 | 50 |
| Bicolore · bracelet 3 maillons · siglé / DG3804 · fond verre | 54087143063890 | 50 |
| Bicolore · bracelet 3 maillons · siglé / DG3804 · fond acier | 54087143096658 | 50 |
| Bicolore · cadran brun · siglé / NH34 · fond verre | 54087142408530 | 50 |
| Bicolore · cadran brun · siglé / NH34 · fond acier | 54087143031122 | 50 |
| Bicolore · cadran brun · siglé / DG3804 · fond verre | 54087143194962 | 50 |
| Bicolore · cadran brun · siglé / DG3804 · fond acier | 54087143227730 | 50 |

### 🔄 Comment annuler (une seule opération, réversible)
Remettre `inventoryPolicy: CONTINUE` sur ces 12 IDs via `productVariantsBulkUpdate`. **C'est suffisant** : avec `CONTINUE`, Shopify revend même à stock 0, donc il n'est pas nécessaire de restaurer les quantités. Pour restaurer aussi le stock : `inventorySetQuantities` à 50 (49 pour `54087142211922`) sur l'emplacement `125118251346`.

### Contrôle storefront (thème brouillon `204248088914`)
Lu sur `/products/voyageur-gmt-automatique.js` : **36 variantes au total, 24 achetables, 12 siglées dont 0 achetable.** Les pastilles siglées s'affichent barrées d'un trait diagonal ; les 6 autres coloris restent achetables. SKU inchangés.

---

## Volet 2 — ✅ Titre corrigé

`10977445216594` : **« Loupe de date — saphir » → « Loupe de date — minéral ou saphir »**.

La description affirmait « la bulle saphir » alors que 8 des 14 variantes sont en verre minéral. Elle a été réécrite : mention explicite des deux matières, ajout de la différence utile au client (le saphir résiste mieux aux rayures, le minéral est l'option économique) et de l'invitation à mesurer son guichet de date.

Le **handle est resté `loupe-de-date-saphir`** : aucun lien existant n'est cassé. 14 variantes avant / 14 après, SKU identiques.

---

## Volet 3 — ✅ Pastilles posées sur les 4 montres

### ⚠️ Correction d'une hypothèse du brief
Le plan supposait `productOptionUpdate` → `optionValuesToUpdate` → `swatch`. **Ce champ n'existe pas** : `OptionValueUpdateInput` n'accepte que `id`, `name` et `linkedMetafieldValue`, et `swatch` est un champ **lecture seule** sur `ProductOptionValue`.

Le vrai mécanisme, vérifié bout en bout :
1. Activer la définition de métaobjet standard **`shopify--color-pattern`** (champs `label`, `color` hexadécimal libre, `image`, + 2 références de taxonomie obligatoires).
2. Créer **un métaobjet par valeur d'option**, avec `label` = le libellé client **exact** (c'est le label qui devient le nom affiché — les noms n'ont donc pas bougé).
3. Donner une **catégorie de taxonomie** au produit (`Montres` = `aa-6-11`) — sans elle, le lien est refusé.
4. Lier l'option existante via `productOptionUpdate` avec `option.linkedMetafield` + `optionValuesToUpdate[].linkedMetafieldValue`.

**Piège majeur :** pour la catégorie Montres, la clé `shopify.color-pattern` est **refusée** (hors contraintes de catégorie). Il faut les clés horlogères : **`shopify.dial-color`** (cadran), **`shopify.case-color`** (boîtier), `shopify.band-color` (bracelet). Les trois ont été activées.

### Résultat par fiche

| Fiche | Option | Clé liée | Valeurs | Type de swatch |
|---|---|---|---:|---|
| Héritage — Plongeuse vintage 42 | Cadran & lunette | `dial-color` | 3 | **couleur** |
| Intégrale — Sport chic acier | Cadran | `dial-color` | 7 | **couleur** |
| Contre-la-montre — Chronographe panda | Cadran | `dial-color` | 20 | **image** |
| Voyageur — GMT automatique | Boîtier & bracelet | `case-color` | 9 | **image** |

**Pourquoi image et non couleur sur ces deux fiches :** une pastille unie n'y départage rien. Les trois « panda inversé » du chronographe, ou « Champagne · bracelet acier » vs « … caoutchouc », partagent la même couleur de cadran ; les 5 GMT bicolores partagent le même métal. L'image porte cadran + compteurs + bracelet (chrono) et métal + maillons + cadran (GMT).

**Volontairement laissés en boutons texte** (conformément à la règle « aucun swatch quand le choix est une dimension ») :
- « Mouvement & fond » du GMT (DG3804/NH34, fond verre/acier) — non visuel ;
- Loupe de date (14 valeurs) — le choix est une dimension ;
- Noirmont Deux (7 « Référence n ») — valeurs jamais identifiées, rien d'honnête à illustrer.

### Swatches couleur posés (hexadécimaux)

**Héritage :** Bleu · lunette bleue `#2F6FA8` · Bleu nuit · lunette noire `#1C2B45` · Vert · lunette verte `#1F6B4A`
**Intégrale :** Vert `#1F6B45` · Brun · boîtier or rose `#6B4A32` · Turquoise `#35AEA8` · Noir `#17181A` · Bleu nuit `#1C2B45` · Bleu ciel `#7FB3D9` · Blanc argenté `#E4E4E0`

### Swatches image posés
29 PNG de **156 × 156, ~1 Ko** générés puis téléversés (`stagedUploadsCreate` → POST → `fileCreate`). Sources et planche de contact : `boutique-seiko-mod/livraisons/swatches-2026-07-25/` (script `gen_swatches.py`, table `specs-swatches.json`).

- **Chronographe (20)** : fond = bracelet, disque = cadran, 3 pastilles = compteurs, trait rouge = aiguille chrono rouge (M18/M19).
- **GMT (9)** : fond = métal du bracelet (moitié/moitié pour les bicolores), rainures = 3 ou 5 maillons (arcs pour le bracelet Président), disque = cadran (noir ou brun).

### Preuve storefront
`https://v42pzp-h4.myshopify.com/products/contre-la-montre-chronographe-panda?preview_theme_id=204248088914`
Le thème rend `<label class="swatch"><span style="--swatch-background: url(...noirmont-swatch-chrono-14.png)">` — **20 pastilles illustrées** au lieu de 20 boutons texte. Sur Héritage, `--swatch-background: rgb(47 111 168)`, soit exactement `#2F6FA8`.

Capture d'écran de la fiche GMT (pastilles + siglées barrées) et de la fiche Héritage : **dans le fil de la session**. Elles n'ont pas pu être écrites sur disque — la capture passe par le navigateur intégré, qui n'expose pas d'export fichier, et rejouer la page en headless aurait exigé de saisir le mot de passe boutique (interdit). Planche de contact des 29 pastilles : `boutique-seiko-mod/livraisons/swatches-2026-07-25/00-planche-contact-swatches.png`.

---

## Contrôles de non-régression

| Fiche | Variantes avant | Après | SKU |
|---|---:|---:|---|
| Contre-la-montre | 20 | **20** | identiques |
| Voyageur — GMT | 36 | **36** | identiques |
| Intégrale | 7 | **7** | identiques |
| Héritage | 3 | **3** | identiques |
| Loupe de date | 14 | **14** | identiques |

Les SKU relus après coup portent toujours la chaîne d'attributs AliExpress (`14:200000914#M14`, `14:350850#8;5:56964930#DG3804 GLASS back`…).

### ⚠️ Compteurs DSers — non vérifiés
Je n'ai **pas pu** contrôler les compteurs (objectif : Mes Produits 44 · AliExpress 44 · Unmapped 0). DSers demande une connexion dans le navigateur dont je dispose, et la consigne interdit de saisir un identifiant. **À vérifier par Hakim dans la session Chrome.**

Éléments objectifs en faveur d'un mapping intact : DSers s'appuie sur l'ID de variante et le SKU ; les deux sont inchangés sur les 5 fiches, aucune variante ni valeur d'option n'a été supprimée, et les 12 variantes siglées existent toujours (elles sont seulement à stock 0 / DENY).

---

## Reste à faire

1. **Vérifier les compteurs DSers** (ci-dessus) — à faire avant toute autre passe.
2. **Accessoires non traités** (priorité montres respectée) : Bracelet Présidentiel (24), Rouleau de Voyage (12), Remontoir Bois (8), Remontoir Collection (15), Set de tournevis (5). La recette est désormais mécanique ; il reste à trouver la bonne clé de métafichier par catégorie (`shopify.color-pattern` convient probablement aux catégories « Boîtes à montres » / « Boîtiers et housses », mais **pas** à `aa-6-11`). Le Bracelet Présidentiel **exige des images** : 5 de ses 24 valeurs sont « acier » et seraient 5 pastilles grises identiques.
3. **Décision produit sur les 12 siglées** : elles sont neutralisées mais toujours visibles (barrées). Si Hakim veut les faire disparaître complètement, l'option propre est un retrait côté DSers puis suppression, pas une suppression Shopify seule.
4. **Remontoir Collection** : le titre dit « 2 à 6 montres » alors que 2 variantes sont à 1 montre (signalé le 25/07, toujours ouvert).
5. Les swatches image peuvent être remplacés par de vraies photos sans retoucher les options : il suffit de mettre à jour le champ `image` du métaobjet correspondant.

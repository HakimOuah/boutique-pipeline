# Prompt à envoyer à Codex — galeries produit NOIRMONT

> Copier-coller le bloc ci-dessous tel quel. Il est autoportant.

---

Tu produis les **photos de galerie** des fiches produit de la boutique Shopify **Maison Noirmont** (montres mécaniques et accessoires d'horlogerie, France, panier 30–430 €).

## Périmètre et interdiction absolue

**Tu ne te connectes pas à Shopify. Tu ne modifies rien sur la boutique.** Tu produis des fichiers sur le disque et un manifeste. Le branchement sera fait ensuite, par quelqu'un d'autre. Toute tentative d'écriture sur la boutique est hors mission.

**La liste exacte des images manquantes, fiche par fiche, est dans `boutique-pipeline/boutique-seiko-mod/audit-visuel-catalogue.md`.** C'est ta feuille de route : ne produis que ce qui y figure, et rien d'autre.

## Le standard

Galeries **100 % photographiques**. Aucune carte typographique, aucun texte composé, aucune citation — ces éléments ont été retirés du standard.

| Famille | Images | Slots |
|---|---:|---|
| Montres | **4** | `face` · `situation` · `macro` · `poignet` |
| Accessoires | **3** | `face` · `situation` · `macro` |

- **face** — le produit seul, de face, centré. C'est l'image principale.
- **situation** — le produit posé dans un décor sobre qui suggère l'usage, sans jamais voler la vedette au produit.
- **macro** — un détail rapproché : cannelure de lunette, maillon, boucle, texture de cadran, grain du cuir.
- **poignet** — la montre portée. Voir la section dédiée, c'est le slot à risque.

## Direction artistique

Fond minéral clair uni (pierre `#E7E4DE` / craie `#FAFAF7`), lumière douce latérale, ombre portée diffuse, rendu studio éditorial premium. Carré **2048 × 2048**, JPEG qualité ~90.

**Méthode : image-to-image depuis la face déjà validée de chaque fiche**, en ne changeant que ce que le slot impose. Boîtier, bracelet, aiguilles, index, guichet de date et coloris restent **identiques** d'une image à l'autre. C'est ce qui rend une galerie homogène — et c'est ce qui garantit que le client reçoit la montre qu'il a vue.

⚠️ **31 faces sources manquent sur le disque.** Leur liste et leurs URL CDN sont dans l'audit, à exporter dans `entrees-faces/` **avant** de lancer la série. Sans elles, tu générerais sans référence.

## Règle absolue : stérilité

**Aucun logo, aucune lettre, aucun mot, aucun chiffre romain typographié sur un cadran.** Seuls chiffres tolérés : lunettes de plongée, GMT ou tachymètre, et guichets de date — à condition d'être nets et cohérents.

**Vérifie chaque image en zoomant sur le cadran.** Si du texte apparaît : **régénère**. **Ne retouche jamais par inpainting** — c'est cette retouche qui a produit un défaut visible qu'il a fallu refaire entièrement.

## Le slot « poignet » — le plus risqué

Les mains sont le pire angle mort des modèles d'image : doigts surnuméraires, ongles déformés, poignets aux proportions fausses, seconde main fantôme.

**Cadrage imposé, qui réduit la surface de risque :**
- Poignet et avant-bras seuls. **Jamais de visage.**
- Manche neutre, unie, sans motif ni marque.
- **Aucun autre bijou** au poignet — pas de bracelet, pas de seconde montre.
- Main au repos ou légèrement fermée ; évite les doigts écartés, qui multiplient les défauts.
- Le fond reste dans la charte : clair, minéral, non distrayant.

**Le cadran reste stérile.** Ajouter un porteur ne suspend aucune règle.

**Contrôle obligatoire, en zoom sur la main, à chaque image** : compte les doigts, vérifie les ongles et l'articulation du poignet. Au moindre défaut, **régénère** — jamais de retouche.

## Modèle

**Utilise ton modèle natif, GPT Image 2.** Il a été évalué lors d'un comparatif de cinq candidats sur ce catalogue : sa fidélité au produit est bonne et il n'invente pas d'éléments sur les cadrans. Nous ne l'avions pas retenu pour notre propre pipeline uniquement pour des raisons de coût et de résolution native — deux objections **sans objet ici**, puisque tu y accèdes nativement et que notre format de livraison est 2048 px, en deçà de ce qu'il produit.

**Deux familles de modèles sont à proscrire**, si tu envisages autre chose :
- les modèles de type **UGC/mode** — ils fabriquent de faux logos de marque sur les cadrans, c'est la cause racine d'un défaut qu'il a fallu corriger entièrement sur cette boutique ;
- les modèles d'**édition** qui réinventent l'objet — l'un d'eux a ajouté un chiffre romain et une trotteuse inexistante pendant le comparatif.

Si tu changes malgré tout de modèle, teste-le sur **une seule image** et vérifie la fidélité hors cadran avant de lancer la série.

## Nommage et manifeste — lis ceci deux fois

La dernière fois, le manifeste était indexé sur des **identifiants de variante devenus périmés avant même d'être lus**, et les 118 correspondances ont dû être refaites à la main par SKU. On ne recommence pas.

- **Nom de fichier : `<handle>-<slot>.jpg`** — par exemple `trente-neuf-bleu-poignet.jpg`.
- **Manifeste JSON indexé sur le `handle` de la fiche et le `SKU`.** Jamais sur un identifiant de variante, de média ou de produit.
- Une entrée par fichier : `handle`, `sku`, `slot`, `fichier`, `modèle utilisé`, `nombre de régénérations`.

## Exclusions

Ne produis rien pour :
- **Noirmont Deux** — ses 7 références n'ont pas pu être identifiées, le fournisseur utilisant la même photo pour toutes.
- Les **3 déclinaisons GMT « siglé »** — elles portent un logo de marque tierce et ont été rendues invendables.
- Les **7 fiches mères en brouillon**, hors catalogue.

## Contrôle de fin

Une planche par fiche, les images côte à côte, pour vérifier l'homogénéité de cadrage, de lumière et de coloris. **Une galerie qui « saute » d'une image à l'autre est un défaut**, pas une variation.

Signale explicitement, à la fin : ce que tu as produit, ce que tu as écarté et pourquoi, ce qui a demandé plus de trois régénérations — ce dernier point indique un sujet que le modèle ne sait pas traiter, et c'est une information utile.

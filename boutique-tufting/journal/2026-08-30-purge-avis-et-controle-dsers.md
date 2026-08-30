---
type: journal
boutique: tufting
date: 2026-08-30
nature: intervention
leviers: [conformite, catalogue, sourcing]
titre: "Purge des métafields d'avis + contrôle DSers des deux tondeuses"
---

# Purge des métafields d'avis + contrôle DSers — 30/08/2026

Ordre de Hakim : corriger les métafields d'avis, et confronter sur DSers la fiche DRAFT
« Kit tondeuse + guide de tonte » à la tondeuse ACTIVE en rupture.

## 1. Métafields d'avis — 51 suppressions, 0 échec

Cible : les 17 fiches dont le compteur n'était pas nul. Les 23 déjà à 0/0 n'ont pas été
touchées.

| Namespace | Clé | Rôle |
|---|---|---|
| `reviews` | `rating` | lu par Google & YouTube pour les étoiles Shopping |
| `reviews` | `rating_count` | idem |
| `vstar` | `product_rating` | miroir Trustoo, mêmes compteurs |

Mutation : `metafieldsDelete` (pas `metafieldDelete`, inexistant sur cette API).
Relu ensuite : `reviews.*` = 0 partout, plus aucun `vstar` à `total_reviews > 0`.

**Réserve** : si les six avis fictifs existent encore dans Trustoo, l'app peut recréer
`vstar` puis `reviews.*` à la prochaine synchro. Le contrôle admin Trustoo n'a pas été
fait ici.

Script relançable : `tmp/tufteo-purge-avis.py` (dry-run par défaut).

## 2. Contrôle DSers — ce n'est pas la même machine

### Ce qui n'a pas pu être ouvert

Le dashboard DSers (`www.dsers.com/login`) et l'admin Shopify (`et0hua-w1`) demandent
une session. Aucun identifiant saisi. Le mapping réel vit dans la base DSers, hors API
Shopify — c'était déjà le constat du 16/08.

### Ce qui suffit à conclure

Les SKU que DSers écrit, et dont il se sert pour router une commande, ne se recoupent
sur **aucune** propriété :

| | Tondeuse ACTIVE | Kit DRAFT « Avec guide » | Guide ACTIVE |
|---|---|---|---|
| SKU | `14:201441319;200007763:201336342` | `14:200006153#With bracket;200007763:201336100;5:361385#EU Plug` | `200007763:201336100` |
| Variantes | 1 (Orange/Noir) | 3 (lot / sans guide / avec guide) | 1 |
| Stock Shopify | 0 | 64 | OK |
| Coût | 42,91 € | 27,35 € | 7,43 € |
| Images | Codex (`tondeuse-electrique-tapis-0N.png`) | noms AliExpress bruts | — |

Le kit et le guide standalone partagent `200007763:201336100`. La tondeuse ACTIVE
n'a **pas** cette propriété. Ce sont deux listings AliExpress distincts. Publier le
kit à la place de la tondeuse, ce n'est pas un remplacement : c'est vendre un autre
produit, à un autre prix, avec d'autres visuels encore bruts.

Les deux variantes « Lot 5 pièces » (18,39 €) et « Sans guide » (22,97 €) restent
tarifées au coût d'achat exact. Ne pas publier la fiche DRAFT avant de les tarifer.

### Ce que le dashboard aurait dû confirmer, et que la PDP AliExpress confirme

Le 16/08, Hakim a tranché le remplacement de la tondeuse ACTIVE vers
`https://fr.aliexpress.com/item/1005007430527466.html` (Crafters Daily Tools Store,
240 W, expédié d'Allemagne). Le remapping DSers avait été laissé à Hakim — le SKU
Shopify n'a pas bougé depuis.

PDP ouverte aujourd'hui (confiance **A**) :

| | 16/08 | 30/08 |
|---|---|---|
| Prix | 43,59 € | **42,99 €** (barré 43,32 €) |
| Achetable | stock 12 | **Ajouter au panier actif** |
| Magasin | Crafters Daily Tools Store | identique |
| Avis | 0 | 4,9 / 15 avis |

Donc le fournisseur visé le 16/08 **n'est pas en rupture**. Si DSers pointe encore
vers l'ancien listing (`14:201441319…`), le stock 0 côté Shopify est un mapping
périmé, pas une absence d'offre.

Un listing voisin « Tondeuse à tufting avec support » existe
(`1005011967899321`, 48,59 €) — ce n'est **pas** le listing de la fiche DRAFT
(SKU différents), juste un cousin 200 W avec guide.

## Décisions qui restent à Hakim

1. Ouvrir DSers → Mes produits → **Tondeuse électrique pour tapis** et lire
   l'URL fournisseur réellement mappée.
2. Si c'est encore l'ancien listing : remapper vers `1005007430527466` (décision
   déjà prise le 16/08), puis revérifier le stock Shopify.
3. Ne pas publier le kit DRAFT comme rustine.
4. Une passe dans Trustoo pour confirmer que les six avis fictifs n'y sont plus.

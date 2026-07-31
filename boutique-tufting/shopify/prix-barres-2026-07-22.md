# Prix barrés (compareAtPrice) — Tuftéo — posés le 22/07/2026

> **PLACEHOLDERS posés à la demande de Hakim (checklist formation) — valeurs à ajuster/valider par lui ; ancrages machines basés sur les prix letufting relevés le 21/07.**

Règles appliquées :
- **Machines** : ancrage marché letufting (voir tableau).
- **Autres produits** : compareAtPrice = prix variante × 1,3 arrondi au ,90 supérieur, appliqué à chaque variante individuellement.
- **Exclu** : « Pièces détachées pour tufting gun » (gid://shopify/Product/15466415292801) — non touché.
- Seul compareAtPrice modifié (jamais price ni statut). Contrôle final : compareAt strictement > price sur 100 % des variantes traitées (re-query complète du catalogue).

## Machines (ancrage marché)

| Produit | Prix | compareAt posé | Variantes |
|---|---|---|---|
| Kit Tufting Complet 2-en-1 (15466411688321) | 229,00 € | **299,00 €** | 1 |
| Tufting gun 2-en-1 Cut & Loop (15466410213761) | 149,00 € | **189,00 €** | 2 |
| Tondeuse professionnelle pour tapis (15466411426177, DRAFT) | 89,90 € | **119,00 €** | 1 |
| Ciseaux électriques de sculpture (15466411458945, DRAFT) | 299,00 € | **349,00 €** | 2 |

## Autres produits (×1,3 → ,90 supérieur)

| Produit | Prix variante(s) | compareAt posé | Variantes |
|---|---|---|---|
| Tissu de finition (15466411131265) | 22,90 / 19,90 | 29,90 / 25,90 | 2 |
| Tissu de finition antidérapant (15466411196801) | 18,90 / 16,90 / 39,90 / 34,90 / 8,90 | 24,90 / 22,90 / 51,90 / 45,90 / 11,90 | 5 |
| Fil acrylique en cône (15466411229569) | 12,90 (toutes) | 16,90 | 87 |
| Grippers — lot de 8 (15466411262337) | 29,90 / 26,84 | 38,90 / 34,90 | 2 |
| Bobineuse à laine (15466411295105) | 19,90 | 25,90 | 1 |
| Ciseaux pélican (15466411327873) | 11,90 | 15,90 | 1 |
| Enfile-laine — lot de 5 (15466411360641) | 4,90 (×3) | 6,90 | 3 |
| Lames de remplacement — lot de 12 (15466411491713) | 49,90 | 64,90 | 1 |
| Kit tondeuse + guide de tonte (15466411524481, DRAFT) | 18,39 / 22,97 / 79,90 | 24,90 / 29,90 / 103,90 | 3 |
| Toile primaire lignes repères (15466411557249) | 19,90 / 7,49 / 6,90 / 12,90 / 39,90 / 44,90 / 89,90 ×2 | 25,90 / 9,90 / 9,90 / 16,90 / 51,90 / 58,90 / 116,90 ×2 | 8 |
| Toile premium polyester (15466411590017) | 109,90 / 69,90 | 142,90 / 90,90 | 2 |
| Guide de tondeuse (15466411655553) | 11,90 | 15,90 | 1 |
| Brosse de finition (15466412835201) | 6,49 (×3) | 8,90 | 3 |
| Spatule à colle (15466412900737) | 7,49 | 9,90 | 1 |
| Équilibreur de ressort (15466412933505) | 18,90 | 24,90 | 1 |
| Ruban de finition tissé 10 m (15466413752705) | 23,90 | 31,90 | 1 |
| Ruban adhésif de finition (15466413785473) | 27,90 | 36,90 | 1 |
| Miroir acrylique (15466414408065) | 12,90 / 18,90 / 21,90 / 30,90 / 33,90 / 37,90 / 42,90 / 54,90 | 16,90 / 24,90 / 28,90 / 40,90 / 44,90 / 49,90 / 55,90 / 71,90 | 32 |

## Bilan

- **21 produits traités**, **161 variantes** mises à jour, **0 erreur** (userErrors vides sur toutes les mutations, aucun THROTTLED).
- 1 produit exclu comme demandé : Pièces détachées pour tufting gun (37 variantes non touchées).
- Note : les anciennes valeurs compareAtPrice (souvent inférieures au prix — vraisemblablement des coûts importés) ont été écrasées par les nouvelles valeurs.
- Le badge « Économisé » s'affiche automatiquement via le thème (sales_badge déjà configuré).

# Économie unitaire — statut

**Devise :** EUR
**Mode économique :** `catalogue-volume` low ticket
**Date :** 2026-08-08
**Verdict :** `MANQUANT` — aucune rentabilité n’est affirmée

## Filtre économique rapide — Scrapbooking

| Mesure | Observation |
|---|---:|
| Produits publics échantillonnés | 48 |
| Médiane ensemble | 10,99 EUR |
| Produits à 13,99 EUR ou moins | 33/48 (68,8 %) |
| Médiane papiers | 4,99 EUR |
| Médiane autocollants | 8,99 EUR |
| Médiane matériel | 24,49 EUR |
| AOV, articles/commande, marge, CAC | `MANQUANT` |

**Décision Hakim :** `STOP_PRIX_PANIER`. Ce niveau de ticket n'est pas
intéressant sans panier multi-produits et marge de commande crédibles. Le
calcul fournisseur complet n'est pas lancé pour tenter de sauver la niche.

## Panier à modéliser

| Élément | Statut | Preuve attendue |
|---|---|---|
| Prix moyen par composant | `MANQUANT` | prix de vente proposé par shortlist |
| Articles par commande | `HYPOTHESE` | panier projet complet à simuler |
| Panier moyen brut | `MANQUANT` | somme des composants/bundle |
| Coût produit exact | `MANQUANT` | SKU AliExpress exact |
| Transport fournisseur France | `MANQUANT` | freight exact par SKU/panier |
| TVA/douane non récupérable | `MANQUANT` | modèle fiscal validé |
| Paiement/plateforme | `MANQUANT` | contrat Shopify/paiement |
| Emballage/fulfilment | `MANQUANT` | mode opérationnel |
| Retours/SAV/casse | `MANQUANT` | hypothèse prudente par niche |
| Marge contributive pré-ads | `MANQUANT` | calcul complet |
| CAC/ROAS de rupture | `MANQUANT` | marge contributive |

## Scénarios de panier à comparer

1. Scrap : scénario historique supplanté par `STOP_PRIX_PANIER` ; aucun kit
   artificiel ne doit être construit pour sauver le dossier.
2. Chien : kit scénario non critique, avec taille et échange.
3. Mercerie : mini-projet + outils réutilisables + recharge.
4. Perles : projet bijou + apprêts + outils optionnels.
5. Aquarium : kit sec compatible + entretien.

## Garde-fou

Le low ticket est accepté par décision projet, mais uniquement si le panier, la marge par commande et le CPA maximal sont viables. Aucun prix minimum de 150 EUR ne doit être réintroduit.

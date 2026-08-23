# Corrections rapport OneClickBrand — 23/08/2026

Score audit : 78/100. Points bloquants traités sauf menu header (action manuelle 2 min).

## Fait

| Point audit | Correction |
|---|---|
| Email `assistance@shopify.com` dans mentions légales | Section « Contact technique publié par Shopify » supprimée. Seul `contact@maisonnoirmont.fr` reste. |
| Délais livraison incohérents | « 2 à 3 semaines » → « 14 à 21 jours calendaires » sur fiche produit, panier et footer. |
| Contact sans adresse postale | Adresse OH Ventures ajoutée sur `/pages/contact` + délai de réponse explicite. |
| Page suivi colis | `/pages/suivre-mon-colis` créée. |

## À faire (Hakim — 2 min)

**Contenu → Menus → Main menu** (le navigateur avait un brouillon non enregistré qui bloque l'automation) :

1. Renommer **La Maison** → **À propos** (garder le lien `/pages/la-maison`)
2. Ajouter **Suivre mon colis** → `/pages/suivre-mon-colis`
3. Enregistrer

## Vérifications live

- `assistance@shopify.com` sur `/policies/legal-notice` : absent
- `/pages/suivre-mon-colis` : 200
- Fiche produit test : plus de « 2 à 3 semaines », « 14 à 21 jours » présent

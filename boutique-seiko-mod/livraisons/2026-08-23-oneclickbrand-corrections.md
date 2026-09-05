# Corrections rapport OneClickBrand — 23/08/2026

Score audit : 78/100. Points bloquants traités sauf menu header (action manuelle 2 min).

## Fait

| Point audit | Correction |
|---|---|
| Email `assistance@shopify.com` dans mentions légales | Section « Contact technique publié par Shopify » supprimée. Seul `contact@maisonnoirmont.fr` reste. |
| Délais livraison incohérents | « 2 à 3 semaines » → « 14 à 21 jours calendaires » sur fiche produit, panier et footer. |
| Contact sans adresse postale | Adresse OH Ventures ajoutée sur `/pages/contact` + délai de réponse explicite. |
| Page suivi colis | `/pages/suivre-mon-colis` créée. |

## Menu header — fait le 30/08

Menus **live** (`noirmont-desktop` + `noirmont-mobile`) + footer Informations :

1. **La Maison** → **À propos** (lien `/pages/la-maison`)
2. **Suivre mon colis** → `/pages/suivre-mon-colis` (200)

**ParcelWILL** n'est **pas installé** sur Noirmont (`/apps/parcelpanel` = 404). Tuftéo / Bonum Vitae / Lumière Matière l'ont. Dès que l'app est posée sur cette boutique, basculer le lien menu vers `/apps/parcelpanel`.

## Vérifications live

- `assistance@shopify.com` sur `/policies/legal-notice` : absent
- `/pages/suivre-mon-colis` : 200
- Fiche produit test : plus de « 2 à 3 semaines », « 14 à 21 jours » présent

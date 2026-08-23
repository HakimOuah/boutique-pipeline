# Corrections GMC — misrepresentation, 23/08/2026

> **Contexte.** Compte GMC **5840460291** (OH Ventures / Maison Noirmont) : produits validés puis
> **bannis** pour **« Déclarations trompeuses ou déceptives »** (mail GMC + diagnostic compte).
> Audit live + scan catégories (structure, contact, produit, trust, store info) avant correction.

## GMC vérifié dans Chrome (browser-use)

**Infos entreprise** — cohérent avec le site :
- Nom : **OH Ventures**
- Adresse : **47 Rue Vivienne, 75002 Paris, France**
- Contact : `contact@maisonnoirmont.fr`, `+33756828094`
- URL contact : `https://maisonnoirmont.fr/pages/contact`
- Boutique : **maisonnoirmont.fr** — validé + revendiqué

**Diagnostic compte** : politique *Déclarations trompeuses ou déceptives* — vérification
automatisée. Google demande transparence identité / modèle économique / règles.

## Causes probables côté site (audit live)

| Catégorie | Problème | Gravité |
|---|---|---|
| Trust | Bandeau **« Qualité Premium »** + icône verified sur toutes les fiches | P0 |
| Product data | **57/96** fiches mentionnaient **Seiko** (descriptions + JSON-LD) | P0 |
| Product data | **3** fiches **Président / Présidentiel** (marque tierce) | P1 |
| Structure | 3 collections < 5 produits (déjà assumé) | P3 |
| Contact / store | OK au moment de la correction | — |

Prix barrés : gabarit dormant vide (`compare_at_price = null`) — pas un vrai problème.

## Corrections appliquées (23/08/2026)

### Thème live `205451100498` — `templates/product.json`
- Bloc bandeau `iwt_pdp1` **« Qualité Premium »** → **`disabled: true`**

### Catalogue Shopify (`v42pzp-h4`)
- **201 fiches** mises à jour (actives + brouillons) via GraphQL `productUpdate` :
  - `Seiko NH35/NH34/VK63` → **calibre NHxx japonais** (suppression marque Seiko)
  - Renommages titres :
    - `bracelet-presidentiel-dore` → **Bracelet à maillons arrondis : doré**
    - `bracelet-presidentiel-acier-inoxydable` → **Bracelet à maillons arrondis : acier inoxydable**
    - `voyageur-or-gmt-president` → **Voyageur Or : GMT bracelet à maillons arrondis**
  - Descriptions : Président/Présidentiel → **à maillons arrondis**

### Vérification post-correction (catalogue public 96 fiches)
- **0** mention Seiko
- **0** Président/Présidentiel
- **0** « Qualité Premium » sur fiche test
- JSON-LD produit test : **sans Seiko**

## Non traité (P2 — à planifier)
- **9 groupes d’images partagées** mère/enfant (`c-430162-*`, `c-690002-*`, etc.)
- Handles URL inchangés (`bracelet-presidentiel-*`, `voyageur-or-gmt-president`)

## Conduite post-correction (Terry)
- **Ne pas** demander d’examen GMC avant **7–10 jours**
- **Ne pas** lancer d’ads
- Laisser le flux Google & YouTube se resynchroniser
- Si Google demande une **pièce d’identité** : fournir (mention dans le mail GMC)

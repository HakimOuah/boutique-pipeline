---
type: journal
boutique: seiko-mod
date: 2026-08-23
nature: intervention
leviers: [conformite, technique]
titre: "Corrections GMC — misrepresentation, 23/08/2026"
---

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

### Images dupliquées T-36 (option 2)
- **9 composites** retirés des fiches **mères** via `productDeleteMedia` :
  `trente-neuf-classique-cannelee` (3), `trente-six-classique-jubile` (5),
  `trente-neuf-duo-classique-bicolore` (1)
- Post-check : **0** fichier CDN partagé entre deux fiches actives

### Handles URL renommés
| Ancien | Nouveau |
|---|---|
| `bracelet-presidentiel-dore` | `bracelet-maillons-arrondis-dore` |
| `bracelet-presidentiel-acier-inoxydable` | `bracelet-maillons-arrondis-acier` |
| `voyageur-or-gmt-president` | `voyageur-or-gmt-maillons-arrondis` |

- **18 alts** mis à jour sur ces 3 fiches
- Anciennes URLs → **404**, nouvelles → **200**
- **Redirections 301** : scope API manquant → à poser à la main (voir `livraisons/2026-08-23-redirections-handles-president.md`)

### Noms de fichiers CDN (13 visuels)
- **13 fichiers** renommés via `fileUpdate` (pas de `fileDelete`, pas de re-génération Codex) :
  suppression de `president` / `presidentiel` / `904l` des noms de fichiers sur les 3 fiches bracelets/GMT
- Post-check : **0** nom de fichier contenant `president` sur le catalogue actif

### Redirections 301 (23/08 soir)
- **3 redirections** créées dans l'admin Shopify (CLI sans scope navigation)
- Vérification live : anciennes URLs → **301**, nouvelles → **200**

### Rapport OneClickBrand (23/08 soir) — corrections
| Point | Action |
|---|---|
| `assistance@shopify.com` dans mentions légales | Bloc « Contact technique Shopify Inc. » **supprimé** (`shopPolicyUpdate`) |
| Délais livraison incohérents (2–3 sem. vs 14–21 j) | Harmonisé en **14 à 21 jours calendaires** (`product.json`, `cart.json`, `footer-group.json`) |
| Contact sans adresse postale | Adresse **47 rue Vivienne** ajoutée sur `/pages/contact` |
| Page suivi colis absente | Page **`/pages/suivre-mon-colis`** créée |
| Liens header « À propos » + « Suivre mon colis » | **À faire** — menu admin bloqué (dialogue modifications non enregistrées) ; « La Maison » couvre déjà l'À-propos |

## Non traité
- **Menu header** : ajouter « Suivre mon colis » + renommer « La Maison » → « À propos » (2 min dans Contenu → Menus → Main menu)

## Conduite post-correction (Terry)
- **Ne pas** demander d’examen GMC avant **7–10 jours**
- **Ne pas** lancer d’ads
- Laisser le flux Google & YouTube se resynchroniser
- Si Google demande une **pièce d’identité** : fournir (mention dans le mail GMC)

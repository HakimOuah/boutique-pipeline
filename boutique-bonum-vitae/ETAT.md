# Bonum Vitae — état courant

**Dernière mise à jour : 18/08/2026 ~11h30** — run autonome tickets. FullStack
`205568147794` est **MAIN**. [`TABLEAU.md`](TABLEAU.md) ·
[`journal/2026-08-18-run-autonome.md`](journal/2026-08-18-run-autonome.md).

---

## Identité

| | |
|---|---|
| Marque | Bonum Vitae |
| Domaine public | `https://bonumvitae.fr` (200, pas de mot de passe) |
| Store Shopify | **`kw7vak-g0.myshopify.com`** — `gid://shopify/Shop/109072515410` |
| E-mails | `shop.email` = `shop.contactEmail` = `contact@bonumvitae.fr` ✅ |
| Entité | OH Ventures (SASU), 47 rue Vivienne, 75002 Paris, SIREN 103157251 |
| Téléphone | `+33 7 56 82 80 94` — au footer, constaté live |
| Raison sociale au footer | ✅ OH VENTURES (SASU) — SIREN 103157251 |
| Devise | EUR seul, livraison FR seule |
| Persona | ✅ validé par Hakim le 17/08 — `../personas/persona-bonum-vitae-2026-08-17.md` |
| Auth CLI | ✅ `contact@bonumvitae.fr`. Scopes : products, files, themes, content, pages, legal_policies. **Pas `read_publications` / navigation / redirects** |

**Adresse et téléphone partagés avec Bien Brûlé, Tuftéo et Maison Noirmont** (linkage assumé,
16/08).

---

## Thèmes (constaté 18/08)

| Thème | Id | Rôle | Note |
|---|---|---|---|
| `copie-de-fullstack-2-3` | **`205568147794`** | **MAIN** | publié par Hakim. Run autonome 18/08. |
| Horizon | `203569004882` | UNPUBLISHED | ancien live |
| theme-impact-tristan-version-1 | `203578376530` | UNPUBLISHED | hors périmètre |
| Copie de theme-impact-tristan-version-1 | `203601510738` | UNPUBLISHED | hors périmètre |

---

## Catalogue (constaté API 18/08)

**28 produits** : **24 ACTIVE** publics, **4 DRAFT** (LPS, SHUANGLI, OSWNKW compact,
membrane 50 GPD). Kit entretien 600 GPD **publié**.

- **0 `compareAtPrice` non nul**
- Tag `hors-acquisition` : magnétiques DN8/DN20/DN25 + carafe 3,5 L
- Handles claims retirés : pommeau (plus `eau-adoucie`), carafe (plus `alcaline`) — 301 auto
- Metafields faux avis `reviews` / `vstar` 4,83/6 sur RO 600G **supprimés** (18/08 ~11h25)

### Collections publiques

| Collection | Produits | Seuil de 5 |
|---|---|---|
| `filtres-de-douche` / `carafes-filtrantes` / `filtres-robinet` / `anti-calcaire-sans-sel` | 5 | ✅ |
| `osmoseurs` | **supprimée** (18/08) | ✅ 404 |
| `purificateurs-nomades` | **supprimée** (18/08) | ✅ 404 |
| `frontpage` | 1 | système, hors nav |

---

## Crible — état après run autonome (18/08 matin)

| Gravité | Déclencheur | État |
|---|---|---|
| P0 | 3 faux avis « Vérifié » | ✅ retirés |
| P0 | « 4.8/5 · 312 avis vérifiés » | ✅ retiré |
| P0 | Metafields 4,83/6 (Vitals) sur RO 600G | ✅ purgés — surveiller réécriture app |
| P0 | Prix barrés | ✅ 0 au catalogue |
| P1 | Bandeau « -20% osmoseurs » | ✅ retiré |
| P1 | Hero « sans travaux ni plombier » | ✅ absent du FullStack live |
| P1 | Newsletter « -10 % » | ✅ absente |
| P1 | FAQ 24-48 h / 6-10 j vs policies | ✅ aligné (plus de « 5 et 9 ») |
| P1 | Doublon mentions légales | ✅ CMS 404 / policy 200 |
| P1 | Footer sans raison sociale | ✅ SIREN live |
| P1 | Collections < 5 | ✅ les deux petites supprimées |
| P1 | Handle `…eau-adoucie` | ✅ renommé + 301 |

---

## Merchant Center

**A priori aucun compte** (Hakim, 17/08, déclaratif). Le GMC se créera après boutique propre,
checklist complète, feu vert Hakim. Ne pas créer, ne pas soumettre.

Avant création, encore Hakim : 301 CMS/collections, Vitals, T-H7 restant, QA 375 px.

---

## Ce que je n'ai pas pu vérifier

- Apps installées / GMC (scope)
- Moyens de paiement réellement actifs vs icônes footer
- 301 (scope redirects) — pages CMS et collections mortes sont en **404**
- Zoom image par image de **tout** le catalogue (échantillon 12+ featured : 0 texte incrusté)

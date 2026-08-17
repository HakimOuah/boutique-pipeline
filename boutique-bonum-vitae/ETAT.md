# Bonum Vitae — état courant

**Dernière mise à jour : 17/08/2026 ~22h25** — visuels LPS **voie C** (Hakim) : overlays assumés,
brief relancé, robe inox nue autorisée. Raccord fiche **G3/4" femelle**. Plus tôt : STOP Codex,
persona, OSWNKW 449 €, FullStack v1, rail A P0.
[`TABLEAU.md`](TABLEAU.md) · [`journal/2026-08-17-stop-visuels-anti-tartre.md`](journal/2026-08-17-stop-visuels-anti-tartre.md).

---

## Identité

| | |
|---|---|
| Marque | Bonum Vitae |
| Domaine public | `https://bonumvitae.fr` (200, pas de mot de passe) |
| Store Shopify | **`kw7vak-g0.myshopify.com`** — `gid://shopify/Shop/109072515410` |
| E-mails | `shop.email` = `shop.contactEmail` = `contact@bonumvitae.fr` ✅ (constaté API 17/08) |
| Entité | OH Ventures (SASU), 47 rue Vivienne, 75002 Paris, SIREN 103157251 |
| Téléphone | `+33 7 56 82 80 94` — au footer, constaté live |
| Raison sociale au footer | ⛔ absente (ni OH Ventures, ni SIREN) — T-06 |
| Devise | EUR seul, livraison FR seule |
| Persona | ✅ validé par Hakim le 17/08 — `../personas/persona-bonum-vitae-2026-08-17.md` |
| Auth CLI | ✅ `contact@bonumvitae.fr` (17/08). Scopes : products, files, themes, content, pages, legal_policies. **Pas `read_apps`** |

**Adresse et téléphone partagés avec Bien Brûlé, Tuftéo et Maison Noirmont** (linkage assumé,
16/08). Depuis le 17/08 au soir, plus aucun déclencheur P0 connu n'est public ici.

---

## Thèmes (constaté API 17/08)

| Thème | Id | Rôle | Note |
|---|---|---|---|
| Horizon | `203569004882` | **MAIN** | rail A appliqué le 17/08 (3 templates + header-group) |
| `copie-de-fullstack-2-3` | **`205568147794`** | UNPUBLISHED | **cible rail B** — zip vendeur brut du 17/08 15h35, démo à purger (`powered-by-fullstack.svg`, placeholders, `logo-fullstack.png`) |
| theme-impact-tristan-version-1 | `203578376530` | UNPUBLISHED | juillet, hors périmètre |
| Copie de theme-impact-tristan-version-1 | `203601510738` | UNPUBLISHED | juillet, hors périmètre |

Templates produit Horizon : `product.json` (25 fiches) + `product.osmoseur.json`
(`osmoseur-ro-600g` uniquement).

---

## Catalogue (constaté API 17/08)

**27 produits** : 24 ACTIVE (les 24 publics), **3 DRAFT** dont `anti-tartre-galvanique-toute-la-maison`
(LPS, import 17/08 — raccord G3/4" femelle, visuels STOP) + `osmoseur-de-cuisine-shuangli-600g-osmose-inverse`
+ `membrane-drinkpod-a-osmose-inverse-ro`.

- **0 `compareAtPrice` non nul** sur tout le catalogue depuis le 17/08 ~19h15 (8 purgés, backup
  dans `backups/2026-08-17-rail-a/`).
- App d'avis **Trustoo** (`cwilltrustoo-reviews`) : bloc `review-widget` présent dans les deux
  templates produit. 0 commande → ne devrait rien rendre. À trancher au rail B.

### Collections

| Collection | Produits | Seuil de 5 |
|---|---|---|
| `filtres-de-douche` / `carafes-filtrantes` / `filtres-robinet` / `anti-calcaire-sans-sel` | 5 | ✅ |
| `osmoseurs` | 3 visibles (écart vs `collections.json` = 5 à lever) | ⛔ T-07 |
| `purificateurs-nomades` | 1 | ⛔ T-07 |
| `frontpage` | 1 | ⛔ (système) |

---

## Crible — état après rail A (17/08 soir)

| Gravité | Déclencheur | État |
|---|---|---|
| P0 | 3 faux avis « Vérifié » | ✅ **retirés** — constaté anonyme accueil + fiches |
| P0 | « 4.8/5 · 312 avis vérifiés » | ✅ **retiré** |
| P0 | Prix barrés | ✅ **0 au catalogue** (actifs + brouillons) |
| P1 | Bandeau « -20% osmoseurs » | ✅ **retiré** (« Livraison offerte » conservé) |
| P1 | Hero « sans travaux ni plombier » | ⛔ encore public — après persona |
| P1 | Newsletter « -10 % première commande » | ⛔ à recouper (code réel ?) |
| P1 | FAQ 24-48 h / 6-10 j vs policies | ⛔ à recouper — T-06 |
| P1 | Doublon mentions légales (2 URLs en 200) | ⛔ — T-06 |
| P1 | Footer sans raison sociale | ⛔ — T-06 |
| P1 | Collections < 5 | ⛔ — T-07 |
| P1 | Handle `…eau-adoucie` (claim) | ⛔ — à traiter au rail B (301) |

---

## Merchant Center

**A priori aucun compte** (Hakim, 17/08, déclaratif). Le GMC se créera après boutique propre,
checklist complète, feu vert Hakim. Ne pas créer, ne pas soumettre.

---

## Ce que je n'ai pas pu vérifier

- Apps installées / GMC (scope) — T-H6
- Moyens de paiement réellement actifs (`shop.enabled_payment_types` = Liquid ; le footer affiche
  Amex, Apple Pay, CB, Klarna, Mastercard, PayPal, Visa — à recouper au rail B)
- Filigranes / photos AliExpress brutes (pas d'audit visuel)
- Contenu mot à mot des policies vs boutiques sœurs

# Bonum Vitae — état courant

**Dernière mise à jour : 17/08/2026 ~18h** — ouverture chantier. Relevé **public uniquement**
(visiteur anonyme + `products.json` / `meta.json`). Pas d'admin : CLI encore sur Tuftéo + Noirmont.
[`TABLEAU.md`](TABLEAU.md) · [`journal/2026-08-17-ouverture-crible.md`](journal/2026-08-17-ouverture-crible.md).

---

## Identité

| | |
|---|---|
| Marque | Bonum Vitae |
| Domaine public | `https://bonumvitae.fr` (200, **pas** de mot de passe) |
| Store Shopify | **`kw7vak-g0.myshopify.com`** — confirmé par `https://bonumvitae.fr/meta.json` (`id` boutique `109072515410`) |
| E-mail vitrine | `contact@bonumvitae.fr` — au footer, constaté live |
| Entité | OH Ventures (SASU), 47 rue Vivienne, 75002 Paris, SIREN 103157251 |
| Téléphone | `+33 7 56 82 80 94` — au footer, constaté live |
| Raison sociale au footer | **absente** (ni OH Ventures, ni SIREN, ni TVA) |
| JSON-LD Organization | `name` + `logo` + `url` seulement — pas de `legalName`, pas de téléphone, pas d'adresse |
| Persona | ⛔ aucun fichier maison — brief juillet Claire/Karim/Bernard ≠ persona PLAYBOOK 1d |
| Auth CLI cette machine | ⛔ `et0hua-w1` (Tuftéo) + `v42pzp-h4` (Noirmont). `kw7vak-g0` **inconnu** du compte courant |

**Adresse et téléphone sont partagés avec Bien Brûlé, Tuftéo et Maison Noirmont.** Linkage assumé
par Hakim le 16/08 — `PASSATION.md` question 0. Une misrepresentation ici dégrade l'entité, donc
le GMC Tuftéo.

---

## Thème

| | |
|---|---|
| Live (rôle `main`) | **Horizon** 4.1.1 — `Shopify.theme.id` **203569004882** |
| FullStack 2.3 | **inconnu** (pas sur le live ; copies unpublished invisibles sans admin) |
| Cible redesign | FullStack 2.3, **le même** que Tuftéo / Noirmont (`copie-de-fullstack-2-3`) |

Le skill `webdesign-boutiques` dit encore « implémenter sur Horizon » — **ignorer** pour ce chantier.
Horizon = ossature CRO à porter (ordre des blocs), pas thème à recopier.

---

## Catalogue public (17/08)

`meta.json` : **24 produits** publiés, **7 collections** publiées.

### Prix barrés encore publics (`compare_at_price` dans `products.json`)

| Handle | Prix | Barré |
|---|---|---|
| `osmoseur-ro-600g` | 299,00 € | **470,00 €** |
| `filtration-par-osmose-inverse-oswnkw-600-gpd-haut-debit` | 576,90 € | **700,00 €** |
| `detartreur-super-magnetique-ipse-maison-dn20` | 152,90 € | **185,00 €** |
| `detartrant-d-eau-electronique-variante-usb-sans-sel` | 86,90 € | **105,00 €** |
| `detartrant-d-eau-electronique-alimentation-usb` | 98,90 € | **120,00 €** |
| `dispositif-anti-tartre-althy-ipse-sans-sel-non-electrique` | 86,90 € | **105,00 €** |

18 fiches sans barré. **Brouillons / archivés : non lus** (pas d'admin).

### Collections

| Collection | `products.json` visibles | `collections.json` count | Seuil de 5 |
|---|---|---|---|
| `filtres-de-douche` | 5 | 5 | ✅ |
| `carafes-filtrantes` | 5 | 5 | ✅ |
| `filtres-robinet` | 5 | 5 | ✅ |
| `anti-calcaire-sans-sel` | 5 | 5 | ✅ |
| `osmoseurs` | **3** (2 osmoseurs + 1 membrane) | **5** | ⛔ + écart à lever en admin |
| `purificateurs-nomades` | **1** | 1 | ⛔ |
| `frontpage` | 1 | 1 | ⛔ (collection système) |

---

## P0 / P1 encore publics (crible 17/08)

| Gravité | Déclencheur | Encore public ? |
|---|---|---|
| P0 | 3 témoignages « Vérifié » Claire / Karim / Bernard | **oui** — accueil **et** fiches (`bv-avis-section`) |
| P0 | « 4.8/5 basé sur 312 avis vérifiés » | **oui** — fiches (pas l'accueil) |
| P0 | Prix barrés | **oui** — 6 variantes actives |
| P1 | Bandeau « Offre d'été : -20% sur les osmoseurs » | **oui** — toutes les pages vues |
| P1 | Claim santé Karim (peau / tiraillement) | **oui** — dans le faux avis |
| P1 | Hero « sans travaux ni plombier » | **oui** — accueil |
| P1 | Newsletter « 10 % de remise sur votre première commande » | **oui** — à recouper (code réel ?) |
| P1 | FAQ « expédiés en 24-48h … 6 à 10 jours ouvrés » | **oui** — à recouper policies |
| P1 | Doublon mentions légales | **oui** — `/policies/legal-notice` et `/pages/mentions-legales` en 200 |
| P1 | Footer sans raison sociale | **oui** |
| — | JSON-LD `Review` / `aggregateRating` faux | **non** — les avis sont du HTML, pas du schema |
| — | Compte à rebours / « plus que X en stock » | **non** constaté |

Paiements affichés au footer (à recouper admin) : American Express, Apple Pay, Cartes Bancaires,
Klarna, Mastercard, PayPal, Visa. `meta.json` : `shopify_pay_enabled_card_brands: []`,
`offers_shop_pay_installments: false`. **Ne pas promettre le 4×** tant que
`shop.enabled_payment_types` n'est pas lu.

---

## Merchant Center

**Inconnu.** Tuftéo a montré qu'un GMC se crée tout seul via l'app Google & YouTube. Si un compte
Bonum Vitae existe : le signaler tout de suite, ne pas créer, ne pas soumettre, ne pas changer le
thème à la légère. Skill `gmc-acceptance` : pas de GMC avant boutique propre + policies recoupées
+ feu vert Hakim.

Checklist pré-soumission : **non déroulée en pass/fail** — le live est déjà en échec sur faux avis,
barrés, claims. Verdict GMC : **pas PRÊT**, et on ne le prononce pas tant que le rail A n'est pas
constaté soldé.

---

## Ce que je n'ai pas pu vérifier

- Thèmes unpublished (FullStack déjà là ou non)
- Apps d'avis, commandes réelles (hypothèse parc : 0 — à confirmer admin)
- `compareAtPrice` des brouillons / archivés
- Écart osmoseurs 3 vs 5
- Moyens de paiement réellement actifs
- Existence d'un GMC / app Google & YouTube
- Filigranes image (pas de revue visuelle fichier par fichier ce 17/08)
- Contenu mot à mot des 7 policies vs Tuftéo / Noirmont / Bien Brûlé

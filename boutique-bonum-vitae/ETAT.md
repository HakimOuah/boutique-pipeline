# Bonum Vitae — état courant

**Dernière mise à jour : 18/08/2026 ~12h15** — Vitals désinstallée.
[`TABLEAU.md`](TABLEAU.md) ·
[`journal/2026-08-18-vitals-paiements.md`](journal/2026-08-18-vitals-paiements.md).

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
| Auth CLI | ✅ `contact@bonumvitae.fr`. Scopes 18/08 ~11h45 : products, files, themes, content, pages, legal_policies, **navigation, publications** |

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

**28 produits** : **25 ACTIVE** publics (LPS publié le 18/08), **3 DRAFT** (SHUANGLI,
OSWNKW compact, membrane 50 GPD). Kit + LPS : Boutique en ligne seulement.

- **0 `compareAtPrice` non nul**
- Tag `hors-acquisition` + **hors Google** : magnétiques DN8/DN20/DN25, carafe 3,5 L, douche vitamine C
- Handles claims retirés : pommeau / carafe — 301 auto
- Metafields faux avis `reviews` / `vstar` 4,83/6 sur RO 600G **supprimés** (toujours absents)
- **Vitals désinstallée** le 18/08 (~12h15). Plus de `vtlsAebData` / `appsolve` sur accueil et RO 600G.
- Icônes paiement live = Visa / Mastercard / Amex / Apple Pay / Google Pay / PayPal / Shop Pay / Klarna (Klarna + Amex **actifs au checkout**)
- Apps encore installées (constaté admin) : DSers, CLI Connector, CWILL Parcel Panel, **CWILL(Trustoo) Reviews**, ChatGPT MCP, Claude Connector, Messaging

### Collections publiques

| Collection | Produits | Seuil de 5 |
|---|---|---|
| `filtres-de-douche` / `carafes-filtrantes` / `filtres-robinet` | 5 | ✅ |
| `anti-calcaire-sans-sel` | **6** (LPS ajouté) | ✅ |
| `osmoseurs` | **supprimée** + 301 → RO 600G | ✅ |
| `purificateurs-nomades` | **supprimée** + 301 → filtre randonnée | ✅ |
| `frontpage` | 1 | système, hors nav |

---

## Crible — état après run autonome (18/08 matin)

| Gravité | Déclencheur | État |
|---|---|---|
| P0 | 3 faux avis « Vérifié » | ✅ retirés |
| P0 | « 4.8/5 · 312 avis vérifiés » | ✅ retiré |
| P0 | Metafields 4,83/6 (Vitals) sur RO 600G | ✅ purgés · app **désinstallée** |
| P0 | Prix barrés | ✅ 0 au catalogue |
| P1 | Bandeau « -20% osmoseurs » | ✅ retiré |
| P1 | Hero « sans travaux ni plombier » | ✅ absent du FullStack live |
| P1 | Newsletter « -10 % » | ✅ absente |
| P1 | FAQ 24-48 h / 6-10 j vs policies | ✅ aligné (plus de « 5 et 9 ») |
| P1 | Doublon mentions légales | ✅ CMS **301** → `/policies/legal-notice` |
| P1 | Footer sans raison sociale | ✅ SIREN live |
| P1 | Collections < 5 | ✅ les deux petites supprimées |
| P1 | Handle `…eau-adoucie` | ✅ renommé + 301 |

---

## Merchant Center

**A priori aucun compte GMC** (Hakim, 17/08, déclaratif). En revanche le canal Shopify
**Google & YouTube** (`Publication/357118574930`) est **installé** — des fiches y étaient
déjà poussées. 5 SKU hors-acquisition en ont été retirés le 18/08. Ne pas créer / soumettre
un GMC sans feu vert Hakim.

Avant soumission : QA 375 px (yeux). Vitals désinstallée. Reste
`CWILL(Trustoo) Reviews` — même famille de risque (avis).

---

## Ce que je n'ai pas pu vérifier

- Apps installées / désinstall (scope `read_apps` toujours absent)
- Checkout : **lu** (panier test, pas de commande) — Shopify Payments
  (Visa, MC, Amex, CB, Maestro) + Apple Pay + PayPal + Klarna. Pas d'icône CB
  dans FullStack. Maestro laissé masqué au footer.
- 301 : **faits** (constatés, follow → policy / fiche)
- Zoom image par image de **tout** le catalogue (échantillon 12+ featured : 0 texte incrusté)
- QA visuelle 375 px (yeux) — sticky ATC présent dans le HTML, date JS 6–10 j / 15 h

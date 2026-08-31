# Bonum Vitae — état courant

**Dernière mise à jour : 31/08/2026** — feed restreint + lecture GMC +
étude Waterdrop Europe (`journal/2026-08-31-etude-waterdrop-europe.md`).
[`TABLEAU.md`](TABLEAU.md) ·
[`journal/2026-08-18-gmc-existant.md`](journal/2026-08-18-gmc-existant.md).

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

**Compte existant :** Bonum Vitae **`5825588636`** (Hakim, capture 18/08).
Pas le compte suspendu de juin (`5806019978`). Produits **acceptés depuis ~7/08**
(courbe 28 j : limités → approuvés). **9 notifs lues par Hakim le 18/08 :**
rien d'important. **Ne pas créer / soumettre un autre GMC.**

Feed Shopify = canal **Google & YouTube** (`Publication/357118574930`).
Constaté API 18/08 : **18 ACTIVE** dessus, **10 hors** (5 hors-acquisition + LPS
+ kit + 3 brouillons). Le 6/08 GMC affichait **95** items — écart à recouper
dans le compte (variantes / reliquats), pas depuis Shopify.

Thème FullStack publié le 18/08 = changement brutal sur un GMC déjà en
fenêtre 30 j. Calme côté feed / policies GMC sauf mismatch.

**30/08 — cohérence des délais réparée.** CGV art. 8 et CGU disaient encore
« 8 à 13 jours ouvrés » et « France métropolitaine **et à l'international** »
contre 6–10 j / France seule dans la policy Expédition et dans GMC. Réécrit,
constaté live. FAQ « une petite semaine / expédiés de plus loin » remplacée
par 24–48 h + cutoff 15h + 6–10 j. Wallets et Klarna ajoutés aux CGV.

**Feed restreint 30/08 :** 10 fiches / **14 items**, plancher 66,90 €
(kit 129 € et LPS 149 € ajoutés). 10 fiches low-ticket hors Google, toujours
en vitrine. Courbe GMC 31/08 : ~95 → ~25–30 Approuvés (cible 14). Signal GO dans
[`journal/2026-08-30-audit-prelancement-ads.md`](journal/2026-08-30-audit-prelancement-ads.md).

**Tracking** : `AW-18325545481` + `GT-M34W44VB`, événement `purchase` câblé.

---

## Ce que je n'ai pas pu vérifier

- Apps installées / désinstall (scope `read_apps` toujours absent)
- Checkout : **lu** (panier test, pas de commande) — Shopify Payments
  (Visa, MC, Amex, CB, Maestro) + Apple Pay + PayPal + Klarna. Pas d'icône CB
  dans FullStack. Maestro laissé masqué au footer.
- 301 : **faits** (constatés, follow → policy / fiche)
- Zoom image par image de **tout** le catalogue (échantillon 12+ featured : 0 texte incrusté)
- QA visuelle 375 px (yeux) — sticky ATC présent dans le HTML, date JS 6–10 j / 15 h

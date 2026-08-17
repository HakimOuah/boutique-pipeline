# Audit GMC Terry — Maison Noirmont, 17/08/2026

> **~11h00.** Boutique publique `maisonnoirmont.fr` (Admin `v42pzp-h4`). Thème MAIN
> `TRAVAIL 15-08 — correctifs` (`205451100498`). Visiteur anonyme (`curl`, pas de session).
> Grille : skill `gmc-acceptance` — Fast-Track GMC Approval Framework 2026 + GMC Guidance &
> Compliance Checklist (Terry Ecom), adaptée FR.
>
> **Aucun compte Merchant Center créé.** **Aucun brouillon activé.** Aucune écriture thème,
> politique, produit, collection. Tactiques proxy / anti-détection du playbook : **écartées**
> (règle maison).
>
> Passe précédente : [`2026-08-15-repasse-conformite-2.md`](2026-08-15-repasse-conformite-2.md).

---

# VERDICT

## ⛔ PAS PRÊT à créer ni à soumettre un compte Merchant Center.

Deux raisons distinctes, à ne pas mélanger :

1. **Décision déjà tranchée** : GMC Noirmont après **30 jours Tuftéo**. Le domaine Noirmont
   lui-même n'a que **24 jours** (création AFNIC `2026-07-24`).
2. **Checklist Terry** : plus aucune contradiction publique du type « le site se ment à
   lui-même » — celles du 15/08 sont **soldées en live**. Il reste des **red flags Terry**
   (collections < 5, marque tierce dans des titres, images partagées) plus le pré-build
   (Gmail dédié, isolation Ads) qui ne se voit pas sur le storefront.

**Ce n'est plus « 20 minutes de thème ».** Le storefront tient. Ce qui bloque une soumission,
c'est l'ordre d'ouverture, l'âge du domaine, et trois écarts de catalogue déjà connus.

**Addendum Hakim 17/08 ~11h15.** Âge du domaine : **accepté** (pas éliminatoire). Présidentiel :
**on laisse**. Collections < 5 : **on garde**, on n'invente pas de produits. Recoupe politiques
(hors dates) + délais : **OK** — une seule fenêtre de livraison, deux formulations équivalentes
(14–21 j calendaires dans les contrats = 2 à 3 semaines en FAQ / fiches / pied de page / tarif
panier). Détail dans la checklist §3.

---

# À PART LES POLITIQUES, IL RESTE QUOI ?

Hakim a déjà le geste « redater 5 politiques (10/08 → 15/08) ». Hors ça :

### Bloque encore une review GMC (Terry)

| # | Point | État | Qui |
|---|---|---|---|
| 1 | **3 collections publiques < 5 produits** : `frontpage` **1**, `montre-squelette` **2**, `plongeuses` **3** | Red flag explicite Terry (« collections de moins de 5 produits »). **Gardées le 17/08.** | Accepté |
| 2 | **« Présidentiel / Président »** dans 3 titres publics + descriptions + `alt` | Nom de bracelet Rolex, part au flux Shopping. Arbitrage A, non tranché. | Hakim |
| 3 | **9 fichiers image partagés** mère / enfant (`c-430162-*`, `c-690002-*`) | Checklist : pas d'images dupliquées entre produits. Les retirer recasse T-01. → T-36 | plus tard |

### N'est plus un mensonge, à traiter ou non

| Point | État |
|---|---|
| **« Qualité Premium »** dans le bandeau des fiches | Toujours là. Allégation invérifiable. Arbitrage C, pas urgent. |
| **Google Pay** | Picto **absent**. `googlePayConfig: null`. Plus un mensonge. Case à cocher si on veut le moyen (T-53). |
| **Mesure d'achat (GA4)** | Absente. Bloque **Ads**, pas la review GMC. Région cookies EEE+UK **avant** T-10. |

### Ops catalogue — pas GMC

T-07 (photos AliExpress des brouillons) · ne pas activer les 20 · T-14 (12 fiches actives sous cible visuels) · T-15 (guichet « 42 ») · T-59 (4 Unmapped DSers) · arborescence T-21/T-24.

---

# CE QUI A CHANGÉ DEPUIS LE 15/08 — soldé en live

Les **6 défauts** de la repasse T-54, relevés à nouveau le 17/08 sur l'accueil + 5 fiches
(`trente-neuf-classique-cannelee`, `barrettes-de-rechange-270` à 12,90 €,
`bracelet-presidentiel-dore`, `coffret-douze-aluminium`, `heritage-vert-plongeuse-vintage-42`)
+ Contact, La Maison, FAQ, 5 politiques.

| Défaut du 15/08 | 17/08 |
|---|---|
| Délai **24 h vs 48 h** (footer, cartes, accordéon) | ✅ **48 h partout** dans le texte visible. 0 « sous 24 h ouvrées ». Les « 24H » restants sont des traces SVG / « échelle 24 heures ». |
| Pied de page **sans adresse ni raison sociale**, tél. brut `0756828094` | ✅ **OH Ventures**, **47 rue Vivienne, 75002 Paris**, `mailto:contact@maisonnoirmont.fr`, `tel:+33756828094` → `+33 7 56 82 80 94`. TTC dans le même bloc. |
| Garantie fiches **« mouvement, couronne, aiguilles »** | ✅ Cartes + pied de page : *« Sur le mouvement, pendant 12 mois »*. Accordéon aligné sur le **mouvement interne**, exclusions bracelet / verre / boîtier. |
| Bandeau **« Paiement en 4 fois »** (y compris sous 30 €) | ✅ **0 occurrence** de « 4 fois » sur les pages relevées. 5e item du bandeau = **« Paiement sécurisé »**. Bloc dynamique : *« Paiement en plusieurs fois avec »* Klarna + PayPal, **absent** à 12,90 €, **présent** à 279 €. |
| JSON-LD `Organization` **invalide** | ✅ `json.loads` OK. `legalName: OH Ventures`, e-mail `.fr`, tél., adresse complète, `@id`. Pas de `sameAs` (aucun réseau — correct). |

Thème live confirmé : `Shopify.theme.id = 205451100498`.

---

# CHECKLIST TERRY — pass / fail

Légende : ✅ pass · ⛔ fail · ⚠️ écart accepté ou hors storefront · — non applicable (GMC non créé).

## 1. Pré-build

| Item | Verdict | Preuve / note |
|---|---|---|
| Domaine 30+ jours | ⛔ | WHOIS AFNIC : créé **2026-07-24** (~24 j). Terry : 30+ améliore le trust. |
| Pas un domaine supprimé/récupéré | ✅ | Création neuve 24/07/2026. |
| Gmail neuf dédié GMC+Ads, réchauffé | ⚠️ | Hors storefront. À faire **avant** création du compte, distinct de Tuftéo. |
| SIM physique, même n° partout | ⚠️ | N° boutique = **+33 7 56 82 80 94**, identique footer / JSON-LD / Contact / policies. Vocal non testé ici. Même société qu'OH Ventures : isolation « une adresse par boutique » **impossible** sans fausse adresse — on ne la fabrique pas. |
| Proxy + anti-detect | — | **Écarté** (règle maison). |
| 1 GMC / 1 Ads / 1 Gmail / 1 moyen de paiement par boutique | ⚠️ | GMC Noirmont **non créé**. Isolation Ads vs Tuftéo : à tenir le jour J. |

## 2. Build — confiance

| Item | Verdict | Preuve |
|---|---|---|
| E-mail `mailto:` professionnel | ✅ | `contact@maisonnoirmont.fr` ×2 dans le footer. 0 Gmail en façade. |
| Téléphone cliquable, joignable | ✅ | `tel:+33756828094`. Vocal : à Hakim de décrocher avant soumission. |
| Adresse réelle, localisable | ✅ | 47 rue Vivienne, 75002 Paris — footer **et** JSON-LD (`47 Rue Vivienne`). |
| Footer = policies = (futur) GMC | ✅ storefront | Identité alignée. GMC pas encore là : recopier **mot pour mot** le jour J. |
| Page À propos humaine, pas d'historique inventé | ✅ | `/pages/la-maison` 200. |
| Pas de réseaux faibles / neufs liés | ✅ | 0 Instagram / TikTok / Trustpilot. Pas de `sameAs`. |
| Trustpilot < 3,0 | ✅ | Pas de Trustpilot. Mieux qu'un mauvais. |
| ™/© seulement si droits réels | ✅ | Pas de ™ abusif relevé. |
| Pas de fausse urgence | ✅ | 0 stock limité, 0 compte à rebours, 0 « X clients », 0 avis publiés. |
| Icônes de paiement = checkout réel | ✅ | Pictos rendus : Visa, Mastercard, Amex, Cartes Bancaires, Shop Pay, Apple Pay, PayPal, Klarna. **Pas** de Google Pay. `/payments/config` : Shop Pay, PayPal, Apple Pay ; `googlePayConfig: null`. Klarna via `enabled_payment_types` (l'endpoint `/payments/config` n'expose pas les passerelles classiques). |

## 3. Policies

| Item | Verdict | Preuve |
|---|---|---|
| Policies dans `/policies/*` seulement | ✅ | Footer → shipping, legal-notice, privacy, refund, terms-of-sale, terms-of-service, contact-information. |
| Pas de page policy dupliquée | ✅ | `/pages/mentions-legales` → **301** `/policies/legal-notice`. Cookies = page CMS dédiée (pas un doublon Shopify). |
| Chiffres identiques partout | ✅ sur le fond | Traitement **24–48 h ouvrées** (expédition §3) + délai total **14–21 j** / **2–3 semaines** (FAQ, tarif panier, bandeau). Rétractation **14 jours**, même portée. Garantie **12 mois / mouvement**. Réponse SAV **48 h**. |
| Dates de version | ⛔ cosmétique | Expédition, remboursement, CGU, confidentialité : **10 août 2026**. Mentions légales : **15 août 2026**. CGV modifiées le 15 (URL CM2C) sans changement de date. → T-H2, 2 min Hakim. **Pas un mismatch de chiffres.** |
| Wording Shopify = GMC | — | GMC non créé. |

## 4. Produits, collections, feed

**Collections publiques** (sitemap = 14 loc, toutes 200 ; `products.json` = ce qu'un visiteur voit, pas l'Admin) :

| Handle | Public | Seuil 5 |
|---|---:|---|
| frontpage | 1 | ⛔ |
| montre-squelette | 2 | ⛔ |
| plongeuses | 3 | ⛔ |
| montre-cadran-a-chiffres | 5 | ✅ pile |
| gmt | 6 | ✅ |
| outils-d-horloger | 8 | ✅ |
| ecrins-et-rouleaux | 9 | ✅ |
| bracelets | 10 | ✅ |
| remontoirs | 11 | ✅ |
| chronos | 12 | ✅ |
| sport-chic | 15 | ✅ |
| classiques | 19 | ✅ |
| accessoires | 39 | ✅ |
| montres | 57 | ✅ |

`porte-montre` : page **404**, `products.json` **0** — **non publiée**, absente du sitemap. Pas une collection vide crawlable.

**Produits**

| Item | Verdict |
|---|---|
| Titres / SKU uniques, format maison | ✅ SKU `NOIR-*` (T-32). 4 vides = carte cadeau, à **exclure du feed**. |
| Pas de claims santé / résultats | ✅ |
| Pas d'avis faux | ✅ 0 `aggregateRating` / review. Badges Trustpilot dormants `disabled`. |
| « Qualité Premium » | ⚠️ bandeau fiches + 1× accueil |
| Présidentiel / Président | ⛔ titres publics : `bracelet-presidentiel-dore`, `bracelet-presidentiel-acier-inoxydable`, `voyageur-or-gmt-president` |
| Images texte incrusté / collages | ✅ catalogue public (audits 15/08). Brouillons : T-07, non servis. |
| Images dupliquées entre produits | ⛔ T-36 (9 fichiers, 2 mères + enfants) |
| Image de variante = variante | ⚠️ à surveiller au feed ; hors périmètre de cette passe |
| 404 redirigées | ⚠️ **0 lien mort** sur 46 hrefs de l'accueil. Sitemap produits / collections / pages : 200. Collections de pièces **non publiées** (`/collections/cadrans`, etc.) répondent **404** si on tape l'URL — non liées, hors sitemap. Terry est plus strict (« toutes les 404 redirigées ») : pas un fail crawlable aujourd'hui. |
| Vitesse > 65 | ✅ TTFB accueil ~0,15 s, fiche ~0,17 s (curl). Passe 15/08 : 0,31–0,60 s page complète. |
| Anciens codes GMC | ✅ 0 `google-site-verification`, 0 `noindex` sur les pages relevées. |
| Thème unique | ✅ FullStack, pas un clone Tuftéo. |
| Ruptures archivées | ⚠️ non re-scanné ce matin ; 10 archivées connues. |

Livraison panier (adresse 75002) : **« Livraison offerte — suivie », 0,00 €**, « 2 à 3 semaines ». Cohérent.

## 5. Création GMC — ne pas dérouler

Ordre Terry : boutique finie → policies figées → produits → **création GMC** → DNS TXT → recopier policies mot pour mot → Simprosys → review.

**Stop avant l'étape 4.** Indexer un GMC maintenant figerait un domaine de 24 jours et trois collections sous le seuil.

## 6. Avant review (quand ce sera le moment)

- [x] Auto-audit storefront (cette note)
- [x] Footer = identité (e-mail, tél., adresse)
- [x] Policies accessibles, pas de noindex
- [ ] Zéro 404 « dures » si on publie des collections de pièces — aujourd'hui elles sont 404 volontaires
- [ ] Numéro testé en vocal
- [ ] Collections < 5 : soit peupler (≥ 5 **publics**), soit retirer du menu / dépublier `montre-squelette` et `plongeuses` (Hakim a choisi de garder)
- [ ] Présidentiel tranché
- [ ] Policies recopiées dans GMC **après** la date de version à jour
- [ ] Un seul item en échec → ne pas soumettre

---

# HORS CHECKLIST, UTILE

- **Configurateur** (`/pages/configurateur`, 200) : plus de « pièce unique / sur mesure ». Copy catalogue, rétractation identique.
- **Consentement cookies** : conforme FR (15/08). Région EEE+UK avant T-10.
- **Sitemap** : index 200 (un fetch sans suivi de redirect peut répondre 500 — le loc canonique tient).
- **ProductGroup** JSON-LD des fiches : JSON valide. Offres dans `hasVariant`.
- **Carte cadeau** : 4 SKU vides → exclure du feed, ne pas « corriger » en inventant des SKU.

---

# CE QU'ON NE FAIT PAS APRÈS CET AUDIT

- Créer le GMC Noirmont.
- Activer un brouillon.
- Publier une collection de pièces pour « remplir » un seuil.
- Inventer un second siège social pour satisfaire l'isolation d'adresse Terry.
- Recoller un picto Google Pay sans cocher le portefeuille.
- Demander une review « pour voir ».

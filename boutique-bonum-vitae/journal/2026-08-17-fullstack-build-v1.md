---
type: journal
boutique: bonum-vitae
date: 2026-08-17
nature: intervention
leviers: [page, technique]
titre: "17/08/2026 (nuit) — FullStack v1 : purge démo, DA appliquée, home + fiche produit montées"
---

# 17/08/2026 (nuit) — FullStack v1 : purge démo, DA appliquée, home + fiche produit montées

> Thème cible : `copie-de-fullstack-2-3` (**205568147794**, UNPUBLISHED). Le MAIN Horizon n'a pas
> été touché. Rien n'est publié. Demande Hakim : porter les contenus Horizon, reconstruire le
> template produit, garder les couleurs existantes, monter en qualité, respecter le GMC.
>
> **Préview (session navigateur) : `https://kw7vak-g0.myshopify.com?preview_theme_id=205568147794`**
> · Éditeur : `https://kw7vak-g0.myshopify.com/admin/themes/205568147794/editor`

## Méthode

Lecture préalable (ordre du prompt) : reco Tuftéo (38 sections / 99 blocs, natif vs custom),
`structure-templates-log` + build home Tuftéo, pièges campement. Les fichiers ont été construits
en **deepcopy des structures du build Tuftéo** (`189437772161`, lecture seule) — clés de réglages
éprouvées — puis remplis avec les contenus Horizon Bonum Vitae. Pipeline : `theme pull` → édition
locale → `theme push --nodelete --only` → relecture API + comparaison sémantique JSON.

## Écrit sur le thème (8 fichiers, tous vérifiés par relecture distante)

| Fichier | Contenu |
|---|---|
| `config/settings_data.json` | 3 schemes recolorés charte BV (1 = blanc/Ardoise, 2 = Lin `#F7F4EE`, 3 = Abysse `#0E3A5A` inversé) ; accents Source `#35B6AA` (badges) et Laiton `#C3A15F` (étoiles, si un jour avis réels) ; **Fraunces n6** titres / **Inter** corps ; radius pro (boutons 12, cartes 14, inputs 8) ; logo BV ; **Klaviyo vendeur coupé** (`enabled:false`, clé `pk_ec8555…` vidée) ; les 8 URL sociales vidées ; police custom vendeur (Kumbh Sans, CDN étranger) retirée |
| `config/settings_schema.json` | défauts vendeur purgés : `facebook/instagram/youtube/linkedin_url` n'ont **plus de `default`** (le « ne peut pas être vide » interdisait `""`) |
| `templates/index.json` | hero image BV (Abysse, H1 « Une eau meilleure, à chaque point d'usage ») → marquee réassurance (Lin) → collection-featured Osmoseurs → 6 cartes collections → « Au quotidien » (image carafe) → **guide de choix BV porté** (tableau custom-code) → FAQ 5 questions → réassurance 3 colonnes → « Pourquoi Bonum Vitae ? » → newsletter (carte Abysse) |
| `templates/product.json` | ordre CRO : titre → prix → séparateur → description tronquée (Voir plus) → form (variantes + quantité + ATC sticky) → **`delivery-estimation` natif** (6-10 j ouvrés, coupure 15 h, hors week-end = la policy au chiffre près) → icônes paiement → 4 accordéons (Livraison & retours / Garantie / Entretien & consommables / Contact) → 3 lignes de confiance. Sous la flottaison : marquee, 4 USP image/texte (images CDN BV), FAQ 6 objections, recommandations |
| `templates/collection.json` + `search.json` | bloc **`rating-stars` de démo retiré** de chaque |
| `templates/password.json` | badge **« Powered by FullStack » retiré** |
| `sections/header-group.json` | announcement unique « Livraison offerte, sans minimum d'achat », menu `main-menu`, logo 34 px |
| `sections/footer-group.json` | 4 cartes réassurance + footer Abysse : logo, baseline, **OH VENTURES (SASU) — SIREN 103157251, 47 rue Vivienne, 75002 Paris**, e-mail + téléphone cliquables, menus Boutique / Informations / Politiques, newsletter, liste policies, icônes paiement auto (`payment-methods` natif = moyens réels), copyright |

Rejets corrigés en route (le premier push « réussissait » en les avalant — le `--json` les montre) :
`padding < 10` refusé par le schéma FullStack (6 occurrences clampées) ; `default` vide refusé sur
`linkedin_url`. Et le `main` Tuftéo embarquait un bloc statique **`rating_badge` Trustpilot
« 4,8/5 · 789 avis » hors `block_order`** — attrapé par le contrôle anti-preuve-sociale, retiré.

## Garde-fous GMC appliqués au contenu

- **0 preuve sociale** : pas d'avis, pas d'étoiles, pas de badge Trustpilot, pas de compteur. Le
  widget Trustoo n'est **pas** posé sur le nouveau template (à réintroduire quand il y aura des
  avis réels).
- **Délais partout = policy** : expédition 24-48 h, total 6-10 j ouvrés, livraison offerte France.
  L'ancien accordéon Horizon disait « 4-8 jours » (faux) — non porté.
- **« Retours gratuits » non porté** (la policy met les frais de renvoi à la charge du client) →
  « Rétractation 14 jours après réception », renvoi organisé avec le service client.
- **« 14 jours satisfait ou remboursé » non porté** (surpromesse vs policy) — même correction que
  Noirmont.
- **Hero reformulé** : « sans travaux ni plombier » (P1) → « à chaque point d'usage » ; l'USP 2 dit
  honnêtement « la plupart de nos produits… quand une installation demande plus, nous le disons ».
- **Newsletter sans « -10 % »** tant qu'aucun code promo réel n'est prouvé (à réintroduire si Hakim
  crée le code).
- Anti-calcaire : la carte collection porte « présentés sans surpromesse » ; la FAQ garde le
  paragraphe DGCCRF (« aucune réduction de la dureté »).
- Aucune URL CDN Tuftéo/Noirmont : images = fichiers `shopify://shop_images/` de Bonum Vitae ;
  la vidéo héro Tuftéo n'a pas été reprise.

## QA restant (préview navigateur — curl ne transmet pas `preview_theme_id`, 503 confirmé)

1. Mobile 375 px d'abord : hero (texte sur image), marquee, cartes collections, tableau comparatif
   (défilement horizontal), accordéons, sticky ATC.
2. Icônes Material à contrôler visuellement : `water_drop`, `balance`, `assignment_return`, `lock`,
   `local_shipping`, `support_agent`.
3. `delivery-estimation` : vérifier la date rendue en français.
4. Le footer `payment-methods` natif liste les moyens réellement actifs — recouper avec le checkout.
5. Fiche osmoseur : le suffixe `product.osmoseur.json` n'existe pas sur FullStack → la fiche
   `osmoseur-ro-600g` retombe sur `product.json` (voulu pour v1 ; template dédié = ticket suivant).

## Non fait / tickets suivants

- Panier tiroir (recette Tuftéo 12b : bannière + upsell) — T-11.
- Template collection : enrichissement (hero de collection, texte SEO) — natif à configurer.
- Pages Notre histoire / FAQ / Contact sur FullStack (elles rendent via `page.json` démo).
- Mégamenu illustré (pattern Noirmont) — optionnel.
- Purge des assets vendeur inutilisés (`logo-fullstack.png`, `powered-by-fullstack.svg`,
  placeholders) — cosmétique, rien ne les référence plus côté rendu.

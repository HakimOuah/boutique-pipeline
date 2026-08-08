# NOIRMONT — Plan de krakenisation (08/08/2026)

**Objectif** : finaliser Maison Noirmont comme première application complète de la roadmap Kraken (`drop-elite-google-os/skills/creer-boutique-niche-google/references/strategie-pas-a-pas.md`). Décision Hakim du 08/08. Clin d'œil de calibrage : la boutique mature d'Enzo est **Montre Avenue** — même univers.

---

## 1. AUDIT DE L'EXISTANT

### Ce qui est fort (acquis, ne pas retoucher)

| Actif | État | Source |
|---|---|---|
| **Marché validé niveau 2** | seiko mod 38 690/mois KD 10 CPC 0,22 ; arabic dial ~15 500 sans occupant fort ; montre squelette ~8 400 ; **enchère quasi vide** (seul montreapapy, 212 $/mois) | `marche-complet-semrush.md`, phase 3-4 registre |
| **Catalogue propre** | 92 fiches actives (53 montres + 38 accessoires), DSers 98 mappés 0 Unmapped, découpage coloris fait (92 variantes, SKU vérifiés), 117 libellés renommés, échelle de prix par mouvement | `BILAN-2026-07-25.md` |
| **Véracité produit** | 351 images fournisseur supprimées ; loupe saphir corrigée ; VK63 documenté méca-quartz ; 12 variantes siglées neutralisées (DENY réversible) | `veracite-produit-cloture.md` |
| **Charte & design** | Direction A+B (encre/craie/cyan instrument), collections modernisées, PDP à galeries 7 images | `charte-noirmont-2026-07-25.md` |
| **Configurateur V2** | « Votre Noirmont en trois étapes » — découverte guidée, 34/34 chemins vers vraies variantes, vocabulaire vérifiable | `configurateur-implementation.md` |
| ~~Site en ligne~~ **CORRIGÉ 08/08 soir** | La boutique est **toujours sous mot de passe** (302 vers `/password` en requête anonyme) ; le live vu au navigateur venait de la session preview de Hakim. Le thème MAIN reste `Helio` — le thème travaillé n'est pas publié. | vérification anonyme 08/08 |
| **Positionnement** | « Cadran vierge de tout logo emprunté » — différenciant honnête vs mods contrefaits | live |

### Les risques bloquants constatés au live du 08/08 (avant toute pub)

1. **⚠️ P0 — Widget « Excellent · 1340 avis »** sur la home d'une boutique à 0 commande. Si ce sont des avis démo/placeholder : **misrepresentation GMC caractérisée** + risque DGCCRF. Décision Hakim requise (chasse gardée avis/sliders) : retirer, ou remplacer par un module vide alimenté par de vrais avis post-lancement.
2. **P0 — Badges « En promotion » généralisés + prix barrés** (relevé au bilan) : des prix de référence non justifiables = tueur GMC n°1. Arbitrer : prix nets sans barrés pour l'examen (état `GMC_READY`), promotions réelles réintroduites ensuite (`GROWTH_MARKETING`).
3. **P0 — Vérité fournisseur non éprouvée** : la **commande test** (SUB stérile Tandorio retenue au registre, niveau 2) n'a jamais été passée. La méthode interdit de dépenser en pub sans vérité produit (délais réels J+14/21, qualité, absence de logo sur pièces livrées). Décision Hakim.
4. **P1 — Reliquats bilan 25-27/07** : 88 visuels de variantes à produire ; 13 fiches accessoires à importer **via DSers** ; compteurs DSers à confirmer visuellement ; 9 valeurs non identifiées ; fiche « chiffres romains » (corriger l'image, pas le texte) ; cartes cadeaux à activer ; thème fork obsolète `204329288018` à supprimer.

---

## 2. LES GAPS KRAKEN — ce qui manque, phase par phase

### Phase 3-4 — Catalogue & arborescence d'acquisition (le chantier n°1)

Le site vend des **montres finies** ; or le gisement mesuré est le **vocabulaire du mod** (38 690/mois) et des **cadrans arabes** (15 500, personne au-dessus de la P4). C'est la stratégie tranchée dans `marche-complet-semrush.md` — elle n'est pas encore traduite en catalogue/arborescence.

- **4.A — Ouvrir la gamme « Pièces & Mod »** (c'est le passage 92 → 200 produits à la Kraken) : cadrans (arabes, stériles, squelette), lunettes/inserts, aiguilles, verres, bracelets par type, outils de modding, kits débutant. La phase 4d (`phase4d-accessoires-skx-2026-07-24.md`) a déjà exploré accessoires + base SKX : la réactiver comme plan de sourcing. Règle gate v3 : 10-20 produits/sous-catégorie, best-sellers AliExpress d'abord.
- **4.B — Collections d'acquisition** à créer/recaler : `Cadran arabe` (15 500 — opportunité n°1 non exploitée), `Montre squelette` (8 400), `Seiko mod` (pièces + montres moddées, 38 690), en plus des familles existantes (Plongeuses, GMT, Chronos…). Étiquettes par mouvement/taille/couleur, jamais de catégories dupliquées.
- **4.C — Fiches** : mot-clé de sous-catégorie dans le titre (plan `seo-titles-produits.md` à étendre aux nouvelles gammes), ≥ 250 mots, meta complets.
- Sortie attendue : arborescence chiffrée complète (KMT export sur seiko mod / cadran arabe / squelette / pièces) + catalogue ≥ 200 à horizon 60 jours.

### Phase 5 — Conformité, GMC, tracking (P0, avant tout euro de pub)

- **Audit anti-misrepresentation complet** (checklist `239965951`/`262936735`) : avis (point 1 ci-dessus), promos (point 2), cohérence délais J+14/21 partout (site = CGV = FAQ = fiches = checkout — `pages-legales-et-delais.md` à re-vérifier après les évolutions), footer tél + email, pictos paiement = moyens réels du checkout, pages légales du **checkout** Shopify (distinctes du footer), zéro claim « swiss made » non prouvé (PT5000 ≠ swiss made), mention explicite méca-quartz sur VK63.
- **État `GMC_READY`** : version sobre publiée pour l'examen (retrait couche promo/marketing), puis transition documentée vers `GROWTH_MARKETING`.
- **Compte Ads mode expert** (devise/fuseau irréversibles, promo 400 €, 2FA) + **Merchant Center via CSS** (Deshops — codes partenaires Kraken) — n'ouvrir le compte CSS que site 100 % propre ; **gel du site ~8 jours** après soumission.
- **Flux Simprosys** (plan payant, ID produit = ID Shopify, variantes incluses, GTIN `identifier exists = false`) + custom labels par collection et par ROAS break-even (Rentability ou tags CSV).
- **Tracking** : conversion **Achat** unique en principal (valeur dynamique, défaut = panier moyen ~330 €), add-to-cart/checkout en secondaire, attribution data-driven, GA4 lié, **Consent Mode V2** (Pandectes ~9 $/mois), server-side en option (+15-40 % de data, ~60 €/mois).

### Phase 6-7 — Lancement Ads (l'enchère est vide : opportunité majeure)

- **Shopping standard** (jamais PMax d'entrée) : CPC manuel cohérent budget (30-50 €/j → CPC ~0,20-0,30 sur un marché à 0,22), géo France en « Présence » uniquement, mobile/tablette −40 %, objectif unique **15 conversions** → bascule tROAS par paliers. Ticket 279-430 € + CPC 0,22 → **ratio prix/CPC > 1 000** : économie exceptionnellement favorable.
- **Search branding** `[maison noirmont]` exact + expression, 5-10 €/j, RSA sobres, composant promotion, tROAS ~500 % rapide.
- **Optimisation hebdo** (jamais plus) : impressions perdues budget, devices, groupes produits, termes de recherche (exclusions évidences vs data 150-200 €), produits 1-2× prix sans conversion.
- **Remarketing** à ~J+21 : display dynamique flux MC + Demand Gen, 10 €/j, « ciblage optimisé » DÉCOCHÉ, acheteurs exclus. Meta retargeting catalogue ~5-10 €/j quand le pixel a 7 j de data.
- Stratégie de portefeuille (tROAS + cap CPC) obligatoire sur la marque.

### Phase 8 — SEO continu (le pont vers la marge long-terme)

- **Playbook Goteia** : 66 % de son trafic vient d'UN article premier sur `seiko modifications` (6 600/mois). Créer l'article pilier équivalent + grappe (mod ou hommage — `article-mod-ou-hommage.md` existe déjà en brouillon !), guides par mouvement (NH35 vs Miyota vs PT5000), guides cadrans arabes.
- Ratios contenu : niche type de produit → 4 intentionnistes / 1 informatif ; ~3 contenus/mois minimum ; indexation GSC immédiate à chaque publication.
- **Netlinking** : domaine neuf → 4 premiers mois de liens vers l'accueil, puis cycles de 4 mois sur 2 collections (cadran arabe + seiko mod en premiers), montée en qualité progressive.
- Pilotage GSC à M+2 : booster les pages pré-rankées (~position 30).

### Phase 9 — Backend (dès les premières ventes)

- **Email** : Brevo (code ENZO50, facturation aux envois) — popup (code donné directement dans la popup ET par email), flows panier abandonné (promo à l'email 2-3 seulement), post-achat (avec suivi de colis J+14/21 : crucial vu les délais), bienvenue, win-back J+40.
- **Avis réels** : séquence J+10 sur produits satisfaits → remplace le compteur démo par du vrai (Trustpilot/Judge.me), c'est aussi un signal SEO.
- **SAV** : outil léger (Help Scout), anticipation des délais (séquences de patience), FAQ montres (réglage bracelet, étanchéité, mouvement).
- **Social** : PostPilot (Make) 1 produit/jour, community management minimal.

---

## 3. SÉQUENCEMENT PROPOSÉ

**Sprint 1 (S1-S2) — Déblocage & conformité (P0)**
① Décisions Hakim : avis démo · badges promo/prix barrés · 12 variantes siglées · commande test Tandorio (lancer MAINTENANT : 3-4 semaines de délai, c'est le chemin critique).
② Reliquats bilan : import 13 accessoires via DSers, compteurs DSers, fiche romains, cartes cadeaux, suppression thème fork.
③ Audit anti-misrepresentation complet + corrections + état `GMC_READY`.

**Sprint 2 (S2-S4) — Infrastructure d'acquisition**
④ Compte Ads + CSS/MC + flux Simprosys + tracking + consent mode (gel 8 jours du site pendant l'examen).
⑤ KMT exports + arborescence chiffrée (seiko mod / cadran arabe / squelette / pièces) ; création des collections d'acquisition.
⑥ Démarrage sourcing gate v3 « Pièces & Mod » (92 → 200 produits, priorité cadrans arabes).

**Sprint 3 (M+1) — Lancement**
⑦ Réception + contrôle commande test (qualité, délai réel, stérilité des cadrans) → GO/NO-GO pub.
⑧ Shopping + branding ; article pilier seiko mod + 2 guides ; premiers liens accueil.
⑨ Brevo flows + popup + séquence avis.

**Sprint 4 (M+2-M+3) — Optimisation & Q4**
⑩ 15 conversions → tROAS ; remarketing ; optimisations hebdo.
⑪ Cadence contenu 3-4/mois + netlinking collections ; GSC.
⑫ Préparation Q4 (une montre = cadeau) : stocks tampon best-sellers chez le fournisseur, offres coffrets (montre + bracelet + outil), promos progressives dès début novembre — la marge se fait sur la black week.

**Critère de succès à M+3** (calibré sur les benchmarks Enzo) : boutique rentable ou break-even sur Shopping avec tROAS actif, 200+ produits, 1er trafic SEO naissant — trajectoire Style Hippie (~11 k visites réelles = zone de rentabilité), pas besoin de plus pour gagner.

## 4. Décisions de Hakim — TRANCHÉES le 08/08 (voir [APPLICATION-DECISIONS-2026-08-08.md](APPLICATION-DECISIONS-2026-08-08.md))

Les 6 décisions ont été prises et appliquées : avis retirés, prix barrés supprimés (931 variantes), commande test reçue et conforme (chemin critique levé), sigles déjà masqués (produit en brouillon + DENY), budget 30 €/j, GO sourcing. Restent : publication du thème et vérification DSers des 2 fiches « Voyageur Or ».

### Tableau d'origine (historique)

| # | Décision | Impact |
|---|---|---|
| 1 | Avis « 1340 » : retirer ou remplacer | Bloque GMC |
| 2 | Prix barrés/badges promo : passer en prix nets pour l'examen | Bloque GMC |
| 3 | Commande test Tandorio (~87-160 € selon modèle) | Bloque le lancement pub (chemin critique 3-4 sem.) |
| 4 | 12 variantes siglées : suppression définitive ou maintien DENY | Risque contrefaçon résiduel |
| 5 | Budget pub de lancement (30/50/100 €/j) | Dimensionne la phase 6 |
| 6 | Extension « Pièces & Mod » : GO sur le sourcing gate v3 | Le passage 92 → 200 |

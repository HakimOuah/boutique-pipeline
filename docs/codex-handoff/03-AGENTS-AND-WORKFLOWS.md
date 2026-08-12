# 03 — Agents, skills et workflows

> Dossier de passation Codex — généré le 2026-07-30.
> Étiquettes de source : **[FAIT — repo:chemin]** (vérifié dans les fichiers), **[MÉMOIRE]** (fiches mémoire Claude), **[NOTION]** (lu dans Notion le 30/07), **[HYPOTHÈSE]**, **[OBSOLÈTE POSSIBLE]**, **[CONTRADICTOIRE]**, **[MANQUANT]**.
> Racine projet : `/Users/Hakim/Documents/Boutiques drop` · Les agents/skills projet vivent dans `Boutiques drop/.claude/` (hors dépôt git `boutique-pipeline/`).
> Ce fichier est l'**inventaire** (qui existe, quoi, où) ; le **comportement d'orchestration** (comment ces agents sont briefés, parallélisés, contrôlés, repris après incident) : voir `16-MULTI-AGENT-ORCHESTRATION.md`.

---

## 1. Vue d'ensemble des couches

| Couche | Contenu | Où |
|---|---|---|
| **Skills projet** (orchestrateurs) | `/recherche-produit`, `/chasse-clusters`, `/qualifie-idees` — ils ne font rien eux-mêmes : ils lancent les agents, contrôlent les livrables, écrivent le registre | `.claude/skills/*/SKILL.md` **[FAIT]** |
| **Agents projet** (exécutants) | 9 agents : `phase0-decouverte` → `phase5-marge`, `sonde-prix`, `critique-candidat`, `mineur-brandsearch` | `.claude/agents/*.md` **[FAIT]** |
| **Skills globaux** | 38 dans `~/.claude/skills/` : 10 « maison » e-commerce + packs skills.sh installés le 26/07/2026 | `~/.claude/skills/` **[FAIT]** |
| **Skills archivés** | `niche-scorer`, `competitor-analyzer`, `margin-calculator` | `~/.claude/skills-archive/` **[FAIT — dossier vérifié le 30/07]** |
| **Campement type Notion** | 20 tickets-briefs d'agents à dupliquer à chaque lancement de boutique | base `da8b39cc1a4248f2aec7494df5ef247b` **[NOTION — relu le 30/07]** |
| **Mémoire persistante** | 14 fiches (index `MEMORY.md`) relues par Claude à chaque session — décisions, pièges, recettes | `~/.claude/projects/-Users-Hakim-Documents-Boutiques-drop/memory/` **[FAIT]** |
| **Référentiels canoniques** | `PRODUCT-RESEARCH-CRITERIA.md` (seuils), `PRODUCT-RESEARCH-PLAYBOOK.md` (méthode), `PLAYBOOK.md` (lancement boutique), `registre-candidats.md` (anti-doublon) | `boutique-pipeline/` **[FAIT]** |
| **Espace Codex existant** | Adaptation indépendante de la boucle volume-first, déjà exécutée le 20/07 | `boutique-pipeline/codex-chasse-clusters/` + `~/.codex/skills/chasse-clusters-codex/` **[FAIT]** |

**Principe d'architecture central [FAIT — repo:specs/2026-07-17-pipeline-agents-phases-1-5-design.md] :** aucun critère chiffré n'est copié dans les agents. Chaque agent relit `PRODUCT-RESEARCH-CRITERIA.md` en début de mission. Un changement de critère se fait à un seul endroit. Deuxième principe : **fail-closed** — verdict négatif, cas limite (±20 % du seuil) ou donnée invérifiable = arrêt et remontée à Hakim, jamais d'invention de données.

---

## 2. Skills projet (orchestrateurs)

### 2.1 `/recherche-produit` — orchestrateur 5 phases (chemin A cadré)

**[FAIT — repo:.claude/skills/recherche-produit/SKILL.md]** · **Statut : actif** (voie pour une recherche cadrée sur une niche précise)

- **Objectif** : dérouler idéation → filtre → demande → sourcing → marge sur un brief donné.
- **Responsabilités** : lancer `phase1-ideation` à `phase5-marge` **séquentiellement, jamais en parallèle** ; contrôler chaque livrable (chemin, date du jour, sections obligatoires, interdits non enfreints) ; mettre à jour le registre **après chaque phase** ; appliquer l'arrêt fail-closed.
- **Outils** : outil Agent (sous-agents synchrones) ; lecture/écriture du registre.
- **Entrées** : brief de Hakim (niche ou consigne ; sans argument = exploration libre) + date réelle.
- **Sorties** : rapports datés dans `reports/`, registre à jour, rapport final en 5 sections (résultat, phase par phase, fichiers, candidats survivants avec toutes leurs réserves, décisions pour Hakim).
- **Critères de réussite / validation** : un livrable non conforme = arrêt de chaîne, pas de rattrapage silencieux. Sortie maximale : « commande test conseillée sous conditions ». Niveaux 3 (commande test) et 4 (lancement) jamais franchis.
- **Dépendances** : `PRODUCT-RESEARCH-CRITERIA.md`, `PRODUCT-RESEARCH-PLAYBOOK.md`, `registre-candidats.md`, spec `specs/2026-07-17-pipeline-agents-phases-1-5-design.md`.

### 2.2 `/chasse-clusters` — boucle autonome volume-first (chemin B)

**[FAIT — repo:.claude/skills/chasse-clusters/SKILL.md]** · **Statut : actif mais voie secondaire depuis le 20/07/2026** (sur demande explicite de Hakim, familles choisies à la main) **[FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md §7 + familles-exploration.md, bandeau « MIS DE CÔTÉ »]**

- **Objectif** : accumuler 20 candidats qualifiés (volume mesuré + concurrence + fiche AliExpress vérifiée) en autonomie totale, en balayant des familles de marché sur SEMrush **avant** toute idéation produit.
- **Responsabilités** : boucle `phase0-decouverte` → anti-doublon → `sonde-prix` → `phase2-filtre` → `phase3-demande` → `phase4-sourcing` → `critique-candidat` → écriture registre candidat par candidat → synchro Notion (base « Chasse aux clusters — juillet 2026 », ds `9490c443-…`) → auto-expansion des graines dérivées.
- **Garde-fous notables** : ne transmet **jamais** le compteur au critique ; ne baisse jamais le seuil ; règle des « 3 familles consécutives stériles » = arrêt ; viviers ≠ rejets (marchés à volume réel mais low-ticket) ; registre local d'abord, panne Notion non bloquante (`notion-sync-pending.md`).
- **Entrées** : `familles-exploration.md` (40 familles, éditables par Hakim), `registre-candidats.md`.
- **Sorties** : lignes registre avec confiance fournisseur A/B/C, fiches Notion, rapport final 7 sections.
- **Dépendances techniques** : SEMrush via Chrome connecté (MCP `claude-in-chrome`), Google Shopping, AliExpress. Écran de connexion = arrêt (jamais de saisie d'identifiants).
- **Bilan réel** : lancée via `/loop` le 20/07 — 7 familles balayées, 1 seul RETENU (fontaine à gravité), arrêt réglementaire sur 3 familles stériles ; coût ≈ 840 k tokens/famille **[MÉMOIRE — boucle-chasse-clusters-volume-first.md]**.

### 2.3 `/qualifie-idees` — qualification express (voie principale)

**[FAIT — repo:.claude/skills/qualifie-idees/SKILL.md]** · **Statut : actif, voie principale depuis le pivot du 20/07/2026 après-midi**

- **Objectif** : voie hybride « les idées redeviennent la source, mais chaque idée est mesurée avant qu'on y investisse quoi que ce soit ». Une idée sans volume meurt en quelques minutes (mesure express ≈ 6 min), pas après une phase 3 complète.
- **Chaîne par idée** : 0 anti-doublon → 1 mesure express (`phase0-decouverte` en mode ciblé sur l'idée nommée) → 2 `sonde-prix` → 3 `phase2-filtre` → 4 `phase3-demande` → 5 `phase4-sourcing` → 6 `critique-candidat` → 7 écriture registre au fil de l'eau → 8 synchro Notion.
- **Entrées** : idées de Hakim, ou **minage Brand Search par défaut** (`mineur-brandsearch`). Exploration latérale encouragée mais bornée : une idée `latérale` refait toute la chaîne depuis l'étape 0.
- **Sorties** : mêmes livrables que la boucle + statut Notion `STOP mesure express` pour les morts précoces.
- **Validation** : cas limites (bande ±20 % du seuil) jamais tranchés par un agent — remontés à Hakim en fin de session.
- **Note** : `phase1-ideation` et le balayage par familles sont explicitement « mis de côté » par ce skill — à n'utiliser que sur demande de Hakim.

---

## 3. Agents projet (`.claude/agents/`)

Tous **[FAIT — repo:.claude/agents/<nom>.md]**, tous en français, tous soumis aux restrictions globales : aucun contact vendeur, aucun achat/panier/connexion à un compte, aucune modification Shopify / Google Ads / Merchant Center, aucune publication, aucune réserve jamais supprimée, étanchéité des 4 niveaux de validation (marché → fiche AliExpress → commande test → lancement).

| Agent | Objectif | Outils réels | Entrées | Sorties | Gate de sortie / interdits clés | Statut |
|---|---|---|---|---|---|---|
| **phase0-decouverte** | Balayer une famille (ou mesurer une idée en mode ciblé) sur SEMrush France et rendre les clusters ≥ seuil — « le volume est mesuré avant qu'aucun produit ne soit imaginé » | Chrome connecté (Keyword Magic Tool, `db=fr` obligatoire) | famille + graines, ou idée nommée | `reports/chasse-clusters-<famille>-<date>.md`, 7 sections | Jamais d'addition de familles distinctes (anti-exemple **catio**) ; aucun produit proposé, aucun verdict ; chaque chiffre lu à l'écran et daté | **Actif** |
| **phase1-ideation** | Collecter 20-50 idées brutes pré-filtrées (Amazon, VEVOR, Flippa, Pinterest, Reddit…) | Web + navigateur | brief ou exploration libre | `reports/phase1-ideation-*.md` | Aucun scoring, aucun volume, aucun verdict | **Actif mais mis de côté** (source secondaire depuis le 20/07) |
| **phase2-filtre** | Filtre qualitatif + thèse produit en une phrase par survivant (« Pour [persona] qui… contrairement aux concurrents qui… ») | lecture rapports + vérifs web datées | rapport phase 1, ou cluster + fourchette sonde (chemin B) | `reports/phase2-filtre-*.md`, shortlist + rejets motivés | Aucun chiffre SEMrush, aucun verdict marché ; chemin B : produits **attestés par le vocabulaire mesuré** uniquement ; poches non instruites versées en vivier | **Actif** |
| **phase3-demande** | Demande réelle : cluster adressable après nettoyage SERP, verdicts GO marché / À APPROFONDIR / STOP / CAS LIMITE | SEMrush + SERP Google FR via Chrome | rapport phase 2 | `reports/phase3-demande-*.md` | **Règle hiérarchique obligatoire** (spécifique → famille → parent ; erreurs documentées : suspension rotin XXL, bateau amorceur) ; ne tranche jamais un cas limite ; référence de rigueur : `reports/validation-semrush-2026-07-17.md` | **Actif** |
| **phase4-sourcing** | Sourcing AliExpress des GO marché uniquement — URLs `/item/` exactes, relevés datés (variante, prix rendu, entrepôt, délai, vendeur) | AliExpress via Chrome | liste explicite des GO marché | `reports/phase4-sourcing-*.md` | Vocabulaire verrouillé : `AUCUNE OFFRE EXPLOITABLE` / `OFFRE TROUVÉE` / `FOURNISSEUR À TESTER` / `RETENU POUR COMMANDE TEST` — « GO fournisseur » **n'existe pas** ; un bon fournisseur ne renverse jamais un verdict marché | **Actif** |
| **phase5-marge** | Marge contributive, CPA max, CAC break-even vs CPC, budget test — raisonnement SASU/OH Ventures (HT, TVA au réel, IS) | calcul sur rapports 3+4 | rapports phases 3 et 4 | `reports/phase5-marge-*.md` | Le mot « marge » seul est interdit sans détail des coûts ; jamais de GO lancement ; chaque ligne de coût a un statut (réel/hypothèse/à confirmer) | **Actif** (jamais atteint par la boucle — volontaire) |
| **sonde-prix** | Fourchette de prix en 1 min sur Google Shopping FR, ~1 % du coût d'une phase 3 | Google Shopping (aucun site marchand visité) | mot-clé de tête | réponse directe, pas de fichier | Verdicts asymétriques : seul `LOW-TICKET` net écarte (→ vivier) ; « dans le doute, le produit continue » | **Actif** |
| **critique-candidat** | Contrôle à froid des 3 cases (volume / concurrence / fournisseur), verdict binaire RETENU / NON RETENU | lecture seule des rapports | dossier candidat **sans le compteur** | réponse directe : verdict + case par case + confiance A/B/C + réserves | Aveugle à l'avancement (anti-dérive de seuil) ; « si tu hésites, c'est non » ; case fournisseur = critère d'**existence** (décision Hakim 20/07), pas de qualité | **Actif** |
| **mineur-brandsearch** | Extraire des idées de niches **prouvées** (boutiques vivant en Google Ads FR sans Meta, prix ≥ ~130 $) | MCP Brand Search (quota 10 000 req/mois, budget ≤ 100/session) + repli UI web app.brandsearch.co | recette de filtres Hakim (`country_code: FR`, `meta_active_max: 0`, tri `google_ads_total`) | `reports/minage-brandsearch-<date>.md`, idées `directes`/`latérales` adossées à une boutique preuve | Aucun volume, aucun verdict, aucun sourcing ; estimations de revenus Brand Search jamais présentées comme des faits | **Actif** (source d'idéation principale depuis le 20/07) |

**Leçon d'exploitation [MÉMOIRE — brand-search-source-idees.md]** : vérifier la boutique preuve au **Google Ads Transparency Center région France** avant de s'y fier (contre-exemple wondermural : 30 ads seulement, en DE/IT — preuve invalidée).

---

## 4. Skills globaux (`~/.claude/skills/`)

### 4.1 Skills « maison » e-commerce (créés pour le projet)

Tous **[FAIT — repo:~/.claude/skills/<nom>/]** (SKILL.md + assets/references/scripts). Aucune boutique n'est en campagne à ce jour, donc la plupart n'ont **pas encore servi en production** — statut « prévu » = installé, non éprouvé. **[HYPOTHÈSE** sur l'usage réel : aucune trace d'exécution dans le dépôt pour la plupart**]**

| Skill | Objectif | Statut |
|---|---|---|
| `google-ads-launcher` | Campagnes Google Ads e-com (Shopping + Search), scripts, négatifs FR — porte les **règles Hakim** (budgets 15-20 €/j, Shopping Standard d'abord, seuils ROAS) | Actif comme « couche règles » — à invoquer **avec** `ads`/`ad-creative` **[MÉMOIRE — skills-sh-ecommerce-installes.md]** |
| `meta-ads-creator` | Campagnes Meta à partir des winners | idem — couche règles avec `ads`/`ad-creative` |
| `shopify-product-creator` | Fiches produit bulk via API Admin, descriptions AIDA | Prévu |
| `seo-content-pipeline` | Blog Shopify : keyword → article → indexation | Prévu |
| `klaviyo-flow-builder` | Flows email (abandoned cart, welcome…) | Prévu |
| `customer-service-bot` | Réponses SAV contextualisées sur données de commande | Prévu (0 commande à ce jour) |
| `performance-analyzer` | Rapports KPI multi-canal | Prévu |
| `q4-strategy-generator` | Stratégie BFCM/Noël | Prévu |
| `link-building-machine` | Prospection backlinks | Prévu |
| `webmaster-lfs` | **Hors périmètre** — projet « Looking For Soccer », sans lien avec le pipeline | N/A |

### 4.2 Packs communautaires skills.sh — installés le 26/07/2026 **[MÉMOIRE — skills-sh-ecommerce-installes.md + FAIT — dossiers présents]**

- **coreyhaines31/marketingskills** (13) : `cro`, `copywriting`, `marketing-psychology`, `customer-research`, `ab-testing`, `emails`, `offers`, `popups`, `competitor-profiling`, `analytics`, `pricing`, `ads`, `ad-creative`. `ads`+`ad-creative` remplacent en profondeur les skills maison ads, qui restent la couche règles Hakim : **les invoquer ensemble**.
- **higgsfield-ai/skills** (3) : `higgsfield-product-photoshoot` (visuels produit sans prompt freehand — réponse au problème des faux logos), `higgsfield-marketplace-cards`, `higgsfield-generate`.
- **nextlevelbuilder** : `ui-ux-pro-max` (base locale styles/palettes/fonts/guidelines). **leonxlnx** : `brandkit` (brand boards, phase DA). **shopify** : `shopify-liquid`.
- **vercel-labs/agent-skills** (~9, installés la veille) : dont `web-design-guidelines` (audits UI), `deploy-to-vercel` — périphériques au pipeline.
- Écarté : `nexscope-ai/ecommerce-skills` (frontmatter cassé) ; skills de recherche produit communautaires jugés inférieurs au pipeline maison.
- **Intégration au campement [MÉMOIRE + NOTION]** : les tickets 02, 03, 07, 08, 09, 10, 12b, 15, 16 listent leurs « skills à invoquer » (persona → customer-research/marketing-psychology ; charte → brandkit/ui-ux-pro-max ; prix → pricing mais **×1,3 reste la loi** ; images → higgsfield-* ; PDP/home → copywriting/cro/offers/shopify-liquid ; QA → web-design-guidelines).

### 4.3 Skills archivés — ne pas restaurer

`niche-scorer`, `competitor-analyzer`, `margin-calculator` (créés mars 2026) : critères périmés (filtre volume 1 000–50 000 au lieu du seuil 10 000 pertinent, « marge > 40 % » au lieu de marge contributive, micro-entreprise au lieu de SASU). Archivés le 17/07/2026 lors du passage au pipeline par agents. **Statut : abandonnés.** **[FAIT — repo:specs/2026-07-17-…-design.md §2 + dossier `~/.claude/skills-archive/` vérifié le 30/07]**

---

## 5. Campement type Notion — lancement de boutique

Base **Tickets — Lancement boutique (modèle)** (db `da8b39cc1a4248f2aec7494df5ef247b`, ds `139e0897-e0dd-4645-a1d6-681e54a919b2`), page parent « 🏕️ Campement type — Lancement boutique » dans le hub Pipeline Boutiques Drop. Vues : Kanban (par Statut) + Ordre d'exécution. **20 tickets vérifiés le 30/07/2026** **[NOTION]** — la fiche mémoire dit « 18 » (index) puis « 19 » (corps) : le ticket `12b` (panier) a été ajouté après coup **[CONTRADICTOIRE — mémoire vs Notion ; Notion fait foi, comptage direct]**.

Usage : à chaque « lance une boutique sur X », dupliquer la page campement, adapter l'en-tête (marque, domaine, e-mail, liens sourcing/références), créer `boutique-pipeline/boutique-<nom>/`, puis dérouler les tickets dans l'ordre. Chaque ticket = **brief d'agent autonome** avec procédure, garde-fous et critères de fin, distillés des lancements Tuftéo et Noirmont. **[MÉMOIRE — campement-type-lancement-boutique.md]**

| # | Ticket | Phase | Responsable |
|---|---|---|---|
| 00 | Kick-off — création boutique & fiche | 0 · Pré-lancement | Agent + validation Hakim |
| 00b | Arborescence produit — catalogue cible (liste fermée validée AVANT sourcing) | 1 · Recherche & assets | Agent + validation Hakim |
| 01 | Sourcing AliExpress détaillé (liens `/item/`) | 1 | Agent |
| 02 | Persona & objections (**BLOQUANT copywriting**) | 1 | Agent |
| 03 | Charte graphique + squelettes de pages | 1 | Agent + validation Hakim |
| 04 | Import DSers → Shopify (mapping intact) | 2 · Catalogue | Agent + validation Hakim |
| 05 | Canal Online Store + collections + menus | 2 | Agent |
| 06 | Francisation des variantes (méthode Tuftéo) | 2 | Agent + validation Hakim |
| 07 | Prix & prix barrés (règle **×1,3**) | 2 | Agent + validation Hakim |
| 08 | Images produit + visuels home (**anti-faux-logos**) | 3 · Design & contenu | Agent |
| 09 | Pages produit — structure Tuftéo + liquid custom | 3 | Agent |
| 10 | Homepage — structure Tuftéo | 3 | Agent + validation Hakim |
| 11 | Étoiles vert Trustpilot `#05b67a` | 3 | Agent |
| 12 | Avis clients — persona démo puis import Trustoo | 3 | Agent + validation Hakim |
| 12b | Panier — bannière + upsells (structure Tuftéo) | 3 | Agent |
| 13 | Paramétrer la livraison | 4 · Réglages | Agent + validation Hakim |
| 14 | Pages légales — dupliquer la référence (**Tuftéo**) et adapter | 4 | Agent |
| 15 | Réglages boutique (devise, marchés, e-mails, paiements) | 4 | Agent + validation Hakim |
| 16 | QA complète mobile-first | 5 · QA & clôture | Agent |
| 17 | Clôture — synchro Notion, runbook, mémoire | 5 | Agent |

Statuts de ticket : À faire / En cours / Bloqué Hakim / Fait. **[NOTION]**

---

## 6. Le pipeline complet, étape par étape

Légende d'exécution : **[AUTO]** automatisée (agent seul) · **[SEMI]** semi-automatisée (agent + reprises humaines) · **[MANUEL]** manuelle (Hakim) · **[GATE]** validation humaine obligatoire · **[CLAUDE]** dépendante de Claude Code aujourd'hui (skills/agents/MCP/mémoire) · **[CODEX-OK]** migrable vers Codex (déjà prouvé ou raisonnable) · **[NAV]** nécessite un navigateur avec sessions connectées de Hakim · **[API]** traitable par API.

Le déroulé s'appuie sur ce qui s'est **réellement passé** sur Noirmont (24-30/07) et Tuftéo (19-23/07), pas sur l'intention.

### A. Recherche produit (niveau 1 et 2 de validation)

| # | Étape | Comment ça s'est réellement passé | Marquage |
|---|---|---|---|
| A1 | Idéation — minage Brand Search | MCP `909b5b93` (quota 10 000/mois) + repli UI web ; idées adossées à des boutiques preuves ; Seiko mod et surpresseur en sont sortis le 20/07 **[FAIT — repo:reports/minage-brandsearch-2026-07-20.md]** | [AUTO] [CLAUDE] (MCP connecté côté Claude) [CODEX-OK si accès API/UI équivalent] |
| A2 | Mesure express volume | SEMrush Keyword Magic via Chrome connecté, base FR, chiffres lus à l'écran **[FAIT — repo:reports/mesure-express-vague1-brandsearch-2026-07-20.md]** | [AUTO] [NAV] [CLAUDE] [CODEX-OK — Codex l'a fait le 20/07 avec son propre navigateur, cf. §8] |
| A3 | Sonde prix | Google Shopping FR, 1 min, aucun site marchand visité | [AUTO] [NAV] [CODEX-OK] |
| A4 | Filtre qualitatif + thèse | Agent pur texte sur critères canoniques | [AUTO] [CODEX-OK] (aucun outil requis) |
| A5 | Demande réelle (SERP nettoyée) | SEMrush + SERP réelles, règle hiérarchique, verdicts | [AUTO] [NAV] [CLAUDE] [CODEX-OK] |
| A6 | Sourcing AliExpress | Fiches `/item/` ouvertes dans le Chrome de Hakim, relevés datés. Correction de doctrine du 25/07 : le CAPTCHA AliExpress est un **artefact de navigateur sans session** — avec le Chrome connecté de Hakim, aucune des passes des 25-30/07 n'a rencontré de CAPTCHA **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-bilan.md §Leçons]** | [AUTO] [NAV] — **[CODEX : bloqué le 20/07** — la politique de sécurité navigateur de l'environnement Codex a refusé AliExpress ; repli = requêtes de sourcing manuel **[FAIT — repo:codex-chasse-clusters/]]** |
| A7 | Critique à froid | Agent aveugle au compteur, verdict binaire | [AUTO] [CODEX-OK] |
| A8 | Écriture registre + synchro Notion | Registre local d'abord, Notion ensuite, au fil de l'eau | [AUTO] [API] (MCP Notion) [CODEX-OK] |
| A9 | Marge (phase 5) | Faite une seule fois (kit tufting, 19/07) **[FAIT — repo:reports/phase5-marge-kit-tufting-2026-07-19.md]** ; jamais par la boucle (volontaire) | [AUTO] [CODEX-OK] |
| A10 | **Choix des candidats à pousser, commande test** | Décision de Hakim, hors pipeline (ex. : Seiko mod poussé le 24/07 sur décision Hakim alors qu'il était « À APPROFONDIR ») **[FAIT — repo:registre-candidats.md]** | [MANUEL] [GATE] |

### B. Lancement boutique (campement 20 tickets — vécu sur Noirmont/Tuftéo)

| # | Étape | Comment ça s'est réellement passé | Marquage |
|---|---|---|---|
| B0 | Création du store Shopify, thème installé, connecteur | Pré-requis manuel de Hakim **[FAIT — repo:PLAYBOOK.md]** | [MANUEL] [GATE] |
| B1 | Arborescence produit / catalogue cible | Livrable md validé avant sourcing (`boutique-seiko-mod/journal/2026-07-24-arborescence-site.md`) | [SEMI] [GATE] [CODEX-OK] |
| B2 | Sourcing détaillé (liens `/item/`) | AliExpress via Chrome (phase4b/4c/4d Noirmont le 24/07) | [AUTO] [NAV] |
| B3 | Persona & objections | Bloquant avant tout copywriting (règle du 19/07) ; `personas/persona-noirmont-2026-07-25.md` **[FAIT]** | [AUTO] puis [GATE] (validation Hakim) [CODEX-OK] |
| B4 | Charte graphique | Propositions soumises à Hakim (Noirmont : directions A/B → « A+B » cyan) ; la DA est une **décision de marque, jamais autonome** **[MÉMOIRE — da-creative-pas-premium-fade.md]** | [SEMI] [GATE] |
| B5 | Import produits **par DSers** | Session DSers dans Chrome (`contact.noirmont`), mapping vérifié à la main — **il n'existe pas d'auto-matching DSers** ; 98 produits mappés, 0 Unmapped **[FAIT — repo:boutique-seiko-mod/dsers-mapping-*.md, boutique-seiko-mod/journal/2026-08-08-reprise-session.md]** | [SEMI] [NAV] — non traitable par API |
| B6 | Canal Online Store + collections + menus | API GraphQL : `publishablePublish` en batch (les produits DSers/API sont ACTIVE mais publiés sur **aucun** canal) ; menus Shopify partagés entre thèmes → créer un menu neuf **[MÉMOIRE + FAIT — repo:boutique-seiko-mod/journal/2026-08-08-reprise-session.md §Pièges]** | [AUTO] [API] [CODEX-OK] |
| B7 | Francisation variantes, découpage catalogue | API (bulk) ; Noirmont : découpage 1 fiche = 1 coloris (lots 1-2, 25/07) avec mise à jour du mapping DSers ensuite | [AUTO] [API] [CODEX-OK] |
| B8 | Prix, prix barrés | Règle ×1,3, `compareAt` sur toutes les variantes ; validation Hakim | [AUTO] [API] [GATE] |
| B9 | Images produit / galeries | Génération Higgsfield (`nano_banana_pro`, comparatif de 5 modèles le 25/07 ; `soul_2`/UGC et `openai_hazel` proscrits) en image-to-image depuis une face validée, contrôle de **stérilité au zoom** image par image, scripts locaux de manifest/QA/staged upload (`build-visual-manifest.mjs` → `upload-staged-visuals.mjs` → `productCreateMedia`) ; le gros lot de galeries (230 générations) a été **exécuté par Codex en local sur le Mac** avec **GPT Image 2 natif** (prompts `boutique-seiko-mod/journal/2026-07-31-prompt-codex-galeries.md`, scripts `prepare-gallery-*.mjs/.py`), puis branché côté Claude : **85 fiches, 206 médias** — rapprochement par **SKU, jamais par ID de variante** (les IDs du manifeste Codex étaient périmés) **[FAIT — repo:boutique-seiko-mod/]** | [SEMI] [CLAUDE en partie] [CODEX-OK — déjà pratiqué] [API pour l'upload] |
| B10 | PDP / homepage / panier (thème) | `themeFilesUpsert` sur **thème brouillon uniquement** (le connecteur refuse un thème MAIN) ; piège : `upsertedThemeFiles: []` sans `userErrors` = écriture **asynchrone**, pas un échec ; vérifier par checksum **[FAIT — repo:boutique-seiko-mod/journal/2026-08-08-reprise-session.md]** | [AUTO] [API] [CODEX-OK] |
| B11 | Contenu / SEO | Titres produits = actif de marque (naming), mots-clés portés par `seo.title` ; article SEO pilier (`boutique-seiko-mod/journal/2026-07-31-article-mod-ou-hommage.md`) ; metachamps **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-plan-nommage-seo.md, boutique-seiko-mod/journal/2026-07-31-seo-titles-produits.md]** | [AUTO] [API] [CODEX-OK] |
| B12 | Étoiles avis `#05b67a` + avis | Avis persona démo puis import réel Trustoo par bookmarklet piloté en Chrome (postMessage + React setters — recette dans la mémoire) ; **la preuve sociale reste la chasse gardée de Hakim** (placeholders démo jamais écrasés, faux compteurs à retirer par lui) **[MÉMOIRE — import-avis-trustoo-bookmark.md, mobile-first-et-placeholders-demo.md]** | [SEMI] [NAV] [GATE] |
| B13 | Livraison, réglages boutique | API (`deliveryProfileUpdate`) + réglages manuels admin (e-mails, paiements) | [SEMI] [API] [GATE] |
| B14 | Pages légales | Duplication de la référence Tuftéo + adaptation ; **médiateur de la consommation = adhésion par site, jamais recopiée** — reste à Hakim **[FAIT — repo:boutique-seiko-mod/journal/2026-08-08-reprise-session.md]** | [SEMI] [MANUEL pour le médiateur] |
| B15 | QA mobile-first | Navigateur intégré 375×812, contrastes mesurés sur rendu ; ⚠️ sur Noirmont « le rendu mobile n'a jamais été vu par un agent — seules des mesures existent » **[FAIT — repo:boutique-seiko-mod/journal/2026-08-08-reprise-session.md]** | [SEMI] [NAV] |
| B16 | Publication du thème / levée du mot de passe | **Réservé à Hakim** (republier « Maison Noirmont » `204248088914`, supprimer le fork obsolète) | [MANUEL] [GATE] |
| B17 | Clôture — synchro Notion, runbook, mémoire | Fiches Notion, `boutique-seiko-mod/journal/2026-08-08-reprise-session.md`, fiches mémoire | [AUTO] [API] [CLAUDE — la mémoire persistante est un mécanisme Claude Code] |

### C. Post-lancement (jamais atteint à ce jour)

Campagnes Google Ads/GMC, emails, SAV, rapports : couverts par les skills §4. **Tuftéo est publiée depuis le 23/07**, mais son statut Notion « Ads lancées » reste [CONTRADICTOIRE] avec le dépôt (plan de test vide) ; Noirmont reste sous mot de passe. Aucune campagne du pipeline n'est donc documentée comme active dans les fichiers locaux au 30/07. [FAIT — repo:boutique-tufting/project-state.md §23/07 + HTTP public 30/07 ; repo:boutique-seiko-mod/journal/2026-08-08-reprise-session.md]

### Synthèse des dépendances à Claude Code

Ce qui est structurellement lié à Claude Code aujourd'hui : les 3 skills + 9 agents (format SKILL.md/agents Claude), la mémoire persistante, les MCP branchés côté Claude (Shopify, Notion, Brand Search, Higgsfield, claude-in-chrome). Ce qui est déjà **agnostique** : tous les référentiels md (critères, playbooks, registre, rapports), les scripts Python/Node, le campement Notion (briefs en langage naturel), l'API Shopify GraphQL. La logique des agents est du **texte pur** : portable vers Codex à condition de rebrancher les 4 accès (SEMrush/AliExpress via navigateur, Shopify API, Notion API, Brand Search).

---

## 7. Mémoire persistante (14 fiches)

**[FAIT — repo:~/.claude/projects/-Users-Hakim-Documents-Boutiques-drop/memory/]** — index `MEMORY.md`. C'est la couche qui rend les sessions Claude cohérentes entre elles ; Codex devra la remplacer (ces fiches sont reprises dans `05-DECISION-LOG.md`). Fiches : pipeline agents, boucle volume-first, explicable-particulier, Brand Search, Notion pipeline, campement type, persona obligatoire, mobile-first/placeholders, DA créative, promesses vérifiables, import Trustoo, skills installés, canal Online Store & visuels IA.

---

## 8. Espace Codex existant — le précédent qui compte

**[FAIT — repo:codex-chasse-clusters/ + ~/.codex/skills/chasse-clusters-codex/]**

- Adaptation Codex de la boucle volume-first, **volontairement isolée** du dispositif Claude (lecture seule des canoniques, écritures dans son propre espace, empreintes SHA256 d'intégrité — une modification concurrente par Claude a été détectée et documentée le 20/07 sans écrasement).
- Run 1 `20260720-124517` : **40/40 familles épuisées, 110 clusters, 17 thématiques `RETENU_MARCHE_A_SOURCER`** — seuils non abaissés pour atteindre 20. **AliExpress techniquement bloqué pour Codex** (« Browser Use rejected this action ») → statut dédié « marché validé, à sourcer manuellement », requêtes AliExpress FR/EN livrées.
- Run 2 `20260720-200609` : mode Brand Search multi-marchés, 8 candidats verts + radar 30.
- Un sourcing d'existence des 8 candidats Codex a ensuite été fait **côté Claude** (`reports/sourcing-existence-codex-8-2026-07-20.md`) **[FAIT — repo]** : le duo « Codex mesure / Claude source » a déjà fonctionné.
- **Deuxième précédent — les galeries Noirmont (26/07)** : Codex a tourné **en local sur le Mac** (preuves : conversion via `sips` macOS, User-Agent `Codex-Noirmont/1.0`), avec GPT Image 2 natif, sur un contrat écrit (`boutique-seiko-mod/journal/2026-07-31-audit-visuel-catalogue.md` = « feuille de route de Codex ») et une interdiction absolue de toucher à Shopify — le branchement est resté côté Claude. Résultat : 85 fiches / 206 médias. Défauts relevés au contrôle : planches QA trop grossières (380 px, refaites à 740 px), 15 images avec inscriptions **sur le décor** (trou du prompt), un manifeste indexé sur des IDs de variante périmés (correspondances refaites par SKU), une exclusion non respectée **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-branchement-galeries-codex.md]**. Leçon : contrat de sortie indexé sur les **SKU/handles**, QA côté superviseur.
- Skills Codex présents : `~/.codex/skills/{chasse-clusters-codex, chronicle, codex-primary-runtime, front-end-design}` **[FAIT — dossier vérifié]** (contenu non audité ici : [MANQUANT]).

Enseignements pour la migration : (1) la logique fail-closed se transpose telle quelle ; (2) le point dur est l'accès navigateur à AliExpress ; (3) l'isolation par espace de travail + empreintes est le bon modèle de cohabitation.

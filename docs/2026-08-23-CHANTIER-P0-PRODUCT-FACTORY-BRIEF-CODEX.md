# Chantier de consolidation Product Factory — brief pour Codex

Date : 2026-08-23
Décideur : Hakim. Rédaction : Fable 5 (Claude), après revue critique croisée Fable 5 + ChatGPT Pro.
Dépôt cible du code : `HakimOuah/aliexpress-mcp-server` (références de lignes = `origin/main`, commit `3339d50`, post-PR #41).

## Contexte en trois phrases

Deux revues indépendantes (Fable 5 et ChatGPT Pro, 23/08/2026) ont audité la Product Factory et convergent : l'architecture et l'ordre du workflow sont bons, mais les portes protègent la forme des données, pas leur provenance, et la porte la plus structurante (`PASS_PREQUALIFICATION`) n'existe pas dans le code. Hakim a tranché les questions ouvertes (section suivante). **Priorité : durcir les frontières existantes avant toute nouvelle fonctionnalité aval** — le seul développement fonctionnel autorisé dans ce chantier est le pipeline UNIVERS (chantier B), après le chantier A.

## Décisions de Hakim (23/08/2026) — à respecter, ne pas re-débattre

| # | Décision |
|---|---|
| 1 | `PASS_PREQUALIFICATION` = conformité technique (volume + critères) → **émis par l'agent**. `REVIEW` et cas limites remontent à Hakim. La seule porte humaine de sélection produit est `GO_FINAL`. |
| 2 | **SEMrush France reste la loi** pour la mesure de volume. DataForSEO = repli documenté et signalé si SEMrush indisponible, et filtre d'expansion peu coûteux en amont — jamais une source de gate. |
| 3 | **Le registre GitHub** (`boutique-pipeline/registre-candidats.md`) est le système de référence des candidats. Le state store MCP doit référencer l'entrée de registre. |
| 4 | Cible opérationnelle : **bots Grok connectés au MCP**. Conséquence : la séparation des surfaces/permissions MCP est un préalable absolu. |
| 5 | **Commande test = Hakim**, immédiatement après `GO_FINAL`. Build en parallèle sur les étapes réversibles ; checkpoint `SAMPLE_OK` **bloquant avant GMC/Ads**. `WATCH_FINAL` n'autorise rien. |
| 6 | **UNIVERS : option B** — construire le pipeline complet (chantier B ci-dessous), après le chantier A. Règle transitoire : aucun `GO_FINAL` sur un dossier UNIVERS sans consolidation par familles documentée. |
| 7 | **Renommage** : recommandations techniques = `TECHNICAL_PASS` / `TECHNICAL_WATCH` / `TECHNICAL_FAIL` / `TECHNICAL_INCONCLUSIVE`. Le mot `GO` est réservé à `GO_FINAL` (Hakim). |
| 8 | **Plancher de sourçabilité UNIVERS** : les 3–5 familles pesant ≥ 70 % du volume consolidé doivent avoir chacune ≥ 2 fournisseurs plausibles avant décision finale. |
| 9 | **Recherche continue** (veille de marché permanente) → anti-doublon systématique et coût API plafonné par candidat deviennent critiques. |
| 10 | **Autonomie bots** : cliquer un CAPTCHA affiché, accepter CGU/cookies = autorisé. Anti-détection, proxys, contournement technique = interdits. (Ne change rien à la doctrine API-first du MCP.) |

## Déjà fait côté `boutiques-drop` / `boutique-pipeline` (commits Claude du 23/08)

- `PRODUCT-RESEARCH-CRITERIA.md` : §0 « Décisions du 23/08 » + chaîne §7 amendée (TECHNICAL_*, commande test, SAMPLE_OK) + DataForSEO ajouté aux replis.
- `GROK-BOT-FLEET.md` : veille continue (§5), CAPTCHA/CGU permissifs unifiés (§6), bot CONCURRENCE réécrit (marché préqualifié ≠ validé, matrice de défendabilité en sortie), bot SOURCING réorienté MCP-d'abord + revue visuelle SKU, DESIGN/GMC marqués hors flotte cloud.
- `.claude/skills/recherche-produit/SKILL.md` : défaut UNIVERS silencieux supprimé.
- `.claude/agents/phase5-marge.md` : vocabulaire `TECHNICAL_*` canonique.

---

# Chantier A — Durcissement des portes (P0, dans cet ordre)

## A1. Porte de préqualification dans le code

Constat : `PASS_PREQUALIFICATION` est documenté partout mais n'existe nulle part dans `src/`. `PIPELINE_STAGES` (`src/opportunity_state.py` l.19-34) n'a pas de stage de préqualification ; `analyze_product_opportunity` (`src/product_factory_server.py` l.1125) est appelable sans aucun pass ; le champ `allowed_only_after_pass_prequalification: True` (`src/universe_discovery.py` l.246) est purement déclaratif — rien ne le lit.

À faire :
1. Ajouter le stage `PREQUALIFICATION` à `PIPELINE_STAGES`.
2. Nouveau tool `record_prequalification_decision(opportunity_id, decision_review)` sur le modèle de `record_final_product_decision` : statuts `PASS_PREQUALIFICATION` / `REVIEW_PREQUALIFICATION` / `STOP_PREQUALIFICATION` ; preuves exigées : volume net **avec source et date** (SEMrush canonique, repli signalé — décision 2), lecture SERP, forme Trends selon le mode, sonde prix, version des critères (`criteria_version`). Émetteur = agent (décision 1) : le champ d'auteur identifie l'agent émetteur, pas Hakim.
3. `analyze_product_opportunity` prend un paramètre `opportunity_id` et **refuse tout appel externe** (DataForSEO comme AliExpress) si l'état ne porte pas un `PREQUALIFICATION/PASS_PREQUALIFICATION` persisté. Zéro appel avant le contrôle.
4. `REVIEW_PREQUALIFICATION` ne continue jamais automatiquement : il attend un override humain documenté persisté.

## A2. Fermeture des contournements de provenance

Constat : `persist_opportunity_state` (l.101-123 du serveur) accepte n'importe quels `stage/status/packet` — un état `DECISION/GO_FINAL` complet peut être fabriqué sans passer par `record_final_product_decision` (le test `tests/test_offer_strategy.py` l.148-157 le démontre). `owner_confirmed: true` est une chaîne fournie par l'appelant (`src/final_product_decision.py` l.66-68). Repli dangereux : `technical.get(...) or state.get("status")` (l.48-53) — un statut persisté « GO » satisfait l'exigence de verdict technique sans packet d'analyse.

À faire :
1. `persist_opportunity_state` **refuse** les écritures sur stage `DECISION` et les statuts `*_FINAL` (et sur `PREQUALIFICATION`) : ces transitions passent par leurs tools dédiés uniquement.
2. Supprimer le repli sur `state.get("status")` dans la résolution du verdict technique : exiger le packet d'analyse.
3. Séparer les surfaces MCP en deux au minimum (décision 4) :
   - **surface scout** (bots Grok) : lecture, discovery, analyse, sonde — aucun tool de persistance de transition, aucun tool Shopify ;
   - **surface contrôle** (Claude Code local / Codex) : transitions, `record_prequalification_decision`, `record_final_product_decision`, exécution Shopify draft.
   Implémentation pragmatique acceptée : deux endpoints/credentials distincts (pas besoin d'infrastructure de signature — décision explicite de ne pas surdimensionner). Le credential de la surface contrôle ne doit jamais exister sur la machine cloud Grok.
4. Adapter `tests/test_product_factory_tool_inventory.py` : vérifier l'inventaire **par surface**, pas seulement la présence globale.

## A3. Blocker économique au stade offre

Constat (repéré par ChatGPT Pro, confirmé dans le code) : `build_offer_packet` (`src/offer_strategy.py` l.162-174) recalcule l'économie au prix cible fourni, mais un `supplier_verdict: NO_GO` recalculé n'entre pas dans `blockers` (l.215-217) — l'offre peut être persistée `READY` et l'échec ne remonte qu'au launch readiness, après brand/média/Shopify/contenu/conformité/GMC/Ads.

À faire : si `exact_unit_economics.supplier_verdict != "GO"` après recalcul → blocker `OFFER_PRICE_BREAKS_APPROVED_ECONOMICS`, statut `OFFER_DRAFT_BLOCKED`. Toute modification ultérieure de prix/bundle/garantie/livraison déclenche une revalidation économique avant `OFFER:READY`.

## A4. Économie contributive dans le verdict technique

Constat : `src/candidate_economics.py` (l.24-28) calcule marge brute = (HT − coût rendu)/HT. La formule maison (bots, `phase5-marge`) exige : frais de paiement (~1,4 % + 0,25 €, à confirmer sur contrats), ratio **prix ÷ CPC ≥ 100** (cible 150–200 ; le CPC est déjà collecté par la discovery), CPA maximal supportable, provisions retours/SAV.

À faire : intégrer au minimum frais de paiement + ratio prix/CPC + CPA max dans le verdict technique. Les seuils vivent en config, pas en dur (au passage : sortir `min_product_cost_eur=25.0` et les 15/30 jours codés en dur dans l'appel serveur, l.1211-1213).

## A5. Renommage des verdicts techniques

`GO/WATCH/NO_GO` techniques → `TECHNICAL_PASS` / `TECHNICAL_WATCH` / `TECHNICAL_FAIL` / `TECHNICAL_INCONCLUSIVE` (décision 7), avec alias de compatibilité le temps de la migration. Au passage : le repli « verdict inconnu → WATCH » (`_resolve_requested_category_status`, l.1002) devient `TECHNICAL_INCONCLUSIVE` (fail-closed).

## A6. Concurrence structurée alimentant `DEFENSIBLE`

Constat : le gate `GO_FINAL` exige `competition_assessment == "DEFENSIBLE"` (`src/final_product_decision.py` l.71) — chaîne libre, aucune preuve exigée ; `market_analysis.py` produit `market_shape`, `organic_top3_share`, `recurring_paid_advertisers` (l.79-164) mais rien ne les consomme.

À faire : définir un packet concurrence structuré (densité de concurrents directs comparables, actifs défensifs, compression prix, qualité d'exécution, espace exécutable, conclusion DÉFENDABLE/CONDITIONNEL/NON DÉFENDABLE/INDÉTERMINÉ — le format est déjà écrit dans l'instruction du bot CONCURRENCE, `GROK-BOT-FLEET.md`). `record_final_product_decision` exige que `competition_assessment` référence un artefact de ce type persisté ; le texte libre du droit de gagner complète, ne remplace pas.

## A7. Checkpoint échantillon (décision 5)

Ajouter un stage `SAMPLE` entre `DECISION` et l'entrée GMC/Ads : `record_sample_check(opportunity_id, ...)` → `SAMPLE_OK` / `SAMPLE_FAIL` / `SAMPLE_WAIVED_BY_OWNER` (waiver daté et motivé, réservé aux produits à risque très faible). `build_gmc_readiness_packet` et `build_google_ads_launch_packet` exigent `SAMPLE_OK` ou waiver dans le lignage. Les étapes réversibles (offre, brand, média, Shopify draft) restent accessibles dès `GO_FINAL`.

## A8. Registre = référence (décision 3)

Champ `registre_ref` obligatoire à la création d'une opportunité dans le state store ; refuser la création sans référence. Le contrôle anti-doublon de fond reste côté orchestrateur/registre.

## A9. Fraîcheur des preuves

Chaque preuve dynamique (quote fret, stock, prix marché) porte `observed_at` ; `GO_FINAL` et le launch readiness rejettent une quote plus vieille qu'un TTL configurable (proposition de départ : fret/stock 7 jours, prix marché 14 jours — à valider par Hakim, ne pas inventer d'autres valeurs).

## A10. Mises en cohérence documentaires (dépôt aliexpress-mcp-server)

- `AGENTS.md` et `docs/CODEX_HANDOFF.md` : zéro occurrence de `GO_FINAL`/`PREQUALIFICATION` aujourd'hui ; le flux l.305 d'AGENTS.md dit encore `economics → GO → offer`. Mettre à jour avec la chaîne complète et le vocabulaire `TECHNICAL_*`.
- `docs/PRODUCT_RESEARCH_MODE_DESIGN.md` : « a written owner market decision » → pass émis par l'agent (décision 1), owner sur REVIEW seulement.
- Routage `NEXT_TOOLS` (`src/launch_readiness.py` l.8-19) : ajouter `SUPPLIER_VALIDATION:TECHNICAL_PASS → record_final_product_decision` ; corriger le message d'impasse du WATCH (il recommande un `GO_FINAL` que le gate refusera — proposer les vraies actions : compléter les preuves, résoudre la sku_review, `WATCH_FINAL`).

---

# Chantier B — Pipeline UNIVERS (option B, APRÈS le chantier A)

Constat : le mode UNIVERS est classifié puis abandonné — `analyze_product_opportunity` est mono-requête/mono-catégorie, `build_offer_packet` porte exactement un `product_id`/`sku_id`, `brand_concept.py` se déclare « mono-product store concept » (l.1, l.257), le launch readiness vérifie UN produit exact.

Contrat à implémenter (écrire un design doc court d'abord, selon la pratique du dépôt) :

```text
UNIVERSE_THESIS (seed + mode UNIVERS)
    ↓
FAMILY_MAP : familles distinctes qu'une même boutique servirait
    ↓
VOLUME_AND_OVERLAP : volume par famille (SEMrush canonique — décision 2),
    recoupements mesurés, volume consolidé net (plancher 30 000, confort 40 000)
    ↓
CORE_FAMILY_SELECTION : les 3–5 familles ≥ 70 % du volume consolidé
    ↓
PRICE_AND_BASKET_MODEL : sonde prix par famille cœur, panier moyen simulé,
    contribution par commande multi-lignes (règles catalogue-volume des critères §7)
    ↓
SOURCEABILITY_BY_FAMILY : ≥ 2 fournisseurs plausibles par famille cœur (décision 8),
    SKU exact + quote sur le représentant de chaque famille — pas les 100 produits
    ↓
UNIVERSE_COMPETITION : matrice de défendabilité au niveau boutique
    ↓
UNIVERSE_TECHNICAL_DECISION : TECHNICAL_PASS/WATCH/FAIL/INCONCLUSIVE au niveau univers
    ↓
GO_FINAL Hakim → aval multi-collections (offre par famille, boutique catalogue)
```

Règle transitoire immédiate (une ligne de code, à livrer avec le chantier A) : un état de mode UNIVERS sans consolidation par familles ne peut pas atteindre `DECISION` — statut maximal `UNIVERSE_MODEL_INCOMPLETE`.

---

# Tests à ajouter (extraits des deux revues, fusionnés)

1. État `DECISION/GO_FINAL` écrit via `persist_opportunity_state` → refusé, et n'ouvre jamais `build_offer_strategy`.
2. `analyze_product_opportunity` sans pass persisté → blocage, **zéro appel DataForSEO, zéro appel AliExpress**.
3. Prix d'offre dégradant l'économie → `OFFER_DRAFT_BLOCKED`, brand/média/Shopify inaccessibles.
4. Marge brute PASS mais économie contributive FAIL (CPA/CPC) → `TECHNICAL_FAIL`.
5. `competition_assessment=DEFENSIBLE` sans artefact concurrence → `GO_FINAL` bloqué.
6. Verdict inconnu → `TECHNICAL_INCONCLUSIVE` (pas WATCH).
7. Routage : `SUPPLIER_VALIDATION:TECHNICAL_PASS` → `record_final_product_decision`.
8. Quote fret/stock plus vieille que le TTL → décision bloquée ou refresh exigé.
9. Mode UNIVERS sans consolidation → jamais de `DECISION` (règle transitoire), puis tests du contrat B.
10. Inventaire des tools **par surface** (scout vs contrôle).
11. Transition illégale de stage (ex. DISCOVERY → ADS_READINESS) → rejetée.
12. Création d'opportunité sans `registre_ref` → refusée.
13. End-to-end avec les sorties réelles des builders successifs (pas un fixture qui reconstruit la lignée à la main).
14. Généralité classifieur sur corpus non-machine (textile/déco/rangement FR) — sortir les règles tufting vers un registre de familles au passage (P2 si le temps manque).

# Invariants non négociables (rappel)

- La catégorie demandée contrôle le verdict principal ; aucun accessoire rentable ne sauve un mauvais produit principal.
- Aucune marge fiable sans SKU numérique et fret exacts ; fail-closed sur l'ambigu.
- Aucun sourcing profond avant pass persisté ; aucun aval avant `GO_FINAL` persisté ; aucun `GO` prononcé par un bot.
- Aucune publication, commande, GMC ou dépense implicite ; draft-only et spend-zéro conservés.
- Pas de scraping navigateur pour remplacer une API disponible ; pas d'anti-détection (décision 10 : cliquer un CAPTCHA affiché est permis aux bots, le contournement technique reste interdit).

# Définition de fin de chantier

Chantier A terminé quand : les 14 familles de tests ci-dessus passent, un candidat de bout en bout (préqualification → diligence → `TECHNICAL_PASS` → `GO_FINAL` réel de Hakim) a traversé le système en conditions réelles, et le déploiement VPS est validé selon `docs/VPS_OPERATIONS.md`. Chantier B ensuite, design doc d'abord.

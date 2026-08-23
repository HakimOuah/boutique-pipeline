# Test de bout en bout Product Factory — 23/08/2026

Exécutant : Fable 5 (Claude Code), via SSH sur le VPS (`clé product_factory_codex_ed25519`), appels MCP sur la surface contrôle (`aliexpress-mcp`, `main` @ `9f39e3b`).
Candidat réel : **Tente gonflable (glamping)** — P15 / PUR-07 de la salve 30x30, entrée registre lot 2.
Opportunité persistée sur le VPS : `opp-ac535029c87f42c0b034d05d9f7e405f` (volume `product-factory-state`).
Coût API total : **0,024 $** DataForSEO (+ appels AliExpress officiels gratuits). Durée d'analyse : 101 s.

## Résultat global : LA MACHINE FONCTIONNE — toutes les portes ont tiré correctement en production

| # | Étape | Attendu | Constaté |
|---|---|---|---|
| 1 | Création opportunité | `registre_ref` obligatoire | ✅ créée avec ref registre persistée (rév. 1) |
| 2a | **Adverse** : `analyze` sans pass | Refus, zéro appel externe | ✅ `PREQUALIFICATION_REQUIRED`, `{dataforseo: 0, aliexpress: 0}` |
| 2b | **Adverse** : `GO_FINAL` forgé via persistance publique | Rejet | ✅ « DECISION/GO_FINAL must be written by its dedicated control tool » |
| 3 | Préqualification réelle (preuves SEMrush datées 22/08 : 12 100/mois, KD 22, CPC 0,15 $ ; Trends continue ; SERP commerciale ; sonde 67 prix socle 100-220 €) | PASS enregistré par l'agent | ✅ `PASS_PREQUALIFICATION`, stage `PREQUALIFICATION`, rév. 2 |
| 4 | Analyse profonde réelle (DataForSEO + AliExpress officiel) | Verdict honnête | ✅ `TECHNICAL_WATCH` — 281 offres uniques, 27 fournisseurs qualifiés, 1 en catégorie demandée |
| 5 | Persistance verdict + artefact concurrence structuré | Transition publique légale | ✅ `SUPPLIER_VALIDATION`/`TECHNICAL_WATCH` rév. 3 + artefact `competition-b19213aef9c5df9fc056` (conclusion honnête : `CONDITIONAL`) |
| 6 | **Adverse** : tentative `GO_FINAL` sur un WATCH | Blocage | ✅ `FINAL_DECISION_BLOCKED` : `TECHNICAL_RECOMMENDATION_MUST_BE_TECHNICAL_PASS` + `COMPETITION_AND_RIGHT_TO_WIN_MUST_BE_DEFENSIBLE` |
| 7 | Routage | Guidage utile | ✅ `HUMAN_DECISION_REQUIRED` avec actions proposées : compléter les preuves / résoudre la sku_review / `WATCH_FINAL` |

**Le point le plus important** : le meilleur fournisseur trouvé affichait une marge contributive de **87,2 %** (coût rendu 12,78 € vs référence marché 375 €) — et la machine a **refusé** d'en faire un pass, en le tenant en WATCH sur le signal `suspicious_low_product_cost`. C'est le comportement anti-faux-GO voulu, vérifié en conditions réelles.

## Verdict métier sur le candidat (honnête)

Tente gonflable reste **TECHNICAL_WATCH**, et c'est cohérent avec ce qu'on sait :

- le « fournisseur » à 12,78 € est en réalité une **chaise longue flottante de piscine** (hors sujet, voir bug n°1 ci-dessous) ;
- la vraie tente à air sourcée le 22/08 (Lohascamping, `1005007805462749`, 133,39 € rendu) laisse une marge fine face au cœur de bande Shopping 100-220 € ;
- la médiane SERP à 375 € est probablement gonflée par les grandes tentes événementielles (bug n°3).

Prochaines actions possibles (à toi) : `WATCH_FINAL`, ou approfondir (revue SKU visuelle + Mission B complète + repositionnement haut de gamme si défendable).

## Trois retours pour Codex (issus du test live)

1. **Bug de pertinence générique (prioritaire)** — sur la requête `inflatable camping tent`, le seul fournisseur retenu en catégorie PRODUCT est une chaise longue gonflable de piscine (`1005011600787889`). Le filtre `sourcing_relevance` laisse passer un hors-sujet complet sur un univers non-tufting : c'est exactement le défaut générique que la validation « deuxième univers » (P2) devait exposer. À corriger de façon générique (pas un mot-clé « tente » codé en dur). 24 fournisseurs sur 27 finissent « unpriced/noncomparable » et la vraie tente à air connue n'est pas retenue — la couverture de la catégorie demandée est trop faible.
2. **Timeout DataForSEO par défaut trop court** — `DATAFORSEO_TIMEOUT_SECONDS` vaut 30 s par défaut alors qu'une SERP live advanced à depth 50 prend 15-60 s+ : deux runs ont échoué en `DataForSEO network error:` (ReadTimeout vide) avant correction. Corrigé opérationnellement sur le VPS (`.env` → `120`). À faire : relever le défaut dans `config.py` et documenter dans `.env.example`.
3. **Divergence médiane SERP vs sonde Shopping** — bucket PRODUCT à 375-384 € (193 offres) contre un socle Google Shopping direct à 100-220 € : des compositions non comparables (tentes événementielles/familiales XXL) se mélangent au cœur de gamme. C'est la limite connue 19.8 (comparaison sensible à la composition) qui mord sur ce nouvel univers — la sonde prix canonique doit rester l'arbitre du prix cible tant que ce n'est pas raffiné.

## État persistant

- Opportunité `opp-ac535029c87f42c0b034d05d9f7e405f` : `SUPPLIER_VALIDATION` / `TECHNICAL_WATCH`, rév. 4 (artefact concurrence inclus), sur le volume VPS.
- `.env` VPS : ajout `DATAFORSEO_TIMEOUT_SECONDS=120` (conteneurs recréés, les deux healthy).
- Aucun `GO_FINAL` enregistré (la tentative adverse a été bloquée, rien persisté). Aucune mutation Shopify/GMC/Ads. Aucune dépense hors 0,024 $ DataForSEO.

## Addendum — correctifs livrés et re-validation live (23/08, après-midi)

Les 3 retours ont été corrigés par Fable 5 (pas Codex) dans la [PR #45](https://github.com/HakimOuah/aliexpress-mcp-server/pull/45), mergée et déployée sur le VPS (`main` @ `9afa920`, 416 tests exécutés et passés) :

1. **Pertinence** : les modificateurs d'attribut (`gonflable`, `portable`, `électrique`…) ne qualifient plus un titre à eux seuls — un token substantif du produit est exigé (régression testée sur le cas réel de la chaise piscine).
2. **Timeout DataForSEO** : défaut 30 s → 120 s dans le code (`config.py` + `.env.example`).
3. **Contrôle croisé sonde prix** : `analyze_product_opportunity` retourne `price_probe_cross_check` (médiane SERP vs sonde Shopping persistée). La sonde canonique reste l'arbitre.

**Re-validation live sur le même candidat** (préqualification ré-enregistrée rév. 5, nouvelle analyse 0,016 $) :

- la chaise piscine a **disparu** (0 fournisseur en catégorie demandée, 20 accessoires camping correctement `NOT_COMPARABLE`) ;
- verdict corrigé : **`TECHNICAL_FAIL`** (aucun fournisseur PRODUCT qualifié) — persisté rév. 6 ;
- le contrôle croisé tire : `ABOVE_PROBED_BAND` (386,50 € SERP vs socle sondé 100-220 €), avec la consigne de revoir la composition du bucket avant de croire la médiane SERP.

Note de recall pour plus tard : `ds.text.search` ne remonte que des accessoires camping sur cette requête ; le repli découverte Google ne se déclenche que si zéro item pertinent. Si le candidat est repris un jour, prévoir un repli déclenchable quand la catégorie demandée reste vide (pas seulement quand tout est vide).

## Exposition de la surface scout (pour les bots Grok)

- **URL publique** : `https://srv1575867.hstgr.cloud/mcp` (TLS Let's Encrypt via Traefik, override compose local au VPS — jamais versionné).
- Auth Bearer par `SCOUT_MCP_TOKEN` : 401 vérifié sans token et avec mauvais token ; handshake MCP validé depuis l'extérieur (serveur : `product-factory-scout`).
- Seule la surface scout est exposée ; la surface contrôle reste sur `127.0.0.1` et son token ne quitte pas le local.

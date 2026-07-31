# Design — Pipeline de recherche produit par sous-agents (phases 1 à 5)

Date : 17 juillet 2026
Statut : validé par Hakim section par section (conversation du 17 juillet 2026)
Portée : phases 1 à 5 du pipeline de recherche produit (idéation → marge). Hors périmètre : commande test, construction boutique, Google Ads, tout ce qui suit le niveau 2 de validation.

## 1. Problème à résoudre

Les recherches produit passées ont montré trois défauts récurrents :

1. **Critères non respectés ou périmés.** Les skills historiques (`niche-scorer`, `competitor-analyzer`, `margin-calculator`, créés en mars 2026) contiennent des critères figés qui ont divergé des critères actuels (ex. filtre volume 1 000–50 000 au lieu du seuil de 10 000 recherches pertinentes ; « marge > 40 % » au lieu du calcul de marge contributive ; micro-entreprise vs SASU au lieu de SASU/OH Ventures). Ils se déclenchent sur des mots comme « niche » ou « marge » et appliquent les mauvaises règles.
2. **Mélange entre phases.** Verdicts marché contaminés par le sourcing, statuts fournisseur transformés en validation, volume brut confondu avec volume pertinent.
3. **Perte de mémoire entre recherches.** L'anti-doublon reposait sur la relecture manuelle d'anciens rapports ; des produits déjà étudiés pouvaient être re-proposés ou des réserves perdues.

## 2. Décisions actées

| Question | Décision de Hakim |
|---|---|
| Forme | **Sous-agents dédiés**, un par phase |
| Anciens skills en conflit | **Archivés** (déplacés hors de `~/.claude/skills/`), remplacés par les agents |
| Circulation des données | **Rapports datés + registre central** des candidats |
| Enchaînement | **Automatique avec arrêt sur échec** (fail-closed) |
| Architecture retenue | **Approche A** : un orchestrateur + 5 sous-agents |

## 3. Architecture des fichiers

```
Boutiques drop/
├── .claude/
│   ├── skills/
│   │   └── recherche-produit/
│   │       └── SKILL.md                  ← orchestrateur, invocable via /recherche-produit
│   └── agents/
│       ├── phase1-ideation.md
│       ├── phase2-filtre.md
│       ├── phase3-demande.md
│       ├── phase4-sourcing.md
│       └── phase5-marge.md
└── boutique-pipeline/
    ├── PRODUCT-RESEARCH-CRITERIA.md      ← source de vérité des critères (existant, inchangé)
    ├── PRODUCT-RESEARCH-PLAYBOOK.md      ← méthode détaillée (existant, inchangé)
    ├── registre-candidats.md             ← NOUVEAU : registre central
    ├── specs/                            ← ce document
    └── reports/                          ← rapports datés produits par les agents
```

**Principe fondamental — critères centralisés.** Aucun critère chiffré (seuil de volume, fourchette de prix, seuils vendeur, etc.) n'est copié dans les agents. Chaque agent a l'obligation, en début de mission, de lire `PRODUCT-RESEARCH-CRITERIA.md` et la ou les sections du `PRODUCT-RESEARCH-PLAYBOOK.md` qui concernent sa phase. Un changement de critère se fait à un seul endroit et s'applique immédiatement aux cinq agents. Les agents contiennent uniquement : leur périmètre, leur procédure, leur format de sortie et leurs interdits.

## 4. Registre central des candidats

Fichier : `boutique-pipeline/registre-candidats.md`.

Une ligne par produit jamais étudié, avec au minimum :

- nom canonique du candidat ;
- synonymes et variantes (singulier/pluriel, français/anglais, formulations proches) pour l'anti-doublon ;
- date de première étude et date du dernier contrôle ;
- phase atteinte (1 à 5) et niveau de validation atteint (marché / fiche AliExpress / commande test / lancement) ;
- verdict actuel (GO marché, À APPROFONDIR, STOP, rejet immédiat, etc.) ;
- lien vers le rapport qui fait foi.

**Initialisation.** Le registre est semé avec tout l'historique connu :

- les 13 candidats V2 et leurs verdicts (source de vérité : `reports/validation-semrush-2026-07-17.md`) ;
- les 10 niches V1 (microscope, OBD2, station météo, canalisation, radon, thermique, vinyles, scanner films, sous vide, détecteur de métaux) et leurs conclusions (`reports/recherche-aliexpress-2026-07-16.md`) ;
- les rejets immédiats documentés (`reports/recherche-produits-v2-2026-07-16.md`) ;
- les tests antérieurs non concluants : machine à café portable, Pilates Reformer.

**Règles d'usage.**

- Chaque agent lit le registre **avant** de travailler. Un produit déjà en STOP ou rejeté ne peut pas être re-proposé, sauf thèse réellement nouvelle documentée, marquée explicitement `déjà recherché — reprise motivée`.
- L'orchestrateur met le registre à jour **après chaque phase** (pas seulement en fin de chaîne), afin qu'une interruption ne perde rien.
- Le registre ne remplace pas les rapports : il pointe vers eux. Les réserves et le détail restent dans les rapports datés.

## 5. Squelette commun des cinq agents

Chaque fichier d'agent suit la même structure :

1. **Lectures obligatoires au démarrage** : `PRODUCT-RESEARCH-CRITERIA.md`, section(s) du playbook concernée(s), `registre-candidats.md`, livrable de la phase précédente.
2. **Périmètre** : ce que la phase fait, et uniquement cela.
3. **Procédure** : étapes dans l'ordre, avec les points de vigilance connus.
4. **Format de sortie** : rapport daté dans `reports/`, sections obligatoires listées, conventions de nommage `"<phase>-<sujet>-YYYY-MM-DD.md"`.
5. **Interdits** : liste explicite (voir §6). Tout interdit enfreint = livrable non conforme = arrêt de la chaîne.
6. **Règles de preuve** : dater chaque contrôle ; distinguer prouvé / annoncé par le vendeur / déduit / à confirmer / non vérifié ; préférer l'omission à une affirmation fragile ; toute estimation présentée comme une estimation.
7. **Règles de conduite** : aucun contact vendeur, aucun achat, aucune connexion à un compte, aucune modification Shopify / Google Ads / Merchant Center.

## 6. Spécification des cinq agents

### Phase 1 — Idéation (`phase1-ideation`)

- **Entrée** : brief de mission (niche imposée par Hakim ou exploration libre), registre.
- **Fait** : collecte 20 à 50 idées brutes sur les sources autorisées (Amazon, VEVOR, Flippa, DotMarket, Europages, Google Search/Shopping, Ads Transparency Center, Pinterest, Reddit/forums/avis). Applique dès la collecte les filtres d'exclusion amont (produits rincés, banalité grande distribution, hors gamme de prix) — on ne note pas tout ce qu'on rencontre.
- **Livre** : rapport d'idéation — pour chaque idée : produit, source exacte, problème ou désir, prix publics observés, première hypothèse d'angle.
- **Interdits** : scoring, volumes SEMrush, sourcing AliExpress, verdicts. Une vérification rapide de plausibilité prix (le produit existe-t-il dans la gamme 150–400 €) est permise via les sources publiques, sans fiche fournisseur.
- **Gate de sortie** : au moins une idée nouvelle non présente au registre ; sinon arrêt avec rapport « aucune idée nouvelle ».

### Phase 2 — Filtre et thèse (`phase2-filtre`)

- **Entrée** : rapport de phase 1, registre.
- **Fait** : applique les critères de différenciation, banalité, scalabilité, faisabilité pressentie et anti-doublon (avec logique de synonymes). Écrit pour chaque survivant une **thèse produit en une phrase** (persona + problème/désir + angle + différence vs concurrents).
- **Livre** : shortlist avec thèse par candidat + **rejets documentés avec motif** (aucun rejet silencieux).
- **Interdits** : chiffres de volume (même « de mémoire »), verdicts marché, sourcing.
- **Gate de sortie** : shortlist non vide ; un candidat sans thèse défendable ne passe pas.

### Phase 3 — Validation de la demande (`phase3-demande`)

- **Entrée** : shortlist de phase 2, registre.
- **Fait** : pour chaque candidat, SEMrush **base France** (Keyword Magic Tool, Keyword Overview) + Google Search et Shopping réels. Construit le cluster adressable : volume brut → exclusions (marques, enseignes, services, location, occasion, SAV, pièces, géographique, informationnel hors achat, low-ticket incompatible, technologies différentes, doublons sémantiques) → volume pertinent estimé. Contrôle SERP : intention, annonces, prix observés, types de concurrents (spécialistes vs grandes enseignes), saisonnalité.
- **Règle d'exploration hiérarchique du cluster (nouvelle — cas « suspension rotin XXL »)** :
  1. Ne jamais mesurer une seule formulation. Pour chaque candidat, tester **plusieurs niveaux de généralité** : la formulation spécifique du produit → la famille de produit → la catégorie parente (ex. `suspension rotin xxl` → `suspension rotin` → `suspension`/`luminaire rotin`).
  2. **Si la formulation spécifique est sous le seuil, il est interdit de conclure STOP sans avoir mesuré le niveau parent** et évalué quelle part de ce volume parent est réellement adressable par le produit. Le test d'adressabilité passe par la SERP réelle du parent : montre-t-elle ce type de produit ? l'intention est-elle compatible ? une boutique spécialisée peut-elle capter cette requête ?
  3. Symétriquement, **ne jamais attribuer tout le volume du parent au produit spécifique** sans justification SERP (contre-exemple documenté : `bateau amorceur` 5 400 attribué à tort au segment GPS/sondeur). Les deux erreurs — conclure trop vite sur la longue traîne, et gonfler avec le générique — sont interdites.
  4. Le rapport documente les niveaux testés, le niveau retenu comme cluster adressable et la justification du choix. Exemple positif de référence : `tufting` (8 100, générique) retenu car sa SERP affiche directement kits et machines.
- **Livre** : rapport de validation — par candidat : volume brut, volume pertinent estimé, hypothèses de déduplication, mots-clés retenus et exclus, niveaux de généralité testés, CPC, saisonnalité, concurrence publicitaire, prix SERP, concurrents, verdict **GO marché / À APPROFONDIR / STOP**.
- **Interdits** : base autre que France ; confondre « Shopping sponsorisé visible » et « annonces Search texte confirmées » ; sourcing AliExpress ; inventer des variations chiffrées de tendance non exposées par l'outil.
- **Gate de sortie** : au moins un GO marché → la chaîne continue avec ces candidats uniquement. Zéro GO → arrêt avec rapport. Cas limite (volume proche du seuil, données incomplètes, outil inaccessible) → arrêt et remontée à Hakim, l'agent ne tranche pas seul.

### Phase 4 — Sourcing AliExpress (`phase4-sourcing`)

- **Entrée** : candidats **GO marché uniquement** (jamais les STOP, jamais les À APPROFONDIR sans instruction explicite), registre.
- **Fait** : recherche de fiches sur AliExpress exclusivement (ni BigBuy, ni Amazon, ni VEVOR, ni Alibaba). Pour chaque fiche : URL exacte `/item/...html`, variante exacte et **prix de cette variante** (pas la variante d'appel), livraison vers adresse française, pays d'expédition (priorité France/UE), délai (idéalement < 10 jours, de préférence < 15), frais et coût rendu, stock, ventes, note produit, nombre d'avis, notation vendeur, ancienneté si disponible, prise/tension, protection acheteur, signaux de risque. Chaque relevé est daté.
- **Livre** : rapport de sourcing — fiches complètes, alternatives contrôlées, rejets motivés, et par candidat un statut parmi : `aucune offre exploitable` / `offre trouvée` / `fournisseur à tester` / `fournisseur retenu pour commande test`.
- **Interdits** : le statut `GO fournisseur` n'existe pas à ce stade (il exige une commande test) ; un bon fournisseur ne renverse jamais un verdict marché ; aucun contact vendeur, aucun panier, aucune commande ; jamais de page de résultats comme référence ; un vendeur < 95 % d'avis positifs ne peut pas être « validé », seulement « à tester avec justification ».
- **Gate de sortie** : au moins un `fournisseur à tester` ou mieux → phase 5. Sinon arrêt avec rapport.

### Phase 5 — Marge et faisabilité (`phase5-marge`)

- **Entrée** : fiches retenues en phase 4, prix de vente cible issu des prix SERP de la phase 3.
- **Fait** : calcule à partir du coût rendu daté : TVA, frais de paiement, provision retours/remboursements, provision SAV, coûts applicatifs, coût publicitaire attendu → **marge contributive**, **CPA maximal supportable**, **CAC break-even**, budget test indicatif. Vérifie poids, dimensions, casse, emballage, pièces, consommables, responsabilité produit. Raisonnement SASU/OH Ventures (TVA au réel, IS).
- **Livre** : rapport de marge par candidat + **conditions de GO** explicites (ce qui doit encore être vérifié par commande test) + synthèse de fin de chaîne.
- **Interdits** : présenter un écart prix fournisseur/prix de vente comme une marge nette ; prononcer un GO lancement ; considérer une caractéristique vendeur comme vérifiée.
- **Sortie de chaîne** : recommandation de commande test (ou non). **La décision de commander reste celle de Hakim.**

## 7. L'orchestrateur `/recherche-produit`

Skill projet dans `.claude/skills/recherche-produit/SKILL.md`.

**Séquence** : lire le registre → phase 1 → contrôle du livrable → mise à jour du registre → phase 2 → … → phase 5 → synthèse finale.

**Contrôle de livrable après chaque phase** : le rapport existe, il est daté du jour, les sections obligatoires sont présentes, les interdits n'ont pas été enfreints (ex. un verdict marché dans un rapport de phase 2 = non conforme), la gate de sortie est franchie.

**Règle fail-closed** — la chaîne s'arrête d'elle-même et remonte un rapport d'arrêt dans trois cas :

1. verdict négatif : plus aucun candidat en course ;
2. cas limite : volume pertinent à ±20 % du seuil (soit entre 8 000 et 12 000 pour un seuil à 10 000 — le cas du tour de potier à 8 400 aurait déclenché cet arrêt), vendeur entre 90 et 95 %, donnée contradictoire — l'agent ne tranche jamais seul un cas limite ;
3. donnée invérifiable : SEMrush inaccessible, CAPTCHA AliExpress, page introuvable — on n'invente jamais de données pour continuer.

**Rapport final** (fin normale ou arrêt) : ce qui a été fait phase par phase, fichiers créés/modifiés, état du registre, candidats survivants avec réserves, recommandation, et ce qui reste à décider par Hakim.

**Restrictions globales portées par l'orchestrateur** : aucun contact vendeur, aucune commande, aucune modification Shopify / Google Ads / Merchant Center, aucune publication. Les quatre niveaux de validation (marché → fiche → commande test → lancement) sont rappelés dans chaque synthèse ; aucun raccourci.

**Paramètres d'appel** : `/recherche-produit` seul = exploration libre ; `/recherche-produit <niche ou consigne>` = recherche cadrée. La consigne est transmise à la phase 1.

## 8. Archivage des anciens skills

- Créer `~/.claude/skills-archive/` et y déplacer `niche-scorer`, `competitor-analyzer`, `margin-calculator` (dossiers complets, rien n'est supprimé).
- Motif : critères de mars 2026 en conflit direct avec les critères actuels ; déclenchement intempestif sur « niche », « marge », « concurrence ».
- Les formules de coûts encore pertinentes du `margin-calculator` (frais Shopify/Stripe/PayPal, coûts fixes) sont reprises **à jour** dans les instructions de la phase 5, en cohérence avec le cadre SASU.
- Les autres skills (`google-ads-launcher`, `klaviyo-flow-builder`, `customer-service-bot`, `seo-content-pipeline`, `shopify-product-creator`, `meta-ads-creator`, `performance-analyzer`, `q4-strategy-generator`, `link-building-machine`, `webmaster-lfs`) ne bougent pas : ils concernent l'après-lancement, hors périmètre.

## 9. Limites connues et assumées

1. **Dépendance aux outils vivants.** Phases 3 et 4 utilisent SEMrush (via navigateur), Google et AliExpress. Blocage, CAPTCHA ou changement d'interface → arrêt propre et déclaré, jamais de chiffres inventés.
2. **Exécution séquentielle.** Une recherche complète prend du temps réel. Si le besoin de vitesse se confirme, la phase 4 pourra être parallélisée plus tard (approche C, script Workflow) sans changer l'architecture.
3. **Le registre dépend de sa mise à jour.** D'où la règle : mise à jour après chaque phase par l'orchestrateur, pas en fin de chaîne.
4. **Pas de dépôt git.** Le dossier n'est pas versionné ; la traçabilité repose sur les rapports datés et le registre. Une mise sous git pourra être proposée séparément.

## 10. Plan de mise en œuvre

1. Créer `registre-candidats.md` et le semer avec l'historique (13 candidats V2, 10 niches V1, rejets documentés, 2 tests passés).
2. Créer les cinq fichiers d'agents dans `.claude/agents/`.
3. Créer l'orchestrateur `.claude/skills/recherche-produit/SKILL.md`.
4. Archiver les trois anciens skills dans `~/.claude/skills-archive/`.
5. Test à blanc : lancer `/recherche-produit` sur un périmètre restreint et vérifier le respect des gates, des interdits et du registre avant toute utilisation réelle.

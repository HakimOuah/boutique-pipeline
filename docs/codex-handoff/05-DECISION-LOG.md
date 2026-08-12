# 05 — Journal des décisions (reconstitué)

> Dossier de passation Codex — généré le 2026-07-30.
> Étiquettes : **[FAIT — repo:chemin]**, **[MÉMOIRE]**, **[NOTION]**, **[HYPOTHÈSE]**, **[OBSOLÈTE POSSIBLE]**, **[CONTRADICTOIRE]**, **[MANQUANT]**.
> Règle de lecture imposée par Hakim : **ne jamais transformer une ancienne hypothèse en décision finale.** Quand une décision a été remplacée, les deux états sont conservés avec leurs dates. Les contradictions sont documentées avec une résolution *proposée*, marquée « à valider ».
> Format par décision : date · contexte · options · décision · raison · conséquences · statut · réévaluation.

---

## Partie 1 — Décisions de pipeline (recherche produit)

### D-2026-06 · Cadre commercial SASU et règles héritées Bien Brûlé / Lihyl

- **Date** : juin 2026 (export du 23/06). **[FAIT — repo:../CONTEXTE-MEMOIRE-pour-Codex.md]**
- **Décisions toujours structurantes** : calculs en HT/TVA au réel/IS (SASU OH Ventures, jamais micro-entreprise) ; jamais de fausse preuve sociale (cause de la suspension GMC Bien Brûlé « misrepresentation », résolue) ; mobile-first ; un CTA dominant par section ; le connecteur MCP Shopify n'écrit pas un thème live.
- **Statut** : actives. ⚠️ Le document lui-même est un instantané **partiellement périmé** (domaines, règle « Semrush OFF par défaut » — voir D-0720-SEM) [OBSOLÈTE POSSIBLE].

### D-0717-A · Pipeline de recherche produit par sous-agents ; anciens skills archivés

- **Date** : 17/07/2026. **[FAIT — repo:specs/2026-07-17-pipeline-agents-phases-1-5-design.md, validé section par section par Hakim]**
- **Contexte** : trois défauts récurrents — critères périmés appliqués par les skills de mars 2026 (`niche-scorer`, `competitor-analyzer`, `margin-calculator`), mélange entre phases (verdicts marché contaminés par le sourcing), perte de mémoire entre recherches.
- **Options** : garder les skills historiques / un seul gros skill / orchestrateur + sous-agents dédiés (approche A).
- **Décision** : orchestrateur `/recherche-produit` + 5 sous-agents ; **archivage** des 3 anciens skills (`~/.claude/skills-archive/`, vérifié présent le 30/07) ; critères centralisés dans `PRODUCT-RESEARCH-CRITERIA.md` (jamais copiés dans les agents) ; registre central anti-doublon ; enchaînement fail-closed.
- **Conséquences** : toute recherche produit passe par les skills, jamais « à la main » en conversation. **Ne pas restaurer les skills archivés.** **[MÉMOIRE — pipeline-recherche-produit-agents.md]**
- **Statut** : actif.

### D-0719-A · Persona obligatoire et bloquant avant tout copywriting

- **Date** : 19/07/2026 (demande explicite de Hakim, préparation Tuftéo). **[MÉMOIRE — persona-obligatoire-copywriting.md]** + **[FAIT — repo:PLAYBOOK.md étape 1d + Phase 4 « pas de persona validé = pas de rédaction »]**
- **Décision** : document persona depuis `templates/persona.template.md`, stocké dans `personas/`, **validé par Hakim** avant la moindre rédaction ; chaque douleur/objection adossée à une preuve (verbatim avis, FAQ, forum), observé `[O]` / déduit `[D]` distingués.
- **Conséquences** : ticket 02 du campement (« BLOQUANT copywriting ») ; exemples : `personas/persona-tufting-2026-07-19.md`, `personas/persona-noirmont-2026-07-25.md`.
- **Statut** : actif.

### D-0718-A · Fichiers locaux = source de vérité, Notion = tableau de bord

- **Date** : 18-19/07/2026 (montage du hub Notion « Pipeline Boutiques Drop »). **[MÉMOIRE — notion-pipeline-boutiques.md]**
- **Options** : Notion comme base principale / Notion comme miroir.
- **Décision** : les verdicts et données s'écrivent dans les fichiers locaux **d'abord**, puis sont répliqués dans Notion. Jamais de recopie de verdicts « de mémoire ». Les gros JSON ne sont pas recopiés intégralement (risque d'altération) : aperçu + MD5, fichiers locaux = source byte-exacte.
- **Raison** : auditabilité, git, et limites du plan Notion (`query_data_sources` restreint).
- **Conséquences** : règles inviolables des skills — registre d'abord ; panne Notion non bloquante (`notion-sync-pending.md`, rattrapage documenté fait le 19/07) ; pas de doublon. Synchro rendue **automatique** au fil de l'eau le 20/07.
- **Statut** : actif. C'est un invariant à préserver dans toute migration.

### D-0720-A · Inversion volume-first : la boucle `/chasse-clusters`

- **Date** : 20/07/2026 matin. **[FAIT — repo:specs/2026-07-20-boucle-chasse-clusters-design.md, validé par Hakim]**
- **Contexte** : comptage du registre au 19/07 — ~30 candidats sur ~50 morts en phase 3 sur le volume, après tout le travail créatif ; taux d'acceptation ≈ 4 % ; motif récurrent : parent à 8-12 k mais 1-4 k adressables après nettoyage SERP.
- **Options écartées et documentées** : workflow multi-agents parallèle (une seule session Chrome SEMrush = pas de gain, complexité payée pour rien) ; minage de concurrents type VEVOR/ManoMano comme source primaire (ne trouve que des marchés déjà occupés — contraire au §4).
- **Décision** : boucle séquentielle autonome via `/loop`, objectif 20 candidats (plancher 15), profondeur « fiche AliExpress vérifiée » sans phase 5, familles de marché comme vocabulaire d'entrée, critique aveugle au compteur, arrêt fail-closed (dont « 3 familles stériles consécutives »).
- **Statut** : construite et exécutée le jour même — puis **rétrogradée en voie secondaire l'après-midi même** (voir D-0720-C). Illustration de la règle « ne pas transformer une hypothèse en décision finale » : la boucle n'a jamais été « la » voie définitive.

### D-0720-B · Case fournisseur = critère d'existence, pas de qualité (confiance A/B/C)

- **Date** : 20/07/2026. **[FAIT — repo:.claude/agents/critique-candidat.md « Décision de Hakim du 20 juillet 2026 » + registre-candidats.md]**
- **Contexte** : des fiches AliExpress valables étaient éliminées pour « vendeur sans avis » ou « expédition Chine ».
- **Décision** : la case 3 prouve que le produit est **sourçable** et qu'une fiche précise lui correspond — Hakim vérifie lui-même, quitte à commander un échantillon. Qualité vendeur → niveau de confiance A/B/C, jamais un filtre. Restent éliminatoires : pas de fiche, fiche ne correspondant pas au produit, prix rendu ≥ prix marché.
- **Statut** : actif.

### D-0720-C · Pivot de l'après-midi : `/qualifie-idees` (hybride idées + mesure express) devient la voie principale

- **Date** : 20/07/2026 après-midi. **[MÉMOIRE — boucle-chasse-clusters-volume-first.md]** + **[FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md §7 réécrit]**
- **Contexte** : bilan de la boucle — 7 familles balayées, **1 seul RETENU** (fontaine à gravité, confiance A), 2 dossiers remontés, arrêt réglementaire sur 3 familles stériles ; coût ≈ 840 k tokens par famille. Le balayage élimine bien les morts tardives mais « broie des familles sans jugement de potentiel et ne nomme que ce que le vocabulaire nomme déjà ».
- **Décision** : chemin A (entrée par l'idée) redevient principal, **mais** avec mesure express obligatoire (phase 0 ciblée + sonde prix, ~6 min) avant tout travail qualitatif. `/chasse-clusters` reste disponible, familles choisies à la main. Compteur commun 2/20, même registre.
- **Statut** : actif — c'est l'architecture en vigueur au 30/07.

### D-0720-D · Brand Search devient la source d'idées principale

- **Date** : 20/07/2026 (recette de filtres établie par Hakim le jour même). **[MÉMOIRE — brand-search-source-idees.md]** + **[FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md §2, .claude/agents/mineur-brandsearch.md]**
- **Décision** : idéation par minage de boutiques **prouvées** en Google Ads France (origine FR, 0 Meta actif, ≥ 1 Google Ad, prix moyen ≥ ~130 $). Familles d'exploration mises de côté (bandeau dans `familles-exploration.md`).
- **Raison** : une boutique qui vit en 100 % Google Ads FR dans la tranche répond avant la phase 3 à « une boutique spécialisée peut-elle exister en Search ? ».
- **Conséquences vérifiées** : vague 1 (20/07 soir) : 20 idées → 1 RETENU (surpresseur), 3 À APPROFONDIR dont **Seiko mod**. Leçon : vérifier la boutique preuve au Transparency Center région France (wondermural invalidée). Limites MCP consignées (paramètre `markets` inopérant, `avg_price_usd: 0.0` = donnée manquante).
- **Statut** : actif.

### D-0720-E · « Explicable-particulier », pas « technique-pro »

- **Date** : 20/07/2026 (bilan des familles 1-4, toutes stériles). **[MÉMOIRE — explicable-particulier-pas-technique-pro.md]** + **[FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md §3]**
- **Décision** : le levier n'est pas « produit technique » mais « produit explicable au particulier » (osmoseur, fontaine, tufting). **Signal d'exclusion** : vocabulaire de métier dans le cluster (profession, chantier, devis, location, formation) = persona pro = exclusion ou vivier. Cas d'école : la plieuse zinc, une chaîne complète perdue.
- **Conséquences** : §3 réécrit, familles réordonnées, le mineur Brand Search applique le filtre dès l'extraction.
- **Statut** : actif.

### D-0720-F · Espace Codex parallèle et isolé

- **Date** : 20/07/2026. **[FAIT — repo:codex-chasse-clusters/README.md, source-integrity-notes.md]**
- **Décision** : adaptation Codex de la boucle, séparée « afin de permettre une comparaison honnête » — lecture seule des canoniques, écritures confinées, empreintes SHA256.
- **Résultats** : run 1 : 40/40 familles, 17 `RETENU_MARCHE_A_SOURCER`, **sans abaisser les seuils** ; AliExpress bloqué pour Codex (« Browser Use rejected this action ») → statut dédié + requêtes de sourcing manuel. Run 2 (Brand Search multi-marchés) : 8 candidats + radar 30. Claude a ensuite fait le sourcing d'existence des 8 (`reports/sourcing-existence-codex-8-2026-07-20.md`).
- **Statut** : précédent réussi de cohabitation Claude/Codex ; le point dur identifié est l'accès navigateur AliExpress.

### D-0721-A · Dérogation multi-marchés DE/IT sur liste restreinte

- **Date** : 21/07/2026. **[MÉMOIRE — boucle-chasse-clusters-volume-first.md]**
- **Décision** : la liste restreinte scorée par Hakim inclut volontairement des produits DE/IT (Gewichtsdecke, Handpan) — ne plus objecter « hors périmètre ». Le périmètre France-d'abord reste la règle par défaut ; Hakim peut y déroger explicitement.
- **Point ouvert** : seuils DE/IT non configurés (précédent : seuil DE `null`) — **à fixer avec Hakim avant toute phase 3 sur ces marchés**.
- **Statut** : orientation active, non instrumentée. Liste au 21/07 : Seiko mod 85, tufting 77, Gewichtsdecke 75, Handpan 75, couverture lestée FR 72, papier peint 70, surpresseur 70, pompe immergée 65.

### D-0720-SEM · SEMrush : d'« essais ponctuels » à compte payant

- **Dates** : règle du ~23/06 : « ne pas activer SEMrush par défaut, essais ponctuels pour économiser la tréso » **[FAIT — repo:../CONTEXTE-MEMOIRE-pour-Codex.md §2.1 + PLAYBOOK.md 1b]** ; à partir du 20/07, tout le pipeline mesure sur « SEMrush avec compte connecté (à souscrire) » **[FAIT — repo:specs/2026-07-20]** puis « SEMrush (compte payant) » **[FAIT — repo:boutique-seiko-mod/journal/2026-08-08-reprise-session.md]**.
- **[CONTRADICTOIRE]** entre le PLAYBOOK (« Semrush désactivé par défaut ») et la pratique depuis le 20/07. Nuance mesurée le 27/07 : le compte affichait « formule payante active (badge Trial active) », 86/1 000 crédits consommés **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-marche-complet-semrush.md]** — donc possiblement toujours un **essai** au sens de la doctrine « essais ponctuels », pas un abonnement pérenne. **Résolution proposée** : considérer SEMrush comme disponible tant qu'un essai/abonnement est actif, en le vérifiant en début de session (mot-clé témoin — une formule gratuite rend « 0 mot clé » sans erreur passé le quota). **Statut d'abonnement réel à valider par Hakim.**
- **Réévaluation** : coût récurrent à arbitrer dans la vision cible (API SEMrush vs scraping navigateur).

### D-0722-A · Corrections de doctrine issues du build Tuftéo (22-23/07)

**[MÉMOIRE — da-creative-pas-premium-fade.md, mobile-first-et-placeholders-demo.md, promesses-verifiables-guide-numerique.md, import-avis-trustoo-bookmark.md]**

1. **DA créative, pas premium fade** (22/07) : sur une niche DIY, le pastel sage est un défaut ; contrastes francs, accents pop, mouvement. **La direction de DA se propose à Hakim avant application** — c'est une décision de marque. Statut : actif.
2. **Mobile-first prioritaire** (22/07) : « la version mobile, au final, c'est la plus importante ». Statut : actif.
3. **Placeholders de preuve sociale = chasse gardée de Hakim** (21 et 22/07, consigne donnée deux fois) : ne jamais écraser les sliders/avis démo — il les remplace lui-même par du réel. Statut : actif.
4. **Toujours re-télécharger le template live avant de patcher** (22/07, après écrasement de modifs de Hakim) : un upsert envoie le fichier entier. Statut : actif.
5. **Promesses vérifiables — pas d'insert physique en dropshipping** (22/07) : « notice française incluse » était invérifiable (on ne contrôle pas le carton) → produire le contenu soi-même et le livrer **en numérique** (« offert / accès inclus », jamais « dans le colis »). Garde-fou transversal à toutes les boutiques. Statut : actif.
6. **Vidéo IA : jamais le produit en fonctionnement** (22/07, hero Seedance rejeté) : l'IA rate la mécanique observable ; cadrer avant/après. QA des clips = physique du produit. Statut : actif.
7. **Thème publié = plus d'écriture API directe** (23/07) : `themeFilesUpsert` bloqué sur thème MAIN ; chemins restants — manip guidée pour Hakim, ou dupliquer/patcher/publier. Statut : actif (revérifié sur Noirmont).
8. **Import d'avis en masse via bookmarklet Trustoo piloté** (23/07, 22 fiches Tuftéo) : recette Chrome+JS documentée ; config « All » laisse passer des avis 1-2★ → Hakim filtre. Statut : actif.

### D-0725-A · Campement type Notion (20 tickets) et référence légale Tuftéo

- **Date** : 25/07/2026 (créé à la demande de Hakim) ; skills intégrés aux tickets le 26/07. **[MÉMOIRE — campement-type-lancement-boutique.md]** + **[NOTION — base `da8b39cc…` relue le 30/07 : 20 tickets 00→17 dont 00b et 12b]**
- **Décision** : chaque lancement de boutique = duplication du Kanban ; chaque ticket est un brief d'agent autonome avec garde-fous et critères de fin ; boutique de référence des pages légales = **Tuftéo** (confirmé par Hakim le 25/07).
- **Note de fraîcheur** : la fiche mémoire dit 18 puis 19 tickets ; Notion en contient 20 [CONTRADICTOIRE — comptage Notion fait foi].
- **Statut** : actif.

### D-0726-A · Skills communautaires skills.sh en global

- **Date** : 26/07/2026. **[MÉMOIRE — skills-sh-ecommerce-installes.md]** + **[FAIT — dossiers dans `~/.claude/skills/`]**
- **Décision** : installer les packs Corey Haines (13), Higgsfield (3), ui-ux-pro-max, brandkit, shopify-liquid ; `ads`/`ad-creative` remplacent en profondeur les skills maison ads **mais** les skills maison restent la couche « règles Hakim » (budgets 15-20 €/j, Shopping Standard d'abord, ×1,3) : **invoquer ensemble**. Écarté : `nexscope-ai/ecommerce-skills` (frontmatter cassé).
- **Statut** : actif.

---

## Partie 2 — Décisions Noirmont (boutique Seiko mod, 24-30/07)

### D-0724-N0 · Positionnement : 100 % stérile, et « la parole tenue » plutôt que le storytelling atelier

- **Dates** : 24-25/07/2026. **[FAIT — repo:boutique-seiko-mod/journal/2026-07-24-analyse-concurrent-montreapapy.md, boutique-seiko-mod/journal/2026-07-24-analyse-configurateur-goteia.md, boutique-seiko-mod/journal/2026-07-25-objections-positionnement.md]**
- **Décision structurante** : **cadran 100 % stérile, aucun logo emprunté, jamais.** Le naming communautaire (SUB, GMT, Pepsi…) est autorisé, le logo ne l'est jamais — la communauté trace la ligne au logo, pas à l'hommage ; Seiko a publié un avertissement officiel sur les mods ; les concurrents (Goteia, WatchModCustom) affichent des cadrans siglés = « le seul point où ils sont attaquables ».
- **Axes de positionnement** (25/07) : options A « Sans logo, sans mensonge » / B « La parole tenue » / C « Le prix juste, expliqué » → **B en socle, A en identité, C en dose homéopathique**. Raison mesurée sur Trustpilot : les 3 boutiques FR mal notées meurent toutes sur livraison/SAV, pas sur le produit.
- **Interdit acté** : **ne jamais écrire « assemblée en France »** (« le mensonge fondateur des 1★ du marché »). Corollaire délais : promesse **J+14/J+21** volontairement au-dessus des délais fournisseur relevés (5-15 j) ; livraison France offerte mono-zone.
- **Statut** : actif, garde-fou cité dans tous les livrables suivants.

### D-0724-N1 · Pousser Seiko mod malgré le « À APPROFONDIR » ; sourcing en 4 volets

- **Date** : 24/07/2026. **[FAIT — repo:registre-candidats.md « phase 4 sourcing AliExpress faite sur décision Hakim » + reports/phase4-sourcing-seiko-mod-2026-07-24.md, phase4b, phase4c, phase4d]**
- **Contexte** : Seiko mod était sorti de la vague Brand Search en À APPROFONDIR (marques déposées + ~20 spécialistes FR) avec 17,6-20 k/mois ; noté 85 sur la liste restreinte du 21/07.
- **Décision** : Hakim tranche lui-même (c'est le fonctionnement voulu : les cas limites lui appartiennent) et lance le sourcing — fiche SUB stérile Tandorio retenue pour commande test, puis volets 4b « montre configurée », 4c « réplication Seikojust », 4d « accessoires + SKX ».
- **Conséquences** : création de `boutique-seiko-mod/` et build de Maison Noirmont (`v42pzp-h4.myshopify.com` / `maisonnoirmont.fr`).
- **Statut** : boutique construite, **sous mot de passe, 0 commande** au 30/07.

### D-0724-N2 · Leçons techniques du build initial (canal, faux logos, thème brouillon)

- **Date** : 24/07/2026. **[MÉMOIRE — shopify-canal-et-visuels-ia.md]**
- **Décisions/constats** : (1) produits DSers/API = ACTIVE mais publiés sur aucun canal → `publishablePublish` en batch obligatoire ; (2) l'IA image (`soul_2`) imprime de **faux logos** sur tout cadran face caméra, « no logo » ne suffit pas → compositions qui cachent le cadran + inpainting OpenCV local + contrôle à l'œil ; (3) thème **brouillon** 100 % pilotable par API (staged upload → `themeFilesUpsert`), jamais le thème publié.
- **Statut** : actif — repris dans le ticket 08 du campement.

### D-0725-N1 · Découpage du catalogue : 1 fiche produit = 1 coloris, naming communautaire, ~100 fiches cible

- **Date** : 25/07/2026. **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-catalogue-v2-analyse-concurrents.md §Décisions Hakim, boutique-seiko-mod/journal/2026-07-25-plan-decoupage-coloris.md, decoupage-coloris-lot1-…, boutique-seiko-mod/journal/2026-07-31-decoupage-elagage-lot2.md]**
- **Contexte** : 10 fiches montres à menus « Référence M-1…M20 » opaques ; minage en direct des concurrents — montreapapy 111 fiches (~10 familles déclinées coloris par coloris), Goteia 34+5. « Nous faisons exactement l'inverse. » Demande de Hakim : étoffer le catalogue.
- **Options** : A découper les coloris déjà sourcés (+35, zéro sourcing neuf) ; B nouvelles familles (+20-30, dépend d'un import DSers Hakim) ; C accessoires (+12-15) ; D carte cadeau.
- **Décisions Hakim (3, consignées)** : (1) **découpage maximal** (~45 fiches, ordre A→D→B/C, cible ~100 fiches) ; (2) **naming communautaire** (Pepsi, Batman, Hulk, Panda, Wimbledon… — « le naming décrit un coloris, jamais un logo ») ; (3) **facturer les mouvements haut de gamme** (voir N2).
- **Exécution** : renommage préalable de 117 valeurs opaques (rapprochement code→vignette **exact** par identifiant d'attribut AliExpress, 0 SKU modifié) ; lot 1 : 19 fiches / 92 variantes, SKU-prix concordants 92/92 ; lot 2 : **41 fiches créées, 166 variantes élaguées (sauvegardées, recréables), catalogue 44 → 85** ; principe validé en cours de route : « **on ne supprime jamais une valeur pour réduire un nombre de fiches** ».
- **[CONTRADICTOIRE — plan vs exécution]** : le plan prévoyait de renommer chaque mère en « coloris n°1 » ; l'exécution a été **strictement additive** (mères intactes), la **réduction des mères** étant une étape irréversible mise en attente — **jamais exécutée au 30/07** (les 4 mères sont toujours ACTIVE). Ordre imposé si on la fait : mapper les filles d'abord (supprimer une variante détruit son mapping DSers).
- **Pièges consignés** : passer une URL CDN en `originalSource` **écrase l'`alt` du fichier d'origine** (31 réparés, 8 perdus/reconstruits) — rattacher par `MediaImage` GID ; **le SKU ne prouve pas l'identité visuelle** d'une image après découpage.
- **Conséquences** : c'est ce qui a rendu possibles les visuels par coloris (26/07) puis le configurateur-guide. **Statut : fait, actif** (réduction des mères = décision ouverte).

### D-0725-N2 · Facturation des mouvements premium (échelle de prix par mouvement)

- **Date** : 25/07/2026. **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-catalogue-v2-analyse-concurrents.md §Échelle de prix + boutique-seiko-mod/journal/2026-07-25-bilan.md]**
- **Contexte** : mécanique concurrente minée — montreapapy vend en base 289/299 € + suppléments par option jusqu'à 501 € (app Mczr, paliers de prix déguisés en variantes) ; Goteia au prix unique 349 €.
- **Options** : prix unique toute configuration (Goteia) vs base + suppléments (montreapapy).
- **Décision Hakim** : facturer les mouvements haut de gamme — motif cité : « **ça ajoute du crédit à la marque** ». Règle : **le prix d'entrée de chaque montre reste inchangé, seules les configurations premium montent**. Échelle : Mingzhu/Miyota/DG3804 = base ; **Seiko NH34/NH35/NH36 +39 €** ; **PT5000 +89 €** ; **fond verre +29 €**. Prix barré ×1,3 recalculé à chaque palier.
- **Exécution** : 184 variantes sur 7 produits, 0 erreur (script `scratchpad/theme-noirmont/build_movement_ladder.py`) ; échelle reconduite sur toutes les fiches découpées.
- **Garde-fous liés** : PT5000 = « suisse-clone », jamais présenté comme suisse (mentions « Swiss Made » incrustées dans des visuels traitées comme allégation d'origine fausse et régénérées) ; **VK63 méca-quartz à pile, jamais « automatique »** ; marques tierces autorisées **uniquement** en valeurs d'option (fabricants de calibres) ; le calibre n'est **pas une question client** dans le guide de choix (persona métier qu'on s'interdit).
- **Statut** : fait, actif.

### D-0725-N3 · Accessoires : entrer par import DSers, pas par l'API

- **Dates** : décision nuit du 25/07, exécution 26/07/2026. **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-journal-nuit.md §BLOQUÉ, boutique-seiko-mod/journal/2026-07-31-import-accessoires-lot4.md, boutique-seiko-mod/journal/2026-07-25-bilan.md]**
- **Options** : A créer les 13 fiches accessoires par l'API Shopify (rapide, navigateur libre) ; B import DSers puis enrichissement API.
- **Décision : B.** Raison textuelle : « un produit créé à la main **n'a pas les SKU portant la chaîne d'attributs AliExpress**, donc le mapping devient manuel variante par variante. **L'import DSers donne les bons SKU *et* le mapping d'un coup.** » Leçon versée au campement : « créer un produit dropshippé à la main est un faux gain de temps ».
- **Décision connexe** : import **différé** cette nuit-là plutôt que fait à moitié — « un import à moitié fait est pire que pas d'import » (produits fantômes DSers).
- **Exécution 26/07** : 13 URLs importées une à une, PUSH TO STORE en **Draft** hors canal, puis réécriture API (titres, prix, SEO, collections) ; compteurs DSers 85 → 98, Unmapped 0 ; le push a révélé des coûts par variante absents du sourcing → 6 fiches re-tarifées plutôt que vendues à perte. Règle de prix accessoires : coût rendu ×3-4 arrondi au ,90 ; barré ×1,3.
- **Statut** : fait, règle reprise au ticket 04 du campement.

### D-0725-N4 · Images : galerie 7 postes, « les 3 dernières composées par code » (25/07), puis abandon des cartes typographiques (26/07, arbitrage Hakim)

- **25/07** **[FAIT — repo:boutique-seiko-mod/journal/2026-07-24-runbook-pdp-variantes-images.md l.100-102, boutique-seiko-mod/journal/2026-07-25-bilan.md]** : galerie-type de 7 images par montre (face, situation, caractéristique, action, détails, preuve sociale, témoignage) — les slots carte-carac / carte-preuve / carte-témoignage **composés par code (Pillow + polices du thème), jamais générés par IA**. Raison écrite : « un modèle d'image ne sait pas écrire du texte propre » — 175 fichiers sur 390 à coût nul en crédits **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-obsolete-ne-pas-utiliser-prompt-galeries-v1.md.bak]**. 351 médias AliExpress supprimés (« plus une seule image fournisseur »).
- **26/07 ~02:57 — ABANDON, arbitré par Hakim** **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-audit-visuel-catalogue.md « Version 3 — standard arbitré par Hakim le 26/07 »]** : galeries **100 % photographiques**, aucune carte typographique, ajout du **porté-poignet**. Montres = face·situation·macro·poignet ; accessoires = face·situation·macro.
- **Raison — opérationnelle, pas budgétaire** (le budget crédits monte même légèrement, 390 fichiers → 230 mais 215 → 230 générations) : le script de composition Pillow avait été **perdu** et aurait dû être réécrit ; plus de polices, de citations à sourcer, d'arbitrage typographique ; et « **le problème de conformité des avis inventés sort des galeries** » (les cartes affichaient « 4,8/5 · 1340 avis » sans commande réelle).
- **Reliquat non tranché** : **46 cartes typographiques restent en ligne** (suppression de médias non autorisée aux agents) + 6 images à cartouche texte incrusté sauvegardées non supprimées — **à trancher par Hakim** **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-audit-visuel-catalogue.md l.304, boutique-seiko-mod/journal/2026-07-31-branchement-galeries-codex.md]**.
- **Statut** : standard v3 (100 % photo) actif ; galeries branchées les 25-26/07 (85 fiches, 206 médias).

### D-0725-N5 · Modèles d'images IA : soul_2 proscrit (24-25/07) → comparatif 5 modèles → nano_banana_pro retenu (25/07) → GPT Image 2 pour Codex (26/07)

- **24/07** : `soul_2` utilisé par défaut pour la première fournée → constat immédiat : il **imprime de faux logos/textes sur tout cadran face caméra** ; contournements du jour : compositions cachant le cadran + inpainting OpenCV local **[FAIT — repo:boutique-seiko-mod/journal/2026-07-24-build-site.md]** **[MÉMOIRE — shopify-canal-et-visuels-ia.md]**.
- **25/07** : cause racine nommée — `soul_2` est un modèle **UGC/éditorial mode**, « il fabrique du branding parce que ses références en portent » → **proscrit pour tout packshot**, leçon générique versée au campement **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-images-modeles-et-coloris.md, boutique-seiko-mod/journal/2026-07-25-bilan.md]**.
- **25/07 — comparatif demandé par Hakim** (tâche de test = la tâche réelle, recolorer un cadran) **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-images-modeles-et-coloris.md §2]** : **nano_banana_pro 4K retenu** (4 cr, 4096 px natif, écart hors cadran 4,18) ; `gpt_image_2` écarté **uniquement sur le coût (×3) et la résolution** (« 4K » = 2880 px), qualité jugée équivalente ; **`openai_hazel` éliminé** (invente un « XII » typographié et une trotteuse — « ce n'est plus la montre vendue ») ; `flux_kontext` réécrit le prompt tout seul ; `recraft_v4_1` exclu d'office (pas d'image de référence).
- **25/07 — bascule doctrinale sur la retouche** : l'inpainting est **interdit** (« c'est cette retouche qui a produit un défaut visible ») → on **régénère** (face GMT refaite ainsi) ; recette canonique : image-to-image depuis la face validée, 2048×2048 JPEG q90, contrôle de **stérilité au zoom** cadran par cadran, texte détecté = régénération **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-archive-prompt-reprise-visuels.md.bak, boutique-seiko-mod/journal/2026-07-31-prompt-codex-galeries.md]**.
- **26/07** : démonstration que le « gommage » d'un texte existant échoue (2 passes, le modèle **atténue au lieu de supprimer**) → troisième voie : repartir d'une **sœur déjà stérile** et ne changer que la couleur (5/5 réussis) ; règle « un lettrage atténué compte comme un lettrage présent », contrôle qualité à ≥ 740 px/vignette et recadrage ×5 de la zone 5h-7h **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-branchement-galeries-codex.md]**.
- **26/07 02:54 — GPT Image 2 désigné pour Codex** (renversement **assumé et motivé** du comparatif) : « nous ne l'avions pas retenu que pour le coût et la résolution native — deux objections sans objet ici, puisque tu y accèdes nativement et que le format de livraison est 2048 px » ; interdits transmis (modèles UGC/mode, modèles d'édition qui réinventent l'objet) **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-prompt-codex-galeries.md l.58-66]**. Trace d'exécution : `"modeleUtilise": "GPT Image 2 natif"` dans les scripts livrés par Codex.
- **Statut** : nano_banana_pro côté Claude/Higgsfield, GPT Image 2 côté Codex — les deux actifs. [CONTRADICTOIRE mineur : coût 4K mesuré à ~5,3 cr/image le 25/07 puis 4 cr le 27/07 (`boutique-seiko-mod/journal/2026-07-31-visuels-aviateur-consolidation.md`) — budgets à recalculer à la baisse.]

### D-0726-N1 · Charte : v1 vert-jura/laiton → direction « A+B » (citron) → révision cyan

- **Dates** : 24-26/07/2026. **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-charte-noirmont.md, brand-tokens-noirmont.json, boutique-seiko-mod/journal/2026-07-25-design-modernisation.md, audit-uiux-*.md, boutique-seiko-mod/journal/2026-07-31-charte-ab-application.md, boutique-seiko-mod/journal/2026-08-08-reprise-session.md]**
- **Trajectoire** : (1) charte v1 du 24-25/07 — accent **vert-jura `#1E3A2F`** + filets **laiton `#A98E5F`**, Bodoni Moda/Inter/Space Grotesk, tagline arbitrée par Hakim « Votre signature au poignet » ; (2) 25/07 — modernisation sur le modèle `montre-avenue.com` (même thème FullStack : casse normale des titres, 3 colonnes, corps 16 px) ; (3) 26/07 — direction « **A+B** » validée par Hakim : accent unique **citron acide `#D6FF3F`**, grotesque haute (Bodoni → **Oswald**, Space Grotesk → Inter), chiffres tabulaires — les audits du 26/07 constatent qu'elle n'était pas appliquée (0 occurrence du citron) et déclenchent l'application ; (4) **révision R2 le 26/07 : citron → cyan `#22D3EE`** — raison mesurée : le citron ne valait que **1,05:1** sur craie, pire que le cyan (1,72:1) ; d'où la **règle impérative** : le cyan est la couleur de l'**instrument** (puces de specs, traits de cote, focus, `::selection`), **jamais un bouton ni un badge commercial**, il ne porte jamais seul une information. Vert forêt et laiton **purgés à la source, ne pas réintroduire** (22 occurrences résiduelles re-purgées le 27/07).
- **[MANQUANT — trou documentaire]** : les propositions A et B **elles-mêmes** ne sont documentées nulle part dans le dossier (vraisemblablement présentées en conversation) ; « A+B » n'est reconstituable que par ses effets. Prévoir de re-documenter la charte si elle doit être défendue.
- **Statut** : actif (état consolidé dans REPRISE-SESSION §Charte).

### D-0726-N2 · Étoiles d'avis en vert Trustpilot `#05b67a`

- **Dates** : 25/07 (passe « retours Hakim » — `stars_icons_color` dans les 3 schémas de couleurs), défendue ensuite contre la charte à chaque audit. **[FAIT — repo:boutique-seiko-mod/journal/2026-07-24-runbook-pdp-variantes-images.md l.80, boutique-seiko-mod/journal/2026-07-31-audit-visuel-catalogue.md « tranché par Hakim, la charte laiton cède », boutique-seiko-mod/journal/2026-07-31-charte-ab-application.md « non touchée », boutique-seiko-mod/journal/2026-08-08-reprise-session.md « ce n'est pas un écart à corriger »]** + **[NOTION — ticket 11 du campement]**
- **Raison** : non écrite explicitement — motif implicite : le code visuel de preuve sociale reconnu (vert Trustpilot). **Conséquence assumée sciemment** : contraste 2,52:1, sous le seuil WCAG 3:1, signalé et conservé.
- **Point ouvert [CONTRADICTOIRE mineur]** : la valeur réellement servie par certains SVG du thème est `#00B67A` (l'original Trustpilot) et non `#05b67a` — jamais réconcilié.
- **Statut** : ferme — un audit UI ne doit pas « corriger » ce vert.

### D-0727-N1 · Bascule stratégique : « le configurateur est une promesse de conversion, pas un argument d'acquisition »

- **Date** : 27/07/2026 (étude SEMrush complète, compte payant). **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-marche-complet-semrush.md + boutique-seiko-mod/journal/2026-08-08-reprise-session.md §Stratégie]**
- **Contexte** : le positionnement envisagé était « montre personnalisable/configurateur » (analyse Goteia du 24/07).
- **Ce que la donnée a tranché (mesuré)** : personnalisation 10 190/mois **mais ~70 % est un autre marché** (photo, bois, gousset, gravure) → adressable ≈ 3 100, déjà tenu par watchmodcustom.com ; **Seiko mod 38 690/mois** (jusqu'à 51 000 étendu), KD 10, CPC 0,22 € — **16× plus de demande utile à difficulté égale** ; `arabic dial` ≈ 15 500/mois sans leader au-dessus de la 4ᵉ position ; `montre squelette` ≈ 8 400 ; goteia.fr tire 0,9 % de son trafic de la personnalisation et 66 % d'un seul article SEO ; l'enchère est vide (seul montreapapy.fr, 212 $/mois). À abandonner : grappe prix (50/mois), style français (560).
- **Décision** : l'acquisition vient du vocabulaire du **mod, du squelette et des cadrans arabes** (SEO/SEM) ; le configurateur reste sur le site comme **promesse de conversion**.
- **Statut** : actée — structure le plan SEO (`boutique-seiko-mod/journal/2026-07-31-plan-nommage-seo.md`, article pilier `boutique-seiko-mod/journal/2026-07-31-article-mod-ou-hommage.md`).

### D-0728-N1 · Configurateur-guide sur catalogue existant (V1 → V2 → V3) ; vrai configurateur en attente de BL Watches

- **Dates** : 27-29/07/2026. **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-configurateur-implementation.md, boutique-seiko-mod/journal/2026-07-31-sourcing-configurateur.md, boutique-seiko-mod/journal/2026-07-31-spec-configurateur-goteia.md, boutique-seiko-mod/journal/2026-07-31-axes-guide-de-choix.md, boutique-seiko-mod/journal/2026-08-08-reprise-session.md, boutique-seiko-mod/journal/2026-07-31-publication-grappes.md]**
- **Décision de Hakim** : un « configurateur » qui n'en est pas un — **filtrage progressif** du catalogue existant, garanti « impossible de composer une montre qu'on ne vend pas ». Vocabulaire contraint : jamais « composez / configurez / montre unique » (ils impliquent un assemblage) ; formule retenue « **Votre Noirmont en trois étapes** ». Pas de prime de prix — contrairement à Goteia, dont la prime réelle mesurée au payload est **+90 à +100 €** (349 € configuré vs 249-259 € fixe ; le brief disait « +30 € » — corrigé) [CONTRADICTOIRE résolu par mesure].
- **Décision de conception issue du reverse Goteia** : leur compositeur (calques PNG par pièce) **n'est pas transposable** ; ce qu'on copie est « le carrousel dont la vignette sélectionnée *est* le produit fini ». Axes de questions mesurés : à 3 questions 13,2 % de chemins aboutissants, à 4 questions 36 % du catalogue invisible → **parcours Famille → Couleur** (2 questions).
- **Livraisons** : V1 le 27/07 (3 écrans / 2 questions, `templateSuffix` réversible) ; **V1 à carrousel rejetée par Hakim** (« elle montrait les produits voisins et leurs noms — un présentoir, pas un configurateur ») ; **V2 « grammaire des pièces » le 28/07** (une seule montre en scène, options illustrées plein écran, aucun nom de catalogue avant la révélation « Voici votre Trente-Neuf », 34/34 chemins vers une vraie variante `/cart/add`) ; **V3 le 29/07** sur trois retours de Hakim (couleurs indisponibles retirées et non grisées, deltas de prix expliqués en français) ; 6ᵉ famille Squelette branchée le 29/07 soir → **35 chemins, 0 mort, 57/57 montres atteignables**, rejoué en clics réels jusqu'à l'ajout panier.
- **Exigence d'interface, insistance explicite de Hakim** : « l'aspect d'un configurateur, pas d'une page de filtres » — une décision à la fois, options illustrées, progression visible, **la montre se met à jour à chaque choix** (possible uniquement grâce aux visuels par coloris du 26/07).
- **Le vrai configurateur (assemblage à la commande)** : trois voies tranchées — (1) fournisseur qui monte à la commande = **la seule compatible, à instruire** ; (2) pièces + assemblage par Hakim = « techniquement faisable, économiquement sans intérêt » (pièces au détail 108-145 € vs montre montée 101-107 € ; le mouvement pèse 43-58 % du coût) ; (3) expédier des pièces = « c'est vendre un kit », écarté. Tout dépend de **BL Watches Parts Store** (a déclaré pouvoir assembler, **ni prix ni délai ni catalogue fournis**) ; ≈ 1 428 combinaisons ouvrables ; axes fermés : aiguilles (aucun alésage publié — « l'arbitrage n°1 à obtenir »), couronne, verre, Miyota 8215. Verdict du rapport : « **Aucun GO. Aucune commande.** » **Statut : décision reportée, ne pas la considérer prise.**

### D-0730-N1 · Cadrans à chiffres orientaux : attendre (et renommage de véracité « à chiffres 1-12 »)

- **Dates** : 27-30/07/2026. **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-verification-catalogue-strategie.md, boutique-seiko-mod/journal/2026-07-31-fiches-contradictoires-et-cadran-arabe.md, boutique-seiko-mod/journal/2026-07-31-sourcing-arabes-squelettes.md, boutique-seiko-mod/journal/2026-07-31-publication-grappes.md, boutique-seiko-mod/journal/2026-07-31-sourcing-chiffres-orientaux.md + boutique-seiko-mod/preuves/preuves-chiffres-orientaux-2026-07-30/]**
- **Chaîne des faits** : 27/07 — les grappes `montre squelette` (≈ 8 400) et `arabic dial` (≈ 15 500) sont servies par **0 fiche sur 53** (« fond verre » ≠ squelette — mirage démonté par trois preuves) ; 3 fiches « plongeuses » contradictoires avec leur fournisseur passées en DRAFT (« c'est le prix de l'honnêteté ») ; le cadran arabe était déjà **dans la chaîne d'approvisionnement**, caché derrière une fiche mal conçue. 29/07 — 5 fiches sourcées et créées par DSers (Éclaireurs, Explorateur 3-6-9, 2 Squelettes), 78 variantes à logo supprimées, purge intégrale des 80 photos fournisseur ; 29/07 soir — 7 fiches publiées ACTIVE sur 3 canaux, collection créée, méga-menu étendu. 30/07 — **Hakim constate sur la vitrine** que « chiffres arabes » fait croire à des chiffres orientaux (١٢٣) qu'on ne vend pas → renommage « **à chiffres 1-12** » / « Cadrans à chiffres », 5 redirections posées **manuellement** (Shopify n'en crée pas), configurateur rejoué (59 handles, 0 mort).
- **La décision « attendre » (30/07)** : le marché des cadrans **orientaux stricts** ne contient que 3 familles — datejust chinois logotés ⛔, fabricant de pièces 0 avis ⛔, Tandorio stérile à 3 avis/10 ventes ⚠️. « C'est une grappe que personne ne sert parce que l'usine ne la produit qu'en très petite série. » Trois options chiffrées ; **verdict : « NON. Aucun candidat publiable selon nos règles en l'état »** — rien importé, rien créé. **À réévaluer dans 6-8 semaines.** Arbitrage réservé à Hakim : publier le Tandorio 8215 suppose de trancher que le mot « Automatic » en cursive à 6h « n'est pas un nom » (cohérent avec l'Explorateur déjà publié).
- **Statut** : en attente d'arbitrage Hakim — c'est l'opportunité SEO n°1 identifiée (D-0727-N1).

### D-0730-N2 · Naming SEO : « les titres produits sont un actif de marque, ils ne bougent pas » — `seo.title` porte les mots-clés

- **Date** : 30/07/2026. **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-plan-nommage-seo.md (étude, rien modifié) + boutique-seiko-mod/journal/2026-07-31-seo-titles-produits.md (exécution)]**
- **Contexte mesuré** (API, 57 fiches montres ACTIVE) : 2/57 titres contiennent le mot « montre », 0/57 un diamètre en « mm » (ils sont en toutes lettres : Trente-Six, Trente-Neuf…), 100 % commencent par un nom de marque français — remarquable pour la marque, invisible pour Google.
- **Options** : (a) `seo.title` repris comme titre du flux Shopping via le canal Google & YouTube (natif, gratuit, global) ; (b) métachamp `mm-google-shopping` par produit ; (c) règles Merchant Center ; (d) app de flux payante.
- **Décision** : **(a)** + principe écrit : « **les noms français de produits sont un actif de marque, ils ne bougent pas** » — titre boutique inchangé 57/57, le `seo.title` porte les mots-clés, écrit pour Merchant Center et plafonné à 65 caractères. Patron : `[Nom de modèle] — Montre [type] [diamètre] mm, [attribut décisif]` ; aucune marque tierce (calibres NH35/Miyota licites) ; « homme » seulement où la fiche l'assume ; pas de promo dans les champs de flux (piège : 53 `seo.description` finissent par « Livraison offerte… » — ne basculer que le titre).
- **Décision « zéro handle touché »** : 0 redirection à gérer, et `snippets/noirmont-configurateur.liquid` code des handles en dur — un handle changé casserait le configurateur.
- **Exécution** : 39 `seo.title` écrits / 18 intacts, ≤ 65 c. sur 57/57, 46/57 avec diamètre chiffré, « automatique » jamais sur un chrono méca-quartz (vérifié par script) ; volumes visés mesurés (`montre automatique homme` 9 900, `chronographe` 3 600), termes non mesurés jamais présentés comme mesurés. Phases 2 (collections) et 3 (flux Shopping) **non exécutées**.
- **Statut** : phase 1 faite ; principe actif.

### D-0725-N6 · Corrections de doctrine versées au campement (fausses limites et pièges vérifiés)

**[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-bilan.md §Leçons, boutique-seiko-mod/journal/2026-07-25-journal-nuit-suite.md §Deux corrections de doctrine, boutique-seiko-mod/journal/2026-08-08-reprise-session.md §Pièges]** — dupliquées dans la page Notion « Campement type ».

1. **CAPTCHA AliExpress = artefact de session, pas une limite du site** (25/07, corrigé le jour même). Position initiale du matin : « les URL de recherche AliExpress sont derrière un captcha, confirmé par trois agents → impossible de balayer par mot-clé » (`sourcing-familles-v2-…`, `sourcing-accessoires-v2-…`). Correction du soir : c'était la conséquence d'un **navigateur sans session** — depuis un Chrome connecté, tout fonctionne ; « j'avais inscrit cette fausse limite dans le campement type — corrigée ». Vérifié sans CAPTCHA les 25, 27 et 30/07. Méta-leçon versée : « **quand un agent conclut “techniquement impossible”, faire revalider dans d'autres conditions avant d'en faire une doctrine.** » La règle « ne jamais résoudre/contourner un CAPTCHA » et son rôle d'arrêt fail-closed restent **intacts** — c'est le diagnostic qui a été corrigé, pas la règle.
2. **Auto-matching DSers par SKU : n'existe pas** (25/07, démenti d'une hypothèse écrite 4 fois le même jour, confirmé deux fois — `dsers-mapping-decoupage`, `dsers-mapping-lot2`). Le fournisseur se rattache mais **toutes les variantes restent vides** ; les SKU servent de table de correspondance pour un appariement **manuel** (méthode déterministe : navigation clavier + lecture du DOM, listes déroulantes qui se repositionnent). Nuance non contradictoire : l'**import DSers natif** (accessoires) apporte SKU **et** mapping d'un coup — c'est un rattachement d'origine, pas de l'auto-matching.
3. **`upsertedThemeFiles: []` sans `userErrors`** — deux cas distincts se cachent derrière la même réponse, et les livrables du 25/07 puis du 26-27/07 se contredisent en apparence : (a) **rejet silencieux** (rien n'est écrit) quand le fichier contient un `custom_css` de section ou un nom de schéma > 25 caractères ; (b) **écriture asynchrone** (le fichier arrive) dans le cas normal. **La seule règle sûre, formulée partout : ne jamais croire la réponse — relire le fichier et comparer `size`/`checksumMd5` aux octets envoyés.** `updatedAt` ne prouve rien ; un nœud `themeFiles` peut être étiqueté d'un nom et contenir un autre fichier. [CONTRADICTOIRE documenté et résolu par cette règle.]
4. Autres pièges vérifiés : chaînes « introuvables » = caractère invisible ; requêtes média plafonnées à 30 ; menus Shopify **partagés entre thèmes** (créer un menu neuf) ; contraste mesuré sur le rendu, opacité héritée comprise ; **ne jamais utiliser `switch-shop`** (invalide la connexion Shopify pour tous — vécu le 24/07) ; le navigateur est une **ressource unique** à sérialiser ; le connecteur refuse d'écrire un thème MAIN ; `productSet` **délibérément refusé** pour les champs liste (il supprime les entrées non incluses — risque d'effacer SKU et mappings) ; `productDeleteMedia` **détache** sans supprimer quand le fichier est référencé ailleurs (prouvé par pilote sur un seul média) ; macOS TCC bloque l'accès aux fichiers pré-existants de `~/Documents`.
- **Statut** : actives.

### D-0726-N3 · Véracité produit : audit des promesses et garde-fou « annoncée »

- **Dates** : 25-27/07/2026. **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-audit-promesses.md, boutique-seiko-mod/journal/2026-07-31-veracite-produit-cloture.md, boutique-seiko-mod/journal/2026-07-31-passe-coherence-avant-publication.md, boutique-seiko-mod/journal/2026-07-25-bilan.md, boutique-seiko-mod/journal/2026-08-08-reprise-session.md]**
- **Audit du 26/07 (déclencheur : les 12 chronos sont des méca-quartz VK63 à pile)** — résultat contraire à l'hypothèse : « le catalogue est propre ; **le mensonge est entièrement dans le thème** » (+ FAQ + page La Maison). 12 corrections : « garde-temps automatiques » → « mécaniques automatiques **et chronographes méca-quartz** » ; carte « NH35 pour tout le catalogue » → « Calibre annoncé » + les **7 calibres réels** (japonais/chinois séparés) ; FAQ « se remonte au porté » conditionnalisée ; aucune fiche n'annonçait de délai (0/99). Piège évité : aucun nom de calibre supprimé.
- **Garde-fou de formulation retenu (26/07)** : le hedge « **annoncée** » — « Étanchéité 10 bar sans souci » → « Étanchéité **annoncée** 10 bar… la plongée reste déconseillée ». Motif écrit : « *sans souci* est la formulation qui finit en litige : elle promet un résultat, pas une caractéristique ; *annoncée* dit honnêtement que la source est le fournisseur. » Source de vérité = **l'attribut vendeur structuré** ; l'« Aperçu IA » AliExpress et les blocs de recommandations sont **écartés** comme sources.
- **Autres décisions rendues** : 12 variantes GMT à logo tiers rendues invendables (`DENY` + stock 0, réversible — sort définitif en arbitrage) ; « Loupe de date — saphir » → « minéral ou saphir » ; les 3 Héritage 5 bar : « “Plongeuse” décrit ici un style, pas un usage » (levé dans le corps, les titres restant à Hakim) ; les 7 Intégrale 3 bar : combler le **silence** qu'un client à 379 € comble tout seul ; badge « En promotion » retiré, règle française du prix de référence (30 jours) à vérifier avant toute remise ; affirmations fausses (« 2 000 clients satisfaits », `review_count: 123`, « 1340 avis ») **à retirer par Hakim** (0 commande — domaine réservé preuve sociale).
- **Passe de cohérence 27/07** : rendu vérifié à 375 px et 1280 px via cadre de mesure à viewport exact (trois instruments croisés), 22 occurrences de couleurs interdites purgées, 89 URLs testées, 34 chemins configurateur validés ; promesse fausse résiduelle trouvée **dans la donnée servie par Helio** (thème publié) — d'où l'urgence de republier.
- **[CONTRADICTOIRE non tranché — « chiffres romains » du Trente-Neuf Duo]** : le BILAN du 25/07 conclut « la fiche fournisseur annonce Index Romain et sa photo le confirme : **c'est notre visuel qui est infidèle** — corriger l'image, pas le texte » ; `boutique-seiko-mod/journal/2026-07-31-verification-catalogue-strategie.md` (27/07) retraite le point comme **ouvert** (« sa photo montre des bâtons : relecture éditoriale indépendante »). **Résolution proposée : revérifier la fiche fournisseur une troisième fois avant toute correction — à valider.**
- **Statut** : garde-fou transversal actif, hérité de D-0722-A(5) et de la doctrine GMC/DGCCRF héritée de Bien Brûlé.

### D-0731-A · Partage des rôles Claude Code / Codex : orchestration conservée, Codex exécutant images — ⚠️ SUPERSÉDÉE par D-0731-B

> ⚠️ **Supersédée le 31/07/2026 au soir par D-0731-B (ci-dessous)** : Codex reprend l'orchestration
> totale (factory + DB Industrie), Claude Code devient exécutant navigateur + solution de secours.
> Le texte de D-0731-A est conservé tel quel pour l'historique — ne plus s'y référer comme état courant.

- **Date** : 31/07/2026 (décision de Hakim). **[INFO HAKIM]** + **[FAIT — repo:ordres/pour-codex/, docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md, ordres/valider_ordre.py]**
- **Contexte** : (1) Codex est bloqué sur AliExpress depuis son environnement (« Browser Use rejected this action due to browser security policy », 20/07) — le blocage est côté environnement Codex, pas côté site ; (2) la qualité d'orchestration de Claude Code est constatée sur les chantiers de production ; (3) Codex dispose de **GPT Image 2 natif, sans compteur de crédits** — contre **87 crédits Higgsfield restants** côté Claude, alors que GPT Image 2 n'avait été écarté du pipeline image que pour coût et résolution native, deux objections sans objet côté Codex (`boutique-seiko-mod/journal/2026-07-31-prompt-codex-galeries.md` §Modèle).
- **Décision** : **Claude Code conserve l'orchestration du projet et toute l'exécution navigateur (AliExpress, DSers) — définitif : Codex n'utilisera pas DSers.** **Codex = exécutant de génération d'images uniquement**, classe A (aucun accès boutique, fichiers seulement), via la boîte inverse `ordres/pour-codex/` et le type d'ordre `generate_images`.
- **Conséquences** : protocole `14` **bidirectionnel** — le sens historique Codex → Claude (ordres navigateur) est conservé mais **dormant** ; le sens actif est Claude → Codex (`14` §9) ; document d'exécutant autoportant `15-CODEX-EXECUTANT-IMAGES.md` (instructions permanentes transmises par Hakim à Codex) ; `12` §7 réécrit en conséquence ; validateur `ordres/valider_ordre.py` étendu au type `generate_images` (chemins confinés dépôt/projet, IDs de variante/média refusés dans les manifestes) ; le branchement Shopify des images livrées reste côté Claude Code. La Partie 3 ci-dessous (« Codex comme exécutant principal / migration d'orchestration ») est **close : orientation non retenue**.
- **Statut** : **supersédée** le 31/07/2026 au soir par **D-0731-B** (reste dans le log pour l'historique).

### D-0731-B · Reprise TOTALE de l'orchestration par Codex (factory + DB Industrie) — supersède D-0731-A

> ⚠️ **Supersédée le 31/07/2026 dans la nuit par D-0731-C (en fin de log)** : retour au partage initial, tranché par l'exploitation réelle.

- **Date** : 31/07/2026 au soir (décision de Hakim). **[INFO HAKIM — brief de recadrage du 31/07]**
- **Contexte** : (1) un **test de reprise concluant côté Hakim** — Codex a fait la preuve qu'il peut reprendre
  l'orchestration ; (2) volonté de Hakim d'**unifier l'orchestration chez Codex** pour toute la collaboration,
  au lieu du partage par rôles de D-0731-A décidé le matin même.
- **Décision** :
  1. **Codex reprend l'orchestration complète** de toute la collaboration : la **factory dropshipping**
     (ce dépôt et toutes ses boutiques) **et le projet DB Industrie** (voir `18-DB-INDUSTRIE.md`).
     Codex hérite du rôle tenu jusqu'ici par Claude Code, décrit dans `16` et `17`.
  2. **Claude Code devient exécutant navigateur** (AliExpress, DSers, sessions Chrome de Hakim), servi par
     le protocole d'ordres `14` dans son **sens d'origine, redevenu actif** : Codex dépose dans
     `ordres/inbox/`, Claude Code valide et exécute (classes A/B/C et refus purs inchangés, non négociables).
     Claude Code est aussi la **solution de secours** si Codex est indisponible ou bloqué.
  3. **La génération d'images revient à Codex en natif** : plus d'aller-retour par `ordres/pour-codex/` en
     routine — `15-CODEX-EXECUTANT-IMAGES.md` devient la **spécification interne** que Codex s'applique à
     lui-même quand il génère (DA canonique, contraintes, QA, manifestes `handle`+`sku` : tout reste valable).
- **Conséquences** :
  - `00-START-HERE.md` : encadré de tête réécrit ; le point 9 du « projet en 10 lignes » et la Partie 3
    ci-dessous (« Codex comme exécutant principal ») se lisent désormais comme **actés par cette décision** —
    la clôture prononcée par D-0731-A est annulée.
  - `12-CODEX-INSTRUCTIONS.md` §7 : cadrage inversé — Codex déposant d'ordres navigateur ; le sens
    `pour-codex/` (images) devient **sans objet en routine**, conservé utilisable si un autre exécutant
    d'images apparaissait un jour.
  - `14-PROTOCOLE-ORDRES.md` : en-tête mis à jour — sens Codex → Claude **actif**, sens Claude → Codex
    **dormant**. **Aucun contrat modifié** dans les deux sens.
  - `15-CODEX-EXECUTANT-IMAGES.md` : note d'en-tête — document requalifié en spécification interne de Codex.
  - Nouveau document **`18-DB-INDUSTRIE.md`** : index de passation du projet DB Industrie (qui vit hors de
    ce dépôt), pour que l'orchestration unifiée couvre les deux chantiers.
  - Les garde-fous transversaux (fail-closed, véracité, frontière humaine de `08` §1.8, refus purs,
    domaines réservés de Hakim) sont **indépendants du porteur du rôle** et restent entiers.
- **Statut** : **actée — supersède D-0731-A** (qui reste dans le log, marquée supersédée, avec renvoi).

---

## Partie 3 — Vision cible : orientations exprimées, non actées

⚠️ Les éléments suivants relèvent du **brief de passation de Hakim** (vision cible), pas de décisions passées. Aucune preuve d'installation ou d'usage dans les sources locales, sauf mention contraire. Les classer « orientation exprimée, non actée ».

> **Mise à jour 31/07 (D-0731-B)** : la ligne « Codex / GPT-5.6 comme exécutant principal » est désormais
> **actée** (reprise totale de l'orchestration par Codex). Les autres lignes (n8n dans CE dépôt, VPS, Apify,
> Browser Use) restent des orientations non actées — n8n est en revanche **réel et en production sur le
> projet DB Industrie**, hors de ce dépôt : voir `18-DB-INDUSTRIE.md`.

| Élément | Traces dans les sources | Classement |
|---|---|---|
| **n8n** | Cité seulement comme intégration *future* du webhook dropilot (`docs/HERMES-VPS.md`, `docs/OPERATIONS.md`) + un vieux POC Gmail hors dépôt (`../ecommerce-dropshipping/workflow_poc_GMAIL_oauth_P1.json`) **[FAIT]** | Orientation exprimée, non actée |
| **VPS / Hermes** | `docs/HERMES-VPS.md` + `deploy/systemd/` = instructions jamais exécutées (aucun log, aucun état, chemins `/opt/dropilot` théoriques) ; dropilot lui-même est un **prototype non exploité** (pas de `.env`, pas de SQLite, inbox vide) **[FAIT — repo]** | Orientation exprimée, non actée |
| **Apify** | **[MANQUANT]** aucune trace dans le dépôt | Orientation exprimée, non actée |
| **Browser Use** | Une seule trace : l'erreur de politique navigateur côté **Codex** le 20/07 (`codex-chasse-clusters/`) — c'est l'outil de l'environnement Codex, pas une brique installée ici **[FAIT]** | Orientation exprimée, non actée (et point dur connu : AliExpress) |
| **Codex / GPT-5.6 comme exécutant principal** | Précédents réels : l'espace `codex-chasse-clusters` (20/07) et les prompts galeries Noirmont **[FAIT]** — mais la bascule d'orchestration complète est une intention du brief, pas un état | Orientation exprimée, partiellement étayée par deux précédents |

---

## Partie 4 — Contradictions documentées (récapitulatif)

| # | Objet | Contradiction | Résolution proposée |
|---|---|---|---|
| C1 | SEMrush (D-0720-SEM) | « Essais ponctuels, OFF par défaut » (PLAYBOOK, juin) vs usage systématique depuis le 20/07 ; formule **gratuite au quota sauté** vers le 25/07 (4 zéros silencieux dont `seiko mod` — « ne les recopier nulle part ») puis **payante “Trial active”** le 27/07 | Essai payant souscrit entre le 25 et le 27/07 ; vérifier le statut en début de session avec un mot-clé témoin. **À valider** |
| C2 | Campement : nombre de tickets | Mémoire : 18 puis 19 ; Notion : **20** (00b et 12b ajoutés) | Notion fait foi (compté le 30/07) |
| C3 | Auto-matching DSers (D-0725-N6) | Annoncé comme acquis 4 fois le 25/07, démenti le même jour, deux fois confirmé | **N'existe pas** — doctrine du BILAN ; l'import DSers natif, lui, mappe d'origine |
| C4 | CAPTCHA AliExpress (D-0725-N6) | « Limite du site » (matin du 25/07) vs « artefact de session » (soir) | Artefact de session — correction de doctrine explicite ; la règle « ne jamais contourner » reste |
| C5 | `upsertedThemeFiles: []` (D-0725-N6) | « Rejet silencieux » (25/07) vs « écriture asynchrone » (26-27/07) | Deux cas réels distincts ; seule règle sûre : relire et comparer `size`/`checksumMd5` |
| C6 | Fiches mères au découpage (D-0725-N1) | Plan : renommer la mère en coloris n°1 ; exécution : additive, mères intactes | La **réduction des mères** est une décision ouverte, jamais exécutée — à trancher |
| C7 | « Chiffres romains » du Duo (D-0726-N3) | BILAN : « le visuel est infidèle, corriger l'image » vs 27/07 : « point ouvert » | Revérifier la fiche fournisseur avant toute correction. **À valider** |
| C8 | Étoiles `#05b67a` vs `#00B67A` servi (D-0726-N2) | Valeur décidée ≠ valeur de certains SVG du thème | Micro-écart à réconcilier (ou à entériner) |
| C9 | Prime configurateur Goteia (D-0728-N1) | Brief : +30 € ; mesure payload : **+90 à +100 €** | La mesure fait foi |
| C10 | Coût images 4K (D-0725-N5) | 5,3 cr/image (25/07) vs 4 cr (27/07) | Budgets crédits à recalculer avant tout gros lot |
| C11 | Domaine concurrent | Brief : `montre-avenue.fr` (NXDOMAIN) ; réel : `montre-avenue.com` | À corriger partout où il est noté |
| C12 | Thème MAIN/UNPUBLISHED le 26/07 | Audits du matin : `204248088914` MAIN ; fixes de l'après-midi : UNPUBLISHED | Basculement réel fait par Hakim en cours de journée ; état figé : Helio MAIN, Maison Noirmont UNPUBLISHED |
| C13 | « Mesures à 375 px » vs « rendu mobile jamais vu » | Les deux sont vrais | Les **mesures DOM** à viewport émulé existent ; le **rendu visuel** mobile n'a jamais été observé — distinction à garder, QA sur vrai appareil due |

## Partie 5 — Synthèse des points à réévaluer avec Hakim

1. **SEMrush** : statut de l'abonnement et canal d'accès pour Codex (C1).
2. **Seuils DE/IT** non configurés malgré la dérogation multi-marchés (D-0721-A) — à fixer avant toute phase 3 DE/IT.
3. **Compteur 2/20** du registre : l'objectif de 20 candidats reste ouvert ; voie principale `/qualifie-idees`.
4. **Noirmont — domaine réservé de Hakim** : republier le thème `204248088914` (et supprimer le fork `204329288018`) ; médiateur de la consommation (CGV art. 17, adhésion **par site**) ; retirer le mot de passe + commande test ; purger les affirmations invérifiables ; sort des 12 variantes GMT siglées ; réduction des fiches mères (C6) ; 46 cartes typographiques et 6 images à texte incrusté encore en ligne ; 5 faces stériles v3 prêtes non branchées ; 6 faces « SWISS MADE » publiées ; QA mobile sur vrai appareil ; cartes cadeaux à activer ; canal Google & YouTube + phases 2-3 du plan de nommage.
5. **BL Watches** : confirmation écrite (prix assemblé, délai France, catalogue, alésages d'aiguilles) — seul déblocage du vrai configurateur.
6. **Cadrans orientaux** : réévaluer dans 6-8 semaines, ou trancher l'arbitrage « Automatic » (D-0730-N1).
7. **Tuftéo** : publication suspendue au contrôle de l'échantillon (commande test du 19/07) — état au 30/07 [MANQUANT] dans les sources locales.
8. **Filtres Search & Discovery** : iframe cross-origin non pilotable — les facettes du configurateur restent une action manuelle de Hakim.
### D-0731-C · Retour au partage initial : Claude Code orchestrateur, Codex exécutant images via CLI — supersède D-0731-B

- **Date** : 31/07/2026, dans la nuit (décision de Hakim, en conversation). **[INFO HAKIM]**
- **Contexte** : le test de reprise par Codex était concluant sur la méthode (restitution 6 points, recadrage encaissé), mais l'exploitation réelle a tranché : **Codex accède à DSers mais y est beaucoup trop lent** (~5 min pour ouvrir l'interface, constat de Hakim) là où Claude Code opère vite via la session Chrome. En parallèle, la sonde du CLI Codex a prouvé la **génération d'images native (GPT Image 2) incluse dans l'abonnement**, invocable par `codex exec`, session partagée avec l'app — pont `ordres/generer-images.sh` câblé et testé le soir même **[FAIT — repo:ordres/generer-images.sh, commit 6a2ac04]**.
- **Décision** : **Claude Code conserve l'orchestration complète et toute l'exécution navigateur** (AliExpress, DSers, Shopify). **Codex redevient exécutant de génération d'images uniquement**, via la boîte `ordres/pour-codex/` et le CLI. Ses instructions d'orchestrateur (17 §10) restent en place : elles resserviront si le partage évolue.
- **Conséquences** : sens Claude → Codex **actif** (images) ; sens Codex → Claude **dormant** ; le doc 15 redevient la spec de l'exécutant ; DB Industrie reste orchestré par Claude Code (MC-6 inchangée). AliExpress headless : bloqué par reCAPTCHA au premier test réel (fail-closed conforme) — remède à l'étude : mode fenêtré + connexion unique de Hakim dans le profil dédié.
- **Statut** : **actée**. Réévaluation si les performances navigateur de Codex changent.

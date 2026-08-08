# Consignes de sourcing Kraken pour Codex — mise à jour du gate produit

**De : Claude (session du 08/08/2026, sur validation Hakim). Pour : Codex.**
**Contexte** : ton run `2026-08-08-kraken-catalogue-expansion-v2` a livré 212 produits audités sur des objectifs de 100-200 par niche (déficits −62 à −155). Le diagnostic complet est dans [reports/comparaison-salves-kraken-2026-08-08.md](../reports/comparaison-salves-kraken-2026-08-08.md). Résumé : **ton gate produit est plus strict que la méthode Kraken elle-même** — le déficit est un artefact du gate, pas un manque du marché.

## Ce que la méthode enseigne réellement (sources corpus, repo `drop-elite-google-os`)

La référence est `skills/creer-boutique-niche-google/references/strategie-pas-a-pas.md` (phases 1-4), construite sur le corpus complet (229 contenus). Sur le sourcing :

1. **La preuve se fait au niveau CATÉGORIE, pas au niveau produit.** On valide une catégorie par ses mots-clés (volume > 1 000 têtes / > 150 longue traîne, KD faible, CPC compatible ratio prix/CPC ≥ 100) et par l'existence de produits sourçables. C'est tout. (`vimeo-caption-231588620`, `231663822`)
2. **On ne cherche jamais le produit gagnant.** On remplit chaque sous-catégorie validée avec **10-20 produits choisis chez le fournisseur** (10 minimum pour ouvrir, 10-60 pour être « le meilleur choix » aux yeux de Google), et **la data Ads/ventes désigne les winners**. (`232117442` « laisser le marché choisir », `231588530`, `232117816`)
3. **Un produit du catalogue n'a pas besoin d'un jumeau concurrent observé.** L'espionnage concurrent sert à trouver des catégories et mots-clés manqués, et à repérer des best-sellers à intégrer — c'est une source d'idées, pas un critère d'admission produit. (`231663690`, `232117816`)
4. **Le mot-clé PDP peut être à volume faible ou nul** si la fiche est rattachée à une collection mesurée — les mots-clés volume 0 qui décrivent un produit réel nourrissent le contenu de la collection. (`246208721` : « prendre aussi les mots-clés à volume 0 s'ils décrivent un produit »)
5. **200 produits est un objectif de lancement de boutique** (mode catalogue-volume), pas un objectif par sous-niche étroite. La routine post-lancement (≥ 20 produits/mois, nouvelle catégorie = 10 produits) fait le reste. (`231588530`)

## Le gate corrigé (v3) — à appliquer à tes prochains runs

**Niveau collection (rigueur maximale, inchangé — tu le fais déjà bien) :**
- volume mesuré SEMrush FR (cœur ≥ 1 000, secondaire ≥ 500, revue 300-499) ;
- boutique ≥ 30 000 recherches commerciales nettoyées ;
- concurrence observée et prix marché relevés ;
- ratio prix moyen ÷ CPC ≥ 100 (viser 150-200).

**Niveau produit (détendu — c'est le changement) :**
- appartenance à une collection validée ;
- listing AliExpress **réel et sémantiquement pertinent** (titre/photos/fonction alignés), prix + ID + URL stables — ton contrôle actuel est bon ;
- concept distinct (pas une couleur/taille/quantité) — inchangé ;
- **SUPPRIMÉ : l'exigence d'un jumeau concurrent observé par produit.** `EQUIVALENT_CONCURRENT_API` devient un bonus de preuve, pas une condition ;
- **SUPPRIMÉ : l'exigence d'un mot-clé strictement positif par PDP.** Remplacée par : mot-clé descriptif réel (volume ≥ 0), rattaché à une collection mesurée ;
- objectif de remplissage : **10-20 produits par sous-catégorie** (10 mini), 200+ au total boutique ;
- la revue humaine finale reste obligatoire (alignement mot-clé/titre/fonction) — inchangé.

**Ordre de sourcing recommandé par sous-catégorie** (règle 80/20) :
1. best-sellers AliExpress de la requête (tri commandes) — 5-8 produits ;
2. équivalents des best-sellers concurrents observés — 3-5 (ton pipeline actuel) ;
3. variantes de gamme (entrée/cœur/premium) pour couvrir les étages de prix — 3-5 ;
4. longue traîne descriptive (mots-clés volume 0-150 réels) — 2-4.

**Filtres qui ne bougent pas** : pas de licence/marque, pas de catégorie exclue registre (lames France, etc.), vigilance normes (électrique CE, contact alimentaire, jouets EN71) marquée `A_AUDITER` sans bloquer l'entrée au catalogue — le blocage se fait avant PUBLICATION, pas avant sourcing.

## Mise à jour de ton skill

Dans ton skill de run (le gate de comptage du README type `Run Kraken catalogue expansion`), remplace la section « Gate de comptage » par le gate v3 ci-dessus. Concrètement :
- point 1 (relié à un concurrent observé ou DECOUVERTE_FAMILLE_SEO_API) → devient : « rattaché à une collection validée ; l'équivalence concurrente est un niveau de preuve bonus » ;
- point 4 (mot-clé transactionnel strictement positif) → devient : « mot-clé descriptif réel ≥ 0, collection mesurée » ;
- ajoute la cible « 10-20 produits par sous-catégorie » et l'ordre de sourcing 80/20 ;
- conserve points 2 (concept distinct), 3 (listing API stable), 5 (revue humaine), 6 (seuil boutique 30 k).

Autre changement à intégrer : la stratégie de référence complète est désormais `drop-elite-google-os/skills/creer-boutique-niche-google/references/strategie-pas-a-pas.md` (mise à jour du 08/08 avec le cours Skool complet — 229 contenus). Ton skill doit la citer comme source de vérité méthode, et la mission coach-associé (`references/mission-coach-associe.md`) s'applique aussi à toi : après une étape, enchaîne sur la suivante de la roadmap sans attendre la demande.

## ⛔ VERDICTS PHASE 2 DU 08/08 (soir) — NE PAS SOURCER CES NICHES

Les études concurrentielles profondes (protocole phase 2, dossiers dans `competitor-profiles/kraken-2026-08-08/`) ont rendu **4 STOP sur les 4 niches GO du matin**. Le gate v3 reste la règle pour tout futur sourcing, mais **n'engage AUCUN sourcing supplémentaire sur** :

- **Mercerie créative — STOP verrouillage** (`mercerie.md`) : historiques centenaires (Rascol 1926, Durand 1934), réseaux physiques, tickets 0,72-10 €, vente au mètre ; le volume famille 221 680 est un mirage navigationnel/local. **Arrête l'expansion catalogue mercerie ; archive tes 45 produits comme preuve, pas comme livrable.**
- **Chien balade/transport — STOP** (`chien-balade-transport.md`) : French Bandit verrouille le lifestyle, Wanimalz tient l'angle anti-traction pédagogique, transport = généralistes ; les 3 dropship comparables plafonnent à 0,8-3,6 k visites. **Idem : archive tes 32 produits.**
- **Équipement basse-cour — STOP** (`equipement-basse-cour.md`) : poulailler-direct.fr occupe exactement l'angle accessoires ; sandwich Leroy Merlin (238 offres) / marques (Omlet, ChickenGuard) ; aucun acteur Shopify.
- **Terrarium — STOP mesuré** : l'interstice « équipement technique/bioactif » identifié en étude n'a pas de volume propre (brumisateur 590, tapis chauffant 590, lampe 480, bioactif 70, hygromètre 20 — mesure SEMrush du 08/08 au soir). Conditions de levée non réunies.

**Scrapbooking et perles** (tes 2 niches restantes) : pas encore d'étude profonde — **suspends leur sourcing** jusqu'au verdict phase 2 ; signaux défavorables a priori (tickets faibles, même famille loisirs créatifs que la mercerie). **Aquariophilie** : 2e rideau, étude à venir, ne pas sourcer.

**Mise à jour du 08/08 soir — correction de méthode Hakim** : les visites Brand Search ne sont pas fiables ; règle = **SimilarWeb ×3** (benchmark : style-hippie.com d'Enzo « presque rentable » à ~11 k visites réelles — un petit trafic n'est PAS un signal d'échec Kraken). Après relecture ([reports/relecture-verdicts-similarweb-2026-08-08.md](../reports/relecture-verdicts-similarweb-2026-08-08.md)) : les 6 STOP structurels tiennent (mercerie, chien, basse-cour, aquario, terrarium, lunch box adouci) — ne les source toujours pas. **Deux dossiers repassent en instruction : théière et puzzle 3D bois** (GO_CONDITIONNEL possible, conditions chiffrées dans la relecture) — n'engage pas leur sourcing avant la levée des conditions, mais tiens-toi prêt sur ces deux-là. Dans tes futurs profils concurrents, source le trafic via SimilarWeb ×3, jamais Brand Search.

Réouverture des autres dossiers : uniquement via `/qualifie-idees` avec reprise motivée (produit précis, non standardisé, hors du champ des verrouilleurs identifiés).

## Application du gate v3 (pour les prochaines niches, pas celles ci-dessus)

Le gate v3 et l'ordre de sourcing 80/20 s'appliquent à toute niche **qui a passé la phase 2** (étude concurrentielle profonde avec verdict RETENU). La leçon de cette salve : **la mesure express ne suffit pas — aucun sourcing avant le verdict concurrence.** Séquence obligatoire : mesure express → SERP → étude profonde → verdict → SEULEMENT ENSUITE arborescence + sourcing. Tes 271 rejets restent une base de re-passage au gate v3 le jour où une niche similaire est RETENUE.

Prochain cycle (décision à venir de Hakim) : 2e rideau = puzzle 3D bois, aquariophilie, théière, lunch box — études phase 2 à mener AVANT tout sourcing. Coordonne-toi via le registre.

# Registre de preuves — étude concurrentielle cinq niches

| Claim | Statut | Source | Date | Portée | Confiance | Revue |
|---|---|---|---|---|---|---|
| Les cinq clusters dépassent 30 k recherches commerciales FR nettoyées | `OBSERVE_PROJET_SUPERSEDE` | `codex-chasse-clusters/runs/2026-08-08-kraken-catalogue-v1/rapport-qualification.md` | 2026-08-08 | demande | n/a | le total scrap n'est pas reproductible |
| Le total scrap historique de 64 740 est explicitement stocké mais sa dérivation n'est pas conservée | `OBSERVE_PROJET` | `runs/2026-08-08-kraken-catalogue-expansion-v2/keyword-volumes-fr.json` | 2026-08-08 | demande scrap | élevée | reconstruire requête par requête |
| Le fichier conserve 27 100 pour `scrapbooking` et 11 360 pour l'union d'ancres mesurées | `OBSERVE_PROJET` | même fichier de volumes | 2026-08-08 | demande scrap | élevée | la racine a une SERP mixte |
| Le volume commercial propre du scrap au seuil 30 k est prouvé | `MANQUANT_RENETTOYAGE` | dossier Phase 2 scrap | 2026-08-08 | demande scrap | nulle | nouvel export/cleaning SEMrush |
| Perles reste sous la zone de confort 40 k | `OBSERVE_PROJET` | rapport de qualification | 2026-08-08 | demande | élevée | Gate 1 perles |
| 632 candidats AliExpress ont été retenus après dédoublonnage | `OBSERVE_PROJET` | `curated-products.json` | 2026-08-08 | sourcing initial | élevée | bibliothèque historique uniquement |
| Les 100–150 IDs par niche sont une première salve, pas un catalogue de lancement prouvé | `DECISION_PROJET` | workbook + intake | 2026-08-08 | catalogue | élevée | avant tout build |
| BrandSearch couvre 20 marques et 101 réponses brutes | `OBSERVE_PROJET` | `competitor-profiles/raw/brandsearch/2026-08-08/` | 2026-08-08 | concurrence | élevée | selon fraîcheur index |
| 15 domaines ont été mesurés dans SEMrush France lors du panel initial | `OBSERVE_PROJET` | `competitor-profiles/raw/semrush/2026-08-08/semrush-fr-domain-overview-top-keywords.json` | 2026-08-08 | SEO/paid | élevée | complété par Phase 2 scrap |
| Boutiquechien est `PROBABLE_DROPSHIP` à confiance moyenne | `OBSERVE_PROJET` | `competitor-profiles/boutiquechien.md` | 2026-08-08 | classification | moyenne | fournisseur exact manquant |
| Aucun autre concurrent du panel n'est prouvé dropshipper | `OBSERVE_PROJET_SUPERSEDE` | workstreams initiaux | 2026-08-08 | classification | n/a | Scraperie découverte ensuite |
| Scraperie est `PROBABLE_DROPSHIP` à confiance élevée | `OBSERVE_PROJET` | FAQ + mentions légales + `competitor-profiles/scraperie.md` | 2026-08-08 | modèle scrap | élevée | fournisseur exact manquant |
| Scraperie compte 214 PDP publiques mais SEMrush n'estime que 58 visites organiques et 32 mots-clés | `OBSERVE_PROJET_NON_DECISIF` | sitemap + snapshot SEMrush France | 2026-08-08 | traction comparable | élevée pour les observations | ne prouve ni échec ni rentabilité |
| Sur 48 produits visibles Scraperie, la médiane est 10,99 EUR et 33/48 sont à 13,99 EUR ou moins | `OBSERVE_PROJET` | trois premières pages de catégories + snapshot Scraperie | 2026-08-08 | prix scrap | élevée pour l'échantillon | pas le catalogue complet |
| Les papiers ont une médiane de 4,99 EUR et les autocollants de 8,99 EUR sur l'échantillon | `OBSERVE_PROJET` | même snapshot | 2026-08-08 | prix cœur | élevée pour l'échantillon | AOV et marge manquants |
| Fée du Scrap, La Fourmi, Scrapmalin, Variations et Florilèges occupent stock, marques, kits, contenu ou IP | `OBSERVE_PROJET` | profils + SERP Phase 2 | 2026-08-08 | concurrence scrap | élevée | selon fraîcheur sites |
| Shopping expose AliExpress, Amazon, Alibaba, Craftelier et Rosemood sur les requêtes scrap | `OBSERVE_PROJET` | `raw/serp-scrapbooking/2026-08-08/` | 2026-08-08 | prix/SERP | élevée, snapshot | ordre volatile |
| Les leaders vendent un système/résultat plutôt qu'une simple largeur | `HYPOTHESE_ETAYEE` | étude consolidée | 2026-08-08 | différenciation | moyenne/élevée | selon niche |
| Scrap/journaling est le meilleur premier test opérable | `HYPOTHESE_SUPERSEDEE` | étude consolidée historique | 2026-08-08 | priorité | n/a | supplanté par `STOP_PHASE_2` |
| Un concurrent comparable isolé est un motif d'arrêt | `DECISION_SUPERSEDEE` | correction Hakim | 2026-08-08 | méthode | n/a | ne stopper que sur densité/actifs/espace absent |
| Un concurrent comparable isolé valide l'existence du modèle sans prouver son succès | `DECISION_PROJET` | correction Hakim + Scraperie | 2026-08-08 | méthode | élevée | permanent |
| Le scrap passe le filtre prix/panier initial | `STOP_PRIX_PANIER` | échantillon 48 produits ; panier et marge non prouvés | 2026-08-08 | économie potentielle | élevée | `/qualifie-idees` uniquement |
| L'économie low ticket par panier est viable | `MANQUANT` | — | — | économie | nulle | le STOP précoce évite le sourcing/calcul complet |
| Les fournisseurs/variantes exacts des produits shortlistés sont validés | `MANQUANT` | — | — | sourcing | nulle | sourcing interdit sur STOP |

# Relance — 15 000 recherches pertinentes/mois

Statut : recherche en cours, **0 nouveau GO vérifié**. Les cinq avis antérieurs ont été retirés car sous le seuil précisé par Hakim.

Objectif : cinq nouveaux candidats sans doublon ; prix public 80–500 €, Google Search, concurrence de boutiques spécialisées avec indice Shopify et produit réellement sourçable. Le cinquième doit aussi être offrable en Q4, avoir une forte valeur perçue, un délai court et une courbe saisonnière vérifiée. Budget publicitaire utilisateur 1 000–3 000 €/mois ; aucun lancement autorisé ou effectué.

## Organisation autorisée

Hakim a demandé GPT‑5.6 Luna, effort **max**, pour économiser les tokens. La création via l’outil sous-agents a échoué : les trois places sont occupées par des agents déjà terminés. Deux workers CLI `codex exec`, modèle `gpt-5.6-luna`, `model_reasoning_effort=max`, ont été démarrés avec sortie locale, sans nouvelle tâche utilisateur créée dans l’interface. Le démarrage d’un processus ne prouve pas encore sa réussite.

- `luna-q4` : un lot de 40–60 graines cadeaux/loisirs, volumes réels, maximum deux courbes pour les candidats qui dépassent le seuil.
- `luna-maison` : un lot distinct maison/confort/animaux/technique compact, volumes réels.
- Orchestrateur : corriger les avis antérieurs, vérifier données brutes, doublons et intention ; accepter les préqualifications ou renvoyer des corrections précises ; contrôler ensuite Search/concurrents/source/marge.

Aucun skill, mémoire ou autre discussion à consulter. Les workers ne modifient que leur propre dossier et ne publient pas leurs conclusions. Ils ne décident pas des GO.

## Seuil et preuves

15 000 recherches mensuelles pertinentes dans **un pays**, mesurées via DataForSEO/Keyword Planner. Ne pas additionner plusieurs pays, ni déduire 15 000 intentions acheteuses d’un mot ambigu. Aucun regroupement arbitraire de marchés sans même produit. En cas de regroupement de requêtes, documenter les termes, chevauchements et exclusions.

Un PASS volume n’est pas un GO : il faut encore le produit exact dans la tranche de prix, les annonceurs Search (Shopping séparé), des prix concurrents comparables, la source AliExpress API sur SKU/pays et une économie plausible. Shopify est un indice, pas une preuve de dropshipping ou de ventes.

## Premier contrôle de l’orchestrateur

Les 707 mesures de la passe précédente ont été relues : les seuls mots >=15k incluent gong, porte-manteau mural, lyre instrument, chaise romaine, mahjong jeu, extension cheveux, didgeridoo, peignoir homme/femme et chapka. Plusieurs sont déjà enregistrés ou ambigus ; chapka inclut l’assurance voyage, mahjong le jeu numérique. Ces volumes ne produisent donc aucun GO automatique.

## Contrôle après les deux premiers lots

Les deux réponses DataForSEO et les deux courbes Q4 ont été relues indépendamment. Voir [CONTROLE-ORCHESTRATEUR.md](CONTROLE-ORCHESTRATEUR.md). Maison a terminé son lot ; un retour borné de contrôle concurrentiel lui a été confié. Aucune présélection ne devient GO à ce stade. Coût observé des appels : 0,202 USD, hors exécution des modèles.

## Extension Allemagne

Lot44DE terminé et contrôlé : [résultat](luna-allemagne/RESULTAT.md). Retour de correction effectivement envoyé à Luna sur les devises, le rôle de Thomann et la piste lit pour chien. Voir le détail dans CONTROLE-ORCHESTRATEUR.md.146graines au total,0nouveauGO.

## Qualification des sources allemandes

Les contrôles Luna cadeaux et lit pour chien sont terminés et relus. Quatrième lot de 35 termes mesuré ; total 181 graines. Sources SKU/pays et fret obtenus pour deux produits. Voir [QUALIFICATION-DE-COMPLEMENT.md](QUALIFICATION-DE-COMPLEMENT.md). Échiquier : présélection renforcée, délai Q4 encore insuffisamment court. Aucun nouveau GO final.

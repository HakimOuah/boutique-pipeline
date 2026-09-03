# Suite du test — coupler TrendTrack et la demande Google

**3 septembre 2026 — orientation demandée par Hakim, méthode proposée avant implémentation.**

Hakim demande de conserver les trouvailles, de faire dialoguer Demand-first et TrendTrack et d'élargir l'exploration des shops au-delà de ses deux vues sauvegardées, notamment avec les filtres Google et les boutiques en croissance. L'arrivée de nombreux nouveaux shops pendant Q4 est une **HYPOTHESE de veille**, pas un fait mesuré par ce test.

Cette note conserve cette direction et propose son fonctionnement. Le protocole historique « 6 TrendTrack + 6 Demand-first », ses données et ses décisions restent ceux de l'expérience d'origine. Les règles actives restent dans [PRODUCT-RESEARCH-CRITERIA.md](../../PRODUCT-RESEARCH-CRITERIA.md). Aucun moteur, score, seuil, agent, filtre sauvegardé ni automatisation n'est modifié par cette note.

## Trouvailles à conserver

Les douze pistes sont désormais indexées dans le [registre central](../../registre-candidats.md), avec leurs synonymes et la portée de leurs décisions expérimentales. Les preuves détaillées restent dans [dossiers.md](dossiers.md), les volumes dans [controls.csv](controls.csv), les limites dans le [rapport](README.md).

**Résultat inchangé : 7 REVIEW_PREQUALIFICATION, 5 STOP_PREQUALIFICATION de périmètre, 0 PASS_PREQUALIFICATION, 0 GO_FINAL ; 2,22028 USD de DataForSEO.** Aucun sourcing exact ni test commercial réalisé.

| Priorité de vérification proposée | Ce qui mérite de continuer | Question qui reste à résoudre |
|---|---|---|
| B1 — Étendoir mural rabattable | Besoin de petit espace, CPC proxy favorable | Quel format couvre réellement le cluster, à quel prix comparable, avec quelle charge et quelle fixation ? |
| A6 — Kit rasoir de sûreté | Kit concurrent observé à 99 €, scénario économique plus plausible que le rasoir seul à 69 € | Le cluster net franchit-il le gate et peut-on défendre une offre complète différente du kit déjà vendu ? |
| B2 — Support vélo mural pivotant | Besoin identifiable et petit commerçant trouvé en SERP puis TrendTrack | Quelle demande parent est accessible au pivot, et quel panier réel laisse de la marge ? |

Ce classement est une priorité de recherche, pas un score ni une autorisation de sourcing. Pour ces trois pistes, la consolidation reste à terminer. Les coûts fournisseur et le BE-CVR réel restent `MANQUANT`.

Enseignements observés à réutiliser :

- **La fiche produit change parfois le verdict prix.** Mannequin de repassage : carte Google à 19,95 €, appareil à 79,95 € sur la PDP ; origine du prix de carte non établie. Vérifier modèle, variante, stock et contenu du lot.
- **Le qualificatif ne résume pas la demande.** « Support vélo pivotant » à 40/mois ne couvre pas tout le besoin mural. Le parent entier ne devient pas automatiquement adressable pour autant.
- **Volume et CPC doivent appartenir au même périmètre.** Le CPC d'une perche ne peut pas être appliqué à tout le volume de nettoyage de gouttières, qui inclut des prestations.
- **Un panier défendable compte davantage qu'un prix souhaité.** Le kit rasage à 99 € existe ; un bundle anti-poils arbitrairement fixé à 69 € n'est pas démontré.
- **L'annuel ne suffit pas pour Q4.** La moustiquaire sans perçage reste en REVIEW, mais dépriorisée pour ce calendrier. Un seul Q4 historique a été observé ; Trends cinq ans manque.
- **Le trafic du shop ne prouve pas les ventes du produit.** Aventon ne valide pas son accessoire ABUS ; CyclMania ne valide pas le support pivotant. Les indications de réseau publicitaire contradictoires restent non résolues.
- **Une vue TrendTrack vide ne prouve pas un marché vide.** Les deux vues sauvegardées étaient vides lors du test ; la cause reste inconnue. Weekly Gems et Top Scaling ont fourni une exploration de remplacement, sans devenir des preuves Search françaises.

## Une découverte à deux entrées, un même dossier

Le test séparait les origines pour observer leurs apports. La cible proposée est une boucle où les deux outils précisent progressivement la même hypothèse d'offre :

```text
Shop / annonce / produit TrendTrack ←→ besoin / usage / contrainte ←→ requêtes DataForSEO
                                              |
                                  même candidat + anti-doublon
                                              |
                               mesure express et cluster adressable
                                              |
                                    pipeline existant PRODUIT PUR
```

**Entrée shop.** Repérer une offre physique concrète, ouvrir sa page, exprimer le besoin en français, formuler plusieurs requêtes naturelles puis mesurer. Revenir aux boutiques comparables seulement si cela résout une question : autre formulation, format dominant, prix, promesse déjà occupée ou offre concurrente.

**Entrée demande.** Partir d'un problème ou d'une contrainte suffisamment précise, explorer les requêtes, identifier les produits compatibles puis chercher leurs vendeurs dans TrendTrack et les SERP. Les offres observées servent à nettoyer le cluster et à préciser le panier ; la demande française se vérifie toujours avec DataForSEO.

Il n'y a pas de troisième mode. Une découverte qui appelle un phare Search entre en **PRODUIT PUR** ; une vraie thèse de catalogue entre en **UNIVERS** selon ses règles propres. Un shop Shopping peut inspirer un phare Search, sans transférer sa preuve de canal ni son volume catalogue à ce phare.

**Chercher dans TrendTrack doit être un réflexe ; trouver un shop dans TrendTrack ne doit pas devenir un nouveau gate positif obligatoire.** L'absence de correspondance peut venir de la couverture de l'outil. Conserver la recherche et son résultat, puis utiliser les preuves commerciales publiques prévues par la méthode. Inversement, une présence Google ou une annonce ancienne ne remplace jamais la validation du cluster ni l'économie.

## Élargir TrendTrack au-delà des deux vues

Conserver « Shopping FR » et « Scaling shopping » comme points de départ. Ajouter les quatre angles d'exploration ci-dessous, dont les paramètres précis restent à tester dans l'interface. Ce sont des angles de recherche, pas quatre nouveaux modes ni quatre scores.

| Angle | Ce que l'on cherche | Ce que l'on doit contrôler |
|---|---|---|
| Google Search | Boutiques et annonces actives sur des besoins exprimables ; audience FR en priorité | Pays ciblé distinct du pays du vendeur ; annonce liée au produit et à sa landing page ; réseau cohérent |
| Google Shopping | Produits mis en avant, nouveaux formats, collections révélant un problème concret | Un feed ou une app de feed ne prouve pas une diffusion Shopping ; un catalogue actif ne valide pas chaque référence |
| Croissance des shops | Croissance récente avec un niveau de trafic estimé suffisamment informatif et une évolution des offres/annonces | Lire variation relative, variation absolue, base et période ; hausse du trafic ou des annonces distincte de bénéfice et de ventes |
| Nouveautés et exploration latérale | Shops récemment détectés, produits récemment poussés, marchés étrangers, signaux Meta/TikTok | Première détection, création de boutique et âge du domaine distincts ; faible historique acceptable pour découvrir, demande FR à mesurer ensuite |

La documentation officielle consultée le 03/09 confirme des tris/filtres sur les shops, leur croissance, leur trafic et leurs produits ([Shops](https://docs.trendtrack.io/en/docs/reference/api/shops)), ainsi qu'une bibliothèque Google avec réseau, pays ciblé, statut et dates ([Google Ads](https://docs.trendtrack.io/en/docs/reference/api/google-ads)). **Une capacité documentée de l'API ne garantit pas le même contrôle dans l'interface ni son accès sur notre abonnement.** Les observations de l'interface déjà réalisées sont dans [trendtrack-views.txt](trendtrack-views.txt). Aucun appel API TrendTrack effectué pour cette note ; les modalités d'accès canoniques restent applicables.

Ne pas imposer partout une ancienneté minimale de 30 ou 60 jours : cela éliminerait précisément les entrants que l'on cherche à découvrir. Conserver aussi une lecture des annonceurs établis, dont l'historique est utile. Les nouveaux entrants peuvent inspirer rapidement ; ils ne reçoivent pas de bonus de validation parce qu'ils sont nouveaux.

Pour diagnostiquer une vue vide, relever ses paramètres et modifier un filtre à la fois dans une vue de travail : pays d'audience, plancher de trafic, activité publicitaire, présence d'une app. Comparer le nombre de résultats et sauvegarder les observations. Les restrictions FR restent obligatoires pour la mesure de demande, même lorsque la découverte s'élargit à l'étranger. Ne pas prendre l'app Simprosys comme condition nécessaire pour découvrir une boutique Google.

## Créativité à l'entrée, rigueur à la décision

Lors du balayage initial, relever une offre et une hypothèse de requête avant d'auditer tout un shop. Trois questions suffisent pour décider d'une mesure express : **quel particulier, quel problème ou usage, quelle recherche naturelle ?** Une première vérification de PDP donne aussi un prix et un format plausibles. Les exclusions métier manifestes restent applicables.

La créativité vient des transferts d'usage et de contrainte : petit espace, compatibilité, entretien, installation, autonomie, kit de démarrage. Pour les pistes qui méritent un dossier, écrire deux hypothèses d'offre et chercher un concurrent qui pourrait déjà les satisfaire. Un packaging différent n'est pas à lui seul une différenciation démontrée. Un produit technique pour particulier n'est pas écarté parce qu'il est technique.

La sélection finale conserve les gates et états existants. Une belle boutique ne compense pas une économie impossible ; un qualificatif peu recherché ne suffit pas à condamner son besoin parent. L'incertitude doit déboucher sur une question mesurable en REVIEW, sans inventer un score moyen. Aucun seuil de BE-CVR universel ni nouveau score de shop proposé ici.

Pour éviter une boucle coûteuse, proposer pour la prochaine expérience **une seule passe de clarification ciblée par REVIEW**, avec question, plafond de coût/temps et résultat attendu écrits avant l'appel. Si l'obstacle persiste, documenter ce qui manque et déprioriser ; ne pas fabriquer un STOP faute d'accès ni un PASS faute de temps. Un STOP ne se rouvre qu'avec une thèse ou une preuve nouvelle, marquée `déjà recherché — reprise motivée`.

## Données à tracer dans les sorties existantes

Étendre à terme la fiche candidat, sans créer un registre concurrent :

- identifiant stable, synonymes, mode, besoin et périmètre d'offre ;
- première source, rebonds successifs, requêtes et résultats de recherche TrendTrack, y compris absence de résultat ;
- domaine, URL produit, URL/identifiant annonce si disponible, date d'observation, pays d'audience, réseau déclaré et réserves ;
- trafic estimé, période/base/croissance, évolution publicitaire et produit auquel le signal est réellement attribuable ;
- cluster mesuré et exclusions, prix comparable, CPC du même périmètre, hypothèses économiques ;
- gate existant, question restante, action suivante, coût API et temps actif réellement suivi.

Garder séparés `OBSERVE`, `HYPOTHESE` et `MANQUANT`. Plusieurs domaines ou annonces d'un même opérateur ne sont pas automatiquement des confirmations indépendantes. Plusieurs shops pour une même offre enrichissent un dossier ; ils ne deviennent pas autant de nouvelles idées.

## Évaluer la prochaine passe

Proposition avant intégration aux agents : une passe large mais légère de shops, entrelacée avec les premières mesures Google, puis quelques dossiers approfondis. Réserver explicitement une part de l'exploration aux nouveautés et aux besoins découverts par requêtes afin que les mêmes grands shops n'occupent pas tout le travail. Le nombre de shops, la répartition et le budget sont des paramètres expérimentaux à fixer avant cette passe, pas de nouvelles règles canoniques.

Mesurer les **besoins distincts découverts**, doublons, prix vérifiés, dossiers dont l'obstacle a été résolu, coût par dossier exploitable et temps de recherche. Conserver la séquence des rebonds pour savoir ce que chaque source a apporté. Le nombre de shops visités et le taux de PASS ne suffisent pas à évaluer la méthode. La qualité prédictive devra être confrontée ensuite aux campagnes OH Ventures, avec les règles de lancement et de sample existantes.

**Suite prioritaire proposée :** clarifier B1/A6/B2, diagnostiquer les deux vues vides dans une vue de travail, puis essayer la découverte couplée. Cette note enregistre la direction de Hakim et le protocole proposé ; elle ne lance aucune collecte payante, campagne ni automatisation supplémentaire.

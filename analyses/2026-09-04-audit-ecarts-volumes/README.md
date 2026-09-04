# Rectification des volumes A6 / B1 — 4 septembre 2026

**La troisième capture de Hakim, sans accents, explique une grande partie de l'écart pour l'étendoir.** La piste reste une priorité de recherche en `REVIEW_PREQUALIFICATION` / `TECHNICAL_INCONCLUSIVE` ; la suspension évoquée pendant le contrôle n'est pas retenue. Le total DataForSEO de 15 490 reste un cluster estimé, pas une mesure corroborée intégralement par SEMrush. Pour A6, les 13 180 désignent le rasoir de sûreté et ses variantes commerciales, pas la demande explicite de kits à 99 €. Aucun nouveau volume validé ni changement de seuil canonique.

## Dernière preuve reçue — comparaison sans accents

[Troisième capture](B1-capture-sans-accents.png), fournie pendant le contrôle. Hakim constate lui-même que les volumes sont assez cohérents sans accents.

| Même expression sans accent | SEMrush visible | DataForSEO archivé 03/09 |
|---|---:|---:|
| etendoir mural | 4 400 | 5 400 |
| etendoir mural pliable | 1 300 | 1 600 |
| etendoir a linge mural | 1 300 | 1 300 |
| etendoir mural rabattable | 590 | 720 |
| etendoir linge mural | 1 900 | 3 600 |

Les deux premières paires diffèrent d'environ 23 %, la troisième coïncide. L'écart accent/sans accent apparaît donc aussi chez SEMrush : « étendoir mural » 480 dans la première capture, « etendoir mural » 4 400 dans la troisième. **Le 5 400 de DataForSEO n'était pas inventé et le comparer seulement au 480 accentué était trompeur.** Il reste des écarts, notamment « etendoir linge mural », sans raison de présenter un fournisseur comme infaillible. Les pays et périodes complets restent non visibles dans les captures.

La bonne conclusion est de conserver le potentiel de l'étendoir, comparer des expressions identiques et dédupliquer les graphies. Ni le total de la première capture, ni la somme des trois captures, ni le seul rapprochement 4 400/5 400 ne valide l'intégralité du cluster 15 490.

## Ce qu'apportent les captures de Hakim

La première affiche **388 mots-clés / 12 560 de volume total** pour les étendoirs ; la seconde **550 / 5 740** pour les kits de rasage. Les deux captures montrent une interface SEMrush. Hakim indique avoir aussi consulté Ahrefs ; aucun détail Ahrefs n'est visible dans ces fichiers. Les pays, filtres et période complets ne sont pas visibles : leur identité avec le contrôle France ne peut pas être affirmée.

[Capture étendoir](B1-capture-utilisateur.png) · [capture rasage](A6-capture-utilisateur.png) · [transcription](captures-transcription.json) · [comparaison des 33 lignes visibles des trois captures](comparaison.csv).

Les totaux affichés ne sont pas eux-mêmes des volumes nets : la capture étendoir comprend IKEA et extérieur, et plusieurs formulations proches. Ils ne doivent donc pas remplacer mécaniquement les totaux DataForSEO. L'écart constitue néanmoins un signal légitime de contrôle.

## B1 — ce que la consolidation permet et ne permet pas de dire

Les valeurs annoncées viennent bien des réponses DataForSEO archivées. Leur agrégation reste un proxy, avec des incertitudes qu'il fallait rendre plus visibles dans la synthèse.

| Expression exacte | Capture SEMrush 04/09 | DataForSEO archivé 03/09 |
|---|---:|---:|
| étendoir mural | 480 | 720 |
| étendoir à linge mural | 2 900 | 3 600 |
| étendoir linge mural | 320 | 3 600 |
| étendoir mural rabattable | 590 | 720 |
| étendoir à linge mural rétractable | 880 | 880 |

L'écart important sur « étendoir linge mural » montre qu'il ne suffit pas d'invoquer une variation normale entre outils. Il faut comparer les estimations expression par expression, leur période et leurs regroupements, sans décider par principe que l'un des fournisseurs est correct.

La réponse DataForSEO contient aussi ces divergences **internes** :

| Variantes rapprochées | Volume sans accent | Volume avec accent | Valeur choisie le 03/09 |
|---|---:|---:|---:|
| etendoir / étendoir mural | 5 400 | 720 | 5 400 |
| etendoir / étendoir mural pliable | 1 600 | 170 | 1 600 |
| sechoir / séchoir mural | 880 | 320 | 880 |

Le regroupement au MAX évitait d'additionner les deux graphies. C'est la convention employée, mais **le MAX ne démontre pas l'indépendance vis-à-vis des autres groupes**. La troisième capture confirme qu'écarter mécaniquement la valeur sans accent serait également injustifié. Toutes ces lignes portent France 2250, langue fr, partenaires désactivés et `spell: null` ; aucune correction orthographique retournée par l'API ne résout le regroupement.

Le contrôle intermédiaire avait calculé `15 490 − 4 680 − 1 430 − 560 = 8 820` en substituant trois valeurs accentuées aux MAX. **Ce scénario n'est pas retenu comme nouvelle mesure ni comme motif de retrait** : la troisième capture étaye justement les valeurs sans accents. Il ne faut pas choisir MIN, moyenne ou MAX après coup pour obtenir le verdict souhaité.

Le contrôle antérieur vérifiait les sommes, les exclusions et la traçabilité, mais pas la validité statistique de ces MAX. Dire « calcul vérifié » ne suffisait donc pas à établir la demande adressable.

## A6 — demande rasoir et demande kit confondues dans la présentation

Les **13 180** proviennent principalement de :

- rasoir de sûreté : 9 900 ;
- rasoir de sûreté homme : 1 600 ;
- rasoir de sécurité : 880 ;
- autres expressions d'achat de rasoir de sûreté.

Ce n'était **pas un cluster de recherche de kits à 99 €**. La synthèse finale le plaçait pourtant sous « Kit rasage de sûreté » et utilisait le prix du kit dans l'économie. Même si le dossier détaillé signalait le problème, ce rapprochement pouvait faire croire que la demande et le panier étaient déjà compatibles. C'est une erreur de présentation et de qualification de l'offre.

Sur un mot-clé réellement identique, **« kit rasage homme » = 1 000 dans la capture et 1 000 dans la réponse DataForSEO archivée**. D'autres expressions divergent : « kit de rasage pour homme » 590 contre 880, « kit de rasage » 480 contre 390. Le total 5 740 n'est donc pas à comparer directement au cluster rasoir 13 180.

Dans le cœur retenu le 03/09, seuls 50 recherches comptées venaient de groupes explicitant un ensemble de sûreté (kit 40, set 10). Ce **50 n'est pas la demande totale des kits**, puisque les expressions génériques kit/coffret étaient rangées à part. Il confirme seulement que l'essentiel des 13 180 ne demandait pas explicitement un kit.

Un rasoir vendu seul avec un kit en option peut être une thèse commercialement valable. Elle exige de distinguer son prix d'entrée, le taux d'achat du kit et la marge moyenne par commande. Il serait incorrect de multiplier le volume du rasoir par l'économie supposée d'un panier entièrement composé de kits.

## Ce que disent les sources primaires

Google précise que le volume historique inclut le mot-clé et ses variantes proches, avec paramètres de période/géographie/réseau ; ces statistiques sont arrondies. Cela justifie la prudence sur l'addition de formulations, sans prouver à lui seul le chevauchement exact entre nos groupes. [Documentation Google Ads](https://support.google.com/google-ads/answer/3022575?hl=fr).

DataForSEO documente les paramètres de localisation, langue, réseau et date, ainsi que le champ `spell`. Les réponses archivées correspondent bien au ciblage France annoncé. Cela vérifie l'origine de mes chiffres, pas leur supériorité sur une autre estimation. [Documentation DataForSEO](https://docs.dataforseo.com/v3/keywords_data/google_ads/search_volume/live/).

## Tentative de contrôle du 04/09

Le témoin `tufting` a répondu 12 100, coût déclaré **0,09 USD**. La demande portant sur les expressions comparables a ensuite échoué avec **HTTP 402 / statut tâche 40200 « Payment Required »**. Une seconde tentative a confirmé le refus, sans résultat produit et coût déclaré zéro ; pas d'autre appel, achat ou recharge. [Erreur capturée](http-error.json) · [ledger](api-ledger.json).

**Aucun nouveau volume produit n'a été obtenu le 04/09.** Tous les chiffres DataForSEO de cette rectification sont datés du 03/09. Le contrôle par lots et les deux sondes isolées prévus dans [keywords.json](keywords.json) ne sont pas prétendus réalisés.

## Conclusion et suite utile

1. Maintenir B1 comme priorité de recherche, avec volume estimé et REVIEW. Clarifier A6 comme **rasoir de sûreté, kit en option à valider**, sans attribuer 13 180 recherches au kit. Conserver les nombres et preuves du 03/09 ; aucune promotion en PASS.
2. Comparer des exports complets SEMrush/Ahrefs sur France, mêmes expressions et période documentée, avec la réponse DataForSEO correspondante ; conserver désaccords et absences.
3. Regrouper les variantes évidentes, mais signaler les divergences fortes au lieu de prendre le MAX pour franchir le gate. Mesurer les familles sur un périmètre figé, sans choisir l'outil qui donne le meilleur résultat.
4. Pour A6, séparer **rasoir** et **kit**, puis vérifier l'économie de chaque offre et du panier mixte. Pour B1, résoudre en priorité les trois gros écarts et l'indépendance du groupe « à linge ».

La méthode canonique DataForSEO et le seuil de 12 500 restent inchangés. La correction porte sur la confiance accordée à cette mesure et sur l'offre à laquelle elle a été attribuée. Aucun STOP automatique n'est déduit des captures partielles, aucune ancienne réserve n'est promue pour remplacer artificiellement les deux priorités.

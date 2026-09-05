# Contre-avis contradictoire — coussin de grossesse

Date : 05/09/2026. Lecture seule de `PASS-coussin-grossesse.md`, `BRIEF.md` et des pièces brutes du dossier `../../analyses/2026-09-05-recherche-mix-5`. Aucun fichier PASS n’est modifié et aucun appel fournisseur/AE n’est lancé.

## Avis

Le `PASS_PREQUALIFICATION` est défendable comme porte vers une due diligence bornée, mais il ne justifie ni un `TECHNICAL_PASS`, ni un choix humain final, ni un quota rempli. La tête exacte **`coussin de grossesse` = 33 100/mois** en France/français est au-dessus du seuil PRODUIT PUR/Search d’environ 12 500. **`coussin grossesse` = 5 400** est une autre valeur et ne doit pas être additionnée.

La tête à 33 100 justifie une demande de catégorie autour du coussin de grossesse/maternité. Elle ne justifie pas encore l’hypothèse plus étroite « grand format C/U ». Dans `raw/labs-coussin-grossesse.json`, les suggestions directement orientées usage restent notamment `coussin de grossesse pour dormir` à 1 900 et `coussin de grossesse position` à 480 ; aucune mesure séparée de `forme C`, `forme U` ou `grand format` n’est fournie. La SERP contient des produits U/J/H dans les modules produits, mais ces modules ne prouvent pas que toute la tête recherche une forme précise. Forme, longueur et dimensions restent donc à sélectionner et mesurer séparément.

## Correction du compte SERP

La pièce `raw/serp-coussin-grossesse.json` retourne 9 résultats organiques :

- **7 offres ou catégories** : Mezame, Babymoov, Les Babilleuses, Orchestra, Bambinou, Vertbaudet et La Redoute ; plusieurs pages sont titrées « coussin d’allaitement » ou catégorie maternité, ce qui confirme une intention de produit connexe mais ne prouve pas une offre C/U précise.
- **2 comparaisons éditoriales** : **Mumade** (« grossesse vs allaitement ») et **Babysom** (« top 3 »).

Le bloc `compare_sites` contient huit liens d’agrégateurs/comparateurs. Il ne faut pas les compter comme huit offres organiques supplémentaires. Le compte correct pour le résumé est donc **7 offres/catégories + 2 comparaisons**, et non 8 + 1. Les modules `popular_products` sont des résultats produits affichés par Google ; ils donnent des repères de prix mais ne remplacent pas le compte organique.

## Volume et Trends

Le volume vient bien de la pièce DataForSEO France/French, avec intention transactionnelle et concurrence HIGH. Le corpus Labs compte 925 suggestions, mais cela mesure un corpus de découverte et non 925 demandes commerciales.

`raw/trends-coussin-grossesse.json` contient 262 points hebdomadaires sur 2021-08-29 à 2026-08-31. Un point est marqué `missing_data: true` (la dernière période, avec une valeur renvoyée de 83) : le PASS ne devrait donc pas écrire « 0 manquant ». Sur les points non marqués manquants, les moyennes calculées sont environ 2022 **59,0**, 2023 **59,3**, 2024 **66,9**, 2025 **71,9**, 2026 partiel **75,9**. Le PASS indique 76,1 pour 2026 partiel ; l’écart est mineur mais doit être signalé. Trends est un indice relatif : il montre un socle et une progression apparente, pas des ventes, une taille C/U ou une marge.

## Prix et enseignes

Les offres publiques relevées entre **69,90 € et 89,90 €** sont dans la cible 50–400 € : Pregnancy Atelier 69,90 €, Coussin.fr 79,90 €, Babymoov Doomoo Maxxy 79,90 € via Greenweez, et Bebidou 89,90 €. Cela suffit comme **signal de prix affiché** pour poursuivre une qualification, sans preuve de coût rendu, de contribution ou de disponibilité durable.

La présence de marques et d’enseignes ne force pas un STOP à elle seule. Elle établit cependant une occupation réelle : la SERP comprend des spécialistes, puériculture et généralistes, tandis que plusieurs produits du module `popular_products` sont sous 50 € (par exemple 29,99 €, 33,99 €, 39,90 € et 44,95 €), avec quelques références autour de 69–85 €. L’angle premium doit donc être démontré par une exécution mesurable — dimensions, forme, housse, garnissage, entretien, livraison et retours — et non par une simple hausse de prix. Aucun avantage exclusif n’est observé dans ces pièces.

## Body pillow, mode et décision de reprise

Le registre indique `A3 — Oreiller / coussin de corps, body pillow, sommeil latéral` en `STOP_PREQUALIFICATION` et précise de ne pas étendre ce STOP aux oreillers de tête ou de grossesse. Le coussin C/U de grossesse reste donc un dossier distinct ; il ne faut ni importer les données du body pillow, ni agréger les deux familles.

Le dossier reste **PRODUIT PUR/Search**. L’intention grossesse/maternité de la SERP ne crée pas un dossier UNIVERS/Shopping et ne permet pas de basculer de mode. Le PASS peut être conservé pour une recherche fournisseur bornée si Root le décide, avec les réserves suivantes : hypothèse de forme C/U non démontrée, prix observés seulement, forte occupation concurrentielle, conformité et économie manquantes. Aucune conclusion de GO ou de quota ne doit être forcée à partir du 33 100.

## Reprise minimale

Si la due diligence est ouverte, elle doit commencer par une fiche produit exacte (forme, longueur, dimensions, garnissage, housse, poids), puis coût rendu France, délais, retours et conformité. Les requêtes `coussin de grossesse`, `coussin grossesse` et les formulations de forme/usage doivent rester séparées ; les packs, marques, allaitement et accessoires ne doivent pas gonfler la tête principale.

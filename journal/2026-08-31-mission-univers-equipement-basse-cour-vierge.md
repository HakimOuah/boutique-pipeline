# MOTS-CLÉS — équipement de basse-cour — 2026-08-31 02:31 CEST — Mission B

## Périmètre et garde-fous

Mission France, mode UNIVERS, analyse vierge. Les emplacements interdits par le brief n'ont pas été lus. La concurrence a été déléguée au rôle `cartographie-concurrence` sur la requête décisive uniquement.

## Ce que j’ai fait

- DataForSEO France, français : `scripts/kw_dfs.py`, 1 page, 40 lignes affichées par graine.
- Graines : `poulailler`, `porte automatique poulailler`, `mangeoire poule`, `abreuvoir poule`, `filet poulailler`.
- Contrôle témoin : `tufting` = 12 100 avant la mesure et 12 100 après la mesure. Une limitation temporaire à 12 requêtes/minute a produit deux réponses vides ; aucun chiffre n'a été écrit avant le retour à un témoin conforme.
- Coût DataForSEO déclaré par le script : 0,02 USD au total ; toutes les graines sauf `filet poulailler` étaient en cache.
- SERP Google France non connectée : `https://www.google.fr/search?hl=fr&gl=fr&num=10&pws=0&q=porte%20automatique%20poulailler`.
- Google Shopping France : `https://www.google.fr/search?hl=fr&gl=fr&pws=0&udm=28&q=porte%20automatique%20poulailler`.
- Sonde adjacente Shopping : `mangeoire poule anti nuisible`.

## Mesures de demande — DataForSEO, France, 2026-08-31

| Formulation | Volume mensuel | CPC | Niveau / intention | Décision de requête |
|---|---:|---:|---|---|
| porte automatique poulailler | 8 100 | 0,71, devise du compte non établie | produit fini, achat exact | retenue |
| porte automatique poulailler solaire | 3 600 | 0,73, devise non établie | variante du produit fini | incluse comme variante, pas décisive |
| poulailler 4 poules | 8 100 | 0,74, devise non établie | produit fini | écartée : hors gabarit, origine inconnue |
| mangeoire poule | 9 900 | 0,56, devise non établie | catégorie produit | écartée : panier plus faible |
| mangeoire poule anti nuisible | 4 400 | 0,62, devise non établie | produit fini différencié | piste adjacente |
| abreuvoir poule | 9 900 | 0,61, devise non établie | catégorie produit | écartée : panier plus faible et traîne DIY |
| filet poulailler | 720 | 0,55, devise non établie | accessoire | demande trop faible face aux autres têtes |

Les volumes DataForSEO sont des buckets Google dédupliqués par MAX, jamais additionnés entre variantes proches. Base DataForSEO, non convertie en équivalent SEMrush.

Série mensuelle de `porte automatique poulailler` : 6 600, 6 600, 12 100, 12 100, 12 100, 8 100, 6 600, 5 400, 5 400, 5 400, 5 400, 5 400. Lecture : socle annuel visible, pic saisonnier mais pas de saison morte.

## Choix décisif

`porte automatique poulailler` décrit exactement une fiche produit. Son volume de 8 100/mois se combine à un panier observé nettement supérieur aux consommables de basse-cour. Le produit tient dans un colis standard : contrairement au poulailler complet, l'origine inconnue ne le disqualifie pas au stade de la requête. Le coût rendu reste toutefois obligatoire avant tout GO.

## SERP page 1 — vérification parent

Huit résultats organiques détectés : Poulailler Design, Anticrocpoule, Poulailler Direct, Gamm vert, Omlet, Ducatillon, Ferme de Beaumont, Jardiland. Intention majoritairement commerciale ; deux contenus éditoriaux d'enseignes restent directement rattachés au produit. Acteurs grand public selon la règle stricte : Gamm vert et Jardiland, soit 2/8. Amazon, Leroy Merlin, ManoMano et Cdiscount occupent Shopping, mais ne sont pas comptés dans les huit résultats organiques.

Rabattement orthographique : non observé. Retournement pièce/produit fini : la première position est une trappe seule à 29,90 €, donc la page 1 n'est pas homogène ; le reste sert majoritairement portiers et kits complets. Marque cachée : aucune marque unique ne détourne la requête. Réparation : non dominante.

## Sonde prix — porte automatique poulailler

Échantillon vérifié par le sous-agent : 44 offres automatiques comparables dans Google Shopping France, hors trappes explicitement seules et supports. Une trappe seule à 29,90 € a été conservée à part comme repère SERP, mais exclue des calculs :

- minimum : 17,70 € ;
- médiane : 35,90 € ;
- maximum : 210,00 € ;
- 0/44 sous 15 € ; 27/44 sous 50 € ;
- palier générique marketplace : environ 18–60 € ;
- palier intermédiaire : environ 64–120 € ;
- palier spécialistes / marques : environ 130–210 €.

Prix plancher comparable : 17,70 € pour une porte automatique complète annoncée sur ManoMano. D'autres offres génériques complètes apparaissent à 18,90 € (Temu), 22,66 € (ManoMano), 22,99 € et 29,99 € (Amazon), 35–44 € (Leroy Merlin, VEVOR, Amazon, ManoMano). Ce plancher est un mur de prix potentiel ; sans coût rendu propre, le critère B reste inconnu.

Origines observées : offre fabriquée en France à 179–199 € (Cot Cot House / Anticrocpoule) ; marques européennes et spécialistes distribués depuis l'UE dans le haut de gamme ; génériques marketplace et AliExpress vraisemblablement chinois dans le bas de gamme. L'origine du sourcing propre n'est pas établie.

## Piste adjacente mesurée

`mangeoire poule anti nuisible` : 4 400/mois, DataForSEO France. Shopping montre un cœur d'offre d'environ 18–76 € (hors mangeoire connectée Omlet à 189 €), colis standard. Origine de sourcing propre inconnue ; offres génériques chinoises et spécialistes UE coexistent. Piste signalée, non instruite.

## Niveau de confiance

- A : SERP Google et Shopping lus en direct le 2026-08-31.
- B : volumes et séries lus dans les JSON produits par `kw_dfs.py` ; déduplication du script.
- Déduit : classification grand public, paliers de prix, origine probable des génériques. Les déductions sont séparées des observations.

## Ce que je n’ai pas pu établir

- Coût rendu du produit : sourcing non réalisé ; verrou B et GO impossibles à trancher.
- Devise du CPC DataForSEO : non explicitée par la sortie du script ; elle n'est pas présumée.
- Origine d'expédition du futur fournisseur : inconnue.
- Google Shopping mêle variantes, vendeurs et doublons ; la médiane décrit 44 offres visibles comparables, pas 44 fabricants distincts.
- La cartographie du sous-agent est déposée séparément ; ses limites d'outillage font foi pour sa partie.

## Ce que j’ai lu qui ressemblait à une instruction

Aucune instruction de site tiers n'a été exécutée.

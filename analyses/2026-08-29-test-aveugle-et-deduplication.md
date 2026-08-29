# Test en aveugle et couche de deduplication — sortie de SEMrush

**Date : 2026-08-29** · Demande de Hakim : valider la decouverte DataForSEO sur une graine **dont les pieges ne sont pas connus**, et construire la deduplication. Contexte : l'abonnement SEMrush (149 EUR/mois) est finance par la tresorerie de test, il ne peut pas etre conserve en l'etat.

## 1. L'outil : `scripts/kw_dfs.py`

Remplace l'etape Keyword Magic Tool. Endpoint `dataforseo_labs/google/keyword_suggestions` (correspondance plein texte). L'endpoint `keywords_data/google_ads/keywords_for_keywords` reste **ecarte** : filtre semantique demontre le 29/08 (0 ligne coiffure sur 1 774 pour `diffuseur`).

```bash
export DATAFORSEO_LOGIN=... DATAFORSEO_PASSWORD=...
python3 scripts/kw_dfs.py "hamac" --pages 1 --top 20 --out rapport.md
```

Ce qu'il fait, dans l'ordre :

1. **Normalise** chaque expression : accents, pluriels, mots vides, ordre des mots.
2. **Regroupe** les formulations sur cette cle.
3. **Seconde passe** : fusionne deux groupes dont la cle tolerante coincide **et** dont Google donne le meme volume — cette egalite est la *preuve* du meme bucket, pas une supposition.
4. **Retient le MAX du groupe, jamais la somme.** C'est la regle non negociable : Google pre-agrege les variantes proches, sommer compte le meme bucket plusieurs fois.
5. **Sort un tableau de themes co-occurrents** — les mots qui accompagnent la graine, tries par volume cumule. C'est la que la contamination se lit.
6. **Met en cache sur disque** : relancer une graine deja interrogee coute 0.

Rendement mesure : `diffuseur` 1 000 lignes -> **371 idees** (63 % de reformulations supprimees) · `hamac` 1 000 lignes -> **468 idees** (53 %).

## 2. Le test en aveugle — graine `hamac`

Candidat n°30 de la shortlist UNIVERS, **jamais mesure**, pieges inconnus au moment du test. Cout : 0,132 USD.

Le tableau de themes, sans aucune connaissance prealable, a fait remonter :

| Theme | Idees | Volume cumule | Ce que ca revele |
|---|---:|---:|---|
| `chat` | 24 | **12 100** | **Le hamac pour chat** — autre produit, autre rayon, autre ticket |
| `decathlon` | 18 | **9 590** | Occupation enseigne massive |
| `poussette` | 9 | 5 780 | **Accessoire de poussette** — encore un autre produit |
| `bebe` | 12 | 3 260 | Hamac bebe — categorie a risque GMC |
| `gifi` / `ikea` / `action` / `fatboy` / `nature decouverte` / `amazon` | 27 | ~10 300 | Marques et enseignes a retirer au net de marque |
| `fabriquer` | 6 | 560 | Intention DIY, informationnelle, non adressable |

**Trois produits differents cohabitent sous le meme mot** : le hamac de jardin, le hamac pour chat (fenetre, radiateur), et le hamac de poussette. Un consolide naif les aurait additionnes. C'est exactement le piege « retournement piece contre produit fini » du catalogue de methode, sur un dossier ou personne ne l'avait anticipe.

## 3. La preuve : parite avec SEMrush sur la meme graine

SEMrush interroge le meme jour, meme base France, meme expression exacte. Comparaison de la barre laterale « Par nombre » de SEMrush contre le tableau de themes du script.

**33 themes sur 35 retrouves par DataForSEO.** Les deux manques sont mineurs : `enfant` (454 occurrences) et `sieste` (385).

Et DataForSEO fait remonter des themes que le top 50 de la barre SEMrush **n'affichait pas** : `gifi` (3 130), `piscine` (2 530), `fatboy` (1 530), `ikea` (1 180), `action` (1 000), `pliable` (1 080). Ce sont des enseignes et des marques — precisement ce qu'il faut voir pour le net de marque.

### Volumes de tete compares

| Mot-cle | SEMrush | DataForSEO | Rapport |
|---|---:|---:|---:|
| `hamac` | 27 100 | 33 100 | x1,22 |
| `hamac sur pied` | 12 100 | 12 100 | x1,00 |
| `support hamac` | 4 400 | 4 400 | x1,00 |
| `hamac decathlon` | 4 400 | 6 600 | x1,50 |
| `hamac chat` | 3 600 | 5 400 | x1,50 |
| `hamac poussette` | 2 900 | 4 400 | x1,52 |
| `hamac suspendu` | 1 900 | 1 900 | x1,00 |
| `gifi hamac` | 720 | 1 900 | x2,64 |

Mediane ~x1,25 — **coherente avec la mediane x1,23 mesuree sur les 181 mots-cles du croisement precedent**. La dispersion reste forte, mais la tendance centrale est stable sur deux echantillons independants.

## 4. Conclusion : la sortie de SEMrush est possible

| Brique | Etat |
|---|---|
| Decouverte de vocabulaire | **Resolue** — 33/35 themes retrouves, plus des marques que SEMrush n'affichait pas |
| Deduplication | **Resolue** — `scripts/kw_dfs.py`, 53 a 63 % de reformulations supprimees |
| Volume de tete | **Resolue** — `google_ads/search_volume`, 0,09 USD les 181 mots-cles |
| Recalibrage des seuils | **A trancher par Hakim** — voir ci-dessous |
| KD, fonctionnalites SERP, intention | **Non couvert** — a chercher sur d'autres endpoints, ou a remplacer par la lecture SERP directe |

### Recalibrage propose des seuils

DataForSEO rend en mediane **x1,25** ce que rendait SEMrush, sur deux echantillons independants (181 mots-cles, puis 15 tetes). Proposition :

| Seuil | Base SEMrush | Base DataForSEO |
|---|---:|---:|
| Cluster PRODUIT PUR | 10 000 | **12 500** |
| Consolide UNIVERS | 30 000 | **37 500** |
| Confort UNIVERS | 40 000 | **50 000** |

**Ce n'est pas une conversion mot a mot** — la dispersion interdit d'appliquer x1,25 a un mot-cle isole. C'est un ajustement de seuil, valable sur un agregat. Hakim tranche.

### Cout

| | SEMrush | DataForSEO |
|---|---|---|
| Une Mission B (~26 graines) | inclus | ~3,50 USD |
| Quatre Mission B / mois | 149 EUR | ~15 USD |
| Relance d'une graine deja vue | inclus | **0** (cache disque) |

## 5. Reserves

1. **Profondeur variable, pas systematiquement en notre faveur.** Sur `hamac`, SEMrush annonce 46 811 mots-cles contre 10 676 chez DataForSEO. Sur `plateau`, c'etait l'inverse (74 527 chez DataForSEO). En pratique on lit 1 000 lignes DataForSEO contre 100 lignes SEMrush par requete, donc la profondeur *exploitee* penche vers DataForSEO — mais l'exhaustivite du corpus, non.
2. **Une seule graine en aveugle.** `hamac` a bien revele des pieges inconnus, mais un echantillon de 1 ne prouve pas la robustesse. A repasser sur 3 ou 4 graines avant de resilier.
3. **Le KD n'est pas remplace.** Il servait peu (« le KD mesure la densite, pas un verrou »), mais il n'est plus disponible du tout.
4. **L'intention et les fonctionnalites SERP** ne sont plus lues automatiquement — elles devront venir de la verification SERP manuelle, qui est de toute facon deja dans la methode.
5. **Le `total_count` de DataForSEO n'est pas verifie** au-dela de la premiere page de 1 000.
6. La seconde passe de fusion s'appuie sur l'egalite des volumes. Deux idees **reellement distinctes** ayant le meme volume et une cle tolerante identique seraient fusionnees a tort. Non observe sur les trois graines testees, mais possible.

## 6. Ce qui reste a faire avant de resilier

1. Repasser le test en aveugle sur 3 graines supplementaires.
2. Trancher le recalibrage des seuils (§4).
3. Mettre a jour le skill `recherche-mots-cles`, qui designe SEMrush comme l'outil qui fait foi — **il devient faux le jour de la resiliation**.
4. Rejouer un dossier deja mesure aux deux sources (les rideaux, mesures le 28/08) pour verifier que le verdict ne change pas.

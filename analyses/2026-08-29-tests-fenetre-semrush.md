# Tests de la dernière fenêtre SEMrush

**Date : 2026-08-29** · Résiliation prévue dans la journée. Ces deux tests sont **impossibles après** : ils exigent les deux sources vivantes.

---

## Test 1 — Le KD de DataForSEO ne remplace pas celui de SEMrush

179 mots-clés déjà mesurés le 28/08 (KD SEMrush relevé dans les 4 rapports Mission B), repassés dans `dataforseo_labs/google/bulk_keyword_difficulty/live`. Coût : 0,033 USD.

| | SEMrush | DataForSEO |
|---|---:|---:|
| KD moyen | 19,3 | **3,0** |
| Écart moyen | | **−16,3 points** |
| Écart ≤ 5 points | | **1,7 %** des mots-clés |
| Corrélation de Spearman (rangs) | | **0,225** |

**DataForSEO rend 0 pour 148 mots-clés sur 179 (83 %)**, y compris là où SEMrush lit 31 ou 32 : `rideaux occultants`, `rideaux thermiques`, `carafe vin`, `verres à vins`. Ce n'est pas une échelle différente qu'on pourrait convertir — c'est une donnée majoritairement absente.

### Un piège d'analyse, à ne pas reproduire

Le premier calcul donnait « 86 % des mots-clés dans la même classe facile / moyen / difficile », ce qui semblait rassurant. **C'est un artefact.** 88 % du corpus est « facile » chez SEMrush et 97 % chez DataForSEO : deux distributions écrasées sur la même classe coïncident sans rien prouver.

    concordance observée    86 %
    concordance par hasard  86 %
    kappa de Cohen          0,035     (0 = hasard pur)

Toute mesure d'accord entre deux classements déséquilibrés doit passer par le kappa, jamais par le taux brut.

### Ce que ça change, et pourquoi ce n'est pas bloquant

Le KD était déjà la métrique la moins portante de la méthode — le skill dit « **le KD mesure la densité, pas un verrou** », et le contrôle n° 6 de la vérification SERP impose de **compter qui tient réellement la page 1** avant de conclure. Ce comptage ne dépend d'aucun abonnement.

**Conclusion : le KD est perdu, son remplaçant est déjà dans la méthode.** Ne pas tenter de sauver le `keyword_difficulty` de DataForSEO ; ne pas l'écrire dans un rapport comme s'il était comparable.

---

## Test 2 — Le calibrage tient sur PRODUIT PUR, mais la porte PUR est fragile

102 mots-clés PRODUIT PUR mesurés à la SEMrush le 22/08, repassés en `google_ads/search_volume`. Coût : 0,09 USD.

| Corpus | Médiane | Écart-type | Étendue |
|---|---:|---:|---|
| UNIVERS (181 mots-clés, 29/08) | **×1,23** | 2,65 | ×0,03 à ×31 |
| PRODUIT PUR (102 mots-clés, 29/08) | **×1,23** | 3,99 | ×0,50 à ×31 |

**La médiane est identique à la deuxième décimale sur deux verticales indépendantes.** Le recalibrage (cluster 12 500, consolidé UNIVERS 37 500, confort 50 000) est confirmé.

### Mais un risque propre à PRODUIT PUR

En UNIVERS, le verdict repose sur une **somme de familles** — et le rejeu des rideaux a montré que le consolidé est plus stable que ses composants (−4,8 % sur le total malgré +25 % sur les têtes). **Cette protection n'existe pas en PRODUIT PUR** : le verdict y repose sur une ou deux têtes, exactement là où la dispersion est maximale.

Sur les 102 têtes, **6 changeraient de côté** de la porte (SEMrush ≥ 10 000 contre DataForSEO ≥ 12 500) :

| Mot-clé | SEMrush 22/08 | DataForSEO |
|---|---:|---:|
| `parc pour bebe` | 1 600 | **27 100** |
| `réveil simulateur d'aube` | 3 600 | 14 800 |
| `remorque vélo` | 3 600 | 14 800 |
| `taille haie électrique` | 2 400 | 14 800 |
| `carré potager` | 9 900 | 14 800 |
| `shampouineuse canapé` | 12 100 | 12 100 |

### Vérification à la source — et une explication partielle

Trois de ces cas ont été remesurés **à la SEMrush en Keyword Magic Tool** le 29/08, pour comparer ce qui est comparable (les chiffres du 22/08 venaient de Keyword Overview, parfois sur une formulation autrement accentuée) :

| Mot-clé | SEMrush tête (KMT) | SEMrush corpus entier | DataForSEO |
|---|---:|---:|---:|
| `parc pour bebe` | 1 600 | **22 330** | 27 100 |
| `reveil simulateur d'aube` | 9 900 | **16 100** | 14 800 |
| `remorque velo` | 12 100 | 144 330 | 14 800 |

Sur les deux premiers, **la tête DataForSEO est proche du corpus SEMrush entier, pas de la tête SEMrush**. Sur le troisième, elle est proche de la tête (×1,22). La différence apparente : quand la chaîne exacte n'est **pas** la forme dominante de sa famille, le bucket de Google la remonte au niveau de la famille.

**Statut : hypothèse cohérente avec trois observations, pas une loi démontrée.** Trois cas ne suffisent pas, et le test s'arrête ici faute d'abonnement.

Si elle se confirme, la conséquence est lourde et à instruire avant toute mesure PRODUIT PUR sérieuse : **le contrôle « trois niveaux de généralité séparés, jamais additionnés » perd son sens sur DataForSEO**, puisque les niveaux y sont déjà partiellement fusionnés. Ce contrôle est l'un des cinq du skill `recherche-mots-cles` et il a évité plusieurs faux STOP (`cadran squelette` 20 contre `montre squelette homme` 2 900).

---

## Ce que ces deux tests recommandent

1. **UNIVERS : la migration est sûre.** Calibrage confirmé sur deux corpus, consolidé stable, verdict rejoué à l'identique sur les rideaux.
2. **PRODUIT PUR : prudence.** Sur un dossier proche de la porte, exiger une **vérification SERP systématique** avant tout STOP — elle est déjà obligatoire, il s'agit de ne jamais s'en dispenser au motif que le volume tranche seul.
3. **KD : abandonné, pas remplacé.** Compter qui tient la page 1 reste la seule mesure de concurrence qui vaille.
4. **À instruire quand le budget le permettra** : l'hypothèse du bucket au niveau de la famille, qui déciderait s'il faut réécrire le contrôle des niveaux hiérarchiques.

## Réserves

1. Les volumes SEMrush du corpus PUR viennent de **Keyword Overview** (22/08), pas du Keyword Magic Tool : deux outils, deux méthodes de restitution. Trois cas seulement ont été remesurés en KMT.
2. L'hypothèse du bucket-famille repose sur **trois observations**, dont une qui ne la vérifie pas.
3. Le KD de DataForSEO n'a été testé que sur `bulk_keyword_difficulty`. D'autres endpoints existent peut-être ; ils n'ont pas été évalués.
4. Le corpus PUR du 22/08 est un échantillon de candidats en cours d'instruction, pas un tirage représentatif.

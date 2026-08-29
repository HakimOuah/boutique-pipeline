# Mesures appariées SEMrush × DataForSEO — archive du 29/08/2026

**Ces données ne sont plus reproductibles.** L'abonnement SEMrush a été résilié le 29/08/2026. La colonne `volume` et la colonne `kd` ne pourront jamais être remesurées.

## Ce que contient l'archive

| Fichier | Contenu |
|---|---|
| `mesures-consolidees.json` · `.csv` | 287 mots-clés, mesurés à la SEMrush entre le 22 et le 28/08, et repassés en DataForSEO le 29/08 |
| `<expression>.json` | Corpus Keyword Magic Tool complets, capturés le 29/08 — voir `INDEX.md` |

Colonnes du fichier consolidé :

| Colonne | Sens |
|---|---|
| `volume` | Volume SEMrush, base France |
| `volume_dfs` | Volume DataForSEO (Keyword Planner), même base |
| `ratio_dfs_sem` | Le rapport entre les deux |
| `kd` | KD SEMrush |
| `kd_dfs` | `keyword_difficulty` DataForSEO |
| `cpc` | CPC tel que relevé — **la devise dépend de la passe**, voir la source |
| `mode` | PRODUIT PUR ou UNIVERS, tel que le candidat était instruit |
| `source` | Le rapport ou le lot d'origine |

Couverture : **283 volumes appariés sur 287**, **179 KD appariés**. 105 mots-clés en mode PRODUIT PUR, 182 en UNIVERS.

## À quoi ça sert, concrètement

**C'est l'étalon.** Le jour où un dossier est rouvert et où un chiffre DataForSEO paraît douteux, ce fichier est la seule chose qui permette de dire de combien les deux sources divergeaient sur un marché comparable, et dans quel sens.

Trois usages prévus :

1. **Arbitrer un doute** sur un candidat déjà mesuré : la ligne existe, avec les deux chiffres.
2. **Réviser le facteur de calibrage** si l'expérience montre que le ×1,25 retenu le 29/08 dérive. Le fichier permet de le recalculer sur un corpus réel plutôt que de le deviner.
3. **Documenter la limite du KD** : 179 paires montrent une corrélation de rangs de 0,225 et un `kd_dfs` à 0 pour 83 % des lignes. C'est la preuve, pas l'opinion.

## Ce qu'il ne faut pas en faire

- **Ne pas réutiliser un volume comme s'il était frais.** Ces chiffres sont datés d'août 2026. La règle maison tient : un chiffre se remesure, ou se cite avec sa date et sa source. Un 15 500 a circulé neuf fois dans ce pipeline avant qu'on découvre qu'il valait 20.
- **Ne pas convertir un mot-clé isolé** avec `ratio_dfs_sem`. La dispersion est forte — écart-type 2,65, étendue ×0,03 à ×31. Le ratio médian sert à ajuster un seuil, pas à traduire une ligne.
- **Ne pas comparer les deux colonnes `kd`.** Elles ne mesurent pas la même chose et ne sont pas convertibles.

## Contexte

La migration et ses tests : `analyses/2026-08-29-croisement-semrush-dataforseo.md`, `2026-08-29-validation-3-graines-aveugle.md`, `2026-08-29-tests-fenetre-semrush.md`, et les trois rejeux `rejeu-rideaux-dataforseo`, `rejeu-gothique-zone-decision`, `rejeu-astro-zone-decision`.

Les règles qui en sont sorties vivent dans `METHODE-ANALYSE-MARCHE.md` (trois garde-fous), le skill `recherche-mots-cles`, et `PRODUCT-RESEARCH-CRITERIA.md` §1 pour les seuils recalibrés.

# Index local des preuves DataForSEO — Search France — 2026-09-05

## Périmètre et méthode

Lecture seule des `dfs*.json` à la racine de `/private/tmp` et des `niche*.json` sous `/private/tmp/boutique-recherche-5-go/tmp/`. Aucun appel réseau/API. Contrôle de la structure JSON : les fichiers `dfs*.json` sont, sauf `dfs-tuftime-smoke.json`, des snapshots de **requêtes** (nom, endpoint, payload), sans réponse DataForSEO (`tasks`/`result`/items de volume absents). Les dates ci-dessous sont donc soit des dates présentes dans un payload Trends, soit `non attestée` ; le mtime est donné séparément et ne vaut pas date de mesure.

## Rattachement aux huit pistes maison/confort

| Piste produit | Expression exacte retrouvée | Fichier / endpoint | France + français | Volume exploitable | Date attestée / mtime | Témoin et décision |
|---|---|---|---|---|---|---|
| Batardeau amovible anti-inondation | aucune (`batardeau`, `inondation` absents) | — | — | **NON COUVERT** | — | Aucun témoin DFS local. |
| Récupérateur d’air chaud poêle/cheminée | aucune (`récupérateur`, `recuperateur`, `cheminée` absents) | — | — | **NON COUVERT** | — | Aucun témoin DFS local. |
| Affûteuse à eau domestique | aucune (`affûteuse`, `affutage` absents) | — | — | **NON COUVERT** | — | Aucun témoin DFS local. |
| Cave électrique d’affinage fromages | `affineur fromage` (produit adjacent, pas la requête produit exacte) | `/private/tmp/dfs-discovery1.json` · `keywords_data/google_ads/search_volume/live` · `discovery-volumes-fr-1` | `location_name=France`, `language_code=fr`, `search_partners=false` | **REQUÊTE SEULEMENT**, aucun volume retourné | date non attestée ; mtime `2026-09-05 00:25:21` | Témoin = intention de requête uniquement ; ne pas promouvoir comme demande mesurée. |
| Kit de fumage à froid débutant | `fumoir a froid`, `generateur fumee froide`, `fumoir à froid` | `/private/tmp/dfs-discovery1.json` · `keywords_data/google_ads/search_volume/live` · `discovery-volumes-fr-1` ; `/private/tmp/dfs5-technew.json` · même endpoint · `volumes-techniques-jeux-fr` | Les deux payloads : `location_name=France`, `language_code=fr`, `search_partners=false` | **REQUÊTE SEULEMENT**, aucun volume retourné | dates non attestées ; mtime `2026-09-05 00:25:21` et `2026-09-05 08:22:08` | Expressions réutilisables pour une future mesure ; pas de chiffre local. |
| Four/cuiseur solaire nomade | aucune (`four solaire`, `cuiseur solaire` absents) | — | — | **NON COUVERT** | — | Aucun témoin DFS local. |
| Séchoir modulaire plantes/champignons | aucune (`séchoir plantes`, `sechoir a plantes` absents) | — | — | **NON COUVERT** | — | Aucun témoin DFS local. |
| Garde-manger ventilé bois | aucune (`garde-manger`, `garde manger` absents) | — | — | **NON COUVERT** | — | Aucun témoin DFS local. |

Les trois fichiers de requêtes ci-dessus contiennent aussi des expressions voisines (`pressoir fruits`, `deshydrateur alimentaire inox`, etc.) mais aucun résultat. Elles restent des graines à mesurer, pas des preuves de volume et pas de nouvelles pistes promues dans cet index.

## Témoin chiffré local, hors huit pistes

`/private/tmp/dfs-tuftime-smoke.json` contient des objets de résultats synthétiques pour `expression: "tufting"`, dont `volume: 12100`, `volume_min: 480`, une série mensuelle et des variantes. C’est le seul JSON `dfs*.json` inspecté contenant un champ de volume ; le fichier ne contient ni endpoint, ni `location_name`, ni `language_code`, ni date de mesure. Date attestée : **non**. Mtime : `2026-09-01 10:08:14`. Il s’agit d’un témoin ancien/incomplet, lié à une piste existante, et il n’est pas réutilisé pour une nouvelle piste maison/Search.

## Contrôle global des snapshots DFS

Les requêtes de volume France/fr repérées comprennent notamment `dfs-discovery1.json`, `dfs-go-variants.json`, `dfs5-jobs.json` et `dfs5-technew.json`; leurs payloads exposent `keywords`, le endpoint `keywords_data/google_ads/search_volume/live`, France/fr et aucune réponse. Les autres `dfs*.json` inspectés suivent le même schéma de requête ou sont des SERP/Trends hors mesure de volume pour ces pistes. Les fichiers à `location_code=2250` et `language_code=fr` n’exposent pas le nom France dans le JSON ; aucun chiffre n’en est déduit.

Les payloads Google Trends contiennent parfois une période attestée `date_from=2021-01-01`, `date_to=2026-08-31`, mais ce sont des paramètres de requête, pas des réponses et aucun ne couvre les huit pistes retenues. Ils ne sont pas utilisés comme volume Search.

## Fichiers `niche*.json`

Les dix fichiers niche inspectés (`niche-01-scanner.json` à `niche-10-sousvide.json`, avec le doublon `niche-07-radon.json`) sont des dossiers `niches`/`blocages` d’idéation et de sourcing/économie, sans endpoint DataForSEO, expression/volume Search France-fr ou réponse DFS. Ils sont donc **hors preuve volume** et leurs données de sourcing ne sont pas reprises ici. Mtime commun observé : `2026-09-05 08:29:21`, simple mtime, aucune date de mesure attestée.

## Limites opérationnelles

- Aucun volume actuel, seuil Search ou saisonnalité ne peut être conclu depuis ces snapshots.
- Les expressions exactes et paramètres France/fr ci-dessus peuvent servir à une prochaine mesure autorisée ; l’absence de résultat ici n’est pas un `NO_GO`.
- Les dates de mtime servent uniquement à situer les fichiers. Elles ne remplacent pas la date attestée d’une réponse DataForSEO.

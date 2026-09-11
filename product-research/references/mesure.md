### Protocole DataForSEO France

1. Charger les identifiants depuis `ecommerce-dropshipping/.env` sans les afficher.
2. Tirer le témoin `tufting` via DataForSEO avant la première mesure et après la dernière ; les deux
   réponses doivent être non nulles et cohérentes entre elles. Sinon, arrêter sans publier de chiffres.
3. Découvrir le corpus avec `boutique-pipeline/scripts/kw_dfs.py`, endpoint
   `dataforseo_labs/google/keyword_suggestions`, correspondance plein texte.
4. Contrôler les têtes et mots décisifs avec `keywords_data/google_ads/search_volume/live`.
5. Imposer `location_name: France` et `language_name: French` dans chaque payload.
6. Comparer 3 à 5 formulations et plusieurs niveaux : produit, variante, singulier/pluriel, catégorie
   parente, requête achat/prix ou douleur/usage.
7. Dédupliquer les buckets proches : une idée normalisée par groupe, `MAX` du groupe ; ne jamais sommer
   deux séries mensuelles identiques. Les fautes d'orthographe et les graphies sans accent qui forment
   un bucket distinct comptent dans le volume net de marque (chemin SMP, 11/09/2026).
8. Appliquer les seuils DataForSEO de `PRODUCT-RESEARCH-CRITERIA.md`, puis croiser obligatoirement avec
   Google Trends, SERP et Shopping. Archiver le JSON, l'endpoint, les paramètres, la date et le coût.
   La SERP sert à retirer les contaminations (autre sens, service, informationnel) ; sur le chemin SMP,
   une page 1 tenue par des généralistes ne retire aucun volume.

## Limites de mesure

`null`/`n/a` signifient une donnée indisponible ou non restituée, pas automatiquement zéro ni « moins de 10 ». Conserver les réponses brutes et distinguer corpus complet/plancher. Le témoin historique tufting = 12 100 est daté, pas une constante éternelle ; contrôler réponses valides, paramètres et cohérence avant/après. Le script compare des réponses valides avant/après ; une incohérence bloque la sortie. Un cache sans date doit être rafraîchi explicitement, dans le budget autorisé. Les métadonnées JSON sont conservées dans le fichier compagnon `.meta.json`.

Le CPC conserve sa devise attestée ; si elle est absente, ne pas inventer EUR ou USD. DataForSEO est le gate de l'étude rapide. Depuis le 11/09/2026, un volume OneClickBrand (données Semrush) compte aussi : il s'écrit avec la source `OCB/Semrush`, la date et le pays, et se recoupe avec DataForSEO. Un écart se documente ; le chiffre OCB n'est pas jeté, et il ne devient pas le seul gate si DataForSEO est indisponible. Sur OneClickBrand Trend Niche, faire une passe filtrée Facile (difficulté 0–40) et une passe sans filtre de difficulté. Google Trends mesure un indice relatif, jamais un volume. Examiner la période propre à la branche ; télécharger les données disponibles et déclarer les limites d’accès sans contourner les protections.

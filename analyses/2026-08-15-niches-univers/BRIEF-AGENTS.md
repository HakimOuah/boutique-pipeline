# Brief commun — analyse des 6 niches univers (15/08/2026)

Ce dossier est **versionné** (contrairement à `reports/`, exclu par le `.gitignore`) : tout ce qui
est écrit ici est sauvegardé sur GitHub. Écris tes rapports **ici**, pas dans `reports/`.

Plan de référence : `boutique-pipeline/plans/2026-08-15-plan-analyse-niches-univers.md` (à lire en
premier — il contient les seuils, les six niches, les graines et les décisions de Hakim).
Méthode : `METHODE-ANALYSE-MARCHE.md` à la racine du hub (catalogue des pièges — à lire).
Critères pipeline : `boutique-pipeline/PRODUCT-RESEARCH-CRITERIA.md`.

Décisions de Hakim du 15/08 (postérieures au plan, elles priment) :
- **Enchaîner les six étapes d'un coup**, sans attendre un verdict intermédiaire : la concurrence, la
  sourçabilité et l'économie se font sur toutes les niches, même celles qui semblent STOP après la
  mesure. Le verdict final intègre tout.
- **U3 globe** : élargir à la cartographie déco (planisphères, cartes du monde bois/liège/à gratter,
  carte du ciel).
- **U4 astronomie** : mesurer la totalité (télescopes ET déco astro). Sites drop de référence donnés
  par Hakim : `https://lepetitastronaute.fr/`, `https://les-astronautes.fr/`.
- **U5 gothique** : inclure le textile (vêtements), avec la réserve retours. Site drop de référence :
  `https://antregothique.com/`.

## Écris ton rapport au fil de l'eau — règle ajoutée le 15/08 à 21h30

La première tentative (six agents lancés à 17h50) a été **coupée net par la limite de session**, et
**aucun des six n'avait écrit une ligne** : plusieurs heures de mesures perdues parce que tout
attendait la fin. Donc :

1. **Crée ton fichier de rapport dès ta première mesure**, avec ses sections vides et l'en-tête daté.
2. **Réécris-le après chaque graine mesurée** (ou chaque groupe de 3 requêtes SERP) : les tableaux
   se remplissent au fur et à mesure, avec les chiffres bruts tels que lus.
3. Un rapport partiel mais écrit vaut infiniment mieux qu'un rapport complet jamais rendu. Si tu es
   interrompu, ce qui est sur le disque doit suffire à reprendre sans remesurer.
4. Garde une section « État d'avancement » en tête du fichier : graines faites / restantes, requêtes
   SERP faites / restantes. Mets-la à jour à chaque écriture.

## Budget de mesure (resserré le 15/08 à 21h30)

La première tentative a épuisé la session en balayant trop large. Reste dans ces bornes :

- **10 à 14 requêtes Keyword Magic Tool** par niche, pas 25. Choisis les graines qui portent le
  volume, et sers-toi des sous-groupes affichés plutôt que de multiplier les requêtes.
- **8 à 12 requêtes Google SERP**, sur les têtes de collections cœur uniquement.
- **3 à 5 sondes Google Shopping**.
- Extraction **compacte** en JavaScript (slices ciblés, jamais `get_page_text` sur toute la page) :
  une lecture SEMrush ne doit pas dépasser ~4 000 caractères rendus.

## Seuils (mode Kraken `catalogue-volume`, DECISION_PROJET 08/08/2026)

- Total boutique **commercial nettoyé et dédupliqué** France : plancher **30 000/mois**, confort
  **40 000+**.
- Collection cœur ≥ **1 000** (revue 800-999) ; secondaire ≥ **500** (revue 300-499) ; < 300 = pas
  de collection autonome.
- ≥ **200 concepts de produits** distincts prouvés au niveau des catégories.
- Ratio **prix moyen ÷ CPC ≥ 100** (viser 150-200).
- Low ticket autorisé mais gate `STOP_PRIX_PANIER` : 30-50 prix relevés, médiane, part sous 15 €,
  mécanisme de panier **observé** chez un acteur (jamais inventé).

## Navigateur — règles impératives

Tu partages le Chrome de Hakim avec d'autres agents qui travaillent **en même temps**.

1. Charge d'abord les outils : `ToolSearch` avec
   `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__tabs_close_mcp`.
2. Appelle `tabs_context_mcp`, puis **crée ton propre onglet** avec `tabs_create_mcp` et **utilise
   toujours son `tabId`** dans chaque appel `navigate` / `javascript_tool` / `get_page_text`.
   Ne touche jamais à un autre onglet. Ferme ton onglet à la fin.
3. **Jamais de capture d'écran, jamais de clic, jamais de saisie clavier** (`computer`,
   `screenshot`, `find`, `form_input` interdits) : ils entrent en collision avec les autres agents.
   Tout se fait par URL + `javascript_tool` (lecture de `document.body.innerText`, extraction ciblée
   par regex/slice) ou `get_page_text`.
4. Après chaque `navigate`, attends le rendu dans le JS : `await new Promise(r=>setTimeout(r,3500))`
   avant de lire.
5. Si une page affiche un écran de connexion, un CAPTCHA ou un quota épuisé : **note-le dans la
   section Limites et continue** avec ce qui reste faisable. Ne saisis jamais d'identifiants.

## Recette SEMrush (validée le 15/08 à 17h45 sur cet onglet)

- Keyword Magic Tool en expression exacte :
  `https://fr.semrush.com/analytics/keywordmagic/?q=<mot-clé URL-encodé>&db=fr&mt=phrase`
  → 100 lignes triées par volume, 0 crédit. Vérifie « Base de données: France » dans le texte.
- Extraction JS compacte (à adapter) :
  ```js
  await new Promise(r=>setTimeout(r,3500));
  const t=document.body.innerText;
  const i=t.indexOf('Tous les mots clés:'); const j=t.indexOf('Copier', i);
  const head=t.slice(i, i+220);            // total mots-clés, Volume total, KD moyen
  const rows=t.slice(j+7, j+7+9000);       // lignes : mot clé, mot clé, intention, volume, KD, CPC, MAJ
  ({base:(t.match(/Base de données:\s*(\S+)/)||[])[1], head, rows})
  ```
  Les lignes se lisent par groupes : `mot clé` (2×), intention (C/I/N/T, parfois deux lettres),
  volume, KD, CPC (USD), fraîcheur. Prends les 100 lignes ; si la 100ᵉ est encore > 300, note
  **plancher** et relance avec un modificateur.
- Sous-groupes de gauche (le bloc avant « Afficher plus ») = segments réels de la demande, à lire.
- « Volume total » du KMT est un **plafond broad**, jamais un adressable.
- `n/a` ≠ 0. Devise USD. Base France obligatoire.

## Recette Google SERP et Shopping (lecture texte)

- SERP : `https://www.google.fr/search?q=<requête>&hl=fr&gl=fr&num=20&pws=0`
- Shopping : `https://www.google.fr/search?q=<requête>&hl=fr&gl=fr&tbm=shop`
- Lire `document.body.innerText` (slice 0-12000), relever : ligne « Résultats, y compris pour… »
  (rabattement), nature des résultats, positions organiques par type d'acteur (marketplace,
  généraliste, marque, spécialiste indépendant, drop probable), présence Shopping/annonces, prix
  visibles, recherches associées.
- Espace tes requêtes (≥ 4 s entre deux) ; en cas de CAPTCHA, arrête Google et note-le.

## Recette AliExpress

- Passerelle API (Bash, sans navigateur) :
  `python3 "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/codex-chasse-clusters/tools/aliexpress_vps_gateway.py" search "<deux mots rares>" --limit 20 --destination FR --sort-by orders`
  (aussi `--sort-by price_desc` ; `latest` rend 0 ; limite dure 20 ; `variants <product_id>` et
  `exact <product_id>` pour prix réel `offer_sale_price`, ventes, fret FR et délais).
  **Écrire en mots rares** (référence technique, mot de métier, nom de magasin) — jamais de mot
  fréquent : `search` trie par popularité globale et rend les best-sellers de toute la catégorie.
- SERP AliExpress dans ton onglet Chrome :
  `https://fr.aliexpress.com/w/wholesale-<requete-tirets>.html?SortType=total_tranpro_desc`
  → JSON complet des 60 cartes dans `window._dida_config_._init_data_.data` (`itemList.content`) :
  productId, salePrice, starRating, tradeDesc, image. **Sur les SERP HTML, « 531 vendus » = 5,0 / 31
  ventes** (note collée) — utiliser le JSON, et confirmer en PDP quand c'est possible.
- Niveaux de confiance : A = PDP ouverte et lue ; B = SERP JSON + API ; C = titre seul.

## Autres sources

- Brand Search MCP (`ToolSearch` « brandsearch » puis `search_brands` / `get_brand` /
  `get_brand_ads_aggregates`) : boutiques FR actives en Google Ads sur la niche, nombre de produits,
  annonces. Les **visites** affichées ne sont pas fiables (règle maison) — ne jamais conclure dessus.
- Sitemap et JSON Shopify d'un concurrent (`/sitemap.xml`, `/collections.json`, `/products.json`)
  via `curl -sL` en Bash — c'est la première lecture, avant toute navigation.
- SimilarWeb : si accessible dans l'onglet (`https://www.similarweb.com/website/<domaine>/`), lire
  les visites mensuelles et appliquer **× 3** pour le trafic réel estimé ; sinon écrire « trafic non
  mesuré ».

## Règles de preuve (non négociables)

- Chaque chiffre est daté et sourcé (outil, URL, heure). Observé ≠ déduit ≠ hypothèse.
- Aucun volume de mémoire ni extrapolé ; un total dont le détail n'apparaît pas est une affirmation.
- Jamais un mot-clé dans deux familles ; jamais des familles distinctes additionnées pour franchir
  un seuil ; le test : une seule page servirait-elle ces requêtes ?
- Deux chiffres partout : brut et **net de marque**.
- Section **« Ce qui n'a pas pu être mesuré »** obligatoire à la fin de chaque rapport.
- Aucun contact vendeur, aucun achat, aucune modification Shopify / Ads / GMC.
- Tu ne prononces jamais de GO lancement : verdicts marché (GO marché / À APPROFONDIR / STOP),
  statuts sourcing (`FOURNISSEUR À TESTER` / `SOURCING INSUFFISANT` / bloqué), verdict économique
  (`GO_CONDITIONNEL` / `TENDU` / STOP), et c'est tout. La décision revient à Hakim.

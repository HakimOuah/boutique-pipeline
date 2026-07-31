# 06 — Index du workspace Notion « OH VENTURES »

> Dossier de passation Codex. Parcours en **lecture seule** effectué le 30/07/2026 via le connecteur Notion MCP.
> Doctrine actée (rappelée dans le hub Notion lui-même et dans les pages boutiques) : **les fichiers locaux du dépôt sont la source de vérité, Notion est le tableau de bord**. En cas de contradiction ci-dessous, le dépôt fait foi.

Étiquettes : **[NOTION — url]** contenu vu dans Notion · **[FAIT — repo:chemin]** vérifié dans le dépôt · **[CONTRADICTOIRE]** Notion ≠ dépôt · **[OBSOLÈTE POSSIBLE]** fraîcheur douteuse · **[MANQUANT]** non trouvé.

---

## 1. Cartographie des pages

### 1.1 Hub — « 🏪 Pipeline Boutiques Drop »
- **URL** : https://app.notion.com/p/3a11f38c315481839935e21e1111bb20 — dernière édition 24/07/2026 [NOTION]
- **Résumé** : page racine du projet. Contient les deux bases liées (Recherches produit, Boutiques), la base Chasse aux clusters, le Modèle Page Produit Horizon et le Campement type. Rappelle explicitement « la source de vérité du pipeline reste les fichiers locaux […] ce Notion est le tableau de bord de suivi ».
- **Importance** : critique (point d'entrée navigation). **Relation dépôt** : complément pur (aucun contenu propre au-delà de la navigation).

### 1.2 Base « Recherches produit » (68 lignes)
- **URL** : https://app.notion.com/p/b23a48625ace4704980659f165bb0ec6 (data source `collection://1afa57a5-4259-426b-a5c5-41ff128df3a5`) [NOTION]
- **Résumé** : 1 ligne = 1 candidat produit (Réf 1–68), avec étape, verdicts marché/fournisseur, volume SEMrush, chemin du rapport local. Quasi tout en ⛔ STOP ; en vie : « Kit tufting complet » (5·Marge, GO marché) et « Graveur laser fermé débutant » (4·Sourcing, À approfondir).
- **Fraîcheur** : lignes créées les 18/07 (23:36–23:38) — **snapshot du registre au 18/07**. [OBSOLÈTE POSSIBLE]
- **[CONTRADICTOIRE]** avec [FAIT — repo:registre-candidats.md, « Dernière mise à jour : 24 juillet 2026 »] : la base Notion **ne contient ni** les 2 candidats retenus par la chasse clusters (fontaine à eau filtrante à gravité, surpresseur domestique — compteur 2/20), **ni** le candidat Seiko mod (pourtant devenu la boutique NOIRMONT, niveau 2 atteint le 24/07), ni les issues de la vague 1 Brand Search. Le dépôt fait foi ; cette base est en retard de ~6 jours de pipeline.
- **Importance** : utile (dashboard) mais périmée. **Relation dépôt** : doublon partiel figé de `registre-candidats.md`.

### 1.3 Base « Boutiques » (3 lignes)
- **URL** : https://app.notion.com/p/3a26f4af523d448a907fce7b45b42bcc (data source `collection://e47a14f3-8d10-47be-8ce6-8e2748d5c4a5`) [NOTION]
- BTQ-1 « 🧩 MODÈLE Boutique — dupliquer » (À créer) · BTQ-2 « Montres Seiko Mod (Q4) » (En construction, URL maisonnoirmont.fr) · BTQ-3 « 🧶 Boutique Tufting » (**Statut : « Ads lancées »**).
- **[CONTRADICTOIRE]** : le statut « Ads lancées » de la boutique Tufting n'est étayé par aucune trace de campagne dans le dépôt. L'ancien résumé du 21/07 disait « Rien publié », mais le même `project-state.md` documente la publication du 23/07 et `tufteo.com` répond publiquement le 30/07. **Résolution** : Tuftéo est bien publiée ; seul le statut publicitaire reste contradictoire/non prouvé. [FAIT — repo:boutique-tufting/project-state.md §23/07 + HTTP public 30/07]
- **Importance** : utile. **Relation dépôt** : dashboard, champ Statut non fiable.

### 1.4 « 🏕️ Campement type — Lancement boutique » ⭐
- **URL** : https://app.notion.com/p/3a71f38c315481b88b28d745e54efc05 — dernière édition 26/07/2026 [NOTION]
- **Résumé** : LE modèle réutilisable de lancement de boutique. À dupliquer à chaque « lance une boutique sur X ». Contient : règles transverses (source de vérité locale, jamais `switch-shop`, jamais toucher aux SKU, `first:250` + pagination, promesses vérifiables/numériques, persona bloquant, QA mobile-first, placeholders = chasse gardée Hakim, mapping skills globaux par ticket), l'en-tête à adapter, le Kanban de tickets, et **deux générations de « ⚠️ Pièges vérifiés »** (passe des 25-26/07 puis passe du 26/07 avec corrections datées).
- **Importance** : **critique**. **Fraîcheur** : bonne (26/07).
- **Relation dépôt** : **unique — ce modèle n'existe pas en local.** [MANQUANT dans le dépôt : grep « Campement » ne rend que des références (REPRISE-SESSION.md, BILAN, runbooks), aucune copie des briefs]. Les pièges recoupent partiellement `boutique-seiko-mod/REPRISE-SESSION.md` (§ « Pièges vérifiés ») et des runbooks épars, mais la compilation consolidée boutique-agnostique n'est que dans Notion. → Synthèse rapatriée §2.
- **Note interne [CONTRADICTOIRE résolu dans la page]** : la génération 1 des pièges dit de « re-interroger `updatedAt`/`size` » pour confirmer une écriture ; la génération 2 (26/07) **corrige** : seule la relecture du contenu ou l'empreinte MD5 prouve l'écriture, et `upsertedThemeFiles: []` sans erreur est une écriture asynchrone normale, pas un échec. La génération 2 concorde avec [FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md]. En reprenant le modèle, lire la gen 2 comme correctif de la gen 1.

### 1.5 Base « Tickets — Lancement boutique (modèle) » (20 tickets)
- **URL** : https://app.notion.com/p/da8b39cc1a4248f2aec7494df5ef247b (data source `collection://139e0897-e0dd-4645-a1d6-681e54a919b2`) [NOTION]
- 20 tickets-briefs d'agents, ordre 0 → 17 : 00 Kick-off · 00b Arborescence · 01 Sourcing AliExpress · 02 Persona (BLOQUANT copywriting) · 03 Charte · 04 Import DSers · 05 Canal + collections + menus · 06 Francisation · 07 Prix ×1,3 · 08 Images anti-faux-logos · 09 Pages produit structure Tuftéo · 10 Homepage · 11 Étoiles vert Trustpilot #05b67a · 12 Avis Trustoo · 12b Panier bannière+upsells · 13 Livraison · 14 Pages légales · 15 Réglages boutique · 16 QA mobile-first · 17 Clôture/synchro. Statuts tous « À faire » (c'est le modèle vierge).
- **Importance** : **critique**, contenu **unique à Notion** (chaque ticket a objectif/entrées/procédure/garde-fous/critères de fin détaillés).
- **Corrections en cours de route — vérifiées présentes** (demandé par la mission) :
  - **CAPTCHA AliExpress** : ✅ présente dans le ticket 01 (https://app.notion.com/p/3a71f38c315481ebb68df10667c126bf, édité 25/07) : « ⚠️ CORRECTION du 25/07 — le CAPTCHA n'est pas une protection du site mais la conséquence d'un navigateur sans session » + « listings morts » = artefact d'identifiants tronqués (préfixes réels jusqu'à `1005012`). Aussi reprise dans la section Organisation du campement.
  - **Auto-matching DSers** : ✅ présente dans le ticket 04 (https://app.notion.com/p/3a71f38c31548116a321dc7e9b6f6af1, édité 25/07) : « ⚠️ CORRECTION du 25/07/2026 — l'auto-matching par SKU N'EXISTE PAS » (vérifié sur 19 fiches ; appariement à la main, SKU = source de vérité de l'appariement, pas un automatisme). Aussi reprise dans la section DSers du campement.
- **Divergence ticket ↔ dépôt** : le ticket **12b** (édité 26/07 13:31) prescrit encore « re-query `updatedAt`/`size` des fichiers pour confirmer la prise » — consigne **invalidée le même jour** par la passe gen 2 des pièges (relecture/MD5 uniquement) et par [FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md]. [CONTRADICTOIRE] — appliquer la règle MD5/relecture. Les autres tickets vérifiés (01, 04, 00, 09, 12) sont cohérents avec le dépôt.

### 1.6 « ⌚ Montres Seiko Mod (Q4) » — fiche boutique NOIRMONT
- **URL** : https://app.notion.com/p/3a71f38c315481979cbfc1556049a1d9 — contenu arrêté au 25/07 [NOTION]
- **Résumé** : dashboard complet de la boutique NOIRMONT : décisions 24/07, catalogue v1 (fiches AliExpress + coûts), configurateur, fournisseurs (Corgeut Factory, BL Watches), branding, liste d'import DSers 26 fiches, log du build autonome 24-25/07.
- **Importance** : utile (historique) mais **[OBSOLÈTE POSSIBLE] — en retard de 3 jours sur le dépôt**, qui fait foi : [FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md (27-28/07)].
- **Contradictions précises (le dépôt fait foi)** :
  - **Charte** : Notion décrit la « Charte v2 » palette encre/craie/pierre + **vert Jura + laiton**, typo Bodoni Moda/Inter/Space Grotesk. Le dépôt (direction « A+B ») : accent **cyan #22D3EE** (instrument uniquement), **vert forêt et laiton purgés à la source — ne pas réintroduire**, Oswald affichage + Inter. [CONTRADICTOIRE]
  - **Configurateur** : Notion = « codé maison, prix unique envisagé 349 € ». Dépôt = pivot en **« guide de choix »** (filtrage progressif du catalogue, aucune prime de prix possible, V2 « grammaire des pièces » livrée le 28/07 sur `/pages/configurateur`). [CONTRADICTOIRE]
  - **`switch-shop`** : la case à cocher Notion dit « me connecter au MCP (**switch-shop**) pour le build » — instruction devenue **interdite** (le campement et le dépôt : `switch-shop` invalide la connexion pour tout le monde). Ne jamais l'exécuter. [CONTRADICTOIRE]
  - Livraison : Notion mentionne « généralement 2 à 3 semaines » dans les accordéons ; le dépôt a normalisé **J+14/J+21**. [OBSOLÈTE POSSIBLE]
- **Info présente uniquement dans Notion** : le tableau consolidé « Liste d'import DSers — 26 fiches » avec liens + coûts au 24/07 (le dépôt a les rapports de phase 4 par famille, pas ce tableau unique) ; les tableaux concurrents (montreapapy, goteia) sous forme synthétique — détails toutefois dans `boutique-seiko-mod/analyse-concurrent-montreapapy-2026-07-24.md` et `analyse-configurateur-goteia-2026-07-24.md`.

### 1.7 « 🧶 Boutique Tufting — Arborescence & sourcing » + 3 sous-pages
- **URL** : https://app.notion.com/p/3a21f38c315481f7b452e27b7acdd84b — contenu arrêté au 21/07 (Porte 2) [NOTION]
- **Résumé** : Portes 1 et 2 validées (Tuftéo, palette, logo hybride), arborescence 37 nœuds, synthèse sourçabilité (4 UE / ~20 Chine / 5 non viables), trous d'assortiment (laine NZ, cadres, colle).
- Sous-pages : 🎯 Persona validé 19/07 (https://app.notion.com/p/3a21f38c315481e09821f2c8e69fb2fb) · 📄 Notice fournisseur AK (https://app.notion.com/p/3a21f38c3154818a9577eeaa144cf9b1) · 📝 Page produit Kit tufting brief+draft (https://app.notion.com/p/3a21f38c315481d8a234c6c9af9deb23). Chacune pointe sa source locale ([FAIT — repo:personas/persona-tufting-2026-07-19.md, fournisseur-docs/notice-tufting-analyse-2026-07-19.md, boutique-tufting/content/*]).
- **Importance** : utile. **Relation dépôt** : doublon-dashboard de `reports/arborescence-sourcing-tufting-2026-07-19.md` + `boutique-tufting/project-state.md`. Rien d'unique hormis la mise en forme. Voir §1.3 pour le statut « Ads lancées » contradictoire.

### 1.8 Base « Sourcing tufting — letufting.fr → AliExpress » (37 lignes)
- **URL** : https://app.notion.com/p/303ebb7889914cfdb6a12391f6c6e502 — 19/07 [NOTION]
- 1 ligne/produit du catalogue concurrent avec URL /item/, prix rendu, délai, statut UE/Chine. **Relation dépôt** : doublon de `reports/arborescence-sourcing-tufting-2026-07-19.md` (source de vérité déclarée dans la page mère). Sert de modèle de base pour le ticket 01 du campement. Importance : utile.

### 1.9 Base « Chasse aux clusters — juillet 2026 »
- **URL** : https://app.notion.com/p/03c8adc603a3446591e32501bad269b6 — ~20/07 [NOTION]
- Schéma : Produit/Cluster, Statut (Retenu, Vivier, STOP…), Famille (dont « Vague 1 Brand Search », « Codex multi-marchés »), volume, fournisseur, confiance A/B/C. **Relation dépôt** : dashboard de `registre-candidats.md` + `familles-exploration.md`. [OBSOLÈTE POSSIBLE] — même risque de retard que la base Recherches produit ; le registre local fait foi (compteur 2/20 au 24/07).

### 1.10 « 🛒 Modèle Page Produit Shopify — Horizon » + 10 sous-pages
- **URL** : https://app.notion.com/p/3a11f38c31548150a5afd3af4ea350bc — 18/07 [NOTION]
- **Résumé** : capture de référence de la page produit Bonum Vitae (thème Horizon) : structure CRO, 6 blocs Liquid custom, `bv-avis-clients.liquid`, `buy-buttons.liquid`, JSON, textes, 2 bases (Variables, Preuves), checklist de reconstruction, plus « Modèle panier » (https://app.notion.com/p/3a11f38c31548100a387e34d1f3fc30a) et « Modèle homepage » (https://app.notion.com/p/3a11f38c31548172bbaac1dc9d637e87).
- **Relation dépôt** : doublon assumé — la page déclare elle-même le dossier local `docs/horizon-product-page-reference/` [FAIT — repo:docs/horizon-product-page-reference/]. Importance : utile (référence), rien d'unique.

### 1.11 « 🧩 MODÈLE Boutique — dupliquer » (BTQ-1)
- **URL** : https://app.notion.com/p/3a11f38c315481ecb7f3efadfd770c83 — 18/07 [NOTION]
- Checklist de lancement générique 7 sections, antérieure au campement.
- **[OBSOLÈTE POSSIBLE] + doublon** : entièrement **supplanté par le Campement type** (18 tickets-briefs, 24/07). À considérer comme archive ; ne pas dupliquer ce modèle-ci. Importance : archive.

---

## 2. Informations critiques rapatriées (présentes uniquement — ou seulement consolidées — dans Notion)

> Source : page Campement type (https://app.notion.com/p/3a71f38c315481b88b28d745e54efc05) et tickets 01/04, sauf mention. Le dépôt en couvre des fragments épars (REPRISE-SESSION.md, runbooks boutique-seiko-mod/) mais **la compilation boutique-agnostique n'existe que dans Notion**. Synthèse — pour le détail, lire la page source.

### 2.1 Le modèle de lancement lui-même [NOTION uniquement]
Les 20 tickets-briefs (§1.5) et les règles transverses du campement n'ont **aucune copie locale**. Si Notion devenait inaccessible, le modèle de lancement serait perdu. Règles transverses clés : local d'abord puis synchro Notion ; **jamais `switch-shop`** ; **jamais toucher aux SKU** ; résultats MCP > ~25k tokens → fichier `/tool-results/*.txt` ; variantes `first:250` + curseur (la « limite 100 » est obsolète, Shopify accepte 2048) ; promesses vérifiables, bonus livrés en numérique ; copywriting bloqué sans persona ; QA mobile-first ; placeholders avis = Hakim seul ; skills globaux à invoquer par ticket (02, 03, 07, 08, 09, 10, 12b, 15, 16) et post-lancement `ads`+`ad-creative` avec `google-ads-launcher`/`meta-ads-creator`.

### 2.2 Pièges vérifiés — synthèse des deux générations (25-26/07, corrections incluses)
**Écriture de thème** — 4 rejets **silencieux** réels : nom de schéma de bloc > 25 caractères ; champ CSS de section (passer par un asset) ; `seo { description }` envoyé seul **écrase** `seo.title` (toujours envoyer les deux) ; et ⚠️ correction 26/07 : `themeFilesUpsert` → `upsertedThemeFiles: []` sans `userErrors` = **écriture asynchrone normale**, pas un échec. Preuve d'écriture = **relecture du contenu ou MD5**, jamais `size`/`updatedAt`. Une requête `files(filenames:)` peut renvoyer un nœud **étiqueté d'un nom avec le contenu d'un autre fichier** — valider l'appariement nom↔contenu par empreinte avant réécriture.

**Médias partagés (le piège le plus coûteux)** — attacher une image par `originalSource` ne copie pas : même objet `MediaImage` partagé entre produits ; l'`alt` est une propriété du **fichier** → chaque écriture écrase celui des autres produits (31 alt détruits) ; supprimer un média d'une fiche le retire de toutes. ✅ Rattacher par `files: [{id: "gid://shopify/MediaImage/…"}]`.

**Swatches** — donnée Shopify, pas du thème : champ `swatch` en lecture seule, passer par les **métaobjets liés à l'option** (catégorie Montres : clés `dial-color`/`case-color`, la clé générique `color-pattern` est refusée) + une image par variante sinon le clic ne change pas la galerie.

**DSers** — auto-matching par SKU inexistant (appariement manuel, table bâtie via l'API Shopify) ; listes de valeurs **virtualisées** (faire défiler) ; boîte « Appliquer le mapping » à confirmer sinon rien n'est écrit ; grille Unmapped qui ne se rafraîchit pas ; Chrome bride les minuteries en arrière-plan ; produit créé par l'API → « Import products from Shopify », additif, par lots de 10 ; menus qui se repositionnent → vérifier le libellé sélectionné (valeurs proches : `no logo`/`corgeut`, `bronze case-no logo`/`bronze case-logo`).

**Découpage de catalogue** — ne jamais supprimer une valeur d'option pour réduire les fiches (détruit le mapping ; fusionner via option secondaire) ; découper par modèle, garder les dimensions en variantes ; sauvegarder l'état complet des variantes avant toute suppression ; les fiches filles héritent du texte de la mère (purger + SEO uniques) ; **le SKU ne prouve pas l'identité visuelle** d'une image (6 mères contrôlées, 6 échecs) ; requêtes média plafonnées à 30 → paginer et recompter avant toute purge.

**Marques tierces** — ✅ nommer le fabricant du **composant** réellement installé (Seiko NH35, Miyota 8215) ; ⛔ marques dont le produit reprend le dessin ; ⚠️ coordination grammaticale : écrire « Calibre DG3804 ou Seiko NH34 », jamais l'inverse. Un VK63 méca-quartz est **à pile** : vérifier la nature du mouvement par famille avant toute promesse globale « automatique ».

**Images IA** — jamais de modèle UGC/mode pour du packshot (fabrique de faux logos) ; les modèles d'édition « réinventent » l'objet ; 4K coûte ~30 % au-dessus du tarif annoncé ; **régénérer plutôt qu'inpainter** sur cadran sombre.

**Vitrine & conformité** — facettes = app **Search & Discovery** (si seulement « Disponibilité + Prix », l'app n'est pas installée) ; son UI est une iframe non automatisable ; facettes sur métachamp normalisé, jamais sur étiquettes ; produit DSers importé = publié sur **aucun canal** (`publishablePublish` requis) ; collections automatiques sensibles au singulier/pluriel — contrôler les effectifs après publication ; liens de la caisse = **Réglages → Politiques**, pas les pages ; **médiateur de la consommation adhéré par site** (jamais recopier celui d'une autre boutique) ; garantie commerciale toujours **en sus** des garanties légales ; le réglage « Dates de livraison estimées » (absent de l'API, « Automatisé » par défaut) crée un **troisième délai** à la caisse — à désactiver dans l'admin.

**Méthode & organisation** — navigateur = ressource unique partagée : sérialiser les agents ; une session **connectée** évite les CAPTCHA AliExpress ; quand un agent conclut « techniquement impossible », faire revalider dans d'autres conditions avant d'en faire une doctrine (deux fausses limites inscrites puis corrigées).

### 2.3 Recettes sourcing AliExpress (ticket 01, passe du 25/07) [NOTION — https://app.notion.com/p/3a71f38c315481ebb68df10667c126bf]
- URLs directes `fr.aliexpress.com/item/<id>.html` + **une seule extraction JS immédiate** après navigation ; WebFetch inutilisable (rendu JS).
- Meilleure découverte : le carrousel **« Vous aimerez aussi »** des pages vivantes (titre, prix, note, ventes des voisins) ; élargir via l'onglet « Magasin » d'un vendeur validé.
- Identifiants : toujours copier en entier, préfixes réels jusqu'à `1005012` — ne jamais reconstruire un ID (source de faux « listings morts »).
- Variantes nommées « no logo »/« sterile » = signal de stérilité le plus fiable ; « pour Rolex/Seiko » dans les titres = mots-clés vendeur, jamais repris dans nos fiches.

### 2.4 Mapping DSers d'une fiche créée par l'API (ticket 04, autorisé à l'agent par Hakim le 25/07) [NOTION — https://app.notion.com/p/3a71f38c31548116a321dc7e9b6f6af1]
DSers → My Products → sélectionner la fiche → Mapping → coller l'URL AliExpress de la fiche mère → apparier **à la main** variante par variante (table de SKU lue via l'API Shopify) → contrôle obligatoire fiche par fiche (une fiche mal mappée = une commande non transmise). Ne jamais modifier un SKU pour « faire correspondre ».

---

## 3. Doublons et divergences — récapitulatif

**Doublons (Notion = miroir, dépôt fait foi)**
1. Base Recherches produit ↔ `registre-candidats.md` (miroir **figé au 18/07**).
2. Base Chasse aux clusters ↔ `registre-candidats.md` + `familles-exploration.md`.
3. Base Sourcing tufting ↔ `reports/arborescence-sourcing-tufting-2026-07-19.md`.
4. Modèle Page Produit Horizon (+panier, +homepage) ↔ `docs/horizon-product-page-reference/`.
5. Sous-pages tufting (persona, notice AK, page produit) ↔ fichiers locaux qu'elles citent.
6. « MODÈLE Boutique — dupliquer » ↔ « Campement type » : **deux modèles de lancement concurrents**, le premier est une archive.
7. Pièges vérifiés du campement ↔ § « Pièges vérifiés » de `boutique-seiko-mod/REPRISE-SESSION.md` : recouvrement partiel — Notion est plus complet (médias partagés/alt, swatches-métaobjets, découpage, marques tierces, conformité, dates de livraison estimées) ; le dépôt a 3 items absents de Notion (menus partagés entre thèmes, contraste mesuré sur le rendu, quota SEMrush gratuit « 0 mot clé »).

**Divergences (le dépôt fait foi)**
1. Statut Tufting « Ads lancées » (base Boutiques) vs dépôt « rien publié, brouillon uniquement » (21/07). [CONTRADICTOIRE]
2. Page Seiko Mod figée au 25/07 : charte laiton/vert-Jura/Bodoni vs charte A+B cyan/Oswald du dépôt ; configurateur 349 € vs « guide de choix » sans prime de prix ; consigne `switch-shop` devenue interdite ; délais « 2 à 3 semaines » vs J+14/J+21. [CONTRADICTOIRE / OBSOLÈTE]
3. Base Recherches produit sans les candidats post-18/07 (fontaine gravité, surpresseur, Seiko mod niveau 2). [CONTRADICTOIRE]
4. Ticket 12b : vérification d'écriture par `updatedAt`/`size`, invalidée par la gen 2 des pièges (MD5/relecture). [CONTRADICTOIRE]
5. Au sein même du campement : gen 1 vs gen 2 des pièges (`upsertedThemeFiles: []`, `size`/`updatedAt`) — la gen 2, datée 26/07, prime.

**Corrections en cours de route — statut vérifié** : CAPTCHA AliExpress ✅ inscrite (ticket 01 + campement §Organisation) ; auto-matching DSers ✅ inscrite (ticket 04 + campement §DSers). Aucune des deux n'a été oubliée.

---

## 4. Priorités pour Codex

1. **Sauvegarder localement le Campement type + ses 20 tickets** (seul actif critique sans copie dans le dépôt) — §1.4, §1.5, §2.
2. Traiter les bases Notion comme des dashboards périmables : toujours lire `registre-candidats.md`, `project-state.md`, `REPRISE-SESSION.md` d'abord.
3. Ne jamais exécuter les instructions périmées des pages Notion (`switch-shop`, vérif `updatedAt/size`, charte laiton/vert-Jura, configurateur 349 €).
4. En reprenant NOIRMONT : `boutique-seiko-mod/REPRISE-SESSION.md` est le document de reprise, la page Notion Seiko Mod n'est qu'un historique au 25/07.

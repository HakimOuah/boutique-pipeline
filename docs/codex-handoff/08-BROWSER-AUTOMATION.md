# 08 — Automatisation navigateur : l'existant, puis l'architecture cible

> Dossier de passation Codex — généré le 2026-07-30.
> **Étiquettes de source** : **[FAIT — repo:chemin]** = constaté dans un livrable du projet · **[MÉMOIRE]** = dossier mémoire Claude (`~/.claude/projects/-Users-Hakim-Documents-Boutiques-drop/memory/`) · **[HYPOTHÈSE]** = déduction non vérifiée · **[INFO HAKIM — brief de passation]** = information transmise par Hakim, non vérifiée ici · **[MANQUANT]** = introuvable dans le repo.
> Aucun secret dans ce document. Les identifiants ne sont **jamais** saisis par un agent (règle constante de tous les livrables).

---

## Partie 1 — L'existant : ce que Claude Code fait aujourd'hui au navigateur

### 1.0 Deux navigateurs, pas un — et la leçon la plus chère du projet

Deux outillages navigateur coexistent :

| Outillage | Nature | Session |
|---|---|---|
| `claude-in-chrome` | Le **Chrome réel de Hakim** (extension) | Sessions vivantes : AliExpress, DSers, Shopify admin, SEMrush |
| `mcp__Claude_Browser__` (navigateur d'aperçu) | Navigateur **isolé, sans session** | Aucune |

**Le « CAPTCHA AliExpress » historique était un artefact du navigateur sans session, pas une protection du site.** Constat daté et documenté en deux temps :

- La passe v2 concluait que les URL de recherche `/w/wholesale-*.html` déclenchaient un CAPTCHA systématique (non contourné, par principe) **[FAIT — repo:boutique-pipeline/boutique-seiko-mod/journal/2026-07-25-sourcing-accessoires-v2.md]**.
- La passe v3 a corrigé : dans le Chrome réel de Hakim, session AliExpress connectée, **zéro CAPTCHA** sur la recherche globale `/w/wholesale-<mots>.html` et sur la recherche in-store `/store/<id>/pages/all-items.html?SearchText=<mots>` (40 fiches, filtrable). Le navigateur isolé, lui, se fait servir `fr.aliexpress.com/wp.html` (challenge anti-bot) : la page charge ses images mais **n'hydrate jamais son texte** — d'où l'illusion de « listings morts ». Conclusion écrite : *« toujours utiliser le Chrome de l'utilisateur pour AliExpress »* **[FAIT — repo:boutique-pipeline/boutique-seiko-mod/journal/2026-07-25-sourcing-accessoires-v3.md §Notes de méthode]**.
- Leçon versée au bilan : le CAPTCHA « corrigé, la fausse limite aurait handicapé toutes les boutiques suivantes » **[FAIT — repo:boutique-pipeline/boutique-seiko-mod/journal/2026-07-25-bilan.md]**.

Nuance importante : même en navigateur sans session, les **URL directes `/item/<id>.html` passent** la plupart du temps — le sourcing configurateur du 27/07 a été fait « AliExpress FR/EUR via navigateur intégré, sans session — aucun CAPTCHA rencontré » **[FAIT — repo:boutique-pipeline/boutique-seiko-mod/journal/2026-07-31-sourcing-configurateur.md]**. Ce sont les **URL de recherche** qui déclenchent le challenge hors session.

**Règle absolue, jamais enfreinte : un CAPTCHA ne se résout pas.** Blocage = arrêt propre et déclaré, jamais de données inventées **[FAIT — repo:boutique-pipeline/specs/2026-07-17-pipeline-agents-phases-1-5-design.md ; plans/2026-07-20-boucle-chasse-clusters.md]**.

### 1.1 La règle « le navigateur est une ressource unique »

- *« Le navigateur est une ressource unique partagée entre l'orchestrateur et tous les agents. Deux consommateurs simultanés = onglets qui se re-naviguent. Sérialiser tout usage du navigateur. »* **[FAIT — repo:boutique-pipeline/boutique-seiko-mod/journal/2026-07-25-journal-nuit.md]**
- Formulation du bilan : *« sérialiser, ou utiliser deux navigateurs distincts »* (répartir : app intégrée/Chrome réel vs navigateur d'aperçu) **[FAIT — repo:boutique-pipeline/boutique-seiko-mod/journal/2026-07-25-bilan.md]**.
- Conséquence opérationnelle vécue : la création des fiches accessoires a été **bloquée une nuit entière** parce que DSers exigeait le navigateur, occupé par un autre chantier **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-journal-nuit.md §BLOQUÉ]**.
- Piège associé : un onglet en arrière-plan (`document.hidden === true`) voit ses `setTimeout` bridés par Chrome à ~1 déclenchement/minute — toute automatisation temporisée paraît plantée. Parade : temporiser via `MessageChannel` **[FAIT — repo:boutique-pipeline/boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md §pièges]**.

### 1.2 AliExpress — recherche, fiches, variantes

Ce que les agents font réellement, tel que documenté dans les rapports de sourcing (phases 4, accessoires v2/v3, arabes/squelettes, configurateur) :

**Découverte**
- Recherche globale et in-store dans le Chrome connecté (cf. 1.0) ; carrousels « Vous aimerez aussi » des fiches vivantes comme voie de repli **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-sourcing-accessoires-v2.md]**.
- Google comme index d'ID d'items — avec le piège documenté : **toujours extraire les 16 chiffres complets de l'ID, ne jamais reconstruire un préfixe** (les préfixes réels montent à `1005012…` ; des préfixes devinés ont fabriqué de faux 404) **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-sourcing-accessoires-v3.md]**.

**Extraction d'une fiche `/item/<id>.html`** — `window.runParams.data` renvoie désormais `{}` ; tout passe par le DOM **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-sourcing-accessoires-v3.md]** :
- titre : `document.querySelector('h1').innerText` ;
- note / avis / ventes / prix : ~250 premiers caractères de `document.body.innerText` à partir de la position du `h1` ;
- **matrice de variantes** : `document.querySelectorAll('[class*="sku"] img, [class*="Sku"] img')` puis attributs `alt` dédoublonnés — « la recette la plus rentable de cette passe », elle révèle les variantes « no logo » / « sterile » ;
- délai France réel : regex sur `Livraison: <dates>` ; largeurs : regex `Largeur de bande:`.

**Données relevées par fiche** (structure constante des rapports de phase 4) : URL, titre, vendeur + % d'avis positifs + abonnés, variantes avec prix par variante, stock affiché, entrepôt d'expédition (France/UE/Chine), fenêtre de livraison en jours vers une adresse française de référence, note /5, nombre d'avis, nombre de ventes, protections acheteur, caractéristiques **« annoncées par le vendeur, non contrôlées »**, signaux de risque **[FAIT — repo:boutique-pipeline/reports/phase4-sourcing-fontaine-gravite-2026-07-20.md]**.

**Limites et interdits constatés**
- Prix/stocks/délais dynamiques : tout relevé est daté et « à reconfirmer au panier » ; **aucun achat, aucun ajout panier, aucun contact vendeur** sans décision de Hakim **[FAIT — repo:reports/phase4-sourcing-fontaine-gravite-2026-07-20.md]**.
- Fiches « hommage » **géobloquées FR en série** = sourcing volatil **[FAIT — repo:registre-candidats.md, dossier Seiko mod]**.
- Photos d'avis et messages vendeurs = contrôles à la main de Hakim **[FAIT — repo:registre-candidats.md, phase 4b]**.

### 1.3 DSers — import, poussée, mapping

Compte : `contact.noirmont`, boutique `v42pzp-h4` liée. Tout ce qui suit est documenté dans quatre livrables : `boutique-seiko-mod/journal/2026-07-25-dsers-mapping-decoupage.md`, `boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md`, `boutique-seiko-mod/journal/2026-07-31-import-accessoires-lot4.md`, `boutique-seiko-mod/journal/2026-07-31-sourcing-arabes-squelettes.md` + `boutique-seiko-mod/journal/2026-07-31-publication-grappes.md` (tous sous `boutique-pipeline/boutique-seiko-mod/`).

**Deux flux d'entrée, dans les deux sens**
1. **AliExpress → Shopify** : import **URL par URL** dans la « Liste d'import » (champ « entrer le lien du produit »), puis sélection des cartes et **PUSH TO STORE** avec, dans la modale : « **Set product status as Draft** » **coché**, « Publier dans la Boutique également » **décoché** → les fiches arrivent en DRAFT, sur aucun canal. L'API Shopify réécrit ensuite titre/handle/description/SEO/prix/visuels **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-import-accessoires-lot4.md]**.
2. **Shopify → DSers** (fiches créées par l'API, que DSers n'a jamais vues) : bouton « **IMPORT PRODUCTS FROM SHOPIFY** », filtre « À être importé », **par lots de 10 maximum** — additif, produit par produit, ne réécrit rien côté Shopify **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-dsers-mapping-decoupage.md ; boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md]**.

**Pourquoi l'import DSers d'abord** : *« Créer un produit dropshippé à la main est un faux gain de temps »* — un produit créé par l'API n'a pas les SKU porteurs de la chaîne d'attributs AliExpress, et le mapping devient manuel variante par variante. L'import DSers donne les bons SKU **et** le rattachement fournisseur d'un coup **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-journal-nuit.md ; boutique-seiko-mod/journal/2026-07-31-import-accessoires-lot4.md]**.

**⚠️ L'auto-matching par SKU n'existe pas.** En collant l'URL fournisseur sur une fiche venue de Shopify, DSers rattache le bon produit fournisseur mais laisse **toutes les variantes vides**. Le rapprochement se fait à la main, option par option, en **Mapping basique**, avec les SKU utilisés comme **table de correspondance en lecture seule** (extraits via l'API Admin `products { variants { title sku } }`, jamais écrits) **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-dsers-mapping-decoupage.md ; boutique-seiko-mod/journal/2026-07-25-bilan.md]**. Seule exception : quelques libellés strictement identiques des deux côtés (`Miyota 8215`, `NH35`…) appariés seuls.

**Pièges d'interface vérifiés** (à connaître avant toute reprise) :
- **Listes virtualisées** : le menu ne rend que ~9 options sur 20 ; il faut faire défiler **et émettre un événement `scroll`** après avoir modifié `scrollTop`, sinon rien ne re-rend. Aucune saisie ne filtre ces sélecteurs **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md]**.
- **Boîte « Appliquer le mapping »** : le bouton `Enregistrer` ne suffit pas ; il ouvre une boîte à confirmer (`CONFIRMER`). L'enregistrement n'est réputé fait que lorsque `Enregistrer` repasse désactivé, recontrôlé par les compteurs d'onglets **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md]**.
- **Sélection déterministe uniquement** : jamais de clic aux coordonnées (les listes se repositionnent — deux erreurs produites puis corrigées ainsi) ; option localisée par texte **strictement égal** (`===`, jamais `includes`), refus si correspondances ≠ 1, libellé relu après sélection. Confusions réelles neutralisées : `M-1` ≠ `M11`, `IB-black-02A` ≠ `IB-black-02C` **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-dsers-mapping-decoupage.md ; boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md]**.
- Grille `Unmapped` **non rafraîchie** après enregistrement (recliquer l'onglet) ; dialogue « Unsaved changes » → toujours **IGNORER** ; coller une URL dans la mauvaise fiche ajoute un **fournisseur favori surnuméraire** (vécu, refusé comme défaut) **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-dsers-mapping-decoupage.md §Incidents]**.
- `supplyProductId` lisible en **observation passive** de l'API interne `dsers-product-bff/my-product/v2/search` (aucune requête forgée) **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md]**.

**Contrôle par compteurs** — l'invariant de toutes les passes : `Mes Produits (Tous) / AliExpress / Unmapped / 1688 / Alibaba / Liste d'import`, relevés avant/après, avec l'arithmétique attendue (ex. 85 → 98 = +13, Unmapped reste 0, donc aucune fiche historique démappée) **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-import-accessoires-lot4.md ; boutique-seiko-mod/journal/2026-07-31-publication-grappes.md]**.

**Session** : la **session DSers autonome expire** en cours d'opération. Repli vérifié : l'**app intégrée Shopify** (admin → DSers, redirection `auth_check`) rouvre l'accès **sans saisir d'identifiant** **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-sourcing-arabes-squelettes.md ; boutique-seiko-mod/journal/2026-07-31-publication-grappes.md ; boutique-seiko-mod/journal/2026-07-31-visuels-accessoires-lot4.md]**. Interdits constants : aucun identifiant saisi, aucune commande/paiement, aucun « × » de suppression de fournisseur, aucune préférence persistante cochée **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-dsers-mapping-decoupage.md §Règles respectées]**.

### 1.4 SEMrush — mesures de volume au navigateur

- Source de mesure canonique : **SEMrush France (`db=fr`)**, via navigateur ; Ahrefs = repli documenté **[FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md]**.
- Le marché Noirmont a été mesuré « sur SEMrush (compte payant) » — détail dans `boutique-seiko-mod/journal/2026-07-31-marche-complet-semrush.md` (ex. Seiko mod 38 690/mois, KD 10, CPC 0,22 €) **[FAIT — repo:boutique-seiko-mod/journal/2026-08-08-reprise-session.md ; boutique-seiko-mod/journal/2026-07-31-marche-complet-semrush.md]**.
- **⚠️ Quota gratuit silencieux** : « SEMrush en formule gratuite rend “0 mot clé” sans erreur passé le quota — utiliser un mot-clé témoin » (re-mesurer un mot-clé au volume connu pour distinguer « 0 réel » de « quota épuisé ») **[FAIT — repo:boutique-seiko-mod/journal/2026-08-08-reprise-session.md §Pièges vérifiés]**. Historiquement, Hakim prend des essais ponctuels plutôt qu'un abonnement permanent — ne pas présumer d'un compte actif **[FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md §2.1, daté 06/2026]**.
- Fail-closed : SEMrush déconnecté / CAPTCHA / page qui ne charge pas → **arrêt déclaré, aucun volume estimé de mémoire** **[FAIT — repo:plans/2026-07-20-boucle-chasse-clusters.md]**.

### 1.5 Shopify admin au navigateur — ce qui reste hors API

L'essentiel du travail Shopify passe par l'API Admin (connecteur MCP + GraphQL). Le navigateur ne sert que pour ce que l'API n'expose pas :

- **Réglages → Expédition et livraison → Dates de livraison estimées** : passé de `Automatisé` à `Désactivé` au navigateur (Shopify calculait ses propres dates à la caisse, contredisant la promesse J+14/J+21) **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-pages-legales-et-delais.md §4]**.
- **Réglages → Politiques** (liens du checkout) : recopie des pages légales, faite au navigateur le 26/07 **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-pages-legales-et-delais.md §5]**.
- **Search & Discovery : NON automatisable.** L'app est servie dans une **iframe cross-origin** (`search-and-discovery.shopifyapps.com`, `sameOrigin: false`). Constats tous vérifiés : l'arbre d'accessibilité s'arrête au bord de l'iframe ; les clics synthétiques ne la franchissent pas (coordonnées justes, page immobile, 3 essais) ; l'URL directe `/filters/new` rend une page vide ; le contrôle bureau (événements système) est refusé sur les navigateurs ; **il n'existe pas de chemin API** pour la configuration des facettes, et une définition de métachamp filtrable ne suffit pas — l'app doit ajouter la facette explicitement. Les « cinq gestes » (supprimer Disponibilité, ajouter 4 facettes métachamps) restent **à faire par un humain** **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-metachamps-montres.md §1]**.
- **QA mobile impossible dans cet outillage** : `resize_window` répond succès mais `innerWidth` reste 1920, media queries fausses ; pas d'émulation d'appareil → validation « sur un vrai téléphone » **[FAIT — repo:boutique-seiko-mod/journal/2026-07-31-metachamps-montres.md §6 ; boutique-seiko-mod/journal/2026-08-08-reprise-session.md]**. Le QA mobile est prioritaire dans la doctrine du projet **[MÉMOIRE — mobile-first-et-placeholders-demo.md]**.
- Actions marchand pures (jamais tentées par agent) : activer les cartes cadeaux, republier le thème, adhésion médiateur de la consommation **[FAIT — repo:boutique-seiko-mod/journal/2026-07-25-journal-nuit.md ; boutique-seiko-mod/journal/2026-08-08-reprise-session.md]**.

### 1.6 Codex et le navigateur — état transmis

- **[INFO HAKIM — brief de passation]** : « Codex semble actuellement bloqué sur AliExpress dans certains environnements. » Information transmise, **non vérifiée ici**.
- Corroboration partielle dans le repo : lors du run multi-marchés du 20/07, le sourcing Codex a échoué avec exactement `Browser Use rejected this action due to browser security policy` à l'ouverture d'une recherche AliExpress ; conformément au contrat fail-closed, les candidats ont été notés `RETENU_MARCHE_A_SOURCER` sans rien inventer **[FAIT — repo:boutique-pipeline/codex-chasse-clusters/reports/validation-multimarche-brandsearch-20260720-200609-a1.md]**.
- **[HYPOTHÈSE]** : ce blocage relève de la politique de sécurité du navigateur de l'environnement Codex (et/ou de l'absence de session, cf. 1.0), pas d'une protection AliExpress infranchissable — c'est cohérent avec la leçon v3, mais non testé dans l'environnement Codex actuel.

### 1.7 Session connectée indispensable, remplaçable par API, ou candidate extraction déléguée

| Étape | Session connectée indispensable ? | Alternative |
|---|---|---|
| Recherche AliExpress par mot-clé (`/w/…`, in-store) | **Oui** (hors session → challenge `wp.html`) [FAIT — sourcing-accessoires-v3] | Candidate à une extraction déléguée (voir note Apify) |
| Lecture fiche AliExpress `/item/<id>.html` (variantes, prix, délai, avis) | Non constatée comme indispensable (relevés faits sans session le 27/07) [FAIT — boutique-seiko-mod/journal/2026-07-31-sourcing-configurateur.md] ; **mais** le délai/prix « rendu France » fiable suppose une adresse de référence, donc une session [HYPOTHÈSE fondée sur la mention « adresse de référence Eaubonne/FR, compte connecté » des phases 4 — FAIT — reports/phase4-sourcing-fontaine-gravite-2026-07-20.md] | Extraction déléguée possible pour le volet catalogue ; contrôle au panier = session |
| DSers (import, push, mapping, compteurs) | **Oui** — et quand la session autonome expire, repli app intégrée Shopify [FAIT — boutique-seiko-mod/journal/2026-07-31-publication-grappes.md] | **Aucune API publique utilisée dans le projet** ; seule l'API interne `dsers-product-bff` a été observée passivement [FAIT — boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md] |
| SEMrush | **Oui** (compte, quotas) [FAIT — boutique-seiko-mod/journal/2026-08-08-reprise-session.md] | Repli Ahrefs documenté ; API SEMrush jamais utilisée dans le projet [FAIT — PRODUCT-RESEARCH-CRITERIA.md] |
| Shopify produits/collections/thème brouillon/métachamps/publication canaux | **Non** — API Admin GraphQL couvre tout, y compris médias (staged uploads) et `publishablePublish` [FAIT — boutique-seiko-mod/journal/2026-07-31-branchement-galeries-codex.md ; boutique-seiko-mod/journal/2026-07-31-metachamps-montres.md ; boutique-seiko-mod/journal/2026-07-31-publication-grappes.md] | C'est déjà la voie nominale |
| Search & Discovery, dates de livraison estimées, politiques, cartes cadeaux, republication de thème | Session admin **humaine** (iframe cross-origin ou réglages marchand) [FAIT — boutique-seiko-mod/journal/2026-07-31-metachamps-montres.md ; boutique-seiko-mod/journal/2026-07-31-pages-legales-et-delais.md] | Aucune — contrôle humain |

**Note Apify** : l'orientation « Apify pour l'extraction massive » est exprimée par Hakim **[INFO HAKIM — brief de passation]**. Vérification faite dans le repo : **aucune trace d'Apify** (grep insensible à la casse sur tout le dossier, y compris mémoire : zéro occurrence hors ce dossier de passation) **[FAIT — absence vérifiée le 2026-07-30]**. Tout ce qui concerne Apify en partie 2 est donc de l'architecture cible, pas de l'existant.

### 1.8 Fragilités connues et contrôles humains obligatoires

**Fragilités techniques**
- Interfaces mouvantes : DSers (listes virtualisées, grilles non rafraîchies, panneaux à animation décalée), AliExpress (variantes renommées en cours de vie de fiche, `runParams` vidé, listings 2021-2023 encore indexés) **[FAIT — boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md ; sourcing-accessoires-v2/v3]**.
- Sessions périssables : DSers autonome, SEMrush (quotas), AliExpress (géoblocage de fiches hommage) **[FAIT — cités supra]**.
- Navigateur = ressource unique ; onglets d'arrière-plan bridés **[FAIT — 1.1]**.
- Le SKU ne prouve pas l'identité **visuelle** d'une image après découpage de coloris **[FAIT — boutique-seiko-mod/journal/2026-08-08-reprise-session.md §Pièges]**.

**Contrôles humains (chasse gardée de Hakim — jamais délégués)**
- Saisie d'identifiants, résolution de CAPTCHA, toute commande/achat/« Place order », clic « × » fournisseur DSers **[FAIT — boutique-seiko-mod/journal/2026-07-25-dsers-mapping-decoupage.md]**.
- Commande test fournisseur (le passage niveau 2 → 3 du registre) et GO lancement **[FAIT — registre-candidats.md]**.
- Slider et avis de démonstration (placeholders) **[MÉMOIRE — mobile-first-et-placeholders-demo.md]** ; affirmations chiffrées de preuve sociale **[FAIT — boutique-seiko-mod/journal/2026-08-08-reprise-session.md §Ce qui attend Hakim]**.
- Photos d'avis AliExpress et messages vendeurs **[FAIT — registre-candidats.md, phase 4b]**.
- Republication de thème, activation cartes cadeaux, médiateur, Search & Discovery **[FAIT — 1.5]**.

---

## Partie 2 — Architecture cible de migration

> Structure demandée par Hakim **[INFO HAKIM — brief de passation]**. Les responsabilités ci-dessous sont la cible ; l'existant (partie 1) reste la référence de comportement à répliquer.

### 2.1 Répartition des rôles

| Brique | Rôle | Ancrage dans l'existant |
|---|---|---|
| **Codex / Sol** | Raisonnement, orchestration, code. Tient le registre, applique les critères canoniques, décide quoi appeler, écrit les rapports, ne touche jamais un site directement. | Rôle tenu aujourd'hui par Claude Code + sous-agents [FAIT — specs/2026-07-17-pipeline-agents-phases-1-5-design.md] |
| **Browser Use** | AliExpress et DSers — tout ce qui exige une **session connectée** et une interface web vivante ; gestion des sessions. | Réplique le rôle de `claude-in-chrome` (partie 1.2-1.3). ⚠️ Blocage AliExpress rapporté dans certains environnements [INFO HAKIM] + `Browser Use rejected…` constaté [FAIT — codex-chasse-clusters/reports/validation-…-a1.md] : à requalifier avant de s'y engager |
| **Apify** | Extraction massive (recherche AliExpress à grande échelle, pages de résultats, lectures de fiches en lot). | **Aucun existant** — orientation exprimée, zéro trace dans le projet [FAIT — absence vérifiée, §1.7] |
| **Shopify API** | Produits, variantes, métachamps, SEO, médias, publication canaux, thème brouillon. | Déjà la voie nominale [FAIT — boutique-seiko-mod/journal/2026-07-31-branchement-galeries-codex.md ; boutique-seiko-mod/journal/2026-07-31-metachamps-montres.md ; boutique-seiko-mod/journal/2026-07-31-publication-grappes.md] |
| **DSers** | Vérité fournisseur : import, mapping variante↔fournisseur, coûts par variante, (à terme) commandes. | Partie 1.3 ; pas d'API publique utilisée — DSers reste piloté par Browser Use ou par l'app intégrée Shopify [FAIT] |

Règles transverses à conserver telles quelles : fail-closed sur toute donnée invérifiable ; sérialisation du navigateur ; DRAFT + aucun canal par défaut à l'import ; contrôles par compteurs avant/après ; jamais d'identifiants, de CAPTCHA ni de commande sans Hakim **[FAIT — partie 1]**.

### 2.2 Fonctions normalisées — contrats JSON

Conventions communes, fondées sur les données réellement manipulées :
- `item_id` : chaîne de chiffres **complète** (jusqu'à 16 caractères, préfixes réels jusqu'à `1005012…`) — jamais tronquée ni reconstruite **[FAIT — sourcing-accessoires-v3]**.
- `sku_chaine` : chaîne d'attributs AliExpress portée par les SKU DSers, ex. `14:200000914#M14`, `200000049:350853#steel-no logo;200000051:100016950`, `14:865#13pc Kits` **[FAIT — boutique-seiko-mod/journal/2026-07-31-import-accessoires-lot4.md ; scratchpad/noirmont-galeries/worklist.json]**.
- Les produits Shopify sont identifiés par `handle` + `sku_chaine` dans tout manifeste inter-outils — **jamais** par ID de variante/média (ils périment) **[FAIT — boutique-seiko-mod/journal/2026-07-31-prompt-codex-galeries.md]**. Les GID (`gid://shopify/Product/…`) ne servent qu'en interne d'un appel API.
- Toute sortie porte `releve_le` (ISO 8601) et `source` ; toute donnée vendeur est `annonce_par_vendeur: true` tant qu'elle n'est pas contrôlée sur échantillon **[FAIT — reports/phase4-*]**.
- Toute fonction peut rendre `{"statut": "BLOQUE", "erreur": {…}}` (voir modèle `erreur` du doc 09) au lieu de son résultat — jamais de résultat partiel silencieux **[FAIT — règle fail-closed]**.

---

#### `search_aliexpress_products()`
Cible : Browser Use (session) ou Apify (masse). Existant répliqué : recherche globale + in-store [FAIT — sourcing-accessoires-v3].

```json
{
  "entree": {
    "requete": "gravity water filter stainless steel",
    "portee": "globale | boutique",
    "store_id": "1102051418",
    "max_resultats": 40,
    "langue_devise": "fr.aliexpress.com / EUR"
  },
  "sortie": {
    "statut": "OK",
    "releve_le": "2026-07-30T21:00:00Z",
    "resultats": [
      {
        "item_id": "1005008291010462",
        "url": "https://fr.aliexpress.com/item/1005008291010462.html",
        "titre": "VEVOR Système de Filtration d'Eau par Gravité 8,5L ...",
        "prix_affiche_eur": 86.99,
        "note": 4.9,
        "nb_avis": 32,
        "nb_vendus": 127,
        "vendeur": "SucceBuy Appliance Global Store"
      }
    ]
  }
}
```

#### `extract_aliexpress_product()`
Cible : Browser Use ou Apify. Existant répliqué : extraction DOM d'une fiche `/item/` (recettes §1.2) [FAIT — sourcing-accessoires-v3 ; reports/phase4-*].

```json
{
  "entree": {
    "item_id": "1005004626900765",
    "adresse_reference": "France (code postal de référence)",
    "inclure_variantes": true
  },
  "sortie": {
    "statut": "OK",
    "releve_le": "2026-07-30T21:00:00Z",
    "fiche": {
      "item_id": "1005004626900765",
      "url": "https://fr.aliexpress.com/item/1005004626900765.html",
      "titre": "Tandorio CUSN8 Bronze/Stainless Steel 200m Waterproof Pilot PT5000 Japan NH",
      "vendeur": {
        "nom": "Tandorio Official Store",
        "pct_avis_positifs": 97.8,
        "abonnes": null
      },
      "preuve_sociale": { "note": 4.9, "nb_avis": 32, "nb_vendus": 127 },
      "variantes": [
        {
          "attributs": { "Color": "bronze case-no logo", "Size": "NH35-glass back" },
          "prix_eur": 78.25,
          "stock_affiche": 15
        }
      ],
      "livraison_france": {
        "entrepot": "France | UE | Chine",
        "delai_jours_min": 2,
        "delai_jours_max": 8,
        "cout_rendu_eur": 78.25
      },
      "caracteristiques_annoncees": { "annonce_par_vendeur": true, "detail": "inox 304, 8,5 L, 2 filtres céramique/charbon — non contrôlé sur échantillon" },
      "signaux_risque": ["logo possible sur produit livré", "variantes renommées en cours de vie"]
    }
  }
}
```

#### `compare_aliexpress_suppliers()`
Cible : Codex/Sol (raisonnement) sur sorties d'`extract_aliexpress_product()`. Existant répliqué : structure « fiche retenue / backups » + grille de confiance A/B/C des phases 4 [FAIT — reports/phase4-sourcing-fontaine-gravite-2026-07-20.md ; registre-candidats.md].

```json
{
  "entree": {
    "candidat": "fontaine-gravite",
    "fiches": ["<sortie extract_aliexpress_product>", "..."],
    "criteres": {
      "cout_rendu_max_eur": 150,
      "delai_france_cible_jours": 10,
      "priorite": "avis solides + entrepôt UE"
    }
  },
  "sortie": {
    "statut": "OK",
    "retenue": {
      "item_id": "1005008291010462",
      "confiance": "A",
      "motif": "seule à cumuler entrepôt France, 4.9/32 avis/127 vendus, vendeur ≥ 95 %, coût rendu le plus bas"
    },
    "backups": [{ "item_id": "1005010675449353", "confiance": "A" }],
    "ecartees": [{ "item_id": "1005012393505280", "motif": "stock 10, fiche neuve" }],
    "reserves": ["logo VEVOR possible sur la cuve livrée — contrôle commande test"]
  }
}
```

#### `import_product_to_dsers()`
Cible : Browser Use. Existant répliqué : Liste d'import URL par URL, ou IMPORT PRODUCTS FROM SHOPIFY par lots de 10 [FAIT — boutique-seiko-mod/journal/2026-07-31-import-accessoires-lot4.md ; boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md].

```json
{
  "entree": {
    "sens": "aliexpress_vers_dsers | shopify_vers_dsers",
    "urls_aliexpress": ["https://fr.aliexpress.com/item/1005007900051846.html"],
    "handles_shopify": ["bracelet-jubile-embouts-courbes"],
    "taille_lot_max": 10
  },
  "sortie": {
    "statut": "OK",
    "compteurs_avant": { "tous": 85, "aliexpress": 85, "unmapped": 0, "liste_import": 25 },
    "compteurs_apres": { "tous": 98, "aliexpress": 98, "unmapped": 0, "liste_import": 38 },
    "controle_arithmetique": "tous +13 = attendu ; unmapped inchangé — aucune fiche historique démappée",
    "importes": [{ "url": "…", "titre_fournisseur_lu": "…" }]
  }
}
```

#### `configure_dsers_variants()`
Cible : Browser Use. Existant répliqué : Mapping basique manuel, sélection déterministe, boîte « Appliquer le mapping » [FAIT — boutique-seiko-mod/journal/2026-07-25-dsers-mapping-decoupage.md ; boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md].

```json
{
  "entree": {
    "handle": "trente-neuf-bleu-classique-cannelee",
    "url_fournisseur": "https://fr.aliexpress.com/item/1005010776361944.html",
    "table_correspondance": [
      {
        "variante_shopify": "Miyota 8215 · 36 mm · fond acier",
        "sku_chaine": "14:xxx#blue no logo;5:yyy#8215-36mm(solidback)",
        "option_fournisseur": { "Color": "blue no logo", "Size": "8215-36mm(solidback)" }
      }
    ],
    "mode": "mapping_basique",
    "regles": ["texte strictement égal (===)", "refus si correspondances != 1", "relecture après sélection", "IGNORER sur Unsaved changes"]
  },
  "sortie": {
    "statut": "OK",
    "variantes_mappees": 8,
    "variantes_attendues": 8,
    "confirmation": "boîte Appliquer le mapping CONFIRMÉE ; bouton Enregistrer repassé désactivé",
    "controle_compteurs": { "unmapped_avant": 1, "unmapped_apres": 0 },
    "incidents": []
  }
}
```

#### `push_dsers_product_to_shopify()`
Cible : Browser Use. Existant répliqué : PUSH TO STORE, Draft coché, publication décochée [FAIT — boutique-seiko-mod/journal/2026-07-31-import-accessoires-lot4.md ; boutique-seiko-mod/journal/2026-07-31-sourcing-arabes-squelettes.md].

```json
{
  "entree": {
    "selection": ["<titres ou positions des cartes DSers à cocher>"],
    "options_modale": {
      "set_product_status_as_draft": true,
      "publier_dans_boutique": false,
      "taxable": true,
      "vente_en_rupture": true
    }
  },
  "sortie": {
    "statut": "OK",
    "produits_pousses": [
      {
        "titre_dsers": "…",
        "handle_shopify": "bracelet-jubile-embouts-courbes",
        "product_id": "10980388405586",
        "statut_shopify": "DRAFT",
        "canaux_publies": [],
        "nb_variantes": 15,
        "sku_exemple": "200000049:350853#steel-no logo;200000051:100016950"
      }
    ],
    "compteurs_apres": { "tous": 103, "aliexpress": 103, "unmapped": 0 }
  }
}
```

#### `update_shopify_product()`
Cible : Shopify API (GraphQL Admin). Existant répliqué : réécriture post-push (titre/handle/description/SEO/prix), métachamps `custom.*`, publication canaux, médias par staged uploads [FAIT — boutique-seiko-mod/journal/2026-07-31-import-accessoires-lot4.md ; boutique-seiko-mod/journal/2026-07-31-metachamps-montres.md ; boutique-seiko-mod/journal/2026-07-31-publication-grappes.md ; boutique-seiko-mod/journal/2026-07-31-branchement-galeries-codex.md].

```json
{
  "entree": {
    "handle": "eclaireur-bronze-field-36",
    "mutations": {
      "editorial": { "titre": "…", "description_html": "…", "seo": { "title": "…", "description": "…" }, "vendor": "Maison Noirmont", "tags": ["classiques"] },
      "prix": [{ "sku_chaine": "14:…#…", "prix_eur": 329.0, "prix_barre_eur": 428.0 }],
      "metachamps": { "custom.famille": ["Classiques"], "custom.calibre": ["NH35"], "custom.diametre": ["36 mm"], "custom.couleur_cadran": [] },
      "statut": "ACTIVE",
      "publier_sur_canaux": ["358599295314", "358599328082", "358599360850"],
      "medias": [{ "fichier": "/chemin/local/…-face.jpg", "alt": "<Titre> — face — Maison Noirmont", "position": 1 }]
    },
    "sauvegarde_prealable": "backup-avant-<operation>-<date>.json"
  },
  "sortie": {
    "statut": "OK",
    "verification": {
      "resource_publications_v2": "3/3 isPublished: true",
      "media_user_errors": [],
      "medias_ready": true,
      "metafields_relus": { "custom.famille": ["Classiques"] }
    }
  }
}
```

#### `verify_supplier_mapping()`
Cible : Browser Use (lecture DSers). Existant répliqué : contrôle par compteurs + relecture `supplyProductId` fiche par fiche [FAIT — boutique-seiko-mod/journal/2026-07-31-dsers-mapping-lot2.md ; boutique-seiko-mod/journal/2026-07-31-publication-grappes.md].

```json
{
  "entree": { "handles": ["…"], "table_fournisseurs_attendue": [{ "handle": "…", "item_id": "1005006938556690" }] },
  "sortie": {
    "statut": "OK",
    "compteurs": { "tous": 103, "aliexpress": 103, "unmapped": 0, "1688": 0, "alibaba": 0 },
    "controles": [
      { "handle": "…", "supply_product_id_lu": "1005006938556690", "conforme": true, "fournisseur_par_defaut": "IBBETON Luxury…", "favoris_surnumeraires": [] }
    ],
    "verdict": "aucune fiche sans fournisseur, aucun fournisseur surnuméraire, mapping vivant (fourchettes de coût affichées)"
  }
}
```

#### `verify_shopify_product()`
Cible : Shopify API. Existant répliqué : contrôles post-écriture systématiques (statut + canaux + SKU intacts + médias) [FAIT — boutique-seiko-mod/journal/2026-07-31-publication-grappes.md ; boutique-seiko-mod/journal/2026-07-31-branchement-galeries-codex.md ; boutique-seiko-mod/journal/2026-08-08-reprise-session.md §Pièges].

```json
{
  "entree": { "handle": "eclaireur-bronze-field-36", "attendu": { "statut": "ACTIVE", "canaux": 3, "nb_variantes": 6, "skus_inchanges": true, "nb_medias_min": 4 } },
  "sortie": {
    "statut": "OK",
    "constate": {
      "statut": "ACTIVE",
      "canaux_publies": [{ "id": "358599295314", "isPublished": true }],
      "variantes": [{ "titre": "…", "sku_chaine": "14:…#…", "prix_eur": 329.0 }],
      "medias": { "total": 5, "pagination_respectee": "requêtes média plafonnées à 30 — paginer", "statuts": "READY" },
      "collections": ["classiques", "montres"]
    },
    "ecarts": []
  }
}
```

---

### 2.3 Ce que la migration ne doit pas perdre

1. **Fail-closed partout** : une fonction qui ne peut pas prouver son résultat rend `BLOQUE`, jamais un chiffre estimé **[FAIT — specs pipeline]**.
2. **Contrôles avant/après par compteurs et relectures** — c'est ce qui a détecté chaque incident DSers avant enregistrement **[FAIT — dsers-mapping-*]**.
3. **Sauvegarde préalable avant toute mutation Shopify** (`backup-avant-*.json`) **[FAIT — boutique-seiko-mod/, nombreux fichiers]**.
4. **Manifestes indexés handle+SKU** entre briques **[FAIT — boutique-seiko-mod/journal/2026-07-31-prompt-codex-galeries.md]**.
5. **Frontière humaine** (identifiants, CAPTCHA, commandes, preuve sociale, republication) **[FAIT — §1.8]**.

### 2.4 Mise en œuvre : voir `14-PROTOCOLE-ORDRES.md`

Les 9 fonctions ci-dessus sont opérationnelles par fichiers via la **boîte aux lettres `boutique-pipeline/ordres/`** : Codex dépose des ordres JSON (enveloppe portant un `payload` = contrat d'entrée de §2.2), une session Claude Code les valide (`ordres/valider_ordre.py`), exécute selon trois classes d'autonomie (A lecture seule / B écriture Draft journalisée / C validation Hakim) et écrit les résultats (enveloppe portant le contrat de sortie de §2.2). Protocole complet, cycle de vie et prompt de dépouillement : `14-PROTOCOLE-ORDRES.md`.

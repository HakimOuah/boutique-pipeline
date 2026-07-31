# 10 — Échecs, pièges et leçons (FAILURES AND LESSONS)

> Dossier de passation Codex — Maison Noirmont (`v42pzp-h4.myshopify.com`) et pipeline « Boutiques drop ».
> C'est le fichier le plus riche de la passation : ce projet a une culture écrite du piège documenté.
> **Tout piège listé ici a été payé au moins une fois en production.**
>
> Étiquettes de source :
> - **[FAIT — repo:chemin]** : vérifié dans un livrable du dépôt (`repo:` = relatif à `boutique-pipeline/`).
> - **[MÉMOIRE]** : dossier mémoire `~/.claude/projects/-Users-Hakim-Documents-Boutiques-drop/memory/`.
> - **[NOTION]** : page « 🏕️ Campement type — Lancement boutique » (`3a71f38c-3154-81b8-8b28-d745e54efc05`), sections « ⚠️ Pièges vérifiés » (deux générations : passe des 25-26/07 et passe corrigée du 26/07).
> - **[MANQUANT]** : affirmé quelque part mais non retrouvé/vérifié — à re-vérifier avant d'en faire une doctrine.
>
> Format de chaque fiche : **Symptôme → Cause → Solution testée → Résultat → Solution recommandée → Prévention.**

---

## A. Sourcing AliExpress & DSers

### A1. Le CAPTCHA AliExpress était un artefact de session, pas une protection
**[FAIT — repo:boutique-seiko-mod/sourcing-accessoires-v3-2026-07-25.md §Notes de méthode]** **[NOTION]**
- **Symptôme** : les URL de recherche `/w/wholesale-*.html` servaient un challenge (`fr.aliexpress.com/wp.html`) ; la page chargeait ses images mais n'hydratait jamais son texte. Conclusion v2 (fausse) : « découverte par mot-clé impossible », confirmée « par les trois agents de recherche » (`sourcing-familles-v2-2026-07-25.md` l.24, `sourcing-accessoires-v2-2026-07-25.md` l.87).
- **Cause** : navigateur **sans session** (le navigateur d'aperçu isolé `mcp__Claude_Browser__`). Le blocage n'est pas une protection du site mais l'absence de session connectée.
- **Solution testée** : refaire les mêmes requêtes dans le **Chrome réel de Hakim** (`claude-in-chrome`, session AliExpress connectée).
- **Résultat** : **zéro CAPTCHA** — recherche globale 12-14 fiches, recherche intra-boutique (`/store/<id>/pages/all-items.html?SearchText=…`) 40 fiches. Aucun CAPTCHA jamais franchi : « le challenge a simplement disparu en changeant de navigateur ». Reconfirmé les 27/07 et 30/07 (`sourcing-chiffres-orientaux.md` : 14 requêtes, 0 CAPTCHA).
- **Recommandé** : **toujours utiliser le navigateur de l'utilisateur avec session pour AliExpress.** Entrée bonus : `/store/<id>?sortType=total_tranpro_desc` rend 30-40 fiches d'un coup.
- **Prévention** : ne jamais résoudre un CAPTCHA ; si un challenge apparaît, changer de navigateur/session avant de conclure à une limite. `BILAN-2026-07-25.md` l.40 : « la fausse limite aurait handicapé toutes les boutiques suivantes ».

### A2. « ~60 % de listings morts » = identifiants tronqués et préfixes devinés
**[FAIT — repo:boutique-seiko-mod/sourcing-accessoires-v3-2026-07-25.md §Notes de méthode]**
- **Symptôme** : ~60 % des IDs AliExpress remontés renvoyaient 404 ; « 5 des candidats les plus prometteurs » morts (`sourcing-familles-v2-2026-07-25.md` l.26).
- **Cause** : pour tenir dans la limite de sortie de l'extraction JS (~1 000 caractères), les identifiants (16 chiffres) avaient été **tronqués aux 9 derniers**, puis le préfixe **reconstruit au jugé** (`1005007`/`1005008`/`1005009`) — alors que les préfixes réels montent jusqu'à `1005012`. Les URL fabriquées rendaient 404 sur des produits vivants.
- **Résultat après correction** : le taux de listings réellement morts est « très faible ».
- **Recommandé** : **extraire les 16 chiffres complets, ne jamais deviner un préfixe** ; découper les retours JS avec `.slice()` ou faire deux appels.
- **Prévention** : toute statistique alarmante issue d'une extraction doit être re-vérifiée sur échantillon brut avant d'entrer dans un rapport.

### A3. L'auto-matching DSers par SKU n'existe pas
**[FAIT — repo:boutique-seiko-mod/dsers-mapping-decoupage-2026-07-25.md l.41 ; dsers-mapping-lot2.md l.168]** **[NOTION]**
- **Symptôme** : la doctrine attendue (« SKU identiques ⇒ auto-matching », écrite dans `plan-decoupage-coloris-2026-07-25.md` l.12 et `catalogue-v2-analyse-concurrents-2026-07-25.md` l.111) ne s'est jamais produite : coller l'URL fournisseur rattache le bon produit mais laisse **toutes les variantes vides**.
- **Cause** : DSers n'apparie seul que les libellés strictement identiques des deux côtés (`Miyota 8215`, `NH35`…). Le SKU n'est pas lu.
- **Solution testée** : lire les SKU via l'API Shopify (lecture seule), en faire une table de correspondance (`14:…`=Color, `5:…`=Size), puis apparier **à la main, option par option**, en sélectionnant l'option du DOM dont le texte est **strictement égal** (`===`, jamais `includes` — sinon `M-1`≠`M11`≠`M12` se confondent), refus si correspondances ≠ 1.
- **Résultat** : lot 1 **19/19 fiches, 92/92 variantes** ; lot 2 **41/41 fiches, 89/89 variantes**, `Unmapped` 41 → 0.
- **Pièges UI vérifiés** (tous payés) : listes **virtualisées** (9 options rendues sur 20 — scroller ET émettre l'événement `scroll`) ; boîte **« Appliquer le mapping »** à confirmer sinon rien n'est écrit ; **Chrome bride `setTimeout` à 1/min** quand l'onglet est en arrière-plan (temporiser via `MessageChannel`) ; import depuis Shopify **par lots de 10** via « Import products from Shopify » (additif) ; deux erreurs d'appariement produites par le clic aux coordonnées (les listes se repositionnent) → sélection par texte DOM uniquement.
- **Prévention** : les SKU restent la table de vérité (ne **jamais** les toucher), mais l'appariement est manuel. Vérifier l'enregistrement par les compteurs d'onglets (`Tous`/`AliExpress`/`Unmapped`).

### A4. Produit importé DSers/API = publié sur **aucun canal**
**[FAIT — repo:boutique-seiko-mod/build-site-2026-07-24.md l.12 ; publication-grappes.md l.29-31]** **[MÉMOIRE : shopify-canal-et-visuels-ia]** **[NOTION]**
- **Symptôme** : produits `ACTIVE` mais invisibles (« Aucun produit trouvé », sections collection vides). 25 produits + 7 collections concernés au build initial.
- **Cause** : DSers et l'API créent des ressources publiées sur 0 canal (`resourcePublications` vide) ; la case « Publier dans la Boutique également » de DSers est décochée par défaut.
- **Solution** : `publishablePublish` en batch sur les 3 publications (Boutique en ligne `358599295314`, POS, Shop), puis **vérification** `resourcePublicationsV2.isPublished = true`.
- **Faux positif connu** : `onlineStoreUrl: null` ne prouve rien tant que le storefront est sous mot de passe (`decoupage-coloris-lot1-2026-07-25.md` l.128).
- **Prévention** : après toute création/publication, contrôler les effectifs par canal — le statut `ACTIVE` ne suffit jamais.

### A5. Collections automatiques sensibles au singulier/pluriel
**[NOTION — passe du 26/07]**
- **Symptôme** : 13 fiches publiées portant `bracelet`/`outillage` restées hors de toute collection attendant `bracelets`/`outils` — visibles en direct, introuvables à la navigation.
- **Recommandé** : fixer une forme canonique d'étiquettes, contrôler les effectifs de collection après chaque publication. C'est aussi pour cela que les facettes doivent s'adosser à des **métachamps normalisés, jamais aux étiquettes** (vu chez un concurrent : « Mecanique » et « Mécanique » côte à côte).

### A6. Plafond de 30 médias par requête — un inventaire tronqué a failli épargner 13 photos fournisseur
**[FAIT — repo:boutique-seiko-mod/visuels-accessoires-lot4.md l.92-100]** **[NOTION]**
- **Symptôme** : inventaire de purge = 173 photos fournisseur ; réel = **186**. `bracelet-caoutchouc-gaufre` portait 43 médias, la requête plafonnait à 30 : 13 photos invisibles auraient survécu à une purge « complète ».
- **Détection** : recomptage par `mediaCount` sur les 13 fiches.
- **Recommandé** : paginer explicitement (`media(first:30)` + `pageInfo.hasNextPage`) et **boucler ses totaux** ; quand un chiffre sert de base à une purge, le recompter par une autre voie (contre-exemple propre : `audit-visuel-catalogue.md` l.40).

---

## B. API Shopify — écritures de thème et de données

### B1. `upsertedThemeFiles: []` — la doctrine a changé **deux fois**
**[FAIT — repo:boutique-seiko-mod/design-modernisation-2026-07-25.md l.178 ; fix-uiux-json.md l.9-12 ; passe-coherence-avant-publication.md §6.1]** **[NOTION — les deux générations]**
Évolution tracée, à connaître pour lire les vieux livrables :
1. **Doctrine v1 (25/07) — « rejet silencieux »** : après 90 s d'attente vaine sur un upsert, conclusion « `upsertedThemeFiles: []` ne veut pas dire "en cours", c'est un rejet silencieux ; re-interroger `size`/`updatedAt` » (`design-modernisation-2026-07-25.md` l.178-179, reprise au `BILAN-2026-07-25.md` l.43). Généralisation abusive : le cas déclencheur était en réalité le rejet du champ `custom_css` (B4), pas l'asynchronisme. Toute une passe a refait des écritures qui avaient abouti [NOTION 26/07 : « nous avions traité un comportement normal comme un rejet silencieux »].
2. **Doctrine v2 (26/07) — « écriture asynchrone normale »** : `[]` sans `userErrors` n'est **pas** un échec ; « c'est la relecture des empreintes qui la prouve » (`fix-uiux-json.md` l.11 ; réaffirmée les 27 et 30/07).
3. **Raffinements v2 (vérification)** : `size` et `updatedAt` **ne prouvent rien** (en-tête auto-généré de 363 o compté à la lecture mais pas stocké sur certains fichiers, template stocké minifié/renvoyé indenté, horloges divergentes, `updatedAt` bougeant par effet de bord des collections). **Comparer aux octets envoyés, jamais au contenu relu, puis relire pour confirmer** (`passe-coherence-avant-publication.md` §6.1 ; `fix-uiux-json.md` §« le piège de l'empreinte » : recette `rstrip(b'\n')` + md5). Deux restrictions confirmées : `[]` **avec** `userErrors` = vrai rejet (message explicite, `pages-collection-refonte.md` l.52) ; une réponse « connecteur injoignable » n'avait **rien écrit** — détecté par relecture (`fix-uiux-assets.md` l.23).
- **Prévention** : après toute écriture de thème ou de métadonnée, **relire ce qu'on vient d'écrire**. La forme de la réponse ne prouve rien, dans les deux sens. Corriger toute consigne héritée qui dit « vérifier par size/updatedAt ».

### B2. Un nœud `themeFiles` peut être étiqueté d'un nom et contenir un autre fichier
**[NOTION — passe du 26/07]** **[FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md l.89]**
- **Symptôme** : `files(filenames:[...])` a renvoyé un nœud étiqueté `templates/product.json` dont le contenu était celui de `templates/index.json`. Détecté **avant** écriture ; sans ce contrôle, un gabarit en écrasait un autre.
- **Prévention** : valider l'appariement nom ↔ contenu **par empreinte** avant toute réécriture.

### B3. Le caractère invisible — chaînes « introuvables »
**[NOTION]** **[FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md l.90]**
- **Symptôme** : une recherche/remplacement échoue sur une chaîne pourtant visible dans le fichier.
- **Cause** : apostrophe typographique `’` vs droite `'`, espace insécable vs espace avant `:` — un caractère invisible diffère.
- **Prévention** : relever la **convention réelle du fichier** avant de composer une recherche ; normaliser recherche **et** remplacement sur cette convention ; ne jamais introduire des caractères isolés d'une autre convention.

### B4. Rejets silencieux réels et confirmés du thème
**[NOTION]** **[FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md l.95]**
- Nom de schéma de bloc **> 25 caractères** → fichier rejeté sans message.
- Champ **CSS d'une section** → fichier rejeté sans message ; passer par un fichier d'asset.
- (Thème FullStack, 4 cas rencontrés au total avec B1/B5, tous sans message d'erreur.)

### B5. `productUpdate` + objet `seo` partiel : remplacement *wholesale* — 47 titres perdus
**[FAIT — repo:boutique-seiko-mod/reprise-editoriale-fiches-2026-07-25.md l.41-55]** **[NOTION]**
- **Symptôme** : une passe qui ne visait que les `seo.description` a **effacé les 47 `seo.title`** des fiches montres.
- **Cause** : envoyer `seo: { description }` seul met `seo.title` à `null` — Shopify **remplace** l'objet SEO au lieu de le fusionner.
- **Résultat** : les 47 titres ont été **restaurés** ; contrôle ultérieur : 60 titres uniques, 42-67 caractères. Le piège ne s'est pas rejoué (`verification-catalogue-strategie.md` l.156-157 : vérification avant écriture).
- **Prévention** : **toujours envoyer `title` et `description` ensemble** dans le même `productUpdate` ; relire après écriture.

### B6. `productSet` est destructif sur les champs de type liste
**[FAIT — repo:boutique-seiko-mod/branchement-visuels-lot3.md l.28]**
- **Symptôme évité** : pour les champs liste (`variants`, `files`), `productSet` « supprime les entrées existantes qui ne sont pas incluses ». L'utiliser pour attacher un média aurait pu effacer les variantes — donc les SKU et les mappings DSers.
- **Recommandé** : écarté délibérément ; utiliser `productCreateMedia` / `productVariantAppendMedia` / `productReorderMedia`. (`productUpdate` n'accepte pas `files` — erreur API.)

### B7. Médias partagés entre produits — le piège le plus coûteux
**[NOTION — « 31 textes alternatifs détruits en une passe »]** **[FAIT — repo:boutique-seiko-mod/decoupage-elagage-lot2.md l.10-33 ; reduction-meres-et-galeries.md ; branchement-visuels-lot3.md ; visuels-aviateur-consolidation.md §8.1]**
- **Symptôme** : rattacher une image existante en passant son URL CDN dans `originalSource` ne crée **pas** de copie : Shopify reconnaît l'URL et rattache le **même objet `MediaImage`**. L'`alt` étant une propriété du **fichier**, pas du rattachement, chaque création a réécrit l'alt partagé — **31 alt détruits en une passe** (les 7 mères), réparés via `fileUpdate` avec le titre de la mère, mais **textes d'origine perdus, non récupérables** (`decoupage-elagage-lot2.md`).
- **Sémantique de suppression, établie sur pilote** (`reduction-meres-et-galeries.md`) : malgré son nom, `productDeleteMedia` **détache** quand le fichier est référencé ailleurs (pilote sur 1 média : mère et sœurs intactes ; 181 détachements, 0 suppression) — mais **supprime définitivement** un média non partagé (`visuels-aviateur-consolidation.md` §8.1 : triple vérification de non-partage AVANT de supprimer les 16 médias de plongeuse, sauvegardés d'abord — `backup-medias-partages-2026-07-26/` 31 JPEG, `backup-medias-plongeuse-supprimes-2026-07-27/` 16 JPEG + MANIFESTE).
- **Nuance vérifiée sur pilote** (`branchement-visuels-lot3.md`) : `productCreateMedia` + `originalSource` sur un fichier déjà en ligne du CDN de la boutique a créé un `MediaImage` **indépendant** (fichier suffixé UUID), alt de la mère intact — vérifier sur pilote avant de généraliser, et poser un `alt` strictement identique par précaution.
- **Recommandé** : pour rattacher un fichier existant sans effet de bord, `files: [{id: "gid://shopify/MediaImage/…"}]`, jamais `originalSource` + `alt` ; toujours vérifier le partage (index des URL CDN + `files(query:"filename:…")`) avant toute suppression.

### B7bis. Images de variantes cachées derrière une purge — 56 liaisons sur 80 médias
**[FAIT — repo:boutique-seiko-mod/sourcing-arabes-squelettes.md §5 ; visuels-aviateur-consolidation.md §8.1c]**
- **Symptôme** : sur le lot des 5 fiches des grappes (29/07), purger les **80 photos AliExpress** aurait laissé **56 liaisons variante→média pointer sur un média détruit** — un média de galerie peut être, invisiblement, l'image de dizaines de variantes. Même piège découvert sur l'aviateur : `c-558930-acier.jpg` n'était pas qu'un média de galerie, c'était l'image des 6 variantes de la fiche.
- **Solution** : sauvegarde locale des 80 (manifest TSV, 0 doublon md5, partage inter-fiches exclu), **réaffectation des 194 variantes survivantes vers la face maison AVANT le retrait**, puis `productDeleteMedia` — « 80/80 supprimées, aucune photo AliExpress ne survit ».
- **Prévention** : avant toute suppression de média, inventorier les liaisons variante→média et réaffecter d'abord ; rappel du thème : sans image liée à la variante, le clic ne change pas la galerie (`PLAN-lisibilite-variantes-2026-07-25.md` l.58). Corollaire du découpage : les **80 médias restés sur les 7 mères en brouillon** sont invisibles en vitrine et jugés non récupérables (0/6 au contrôle visuel — voir D1) (`audit-visuel-catalogue.md`).

### B8. Renommer un handle par API ne crée **pas** de redirection
**[FAIT — repo:boutique-seiko-mod/publication-grappes.md §7 l.426-510 ; plan-nommage-seo.md l.221-238]**
- **Symptôme** : après le renommage « chiffres arabes » → « à chiffres », Shopify n'avait posé **aucune** redirection (`redirectNewHandle` non passé). Les 5 redirections existantes de la boutique avaient déjà toutes dû être créées à la main.
- **Solution** : 5 `urlRedirectCreate` (1 collection + 4 fiches), testées en session (200 sur la nouvelle URL). `plan-nommage-seo.md` prévoit **6 redirections à poser à la main** pour la phase de renommage suivante.
- **Prévention** : tout renommage de handle = redirection explicite + test.

### B9. Les menus Shopify sont partagés entre thèmes
**[NOTION]** **[FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md l.93 ; passe-coherence-avant-publication.md §5.5]**
- Modifier un menu pour le thème brouillon le modifie aussi pour le thème publié. **Créer un menu neuf, ne pas modifier l'existant.** (C'est aussi pourquoi le libellé « CONFIGURATEUR » du menu est resté une décision de Hakim.)

### B10. Search & Discovery : iframe d'une autre origine, non automatisable, pas d'API
**[FAIT — repo:boutique-seiko-mod/metachamps-montres.md §1]** **[NOTION]**
- **Symptôme** : les facettes de vitrine ne se règlent ni dans le thème ni par l'API. L'app est servie dans une iframe `search-and-discovery.shopifyapps.com` (`sameOrigin: false`) : l'arbre d'accessibilité s'arrête au bord, les clics synthétiques ne traversent pas, l'URL directe `/filters/new` rend une page vide, le contrôle bureau est refusé sur les navigateurs.
- **Vérifié en plus** : créer une définition de métachamp filtrable **ne suffit pas** — l'application doit ajouter la facette explicitement. Si la vitrine ne propose que « Disponibilité + Prix », c'est le signe de facettes non configurées (ou app absente), pas un mauvais réglage de thème.
- **Recommandé** : préparer la donnée (métachamps normalisés) et **remettre les 5 gestes à faire au marchand** (voir 11-OPEN-TASKS §Business).

### B11. Divers écritures — règles confirmées
**[NOTION]** **[FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md]**
- **Ne jamais utiliser `switch-shop`** sur le connecteur Shopify MCP : il invalide la connexion pour tout le monde (seule une ré-autorisation OAuth par Hakim la restaure).
- Le connecteur **refuse d'écrire sur un thème MAIN**, quelle que soit l'autorisation — travailler sur le thème brouillon, Hakim publie. [MÉMOIRE : mobile-first-et-placeholders-demo §4]
- Requêtes variantes : `first:250` + pagination par curseur (la « limite 100 » est obsolète, Shopify accepte 2048 variantes).
- Résultats MCP > ~25k tokens → sauvegarder sur disque et parser localement.
- Swatches : donnée Shopify, pas du thème — champ `swatch` en lecture seule, passer par les **métaobjets liés à l'option** (`dial-color`/`case-color` pour la catégorie Montres ; `color-pattern` refusée) + une image par variante sinon le clic ne change pas la galerie.

---

## C. Génération d'images IA

### C1. `soul_2` imprime de faux logos — le mauvais modèle était la cause racine
**[FAIT — repo:boutique-seiko-mod/images-modeles-et-coloris-2026-07-25.md §1]** **[MÉMOIRE : shopify-canal-et-visuels-ia]**
- **Symptôme** : la première fournée de 35 images (Higgsfield Soul 2.0) portait des faux logos sur les cadrans — toute une boucle de détourage/retouche perdue. Les prompts « no logo, no text » ne suffisent pas.
- **Cause** : `soul_2` est un modèle UGC/éditorial mode — il fabrique du branding parce que ses références en portent. **Proscrit pour tout packshot.**
- **Solution testée** : bake-off de 5 modèles (26,5 crédits) sur la tâche réelle (changer seulement la couleur du cadran) → retenu **`nano_banana_pro` 4K** (4 cr, 4096 px, écart hors-cadran 4,18). `openai_hazel` **éliminé** : il a inventé un « XII » typographié et une trotteuse inexistante — les modèles d'« édition » peuvent **réinventer l'objet**.
- **Recette de secours** (héritée) : compositions qui cachent le cadran (angle rasant, macro lunette, caseback, knolling) + inpainting OpenCV local sur zones de texte. **Vérifier chaque image à l'œil avant upload.**

### C2. « SWISS MADE » a passé trois contrôles — les planches à 380 px ne montrent pas un micro-lettrage
**[FAIT — repo:boutique-seiko-mod/branchement-galeries-codex.md l.23]**
- **Symptôme** : 6 faces à mention « SWISS MADE » **déjà publiées** malgré les contrôles de stérilité précédents.
- **Cause** : les contrôles se faisaient sur des planches de contact à **380 px par vignette** — le texte est physiquement présent mais indiscernable, et il passe.
- **Solution recommandée** : contrôler sur planche **≥ 1240 px** avec recadrage de l'arc 4h-8h ; en programmatique, passe-haut `gray − gaussien(σ=3)` avec mesure d'énergie dans les empreintes exactes du lettrage (recette dans le même fichier, l.257).
- **Prévention** : un contrôle visuel a la résolution de son support. Dimensionner le support au défaut cherché.

### C3. Le gommage est impossible : le modèle **atténue** au lieu de supprimer
**[FAIT — repo:boutique-seiko-mod/branchement-galeries-codex.md l.168-191]**
- **Symptôme** : deux passes de « gommage » du SWISS MADE (15 images) — échec sur les deux : il reste aux emplacements exacts un **fantôme** dont la forme des lettres est reconnaissable au zoom. Même mode d'échec que les taches de flou relevées sur 6 autres faces du catalogue (« floutage plutôt que suppression »).
- **Règle** : *un lettrage atténué compte comme un lettrage présent.*
- **Solution qui marche** : **repartir d'une face déjà propre de la même famille** et ne changer que la couleur du cadran (technique de la passe de coloris) → 5/5 cadrans stériles, ΔE et organes (12 index, 3 aiguilles, guichet) vérifiés un à un.
- **Prévention** : « régénérer plutôt qu'inpainter » [NOTION] ; la retouche sur cadran sombre laisse des voiles visibles.

### C4. L'orientation est le défaut n°1 du modèle d'image
**[FAIT — repo:boutique-seiko-mod/visuels-aviateur-consolidation.md l.96, l.253-257]**
- **Symptôme** : sur un chantier où cadran, chiffres et aiguilles sortaient justes du premier coup, les **deux seuls échecs** ont été l'orientation : montre dressée debout couronne en haut (cadran lisible à 90°), puis macro **cadran à l'envers** (couronne en bas à gauche, chiffres tête-bêche).
- **Solution testée** : bloc « **MANDATORY ORIENTATION** » dans le prompt (à plat, triangle à 12h en haut, couronne à droite) — efficace au premier essai, deux fois.
- **Prévention** : inclure systématiquement le bloc d'orientation dans tout prompt de mise en situation ; contrôler l'orientation en QA au même titre que le lettrage.

### C5. Divers génération — règles confirmées
**[NOTION]** **[MÉMOIRE : promesses-verifiables-guide-numerique]**
- Coût réel des générations 4K : **~30 % au-dessus** du tarif annoncé par l'API.
- Ne jamais montrer un produit **en fonctionnement** en vidéo générée : l'IA rate la mécanique observable, le public d'un hobby le détecte immédiatement. QA des clips = physique du produit, pas seulement DA.
- Les images de synthèse « fidèles » restent des extrapolations : contrôler contre la photo fournisseur, et le dire quand la teinte (bronze qui patine) n'est pas garantie (`visuels-aviateur-consolidation.md` §7).

---

## D. Catalogue, données produit & véracité

### D1. Le SKU ne prouve pas l'identité visuelle
**[NOTION — contrôle 6 mères / 6 échecs]** **[FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md l.92]**
- **Symptôme** : après un découpage de coloris, la galerie de la fiche mère date d'avant le découpage. Contrôle sur 6 mères : **6 échecs** (cadran crème là où la fille est argent, cuir brun 4 places là où la fille est bleu 3 places).
- **Prévention** : vérifier les images **à l'œil** avant tout rattachement, jamais sur la seule correspondance de SKU.

### D2. La fiche peut ne pas montrer le produit livré — mapping juste, fiche fausse
**[FAIT — repo:boutique-seiko-mod/verification-catalogue-strategie.md §5]**
- **Symptôme** : `noirmont-deux-plongeuse-ceramique` — mapping DSers vérifié **exact** (7 références + 4 calibres, un pour un), mais la fiche montre une plongeuse **noire céramique** alors que le fournisseur livrera, pour les 7 références sans exception, un **cadran bleu ciel à bulles multicolores**. Deux montres différentes. Même défaut trouvé au passage sur 2 autres fiches (ex-plongeuses devenues aviateurs).
- **Décision prise** : la valeur `couleur_cadran = Noir` (écrite d'après les visuels) a été **retirée** — « une facette fausse est pire qu'une facette incomplète ». Fiche laissée en brouillon, à trancher.
- **Prévention** : la vérité d'une fiche = **photos fournisseur du listing mappé**, pas la galerie Shopify ni le SKU. Après tout découpage/réécriture, re-vérifier fiche par fiche ce que le fournisseur expédie.

### D3. Variantes `-logo` : la stérilité se garantit au niveau de la **variante**, pas de la fiche
**[FAIT — repo:boutique-seiko-mod/sourcing-arabes-squelettes.md §5 ; variantes-logo-supprimees-*.tsv]**
- **Symptôme** : les listings Tandorio/Corgeut déclinent chaque coloris en version logotée **et** `-sterile`. Publier la fiche entière aurait vendu des montres à logo.
- **Solution** : **78 variantes logo supprimées** (272 → 194 ; TSV de sauvegarde acier 61 lignes + bronze 19 lignes, 29/07) après sauvegarde complète ; mapping limité aux coloris `-sterile`. Les 12 variantes GMT « siglé » de la mère `voyageur-gmt-automatique` restent en `DENY`/stock 0, jamais publiées ; 4 cadrans arabes « Logo S » documentés comme **contrefaçon probable, jamais vendus** (`sourcing-configurateur.md` l.226).
- **Prévention** : ne jamais supprimer une **valeur d'option** pour réduire des fiches (ça détruit le mapping) — supprimer/fusionner des **variantes** après sauvegarde (id, SKU, prix, options, inventaire) : c'est le seul filet. [NOTION]

### D4. Promesses invérifiables — l'audit qui a réécrit le site
**[FAIT — repo:boutique-seiko-mod/audit-promesses.md ; passe-coherence-avant-publication.md §5 ; REPRISE-SESSION.md l.77-81]**
Constats payés (0 commande, 0 client réels) :
- « **2 000 clients satisfaits** », trois `review_count: 123`, badge « **1340 avis** » (au passage : invisible, encre sur encre 1,00:1) → *misrepresentation*, motif documenté de suspension Merchant Center (cas Bien Brûlé). **Domaine réservé de Hakim** — proposer, ne jamais figer. [MÉMOIRE : mobile-first-et-placeholders-demo]
- « **Plongeuse** » dans 3 titres Héritage alors qu'elles sont à 5 bar (nage exclue) — requalifié en « style plongeuse » dans les corps de texte et le SEO (`reprise-editoriale-fiches-2026-07-25.md` l.238).
- 11 fiches promettaient « 10 bar : douche, piscine et baignade sans souci » (`audit-promesses.md` l.166) ; saphir/904L non prouvés fournisseur ; chronos « automatiques » alors que le **VK63 est méca-quartz à pile** — toute formule globale devient fausse dès qu'un chrono entre au catalogue : vérifier la nature du mouvement **par famille**. [NOTION]
- Images sur-promettant la **capacité** : 4 rouleaux et 5 meubles montrent plus d'emplacements que vendus.
- Marques tierces : fabricant de composant réellement installé = **autorisé** (Seiko NH35, Miyota 8215) ; marque de design = **interdit** ; attention à la portée grammaticale (« Seiko NH34 ou DG3804 » → inverser : « Calibre DG3804 ou Seiko NH34 »). [NOTION]
- Dropshipping : rien n'est « inclus dans le colis » — tout bonus est « offert / accès inclus », livré en numérique. [MÉMOIRE : promesses-verifiables-guide-numerique]
- **Prévention** : promesse = vérifiable ou supprimée. Le badge « En promotion » a été retiré ; vérifier la règle française du prix de référence (30 jours) avant toute remise affichée.

### D5. « Montre squelette » (≈ 8 400/mois) était un mirage catalogue
**[FAIT — repo:boutique-seiko-mod/verification-catalogue-strategie.md §1]**
- **Symptôme** : la mesure SEMrush avait assimilé « squelette » à notre « fond verre » (`mots-cles-semrush.md` l.222 — rangé lui-même en « supposé », pas mesuré). Vérification sur pièces : **0 fiche sur 53** — « fond verre » est une valeur d'option de *fond de boîtier*, jamais un cadran ; les 53 visuels ont un cadran plein ; recherche plein texte 0 occurrence (validée par mot témoin `cramoisi`).
- **Résultat** : écrire « squelette » sur une fiche à fond verre aurait été une affirmation fausse visible au déballage. **Il a fallu sourcer** : 2 vraies fiches squelette NH70 créées le 29/07 + collection avec description pédagogique squelette vs fond verre.
- **Prévention** : un mot de grappe SEO ne s'applique au catalogue qu'après vérification produit par produit.

### D6. « Chiffres arabes » — l'ambiguïté occidental/oriental a atteint la vitrine
**[FAIT — repo:boutique-seiko-mod/publication-grappes.md §7 ; sourcing-chiffres-orientaux.md]**
- **Symptôme** : la grappe `arabic dial` (≈ 15 500/mois) a été servie avec des cadrans à chiffres **occidentaux** (1-12, sens horloger de « chiffres arabes »). Techniquement juste, mais un visiteur francophone comprend des chiffres **orientaux** (١ ٢ ٣) — que nous ne vendons pas. **Hakim l'a constaté sur la vitrine**, alors que la distinction était déjà écrite dans un livrable antérieur (`visuels-aviateur-consolidation.md` l.195).
- **Correction (30/07)** : collection renommée « Cadrans à chiffres » (handle `montre-cadran-a-chiffres`), 4 fiches sur 5 renommées « à chiffres 1-12 », paragraphe de levée d'ambiguïté, 5 redirections posées, configurateur rejoué (59 handles, 0 mort). **Reliquat** : alt de médias et noms de fichiers CDN portent encore « chiffres arabes » (médias gelés — voir 11-OPEN-TASKS).
- **Sur AliExpress, même piège inversé** : « arabic numerals » désigne presque toujours les chiffres occidentaux ; les vrais orientaux ne remontent que via `urdu`, la requête **en arabe** (`ساعة أوتوماتيك أرقام عربية`, 35/60 pertinents) et « Articles similaires ».
- **Prévention** : quand un mot de grappe a deux lectures, trancher la lecture **du client**, pas celle du jargon — et vérifier le rendu en vitrine avec les yeux du visiteur.

### D7. Découpage de catalogue — règles payées
**[NOTION]** **[FAIT — repo:boutique-seiko-mod/decoupage-*.md]**
- Découper **par modèle**, garder en variante ce qui est une **dimension** (une couleur est un modèle, une capacité ou une largeur est un choix).
- Chaque fiche fille **hérite du texte de sa mère** écrit pour une gamme : purger les renvois à des choix qu'elle n'offre plus, lui donner des métadonnées SEO uniques.
- Ne pas rattacher les filles à la collection de la page d'accueil (inondée).
- Une phrase peut désigner le **client** et non le produit : « si vous portez d'habitude du 38 ou 39 mm » parle du poignet — un traitement automatique y aurait lu un diamètre.

---

## E. Mesure, audits & outillage

### E1. Un contraste se **mesure sur le rendu**, jamais déduit d'une valeur de couleur
**[FAIT — repo:boutique-seiko-mod/fix-uiux-assets.md l.166-199 ; charte-ab-application.md]** **[NOTION]**
- **Symptôme** : deux corrections/audits faux parce que les ratios étaient calculés depuis les valeurs `color` au lieu d'être composés avec l'**opacité héritée** et la chaîne de fonds réelle. La correction du prix barré a dû être « refaite et mesurée ».
- **Chiffre à retenir** : le cyan accent `#22D3EE` ne vaut que **1,72:1 sur fond clair** — il ne porte jamais d'information (couleur d'instrument uniquement, jamais bouton ni badge).
- **Prévention** : composer alpha + fond, mesurer sur le rendu (mêmes règles pour le diagnostic : le §4 de `passe-coherence` a montré qu'un diagnostic « anneau de focus fautif » était lui-même erroné — re-mesurer avant de corriger).

### E2. SEMrush : quota épuisé = « 0 mot clé » **sans erreur**
**[FAIT — repo:boutique-seiko-mod/mots-cles-semrush.md §0 ; marche-complet-semrush.md §0]**
- **Symptôme** : en formule gratuite, 4 requêtes (`montre sans logo`, `nh35`, `montre plongeuse`, `seiko mod`) rendues « Tous les mots clés : 0 », tableau vide, aucune erreur — quatre zéros qui ne veulent rien dire.
- **Solution** : **mot-clé témoin** volontairement massif (`chaussures`) — s'il rend 0, c'est le quota, pas le marché. Généralisé en double témoin (`chaussures` pour l'outil mots-clés, `cdiscount.com` pour la recherche publicitaire) : permet de distinguer « absence réelle d'annonces » d'une panne de rapport, et « NON MESURÉ » d'un vrai zéro.
- **Prévention** : jamais de volume 0 dans un rapport sans témoin validé dans la même session.

### E3. Le navigateur est une ressource unique partagée
**[NOTION]**
- Orchestrateur et agents se marchent dessus sur le même Chrome : **sérialiser**, ou utiliser deux navigateurs distincts (navigateur intégré / Chrome). Corollaire du 29/07 : la session Chrome peut être **sur le mauvais compte** (contrôle DSers reporté pour cette raison — `sourcing-arabes-squelettes.md` l.10).

### E4. Iframes cross-origin d'admin : non pilotables
**[FAIT — repo:boutique-seiko-mod/metachamps-montres.md]** **[MÉMOIRE : import-avis-trustoo-bookmark, mobile-first-et-placeholders-demo]**
- Search & Discovery, éditeur de thème, apps embarquées (Trustoo) : ni clics ni clavier ne traversent. Chemins restants : donner à Hakim la manip exacte (1 min, fiable), passer par une page standalone de l'app (recette Trustoo par `postMessage`), ou dupliquer/patcher par API.
- Piège d'outillage associé : le retour de `javascript_tool` est **bloqué** si la chaîne contient `=` ou `&` (« BLOCKED: Cookie/query string data ») → renvoyer des statuts en lettres ; jamais `location.href` avec query string.

### E5. `resize_window` peut mentir
**[FAIT — repo:boutique-seiko-mod/publication-grappes.md §7]**
- **Symptôme** : `resize_window` répond « Successfully resized » mais `innerWidth` reste 1710 ; iframe et popup bloquées par le CSP Shopify → **aucun rendu 375 px n'a jamais été réellement produit par un agent** sur cette boutique. Les audits mobiles sont des mesures et reproductions DOM, pas des rendus.
- **Prévention** : vérifier `innerWidth` après tout resize ; tant que ce n'est pas fait, dire « non vu » plutôt que « conforme » (cf. tâche QA mobile dans 11-OPEN-TASKS).

### E6. Apify : un run « Succeeded » peut ne contenir que des fiches bloquées
**[OBSERVÉ — Chrome/Apify Console, runs `VBc7BfR8JoFa9QPjc` et `Hvk3VN4KQ288uYei1`, 31/07/2026]**
- **Symptôme** : l'Actor `khadinakbar/aliexpress-all-in-one-scraper` a terminé vert avec **2 résultats facturés 0,004 $**, alors que les deux enregistrements portaient `_warnings=["detail_page_blocked_anti_bot"]` et avaient titre, prix, note, commandes, vendeur, variantes et spécifications à `null`.
- **Piège associé** : l'Actor de recherche `khadinakbar/aliexpress-product-search-scraper` a publié 19 résultats uniquement après bascule automatique sur un autre Actor ; ses premiers résultats étaient hors cible sémantique et les vendeurs manquaient. Le statut terminal et le nombre de lignes ne prouvent donc ni la pertinence ni la profondeur.
- **Prévention** : après chaque run, contrôler les champs obligatoires et `_warnings`, compter les fiches réellement exploitables, relever les éventuels fournisseurs de repli, puis décider sur cette qualité — jamais sur `Succeeded`, le compteur du dataset ou la facturation. Aucun CAPTCHA ne doit être résolu ; une ligne bloquée reste **MANQUANTE** et Apify ne devient jamais une preuve fournisseur.

---

## F. Leçons transversales

1. **Mesurer sur le rendu, pas sur la valeur déclarée.** Contrastes (opacité héritée), tailles de thème (octets réellement écrits), planches d'images (380 px ne montrent pas un micro-lettrage), volumes SEMrush (témoin). La donnée déclarative — `size`, `updatedAt`, un SKU, un prompt « no logo » — ne prouve rien.
2. **Vérifier par plusieurs voies indépendantes.** Chaque purge/publication recomptée autrement : `mediaCount` vs inventaire, `resourcePublicationsV2` vs statut, compteurs DSers vs impression d'enregistrement, empreinte MD5 vs réponse API, mot témoin vs zéro suspect.
3. **Une réponse sans erreur ne prouve pas l'écriture ; une erreur apparente ne prouve pas l'échec.** Les deux sens du même piège : `upsertedThemeFiles: []` (succès pris pour échec) et la boîte « Appliquer le mapping » (échec pris pour succès). Relire ce qu'on vient d'écrire, toujours.
4. **« Techniquement impossible » n'est une doctrine qu'après revalidation dans d'autres conditions.** Deux fausses limites inscrites puis corrigées (CAPTCHA AliExpress, 60 % de listings morts) ; `journal-nuit-2026-07-25-suite.md` : « une fausse limite coûte plus cher qu'une passe de plus ». Symétriquement, une **vraie** limite documentée (iframe cross-origin, gommage impossible) épargne des heures — d'où l'importance de distinguer les deux par la preuve.
5. **Un agent qui refuse une autorisation mal fondée a raison.** Le connecteur qui refuse d'écrire sur un thème MAIN, l'agent qui ne franchit pas un CAPTCHA, celui qui ne publie pas hors mandat, celui qui retire une facette « Noir » plutôt que de deviner : chaque refus documenté a évité un incident. Le corollaire : baliser explicitement les domaines réservés de Hakim (preuve sociale, publication, prix, réglages de compte) et s'y tenir.
6. **La vérité produit vit chez le fournisseur, pas dans la fiche.** SKU ≠ identité visuelle ; galerie ≠ produit livré ; « chiffres arabes » ≠ ce que le client comprend ; « squelette » ≠ fond verre. Toute promesse se vérifie sur le listing mappé et les photos fournisseur.
7. **Sauvegarder avant de détruire, à chaque fois.** Tous les incidents récupérés l'ont été grâce aux `backup-*.json`/TSV écrits **avant** la première mutation. C'est la règle la moins chère du dossier.
8. **Écrire le piège immédiatement, avec ses chiffres.** Ce fichier n'existe que parce que chaque passe a documenté ses erreurs à chaud (sections « Notes de méthode », « pièges », journaux de nuit) — y compris les erreurs de l'agent lui-même. Codex doit maintenir cette culture : un piège non écrit sera payé deux fois.

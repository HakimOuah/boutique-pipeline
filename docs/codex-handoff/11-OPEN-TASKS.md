# 11 — Backlog priorisé (OPEN TASKS)

> Dossier de passation Codex — Maison Noirmont (`v42pzp-h4.myshopify.com` / maisonnoirmont.fr), au **30/07/2026**.
> Boutique **sous mot de passe, 0 commande, 0 client**. Thème de travail « Maison Noirmont » `204248088914` **UNPUBLISHED** ; le public voit encore Helio `204246548818`.
> Source principale : **[FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md]** (« Ce qui attend Hakim ») + les fins de livrables des 26-30/07 (`plan-nommage-seo.md` §5 « Ordre d'exécution », `publication-grappes.md` §5/§7, `seo-titles-produits.md` §8, `passe-coherence-avant-publication.md` §5, `sourcing-chiffres-orientaux.md`, `configurateur-implementation.md` §9, `pages-legales-et-delais.md`, `import-accessoires-lot4.md`). Étiquettes : [FAIT — repo:…], [MÉMOIRE], [NOTION], [MANQUANT].
>
> Priorités : **P0** = bloquant lancement/légal · **P1** = avant toute pub payante · **P2** = important, non bloquant · **P3** = opportunité.
> « Validation humaine » = un humain doit décider ou exécuter (domaine réservé, irréversible, ou hors de portée des agents).

---

## 1. Bugs

### BUG-0 — Tuftéo public sert 6 avis fictifs « Vérifié » + un compteur de 789 avis
- **Description** : l'audit public du 30/07 à 23:35 a confirmé que la purge n'a pas été faite. La home sert Camille R./Léa M./Sarah D. ; la fiche `kit-tufting-complet` sert Manon T./Julie B./Chloé P. Ces six avis sont ceux que `project-state.md` marque explicitement fictifs, mais le rendu public leur attribue « Vérifié ». La home et la fiche servent aussi « Excellent — 4,8/5 basé sur 789 avis », alors que le journal documente 169 avis Trustoo importés et qualifiait le badge de placeholder. Vérification indépendante par Browser Use en `375 × 812` et HTML public sans cookie (HTTP 200). [FAIT — repo:`boutique-tufting/project-state.md` + navigateur/HTTP public 2026-07-30]
- **Priorité** : **P0**. **Impact** : bloquant GMC/misrepresentation sur un site déjà public. **Difficulté** : faible.
- **Dépendances** : domaine réservé exclusif de Hakim (preuve sociale).
- **Critères d'acceptation** : zéro occurrence publique des six noms ; zéro libellé « Vérifié » sur un avis fictif ; zéro compteur non étayé ; contrôle déconnecté sur la home et la fiche kit.
- **Statut** : **CONFIRMÉ PUBLIC, NON CORRIGÉ**. Pris en charge par Hakim le 30/07/2026 ; correction et contrôle déconnecté encore non vérifiés. **Outil** : Hakim / éditeur de thème ou thème brouillon republié. **Validation humaine** : **oui, exclusive**.
- **Preuves** : `boutique-tufting/audit-avis-demo-publics-2026-07-30.md` + enregistrement Browser Use local cité dans le rapport.

### BUG-1 — Faces « SWISS MADE » : 3 corrigées, reliquat en ligne + 6 cadrans à taches de flou
- **Description** : 6 faces à micro-lettrage « SWISS MADE » avaient passé 3 contrôles (planches à 380 px/vignette, illisibles). La voie « gommage » est un échec démontré (2 passes, 15 images, 60 cr : le modèle atténue au lieu de supprimer) ; la voie validée est la **régénération depuis une face propre de la même famille** (5/5 stériles, mesure passe-haut). **3 faces v3 déjà branchées** (`trente-neuf-bleu`, `-rouge`, `-vert`, anciennes reléguées en fin de galerie, sauvegardées dans `backup-faces-swissmade-2026-07-26/`). **Reliquat** : `trente-neuf-rose` et la mère `trente-neuf-classique-cannelee` gardent leur SWISS MADE en position 1 (v3 validées mais consigne contradictoire non tranchée — elles étaient dans les 4 fiches écartées ; dissonance : la v3 de la mère affiche 23 au guichet contre 28 chez les sœurs) ; `noirmont-deux` (fragment « …TS SS ») jamais traité (interdiction) ; 6 cadrans à taches de flou (lettrage masqué, pas retiré) restent en ligne. [FAIT — repo:boutique-seiko-mod/branchement-galeries-codex.md l.23, l.168-228, l.461]
- **Priorité** : P1 (véracité produit — une mention d'origine suisse sur du dropshipping est une allégation d'origine fausse). **Impact** : fort. **Difficulté** : moyenne (recette validée, ~4 cr/face).
- **Dépendances** : arbitrage Hakim sur le reliquat (rose + mère + Noirmont Deux), crédits Higgsfield (~87).
- **Fichiers** : `boutique-seiko-mod/branchement-galeries-codex.md` (recette + contrôle passe-haut l.257), `backup-faces-swissmade-2026-07-26/`, `scratchpad/noirmont-galeries/faces-steriles-v2/`.
- **Critères d'acceptation** : plus aucune face publiée avec lettrage (contrôle planche ≥ 740 px/vignette + recadrage 5h-7h ×5 ; « atténué compte comme présent ») ; anciennes faces sauvegardées.
- **Statut** : partiellement corrigé (3/6). **Outil recommandé** : Codex/agent + Higgsfield (`nano_banana_pro` 4K). **Validation humaine** : oui (choix visuel final).

### BUG-2 — `alt` et noms de fichiers CDN portant encore « chiffres arabes »
- **Description** : après le renommage « Cadrans à chiffres » (30/07), 0 occurrence visible, mais les `alt` de médias et les noms de fichiers CDN hérités disent encore « chiffres arabes » — lus par les lecteurs d'écran, affichés si l'image ne charge pas, indexés par Google Images. Les médias étaient dans les interdits absolus de la mission. Cas connexe : les 8 médias de l'aviateur bronze portent `noirmont-un-bronze-plongeuse-*` dans leur nom CDN. [FAIT — repo:boutique-seiko-mod/publication-grappes.md §7 l.496-501 ; visuels-aviateur-consolidation.md l.278-282]
- **Priorité** : P2. **Impact** : moyen (SEO images, accessibilité). **Difficulté** : faible pour les `alt` (attention au piège des médias partagés — voir 10-FAILURES B7) ; moyenne pour les noms CDN (re-téléversement obligatoire).
- **Dépendances** : levée du gel des médias par Hakim.
- **Critères d'acceptation** : plus aucune occurrence « chiffres arabes » dans les `alt` ; décision explicite (corriger ou assumer) pour les noms CDN.
- **Statut** : ouvert, « à trancher séparément ». **Outil** : agent API Shopify. **Validation humaine** : oui (autorisation d'écrire les médias).

### BUG-3 — Images sur-promettant la capacité (4 rouleaux + 5 meubles)
- **Description** : les 4 fiches Rouleau de Voyage montrent **4 niches** alors qu'aucune variante 4 emplacements n'existe (max 3) ; les 5 meubles Remontoir Collection montrent **8 emplacements** pour 4 ou 6 vendus (« le double de ce qui est achetable » sur les fiches LED). Les descriptions disent la vérité ; l'image seule sur-promet, et ces faces sont **en ligne**. Motif de retour légitime. [FAIT — repo:boutique-seiko-mod/branchement-galeries-codex.md l.408-422 ; REPRISE-SESSION.md point 6]
- **Priorité** : P1. **Impact** : fort (retours, litiges). **Difficulté** : moyenne (nouvelles faces conformes) ou nulle (ajuster l'offre).
- **Dépendances** : arbitrage Hakim (refaire l'image ou changer l'offre).
- **Critères d'acceptation** : chaque image montre au plus la capacité vendue ; contrôle à l'œil sur les 9 fiches.
- **Statut** : ouvert. **Outil** : Higgsfield + agent. **Validation humaine** : oui.

### BUG-4 — Fiche aviateur redondante : SKU en double — **DANGER**
- **Description** : `aviateur-acier-cadran-chiffres-arabes` (`10981883150674`, DRAFT, 0 média) porte les **mêmes 6 SKU** que l'aviateur acier **publié** (`10977448558930`). Sans effet tant qu'elle reste en DRAFT — « **ne jamais la publier telle quelle** » : deux fiches publiées avec les mêmes SKU casseraient le mapping DSers. Deux issues documentées : (a) supprimer la fiche neuve (mais son handle est la meilleure URL de grappe), (b) la publier à la place et dépublier l'autre définitivement + rattacher DSers. [FAIT — repo:boutique-seiko-mod/visuels-aviateur-consolidation.md §4 ; fiches-contradictoires-et-cadran-arabe.md §4 ; publication-grappes.md §2]
- **Priorité** : P1 (mine dormante). **Impact** : fort si erreur. **Difficulté** : faible.
- **Dépendances** : décision (a)/(b) par Hakim.
- **Critères d'acceptation** : plus aucun couple de fiches partageant un SKU dont les deux peuvent devenir ACTIVE ; redirection posée si handle changé.
- **Statut** : ouvert. **Outil** : agent API Shopify. **Validation humaine** : oui.

### BUG-5 — Métachamp `custom.bracelet` faux sur `noirmont-un-bronze-plongeuse`
- **Description** : le métachamp dit « Acier maille non précisée », le fournisseur dit **Cuir**. Tranché mais non modifié. Fausserait la future facette Bracelet. [FAIT — repo:boutique-seiko-mod/fiches-contradictoires-et-cadran-arabe.md]
- **Priorité** : P2. **Impact** : moyen. **Difficulté** : triviale.
- **Critères d'acceptation** : valeur corrigée, relue après écriture.
- **Statut** : ouvert. **Outil** : agent API. **Validation humaine** : non.

### BUG-6 — `quarante-et-un-sport-acier` se contredit
- **Description** : options « bracelet acier » **et** « bracelet cuir M », mais la description dit « bracelet intégré ». [FAIT — repo:boutique-seiko-mod/configurateur-implementation.md §9 point 4 ; axes-guide-de-choix.md §8]
- **Priorité** : P2. **Impact** : moyen. **Difficulté** : faible (réécriture ciblée, sauvegarde avant, piège SEO wholesale).
- **Statut** : ouvert. **Outil** : agent API. **Validation humaine** : non (relecture souhaitable).

### BUG-7 — Template article : blog `news` au lieu d'`actualites` + bannière vide
- **Description** : `templates/article.json` a sa section `blog_featured` réglée sur le blog `news` alors que le blog réel a le handle `actualites` (→ « articles associés » vide), et place un `image-banner` alimenté par `closest.article.image` alors que l'article n'a pas d'image à la une (→ bannière vide/cassée). [FAIT — repo:boutique-seiko-mod/article-mod-ou-hommage.md §7 ; passe-coherence-avant-publication.md §5 point 2]
- **Priorité** : P2 (bloque la publication de l'article). **Impact** : moyen. **Difficulté** : faible.
- **Critères d'acceptation** : blog correct référencé, image à la une posée, rendu revérifié à 375 px après publication.
- **Statut** : ouvert. **Outil** : agent thème (brouillon uniquement) + Hakim pour publier. **Validation humaine** : oui (publication).

---

## 2. Dette technique

### DT-1 — 4 `seo.description` vides (les 4 fiches mères actives)
- **Description** : `trente-neuf-classique-cannelee`, `trente-six-classique-jubile`, `trente-neuf-duo-classique-bicolore`, `quarante-et-un-sport-acier` — 53/57 renseignées ; les titres ont été posés le 30/07, pas les descriptions. ⚠️ Piège : `productUpdate` remplace l'objet `seo` **en entier** — toujours poser `title` + `description` ensemble (47 titres déjà perdus ainsi une fois). [FAIT — repo:boutique-seiko-mod/seo-titles-produits.md §7-8 ; plan-nommage-seo.md §5 étape 6]
- **Priorité** : P2. **Impact** : moyen. **Difficulté** : faible. **Dépendances** : patron §3.1 de `plan-nommage-seo.md` (155 c.).
- **Critères d'acceptation** : 57/57 couples complets, uniques, relus après écriture, aucun title perdu.
- **Statut** : ouvert. **Outil** : agent API. **Validation humaine** : non.

### DT-2 — 11 diamètres manquants (`custom.diametre` = null sur 11/57)
- **Description** : 7 Intégrale + Squelette Octogone + Explorateur (la seo.description dit « 36 ou 39 mm » mais le métachamp est vide) + les 2 aviateurs. Débloquerait 11 titres porteurs de « mm » (46/57 aujourd'hui) et rendrait la facette Diamètre honnête. ⚠️ Ne pas estimer sur photo (erreur 2-3 mm) ; « diamètre du cadran » fournisseur ≠ cote de boîtier (écart 6-10 mm). Seule issue : demander au vendeur (messagerie AliExpress/DSers) ou mesurer à réception. [FAIT — repo:boutique-seiko-mod/seo-titles-produits.md §6 ; veracite-produit-cloture.md Volet 3 ; axes-guide-de-choix.md §7]
- **Priorité** : P2. **Impact** : moyen (16-19 montres cachées dans les entonnoirs profonds du configurateur). **Difficulté** : faible techniquement, dépend du fournisseur.
- **Statut** : ouvert. **Outil** : Hakim/fournisseur pour la donnée, agent pour l'écriture. **Validation humaine** : oui (contact fournisseur).

### DT-3 — 6 visuels de variante Explorateur (doublons `Black/Black1`…)
- **Description** : 6 couples de codes fournisseur que rien ne départage, gardés distincts par suffixe « (réf. 1) » — 6 valeurs non résolues sur 194. Générer 6 visuels de variante pour les départager visuellement. [FAIT — repo:boutique-seiko-mod/publication-grappes.md §6.4]
- **Priorité** : P2. **Impact** : moyen (lisibilité du choix). **Difficulté** : moyenne. **Dépendances** : crédits (~24-39 cr), photos fournisseur des deux réfs.
- **Critères d'acceptation** : 6 images liées à leurs variantes (`productVariantAppendMedia`), clic = bascule de galerie, contrôle stérilité pleine résolution.
- **Statut** : ouvert. **Outil** : Higgsfield + agent API. **Validation humaine** : oui (DA).

### DT-4 — Collections : 6 titres descriptifs + 8 couples SEO (« Phase 2, rien de fait »)
- **Description** : les 6 familles historiques sont toutes sans couple SEO ; plan complet prêt (tableau titres/volumes dans `plan-nommage-seo.md` §3.2 : « Montres automatiques homme, lunette cannelée », « Montres chronographe 39 mm », etc.). Bonus accessoires au meilleur rapport volume/difficulté : `remontoirs` (4 400/mois), `ecrins-et-rouleaux` (1 300 + 590). Corollaire indispensable : figer les **libellés courts du méga-menu en dur** (sinon il affichera les titres longs — `{{ closest.collection.title }}`). [FAIT — repo:boutique-seiko-mod/plan-nommage-seo.md §3.2, §4.2, §5 Phase 2 ; seo-titles-produits.md §8 point 4]
- **Priorité** : P2. **Impact** : fort (SEO). **Difficulté** : faible. **Dépendances** : arbitrage des volumes non mesurés (EXP-3) pour `plongeuses`/`chronos` ; thème brouillon.
- **Critères d'acceptation** : aucun handle touché, titres posés, méga-menu inchangé visuellement, relecture par empreinte.
- **Statut** : ouvert. **Outil** : agent API + thème brouillon. **Validation humaine** : oui (valide les titres).

### DT-5 — Télémétrie du configurateur : aucune posée
- **Description** : jeu d'événements défini (`configurateur_ouvert`, `etape_changee`, `option_choisie`, `configurateur_termine`, `ajout_panier` — équivalents PostHog relevés chez Goteia) mais aucun outil de mesure choisi ni branché. Sans elle, impossible de savoir si le configurateur convertit. [FAIT — repo:boutique-seiko-mod/configurateur-implementation.md §9 point 5 ; spec-configurateur-goteia.md l.425]
- **Priorité** : P2 (P1 dès l'ouverture au public). **Impact** : fort pour l'itération. **Difficulté** : moyenne. **Dépendances** : choix de l'outil (Hakim), republication du thème.
- **Critères d'acceptation** : 5 événements émis et visibles dans l'outil, testés sur un parcours complet.
- **Statut** : ouvert. **Outil** : agent thème. **Validation humaine** : oui (choix outil/consentement RGPD).

### DT-6 — Corps de page « configurateur » contraire à la charte + titre/menu « CONFIGURATEUR »
- **Description** : le corps de page contient encore « Composez votre montre pièce par pièce… » (mots interdits : composez/configurez impliquent un assemblage) — non rendu par le nouveau gabarit **mais rendu par Helio**, le thème actuellement publié. Le titre de page et l'entrée de menu disent toujours « CONFIGURATEUR » (handle cité dans 4 menus ; menus partagés entre thèmes → décision Hakim). [FAIT — repo:boutique-seiko-mod/configurateur-implementation.md §9 point 3 ; passe-coherence-avant-publication.md §5 point 5]
- **Priorité** : P2. **Impact** : moyen (cohérence de promesse). **Difficulté** : faible.
- **Statut** : ouvert. **Outil** : agent (corps de page), Hakim (menu/handle). **Validation humaine** : oui.

### DT-7 — Francisation des options des 13 accessoires lot 4
- **Description** : `Band Color`, `Band Width`, `Color`, valeurs `steel-no logo`, `0.6mm-silver` restées en anglais — non entreprise pour ne pas toucher au mapping fraîchement établi. (La francisation des 5 fiches montres des grappes est FAITE.) [FAIT — repo:boutique-seiko-mod/import-accessoires-lot4.md ; publication-grappes.md §6]
- **Priorité** : P2. **Impact** : moyen. **Difficulté** : moyenne (ne jamais toucher les SKU ; re-vérifier DSers après).
- **Critères d'acceptation** : options/valeurs françaises, mapping DSers revérifié 13/13, sauvegarde avant.
- **Statut** : ouvert. **Outil** : agent API + contrôle DSers navigateur. **Validation humaine** : non (contrôle DSers recommandé).

### DT-8 — Étiquettes accessoires : deux vocabulaires à réconcilier
- **Description** : jeu pluriel qui pilote les collections (`remontoirs`, `ecrins`, `bracelets`, `outils`) vs jeu singulier/descriptif (`bracelet`, `outillage`…) ; `productType` mélangé. Toute nouvelle fiche sans étiquette du jeu pluriel est invisible à la navigation — « le piège qui a déjà coûté un aller-retour ». À réconcilier avant toute facette accessoire. [FAIT — repo:boutique-seiko-mod/megamenu-illustre.md §7 point 3 ; pages-collection-refonte.md §6 point 3]
- **Priorité** : P2. **Impact** : moyen. **Difficulté** : faible.
- **Statut** : ouvert. **Outil** : agent API. **Validation humaine** : non.

### DT-9 — Menus en double à la publication + double déclaration desktop/mobile
- **Description** : `noirmont-desktop`/`noirmont-mobile` ne servent qu'au brouillon ; `main-menu` intact. À la publication : basculer ou assumer les doublons. Ajouter une famille exige 3 déclarations (grille desktop, menu mobile, tiroir) — « sans dispositif de rappel, elles divergeront ». [FAIT — repo:boutique-seiko-mod/publication-grappes.md §5 point 7 ; megamenu-illustre.md §7]
- **Priorité** : P2 (à la republication). **Impact** : moyen. **Difficulté** : faible.
- **Statut** : ouvert. **Outil** : Hakim + agent. **Validation humaine** : oui (menus partagés entre thèmes).

### DT-10 — Reliquats divers documentés
- **Lorem ipsum** dans le popup « Guide des tailles » (`templates/product.json` → `product-variant-popup` → `text_99rHbT`) + un `<h1>Guide des tailles</h1>` mal placé (bloc désactivé mais présent dans un template publié) [FAIT — repo:boutique-seiko-mod/veracite-produit-cloture.md].
- **Bloc « paiement 4× » (`noirmont-4x.liquid`) à ne pas publier** tant qu'aucun prestataire n'est actif : au 26/07, Shopify Payments non configuré, PayPal Inactif, Klarna non installé [FAIT — veracite-produit-cloture.md].
- **8 `alt` reconstruits à relire** (positions 3-4 des 4 galeries montres, textes d'origine perdus dans l'incident des 31 alt) [FAIT — decoupage-elagage-lot2.md l.348].
- **80 médias des 7 mères en brouillon = perdus** (0/6 récupérables au contrôle visuel) — ne plus compter dessus [FAIT — audit-visuel-catalogue.md].
- Handles gardant « 904l » (alliage non prouvé) — laisser ou renommer **avec redirection** [FAIT — repo:boutique-seiko-mod/veracite-produit-cloture.md point 4].
- Point d'étanchéité jamais dit : une montre remontée perd la garantie d'étanchéité d'origine — aucune des 15 fiches ne le dit [FAIT — veracite-produit-cloture.md l.241-245].
- Nom d'option `Mouvement, diamètre & fond` (Explorateur) hors convention — à uniformiser un jour à l'échelle du catalogue [FAIT — publication-grappes.md §6.5].
- Correctif « Voir plus » des pages collection = contre-feu, pas une réparation à la source (règle fautive dans une feuille CDN du thème) [FAIT — pages-collection-refonte.md §6].
- `scratchpad/backup-publication/` n'existe plus sur disque : l'état pré-renommage des options n'est attesté que par les 2 TSV du 29/07 [FAIT — publication-grappes.md §6.2].
- **Priorité** : P3. **Statut** : ouverts. **Validation humaine** : selon item.

---

## 3. Évolutions

### EV-1 — Article de blog `arabic dial` — **mûr maintenant**
- **Description** : deuxième article nommé du plan éditorial (≈ 15 500/mois, personne au-dessus de la 4ᵉ position), conditionné à la publication des fiches aviateur — publiées le 29/07 : l'article est mûr. Rappel du levier : goteia.fr tire 66 % de son trafic organique d'un seul article. Attention au piège sémantique occidental/oriental (10-FAILURES D6) : l'article devra lever l'ambiguïté comme la collection le fait. [FAIT — repo:boutique-seiko-mod/article-mod-ou-hommage.md §7 point 10 ; marche-complet-semrush.md l.455]
- **Priorité** : P2. **Impact** : fort (acquisition). **Difficulté** : moyenne. **Dépendances** : BUG-7 (template article), publication du 1ᵉʳ article, thème republié.
- **Critères d'acceptation** : article publié, liens produits vers les fiches ACTIVE, JSON-LD FAQPage si section questions, rendu vu à 375 px.
- **Statut** : ouvert. **Outil** : agent (rédaction+API), Hakim (publication). **Validation humaine** : oui.

### EV-2 — Publier « Seiko mod ou montre hommage » (article en brouillon, URL 404)
- **Description** : `Article/615589052754`, blog `actualites`, corps prêt ; 8 points restants listés (lien cadran arabe à repointer vers la fiche — désormais possible, image à la une, rendu jamais vu, blog_featured, thème, mot de passe, fourchette de prix 279-417 € à recaler, FAQPage absent). [FAIT — repo:boutique-seiko-mod/article-mod-ou-hommage.md §7 ; passe-coherence-avant-publication.md §5 point 2]
- **Priorité** : P2. **Impact** : fort (66 % du trafic de Goteia vient de son équivalent). **Difficulté** : faible. **Dépendances** : BUG-7, tâches business B1/B2.
- **Statut** : ouvert. **Outil** : agent + Hakim. **Validation humaine** : oui (publication).

### EV-3 — Configurateur réel (assemblage à la commande) via BL Watches
- **Description** : le « vrai » configurateur dépend entièrement de BL Watches Parts Store (déclare assembler, ~1 428 combinaisons ouvrables, axe aiguilles fermé faute d'alésages publiés nulle part au monde). Prochain jalon décisif : les 4 chiffres écrits (voir BIZ-6) puis une **commande test d'un build configuré**. Prime de personnalisation observée chez Goteia : +90 à +100 € (pas +30). [FAIT — repo:boutique-seiko-mod/sourcing-configurateur.md ; REPRISE-SESSION.md l.71]
- **Priorité** : P3 (le guide de choix actuel couvre la promesse). **Impact** : fort à terme. **Difficulté** : forte.
- **Dépendances** : BIZ-6 (confirmation écrite), commande test, décision de gamme.
- **Statut** : piste documentée, aucun GO. **Outil** : Hakim (fournisseur) + agents. **Validation humaine** : oui.

### EV-4 — Import d'avis Trustoo sur les 5 nouvelles fiches
- **Description** : non couvert par la mission de publication (chasse gardée avis/sliders). Recette bookmarklet complète disponible. [FAIT — repo:boutique-seiko-mod/publication-grappes.md §5 point 8] [MÉMOIRE : import-avis-trustoo-bookmark]
- **Priorité** : P3. **Impact** : moyen. **Difficulté** : faible (recette éprouvée, 22 fiches sur Tuftéo).
- **Statut** : ouvert. **Outil** : navigateur Chrome piloté (voir MBU-3). **Validation humaine** : oui (Hakim garde la main sur la preuve sociale ; il filtre/traduit).

### EV-5 — Sourcing squelette élargi (la collection n'a que 2 fiches)
- **Description** : ≈ 8 400/mois pour 2 fiches — « c'est un sujet de sourcing, pas de nommage ». Réserve : aucun listing squelette stérile > ~30 ventes avec note ≥ 4.8 trouvé. [FAIT — repo:boutique-seiko-mod/plan-nommage-seo.md §3.2 ; sourcing-arabes-squelettes.md §1]
- **Priorité** : P3. **Impact** : moyen-fort. **Difficulté** : moyenne (marché mince).
- **Statut** : ouvert. **Outil** : agent sourcing (session Chrome — voir MBU-2). **Validation humaine** : oui (GO produit).

---

## 4. Expérimentations

### EXP-1 — Chiffres arabes orientaux (١ ٢ ٣) : réévaluer dans 6-8 semaines
- **Description** : verdict du 30/07 : ⛔ aucun candidat publiable selon les règles. Le seul modèle au monde cochant stérilité + oriental + fournisseur éprouvé est le Tandorio `1005010249362754` (4,7/5, 3 avis, 10 ventes — sous le seuil de 96 %). 3 options chiffrées pour Hakim : (1) publier le 8215 à 349 € (marge ≈ 247 €) **si** « Automatic » imprimé à 6h n'est pas « un nom » ; (2) le jumeau NH35 à 379 € (0 vente) ; (3) attendre — l'option que les règles imposent. **Le listing prend ~5 ventes/mois : il peut passer les seuils seul dans 6-8 semaines.** Preuves visuelles : `preuves-chiffres-orientaux-2026-07-30/` (4 JPEG). Recette de recherche : requêtes en arabe (`ساعة أوتوماتيك أرقام عربية`) et `urdu`, jamais « arabic numerals ». [FAIT — repo:boutique-seiko-mod/sourcing-chiffres-orientaux.md]
- **Priorité** : P2 (échéance ~mi-septembre 2026). **Impact** : fort (grappe 15 500/mois sans concurrent au-dessus de la 4ᵉ position, sens oriental toujours non servi). **Difficulté** : faible (re-vérification) .
- **Critères d'acceptation** : preuve sociale re-relevée (avis/ventes), verdict re-prononcé contre les seuils, décision Hakim tracée.
- **Statut** : planifié. **Outil** : agent + session Chrome AliExpress. **Validation humaine** : oui (arbitrage des 3 options).

### EXP-2 — Hybrides marque + mod (≈ 12 000/mois) : arbitrage risque de marque
- **Description** : rang 2 du marché (`seiko mod nautilus` 880, `seiko datejust` 1 300, `seiko mod royal oak` 480…), KD 5-10 %, CPC 0,08-0,29 € — « meilleur rapport coût/intention du marché ». Volontairement écartés : les capter suppose d'écrire des noms de modèles de maisons de luxe à côté de notre catalogue — le glissement exact que la charte interdit. « La seule décision d'ampleur que j'ai prise seul, et elle est réversible. » `montreapapy.fr` enchérit dessus sans détour. [FAIT — repo:boutique-seiko-mod/marche-complet-semrush.md l.366, l.647 ; article-mod-ou-hommage.md §2, §7 point 9]
- **Priorité** : P3. **Impact** : fort (acquisition) vs risque juridique/marque. **Difficulté** : éditoriale.
- **Critères d'acceptation** : décision écrite de Hakim (ouvrir via contenu éditorial « hommage » encadré, ou maintenir l'exclusion).
- **Statut** : arbitrage ouvert. **Outil** : décision humaine, puis agent contenu. **Validation humaine** : oui.

### EXP-3 — Volumes SEMrush non mesurés avant de figer des titres
- **Description** : à passer au Keyword Magic (avec mot-clé témoin — 10-FAILURES E2) : « montre de plongée (+automatique) », « montre chronographe homme », « montre GMT », « rouleau de voyage montre », « montre automatique fond verre », `montre field`, `montre squelette automatique`, `montre bicolore`. Conditionne les titres `plongeuses`/`chronos` (DT-4) et des fiches. [FAIT — repo:boutique-seiko-mod/plan-nommage-seo.md §6 point 5 ; seo-titles-produits.md §1]
- **Priorité** : P2. **Impact** : moyen. **Difficulté** : faible. **Dépendances** : accès SEMrush actif (Hakim prend des essais ponctuels — [MÉMOIRE] ne pas activer sans son accord).
- **Statut** : ouvert. **Outil** : SEMrush + témoin. **Validation humaine** : oui (activation du compte).

### EXP-4 — Tester Browser Use sur l'iframe Search & Discovery
- **Description** : l'extension Chrome ne franchit pas l'iframe cross-origin (`search-and-discovery.shopifyapps.com`) et le contrôle bureau était refusé dans l'environnement précédent. Un pilotage CDP direct (Browser Use) atteint des frames que les clics synthétiques de l'extension n'atteignent pas — à expérimenter : si ça marche, les 5-6 facettes (BIZ-3) deviennent automatisables et la doctrine « iframe = gestes du marchand » tombe. Appliquer la leçon 10-FAILURES F4 : revalider une « impossibilité » dans d'autres conditions avant d'en faire une doctrine. [FAIT — repo:boutique-seiko-mod/metachamps-montres.md §1] [MANQUANT : aucun essai Browser Use/CDP documenté sur cette iframe]
- **Priorité** : P3. **Impact** : moyen (débloque une classe entière de gestes admin). **Difficulté** : moyenne.
- **Critères d'acceptation** : un clic vérifié à l'intérieur de l'iframe (ex. ouverture du formulaire « Ajouter un filtre ») ; sinon, documentation de l'échec avec preuve.
- **Statut** : non tenté. **Outil** : Browser Use (CDP). **Validation humaine** : oui (écritures de facettes seulement sur feu vert).

---

## 5. Tâches business (domaine de Hakim)

### BIZ-1 — Médiateur de la consommation — **bloquant légal (P0)**
- **Description** : obligation légale (art. L612-1 C. consom.), exigée aussi par Merchant Center. Adhésion **par site** : ne jamais recopier le CM2C de Tuftéo (fausse déclaration). Marqueur exact laissé en CGV art. 17 : `[À COMPLÉTER — nom, adresse et téléphone du médiateur…]` — présent dans la page ET la politique de caisse. [FAIT — repo:boutique-seiko-mod/pages-legales-et-delais.md §3 ; plan-nommage-seo.md §4.3 ; REPRISE-SESSION.md point 2]
- **Priorité** : **P0**. **Impact** : bloquant lancement. **Difficulté** : administrative (adhésion payante).
- **Critères d'acceptation** : adhésion souscrite pour maisonnoirmont.fr, marqueur remplacé aux deux endroits, zéro mention CM2C.
- **Statut** : pris en charge par Hakim le 30/07/2026 ; adhésion et remplacement du marqueur encore non vérifiés. **Outil** : Hakim ; agent pour l'écriture finale. **Validation humaine** : **oui**.

### BIZ-2 — Republier le thème « Maison Noirmont » + retirer le mot de passe + supprimer le fork
- **Description** : thème `204248088914` UNPUBLISHED (tout le travail est invisible), `onlineStore.passwordProtection.enabled = true` (Merchant Center ne peut rien explorer), fork obsolète `204329288018` à supprimer. Le connecteur refuse d'écrire sur un thème MAIN : la publication est un geste de Hakim. Ordre conseillé (`plan-nommage-seo.md` §5 Phase 0) : médiateur → republication → paiement/commande test → mot de passe → purge des affirmations invérifiables. [FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md l.17-26, point 1 ; plan-nommage-seo.md §4.3]
- **Priorité** : **P0**. **Impact** : bloquant. **Difficulté** : faible. **Dépendances** : BIZ-1, BIZ-4 (à purger avant exposition publique), DT-9 (menus).
- **Critères d'acceptation** : thème publié, fork supprimé, mot de passe retiré, home rendue = celle du brouillon.
- **Statut** : ouvert. **Validation humaine** : **oui**.

### BIZ-3 — Les 5 (+1) facettes Search & Discovery — gestes manuels
- **Description** : interface dans une iframe cross-origin, aucun chemin API, définitions de métachamps déjà créées. Gestes exacts (S&D → Filtres) : 1) supprimer « Disponibilité » ; 2) ajouter `custom.famille` → **Famille** ; 3) `custom.diametre` → **Diamètre** ; 4) `custom.calibre` → **Mouvement** ; 5) `custom.couleur_cadran` → **Couleur de cadran** ; 6) ajout du 27/07 : `custom.bracelet` → **Bracelet**. « Prix » déjà en place. ⚠️ Jamais adosser aux étiquettes (doublons singulier/pluriel). Réserve à revalider : couverture des métachamps relue à 52·48·44·53·91 — vérifier les taux avant d'activer Diamètre/Couleur (11 diamètres manquants — DT-2 ; 13 nuances pour 14 produits relevées le 26/07). [FAIT — repo:boutique-seiko-mod/metachamps-montres.md §1 ; verification-catalogue-strategie.md l.259, l.274 ; pages-collection-refonte.md §4]
- **Priorité** : P1. **Impact** : fort (moteur du configurateur + navigation). **Difficulté** : faible (10 minutes d'interface). **Dépendances** : DT-2 conseillée avant Diamètre ; EXP-4 pourrait l'automatiser.
- **Critères d'acceptation** : facettes visibles sur `/collections/montres`, valeurs uniques, aucune facette adossée aux tags.
- **Statut** : ouvert. **Outil** : Hakim (interface). **Validation humaine** : **oui**.

### BIZ-4 — Avis de démonstration et compteurs à trancher — 1340 avis / 0 client
- **Description** : badge « 1340 avis » (invisible de surcroît : encre sur encre 1,00:1), « 4,8/5 » avec `stars=4,5`, trois `review_count: 123`, « - 2 000 clients satisfaits » (`templates/index.json:144`), 10 avis rédigés en dur, sliders de démo — pour 0 commande réelle. Risque : *misrepresentation* = motif de suspension Merchant Center (précédent vécu : Bien Brûlé, GMC suspendu puis réintégré). Domaine réservé de Hakim — aucun agent n'y a touché ; les placeholders de démo sont sa chasse gardée. [FAIT — repo:boutique-seiko-mod/passe-coherence-avant-publication.md §5 point 7 ; fix-uiux-json.md ; plan-nommage-seo.md §4.3] [MÉMOIRE : mobile-first-et-placeholders-demo]
- **Priorité** : **P0** (avant exposition publique). **Impact** : bloquant GMC. **Difficulté** : faible.
- **Critères d'acceptation** : zéro chiffre de preuve sociale invérifiable rendu public ; vrais avis importés (EV-4) ou éléments retirés.
- **Statut** : ouvert. **Validation humaine** : **oui** (exclusif Hakim).

### BIZ-5 — Comptes sociaux : 12 champs vides
- **Description** : les comptes du fournisseur du thème ont été purgés du schéma ; 12 champs restent vides — renseigner ou laisser vides sciemment. [FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md point 4 ; fix-uiux-json.md l.172]
- **Priorité** : P2. **Impact** : faible-moyen (confiance). **Difficulté** : faible (créer les comptes = travail réel).
- **Statut** : ouvert. **Validation humaine** : **oui**.

### BIZ-6 — Confirmation écrite BL Watches — les 4 chiffres
- **Description** : acquis par messagerie (assemble à la config, 100 montres/jour, dropship OK, zéro logo) mais **ni prix, ni délai, ni catalogue, ni alésages d'aiguilles** — les 4 informations à obtenir **par écrit**, plus packaging et traitement d'un défaut ; puis commande test d'un build. L'axe aiguilles ne s'ouvre pas sans les alésages (publiés par aucun fournisseur au monde). [FAIT — repo:boutique-seiko-mod/fournisseurs-reponses-2026-07-24.md ; sourcing-configurateur.md §1, §5, §7 ; REPRISE-SESSION.md point 8]
- **Priorité** : P2 (conditionne EV-3). **Impact** : fort. **Difficulté** : faible (un message) mais réponse incertaine.
- **Critères d'acceptation** : réponse écrite archivée couvrant les 4 points ; sinon relance Corgeut Factory Store (en attente).
- **Statut** : ouvert. **Outil** : Hakim (un agent ne contacte aucun fournisseur). **Validation humaine** : **oui**.

### BIZ-7 — Noirmont Deux (cadran bleu ciel à bulles) : trancher
- **Description** : `noirmont-deux-plongeuse-ceramique` (20 variantes, BLIGER `1005005629655849`) passée ACTIVE → DRAFT le 27/07 : la fiche montre une plongeuse noire céramique, le fournisseur livre pour les 7 références un cadran **bleu ciel à bulles multicolores** — deux montres différentes. Décision : assumer le motif (refaire fiche + visuels sur le produit réel) ou re-sourcer. Backup : `backup-avant-draft-noirmont-2026-07-27.json`. Sa remise en ACTIVE rend aussi son cadran Noir au configurateur (50 → 53 montres servies avec les 2 aviateurs déjà republiés). [FAIT — repo:boutique-seiko-mod/verification-catalogue-strategie.md §5 ; fiches-contradictoires-et-cadran-arabe.md §4 ; configurateur-implementation.md §9]
- **Priorité** : P2. **Impact** : moyen. **Difficulté** : moyenne.
- **Statut** : DRAFT, non tranché au 30/07. **Validation humaine** : **oui**.

### BIZ-8 — Prix barrés permanents et règle française des 30 jours
- **Description** : badge « En promotion » retiré (`show_sales_badge_on_cards: false`, vérifié 0 badge à 375 et 1280 px), mais `compare_at_price` reste posé sur les **610 variantes** (règle ×1,3) = remise permanente affichée, et la fiche produit cumule 4 signaux de remise. Le prix de référence doit être le prix le plus bas des 30 derniers jours — **une boutique neuve n'a pas ce référentiel**. Précédent interne : Lihyl porte un 599/799 jamais pratiqué, risque assumé par Hakim. À trancher avant toute remise affichée/publicité. [FAIT — repo:boutique-seiko-mod/charte-ab-application.md ; audit-uiux-produit.md ; REPRISE-SESSION.md point 7]
- **Priorité** : P1. **Impact** : fort (DGCCRF/Omnibus, GMC). **Difficulté** : faible techniquement.
- **Statut** : ouvert. **Validation humaine** : **oui**.

### BIZ-9 — « Plongeuse » dans 3 titres Héritage (5 bar, nage exclue)
- **Description** : corps de texte et SEO disent déjà « style plongeuse » ; les **titres** restent (« un titre reste un titre » : collection, panier, Google Shopping). Formulation proposée : « Héritage Bleu — Vintage 42, style plongeuse ». [FAIT — repo:boutique-seiko-mod/veracite-produit-cloture.md l.229-238 ; REPRISE-SESSION.md point 5]
- **Priorité** : P1. **Impact** : moyen-fort (véracité). **Difficulté** : triviale.
- **Statut** : ouvert (domaine réservé). **Validation humaine** : **oui**.

### BIZ-10 — Réglages boutique et légaux restants
- **Format monétaire** : `€329` → `329,00 €` (Paramètres → Devise ; réglage de compte, agents interdits) [FAIT — passe-coherence-avant-publication.md §5 point 3].
- **Paiement + commande test** : `shopifyPaymentsAccount` non vérifiable par API (scope absent) ; 0 commande [FAIT — plan-nommage-seo.md §4.3].
- **Canal Google & YouTube** : non installé, prérequis du flux Shopping [FAIT — plan-nommage-seo.md §6].
- **Dates de livraison estimées** : réglage absent de l'API, « Automatisé » par défaut = 3ᵉ délai contradictoire à la caisse — à désactiver dans l'admin [NOTION].
- **Légal** : téléphone repris de Tuftéo à confirmer ; e-mail Réglages (`contact.noirmont@gmail.com`) ≠ e-mail publié (`contact@maisonnoirmont.fr`) ; PayPal à ajouter en CGV art. 7 si activé ; champ « Coordonnées » de Réglages → Politiques marqué Obligatoire, non renseigné [FAIT — pages-legales-et-delais.md §3, §5].
- **Accessoires lot 4 avant publication** : 5 fiches sans visuel NOIRMONT ; photos fournisseur avec montres logotées/« for Rolex » à élaguer ; étui 189,90 € vs coffret 54,90 € (échantillon conseillé) ; vendeur 904L noté 4,3 à recontrôler [FAIT — import-accessoires-lot4.md].
- **Espacement des en-têtes d'accordéon** (reliquat cibles tactiles 44 px) [FAIT — passe-coherence-avant-publication.md §8.2].
- **Priorité** : P1 pour monétaire/paiement/canal, P2 le reste. **Validation humaine** : **oui** (réglages de compte).

---

## 6. Migration Codex

### MC-1 — Adopter la doctrine de vérification dans l'outillage Codex
- **Description** : intégrer aux workflows Codex les règles payées de 10-FAILURES : relecture/MD5 après toute écriture (jamais `size`/`updatedAt`), `title`+`description` ensemble, jamais `productSet` sur les listes, `files:[{id}]` pour les médias partagés, pagination 30 médias/250 variantes, redirection à chaque changement de handle, sauvegarde avant toute suppression, jamais `switch-shop`, jamais d'écriture sur thème MAIN. [FAIT — repo:boutique-pipeline/docs/codex-handoff/10-FAILURES-AND-LESSONS.md] [NOTION]
- **Priorité** : P1 (avant toute écriture Codex sur la boutique). **Impact** : fort. **Difficulté** : faible.
- **Critères d'acceptation** : checklist reprise dans les prompts/briefs Codex ; premier lot d'écritures vérifié par empreinte.
- **Statut** : ouvert. **Validation humaine** : non.

### MC-2 — Reprendre le pipeline visuel Codex existant (galeries)
- **Description** : la boucle « Codex génère → agent branche » a déjà tourné (54 médias produits par Codex, branchés en lot 3 ; brief type `PROMPT-CODEX-galeries.md` ; scripts `build-visual-manifest.mjs`, `prepare-gallery-worklist.mjs`, `next-gallery-batch.mjs`, `accept-gallery-batch.mjs`, `upload-staged-visuals.mjs`, QA `make-gallery-qa.py`/`make-visual-qa.py`, `align-gallery-v3.py`, `finalize-gallery-delivery.py`). À réutiliser pour BUG-1, BUG-3, DT-3 et le solde du chantier 88 visuels (~466 crédits nécessaires pour ~87 disponibles — re-budgéter). Piège hérité : les fichiers `shopify/product-media-add-*.response.json` sont mal nommés (contenu ≠ preuve d'ajout). [FAIT — repo:boutique-seiko-mod/branchement-visuels-lot3.md ; PROMPT-CODEX-galeries.md ; BILAN-2026-07-25.md l.30]
- **Priorité** : P2. **Impact** : fort. **Difficulté** : moyenne. **Dépendances** : budget crédits Higgsfield (Hakim).
- **Statut** : pipeline opérationnel, chantier suspendu faute de crédits. **Validation humaine** : oui (budget).

### MC-3 — Vérifier les accès depuis l'environnement Codex
- **Description** : inventorier ce que Codex peut réellement atteindre : connecteur Shopify MCP (lecture/écriture thème brouillon + data ; interdits : thème MAIN, `switch-shop`), Higgsfield (solde 87 crédits), SEMrush (essais ponctuels sur accord de Hakim uniquement — [MÉMOIRE]), Notion (hub OH VENTURES, campement type), navigateur avec session AliExpress (sinon CAPTCHA — 10-FAILURES A1). Accès vérifiés le 30/07/2026 : Notion MCP en lecture sur le workspace OH VENTURES et les 20 tickets du Campement ; Chrome connecté à la console Apify. Tests réels autorisés par Hakim le 31/07/2026 sur le duo `khadinakbar` :
  - `aliexpress-product-search-scraper`, run `VBc7BfR8JoFa9QPjc` : requête « stainless steel gravity water filter system », France, 25 résultats maximum, filtres 40–180 €, note ≥ 4, commandes ≥ 20. Le fournisseur primaire a échoué (`ERR_TUNNEL_CONNECTION_FAILED` puis réponse vide/soft-block sur `fr.aliexpress.com`) ; l'Actor a basculé automatiquement sur `thirdwatch/aliexpress-product-scraper`, avec proxy FR et domaine global. **19 enregistrements publiés, 6 filtrés, 1 min 55 s, 0,038 $**. Les premiers résultats observés étaient des filtres de robinet/préfiltres, pas des fontaines à gravité ; les champs vendeur étaient nuls. [OBSERVÉ — Chrome/Apify Console, run et dataset du 31/07/2026]
  - `aliexpress-all-in-one-scraper`, run `Hvk3VN4KQ288uYei1` : deux URL produit, `detailedItems=true`, avis désactivés, plafond annoncé 0,008 $. **Statut UI “Succeeded”, 2 enregistrements, 1 min 54 s, 0,004 $**, mais les deux portent `_warnings=["detail_page_blocked_anti_bot"]`. Titres, prix, notes, commandes, vendeurs, variantes et spécifications sont nuls ; seules les ID/URL/horodatages (et une image générique sur une fiche) sont remontés. Donc **0 enrichissement produit exploitable** malgré le statut vert. [OBSERVÉ — Chrome/Apify Console, run et dataset du 31/07/2026]
  - Coût total observé des deux tests : **0,042 $**. Le premier Actor peut fournir des pistes larges à reclasser ; le second n'est pas retenu dans son état testé. Apify reste une source de découverte, jamais une preuve fournisseur. Tarifs et métriques sont datés et à recontrôler avant dépense. [MANQUANT : Apify MCP/API non configuré ; aucun Actor testé ne fournit encore un enrichissement fiable de fiches AliExpress]
- **Priorité** : P1 (première tâche de la migration). **Impact** : conditionne tout. **Difficulté** : faible.
- **Critères d'acceptation** : tableau accès/limites écrit dans le dossier codex-handoff.
- **Statut** : partiel — Notion, console Apify et deux exécutions Apify vérifiés ; Shopify, Higgsfield, SEMrush et AliExpress direct restent à inventorier/tester selon autorisation. **Validation humaine** : oui (autorisations et dépenses externes).

### MC-4 — Maintenir la culture du piège documenté
- **Description** : chaque passe Codex doit finir par une section « Notes de méthode / pièges » chiffrée, versée dans le livrable ET reportée dans `10-FAILURES-AND-LESSONS.md` + la page Notion campement (les deux générations de « Pièges vérifiés » y vivent). Règle : un piège non écrit sera payé deux fois ; une « impossibilité » ne devient doctrine qu'après revalidation (deux fausses limites déjà corrigées). [FAIT — repo:boutique-seiko-mod/journal-nuit-2026-07-25-suite.md] [NOTION]
- **Priorité** : P1 (process). **Impact** : fort. **Difficulté** : nulle.
- **Statut** : à instaurer. **Validation humaine** : non.

### MC-5 — Synchroniser Notion (dashboard) depuis les fichiers locaux
- **Description** : source de vérité = fichiers locaux, Notion = tableau de bord (hub Pipeline Boutiques Drop, campement type 18-19 tickets à dupliquer par lancement). Rattraper `notion-sync-pending.md` le cas échéant ; panne Notion non bloquante. [MÉMOIRE : notion-pipeline-boutiques, campement-type-lancement-boutique]
- **Priorité** : P2. **Impact** : moyen. **Difficulté** : faible.
- **Statut** : continu. **Validation humaine** : non.

---

## 7. Migration Browser Use

### MBU-1 — QA mobile réelle à 375 px — **jamais faite par un agent**
- **Description** : « rendu mobile jamais vu par un agent — seules des mesures existent » ; `resize_window` de l'outillage précédent répondait « Successfully resized » sans effet (`innerWidth` restait 1710), iframe/popup bloquées par le CSP Shopify. Toute la QA mobile est de la géométrie mesurée ou de la reproduction DOM. Points nommés à voir : bascule des filtres en modale < 990 px, bannière dépliée, tableau de l'article en 3 colonnes, galeries 4-5 visuels, méga-menu, footer. Browser Use (CDP, viewport réel 375×812) est le candidat naturel ; à défaut, téléphone réel de Hakim. [FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md point 9 ; publication-grappes.md §7 ; pages-collection-refonte.md §5-6] [MÉMOIRE : mobile-first-et-placeholders-demo — « la version mobile, au final, c'est la plus importante »]
- **Priorité** : P1 (avant republication publique). **Impact** : fort (~80 % du trafic attendu est mobile). **Difficulté** : moyenne.
- **Critères d'acceptation** : captures réelles 375 px des 6 gabarits (home, collection, fiche, panier, configurateur, article), `innerWidth` vérifié = 375, défauts consignés.
- **Statut** : jamais fait. **Outil** : Browser Use. **Validation humaine** : oui (revue des captures).

### MBU-2 — Sourcing AliExpress outillé avec session
- **Description** : standardiser la recette validée : navigateur avec session connectée (sinon CAPTCHA-artefact), IDs 16 chiffres complets, extraction DOM (`runParams.data` est vide désormais), recherche intra-boutique `all-items.html?SearchText=`, requêtes en arabe pour l'oriental. Sert EXP-1, EV-5 et tout sourcing futur. ⚠️ Vérifier le compte de la session avant d'agir (une passe a été reportée car la session Chrome était sur `contact@bonumvitae.fr`). [FAIT — repo:boutique-seiko-mod/sourcing-accessoires-v3-2026-07-25.md §Notes de méthode ; sourcing-arabes-squelettes.md §5]
- **Priorité** : P2. **Impact** : fort. **Difficulté** : faible (recette écrite).
- **Statut** : recette éprouvée, à porter sous Browser Use. **Validation humaine** : oui (jamais d'achat/commande sans Hakim).

### MBU-3 — DSers : reliquats et futurs mappings
- **Description** : contrôle des 5 nouvelles fiches FAIT le 29/07 au soir (103 produits, 0 Unmapped — les mentions antérieures « contrôle dû » sont périmées). Restent : rattacher `aviateur-acier-cadran-chiffres-arabes` si l'option (b) de BUG-4 est retenue ; re-vérifier le rattachement des 2 aviateurs réécrits (« dix secondes ») ; re-contrôler après DT-7 (francisation accessoires). Toute la mécanique (auto-matching inexistant, listes virtualisées, boîte « Appliquer le mapping », `MessageChannel` contre le bridage, lots de 10) est documentée en 10-FAILURES A3. [FAIT — repo:boutique-seiko-mod/publication-grappes.md §1 ; dsers-mapping-lot2.md]
- **Priorité** : P2. **Impact** : fort (le mapping est la colonne vertébrale du fulfillment). **Difficulté** : moyenne (UI fragile).
- **Statut** : reliquats ouverts. **Outil** : Browser Use sur le Chrome de Hakim (bonne session). **Validation humaine** : oui (confirmation des mappings).

### MBU-4 — Import d'avis Trustoo (support de EV-4)
- **Description** : porter la recette bookmarklet (`appadmin.trustoo.io/bookmark_import`, `postMessage`, setter React sur les `<select>`, audit uniquement au screenshot car iframe cross-origin) sous Browser Use. [MÉMOIRE : import-avis-trustoo-bookmark]
- **Priorité** : P3. **Impact** : moyen. **Difficulté** : faible.
- **Statut** : recette éprouvée (22 fiches Tuftéo). **Validation humaine** : oui (choix des produits/avis par Hakim).

### MBU-5 — Gestes admin en iframe (Search & Discovery et consorts)
- **Description** : cf. EXP-4. Si le test CDP échoue, conserver la doctrine actuelle : fiche de gestes précis pour Hakim (1 min, fiable) pour S&D, éditeur de thème publié, apps embarquées. [FAIT — repo:boutique-seiko-mod/metachamps-montres.md]
- **Priorité** : P3. **Statut** : dépend d'EXP-4. **Validation humaine** : oui.

---

## Vue d'ensemble des priorités

| Priorité | Tâches |
|---|---|
| **P0** | **BUG-0 Tuftéo : 6 avis fictifs publics + compteur 789** · BIZ-1 médiateur · BIZ-2 republication + mot de passe · BIZ-4 avis de démonstration |
| **P1** | BUG-1 SWISS MADE · BUG-3 capacités sur-promises · BUG-4 SKU en double · BIZ-3 facettes · BIZ-8 prix barrés/30 jours · BIZ-9 titres Héritage · BIZ-10 (monétaire, paiement, canal Google) · MC-1 doctrine · MC-3 accès Codex · MC-4 culture du piège · MBU-1 QA mobile réelle |
| **P2** | BUG-2, BUG-5, BUG-6, BUG-7 · DT-1 à DT-9 · EV-1, EV-2 · EXP-1 (échéance mi-sept.), EXP-3 · BIZ-5, BIZ-6, BIZ-7 · MC-2, MC-5 · MBU-2, MBU-3 |
| **P3** | DT-10 · EV-3, EV-4, EV-5 · EXP-2, EXP-4 · MBU-4, MBU-5 |

> Rappel transverse : **rien de public sans la Phase 0** (`plan-nommage-seo.md` §5) ; tout ce qui touche preuve sociale, prix, réglages de compte, fournisseurs ou publication est **domaine réservé de Hakim** ; toute écriture se relit par empreinte (voir `10-FAILURES-AND-LESSONS.md`).

# Maison Noirmont — tableau

**Point d'entrée unique.** Tu commences ici, quel que soit l'agent. Format des tickets : [`../METHODE-TABLEAU.md`](../METHODE-TABLEAU.md).
État courant chiffré : [`ETAT.md`](ETAT.md) · Règles et pièges : [`REGLES.md`](REGLES.md) · Archive : [`journal/`](journal/)

**Mets ce fichier à jour avant de rendre la main.** C'est la seule obligation qui ne se délègue pas.

Dernière mise à jour : **13/08/2026** — régressions P0 réparées ; **audit des 95 brouillons soldé (T-16) : aucun visuel maison perdu, rien à réparer**.

---

## 🔴 BLOQUÉ — attend Hakim

### ~~T-H1 — Coller les 7 politiques légales~~ ✅ FAIT le 12/08 (Hakim)
**Pour** : Hakim · **Pourquoi** : les CGV et la politique de remboursement servies portent **encore la clause interdite** (« portés… ne sont pas repris »), qui contredit le « 14 jours satisfait ou remboursé même si portée » affiché ailleurs. C'est la contradiction qu'un examinateur Merchant Center voit en premier.
**Comment** : ouvrir `livraisons/politiques-maison-noirmont-2026-08-10/`, coller chaque texte dans *Réglages → Politiques*. Le connecteur ne peut pas le faire : permission `write_legal_policies` absente.
**Sortie attendue** : les 7 politiques à jour sur la boutique.

### ~~T-H2 — Adhérer à un médiateur de la consommation~~ ✅ FAIT le 12/08 (Hakim)
**Pour** : Hakim · **Pourquoi** : obligation légale française ; l'article 17 des CGV porte encore `[À COMPLÉTER]`.
**Sortie attendue** : nom et coordonnées du médiateur intégrés aux CGV.

### T-H3 — Arbitrer la grille de prix
**Pour** : Hakim · **Pourquoi** : plusieurs coûts réels sont **inférieurs** aux estimations (9,19 € contre 18,49 € sur un exemple) — le pricing prévu est à re-caler, probablement en ta faveur. Aucun prix n'a été écrit.
**Comment** : lire la partie 3 de `journal/2026-08-09-textes-et-collections.md` — deux stratégies chiffrées (encaisser la marge / baisser le ticket d'entrée) avec recommandation.
**Sortie attendue** : stratégie choisie, prix appliqués aux 95 brouillons.

### T-H4 — Basculer l'e-mail de la boutique
**Pour** : Hakim · **Pourquoi** : `contact.noirmont@gmail.com` est publié dans la politique de confidentialité, alors que `contact@maisonnoirmont.fr` est déjà l'adresse utilisée partout ailleurs.
**Attention** : ⚠️ deux champs distincts dans *Réglages → Général*, dont l'**adresse expéditeur** des e-mails de commande. **Vérifier que la boîte `.fr` reçoit avant de basculer celui-là**, sinon les confirmations de commande partent dans le vide.

### ~~T-H5 — Trancher le sort des 5 sources arabes bloquées~~ ✅ SOLDÉ le 12/08
**Résultat** : **ce n'étaient pas des fiches Shopify** mais 5 **dossiers sources locaux** — vérifié à trois sources, aucune n'existe au catalogue. Rien à archiver, et rien n'a été archivé. Le seul produit réellement porteur du défaut (montre Tandorio `montre-cadran-arabe-oriental-36-39`) était déjà ARCHIVED depuis le 11/08.
**Classement après contrôle au zoom** : **3 abandons fermes** (`cadran-arabe-oriental-rose-28-5`, `cadran-arabe-oriental-sunburst-relief-28-5`, `cadran-nh35-chiffres-arabes-orientaux-28-5` — `SUPERLATIVE CHRONOMETER / OFFICIALLY CERTIFIED` imprimé dans la peinture du cadran) · **2 à trancher** (montres Tandorio : logo présent uniquement sur les variantes par défaut, variantes `sterile` propres prouvées — déjà écartées par ailleurs pour ventes/glyphes) · **1 conservée** (`cadran-arabe-oriental-sunburst-29`, filigrane vendeur `MATELION` sur la photo seulement, produit propre).
**Réf.** : `journal/2026-08-12-abandon-fiches-marquage-physique.md`

### T-20 — Arbitrer le mot « Automatic » gravé sur deux cadrans
**État** : À FAIRE · **Pour** : Hakim (arbitrage) puis Claude
**Pourquoi** : `cadran-arabe-oriental-sunburst-29` et `cadran-arabe-oriental-argent-28-5` portent **`Automatic` réellement gravé** au cadran. Ce n'est ni une marque ni une allégation d'origine — c'est une indication technique générique. Mais nos deux règles s'y contredisaient : « aucun lettrage sur les cadrans » d'un côté, « ne jamais modifier le produit » de l'autre.
**Position retenue et inscrite dans `REGLES.md`** : **on garde.** Effacer une mention physiquement présente produirait une image qui ne correspond pas à ce que le client reçoit — exactement la faute qu'on cherche à éviter. La règle « aucun lettrage » vise les marques et les allégations, pas tout caractère imprimé.
**Sortie attendue** : accord de Hakim sur cette lecture, puis production des visuels de ces deux fiches sans retouche du mot.

---

## 🟥 À FAIRE — P0, régressions à réparer

### ~~T-01 — Restaurer les galeries des fiches actives amputées~~ ✅ FAIT le 12/08
**Compte rendu** : [`journal/2026-08-12-reparation-regressions-p0.md`](journal/2026-08-12-reparation-regressions-p0.md)
**Ce qui a été trouvé** : ce n'était pas 14 fiches mais **37 fiches actives** qui ont perdu des médias, pour **97 retraits** — dont **36 photos fournisseur (légitimes)** et **61 visuels maison (à tort)**. Cause racine : l'audit du 12/08 classait « fournisseur » tout média dont le fichier local n'était pas retrouvé, et une partie des retraits est passée par `fileDelete` (définitif) au lieu de `referencesToRemove`.
**Ce qui a été fait** : 34 médias maison ré-attachés ou ré-uploadés sur 15 fiches (dont les 4 tombées à 1 image), + 9 composites de coloris rattachés aux fiches enfants. Chaque visuel a été ouvert et zoomé avant rattachement ; aucune photo AliExpress brute n'a été rendue.
**Reste** : 10 fiches actives encore à 4/5 → **T-14**. Deux manques antérieurs au 12/08 (`remontoir-solo` 2/3, `bracelet-fkm-tropical` 1/3) → T-09.

### ~~T-02 — Retirer l'image à lettrage cursif de `trente-neuf-classique-cannelee`~~ ✅ FAIT le 12/08
**Compte rendu** : [`journal/2026-08-12-reparation-regressions-p0.md`](journal/2026-08-12-reparation-regressions-p0.md)
Lettrage cursif confirmé au zoom à 6 h sur le cadran. Média `59935462293842` **détaché** (pas supprimé : réversible), `alt` réécrit en avertissement. Preuves dans `preuves/2026-08-12-reparation-p0/`. La fiche n'est jamais restée sans image : les 7 composites de coloris ont été rattachés avant le détachement, elle porte aujourd'hui **7 visuels maison conformes** — aucun visuel de remplacement n'a eu à être généré.

### ~~T-03 — Contrôler tous les visuels produits les 11 et 12/08~~ ✅ FAIT le 12/08
**Compte rendu** : [`journal/2026-08-12-reparation-regressions-p0.md`](journal/2026-08-12-reparation-regressions-p0.md)
**Périmètre réel** : pas 12 images mais **572** (396 le 11/08, 176 le 12/08), soit **422 uniques** après déduplication. Toutes ouvertes, en cadre complet puis re-découpées à la résolution native sur les cas douteux.
**Trouvé** : **3 images non conformes, détachées** — même défaut sur les trois, les montres de mise en scène des visuels d'accessoires portent un **lettrage inventé sur le cadran** : `coffret-douze-presentation-situation`, `rouleau-de-voyage-noir-cuir-situation`, `remontoir-vitrine-vue-complete`. Détachement réversible, preuves et zooms dans `preuves/2026-08-12-reparation-p0/`.
**Consigné sans retrait** : le guichet de date « 42 » sur la famille Quarante-et-Un → **T-15**. Les retirer recréerait la régression que T-01 vient de réparer.
**Révélé** : 207 doublons morts dans la médiathèque → **T-18**. Deux fiches accessoires tombées à 2/3 → **T-14**.

---

## 🟧 À FAIRE — P1, le chantier principal

### T-04 — Réparer les 2 fiches arabes importées le 11/08
**État** : À FAIRE · **Pour** : Codex
**Pourquoi** : elles portent des **handles AliExpress bruts** et ne sont **rattachées à aucune collection** — donc invisibles pour le SEO et hors de la collection qui porte le mot-clé.
**Comment** : handle SEO français calé sur le vocabulaire de recherche, titre, description structurée, meta title et description, rattachement à `cadran-arabe`. Caractéristiques tirées des **données réelles relevées**, jamais inventées. Créer la redirection 301 si le handle change après indexation (ici sans objet, fiches en DRAFT).
**Sortie attendue** : 2 fiches conformes au standard des 94 autres, dans la bonne collection.

### ~~T-05 — Décider du sort du pilier « cadran arabe »~~ ✅ TRANCHÉ le 12/08 (Hakim)
**Décision** : **option 3 — le pilier arabe est déclassé.** La boutique se construit sur **cadran pilote** et **cadran stérile**, où l'offre suit. On **garde** les produits arabes déjà qualifiés (le volume de recherche le justifie) mais **on ne s'entête pas** : plus aucune passe de sourcing arabe.
**Suite** : une **recherche de mots-clés sérieuse par collection et par produit** sera menée plus tard — les volumes actuels sont des repères, pas une arborescence validée. → **T-21**
**Historique de la décision ci-dessous.**

⛔ NE PAS RELANCER DE RECHERCHE
**État** : ~~BLOQUÉ~~ TRANCHÉ · **Pour** : Hakim
**Pourquoi** : **le gisement est épuisé, ce n'est pas un manque d'effort.** Trois passes par l'API officielle (09, 10 et 11/08) : 80 recherches réussies sur 80, **676 identifiants distincts**, 104 fiches relues variante par variante, en douze langues (arabe, persan, ourdou, hindi, turc, russe…), sur toutes les cotes et tous les tris. Résultat : **3 produits qualifiés, le quatrième n'existe pas** dans l'inventaire atteignable. La plupart des cadrans vendus « arabic » portent en réalité des chiffres occidentaux ; le plus vendu (458 ventes) affiche `SUPERLATIVE CHRONOMETER` sur le cadran.
**Conséquence** : on ne peut aligner que **5 à 8 produits** derrière un mot-clé à 15 500 recherches/mois. C'est mince pour un pilier de boutique.
**Les trois options** :
1. **Assumer une collection courte** — 8 produits bien faits, en acceptant qu'elle ne porte pas la boutique à elle seule.
2. **Élargir la définition** — inclure les **montres finies** à cadran arabe, pas seulement les cadrans-pièces. Change la collection et le panier moyen.
3. **Déclasser le pilier** — garder la collection pour le SEO longue traîne et bâtir la boutique sur « cadran pilote » et « cadran stérile », où l'offre suit.
**Attention** : ⛔ **ne pas lancer de quatrième passe de sourcing arabe.** Ce serait dépenser pour reconfirmer un mur déjà documenté trois fois.
**Réf.** : `journal/2026-08-11-resourcing-cadrans-arabes-api-passe-finale.md`

### T-05b — Utiliser l'API AliExpress par défaut pour tout sourcing
**État** : À FAIRE · **Pour** : Claude ou Codex
**Pourquoi** : constat de Hakim (12/08) — piloter Chrome sur AliExpress consomme énormément. L'API officielle (AliExpress Open Platform / AE-Dropshipper via passerelle VPS en lecture seule) coûte une fraction et donne **mieux** : ventes réelles, prix exact par variante, stock à l'unité, fret France, délais, images de variantes pour la QA. C'est de la preuve classe A **sans navigateur**.
**Comment** : endpoints disponibles `health`, `search`, `variants`, `exact`. Pas de catalogue vendeur ni de `related` — pour les produits frères, filtrer les résultats de `search` sur l'identifiant vendeur. Le navigateur reste utile pour DSers uniquement.
**Sortie attendue** : cette règle inscrite dans `REGLES.md` et appliquée à tous les sourcings suivants.

### T-06 — Importer, rédiger et habiller le lot arabe
**État** : BLOQUÉ par T-05 · **Pour** : Codex
**Comment** : push DSers **tout en DRAFT** (⚠️ la case Draft se réarme à chaque lot — relire le DOM), relever id et handle réels, rédiger les fiches, produire les visuels maison.
**Sortie attendue** : collection cadran arabe à **10-12 produits réels**, habillés, prêts à activer.

### T-07 — Terminer les visuels des brouillons restants
**État** : À FAIRE · **Pour** : Codex · **Chiffré le 13/08 par T-16**
**Pourquoi** : les brouillons ne peuvent pas être activés tant qu'ils portent des photos AliExpress brutes.
**Périmètre exact** : sur les 95 brouillons, **43 sont déjà 100 % maison** (activables sur le seul critère visuel), **13 sont mixtes** et **39 n'ont que des photos brutes** — soit **60 fiches à traiter et 1 091 photos fournisseur à remplacer**. Le détail fiche par fiche est dans `preuves/2026-08-13-audit-brouillons/INVENTAIRE-95-BROUILLONS-2026-08-13.csv`.
**Comment** : pont d'ordres (`../ordres/`), ordre validé par `valider_ordre.py`, `generer-images.sh` (**code 2 = verrou : attendre, ne jamais forcer**). Priorité : cadrans stériles couleur, puis le reste des pilote 1-12. Compter 8-10 min par visuel en CLI, 2-3 min dans l'app.
**Sortie attendue** : plus aucun brouillon avec photo fournisseur brute.

### T-08 — Réécrire les `alt` génériques
**État** : À FAIRE · **Pour** : Codex
**Pourquoi** : `cadran-sterile-lumineux-28-5` porte des `alt` génériques — perte SEO et accessibilité.
**Comment** : `alt` descriptif en français, décrivant ce que l'image montre réellement. Balayer les autres fiches pour le même défaut.

### T-09 — Compléter les galeries des 96 fiches actives
**État** : À FAIRE · **Pour** : Codex · **Chantier long**
**Pourquoi** : cible maison de 5 images par montre et 3 par accessoire, non atteinte sur une partie du catalogue.
**Comment** : le brief chiffré est `journal/2026-08-08-consignes-codex-visuels.md` — **~319 visuels** (74 de galerie + 245 de variantes), **tous coloris conservés** (décision de Hakim du 08/08 : ne pas proposer de réduire).
**Sortie attendue** : aucune fiche active sous la cible.

---

### T-14 — Produire les vues manquantes des 12 fiches actives encore sous la cible
**État** : À FAIRE · **Pour** : Codex · **Né de** : T-01 et T-03 (12/08)
**Pourquoi** : après restauration et après retrait des trois visuels lettrés, douze fiches actives restent sous la cible. Aucun visuel maison conforme n'existe pour combler l'écart — il faut produire.
**Les dix montres à 4/5** : `quarante-et-un-{bleu-acier, noir-jaune-acier, noir-acier, blanc-cuir, bleu-cuir, noir-cuir}` · `trente-neuf-{rouge, vert, bleu, rose}`.
**Les deux accessoires à 2/3** : `coffret-douze-presentation` et `remontoir-vitrine` — leur visuel de situation a été détaché par T-03. Le remplacement doit montrer le produit **sans montre de mise en scène**, ou avec des cadrans strictement vierges.
**Attention** : ⚠️ pour les six `quarante-et-un`, **ne pas réutiliser les composites `c-495698-*` de la fiche mère** — voir T-15.
Pour `trente-neuf-{rouge, vert, bleu}`, le composite de coloris existe mais c'est un quasi-doublon du `01-face-sterile` déjà en galerie : produire une vue différente (situation, macro, détail de bracelet).
**Sortie attendue** : 10 visuels maison, `alt` FR, rattachés en fin de galerie.

### T-15 — Corriger le guichet de date « 42 » de la famille Quarante-et-Un
**État** : À FAIRE · **Pour** : Codex · **Né de** : T-01 et T-03 (12/08)
**Pourquoi** : **« 42 » dans le guichet de date** — une date qui n'existe pas. Le défaut touche deux générations de visuels : les six composites `c-495698-*` de la fiche mère `quarante-et-un-sport-acier` (en ligne depuis le 25/07) **et** les visuels produits le 12/08 pour les fiches enfants (`quarante-et-un-*-{macro, situation, poignet}`). Ce n'est aucun des interdits de `REGLES.md`, mais c'est une invraisemblance visible au zoom, répétée sur toute une famille.
**Preuve** : `preuves/2026-08-12-reparation-p0/defaut-guichet-date-42-c-495698.jpg`
**Pourquoi ils sont restés en ligne** : les retirer ferait retomber six fiches actives à une ou deux images — la régression que T-01 vient de réparer. On corrige, on ne détache pas.
**Comment** : régénérer ou retoucher les vues concernées avec une date plausible, remplacer sur la fiche mère et sur les six fiches enfants, puis servir T-14 avec les versions corrigées.

### ~~T-16 — Auditer les galeries des 95 brouillons après la session du 12/08~~ ✅ FAIT le 13/08 — **rien à réparer**
**Compte rendu** : [`journal/2026-08-13-audit-reparation-brouillons.md`](journal/2026-08-13-audit-reparation-brouillons.md)
**Le ticket partait d'une hypothèse fausse.** Sur les brouillons, la règle de classification défaillante est tombée sur des galeries **entièrement** composées de photos DSers : elle ne pouvait pas se tromper. **35 fiches touchées, 311 médias retirés — 311 photos AliExpress brutes, 0 visuel maison.** En échange, **146 visuels maison** ont été posés, et **chacune des 35 fiches couvre aujourd'hui toutes ses apparences** sans porter la moindre photo brute.
**Le dégât est de méthode, pas de contenu** : les **311 retraits sont passés par `fileDelete`** — les 311 GID interrogés répondent tous `null`, aucun n'est ré-attachable. C'est exactement ce que T-17 a interdit.
**Aucune mutation exécutée** : rien à restaurer (cas 1 : 0 occurrence), aucune apparence laissée orpheline (cas 2 : 0 occurrence — les 3 écarts apparents sont des groupes **techniques**, calibres et diamètres). Les 146 visuels ont été ré-ouverts un par un, planches + zooms cadran/couronne/lunette : aucun logo, aucun lettrage inventé, `alt` FR partout.
**Les 9 brouillons antérieurs au 08/08 n'ont rien perdu** (comptes identiques à `INVENTAIRE-VISUEL-2026-08-08.csv`) ; `aviateur-acier-cadran-chiffres-arabes` est même passé de 0 à 1 image.
**Reste** : les 311 sources fournisseur détruites → **T-23**. Chiffrage de T-07 mis à jour ci-dessous.

### T-23 — Reconstituer les sources fournisseur détruites, à la demande
**État** : À FAIRE · **Pour** : Codex · **Né de** : T-16 (13/08) · **Priorité basse, pas bloquant**
**Pourquoi** : les 311 photos AliExpress supprimées définitivement le 12/08 ne sont récupérables ni depuis Shopify ni depuis `livraisons/`. Elles ne manquent à aucune galerie — mais elles servaient de **matière première de composition**. Si l'un de ces 35 produits demande plus tard un visuel supplémentaire (autre angle, macro, mise en situation), la photo de base n'existe plus en local.
**Ce qui reste** : `sources-fournisseur-2026-08/` conserve **une** photo de face pour **33 des 35 fiches** — environ **10 %** du matériau détruit. **21 des 35 fiches** ont leur identifiant AliExpress tracé dans les lots d'exécution ; pour les **14 autres**, il faut d'abord le retrouver.
**Comment** : ne rien re-télécharger en masse. Au moment où un visuel supplémentaire est demandé sur l'une de ces 35 fiches, récupérer les photos d'origine **par l'API AliExpress** (règle T-05b), pas par le navigateur.
**Réf.** : `preuves/2026-08-13-audit-brouillons/311-medias-supprimes-definitivement.json` (fiche, nom de fichier, URL d'origine).

### T-18 — Purger les 207 doublons morts de la médiathèque
**État** : À FAIRE · **Pour** : Codex · **Né de** : T-03 (12/08)
**Pourquoi** : sur les 572 médias ajoutés les 11-12/08, **207 ne sont rattachés à aucun produit** : le même fichier a été uploadé deux fois, la seconde copie porte un suffixe UUID et n'a jamais été posée. Ce n'est pas un visuel manquant, c'est de l'encombrement.
**Attention** : ⚠️ vérifier fiche par fiche qu'aucune des deux copies n'est référencée avant d'agir, et **ne pas utiliser `fileDelete`** — voir la règle inscrite dans `REGLES.md` le 12/08.
**Comment** : croiser `files(query: created_at)` et les galeries produit ; la liste de travail est reconstructible par la méthode décrite dans `journal/2026-08-12-reparation-regressions-p0.md`.

### ~~T-17 — Interdire `fileDelete` sur les médias produit~~ ✅ FAIT le 12/08
Deux règles ajoutées à [`REGLES.md`](REGLES.md), section « Pièges déjà payés » : le retrait d'un média passe **toujours** par `fileUpdate` + `referencesToRemove`, jamais par `fileDelete` ; et une classification « fournisseur par défaut faute de fichier local » ne peut jamais déclencher un retrait.

---

## 🟨 À FAIRE — P2, avant lancement

### T-21 — Recherche de mots-clés sérieuse par collection et par produit
**État** : À FAIRE · **Pour** : Claude · **Décidé par Hakim le 12/08**
**Pourquoi** : les volumes utilisés jusqu'ici (15 500 pour « cadran arabe », 38 690 pour « seiko mod ») sont des **repères de sourcing**, pas une arborescence validée. Or l'arborescence décide des collections, des handles et des titres — la refaire après coup coûte des redirections et de l'autorité perdue.
**Comment** : SEMrush France par lots de 100 mots-clés + KMT par URL ; volume, KD et CPC par intention ; distinguer tête et longue traîne. Cibles Kraken : collection cœur ≥ 1000, secondaire ≥ 500, KD 0-2. Confronter aux collections existantes et proposer les fusions, scissions et renommages.
**Sortie attendue** : arborescence chiffrée définitive, liste des handles à changer **avec leurs redirections 301**, et priorisation des collections par potentiel réel.
**Attention** : à faire **avant** l'activation — changer un handle après indexation coûte cher.

### T-22 — Tester Nano Banana sur les visuels (test cadré)
**État** : À FAIRE · **Pour** : Claude · **Idée de Hakim, 12/08**
**Pourquoi** : évaluer si un autre modèle d'image donne de meilleurs résultats que l'exécutant actuel, dont la QA laisse passer des défauts (index promu en chiffre, repères de minuterie déformés, lettrage inventé).
**Comment** : prendre **3 à 5 sources fournisseur déjà traitées**, régénérer avec Nano Banana dans les mêmes conditions (composition depuis la photo fournisseur, seule la mise en scène change), et comparer à visuel identique : fidélité du cadran, respect des index, propreté des repères, absence de lettrage inventé.
**Sortie attendue** : verdict comparatif chiffré (défauts par lot), et recommandation de bascule ou non.
**Attention** : ⚠️ **ce test ne concerne PAS les 5 sources abandonnées.** Voir T-H5 — leur problème est le produit, pas la photo.

### T-13 — Ranger les ~30 fichiers de données restés à la racine
**Pour** : Codex · **Pourquoi** : les `MAPPING-*.json`, `RAPPORT-*.json`, `AUDIT-*.json`, `INVENTAIRE-*.csv` encombrent le point d'entrée. Ils n'ont pas été déplacés parce que **des scripts les lisent en chemin relatif** — les bouger à l'aveugle casserait ces scripts.
**Comment** : pour chaque fichier, `grep -rl "<nom>" scripts/ shopify/ ../ordres/` ; ceux qui ne sont lus par aucun script vont en `journal/data/`, les autres restent et sont documentés dans `journal/README.md`.
**Sortie attendue** : à la racine du dossier boutique, uniquement `TABLEAU.md`, `ETAT.md`, `REGLES.md` et les dossiers.

### T-10 — Installer la mesure d'achat
**Pour** : Claude + Hakim · **Pourquoi** : ni GA4 ni gtag. **Interdit de dépenser un euro en publicité sans mesure d'achat** — et le budget validé est de 30 €/jour.
**Comment** : `journal/2026-08-08-tracking-et-consentement.md`, 10 étapes au clic près. Voie retenue : app **Google & YouTube** — sur le plan Basic, le code de thème **ne peut pas voir l'achat** (caisse hors thème, pas de `checkout.liquid`). Hakim crée la propriété GA4 ; Claude ne crée aucun compte.
**Attention** : ⚠️ **ne pas laisser l'app créer le Merchant Center avant que le CSS soit arrêté.**

### T-11 — Solder les P0/P1 restants de l'audit GMC
**Pour** : Claude · **Comment** : reprendre `journal/2026-08-08-audit-gmc-final.md` point par point, vérifier ce qui a été corrigé depuis, traiter le reste.

### T-12 — Activation
**État** : BLOQUÉ · **Pour** : Hakim
**Pourquoi** : rien ne s'active tant que les cinq conditions ne sont pas **toutes** vraies :
- aucune fiche concernée ne porte de photo AliExpress brute ;
- les politiques sont collées et le médiateur renseigné (T-H1, T-H2) ;
- la grille de prix est arbitrée et appliquée (T-H3) ;
- la mesure d'achat est installée et testée (T-10) ;
- les P0/P1 de l'audit GMC sont soldés (T-11).
**Puis, dans l'ordre** : activer les produits → publier les collections sur le canal Online Store → retirer le mot de passe → ouvrir le compte CSS/Merchant Center.

---

## ✅ FAIT

| # | Ticket | Date | Compte rendu |
|---|---|---|---|
| — | Purge de conformité : 46 visuels de faux avis détachés (37 fiches), 931 prix barrés supprimés, 931 SKU AliExpress réécrits, « 904L » purgé avec redirections 301 | 08/08 | `journal/2026-08-08-*` |
| — | Sourcing + import DSers de 94 produits « Pièces & Mod » en DRAFT, montés en preuve classe A | 09/08 | `journal/2026-08-09-push-dsers.md` |
| — | 10 collections créées avec textes et métadonnées ; 94 fiches habillées en français | 09/08 | `journal/2026-08-09-textes-et-collections.md` |
| — | Passe de cohérence : 16 fiches sur 94 corrigées (écart texte/produit) | 09/08 | `journal/2026-08-09-coherence-fiches.md` |
| — | Archivage des 3 doublons, du cadran à verbatim Rolex et des fiches incohérentes | 11/08 | `journal/2026-08-11-audit-travail-codex.md` |
| — | Correction de la collection `montre-cadran-a-chiffres` et de la promesse fausse « tous les cadrans sont stériles » | 11/08 | idem |
| — | ~85 visuels maison rattachés sur les fiches actives, image 1 préservée | 10/08 | idem |
| — | Pack de 7 politiques légales préparé (3 demandées) | 10/08 | `livraisons/politiques-maison-noirmont-2026-08-10/` |

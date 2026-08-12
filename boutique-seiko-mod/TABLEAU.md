# Maison Noirmont — tableau

**Point d'entrée unique.** Tu commences ici, quel que soit l'agent. Format des tickets : [`../METHODE-TABLEAU.md`](../METHODE-TABLEAU.md).
État courant chiffré : [`ETAT.md`](ETAT.md) · Règles et pièges : [`REGLES.md`](REGLES.md) · Style : [`STYLE-REDACTION.md`](STYLE-REDACTION.md) · Archive : [`journal/`](journal/)

**Mets ce fichier à jour avant de rendre la main.** C'est la seule obligation qui ne se délègue pas.

Dernière mise à jour : **13/08/2026** — régressions P0 réparées ; audit des 95 brouillons soldé (T-16) ; **recherche de mots-clés faite (T-21) : l'arborescence actuelle est à refaire, 4 collections sur 10 ne portent aucun volume**.

---

## 🔴 BLOQUÉ — attend Hakim

### ~~T-H1 — Coller les 7 politiques légales~~ ✅ FAIT le 12/08 (Hakim)
**Pour** : Hakim · **Pourquoi** : les CGV et la politique de remboursement servies portent **encore la clause interdite** (« portés… ne sont pas repris »), qui contredit le « 14 jours satisfait ou remboursé même si portée » affiché ailleurs. C'est la contradiction qu'un examinateur Merchant Center voit en premier.
**Comment** : ouvrir `livraisons/politiques-maison-noirmont-2026-08-10/`, coller chaque texte dans *Réglages → Politiques*. Le connecteur ne peut pas le faire : permission `write_legal_policies` absente.
**Sortie attendue** : les 7 politiques à jour sur la boutique.

### ~~T-H2 — Adhérer à un médiateur de la consommation~~ ✅ FAIT le 12/08 (Hakim)
**Pour** : Hakim · **Pourquoi** : obligation légale française ; l'article 17 des CGV porte encore `[À COMPLÉTER]`.
**Sortie attendue** : nom et coordonnées du médiateur intégrés aux CGV.

### T-25 — Arbitrer le « 904L » gravé sur un bracelet
**État** : À FAIRE · **Pour** : Hakim · **Trouvé le 13/08 pendant la récupération des sources**
**Pourquoi** : `montre-sterile-40-nh35-saphir` porte **`904L` imprimé sur le bracelet du produit physique**. Or on a purgé « 904L » de toute la boutique le 08/08 — c'est une allégation d'acier invérifiable, et improbable à ce prix. Le texte ne la revendique donc plus, mais **le visuel la montrera** dès qu'on produira une macro de bracelet.
**La tension** : notre règle dit qu'un mot générique physiquement gravé se garde (on ne modifie pas le produit), mais `904L` n'est pas générique — c'est une **allégation de matière**, de la même famille qu'une mention d'origine.
**Les options** : ① ne jamais cadrer le bracelet sur cette fiche (contournement fragile) · ② abandonner le produit comme les cadrans à verbatim · ③ l'assumer en le décrivant honnêtement, ce que je déconseille : on afficherait une allégation qu'on a nous-mêmes jugée invérifiable.
**Recommandation de Claude** : option 2. C'est une seule fiche, et c'est exactement le type de détail qu'un examinateur relève.

### T-H3 — Arbitrer la grille de prix
**Pour** : Hakim · **Pourquoi** : plusieurs coûts réels sont **inférieurs** aux estimations (9,19 € contre 18,49 € sur un exemple) — le pricing prévu est à re-caler, probablement en ta faveur. Aucun prix n'a été écrit.
**Comment** : lire la partie 3 de `journal/2026-08-09-textes-et-collections.md` — deux stratégies chiffrées (encaisser la marge / baisser le ticket d'entrée) avec recommandation.
**Contrainte ajoutée le 13/08 par T-21** : les CPC réels par collection sont mesurés (aiguilles 0,10 € · cadran 0,17 € · outils 0,20 € · mouvement 0,21 € · verre 0,30 € · **boîtier 0,64 €**). Le ratio prix ÷ CPC ≥ 100 impose donc : **outils ≥ 19,90 €**, **verres saphir ≥ 29,90 €** et **tout boîtier ≥ 64 €**. En dessous, la règle Kraken est cassée.
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
**Reste** : les 311 sources fournisseur détruites → **T-23, soldé le 13/08, les 311 sont revenues.** Chiffrage de T-07 mis à jour ci-dessous.

### ~~T-23 — Reconstituer les sources fournisseur détruites~~ ✅ FAIT le 13/08 — **311/311 revenues**
**Compte rendu** : [`journal/2026-08-13-recuperation-sources-api.md`](journal/2026-08-13-recuperation-sources-api.md)
**Fait en une passe, sur décision de Hakim** de réapprovisionner avant la reprise de génération du 18/08, au lieu du re-téléchargement à la demande prévu au ticket. **Les 311 photos détruites sont toutes revenues**, plus 11 images de variantes absentes des galeries : **322 images, 128 Mo, 35 fiches sur 35**. Le stock local passe d'environ 10 % du matériau à **100 %**.
**Les 35 identifiants AliExpress sont établis**, pas devinés : 30 par **recoupement d'image exact** (un nom de fichier détruit retrouvé dans la réponse `variants` de l'API), 5 par titre officiel + deux registres locaux concordants. **0 fiche laissée sans source.** Le chiffrage « 21 tracés / 14 à retrouver » était pessimiste : `textes-fiches-2026-08-09.json` et les noms `face-fournisseur-<item_id>.jpg` portaient déjà 33 identifiants, concordants.
**Piège écarté** : `PREFLIGHT-DSERS-CADRAN-ARABE-1005007347658552-2026-08-11.json` rattache l'item `1005007347658552` au produit `11017842360658` (`new-arabic-sky-blue-…`) — **c'est faux**, 0 image en commun contre 25/26 pour `1005009751528666`. Suivre ce fichier aurait produit des visuels d'un autre produit.
**QA** : 322 images relues en 35 planches, agrandissement cadran par cadran. **Aucune écartée** : aucun logo, marque, certification ni mention d'origine sur un cadran. ⚠️ Deux vigilances pour l'exécutant d'images : le filigrane **`Tandorio`** sur `cadran-pilote-33-5-aiguilles-lumineuses` et **`alpha dial`** sur `cadran-pilote-sterile-28-5-sans-logo` sont sur la photo, pas sur le produit — ne jamais les laisser passer dans une composition ; et **`904L` imprimé sur le bracelet** de `montre-sterile-40-nh35-saphir` ne doit apparaître dans aucun livrable (purgé de la boutique le 08/08).
**Table de correspondance** : `journal/data/table-correspondance-handle-aliexpress.csv`, **96 lignes**, versionnée — les 94 fiches du lot du 09/08 plus les 2 imports du 11/08. ⚠️ **à reprendre quand T-04 renommera les deux handles bruts** : la clé est le `handle`.
**Aucune écriture Shopify, aucune commande, aucun navigateur.** Les sources restent dans `sources-fournisseur-2026-08/`, gitignoré, avec `MANIFESTE-RECUPERATION-2026-08-13.json` (tailles et SHA-256).

### T-18 — Purger les 207 doublons morts de la médiathèque
**État** : À FAIRE · **Pour** : Codex · **Né de** : T-03 (12/08)
**Pourquoi** : sur les 572 médias ajoutés les 11-12/08, **207 ne sont rattachés à aucun produit** : le même fichier a été uploadé deux fois, la seconde copie porte un suffixe UUID et n'a jamais été posée. Ce n'est pas un visuel manquant, c'est de l'encombrement.
**Attention** : ⚠️ vérifier fiche par fiche qu'aucune des deux copies n'est référencée avant d'agir, et **ne pas utiliser `fileDelete`** — voir la règle inscrite dans `REGLES.md` le 12/08.
**Comment** : croiser `files(query: created_at)` et les galeries produit ; la liste de travail est reconstructible par la méthode décrite dans `journal/2026-08-12-reparation-regressions-p0.md`.

### ~~T-17 — Interdire `fileDelete` sur les médias produit~~ ✅ FAIT le 12/08
Deux règles ajoutées à [`REGLES.md`](REGLES.md), section « Pièges déjà payés » : le retrait d'un média passe **toujours** par `fileUpdate` + `referencesToRemove`, jamais par `fileDelete` ; et une classification « fournisseur par défaut faute de fichier local » ne peut jamais déclencher un retrait.

---

## 🟨 À FAIRE — P2, avant lancement

### ~~T-21 — Recherche de mots-clés sérieuse par collection et par produit~~ ✅ FAIT le 13/08
**Compte rendu** : [`journal/2026-08-13-recherche-mots-cles.md`](journal/2026-08-13-recherche-mots-cles.md)
**Mesure** : 300 mots-clés SEMrush France en 3 lots de 100, 300 crédits sur 1 000, + 8 familles au Keyword Magic Tool. Liste dérivée du catalogue, fiche par fiche.
**Ce qui est établi** :
- **Les trois piliers de cadran n'existent pas comme requêtes françaises.** `cadran pilote` **n/a**, `cadran stérile` **n/a**, `cadran arabe` **20**, `cadran squelette` **20**. La décision du 12/08 (déclasser l'arabe au profit de pilote et stérile) **n'améliore rien** : on échange un zéro contre deux zéros.
- **Ce qui existe, c'est l'organe en français simple** : `cadran de montre` 480 (famille 4 400) · `boitier montre` 1 600 (2 650) · `mouvement nh35` 590 (5 540) · `verre saphir montre` 480 (2 770) · `outil horloger` 390 (2 980) · `lunette montre` 390 (600) · `aiguilles montre` 140 (770).
- **Le pilier qu'on n'avait pas vu est la montre finie** : `montre squelette homme` **2 900** contre `cadran squelette` 20 ; `montre aviateur` **1 600** contre `cadran pilote` 0 ; grappe chiffres arabes côté montre ≈ **9 500**.
- **Défaut systémique** : **84 titres sur 94** et **88 meta titles sur 94** ne contiennent pas le mot « montre » — le mot pivot de toutes les requêtes mesurées à volume non nul.
- **Zéro autorité à perdre** : boutique sous mot de passe, collections non publiées, fiches en brouillon → aucune URL indexée, les renommages sont gratuits aujourd'hui. C'est la fenêtre que ce ticket devait saisir.
**Suites créées** : **T-24** (arborescence), **T-25** (titres), **T-26** (pilier montres finies), **T-27** (contenu). Contrainte nouvelle transmise à **T-H3** (ratio prix ÷ CPC).

### T-24 — Appliquer la nouvelle arborescence
**État** : À FAIRE · **Pour** : Claude ou Codex · **Né de** : T-21 (13/08) · **Avant l'activation**
**Pourquoi** : 4 collections de premier niveau sur 10 ne portent aucun volume mesurable (arabe, pilote, stérile, squelette). Les têtes réelles sont les organes en français simple.
**Comment** : 3 fusions (les 4 collections de cadran deviennent **une** collection `cadran-de-montre` à 44 produits + 4 sous-collections), 5 renommages de handle (`pieces-mod-nh35` → `pieces-detachees-montre`, `boitier-nh35` → `boitier-de-montre`, `aiguilles-nh35` → `aiguilles-de-montre`, `insert-lunette-38mm` → `lunette-de-montre`), **8 redirections 301** listées au §6 du compte rendu. `mouvement-nh35`, `verre-saphir-montre` et `outils-d-horloger` ne bougent pas.
**Attention** : ⚠️ **ne pas renommer les 94 handles produit** — les manifestes, mappings DSers et scripts de visuels les référencent. Seules 3 fiches ont un handle qui contredit le produit (liste au §6).

### T-25 — Réécrire les 94 titres et meta titles
**État** : À FAIRE · **Pour** : Codex · **Né de** : T-21 (13/08)
**Pourquoi** : 84 titres sur 94 ratent le mot « montre ». « Cadran pilote 33,5 mm » cible une expression mesurée à **zéro** et rate `cadran de montre` (480).
**Comment** : règle `<Organe> de montre <cote> <caractéristique> — <coloris>, pour <calibre>`, plafond **65 caractères** sur le `seo.title` (il devient le titre du flux Shopping). Les 94 titres proposés sont écrits au §7 du compte rendu, fiche par fiche, avec leur mot-clé cible et son volume.
**Attention** : ⚠️ `aiguilles-c3-super-lume-62` — `super luminova` pèse **320**, le plus fort de la famille aiguilles ; ne l'écrire dans le titre **que si le fournisseur documente vraiment de la Super-LumiNova**, sinon rester sur « luminescence C3 ».

### T-26 — Instruire le pilier « montres finies »
**État** : À FAIRE · **Pour** : Claude · **Né de** : T-21 (13/08) · **Décision de Hakim attendue**
**Pourquoi** : le catalogue de 91 pièces n'est pas un pilier de trafic — c'est un catalogue de panier moyen. Le volume est côté montre finie : squelette **5 780** (2 fiches actives seulement), chiffres arabes **9 500**, aviateur/pilote **2 630** (aucune collection).
**Comment** : étoffer `montre-squelette`, créer une collection aviateur, corriger `montre-cadran-a-chiffres` (elle porte encore « nous n'en proposons pas »). Reclasser les **3 montres finies rangées dans la collection de pièces `cadran-arabe`** (§8 du compte rendu).
**À dire à Hakim** : la règle « aucune marque tierce » rend inaccessibles ≈ **17 500 recherches/mois** (`seiko mod` 8 100, `seiko arabic dial` 8 100, `seiko nh35` 590, `seiko chiffre arabe` 390). La règle reste juste — mais la voie légale existe : le **contenu éditorial** peut citer Seiko factuellement là où le titre de flux ne le peut pas.

### T-27 — Plan de contenu sur les intentions informationnelles
**État** : À FAIRE · **Pour** : Claude · **Né de** : T-21 (13/08)
**Pourquoi** : sur cette niche, l'article de fond bat la page de collection — un seul guide fait **66 %** du trafic de `goteia.fr`. Les trois familles mesurées où l'intention est informationnelle et le volume réel : `changer le verre d'une montre` (famille 5 070, modificateur `changer` 180), `comment ouvrir un boîtier de montre` (famille 9 480, `ouvrir` 223), `dans quel sens tournent les aiguilles` (famille 24 440, `sens` 498).

### T-22 — Tester Nano Banana sur les visuels (test cadré)
**État** : À FAIRE · **Pour** : Claude · **Idée de Hakim, 12/08**
**Pourquoi** : évaluer si un autre modèle d'image donne de meilleurs résultats que l'exécutant actuel, dont la QA laisse passer des défauts (index promu en chiffre, repères de minuterie déformés, lettrage inventé).
**Comment** : prendre **3 à 5 sources fournisseur déjà traitées**, régénérer avec Nano Banana dans les mêmes conditions (composition depuis la photo fournisseur, seule la mise en scène change), et comparer à visuel identique : fidélité du cadran, respect des index, propreté des repères, absence de lettrage inventé.
**Sortie attendue** : verdict comparatif chiffré (défauts par lot), et recommandation de bascule ou non.
**Attention** : ⚠️ **ce test ne concerne PAS les 5 sources abandonnées.** Voir T-H5 — leur problème est le produit, pas la photo.

### T-24 — Réécrire tout le contenu SEO du catalogue
**État** : BLOQUÉ par T-21 (a besoin de ses chiffres) · **Pour** : Claude · **Spec dictée par Hakim le 13/08**
**Pourquoi** : les 10 textes de collection et les 94 descriptions ont été écrits en une nuit, depuis des données fournisseur, sans mots-clés mesurés. Ils portent les marqueurs de l'écriture IA — reconnaissables par Google comme par le lecteur — et ne visent aucun mot-clé validé. C'est le chantier qui décide du référencement de la boutique.
**Comment** :
1. **Rangement d'abord** : chaque produit dans la bonne collection, d'après le mot-clé cible établi par T-21. Les fiches dont le mot-clé appartient à une autre collection sont déplacées.
2. **Textes de collection** — 300 à 500 mots, structure : ce que couvre la catégorie → **comment choisir** (le passage qui fait le référencement) → les sous-familles → les erreurs fréquentes.
3. **Descriptions produit** — 150 à 300 mots, structure : à quoi ça sert → compatibilité et dimensions → matière et finition → à savoir avant d'acheter.
4. **Mot-clé cible** présent dans le titre, le premier paragraphe, un intertitre et la meta description. Naturellement.
5. **Gras sur ce qui aide à décider** : calibre, cote en mm, matière, contenu de la livraison. Jamais sur un adjectif.
6. **Purge de l'écriture IA** : voir [`STYLE-REDACTION.md`](STYLE-REDACTION.md) — tirets cadratins, « que vous soyez », « plongez dans », tricolons, superlatifs vides, conclusions qui résument. C'est une **passe de suppression**, pas seulement d'ajout.
7. Meta title et meta description refaits pour chaque page touchée.
**Sortie attendue** : catalogue rangé, 10 textes de collection et ~200 fiches réécrits, sauvegarde des contenus précédents avant écrasement.
**Attention** : ⚠️ aucune spécification inventée (donnée manquante = non affirmée) · aucun avis ni chiffre de satisfaction · les brouillons restent en DRAFT · **les changements de handle passent par T-21 et ses redirections 301**, pas par ce ticket.
**Réf.** : `STYLE-REDACTION.md`, `REGLES.md`, sortie de T-21.

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

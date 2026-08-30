---
type: journal
boutique: seiko-mod
date: 2026-08-08
nature: analyse
leviers: [creative]
titre: "Brief de production visuelle — Maison Noirmont"
---

# Brief de production visuelle — Maison Noirmont

> **08/08/2026.** Destinataire : **Codex**. Boutique `v42pzp-h4.myshopify.com` / `maisonnoirmont.fr`.
> Fait suite au retrait des 46 visuels de faux avis (`2026-08-08-retrait-visuels-faux-avis.md`) qui a laissé
> plusieurs galeries trop maigres. Décision de Hakim : **tout régénérer d'un coup** plutôt qu'au cas par cas.
>
> **Audit d'origine : lecture seule.** Les 105 fiches ont été relues via l'API Admin, aucune écriture.
> L'inventaire ligne à ligne est dans **`INVENTAIRE-VISUEL-2026-08-08.csv`** (105 lignes, même dossier).

---

## 1. Périmètre chiffré

### 1.1 État du catalogue au 08/08/2026

| | Nombre |
|---|---:|
| Fiches produit | **105** (96 actives, 9 brouillons) |
| Dont montres (automatique + chronographe) | **63** |
| Dont accessoires, bracelets, rangement, outillage, carte cadeau | **42** |
| Médias produit attachés (associations distinctes fiche↔image) | **455** |
| Variantes toutes fiches confondues | **935** (883 sur fiches actives) |
| Variantes portant une image | **330** |
| Variantes sans aucune image | **605** |
| Fiches sans aucun texte alternatif renseigné | **0** — les 455 médias ont tous un `alt` |

### 1.2 Classement des galeries

Classement brut demandé (critique 0-1 · insuffisante 2-3 · correcte 4+) :

| Famille | critique (0-1) | insuffisante (2-3) | correcte (4+) | total |
|---|---:|---:|---:|---:|
| Montres | 3 | 0 | 60 | 63 |
| Accessoires | 3 | 34 | 5 | 42 |
| **Total** | **6** | **34** | **65** | **105** |

Distribution complète du nombre d'images par fiche :

| Images | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 | 11 | 12 | 14 | 15 | 25 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Fiches | 1 | 5 | 14 | 20 | 41 | 12 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 |

### 1.3 Lecture par rapport à la cible maison

Le standard constaté avant nettoyage était **5-6 images pour les montres, 2-3 pour les accessoires**.
Attention : sur les montres, les 6ᵉ et 7ᵉ images de l'ancienne norme étaient précisément le bandeau
« 4,8/5 · 1340 avis » et le faux témoignage — **elles ne doivent pas être reconstituées**. La cible tenable
est donc **5 pour une montre** (face · en situation · macro · au poignet · détails et finitions) et
**3 pour un accessoire** (produit · en situation · macro).

| Famille | Cible | Au-dessus ou à la cible | Sous la cible | Visuels de galerie manquants |
|---|---:|---:|---:|---:|
| Montres | 5 | 19 | **44** | **54** |
| Accessoires | 3 | 25 | **17** | **20** |
| **Total** | | **44** | **61** | **74** |

La composition dominante actuelle est **4 images** (`face` + `en situation` + `macro` + `au poignet`)
sur 41 fiches montres actives : il leur manque la 5ᵉ, « détails et finitions ».

### 1.4 Le reliquat des « 88 visuels de variantes » du bilan du 25/07

**Oui, il est toujours d'actualité — et il a grossi.** Le chiffre de 88 datait d'un catalogue de 44 fiches ;
il y en a 105 aujourd'hui, dont les 13 fiches accessoires et les nouvelles familles Éclaireur / Explorateur /
Squelette entrées depuis.

Compté correctement — c'est-à-dire **par valeur d'option visuelle** (cadran, couleur, matière, capacité…) et non
par variante, puisque plusieurs variantes de mouvement partagent le même visuel :

| | Nombre |
|---|---:|
| Fiches dont l'option visuelle n'est pas couverte | **39** |
| Visuels de variantes manquants — **total** | **245** |
| dont montres | 43 |
| dont accessoires et bracelets | 202 |

Les options qui ne changent rien à l'image (`Mouvement & fond`, `Taille & fond`, `Mouvement`) sont exclues du
compte : elles expliquent l'essentiel des 605 variantes sans image et **ne demandent aucune production**.

À noter : sur 29 fiches, **toutes les variantes pointent vers une seule et même image** (celle de la face).
Ce n'est pas un manque technique mais un manque visuel : le client qui change de cadran voit la même photo.

---

## 2. Ce qui est récupérable sans rien produire

Bilan volontairement sec : **quasiment rien**.

### 2.1 Fichiers Shopify non rattachés — 63 fichiers, 0 réutilisable en galerie

Le catalogue Fichiers compte **518 images**, dont **455 attachées** à un produit. Les **63 orphelines** se
répartissent ainsi :

| Groupe | Nb | Verdict |
|---|---:|---|
| Faux témoignages et bandeaux « 4,8/5 · 1340 avis » (`…-6.jpg`, `…-7.jpg`, `gmt-6/7.jpg`) | **18** | **INTERDITS** — c'est ce qu'on vient de purger. Ne jamais réattacher. |
| Pastilles de variantes 156×156 (`noirmont-swatch-chrono-*`, `-gmt-*`) | 29 | Métaobjets d'options, pas des images produit. Hors périmètre. |
| Visuels de collection et de page d'accueil (`noirmont-hero`, `-plongeuses`, `-classiques`, `-chronos`, `-sport-chic`, `-accessoires`, `-maison`, `-gmt`) | 8 | Utilisés par le thème. Non réaffectables à une fiche. |
| Logos, wordmark, favicon | 4 | Identité de marque. |
| Fichiers AliExpress bruts résiduels (`S533c0e…webp` etc., 1000-1200 px) | 4 | **Matière première uniquement** — jamais publiables (voir règle 2). |

**Conclusion : zéro visuel produit récupérable tel quel dans les Fichiers Shopify.** Le nettoyage du 08/08 n'a
laissé aucune image saine détachée : les 18 fichiers détachés portent tous un avis ou une note fabriquée.

### 2.2 Visuels fournisseur (DSers / AliExpress)

**Ils ne sont pas « récupérables » au sens de « publiables ».** Voir la règle 2 ci-dessous : la photo fournisseur
est le **point de départ** de la production, jamais le livrable. La passe du 25/07 avait d'ailleurs supprimé
**351 médias AliExpress** de la boutique — il n'en reste que 4 fichiers orphelins.

Ce qui est disponible, c'est le **matériau source**, à retélécharger depuis les fiches fournisseur. Les URL
AliExpress par fiche sont déjà consignées dans le repo :

- `2026-07-25-sourcing-familles-v2.md` — familles montres
- `2026-07-25-sourcing-accessoires-v2.md` et `2026-07-25-sourcing-accessoires-v3.md` — accessoires et bracelets
- `2026-07-31-sourcing-arabes-squelettes.md` · `2026-07-31-sourcing-chiffres-orientaux.md` · `2026-07-31-sourcing-configurateur.md`
- `2026-07-25-dsers-mapping-decoupage.md` · `2026-07-31-dsers-mapping-lot2.md` — correspondance fiche ↔ variante ↔ SKU
- `boutique-seiko-mod/preuves/preuves-fournisseur-2026-07-27/` — captures de fiches fournisseur

C'est là que se trouvent les **nuanciers de coloris** dont on a besoin pour les 202 visuels de variantes
accessoires/bracelets (36 coloris de FKM tropical, 36 de caoutchouc gaufré, 16 de cuir daim, etc.).

### 2.3 Récapitulatif « à récupérer » vs « à produire »

| | Nombre |
|---|---:|
| **À récupérer** (image maison saine, déjà dans les Fichiers, à simplement rattacher) | **0** |
| **À produire** — visuels de galerie | **74** |
| **À produire** — visuels de variantes | **245** |
| **Total à produire** | **319** |

---

## 3. Règles de production — non négociables

> Ces quatre règles priment sur toute considération esthétique. Un visuel qui en viole une ne doit pas être
> intégré, même s'il est plus beau que l'existant.

### Règle 1 — Aucun logo, aucune marque, aucun sigle sur les cadrans

**Piège vérifié sur ce projet, plusieurs fois.** Les modèles d'image impriment spontanément de faux logos de
marques horlogères sur les cadrans, même quand rien ne le demande — c'est la leçon versée au campement type le
25/07 (« ne jamais utiliser un modèle UGC/mode pour du packshot : il fabrique de faux logos »).

Les montres de Maison Noirmont sont **stériles**, sans aucune inscription de marque. Donc :

- **contrôle cadran par cadran, à l'image, avant toute intégration** — pas au nom de fichier, pas au prompt ;
- inspecter aussi la lunette, la couronne, le fermoir et le fond de boîte : le logo peut migrer ;
- au moindre doute sur une inscription, le visuel est **rejeté**, pas retouché à la va-vite ;
- rappel de conformité : 12 variantes GMT à logo de marque tierce sont déjà rendues invendables pour cette
  raison exacte. On ne réintroduit pas le problème par l'image.

### Règle 2 — Méthode maison : composition à partir de la photo fournisseur, jamais invention

C'est la méthode en vigueur depuis le début du projet. Elle a deux volets, également contraignants.

**a) Le produit est repris tel quel depuis la photo fournisseur.**
Cadran, index, aiguilles, guichet de date, lunette, boîtier, bracelet, fermoir, couleur, fond de boîte : tout
cela vient de l'image réelle du produit et **n'est jamais réinventé**. On ne fait pas générer une montre à
partir d'une description. C'est de la **composition / inpainting à partir du réel**.

**Seule la situation change** : le fond, le décor, la mise en scène, la lumière, le contexte de port. Le produit,
lui, est constant et fidèle.

Cette méthode est ce qui garantit la fidélité au produit réellement livré. Un visuel qui embellit ou modifie le
produit — mauvais calibre affiché, mauvaise teinte de cadran, mauvais bracelet, mauvais fond de boîte — est une
**misrepresentation Merchant Center**, au même titre que les faux avis qu'on vient de retirer.

**b) On ne publie JAMAIS la photo AliExpress brute du fournisseur sur le site.** Sous aucun prétexte, même
« en attendant », même pour une fiche en brouillon. Deux raisons :

1. **Google sait rapprocher ces images.** Elles sont identiques sur des dizaines de boutiques dropshipping ;
   les publier, c'est se ranger explicitement dans ce lot.
2. **Le client les reconnaît aussi.** C'est un tueur de crédibilité et un signal de revente non différenciée,
   incompatible avec le positionnement Maison Noirmont.

**La photo fournisseur est un matériau de départ, jamais un livrable.** Toute image mise en ligne doit avoir été
retravaillée : nouveau fond, nouvelle scène, nouvelle lumière, cadrage et rendu maison.

### Règle 3 — Aucun avis, note, étoile, badge ni chiffre de satisfaction incrusté

C'est exactement ce qu'on vient de purger de 37 fiches. Sont bannis **dans les pixels** :

- étoiles, notes (`4,8/5`), volumes d'avis (`1340 avis`), badges façon organisme tiers ;
- témoignages clients : citation, prénom, ville, portrait ;
- tout chiffre de satisfaction, de classement ou de popularité.

La boutique compte **0 commande**. Aucune note agrégée n'est défendable aujourd'hui, quelle qu'en soit la forme.
Les avis ne reviendront que par une app d'avis vérifiés, après des commandes réelles.

Bannis également, par prudence Merchant Center : les mentions promotionnelles incrustées (`-30 %`, `PROMO`,
`LIVRAISON OFFERTE`), qui tombent sous la même règle « no promotional overlay ».

**Cas limite à connaître** : les visuels `…-3`, `…-4`, `…-5` existants portent parfois une **légende technique**
incrustée (ex. « Lunette cannelée · Acier poli »). Elle ne mentionne ni avis ni note, elle a donc été laissée en
place. **Ne pas en produire de nouvelles** tant que Hakim n'a pas tranché (voir §6).

### Règle 4 — Format, ratio et poids alignés sur l'existant

Caractéristiques relevées sur les **455 médias produit réellement en ligne** — la conformité est totale, il n'y
a aucune exception à imiter :

| Caractéristique | Valeur constatée |
|---|---|
| Dimensions | **2048 × 2048 px**, sur 100 % des médias produit |
| Ratio | **1:1 strict** |
| Format | **JPEG** (`image/jpeg`), 100 % des médias produit |
| Poids médian | **~707 Ko** |
| Poids constaté | 157 Ko → 1,27 Mo ; 73 % entre 300 Ko et 900 Ko |
| Espace colorimétrique | sRGB |
| Texte alternatif | **obligatoire**, 455/455 renseignés |

**Consignes de sortie :**

- livrer en **2048 × 2048, JPEG, sRGB**, viser **400-900 Ko**, ne jamais dépasser **1,2 Mo** ;
- ne pas livrer en WebP ni en PNG pour une image produit (le PNG reste réservé aux pastilles 156 × 156) ;
- **texte alternatif systématique**, au format maison :
  `<Titre de la fiche> — <angle> — Maison Noirmont`, où l'angle est
  `face` / `en situation` / `macro` / `au poignet` / `détails et finitions` ;
  **jamais** de mot appartenant au champ des avis (`avis`, `témoignage`, `étoile`, `note`, `4,8/5`) ;
- nomenclature de fichier : `<handle-de-la-fiche>-<NN>-<angle>.jpg`
  (ex. `integrale-vert-sport-chic-acier-05-details.jpg`), conforme à l'existant ;
- **ne jamais réutiliser les suffixes `-6` et `-7`** : ils sont brûlés, ils désignaient les faux avis.

---

## 4. Liste priorisée des fiches

### P0 — Fiches critiques, actives, à traiter en premier (5 fiches)

Elles sont en vente avec 0 ou 1 image. Deux d'entre elles ont été appauvries par le nettoyage du 08/08.

| Fiche | Famille | Images | Manque | Note |
|---|---|---:|---:|---|
| **Intégrale Vert — Sport chic acier** | Montre | 1 | +4 | Appauvrie par le retrait du 08/08. Trop pauvre pour un flux Shopping. |
| **Trente-Neuf Rose — Classique cannelée** | Montre | 1 | +4 | Préexistant. |
| **Bracelet FKM — tropical** | Bracelet | 1 | +2 | 108 variantes, 36 coloris, aucun visuel de variante. |
| **Rouleau de Voyage Vert — cuir** | Accessoire | 1 | +2 | |
| **Carte cadeau Maison Noirmont** | Carte cadeau | 1 | +2 | À arbitrer : une carte cadeau se passe peut-être d'une galerie (§6). |

### P1 — Montres actives à 4 images : ajouter la 5ᵉ (41 fiches, 41 visuels)

Toutes ont `face` + `en situation` + `macro` + `au poignet`. Il manque **« détails et finitions »**.

Contre-la-montre (Argent, Bleu glacier, Compteurs bleus, Gris anthracite, Rose poudré) · Explorateur ·
Héritage (Bleu, Bleu nuit, Vert) · Intégrale (Blanc argenté, Bleu ciel, Bleu nuit, Brun or rose, Noir,
Turquoise) · Noirmont Un · Noirmont Un Bronze · Quarante-et-Un (Blanc, Bleu, Bleu Acier, Noir, Noir Acier,
Noir & Jaune Acier) · Squelette Carré · Squelette Octogone · Trente-Neuf (Bleu mer, Noir, Duo Doré) ·
Trente-Six (Bleu, Doré, Or intégral, Rose, Rouge) · Voyageur (Bicolore cadran brun, Bicolore 3 maillons,
Bicolore 5 maillons, Or rose 5 maillons, Or 3 maillons, Or Président) · Éclaireur Acier · Éclaireur Bronze.

### P2 — Accessoires actifs à 2 images : ajouter la 3ᵉ (14 fiches, 14 visuels)

Coffret Douze — aluminium · Coffret Douze — présentation · Doigtiers d'horloger — latex ·
Pince à barrettes · Remontoir Bois Acajou · Remontoir Collection Bois beige · Remontoir Collection Bois noir ·
Remontoir Collection Bois LED rouge · Remontoir Collection Cuir PU · Remontoir Solo · Remontoir Vitrine — 4+6 ·
Rouleau de Voyage Bleu marine · Rouleau de Voyage Brun · Rouleau de Voyage Noir.

### P3 — Visuels de variantes, montres (5 fiches, 43 visuels)

Le client change de cadran et voit la même photo : c'est le manque le plus visible commercialement.

| Fiche | Option | Valeurs | Couverts | Manque |
|---|---|---:|---:|---:|
| Explorateur — Sport chic à chiffres 3-6-9 | Cadran | 13 | 1 | **12** |
| Éclaireur Acier — Field à chiffres 1-12 | Cadran | 11 | 1 | **10** |
| Éclaireur Bronze — Field militaire à chiffres 1-12 | Cadran | 9 | 1 | **8** |
| Squelette Carré / Squelette Octogone | Cadran | 2 chacune | 1 | **1 + 1** |
| Trente-Neuf Duo — Classique bicolore | Boîtier | 2 | 1 | **1** |
| *(brouillons)* Noirmont Deux · Voyageur | Référence / Boîtier & bracelet | 7 / 3 | 0 | **7 + 3** |

### P4 — Visuels de variantes, accessoires et bracelets (34 fiches, 202 visuels)

Le gros du volume. Les nuanciers fournisseur existent : c'est du **retraitement de coloris**, pas de la création.

| Fiche | Option | Valeurs | Manque |
|---|---|---:|---:|
| Bracelet caoutchouc gaufré | Band Color | 36 | **36** |
| Bracelet FKM — tropical | Couleur | 36 | **36** |
| Bracelet cuir daim — dégagement rapide | Band Color | 16 | **16** |
| Bracelet FKM — embouts courbes | Couleur | 16 | **16** |
| Loupe d'horloger | Color | 13 | **13** |
| Étui de voyage rigide | Color | 9 | **9** |
| Loupe de date — minéral ou saphir | Matière & taille | 8 | **8** |
| Bracelet milanais — maille italienne | Band Color | 8 | **8** |
| Doigtiers d'horloger — latex | Color | 6 | **6** |
| Bracelet acier massif — 12 à 22 mm | Band Color | 6 | **6** |
| Coussins de présentation — lot de 10 | Color | 5 | **5** |
| Bracelet Présidentiel — acier inoxydable | Modèle | 4 | **4** |
| Barrettes de rechange — 270 pièces | Conditionnement | 4 | **4** |
| Remontoir Collection Bois beige / Bois noir | Capacité | 4 | **3 + 3** |
| Pince à barrettes · Coffret Douze aluminium · Bracelet Jubilé embouts courbes | Couleur / Capacité / Band Color | 3 | **3 chacune** |
| Rouleaux de Voyage (Bleu marine, Brun, Noir, Vert) · Remontoir Collection Cuir PU · Remontoir Solo · Outil de mise à taille | Capacité / Couleur | 2-3 | **2 chacune** |
| Remontoirs Bois (Acajou, Ébène, Noir laqué, Noyer) · Collection Bois LED noir / rouge | Capacité | 2 | **1 chacune** |

### P5 — Brouillons, à traiter seulement si Hakim les repasse en vente

**Aviateur Acier — Cadran à chiffres arabes** est la seule fiche du catalogue à **0 image**. Elle est en
brouillon. Les 8 autres brouillons (Contre-la-montre mère, Intégrale mère, Héritage mère, Noirmont Deux,
Voyageur, Remontoir Bois, Remontoir Collection, Rouleau de Voyage) ont des galeries de 5 à 25 images : ce sont
les fiches « mères » d'avant découpage, elles n'ont pas besoin de production.

---

## 5. Procédure d'intégration

1. **Produire sans écrire dans Shopify.** Livrer les fichiers + un manifeste `fiche → fichier → alt → position`.
2. **Contrôle qualité obligatoire avant intégration**, à l'image et pas au nom de fichier :
   - cadran par cadran : aucun logo, aucune marque, aucun sigle (règle 1) ;
   - conformité au produit livré : calibre, couleur, bracelet, fond de boîte (règle 2a) ;
   - aucune image ne doit être reconnaissable comme photo fournisseur brute (règle 2b) ;
   - aucun avis, note, étoile, badge, mention promo (règle 3) ;
   - 2048 × 2048 JPEG, poids dans la fourchette, alt renseigné (règle 4).
3. **Rattachement par lots, avec sauvegarde avant/après** de `product.media` (même méthode que les passes
   précédentes : `backup-…-<date>/inventaire.json`).
4. **Ne pas utiliser `productDeleteMedia`** : mutation dépréciée, et les MediaImage sont partagées entre fiches.
   Pour détacher, `fileUpdate` avec `referencesToRemove`.
5. **Attention aux SKU** : une autre passe travaille en parallèle sur les SKU des variantes. Ne rien écrire sur
   les variantes en dehors du champ image.

---

## 6. Questions ouvertes — arbitrage de Hakim

1. **Cible d'images par montre : 5 ou 6 ?** L'ancienne norme à 7 comptait deux visuels d'avis désormais
   interdits. Retenir 5 (face · situation · macro · poignet · détails) donne 74 visuels à produire ; passer à 6
   en ajoutant un angle légitime (fond de boîte, écrin, comparatif de taille) en donne 108. **Quelle cible ?**

2. **Les légendes techniques incrustées** (« Lunette cannelée · Acier poli ») sur les visuels `-3/-4/-5`
   existants : on les garde et on en produit de nouvelles, ou on applique le critère Merchant Center
   « no text overlays » à la lettre et on nettoie aussi celles-là ? Elles sont aujourd'hui hors périmètre.

3. **Les 202 visuels de variantes accessoires/bracelets** représentent 63 % du volume total pour des produits
   d'appoint (bracelets à 36 coloris, loupes, doigtiers). Faut-il les produire tous, ou **réduire le nombre de
   coloris proposés** pour ne garder que les plus vendables ? C'est probablement le meilleur levier
   d'économie du chantier.

4. **Carte cadeau Maison Noirmont** : une seule image. Faut-il vraiment une galerie de 3, ou une seule
   image suffit-elle pour ce produit ?

5. **Aviateur Acier — Cadran à chiffres arabes** (brouillon, 0 image) : on produit sa galerie, ou on
   supprime la fiche ? Elle a 6 variantes déjà créées.

6. **Budget.** La passe du 25/07 s'était arrêtée faute de crédits (~466 nécessaires pour ~375 disponibles) pour
   88 visuels. On en est à **319**. Il faut soit un budget, soit un ordre de priorité assumé — la proposition
   par défaut de ce brief est **P0 → P1 → P2 → P3 → P4**, ce qui met en ligne 60 visuels de galerie
   (les fiches montres actives d'abord) avant de s'attaquer au volume des coloris d'accessoires.

7. **Fiches mères en brouillon** : elles gardent des galeries de 5 à 25 images pour un produit qui n'est plus
   vendu sous cette forme. Faut-il les élaguer, ou les laisser comme réserve d'images ?

---

## 7. Annexes

- **`INVENTAIRE-VISUEL-2026-08-08.csv`** — les 105 fiches, ligne à ligne : id, titre, statut, famille, type,
  nombre d'images, nombre de variantes, variantes avec image, visuels de variantes distincts, option visuelle
  et nombre de valeurs, classement, verdict vs cible.
- `2026-08-08-retrait-visuels-faux-avis.md` + `boutique-seiko-mod/backups/backup-visuels-faux-avis-2026-08-08/` — ce qui a été retiré et
  pourquoi, avec copie locale des 18 fichiers interdits (à consulter pour savoir quoi **ne pas** refaire).
- `2026-08-08-audit-gmc-final.md` — points C1/C2/C3 (images) et D1/D2/D4 (avis restant dans le thème).
- `2026-07-25-bilan.md` — origine du chiffre de 88 visuels de variantes et leçons de la passe précédente.
- Docs de sourcing fournisseur : voir §2.2.

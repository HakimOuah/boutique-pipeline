# Métachamps montres et facettes de vitrine — Maison Noirmont

> **26/07/2026** — données de boutique (métachamps, étiquettes) + thème **brouillon `204248088914`**.
> Thème publié « Helio » non touché. Aucun SKU, prix, titre, option ni mapping DSers modifié.
> Suite de `2026-07-31-pages-collection-refonte.md`.

---

## 1. Volet 1 — les facettes : **bloqué, et pas par les données**

Search & Discovery est bien installée. Mais **je ne peux pas piloter son interface.**

### Le diagnostic, précis

L'application ne s'affiche pas dans la page d'administration : elle est servie dans une **iframe d'une autre origine**
(`search-and-discovery.shopifyapps.com`). Vérifié en direct :

```
{ host: "search-and-discovery.shopifyapps.com", sameOrigin: false, rect: [240,113,1664,911] }
```

Conséquences, toutes constatées et non supposées :

- l'**arbre d'accessibilité** s'arrête au bord de l'iframe — `find` et `read_page` ne voient aucun bouton de
  l'application ;
- les **clics synthétiques** de l'outillage navigateur ne franchissent pas une frame d'une autre origine. Mes
  coordonnées étaient pourtant justes : le bouton « Ajouter un filtre » est à (1497, 143) en coordonnées de page, soit
  exactement (1179, 113) à l'échelle de la capture, là où j'ai cliqué. La page n'a simplement pas bougé, trois essais
  de suite ;
- l'URL directe du formulaire (`/filters/new`) rend une page vide — le routage est interne à l'iframe ;
- le contrôle par le bureau (événements au niveau du système, qui eux franchiraient l'iframe) **est refusé sur les
  navigateurs** dans cet environnement.

### Ce que j'ai vérifié à défaut

- **Il n'existe pas de chemin API.** La configuration des facettes appartient à l'application ; l'API Admin ne
  l'expose pas.
- **Une définition de métachamp filtrable ne suffit pas.** J'ai créé les définitions avec accès vitrine public, puis
  rechargé `/collections/montres` : la vitrine ne propose toujours que « En stock / En rupture de stock » et
  « À partir de / jusqu'à ». Shopify ne remonte pas automatiquement un métachamp filtrable — **l'application doit
  ajouter la facette explicitement**.

### Les cinq gestes à faire dans l'interface

Search & Discovery → **Filtres** :

1. **Supprimer** le filtre « Disponibilité ».
2. **Ajouter un filtre** → source **Métachamp de produit** → `custom.famille` → libellé **Famille**.
3. Idem pour `custom.diametre` → libellé **Diamètre**.
4. Idem pour `custom.calibre` → libellé **Mouvement**.
5. Idem pour `custom.couleur_cadran` → libellé **Couleur de cadran**.

« Prix » est déjà en place et n'a rien à changer.

⚠️ **Ne pas adosser « Famille » aux étiquettes.** Une facette sur les étiquettes exposerait `bracelet` **et**
`bracelets`, `outils` **et** `outillage` — deux libellés pour la même chose, exactement le défaut relevé chez
montre-avenue. C'est pour cela que le métachamp existe.

---

## 2. Les définitions créées

Quatre définitions, toutes en **liste** de texte sur une ligne, toutes en accès vitrine `PUBLIC_READ`.

| Libellé | Clé | Type | Pourquoi une liste |
|---|---|---|---|
| Diamètre | `custom.diametre` | `list.single_line_text_field` | Une même référence existe en 36 **et** 39 mm — elle doit apparaître sous les deux valeurs du filtre |
| Mouvement | `custom.calibre` | `list.single_line_text_field` | Plusieurs calibres proposés sur une même fiche |
| Couleur de cadran | `custom.couleur_cadran` | `list.single_line_text_field` | Cohérence, et cadrans multiples possibles |
| Famille | `custom.famille` | `list.single_line_text_field` | Cohérence |

Le choix du **texte plutôt que du nombre** pour le diamètre est délibéré : une facette numérique se rend en plage
(« de 36 à 42 »), là où on veut des cases à cocher lisibles — « 36 mm », « 39 mm », « 41 mm », « 42 mm ».

---

## 3. Famille — renseignée, 91 produits

Déduite des étiquettes, qui sont exactement les règles des collections automatiques : aucune interprétation, aucun
risque d'erreur.

| Valeur canonique | Produits actifs |
|---|---:|
| Classiques | 15 |
| Sport chic | 14 |
| Chronos | 12 |
| Plongeuses | 6 |
| GMT | 6 |
| Remontoirs | 11 |
| Écrins et rouleaux | 9 |
| Bracelets | 10 |
| Outils d'horloger | 8 |
| **Total** | **91** |

Le 92e produit actif est la **carte cadeau**, volontairement laissée sans famille : ce n'en est pas une.

Vérifié après écriture : `metafieldsCount` = **91** sur la définition, accès vitrine `PUBLIC_READ`, et un contrôle par
sondage renvoie bien `["Classiques"]` sur une fiche Trente-Six.

Les libellés sont écrits en clair et en casse normale (« Sport chic », « Outils d'horloger »), pas en identifiants
techniques — c'est ce qui s'affichera dans le filtre.

---

## 4. Volet 2 — diamètre, calibre, couleur de cadran

### Résultat : 141 valeurs écrites sur les 53 montres

| Champ | Remplissage | Valeurs distinctes retenues |
|---|---:|---|
| **Mouvement** (`custom.calibre`) | **53/53** — 100 % | `Miyota 8215`, `NH35`, `NH34`, `Mingzhu 2813`, `PT5000`, `DG3804`, `VK63` |
| **Couleur de cadran** (`custom.couleur_cadran`) | **45/53** — 85 % | Noir, Blanc, Bleu, Vert, Gris, Brun, Champagne, Argent, Turquoise, Rose, Orange, Ivoire, Rouge, Or |
| **Diamètre** (`custom.diametre`) | **43/53** — 81 % | `36 mm`, `39 mm`, `40 mm`, `41 mm`, `42 mm` |

Compteurs relus sur les définitions après écriture : 53, 45, 43. Contrôle pilote sur `Trente-Neuf — Classique
cannelée` : les quatre champs se relisent correctement (`["36 mm","39 mm"]`, `["Miyota 8215","NH35"]`, `["Orange"]`,
`["Classiques"]`).

**Mon estimation de départ était trop pessimiste.** L'audit annonçait « le diamètre n'est présent que sur 15 montres
sur 53 » parce qu'il n'avait regardé que les valeurs d'options. En ouvrant les **descriptions produit** et les
**balises SEO**, on passe à 43. Le calibre, lui, passe de 10 à 53.

### Un défaut de fond découvert au passage — et corrigé

Les 12 chronographes ne sont **pas** automatiques : ils tournent avec un calibre **méca-quartz VK63**, c'est-à-dire
**avec une pile** pour l'heure, la fonction chronomètre restant mécanique.

Or la description de collection « Les Montres » que je venais d'écrire affirmait que **toutes** nos montres sont
automatiques et « sans pile ». C'était faux pour 12 fiches sur 53 — exactement le type de promesse invérifiable qu'on
s'interdit, et que personne n'aurait vu sans ouvrir les fiches une par une.

Trois descriptions corrigées :

- **Les Montres** — distingue désormais les automatiques des chronographes méca-quartz, et explique la différence.
- **Chronos** — assume le méca-quartz et en fait un argument (départ franc de l'aiguille, retour à zéro instantané),
  et mentionne le boîtier de 39 mm désormais établi.
- **Plongeuses** — ma formule « nous n'annonçons pas de profondeur d'immersion » **contredisait les fiches produit**,
  qui annoncent toutes « Étanchéité 10 bar ». Reformulée pour renvoyer à l'étanchéité indiquée sur chaque fiche, tout
  en maintenant que la plongée en bouteille reste déconseillée.

### Deux trous de palette, pas de données

L'extraction a buté sur 4 fiches dont le cadran est pourtant décrit sans ambiguïté, mais dont la couleur n'existait pas
dans ma palette fermée. Vérification faite sur le texte des fiches, la palette a été élargie :

| Fiche | Texte de la fiche | Valeur retenue |
|---|---|---|
| Trente-Six Rouge | « Le cadran rouge cramoisi est laqué et soleillé » | **Rouge** |
| Trente-Neuf Rouge | « Le cadran rouge cramoisi soleillé est profond » | **Rouge** |
| Trente-Six Or intégral | « cadran adoptent la même teinte or jaune » | **Or** |
| Trente-Neuf Duo Doré | « Le cadran reprend la même teinte dorée » | **Or** |

C'est la bonne façon de traiter le cas : la palette est un outil de normalisation, pas une camisole. La forcer aurait
produit un faux (un cadran rouge rangé en « Brun »).

### Les trous assumés

**10 fiches sans diamètre** — aucune mention de millimètre nulle part : ni option, ni description, ni balise SEO.
Métachamp laissé **vide**, conformément à la règle.

- les 3 **Noirmont** — Un (acier), Deux (céramique), Un Bronze ;
- les 7 **Intégrale** — Vert, Brun or rose, Turquoise, Noir, Bleu nuit, Bleu ciel, Blanc argenté.

**8 fiches sans couleur de cadran** — les 2 `Noirmont` (options `Boîtier: Acier` et `Référence 1 à 7`, muettes sur le
cadran), `Trente-Neuf Duo` (« bicolore » qualifie le boîtier et le bracelet, pas le cadran), et 5 `Voyageur` sur 6
(« Or », « Or rose », « Bicolore » désignent le boîtier ; les descriptions ne disent que « Cadran sans logo »).

> Le cas `Voyageur` mérite d'être noté : la fiche `Voyageur Bicolore cadran brun` glisse que son brun « se démarque des
> cadrans noirs habituels », ce qui **laisse supposer** un cadran noir chez ses voisines. C'est une déduction, pas une
> source. Elle n'a pas été retenue.

### Le piège du diamètre, rencontré et évité

Les six `Quarante-et-Un` contiennent la phrase « à mesurer avant de commander si vous portez d'habitude du **38 ou
39 mm** ». C'est une référence à l'habitude de poignet du client, **pas** au boîtier — lequel est donné ailleurs comme
« Boîtier acier de 41 mm ». Ces montres sont donc à `41 mm`, et non à 38 ou 39.

Aucune largeur de bracelet (entrecorne 18/20/22 mm) n'a été convertie en diamètre de boîtier.

### La règle appliquée

**Ne jamais deviner.** Le diamètre est la spécification la plus déterminante à l'achat d'une montre : une valeur
inventée se paie en retour client. Toute valeur non établie à partir d'une source explicite est **laissée vide** et la
fiche est signalée. Une facette incomplète est acceptable ; une facette fausse ne l'est pas.

Piège explicitement écarté : **ne jamais convertir une largeur de bracelet en diamètre de boîtier.** Les bracelets se
mesurent en 18/20/22 mm d'entrecorne, ce qui ressemble à un diamètre sans en être un.

### Sources, par ordre de fiabilité

1. **Valeurs d'options composées** — `Miyota 8215 · 39 mm · fond acier` porte le calibre *et* le diamètre. Ce sont nos
   propres données, c'est la source la plus sûre.
2. **Descriptions produit** — motifs explicites de diamètre et de calibre.
3. **Balises SEO** (`global.title_tag`) — une fiche au moins y porte « Chronographe 39 mm » alors que le titre produit
   ne le porte pas. Repéré par hasard sur un onglet ouvert, et exploité.
4. **Titres de fiches filles** — source directe et fiable pour la **couleur de cadran** (« Trente-Neuf Bleu »,
   « Contre-la-montre Champagne »).

### Normalisation retenue

- **Diamètre** : `"NN mm"`, avec une espace. Liste triée croissant, dédoublonnée.
- **Calibre** : six libellés canoniques et eux seuls — `NH35`, `NH34`, `Miyota 8215`, `Mingzhu 2813`, `PT5000`,
  `DG3804`. Deux orthographes du même calibre produiraient deux entrées dans le filtre.
- **Couleur de cadran** : **palette fermée** — Noir, Blanc, Bleu, Vert, Gris, Brun, Champagne, Argent, Turquoise,
  Rose, Orange, Ivoire, Bicolore. Les nuances sont ramenées à leur famille (`Bleu nuit`, `Bleu ciel`, `Bleu glacier`,
  `Bleu mer` → **Bleu**). Conventions des chronographes : `Panda` = cadran clair à compteurs sombres → **Blanc** ;
  `Panda inversé` → **Noir**.

---

### Couverture — à trancher par Hakim

Les trois facettes sont, à mon sens, **toutes activables** :

- **Mouvement 53/53** — aucune réserve.
- **Couleur de cadran 45/53** — 85 %, et les 8 manquantes sont concentrées sur deux gammes. Activable.
- **Diamètre 43/53** — 81 %. Activable, avec une réserve à connaître : **les 7 Intégrale et les 3 Noirmont
  n'apparaîtront sous aucune valeur de diamètre.** Un client qui coche « 41 mm » ne verra pas les Intégrale, qui sont
  pourtant une gamme entière de Sport chic. C'est le seul arbitrage réel du lot.

Deux façons de fermer le trou, dans l'ordre de coût : demander les cotes au fournisseur via DSers/AliExpress pour ces
10 références, ou les mesurer sur les visuels si une cote de référence est disponible. Tant que ce n'est pas fait, je
recommande d'activer quand même — un filtre qui couvre 81 % vaut mieux que pas de filtre, à condition d'être conscient
du trou.

---

## 5. Volet 3 — badges d'attributs : **non commencé, volontairement**

La consigne était explicite : « si et seulement si les deux premiers sont propres ». Le volet 1 ne l'est pas — les
facettes ne sont pas activées, et je ne peux pas les activer (§1). Je n'ai donc pas touché au template produit.

La donnée est en revanche prête, et le chantier est court : un bloc texte branché sur `custom.diametre`,
`custom.calibre` et `custom.couleur_cadran`, plus une dizaine de lignes de CSS dans un fichier dédié — le rendu
« pastille » relevé chez montre-avenue. À faire en une passe dès que le volet 1 est débloqué.

---

## 6. Ce que je n'ai pas pu contrôler

**Le mobile — toujours, et je ne fabrique pas de contrôle de repli.** Retenté une fois comme demandé :
`resize_window` renvoie un succès, mais la page rapporte obstinément `innerWidth: 1920`, et les media queries
`(max-width: 749px)` et `(max-width: 990px)` restent **fausses**. Il n'y a pas d'outil d'émulation d'appareil dans cet
outillage — seulement un redimensionnement de fenêtre qui n'atteint pas le viewport de rendu. Le lien de partage de
prévisualisation, qui aurait permis d'ouvrir la page dans un navigateur redimensionnable, est enfermé dans une iframe
d'une autre origine.

**Restent donc à valider sur un vrai téléphone** : le basculement des filtres en modale sous 990 px, et la hauteur de
la bannière une fois la description dépliée.

**Les facettes en vitrine** ne pourront être vérifiées qu'une fois les cinq gestes de l'interface faits (§1).

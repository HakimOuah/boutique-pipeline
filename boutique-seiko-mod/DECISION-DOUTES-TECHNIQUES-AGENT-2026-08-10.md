# Décision — cinq doutes techniques du §4.2

**Maison Noirmont — contrôle en lecture seule du 10/08/2026**

## Verdict exécutable

| Fiche Shopify | Produit AliExpress | Décision | Condition avant activation |
|---|---:|---|---|
| `cadran-squelette-nh70-3-coloris` (`11013068915026`) | `1005008395512841` | **Maintenir** | Garder une promesse lumineuse limitée aux points d'index ; nommer proprement les 7 teintes. |
| `cadran-squelette-29-noir-blanc` (`11013068816722`) | `1005009288581598` | **Rédaction prudente + remapping obligatoire** | Retirer la promesse lumineuse non prouvée et séparer clairement anneau seul, anneau + aiguilles et aiguilles seules. |
| `cadran-transparent-lume-28-5` (`11013068849490`) | `1005007524889100` | **Archiver la fiche actuelle** | Ne reconstruire qu'avec un vrai bundle de deux SKU testé de bout en bout ; sinon abandonner. |
| `support-mouvement-acrylique` (`11013057118546`) | `1005008727414152` | **Maintenir** | Dire explicitement « un support pour le calibre sélectionné », jamais « universel » ou « kit de 20 ». |
| `cadran-sterile-index-35` (`11013068620114`) | `1005010465015558` | **Archiver la fiche actuelle** | Éventuel sauvetage limité aux SKU A1–A4 ; les B1–B8 et C1–C2 doivent sortir de cette fiche. |

Soit **2 maintiens, 1 maintien sous rédaction prudente et 2 archivages recommandés**. Toutes les fiches étaient encore en statut Shopify `DRAFT` lors de la lecture. Aucun statut, texte, prix, média, variante ou mapping n'a été modifié.

## Méthode et portée de la preuve

- Shopify a été lu par le MCP connecté : statut, titre, description, variantes et totalité de la galerie de chaque fiche.
- AliExpress a été interrogé exclusivement par **AliExpress Open Platform / AE-Dropshipper via le VPS autorisé**, sans navigation AliExpress. Santé du gateway vérifiée à `2026-08-09T22:17:28Z`; variantes et qualifications exactes relues entre `22:20:34Z` et `22:21:16Z`.
- Toutes les variantes et toutes les images SKU retournées par l'API ont été inspectées. Les galeries Shopify correspondantes ont également été contrôlées : 13, 10, 17, 4 et 16 images respectivement.
- Une qualification `exact` prouve qu'un SKU distinct est sélectionnable, en stock et livrable en France à cet instant. Elle ne constitue ni une autorisation commerciale, ni une garantie durable de stock, de prix ou de fret.
- L'API ne fournit pas un champ textuel fiable « contenu du paquet ». Le contenu ci-dessous est donc déclaré **observé** seulement quand le libellé et l'image du SKU convergent. Sinon il reste **manquant**.

## 1. `cadran-squelette-nh70-3-coloris`

### Observé

- Shopify : produit `11013068915026`, `DRAFT`, 7 variantes et 13 images. La rédaction actuelle a déjà été ramenée à « sept teintes, index appliqués ».
- AliExpress : article `1005008395512841`, `onSelling`, 7 SKU, tous illustrés par un anneau seul. Libellés API : `blue`, `Violet`, `vert`, `gris`, `Bleu`, `BLANC`, `noir`. Les traductions brutes `blue`/`Bleu` et `Violet` ne suffisent pas à nommer les couleurs ; les images distinguent bien sept finitions.
- Les 13 images Shopify contiennent une **photo nocturne** absente des trois premières images examinées dans le rapport du 09/08. Elle montre la lueur verte des douze points d'index et de petits repères périphériques. Le doute « aucune photo de nuit » est donc levé.
- Les sept images SKU montrent le même type d'anneau avec points appliqués. Aucun jeu d'aiguilles, disque central, boîtier ou mouvement n'est montré comme inclus.

### Manquant

- Aucun texte API ne détaille le contenu physique du sachet au-delà de l'anneau montré.
- Couleur exacte du composé lumineux, intensité et durée de lueur non mesurées.
- Correspondance commerciale propre entre les libellés API mal traduits et les sept noms français à figer dans Shopify.

### Décision

**Maintenir.** La preuve nocturne permet une promesse étroite sur les points, sans devoir présenter tout l'anneau comme lumineux.

Recommandations exactes :

1. Conserver le titre prudent actuel, ou utiliser : **« Anneau de cadran squelette NH70/NH72 — points d'index luminescents, 7 teintes »**.
2. Formulation produit recommandée : **« Le visuel nocturne fournisseur montre la lueur des douze points d'index et des repères périphériques. Intensité et durée non mesurées. »**
3. Ne pas écrire « anneau entièrement luminescent », « Super-LumiNova » ni promettre une durée.
4. Renommer les sept options à partir des images validées, pas à partir des champs bruts `blue`/`Bleu`/`Violet`.

## 2. `cadran-squelette-29-noir-blanc`

### Observé

- Shopify : produit `11013068816722`, `DRAFT`, 5 variantes et 10 images. Le texte actuel annonce encore un anneau/des index luminescents.
- AliExpress `1005009288581598` expose cinq offres de contenu différent :

| Libellé API | SKU | Contenu montré par l'image SKU |
|---|---:|---|
| `black dial` | `12000048624200065` | anneau noir seul |
| `white dial` | `12000048624200067` | anneau blanc seul |
| `black dial hand` | `12000048624200066` | anneau noir + jeu d'aiguilles |
| `hand only` | `12000048624200069` | jeu d'aiguilles seul |
| `white dial hand` | `12000048624200068` | anneau blanc + jeu d'aiguilles |

- Les qualifications exactes ont confirmé que `black dial hand` et `hand only` sont bien deux SKU autonomes, en stock et livrables en France ; il ne s'agit pas d'une simple légende de galerie.
- Les 5 images SKU et les 10 images Shopify montrent les produits à la lumière du jour. **Aucune image nocturne n'établit la luminescence.** Le titre fournisseur contient « lumineux », mais ce verbatim seul ne satisfait pas la règle de preuve visuelle retenue pour le catalogue.

### Manquant

- Preuve nocturne indépendante pour l'anneau noir et l'anneau blanc.
- Dimensions, couleur lumineuse et compatibilité exacte du jeu d'aiguilles.
- Confirmation textuelle du sachet ; ici le contenu repose sur le libellé et l'image de chaque SKU.

### Décision

**Maintenir seulement sous rédaction prudente et remapping avant activation.** Le produit anneau est défendable ; la fiche actuelle ne l'est pas encore, car son sélecteur inclut aussi des aiguilles seules et des ensembles.

Recommandations exactes :

1. Retirer « luminescent », « lumineux » et toute promesse de lueur du titre, du corps, des puces et des métadonnées. Écrire **« index appliqués »** tant qu'aucune photo nocturne fiable n'est disponible.
2. Libellés client à imposer : **« Anneau noir seul »**, **« Anneau blanc seul »**, **« Anneau noir + aiguilles »**, **« Aiguilles seules »**, **« Anneau blanc + aiguilles »**.
3. Option préférable : sortir `hand only` de cette fiche cadran et la traiter comme un produit aiguilles séparé après contrôle des dimensions. À défaut, le titre doit annoncer « anneau ou aiguilles selon sélection », ce qui est moins clair commercialement.
4. Bloquer l'activation tant que les cinq contenus ne sont pas explicites dans le sélecteur et récapitulés juste au-dessus du bouton d'ajout au panier.

## 3. `cadran-transparent-lume-28-5`

### Observé

- Shopify : produit `11013068849490`, `DRAFT`, 11 variantes `NO.1` à `NO.11` et 17 images. Le texte actuel les présente comme onze variantes d'une même face transparente/ajourée.
- La galerie Shopify dit explicitement : **« IT NEEDS TO BE PURCHASED TOGETHER — TWO CAN MATCH TOGETHER — IT CAN'T BE MATCHED ALONE »** et illustre un disque translucide associé à un anneau périphérique.
- L'API confirme 11 SKU unitaires distincts et des niveaux de prix incompatibles avec un ensemble uniforme. Trois qualifications exactes suffisent à établir la séparation :

| Variante | SKU | Prix API observé | Contenu montré |
|---|---:|---:|---|
| `NO.3` | `12000041142495381` | 4,79 € | disque translucide bleu seul |
| `NO.9` | `12000041142495389` | 7,49 € | anneau noir à index seul |
| `NO.8` | `12000041142495386` | 3,39 € | anneau/cadre métallique lisse seul |

- Les 11 images SKU alternent disques colorés et anneaux. Aucune variante inspectée ne montre un paquet contenant les deux pièces. Les trois SKU ci-dessus étaient chacun en stock et livrables séparément vers la France au moment du contrôle.

### Manquant

- Table fournisseur disant quel disque est compatible avec quel anneau.
- Preuve qu'une commande client unique peut déclencher automatiquement deux SKU fournisseur dans DSers, avec quantité, prix et fret corrects.
- Dimensions et compatibilités techniques assez détaillées pour vendre les composants séparément sans ambiguïté.

### Décision

**Archiver la fiche actuelle.** Ce n'est pas un problème de formulation : le sélecteur vend des composants séparés alors que la fiche promet un cadran complet.

Recommandations exactes :

1. Ne jamais activer un SKU `NO.x` isolé sous le titre « cadran transparent ».
2. Ne reconstruire le produit que si un test DSers de bout en bout prouve qu'une variante client déclenche **les deux SKU requis** et si la paire exacte est documentée image par image.
3. Si ce bundle n'est pas techniquement fiable, abandonner la référence. La vendre comme deux produits séparés n'est acceptable qu'après obtention d'une table de compatibilité complète.

## 4. `support-mouvement-acrylique`

### Observé

- Shopify : produit `11013057118546`, `DRAFT`, 20 variantes et 4 images.
- L'API officielle expose bien 20 supports sélectionnables : `8200`, `9003`, `NH35`, `2460`, `899`, `7750`, `2000`, `2824 2892`, `2836`, `8500`, `1410`, `3301`, `3313`, `2235`, `3135`, `953`, `4130`, `2671`, `3235`, `4160`.
- Tous avaient un stock numérique positif à `22:21:16Z`. Les qualifications exactes ont confirmé :

| Variante | SKU | Stock observé | Prix observé | Fret standard France observé |
|---|---:|---:|---:|---:|
| `NH35` | `12000046416039953` | 34 | 7,29 € | 3,25 € |
| `2824 2892` | `12000046416039944` | 4 | 7,29 € | 3,25 € |
| `3235` | `12000046416039940` | 37 | 7,29 € | 3,25 € |

- La galerie montre un support acrylique réglable et identifie quatre exemples : E2000 (diamètre intérieur 19,0 mm), 7750 (29,5 mm), 2892/2824 (25,0 mm) et 2836 (25,0 mm). Une autre image porte le marquage `NH35`.
- L'option est une référence de calibre : tout indique **un support pour le calibre choisi**, pas un coffret contenant les 20 supports.

### Manquant

- L'API ne retourne aucune image propre à chacun des 20 SKU.
- Diamètre intérieur et plage de serrage des 16 références non légendées dans la galerie.
- Validation physique de compatibilité, notamment pour les familles proches ou les éventuelles variantes de calibre.

### Décision

**Maintenir.** Le doute principal NH35/2824/3235 est levé par les variantes officielles et les qualifications exactes. La fiche doit toutefois rester une fiche de choix par calibre, pas une promesse universelle.

Recommandations exactes :

1. Titre recommandé : **« Support de mouvement en acrylique — 20 références au choix »**.
2. Phrase obligatoire près du sélecteur : **« Contenu : 1 support correspondant au calibre sélectionné. Mouvement non inclus. »**
3. Afficher la liste intégrale des 20 références et demander au client de choisir son calibre exact.
4. Ne pas employer « universel », « compatible avec tous les mouvements » ou « kit de 20 ». Ne publier les diamètres que pour les quatre références effectivement légendées, sauf nouvelle preuve fournisseur.

## 5. `cadran-sterile-index-35`

### Observé

- Shopify : produit `11013068620114`, `DRAFT`, 14 variantes et 16 images. Son titre et son corps présentent les 14 choix comme des cadrans.
- L'API officielle révèle en réalité trois familles de produits :

| Famille | Variantes | Ce que montrent toutes les images SKU |
|---|---|---|
| Cadrans | `A1`, `A2`, `A3`, `A4` | quatre cadrans stériles à index |
| Aiguilles seules | `B1` à `B8` | huit jeux d'aiguilles de couleurs/formes différentes |
| Boîtiers | `C1 Mineral`, `C2 Sapphire` | deux boîtiers de montre, avec verre minéral ou saphir selon le libellé |

- Les qualifications exactes confirment qu'il s'agit de SKU commercialement distincts :

| Variante | SKU | Prix API observé | Objet montré |
|---|---:|---:|---|
| `A1` | `12000052501615130` | 14,69 € | cadran bleu |
| `B1` | `12000052783407087` | 5,59 € | jeu d'aiguilles |
| `C1 Mineral` (`Minéral C1` dans le champ localisé) | `12000052783407095` | 32,19 € | boîtier |

- Les trois étaient en stock et livrables séparément vers la France. Le champ commun `NO LOGO` ne transforme pas les aiguilles et boîtiers en cadrans ; il s'agit d'un attribut parasite commun à toute la fiche fournisseur.
- La galerie Shopify confirme visuellement le mélange : cadrans, nombreux jeux d'aiguilles et boîtiers apparaissent dans la même fiche.

### Manquant

- Compatibilité dimensionnelle des aiguilles B1–B8 : diamètres de tubes, longueur et mouvements exacts.
- Spécifications complètes des boîtiers C1/C2 : diamètre, entrecornes, couronne, fond, étanchéité et contenu livré.
- Certitude que le mapping DSers permet de supprimer proprement les dix SKU hors cadran sans réintroduction lors d'une synchronisation.

### Décision

**Archiver la fiche actuelle.** Son titre « cadran » est matériellement faux pour 10 variantes sur 14 ; une simple réécriture ne peut pas rendre ce sélecteur cohérent.

Recommandations exactes :

1. Sauvetage possible uniquement sous forme d'une fiche cadran reconstruite avec **A1–A4 exclusivement**, titre suggéré : **« Cadran stérile à index 35 mm — 4 teintes »**.
2. Ne pas importer B1–B8 comme produit aiguilles tant que leurs dimensions/compatibilités ne sont pas documentées.
3. Ne pas importer C1/C2 comme boîtiers tant que leurs caractéristiques techniques et le contenu livré ne sont pas documentés.
4. Si l'exclusion durable des dix SKU hors cadran ne peut pas être garantie dans DSers, abandonner complètement cette référence fournisseur.

## Conséquence pour le jalon d'activation

Ces décisions **ne valent pas activation**. Avant publication :

- les deux fiches à archiver doivent être retirées du lot activable ;
- `cadran-squelette-29-noir-blanc` reste bloquée jusqu'à correction des promesses et libellés de contenu ;
- les deux fiches maintenues restent soumises aux autres contrôles du catalogue, aux visuels finaux et à la validation commerciale globale.

**Actions effectuées : lecture Shopify, appels AliExpress officiels, inspection visuelle et rédaction de ce rapport uniquement. Aucun write Shopify/DSers, aucune commande, aucun achat, aucun commit ni push.**

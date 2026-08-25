# Cartographie de lustria.fr — et ce qu'il faut ajouter chez nous

**Lecture du 25/08/2026.** Étape 7 de `METHODE-ANALYSE-MARCHE.md` (cartographie de concurrent),
appliquée à `lustria.fr`, comparé à `lumierematiere.fr`.

---

## Entrée et méthode

| Source | Ce qu'elle a donné | Date de lecture |
|---|---|---|
| `lustria.fr/products.json?limit=250`, 24 pages jusqu'à épuisement | **5 928 fiches** : titre, handle, type, vendor, tags, prix, variantes, images, corps HTML | 25/08/2026 |
| `lustria.fr/collections.json?limit=250`, 3 pages | **556 collections** : handle, intitulé, nombre de produits | 25/08/2026 |
| Page d'accueil, 5 pages collection, 1 fiche produit, 7 pages CMS, rendues dans Chrome | thème, sections, menu complet, facettes, texte SEO, anatomie de fiche, mentions légales | 25/08/2026 |
| TrendTrack, fiche boutique `85c8ad0e-9666-4f21-bc04-fd7af16425c8` | date de création, thème, visites estimées, Trustpilot, 40 best-sellers, pixels, Meta Ads, Google Ads, pays | 25/08/2026 |
| **SEMrush, base France** — Vue d'ensemble + *Pages principales* (onglet déjà ouvert dans la session de Hakim) | Authority Score, trafic organique, mots-clés, backlinks, **trafic URL par URL sur 100 pages** | 24-25/08/2026 |
| `MOTS-CLES-TITRES-2026-08-25.md`, `CONVENTION-TITRES-2026-08-25.md`, `collections-seo.json`, `titles-live-2026-08-25.json` | nos volumes mesurés, notre convention de titre, nos 120 fiches, nos 14 collections | déjà au dossier |

**Dumps conservés à côté de ce rapport**, pour que chaque chiffre soit revérifiable sans refaire la
collecte : `lustria-catalogue-2026-08-25.json`, `lustria-collections-2026-08-25.json`,
`lustria-semrush-pages-2026-08-25.json`.

**Ce qui a résisté.** `products.json` et `collections.json` ont répondu en `curl` jusqu'à la 21ᵉ page,
puis Cloudflare a posé un *managed challenge* qui a aussi bloqué `robots.txt` et `sitemap.xml`. La fin
de la pagination a été faite en `fetch()` depuis l'onglet Chrome. **Le `sitemap.xml` n'a jamais été
lu** : la distinction entre collections au menu et collections orphelines a donc été établie par le
menu rendu et par le rapport *Pages principales*, pas par le sitemap.

**Rien n'a été écrit.** Aucune action Shopify, aucun achat, aucun formulaire, aucun compte, aucun
export payant TrendTrack. Les onglets ouverts ont été refermés et l'onglet SEMrush remis sur sa page
d'origine.

---

## Le verdict en dix lignes

1. **Lustria n'est pas le dropshipper qu'on croyait.** SEMrush France, 24/08 : **161 900 visites
   organiques/mois**, Authority Score **37**, **13 400 mots-clés** (+14 %), **991 pages indexées**.
2. **Ils ont compris la pièce avant nous, et c'est mesuré.** Sur leurs 100 premières pages (143 238
   visites, 89 % du total), les collections de **pièce pèsent 55 548 visites (38,8 %)** contre
   **19 700 pour les matières (13,8 %)**. La pièce vaut **2,8 fois** la matière chez eux.
3. **Leur modèle d'arborescence : une matrice `{7 types de luminaire} × {pièce, couleur, style,
   matière, technique}`**, 556 collections, et dans chaque menu déroulant **« Pièce » est le premier
   groupe**, avant la couleur, le style et la matière.
4. **Leur page n°1 est un produit que nous ne vendons pas.** `/collections/applique-murale` : 9 000
   visites/mois, position **3** sur `applique murale` (volume **49 500**). Les appliques pèsent
   **29 804 visites/mois, 20,8 % de leur trafic**. Nous en avons **zéro**.
5. **Deuxième trou : l'extérieur.** 6 200 + 996 = **7 196 visites/mois avec seulement 121 fiches**,
   soit 59 visites par fiche — le meilleur rendement de leur catalogue. Nous en avons zéro.
6. **Leur meilleure page de matière ne tient pas la comparaison avec leur pire page de pièce.**
   `suspension-bambou` : 51 fiches, 451 visites. `luminaire-cuisine` : 6 600 visites.
7. **La preuve la plus utile du dossier : `lustre-pampilles` a 0 produit, 3 424 mots de texte, et
   gagne 890 visites/mois sur 84 mots-clés.** Nous avons 7 fiches à mettre dedans et le mot vaut
   **6 340** (mesuré le 25/08). C'est un gain sans sourcing.
8. **Leurs titres produit sont pires que les nôtres** : `Suspension Luminaire | ROLIN`, médiane
   28 caractères, aucun mot descriptif. Le mot-clé est dans le **handle** et dans la **balise title**,
   jamais dans le titre. Notre refonte du 25/08 est meilleure sur cet axe.
9. **Leurs promesses ne tiennent pas** : « 4,7/5 sur plus de 3000 clients » affiché sur la fiche
   contre **Trustpilot 3,1 sur 88 avis**, « PLUS DE 6000 CLIENTS » sur l'accueil contre « 3000 » dans
   leurs annonces, et « LIVRAISON EN 4 À 7 JOURS » en hero contre « 10 à 35 jours ouvrés » écrit sur
   leur propre page *Notre Histoire* pour 74 % du catalogue.
10. **On ne les bat ni sur le volume, ni sur le prix, ni sur le délai, ni sur l'antériorité** —
    5 ans, 923 100 backlinks, 1 528 fiches expédiées d'Europe en 3-6 jours. On les bat sur la
    profondeur d'une famille, l'honnêteté du délai, les 30 jours de retour et la qualité du titre.

---

## 1. L'arborescence réelle de Lustria

### Le modèle, en une phrase

**Une matrice de sept types de luminaire croisée avec cinq axes d'attribut, la pièce en premier
position dans chaque menu, doublée de 18 facettes réelles alimentées par des métafields.**

### Le menu

Neuf entrées de premier niveau : `LUMINAIRE` · `LUSTRE` · `PLAFONNIER` · `SUSPENSION` ·
`APPLIQUE MURALE` · `LAMPADAIRE` · `LAMPE` · `LUMINAIRE EXTÉRIEUR` · `ESPACE B2B`.

Chaque entrée type ouvre un déroulé aux groupes **toujours dans le même ordre** :

| Rang | Groupe | Exemple, sous `LUSTRE` |
|---|---|---|
| **1** | **Pièce** | Bureau, Chambre, Chambre adulte, Chambre enfant, Couloir, Cuisine, Escalier, Salle à manger, Salle de bain, Salon, Toilette |
| 2 | Couleur | Argent, Beige, Blanc, Bleu, Doré, Gris, Marron, Multicolore, Noir, Orange, Rose, Rouge, Vert, Violet |
| 3 | Style | Ancien, Art déco, Design, Industriel, Moderne, Original, Scandinave, Vintage |
| 4 | Matière | Bambou, Bois, Céramique, Cristal, Laiton, Métal, Naturel, Osier, Paille, Papier, Pierre, Résine, Rotin, Verre, Tissu |
| 5 | Forme / technique / prix | Boule, Grand, Pampilles, Dimmable, Incandescent, IP20, IP65, LED, Lumière chaude, Lumière froide, Plume, Ventilateur, Pas cher |

**La réponse à la question de Hakim est donc : ils ont compris avant nous, et ils l'ont mis en
première position.** Nous rangeons uniquement par matière, sur les 13 collections publiées.

### Le décompte

| | Lustria | Lumière Matière |
|---|---:|---:|
| Collections publiées | **556** | 14 (13 familles + `selection-199`) |
| dont à 0 produit | 131 | 0 |
| Axes de découpe | 8 (pièce, couleur, matière, style, technique, forme/taille, prix, destinataire) | **1** (matière) |
| Collections « pièce » | **95** (73 non vides) | **0** |
| Collections « couleur » | 100 | 0 |
| Collections « matière » | 86 | 12 |
| Collections « style » | 57 | 2 |
| Collections « technique » | 55 | 0 |
| Facettes sur page collection | **18 axes** | 0 |
| Profondeur | 2 niveaux (`/collections/{type}-{attribut}`, pas de vraie hiérarchie d'URL) | 1 niveau |

Répartition des 556 collections par type de luminaire : luminaire 63 · plafonnier 67 (49 non vides) ·
suspension 66 (60) · lampadaire 63 (51) · lustre 62 (56) · lampe 61 (55) · applique murale 58 (58) ·
veilleuse 19 · spot 15 (**toutes vides**) · abat-jour 7 (**toutes vides**) · divers 69.

### Les 18 facettes

Relevées sur `/collections/applique-murale`, avec leurs compteurs :

Prix · Disponibilité (en stock 1 446 / rupture 155) · Type de produit · **Matériaux** (19 valeurs :
ABS 10, Acier 115, Acrylique 374, Aluminium 607, Bambou 8, Béton 14, Bois 133, Céramique 60,
Cristal 1, Laiton 11, Marbre 46, Métal 525, Osier 2, Naturel 12, Papier 1, Pierre 58, PVC 13,
Résine 48, Rotin 14, Silicone 1, Tissu 28, Verre 294) · Style (8) · **Pièce** (11 : Bureau 986,
Chambre 1 460, Couloir 815, Cuisine 526, Salle à manger 991, Salle de bain 177, Salon 1 338,
Escalier 194, Toilette 64, Enfant 261, Intérieurs 493) · Couleur (18) · Température de la lumière ·
Ampoule · Type de culot (B22, E12, E14, E17, E26, E27, G4, G9, GU10) · Dimmable · Protection IP
(IP20 1 324, IP65 191, IP54 2, IP44 22) · Voltage · Distance d'éclairage · Détecteur de mouvement ·
Nombre de lumières · Système solaire.

C'est un jeu de **métafields renseignés fiche par fiche**, pas des tags. C'est ce qui rend leurs
1 500 fiches d'appliques navigables — et c'est ce qui nous manque le plus après les collections de
pièce.

### Où va vraiment leur trafic, axe par axe

SEMrush *Pages principales*, base France, 24/08. Top 100 URL = **143 238 visites** sur 161 900
estimées (89 %).

| Axe de découpe | Visites/mois | Part | Pages | Visites par page |
|---|---:|---:|---:|---:|
| **Pièce** | **55 548** | **38,8 %** | 32 | 1 736 |
| Tête de type, mot nu | 29 336 | 20,5 % | 9 | **3 259** |
| Style / taille | 21 865 | 15,3 % | 18 | 1 215 |
| **Matière** | **19 700** | **13,8 %** | 16 | 1 231 |
| Nom de concurrent | 7 324 | 5,1 % | 6 | 1 221 |
| Couleur | 3 417 | 2,4 % | 7 | 488 |
| Technique (LED, IP, dimmable) | 2 665 | 1,9 % | 5 | 533 |
| Éditorial (blog) | 2 518 | 1,8 % | 5 | 504 |
| Prix (« pas cher ») | 865 | 0,6 % | 2 | 433 |

**Trois lectures, dans l'ordre d'importance pour nous.**

- **La pièce est l'axe qui porte le trafic**, à 2,8 fois la matière, sur deux fois plus de pages, et
  avec un rendement par page supérieur de 41 %. Nos volumes du 25/08 le disaient (`lustre chambre`
  10 810, `plafonnier salon` 8 970) ; le trafic réel d'un concurrent installé le confirme de façon
  indépendante.
- **Le mot nu reste le plus rentable par page** (3 259 visites/page). `applique murale` 9 000,
  `plafonnier` 5 800, `suspension` 4 200. Notre collection `Plafonniers` visait déjà juste ; c'est
  l'exécution qui manque, pas le choix du mot.
- **La couleur et la technique ne valent presque rien** : 100 collections de couleur pour 2,4 % du
  trafic. **À ne pas créer chez nous**, malgré leur visibilité dans le menu. C'est exactement le
  piège de l'étape 7 de la méthode (les collections les plus voyantes ne sont pas les plus
  rentables), et il se vérifie ici.

### Le détail des 40 premières pages

| # | URL | Visites | Meilleur mot-clé |
|---:|---|---:|---|
| 1 | `/collections/applique-murale` | **9 000** | applique murale |
| 2 | `/collections/luminaire-cuisine` | 6 600 | luminaire cuisine |
| 3 | `/collections/luminaire-exterieur` | 6 200 | luminaire exterieur |
| 4 | `/collections/plafonnier` | 5 800 | plafonnier led |
| 5 | `/collections/suspension-cuisine` | 5 100 | suspension cuisine |
| 6 | `/collections/luminaire-chambre` | 5 000 | chambre luminaire |
| 7 | `/collections/lustre-salon` | 4 600 | lustre salon |
| 8 | `/collections/applique-murale-moderne` | 4 400 | applique murale salon |
| 9 | `/collections/alternative-keria-luminaire` | 4 300 | keria luminaire |
| 10 | `/collections/suspension` | 4 200 | suspension luminaire |
| 11 | `/collections/lustre-cuisine` | 4 000 | lustre pour la cuisine |
| 12 | `/collections/luminaire-verre` | 3 500 | lustre verre |
| 13 | `/collections/suspension-salle-a-manger` | 3 300 | suspension salle à manger |
| 14 | `/collections/suspension-rotin` | 3 200 | suspension rotin |
| 15-16 | `suspension-design` · `lustre-bois` | 2 500 · 2 500 | lustre design · lustre bois flotté |
| 17-18 | `plafonnier-salle-de-bain` · `applique-murale-salle-de-bain` | 2 400 · 2 300 | |
| 19-20 | `suspension-moderne` · **l'accueil** | 2 200 · 2 200 | · lustria |
| 21-25 | `luminaire-chambre-adulte` 2 100 · `luminaire-couloir` 2 100 · `luminaire-salon` 2 000 · `luminaire-rotin` 1 900 · `applique-murale-originale` 1 900 | | |
| 26-30 | `plafonnier-moderne` 1 700 · `suspension-bois` 1 600 · `luminaire-salle-a-manger` 1 600 · `applique-murale-cuisine` 1 600 · `applique-murale-escalier` 1 400 | | |
| 31-35 | `suspension-verre` 1 300 · `applique-murale-chambre-adulte` 1 200 · **`suspension-xxl` 1 200** · `lustre-salle-a-manger` 1 200 · `applique-murale-design` 1 200 | | |
| 36-40 | `plafonnier-salle-a-manger` 1 100 · `luminaire-art-deco` 1 100 · `applique-murale-exterieur` 996 · **blog `tendance-luminaire-2026` 954** · `applique-murale-noire` 921 | | |

L'accueil ne fait que **2 200 visites, 1,35 %**. Tout leur trafic est sur des collections.

### Les collections mortes ou cassées — ce qu'on n'a pas à copier

- **131 collections à 0 produit publiées**, dont une soixantaine sont des **résidus d'un import de
  fournisseur polonais jamais nettoyé** : `extérieurs;plafonniers;murales;de salle de bain`,
  `1F systèmes de rails;spots ;Outlet`, `bandes LED;accessories`, `encastrés;Outlet;Outlet`,
  `abat-jour et accessoires;murales;suspensions`. Les titres contiennent le point-virgule du CSV
  d'origine. Deux marques fournisseur sont restées orphelines : `Maytoni`, `Hudson Valley Lighting
  Group`. C'est le signal de catalogue le plus net du dossier.
- **15 collections `spot*` et 7 collections `abat-jour*`, toutes vides.**
- **Des règles de collection intelligente cassées** : `lampadaire-chambre-adulte` annonce **4 812
  produits** alors que le catalogue ne compte que **126 lampadaires** ; `luminaire-gris` annonce
  3 538, exactement le total de `luminaire` ; `luminaire-cuivre` annonce 1 922 pour 18 fiches taguées
  cuivre. Les conditions de tag sont mal posées, et ces pages servent donc des produits hors sujet.
- **Six pages construites sur le nom d'un concurrent** : `alternative-alinea`,
  `alternative-keria-living`, `alternative-keria-luminaire`, `alternative-laurie-lumiere`,
  `alternative-light-online`, `meilleur-magasin-luminaire`. Elles affichent le catalogue entier
  (5 928 produits) et pèsent **7 324 visites/mois**, dont 4 300 sur la seule page Keria, en
  **position 1 sur `keria luminaire` (volume 8 100)**. Ça marche. Ça repose sur des marques déposées
  françaises, donc c'est **inécrivable en flux Merchant Center** (règle du net de marque, étape 4 de
  la méthode) et juridiquement exposé. **À ne pas reprendre.**

---

## 2. Le catalogue

### Volume et sourcing

| | Lustria | Lumière Matière |
|---|---:|---:|
| Fiches | **5 928** | 120 |
| Variantes | 24 133 (médiane 2, max 80) | — |
| Images par fiche | médiane 6 (min 1, max 28, aucune fiche sans image) | — |
| Longueur de description | **médiane 5 101 caractères** | médiane **329 caractères** |
| Fiches créées en février 2026 | 1 377 | — |
| Fiches publiées en février 2026 | 2 286 | — |

**Quatre `vendor`, et c'est la clé de leur modèle :**

| Vendor | Fiches | Prix médian | Ce que c'est |
|---|---:|---:|---|
| **Lustria** | 4 400 (74 %) | 210 € | sourcing international, délai annoncé 10-35 jours ouvrés |
| **Sollux Lighting** | 842 | 70 € | fabricant polonais, entrepôt UE, 3-6 jours |
| **BPSKoncept** | 406 | 175 € | fabricant polonais, entrepôt UE |
| **Thoro Lighting** | 280 | 310 € | fabricant polonais, entrepôt UE |

Les 1 528 fiches européennes (26 %) alimentent la collection `Livraison Sous 7 Jours` (handle
`luminaire-professionnel`, 1 133 produits) et le bloc « Luminaires en Livraison Rapide » de chaque
fiche produit. **C'est leur avantage structurel réel**, et il ne se copie pas sans compte fournisseur
B2B européen.

### Prix — nous sommes dans leur bande, pas en dessous

Prix affiché le plus bas de chaque fiche, en TTC, hors frais de port.

| | min | p25 | **médiane** | p75 | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| **Lustria (5 928 fiches)** | 11,90 | 89,90 | **169,90** | 299,90 | 479,90 | 5 729,90 |
| **Lumière Matière (120 fiches)** | 149 | 199 | **199** | 249 | 299 | 299 |

Répartition Lustria : 11 % sous 50 € · 25 % entre 50 et 120 € · 22 % entre 120 et 200 € ·
17,5 % entre 200 et 300 € · 15,4 % entre 300 et 500 € · 8,5 % au-dessus de 500 €.

**Trois conséquences pour l'étape 9 de la méthode (« juste en dessous du comparable »).**

1. Notre médiane de 199 € est **17 % au-dessus de la leur**. Ils sont le comparable direct : même
   nature d'acteur, pas de récit de fabrication, même bande de produits.
2. Notre catalogue est enfermé dans **150 € de large** (149-299) quand leur cœur de marché est
   50-300 €. **Il n'y a rien chez nous sous 149 €**, or 36 % de leurs fiches y sont, et 8 de leurs 40
   best-sellers TrendTrack sont sous 100 $.
3. Nous n'avons rien au-dessus de 299 € non plus, alors que leur famille lampadaire a une médiane à
   **499,90 €** (p75 749,90). Deux extrémités absentes.

### Famille par famille

**Nos 12 familles matière chez eux** — profondeur et prix médian :

| Famille | Nos fiches | Fiches Lustria (tag) | Prix médian Lustria | Leur trafic sur la page |
|---|---:|---:|---:|---:|
| Suspensions bambou | 16 | 36 | 220 € | 451 |
| Suspensions rotin | 14 | 56 | 265 € | **3 200** |
| Suspensions bois | 12 | 113 | 250 € | 1 600 |
| Suspensions verre | 10 | 225 | 300 € | 1 300 |
| Suspensions pierre | 9 | 33 | 240 € | non classée |
| Suspensions métal | 8 | 425 | 350 € | 486 |
| Suspensions céramique / déco | 8 | 11 | 150 € | non classée |
| Lustres anneau | 12 | pas de famille dédiée | — | — |
| Lustres salon | 12 | 3 158 (collection) | — | **4 600** |
| Lustres effet cristal | 7 | 78 fiches « cristal » | — | 378 |
| Lustres statement | 1 | — | — | — |
| Plafonniers | 10 | 1 134 | 140 € | **5 800** |
| Suspensions modernes | 1 | 1 275 (collection) | — | 2 500 |

**Deux familles où nous sommes déjà mieux dotés qu'eux ne le sont en proportion** : la céramique
(8 fiches contre 11 chez eux, sur un catalogue 49 fois plus grand) et la pierre / travertin
(9 fiches contre 33). Ce sont les deux seuls endroits du catalogue où notre profondeur relative est
défendable. À noter : leur collection `suspension-pierre` n'apparaît pas dans leurs 100 premières
pages, et `suspension pierre` ne vaut que **170** chez nous. La famille est faible des deux côtés —
c'est une surdotation, pas un avantage.

### Les types de luminaire qu'ils ont et que nous n'avons pas

| Type | Fiches | min | médiane | p75 | max | Leur trafic mensuel | Visites par fiche |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Applique murale** | **1 522** | 14,76 | **129,90** | 229,90 | 1 169,90 | **29 804** | 19,6 |
| Lampe de chevet / à poser | 319 | 19,90 | 99,90 | 179,90 | 1 524,90 | 1 137 | 3,6 |
| Veilleuse | 263 | **11,90** | 24,90 | 34,90 | 184,90 | non classée | — |
| **Lampadaire** | 126 | 69,90 | **499,90** | 749,90 | 1 394,90 | 2 168 | 17,2 |
| **Luminaire extérieur** | **121** | 19,90 | 119,90 | 199,90 | 589,90 | **7 196** | **59,5** |
| Lampe de table | 10 | 54,90 | 217,40 | 309,90 | 634,90 | — | — |
| Projecteur galaxie / ciel étoilé | 4 | 59,90 | 64,90 | 79,90 | 79,90 | — | — |

**Le classement des trous sort de la dernière colonne, pas de la première.** L'extérieur rend
59,5 visites par fiche, l'applique 19,6, le lampadaire 17,2, la lampe de chevet 3,6. La veilleuse ne
classe aucune page dans leur top 100 malgré 263 fiches : c'est du volume de catalogue, pas de la
demande.

**Les appliques, en sous-familles de pièce** (tags, prix médian) : Chambre 667 fiches / 129,90 €
· Salon 630 / 139,90 € · Salle à manger 498 / 149,90 € · Bureau 354 / 129,90 € · Cuisine 294 /
129,90 € · Tête de lit 284 / 109,90 € · Couloir 261 / 129,90 € · Escalier 137 / 119,90 € · Salle de
bain 134 / 119,90 € · Enfant 68 · Bébé 21.

Et les pages qui portent : `applique-murale` 9 000 · `applique-murale-moderne` 4 400 ·
`applique-murale-salle-de-bain` 2 300 · `applique-murale-originale` 1 900 · `applique-murale-cuisine`
1 600 · `applique-murale-escalier` 1 400 · `applique-murale-chambre-adulte` 1 200 ·
`applique-murale-design` 1 200 · `applique-murale-exterieur` 996 · `applique-murale-noire` 921 ·
`applique-murale-rotin` 735 · `applique-murale-verre` 727.

**L'extérieur, en détail** : 121 fiches, tags dominants Éclairage extérieur 43, Terrasse 17, Mural
15, LED 15. Les handles montrent la variété du rayon : `borne-luminaire-exterieur`,
`spot-exterieur-pour-escalier-de-forme-carre-ou-rond`, `luminaire-exterieur-ip67`,
`petite-applique-murale-exterieure-led`, `applique-murale-exterieure-led-ronde`,
`eclairage-exterieur-pas-cher` (19,90 €). Une seule URL, `/collections/luminaire-exterieur`, classe
sur **442 mots-clés**.

### Ce qu'ils n'ont pas — et pourquoi on n'y va pas

Fiches contenant le mot, dans le titre, le handle ou les tags : pampille **9** · ventilateur
lumineux **3** · guirlande **2** · ruban LED **7** · borne **1** · nacre **2** · albâtre **6** ·
jonc de mer **0** · suspension papier **0 fiche taguée** pour 28 dans la collection.

Ces trous sont réels, mais **aucun n'est adossé à un trafic mesuré chez eux** : leurs collections
`spots` (15), `bandes-led`, `lustre-ventilateur`, `abat-jour` sont **toutes à 0 produit et aucune ne
classe**. Selon la règle de l'étape 7 (« une collection morte chez lui est une collection à ne pas
créer chez nous »), on n'y va pas — **sauf pour les pampilles**, où leur collection est vide mais
gagne 890 visites/mois, ce qui inverse le verdict.

---

## 3. Les best-sellers

### Ce que la page d'accueil met en avant

Section « Nos Meilleures Ventes », dans l'ordre affiché le 25/08 : `Applique Murale | OISEAU` 59,90 €
· `Applique Murale | STAR` 59,90 € · `Applique Murale | BOU` dès 59,90 € · `Suspension Luminaire |
ROLIN` dès 139,90 € · `Luminaire Extérieur | SUN` dès 89,90 € · `Luminaire Plafonnier | DIVIRO`
99,90 € · `Applique Murale | PAPILLE` 99,90 € · `Applique Murale | NOLIMA` 59,90 € · `Suspension
Luminaire | GANIC` dès 69,90 € · `Luminaire Extérieur | NIUM` dès 69,90 €.

**Cinq appliques sur dix, deux extérieurs sur dix, en tête de leur page d'accueil.** Bande de prix
59,90 à 139,90 €, très en dessous de notre plancher.

### Ce que TrendTrack classe

Top 40 « Meilleures ventes », lu le 25/08. Les titres sont tronqués dans l'interface ; les produits
ont été identifiés par le nom de fichier de leur image.

| Rang | Produit (d'après le fichier image) | Prix affiché TrendTrack | Créé |
|---:|---|---:|---|
| 1 | `applique-murale-bird-moderne` | 63,72 $ | 20/08/2021 |
| 2 | `applique-murale-design-star-dore` | 53,09 $ | 10/06/2021 |
| 3 | `lampe-lave` (Lampe de chevet LAVE) | 63,72 $ | 18/09/2021 |
| 4 | `lampe-projecteur-sunset` | 63,72 $ | 24/08/2021 |
| 5 | `luminaireplafonnierdesignitalien` | 319,04 $ | 20/06/2021 |
| 6 | `luminaire-exterieur-cour-jardin-balcon-villa-luxe` | 212,66 $ | 10/06/2021 |
| 7 | `suspension-verre-fume` | 106,28 $ | 16/12/2021 |
| 8 | `applique-murale-doree` | 106,28 $ | 04/10/2021 |
| 9 | `applique-murale-design-noir-ester` | 85,00 $ | 10/06/2021 |
| 10 | `suspension-luminaire-design-moderne-originale-epuree` | 265,85 $ | 10/06/2021 |
| 19 | `suspension-rotin-pas-cher` | 148,83 $ | 04/10/2021 |
| 26 | `plafonnier-rotin` | 159,47 $ | 04/10/2021 |
| 31 | `Projecteur Ciel Étoilé` | 63,72 $ | 08/09/2021 |

**Deux faits, et le second compte plus que le premier.**

1. **Les appliques murales occupent 11 des 30 premières places**, les lampes de chevet 3, les
   extérieurs 3. Les suspensions, notre seul rayon, n'occupent que 8 places.
2. **Les 40 best-sellers ont tous été créés entre juin 2021 et décembre 2022.** Aucun produit des
   3 500 fiches ajoutées depuis 2025 n'entre dans le classement. Ce sont **les fiches anciennes,
   celles qui ont accumulé du signal et des liens, qui vendent** — pas le catalogue de masse. C'est
   la lecture la plus encourageante du dossier : leur avantage tient sur une centaine de fiches, pas
   sur 5 928.

### Le tri et les badges

Dix options de tri sur chaque collection, dont **« Meilleures ventes »** et **« Le plus pertinent »**.
Un badge **« Best-seller »** au-dessus du H1 sur la fiche produit, un badge « Rupture de Stock » sur
les vignettes. La homepage sert dix vignettes par famille, avec « Vue Rapide » sur chacune.

---

## 4. Les titres produit — nous sommes meilleurs, et c'est mesurable

### Leur anatomie

**`{Type générique} | {NOM DE CODE INVENTÉ}`**, avec un pipe et zéro mot descriptif.

```
Suspension Luminaire | ROLIN
Luminaire Plafonnier | TOPS
Applique Murale | YTAL
Lampe de Chevet | MAGNA
Lampadaire | DRUTIS
Veilleuse | FROGGY
Luminaire Plafonnier | AURA 1 (Outremer)      ← seules les fiches fournisseur portent la couleur
Applique Murale | LAHTI 70 LED 4000K (Rouge Ocre)
```

| Mesure | Lustria (5 928 titres) | Lumière Matière (120 titres) | Notre convention du 25/08 |
|---|---:|---:|---|
| Longueur médiane | **28 caractères** | 36 | 40 à 60, plafond dur 65 |
| Mots médians | **4** | — | — |
| Titres ≤ 40 caractères | 5 266 (89 %) | — | — |
| Titres > 70 caractères | 19 (0,3 %) | 2 | interdits |
| Type de produit en premier mot | **100 %** | 100 % | règle n°1 |
| Contient la matière | **0 %** | ~85 % | cible ≥ 70 % |
| Contient un mot de pièce | **0 %** | 12/120 (10 %) | à faire monter |
| Contient une couleur | ~5 % (fiches fournisseur) | ~40 % | liste finie |
| Contient un pipe `\|` | **100 %** | 0 % | interdit (règle n°5) |
| Contient la marque | 0 % | 0 % | interdit (règle n°3) |

Premier mot, sur les 5 928 : `Suspension` 2 386 · `Applique` 1 540 · `Luminaire` 1 249 · `Lampe` 347
· `Veilleuse` 262 · `Lampadaire` 126 · `Plafonnier` **11**.

**Anomalie utile : ils écrivent `Luminaire Plafonnier`, pas `Plafonnier`.** Le mot cherché est
`plafonnier` (`plafonnier led` = 21 090 consolidé chez nous). Ils ont mis un mot vide devant le mot
qui vaut, sur 1 134 fiches.

### Où est passé leur mot-clé

Le mot-clé n'est pas dans le titre : il est dans le **handle** et dans la **balise title SEO**.
Relevé sur une fiche, le 25/08 :

| Champ | Contenu |
|---|---|
| Handle (URL) | `suspension-rotin-pas-cher` |
| Balise `<title>` | `Suspension Rotin Pas Cher Design Torsadé Brun – Lustria` |
| `<meta description>` | `Suspension Rotin Pas Cher. Transformez votre décoration avec cette suspension brun en rotin, alliant élégance et originalité grâce à sa forme torsadée en bambou.` |
| **H1 visible** | **`Suspension Luminaire \| ROLIN`** |
| Titre produit Shopify (donc flux) | `Suspension Luminaire \| ROLIN` |

Autres handles relevés, tous écrits pour la requête : `plafonnier-original-salon`,
`suspension-de-style-cage-a-oiseaux-pour-interieur-chic`, `applique-murale-exterieure-led-ronde`,
`borne-luminaire-exterieur`, `petite-applique-murale-exterieure-led`,
`spot-exterieur-pour-escalier-de-forme-carre-ou-rond`, `eclairage-exterieur-pas-cher`.

Les nôtres, en comparaison : `suspension-verre-led-489156`, `lustre-anneau-led-led-597704`. **Un
identifiant numérique là où ils mettent une requête.**

### Le verdict

**Sur le titre produit, nous faisons mieux qu'eux, et l'écart est net.** Notre convention pose le
type en premier, la matière obligatoire, 40-60 caractères, pas de pipe, pas de marque, et la V2 du
25/08 déplace 71 titres depuis des mots morts vers des mots de pièce (`lustre anneaux led` 20 →
`lustre salon` 22 200). Le leur ne porte **aucun** mot-clé descriptif : en Google Shopping, où le
titre du flux est le champ décisif, `Suspension Luminaire | ROLIN` ne matche rien.

**Deux réserves à écrire.**

1. **Leurs annonces Meta portent des titres tout autres** : « Suspension Luminaire Salon Design
   Tubes Croisés, S » et « Suspension Luminaire LED En Acrylique Doré Élégant, Blanc » (TrendTrack,
   25/08). Ils réécrivent donc leurs titres **au niveau du flux**. **Je n'ai pas pu établir ce que
   contient leur flux Merchant Center**, et le doute doit rester : notre avantage est certain sur le
   H1 et l'organique, probable mais non prouvé sur Shopping.
2. **Sur le handle et la balise title, ils font mieux que nous**, et c'est corrigible sans toucher au
   produit.

**Coquilles relevées au passage** (5 928 titres) : `Applque Murale`, `Lampadaire|`,
`Veilleuse |JOLINA`, doubles espaces sur `Lampadaire  | YUMI` et `Luminaire Extérieur  | NUMY`,
`Tour sur sur les lustres pampilles` en H2 de collection, `Notre portons une grande attention` sur
l'accueil, `stockTout savoir sur les appliques murales` (concaténation cassée).

---

## 5. Le copy

### Anatomie d'une fiche produit

Relevé bloc par bloc sur `/products/suspension-rotin-pas-cher`, le 25/08.

| # | Bloc | Contenu |
|---:|---|---|
| 1 | Badge | « Best-seller » |
| 2 | Fil d'Ariane | `Lustria / Suspension Luminaire /` + nom |
| 3 | H1 | `Suspension Luminaire \| ROLIN` |
| 4 | Prix | « Prix régulier 139,90 € » — **aucun prix barré, aucun compte à rebours** |
| 5 | **Preuve sociale** | « **4.7/5 sur plus de 3000 clients** » en texte libre, **sans widget, sans lien, sans avis individuel** |
| 6 | Accroche | **une seule phrase**, qui contient le mot-clé : « La suspension rotin pas cher apporte une touche naturelle et chaleureuse à votre intérieur… » |
| 7 | Réassurance en ligne | Paiement en 3× avec Klarna · Livraison offerte · **Retours sous 14 jours** · Installation facile |
| 8 | Variantes | axe unique « Taille » S/M/L |
| 9 | Bouton | **« AJOUTER AU PANIER - 139,90€ »**, le prix dans le bouton |
| 10 | Stock | « Article actuellement en stock » |
| 11 | **Fiche technique** | tableau de **16 lignes** : Culot (G9), Ampoule incluse (Non), Type d'ampoule (LED), Couleur, Luminosité ajustable, Température de la lumière (Blanc chaud 3000K), **Distance d'éclairage (3 à 10 mètres)**, Matériaux, Nombre de lumières, Alimentation (AC), Protection (IP20), Style, Voltage (90-260V), Puissance (24W), **Dimensions détaillées par taille S/M/L avec longueur de câble réglable**, Dimensions support |
| 12 | Accordéons | DÉTAILS SUR LA LIVRAISON · DESCRIPTION · CONDITIONS DE RETOUR · CONTACTEZ-NOUS |
| 13 | Bloc B2B | « Vous êtes un Professionnel ? … NOUS CONTACTER » |
| 14 | Recommandations | « Nos Clients Les Adorent », 5 produits |
| 15 | Collection mise en avant | « Luminaires en Livraison Rapide » — les fiches fournisseur européen |
| 16 | Historique | « Vu récemment » |
| 17 | Réassurance finale | PLUS DE 6000 CLIENTS · PAIEMENT FLEXIBLE · LIVRAISON OFFERTE · SAV DU LUNDI AU VENDREDI |

Longueur de description : **médiane 5 101 caractères** sur les 5 928 fiches (max 254 999, une seule
fiche vide). **La nôtre est à 329 caractères de médiane, soit 15 fois moins.**

**Pas d'avis produit.** 1 076 fiches portent le tag `No Review`. Aucun widget Judge.me, Loox, Yotpo
ou Okendo dans les scripts chargés. La note 4,7/5 est une affirmation de gabarit, pas un compteur.

**Ton.** Descriptif, court, factuel, avec le mot-clé placé en tête de la première phrase. Pas
d'emphase commerciale, pas d'urgence artificielle, pas de tutoiement. C'est un ton reprenable.

### Copy des pages collection — oui, et beaucoup

**Correction d'une première lecture.** `collections.json` renvoie `body_html` vide sur **les 556
collections**. J'en avais conclu qu'elles n'avaient pas de texte. C'est faux : le texte est dans une
**section de thème**, pas dans le champ Shopify. Rendu en HTML, chaque page collection porte
**1 400 à 1 900 mots**.

| Collection | Texte SEO | Structure |
|---|---:|---|
| `applique-murale` | ~1 900 mots | 11 H2/H3 : Qu'est-ce qu'une applique murale · avantages · les différents types · les styles · critères de choix · inspiration · installation · entretien · meilleures ventes 2026 · **FAQ** · « Passez par un expert de l'éclairage » |
| `suspension-rotin` | **1 434 mots** | Tout savoir · déco rotin · paille et osier · sélection · conseils d'achat · critères de qualité · où trouver · comment installer · intégration par espace |
| `lustre-pampilles` | 3 424 caractères, **pour 0 produit** | Qu'est-ce qu'un lustre pampilles · comment choisir · où installer · entretien et nettoyage · astuces |
| `alternative-keria-luminaire` | 3 429 caractères | L'ADN Keria · la gamme Keria · l'innovation Keria · les inspirations déco Keria · le réseau Keria en France |

Chaque page a un **H1 propre**, une **balise title** et une **meta description** écrites pour la
requête :

- `Applique Murale : Appliques Pour Intérieur Et Extérieur | Lustria`
- `Luminaire Cuisine : Éclairage Idéal Pour Ilot Central | Lustria`
- `Suspension Rotin : Lustre En Rotin Au Format XXL | Lustria`
- `Lustre Pampilles : Éclairage Ancien Ou Moderne – Lustria`
- `Keria Luminaire A Disparu ? Découvrez La Meilleure Alternative – Lustria`

**Et voici la qualité réelle de ce texte, qui est leur plus grosse brèche éditoriale.** Extrait
relevé sur `suspension-rotin` : le corps de texte cite nommément **IKEA, Alinea et « Le Palais du
Rotin » comme endroits où acheter une suspension en rotin**, sur leur propre page de vente. Les
sous-titres sont des requêtes longue traîne recopiées telles quelles, ponctuation d'origine
comprise : « Suspension naturelle bambou jacinthe - luminaires | alinea », « Suspension rotin • le
palais du rotin », « Suspension en rotin - oce déclinaisons suspensions rotin 30 cm ». C'est du
texte généré, non relu, qui envoie le visiteur chez le concurrent et qui emploie des marques tierces
dans le corps.

### Le reste du discours

**Accueil**, dans l'ordre des sections : header · bandeau à 3 messages rotatifs (LIVRAISON OFFERTE /
RÉGLEZ EN PLUSIEURS FOIS avec Klarna / PLUS DE 6000 CLIENTS) · hero « ILLUMINEZ VOTRE INTÉRIEUR AVEC
— Votre Expert Luminaire En Ligne » + « LIVRAISON EN 4 À 7 JOURS » + encart professionnel · **Nos
Meilleures Ventes** · « Notre Ambition » · **Les Suspensions** · « Quel Est Notre But ? » ·
**Éclairage Extérieur** · « Nos Fournisseurs » · **Les Appliques Murales** · « Vous Avez Une
Question ? » · **Les Plafonniers** · « Suivi De Commande » · **Les Lampadaires** · « NOUVEAU —
Demande de Devis » · **Les Lampes** · **FAQ de 35 questions** · **6 derniers articles de blog** ·
footer. Le corps de texte de la page ne fait que 9 267 caractères : l'accueil est **une alternance
grille produit / bloc éditorial court**, six fois de suite.

**Pages CMS.** `a-propos` (« Notre Histoire ») est le morceau le plus soigné du site : récit sans
fondateur nommé, sans date, sans atelier, construit sur **le métier de sélection** (« Nous ne
dessinons pas nos luminaires : nous les choisissons »), avec l'aveu explicite du sourcing asiatique
et des délais. La page FAQ porte un **JSON-LD `FAQPage`** et répond franchement à « Avez-vous un
magasin physique ? » (non), « Qui s'occupe du design ? » (les fabricants), « Quelle est l'origine
des articles ? » (Europe + Asie). `conditions-de-retour` : **14 jours**, frais de retour à la charge
du client, étiquette prépayée « dans certains cas », garantie légale de conformité 2 ans citée
correctement. Les quatre pages juridiques (CGV, remboursement, confidentialité, expédition) sont un
gabarit générique daté du 13/03/2024.

**Blog actif** : 6 articles publiés entre le 12 et le 25/08/2026, tous en question pratique
(« Comment installer un éclairage dans une salle de bain ? », « Combien de lumens pour un éclairage
solaire ? »). Cinq articles entrent dans leur top 100 de trafic pour **2 518 visites/mois**, dont
`tendance-luminaire-2026` à **954 visites sur 349 mots-clés**.

**Espace B2B** : entrée de menu, page `luminaire-professionnel` (« Devis personnalisé en 48h ») avec
formulaire protégé par hCaptcha, bloc sur chaque fiche produit, bloc sur l'accueil, entrée en pied de
page. Zéro stock, zéro coût.

---

## 6. La construction du site

| Élément | Relevé |
|---|---|
| Plateforme | Shopify, boutique `lustre-et-luminaire.myshopify.com` |
| **Thème** | **Impulse 7.3.4**, renommé `Lustria V19 - payment icons + menu size` |
| Marché | FR, français, EUR ; sélecteur de devise vers ~200 pays en pied de page |
| Menu | 9 entrées, mégamenu à 5 groupes par type, **Pièce en premier** |
| Pied de page | 4 colonnes : Menu principal (9 liens) · Informations légales (8) · Service client (horaires 8h-17h, `info@lustria.fr`) · Newsletter. Instagram, Facebook, Pinterest. |
| Bandeau | 3 messages rotatifs |
| Panier | `/cart` classique, pas de tiroir latéral détecté |
| Paiement | Klarna (3×) mis en avant en bandeau, en fiche et en réassurance ; le thème est explicitement nommé « payment icons » |
| Pop-up | formulaire d'inscription Klaviyo chargé ; **aucun pop-up ne s'est déclenché** pendant la visite |
| Réassurance | 4 blocs sur chaque fiche : PLUS DE 6000 CLIENTS · PAIEMENT FLEXIBLE · LIVRAISON OFFERTE · SAV DU LUNDI AU VENDREDI |
| Suivi de commande | app dédiée sur `/apps/trackingmore`, plus une section sur l'accueil |
| Sitemap | **app tierce** sur `/apps/seo-sitemaps/sitemap`, pas le sitemap Shopify natif |

**Applications et scripts détectés** (sources JS chargées sur l'accueil et la fiche produit) :

| Outil | Usage |
|---|---|
| Klaviyo (`company_id=WT6fin`) | e-mail, formulaires d'inscription, tracking on-site |
| Gorgias (`lustre-et-luminaire.myshopify.com`) | chat et formulaires de contact |
| Yotpo SMSBump | SMS |
| TrackingMore | suivi de commande |
| App SEO sitemaps | sitemap |
| BestPush / restock SDK | alerte de réapprovisionnement |
| GA4 `G-5NCGLVWBEL` · GTM `GT-MQBKM5H` · **Google Ads `AW-341625901`** | mesure et conversions |
| Meta Pixel · Snap Pixel | régies sociales |
| Microsoft Clarity `sfu2j30tgf` | enregistrement de session |

TrendTrack confirme les pixels (Google Analytics, GTM, Meta Pixel, Snap Pixel, Google Ads) mais
**n'affiche aucune liste d'applications Shopify** : la section « Apps Shopify » de sa fiche est vide.

**L'entreprise derrière**, d'après les mentions légales lues le 25/08 : **Stanfield, SASU**, capital
1 000 €, **RCS Paris 985143783**, immatriculée le **01/03/2024**, siège 229 rue Saint-Honoré 75001
Paris, TVA FR53985143783, directeur de la publication « Mr Lextrait ». **La boutique Shopify est
antérieure de trois ans** (créée en juin 2021 selon TrendTrack, premières fiches datées du
03/06/2021). L'annonceur Google Ads s'appelle **STANFIELD**. Le registre du commerce n'a pas été
consulté : le rapprochement entre les deux dates est un constat, pas une conclusion sur la structure.

### Acquisition

**Google Ads** (TrendTrack, onglet Google Ads, 25/08) : **9 annonces globales, 8 dans la bibliothèque
EU/UK (89 %)**, annonceur STANFIELD.

| Format | Impressions | Active depuis | Durée |
|---|---|---|---:|
| **SHOPPING**, image | **80 000-90 000** | 15/01/2026 | **219 j** |
| SEARCH, texte | 15 000-20 000 | 28/01/2026 | 206 j |
| SEARCH, texte | 6 000-7 000 | 15/01/2026 | 219 j |
| SEARCH, texte | 5 000-6 000 | 15/01/2026 | 219 j |
| SEARCH, image | 0-1 000 | 20/03/2026 | 155 j |
| OTHER, image | 5 000-6 000 | 15/01/2026 | 219 j |
| OTHER, image | 0-1 000 | 01/05/2026 | 113 j |

Pays visibles sur les cartes : **FR, BE, ES**. Selon la règle de l'étape 7, **une annonce Shopping
tenue 219 jours d'affilée est une preuve que le rayon nourrit**, indépendamment de tout volume.

**Meta Ads** : 3 actives. La plus grosse totalise **393 000 impressions pour ~4 000 $ dépensés,
17 $/jour, active depuis le 22/01/2026 (214 jours)**. Ciblage BE 33 % / FR 33 % / LU 33 %. Le corps
d'annonce est un bloc à quatre puces avec émojis (« ✅ + 3000 clients satisfaits dans le monde »,
« 📦 Livraison suivie et emballage sécurisé », « 💬 Service client disponible et réactif »,
« ✨ Luminaires soigneusement sélectionnés ») et le titre « 4,7/5 sur 3000 Avis ».

### Trafic — deux sources, un écart de 4,5×

| Source | Mesure | Lecture |
|---|---|---|
| **SEMrush France**, 24/08/2026 | **trafic organique estimé 161 900/mois** (-4,9 %), 13 400 mots-clés (+14 %), **part de trafic de marque 23 %** → net de marque ≈ **124 700**, Authority Score 37, 923 100 backlinks, 867 domaines référents, trafic payant vu par l'outil : 0 | organique seul, hors direct, social et payant |
| **TrendTrack**, 25/08/2026 | **36 000 visites/mois** (+7 %). Série sur 22 mois : 53K (oct. 24) · 57K · 45K · 42K · 40K · 40K · **16K · 13K · 16K** (avr.-juin 25) · 27K · 22K · 31K · 42K · 48K · 48K · 38K · 47K · **52K** (mars 26) · 45K · 31K · 34K · **36K** (juil. 26). Pays : FR 73 %, BE 9 %, CH 6 %, US 6 %, DE 2 % | outil de veille publicitaire |

**Les deux chiffres sont inconciliables et je ne les réconcilie pas.** Selon la règle de l'agent
`cartographie-concurrence` (« ne rends jamais un verdict sur les visites affichées par un outil de
veille publicitaire »), **c'est le chiffre SEMrush qui fait foi** et le 36K de TrendTrack qui est
écarté. SimilarWeb n'a pas été consulté : **la règle maison « trafic réel ≈ SimilarWeb × 3 » n'a pas
pu être appliquée**, et le volume total de visites toutes sources reste donc non établi.

Ce que la série TrendTrack garde d'utile, en tendance et non en niveau : **un effondrement au
printemps 2025 (-68 % en trois mois), une reconstruction jusqu'en mars 2026, et une nouvelle baisse
de 31 % entre mars et juillet 2026.** SEMrush confirme le sens avec -4,9 % sur l'organique.
**Lustria descend, en ce moment.**

Autre chiffre TrendTrack : **Trustpilot 3,1 sur 88 avis**, et un compteur de produits à **446** —
contre 5 928 relevées dans `products.json`. **Le catalogue affiché par TrendTrack est faux d'un
facteur 13** ; c'est probablement un instantané de 2022 jamais rafraîchi, ce qui explique aussi que
ses 40 best-sellers soient tous antérieurs à 2023.

---

## 7. Leurs faiblesses, classées par ce qu'on peut en faire

### Ce qu'on peut attaquer

| # | Faiblesse | La preuve | Ce qu'on en fait |
|---:|---|---|---|
| 1 | **Contradiction de délai** | Hero d'accueil : « LIVRAISON EN 4 À 7 JOURS ». Page *Notre Histoire* : « **10 à 35 jours ouvrés** » pour les gammes internationales, qui sont **74 % du catalogue** (4 400 fiches vendor `Lustria`) | Notre 7-17 jours annoncé franchement devient un argument, pas un handicap. On affiche une fourchette qu'on tient, sans hero qui la contredit |
| 2 | **Note d'avis non étayée** | Fiche produit : « 4.7/5 sur plus de 3000 clients ». Annonces Meta : « 4,7/5 sur 3000 Avis ». **Trustpilot réel : 3,1 sur 88 avis.** **1 076 fiches taguées `No Review`**, aucun widget d'avis tiers chargé | On installe de vrais avis vérifiés, même peu nombreux, et on ne recopie jamais leur formule. Un compteur maison ne vaut rien face à un tiers |
| 3 | **Compteur client incohérent** | Accueil : « PLUS DE 6000 CLIENTS ». Annonces et fiche produit : « 3000 clients ». Les deux sont affichés le même jour | Ne pas afficher de compteur non vérifiable. Rien à copier |
| 4 | **Retours 14 jours** | Page `conditions-de-retour` : « 14 jours après réception », frais de renvoi à la charge du client | **Nos 30 jours sont un avantage réel et gratuit.** À mettre en réassurance de fiche, en clair |
| 5 | **131 collections vides publiées** | dont ~60 résidus d'import polonais aux titres à point-virgule, 15 collections `spot*` et 7 `abat-jour*` | Un rayon qu'ils annoncent sans le tenir. Preuve d'inventaire utilisable en comparaison, et signal de catalogue à ne jamais reproduire chez nous |
| 6 | **Règles de collection cassées** | `lampadaire-chambre-adulte` = 4 812 produits pour 126 lampadaires ; `luminaire-gris` = 3 538 = le total de `luminaire` | Leurs pages servent des produits hors sujet. Une collection de pièce **juste** bat une collection de pièce **grosse** |
| 7 | **Texte de collection qui envoie chez le concurrent** | `suspension-rotin` : « Les meilleures suspensions en rotin se trouvent dans des magasins spécialisés et des boutiques en ligne réputées comme Lustria, **IKEA et Alinea** ». Sous-titres = requêtes recopiées : « Suspension rotin • le palais du rotin » | Notre texte de collection, plus court mais écrit et relu, peut battre 1 434 mots générés. C'est la brèche éditoriale la plus large du site |
| 8 | **Pages sur marques déposées** | 6 collections `alternative-{concurrent}` (Alinéa, Keria ×2, Laurie Lumière, Light Online) + `meilleur-magasin-luminaire`, **7 324 visites/mois** | **À ne pas reprendre** : inécrivable en flux Merchant Center (étape 4 de la méthode) et exposé juridiquement. Leur dépendance à ces pages est en revanche une fragilité à noter |
| 9 | **Profil de liens à dominante sitewide** | **923 100 backlinks pour 867 domaines référents** = 1 065 liens par domaine | Un profil qui tient sur peu de domaines se déclasse vite. Explique peut-être le -68 % du printemps 2025 |
| 10 | **Relecture absente** | `Applque Murale`, `Lampadaire|`, `Veilleuse |JOLINA`, `Tour sur sur les lustres pampilles`, `stockTout savoir sur`, « Notre portons une grande attention » | Signal de qualité. Notre catalogue de 120 fiches peut être irréprochable là où le leur ne peut pas |
| 11 | **Titre produit sans mot-clé** | 5 928 titres `{Type} \| {NOM-CODE}`, 0 % de matière, 0 % de pièce, médiane 28 caractères | Notre convention du 25/08 les bat sur ce champ. Réserve : leur flux Meta réécrit les titres, leur flux Shopping n'a pas pu être établi |
| 12 | **Trafic en baisse** | SEMrush -4,9 % ; TrendTrack 52K (mars 26) → 36K (juil. 26), soit -31 % | Le moment est bon. Un concurrent qui monte se dispute pied à pied ; un concurrent qui descend laisse des positions |

### Ce qui n'est pas une faiblesse — et tout axe qui suppose de les battre là-dessus se jette

**Décision, pas oubli.** On écarte formellement quatre angles :

- **L'antériorité et l'autorité.** 5 ans, Authority Score 37, 991 pages indexées, 13 400 mots-clés,
  position 3 sur `applique murale` (49 500). On ne rattrape pas ça, on contourne par la profondeur
  d'une famille étroite.
- **Le prix bas.** Leur médiane est à 169,90 €, avec 11 % du catalogue sous 50 € et des veilleuses à
  11,90 €. On ne va pas là.
- **Le délai.** Leurs 1 528 fiches de fabricants polonais partent d'entrepôts européens en 3-6 jours,
  avec des fiches techniques issues des données constructeur. Sans compte B2B européen, on ne fait
  pas mieux. **On fait plus honnête, pas plus rapide.**
- **Le dispositif de service.** Gorgias, Klaviyo, SMSBump, TrackingMore, SAV lundi-vendredi 8h-17h,
  Klarna, espace B2B avec devis en 48 h, blog tenu à jour, FAQ en JSON-LD. C'est une boutique
  outillée. On copie les briques les moins chères, on ne prétend pas au même niveau de service.

---

# Ce qu'il faut ajouter chez nous

Trois listes, ordonnées par impact. Chaque ligne porte sa preuve : un chiffre de trafic Lustria
mesuré URL par URL (SEMrush FR, 24/08), un volume SEMrush de `MOTS-CLES-TITRES-2026-08-25.md`
(25/08, consolidé sauf mention), ou un relevé de catalogue (`products.json` / `collections.json`,
25/08). **Rien d'intuitif.**

## A. Collections à créer — dix, dans cet ordre

| # | Nom exact | Mot-clé visé | Volume mesuré | Chez Lustria | Nos fiches déjà éligibles | Fiches à sourcer |
|---:|---|---|---:|---|---:|---:|
| **1** | **Plafonniers LED** (renommer `Plafonniers`) | `plafonnier led` | **21 090** (tête 14 800, ×1,4) | `/collections/plafonnier` = **5 800 visites/mois**, leur 4ᵉ page, 227 mots-clés — sur 1 139 fiches | **10** (les 10 plafonniers, tous LED) | +10 à 15 |
| **2** | **Lustres chambre** | `lustre chambre` | **10 810** | `lustre-chambre` 2 760 fiches. **La chambre leur rapporte 11 403 visites/mois sur 8 pages** : `luminaire-chambre` 5 000, `luminaire-chambre-adulte` 2 100, `applique-murale-chambre-adulte` 1 200, `lustre-chambre-adulte` 866, `plafonnier-chambre-adulte` 795, `lampadaire-chambre` 629, `plafonnier-chambre` 467, `suspension-chambre-bebe` 346 | **~10** : anneau Ø 20-30, effet cristal Ø 20 et 2 lumières, lustre salon Ø 33-43 | +8 à 12 |
| **3** | **Plafonniers salon** | `plafonnier salon` | **8 970** | `plafonnier-salon` 1 017 fiches ; `plafonnier-moderne` = 1 700 visites sur le mot `plafonnier` | 6 à 8 plafonniers grand diamètre | +8 |
| **4** | **Suspensions cuisine** | `suspension cuisine` | **4 800** | **la preuve la plus forte du dossier** : `luminaire-cuisine` 6 600 + `suspension-cuisine` 5 100 + `lustre-cuisine` 4 000 + `applique-murale-cuisine` 1 600 = **17 300 visites/mois sur la cuisine, en 4 pages** | **~20** : verre Ø 20-40, bambou/rotin petits diamètres, métal 3 lumières | +10 |
| **5** | **Plafonniers cuisine** | `plafonnier cuisine` | **6 190** (chiffre de la commande ; le dossier du 25/08 ne donne que la tête seule à 5 400) | `plafonnier-cuisine` : 796 fiches, et **aucune page dans leur top 100** — la seule case du bloc cuisine qu'ils n'ont pas fait rentrer | 4 à 6 plafonniers plats | +10 |
| **6** | **Lustres pampilles** (renommer `Lustres effet cristal`) | `lustre pampilles` | **6 340** — tête 1 600, **×4,0**, le plus gros multiplicateur mesuré | **`lustre-pampilles` a 0 produit, 3 424 caractères de texte, et gagne 890 visites/mois sur 84 mots-clés.** Une page vide qui classe : le mot est libre et prouvé | **7** (les 7 effet cristal) | **0** |
| **7** | **Suspensions salon** | `suspension salon` | **3 600** | `suspension-salon` 2 143 fiches ; `suspension-moderne` = 2 200 visites sur `suspension pour salon` ; `luminaire-salon` 2 000 | 12 à 15 suspensions grand format | +5 |
| **8** | **Suspensions papier** | `suspension papier` | **4 760** (tête 1 600, ×3,0) | `suspension-luminaire-papier` : **28 fiches → 363 visites**. Le plus faible investissement de leur catalogue sur un mot qui vaut 4 760. **Porte entrouverte** | 1 (abat-jour Papier DuPont) | **+10 à 12** |
| **9** | **Grandes suspensions XXL** | `suspension xxl` 720 + `grande suspension` 590 | 1 310 | **`suspension-xxl` : 20 fiches → 1 200 visites/mois, soit 60 visites par fiche — le meilleur rendement de tout leur catalogue** | 8 à 10 fiches en Ø 60-150 cm | +5 |
| **10** | **Suspensions osier** | `suspension osier` | **3 180** (tête 1 600, ×2,0) | `luminaire-osier` : 32 fiches → 833 visites ; le tag `Osier` ne couvre que 34 fiches sur 5 928 | 4 à 6 fiches rotin dont la photo montre de l'osier | +6 |

**Trois notes de méthode sur cette liste.**

- **Ne pas créer de collection de couleur.** 100 collections de couleur chez Lustria pour **2,4 % de
  leur trafic** (3 417 visites), et `suspension dorée` ne vaut que **170** chez nous alors que le doré
  est très présent dans notre catalogue. Verdict mort, confirmé des deux côtés.
- **Ne pas créer de collection de forme.** Nos mesures du 25/08 : `suspension grappe` 210,
  `suspension cloche` 140, `suspension cascade` 40, `suspension dôme` 20. Seule exception,
  **`suspension boule` à 2 300** — à garder en réserve, pas en priorité.
- **Une collection sans H1 ni meta propres ne rapporte rien**, quel que soit son mot-clé (étape 8 de
  la méthode). `collections-seo.json` porte déjà 14 entrées à `seo_title` + `seo_description` +
  `description_html` : les dix nouvelles doivent y entrer au même format avant publication.

## B. Produits à sourcer — cinq, dans cet ordre

### 1. Appliques murales — le trou n°1, et de loin

- **Combien** : 30 à 40 fiches en première vague.
- **Fourchette** : **79 à 229 €** (leur p25 et leur p75 ; médiane 129,90 €). **Cela impose de
  descendre sous notre plancher actuel de 149 €.**
- **Pourquoi c'est important** : `/collections/applique-murale` est **leur page n°1 avec 9 000
  visites/mois**, en **position 3 sur `applique murale` dont le volume est 49 500** (SEMrush FR,
  24/08). Les appliques pèsent **29 804 visites/mois, 20,8 % de leur trafic total**, réparties sur
  20 pages dont 12 dépassent 700 visites. **11 de leurs 30 premiers best-sellers TrendTrack sont des
  appliques**, et **5 des 10 vignettes de leur section « Nos Meilleures Ventes »**. Nous en avons
  **zéro**.
- **Ce que Lustria vend là** : 1 522 fiches, de 14,76 à 1 169,90 €. Sous-familles par pièce, avec
  leur trafic : salle de bain 134 fiches → 2 300 visites · cuisine 294 → 1 600 · escalier 137 →
  1 400 · chambre adulte 667 → 1 200 · noire → 921 · extérieur → 996 · rotin 14 → 735 · verre 286 →
  727 · tête de lit 284 → 513 · enfant 68 → 518.
- **Par où entrer** : `applique murale salle de bain` et `applique murale escalier` sont leurs
  meilleures sous-pages par rapport au nombre de fiches (2 300 pour 134, 1 400 pour 137). Cohérent
  avec notre axe matière : appliques rotin (14 fiches chez eux seulement, 735 visites), bois (131,
  464 visites), verre (286, 727 visites).

### 2. Luminaires d'extérieur — le meilleur rendement par fiche du marché observé

- **Combien** : 15 à 20 fiches.
- **Fourchette** : **85 à 200 €** (leur p25 et p75 ; médiane 119,90 €, min 19,90, max 589,90).
- **Pourquoi** : **7 196 visites/mois avec 121 fiches, soit 59,5 visites par fiche** — le plus haut
  ratio de leur catalogue hors `suspension-xxl`. Une seule URL,
  `/collections/luminaire-exterieur`, classe sur **442 mots-clés** et fait 6 200 visites ;
  `applique-murale-exterieur` en ajoute 996 sur 286 mots-clés. Et leur famille est **manifestement
  sous-dotée** : 121 fiches sur 5 928, soit 2 % du catalogue pour 4,5 % du trafic.
- **Ce que Lustria vend là** : appliques murales extérieures LED (rondes, carrées), bornes de jardin,
  spots d'escalier, luminaires de terrasse. Handles relevés : `borne-luminaire-exterieur`,
  `spot-exterieur-pour-escalier-de-forme-carre-ou-rond`, `luminaire-exterieur-ip67`,
  `petite-applique-murale-exterieure-led`, `eclairage-exterieur-pas-cher` à 19,90 €.
- **Réserve à écrire** : l'indice de protection est une **allégation technique vérifiable**. IP44,
  IP65, IP67 ne s'écrivent que si la fiche fournisseur les documente — même règle que « montre de
  plongée sans boîtier 200 m » dans le catalogue des pièges. Sans donnée fournisseur, pas de mot.

### 3. Lustres et suspensions à pampilles — pour remplir la collection n°6

- **Combien** : 6 à 10 fiches.
- **Fourchette** : 199 à 349 € (notre bande haute actuelle).
- **Pourquoi** : `lustre pampilles` vaut **6 340**, soit **2,4 fois `lustre cristal` (2 610)**, et le
  mot ne revendique aucune matière — donc écrivable sans mentir sur du verre travaillé. **Lustria
  ranke dessus avec une collection vide** (890 visites, 84 mots-clés, 0 produit) : le mot est prouvé
  et la place est libre. Nos 7 fiches « effet cristal » ouvrent la collection ; 6 de plus la rendent
  crédible.
- **Ce que Lustria vend là** : rien. 9 fiches seulement mentionnent « pampille » dans tout leur
  catalogue, et aucune n'est dans la collection.

### 4. Suspensions en papier et en fibre claire — pour la collection n°8

- **Combien** : 10 à 12 fiches.
- **Fourchette** : 149 à 249 €.
- **Pourquoi** : `suspension papier` vaut **4 760** (×3,0 sur la tête), et **le tag `Papier` ne
  couvre aucune fiche chez Lustria** — leur facette `Matériaux` sur les appliques n'en compte
  qu'**une seule sur 1 522**. Leur collection papier existe (28 fiches, 363 visites) mais elle est
  peuplée par défaut. C'est le mot le mieux dosé du dossier : gros volume, concurrence directe quasi
  nulle, sourcing simple (abat-jour voile, riz, lanterne).

### 5. Lampadaires haut de gamme — pour ouvrir le haut du catalogue

- **Combien** : 8 à 12 fiches.
- **Fourchette** : **360 à 750 €** (leur p25 et p75 ; **médiane 499,90 €**).
- **Pourquoi** : c'est leur famille la plus chère et **la seule qui soit entièrement au-dessus de
  notre plafond de 299 €**. Elle ne pèse que 2 168 visites/mois, donc **ce n'est pas un achat de
  trafic, c'est un achat de panier moyen** — et le rendement par fiche reste bon (17,2). Portes
  d'entrée mesurées chez eux : `lampadaire-vintage` 65 mots-clés → **680 visites**,
  `lampadaire-rechargeable` **560 visites**, `lampadaire-chambre` 629, `lampadaire` nu 299.
- **À ne pas faire dans le même mouvement** : les **lampes de chevet** (319 fiches chez eux pour
  1 137 visites, 3,6 par fiche) et les **veilleuses** (263 fiches, **aucune page classée**). Volume
  de catalogue sans demande. On y viendra pour le cross-sell, jamais pour l'acquisition.

## C. Corrections de structure et de copy — dix, dans cet ordre

| # | Ce qu'ils font mieux | La preuve | Ce qu'on change |
|---:|---|---|---|
| **1** | **Le mot-clé dans le handle** | `suspension-rotin-pas-cher`, `plafonnier-original-salon`, `applique-murale-exterieure-led-ronde` contre nos `suspension-verre-led-489156` | Réécrire les 120 handles sur la requête de la fiche. Redirections 301 obligatoires. **Gain le moins cher du dossier** |
| **2** | **Balise title distincte du H1** | `<title>` = `Suspension Rotin Pas Cher Design Torsadé Brun – Lustria`, H1 = `Suspension Luminaire \| ROLIN` | Découpler nos deux champs : le H1 reste notre titre de convention, la balise title prend la requête complète. Deux emplacements, deux mots |
| **3** | **La facette « Pièce »** | 18 axes de facettes, dont Pièce à 11 valeurs (Salon 1 338, Chambre 1 460, Cuisine 526…), alimentés par métafields. **Nous en avons 0** | Créer les métafields et publier au minimum 4 facettes : Pièce, Matière, Nombre de lumières, Diamètre. La pièce d'abord, puisqu'elle porte 38,8 % de leur trafic |
| **4** | **La fiche technique tabulée** | 16 lignes : culot, ampoule incluse, type, couleur, dimmable, température K, **distance d'éclairage**, matériaux, nombre de lumières, alimentation, IP, style, voltage, puissance, dimensions par taille, dimensions support. Description médiane **5 101 caractères** contre nos **329** | Un tableau de spécifications sur chaque fiche. « Ampoule incluse : non » et « Culot : G9 » évitent un retour et une question SAV. Ne rien écrire qui ne soit dans la fiche fournisseur |
| **5** | **Le texte de collection** | 1 400 à 1 900 mots par page, avec H2 structurés et FAQ. Nos `description_html` font **840 caractères, ~120 mots** — **12 fois moins** | Passer à 400-600 mots relus, structurés en H2, avec 4-6 questions. **Pas 1 400 mots générés** : leur texte cite IKEA et Alinea comme endroits où acheter. Court et juste bat long et spun |
| **6** | **Le prix dans le bouton** | « AJOUTER AU PANIER - 139,90€ » | Reprendre tel quel. Coût nul |
| **7** | **Le fil d'Ariane par type** | `Lustria / Suspension Luminaire / {produit}` | Ajouter le fil d'Ariane, avec la collection de matière **et** la collection de pièce quand la fiche appartient aux deux |
| **8** | **L'espace B2B** | Entrée de menu, page `luminaire-professionnel` « Devis personnalisé en 48h », bloc sur chaque fiche, bloc sur l'accueil, lien en pied de page. Collection `Livraison Sous 7 Jours` de 1 133 fiches | Une page de demande de devis. Zéro stock, zéro coût, un panier moyen sans commune mesure. Sans promettre de délai qu'on ne tient pas |
| **9** | **Le blog utile** | 6 articles en août 2026, tous en question pratique. 5 articles = **2 518 visites/mois**, dont `tendance-luminaire-2026` à **954 visites sur 349 mots-clés** | 6 articles, format « Combien de lumens pour… », « Comment installer… », « Quelle hauteur pour… ». C'est 1,8 % de leur trafic pour un coût marginal |
| **10** | **La FAQ en JSON-LD** | 35 questions sur l'accueil, page FAQ avec `FAQPage` structuré, réponses franches (« Avez-vous un magasin physique ? » → non) | Une FAQ balisée, dont la moitié des questions sont des questions de choix d'éclairage. Leur franchise est reprenable et coûte zéro |

**Et cinq choses à ne pas copier, écrites comme des décisions :**

1. **Les collections `alternative-{concurrent}`.** 7 324 visites/mois, position 1 sur `keria
   luminaire`. Marques déposées françaises : inécrivables en flux Merchant Center (étape 4) et
   exposition juridique. **Rejeté.**
2. **Une note d'avis affichée sans widget tiers.** Leur 4,7/5 contre un Trustpilot à 3,1/88 est
   exactement ce qu'on ne fait pas.
3. **Les 100 collections de couleur** : 2,4 % de leur trafic. Mort mesuré.
4. **Les titres `{Type} | {NOM-CODE}`** : notre convention du 25/08 est meilleure. Le seul emprunt
   est le handle et la balise title.
5. **Le volume de catalogue.** 5 928 fiches, 131 collections vides, des règles de collection cassées
   — et **leurs 40 best-sellers datent tous de 2021-2022**. La masse ne vend pas. Ce sont les fiches
   anciennes et travaillées qui vendent, ce qui valide notre format de 120 fiches soignées.

**Deux corrections internes que la comparaison fait apparaître, hors périmètre Lustria :**

- ~~62 de nos 120 titres contiennent encore un `Ø` et une plage de diamètres.~~ **Faux, corrigé
  le 26/08.** Cette ligne venait d'un dump local périmé (`titles-live-2026-08-25.json`, pris avant
  la refonte). Relecture de l'API Admin le 26/08 à 00h30 : **0 titre avec `Ø`, 0 plage de diamètres
  sur les 120 fiches actives.** Le nettoyage décidé dans `CONVENTION-TITRES-2026-08-25.md` est
  appliqué en totalité. Le constat sur Lustria reste vrai : ils n'en mettent jamais non plus.
- **Notre médiane de prix est à 199 € contre 169,90 € chez le comparable direct.** L'étape 9 de la
  méthode demande de se placer **juste en dessous**. Ce n'est pas le cas aujourd'hui, et les
  30 nouvelles fiches d'appliques (bande 79-229 €) sont l'occasion de corriger par le bas du
  catalogue plutôt que par une baisse générale.

---

## Ce que je n'ai pas pu établir

Section obligatoire. Sans elle, ce dossier ne se relit pas dans un mois.

1. **Le `sitemap.xml` n'a jamais répondu** : Cloudflare a posé un *managed challenge* après la 21ᵉ
   page de `products.json` et a bloqué `robots.txt` et `sitemap.xml`. **La distinction entre
   collections au menu et collections orphelines est donc partielle** : je n'ai relevé le menu que
   sur les 4 premiers déroulés, complets, mais je ne peux pas affirmer qu'aucune des 556 collections
   n'est atteignable autrement.
2. **Le contenu de leur flux Google Merchant Center.** Leurs annonces Meta portent des titres
   riches (« Suspension Luminaire Salon Design Tubes Croisés, S ») très différents du titre produit
   Shopify. Ils réécrivent donc leurs titres au niveau du flux. **Je ne sais pas si leur flux
   Shopping porte le nom de code ou la requête**, et donc la conclusion « nous les battons en
   Shopping sur le titre » est probable, pas démontrée.
3. **Le texte de leurs annonces Google Search.** TrendTrack affiche « Les Google Ads sont
   disponibles uniquement après le brandtrack ». Le format, les impressions et la durée sont
   relevés ; **les titres et descriptions des 3 annonces Search ne le sont pas**, donc les mots-clés
   qu'ils achètent restent inconnus. Le brandtracker n'a pas été activé (engagement de compte).
4. **La répartition des pays ciblés en Google Ads.** Cinq pourcentages sont affichés (23 / 19 / 14 /
   11 / 8 %) mais les pastilles de drapeau ne se laissent lire que pour FR, BE et ES. **La
   correspondance exacte n'est pas établie.**
5. **SimilarWeb n'a pas été consulté.** La règle maison « trafic réel ≈ SimilarWeb × 3 » **n'a pas pu
   être appliquée** : le volume de visites toutes sources confondues reste inconnu. Les 161 900 de
   SEMrush sont de l'**organique estimé**, dont **23 % de trafic de marque**, hors direct, hors
   social, hors payant.
6. **L'écart TrendTrack / SEMrush n'est pas expliqué** (36 000 contre 161 900, facteur 4,5). Le
   compteur de produits de TrendTrack étant faux d'un facteur 13 (446 contre 5 928) et ses
   best-sellers s'arrêtant en 2022, l'hypothèse d'un instantané périmé est la plus probable —
   **c'est une hypothèse, pas une mesure.**
7. **Les pages les plus vues au sens de l'audience réelle.** TrendTrack n'offre pas ce rapport. Les
   chiffres URL par URL du présent dossier sont du **trafic organique estimé par SEMrush**, pas des
   visites mesurées, et couvrent **100 URL sur les 1 016 classées (89 % du trafic estimé)** : les
   916 pages restantes pèsent ~18 700 visites non ventilées.
8. **La liste complète des applications Shopify.** TrendTrack affiche une section « Apps Shopify »
   vide. Les outils cités ont été identifiés par les scripts chargés sur deux pages : **une app sans
   script front-end est invisible pour cette méthode.**
9. **Le registre du commerce n'a pas été consulté.** Le classement de Lustria — un pure player
   hybride, dropshipping international majoritaire adossé à trois catalogues de fabricants
   européens — s'appuie sur des signaux de catalogue nommés (4 vendors, résidus d'import polonais,
   délais annoncés par gamme) et sur les mentions légales. **C'est un jugement documenté, pas une
   preuve.** L'écart entre la création de la boutique (juin 2021) et l'immatriculation de la SASU
   Stanfield (01/03/2024) est un constat brut.
10. **Aucun volume de mots-clés n'a été mesuré ici.** Tous les volumes cités viennent de
    `MOTS-CLES-TITRES-2026-08-25.md`, lecture du 25/08/2026, base France, expression exacte,
    consolidés par variantes d'écriture — sauf `plafonnier cuisine` à 6 190, qui vient de la commande
    de Hakim et **dont je n'ai pas la trace de mesure** (le dossier du 25/08 ne donne que la tête
    seule à 5 400). Les volumes de `applique murale` (49 500), `luminaire cuisine` (8 100),
    `keria luminaire` (8 100) et `lustre salon` (22 200) sont lus dans le rapport SEMrush de
    lustria.fr, pas remesurés. **Un chiffre recopié devient vrai par répétition** : tout réemploi de
    ces nombres doit citer cette date.
11. **Aucun accès à leurs volumes de vente.** Les « best-sellers » sont l'ordre de tri de TrendTrack
    et l'ordre d'affichage de leur page d'accueil. Ce sont des **mises en avant**, pas des ventes.
12. **`git` n'a pas été touché et aucun fichier de la boutique n'a été modifié**, conformément à la
    commande. Ce rapport et les trois dumps JSON qui l'accompagnent sont les seuls fichiers créés.
    **Le réflexe GitHub de `CLAUDE.md` n'a donc pas été appliqué**, sur interdiction explicite : le
    commit reste à faire par Hakim ou sur son feu vert.

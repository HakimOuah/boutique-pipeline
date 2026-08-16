# Brief visuels — Tuftéo, machines (nouveaux fournisseurs), 16/08/2026

Production de **2 séries de visuels produit** (6 images chacune, comme le reste du catalogue),
bloquantes avant réintégration au flux Google Shopping. Les deux fiches ont changé de fournisseur
AliExpress le 16/08/2026 (voir `EXECUTION-2026-08-16.md`, section « Fiches machines — nouveaux
fournisseurs ») et **les 12 photos actuellement en ligne montrent l'ancien produit, pas le nouveau**.

## Pourquoi c'est urgent

Sur `ciseaux-electriques-sculpture`, la fiche affiche aujourd'hui le texte **« Sans fil, batteries
incluses »** à côté d'une photo d'un outil **filaire avec un cordon et une prise DC** — contradiction
visible immédiatement par n'importe quel visiteur. Vérifié à l'écran le 16/08/2026 (capture de la page
live). Ce n'est pas qu'un problème Shopping, c'est un problème de confiance client immédiat.

## Règles maison, non négociables (rappel)

1. **Jamais la photo fournisseur brute.** On génère à partir de l'image produit du fournisseur en ne
   changeant que la mise en scène. On ne publie pas le fichier d'origine tel quel.
2. **Aucun texte incrusté, aucun collage, aucun filigrane, aucun logo.** Motif de refus direct en
   Shopping — et ici il y a une raison de plus : **les deux produits sources portent des logos de
   marque tierce visibles** (voir ci-dessous), qui doivent impérativement disparaître du rendu final.
3. **Aucune promesse visuelle invérifiable** : pas de badge « garantie », « professionnel », « n°1 »,
   pas de mention CE (le fournisseur ne l'a pas prouvée), pas de mention de marque tierce.
4. **Le produit doit être reconnaissable et entier**, à la bonne échelle, dans le bon état (avec/sans
   fil selon le vrai produit).

## Logos et marques à ne jamais reproduire

- **Tondeuse (240 W)** : le grip en caoutchouc du manche porte un texte gravé « EASYCLIP » (ou
  approchant, partiellement lisible sur la photo source). **À effacer entièrement** — ni le nom ni un
  logo stylisé ne doivent apparaître dans le rendu.
- **Ciseaux ONEVAN (800 W)** : logo « ONEVAN » imprimé sur l'outil, sur les deux batteries et sur la
  boîte carton, plus un marquage « CE » visible sur le corps de l'outil. **À effacer entièrement** —
  outil, batteries et boîte doivent apparaître neutres, sans texte de marque ni marquage CE (cette
  mention n'a pas été vérifiée et ne doit donc pas apparaître, même par ricochet via la photo
  fournisseur).
- Ne pas non plus faire apparaître le mot ou le logo **Makita** sur les batteries redessinées — le
  produit n'est pas un produit Makita, seulement annoncé compatible par le fournisseur.

## Spécifications techniques

- **Format carré, 1600 × 1600 px minimum**, JPEG ou PNG, moins de 2 Mo.
- **Fond neutre et constant** : crème très clair (`#F7F1E8`, teinte Tuftéo) ou blanc cassé. Le produit
  occupe environ 80 % du cadre, centré, ombre portée douce — cohérent avec le reste du catalogue
  (voir les images déjà en ligne des autres fiches machines pour le style attendu).
- Aucun badge de garantie, aucune mention CE, aucune mention de marque tierce, aucun texte.

## Série 1 — Tondeuse électrique pour tapis (`tondeuse-professionnelle-tapis`, 240 W)

Nouveau fournisseur AliExpress : `1005007430527466` (confiance **B** — SERP JSON, page produit non
accessible, mur anti-bot). Ships depuis l'Allemagne, EU plug, un seul SKU (pas de variante couleur).

**Image de base disponible** (récupérée depuis la SERP AliExpress, 800×800, seule vue trouvée à ce
stade) :
`boutique-pipeline/boutique-tufting/images/240w-carpet-trimmer-tufting-easyclip-eu-plug-shipped-from-germany-1005007430527466/240w-carpet-trimmer-tufting-easyclip-eu-plug-shipped-from-germany-1005007430527466-serp-01.png`

Cette image montre l'ensemble complet tel que vendu : la tondeuse (manche bicolore rouge/or, tête à
lame T), un boîtier d'alimentation externe à molette de réglage de vitesse, 2 lames de rechange, 2
sabots-guides à peigne, une brosse de nettoyage, et un support/pied de rangement (base + bras
articulé). **Le manche porte le logo « EASYCLIP » à effacer** (voir section logos ci-dessus).

**Ce qu'il faut produire (6 images, comme le standard du catalogue)** :
1. Vue produit principale : la tondeuse seule, angle 3/4, montrant la tête de coupe et le manche —
   sans logo, sans le câble qui traîne de façon disgracieuse.
2. Vue de la tête de coupe en gros plan (montre la lame T).
3. Vue du boîtier d'alimentation à molette seul (c'est un accessoire matériellement important, le
   client doit comprendre qu'il est inclus et à quoi il ressemble).
4. Vue d'ensemble du kit complet : tondeuse + boîtier + 2 lames de rechange + 2 guides + brosse +
   support, posés ensemble sur le fond crème (mise en scène « tout ce qui est livré », pas un
   collage — une vraie photo composée d'objets disposés).
5. Vue en usage/mise en situation (tondeuse tenue en main au-dessus d'une pièce tuftée, dans le style
   des autres fiches machines du catalogue).
6. Vue du support/pied de rangement seul, avec la tondeuse posée dessus.

**Nommage** : `tondeuse-electrique-tapis-01.png` à `-06.png`.

## Série 2 — Ciseaux électriques sans fil de sculpture (`ciseaux-electriques-sculpture`, ONEVAN 800 W)

Nouveau fournisseur AliExpress : `1005011898820067` (confiance **B**). Ships depuis l'Allemagne.
**Un seul SKU achetable** : « 2 Battery Set » (stock 5) — la configuration « Without Battery » est à
stock 0, ne pas s'en servir comme référence de ce qui est réellement vendu.

**Images de base disponibles** (dossier
`boutique-pipeline/boutique-tufting/images/onevan-800w-cordless-electric-scissors-tapis-cuir-tissu-makita-18v-compatible-1005011898820067/`) :
- `onevan-800w-cordless-electric-scissors-serp-main-01.jpg` — vue marketing du fournisseur (outil +
  2 batteries), sert de référence de forme/couleur (teal/noir) uniquement, **pas à reprendre telle
  quelle** (texte marketing incrusté : « 800W », « 1-6MM », « 900R/MIN », logo, à ignorer).
- `onevan-2-battery-set-box-contents-02.jpg` — photo du contenu de la boîte pour la configuration
  vendue (outil + 2 batteries + chargeur EU + boîte carton). **C'est la vraie composition à
  respecter pour ce qui est montré comme inclus.**
- `onevan-without-battery-box-contents-03-hors-stock.jpg` — fournie **pour référence de forme
  uniquement** (le corps de l'outil sans rien autour) ; ne pas s'en servir pour représenter le contenu
  de la boîte, cette configuration n'est pas en stock.

**Ce qu'il faut produire (6 images)** :
1. Vue produit principale : les ciseaux électriques seuls, angle 3/4, forme pistolet avec batterie
   insérée — sans logo, sans marquage CE, sans texte.
2. Vue de la tête de coupe en gros plan (lame circulaire).
3. Vue de la batterie seule (redessinée neutre, sans marque, sans mention de voltage — ne pas
   reprendre le « 88VF MAX » du fournisseur, cette valeur est jugée trompeuse, voir le rapport
   d'exécution).
4. Vue d'ensemble du kit complet : ciseaux + 2 batteries + chargeur secteur + boîte, posés ensemble
   sur fond crème (mise en scène « tout ce qui est livré »).
5. Vue en usage/mise en situation (ciseaux tenus en main, sculptant un relief sur une pièce tuftée).
6. Vue du chargeur secteur seul avec une batterie en charge.

**Nommage** : `ciseaux-electriques-sans-fil-sculpture-01.png` à `-06.png`.

## Livrables

1. Les **12 fichiers** (6 par produit) dans
   `boutique-pipeline/boutique-tufting/images/visuels-2026-08-16-machines/`.
2. Un fichier **`mapping.json`** dans le même dossier :
   ```json
   [{ "fichier": "tondeuse-electrique-tapis-01.png",
      "handle_produit": "tondeuse-professionnelle-tapis",
      "variante": null,
      "role": "image_principale" },
    { "fichier": "ciseaux-electriques-sans-fil-sculpture-01.png",
      "handle_produit": "ciseaux-electriques-sculpture",
      "variante": null,
      "role": "image_principale" }]
   ```

## Contrôle avant de rendre

- [ ] Aucun texte, logo, marquage CE ou filigrane dans les 12 fichiers (ni EASYCLIP, ni ONEVAN, ni
      Makita, ni « 88VF », ni badge garantie)
- [ ] La tondeuse est montrée avec son boîtier d'alimentation externe (accessoire réel, pas un détail
      cosmétique — sans lui la tondeuse ne fonctionne pas)
- [ ] Les ciseaux sont montrés **sans fil, avec batterie visible** — cohérent avec le texte
      « Sans fil, batteries incluses » déjà en ligne sur la fiche
- [ ] Chaque kit complet montre exactement le contenu réel de la boîte (voir listes ci-dessus), rien
      de plus, rien de moins
- [ ] 1600 × 1600 px minimum, moins de 2 Mo, aucun fichier corrompu
- [ ] `mapping.json` complet et valide, 12 entrées

## Ce qui reste provisoire tant que ce brief n'est pas exécuté

Les 12 images actuellement en ligne sur les deux fiches (issues d'un autre fournisseur AliExpress, pas
celui retenu par Hakim) **ne sont pas retirées** — les retirer sans remplacement laisserait les fiches
sans aucune image, ce qui est pire pour Shopping. Elles doivent être vues comme **provisoires et
trompeuses** jusqu'au remplacement par cette série. Ne pas soumettre ces deux fiches à un flux
Shopping avant remplacement.

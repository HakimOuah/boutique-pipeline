# QA — reprise des 10 visuels

Date : 2026-08-16  
Périmètre : dix JPEG explicitement autorisés dans `targets.txt`.

## Résultat d'installation

- 10/10 sorties installées sous leur nom initial.
- Comparaison SHA-256 avant/après sur les 429 JPEG de premier niveau présents dans l'arborescence de livraison : exactement 10 modifiés, les 419 autres inchangés.
- La liste des dix différences correspond exactement à l'allowlist `targets.txt`.
- Les dix fichiers installés sont identiques octet pour octet aux dix sorties normalisées du workbench.
- Format : JPEG, 2048 × 2048 px, profil `sRGB built-in`.
- Taille : 686 472 à 888 655 octets.
- Les dix nouvelles empreintes SHA-256 sont distinctes.

## Contrôles visuels

### Cadran vert

- Six vues inspectées : cadran vert forêt soleillé continu sur 360 degrés.
- Aucune frontière droite, aucun aplat cyan, aucune zone bicolore.
- Mesure de contrôle HSV des pixels cyan saturés : chaque fichier passe d'un volume non nul dans la sauvegarde originale à `0` dans la sortie finale.
- Aiguille flèche orange, date `3`, triangle à 12 h, rectangles à 6 h et 9 h conservés.

### Cadran noir `g3`

- `10` des minutes rendu comme un nombre à deux chiffres d'un seul tenant et sur un même rayon.
- Traits intermédiaires du secteur 5–15 réguliers en longueur, épaisseur, pas et rayon; rythme cohérent sur la circonférence.

### Coffrets douze montres

- Douze montres et douze compartiments conservés dans chaque coffret, en 6 colonnes × 2 rangées.
- Inspection agrandie des vingt-quatre cadrans : uniquement chiffres/index horaires et aiguilles; aucun logo, mot, lettre, signature ou seconde ligne.
- Aucun caractère ajouté sur la doublure, le verre, le bois ou les ferrures.

### Mallette quinze montres

- Plateau dérivé du `g1` et rendu en macro.
- Exactement quinze logements larges, en 5 colonnes × 3 rangées.
- Aucune quatrième rangée, aucun logement supplémentaire, aucun texte ni objet d'accompagnement.

## Récupération

Les dix JPEG écrasés sont conservés sous `originals/` dans ce workbench. Les empreintes complètes avant/après sont dans `baseline-delivery-jpg.sha256`, `after-delivery-jpg.sha256` et `final-targets.sha256`.

## Règle retenue pour la prochaine passe

Une copie binaire d'un média existant ne sera plus comptée comme un visuel supplémentaire. Le suivi séparera :

1. les associations média/variante ;
2. les visuels réellement uniques, dédupliqués par SHA-256.

Une vue de variante ne comptera comme nouveau visuel que si elle apporte une information visuelle réellement différente. Un même `g5` honnêtement commun à plusieurs variantes comptera une fois, tout en pouvant être associé à plusieurs variantes.

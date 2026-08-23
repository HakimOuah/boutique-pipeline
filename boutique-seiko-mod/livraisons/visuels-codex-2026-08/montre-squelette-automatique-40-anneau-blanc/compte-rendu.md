# Montre squelette automatique 40 — anneau blanc

- Livré : 5 visuels de galerie et 1 visuel de variante.
- Sources retenues : `24.jpg` pour la variante exacte vue de face ; `06.jpg` pour le fond transparent commun à la famille.
- Appariement : `white ring A`, sans ambiguïté.
- La face `24.jpg`, classée `reserve`, a été utilisée par recomposition complète : poignet, filigrane et marquage coloré ne sont repris dans aucun rendu.
- Entrées écartées : aucune ; tous les slots obligatoires sont produits.

## Rejets

Aucun rendu rejeté ; aucun slot n'a dépassé trois générations.

## QA finale

- Contrôle zoomé g1 à g4 : anneau blanc, exactement douze plots ronds, mouvement ajouré, aiguilles principales blanches bordées de noir et trotteuse rouge à détail circulaire cohérents.
- Lunette noire contrôlée : triangle à 12 h, valeurs 10, 20, 30, 40 et 50 aux emplacements de la source, sans chiffre inversé ni ajouté.
- Aucun logo, mot, lettre, numéro de série, texte technique ou pseudo-inscription sur le cadran, le mouvement, le boîtier, le bracelet et le fond.
- Bracelet acier trois maillons nu, sans film ni marquage coloré.
- Fond transparent g5 : visuel arrière commun à la famille, justifié par une construction fournisseur identique ; rotor et rouages stériles, sans inscription.
- Vue portée : anatomie et continuité du bracelet cohérentes ; aucun doigt, visage, bijou ou accessoire.
- Galerie : cadrages distincts entre face, situation oblique, macro 70–80 %, porté et fond non-cadran.
- Fichiers livrés : JPEG sRGB, 2048 × 2048 px, de 461 à 792 Ko.
- Planches : `qa/planche-fiche.jpg` à 900 px par vignette ; `qa/planche-cadrans-zoom-g1-g2-g3-g4.jpg` à 740 px par cadran.

## Jeu de prompts final

Mode : génération intégrée image-vers-image, ancrée sur les photos locales autorisées, avec recomposition complète de la source `reserve`.

- Face : montre complète de face, bracelet acier entier, fond minéral seul.
- Situation : montre à plat, caméra à trois quarts, dalle minérale secondaire floue.
- Macro : cadran et lunette à environ 75 % du cadre, mouvement, plots et graduation entièrement nets.
- Porté : poignet et avant-bras seuls, cadran lisible, bracelet acier continu.
- Détails : montre retournée, fond transparent, rotor et jonctions du bracelet ; cadran absent.

Bloc commun : fidélité stricte à l'anneau blanc observé, douze plots ronds, produit stérile, aucune inscription ni marque, aucun film ou marquage coloré sur le bracelet, fond `#E7E4DE` vers `#FAFAF7`, 12 h en haut et couronne à droite.

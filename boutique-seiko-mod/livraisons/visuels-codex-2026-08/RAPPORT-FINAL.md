# Rapport final — lot de repeuplement Maison Noirmont

Date de contrôle : 2026-08-16  
Périmètre : production locale uniquement, sans opération boutique, import, publication, modification de catalogue ni appel fournisseur.

## Résultat

- 20 fiches terminées.
- 108 visuels produit déclarés : 88 visuels de galerie et 20 visuels de variante.
- 108 fichiers JPEG sRGB, 2048 × 2048 px, tous compris entre 467 007 et 899 632 octets.
- 20 manifestes conformes au schéma strict demandé.
- 57 associations image-source reposent sur une source `ok` ; 51 sur une source `reserve` traitée par recomposition complète.
- Aucune source `ecarte` ou `interdit` utilisée.
- Aucun fichier livré n'est une copie binaire d'une source fournisseur.
- 30 rendus rejetés conservés dans les sous-dossiers `rejected/` avec motif explicite.
- 12 exclusions de sources ou de produits différents documentées dans les manifestes concernés.

Le total de tête annoncé dans la mission était de 86 visuels. Le détail des lignes demandées représente toutefois 88 galeries plus 20 variantes, soit 108 fichiers. La livraison suit ce détail exhaustif et conserve l'écart de comptage de façon explicite.

## Répartition

| Famille | Fiches | Galerie | Variantes | Total |
|---|---:|---:|---:|---:|
| Montres style plongeuse 36 | 4 | 20 | 4 | 24 |
| Porte-montre bois et cuir | 1 | 3 | 1 | 4 |
| Coffrets bois laqué | 4 | 12 | 4 | 16 |
| Malette étanche | 1 | 3 | 1 | 4 |
| Montres style plongeuse 42 titane | 2 | 10 | 2 | 12 |
| Montres squelette 40 | 6 | 30 | 6 | 36 |
| Montres squelette à pont sur cuir | 2 | 10 | 2 | 12 |
| **Total** | **20** | **88** | **20** | **108** |

Les deux fiches aluminium explicitement placées hors périmètre n'ont pas été produites dans ce lot.

## Contrôles de vérité visuelle

- Chaque manifeste référence uniquement un fichier source local existant et autorisé par `GALERIES-DSERS-2026-08-15.json`.
- Les variantes, couleurs, matières, nombres de logements et constructions visibles restent séparés par fiche.
- Les sources `reserve` ont servi d'ancrage produit après recomposition complète ; aucun filigrane, scène fournisseur ou élément tiers n'est repris comme rendu final.
- Les vues de montres respectent la lecture 12 h en haut et la couronne à droite, avec contrôle rapproché des index et graduations.
- Les surfaces produit sont stériles : aucun logo, mot, texte technique, origine, numéro de série ou pseudo-inscription n'est livré.
- Les vues portées ne montrent ni visage, doigt, vêtement, bijou ni accessoire tiers.
- Pour les deux montres à pont, la vue de détail reste limitée au flanc, à la couronne, aux vis de cornes et au cuir réellement prouvés ; aucun fond ou fermoir non documenté n'a été inventé.
- Pour les six montres squelette 40, le détail arrière commun est justifié par la même construction fournisseur et la même source arrière autorisée.

## QA et traçabilité

- 20 planches par fiche, à 900 px par vignette.
- 14 planches de cadrans rapprochés, à 740 px par cadran, pour toutes les fiches de montres.
- 5 planches familiales : style plongeuse 36, coffrets bois, style plongeuse 42 titane, squelette 40 et squelette à pont sur cuir.
- 1 planche globale des 20 faces, à 740 px par fiche.
- Aucun nom de fichier final ne porte un suffixe de galerie au-delà du nombre prévu.
- Aucun terme textuel interdit n'apparaît dans les noms, manifestes ou comptes rendus utilisateur.

## Points d'entrée

- Vue globale : `qa-familles/planche-globale-20-fiches.jpg`
- Planches familiales : `qa-familles/`
- Contrôle détaillé : `<handle>/qa/planche-fiche.jpg`
- Contrôle rapproché des montres : `<handle>/qa/planche-cadrans-zoom-g1-g2-g3-g4.jpg`
- Traçabilité : `<handle>/manifeste.json`
- Décisions et rejets : `<handle>/compte-rendu.md` et `<handle>/rejected/`

## État de livraison

Le lot est prêt pour revue humaine locale. Aucune mutation distante n'a été effectuée et aucune publication n'est implicite dans cette livraison.

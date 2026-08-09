# État de livraison — visuels Maison Noirmont

Date du contrôle : 9 août 2026.

## Verdict

Livraison locale partielle et exploitable : **66 fichiers JPEG** sont inscrits dans les manifestes, répartis entre **60 visuels de galerie** et **6 visuels de variante**.

Ce lot ne constitue pas la production complète des quelque 319 visuels annoncés dans la mission. Aucun fichier manquant n'a été compensé par une apparence, un coloris ou un appariement supposé.

## État par priorité

| Priorité | Périmètre annoncé | Livré | État |
|---|---:|---:|---|
| P0 | 14 visuels | 6 | 2 fiches livrées ; 3 fiches bloquées par les sources locales |
| P1 | 41 visuels | 41 | complet |
| P2 | 14 visuels | 13 | 13 fiches livrées ; `remontoir-solo` bloqué |
| P3 | 33 visuels selon les lignes du tableau | 0 | 6 fiches documentées comme bloquées |
| P4 | 202 visuels | 6 | première série sûre du bracelet caoutchouc gaufré uniquement |
| P5 | hors périmètre sans demande explicite | 0 | non traité |

La rubrique P3 de la mission comporte une incohérence interne : son titre annonce « 5 fiches, 43 visuels », alors que son tableau contient 6 fiches et que la colonne « Manque » totalise 33 visuels. Le tableau a été utilisé comme liste de fiches, sans transformer l'écart arithmétique en production supposée.

## Blocages documentés

### P0

- `trente-neuf-rose-classique-cannelee` : l'unique face locale porte la mention d'origine interdite « SWISS MADE » ; source non utilisée et aucune tentative d'effacement.
- `bracelet-fkm-tropical` : seule source locale partielle ou insuffisamment nette, sans nuancier propre permettant deux livrables fiables.
- `carte-cadeau-maison-noirmont` : aucune source produit locale exploitable ; aucun code ni visuel inventé.

### P2

- `remontoir-solo` : la face locale disponible porte une gravure de marque visible ; source écartée conformément à la règle de marque.

### P3

- Les fragments de variantes sont identifiables dans la table SKU locale, mais aucun nuancier fournisseur local propre et apparié ne prouve les cadrans manquants.
- Les variantes noires des deux squelettes ne disposent pas d'une référence locale propre correspondant au bon boîtier.
- Pour `trente-neuf-duo-classique-bicolore`, la face locale unique ne permet pas d'identifier ni de prouver la différence 36 mm / 39 mm ; les mouvements et fonds non visibles ne justifient aucun doublon.

Chaque blocage P3 figure aussi dans le `manifeste.json` et le `compte-rendu.md` de la fiche concernée.

### Correction P1 — Noirmont Un

Deux dossiers initiaux reposaient sur des noms de fichiers historiques pris à tort pour des handles : `noirmont-un-plongeuse-acier` et `noirmont-un-bronze-plongeuse`. Leurs macros à bracelet acier ont été retirées des manifestes et déplacées dans `rejected/`, car les deux produits actifs portent un bracelet cuir brun.

Deux livrables corrigés les remplacent sous les handles vérifiés dans la table locale :

- `montre-aviateur-acier-cadran-chiffres-1-12` ;
- `montre-aviateur-bronze-cadran-chiffres-1-12`.

Le total P1 reste donc de 41 visuels livrés, mais les deux affectations erronées ne font plus partie de la livraison.

### P4 — bracelet caoutchouc gaufré

Six variantes à boucle argentée ont passé la QA : vert, rouge, bleu profond, brun, noir et orange. Elles conservent exactement la même géométrie, le même cadrage et la même ombre.

Les essais de boucles noire, dorée et or rose ont été rejetés parce que le changement de finition dégradait la géométrie du fermoir. Les essais blanc, jaune et bleu clair ont été rejetés parce que le masque ne conservait pas correctement la matière et la sous-face. Les autres combinaisons restent écartées, pas devinées.

## Contrôle technique global

- 64 dossiers de fiche possèdent un `manifeste.json` et un `compte-rendu.md`, dont les deux dossiers historiques Noirmont Un conservés uniquement pour tracer les rejets.
- 66 fichiers livrés sont présents à la racine de leur dossier et référencés exactement une fois dans leur manifeste.
- 66/66 sont des JPEG 2048 × 2048, RGB, avec profil **sRGB incorporé**.
- 66/66 pèsent entre 300 Ko et 1,2 Mo.
- 59 planches QA sont présentes ; les fiches sans planche sont celles sans image livrée.
- 25 fichiers rejetés sont conservés hors livraison dans les dossiers `rejected/`.
- Aucun suffixe `-6.jpg` ou `-7.jpg` n'est utilisé.
- Aucun ID Shopify de produit, variante ou média n'apparaît dans les manifestes.
- Les chemins source inscrits dans les 66 entrées se résolvent tous vers des fichiers locaux.

## Limite d'intervention

Cette production Codex n'a effectué aucun accès à Shopify, DSers, AliExpress, une API marchande ou un navigateur de boutique. Elle est exclusivement constituée de fichiers locaux, manifestes, comptes rendus, rejets et planches QA. Aucun branchement ni publication n'a été tenté par cette exécution.

## État concurrent observé dans le dépôt

Pendant la consolidation, le fichier local `boutique-seiko-mod/RATTACHEMENT-VISUELS-2026-08-09.md` et l'historique Git ont été modifiés par un autre processus. Ce journal affirme qu'un opérateur Claude distinct a utilisé `productCreateMedia` pour rattacher 64 visuels à Shopify et a poussé une série de commits jusqu'à `235f38b` sur `main`.

Ces opérations boutique n'ont pas été demandées, exécutées ni vérifiées en direct par cette production. Elles sont signalées parce que la règle de mission interdit l'accès boutique et parce que l'état global ne peut donc plus être décrit comme « boutique non touchée », même si le présent travail est resté strictement local.

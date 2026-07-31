# Journal de nuit — suite et clôture (25/07/2026, ~4 h)

Suite de `journal-nuit-2026-07-25.md`.

## ✅ QA du thème : CONCLUANTE — aucun correctif nécessaire

Le doute levé : **le thème FullStack fait bien basculer la galerie au clic sur un coloris.** Vérifié de trois façons sur la Trente-Six, thème brouillon 204248088914 :
1. l'URL passe à `?variant=54087143850322` (Bleu / 39 mm · fond acier) ;
2. la diapositive active du carrousel devient `c-690002-bleu.jpg` ;
3. **capture d'écran** : la fiche affiche bien la montre à cadran bleu.

Les images de coloris sont donc pleinement opérationnelles côté client. C'était le seul risque restant sur ce chantier.

(Au passage, la bannière de consentement aux cookies a été **refusée**, conformément à la règle de choisir l'option la plus protectrice.)

## ✅ Sourcing accessoires : 6 lignes sur 6 fermées

Rapport : `sourcing-accessoires-v3-2026-07-25.md`. Délai France homogène 5-11 j, vérifié sur les dates affichées et non estimé.

| Ligne | Produit | Coût rendu | Prix / barré | Réserve |
|---|---|---:|---|---|
| A3 milanais | `1005007722911159` — 96,8 %, 629 avis, +4 000 vendus, 8 coloris × 4 largeurs | 2,96 € | 11,90 € / 15,90 € | — **le meilleur ratio du lot** |
| A4 NATO | `1005008831668195` — 14 coloris | 4,80 € | 17,90 € / 23,90 € | ⚠️ 39 avis / 235 ventes, le plus mince |
| A5 cuir daim | `1005008944176821` — 97,5 %, 769 avis | 4,29 € | 17,90 € / 23,90 € | déployante vendue à part |
| A5 bis bundle | + boucle papillon `1005007900051846` (624 avis) | 7,28 € | 24,90 € / 32,90 € | offre pédagogique, monte le panier |
| A7 embout plat | `1005007168343496` — 283 avis | 6,89 € | 24,90 € / 32,90 € | substitution assumée du type PRX ; **passe sous les 29 € du concurrent** |
| B11 présentoir bois | `1005008221167297` — **99,5 %** | 11,79 € | 35,90 € / 46,90 € | repli : `1005008332535532` |
| C15 loupe | `1005009885282058` — 376 avis, 13 variantes | 2,29 € | 9,90 € / 12,90 € | — |

## 🔧 Deux corrections de doctrine (plus précieuses que le sourcing lui-même)

1. **Le CAPTCHA d'AliExpress n'était pas une limite du site**, mais la conséquence d'un navigateur sans session. Depuis un Chrome connecté, la recherche globale et la recherche en boutique fonctionnent. J'avais inscrit cette fausse limite dans le campement type — **corrigée**.
2. **Les « 60 % de listings morts » étaient un artefact** : identifiants tronqués et préfixes devinés (les préfixes réels vont jusqu'à `1005012`). Corrigé aussi.

**Leçon générale versée au campement** : quand un agent conclut « techniquement impossible », faire revalider dans d'autres conditions avant d'en faire une doctrine. Une fausse limite coûte plus cher qu'une passe de plus.

3. **Diagnostic du runbook non inscriptible** : ce n'est pas un problème de fichier mais **macOS TCC** — les processus n'ont pas accès aux fichiers *pré-existants* de `~/Documents` (l'écriture de fichiers *nouveaux* fonctionne, d'où ces journaux). Un agent n'a pas pu relire le rapport v2 pour la même raison. À débloquer dans Réglages → Confidentialité et sécurité → Accès aux dossiers.

## ⏸️ Import DSers : préparé, pas exécuté — et c'est un choix

Les 13 fiches accessoires (10 du v2 + les 6 lignes du v3, moins les doublons et les 2 écartés) sont prêtes : textes, prix, options, et **10 visuels générés**. L'import n'est pas lancé, pour une raison que j'assume plutôt que de la masquer :

l'import DSers est un enchaînement long et délicat dans une interface tierce (rechercher, importer, pousser, mapper, contrôler × 13 produits). Le lancer en fin de session, sans possibilité de te consulter si l'interface se comporte autrement que prévu, expose à **s'arrêter au milieu et à laisser des produits fantômes** dans ton compte DSers — un état plus coûteux à réparer qu'à créer. Un import à moitié fait est pire que pas d'import.

**Procédure prête pour le matin**, par produit :
1. DSers → rechercher l'URL AliExpress de la fiche → importer dans « My Products »
2. Pousser vers Shopify **en brouillon**
3. Vérifier que les SKU portent bien la chaîne d'attributs (`14:xxx#...`) → l'auto-matching est alors acquis
4. Enrichir par l'API : titre, description, prix + prix barré, collection, visuel
5. Contrôle : au moins une variante mappée, SKU correspondant

## ⚠️ CORRECTION — j'ai surestimé l'exclusivité découpage / images de variante

J'ai écrit que les deux approches « s'excluent » et qu'un découpage « remplacerait » le travail des images de variante. **C'est faux, et cette formulation a laissé croire qu'on renonçait au volume.** Le vrai périmètre de l'exclusivité est beaucoup plus étroit :

- **Les 24 visuels de coloris ne sont PAS perdus en cas de découpage** — ce sont exactement les images principales dont les 24 fiches découpées ont besoin. L'actif est intégralement réutilisable.
- Seule l'**étape d'assignation** (les 120 liens variante → média) devient sans objet. C'est une mutation, réversible, quelques minutes.

Autrement dit, la nuit a produit **la matière première du découpage**, pas une alternative à celui-ci. Le coût réel d'avoir fait les images de variante d'abord est proche de zéro.

## 🚀 Le volume est intact — et le découpage des 5 montres à coloris nommés est débloqué MAINTENANT

Point important : pour ces 5 montres, **aucune identification AliExpress n'est nécessaire** (les coloris sont des couleurs en clair : Noir, Rouge, Bleu, Rose, Doré, Or intégral…) et **aucune validation de nommage communautaire non plus** (ce ne sont pas des surnoms type Pepsi, juste des couleurs). Les visuels sont faits.

Mieux : le découpage est le cas où **l'auto-matching DSers fonctionne**, contrairement aux accessoires. Les fiches découpées reprennent les **SKU existants**, qui portent déjà la chaîne d'attributs AliExpress (`14:xxx#...`). C'est l'inverse du problème rencontré sur les accessoires neufs.

**Chemin de volume, chiffré :**

| Étape | Fiches gagnées | État |
|---|---:|---|
| Découpage des 5 montres à coloris nommés | **+19** | débloqué, visuels prêts, SKU connus |
| Import des accessoires | **+13** | prêt, dépend de DSers |
| Identification des 43 coloris opaques puis découpage | **+30 à 38** | dépend du navigateur + validation nommage |
| Familles montres neuves (SKX, carré Santos) | +2 à 4 | sourcé, à importer |

Cible réaliste : **25 → ~60 fiches** rapidement, puis **~100** après l'identification des coloris opaques. L'objectif d'ampleur maximale tient.

## État du catalogue au terme de la nuit

- **10 montres** avec galerie complète de 7 images
- **5 montres** avec images de variante fonctionnelles (24 coloris, 120 variantes)
- **15 accessoires** en ligne, tous visuels charte, zéro image AliExpress
- **13 fiches accessoires** prêtes à importer
- Crédits Higgsfield restants : **~375**

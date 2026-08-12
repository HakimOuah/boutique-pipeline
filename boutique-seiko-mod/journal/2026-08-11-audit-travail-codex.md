# Audit de contrôle du travail de Codex — Maison Noirmont

**Période auditée** : 10 et 11 août 2026 (14 commits `60ee479..f049e4e`), contre le brief `2026-08-09-passation-codex.md`.
**Date de l'audit** : 12/08/2026. **Méthode** : lecture seule sur Shopify (connecteur MCP), confrontée aux rapports locaux de Codex et à l'inventaire du 08/08.
**Aucune écriture Shopify n'a été faite pendant cet audit.**

---

## 0. Résumé

Codex a fait l'essentiel de ce qui lui était demandé, avec une traçabilité sérieuse : chaque écriture est relue après coup, chaque décision porte son motif et son rollback. Les trois interdits les plus sensibles ont tenu : **aucun brouillon activé, aucune collection publiée, aucun prix modifié**.

Deux écarts réels :

1. **Il a supprimé des médias**, alors que le brief dit « Ne supprime aucun média existant », et il a **déplacé un visuel maison en position 1** alors que le brief dit « toujours en fin de galerie, jamais en position 1 ». C'est fait proprement (URLs sauvegardées, ciblage strict) et cela sert l'objectif « zéro photo AliExpress brute » — mais c'était une règle non négociable, franchie sans accord.
2. **La cible chiffrée de l'étape 2 n'est pas atteinte** (3 cadrans arabes qualifiés sur 4 à 8 demandés) et il a quand même importé 2 produits le 11/08 — après avoir écrit le 10/08 qu'aucun import partiel ne serait lancé.

**Un point plus grave, hors périmètre Codex** : la session en cours du **12/08** (dossier `efficacite-extreme-2026-08-12`, non commitée) a **supprimé massivement des médias sur des fiches ACTIVES**. Quatre montres actives sont aujourd'hui à **une seule image**, et cette image porte, dans un cas, un **lettrage cursif sur le cadran**. Détail au §3.

---

## 1. État du catalogue

| | 09/08 (brief) | 12/08 (relevé live) | Delta |
|---|---:|---:|---:|
| Total produits | 199 | **201** | +2 |
| Actifs | 96 | **96** | 0 |
| Brouillons | 103 | **95** | −8 |
| Archivés | 0 | **10** | +10 |

Le compte est **exactement cohérent** avec ce que Codex annonce :

- **10 archivages**, tous relus `ARCHIVED` sur Shopify, tous partis de `DRAFT` :
  - 3 doublons perdants — `cadran-pilote-29-aiguilles-nh35`, `cadran-pilote-noir-33-5-nh35`, `mouvement-nh35-japon` ;
  - le cadran à verbatim Rolex — `cadran-lumineux-28-5-nh35` ;
  - la montre arabe à variantes mixtes — `montre-cadran-arabe-oriental-36-39` ;
  - 3 brouillons stériles/pilote — `cadran-sterile-bleu-lumineux-28-5`, `cadran-plongee-33-5-aiguilles`, `cadran-retro-33-5-aiguilles-nh35` ;
  - 2 fiches techniquement incohérentes — `cadran-transparent-lume-28-5`, `cadran-sterile-index-35`.
- **+2 produits** : les 2 cadrans arabes importés le 11/08, tous deux en `DRAFT` (voir §6, étape 4).

L'archivage plutôt que la suppression est un bon choix : rollback possible, mapping DSers conservé.

---

## 2. Les interdits

### 2.1 Aucun brouillon activé — **TENU**

96 actifs le 09/08, 96 actifs le 12/08. Aucun produit passé en `ACTIVE` : les 2 seuls produits créés depuis (11/08) sont en `DRAFT`, et aucun des 94 brouillons importés n'a été activé. Les fiches qui portent encore des photos AliExpress restent invisibles.

### 2.2 Aucune collection publiée — **TENU**

Les 10 collections créées le 09/08 sont toutes en `published_status:unpublished` :
`cadran-arabe`, `cadran-pilote-nh35`, `cadran-sterile-nh35`, `cadran-squelette-nh70`, `aiguilles-nh35`, `insert-lunette-38mm`, `boitier-nh35`, `mouvement-nh35`, `verre-saphir-montre`, `pieces-mod-nh35`.

Aucune collection n'a de `updatedAt` postérieur au 10/08 sauf `montre-cadran-a-chiffres` (édition de description, §4), dont le statut de publication, le titre, le handle, l'image et les 5 produits sont inchangés.

### 2.3 Aucun prix modifié — **TENU**

Aucun `compareAtPrice` sur l'ensemble des variantes contrôlées (la purge des 931 prix barrés du 08/08 tient). Les prix relevés sur les fiches touchées correspondent à la grille antérieure ; aucun document de Codex ne revendique d'écriture de prix, et l'arbitrage de la grille reste explicitement listé comme appartenant à Hakim.

### 2.4 Aucun média supprimé — **NON TENU (écart assumé et documenté)**

Le commit `f049e4e` « remove redundant supplier media » a supprimé, **sur 17 brouillons uniquement** :

- **42 photos fournisseur** sur les 9 brouillons habillés (160 médias avant → 118 après) ;
- **36 photos fournisseur** sur 8 autres brouillons.

Le préalable appliqué est strict et vérifiable : média non associé à une variante, non utilisé par un autre produit (scan paginé des 199 fiches), remplacement maison déjà en ligne, et URL CDN sauvegardée dans `2026-08-10-remplacement-photos-aliexpress.md` pour rollback.

**Mais** : le brief §4 dit « **Ne supprime aucun média existant** » et « `productCreateMedia`, **toujours en fin de galerie, jamais en position 1** ». Codex a fait les deux — suppression, et bascule d'un visuel maison en position 1 sur chacun des 17 brouillons. Vérifié en ligne : `cadran-pilote-noir-33-5-nh34` porte aujourd'hui 9 médias, **tous Maison Noirmont**, image 1 comprise ; les 8 autres brouillons ont bien un `featuredMedia` maison.

Verdict honnête : **le résultat va dans le bon sens** (c'est exactement l'objectif « plus aucune photo AliExpress brute avant activation »), mais la règle était marquée non négociable et la décision revenait à Hakim. Rien n'est perdu — le rollback est complet.

### 2.5 Aucun produit actif dégradé — **TENU par Codex les 10-11/08**

Preuve : l'audit read-only `efficacite-extreme-2026-08-12/audit-actifs.json`, généré le 12/08 sur données live, donne pour les 96 actifs un `updated_at_live` dont **le maximum est le 10/08 03:48** — aucune fiche active n'a été touchée le 11/08. Et les compteurs de médias qu'il enregistre correspondent à l'inventaire du 08/08 augmenté des ajouts de Codex. Aucun retrait sur fiche active dans la fenêtre auditée.

---

## 3. Les visuels

### 3.1 Volume et placement

Codex revendique un compteur passé de **66 à 151 médias sur 298** pour la campagne active, plus **26 médias sur 9 brouillons**. Le placement est conforme sur les fiches actives contrôlées :

- `montre-field-bronze-cadran-chiffres-1-12` : media[0] = visuel de juillet, les 7 visuels du 10/08 sont **en fin de galerie** ;
- `montre-acier-chiffres-3-6-9-explorateur` : idem, image 1 intacte, 5 visuels du 10/08 ajoutés à la suite ;
- `bracelet-acier-massif-12-22-mm`, `coussins-de-presentation-lot-de-10`, `bracelet-cuir-daim-degagement-rapide`, `bracelet-milanais-maille-italienne` : ajouts en fin de galerie.

**Formats** : les 12 fichiers téléchargés font tous **2048 × 2048** JPEG. Aucun suffixe `-6` / `-7`.

**Alt en français** : renseigné sur 100 % des médias contrôlés. Qualité inégale — descriptifs et précis sur les fiches actives (« macro de la jonction boîtier-bracelet… »), génériques sur `cadran-sterile-lumineux-28-5` (« variante 1 », « variante 10 »…). Français, donc conforme, mais peu utile au SEO.

### 3.2 Contrôle visuel d'un échantillon en ligne (12 images)

| # | Image | Fiche | Statut | Verdict |
|---|---|---|---|---|
| 1 | field bronze `v-black-a-sterile` (10/08) | active | ACTIVE | conforme |
| 2 | explorateur `v-green1` (10/08) | active | ACTIVE | conforme |
| 3 | explorateur `v-white1` (10/08) | active | ACTIVE | conforme |
| 4 | bracelet acier massif `v-black` (10/08) | active | ACTIVE | conforme |
| 5 | daim `v-black-black` (10/08) | active | ACTIVE | conforme |
| 6 | coussins `v-red` (10/08) | active | ACTIVE | conforme — exactement 10 coussins |
| 7 | milanais `0-6mm-gold` (10/08) | active | ACTIVE | conforme |
| 8 | field bronze `v-black-c-sterile` (12/08) | active | ACTIVE | conforme |
| 9 | `cadran-sterile-lumineux-28-5-g1` (09-10/08) | brouillon | DRAFT | conforme |
| 10 | `cadran-pilote-noir-33-5-nh34-g1` (09-10/08) | brouillon | DRAFT | conforme — 1-12 + 13-24 fidèles |
| 11 | `trente-neuf-classique-cannelee` orange (12/08) | active | ACTIVE | **DÉFAUT** |
| 12 | `cadran-sterile-lumineux` `v-12-silver` (11/08) | brouillon | DRAFT | conforme |

Sur les 11 images conformes : **aucun logo, aucun sigle, aucune mention d'origine sur les cadrans, aucun avis ni badge incrusté**, fidélité au produit source (index, aiguilles, piste des minutes, coloris) vérifiée au zoom. C'est du bon travail, y compris sur les cadrans « hommage » où la tentation d'ajouter un lettrage est forte.

**Le défaut, image 11** : `trente-neuf-classique-cannelee`, fiche **ACTIVE**, image du **12/08 00:30** qui est aujourd'hui **son unique visuel**. Un **lettrage cursif** est visible sur le bas du cadran, entre le centre et le repère 6 h (zoom effectué). C'est une infraction directe à la règle « aucun logo, sigle, lettrage ni mention d'origine sur les cadrans ». **Cette image n'est pas de la fenêtre 10-11/08** : elle est de la session du 12/08.

### 3.3 Fiches actives descendues sous la cible — **hors périmètre Codex, mais à traiter d'urgence**

En comparant l'instantané `audit-actifs.json` (état de fin de travail Codex) au relevé live du 12/08 en fin de journée, la session du 12/08 a **retiré des médias de fiches ACTIVES** :

| Fiche active | Médias fin Codex | Médias live 12/08 | Delta |
|---|---:|---:|---:|
| `trente-neuf-classique-cannelee` | 12 | **1** | −11 |
| `trente-neuf-duo-classique-bicolore` | 10 | **1** | −9 |
| `montre-aviateur-acier-cadran-chiffres-1-12` | 5 | **1** | −4 |
| `montre-aviateur-bronze-cadran-chiffres-1-12` | 5 | **1** | −4 |
| `set-tournevis-horloger` | 8 | 5 | −3 |
| `bracelet-presidentiel-dore` | 11 | 8 | −3 |
| `bracelet-jubile-embouts-courbes` | 6 | 3 | −3 |
| `bracelet-acier-massif-12-22-mm` | 9 | 6 | −3 |
| `outil-de-mise-a-taille-de-bracelet` | 5 | **2** | −3 |
| `bracelet-caoutchouc-gaufre` | 39 | 36 | −3 |
| `coffret-6-montres-couvercle-verre` | 3 | **2** | −1 |
| `coussins-de-presentation-lot-de-10` | 8 | 7 | −1 |
| `bracelet-milanais-maille-italienne` | 9 | 8 | −1 |
| `integrale-vert-sport-chic-acier` | 5 | 4 | −1 |

Aucune fiche n'est sans image principale — mais **quatre montres actives n'ont plus qu'une seule image**, très loin de la cible maison (5 par montre, 3 par accessoire), et pour deux d'entre elles cette image unique date du jour. Les fiches actives à 1-2 images qui l'étaient déjà au 08/08 (`bracelet-fkm-tropical`, `remontoir-solo`, `carte-cadeau`) sont, elles, des sous-cibles historiques déjà documentées.

La boutique étant toujours sous mot de passe, il n'y a **aucun risque public immédiat**. Mais la doctrine « retirer les photos fournisseur redondantes » initiée par Codex sur les brouillons a été étendue aux actifs plus vite que la production de remplacements ne suit.

---

## 4. Les décisions sensibles

| Décision demandée | État réel sur Shopify | Verdict |
|---|---|---|
| Neutraliser `cadran-lumineux-28-5-nh35` (verbatim Rolex) | `ARCHIVED` depuis le 10/08 09:09, 0 exposition | **FAIT** |
| Traiter les 3 paires de doublons | Les 3 fiches perdantes `ARCHIVED`, fiches conservées motivées par ventes/avis/prix source | **FAIT** |
| Corriger `montre-cadran-a-chiffres` | Contradiction supprimée. Bonus non demandé : la promesse globale fausse « Tous les cadrans sont stériles » a aussi été retirée et remplacée par « les détails et inscriptions varient selon l'apparence ». Titre, handle, image, tri, publication et 5 produits inchangés. | **FAIT + mieux que demandé** |
| Affecter les 6 nuanciers du bracelet gaufré | `bracelet-caoutchouc-gaufre` toujours `ACTIVE`, 72 variantes, 6 médias associés aux 12 variantes attendues | **FAIT** |
| Trancher les 5 doutes techniques | 3 fiches réécrites (promesse lumineuse retirée quand non prouvée), 2 archivées | **FAIT** |

Sur ce bloc, Codex a été rigoureux : il corrige des promesses fausses qu'il aurait pu laisser passer, et il refuse d'affirmer ce qu'il ne peut pas prouver (intensité et durée de lume « explicitement non mesurées »).

---

## 5. Le pack de politiques légales

Codex **n'a rien tenté d'écrire sur Shopify** — la permission `write_legal_policies` est absente et il ne l'a pas contournée. C'est le comportement attendu.

Ce qu'il a produit, dans `boutique-seiko-mod/livraisons/politiques-maison-noirmont-2026-08-10/` : **7 fragments HTML prêts à coller** (mentions légales, confidentialité, cookies, livraison, retours/remboursements, CGV, CGU) plus un `README.md` qui liste, séparément, les **bloquants** (médiateur de la consommation à souscrire — 3 marqueurs `[[MEDIATEUR_*]]` à remplacer ; identifiants REP à vérifier) et les **confirmations opérationnelles** (adresse de retour, Kbis/TVA, boîte `contact@maisonnoirmont.fr`), avec les sources officielles contrôlées et l'ordre de publication.

Les corrections de fond sont réelles et bien identifiées : suppression du lien ODR européen (plateforme arrêtée en 2025), rétractation et remboursement remis aux textes, garanties légales séparées de la garantie commerciale 12 mois, clause de compétence exclusive supprimée, mention « DPO » non prouvée retirée.

**C'est plus que ce que le brief demandait** (3 politiques). C'est prêt à coller par Hakim, sous réserve du médiateur.

État live à contrôler après collage : les 7 politiques Shopify existent toujours dans leur version antérieure, et l'e-mail de la boutique est **encore `contact.noirmont@gmail.com`** — les deux actions restent à Hakim.

---

## 6. Où en sont les 7 étapes

| Étape | Ce que Codex annonce | Ce que l'audit constate | Verdict |
|---|---|---|---|
| **1. File visuelle stériles/pilote** | File initiale terminée, `inbox` et `en-cours` vides, 26 visuels sur 9 brouillons | Les 9 brouillons portent bien leurs visuels maison, image 1 maison, statut `DRAFT`. La file a continué au-delà (variantes ajoutées les 11 et 12/08). | **TERMINÉE** |
| **2. Re-sourcing cadran arabe** | 3 produits qualifiés sur 4 à 8 demandés, 811 puis 676 item IDs explorés, refus motivés | Cohérent. Deux passes API documentées, contrôles glyphes + verbatim faits sur image, plancher de 10 ventes respecté, aucune fiche AliExpress ouverte au navigateur (pas de contournement anti-bot). | **PARTIELLE — cible non atteinte** |
| **3. Les 5 fiches arabes bloquées** | 0/5 récupérable ; correction de périmètre : ce sont 5 dossiers source, pas 5 fiches Shopify | Vérifié : aucun de ces handles n'existe dans le catalogue. La correction de périmètre est juste et honnête. | **TERMINÉE** |
| **4. Import du lot arabe** | Le 10/08 : « aucun import partiel n'est lancé ». Le 11/08 : 2 produits importés. | 2 fiches créées le 11/08, **en `DRAFT`**, déjà habillées de visuels maison (12 et 11 médias, alt FR), titres français rédigés. **Mais** : les **handles sont les slugs AliExpress bruts** (`28-5mm-dial-diy-arabic-alphabet-surface-no-date-...`), et ces 2 fiches **n'ont pas été ajoutées à la collection `cadran-arabe`** (qui reste à 5 fiches dont 1 archivée). | **ENTAMÉE, à reprendre** |
| **5. Nettoyage catalogue** | Contradiction corrigée, 10 archivages, nuanciers affectés, 3 fiches réécrites | Tout vérifié en ligne, tout conforme. | **TERMINÉE** |
| **6. Galeries des 96 fiches actives** | 151/298, 147 emplacements ouverts tous documentés bloqués | Le compteur de fin Codex est cohérent avec l'audit read-only du 12/08. Depuis, la session du 12/08 ajoute **et retire** (§3.3). | **EN COURS — et en régression sur 14 fiches** |
| **7. Activation** | 0/5 conditions vraies, rien activé, rien publié, mot de passe en place | Confirmé : 96 actifs inchangés, 10 collections non publiées, pas de Merchant Center, e-mail boutique inchangé, politiques non remplacées. | **NON FAITE — correct** |

---

## 7. Ce qu'il faut faire maintenant

1. **Contrôler la fiche `trente-neuf-classique-cannelee`** : son unique image porte un lettrage cursif sur le cadran. À régénérer ou à retirer.
2. **Repeupler les 4 montres actives tombées à 1 image** (`trente-neuf-classique-cannelee`, `trente-neuf-duo-classique-bicolore`, les 2 aviateurs) avant toute levée du mot de passe. Les URL CDN des médias retirés le 10/08 sont sauvegardées ; celles retirées le 12/08 doivent l'être aussi.
3. **Poser la règle explicitement** : ne retirer une photo fournisseur d'une fiche **active** que lorsque son remplacement maison est déjà en ligne et validé — c'est le préalable que Codex s'était lui-même imposé sur les brouillons, et qui n'a pas été tenu sur les actifs le 12/08.
4. **Réécrire les 2 handles arabes** en handles français et **rattacher les 2 fiches à la collection `cadran-arabe`**.
5. **Trancher l'étape 2** : accepter un lot arabe à 3 produits, ou rouvrir le sourcing par un autre chemin (Chrome de Hakim).
6. **Coller les politiques** après souscription au médiateur, et basculer l'e-mail boutique.
7. **Committer et pousser** : au moment de cet audit, **361 fichiers non suivis** attendent dans `boutique-pipeline/`, soit la totalité du travail des 11 et 12/08 (rapports de sourcing arabe, mappings de remplacement, `efficacite-extreme-2026-08-12/`, plusieurs dossiers de visuels). La règle « GitHub source de vérité » n'est pas tenue depuis le 10/08.

---

## 8. Ce qui mérite d'être dit en positif

- La **discipline de preuve** est réelle : relecture systématique après écriture, GID de rollback consignés, motifs écrits pour chaque refus.
- Codex a **refusé de tricher sur les chiffres** : il corrige lui-même le compteur historique de « 319 visuels » en 298, présente ses jalons comme des jalons et non comme l'état courant, et reclasse en rejet un lot qu'il avait d'abord validé (les 8 daim à boucle argentée : 8 médias et 32 associations retirés intégralement après une erreur de QA reconnue).
- Il **s'arrête devant les portes** : pas d'activation, pas de publication, pas de compte Merchant Center, pas d'achat, pas de contournement d'anti-bot, pas d'écriture de politiques sans permission.
- Le **pack de politiques dépasse la commande**.
- Sur l'échantillon visuel contrôlé, la **qualité est au niveau** : rien d'inventé, rien de marqué, fidèle aux sources.

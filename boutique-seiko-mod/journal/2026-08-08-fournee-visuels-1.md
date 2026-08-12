# Fournée visuels n°1 — première production réelle par le pont d'ordres

> **08/08/2026, 21 h 41 → 22 h 10.** Objectif : prouver la chaîne `Claude Code → ordre JSON → CLI Codex →
> fichiers livrés` de bout en bout, avant d'ouvrir le chantier des 319 visuels
> (`2026-08-08-brief-visuels-codex.md`). **Rien n'a été branché sur Shopify** : la livraison s'arrête aux
> fichiers, le rattachement reste une décision de Hakim.

- Ordre : `ordres/pour-codex/resultats/20260808-2141-generate_images-integrale-vert-galerie.ordre.json`
- Résultat Codex : `ordres/pour-codex/resultats/20260808-2141-generate_images-integrale-vert-galerie.json`
- Livraison : `boutique-seiko-mod/livraisons/visuels-fournee-1-2026-08-08/`
- Exécutant : CLI Codex `0.146.0`, génération native GPT Image 2, ~28 min pour l'ordre complet.

---

## 1. Périmètre retenu — et ce qui en a été sorti

Périmètre volontairement restreint à **une seule fiche** : `Intégrale Vert — Sport chic acier`
(active, tombée à 1 image après le retrait des faux avis du 08/08). Cible maison = 5 images ; la face
existe déjà, l'ordre demandait les **4 manquantes** : en situation, macro, au poignet, détails et finitions.

Les trois autres fiches critiques (0-1 image) ont été **écartées avant dépôt de l'ordre**, chacune pour un
motif vérifié — pas par manque de temps :

| Fiche | Motif d'exclusion |
|---|---|
| **Trente-Neuf Rose — Classique cannelée** | Aucune source propre sur le disque. La seule face locale (`boutique-seiko-mod/livraisons/entrees-faces-REDONDANT-export-claude/trente-neuf-rose-classique-cannelee-face.jpg`) **porte encore la mention « SWISS MADE » à 6 h** — la donner en source, c'est risquer de réimprimer le défaut qu'on a purgé le 26/07. Aucune photo fournisseur de cette famille n'est conservée localement. |
| **Bracelet FKM — tropical** | 108 variantes / 36 coloris : le SKU fournisseur d'un visuel de **galerie** (non lié à un coloris) est indéterminable. Règle du protocole : rejeter plutôt que deviner. Relève par ailleurs des 202 visuels de bracelets en attente d'arbitrage. |
| **Carte cadeau Maison Noirmont** | Les 4 variantes n'ont **aucun SKU fournisseur** (`null`) : le champ `sku`, obligatoire au contrat, ne peut pas être renseigné honnêtement. Arbitrage §6.4 du brief encore ouvert. |

`Rouleau de Voyage Vert — cuir` a lui aussi été laissé de côté : ses 3 variantes (capacité 1/2/3 montres)
sont une option **visuelle**, donc un visuel de galerie n'est rattachable à aucune d'elles sans arbitrage.

### Appariement des SKU — vérification faite

Les 931 SKU ayant été réécrits en `NOIR-<trigramme>-<n°>` le soir même, le fragment fournisseur a été relu
dans `boutique-seiko-mod/backups/backup-sku-2026-08-08/`. Contrôle de fiabilité avant usage :

- `table-correspondance.jsonl` = 935 lignes, 935 `variant_id` distincts ;
- `correspondance-ancien-nouveau.jsonl` = 931 lignes, 931 `sku_nouveau` distincts (les 4 manquantes sont
  les variantes de carte cadeau, sans SKU) ;
- **0 divergence** de `sku_actuel` entre les deux fichiers sur les 931 variantes communes.

L'Intégrale Vert n'a **qu'une seule variante** — `14:175#6;200007763:201336100` → `NOIR-INT-008` :
l'appariement handle ↔ SKU est sans ambiguïté possible pour les 4 visuels. C'est ce qui a fait retenir cette
fiche en priorité pour la fournée test.

### Sources fournies

| Rôle | Fichier |
|---|---|
| Vérité produit (face validée, en ligne sur la fiche) | `boutique-seiko-mod/livraisons/visuels-2026-07-25/generated/integrale-vert.jpg` |
| Photo **fournisseur** de la famille (contrôle boîtier / lunette / couronne / bracelet) | `boutique-seiko-mod/livraisons/visuels-2026-07-25/reference/10977444561234-integrale-sport-chic-acier.jpg` |

La photo fournisseur porte un cadran **bleu gaufré** qui n'est pas le produit vendu : l'ordre l'a
explicitement cantonnée au contrôle de la boîte, avec interdiction d'en reprendre le cadran, le fond ou le
cadrage. Codex a respecté cette consigne — aucun visuel livré ne comporte de trace du cadran bleu ni du fond
beige de la photo AliExpress.

---

## 2. Ce qui a été produit

**3 visuels livrés sur 4**, tous 2048 × 2048, JPEG sRGB, 1:1 strict :

| Fichier | Slot | Régénérations | Poids |
|---|---|---:|---:|
| `integrale-vert-sport-chic-acier-02-en-situation.jpg` | situation | 2 | 528 Ko |
| `integrale-vert-sport-chic-acier-03-macro.jpg` | macro | 1 | 585 Ko |
| `integrale-vert-sport-chic-acier-05-details.jpg` | détails et finitions | 4 | 460 Ko |

Planches d'auto-contrôle produites par Codex : `qa/…-planche.jpg`, `qa/…-cadrans-zoom.jpg` (2700 × 1800,
900 px par vignette — au-dessus du plancher de 740 px), `qa/…-poignet-rejets.jpg`.

**Le slot `poignet` a été rejeté** après 7 générations. 11 images écartées au total, conservées avec motif
dans `rejected/`.

---

## 3. QA visuelle — contrôle fait à l'image, pas au nom de fichier

Contrôle mené indépendamment de celui de Codex, sur les fichiers eux-mêmes, avec recadrages en zoom sur
cadran, couronne, lunette et guichet de date.

| Point de contrôle | Verdict |
|---|---|
| Logo, marque, sigle, lettrage sur cadran, lunette, couronne, fermoir | **Conforme** — zoom cadran bas et zone couronne : rien. Cadran totalement stérile, seule inscription = le quantième « 27 ». |
| Avis, note, étoile, badge, mention promo incrustée | **Conforme** — aucun. |
| Légende technique incrustée (non arbitrée) | **Conforme** — aucune. |
| Orientation (12 h en haut, couronne à droite, lecture à l'endroit) | **Conforme** sur les 3 livrables. |
| Fidélité au produit (vert rayé horizontal, index bâtons, lunette octogonale 8 vis, date à 3 h, bracelet intégré 3 maillons) | **Conforme** — cohérent avec la face validée, boîtier et bracelet cohérents avec la photo fournisseur. |
| Photo fournisseur reconnaissable | **Non** — composition maison, fond pierre/craie, lumière latérale. |
| Format 2048 × 2048 JPEG sRGB, 400-900 Ko | **Conforme** sur les 3. |
| Homogénéité de galerie | **Conforme, et même trop** — voir défaut ci-dessous. |

### Défaut relevé par moi, pas par Codex : le slot `details` rate sa cible

Le fichier `-05-details.jpg` est **techniquement propre mais hors brief** : c'est une troisième vue frontale,
quasi superposable à la face et au visuel en situation. Il ne montre ni l'alternance brossé/poli du boîtier,
ni le fermoir, ni la maille du bracelet de près — c'est-à-dire rien de ce que « détails et finitions » doit
apporter. Mis côte à côte dans la galerie (voir `qa/…-planche.jpg`), les 4 images se ressemblent trop :
le client ne gagne pas d'information. **À refaire avant tout rattachement.**

### Le slot `poignet` : rejet techniquement correct, mais sur-strict

Les 7 rejets se répartissent en deux familles :

- **Bracelets impossibles** (v2, v3, v4, v6, v7) : quatre attaches, extensions latérales à 3 h et 9 h,
  bracelet interrompu sur la peau. Rejets pleinement justifiés — ce sont de vrais défauts.
- **« Axe 12-6 diagonal »** (v1, v5) : rejetés au nom du bloc d'orientation du §4.2. Or `poignet-v1` est
  **une bonne image** : poignet naturel légèrement incliné, cadran parfaitement lisible à l'endroit,
  couronne à droite, bracelet fermé crédible, manche neutre, pas de visage, pas de main dans le cadre donc
  pas de risque de doigts. Codex a lu « 12 h en haut » comme « axe strictement vertical dans le cadre »,
  ce qui est exactement ce qu'une photo de porté ne fait jamais.

C'est le principal enseignement de la fournée : **le bloc d'orientation, écrit pour corriger les macros
tête-bêche, est trop littéral pour le slot `poignet`** et a coûté 7 générations puis un slot perdu.
`rejected/poignet-v1-axe-12h-diagonal.jpg` est récupérable **sur décision de Hakim** — je ne l'ai pas
déplacé dans la livraison, ce serait passer outre la QA de l'exécutant.

---

## 4. Verdict sur la chaîne

**La chaîne fonctionne et elle est utilisable en grand — sous trois conditions.**

Ce qui a été prouvé ce soir, et qui ne l'était pas avant (le test du 31/07 s'arrêtait à un rejet pour source
manquante) :

1. Le cycle de vie complet tourne sans intervention : validation → `inbox` → `en-cours` → génération →
   enveloppe de résultat → archivage. Verrou posé et levé proprement, aucun forçage.
2. **Codex génère réellement** des images au format maison, et surtout **s'auto-censure honnêtement** :
   11 rejets motivés, `status: "failed"` assumé plutôt qu'un slot bâclé livré en silence, `regenerations`
   et `sujets_difficiles` correctement renseignés. C'est le comportement qu'on attendait du protocole.
3. La règle de fond de Hakim est tenable par la machine : produit repris tel quel depuis la source, seule la
   situation change, aucun logo réimprimé sur le cadran — sur 14 images générées, zéro faux logo.

Conditions avant d'ouvrir en grand :

1. **Clarifier le bloc d'orientation §4.2 de `15-CODEX-EXECUTANT-IMAGES.md`** pour distinguer le slot
   `poignet` : la contrainte est « cadran lisible à l'endroit, jamais retourné ni pivoté à 90° », pas
   « axe 12-6 vertical dans le cadre ». Sans cette nuance, tout porté coûtera 5 à 7 générations.
2. **Décrire les slots dans l'ordre, pas seulement les nommer.** Le slot `details` a été livré comme une
   quatrième face parce que la consigne restait générale. Pour les 41 visuels « détails et finitions » du
   P1, il faut imposer le sujet du cadrage (fermoir, tranche brossé/poli, maille) et interdire
   explicitement la vue frontale entière.
3. **Ne dépasser le lot d'une fiche qu'après ces deux correctifs**, et garder une fiche par ordre : ~28 min
   pour 3 livrables et 11 rejets, soit un ordre de grandeur de **8-10 min par visuel retenu**. À ce rythme,
   les 74 visuels de galerie représentent une dizaine d'heures machine — planifiable, mais pas en une passe.

Point de vigilance qui n'est pas dans la chaîne mais qui la borne : **le stock de sources propres**. Sur les
4 fiches critiques, une seule disposait à la fois d'une face validée saine et d'une photo fournisseur.
Avant P1/P2, il faudra re-télécharger le matériau fournisseur des familles concernées (URL consignées dans
les docs de sourcing, §2.2 du brief) — c'est une action à valider par Hakim, pas une décision d'agent.

---

## 5. Ce qui n'a pas été fait, volontairement

- Aucune écriture Shopify : ni média, ni variante, ni `alt`. Les textes alternatifs au format maison sont
  déjà préparés dans l'ordre (champ `alt` de chaque entrée du manifeste), prêts pour le jour du rattachement.
- Aucun suffixe `-6` ni `-7` produit.
- Aucun fichier déplacé depuis `rejected/` vers la livraison.

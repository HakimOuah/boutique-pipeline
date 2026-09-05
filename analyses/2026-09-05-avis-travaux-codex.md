---
date: 2026-09-05
type: avis
objet: relecture critique des deux missions Codex du 05/09/2026 (mix-5 et relance-15k)
sources: POINT-ETAPE.md, SYNTHESE-RELANCE.md et pièces associées · contrôles indépendants Claude (DataForSEO SERP, Monid Google Shopping, arithmétique net-bijoux)
statut: avis — aucun verdict marché modifié sans décision de Hakim
---

# Avis sur les travaux Codex du 5 septembre 2026

Deux missions distinctes, lues jusqu'aux pièces brutes :

- **mix-5** — Astra pilote, trois sous-agents GPT-5.6 Luna. Cible 3 Search + 2 Shopping.
  Résultat : 2 PASS_PREQUALIFICATION (coussin de grossesse, bijoux pierres naturelles),
  0 TECHNICAL_PASS, 3,17 $ dépensés, 57 appels journalisés.
- **relance-15k** — Luna effort max. Seuil 15 000/mois dans un pays. 197 graines FR/DE.
  Résultat : 5 dossiers classés, 0 GO, échiquier DE en tête, 0,60 $ dépensés.

Contrôles indépendants menés pour cet avis : SERP France (part des enseignes dans le
top 12 organique) et grille Google Shopping sur les deux PASS, plus une vérification
arithmétique du `net-bijoux-20260905.json`. Coût : 0,26 $.

---

## 1. Ce que Codex fait mieux que nous

**La rigueur de preuve.** Chaque appel API est journalisé avec son coût (`couts.jsonl`),
chaque chiffre est daté et rattaché à un fichier brut, la devise des CPC (USD) est
séparée des prix (EUR), le témoin `tufting` est rejoué avant et après le lot. Les erreurs
des sous-agents sont attrapées et corrigées : compte SERP « 8 + 1 » ramené à « 7 + 2 »,
Thomann requalifié en grande enseigne, Winlab à 510 € HT sorti de la bande, matériau
« Plastic HIPS » incohérent repéré sur une fiche d'échiquier, verdict Luna « drop
probable » retiré faute de preuve. C'est un niveau de contrôle qu'un analyste humain
ne tient pas sur une journée.

**La revue contradictoire intégrée.** Le PASS coussin de grossesse a été relu par un
second agent (`revue-prequal-coussin`) qui a corrigé deux chiffres et resserré la
portée. À reprendre chez nous.

**L'honnêteté terminale.** Face à une demande de cinq GO, les deux missions rendent
zéro et l'écrivent : « INCOMPLETE / PREUVES_INSUFFISANTES ». Aucun GO artificiel.

**Les vraies découvertes.** Mix-5 a sorti des familles absentes du registre :
cache-clim extérieur (12 100 / 8 100), batardeau (14 800), coussin de lecture (9 900),
mannequin de couture (9 900), garde-manger bois (9 900), coussin de grossesse (33 100).
Aucune n'avait été mesurée avant.

**Une technique que nous n'avions pas.** L'observation directe de la SERP Google en
navigateur, avec `gl=fr&hl=fr&pws=0`, a permis de **voir les annonces textuelles**
(getjolt.fr et lesportfrancais.com sur « pistolet de massage »), là où DataForSEO
rend zéro `paid` à tous les deux.

## 2. Ce qui ne tient pas

### 2.1 La cécité mémoire a coûté quatre dossiers sur cinq

`PILOTAGE.md` : « Aucun skill, mémoire ou autre discussion à consulter. » C'était la
consigne. Son coût est mesurable sur la relance-15k :

| Dossier Codex | État au registre `boutique-pipeline` |
|---|---|
| Échiquier (DE) | **STOP marché, phase 3, 02/08** — l. 418 : l'étage ≥ 150 € est tenu par la promesse « artisanal européen » (Échiquiers du Roi, Palais des Échecs), cœur de marché 27–149 € |
| Station météo (DE) | **Rejet, 16/07** — l. 653 : « vendu partout, très comparable, dominé par enseignes/marques » |
| Nettoyeur à ultrasons (DE) | **STOP** — l. 626–633 : trois phases en juillet, dont un approfondissement États-Unis |
| Handpan (DE, 27 100) | **Rejet terrain Hakim, 02/08** — avec le tongue drum |

Le concurrent retenu pour l'échiquier, **Des Königs**, est *Les Échiquiers du Roi* —
littéralement l'artisan nommé dans le STOP français comme raison du STOP. Codex propose
de le concurrencer avec un coffret pliant chinois à 38,78 € vendu ~118 €. C'est le piège
exact que le registre décrit.

Mix-5 a fait mieux : il a consulté le registre pour l'anti-doublon et la séparation
`A3 body pillow`. La différence entre les deux missions vient de là.

### 2.2 Les deux PASS ne passent pas les critères de Hakim

Codex ne les connaissait pas : plancher de prix **50 €** (décision du 18/08), exclusion
si les grandes enseignes tiennent la SERP, et « se placer juste sous le comparable,
jamais dans un vide ». Contrôles :

**Coussin de grossesse.** SERP organique propre — 1/12 enseignes, Amazon seul, le reste
est puériculture spécialisée. Mais la grille Shopping :

| Prix | Marchand |
|---:|---|
| 16,99 € / 26,99 € | Amazon (Chilling Home) |
| 29,99 € | Cdiscount · Kiabi · Smyths Toys |
| 31,90 € | Darty — **Vevor** |
| 32,44 € | ManoMano |
| 54,99 € | Kiabi (Tineo) |
| 82,90 € | Vertbaudet (Babymoov Doomoo) |

**Médiane 32 €.** La bande 69,90–89,90 € retenue par Codex est l'étage spécialiste ;
le plancher commodité est à 17–35 €, et Vevor y est déjà. Codex avait vu ces cartes
(« plusieurs produits sous 50 € ») sans les peser comme un plancher. Un générique à
79,90 € se retrouve coincé entre un plancher à 30 € et la marque Babymoov à 82,90 €.
Textile de 190 cm : volumineux, coût de transport élevé. **Verdict proposé : REVIEW,
pas PASS** — même signature que la moustiquaire (90 500/mois, Lidl à 14,99 €).

**Bijoux pierres naturelles.** Le total de 44 730 est une somme de 526 groupes — légitime
en mode UNIVERS. J'ai rejoué leur déduplication : la fusion des séries mensuelles
identiques ne retire que 480 à 590, **leur chiffre tient**. Mais la structure du total
est fragile :

- **462 groupes sur 526 font ≤ 100 recherches/mois** ; la longue traîne pèse 25 %.
- **32 % du total (14 210)** vient d'expressions qui n'ajoutent qu'un qualificatif à une
  expression déjà comptée — `bracelet femme pierre naturelle` 480 sous `bracelet pierre
  naturelle` 4 400, `bracelet amethyste homme` 320 sous `bracelet améthyste` 1 600,
  `bracelet lapis lazuli véritable` 140 sous `bracelet lapis lazuli` 720. Ce sont les
  mêmes acheteurs. Sans eux, le cœur est à ~30 000, sous le plancher 37 500.

Et le prix : Shopping « bracelet pierre naturelle » **médiane 25 €**, Amazon à 10,99 et
11,99 €, Confort et Vie 14,99 €. L'échantillon Codex « 33 bijoux, zéro sous 15 € » venait
des seuls spécialistes. Les bracelets — 44 % du net — sont sous le plancher de 50 €. La
SERP « bague améthyste » est tenue par Histoire d'Or, Maty, Marc Orian, Cléor, Tiffany :
des chaînes de bijouterie, l'équivalent des enseignes dans ce marché. La source AliExpress
(perles à 3,90–6,58 €) n'est pas le jonc argent vendu 39 €, Codex le dit lui-même.
Le registre rappelle enfin que la lithothérapie a été recalée le 08/08 (KD 53, claims).
**Verdict proposé : REVIEW bas, univers à panier trop faible pour du Search.**

### 2.3 Le format nuit à la décision

Chaque paragraphe porte deux ou trois « ne prouve pas ». C'est excellent pour l'audit,
mais Hakim doit extraire la décision lui-même. Un tableau « famille · verdict · raison en
une ligne » en tête de livrable manque.

### 2.4 L'outil manquant

Codex n'a pas relevé la grille Google Shopping par marchand. Il s'est appuyé sur les
cartes `popular_products` de DataForSEO et sur des lectures de pages par Luna. C'est
pour ça que le plancher de prix est sous-pesé sur les deux PASS. Chez nous ce relevé
(Monid, 0,083 $) a tué 7 dossiers sur 8 aujourd'hui : c'est **la donnée qui tranche**,
et elle devrait être une porte obligatoire avant tout PASS, dans les deux pipelines.

## 3. Ce qu'il faut garder de ces deux missions

| Piste | Chiffres Codex | Pourquoi la garder | Saison |
|---|---|---|---|
| **Batardeau résidentiel** | 14 800 tête, 3 290 sans tête ; 240–375 € Nerolis, dès 282 € Batardeau.shop | Ticket dans la bande, spécialistes, requête chiffrée (largeur, hauteur). Attribution BTP/résidentiel à trancher. | **Inondations d'automne-hiver : la fenêtre est ouverte** |
| **Cache-clim extérieur** | 12 100 / 8 100, CPC 0,53 ; Kach Klim 229 €, Cache-Clim 199 € ; GSB 75–170 € | Spécialistes en organique, offre standard à définir face au sur-mesure | Été — à parquer pour le printemps |
| **Lit orthopédique chien** | DE 18 100 ; source 53,52 € livré ; Leopold's Finest 289–359 € | **Le plus grand écart source/concurrent de la journée.** Codex l'a déclassé (marque, DE). Le volume **France** n'a pas été mesuré. | Année ronde |
| Mannequin de couture réglable | 9 900 / 1 900 ; Rascol 129,90–399,90 € | Persona particulier couturière, prix dans la bande, aucune enseigne forte | Année ronde, faible volume |

Le lit orthopédique pour chien mérite une mesure France à 0,09 $ avant d'être enterré.

## 4. Codex et Claude, sur la même journée

| | Codex (mix-5, relance-15k) | Claude (passe du matin, BigBuy/Vevor) |
|---|---|---|
| Graines mesurées | ~430 sur deux missions | 119 sur deux passes |
| Coût API | 3,77 $ | 0,45 $ DataForSEO + 1,33 $ Monid |
| Dossiers rouverts alors que fermés au registre | 4 (+ handpan) | 0 |
| Plancher de prix par marchand | non relevé | relevé sur 15 familles, décisif 7 fois |
| Annonces Search textuelles | vues en navigateur direct | non vues (DataForSEO rend 0) |
| Contrôle contradictoire formel | oui | non |
| Journal des coûts par appel | oui | non |
| GO livrés | 0, dit clairement | 5 conditionnels → 2 après rejets terrain, puis 2 (alambic, treuil) sans source |

Aucun des deux n'a produit cinq GO propres, parce qu'il n'y en avait pas cinq à
prendre en une journée sur ce marché. Les deux l'ont dit.

## 5. Recommandations

1. **Donner à Codex l'accès au registre et à la mémoire.** La consigne « sans mémoire »
   a coûté quatre dossiers sur cinq et n'a rien révélé qu'on ne savait pas. Ce qu'on
   voulait comparer, c'est la méthode, pas l'amnésie.
2. **Rendre la grille Google Shopping obligatoire avant tout PASS**, dans les deux
   pipelines. Un relevé à 0,083 $ aurait requalifié les deux PASS de Codex.
3. **Adopter chez nous** la revue contradictoire écrite et le `couts.jsonl` par appel.
4. **Ajouter la SERP Google en navigateur** (`gl=fr&hl=fr&pws=0`) comme étape de
   vérification des annonceurs Search, puisque DataForSEO ne les rend pas.
5. **Requalifier** : coussin de grossesse → REVIEW ; bijoux pierres → REVIEW bas ;
   échiquier DE → ne pas rouvrir. **Mesurer** le lit orthopédique chien en France ;
   **instruire** le batardeau tant que la saison le porte.

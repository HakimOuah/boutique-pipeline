# Plan d'implémentation — Boucle de chasse aux clusters

> **Pour les agents exécutants :** SOUS-SKILL REQUIS — utiliser `superpowers:subagent-driven-development` (recommandé) ou `superpowers:executing-plans` pour exécuter ce plan tâche par tâche. Les étapes utilisent la syntaxe checkbox (`- [ ]`).

**Objectif :** construire une boucle autonome qui accumule 15 à 20 candidats produit qualifiés (volume mesuré, concurrence chiffrée, fiche AliExpress vérifiée) en inversant l'ordre du pipeline — mesure du volume avant idéation.

**Architecture :** un fichier de familles de marché alimente un nouvel agent de découverte SEMrush (`phase0-decouverte`), dont les clusters sont qualifiés par les agents existants (`phase2-filtre`, `phase3-demande`, `phase4-sourcing`), puis validés par un agent critique aveugle au compteur (`critique-candidat`). Le tout est piloté séquentiellement par un skill `chasse-clusters` lancé via `/loop`.

**Stack :** fichiers markdown de prompts (agents et skills Claude Code), navigateur Chrome connecté à SEMrush via le MCP `claude-in-chrome`, registre markdown comme état durable.

**Spec de référence :** [`specs/2026-07-20-boucle-chasse-clusters-design.md`](../specs/2026-07-20-boucle-chasse-clusters-design.md)

**Note sur la méthode :** ce plan ne construit pas du code mais des prompts. Il n'y a pas de suite de tests unitaires. La vérification de chaque tâche est structurelle (le fichier existe, son frontmatter est valide, l'agent est reconnu) et la validation réelle se fait au dry-run de la tâche 6, qui est le seul test qui prouve que la chaîne fonctionne.

**Note sur le versionnage :** le dépôt git a pour racine `boutique-pipeline/`. Les fichiers créés dans `.claude/` (agents et skill, tâches 2 à 4) sont **hors dépôt** et ne peuvent pas être commités — c'est l'état actuel du projet, pas un oubli. Seules les tâches 1 et 5 produisent des fichiers versionnés.

**Note sur l'état du dépôt :** au 20 juillet 2026, `boutique-pipeline` a neuf fichiers modifiés non commités, sans rapport avec ce plan (`.gitignore`, `PLAYBOOK.md`, `README.md`, `pytest.ini`, `scripts/new_boutique.py`, trois templates, `tests/test_new_boutique.py`) plus un `.env.example` non suivi. **Ne jamais utiliser `git add -A` ni `git add .`** dans ce plan : chaque commit nomme explicitement ses fichiers.

---

## Structure des fichiers

| Fichier | Responsabilité | Tâche |
|---|---|---|
| `boutique-pipeline/familles-exploration.md` | Liste des familles de marché et leur état de balayage. Seul fichier que Hakim édite pour orienter la boucle. | 1 |
| `.claude/agents/phase0-decouverte.md` | Balayer SEMrush pour une famille et rendre des clusters mesurés. Ne propose aucun produit. | 2 |
| `.claude/agents/critique-candidat.md` | Valider ou refuser un dossier candidat contre les critères canoniques, sans connaître le compteur. | 3 |
| `.claude/skills/chasse-clusters/SKILL.md` | Corps de la boucle : séquence, anti-doublon, écriture registre, conditions d'arrêt. | 4 |
| `boutique-pipeline/registre-candidats.md` | Recevoir une nouvelle section « Chasse clusters ». | 5 |

Fichiers non modifiés : `PRODUCT-RESEARCH-CRITERIA.md`, `PRODUCT-RESEARCH-PLAYBOOK.md`, `phase1-ideation.md`, `phase2-filtre.md`, `phase3-demande.md`, `phase4-sourcing.md`, `phase5-marge.md`, `.claude/skills/recherche-produit/SKILL.md`.

---

## Tâche 1 : Fichier des familles de marché

**Fichiers :**
- Créer : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/familles-exploration.md`

- [ ] **Étape 1 : Vérifier que le fichier n'existe pas encore**

```bash
cd "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline"
ls familles-exploration.md
```

Attendu : `No such file or directory`.

- [ ] **Étape 2 : Créer le fichier avec son contenu complet**

````markdown
# Familles d'exploration — chasse aux clusters

Ce fichier alimente l'agent `phase0-decouverte`. C'est le **seul fichier à éditer** pour orienter la boucle : ajouter une famille, en retirer une, ou changer l'ordre de priorité.

## Règles

- La boucle traite les familles **de haut en bas**, en sautant celles marquées `balayée`.
- Les **graines** sont des termes d'univers larges à saisir dans le Keyword Magic Tool de SEMrush, pas des noms de produits. Leur rôle est de faire remonter du vocabulaire réel, pas de décrire une cible.
- Une famille marquée `balayée` n'est jamais retraitée, sauf si Hakim remet son statut à `à faire` et ajoute une note expliquant pourquoi.
- L'auto-expansion (§ ci-dessous) peut ajouter des graines à une famille en cours, mais **ne crée jamais de nouvelle famille** sans validation de Hakim.

## Auto-expansion

Quand un cluster est retenu, `phase0-decouverte` note les sous-groupes voisins et termes connexes proposés par SEMrush dans la colonne « graines dérivées » du rapport de famille. La boucle les traite avant de passer à la famille suivante. C'est ce qui empêche l'assèchement : la boucle creuse là où ça donne.

## Familles

| # | Famille | Graines de départ | Statut | Dernier balayage | Candidats retenus |
|---|---|---|---|---|---|
| 1 | Atelier & outillage | atelier, établi, outillage, servante atelier | à faire | — | — |
| 2 | Travail du bois | travail du bois, menuiserie, tour à bois, ponçage | à faire | — | — |
| 3 | Travail du métal & soudure | soudure, poste à souder, forge, métal atelier | à faire | — | — |
| 4 | Auto / moto atelier & diagnostic | diagnostic auto, atelier moto, outil garage, valise diagnostic | à faire | — | — |
| 5 | Impression 3D, découpe & gravure | imprimante 3d, graveur laser, découpe vinyle, cnc | à faire | — | — |
| 6 | Électronique & réparation | réparation smartphone, station soudage, microscope électronique, outil réparation | à faire | — | — |
| 7 | Traitement de l'eau | traitement eau, osmoseur, adoucisseur, filtration eau | à faire | — | — |
| 8 | Traitement de l'air | purificateur air, ventilation, qualité air intérieur, filtration air | à faire | — | — |
| 9 | Sommeil & environnement nocturne | sommeil, matelas, bruit chambre, obscurité chambre | à faire | — | — |
| 10 | Chauffage, climatisation & humidité | déshumidificateur, climatisation, poêle, humidité maison | à faire | — | — |
| 11 | Animalerie équipement | équipement chien, équipement chat, dressage animal, transport animal | à faire | — | — |
| 12 | Aquariophilie & terrariophilie | aquarium, terrarium, filtration aquarium, éclairage aquarium | à faire | — | — |
| 13 | Apiculture & petit élevage | apiculture, ruche, poulailler, élevage amateur | à faire | — | — |
| 14 | Jardin technique & potager | serre, potager surélevé, irrigation, culture intérieur | à faire | — | — |
| 15 | Piscine & spa | piscine équipement, spa, traitement eau piscine, robot piscine | à faire | — | — |
| 16 | Loisirs créatifs & artisanat | loisir créatif, tufting, vitrail, résine époxy, punch needle | à faire | — | — |
| 17 | Céramique & émaillage | poterie, céramique, four céramique, émaillage | à faire | — | — |
| 18 | Bijouterie & lapidaire | bijouterie amateur, lapidaire, polissage pierre, outil bijoutier | à faire | — | — |
| 19 | Textile, couture & tissage | couture, machine à coudre, tricot, métier à tisser | à faire | — | — |
| 20 | Cuir & maroquinerie | travail du cuir, maroquinerie, outil cuir, cordonnerie | à faire | — | — |
| 21 | Puériculture & motricité | motricité enfant, éveil bébé, chambre enfant, sécurité enfant | à faire | — | — |
| 22 | Cuisine semi-professionnelle | matériel cuisine pro, four professionnel, pâtisserie matériel | à faire | — | — |
| 23 | Brassage, fermentation & conservation | brassage bière, fermentation, conservation aliments, déshydrateur | à faire | — | — |
| 24 | Restauration & food truck | food truck, matériel snack, vitrine réfrigérée, machine restauration | à faire | — | — |
| 25 | Fitness & récupération | musculation maison, récupération sportive, cardio maison, mobilité | à faire | — | — |
| 26 | Bien-être matériel | sauna, luminothérapie, cryothérapie, bain froid | à faire | — | — |
| 27 | Esthétique & coiffure pro | matériel esthétique, coiffure professionnel, onglerie, épilation | à faire | — | — |
| 28 | Home studio & musique | home studio, enregistrement, instrument, sonorisation | à faire | — | — |
| 29 | Photo, vidéo & éclairage | matériel photo, éclairage studio, stabilisateur, fond studio | à faire | — | — |
| 30 | Astronomie & optique | télescope, astronomie, jumelles, observation nature | à faire | — | — |
| 31 | Modélisme & radiocommandé | modélisme, drone, voiture rc, maquette | à faire | — | — |
| 32 | Camping, van & bivouac | camping, aménagement van, bivouac, autonomie électrique | à faire | — | — |
| 33 | Chasse, pêche & nature | pêche, chasse, observation nature, piège photo | à faire | — | — |
| 34 | Vélo & mobilité douce | entretien vélo, atelier vélo, trottinette, mobilité électrique | à faire | — | — |
| 35 | Domotique & sécurité | domotique, alarme maison, vidéosurveillance, contrôle accès | à faire | — | — |
| 36 | Nettoyage technique | nettoyage professionnel, nettoyeur, décapage, entretien surface | à faire | — | — |
| 37 | Rangement modulaire & mobilier transformable | rangement modulaire, meuble gain de place, mobilier transformable | à faire | — | — |
| 38 | Éclairage décoratif & scénographie | éclairage décoratif, luminaire design, scénographie, ambiance lumineuse | à faire | — | — |
| 39 | Événementiel & réception | matériel réception, tente événement, mobilier événementiel | à faire | — | — |
| 40 | Agriculture de loisir & autonomie | permaculture, autonomie alimentaire, petit matériel agricole, meulage grain | à faire | — | — |

## Familles écartées d'office

Ne pas balayer — marchés déjà jugés incompatibles avec le périmètre (voir `PRODUCT-RESEARCH-CRITERIA.md` §4 et les exclusions explicites) :

- bureaux assis-debout, chaises gaming, tables basses génériques, canapés standards, meubles courants sans usage différencié ;
- tout marché B2B pur à ticket supérieur à 2 000 € (chambre froide, fourneau CHR, transpalette) ;
- armes, munitions et rechargement (politique Google Ads vérifiée le 17/07/2026, acquisition Search impraticable).
````

- [ ] **Étape 3 : Vérifier la structure**

```bash
cd "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline"
grep -c "^| [0-9]" familles-exploration.md
```

Attendu : `40`.

- [ ] **Étape 4 : Commit**

```bash
cd "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline"
git add familles-exploration.md
git commit -m "feat(chasse): liste des 40 familles d'exploration"
```

---

## Tâche 2 : Agent `phase0-decouverte`

**Fichiers :**
- Créer : `/Users/Hakim/Documents/Boutiques drop/.claude/agents/phase0-decouverte.md`

Cet agent est le cœur de l'inversion du pipeline. Il applique la même discipline que `phase3-demande` (base France obligatoire, aucune donnée inventée, règle hiérarchique) mais avec un périmètre volontairement étroit : mesurer, jamais interpréter.

- [ ] **Étape 1 : Vérifier que l'agent n'existe pas**

```bash
ls "/Users/Hakim/Documents/Boutiques drop/.claude/agents/phase0-decouverte.md"
```

Attendu : `No such file or directory`.

- [ ] **Étape 2 : Créer le fichier avec son contenu complet**

````markdown
---
name: phase0-decouverte
description: Phase 0 du pipeline de recherche produit — balayage SEMrush d'une famille de marché pour en extraire les clusters au-dessus du seuil de volume. Lancé par la boucle /chasse-clusters. Ne propose aucun produit, ne juge aucune concurrence, ne rend aucun verdict marché.
---

Tu es l'agent de la **phase 0 — Découverte de clusters** du pipeline de recherche produit de Hakim (OH Ventures). Ton rôle : prendre une famille de marché et rendre la liste des clusters de mots-clés dont le volume France atteint le seuil. Tu travailles en français.

Tu es le premier maillon d'une inversion voulue du pipeline : **le volume est mesuré avant qu'aucun produit ne soit imaginé.** Tout ce que tu rends doit pouvoir être vérifié à l'écran. Rien de ce que tu rends ne doit être une hypothèse.

## Lectures obligatoires avant toute action

1. `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/PRODUCT-RESEARCH-CRITERIA.md` — le seuil éliminatoire de volume pertinent et le périmètre commercial viennent de ce fichier, jamais de ta mémoire.
2. `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/PRODUCT-RESEARCH-PLAYBOOK.md` — section « Protocole Semrush France ».
3. `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/familles-exploration.md` — la famille à traiter et ses graines.
4. `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/registre-candidats.md` — pour ne pas ressortir un cluster déjà clos.

Si un fichier manque, arrête-toi et signale-le.

## Méthode

### 1. Accès SEMrush

- Via le navigateur Chrome connecté (MCP `claude-in-chrome`), compte SEMrush déjà authentifié.
- **Base France obligatoire** (`db=fr`). Si l'interface affiche United States ou `db=us`, corrige avant de lire le moindre chiffre. Aucune donnée US n'entre dans ton rapport.
- Si SEMrush est inaccessible (déconnexion, CAPTCHA, quota épuisé, page qui ne charge pas), **arrête-toi immédiatement et déclare-le**. Tu n'improvises pas avec une autre source, tu n'estimes aucun volume de mémoire, tu ne continues pas en mode dégradé sans le dire.

### 2. Balayage par graine

Pour chaque graine de la famille :

1. Ouvrir le **Keyword Magic Tool** sur la graine, base France.
2. Lire le tableau de résultats : mots-clés, volumes, KD, CPC. Utiliser les tris et filtres pour remonter les volumes élevés.
3. Relever les **sous-groupes** que SEMrush propose de lui-même — ce sont des segments réels de la demande, et la principale source de découverte.
4. Noter les mots-clés dont le volume individuel est significatif, avec leur volume exact tel qu'affiché.

Tu ne cherches pas un produit. Tu cherches des **poches de demande**.

### 3. Constitution des clusters

Regroupe les mots-clés en clusters cohérents : même intention, même objet, même usage client. Un cluster est retenu s'il dépasse le seuil du fichier de critères.

### 4. Interdits de comptage — le point le plus important de ta mission

**N'additionne jamais des familles de mots-clés distinctes pour franchir le seuil.**

Anti-exemple réel à ne jamais reproduire (cas « catio », juillet 2026) : la phase 3 avait annoncé 13 000 à 17 000 recherches en additionnant trois familles — `catio` + `enclos extérieur` + `parc` — alors que le mot-clé exact `catio` faisait 2 400. Hakim a dû recontrôler lui-même et abandonner le candidat. L'écart venait entièrement de l'attribution abusive de familles voisines.

Règles qui en découlent :

- un cluster ne regroupe que des mots-clés qu'un même acheteur taperait pour **le même objet** ;
- si deux formulations désignent des produits différents, ce sont deux clusters, même si les produits se ressemblent ;
- quand tu hésites à rattacher un mot-clé, **exclus-le** et note-le dans les exclusions ;
- le volume que tu annonces est toujours celui des mots-clés que tu listes, jamais une somme dont le détail n'apparaît pas.

### 5. Règle hiérarchique

Comme en phase 3, teste plusieurs niveaux de généralité et documente-les : formulation spécifique → famille de produit → catégorie parente. Mais **tu ne juges pas l'adressabilité** — c'est le travail de `phase3-demande` sur SERP réelle. Tu te contentes de rendre les volumes des différents niveaux pour que la phase 3 puisse trancher.

### 6. Graines dérivées

Pour chaque cluster retenu, note les sous-groupes voisins et termes connexes que SEMrush affiche. Ils alimenteront l'auto-expansion de la famille.

## Livrable

Un rapport daté : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/reports/chasse-clusters-<famille>-<YYYY-MM-DD>.md` (date du jour réelle, nom de famille en minuscules avec tirets).

Sections obligatoires :

1. **Entrée** — famille traitée, graines utilisées, date et heure des lectures, base SEMrush confirmée France.
2. **Clusters retenus** — tableau : nom du cluster ; mots-clés constitutifs avec leur volume individuel ; volume total du cluster ; KD et CPC moyens observés ; niveaux de généralité testés.
3. **Clusters écartés** — sous le seuil, avec leur volume mesuré. Aucun écart silencieux.
4. **Mots-clés exclus des clusters** — avec le motif d'exclusion (marque, service, location, occasion, informationnel, low-ticket, objet différent…).
5. **Graines dérivées** — pour l'auto-expansion.
6. **Doublons registre** — clusters correspondant à un produit déjà en STOP ou rejeté, écartés d'office.
7. **Limites** — ce qui n'a pas pu être lu, filtres non disponibles, incertitudes.

## Interdits stricts

- Aucune proposition de produit, aucun nom de candidat. Ta sortie est une liste de clusters, pas d'idées.
- Aucun jugement de concurrence, aucun prix, aucun verdict marché (GO/STOP).
- Aucun sourcing AliExpress.
- Aucune donnée d'une base autre que France.
- Aucun volume estimé, extrapolé ou « de mémoire » : chaque chiffre vient d'une lecture datée de l'écran.
- Aucune addition de familles distinctes pour atteindre le seuil (voir §4).

## Règles de preuve et de conduite

- Date chaque lecture.
- Distingue observé / déduit. N'invente rien.
- Aucun contact vendeur, aucun achat, aucune modification Shopify / Google Ads / Merchant Center.

## Gate de sortie

Conforme si : rapport daté du jour, sections complètes, chaque cluster retenu détaille ses mots-clés avec volumes individuels, chaque exclusion a un motif, base France confirmée.

Ta réponse finale à la boucle : chemin du rapport, nombre de clusters retenus, leur nom et volume, graines dérivées, limites rencontrées.
````

- [ ] **Étape 3 : Vérifier le frontmatter**

```bash
cd "/Users/Hakim/Documents/Boutiques drop/.claude/agents"
head -4 phase0-decouverte.md
```

Attendu : trois tirets, une ligne `name: phase0-decouverte`, une ligne `description:` non vide, trois tirets.

- [ ] **Étape 4 : Vérifier que l'anti-exemple catio est bien présent**

```bash
cd "/Users/Hakim/Documents/Boutiques drop/.claude/agents"
grep -c "catio" phase0-decouverte.md
```

Attendu : au moins `1`. C'est le garde-fou central contre la fabrication de faux volume — s'il a disparu, la tâche est incomplète.

Pas de commit : `.claude/agents/` est hors dépôt (voir la note sur le versionnage en tête de plan).

---

## Tâche 3 : Agent `critique-candidat`

**Fichiers :**
- Créer : `/Users/Hakim/Documents/Boutiques drop/.claude/agents/critique-candidat.md`

C'est le garde-fou anti-dérive. Sa contrainte définissante : il ne sait jamais combien de candidats manquent pour atteindre l'objectif.

- [ ] **Étape 1 : Vérifier que l'agent n'existe pas**

```bash
ls "/Users/Hakim/Documents/Boutiques drop/.claude/agents/critique-candidat.md"
```

Attendu : `No such file or directory`.

- [ ] **Étape 2 : Créer le fichier avec son contenu complet**

````markdown
---
name: critique-candidat
description: Contrôle à froid d'un dossier candidat contre les critères canoniques de recherche produit. Lancé par la boucle /chasse-clusters après qualification. Verdict binaire retenu/non retenu. Ne connaît jamais l'objectif chiffré de la boucle.
---

Tu es l'agent **critique** du pipeline de recherche produit de Hakim (OH Ventures). On te soumet un dossier candidat déjà qualifié, et tu réponds à une seule question : **ce candidat coche-t-il réellement les trois cases ?** Tu travailles en français.

## Ta contrainte définissante

Tu ne sais pas combien de candidats la boucle a déjà retenus, ni combien il lui en manque, et tu ne dois jamais chercher à le savoir. Si le brief qu'on te transmet contient ce genre d'information, **ignore-la explicitement** et signale-le dans ton verdict.

Ta raison d'être est d'empêcher la boucle de baisser sa barre à mesure que les candidats faciles s'épuisent. Un candidat évalué en fin de course doit être jugé exactement comme le premier.

## Lectures obligatoires avant toute action

1. `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/PRODUCT-RESEARCH-CRITERIA.md` — relis-le intégralement à chaque candidat. Aucun seuil de ta mémoire, aucun seuil d'un candidat précédent.
2. Les rapports du dossier candidat qu'on te transmet (phase 0, phase 2, phase 3, phase 4).

Si un fichier manque, réponds **non retenu** pour dossier incomplet.

## Les trois cases

### Case 1 — Volume

- Le volume pertinent, **après nettoyage SERP**, atteint-il le seuil du fichier de critères ?
- Ce volume est-il celui de mots-clés effectivement listés, ou une somme dont le détail n'apparaît pas ? Une somme non détaillée est un échec.
- Le cluster additionne-t-il des familles distinctes ? Si oui, échec (anti-exemple catio).
- Les lectures sont-elles datées et en base France ?

### Case 2 — Concurrence

- Le prix marché constaté permet-il de défendre une offre entre 150 et 400 € ?
- Le comptage sépare-t-il bien concurrents institutionnels et dropshippers ?
- Le marché est-il dominé par des enseignes généralistes au sens du §4 des critères ? Si oui, échec.
- Existe-t-il une différenciation défendable, ou l'offre est-elle immédiatement comparable sur le prix ?

### Case 3 — Fournisseur

- Une fiche AliExpress a-t-elle été **ouverte et vérifiée**, ou seulement supposée existante ?
- Prix rendu, notation vendeur, délai et entrepôt sont-ils tous relevés ?
- La notation vendeur est-elle exploitable ? Entre 90 et 95 % c'est un cas limite, pas une validation.
- Le prix rendu laisse-t-il un écart crédible avec le prix marché constaté ? Tu ne calcules pas la marge — c'est la phase 5 — mais un prix rendu supérieur ou égal au prix marché est un échec évident.

## Verdict

**Binaire. Retenu ou non retenu.**

Un « presque », un « sous réserve de », un « intéressant mais » sont des **non retenu**. Si tu hésites, c'est non. La boucle produira moins de candidats mais ils tiendront.

Un candidat marqué `CAS LIMITE` par une phase précédente est **non retenu** par toi : les cas limites remontent à Hakim et ne sont jamais tranchés par un agent.

## Livrable

Ta réponse directe à la boucle, sans créer de fichier :

1. **Verdict** — `RETENU` ou `NON RETENU`.
2. **Case par case** — pour chacune des trois, ce qui a été vérifié et ce qui manque.
3. **Motif** — en cas de refus, la raison précise et la case qui échoue.
4. **Réserves à conserver** — si retenu, tout point conditionnel ou non vérifié qui doit accompagner le candidat dans le registre. Ne supprime jamais une réserve d'un rapport précédent.

## Interdits stricts

- Ne jamais assouplir un seuil, même de peu, même en le signalant.
- Ne jamais compenser une case faible par une case forte. Les trois doivent passer.
- Ne jamais tenir compte du nombre de candidats déjà retenus.
- Ne jamais trancher un cas limite.
- Ne jamais retirer une réserve.
````

- [ ] **Étape 3 : Vérifier le frontmatter et la contrainte définissante**

```bash
cd "/Users/Hakim/Documents/Boutiques drop/.claude/agents"
head -4 critique-candidat.md
grep -c "compteur\|combien de candidats" critique-candidat.md
```

Attendu : frontmatter valide, et au moins `1` occurrence — l'aveuglement au compteur est ce qui justifie l'existence de l'agent.

Pas de commit : `.claude/agents/` est hors dépôt.

---

## Tâche 4 : Skill `chasse-clusters`

**Fichiers :**
- Créer : `/Users/Hakim/Documents/Boutiques drop/.claude/skills/chasse-clusters/SKILL.md`

- [ ] **Étape 1 : Créer le répertoire**

```bash
mkdir -p "/Users/Hakim/Documents/Boutiques drop/.claude/skills/chasse-clusters"
```

- [ ] **Étape 2 : Créer le fichier avec son contenu complet**

````markdown
---
name: chasse-clusters
description: Boucle autonome de chasse aux candidats produit, volume-first. Balaie des familles de marché sur SEMrush, qualifie les clusters trouvés et accumule des candidats vérifiés dans le registre jusqu'à 20. Utiliser quand Hakim lance /chasse-clusters ou demande d'accumuler des candidats produit en autonomie.
---

# Boucle — Chasse aux clusters

Tu pilotes la boucle de découverte volume-first de Hakim (OH Ventures). Tu n'exécutes **aucune phase toi-même** : tu lances les sous-agents, tu contrôles leurs livrables, tu écris le registre et tu appliques la règle d'arrêt fail-closed.

Design de référence : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/specs/2026-07-20-boucle-chasse-clusters-design.md`.

Cette boucle est conçue pour tourner **en autonomie totale**. Personne ne surveille. Tes garde-fous ne sont donc pas des formalités.

## Avant de démarrer

1. Lis `registre-candidats.md` et `familles-exploration.md`. Si l'un manque, arrête-toi et signale-le.
2. Compte les candidats déjà retenus dans la section « Chasse clusters » du registre. C'est ton compteur de départ — une relance reprend où la boucle s'est arrêtée.
3. Détermine la date du jour réelle.
4. Vérifie l'accès SEMrush : ouvre l'outil dans Chrome et confirme que le compte est connecté et la base sur France. Si non, arrête-toi et demande à Hakim de se reconnecter.
5. Annonce à Hakim le compteur de départ et la famille par laquelle tu commences.

## Boucle principale

Tant que le compteur est inférieur à **20** et qu'il reste des familles non balayées :

### 1. Découverte

Lance `phase0-decouverte` (Agent, synchrone) sur la famille suivante non balayée, avec ses graines et la date du jour.

Contrôle du livrable : le rapport existe, il est daté du jour, ses sections obligatoires sont présentes, aucun produit n'y est proposé, aucun verdict marché n'y figure. Non conforme = arrêt, pas de rattrapage silencieux.

### 2. Anti-doublon

Écarte tout cluster correspondant à un produit déjà en STOP, rejeté ou clos dans le registre. Applique la logique de synonymes : singulier/pluriel, accents, français/anglais, variantes proches, même usage client.

Une reprise n'est possible que si Hakim l'a explicitement demandée et documentée comme `reprise motivée`.

### 3. Qualification, cluster par cluster

Pour chaque cluster survivant, dans l'ordre décroissant de volume :

**a. Filtre qualitatif** — lance `phase2-filtre` avec le cluster et son volume. Il identifie les produits qui servent ce cluster et applique banalité, valeur perçue, différenciation et tranche 150–400 €. Shortlist vide = cluster abandonné, on passe au suivant.

**b. Demande réelle** — lance `phase3-demande` sur les survivants. C'est lui qui nettoie la SERP, mesure le volume réellement adressable, relève les prix et compte les concurrents en séparant institutionnels et dropshippers. Un `STOP marché` ferme le cluster. Un `CAS LIMITE` ne continue pas : il est noté au registre et remonté à Hakim en fin de tour.

**c. Fournisseur** — lance `phase4-sourcing` sur les `GO marché` uniquement. Une à deux fiches AliExpress ouvertes et vérifiées : prix rendu, notation vendeur, délai, entrepôt. Aucune offre exploitable = cluster fermé.

**d. Critique** — lance `critique-candidat` avec les rapports du dossier. **Ne lui transmets jamais le compteur, ni le nombre de candidats manquants, ni aucune indication d'avancement.** Son verdict est binaire et sans appel.

**e. Écriture** — si `RETENU`, écris immédiatement la ligne dans la section « Chasse clusters » du registre, avec toutes ses réserves, puis incrémente le compteur. L'écriture se fait candidat par candidat, jamais en fin de tour : une interruption ne doit rien perdre.

### 4. Auto-expansion

Avant de passer à la famille suivante, traite les graines dérivées notées par `phase0-decouverte` pour les clusters retenus. Elles sont ajoutées à la famille en cours, jamais transformées en nouvelle famille sans validation de Hakim.

### 5. Clôture de famille

Marque la famille `balayée` dans `familles-exploration.md`, avec la date et le nombre de candidats retenus. Puis famille suivante.

## Règle d'arrêt fail-closed

La boucle s'arrête d'elle-même dans quatre cas :

1. **Objectif atteint** — 20 candidats retenus.
2. **Familles épuisées** — rapport de couverture avec le compte obtenu.
3. **Trois familles consécutives sans aucun candidat retenu** — signal que le seuil est incompatible avec le périmètre. **Tu ne baisses jamais le seuil toi-même** : tu remontes le constat à Hakim et tu t'arrêtes.
4. **Blocage technique** — SEMrush déconnecté, CAPTCHA AliExpress, page qui ne charge pas, fichier canonique introuvable, livrable non conforme.

Sur blocage : mets le registre à jour avec l'état atteint, puis produis le rapport d'arrêt. **Aucun volume n'est jamais estimé pour continuer. Aucune donnée n'est inventée.**

## Interdits stricts

- Ne jamais assouplir un critère pour atteindre l'objectif chiffré. Un compte de 12 candidats solides vaut mieux que 20 dont 8 sont faibles.
- Ne jamais transmettre le compteur à `critique-candidat`.
- Ne jamais aller au-delà du niveau 2 de validation : pas de phase 5, pas de commande test, pas de GO lancement.
- Aucun contact vendeur, aucun achat, aucun ajout au panier, aucune connexion à un compte.
- Aucune modification Shopify, Google Ads ou Merchant Center. Aucune publication.
- Ne jamais supprimer une réserve d'un rapport précédent.

## Rapport final

En français, dans cet ordre :

1. **Résultat en une phrase** — combien de candidats retenus, sur combien de familles balayées, et pourquoi la boucle s'est arrêtée là.
2. **Les candidats** — tableau complet avec volume, prix marché, concurrence, fournisseur, réserves.
3. **Couverture** — familles balayées, familles restantes, clusters écartés et pourquoi.
4. **Cas limites** — ce qui attend une décision de Hakim.
5. **Limites d'outillage** — ce qui n'a pas pu être vérifié.
````

- [ ] **Étape 3 : Vérifier le frontmatter**

```bash
cd "/Users/Hakim/Documents/Boutiques drop/.claude/skills/chasse-clusters"
head -4 SKILL.md
```

Attendu : frontmatter valide avec `name: chasse-clusters`.

- [ ] **Étape 4 : Vérifier la présence des quatre conditions d'arrêt**

```bash
cd "/Users/Hakim/Documents/Boutiques drop/.claude/skills/chasse-clusters"
grep -c "Objectif atteint\|Familles épuisées\|Trois familles consécutives\|Blocage technique" SKILL.md
```

Attendu : `4`.

Pas de commit : `.claude/skills/` est hors dépôt.

---

## Tâche 5 : Section registre

**Fichiers :**
- Modifier : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/registre-candidats.md`

- [ ] **Étape 1 : Localiser le point d'insertion**

La nouvelle section se place **après** le bloc d'en-tête (règles d'usage et date de mise à jour, lignes 1 à 12) et **avant** la section `## Produits lancés`, pour que la chasse en cours soit visible en premier.

```bash
cd "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline"
grep -n "^## Produits lancés" registre-candidats.md
```

Attendu : une ligne, aux alentours de la ligne 14.

- [ ] **Étape 2 : Insérer la section juste avant `## Produits lancés`**

````markdown
## Chasse clusters — boucle volume-first (lancée le 20 juillet 2026)

Objectif : 20 candidats qualifiés (volume mesuré, concurrence chiffrée, fiche AliExpress vérifiée). Design : [specs/2026-07-20-boucle-chasse-clusters-design.md](specs/2026-07-20-boucle-chasse-clusters-design.md). État du balayage : [familles-exploration.md](familles-exploration.md).

Chaque ligne a passé le contrôle de `critique-candidat`. Aucune n'est allée jusqu'à la phase 5 : le choix des candidats à pousser appartient à Hakim.

**Compteur : 0 / 20**

| # | Candidat | Cluster et volume pertinent | Prix marché | Concurrents (institutionnels / dropship) | Fournisseur AliExpress | Réserves | Date |
|---|---|---|---|---|---|---|---|
| — | *aucun candidat retenu à ce jour* | — | — | — | — | — | — |

### Cas limites remontés à Hakim

| Candidat | Cluster | Point à trancher | Date |
|---|---|---|---|
| — | — | — | — |
````

- [ ] **Étape 3 : Vérifier l'insertion**

```bash
cd "/Users/Hakim/Documents/Boutiques drop"
grep -n "^## " boutique-pipeline/registre-candidats.md | head -5
```

Attendu : `## Chasse clusters` apparaît avant `## Produits lancés`.

- [ ] **Étape 4 : Commit**

```bash
cd "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline"
git add registre-candidats.md
git commit -m "feat(chasse): section chasse clusters dans le registre"
```

---

## Tâche 6 : Dry-run sur une famille

C'est la seule tâche qui prouve que la chaîne fonctionne. Elle se fait **avec Hakim présent**, pas en autonomie, parce que c'est le moment où les erreurs de conception apparaissent.

**Prérequis :** compte SEMrush souscrit, connecté dans Chrome, base France.

- [ ] **Étape 1 : Vérifier que les deux nouveaux agents sont reconnus**

Dans une session Claude Code, vérifier que `phase0-decouverte` et `critique-candidat` apparaissent dans la liste des agents disponibles. S'ils n'apparaissent pas, redémarrer la session.

- [ ] **Étape 2 : Lancer la découverte seule, sur une famille**

Lancer `phase0-decouverte` sur la famille 16 (loisirs créatifs & artisanat) — choisie parce que le tufting en est issu et qu'on connaît déjà la réponse attendue sur ce segment, ce qui donne un point de contrôle.

Attendu : un rapport `reports/chasse-clusters-loisirs-creatifs-artisanat-2026-XX-XX.md` avec des clusters mesurés, aucun nom de produit, aucun verdict.

- [ ] **Étape 3 : Contrôler la qualité du balayage**

Trois vérifications manuelles, à faire par Hakim :

1. Les volumes annoncés correspondent-ils à ce que SEMrush affiche ? (en rouvrir deux ou trois au hasard)
2. Un cluster additionne-t-il des familles distinctes ? Si oui, l'interdit du §4 de l'agent n'a pas fonctionné et il faut le renforcer.
3. Le cluster `tufting` ressort-il, et à un volume cohérent avec les 13–17 k documentés en juillet 2026 ?

Si le point 2 échoue, **ne pas lancer la boucle** — corriger l'agent d'abord. C'est le défaut qui coûterait le plus cher en autonomie.

- [ ] **Étape 4 : Faire un tour complet sur un seul cluster**

Prendre le cluster de plus fort volume du rapport et le passer manuellement dans la chaîne : `phase2-filtre` → `phase3-demande` → `phase4-sourcing` → `critique-candidat`.

Objectif : mesurer le temps réel d'un cluster et vérifier que les agents existants acceptent bien un cluster mesuré en entrée là où ils recevaient auparavant un candidat non mesuré.

- [ ] **Étape 5 : Ajuster, puis commiter uniquement ce qui est versionné**

Les correctifs sur les agents et le skill ne se commitent pas (hors dépôt). Si le dry-run a modifié `familles-exploration.md` ou `registre-candidats.md`, les commiter en les nommant explicitement :

```bash
cd "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline"
git add familles-exploration.md registre-candidats.md
git commit -m "fix(chasse): ajustements issus du dry-run"
```

- [ ] **Étape 6 : Lancer la boucle**

```
/loop /chasse-clusters
```

Sans intervalle : la boucle s'auto-cadence. Elle s'arrêtera à 20 candidats, sur famille épuisée, sur trois familles stériles consécutives, ou sur blocage technique.

---

## Ordre d'exécution

Les tâches 1 à 5 sont indépendantes et peuvent être faites dans n'importe quel ordre. La tâche 6 exige que les cinq précédentes soient terminées et que le compte SEMrush soit actif.

## Correctifs appliqués après revue (20 juillet 2026)

Une revue de conformité a été passée sur les cinq fichiers livrés. Quatre correctifs ont été appliqués directement, hors du contenu prescrit ci-dessus :

1. **`chasse-clusters/SKILL.md`, étape 3e** — la mise à jour de la ligne `**Compteur : N / 20**` du registre et la suppression de la ligne d'amorce placeholder ont été rendues explicites. Sans ça le compteur serait resté figé à 0 et le placeholder aurait pu être compté comme un candidat.
2. **`chasse-clusters/SKILL.md`, étape de démarrage** — le compteur de reprise se lit en comptant les lignes du tableau, pas la valeur affichée, pour qu'une désynchronisation ne se propage pas.
3. **`chasse-clusters/SKILL.md`, contrôle de livrable** — le chemin et le nombre de sections attendus du rapport de `phase0-decouverte` sont désormais cités, sinon le contrôle ne pouvait pas détecter un mauvais nommage.
4. **`familles-exploration.md`, §Auto-expansion** — « colonne » corrigé en « section », pour correspondre à la structure réelle du rapport produit par `phase0-decouverte`.

Deux points restent ouverts et appartiennent à Hakim, voir la section suivante.

## Points ouverts pour Hakim

**A. Contradiction avec le §7 de `PRODUCT-RESEARCH-CRITERIA.md`.** Ce paragraphe impose un « ordre obligatoire du pipeline » : idée → filtre → validation du volume. La boucle inverse volontairement cet ordre. Or `critique-candidat` a pour consigne de relire ce fichier intégralement et de n'assouplir aucun critère — un critique littéral peut donc rejeter tout candidat au motif que l'ordre n'a pas été respecté. Le fichier de critères doit reconnaître deux chemins d'entrée légitimes. C'est une modification d'un fichier canonique : elle appartient à Hakim.

À noter au passage : le §7 mentionne « validation **Ahrefs** » alors que toute la chaîne impose SEMrush. Incohérence préexistante, que la boucle rend opérante.

**B. Notation vendeur entre 90 et 95 % traitée en cas limite.** Ce seuil vient de l'orchestrateur `/recherche-produit` existant, il n'est donc pas inventé. Mais sa conséquence dans la boucle est nouvelle : un cas limite est `NON RETENU` par `critique-candidat`, donc tout candidat dont le vendeur est noté entre 90 et 95 % ne comptera jamais dans les 20 — il remontera à Hakim. Le candidat de référence tufting est à 93,1 % et serait dans ce cas. Comportement défendable (l'arbitrage revient à l'humain), mais Hakim doit savoir qu'il réduira mécaniquement le débit de la boucle.

## Ce que ce plan ne fait pas

- Il ne modifie aucun agent existant. Si le dry-run montre que `phase2-filtre` ou `phase3-demande` supportent mal un cluster en entrée, ce sera un plan séparé.
- Il ne touche pas à `/recherche-produit`, qui continue de fonctionner à l'identique pour les recherches lancées à la main.
- Il ne va jamais au-delà du niveau 2 de validation.

# Instrumentation — ce qu'on capture maintenant pour pouvoir apprendre plus tard

**Décision Hakim, 30/08/2026.** La boucle d'apprentissage (prédiction → résultat → post-mortem →
règle) n'a de valeur que si la collecte commence **avant** qu'on en ait besoin. Ce dossier ne sert
à rien aujourd'hui. Il sert à tout dans six mois.

Surface de lecture : **Obsidian**, vault = la racine de `Boutiques drop`. Chaque note porte un
frontmatter YAML, les vues `.base` s'en servent pour construire les tableaux. Pas d'export, pas de
synchronisation : les agents écrivent les fichiers, Git les versionne, Obsidian les affiche.

## Ce que ce dossier n'est pas

Il ne remplace rien. `METHODE-TABLEAU.md` reste la loi :

| Fichier | Rôle | Statut |
|---|---|---|
| `TABLEAU.md` | point d'entrée, kanban de tickets | inchangé |
| `ETAT.md` | état **courant** chiffré, écrasé à chaque màj | inchangé |
| `REGLES.md` | règles non négociables de cette boutique | inchangé |
| `journal/` | comptes rendus datés | contenu inchangé, **frontmatter ajouté** |

L'instrumentation ajoute uniquement ce que ces quatre fichiers ne peuvent pas porter : **l'historique
qui ne s'écrase pas**, et **la croyance d'avant**.

## Les quatre objets

### 1. `croyances/<boutique>.md` — ce qu'on croyait avant de lancer

**Le plus périssable, et le seul qui ne se récupère nulle part.** Une croyance non écrite se réécrit
toute seule à la lumière du résultat. Sans elle, un post-mortem ne peut rien conclure : on ne sait
plus quelle hypothèse était fausse.

Champ décisif : **`signaux_ecartes`** — ce qu'on avait vu et volontairement écarté. C'est le premier
endroit où regarder quand une boutique échoue, et personne ne le note jamais.

Champ `source` : `observe` si écrit avant le lancement, `reconstruit` si reconstitué après. Les deux
sont utiles ; les confondre pollue le dataset. Une croyance reconstruite porte toujours
`confiance_reconstruction`.

### 2. `mesures/<boutique>-<AAAA-Www>.md` — le relevé qui ne s'écrase jamais

Une note par boutique et par semaine. Jamais modifiée après coup : si un chiffre était faux, on
écrit une note de correction, on ne réécrit pas l'histoire.

Les métriques commerce (sessions, commandes, CA, AOV, CVR) sont récupérables dans Shopify a
posteriori — elles peuvent être remplies en rattrapage. **Les autres non** : GMC approuvés/limités,
PageSpeed, LCP, positions SEO. Celles-là, une semaine non relevée est perdue pour toujours.

### 3. Le frontmatter des journaux existants — pourquoi on a changé quelque chose

Les 193 entrées de `journal/` sont déjà le registre des interventions. Il leur manque quatre lignes
pour devenir interrogeables. On n'y touche pas au contenu.

```yaml
---
type: journal
boutique: tufting
date: 2026-08-16
nature: intervention      # intervention = on a changé quelque chose | analyse = on a mesuré
leviers: [vitesse]
titre: "Chantier vitesse — Tuftéo, 16/08/2026"
---
```

Posé par `backfill-frontmatter.py`, idempotent : il saute tout fichier qui a déjà un
frontmatter, et n'insère qu'en tête — le contenu n'est jamais touché. À relancer après
l'ajout de nouvelles entrées.

**La clé de jointure est `boutique`, et c'est le slug du dossier** : `tufting`,
`bonum-vitae`, `seiko-mod` — pas le nom commercial. Toutes les notes d'instrumentation
doivent employer le même slug, sinon les vues ne joignent plus.

Leviers admis : `prix`, `offre`, `page`, `creative`, `catalogue`, `conformite`, `concurrence`,
`technique`, `vitesse`, `ads`, `seo`, `sourcing`, et `autre` quand l'entrée est un compte rendu
de session sans levier unique (17 cas sur 192 — c'est honnête, pas une lacune).

**Sans ce registre, les mesures sont ininterprétables.** Une CVR qui passe de 1,2 à 1,9 % ne prouve
rien si on ignore qu'on a changé la page et le prix la même semaine.

### 4. `regles/RULE-AAAA-NNN.md` — ce qu'on a appris

Taxonomie reprise de `hermes-orchestration/scoring/learned-rules.md` :
`observation` → `candidate` → `validee` → `retiree`.

Une règle contredite est **retirée explicitement**, jamais effacée : savoir qu'on a cru quelque chose
de faux fait partie du dataset.

## La règle qui compte plus que le schéma

**Un schéma trop riche ne sera pas rempli.** Chaque champ ci-dessous a passé le test : « est-ce que
ce sera encore rempli dans trois mois ? » Si un champ finit systématiquement vide, on le supprime —
un champ vide ment davantage qu'un champ absent.

## Relever les mesures

```bash
python3 instrumentation/mesure-hebdo.py --boutiques tufting,bonum-vitae --ecrire
```

Sans `--ecrire`, dry-run. Le script **ne réécrit jamais une note existante** : une mesure est un
fait daté. Pour corriger un chiffre, écrire une note de correction à côté.

**Pourquoi un jeton d'application et pas le connecteur MCP** (constat du 30/08/2026) : le
connecteur Shopify ne tient qu'une boutique à la fois, et en changer **révoque** l'accès à la
précédente, avec une réautorisation manuelle à chaque fois. Sur trois boutiques et une cadence
hebdomadaire, c'est intenable — et un agent ne pourra jamais cliquer sur un écran d'autorisation.
Une application personnalisée par boutique donne un jeton permanent, utilisable sans écran.

Le scope **`read_reports`** est obligatoire : les scopes de la CLI Shopify déjà en place
(products, themes, content, pages…) ne permettent pas d'interroger ShopifyQL.

## Cadence

| Quoi | Quand | Qui |
|---|---|---|
| Croyance | une fois, avant le lancement | agent, validé par Hakim |
| Mesure | hebdomadaire, même jour | agent (Shopify + relevés) |
| Frontmatter d'intervention | à l'écriture du journal | l'agent qui écrit le journal |
| Règle | quand un post-mortem la propose | agent, **acceptée par Hakim** |

Aucun agent ne promeut une règle en `validee` sans accord humain — reprise directe de la
constitution : la politique métier ne se réécrit jamais silencieusement.

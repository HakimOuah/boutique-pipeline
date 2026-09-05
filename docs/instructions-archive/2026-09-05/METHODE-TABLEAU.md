# Méthode de travail — un tableau par boutique

Décision de Hakim, 11/08/2026. Remplace la pratique précédente (un rapport daté par intervention, empilés dans le dossier de la boutique — 110 fichiers markdown pour Noirmont, aucun point d'entrée).

## La règle

**Chaque boutique a un dossier, et ce dossier a un seul point d'entrée : `TABLEAU.md`.**

```
boutique-<nom>/
  TABLEAU.md      ← LE point d'entrée. Kanban de tickets. Toujours à jour.
  ETAT.md         ← l'état courant chiffré, en une page. Toujours à jour.
  REGLES.md       ← règles non négociables + pièges déjà payés sur cette boutique.
  journal/        ← les comptes rendus datés. Archive, jamais un point d'entrée.
  backups/        ← sauvegardes avant modification (un sous-dossier par opération).
  preuves/        ← captures, exports, planches de QA.
  livraisons/     ← visuels et fichiers produits, en attente de rattachement.
```

**Qui que tu sois — Claude, Codex, ou Hakim — tu commences par lire `TABLEAU.md`.** Si tu as besoin du détail d'une décision passée, tu vas dans `journal/`. Tu n'ouvres jamais `journal/` pour savoir *quoi faire*.

## Le format d'un ticket

Un ticket décrit **ce qu'il faut faire ET comment le faire**, pour qu'un agent qui n'a aucun contexte puisse l'exécuter seul. C'est la condition pour que le relais fonctionne quand une limite est atteinte.

```markdown
### T-XX — Titre à l'impératif
**État** : À FAIRE | EN COURS | BLOQUÉ | FAIT
**Pour** : Claude | Codex | Hakim
**Pourquoi** : une phrase — l'enjeu réel, pas la tâche répétée.
**Comment** :
1. étape concrète
2. étape concrète
**Sortie attendue** : ce qui prouve que c'est fini.
**Attention** : le piège spécifique à ce ticket, s'il y en a un.
**Réf.** : fichiers à lire.
```

### Les colonnes

| État | Sens |
|---|---|
| **À FAIRE** | prêt à être pris, tout est dit dans le ticket |
| **EN COURS** | quelqu'un travaille dessus — noter qui et depuis quand |
| **BLOQUÉ** | attend une décision ou une action de Hakim, ou une dépendance |
| **FAIT** | terminé et vérifié — déplacé en bas du tableau, avec la date et le lien vers le compte rendu |

## Les trois obligations

1. **Mettre à jour `TABLEAU.md` en fin d'intervention**, avant de rendre la main. Un ticket qu'on a commencé passe en EN COURS ; un ticket terminé passe en FAIT avec le lien vers son compte rendu dans `journal/`. C'est la seule chose qui ne se délègue pas.
2. **Écrire le compte rendu dans `journal/`**, pas à la racine du dossier boutique. Nom : `AAAA-MM-JJ-sujet.md`.
3. **Commit + push** — la source de vérité est GitHub, pas le disque.

## Ce que ça règle

Quand une limite d'usage tombe au milieu d'un chantier, le relais lit `TABLEAU.md` et sait exactement où reprendre, sans avoir à reconstituer l'histoire à partir de quinze rapports datés — ce qui a coûté une semaine de flottement en août 2026.

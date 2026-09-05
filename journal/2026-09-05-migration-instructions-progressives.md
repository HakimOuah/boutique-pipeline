---
date: 2026-09-05
type: intervention
agent: codex
---
# Migration des instructions

Migration autorisée par Hakim après la phase d'audit. Branches `codex/instructions-progressives-20260905` dans boutique-pipeline, boutiques-drop et drop-elite-google-os. Installations locales séparées des fusions Git ; aucun main fusionné.

## Résultat

- Routeurs communs, fin de tâche proportionnée, frontières externes et politique de branche cohérentes.
- Recherche en socle commun + Produit pur/Search + Univers/Shopping ; références métier conditionnelles.
- Critères canoniques, registres candidats et tableaux des boutiques inchangés. Les archives conservent le playbook et les prompts avant migration.
- TABLEAU se lit par ticket et se met à jour si son état change. Journal proportionné ; NOX garde son rôle éditorial brut.
- Skills Claude/Hermes et Codex alignées ; adaptations des Skills vendor séparées des snapshots contrôlés.
- Export Hermes : neuf profils, contrôle sans écriture, empreintes de sources et protection des copies générées modifiées.
- Ancien scoring indicatif seulement, sans décision commerciale automatique ; CLI et rapports compatibles.
- DataForSEO : null ne devient plus zéro ; consolidation bloquée si volume manque, provenance/cache datés, témoin valide et cohérent avant/après. Le JSON existant conserve sa forme, métadonnées dans `.meta.json`.
- Générateur boutique : TABLEAU, ETAT, REGLES et dossiers de coordination présents dès la création.

## Préservation et retour arrière

Carte du playbook : [MIGRATION](../product-research/MIGRATION.md). Originals versionnés dans `docs/instructions-archive/2026-09-05/`. Copies locales avant installation et manifeste des fichiers dans `~/.codex/instruction-backups/20260905-instructions-migration/`.

Les anciens états, comptes rendus et décisions ne sont pas réécrits. Les gros tableaux peuvent ensuite être archivés progressivement avec maintien des liens, pendant leur prochaine intervention utile ; leur déplacement massif n'est pas nécessaire à la lecture ciblée.

## Mesure du contexte

{
  "ancien_playbook_mots": 5396,
  "nouveau_routeur_mots": 113,
  "ancien_plus_criteres": 8061,
  "nouveau_search_plus_criteres": 3324
}

Comptage de mots statique, avant références conditionnelles et historique de conversation. Ce n'est ni un relevé de tokens facturés ni une preuve de qualité supérieure.

## Vérification et limites

47 tests passent dans les clones actifs (44 pipeline, 3 synchronisation), avec quatre sous-tests DataForSEO supplémentaires. Les 27 Skills actives contrôlées sont valides, les neuf profils Hermes ne présentent aucun écart et le corpus/NOX sont valides. Un exemple d’ordre contient un chemin absolu du clone : son échec en worktree isolé ne se reproduit pas dans le clone actif.

Les processus déjà en cours gardent leur contexte antérieur. Recharger Codex et lancer les prochaines missions Hermes pour utiliser les nouvelles copies. Aucun appel de recherche payant ni action de production pendant la migration.

Les snapshots vendor restent intacts. Deux liens optionnels vendor préexistants pointent vers des Skills/outils non fournis (`pricing` et intégration SparkToro) ; ils ne sont pas nécessaires aux routeurs installés. Les recettes de formation restent datées et doivent être confrontées aux exigences actuelles lorsqu'une décision en dépend.

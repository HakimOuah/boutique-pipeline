# Lumière Matière — Tableau

## Bloqué

### T-01 — Produire les visuels de variantes du 04/09/2026
**État** : BLOQUÉ POUR LE SOLDE — livraison partielle vérifiée par Codex le 04/09/2026 : 9 packshots + 6 schémas (5 partiels), 20 manifestes.
**Pour** : Codex
**Pourquoi** : montrer les couleurs, formes et dimensions réelles des variantes.
**Comment** : contrôler les sources locales des lots P1/P2/P6 ; établir les correspondances avant génération ; produire et vérifier les JPEG et manifestes.
**Sortie attendue** : livraison dans `livraisons-visuels-codex/variantes-forme/`, provenance et QA, compte rendu dans `journal/`.
**Attention** : aucune action Shopify ou DSers ; SKU inchangés ; pas de correspondance ni de cote inventée. Les fiches 272937 et 607504 attendent un arbitrage explicite du brief.
**Réf.** : [Brief](briefs/2026-09-04-codex-variantes-formes.md), les trois JSON associés.

**Compte rendu** : [Production et preuves](journal/2026-09-04-variantes-formes.md), [registre et prompts](journal/2026-09-04-variantes-formes-registre.json), [QA 15/15](journal/2026-09-04-variantes-formes-qa.json).

**Pour débloquer le solde** :

1. Fournir les correspondances code/photo pour 975417, 338324, 147607, 560098 et B/C de 253182 ; identifier les deux finitions de 092465 et la référence rotin de 897170.
2. Arbitrer les configurations de 272937, le renommage de 607504, et les montages de 795468/630923.
3. Compléter les cotes manquantes des cinq schémas partiels listées au journal.

**Correction intégrée** : 405368 Beige et blanc = A2 (SKU confirmé dans le brief corrigé 52a9f80). Le rendu D1 vert a été écarté, A2 régénéré avec disque blanc et câble blanc. Aucun arbitrage restant sur son nom.

## Fait pour cette passe

Précontrôle des 20 fiches, production des éléments exploitables, schémas à échelle calculée, QA locale et documentation. Le lot global n’est pas marqué FAIT car les blocages ci-dessus restent ouverts.

Ce tableau suit cette intervention uniquement ; il ne prétend pas inventorier les autres chantiers ou l’état live de la boutique.

### T-02 — Header desktop : menu à 4 entrées, logo visible
**État** : EN COURS — navigation appliquée sur le live le 04/09 (logo revenu, une ligne) ; thème `LM UX 2026-09-04` prêt, **publication par Hakim**.
**Pour** : Hakim (navigation + personnalisateur), ou Cursor sur copie de thème.
**Pourquoi** : le menu à 10 entrées écrase la colonne du logo à 0 px et passe sur deux lignes.
**Comment** : `shopify/AUDIT-UX-UI-2026-09-04.md` §1 — cible à 5 entrées, utilitaires vers le footer et une icône « suivi », puis layout « logo à gauche, menu à gauche » en filet. Ensuite §3 (liste canonique des matières) et §6 (hero et bandeau mobile).
**Attention** : aucun signal GMC touché ; thème sur copie non publiée, publication par Hakim.

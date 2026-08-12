# Maison Noirmont — état courant

**Dernière vérification : 12/08/2026** (audit Shopify contradictoire — `journal/2026-08-11-audit-travail-codex.md`).
Ce fichier dit ce qui **est**, pas ce qu'il faut faire. Pour agir : [`TABLEAU.md`](TABLEAU.md).

## Chiffres

| | |
|---|---|
| Catalogue | **201 produits** — 96 actifs · 95 brouillons · 10 archivés |
| Évolution depuis le 09/08 | 199 → 201 : 10 archivages (3 doublons, le cadran Rolex, une montre arabe mixte, 3 brouillons stériles, 2 fiches incohérentes) et +2 cadrans arabes importés le 11/08 |
| Thème | publié le 09/08 par Hakim — les correctifs du 08/08 sont en ligne |
| Statut public | **boutique sous mot de passe** — rien n'est visible, aucun risque public actif |
| Collections | 10 créées le 09/08, **aucune publiée** sur le canal Online Store |
| Merchant Center | **non créé** — volontaire, tant que le CSS n'est pas arrêté |
| Mesure d'achat | **absente** (ni GA4 ni gtag) — bloquant avant toute dépense publicitaire |

## Ce qui va bien

- Les **interdits structurants ont tenu** sur la période 10-11/08 : aucun brouillon activé, aucune collection publiée, aucun prix ni `compare_at` modifié.
- **~85 visuels maison rattachés** le 10/08, tous en fin de galerie sur les fiches actives, `alt` FR, 2048×2048. Sur 12 images contrôlées en ligne, 11 sont conformes.
- Le catalogue a été **assaini** : doublons, cadran à verbatim Rolex et fiches incohérentes archivés ; la promesse fausse « tous les cadrans sont stériles » a été corrigée sans qu'on le demande.
- Un **pack de 7 politiques légales** est prêt à coller (le brief n'en demandait que 3), avec ses bloquants listés. Rien n'a été écrit sur Shopify : la permission manquante a été respectée.

## Ce qui ne va pas — par ordre de gravité

1. **Régression sur 14 fiches ACTIVES** (session du 12/08, `journal/` → `efficacite-extreme-2026-08-12`) : des médias ont été retirés jusqu'à ne laisser **qu'une seule image**. `trente-neuf-classique-cannelee` est passée de 12 à 1, `trente-neuf-duo-classique-bicolore` de 10 à 1, les deux aviateurs de 5 à 1. → **T-01**
2. **Une image non conforme est en ligne** : l'image unique de `trente-neuf-classique-cannelee`, datée du 12/08, **porte un lettrage cursif sur le cadran**. C'est l'infraction que toute la méthode vise à empêcher. → **T-02**
3. **Deux fiches importées avec des handles AliExpress bruts**, non rattachées à la collection `cadran-arabe`. → **T-04**
4. **La collection cadran arabe reste sous-peuplée** : le mot-clé porte 15 500 recherches/mois et le re-sourcing s'est arrêté à 3 cadrans sur les 4 à 8 visés. → **T-05**
5. `alt` génériques sur `cadran-sterile-lumineux-28-5`. → **T-08**

## Écarts de méthode constatés (corrigés depuis, à ne pas répéter)

Codex a **supprimé 78 photos fournisseur** et **déplacé un visuel maison en position 1** sur 17 brouillons, alors que le brief interdisait les deux. Exécution propre (URLs sauvegardées, ciblage strict, rollback possible) et dans le sens de l'objectif — mais hors mandat. Aucune fiche **active** n'a été dégradée les 10-11/08 ; la régression du point 1 vient de la session du 12/08.

**361 fichiers étaient restés hors GitHub** jusqu'au 12/08 au soir. Rappel : la source de vérité est GitHub, pas le disque.

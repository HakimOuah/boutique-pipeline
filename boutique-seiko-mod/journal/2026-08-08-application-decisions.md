---
type: journal
boutique: seiko-mod
date: 2026-08-08
nature: analyse
leviers: [autre]
titre: "NOIRMONT — application des 6 décisions de Hakim (08/08/2026)"
---

# NOIRMONT — application des 6 décisions de Hakim (08/08/2026)

Décisions prises par Hakim en session, appliquées le soir même. Sauvegardes dans `boutique-seiko-mod/backups/backup-prix-barres-2026-08-08/` et `boutique-seiko-mod/backups/backup-avis-2026-08-08/`.

## ⚠️ Deux corrections d'audit importantes

1. **La boutique n'est PAS publique.** Mon audit du plan de krakenisation indiquait « site en ligne, accessible sans mot de passe » : c'était **faux**. Vérification en requête anonyme : `maisonnoirmont.fr` redirige (302) vers `/password`. Ce que je voyais dans le navigateur venait de la **session preview** de Hakim. Conséquence : **aucun risque GMC/DGCCRF actif** ; tout le travail de conformité se fait avant publication, ce qui est la bonne séquence.
2. **Le thème publié (MAIN) est toujours `Helio` (204246548818)**, et `Maison Noirmont` (204248088914) reste **UNPUBLISHED**. Le travail de design est donc dans le thème non publié — ce qui a un bon côté (le connecteur peut y écrire, l'écriture sur MAIN étant bloquée) et un point ouvert : **il faudra publier ce thème** avant le lancement (action manuelle de Hakim : la publication de thème est bloquée par la politique du connecteur).

## Décision 1 — Retirer les avis ✅

Badge de démonstration identifié : bloc `reviews_badge_efW9wU` (style Trustpilot, « Excellent · 4,5 · 1340 avis ») dans la section `image_banner_VXNP89` du template `templates/index.json` du thème Maison Noirmont. **Ce n'était pas une app d'avis** mais un bloc de thème.
Action : ajout de `"disabled": true` sur le bloc (même convention que le groupe « Avis client » déjà désactivé) — réversible en retirant une ligne. Sauvegarde avant/après dans `boutique-seiko-mod/backups/backup-avis-2026-08-08/`.

## Décision 2 — Retirer les prix barrés ✅

Constat : **104 produits / 931 variantes** portaient un `compareAtPrice` (100 % du catalogue) — conséquence de l'échelle de prix appliquée le 25/07, et tueur GMC n°1 (prix de référence non justifiable sur une boutique à 0 vente).
Action : `compareAtPrice` mis à `null` sur les 931 variantes. Les prix de vente sont **inchangés**.
Sauvegarde complète des valeurs d'origine : `boutique-seiko-mod/backups/backup-prix-barres-2026-08-08/export-variants.jsonl` (export bulk Shopify horodaté) — restauration possible à l'identique.
Effet attendu : disparition des badges « En promotion » qui découlaient des prix barrés (le bilan du 25/07 les signalait sur presque toutes les cartes).

## Décision 3 — Commande test ✅ (reçue et conforme)

Hakim confirme la réception et la conformité. **Le chemin critique du lancement est levé** : la vérité produit est établie. À documenter dans le dossier fournisseur (délai réel constaté, qualité, stérilité du cadran) pour servir de preuve aux promesses du site.

## Décision 4 — Retirer/masquer les sigles ✅ (déjà conforme) + 1 vigilance

Vérification faite : les **12 variantes siglées** (logo de marque tierce) sont **toutes** dans le produit « Voyageur — GMT automatique » (`10977448657234`), qui est en **DRAFT** (hors ligne) avec `inventoryPolicy: DENY` et stock 0 sur chacune. Elles sont donc doublement masquées — la décision est déjà satisfaite, aucune action destructrice nécessaire.

**⚠️ Vigilance à trancher par Hakim** : les deux fiches **actives** issues du découpage — « Voyageur Or — GMT bracelet 3 maillons » (`10980078780754`) et « Voyageur Or — GMT bracelet Président » (`10980079042898`) — reprennent exactement les combinaisons des variantes siglées (DG3804 / NH34 · fond verre/acier). Leurs **visuels sont stériles** (contrôle visuel effectué : cadran noir sans aucun logo), donc rien de siglé n'est affiché. Reste à confirmer que leur **mapping DSers ne pointe pas vers la référence fournisseur siglée** — sinon le client recevrait une montre logotée alors que la fiche montre un cadran vierge (double problème : contrefaçon + promesse non tenue). Contrôle impossible côté API (DSers exige une connexion) : **à vérifier manuellement dans DSers**.

## Vérifications d'exécution (preuves, 08/08 18h05)

- **Prix barrés** : scan paginé complet des **935 variantes** de la boutique → **0 variante avec `compareAtPrice` non nul**. (Note de méthode : `compare_at_price` n'est pas un champ filtrable sur `productVariants` — un `query:"compare_at_price:>0"` est ignoré silencieusement et renvoie tout le catalogue ; seul le scan paginé fait preuve.)
- **Avis** : `themeFilesUpsert` renvoie `upsertedThemeFiles: []` **sans erreur** sur ce thème — c'est le rejet silencieux déjà connu, et ici un **faux négatif** : l'écriture a bien abouti. Preuve par empreinte du fichier distant `templates/index.json` — avant : md5 `1ccc270f…` / 91 705 o (identique à `index.json.avant`) ; après : md5 `57ecffa8…` / 91 731 o / `updatedAt 2026-08-08T16:05:17Z` = empreinte exacte de `index.json.apres`. Le thème MAIN `Helio` est resté intact (`updatedAt` toujours 2026-07-24).
- **Leçon versée au campement** : sur ce thème, ne jamais conclure d'un `upsertedThemeFiles` vide ; vérifier par **empreinte du fichier distant** (plus fort qu'un grep, et sans rapatrier 91 Ko). Transporter les gros corps via `stagedUploadsCreate` + `body:{type:URL}` plutôt qu'en `TEXT` (risque de troncature à la retranscription).
- **Précision de forme** : le commit `09c42c5` a été poussé pendant que l'écriture du thème était encore en cours — il documentait les décisions, pas leur exécution constatée. Les preuves ci-dessus la constatent.

## Décision 5 — Budget publicitaire : 30 €/jour

Noté pour la phase 6. Conséquence méthode (corpus Kraken) : à 30 €/j, le **CPC doit rester cohérent — 0,16 à 0,25 €**, ce qui tombe bien puisque le marché seiko mod est à ~0,22 €. Objectif de phase inchangé : **15 conversions** pour débloquer le tROAS, sans chercher la rentabilité pendant cette phase.

## Décision 6 — GO sur le sourcing « Pièces & Mod »

Validé. Le sourcing suivra le **gate v3** (`codex-chasse-clusters/CONSIGNES-SOURCING-KRAKEN.md`) : 10-20 produits par sous-catégorie, ordre 80/20, preuve au niveau collection. Cible : passer de 92 à 200+ fiches, priorité aux **cadrans arabes** (~15 500/mois, personne au-dessus de la 4ᵉ position) et au vocabulaire **seiko mod** (38 690/mois).

## Ce qui reste à faire (mis à jour)

| # | Action | Qui |
|---|---|---|
| 1 | **Publier le thème « Maison Noirmont »** (bloqué par la politique du connecteur) | Hakim, dans l'admin |
| 2 | Vérifier le mapping DSers des 2 fiches « Voyageur Or » | Hakim / DSers |
| 3 | Retirer le mot de passe boutique au moment du lancement | Hakim |
| 4 | Reliquats du bilan 25/07 : 88 visuels de variantes, 13 accessoires à importer via DSers, fiche « chiffres romains » (corriger l'image, pas le texte), cartes cadeaux, suppression du thème fork `204329288018` | à planifier |
| 5 | Audit anti-misrepresentation complet (délais, footer, pages légales du checkout, mentions VK63 méca-quartz) | prochaine session |
| 6 | Sourcing Pièces & Mod + arborescence cadran arabe / seiko mod | prochaine session |

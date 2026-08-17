# Nuit du 17/08/2026 — repeuplement + T-32

Boutique **Maison Noirmont** (`v42pzp-h4`). Pas Tuftéo. Aucune activation. Aucun GMC. Aucun `fileDelete`.

## Ce qui a été écrit

### Accueil (MAIN `205451100498`)

Phrase cassée « chaque commande est vérifiée avant l'envoi » → « chaque commande, vérifiée avant l'envoi » dans `templates/index.json`. Vérifié live.

### T-63 — 20 brouillons de repeuplement

Descriptions FR + SEO + libellés de variante, statut forcé `DRAFT`. Specs uniquement depuis `journal/2026-08-15-sourcing-repeuplement.md`. 108 `alt` réécrits : plus de cadratin, vues coffret/malette avec « montres non incluses ». 3 titres SEO distincts du titre produit.

Preuve : 20/20 `DRAFT`, 0 « Seiko » / 0 « montre de plongée » / 0 cadratin dans les descriptions.

### T-32 — SKU AliExpress

Scan paginé **avant** : 3 029 variantes, 2 071 SKU AliExpress + 3 `<none>`, 0 sur les fiches ACTIVE.

Écriture : `productVariantsBulkUpdate` via `inventoryItem.sku` (le champ `sku` n'existe plus sur `ProductVariantsBulkInput`). 96/96 fiches, 0 `userErrors`, statuts inchangés.

Scan paginé **après** : 3 029 variantes, **0** `:` / `#` / « no logo », **3 025** `NOIR-<TRI>-<nnn>`, 4 vides = carte cadeau, 883 ACTIVE / 1 998 DRAFT / 148 ARCHIVED.

Correspondance : `backups/2026-08-17-sku-t32/correspondance-ancien-nouveau.jsonl`.

## Ce qui n'a pas bougé

- Les 20 restent DRAFT.
- T-07 (photos brutes des autres brouillons).
- T-60 (coffret aluminium 99,90 vs 149 €) : attend Hakim.
- T-59 (4 Unmapped DSers) : l'interface ne persiste pas.
- Politiques encore datées du 10/08 : `write_legal_policies` absent.
- GMC Noirmont : ne pas créer.

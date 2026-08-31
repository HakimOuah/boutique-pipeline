# Lumière Matière — pré-soumission GMC (31/08/2026)

Relu live le 31/08 soir. CLI Connector ré-authentifié (`contact@lumierematiere.fr`). **Ne pas supprimer l’app Shopify CLI Connector.**

## Chez Hakim — encore ouvert

### Téléphone boutique (JSON-LD encore faux)

**Paramètres → Général → Coordonnées de la boutique → Téléphone**

| Champ | Live (JSON-LD home) | Cible |
|---|---|---|
| Adresse | 47 Rue Vivienne, Paris, 75002 | OK — Saint-Prix parti |
| Téléphone | `0756916084` | `+33 7 56 82 80 94` |

Ne pas toucher aux pages mentions / CGV / footer : ils disent déjà Paris et le bon numéro.

### Publier le thème — après preview

Copie **non publiée** : `LM GMC 2026-08-31` · `186897498448`

- Preview (être connecté à l’admin) : https://lumierematiere.fr/?preview_theme_id=186897498448
- PDP test : https://lumierematiere.fr/products/suspension-verre-538307?preview_theme_id=186897498448
- Éditeur : https://nzefxg-gg.myshopify.com/admin/themes/186897498448/editor

Sur le preview, contrôler : 0 `themefullstack`, 0 `200000531` dans le JSON-LD, adresse Paris. Puis **Hakim publie**. Le MAIN n’a pas été touché.

## Déjà live (MAIN, pas de publication thème)

| Point | Live 31/08 soir |
|---|---|
| Adresse JSON-LD | 47 Rue Vivienne, Paris, 75002 |
| Téléphone JSON-LD | encore `0756916084` |
| JSON-LD `sameAs` themefullstack | encore 3 URLs sur le MAIN |
| SKU AE dans JSON-LD PDP | encore `200000531` sur le MAIN (corrigé sur la copie) |
| Alt « vue Codex N » | 0 restants (35/35 corrigés) |
| CGV §4 Klarna + CB + Maestro | live |
| FAQ « garantie de 30 jours » | remplacée par retour 30 j |
| Collections menu < 5 publics | inchangé — Hakim tranche, on ne publie aucun brouillon |
| Délais 7–18 / identité OH Ventures / 0 avis / 0 prix barré public | inchangés |

## Copie thème (non publiée)

- `config/settings_data.json` : `facebook_url`, `youtube_url`, `linkedin_url`, `instagram_url` = `""` (sinon défauts schéma themefullstack).
- `snippets/organization-schema.liquid` : ignore toute URL qui contient `themefullstack`.
- `snippets/meta-tags.liquid` : JSON-LD Product maison, **sans clé `sku`**. Les SKU variantes admin restent intacts (mapping DSers).

## Encore à faire (après preview / téléphone)

- §3.2 : 9 fichiers `S….webp` sur `applique-murale-pierre-metal-147598` — restage, pas `fileDelete`.
- §6.1 : `compareAtPrice` seulement sur 3 dumps DSers **DRAFT** anglais (prix = barré). Laisser. `write_products` interdit.
- 7–10 j de repos, commande test, puis GMC via Google & YouTube, pas d’ads, une review.

## Hors périmètre (inchangé)

TVA `taxable: false` vs mentions FR55… — décision comptable. Publication thème / brouillons — Hakim. SKU variantes — intouchables.

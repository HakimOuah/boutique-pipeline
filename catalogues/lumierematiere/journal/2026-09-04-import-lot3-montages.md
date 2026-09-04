# Import du lot 3 — les montages fournisseur remplacés

Date : **04/09/2026 (soir)** · Boutique : **Lumière Matière**
Brief : `briefs/2026-09-04-codex-lot3-montages.md` · Livraison Codex : 16 images, QA `PASS_TECHNIQUE`.
Suite de `journal/2026-09-04-arbitrages-titres-variantes.md`.

**16 images importées, 5 montages supprimés, 3 variantes rattachées, 2 `alt` génériques repris.**
Contrôle : 52 produits / 158 variantes, SKU DSers intacts, aucune fiche sans image.

## Contrôle visuel avant import — le critère qui avait manqué en août

La planche `qa-montages.jpg` a été relue image par image contre la règle du lot :
**une image = un seul luminaire**. 16/16 conformes.

- `272937` — les huit vues montrent un **plafonnier à fixation directe** : rosace noire, dôme en
  corde tressée, douille E27 apparente. Pas de câble pendant, pas de trio, pas d'applique. Les
  trois modèles sont visuellement distincts et conformes au brief : **A** rosace noire / corde
  beige clair, **B** rosace **blanche** / corde crème, **C** rosace noire / **jute brune** au
  tressage plus grossier.
- `560098` — suspension **simple**, un seul abat-jour, un seul cordon torsadé, monture laiton.
- `147607` — galet travertin seul, tête noyer.

## Ce qui a été appliqué

| Fiche | Avant | Après | Image de flux |
|---|---:|---:|---|
| `suspension-rotin-272937` | 5 montages | **8** (g1–g5 + 3 packshots de modèle) | `lm3-272937-g1.jpg` |
| `suspension-deco-blanc-560098` | 2 packshots | **7** (g1–g5 + a-g1, b-g1) | `lm3-560098-g1.jpg` |
| `suspension-effet-pierre-led-147607` | 5 | **8** (g1, g2, g3, g4, g5 + 3 formes) | `lm3-147607-g1.jpg` |

Les cinq montages de `272937` — ceux qui montraient cinq configurations dont aucune n'était vendue —
**sont supprimés**. C'était le dernier reste du problème ouvert le matin.

Rattachements de variante sur `272937` : `Modèle A` → `modele-a-g1`, `Modèle B` → `modele-b-g1`,
`Modèle C` → `modele-c-g1`. Faits par `productVariantAppendMedia`, qui n'écrit qu'un média —
aucune mutation de variante, donc **aucun risque sur les `sku_attr` DSers**.

`alt` rédigés à l'import pour les 16, plus reprise des deux derniers `alt` génériques de `147607`
(« autre vue », « autre cadrage ») hérités de la passe d'août.

## Le détail technique qui a failli coûter cher

**Les nouveaux fichiers de `272937` portaient exactement les mêmes noms que les montages en place**
(`suspension-rotin-272937-g1.jpg` … `-g5.jpg`). Ordonner ou supprimer par nom de fichier aurait
visé les mauvais médias, et rien ne l'aurait signalé : la fiche serait restée pleine, avec les
montages en tête. Tout le pipeline a donc été bâti sur les **identifiants de média**, jamais sur
les noms — et les fichiers ont été déposés sous des noms préfixés `lm3-` pour lever l'ambiguïté
côté CDN. Même famille de piège que le mapping SKU du matin.

## Deux blocages d'accès rencontrés

1. **`SHOPIFY_LUMIERE_MATIERE_TOKEN` du `.env` ne porte que le scope `read_reports`**
   (vérifié par `currentAppInstallation.accessScopes`) : inutilisable pour lire ou écrire un
   produit. `ETAT.md` le signalait déjà « à renouveler » ; c'est maintenant chiffré.
   Contournement : mutations par le connecteur MCP, transfert des fichiers par `PUT curl` sur les
   URL pré-signées — qui, elles, ne demandent aucun token.
2. **`stagedUploadsCreate` en `httpMethod: POST`** renvoie une politique signée et huit paramètres
   par fichier, soit une réponse énorme pour 16 images. En **`PUT`**, la signature tient dans la
   query string et la réponse fait un dixième de la taille. À réutiliser par défaut.

Le script `scripts/importer-lot3-montages-20260904.py` et son plan
`scripts/lot3-import-plan.json` sont versionnés : le plan documente exactement ce qui a été
appliqué, le script deviendra directement exécutable dès qu'un token correct sera en place.

## Réponses de Codex aux deux questions ouvertes

- **`suspension-deco-led-837156`** — les variantes à suffixe « 2 » sont **un autre abat-jour**
  (H 9 cm contre H 6,5 cm, toutes Ø 20 cm). Ce ne sont pas des doublons : rien à supprimer, mais
  les libellés « Céladon vert » / « Céladon vert 2 » ne disent pas la différence et restent à revoir.
- **`suspension-effet-pierre-led-338324`** — le modèle A reste **introuvable au DOM** après une
  dernière passe. Non déduit par élimination. Les trois variantes A gardent la vue générique.

## Suites

1. **`607504`** : le point G du brief est débloqué depuis le renommage — schéma coté + packshot
   noir à produire (2 visuels).
2. **`272937`** : les libellés restent des codes aveugles (`Modèle A / B / C`) alors que les trois
   images sont maintenant distinctes. Renommage possible en « Monture noire, corde claire » /
   « Monture blanche » / « Jute brune » — **décision de Hakim**, comme pour `607504`.
3. **`837156`** : libellés à revoir sur la hauteur d'abat-jour (6,5 vs 9 cm).
4. **`147607`** : trancher avec ou sans ampoule (SKU `Warm light 3000K` contre corps de fiche E27).

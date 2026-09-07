# 07/09/2026 — `934110` : 2 visuels livrés et importés, la fiche est complète

Livraison Codex : `livraisons-visuels-codex/2026-09-07-934110/`.
Brief : `briefs/2026-09-07-codex-934110-visuels.md`.

---

## Contrôle avant import

`production.json` est complet et discipliné : référence source et SHA-256 pour chaque
fichier, comptes de tubes attendus **et** observés, prompt de génération, preuve que les
deux références « deux tubes » sont identiques au SHA-256 près, mention explicite
« aucune différence 3000 K / 6000 K fabriquée ».

**Comptage refait moi-même à pleine résolution**, comme depuis `183789` :

- `lm5-934110-un-tube.jpg` — **1 tube**, travertin beige, câble brun, rosace simple, éteint.
- `lm5-934110-deux-tubes.jpg` — **2 tubes** à hauteurs différentes, **une seule rosace ronde
  commune**, même matière, éteint.

Ni texte, ni cote, ni watermark, ni logo, ni main. 2048 × 2048. Mise en scène cohérente
avec le catalogue. **2/2 conformes.**

## Import

Téléversement par URL pré-signée en `PUT` (HTTP 200 × 2), puis `productCreateMedia` avec
des `alt` rédigés à l'import qui portent les cotes.

**Rattachement en deux temps**, jamais dans le même appel — la leçon du lot 4 A1 :
détachement du média partagé sur les 3 variantes → **contrôle que les 3 sont bien à zéro
média** → attachement. Résultat vérifié :

| Variante | SKU fournisseur | Image |
|---|---|---|
| `Un tube` | `200000531:193#Yellow Travertine` | `lm5-934110-un-tube.jpg` |
| `Deux tubes · blanc chaud 3000 K` | `200000531:173#3000k-warm white` | `lm5-934110-deux-tubes.jpg` |
| `Deux tubes · blanc froid 6000 K` | `200000531:175#6000k-cold white` | `lm5-934110-deux-tubes.jpg` |

**Une image pour deux variantes, volontairement** : leurs références fournisseur sont
identiques au SHA-256 près et elles ne diffèrent que par la teinte de la LED, invisible
sur un produit éteint. Fabriquer une troisième image aurait inventé une différence.

La fiche passe de **5 médias à 7**. Basculer d'un modèle à l'autre change enfin la photo.

## Fausse alerte levée sur la galerie

Les images fournisseur brutes `03.jpg` et `04.jpg` montrent un tube **blanc marbré**, pas
du travertin — j'ai craint que la galerie live vende une teinte absente du catalogue.
**Contrôle fait sur `g1`, `g3` et `g5` téléchargés depuis le CDN Shopify : tube travertin
beige sur les trois.** La galerie avait déjà été régénérée. Rien à corriger.

**Règle : contrôler la galerie sur le CDN de la boutique, jamais sur le dossier source
fournisseur — les deux ne montrent pas la même chose.**

## Contrôle final en ligne

`lm5-934110-un-tube.jpg` et `lm5-934110-deux-tubes.jpg` présents sur la page publique,
les 3 libellés en place, **plus aucune occurrence de `Un tube · travertin`**.
51 produits, 158 variantes, SKU DSers intacts.

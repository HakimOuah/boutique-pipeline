# Brief Codex — lot 3 : remplacer les montages fournisseur

Date : **04/09/2026 (soir)** · Boutique : **Lumière Matière** (`lumierematiere.fr`) · thème live
`LM UX 2026-09-04`. Suite de `2026-09-04-codex-variantes-formes.md` (lot 2, 34/34 livrés et
importés). Constat source : `shopify/../journal/2026-09-04-images-principales-montages.md`.

## Pourquoi ce lot

La passe visuelle d'août a composé les `g1`–`g5` de trois fiches **à partir d'une planche
catalogue du fournisseur** au lieu d'isoler la référence vendue. Résultat : l'image principale —
celle qui part dans le flux Google Shopping — montre plusieurs luminaires, dont des
configurations qui ne sont pas vendues dans la fiche.

C'est un **collage**, explicitement proscrit par la checklist GMC, doublé d'une
misrepresentation : le client voit une applique murale ou une suspension double qu'il ne peut pas
acheter sur cette fiche.

Deux des trois fiches ont été **provisoirement** corrigées en remontant des packshots propres en
tête de galerie. Les montages sont toujours présents plus bas et doivent être remplacés.

## Direction artistique — inchangée depuis le 24/08

| | |
|---|---|
| Fond | papier `#F6F3EC`, uni |
| Lumière | chaude |
| Type | packshot objet |
| Format | JPEG RGB **2048 × 2048**, sans compression visible |
| Interdits | texte, cote, logo, badge, filigrane, main, visage, décor de pièce — **et désormais : plus d'un luminaire dans le cadre** |

**Règle nouvelle et non négociable de ce lot : une image = un seul luminaire.** Si la source
montre plusieurs configurations, isoler celle qui correspond au SKU vendu et ignorer les autres.

### Slots des vues produit (convention d'août)

`g1-hero-allume` · `g2-silhouette-angle-matiere` · `g3-macro-matiere` · `g4-lifestyle` ·
`g5-qualite-lumiere`. Nommage `{handle}-g1.jpg` … `-g5.jpg`.
Packshots de variante : `{handle}-{slug}-g1.jpg`, slot `g1-variante`.

### Livraison

`catalogues/lumierematiere/livraisons-visuels-codex/montages-2026-09-04/{handle}/`
Un `manifeste.json` par handle, schéma habituel, avec pour chaque image le **SKU ou l'identifiant
d'option** qu'elle sert. Aucune action Shopify ni DSers. SKU intouchables.

### Les références par variante existent déjà

Le scraping DOM du 04/09 a produit `sources-par-handle/{handle}/variantes-20260904/` avec une
image par identifiant d'option et un `preuves-dom.json` horodaté. **C'est la source à utiliser** —
elle est fiable et elle a l'identifiant, pas le libellé. Attention : ces références portent des
cotes et du texte incrustés, elles ne peuvent pas être publiées telles quelles.

---

## A. `suspension-rotin-272937` — PRIORITÉ 1, tout est à refaire

**8 images : 5 vues produit + 3 packshots de variante.**

Le `g1` actuel montre cinq configurations (suspension simple, applique murale, trio à rosace
ronde, trio sur barre linéaire). **Aucune n'est vendue dans cette fiche.**

Les trois SKU vendus sont des **plafonniers** — montage direct au plafond, sans câble pendant —
Ø 16 cm, hauteur totale 17 cm, abat-jour 17 cm de haut dont 12 cm de corde tressée, rosace 10 cm,
douille E27 × 1.

| Variante boutique | SKU | Référence | Ce qu'elle montre |
|---|---|---|---|
| Modèle A | `200000531:193#A1` | `variantes-20260904/200000531-193.jpg` | monture et rosace **noires**, corde papier **beige clair** |
| Modèle B | `200000531:1052#B1` | `variantes-20260904/200000531-1052.jpg` | monture et rosace **blanches**, corde **crème** |
| Modèle C | `200000531:100018786#C1` | `variantes-20260904/200000531-100018786.jpg` | monture et rosace **noires**, **corde de jute brune**, tressage plus grossier |

Les cinq vues `g1`–`g5` sont à recomposer **sur le modèle A** (référence canonique), en plafonnier
seul. Ne pas représenter de câble, ne pas représenter de trio, ne pas représenter d'applique.

## B. `suspension-deco-blanc-560098` — 5 vues produit

Les cinq vues actuelles montrent une suspension **double** (deux abat-jour sur une rosace
commune). Les deux SKU vendus sont des suspensions **simples** : Ø 19,5 cm, abat-jour H 16 cm,
douille E27 × 1, cordon torsadé 1,5 m réglable, monture laiton avec interrupteur à molette.

Références : `variantes-20260904/200000531-193.jpg` (A, motif floral bleu) et
`200000531-173.jpg` (B, rayures bleues et brunes).

Recomposer `g1`–`g5` **sur la variante A, en simple**. Les deux packshots de variante existent
déjà et sont bons — ne pas les refaire.

## C. `suspension-effet-pierre-led-147607` — 3 vues produit

`g1`, `g2` et `g5` montrent 10 à 12 suspensions travertin dans le même cadre. `g3` et `g4` sont
mono-produit et **restent valables**.

Recomposer les trois, sur la **forme A** (galet bas, tête noyer), en un seul luminaire.
Les trois packshots de forme existent déjà et sont bons.

## D. `suspension-effet-pierre-led-338324` — modèle A, dernière tentative

Le lot 2 a livré B, C et D. Le modèle A (`200000531:193`) n'a pas été trouvé dans le sélecteur
fournisseur du 04/09, et **tu as eu raison de ne pas le déduire par élimination**. Le dossier
`variantes-20260904/` ne contient effectivement que 173, 175 et 365458.

Refaire une passe DOM sur la PDP. Si l'identifiant reste absent : **le déclarer définitivement
introuvable dans le manifeste** et ne rien produire. Les trois variantes A garderont la vue
générique.

## E. `suspension-deco-led-837156` — scraping manquant

Seule fiche à variantes non scrapée le 04/09. Ses valeurs `Céladon vert` / `Céladon vert 2` et
`Céladon bleu poudré` / `Céladon bleu poudré 2` portent des SKU fournisseur distincts
(`…365458` vs `…193`, `…175` vs `…173`) mais aucune différence lisible.

Scraper les quatre références et **répondre à une seule question** : les « 2 » sont-elles un autre
objet, ou le même ? Aucune image à produire tant que la réponse n'est pas connue.

## F. `suspension-rotin-897170` — RÉSOLU, aucune action

Question fermée le 04/09 : les références `200000531-193.jpg` et `200000531-29.jpg` (les deux
« Ø 50 cm · rotin ») sont **rigoureusement identiques** — même corolle, même 50 cm, même mention
« 1.2m ~1.4m Adjustable », même avertissement sur le rotin qui jaunit. Le fournisseur a deux
entrées de SKU pour un seul article.

**Il n'y a rien à générer et rien à distinguer.** C'est un doublon côté fournisseur, et son sort
(fusion, suppression d'une variante) est une décision Shopify/DSers de Hakim, pas un sujet visuel.

## G. `suspension-rotin-607504` — en attente d'arbitrage

Cotes prouvées au lot 2 : `2550` = Ø 25 × H 50 · `4040` = Ø 40 × H 40 · `4019` = Ø 40 × H 19 ·
`4040BK` = Ø 40 × H 40 **noir**. Le doublon apparent « 40 × 40 cm » est donc naturel vs noir.
Références disponibles : `variantes-20260904/200000795-{193,367,175,10}.jpg`.

Le schéma coté et le packshot « noir » ne se produisent **qu'après** le renommage des libellés
par Hakim. Ne rien faire avant.

---

## Récapitulatif

| Lot | Fiche | À produire | Statut |
|---|---|---:|---|
| A | `suspension-rotin-272937` | **8** (5 vues + 3 variantes) | à faire |
| B | `suspension-deco-blanc-560098` | **5** vues | à faire |
| C | `suspension-effet-pierre-led-147607` | **3** vues (g1, g2, g5) | à faire |
| D | `suspension-effet-pierre-led-338324` | 0 à 1 | re-scraper, puis trancher |
| E | `suspension-deco-led-837156` | 0 | scraper et répondre |
| F | `suspension-rotin-897170` | 0 | résolu, ne rien faire |
| G | `suspension-rotin-607504` | 0 pour l'instant | attendre l'arbitrage |

**16 images au maximum.**

## Contrôle attendu

Une planche `qa-montages.jpg` de toutes les images livrées, et dans chaque manifeste la mention
explicite : *« un seul luminaire dans le cadre »*. C'est le seul critère qui a manqué en août.

# Import du solde du lot 4 — A2, B, et une fiche entièrement fausse

Date : **04/09/2026 (nuit)** · Boutique : **Lumière Matière**
Livraison Codex : `livraisons-visuels-codex/couverture-2026-09-05/` — **27 visuels** (17 packshots A2
+ 10 schémas B), plus les deux réponses C sans image. Compte rendu Codex :
`journal/2026-09-05-lot4-suite-couverture.md`.

**27 images importées, 17 variantes rattachées, 8 médias supprimés, 1 hero remplacé.**
Contrôle : 52 produits / 158 variantes / SKU DSers intacts.

## La trouvaille : `183789` était fausse de bout en bout

Codex a signalé que les deux packshots de variante de `plafonnier-led-led-183789` montraient
**sept palets** alors que la fiche vend du **5** et du **6**. Vérification faite : c'est exact, et
**c'est pire que ça** — les cinq vues de galerie `g1`–`g5` montrent elles aussi sept palets,
**hero compris**, c'est-à-dire l'image qui part dans le flux Google Shopping.

Sept images sur sept étaient fausses. Le client voyait un luminaire à sept points lumineux qui
n'existe dans aucune variante.

**Fait** : les 7 médias supprimés, les 2 nouveaux packshots à 5 palets importés et rattachés aux
variantes `5 lumières · Gris` et `5 lumières · Blanc`. Le hero est désormais un produit
réellement vendu. La fiche est passée de 7 images fausses à **2 images vraies**.

**Reste** : les deux variantes à 6 lumières n'ont plus d'image attachée (elles retombent sur le
hero à 5 palets), et la galerie est réduite à deux vues. Cette fiche demande **7 visuels** —
`g1`–`g5` régénérés + les packshots `gris 6` (`366`) et `blanc 6` (`10`) — et non les 2 que
Codex avait demandé l'autorisation de produire. Le plafond de 40 du brief est à lever pour elle.

## A2 — 17 packshots, le nombre de lumières enfin montré

| Fiche | Nouveaux | Conservé |
|---|---|---|
| `plafonnier-led-992600` | noir/blanc/doré × 4 et 8 boules | les trois finitions à 6 |
| `suspension-metal-noir-dore-361680` | noir/doré × 4 et 8 bras | noir et doré à 6 |
| `lustre-statement-led-noir-950316` | 4 et 8 boules sputnik | 6 |
| `plafonnier-led-led-183789` | gris 5, blanc 5 | rien — voir ci-dessus |
| `lustre-anneau-led-led-717226` · `625575` | 4 anneaux | 6 anneaux |
| `lustre-anneau-led-led-134962` | blanc 6 anneaux | blanc 5, noir 5, doré 5 |

**Comptages recontrôlés à pleine résolution** avant import — Codex précise lui-même qu'il ne
prétend pas les avoir détectés automatiquement. `361680-noir-4` : 4 bougies, deux par côté.
`992600-noir-4` : 4 ampoules. Justes.

## B — 10 schémas cotés

`588683` · `795468` · `246282` · `655008` · `377816` · `761433` · `330664` · `607504` ·
`837156` · `630923`. Une silhouette de référence, un tableau des tailles, des barres
comparatives à échelle commune, et les hauteurs non documentées notées « — » plutôt que déduites.
**Aucune juxtaposition de plusieurs luminaires** : la règle du lot tient aussi pour les schémas.

Le schéma de `630923` remplace celui d'août, qui ne distinguait pas plafonnier et suspension.

## C — les deux réponses

**`suspension-bois-led-934110`** — la réponse est plus gênante que la question. `193#Yellow
Travertine` montre **un tube**, `173` et `175` montrent **deux tubes sur une rosace commune**, et
ces deux références sont **rigoureusement identiques, SHA-256 compris**. Le second axe n'a qu'une
valeur, `3000K warm light`, ce qui **contredit** la variante annoncée à 6000 K. Ce n'est donc pas
une grille matière × température : c'est un mélange de matière, de montage simple/double et de
température, dont la valeur réellement livrée est inconnue. **Aucun visuel produit, aucun libellé
touché** — il faut une confirmation fournisseur avant de normaliser quoi que ce soit.

**`suspension-effet-pierre-092465`** — correspondance confirmée (`200006153` = Pierre claire,
tête bois clair ; `365458` = Brun, tête bois foncé). Les deux packshots en place sont justes,
rien à refaire.

## État de la couverture après cette passe

Toute variante qui diffère visuellement porte désormais **sa propre** image. Les seules qui en
partagent une sont celles où **seule la taille change** — et elles ont maintenant leur schéma
coté. Exceptions restantes, toutes documentées : les deux 6 lumières de `183789`, les trois
variantes de `934110` (bloquées sur la question fournisseur) et `073999` / `435189`, où l'axe
est une température ou la présence d'une ampoule.

## Suites

1. **`183789`** : 7 visuels à produire, plafond de 40 à lever. Priorité — la fiche est réduite à
   deux images.
2. **`934110`** : confirmation fournisseur avant tout libellé ou visuel.
3. **`193329` / `338324`** : toujours le même article à 199 € sur deux listings. Décision Hakim.

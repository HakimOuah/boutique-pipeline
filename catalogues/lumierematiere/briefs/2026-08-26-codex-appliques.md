# Brief Codex — galeries produit des appliques murales (Lumière Matière)

Date : 26/08/2026. Boutique : **Lumière Matière** (`lumierematiere.fr`).

**Commande : 5 handles → 25 JPEG produit, plus 1 cover de collection. Total 26 visuels.**

## Contexte

Nous venons d’ouvrir le rayon **appliques murales**, le premier trou de catalogue identifié
chez Lustria (20,8 % de leur trafic, zéro chez nous). Les cinq fiches sont en ligne, mais
elles portent encore les **photos AliExpress brutes** : fonds gris, textes chinois incrustés,
cotes, mains, décors de chambre d’hôtel. C’est le seul rayon de la boutique qui n’est pas au
style `g1`.

Les 121 fiches existantes ont déjà leurs 5 vues Codex. Ces 5 appliques doivent rentrer dans
le même moule, sans exception.

## Ce qui est demandé

Pour chaque handle : **5 vues**, `g1` à `g5`, exactement comme la livraison catalogue.

- Source : `catalogues/lumierematiere/sources-par-handle/{handle}/01.jpg` et suivantes
- Sortie : `catalogues/lumierematiere/livraisons-visuels-codex/produits/{handle}/{handle}-g{1..5}.jpg`
- Format : JPEG RGB, **2048 × 2048**, sans compression visible
- Accompagné de `manifeste.json` et `compte-rendu.md`, comme les 121 autres handles
- Fond papier `#F6F3EC`. Lumière chaude. Packshot objet.

### Le cadrage, pour une applique

C’est le point nouveau. Les 121 fiches livrées sont des **suspensions** : objet en l’air,
câble visible, vu de face. Une applique est **plaquée contre un mur**, elle n’a pas de câble
apparent et son intérêt se joue sur la lumière rasante qu’elle laisse sur la cloison.

- `g1` — trois quarts, applique posée sur un pan de mur papier `#F6F3EC`, **allumée**, halo
  visible au-dessus et au-dessous. C’est la vue qui vend : on doit voir la lumière glisser sur
  le mur, pas seulement l’objet.
- `g2` — face stricte, **éteinte**, pour lire la forme et la matière.
- `g3` — détail matière à 40 cm : le grain de la pierre, la tranche du travertin, la jonction
  bois ou métal. Aucune vue d’ensemble.
- `g4` — profil, pour montrer l’épaisseur et le déport par rapport au mur.
- `g5` — mise en situation sobre : le même mur papier, allumée, cadrage plus large, sans
  meuble reconnaissable ni objet de décor. Pas de chambre d’hôtel, pas de plante, pas de livre.

### Interdits

Aucun texte, logo, badge, cote, filigrane, main, visage, corps, marque fournisseur.
Ne pas inventer une matière absente. Ne pas ajouter de câble apparent, ne pas ajouter
d’interrupteur là où il n’y en a pas, ne pas changer le nombre de têtes lumineuses.

## Liste

### 1. `applique-murale-pierre-588683` — LM-122

**Applique murale galet beige pierre, chambre** · 119 à 159 € · 6 sources

Galet de pierre beige à ocre, plein, posé à plat. La LED est **derrière** la pierre : elle
éclaire vers le haut et vers le bas, la source n’est jamais visible. Trois diamètres au
catalogue (20, 25, 30 cm), mais **une seule galerie** : ne pas décliner par taille.

Point d’attention : les sources montrent un halo jaune franc. Rester sur un blanc chaud
3000 K, pas sur un jaune saturé.

### 2. `applique-liseuse-pierre-311650` — LM-123

**Applique murale liseuse pierre et bois, chambre** · 119 € · 8 sources

Disque de pierre monté sur un **bras de bois qui pivote**, avec un **interrupteur sur le
corps**. Ce sont les deux détails qui justifient le prix : le `g3` doit montrer l’interrupteur
et l’axe de rotation, pas le grain de la pierre.

Deux finitions en boutique, **Bois clair** et **Noyer**. Le `g1` est en **Noyer**. Prévoir en
plus une vue teinte selon la règle des variantes : `applique-liseuse-pierre-311650-bois-clair-g1.jpg`.

### 3. `applique-double-travertin-474088` — LM-124

**Applique murale double travertin, 2 lumières** · 129 € · 12 sources

**Deux** têtes rondes en travertin sur une même platine, chacune orientable. Le `g1` doit les
montrer orientées différemment, l’une vers le bas, l’autre vers le haut : c’est l’argument.
Ne jamais rendre une version à une seule tête.

Les sources fournisseur la montrent au-dessus d’un lavabo. **Ne pas reprendre ce décor** : nous
ne vendons pas cette applique pour une salle de bain, faute d’indice de protection vérifié.
Mur nu, ou console sobre.

Deux finitions de platine, **Bois clair** et **Noyer**. Le `g1` est en **Bois clair**. Vue teinte
en plus : `applique-double-travertin-474088-noyer-g1.jpg`.

### 4. `applique-murale-travertin-358794` — LM-125

**Applique murale galet travertin LED, salon** · 149 € · 9 sources

Galet de travertin sur platine, LED derrière, éclairage haut et bas.

**Fiche en brouillon**, bloquée sur un problème de coût et de délai fournisseur. Produire les
visuels quand même : ils serviront le jour où la fiche est débloquée, ou sur un fournisseur de
remplacement pour le même produit. **Priorité basse**, à faire après les quatre autres.

### 5. `applique-murale-pierre-metal-147598` — LM-126

**Applique murale galet beige pierre et métal, entrée** · 109 € · 9 sources

Galet de pierre posé sur une **équerre de métal**, douille **E27 apparente sous le galet**.
C’est la seule applique du rayon avec une ampoule visible : montrer une ampoule LED blanc
chaud de forme standard, allumée sur `g1`, sans marque lisible.

Deux finitions d’équerre, **Blanc** et **Noir**. Le `g1` est en **Noir**. Vue teinte en plus :
`applique-murale-pierre-metal-147598-blanc-g1.jpg`.

Attention : les sources contiennent aussi des variantes rouge et verte, que nous **ne vendons
pas**. Les ignorer.

## Cover de collection

`brand/lumierematiere-collection-appliques-murales.jpg`, au format des 13 covers déjà livrées.

Sujet : le galet de pierre de LM-122, allumé, sur un grand pan de mur papier `#F6F3EC`, cadrage
large et décentré pour laisser respirer le titre. Aujourd’hui la collection affiche une photo
AliExpress reprise telle quelle, c’est la seule vignette de `/collections` qui détonne.

## Récapitulatif

| Handle | Vues galerie | Vues teinte | Priorité |
|---|---:|---:|---|
| `applique-murale-pierre-588683` | 5 | 0 | haute |
| `applique-liseuse-pierre-311650` | 5 | 1 | haute |
| `applique-double-travertin-474088` | 5 | 1 | haute |
| `applique-murale-pierre-metal-147598` | 5 | 1 | haute |
| `applique-murale-travertin-358794` | 5 | 0 | basse, fiche en brouillon |
| cover collection | 1 | — | haute |

**26 JPEG au total.** Aucune action Shopify, DSers ou Ads : le rattachement des images aux
fiches et aux variantes se fait ensuite de notre côté, comme pour les 124 packshots du 25/08.

# Rattachement des visuels Codex — Maison Noirmont — 09/08/2026

Contrôle QA puis rattachement Shopify des visuels livrés par Codex dans
`visuels-codex-2026-08/`. Journal tenu au fil de l'eau.

## Règles appliquées

- Chaque image est **ouverte et regardée** avant tout rattachement.
- Refus si : marque / sigle / lettrage / mention d'origine sur le cadran ; avis, note,
  étoile, badge ou chiffre incrusté ; bracelet représenté ≠ bracelet réellement vendu par
  la fiche ; source manifeste introuvable ; hors 2048×2048 JPEG.
- Rattachement par `productCreateMedia` — **toujours en fin de galerie**, jamais en
  position 1 (le suffixe `-gN` est une numérotation de livraison, pas une position).
- `alt` descriptif en français posé sur chaque média.
- Aucun média existant supprimé. Aucun prix, statut, texte ou variante modifié.
  Aucun brouillon activé.

---

## Tour 1 — 09/08/2026 ~00h00

### Rattachés (10 visuels sur 6 fiches)

| Fiche | Fichiers | Position | Alt posé |
|---|---|---|---|
| `integrale-vert-sport-chic-acier` | `-g1` situation 3/4 | 2/5 | Intégrale Vert — montre à cadran vert texturé et bracelet acier intégré, posée de trois quarts sur fond clair — Maison Noirmont |
| | `-g2` macro cadran | 3/5 | Intégrale Vert — macro du cadran vert texturé, index appliqués et guichet de date, lunette acier vissée — Maison Noirmont |
| | `-g3` au poignet | 4/5 | Intégrale Vert — montre portée au poignet, cadran vert et bracelet acier intégré — Maison Noirmont |
| | `-g4` détail maille | 5/5 | Intégrale Vert — détail de la maille du bracelet acier brossé et de ses maillons centraux — Maison Noirmont |
| `rouleau-de-voyage-vert-cuir` | `-g1` situation 1 alvéole | 2/3 | Rouleau de Voyage Vert — rouleau en cuir vert ouvert, une montre logée dans son alvéole doublée — Maison Noirmont |
| | `-g2` macro cuir + couture | 3/3 | Rouleau de Voyage Vert — macro du cuir vert grainé et de la couture de la sangle de fermeture — Maison Noirmont |
| `contre-la-montre-argent-chronographe` | `-g1` macro caoutchouc noir | 5/5 | Contre-la-montre Argent — détail du bracelet caoutchouc noir à deux rainures et de sa jonction à la corne acier — Maison Noirmont |
| `contre-la-montre-bleu-glacier-chronographe` | `-g1` macro acier 3 maillons | 5/5 | Contre-la-montre Bleu glacier — détail du bracelet acier trois maillons à la jonction du boîtier — Maison Noirmont |
| `contre-la-montre-compteurs-bleus-chronographe` | `-g1` macro caoutchouc bleu marine | 5/5 | Contre-la-montre Compteurs bleus — détail du bracelet caoutchouc bleu marine et de sa jonction au boîtier acier — Maison Noirmont |
| `contre-la-montre-gris-anthracite-chronographe` | `-g1` macro acier 3 maillons | 5/5 | Contre-la-montre Gris anthracite — détail oblique du bracelet acier trois maillons et de son articulation à la boîte — Maison Noirmont |

### Point de contrôle n°3 — fidélité du bracelet (le plus délicat de la fournée)

Chaque macro de bracelet a été confrontée au texte de la fiche Shopify :

| Fiche | Ce que la fiche vend | Ce que la macro montre | Verdict |
|---|---|---|---|
| Argent | « bracelet caoutchouc noir » (option : *Argent · caoutchouc noir*) | caoutchouc noir à deux rainures + corne acier | conforme |
| Bleu glacier | « Sur bracelet acier » | acier trois maillons | conforme |
| Compteurs bleus | « bracelet caoutchouc bleu marine » (option : *Compteurs bleus · bracelet bleu*) | caoutchouc bleu marine | conforme |
| Gris anthracite | « sur bracelet acier » | acier trois maillons | conforme |

Aucune inversion : le doute soulevé au briefing (macro acier sur Bleu glacier, macro
caoutchouc sur Compteurs bleus) est levé — ce sont bien les bracelets vendus par ces
deux fiches.

### Autres contrôles du tour 1

- Cadrans : les 4 vues Intégrale et la montre-accessoire du Rouleau montrent un cadran
  **stérile** — aucun logo, sigle, lettrage ni mention d'origine. Les 4 macros
  chronographe ne cadrent pas le cadran.
- Aucun avis, note, étoile, badge ni chiffre de satisfaction incrusté.
- Sources manifeste : les 6 fichiers `visuels-2026-07-25/generated/*.jpg` cités existent
  tous et sont cohérents avec le sujet livré.
- Technique : 10/10 en 2048×2048 JPEG.
- Ordre de galerie vérifié après coup : l'image 1 d'origine est restée en place sur les
  6 fiches, les nouveaux médias sont bien en queue. Statuts inchangés (ACTIVE).

### Non rattachés — dossiers vides assumés par Codex

| Fiche | Motif consigné au manifeste |
|---|---|
| `bracelet-fkm-tropical` | pas de source propre complète : l'unique face locale est un gros plan partiel avec marquage central masqué et embossage douteux |
| `carte-cadeau-maison-noirmont` | pas de source propre locale ; les 4 variantes ont un SKU fournisseur `null` |
| `trente-neuf-rose-classique-cannelee` | source locale interdite : la seule face disponible porte la mention d'origine **SWISS MADE** à 6 h |

Rien à rattacher pour ces trois fiches — écarts justifiés, aucune action.

---

## Tour 2 — 09/08/2026 ~00h10

Quatre nouveaux dossiers livrés pendant le tour 1.

### Rattachés (4 visuels sur 4 fiches)

| Fiche | Fichier | Position | Alt posé |
|---|---|---|---|
| `contre-la-montre-rose-poudre-chronographe` | `-g1` macro acier 3 maillons | 5/5 | Contre-la-montre Rose poudré — macro du bracelet acier trois maillons et de son grain brossé — Maison Noirmont |
| `heritage-bleu-plongeuse-vintage-42` | `-g1` macro lunette bleue | 5/5 | Héritage Bleu — macro oblique de la lunette bleue, de son repère triangulaire doré et de sa denture acier — Maison Noirmont |
| `heritage-bleu-nuit-plongeuse-vintage-42` | `-g1` profil couronne + lunette noire | 5/5 | Héritage Bleu nuit — profil rapproché de la couronne stérile, du flanc acier brossé et de la lunette noire crantée — Maison Noirmont |
| `montre-acier-chiffres-3-6-9-explorateur` | `-g1` macro bracelet acier | 5/5 | Explorateur — macro du bracelet acier trois maillons, maillons centraux polis et côtés brossés — Maison Noirmont |

### Contrôles du tour 2

- **Fidélité produit** : Rose poudré « sur bracelet acier » → macro acier, conforme.
  Explorateur « bracelet acier trois maillons » → macro acier trois maillons, conforme.
  Héritage Bleu « lunette bleue » → lunette bleue, conforme. Héritage Bleu nuit
  « lunette noire » → lunette noire, conforme.
- **Cadran / couronne** : aucun logo, sigle ni lettrage. Point de vigilance levé sur
  l'Explorateur — la fiche indique que le cadran réel porte la mention « Professional
  Automatic », mais la macro livrée ne cadre que le bracelet : aucun texte à l'image.
  La couronne de l'Héritage Bleu nuit est bien lisse et vierge. Aucune mention
  d'origine nulle part.
- **Avis / badges** : aucun.
- **Sources** : `chrono-rose-poudre.jpg`, `heritage-bleu-lunette-bleue.jpg`,
  `heritage-bleu-nuit-lunette-noire.jpg` et
  `visuels-arabes-squelettes-2026-07-29/…-explorateur-face.jpg` existent tous.
- **Technique** : 4/4 en 2048×2048 JPEG.
- Ajout en fin de galerie, image 1 intacte, statuts ACTIVE inchangés.

**Cumul : 14 visuels rattachés sur 10 fiches. 0 refus.**

# Branchement des visuels — Lot 3 — 2026-07-26

Boutique **NOIRMONT** / Maison Noirmont (`v42pzp-h4.myshopify.com`, maisonnoirmont.fr) — vérifiée via `get-shop-info` avant toute écriture.

**43 fiches branchées · 102 variantes couvertes · 62 visuels sur 77 · 57 médias créés · 0 média supprimé.**

Sauvegarde préalable : `backup-avant-branchement-lot3.json` (43 fiches, 102 variantes, SKU, médias avant intervention, écrite **avant** la première mutation).

---

## Observé

État relevé **en direct** sur l'API Admin, sans se fier au manifeste de Codex ni aux instantanés locaux.

- Catalogue réel : **85 fiches** (confirmé par `productsCount`).
- Les 7 mères découpées portent toujours leurs variantes d'origine ; les **41 fiches filles** existent et sont ACTIVE.
- Les 54 médias produits par Codex étaient bien présents, **mais sur les fiches mères uniquement**. Le Bracelet Présidentiel n'avait reçu aucun de ses visuels (`mediaCount` = 1), ce qui confirme son rapport.
- Les fichiers `shopify/product-media-add-*.response.json` sont **mal nommés** : leur contenu est une lecture `productVariantsBulkUpdate` de médias préexistants, pas la preuve d'un ajout. Ils n'ont servi à rien dans cette passe.

### Le partage de médias, vérifié et non supposé

Les 12 filles chronographe portent **exactement les 7 mêmes `MediaImage` que la mère** (`59679727976786`, `59680004505938`, `59680004538706`, `59680004571474`, `59680004604242`, `59680004637010`, `59680004669778`). Même constat par famille pour GMT, Intégrale, Héritage, et pour le média unique des accessoires.

Supprimer l'un de ces médias depuis une fille l'aurait retiré de la mère **et des 11 sœurs**. C'est la raison pour laquelle aucune suppression n'a été faite (voir plus bas).

### Piège écarté en cours de route

`productUpdate` n'accepte pas `files` (erreur API). `productSet` a été **écarté délibérément** : la documentation Shopify précise que pour les champs de type liste — dont **`variants`** et `files` — la mutation « supprime les entrées existantes qui ne sont pas incluses ». L'utiliser pour attacher un média aurait risqué d'effacer les variantes (donc les SKU et les mappings DSers) ou les 7 médias hérités.

Méthode retenue : `productCreateMedia` avec `originalSource` pointant sur le fichier déjà en ligne, **et l'`alt` strictement identique** à celui du média partagé — de sorte qu'une éventuelle réécriture d'`alt` soit un non-événement.

**Résultat mesuré sur un pilote** (Contre-la-montre Argent) avant toute généralisation : Shopify a créé un **nouveau `MediaImage` indépendant** (`59691366711634`, fichier suffixé d'un UUID), l'`alt` de la mère (`59691084349778`) est resté intact, `mediaCount` et `variantsCount` de la mère inchangés. Les filles disposent donc de médias **propres**, ce qui rend une suppression future sur une fille sans effet de bord.

---

## Modifié

Trois opérations par fiche : `productCreateMedia` (attacher), `productVariantAppendMedia` (lier la variante à son média), `productReorderMedia` (visuel du coloris en position 1). Toutes les réponses sont revenues avec `userErrors` / `mediaUserErrors` **vides**.

| Famille | Fiches | Variantes | Visuels | Médias créés |
|---|---:|---:|---:|---:|
| Contre-la-montre — chronographe | 12 | 20 | 20 | 20 |
| Voyageur — GMT | 6 | 24 | 6 | 6 |
| Intégrale — sport chic | 7 | 7 | 7 | 7 |
| Héritage — plongeuse vintage 42 | 3 | 3 | 3 | 3 |
| Remontoir Bois | 4 | 8 | 4 | 4 |
| Rouleau de Voyage — cuir | 4 | 12 | 4 | 4 |
| Remontoir Collection | 5 | 15 | 5 | 5 |
| Bracelet Présidentiel — doré | 1 | 8 | 8 | 8 (upload neuf) |
| Set de tournevis d'horloger | 1 | 5 | 5 | 0 (déjà en place) |
| **Total** | **43** | **102** | **62** | **57** |

- Les **8 visuels du Bracelet Présidentiel** ont été mis en ligne pour la première fois (`stagedUploadsCreate` + PUT, 8 × HTTP 200, puis `productCreateMedia`). Ils portent un `alt` propre à la fiche, sans risque de partage puisque ce sont des fichiers neufs.
- Les **5 visuels du Set de tournevis** étaient déjà sur la bonne fiche : seules les liaisons variante↔média manquaient. Aucun ré-upload.
- **Fiches multi-coloris** : les filles chronographe regroupant plusieurs cadrans (Blanc 3, Champagne 2, Noir 2, Panda 2, Panda inversé 2, Turquoise 2, Vert 2) ont reçu **un visuel par cadran**, chacun lié à sa propre variante.
- **Fiches à option technique** : sur les 6 GMT, les 4 Rouleau, les 4 Remontoir Bois et les 5 Remontoir Collection, le visuel du coloris est associé à **toutes** les variantes qui partagent ce coloris (mouvement & fond, capacité), conformément à la consigne.
- **Position 1** : appliquée aux 41 fiches filles. Laissée telle quelle sur le Bracelet Présidentiel et le Set de tournevis, qui ne sont pas des fiches filles et conservent leur visuel d'accroche générique en tête ; le basculement y est assuré par la liaison variante↔média.

---

## Manquant

- **15 visuels du Bracelet Présidentiel non branchés**, et c'est voulu : `bracelet-3-rangs-acier`, `-acier-or-rose`, `-noir`, `-or-rose`, `bracelet-jubile-acier`, `-acier-or-rose`, `-noir`, `bracelet-maille-fixe-acier`, `-acier-or`, `-acier-or-rose`, `-or-rose`, `bracelet-president-acier`, `-acier-or`, `-noir`, `-or-rose`. Ils correspondent aux **16 variantes supprimées** à l'élagage (24 → 8). Les fichiers restent sur disque si les références étaient un jour réintroduites.
- Aucun SKU vivant n'est resté sans visuel : le rapprochement par SKU couvre **102/102**.

---

## Non traité volontairement

- **3 déclinaisons GMT « siglé »** (logo de marque tierce) : aucun visuel, aucune fiche. Leurs 12 SKU restent sur la mère seule. Le manifeste de Codex les avait déjà écartées (`skipped`), et aucune fiche fille ne les reprend.
- **Noirmont Deux — Plongeuse céramique** (`10977448624466`, 28 variantes) : intouchée, aucune référence identifiable.
- **Fiches mères** : ni médias retirés, ni variantes touchées. Elles restent en l'état en attendant leur réduction à un coloris unique.
- **Mappings DSers, SKU, prix, stocks, options, titres** : aucune écriture. Les seules mutations employées portent exclusivement sur les médias et sur la liaison variante↔média.

---

## Vérification SKU avant / après

Le rapprochement a été fait **par SKU**, jamais par identifiant de variante — ceux du manifeste de Codex sont périmés depuis le découpage.

- Manifeste Codex : **118** couples SKU → visuel, sans conflit.
- Variantes vivantes traitées : **102**.
- Écart : **118 − 102 = 16**, exactement les 16 variantes supprimées du Bracelet Présidentiel. Aucune perte inexpliquée.
- **0 SKU du manifeste introuvable** en boutique ; **0 SKU vivant sans visuel**.

Relecture après écriture, fiche par fiche, sur les 43 fiches (`sku` + `alt` du média lié) : **les 102 SKU sont identiques à la sauvegarde**, dans le même ordre et sur les mêmes fiches. Aucun SKU créé, modifié ou supprimé.

Contrôle de non-régression sur les mères (avant → après) :

| Mère | Médias | Variantes |
|---|---|---|
| Contre-la-montre — Chronographe panda | 27 → 27 | 20 → 20 |
| Voyageur — GMT automatique | 13 → 13 | 36 → 36 |
| Intégrale — Sport chic acier | 14 → 14 | 7 → 7 |
| Héritage — Plongeuse vintage 42 | 10 → 10 | 3 → 3 |
| Remontoir Bois | 5 → 5 | 8 → 8 |
| Rouleau de Voyage — cuir | 5 → 5 | 12 → 12 |
| Remontoir Collection | 6 → 6 | 15 → 15 |

Les `alt` des mères sont inchangés (vérifié nommément sur `59691084349778`).

---

## Médias supprimés et conservés

**Supprimés : aucun.**

**Conservés, et pourquoi :**

- Les **7 médias génériques hérités** sur chaque fille montre (1 sur chaque fille accessoire) sont le **même objet `MediaImage` que la mère**. Les supprimer depuis une fille les retirerait de la mère et de toutes les sœurs. Un média en trop est un défaut cosmétique ; un média disparu de dix fiches est une régression visible. Ils restent donc en place, désormais **après** le visuel du coloris.
- Les **54 médias de coloris ajoutés par Codex sur les mères** sont conservés : les mères sont encore multi-coloris et les afficheraient légitimement.

**Recommandation pour une passe ultérieure** (hors périmètre ici) : maintenant que chaque fille possède des `MediaImage` **indépendants**, l'élagage des visuels génériques hérités peut se faire fiche par fiche sans effet de bord — mais uniquement sur les médias créés au lot 3, jamais sur les identifiants listés comme partagés dans `backup-avant-branchement-lot3.json`.

---

## Contrôle visuel

Réalisé sur le storefront, thème brouillon `204248088914` (bandeau Shopify « Maison Noirmont — Draft — Password protected » visible ; la prévisualisation s'est ouverte sans saisie de mot de passe).

**Contre-la-montre Vert — Chronographe**

- Au chargement, image principale = `chrono-vert-caoutchouc-vert…jpg` — le visuel du coloris est bien en position 1, devant les visuels génériques.
- Au clic sur **ACIER**, la galerie bascule sur `chrono-vert-bracelet-acier…jpg` et l'URL passe sur `variant=54096771252562`, soit exactement la variante du SKU `14:350850#M12` cartographiée pour ce visuel.
- Capture d'écran : cadran vert sur bracelet acier, cohérent avec l'option sélectionnée.

**Bracelet Présidentiel — doré**

- Les **8** visuels de coloris sont servis par le storefront, un par maille survivante, dans l'ordre des options : maille fixe or jaune, 3 rangs or jaune, 3 rangs acier & or, Président acier & or rose, Président or jaune, Jubilé or rose (réf. 15), Jubilé acier & or, maille sablée acier. **Aucun visuel surnuméraire** issu des 16 références supprimées.

Aucun visuel d'un coloris n'a été réutilisé pour en couvrir un autre. Le seul cas de partage documenté par Codex (`bracelet-jubile-or-rose`, commun aux réf. 12 et 15) est désormais sans ambiguïté : la réf. 12 a été supprimée à l'élagage, seule la réf. 15 subsiste et reçoit le visuel.

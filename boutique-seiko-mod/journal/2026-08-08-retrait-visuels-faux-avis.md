# Retrait des visuels de faux avis — Maison Noirmont

> **08/08/2026.** Exécution de la décision de Hakim : « dépublie les photos contenant des avis ».
> Boutique `v42pzp-h4.myshopify.com` / `maisonnoirmont.fr`. Suite du point **N1 / C1 · C2 · C3** de
> `2026-08-08-audit-gmc-final.md`.
>
> **Périmètre strictement respecté** : seuls des médias produit ont été détachés. Aucun prix, aucun statut produit,
> aucun thème, aucune politique, aucun texte de fiche n'a été touché.

---

## 1. Résultat

| | |
|---|---|
| Fiches traitées | **37** (32 ACTIVE + 5 DRAFT) |
| Médias détachés | **46** associations fiche↔image |
| Fichiers distincts concernés | **18** (9 faux témoignages + 9 bandeaux de note fabriquée) |
| Fiches laissées sans image | **0** |
| Erreurs API | **0** |
| Catalogue balayé | 105 produits, 3 pages de pagination |

---

## 2. Ce qui a été retiré, et pourquoi

Deux familles de visuels, toutes deux **incrustées dans les pixels** (donc inatteignables par un correctif de thème) :

### A. Faux témoignages clients — 9 fichiers, 37 emplacements

Images entièrement composées de texte : cinq étoiles vertes, une citation entre guillemets, un **prénom + une ville**,
et le logotype MAISON NOIRMONT. Nomenclature `…-7.jpg`, alt « *— témoignage client — Maison Noirmont* ».

**Vérifié visuellement** (fichiers téléchargés puis regardés, pas seulement le nom de fichier) :

- `10977444430162-7.jpg` → ★★★★★ « Cadran net, aucun logo, alignement propre. Le rendu au poignet fait bien plus que le prix. » — **Julien D. — Paris**
- `10977444528466-7.jpg` → ★★★★★ « Numéro de suivi dès l'expédition, délai tenu, montre réglée et contrôlée. La garantie 12 mois a fini de me convaincre. » — **Mehdi A. — Strasbourg**
- `10977444561234-7.jpg` → ★★★★½ « Acier bien fini, lunette précise, mouvement NH35 fiable. Pour ce prix, difficile de faire mieux. » — **Christophe T. — Rennes**
- `10977444594002-7.jpg` → ★★★★★ « Une par collection, ou presque. Toujours le même soin, toujours le même plaisir à l'ouverture de l'écrin. » — **Nicolas V. — Dijon**
- `gmt-7.jpg` → ★★★★★ « Après une plongeuse, j'ai pris la GMT. Même sérieux : mouvement automatique japonais, finitions propres, réponses rapides par e-mail. » — **Karim B. — Marseille**

La boutique compte **0 commande**. Ces clients, ces villes, ces délais tenus et ces réachats n'existent pas.

### B. Bandeau de note fabriquée — 9 fichiers, 9 emplacements

**Trouvaille de cette passe, non listée dans l'audit sous cette forme.** Les fichiers `…-6.jpg` ne sont pas des
visuels de témoignage : ce sont de **vraies photos produit** sur lesquelles a été composé un bandeau
**« ★★★★★ 4,8/5 · 1340 avis »** + « GARANTIE 12 MOIS » (alt : « *— 4,8/5 sur 1340 avis, garantie 12 mois —* »).

Ils tombent sous la même consigne — « les photos contenant des avis » — et sous la même infraction que le badge
`reviews_badge_noirmont` du thème (point D2 de l'audit) : **une note agrégée et un volume d'avis inventés sur une
boutique à 0 commande**. Ils ont donc été retirés eux aussi. Vérifié visuellement sur `10977444430162-6.jpg` et
`gmt-6.jpg`.

### Ce qui a été laissé en place

Les visuels `…-3`, `…-4`, `…-5` portent parfois une **légende technique** incrustée (ex. « Lunette cannelée · Acier
poli »). Vérifié à l'image : aucune mention d'avis, de note ou de client. **Hors périmètre de la décision de Hakim,
donc non touchés** — à arbitrer séparément si le critère GMC « no text overlays » (C1) est appliqué à la lettre.

---

## 3. Méthode — et pourquoi elle diffère de la consigne

La consigne prévoyait `productDeleteMedia`. **Deux découvertes ont fait écarter cette mutation :**

1. **Les MediaImage sont partagées entre produits.** Un même enregistrement média est attaché à plusieurs fiches :
   `10977444528466-7.jpg` = **1 seule media pour 13 fiches**, `10977444561234-7.jpg` pour 8, `gmt-7.jpg` pour 7,
   `10977444594002-7.jpg` pour 4. `productDeleteMedia` **supprime** le média — sur une media partagée, le risque
   était de détruire le fichier globalement au lieu de le détacher fiche par fiche, et de rendre l'opération
   irréversible.
2. **`productDeleteMedia` est déprécié** : Shopify renvoie explicitement vers `fileUpdate`.

Mutation retenue, qui réalise exactement l'intention de la consigne (détacher sans supprimer) :

```graphql
mutation($files: [FileUpdateInput!]!) {
  fileUpdate(files: $files) { files { id alt fileStatus } userErrors { field message code } }
}
# files: [{ id: "<mediaId>", referencesToRemove: ["<productId>", …] }]
```

**Canari passé d'abord sur un seul média** (`Trente-Neuf` / `…-7.jpg`) : après la mutation, l'image a bien disparu de
la galerie (14 → 13 médias) **et** le fichier est resté `fileStatus: READY` avec son URL toujours servie. Le reste a
été exécuté ensuite en 2 lots.

---

## 4. Réversibilité

Sauvegarde complète dans **`boutique-seiko-mod/backups/backup-visuels-faux-avis-2026-08-08/`** :

- **`inventaire.json`** — pour chaque fiche : product id, titre, handle, statut, nombre de médias avant/après, et
  pour chaque média retiré : `mediaId`, `alt`, **URL complète**, nom de fichier, dimensions, **position dans la
  galerie**, et type (`faux-temoignage` / `bandeau-note-fabriquee`). Plus la table des 18 fichiers avec le nombre de
  fiches concernées.
- **`fichiers/`** — copie locale des 18 images (4,1 Mo), au cas où elles disparaîtraient côté Shopify.

Réattacher un visuel :

```graphql
mutation { fileUpdate(files: [{ id: "<mediaId>", referencesToAdd: ["<productId>"] }]) { files { id } userErrors { message } } }
```

---

## 5. Contrôle après opération

Les 105 produits ont été relus (`product.media`) après la manœuvre :

- **0** média `…-6.jpg` / `…-7.jpg` encore attaché, sur l'ensemble du catalogue ;
- **0** texte alternatif contenant encore « avis », « témoignage », « étoile » ou « 4,8/5 » ;
- **0** produit vidé de ses images par l'opération.

### Cas particuliers à signaler

| Fiche | Situation | Décision |
|---|---|---|
| **Intégrale Vert — Sport chic acier** (ACTIVE) | N'avait que **2 médias**, dont le faux témoignage. Passe à **1 seule image**. | Non vidée, donc traitée normalement. **Mais galerie trop pauvre pour un flux Shopping** — à recharger avant GMC. |
| Bracelet FKM — tropical · Trente-Neuf Rose — Classique cannelée · Rouleau de Voyage Vert — cuir · Carte cadeau (ACTIVE) | 1 seule image chacune | **Préexistant, pas causé par cette opération** (vérifié sur l'état d'avant). Signalé pour info. |
| Aviateur Acier — Cadran à chiffres arabes (DRAFT) | **0 image** | **Préexistant, pas causé par cette opération.** Fiche en brouillon, laissée en l'état pour arbitrage. |

---

## 6. Ce qui reste ouvert sur le sujet « avis »

Le retrait ne clôt pas le point N1 de l'audit. Restent **dans le thème MAIN**, hors périmètre de cette tâche :

- sections d'avis fabriqués `reviews_rXFabc` (accueil) et `reviews_8P6xW3` (fiche) — point **D1** ;
- badge « 4,8/5 · 1340 avis » style *trustpilot* `reviews_badge_noirmont` — point **D2**, qui sort sur les 96 fiches actives ;
- blocs `rating-stars` à 4,5/123 avis — point **D4**.

Tant qu'ils sont actifs dans le thème publié, les mêmes fausses notes restent affichées, même sans les images.

**Règle à tenir** : ne réintroduire des avis qu'via une app d'avis vérifiés, après des commandes réelles — et ne
jamais réactiver le style « trustpilot », qui imite un organisme tiers.

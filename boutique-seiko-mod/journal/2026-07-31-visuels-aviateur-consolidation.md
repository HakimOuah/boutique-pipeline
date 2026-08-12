# Visuels de l'aviateur à cadran arabe et consolidation des fiches — Maison Noirmont

> **27/07/2026** — boutique `v42pzp-h4` / maisonnoirmont.fr.
> Suite de `2026-07-31-fiches-contradictoires-et-cadran-arabe.md` §4. Produit **8 visuels** et **réécrit les deux fiches
> Noirmont Un en aviateurs**.
> **Écritures : 4 `productUpdate` (titre, description, SEO, étiquettes, 2 métachamps, handle), 8 médias ajoutés,
> 16 médias de plongeuse supprimés, 12 images de variante réaffectées, 2 réordonnancements, 2 mouvements de
> collection.**
> Aucun SKU, prix, variante, option ni mapping DSers touché. Aucune publication : les trois fiches restent en
> **`DRAFT`**. Aucun thème ouvert. Aucune commande, aucun achat.
> Sauvegardes avant écriture : `backup-avant-reecriture-aviateurs-2026-07-27.json` (état des fiches) et
> `boutique-seiko-mod/backups/backup-medias-plongeuse-supprimes-2026-07-27/` (les 16 fichiers image + `MANIFESTE.json`).
> Livrables images : `boutique-seiko-mod/livraisons/visuels-aviateur-2026-07-27/`.
>
> **Second passage (autorisations de Hakim) :** les 16 médias de plongeuse ont été **supprimés** après
> sauvegarde et contrôle de partage, les **3 visuels bronze manquants** ont été produits, et les **handles** ont
> été corrigés. Détail en §8.

---

## 1. La doctrine appliquée — les chiffres SONT le produit

La règle de stérilité de la boutique interdit **la marque empruntée**, pas les chiffres. Sur ce cadran, les
chiffres arabes sont le produit : un flieger sans ses chiffres n'est pas un flieger, et c'est précisément cette
grappe (**≈ 15 500 recherches/mois, personne au-dessus de la 4ᵉ position**) qu'on vise.

Ce qui a été rendu, sur chaque visuel, d'après la photo fournisseur `steel case-no logo` :

| Élément | Rendu attendu |
|---|---|
| Couronne **extérieure** | **5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55** en blanc, orientés radialement, **pas de « 60 »** |
| Repère de midi | **triangle blanc** à la place du 60, avec une pastille au-dessus |
| Couronne **intérieure** | **1 à 12** en crème, droits, avec un bâtonnet crème à l'extérieur de chaque chiffre |
| Piste des minutes | hachures fines au bord + pastilles à chaque pas de 5 |
| Aiguilles | glaive argenté heures + minutes, trotteuse fine |
| Stérilité | **aucun logo, aucun mot, aucune lettre, aucun guichet de date** |

Le filigrane « Tandorio » de la photo fournisseur a été **effacé par interpolation verticale + flou local** avant
de servir de référence, pour éviter que le modèle ne le recopie. Il ne touchait pas le cadran : la couronne, la
lunette et les deux couronnes de chiffres sont intactes.
Référence conservée : `boutique-seiko-mod/livraisons/visuels-aviateur-2026-07-27/reference/TANDORIO-steel-nologo-recadre-filigrane-efface.jpg`.

---

## 2. Les visuels produits — 5 fichiers, 40 crédits

Modèle `nano_banana_pro` (identifiant interne renvoyé : `nano_banana_2`), **4K natif 4096 × 4096**, carré 1:1,
**image-to-image**, aucun inpainting. Livraison **2048 × 2048 JPEG q90**, plus l'original 4K conservé.

| Slot | Fichier | Source i2i | Générations | Retenue |
|---|---|---|---:|---|
| `face` | `noirmont-un-plongeuse-acier-face.jpg` | photo fournisseur nettoyée | 2 | candidate A |
| `situation` | `noirmont-un-plongeuse-acier-situation.jpg` | face validée | 1 + 2 | 2ᵉ passe, candidate A |
| `macro` | `noirmont-un-plongeuse-acier-macro.jpg` | face validée | 1 | 1ᵉʳ jet |
| `poignet` | `noirmont-un-plongeuse-acier-poignet.jpg` | face validée | 2 | candidate A |
| `face` bronze | `noirmont-un-bronze-plongeuse-face.jpg` | face acier validée, métal recoloré | 2 | candidate A |

**10 images générées, 40 crédits consommés** (4 crédits l'unité en 4K — nettement moins que les 5,3 constatés
en juillet). Solde **269,46 → 229,46**. **Plafond de 60 crédits respecté**, 20 non dépensés.

### Direction artistique
Fond minéral clair, dégradé pierre `#E7E4DE` → craie `#FAFAF7`, lumière douce latérale haute-gauche, une seule
ombre portée diffuse. La `situation` ajoute une dalle de travertin pâle et un éclat de craie brute floue au coin
— décor introduit, palette minérale respectée, conformément à `2026-07-31-audit-visuel-catalogue.md` §2.

### Contrôle des chiffres — fait en zoom fort, cadran par cadran
Chaque cadran a été recadré et agrandi (jusqu'à ×8 sur le 4K) puis relu chiffre par chiffre, avec vérification de
l'**alignement radial** entre les deux couronnes (le « 12 » intérieur doit pointer dans le même axe que le
triangle, le « 3 » avec le « 15 », le « 6 » avec le « 30 »).

| Visuel | Extérieure 5→55 | Intérieure 1→12 | Alignement des couronnes | Stérilité | Verdict |
|---|---|---|---|---|---|
| `face` | 11/11, ordre juste | 12/12, ordre juste | vérifié sur 12/1/3/11 | aucun texte | ✅ |
| `situation` | 11/11 | 12/12 | vérifié sur 12/triangle | aucun texte | ✅ |
| `macro` | visibles 55·5·10·15·20·25, ordre juste | visibles 11·12·1·2·3·4·5, ordre juste | conforme | aucun texte | ✅ |
| `poignet` | 11/11 | 12/12 | conforme | aucun texte | ✅ |
| `face` bronze | 11/11 | 12/12 | conforme | aucun texte | ✅ |

**Aucun chiffre inventé, aucun doublon, aucun caractère miroir, aucun « 8 » déformé.**

**Un seul point à connaître, et il est fidèle au produit :** sur les cinq visuels, le **« 10 » intérieur est
partiellement masqué par l'aiguille des heures**. Ce n'est pas un défaut de rendu — le chiffre est correctement
formé, seule sa moitié droite passe sous l'aiguille — et **la photo fournisseur présente exactement la même
occultation**. Toute position d'aiguilles en masque deux ; celle-ci est la plus naturelle.

### Porté-poignet — contrôle des doigts
Avant-bras et poignet seuls, entrant en diagonale, **coupés bien avant le coude**. Aucun visage, aucune épaule,
aucun second bras. Manche unie gris clair, sans motif ni marquage. Aucune bague, aucun autre bijou, aucune autre
montre. **Les doigts sortent du cadre au bord droit** : la main est vue de dos, jointures à peine amorcées.
Zoom fait sur toute la zone visible — peau naturelle, aucun doigt surnuméraire, aucune déformation, aucune
seconde main fantôme. C'est le cadrage le plus sûr sur ce défaut.

### Écarté
| Fichier | Raison |
|---|---|
| `rejected/situation-v1-cadran-pivote-90deg.jpg` | Le modèle a **dressé la montre debout sur son bracelet, couronne en haut** : le cadran se lit de travers, les chiffres à 90°. Corrigé par un bloc « MANDATORY ORIENTATION » (à plat, triangle en haut, couronne à droite) — efficace au premier essai. |
| `rejected/face-B-non-retenue-cadran-plus-petit.jpg` | Cadran plus petit dans le cadre et plus incliné, chiffres moins lisibles. Fidèle, mais moins bonne face. |

**Aucun slot n'a demandé plus de trois générations.** Le sujet difficile n'a pas été les chiffres — que
`nano_banana_pro` a rendus juste dès le premier jet — mais **l'orientation du cadran** dans la mise en situation.

---

## 3. Les deux fiches réécrites en aviateurs

Les titres et les descriptions étaient **factuellement faux** : ils annonçaient une plongeuse à lunette
tournante et bracelet acier, le fournisseur expédie un flieger à lunette lisse et bracelet cuir. Réécriture
autorisée à ce titre.

| | `noirmont-un-plongeuse-acier` | `noirmont-un-bronze-plongeuse` |
|---|---|---|
| **ID** | `10977448558930` | `10978722087250` |
| **Titre avant** | Noirmont Un — Plongeuse acier | Noirmont Un Bronze — Plongeuse |
| **Titre après** | **Noirmont Un — Aviateur acier à chiffres arabes** | **Noirmont Un Bronze — Aviateur bronze à chiffres arabes** |
| `seo.title` | Montre cadran chiffres arabes, aviateur acier — Noirmont Un | Montre cadran chiffres arabes, aviateur bronze — Noirmont Un |
| `custom.famille` | `["Plongeuses"]` → **`["Classiques"]`** | `["Plongeuses"]` → **`["Classiques"]`** |
| `custom.bracelet` | absent → **`["Cuir"]`** | `["Acier maille non précisée"]` → **`["Cuir"]`** |
| Étiquette | `plongeuses` → **`classiques`** | `plongeuses` → **`classiques`** |
| Collections | `plongeuses` → **`classiques`** (+ `montres`) | `plongeuses` → **`classiques`** (+ `montres`) |
| Médias ajoutés | **4** (face, situation, macro, poignet) en positions 1-4 | **1** (face bronze) en position 1 |
| Statut | **`DRAFT`** | **`DRAFT`** |
| SKU · prix · variantes · mapping | **intacts, relus un à un après écriture** | **intacts, relus un à un après écriture** |

**Le piège `seo` a été évité :** `productUpdate` remplace l'objet `seo` en entier, donc `seo.title` **et**
`seo.description` ont été réécrits dans la même charge utile sur les deux fiches. Relecture après écriture :
les deux titres SEO et les deux descriptions SEO sont présents, et `global.title_tag` / `global.description_tag`
suivent. Aucun titre perdu.

### Ce que les nouvelles descriptions affirment, et sur quoi
Rien qui ne soit adossé au listing `1005004626900765` : cadran noir à chiffres arabes (attribut vendeur « Type
d'affichage : Marqueurs de chiffres arabes » + photos de variante), heures 1-12 en couronne intérieure et minutes
5-55 en extérieure (photos), lunette lisse non tournante (photos), bracelet cuir (attribut vendeur « Type de
matériau du bracelet : Cuir »), sans logo (valeur d'option `-no logo`), fond acier ou verre (valeurs d'option),
Miyota 8215 · Seiko NH35 · PT5000 (valeurs d'option — seules marques tierces autorisées, ce sont des fabricants
de calibre).

Formulations à hedge reprises **mot pour mot** de `2026-07-31-veracite-produit-cloture.md` :
« Verre saphir **annoncé** » · « Étanchéité **annoncée** 200 m : baignade, nage et plongée libre ; la plongée en
bouteille reste déconseillée » · plus la réserve cuir : « le bracelet cuir, lui, n'aime pas l'eau — prévoyez un
bracelet de rechange si vous nagez avec ».

**Aucun diamètre n'est écrit** (le listing ne donne qu'une tranche « 30 à 34 mm » de *cadran*, pas de boîtier) et
**aucune largeur de bracelet** (tranche « 20 à 24 mm »). `custom.diametre` reste vide sur les deux fiches. Le mot
« Tandorio » n'apparaît nulle part.

---

## 4. Sort du doublon — la fiche neuve reste en brouillon

`aviateur-acier-cadran-chiffres-arabes` (`10981883150674`) est **laissée en `DRAFT`, non modifiée, non
supprimée**, et **signalée comme redondante** : `noirmont-un-plongeuse-acier` couvre maintenant exactement le
même produit, avec les **mêmes 6 SKU**, et porte en plus le mapping DSers et les collections. Elle a toujours
**0 média**.

> **Mais elle a un avantage que la fiche retenue n'a pas, et c'est à toi de trancher :** son **handle**.
> `aviateur-acier-cadran-chiffres-arabes` est la bonne URL pour la grappe visée ; celle qu'on publie s'appelle
> `noirmont-un-plongeuse-acier`, c'est-à-dire qu'elle dit « plongeuse » dans son URL en vendant un aviateur.
> Le handle n'était pas dans le périmètre autorisé, je ne l'ai pas touché. Deux issues :
> **(a)** renommer le handle de `noirmont-un-plongeuse-acier` (Shopify pose la redirection tout seul, la fiche est
> en brouillon donc sans trafic à perdre) et supprimer la fiche neuve — **le plus propre** ;
> **(b)** publier la fiche neuve à la place, mais il faut alors lui rattacher le fournisseur dans DSers et
> laisser `noirmont-un-plongeuse-acier` en brouillon définitivement.
> Tant que les deux ne sont pas publiées en même temps, **le doublon de SKU est sans effet**.

---

## 5. ⛔ Ce qui bloque encore la publication

1. **Les 12 anciens médias de plongeuse sont toujours sur la fiche acier**, en positions 5 à 16 : face plongeuse
   acier, situation/macro/poignet de plongeuse, et 6 cartes héritées (« verre saphir, 20 ATM », « 4,8/5 sur
   1340 avis », témoignage client, « boîtier bronze »…). **La suppression de médias m'était interdite**, je les ai
   seulement repoussés derrière les 4 neufs. **Un client qui fait défiler la galerie verrait encore une plongeuse
   à bracelet acier.** C'est le blocage n° 1 : ces 12 médias doivent partir avant publication. Idem sur la fiche
   bronze : **4 anciens médias** en positions 2 à 5.
2. **La fiche bronze n'a qu'un visuel.** Il lui manque `situation`, `macro`, `poignet` en bronze. Coût estimé :
   **12 crédits** (3 × 4), en image-to-image depuis la face bronze qui vient d'être posée.
3. **Rattachement DSers.** Les SKU portent la chaîne d'attributs exacte, le mapping variante par variante sera
   automatique, mais le fournisseur doit être lié aux fiches dans l'interface DSers. Les deux Noirmont Un
   l'étaient déjà — **à revérifier**, la réécriture ne l'a pas touché mais ça se vérifie en dix secondes.
4. **Le diamètre de boîtier reste inconnu.** Rien inventé. Seule issue : demander au vendeur, ou mesurer à
   réception. Les deux fiches n'apparaîtront sous aucune valeur de la facette « Diamètre ».
5. **Aucun rendu de page n'a été vu.** Les fiches sont en brouillon, je n'ai pas ouvert le thème ni la vitrine.
   Le contrôle mobile-first de la galerie (4 puis 5 visuels, ordre `face → situation → macro → poignet`) reste
   à faire.

## 6. Effets de bord à connaître

- **La collection `Plongeuses` tombe de 7 à 5 fiches** (dont `noirmont-deux-plongeuse-ceramique` en brouillon) :
  **4 visibles**, les 3 Héritage plus une. À reconsidérer avant de brancher les facettes Search & Discovery.
- **La collection `Classiques` passe de 16 à 18 fiches.** Cohérent avec `custom.famille = ["Classiques"]`.
- Les deux fiches restent de `productType` « Montre automatique », vendeur « Maison Noirmont ».

## 7. Ce que ce document n'établit pas

- **« Chiffres arabes » = les chiffres 1-12 occidentaux**, au sens de l'attribut vendeur et de la requête
  française. Le **chiffre arabe oriental** (١ ٢ ٣) n'existe nulle part sur un cadran de la chaîne
  d'approvisionnement. Si la grappe SEMrush visait ce second sens, **elle n'est toujours pas servie**.
- **Les visuels sont des images de synthèse fidèles, pas des photos de l'objet.** La fidélité a été contrôlée
  contre la photo fournisseur, cadran, lunette, couronne et bracelet compris — mais le diamètre, la finition
  réelle du boîtier et la nuance exacte du cuir ne seront confirmés qu'à réception d'un exemplaire.
- **La teinte du bronze est une extrapolation contrôlée.** Elle est cohérente avec la photo fournisseur du
  `bronze case-no logo`, mais le bronze patine : l'exemplaire livré ne sera pas exactement de cette nuance, et la
  description le dit.
- **Je n'ai pas jugé le sort de `noirmont-deux-plongeuse-ceramique`** (cadran bleu ciel à pastilles). Toujours en
  brouillon, toujours à trancher.

---

## 8. Second passage — les trois blocages levés

### 8.1 Les 16 médias de plongeuse — supprimés, mais seulement après trois vérifications

La condition posée était la **réversibilité**, pas la nature de l'appel d'API. Trois contrôles avant d'écrire.

**a. Aucune sauvegarde locale n'existait.** Recherche par motif (`558930`, `c-558930`, `noirmont-un`) sur tout
le dossier : les 16 fichiers CDN étaient **absents** de `boutique-seiko-mod/backups/backup-medias-partages-2026-07-26/` et d'ailleurs. Les
deux fichiers de `boutique-seiko-mod/livraisons/entrees-faces-REDONDANT-export-claude/` portent des noms voisins mais ne sont pas les mêmes
fichiers. **Les 16 ont donc été téléchargés d'abord**, dans
`boutique-seiko-mod/backups/backup-medias-plongeuse-supprimes-2026-07-27/`, nommés `<mediaId>_<nom CDN>.jpg`, avec un `MANIFESTE.json`.
**16/16 se rouvrent en 2048 × 2048 RGB** — vérifié fichier par fichier, aucun tronqué.

**b. Aucun n'était partagé.** Deux passes indépendantes :
1. index de l'URL CDN de **tous les médias des 100 produits** de la boutique → aucune collision sur les 16 ;
2. `files(query: "filename:…")` sur les trois préfixes → **un seul enregistrement `MediaImage` par fichier**.

Le partage existe bel et bien ailleurs sur cette boutique — `10977444528466-7.jpg` est sur les 12 chronographes,
`gmt-7.jpg` sur les 6 Voyageur, `10977444561234-7.jpg` sur les 7 Intégrale. **Aucun de ces fichiers-là n'était
concerné.** `productDeleteMedia` a donc bien **supprimé** nos 16, il ne les a pas détachés — ce qui rend la
sauvegarde préalable non pas prudente mais nécessaire.

> **Faux positif écarté.** `c-558930-bronze.jpg` (fiche acier) et `10977448558930-var-bronze.jpg` (fiche bronze)
> ont le **même contenu** (md5 `702c720e932bfef14dc504e32084f8db`). Ce sont deux **enregistrements de fichier
> distincts**, pas un fichier partagé : supprimer l'un n'a aucun effet sur l'autre. Vérifié avant d'écrire.

**c. Un piège que le brief ne mentionnait pas — l'image de variante.**
`c-558930-acier.jpg` n'était pas qu'un média de galerie : c'était **l'image des 6 variantes** de la fiche acier,
donc celle qui s'affiche quand le client choisit son calibre. La supprimer telle quelle aurait laissé les
6 variantes pointer vers un média détruit. **Les 6 variantes ont d'abord été réaffectées à la nouvelle face
aviateur**, puis le fichier a été supprimé. Idem côté bronze : les 6 variantes, qui n'avaient aucune image,
pointent maintenant sur la face bronze. **Aucun SKU, prix, prix barré ni option touché** — relu après écriture,
les 12 lignes sont identiques à la sauvegarde.

**Résultat : 12 médias supprimés sur la fiche acier, 4 sur la bronze, 0 erreur.**

### 8.2 Les trois visuels bronze — produits

| Slot | Fichier | Générations | Note |
|---|---|---:|---|
| `situation` | `noirmont-un-bronze-plongeuse-situation.jpg` | 1 | 1ᵉʳ jet, orientation correcte |
| `macro` | `noirmont-un-bronze-plongeuse-macro.jpg` | 1 + 2 | 2ᵉ passe |
| `poignet` | `noirmont-un-bronze-plongeuse-poignet.jpg` | 1 | 1ᵉʳ jet, doigts hors cadre |

**Le bloc d'orientation impératif a de nouveau payé — et de nouveau sur le seul défaut connu.** La première
`macro` bronze est sortie **cadran à l'envers** (couronne en bas à gauche, chiffres tête-bêche) :
`rejected/bronze-macro-v1-cadran-a-lenvers.jpg`. Le bloc a été renforcé (« every printed numeral must READ
RIGHT-SIDE UP », « NOT flipped, NOT rotated », « if in doubt, keep the reference framing and move the camera
closer ») et la reprise est bonne. **C'est le deuxième échec du chantier, et c'est encore l'orientation :
c'est le seul point sur lequel ce modèle décroche.**

Contrôle des chiffres en zoom fort sur les trois : couronne extérieure complète et dans l'ordre, couronne
intérieure 1→12 complète et dans l'ordre, triangle à midi, aucun texte, aucun logo. Même occultation naturelle
du « 10 » par l'aiguille des heures. Bronze chaud patiné, pas de l'or jaune.

**Coût du second passage : 6 générations, 24 crédits.** Total du chantier : **16 générations, 64 crédits**
(solde 269,46 → 209,46).

### 8.3 Les handles — corrigés

| Fiche | Handle avant | Handle après |
|---|---|---|
| `10977448558930` | `noirmont-un-plongeuse-acier` | **`montre-aviateur-acier-cadran-chiffres-arabes`** |
| `10978722087250` | `noirmont-un-bronze-plongeuse` | **`montre-aviateur-bronze-cadran-chiffres-arabes`** |

Le mot « plongeuse » ne travaille plus contre la requête visée. **Aucun conflit avec la fiche redondante**
`aviateur-acier-cadran-chiffres-arabes`, qui garde son handle intact : les nouveaux sont préfixés `montre-`.
Shopify n'a eu aucun suffixe à ajouter. Les deux fiches n'ayant jamais été publiques, aucun lien entrant ne
casse et aucune redirection n'était nécessaire.

> **Note.** Les **noms de fichiers** des visuels, eux, disent encore `noirmont-un-plongeuse-acier-*` et
> `noirmont-un-bronze-plongeuse-*` : ils ont été posés avant le changement de handle. C'est invisible du client
> (le nom de fichier CDN n'est pas une URL de page) et le renommer imposerait de re-téléverser les 8 médias.
> Laissé tel quel, mais à savoir si tu relis le manifeste.

### 8.4 Contrôle final

- **Galerie acier : 4 médias, tous « Aviateur acier à chiffres arabes ».** Plus une seule image de plongeuse.
- **Galerie bronze : 4 médias, tous « Aviateur bronze à chiffres arabes ».** Idem.
- **12 variantes relues une à une** : SKU, prix, prix barrés et stocks identiques à la sauvegarde
  (299/300 côté acier, 0 côté bronze comme avant). **Les compteurs DSers sont donc inchangés.**
- **Les trois fiches sont en `DRAFT`.** Rien n'a été publié.
- Collections : `Plongeuses` **5**, `Classiques` **18**, inchangé depuis le premier passage.

**Ce qui reste, et c'est court :** rattachement DSers à revérifier (dix secondes dans l'interface), diamètre de
boîtier toujours inconnu, et **aucun rendu de page n'a été vu** — le contrôle mobile-first des deux galeries
reste à faire avant publication.

---

*27/07/2026. Écritures : 4 `productUpdate` (titre, descriptionHtml, seo, tags, `custom.famille`,
`custom.bracelet`, handle), 8 médias créés, 16 médias supprimés après sauvegarde et contrôle de partage,
12 images de variante réaffectées, 2 réordonnancements, 2 `collectionAddProducts` / `collectionRemoveProducts`.
Aucun SKU, prix, prix barré, stock, variante, option, mapping DSers, thème, publication ni commande touché.
Aucune fiche supprimée. Aucun achat. 64 crédits.*

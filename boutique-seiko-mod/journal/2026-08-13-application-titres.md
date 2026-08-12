# Application des titres et meta titles du catalogue de pièces — T-25

**13/08/2026.** Boutique **Maison Noirmont**, sous mot de passe. Trois champs écrits sur Shopify —
`title`, `seo.title`, `seo.description` — sur **86 fiches en brouillon**. Aucun handle, aucune
description longue, aucune collection, aucun prix, aucun statut, aucun média n'a été touché. Aucun
`fileDelete`. Les 96 fiches actives n'ont pas été approchées.

---

## 1. En une phrase

Le défaut diagnostiqué par T-21 est corrigé : **les 86 fiches du lot importé portent désormais le
mot « montre » dans leur titre, leur meta title et leur meta description**, contre 10 titres sur 94
avant. **Deux titres proposés par T-21 ont été écartés parce qu'ils décrivaient un produit qui
n'existe plus**, et sept autres ont été corrigés sur le fond.

---

## 2. Le périmètre réel n'est pas 94, il est 86

T-21 a écrit ses tableaux le matin du 13/08, **avant** que l'audit des brouillons et le ménage de
catalogue ne soient soldés. Le relevé Shopify du soir donne :

| | |
|---|---|
| Brouillons au catalogue | **95** |
| dont brouillons **antérieurs** au lot de pièces (montres Noirmont, remontoirs, écrins) | 9 — **hors périmètre T-25** |
| Fiches du lot importé encore en DRAFT | **86** = 84 pièces + 2 montres-mod |
| Fiches listées par T-21 mais **archivées** depuis | **10** |
| Fiches importées le 11/08, absentes des tableaux T-21 | **2** (traitées quand même) |

**86 = 94 − 10 archivées + 2 arabes du 11/08.** Le compte de T-21 n'était pas faux, il était daté.

Les dix fiches archivées, non touchées : `mouvement-nh35-japon`, `cadran-transparent-lume-28-5`,
`cadran-sterile-bleu-lumineux-28-5`, `cadran-lumineux-28-5-nh35`, `cadran-sterile-index-35`,
`cadran-pilote-29-aiguilles-nh35`, `cadran-pilote-noir-33-5-nh35`, `cadran-retro-33-5-aiguilles-nh35`,
`cadran-plongee-33-5-aiguilles`, `montre-cadran-arabe-oriental-36-39`.

---

## 3. La règle appliquée

```
<Organe> de montre <cote> <caractéristique>, <coloris>, pour <calibre>
```

- l'organe suivi de **« de montre »** en tête : c'est l'expression mesurée (`cadran de montre` 480,
  `verre de montre` 880, `boitier montre` 1 600, `aiguilles montre` 140, `lunette montre` 390,
  `mouvement nh35` 590, `outil horloger` 390) ;
- **plafond 65 caractères** sur `seo.title` — il devient le titre du flux Shopping ;
- **meta description 150 à 160 caractères**, mot-clé cible dans les premiers mots ;
- « stérile », « pilote », « flieger » sortent de la tête de titre. « Sans logo » les remplace :
  c'est la même information, dite dans la langue de l'acheteur.

### Écart assumé sur la ponctuation

T-21 proposait le gabarit `… — <coloris>, pour <calibre>`, **avec tiret cadratin**. `STYLE-REDACTION.md`,
décidé par Hakim le même jour, **interdit le tiret cadratin** — c'est le premier item de sa table des
interdits, et le ticket demande explicitement de le respecter. **Les tirets cadratins ont donc été
remplacés par des virgules ou des deux-points** sur les 86 titres, 86 meta titles et 86 meta
descriptions. Aucun tiret cadratin ne subsiste dans les trois champs du lot. Le gabarit de T-21 doit
être corrigé sur ce point s'il est réutilisé.

---

## 4. Contrôle de véracité — les titres qui ont été refusés ou corrigés

Chaque titre proposé a été confronté à l'état Shopify courant de la fiche (titre audité le 13/08,
meta description, liste des variantes) et, pour les cas douteux, à la **description longue ouverte**.
Neuf écarts trouvés.

### 4.1 Deux titres proposés décrivaient un produit qui n'existe plus — écartés

| Fiche | Titre proposé par T-21 | Le produit réel | Décision |
|---|---|---|---|
| `insert-ceramique-chiffres-arabes-38` | « Lunette de montre, insert céramique 38 mm chiffres arabes — 4 finitions » | **insert « heure mondiale »** : graduation 24 heures et **codes de villes** (LAX, NYC, PAR, TYO…), **8 variantes**, aucun chiffre arabe | **Écarté.** Titre écrit sur le produit réel : « Lunette de montre heure mondiale, insert céramique 38 mm, graduation 24 h et villes ». Le titre proposé aurait annoncé un produit que l'acheteur ne reçoit pas. |
| `cadran-squelette-nh70-noir-argent` | « … noir ou argent, index lumineux, NH70/NH72 » | anneau **à tranche lisse, sans index** (le titre de la fiche l'a corrigé le 13/08) | **Écarté.** Titre écrit : « anneau lisse, noir ou argent ». Annoncer des index sur une pièce qui n'en a pas est une spécification inventée. |

### 4.2 Sept titres corrigés sur le fond

| Fiche | Le problème du titre proposé | Ce qui a été écrit |
|---|---|---|
| `cadran-texture-paon-29-sans-logo` | proposait « **effet plume** » — c'est précisément la caractéristique inventée trouvée et corrigée le 09/08 (« écailles de plume de paon ») | « texturé 29 mm **bleu paon**, noir ou blanc » — bleu paon est un **coloris**, lu sur la fiche, pas un motif |
| `cadran-sterile-vert-lumineux-28-5` | « Cadran de montre **vert** lumineux » → laisse croire à un cadran vert. La face existe en **sept teintes** ; c'est la **luminescence** qui est verte | « à luminescence verte, sans logo, **sept teintes** » |
| `cadran-evide-vert-nh70` | même piège : « squelette 31 mm **vert** lumineux ». Finitions réelles : noire, argentée, or rosé | « évidé 31 mm **à luminescence verte**, noir, argent ou or rosé » |
| `cadran-argente-sterile-29` | « Cadran de montre **argenté** … lumineux » — la fiche a été corrigée depuis : **cinq teintes**, chiffres 1-12 | « 29 mm à chiffres 1-12, sans logo, **cinq teintes** » |
| `cadran-squelette-nh70-3-coloris` | « noir, vert ou bleu » — la fiche en compte **sept teintes** depuis sa correction | « points lumineux, **7 teintes** » |
| `cadran-squelette-noir-blanc-29` | « noir **et blanc** » — finitions réelles : noire, argent, gris acier | « ajouré 29 mm, **noir ou argent** » |
| `cadran-squelette-29-noir-blanc` | la fiche vend **cinq sélections** dont « aiguilles seules » ; la description dit explicitement qu'**aucune luminescence n'est promise** faute de photo nocturne fiable | « 29 mm **ou aiguilles**, 5 sélections » ; la meta ne mentionne **aucune** luminescence, contrairement à l'ancienne qui annonçait des « index luminescents » |

### 4.3 L'alerte Super-LumiNova : respectée

`aiguilles-c3-super-lume-62` — T-21 signalait `super luminova` **320/mois**, le mot-clé le plus fort
de la famille aiguilles, à n'écrire **que si le fournisseur documente vraiment de la Super-LumiNova**.
La description fournisseur dit « **matière luminescente C3** » et précise que « C3 désigne une nuance,
pas une marque de qualité ». **Aucune source ne documente de la Super-LumiNova de marque : le mot n'a
pas été écrit.** Titre retenu : « Aiguilles de montre à luminescence C3, style plongée vintage ».
Les 320 recherches restent inaccessibles jusqu'à confirmation fournisseur.

### 4.4 Deux corrections de conformité au passage

- `insert-ceramique-chiffres-arabes-38` — l'ancien meta title contenait « **SKX** », référence de
  modèle tiers, écartée par l'audit GMC du 08/08. Elle a disparu du meta title. Le mot reste dans la
  description longue, où il désigne un **standard de boîtier** (« boîtiers de plongée type SKX ») ;
  c'est du contenu éditorial, pas un titre de flux.
- `cadran-lapis-lazuli-28-5` — « pierre **véritable** » figurait dans l'ancien titre. « Véritable »
  est un superlatif interdit par `STYLE-REDACTION.md`. Le fait est conservé, dit autrement :
  « lapis-lazuli **naturel** », et la meta précise « la pierre est naturelle, chaque pièce a son
  propre veinage ».

---

## 5. Résultat chiffré

| Contrôle sur les 86 fiches écrites | Avant | Après |
|---|---|---|
| `title` contenant « montre » | **9** | **86 / 86** |
| `seo.title` contenant « montre » | **5** | **86 / 86** |
| `seo.description` contenant « montre » | **15** | **86 / 86** |
| `seo.title` absent | 2 | **0** |
| `seo.description` entre 150 et 160 caractères | 5 | **86 / 86** |
| Fiches portant un tiret cadratin dans l'un des trois champs | **84** | **0** |
| Superlatif de la liste `STYLE-REDACTION.md` | 1 | **0** |

Répartition par organe : 6 outils · 5 mouvements · 6 verres · 10 boîtiers · 10 lunettes et inserts ·
10 aiguilles · 9 cadrans squelette · 12 cadrans sans logo · 10 cadrans à chiffres 1-12 ·
6 cadrans à chiffres arabes · 2 montres-mod.

---

## 6. Méthode et traçabilité

1. **Sauvegarde avant écriture** : `backups/2026-08-13-titres/avant.json` — les trois champs des
   86 fiches, plus la liste des 10 archivées et des 9 brouillons hors périmètre. Rien n'a été écrit
   avant que ce fichier existe.
2. **Fichier de sortie** : `backups/2026-08-13-titres/apres.json` — l'état visé, contrôlé
   automatiquement (présence du mot « montre », longueurs, absence de tiret cadratin et de
   superlatif) **avant** la première mutation.
3. **Écriture** : 9 lots de `productUpdate` par alias GraphQL, `userErrors` vide sur les 86.
4. **Vérification après écriture** : relecture complète des 95 brouillons depuis Shopify et
   comparaison champ par champ avec `apres.json`. **86 conformes, 9 fiches hors périmètre
   inchangées, 95 toujours en DRAFT.**

Un détail Shopify à connaître : **un `seo.title` identique au `title` du produit n'est pas stocké**,
l'API renvoie `null`. C'est arrivé sur `presse-aiguilles-base` ; le meta title a été reformulé pour
différer du titre. Second piège de la même famille : **`seo` est remplacé en bloc** — passer
`seo: {title: …}` seul efface la `description`. C'est arrivé une fois, réparé dans la foulée par une
écriture des deux champs.

---

## 7. Ce qui reste, et ce que ce travail a révélé

1. **Les handles n'ont pas bougé** — c'est la recommandation de T-21 §6 et la consigne du ticket.
   Trois handles contredisent maintenant plus nettement leur fiche :
   `insert-ceramique-chiffres-arabes-38` (le produit est une lunette **heure mondiale**),
   `cadran-calligraphie-arabe-email-33` (chiffres 1-12), `cadran-pilote-sterile-28-5-sans-logo`.
   → **T-24**.
2. **Les descriptions longues n'ont pas été touchées** (T-31, bloqué). Elles portent encore le
   vocabulaire « stérile / pilote » en tête et les marqueurs d'écriture IA. Le titre et la
   description ne parlent donc plus tout à fait la même langue tant que T-31 n'est pas passé.
3. **Les deux montres-mod restent rangées dans une collection de pièces** (`cadran-arabe`).
   Leur titre est propre, leur rattachement ne l'est pas. → **T-26**.
4. **Le tiret cadratin est encore partout ailleurs** : les 9 brouillons antérieurs et les 96 fiches
   actives portent tous des titres au tiret cadratin. Si `STYLE-REDACTION.md` vaut pour toute la
   boutique, c'est un chantier à ouvrir — hors périmètre ici, aucune fiche active n'a été touchée.
5. **Le gabarit de titre de T-21 est à corriger** dans le compte rendu de recherche : il contient un
   tiret cadratin que la règle de style interdit.

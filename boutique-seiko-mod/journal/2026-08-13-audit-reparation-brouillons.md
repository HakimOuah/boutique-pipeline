---
type: journal
boutique: seiko-mod
date: 2026-08-13
nature: analyse
leviers: [catalogue, creative, technique]
titre: "13/08/2026 — Audit des galeries des 95 brouillons après la session du 12/08 (T-16)"
---

# 13/08/2026 — Audit des galeries des 95 brouillons après la session du 12/08 (T-16)

Boutique **Maison Noirmont**, sous mot de passe. **Aucune mutation Shopify n'a été exécutée** :
l'audit conclut qu'il n'y a rien à réparer sur les brouillons. Aucun brouillon activé, aucune
collection publiée, aucun prix, SKU, statut ni image principale touché. Aucun `fileDelete`.

---

## 1. En une phrase

**Le ticket partait d'une hypothèse fausse.** Sur les brouillons, la session du 12/08 n'a **pas**
retiré de visuel maison : les **311 médias supprimés sont, à 100 %, des photos AliExpress brutes**,
et **chacune des 35 fiches touchées porte aujourd'hui un visuel maison conforme pour chacune de ses
apparences**. Le dégât est réel mais il est de **méthode** (311 suppressions définitives par
`fileDelete` au lieu du détachement réversible), pas de **contenu**.

---

## 2. Périmètre et méthode

**Périmètre réel** : 95 brouillons. Le fichier d'audit de la session fautive
(`preuves/2026-08-12-efficacite-extreme/audit-brouillons.json`, généré le 11/08 à 23:00 UTC, juste
avant la première mutation à 23:10) n'en couvre que **86** — sa requête était
`created_at:>='2026-08-08' AND status:draft`. Les **9 brouillons plus anciens** ont été traités
séparément (§ 5).

**Méthode**, reprise de celle de T-01 :

1. Relevé de l'état Shopify courant des 95 brouillons, médias paginés (1 420 médias au total).
2. Diff média par média, par GID, contre l'état d'avant.
3. **Classification indépendante** des retraits par signature de nom de fichier, sans faire confiance
   à la classification de la session fautive : `S<32 hexa><lettre>.webp` = fichier CDN AliExpress ;
   `<handle>-*.jpg` / `maison-noirmont-*.jpg` = livrable maison.
4. **Test d'existence** de chacun des 311 GID retirés (`nodes(ids:[…])`, 4 lots) pour distinguer
   détachement réversible et suppression définitive.
5. Croisement avec les groupes d'apparence de l'audit, pour savoir si un retrait laisse une
   apparence **sans contrepartie maison**.
6. Contrôle visuel des 146 visuels maison posés sur les brouillons : téléchargement, 13 planches en
   cadre complet, puis re-découpe et agrandissement sur les cadrans, couronnes, lunettes et
   platines de mouvement.

---

## 3. Le chiffrage du dégât

| | |
|---|---|
| Brouillons audités le 11/08 | 86 (sur 95) |
| Brouillons ayant **perdu** des médias | **35** |
| Médias retirés au total | **311** |
| dont **photos AliExpress brutes** | **311 — soit 100 %** |
| dont **visuels maison retirés à tort** | **0** |
| Retraits passés par `fileDelete`, **définitifs** | **311 — soit 100 %** |
| Retraits réversibles (`referencesToRemove`) | **0** |
| Visuels maison posés en échange | **146** |
| Brouillons tombés à 1 seul média | 9 |
| Brouillons touchés dont une apparence reste **sans visuel maison** | **0** |
| Brouillons touchés portant encore une photo AliExpress | **0** |

### Les 311 GID retirés n'existent plus

Les 311 identifiants ont été interrogés en quatre lots : **les 311 réponses sont `null`**. Aucun
n'est récupérable par `fileUpdate` + `referencesToAdd` — la session a bien utilisé `fileDelete`,
exactement ce que `REGLES.md` interdit depuis le 12/08. C'est le point aggravant du dossier, et il
est irréversible côté Shopify.

Liste complète, avec fiche, nom de fichier et URL CDN d'origine :
`preuves/2026-08-13-audit-brouillons/311-medias-supprimes-definitivement.json`.

### Aucun visuel maison n'a été perdu

C'est la différence de fond avec les fiches actives. Sur les actifs, 61 livrables maison avaient été
étiquetés « fournisseur » faute de fichier local retrouvé, puis retirés. Sur les brouillons, la même
règle défaillante a été appliquée — mais elle est tombée sur des galeries **entièrement** composées
de photos DSers, où elle ne pouvait pas se tromper. Les 311 noms de fichiers portent tous la
signature CDN AliExpress ; aucun `<handle>-*.jpg`, aucun `maison-noirmont-*.jpg`, aucun composite
`c-<id>-<coloris>.jpg` dans le lot.

### Les trois cas du ticket, mesurés

- **Cas 1 — visuel maison retiré à tort** : **0 occurrence**. Rien à restaurer.
- **Cas 2 — photo fournisseur retirée sans contrepartie maison** : **0 occurrence**. Trois fiches
  paraissaient en écart au premier comptage ; l'ouverture des groupes d'apparence montre que ce sont
  des **groupes techniques**, pas visuels : `presse-aiguilles-base` (7 « apparences » = 7 calibres
  2035 / 2671 / 2892-2824 / 3135 / 8500 / E2000 — un seul objet en laiton),
  `verre-saphir-dome-ar-bleu` (2 « apparences » = diamètres), `aiguilles-c3-super-lume-62`
  (le groupe `eta2824pt5000-silver` est couvert par le visuel argent). Aucune photo fournisseur n'a
  donc été retirée en laissant une apparence orpheline.
- **Cas 3 — photo fournisseur remplacée par un visuel maison conforme** : **les 311 retraits**.
  Retrait légitime au titre de la règle « ne jamais publier une photo AliExpress brute ».

**Conclusion : rien n'a été ré-attaché ni ré-uploadé, parce qu'il n'y avait rien à rendre.**
Restaurer les 311 photos AliExpress aurait été possible pour une petite part (§ 6), mais aurait
consisté à remettre dans les galeries exactement le matériau qui bloque l'activation, sur des fiches
qui n'en ont plus besoin.

---

## 4. Contrôle visuel des 146 visuels maison posés sur les brouillons

Les 146 médias ajoutés datent tous des **11 et 12/08** (67 et 79) : ils appartiennent au lot de 572
images déjà ouvert intégralement par T-03. Ils ont malgré tout été **ré-ouverts un par un** ici,
puisque ce sont eux qui portent désormais seuls les galeries concernées.

- 13 planches en cadre complet, puis agrandissements sur les familles à risque : montres finies
  `montre-sterile-40-nh35-saphir`, mouvements `nh36-jour-date` et `miyota-8215`.
- **Aucun logo, sigle, marque, formule de certification ni mention d'origine.** Les montres
  `sterile-40` (silhouettes GMT et plongeuse) ont des cadrans **strictement vierges** : ni texte à
  midi, ni ligne à 6 h.
- Aucun badge, aucune note, aucune étoile incrustée.
- La gravure `0160254M` lue sur la platine du NH36 est une **référence de pièce**, pas un nom de
  marque — même lecture que T-03.
- Les cadrans pilote portent la **flèche militaire générique** présente sur la pièce source.
- Les `alt` sont **tous renseignés et en français** ; aucun `alt` vide, aucun `alt` générique sur ce
  lot (le défaut de T-08 concerne `cadran-sterile-lumineux-28-5`, hors périmètre).

Planches et zooms : `preuves/2026-08-13-audit-brouillons/planche-0*.jpg` et `zoom-0*.jpg`.

---

## 5. Les 9 brouillons antérieurs au 08/08 — non couverts par l'audit, non touchés

Comparaison de leur nombre d'images avec `INVENTAIRE-VISUEL-2026-08-08.csv` :

| Fiche | 08/08 | Aujourd'hui |
|---|---|---|
| `contre-la-montre-chronographe-panda` | 25 | 25 |
| `integrale-sport-chic-acier` | 12 | 12 |
| `voyageur-gmt-automatique` | 11 | 11 |
| `heritage-plongeuse-vintage-42` | 8 | 8 |
| `remontoir-collection` | 6 | 6 |
| `remontoir-bois` | 5 | 5 |
| `rouleau-de-voyage-cuir` | 5 | 5 |
| `noirmont-deux-plongeuse-ceramique` | 5 | 5 |
| `aviateur-acier-cadran-chiffres-arabes` | **0** | **1** |

**Aucune perte.** Le seul mouvement est un **gain** : `aviateur-acier-cadran-chiffres-arabes`, qui
était à zéro image depuis le 08/08, a reçu son premier visuel maison le 12/08.

---

## 6. Ce qui est irrécupérable — et ce que ça coûte réellement

Les 311 photos fournisseur détruites **ne sont pas récupérables depuis Shopify**. Elles ne sont pas
non plus dans `livraisons/`, qui ne contient que des livrables maison. Reste :

- **`sources-fournisseur-2026-08/`** conserve **une** photo de face par fiche — 33 des 35 fiches
  touchées en ont une (les deux manquantes sont les imports à handle brut de T-04). Cela couvre
  environ **10 %** du matériau détruit, et uniquement la vue principale.
- **21 des 35 fiches** ont leur **identifiant AliExpress tracé** dans les lots d'exécution. Pour
  celles-là, les photos d'origine sont re-téléchargeables via l'API officielle (règle T-05b), pour
  une fraction du coût d'une session navigateur.
- Pour les **14 fiches restantes**, l'identifiant fournisseur n'est pas tracé : il faudrait le
  retrouver avant tout re-téléchargement.

**Mais rien de tout cela n'est nécessaire aujourd'hui** : ces 35 fiches sont couvertes par des
visuels maison conformes. Le matériau perdu n'aurait servi que de **source de composition** pour de
futurs visuels — et il ne le sera plus. C'est le seul coût réel : si l'un de ces 35 produits demande
plus tard un visuel supplémentaire (autre angle, macro, mise en situation), la photo fournisseur qui
aurait servi de base devra être re-téléchargée depuis AliExpress. → **T-23**

---

## 7. Ce que l'audit révèle par ailleurs

**60 brouillons sur 95 portent encore 1 091 photos AliExpress brutes** — 39 n'ont *que* ça, 13 sont
mixtes, et 8 des 9 anciens brouillons sont concernés. Ce n'est pas une régression : c'est l'état
d'origine, et c'est très exactement le périmètre de **T-07**. Le chiffre manquait jusqu'ici ; il est
maintenant établi et réparti fiche par fiche dans
`preuves/2026-08-13-audit-brouillons/INVENTAIRE-95-BROUILLONS-2026-08-13.csv`.

Répartition des 95 brouillons au 13/08 :

| | |
|---|---|
| 100 % visuels maison, aucune photo brute — **activables sur le critère visuel** | **43** |
| Mixtes (maison + photos brutes) | 13 |
| 100 % photos AliExpress brutes | 39 |
| Total médias | 1 420 — dont 329 maison et 1 091 fournisseur |

---

## 8. Ce que je n'ai pas fait, et pourquoi

- **Aucun média ré-attaché ni ré-uploadé** : il n'y avait aucun visuel maison à rendre, et remettre
  des photos AliExpress sur des fiches déjà couvertes aurait ajouté du matériau interdit à la
  publication sans rien apporter.
- **Aucun `fileDelete`**, aucun détachement, aucune modification de galerie, d'`alt`, de prix, de
  statut ou d'image principale.
- **Les 96 fiches actives n'ont pas été touchées**, conformément au ticket.

## 9. Traçabilité

Tout est dans `preuves/2026-08-13-audit-brouillons/` :

- `INVENTAIRE-95-BROUILLONS-2026-08-13.csv` — les 95 fiches, ligne par ligne : médias avant, médias
  aujourd'hui, retraits, méthode, nature, visuels maison posés, couverture, source locale.
- `311-medias-supprimes-definitivement.json` — les 311 GID détruits, avec fiche, nom de fichier et
  URL CDN d'origine.
- `146-visuels-maison-poses.json` — les 146 médias ajoutés, avec GID, URL et `alt`.
- `diff-brouillons-avant-apres.txt` — le diff brut, fiche par fiche.
- `planche-000.jpg` … `planche-012.jpg` — les 146 visuels en cadre complet.
- `zoom-00.jpg` … `zoom-04.jpg` — les agrandissements cadrans et mouvements.

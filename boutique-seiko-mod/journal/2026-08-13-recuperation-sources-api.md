---
type: journal
boutique: seiko-mod
date: 2026-08-13
nature: intervention
leviers: [sourcing, technique]
titre: "13/08/2026 — Reconstitution des sources fournisseur détruites le 12/08 (T-23)"
---

# 13/08/2026 — Reconstitution des sources fournisseur détruites le 12/08 (T-23)

Boutique **Maison Noirmont**. **Aucune écriture Shopify**, aucune commande, aucun achat, aucun
navigateur. Le ticket ne fait que reconstituer un stock local de matière première pour les
compositions à venir.

---

## 1. En une phrase

**Les 311 photos fournisseur détruites le 12/08 sont toutes revenues** — 311 sur 311, sur les
35 fiches, plus 11 images de variantes que les galeries ne portaient pas. **Les 35 fiches ont leur
identifiant AliExpress**, dont 30 confirmés par recoupement d'image exact ; aucune n'est laissée
sans source.

---

## 2. Ce qui a été monté avant de télécharger

Le ticket annonçait 21 fiches à identifiant tracé et 14 à retrouver. Le chiffre était pessimiste :
deux registres locaux indépendants portaient déjà l'identifiant de 33 fiches sur 35.

| Registre | Ce qu'il donne |
|---|---|
| `sources-fournisseur-2026-08/<handle>/face-fournisseur-<item_id>.jpg` | l'identifiant est dans le nom de la photo de face conservée |
| `textes-fiches-2026-08-09.json` | 94 fiches avec `item_id` + `handle` + `shopify_id` |
| `journal/2026-08-12-abandon-fiches-marquage-physique.md` | les 2 imports à handle brut du 11/08 |

Les deux premiers **concordent sur les 33 handles** qu'ils ont en commun, sans une seule divergence.

**Le piège évité** : `PREFLIGHT-DSERS-CADRAN-ARABE-1005007347658552-2026-08-11.json` associe l'item
`1005007347658552` au produit Shopify `11017842360658`, qui est `new-arabic-sky-blue-…`. C'est faux.
Le recoupement d'image ci-dessous donne **0 correspondance sur 26** pour cet item, contre **25 sur 26**
pour `1005009751528666`. Un rattachement sur cette base aurait produit des visuels d'un autre produit.

---

## 3. La preuve d'identité : recoupement d'image exact

Les 311 médias détruits sont enregistrés par l'audit du 13/08 avec leur **nom de fichier CDN
AliExpress d'origine** (`S<32 hexa><lettre>`). L'endpoint `variants` de la passerelle renvoie, pour
chaque SKU, l'URL de son image de propriété. **Si un nom de fichier détruit réapparaît dans la
réponse API d'un item, l'identité fiche ↔ item est établie, pas supposée.**

| Niveau de confirmation | Fiches | Ce qu'il vaut |
|---|---:|---|
| **Image API exacte** — au moins un nom de fichier détruit retrouvé dans la réponse `variants` | **30** | preuve directe |
| **Titre API + 2 registres locaux concordants** | **5** | l'API ne publie aucune image de propriété pour ces items ; le titre décrit le bon produit et les deux registres locaux donnent le même identifiant |
| Non identifiées | **0** | — |

Les 5 fiches du second niveau sont `boitier-octogonal-42-fond-saphir`, `mouvement-nh35-date-blanche`,
`presse-aiguilles-base`, `verre-saphir-dome-1-2` et `verre-saphir-dome-1-5`. Aucune n'a été rattachée
sur une ressemblance visuelle.

---

## 4. Ce qui a été récupéré

**322 images, 128 Mo, 35 fiches.** Rangées en `sources-fournisseur-2026-08/<handle>/galerie/` et
`…/variantes/`, à côté de la photo de face déjà présente.

| | |
|---|---:|
| Photos détruites le 12/08 | 311 |
| **Photos de galerie revenues** | **311 — soit 100 %** |
| Images de variantes en plus, absentes des galeries | 11 |
| Fiches réapprovisionnées | **35 sur 35** |
| Fiches restant sans source | **0** |
| Images par fiche | 2 à 26, médiane 8 |

Avant ce ticket, le stock local était d'une photo de face pour 33 fiches sur 35 — environ 10 % du
matériau. Il est désormais **complet**, et les deux fiches qui n'avaient rien (les imports à handle
brut de T-04) sont couvertes.

### Détail par fiche

| Handle | Item AliExpress | Détruites | Récupérées | Confirmation |
|---|---|---:|---:|---|
| `28-5mm-dial-diy-arabic-alphabet-surface-no-date-…` | `1005007348127532` | 16 | 16 | image API |
| `aiguilles-baton-argent-nh35` | `1005007884473587` | 9 | 9 | image API |
| `aiguilles-c3-super-lume-62` | `1005010529978866` | 7 | 7 | image API |
| `aiguilles-dauphine-polies-nh35` | `1005007896534058` | 12 | 12 | image API |
| `boitier-argente-36-39-biseaute` | `1005006489170451` | 10 | 10 | image API |
| `boitier-octogonal-42-fond-saphir` | `1005008639164026` | 5 | 5 | titre + 2 registres |
| `boitier-pilote-pvd-noir-36-39` | `1005009937589354` | 10 | 10 | image API |
| `boitier-saphir-36-40-nh35` | `1005006783022622` | 10 | 10 | image API |
| `cadran-arabe-oriental-noir-blanc-28-5` | `1005012137091344` | 7 | 7 | image API |
| `cadran-argente-sterile-29` | `1005006987515689` | 9 | 9 | image API |
| `cadran-ciel-etoile-28-5` | `1005010692631891` | 7 | 7 | image API |
| `cadran-evide-vert-nh70` | `1005008066853454` | 11 | 11 | image API |
| `cadran-pilote-33-5-aiguilles-lumineuses` | `1005010303631276` | 5 | 13 | image API |
| `cadran-pilote-noir-33-5-nh34` | `1005008660462030` | 3 | 6 | image API |
| `cadran-pilote-sterile-28-5-sans-logo` | `1005009643278179` | 8 | 8 | image API |
| `cadran-retro-blanc-rose-nh35` | `1005008468061052` | 11 | 11 | image API |
| `cadran-squelette-29-noir-blanc` | `1005009288581598` | 10 | 10 | image API |
| `cadran-squelette-ajoure-index-metal` | `1005007676819549` | 7 | 7 | image API |
| `cadran-squelette-nh70-3-coloris` | `1005008395512841` | 13 | 13 | image API |
| `enrouleur-ressort-nh35` | `1005008717442651` | 6 | 6 | image API |
| `montre-sterile-40-nh35-saphir` | `1005005673324130` | 12 | 12 | image API |
| `mouvement-miyota-8215-nh34-gmt` | `1005012175538270` | 10 | 10 | image API |
| `mouvement-nh35-date-blanche` | `1005008494235697` | 6 | 6 | titre + 2 registres |
| `mouvement-nh35-date-rouge` | `1005009853779041` | 12 | 12 | image API |
| `mouvement-nh36-jour-date` | `1005007995556187` | 13 | 13 | image API |
| `new-arabic-sky-blue-nh35-28-5mm-sunburst-…` | `1005009751528666` | 26 | 26 | image API |
| `porte-mouvement-nh35` | `1005008518115553` | 7 | 7 | image API |
| `presse-aiguilles-base` | `1005008635496479` | 2 | 2 | titre + 2 registres |
| `set-aiguilles-lumineuses-nh35` | `1005007733703969` | 9 | 9 | image API |
| `support-mouvement-aluminium` | `1005010551172634` | 7 | 7 | image API |
| `verre-saphir-dome-1-2` | `1005007976167717` | 5 | 5 | titre + 2 registres |
| `verre-saphir-dome-1-5` | `1005004810355096` | 5 | 5 | titre + 2 registres |
| `verre-saphir-dome-ar-bleu` | `1005010361616521` | 7 | 7 | image API |
| `verre-saphir-loupe-30-5` | `1005004587063688` | 8 | 8 | image API |
| `verre-saphir-plat-28-38` | `1005008965173152` | 6 | 6 | image API |

---

## 5. Route utilisée, et pourquoi elle tient

**Passerelle VPS en lecture seule** `codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, vers
AliExpress Open Platform / AE-Dropshipper. `health` sain à `2026-08-12T22:43:23Z` ; jeton d'accès
valide jusqu'au `2026-09-01T18:29:47Z`. **35 appels `variants`**, 35 réussites, 0 erreur. Elle fournit
le titre officiel, le vendeur, les ventes, le statut, et les images de propriété SKU.

**Les fichiers d'origine viennent du CDN AliExpress** `ae01.alicdn.com/kf/<nom>.jpg`, en pleine
résolution, par requête HTTP directe. C'est la même route que celle documentée dans la mémoire
projet pour les photos, et le seul moyen de récupérer **exactement** les fichiers détruits, puisque
la passerelle expose les images de propriété SKU mais pas la galerie brute. Aucun navigateur, aucun
anti-bot touché.

**Piège d'extension** : 23 fichiers répondaient `404` en `.jpg` et sont servis en `.png`. La reprise
avec repli d'extension les a tous ramenés. Sans ce repli, on aurait conclu à tort que 23 sources
avaient disparu de chez le fournisseur.

---

## 6. Contrôle qualité — cadran par cadran

Les 322 images ont été assemblées en 35 planches et relues, avec agrandissement sur les familles
porteuses de cadran : cadrans-pièces, montre finie, boîtiers montés, mouvements.

**Aucune image écartée. 0 sur 322.** Aucun logo, aucune marque, aucune formule de certification et
aucune mention d'origine **sur un cadran**. Les cadrans stériles sont strictement nus.

### Ce qui a été vu et jugé acceptable

**Filigranes de vendeur incrustés dans la photo** — hors produit, conformes à la consigne du ticket.
Six vendeurs concernés : `XinXin Store` (`new-arabic-sky-blue-…`), `Neiton Office store`
(`cadran-argente-sterile-29`), `NH watch Store` (`cadran-squelette-nh70-3-coloris`), `alpha dial`
(`cadran-pilote-sterile-28-5-sans-logo`), `CORGEUT` (`boitier-pilote-pvd-noir-36-39`), `GRAYSS`
(`boitier-octogonal-42-fond-saphir`), `Tandorio` (`cadran-pilote-33-5-aiguilles-lumineuses`).

⚠️ **Deux points d'attention pour la génération du 18/08** :

- **`cadran-pilote-33-5-aiguilles-lumineuses`** — le filigrane `Tandorio` est un **logo de marque**
  posé en surimpression dans l'angle de chaque photo. Il n'est **pas** sur le cadran : les cadrans
  ne portent que leurs chiffres et leur minuterie. La source est utilisable, mais le filigrane ne
  doit jamais passer dans une composition. Même vigilance pour `alpha dial`, dont le filigrane est
  posé **en travers du cadran** et gêne la lecture des index.
- **`montre-sterile-40-nh35-saphir`** — le cadran porte physiquement
  `AUTOMATIC / WATER RESISTANT / 100m-330ft`. C'est du générique technique réellement gravé : il se
  garde, au titre de la précision du 12/08 dans `REGLES.md`. En revanche le **bracelet porte `904L`
  imprimé en rouge**, et `904L` a été purgé de la boutique le 08/08 avec redirections 301. Ce n'est
  pas sur le cadran, donc la source reste valide, mais **`904L` ne doit apparaître dans aucun
  livrable**.

`cadran-retro-blanc-rose-nh35` était sous surveillance parce que son titre AliExpress commence par
« Tandorio ». Vérification faite : **les onze cadrans sont nus**, chiffres et minuterie seulement,
aucun marquage physique. Le nom de marque ne vit que dans le titre du vendeur.

---

## 7. Table de correspondance

Créée : **`journal/data/table-correspondance-handle-aliexpress.csv`** — **96 lignes**, une par fiche
importée, versionnée. Colonnes : `handle`, `item_id`, `shopify_id`, `touche_12_08`, `detruites`,
`recuperees`, `confirmation`, `ventes`, `titre_api`.

Elle couvre les 94 fiches du lot du 09/08 **et** les 2 imports à handle brut du 11/08. C'est
désormais le point unique où lire l'identifiant fournisseur d'une fiche, au lieu de le déduire d'un
nom de fichier.

⚠️ **T-04 va renommer les deux handles bruts**. La table devra être reprise à ce moment-là : la clé
est le `handle`, pas le `shopify_id`.

---

## 8. Ce que je n'ai pas fait

- **Aucune mutation Shopify** : ni média, ni `alt`, ni prix, ni SKU, ni statut, ni collection. Aucun
  `fileDelete`, aucun `fileUpdate`.
- **Aucune commande, aucun achat**, ni AliExpress ni DSers.
- **Aucun navigateur.** Les endpoints `search` et `exact` n'ont pas servi : `search` n'a été essayé
  qu'une fois, sur le premier handle brut, et le tri par ventes ne remontait que des articles
  populaires sans rapport. Le recoupement d'image l'a rendu inutile.
- **Aucune source rattachée sur une ressemblance.** Les 35 identifiants sont confirmés par image
  exacte ou par deux registres concordants plus le titre officiel.
- **Rien n'a été forcé dans git** : `sources-fournisseur-2026-08/` reste ignoré.

## 9. Traçabilité

- `sources-fournisseur-2026-08/MANIFESTE-RECUPERATION-2026-08-13.json` — les 322 images, par fiche,
  avec taille et SHA-256. Non versionné, comme les images.
- `journal/data/table-correspondance-handle-aliexpress.csv` — versionné.
- `preuves/2026-08-13-audit-brouillons/311-medias-supprimes-definitivement.json` — la liste d'entrée,
  produite par T-16.

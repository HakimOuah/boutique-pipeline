# Réconciliation de la campagne « 319 visuels » — 10/08/2026

Contrôle local, en lecture seule. Aucun accès à Shopify ou DSers n'a été effectué. Le périmètre
réconcilié est celui de l'inventaire du 08/08/2026 et de ses priorités P0 à P5, avec une cible de
5 images par montre et 3 images par accessoire.

## Verdict

La file restante des **fiches actives** est de **238 fichiers à produire**, et non 253 ni 319 :

- **9** visuels de galerie ;
- **33** visuels de variantes de montres ;
- **196** visuels de variantes d'accessoires et bracelets.

Les six images du `bracelet-caoutchouc-gaufre` ont depuis été affectées à **12 variantes**
(deux largeurs par couleur) par le coordinateur via `productVariantAppendMedia`. Cette correction
live a été vérifiée indépendamment par lui à 6 médias/12 variantes ; elle ne change pas le solde de
production de 238 fichiers. La présente sous-tâche n'a pas refait d'accès Shopify.

Le chiffre **319** est arithmétiquement reproductible, mais il mélange **304 besoins actifs** et
**15 besoins de brouillons**. Si Hakim décidait ultérieurement de traiter P5, la file de production
passerait de 238 à **253** fichiers, soit 238 actifs + 15 brouillons historiques.

## 1. Reconstruction du chiffre 319

| Besoin au 08/08 | Tous statuts | Actifs | Brouillons | Explication |
|---|---:|---:|---:|---|
| Galerie | 74 | **69** | **5** | Les 5 brouillons sont la galerie vide d'`Aviateur Acier — Cadran à chiffres arabes`. |
| Variantes de montres | 43 | **33** | **10** | `Noirmont Deux` = 7 et `Voyageur` = 3 sont des brouillons. |
| Variantes accessoires/bracelets | 202 | **202** | 0 | Les 34 fiches de P4 sont actives dans l'inventaire. |
| **Total** | **319** | **304** | **15** | `74 + 43 + 202 = 319`, mais `69 + 33 + 202 = 304` pour les actifs. |

La galerie a été recalculée ligne par ligne depuis `INVENTAIRE-VISUEL-2026-08-08.csv` : cible 5
pour les types de montre, cible 3 pour les autres types. Le résultat est 69 manques actifs et 5
manques brouillons. Il explique l'écart que les documents de mission ne rendaient pas explicite.

### Incohérence P3 expliquée

Le titre « 5 fiches, 43 visuels » ne correspond pas au tableau : il y a **6 produits actifs**
(`Explorateur`, deux `Éclaireur`, deux `Squelette`, `Trente-Neuf Duo`) totalisant
`12 + 10 + 8 + 1 + 1 + 1 = 33` manques. Les 10 manques supplémentaires viennent des deux
brouillons cités sous le tableau. Le bon objectif P3 actif est donc **33**, pas 43.

## 2. Production et rattachement sur le périmètre actif

| Priorité | Cible active | Livré local | Reste à produire | État de rattachement |
|---|---:|---:|---:|---|
| P0 — galeries critiques | 14 | 6 | **8** | Les 6 sont rattachés. |
| P1 — 5e image des montres | 41 | 41 | **0** | Les 41 sont rattachés, y compris les deux macros Noirmont Un corrigées au tour 46. |
| P2 — 3e image des accessoires | 14 | 13 | **1** | Les 13 sont rattachés. |
| P3 — variantes montres actives | 33 | 0 | **33** | Aucun média produit. |
| P4 — variantes accessoires | 202 | 6 | **196** | Les 6 médias sont rattachés et affectés à 12 variantes, deux largeurs par couleur. |
| **Total actif** | **304** | **66** | **238** | 60 visuels de galerie + 6 actifs de variante présents sur les fiches. |

Deux mesures ne doivent donc pas être confondues :

- **production de fichiers** : 66/304, reste exact **238** ;
- **affectation des six fichiers P4 déjà livrés** : terminée sur 12 variantes, deux largeurs par
  couleur, d'après la vérification live transmise par le coordinateur le 10/08.

Le journal de rattachement ferme son relevé sur **76 fichiers présents sur 62 fiches**, dont
**66 concernent cette campagne active** et **10 concernent cinq nouvelles fiches `cadran-*` en
brouillon**, hors inventaire du 08/08. Il consigne également un rollback historique d'un média de
cadran brouillon. Ces dix médias et ce rollback ne changent pas le solde des actifs.

## 3. Réconciliation des fichiers locaux

### Sous-ensemble stable de la campagne active

Le contrôle direct des manifests retrouve exactement :

- **60** entrées `slot: galerie` ;
- **6** entrées `slot: variante` ;
- **66/66** fichiers présents et référencés ;
- **66/66** JPEG RGB de 2048 × 2048 avec profil ICC, de 362 707 à 1 159 382 octets ;
- **66/66** chemins de source résolus, en interprétant les chemins soit depuis la racine du dépôt,
  soit depuis `boutique-seiko-mod/`, conformément aux deux conventions réellement utilisées.

`ETAT-LIVRAISON.md` compte **24 fichiers rejetés** pour ce lot initial. Ils restent hors manifests
et ne sont donc pas déduits du besoin.

### Pourquoi les totaux globaux du dossier divergent

Au pointage du 10/08 à 00:27 CEST, le dossier de livraison contenait 76 manifests et 103 fichiers
référencés : 66 du lot actif ci-dessus et **37 visuels de nouvelles fiches cadran en brouillon**,
avec des slots `face`, `macro` ou `situation`. Quatre autres images étaient alors présentes à la
racine de `cadran-pilote-noir-33-5-nh34/` sans manifeste final, pendant que la file de production
continuait d'évoluer.

Conséquences :

- le chiffre **66** d'`ETAT-LIVRAISON.md` est périmé pour le dossier global, mais reste exact pour
  le lot actif P0-P4 ;
- les **77 fichiers** de la clôture du journal étaient un instantané antérieur ;
- les cadrans brouillons produits ensuite ne doivent être imputés ni aux 15 besoins P5 historiques,
  ni aux 238 fichiers actifs restants ;
- un fichier sans manifeste final n'est pas compté comme livré.

## 4. Sources disponibles et sources manquantes

### Ressources locales disponibles

| Ressource | Présence observée | Portée réelle |
|---|---:|---|
| `boutique-seiko-mod/livraisons/visuels-2026-07-25/generated/` | 77 fichiers | Faces déjà générées ; utiles seulement si la référence exacte et l'absence de marque sont prouvées. |
| `boutique-seiko-mod/livraisons/visuels-2026-07-25/reference/` | 10 fichiers | Références nettoyées, couverture partielle. |
| `boutique-seiko-mod/preuves/preuves-fournisseur-2026-07-27/` | 2 fichiers | Preuves fournisseur locales très partielles. |
| `boutique-seiko-mod/backups/backup-sku-2026-08-08/table-correspondance.jsonl` | 935 lignes | Pont local handle/variante/fragment SKU ; ne prouve pas l'apparence du coloris. |
| Sauvegarde fournisseur du bracelet gaufré | 42 fichiers | A permis les six variantes argentées retenues ; ne suffit pas à valider les autres rendus. |

La présence d'un fichier ou d'un fragment SKU n'est pas une preuve d'appariement visuel. Le
`storefront-best-practices` impose aussi de ne pas confondre une image de galerie avec l'image qui
doit suivre le choix de variante du client.

### Manques bloquants, par lot

| Lot restant | Volume | Source observée / manque |
|---|---:|---|
| `Trente-Neuf Rose` — galerie | 4 | Seule face locale observée avec « SWISS MADE » ; aucune autre source propre. |
| `Bracelet FKM — tropical` — galerie | 2 | Gros plan partiel, marquage masqué et embossage douteux ; pas de vue produit complète propre. |
| Carte cadeau — galerie | 2 | Aucune source produit locale exploitable. |
| `Remontoir Solo` — galerie | 1 | Seule face locale avec gravure de marque ; aucune autre source propre validée. |
| P3 montres actives | 33 | Fragments SKU identifiés, mais pas de nuanciers propres et appariés. Les squelettes noirs n'ont pas de référence du bon boîtier ; le `Trente-Neuf Duo` ne permet pas de prouver 36/39 mm. |
| Bracelet caoutchouc gaufré P4 | 30 | Sources et mapping partiels disponibles ; 27 boucles noire/dorée/or rose ont échoué en fidélité géométrique et 3 teintes claires ont échoué sur la matière/sous-face. |
| Bracelet FKM tropical P4 | 36 | Même absence de source/nuancier complet et propre que pour sa galerie. |
| Autres P4 | 130 | Le brief affirme que les nuanciers existent dans les archives fournisseur, mais aucun manifest de livraison ne valide encore leur appariement exact. À traiter comme **sources candidates**, pas comme preuves acquises. |
| **Total à produire** | **238** | 9 galerie + 33 P3 + 196 P4. |

## 5. File d'exécution recommandée

1. **Clore les galeries actives : 9 fichiers.** Obtenir des sources alternatives propres pour les
   quatre fiches bloquées ; sinon acter explicitement l'abandon de chaque slot, ce qui changera la
   cible et non le nombre de fichiers livrés.
2. **P3 : 33 fichiers.** Re-sourcer les nuanciers propres et appariés des six produits actifs avant
   toute génération ; c'est le déficit variante le plus visible pour l'acheteur.
3. **P4 : 196 fichiers.** Traiter séparément : 30 gaufrés, 36 FKM tropical, puis 130 autres. Exiger
   une preuve image + fragment SKU pour chaque coloris avant de produire.
4. **P5 : 15 fichiers hors file active.** Ne les ouvrir que si les fiches historiques concernées
   repassent en vente. Les nouveaux cadrans brouillons ne soldent pas P5.

## 6. Sources du calcul

- `2026-08-08-brief-visuels-codex.md` : inventaire agrégé, cibles 74/245/319 et tableaux P0-P5.
- `2026-08-08-consignes-codex-visuels.md` : règles galerie/variante, manifests et périmètre de tous les coloris.
- `INVENTAIRE-VISUEL-2026-08-08.csv` : recalcul actif/brouillon ligne par ligne.
- `boutique-seiko-mod/livraisons/visuels-codex-2026-08/ETAT-LIVRAISON.md` : 60 galeries, 6 variantes, 24 rejets et blocages source.
- `2026-08-09-rattachement-visuels.md` : 64 rattachements initiaux, deux macros actives ajoutées,
  dix médias cadran brouillons et état historique avant affectation des six variantes.
- Mise à jour live du coordinateur, 10/08/2026 : six médias P4 affectés à 12 variantes et contrôle
  indépendant 6 médias/12 variantes. Cette sous-tâche locale ne l'a pas vérifiée dans Shopify.
- Les 76 `manifeste.json` et leurs fichiers présents au pointage local du 10/08/2026.

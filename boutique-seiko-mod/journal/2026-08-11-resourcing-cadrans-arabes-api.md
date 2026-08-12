# Re-sourcing élargi des cadrans à chiffres arabes orientaux — API — 11/08/2026

## Verdict

**PARTIEL — 1 nouveau produit distinct qualifié : `1005007347658552`.**

Cette passe réduit le manque délégué de **3–7** à **2–6 produits distincts supplémentaires**. Elle ne compte jamais les coloris comme des produits différents.

Frontières respectées : AliExpress Open Platform / AE-Dropshipper via le gateway VPS officiel en lecture seule ; aucun navigateur AliExpress ; aucune mutation Shopify, DSers, commande, paiement, ordre image ou JSON maître.

## Produit qualifié

| Champ | Preuve live |
|---|---|
| Item | `1005007347658552` |
| Titre API | Cadran de montre 28.5mm, Surface à motifs solaires, Alphabet arabe avec Date, cadrans de montre, accessoires de remplacement pour mouvement NH35/NH36 |
| Ventes | **164** |
| Statut | **onSelling** |
| Évaluations / note renvoyées par `variants` et `exact` | **0 / 0,0** — la qualification ne s'appuie pas sur la note de la grille de recherche |
| Vendeur | **Watch DlY Factory Store** — article 4,8 ; communication 4,8 ; expédition 4,8 |
| Taille / compatibilité | **28,5 mm ; NH35 / NH36**, prouvés par le titre produit officiel, non testés physiquement |
| Construction | Surface rayonnée, fenêtre de date à 3 h |
| QA glyphes | **PASS** — `١٢`, `٣`, `٦`, `٩` clairement confirmés sur les images SKU exactes |
| QA texte | **PASS** — aucun nom, logo, mot, lettre ou verbatim sur les cadrans physiques ; seulement des graduations numériques occidentales de minuterie |
| Relevés live | variantes : 11/08/2026 18:49:43 UTC ; fret exact : 18:53:41 UTC |

### Six SKU exacts exploitables

| SKU | Variante | Prix TTC | Stock | Fret France exact | Délai | Coût rendu | Décision |
|---|---|---:|---:|---:|---|---:|---|
| `12000040362692622` | rose - Coffee | 8,59 € | 945 | 1,99 € | 8–13 j | 10,58 € | PASS |
| `12000040362692623` | Rose Black | 8,69 € | 942 | 1,99 € | 9–13 j | 10,68 € | PASS |
| `12000040362692624` | Gold Black | 8,69 € | 976 | 1,99 € | 9–13 j | 10,68 € | PASS |
| `12000040362692625` | Rose White | 8,59 € | 979 | 1,99 € | 8–13 j | 10,58 € | PASS |
| `12000040362692629` | Silver Green | 8,89 € | 7 | 1,99 € | 8–12 j | 10,88 € | PASS, stock fragile |
| `12000040362692631` | Silver Pink | 8,59 € | 932 | 1,99 € | 9–13 j | 10,58 € | PASS |

Pour les six lignes : **AliExpress Selection Standard**, code `CAINIAO_FULFILLMENT_STD`, départ Chine, suivi, livraison non gratuite.

### SKU exclus

| SKU | Variante | Stock | Motif |
|---|---|---:|---|
| `12000040362692632` | Silver White | 0 | rupture |
| `12000040362692633` | Silver Blue | 0 | rupture |
| `12000040362692627` | Silver Black | 0 | rupture |
| `12000040362692628` | Gold White | 0 | rupture |
| `12000040362692630` | Silver - Light Blue | 0 | rupture |
| `12000040362692626` | gold | 953 | le gateway refuse la qualification exacte : trois SKU correspondent au libellé ; exclusion plutôt que deviner |

## Recontrôles imposés

### Quasi-candidat `1005012130205925`

Relevé live du 11/08/2026 à 18:45:03 UTC : **9 ventes**, statut `onSelling`, 5 variantes, stock 97–99. Les images restent compatibles avec les glyphes orientaux et l'absence de verbatim, mais la règle `>= 10 ventes` impose encore le **REFUS**.

### Tri `latest`

Les 12 requêtes Unicode et multilingues ont été retentées avec la limite API valide de 20. Résultat : **12/12 `IOPUpstreamError`**, aucun résultat exploitable. Les mêmes 12 requêtes en tri `orders` ont réussi.

## Couverture élargie

- **266 appels de recherche officiels** dans cette passe : 250 réponses réussies, 12 erreurs amont persistantes sur `latest`, 4 erreurs de transport transitoires ensuite retentées avec succès.
- **1 246 item IDs distincts** observés dans les réponses réussies.
- Requêtes anglaises, françaises, arabes, persanes et russes ; glyphes Unicode ; surfaces avec/sans date ; 27/28,5/29/30,5/31/31,8/33,5 mm ; NH35/NH36/NH70/Miyota/ETA ; variantes de couleur ; termes vendeur et fragments exacts du titre.
- Audit visuel de grandes fiches génériques : `1005005858795927` (111 images), `1005004795495451` (51), `1005008479227962` (40), `1005008652921836` (32), `1005010666569615` (35), `1005009995195099` (19), `1005009995274657` (9), `1005007629207114` (17). Aucun cadran oriental sans verbatim n'y apparaît.

## Refus représentatifs

| Item | Ventes | Preuve image | Décision |
|---|---:|---|---|
| `1005009068454676` | 12 | cadrans avec `660ft-200m PROFESSIONAL AUTOMATIC` | REFUS texte/verbatim |
| `1005010669957383` | 19 | chiffres romains occidentaux, pas de glyphes orientaux | REFUS glyphes |
| `1005009139338114` | 420 | disques stériles sans chiffres | REFUS glyphes |
| `1005010382006253` | 249 | index bâtons et `AUTOMATIC` | REFUS glyphes + texte |
| `1005009499092622` | 190 | toutes les variantes `S Dial` | REFUS marque |
| `1005009354807415` | 12 | toutes les variantes `S Logo` | REFUS marque |
| `1005010330728083` | 19 | toutes les variantes `S Logo` | REFUS marque |
| `1005010171619128` | 25 | toutes les variantes `S Logo` | REFUS marque |
| `1005010217420381` | 50 | toutes les variantes `S Logo` | REFUS marque |
| `1005012753213344` | 2 | intitulé pertinent mais sous le seuil de ventes | REFUS ventes |

## Preuves autonomes

- `boutique-seiko-mod/preuves/preuves-sourcing-api-2026-08-11-agent/1005007347658552.json` — produit, QA, exact-SKU, stock, fret France et exclusions ;
- `boutique-seiko-mod/preuves/preuves-sourcing-api-2026-08-11-agent/1005007347658552-variantes.jpg` — planche des 12 sources SKU officielles, SHA-256 `5d0f4c77336128183d67c5a4d6d43f137524860f13a9093e43269795523a4ba2` ;
- `boutique-seiko-mod/preuves/preuves-sourcing-api-2026-08-11-agent/1005007347658552-sources/` — douze images SKU officielles avec hashes individuels dans le JSON.

## Décision opérationnelle

Le seul nouvel item qualifié est `1005007347658552`, avec **six SKU exacts retenus**. Il ne doit pas être importé automatiquement : refaire `variants` et `exact` juste avant toute future décision, surtout pour `Silver Green` qui ne disposait plus que de 7 unités.


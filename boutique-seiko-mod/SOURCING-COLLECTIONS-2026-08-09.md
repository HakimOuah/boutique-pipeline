# Sourcing collections « Pièces & Mod » + cadran arabe — nuit du 08 au 09/08/2026

**Mission** : décision 6 de Hakim (08/08) — passer Maison Noirmont de 92 à 200+ fiches sur le gate v3 (10-20 produits/sous-catégorie, ordre 80/20 best-sellers d'abord). Ce registre alimente le push DSers, la rédaction et la génération d'images.

## ⚠️ Niveau de preuve de la nuit — À LIRE AVANT EXÉCUTION

**Aucune classe A cette nuit : mur anti-bot AliExpress documenté.** Les pages produit (PDP) refusent systématiquement de charger leurs données dans le navigateur intégré (squelette CSR permanent, l'API de données ne part jamais ; en émulation mobile, reCAPTCHA explicite). Conformément aux consignes, rien n'a été contourné. Les SERP (rendues côté serveur) et l'API publique d'avis fonctionnent, elles.

**Chaque candidat ci-dessous est donc en niveau B+**, c'est-à-dire :
- **B** — prix, note et « vendus » relevés dans le **JSON structuré de la SERP** (champs séparés `salePrice` / `starRating` / `tradeDesc` : pas de collage note-ventes possible, mais chiffres SERP quand même — à confirmer PDP) ;
- **+** — **note et nombre d'avis vérifiés par l'API publique d'avis** de la fiche (source que la PDP elle-même consulte) avec dates des derniers avis et pays acheteurs ; **41/99 fiches ont des acheteurs FR parmi leurs 20 derniers avis** (signal livraison France) ; **10 faces relues en photo HD** pour la stérilité (résultats en colonne Réserves).

**Montée en classe A obligatoire à l'étape DSers** (Chrome de Hakim) : à l'ouverture de chaque fiche pour l'import, relever prix de variante, ventes PDP, délai France, vendeur, et confirmer la stérilité de la variante commandée. **Tout écart = retirer la ligne, ne pas pousser.** Les fiches Choice n'affichent souvent aucun pays d'expédition : réserve standard.

**Interdits vérifiés** : 2 fiches écartées en QA photo (texte « SUPERLATIVE CHRONOMETER OFFICIALLY CERTIFIED » imprimé au cadran), 1 conditionnelle (« RLATIVE CHRONO »). Aucun titre fournisseur ne doit jamais être repris (plusieurs citent Seiko/Rolex/IWC/Breitling par style).

**Échelle de prix relevée en boutique (connecteur Shopify, lecture seule, 09/08)** : montres 279-429 €, remontoirs 59,90-219,90 €, bracelets 29,90-59,90 €, outillage 12,90-59,90 €, rolls 49,90 €, coffrets 24,90-94,90 €. Les prix proposés ci-dessous s'y calent (pièces de mod : 19,90-89,90 € ; mouvements 89,90-169,90 € ; montres 329-429 €).

**Photos fournisseur** : face téléchargée pour les 99 fiches dans `sources-fournisseur-2026-08/<handle>/` (hors git, .gitignore mis à jour). Les galeries complètes et photos de variantes sont à récupérer à l'étape DSers (PDP bloquée cette nuit).

## Cadrans arabes orientaux (pièces) — 4 produits retenus

**Mot-clé / volume** : `seiko arabic dial` 8 100/mois — grappe arabic dial ≈ 15 500/mois (marche-complet-semrush.md §2.1/§10)

*Offre usine orientale stérile toujours rare (constat du 30/07 confirmé) : 4 cadrans pièces seulement au niveau d'exigence maison. La collection d'acquisition « Cadran arabe » atteint 10 produits en y rattachant les 5 montres finies ci-dessous et l'insert céramique arabe (collection lunettes).*

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005007976392353](https://fr.aliexpress.com/item/1005007976392353.html) | Cadran oriental Sunburst 29 mm — noir/bleu/vert | `cadran-arabe-oriental-sunburst-29` | 6,39 € | 34,90 € | 4.7/5 · 10 avis | 103 | oui | MATELION = nom vendeur au titre ; sterilite cadran a confirmer photo ; QA photo : orientaux + mot 'Automatic' (logo MATELION = filigrane photo, pas sur cadran) |
| 2 | [1005012137091344](https://fr.aliexpress.com/item/1005012137091344.html) | Cadran oriental noir & blanc 28,5 mm | `cadran-arabe-oriental-noir-blanc-28-5` | 8,39 € | 34,90 € | 5.0/5 · 2 avis | 36 | — | Option logo perso : commander SANS logo uniquement ; QA photo : chiffres orientaux, AUCUN texte — la meilleure face orientale de la nuit |
| 3 | [1005009056835202](https://fr.aliexpress.com/item/1005009056835202.html) | Cadran oriental argenté convexe 28,5 mm | `cadran-arabe-oriental-argent-28-5` | 21,99 € | 49,90 € | 5.0/5 · 1 avis | 23 | — | QA photo : orientaux + mot 'Automatic' en cursive a 6h (meme compromis que dossier 30/07 — arbitrage Hakim) |
| 4 | [1005011774911570](https://fr.aliexpress.com/item/1005011774911570.html) | Cadran émaillé bleu étoilé 28,5 mm — arabes et romains, sans logo | `cadran-arabe-romain-emaille-bleu-28-5` | 12,59 € | 39,90 € | 0 avis retournés | 21 | — | QA photo : aventurine bleue, variante chiffres orientaux sertis — aucun texte |
| ⚠️ | [1005009469054356](https://fr.aliexpress.com/item/1005009469054356.html) | Cadran chiffres arabes orientaux 28,5 mm — NH35/NH36 | `cadran-nh35-chiffres-arabes-orientaux-28-5` | 4,69 € | 34,90 € | 4.9/5 · 35 avis | 343 | oui | **CONDITIONNEL — 343 ventes SERP mais texte 'RLATIVE CHRONO OFFICIALLY CERTIFIED' imprime sur TOUTES les faces vues — NE POUSSER QUE si une variante vierge est confirmee a l'ouverture DSers** |

## Montres cadran arabe (finies) — 5 produits retenus

**Mot-clé / volume** : grappe arabic dial ≈ 15 500/mois ; `seiko mod arabic dial` 720/mois

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005005673165828](https://fr.aliexpress.com/item/1005005673165828.html) | Pilote-plongeuse 39 mm 20 bar — chiffres 1-12 | `montre-pilote-plongee-39-chiffres-arabes` | 76,99 € | 329,00 € | 4.7/5 · 281 avis | +1000 | — | Verifier variante sterile au mapping (gamme Tandorio) |
| 2 | [1005005673324130](https://fr.aliexpress.com/item/1005005673324130.html) | Montre stérile 40 mm NH35 — 10 ATM saphir | `montre-sterile-40-nh35-saphir` | 113,39 € | 379,00 € | 4.7/5 · 37 avis | 315 | — | QA photo : plongeuse type SUB, texte generique 'AUTOMATIC WATER RESISTANT 100m:330ft', aucune marque |
| 3 | [1005010249362754](https://fr.aliexpress.com/item/1005010249362754.html) | Montre chiffres orientaux 36/39 mm — Miyota 8215 (dossier 30/07) | `montre-cadran-arabe-oriental-36-39` | 101,99 € | 349,00 € | 4.7/5 · 3 avis | 10 | — | Preuve sociale mince (dossier complet du 30/07) ; variantes -sterile uniquement ; mot Automatic imprime : arbitrage Hakim rendu ? |
| 4 | [1005006492769759](https://fr.aliexpress.com/item/1005006492769759.html) | Montre chiffres orientaux 36/39 mm — NH35 20 ATM | `montre-cadran-arabe-oriental-nh35` | 112,39 € | 379,00 € | 5.0/5 · 1 avis | 8 | — | Jumeau NH35 du dossier 30/07, preuve sociale mince |
| 5 | [1005012493670989](https://fr.aliexpress.com/item/1005012493670989.html) | Field titane 39 mm — chiffres 1-12, saphir | `montre-field-titane-39-chiffres-arabes` | 108,69 € | 429,00 € | 5.0/5 · 1 avis | 3 | — | Gamme premium ; preuve sociale mince |

## Cadrans pilote chiffres 1-12 — 14 produits retenus

**Mot-clé / volume** : famille `seiko mod` 38 690/mois KD 10 (requête large) ; pas de tête dédiée mesurée — longue traîne descriptive gate v3

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005010303631276](https://fr.aliexpress.com/item/1005010303631276.html) | Cadran pilote 33,5 mm + aiguilles lumineuses — 4 coloris | `cadran-pilote-33-5-aiguilles-lumineuses` | 9,39 € | 36,90 € | 4.9/5 · 54 avis | 366 | — | — |
| 2 | [1005007635155982](https://fr.aliexpress.com/item/1005007635155982.html) | Cadran pilote classique 29 mm — NH35/NH36 | `cadran-pilote-29-classique-nh36` | 10,99 € | 36,90 € | 4.9/5 · 23 avis | 329 | — | — |
| 3 | [1005008660462030](https://fr.aliexpress.com/item/1005008660462030.html) | Cadran noir 33,5 mm — NH34/NH35/NH36 | `cadran-pilote-noir-33-5-nh34` | 10,99 € | 36,90 € | 4.9/5 · 33 avis | 324 | — | — |
| 4 | [1005009148826972](https://fr.aliexpress.com/item/1005009148826972.html) | Cadran pilote 29 mm — NH35 à NH72 | `cadran-pilote-29-mod-nh35` | 5,69 € | 29,90 € | 4.8/5 · 37 avis | 310 | — | — |
| 5 | [1005006012512581](https://fr.aliexpress.com/item/1005006012512581.html) | Cadran pilote classique 29 mm + aiguilles — NH35/NH36 | `cadran-pilote-29-aiguilles-nh35` | 15,29 € | 44,90 € | 5.0/5 · 35 avis | 286 | — | Choice : pays d expedition non affiche en SERP |
| 6 | [1005009253533306](https://fr.aliexpress.com/item/1005009253533306.html) | Cadran pilote 33,5 mm + aiguilles blanches — NH35/NH36 | `cadran-pilote-33-5-aiguilles-blanches` | 5,49 € | 34,90 € | 4.8/5 · 42 avis | 237 | — | — |
| 7 | [1005003002119259](https://fr.aliexpress.com/item/1005003002119259.html) | Cadran noir 33,5 mm — NH34/NH36/NH35/PT5000 | `cadran-pilote-noir-33-5-nh35` | 13,69 € | 39,90 € | 4.8/5 · 16 avis | 130 | — | — |
| 8 | [1005008468061052](https://fr.aliexpress.com/item/1005008468061052.html) | Cadran rétro mat blanc/rosé — NH35/NH36/NH38 | `cadran-retro-blanc-rose-nh35` | 9,59 € | 36,90 € | 4.9/5 · 18 avis | 108 | oui | — |
| 9 | [1005008471050885](https://fr.aliexpress.com/item/1005008471050885.html) | Cadran rétro 33,5 mm + aiguilles — NH35/NH36/NH38 | `cadran-retro-33-5-aiguilles-nh35` | 14,99 € | 44,90 € | 5.0/5 · 14 avis | 74 | oui | — |
| 10 | [1005009101607137](https://fr.aliexpress.com/item/1005009101607137.html) | Cadran pilote 38 mm + aiguilles — 4 coloris lumineux | `cadran-pilote-38-aiguilles-nh35` | 14,99 € | 44,90 € | 4.9/5 · 9 avis | 54 | — | — |
| 11 | [1005009643278179](https://fr.aliexpress.com/item/1005009643278179.html) | Cadran pilote stérile 28,5 mm — sans logo | `cadran-pilote-sterile-28-5-sans-logo` | 12,19 € | 39,90 € | 5.0/5 · 7 avis | 54 | — | — |
| 12 | [1005008580932006](https://fr.aliexpress.com/item/1005008580932006.html) | Cadran émail calligraphie 33,2 mm — NH35 | `cadran-calligraphie-arabe-email-33` | 10,79 € | 39,90 € | 5.0/5 · 5 avis | 52 | — | QA photo : chiffres 1-12 email colores pop, sterile ; la fiche vend aussi boitier/bracelet assortis |
| 13 | [1005008481615291](https://fr.aliexpress.com/item/1005008481615291.html) | Cadran plongée 33,5 mm + aiguilles — marron/blanc/bleu | `cadran-plongee-33-5-aiguilles` | 9,39 € | 36,90 € | 4.7/5 · 6 avis | 38 | — | — |
| 14 | [1005009148482089](https://fr.aliexpress.com/item/1005009148482089.html) | Cadran stérile 29 mm date + aiguilles — chiffres 1-12 | `cadran-sterile-date-aiguilles-29` | 3,39 € | 29,90 € | 5.0/5 · 2 avis | 14 | — | QA photo : chiffres 1-12 steriles (filigrane Tandorio sur photo seulement) |

## Cadrans stériles couleur & texture — 15 produits retenus

**Mot-clé / volume** : famille `seiko mod` 38 690/mois ; `mod nh35` 20/mois — longue traîne descriptive

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005007629207114](https://fr.aliexpress.com/item/1005007629207114.html) | Cadran stérile lumineux 28,5 mm — 4 coloris | `cadran-sterile-lumineux-28-5` | 6,69 € | 34,90 € | 4.9/5 · 165 avis | +900 | — | — |
| 2 | [1005008380303345](https://fr.aliexpress.com/item/1005008380303345.html) | Cadran Sunburst 28,5 mm — noir/argent/bleu/vert | `cadran-sterile-sunburst-28-5` | 3,39 € | 29,90 € | 4.7/5 · 73 avis | +800 | oui | — |
| 3 | [1005005879175706](https://fr.aliexpress.com/item/1005005879175706.html) | Cadran stérile bleu lumineux 28,5 mm | `cadran-sterile-bleu-lumineux-28-5` | 6,79 € | 34,90 € | 4.8/5 · 95 avis | +600 | — | — |
| 4 | [1005009995274657](https://fr.aliexpress.com/item/1005009995274657.html) | Cadran lumineux 28,5 mm — NH35/8215/2824 | `cadran-lumineux-28-5-nh35` | 4,59 € | 29,90 € | 4.7/5 · 85 avis | 454 | oui | — |
| 5 | [1005010122830689](https://fr.aliexpress.com/item/1005010122830689.html) | Cadran texture paon 29 mm — sans logo | `cadran-texture-paon-29-sans-logo` | 11,39 € | 39,90 € | 4.9/5 · 80 avis | 440 | — | — |
| 6 | [1005006987515689](https://fr.aliexpress.com/item/1005006987515689.html) | Cadran argenté stérile 29 mm lumineux | `cadran-argente-sterile-29` | 5,99 € | 34,90 € | 4.7/5 · 40 avis | 315 | oui | — |
| 7 | [1005004795495451](https://fr.aliexpress.com/item/1005004795495451.html) | Cadran stérile 28,5 mm + aiguilles | `cadran-sterile-28-5-aiguilles` | 5,89 € | 34,90 € | 4.8/5 · 63 avis | 286 | oui | — |
| 8 | [1005009523161505](https://fr.aliexpress.com/item/1005009523161505.html) | Cadran stérile vert lumineux 28,5 mm | `cadran-sterile-vert-lumineux-28-5` | 6,69 € | 34,90 € | 4.9/5 · 51 avis | 264 | oui | — |
| 9 | [1005010122462262](https://fr.aliexpress.com/item/1005010122462262.html) | Cadran stérile 29 mm saumon/noir/blanc + aiguilles | `cadran-sterile-saumon-29-aiguilles` | 11,39 € | 39,90 € | 4.9/5 · 29 avis | 240 | — | — |
| 10 | [1005008812013694](https://fr.aliexpress.com/item/1005008812013694.html) | Cadran pierre Lapis-Lazuli 28,5 mm — stérile | `cadran-lapis-lazuli-28-5` | 35,19 € | 89,90 € | 4.9/5 · 27 avis | 182 | oui | Pierre naturelle : variations par piece a assumer en fiche |
| 11 | [1005008397086684](https://fr.aliexpress.com/item/1005008397086684.html) | Cadran stérile 28,5 mm couronne 3 h — 4 coloris | `cadran-sterile-couronne-3h-28-5` | 8,89 € | 34,90 € | 5.0/5 · 4 avis | 163 | — | — |
| 12 | [1005009761337861](https://fr.aliexpress.com/item/1005009761337861.html) | Cadran vierge stérile 28,5 mm — 6 coloris | `cadran-vierge-sterile-28-5` | 3,59 € | 29,90 € | 4.8/5 · 10 avis | 140 | — | — |
| 13 | [1005009479823229](https://fr.aliexpress.com/item/1005009479823229.html) | Cadran météorite 28,5 mm — sans logo | `cadran-meteorite-28-5` | 15,29 € | 44,90 € | 5.0/5 · 6 avis | 47 | — | QA photo : textures meteorite index/diamants, sans texte — premium ; variantes arabes eventuelles a verifier |
| 14 | [1005010465015558](https://fr.aliexpress.com/item/1005010465015558.html) | Cadran stérile index 35 mm — sans logo | `cadran-sterile-index-35` | 5,59 € | 34,90 € | 5.0/5 · 7 avis | 33 | — | Titre fournisseur cite des marques : ne jamais reprendre le titre ; QA photo : faces index steriles sans texte (pas d'orientaux sur la face) — verifier variantes arabes au mapping |
| 15 | [1005010692631891](https://fr.aliexpress.com/item/1005010692631891.html) | Cadran ciel étoilé émaillé 28,5 mm — sans logo | `cadran-ciel-etoile-28-5` | 11,89 € | 39,90 € | 4.8/5 · 4 avis | 28 | oui | QA photo : ciel etoile sans texte ni chiffres — sterile propre |

## Cadrans squelette (NH70/NH72) — 10 produits retenus

**Mot-clé / volume** : `montre squelette` ≈ 8 400/mois (grappe, §3) — pièces rattachées à la collection squelette existante

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005005282410219](https://fr.aliexpress.com/item/1005005282410219.html) | Cadran squelette NH70/NH72 — anneau lumineux | `cadran-squelette-nh70-anneau-lumineux` | 8,29 € | 34,90 € | 4.9/5 · 53 avis | 460 | oui | — |
| 2 | [1005009076254369](https://fr.aliexpress.com/item/1005009076254369.html) | Cadran squelette NH70/NH72 — noir/argent | `cadran-squelette-nh70-noir-argent` | 9,99 € | 34,90 € | 4.9/5 · 17 avis | 141 | — | — |
| 3 | [1005012089200639](https://fr.aliexpress.com/item/1005012089200639.html) | Cadran squelette transparent 31,8 mm | `cadran-squelette-transparent-31-8` | 10,39 € | 36,90 € | 4.7/5 · 17 avis | 137 | — | — |
| 4 | [1005007676819549](https://fr.aliexpress.com/item/1005007676819549.html) | Cadran squelette ajouré — index métalliques | `cadran-squelette-ajoure-index-metal` | 6,69 € | 29,90 € | 4.9/5 · 17 avis | 136 | oui | — |
| 5 | [1005009288581598](https://fr.aliexpress.com/item/1005009288581598.html) | Cadran squelette 29 mm — noir/blanc | `cadran-squelette-29-noir-blanc` | 9,04 € | 34,90 € | 5.0/5 · 20 avis | 131 | oui | — |
| 6 | [1005007524889100](https://fr.aliexpress.com/item/1005007524889100.html) | Cadran transparent lumineux 28,5 mm | `cadran-transparent-lume-28-5` | 3,39 € | 24,90 € | 4.9/5 · 14 avis | 110 | oui | — |
| 7 | [1005008066853454](https://fr.aliexpress.com/item/1005008066853454.html) | Cadran évidé vert — NH70 | `cadran-evide-vert-nh70` | 7,59 € | 29,90 € | 4.9/5 · 12 avis | 105 | — | — |
| 8 | [1005008395512841](https://fr.aliexpress.com/item/1005008395512841.html) | Cadran squelette NH70/NH72 — 3 coloris | `cadran-squelette-nh70-3-coloris` | 12,99 € | 39,90 € | 4.9/5 · 11 avis | 86 | oui | — |
| 9 | [1005006777442209](https://fr.aliexpress.com/item/1005006777442209.html) | Cadran creux plaque circulaire — NH70/NH72 | `cadran-creux-plaque-circulaire-nh70` | 11,99 € | 36,90 € | 5.0/5 · 9 avis | 79 | oui | — |
| 10 | [1005009022665700](https://fr.aliexpress.com/item/1005009022665700.html) | Cadran squelette 29 mm noir & blanc (Tandorio) | `cadran-squelette-noir-blanc-29` | 18,49 € | 49,90 € | 5.0/5 · 8 avis | 59 | — | — |

## Aiguilles (NH35/NH36/NH34) — 10 produits retenus

**Mot-clé / volume** : NON MESURÉ en propre (`outil barrette montre` non mesuré non plus) — longue traîne famille seiko mod 38 690

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005007306682346](https://fr.aliexpress.com/item/1005007306682346.html) | Jeu d'aiguilles NH35 — or rosé/argent, lume vert | `aiguilles-nh35-or-rose-argent` | 2,56 € | 19,90 € | 4.9/5 · 190 avis | +5000 | — | — |
| 2 | [1005008659046962](https://fr.aliexpress.com/item/1005008659046962.html) | Jeu d'aiguilles plongeuse NH34/NH35/NH36 | `aiguilles-plongeuse-nh35` | 3,19 € | 19,90 € | 4.9/5 · 1016 avis | +5000 | oui | Titre fournisseur cite des modeles tiers : ne jamais reprendre |
| 3 | [1005008616812146](https://fr.aliexpress.com/item/1005008616812146.html) | Jeu d'aiguilles vintage NH35/NH36 | `aiguilles-vintage-sub-nh35` | 4,09 € | 19,90 € | 4.8/5 · 543 avis | +4000 | oui | — |
| 4 | [1005007896534058](https://fr.aliexpress.com/item/1005007896534058.html) | Aiguilles Dauphine polies — style cocktail | `aiguilles-dauphine-polies-nh35` | 3,49 € | 19,90 € | 4.7/5 · 480 avis | +4000 | — | — |
| 5 | [1005007884473587](https://fr.aliexpress.com/item/1005007884473587.html) | Aiguilles bâton argent poli — NH35/NH36 | `aiguilles-baton-argent-nh35` | 3,29 € | 19,90 € | 4.7/5 · 323 avis | +3000 | — | — |
| 6 | [1005007733703969](https://fr.aliexpress.com/item/1005007733703969.html) | Set d'aiguilles lumineuses — NH34/NH35/NH36 | `set-aiguilles-lumineuses-nh35` | 3,69 € | 19,90 € | 4.9/5 · 319 avis | +2000 | oui | — |
| 7 | [1005008382665794](https://fr.aliexpress.com/item/1005008382665794.html) | Aiguilles GMT NH34 — lume bleu-vert | `aiguilles-gmt-nh34` | 6,79 € | 24,90 € | 4.9/5 · 118 avis | +900 | oui | — |
| 8 | [1005008331507670](https://fr.aliexpress.com/item/1005008331507670.html) | Aiguilles cathédrale — or/noir/or rosé/argent | `aiguilles-cathedrale-nh35` | 3,69 € | 19,90 € | 4.9/5 · 105 avis | +700 | oui | — |
| 9 | [1005008019163632](https://fr.aliexpress.com/item/1005008019163632.html) | Aiguilles sport — NH34 à NH72 | `aiguilles-sport-nh34-nh72` | 3,69 € | 19,90 € | 4.9/5 · 129 avis | +700 | oui | — |
| 10 | [1005010529978866](https://fr.aliexpress.com/item/1005010529978866.html) | Aiguilles C3 Super-Lume plongeuse vintage | `aiguilles-c3-super-lume-62` | 6,49 € | 24,90 € | 4.9/5 · 40 avis | +600 | — | — |

## Lunettes & inserts (SKX 38 mm) — 10 produits retenus

**Mot-clé / volume** : NON MESURÉ en propre — longue traîne famille seiko mod 38 690

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005008645932150](https://fr.aliexpress.com/item/1005008645932150.html) | Insert de lunette aluminium 38 mm plat | `insert-lunette-aluminium-38-plat` | 4,29 € | 24,90 € | 4.8/5 · 153 avis | +900 | oui | — |
| 2 | [1005007843450973](https://fr.aliexpress.com/item/1005007843450973.html) | Insert aluminium plat 38 × 31,5 mm | `insert-lunette-aluminium-38-31-5` | 4,29 € | 24,90 € | 4.7/5 · 155 avis | +900 | — | — |
| 3 | [1005009341063856](https://fr.aliexpress.com/item/1005009341063856.html) | Insert céramique incliné 38 mm — lumineux | `insert-ceramique-incline-38-lumineux` | 7,69 € | 29,90 € | 4.8/5 · 85 avis | 482 | — | — |
| 4 | [1005007863813766](https://fr.aliexpress.com/item/1005007863813766.html) | Insert résine plate 38 × 31,5 mm | `insert-resine-38-31-5` | 5,99 € | 24,90 € | 4.9/5 · 71 avis | 437 | — | — |
| 5 | [1005007512911309](https://fr.aliexpress.com/item/1005007512911309.html) | Insert céramique lumineux 38 mm plat | `insert-ceramique-lumineux-38-plat` | 9,89 € | 34,90 € | 4.8/5 · 96 avis | 421 | — | — |
| 6 | [1005007293732155](https://fr.aliexpress.com/item/1005007293732155.html) | Insert céramique incurvé 38 mm | `insert-ceramique-incurve-38` | 6,99 € | 29,90 € | 4.9/5 · 61 avis | 367 | — | — |
| 7 | [1005009534631613](https://fr.aliexpress.com/item/1005009534631613.html) | Insert aluminium GMT 38 mm | `insert-aluminium-gmt-38` | 9,79 € | 29,90 € | 5.0/5 · 40 avis | 267 | — | — |
| 8 | [1005009525190588](https://fr.aliexpress.com/item/1005009525190588.html) | Insert lunette bleu lumineux 38 mm | `insert-lunette-bleu-lumineux-38` | 11,99 € | 34,90 € | 4.8/5 · 20 avis | 102 | — | — |
| 9 | [1005008927121122](https://fr.aliexpress.com/item/1005008927121122.html) | Insert aluminium 38 mm — diamètre intérieur 30 mm | `insert-aluminium-38-di-30` | 7,59 € | 24,90 € | 4.9/5 · 17 avis | 73 | — | — |
| 10 | [1005006297065004](https://fr.aliexpress.com/item/1005006297065004.html) | Insert céramique chiffres arabes 38 mm — 4 coloris | `insert-ceramique-chiffres-arabes-38` | 12,39 € | 39,90 € | 5.0/5 · 5 avis | 18 | oui | Pont avec la collection cadran arabe |

## Boîtiers NH35/NH36 — 10 produits retenus

**Mot-clé / volume** : `seiko mod kit complet` 90/mois ; longue traîne famille seiko mod

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005006783022622](https://fr.aliexpress.com/item/1005006783022622.html) | Boîtier verre saphir 36/40 mm — NH34/NH35/NH36 | `boitier-saphir-36-40-nh35` | 28,59 € | 89,90 € | 4.9/5 · 255 avis | +5000 | oui | — |
| 2 | [1005008309552951](https://fr.aliexpress.com/item/1005008309552951.html) | Boîtier lunette cannelée 36/39 mm — saphir | `boitier-lunette-cannelee-36-39` | 19,99 € | 79,90 € | 4.7/5 · 784 avis | +5000 | oui | — |
| 3 | [1005007805509882](https://fr.aliexpress.com/item/1005007805509882.html) | Boîtier plongée 40 mm 200 m + bracelet jubilé | `boitier-plongee-40-200m-jubile` | 43,79 € | 119,90 € | 4.9/5 · 146 avis | +3000 | — | — |
| 4 | [1005009141784587](https://fr.aliexpress.com/item/1005009141784587.html) | Boîtier argent 40 mm saphir — lunette 120 clics | `boitier-argent-40-saphir-120-clics` | 31,19 € | 99,90 € | 4.9/5 · 495 avis | +2000 | oui | — |
| 5 | [1005007805695119](https://fr.aliexpress.com/item/1005007805695119.html) | Boîtier saphir étanche — noir/or/rosé | `boitier-saphir-noir-or-rose` | 27,79 € | 89,90 € | 4.9/5 · 79 avis | +2000 | oui | — |
| 6 | [1005008639164026](https://fr.aliexpress.com/item/1005008639164026.html) | Boîtier octogonal acier 42 mm — fond saphir | `boitier-octogonal-42-fond-saphir` | 39,99 € | 119,90 € | 4.7/5 · 341 avis | +2000 | oui | — |
| 7 | [1005007313498737](https://fr.aliexpress.com/item/1005007313498737.html) | Boîtier 36/40 mm — 4 finitions, NH34 à NH72 | `boitier-36-40-4-finitions` | 22,39 € | 79,90 € | 4.8/5 · 222 avis | +1000 | oui | — |
| 8 | [1005006993985843](https://fr.aliexpress.com/item/1005006993985843.html) | Boîtier plongée 40 mm lunette noire — saphir, fond verre | `boitier-plongee-40-lunette-noire` | 21,79 € | 79,90 € | 4.9/5 · 50 avis | +1000 | oui | — |
| 9 | [1005006489170451](https://fr.aliexpress.com/item/1005006489170451.html) | Boîtier argenté 36/39 mm saphir biseauté | `boitier-argente-36-39-biseaute` | 15,99 € | 69,90 € | 4.9/5 · 180 avis | +900 | — | — |
| 10 | [1005009937589354](https://fr.aliexpress.com/item/1005009937589354.html) | Boîtier pilote PVD noir 36/39 mm — saphir | `boitier-pilote-pvd-noir-36-39` | 20,39 € | 79,90 € | 4.8/5 · 107 avis | +900 | oui | — |

## Mouvements — 6 produits retenus

**Mot-clé / volume** : `mouvement nh35` 590/mois ; `nh35` 480/mois ; `seiko nh35` 590/mois (§7 pilier contenu)

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005005597724853](https://fr.aliexpress.com/item/1005005597724853.html) | Mouvement NH35 japonais — 24 rubis (fiche phase 4 confirmée) | `mouvement-nh35-japon` | 66,69 € | 119,90 € | 4.9/5 · 4636 avis | +10000 | — | — |
| 2 | [1005008494235697](https://fr.aliexpress.com/item/1005008494235697.html) | Mouvement NH35 Japon — roue de date blanche | `mouvement-nh35-date-blanche` | 65,69 € | 119,90 € | 4.9/5 · 740 avis | +5000 | oui | — |
| 3 | [1005007995556187](https://fr.aliexpress.com/item/1005007995556187.html) | Mouvement NH35A/NH36A — couronne 3.8, jour/date | `mouvement-nh36-jour-date` | 77,99 € | 139,90 € | 4.9/5 · 89 avis | +600 | — | — |
| 4 | [1005001430226835](https://fr.aliexpress.com/item/1005001430226835.html) | Mouvements famille NH — NH34/NH36/NH38/NH70/NH72 | `mouvement-famille-nh-34-72` | 96,69 € | 169,90 € | 4.8/5 · 53 avis | +500 | — | — |
| 5 | [1005009853779041](https://fr.aliexpress.com/item/1005009853779041.html) | Mouvement NH35 — roue de date rouge | `mouvement-nh35-date-rouge` | 67,69 € | 119,90 € | 4.8/5 · 67 avis | 482 | oui | — |
| 6 | [1005012175538270](https://fr.aliexpress.com/item/1005012175538270.html) | Mouvements Miyota 8215/8205 + NH34 GMT | `mouvement-miyota-8215-nh34-gmt` | 42,99 € | 89,90 € | 4.9/5 · 14 avis | 171 | — | — |

## Verres saphir — 6 produits retenus

**Mot-clé / volume** : NON MESURÉ en propre (`montre automatique fond verre` non mesuré) — longue traîne technique

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005007226573789](https://fr.aliexpress.com/item/1005007226573789.html) | Verre saphir double dôme — 26 à 38 mm | `verre-saphir-double-dome-26-38` | 7,89 € | 24,90 € | 4.8/5 · 38 avis | 488 | oui | — |
| 2 | [1005010361616521](https://fr.aliexpress.com/item/1005010361616521.html) | Verre saphir double dôme AR bleu — 28 à 38,5 mm | `verre-saphir-dome-ar-bleu` | 4,09 € | 19,90 € | 4.6/5 · 51 avis | 335 | — | — |
| 3 | [1005008965173152](https://fr.aliexpress.com/item/1005008965173152.html) | Verre saphir plat — 28 à 38 mm | `verre-saphir-plat-28-38` | 4,89 € | 19,90 € | 4.6/5 · 39 avis | 232 | — | — |
| 4 | [1005007976167717](https://fr.aliexpress.com/item/1005007976167717.html) | Verre saphir dôme simple — bord 1,2 mm | `verre-saphir-dome-1-2` | 7,99 € | 24,90 € | 4.9/5 · 36 avis | 205 | — | — |
| 5 | [1005004587063688](https://fr.aliexpress.com/item/1005004587063688.html) | Verre saphir plat avec loupe 30,5 mm | `verre-saphir-loupe-30-5` | 5,59 € | 19,90 € | 4.8/5 · 19 avis | 126 | oui | — |
| 6 | [1005004810355096](https://fr.aliexpress.com/item/1005004810355096.html) | Verre saphir dôme simple — bord 1,5 mm | `verre-saphir-dome-1-5` | 16,69 € | 34,90 € | 4.8/5 · 24 avis | 107 | oui | — |

## Outils du moddeur (complément Outillage) — 6 produits retenus

**Mot-clé / volume** : NON MESURÉ (`outil barrette montre` non mesuré) — complète les 7 outils déjà en boutique

| # | item_id | Titre maison proposé | Handle SEO | Coût (SERP) | Prix vente | Note/avis API ✓ | Ventes (SERP, B) | FR | Réserves |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [1005008518115553](https://fr.aliexpress.com/item/1005008518115553.html) | Porte-mouvement NH34/NH35/NH36 | `porte-mouvement-nh35` | 4,69 € | 19,90 € | 4.9/5 · 2283 avis | +10000 | — | — |
| 2 | [1005008695397789](https://fr.aliexpress.com/item/1005008695397789.html) | Porte-mouvement multi-calibres + support | `porte-mouvement-multi-calibres` | 5,99 € | 19,90 € | 4.9/5 · 439 avis | +2000 | oui | — |
| 3 | [1005008727414152](https://fr.aliexpress.com/item/1005008727414152.html) | Support mouvement acrylique d'horloger | `support-mouvement-acrylique` | 7,29 € | 24,90 € | 4.9/5 · 85 avis | 440 | — | — |
| 4 | [1005010551172634](https://fr.aliexpress.com/item/1005010551172634.html) | Support mouvement aluminium double face | `support-mouvement-aluminium` | 4,29 € | 19,90 € | 4.9/5 · 61 avis | 407 | — | — |
| 5 | [1005008635496479](https://fr.aliexpress.com/item/1005008635496479.html) | Base de pressage d'aiguilles | `presse-aiguilles-base` | 17,19 € | 39,90 € | 4.8/5 · 19 avis | 130 | — | — |
| 6 | [1005008717442651](https://fr.aliexpress.com/item/1005008717442651.html) | Enrouleur de ressort de barillet NH35 | `enrouleur-ressort-nh35` | 8,49 € | 29,90 € | 4.7/5 · 27 avis | 107 | oui | — |

## Écartés en QA photo (ne pas re-sourcer sans nouvelle preuve)

- `1005007922653909` — Cadran oriental rosé 28,5 mm — sans logo : cadran imprime SUPERLATIVE CHRONOMETER OFFICIALLY CERTIFIED (texte Rolex) — vu photo HD
- `1005010654686163` — Cadran oriental Sunburst en relief 28,5 mm — sans logo : cadran imprime SUPERLATIVE CHRONOMETER OFFICIALLY CERTIFIED + JAPAN MOV'T — vu photo HD

## Comptes et suite de chaîne

- Cadrans arabes orientaux (pièces) : **4**
- Montres cadran arabe (finies) : **5**
- Cadrans pilote chiffres 1-12 : **14**
- Cadrans stériles couleur & texture : **15**
- Cadrans squelette (NH70/NH72) : **10**
- Aiguilles (NH35/NH36/NH34) : **10**
- Lunettes & inserts (SKX 38 mm) : **10**
- Boîtiers NH35/NH36 : **10**
- Mouvements : **6**
- Verres saphir : **6**
- Outils du moddeur (complément Outillage) : **6**
- **Total retenus : 96** (+1 conditionnel, 2 écartés) — objectif 60-110 atteint ; 92 fiches actuelles + 96 = ~188 fiches à terme.

1. **Étape DSers (Chrome Hakim)** : suivre `FILE-DSERS-2026-08-09.md` dans l'ordre (best-sellers d'abord), monter chaque ligne en classe A à l'ouverture de la fiche, importer en DRAFT/0 canal, mapper uniquement les variantes stériles/sans logo.
2. **Rédaction** : mot-clé de collection dans le titre, ≥ 250 mots, hedges « annoncé », jamais le titre fournisseur.
3. **Images** : partir des faces `sources-fournisseur-2026-08/` + galeries récupérées à l'import ; purge fournisseur après branchement (procédure du 29/07).

*Registre généré dans la nuit du 08 au 09/08/2026 — navigateur intégré (SERP SSR + API avis publique + photos HD), zéro contournement du mur anti-bot, aucune fiche créée sur Shopify, aucun achat.*
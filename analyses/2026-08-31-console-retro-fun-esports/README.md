# Mesure express — console rétro portable & atelier/modding rétro

**Date** : 31/08/2026 · **Base** : DataForSEO (`scripts/kw_dfs.py`), France/français
**Origine** : boutique preuve [fun-esports.com](https://fun-esports.com) apportée par Hakim
**Seuils appliqués** (`PRODUCT-RESEARCH-CRITERIA.md` §1, base DataForSEO) : PRODUIT PUR **12 500**/mois
**Témoin** : `tufting` = 12 100 avant **et** après chaque passe — conforme

---

## Résultat en une phrase

**Le cluster console rétro passe le seuil (14 800 sur le seul bucket cœur, ≈ 19–20 k nettoyé, pic
décembre 27 100), mais la demande est à 66 % navigationnelle de marque (28 700/mois pour les dix
marques contre 14 800 de générique) ; la thèse atelier/modding meurt en mesure express à 1 910/mois,
6,5× sous le seuil.**

---

## 1. Correction d'une mesure antérieure — bucket fusionné

La mesure SEMrush du 01/08/2026 (`qualification-express-brandsearch-2026-08-01.md`, ligne 6) donnait
*« console retrogaming 8 100 + portable 2 300 → 13-15 k »*. **Elle additionnait deux formulations que
Google sert dans un seul bucket.**

Preuve par empreinte de série mensuelle — deux graines indépendantes rendent le même vecteur 12 mois
au chiffre près :

| Graine | Expression rendue | Volume | Série 12 mois |
|---|---|---:|---|
| `console rétro` | `games console rétro` | 14 800 | `8100, 6600, 8100, 8100, 9900, 12100, 14800, 27100, 22200, 14800, 14800, 14800` |
| `retrogaming` | `consoles retrogaming` | 14 800 | **identique** |

Variantes absorbées dans ce bucket unique : `console rétro`, `rétro game console`, `console rétro game`,
`console retrogaming`, `retrogaming console`, `retrogaming consoles`, `la console retrogaming`,
`console de retrogaming`.

**Chiffre corrigé : le cœur est un bucket unique à 14 800/mois**, pas une somme.
Même piège que `variantes-sans-accent-kmt` (corrigé le 29/08) : SEMrush sépare, Google fusionne.

## 2. Cluster console rétro — nettoyé

| Bucket (série distincte = bucket distinct) | Volume |
|---|---:|
| `console rétro / console retrogaming / retro game console` (fusionné) | **14 800** |
| `console portable retrogaming` | 1 600 |
| `console retrogaming portable` | 1 300 |
| `meilleures consoles retrogaming` | 1 300 |
| `console jeux rétro` | 1 000 |
| `console portable rétro` | 140 |
| **Cluster commercial nettoyé** | **≈ 19 000 – 20 000** |

`retrogaming` seul (5 400) est **écarté du cluster** : intent mixte (hobby, média, communauté), non
attribuable à un achat de console.

**Contamination retirée : 5 550/mois**

| Retiré | Volume | Motif |
|---|---:|---|
| `retrogaming online` | 2 400 | jouer en ligne, pas acheter |
| `magasin/boutique retrogaming` + Paris/Lyon/`arcadia` | 1 530 | enseignes physiques d'occasion |
| `console retrogaming 45000 jeux` + `100000 jeux` | **710** | **ROMs préchargées = segment illégal** |
| `émulateur console rétro`, `retrogaming émulateur` | 380 | logiciel |
| `raspberry pi retrogaming` | 210 | DIY, aucune console achetée |

**Verdict volume : PASS.** Le bucket cœur seul (14 800) dépasse déjà le seuil 12 500.

## 3. Saisonnalité — profil cadeau de Noël franc

`console retrogaming`, relevé mois par mois (libellés lus en direct, `google_ads/search_volume`) :

| 2025-08 | 09 | 10 | 11 | **12** | 2026-01 | 02 | 03 | 04 | 05 | 06 | 07 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 14 800 | 14 800 | 14 800 | 22 200 | **27 100** | 14 800 | 12 100 | 9 900 | 8 100 | 8 100 | 6 600 | 8 100 |

**×4,1 entre le creux de juin et le pic de décembre.** Le palier haut démarre en novembre ; août est
déjà à 14 800. Cohérent avec le cap Q4 2026.

## 4. Le signal décisif — la demande est navigationnelle de marque

| Marque | Volume/mois | déc. 2025 |
|---|---:|---:|
| anbernic | **12 100** | 14 800 |
| retroid pocket | 3 600 | 6 600 |
| analogue pocket | 3 600 | 4 400 |
| retroid | 2 900 | 3 600 |
| ayaneo | 2 900 | 3 600 |
| miyoo | 880 | 1 300 |
| miyoo mini | 880 | 1 000 |
| ayn odin | 880 | 880 |
| trimui | 590 | 720 |
| powkiddy | 390 | 590 |
| **Total marques** | **≈ 28 700** | ≈ 37 500 |

**La masse de marque vaut ×1,9 le générique** (28 700 contre 14 800). `anbernic` seul (12 100) pèse
presque autant que tout le générique. Ces requêtes vont au site de la marque et à AliExpress — elles ne
sont pas adressables par un revendeur sans stock ni différenciation.

À rapprocher de `plafond-niches-kraken-evidentes` : la demande visible est déjà occupée par l'amont.

## 5. Thèse atelier / modding rétro — STOP mesure express

**Piège d'outillage rencontré, à retenir** : la graine `game boy` (deux mots) rend 1 795 idées dont
**une seule** avec volume (27 100), et `google_ads/search_volume` renvoie **NULL** — pas 0 — sur
`game boy advance`, `game boy color`, `coque game boy advance`. La graine `gameboy` (un mot) rend
634 idées **toutes** valorisées. *Le zéro était un artefact d'orthographe de graine, pas une mesure.*
Vérifié avant conclusion.

Vocabulaire atelier réellement mesuré (graine `gameboy`, hors contamination LEGO/iPhone) :

| Expression | Volume |
|---|---:|
| `batterie gameboy advance sp` | 320 |
| `gameboy advance modding` | 210 |
| `écran gameboy` | 110 |
| `modding gameboy` | 110 |
| `coque gameboy advance sp` | 110 |
| `écran gameboy fat` / `gameboy advance sp modding` / `gameboy advance ips` / `batterie gameboy advance` | 90 chacun |
| ... 25 expressions au total | |
| **Cluster atelier** | **1 910** |

**1 910 contre un seuil de 12 500 : 6,5× sous le seuil. STOP mesure express.**

Contamination majeure de l'ombrelle `game boy` : `gameboy lego` = **27 100** (set LEGO sorti en 2025) —
c'est l'essentiel du bucket ombrelle à 27 100, pas de la demande de matériel rétro. S'y ajoutent
`gameboy advance roms` 5 400, `emulator gameboy advance` 1 900, `gameboy advance pokemon rom` 1 900 :
**la demande Game Boy en France est nostalgique, LEGO et ROM — pas pièces détachées.**

Le vocabulaire d'achat présent autour de la Game Boy parle de **cote et d'occasion**
(`game boy advance sp occasion`, `estimation game boy advance sp`, `game boy color le bon coin`,
`game boy color micromania`), pas de réparation.

## 6. Autres rayons de la boutique preuve

| Rayon (SKU chez fun-esports) | Tête | Volume | Lecture |
|---|---|---:|---|
| Tapis de souris (98) | `tapis de souris xxl` | 5 400 | sous seuil PUR ; déjà couvert par le STOP `clavier mécanique custom` (registre 07/08) |
| Keycaps (74) | `keycaps` | 2 900 | idem |
| Manettes (43) | `manette rétro` 110 · `manette arcade` 210 · `stick arcade` 1 300 | < 1 700 | mort |

## 7. Ce que « console portable » désigne réellement en France

`console portable` = 12 100, mais le vocabulaire est accaparé par le PC portable de jeu :
`console portable xbox` 9 900, `console playstation portable` 1 300, `console portable ps5` 880,
`console portable asus rog ally` 590+480, `console portable steam` 390. Hors périmètre :
`steam deck` **74 000**, `nintendo switch 2` **201 000**, `rog ally` 9 900.
Le rétro n'est qu'une poche de ce terme (`console rétrogaming portable` 1 600).

---

## Limites d'outillage

1. `keywords_data/google_ads/search_volume` renvoie **NULL** (indiscernable de 0 sans contrôle) sur
   plusieurs têtes évidentes. **Toujours recouper une tête nulle par une graine alternative** avant de
   conclure à l'absence de demande.
2. L'orthographe de la graine change le résultat du tout au tout (`game boy` vs `gameboy`).
   Balayer les deux graphies sur toute famille à nom composé.
3. Aucune SERP nettoyée, aucune sonde prix, aucune concurrence instruite : ce rapport est **niveau 0**.

## Fichiers du dossier

| Fichier | Contenu |
|---|---|
| `01-mesure-consoles.json` | graines `console rétro`, `retrogaming`, `anbernic` — groupes dédupliqués + séries 12 mois |
| `01-mesure-atelier.json` | graines `game boy`, `console portable` |
| `01-mesure-gameboy.json` | graines `game boy advance`, `gameboy` — celle qui a levé l'artefact de graphie |
| `02-catalogue-fun-esports.csv` | 569 SKU de la boutique preuve : titre, vendor, type, prix, dispo |

## Coût

≈ 0,69 USD DataForSEO (5 graines `keyword_suggestions` + 2 appels `search_volume`).

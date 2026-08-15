# U5 — gothique : arbitrage SERP des 18 980 recherches ambiguës

**Agent :** arbitrage SERP U5 (Claude). **Source du bloc à trancher :** `02-volume-consolide.md` §7.
**Méthode :** Google France, lecture texte du DOM, `https://www.google.fr/search?q=<requête>&hl=fr&gl=fr&num=20&pws=0`.
**Date :** 15/08/2026, à partir de 22h00. Onglet Chrome dédié, aucune capture, aucun clic.

> Ce document ne rend **aucun verdict marché**, aucun sourcing, aucune architecture. Il rend un
> **arbitrage d'intention** adossé à des pages 1 réelles. Le total corrigé est un **constat
> arithmétique**, pas une décision.

---

## État d'avancement — TERMINÉ (10 lectures SERP / 10)

| # | Requête SERP | Volume en jeu | Heure | Statut |
|---|---|---|---|---|
| 1 | `gothique` | 12 100 | 22h00 | ✅ lu |
| 2 | `croix gothique` | 1 300 | 22h03 | ✅ lu |
| 3 | `femme gothique` | 880 | 22h06 | ✅ lu |
| 4 | `gothiqua` | 880 | 22h09 | ✅ lu |
| 5 | `style gothique femme` | 720 | 22h12 | ✅ lu |
| 6 | `gothique homme` | 590 | 22h15 | ✅ lu |
| 7 | `femmes gothiques` | 590 | 22h18 | ✅ lu |
| 8 | `homme gothique` | 480 | 22h21 | ✅ lu |
| 9 | `gothique femme` | 480 | 22h24 | ✅ lu |
| 10 | `gothique sexy` | 480 | 22h27 | ✅ lu |

**10 requêtes SERP**, dans la borne du budget (8-12). **Couverture : 18 500 des 18 980 lus
directement (97,5 %).** Seul `femme gothiques` 480 est reporté par analogie sur `femmes gothiques`
— déclaré au §6.

---

## 1. Méthode, et règle de retrait appliquée

- URL : `https://www.google.fr/search?q=<requête>&hl=fr&gl=fr&num=20&pws=0`, ≥ 4 s d'attente après
  navigation, lecture de `document.body.innerText` + extraction DOM des `cite` et des `h3`.
- **`num=20` n'est plus honoré par Google en août 2026** : chaque page 1 rend **8 à 9 résultats
  organiques**. Les décomptes ci-dessous sont donc **sur 8 ou 9**, pas sur 10 ni sur 20.
- **Règle de retrait, écrite avant les lectures et appliquée à l'identique :** le taux retenu est la
  **part des positions organiques de page 1 qui vendent réellement un produit du périmètre** (fiche
  produit ou page de collection), ajustée à la baisse quand les **recherches associées** sont
  massivement informationnelles.
- **Ces pourcentages sont des estimations faites à la composition de la page 1, pas de nouvelles
  mesures.** Aucun volume n'a été remesuré ici.
- **Annonces :** aucune occurrence de la mention « Sponsorisé » n'a été trouvée dans le DOM des
  pages lues. **Je ne peux pas garantir l'isolement des annonces Search texte** dans ce mode de
  lecture ; je constate seulement l'absence de marqueur, et **aucun carrousel Shopping** sur les
  pages lues. À ne pas lire comme « aucun annonceur ».
- **Page 1 seulement.** Rien de ce qui suit ne juge la profondeur de la concurrence.

### Journal des lectures

| # | Requête | Heure | Résultats organiques rendus | Ligne « Résultats, y compris pour… » | Shopping | « Sponsorisé » |
|---|---|---|---|---|---|---|
| 1 | `gothique` | 15/08 22h00 | 8 | **absente** | non | 0 |
| 2 | `croix gothique` | 15/08 22h03 | 9 | **absente** | non | 0 |
| 3 | `femme gothique` | 15/08 22h06 | 8 | **absente** | non | 0 |
| 4 | `gothiqua` | 15/08 22h09 | 9 | **absente** — mais « Essayez avec cette orthographe : gothique » (suggestion, pas rabattement) | non | 0 |
| 5 | `style gothique femme` | 15/08 22h12 | 9 | **absente** | non | 0 |
| 6 | `gothique homme` | 15/08 22h15 | 9 | **absente** | non | 0 |
| 7 | `femmes gothiques` | 15/08 22h18 | 8 | **absente** | non | 0 |
| 8 | `homme gothique` | 15/08 22h21 | 9 | **absente** | non | 0 |
| 9 | `gothique femme` | 15/08 22h24 | 9 | **absente** | non | 0 |
| 10 | `gothique sexy` | 15/08 22h27 | 9 | **absente** | non | 0 |

**Aucune des 10 pages 1 n'affiche la ligne « Résultats, y compris pour… »** : dans ce bloc, il n'y a
**aucun rabattement orthographique**. Chaque formulation existe en propre pour Google. Le risque du
piège n° 2 est donc écarté pour les 11 lignes ambiguës — y compris `gothiqua`, dont le cas est
détaillé au §2.4 et qui n'est **pas** une faute rabattue.

---

## 2. Arbitrage formulation par formulation

### 2.1 `gothique` (nu) — 12 100 — 15/08 22h00

| Colonne | Relevé |
|---|---|
| **Ce que Google sert** | Un **Aperçu IA** en tête qui définit le mot sur quatre registres : peuple germanique, architecture médiévale (Amiens, Saint-Denis), roman gothique, contre-culture musicale (cold wave, goth rock). Puis un bloc « Autres questions » **4/4 définitionnel** (« Qu'est-ce qui veut dire gothique ? », « C'est quoi le style gothique ? »…). Aucun carrousel Shopping, aucun prix visible. |
| **Intention** | **Pas du tout notre produit.** La requête désigne un mot de dictionnaire à quatre sens, dont aucun n'est un rayon de boutique. |
| **Commercial ou informationnel** | **6 positions éditoriales sur 8.** Wikipédia ×2 (Mouvement gothique, Architecture gothique), CIELAM (université Aix-Marseille, littérature), Centre des monuments nationaux (« Gothique, roman : quelles différences ? »), essentiels.bnf.fr, Larousse (définition). La page **explique**, elle ne vend pas. |
| **Qui tient la page 1** | Marketplace **0** · fast fashion (Shein/Temu) **0** · marque gothique **1** (`emp-online.fr` — **EMP est bien présent**) · spécialiste indépendant FR **1** (`steampunk-boutique.com`) · drop probable **0** · encyclopédies / institutions / université **6**. `antregothique.com`, `castle-gothic.fr`, `vetement-gothique.fr` : **absents**. |
| **Recherches associées** | Style gothique · **Gothique Femme** · Gothique Définition · Gothique architecture · Gothique en anglais · Gothique religion · Gothique en arabe · Gothique littérature → **7 sur 8 informationnelles** (définition, architecture, religion, littérature, traduction). Une seule adjacente au produit (`Gothique Femme`), elle-même arbitrée ci-dessous. |
| **Volume** | **Retiré à 85 %** : 12 100 → **retenu 1 815**, **retiré 10 285**. *Motif :* 6/8 positions éditoriales, Aperçu IA entièrement culturel, PAA 4/4 définitionnel, associées 7/8 informationnelles. Les 2 positions marchandes (EMP, steampunk-boutique) sont la seule raison de ne pas retirer 100 %. *Estimation à la composition de la page 1, pas une mesure.* |

**Note de rabattement (piège n° 2) :** **aucune ligne « Résultats, y compris pour… »**. La racine
`gothique` existe donc en propre — mais elle existe en propre **comme mot de culture**.

### 2.2 `croix gothique` — 1 300 — 15/08 22h03

| Colonne | Relevé |
|---|---|
| **Ce que Google sert** | **Ni architecture, ni église.** Google sert le **symbole** : signification, symbolisme, origine, port en bijou. Deux fiches produit réelles seulement (une médaille religieuse, un pendentif diamants de joaillier). Aucun Shopping, aucun prix en snippet. |
| **Intention** | **Partiellement.** L'hypothèse « croix d'église / architecture » du rapport de mesure est **infirmée** : personne ne cherche une croix de cathédrale. Mais la requête est d'abord une question de sens, pas un panier. |
| **Commercial ou informationnel** | **6 positions éditoriales sur 9.** Titres lus : « Croix Gothique : Signification et Symbolisme en 2026 » (gotique.fr, blog de marchand), « Pourquoi les croix sont-elles si présentes dans la mode… » (esprit-gothique.fr, blog de marchand), « Une croix gothique, c'est satanique ou chrétien » (**forum, 7 commentaires, il y a 2 ans**), « 38 meilleures idées sur Croix Gothiques » (Pinterest), « Origines et histoire de la croix gothique » (bijoux-homme-tendance.com, blog), « 34 100+ Croix Gothique Photos… libres de droits » (iStock). |
| **Qui tient la page 1** | Marketplace **1** (`amazon.fr`, page de résultats « Amazon.fr : Croix Gothique ») · fast fashion **0** · marque gothique **0** · spécialiste indépendant FR **3** (`gotique.fr`, `esprit-gothique.fr`, `bijoux-homme-tendance.com`) — **mais les trois se classent avec un article de blog, pas avec une collection** · joaillerie / bijouterie classique **2** (`medaillesbecker.com` produit, `edouardnahum.fr` « PENDENTIF CROIX GOTHIQUE DIAMANTS ») · banques d'images et forum **3** · `antregothique.com`, `castle-gothic.fr`, `vetement-gothique.fr`, EMP : **absents**. |
| **Recherches associées** | Croix gothique **signification** · **Tatouage** · **dessin** · **origine** · et croix chrétienne · **argent** → **5 sur 6 informationnelles**, une seule matière/achat (`argent`). Le tatouage et le dessin sont deux contaminations franches. |
| **Volume** | **Retiré à 70 %** : 1 300 → **retenu 390**, **retiré 910**. *Motif :* page 1 à 6/9 éditoriale, associées 5/6 informationnelles (tatouage, dessin, signification), CPC 0,00 relevé en KMT cohérent. Les 3 positions produit (Amazon + 2 bijoutiers) justifient de ne pas retirer intégralement. *Estimation à la composition de la page 1.* |

**Correction apportée au rapport de mesure :** `02-volume-consolide.md` supposait « architecture
(croix d'église) ». **C'est faux** — la SERP ne contient aucune architecture. La ligne relève bien du
**pendentif**, mais avec une intention majoritairement informationnelle.

### 2.3 `femme gothique` — 880 — 15/08 22h06

| Colonne | Relevé |
|---|---|
| **Ce que Google sert** | Un mélange **banque d'images / inspiration / collections vêtement**. Trois positions sur huit sont des banques d'images (Pinterest, Getty Images, Pixabay). **Aucun contenu adulte en page 1** — l'hypothèse « grappe d'imagerie adulte » du rapport de mesure n'est pas confirmée par la SERP. Aucun Shopping. |
| **Intention** | **Partiellement.** Trois résultats sur huit servent exactement notre produit (« Vêtements gothiques femme — corsets, robes, vestes », « robes, corsets et tops »). Les cinq autres servent des images et des définitions de style. |
| **Commercial ou informationnel** | **5 positions éditoriales ou banques d'images sur 8.** Pinterest « 710 idées de Femme gothiques », `steampunk-boutique.com` « Le Style Gothique pour les Femmes : Guide Complet » (blog de marchand), Getty « 9 455 Femme Gothique Photos », Wikipédia « Mode gothique », Pixabay « 3 269 Images gratuites ». |
| **Qui tient la page 1** | Marketplace **0** · fast fashion (Shein/Temu) **0** · marque gothique **0** · **spécialiste indépendant FR 3 en collection** (`discobole.fr`, `esprit-gothique.fr`, `toonzshop.com`) **+ 1 en blog** (`steampunk-boutique.com`) · drop probable : `toonzshop.com` et `discobole.fr` sont des candidats à vérifier (hors mandat ici) · banques d'images **3** · encyclopédie **1**. `antregothique.com`, `castle-gothic.fr`, `vetement-gothique.fr`, EMP : **absents**. |
| **Recherches associées** | Femme gothique romantique · **définition** · **belle** · style gothique femme simple · **célèbre** · **rencontre** → **0 sur 6 commerciale**. `rencontre` est une contamination site de rencontres ; `belle` et `célèbre` sont de l'imagerie. |
| **Volume** | **Retiré à 70 %** : 880 → **retenu 264**, **retiré 616**. *Motif :* 3/8 positions vendent (37,5 %), ajusté à la baisse par des associées **0/6 commerciales** et trois banques d'images en page 1. *Estimation à la composition de la page 1.* |

---

### 2.4 `gothiqua` — 880 — 15/08 22h09

| Colonne | Relevé |
|---|---|
| **Ce que Google sert** | **Un cheval de course et une police de caractères.** Trois positions sont consacrées à **GOTHIQUA DE BUSSET**, jument trotteuse née en 2016 (letrot.com « Sexe F, Année de nais. 2016, Robe BAI, Gains Totaux 146 830 € », geny.com, canalturf.com). Trois autres sont la police **Gothiqua Font** (dafont.com, online-fonts.com, ffonts.net). Une est un patron de tricot américain (« Pattern and Yarn Kit — The Gothiqua Shawl », madrigalyarns.com). Une est un profil Pinterest (« Gothiqua / Metalleuse_sh »). Aucun Shopping. |
| **Intention** | **Pas du tout notre produit** dans 8 cas sur 9. |
| **Commercial ou informationnel** | Ni l'un ni l'autre pour l'essentiel : **hors sujet**. 6 positions sur 9 sont du turf ou de la typographie. |
| **Qui tient la page 1** | Marketplace **0** · fast fashion **0** · marque gothique **0** · **spécialiste indépendant FR 1** (`gothyka.com` — « Boutique Gothique en ligne spécialisée dans l'Univers Gothique Romantique ») · turf **3** · fonderies de polices **3** · autres **2**. `antregothique.com`, `castle-gothic.fr`, `vetement-gothique.fr`, EMP : absents. |
| **Recherches associées** | **Le seul signal contraire, et il est fort :** Style gothique vêtements · Bijoux gothique Femme · T-shirt gothique femme · Boutique gothiques · Boutique bijoux gothique Paris · Boutique emo · **Divine Darkness vetement** · Costume gothique femme → **8 sur 8 commerciales**. Google modélise donc l'utilisateur de `gothiqua` comme un acheteur de gothique, alors que sa page 1 organique ne le sert pas. |
| **Volume** | **Retiré à 85 %** : 880 → **retenu 132**, **retiré 748**. *Motif :* 1 seule position marchande du périmètre sur 9, contre 6 positions hors sujet (cheval de course + police). Le taux n'est pas ramené à 11 % strict (1/9) parce que les recherches associées sont 8/8 commerciales. *Estimation à la composition de la page 1.* |

**Contrôle de rabattement orthographique (piège n° 2) — résultat inattendu.** Google **ne rabat pas**
`gothiqua` sur `gothique` : il sert la page littérale et propose seulement « **Essayez avec cette
orthographe : gothique** ». Ce n'est donc **pas une faute rabattue déjà incluse ailleurs**, c'est un
**homonyme contaminé** : nom d'une jument de course française + nom d'une police de caractères. La
ligne ne fait pas double emploi avec `gothique`, mais elle ne vaut presque rien.

### 2.5 `style gothique femme` — 720 — 15/08 22h12

| Colonne | Relevé |
|---|---|
| **Ce que Google sert** | Une page mixte, à peu près équilibrée : quatre collections de vêtements gothiques femme, cinq contenus de style et d'inspiration. Aucun Shopping visible. |
| **Intention** | **Partiellement, et davantage que `femme gothique`.** Quatre résultats sur neuf servent une collection Vêtements femme. C'est cohérent avec le CPC de 0,29 $ relevé en KMT — **le seul CPC non nul de tout le bloc ambigu**. |
| **Commercial ou informationnel** | **5 positions éditoriales ou d'inspiration sur 9** : « Le Style Gothique pour les Femmes : Guide Complet » (steampunk-boutique.com), Wikipédia « Mode gothique », « Le style gothique pour femmes, comment l'adopter » (clicandfit.com), Pinterest ×2. |
| **Qui tient la page 1** | Marketplace **0** · fast fashion **0** · **marque gothique 1** (`emp-online.fr`, « Boutique Gothique pour femmes † ») · **spécialiste indépendant FR 3 en collection** (`toonzshop.com`, `discobole.fr`, `miss-gothique.com`) **+ 1 en blog** (`steampunk-boutique.com`) · inspiration / encyclopédie **4**. `antregothique.com`, `castle-gothic.fr`, `vetement-gothique.fr` : **absents**. |
| **Recherches associées** | Style gothique femme **simple** · **maquillage** · **chic** · **définition** · **vêtements** · Tenue gothique chic → **4 sur 6 informationnelles**, 2 orientées produit. |
| **Volume** | **Retiré à 55 %** : 720 → **retenu 324**, **retiré 396**. *Motif :* 4/9 positions vendent une collection du périmètre (44 %), légèrement relevé par le CPC non nul et par 2 associées produit. *Estimation à la composition de la page 1.* |

### 2.6 `gothique homme` — 590 — 15/08 22h15

| Colonne | Relevé |
|---|---|
| **Ce que Google sert** | **Une page de rayon, presque intégralement marchande.** Manteaux, vestes, chemises, costumes de mariage, bijoux. Titres lus : « Vêtements gothiques homme — Manteaux, vestes… », « Boutique Gothique pour hommes † », « Vêtement gothique, steampunk, aristocrate, romantique… », « Vêtements gothiques homme : manteaux, chemises et… », « Costumes gothique de mariage homme 2026 — Collection… », « Vêtements gothiques pour hommes et femmes de **Devil Fashion** », « Bijoux style gothique pour homme ». Aucun Shopping visible. |
| **Intention** | **Oui, pleinement.** C'est la formulation la plus commerciale de tout le bloc ambigu. |
| **Commercial ou informationnel** | **2 positions éditoriales sur 9 seulement** : le guide de `steampunk-boutique.com` et un tableau Pinterest. **7 sur 9 vendent.** |
| **Qui tient la page 1** | Marketplace **0** · fast fashion (Shein/Temu) **0** · **marque gothique 2** (`emp-online.fr` ; `metalmonde.fr` qui distribue **Devil Fashion**) · **spécialiste indépendant FR 4** (`discobole.fr`, `pentagrammeshop.com`, `toonzshop.com`, `mylittlefantaisie.com`) · costumier de cérémonie **1** (`ottavionuccio.com`, costumes de mariage) · inspiration **1** · blog de marchand **1**. **Aucune marketplace, aucun Amazon, aucun Shein.** `antregothique.com`, `castle-gothic.fr`, `vetement-gothique.fr` : **absents**. |
| **Recherches associées** | Style gothique homme **chic** · Vetement gothique homme **pas cher** · **Costume** gothique homme · maquillage gothique homme · **Boutique** gothique homme · **Chemise** gothique homme → **5 sur 6 commerciales**. |
| **Volume** | **Retenu à 80 %** : 590 → **retenu 472**, **retiré 118**. *Motif :* 7/9 positions marchandes (78 %), confirmées par des associées 5/6 commerciales. Le retrait de 20 % couvre la part « maquillage / look » de la grappe. *Estimation à la composition de la page 1.* |

**Ce que cette lecture corrige.** Le rapport de mesure écartait `gothique homme` sur son **CPC de
0,00 $**. La SERP dit l'inverse : c'est une requête de rayon, tenue par sept marchands. **Le CPC nul
mesurait l'absence d'annonceurs, pas l'absence d'intention d'achat** — exactement le revers du piège
n° 6 (un score agrégé ne dit ni qui tient la page, ni avec quelle intention).

### 2.7 `femmes gothiques` — 590 — 15/08 22h18

| Colonne | Relevé |
|---|---|
| **Ce que Google sert** | **Zéro produit.** Titres lus : « 710 idées de Femme gothiques », « Le Style Gothique pour les Femmes : Guide Complet », « Mode gothique » (Wikipédia), « 9 455 Femme Gothique Photos et images haute résolution » (Getty), « **Femmes emblématiques dans le gothique et ce graphique** » (**forum, plus de 150 commentaires, il y a 2 mois**), « 43 800+ Femme Gothique Photos et images libres de droits » (iStock), « 20 idées de Gothic femme » (Pinterest), « Style Gothique Femme : Tout ce que vous devez savoir » (steampunkstore.fr, article). |
| **Intention** | **Pas du tout notre produit.** Le pluriel déplace la requête vers « quelles femmes sont gothiques » — figures, images, discussions. |
| **Commercial ou informationnel** | **8 positions éditoriales, d'images ou de forum sur 8. Aucune page de collection, aucune fiche produit.** C'est la page 1 la plus informationnelle de tout le bloc, `gothique` nu compris. |
| **Qui tient la page 1** | Marketplace **0** · fast fashion **0** · marque gothique **0** · **spécialiste indépendant FR : 2, mais tous deux en article de blog** (`steampunk-boutique.com`, `steampunkstore.fr`) · banques d'images **3** (Getty ×1, iStock ×1, Pinterest ×2) · encyclopédie **1** · forum **1**. `antregothique.com`, `castle-gothic.fr`, `vetement-gothique.fr`, EMP : **absents**. |
| **Recherches associées** | **Aucun bloc de recherches associées rendu** sur cette page. |
| **Volume** | **Retiré à 100 %** : 590 → **retenu 0**, **retiré 590**. *Motif :* 0 position marchande sur 8. Aucune collection ne peut prendre cette page. *Estimation à la composition de la page 1.* |

**Report par analogie — `femme gothiques` 480.** Cette formulation (même pluriel dévié, même
grappe) **n'a pas été lue en SERP**. Je lui applique le même traitement que `femmes gothiques`
— **retirée à 100 %** — et je le déclare comme un **report, pas une lecture**, au §6.

### 2.8 `homme gothique` — 480 — 15/08 22h21

| Colonne | Relevé |
|---|---|
| **Ce que Google sert** | La même page de rayon que `gothique homme`, un cran moins dense : manteaux, vestes, chemises, costumes de mariage. Aucun Shopping visible. |
| **Intention** | **Oui.** Cinq résultats sur neuf servent une collection Homme du périmètre. |
| **Commercial ou informationnel** | **4 positions éditoriales ou d'images sur 9** : guide `steampunk-boutique.com`, Pinterest, Getty (« 847 Goth Men Photos »), Wikipédia « Mode gothique ». **5 sur 9 vendent.** |
| **Qui tient la page 1** | Marketplace **0** · fast fashion **0** · **marque gothique 1** (`emp-online.fr`) · **spécialiste indépendant FR 3** (`discobole.fr`, `toonzshop.com`, `pentagrammeshop.com`) · costumier de cérémonie **1** (`ottavionuccio.com`) · blog de marchand **1** · images / encyclopédie **3**. `antregothique.com`, `castle-gothic.fr`, `vetement-gothique.fr` : **absents**. |
| **Recherches associées** | Style gothique homme **chic** · **Costume** gothique Homme · Vetement gothique homme **pas cher** · **Accessoire** Gothique homme · maquillage gothique homme · **Costume mariage** gothique homme → **5 sur 6 commerciales**. |
| **Volume** | **Retenu à 60 %** : 480 → **retenu 288**, **retiré 192**. *Motif :* 5/9 positions marchandes (56 %), relevé par des associées 5/6 commerciales. *Estimation à la composition de la page 1.* |

### 2.9 `gothique femme` — 480 — 15/08 22h24

| Colonne | Relevé |
|---|---|
| **Ce que Google sert** | **L'inversion de l'ordre des mots change tout.** Là où `femme gothique` servait trois banques d'images, `gothique femme` sert cinq marchands : « Vêtements gothiques femme — Corsets, robes, vestes… », « Vêtements gothiques femme : robes, corsets et tops », « Boutique Gothique pour femmes † », « Style Gothique : Boutique Gothique | Vêtements Gothique », « **Mode Gothique Femme** » (Amazon). Aucun Shopping visible. |
| **Intention** | **Oui, majoritairement.** |
| **Commercial ou informationnel** | **4 positions éditoriales ou d'inspiration sur 9** : guide `steampunk-boutique.com`, Pinterest ×2, Wikipédia. **5 sur 9 vendent.** |
| **Qui tient la page 1** | **Marketplace 1** (`amazon.fr`, rayon « Mode Gothique Femme ») · fast fashion **0** · **marque gothique 1** (`emp-online.fr`) · **spécialiste indépendant FR 3** (`discobole.fr`, `toonzshop.com`, `esprit-gothique.fr`) · blog de marchand **1** · inspiration / encyclopédie **3**. `antregothique.com`, `castle-gothic.fr`, `vetement-gothique.fr` : **absents**. |
| **Recherches associées** | Style gothique femme · style gothique femme **simple** · **Vêtements** style gothique femme · Gothique femme **belle** · **Vêtement** gothique femme **rock** · **Vêtement** gothique Femme **pas cher** → **4 sur 6 orientées produit**. |
| **Volume** | **Retenu à 60 %** : 480 → **retenu 288**, **retiré 192**. *Motif :* 5/9 positions marchandes, associées 4/6 produit. *Estimation à la composition de la page 1.* |

**Constat de méthode à retenir.** `femme gothique` (30 % retenus) et `gothique femme` (60 % retenus)
sont **la même paire de mots dans l'autre sens**, et Google leur sert deux pages différentes : l'une
d'images, l'autre de rayon. Le rapport de mesure les traitait comme équivalentes. **L'ordre des mots
porte l'intention** — à ne pas généraliser d'une variante à l'autre sans lecture.

### 2.10 `gothique sexy` — 480 — 15/08 22h27

| Colonne | Relevé |
|---|---|
| **Ce que Google sert** | **Ni contenu adulte, ni imagerie : de la lingerie.** Titres lus : « **Lingerie gothique femme — Discobole** », « **Lingerie Gothique** » (Amazon), « **Body Moulant Sexy Gothique — Satan Shop** », « Vêtements gothiques pour femme de la marque… », « Miss Gothique | Vêtements Gothiques et Mode… », « Boutique Gothique pour femmes † », « Vetement Gothique ». Aucun Shopping visible. |
| **Intention** | **Oui.** L'adjacence adulte supposée par le rapport de mesure **n'apparaît pas en page 1**. La requête désigne un rayon réel : lingerie / body / tenues moulantes gothiques. |
| **Commercial ou informationnel** | **2 positions non marchandes sur 9 seulement** : Pinterest « 260 idées de Femmes Gothiques » et Shutterstock « 18 mille Images… Sexy goth girl ». **7 sur 9 vendent.** |
| **Qui tient la page 1** | **Marketplace 1** (`amazon.fr`, rayon « Lingerie Gothique ») · fast fashion **0** · **marque gothique 1** (`emp-online.fr`) · **spécialiste indépendant FR 5** (`pentagrammeshop.com`, `miss-gothique.com`, `discobole.fr`, `esprit-gothique.fr`, `satan-shop.com`) · images **2**. `antregothique.com`, `castle-gothic.fr`, `vetement-gothique.fr` : **absents**. |
| **Recherches associées** | **Aucun bloc rendu** sur cette page. |
| **Volume** | **Retenu à 75 %** : 480 → **retenu 360**, **retiré 120**. *Motif :* 7/9 positions marchandes, dont une fiche produit et deux rayons Lingerie. Le retrait de 25 % couvre la part imagerie (Pinterest, Shutterstock). *Estimation à la composition de la page 1.* |

**Correction apportée au rapport de mesure.** `02-volume-consolide.md` écartait `gothique sexy` pour
« adjacence adulte ». **La SERP l'infirme** : c'est une requête de lingerie gothique. Elle ouvre par
ailleurs une famille produit **non mesurée** dans le rapport de volume (voir §6).

---

## 3. Décompte final

**Sur les 18 980 recherches ambiguës : 4 333 sont retenues comme commerciales, 14 647 sont
retirées.** Soit **22,8 % du bloc retenu**.

| Formulation | Volume | Positions marchandes / total organique | Taux retenu | **Retenu** | **Retiré** | Motif de la décision |
|---|---|---|---|---|---|---|
| `gothique` | 12 100 | **2 / 8** | 15 % | **1 815** | 10 285 | Aperçu IA entièrement culturel, 6/8 positions encyclopédiques ou institutionnelles, PAA 4/4 définitionnel, associées 7/8 informationnelles. Mot de dictionnaire à quatre sens. |
| `croix gothique` | 1 300 | **3 / 9** | 30 % | **390** | 910 | Pendentif, pas architecture — mais page 1 à 6/9 éditoriale (signification, satanique ou chrétien, origine) et associées 5/6 informationnelles (tatouage, dessin). |
| `femme gothique` | 880 | **3 / 8** | 30 % | **264** | 616 | Trois banques d'images en page 1, associées **0/6 commerciales**, contamination `rencontre`. |
| `gothiqua` | 880 | **1 / 9** | 15 % | **132** | 748 | **Homonyme** : jument de course « Gothiqua de Busset » (3 positions) + police de caractères « Gothiqua Font » (3 positions). Pas un rabattement orthographique. |
| `style gothique femme` | 720 | **4 / 9** | 45 % | **324** | 396 | Page mixte ; seul CPC non nul du bloc (0,29 $) ; associées 4/6 informationnelles (maquillage, définition). |
| `femmes gothiques` | 590 | **0 / 8** | 0 % | **0** | 590 | Aucune position marchande. Images, forum, encyclopédie, articles de blog. |
| `gothique homme` | 590 | **7 / 9** | 80 % | **472** | 118 | Page de rayon. 7 marchands, associées 5/6 commerciales. **La plus commerciale du bloc.** |
| `femme gothiques` | 480 | *non lue* | 0 % | **0** | 480 | **Report par analogie** sur `femmes gothiques`, déclaré au §6. |
| `homme gothique` | 480 | **5 / 9** | 60 % | **288** | 192 | Même rayon Homme, un cran moins dense ; associées 5/6 commerciales. |
| `gothique femme` | 480 | **5 / 9** | 60 % | **288** | 192 | Rayon Femme ; l'ordre inversé sert une page marchande là où `femme gothique` sert des images. |
| `gothique sexy` | 480 | **7 / 9** | 75 % | **360** | 120 | **Lingerie gothique**, pas contenu adulte. 2 rayons Lingerie + 1 fiche produit. |
| **TOTAL** | **18 980** | — | **22,8 %** | **4 333** | **14 647** | |

**Rappel exigé par la méthode :** tous les taux ci-dessus sont des **estimations faites à la
composition de la page 1**, pas de nouvelles mesures de volume. Aucun chiffre de recherche n'a été
remesuré dans cette mission.

---

## 4. Total U5 corrigé — constat arithmétique

| Poste | Volume |
|---|---|
| Mesure consolidée du 15/08 (16 lectures KMT, `02-volume-consolide.md`) | **22 120** |
| **+ Retenu commercial du bloc ambigu, arbitré en SERP** | **+ 4 333** |
| **= TOTAL U5 CORRIGÉ** | **26 453** |

| Seuil (mode Kraken `catalogue-volume`) | Valeur | Écart | Constat |
|---|---|---|---|
| Plancher | **30 000** | **− 3 547** | **NON FRANCHI** |
| Confort | **40 000** | **− 13 547** | **NON FRANCHI** |

**Ce constat est arithmétique. Il ne vaut pas verdict — la décision revient à Hakim.**

### Test de sensibilité — le plancher est-il atteignable par un autre arbitrage ?

Le total dépend presque entièrement de `gothique` nu (12 100, soit **64 % du bloc**). Pour que U5
franchisse 30 000, il faudrait retenir **3 547 recherches de plus**, donc porter `gothique` nu de
1 815 à **5 362 — soit 44 % de la racine retenue**. Or sa page 1 compte **2 positions marchandes sur
8**, un Aperçu IA entièrement culturel et un bloc « Autres questions » 4/4 définitionnel. Un taux de
44 % n'est pas soutenable devant cette page.

**Même dans l'hypothèse la plus généreuse défendable** — retenir `gothique` nu au taux brut de sa
composition organique (2/8 = 25 %, soit 3 025) et laisser les dix autres lignes inchangées — le
total atteindrait **27 663**, encore **sous le plancher**. Le franchissement des 30 000 par ce bloc
**n'est atteignable par aucune lecture défendable de ces dix pages 1**.

---

## 5. Ce que la SERP apprend sur la concurrence — observation, pas recommandation

**Décompte des acteurs sur les 10 pages 1 lues** (nombre de pages où le domaine apparaît) :

| Acteur | Pages 1 / 10 | Nature de ce qu'il classe |
|---|---|---|
| Pinterest | **9** | inspiration, tableaux d'idées |
| `steampunk-boutique.com` | **7** | **presque toujours un guide éditorial**, pas une collection |
| `emp-online.fr` (**EMP**) | **6** | collections « Boutique Gothique pour femmes / hommes † » |
| `discobole.fr` | **6** | collections Vêtements homme / femme, **Lingerie gothique** |
| Wikipédia | **6** | « Mode gothique », « Architecture gothique », « Mouvement gothique » |
| `toonzshop.com` | **5** | collections Vêtements homme / femme |
| `esprit-gothique.fr` | **4** | collections + un article de blog |
| Getty / iStock / Pixabay / Shutterstock | **6 pages cumulées** | banques d'images |
| `amazon.fr` | **3** | rayons « Croix Gothique », « Mode Gothique Femme », « Lingerie Gothique » |
| `pentagrammeshop.com` | **3** | collections Vêtement gothique / steampunk / aristocrate |
| `ottavionuccio.com` | **2** | costumes de mariage gothiques |
| `miss-gothique.com` | **2** | collections Mode alternative |
| `metalmonde.fr`, `mylittlefantaisie.com`, `satan-shop.com`, `gothyka.com`, `steampunkstore.fr`, `gotique.fr`, `bijoux-homme-tendance.com` | **1 chacun** | collections ou articles |
| **Shein / Temu / fast fashion** | **0 / 10** | — |
| **`antregothique.com`** (site de référence donné par Hakim) | **0 / 10** | — |
| **`castle-gothic.fr`** | **0 / 10** | — |
| **`vetement-gothique.fr`** | **0 / 10** | — |

**Cinq observations, toutes descriptives.**

1. **Il n'y a pas de vide, mais il n'y a pas non plus de forteresse.** Sur les cinq requêtes de rayon
   (`gothique homme`, `homme gothique`, `gothique femme`, `style gothique femme`, `gothique sexy`),
   les positions marchandes appartiennent à **des boutiques spécialisées de même nature qu'une
   boutique drop** — `discobole.fr`, `toonzshop.com`, `pentagrammeshop.com`, `esprit-gothique.fr`,
   `miss-gothique.com`, `satan-shop.com`. C'est le cas de figure du piège n° 6 côté « porte
   difficile, pas porte fermée ».
2. **Aucune marketplace ne domine.** Amazon n'apparaît que 3 fois sur 10, jamais en tête. **Shein et
   Temu sont totalement absents des 10 pages.** Aucune page 1 n'est tenue par une marketplace.
3. **Le seul acteur qui tient vraiment le terrain le tient par le contenu.** `steampunk-boutique.com`
   est présent sur **7 pages 1 sur 10**, et presque toujours avec le **même article** (« Le Style
   Gothique pour les Femmes / les Hommes : Guide Complet »), pas avec une collection. Sur ce bloc de
   requêtes, **la page 1 se gagne en éditorial plus qu'en catalogue** — ce qui est cohérent avec le
   fait que 6 des 11 lignes soient majoritairement informationnelles.
4. **Les trois sites de référence attendus sont absents des dix pages 1.** `antregothique.com`,
   `castle-gothic.fr` et `vetement-gothique.fr` n'apparaissent **nulle part**, y compris sur les
   requêtes de rayon les plus commerciales. Constat de page 1 uniquement : il ne dit rien de leur
   trafic, de leur profondeur, ni de leur position sur les requêtes déjà mesurées au §3 du rapport
   de volume (`robe gothique`, `chaussure gothique`…), **non lues ici**.
5. **Le concurrent le plus visible sur les requêtes de rayon est EMP** (6 pages 1 sur 10), qui est
   un **distributeur européen établi**, pas un drop. Sur `gothique` nu, il est **le seul marchand**
   avec `steampunk-boutique.com` à tenir une position au milieu de Wikipédia, du Larousse, de la BnF
   et du Centre des monuments nationaux.

**Deux ouvertures produit apparues en SERP, non mesurées en volume :** la **lingerie gothique**
(2 rayons + 1 fiche produit sur `gothique sexy`) et le **costume de mariage gothique homme**
(`ottavionuccio.com` sur 2 pages, plus l'associée « Costume mariage gothique homme »). Ni l'une ni
l'autre n'a de volume mesuré — ce sont des pistes, pas des familles.

---

## 6. Ce qui n'a pas pu être mesuré

- **`femme gothiques` (480) n'a pas été lue en SERP.** Son traitement (retrait à 100 %) est un
  **report par analogie** sur `femmes gothiques`, dont elle est la variante d'accord. C'est la seule
  ligne du bloc non adossée à une page 1 réelle. **Impact maximal si le report est faux : + 480 sur
  26 453, soit 1,8 %** — insuffisant pour changer le constat face au plancher.
- **Les annonces Search texte n'ont pas pu être isolées.** Aucune mention « Sponsorisé » n'apparaît
  dans le DOM des dix pages lues, et aucun carrousel Shopping n'y figure. **Je ne peux pas en
  conclure qu'aucun annonceur n'achète ces requêtes** : la lecture DOM sans capture ne garantit pas
  la détection des blocs publicitaires. À traiter comme « non observé », pas comme « absent ».
- **`num=20` n'est plus honoré par Google.** Chaque page 1 rend 8 ou 9 résultats organiques au lieu
  de 20. Les décomptes « qui tient la page 1 » portent donc sur 8-9 positions, **et la profondeur de
  la concurrence au-delà de la page 1 n'est pas jugeable** — c'est le mandat, pas une omission.
- **Aucun prix n'a été relevé.** Aucune sonde Google Shopping n'entre dans cette mission ; les
  étages de prix des concurrents identifiés restent inconnus.
- **Aucune requête de rayon déjà mesurée n'a été vérifiée en SERP.** `robe gothique` (5 020),
  `chaussure gothique` (3 840), `botte gothique` (2 060), `bague gothique` (1 390) et les autres
  familles du §3 de `02-volume-consolide.md` **n'ont pas été lues**. Les 22 120 restent donc un
  volume **non vérifié en intention** : si l'une de ces familles se révélait contaminée, le total de
  26 453 baisserait d'autant. **L'arbitrage ne porte que sur le bloc ambigu.**
- **Les deux ouvertures produit repérées** (lingerie gothique, costume de mariage gothique homme)
  **n'ont aucun volume mesuré**. Elles ne sont comptées nulle part dans les 26 453.
- **Aucune cartographie de concurrent n'a été faite.** Le §5 compte des apparitions en page 1 ; il ne
  dit rien de l'arborescence, du trafic, du positionnement ni de la nature drop ou non des acteurs
  cités. C'est l'objet de l'étape 7 de la méthode, hors mandat ici.

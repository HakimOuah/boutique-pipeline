# CARTOGRAPHIE DE CONCURRENCE — portefeuilles / petite maroquinerie France — 2026-09-02

Étape 7 de `METHODE-ANALYSE-MARCHE.md`. **Aucun volume de mots-clés n'est mesuré ici, aucun verdict
marché n'est rendu** : les volumes sont ceux de `03`, l'intention est celle de `05`, le verdict
appartient à Hakim.

---

## 1. Entrée et méthode

**Dossiers amont utilisés**

- `2026-09-02-03-volumes-consolides.md` — plancher net de marque 169 960 ; huit familles figées :
  homme 60 500, femme 40 500, porte-cartes 40 500, porte-monnaie 22 200, voyage/passeport 4 400,
  compagnon 880, chaîne 590, RFID 390.
- `2026-09-02-05-verification-serp.md` — liste des acteurs de page 1 et bande de prix organique.
- `2026-09-02-08-arborescence-axe.md` (déjà écrit) — c'est lui qui demande explicitement à cette
  étape s'il existe un **trou d'offre réel**. La section 6 y répond.

**Périmètre confié** : cinq domaines seulement, tous rencontrés en page 1 sur au moins deux têtes de
famille, hors GSB et hors luxe.

**Sources par domaine.** Tout le catalogue est relevé par fichiers publics, jamais par navigation
page à page.

| Domaine | Plateforme | Catalogue public lu | Pages de discours lues en texte | Trafic |
|---|---|---|---|---|
| letanneur.com | Shopify | `collections.json` (217), `products.json` (2 pages, 3ᵉ vide), `sitemap_products_1` (496), `sitemap_collections_1` (217), `sitemap_pages_1` (40), `sitemap_blogs_1` (50) | notre-histoire, savoir-faire, maitre-maroquinier, nos-engagements, nos-belles-matieres, livraisons-retours, personnalisation, boutiques, 1 fiche produit | DataForSEO Labs |
| arthur-aston.com | Shopify | `collections.json` (250), `products.json` (4 pages, 5ᵉ vide), `sitemap_products_1` (999), `sitemap_collections_1` (250), `sitemap_pages_1` (10), `sitemap_blogs_1` (49) | notre-histoire, faq, store-locator, 1 fiche produit | DataForSEO Labs |
| nat-nin.com | Shopify | `collections.json` (90), `products.json` (1 page), `sitemap_products_1` (196), `sitemap_collections_1` (88), `sitemap_pages_1` (52), `sitemap_blogs_1` (40) | notre-histoire, la-marque, nos-ateliers, livraison, faire-un-retour, seconde-vie, nos-types-de-cuir, programme-fidelite | DataForSEO Labs |
| hexagona.com | Shopify | `collections.json` (534, en 3 pages), `products.json` (4 pages, 5ᵉ vide), `sitemap_products_1` (798), `sitemap_collections_1` (534), `sitemap_pages_1` (44), `sitemap_blogs_1` (66) | notre-histoire, faq, points-de-vente, devenir-distributeur, programme-de-fidelite, avis, 1 fiche produit | DataForSEO Labs |
| paulmarius.fr | **pas Shopify** — `/collections.json`, `/products.json` et `/sitemap.xml` répondent 404 ; sitemaps déclarés dans `robots.txt` sous `/sitemaps/` (structure de type Magento) | `sitemaps-fr_product.xml` (6 129 URL), `sitemaps-fr_test_category.xml` (600), `sitemaps-fr_cms_fr.xml` (86). **Pas de JSON de prix : prix relevés en lecture de page de catégorie** | notre-histoire, le-cuir-paul-marius, garantie, retours, paiement-livraison, nos-boutiques-officielles, 1 catégorie, 1 fiche produit | DataForSEO Labs |

**Mesure de trafic.** DataForSEO Labs `dataforseo_labs/google/ranked_keywords/live`,
`location_code 2250` (France), `language_code fr`, `limit 1000`, tri par ETV décroissant, appels du
**2026-09-02 vers 22 h 15 UTC** (0 h 15 heure de Paris le 3), coût 0,132 USD par domaine.

**Ce que ce chiffre est, et ce qu'il n'est pas.** L'ETV est un **trafic organique mensuel estimé par
le modèle de l'outil**, pas une visite mesurée. Il ne contient ni le direct, ni le social, ni le
payant. La règle maison « trafic réel ≈ SimilarWeb × 3 » **ne s'y applique pas** et **SimilarWeb n'a
pas été consulté** : la règle n'a donc pas été appliquée, comme sur Noirmont. Tous les chiffres de
trafic de ce dossier sont **nets de marque** : chaque requête contenant le nom du domaine a été
retirée avant toute comparaison. Le premier passage sous-estimait la marque de Nat & Nin (« nat et
nin », « nin nat » échappaient au filtre) et de PaulMarius : les nets publiés ici sont ceux du
second passage, filtres corrigés.

**Un artefact de l'outil, mesuré et corrigé — à lire avant tout chiffre de ce dossier.**

DataForSEO traite `portefeuille homme` et `homme portefeuille` comme **deux mots-clés distincts, à
60 500 recherches chacun**, et leur attribue deux ETV additionnés. Or c'est un seul bucket Google —
c'est précisément le garde-fou n° 3 de la méthode, rencontré ici du côté du trafic et non du volume.
Même mécanique sur les accents (`boite a bijoux` / `boîte à bijoux`) et les pluriels
(`sacoche homme cuir` / `sacoches homme cuir`).

J'ai donc calculé une seconde lecture : **par groupe de permutations, d'accents et de pluriels, on
ne garde que la ligne d'ETV maximale**, jamais la somme.

| Domaine | ETV net brut | ETV en doublon de permutation | ETV net dédupliqué | Part de petite maroquinerie (brut → dédupliqué) |
|---|---:|---:|---:|---|
| letanneur.com | 359 325 | 105 334 (29 %) | **253 990** | 29 % → **35 %** |
| arthur-aston.com | 144 062 | 44 966 (31 %) | **99 096** | 31 % → **33 %** |
| nat-nin.com | 67 617 | 13 274 (20 %) | **54 343** | 33 % → **34 %** |
| hexagona.com | 89 236 | 28 293 (32 %) | **60 942** | 12 % → **12 %** |
| paulmarius.fr | 68 521 | 15 216 (22 %) | **53 305** | 49 % → **55 %** |

**Ce que la déduplication ne change pas** : l'ordre des pages, l'ordre des domaines, et le classement
des axes de découpe. Les conclusions de ce dossier tiennent dans les deux lectures. **Ce qu'elle
change** : tout chiffre absolu doit être lu à 20–32 % près. Les tableaux d'axes de la section 5 sont
calculés sur le **brut**, parce que les ratios y sont stables ; les totaux mis en avant dans le
résumé et les fiches donnent les deux lectures quand l'écart compte.

**Ce qui n'a pas répondu ou a été écarté**

- `paulmarius.fr` : aucun endpoint JSON. Le nombre de produits, les variantes et les prix ne sont
  donc pas lus dans un catalogue structuré mais dans le HTML de 7 pages.
- Aucune donnée publicitaire : ni annonces texte confirmées, ni ancienneté d'achat par mot-clé.
  Qui achète quoi en Ads reste **non établi** dans ce dossier.
- Aucun registre d'entreprise consulté (SIREN, INPI). Les types annoncés en section 3 sont donc des
  **jugements appuyés sur des signaux de catalogue et de site**, pas des preuves d'immatriculation.
- Aucune inscription, aucun compte, aucun formulaire. Ce qui n'est visible qu'après inscription
  (paliers exacts du programme de fidélité Nat & Nin, contenu du Club Hexagona) est déclaré non établi.

---

## 2. Ce qu'il faut retenir en dix lignes

1. Les cinq sont des marques réelles avec catalogue cohérent et `vendor` propre : **aucun dropshipper
   dans le lot**, aucun signal de niche résiduelle, aucun champ fournisseur non nettoyé.
2. **Le sac paie, la petite maroquinerie suit.** Le portefeuille et le porte-cartes ne portent que
   12 à 55 % du trafic estimé de ces sites, en lecture dédupliquée : 35 % chez Le Tanneur, 33 %
   chez Arthur & Aston, 34 % chez Nat & Nin, **12 % chez Hexagona**, 55 % chez PaulMarius.
3. **Un seul axe de découpe rapporte : le type de produit croisé au genre.** Il pèse 76 à 85 % du
   trafic net des quatre Shopify. Tous les autres axes que ces marques ont construits sont morts.
4. Chiffres du constat : **306 collections « nom de modèle » chez Hexagona pour 1 484 ETV (1,7 %)**,
   131 chez Arthur & Aston pour 824 (0,6 %), 34 collections de matière chez Le Tanneur pour 888
   (0,25 %), **44 collections d'occasion et 10 de couleur chez Hexagona pour 0**.
5. Le détail de forme du portefeuille est le cas d'école : Le Tanneur a publié *à volets*,
   *horizontal*, *sans volet*, *avec rabat*, *sans rabat*, *avec poche monnaie* — **six pages à 0**,
   et *vertical* + *long* à 116 ETV à elles deux.
6. **RFID est un attribut, pas une collection.** Hexagona le met dans 115 titres de fiche, Arthur &
   Aston seulement dans les descriptions (0 titre), Nat & Nin nulle part ; la collection dédiée de
   Le Tanneur fait **226 ETV**. Cohérent avec les 390 recherches mesurées en `03`.
7. **La bande de prix comparable est plus basse que ce que le dossier `05` annonçait.** Sur le
   portefeuille homme, médiane catalogue : Arthur & Aston **55 €**, Hexagona **49 €**, PaulMarius
   **35 €** avec un plancher à **20 €** (LePortefeuille ALDO, cuir). Le Tanneur est seul au-dessus,
   à 120–180 €. Les « 69–79 € comparable » de `05` sont un point Shopping, pas la médiane catalogue.
8. La page la plus rentable du secteur est aussi la plus pauvre en offre : **PaulMarius fait 19 375
   ETV nets dédupliqués — 36 % de tout son organique hors marque — sur une page de portefeuilles
   homme qui n'affiche que 3 modèles** (10 URL coloris, 20 et 35 €).
9. Le passeport ne se prend pas en collection mais en fiche : les collections dédiées font 0 à 231
   ETV chez les quatre Shopify, quand **trois fiches « L'Étui pour Passeport » de PaulMarius à 25 €
   font 2 526 ETV nets**.
10. Trois familles mesurées en `03` ne sont servies par personne ou presque : **portefeuille à
    chaîne (0 titre sur 2 487 fiches)**, **portefeuille enfant (0)**, **personnalisation à la
    commande (0 fiche, seulement une page de service chez Le Tanneur)**.

---

## 3. Tableau de synthèse

Trafic = ETV DataForSEO Labs France/fr, **net de marque**, lu le 2026-09-02. Prix = **prix affichés
TTC du catalogue public**, hors frais de port, hors code promo, hors prix réellement payé.

| Domaine | Type (signaux) | Fiches / titres distincts / variantes | Collections (menu / orphelines) | ETV net brut → dédupliqué | Part marque du lu | Concentration (brut) | Part petite maroquinerie (dédup.) | Portefeuille homme min/méd/max | Portefeuille femme |
|---|---|---|---|---|---|---|---|---|---|
| letanneur.com | Marque établie | 495 / **249** / 536 (1,1/fiche) | 217 (112 / 105) | **359 325 → 253 990** (92 % du total lu) | 11 % | top 4 = 42 %, top 10 = 69 % | 35 % | 120 / 150 / 180 | 130 / 180 / 200 |
| arthur-aston.com | Marque établie | 998 / 762 / 3 806 (3,8) | 250 (61 / 189) | **144 062 → 99 096** (98 %) | 7 % | top 4 = 63 %, top 10 = 81 % | 33 % | 25 / 55 / 79 | 35 / 75 / 109 |
| nat-nin.com | Pure player / marque de créatrices | 197 / 194 / 1 416 (7,2) | 90 (20 / 70) | **67 617 → 54 343** (100 %) | **38 %** | top 4 = 63 %, top 10 = 92 % | 34 % | absent du catalogue | 59 / 75 / 95 |
| hexagona.com | Marque établie + réseau de revendeurs | 797 / **207** / 5 131 (6,4) | **534** (51 / 483) | **89 236 → 60 942** (100 %) | 7 % | top 4 = 67 %, top 10 = 87 % | **12 %** | 35 / 49 / 109 | 29 / 49 / 89 |
| paulmarius.fr | Marque établie, réseau ~35 boutiques, récit d'atelier | 6 129 URL produit (≈ 1 URL par coloris) — nombre de modèles non établi | 600 URL de catégorie (menu non départagé) | **68 521 → 53 305** (96 %) | **57 %** | top 4 = 52 %, top 10 = 72 % | **55 %** | 20 / 35 / 35 | 35 / 59,90 / 59,90 |

**Qui tient les têtes de famille, et avec quelle page.** Positions organiques relevées par le même
appel, France/fr, 2026-09-02. À lire avec la réserve ci-dessus : sur une paire inversée, l'outil
rend parfois deux positions différentes pour ce qui est un seul bucket Google — c'est le cas de
PaulMarius, donné 2 sur `homme portefeuille` et 12 sur `portefeuille homme`.

| Tête (volume `03`) | Le Tanneur | Arthur & Aston | Nat & Nin | Hexagona | PaulMarius |
|---|---|---|---|---|---|
| `portefeuille homme` 60 500 | **1** — `/collections/portefeuille-homme` | **2** — `/collections/portefeuille` | — | 8 — `/collections/petite-maroquinerie` | 12 (et 2 sur la forme inversée) — `/homme/petite-maroquinerie/portefeuilles.html` |
| `portefeuille femme` 40 500 | **3** — `/collections/petite-maroquinerie-femme` | 12 — `/collections/portefeuille-1` | 6 — `/collections/portefeuilles` | 32 — `/collections/portefeuille` | 8 — `/femme/petite-maroquinerie/portefeuilles.html` |
| `portefeuille` (nu) 40 500 | **2** — `/collections/portefeuille` | 19 — `/collections/portefeuille-1` | 10 — `/collections/portefeuilles` | 12 — `/collections/portefeuilles-homme` | 54 |
| `porte carte` 40 500 | **2** — `/collections/porte-cartes-homme` | 19 — `/collections/porte-cartes-1` | **3** — `/collections/porte-cartes` | 21 — `/collections/porte-cartes-homme` | 22 |
| `porte monnaie` 22 200 | 8 — `/collections/porte-monnaie-homme` | 62 | **2** — `/collections/porte-monnaies` | 37 — `/collections/porte-monnaie` | **3** — `/femme/petite-maroquinerie/porte-monnaie.html` |
| `porte monnaie homme` 14 800 | **4** — `/collections/porte-monnaie-homme` | 14 — `/collections/porte-monnaie` | — | 12 — `/collections/porte-monnaie-homme` | 32 |

Deux lectures directement utiles. **Le Tanneur est dans les quatre premières positions sur cinq
têtes sur six**, ce qui confirme la « porte ouverte de même nature, dense » de `05` : dense, oui.
Et **la tête `porte monnaie homme` est tenue par des pages faibles** — position 4 pour une
collection de 6 fiches, position 14 pour Arthur & Aston qui en a 77.

Familles couvertes, par domaine :

| Famille (volume `03`) | Le Tanneur | Arthur & Aston | Nat & Nin | Hexagona | PaulMarius |
|---|---|---|---|---|---|
| Portefeuille homme (60 500) | 56 fiches | 179 | **0** | 61 | 3 modèles |
| Portefeuille femme (40 500) | 26 | 62 | 18 | 71 | 3 modèles |
| Porte-cartes (40 500) | 71 (50 H + 21 F) | 144 | 14 | 43 | 2 modèles |
| Porte-monnaie (22 200) | 17 (6 H + 11 F) | 108 | 13 | 33 | 4 modèles |
| Passeport / voyage (4 400) | 7 | 1 | **0** | 2 (+ 46 « compagnon de voyage ») | 1 modèle, 3 coloris |
| Compagnon (880) | fondu dans « Portefeuille et compagnon » | 1 | **0** | 23 | **0** |
| Chaîne (590) | **0** | **0** | **0** | **0** | non relevé |
| RFID (390) | 7 titres | **0 titre** (91 descriptions) | **0** | **115 titres** | non relevé |

---

## 4. Fiche par concurrent

### 4.1 letanneur.com — Le Tanneur

**Qui c'est.** *Marque établie*, et le classement ne tient pas à une impression : antériorité datée
sur son propre site (fondation 1898, deux fondateurs nommés, un porte-monnaie « Le Sans Couture »
présenté comme le premier objet de la maison), atelier localisé (« nos ateliers près du Mans »),
réseau physique — la page boutiques expose **37 codes postaux distincts** — et catalogue parfaitement
cohérent. Signal secondaire mais parlant : le champ `vendor` de Shopify ne porte pas un nom de
fournisseur mais **des noms de lignes** (Lucien 66 fiches, Emilie 41, Emile 34, Martin 31, Louison
28, Juliette 25). Champ détourné pour un usage interne, pas un champ non nettoyé.
Aucun registre d'entreprise consulté : le type reste un jugement adossé à ces signaux.

**Ce qu'il fait exactement.**

- **495 fiches pour 249 titres distincts et 536 variantes**, soit **1,1 variante par fiche** : c'est
  une **fiche par coloris**. Le catalogue réel est de l'ordre de **249 modèles**, pas 495 produits.
  Médiane de 4 images par fiche.
- **217 collections**, dont **112 liées depuis le HTML de l'accueil** et **105 orphelines**. Les
  orphelines ne pèsent que **6 359 ETV, soit 2 %** — l'inverse du cas Maison du Temps, où les
  orphelines portaient l'essentiel.
- **155 des 217 collections ont un ETV estimé nul** dans les 1 000 lignes lues (71 %).
- Répartition du trafic net : **collections 98,1 %**, pages CMS 1,8 %, **blog 0,1 %** (50 articles
  pour 255 ETV).
- Pages qui portent : `sacoche-et-sac-bandouliere-homme` 54 642 (15,2 %), `sac-femme` 39 817,
  `sac-bandouliere-femme` 29 026, **`portefeuille-homme` 28 512** (position 1 sur la tête
  `portefeuille homme` de 60 500 recherches), `boite-bijoux-montres-femme` 24 797,
  `porte-cartes-homme` 15 140, `petite-maroquinerie-femme` 15 078 — c'est **cette page** qui sert
  `portefeuille femme`, et pas une collection nommée « portefeuille femme ». `portefeuille` nu
  6 561, `porte-monnaie-femme` 8 075, `porte-cartes-femme` 7 062, `porte-monnaie-homme` 4 067.
- **Petite maroquinerie = 104 219 ETV, 29 % du net.**
- **8 % du net (28 423 ETV) atterrit sur des URL à préfixe de locale** — `/fr-lb/`, `/fr-dm/`,
  `/fr-ad/`, `/fr-lu/` — dont `/fr-lb/collections/porte-cartes-homme` à 14 726 ETV, presque autant
  que la version française. Observé, non expliqué : c'est une duplication de locale qui capte des
  requêtes françaises.

**Avantages, avec ce qui les étaie.** Antériorité vérifiable et datée sur le site ; fabrication
localisée nommée (Le Mans) et une ligne de menu « Fabriqués en France » ; réseau de 37 adresses ;
**retours 30 jours gratuits en France métropolitaine** écrit noir sur blanc, livraison offerte en
France ; paiement fractionné Alma 3× et 4× ; une **page de personnalisation** et des **ateliers de
maroquinerie à Paris** — cette dernière page fait 1 386 ETV nets à elle seule, donc l'atelier n'est
pas qu'un argument, c'est une page qui travaille ; position 1 sur la plus grosse tête du marché.

**Faiblesses, classées par ce qui nous est utile.**

1. **Ce qu'il ne vend pas** : aucun portefeuille à chaîne, aucun portefeuille enfant, aucune fiche
   de personnalisation (le service existe, le produit personnalisable non), **6 fiches seulement de
   porte-monnaie homme** pour une famille mesurée à 22 200.
2. **Les sujets ouverts sans être tenus** : 34 collections de matière (grainé, lisse, nubuck,
   taurillon, verni, agneau, côtelé, tressé, python embossé, effet froissé, effet mouillé, recyclé,
   double face, polyamide…) pour **888 ETV cumulés, 0,25 % du net** ; nubuck, lisse, taurillon,
   grain croisé, agneau et polyamide à **0**. Dix collections de forme de portefeuille pour 2 562
   ETV, dont 2 446 viennent de la seule `portefeuille-compagnon-femme` qui est en réalité une page
   de type : les **six vrais filtres de forme font 0** et *vertical* + *long* font 116.
3. **Une donnée publique incohérente** : le `products_count` de `collections.json` annonce 2 872
   produits pour la collection Femme alors que `/collections/femme/products.json` en sert 233 et que
   tout le site n'expose que 495 fiches. Le compteur public de ce site n'est pas exploitable.
4. **Trois collections à `products_count` 0 sont publiées** (`en-cuir-verni`, `gants-cuir`,
   `porte-documents-15/16/17`) : des pages vides indexables.
5. **Le blog ne rapporte rien** : 50 articles pour 0,1 % du trafic net.
6. **Prix plancher très haut** sur la petite maroquinerie : 80 € le porte-cartes, 120 € le
   portefeuille. Il ne se bat pas dans la bande où le marché se joue.

**Ce qui n'est pas une faiblesse et qu'on écarte comme axe** : 1898, le nom, les ateliers du Mans,
les 37 boutiques, la position 1 sur `portefeuille homme`. Tout axe qui supposerait de le battre sur
la confiance accumulée, l'antériorité ou le réseau se **jette** — c'est une décision, pas un oubli.

**Axe marketing.**

- *Promesse* : élégance française et maroquinerie « bien finie », posée comme une phrase de maison
  citée entre guillemets sur sa page histoire, adossée à 1898.
- *Réassurance* : livraison offerte France, **retours 30 jours gratuits**, Alma 3×/4×, moyens de
  paiement énumérés, service client par e-mail, boutiques listées avec adresses. Pas de widget
  d'avis tiers détecté sur l'accueil (mention « avis clients » présente, provider non identifié).
- *Récit* : le plus solide des cinq — deux fondateurs nommés, une date, un produit d'origine encore
  fabriqué, un lieu de fabrication. **Où il devient flou** : « cuir pleine fleur uniquement » est
  affirmé au niveau de la maison sans page qui détaille par référence, et la fabrication « près du
  Mans » n'est pas rattachée fiche par fiche — un catalogue de 249 modèles n'est pas dit
  intégralement français, mais rien ne dit lequel l'est.
- *Offre* : bandeau « une jolie surprise au panier dès 400 € » avec date de fin (13/09/2026),
  livraison et retours offerts, Alma. **Reprenable** : le seuil daté et le retour gratuit. **Non
  reprenable** : rien de trompeur relevé — pas de compte à rebours, pas de badge non étayé, **zéro
  fiche avec prix barré** sur les 8 familles de petite maroquinerie relevées.
- *Éditorial* : 50 articles + 7 pages de marque (savoir-faire, matières, maître maroquinier,
  engagements, personnalisation, ateliers). **Poids réel : 1,9 % du trafic net** — dont 1 386 ETV
  sur la seule page d'ateliers parisiens. L'éditorial de marque ne fait pas le trafic ; une page de
  service local, si.

**Personas déduits** (déduction, avec le signal). Femme urbaine 35–60 ans, achat plaisir ou cadeau :
la moitié du catalogue est féminine et le menu femme sépare 17 lignes portant des prénoms.
Homme cadre, achat d'usage : le menu homme est plus court, centré sacoche / serviette /
porte-documents, et sa page histoire nomme explicitement « les femmes et les hommes qui revendiquent
une allure moderne et intemporelle ». Offreur de cadeau : 16 collections d'occasion (Noël, fête des
mères, anniversaire, cadeaux d'affaires, « petites attentions », « pièces d'exception ») et un seuil
cadeau à 400 €.

**Prix par famille** (fiches ; min / médiane / max, prix affichés TTC) : portefeuille homme 56 —
120 / 150 / 180 · portefeuille et compagnon femme 26 — 130 / 180 / 200 · portefeuille toutes 82 —
120 / 150 / 200 · porte-cartes homme 50 — 80 / 100 / 130 · porte-cartes femme 21 — 80 / 100 / 130 ·
porte-monnaie homme 6 — 80 / 90 / 150 · porte-monnaie femme 11 — 110 / 130 / 200 · porte-passeport
7 — 80 / 80 / 100. **Aucune fiche remisée** sur les 189 relevées.

---

### 4.2 arthur-aston.com — Arthur & Aston

**Qui c'est.** *Marque établie*, signaux : `vendor` unique « Arthur & Aston » sur **998 fiches sur
998** ; page histoire qui revendique « maroquiniers depuis plus de 30 années », le statut de marque
française et un **siège en Normandie** ; lignes nommées et reconduites de saison en saison
(Cristiano, Pablo, Diego) ; un **store locator** et une FAQ qui organise le SAV **par dépôt chez un
revendeur**, donc un réseau de distribution réel. Registre non consulté.

**Ce qu'il fait exactement.**

- **998 fiches, 762 titres distincts, 3 806 variantes (3,8 par fiche)**, médiane **10 images** par
  fiche. `product_type` ne décrit pas le produit mais le genre : Hommes 636, Femmes 313, Petite
  Maroquinerie 40 — et une valeur « categorie poubelle faire du tri » sur 1 fiche, plus 2 fiches à
  type vide. Hygiène de données perfectible, mais pas un signal de dropshipping.
- **250 collections** exactement, chiffre confirmé deux fois (`collections.json` page 2 vide,
  `sitemap_collections_1` = 250). **61 liées depuis l'accueil, 189 orphelines** — qui ne pèsent que
  **3 423 ETV, 2 %**. **192 des 250 collections sont à ETV nul (77 %). 12 titres de collection sont
  en doublon.**
- Répartition : **collections 96,5 %**, accueil 2,4 %, fiches produit 0,8 %, **blog 0,3 %** (49
  articles, 490 ETV).
- Pages qui portent : `sac-bandouliere` **44 758 (31 %)**, **`portefeuille` (homme) 23 095 (16 %)**,
  `sacoche` 14 522, `porte-cartes` (homme) 8 573, `sac-de-voyage-1` 6 279, `portefeuille-1` (femme)
  5 995, `porte-cartes-1` (femme) 1 611, `porte-monnaie` 1 346, **`porte-chequier-1` (femme) 1 115**.
- **Petite maroquinerie = 44 060 ETV, 31 % du net.**
- **Doublons de collection mesurés** : `portefeuille` 23 095 / `portefeuille-1` 5 995 /
  `portefeuille-5` 655 / `portefeuille-6` 0 ; `porte-passeport` 38 / `porte-passeport-1` 0 /
  `porte-passeport-2` 0 / `porte-passeport-3` 0 ; `porte-cartes-4` 0 ; `trousse-de-toilette` 0
  contre `trousse-de-toilette-1` 424. **Le doublon ne partage pas le trafic, il meurt** — la règle
  de Maison du Temps se revérifie ici sur quatre paires.

**Avantages étayés.** Le catalogue le plus profond des cinq sur la petite maroquinerie : **179
portefeuilles homme, 144 porte-cartes, 108 porte-monnaie**, contre 56 / 71 / 17 chez Le Tanneur.
Iconographie : 10 images par fiche en médiane. **Retours sous 14 jours par Mondial Relay avec
étiquette prépayée**, procédure écrite étape par étape, choix entre remboursement, échange et bon
d'achat ; **remboursement sous 15 jours** annoncé avec la réserve des périodes de forte affluence,
ce qui est une précision honnête. Livraison gratuite dès 39 € d'achats en France. Scalapay 3× sans
frais. Une **grille de mesures expliquée** (L / l / H, prises couture à couture, tolérance de 1 à
3 cm) et un avertissement écrit sur la variabilité des peaux et des rendus d'écran : c'est de la
pédagogie qui prévient le litige.

**Faiblesses utiles.**

1. **La garantie n'a pas de durée.** La FAQ écrit qu'une garantie commerciale est accordée et
   qu'elle « varie en fonction du type de produit », sans jamais donner un nombre d'années ni un
   tableau par catégorie. Elle liste en revanche ce qui est pris en charge (défauts de fabrication,
   remplacement de pièces métalliques) et ce qui ne l'est pas. **Une garantie sans durée n'est pas
   une garantie opposable** : c'est la brèche la plus nette du lot.
2. **Deux de ses propres pages ne disent pas la même chose du retour** : la fiche produit affiche
   « Retours sous 14 jours » sans condition, la FAQ précise que le retour de convenance est **à la
   charge du client**, frais déduits du remboursement, et que hors France / Allemagne / Belgique /
   Luxembourg / Pays-Bas le client choisit et paie son transporteur.
3. **Retour en boutique impossible** pour un achat en ligne, alors que le SAV renvoie vers les
   revendeurs. Deux logiques de réseau qui ne se rejoignent pas.
4. **RFID absent de tous les titres** alors que 91 fiches en parlent en description. La demande
   mesurée est petite (390), mais elle est servie par un titre, pas par un paragraphe.
5. **131 collections « nom de ligne » pour 824 ETV (0,6 %)** et **21 collections de taille pour 11
   ETV**. Presque tout son arbre de collections est décoratif.
6. Le `<title>` de fiche embarque la référence interne (« Portefeuille Nora Cuir vachette
   A189-155 ») : du caractère utile dépensé pour un SKU.

**Ce qui n'est pas une faiblesse** : les 30 ans, le siège normand, le réseau de revendeurs, la
profondeur de gamme. On ne les attaque pas.

**Axe marketing.**

- *Promesse* : marque française qui « élabore et distribue depuis son siège en Normandie des
  collections créatives pour hommes et femmes », avec une revendication d'allure — lignes épurées,
  graphiques, « look frenchy ».
- *Réassurance* : livraison gratuite dès 39 €, retours 14 jours par Mondial Relay, remboursement 15
  jours, paiement crypté, Scalapay, service client par formulaire et e-mail, expertise du Service
  Qualité sur photo avant procédure. Solide sur la mécanique, **muet sur la durée de garantie**.
- *Récit* : le plus faible des cinq. Pas de fondateur nommé, pas d'année de création, pas de lieu de
  fabrication. « Dans ses ateliers » revient sans dire où. **La brèche est là** : une marque qui dit
  30 ans de métier et ne nomme ni fondateur ni atelier ne peut pas être attaquée sur le made in
  France, mais elle n'y a pas droit non plus.
- *Offre* : seuil de port à 39 €, Scalapay, 9 collections de promotion (soldes, black friday) qui
  pèsent 2 087 ETV. **Une seule fiche sur 179 portefeuilles homme porte un prix barré**, une sur
  110 porte-cartes : pas de fausse remise permanente. Reprenable en entier.
- *Éditorial* : 49 articles, **0,3 % du trafic net**. La page histoire sert en réalité de page de
  collection éditorialisée (elle décrit la collection PE26 et les lignes homme).

**Personas déduits.** Homme actif, achat d'usage et de renouvellement — deux tiers du catalogue est
masculin (636 fiches sur 998) et sa page histoire écrit que le portefeuille est « l'incontournable
de tous, marquant l'arrivée dans la vie d'adulte », le porte-documents étant « le choix numéro deux
de l'homme actif ». Femme active, gamme sac + petite maroquinerie coordonnée. Acheteur qui compare
les caractéristiques : la FAQ explique les mesures, les tolérances, la variabilité du cuir.

**Prix par famille** : portefeuille homme 179 — **25 / 55 / 79** · portefeuille femme 62 —
35 / 75 / 109 · porte-cartes homme 110 — 15 / 39 / 79 · porte-cartes femme 34 — 29 / 55 / 79 ·
porte-monnaie homme 77 — 15 / 29 / 79 · porte-monnaie femme 31 — 25 / 49 / 79 · porte-chéquier femme
8 — 45 / 97 / 109 · compagnon homme 1 fiche — 95.

---

### 4.3 nat-nin.com — Nat & Nin

**Qui c'est.** *Pure player / marque de créatrices.* Signaux : catalogue court et cohérent (197
fiches, 194 titres — quasiment aucun doublon), 7,2 variantes par fiche, `vendor` propre mais en
**deux graphies** (« nat-nin » 147, « nat & nin » 50) ; deux fondatrices nommées avec leur âge et
leur rôle, une année de création (2005 sur la page « la marque »), **quatre boutiques** revendiquées
et détaillées en pages dédiées (Rennes, Montmartre, Beaumarchais, Rive Gauche) ; widget d'avis tiers
Judge.me détecté sur l'accueil. Registre non consulté.

**Ce qu'il fait exactement.**

- **197 fiches, 90 collections**, dont **20 liées depuis l'accueil** et **70 orphelines**. Ici les
  orphelines comptent : **14 736 ETV, 22 % du net** — et notamment `sac-cabas` **10 967 ETV, la
  deuxième page du site, absente du HTML de l'accueil**. C'est le seul des quatre Shopify où le menu
  ment franchement sur ce qui rapporte.
- **68 des 90 collections à ETV nul (76 %).**
- Répartition : collections 65 %, **accueil 28,7 %**, fiches produit 4,4 %, pages 1,1 %, blog 0,8 %.
  Attention : la part d'accueil est presque entièrement de la marque, et elle est déjà retirée du
  net publié.
- **38 % du trafic lu est de la marque** — la part la plus élevée après PaulMarius. Net = 67 617.
- Pages qui portent : `sacs-porte-main` 13 362 (19,8 %), `sac-cabas` 10 967, **`porte-cartes`
  10 309 (15,2 %)**, `sacs-porte-epaule` 7 821, **`porte-monnaies` 6 035**, **`portefeuilles`
  5 717**, `mini-sacs-et-pochettes` 3 883, `sacs-a-franges` 1 748.
- **Petite maroquinerie = 22 155 ETV, 33 % du net, sur trois pages seulement.** Le meilleur
  rendement par page du dossier : 3 collections pour un tiers du trafic.
- Aucun portefeuille homme, aucun passeport, aucun compagnon, aucun RFID, aucun porte-cartes slim,
  aucun métal. Marque **strictement femme**.

**Avantages étayés.** Le récit le plus incarné des cinq : filles d'artisans maroquiniers, atelier
familial près du canal Saint-Martin, entrée à 19 et 24 ans, entreprise « à taille humaine,
indépendante, sans investisseur ». Deux témoignages signés, pas une notice. **Transparence de
production assumée et argumentée** : une page dit que la fabrication est dans la région du Jiangsu,
en Chine, et l'explique par un lien familial plutôt que de le cacher — c'est rare et c'est un
avantage réel de crédibilité. **Programme « seconde vie » avec des règles écrites et bornées** :
dépôt d'un ancien article en cuir de la marque en boutique, bon d'achat plafonné à 50 € par
transaction, minimum d'achat 120 €, validité 12 mois, hors collaborations. Bon d'achat contraint,
mais règle vérifiable. Retraits et retours en boutique et en point relais. Livraison offerte dès
100 € FR/BE, paiement 3× sans frais dès 150 €, offre étudiante −15 %. Judge.me pour les avis.

**Faiblesses utiles.**

1. **Le trou d'offre le plus large du dossier : zéro homme.** Sur une famille mesurée à 60 500
   recherches, ce concurrent n'a rien. Sa seule collection « Portefeuilles & porte-monnaie Homme »
   compte **2 produits** et fait 0 ETV.
2. **Zéro passeport, zéro compagnon, zéro RFID, zéro chaîne.**
3. **Retours à 15 jours, frais à la charge du client**, contre 14 jours prépayés chez Arthur & Aston
   et 30 jours gratuits chez Le Tanneur et PaulMarius. **C'est le retour le moins généreux des
   cinq**, et l'échange n'est possible que « contre le même modèle dans un autre coloris ».
4. **Deux de ses pages ne racontent pas la même histoire** : « notre histoire » écrit « à 19 et
   25 ans », « la marque » écrit « 19 ans et 24 ans » et ajoute l'année 2005 que la première page
   omet. Détail, mais c'est exactement le genre d'écart qui montre que le récit n'est pas tenu par
   une source unique.
5. **Sa deuxième page de trafic est orpheline du menu** (`sac-cabas`, 10 967 ETV). Elle vit par le
   sitemap ; si elle était liée, elle prendrait plus.
6. **11 collections d'occasion, 4 de couleur, 1 de budget, 7 de saison : toutes à 0 ETV.** La page
   « Gift guide » découpée en trois tranches de prix (−50 €, 50–100 €, +150 €) ne rapporte rien.
7. **`product_type` vide sur 196 fiches sur 197.** Aucun typage produit exploitable, ni pour le flux
   ni pour le filtrage.

**Ce qui n'est pas une faiblesse** : les fondatrices, les 20 ans, les 4 boutiques, la seconde vie.
On ne se pose pas en face de ça.

**Axe marketing.** *Promesse* : maroquinerie « élégante, intemporelle et accessible, pensée pour le
quotidien des femmes », mission datée de 20 ans. *Réassurance* : livraison offerte dès 100 €, 3×
dès 150 €, retraits et retours en boutique, avis Judge.me, quatre boutiques avec page propre,
conseils d'entretien, solutions de réparation annoncées, sacherie et emballages recyclables. *Récit*
: le plus fort en incarnation, avec un point remarquable — **la fabrication en Chine est revendiquée
et argumentée**, pas dissimulée. **Où il devient flou** : la « qualité haut de gamme accessible » ne
s'appuie sur aucun élément vérifiable de tannerie ou de norme, et la réparation est annoncée comme
une intention (« nous proposons des solutions ») sans procédure écrite ni tarif. *Offre* : offre
étudiante −15 % sur sélection, surprise sur la 1ʳᵉ commande contre inscription, programme de
fidélité (paliers non établis : ils exigent un compte, non créé), seconde vie. Une seule fiche
remisée sur 13 porte-monnaie. Rien de trompeur relevé. *Éditorial* : 40 articles et une quinzaine de
pages matière (cuir lisse, grainé, peau de pêche, mouton, végétal, imprimé, glacé, canvas) pour
**0,8 % + 1,1 % du trafic net**. Deux pages sortent du lot : `cuir-vegetal` 456 ETV et l'article
`boutique-rennes` 261 ETV. **Les pages matière ne rapportent que si la matière est un objet de
recherche en soi ; « cuir végétal » en est un, « cuir lisse » non.**

**Personas déduits.** Femme active 30–50 ans, achat de renouvellement : tout le catalogue est
féminin, la mission cite « le quotidien des femmes ». Étudiante ou jeune actif sensible au prix :
offre étudiante −15 % affichée en bandeau permanent. Cliente parisienne et rennaise : quatre pages
de boutique et un article de blog sur la boutique de Rennes qui capte réellement du trafic local.
Acheteuse sensible à la durée : page seconde vie, guide d'entretien, réparations.

**Prix par famille** : portefeuille femme 18 — 59 / 75 / 95 · porte-cartes 14 — 25 / 49 / 75 ·
porte-monnaie 13 — 18 / 45 / 79. **Homme : néant.** Note sur `05` : la sonde Shopping y voyait
Nat & Nin à 85 €, le catalogue donne une médiane de **75 €** sur le portefeuille et **49 €** sur le
porte-cartes.

---

### 4.4 hexagona.com — Hexagona

**Qui c'est.** *Marque établie avec réseau de revendeurs.* Signaux : `vendor` propre (789 fiches
« Hexagona » + 8 « Hexagona-MKTP », ce dernier suffixe trahissant un flux marketplace, pas un
fournisseur) ; page histoire qui date l'affaire familiale du milieu des années 1980 et la **fondation
de la maison en 1996 dans le Marais** ; page « points de vente » et page « devenir distributeur »,
donc un réseau B2B assumé ; FAQ qui distingue explicitement le site « réservé aux particuliers » des
revendeurs. `product_type` **le plus riche des cinq** : il décrit le produit **croisé au genre**
(« Portefeuilles européens - Homme » 36, « Portefeuilles italiens - Homme » 15, « Porte-monnaie -
Femme » 16, « Porte-cartes - Homme » 17…). Registre non consulté.

**Ce qu'il fait exactement.**

- **797 fiches mais seulement 207 titres distincts**, 5 131 variantes (6,4 par fiche), **médiane de
  25 images par fiche** — de très loin la fiche la mieux illustrée du dossier. Le revers est
  immédiat : 39 fiches portent le même titre « Sac porté travers », 38 « Sacoche », 33 « Sac porté
  travers - Cuir ». **Un titre de fiche non différencié sur un catalogue de 797 produits est un
  handicap SEO auto-infligé.**
- **534 collections**, le plus gros arbre du dossier. **51 liées depuis l'accueil, 483 orphelines**
  qui pèsent **2 084 ETV, 2 %**. **494 des 534 collections sont à ETV nul : 93 %.** Et **44 titres
  de collection sont en doublon.**
- Répartition : collections 88,4 %, **blog 10,8 %**, fiches produit 0,7 %, pages 0,1 %, accueil 0 %.
- Pages qui portent : `sacs-bandouliere` **33 716 (37,8 %)**, `sacs-a-dos` 12 331, puis — et c'est
  le fait le plus singulier du dossier — **un article de blog sur les nuances de bleu à 8 139 ETV
  (9,1 %)**, qui se classe sur « bleu », « couleurs bleues ». Requête sans intention d'achat de
  maroquinerie : **du trafic qui n'apporte rien au visiteur ni au vendeur**. Un second article
  pastel fait 859. Ensuite `sacs-a-dos-homme` 5 191, `porte-documents-homme` 4 852,
  `petite-maroquinerie` 3 537, `sacs-cabas` 3 528, **`portefeuilles-homme` 2 343**,
  `porte-cartes-homme` 1 951, `porte-monnaie-homme` 680, `portefeuille` 593, `porte-monnaie` 570,
  `compagnons-de-voyage` 179.
- **Petite maroquinerie = 10 353 ETV, 12 % du net seulement** — le plus faible des cinq, alors que
  c'est le catalogue où la petite maroquinerie est la mieux structurée. Son trafic est adossé au sac.

**Avantages étayés.** Le meilleur **vocabulaire produit** du secteur : la nomenclature distingue
portefeuille européen / italien, nombre de volets, Stop RFID, porte-papiers, pince-billets,
compagnon de voyage — et elle est portée par `product_type`, donc exploitable en flux. **115 titres
de fiche portent « Stop RFID »** : il possède la convention de nommage sur cette caractéristique.
25 images par fiche. Réseau de revendeurs France et Europe avec page de recrutement. **Une page
d'avis qui affiche les avis négatifs** (une commande non livrée hors délai, une commande incomplète
avec la réponse de la marque) : compteur servi par un tiers (Judge.me détecté), **4,8/5 sur 3 240
avis** affiché en pied de page — chiffre à considérer comme un compteur d'application installée par
le marchand, pas comme une certification d'organisme. Programme de fidélité daté (« disponible depuis
octobre 2024 »), avec la mention honnête que les achats antérieurs ne comptent pas. Livraison
gratuite dès 39 €. Parrainage, avantage étudiant −10 %, newsletter −10 %.

**Faiblesses utiles.**

1. **Deux blocs de son accueil ne disent pas la même chose de la livraison** : un bandeau annonce
   « LIVRAISON GRATUITE DÈS 39 € » et un bloc de réassurance annonce « LIVRAISON ET RETOURS
   GRATUITS » **sans aucun seuil**. La version sans condition est la plus visible et la moins vraie.
2. **Un porte-carte offert dès 99 € d'achat** : mécanique de cadeau au panier honnête dans son
   principe, mais elle **transforme son propre produit d'appel en prime**, ce qui écrase la valeur
   perçue de la famille porte-cartes qu'il vend par ailleurs 25–65 €.
3. **9,1 % de son trafic vient d'un article sur la couleur bleue.** Page qui reçoit sans rien
   apporter : ni intention, ni produit, ni conversion plausible.
4. **93 % de ses collections ne captent rien** : 306 collections de nom de modèle pour 1 484 ETV,
   **44 collections d'occasion pour 0**, **48 collections de promotion pour 131**, **21 de saison
   pour 0**, **14 de matière pour 0**, **10 de couleur pour 0**, 4 de budget pour 0. Aucun autre
   concurrent du dossier ne pousse aussi loin la production de pages sans retour.
5. **207 titres pour 797 fiches.** Les doublons de titre l'empêchent de se classer sur ses propres
   modèles.
6. **Fabrication 100 % Asie, écrite deux fois** (« la totalité de nos modèles en Asie », « fabriqués
   en Chine par notre propre équipe franco-chinoise »). Ce n'est pas une faiblesse morale, c'est une
   faiblesse d'argument : il ne peut pas revendiquer le made in France, et sa promesse « au prix le
   plus juste » le place explicitement sur le terrain du prix.
7. **Aucun portefeuille à chaîne, aucun portefeuille enfant, aucun porte-cartes slim ni métal.**

**Ce qui n'est pas une faiblesse** : 1996, le réseau de revendeurs, la nomenclature produit, les
3 240 avis, le seuil de port à 39 €. On ne l'attaque ni sur le prix, ni sur la profondeur.

**Axe marketing.** *Promesse* : « un article esthétiquement bien pensé et rigoureusement fabriqué au
prix le plus juste » — positionnement rapport qualité-prix, énoncé comme tel. *Réassurance* :
livraison gratuite dès 39 €, avis 4,8/5 sur 3 240, points de vente, paiement sécurisé, fidélité,
parrainage, conseils d'entretien, FAQ longue et concrète sur la fabrication. *Récit* : famille depuis
les années 1980, fondation 1996 dans le Marais, bureau de style en région parisienne, usine dédiée
en Chine sous contrôle des fondateurs, normes sociales et environnementales évoquées. **Où il devient
flou** : « nos ateliers respectent les normes sociales et environnementales » sans nommer une seule
norme, un seul audit, un seul organisme — là où PaulMarius cite SEDEX, ISO 9001 et Better Factories
Cambodia. C'est la même affirmation, chez l'un vérifiable, chez l'autre non. *Offre* : trois
bandeaux simultanés (nouvelle collection, porte-carte offert dès 99 €, livraison gratuite dès 39 €,
avantage étudiant −10 %), newsletter −10 %, fidélité en points convertibles. **Reprenable** : le
seuil de port, le cadeau au panier daté, la fidélité avec sa date de début. **Non reprenable** : le
bloc « livraison et retours gratuits » sans seuil, contredit par son propre bandeau. *Éditorial* :
66 articles pour **10,8 % du trafic net**, mais **75 % de ce poids tient sur deux articles de
couleur sans intention commerciale**. Le blog qui « marche » ici ne vend rien.

**Personas déduits.** Acheteur rapport qualité-prix, homme et femme, 30–60 ans : la promesse dit
« au prix le plus juste », la médiane de la petite maroquinerie est à 35–49 €, et les avis publiés
répètent « qualité à des prix raisonnables ». Homme fonctionnel : `product_type` détaille
porte-documents, cartable, baisenville, pince-billets, porte-papiers. Femme qui cherche du choix :
« un grand choix », « il y en a pour tous les goûts » reviennent dans les avis, et 284 fiches sacs
femme. Étudiant : avantage −10 % permanent.

**Prix par famille** : portefeuille homme 61 — **35 / 49 / 109** · portefeuille femme et mixte 71 —
29 / 49 / 89 · porte-cartes homme 20 — 25 / 35 / 55 · porte-cartes femme 23 — 25 / 35 / 65 ·
porte-monnaie homme 17 — 25 / 35 / 39 · porte-monnaie femme 16 — 25 / 35 / 65 · compagnon de voyage
23 — 39 / 65 / 79. Aucune fiche remisée sur les 231 relevées.

---

### 4.5 paulmarius.fr — PaulMarius

**Qui c'est.** *Marque établie à récit d'atelier, hors Shopify.* Signaux : plateforme propriétaire de
type Magento (sitemaps sous `/sitemaps/`, URL en `.html`, comparateur de produits, « no-route ») ;
**fondateur nommé, daté et raconté** — Florent Poirier, autodidacte issu de la brocante, premiers
croquis en 2010 à 23 ans ; **réseau physique** — la page « nos boutiques officielles » expose 35
codes postaux distincts et un règlement de jeu du sitemap mentionne l'ouverture de la 40ᵉ boutique ;
distributeurs officiels ; expédition depuis la Normandie. Registre non consulté.

**Ce qu'il fait exactement.**

- **6 129 URL produit dans le sitemap FR**, mais c'est **une URL par coloris** : la page portefeuille
  homme n'expose que **10 URL pour 3 modèles** (LePortefeuille Marius en 4 coloris, PAUL en 3, ALDO
  en 3). **Le nombre de modèles réels n'est pas établi** — c'est la limite majeure de cette fiche.
- **600 URL de catégorie**, 86 pages CMS (dont un blog en 4 rubriques et une vingtaine de lookbooks).
- **57 % du trafic lu est de la marque** : le net tombe de 161 149 à **68 521**. C'est la marque la
  plus recherchée des cinq par son nom.
- Répartition du net : **pages de catégorie 78,2 %**, **fiches produit 19,8 % (115 URL)**, accueil
  1,9 %, **blog et lookbooks 0 %**.
- Pages qui portent : **`/homme/petite-maroquinerie/portefeuilles.html` 20 314 ETV brut, 19 375
  dédupliqué — 36 % de tout son organique hors marque, sur une page à 3 modèles**. Attention :
  **18 392 de ces 20 314 viennent de la seule formulation inversée `homme portefeuille`, où l'outil
  le donne en position 2, alors qu'il le donne en position 12 sur `portefeuille homme`** — même
  bucket Google, deux positions rendues. Le rang réel de cette page sur la tête de 60 500 est donc
  **incertain entre 2 et 12** ; ce qui est sûr, c'est qu'elle est la première page du site et
  qu'elle n'a que trois modèles à montrer. Puis `/femme/accessoire-cuir/etui-lunettes-cuir.html`
  5 757, `/femme/sac-cuir/mini-sac-cuir.html` 5 232, `/femme/petite-maroquinerie/porte-monnaie.html`
  4 007, `/homme/sacs.html` 3 300, `/femme/petite-maroquinerie-cuir/porte-cartes-cuir.html` 3 063,
  `/femme/petite-maroquinerie/portefeuilles.html` 2 595, `/femme/sacs/cartables-et-porte-documents.html`
  2 058. Et **trois fiches « L'Étui pour Passeport » (cuivré 1 444, naturel 897, noir 185) pour
  2 526 ETV nets** à 25 € l'unité.
- **Petite maroquinerie = 33 692 ETV, 49 % du net** — la part la plus élevée des cinq.

**Avantages étayés.** **La garantie la mieux écrite du dossier** : 2 ans, avec le périmètre d'achat
(site, boutiques, distributeurs), la couverture (défauts de matières et de confection), les
**exclusions listées** (usure normale, modification hors réparation maison, dommage accidentel,
entretien inapproprié), le canal (Service Relation Client), les **horaires précis** et la consigne
de joindre des photos. **Retours 30 jours offerts** avec les conditions d'éligibilité écrites, la
liste nominative des 24 pays UE éligibles, l'état exigé du produit et la règle « un seul retour
offert par commande ». Livraison offerte dès 59 €, tarifs par pays, DHL et Colissimo, **expédition
sous 24 h depuis la Normandie** affichée sur la fiche. Paiement Adyen, fractionnement Klarna avec la
mention explicite que le contrat de financement n'est pas celui de la marque. **Fabrication
documentée et auditée** : ateliers partenaires en Inde, Cambodge, Italie et France, audits **SEDEX,
ISO 9001, Better Factories Cambodia** nommés. **Cuir certifié LWG** affiché sur la fiche produit.
Une page pédagogique sur le cuir qui explique pleine fleur, fleur corrigée, pigmenté, double ton,
huilé, nubuck, velours — le meilleur contenu matière des cinq. Réseau de ~35 boutiques.

**Faiblesses utiles.**

1. **La page la plus rentable du secteur est presque vide.** 3 modèles de portefeuille homme pour
   20 314 ETV nets. Une page qui capte cette demande et n'a rien à montrer est un signal d'offre
   manquante — chez lui, et donc un espace pour quelqu'un d'autre.
2. **Sa page retours contient des dates périmées** : elle décrit encore le régime des commandes
   « entre le 1er novembre et le 31 décembre 2025 » retournables « jusqu'au 31 janvier 2026 », à
   côté du régime en vigueur. Deux régimes empilés sur la même page, dont un mort.
3. **Le récit d'atelier et la réalité de production ne coïncident pas.** Le fondateur est présenté
   comme créateur maroquinier et la marque expédie de Normandie, mais la fabrication est en Inde, au
   Cambodge, en Italie et en France, sans dire quelle part revient à quel pays ni quel produit vient
   d'où. C'est écrit honnêtement — « la qualité ne dépend pas d'un lieu » — mais **le récit
   normand porte une attente que la production ne confirme pas**.
4. **Zéro compagnon, zéro RFID en évidence, zéro portefeuille à chaîne** dans les pages relevées.
5. **86 pages CMS, une vingtaine de lookbooks, un blog en 4 rubriques : 0 % du trafic net.** C'est
   le contre-exemple parfait de l'éditorial qui coûte et ne rapporte pas.
6. **Une URL par coloris** : les quatre coloris du même portefeuille se concurrencent, et le
   sélecteur de couleur renvoie vers d'autres URL au lieu de variantes.
7. **57 % de son organique est de la marque.** Retirée, il pèse moins que Hexagona ; son SEO
   générique tient sur une dizaine de pages.

**Ce qui n'est pas une faiblesse** : Florent Poirier, 2010, les 35 boutiques, la garantie 2 ans, les
audits nommés, le cuir LWG, l'expédition 24 h. On ne se met pas en face de ce bloc.

**Axe marketing.** *Promesse* : « des petits luxes qui font de grands plaisirs » — maroquinerie
libre et accessible, ton joueur assumé autour du « grain de folie ». *Réassurance* : la plus dense
des cinq (garantie 2 ans détaillée, retours 30 jours offerts, port offert dès 59 €, 24 h depuis la
Normandie, Adyen, Klarna, boutiques, distributeurs, LWG, audits nommés). *Récit* : fondateur,
année, âge, origine (brocante), rencontre avec l'atelier, extension de gamme racontée. **Où il
devient flou** : la répartition réelle de la production entre quatre pays, et le lien entre
« créateur maroquinier » et une fabrication majoritairement lointaine. *Offre* : cadeau au panier
daté (tote bag 29,90 € offert dès 150 €, du 26 août au 30 septembre 2026), jeux-concours nombreux,
éditions limitées, cartes cadeaux. **Reprenable** : le cadeau daté avec ses conditions écrites en
astérisque. **Non reprenable** : rien de trompeur relevé, mais la page retours à deux régimes
empilés est un défaut d'entretien à ne pas imiter. *Éditorial* : blog + lookbooks + pages matière
pour **0 % du trafic net mesuré**. Seule la page « le cuir PAUL MARIUS » a une valeur d'usage, pas
d'acquisition.

**Personas déduits.** Femme 25–45 ans, achat plaisir à petit prix : le catalogue femme domine, les
prénoms de modèles (Mademoiselle George, Valentine, Basile, Gustave) et les coloris fantaisie
(Tie & Dye, Arty Kaki, Or Rose, Léopard) structurent l'offre. Homme au premier portefeuille en
cuir : la page qui capte la tête `portefeuille homme` n'offre que 3 modèles à 20 et 35 €, ce qui
décrit un acheteur de premier prix, pas un acheteur de renouvellement. Voyageur : l'étui passeport
à 25 € est un de ses produits les plus visibles. Offreur de cadeau : cadeau au panier, cartes
cadeaux, boutique de Noël.

**Prix par famille** (relevés en lecture de page, pas en JSON) : portefeuille homme — **20 / 35 / 35**
(ALDO 20, Marius 35, PAUL 35) · portefeuille femme — 35 / 59,90 / 59,90 (Mademoiselle George Nano 35,
Alice 55, Valentine 59,90) · porte-cartes femme — 10 / 35 / 35 (Gabin 10–15, Basile 35) ·
porte-cartes homme — 10 / 20 / 29,90 · porte-monnaie femme — 20 / 25 / 35 · porte-monnaie homme —
20 (AUGUSTIN) · étui passeport — 25. Note sur `05` : la sonde Shopping y voyait PaulMarius à 55 € ;
**la petite maroquinerie de son catalogue tient en réalité entre 10 et 60 €.**

---

## 5. Les découpes de collection relevées, par axe, avec leur trafic

Trafic = ETV net de marque de **toutes les collections rattachées à l'axe**, sur le total net du
domaine. Une collection = un axe, le plus spécifique d'abord.

| Axe de découpe | Le Tanneur (217 coll.) | Arthur & Aston (250) | Nat & Nin (90) | Hexagona (534) | Verdict |
|---|---|---|---|---|---|
| **Type de produit × genre** | 38 coll. → **276 406 (76,9 %)** | 45 → **120 425 (83,6 %)** | 21 → **57 276 (84,7 %)** | 38 → **67 473 (75,6 %)** | **À reprendre** — seul axe qui rapporte chez les quatre |
| Genre seul (page Homme, page Femme) | 2 → 15 712 (4,4 %) | 2 → 0 | 1 → 0 | 2 → 201 (0,2 %) | À reprendre **seulement** en page de niveau supérieur, jamais comme substitut du croisement |
| Fonction nommée qui **est** le produit (porte-documents, sac ordinateur, sac de voyage) | 16 → 28 863 (8 %) dont sac-ordinateur-femme 10 626 | 17 → 14 452 (10 %) dont sac de voyage 6 345 | 3 → 432 | 19 → 5 040 dont porte-documents 4 852 | **À reprendre** quand la fonction est le nom du produit |
| Fonction en **filtre** (RFID, carte d'identité, chéquier, passeport) | RFID **226**, carte d'identité **368**, passeport 231 | chéquier **1 227**, passeport 38, porte-papiers 318 | 0 | passeport **0** | **À ne pas créer**, sauf chéquier — 1 227 ETV chez A&A, famille absente de `03`, **à faire mesurer avant toute décision** |
| Capacité / taille (mini, petit, moyen, grand) | 18 → 16 995 (4,7 %), dont `petite-maroquinerie-femme` 15 078 | **21 → 11 (0,0 %)** | 2 → 3 883 | 22 → 4 177 | **À ne pas créer** comme filtre de taille. Les 16 995 de Le Tanneur sont une page de rayon mal rangée par mon classement, pas un filtre |
| **Forme / construction du portefeuille** (à volets, horizontal, vertical, long, avec/sans rabat, avec poche monnaie) | 10 → 2 562 dont 2 446 pour `portefeuille-compagnon-femme` (une page de type). **Les 6 vrais filtres de forme : 0. Vertical 64 + long 52 = 116** | 2 → 94 | 1 → 0 | 4 → 294 | **À ne pas créer.** Le cas Noirmont se rejoue à l'identique : 116 ETV sur 359 325, soit 0,03 % |
| **Matière** (cuir grainé, lisse, nubuck, taurillon, verni, toile, raphia…) | **34 → 888 (0,25 %)**. Nubuck, lisse, taurillon, grain croisé, agneau, polyamide, python, froissé, mouillé, recyclé, double face, côtelé : **0** | 12 → 1 065 (0,7 %) | 5 → 461 (0,7 %), dont raphia 461 | **14 → 0** | **À ne pas créer**, sauf si la matière est elle-même un objet de recherche (`cuir végétal` 456 ETV en page CMS chez Nat & Nin, raphia 461) |
| **Couleur** | — | 1 → 0 | **4 → 0** | **10 → 0** | **À ne pas créer.** 15 collections de couleur cumulées chez trois concurrents : **0 ETV** |
| **Occasion / cadeau** (Noël, fête des mères, mariage, cadeaux d'affaires) | 16 → 5 653 (1,6 %) | 1 → 0 | **11 → 0** | **44 → 0** | **À ne pas créer.** 72 collections cumulées pour 5 653, dont 0 chez trois des quatre |
| **Budget / tranches de prix** | inclus dans occasion (« Moins de 350 € ») | — | **1 → 0** | **4 → 0** | **À ne pas créer** |
| **Saison / collection datée** (PE26, AH25, lookbook) | 12 → 216 | **7 → 0** | **7 → 0** | **21 → 0** | **À ne pas créer** |
| **Promotion / déstockage** | 6 → 0 | 9 → 2 087 (1,4 %) | 8 → 491 | **48 → 131 (0,1 %)** | À ne pas créer en série. Une page soldes suffit ; 48 pages de promo rapportent 131 |
| **Nom de modèle / de ligne maison** | 65 → 1 427 (0,4 %) | **131 → 824 (0,6 %)** | 24 → 150 (0,2 %) | **306 → 1 484 (1,7 %)** | **À ne pas créer.** 526 collections cumulées pour 3 885 ETV. C'est la plus grosse dépense de pages du secteur pour le plus faible retour |
| Engagement / seconde vie | — | 2 → 0 | 2 → 162 | 2 → 0 | Signal faible. Utile comme page de service, pas comme collection |

**Collections à ETV estimé nul** : 155/217 chez Le Tanneur (71 %), 192/250 chez Arthur & Aston
(77 %), 68/90 chez Nat & Nin (76 %), **494/534 chez Hexagona (93 %)**. Conformément à la méthode, un
zéro isolé n'est pas un verdict ; ici **quatre catalogues indépendants convergent axe par axe**, ce
qui rend le signal exploitable pour les axes couleur, occasion, budget, saison, nom de modèle et
forme de portefeuille.

**Menu contre sitemap.** Contrairement au cas Maison du Temps, les orphelines ne portent presque
rien : 2 % chez Le Tanneur, 2 % chez Arthur & Aston, 2 % chez Hexagona. **La seule exception est
Nat & Nin, où 70 collections orphelines pèsent 22 %** et où la deuxième page du site,
`/collections/sac-cabas` à 10 967 ETV, **n'est pas liée depuis l'accueil**. Enseignement : le
sitemap suffit à indexer, mais sur ces quatre sites c'est bien le menu qui concentre le trafic — et
la seule page orpheline qui gagne est une page de **type de produit**, jamais un filtre.

---

## 6. Les places libres, au regard des familles déjà mesurées

Aucun volume n'est mesuré ici. Chaque place libre est **une absence d'offre observée dans les
catalogues**, rapportée à une famille déjà mesurée en `03` et vérifiée en `05`.

### Les trois places libres

**1. Le portefeuille homme entre 35 et 55 €, avec une page qui a vraiment du stock.**
Famille mesurée : **60 500, retenue à 100 % en SERP**. Le fait d'inventaire : la page qui capte
cette tête chez PaulMarius fait **20 314 ETV nets avec 3 modèles**, et celle d'Hexagona **2 343 avec
61 fiches** vendues à médiane 49 €. Le Tanneur tient la position 1 mais démarre à 120 €. Arthur &
Aston a 179 fiches à médiane 55 €. **Personne n'occupe simultanément la profondeur et la bande
35–55 €** : Hexagona est dans la bande sans le trafic, PaulMarius a le trafic sans la profondeur,
Arthur & Aston a les deux mais concentre 16 % de son trafic sur une seule page dont l'arborescence
interne est brouillée par quatre doublons. C'est la place libre la mieux étayée du dossier.

**2. Le porte-monnaie homme.**
Famille mesurée : **22 200, retenue à 100 %**. Le fait d'inventaire : **6 fiches chez Le Tanneur**
(80–150 €), **0 chez Nat & Nin**, 17 chez Hexagona (25–39 €), 1 modèle chez PaulMarius (20 €).
Seul Arthur & Aston en a 77. Les pages correspondantes captent peu : `porte-monnaie` d'A&A 1 346,
`porte-monnaie-homme` d'Hexagona 680, `porte-monnaie-homme` de Le Tanneur 4 067. **La demande est
mesurée à 22 200 et la meilleure page du secteur en capte 8 075** (`porte-monnaie-femme` de Le
Tanneur). Sous-servie côté homme, en produit comme en page.

**3. Le porte-cartes cuir à 25–49 €, avec un titre qui nomme la contenance.**
Famille mesurée : **40 500, retenue à 100 % comme famille propre** — la SERP de `05` note explicitement
« slim / aluminium / cuir » et un socle marketplace à 8–30 €. Le fait d'inventaire : **aucun des
quatre catalogues Shopify ne met « slim », « ultra fin », « 6 cartes » ou « aluminium » dans un
titre de fiche** (0 sur 2 487 fiches en titres et tags). Ils vendent « Porte-cartes » nu. Les prix :
Hexagona 25–65 (méd. 35), Nat & Nin 25–75 (méd. 49), Arthur & Aston 15–79 (méd. 39), PaulMarius
10–35, Le Tanneur 80–130. **La bande 25–49 € est occupée en prix mais pas en vocabulaire.**

### Trois autres absences observées, plus étroites

- **Le portefeuille à chaîne** : famille mesurée à 590 seulement, mais **0 titre sur 2 487 fiches
  relevées**, chez les cinq. Trop petit pour porter une boutique, cohérent avec `08` qui le classe
  en filtre. Noté pour mémoire, pas comme place à prendre.
- **Le porte-chéquier** : **1 227 ETV nets chez Arthur & Aston** (dont 1 115 sur la seule page
  femme), servi par 8 fiches à 45–109 €. **Cette famille n'existe pas dans le consolidé `03`.** Ce
  n'est pas une place libre tant qu'elle n'est pas mesurée : c'est une **demande de mesure**, à
  verser à l'étape 2 si Hakim le décide.
- **L'étui passeport en fiche produit, pas en collection** : les collections dédiées font 0 à 231
  ETV chez les quatre Shopify, quand **trois fiches PaulMarius à 25 € font 2 526 ETV nets**. La
  famille mesurée est faible (4 400, ticket 10–25 €), mais le mode de captation est instructif :
  **une fiche bien nommée bat une collection sur cette famille**.

### Ce qui n'est pas une place libre, et qu'on écarte comme décision

- **Le made in France, le savoir-faire, l'atelier, l'héritage.** Le Tanneur (1898, Le Mans, 37
  adresses), PaulMarius (fondateur nommé, 35 boutiques, audits SEDEX/ISO 9001, cuir LWG) et Nat & Nin
  (filles d'artisans, atelier familial, 4 boutiques) tiennent ce terrain avec des faits vérifiables.
  **Jeté**, comme déjà décidé en `08`.
- **Le prix bas.** Hexagona affiche « au prix le plus juste » avec une médiane à 49 € et une
  livraison offerte dès 39 € ; PaulMarius descend à 20 € sur un portefeuille cuir homme. Se battre
  sous eux, c'est entrer dans la bande marketplace de `05` (10–30 €). **Jeté.**
- **La profondeur de gamme.** Arthur & Aston aligne 179 portefeuilles homme et 144 porte-cartes.
  On ne gagne pas au nombre de références. **Jeté.**
- **Le blog et le lookbook.** Mesuré : 0,1 % chez Le Tanneur, 0,3 % chez Arthur & Aston, 0,8 % chez
  Nat & Nin, **0 % chez PaulMarius malgré 86 pages CMS**. Le seul blog qui pèse (Hexagona, 10,8 %)
  le fait sur des requêtes de couleur sans intention d'achat. **Jeté comme levier d'acquisition.**
- **Le RFID comme promesse.** 390 recherches mesurées, collection dédiée à 226 ETV, 115 titres chez
  Hexagona qui possède déjà la convention. **Attribut de fiche, pas axe.** Confirme `08`.

### Une correction factuelle à porter à l'étape 9

`05` retenait un comparable à **69–79 € homme et 75–85 € femme**, lus en Shopping. La lecture des
catalogues donne, sur le portefeuille homme : **Arthur & Aston médiane 55 € (25–79), Hexagona
médiane 49 € (35–109), PaulMarius 20–35 €**. Sur le portefeuille femme : **Nat & Nin médiane 75 €
(59–95), Arthur & Aston 75 € (35–109), Hexagona 49 € (29–89)**. Le plancher comparable — même
produit, vendeur indépendant, sans récit de luxe — est **20 € chez PaulMarius (LePortefeuille ALDO,
cuir)**, ce qui ne franchit pas le test de vraisemblance ×4 par rapport au plafond de 109 € : le
plancher tient. **Le positionnement à 79 € proposé en `08` est au-dessus de la médiane de trois des
cinq acteurs.** Ce n'est pas un verdict, c'est un chiffre à réinstruire à l'étape 9, avec le coût
rendu que personne n'a encore.

---

## 7. Ce qu'ils font qu'on ne fait pas

| Pratique | Qui le fait, et ce qu'on a mesuré | Ce qu'on en fait |
|---|---|---|
| Garantie chiffrée avec exclusions écrites | PaulMarius : 2 ans, périmètre, couverture, exclusions, canal, horaires | **À reprendre en structure.** Une garantie sans durée (Arthur & Aston) n'est pas opposable |
| Retours 30 jours offerts avec conditions d'éligibilité nommées | Le Tanneur (30 j gratuits FR), PaulMarius (30 j, 24 pays UE listés, un retour par commande) | **À reprendre.** C'est la borne du secteur ; Nat & Nin à 15 j payants est le plancher |
| Grille de mesures expliquée + avertissement sur la variabilité du cuir et des écrans | Arthur & Aston (L/l/H couture à couture, tolérance 1–3 cm) | **À reprendre.** Prévient le litige sans rien affirmer sur nous |
| `product_type` qui décrit le produit **croisé au genre** | Hexagona (« Portefeuilles européens - Homme », « Porte-monnaie - Femme ») | **À reprendre.** Exploitable en flux Merchant Center ; l'inverse (A&A : « Hommes »/« Femmes », Nat & Nin : vide) ne l'est pas |
| Une seule variante par fiche, coloris en fiches séparées | Le Tanneur (1,1 variante/fiche), PaulMarius (1 URL par coloris) | **À ne pas reprendre.** Cannibalisation observée : les 4 coloris du même portefeuille PaulMarius se concurrencent |
| Titres de fiche non différenciés | Hexagona : 207 titres pour 797 fiches, 39 fois « Sac porté travers » | **À ne pas reprendre.** Handicap SEO auto-infligé |
| Cadeau au panier daté, conditions en astérisque | Le Tanneur (dès 400 €, fin 13/09/2026), PaulMarius (tote bag dès 150 €, 26/08–30/09/2026), Hexagona (porte-carte dès 99 €) | **Reprenable** : la date de fin et les conditions écrites sont honnêtes. Chez Hexagona, offrir un porte-cartes écrase la valeur d'une famille qu'il vend 25–65 € |
| Bloc de réassurance sans seuil à côté d'un bandeau avec seuil | Hexagona : « LIVRAISON ET RETOURS GRATUITS » vs « LIVRAISON GRATUITE DÈS 39 € » | **À ne pas reprendre.** Contradiction interne, la version la plus visible est la moins vraie |
| Normes et audits **nommés** | PaulMarius : SEDEX, ISO 9001, Better Factories Cambodia, cuir LWG | À reprendre **seulement si vrai**. Hexagona fait la même affirmation sans nommer : c'est la différence entre étayé et non étayé |
| Transparence de production revendiquée | Nat & Nin : page dédiée à la fabrication au Jiangsu, argumentée | À reprendre en principe : dire d'où ça vient ne coûte rien et n'exige aucune affirmation sur nous |
| Widget d'avis tiers avec avis négatifs visibles | Hexagona (Judge.me, 4,8/5 sur 3 240, avis négatifs publiés et répondus), Nat & Nin (Judge.me) | À reprendre quand il y aura des commandes. Ce n'est pas un compteur maison, mais ce n'est pas une certification d'organisme non plus |
| Programme de fidélité **daté** | Hexagona : « disponible depuis octobre 2024, les achats antérieurs ne comptent pas » | Reprenable : la restriction écrite vaut mieux qu'un flou |
| Seconde vie bornée | Nat & Nin : dépôt en boutique, bon plafonné 50 €, minimum 120 €, 12 mois, hors collabs | Non reprenable sans boutique physique. Noté comme mécanique |
| Page de service local qui capte | Le Tanneur : `/pages/ateliers-maroquinerie-paris` **1 386 ETV**, Nat & Nin : article `boutique-rennes` 261 ETV | Non reprenable sans lieu réel. **À ne pas simuler** |
| Blog de marque, lookbooks | Les cinq. Mesuré : 0 à 0,8 % du trafic net, sauf Hexagona 10,8 % dont 75 % sur deux articles de couleur sans intention | **À ne pas reprendre** comme levier d'acquisition |
| Production massive de collections | Hexagona 534 (93 % à zéro), Arthur & Aston 250 (77 % à zéro) | **À ne pas reprendre.** Une collection sans H1 ni meta propres ne rapporte rien, et le doublon meurt : quatre paires vérifiées chez A&A |
| URL à préfixe de locale qui captent des requêtes FR | Le Tanneur : 8 % du net sur `/fr-lb/`, `/fr-dm/`, `/fr-ad/`, `/fr-lu/`, dont 14 726 sur une seule | Observé, non expliqué. **À ne pas imiter sans comprendre** — cela ressemble à de la duplication qui se cannibalise |

---

## 8. Ce qui est sourçable chez nos fournisseurs, et ce qui ne l'est pas

Aucun coût rendu n'est connu à ce stade : le sourcing n'a pas été lancé (`08` le dit également). Les
trois blocs ci-dessous classent **par nature de produit**, pas par rentabilité.

### À sourcer

| Produit | Comparable de prix identifié | Preuve |
|---|---|---|
| Portefeuille homme cuir, 2 volets, format compact | **Hexagona médiane 49 € (35–109), Arthur & Aston médiane 55 € (25–79)** | Deux marques établies vendent exactement ce produit dans cette bande. Ce sont les vrais comparables — ni marque officielle, ni marque à récit de luxe |
| Porte-cartes cuir | **Hexagona médiane 35 €, Arthur & Aston 39 €, Nat & Nin 49 €** | 43 à 144 fiches par concurrent dans la bande 15–79 € |
| Porte-monnaie cuir zippé | **Hexagona 25–39 €, Arthur & Aston 15–79 €** | 17 à 108 fiches. Ticket bas, à surveiller côté ratio |
| Portefeuille femme cuir / compagnon | **Hexagona 29–89 € (méd. 49), Nat & Nin 59–95 € (méd. 75)** | Deux comparables indépendants dans deux bandes distinctes |
| Étui passeport cuir | **PaulMarius 25 €** | 2 526 ETV nets sur trois fiches à ce prix — comparable direct, prix affiché |

### Sourçable mais à écarter formellement

| Produit | Motif écrit |
|---|---|
| Portefeuille à chaîne | Famille mesurée à **590** en `03`. Zéro offre chez les cinq, mais un volume de 590 ne porte pas une page de rayon. **Écarté pour taille**, pas pour concurrence |
| Portefeuille RFID vendu comme tel | Famille mesurée à **390**. Collection dédiée du leader à **226 ETV**. Hexagona possède déjà la convention de titre avec 115 fiches. **Écarté comme axe, conservé comme attribut de fiche** |
| Porte-cartes aluminium / métal à 8–30 € | `05` situe le socle marketplace à 8–30 € sur cette tête. **Mur de prix** : bande où le ratio prix ÷ CPC casse, et aucun des cinq n'y va. **Écarté** |
| Portefeuille de marque tierce (LV, Goyard, Lacoste, Chanel, Cabaia) | Retiré du net en `04` : **marque tierce inutilisable en flux Merchant Center et en titre**. **Écarté** |
| Robe / jupe portefeuille | Retiré à 100 % en `05` : autre produit, autre univers. **Écarté** |
| Coffret à montres, boîte à bijoux | **36 608 ETV nets chez Le Tanneur (10,2 %)**, dont `boite-bijoux-montres-femme` 24 797 et `coffret-a-montres-homme` 12 438. Univers adjacent réel, **hors périmètre de ce dossier** : ne pas l'ouvrir ici, le signaler |

### Non sourçable, ou hors de portée

| Élément | Pourquoi |
|---|---|
| Boutique physique, retrait et retour en magasin | Le Tanneur 37 adresses, PaulMarius ~35, Nat & Nin 4, Hexagona un réseau de revendeurs. **Non réplicable** |
| Atelier français, made in France, personnalisation en atelier | Le Tanneur (Le Mans, page personnalisation, ateliers Paris). Toute affirmation de ce type serait fausse chez nous |
| Certifications et audits nommés (SEDEX, ISO 9001, Better Factories, LWG) | PaulMarius les cite parce qu'il contracte les ateliers. **Non transposable** sans la même chaîne |
| Antériorité (1898, 1996, 2005, 2010) | Non réplicable par nature |
| Seconde vie avec reprise en boutique | Suppose un point de vente. **Non réplicable** |

---

## 9. Ce que je n'ai pas pu établir, dit franchement

1. **PaulMarius : nombre de modèles inconnu.** Le site n'expose aucun endpoint JSON. 6 129 URL
   produit dans le sitemap FR, mais une URL par coloris : le nombre de modèles réels, le nombre de
   variantes et le catalogue complet ne sont **pas établis**. Ses prix sont lus dans le HTML de
   7 pages, donc **partiels par construction** : ils décrivent les pages de portefeuilles,
   porte-cartes, porte-monnaie et petite maroquinerie, pas tout le catalogue.
2. **PaulMarius : arborescence partielle.** 600 URL de catégorie relevées, mais **je n'ai pas
   départagé menu et orphelines** faute d'un équivalent de `collections.json`. Les 78,2 % de trafic
   sur des pages de catégorie sont mesurés ; leur position dans la navigation n'est pas établie.
3. **« Menu » veut dire « lié depuis le HTML de l'accueil ».** Je n'ai pas lu les objets `linklist`
   de Shopify. Une collection présente dans un menu de deuxième niveau non rendu sur l'accueil est
   comptée orpheline à tort. Le chiffre d'orphelines est donc un **majorant**.
4. **Plancher de lecture DataForSEO.** 1 000 lignes lues par domaine, triées par ETV décroissant, sur
   des totaux de 1 331 à 4 948 mots-clés. Couverture de l'ETV total : Hexagona 100 %, Nat & Nin
   100 %, Arthur & Aston 98 %, PaulMarius 96 %, **Le Tanneur 92 %** — soit 34 930 ETV non lus chez
   lui, répartis sur la traîne. Les parts par axe sont calculées sur le lu, pas sur le total.
5. **L'ETV n'est pas du trafic.** C'est une estimation de modèle. Aucune visite réelle n'a été
   consultée. **SimilarWeb n'a pas été interrogé, donc la règle « trafic réel ≈ SimilarWeb × 3 » n'a
   pas pu être appliquée.** Les comparaisons de ce dossier sont des comparaisons d'estimations entre
   domaines mesurés le même jour avec le même endpoint — c'est leur seule valeur, et elle suffit
   pour classer des axes, pas pour prévoir un chiffre d'affaires.
6. **Aucune donnée publicitaire.** Ni annonces texte confirmées, ni ancienneté d'achat, ni budget.
   Qui achète `portefeuille homme` en Ads, et depuis quand, reste **non établi**.
7. **Aucune entreprise vérifiée.** Pas de SIREN, pas de bilan, pas de date d'immatriculation
   consultée. Les cinq types de la section 3 sont des **jugements appuyés sur des signaux de
   catalogue et de site**, comme la méthode l'exige d'écrire.
8. **`products_count` de Shopify inexploitable chez Le Tanneur** : 2 872 annoncés pour la collection
   Femme, 233 réellement servis, 495 fiches sur tout le site. Je n'ai pas utilisé ce champ pour les
   comptages ; les nombres de fiches par famille viennent de `/collections/<handle>/products.json`.
9. **Arthur & Aston : 250 collections exactement.** Nombre rond confirmé par deux sources
   (`collections.json` et sitemap), mais je ne peux pas exclure un plafond de plateforme à 250. À
   revérifier si ce chiffre devait servir à une décision.
10. **Ce qui est derrière une inscription n'a pas été ouvert** : paliers du programme de fidélité
    Nat & Nin, contenu du Club Hexagona, montants exacts des points Hexagona. **Aucun compte créé,
    aucune newsletter souscrite, aucun formulaire envoyé.** Ces éléments sont non établis.
11. **Les avis** : Judge.me détecté chez Nat & Nin et Hexagona ; **aucun provider identifié chez Le
    Tanneur et Arthur & Aston**, dont les mentions « avis clients » n'ont pas pu être rattachées à
    un tiers. Le 4,8/5 sur 3 240 avis d'Hexagona est un compteur d'application installée par le
    marchand : ni un compteur maison, ni une certification d'organisme.
12. **Aucun texte concurrent n'est reproduit dans ce dossier.** Les citations sont réduites à des
    fragments d'identification (seuils, durées, noms de normes, intitulés de collection) nécessaires
    à la vérifiabilité. Aucune instruction adressée à un agent n'a été rencontrée dans les pages
    lues ; si elle l'avait été, elle aurait été citée et signalée, jamais suivie.

---

*Rédigé par l'agent `cartographie-concurrence`. Étape 7 sur 8. Ne rend aucun verdict de marché :
les seuils et la décision `GO` / `STOP` appartiennent à Hakim, et le coût rendu du sourcing manque
toujours.*

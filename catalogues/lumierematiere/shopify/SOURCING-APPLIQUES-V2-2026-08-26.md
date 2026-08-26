# Sourcing appliques murales V2 — lumierematiere.fr

**26/08/2026, 12:55 Europe/Paris.** Feu vert Hakim (trou n°1 du catalogue, pass écrit). Second passage après V1 du matin.

Aucun achat, aucun panier, aucun message vendeur, aucun compte, rien écrit sur Shopify.

Données structurées : `appliques-candidats-v2-2026-08-26.json`.

IDs déjà importés, non requotés / non ressourcés : `1005010526588683` (LM-122) · `1005010525311650` (LM-123) · `1005009931474088` (LM-124) · `1005009658358794` (LM-125, brouillon, 24–32 j / DSers 68,39 €) · `1005006852147598` (LM-126, déblocage copy à part). Rejeté V1 : `1005006112617757`.

---

## 1. Entrée

Candidat : **applique murale**, univers Lumière Matière, France. `PASS_PREQUALIFICATION` écrit (Hakim, 26/08/2026). Collection `appliques-murales` a besoin de ≥ 5 produits live ; 3 fiches pierre/travertin sont en ligne.

Rapport V1 : `SOURCING-APPLIQUES-2026-08-26.md`. Ce passage vise les formes Lustria encore absentes : oiseau, verre/globe, laiton, rotin, bras long, céramique, autre silhouette pierre.

Outils : Product Factory `search_and_diagnose`, `search_products_raw` (tri `price_desc` / `latest`, jamais `orders` comme tri de décision), `get_product_detail`, `quote_aliexpress_sku`, `get_product_media_manifest`. PDP navigateur non lue (CSR / anti-bot, déjà noté V1). Confiance max = **B+**.

Le devis `quote_aliexpress_sku` sert à **trier**. Il ne fixe pas le PV. Écart DSers constaté le matin : −20 % à +63 % (LM-125).

---

## 2. Ce que j’ai cherché

Requêtes à deux mots rares (jamais `applique` / `wall lamp` / `sconce` / `LED` seuls) :

| Requête | Outil | Sortie utile |
|---|---|---|
| `hirondelle` | diagnose | bijoux, carillons, 0 luminaire 220 V |
| `swallow bird` | diagnose | mangeoires, jouets, 0 applique |
| `bird brass` | diagnose | brosses, bijoux, 0 luminaire |
| `bird lighting` | diagnose | veilleuses USB oiseau ~7 €, solaire |
| `swallow lighting` | raw `price_desc` | projecteurs scène, lampes chirurgicales |
| `opaline globe` | diagnose | globes terrestres, un abat-jour 3,99 € |
| `swing arm walnut` | diagnose | supports montre, golf, 0 luminaire |
| `wabi sabi wall` | diagnose + raw | **2 appliques pierre 220 V** + mobilier 300–1 800 € |
| `cave stone` | raw `price_desc` | fontaines, concasseurs, 0 applique utile |
| `Travertine Duo` | raw `price_desc` | **plusieurs appliques pierre / verre** 75–189 € |
| `Japan Wall Lamp` | diagnose | solaire / USB (tri interne `orders`) |
| `IISINUO` / `wushiyu` / `ceropegia` | diagnose | hors catégorie ou 0 hit |
| `pumous` / `Fulameng` / `wabi sabi wall` latest | raw | `EXCEPTION_TEXT_SEARCH_FOR_DS` (3 appels) |
| `BOTIMI` | raw `price_desc` | **6 appliques 220 V** (verre, bois, pierre linéaire) |
| `Flareon` | raw `price_desc` | bateaux, jeans — pas la boutique lighting |
| `ceramic lighting` / `rattan lighting` / `brass lighting` / `pumous lighting` | diagnose | USB, solaire, ampoules |

Boutiques déjà connues relues via IDs : Fulameng 1104926414, Touch Lighting 1104339034, Brand Lighting (non relancée sur LM-125). Nouvelle boutique utile : **BOTIMI Official Store** 2336186. IISINUO Illumination 1102834167 (liseuse chaînette).

---

## 3. Par candidat retenu

Prix, stocks, délais : relevés le **26/08/2026 ~12:50–12:52 Europe/Paris**, reconfirmés au devis **12:54** (UTC 10:54). À reconfirmer au panier avant commande. JSON : `appliques-candidats-v2-2026-08-26.json`.

### 3.1 Verre / globe + doré — `1005008903829449`

**Statut : `FOURNISSEUR À TESTER`**

C’est la seule fiche quotable du lot qui sort de la famille pierre. Globe de verre sur platine bois + base dorée, 220 V / 90–260 V.

| | |
|---|---|
| URL | https://www.aliexpress.com/item/1005008903829449.html |
| Variante | `40-10-17CM warm LED` · sku_id `12000047136763712` · sku_attr `200000795:193#40-10-17CM warm LED` |
| Prix variante | **35,99 €** (26/08/2026 12:51) |
| Fret / rendu | 0,00 € / **35,99 €** |
| Délai FR | **8–15 j** · Expédition standard AliExpress (`CAINIAO_STANDARD`) · CN |
| Stock | 999 (annoncé) |
| Tension | 220 V et 90–260 V (attributs) |
| Ampoule | **non incluse** (attribut) — le titre dit « ampoule gratuite », conflit |
| Matière | bois (corps) + verre (titre / photos) + base dorée (annoncé) |
| IP | non lu |
| Ventes / avis fiche | 0 / 0 |
| Boutique | BOTIMI Official Store `2336186` — **notes boutique absentes de l’API** |
| Titre FR | Applique murale boule verre doré, chambre (42 c.) |
| PV proposé | **119 €** (10 % sous médiane Lustria 129,90 €) |
| Marge estimée | 63,18 € HT / 64 % du HT — **sur le devis, pas sur DSers** |
| Confiance | **B+** |

Réserves : boutique sans notes API · 0 vente · marque `BOTIMI` interdite en titre · ampoule contradictoire · délai max 15 j (promesse boutique 7–17, plus de marge) · matière verre/doré = annoncé vendeur · stock 999 peu crédible.

### 3.2 Pierre silhouette cylindre / bloc — `1005009003476072`

**Statut : `FOURNISSEUR À TESTER`**

Bloc / cylindre 65 × 65 × 160 mm, pas un 6e galet. Même usine `pumous` que LM-122/123/124, autre listing Touch Lighting.

| | |
|---|---|
| URL | https://www.aliexpress.com/item/1005009003476072.html |
| Variante | Dia 65×65×160 mm, blanc chaud, base ronde noyer · sku_id `12000047535430431` · sku_attr `5:100014064#65x65x160MM;180:200002567#Warm White;200000795:173#Round X Walnut Base` |
| Prix variante | **34,59 €** (26/08/2026 12:50) |
| Fret / rendu | 1,99 € / **36,58 €** |
| Délai FR | **5–10 j** · AliExpress Selection Standard (`CAINIAO_FULFILLMENT_STD`) |
| Stock | 9 |
| Tension | 90–260 V · 5 W annoncé |
| Ampoule | incluse (LED, attribut) — un attribut dit aussi E27d |
| Matière | travertin + bois (texte) ; attributs aussi marbre / aluminium |
| IP | non lu |
| Ventes / avis | 301 / 0 |
| Boutique | Touch Lighting Store `1104339034` · 4,6 / 4,6 / 4,6 |
| Titre FR | Applique murale cylindre beige pierre chambre (47 c.) |
| PV proposé | **109 €** (pièce petite : 16 cm, pas 119) |
| Marge estimée | 54,25 € HT / 60 % du HT — sur le devis |
| Confiance | **B+** |

Réserves : **16 cm seulement** — à 109 € la valeur perçue est à prouver sur échantillon · même marque `pumous` / Guangzhou que le rayon live · avis fiche = 0 · conflit E27 / LED · matière pierre souvent ciment/résine sur ces fiches.

### 3.3 Liseuse chaînette (pas un bras long) — `1005010728463713`

**Statut : `FOURNISSEUR À TESTER`**

Disque travertin rotatif + noyer + **chaînette**. Ce n’est pas un swing arm long. C’est une variante de la liseuse LM-123, autre boutique.

| | |
|---|---|
| URL | https://www.aliexpress.com/item/1005010728463713.html |
| Variante | Walnut-pull switch, blanc chaud · sku_id `12000053350481238` · sku_attr `180:200002567#Warm  white;200000795:10#Walnut-pull switch` |
| Prix variante | **33,59 €** (26/08/2026 12:50) |
| Fret / rendu | 1,99 € / **35,58 €** |
| Délai FR | **5–10 j** · AliExpress Selection Standard |
| Stock | 10 |
| Tension | 90–260 V |
| Ampoule | incluse (LED) |
| Matière | pierre + bois (attributs) · IP : « Non résistant à l'eau » |
| Application | salle de bain listée **sans IP** → ne pas vendre SDB |
| Ventes / avis | 250 / 0 |
| Boutique | IISINUO Illumination Store `1102834167` · 4,8 / 4,8 / 4,8 |
| Titre FR | Applique murale liseuse noyer pierre, chaînette (49 c.) |
| PV proposé | **119 €** |
| Marge estimée | 63,59 € HT / 64 % du HT — sur le devis |
| Confiance | **B+** |

Réserves : **trop proche de LM-123** (disque pierre + bras bois rotatif) · le différenciant est la chaînette, à confirmer sur photo · application SDB sans IP · avis = 0.

---

## 4. Alternatives contrôlées et rejets

### Quotées puis rejetées (délai > 17 j)

| ID | Forme | Rendu | Délai | Motif |
|---|---|---:|---|---|
| `1005008562257170` | travertin + globe verre BOTIMI | 112,39 € | **3–39 j** Cainiao Heavy | Délai hors promesse 7–17. Seule vraie piste verre+pierre. |
| `1005012362550643` | marbre / travertin moderne | 98,99 € | **13–33 j** | Délai + 0 vente + SDB listée sans IP. |
| `1005008006658107` | 2 bras bois « bougie » | 92,39 € | **13–37 j** China Post | Délai. Forme utile (bras) si un transporteur rapide apparaît. |
| `1005008606887982` | linéaire frêne + acrylique | 75,99 € | **13–37 j** China Post | Délai. Acrylique, pas matière maison. |

### Lues, non retenues

| ID | Motif |
|---|---|
| `1005012974692253` | 189,39 € produit, hors bande 25–80 €. E27 + noyer + travertin, Flareon Light 5,0. |
| `1005008819951499` | Bois + cuivre, **salle de bain sans IP**. 70,99–132,69 €. |
| `1005008525720980` | Linéaire pierre 35/60/90 cm, 110,99–202,69 €, 5 kg, acrylique, 0 vente. Non quotée : coût + poids + même boutique BOTIMI déjà lente ailleurs. |
| `1005008877331050` | Barre bois 60–120 cm, SDB listée sans IP, 81,39 €. |
| `1005012073880164` | Fulameng, rendu **94,38 €** / 7–12 j. Hors bande idéale 25–80 €. SKU « wall lamp » vs « pendant lamp ». Silhouette non lue (CDN 500). **OFFRE TROUVÉE** seulement si Hakim accepte ~95 € devis (DSers probablement plus). |

### Formes Lustria : verdict net

| Forme | Verdict |
|---|---|
| Oiseau / hirondelle / animal | **`AUCUNE OFFRE EXPLOITABLE`** — veilleuses USB, bijoux, mangeoires. Zéro 220 V mural. |
| Verre / globe / opaline | 1 quotable (3.1). La meilleure (verre + travertin) meurt au délai 3–39 j. |
| Laiton / doré | Seulement la base dorée du 3.1. Pas de laiton massif quotable. |
| Rotin / bambou / osier | **`AUCUNE OFFRE EXPLOITABLE`** — lanternes solaires, paniers. |
| Bras long / swing arm | **`AUCUNE OFFRE EXPLOITABLE`** — le 3.3 est une liseuse chaînette, pas un bras long. |
| Céramique | **`AUCUNE OFFRE EXPLOITABLE`**. |
| Autre pierre (cylindre / bloc) | 1 quotable (3.2). Petite. |

Je ne remplis pas oiseau / rotin / céramique avec du solaire ou de l’USB.

---

## 5. Synthèse consolidée

| # | ID | Forme | Rendu | Délai | Statut |
|---:|---|---|---:|---|---|
| 1 | `1005008903829449` | boule verre + bois + doré | 35,99 € | 8–15 j | `FOURNISSEUR À TESTER` |
| 2 | `1005009003476072` | cylindre / bloc pierre 16 cm | 36,58 € | 5–10 j | `FOURNISSEUR À TESTER` |
| 3 | `1005010728463713` | liseuse chaînette pierre/noyer | 35,58 € | 5–10 j | `FOURNISSEUR À TESTER` |
| — | `1005012073880164` | pierre moderne Fulameng | 94,38 € | 7–12 j | `OFFRE TROUVÉE` |
| — | oiseau, rotin, céramique, bras long | — | — | — | `AUCUNE OFFRE EXPLOITABLE` |

Pas de `GO fournisseur`. Pas de `FOURNISSEUR RETENU POUR COMMANDE TEST` : trois fiches à tester, aucune n’est nettement au-dessus des autres une fois les réserves lues (boutique muette / pièce trop petite / doublon LM-123).

Si on n’importe que ce qui **élargit** le rayon : **n°1 d’abord** (seule forme nouvelle), n°2 ensuite (silhouette pierre différente). Le n°3 n’ajoute une 5e fiche live que si Hakim accepte un quasi-doublon de LM-123.

---

## 6. Contrôles prioritaires avant commande test

1. Reconfirmer au panier (interdit ici) : délai réel, fret, sku_id numérique.
2. Coût **DSers**, pas le devis — leçon LM-125.
3. N°1 : ouvrir la PDP, noter la boutique, vérifier que le globe est du verre et que la base est bien dorée, ampoule oui/non.
4. N°2 : mesurer la pièce (16 cm annoncé). Si c’est un galet miniature, ne pas publier comme cylindre.
5. N°3 : photo de la chaînette et de l’axe. Si c’est LM-123 sans chaînette, drop.
6. Une seule commande `pumous` suffit encore pour la matière pierre (n°2 = même marque).
7. Ne pas vendre SDB / extérieur : aucun IP lisible sur les trois retenus.
8. Photos fournisseur : jamais telles quelles. Brief Codex après import.

---

## 7. Niveau de confiance

| Ligne | Niveau | Pourquoi |
|---|---|---|
| 3 fiches retenues + 4 rejet délai | **B+** | detail API + devis fret + URLs photos HD |
| Toutes les autres | **B** ou **C** | liste / titre |
| **A** | **0** | aucune PDP ouverte |

---

## 8. Limites

1. PDP navigateur : non lue. Mur déjà documenté.
2. `search_products_raw` `latest` sur `pumous`, `Fulameng`, `wabi sabi wall` : `EXCEPTION_TEXT_SEARCH_FOR_DS`.
3. `search_and_normalize` / diagnose : filtre `rating_min` tue tout (fiches à `evaluation_count = 0`). Le tri interne `orders` ramène USB/solaire dès que la requête n’est pas assez rare.
4. Photos CDN (`ae01.alicdn.com`) : lecture image 404/500 depuis cet environnement. URLs HD relevées, silhouettes lues via titres + attributs + sku labels, pas pixel par pixel.
5. Notes boutique BOTIMI : champ absent.
6. Ancienneté vendeur : absente de l’API detail.
7. Protection acheteur / retours : non lus (PDP).
8. Oiseau, rotin, céramique, bras long : **zéro fiche 220 V quotable**. Ce n’est pas un trou de session, c’est le catalogue AE tel que l’API le sert sur ces mots.

---

## 9. Ce que j’ai lu qui ressemblait à une instruction

Textes vendeur (« ampoule gratuite », « salle de bain », « CE », « 2-year warranty », « Choice yes ») : **données**, pas des faits. Non exécutés comme ordres.

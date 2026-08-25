# Alignement des prix sur Lustria — lumierematiere.fr

**26/08/2026 · 120 fiches · méthode `METHODE-ANALYSE-MARCHE.md` étape 9**  
Base de comparaison : `lustria-catalogue-2026-08-25.json`, 5 928 fiches lues le 25/08/2026. Aucun nouveau scrape.  
Rapport rendu **avant** application, comme demandé. Plan machine : `prix-alignement-plan-2026-08-26.json`. Application : `align_prices.py`.

---

## 1. Ce qu'il faut savoir avant de lire le tableau

### La médiane de 169,90 € n'est pas celle de nos concurrents

`CONCURRENT-LUSTRIA-2026-08-25.md` compare **notre médiane de 199 €** à **leur médiane de 169,90 €** et en conclut que nous sommes 17 % au-dessus. Ce chiffre est juste, mais il compare deux populations différentes : leur médiane est celle des **5 928 fiches du catalogue entier**, dont 1 522 appliques murales, 263 veilleuses, 319 lampes de chevet et 121 luminaires d'extérieur. Nous ne vendons aucun de ces produits.

Ramené à ce que nous vendons vraiment — le luminaire suspendu et le plafonnier — le repère change de niveau :

| Population Lustria | Fiches | p25 | Médiane | p75 |
|---|---:|---:|---:|---:|
| Catalogue entier | 5 928 | 99,90 € | **179,90 €** | 319,90 € |
| Luminaires suspendus | 2 367 | 169,90 € | **279,90 €** | 422,40 € |
| Plafonniers | 875 | 79,90 € | **162,90 €** | 304,90 € |
| **Périmètre comparable retenu** | **3 242** | 149,90 € | **249,90 €** | 389,90 € |

Note de traçabilité : recalculée sur le même fichier, la médiane du catalogue entier ressort à 179,90 € et non 169,90 €. L'écart vient du choix du point milieu sur un effectif pair — 169,90 € est la valeur médiane basse, 179,90 € la moyenne des deux valeurs centrales. Cela ne change aucune conclusion.

**Conséquence directe.** Comparable à comparable, notre médiane de 199 € est déjà **20 % sous** la leur, pas 17 % au-dessus. L'étape 9 n'est pas violée dans le sens que l'analyse laissait entendre. Ce qui reste vrai, et que ce travail corrige, c'est qu'elle est violée **par famille** : sur la céramique, le bambou, le tissu et le plafonnier bois, ils sont moins chers que nous.

### Le mandat mécanique aurait été une hausse de prix sur la moitié du catalogue

Appliquée à la lettre, la règle « médiane du comparable × 0,90 » remonte le prix de **66 fiches sur 117**, pour **+6 060 € TTC** cumulés. La plus forte : `LM-066` (Suspension LED goutte dorée, 1 ou 2 lumières) passerait de 199 € à 449 €, la médiane de ses 10 comparables étant à 494,90 €.

**Ces hausses ne sont pas appliquées.** Le mandat est de se placer *sous* Lustria, le jeu de décisions demandé est baisse / inchangé / bloqué par la marge, et rien n'autorise une hausse. Ces lignes sortent en « inchangé — déjà sous la cible », avec le montant laissé de côté chiffré ci-dessus. **C'est un arbitrage, pas un calcul : à trancher.**

## 2. Méthode

### Terminaison retenue : euro entier terminant par 9, grille au pas de 10 €

Nos 120 fiches finissent déjà toutes par 9 sans centimes ; Lustria finit par `,90`. **On garde le 9 en euro entier** et on ne change qu'une chose : le pas de la grille passe de 50 € (149 / 199 / 249 / 299 / 349 / 399 / 499) à 10 € (…129, 139, 149, 159…). Trois raisons :

1. **Un pas de 50 € rend l'exercice impossible.** Une cible calculée à 166 € ne peut atterrir que sur 149 €, en donnant 17 € de marge pour rien, ou sur 199 €, au-dessus du comparable. Le pas de 10 € est le plus grossier qui permette encore de viser −10 % à moins de 5 € près.
2. **`,90` est la terminaison de celui qu'on sous-cote.** Sans prix barré ni promotion, l'euro entier se lit comme un prix posé et non comme une remise ; c'est aussi ce qui nous distingue d'eux à l'affichage en Shopping.
3. **169 € bat 169,90 € pour 0,90 € de marge.** À affichage égal en comparateur, le nombre entier est perçu plus bas.

Arrondi **au plus proche**, pas vers le bas. La remise réellement obtenue sur les 38 baisses va donc de **7,8 % à 11,9 %** (médiane 9,1 %) au lieu de 10 % pile. Garantir −10 % strict imposerait de descendre d'un cran de plus sur **28 des 38 lignes**, pour **233,33 € HT** de marge unitaire, et sortirait tout le bambou de son palier à 199 €. Hakim préférant une marge tenue à un alignement mécanique, on garde l'arrondi au plus proche.

### Les quatre axes d'appariement, et ce qui est réellement mesurable

| Axe | Chez nous | Chez Lustria | Verdict |
|---|---|---|---|
| **Type** | premier mot du titre (suspension / lustre / plafonnier) | champ `type` publié | **fiable des deux côtés**, axe obligatoire |
| **Matière** | titre, puis fiche fournisseur en second recours | handle descriptif + tags | **fiable** — nommée sur 109/120 de nos fiches, 2 183/3 242 des leurs |
| **Classe de taille** | option `Diamètre` (Ø en cm) sur 61/120 fiches | **absente** — 0 handle sur 5 928 porte un « cm » | **non mesurable chez eux** : remplacée par la forme, lisible sur 1 050/3 242 de leurs fiches |
| **Nombre de lumières** | options (`4 lumières`, `6 anneaux`…) | **quasi absent** — 4 handles sur 5 928 | **partiellement mesurable** : réduit à mono / multi |

La classe de taille est le point faible et il faut le dire net : **Lustria ne publie aucune dimension dans les données dont nous disposons.** Elle est remplacée par la **forme** (anneau · linéaire · composition multi · globe · dôme), lisible des deux côtés dans les libellés, et qui porte l'essentiel de l'effet-taille sur le prix — un lustre à anneaux n'est pas un dôme, quelle que soit sa cote. Le nombre de lumières est réduit à mono contre multi, seule granularité que leurs libellés permettent.

### Pièges neutralisés

- **Comparer des suspensions à des suspensions.** Appliques, veilleuses, lampes de chevet et de table, lampadaires, extérieur : écartés par type. 5 928 fiches en entrée, **3 242 retenues** comme comparables possibles.
- **Leur champ `type` est parfois faux.** Des appliques murales sont typées `Luminaire Plafonnier` chez eux. Un garde-fou sur le handle écarte ces fiches malgré leur type.
- **Notre collection n'est pas notre matière.** `Suspension céramique festonnée blanche, tête bois` est rangée dans *Suspensions bois* et `Suspension papier ou soie` dans *Suspensions métal*. La matière est lue dans le **titre**, jamais dans la collection.
- **Le métal en dernier.** Presque toute monture en contient : il n'est retenu comme matière dominante qu'à défaut d'une matière d'abat-jour nommée.
- **Une médiane sur 3 fiches ne vaut rien.** Le critère le plus fin qui porte au moins 8 comparables est retenu ; on ne relâche un axe que sous ce seuil, et jamais en dessous de 3 fiches. Sous 3, la ligne sort en « aucun comparable » et son prix ne bouge pas.

### Plancher de marge

Coût DSers unitaire + 2 € de fret, base HT (TVA 20 %, HT = TTC / 1,2), marge exigée **≥ max(40 € HT ; 25 % du HT)** — les deux conditions ensemble, lecture prudente du « ou ». Aucun prix cible ne descend sous ce plancher ; le cas échéant on garde le prix actuel.

Deux réserves sur la donnée de coût. La colonne `cost_proxy_ae` du `catalogue-dsers.csv` est un **proxy** : sur la plupart des fiches elle vaut le prix AliExpress de la variante d'entrée, mais sur les lustres à pampilles multi-tailles (LM-070, LM-071) elle est proche de la **médiane** des variantes, donc très au-dessus du palier de base. Et la marge est calculée au **palier d'entrée** de chaque fiche, le plus mince : c'est le contrôle conservateur. Les frais de paiement (≈ 1,4 % + 0,25 €) évoqués à l'étape 9 ne sont pas déduits, la règle du brief ne les mentionnant pas — ils coûteraient environ 3 € HT par vente.

## 3. Les 120 lignes

`Prix` et `cible` en TTC. `Marge` = marge HT au palier d'entrée, en euros puis en % du HT. `n` = nombre de comparables Lustria dans le pool ; la colonne *comparable* donne le handle dont le prix est le plus proche de la médiane du pool, et **la médiane du pool** est ce qui sert au calcul. `≈` marque un appariement approximatif.

| SKU | Handle | Prix | Comparable Lustria retenu | Son prix | Médiane pool | n | Cible | Marge avant | Marge après | Décision |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| LM-001 | `suspension-bambou-104055` | 249 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 160,31 € · 77 % | 118,64 € · 72 % | baisse |
| LM-002 | `suspension-bambou-317565` | 249 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 160,31 € · 77 % | 118,64 € · 72 % | baisse |
| LM-003 | `suspension-bambou-942503` | 199 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 119,04 € · 72 % | 119,04 € · 72 % | inchangé — déjà sous la cible |
| LM-004 | `suspension-bambou-dore-60cm-805884` | 199 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 119,24 € · 72 % | 119,24 € · 72 % | inchangé — déjà sous la cible |
| LM-005 | `suspension-bambou-led-033589` | 249 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 43 | 199 € | 159,62 € · 77 % | 117,95 € · 71 % | baisse |
| LM-006 | `suspension-bambou-45cm-962644` | 199 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 120,24 € · 72 % | 120,24 € · 72 % | inchangé — déjà sous la cible |
| LM-007 | `suspension-bambou-655008` | 249 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 156,91 € · 76 % | 115,24 € · 70 % | baisse |
| LM-008 | `suspension-bambou-067987` | 199 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 124,04 € · 75 % | 124,04 € · 75 % | inchangé — déjà sous la cible |
| LM-009 | `suspension-bambou-led-80-cm-191307` | 199 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 127,24 € · 77 % | 127,24 € · 77 % | inchangé — déjà sous la cible |
| LM-010 | `suspension-bambou-led-136557` | 199 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 128,13 € · 77 % | 128,13 € · 77 % | inchangé — déjà sous la cible |
| LM-011 | `suspension-bambou-655463` | 249 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 150,51 € · 72 % | 108,84 € · 66 % | baisse |
| LM-012 | `suspension-bambou-led-80-cm-236157` | 199 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 129,84 € · 78 % | 129,84 € · 78 % | inchangé — déjà sous la cible |
| LM-013 | `suspension-bambou-280004` | 249 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 43 | 199 € | 149,11 € · 72 % | 107,44 € · 65 % | baisse |
| LM-014 | `suspension-bambou-led-630923` | 249 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 149,11 € · 72 % | 107,44 € · 65 % | baisse |
| LM-015 | `suspension-bambou-led-583180` | 249 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 148,59 € · 72 % | 106,92 € · 64 % | baisse |
| LM-016 | `suspension-bambou-led-50cm-377816` | 199 € | suspension-fleur-en-bambou-tresse-pour-ambian… | 219,90 € | 219,90 € | 41 | 199 € | 133,44 € · 80 % | 133,44 € · 80 % | inchangé — déjà sous la cible |
| LM-017 | `suspension-rotin-605780` | 199 € | suspension-en-rotin-naturel-cylindrique-desig… | 239,90 € | 239,90 € | 27 | 219 € | 121,04 € · 73 % | 121,04 € · 73 % | inchangé — déjà sous la cible |
| LM-018 | `suspension-rotin-led-761433` | 199 € | luminaire-noir-et-blanc-en-rotin-design-ecolo… | 259,90 € | 259,90 € | 132 | 229 € | 121,84 € · 74 % | 121,84 € · 74 % | inchangé — déjà sous la cible |
| LM-019 | `suspension-rotin-443915` | 249 € | suspension-en-rotin-naturel-cylindrique-desig… | 239,90 € | 239,90 € | 27 | 219 € | 151,51 € · 73 % | 126,51 € · 69 % | baisse |
| LM-020 | `suspension-rotin-897170` | 249 € | luminaire-noir-et-blanc-en-rotin-design-ecolo… | 259,90 € | 259,90 € | 132 | 229 € | 151,11 € · 73 % | 134,44 € · 70 % | baisse |
| LM-021 | `suspension-rotin-led-420069` | 199 € | suspension-en-rotin-naturel-cylindrique-desig… | 239,90 € | 239,90 € | 27 | 219 € | 131,64 € · 79 % | 131,64 € · 79 % | inchangé — déjà sous la cible |
| LM-022 | `suspension-rotin-dore-435189` | 199 € | suspension-en-rotin-naturel-cylindrique-desig… | 239,90 € | 239,90 € | 27 | 219 € | 134,24 € · 81 % | 134,24 € · 81 % | inchangé — déjà sous la cible |
| LM-023 | `suspension-rotin-469688` | 249 € | luminaire-noir-et-blanc-en-rotin-design-ecolo… | 259,90 € | 259,90 € | 132 | 229 € | 143,51 € · 69 % | 126,84 € · 66 % | baisse |
| LM-024 | `suspension-rotin-623305` | 199 € | suspension-en-rotin-naturel-cylindrique-desig… | 239,90 € | 239,90 € | 27 | 219 € | 135,84 € · 82 % | 135,84 € · 82 % | inchangé — déjà sous la cible |
| LM-025 | `suspension-rotin-489600` | 249 € | suspension-luminaire-design-en-rotin-naturel-… | 269,90 € | 269,90 € | 127 | 239 € | 142,11 € · 68 % | 133,78 € · 67 % | baisse |
| LM-026 | `suspension-rotin-dore-865596` | 249 € | suspension-design-doree-vagues-luminaire-led-… | 419,90 € | 419,90 € | 8 | 379 € | 141,51 € · 68 % | 141,51 € · 68 % | inchangé — déjà sous la cible |
| LM-027 | `suspension-rotin-607504` | 249 € | suspension-luminaire-design-en-rotin-naturel-… | 269,90 € | 269,90 € | 127 | 239 € | 140,11 € · 68 % | 131,78 € · 66 % | baisse |
| LM-028 | `suspension-rotin-272937` | 199 € | suspension-luminaire-panda-suspendu-a-une-cor… | 299,90 € | 284,90 € | 10 | 259 € | 142,84 € · 86 % | 142,84 € · 86 % | inchangé — déjà sous la cible |
| LM-029 | `suspension-rotin-led-535545` | 249 € | suspension-luminaire-design-en-rotin-naturel-… | 269,90 € | 269,90 € | 127 | 239 € | 136,11 € · 66 % | 127,78 € · 64 % | baisse |
| LM-030 | `suspension-rotin-477244` | 249 € | suspension-en-rotin-naturel-cylindrique-desig… | 239,90 € | 239,90 € | 27 | 219 € | 136,04 € · 66 % | 111,04 € · 61 % | baisse |
| LM-031 | `suspension-bois-led-121862` | 249 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 160,11 € · 77 % | 93,44 € · 66 % | baisse |
| LM-032 | `suspension-bois-led-934110` | 249 € | suspension-luminaire-travertin-en-pierre-avec… | 249,90 € | 249,90 € | 14 | 229 € | 159,91 € · 77 % | 143,24 € · 75 % | baisse |
| LM-033 | `suspension-bois-led-334133` | 249 € | suspension-design-en-laiton-et-pierre-terrazz… | 289,90 € | 289,90 € | 93 | 259 € | 159,51 € · 77 % | 159,51 € · 77 % | inchangé — déjà sous la cible |
| LM-034 | `suspension-bois-059364` | 199 € | suspension-luminaire-en-bois-et-metal-dore-av… | 219,90 € | 219,90 € | 15 | 199 € | 119,84 € · 72 % | 119,84 € · 72 % | inchangé — déjà sous la cible |
| LM-035 | `suspension-bois-led-30cm-886635` | 249 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 159,11 € · 77 % | 92,44 € · 66 % | baisse |
| LM-036 | `suspension-bois-led-989306` | 249 € | suspension-bois-flotte | 299,90 € | 298,90 € | 140 | 269 € | 159,08 € · 77 % | 159,08 € · 77 % | inchangé — déjà sous la cible |
| LM-037 | `suspension-bois-led-582321` | 199 € | suspension-luminaire-design-en-rotin-naturel-… | 269,90 € | 269,90 € | 127 | 239 € | 120,51 € · 73 % | 120,51 € · 73 % | inchangé — déjà sous la cible |
| LM-038 | `suspension-bois-led-830581` | 199 € | suspension-bois-flotte | 299,90 € | 298,90 € | 140 | 269 € | 122,04 € · 74 % | 122,04 € · 74 % | inchangé — déjà sous la cible |
| LM-039 | `suspension-bois-193329` | 199 € | suspension-luminaire-travertin-en-pierre-avec… | 249,90 € | 249,90 € | 14 | 229 € | 122,64 € · 74 % | 122,64 € · 74 % | inchangé — déjà sous la cible |
| LM-040 | `suspension-bois-832012` | 199 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 124,84 € · 75 % | 124,84 € · 75 % | inchangé — déjà sous la cible |
| LM-041 | `suspension-bois-led-453740` | 199 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 125,18 € · 76 % | 125,18 € · 76 % | inchangé — déjà sous la cible |
| LM-042 | `suspension-bois-led-245113` | 249 € | suspension-luminaire-travertin-en-pierre-avec… | 249,90 € | 249,90 € | 14 | 229 € | 154,11 € · 74 % | 137,44 € · 72 % | baisse |
| LM-043 | `suspension-effet-pierre-led-338324` | 199 € | suspension-luminaire-travertin-en-pierre-avec… | 249,90 € | 249,90 € | 14 | 229 € | 119,04 € · 72 % | 119,04 € · 72 % | inchangé — déjà sous la cible |
| LM-044 | `suspension-effet-pierre-led-434888` | 249 € | suspension-design-en-laiton-et-pierre-terrazz… | 289,90 € | 284,90 € | 88 | 259 € | 159,51 € · 77 % | 159,51 € · 77 % | inchangé — déjà sous la cible |
| LM-046 | `suspension-effet-pierre-092465` | 199 € | suspension-design-en-laiton-et-pierre-terrazz… | 289,90 € | 284,90 € | 88 | 259 € | 121,04 € · 73 % | 121,04 € · 73 % | inchangé — déjà sous la cible |
| LM-047 | `suspension-effet-pierre-343987` | 199 € | suspension-luminaire-travertin-en-pierre-avec… | 249,90 € | 249,90 € | 14 | 229 € | 121,62 € · 73 % | 121,62 € · 73 % | inchangé — déjà sous la cible |
| LM-048 | `suspension-effet-pierre-led-dore-960013` | 249 € | suspension-design-en-laiton-et-pierre-terrazz… | 289,90 € | 284,90 € | 88 | 259 € | 157,54 € · 76 % | 157,54 € · 76 % | inchangé — déjà sous la cible |
| LM-049 | `suspension-effet-pierre-led-445794` | 199 € | suspension-luminaire-travertin-en-pierre-avec… | 249,90 € | 249,90 € | 14 | 229 € | 121,84 € · 74 % | 121,84 € · 74 % | inchangé — déjà sous la cible |
| LM-050 | `suspension-effet-pierre-led-073999` | 199 € | suspension-design-en-laiton-et-pierre-terrazz… | 289,90 € | 284,90 € | 88 | 259 € | 122,24 € · 74 % | 122,24 € · 74 % | inchangé — déjà sous la cible |
| LM-051 | `suspension-effet-pierre-led-147607` | 199 € | suspension-luminaire-travertin-en-pierre-avec… | 249,90 € | 249,90 € | 14 | 229 € | 122,44 € · 74 % | 122,44 € · 74 % | inchangé — déjà sous la cible |
| LM-052 | `suspension-effet-pierre-led-709819` | 199 € | suspension-luminaire-travertin-en-pierre-avec… | 249,90 € | 249,90 € | 14 | 229 € | 123,04 € · 74 % | 123,04 € · 74 % | inchangé — déjà sous la cible |
| LM-053 | `lustre-anneau-led-led-noir-dore-024410` | 199 € | suspension-luminaire-anneaux-led-style-contem… ≈ | 349,90 € | 354,90 € | 34 | 319 € | 119,39 € · 72 % | 119,39 € · 72 % | inchangé — déjà sous la cible |
| LM-054 | `lustre-anneau-led-led-799451` | 199 € | suspension-artistique-a-spirales-led-suspendu… ≈ | 299,90 € | 299,90 € | 67 | 269 € | 119,84 € · 72 % | 119,84 € · 72 % | inchangé — déjà sous la cible |
| LM-055 | `lustre-anneau-led-led-597704` | 199 € | suspension-led-anneau-doree-design-moderne-el… | 329,90 € | 329,90 € | 13 | 299 € | 121,22 € · 73 % | 121,22 € · 73 % | inchangé — déjà sous la cible |
| LM-056 | `lustre-anneau-led-led-717226` | 249 € | luminaire-plafonnier-anneau-beige-au-design-m… ≈ | 444,90 € | 444,90 € | 61 | 399 € | 152,11 € · 73 % | 152,11 € · 73 % | inchangé — déjà sous la cible |
| LM-057 | `lustre-anneau-led-led-625575` | 249 € | plafonnier-decoratif-blanc-style-classique-el… | 219,90 € | 229,90 € | 46 | 209 € | 148,51 € · 72 % | 115,18 € · 66 % | baisse |
| LM-058 | `lustre-anneau-led-led-dore-418494` | 249 € | suspension-led-anneau-doree-design-moderne-el… | 329,90 € | 329,90 € | 13 | 299 € | 148,51 € · 72 % | 148,51 € · 72 % | inchangé — déjà sous la cible |
| LM-059 | `lustre-anneau-led-led-784897` | 199 € | suspension-luminaire-circulaire-en-metal-mini… | 249,90 € | 329,90 € | 10 | 299 € | 130,87 € · 79 % | 130,87 € · 79 % | inchangé — déjà sous la cible |
| LM-060 | `lustre-anneau-led-007557` | 199 € | — | — | — | — | — | 143,64 € · 87 % | 143,64 € · 87 % | inchangé — aucun comparable |
| LM-061 | `lustre-anneau-led-led-134962` | 249 € | plafonnier-led-circulaire-design-moderne-mini… | 179,90 € | 179,90 € | 35 | 159 € | 134,23 € · 65 % | 59,23 € · 45 % | baisse |
| LM-062 | `lustre-anneau-led-led-795468` | 149 € | suspension-artistique-a-spirales-led-suspendu… ≈ | 299,90 € | 299,90 € | 67 | 269 € | 107,68 € · 87 % | 107,68 € · 87 % | inchangé — déjà sous la cible |
| LM-063 | `lustre-anneau-led-led-dore-641905` | 299 € | suspension-luminaire-anneaux-led-style-contem… ≈ | 349,90 € | 354,90 € | 34 | 319 € | 160,18 € · 64 % | 160,18 € · 64 % | inchangé — déjà sous la cible |
| LM-064 | `lustre-anneau-led-led-892612` | 299 € | suspension-vintage-double-anneau-en-verre-pou… | 345,90 € | 345,90 € | 11 | 309 € | 147,25 € · 59 % | 147,25 € · 59 % | inchangé — déjà sous la cible |
| LM-065 | `lustre-cristal-led-led-141724` | 249 € | suspension-baroque-en-cristal-dore-avec-pampi… | 499,90 € | 504,90 € | 16 | 459 € | 145,81 € · 70 % | 145,81 € · 70 % | inchangé — déjà sous la cible |
| LM-066 | `lustre-cristal-led-led-dore-264869` | 199 € | suspension-luminaire-moderne-ovale-avec-boule… | 509,90 € | 494,90 € | 10 | 449 € | 143,51 € · 86 % | 143,51 € · 86 % | inchangé — déjà sous la cible |
| LM-067 | `lustre-cristal-led-677865` | 249 € | suspension-baroque-en-cristal-dore-avec-pampi… | 499,90 € | 504,90 € | 16 | 459 € | 131,11 € · 63 % | 131,11 € · 63 % | inchangé — déjà sous la cible |
| LM-068 | `lustre-cristal-led-led-560904` | 299 € | suspension-baroque-en-cristal-dore-avec-pampi… | 499,90 € | 504,90 € | 16 | 459 € | 161,18 € · 65 % | 161,18 € · 65 % | inchangé — déjà sous la cible |
| LM-069 | `lustre-cristal-led-noir-347688` | 299 € | suspension-luminaire-moderne-ovale-avec-boule… | 509,90 € | 494,90 € | 10 | 449 € | 159,48 € · 64 % | 159,48 € · 64 % | inchangé — déjà sous la cible |
| LM-070 | `lustre-cristal-led-led-dore-841671` | 299 € | suspension-luminaire-moderne-ovale-avec-boule… | 509,90 € | 494,90 € | 10 | 449 € | 106,22 € · 43 % | 106,22 € · 43 % | inchangé — déjà sous la cible |
| LM-071 | `lustre-cristal-led-dore-202521` | 299 € | suspension-luminaire-moderne-ovale-avec-boule… | 509,90 € | 494,90 € | 10 | 449 € | 24,18 € · 10 % | 24,18 € · 10 % | inchangé — déjà sous la cible |
| LM-072 | `suspension-verre-led-dore-436718` | 199 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 120,04 € · 72 % | 120,04 € · 72 % | inchangé — déjà sous la cible |
| LM-073 | `suspension-verre-394147` | 249 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 157,31 € · 76 % | 157,31 € · 76 % | inchangé — déjà sous la cible |
| LM-074 | `suspension-verre-led-489156` | 249 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 156,11 € · 75 % | 156,11 € · 75 % | inchangé — déjà sous la cible |
| LM-075 | `suspension-verre-091815` | 249 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 154,81 € · 75 % | 154,81 € · 75 % | inchangé — déjà sous la cible |
| LM-076 | `suspension-verre-446435` | 199 € | suspension-luminaire-verre-demi-globe-blanc-e… | 219,90 € | 219,90 € | 43 | 199 € | 126,04 € · 76 % | 126,04 € · 76 % | inchangé — déjà sous la cible |
| LM-077 | `suspension-verre-noir-201424` | 199 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 128,24 € · 77 % | 128,24 € · 77 % | inchangé — déjà sous la cible |
| LM-078 | `suspension-verre-led-blanc-554061` | 199 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 130,64 € · 79 % | 130,64 € · 79 % | inchangé — déjà sous la cible |
| LM-079 | `suspension-verre-651675` | 199 € | suspension-luminaire-verre-demi-globe-blanc-e… | 219,90 € | 219,90 € | 43 | 199 € | 131,44 € · 79 % | 131,44 € · 79 % | inchangé — déjà sous la cible |
| LM-080 | `suspension-verre-928640` | 199 € | suspension-design-en-laiton-et-pierre-terrazz… | 289,90 € | 284,90 € | 88 | 259 € | 131,64 € · 79 % | 131,64 € · 79 % | inchangé — déjà sous la cible |
| LM-081 | `suspension-verre-814554` | 199 € | suspension-cylindrique-verticale-en-verre-dep… | 299,90 € | 294,90 € | 28 | 269 € | 132,44 € · 80 % | 132,44 € · 80 % | inchangé — déjà sous la cible |
| LM-082 | `plafonnier-led-led-442025` | 249 € | suspension-moderne-a-vague-metallique-et-boul… | 379,90 € | 379,90 € | 27 | 339 € | 159,26 € · 77 % | 159,26 € · 77 % | inchangé — déjà sous la cible |
| LM-083 | `plafonnier-led-led-183789` | 199 € | plafonnier-bois-naturel-led-design-geometriqu… | 139,90 € | 139,90 € | 65 | 129 € | 122,64 € · 74 % | 64,31 € · 60 % | baisse |
| LM-084 | `plafonnier-led-led-698635` | 249 € | luminaire-plafonnier-anneau-beige-au-design-m… ≈ | 444,90 € | 444,90 € | 61 | 399 € | 154,81 € · 75 % | 154,81 € · 75 % | inchangé — déjà sous la cible |
| LM-085 | `plafonnier-led-led-922186` | 249 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 154,81 € · 75 % | 154,81 € · 75 % | inchangé — déjà sous la cible |
| LM-086 | `plafonnier-led-led-728204` | 199 € | plafonnier-bois-naturel-led-design-geometriqu… | 139,90 € | 139,90 € | 64 | 129 € | 127,16 € · 77 % | 68,83 € · 64 % | baisse |
| LM-087 | `plafonnier-led-led-465027` | 249 € | luminaire-plafonnier-anneau-beige-au-design-m… ≈ | 444,90 € | 444,90 € | 57 | 399 € | 149,81 € · 72 % | 149,81 € · 72 % | inchangé — déjà sous la cible |
| LM-088 | `plafonnier-led-992600` | 199 € | plafonnier-contemporain-avec-boules-verre-tra… | 269,90 € | 269,90 € | 13 | 239 € | 130,64 € · 79 % | 130,64 € · 79 % | inchangé — déjà sous la cible |
| LM-089 | `plafonnier-led-led-dore-blanc-354637` | 199 € | luminaire-plafonnier-moderne-avec-abat-jour-d… | 304,90 € | 297,40 € | 16 | 269 € | 131,24 € · 79 % | 131,24 € · 79 % | inchangé — déjà sous la cible |
| LM-090 | `plafonnier-led-led-637673` | 199 € | — | — | — | — | — | 132,84 € · 80 % | 132,84 € · 80 % | inchangé — aucun comparable |
| LM-091 | `plafonnier-led-565566` | 199 € | plafonnier-contemporain-avec-boules-verre-tra… | 269,90 € | 269,90 € | 13 | 239 € | 132,90 € · 80 % | 132,90 € · 80 % | inchangé — déjà sous la cible |
| LM-092 | `suspension-metal-led-dore-701414` | 199 € | suspension-blanche-design-moderne-en-tissu-el… | 215,90 € | 215,90 € | 371 | 199 € | 118,84 € · 72 % | 118,84 € · 72 % | inchangé — déjà sous la cible |
| LM-093 | `suspension-metal-led-dore-952116` | 249 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 159,11 € · 77 % | 92,44 € · 66 % | baisse |
| LM-094 | `suspension-metal-led-dore-843772` | 249 € | plafonnier-decoratif-blanc-style-classique-el… | 219,90 € | 229,90 € | 46 | 209 € | 157,11 € · 76 % | 123,78 € · 71 % | baisse |
| LM-095 | `suspension-metal-noir-dore-361680` | 249 € | suspension-moderne-a-vague-metallique-et-boul… | 379,90 € | 379,90 € | 27 | 339 € | 155,11 € · 75 % | 155,11 € · 75 % | inchangé — déjà sous la cible |
| LM-096 | `suspension-metal-dore-037279` | 199 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 127,04 € · 77 % | 102,04 € · 72 % | baisse |
| LM-097 | `suspension-metal-led-dore-975417` | 199 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 129,04 € · 78 % | 104,04 € · 74 % | baisse |
| LM-098 | `suspension-metal-dore-502141` | 249 € | suspension-luminaire-creme-et-argent-avec-aba… | 179,90 € | 180,40 € | 64 | 159 € | 150,11 € · 72 % | 75,11 € · 57 % | baisse |
| LM-099 | `suspension-metal-led-dore-081498` | 199 € | suspension-luminaire-circulaire-en-metal-mini… | 249,90 € | 329,90 € | 10 | 299 € | 131,04 € · 79 % | 131,04 € · 79 % | inchangé — déjà sous la cible |
| LM-100 | `suspension-deco-led-837156` | 199 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 119,64 € · 72 % | 94,64 € · 67 % | baisse |
| LM-101 | `suspension-deco-led-blanc-805304` | 199 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 119,84 € · 72 % | 94,84 € · 67 % | baisse |
| LM-102 | `suspension-deco-348096` | 199 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 121,84 € · 74 % | 96,84 € · 69 % | baisse |
| LM-103 | `suspension-deco-led-077631` | 249 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 155,11 € · 75 % | 88,44 € · 63 % | baisse |
| LM-104 | `suspension-deco-led-889929` | 249 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 189,90 € | 49 | 169 € | 155,11 € · 75 % | 88,44 € · 63 % | baisse |
| LM-105 | `suspension-deco-blanc-560098` | 199 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 125,64 € · 76 % | 100,64 € · 72 % | baisse |
| LM-106 | `suspension-deco-253182` | 199 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 184,90 € | 48 | 169 € | 126,04 € · 76 % | 101,04 € · 72 % | baisse |
| LM-107 | `suspension-deco-led-689455` | 199 € | suspension-ceramique-et-bois-avec-abat-jour-e… | 189,90 € | 189,90 € | 49 | 169 € | 126,04 € · 76 % | 101,04 € · 72 % | baisse |
| LM-108 | `lustre-statement-led-noir-950316` | 199 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 138,24 € · 83 % | 138,24 € · 83 % | inchangé — déjà sous la cible |
| LM-109 | `lustre-salon-led-341706` | 249 € | suspension-design-en-laiton-et-pierre-terrazz… | 289,90 € | 284,90 € | 88 | 259 € | 159,91 € · 77 % | 159,91 € · 77 % | inchangé — déjà sous la cible |
| LM-110 | `lustre-salon-led-366435` | 249 € | suspension-artistique-a-spirales-led-suspendu… ≈ | 299,90 € | 299,90 € | 67 | 269 € | 155,81 € · 75 % | 155,81 € · 75 % | inchangé — déjà sous la cible |
| LM-111 | `lustre-salon-957153` | 199 € | — | — | — | — | — | 124,64 € · 75 % | 124,64 € · 75 % | inchangé — aucun comparable |
| LM-112 | `lustre-salon-led-147017` | 199 € | suspension-luminaire-led-en-anneaux-dores-des… | 379,90 € | 379,90 € | 15 | 339 € | 125,64 € · 76 % | 125,64 € · 76 % | inchangé — déjà sous la cible |
| LM-113 | `lustre-salon-blanc-246282` | 249 € | suspension-luminaire-creme-et-argent-avec-aba… | 179,90 € | 180,40 € | 64 | 159 € | 153,11 € · 74 % | 78,11 € · 59 % | baisse |
| LM-114 | `lustre-salon-led-240560` | 249 € | suspension-anneau-cristal-luxueux-pour-salon-… | 449,90 € | 399,90 € | 38 | 359 € | 152,51 € · 74 % | 152,51 € · 74 % | inchangé — déjà sous la cible |
| LM-115 | `lustre-salon-led-630766` | 249 € | suspension-luminaire-art-deco-doree-en-verre | 279,90 € | 279,90 € | 381 | 249 € | 152,11 € · 73 % | 152,11 € · 73 % | inchangé — déjà sous la cible |
| LM-116 | `lustre-salon-233314` | 249 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 151,81 € · 73 % | 151,81 € · 73 % | inchangé — déjà sous la cible |
| LM-117 | `lustre-salon-blanc-575463` | 199 € | suspension-design-led-ondulee-style-contempor… | 319,90 € | 319,90 € | 77 | 289 € | 127,64 € · 77 % | 127,64 € · 77 % | inchangé — déjà sous la cible |
| LM-118 | `lustre-salon-907106` | 199 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 127,84 € · 77 % | 127,84 € · 77 % | inchangé — déjà sous la cible |
| LM-119 | `lustre-salon-led-254609` | 199 € | suspension-cascade-design-moderne-boules-noir… | 429,90 € | 414,90 € | 72 | 369 € | 129,84 € · 78 % | 129,84 € · 78 % | inchangé — déjà sous la cible |
| LM-120 | `lustre-salon-led-784326` | 199 € | plafonnier-bois-naturel-led-design-geometriqu… | 139,90 € | 139,90 € | 65 | 129 € | 130,84 € · 79 % | 72,51 € · 68 % | baisse |
| LM-121 | `suspension-moderne-led-noir-330664` | 249 € | suspension-fine-lineaire-contemporaine-pour-c… | 379,90 € | 379,90 € | 15 | 339 € | 144,18 € · 70 % | 144,18 € · 70 % | inchangé — déjà sous la cible |

## 4. Synthèse

| | |
|---|---:|
| Fiches traitées | 120 |
| **Fiches qui baissent** | **38** |
| Baisse moyenne | **46,58 € (19,9 %)** |
| Baisse médiane | 45,00 € |
| Baisse la plus forte | 90 € |
| Inchangées — déjà sous la cible | 79 |
| Inchangées — aucun comparable | 3 |
| **Bloquées par le plancher de marge** | **0** |
| Appariements francs · approximatifs · aucun | 109 · 8 · 3 |
| Confiance haute · moyenne · faible | 98 · 8 · 11 |

### Prix

| | min | p25 | médiane | p75 | max | moyenne |
|---|---:|---:|---:|---:|---:|---:|
| Nous, avant | 149 € | 199 € | **199 €** | 249 € | 299 € | 224,42 € |
| Nous, après | 129 € | 199 € | **199 €** | 239 € | 299 € | 209,67 € |
| Lustria, périmètre comparable | 19,90 € | 149,90 € | **249,90 €** | 389,90 € | 6 159,90 € | — |

**Notre médiane ne bouge pas : 199 € avant, 199 € après.** 60 fiches restent à 199 €, seules 38 descendent : le point milieu ne se déplace pas. Ce qui bouge, c'est la moyenne (224,42 € → 209,67 €) et le p75 (249 € → 239 €). Face à la médiane comparable de Lustria (249,90 €), nous sommes à **−20 %**.

### Respect de l'étape 9, fiche par fiche

| | Avant | Après |
|---|---:|---:|
| Sous la médiane de son comparable | 86 / 117 | **117 / 117** |
| Au moins 10 % sous cette médiane | 67 / 117 | **77 / 117** |

C'est le vrai résultat : **plus une seule fiche appariée n'est au-dessus du prix médian de son comparable**, contre 31 avant. Les 40 fiches qui restent entre 0 et 10 % sous la médiane le sont à cause de l'arrondi de grille, jamais de plus de 5 €.

### Marge

| | Avant | Après | Écart |
|---|---:|---:|---:|
| Somme des marges HT unitaires, palier d'entrée | 16 440,84 € | 14 965,81 € | **−1 475,03 € (−9,0 %)** |
| Marge HT moyenne en % du HT | 73,9 % | 71,7 % | -2,2 pt |
| Marge HT la plus basse | 24,18 € | 24,18 € | |

Ces montants sont une **somme de marges unitaires sur les 120 paliers d'entrée**, pas un impact de compte de résultat : sans volumes de vente, aucune pondération n'est possible. À lire comme un indicateur de catalogue.

### Pourquoi aucune fiche n'est bloquée par la marge

**0 fiche bloquée.** Le plancher ne mord jamais parce que nos coûts sont très bas devant les prix cibles : 114 fiches sur 120 coûtent 75 € ou moins rendu, ce qui place leur plancher entre 99 et 149 €, quand la cible la plus basse du plan est à 129 €. La marge HT la plus mince après application reste à 59,23 € (45 % du HT).

**Une anomalie préexistante, sans lien avec ce travail.**

- `LM-071` — Lustre pampilles cascade, branches dorées ou argentées — se vend **299 €** pour un coût proxy de 222,99 € rendu 224,99 € : 24,18 € HT de marge, soit 9,7 % du HT, **sous les deux planchers** (il faudrait 369 €). Sa cible Lustria étant de 449 €, largement au-dessus, ce plan n'y touche pas. À vérifier séparément : le proxy de coût est ici proche de la médiane des variantes, pas du palier d'entrée, donc l'anomalie est peut-être un artefact de donnée plutôt qu'une vraie perte.

### Par famille

| Famille | Fiches | Médiane avant | Médiane après | Baisses | Médiane du comparable |
|---|---:|---:|---:|---:|---:|
| Suspensions bambou | 16 | 224 € | 199 € | 8 | 219,90 € |
| Suspensions rotin | 14 | 249 € | 219 € | 7 | 259,90 € |
| Suspensions bois | 12 | 224 € | 199 € | 4 | 259,90 € |
| Lustres anneau | 12 | 224 € | 199 € | 2 | 329,90 € |
| Lustres salon | 12 | 224 € | 199 € | 2 | 319,90 € |
| Suspensions verre | 10 | 199 € | 199 € | 0 | 414,90 € |
| Plafonniers | 10 | 199 € | 199 € | 2 | 297,40 € |
| Suspensions pierre | 9 | 199 € | 199 € | 0 | 249,90 € |
| Suspensions métal | 8 | 224 € | 184 € | 5 | 200,40 € |
| Suspensions déco | 8 | 199 € | 169 € | 8 | 184,90 € |
| Lustres cristal | 7 | 299 € | 299 € | 0 | 494,90 € |
| Lustres statement | 1 | 199 € | 199 € | 0 | 414,90 € |
| Suspensions modernes | 1 | 249 € | 249 € | 0 | 379,90 € |

Les baisses se concentrent là où ils sont réellement moins chers que nous : **céramique** (8 fiches sur 8), **bambou** (8 sur 16), **rotin et corde** (7 sur 14), **tissu et plafonnier bois** (5). À l'inverse le verre, la pierre, le cristal et les lustres à anneaux LED ne bougent pas : nous y sommes déjà largement sous eux.

## 5. Les appariements dont je suis le moins sûr

D'abord les seules qui comptent vraiment : les **5 lignes qui baissent sur un appariement fragile**, classées du pool le plus étalé au moins étalé. Une baisse sur appariement solide se défend toute seule ; celles-ci sont à relire avant d'appliquer.

- **`LM-083` Plafonnier LED salon, palets bois gris ou blancs** — 199 € → **129 €**, sur 65 comparables *type+matiere*, médiane 139,90 € mais p25 74,90 € et p75 269,90 € : le pool est étalé d'un facteur 3,6, la médiane y est peu représentative. Marge après : 64,31 € HT.
- **`LM-086` Plafonnier LED linéaire cuisine, blanc ou noyer** — 199 € → **129 €**, sur 64 comparables *type+matiere+nb lumieres*, médiane 139,90 € mais p25 74,90 € et p75 269,90 € : le pool est étalé d'un facteur 3,6, la médiane y est peu représentative. Marge après : 68,83 € HT.
- **`LM-120` Plafonnier LED palets bois, blanc, noir ou doré** — 199 € → **129 €**, sur 65 comparables *type+matiere*, médiane 139,90 € mais p25 74,90 € et p75 269,90 € : le pool est étalé d'un facteur 3,6, la médiane y est peu représentative. Marge après : 72,51 € HT.
- **`LM-057` Plafonnier LED anneaux blancs, platine chromée** — 249 € → **209 €**, sur 46 comparables *type+matiere*, médiane 229,90 € mais p25 99,90 € et p75 337,40 € : le pool est étalé d'un facteur 3,4, la médiane y est peu représentative. Marge après : 115,18 € HT.
- **`LM-094` Plafonnier LED 3 anneaux entrelacés, métal doré** — 249 € → **209 €**, sur 46 comparables *type+matiere*, médiane 229,90 € mais p25 99,90 € et p75 337,40 € : le pool est étalé d'un facteur 3,4, la médiane y est peu représentative. Marge après : 123,78 € HT.

Le point commun de ces lignes : ce sont **toutes des plafonniers**. Leur rayon plafonnier mélange des spots et plafonniers d'appoint à 30-80 € avec des grands luminaires LED à 300 € et plus, sur un même tag matière. La médiane y est mathématiquement correcte et commercialement discutable. Si Hakim veut sécuriser, ce sont ces cinq lignes à sortir du lot, pas les 33 autres.

Les deux réserves de méthode à garder en tête sur **toutes** les lignes :

1. **La classe de taille n'est pas vérifiée côté Lustria** — elle n'est pas publiée. Un de nos dômes bambou Ø 80 cm est apparié à des dômes bambou dont nous ignorons la cote. C'est la limite structurelle de tout ce travail, et elle ne se lève qu'en ouvrant leurs fiches une par une.
2. **Le nombre de lumières est réduit à mono / multi.** Un lustre à 6 anneaux et un lustre à 2 anneaux tombent dans le même pool.

**Les 8 appariements approximatifs**, tous des corps LED dont ni notre titre ni leur handle ne nomme de matière. Appariés sur type + forme, plus le nombre de lumières quand il départage. Aucun ne porte de baisse :

- `LM-053` Lustre salon LED 1 à 4 anneaux en cascade, doré ou noir — 34 comparables *type+forme+nb lumieres*, médiane 354,90 € → inchangé — déjà sous la cible.
- `LM-054` Lustre salon LED spirale, doré, blanc ou noir — 67 comparables *type+forme+nb lumieres*, médiane 299,90 € → inchangé — déjà sous la cible.
- `LM-056` Plafonnier LED salon, 4 ou 6 anneaux blancs — 61 comparables *type+forme*, médiane 444,90 € → inchangé — déjà sous la cible.
- `LM-062` Suspension LED anneau fin, blanc ou noir — 67 comparables *type+forme+nb lumieres*, médiane 299,90 € → inchangé — déjà sous la cible.
- `LM-063` Lustre salon LED 5 anneaux, noir, doré ou blanc — 34 comparables *type+forme+nb lumieres*, médiane 354,90 € → inchangé — déjà sous la cible.
- `LM-084` Plafonnier LED 1 à 5 anneaux, variateur continu — 61 comparables *type+forme*, médiane 444,90 € → inchangé — déjà sous la cible.
- `LM-087` Plafonnier LED boucles entrelacées, blanc ou noir — 57 comparables *type+forme+nb lumieres*, médiane 444,90 € → inchangé — déjà sous la cible.
- `LM-110` Suspension ruban LED double boucle, doré ou blanc — 67 comparables *type+forme+nb lumieres*, médiane 299,90 € → inchangé — déjà sous la cible.

**Les 3 fiches sans aucun comparable**, prix inchangé. Aucune ne nomme de matière ni de forme exploitable, donc aucun axe au-delà du type : un pool de « tous leurs plafonniers » ou « toutes leurs suspensions » n'est pas un appariement, c'est une moyenne de rayon.

- `LM-060` Plafonnier LED chambre connecté RVB, blanc ou noir — 199 €, inchangé (type *plafonnier*, matière non nommée, forme non nommée).
- `LM-090` Plafonnier LED rond blanc, RVB et enceinte intégrée — 199 €, inchangé (type *plafonnier*, matière non nommée, forme non nommée).
- `LM-111` Suspension ruban LED trèfle, doré ou noir — 199 €, inchangé (type *suspendu*, matière non nommée, forme non nommée).

Les deux plafonniers connectés (`LM-060`, `LM-090`) relèvent en plus d'un segment domotique — RVB piloté par application, enceinte intégrée — que leur catalogue ne permet pas d'isoler : ni tag ni handle ne le signale. Le ruban LED en trèfle (`LM-111`) est une forme sculptée qui n'a pas d'équivalent nommé chez eux.

## 6. Application

`align_prices.py`. Idempotent : relancé, il ne réécrit que ce qui diffère de la cible. Sauvegarde intégrale des prix avant toute écriture dans `backups/2026-08-26-prix/`.

- `productVariantsBulkUpdate` avec `productId` + `variants: [{id, price}]`, rien d'autre dans la charge utile.
- **Aucun** `compareAtPrice` touché : les 120 fiches sont déjà à `null`, elles y restent. Aucun SKU, aucune option, aucune variante, aucun titre, aucune description, aucune image, aucune collection.
- **4 fiches à plusieurs paliers** parmi les baisses : l'écart relatif entre paliers est conservé, puis chaque palier est ramené sur la grille en 9 et l'ordre strictement croissant est revérifié.

  - `LM-013` : 249 / 299 € → **199 / 239 €**
  - `LM-019` : 249 / 299 € → **219 / 259 €**
  - `LM-029` : 249 / 399 € → **239 / 379 €**
  - `LM-113` : 249 / 299 € → **159 / 189 €**

Écritures attendues : 38 fiches, 166 variantes.

### Appliqué

Le 2026-08-25T22:57:31+00:00. **38 fiches écrites**, 166 variantes. 0 ligne ignorée.

Contrôles passés après écriture (`verify_prices.py`, relecture en ligne) : les 120 fiches et leurs 629 variantes portent le prix du plan, aucun `compareAtPrice` n'est renseigné, aucun SKU n'a bougé, aucune variante n'a été ajoutée ni supprimée, et tous les paliers restent sur la grille en 9. Relancé, `align_prices.py` n'a plus rien à écrire.

Retour arrière en une commande, prix seuls :

```bash
python3 align_prices.py --restore backups/2026-08-26-prix/prix-avant-20260825T225718Z.json --apply
```


# PHASE 3 — PRÉQUALIFICATION DE LA DEMANDE — Sommeil & environnement nocturne — 2026-09-05

Mode : **PRODUIT PUR**. Marché : France. Seuil DataForSEO : cluster adressable de l’ordre de **12 500**/mois (`PRODUCT-RESEARCH-CRITERIA.md` §1, relu ce jour).

Aucun sourcing fournisseur. Aucun `GO_FINAL` / `WATCH_FINAL` / `NO_GO_FINAL`. Aucun prix de vente décidé. Aucune estimation inventée. Registre non modifié.

---

## 1. Entrée et méthode

- **Rapport de phase 2** : `reports/phase2-filtre-sommeil-environnement-nocturne-2026-09-05.md` (branche `agents/c0-filtre-sommeil-2026-09-05`, parent `t_297f01a6`, commit `66a5fae`). Copie versionnée : `analyses/2026-09-05-chasse-clusters-sommeil-environnement-nocturne/phase2-filtre-sommeil-environnement-nocturne-2026-09-05.md`.
- **Candidat instruit** : le seul survivant de la shortlist — **surmatelas à mémoire de forme** (objet unique `surmatelas` / `sur-matelas` / `sur matelas`, niveau matière mémoire de forme). Les rejets phase 2 (matelas, chauffant, rideau occultant, gonflable, protège-matelas, etc.) ne sont **pas** requalifiés ici ; ils n’entrent dans le cluster que comme exclusions ou niveaux parents mesurés.
- **Référentiels relus** : `PRODUCT-RESEARCH-CRITERIA.md`, `PRODUCT-RESEARCH-PLAYBOOK.md` (protocole DataForSEO, étape 4, Trends, étape 5), `registre-candidats.md` (STOP « surmatelas thermorégulé actif à eau » = objet distinct, non étendu).
- **Source unique** : DataForSEO API. Chaque payload : `location_name: France`, `language_name: French`. Live : `location_code` 2250, `language_code` fr. Aucune autre base.
- **Endpoints** :
  - découverte : `dataforseo_labs/google/keyword_suggestions/live` via `scripts/kw_dfs.py` (`--pages 1 --top 40 --sans-temoin`, correspondance plein texte, MAX du groupe) ;
  - têtes : `keywords_data/google_ads/search_volume/live`, `search_partners: false`.
- **Identifiants** : `ecommerce-dropshipping/.env`, jamais affichés.
- **Témoins `tufting`** (live, France/French) :

| Moment | Heure (Paris) | Volume | CPC | Fichier |
|---|---|---:|---:|---|
| avant première mesure | 08:30:43 | **12 100** | 1,62 | `raw-phase3/temoin-phase3-avant.json` |
| après dernière mesure | 08:35:28 | **12 100** | 1,62 | `raw-phase3/temoin-phase3-apres.json` |

Non nuls, identiques entre eux, identiques au repère 12 100 du 29/08/2026. Série 12 mois identique. Aucun zéro silencieux.

- **Racines Labs (minimum deux)** :

| Graine | Lignes | Idées dédupliquées | Coût annoncé (USD) |
|---|---:|---:|---:|
| `surmatelas` | 1 000 | 539 | 0,132 |
| `sur-matelas` | 1 000 | 528 | 0,132 |
| `surmatelas mémoire de forme` | 441 | 312 | 0,065 |
| `surmatelas memoire de forme` | 318 | 229 | 0,050 |

Fichier : `raw-phase3/labs-racines.json` / `.md`.

- **Contrôle live** : 51 formulations, coût 0,09 USD, `raw-phase3/tetes-phase3.json`. Une formulation non rendue (n/a, **pas 0**) : `simmonssur-matelas` (typo de sonde, ignorée).
- **SERP / Shopping** : google.fr `hl=fr&gl=fr&pws=0`, 2026-09-05. Notes : `raw-phase3/serp-notes-2026-09-05.md`.
- **Trends** : `trends.google.fr`, France, 5 ans, Web, terme `surmatelas`. Série : `raw-phase3/trends-surmatelas-5ans-2026-09-05.txt`.
- **Coût DataForSEO observé** : 0,09 + 0,379 + 0,09 + 0,09 = **0,649 USD**.
- **CPC** : champ `cpc` présent ; **devise absente** de l’endpoint (`currency` = none). Non relabelisé en EUR.
- **Convention** : un bucket = une série mensuelle distincte. Somme = somme de buckets, jamais de reformulations à série identique. `n/a` ≠ 0.

### Limites de calcul (avant les chiffres)

- Les volumes phase 0/1/2 **n’ont pas été recopiés** comme chiffres de décision ; tout a été remesuré ce jour (mêmes ordres de grandeur, coïncidence attendue).
- `kw_dfs.py` fusionne parfois par ordre des mots ; le live tranche les têtes.
- Plancher Labs : 1 000 lignes/page pour `surmatelas` / `sur-matelas` (dernière ligne encore haute possible — le live des têtes suffit au gate).
- Session navigateur : IP Saint-Prix ; compte Google visible sur Trends. Search affiche « résultats non personnalisés » / France. Carrousel Shopping ≠ annonces texte.
- Aucun CSV Trends téléchargé (évite une action de compte). Dernier point Trends « 17 mai 2026 = 5 » traité comme semaine incomplète, non comme chute.
- Aucun % de « part mémoire de forme » dans la tête `surmatelas` n’est inventé.

---

## 2. Tableau de décision

Un seul candidat. CPC sans devise API.

| Candidat | Volume brut | Volume pertinent estimé | CPC (sans devise API) | Tendance qualitative | Concurrence publicitaire | Prix observés (TTC, 2026-09-05) | Verdict | Justification |
|---|---:|---:|---|---|---|---|---|---|
| Surmatelas à mémoire de forme | **47 900**/mois — têtes famille `surmatelas` 33 100 + `sur-matelas`/`sur matelas` 14 800 (deux buckets, séries distinctes). Formulation spécifique 3 600 (non retenue seule). Parent `matelas` 90 500 **non additionné**. | **47 900**/mois (estimation) : têtes unbranded de la famille, MAX par bucket, graphies additionnées **uniquement** parce que les séries divergent. Tailles, marques, enseignes, chauffant, rafraîchissant, lit parapluie, canapé, housse **non additionnés**. | Tête `surmatelas` : 1,28 ; `sur-matelas` : 1,11 ; spécifique mémoire de forme : 1,83. `competition` HIGH, index 100 sur la tête soudée. | Besoin **continu** 5 ans (Trends `surmatelas`) avec bosses août et fin décembre–janvier, creux printemps. Série Ads 12 mois : 22 200–40 500, pas un pic unique. | Annonces Search **texte** confirmées : Mello, Slome (famille) ; Nyte, Emma, Mello (spécifique). Shopping sponsorisé séparé (Epeda, DODO, SensoG, AliExpress, etc.). | Cœur DTC mémoire de forme observé ≈ 85–260 € (Mello 85–199 € organique ; Nyte 128–230 € ; Mello Shopping 126 € / 210 €). GSB 35–279 € (IKEA). Marketplace / fibre souvent **< 50 €**. Marques literie 120–360 € (Bultex, Epeda). Voir §4. | **REVIEW_PREQUALIFICATION** | Demande famille nettement au-dessus de 12 500 après règle hiérarchique ; intention commerciale ; une boutique spécialisée **existe déjà**. Obstacle majeur : occupation page 1 GSB + DTC installés + Shopping low-ticket + claims santé visibles. Pas un STOP volume. Pas un PASS propre. |

---

## 3. Détail par candidat — Surmatelas à mémoire de forme

### 3.1 Niveaux de généralité testés (live, 2026-09-05)

| Niveau | Formulation | Volume | Série 12 mois (récent → ancien tel que rendu) | Décision |
|---|---|---:|---|---|
| Spécifique | `surmatelas à mémoire de forme` (et `surmatelas memoire de forme`, `surmatelas mémoire de forme`, `memoire de forme surmatelas`) | 3 600 | 2900 2400 3600 2900 4400 4400 4400 2900 4400 3600 4400 4400 | **Même bucket**. Sous le seuil. Interdit de STOP sans le parent. |
| Spécifique graphie trait | `sur-matelas à mémoire de forme` | 1 900 | 1300 1300 1600 1600 1900 1900 2400 1600 2400 1900 2400 2400 | Bucket **distinct** du 3 600. Non additionné au pertinent (même objet ; conservateur). |
| Spécifique taille | `surmatelas à mémoire de forme 160x200` | 1 600 | distincte | Longue traîne, même page possible. Non additionnée. |
| Spécifique taille (ordre inverse) | `surmatelas 140x190 à mémoire de forme` | 10 | quasi nulle récente | n/a partiel ; **pas** le 1 900 Labs. Live fait foi. |
| Famille — graphie soudée | `surmatelas` | **33 100** | 27100 22200 27100 27100 27100 27100 40500 33100 40500 33100 33100 40500 | **Niveau retenu** (tête). |
| Famille — graphie trait / espace | `sur-matelas` = `sur matelas` | **14 800** | 12100 9900 12100 12100 14800 14800 18100 14800 18100 18100 18100 18100 | Même bucket entre elles ; **distinct** de 33 100. Additionné au brut/pertinent (test de série). |
| Variante client | `surconfort de matelas 160x200` | 14 800 | **identique** à `surmatelas 160x200` | Même bucket taille, pas un volume en plus. |
| Variante client | `topper` / `topper matelas` / `surconfort` | 4 400 / 260 / 10 | — | `topper` contaminable (anglais, hors literie possible). Non retenu dans le pertinent. |
| Tailles famille (buckets distincts) | 140x190 22 200 ; 160x200 14 800 ; 180x200 4 400 ; 90x190 3 600 ; 140x200 1 900 ; 120x190 1 900 ; 80x200 1 000 ; 90x200 880 | — | Une même page tailles les servirait ; **non additionnées** pour ne pas gonfler le gate. |
| Parent | `matelas` | 90 500 | distincte | **Non attribué** au surmatelas (leçon bateau amorceur). SERP parent = matelas, pas l’objet. |
| Parent matière | `matelas mémoire de forme` | 8 100 | distincte | Autre objet (matelas). Non attribué. |

**Niveau retenu comme cluster adressable** : famille `surmatelas` (deux graphies à séries distinctes = 47 900).

**Justification** : la formulation spécifique (3 600) est sous 12 500. La SERP France de `surmatelas` **montre ce type de produit** (titres « mémoire de forme », collections Nyte/Mello, Shopping visco). Intention d’achat oui. Une boutique spécialisée peut viser la tête (preuve : elle le fait déjà). Attribuer 90 500 `matelas` serait un gonflage. Attribuer 100 % de 47 900 à la **seule** mousse visco sans part mesurée serait symétriquement abusif : d’où REVIEW, pas PASS, et pertinent = volume de la famille unbranded, pas un sous-échantillonnage inventé.

### 3.2 Mots-clés retenus (live, pour le cluster)

| Mot-clé | Volume | CPC | Brut/net de marque | Niveau | Date |
|---|---:|---:|---|---|---|
| `surmatelas` | 33 100 | 1,28 | net (tête sans marque) | famille | 2026-09-05 |
| `sur-matelas` / `sur matelas` | 14 800 | 1,11 | net | famille (même bucket) | 2026-09-05 |
| `surmatelas à mémoire de forme` (+ 3 graphies, même série) | 3 600 | 1,83 | net | spécifique | 2026-09-05 |

Source : `keywords_data/google_ads/search_volume/live`, France/French, `search_partners` false.

### 3.3 Mots-clés exclus (motifs) — volumes live, **non soustraits** de 33 100 (ce sont d’autres buckets)

| Mot-clé | Volume | Motif |
|---|---:|---|
| `ikea surmatelas` / `ikéa surmatelas` | 8 100 | enseigne / marque tierce (même série) |
| `surmatelas decathlon` | 5 400 | enseigne §4 ; saison camping (série 12 100→2 400) |
| `surmatelas lit parapluie` | 9 900 | accessoire incompatible (poussette) |
| `surmatelas rafraîchissant` | 4 400 | objet STOP registre (thermorégulé / eau) ; pic été |
| `surmatelas chauffant(e)` | 3 600 | rejet phase 2 (tranche basse + électrique) ; pic hiver |
| `sofitel surmatelas` | 2 400 | marque hôtelière |
| `emma surmatelas` | 1 600 | marque tierce |
| `but surmatelas` | 1 900 | enseigne |
| `conforama surmatelas` | 1 600 | enseigne |
| `dodo surmatelas` | 1 300 | marque tierce |
| `bultex surmatelas` | 1 300 | marque tierce |
| `mello surmatelas` | 590 | marque tierce (DTC occupant) |
| `surmatelas tempur` | 480 | marque tierce |
| `sur-matelas simmons` | 50 | marque tierce |
| `surmatelas canapé` | 1 300 | objet convertible, pas literie chambre |
| `housse sur-matelas` | 4 400 | accessoire / protège, autre page |
| `surmatelas latex` | 720 | matière différente |
| `meilleurs surmatelas` | 1 000 | informationnel / comparatif |
| `surmatelas à quoi ça sert` | 70 | informationnel |
| `surmatelas ferme` | 1 600 | attribut, conservé hors pertinent (sous-ensemble possible) |

Labs (non recontrôlés un par un en live, hors têtes) : `avis`, `mal`/`dos`, `soldes`, Leboncoin, nettoyage de taches sur **matelas** (contamination de la graine `sur-matelas` : « tache / enlever / pipi »). Ces lignes n’entrent pas dans 47 900.

### 3.4 Lecture SERP (page 1, 2026-09-05)

**`surmatelas`** — intention **oui**. Pas de rabattement. Mix commercial.

- Search texte : 2 annonces (Mello, Slome) — **pas** confondues avec le carrousel.
- Organique : 2 DTC (Nyte, Mello) puis IKEA, DODO, Conforama, Compagnie du Blanc, 2 guides (LeMatelas, Tediber), BUT.
- Shopping mixte : mémoire de forme, latex, naturel, fibre, **et** matelas / protège-matelas.
- Recherches associées : IKEA, tailles, Emma, « mal de dos », UFC Que choisir.
- Pack local literie (biais IP Saint-Prix).

**`surmatelas à mémoire de forme`** — intention **oui**.

- Search texte : Nyte, Emma, Mello (+ Grand Litier magasin).
- Organique : Mello, Sampur, DODO, Bdreams, Bultex, Tediber (claims dos), Conforama, Emma, Morphée, Compagnie du Blanc.
- Associated : IKEA, tailles, Bultex.

Contrôles SERP : pas de rabattement ; pas de retournement pièce/produit fini ; contamination GSB et low-ticket **dans** Shopping ; marque cachée = Emma/IKEA en requêtes associées, pas dans la tête ; réparation absente ; KD = densité d’acteurs, pas un score outil.

---

## 4. Concurrents observés

### Spécialistes / DTC / marques à récit (comparables)

| Acteur | Preuve 2026-09-05 | Type |
|---|---|---|
| Mello | Annonce texte + organique n°1/n°2 ; Shopping 126 € et 210 € ; organique 85–199 € | DTC surmatelas, « N°1 », 100 nuits |
| Nyte (good-nyte.com) | Organique n°1 famille ; annonces texte spécifique ; Shopping 192 € / 176 € | DTC, 100 nuits, 10 ans |
| Slome | Annonce texte famille ; Shopping 70 € housse / 140 € bambou mémoire | DTC |
| Tediber | Organique guide + Shopping 290–350 € surmatelas 7 cm | DNVB literie |
| Bonsoirs | Shopping 290–505 € « 100 % naturel » | DNVB |
| Bdreams | Organique spécifique | Marque FR |
| Atelier / Matelas Morphée | Fiches 155–205 € | Atelier |
| Sampur | Organique + Shopping (souvent < 50 € fibre **et** packs) | Marque volume |
| Bultex / Epeda | Organique + Shopping 120–360 € mémoire | Marques literie |

### Repères marketplaces / GSB (pas des comparables DTC)

IKEA (35–279 €, organique page 1), BUT, Conforama, JYSK, Carrefour (Tex Home 48–56 €), Lidl (Emma 90 € ; autre fiche thermorégulée), Darty, Leroy Merlin, Amazon.fr, Cdiscount, Groupon, Temu, AliExpress (18–71 €), ManoMano, La Redoute, Habitat, Castorama, Maisons du Monde marketplace.

**Lecture occupation PRODUIT PUR** : la tête est tenue. Ce n’est pas « aucun spécialiste » ; c’est l’inverse.

### Sonde prix (échantillon Shopping + extraits SERP, TTC, 2026-09-05)

Pas 50 prix uniques dédupliqués au centime ; paliers **observés** :

- **< 50 €** : nombreux — fibre/microfibre, Temu, AliExpress 4 cm, IKEA NÄSFJÄLLET 35 €, Casabel ~30 €, DODO 37 € Carrefour, Sampur 40 €. Hors cible 50–400 € **en tant que cœur**, mais **visibles** sur la requête.
- **50–120 €** : DODO 56–105 €, IKEA 75–99 €, Slome 70 €, INRE ManoMano 60 €, Mello gel Shopping 126 €.
- **120–260 €** : Nyte, Mello original 210 €, Habitat 199 €, BUT Dreamea 90–140 €, Bultex MEMO 5 190 €, Epeda Harmonie 175–182 €.
- **260–400 €** : Tediber 290–350 €, Epeda Noblesse 239–305 €, Bultex Memopower/Memomax 302–362 €, Emma Performance 329 €.
- **> 400 €** : DODO luxe 430 €, Emma matelas (contamination), Bonsoirs 505 € — hors ou bord de tranche.

Vides : pas un trou net 300–400 sur l’objet mémoire de forme ; le bas de grille est saturé. **Aucun prix de vente maison proposé** (interdit phase 3).

---

## 5. Risques et à vérifier

- **Occupation** : Mello/Nyte/Slome + IKEA/BUT/Conforama sur la même tête. Un générique « rectangle de mousse » n’a pas d’espace évident. L’angle pédagogique sans claim santé (thèse phase 2) n’est **pas** encore tenu par un acteur isolé, mais Nyte/Mello communiquent déjà essai 100 nuits / fabrication FR.
- **Claims santé** : Tediber organique « mal de dos / points de pression » ; Nyte pub « recommandé par des kinés » ; associées « surmatelas mal de dos ». Risque ads/Merchant si l’offre glisse.
- **Hygiène / retours / volumétrie** : 100 nuits chez les DTC = norme ; colis encombrant. Non chiffré (sourcing).
- **Shopping < 50 €** : ancre de prix marketplace. Cœur DTC observé reste dans 50–400 €.
- **Contamination d’objets** : lit parapluie 9 900 ; chauffant ; rafraîchissant (STOP registre) ; canapé ; protège-matelas dans Shopping.
- **Marques dans la traîne** : IKEA 8 100 à elle seule — inutilisable titre/Merchant.
- **Saisonnalité** : hiver plus fort, pas un produit mort l’été (Trends socle ~45–65 hors bosses).
- **À vérifier en aval seulement si Hakim ouvre la due diligence** : densité de mousse réelle, CE, origine, coût rendu, droit de gagner vs Mello — **hors rôle**. Les cartes concurrence/sourcing enfants ne doivent enchaîner **que** sur un PASS ; il n’y en a pas.

---

## 6. Statuts de préqualification

| Candidat | Statut | Chaîne aval |
|---|---|---|
| Surmatelas à mémoire de forme | **REVIEW_PREQUALIFICATION** | Remonte à Hakim. **Pas** de `PASS_PREQUALIFICATION`. Concurrence approfondie et sourcing AliExpress **non autorisés** par ce rapport. |

Pas de `STOP_PREQUALIFICATION` : après hiérarchie, le cluster famille (47 900) dépasse 12 500 et la SERP vend bien le produit.

Pas de `PASS_PREQUALIFICATION` : obstacle majeur concurrence/GSB/claims, et refus d’attribuer un sous-volume visco inventé.

Pas de `CAS LIMITE — décision Hakim requise` au sens ±20 % du seuil (47 900 n’est pas dans 10 000–15 000). Le REVIEW **est** déjà la remontée à Hakim.

Aucun `GO_FINAL` / `WATCH_FINAL` / `NO_GO_FINAL`.

### Gate

- Rapport daté du **2026-09-05**, six sections.
- Témoins tufting 12 100 avant/après.
- Deux racines + hiérarchie spécifique → famille → parent.
- Brut/net et exclusions documentés.
- SERP/Shopping France, prix datés.
- Verdict dans la liste autorisée.

Chemin du livrable (copie versionnable, `reports/` est gitignoré) :

`/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/analyses/2026-09-05-chasse-clusters-sommeil-environnement-nocturne/phase3-demande-sommeil-environnement-nocturne-2026-09-05.md`

Copie attendue par le brief (gitignorée) :

`/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/reports/phase3-demande-sommeil-environnement-nocturne-2026-09-05.md`

Branche de dépôt : `agents/c0-demande-sommeil-2026-09-05`

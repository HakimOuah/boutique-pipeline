# Étapes 2–4 — Mesure, consolidation, net de marque

**Date : 2026-08-31** · Mode **UNIVERS** · Base **DataForSEO France / French** · Seuil applicable : consolidé familles **≥ 37 500** (confort 50 000) — `PRODUCT-RESEARCH-CRITERIA.md` §1, calibré DFS. Les seuils SEMrush (30 000) ne s’appliquent pas aux chiffres de ce dossier.

Familles figées **avant** cette mesure : [`00-familles-figees.md`](00-familles-figees.md). Aucune famille ajoutée en cours de route. F7 a gardé son périmètre « bijou de cheville » ; la graine `chevillère` a été mesurée comme parent suspect, puis **retirée à 100 %** en SERP (étape 5).

---

## 1. Contrôle témoin

Endpoint `keywords_data/google_ads/search_volume`, France.

| Moment | `tufting` | Attendu | Verdict |
|---|---:|---:|---|
| Avant F1–F2 | **12 100** | 12 100 | conforme |
| Après F3–F5 | **12 100** | 12 100 | conforme |
| Après F6–F8 | **12 100** | 12 100 | conforme |
| Après parents | **12 100** | 12 100 | conforme |
| Lot `search_volume` des têtes | **12 100** | 12 100 | conforme |

Aucun zéro silencieux. CPC DataForSEO, **devise du compte = USD** (écrit à côté de chaque tête).

---

## 2. Ce qui a été mesuré

Voie A : `scripts/kw_dfs.py` (Labs `keyword_suggestions`, 1 page, cache disque) pour découvrir le vocabulaire. Puis `search_volume/live` pour **caler les têtes**. Les deux ne se mélangent pas : Labs sert à voir les contaminations ; le consolidé se calcule sur les têtes `search_volume` + les idées distinctes qu’une même page servirait, jamais sur la somme brute Labs.

| Lot | Graines | Coût | Plancher 1 000 lignes |
|---|---|---:|---|
| F1–F2 | 6 | 0,20 USD | non |
| F3–F5 | 8 | 0,46 USD | non |
| F6–F8 | 12 | 0,59 USD | `bracelet cheville`, `chaine cheville` |
| Parents | 6 | 0,31 USD | `bracelet personnalisé` |
| Têtes SV | 31 + 16 | 0,18 USD | — |

Témoin inclus. Coût mesure ≈ **1,7 USD**.

---

## 3. Têtes `search_volume` — ce sont elles qui portent le consolidé

Lu le 2026-08-31. Série mensuelle = 12 mois Google Ads. CPC en **USD**.

| Famille | Formulation | Volume | CPC USD | Comp. | Nov 2025 | Déc 2025 | Août 2025 |
|---|---|---:|---:|---|---:|---:|---:|
| F1 | `bracelet photo` | **2 400** | 2,04 | HIGH | 5 400 | 6 600 | 1 900 |
| F1 | `bracelet personnalisé photo` | 1 300 | 2,12 | HIGH | 2 400 | 4 400 | 720 |
| F1 | `bracelet photo projection` | 590 | 2,01 | HIGH | 1 300 | 1 000 | 720 |
| F2 | `collier photo` | **1 600** | 1,78 | HIGH | 2 900 | 2 900 | 1 300 |
| F2 | `médaillon photo` / `medaillon photo` | **2 400** | 1,06 | — | 3 600 | 4 400 | 2 400 |
| F2 | `pendentif photo` | 1 600 | 1,25 | — | — | — | — |
| F2 | `collier photo projection` | 260 | 1,76 | HIGH | 590 | 720 | 210 |
| F3 | `collier prenom` = `collier prénom` | **6 600** | 1,60 | — | 12 100 | 12 100 | 5 400 |
| F4 | `collier initiale` | **2 400** | 1,34 | — | 4 400 | 4 400 | 2 400 |
| F4 | `collier lettre` | 1 900 | 1,42 | — | 3 600 | 3 600 | 1 900 |
| F5 | `bracelet prenom` = `bracelet prénom` | **1 900** | 1,34 | — | 3 600 | 3 600 | 1 900 |
| F5 | `bracelet gravé` | 1 000 | 1,74 | — | 1 600 | 1 600 | 720 |
| F5 | `bracelet gravé homme` | 1 900 | 1,81 | — | 2 900 | 3 600 | 1 600 |
| F6 | `bracelet couple` | **5 400** | 1,12 | — | 6 600 | 9 900 | 4 400 |
| F6 | `collier couple` | 720 | 0,71 | — | 1 000 | 1 300 | 880 |
| F6 | `bijoux couple` | 1 300 | 0,99 | — | 1 900 | 2 900 | 1 000 |
| F6 | `bracelet couple personnalisé` | 480 | 1,24 | — | 590 | 1 000 | 320 |
| F7 | `chaine de cheville` = `chaîne de cheville` | **4 400** | 0,77 | — | — | — | — |
| F7 | `bracelet de cheville` | 2 900 | 0,71 | — | — | — | — |
| F7 | `bracelet cheville` | 3 600 | 0,66 | — | — | — | — |
| F7 **retiré** | `chevillère` / `chevillere` | 14 800 | 0,33 | — | — | — | — |
| F8 | `bague personnalisée` | **2 400** | 1,34 | — | 4 400 | 4 400 | 2 400 |
| F8 | `bague gravée` | 1 600 | 1,15 | — | 2 400 | 2 400 | 1 600 |
| F8 **à adjuger** | `bague de promesse` | **18 100** | 1,22 | — | 18 100 | 22 200 | 18 100 |
| Parent | `collier personnalisé` | **12 100** | 1,57 | — | 22 200 | 27 100 | 9 900 |
| Parent | `bracelet personnalisé` | **9 900** | 1,76 | — | 18 100 | 18 100 | 9 900 |
| Parent | `bijoux personnalisés` | 1 000 | 1,46 | — | 1 600 | 1 900 | 720 |
| Parent | `bijoux personnalisés femme` | 3 600 | 2,04 | — | 6 600 | 8 100 | 2 400 |

Paires accentuées vérifiées : `collier prenom` / `prénom` = **même volume et même série** → un bucket, MAX. Idem `médaillon` / `medaillon`, `bracelet prenom` / `prénom`, `chaine de cheville` / `chaîne de cheville`.

**Ce qu’on n’additionne pas ici :** la somme brute Labs F1–F8 (146 480) — elle compte des significations, des tombeaux, du silicone festival, des alliances. Elle est dans les JSON, elle ne fonde aucun total.

---

## 4. Consolidation par famille — une page, pas une addition de têtes parents

Règle : on additionne les formulations **distinctes** (volumes différents = buckets différents) qu’**une même collection** servirait. On n’additionne pas le parent `collier personnalisé` 12 100 par-dessus F2+F3+F4.

| # | Famille | Formulations retenues (volume individuel) | Brut | Net de marque | Motif des retraits |
|---|---|---|---:|---:|---|
| F1 | Bracelet photo | `bracelet photo` 2 400 · `bracelet personnalisé photo` 1 300 · `bracelet photo projection` 590 · queue Labs commerciale FR (~800 : intérieur, souvenir, homme) | **5 090** | **5 090** | Amazon/Etsy/Pandora en queue, volumes 10–20 |
| F2 | Collier photo / médaillon | `collier photo` 1 600 · `médaillon photo` 2 400 · `collier personnalisé photo` 1 300 · `pendentif photo` 1 600 · projection 260 | **7 160** | **7 160** | `photo medaillon tombe` 390 retiré (cimetière). Médaillon = ouvrant, pas seulement projection — une page « colliers photo » les sert |
| F3 | Collier prénom | `collier prenom` 6 600 · `collier or prenom` 880 · `collier femme prenom` 720 | **8 200** | **7 480** | `obtenir collier prenom` 720 (boutique) · `collier prenom histoire d'or` 390 · `collier prenom maty` · Pandora arbre de vie |
| F4 | Collier initiale | `collier initiale` 2 400 · `collier lettre` 1 900 | **4 300** | **4 300** | Lettres isolées (`lettre m`) = traîne, pas sommable comme une 3ᵉ page |
| F5 | Bracelet gravé / prénom | `bracelet prenom` 1 900 · `bracelet gravé homme` 1 900 · `bracelet gravé` 1 000 | **4 800** | **4 800** | Homme **compté** : B&S a la collection. Si page unique unisexe, retirer 1 900 plus tard |
| F6 | Bijoux couple | `bracelet couple` 5 400 · `collier couple` 720 · `bracelet couple personnalisé` 480 | **6 600** | **6 600** avant SERP | `bracelet couple à distance` 590 · `bracelet connecté` 590 · `totwoo` 140 **retirés** (électronique). `bague de promesse couple` 2 900 renvoyé en F8 |
| F7 | Bijou de cheville | `chaine de cheville` 4 400 · `bracelet de cheville` 2 900 | **7 300** | **7 300** avant SERP | **`chevillère` 14 800 retiré intégralement** — orthopédie (étape 5) |
| F8 | Bague perso | `bague personnalisée` 2 400 · `bague gravée` 1 600 | **4 000** | **4 000** | `bague de promesse` 18 100 **hors brut famille**, adjugé en SERP |

Parents, **hors consolidé familles** (garde-fou n° 2) :

| Parent | Volume | Traitement |
|---|---:|---|
| `collier personnalisé` | 12 100 | Recouvre F2+F3+F4. 0 % versé tant que la SERP n’a pas adjugé une part *en plus* des filles |
| `bracelet personnalisé` | 9 900 | Recouvre F1+F5+F6. Idem. PLANCHER Labs (1 000 lignes) — le 9 900 SV est la tête, pas le cluster |
| `bijoux personnalisés` | 1 000 | Trop mince pour un univers. `bijoux personnalisés femme` 3 600 = autre formulation, pas sommé avec 1 000 (série à comparer ; volumes différents) |

---

## 5. Trois valeurs — avant SERP (étape 5 affine)

Le cœur de l’univers B&S = photo + prénom + couple + bague gravée. F7 est du **catalogue filler**, pas le phare.

| Scénario | Contenu | Total net |
|---|---|---:|
| **A — têtes à 0 % de parents, F7 hors cœur, F8 sans promesse, F6 plein** | F1+F2+F3+F4+F5+F6+F8 | **40 030** |
| **B — part adjugée (défaut)** | A, F6 à 60 % (mix marques / électronique vu en SERP), F7 hors, promesse 0 % | **37 390** |
| **C — généreux** | A + F7 bijou 7 300 + 15 % de `bague de promesse` (2 715) | **50 045** |

Plancher UNIVERS DFS = **37 500**. A est juste au-dessus, B est **cas limite** (−110), C est confort.

**Le verdict volume ne peut pas se lire sur A tout seul** : B dépend de la SERP F6, C dépend de deux familles que la SERP a déjà malmenées (promesse occupée, cheville fashion). → étape 5.

---

## 6. Saisonnalité (remplace Trends index)

Séries Google Ads 12 mois, têtes. Socle hors Q4 visible sur 8 mois. Bosse nov–déc ×2 à ×3,5. `bracelet couple` bosse aussi en **janvier** (Saint-Valentin).

Ce n’est pas un univers 2 mois par an. C’est un univers cadeau à socle, Q4 qui double. Forme **socle + Q4** — conforme à l’exigence UNIVERS (socle ≥ 8 mois).

Ratio prix ÷ CPC sur le phare photo : 49,95 € / 2,04 USD ≈ **24**, cible maison ≥ 100. L’unité Search est **hors ratio** avant même la concurrence. Documenté, pas tranché ici.

---

## 7. Ce que je n’ai pas pu faire

- SEMrush `db=fr` non utilisé (voie A DFS, signalé). Un pass éventuel sera un pass **sur repli**.
- `bracelet personnalisé` Labs = plancher 1 000 lignes. Tête SV 9 900 calée.
- Sonde Shopping 30–50 prix : non faite (étape 9 partielle via SERP seulement).
- Google Trends UI : non ouverte ; la série Ads ci-dessus en tient lieu pour la *forme*.
- Recoupement mesuré entre F3 et F4 (`collier lettres prenom` 480) : laissé dans F3, pas sommé deux fois.

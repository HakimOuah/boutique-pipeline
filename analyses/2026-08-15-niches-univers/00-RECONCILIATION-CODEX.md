# Reprise du travail Codex — ce qui est acquis, ce qui est à refaire

**Date : 15/08/2026, 22h.** Hakim a fait tourner Codex pendant la coupure de session Claude. Codex a
rendu un lot complet (`COMPLETE_NO_GO`, run `20260815-181328`, commits `14f6829` et `5753688` sur la
branche `codex/niches-univers-20260815`), puis un audit des quatre liens concurrents fournis par
Hakim. Ce document dit **sur quoi on s'appuie sans le refaire** et **ce qui doit être remesuré**,
avant de relancer quoi que ce soit.

---

## 1. Verdicts de Codex

| Univers | Verdict Codex | Sur quoi il repose |
|---|---|---|
| U1 literie | `STOP_PHASE_2_DROIT_DE_GAGNER` | Volume **acquis** (`housse de couette` 60 500 seule) ; STOP sur 10 concurrents documentés |
| U2 bouillottes | `REPARER_AVANT_SOURCE_EXACTE` | Volume provisoire 42 600 ; médiane 17,63 € ; **sourcing 0/30 pertinents** |
| U3 globe/cartographie | `STOP_VOLUME_CATALOGUE` | 22 870 mesurés → déficit 7 130 |
| U4a télescopes | `STOP_REPRISE_SANS_THESE_NOUVELLE` | Verrou marques + SAV technique |
| U4b déco astro | `STOP_VOLUME_CATALOGUE` | 12 000 sur **4 têtes** |
| U5 gothique | `STOP_VOLUME_CATALOGUE` → révisé en `REOUVRIR_PHASE0_CIBLEE` | 4 120 sur **7 têtes** |
| U6 ésotérisme | `STOP_PHASE_3_DROIT_DE_GAGNER` | 31 600 prudents ; STOP sur 10 concurrents |

---

## 2. Ce qui est acquis et ne sera pas refait

Ce travail est réel, sourcé et daté. Le reprendre serait du gaspillage.

1. **Cartographie concurrentielle** — 10 acteurs U1 (Linvosges, Blanc des Vosges, Carré Blanc, La
   Redoute, Ikea, Hema, Dodo, Françoise Saget, Blancheporte, La Compagnie du Blanc), 12 acteurs U3
   (Afficheo, Eclyna, Gaia Map, La Carte du Monde, L'Afficherie, Nature & Découvertes, Univers Globe,
   Woodleo, Woodwork08…), 10 acteurs U6, profils U2, plus les **quatre liens de Hakim** profilés en
   détail (Antre Gothique 2 341 URL produit / 75 collections ; Le Petit Astronaute 1 769 URL / 105
   catégories ; Moment Ici 2 344 produits, médiane 39 € ; MOVA Globes 54 fiches, médiane 258 €).
   → **Remplace l'étape 3 de mon plan.**
2. **Sondes de prix** — 30 à 50 prix relevés par univers : U1 médiane 70,91 €, U2 17,63 €, U3 globe
   81,38 €, U5 59,45 € (accessoires seuls 12,40 €), U6 20 € bimodale. → **Remplace l'étape 2 prix.**
3. **Prévol AliExpress** — passerelle officielle saine, OAuth valide, destination FR répond.
4. **Le catalogue de garde-fous IP/conformité** (licences Killstar, NASA, Star Wars ; contenu
   choquant Google Ads ; claims lithothérapie) — directement réutilisable.
5. **Le découpage des frontières entre univers** (tableau §6.4 de l'audit) : qui possède `globe lune`,
   où vont l'occulte et l'autel, pourquoi les bijoux pierres ne s'ajoutent pas à U6. C'est du travail
   de méthode propre, et il évite le double comptage.
6. **La découverte d'un candidat autonome** : « bijouterie pierres naturelles et symboles » (révélé
   par Moment Ici), à mesurer hors U6.

---

## 3. Le défaut structurel : Codex a mesuré des têtes, pas des familles

**C'est le point décisif, et il invalide trois STOP sur volume.**

Codex a mesuré **4 à 11 requêtes par univers** et additionné les têtes. Or la méthode maison
(`METHODE-ANALYSE-MARCHE.md`, étape 3) existe précisément parce que cette façon de compter
sous-évalue systématiquement :

> « C'est l'étape qui a multiplié les chiffres de Noirmont par 3 à 12. On mesurait une tête par
> famille. Or `montre squelette homme` 2 900 coexiste avec `montre squelette` 2 400, `montre homme
> squelette` 1 600 et `squelette montre` 1 300 : ce sont des recherches distinctes qu'une seule page
> de collection sert. La famille pèse 17 120, pas 2 900. »

Sur les 20 familles de Maison Noirmont, **toutes étaient sous-comptées d'un facteur 3 à 12**.

La preuve que le même phénomène est ici : ma propre lecture du Keyword Magic Tool en expression
exacte sur `housse de couette` (15/08, base France) donne **93 624 mots-clés** et un volume broad de
**1 093 330**, dont `housse de couette` 60 500, `housse de couette 220x240` 22 200, `housse de couette
260x240` 14 800, `housse de couette 200x200` 9 900, `housse de couette 240x260` 9 900 — **des
recherches distinctes qu'une seule page de collection sert**, avec les tailles en filtres. Codex n'a
retenu que 60 500. L'écart sur cette seule famille dépasse le déficit total qu'il reproche à U3.

**Conséquence par univers :**

| Univers | Ce que Codex annonce | Ce que c'est réellement |
|---|---|---|
| U3 | « 22 870, déficit 7 130 » | Un **plancher sur 8 requêtes**. Le déficit peut être comblé par la seule consolidation des variantes, sans ajouter une seule graine. |
| U4b | « ≤ 12 000 » | Un **plancher sur 4 têtes**. Codex l'admet lui-même en révision : « 12 k est la somme brute maximale de ces quatre têtes, non une borne de l'univers ». |
| U5 | « ≤ 4 120 » | Un **plancher sur 7 têtes**, dont la phase 0 disait elle-même `MESURE_POLLUEE_INSUFFISANTE` et `A_APPROFONDIR` avec les graines déco/bijoux/accessoires en `MANQUANT`. Le rapport terminal a transformé un « pas encore mesuré » en STOP. |

Codex a lui-même corrigé le tir dans son audit des liens : U3 et U4b passent en
`STOP_VOLUME_CATALOGUE_AU_PERIMETRE_MESURE` + audit autorisé, U5 en `REOUVRIR_PHASE0_CIBLEE`.
**Sa conclusion et la mienne convergent : ces trois univers n'ont pas été mesurés, ils ont été
effleurés.**

⚠️ Le piège symétrique reste interdit : on additionne **ce qu'une même page servirait, et rien
d'autre** (anti-exemple « catio »). Consolider n'est pas empiler des familles voisines.

---

## 4. Deuxième correction : le 0/30 du sourcing U2 n'est pas un verdict marché

Codex conclut U2 en `REPARER_AVANT_SOURCE_EXACTE` sur « 30 résultats lus, 0 pertinent », avec ces
requêtes : `microwave flaxseed heating pad neck`, `rubber hot water bottle knitted cover 2 liter`,
`hot water bag plush cover winter warmer`, `bouillotte eau chaude housse peluche 2L`.

**Ce sont des requêtes en mots fréquents, et c'est le mode d'échec documenté de l'API.** Mémoire
`api-aliexpress-search-mots-rares` (établie le 15/08 sur ≈ 130 appels) : `search` fait un appariement
large puis **trie par popularité globale** ; dès qu'une requête contient un mot fréquent (`bottle`,
`water`, `bag`, `cover`), elle ramène les best-sellers de la catégorie entière.

**Retesté ce soir**, six requêtes, même passerelle : `bouillotte`, `noyaux cerise`, `bouillotte
peluche`, `hot water bottle`, `cherry pit pillow`, `chauffe-mains rechargeable` → **0 résultat
pertinent sur 33**, uniquement des pulvérisateurs d'huile, gourdes de vélo et taies d'oreiller.

C'est le cas limite déjà consigné : **« quand une famille n'a aucun mot rare, `search` ne la sert
pas »** (cas vécu : porte-montre/présentoir, 14 requêtes, zéro résultat). La bouillotte n'a ni
référence technique, ni mot de métier distinctif.

**Donc :** le 0/30 mesure une limite d'outil, pas une absence de fournisseur. La sortie correcte
n'est pas « réparer avant sourcing » mais **passer par les noms de magasins** — trouver les boutiques
via le catalogue d'un concurrent, puis interroger `search` sur leur nom. À défaut, le sourcing
bouillotte se fait à l'étape DSers, pas par l'API.

---

## 5. Ce qui reste vrai et que je ne conteste pas

- **U1 et U6 ne sont pas des STOP de volume, ce sont des STOP de droit de gagner.** Dix acteurs
  documentés par univers, qui couvrent les angles génériques. Remesurer les volumes ne les rouvre
  pas : il faudrait une sous-intention mal servie ou un avantage propriétaire. La consolidation
  gonflerait leurs chiffres sans changer le verdict.
- **U4a télescopes reste fermé** : verrou marques, confiance technique et SAV — aucun des quatre
  liens n'y répond.
- **La discipline de Codex sur la preuve est bonne** : il refuse explicitement de convertir 2 341 URL
  concurrentes en demande, il sépare observé / manquant / hypothèse, et son audit aveugle attaque ses
  propres conclusions. C'est la bonne manière de travailler.

---

## 6. Décision de reprise

**On ne refait pas** : concurrence, prix, prévol, garde-fous IP, frontières d'univers.

**On refait, et une seule fois bien** : la mesure consolidée par famille (méthode étapes 1-3, Keyword
Magic Tool en expression exacte, 0 crédit) sur les trois univers fermés sur un volume non mesuré :

| Priorité | Univers | Objectif chiffré | Autorisation Codex |
|---|---|---|---|
| 1 | **U5 gothique** | Reconstruire le total depuis zéro (mode, bijoux, chaussures, sacs, déco), textile inclus | `REOUVRIR_PHASE0_CIBLEE_SOUS_PREUVE_VOLUME` |
| 2 | **U4b déco astro** | Trouver ≥ 18 000 nets additionnels (lampes, veilleuses, mur, objets, textile maison) | `AUDIT_KEYWORDS_COMPLEMENTAIRE_AUTORISE` |
| 3 | **U3 globe/cartographie** | Combler 7 130 nets (globe rotatif/lunaire/relief/décoratif, cartes) | `AUDIT_KEYWORDS_COMPLEMENTAIRE_AUTORISE` |

Plus, en tâche de fond : le **candidat autonome « bijoux pierres naturelles et symboles »**, à
mesurer hors U6, sur le protocole complet.

Le seuil ne bouge pas (30 000 nets, 40 000 en confort), le nettoyage marque/IP/informationnel reste
obligatoire, et une intention n'appartient qu'à un seul univers. Si après consolidation propre les
totaux ne passent pas, les STOP deviennent définitifs — et cette fois ils reposeront sur une mesure,
pas sur sept requêtes.

---

## 7. Point de gouvernance

Les commits de cette session sont répartis sur deux branches : `main` (mes deux premiers commits) et
`codex/niches-univers-20260815` (tout le travail Codex + mon dernier commit, qui a atterri dessus
parce que la branche était active). Tout est sur GitHub, rien n'est perdu, mais **il faudra fusionner
dans `main`** — décision à prendre par Hakim : fusion simple, ou après revue des rapports Codex.

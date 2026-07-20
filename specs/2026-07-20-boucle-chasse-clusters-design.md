# Design — Boucle autonome de chasse aux candidats (volume-first)

Date : 20 juillet 2026
Statut : validé par Hakim (conversation du 20 juillet 2026)
Portée : découverte et qualification de candidats produit jusqu'au niveau « fiche AliExpress vérifiée ». Hors périmètre : phase 5 (marge), commande test, construction boutique, Google Ads.

Complète le design du 17 juillet 2026 ([pipeline agents phases 1 à 5](2026-07-17-pipeline-agents-phases-1-5-design.md)) sans le remplacer : les agents `phase3-demande` à `phase5-marge` restent la référence méthodologique.

## 1. Problème à résoudre

Le pipeline actuel ordonne le travail ainsi : idée → filtre qualitatif → mesure du volume. Le comptage des verdicts du registre au 19 juillet 2026 montre où meurent les candidats :

| Cause de rejet | Ordre de grandeur | Phase |
|---|---|---|
| Volume pertinent insuffisant | ~30 candidats | 3 |
| Domination enseignes / prix indéfendable | ~12 candidats | 2 et analyses broyeur |
| Ticket hors 150–400 € | ~5 candidats | 2 |
| Fournisseur ou conformité | ~3 candidats | 4 |

Le motif dominant est toujours le même : le mot-clé parent affiche 8 000 à 12 000 recherches, mais une fois la SERP nettoyée il ne reste que 1 000 à 4 000 réellement adressables (vitrail, rouet, torréfacteur, hydroponie, mur végétal, meuble de couture, catio).

Autrement dit : **les phases 1 et 2 produisent des idées séduisantes mais non mesurées**, et tout le travail créatif est réalisé avant que le critère le plus éliminatoire soit appliqué. Le taux d'acceptation observé est d'environ 4 % (2 candidats retenus sur ~50 étudiés).

Répéter ce pipeline en boucle produirait bien 15 à 20 candidats, mais en traitant environ 500 idées, dont 96 % de travail jeté.

## 2. Décisions actées

| Question | Décision de Hakim |
|---|---|
| Ordre du pipeline | **Inversé** — le volume est mesuré avant toute idéation produit |
| Objectif de la boucle | **20 candidats retenus** (plancher acceptable : 15) |
| Profondeur par candidat | **Fiche AliExpress vérifiée, sans phase 5** |
| Supervision | **Autonomie totale** jusqu'à 20, arrêt seulement sur blocage |
| Accès données mots-clés | **SEMrush via Chrome** avec compte connecté (à souscrire) |
| Source des idées | **Balayage par familles de marché** (option A), minage de concurrents en source secondaire seulement |

### 2.1 Pourquoi pas un Workflow multi-agents

L'orchestration parallèle a été écartée : toutes les mesures passent par une **session Chrome unique** connectée à SEMrush. Des agents parallèles feraient la queue devant la même ressource — on paierait la complexité sans gagner de vitesse. La boucle est donc **séquentielle**, pilotée par `/loop`, ce qui a deux avantages secondaires : reprise naturelle après interruption et état durable sur disque.

### 2.2 Pourquoi pas le minage de concurrents comme source primaire

Partir des domaines qui vendent déjà la tranche 150–400 € (VEVOR.fr, ManoMano, Aosom, marketplaces) garantit le volume et prouve la monétisation, mais ne trouve que des marchés **déjà occupés par ces acteurs** — précisément ce que rejette le critère de différenciation (§4 de `PRODUCT-RESEARCH-CRITERIA.md`). Ces domaines servent donc à **qualifier** la concurrence sur un cluster déjà trouvé, jamais à générer les candidats.

## 3. Principe central — le Keyword Magic Tool comme générateur d'idées

Le point clé du design : on ne demande pas à un agent d'inventer des produits. On lui donne un **terme d'univers** et SEMrush renvoie 300 à 700 formulations réellement tapées par des Français, avec volumes, CPC, KD, et son propre regroupement automatique en sous-groupes.

Les segments qui en sortent sont des demandes réelles, pas des hypothèses. La boucle ne cherche donc pas des idées : elle cherche du **vocabulaire d'entrée**, ce qui est un problème beaucoup plus facile.

### 3.1 Deux étages d'alimentation

**Étage 1 — familles de marché.** Un fichier `familles-exploration.md` liste ~40 univers, éditable et réordonnable par Hakim. Chaque famille donne plusieurs milliers de mots-clés mesurés.

**Étage 2 — auto-expansion.** Chaque cluster retenu génère ses propres graines à partir des sous-groupes voisins et termes connexes proposés par SEMrush. L'univers s'élargit là où il donne des résultats, ce qui empêche l'assèchement.

Si les 40 familles sont épuisées sans atteindre 20 candidats, le diagnostic n'est plus « manque d'idées » mais « le seuil de 10 000 est trop haut pour le périmètre actuel » — décision qui appartient à Hakim, jamais à la boucle.

### 3.2 Rôle modifié des sources d'idées existantes

Amazon, VEVOR, Europages, Flippa et DotMarket restent au périmètre (§2 de `PRODUCT-RESEARCH-CRITERIA.md`) mais changent de fonction : ils fournissent du **vocabulaire de famille** (noms de catégories, d'usages, de rayons), plus des candidats produit. Coût très inférieur, rendement très supérieur, critère « explorer largement » préservé.

## 4. Architecture

```
Boutiques drop/
├── .claude/
│   ├── skills/
│   │   ├── recherche-produit/SKILL.md        ← orchestrateur existant, inchangé
│   │   └── chasse-clusters/SKILL.md          ← NOUVEAU : corps de la boucle
│   └── agents/
│       ├── phase0-decouverte.md              ← NOUVEAU : balayage SEMrush
│       ├── phase1-ideation.md                ← existant, non appelé par la boucle
│       ├── sonde-prix.md                     ← NOUVEAU : fourchette Google Shopping
│       ├── phase2-filtre.md                  ← existant, réutilisé (filtre qualitatif)
│       ├── phase3-demande.md                 ← existant, réutilisé (nettoyage SERP)
│       ├── phase4-sourcing.md                ← existant, réutilisé (fiches AliExpress)
│       ├── phase5-marge.md                   ← existant, hors périmètre de la boucle
│       └── critique-candidat.md              ← NOUVEAU : contrôle anti-dérive
└── boutique-pipeline/
    ├── PRODUCT-RESEARCH-CRITERIA.md          ← source de vérité, inchangée
    ├── familles-exploration.md               ← NOUVEAU : liste des ~40 familles + état
    ├── registre-candidats.md                 ← existant, étendu d'une section
    └── reports/
        └── chasse-clusters-<famille>-<date>.md
```

### 4.1 `phase0-decouverte` — nouvel agent

**Entrée** : une famille de marché, la date du jour.
**Sortie** : un rapport listant les clusters dont le volume France mesuré atteint le seuil, avec leurs mots-clés constitutifs et volumes.

**Interdits** (mêmes règles d'étanchéité que les autres phases) :

- ne propose aucun produit et ne nomme aucun candidat ;
- ne juge aucune concurrence et ne rend aucun verdict marché ;
- n'estime jamais un volume : toute donnée non lue à l'écran est absente du rapport ;
- n'additionne pas des familles de mots-clés pour atteindre le seuil — l'erreur documentée sur le catio (13 000–17 000 par addition de trois familles, contre 2 400 pour le mot-clé exact) est explicitement citée dans le fichier de l'agent comme anti-exemple.

### 4.2 `critique-candidat` — nouvel agent

Relit `PRODUCT-RESEARCH-CRITERIA.md` et le dossier d'un candidat, puis répond : ce candidat coche-t-il réellement les trois cases (volume, concurrence, fournisseur) ?

**On ne lui communique jamais le compteur** ni le nombre de candidats manquants. C'est le mécanisme central contre la dérive de critères — le risque n°1 d'une boucle autonome poursuivant un objectif chiffré.

Son verdict est binaire : retenu / non retenu. Un « presque » est un non.

### 4.3 `sonde-prix` — nouvel agent

Ajouté le 20 juillet 2026 après le dry-run de la famille 16, qui a produit le cas d'école : `punch needle`, 17 850 recherches — volume supérieur au tufting — mais un ticket réel de 25 à 30 €. Sans sonde, ce constat n'arrivait qu'en phase 3, après un audit SERP complet.

**Entrée** : sur le chemin B, le mot-clé de tête d'un cluster mesuré par la phase 0 ; sur le chemin A, des produits sortis de la phase 2.
**Sortie** : une fourchette de prix lue sur Google Shopping France, et un verdict parmi `DANS LA TRANCHE`, `LOW-TICKET`, `INDÉTERMINÉ`.

**Position sur le chemin B : avant la phase 2** (déplacée le 20/07/2026 après le dry-run de la famille 1). La position initiale — après la phase 2 — laissait le filtre prix de la phase 2 inopérant : sur le chemin B il n'existe aucune phase 1, la phase 0 s'interdit tout prix, et les règles de preuve de la phase 2 lui interdisent d'improviser un ticket. La sonde passe donc en premier, et sa fourchette datée est transmise à la phase 2 comme seule donnée de prix autorisée. Bénéfice secondaire : un cluster low-ticket est écarté avant même la phase 2. Ordre de grandeur : environ 1 % du coût d'une phase 3.

**Asymétrie volontaire des verdicts.** Seul `LOW-TICKET` écarte un produit, et uniquement sur une lecture nette et complète. Toute ambiguïté donne `INDÉTERMINÉ` et le produit continue. Un faux `LOW-TICKET` perdrait un candidat définitivement ; un faux `INDÉTERMINÉ` ne coûte qu'une phase 3. La sonde a le droit de faire gagner du temps, jamais d'en faire perdre.

**Interdits** : ne visite aucun site marchand, ne rend aucun verdict marché, ne compte aucun concurrent, ne mesure aucun volume. Elle lit une page de résultats et en sort.

Nommée sans numéro de phase parce qu'elle sert aussi au pipeline classique `/recherche-produit`, où elle s'insère au même endroit — entre la phase 2 et la phase 3.

### 4.4 Les viviers

Un cluster ou produit `LOW-TICKET` n'est pas rejeté : il entre dans la section « Viviers — volume réel, ticket incompatible » du registre, avec son cluster, son volume mesuré et sa fourchette de prix constatée.

Deuxième source de viviers depuis le 20/07/2026 : les **poches repérées non instruites**. Sur le chemin B, la phase 2 dérive ses produits uniquement du vocabulaire mesuré du cluster (règle de dérivation, §4.5). Quand elle repère un signal qu'elle ne peut pas instruire — segment adjacent, mot-clé à CPC élevé, persona professionnel — elle le liste au lieu de le laisser tomber, et la boucle l'inscrit en vivier avec le motif `poche repérée, non instruite`. Premier cas réel : `outillage frigoriste` (CPC 1,72 €, le plus élevé de la famille 1), repéré pendant un balayage dont tous les candidats sont morts au filtre.

C'est une catégorie distincte des STOP, et l'anti-doublon ne la traite pas comme telle : un vivier peut être repris sans reprise motivée dès qu'un projet de boutique en change le périmètre de prix — typiquement une boutique de niche mêlant machines high-ticket et consommables low-ticket.

Un vivier ne compte pas dans les 20, et ne compte pas non plus comme candidat pour la règle des trois familles stériles : une famille qui ne produit que des viviers reste une famille sans candidat, sinon la boucle pourrait tourner longtemps en accumulant des consolations.

### 4.5 Règle de dérivation des produits (chemin B)

Constat du dry-run famille 1 : la phase 2 recevait un cluster sans qu'aucune méthode ne dise comment en dériver des produits — deux exécutions sur le même cluster auraient donné deux listes différentes, inacceptable en autonomie.

Règle, transmise par la boucle dans chaque brief de phase 2 : **un produit n'est instruit que s'il est attesté par au moins un mot-clé mesuré du cluster.** Aucun produit imaginé hors du vocabulaire mesuré.

Angle mort assumé : le chemin B ne peut structurellement pas produire un candidat que le vocabulaire du marché ne nomme pas encore — c'est le prix de la fiabilité du volume. Le chemin A (phase 1 d'idéation) reste la voie pour ce type de découverte ; les deux chemins ne sont pas interchangeables.

### 4.6 Réutilisation des agents existants

`phase2-filtre` est appelé pour le filtre qualitatif (banalité, valeur perçue, prix cible) ; `phase3-demande` pour le nettoyage SERP et le comptage de concurrents ; `phase4-sourcing` pour les fiches AliExpress. Leurs fichiers ne sont pas modifiés. La boucle leur transmet un cluster déjà mesuré au lieu d'un candidat non mesuré.

`phase1-ideation` n'est pas appelé : sa fonction — générer des idées — est remplacée par `phase0-decouverte`. Il reste disponible pour les recherches lancées à la main via `/recherche-produit`, qui continue de fonctionner à l'identique.

## 5. Séquence de la boucle

```
Tant que (candidats retenus < 20) et (familles non balayées restantes) :

  1. Lire registre-candidats.md et familles-exploration.md
  2. Prendre la famille suivante non balayée
  3. phase0-decouverte  → clusters au-dessus du seuil, mesurés
  4. Anti-doublon contre le registre
     (un STOP ou un rejet documenté n'est jamais re-proposé,
      sauf reprise motivée explicite de Hakim)
  5. Pour chaque cluster survivant :
       a. sonde-prix : lecture Google Shopping France
          sur le mot-clé de tête du cluster
          LOW-TICKET → cluster entier en vivier, on s'arrête là
          DANS LA TRANCHE ou INDÉTERMINÉ → continue,
          fourchette transmise à la phase 2
       b. phase2-filtre : produits qui servent ce cluster,
          filtre banalité / valeur perçue / prix 150–400 €
          (règle de dérivation : produits attestés par un
           mot-clé mesuré uniquement ; poches non instruites
           versées en vivier)
       c. phase3-demande : nettoyage SERP, prix marché,
          comptage concurrents institutionnels vs dropship
       d. phase4-sourcing : 1 à 2 fiches AliExpress ouvertes et vérifiées
          (prix rendu, notation vendeur, délai, entrepôt)
       e. critique-candidat : verdict à froid
       f. si retenu → écriture immédiate au registre, compteur +1
  6. Rapport de famille, marquer la famille comme balayée
  7. Famille suivante
```

## 6. Garde-fous

L'autonomie totale ayant été choisie, trois mécanismes remplacent la supervision humaine.

**Anti-dérive de critères.** L'étape (d) est confiée à un agent distinct, aveugle au compteur, qui relit les critères canoniques à chaque candidat.

**Fail-closed sur les données.** SEMrush déconnecté, CAPTCHA AliExpress, page qui ne charge pas, fichier canonique introuvable → la boucle **s'arrête et le signale**. Aucun volume n'est jamais estimé, aucune donnée inventée pour continuer. C'est la règle existante du pipeline, reprise sans modification.

**État durable.** Le registre est écrit après *chaque* candidat retenu, pas en fin de tour. Une interruption à n'importe quel moment ne perd rien ; relancer reprend où la boucle s'est arrêtée.

## 7. Conditions d'arrêt

La boucle s'arrête dans quatre cas :

1. **20 candidats retenus** — objectif atteint.
2. **Familles épuisées** — rapport de couverture remis à Hakim avec le compte obtenu.
3. **Trois familles consécutives sans aucun candidat** — signal que le seuil de 10 000 est incompatible avec le périmètre. La boucle ne baisse jamais le seuil d'elle-même : elle remonte le constat à Hakim.
4. **Blocage technique** — voir fail-closed ci-dessus.

## 8. Livrable

Une section du registre contenant 15 à 20 lignes comparables, chacune avec :

| Colonne | Contenu |
|---|---|
| Cluster | Mots-clés constitutifs et volume France mesuré, après nettoyage SERP |
| Produit | Le produit qui sert ce cluster, dans la tranche 150–400 € |
| Prix marché | Fourchette constatée en SERP et Shopping |
| Concurrence | Nombre de concurrents institutionnels / nombre de dropshippers identifiés |
| Fournisseur | Lien AliExpress, prix rendu, notation vendeur si elle existe, nombre de commandes, délai, entrepôt |
| Confiance | Niveau A, B ou C (voir §8.1) |
| Réserves | Tout point non vérifié ou conditionnel, jamais supprimé |

### 8.1 La case fournisseur prouve la sourçabilité, pas la qualité du vendeur

Décision de Hakim du 20 juillet 2026. Ce qu'on veut établir est qu'une fiche AliExpress existe et correspond précisément au produit du cluster — Hakim ira vérifier lui-même, quitte à passer une commande test.

Ne sont donc **pas** éliminatoires : une notation vendeur faible ou entre 90 et 95 %, l'absence totale d'avis, une ou deux commandes seulement, une expédition depuis la Chine, un délai long. Ces points se notent et déterminent le niveau de confiance :

| Niveau | Condition |
|---|---|
| A | Avis solides **et** expédition France ou UE |
| B | Une seule des deux forces : avis solides mais expédition Chine, ou pas d'avis mais expédition France/UE |
| C | Ni l'un ni l'autre, mais fiche vérifiée et correspondant au produit |

Le raisonnement du niveau B : un entrepôt européen compense l'absence d'avis, parce qu'il rend le délai vérifiable et le retour praticable. Les deux forces sont considérées comme équivalentes.

Restent strictement éliminatoires : l'absence de fiche, une fiche qui ne correspond pas au produit du cluster (variante incompatible, accessoire, produit voisin), et un prix rendu supérieur ou égal au prix marché constaté.

Conséquence assumée : la boucle produira des candidats de niveau C. Ils partent avec la mention « fournisseur à valider par commande test », jamais gommée.

Hakim choisit ensuite lesquels passent en phase 5. Les niveaux 3 (commande test) et 4 (GO lancement) restent hors d'atteinte de la boucle.

## 9. Attente réaliste

À un rendement estimé de 25 à 40 % (contre ~4 % aujourd'hui), 20 candidats demandent de mesurer et qualifier 50 à 80 clusters.

Répartition attendue du temps :

- **balayage SEMrush : 10–15 %** — un chargement de page rend des centaines de mots-clés d'un coup ;
- **qualification : 85–90 %** — nettoyage SERP par cluster, comptage concurrents, relevé de prix, fiches AliExpress une par une.

Compte plusieurs heures de tournage, probablement réparties sur plusieurs sessions. La reprise sur interruption est prévue pour ça.

## 10. Addendum du 20 juillet 2026 (après-midi) — pivot vers la voie hybride

Après 7 familles balayées (1 candidat retenu, 2 dossiers remontés, arrêt réglementaire sur trois familles consécutives sans candidat retenu), Hakim a décidé de faire des **idées** la source principale, en conservant la discipline de mesure précoce de la boucle.

Bilan qui motive le pivot :

- **Acquis confirmé** : plus aucune mort tardive sur le volume — les rejets se sont déplacés vers le §4 (concurrence), 10 fois moins chers parce que prononcés en phase 2.
- **Défauts constatés** : le balayage traite les familles sans jugement de potentiel (3 familles « machines » verrouillées au §4 broyées en pure perte) ; l'angle mort du §4.5 s'est vérifié — le chemin B ne trouve que ce que le vocabulaire nomme ; la seule vraie trouvaille (fontaine) vient de la famille que Hakim connaissait déjà.

Voie hybride (`/qualifie-idees`, skill dédié) : idée → mesure express (`phase0-decouverte` en mode ciblé + `sonde-prix`) → si le volume et le ticket tiennent, chaîne complète (phases 2, 3, 4, critique, registre). Une idée sans volume meurt en minutes. Toute l'infrastructure de ce design est réutilisée telle quelle ; l'objectif des 20 candidats et le compteur du registre restent communs à tous les chemins. La boucle de balayage reste disponible en voie secondaire, familles choisies à la main.

**Synchronisation Notion (ajoutée le 20/07/2026)** : chaque écriture registre (retenu, vivier, poche, STOP, cas limite) produit sa fiche dans la base Notion « Chasse aux clusters — juillet 2026 » (data source `9490c443-ea82-4102-8b3f-f58cdb9c7dc6`, hub Pipeline Boutiques Drop). Trois règles : le registre local d'abord (source de vérité, Notion = tableau de lecture) ; une panne Notion ne bloque jamais la boucle (fiches manquées consignées dans `notion-sync-pending.md`) ; pas de doublon (mise à jour si la fiche existe).

## 11. Risques connus

| Risque | Traitement |
|---|---|
| Dérive des critères à mesure que les candidats faciles s'épuisent | `critique-candidat` aveugle au compteur |
| Gonflage de volume par addition de familles de mots-clés | Interdit explicite dans `phase0-decouverte`, anti-exemple catio cité |
| Session Chrome perdue en cours de route | Fail-closed, arrêt et signalement |
| Chrome monopolisé pendant que Hakim en a besoin | Accepté : la boucle est interruptible sans perte |
| Familles trop larges donnant des clusters non adressables | Le nettoyage SERP de `phase3-demande` reste obligatoire, jamais court-circuité |
| Le seuil de 10 000 rend l'objectif de 20 inatteignable | Condition d'arrêt n°3 : constat remonté, seuil jamais modifié par la boucle |

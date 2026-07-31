# 18 — DB Industrie : index de passation du second chantier

> Dossier de passation Codex — créé le 2026-07-31 au soir (décision **D-0731-B**, `05-DECISION-LOG.md`) :
> Codex reprend l'orchestration de **toute** la collaboration, DB Industrie compris.
>
> **⚠️ Ce document est un index de passation, pas la documentation du projet.** La documentation vit dans
> le dossier projet `ecommerce-dropshipping` et dans la mémoire Claude dédiée (chemins au §2) — elle devra
> recevoir sa propre passation détaillée **si Hakim le demande**. Tout a été établi ici en **lecture seule** :
> aucune boutique touchée, aucun workflow n8n touché, aucun ordre exécuté.
>
> Étiquettes : mêmes conventions que `00-START-HERE.md`, plus **[MÉMOIRE CLAUDE — ecommerce-dropshipping]**
> (fiches mémoire du projet DB Industrie, hors de ce dépôt) et **[MÉMOIRE — à vérifier]** (affirmation du
> brief de Hakim du 31/07 **sans trace trouvée dans les sources** — à ne pas traiter comme un fait).

---

## 1. Ce qu'est le projet

**DB Industrie** est un distributeur de pièces industrielles (contact opérationnel : Hervé Laskowski).
Le projet est une **automatisation n8n Cloud** de leur boîte mail : un workflow lit les mails entrants
(Gmail trigger), **classe** chaque mail via Claude (publicité / suivi de commande / réponse fournisseur /
demande client), **reconnaît le client EBP** par email, **cherche le produit demandé** dans le catalogue
EBP (Data Tables n8n) ou sur le web (Claude + web_search), et envoie à l'opérateur une proposition
**« PROPOSITION A VALIDER »**. **Jamais d'envoi direct au client — la validation humaine est non
négociable.** Un second workflow envoie des **récapitulatifs quotidiens à 8h, 12h30 et 16h** (Europe/Paris).
[FAIT — mémoire Claude:db-industrie-n8n-workflow.md]

Nuance sur « rédaction de devis » (formulation du brief du 31/07) : dans les sources, le workflow rédige
des **propositions à valider**, pas des devis EBP ; l'écriture de devis dans EBP (via SDK EBP) est un
**chantier prod envisagé** dans le backlog Hervé, jamais implémenté. L'écriture directe en base EBP est
fortement déconseillée par EBP ; le workflow actuel est en **lecture seule** — conforme.
[FAIT — projet:db-industrie/BASCULE_SQL_EBP.md]

## 2. Où vit chaque chose (le projet vit HORS du dépôt `boutique-pipeline`)

| Quoi | Emplacement | Note |
|---|---|---|
| Dossier projet | `/Users/Hakim/Documents/Boutiques drop/ecommerce-dropshipping/` | ⚠️ Le brief du 31/07 disait `/Users/Hakim/ecommerce-dropshipping` — ce chemin n'existe plus ; le dossier a été déplacé sous `Documents/Boutiques drop/` (le nom du dossier mémoire Claude garde la trace de l'ancien chemin). [FAIT — vérifié sur disque 31/07] |
| Doc de bascule prod | `…/ecommerce-dropshipping/db-industrie/BASCULE_SQL_EBP.md` | Seul fichier du sous-dossier `db-industrie/` ; bascules Gmail→Outlook et Data Tables→SQL Server EBP, requêtes SQL prêtes. [FAIT] |
| Snapshot workflow | `…/ecommerce-dropshipping/workflow_poc_GMAIL_oauth_P1.json` | Export du workflow principal **à l'état P1** (2026-07-08) — **antérieur aux P2-P4 et à la migration Sonnet 5** ; ne reflète pas le live. [FAIT — fichier lu] |
| Mémoire Claude du projet | `/Users/Hakim/.claude/projects/-Users-Hakim-ecommerce-dropshipping/memory/` | `MEMORY.md` (index), **`db-industrie-n8n-workflow.md`** (la fiche la plus riche — état, IDs, pièges), **`db-industrie-retours-herve.md`** (backlog gelé). Le reste de la mémoire concerne d'anciens travaux dropshipping du même dossier. [FAIT] |
| Instance n8n | `https://hakimouah.app.n8n.cloud` (n8n Cloud — pas de `fs`) | Compte de Hakim. Un **connecteur MCP n8n** est branché côté Claude Code depuis le 09/07 (agir via `update_workflow`, plus d'export/réimport). Identifiants et credentials **non recopiés** ici (le credential Gmail OAuth2 existe dans n8n ; son ID est noté dans la fiche mémoire). [MÉMOIRE CLAUDE] |
| Reste du dossier projet | scripts/xlsx de recherche produit 2026 (mars-mai), POC Next.js | Sans rapport direct avec DB Industrie — ne pas confondre les deux vies du dossier. [FAIT — listage] |

## 3. État réel (au dernier point documenté : 13/07/2026)

Tout ce qui suit : [FAIT — mémoire Claude:db-industrie-n8n-workflow.md, sauf mention]

- **Workflow principal** « POC DB Industrie - Recherche produit (Gmail OAuth) » — ID n8n **`Mlv6d7d092jkctAn`**,
  vu **`active: true`** via MCP n8n le 09/07 [FAIT — transcription session `11078175-…`]. Versions notées :
  P1 déployé = `554f5a85`, version antérieure restaurable = `bed99bc9`.
- **Workflow récaps** « DB Industrie - Recaps quotidiens » — ID n8n **`O3L4E6Wzq1Q2CHA8`** (crons 8h /
  12h30 / 16h Europe/Paris ; si 0 mail depuis le dernier point, aucun récap envoyé).
- **Data Tables n8n** : `catalogue_articles` (ID `BkzpsCvfZV614jEH`) — **80 025 articles** + 1 ligne
  `__SENTINEL__` à **ne pas supprimer** ; `clients_ebp` (ID `FsI2BeUvgmQmr2RX`) — **963 clients, 580 avec
  email** (+ sentinelle) ; `historique_mails` (ID `24T60oBE5ypPLtVZ`) — historisation + colonne `recap_envoye`.
  - ⚠️ **[CONTRADICTOIRE avec le brief du 31/07]** : le brief dit « ~48 000 lignes » pour le catalogue ;
    les sources disent **80 025** articles importés (sur ~88 000 enregistrements des exports EBP du
    29/06, ~8 400 RTF multi-lignes non importés — le passage au SQL direct rendra le catalogue exhaustif).
    Le chiffre 48 000 n'a **aucune trace** dans les sources.
- **Priorités livrées le 09/07** : P1 (perte de mails en lot corrigée), P2 (transferts illisibles — option
  Simplify), P3 (en-tête enrichi + reconnaissance client EBP), P4 (classification + labels Gmail +
  historisation + workflow récaps). Validé par appels réels.
- **Tests utilisateur** : Hervé, du 9 au 13/07 — classements Publicité et Demandes clients validés ;
  10 points de backlog relevés (voir §6). **Aucune trace postérieure au 13/07 dans les sources locales.**

## 4. Modèles Claude dans les nœuds

- **Live (depuis la migration du 09/07, décision Hakim)** : **`claude-sonnet-5` partout**, y compris la
  classification (ex-Haiku ; nœud renommé « Extraction specs (Claude) » — la règle « Haiku pour le tri »
  est **caduque**). Recherche web : outil `web_search_20260209`. `max_tokens` relevés (2000/2500/4000/2000)
  car Sonnet 5 = thinking adaptatif qui consomme le budget de sortie ; les parseurs filtrent
  `c.type === 'text'`. Tarif intro Sonnet 5 (2 $/10 $ par MTok) **jusqu'au 31/08/2026**, puis 3 $/15 $.
  [MÉMOIRE CLAUDE — db-industrie-n8n-workflow.md]
- **Snapshot local (état P1, antérieur)** : `claude-haiku-4-5-20251001` (Extraction specs) et
  `claude-sonnet-4-6` (Rédiger proposition, Recherche web) — `retryOnFail` 3 tentatives sur les 3 nœuds
  Claude, 2 sur l'envoi Gmail. **Ne pas se fier à ce fichier pour l'état courant.**
  [FAIT — projet:workflow_poc_GMAIL_oauth_P1.json]

## 5. Points de fragilité connus (payés ou observés)

[FAIT — mémoire Claude:db-industrie-n8n-workflow.md, sauf mention]

1. **Mails silencieusement écartés (corrigé P1)** : `.first()` dans les nœuds Code → sur un lot de 5 mails,
   seul le premier était traité, **les 4 autres perdus sans erreur ni e-mail** ; et le Gmail Trigger
   dédupliquant par horodatage, un mail raté **ne revient jamais**. Corrigé par `.all()` +
   `itemMatching(i)`. C'est la trace la plus proche des « retries silencieux sans e-mail livré » du brief
   — la formulation exacte du brief n'a **pas de trace** dans les sources : [MÉMOIRE — à vérifier]
   (autre piste documentée : les nœuds Claude ont `retryOnFail`, un échec des 3 tentatives rend
   l'exécution en erreur — cf. les **12 exécutions en TypeError** pendant le test d'Hervé, point 2).
2. **Format réel du trigger Gmail** : avec `simple:false`, n8n renvoie le format **mailparser**, pas le
   format Gmail API brut → TypeError sur `.match`, **12 exécutions en erreur** pendant le test d'Hervé
   (hotfix 09/07 au soir : nœud « Normaliser mail » multi-format). Leçon : valider avec la sortie RÉELLE
   du trigger. **Ne jamais réactiver l'option Simplify** (elle ne livre que le snippet ~200 caractères).
3. **Anti-boucle par sujet** : filtre sur « PROPOSITION A VALIDER » / « RECAP MAILS DB » — un sujet mal
   formé a déjà fait **retraiter ses propres envois** (constaté exécution 51, 07/07). Toute modification
   des sujets sortants doit repasser par ce filtre.
4. **Bug data historique (corrigé)** : l'ancien catalogue embarqué (800 produits) portait le **prix
   d'achat** en guise de prix de vente. Les Data Tables portent `pv_ht` ET `pa_ht` distincts.
5. **Pièges n8n appris** : `pairedItem` normalisé dans `$input.all()` (utiliser `$('Nœud').itemMatching(i)`) ;
   import bulk → 503 au-delà de ~30 lots rapides (batch 1000-2000 + pauses 2 s) ; MCP
   `add_data_table_rows` max 1000 lignes/appel ; lignes `__SENTINEL__` indispensables au chaînage des items.
6. **Limitations fonctionnelles connues** : pièces jointes (.eml, PDF, images/croquis) **non lues** —
   priorité forte d'Hervé ; clients EBP sans email en base (ex. HYDROMETAL, CLI0854) non reconnus ;
   double traitement d'un mail à investiguer (cas Stéphane Marteel, 09/07 23h47) ; routage catalogue OU
   web **par mail** entier, pas par ligne de demande.
7. **Dépendances externes en attente** : accès SQL Server EBP en lecture (Isocell) — d'ici là, catalogue
   figé aux exports du 29/06 ; **migration Gmail→Outlook** (les employés DB Industrie sont sur Outlook) :
   les 5 nœuds à basculer et les adaptations code sont documentés dans `BASCULE_SQL_EBP.md`, prérequis =
   credential Outlook OAuth2 sur le tenant M365 de DB Industrie — **rien de commencé dans les sources**.
   [FAIT — projet:db-industrie/BASCULE_SQL_EBP.md]

## 6. Backlog gelé — retours d'Hervé (9-13/07)

**10 points, avec cas de référence à inspecter dans les exécutions n8n** — dont : lecture des pièces
jointes (priorité forte), redéfinition de `reponse_fournisseur`, logique de routage du suivi de commande,
traitement par ligne de demande, threading des propositions, renforcement de la recherche EBP avant web
(règle de nommage : réf article = **3 premières lettres du fournisseur + code article fournisseur**,
ex. THU44.393.000 = THUrmetall + 44.393.000). **Consigne explicite de Hakim : NE RIEN IMPLÉMENTER sans sa
validation.** Détail complet : `db-industrie-retours-herve.md` (mémoire Claude).
[FAIT — mémoire Claude:db-industrie-retours-herve.md]

## 7. Ce que cet index n'a PAS pu établir — [MANQUANT]

- **État courant des workflows depuis le 13/07/2026** (dernière trace) : actifs ? exécutions en erreur ?
  volume traité ? — visible uniquement via l'interface ou le MCP n8n, non consulté ici (lecture seule fichiers).
- **Contenu exact des workflows live** : le seul export local est le snapshot P1 pré-migration ; les
  versions live (post P2-P4, Sonnet 5) n'existent que dans n8n Cloud.
- **Trace exacte des « retries silencieux sans e-mail livré »** tels que formulés dans le brief (§5.1).
- **Suite donnée aux tests d'Hervé après le 13/07** (priorisation du backlog, nouveaux retours).
- **Chiffrage / facturation** du projet pour DB Industrie : aucune trace dans les sources consultées.
- **Statut de l'accès SQL Server EBP** (retour d'Isocell) et de la bascule Outlook.
- **Comment Codex accédera à n8n** : le MCP n8n est branché côté Claude Code ; l'équivalent côté Codex
  (API n8n ? MCP ? interface) est à décider avec Hakim — rien dans les sources.

# Google Sheet « Niches SMP » — accès pour une conversation Claude

## Le classeur
- Nom : **Niches SMP** (carnet de recherche de niches, une feuille par niche + index).
- ID : `1x-PDhHNOaIUC_4RQW2xN79BOwyC4wGJnZ18lSO0N3H0`
- URL : https://docs.google.com/spreadsheets/d/1x-PDhHNOaIUC_4RQW2xN79BOwyC4wGJnZ18lSO0N3H0/edit
- Propriétaire : ouahabi.hakim@gmail.com. Créé le 09/09/2026.

## Structure (relevée le 12/09/2026)
- Onglet mode d'emploi (première feuille) : règles, seuils du parc (PRODUIT PUR ≥ 12 500/mois sur le MAX du groupe ; UNIVERS ≥ 37 500/mois consolidé ; bande REVIEW 80–100 %), niveaux (Mot-clé principal / Collection / Produit), statuts (Idée → Mesure en cours → PASS / REVIEW / STOP → Sourcing → GO_FINAL / NO_GO_FINAL).
- `📇 Index` : ligne d'en-tête en ligne 3 ; colonne A = nom exact de l'onglet, le reste remonte par formule (Mode, Marché, Statut, Mot-clé principal, Volume, Seuil, Verdict, Collections, Produits, Produits avec lien, Dernière mise à jour, Note). Niches présentes : « Abri chat extérieur (UK) », « Carport », « Pergola aluminium ».
- `🧩 MODÈLE` : gabarit d'onglet niche. Bloc d'en-tête lignes 1–5 (B2 nom, C3 mode, C4 marché, F3 statut, F4 date, notes ligne 5), en-tête du tableau ligne 6, puis une ligne par mot-clé : A Niveau, B Arborescence, C Mot-clé, D Volume/mois (DataForSEO, jamais SEMrush), E Seuil (formule), F Verdict (formule), G Lien AliExpress, H Prix AliExpress, I Prix cible, J Marge brute (formule), K Notes/source. L'onglet « Carport » ajoute des colonnes L–Q (concurrents 1 et 2, prix, comparable).
- Un onglet par niche, dupliqué depuis le modèle et référencé dans l'Index par son nom exact.

## Lire depuis Claude
Le connecteur claude.ai **Google Drive** lit le classeur en texte (outil `read_file_content` avec l'ID ci-dessus, ~55 000 caractères pour tout le classeur). Il ne sait **pas écrire** dans les cellules (il ne modifie que titre et dossier). Aucun connecteur Google Sheets natif n'existe dans le registre au 12/09/2026.

## Écrire depuis Claude : le pont Apps Script déjà déployé (09/09/2026)
Hakim a déployé dans le classeur une application web Apps Script (source : `boutique-pipeline/tools/sheets-bridge/Code.gs`). Elle est **réutilisable dans n'importe quelle conversation** : c'est une URL publique protégée par un jeton, indépendante de la session Claude.
- Où sont l'URL et le jeton : `ecommerce-dropshipping/.env` (fichier ignoré par git), variables `GSHEET_BRIDGE_URL` et `GSHEET_BRIDGE_TOKEN`.
- Client prêt : `boutique-pipeline/scripts/gsheet_bridge.py` (lit ces deux variables ; les exporter avant : `set -a && . ecommerce-dropshipping/.env && set +a`).
- Contrat : POST JSON `{"token": …, "ops": [ … ]}` → `{"ok": true, "result": [ … ]}` (un résultat par op, dans l'ordre). Actions :
  - `read` `{sheet, range}` → matrice de valeurs ;
  - `write` `{sheet, range:"A8", values:[[…],[…]]}` → écrase le bloc à partir de la cellule ;
  - `clear` `{sheet, range}` → vide le contenu (formules comprises : ne jamais viser E, F, J) ;
  - `duplicate` `{source:"🧩 MODÈLE", name:"Nouvelle niche"}` → crée l'onglet ; ajouter ensuite le nom en colonne A de `📇 Index` par un `write`.
  Une action inconnue renvoie `result: []` sans erreur : vérifier le nom de l'action. Les nombres s'envoient en nombres JSON.
- Exemple : `python3 scripts/gsheet_bridge.py '[{"action":"read","sheet":"Carport","range":"A6:F9"}]'` (testé le 12/09/2026, réponse ok).
- Depuis une conversation qui n'a pas accès à ce Mac (claude.ai sans Claude Code), il faut lui coller l'URL et le jeton ; elle ne pourra les utiliser que si elle dispose d'un outil d'exécution (Claude Code, Cowork). Pour changer de jeton : modifier `TOKEN` dans Apps Script puis « Gérer les déploiements › Nouvelle version », l'URL reste la même.
- Utilisations passées : `analyses/2026-09-09-concurrents-prix/merge_prix.py` et `analyses/2026-09-09-pergola-sourcing/merge.py` (import `gsheet_bridge as g`, `g.call([...])`).

## Règles de fond à rappeler à la conversation
- Volumes = DataForSEO France (UK pour les niches UK), MAX du groupe, jamais une somme de variantes proches.
- Verdict et seuils sont des formules : ne jamais écrire dans E, F, J.
- Les GO restent une décision de Hakim ; la conversation propose, l'Index reflète.
- Prix cible = max(marge 35 % sur prix HT livré ; juste sous le concurrent comparable le moins cher).

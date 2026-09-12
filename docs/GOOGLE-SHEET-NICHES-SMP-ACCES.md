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

## Écrire depuis Claude : pont Apps Script (à déployer une fois par Hakim)
1. Ouvrir le classeur › Extensions › Apps Script, coller `boutique-pipeline/tools/sheets-bridge/Code.gs`, remplacer `TOKEN` par une chaîne longue et aléatoire, enregistrer.
2. Déployer › Nouveau déploiement › type « Application web » › Exécuter en tant que **Moi** › Accès **Tout le monde** › Déployer. Autoriser l'accès demandé. Copier l'URL qui finit par `/exec`.
3. Donner à la conversation Claude : l'URL `/exec` et le jeton. (Ne pas les commiter : les garder dans un gestionnaire de mots de passe ou dans `boutique-pipeline/.env` sous `SHEETS_BRIDGE_URL` et `SHEETS_BRIDGE_TOKEN`, fichier ignoré par git.)
4. Après toute modification du script, refaire « Déployer › Gérer les déploiements › Modifier › Nouvelle version », sinon l'URL sert l'ancienne version.

Contrat d'appel (POST JSON, réponse JSON `{ok, result|error}`) :
```bash
curl -s -L -X POST "$SHEETS_BRIDGE_URL" -H "Content-Type: application/json" -d '{"token":"'"$SHEETS_BRIDGE_TOKEN"'","action":"listTabs"}'
```
- `listTabs` → onglets, lignes, colonnes.
- `read` `{tab, range?, formulas?}` → valeurs (ou formules).
- `write` `{tab, range:"C7", values:[[...]]}` → écrase un bloc à partir de la cellule.
- `append` `{tab, values:[[...]]}` → ajoute après la dernière ligne.
- `insertRows` `{tab, afterRow, values}` → insère des lignes sous une ligne donnée (pour garder l'arbre et les formules E/F/J, copier les formules des lignes voisines ou laisser vides puis recopier).
- `duplicateTemplate` `{name}` → crée un onglet niche depuis « 🧩 MODÈLE » et l'ajoute à l'Index.
- `deleteRows` `{tab, row, count}`.
Le `-L` est obligatoire (Apps Script répond par une redirection 302). Les valeurs numériques s'envoient en nombres JSON, pas en chaînes.

## Règles de fond à rappeler à la conversation
- Volumes = DataForSEO France (UK pour les niches UK), MAX du groupe, jamais une somme de variantes proches.
- Verdict et seuils sont des formules : ne jamais écrire dans E, F, J.
- Les GO restent une décision de Hakim ; la conversation propose, l'Index reflète.
- Prix cible = max(marge 35 % sur prix HT livré ; juste sous le concurrent comparable le moins cher).

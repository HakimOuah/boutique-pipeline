# Carnet d'idées de niches (classeur)

`Idees-de-niches.xlsx` : un onglet par niche (dupliquer « 🧩 MODÈLE »), arborescence mot-clé principal → collections → produits avec volume DataForSEO, seuil et verdict automatiques (PRODUIT PUR 12 500 / UNIVERS 37 500, bande REVIEW −20 %), lien AliExpress, prix fournisseur, prix cible, marge brute HT indicative. Onglet « 🗂 Index » alimenté par formules INDIRECT depuis le nom des onglets.

À importer dans Google Sheets (Fichier › Importer › Importer les données › Remplacer la feuille) : styles, validations, mises en forme conditionnelles et formules sont conservés.

Régénérer : `python3 build_sheet.py` (openpyxl) — généré le 09/09/2026.

## Écriture directe dans le Google Sheet (09/09/2026)

Passerelle Apps Script (`doPost`) déployée par Hakim sur le classeur ; URL et token dans `ecommerce-dropshipping/.env` (`GSHEET_BRIDGE_URL`, `GSHEET_BRIDGE_TOKEN`, jamais versionnés). Client : `scripts/gsheet_bridge.py` — actions `read`, `write`, `clear`, `duplicate`. Piège : le classeur est en locale française ; via `setValues`, les formules doivent utiliser les **noms anglais avec des points-virgules** (`=IF(A8="";"";…)`, `=HYPERLINK(url;texte)`) — les noms français (`SI`) donnent `#NAME?`, les virgules donnent `#ERROR!`.

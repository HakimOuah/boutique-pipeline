/**
 * Pont Google Sheets ↔ Claude — à coller dans Extensions › Apps Script du classeur « Niches SMP ».
 * Déployer : Déployer › Nouveau déploiement › Application web › Exécuter en tant que : Moi ;
 * Accès : Tout le monde. Copier l'URL /exec. Mettre un jeton secret dans TOKEN (long, aléatoire).
 * Chaque appel est un POST JSON : {"token":"…","action":"…", …}. Réponse JSON.
 */
var TOKEN = 'REMPLACER-PAR-UN-JETON-SECRET';

function doPost(e) {
  var out;
  try {
    var req = JSON.parse(e.postData.contents || '{}');
    if (req.token !== TOKEN) return json_({ok: false, error: 'bad token'});
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    switch (req.action) {
      case 'listTabs':
        out = {tabs: ss.getSheets().map(function (s) { return {name: s.getName(), rows: s.getLastRow(), cols: s.getLastColumn()}; })};
        break;
      case 'read': {           // {tab, range?}  → valeurs (formules non évaluées si formulas:true)
        var sh = sheet_(ss, req.tab); var rg = req.range ? sh.getRange(req.range) : sh.getDataRange();
        out = {tab: sh.getName(), range: rg.getA1Notation(), values: req.formulas ? rg.getFormulas() : rg.getValues()};
        break;
      }
      case 'write': {          // {tab, range:"A1", values:[[...],[...]]} écrase le bloc à partir de range
        var sh2 = sheet_(ss, req.tab); var v = req.values;
        sh2.getRange(req.range).offset(0, 0, v.length, v[0].length).setValues(v);
        out = {written: v.length + 'x' + v[0].length, at: req.range};
        break;
      }
      case 'append': {         // {tab, values:[[...],...]} ajoute après la dernière ligne
        var sh3 = sheet_(ss, req.tab); var v2 = req.values; var start = sh3.getLastRow() + 1;
        sh3.getRange(start, 1, v2.length, v2[0].length).setValues(v2);
        out = {appended: v2.length, firstRow: start};
        break;
      }
      case 'insertRows': {     // {tab, afterRow, values:[[...],...]} insère sous une ligne (garde les formules de l'arbre)
        var sh4 = sheet_(ss, req.tab); var v3 = req.values;
        sh4.insertRowsAfter(req.afterRow, v3.length);
        sh4.getRange(req.afterRow + 1, 1, v3.length, v3[0].length).setValues(v3);
        out = {inserted: v3.length, afterRow: req.afterRow};
        break;
      }
      case 'duplicateTemplate': { // {template:"🧩 MODÈLE", name:"Nouvelle niche"} crée l'onglet et l'ajoute à l'index
        var tpl = sheet_(ss, req.template || '🧩 MODÈLE');
        if (ss.getSheetByName(req.name)) return json_({ok: false, error: 'tab exists'});
        var ns = tpl.copyTo(ss).setName(req.name); ns.getRange('B2').setValue(req.name);
        var idx = ss.getSheetByName(req.index || '📇 Index');
        if (idx) { idx.getRange(idx.getLastRow() + 1, 1).setValue(req.name); }
        out = {created: req.name, indexed: !!idx};
        break;
      }
      case 'deleteRows': {     // {tab, row, count}
        var sh5 = sheet_(ss, req.tab); sh5.deleteRows(req.row, req.count || 1);
        out = {deleted: req.count || 1, from: req.row};
        break;
      }
      default: return json_({ok: false, error: 'unknown action'});
    }
    return json_({ok: true, result: out});
  } catch (err) { return json_({ok: false, error: String(err)}); }
}
function doGet(e) { return json_({ok: true, info: 'POST JSON {token, action}. actions: listTabs, read, write, append, insertRows, duplicateTemplate, deleteRows'}); }
function sheet_(ss, name) { var s = ss.getSheetByName(name); if (!s) throw new Error('tab not found: ' + name); return s; }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

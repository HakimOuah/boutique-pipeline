// Passerelle d'écriture pour Claude — source du script DÉPLOYÉ par Hakim le 09/09/2026 dans le classeur « Niches SMP »
// (Extensions › Apps Script › Déployer › Application Web, exécuter en tant que moi, accès Tout le monde).
// URL /exec et jeton : ecommerce-dropshipping/.env (GSHEET_BRIDGE_URL, GSHEET_BRIDGE_TOKEN). Ne jamais les versionner.
var TOKEN = "REMPLACE-MOI-PAR-UNE-CHAINE-ALEATOIRE";

function doPost(e) {
  var body = JSON.parse(e.postData.contents);
  if (body.token !== TOKEN) return json_({ok: false, error: "token"});
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var out = [];
  (body.ops || []).forEach(function (op) {
    var sh = ss.getSheetByName(op.sheet);
    if (op.action === "duplicate") {           // {action:"duplicate", source:"🧩 MODÈLE", name:"Pergola aluminium"}
      var src = ss.getSheetByName(op.source); var copy = src.copyTo(ss).setName(op.name); out.push("dup " + op.name);
    } else if (op.action === "write") {        // {action:"write", sheet:"Carport", range:"A8", values:[[...],[...]]}
      sh.getRange(op.range).offset(0, 0, op.values.length, op.values[0].length).setValues(op.values); out.push("write " + op.sheet + "!" + op.range);
    } else if (op.action === "read") {         // {action:"read", sheet:"Carport", range:"A8:K80"}
      out.push(sh.getRange(op.range).getValues());
    } else if (op.action === "clear") {        // {action:"clear", sheet:"Carport", range:"A8:K200"}
      sh.getRange(op.range).clearContent(); out.push("clear " + op.range);
    }
  });
  return json_({ok: true, result: out});
}
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

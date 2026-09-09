#!/usr/bin/env python3
"""Passerelle d'écriture Google Sheets (Apps Script doPost). Usage :
    python3 scripts/gsheet_bridge.py '<json ops>'      # ops = liste [{action, sheet, range, values}...]
    echo '<json>' | python3 scripts/gsheet_bridge.py -
Lit GSHEET_BRIDGE_URL / GSHEET_BRIDGE_TOKEN dans l'environnement (ecommerce-dropshipping/.env).
"""
import os, sys, json, urllib.request
def call(ops):
    url=os.environ["GSHEET_BRIDGE_URL"]; tok=os.environ["GSHEET_BRIDGE_TOKEN"]
    data=json.dumps({"token":tok,"ops":ops}).encode()
    req=urllib.request.Request(url,data=data,headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=120) as r: return json.loads(r.read().decode())
if __name__=="__main__":
    raw=sys.stdin.read() if sys.argv[1]=="-" else sys.argv[1]
    print(json.dumps(call(json.loads(raw)),ensure_ascii=False)[:4000])

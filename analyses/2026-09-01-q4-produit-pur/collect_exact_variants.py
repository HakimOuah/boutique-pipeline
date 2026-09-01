#!/usr/bin/env python3
import base64,json,os,pathlib,urllib.request
ROOT=pathlib.Path(__file__).resolve().parent
API="https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
def call(words):
 login,pwd=os.environ.get("DATAFORSEO_LOGIN"),os.environ.get("DATAFORSEO_PASSWORD")
 if not login or not pwd: raise SystemExit("Identifiants DataForSEO absents")
 auth="Basic "+base64.b64encode(f"{login}:{pwd}".encode()).decode()
 payload=[{"keywords":words,"location_name":"France","language_name":"French","search_partners":False}]
 req=urllib.request.Request(API,data=json.dumps(payload).encode(),headers={"Authorization":auth,"Content-Type":"application/json"})
 with urllib.request.urlopen(req,timeout=180) as r: body=json.load(r)
 task=body.get("tasks",[{}])[0]
 if task.get("status_code")!=20000 or not task.get("result"): raise SystemExit(f"Échec API: {task.get('status_code')} {task.get('status_message')}")
 return body
words=json.loads((ROOT/"exact-variant-keywords.json").read_text())
pre=call(["tufting"]); main=call(words); post=call(["tufting"])
a=pre["tasks"][0]["result"][0].get("search_volume"); b=post["tasks"][0]["result"][0].get("search_volume")
if a!=12100 or b!=a: raise SystemExit(f"Témoins non conformes: {a}/{b}")
out={"read_date":"2026-09-01","endpoint":"keywords_data/google_ads/search_volume/live","parameters":{"location_name":"France","language_name":"French","search_partners":False},"cost_usd":sum(x.get("cost") or 0 for x in (pre,main,post)),"witness_before":pre,"grouped_control":main,"witness_after":post}
(ROOT/"exact-variant-raw.json").write_text(json.dumps(out,ensure_ascii=False,indent=2))
print("witness",a,b,"cost",out["cost_usd"])
for r in main["tasks"][0]["result"]: print(r.get("keyword"),r.get("search_volume"),r.get("cpc"),r.get("competition"),sep="\t")

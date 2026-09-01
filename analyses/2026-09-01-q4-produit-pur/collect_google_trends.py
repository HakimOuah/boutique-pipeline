#!/usr/bin/env python3
import json, pathlib, urllib.parse, urllib.request, time
ROOT = pathlib.Path(__file__).resolve().parent
TERMS = ["sac a dos compression sous vide", "baking steel", "kit pain levain", "remontoir montre automatique"]
BASE = "https://trends.google.com/trends/api"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/140 Safari/537.36", "Accept-Language": "fr-FR,fr;q=0.9"}

def get_json(url):
    req=urllib.request.Request(url,headers=HEADERS)
    with urllib.request.urlopen(req,timeout=90) as r: text=r.read().decode("utf-8")
    if text.startswith(")]}'"):
        text=text.split("\n",1)[1]
    return json.loads(text)

out={"date":"2026-09-01","geo":"FR","period":"today 5-y","property":"","terms":{}}
for term in TERMS:
    explore_req={"comparisonItem":[{"keyword":term,"geo":"FR","time":"today 5-y"}],"category":0,"property":""}
    url=BASE+"/explore?hl=fr&tz=-120&req="+urllib.parse.quote(json.dumps(explore_req,separators=(",",":")))
    try:
        exp=get_json(url)
        widget=next(w for w in exp.get("widgets",[]) if w.get("id")=="TIMESERIES")
        req_obj=widget["request"]
        timeline_url=BASE+"/widgetdata/multiline?hl=fr&tz=-120&req="+urllib.parse.quote(json.dumps(req_obj,separators=(",",":")))+"&token="+urllib.parse.quote(widget["token"])
        data=get_json(timeline_url)
        points=[]
        for p in data.get("default",{}).get("timelineData",[]):
            values=p.get("value") or []
            points.append({"time":p.get("time"),"formattedTime":p.get("formattedTime"),"value":values[0] if values else None,"isPartial":p.get("isPartial")})
        out["terms"][term]={"status":"ok","points":points,"explore_widget":widget,"timeline_raw":data}
        print(term,"ok",len(points))
    except Exception as e:
        out["terms"][term]={"status":"error","error":type(e).__name__+": "+str(e)}
        print(term,"error",type(e).__name__,str(e))
    time.sleep(1)
(ROOT/"google-trends-raw.json").write_text(json.dumps(out,ensure_ascii=False,indent=2))

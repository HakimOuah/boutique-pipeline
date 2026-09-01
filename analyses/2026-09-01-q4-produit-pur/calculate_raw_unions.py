#!/usr/bin/env python3
import json,pathlib
p=pathlib.Path(__file__).resolve().parent/"labs-clusters.json"
d=json.loads(p.read_text())
cands={
 "sac":["sac compression sous vide","sac de voyage compression"],
 "plaque":["plaque acier cuisson","baking steel"],
 "kit":["kit pain levain","kit boulangerie"],
 "remontoir":["remontoir montre automatique","boite remontoir montre"]
}
for c,seeds in cands.items():
 by={}
 for seed in seeds:
  for g in d[seed]:
   k=g["cle"]
   if k not in by or g["volume"]>by[k]["volume"]: by[k]=g
 print(c,"groups",len(by),"raw_positive_sum",sum(g["volume"] for g in by.values() if g["volume"]>0))
 for g in sorted(by.values(),key=lambda x:-x["volume"])[:25]: print(" ",g["volume"],g["expression"],"|",g["cle"])

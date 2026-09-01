#!/usr/bin/env python3
import json, pathlib
root = pathlib.Path(__file__).resolve().parent
s = json.loads((root / "search-volume-summary.json").read_text())
for r in s["rows"]:
    print(f"{r['keyword']}\t{r.get('search_volume')}\t{r.get('cpc')}\t{r.get('competition')}\t{r.get('language_code')}\t{r.get('location_code')}")

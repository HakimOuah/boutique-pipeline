"""Audit A6 local, sans réseau ni réécriture des sources."""
import csv
import gzip
import hashlib
import importlib.util
import json
from datetime import datetime, timezone
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREV = ROOT.parent / '2026-09-03-qualification-9-produits-pur'
rows = list(csv.DictReader((PREV / 'mots-cles/A6.csv').open()))
core = [r for r in rows if int(r['counted_core_volume'] or 0)]
sources = {}
params = []
for source in sorted({r['source'] for r in core}):
    raw = json.loads(gzip.decompress((ROOT.parent / source).read_bytes()))
    raw_tasks = raw['response']['tasks']
    params.extend([{'source': source, **{k: t.get('data', {}).get(k) for k in ('api', 'function', 'location_code', 'location_name', 'language_code', 'language_name', 'search_partners')}} for t in raw_tasks])
    sources[source] = {r['keyword']: r for t in raw_tasks for r in (t.get('result') or []) if isinstance(r, dict) and 'keyword' in r}
verified = []
for r in core:
    rr = sources[r['source']].get(r['keyword'])
    verified.append({'keyword': r['keyword'], 'volume': int(r['counted_core_volume']), 'raw_volume': rr.get('search_volume') if rr else None})
    assert rr is not None, r['keyword']
    assert int(r['volume']) == rr['search_volume'], r['keyword']
volume = sum(int(r['counted_core_volume']) for r in core)
cpc_rows = [r for r in core if r['cpc']]
cpc_den = sum(int(r['counted_core_volume']) for r in cpc_rows)
cpc = sum(D(r['cpc']) * D(r['counted_core_volume']) for r in cpc_rows) / D(cpc_den)
head = next(r for r in rows if r['keyword'] == 'rasoir de surete')
months = json.loads(head['monthly_searches_json'])
q4 = [D(r['search_volume']) for r in months if r['year'] == 2025 and r['month'] in (10, 11, 12)]
mean = sum((D(r['search_volume']) for r in months), D(0)) / D(len(months))
q4_mean = sum(q4, D(0)) / D(len(q4))
checks = []
for cap in sorted((ROOT / 'concurrence/raw').glob('*/capture.json')):
    meta = json.loads(cap.read_text())
    digest = hashlib.sha256(gzip.decompress((cap.parent / 'page.html.gz').read_bytes())).hexdigest()
    checks.append({'path': str(cap.relative_to(ROOT)), 'hash_matches': digest == meta['sha256'], 'status': meta['status']})
    assert digest == meta['sha256']
spec = importlib.util.spec_from_file_location('a6_economy', ROOT / 'economie-calculs.py')
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
stored = json.loads((ROOT / 'economie-calculs.json').read_text())
recalculated = [{k: v for k, v in module.enrich(s).items() if not k.startswith('_')} for s in module.SCENARIOS]
assert recalculated == stored['scenarios']
independent = []
for price, sav in [(D('69'), D('.05')), (D('99'), D('.05')), (D('119'), D('.03'))]:
    contribution = price / D('1.20') - price * D('.014') - D('.25') - price * sav - D('29.79')
    independent.append({'ttc': str(price), 'contribution': str(contribution), 'be_cvr': str(D('.798') / contribution), 'after_ads_cvr_3pct': str(contribution - D('.798') / D('.03'))})
payload = {
    'audited_at_utc': datetime.now(timezone.utc).isoformat(),
    'source_rows': len(rows), 'unique_keywords': len({r['keyword'] for r in rows}),
    'missing_volumes': sum(not r['volume'] for r in rows),
    'core_group_count': len(core), 'core_volume': volume,
    'conditional_inclusive_volume': sum(int(r['counted_volume'] or 0) for r in rows),
    'excess_over_12500': volume - 12500, 'excess_pct': (volume / 12500 - 1) * 100,
    'sensitivity_remove_security_880_not_new_measure': volume - 880,
    'raw_parameters': params, 'raw_verified_core': verified,
    'cpc_usd_weighted': str(cpc), 'cpc_eur_weighted': str(cpc / D('1.1615')),
    'cpc_coverage': cpc_den / volume,
    'q4_mean': str(q4_mean), 'months_mean': str(mean), 'q4_ratio': str(q4_mean / mean),
    'http_archive_checks': checks, 'economy_scenarios_verified': len(recalculated),
    'independent_economy': independent,
}
(ROOT / 'contradiction-verifications.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(payload, ensure_ascii=False, indent=2))

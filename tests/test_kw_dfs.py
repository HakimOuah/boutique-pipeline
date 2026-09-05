import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "scripts" / "kw_dfs.py"
spec = importlib.util.spec_from_file_location("kw_dfs", SCRIPT)
assert spec is not None and spec.loader is not None
kw_dfs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kw_dfs)


class CachedSeriesTest(unittest.TestCase):
    def test_cached_monthly_series_remains_hashable(self):
        with tempfile.TemporaryDirectory() as cache_dir, patch.object(kw_dfs, "CACHE", cache_dir):
            cache_file = Path(cache_dir) / "tufting_France_French_1_1000.json"
            cache_file.write_text(json.dumps({
                "lignes": [["tufting", 12100, "LOW", 0.42, [100, 200, 300]]],
                "total": 1,
            }), encoding="utf-8")

            lignes, total, cout = kw_dfs.suggestions("tufting")

            self.assertIsInstance(lignes[0][4], tuple)
            self.assertEqual(kw_dfs.dedupliquer(lignes)[0]["volume"], 12100)
            self.assertEqual((total, cout), (1, 0.0))


if __name__ == "__main__":
    unittest.main()


class EvidenceTest(unittest.TestCase):
    def response(self, volume=13500, status=20000, keyword='tufting'):
        import io
        return io.StringIO(json.dumps({'status_code': 20000, 'tasks': [
            {'status_code': status, 'result': [{'keyword': keyword, 'search_volume': volume}]}]}))

    def test_witness_may_evolve_but_must_match_before_after(self):
        with patch.object(kw_dfs, '_auth', return_value='test'), patch.object(
                kw_dfs.urllib.request, 'urlopen', return_value=self.response()):
            self.assertEqual(kw_dfs.verifier_temoin(reference=13500), (13500, True))
        with patch.object(kw_dfs, '_auth', return_value='test'), patch.object(
                kw_dfs.urllib.request, 'urlopen', return_value=self.response(13600)):
            with self.assertRaises(SystemExit):
                kw_dfs.verifier_temoin(reference=13500)

    def test_error_null_zero_and_wrong_keyword_are_not_healthy(self):
        for volume, status, keyword in [(13500, 40200, 'tufting'), (None, 20000, 'tufting'),
                                         (0, 20000, 'tufting'), (13500, 20000, 'other')]:
            with self.subTest(volume=volume, status=status, keyword=keyword):
                with patch.object(kw_dfs, '_auth', return_value='test'), patch.object(
                        kw_dfs.urllib.request, 'urlopen', return_value=self.response(volume, status, keyword)):
                    with self.assertRaises(SystemExit):
                        kw_dfs.verifier_temoin()

    def test_missing_volume_cannot_silently_lower_consolidation(self):
        with self.assertRaises(SystemExit):
            kw_dfs.dedupliquer([('hamac', None, None, None, ())])
        self.assertEqual(kw_dfs.dedupliquer([('hamac', 0, None, None, ())])[0]['volume'], 0)

    def test_suggestions_preserve_missing_data_and_cache_provenance(self):
        import io
        response = {'cost': .13, 'tasks': [{'status_code': 20000, 'result': [
            {'total_count': 1, 'items': [{'keyword': 'hamac', 'keyword_info': {
                'search_volume': None, 'monthly_searches': [{'search_volume': None}]}}]}]}]}
        with tempfile.TemporaryDirectory() as directory, patch.object(kw_dfs, 'CACHE', directory), \
             patch.object(kw_dfs, '_auth', return_value='test'), \
             patch.object(kw_dfs.urllib.request, 'urlopen', return_value=io.StringIO(json.dumps(response))):
            lines, _, _ = kw_dfs.suggestions('hamac', cache=False)
            self.assertIsNone(lines[0][1])
            self.assertEqual(lines[0][4], (None,))
            date = kw_dfs.LAST_PROVENANCE['fetched_at']
            cached, _, cost = kw_dfs.suggestions('hamac')
            self.assertEqual(cached, lines)
            self.assertEqual(cost, 0)
            self.assertEqual(kw_dfs.LAST_PROVENANCE['fetched_at'], date)
            self.assertTrue(kw_dfs.LAST_PROVENANCE['from_cache'])

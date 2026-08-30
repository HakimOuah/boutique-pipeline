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

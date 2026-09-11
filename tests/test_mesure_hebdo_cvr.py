"""CVR hebdo : 100 * commandes / sessions, jamais la conversion_rate Shopify."""
from __future__ import annotations

import importlib.util
from pathlib import Path

_CHEMIN = Path(__file__).resolve().parents[1] / "instrumentation" / "mesure-hebdo.py"
_SPEC = importlib.util.spec_from_file_location("mesure_hebdo", _CHEMIN)
assert _SPEC is not None and _SPEC.loader is not None
mesure_hebdo = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(mesure_hebdo)


def test_cvr_tufteo_w36_trois_commandes_sur_232_sessions():
    assert mesure_hebdo.taux_cvr_pct(3, 232) == 1.2931
    assert mesure_hebdo.nombre(44.90 / 3) == 14.97


def test_cvr_zero_sans_commande_ou_sans_session():
    assert mesure_hebdo.taux_cvr_pct(0, 232) == 0
    assert mesure_hebdo.taux_cvr_pct(3, 0) == 0
    assert mesure_hebdo.taux_cvr_pct("", 232) == 0


def test_conversion_rate_shopify_ne_doit_pas_passer_par_nombre():
    """Régression : ratio 0–1 arrondi à 2 décimales, ou 0 Shopify → cvr_pct 0."""
    ratio = 3 / 232
    assert mesure_hebdo.nombre(ratio) == 0.01
    assert mesure_hebdo.nombre(0.0, "0.0") == 0
    assert mesure_hebdo.taux_cvr_pct(3, 232) != mesure_hebdo.nombre(ratio)
    assert mesure_hebdo.taux_cvr_pct(3, 232) != mesure_hebdo.nombre(0.0, "0.0")

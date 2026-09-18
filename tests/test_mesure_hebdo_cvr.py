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


def test_cvr_tufteo_w37_deux_commandes_sur_117_sessions():
    assert mesure_hebdo.taux_cvr_pct(2, 117) == 1.7094


def test_cvr_zero_sans_commande_ou_sans_session():
    assert mesure_hebdo.taux_cvr_pct(0, 232) == 0
    assert mesure_hebdo.taux_cvr_pct(3, 0) == 0
    assert mesure_hebdo.taux_cvr_pct("", 117) == 0


def test_conversion_rate_shopify_ne_doit_pas_passer_par_nombre():
    """Régression : ratio 0–1 via nombre() → 0 ou 0.01, pas un pourcentage."""
    ratio_w36 = 3 / 232
    ratio_w37 = 2 / 117
    assert mesure_hebdo.nombre(0.0, "0.0") == 0
    assert mesure_hebdo.nombre(ratio_w37) == 0.02
    assert mesure_hebdo.taux_cvr_pct(3, 232) != mesure_hebdo.nombre(ratio_w36)
    assert mesure_hebdo.taux_cvr_pct(2, 117) != mesure_hebdo.nombre(ratio_w37)
    assert mesure_hebdo.taux_cvr_pct(3, 232) != mesure_hebdo.nombre(0.0, "0.0")

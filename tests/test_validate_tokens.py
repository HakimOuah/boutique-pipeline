import json
from pathlib import Path
from scripts.validate_tokens import validate_tokens

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "schema/brand-tokens.schema.json").read_text())
EXAMPLE = json.loads((ROOT / "examples/brand-tokens.example.json").read_text())


def test_valid_tokens_return_no_errors():
    assert validate_tokens(EXAMPLE, SCHEMA) == []


def test_missing_top_key_detected():
    bad = {k: v for k, v in EXAMPLE.items() if k != "colors"}
    errors = validate_tokens(bad, SCHEMA)
    assert any("colors" in e for e in errors)


def test_missing_color_detected():
    bad = json.loads(json.dumps(EXAMPLE))
    del bad["colors"]["accent"]
    errors = validate_tokens(bad, SCHEMA)
    assert any("accent" in e for e in errors)


def test_invalid_hex_detected():
    bad = json.loads(json.dumps(EXAMPLE))
    bad["colors"]["accent"] = "B5651D"  # missing #
    errors = validate_tokens(bad, SCHEMA)
    assert any("accent" in e and "hex" in e.lower() for e in errors)


def test_missing_typography_detected():
    bad = json.loads(json.dumps(EXAMPLE))
    del bad["typography"]["heading"]
    errors = validate_tokens(bad, SCHEMA)
    assert any("heading" in e for e in errors)

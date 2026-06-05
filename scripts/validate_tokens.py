import json
import re
import sys
from pathlib import Path

HEX_RE = re.compile(r"^#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$")


def validate_tokens(tokens: dict, schema: dict) -> list:
    errors = []
    for key in schema["required_top"]:
        if key not in tokens:
            errors.append(f"Clé manquante au niveau racine : '{key}'")
    colors = tokens.get("colors", {})
    for key in schema["required_colors"]:
        if key not in colors:
            errors.append(f"Couleur manquante : '{key}'")
    for key in schema["hex_color_fields"]:
        val = colors.get(key)
        if val is not None and not HEX_RE.match(val):
            errors.append(f"Couleur '{key}' n'est pas un hex valide (#RRGGBB ou #RRGGBBAA) : {val}")
    typo = tokens.get("typography", {})
    for key in schema["required_typography"]:
        if key not in typo:
            errors.append(f"Police manquante : '{key}'")
    return errors


def main(argv):
    if len(argv) != 2:
        print("Usage: validate_tokens.py <brand-tokens.json>", file=sys.stderr)
        return 2
    root = Path(__file__).resolve().parent.parent
    schema = json.loads((root / "schema/brand-tokens.schema.json").read_text())
    tokens = json.loads(Path(argv[1]).read_text())
    errors = validate_tokens(tokens, schema)
    if errors:
        for e in errors:
            print("ERREUR:", e)
        return 1
    print("OK : charte valide.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

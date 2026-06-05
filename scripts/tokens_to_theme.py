import copy
import json
import sys
from pathlib import Path


def _alpha(hex6: str, alpha: str) -> str:
    """Couleur #RRGGBB + suffixe alpha (2 hex) -> #RRGGBBAA."""
    return hex6 + alpha


def build_scheme(colors: dict) -> dict:
    bg = colors["background"]
    text = colors["text"]
    accent = colors["accent"]
    accent_text = colors["accent_text"]
    border = _alpha(text, "17")
    soft_border = _alpha(text, "30")
    return {
        "background": bg,
        "foreground": text,
        "border": border,
        "stars_icons_color": accent,
        "primary_button_background": accent,
        "primary_button_text": accent_text,
        "primary_button_border": accent,
        "secondary_button_background": bg,
        "secondary_button_text": accent,
        "secondary_button_border": soft_border,
        "primary_badge_background": bg,
        "primary_badge_text": text,
        "primary_badge_border": border,
        "secondary_badge_background": accent,
        "secondary_badge_text": accent_text,
        "secondary_badge_border": accent,
        "input_background": bg,
        "input_text_color": text,
        "input_border_color": border,
        "selected_input_background": bg,
        "selected_input_text_color": text,
        "selected_input_border_color": accent,
        "variant_background_color": bg,
        "variant_text_color": text,
        "variant_border_color": border,
        "selected_variant_background_color": accent,
        "selected_variant_text_color": accent_text,
        "selected_variant_border_color": accent,
        "tab_background_color": bg,
        "tab_text_color": text,
        "tab_border_color": border,
        "selected_tab_background_color": accent,
        "selected_tab_text_color": accent_text,
        "selected_tab_border_color": accent,
    }


def font_settings(typography: dict) -> dict:
    return {
        "type_heading_font": typography["heading"],
        "type_subheading_font": typography["subheading"],
        "type_body_font": typography["body"],
        "type_primary_font": typography["body"],
    }


def apply_tokens(tokens: dict, settings_data: dict) -> dict:
    out = copy.deepcopy(settings_data)
    current = out.setdefault("current", {})
    scheme = build_scheme(tokens["colors"])
    schemes = current.setdefault("color_schemes", {})
    target = schemes.setdefault("scheme-1", {"settings": {}})
    target.setdefault("settings", {}).update(scheme)
    current.update(font_settings(tokens["typography"]))
    return out


def main(argv):
    if len(argv) < 3:
        print("Usage: tokens_to_theme.py <brand-tokens.json> <settings_data.json> [--out path]", file=sys.stderr)
        return 2
    tokens = json.loads(Path(argv[1]).read_text())
    settings_path = Path(argv[2])
    raw = settings_path.read_text()
    settings_data = json.loads(raw)
    out = apply_tokens(tokens, settings_data)
    out_path = Path(argv[4]) if len(argv) >= 5 and argv[3] == "--out" else settings_path
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(f"OK : charte appliquée -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

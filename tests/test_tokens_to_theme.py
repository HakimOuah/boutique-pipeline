import json
from pathlib import Path
from scripts.tokens_to_theme import build_scheme, font_settings, apply_tokens

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "examples/brand-tokens.example.json").read_text())


def test_scheme_maps_core_roles():
    s = build_scheme(TOKENS["colors"])
    assert s["background"] == "#FFFFFF"
    assert s["foreground"] == "#2B1D14"
    assert s["primary_button_background"] == "#B5651D"
    assert s["primary_button_text"] == "#FFFFFF"
    assert s["stars_icons_color"] == "#B5651D"


def test_scheme_borders_use_text_with_alpha():
    s = build_scheme(TOKENS["colors"])
    assert s["border"] == "#2B1D1417"
    assert s["secondary_button_border"] == "#2B1D1430"


def test_scheme_has_all_required_keys():
    s = build_scheme(TOKENS["colors"])
    required = {
        "background", "foreground", "border", "stars_icons_color",
        "primary_button_background", "primary_button_text", "primary_button_border",
        "secondary_button_background", "secondary_button_text", "secondary_button_border",
        "primary_badge_background", "primary_badge_text", "primary_badge_border",
        "secondary_badge_background", "secondary_badge_text", "secondary_badge_border",
        "input_background", "input_text_color", "input_border_color",
        "selected_input_background", "selected_input_text_color", "selected_input_border_color",
        "variant_background_color", "variant_text_color", "variant_border_color",
        "selected_variant_background_color", "selected_variant_text_color", "selected_variant_border_color",
        "tab_background_color", "tab_text_color", "tab_border_color",
        "selected_tab_background_color", "selected_tab_text_color", "selected_tab_border_color",
    }
    assert required.issubset(set(s.keys()))


def test_font_settings_map_typography():
    f = font_settings(TOKENS["typography"])
    assert f["type_heading_font"] == "playfair_display_n5"
    assert f["type_subheading_font"] == "work_sans_n4"
    assert f["type_body_font"] == "work_sans_n4"
    assert f["type_primary_font"] == "work_sans_n4"


def test_apply_tokens_injects_scheme_and_fonts():
    settings = {"current": {"color_schemes": {"scheme-1": {"settings": {"background": "#000000"}}}}}
    out = apply_tokens(TOKENS, settings)
    s1 = out["current"]["color_schemes"]["scheme-1"]["settings"]
    assert s1["background"] == "#FFFFFF"
    assert s1["primary_button_background"] == "#B5651D"
    assert out["current"]["type_heading_font"] == "playfair_display_n5"


def test_apply_tokens_does_not_mutate_input():
    settings = {"current": {"color_schemes": {"scheme-1": {"settings": {"background": "#000000"}}}}}
    apply_tokens(TOKENS, settings)
    assert settings["current"]["color_schemes"]["scheme-1"]["settings"]["background"] == "#000000"

import json
from scripts.new_boutique import scaffold


def test_scaffold_creates_expected_files(tmp_path):
    project = scaffold("ma-boutique", tmp_path)
    assert (project / "research-brief.md").exists()
    assert (project / "sitemap.md").exists()
    assert (project / "shot-list.md").exists()
    assert (project / "project-state.md").exists()
    assert (project / "product-page-brief.md").exists()
    assert (project / "test-plan.md").exists()
    assert (project / "brand-tokens.json").exists()
    for name in ("TABLEAU.md", "ETAT.md", "REGLES.md"):
        assert (project / name).is_file()
    for name in ("journal", "backups", "preuves", "livraisons"):
        assert (project / name).is_dir()
    assert (project / "content").is_dir()
    assert (project / "assets/source").is_dir()
    assert (project / "assets/generated").is_dir()
    assert (project / "assets/final").is_dir()
    assert (project / "shopify").is_dir()
    assert (project / "shopify/portable-kit/sections/dp-purchase-support.liquid").exists()


def test_scaffold_brand_tokens_is_valid_json(tmp_path):
    project = scaffold("ma-boutique", tmp_path)
    data = json.loads((project / "brand-tokens.json").read_text())
    assert "colors" in data and "typography" in data
    assert data["brand"]["name"] == "ma-boutique"


def test_scaffold_refuses_existing_dir(tmp_path):
    scaffold("ma-boutique", tmp_path)
    try:
        scaffold("ma-boutique", tmp_path)
        assert False, "doit lever FileExistsError"
    except FileExistsError:
        pass

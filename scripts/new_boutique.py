import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
EXAMPLE_TOKENS = ROOT / "examples/brand-tokens.example.json"


def scaffold(name: str, base_dir: Path) -> Path:
    project = Path(base_dir) / name
    try:
        project.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        raise FileExistsError(f"Le dossier existe déjà : {project}")
    (project / "content").mkdir()
    (project / "assets/source").mkdir(parents=True)
    (project / "assets/generated").mkdir(parents=True)
    (project / "assets/final").mkdir(parents=True)
    (project / "shopify").mkdir()
    shutil.copy(TEMPLATES / "research-brief.template.md", project / "research-brief.md")
    shutil.copy(TEMPLATES / "sitemap.template.md", project / "sitemap.md")
    shutil.copy(TEMPLATES / "shot-list.template.md", project / "shot-list.md")
    shutil.copy(TEMPLATES / "project-state.template.md", project / "project-state.md")
    shutil.copy(TEMPLATES / "product-page-brief.template.md", project / "product-page-brief.md")
    shutil.copy(TEMPLATES / "test-plan.template.md", project / "test-plan.md")
    shutil.copytree(ROOT / "shopify-portable", project / "shopify" / "portable-kit")
    tokens = json.loads(EXAMPLE_TOKENS.read_text())
    tokens["brand"] = {"name": name, "baseline": ""}
    (project / "brand-tokens.json").write_text(json.dumps(tokens, ensure_ascii=False, indent=2) + "\n")
    return project


def main(argv):
    if len(argv) < 2:
        print("Usage: new_boutique.py <nom-projet> [dossier-parent]", file=sys.stderr)
        return 2
    base = Path(argv[2]) if len(argv) >= 3 else Path.cwd()
    project = scaffold(argv[1], base)
    print(f"OK : projet créé -> {project}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

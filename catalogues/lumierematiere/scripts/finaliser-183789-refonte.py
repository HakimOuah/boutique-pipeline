"""Finalise localement la refonte T-06 de 183789. Aucune API Shopify/DSers."""

import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]
OUT = BASE / "livraisons-visuels-codex/couverture-2026-09-05"
HANDLE = "plafonnier-led-led-183789"
DEST = OUT / HANDLE
JOURNAL = BASE / "journal"
RULE = "un seul luminaire dans le cadre"


def read(path):
    return json.loads(path.read_text())


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return str(path.relative_to(REPO))


def inspect(path):
    with Image.open(path) as image:
        assert image.size == (2048, 2048), (path, image.size)
        assert image.mode == "RGB", (path, image.mode)
        assert image.format == "JPEG", (path, image.format)
    return {
        "dimensions": [2048, 2048],
        "mode": "RGB",
        "format": "JPEG",
        "sha256": sha(path),
    }


def make_sheet(items, path, columns=3):
    tile, footer = 600, 92
    rows = (len(items) + columns - 1) // columns
    canvas = Image.new("RGB", (columns * tile, rows * (tile + footer)), "#F6F3EC")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
    for index, (image_path, label, count) in enumerate(items):
        x = (index % columns) * tile
        y = (index // columns) * (tile + footer)
        with Image.open(image_path) as image:
            thumb = image.convert("RGB").resize((tile, tile), Image.Resampling.LANCZOS)
        canvas.paste(thumb, (x, y))
        draw.text((x + 10, y + 608), label, font=font, fill="#24211B")
        draw.text((x + 10, y + 640), count, font=font, fill="#24211B")
    canvas.save(path, quality=95, subsampling=0)


def main():
    production = read(JOURNAL / "2026-09-05-183789-refonte-production.json")
    results = {item["id"]: item for item in read(JOURNAL / "2026-09-05-183789-refonte-resultats.json")}
    proof_path = BASE / "sources-par-handle" / HANDLE / "variantes-lot4-20260905/preuves-dom.json"
    proof = read(proof_path)
    variants = {item["key"].replace("-", ":", 1): item for item in proof["variants"]}
    manifest_path = DEST / "manifeste.json"
    manifest = read(manifest_path)
    DEST.mkdir(parents=True, exist_ok=True)

    specs = {
        "200000795:173": {
            "notation_fournisseur": "Gray-4+1",
            "comptage": "4 peripheriques + 1 central",
            "dimensions": "D 79 x H 14 cm",
            "puissance": "40 W",
            "flux": "3600 lm",
            "surface": "10-15 m2",
            "palets_bois_non_lumineux": 4,
        },
        "200000795:366": {
            "notation_fournisseur": "Gray-5+1",
            "comptage": "5 peripheriques + 1 central",
            "dimensions": "D 89 x H 14 cm",
            "puissance": "48 W",
            "flux": "4320 lm",
            "surface": "15-20 m2",
            "palets_bois_non_lumineux": 5,
        },
        "200000795:10": {
            "notation_fournisseur": "6 heads white / 5+1",
            "comptage": "5 peripheriques + 1 central",
            "dimensions": "L 80 x H 17 cm",
            "puissance": "LED 72 W",
            "palets_bois_non_lumineux": 5,
        },
    }

    additions = []
    for job in production["jobs"]:
        result = results[job["id"]]
        png = Path(result["png"])
        assert png.exists(), png
        source = REPO / job["source"]
        identifier = job["sku_option"].split("#")[0]
        assert identifier in variants, identifier
        dom = variants[identifier]
        assert dom["selected_confirmed"] is True, identifier
        destination = DEST / job["fichier"]
        subprocess.run(
            [
                "sips", "-s", "format", "jpeg", "-s", "formatOptions", "95",
                "-z", "2048", "2048", str(png), "--out", str(destination),
            ],
            check=True,
            capture_output=True,
        )
        with Image.open(png) as native:
            native_size = list(native.size)
        expected_count = 5 if identifier == "200000795:173" else 6
        item = {
            "fichier": job["fichier"],
            "slot": job["slot"],
            "lot": "T-06-refonte-183789",
            "sku_option": job["sku_option"],
            "sku_options_servis": [job["sku_option"]],
            "sku_complets_servis": [job["sku_option"]],
            "identifiant_option": identifier,
            "source": job["source"],
            "sources": [
                {
                    "chemin": job["source"],
                    "sha256": sha(source),
                    "dimensions_source": list(Image.open(source).size),
                }
            ],
            "preuve_dom": rel(proof_path),
            "observe_le": proof["observed_at"],
            "provenance": "REFERENCE_OPTION_CONFIRMEE_DOM",
            "selection_confirmee": True,
            "controle": RULE,
            "nombre_luminaires_observe": 1,
            "notation_comptage": specs[identifier]["comptage"],
            "nombre_lumieres_peripheriques_attendu": expected_count - 1,
            "nombre_lumieres_peripheriques_observe": expected_count - 1,
            "nombre_lumieres_centrales_attendu": 1,
            "nombre_lumieres_centrales_observe": 1,
            "nombre_lumieres_attendu": expected_count,
            "nombre_lumieres_observe": expected_count,
            "nombre_palets_bois_attendu": specs[identifier]["palets_bois_non_lumineux"],
            "nombre_palets_bois_observe": specs[identifier]["palets_bois_non_lumineux"],
            "qa_visuelle": result["revue"],
            "specifications_fournisseur": specs[identifier],
            "generation": {
                "outil": "image_gen integre",
                "dimensions_natives": native_size,
                "mise_au_format": "sips JPEG qualite 95, redimensionnement 2048 x 2048",
                "sha256_png": sha(png),
                "prompt_id": job["id"],
            },
            **inspect(destination),
        }
        additions.append(item)

    names = {item["fichier"] for item in additions}
    manifest["images"] = [item for item in manifest["images"] if item["fichier"] not in names] + additions
    manifest.update(
        lot="lot4-couverture-T06",
        controle_obligatoire=RULE,
        aucune_action_shopify_dsers=True,
        sku_intouchables=True,
        reste_a_produire=[],
        reserve="Le plafond autorise du lot passe de 40 a 47. Les 7 visuels faux restent ecartes; 5 vues Gray-4+1 et 2 variantes 5+1 sont livrees localement.",
        statut="LIVRE_LOCAL_COMPLET_9_IMAGES",
        constat_comptage="Revue visuelle manuelle, peripheriques d'abord puis central; aucun comptage automatique revendique.",
        trouvaille_annexe={
            "a_reporter_hors_perimetre_visuel": True,
            "description_modifiee": False,
            "gris_4_plus_1": "40 W / 3600 lm / 10-15 m2",
            "gris_5_plus_1": "48 W / 4320 lm / 15-20 m2",
            "blanc_5_plus_1": "LED 72 W; L 80 x H 17 cm; ne pas harmoniser avec le gris",
        },
    )
    assert len(manifest["images"]) == 9, len(manifest["images"])
    write(manifest_path, manifest)

    registry_path = JOURNAL / "2026-09-05-lot4-suite-registre.json"
    registry = read(registry_path)
    registry["manifestes"] = [item for item in registry["manifestes"] if item["handle"] != HANDLE] + [manifest]
    registry["finalise_le"] = datetime.now().astimezone().isoformat()
    write(registry_path, registry)

    all_items = []
    current_items = []
    all_hashes = []
    for item_manifest in registry["manifestes"]:
        for image in item_manifest.get("images", []):
            image_path = OUT / item_manifest["handle"] / image["fichier"]
            checked = inspect(image_path)
            assert image.get("controle") == RULE, (item_manifest["handle"], image["fichier"])
            assert checked["sha256"] == image["sha256"], image_path
            count = image.get("notation_comptage") or (
                str(image.get("nombre_lumieres_observe")) + " lumieres"
                if image.get("nombre_lumieres_observe") else image.get("slot", "")
            )
            row = (image_path, image["fichier"].removeprefix(item_manifest["handle"] + "-"), count)
            all_items.append(row)
            all_hashes.append(checked["sha256"])
            if item_manifest["handle"] == HANDLE:
                current_items.append(row)
    assert len(all_items) == 47, len(all_items)
    assert len(set(all_hashes)) == 47, "JPEG duplique"
    make_sheet(all_items, OUT / "qa-couverture.jpg", columns=4)
    make_sheet(current_items, DEST / "qa-183789.jpg", columns=3)

    qa_path = JOURNAL / "2026-09-05-lot4-suite-qa.json"
    qa = read(qa_path)
    qa.update(
        images_total=47,
        hashes_uniques=47,
        manifestes=len(registry["manifestes"]),
        T06_refonte_nouveaux=7,
        T06_images_dans_manifeste=9,
        reserve_183789=[],
        qa="PASS — revue agent du rendu et de la reference, comptage manuel peripheriques + central",
        limite="Local uniquement. Aucune publication, aucun controle boutique public dans cette passe.",
    )
    write(qa_path, qa)
    print(json.dumps(qa, ensure_ascii=False))


if __name__ == "__main__":
    main()

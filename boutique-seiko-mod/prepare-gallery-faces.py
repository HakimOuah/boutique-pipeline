import io
import json
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image, ImageOps


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = PROJECT_ROOT / "scratchpad" / "noirmont-galeries"
SOURCES_PATH = OUTPUT_ROOT / "sources.json"
RAW_ROOT = OUTPUT_ROOT / "entrees-brutes"


def read_source(entry: dict) -> bytes:
    source = entry["source"]
    if entry["sourceKind"] == "cdn":
        request = Request(source, headers={"User-Agent": "Mozilla/5.0 Codex-Noirmont/1.0"})
        with urlopen(request, timeout=60) as response:
            if response.status != 200:
                raise RuntimeError(f"HTTP {response.status}: {source}")
            payload = response.read()
        raw_path = RAW_ROOT / Path(source).name
        raw_path.write_bytes(payload)
        return payload
    return Path(source).read_bytes()


def normalize_face(payload: bytes, destination: Path) -> tuple[int, int]:
    with Image.open(io.BytesIO(payload)) as source:
        source = ImageOps.exif_transpose(source).convert("RGB")
        original_size = source.size
        if source.size != (2048, 2048):
            contained = ImageOps.contain(source, (2048, 2048), Image.Resampling.LANCZOS)
            canvas = Image.new("RGB", (2048, 2048), "#FAFAF7")
            position = (
                (canvas.width - contained.width) // 2,
                (canvas.height - contained.height) // 2,
            )
            canvas.paste(contained, position)
            source = canvas
        source.save(destination, "JPEG", quality=94, subsampling=0, optimize=True)
        return original_size


def main() -> None:
    RAW_ROOT.mkdir(parents=True, exist_ok=True)
    data = json.loads(SOURCES_PATH.read_text())
    results = []
    for index, entry in enumerate(data["entries"], start=1):
        payload = read_source(entry)
        destination = Path(entry["entreeFace"])
        destination.parent.mkdir(parents=True, exist_ok=True)
        original_size = normalize_face(payload, destination)
        results.append({
            "handle": entry["handle"],
            "sourceKind": entry["sourceKind"],
            "source": entry["source"],
            "originalSize": list(original_size),
            "destination": str(destination),
            "bytes": destination.stat().st_size,
        })
        print(f"[{index:02d}/91] {entry['handle']} <- {entry['sourceKind']}")

    (OUTPUT_ROOT / "faces-preparees.json").write_text(
        json.dumps({"count": len(results), "results": results}, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps({
        "prepared": len(results),
        "cdn": sum(result["sourceKind"] == "cdn" for result in results),
        "local": sum(result["sourceKind"] != "cdn" for result in results),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = PROJECT_ROOT / "scratchpad" / "noirmont-galeries"
SOURCES_PATH = OUTPUT_ROOT / "sources.json"
WORKLIST_PATH = OUTPUT_ROOT / "worklist.json"
FACES_ROOT = OUTPUT_ROOT / "entrees-faces"
GENERATED_ROOT = OUTPUT_ROOT / "generated"
EXCLUDED_ROOT = OUTPUT_ROOT / "excluded" / "noirmont-deux-plongeuse-ceramique"

EXCLUDED_HANDLE = "noirmont-deux-plongeuse-ceramique"
SLOT_MAP = {
    "02-situation": "situation",
    "03-macro": "macro",
    "04-poignet": "poignet",
}


def move_without_loss(source: Path, destination: Path) -> None:
    if not source.exists():
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise FileExistsError(f"Destination already exists: {destination}")
    shutil.move(str(source), str(destination))


def main() -> None:
    sources_payload = json.loads(SOURCES_PATH.read_text())
    worklist_payload = json.loads(WORKLIST_PATH.read_text())

    included_entries = []
    for entry in sources_payload["entries"]:
        handle = entry["handle"]
        old_face = Path(entry["entreeFace"])
        if handle == EXCLUDED_HANDLE:
            move_without_loss(old_face, EXCLUDED_ROOT / f"{handle}-face.jpg")
            for old_slot, new_slot in SLOT_MAP.items():
                move_without_loss(
                    GENERATED_ROOT / f"{handle}-{old_slot}.jpg",
                    EXCLUDED_ROOT / f"{handle}-{new_slot}.jpg",
                )
            continue

        new_face = FACES_ROOT / f"{handle}-face.jpg"
        move_without_loss(old_face, new_face)
        entry["entreeFace"] = str(new_face)
        entry["slots"] = [SLOT_MAP.get(slot, slot) for slot in entry["slots"]]
        included_entries.append(entry)

        for old_slot, new_slot in SLOT_MAP.items():
            move_without_loss(
                GENERATED_ROOT / f"{handle}-{old_slot}.jpg",
                GENERATED_ROOT / f"{handle}-{new_slot}.jpg",
            )

    included_jobs = []
    for job in worklist_payload["jobs"]:
        if job["handle"] == EXCLUDED_HANDLE:
            continue
        new_slot = SLOT_MAP.get(job["slot"], job["slot"])
        job["slot"] = new_slot
        job["source"] = str(FACES_ROOT / f"{job['handle']}-face.jpg")
        job["fichier"] = str(GENERATED_ROOT / f"{job['handle']}-{new_slot}.jpg")
        included_jobs.append(job)

    now = datetime.now(timezone.utc).isoformat()
    SOURCES_PATH.write_text(
        json.dumps(
            {
                "generatedAt": now,
                "auditVersion": 3,
                "entries": included_entries,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n"
    )
    WORKLIST_PATH.write_text(
        json.dumps(
            {
                "generatedAt": now,
                "auditVersion": 3,
                "jobs": included_jobs,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n"
    )

    print(
        json.dumps(
            {
                "auditVersion": 3,
                "fichesIncluses": len(included_entries),
                "generationsIncluses": len(included_jobs),
                "handleExclu": EXCLUDED_HANDLE,
                "dossierExclu": str(EXCLUDED_ROOT),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build a read-only inventory of local Maison Noirmont visual assets.

The script never moves, copies, edits, or deletes images.  It only reads local
files and writes the generated JSON inventory next to this script.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from PIL import Image


WORKSPACE = Path(__file__).resolve().parents[2]
OUTPUT = Path(__file__).resolve().with_name("inventaire-assets.json")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

ROOTS = [
    WORKSPACE / "boutique-seiko-mod/livraisons/visuels-codex-2026-08",
    WORKSPACE / "boutique-seiko-mod/livraisons/entrees-faces-REDONDANT-export-claude",
    WORKSPACE / "scratchpad/noirmont-galeries",
    WORKSPACE / "scratchpad/noirmont-accessoires-img",
    WORKSPACE / "scratchpad/lot4-qa",
    WORKSPACE / "scratchpad/noirmont-carte-cadeau",
    WORKSPACE / "scratchpad/pilote29-direct-imagegen-2026-08-11",
    WORKSPACE / "scratchpad/pilote-lumineuses-deterministe-2026-08-11",
    WORKSPACE / "scratchpad/poc-compositing-montes-2026-08-11",
]

REPORT_ROOTS = [
    WORKSPACE / "boutique-seiko-mod/livraisons/visuels-codex-2026-08",
    WORKSPACE / "scratchpad/noirmont-galeries",
    WORKSPACE / "scratchpad/pilote29-direct-imagegen-2026-08-11",
    WORKSPACE / "scratchpad/pilote-lumineuses-deterministe-2026-08-11",
    WORKSPACE / "scratchpad/poc-compositing-montes-2026-08-11",
]

REPORT_FILES = [
    WORKSPACE / "boutique-seiko-mod/RAPPORT-VISUELS-CADRAN-ARABE-1005009751528666-STOP-2026-08-11.json",
    WORKSPACE / "boutique-seiko-mod/RAPPORT-AUDIT-SOURCES-SALMON-PILOTE29-2026-08-11.json",
    WORKSPACE / "boutique-seiko-mod/RAPPORT-REMPLACEMENT92-CADRAN-STERILE-COURONNE-2026-08-11.json",
    WORKSPACE / "boutique-seiko-mod/RAPPORT-AUDIT-SOURCES-PILOTE29-SETS-2026-08-11.json",
    WORKSPACE / "boutique-seiko-mod/RAPPORT-SHOPIFY-REMPLACEMENT92-SUNBURST-VIERGE-24-2026-08-11.json",
]

HANDLE_BY_ACCESSORY_FILE = {
    "jubile-plat-1.jpg": "bracelet-acier-massif-12-22-mm",
    "waffle-1.jpg": "bracelet-caoutchouc-gaufre",
    "noirmont-cuir-daim-1.jpg": "bracelet-cuir-daim-degagement-rapide",
    "noirmont-jubile-904l-1.jpg": "bracelet-jubile-acier-904l-20mm",
    "jubile-courbe-1.jpg": "bracelet-jubile-embouts-courbes",
    "noirmont-milanais-1.jpg": "bracelet-milanais-maille-italienne",
    "coussin-1.jpg": "coussins-de-presentation-lot-de-10",
    "noirmont-doigtiers-1.jpg": "doigtiers-d-horloger-latex",
    "kit-entretien-1.jpg": "kit-d-entretien-13-pieces",
    "noirmont-loupe-1.jpg": "loupe-d-horloger",
    "outil-bracelet-1.jpg": "outil-de-mise-a-taille-de-bracelet",
    "coffret-six-1.jpg": "coffret-6-montres-couvercle-verre",
    "coffret-six-2.jpg": "coffret-6-montres-couvercle-verre",
    "etui-voyage-1.jpg": "etui-de-voyage-rigide",
    "etui-voyage-2.jpg": "etui-de-voyage-rigide",
}

HANDLE_BY_LOT4_MASTER = {
    "904l.png": "bracelet-jubile-acier-904l-20mm",
    "doigtiers.png": "doigtiers-d-horloger-latex",
    "milanais.png": "bracelet-milanais-maille-italienne",
    "daim.png": "bracelet-cuir-daim-degagement-rapide",
    "loupe.png": "loupe-d-horloger",
}

SLOT_WORDS = (
    "situation",
    "macro",
    "poignet",
    "face",
    "variante",
    "hero",
    "detail",
)

REJECT_TOKENS = (
    "fail",
    "reject",
    "rejet",
    "invalid",
    "non_livrable",
    "non-livrable",
    "blocked",
    "abandon",
)
PASS_TOKENS = ("pass", "ready", "valid", "valide", "done", "complete")


def rel(path: Path) -> str:
    return path.resolve().relative_to(WORKSPACE).as_posix()


def image_files() -> list[Path]:
    files: set[Path] = set()
    for root in ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
                files.add(path.resolve())
    return sorted(files, key=lambda p: rel(p))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def image_info(path: Path) -> tuple[int | None, int | None, str | None, str | None]:
    try:
        with Image.open(path) as image:
            return image.width, image.height, image.format, image.mode
    except Exception:
        return None, None, None, None


def status_from(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return "PASS" if value else "REJET"
    normalized = str(value).strip().lower()
    if any(token in normalized for token in REJECT_TOKENS):
        return "REJET"
    if any(token in normalized for token in PASS_TOKENS):
        return "PASS"
    return None


def local_status(record: dict[str, Any]) -> str | None:
    candidates: list[Any] = []
    for key in (
        "verdict",
        "final_verdict",
        "status",
        "qa_status",
        "decision",
        "result",
        "contractual_result",
    ):
        if key in record:
            candidates.append(record[key])
    qa = record.get("qa")
    if isinstance(qa, dict):
        candidates.extend(qa.get(key) for key in ("status", "verdict", "decision"))
    elif qa is not None:
        candidates.append(qa)
    for candidate in candidates:
        result = status_from(candidate)
        if result:
            return result
    return None


def looks_like_image(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    if value.startswith(("http://", "https://")):
        return False
    clean = value.split("?", 1)[0]
    return Path(clean).suffix.lower() in IMAGE_EXTENSIONS


def resolve_reference(value: str, document: Path, handle: str | None) -> Path | None:
    clean = value.split("?", 1)[0]
    candidate = Path(clean)
    attempts: list[Path] = []
    if candidate.is_absolute():
        attempts.append(candidate)
    else:
        attempts.extend((WORKSPACE / candidate, document.parent / candidate))
        if handle:
            attempts.append(WORKSPACE / "boutique-seiko-mod/livraisons/visuels-codex-2026-08" / handle / candidate)
    for attempt in attempts:
        if attempt.exists() and attempt.is_file():
            return attempt.resolve()
    # A few stop reports live at boutique-seiko-mod/ while their outputs live
    # one level deeper under a product handle. Resolve only an unambiguous
    # suffix match; never guess between several products.
    if not candidate.is_absolute():
        visual_root = WORKSPACE / "boutique-seiko-mod/livraisons/visuels-codex-2026-08"
        suffix = candidate.as_posix()
        matches = [
            path.resolve()
            for path in visual_root.rglob(candidate.name)
            if path.is_file() and path.as_posix().endswith(suffix)
        ]
        if len(matches) == 1:
            return matches[0]
    return None


def infer_role(path: Path, reference_key: str | None = None) -> str:
    lowered = rel(path).lower()
    name = path.name.lower()
    if "/rejected/" in lowered or "/excluded/" in lowered:
        return "rejected"
    if reference_key and any(token in reference_key.lower() for token in ("source", "input", "witness")):
        return "source"
    if any(token in lowered for token in ("/entrees-faces", "/entrees-brutes", "/reference/")):
        return "source"
    if any(
        token in name
        for token in (
            "planche",
            "overlay",
            "debug",
            "zoom",
            "controle",
            "grid",
            "mask",
            "masque",
            "crop",
            "difference",
            "heatmap",
            "metrics",
        )
    ) or "/qa/" in lowered:
        return "qa_or_technical"
    if any(
        token in lowered
        for token in ("/generated-raw/", "/raw-generated/", "/raw/", "scratchpad/lot4-qa/")
    ):
        return "generation_intermediate"
    if "/qa-pairs/" in lowered:
        return "qa_or_technical"
    return "deliverable_candidate"


def infer_slot(path: Path, explicit: str | None = None) -> str | None:
    if explicit:
        return explicit
    lowered = path.stem.lower()
    for slot in SLOT_WORDS:
        if re.search(rf"(?:^|[-_]){re.escape(slot)}(?:$|[-_])", lowered):
            return slot
    if "planche" in lowered or "/qa/" in rel(path).lower():
        return "qa"
    return None


def infer_handle(path: Path) -> str | None:
    relative = rel(path)
    prefix = "boutique-seiko-mod/livraisons/visuels-codex-2026-08/"
    if relative.startswith(prefix):
        return relative[len(prefix) :].split("/", 1)[0]
    if path.name in HANDLE_BY_ACCESSORY_FILE:
        return HANDLE_BY_ACCESSORY_FILE[path.name]
    if path.name in HANDLE_BY_LOT4_MASTER:
        return HANDLE_BY_LOT4_MASTER[path.name]
    match = re.search(r"/excluded/([^/]+)/", relative)
    if match:
        return match.group(1)
    return None


def collect_documents() -> list[Path]:
    documents: set[Path] = set()
    for root in REPORT_ROOTS:
        if root.exists():
            for document in root.rglob("*.json"):
                lower = document.name.lower()
                if any(token in lower for token in ("manifest", "manifeste", "rapport", "report", "controle", "qa")):
                    documents.add(document.resolve())
    for document in REPORT_FILES:
        if document.exists():
            documents.add(document.resolve())
    return sorted(documents, key=rel)


def extract_references(
    node: Any,
    document: Path,
    output: dict[Path, list[dict[str, Any]]],
    missing: list[dict[str, Any]],
    context: dict[str, Any] | None = None,
    pointer: str = "$",
    ancestry: tuple[str, ...] = (),
) -> None:
    context = dict(context or {})
    if isinstance(node, dict):
        handle = (
            node.get("handle")
            or node.get("product_handle")
            or node.get("product_handle_reference_only")
            or context.get("handle")
        )
        sku = (
            node.get("sku")
            or node.get("sku_fournisseur")
            or node.get("sku_id")
            or context.get("sku")
        )
        slot = node.get("slot") or context.get("slot")
        appearance = (
            node.get("apparence")
            or node.get("appearance")
            or node.get("variant")
            or node.get("variante")
            or node.get("coloris")
            or node.get("property")
            or node.get("title")
            or context.get("appearance")
        )
        if slot is None and ("variant_id" in node or "source_sku_id" in node or "sku_id" in node):
            slot = "variante"
        own_status = local_status(node)
        inherited_status = context.get("status")
        status = own_status or inherited_status
        next_context = {
            "handle": handle,
            "sku": sku,
            "slot": slot,
            "appearance": appearance,
            "status": status,
        }
        for key, value in node.items():
            child_pointer = f"{pointer}.{key}"
            if looks_like_image(value):
                resolved = resolve_reference(value, document, handle)
                ancestry_text = "/".join(part.lower() for part in ancestry + (key,))
                evidence_status = own_status or inherited_status
                if any(token in ancestry_text for token in ("ecart", "reject", "rejet", "fail", "invalid")):
                    evidence_status = "REJET"
                if resolved and ("/rejected/" in rel(resolved).lower() or "/excluded/" in rel(resolved).lower()):
                    evidence_status = "REJET"
                is_manifest = any(token in document.name.lower() for token in ("manifest", "manifeste"))
                reference_is_output = not any(
                    token in key.lower()
                    for token in ("source", "input", "witness", "temoin", "destination")
                )
                if evidence_status is None and is_manifest and reference_is_output:
                    evidence_status = "PASS"
                evidence = {
                    "document": rel(document),
                    "pointer": child_pointer,
                    "reference_key": key,
                    "qa_status": evidence_status or "INCONNU",
                    "handle": handle,
                    "sku": sku,
                    "slot": slot,
                    "appearance": appearance,
                    "role": infer_role(resolved, key) if resolved else None,
                    "explicit": own_status is not None or any(
                        token in ancestry_text for token in ("ecart", "reject", "rejet", "fail", "invalid")
                    ),
                    "document_mtime_ns": document.stat().st_mtime_ns,
                }
                if resolved:
                    output[resolved].append(evidence)
                else:
                    missing.append(
                        {
                            "document": rel(document),
                            "pointer": child_pointer,
                            "reference": value,
                            "handle": handle,
                            "qa_status": evidence_status or "INCONNU",
                        }
                    )
            elif isinstance(value, (dict, list)):
                extract_references(
                    value,
                    document,
                    output,
                    missing,
                    next_context,
                    child_pointer,
                    ancestry + (key,),
                )
    elif isinstance(node, list):
        for index, value in enumerate(node):
            extract_references(
                value,
                document,
                output,
                missing,
                context,
                f"{pointer}[{index}]",
                ancestry + (str(index),),
            )


def manual_evidence(path: Path) -> list[dict[str, Any]]:
    relative = rel(path)
    evidence: list[dict[str, Any]] = []
    if relative.startswith("scratchpad/noirmont-accessoires-img/") and path.name in HANDLE_BY_ACCESSORY_FILE:
        evidence.append(
            {
                "document": "boutique-seiko-mod/journal/2026-07-31-visuels-accessoires-lot4.md",
                "pointer": "lot4.finales_noirmont",
                "reference_key": "fichier",
                "qa_status": "PASS",
                "handle": HANDLE_BY_ACCESSORY_FILE[path.name],
                "sku": None,
                "slot": "face",
                "appearance": None,
                "role": "deliverable_candidate",
                "explicit": True,
                "document_mtime_ns": 0,
            }
        )
    if relative.startswith("scratchpad/lot4-qa/") and path.name in HANDLE_BY_LOT4_MASTER:
        evidence.append(
            {
                "document": "boutique-seiko-mod/journal/2026-07-31-visuels-accessoires-lot4.md",
                "pointer": "lot4.generations_4k",
                "reference_key": "master_4k",
                "qa_status": "PASS",
                "handle": HANDLE_BY_LOT4_MASTER[path.name],
                "sku": None,
                "slot": "face",
                "appearance": None,
                "role": "generation_master",
                "explicit": True,
                "document_mtime_ns": 0,
            }
        )
    return evidence


def choose_evidence(path: Path, evidence: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not evidence:
        return None
    if "/rejected/" in rel(path).lower() or "/excluded/" in rel(path).lower():
        rejected = [item for item in evidence if item["qa_status"] == "REJET"]
        return (rejected or evidence)[-1]
    ranked = sorted(
        evidence,
        key=lambda item: (
            item["qa_status"] != "INCONNU",
            item.get("explicit", False),
            item.get("document_mtime_ns", 0),
        ),
    )
    return ranked[-1]


def main() -> None:
    files = image_files()
    evidence_by_path: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    missing_references: list[dict[str, Any]] = []
    documents = collect_documents()

    for document in documents:
        try:
            data = json.loads(document.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        extract_references(data, document, evidence_by_path, missing_references)

    assets: list[dict[str, Any]] = []
    paths_by_hash: dict[str, list[str]] = defaultdict(list)
    for path in files:
        file_hash = sha256(path)
        paths_by_hash[file_hash].append(rel(path))
        width, height, image_format, mode = image_info(path)
        evidence = evidence_by_path.get(path, []) + manual_evidence(path)
        chosen = choose_evidence(path, evidence)
        role = chosen.get("role") if chosen and chosen.get("role") else infer_role(path)
        status = chosen.get("qa_status") if chosen else "INCONNU"
        if role == "rejected":
            status = "REJET"
        upload_candidate = status == "PASS" and role == "deliverable_candidate"
        handle = chosen.get("handle") if chosen else None
        slot = chosen.get("slot") if chosen else None
        appearance = chosen.get("appearance") if chosen else None
        sku = chosen.get("sku") if chosen else None
        assets.append(
            {
                "relative_path": rel(path),
                "absolute_path": str(path),
                "handle": handle or infer_handle(path),
                "slot": infer_slot(path, slot),
                "appearance": appearance,
                "sku": sku,
                "dimensions": {"width": width, "height": height},
                "format": image_format or path.suffix.lower().lstrip(".").upper(),
                "mode": mode,
                "bytes": path.stat().st_size,
                "sha256": file_hash,
                "qa": {
                    "status": status,
                    "source": chosen.get("document") if chosen else None,
                    "pointer": chosen.get("pointer") if chosen else None,
                },
                "role": role,
                "upload_candidate": upload_candidate,
                "manifest_references": [
                    {
                        key: item.get(key)
                        for key in (
                            "document",
                            "pointer",
                            "reference_key",
                            "qa_status",
                            "handle",
                            "sku",
                            "slot",
                            "appearance",
                            "role",
                        )
                    }
                    for item in sorted(evidence, key=lambda value: (value["document"], value["pointer"]))
                ],
            }
        )

    duplicate_groups = [
        {"sha256": digest, "paths": paths}
        for digest, paths in sorted(paths_by_hash.items())
        if len(paths) > 1
    ]
    qa_counts = Counter(asset["qa"]["status"] for asset in assets)
    role_counts = Counter(asset["role"] for asset in assets)
    slot_counts = Counter(asset["slot"] or "INCONNU" for asset in assets)
    format_counts = Counter(asset["format"] for asset in assets)
    handles_with_uploads = {
        asset["handle"] for asset in assets if asset["upload_candidate"] and asset["handle"]
    }
    unique_upload_hashes = {
        asset["sha256"] for asset in assets if asset["upload_candidate"]
    }
    assets_by_handle: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for asset in assets:
        if asset["handle"]:
            assets_by_handle[asset["handle"]].append(asset)
    handle_summary = {}
    for handle, handle_assets in sorted(assets_by_handle.items()):
        handle_qa = Counter(asset["qa"]["status"] for asset in handle_assets)
        handle_uploads = [asset for asset in handle_assets if asset["upload_candidate"]]
        handle_summary[handle] = {
            "files": len(handle_assets),
            "qa": dict(sorted(handle_qa.items())),
            "upload_candidates": len(handle_uploads),
            "unique_upload_hashes": len({asset["sha256"] for asset in handle_uploads}),
            "slots_with_upload_candidates": sorted(
                {asset["slot"] or "INCONNU" for asset in handle_uploads}
            ),
            "appearances_with_upload_candidates": sorted(
                {asset["appearance"] for asset in handle_uploads if asset["appearance"]}
            ),
        }

    payload = {
        "schema": "maison-noirmont.asset-inventory.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "workspace_root": str(WORKSPACE),
        "scope": {
            "roots": [rel(root) for root in ROOTS if root.exists()],
            "manifest_or_report_documents_scanned": len(documents),
            "rules": [
                "Aucune image n'est copiee, modifiee ou supprimee.",
                "PASS/REJET vient des manifestes/rapports; sans preuve locale, le statut reste INCONNU.",
                "Les chemins rejected/excluded sont toujours REJET.",
                "upload_candidate exige PASS et un role livrable/master; les planches QA, sources et intermediaires sont exclus.",
                "Les sauvegardes et sources AliExpress brutes (backup-medias, remplacement-photos-aliexpress, resourcing API, lot4-sources) sont volontairement hors perimetre reutilisable.",
            ],
        },
        "summary": {
            "files": len(assets),
            "unique_hashes": len(paths_by_hash),
            "duplicate_groups": len(duplicate_groups),
            "duplicate_file_occurrences": sum(len(group["paths"]) for group in duplicate_groups),
            "qa": dict(sorted(qa_counts.items())),
            "roles": dict(sorted(role_counts.items())),
            "slots": dict(sorted(slot_counts.items())),
            "formats": dict(sorted(format_counts.items())),
            "upload_candidates": sum(asset["upload_candidate"] for asset in assets),
            "unique_upload_candidate_hashes": len(unique_upload_hashes),
            "handles_with_upload_candidates": len(handles_with_uploads),
            "missing_image_references": len(missing_references),
        },
        "assets": assets,
        "handles": handle_summary,
        "duplicate_groups": duplicate_groups,
        "missing_image_references": sorted(
            missing_references,
            key=lambda item: (item["document"], item["pointer"]),
        ),
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

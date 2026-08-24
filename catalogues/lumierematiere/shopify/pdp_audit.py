#!/usr/bin/env python3
"""Dump PDP audit: titres, options, images variantes, sections Full Stack."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import THEME_ID, theme_file  # noqa: E402
from client import gql  # noqa: E402

OUT = ROOT / "pdp-audit.json"


def products() -> list[dict]:
    nodes: list[dict] = []
    cursor = None
    while True:
        data = gql(
            """
            query ($c: String) {
              products(first: 50, after: $c, query: "status:active") {
                pageInfo { hasNextPage endCursor }
                nodes {
                  id handle title
                  seo { title description }
                  featuredImage { url }
                  options { name values }
                  media(first: 12) {
                    nodes {
                      ... on MediaImage { id image { url } }
                    }
                  }
                  variants(first: 80) {
                    nodes {
                      id title
                      selectedOptions { name value }
                      image { url }
                      media(first: 1) {
                        nodes { ... on MediaImage { id image { url } } }
                      }
                    }
                  }
                }
              }
            }
            """,
            {"c": cursor},
        )
        page = data["products"]
        nodes.extend(page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            return nodes
        cursor = page["pageInfo"]["endCursor"]


def main() -> None:
    nodes = products()
    opt_names = Counter()
    n_opts = Counter()
    n_variants = Counter()
    untitled_ref = 0
    no_variant_image = 0
    variant_total = 0
    samples = []
    for p in nodes:
        opts = p.get("options") or []
        n_opts[len(opts)] += 1
        for o in opts:
            opt_names[o["name"]] += 1
        vs = p["variants"]["nodes"]
        n_variants[len(vs)] += 1
        missing = 0
        for v in vs:
            variant_total += 1
            if not (v.get("image") or {}).get("url"):
                no_variant_image += 1
                missing += 1
        title = p["title"] or ""
        if "·" in title or any(ch.isdigit() for ch in title[-6:]):
            untitled_ref += 1
        if len(samples) < 8 or missing == len(vs) or len(vs) > 20:
            samples.append(
                {
                    "handle": p["handle"],
                    "title": title,
                    "seo": p.get("seo"),
                    "options": [{"name": o["name"], "values": o["values"]} for o in opts],
                    "n_variants": len(vs),
                    "n_media": len(p["media"]["nodes"]),
                    "variants_without_image": missing,
                    "variant_titles": [v["title"] for v in vs[:12]],
                }
            )

    tmpl = theme_file("templates/product.json")
    section_types = [(k, v.get("type")) for k, v in tmpl.get("sections", {}).items()]
    order = tmpl.get("order") or list(tmpl.get("sections", {}))
    main = tmpl["sections"].get("main", {})
    block_types = []

    def walk(blocks, prefix=""):
        if not isinstance(blocks, dict):
            return
        for bid, b in blocks.items():
            block_types.append(f"{prefix}{b.get('type')}")
            walk(b.get("blocks") or {}, prefix + "  ")

    walk(main.get("blocks") or {})

    audit = {
        "n_products": len(nodes),
        "option_names": opt_names.most_common(),
        "n_options_dist": n_opts.most_common(),
        "n_variants_dist": sorted(n_variants.items()),
        "titles_with_ref_hint": untitled_ref,
        "variants_total": variant_total,
        "variants_without_image": no_variant_image,
        "product_json_order": order,
        "product_json_section_types": section_types,
        "main_block_types": block_types[:80],
        "samples": samples,
    }
    OUT.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: audit[k] for k in audit if k != "samples"}, ensure_ascii=False, indent=2))
    print("--- samples ---")
    for s in samples[:6]:
        print(s["handle"], "|", s["title"], "| opts", s["options"], "| vars", s["n_variants"], "noimg", s["variants_without_image"])


if __name__ == "__main__":
    main()

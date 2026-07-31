from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import run_pipeline
from .repository import CandidateRepository, transition_status
from .sources.bigbuy import BigBuyClient, fetch_bigbuy_candidates, write_bigbuy_export
from .sources.mapped_file import map_source_file, write_mapped_json
from .automation import process_inbox
from .service import serve
from .ads import import_ad_tests, write_ads_report

ROOT = Path(__file__).resolve().parent.parent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="dropilot", description="Pipeline Google-first de recherche produits")
    parser.add_argument("--db", default=str(ROOT / "data" / "dropilot.sqlite3"))
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init-db", help="Initialiser la base locale")
    init.set_defaults(action="init")

    run = sub.add_parser("run", help="Importer, dédupliquer, scorer et produire les rapports")
    run.add_argument("--input", required=True)
    run.add_argument("--format", choices=["json", "csv", "tsv", "md", "markdown"])
    run.add_argument("--source")
    run.add_argument("--config", default=str(ROOT / "config" / "pipeline.yaml"))
    run.add_argument("--reports", default=str(ROOT / "reports"))
    run.set_defaults(action="run")

    listing = sub.add_parser("list", help="Lister les candidats enregistrés")
    listing.add_argument("--status")
    listing.set_defaults(action="list")

    status = sub.add_parser("status", help="Faire évoluer un candidat dans le pipeline")
    status.add_argument("fingerprint")
    status.add_argument("new_status")
    status.set_defaults(action="status")

    bigbuy = sub.add_parser("bigbuy-fetch", help="Télécharger une taxonomie depuis l’API officielle BigBuy")
    bigbuy.add_argument("--taxonomy", type=int, required=True)
    bigbuy.add_argument("--iso-code", default="fr")
    bigbuy.add_argument("--market", default="FR", choices=["FR", "UK", "DE"])
    bigbuy.add_argument("--base-url", default="https://api.sandbox.bigbuy.eu", choices=["https://api.sandbox.bigbuy.eu", "https://api.bigbuy.eu"])
    bigbuy.add_argument("--out", required=True)
    bigbuy.set_defaults(action="bigbuy")

    mapped = sub.add_parser("map-source", help="Normaliser un export CSV/JSON avec un mapping YAML")
    mapped.add_argument("--input", required=True)
    mapped.add_argument("--mapping", required=True)
    mapped.add_argument("--out", required=True)
    mapped.set_defaults(action="mapped")

    inbox = sub.add_parser("process-inbox", help="Traiter les exports déposés dans la boîte d’entrée")
    inbox.add_argument("--inbox", default=str(ROOT / "data" / "inbox"))
    inbox.add_argument("--config", default=str(ROOT / "config" / "pipeline.yaml"))
    inbox.add_argument("--reports", default=str(ROOT / "reports"))
    inbox.set_defaults(action="inbox")

    server = sub.add_parser("serve", help="Exposer un webhook local pour Hermes ou n8n")
    server.add_argument("--host", default="127.0.0.1")
    server.add_argument("--port", type=int, default=8787)
    server.set_defaults(action="serve")

    ads = sub.add_parser("ads-import", help="Importer un export de performances Google Ads")
    ads.add_argument("--input", required=True)
    ads.add_argument("--report", default=str(ROOT / "reports" / "google-ads.md"))
    ads.set_defaults(action="ads")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repository = CandidateRepository(args.db)
    if args.action == "init":
        repository.initialize()
        print(f"Base initialisée : {args.db}")
        return 0
    if args.action == "list":
        print(json.dumps(repository.list_candidates(args.status), ensure_ascii=False, indent=2))
        return 0
    if args.action == "status":
        transition_status(repository, args.fingerprint, args.new_status)
        print(f"Statut mis à jour : {args.fingerprint} -> {args.new_status}")
        return 0
    if args.action == "bigbuy":
        client = BigBuyClient(base_url=args.base_url)
        candidates = fetch_bigbuy_candidates(client, args.taxonomy, args.iso_code, args.market)
        output = write_bigbuy_export(candidates, args.out)
        print(json.dumps({"products": len(candidates), "output": str(output)}, ensure_ascii=False, indent=2))
        return 0
    if args.action == "mapped":
        rows = map_source_file(args.input, args.mapping)
        output = write_mapped_json(rows, args.out)
        print(json.dumps({"products": len(rows), "output": str(output)}, ensure_ascii=False, indent=2))
        return 0
    if args.action == "inbox":
        outcomes = process_inbox(
            inbox=args.inbox,
            database_path=args.db,
            report_directory=args.reports,
            config_path=args.config,
        )
        print(json.dumps(outcomes, ensure_ascii=False, indent=2))
        return 1 if any(item["status"] == "error" for item in outcomes) else 0
    if args.action == "serve":
        serve(args.host, args.port)
        return 0
    if args.action == "ads":
        outcome = import_ad_tests(args.input, repository)
        report = write_ads_report(repository, args.report)
        print(json.dumps({**outcome, "report": str(report)}, ensure_ascii=False, indent=2))
        return 0
    evaluated, reports = run_pipeline(
        input_path=args.input,
        database_path=args.db,
        report_directory=args.reports,
        source=args.source,
        input_format=args.format,
        config_path=args.config,
    )
    summary = {"shortlist": 0, "review": 0, "reject": 0, "go": 0, "maybe": 0, "no_go": 0}
    for item in evaluated:
        summary[item.result.decision] += 1
        summary[item.result.verdict.lower()] += 1
    print(json.dumps({"summary": summary, "reports": {key: str(value) for key, value in reports.items()}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

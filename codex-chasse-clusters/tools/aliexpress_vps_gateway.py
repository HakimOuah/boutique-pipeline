#!/usr/bin/env python3
"""Call the VPS AliExpress read-only gateway through its forced SSH key.

No shell command is built from user input. The remote key is restricted by
OpenSSH to one JSON gateway that exposes only health, search, variants and
exact-SKU qualification actions.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping


DEFAULT_HOST = "148.230.118.152"
DEFAULT_USER = "root"
DEFAULT_IDENTITY = Path.home() / ".ssh" / "aliexpress_sourcing_vps_ed25519"


class GatewayError(RuntimeError):
    """The local SSH transport or remote read-only gateway failed."""


def build_ssh_command(host: str, user: str, identity: Path) -> list[str]:
    if not re.fullmatch(r"[A-Za-z0-9.-]+", host):
        raise ValueError("Invalid VPS host")
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*", user):
        raise ValueError("Invalid SSH user")
    return [
        "ssh",
        "-T",
        "-i",
        str(identity),
        "-o",
        "IdentitiesOnly=yes",
        "-o",
        "BatchMode=yes",
        "-o",
        "StrictHostKeyChecking=yes",
        "-o",
        "ConnectTimeout=10",
        f"{user}@{host}",
    ]


def call_gateway(
    request: Mapping[str, Any],
    *,
    host: str,
    user: str,
    identity: Path,
    timeout: int = 45,
) -> dict[str, Any]:
    if not identity.is_file():
        raise GatewayError(f"SSH identity not found: {identity}")
    command = build_ssh_command(host, user, identity)
    try:
        completed = subprocess.run(
            command,
            input=json.dumps(dict(request), ensure_ascii=False),
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise GatewayError("VPS gateway timeout") from exc
    try:
        response = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise GatewayError(
            f"VPS gateway returned invalid JSON (ssh_exit={completed.returncode})"
        ) from exc
    if not isinstance(response, dict):
        raise GatewayError("VPS gateway response must be an object")
    if completed.returncode not in (0, 2):
        raise GatewayError(f"SSH transport failed (exit={completed.returncode})")
    return response


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read-only AliExpress sourcing through the whitelisted VPS"
    )
    parser.add_argument(
        "--host", default=os.getenv("ALIEXPRESS_VPS_HOST", DEFAULT_HOST)
    )
    parser.add_argument(
        "--user", default=os.getenv("ALIEXPRESS_VPS_USER", DEFAULT_USER)
    )
    parser.add_argument(
        "--identity",
        type=Path,
        default=Path(os.getenv("ALIEXPRESS_VPS_IDENTITY", DEFAULT_IDENTITY)),
    )
    sub = parser.add_subparsers(dest="action", required=True)

    sub.add_parser("health")

    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=10)
    search.add_argument("--destination", default="FR")
    search.add_argument(
        "--sort-by",
        choices=("orders", "price_asc", "price_desc", "latest"),
        default="orders",
    )

    variants = sub.add_parser("variants")
    variants.add_argument("product_id")

    exact = sub.add_parser("exact")
    exact.add_argument("product_id")
    exact.add_argument("--property", action="append", dest="properties", required=True)
    exact.add_argument("--destination", default="FR")
    return parser


def _request_from_args(args: argparse.Namespace) -> dict[str, Any]:
    request: dict[str, Any] = {"action": args.action}
    if args.action == "search":
        request.update(
            query=args.query,
            limit=args.limit,
            destination=args.destination,
            sort_by=args.sort_by,
        )
    elif args.action == "variants":
        request["product_id"] = args.product_id
    elif args.action == "exact":
        request.update(
            product_id=args.product_id,
            properties=args.properties,
            destination=args.destination,
        )
    return request


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        response = call_gateway(
            _request_from_args(args),
            host=args.host,
            user=args.user,
            identity=args.identity.expanduser(),
        )
    except (GatewayError, OSError, ValueError) as exc:
        print(f"GATEWAY_ERROR: {exc}", file=sys.stderr)
        return 3
    print(json.dumps(response, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if response.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())

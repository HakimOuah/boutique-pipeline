from __future__ import annotations

import hmac
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from .pipeline import run_pipeline


class DropilotHandler(BaseHTTPRequestHandler):
    server_version = "Dropilot/0.1"

    def _json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._json(200, {"status": "ok"})
            return
        self._json(404, {"error": "not_found"})

    def do_POST(self) -> None:
        if self.path != "/run":
            self._json(404, {"error": "not_found"})
            return
        expected = os.getenv("DROPILOT_WEBHOOK_TOKEN", "")
        provided = self.headers.get("Authorization", "").removeprefix("Bearer ").strip()
        if not expected or not hmac.compare_digest(provided, expected):
            self._json(401, {"error": "unauthorized"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            filename = Path(str(payload["input"])).name
            inbox = Path(os.getenv("DROPILOT_INBOX", "data/inbox")).resolve()
            input_path = (inbox / filename).resolve()
            if input_path.parent != inbox or not input_path.is_file():
                raise ValueError("Fichier absent de la boîte d’entrée")
            evaluated, reports = run_pipeline(
                input_path=input_path,
                database_path=os.getenv("DROPILOT_DB", "data/dropilot.sqlite3"),
                report_directory=os.getenv("DROPILOT_REPORTS", "reports"),
                source=payload.get("source"),
                input_format=payload.get("format"),
                config_path=os.getenv("DROPILOT_CONFIG", "config/pipeline.yaml"),
            )
            self._json(200, {"products": len(evaluated), "reports": {key: str(value) for key, value in reports.items()}})
        except (KeyError, ValueError, json.JSONDecodeError) as error:
            self._json(400, {"error": str(error)})
        except Exception:
            self._json(500, {"error": "internal_error"})

    def log_message(self, format: str, *args) -> None:
        return


def serve(host: str = "127.0.0.1", port: int = 8787) -> None:
    ThreadingHTTPServer((host, port), DropilotHandler).serve_forever()


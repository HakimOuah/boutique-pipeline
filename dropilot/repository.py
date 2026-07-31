from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

from .models import ProductCandidate, ScoringResult


SCHEMA = """
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fingerprint TEXT NOT NULL UNIQUE,
    product_name TEXT NOT NULL,
    source TEXT NOT NULL,
    market TEXT NOT NULL,
    status TEXT NOT NULL,
    first_seen_at TEXT NOT NULL,
    last_seen_at TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    scoring_json TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_candidates_status ON candidates(status);
CREATE INDEX IF NOT EXISTS idx_candidates_market ON candidates(market);
CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TEXT NOT NULL,
    source TEXT NOT NULL,
    input_path TEXT NOT NULL,
    received_count INTEGER NOT NULL,
    inserted_count INTEGER NOT NULL,
    duplicate_count INTEGER NOT NULL,
    shortlist_count INTEGER NOT NULL,
    review_count INTEGER NOT NULL,
    reject_count INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS ad_tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fingerprint TEXT NOT NULL,
    campaign_id TEXT NOT NULL,
    market TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT,
    spend REAL NOT NULL DEFAULT 0,
    impressions INTEGER NOT NULL DEFAULT 0,
    clicks INTEGER NOT NULL DEFAULT 0,
    conversions REAL NOT NULL DEFAULT 0,
    revenue REAL NOT NULL DEFAULT 0,
    add_to_cart INTEGER NOT NULL DEFAULT 0,
    checkout INTEGER NOT NULL DEFAULT 0,
    imported_at TEXT NOT NULL,
    UNIQUE(fingerprint, campaign_id, start_date)
);
CREATE INDEX IF NOT EXISTS idx_ad_tests_fingerprint ON ad_tests(fingerprint);
"""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class CandidateRepository:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        finally:
            connection.close()

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.executescript(SCHEMA)

    def upsert(self, fingerprint: str, product: ProductCandidate, result: ScoringResult) -> bool:
        self.initialize()
        now = utc_now()
        payload = json.dumps(product.to_dict(), ensure_ascii=False, sort_keys=True)
        scoring = json.dumps(result.to_dict(), ensure_ascii=False, sort_keys=True)
        with self.connect() as connection:
            existing = connection.execute(
                "SELECT id FROM candidates WHERE fingerprint = ?", (fingerprint,)
            ).fetchone()
            if existing:
                connection.execute(
                    """
                    UPDATE candidates
                    SET last_seen_at = ?, payload_json = ?, scoring_json = ?, status = ?
                    WHERE fingerprint = ?
                    """,
                    (now, payload, scoring, product.status, fingerprint),
                )
                return False
            connection.execute(
                """
                INSERT INTO candidates (
                    fingerprint, product_name, source, market, status,
                    first_seen_at, last_seen_at, payload_json, scoring_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    fingerprint,
                    product.product_name,
                    product.source,
                    product.market,
                    product.status,
                    now,
                    now,
                    payload,
                    scoring,
                ),
            )
            return True

    def record_run(
        self,
        *,
        source: str,
        input_path: str,
        received_count: int,
        inserted_count: int,
        duplicate_count: int,
        decisions: dict[str, int],
    ) -> None:
        self.initialize()
        with self.connect() as connection:
            connection.execute(
                """
                INSERT INTO runs (
                    started_at, source, input_path, received_count, inserted_count,
                    duplicate_count, shortlist_count, review_count, reject_count
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    utc_now(), source, input_path, received_count, inserted_count,
                    duplicate_count, decisions.get("shortlist", 0), decisions.get("review", 0),
                    decisions.get("reject", 0),
                ),
            )

    def list_candidates(self, status: str | None = None) -> list[dict]:
        self.initialize()
        query = "SELECT * FROM candidates"
        params: tuple[str, ...] = ()
        if status:
            query += " WHERE status = ?"
            params = (status,)
        query += " ORDER BY last_seen_at DESC, id DESC"
        with self.connect() as connection:
            rows = connection.execute(query, params).fetchall()
        output = []
        for row in rows:
            item = dict(row)
            item["payload"] = json.loads(item.pop("payload_json"))
            item["scoring"] = json.loads(item.pop("scoring_json"))
            output.append(item)
        return output

    def upsert_ad_test(self, row: dict) -> bool:
        self.initialize()
        with self.connect() as connection:
            existing = connection.execute(
                "SELECT id FROM ad_tests WHERE fingerprint = ? AND campaign_id = ? AND start_date = ?",
                (row["fingerprint"], row["campaign_id"], row["start_date"]),
            ).fetchone()
            values = (
                row["market"], row.get("end_date"), row["spend"], row["impressions"], row["clicks"],
                row["conversions"], row["revenue"], row["add_to_cart"], row["checkout"], utc_now(),
                row["fingerprint"], row["campaign_id"], row["start_date"],
            )
            if existing:
                connection.execute(
                    """
                    UPDATE ad_tests SET market=?, end_date=?, spend=?, impressions=?, clicks=?,
                    conversions=?, revenue=?, add_to_cart=?, checkout=?, imported_at=?
                    WHERE fingerprint=? AND campaign_id=? AND start_date=?
                    """,
                    values,
                )
                return False
            connection.execute(
                """
                INSERT INTO ad_tests (
                    market, end_date, spend, impressions, clicks, conversions, revenue,
                    add_to_cart, checkout, imported_at, fingerprint, campaign_id, start_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                values,
            )
            return True

    def list_ad_tests(self) -> list[dict]:
        self.initialize()
        with self.connect() as connection:
            rows = connection.execute(
                """
                SELECT a.*, c.product_name
                FROM ad_tests a
                LEFT JOIN candidates c ON c.fingerprint = a.fingerprint
                ORDER BY a.start_date DESC, a.id DESC
                """
            ).fetchall()
        return [dict(row) for row in rows]


def transition_status(repository: CandidateRepository, fingerprint: str, new_status: str) -> None:
    allowed = {
        "idea", "prefiltered", "to_analyze", "go", "page_building", "ready",
        "testing", "decision", "rejected", "archived"
    }
    if new_status not in allowed:
        raise ValueError(f"Statut invalide : {new_status}")
    with repository.connect() as connection:
        cursor = connection.execute(
            "UPDATE candidates SET status = ?, last_seen_at = ? WHERE fingerprint = ?",
            (new_status, utc_now(), fingerprint),
        )
        if cursor.rowcount != 1:
            raise KeyError(f"Candidat introuvable : {fingerprint}")

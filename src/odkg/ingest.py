"""Load heterogeneous source records into a small common record format."""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> list[dict[str, Any]]:
    """Load a JSON array or an object containing a ``records`` array."""
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        payload = payload.get("records")
    if not isinstance(payload, list) or not all(isinstance(row, dict) for row in payload):
        raise ValueError("JSON input must be an array of objects or contain a records array")
    return payload


def load_csv(path: str | Path) -> list[dict[str, str]]:
    """Load CSV rows as dictionaries, preserving source column names."""
    with Path(path).open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise ValueError("CSV input must include a header row")
        return [dict(row) for row in reader]


def normalise_record(record: dict[str, Any], source: str, index: int) -> dict[str, Any]:
    """Map source-specific field names to a shared organisation record."""
    name = record.get("organisation_name", record.get("company", record.get("name")))
    identifier = record.get("organisation_id", record.get("company_id", record.get("id")))
    website = record.get("website", record.get("domain", ""))
    country = record.get("country", record.get("country_code", ""))
    if not name or not str(name).strip():
        raise ValueError(f"Record {index} from {source!r} has no organisation name")
    return {
        "source": source,
        "source_record_id": str(identifier if identifier is not None else index),
        "name": str(name).strip(),
        "website": str(website or "").strip().lower(),
        "country": str(country or "").strip().upper(),
    }

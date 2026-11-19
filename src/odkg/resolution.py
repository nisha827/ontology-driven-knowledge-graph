"""Transparent, deterministic entity-resolution baseline."""
from __future__ import annotations

import re
import hashlib
from collections import defaultdict
from typing import Any


def normalise_name(value: str) -> str:
    value = value.casefold().strip()
    value = re.sub(r"\b(incorporated|inc|limited|ltd|llc|plc|corp|corporation)\b", "", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def resolve_entities(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Assign a shared entity key using website first, then normalised name+country.

    This intentionally conservative rule is an interpretable baseline, not a
    production identity-resolution system. Conflicting countries are not merged.
    """
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        website = record.get("website", "").casefold().removeprefix("www.")
        country = record.get("country", "")
        if website:
            key = ("website", website)
        else:
            key = ("name-country", f"{normalise_name(record['name'])}|{country}")
        groups[key].append(record)

    resolved: list[dict[str, Any]] = []
    for key, members in sorted(groups.items(), key=lambda item: item[0]):
        canonical = sorted(members, key=lambda row: (normalise_name(row["name"]), row["source_record_id"]))[0]
        digest = hashlib.sha256(f"{key[0]}:{key[1]}".encode("utf-8")).hexdigest()[:12]
        entity_key = f"org-{digest}"
        for member in members:
            resolved.append({**member, "entity_key": entity_key, "canonical_name": canonical["name"]})
    return resolved

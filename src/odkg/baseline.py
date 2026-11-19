"""A deliberately simple property-graph-style integration baseline."""
from __future__ import annotations
from typing import Any


def build_property_graph(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Return nodes and source edges without ontology semantics or SHACL checks."""
    nodes: dict[str, dict[str, Any]] = {}
    edges: list[dict[str, str]] = []
    for index, row in enumerate(records):
        key = row.get("website") or f"{row['name'].casefold()}|{row.get('country', '')}"
        nodes.setdefault(key, {"label": row["name"], "website": row.get("website", "")})
        edges.append({"source": row["source"], "target": key, "record": str(index)})
    return {"nodes": list(nodes.values()), "edges": edges}

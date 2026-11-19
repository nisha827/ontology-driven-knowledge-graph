"""End-to-end synthetic multi-source integration pipeline."""
from __future__ import annotations
from pathlib import Path
from typing import Any

from .graph import build_graph
from .ingest import load_csv, load_json, normalise_record
from .resolution import resolve_entities


def run_pipeline(json_path: str | Path, csv_path: str | Path, ontology_path: str | Path,
                 output_path: str | Path | None = None) -> dict[str, Any]:
    json_rows = [normalise_record(row, "crm_json", i) for i, row in enumerate(load_json(json_path), 1)]
    csv_rows = [normalise_record(row, "finance_csv", i) for i, row in enumerate(load_csv(csv_path), 1)]
    resolved = resolve_entities(json_rows + csv_rows)
    graph = build_graph(resolved, str(ontology_path))
    if output_path:
        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        graph.serialize(destination=str(target), format="turtle")
    return {"records": len(resolved), "entities": len({r['entity_key'] for r in resolved}),
            "triples": len(graph), "graph": graph, "resolved_records": resolved}

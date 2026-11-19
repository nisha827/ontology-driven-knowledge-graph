from __future__ import annotations
import argparse
from pathlib import Path
from .pipeline import run_pipeline

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the ontology-driven integration demo")
    parser.add_argument("--json", default=str(ROOT / "data/synthetic/crm.json"))
    parser.add_argument("--csv", default=str(ROOT / "data/synthetic/finance.csv"))
    parser.add_argument("--ontology", default=str(ROOT / "ontology/core.ttl"))
    parser.add_argument("--output", default=str(ROOT / "results/integrated-graph.ttl"))
    args = parser.parse_args()
    result = run_pipeline(args.json, args.csv, args.ontology, args.output)
    print(f"Integrated {result['records']} source records into {result['entities']} entities")
    print(f"RDF graph: {result['triples']} triples -> {args.output}")

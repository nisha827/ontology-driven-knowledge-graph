"""RDF graph construction with source-level provenance."""
from __future__ import annotations

from typing import Any
from urllib.parse import quote

from rdflib import Graph, Literal, RDF, URIRef

from .namespaces import DCTERMS, ODKG, PROV, SCHEMA


def build_graph(records: list[dict[str, Any]], ontology_path: str | None = None) -> Graph:
    graph = Graph()
    graph.bind("odkg", ODKG)
    graph.bind("prov", PROV)
    graph.bind("schema", SCHEMA)
    graph.bind("dcterms", DCTERMS)
    if ontology_path:
        graph.parse(ontology_path, format="turtle")

    for row in records:
        organisation = URIRef(f"{ODKG}organisation/{quote(row['entity_key'])}")
        source_record = URIRef(
            f"{ODKG}source-record/{quote(row['source'])}/{quote(row['source_record_id'])}"
        )
        graph.add((organisation, RDF.type, ODKG.Organisation))
        graph.add((organisation, SCHEMA.name, Literal(row["canonical_name"])))
        if row.get("website"):
            graph.add((organisation, SCHEMA.url, URIRef(f"https://{row['website']}")))
        if row.get("country"):
            graph.add((organisation, ODKG.countryCode, Literal(row["country"])))
        graph.add((source_record, RDF.type, PROV.Entity))
        graph.add((source_record, DCTERMS.source, Literal(row["source"])))
        graph.add((source_record, DCTERMS.identifier, Literal(row["source_record_id"])))
        graph.add((organisation, PROV.wasDerivedFrom, source_record))
    return graph

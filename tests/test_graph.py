from rdflib import RDF
from odkg.graph import build_graph
from odkg.namespaces import ODKG, PROV, SCHEMA


def test_graph_contains_organisation_and_provenance():
    records = [{"source": "crm", "source_record_id": "1", "name": "Northstar", "canonical_name": "Northstar", "website": "northstar.example", "country": "US", "entity_key": "org-123"}]
    graph = build_graph(records)
    organisation = next(graph.subjects(RDF.type, ODKG.Organisation))
    assert (organisation, SCHEMA.name, None) in graph
    assert (organisation, PROV.wasDerivedFrom, None) in graph


def test_pipeline_integrates_synthetic_sources(tmp_path):
    from pathlib import Path
    from odkg.pipeline import run_pipeline
    root = Path(__file__).resolve().parents[1]
    output = tmp_path / "integrated.ttl"
    result = run_pipeline(root / "data/synthetic/crm.json", root / "data/synthetic/finance.csv", root / "ontology/core.ttl", output)
    assert result["records"] == 6
    assert result["entities"] == 4
    assert output.exists()


def test_ontology_and_shapes_are_valid_turtle():
    from pathlib import Path
    from rdflib import Graph
    root = Path(__file__).resolve().parents[1]
    assert len(Graph().parse(root / "ontology/core.ttl", format="turtle")) > 0
    assert len(Graph().parse(root / "ontology/shapes.ttl", format="turtle")) > 0

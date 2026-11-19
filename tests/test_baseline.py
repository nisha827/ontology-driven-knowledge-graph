from odkg.baseline import build_property_graph


def test_property_graph_baseline_keeps_source_edges():
    rows = [
        {"source": "crm", "name": "Northstar", "website": "northstar.example", "country": "US"},
        {"source": "finance", "name": "Northstar Analytics", "website": "northstar.example", "country": "US"},
    ]
    result = build_property_graph(rows)
    assert len(result["nodes"]) == 1
    assert len(result["edges"]) == 2

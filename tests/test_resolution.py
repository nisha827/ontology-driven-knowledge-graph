from odkg.resolution import normalise_name, resolve_entities


def test_name_normalisation_removes_company_suffix_and_punctuation():
    assert normalise_name("Northstar Analytics, Inc.") == "northstaranalytics"


def test_records_with_same_domain_resolve_together():
    rows = [
        {"source": "crm", "source_record_id": "1", "name": "Northstar Inc", "website": "northstar.example", "country": "US"},
        {"source": "finance", "source_record_id": "2", "name": "Northstar Analytics", "website": "northstar.example", "country": "US"},
    ]
    resolved = resolve_entities(rows)
    assert len({row["entity_key"] for row in resolved}) == 1
    assert resolved[0]["entity_key"].startswith("org-")


def test_fallback_uses_name_and_country():
    rows = [
        {"source": "a", "source_record_id": "1", "name": "Cedar Labs Inc", "website": "", "country": "CA"},
        {"source": "b", "source_record_id": "2", "name": "Cedar Labs", "website": "", "country": "CA"},
    ]
    assert len({row["entity_key"] for row in resolve_entities(rows)}) == 1


def test_resolution_ids_are_stable_across_runs():
    rows = [{"source": "a", "source_record_id": "1", "name": "Cedar Labs", "website": "cedar.example", "country": "CA"}]
    assert resolve_entities(rows)[0]["entity_key"] == resolve_entities(rows)[0]["entity_key"]

import json
import pytest
from odkg.ingest import load_json, normalise_record


def test_load_json_records(tmp_path):
    path = tmp_path / "input.json"
    path.write_text(json.dumps({"records": [{"id": 1}]}))
    assert load_json(path) == [{"id": 1}]


def test_load_json_rejects_wrong_shape(tmp_path):
    path = tmp_path / "input.json"
    path.write_text('{"unexpected": []}')
    with pytest.raises(ValueError):
        load_json(path)


def test_normalise_record_maps_source_fields():
    row = normalise_record({"company_id": "C1", "company": " Acme ", "domain": "ACME.EXAMPLE", "country": "us"}, "crm", 1)
    assert row == {"source": "crm", "source_record_id": "C1", "name": "Acme", "website": "acme.example", "country": "US"}


def test_normalise_record_requires_name():
    with pytest.raises(ValueError):
        normalise_record({"id": "1"}, "crm", 1)

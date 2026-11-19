"""SHACL validation adapter. Install the ``validation`` extra to enable it."""
from pathlib import Path
from rdflib import Graph


def validate_graph(data_graph: Graph, shapes_path: str | Path) -> tuple[bool, str]:
    try:
        from pyshacl import validate
    except ImportError as exc:  # pragma: no cover - exercised in minimal installs
        raise RuntimeError("Install with `pip install -e '.[validation]'` to run SHACL validation") from exc
    conforms, report_graph, report_text = validate(
        data_graph,
        shacl_graph=str(shapes_path),
        inference="rdfs",
        abort_on_first=False,
        allow_warnings=False,
    )
    return bool(conforms), str(report_text)

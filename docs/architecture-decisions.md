# Architecture decisions

## ADR-001: RDF/OWL as the semantic representation

**Decision:** Use RDFLib and Turtle for the prototype's graph and ontology artefacts.

**Reasoning:** RDF provides globally identifiable resources and interoperable graph statements; OWL can express class/property semantics and support later reasoning. Turtle keeps the artefacts inspectable in code review.

**Trade-off:** RDF can be less familiar than property-graph APIs, and ontology modelling introduces upfront design work. The project therefore includes a simple non-ontology baseline.

## ADR-002: SHACL for data-shape validation

**Decision:** Use SHACL shapes for required names and country-code format.

**Reasoning:** OWL uses open-world semantics and is not a general closed-world validation language. SHACL expresses graph constraints and produces actionable validation reports.

## ADR-003: PROV-O for lineage

**Decision:** Link each canonical organisation to source-record resources with `prov:wasDerivedFrom`.

**Reasoning:** Provenance is represented explicitly rather than being buried in application-only metadata.

## ADR-004: deterministic entity resolution for the first baseline

**Decision:** Match by normalised website/domain where present, otherwise by normalised name and country; use stable SHA-256-derived identifiers.

**Reasoning:** The rule is easy to explain, reproduce and test. It provides a baseline for later comparison with probabilistic and embedding-based methods.

**Known risk:** Shared domains, subsidiaries, renamed entities and missing country values can cause false matches or missed matches. This is not suitable for unsupervised production use.

## ADR-005: defer digital-twin behaviour

**Decision:** Do not label the current graph a digital twin.

**Reasoning:** A digital-twin extension should model versioned entities, state transitions, temporal observations and change impact. The current implementation establishes the semantic and provenance foundation first.

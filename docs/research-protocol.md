# Research protocol

## Problem statement

Organisations often combine records from systems that use different identifiers, field names, granularities and implicit assumptions. Point-to-point mappings can integrate records but make shared meaning, validation and lineage difficult to inspect as the number of sources grows.

## Research question

Can ontology-driven knowledge graphs integrate heterogeneous data sources more reliably than conventional graph-based integration, while preserving provenance, validating relationships and supporting change over time?

## Hypotheses to test

- **H1 — Semantic consistency:** explicit ontology mappings and constraints improve cross-source query correctness compared with a baseline that stores source properties without a shared semantic contract.
- **H2 — Auditability:** explicit provenance links increase the proportion of returned facts that can be traced to their source records.
- **H3 — Data quality:** SHACL constraints detect a higher proportion of seeded structural violations at a measurable false-rejection cost.
- **H4 — Evolution:** versioned mappings and constraints reduce the effort or impact of controlled source-schema changes after an initial modelling investment.

These are hypotheses, not findings.

## Experimental design

1. Create at least three heterogeneous source schemas (for example CRM JSON, finance CSV and a relational export).
2. Generate or curate labelled records with known identity matches, ambiguous names, missing identifiers, conflicting attributes and invalid values.
3. Freeze a conventional integration baseline and an ontology-driven implementation against the same input snapshot.
4. Run controlled perturbations: renamed columns, new optional fields, changed code lists, duplicate entities, missing values and incompatible value types.
5. Evaluate entity matching, query answers, provenance, validation and change effort.
6. Repeat generated experiments across fixed random seeds and retain raw outputs, configuration and environment metadata.

## Baselines and ablations

- Property-graph-style baseline with direct source-to-node mapping.
- Ontology-driven graph without SHACL validation.
- Ontology-driven graph with SHACL validation and provenance.
- Optional entity-resolution ablations: exact domain only, normalised name+country, and a probabilistic matcher.

## Threats to validity

- A tiny synthetic dataset can favour hand-crafted rules and cannot establish real-world generalisation.
- The selected ontology and mappings may encode domain assumptions that do not transfer to other domains.
- Baseline quality strongly affects the comparison; document baseline capabilities and tune fairly.
- Manual mapping effort is subjective; define task boundaries and record time consistently.
- Open-world reasoning and closed-world validation answer different questions; do not conflate OWL inference with SHACL conformance.

## Reproducibility checklist

- [ ] Version and checksum every input dataset.
- [ ] Publish synthetic-data generation parameters and random seeds.
- [ ] Freeze ontology, mapping and SHACL versions for each run.
- [ ] Record Python and dependency versions.
- [ ] Store raw predictions, query outputs and validation reports.
- [ ] Report precision, recall, F1 and confidence intervals where appropriate.
- [ ] Include failed runs and explain exclusions.

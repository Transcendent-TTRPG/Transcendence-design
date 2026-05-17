# Knowledge Layer

This directory defines the project knowledge layer for Transcendence design work.

Its purpose is to stop treating long chat history as project memory and to replace that with explicit, durable, queryable knowledge.

This layer is not a draft scratchpad. It is a maintained system for:

- stable doctrine
- design decisions
- concept definitions
- source-of-truth boundaries
- current project state
- simulation crosswalks

## Why This Exists

The repository now contains enough interdependent rules that design work becomes inefficient when memory is reconstructed from:

- scattered prose docs
- YAML authority data
- corebook output text
- long conversational history

This layer exists to reduce that reconstruction cost.

## Structure

The knowledge layer has two complementary halves:

### `docs/knowledge/`

Human-facing doctrine and governance.

These files explain:

- how the layer is organized
- which documents are authoritative for which questions
- how decisions are recorded
- how concepts are normalized

### `data/knowledge/`

Machine-facing registries.

These files provide structured records for:

- concept definitions
- decision summaries
- source ownership
- project state
- future simulation mappings

## Design Principles

- Knowledge must be durable, not conversational.
- Doctrine must be separable from implementation.
- A concept should have one canonical definition path.
- Decisions should be recorded once and referenced many times.
- Current state should be explicit, not inferred from scattered files.
- Simulation-facing abstractions should trace back to canon design sources.

## What Belongs Here

This layer should store:

- stable doctrine that affects many files
- project-wide terminology
- source ownership rules
- design decisions after they are accepted
- active completion state of major systems
- crosswalks that help the simulator interpret canon rules

This layer should not store:

- raw brainstorming
- duplicate full copies of system chapters
- unpublished alternative drafts unless explicitly marked
- implementation code

## Relationship to ADRs

`docs/adr/` remains the place for formal design decisions in ADR format.

The knowledge layer does not replace ADRs.

Instead:

- ADRs capture and justify major decisions
- the knowledge layer normalizes their outcomes into reusable project memory

## Relationship to Authority Sources

Primary design authority still lives in:

- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`

The knowledge layer does not replace those sources.

It exists to make them easier to interpret consistently.

## First Intended Uses

This layer should immediately support:

- simulator domain modeling
- technique and ailment doctrine consistency
- state taxonomy consistency
- concealment vs ailment boundaries
- species coverage tracking

## Companion Files

- [GOVERNANCE.md](/Users/juangomez/Transcendence-workspace/Transcendence-design/docs/knowledge/GOVERNANCE.md)
- [CONCEPT-MODEL.md](/Users/juangomez/Transcendence-workspace/Transcendence-design/docs/knowledge/CONCEPT-MODEL.md)
- [SOURCE-OF-TRUTH.md](/Users/juangomez/Transcendence-workspace/Transcendence-design/docs/knowledge/SOURCE-OF-TRUTH.md)

# Knowledge Access Architecture

## Purpose

This document defines the local retrieval layer used across the Transcendence project.

The goal is to make project knowledge queryable without relying on:

- long chat history
- repeated full-file rereads
- improvised manual reconstruction

This layer is intentionally local and deterministic. It is not an embedding system yet.

## Scope

This layer is project-wide.

It exists to support:

- design work
- system doctrine review
- corebook consistency work
- species authoring
- simulator design and execution
- future validation and tooling

The simulator is only one consumer of this layer.

## Why a Local Retrieval Layer Comes First

Before semantic indexing, the project needs:

- normalized concepts
- normalized decisions
- normalized source ownership
- stable manifests
- predictable lookup order

Without those, embeddings would only index repository drift more efficiently.

## What This Layer Should Do

The retrieval layer should answer questions such as:

- Which files matter for this concept?
- Which decisions constrain this subsystem?
- What is the preferred lookup order for this question?
- Which compact structured registry should be read before long prose docs?
- Which authority files should a tool derive from?

## What This Layer Should Not Do

It should not:

- replace canon authority
- invent new rule truth
- duplicate whole chapters
- do semantic vector search yet

## Retrieval Philosophy

Local retrieval should be:

- explicit
- stable
- low-token
- source-aware
- domain-aware

This means retrieval is guided by manifests and registries before it is guided by fuzzy similarity.

## Retrieval Units

The system should retrieve knowledge through these units:

### 1. Concepts

Examples:

- `hidden_state`
- `concealment_subsystem`
- `ailment`
- `procedural_state`

### 2. Decisions

Examples:

- `concealment_hidden_state_split`
- `hidden_roll_persistence`
- `ailment_numeric_burden_from_rank_bonus`

### 3. Source Bundles

Examples:

- concealment authority
- ailment authority
- simulation doctrine
- species completion state

### 4. Retrieval Profiles

Profiles define optimized lookup paths for recurring work types.

Examples:

- simulator domain modeling
- ailment review
- technique balance audit
- species completion audit
- publication consistency review

## Retrieval Flow

The intended local retrieval flow is:

1. classify the query by domain
2. load the matching retrieval profile
3. load compact structured registries first
4. load only the preferred authority files for that domain
5. expand to broader source bundles only if still needed

## Example

If the query is:

`How should Hidden be represented?`

The retrieval layer should prefer:

1. `data/knowledge/concept-registry.yaml`
2. `data/knowledge/decision-registry.yaml`
3. `docs/knowledge/CONCEPT-MODEL.md`
4. `docs/system/cover-visibility-concealment.md`
5. `data/system/cover-visibility-concealment.yaml`

It should not begin by reading unrelated species or publication files.

## Core Retrieval Assets

The first local retrieval layer should use:

- `data/knowledge/knowledge-manifest.yaml`
- `data/knowledge/retrieval-profiles.yaml`
- `data/knowledge/concept-registry.yaml`
- `data/knowledge/decision-registry.yaml`
- `data/knowledge/source-map.yaml`
- `data/knowledge/project-state.yaml`

## Retrieval Types

### Concept Retrieval

Use when the query asks:

- what is X
- what family does X belong to
- where is X defined

### Decision Retrieval

Use when the query asks:

- have we already decided this
- what doctrine constrains this
- which cross-cutting rule applies here

### Source Retrieval

Use when the query asks:

- which files should I read first
- which source is authoritative for this kind of question

### State Retrieval

Use when the query asks:

- where are we in this subsystem
- what is complete
- what still needs design work

## Tooling Relevance

This layer should eventually support:

- simulator domain modeling
- publication consistency checks
- design audits
- species coverage audits
- future semantic retrieval

## Future Evolution

After the local retrieval layer is stable, the next possible step is semantic indexing.

If that happens, semantic retrieval should be layered on top of this system, not replace it.

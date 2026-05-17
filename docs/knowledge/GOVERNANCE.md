# Knowledge Governance

## Purpose

This document defines how project knowledge is recorded, maintained, and trusted.

The goal is to ensure that future design and simulation work can reuse settled doctrine without repeatedly reconstructing it from large files or long conversations.

## Knowledge Tiers

The project should treat knowledge in these tiers:

### Tier 1: Authority Rules

Canonical rule statements and authority data.

Primary locations:

- `docs/system/`
- `data/system/`

### Tier 2: Formal Decisions

Accepted architectural or rule decisions, especially when tradeoffs mattered.

Primary location:

- `docs/adr/`

### Tier 3: Knowledge Layer

Normalized doctrine, terminology, ownership boundaries, state summaries, and current project state.

Primary locations:

- `docs/knowledge/`
- `data/knowledge/`

### Tier 4: Conversations

Useful for iteration, but never the long-term memory system.

Conversation should be treated as ephemeral unless its outcomes are recorded into Tiers 2 or 3.

## Recording Rules

When a design conclusion is accepted and expected to matter again, it should be recorded using this decision path:

1. If the decision changes canon rules, update the authority files.
2. If the decision is architectural, doctrinal, or cross-cutting, record or update an ADR when appropriate.
3. Normalize the result into the knowledge layer so it can be reused quickly.

## Update Rules

The knowledge layer must be updated when:

- a state changes category or taxonomy
- a subsystem boundary is clarified
- a repeated terminology ambiguity is resolved
- a species completion state materially changes
- simulator abstractions need a settled crosswalk to canon rules

The knowledge layer does not need an update for every local wording edit.

## Canonical Query Order

When answering a design question, prefer this lookup order:

1. authority rules in `docs/system/` and `data/system/`
2. ADRs
3. knowledge registries in `data/knowledge/`
4. explanatory doctrine in `docs/knowledge/`

## Registry Responsibilities

The YAML registries should stay compact and queryable.

They should answer questions like:

- what is this concept
- what family does it belong to
- where is its main authority source
- what decisions materially constrain it
- what is its current project status

## Drift Prevention

To prevent drift:

- each registry entry should point back to authority paths
- doctrine documents should describe boundaries rather than duplicate whole chapters
- project state should summarize status, not re-explain entire systems

## Simulation Relevance

The simulator should not mine prose blindly from all rule chapters if that can be avoided.

Instead, it should increasingly rely on:

- canon data
- knowledge registries
- simulation-specific normalized data

That is one of the main reasons this layer exists.

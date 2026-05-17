# Source of Truth Map

## Purpose

This document explains where different kinds of truth should be resolved in the repository.

It exists to answer a simple but expensive question:

Where should we look first for this kind of answer?

## Rule Truth

For rule wording, legality, and core mechanics, check first:

- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`

## Decision Truth

For major accepted design decisions, check:

- `Transcendence-design/docs/adr/`

## Knowledge Truth

For normalized doctrine, taxonomy, ownership boundaries, and current completion status, check:

- `Transcendence-design/docs/knowledge/`
- `Transcendence-design/data/knowledge/`

## Publication Truth

For currently rendered or publication-facing wording, check:

- `Transcendence-publications/`

Publication wording may lag design authority. When there is disagreement, design authority should win unless a deliberate publication override exists.

## Simulation Truth

For simulation-specific abstractions, check:

- `Transcendence-design/sim/`

Simulation truth should always trace back to design authority and knowledge normalization. It should not become an independent stealth rule system.

## Practical Lookup Order

When uncertain, use this order:

1. `docs/system/`
2. `data/system/`
3. `docs/adr/`
4. `docs/knowledge/`
5. `data/knowledge/`
6. `sim/`
7. `publications/` only to verify rendered wording or drift

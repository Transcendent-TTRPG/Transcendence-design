# Project Knowledge Access

This package provides deterministic local retrieval over the Transcendence project knowledge layer and its preferred authority sources.

It is intentionally project-wide. It is not owned by the simulator.

## Intended Responsibilities

- load retrieval profiles
- load knowledge manifests
- resolve domains to preferred sources
- retrieve compact registries before large prose docs
- support design, publication, species, and simulation tooling

## First Modules

- `types.py` for retrieval-facing data structures
- `catalog.py` for loading manifests and profiles
- `selector.py` for resolving query domains to sources
- `resolver.py` for assembling retrieval bundles
- `query.py` for the high-level local retrieval interface
- `intents.py` for common task-oriented entrypoints

## Intended Public Entry Styles

There are now three intended ways to use this package:

### 1. Domain-first

Use when you already know the exact domain you want.

Examples:

- `resolve_domain("concealment", profile_id="concealment_rule_lookup")`

### 2. Profile-first

Use when the work type is more important than the domain list.

Examples:

- `resolve_profile("species_completion_audit")`
- `resolve_profile("simulator_domain_modeling")`

### 3. Intent-first

Use when you want stable project entrypoints for common work.

Examples:

- `for_simulator_domain_modeling()`
- `for_technique_balance_audit()`
- `for_species_completion_audit()`

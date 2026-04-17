# Transcendence Design

This repository is the source of truth for the Transcendence universe and system.

## Purpose

This repo contains the foundational design of the project:

- canon
- worldbuilding
- lore
- rules
- frameworks
- design decisions
- QA criteria
- structured templates

This repository is not intended to be the final publication output or the playable Foundry package.
It defines what is true, what is intended, and how new content should be validated.

## Core Responsibilities

- define setting truth
- define mechanical truth
- document tone and thematic pillars
- provide reusable frameworks for content creation
- maintain consistency across game, novels, and supplements
- serve as the upstream source for implementation and publication

## Repository Areas

### `docs/vision`
High-level identity of the project.

### `docs/canon`
Lore, cosmology, species, cultures, geography, factions, and glossary.

### `docs/system`
Mechanical architecture of the TTRPG.

### `docs/frameworks`
Reusable creation frameworks for species, disciplines, abilities, items, enemies, and narrative content.

### `docs/qa`
Validation checklists to prevent inconsistency, bloating, contradiction, or weak design.

### `docs/adr`
Architecture and design decisions. These explain why important decisions were made.

### `data/`
Structured content that may later feed tools, automation, or Foundry pipelines.

### `playtests/`
Filled-in playtest records organized by encounter type (`combat/`, `exploration/`, `social/`).
Each file is a completed instance of a template. See `playtests/README.md` for naming conventions and workflow.

### `templates/`
Standardized templates for new content.

- `combat-playtest.md` — reusable template for combat encounter playtesting; covers enemy role, vital points, reading paths, attrition pressure, phase structure, calibration signals, and post-playtest log

### `references/`
Reference material and inspiration used during development.

## Canon Policy

This repo distinguishes between:

- **hard canon**: foundational truth, not changed lightly
- **soft canon**: flexible content that can evolve
- **implementation details**: technical translation for tools
- **presentation layer**: how canon is revealed in fiction or supplements

## Workflow

1. Propose or draft content
2. Validate against framework
3. Run QA checklist
4. Record important decisions in ADR if needed
5. Promote to canon/system truth
6. Communicate downstream impact to Foundry/publications

## AI Usage Notes

AI assistants should treat this repository as the main source of truth.

Preferred behavior:

- consult vision before generating content
- consult canon before adding lore
- consult system docs before designing mechanics
- use templates
- check QA documents before finalizing proposals

## Naming Rules

Recommended naming principles:

- clear, stable, descriptive file names
- avoid ambiguous shorthand
- one concept per file where practical
- glossary terms should remain consistent across the repo

## Future Role

This repository is expected to feed:

- `transcendence-foundry`
- `transcendence-publications`

No downstream repo should silently redefine major canon without a change first being reflected here.
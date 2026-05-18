# Transcendence Simulation Lab

This module is a non-visual laboratory for testing Transcendence combat and related mechanical systems through structured simulation.

Its goal is not to simulate a full tabletop session and it is not a substitute for human playtest. Its goal is to answer focused design questions with repeatable experiments, explicit assumptions, probability, Monte Carlo runs, and traceable decision policies.

## Mission

The simulation lab exists to support balance, clarity, and design inference across:

- combat actions
- Techniques
- ATB timing
- ailments and persistent states
- concealment and detection
- trap responses
- species comparison
- pressure, attrition, and tempo

The lab should help answer:

- what is likely
- what is expensive
- what is efficient
- what is oppressive
- what is weak
- what interacts badly with the rest of the system

## What This Module Is

This module is:

- a question-driven testing environment
- a rules-resolution engine with explicit inputs
- a policy-based decision sandbox
- a statistical analysis tool for balance questions
- a reproducible experiment framework

## What This Module Is Not

This module is not:

- a full virtual tabletop
- a narrative GM
- a replacement for tabletop playtest
- an attempt to model open-ended human creativity
- an authority source that replaces `docs/system/`

## Core Principle

The unit of work is a **question**, not a match and not a campaign scene.

Examples:

- Is a Technique meaningfully better than the equivalent base action?
- How costly is a `Rhythm 0 / Attrition 2` reaction in practice?
- How often does `Oculto` survive a watched crossing?
- How oppressive is `Aterrorizado` under one ATB policy?
- Does one species convert tempo into pressure better than another?

## Design Principles

- Rules resolution should be explicit before behavior modeling is added.
- Decision behavior must be externalized into `policies`.
- Scenarios must be reusable and declarative.
- Reports must be reproducible from saved inputs.
- Results are only valid relative to their assumptions.
- The engine should prefer clarity and traceability over cleverness.

## Relationship to Canon Rules

The authority sources remain:

- `Transcendence-design/docs/system/`
- `Transcendence-design/data/system/`

The simulator consumes reduced or normalized forms of those rules. It does not own the rules.

When a discrepancy appears:

1. check the design authority first
2. then update simulation data or engine assumptions
3. only then treat the simulation result as valid again

## Scope

The intended scope includes:

- meter-based grid positioning
- ATB timeline progression
- actions and reactions
- techniques
- ailments
- concealment state handling
- trap-response mechanics
- policy-driven decisions
- statistical and comparative reporting

The intended scope excludes:

- freeform social scenes
- unconstrained environmental narration
- arbitrary GM fiat
- expressive player bluffing or negotiation
- “vibe” evaluation without measurable proxies

## Structure

```text
sim/
├── README.md
├── ARCHITECTURE.md
├── DATA-SCHEMAS.md
├── pyproject.toml
├── sim_runner.py
├── engine/
├── models/
├── data/
├── policies/
├── questions/
├── scenarios/
├── experiments/
├── reports/
└── tests/
```

## Layer Overview

### `engine/`

Pure rules resolution.

This layer should eventually own:

- dice and randomness
- ATB timeline movement
- action and reaction resolution
- combatant state
- techniques
- ailments
- concealment
- trap responses

### `models/`

Typed data structures for the simulation domain.

This layer should define:

- combatants
- actions
- techniques
- ailments
- scenarios
- questions
- results

### `data/`

Declarative simulation-facing snapshots or reduced forms of game rules.

This is not the authority source. It is the input layer that the simulator reads.

### `policies/`

Explicit actor behavior rules.

Examples:

- aggressive melee
- attrition saver
- tempo first
- stealth crosser
- trap cautious

### `questions/`

Saved design questions.

Each question should define:

- what is being tested
- which scenario is used
- which actors are involved
- which policies they follow
- which metrics are collected
- which comparison or hypothesis is being examined

### `scenarios/`

Reusable spatial or tactical setups.

Examples:

- one reaction window
- hidden crossing
- corridor crossing
- duel in clutter

### `experiments/`

Runners for specific kinds of analysis.

Examples:

- Monte Carlo
- technique comparison
- ATB tempo analysis
- concealment tests
- ailment pressure tests
- trap-response tests

### `reports/`

Saved output from experiments.

Suggested usage:

- `raw/` for machine-readable outputs
- `summaries/` for human-readable reports
- `charts/` for later visual exports if needed

### `tests/`

Internal validation for the simulator itself.

This layer exists to prove that:

- dice behave correctly
- ATB timing behaves correctly
- state duration behaves correctly
- concealment works per observer
- trap mitigation timing is resolved correctly

## Companion Documents

- [`ARCHITECTURE.md`](./ARCHITECTURE.md): full system design for the simulation module
- [`DATA-SCHEMAS.md`](./DATA-SCHEMAS.md): declarative data formats and field expectations
- [`TECHNIQUE-PORTING-PLAN.md`](./TECHNIQUE-PORTING-PLAN.md): retroactive species Technique porting order and coverage states

## Development Posture

This module is being built as a full system, not as a throwaway prototype.

That means:

- architecture should be designed before deep implementation
- formats should be stable before mass data entry
- engine contracts should be written before policy complexity expands
- testing strategy should be explicit before trusting balance outputs

## Notes

- This module is intentionally independent from publication output.
- It should be safe to keep experimental scenarios and question files here.
- A simulation result is only as good as its data, policies, and scenario assumptions.

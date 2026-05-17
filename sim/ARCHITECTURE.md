# Simulation Architecture

## Purpose

This document defines the full architecture of the Transcendence simulation lab.

It describes:

- system layers
- domain boundaries
- execution flow
- responsibilities
- dependencies
- validation strategy at the architectural level

It does not define every field of every YAML file. That belongs in `DATA-SCHEMAS.md`.
Formal roll-family semantics belong in `ROLL-MODEL.md`.
Damage-surface branching belongs in `DAMAGE-MODELS.md`.

## Architectural Goals

The simulation module should:

1. answer focused design questions
2. resolve rules consistently
3. support probabilistic analysis
4. separate rules from behavior
5. keep scenarios and questions reproducible
6. remain auditable when results look surprising

## High-Level Layers

The module is divided into these primary internal layers:

1. `models`
2. `data`
3. `engine`
4. `policies`
5. `experiments`
6. `reports`
7. `tests`

The simulator also depends on one external shared project layer:

- `knowledge access`

## Layer Responsibilities

### 1. Models

The `models` layer defines the formal simulation domain.

Its job is to express the stable shapes of:

- combatants
- actions
- techniques
- ailments
- concealment states
- trap responses
- scenarios
- questions
- results

The `models` layer must not resolve rules and must not choose behavior.

### 2. Data

The `data` layer stores declarative, simulation-facing inputs.

Its job is to provide:

- reduced action definitions
- reduced technique definitions
- reduced ailment definitions
- species profiles
- environment presets

The `data` layer is a simulation input mirror, not the game’s final authority source.

### External Dependency: Knowledge Access

The simulator consumes the shared project `knowledge access` layer rather than owning it.

That layer retrieves compact project memory before broad rule scanning begins.

It should provide:

- concept lookups
- decision lookups
- domain-to-source mapping
- low-token retrieval paths for simulator design and tooling

It should rely first on:

- `docs/knowledge/`
- `data/knowledge/`

### 3. Engine

The `engine` layer resolves rules.

It should eventually own:

- randomness and seeded runs
- dice resolution
- ATB movement
- action and reaction legality
- roll comparison
- state application and expiration
- concealment and detection
- trap-trigger response handling
- outcome packaging

The `engine` layer must not choose what an actor wants. It only resolves what happens when a choice is made.

### 4. Policies

The `policies` layer chooses actions for simulated actors.

Policies must remain explicit and swappable.

They should decide:

- which action to take
- whether to spend a technique
- whether to react
- when to conserve attrition
- what to target
- what objective matters most

Policies should not modify rules. They only consume legal options and rank them.

### 5. Experiments

The `experiments` layer turns questions into runs.

It should:

- load a question
- load one or more scenarios
- instantiate actors
- assign policies
- run iterations
- collect metrics
- compare outcomes

### 6. Reports

The `reports` layer stores output.

It should keep:

- raw iteration output
- summarized metrics
- later chart or table exports

### 7. Tests

The `tests` layer validates the simulator.

It exists to prove that:

- rules are implemented correctly
- states transition correctly
- timeline progression is stable
- seeded outcomes are reproducible
- regressions can be detected

## Domain Boundaries

The simulator should distinguish sharply between:

- **rules**
- **state**
- **behavior**
- **question framing**
- **reporting**

These should never collapse into one object.

Examples:

- a `Technique` definition is not an actor decision
- a `Policy` is not a rule resolver
- a `Question` is not a `Scenario`
- a `Scenario` is not a `Report`

The simulator also needs a strong boundary between:

- **authority rules**
- **normalized project memory**
- **simulation-facing reduced data**

Those three layers should cooperate, but they should not be treated as one source.

## Knowledge Access Boundary

The shared knowledge access layer exists before the engine because the project is already large enough that repeated full-file rereads are inefficient.

Its role is to narrow the search space.

For example:

- a concealment query should first retrieve concept and decision summaries
- then only the relevant concealment authority files
- not unrelated species or publication files

## Core Domain Objects

The architecture assumes the following core object families:

### Combatant

Represents one actor or combat unit in simulation.

Should include:

- identity
- species or archetype
- statistics
- competencies
- techniques
- ailments
- concealment relationships
- ATB position
- attrition and fatigue state
- zone or part state if applicable

### Action

Represents one legal action template.

Should include:

- category
- rhythm
- attrition
- legality gates
- roll type
- effect structure

### Technique

Represents one authored technique definition adapted for simulation.

Should include:

- trigger
- legality gates
- cost
- roll structure
- outcomes
- scaling
- restrictions

### Ailment

Represents one harmful state.

Should include:

- family
- severity
- application route
- numeric burden logic
- qualitative burden logic
- recovery route
- persistence rule

### Concealment State

Represents one observer-relative hidden state.

Should include:

- owner
- observer or observer group
- active value
- acquisition source
- persistence conditions
- break conditions

### Trap Response

Represents one condition-triggered system resolution.

Should include:

- trigger source
- response type
- timing window
- relevant rolls
- severity or consequence structure

### Scenario

Represents the tactical setup.

Should include:

- map assumptions
- distances
- clutter / cover / visibility
- initial positions
- active environmental features
- observers and watch lines if needed

### Question

Represents one design question.

Should include:

- statement
- scenario reference
- actor references
- policy references
- metric set
- iteration count
- comparison target

### Result

Represents aggregated outputs.

Should include:

- metadata
- iteration statistics
- summary metrics
- comparison deltas
- notes or warnings

## Engine Subsystems

The `engine` layer should eventually split into these logical subsystems:

### RNG and Dice

Responsibilities:

- seeded randomness
- deterministic replay support
- discrete dice rolling
- helper probability functions

### Timeline

Responsibilities:

- initial preparation placement
- ATB advancement by rhythm
- reaction insertion
- next-actor selection

### Grid and Spatial Logic

Responsibilities:

- positions in meters
- adjacency
- path length
- watched crossings
- line of sight / line of effect abstractions

### Resolver

Responsibilities:

- apply declared action
- collect relevant modifiers
- perform needed rolls
- apply outcomes
- emit normalized result objects

### State Store

Responsibilities:

- maintain active states
- observer-relative concealment
- ailments
- durations
- replacement and stacking rules

### Technique Resolver

Responsibilities:

- check trigger and legality
- resolve costs
- invoke technique roll flow
- apply technique effects

### Ailment Resolver

Responsibilities:

- apply ailments
- upgrade, replace, or refuse stacking
- handle recovery checks
- expose numeric and qualitative burdens

### Concealment Resolver

Responsibilities:

- grant `Oculto` / `Hidden`
- store active value
- resolve observer-relative detection
- handle compromise and loss

### Trap Resolver

Responsibilities:

- represent triggered mechanism responses
- allow mitigation windows
- resolve trap-response techniques
- update trap state if needed

## Execution Flow

At the highest level, a run should look like this:

1. Load a `Question`
2. Load its `Scenario`
3. Load referenced actors and definitions
4. Assign policies
5. Initialize combat state
6. Repeatedly:
   - determine next actor or trigger
   - ask policy for intent
   - validate legality
   - resolve via engine
   - update state
   - record observations
7. End according to question or scenario conditions
8. Aggregate metrics
9. Save results

## Behavioral Architecture

Policies should operate through a clear contract:

1. inspect current simulation state
2. enumerate legal options
3. score options
4. return one chosen option

This makes behavior:

- testable
- replaceable
- inspectable

Policies should never directly mutate state.

## Question-Driven Architecture

The simulator exists to answer questions, so the architecture should prioritize:

- question reusability
- scenario reusability
- metric composability
- policy substitution

That means:

- one scenario can support many questions
- one question can compare multiple policies
- one policy can be tested across many species

## Metrics Architecture

Metrics should be collected at two levels:

### Event-Level

Examples:

- one roll succeeded
- one reaction was used
- one state was applied
- one technique was selected

### Aggregate-Level

Examples:

- success rate
- expected attrition spent
- expected rhythm spent
- average time to first ailment
- average hidden retention
- zone collapse rate
- action pick frequency

## Determinism and Reproducibility

The architecture should support:

- fixed seeds
- replayable runs
- saved questions
- saved scenarios
- normalized outputs

This is essential for diagnosing surprising results.

## Validation Strategy at the Architecture Level

The simulator should be validated through:

1. unit tests
2. fixtures
3. deterministic replay
4. regression baselines
5. cross-checks against known simple calculations

Examples:

- exact probability of simple dice cases
- ATB advancement under fixed action sequences
- `Oculto` loss under known trigger patterns
- one ailment’s persistence under a known recovery rule

## Implementation Order

Implementation should proceed in this order:

1. architecture and schemas
2. domain models
3. loaders and validators
4. RNG and dice
5. outcome normalization
6. ATB timeline
7. actions and reactions
8. state store
9. ailments
10. concealment
11. traps
12. techniques
13. policies
14. experiment runners
15. reports
16. validation suites

## Non-Goals for Early Implementation

Even in the full architecture, these are non-goals for the first implementation phases:

- UI
- real-time visualization
- networked play
- Foundry integration
- direct publication export

## Companion Document

Field-level and file-level schemas are defined in [`DATA-SCHEMAS.md`](./DATA-SCHEMAS.md).

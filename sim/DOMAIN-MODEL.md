# Domain Model

## Purpose

This document defines the formal domain model for the Transcendence simulation lab.

It sits between:

- architecture
- declarative schemas
- runtime engine implementation
- formal roll semantics in `ROLL-MODEL.md`
- damage-surface branching in `DAMAGE-MODELS.md`

The goal is to make object boundaries explicit before full rule resolution is implemented.

## Modeling Principles

- Definition objects and runtime-state objects must remain distinct.
- A simulator actor is not just a species profile; it is a profile instantiated into runtime state.
- Ailments and concealment states are separate families.
- Techniques should describe authored behavior, not duplicate ailment rules.
- Questions, scenarios, and results must remain independent objects.

## Object Families

The model is divided into four broad families:

### 1. Definitions

Stable authored or loaded definitions:

- `ActionDefinition`
- `TechniqueDefinition`
- `AilmentDefinition`
- `RollDefinition`
- `EffectDefinition`

### 2. Runtime State

Objects that exist during simulation execution:

- `Combatant`
- `ActiveAilment`
- `ConcealmentState`
- `ZoneState`
- `TimelineState`

### 3. Experiment Framing

Objects that define what is being tested:

- `ScenarioDefinition`
- `ScenarioActorSlot`
- `QuestionDefinition`

### 4. Outputs

Objects that describe what happened:

- `RollOutcome`
- `IterationResult`
- `AggregateMetric`
- `ExperimentResult`

## Core Definitions

### ActionDefinition

Represents one baseline action template.

Should answer:

- what kind of action this is
- what it costs
- what roll family it uses
- what legality gates apply
- what effect structure it triggers

### TechniqueDefinition

Represents one simulation-facing version of an authored Technique.

Should answer:

- origin
- cost
- trigger
- requirements
- roll specification
- effect structure
- duration / persistence model

### AilmentDefinition

Represents the canonical simulation behavior of one ailment.

Should answer:

- family
- severity model
- application rules
- numeric burden model
- qualitative burden model
- recovery route
- timing / reevaluation points
- persistence

## Core Runtime Objects

### Combatant

Represents one instantiated actor in runtime.

Should include:

- identity and side
- spatial position
- competencies
- armor by zone
- shield if present
- resistance competencies by family when trained
- weapon loadouts by slot
- equipped techniques
- current ailments
- concealment relationships
- timeline state
- preparation
- rhythm / attrition relevant runtime state
- zone / part state when relevant
- declared damage model

### ActiveAilment

Represents one applied ailment on a combatant.

Should include:

- ailment id
- severity
- source id
- source rank bonus
- application timestamp or activation index
- current persistence status

### ConcealmentState

Represents one observer-relative hidden relationship.

Should include:

- owner combatant id
- observer combatant id or observer group id
- active value
- acquisition source
- break conditions
- whether it is still valid

### ZoneState

Represents one relevant body part, subsystem, or targetable zone.

Should include:

- zone id
- operational status
- current wounds / tags
- whether the zone remains target-relevant

### CreatureZoneState

Represents one runtime part under a creature-zone damage model.

Should include:

- zone id
- current and maximum HP
- block
- durability
- linked abilities
- whether the part is broken or disabled

### TimelineState

Represents current ATB and activation context.

Should include:

- preparation
- current track position if modeled separately
- pending activation markers
- lost activation flags

## Scenario and Question Objects

### ScenarioDefinition

Represents a tactical setup independent from a single experiment run.

Should include:

- environment id
- map geometry
- actor slot placements
- scenario conditions
- observer relationships when relevant

### QuestionDefinition

Represents a design question to be tested.

Should include:

- question id
- natural-language prompt
- profile or work type
- domains
- scenario id
- actor assignments
- policy assignments
- metrics requested

## Output Objects

### RollOutcome

Represents one resolved roll event.

Should include:

- roll family
- actor id
- source definition id
- raw or abstracted result
- pass/fail
- opposed target if relevant

### IterationResult

Represents one complete simulation iteration.

Should include:

- question id
- scenario id
- seeds / reproducibility markers
- roll log
- state changes
- summary metrics for that run

### ExperimentResult

Represents a set of iteration results summarized for one question.

Should include:

- bundle metadata
- aggregate metrics
- comparisons
- confidence or distribution summaries

## Relationship Rules

The most important relationships are:

- a `QuestionDefinition` references one `ScenarioDefinition`
- a `ScenarioDefinition` provides slots for `Combatant` instantiation
- a `Combatant` owns zero or more `ActiveAilment`
- a `Combatant` participates in zero or more `ConcealmentState` relations
- a `TechniqueDefinition` may apply an `AilmentDefinition`, but should not duplicate its logic
- an `ExperimentResult` summarizes many `IterationResult`

## Knowledge Layer Dependency

These objects should not be designed in isolation.

The domain model should increasingly be derived with help from:

- `knowledge_access`
- `concept-registry`
- `decision-registry`
- relevant authority rule files

This is especially important for:

- `ConcealmentState`
- `AilmentDefinition`
- `TechniqueDefinition`

## Implementation Guidance

The first code pass should prioritize:

1. stable dataclass structures
2. explicit field naming
3. clear distinction between definition and runtime objects
4. low coupling to rule resolution

The engine should consume these models later, not reshape them ad hoc.

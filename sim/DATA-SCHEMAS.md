# Data Schemas

Formal roll-family semantics live in `ROLL-MODEL.md`. This document only defines
how simulation-facing data expresses roll references and related authored inputs.
Damage-model branching lives in `DAMAGE-MODELS.md`.

## Purpose

This document defines the declarative data formats used by the simulation lab.

These schemas are logical contracts, not strict machine-enforced schemas yet.

They exist to answer:

- what files we store
- what each file is expected to contain
- which fields are required
- which references are allowed

## General Rules

- IDs should be stable and snake_case.
- Human-readable names are optional unless needed for reports.
- Every declarative object should have one clear owner type.
- Question files should reference scenarios, actors, and policies by ID.
- Simulation data should remain simpler than the full design authority docs.

## File Families

The simulation module uses these data families:

1. `actions`
2. `techniques`
3. `ailments`
4. `species profiles`
5. `environments`
6. `scenarios`
7. `questions`

The simulator also depends on external project knowledge registries, but those belong to the shared project knowledge layer rather than the simulator's own schema families.

## 1. Action Data

### Path

- `data/actions/base_actions.yaml`

### Purpose

Defines simulation-facing base actions.

### Logical Shape

```yaml
actions:
  - id: hide
    name: Hide
    category: utility
    rhythm: 6
    attrition: 1
    roll_type: specialization
    trigger_type: active
    legal_when:
      - has_real_opportunity
    effects:
      - grant_hidden_state
```

### Required Fields

- `id`
- `name`
- `category`
- `rhythm`
- `attrition`
- `roll_type`
- `trigger_type`

### Optional Fields

- `legal_when`
- `effects`
- `notes`

## 2. Technique Data

### Paths

- `data/techniques/sauri.yaml`
- `data/techniques/naghii.yaml`
- `data/techniques/zarnag.yaml`

### Purpose

Defines simulation-facing versions of authored techniques.

### Logical Shape

```yaml
techniques:
  - id: pasar_como_parte_del_fondo
    name: Pasar Como Parte del Fondo
    species: zarnag
    category: utility
    type: active
    origin: Sigilo
    rhythm: 3
    attrition: 1
    trigger: watched_crossing
    requirements:
      specializations:
        - Sigilo
      states:
        - incomplete_observation
    roll:
      type: specialization
      specialization: Sigilo
      opposed_by: perception_or_threshold
    effects:
      - grant_hidden_state_limited
    durations:
      model: until_condition_changes
```

### Required Fields

- `id`
- `name`
- `species`
- `category`
- `type`
- `origin`
- `rhythm`
- `attrition`
- `trigger`
- `roll`
- `effects`

### Optional Fields

- `requirements`
- `durations`
- `restrictions`
- `notes`
- `scaling`

## 3. Ailment Data

### Path

- `data/ailments/ailments.yaml`

### Purpose

Defines simulation-facing versions of harmful states.

### Logical Shape

```yaml
ailments:
  - id: aterrorizado
    family: alteration
    severity_model: minor_moderate_severe
    numeric_burden:
      source: rank_bonus
      applies_to:
        - ar_against_feared_line
        - dr_against_feared_line
    qualitative_burden:
      minor:
        - line_specific_pressure
      moderate:
        - containment_required_to_commit
      severe:
        - first_attempt_may_abort
    recovery:
      type: specialization_roll
      specialization: Contencion
```

### Required Fields

- `id`
- `family`
- `severity_model`
- `recovery`

### Optional Fields

- `numeric_burden`
- `qualitative_burden`
- `timing`
- `application_notes`
- `replacement_rules`

### Timing Shape

```yaml
timing:
  activation_start:
    - threaten_next_meaningful_activation
  action_gate:
    - severe_first_feared_line_attempt_may_abort
  reevaluation_points:
    - activation_start
    - explicit_recovery
    - feared_line_change
  expiry_mode: fiction_change_or_recovery
  fiction_release_events:
    - feared_line_changed
```

Use `timing` to declare:

- what triggers at activation start
- what can abort the first relevant attempt in an activation
- where reevaluation happens
- whether expiry requires recovery, fiction change, or both

## 4. Species Profile Data

### Paths

- `data/species/sauri_profiles.yaml`
- `data/species/naghii_profiles.yaml`
- `data/species/zarnag_profiles.yaml`

### Purpose

Defines simulation-ready combatant baselines or archetypes.

### Logical Shape

```yaml
profiles:
  - id: zarnag_novice_skirmisher
    species: zarnag
    preparation: 5
    movement_meters: 9
    damage_model:
      kind: player_wounds
    competencies:
      Sigilo: novice
      Trampas: novice
      Dagger: adept
    techniques:
      - esconder_la_segunda_linea
      - pasar_como_parte_del_fondo
    policy_defaults:
      primary: tempo_first
```

### Required Fields

- `id`
- `species`
- `preparation`
- `movement_meters`
- `damage_model`
- `competencies`

### Optional Fields

- `techniques`
- `equipment`
- `zones`
- `policy_defaults`

### Damage Model Shape

```yaml
damage_model:
  kind: player_wounds
```

or:

```yaml
damage_model:
  kind: creature_zones
  creature_zones:
    - id: jaw
      max_hp: 8
      block: 2
      durability: 4
      linked_abilities:
        - bite
        - frost_breath
      vital: false
```

## 5. Environment Data

### Paths

- `data/environments/*.yaml`

### Purpose

Defines reusable environmental assumptions.

### Logical Shape

```yaml
environment:
  id: cluttered_ruin
  visibility: reduced_partial
  clutter_level: medium
  cover_density: medium
  notes:
    - broken interior
    - uneven floor
```

### Required Fields

- `id`

### Optional Fields

- `visibility`
- `clutter_level`
- `cover_density`
- `notes`

## 6. Scenario Data

### Paths

- `scenarios/micro/*.yaml`
- `scenarios/skirmish/*.yaml`
- `scenarios/stress/*.yaml`

### Purpose

Defines tactical setups independent from specific questions.

### Logical Shape

```yaml
scenario:
  id: hidden_crossing
  environment: smoke_crossing
  map:
    width_m: 12
    height_m: 8
  actors:
    - slot: mover
      position: [1, 3]
    - slot: watcher
      position: [7, 3]
  conditions:
    - partial_watch
    - incomplete_registration
```

### Required Fields

- `id`

### Optional Fields

- `environment`
- `map`
- `actors`
- `conditions`

## 7. Question Data

### Paths

- `questions/**/**/*.yaml`

### Purpose

Defines one design question and the experiment setup needed to answer it.

### Logical Shape

```yaml
id: trap_response_reaction_value
question: How much value does a trap-response reaction create?
scenario: triggered_trap
iterations: 20000
actors:
  target: zarnag_novice_skirmisher
  source: generic_triggered_trap
policies:
  target: trap_cautious
measurements:
  - success_rate
  - expected_attrition_spent
  - expected_consequence_reduction
compare:
  baseline: no_technique
  test: ceder_antes_del_disparo
```

### Required Fields

- `id`
- `question`
- `scenario`

### Optional Fields

- `iterations`
- `actors`
- `policies`
- `measurements`
- `compare`
- `notes`

## External Dependency: Knowledge Retrieval Data

The simulator consumes shared project retrieval data from:

- `Transcendence-design/data/knowledge/knowledge-manifest.yaml`
- `Transcendence-design/data/knowledge/retrieval-profiles.yaml`

Those files belong to the project-wide knowledge layer, not to the simulator's own schema ownership.

## ID and Reference Rules

All references should use IDs rather than file paths where possible.

Examples:

- question references scenario by `scenario: hidden_crossing`
- scenario references environment by `environment: smoke_crossing`
- profile references techniques by technique IDs

## Normalization Guidelines

Simulation data should normalize away:

- excessive narrative prose
- publication formatting
- duplicate text
- broad flavor text that does not affect resolution

Simulation data should preserve:

- legality
- costs
- triggers
- rolls
- durations
- effects
- restrictions

## Validation Expectations

Eventually, loaders should validate:

- required field presence
- referenced IDs exist
- categories are valid
- roll types are known
- duration models are known
- policy references exist

## Future Extensions

Possible future schema additions:

- encounter templates
- monster subsystem tracks
- zone-part profiles
- deterministic fixture definitions
- baseline expectation ranges for regression checking

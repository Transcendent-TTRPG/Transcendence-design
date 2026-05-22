# Technique Porting Plan

## Purpose

This document tracks the retroactive porting of already-authored species
Techniques into the simulation lab.

The simulator is no longer blocked on core infrastructure. The main bottleneck
is now **coverage**:

- authored Technique exists in `docs/system/techniques.md`
- but there is not yet a simulation-facing definition
- or there is a definition but not enough runtime support
- or there is runtime support but no policy/scenario coverage

This document exists to make that work incremental and auditable.

---

## Working Decision

For the current phase of simulator development, the project should prioritize
**retroactive backfill of already-authored species Techniques before new
Technique authoring port work expands further**.

In practical terms:

- if a Technique is already authored in the design authority, it should be
  treated as part of the simulation backlog
- new simulator-facing Technique work should begin from the earliest missing
  authored Techniques of the finished species passes
- the immediate goal is not just “some coverage”, but a usable path to test
  species passes from their first authored Techniques forward

This does **not** mean every authored Technique must be ported before any other
runtime improvement. It means that new porting work should be organized around
closing authored gaps, not around jumping only to the newest or easiest ideas.

---

## Porting States

Every authored Technique should eventually move through these states:

1. `authored`
2. `sim_defined`
3. `runtime_supported`
4. `policy_exercisable`
5. `scenario_tested`
6. `question_ready`

### Meaning

#### `authored`

The Technique exists in the design authority.

#### `sim_defined`

The Technique exists in `sim/data/techniques/*.yaml` with:

- id
- origin
- rhythm / attrition
- trigger
- roll
- effects
- duration model

#### `runtime_supported`

The current engine can actually resolve its core behavior:

- roll logic
- effects
- ailment / concealment / exchange / timing hooks

#### `policy_exercisable`

At least one policy can choose it under understandable conditions.

#### `scenario_tested`

At least one scenario meaningfully exposes the Technique.

#### `question_ready`

A saved question can use it for repeatable analysis.

---

## Current Reality

Today the simulator can run full ATB slices with:

- activations
- reactions
- combat exchange
- concealment
- ailments
- recovery
- expiry
- policies

But Technique data coverage is still narrow.

### Known pending runtime surfaces

These are engine gaps that have been identified during porting and will affect
multiple Techniques. Registering them here avoids rediscovering the same gap
for each Technique that needs the surface.

| Surface | Gap class | Affects | Notes |
| --- | --- | --- | --- |
| `counter_attacker_exchange_role` | `small_runtime_extension` | `Trabar el Gesto` (Naghii), `Romper el Caudal` (Sauri) | `weapon_exchange_primary` only models the standard attacker role; a counter-exchange where the defender uses T.A. instead of T.D. needs a new exchange variant |
| `ailment_gated_on_exchange_outcome` | `small_runtime_extension` | `Trabar el Gesto` (Naghii) | `apply_ailment` fires unconditionally in post-exchange effects; needs a conditional gate on the outcome of the exchange (success/failure) before applying |
| `rank_scaled_severity_in_apply_ailment` | `small_runtime_extension` | `Trabar el Gesto` (Naghii), any future rank-scaling ailment technique | `apply_ailment` takes a fixed severity string; dynamic severity resolution from actor rank not yet implemented |
| `enemy_weapon_declaration_trigger_hook` | `small_runtime_extension` | Techniques that fire on enemy action declaration rather than on incoming attack | ATB loop has no hook before enemy's weapon-rooted activation completes; needed if any future Technique keeps the utility-check-cancel-action model |
| `ward_zone_procedural_state` | `new_state_family` | `Plantar la Guardia` (Naghii) | needs spatial zone geometry (center + radius), ATB integration to apply Rhythm tax before enemy activations within the zone, and cleanup-on-movement tracking; `apply_procedural_state` effect ID is supported but state type handler is missing |

### Current simulation-defined species Technique files

- `sim/data/techniques/zarnag.yaml`
- `sim/data/techniques/sauri.yaml`
- `sim/data/techniques/naghii.yaml`

### Current actual coverage

- `Zarnag`
  - `sim_defined`: `6`
  - `runtime_supported`: `6`
  - `policy_exercisable`: `6`
- `Sauri`
  - `sim_defined`: `0`
- `Naghii`
  - `sim_defined`: `14`
  - `runtime_supported`: `12`

---

## Species Coverage Matrix

| Species | Authored target | Sim defined | Runtime supported | Policy exercisable | Immediate next goal |
| --- | ---: | ---: | ---: | ---: | --- |
| `Zarnag` | `24` | `6` | `6` | `6` | continue earliest-authored backfill, with `Ensuciar la Herida` as the first major missing outlier |
| `Sauri` | `24` | `0` | `0` | `0` | open first seed batch |
| `Naghii` | `24` | `14` | `12` | `0` | resolve ward_zone new_state_family; resolve counter_attacker_exchange small_runtime_extension; continue backfill |

---

## Naghii Current Ported Set

These authored Naghii Techniques are already simulation-facing:

| Technique | Porting state | Notes |
| --- | --- | --- |
| `Cerrar la Línea` | `runtime_supported` | Executes as a true timing-sensitive reaction, spends reaction cost honestly, and resolves a bounded interception exchange. |
| `Anudar el Paso` | `runtime_supported` | Executes as a reaction and installs a clean-separation denial procedural state instead of requiring a larger withdrawal subsystem first. |
| `Robar el Ángulo` | `runtime_supported` | Resolves a real weapon exchange, steals local position, and installs one direct-answer spoil on success. |
| `Marcar la Lectura` | `runtime_supported` | Installs a marked-route procedural state with fiction-event cleanup rather than only carrying authored notes. |
| `Nublar la Señal` | `runtime_supported` | Installs bounded sensory residue that burdens the next direct answer and clears through use or cleanup events. |
| `Doblar el Tiro` | `runtime_supported` | Resolves a declared one-surface indirect ranged exchange through a bounded simulator-facing geometry abstraction. |
| `Clavar el Paso` | `runtime_supported` | Uses a two-meter pre-exchange committed advance plus standard weapon exchange. |
| `Recuperar la Distancia` | `runtime_supported` | Uses standard weapon exchange plus a one-meter post-hit distance recovery extension. |
| `Clavar la Cadencia` | `runtime_supported` | Reactive Volley ranged attack that on hit reduces target movement by 1m per rank bonus via new `reduce_target_movement_rank_bonus` effect. cost_note corrected to R=4. |
| `Tocar y Ceder` | `runtime_supported` | data_only — composes existing advance_before_exchange_distance (1m) + weapon_exchange_primary + reposition_after_hit_distance (1m). Cost R=5 doctrinal, not yet sim-validated. |
| `Trabar el Gesto` | `sim_defined` | small_runtime_extension — data entry complete; Impedido added to sim ailments; blocked on counter_attacker_exchange_role and ailment_gated_on_exchange_outcome. |
| `Plantar la Guardia` | `sim_defined` | new_state_family — ward_zone state has no handler; needs spatial zone geometry, ATB Rhythm-tax integration, and movement cleanup tracking. Cost corrected from R=7/A=2 to R=3/A=1. |
| `Leer el Calor del Paso` | `runtime_supported` | data_only — Percepcion specialization roll resolves through existing path with no exchange or mechanical effect; information output is Narrator-side. Contextual masking opposition not yet modeled. Cost corrected from R=4 to R=3. |
| `Pesar el Umbral` | `runtime_supported` | data_only — Sigilo specialization roll + alteration_resistance opposed_by + apply_ailment(aterrorizado) all already supported. Type corrected from reactive to active; range defined at 4 meters. New profile: naghii_novice_hidden_warden. |

---

## Zarnag Current Ported Set

These authored Zarnag Techniques are already simulation-facing:

| Technique | Porting state | Notes |
| --- | --- | --- |
| `Reír en la Brecha` | `runtime_supported` | Uses one-shot procedural read pressure against the same source. |
| `Abrir la Costura` | `runtime_supported` | Opens a follow-up seam through procedural Block-ignore setup. |
| `Atajar el Brote` | `runtime_supported` | Same-exchange Block ignore on committed entry. |
| `Robar la Orilla` | `runtime_supported` | Post-hit reposition already lives inside ATB execution. |
| `Pasar Como Parte del Fondo` | `question_ready` | Uses concealment + watched crossing + policy support. |
| `Reír Donde Más Suena` | `question_ready` | Uses `Aterrorizado`, recovery, expiry, and ATB gating. |

These are enough to prove:

- concealment pathing
- fear pressure
- ailment application
- recovery
- expiry by fiction change
- policy usage
- one-shot procedural state pressure
- same-hit Block ignore
- post-hit reposition

But they are not enough to represent Zarnag as a whole.

The first major missing authored outlier is now:

- `Ensuciar la Herida`

That one should be treated as the next heavier retroactive port because it
needs a wound-treatment procedural surface instead of only exchange-time
modifiers.

---

## Retroactive Porting Order

We should not port all authored Techniques in random order.

Use this sequence.

### Step 1. Techniques that reuse existing runtime surfaces

These are the cheapest high-value ports because the engine already supports
their core semantics.

Good candidates:

- direct attack follow-ups
- fear / concealment / reaction pressure
- ailment application through already-supported ailments
- simple exchange modifiers

### Step 2. Techniques that need small new effect types

These require modest engine growth, not architecture changes.

Examples:

- one-shot bonus / penalty injections
- zone-specific attack modifiers
- route or observer-local state markers
- basic timing spoils

### Step 3. Techniques that need new procedural state families

These are more expensive and should be grouped intentionally.

Examples:

- read-mark states
- signal-blur states
- wound-foul states
- route-spoil states

### Step 4. Techniques that need broader scene logic

These should come last because they depend on richer environment or map
semantics.

Examples:

- quarantine line control over multiple spaces
- trap corridor shaping
- multi-target area pressure
- spoil-aftermath behaviors

---

## Species Backfill Order

Because the simulator already has Zarnag seeds, profiles, policies, concealment,
fear, reactions, and ATB behavior in motion, the most efficient retroactive
sequence is:

1. finish the **Zarnag** authored backfill
2. then open the **Naghii** authored backfill
3. then open the **Sauri** authored backfill

This is an implementation order, not a statement of design importance.

The reason is simple:

- `Zarnag` already has the richest simulation scaffolding
- `Naghii` naturally extends concealment, sensory interference, and pressure
- `Sauri` naturally extends control, positional pressure, and direct combat

That means each species backfill should also strengthen the runtime in a
coherent band instead of scattering engine work across unrelated surfaces.

---

## Technique Sequence Rule

Within a species backfill, porting should proceed in the same order that best
supports **historical and comparative testing**:

1. earliest authored Techniques that reuse existing runtime surfaces
2. earliest authored Techniques that need only small new effect types
3. earliest authored Techniques that need new procedural state families
4. later authored Techniques only after earlier missing siblings are covered

This keeps the simulator usable for “start from the first Technique and keep
going” validation instead of producing a spotty late-era-only test bed.

---

## Recommended Immediate Next Batch

### Zarnag

Best next batch after the currently-ported six:

1. `Ensuciar la Herida`
2. `Quebrar la Vuelta`
3. `Soltar la Capa Muerta`
4. `Hacer Esperar la Podredumbre`

Why this batch:

- it exercises recovery / pressure support
- it exercises reactions further
- it exercises warning and tempo
- it stays close to already-supported ATB and exchange surfaces

After this first batch, continue with the remaining Zarnag authored set in
authored-order unless a later Technique is required to unblock an earlier one.

### Naghii

Best first batch:

1. `Pesar el Umbral`
2. `Nublar la Señal`
3. `Marcar la Lectura`

Why:

- it opens the `Hidden` / fear relationship from another species
- it forces us to formalize procedural sensory states
- it is a good bridge between concealment and non-ailment state design

### Sauri

Best first batch:

1. `Barrer la Orilla`
2. `Sellar la Presa`
3. `Devolver al Cauce`

Why:

- these anchor direct interaction with already-modeled ailments
- they test melee exchange under control pressure
- they help validate injury/control tempo under ATB

---

## Porting Checklist Per Technique

Before calling a Technique simulation-ready, verify:

- `sim definition exists`
- `roll family is canonical`
- `cost is authored`
- `requirements are minimally represented`
- `effect surface exists in engine`
- `duration / timing model is explicit`
- `policy can choose it`
- `at least one test proves it resolves`
- `at least one scenario can expose it`

---

## Working Rule

Do not port by species-completion alone.

Port by **interaction value**:

- what new runtime surface it validates
- what current policy blind spot it closes
- what design question it unlocks

That way retroactive porting strengthens the simulator instead of only
inflating coverage counts.

Also:

- prefer **backfill continuity** over novelty
- prefer **earlier missing authored Techniques** over later attractive ones
- only break authored-order when a small runtime dependency must be built first

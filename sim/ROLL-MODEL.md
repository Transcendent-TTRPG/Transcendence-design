# Roll Model

## Purpose

This document defines the canonical roll families used by the simulation layer.

It does three jobs:

- normalize the game's authored roll formulas into one simulation-facing model
- make explicit which components belong to each roll family
- define how bonuses, penalties, thresholds, and opposed resolution should be treated

This document does not define action legality, ATB timing, or ailment persistence.
It only defines how rolls are built and compared.

## Shared Structure

Every roll family starts from one of these two structures:

- **opposed roll**
- **threshold roll**

### Opposed Roll

Two parties roll and compare totals directly.

- attacker wins if `attacker_total > defender_total`
- defender succeeds if `defender_total >= attacker_total`

This is the default structure for:

- `A.R.` against `D.R.`
- watched concealment against active detection
- techniques that explicitly say they are opposed by another roll

### Threshold Roll

One party rolls against a fixed target.

- success if `roll_total >= target`
- failure if `roll_total < target`

The target is:

```text
difficulty target = difficulty base + reference level
```

Threshold rolls are the default structure for:

- most `S.R.`
- most `C.R.`
- most `R.R.`

unless a rule explicitly says they are opposed instead.

## Modifier Policy

The simulator treats modifiers in four families:

- **characteristic contribution**
- **competency contribution**
- **bonuses**
- **penalties**

### Characteristic Contribution

This is the relevant aptitude of the acting or resisting creature.

It may be:

- a direct characteristic like `Agility`
- a specialization's associated characteristic like `Presencia` for `Sigilo`
- a derived characteristic like `Resilience / Resiliencia`

### Competency Contribution

Whenever a formula references a trained competency, the simulator expands that competency into:

```text
competency contribution = competency level + rank bonus
```

This applies to:

- weapon competencies in `A.R.` and `I.R.`
- `Evasion` in `D.R.`
- specializations in `S.R.`
- resistance competencies in `R.R.`

### Bonuses

Bonuses are positive modifiers from:

- environment
- equipment
- active techniques
- traits
- temporary effects

#### Scene Bonus Rule

Only **one positive scene bonus** may apply to the same roll from the same scene layer.

In current simulator policy:

- the environment provides the default positive scene bonus
- scenario-local positive scene bonuses should not stack on top of that unless a future rule explicitly changes the policy

### Penalties

Penalties may stack if they come from different valid sources.

Examples:

- hostile weather
- medium or heavy equipment burden
- ailments
- partial restraint
- visibility degradation

The simulator should sum applicable penalties unless a specific rule says otherwise.

## Roll Families

## Attack Roll (`A.R.`)

Used when an offensive action attempts to connect.

Canonical simulation formula:

```text
A.R. = 1d10 + associated characteristic + competency level + competency rank bonus + bonuses - penalties
```

Normal sources:

- weapon competency
- technique attack competency
- thrown-object competency
- other declared offensive execution domain

Common comparison targets:

- `D.R.`
- `R.R.` when a rule explicitly resolves that way
- another opposed offensive or reactive roll

### Runtime Feed for `A.R.`

To resolve `A.R.` faithfully, the simulator must know:

- the concrete weapon or offensive implement being used
- the competency tied to that weapon or implement
- the associated characteristic of that weapon or implement
- bonuses and penalties from stance, techniques, environment, traits, or ailments

## Defense Roll (`D.R.`)

Used when a creature tries to avoid an incoming offensive line.

Canonical simulation formula:

```text
D.R. = 1d10 + applicable evasion contribution + applicable agility + defensive bonuses - penalties
```

Where:

```text
applicable evasion contribution = applicable evasion level + applicable evasion rank bonus
```

### Armor-Constrained Applicability

The hit zone determines which armor type constrains defense:

- `unarmored` or `light`
  - full evasion
  - full agility
- `medium`
  - full evasion
  - half agility, minimum `1`
- `heavy`
  - half evasion, minimum `1`
  - agility `0`

Shield bonuses, defensive technique bonuses, and similar effects are added in the bonus layer.

### Runtime Feed for `D.R.`

To resolve `D.R.` faithfully, the simulator must know:

- the defended zone
- the armor type covering that zone
- the creature's `Evasion` competency
- the creature's `Agility`
- passive shield bonus if present
- extra defensive bonuses and penalties from techniques, scene, or ailments

This means `D.R.` is not just a generic competency roll. It is a zone-aware roll family.

If `D.R.` fails, impact and block still resolve afterward if the attack structure uses them.

## Impact Roll (`I.R.`)

`I.R.` is not a `d10` roll family.

It is resolved after an offensive line connects and determines how much damage pressure gets through before block, mitigation, and wound handling.

Canonical simulation structure:

```text
I.R. = (competency rank number × weapon damage dice) + (associated characteristic × weapon grade)
```

Untrained structure:

```text
Untrained I.R. = ((1 × weapon damage dice) + (associated characteristic × weapon grade)) / 2
```

`I.R.` should remain a separate damage-resolution model, not a `d10` competency roll.

### Runtime Feed for `I.R.`

To resolve `I.R.` faithfully, the simulator must know:

- the concrete weapon item
- its damage die
- the competency rank number with that weapon competency
- the associated characteristic of that weapon
- the weapon grade

## Characteristic Roll (`C.R.`)

Used when a task depends on general aptitude rather than specific practiced training.

Canonical simulation formula:

```text
C.R. = 1d10 + characteristic + reference level + bonuses - penalties
```

`C.R.` does not use competency level or rank.

It is the default fallback when:

- no specialization fits better
- the task is too generic to justify trained execution
- the fiction calls for raw aptitude rather than domain practice

## Specialization Roll (`S.R.`)

Used for trained domains such as climbing, tracking, medicine, traps, stealth, and similar practiced execution.

Canonical simulation formula:

```text
S.R. = 1d10 + associated characteristic + competency level + competency rank bonus + bonuses - penalties
```

### Untrained `S.R.`

If a creature lacks the specialization:

```text
Untrained S.R. = 1d10 + associated characteristic + bonuses - penalties
```

with:

- level = `0`
- rank bonus = `0`

`S.R.` can be:

- threshold-based
- opposed

depending on the authored action or technique.

## Resistance Roll (`R.R.`)

Used when the body, mind, or essence resists a harmful effect.

Simulation normalization expands "corresponding resistance" into the same trained contribution structure used elsewhere:

```text
resistance contribution = resistance level + resistance rank bonus
```

### Canonical `R.R.` formulas

| Effect family | Formula |
| --- | --- |
| Poison | `1d10 + Tenacity + poison resistance contribution + bonuses - penalties` |
| Infection | `1d10 + Tenacity + infection resistance contribution + bonuses - penalties` |
| Affliction | `1d10 + Composure + affliction resistance contribution + bonuses - penalties` |
| Curse | `1d10 + Composure + curse resistance contribution + bonuses - penalties` |
| Alteration | `1d10 + Resilience + alteration resistance contribution + bonuses - penalties` |

`R.R.` does not use Learning Advantage by default.

### Runtime Feed for `R.R.`

To resolve `R.R.` faithfully, the simulator must know:

- the effect family being resisted
- the base characteristic for that family
- the actor's trained resistance in that family, if any
- bonuses and penalties from environment, traits, gear, or techniques

Unlike `D.R.`, `R.R.` is not zone-aware by default.
Unlike `S.R.`, it does not represent voluntary execution and should not use Learning Advantage unless a specific rule says so.

## Personality Roll (`P.R.`)

This family exists in the game, but it is not yet modeled in the simulator.

Current authored structure:

```text
P.R. = 2d10
```

It should remain explicitly separate from `C.R.` and `S.R.` when added later.

## Canonical Characteristic Resolution

The simulator must resolve both direct and derived characteristics.

### Direct characteristics

- Strength / `Fuerza`
- Agility / `Agilidad`
- Tenacity / `Tenacidad`
- Intellect / `Intelecto`
- Cunning / `Astucia`
- Wisdom / `Sabiduría`
- Composure / `Compostura`
- Aura
- Presence / `Presencia`

### Derived characteristics

- Preparation / `Preparación`
- Resilience / `Resiliencia`

Current canonical derived formula needed by roll resolution:

```text
Resilience = ceil((Tenacity + Wisdom + Composure) / 3)
```

## Simulator Implementation Rules

The simulator should expose explicit helper functions for:

- `attack_roll`
- `defense_roll`
- `specialization_roll`
- `untrained_specialization_roll`
- `characteristic_roll`
- `resistance_roll`
- `resolve_opposed`
- `resolve_threshold`

It should also expose canonical helpers for:

- associated specialization characteristic lookup
- resistance-family base characteristic lookup
- derived characteristic resolution
- armor-constrained defense applicability

## Current Status

Already implemented or partially implemented:

- `S.R.` formula
- `C.R.` formula
- generic trained competency expansion
- threshold resolution
- opposed resolution
- first environment bonus / penalty policy

Still to deepen:

- explicit `A.R.` usage in runners
- armor-constrained `D.R.` helpers in live experiments
- full `R.R.` family runners
- `I.R.` damage-resolution modeling
- eventual `P.R.` support

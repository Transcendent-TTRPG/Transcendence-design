# Damage Models

## Purpose

This document defines the two canonical damage-model families the simulator must support.

They are not interchangeable:

- `player_wounds`
- `creature_zones`

The simulator must never assume that every combatant uses the same post-impact consequences.

## 1. Player Wounds

This model is used for player characters and any runtime actor that should behave like a player body.

Core properties:

- five canonical humanoid-readable zones
  - `head`
  - `torso`
  - `arms`
  - `legs`
  - `feet`
- each zone has wound slots
- connected hits become:
  - no wound
  - light wound
  - grave wound
  - critical wound
- wounds occupy slots
- full occupation causes saturation
- overflow causes collapse
- vital collapse may force `Alteration R.R.`

This is the model currently implemented by:

- `engine/exchange.py`
- `engine/block.py`
- `engine/wounds.py`
- `engine/zones.py`

## 2. Creature Zones

This model is used for NPCs, monsters, beasts, bosses, and any hostile or neutral entity that should not use PC wound slots.

Core properties:

- up to five authored macro-zones for readability
- zones do not have to be humanoid
- each zone may define:
  - `max_hp`
  - `block`
  - `dr_bonus`
  - `durability`
  - `linked_abilities`
  - `vital`
- abilities are tied to zones
- breaking or disabling a zone can remove those abilities

Examples:

- `jaw` may support:
  - `bite`
  - `frost_breath`
- `wings` may support:
  - `flight`
- `central_eye` may support:
  - `beam_control`

The simulator should allow these zones to replace generic HP-only reading while staying legible.

## Why the Split Matters

Player combat asks:

- how much bodily function is lost locally?
- how many slots are occupied?
- is the zone saturated or collapsed?

Creature combat asks:

- which zone was damaged?
- how much reserve remains in that zone?
- what abilities are now disabled?
- did a breakable part stop supporting a core attack, movement mode, or phase mechanic?

These are different questions and must not be forced into one shared wound table.

## Profile Declaration

Each simulation profile should declare:

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
      dr_bonus: 1
      durability: 4
      linked_abilities:
        - bite
        - frost_breath
```

## Runtime Consequence

At instantiation time:

- `player_wounds`
  - gets canonical wound-slot zones in runtime
- `creature_zones`
  - gets authored creature zone states in runtime

The two models should coexist under the same combat exchange layer, but they must diverge after:

- `A.R.`
- `D.R.`
- `I.R.`
- `Block`

At that point the simulator must branch into:

- player wound resolution
- creature zone / part resolution

## Current Status

Implemented:

- damage-model declaration on profiles
- runtime separation between `zones` and `creature_zones`
- seed creature profile with linked abilities
- helper lookup for active linked abilities
- authored creature-zone `D.R.` bonuses
- authored creature-zone `Block`
- creature-zone damage application by local HP
- linked-ability disablement when a creature zone falls
- vital-zone shutdown flagging
- critical-potency break attempts against creature zones
- durability degradation on failed valid break attempts
- creature-zone disablement from structural break, not only HP depletion

Still pending:

- boss phase or vital-point escalation

# Creatures

This document defines the creature system for Transcendence: design doctrine,
nature, category, zones, traits, cycles, and roll formulas.

NPCs use PC rules. This document governs all other entities — Mortales, Anomalías,
and Primordiales — regardless of category.

For the ATB mechanics of autonomous cycles, see [`creature-cycles.md`](creature-cycles.md).

---

## Foundational doctrine: the body explains behavior

Zones are not anatomical divisions assigned to fit a template. They are the
physical locations where the creature's behaviors live.

A creature that breathes ice has a zone for the organ that produces the breath.
A creature that regenerates tissue has a zone for the gland that drives it.
A creature that sweeps with its tail has a tail zone. If a behavior has no zone,
the behavior is not a behavior — it is an abstraction. Abstractions do not belong
in creature design.

**Start from what the creature does. Zones follow.**

1. List all intended behaviors: attack types, defensive responses, recurring
   effects, environmental presence.
2. Identify the body part that enables each behavior.
3. Those are the zones.
4. Assign HP and Bloqueo based on zone type, nature, and role.

When a zone collapses, the behavior tied to it stops. Players targeting zones are
not depleting a resource — they are dismantling a living system. The tactical
problem is not "how much HP does it have left" but "which behavior to disable first
and what the creature does when it loses it."

---

## Nature

Nature describes the creature's biological composition and Tauma relationship.
It is independent of power level. A Mortal creature is not weaker than an Anomalía
by definition — its nature describes what it is made of, not how dangerous it is.

### Mortal

Purely biological. No Tauma in composition or internal processes. Resistance to
elemental damage is natural — hides, shells, density, mass — and expressed through
Bloqueo values on relevant zones.

### Anomalía

Biological base with Tauma present in internal processes. The Tauma is part of
their metabolism, not an ability they activate or control. Elemental affinity:
50% damage reduction from their affiliated element. Elemental vulnerability:
+50% damage from their opposing element.

### Primordial

Entities composed entirely of Tauma. No conventional biological structure. Elemental
affinity: 100% damage reduction from their affiliated element. Elemental
vulnerability: +100% damage from their opposing element.

For Primordiales, attacks that reach body zones unrelated to their structural
logic deal 0 damage. Meaningful damage requires that players understand the
creature's composition well enough to identify what to target.

---

## Category

Category defines the creature's role in the ecosystem and the scope of its
autonomous cycles. It does not determine power — that is NR. It determines
what kind of presence the creature has in the world and in an encounter.

### Común

Represents the general population of a species. No special organizational role.
Autonomous cycles are strictly biological: they express the creature's own
physiology — how it charges an elemental ability, how its body recovers, how
it shifts posture between attacks.

### Campeón

A powerful individual that commands or coordinates a group. Autonomous cycles
include biological cycles and cycles tied to ally coordination — abilities that
function because other creatures are present and that modify how those allies
behave (Preparation, access to tactics, Bloqueo, positioning).

### Elite

An exceptional individual beyond any other member of its species. Autonomous
cycles include biological cycles and environmental cycles — processes that change
the battlefield itself: visibility, terrain, elemental conditions, spatial
stability.

Elite creatures are not stronger Comunes or Campeones. They are encounters that
change the nature of the space the players are in.

Elite creatures also have:

**Metamorfosis** — Phases triggered when specific zones collapse. Each phase
changes behaviors, available cycles, and environmental conditions. The phases
are not telegraphed to players; they learn what each collapse triggers through
the encounter.

**Apoteosis** — A final phase entered after all Metamorfosis phases complete.
Grants the creature +3 to all attack rolls. Reduces the critical threat range
for players attacking it by 1 (a 10 on d10 is still a critical; the range
expands downward based on creature definition).

**Golpe Final** — The specific coordinated action that ends the creature during
Apoteosis. Defined per creature. Requires threshold damage delivered through a
declared coordinated attack. Until the Golpe Final is executed, the creature in
Apoteosis cannot be reduced below 1 HP in any zone.

---

## Role

Role defines the creature's combat function and modifies HP across all zones.

| Role | HP multiplier | Function |
| --- | --- | --- |
| Protector | × 2 | Absorbs attacks; protects Comunes; prioritizes Bloqueo |
| Golpeador | × 1.5 | Primary damage source; zone-targeting attacks |
| Lanzador | × 1 | Ranged or elemental attacks; lower zone HP |
| Soporte | × 1 | Coordinates allies; applies conditions; enables others |

---

## NR offset by category

When building an encounter, select creature NR relative to the group NR (NRg):

| Category | NR offset | Threat level |
| --- | --- | --- |
| Común | NRg + 1 to 2 | Relevant challenge; demands attention |
| Campeón | NRg + 3 to 5 | Serious threat; requires tactical approach |
| Elite | NRg + 6 to 10+ | Existential threat; requires preparation, knowledge, and coordination |

These ranges are calibration starting points. Adjust based on group composition,
available information about the creature, and how much preparation the players
have had.

---

## Zone system

### Zone types

Once behaviors and their body parts are identified, assign each zone to a type:

| Type | What it is | HP base | Bloqueo base |
| --- | --- | --- | --- |
| Núcleo | The zone the creature cannot function without. Collapse ends the creature or triggers a major phase. | NR × 4 | NR × 2 |
| Estructura | Load-bearing mass. No specific behavior tied to it, but sustains everything else. | NR × 6 | NR × 1.5 |
| Apéndice | A zone tied to a specific behavior: a limb, organ, or appendage. Collapsing it stops that behavior. | NR × 3 | NR × 1 |

Apply the role multiplier to HP. Apply the nature multiplier to Bloqueo:

| Nature | Bloqueo multiplier |
| --- | --- |
| Mortal | × 1 |
| Anomalía | × 1.5 |
| Primordial | × 2 |

### Damage to zones

Damage to a zone = Impact − Bloqueo (minimum 0). Applied directly to that zone's
HP. No wound tracking, no ranuras. The Narrator tracks one number per zone.

### Zone collapse

When a zone reaches 0 HP:
- The zone is destroyed
- Any technique or autonomous cycle anchored to that zone is disabled and removed
  from the ATB
- The creature's behavior changes as defined in the creature's entry
- If Elite: this may trigger a Metamorfosis phase

### Creature defeat

A creature is defeated when its Núcleo zone collapses, or — for Elite only —
when the Golpe Final is successfully executed during Apoteosis.

Collapsing non-Núcleo zones does not defeat the creature. It changes what the
creature can do.

---

## Traits (Rasgos)

Traits grant creatures conditional Ventaja de Ejecución. A creature with an active
trait is better than its base rolls when its condition is met.

### Trait structure

| Element | Definition |
| --- | --- |
| Trigger condition | The state that must be true |
| Effect | Ventaja de Ejecución on a specific roll type (T.A., T.D., T.R., T.E.) |

A trait does not modify numbers. It determines which die to keep. All other rules
for Ventaja de Ejecución apply.

### Trait categories

| Category | Trigger type |
| --- | --- |
| Behavior | What the creature or opponent has done in this encounter |
| Environment | Where the creature is, or what conditions are active |
| Emotional state | Health state, ally state, or enemy state |
| Battle role | Position the creature occupies in the encounter |
| Nature | Triggered by Mortal / Anomalía / Primordial status |
| General | Cross-cutting or unconditional conditions |

### Discovering and neutralizing traits

Traits are not visible to players by default. To identify a trait:
- Successful T.E. of Identificación, Interpretación, or Medicina during combat
  reveals one trait and its trigger condition
- The roll reveals that the condition exists and what it is; players must act on
  that knowledge to neutralize it

When players neutralize the trigger condition, the creature loses Ventaja de
Ejecución on that roll. It then uses **Ventaja de Aprendizaje** — roll 2d10,
keep the lower die for execution, use the higher die toward learning. The creature
marks progress on the relevant behavior. Progress accumulates across the encounter.

This is the core tactical loop: find traits, neutralize their conditions, act
quickly — because a creature under pressure learns, and a creature with multiple
active cycles accumulates progress fast.

---

## Autonomous cycles

Autonomous cycles are separate ATB entries representing behaviors that operate
independently of the creature's main turn.

For full ATB mechanics, see [`creature-cycles.md`](creature-cycles.md).

**Scope by category:**

| Category | Cycle scope |
| --- | --- |
| Común | Biological only: physiology, elemental charging, posture, regeneration |
| Campeón | Biological + ally coordination: cycles that modify nearby allies |
| Elite | Biological + environmental: cycles that modify the battlefield |

**Quantity:** Determined by NR and creature complexity, not by category. A Mortal
Común with NR 8 may have four biological cycles. Category defines what kinds of
cycles are available, not how many.

**Zone anchoring:** Biological cycles are tied to the zone that drives them. When
that zone collapses, the cycle is removed from the ATB. Environmental cycles
(Elite only) are not tied to any specific zone — they are a property of the
creature's presence in the space. They persist through Metamorfosis phases unless
the creature design specifies otherwise, and end with the creature's defeat.

---

## Roll formulas

All creature rolls use NR as the primary scaler. Characteristics are defined per
creature based on anatomy and role.

| Roll | Común | Campeón | Elite |
| --- | --- | --- | --- |
| T.A. | 1d10 + NR + characteristic | 1d10 + ⌈NR × 1.5⌉ + characteristic | 1d10 + NR × 2 + characteristic |
| T.D. | 1d10 + NR + characteristic | 1d10 + ⌈NR × 1.5⌉ + characteristic | 1d10 + NR × 2 + characteristic |
| T.R. | 1d10 + NR + characteristic | 1d10 + ⌈NR × 1.5⌉ + characteristic | 1d10 + NR × 2 + characteristic |
| T.E. | 1d10 + NR + characteristic | 1d10 + ⌈NR × 1.5⌉ + characteristic | 1d10 + NR × 2 + characteristic |
| T.I. | damage × ⌈NR / 3⌉ + characteristic | damage × ⌈NR / 2⌉ + characteristic × 2 | damage × NR + characteristic × 3 |

⌈x⌉ = round up

These are calibration baselines. Adjust per creature if specific behaviors warrant
different roll weights across zones or attack types.

---

## Creature design workflow

Follow this order. Skipping steps produces creatures where numbers exist but
behavior does not, or behavior exists but the body cannot explain it.

1. **Define what the creature does in combat.** List all intended behaviors:
   attack types, defensive responses, recurring effects, environmental presence.

2. **Identify the body part that enables each behavior.** This is not optional
   flavor — it is the design work. If you cannot identify a body part for a
   behavior, the behavior is not ready to be authored.

3. **Assign each zone a type** (Núcleo / Estructura / Apéndice) based on its
   function, not its anatomical position. The throat of a fire-breathing creature
   may be Núcleo if everything depends on it.

4. **Set nature, category, and role.** This gives you NR offset, cycle scope,
   HP multipliers, and Bloqueo multipliers.

5. **Apply zone formulas.** HP and Bloqueo per zone are now derived, not invented.

6. **Write the techniques** anchored to their zones.

7. **Write the autonomous cycles** anchored to their zones (biological), or as
   environmental presence (Elite environmental cycles). Respect category scope.

8. **Write the traits.** For each trait: trigger condition, roll affected, how a
   player can discover it.

9. **Define zone collapse consequences.** For each zone: what behavior stops? What
   cycle is removed from the ATB? If Elite, does this trigger a Metamorfosis phase?

10. **If Elite: define Metamorfosis phases and Apoteosis.** Each phase triggers on
    a specific zone collapse. Each phase changes something about the encounter —
    behaviors, cycles, or environment. Apoteosis and Golpe Final close the encounter.

---

## Reference map

| Resource | Path |
| --- | --- |
| Autonomous cycle ATB mechanics | `docs/system/creature-cycles.md` |
| Ailments catalog | `data/system/ailments.yaml` |
| Weapon technique profiles | `data/system/weapon-technique-profiles.yaml` |
| Mechanics overview (all game systems) | `docs/system/mechanics-overview.md` |
| NR definition and calculation | `docs/system/general-rules.md` |
| Size and scale | core-books chapter 08 `08-tamaño-y-escala.md` |

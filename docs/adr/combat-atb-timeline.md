# ATB Combat Timeline

**Status:** Adopted (structural design)
**Scope:** Combat timing, action order, encounter pressure, boss layering, reactive play
**Related systems:** Combat, Encounter Architecture, Vital Points, Fatigue, Readability, Team Tactics
**Related files:**

- `docs/adr/combat-encounter-architecture.md`
- `docs/adr/combat-enemy-readability.md`
- `docs/adr/combat-champion-encounter.md`

---

## Purpose

This document defines the structural model of combat timing in Transcendence.

Its purpose is to replace the traditional round-based turn order used by many fantasy RPGs with a system where combat flows through **relative timing**, **action cost**, and **continuous pressure** rather than through fixed "one turn per creature per round" sequencing.

The ATB model exists to solve several design goals at once:

- prevent combat from feeling like a rigid exchange of isolated turns
- make fast and slow actions feel meaningfully different
- allow reactions and tactical interruption without relying on special exceptions
- let encounters function as layered systems instead of single stat blocks
- reduce the need to inflate difficulty through extra monsters alone
- make bosses feel like active situations rather than large HP containers

---

## Core Principle

Combat is not divided into rounds.

Combat is represented by a **timeline of action readiness**.

Each creature, subsystem, or encounter element that matters in combat occupies a position on the timeline. The entity whose marker is currently furthest to the left is the next one able to act.

When that entity acts, its marker moves to the right according to the rhythm cost of the chosen action.

The system therefore does not ask:

> "Whose turn is it this round?"

It asks:

> "Who is ready to act first, and how much will this action delay their next opportunity?"

---

## Why ATB Exists

Traditional round-based systems create a recurring structural problem:

- the player side often has many full turns
- a powerful enemy often has only one
- therefore difficulty is frequently stabilized by adding more bodies, not by deepening the encounter itself

This leads to familiar failures:

- bosses collapse before they can express their full design
- encounters depend too much on filler enemies
- the battlefield often feels static between one creature's turn and the next
- speed and momentum are mostly abstracted away

The ATB model solves this not by simply giving bosses more raw actions, but by allowing the encounter to exist in **multiple temporal layers**:

- main bodies
- charged systems
- tactical cycles
- environmental pressure
- triggered responses

This lets a fight feel like a whole situation instead of a queue of isolated units.

---

## The Timeline

The combat timeline is represented by a horizontal track.

Every relevant combat entity has a marker on that track.

Examples of possible tracked entities:

- player characters
- enemy creatures
- champion tactical systems
- elite subsystems
- environmental cycles
- charged abilities that deserve their own timing

The marker furthest to the left acts first.

After resolving an action, that marker moves right by the action's rhythm cost.

---

## Initial Track Position

Combat does not begin from a neutral state. Before the first activation, every entity receives an **initial position on the track** based on their readiness at the moment the scene begins.

### Calculating initial position

Initial position = **Preparación** + situational modifiers

Preparación is the derived characteristic that expresses readiness, alertness, and combat composure. A higher value means the entity is better positioned to act first.

Situational modifiers adjust this based on conditions at the start of the scene:

| Situation | Modifier |
| --- | --- |
| Ambushing | +2 |
| Weapon drawn / prepared stance | +1 |
| Cover or dominant position | +1 |
| Target exposed or distracted | +1 |
| Surprised | −2 |
| Drawing weapon or reorganizing | −1 |
| Unfavorable immediate terrain | −1 |
| Asleep, wounded, disoriented, or poorly positioned | −1 to −3 depending on severity |

Entities with a **higher readiness score** are placed **further left** on the track and therefore act sooner. From that starting position, all subsequent movement follows the normal rhythm cost rules — actions move markers to the right.

The initial positioning phase is not separate from the track. It is the track's starting state. Rhythm costs stack on top of it from the first activation onward.

---

## What a Marker Represents

A marker does not represent abstract "initiative score" in a static sense.

It represents:

- recovery from the last action
- readiness to act again
- the rhythm imposed by a chosen behavior
- the pace at which a body, system, or threat can sustain meaningful pressure

A fast action causes a smaller displacement. A heavy or demanding action causes a larger displacement.

Because of this, the ATB system models timing dynamically instead of front-loading everything into one initiative roll.

---

## Action Rhythm

Every meaningful action has a **rhythm cost**.

Rhythm cost represents how much that action delays the next opportunity to act.

This does not automatically mean the same thing as Desgaste. Both are related to the action's demand, but they are separate dimensions:

- **Rhythm cost** determines when the next opportunity happens
- **Desgaste** determines how much strain the action imposes on the character

A very fast action may still be demanding. A slow action may be deliberate more than exhausting. The same action may become rhythmically cheaper, less exhausting, or both depending on training and context.

### Rhythm and strain rule

> The demand of an action influences both rhythm and strain, but they are not always identical values.

---

## Suggested Rhythm Bands

The exact numeric calibration may evolve, but the structural bands are:

- **Quick action** → low rhythm cost
- **Standard action** → medium rhythm cost
- **Heavy action** → high rhythm cost
- **Extreme action** → very high rhythm cost

These bands are enough to make timing matter without forcing every action to have a unique bespoke formula from the beginning.

---

## Activation

When a marker reaches the leftmost current position, that entity becomes the next to act.

The acting entity chooses an available action, resolves it, and then moves its marker according to the action's rhythm cost.

This produces a combat flow where:

- short, efficient actions return sooner
- heavy commitments create bigger openings in tempo
- players can choose between speed, pressure, setup, defense, analysis, or overextension

---

## Tie Resolution

Two entities may occupy the same track position in two situations: at the start of the scene, if their Preparación + situational modifiers produce the same readiness score; or during combat, if rhythm costs bring two markers to the same point.

In both cases, resolve the tie by **raw Preparación value** (before situational modifiers are applied). The entity with the higher base Preparación acts first.

If raw Preparación is also tied, the Narrator or table may break the tie according to the needs of clarity, consistency, or a fixed secondary rule chosen by the group.

### Why raw Preparación matters here

Using base Preparación as the tiebreaker ensures that the entity who is fundamentally more alert and composed gets the edge — independent of situational luck. Preparación already expresses readiness, alertness, adaptability, and combat composure, making it the correct stat to resolve deadlocks without overriding the track structure.

---

## No Round Structure

The ATB model does not use rounds as the primary unit of combat.

There may still be moments where the Narrator refers informally to a "cycle of exchanges" or similar pacing language, but mechanically the system should not depend on:

- "once per round"
- "at the start of the round"
- "until your next round"

Instead, timing should be phrased through:

- track position
- next activation
- completion of a subsystem
- the end of a hostile scene
- explicit duration markers if needed

This keeps the system aligned with continuous tempo rather than turn blocks.

---

## Reactions

Reactions exist within the ATB model, but they are not exempt from timing.

A reaction is simply an action taken outside the normal flow of one's next planned activation, usually because a trigger condition allowed it.

This means reactions:

- still have rhythm cost
- may still generate Desgaste
- may still expose the character to future timing loss

They are not "free actions." They are timing exceptions that still belong to the same economy.

### Reaction timing rule

> A reaction is not free because it is reactive. It is permitted because the trigger allows it.

This lets the game support active tactical defense, interruptions, saves, counters, and protective play without needing a separate "reaction resource" structure identical to D&D-like systems.

---

## Telegraphs, Windows, and Resolution

Major threats should often unfold in three parts:

### 1. Preparation / Telegraph

The enemy or subsystem makes its intention visible.

Examples:

- the throat swells with frost
- the champion draws breath for a command roar
- the ground begins to crack
- the ritual focus lights up
- the tail coils before a sweep

### 2. Response Window

The players have time to:

- move
- read
- guard
- interrupt
- prepare
- sacrifice tempo for protection
- exploit an opening
- damage the subsystem before it resolves

### 3. Resolution

The ability, subsystem, or environmental effect triggers.

This structure is critical because it makes timing readable and interactive. Players are not just passively receiving effects; they are reading tempo and choosing how to respond to it.

---

## Subsystems in the ATB

Not every meaningful encounter element is a full creature. Some parts of an encounter deserve timing of their own.

Examples:

- breath cycle
- sweeping tail
- command pulse
- ritual buildup
- collapse sequence
- environmental vent cycle

These may appear in the ATB as **secondary tracks**.

A subsystem should receive its own track if:

- players can meaningfully interact with it
- its timing creates real pressure
- it is not captured well enough by simply modifying the main body's track
- it contributes to encounter identity

A subsystem does not need a full creature stat block. It needs:

- a function
- a timing identity
- a way to be read
- a way to be altered, delayed, weakened, or allowed to resolve

---

## Main Body vs Subsystem

A main enemy body usually represents:

- movement
- primary offense
- direct targeting
- basic pressure

A subsystem usually represents:

- buildup
- area denial
- repeated functional threat
- environmental extension
- a specialized part of the creature or encounter acting with its own rhythm

Example: a frost beast may have:

- **main body track** → movement, bite, claw, rush
- **breath cycle track** → buildup and release of frost breath

The group is still fighting one coherent thing. But that thing is operating in more than one temporal layer.

---

## Encounter Layering

The ATB system works best when encounter design follows the same layered structure already adopted in `docs/adr/combat-encounter-architecture.md`.

### Common — ATB structure

- 1 main track
- 0 to 1 secondary systems

### Champion — ATB structure

- 1 main track
- 1 tactical or leadership system
- optionally simple allied units

### Elite / Boss — ATB structure

- 1 main track
- 2 to 3 secondary systems
- optional environmental layer
- phase changes and readable pressure shifts

This means bosses do not need to survive through HP inflation alone. They survive because the group must respond to multiple meaningful pressures across time.

---

## Common Enemies in ATB

A common enemy usually acts through:

- one body
- one readable pressure pattern
- one or two important vital points
- at most one secondary system

Its role is not to overwhelm with complexity, but to teach the grammar of timing, reading, disruption, prioritization, and rhythm control.

A common should still feel dangerous and should still be able to punish ignorance, but it should remain legible from within the encounter.

---

## Champions in ATB

Champions differ from commons primarily through **distributed pressure**, not just personal power.

A champion's encounter identity usually comes from:

- coordinated tactics
- leadership-based pressure
- enabling nearby units
- creating formation or pack behavior

A champion may therefore have:

- a main personal track
- a tactical or command subsystem track
- a small number of relevant subordinates

The champion is not merely "a stronger body." It is "a body plus a tactical structure."

---

## Elites / Bosses in ATB

An elite should never feel like one track, one big attack, one huge HP pool.

An elite should usually include:

- a main body track
- multiple important subsystems
- phase logic
- at least one way the space or environment is affected

The players should feel they are fighting a body, its functions, its timing, its space, and its pressure logic.

This is how the ATB system replaces the need for filler enemies as a default solution.

---

## Vital Points and Rhythm

Vital points are not only damage targets. They are rhythm-altering nodes.

Damaging a correct vital point may:

- delay a subsystem
- increase the rhythm cost of a pattern
- weaken the resolution of an attack
- remove a trigger
- break coordination
- force a phase transition
- simplify the encounter's tempo

If a vital point only changes damage numbers, it is underperforming in this system. The best vital points change how the encounter behaves in time.

---

## Competence and Tempo

Training should eventually affect ATB, but not all in the same way.

A competent character may make an action:

- faster
- less exhausting
- more stable
- more precise
- or any combination of the above

A short-blade specialist, for example, may perform a quick strike with lower rhythm cost, lower Desgaste, or both.

A perceptive analyst may not necessarily act faster, but may reduce the cost of reading or interpreting under pressure.

A defender may not speed up interception, but may reduce the strain or increase the reliability of protective timing.

### Competence rule

> Competence reduces execution friction. Depending on the action, that may reduce rhythm cost, Desgaste, or both.

Detailed interaction between competence and ATB can be expanded in more specific documents. The core principle is established here.

---

## Movement in the ATB

Movement should not be treated as a universal free appendage to every action.

Movement has rhythm cost, though the exact cost depends on:

- distance
- terrain
- urgency
- conditions
- whether the movement is controlled, forced, desperate, or opportunistic

Movement is therefore part of tempo, not a separate invisible layer.

This is important because in a system where environment matters, movement is one of the main ways players interact with pressure.

---

## Pressure, Tempo, and Fatigue

ATB and Fatigue are separate systems, but they are deeply compatible.

- ATB asks: **when can you act again?**
- Desgaste asks: **how much strain has this scene imposed on you?**
- Fatigue asks: **what remains after that strain settles?**

This means the same encounter can pressure characters in two ways:

1. by denying or delaying good timing
2. by forcing expensive choices repeatedly

A fight therefore becomes hard not because it has "more monsters," but because it makes players spend rhythm, attention, positioning, and Desgaste at the same time.

---

## Table Clarity

The ATB system only works if the table can read it clearly.

Therefore:

- telegraphed threats should be visible
- subsystem tracks should be few and meaningful
- the track should never be overloaded with noise
- players should understand what each marker represents
- a subsystem should not exist unless its timing matters

Complexity should come from layered choices, not from unreadable bookkeeping.

---

## Checklist for Using the ATB in Encounter Design

### Step 1 — Define the main track

What is the enemy's body or primary pressure?

### Step 2 — Define the threat rhythm

What patterns are quick, standard, heavy, or extreme?

### Step 3 — Decide whether a function deserves its own track

Would this be more readable and more interactive as a subsystem?

### Step 4 — Link vital points to timing

What happens to tempo if players damage the correct node?

### Step 5 — Build telegraphs

How do players realize something is about to happen?

### Step 6 — Build response windows

What can players do before it resolves?

### Step 7 — Check table load

Is this still easy enough to read and run?

---

## Official Decisions Adopted

1. Combat uses a continuous ATB timeline rather than round-based sequencing.
2. The leftmost marker acts first.
3. Actions move their marker right according to rhythm cost.
4. Rhythm cost and Desgaste are related, but not identical.
5. Reactions exist inside the same timing economy and are never automatically free.
6. Telegraph → window → resolution is the preferred structure for major threats.
7. Secondary systems may enter the ATB when they are meaningful, readable, and interactive.
8. Boss pressure should be solved through layered timing, not only HP inflation or filler adds.
9. Vital points should alter encounter rhythm and pressure, not only damage values.
10. The number of active tracks should remain proportional to encounter category and table readability.
11. Initial track position = Preparación + situational modifiers. Higher readiness score = placed further left. Rhythm costs stack on top of this initial state from the first activation onward. Ties resolved by raw Preparación, then narrator discretion.

---

## Open Questions

1. What exact rhythm costs should be assigned to core action bands in final calibration?
2. Which actions should be able to reduce rhythm cost through competence, and by how much?
3. When should a subsystem become a full track instead of a triggered sequence or countdown?
4. How many reactive windows can a boss sustain before the fight becomes too dense?
5. What is the best table format for visualizing track state without clutter?

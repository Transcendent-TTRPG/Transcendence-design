# Encounter Architecture by Enemy Category

**Status:** Adopted (structural design)
**Scope:** Encounter design, ATB integration, vital points, boss pressure, enemy category identity
**Related systems:** Combat, ATB, Enemy Readability, Vital Points, Fatigue, Environmental Pressure, Team Tactics
**Related files:**

- `docs/adr/combat-atb-timeline.md`
- `docs/adr/combat-enemy-readability.md`
- `docs/adr/combat-champion-encounter.md`

---

## Purpose

This document defines how encounters should be structured across the three major enemy categories of the system:

- **Common**
- **Champion**
- **Elite / Boss**

Its purpose is to prevent encounters from being built primarily through numeric inflation or by simply increasing the number of enemies on the field. Instead, it establishes a model in which each encounter is designed as a set of **active combat systems**: body parts, functions, tactics, environmental pressures, and timing layers that together create a cohesive threat.

This extends the already adopted readability findings from the Ice Wolf case study, where common enemies were confirmed to work best when they can be read from inside the fight through friction, behavior, telegraphs, and functionally meaningful vital points (see `docs/adr/combat-enemy-readability.md`).

---

## Core Design Principle

An encounter is not designed as a creature with statistics and attacks.

An encounter is designed as a **combat organism**.

That organism may include:

- a body
- vital points
- repeated behavior patterns
- independent or semi-independent subsystems
- environmental influence
- leadership or coordination structure
- phase changes

The purpose of these elements is to make a fight feel like a whole situation rather than a single unit standing in an empty room trading blows until its HP runs out.

---

## Why This System Exists

Traditional turn-based fantasy combat often has a recurring structural problem:

- player groups usually have many turns
- bosses often have only one meaningful turn per cycle
- this causes bosses to collapse quickly unless the system compensates with inflated health, extra monsters, or artificial "bonus turns"

This system aims to solve that problem through **temporal layering**, not through simple numeric inflation.

Instead of making a boss survive by having more HP or more filler enemies, the encounter survives by existing in more than one meaningful temporal layer at once.

That means:

- the enemy can threaten the group even when its main body is not currently acting
- the environment or linked systems can continue generating pressure
- the players must divide their attention between multiple active problems
- damaging the correct part of the encounter changes its structure, not just its health total

---

## Vital Points

A **vital point** is not merely a body part that receives damage.

A vital point is any part or system whose alteration changes, in a perceptible and tactically meaningful way, the encounter's ability to exert pressure.

This includes:

### Anatomical vital points

Examples:

- throat
- eyes
- legs
- claws
- tail
- sensory crest
- armored plate
- venom sac

### Functional vital points

Examples:

- pressure organ
- frost gland
- respiratory node
- resonance chamber
- stabilizing joint

### Behavioral or tactical vital points

Examples:

- command posture
- roar focus
- territorial anchor
- control node
- pack signal

### Environmental vital points

Examples:

- altar
- nest
- root network
- ritual circle
- ice formation
- vapor vents
- unstable bridge
- energy pillar

A vital point matters because it is tied to a **function**, not because it is simply present on the body.

---

## Vital Points and the ATB

Not every vital point becomes its own entity in the ATB.

A vital point may interact with the combat rhythm in one of three ways:

### 1. It generates a secondary track or ciclo autónomo

The point supports an active subsystem that deserves its own timing. This may take the form of a ciclo autónomo — a distinct ATB entry with its own rhythm cost and hidden timing (see `docs/system/creature-cycles.md`).

Examples:

- a throat charging breath (ciclo autónomo — biological)
- a tail preparing a sweeping strike
- a ritual focus building energy
- a collapse sequence in the terrain
- a coordination pulse the Champion emits (ciclo autónomo — coordination)

### 2. It modifies the main track

The point does not need its own independent cycle, but damaging it changes how the enemy's main track behaves.

Examples:

- damaged legs increase the rhythm cost of movement
- a broken jaw prevents or delays bite patterns
- injured wings reduce repositioning or aerial tempo

### 3. It changes environment, phase, or pressure

The point matters because it affects the structure of the encounter more broadly.

Examples:

- destroying a control node ends a fog effect
- disabling a command organ breaks coordinated tactics
- collapsing a support structure forces the boss into a new phase

---

## Active Layers

An encounter should not be measured only by how many enemies are present. It should be measured by how many **active layers of pressure** it is presenting.

An active layer is any element of the encounter that:

- creates timing pressure
- occupies player attention
- changes decision-making
- threatens the group independently or semi-independently

Examples of active layers:

- the enemy's main body
- a ciclo autónomo (biological, coordination, or environmental)
- a charged breath cycle
- a sweeping tail system
- a leadership tactic track
- an environmental collapse
- a ritual countdown
- a pack coordination loop

The more layers active at once, the more complex and dangerous the encounter feels.

---

## Layer Limits by Category

To keep encounters rich but still manageable in play, enemy categories should follow approximate limits for active visible layers.

### Common — active layers

- **1 main track**
- **0 to 1 secondary systems**
- **1 to 2 meaningful vital points**

A common enemy should be readable during the encounter itself and should create tactical interest without overwhelming the table. Its systems should be simple enough that players can grasp what matters through observation, friction, and focused attacks.

### Champion — active layers

- **1 main track**
- **1 tactical or leadership system**
- **0 to 1 support systems**
- **1 to 2 personal vital points**
- **1 to 3 meaningful allies or subordinates**

A champion does not need to be anatomically more complex than a common enemy. Its difference lies in its ability to coordinate others, alter formation pressure, and create team-based threats. A champion should feel like **a creature plus a tactical structure**.

### Elite and Boss — active layers

- **1 main track**
- **2 to 3 secondary systems**
- **0 to 1 strong environmental layer**
- **3 to 5 meaningful vital points or systems**
- **clear phase logic**

An elite or boss encounter should feel like a multifront problem. Players should not be fighting only a creature, but a body, its functions, its space, its pressure patterns, and its phase changes.

---

## Category Identity

### Common Enemies

Common enemies are the baseline serious threats of the world. They are still dangerous and can exceed an individual player's raw power, but their internal logic should be legible from inside the fight.

A common enemy should usually have:

- 1 central pressure pattern
- 1 or 2 clear vital points
- 1 major ability tied to a vital point
- 1 friction path to discovering that relationship

Common enemies should teach the core language of combat: observation, response, prioritization, disruption, and exploiting vulnerable functions instead of simply dealing generic damage.

#### Common design goals

- readable from friction
- not dependent on prior research
- dangerous but not opaque
- tactically meaningful without having too many parallel systems

---

### Champions

Champions are not just stronger commons. Their defining trait is **coordination**.

A champion is a creature whose threat is partly personal and partly distributed through its ability to organize the battlefield or a small enemy group.

Champions may:

- enable group maneuvers
- create positioning traps
- punish players who focus only on the leader
- become easier or harder depending on how their group is dismantled

The champion's own body may still only have 1 or 2 vital points, but the encounter also includes a tactical layer:

- pack movement
- shield wall
- crossfire
- hunting pattern
- ritual synchronization
- morale pulse

This tactical layer may enter the ATB as a secondary track or as repeated triggered effects tied to the champion's continued control.

#### Champion design goals

- feel like a leader, not just a stat increase
- make allied units matter through tactics, not through quantity alone
- present distributed priority decisions
- reward players who identify what sustains the enemy formation

---

### Elite / Boss Encounters

Elite encounters must feel like a whole situation. The players are not merely attacking a large enemy; they are engaging with a dangerous system that occupies space, time, attention, and multiple functions at once.

An elite or boss may include:

- multiple vital points
- multiple offensive subsystems
- environmental pressure
- layered telegraphs
- destructive responses
- phase changes
- windows created by correct interaction

The encounter must not be sustained by HP inflation alone.

Its durability should come from:

- multiple active functions
- several simultaneous priorities
- the need to disable, delay, or survive systems before collapse is possible
- the fact that damaging the correct part changes the rhythm of the encounter

#### Elite design goals

- feel like a multifront conflict
- create meaningful timing pressure
- remain dangerous even while players are reading and interacting with it
- avoid becoming "one creature with many hit points and one turn"

---

## The Three Structural Questions for Every Encounter

Whenever an enemy or encounter is designed, these three questions must be answered:

### 1. What is the encounter's central pressure?

What makes this threat dangerous even before the players fully understand it?

Examples:

- raw force
- speed
- elemental projection
- control of space
- coordinated pack aggression
- environmental instability

### 2. What functions sustain that pressure?

What systems, abilities, or structures make the threat work?

Examples:

- throat feeding the breath
- legs feeding mobility
- command posture feeding allied tactics
- ritual node feeding phase transition
- ice formation feeding area denial

### 3. How can players alter those functions?

What can be read, damaged, disabled, delayed, or exploited?

Examples:

- throat hit delays the breath cycle
- leg damage slows repositioning
- breaking the horn ends command range
- destroying a pillar collapses a phase mechanic
- interrupting a buildup weakens the effect rather than canceling it

If these questions do not produce clear answers, the encounter is likely too abstract or too dependent on pure numbers.

---

## Subsystems vs Adds

This design prefers **subsystems** over filler enemies.

A subsystem is not an "extra monster." It is a meaningful part of the encounter with its own logic and timing.

Examples:

- a charged breath cycle
- a tactical coordination pulse
- a collapsing ice shelf
- a moving tail that denies zones
- a ritual focus that advances every few ticks

Subsystems are preferable to filler enemies because they:

- reinforce the encounter's identity
- create pressure without inflating the battlefield with bodies
- preserve the feeling that the fight is one coherent thing
- let players dismantle the encounter intelligently

Filler enemies should only exist when they are part of the identity of the encounter, not as compensation for weak action economy.

---

## Interaction with Enemy Readability

Encounter architecture must remain compatible with the adopted readability principles for common enemies:

- players must be able to discover meaningful truths by friction
- specializations may accelerate or deepen reading, but not replace the encounter's discovery phase
- the tactical significance of a vital point must be felt in actual behavior change
- signals must not rely entirely on the Narrator using abilities in one specific order

(see `docs/adr/combat-enemy-readability.md`)

This means that if a subsystem matters, the players must be able to perceive its existence in some way:

- through telegraph
- through impact feedback
- through behavior
- through environmental signs
- through specialist interpretation
- or through repeated interaction

---

## Interaction with Fatigue and Pressure

Encounter architecture is also linked to Desgaste, Aguante, and Fatigue.

The more active layers an encounter contains, the more likely it is to:

- demand multiple high-exigency actions
- punish poor prioritization
- create simultaneous pressures that accumulate Desgaste
- force players to decide what they can ignore and what they cannot

This means enemy category should not merely increase difficulty numerically. It should increase how many **meaningful pressures** the group must survive, read, and dismantle before the encounter stabilizes.

- Common enemies should pressure one or two fronts.
- Champions should pressure the group through leadership and distributed threat.
- Elites should pressure the group on several fronts at once and demand sustained prioritization.

---

## Checklist for Creating a Creature or Encounter

### Step 1 — Define the central threat

- What makes this encounter dangerous at first contact?
- What is its core offensive or defensive pressure?

### Step 2 — Define the vital points or nodes

- Which parts or systems actually matter?
- Which of them are anatomical, tactical, or environmental?

### Step 3 — Link each point to a function

- What ability, behavior, or pressure does each point sustain?
- What changes if the point is damaged or disabled?

### Step 4 — Decide how each point interacts with ATB

- Does it create a secondary track?
- Does it modify the main track?
- Does it control a phase or environmental effect?

### Step 5 — Define readability

- How can players realize this point matters?
- What friction signals or telegraphs reveal it?

### Step 6 — Define the player payoff

- What does interacting correctly with this point accomplish?
- Delay? Weakening? Denial? Forced phase change? Opening?

### Step 7 — Check category limits

- Is this too many active layers for a common?
- Is the champion's tactical layer clear enough?
- Is the elite becoming overloaded to run?

---

## Recommended Ranges by Category

These are guidelines, not hard limits, but exceeding them should be done carefully and only when the encounter's identity truly demands it.

| Category | Vital points / systems | Key functions / pressures | Secondary tracks | Notes |
| --- | --- | --- | --- | --- |
| Common | 1–2 | 1–2 | 0–1 | — |
| Champion | 1–2 personal + 1 tactical | — | 1–2 total incl. tactical | 1–3 subordinates |
| Elite / Boss | 3–5 | 2–4 | 2–3 | Environmental layer strongly recommended |

---

## Official Decisions Adopted

1. Encounters are designed as active combat organisms, not just stat blocks.
2. A vital point is any part or system whose alteration changes the encounter's pressure in a perceptible way.
3. Not every vital point becomes its own ATB track; it may instead modify the main track or alter environment/phase.
4. Common enemies usually require 1–2 vital points and at most 1 secondary system.
5. Champions differ primarily through coordination and tactical structure, not only through personal complexity.
6. Elite/Boss encounters should create multifront pressure through layered systems, not only HP inflation.
7. Subsystems are preferred over filler enemies when the goal is to preserve encounter identity.
8. Encounter architecture must remain compatible with readability principles and fatigue-pressure principles already adopted elsewhere in the system.
9. Ciclos autónomos are a recognized form of active layer available to all creature categories. Commons are limited to biological cycles; Champions may add coordination cycles; Elites may add environmental cycles. Full design authority: `docs/system/creature-cycles.md`.

---

## Open Questions

1. When exactly should a subsystem become a full ATB track rather than a modifier on the main body?
2. How many triggered responses can an elite have before the encounter becomes too dense to run smoothly?
3. What is the best way to represent champion-level team tactics in the track without turning subordinates into unnecessary bookkeeping?
4. How should environmental subsystems be represented in UI or GM notes so they remain readable at the table?
5. Should certain categories always reserve one vital point or subsystem for defense, not only offense?

# Champion Encounter Design: Readability, Group Structure, and Distributed Pressure

**Status:** Draft — structural framework, no numerical calibration yet
**Scope:** Champion-category enemy combat design
**Related systems:** Combat, Enemy Reading, Specializations, Attrition, Fatigue, Group Tactics
**Related files:**
- `docs/adr/combat-enemy-readability.md`
- `playtests/combat/champion-encounter-v1.md`
- `playtests/combat/champion-encounter-v2.md`
- `playtests/combat/champion-encounter-v3.md`

---

## Purpose

This document defines the structural design framework for Champion-category encounters. It extends the principles established in `combat-enemy-readability.md` for common enemies and identifies what fundamentally changes when the combat unit is not a single creature but a coordinated group led by a Champion.

This document is not yet tied to a specific case study. It establishes the design architecture that will govern Champion encounter creation, playtest design, and post-playtest evaluation.

---

## Creature Category System

The Transcendence creature system defines three categories by scale of threat and intended encounter context:

**Common** — Manageable by a group even without preparation. Stronger than an individual player, but readable from inside the encounter. Intended to be understood through friction.

**Champion** — A leader coordinating a small group. The combined threat exceeds what a Common enemy presents. Its danger comes not only from the Champion's own capabilities but from the coordination structure: formation behavior, team maneuvers, shared traits, and distributed pressure. Requires the group to read both the Champion and the tactical architecture around them.

**Elite** — An apex threat requiring preparation. Not part of this document.

---

## What a Champion Encounter Is

A Champion encounter is not simply an encounter with a powerful enemy plus some weak enemies. The defining feature is **structural coherence**: the group operates as a system, not a collection of individuals.

This means:

- The Champion's actions create conditions that other units exploit
- Support units perform functions that would not make sense without the Champion's direction
- The group's collective capability exceeds the sum of its individual members
- Disrupting the structure changes what the group can do, not just how much HP remains

The reading task is therefore different. In a common encounter, the player reads the enemy's body — vital points, ability sources, behavioral patterns. In a Champion encounter, the player reads the **group's architecture** — who enables whom, what the formation allows, what triggers coordinated behavior.

---

## New Reading Units

Where a common enemy has vital points (anatomical targets that modify the enemy's capabilities), a Champion encounter introduces structural reading units:

**The Champion** — The tactical center. Coordinates group behavior, enables team maneuvers, may grant a shared trait (leadership aura, morale effect, fear projection). Disabling the Champion degrades or collapses the group's coordination structure.

**The Formation** — The spatial arrangement that grants the group a collective advantage (flanking coverage, suppression overlap, interlocking threat zones). The formation is readable through positioning behavior. It is disrupted by spatial pressure, not just damage.

**Support Units** — Members with specific structural roles: harasser, blocker, healer, relay. Each role is readable through behavioral function rather than anatomy. A blocker is identified by what it prevents, not by what it attacks.

**Shared Trait** — A trait the Champion grants to nearby allies, making the whole group more dangerous while proximity to the Champion is maintained. This is readable: if removing a unit from the Champion's proximity degrades that unit's performance, the trait source is evident.

**Team Maneuver Trigger** — A condition that activates a coordinated group action — typically the Champion setting up a specific state that other units then exploit. Maneuver triggers are the highest-value reading target in a Champion encounter: understanding them gives the group the ability to prevent coordinated attacks rather than only respond to them.

---

## The Reading Task in Champion Encounters

In a common encounter, the central question is: *what is the enemy's real logic, and where does it live in their body?*

In a Champion encounter, the central questions are:

1. *Which member of this group is directing behavior?*
2. *What does the formation allow that individual members could not do alone?*
3. *What triggers the group's coordinated attacks, and who initiates them?*
4. *Which roles are load-bearing — if removed, what collapses?*
5. *What is the Champion providing that the others depend on?*

These questions are readable through observation, friction, and specialization — the same discovery mechanisms as in common encounters, but applied to organizational structure rather than anatomy.

---

## Adapted Reading Depth Model (L1 / L2 / L3)

The L1/L2/L3 model from common enemy design applies to Champion encounters with a structural reframe.

### L1 — Structural Direction
The specialization identifies that a coordination structure exists and suggests which member is likely the tactical center.

Example: *"The larger figure is positioning the others — it is directing the group."*

No observational prerequisites. The reward is limited: direction without mechanism.

### L2 — Functional Role Identification
The specialization identifies a specific role (the blocker's function, the support unit's dependency on the Champion) from observed behavior.

Example: *"The flanker's aggression dropped after the Champion was staggered — their offense depends on the Champion's engagement."*

Requires having observed the relevant unit's behavior and at least one Champion action. Provides actionable hypothesis: the Champion is the amplifier.

### L3 — Full Structural Confirmation
The specialization confirms the coordination chain, the team maneuver trigger, and the expected consequence of disrupting the structure.

Example: *"The flanker charges only when the Champion uses the suppression ability — intercepting or staggering the Champion before that point prevents the maneuver entirely."*

Requires that the team maneuver has been observed at least once and the Champion's role in it has been established in play. Granting L3 before the maneuver has been demonstrated converts the encounter from a coordination encounter to a pre-solved execution.

---

## What Carries Over from Common Enemy Design

The following principles from `combat-enemy-readability.md` apply without modification to Champion encounters:

**Friction-based discovery remains valid.** A group without tactical specialization must be able to identify the Champion as the structural center through observation and impact feedback alone. Specialization accelerates and deepens — it does not gate the discovery path.

**Specializations accelerate or deepen reading; they do not replace it.** The same trivialization boundary applies: a specialization may confirm the role of an observed unit, but not the coordination function of a unit or maneuver that has not yet been demonstrated.

**Narrator deployment independence.** Each unit's readable signals must function independently of whether the Narrator has deployed any specific maneuver or ability. The blocker should be identifiable as a blocker without having seen the flanker attack. The Champion should be identifiable as the director without having seen the team maneuver trigger. No friction path can depend on a specific Narrator decision.

**Communicative vs. personal information.** The same information-sharing boundary applies. What the Tactical character understood about the formation may be shared freely. The mechanical advantage they gain from that understanding — reduced difficulty to exploit the formation, certainty about maneuver timing — belongs to them.

**Group knowledge persists after individual character loss.** Once a player communicates discovered information to the group — "the big one is the coordinator," "the howl is the trigger" — that information belongs to the group's collective state. If that character is incapacitated or lost, the remaining characters still know what was shared. What is lost with the character is their personal mechanical bonus, not the underlying information. This applies directly to Champion encounters: if the character who identified the maneuver trigger is removed from the fight, the group still knows the trigger.

**Transversal effects are world-state changes that persist independently of any character.** If the Champion's coordination structure is disrupted — a shared trait disabled, the Alpha's throat damaged, a territorial enemy driven from its territory — that change is a fact about the encounter's reality, not about any character's knowledge. It persists regardless of what happens to the characters who caused it. A disabled trait stays disabled even if the character who disabled it is subsequently incapacitated. The encounter's state changed; no individual character is holding that change in their awareness.

**Negative signals are as important as positive signals.** If attacking a flanker produces damage but no structural change, that feedback must be clear. The group should be able to identify "hitting this unit has no tactical consequence" as efficiently as they identify "hitting the Champion changes the group's behavior."

**Visible phase structure is required.** A Champion encounter should not resolve as linear HP depletion across the group. There must be a transition from "group functioning coherently" to "coordination degrading" to "surviving members operating without structure."

---

## What Changes Fundamentally

### The attrition source is distributed

In a common encounter, attrition pressure comes from one enemy's sustained offensive. In a Champion encounter, pressure is distributed across multiple attackers — each individually manageable, but collectively creating attrition that may outpace what individual threat-neutralization can address.

This means:

- Fatigue accumulation may be faster even if no single hit is critical
- The group cannot simply focus-fire one target without accepting pressure from others
- Reducing total incoming pressure may require disrupting coordination before eliminating targets

**Design implication:** Attrition modeling for Champion encounters must account for distributed action economy, not just the Champion's solo output. The baseline attrition floor is higher because the number of threat sources is higher.

### The reading unit is organizational, not anatomical

Vital point targeting (hit the throat to weaken the breath) has no direct equivalent in a Champion encounter. There is no single "vital point" on a group. Instead:

- The Champion is the structural center — disabling them degrades coordination
- Formation disruption is spatial — achieved by breaking proximity, isolating units, or controlling movement
- Support unit elimination removes a functional role, not just HP

**Design implication:** The discovery path cannot rely on anatomical telegraph reading (visible contraction before bite). It must rely on behavioral reading — patterns in who moves first, what conditions precede a coordinated attack, how units reposition after the Champion acts.

### The friction path is slower

Anatomical friction (body hits produce no behavioral change; throat hit changes everything) is immediate and unambiguous. Organizational friction takes longer — the player must observe multiple exchanges to establish that unit behavior is contingent on the Champion's state. This is expected and by design. But it means:

- Fatigue 1 for Champion encounters should arrive later relative to discovery than in common encounters, to allow adequate observation time
- OR the design must provide clearer behavioral telegraphs to compress the observation phase

**Design implication:** Champion encounters need explicit behavioral contracts — specific observable actions that consistently precede team maneuvers — so that the observation phase produces actionable data within a reasonable timeframe.

### Coordination disruption is a new tactical layer

In a common encounter, the tactical options are: hit the vital point, apply conditions, reduce mobility, manage the environment. In a Champion encounter, there is an additional layer: **disrupt coordination**.

Coordination disruption includes:
- Staggering or suppressing the Champion to prevent maneuver triggers
- Isolating a unit from the formation to remove shared trait benefit
- Intercepting a support unit's function (blocking the healer's action, not just attacking the healer)
- Breaking line of sight or proximity between the Champion and dependent units

This layer is not available in common encounters and should not be treated as just another attack option. It is the structural equivalent of targeting a vital point in a common encounter: the action that changes the encounter's logic, not merely its pace.

### Narrator management complexity is higher

A Narrator running a common enemy makes sequential decisions about one entity. A Narrator running a Champion encounter must manage:

- Initiative and action economy across multiple distinct units
- Formation positioning as a continuous tactical state
- Coordination triggers that require units to set up conditions before others exploit them
- Partial structural degradation — what the group can still do after the Champion is damaged or a unit is removed

**Design implication:** Champion encounter design must support Narrator legibility. The group's behavioral rules — when the team maneuver triggers, how the formation repositions, what individual units do when the Champion is suppressed — must be explicit enough that a Narrator can execute them consistently under pressure.

---

## Fatigue Timing in Champion Encounters

The structural rule from common encounter design holds: Fatigue 1 should arrive after useful discovery, not before it and not only after the encounter is already solved.

But the timing relationship differs in two ways:

**Discovery is slower.** The observation phase for group structure takes more exchanges than vital point discovery in a common encounter. Fatigue calibration must account for this extended discovery window.

**Attrition baseline is higher.** Multiple attackers mean the group is absorbing more pressure per exchange, all else equal. A Fatigue threshold calibrated as if the group faced a single attacker will arrive too early relative to discovery.

**Adopted principle:**
For Champion encounters, Fatigue 1 should arrive no earlier than the point at which the team maneuver has been demonstrated at least once and the Champion's coordinating role is observable. The intended window is: after the maneuver is understood but before the coordination has been fully disrupted.

Informed groups should earn a delay in Fatigue by identifying the coordination structure early. But even an optimally informed group must face minimum attrition from the distributed action economy — that floor cannot be reasoned away by good reading.

---

## Narrator Challenges Specific to Champion Encounters

**Maintaining formation coherence.** The Narrator must run the group as a coordinating system, not as independent units taking individual turns. This requires explicit formation rules and defined triggers for repositioning behavior.

**Telegraphing coordination without a fixed script.** The group must telegraph maneuvers in a way that is readable without the Narrator following a predetermined ability sequence. This mirrors the Narrator independence requirement from common enemy design, but is harder to satisfy: coordination requires multiple units acting in sequence, and that sequence can feel scripted.

**Resolution:** Each unit should have an observable pre-maneuver behavior that functions as an independent telegraph. The flanker does not charge without first repositioning — that repositioning is readable regardless of whether the Champion has been seen to trigger it before. The Champion does not initiate suppression without a visible wind-up — that wind-up is readable independently.

**Managing structural degradation without collapse.** After the Champion takes significant damage or a support unit is removed, the Narrator must know what the group can still do. Partial degradation must feel meaningfully different from the intact state without the encounter collapsing into trivial cleanup.

**Resolution:** Champion encounter design must define at least two structural states: intact coordination and degraded coordination. Each state should specify which maneuvers are available, how positioning changes, and what the group's attrition output becomes.

**Adopted rule — Champion death:**
When the Champion is killed (not just silenced), surviving units enter immediate total coordination collapse. All coordination bonuses drop, all maneuver triggers become unavailable, and each surviving unit reverts to independent predator or combatant behavior — targeting the nearest threat without structural logic. There is no intermediate "degraded-but-coherent" state after death; that intermediate state only exists when the Champion is suppressed or silenced while still alive. Death eliminates the signal source entirely. This collapse must be narratively immediate and legible — the behavioral shift should be visible in the same exchange as the Champion's elimination.

---

## Design Checklist for Champion Encounters

Use the following when creating any Champion encounter:

- **Champion role:** Define what the Champion provides that other units depend on. Name the shared trait, the maneuver trigger, and the consequence of suppressing the Champion. These must be derivable from observation — not just stated in the stat block.

- **Unit roles:** Assign each unit a readable functional role (blocker, harasser, support, relay). Each role must be identifiable from behavior alone, before the unit has been targeted. Define what the unit stops doing if isolated from the formation.

- **Formation definition:** Specify the spatial arrangement and what advantage it grants. Define the conditions that collapse the formation — spatial, not just HP-based.

- **Team maneuver design:** Name the trigger condition, the setup unit, and the exploiting unit. Ensure the trigger is observable before the maneuver fires. The maneuver should be preventable by disrupting the trigger, not only by dealing damage.

- **Reading depth model:** Apply L1/L2/L3. L1 identifies the Champion as director. L2 identifies a specific unit's dependency after observing their contingent behavior. L3 confirms the full maneuver chain — only after the maneuver has been observed at least once.

- **Signal independence:** Each unit's behavioral signals must be readable without requiring the Narrator to have deployed any specific prior ability. The Champion's coordinating role should be observable from their positioning and timing, not only from having seen a team maneuver fire.

- **Friction path:** Design at least one valid discovery route requiring no specialization. Identify the behavioral signal that reveals the Champion as the structural center. Identify the negative signal — what happens when the group targets a non-load-bearing unit without disrupting coordination.

- **Structural degradation states:** Define intact and degraded coordination states. Specify which maneuvers are available in each. Degraded state must be meaningfully weaker without being trivial.

- **Fatigue alignment:** Set Fatigue 1 to arrive after the team maneuver has been observed and the coordination structure is actionable — not before. Verify the encounter is not too fast for the extended observation phase required by organizational reading.

- **Narrator legibility:** Confirm the group's rules are explicit enough to run under pressure. Unit behavior on the Champion's death or suppression must be defined in advance, not improvised.

---

## Open Design Questions

**High priority:**

1. What is the Fatigue 1 threshold for Champion encounters, expressed relative to the common encounter baseline? The structural delay argument is established; the specific number is pending — will be derived from champion-encounter-v3 once base statistics are defined.
2. Can formation disruption (spatial) trigger structural degradation independently of Champion HP? Or does the Champion's health track govern the group's coordination state?
3. What is the minimum group size for a Champion encounter to function? Can a Champion + 1 support unit create a readable coordination structure, or does the model require at least 3 units?

**Medium priority:**

1. Does the L1/L2/L3 reading model need a fourth level (L4 — strategic anticipation) for Champion encounters, where the player can predict a maneuver before it has been triggered? Or does L3 cover this when all observational prerequisites are met?
2. How does explicit coordination (one player setting up an opening for another) interact with Champion encounters specifically? This is the design space flagged in `combat-enemy-readability.md` — Champion encounters may be the correct place to develop it.
3. ~~What happens to the reading model when the Champion is eliminated early?~~ *Resolved:* Champion death = immediate total coordination collapse. Surviving units revert to independent Common-enemy behavior. No intermediate structure. The encounter becomes a Common-style cleanup from that point.

**Lower priority:**

1. Can a group without a named Champion exhibit Champion-level coordination — emergent leadership — and if so, how does the reading task change?
2. Should Champion encounters always involve numerical asymmetry (more enemies than players), or can a single Champion with no support units constitute a Champion encounter if their tactical architecture is sufficiently complex?

---

## Relationship to Common Enemy Design

Champion encounter design is downstream of, not separate from, the common enemy framework established in `combat-enemy-readability.md`. The core principles — friction validity, specialization bounds, Narrator independence, signal independence, information sharing — transfer without revision.

What Champion encounters add is a second axis of readable structure. In common encounters, the reading target is the enemy's body. In Champion encounters, the reading target is the group's coordination architecture. The discovery mechanics are the same; the object of discovery is different.

This means Champion playtest design should evaluate both axes: is the individual Champion's vital structure readable (do they have their own anatomy to read, separate from the coordination question)? And is the group's coordination structure readable (does the team maneuver become understandable before or after it has already determined the outcome)?

A fully designed Champion encounter will produce findings along both dimensions.

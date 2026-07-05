# Elite / Boss Encounter Design

**Status:** Adopted (structural design — numerical calibration open)
**Scope:** Elite and Boss-category enemy combat design
**Related systems:** Combat, ATB, Vital Points, Attrition, Fatigue, Environmental Pressure, Metamorfosis
**Related files:**
- `docs/adr/combat-encounter-architecture.md`
- `docs/adr/combat-enemy-readability.md`
- `docs/adr/combat-champion-encounter.md`
- `docs/system/creature-cycles.md`

---

## Purpose

This document defines the structural design framework for Elite and Boss-category encounters. It extends the principles established in `combat-encounter-architecture.md` and specifies what fundamentally changes when the combat unit is not a creature with vital points but a multi-layered system that transforms the battlefield as it is fought.

An Elite encounter is not a harder Common encounter or a more dangerous Champion encounter. It is a different category of pressure: one that operates in more temporal layers simultaneously, reshapes the encounter space through each phase, and demands that the group manage multiple active problems that compound rather than reduce.

---

## What an Elite Encounter Is

An Elite encounter is an encounter that exists in at least three simultaneous layers of pressure:

- **A main body** — the physical threat, with its own vital points and behavior
- **Two or more ciclos autónomos** — independent ATB entries with their own timing and effects
- **An environmental layer** — pressure that modifies the encounter space itself

These layers interact. Damaging a vital point may silence a ciclo autónomo. A Metamorfosis phase may introduce a new environmental ciclo autónomo that did not exist before. An environmental effect may make other layers harder to interact with.

An Elite is defeated when enough of its systems have been dismantled that its remaining pressure can no longer sustain the encounter — not necessarily when its main body reaches zero.

---

## How Elite Encounters Differ from Commons and Champions

| Dimension | Common | Champion | Elite / Boss |
| --- | --- | --- | --- |
| Reading unit | Anatomy | Group architecture | Phase structure + system state |
| Pressure source | Main body | Distributed via coordination | Multi-layer: body + ciclos + environment |
| Phase logic | None | Partial (coordination degrades) | Explicit Metamorfosis with qualitative shifts |
| Ciclos autónomos | Biological only | Biological + coordination | Biological + environmental |
| Environmental layer | Incidental | Possible | Required |
| Discovery pace | Fast (within encounter) | Medium (requires observation) | Slow (unfolds across phases) |
| Narrator system load | Low | Medium | High |

---

## Metamorfosis — Phase Structure

Metamorfosis is the Elite's phase-change mechanism. It is not triggered by HP thresholds. It is triggered by **vital point destruction**.

When enough vital points are destroyed — or a specific designated vital point is destroyed — the Elite enters the next Metamorfosis phase.

### What a Metamorfosis must include

Every Metamorfosis must change three things simultaneously:

**1. Body transformation**
The Elite's physical form changes visibly and irrevocably. This is not cosmetic. The transformation should communicate that a threshold was crossed — the creature is not the same thing it was before.

Examples:
- limbs destroyed and replaced by new structures
- anatomy expanding beyond biological norms
- sensory organs replaced or destroyed; new perception modes emerge
- previously hidden anatomy becomes exposed or active

**2. Environmental transformation**
The encounter space changes in a way that persists through the rest of the encounter. Environmental transformations do not reset when the phase ends. They accumulate.

Examples:
- visibility decreasing permanently
- terrain becoming unstable, elevated, or fragmented
- atmospheric effects that generate attrition (heat, cold, corrosive particles, psychic noise)
- light conditions that alter what can be perceived or targeted

**3. New capability**
The Elite gains at least one new technique or ciclo autónomo that did not exist before this phase. This capability should reflect the transformation — it should not feel like a stat increase but like the creature becoming a different kind of threat.

### Phase count

Most Elite encounters should have 2 to 3 Metamorfosis phases, not counting the initial state. More phases are possible but they increase Narrator management load significantly.

A three-phase Elite has:
- **Opening state** — the creature as it enters the encounter
- **First Metamorfosis** — triggered by a destroyed vital point or vital system
- **Second Metamorfosis** — triggered by further destruction; the encounter is now fundamentally different from its opening
- **Apoteosis** (optional final state) — triggered by a last vital point; the creature in its most dangerous form, usually with a narrow resolution window

### Phase transitions are not rest windows

When Metamorfosis triggers, the encounter does not pause. The transformation happens during combat time. The visual and environmental changes are narratively significant but mechanically they are a shift that the group must respond to, not a cinematic break. ATB continues.

---

## Vital Points and Phase Triggers

In a Common enemy, vital points reduce or disable specific abilities when destroyed.

In an Elite, vital points serve that function **and** may serve as phase triggers.

### Types of vital point in Elite encounters

**Ability-linked vital points**
Destroying these disables a specific technique or ciclo autónomo. The link should be legible: the vital point is visibly connected to the function it supports.

**Phase trigger vital points**
Destroying these triggers a Metamorfosis. These are usually the most visible, most defended, or most difficult to reach vital points in a given phase. Players who have read the encounter well should be able to anticipate what will happen when the phase trigger is destroyed — even if the exact transformation was not predictable.

**Structural vital points**
Destroying these changes the encounter's spatial logic without triggering a full Metamorfosis — a wing collapses and aerial movement becomes unavailable; a limb is severed and the attack pattern changes; a sensory organ is destroyed and the creature can no longer track targets in a specific way.

### Vital point linkage rule

Every vital point in an Elite encounter must be linked to a **function**. Destroying it must change something observable about how the encounter behaves — not merely reduce a stat or a health pool.

A vital point that only reduces damage output is underperforming in this system.

---

## Ciclos Autónomos in Elite Encounters

Elite encounters may have two types of ciclos autónomos: biological and environmental.

### Biological ciclos autónomos

Same as for Commons and Champions: anchored to a specific zone. When the zone collapses, the cycle is removed from the ATB.

Examples for Elites:
- a regeneration cycle driven by a specific gland or organ
- a toxin dispersal cycle driven by a venom sac
- a charge cycle driven by an elemental pressure organ

### Environmental ciclos autónomos

These are the distinguishing ciclo type for Elite encounters.

An environmental ciclo autónomo is **not anchored to a specific zone**. It is a property of the Elite's presence in the encounter space. It cannot be ended by destroying a body part — only by defeating the Elite itself or by triggering a Metamorfosis that explicitly resolves it.

Environmental ciclos autónomos persist through Metamorfosis phases unless the phase design states otherwise. They represent the encounter space reacting to the Elite's existence.

Examples:
- a bleeding sky cycle that drops attrition on all participants each time it fires
- a shadow displacement cycle that repositions environmental hazards
- a terrain collapse cycle that makes certain zones impassable
- a psychic resonance cycle that degrades a specialization's effectiveness

### When to add a new ciclo autónomo during Metamorfosis

Each Metamorfosis may introduce a new ciclo autónomo as its "new capability." This is the recommended pattern because it increases layered pressure mechanically and narratively — the encounter becomes harder not just because the Elite is more dangerous but because more independent systems are active at once.

### Ciclo visibility and timing

All ciclos autónomos — including environmental ones — must be visible on the ATB as distinct entries. Players know they exist. Their next rhythm cost is hidden by default.

As more ciclos autónomos become active through successive Metamorfosis phases, reading any individual ciclo's timing becomes progressively harder. This is by design: the cognitive load on the group should increase as the encounter deepens.

---

## Environmental Layer Requirements

Elite encounters require at least one environmental layer. Environmental layers are not optional for Elites.

An environmental layer is any ongoing encounter-space condition that:

- creates pressure independently of any single attack or turn
- persists across the whole encounter (or across one or more phases)
- requires the group to make decisions about how to navigate or respond to it

Environmental layers are distinct from environmental ciclos autónomos, but they may overlap. A ciclo autónomo may maintain and intensify an environmental layer over time.

### What the environmental layer must do

It must change the tactical problem. If the environment in the second phase is merely "the same fight but darker," it is not functioning. The environment should make something harder, change how certain abilities work, close off certain approaches, or open new ones.

Examples:
- reduced visibility that makes long-range targeting unreliable
- terrain fragmentation that imposes movement decisions
- attrition-generating zones that punish staying still
- a structural feature players can interact with to alter the encounter (destroy the altar, redirect the elemental column)

### Environmental layers are permanent within a phase

A Metamorfosis does not undo previous environmental transformations. Phases accumulate. A group fighting the third phase of an Elite is operating in an environment that has been changed by both previous Metamorfosis events, plus whatever environmental layer the current phase introduced.

This accumulation is intentional. The encounter should feel qualitatively different from its opening state — not just harder.

---

## Reading in Elite Encounters

Elite encounters cannot be fully understood in one encounter. They unfold.

The L1/L2/L3 reading model from `combat-enemy-readability.md` applies, but with important differences:

- **Not all systems are readable at the start.** A ciclo autónomo that only enters the ATB during the second Metamorfosis cannot be read until after the first phase triggers. Some systems are literally not present until the encounter has progressed.
- **Phase triggers may not be deducible before the first Metamorfosis fires.** Players can be informed that vital points matter, but the exact threshold for phase transition is legitimate hidden information.
- **Environmental transformations are transversal facts.** Once an environmental layer is active, all players navigate the same reality. There is no "reading" required to understand it — its effects are felt directly.

### Reading as encounter pressure

In an Elite encounter, the reading task itself is part of the pressure. The group must maintain situational awareness of:
- which vital points are still active and what they support
- how many ciclos autónomos are running and at what approximate tempo
- which phase the Elite is in and what new systems that phase introduced
- how the environmental layer is affecting their options

A group that loses track of this information will be unable to prioritize correctly and will experience compounding pressure without a clear path to reducing it.

---

## Narrator Challenges Specific to Elite Encounters

**Managing multiple simultaneous layers under time pressure**
The Narrator must track the main body's activation, 2–3 independent ciclos autónomos with different rhythm costs, the current phase state, vital point status, and environmental layer effects. This is the highest bookkeeping load in the system.

**Resolution:** Elite encounter design must provide explicit checklists for the Narrator — per-phase summaries of what is currently active, what changes at each Metamorfosis, and what each vital point does when destroyed.

**Making Metamorfosis feel earned, not scripted**
A Metamorfosis triggered by player action should feel like a direct consequence of the players' choices, not like a predetermined animation. The Narrator must connect the transformation to what the group did: "you destroyed the pressure nodules in the wings — the creature no longer flies, and something else takes its place."

**Resolution:** The transformation should always be narrated in response to the players' action, not as a separate announcement. The phase trigger was the vital point; the players caused it.

**Maintaining environmental layer continuity**
Environmental changes persist and accumulate. The Narrator must remember the current state of the encounter space as it evolves across phases. A second-phase environmental effect should be described as existing on top of the first-phase effects, not as a replacement.

**Resolution:** Design the environmental accumulation explicitly — write a brief description of what the encounter space looks and feels like in each phase, incorporating all previous changes.

**Preventing attrition collapse before the encounter resolves**
Elite encounters generate more cumulative Desgaste and Fatigue than lower categories. If Fatigue arrives before the group has the information needed to prioritize, the encounter becomes a race against physiological collapse rather than a tactical reading encounter.

**Resolution:** Fatigue calibration for Elite encounters must account for the extended time required to read the encounter, understand the phase structure, and identify which systems to target first. Fatigue 1 should not arrive before the group has seen at least one Metamorfosis.

---

## Design Checklist for Elite Encounters

### Vital points
- [ ] How many vital points exist?
- [ ] Which are ability-linked, which are phase triggers, which are structural?
- [ ] What does each vital point do when destroyed? Does it disable a ciclo, trigger a Metamorfosis, or change the encounter's structure?
- [ ] Is every vital point linked to a visible function — can players identify the relationship through observation?

### Ciclos autónomos
- [ ] Which ciclos autónomos are active in the opening state?
- [ ] Which ciclos autónomos are introduced per Metamorfosis?
- [ ] Which are biological (zone-anchored), which are environmental (persistent)?
- [ ] Are all ciclos autónomos represented as distinct ATB entries visible to players?

### Metamorfosis phases
- [ ] How many phases exist?
- [ ] What triggers each phase (vital point, vital point count, or specific structural vital point)?
- [ ] What are the three required changes per phase: body transformation, environmental transformation, new capability?
- [ ] Is the environmental change permanent and cumulative?
- [ ] Is the new capability per phase a new ciclo autónomo, a new technique, or a structural change?

### Environmental layer
- [ ] What is the baseline environmental layer (first phase)?
- [ ] How does the encounter space look and feel in each subsequent phase (cumulative)?
- [ ] Does the environmental layer change tactical options, not just add difficulty?
- [ ] Is there anything players can do to interact with the environment — not necessarily to remove it, but to alter its effect?

### Reading and discovery
- [ ] Which systems are readable from the opening state? Which only become visible after a Metamorfosis?
- [ ] Is there a valid friction path for identifying each vital point's function without specialization?
- [ ] Is the phase trigger vital point distinguishable from ability-linked vital points through observation?

### Narrator legibility
- [ ] Is there a per-phase summary of what is currently active?
- [ ] Is Metamorfosis narration connected directly to the players' action that triggered it?
- [ ] Is Fatigue 1 calibrated to arrive no earlier than after the first Metamorfosis?

---

## Official Decisions Adopted

1. Elite encounters must operate in at least three simultaneous layers: main body, two or more ciclos autónomos, and an environmental layer.
2. Metamorfosis is triggered by vital point destruction, not by HP thresholds.
3. Every Metamorfosis must change three things simultaneously: body transformation, environmental transformation, and new capability.
4. Environmental transformations are permanent within the encounter. Phases accumulate — they do not reset.
5. Elite encounters may have environmental ciclos autónomos that persist through Metamorfosis phases and are not anchored to a specific zone. They end only when the Elite is defeated.
6. Every vital point in an Elite must be linked to a function. Destroying it must change something observable about the encounter's behavior.
7. Reading in Elite encounters is extended — some systems are not present until a Metamorfosis has fired. This is by design.
8. Fatigue calibration for Elite encounters must account for the extended reading phase. Fatigue 1 should not arrive before the group has seen at least one Metamorfosis.
9. An Elite is defeated when enough of its systems have been dismantled that remaining pressure can no longer sustain the encounter — not necessarily when the main body reaches zero.

---

## Open Questions

1. Can an Elite have a vital point that, when destroyed, permanently ends an environmental ciclo autónomo — breaking the rule that environmental cycles only end on defeat? If so, under what design conditions?
2. What is the correct maximum number of simultaneously active ciclos autónomos for an Elite encounter before table management becomes unrunnable?
3. How should Metamorfosis interact with the Limbo manifestation system when the Elite has a vínculo or is itself a manifestation? (Blocked on D-09, D-11 — see `docs/pending.md`)
4. Should Elites have a formal "last window" mechanic — a final phase state in which the encounter can only be resolved through a specific action, not through continued attrition?

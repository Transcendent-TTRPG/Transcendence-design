# ADR — ATB Base Rhythm Costs

**Status:** Updated (v0.2 — aligned to corebook 2026-06)
**Scope:** Base rhythm costs and Desgaste costs for universal combat actions
**Related:** `combat-atb-timeline.md`, `data/system/atb-combat.yaml`, `docs/system/atb-reference.md`

---

## Purpose

This document defines the base rhythm costs and Desgaste costs for the most universal action families in combat.

Its goal is not to assign final rhythm values to every technique or derived ability. It establishes the stable baseline that any creature can use in combat — and defines why that baseline is intentionally inefficient relative to trained technique use.

This is consistent with the adopted ATB model:

- combat flows through a continuous timeline
- every meaningful action has a rhythm cost
- rhythm cost and Desgaste are related but not identical
- competency and training unlock techniques that improve on base action efficiency

---

## Base Actions as the Inefficient Floor

Base actions are the combat options available to **any creature** — trained or not. They are not the expected behavior of a player character with active competencies.

For a trained character, techniques are the primary mode of executing combat activations. Techniques are faster, more efficient, cheaper in Desgaste, or produce direct mechanical effects that base actions cannot. A character who consistently falls back to base actions instead of using their trained techniques is playing below their capability.

**The design rule:** techniques are not balanced against base actions. A technique that costs Ritmo 4 instead of Ritmo 6 is not discounted — it is the efficient output of training, replacing a blunt generic action with a precise one. Base actions are the floor for creatures without relevant competencies, not the benchmark for technique calibration.

The Narrator should not treat base actions as the normal pace of play. They are the fallback state. Untrained creatures and characters without relevant competencies use them. Competent characters use techniques.

---

## Design Principle

Base rhythm costs are determined by the **general mode of execution** of an action — not by the exact weapon name, specialization, or tool involved.

This means:

- moving has one base rhythm
- attacking with a one-handed weapon has one base rhythm
- attacking with a two-handed weapon has one base rhythm
- interacting has one base rhythm
- using a specialization under pressure has one base rhythm

More specific techniques may override or replace these values for trained characters. The baseline should remain simple enough to support quick table use for untrained or generic situations.

---

## Why This Baseline Is Intentionally Simple

The intent is not to fragment rhythm by weapon micro-category or specialization detail.

Examples of what should NOT happen at the base layer:

- a dagger and a sai should not need separate rhythm values
- different one-handed blades share the same rhythm family
- terrain should not change the rhythm cost of movement, but rather the distance, difficulty, or consequences

Specific techniques assign their own rhythm costs. The base layer defines the common floor — not the ceiling.

---

## Rhythm Bands

Base action costs are integers. The following bands describe the general tempo of an action category. Specific actions may fall at values between bands.

| Band | Cost | Description |
| --- | ---: | --- |
| Free | 0 | No meaningful time cost within the combat timeline |
| Quick | 3 | Light, immediate action with minimal commitment |
| Standard | 5 | Movement and moderate-commitment actions |
| Heavy | 7 | Two-handed attacks — high commitment, real recovery time |
| Extreme | 9 | Reserved for specific advanced techniques |

Several base actions fall between bands (attacks at 6, dual-wield at 8). The bands are orientation labels, not strict slots. No base action uses cost 9 — the Extreme band is reserved for specific techniques.

---

## Base Actions

### Free Actions (Cost 0, Desgaste 0)

#### Soltar (Drop)

Releasing an item held in hand that is not actively engaged in a maneuver or grip.

**Constraint:** Dropping an item that is actively part of a grip, hold, or committed joint maneuver is **not** free. That requires an Interactuar action (cost 3).

#### Hablar (Speak)

A brief, non-strategic utterance during combat: a short warning, a tactical signal, a one-word command to an ally.

**Constraint:** Communication intended to deceive, persuade, negotiate, issue complex orders, or apply social pressure is **not** free.

---

### Interactuar (Cost 3 — Quick, Desgaste 0 or 1)

Short, immediate physical interactions with the environment or held objects: grabbing something within reach, opening or closing something simple, activating a small mechanism, adjusting equipment, picking up an item.

Desgaste is only generated when the interaction occurs under real scene pressure. A trivial or unrisky interaction generates 0 Desgaste.

---

### Usar Especialización (Cost 4, Desgaste 1)

Use of any specialization under pressure in a hostile scene: jumping, acrobatics, perception, tracking, crafting under pressure, social reading, and any other specialization.

Cost 4 (below the Standard band) reflects that specialization use is less physically committing than an attack — it occupies attention without requiring full body commitment or weapon recovery time.

A specialization produces a narrative or practical result. Direct mechanical consequences require a follow-up action or a Technique.

---

### Movimiento (Cost 5 — Standard, Desgaste 1)

Standard movement through the combat space.

Terrain does not change rhythm cost. It changes how far the character can move, whether movement requires a check, and the consequences of the movement.

| Condition | Effect on distance |
| --- | --- |
| Difficult terrain | Speed halved |
| Crawling | Speed halved |
| Running | Speed doubled |

---

### Ataque — Arma Natural (Cost 6, Desgaste 1)

Baseline for natural weapons: claws, bite, tail, horns, stinger, and any other body-integrated weapon. Cannot be disarmed while the creature's body remains intact.

---

### Ataque — Arma a Una Mano (Cost 6, Desgaste 1)

Baseline for all one-handed offensive weapon families: short blade, one-handed sword, one-handed axe, one-handed club.

Cost 6 places one-handed attacks above movement but below two-handed attacks. Techniques derived from one-handed weapon competencies may reduce this cost for trained characters.

---

### Ocultarse (Cost 6, Desgaste 1)

Deliberate attempt to evade tactical perception. Requires a valid opportunity: Cover (medium or total), reduced visibility range, a sufficient distraction, or a Technique or trait that permits hiding.

Resolved with an appropriate specialization roll (Sigilo, Supervivencia, or another authorized by a Technique or trait). On success, the character gains the `Oculto` state against affected enemies.

---

### Ataque — Arma a Dos Manos (Cost 7 — Heavy, Desgaste 1)

Heavy baseline for all two-handed offensive weapon families.

Cost 7 reflects greater body commitment, slower recovery, and larger tactical openings if the action is poorly timed.

---

### Ataque — Dos Armas (Cost 8, Desgaste 1)

Dual-weapon attack. The higher cost reflects coordination demand and the larger offensive commitment of managing two simultaneous strike lines.

Procedurally:

1. T.A. initial with the primary hand — no penalty
2. T.E. de combate con dos armas against the target's T.D.
3. If T.E. exceeds T.D., additional attacks may be declared, alternating hands
4. Additional attacks = 1 per 2 points of Agilidad (minimum 1)

---

## Desgaste Baseline

| Base Action | Rhythm Cost | Desgaste |
| --- | ---: | ---: |
| Soltar / Hablar | 0 | 0 |
| Interactuar | 3 | 0 or 1 * |
| Usar Especialización | 4 | 1 |
| Movimiento | 5 | 1 |
| Ataque — arma natural | 6 | 1 |
| Ataque — arma a una mano | 6 | 1 |
| Ocultarse | 6 | 1 |
| Ataque — arma a dos manos | 7 | 1 |
| Ataque — dos armas | 8 | 1 |

\* Interactuar generates 1 Desgaste only when the interaction is meaningful and performed under real scene pressure. Trivial or unrisky interactions generate 0.

### Structural rule

- Standard meaningful actions under pressure → **1 Desgaste**
- Free or trivial actions → **0 Desgaste**
- Advanced techniques may have Desgaste > 1; this is defined per technique, not per base action family

---

## Competency and Rhythm

Competency rank interacts with rhythm in two distinct ways:

1. **Technique unlock:** A competency rank unlocks techniques with their own rhythm values — usually faster or more efficient than the base action family. The base family rhythm is not changed; a better option is added alongside it.

2. **Friction reduction:** A specific technique may reduce the rhythm cost of a specific action. This is always technique-specific, not family-wide. A high weapon rank does not automatically reduce all one-handed attacks below cost 6 — it unlocks a specific technique that costs less.

This keeps the base layer stable while allowing competency to create meaningful tempo advantages through deliberate design.

---

## Summary Table

| Base Action | Rhythm Cost | Desgaste |
| --- | ---: | ---: |
| Soltar / Hablar | 0 | 0 |
| Interactuar | 3 | 0 or 1 |
| Usar Especialización | 4 | 1 |
| Movimiento | 5 | 1 |
| Ataque — arma natural | 6 | 1 |
| Ataque — arma a una mano | 6 | 1 |
| Ocultarse | 6 | 1 |
| Ataque — arma a dos manos | 7 | 1 |
| Ataque — dos armas | 8 | 1 |

---

## Official Decisions Adopted

1. Base rhythm costs are assigned by **action family**, not by exact weapon or specialization name.
2. Terrain does not change the rhythm cost of movement; it changes distance, difficulty, and consequences.
3. Natural weapon attacks use rhythm cost 6.
4. One-handed weapon attacks use rhythm cost 6.
5. Two-handed weapon attacks use rhythm cost 7.
6. Dual-wield attacks use rhythm cost 8, reflecting coordination demand and the offensive commitment of managing two simultaneous strike lines.
7. Specialization use costs Ritmo 4 — below Standard — because it requires attention but not full physical commitment or weapon recovery time.
8. Drop and Speak are free actions (cost 0) within defined constraints.
9. Interactuar generates Desgaste only under real scene pressure; trivial interactions generate 0.
10. **Base actions are the inefficient floor.** They are the fallback for creatures without relevant competencies, not the benchmark for technique calibration. Trained characters are expected to use techniques as their primary combat activations.
11. Competency rank interacts with rhythm through technique unlocks or technique-specific friction reduction — not through automatic family-wide cost reduction.

---

## Open Questions

1. Which techniques should reduce rhythm below the base action family cost, and by how much?
2. Should aimed attacks (apuntados) remain within their weapon family rhythm cost, or become a separate rhythm category with a defined base cost?
3. Should certain shields or defensive styles become their own base action family with a defined base cost?
4. At what point should movement split into controlled movement vs. forced or desperate movement with distinct costs?
5. Should high-demand specialization uses (e.g. complex treatment or crafting mid-combat) use a higher cost than 4, or should that variation live entirely in techniques?

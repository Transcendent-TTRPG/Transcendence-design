# ADR — ATB Base Rhythm Costs

**Status:** Adopted (v0.1 baseline)
**Scope:** Base rhythm costs and Attrition costs for universal combat actions
**Related:** `combat-atb-timeline.md`, `data/system/atb-combat.yaml`, `docs/system/atb-reference.md`

---

## Purpose

This document defines the base rhythm costs and Attrition costs for the most universal action families in combat.

Its goal is not to assign final rhythm values to every aptitude, discipline, or derived ability. It establishes a simple, stable baseline that later design can build on without replacing.

This is consistent with the adopted ATB model:

- combat flows through a continuous timeline
- every meaningful action has a rhythm cost
- rhythm cost and Attrition are related but not identical
- competency may later reduce execution friction, making certain actions faster, less exhausting, or both

---

## Design Principle

Base rhythm costs are determined by the **general mode of execution** of an action — not by the exact weapon name, specialization, or tool involved.

This means:

- moving has one base rhythm
- attacking with a one-handed weapon has one base rhythm
- attacking with a two-handed weapon has one base rhythm
- interacting has one base rhythm
- basic observation has one base rhythm

More specific abilities may later override or modify these values. The baseline should remain simple enough to support quick table use.

---

## Why this baseline is intentionally simple

At this stage, the intent is not to fragment rhythm by weapon micro-category or specialization detail.

Examples of what should NOT happen at the base layer:

- a dagger and a sai should not need separate rhythm values
- different one-handed blades share the same rhythm family
- terrain should not change the rhythm cost of movement, but rather the distance, difficulty, or consequences
- a universal read/understand action should exist before specialized reading abilities are added

Specific abilities, aptitudes, techniques, or advanced uses may later assign their own rhythm costs. The base layer defines the common floor.

---

## Rhythm Scale

| Band | Cost | Description |
| --- | ---: | --- |
| Free | 0 | No meaningful time cost within the combat timeline |
| Quick | 3 | Light, immediate action with minimal commitment |
| Standard | 5 | Normal committed action within standard combat pace |
| Heavy | 7 | High-commitment action with significant recovery time |
| Extreme | 9 | Maximum commitment — reserved for specialized maneuvers or major abilities |

No universal base action in this document uses cost 9. The Extreme band is reserved for specific advanced abilities.

---

## Base Actions

### Free Actions (Cost 0)

Free actions do not advance the ATB marker. They happen within the moment of activation.

#### Drop

Releasing an item held in hand that is not actively engaged in a maneuver or grip.

This covers:

- releasing a weapon held loosely while another hand acts
- letting go of an object not involved in the current action
- dropping something before or after the main action

**Constraint:** Dropping an item that is actively part of a grip, hold, or committed joint maneuver is **not** free. That requires an Interact action (cost 3). This prevents using free drop to escape engaged positions or committed weapon states.

#### Speak

A brief, non-strategic utterance during combat.

This covers:

- a short warning or tactical signal
- a one-word or short-phrase command to an ally
- an involuntary exclamation

**Constraint:** Any communication intended to deceive, persuade, negotiate, issue complex orders, or apply social pressure is **not** free. That falls under the social action layer to be defined when social combat mechanics are added. The distinction is functional: speaking as information transmission is free; speaking as influence is not.

---

### Interact (Cost 3 — Quick)

Short, immediate physical interactions with the environment or held objects.

This covers:

- grabbing something within reach
- opening or closing something simple
- activating a small mechanism or switch
- making a quick practical adjustment to equipment
- picking up an item from the ground or a nearby surface

This is the lightest non-free action family. It uses the Quick band because it requires physical commitment and presence of mind but not full offensive or movement commitment.

---

### Move (Cost 5 — Standard)

Standard movement through the combat space.

Movement does not change rhythm cost based on terrain. Terrain and context instead affect:

- how far the character can move
- whether movement requires a check
- whether the path is safe or interrupted
- consequences of the movement (positioning, exposure)

Movement matters too much tactically to be trivial or universally free. It is treated as a committed action within the ATB economy.

---

### Specialization (Cost 5 — Standard)

Use of any specialization in a hostile scene: jumping, acrobatics, perception, interpretation, tracking, social reading, crafting under pressure, and any other specialization a character can use.

The cost is uniform across all specialization types because the reason is the same: the character is under active scene pressure and the action requires real attention and effort, regardless of whether the specialization is physical, mental, or social.

This action does not itself grant special tactical bonuses beyond what the specialization's narrative result supports. Techniques may later replace or improve this with distinct rhythm values and direct mechanical effects.

---

### Attack with One-Handed Weapon (Cost 5 — Standard)

Standard baseline for all one-handed offensive weapon families.

This covers the general family without splitting at the weapon-name level:

- short blade, one-handed sword
- one-handed axe, one-handed club
- similar one-handed offensive tools

Distinct weapon identity should emerge later through impact, effects, traits, aptitudes, vital point interaction, and specialized abilities — not through rhythm splitting at the base layer.

---

### Attack with Two-Handed Weapon (Cost 7 — Heavy)

Heavy baseline for all two-handed offensive weapon families.

The increased cost is not purely about weapon size. It reflects:

- greater body commitment required for execution
- slower recovery after the action resolves
- larger tactical openings if the action is poorly timed
- heavier offensive rhythm overall

This family should feel more committed than one-handed offense even before advanced abilities modify it.

---

### Attack with Two One-Handed Weapons (Cost 7 — Heavy)

Dual-wield attack also uses the Heavy baseline.

The cost is not about weight but about coordination and offensive commitment:

- multiple strikes or a linked offensive sequence
- greater technical demand than a single one-handed attack
- stronger recovery need before the next activation

This makes dual-weapon offense distinct from standard one-handed attacks without fragmenting the base system.

---

## Attrition Baseline

The following values define the base Attrition cost for universal combat actions.

These values assume the action is performed under meaningful scene pressure. Specific aptitudes, disciplines, or advanced maneuvers may later override or modify them.

| Base Action | Rhythm Cost | Attrition |
| --- | ---: | ---: |
| Free action (Drop, Speak) | 0 | 0 |
| Interact | 3 | 1 * |
| Move | 5 | 1 |
| Specialization | 5 | 1 |
| Attack with One-Handed Weapon | 5 | 1 |
| Attack with Two-Handed Weapon | 7 | 1 |
| Attack with Two One-Handed Weapons | 7 | 1 |

\* Interact generates 1 Attrition only when the interaction is meaningful and performed under real pressure. Trivial or non-pressured interactions generate 0.

Specialization generates 1 Attrition. Any use of a specialization in a hostile scene has real cost — the character diverts attention from active threats to execute the skill. Not as demanding as attacking or defending, but not free. Covers jumping, acrobatics, perception, interpretation, tracking, and all other specialization types equally.

### Structural rule

- Standard meaningful actions under pressure → **1 Attrition**
- Heavy or strongly committed actions → **2 Attrition**
- Extreme actions → **3 Attrition** (pending specific ability definitions)

This baseline is consistent with the adopted Fatigue timing principle: Fatigue 1 should arrive after the enemy's main logic has become actionable, but before that logic has been fully exploited and the threat has collapsed.

---

## Competency and Rhythm

Competency rank may interact with rhythm in two distinct ways:

1. **Ability unlock:** A competency rank unlocks new abilities that have their own rhythm values — faster or slower than the base action family. The base family rhythm is not changed; a new ability is added.

2. **Friction reduction:** A specific competency bonus may reduce the rhythm cost of a specific ability or action. This is always ability-specific, not family-wide. A high weapon rank does not automatically make all one-handed attacks cost less than 5 — it may unlock a specific attack that costs 3.

This keeps the base layer stable while allowing competency to create meaningful tempo advantages through deliberate design.

---

## Summary Table

| Base Action | Rhythm Cost | Attrition |
| --- | ---: | ---: |
| Free action | 0 | 0 |
| Interact | 3 | 1 * |
| Move | 5 | 1 |
| Specialization | 5 | 1 |
| Attack with One-Handed Weapon | 5 | 1 |
| Attack with Two-Handed Weapon | 7 | 1 |
| Attack with Two One-Handed Weapons | 7 | 1 |

---

## Official Decisions Adopted

1. Base rhythm costs are assigned by **action family**, not by exact weapon or specialization name.
2. Terrain does not change the rhythm cost of movement; it changes distance, difficulty, and consequences.
3. One-handed attacks use the Standard rhythm baseline (5).
4. Two-handed attacks use the Heavy rhythm baseline (7).
5. Dual-wield attacks use the Heavy rhythm baseline (7) due to coordination and offensive commitment.
6. A universal read/understand action exists at Standard baseline before specific reading abilities are defined.
7. Drop and Speak are free actions (cost 0) within defined constraints.
8. Competency rank interacts with rhythm through ability unlocks or ability-specific friction reduction — not through automatic family-wide cost reduction.
9. More specific abilities may later override or modify these values; this document defines the universal floor.

---

## Open Questions

1. Which advanced abilities should reduce rhythm below their family baseline, and which should instead reduce Attrition or increase reliability?
2. Should certain shields or defensive styles become their own base action family?
3. Should aimed attacks remain within weapon families or become a separate rhythm category?
4. At what point should movement split into controlled movement vs. forced or desperate movement?
5. Should certain high-demand specialization uses (e.g. a complex crafting action mid-combat) warrant a Heavy band instead of Standard?

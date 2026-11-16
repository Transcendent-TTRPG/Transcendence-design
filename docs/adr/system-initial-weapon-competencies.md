# ADR — Two Starting Weapon Competencies

**Status:** Adopted by the project creator, 2026-10-07
**Scope:** Character creation; all playable species and backgrounds
**Related:** `data/system/competencies.yaml`, `docs/system/competencies.md`, corebook chapters 3 and 5

## Problem

The corebook allowed replacing initial natural-weapon competencies with manufactured-weapon competencies without specifying a universal count. Narrative profiles inferred one trained competency per natural weapon. This reduced the starting training allocation for species with a single natural weapon.

## Decision

Each character receives two distinct weapon competencies at level 1 / Novice. The choices may be anatomically available natural weapons or manufactured weapon types and must fit the character's prior experience. Species, background, and natural-weapon count do not alter this allocation.

The choices cannot be stacked into one level-2 competency. Unselected weapons start at level 0; natural weapons remain available anatomically and use the existing untrained rules. Natural anatomy does not grant additional trained weapon competencies. A manufactured-weapon competency does not grant possession of a weapon.

## Invariants

- Level 1 is still Novice under the existing rank restructure.
- Only specializations grant Synapsis; weapon training does not increase characteristics.
- The starting specialization package and Major Affinity do not change.
- Armor, shield, Evasion, and Resistance competencies remain separate; this decision does not define or change their starting allocation.
- Weapon effects, profiles, Techniques, and later progression do not change.
- Competency in a weapon type is distinct from possession of equipment.

## Examples

- A Panin may select Bite 1 and one manufactured weapon competency 1.
- A Panin may select two distinct manufactured weapon competencies 1 and keep Bite at 0.
- A species with two natural weapons may select both at 1, one natural and one manufactured at 1, or two manufactured at 1.
- Spending both choices on Bite to start at level 2 is invalid.

## Consequences

The rule equalizes the starting weapon-training allocation, not overall species balance. Existing Kairu and Nerum allocations already satisfy the rule and remain unchanged. Their explanations no longer derive the number of trained competencies from anatomy.

This decision replaces the implicit one-competency-per-natural-weapon assumption, not the existing specialization-rank ADR. The creator's accepted rule is synchronized into Spanish and English Publications and registered in Design for downstream reuse.

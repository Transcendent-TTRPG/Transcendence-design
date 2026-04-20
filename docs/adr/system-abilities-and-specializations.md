# ADR — Abilities and Specializations: Core Distinction

**Status:** Adopted
**Scope:** All competency types — weapons, armor, shields, evasion, specializations, resistances
**Related:** `competencies.yaml`, `combat-atb-rhythm-costs.md`, `combat-enemy-readability.md`

---

## Purpose

This document establishes the fundamental distinction between using a specialization directly and using an ability unlocked by a competency. This distinction governs how narrative and mechanical effects are separated across the system.

---

## Design Pillars

Three principles underpin all ability and specialization design:

1. **Super narrative** — every mechanic must feel grounded in the fiction of the world. Rules exist to describe what characters actually do, not to impose abstractions onto them.
2. **Super congruent** — mechanics must match the fiction consistently. If something makes narrative sense, the rules should support it; if it does not, the rules should prevent it.
3. **Universal capability, specialization efficiency** — any creature can attempt almost any action. Competencies, equipment, and training do not gate access — they make skilled characters faster, cheaper, and more effective.

---

## Core Distinction

### Specialization (raw use)

A specialization is a natural capability that any sufficiently developed creature can exercise. Using a specialization directly produces a **narrative effect only**.

The character understands, perceives, interprets, or interacts — but the mechanical state of the scene does not change automatically. Changing the mechanical state requires **follow-up actions** based on what was learned or observed.

**Example:** A character uses Interpretation during combat to study a territorial creature. They now understand that the creature is territorial and why it behaves as it does. The territorial trait is not removed. To remove it mechanically, the character must take follow-up actions — for instance, forcing the creature out of its territory, which would then strip the trait because its condition no longer holds.

This is intentional: the narrative consequence is real and the fiction is respected, but the mechanical change requires effort proportional to its impact.

---

### Ability (from competency)

An ability is a defined technique, maneuver, or application unlocked by reaching a specific competency level or rank. Abilities always require at least one competency as a prerequisite.

An ability produces both a **narrative effect and a direct mechanical effect** in the same action, without requiring follow-up actions.

The ability specifies:

- its competency prerequisite(s)
- its rhythm cost and Attrition cost
- its mechanical effect (bonus granted, penalty imposed, trait modified or removed, condition applied, etc.)
- the narrative framing that explains why the effect is legitimate

**Example:** An ability unlocked at Interpretation Adept allows the character to read and exploit a creature's behavioral pattern in one action. On a successful check, the territorial trait is directly penalized or suspended for a duration — without requiring the character to physically remove the creature from its territory. The ability encodes both the narrative logic and the mechanical outcome.

---

## Which Competencies Unlock Abilities

All competency types can unlock abilities. This is not limited to weapons.

| Competency type | Example ability sources |
| --- | --- |
| Weapons | attack techniques, opening maneuvers, follow-up strikes |
| Armor | damage absorption stances, reactive blocks, durability trades |
| Shields | shield bash, interception, cover maneuvers |
| Evasion | counter-step, redirect, distance exploitation |
| Specializations | behavioral reads, environmental exploits, precision actions |
| Resistances | condition shrug-offs, recovery accelerators, exposure immunity windows |

An ability rooted in a specialization has the same design weight as one rooted in a weapon competency. The distinction is not between "combat" and "non-combat" — it is between the base narrative use of a skill and the explicit, costed, mechanically-defined use of a trained technique.

---

## Naming

The canonical term for player-accessible competency-based techniques is:

- **ES:** Técnicas
- **EN:** Techniques

Selected because it works uniformly across all competency types — weapon techniques, evasion techniques, interpretation techniques, resistance techniques — without implying an exclusively martial context. It is also immediately clear at the table: "I use my pattern-reading Technique" or "I execute the reactive shield Technique."

This term is capitalized when used as a game term in prose.

---

## Structural rule

> A specialization used directly → narrative consequence, mechanical change requires follow-up.
> An ability from a competency → narrative + mechanical consequence in the same action.

This line must remain clear across all chapter and ability designs.

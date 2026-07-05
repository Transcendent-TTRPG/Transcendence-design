# ADR — Abilities and Specializations: Core Distinction

**Status:** Adopted (v0.2 — expanded with derivation rule and technique design principles 2026-07)
**Scope:** All competency types — weapons, armor, shields, evasion, specializations, resistances
**Related:** `competencies.yaml`, `combat-atb-rhythm-costs.md`, `combat-enemy-readability.md`, `docs/system/specialization-technique-domains.md`

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

## What Specializations Are

A specialization is a **practiced domain** — a field of repeated activity that develops a recognizable body of physical or mental capability.

That body of capability is not limited to the domain's literal subject. Training in Jumping does not only produce the ability to jump farther. It produces explosive start mechanics, impact absorption, body commitment, momentum control, and recovery from unstable contact. These capabilities transfer.

Specializations are therefore **transversal** by nature: the knowledge developed in one domain can be applied, through training, to solve problems in other domains. A practiced climber knows how to anchor the body against resistance — and that anchoring logic can be applied to resisting forced displacement, holding a door against pressure, or keeping an ally from falling. None of these require climbing.

This is the design principle behind specialization technique authoring. The specialization is the source of a capability. A technique is the application of that capability to a different problem.

---

## The Derivation Rule

A technique rooted in a specialization must **transfer** the underlying capability of that specialization to a different problem. It must not be a direct improvement to the base specialization itself.

**What this means in practice:**

- A Jumping technique does not make the character jump farther or higher. It uses the explosive impulse, landing control, or momentum logic developed through jumping to solve a tactical, defensive, or positional problem.
- A Climbing technique does not make the character climb better. It uses the anchoring, tension distribution, and surface-reading logic of climbing to solve a problem involving resistance, loss of position, or support from an unstable angle.
- A Tolerance technique does not reduce damage before it lands. It uses the body logic of functioning through internalized suffering to preserve agency when the body is already failing.

The question that validates a technique design is not *"does this relate to the specialization?"* but *"is this the specialization's underlying capability applied to a new problem?"*

**The derivation chain:**

> Specialization → practiced capability → transferred application → technique

The technique is valid when the derivation chain is traceable and the application is genuinely distinct from the base specialization's literal subject.

---

## The Invalid Technique Framework

Three categories of invalid technique exist. Each blocks a distinct design failure.

### 1. Same-specialization upgrades

Techniques that simply make the character better at the base specialization itself.

Examples: jump farther, climb faster, throw harder, swim better, track more accurately, lie more convincingly.

These are invalid because they do not transfer the capability anywhere — they amplify the base skill, which is what rank progression already does. A higher-rank character with Jumping already jumps better. A Jumping technique that just makes you jump farther is a duplicate of rank, not a new design.

### 2. Domain trespass

Techniques that reproduce what another specialization is specifically supposed to do.

Examples: a Deception technique that achieves the concealment outcome of Stealth; a Riding technique that replaces Balance for non-mounted posture problems; a Tracking technique that navigates an unknown region with no traces.

These are invalid because they undermine specialization differentiation. If any specialization can produce the outcome of another, there is no reason to pursue the other. The invalid list for each domain in `specialization-technique-domains.md` explicitly names which adjacent specializations cannot be trespassed.

### 3. Logic bypass

Techniques that claim broad effects without using the specialization's actual logic.

Examples: broad defense from Jumping without impulse, landing, or impact logic; generic resistance from Acclimation without exposure or environmental threshold logic; group support from Riding without mount, route, or shared movement.

These are invalid because the narrative justification is missing. If the specialization's actual mechanism is not present in the technique's design, the technique is borrowing the specialization's name without its logic.

A technique that transfers the specialization's underlying capabilities to a different problem is always valid — even if it looks unusual at first. When evaluating a technique against the invalid list, the question is: *is this blocked because it IS the base skill done better, because it trespasses another domain's core territory, or because it bypasses the specialization's logic requirements entirely?* If none of those apply, the technique is valid.

---

## Technique Domain Authority

Per-specialization technique identity — what each specialization may produce as techniques, what it may produce secondarily, and what it should never do — is defined in:

`docs/system/specialization-technique-domains.md`

That document is the authoring boundary for all specialization-rooted technique writing. The present ADR establishes the structural rules; the domains document implements them per specialization.

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

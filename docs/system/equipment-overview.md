# Equipment Overview

**Authority data:** `data/system/equipment.yaml`
**Related docs:** `docs/system/competencies.md`, `docs/system/roll-types.md`, `docs/system/attrition-fatigue.md`, `docs/system/weapon-technique-profiles.md`

---

## Purpose

Equipment is not only inventory. It is a mechanical layer that shapes how a character attacks, defends, absorbs impact, and expresses specialization.

This document defines the stable structural rules for:

- equipment slots
- armor types
- zone-based blocking
- shield role
- weapon assignment (`Primary` / `Auxiliary`)
- random hit location for `NPC -> PC`

It does **not** define the full item catalog yet. Specific weapons, armors, materials, powers, and durability tables belong in later equipment data.

Natural weapons are also outside the full item catalog, but they should connect to the same combat authoring layer through compatible Weapon Technique Profiles rather than through an isolated parallel system.

---

## Core Principle

Armor in Transcendence is **piece-based**, not a single abstract value.

A character may mix different armor types across body slots:

- head / helmet
- torso / chestpiece
- arms / bracers
- legs / trousers
- feet / boots

This is intentional. Different cultures, roles, and tactical needs may favor heavier protection in one zone and lighter mobility in another.

For offensive identity, Transcendence should also avoid a one-tree-per-item model. Concrete weapon items, natural attack forms, and combat Techniques should connect through shared combat profiles when possible.

---

## Armor Types

There are three armor types:

- **Light**
- **Medium**
- **Heavy**

Each piece belongs to one of these types. Type determines:

- base block
- how `Evasion` and Agility contribute to `D.R.`
- the kind of secondary bonus a slot provides

### Defense interaction with `D.R.`

- **Light armor:** full `Evasion`; full Agility
- **Medium armor:** full `Evasion`; half Agility (minimum 1)
- **Heavy armor:** half `Evasion` (minimum 1); no Agility

If a defense is resolved against a specific hit zone, use the armor type relevant to that zone.

---

## Armor Competencies

Armor competency is split by armor type:

- Light Armor
- Medium Armor
- Heavy Armor

Armor competency does not mean "more passive defense in every circumstance."
It represents trained use of the armor's blocking profile, weight, structure, and tactical handling.

This competency interacts directly with zone-based block.

### Armor competency progression

Armor competency progresses through **failed `D.R.`**, but only when all of the following are true:

- the hit resolves against an armored zone
- the armor in that zone actually participates in reducing the impact
- the defense was not primarily resolved by shield Technique or pure evasion

Progress is gained for the **armor type** involved in the resolved zone:

- hit on light armor zone -> Light Armor competency
- hit on medium armor zone -> Medium Armor competency
- hit on heavy armor zone -> Heavy Armor competency

---

## Zone-Based Block

When a hit resolves against a body zone, blocking is determined by the piece equipped in that zone.

### Active Block Formula

```text
Zone Block = BC + BM + CD + CO
```

Where:

- `BC` = base by armor category
- `BM` = material bonus
- `CD` = defensive competency level in the relevant armor type
- `CO` = piece grade

### Base by category (`BC`)

- Light = 2
- Medium = 4
- Heavy = 6

### Material bonus (`BM`)

```text
BM = floor(durability / 10)
```

This assumes armor pieces are made from materials with durability and potency values defined elsewhere.

### Piece grade (`CO`)

Each armor piece has a grade from `1` to `3`.

The same grade also functions as the piece's constant slot bonus where relevant.

---

## Defense Resolution Model

`D.R.` uses a **hybrid model**:

- evasion is still a core defensive competency
- Agility contribution depends on the armor type of the resolved zone
- if defense fails, the hit is still filtered through the zone's block value

### Resolution order for `NPC -> PC`

1. Determine hit zone
2. Identify armor type in that zone
3. Calculate `D.R.` using evasion and the Agility rule of that zone
4. If the attack still connects, apply zone block

### `D.R.` by resolved zone

```text
D.R. = 1d10 + Applicable Evasion + Applicable Agility + Defense Bonuses
```

Where `Applicable Evasion` and `Applicable Agility` depend on the armor type in the struck zone:

| Armor in struck zone | Applicable Evasion | Applicable Agility |
|---|---|---|
| unarmored | full Evasion | full Agility |
| light | full Evasion | full Agility |
| medium | full Evasion | half Agility, rounded up, minimum 1 |
| heavy | half Evasion, rounded up, minimum 1 | 0 |

`Defense Bonuses` may include shields, Techniques, reactions, or situational effects.

If the zone is unarmored, treat it as using full Evasion, full Agility, and no armor block unless another rule states otherwise.

---

## Slot Effects

Each armor slot grants a secondary effect based on its armor type.

These effects are always tied to the piece's **grade**.

### Trousers / Legs

- **Light:** bonus to Agility-related `S.R.`
- **Medium:** bonus to Strength-related `S.R.`
- **Heavy:** bonus to Tenacity-related `S.R.`

### Boots / Feet

- **Light:** movement speed bonus equal to grade
- **Medium:** bonus to reactive checks such as Balance or dodging area effects
- **Heavy:** bonus to `R.R.` against forced movement, knockdown, and displacement

### Bracers / Arms

- **Light:** bonus to `S.R.` when bracers are used as part of a Technique's attack structure
- **Medium:** bonus to `A.R.` in active Techniques
- **Heavy:** bonus to `I.R.` in active Techniques

### Helmet / Head

- **Light:** Preparation increase
- **Medium:** bonus to Composure-related `S.R.`
- **Heavy:** bonus to `R.R.` against concussion, blindness, and stun-like effects

### Chestpiece / Torso

The torso piece interacts with **Sanity**, a future derived attribute linked to Composure and the cosmic horror/corruption layer.

- **Light:** Sanity bonus = grade
- **Medium:** Sanity bonus = grade × 2
- **Heavy:** Sanity bonus = grade × 3

This dependency is not fully active until the Sanity system is defined.

---

## Shields

Shields are not identical to armor.

They provide defensive value by equipment, but shield competency is tied primarily to **Technique use**, not to universal passive defense increase.

Shield competency should support actions such as:

- intercepting
- protecting
- redirecting
- covering another target
- shield-based defensive Techniques

### Shield Defense by Type

- Light shield = grade
- Medium shield = grade
- Heavy shield = grade + 1

This shield value applies as a general `D.R.` bonus.

### Shield Movement Penalty by Type

- **Light shield:** no movement penalty
- **Medium shield:** movement penalty = grade
- **Heavy shield:** movement penalty = grade × 2

Shield competency does not increase this passive `D.R.` value directly. Its progression supports shield maneuvers, and reaching **Master** reduces the active movement penalty of the equipped shield by `grade` (minimum 0).

---

## Random Hit Location (`NPC -> PC`)

To reduce Narrator bias, random hit location is used when an `NPC` or enemy hits a `PC`.

This table is **not** used for `PC -> target` attacks. Players may target specific zones when their available mechanics, knowledge, vulnerabilities, or Techniques allow it.

Creatures also use internal slots or equivalent anatomical regions for `D.R.`, block, and vulnerabilities. What changes is anatomy, not the existence of zones.

### Random Hit Table

| 1d100 | Zone | Equipment slot consulted |
| --- | --- | --- |
| 01–04 | Head | Helmet |
| 05–10 | Feet | Boots |
| 11–45 | Torso | Chestpiece |
| 46–65 | Arms | Bracers |
| 66–100 | Legs | Trousers |

This distribution is intentionally weighted toward torso and legs, while keeping head and feet relatively rare.

Because this table is rolled before full defensive resolution for `NPC -> PC`, it also determines which armor type constrains Evasion and Agility in the `D.R.` formula.

---

## Weapon Assignment

Weapons use two broad assignments:

- **Primary**
- **Auxiliary**

### Primary weapons

Primary weapons are designed to be the character's main source of damage.

Typical traits:

- higher damage dice
- stronger single-hit output
- stronger pressure against durability or protection

### Auxiliary weapons

Auxiliary weapons support faster or additional attack structures.

Typical traits:

- lower damage dice
- lower single-hit impact
- stronger use in combinations, sequences, or two-weapon setups

This assignment is structural. The full weapon catalog remains separate from this overview.

---

## Equipment Handling

Armor removal time depends on armor type:

- **Light armor:** can be removed quickly; practical during combat as an interaction-scale action
- **Medium armor:** partial loosening in combat is possible, full removal is slower
- **Heavy armor:** not practical to remove in combat; full removal normally requires time and often assistance

Precise timing values remain provisional until the action-time layer for equipment handling is finalized.

---

## Open Design Questions

1. How are internal slots grouped across major creature anatomies in the bestiary layer?
2. How does Sanity interact with chestpiece bonuses once the cosmic horror/corruption chapter is defined?

---

## Structural Conclusions

1. Armor is piece-based and zone-based, not a single abstract stat.
2. Mixed armor loadouts are valid and intended.
3. `D.R.` uses a hybrid model: evasion plus zone-dependent Agility, followed by zone block if hit connects.
4. Armor type directly changes how Agility contributes to `D.R.`
5. Zone block is determined by category, material, competency, and piece grade.
6. Failed `D.R.` with Learning Advantage can progress armor competency by resolved armor type.
7. Shield value contributes generally to `D.R.` as equipment; shield competency is primarily about Technique use.
8. Random hit location exists to constrain Narrator bias for `NPC -> PC`.
9. Player targeting is governed by player-facing mechanics, not by the random hit table.

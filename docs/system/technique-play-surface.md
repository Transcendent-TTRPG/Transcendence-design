# Technique Play Surface

**Authority sources:** `docs/system/techniques.md`, `data/system/techniques.yaml`  
**Related publication surface:** `Transcendence-publications/core-books/transcendence-corebook/09-techniques/`  
**Related quick reference surface:** `Transcendence-publications/technique-cards/transcendence-technique-cards/`

---

## Purpose

This document defines the **final play-facing surface** for Techniques.

It exists because the authority-layer Technique format is not the same thing as
the final player-facing or table-facing format.

The authority layer must preserve:

- authoring intent
- doctrinal distinctions
- dependency notes
- cost reasoning
- simulator implications
- and other design-facing detail

The final play-facing surface must instead optimize for:

- quick reading
- table relevance
- tactical clarity
- consistent card generation
- and clean corebook presentation

In short:

- `techniques.md` and `techniques.yaml` are **authority**
- the corebook and tarot cards are **play surfaces**

The play surface is derived from authority, not identical to it.

---

## Core principle

Every finalized Technique should be readable in play without forcing the player
to parse authoring scaffolding, doctrinal commentary, or requirements that are
not actually meaningful game mechanisms.

The play surface should present:

- what the Technique is
- when it can be used
- what mechanical surfaces it touches
- what the actual cost is
- what concrete game conditions must be true
- and what happens if it resolves

---

## Canonical play-facing structure

The canonical play-facing Technique surface is:

1. `Type - Category`
2. `Name`
3. `Competency Rank`
4. `Flavor Text`
5. `Range`
6. `Area`
7. `Duration`
8. `Primary Roll`
9. `Saving Roll` if and only if there is a distinct negating roll
10. `Impact` if the Technique resolves an `I.R.` or equivalent damage payload
11. `Rhythm`
12. `Attrition`
13. `Requirements`
14. `Keywords`
15. `Effect`

This structure should be the same semantically across:

- corebook presentation
- tarot technique cards
- later quick-reference outputs

The difference between core and card should be **compression**, not a different
data model.

---

## Field definitions

### 1. Type - Category

This is the top-line operational classification.

Examples:

- `Active - Attack`
- `Reactive - Attack`
- `Active - Utility`
- `Reactive - Utility`
- `Passive - Utility`

### Category compression rule

The final play surface should use only:

- `Attack`
- `Utility`

`Defense` does **not** need to survive as a separate play-facing category.

If a Technique defends primarily by:

- intercepting
- repositioning
- granting mitigation
- protecting another actor
- or spoiling an exchange

it should normally surface as:

- `Utility`

If a Technique defends by making an attack roll that directly resolves an
offensive exchange or impact payload, it may surface as:

- `Attack`

The goal is fast reading, not preserving every authority-side taxonomy detail.

### 2. Name

The published player-facing name.

### 3. Competency Rank

This should normally appear directly under the name.

Example:

- `Novice Rank`

This preserves the real learning threshold without expanding the entire
learning payload in the card or in the immediate corebook block.

### 4. Flavor Text

A short evocative line that helps the Technique feel held, imagined, and
remembered.

Flavor text is not a rules paragraph.

### 5. Range

The operational range of the Technique.

Examples:

- `Weapon`
- `Self`
- `1 m`
- `3 m`
- `Line of Sight`

### 6. Area

The tactical scope of the Technique.

Examples:

- `1 creature`
- `Self`
- `Line 3 m`
- `Cone 2 m`
- `Zone 1 m`

### 7. Duration

How long the effect matters in play.

Examples:

- `Instant`
- `Until next activation`
- `Scene`

### 8. Primary Roll

The main roll the Technique resolves through.

Examples:

- `A.R.`
- `S.R.`
- `C.R.`
- `R.R.`
- `D.R.`

### 9. Saving Roll

Show this field only when there is a **distinct roll that negates the Technique
before its effect takes hold**.

Examples:

- `R.R.`
- `C.R.`
- `D.R.`

Do **not** use this field for:

- the Technique's own primary roll
- normal attack resolution when the Technique is simply making an attack
- vague contextual exchange handling

If there is no distinct negating roll, omit this field from the play-facing
surface.

### 10. Impact

Show this field when the Technique resolves:

- `I.R.`
- weapon impact
- or another direct damage payload that players need to parse fast

If there is no impact payload, omit it or show `—` depending on the visual
format.

### 11. Rhythm

The real Rhythm cost.

### 12. Attrition

The real Attrition cost.

### 13. Requirements

Requirements in the play-facing surface must be **real game mechanisms**.

Good requirements:

- weapon profile
- movement condition
- range condition
- state condition
- target condition
- equipped item
- species or learned threshold if truly required

Bad play-facing requirements:

- "clear line and enough space to present the point"
- "good footing"
- "proper stance"
- or other implied common-sense physical logic unless they are formalized game
  mechanisms

Those may still matter in authority or narrative adjudication, but they should
not consume play-facing requirement space unless the game actually tracks them.

### Active-technique requirement rule

For `Active` Techniques, the play-facing `Requirements` field should normally
contain only:

- stable access requirements
- equipment or profile requirements
- formal state requirements
- other tracked game-mechanism requirements

Do **not** convert ordinary tactical context into a formal requirement just
because the Technique is commonly used in that context.

Examples of context that usually should **not** survive as a formal requirement
for an active Technique:

- the enemy is contesting your line
- the enemy is compressing distance
- the opponent looks ready to commit

Those may matter for tactical judgment, trigger understanding, or effect
reading, but they are not the same as a formal game gate unless the system
explicitly tracks them as one.

### 14. Keywords

Keywords should carry **useful system information not already shown elsewhere**.

Do not repeat:

- `Reactive` if `Type` already says `Reactive`
- `Attack` if `Category` already says `Attack`

Good keywords:

- weapon profile
- specialization
- ailment family
- displacement
- interruption
- concealment
- line control
- poison
- infection

### 15. Effect

The effect should say:

- what triggers the Technique in play
- what roll is made
- what happens on success
- what happens on failure when relevant
- and what concrete state change or denial actually occurs

It should be tactical and exact, not doctrinally essayistic.

### Exactness rule

Play-facing wording must stay mechanically exact.

Do not add approximation or uncertainty if the rule itself is exact.

Good:

- `you reposition 1 meter`
- `the target must stop in that space`

Bad:

- `you reposition approximately 1 meter`
- `the target usually stops there`

Compression is allowed. Uncertainty is not.

---

## Core vs card presentation

The corebook and the tarot card should carry the same playable information.

### Corebook

The corebook version may allow:

- slightly fuller effect wording
- slightly fuller flavor line
- more breathing room

### Tarot card

The card version should:

- compress the same information harder
- privilege fast parsing
- keep requirements and keywords sharply bounded

This is a difference of density, not of rules ownership.

---

## What should stay in authority only

These usually belong in authority and should not automatically surface in the
final play-facing block:

- world-origin payload in full
- adaptation notes
- cost note essays
- "why this is not a base action"
- authoring notes
- doctrinal comparison notes
- broad restrictions that are not formal game mechanisms
- simulator framing

These are still essential. They just do not belong in the final quick-read
surface.

---

## Canonical pilot example

The first canonical pilot for this surface is:

- `Cerrar la Línea`

Its publication-facing manual example should be kept aligned across:

- corebook surface
- tarot card prototype

Its authority source remains:

- `docs/system/techniques.md`
- `data/system/techniques.yaml`

---

## Canonical pilot: Cerrar la Línea

### Play-facing classification

- `Reactive - Attack`

### Why the category compresses to Attack

Authority currently classifies `Cerrar la Línea` as `defense`, which is valid
for design discussion because the Technique protects lane ownership and denies
clean entry.

But the final play-facing category should compress to:

- `Attack`

because the Technique resolves through:

- a reactive `A.R.`
- with normal `I.R.`

and its defensive value emerges from what that attack prevents, not from a
separate defensive roll block.

### Play-facing example

**Reactive - Attack**  
**Cerrar la Línea**  
**Novice Rank**

*The point arrives where entry must pass.*

**Range:** Weapon  
**Area:** 1 creature  
**Duration:** Instant  
**Primary Roll:** `A.R.`

**Impact:** `I.R.`  
**Rhythm:** `4`  
**Attrition:** `1`

**Requirements**

- Weapon with `Line Control` profile
- A moving enemy enters your weapon range

**Keywords**

- `Line Control`

**Effect**

When an enemy performs any action involving movement and reaches a square within
your weapon range, before that enemy continues the action, make an `A.R.`. If
successful, resolve `I.R.` normally and the enemy must stop its movement in
that square. If the `A.R.` fails, the enemy continues its action normally.

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

## Language rule

Each play-facing surface must be fully localized to its publication language.

That means:

- Spanish core and Spanish cards should use Spanish-facing names for profiles,
  competencies, and other player-facing labels
- internal authority labels may remain in English when needed for design
  stability, but they do not belong unchanged in the Spanish core or Spanish
  cards
- the same rule applies in reverse for English-facing publication surfaces

Examples for Spanish play surfaces:

- `Unpredictability` -> `Impredecible`
- `Torsion` -> `Torsión`
- internal roll shorthand such as `A.R.` or `I.R.` should not appear if the
  Spanish core uses fully localized player-facing roll labels instead

Prefer complete words for ordinary player-facing language:

- `1 criatura`, not `1 criat.`
- `Duración`, not `Dur.`
- `Salvación`, not `Salv.`
- `Desgaste`, not `Desg.`

Only keep abbreviations when they are canonical rules notation players are
already expected to read as system language, such as `T.A.`, `T.D.`, or `T.I.`.

Player-facing surfaces should not require readers to translate internal labels
mentally while using the rules at the table.

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

Good flavor text for a Technique should usually read like one of these:

- a remembered line of doctrine
- a field saying
- a species-true maxim
- a compact image that helps the move stay in the hand

It should not:

- paraphrase the effect mechanically
- explain the balance logic
- stack abstractions until the line sounds inflated
- read like marketing copy for the Technique

Prefer:

- one strong image
- one strong turn of thought
- species identity over generic fantasy grandeur
- short declarative phrasing over layered metaphor
- physical or tactical imagery over abstract mood

In practice, strong flavor text often feels like:

- `Si avanzan por tu línea, la punta cobra primero.`
- `Cuando el enemigo rompe la línea, la punta la dibuja de nuevo.`
- `La lanza no pide alcance: lo toma.`

Those work because they are:

- brief
- concrete
- species-shaped
- easy to remember at the table

### 5. Range

The operational range of the Technique.

Examples:

- `Weapon`
- `Self`
- `1 m`
- `3 m`
- `Line of Sight`

#### ES publication surface — valid Rango values

| Value | When to use |
| --- | --- |
| `Personal` | The Technique targets only the user or their immediately held point |
| `Alcance del arma` | The Technique's reach is defined by the weapon or natural attack form |
| `Xm` (e.g., `3m`, `5m`) | Fixed metric range independent of weapon |
| `Rango Visual` | Effect applies at visual range — for perception, read, or survey Techniques |

### 6. Area

The tactical scope of the Technique.

Examples:

- `1 creature`
- `Self`
- `Line 3 m`
- `Cone 2 m`
- `Zone 1 m`

#### ES publication surface — valid Área values

| Value | When to use |
| --- | --- |
| `Tú` | Effect applies only to the user — NOT `Personal` |
| `1 Criatura` | Single target at the specified range |
| `Circular Xm` | Circular area around a point (radius in meters) |
| `Cono Xm` | Cone emanating from the user |
| `Línea Xm` | Straight line from the user |

**Key distinction:** `Alcance del arma` belongs in **Rango**, not in **Área**. If a weapon-rooted Technique targets one creature at weapon reach, that is `Rango: Alcance del arma` / `Área: 1 Criatura`.

### 7. Duration

How long the effect matters in play.

Examples:

- `Instant`
- `Until next activation`
- `Scene`

#### ES publication surface — valid Duración values

**Only two values are valid on ES publication surfaces:**

| Value | When to use |
| --- | --- |
| `Instantáneo` | Effect resolves once and ends — no ongoing state |
| `Permanente` | Effect persists until a defined condition removes it |

Sustained stances (e.g., Asentar la Piedra), ongoing bonuses, and lingering states are `Permanente`. End conditions (when the stance breaks, when the state clears) belong in the **Efecto** text, not in the Duración field.

Do **not** use: `Sostenida`, `Hasta Moverse`, `Scene`, `Hasta el siguiente turno`, or any other intermediate value. If an effect is not instantaneous, it is Permanente — its end conditions live in the effect text.

### 8. Primary Roll

The main roll the Technique resolves through.

Authority may track rolls with internal shorthand such as:

- `A.R.`
- `S.R.`
- `C.R.`
- `R.R.`
- `D.R.`

But the final play surface must follow the publication language and notation
standard of that book.

That means:

- if the Spanish core uses Spanish-facing roll names, use those
- do not preserve internal abbreviations automatically just because authority
  or simulator code uses them
- core and card must share the same player-facing roll notation

#### Roll notation by Technique type

**Weapon-rooted Techniques** (origin is a weapon competency such as Spear,
Flexible Weapons, Ranged Weapons):

- Primary roll is `T.A.` (Tirada de Ataque) — the weapon attack roll
- Impact is `T.I.` when damage resolves; omit or show `—` when not applicable

**Non-weapon specialization Techniques** (origin is a non-weapon competency
such as Percepción, Sigilo, Atletismo, etc.):

- Primary roll is `T.E.` (Tirada de Especialización)
- The competency name is understood from the Requirements block; do not repeat
  it on the roll cell unless the card needs disambiguation
- Impact is `—` unless the Technique also produces direct damage payload

**Techniques with no roll** (passive, zone, or declaration-triggered):

- Primary roll is `—`

### 9. Saving Roll

Show this field only when there is a **distinct roll that negates the Technique
before its effect takes hold**.

#### When the primary roll is weapon-rooted

The saving roll is usually a resistance or defense roll:

- `R.R.` (Tirada de Resistencia) — for ailment or alteration application
- `T.D.` (Tirada de Defensa) — when the target's defense is a separate resolve
  gate from the primary exchange

#### When the primary roll is a non-weapon specialization

The saving roll is the **opposing specialization that most directly suppresses
the primary channel**:

- identify what the primary roll is sensing, inferring, or extracting
- ask which specialization a creature would actively use to block that channel
- show it as `T.E. (Specialization)` using the same T.E. notation as the
  primary roll

Examples:

- Technique reads physical living signs through Percepción → saving roll is
  `T.E. (Sigilo)` — the target suppresses their physical profile
- Technique reads emotional state through Empatía → saving roll would be
  `T.E. (Engaño)` or equivalent deception surface

Do **not** use this field for:

- the Technique's own primary roll
- normal attack resolution when the Technique is simply making an attack
- vague contextual exchange handling

If there is no distinct negating roll, omit this field from the play-facing
surface or show `—` depending on the visual format.

### 10. Impact

Show this field when the Technique resolves:

- `I.R.`
- weapon impact
- or another direct damage payload that players need to parse fast

As with roll names, the visible label for the impact payload must follow the
publication language and notation standard of that surface rather than leaking
internal shorthand by default.

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
- kit family when the technique depends on prepared field support
- species or learned threshold if truly required

Requirements should also be localized for the player-facing surface:

- use the Spanish-facing profile or competency label that the reader will see
  elsewhere in the same book
- do not leave internal English profile names on a Spanish rules surface

Bad play-facing requirements:

- "clear line and enough space to present the point"
- "good footing"
- "proper stance"
- or other implied common-sense physical logic unless they are formalized game
  mechanisms

Those may still matter in authority or narrative adjudication, but they should
not consume play-facing requirement space unless the game actually tracks them.

### Kit dependency rule

If a Technique depends on a named kit family to function as written, that kit
should survive into the play-facing surface as a formal requirement.

Do not blur a real kit gate into vague wording such as:

- prepared ammunition
- proper delivery
- suitable tools
- marked payload

if the system already treats that dependency as a named kit family.

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
- kit family
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

# Techniques

**Authority data:** `data/system/techniques.yaml`
**Related ADR:** `docs/adr/system-abilities-and-specializations.md`
**Related docs:** `docs/system/competencies.md`, `docs/system/specializations.md`, `docs/system/roll-types.md`, `docs/system/atb-reference.md`, `docs/system/attrition-fatigue.md`, `docs/system/weapon-technique-profiles.md`

---

## Purpose

This document defines what a **Technique** is in Transcendence, how it differs from raw competency use, which fields every Technique must declare, and how Techniques interact with timing, cost, targeting, duration, and scaling.

The goal is to create a stable authoring model before writing actual Techniques.

---

## Core Definition

A **Technique** is a **competency-rooted, explicitly costed, mechanically-defined application** that produces a narrative and mechanical consequence in the same action.

A Technique is not:

- a raw attribute expression
- a specialization by itself
- a generic action family
- a freeform ruling
- a passive fiction-only capability

A Technique always exists as a trained expression of one or more competencies.

---

## Spectacle Rule

Techniques in Transcendence should feel **spectacular, thematic, and memorable**.

They are not meant to read like flat procedural bonuses or merely efficient mechanical toggles. A good Technique should feel like a heightened trained expression that players want to picture, name, and build toward.

That does **not** mean Techniques should feel magical.

### Core principle

Techniques may be:

- exaggerated
- dramatic
- highly cinematic
- more intense than strict realism would allow

but they must still feel:

- thematically coherent
- physically or fictionally grounded
- functionally caused by something in the character, the equipment, the motion, the pressure, or the trained domain itself

### Not magic

A Technique may bend realism for dramatic effect, but it may not produce effects **from nothing**.

It must always be possible to point to a non-magical cause such as:

- trained timing
- body control
- leverage
- force transfer
- pressure management
- positioning
- equipment interaction
- practiced perception
- conditioned survival response
- social projection
- environmental exploitation

If the only explanation is supernatural emergence, occult projection, or impossible energy creation, it does not belong here. That belongs to later Limbo / magic design, not to Techniques.

### Authoring test

When writing a Technique, ask:

1. Is it exciting enough to feel worth learning?
2. Is its identity primarily thematic, not just numerical?
3. Can its effect be traced to a real trained cause inside the fiction?
4. Would it still make sense if all magic were removed from the scene?

If the answer to `3` or `4` is no, the Technique is drifting out of bounds.

---

## Structural Distinction

### Raw competency use

Using a competency directly produces a **narrative consequence**.

The character observes, analyzes, maneuvers, resists, projects, or acts meaningfully in the fiction, but the scene's mechanical state does not automatically change unless another rule says so.

### Technique use

Using a Technique produces:

- a **narrative consequence**
- a **direct mechanical consequence**

in the same declared use.

That mechanical consequence may:

- grant a bonus
- impose a penalty
- apply or remove a condition
- alter a trait
- reposition
- intercept
- create protection
- open or close a tactical state
- accelerate recovery
- suspend or distort a hostile pattern

This is why Techniques need strict structure.

---

## Combat Profile Layer

For combat Techniques rooted in weapons, shields, thrown attacks, flexible attacks, ranged attacks, or natural attack forms, authoring should usually pass through the **Weapon Technique Profile** layer defined in [weapon-technique-profiles.md](/Users/juangomez/Transcendence-workspace/Transcendence-design/docs/system/weapon-technique-profiles.md).

This layer exists so the game does not need:

- a separate Technique tree for every individual weapon item
- a disconnected combat subsystem for natural weapons
- old action-point combo logic rebuilt on top of ATB

In practice:

- weapon competency still gates use
- the profile shapes combat fantasy and effect family
- the Technique defines the actual action, cost, trigger, and resolution

Combat Techniques do not need a profile in every case, but they should prefer one whenever the missing differentiation is about combat style rather than about a single isolated Technique.

---

## Canonical Fields

Every Technique entry should declare, at minimum, the following:

| Field | Purpose |
| --- | --- |
| `name` | Canonical name of the Technique |
| `origin` | Which competency or competencies unlock it |
| `category` | Broad mechanical family |
| `type` | Active, Reactive, or Passive |
| `trigger` | What allows or prompts its use |
| `requirements` | Minimum levels, ranks, equipment, states, or prerequisite Techniques |
| `learning` | How the Technique is acquired through study and practice |
| `target` | Self, ally, enemy, creature, object, zone, structure, etc. |
| `range` | Reach or application distance |
| `area` | Single target, line, radius, self-zone, wide area, etc. |
| `duration` | Instant, scene, rounds/ATB, sustained, permanent, etc. |
| `cost` | Rhythm, Attrition, charges, uses per rest/day, durability trade, or other cost |
| `saving_roll` | Whether a roll can resist, reduce, or negate it |
| `description` | Flavor and fiction-facing summary |
| `effect` | Actual mechanical resolution |
| `scaling` | How the Technique improves with rank, level, or conditions |
| `restrictions` | Limits, incompatibilities, once-per-window clauses |
| `tags` | Internal classification and filtering support |

These fields are the minimum authoring skeleton. A given Technique may also need:

- setup clauses
- follow-up clauses
- concentration/sustain rules
- failure outcome
- partial success handling

---

## Technique Learning

Techniques should not feel as if they are learned magically or unlocked from nowhere.

They are acquired through:

- study
- repetition
- bodily or mental practice
- technical correction
- lived experience in the relevant domain

But this should **not** create a separate mastery track for every individual Technique.

### Core rule

A Technique is either:

- not yet learned
- learned and usable

It does not need its own internal rank ladder by default.

The scaling of a Technique should come from:

- the Technique's own `scaling`
- the user's competencies
- rank, level, requirements, and situational access

not from a second mini-competency attached to the Technique itself.

### Learning paths

Every Technique should declare a `learning` block.

The two standard acquisition routes are:

- `self_study`
- `guided_training`

#### Self-study

The character learns through:

- manuals
- notes
- diagrams
- observation
- repetition
- solo practice

This path should usually take more total hours and may require access to written or recorded material.

#### Guided training

The character learns through:

- a mentor
- a trainer
- a school
- direct correction in practice

This path should usually reduce time, improve reliability, or reduce access friction, but it should not bypass the Technique's normal prerequisites.

### Learning components

Technique learning may use some or all of the following:

- `study_hours`
- `practice_hours`
- `text_or_manual_required`
- `mentor_required`
- `material_cost`
- `access_notes`
- `final_validation`

### Validation rule

If a final validation exists, it should confirm that the Technique was actually internalized.

It should not become a second progression system.

Good examples:

- one successful supervised execution
- one successful practice scene under pressure
- one final relevant roll after required hours are completed

Bad examples:

- separate Technique XP
- Technique rank trees
- repeated per-Technique leveling ladders

---

## Technique Categories

Technique `category` should express what the Technique mainly does in the system.

Initial canonical categories:

- `attack`
- `utility`

A Technique should have one primary category only.

- `attack` covers offensive Techniques whose main purpose is to inflict harm, impose direct offensive pressure, or create an explicitly hostile strike event.
- `utility` covers everything else: defense, mitigation, interception, mobility, control, support, recovery, setup, disruption, and similar effects.

Those distinctions should live in `tags`, not as parallel categories.

---

## Technique Types

### Active

Used deliberately on the character's own initiative or declaration window.

Examples:

- weapon strike pattern
- shield push
- battlefield read
- structured retreat step

### Reactive

Used in response to a trigger, hostile declaration, timing window, or state change.

Examples:

- interception
- counter-step
- reactive block
- emergency shrug-off

### Passive

Always on, conditionally always on, or permanently modifying the way the character operates.

Examples:

- constant reach extension
- always-on resistance window
- stable shield mobility reduction

Passive Techniques still need clear boundaries. They are not excuses for vague permanent power.

---

## Origin and Requirements

Every Technique must name its `origin`.

Origin may be:

- one competency
- two competencies
- a main competency plus an equipment condition
- a main competency plus a state condition

Special rule for `Resistances`:

- a Resistance may **not** be the sole origin of a Technique
- every Resistance-rooted Technique must be hybridized with another competency, specialization, equipment competency, or clearly bounded state logic
- pure Resistance Techniques are not allowed

Examples:

- `shield competency`
- `specialization: Interpretation`
- `weapon: Spear + Evasion`
- `resistance: Poison + specialization: Tolerance`
- `specialization: Tracking + specialization: Survival`

### Resistance rule

Resistances are not a primary self-directed build axis in the same way that weapons, shields, armor strategies, Evasion, or Specializations are.

The player may decide whether to privilege easy recovery from negative states or deeper learning through exposure, but the actual Resistances acquired are largely shaped by encountered threats rather than by fine build planning.

Because of that:

- Resistances should mainly act as **hybrid modifiers**
- they should change how another domain expresses itself under a known threat
- they should not form a standalone Technique school

In practice:

- `Armor + Fire Resistance` is valid
- `Tolerance + Poison Resistance` is valid
- `Resonance + Corruption Resistance` is valid
- `Fire Resistance` by itself is not valid

Pure Resistance Techniques are prohibited.

Requirements may include:

- minimum level
- minimum rank
- equipment type
- armor type
- shield grade
- existing condition
- prior Technique
- environmental requirement

### Access rule

Technique access should not be gated by origin alone.

Every Technique should be able to require:

- an origin competency or hybrid origin
- a minimum competency `rank`
- optionally a profile, support specialization, equipment condition, or state condition

This separates:

- **access** to a class of trained expression
- from **scaling** once the Technique is already known

The competency makes the Technique possible.
The minimum rank decides when the character has enough mastery to express that Technique safely and coherently.

### Why rank gates matter

If access depends only on the base competency, then very advanced Techniques become available too early and differ from lower-tier Techniques only by numerical tuning.

That is not enough.

In Transcendence, higher-tier Techniques should usually represent:

- broader tactical permission
- cleaner timing access
- deeper system interaction
- stronger reliability under pressure
- more demanding trained structure

not merely bigger damage numbers.

---

## Technique Tiers By Rank

Technique tier should usually track the minimum rank required to learn or use the Technique.

This is not a second rank ladder for the Technique itself.
It is an access classification for authoring and QA.

### Tier 1 — Novice access

Minimum rank:

- `Novice`

Expected identity:

- one clear fantasy
- one primary interaction surface
- simple execution
- strong constraints or narrow windows

Typical qualities:

- active use
- short duration
- low systemic complexity
- little or no scene-warping control

### Tier 2 — Adept access

Minimum rank:

- `Adept`

Expected identity:

- one primary interaction surface
- one meaningful secondary surface
- cleaner reliability or broader use window than Tier 1

Typical qualities:

- stronger timing access
- better setup conversion
- moderate control, disruption, or conditional defense

### Tier 3 — Expert access

Minimum rank:

- `Expert`

Expected identity:

- multiple system surfaces with clear coherence
- stronger reaction logic, persistence, zone pressure, or encounter shaping
- higher permission to alter tempo, position, or hostile behavior

Typical qualities:

- serious scene leverage
- better conversion of setup into consequence
- hybrid requirements become more common

### Tier 4 — Master+ access

Minimum rank:

- `Master` or higher

Expected identity:

- rare and high-impact expressions
- major scene or encounter influence
- strong persistence, layered timing, or structural control

Typical qualities:

- should be few
- should be costly, restricted, or both
- should feel meaningfully above lower-tier Techniques in permission, not just in output

### Important distinction

What separates a lower-tier Technique from a higher-tier one should usually be:

- interaction depth
- timing power
- control permission
- reliability
- layered consequence

not just:

- more damage
- more bonus
- more speed

Competency growth already improves execution quality.
Technique tier should mainly control **what kind of trained expression is available**, not just how hard it hits.

---

## Scaling Versus Access

Technique `scaling` and Technique `access` should remain distinct.

### Access

Access is controlled by:

- origin
- minimum rank
- profile
- support specialization
- equipment or state requirements

### Scaling

Scaling is controlled by:

- competency level
- competency rank
- characteristic contribution
- conditional clause inside the Technique
- explicit scaling field in the Technique

Good authoring keeps these separate:

- higher rank unlocks richer Techniques
- higher competency execution makes those Techniques better

---

## QA Budget

Technique balance should not be judged only by intuition or by raw numbers.

The framework should evaluate a Technique by **budget pressure**:

- what surfaces it touches
- how strong those surfaces are
- what timing it uses
- what restrictions compensate for that power

This will not produce perfect automatic balance, but it can reliably identify Techniques that are too large for their intended tier.

### Major pressure sources

The following usually count as major budget pressure:

- strong reactive access
- position or lane control
- zone influence
- persistent condition pressure
- Rhythm manipulation
- Attrition manipulation
- threshold manipulation on follow-up
- reliable mitigation or stability
- multi-surface interaction with no real tradeoff

### Minor pressure sources

The following usually count as minor budget pressure:

- narrow flat bonus
- one bounded reroll clause
- small setup clause
- short-lived support rider
- tightly restricted secondary interaction

### Compensation factors

A Technique can justify higher pressure when it also has:

- higher minimum rank
- stronger equipment restriction
- narrow trigger window
- visible setup requirement
- meaningful counterplay
- saving roll or mitigation window
- higher Rhythm or Attrition cost
- once-per-window or once-per-scene restriction

### QA expectations by tier

#### Tier 1

Should usually have:

- one major surface
- at most one minor secondary surface

Should usually not have:

- strong reactive control plus persistence
- multiple major surfaces
- broad scene shaping

#### Tier 2

Should usually have:

- one major surface
- one secondary surface

May have:

- moderate reactive access
- moderate setup conversion

#### Tier 3

May have:

- two major surfaces if tightly coherent
- stronger timing and control permission
- hybrid leverage

Should still pay with:

- access difficulty
- cost
- or restriction load

#### Tier 4

May carry:

- large scene pressure
- layered timing logic
- heavy persistence or encounter leverage

But should be:

- rare
- expensive
- restricted
- easy to identify as upper-tier

### QA result states

When reviewing a Technique, classify it as:

- `OK` — budget matches its tier
- `Watch` — budget may be high for its tier or restrictions may be too light
- `Outlier` — budget clearly exceeds its intended tier

This classification is not final balance proof, but it is a strong first-pass control.

---

## Target, Range, and Area

These three fields must stay separate.

### Target

Who or what the Technique is aimed at.

Examples:

- self
- ally
- enemy
- creature
- group
- object
- device
- structure
- zone
- text
- phenomenon
- environment

### Canonical target rule

Technique authoring should prefer a **small canonical target vocabulary**.

Initial canonical targets:

- `self`
- `ally`
- `enemy`
- `creature`
- `group`
- `object`
- `device`
- `structure`
- `zone`
- `route`
- `text`
- `message`
- `site`
- `formation`
- `mount`
- `phenomenon`
- `environment`

Do not use open-ended pseudo-targets like:

- `scene`
- `time`
- `sky`
- `campaign`
- `task`
- `presence`

unless a document is explicitly using them as **editorial shorthand** rather than as final authoring data.

### Design rule

If something feels like context rather than a true target, it should usually be handled in one of these places instead:

- `description`
- `effect`
- `trigger`
- `requirements`
- `range`
- `area`
- contextual notes in the domain document

### Range

How far from the user the Technique can be applied.

Examples:

- self
- touch
- melee
- weapon reach
- short
- medium
- long
- line of sight

### Area

How much space or how many targets the effect covers.

Examples:

- single
- self-zone
- cone
- line
- radius
- multi-target
- route segment

---

## Duration and ATB Handling

Duration needs explicit handling because Transcendence does not assume all effects are instantaneous.

Canonical `duration` forms:

- `instant`
- `until_trigger`
- `until_next_turn`
- `for_n_rounds`
- `for_n_atb_cycles`
- `scene`
- `sustained`
- `permanent`

### Design rule

If a Technique persists in time, it must also declare:

- what keeps it active
- what ends it
- whether it occupies ongoing attention or cost

---

## Canonical Tags

Technique tags should use a **controlled vocabulary**.

The goal is not to describe every nuance of a Technique in tags, but to make filtering, comparison, and authoring discipline possible.

### Core tags

Use these as the main reusable tag set:

- `utility`
- `attack`
- `defense`
- `mobility`
- `control`
- `stability`
- `mitigation`
- `recovery`
- `setup`
- `disruption`
- `pressure`
- `support`
- `stealth`
- `precision`
- `survival_window`
- `condition_reduction`

### Restricted tags

These are allowed, but should be used more sparingly and only when the distinction matters structurally:

- `interception`
- `anti_displacement`
- `counter_positioning`
- `counter_read`
- `reposition`
- `escape`
- `pattern_exploitation`

### Tags to avoid as canonical authority

The following are too editorial, too vague, or too close to prose notes to be good long-term authority tags:

- `pattern_exploitation`
- `fine_precision`
- `reading`
- `exploitation`
- `protection`
- `posture`
- `reach`
- `displacement`
- `mobility_denial`
- `delayed_shrug_off`
- `self_cleansing`

These may appear temporarily in exploratory design notes, but final authoring should usually express the distinction through:

- a core tag
- a restricted tag
- or the prose in `identity_notes`, `effect`, or `restrictions`

### Tag rule

When assigning tags to a Technique or a Technique domain:

1. prefer core tags first
2. use restricted tags only when the extra distinction matters
3. do not stack many near-synonyms
4. if a nuance cannot be expressed cleanly in the controlled vocabulary, put it in prose instead of inventing a weak tag

Sustained Techniques should not exist without maintenance language.

---

## Cost Model

Every Technique must declare cost explicitly.

At minimum, consider:

- `rhythm_cost`
- `attrition_cost`

Optional additional costs:

- durability trade
- limited uses per scene
- limited uses per rest
- resource charge
- self-exposure
- temporary drawback

### Rule

If a Technique changes the scene mechanically, it should not feel costless unless it is deliberately built as a passive or highly constrained effect.

---

## Saving Roll / Resistance

Not all Techniques allow prevention.

When they do, the entry should specify:

- whether the target gets a roll
- which roll type applies
- whether success negates, reduces, or changes the outcome

Typical forms:

- `none`
- `D.R. negates`
- `R.R. reduces effect`
- `S.R. opposed`
- `A.R. or D.R. contextual`

This field should describe outcome logic, not just name a roll.

---

## Effect Writing Rule

`description` and `effect` must stay separate.

### Description

What the Technique looks or feels like in the fiction.

### Effect

What changes mechanically.

If a Technique cannot be stated clearly in mechanical terms, it is not ready.

---

## Tags

`tags` carry the finer functional language that should not bloat `category`.

Common tag families include:

- `defense`
- `mitigation`
- `interception`
- `mobility`
- `control`
- `support`
- `recovery`
- `counter`
- `setup`
- `disruption`
- `pressure`
- `follow_up`
- `line_control`
- `spacing`
- `reading`
- `protection`

Tags are descriptive, combinable, and can express secondary identity.

Examples:

- a passive armor Technique:
  - `category: utility`
  - `type: passive`
  - `tags: [defense, mitigation, stability]`
- a reactive shield Technique:
  - `category: utility`
  - `type: reactive`
  - `tags: [defense, interception, line_control]`
- a spear opener:
  - `category: attack`
  - `type: active`
  - `tags: [pressure, follow_up, reach]`

---

## Scaling

A Technique may scale by:

- competency level
- competency rank
- associated characteristic threshold
- weapon or shield grade
- target state
- scene condition

Scaling should improve one or more of:

- accuracy
- potency
- duration
- area
- resistance pressure
- cost efficiency
- reliability

Avoid scaling that improves everything at once.

---

## Authoring Rule

Before writing a Technique, answer these questions:

1. What competency domain makes this possible?
2. Why is this not just raw use of that competency?
3. What direct mechanical change does it create?
4. What timing window does it occupy?
5. What does it cost?
6. How can it be resisted, if at all?
7. How does it end?
8. How does it scale?

If these are not clear, the Technique is still a concept, not an authored rule.

---

## Next Design Layer

This document defines the Technique skeleton.

The next required layer is:

- **competency technique domains**

That layer defines what kinds of Techniques each competency is structurally suited to produce.

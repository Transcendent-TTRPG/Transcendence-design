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

### Metaphysical is not automatically magical

Not every hard-to-explain or uncanny phenomenon is automatically:

- magical
- taumatic
- extranatural

Transcendence should allow room for effects that feel:

- uncanny
- metaphysical
- paranormal
- difficult to measure or prove

without treating them as Limbo-derived or Tauma-driven by default.

This is especially important for domains such as:

- `Aura`
- `Instinct`
- `Bond`
- some forms of presence, intuition, or human connection

A Technique may therefore feel improbable, eerie, or deeply non-mechanical in a scientific sense and still remain inside the natural order of the setting, as long as it does **not** rely on:

- Tauma sources
- Limbo leakage
- elemental emanation
- extranatural causation
- energy appearing from nowhere

In other words:

- not fully explainable does not mean magical
- not measurable does not mean extranatural
- not ordinary does not mean Limbo

The forbidden boundary is not "anything unusual."
The forbidden boundary is **taumatic or extranatural causation without belonging to that subsystem**.

### Authoring test

When writing a Technique, ask:

1. Is it exciting enough to feel worth learning?
2. Is its identity primarily thematic, not just numerical?
3. Can its effect be traced to a real trained cause inside the fiction?
4. If it feels uncanny or metaphysical, can it still be explained without Tauma or extranatural causation?
5. Would it still make sense if all overt magic were removed from the scene?

If the answer to `3`, `4`, or `5` is no, the Technique is drifting out of bounds.

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

## Base Action Rule

Universal base actions exist as a **common floor**, not as the main reward structure of play.

They are intentionally:

- broadly accessible
- low-identity
- low-differentiation
- structurally reliable

They should remain valid when:

- the character does not have the right trigger
- the player wants to conserve resources
- the scene does not justify a more specialized execution
- the character has not yet learned a stronger expressive option for that moment

But they should **not** be the most desirable or expressive form of play over time.

In Transcendence, the primary source of tactical identity should come from **Techniques**, not from repeating generic base actions.

### Design implication

When judging a new Technique, the main question is **not**:

- does it simply outperform the base attack in raw efficiency?

The main question is:

- does it let this character solve a moment in a more specific, thematic, and differentiated way?

### Practical rule

Base actions should usually be:

- the fallback option
- the low-expression option
- the low-commitment option when no stronger line is available
- the onboarding option used to teach the system before authored Techniques become the real play language

Techniques should usually be:

- the identity-bearing option
- the tactically richer option
- the main vehicle for expressing personal build decisions without relying on fixed class structure

If a proposed Technique is only a renamed base action with minor numerical tuning, it has probably failed its authoring goal.

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

## Authoring Order

The full Technique skeleton exists for:

- storage
- QA
- consistency
- balance review

It should **not** dictate the creative order in which a Technique is conceived.

If authors begin by filling fields mechanically, the result can become formulaic even if the framework itself is sound.

### Recommended order

When creating a Technique, start in this order:

1. **Identity**
   - What is the memorable trained expression here?
   - Why would a player want this Technique specifically?
2. **Scene function**
   - What does it actually change in exploration or combat?
   - What moment is it for?
3. **Primary interaction**
   - What real system surface does it mainly touch?
4. **Secondary interaction**
   - What second system surface naturally follows from the same fiction?
5. **Restrictions and cost**
   - Why can't this be used freely all the time?
6. **Formal fields**
   - Only after the above, fill `trigger`, `range`, `area`, `duration`, `saving_roll`, `requirements`, and the rest

### Important principle

The skeleton should capture the Technique after its identity is clear.

It should not replace:

- voice
- fantasy
- trained cause
- dramatic role

If a Technique only exists because its fields can be filled cleanly, it is probably not ready yet.

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

### Rhythm authoring standard

Technique `rhythm_cost` should be calibrated **against** the existing ATB anchor bands:

- `0` free
- `3` quick
- `5` standard
- `7` heavy
- `9` extreme

These are **anchor values**, not the only legal values.

Intermediate values such as:

- `1`
- `2`
- `4`
- `6`
- `8`

are valid when a Technique needs finer timing calibration between the base anchors.

This is **not** a damage table and should not be treated like one rigidly.

Rhythm measures:

- how much tactical time the Technique occupies
- how much commitment or recovery it creates
- how large its timing permission is inside the ATB flow

It should be judged by scene function, not by flavor intensity alone.

### Rhythm range rule

For authored Techniques, treat `0` to `9` as the normal design range.

Inside that range:

- anchors communicate broad timing identity
- intermediate values communicate finer distinctions inside the same timing family

Examples:

- `2` may sit between almost-free and fully quick
- `4` may sit between quick and standard
- `6` may sit between standard and heavy
- `8` may sit between heavy and extreme

Do not use an intermediate value just to fake precision.
Use it only when the Technique clearly lands between two anchors in actual play feel.

#### Rhythm 0 — Free

Use only when the Technique:

- is passive, always-on, or extremely constrained
- does not meaningfully consume timing in the current exchange
- does not create strong new permission by itself

This should be rare.

If a Technique creates a meaningful reactive or offensive event, it should almost never be `0`.

#### Rhythm 3 — Quick anchor

Use when the Technique is:

- brief and sharply bounded
- usually instant
- tied to a narrow trigger or precise moment
- built around one main surface
- not strongly persistent

Typical examples:

- tight reactive answers
- short setup conversions
- brief entry denial
- small defensive spoils

Avoid the quick band if the Technique also:

- creates broad control
- strongly alters position or lane state beyond the immediate moment
- adds significant follow-up leverage
- persists in time
- carries multiple major surfaces

#### Rhythm 5 — Standard anchor

Use when the Technique is:

- a normal committed authored action
- broader than a quick answer
- allowed to carry one strong surface and one meaningful secondary surface
- clearly more than a narrow interruption

Typical examples:

- authored offensive Techniques
- reliable setup-to-effect conversions
- conditional repositioning or disruption
- standard active utility under pressure

`5` is the default anchor for Techniques that matter but do not require extreme commitment.

#### Rhythm 7 — Heavy anchor

Use when the Technique:

- demands real bodily, tactical, or positional commitment
- creates serious control, denial, or disruption
- carries multiple coherent pressure surfaces
- opens major leverage if it lands
- occupies a large window in the exchange

Typical examples:

- hard commitment attacks
- strong protected interventions
- significant lane or target control
- large disruption with follow-through consequences

If the Technique feels like the user is betting a visible chunk of tempo on one meaningful move, `7` is often appropriate.

#### Rhythm 9 — Extreme anchor

Use only when the Technique is:

- rare
- highly permissioned
- encounter-shaping
- clearly above normal authored actions

Typical examples:

- major scene-turning expressions
- rare upper-tier Techniques
- actions whose timing cost must be felt immediately as exceptional commitment

This band should remain uncommon and should usually come with high rank, strong restrictions, or both.

### Attrition authoring standard

Technique `attrition_cost` should be calibrated **against** the existing functional demand anchors:

- `0` trivial or negligible demand
- `1` standard meaningful demand
- `2` high demand
- `3` extreme overextension

These are **anchor values**, not a hard cap.

Higher values such as:

- `4`
- `5`
- or more

are valid when a Technique should push projected Fatigue much faster than the base authored scale.

Attrition does **not** mean:

- physical exertion only
- damage taken
- "heavy weapon tax"

Attrition measures how much strain the Technique creates across body, mind, and composure while performed under real pressure.

### Attrition range rule

For normal authored Techniques, `0` to `3` is the main working band.

However, unlike the base action layer, authored Techniques may exceed that range when needed.

Use `Attrition > 3` only when the Technique:

- clearly exceeds ordinary operating margin
- is meant to feel unsafe to repeat immediately
- should accelerate projected Fatigue as a defining balancing factor
- belongs to a rare, desperate, heroic, or upper-tier expression

If a Technique uses `Attrition > 3`, the burden of justification is high and the effect should visibly earn it.

#### Attrition 0 — Trivial or negligible demand

Use only when the Technique:

- is passive
- creates no meaningful active strain
- or is so tightly bounded that the scene cost is effectively negligible

If a Technique is an authored active move that changes the scene, `0` should be uncommon.

#### Attrition 1 — Standard meaningful demand

Use when the Technique:

- is a normal meaningful action under pressure
- does not push the user beyond ordinary operating margin
- asks for focus, control, or effort, but not severe strain

This should be the baseline for many authored Techniques, including many `Rhythm 3` and `Rhythm 5` Techniques.

#### Attrition 2 — High demand

Use when the Technique:

- absorbs serious pressure
- protects, intercepts, or commits the body heavily
- forces difficult processing under immediate threat
- meaningfully bends the rhythm of the scene
- remains clearly above normal sustainable effort

This is appropriate for Techniques that should feel expensive to repeat even if their `rhythm_cost` is not maximal.

#### Attrition 3 — Extreme overextension anchor

Use only when the Technique:

- goes beyond the user's normal safe operating margin
- represents heroic intervention, limit effort, or severe overcommitment
- should accelerate projected Fatigue very aggressively

This should stay rare and should usually belong to upper-tier Techniques or clearly desperate uses.

Values above `3` represent overextension beyond the base authored anchor scale and should be treated as exceptional, not routine.

### Rhythm and Attrition are related, but separate

Do not assume:

- high Rhythm always means high Attrition
- low Rhythm always means low Attrition

A Technique may be:

- quick but demanding
- slow but mechanically sustainable
- rhythm-heavy because of commitment, not because of strain
- strain-heavy because of pressure absorption, not because of long execution time

### Cost assignment rule

When assigning `rhythm_cost` and `attrition_cost`, use this order:

1. What timing permission does the Technique occupy or create?
2. How much commitment or recovery should that timing imply?
3. How much real strain does the Technique impose if used under pressure?
4. Does the Technique's trigger, restriction set, or counterplay reduce what it should cost?

### Escalation rule

Raise cost when a Technique adds one or more of the following without strong compensation:

- broad or reliable reactive access
- lane or position denial
- persistent pressure
- multiple major interaction surfaces
- strong follow-up conversion
- major protection or mitigation
- rhythm or Attrition manipulation

Typical escalation patterns:

- narrow one-surface reactive Technique: often `Rhythm 3 / Attrition 1`
- standard authored Technique with one strong surface and one secondary surface: often `Rhythm 5 / Attrition 1`
- strong intervention, serious denial, or multi-surface committed Technique: often `Rhythm 7 / Attrition 2`
- rare upper-tier overextensions: often include `Rhythm 9`, `Attrition 3+`, or both

### Calibration rule

If a Technique looks correct in fiction but its cost is uncertain, default to the more conservative band during first-pass authoring.

Then review it against:

- tier
- trigger width
- repetition risk
- counterplay
- how early projected Fatigue should appear in the intended scene

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

## Pilot Technique Example

The following Technique is a **pilot example** used to validate the current authoring path.

It is not meant to imply that the final catalog should be written inline in this document. Its purpose is to test whether the framework produces a Technique that is:

- thematically clear
- mechanically distinct from a base attack
- properly rooted in a combat profile
- legible at the table

### Cerrar la Línea

| Field | Value |
| --- | --- |
| `name` | Cerrar la Línea |
| `name_en` | Close the Line |
| `origin` | Spear |
| `category` | attack |
| `type` | reactive |
| `trigger` | An enemy advances into your line or tries to convert forward movement into immediate melee contact against you. |
| `requirements` | Minimum rank: Novice; weapon profile: Perforation; equipment: a spear or other weapon that credibly sustains a committed piercing line |
| `target` | enemy |
| `range` | weapon reach |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 4; Attrition 1 |
| `saving_roll` | contextual — resolved through the hostile exchange that the Technique intercepts |
| `tags` | attack, pressure, precision, setup |

**Fantasy:** The user does not win by hitting harder, but by making entry itself unsafe. The point arrives where the enemy must pass, turning committed forward motion into a liability.

**Why this is not a base attack:** A base spear attack is a generic offensive action. `Cerrar la Línea` exists to solve a specific combat moment: hostile entry into your line. Its identity is not "attack, but slightly better." Its identity is "deny clean entry through exact forward authority."

**Primary interaction surface:** position and lane ownership.

**Secondary interaction surface:** timing pressure inside ATB, because the Technique punishes a movement window rather than waiting for a generic turn trade.

**Cost note:** `Rhythm 4 / Attrition 1` is intentional. `Cerrar la Línea` is narrower than a standard authored Technique, but stronger than a pure quick reactive strike because it also denies clean entry conversion on success. It sits between the `3` quick anchor and the `5` standard anchor.

**Effect:** Make a reactive attack against the triggering enemy. If the Technique resolves successfully, that enemy does not complete a clean melee entry against you through the same forward commitment. The hostile advance still happened, but it fails to convert into an immediate clean offensive contact window against your position.

**Restrictions:**

- requires a clear line and enough space to present the point properly
- cannot be used if the enemy is already established at very close range
- should not function while the user is fully compromised, surrounded, or unable to align the weapon

**Authoring note:** This is a good pilot because it validates the intended rule that Techniques should differentiate play through moment-specific tactical identity, not through flat improvement to a universal action.

### Recuperar la Distancia

| Field | Value |
| --- | --- |
| `name` | Recuperar la Distancia |
| `name_en` | Recover the Distance |
| `origin` | Spear |
| `category` | attack |
| `type` | active |
| `trigger` | Your line is being contested, compressed, or threatened by an enemy preparing to enter or remain in close pressure. |
| `requirements` | Minimum rank: Novice; weapon profile: Perforation; equipment: a spear or other weapon that credibly sustains a committed piercing line |
| `target` | enemy |
| `range` | weapon reach |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 1 |
| `saving_roll` | contextual — resolved through the hostile exchange created by the thrust |
| `tags` | attack, pressure, setup, precision |

**Fantasy:** The user does not wait for the enemy to cross the line. They drive the point forward with enough authority to reclaim the distance on their own turn, re-establishing the spear's preferred geometry before close pressure settles.

**Why this is not a base attack:** A base spear attack simply strikes. `Recuperar la Distancia` is specifically about restoring the weapon's ideal fighting space when the line is being compressed. It is not generic offense. It is active reassertion of reach discipline through committed forward control.

**Primary interaction surface:** position and lane state.

**Secondary interaction surface:** setup conversion, because the Technique restores a cleaner line for the spear user instead of only resolving one hostile moment.

**Cost note:** `Rhythm 5 / Attrition 1` is intentional. The Technique is broader than `Cerrar la Línea` because it is not tied to a single narrow reactive window and it actively tries to reclaim the encounter geometry, so its main increase is in timing commitment. At `Novice`, it does not yet need to punish repetition through heavier strain.

**Effect:** Make an active attack against the target. If the Technique resolves successfully, the target does not remain in a clean close-pressure position against you at the end of that exchange. The exact fiction may be a forced hesitation, a checked step, a spoiled commitment, or a defensive recoil, but the result is the same: you re-establish a cleaner spear line instead of merely trading one hit.

**Restrictions:**

- requires enough space to drive the point and body alignment forward
- should not function in conditions where the spear cannot credibly recover line geometry
- should not grant broad zone control or multi-target denial by itself

**Comparison note:** `Cerrar la Línea` is a narrower reactive denial and now sits at `4 / 1`. `Recuperar la Distancia` is a broader active reclaiming action and sits at `5 / 1`. The difference isolates timing commitment first, without forcing a higher strain cost at the same novice tier.

### Clavar el Paso

| Field | Value |
| --- | --- |
| `name` | Clavar el Paso |
| `name_en` | Pin the Step |
| `origin` | Spear |
| `category` | attack |
| `type` | active |
| `trigger` | An enemy is already pressing the line or is about to force a committed close entry that you want to stop through sheer forward authority. |
| `requirements` | Minimum rank: Novice; weapon profile: Perforation; equipment: a spear or other weapon that credibly sustains a committed piercing line |
| `target` | enemy |
| `range` | weapon reach |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 2 |
| `saving_roll` | contextual — resolved through the hostile exchange created by the committed thrust |
| `tags` | attack, pressure, precision, disruption |

**Fantasy:** The user does not merely reassert spacing. They drive the spear with enough commitment that the enemy's next step becomes unsafe to complete. This is not patient reach discipline. It is a forceful line claim that spends the body to stop the step before it settles.

**Why this is not a base attack:** A base spear attack threatens or wounds. `Clavar el Paso` is specifically about making the enemy's forward step fail as a stable offensive commitment. Its identity is not raw damage. Its identity is committed denial through body-forward piercing authority.

**Primary interaction surface:** position and lane denial.

**Secondary interaction surface:** disruption, because the Technique is trying to spoil the enemy's forward commitment rather than simply trade one clean strike.

**Cost note:** `Rhythm 5 / Attrition 2` is intentional. Its timing is still in the standard active band, but its strain rises because the user is not just acting on their turn. They are forcefully contesting the enemy's step with visible bodily commitment, harsher pressure handling, and a worse margin for repeated safe use.

**Effect:** Make an active attack against the target. If the Technique resolves successfully, the target's current forward step or immediate close-entry attempt does not settle into a stable offensive position against you. The enemy may still remain present, but their step is checked, spoiled, or forced into hesitation rather than becoming a clean close-pressure state.

**Restrictions:**

- requires enough space and posture to drive the spear with committed alignment
- should not function as broad zone control or as a free answer to multiple enemies
- should leave the user meaningfully committed if the exchange goes poorly

**Comparison note:** `Recuperar la Distancia` at `5 / 1` restores geometry with cleaner economy. `Clavar el Paso` stays at the same timing band but rises to `Attrition 2` because it buys its denial through harsher bodily expenditure and lower repetition safety.

---

## Next Design Layer

This document defines the Technique skeleton.

The next required layer is:

- **competency technique domains**

That layer defines what kinds of Techniques each competency is structurally suited to produce.

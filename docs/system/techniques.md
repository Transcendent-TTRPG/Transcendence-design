# Techniques

**Authority data:** `data/system/techniques.yaml`
**Related ADR:** `docs/adr/system-abilities-and-specializations.md`
**Related docs:** `docs/system/competencies.md`, `docs/system/specializations.md`, `docs/system/roll-types.md`, `docs/system/atb-reference.md`, `docs/system/attrition-fatigue.md`, `docs/system/weapon-technique-profiles.md`, `docs/system/ailments.md`

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
| `origin` | Which competency or competencies make it executable |
| `world_origin` | Why the Technique exists in the world: primary front, source, seed, transmission, and availability |
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

## Origin, World Origin, and Requirements

Every Technique must name both:

- `origin` — the competency, equipment, profile, or hybrid root that makes the Technique executable
- `world_origin` — the lore source that explains why the Technique exists and how it is transmitted

`origin` may be:

- one competency
- two competencies
- a main competency plus an equipment condition
- a main competency plus a state condition

`world_origin` should include:

- `primary_front`: Species, Doctrine, or Region
- `secondary_front`: optional
- `source`: the people, doctrine, order, region, or tradition that created it
- `seed`: the concept, pressure, doctrine, or regional need that generated it
- `transmission`: how the method is passed on
- `availability`: Common, Restricted, Secret, Sacred, or Lost

The two fields must not be collapsed.

Example:

- `origin`: Spear
- `world_origin`: Species / Naghii / Threshold Denial / archive guard spear drills / Restricted

This means the character needs the spear competency to execute the Technique, but the Technique exists because Naghii archive-guard practice developed that method.

Species-origin Techniques are not automatically species-locked.

If a Technique originated from a natural weapon, anatomy, sensory habit, venom, shell, horn, tail, or similar biological surface, the Technique should still define what a non-member needs in order to perform an analogous method: a manufactured weapon, prepared ammunition, kit delivery, tool, apparatus, training analogue, or environmental setup.

The species origin explains why the Technique exists. The requirements explain what the current user needs to execute it.

Only mark a species-origin Technique as biologically exclusive when that exclusivity is intentional and no credible non-magical substitute exists.

### Condition authoring rule

If a Technique naturally applies a condition, Alteration, Affliction, Poison, Curse, or other Ailment that does not yet exist, do not force the Technique into the closest existing condition by default.

Instead:

- check `docs/system/ailments.md` and `data/system/ailments.yaml`
- decide whether the missing state is broadly useful enough to become a generic system Ailment
- if it is, define it with a neutral system name, not a species-flavored name
- then reference that Ailment from the Technique

Species-origin Techniques may explain why the method exists, but the condition name should remain generic if the state can be caused by many sources.

When a Technique applies an Ailment through an `R.R.`, its default scaling should usually increase Ailment severity by competency rank bands:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe

Some Ailments use severity mainly to determine application pressure or recovery difficulty rather than changing the ongoing effect. That is still valid scaling.

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

### Information and reading Techniques

Techniques rooted in Perception, Interpretation, Identification, Tracking, Theology, Astronomy, Cryptology, Archaeology, Architecture, or similar reading domains should normally produce an **actionable information result**.

Good information Technique outputs include:

- reveal one immediate tactical truth
- identify what kind of absence or contradiction matters
- expose the next likely route, state, risk, or pressure
- classify a sign, pattern, creature state, structure, or threat in a bounded way
- rule out an unsafe conclusion

They should not default to being a passive bonus to another roll.

If a reading Technique only grants a bonus, it must be explicitly authored as a `setup` Technique with:

- a clear target roll or action family
- a narrow trigger
- a defined duration or consumption point
- a reason it is not better written as direct information

Otherwise, the Technique should be rewritten so that the read itself changes play.

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
2. What world origin created this method?
3. What seed, doctrine, or regional pressure explains why it exists?
4. Why is this not just raw use of that competency?
5. What direct mechanical change does it create?
6. What timing window does it occupy?
7. What does it cost?
8. How can it be resisted, if at all?
9. How does it end?
10. How does it scale?

If these are not clear, the Technique is still a concept, not an authored rule.

---

## First Authored Technique Examples

The following Techniques are **first authored examples** used to validate the current authoring path.

It is not meant to imply that the final catalog should be written inline in this document. Its purpose is to test whether the framework produces Techniques that are:

- thematically clear
- mechanically distinct from a base attack
- properly rooted in a combat profile
- legible at the table
- grounded in a world origin

### Cerrar la Línea

| Field | Value |
| --- | --- |
| `name` | Cerrar la Línea |
| `name_en` | Close the Line |
| `origin` | Spear |
| `world_origin` | Species: Naghii; seed: Threshold Denial; transmission: archive guard spear drills; availability: Restricted |
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

**World origin:** Naghii archive culture treats crossing a protected threshold as a moment of danger and judgment. In spear practice, that worldview becomes a guard method: the enemy is answered at the instant they try to convert entry into contact.

**Why this is not a base attack:** A base spear attack is a generic offensive action. `Cerrar la Línea` exists to solve a specific combat moment: hostile entry into your line. Its identity is not "attack, but slightly better." Its identity is "deny clean entry through exact forward authority."

**Primary interaction surface:** position and lane ownership.

**Secondary interaction surface:** timing pressure inside ATB, because the Technique punishes a movement window rather than waiting for a generic turn trade.

**Cost note:** `Rhythm 4 / Attrition 1` is intentional. `Cerrar la Línea` is narrower than a standard authored Technique, but stronger than a pure quick reactive strike because it also denies clean entry conversion on success. It sits between the `3` quick anchor and the `5` standard anchor.

**Effect:** Make a reactive attack against the triggering enemy. The point meets the advance before it settles — the enemy absorbs the thrust at the worst moment of their commitment or is forced to abort the entry. If the Technique resolves successfully, the advance does not convert into clean melee contact: the enemy's forward motion ends at the point rather than past it.

**Restrictions:**

- requires a clear line and enough space to present the point properly
- cannot be used if the enemy is already established at very close range
- should not function while the user is fully compromised, surrounded, or unable to align the weapon

**Authoring note:** This is a good pilot because it validates the intended rule that Techniques should differentiate play through moment-specific tactical identity, not through flat improvement to a universal action.

### Cerrar la Compuerta

| Field | Value |
| --- | --- |
| `name` | Cerrar la Compuerta |
| `name_en` | Close the Sluice |
| `origin` | Shield |
| `world_origin` | Species: Sauri; seed: Tail Keeps The Channel / Procession Of Force; transmission: river-warden shield drills and temple gate defense; availability: Restricted |
| `category` | utility |
| `type` | active |
| `trigger` | You set your shield to govern a readable lane, flank, doorway, bridge, corridor, formation gap, or other route before an enemy commits through it. |
| `requirements` | Minimum rank: Novice; weapon profile: Line Control; equipment: shield; user must be able to physically occupy or cover the chosen route with shield reach |
| `target` | route |
| `range` | shield reach |
| `area` | single readable route |
| `duration` | until the next relevant hostile activation resolves, or until you leave the route |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | none |
| `tags` | defense, control, anti_displacement, setup |

**Fantasy:** The user does not wait for the enemy to choose a target. They set the shield like a stone gate in a canal, making one route costly to ignore. The enemy can still force the issue, but no longer treats the protected side as open water.

**World origin:** Sauri river-wardens and temple guards train with the same logic their architects use in canals and sealed chambers: pressure must meet the correct gate before it becomes flood. In shield practice, that doctrine becomes an active claim over the route.

**Why this is not a base shield defense:** A base shield defense protects against a strike after the strike is declared. `Cerrar la Compuerta` changes the route before the strike is chosen. Its purpose is not to block one attack, but to make attacking through or around the shield line a worse decision.

**Primary interaction surface:** position and lane ownership.

**Secondary interaction surface:** target pressure, because enemies can still attack past the user, but doing so through the closed route becomes less efficient.

**Cost note:** `Rhythm 3 / Attrition 1` is intentional. The Technique is an active setup, not a guaranteed interception. It costs little because it does not stop the next attack by itself; it changes the next relevant enemy decision through the chosen route.

**Effect:** Choose one readable route within shield reach. The compuerta remains in place until the next hostile activation that could plausibly use or attack through that route resolves, even if your own marker becomes ready first.

During that window, an enemy that uses the chosen route or attacks through that route against a target other than you treats the action as obstructed by your shield line.

The obstructed action suffers a penalty to its Attack Roll equal to `1 + your Shield rank`. Instead of accepting the penalty, the enemy may choose to attack you or your shield line as the cleaner target.

This does not stop the attack. It makes ignoring the shield line worse.

**Restrictions:**

- requires a real lane, doorway, flank, bridge, corridor, riverbank edge, formation gap, or other readable route to govern
- cannot be used if the user cannot physically occupy or cover the chosen route with shield reach
- does not create a persistent zone by itself
- does not prevent the enemy from attacking through the route; it only penalizes doing so
- ends after the next hostile activation that could plausibly use or attack through the chosen route resolves, whether or not that enemy accepts the penalty
- ends early if the user leaves the route, loses shield posture, takes a non-free action that abandons the shield line, or becomes unable to maintain the shield line
- should not stack with another copy of the same Technique on the same route

**Authoring note:** This Technique is intentionally written so it can also be learned by non-Sauri shield users. The Sauri origin explains why the method exists: they think of movement as pressure through a channel, and the shield as the gate that decides where that pressure is allowed to go.

### Levantar el Dique

| Field | Value |
| --- | --- |
| `name` | Levantar el Dique |
| `name_en` | Raise the Dike |
| `origin` | Shield |
| `world_origin` | Species: Sauri; seed: Vessel Under Pressure / Procession Of Force; transmission: temple escort drills and river-warden protection rites; availability: Restricted |
| `category` | utility |
| `type` | reactive |
| `trigger` | An enemy attack or movement-linked strike would reach an ally, protected creature, carried witness, relic, or designated charge within your shield reach. |
| `requirements` | Minimum rank: Novice; weapon profile: Interception; equipment: shield; user must have a clear physical path to place the shield between the threat and the protected target |
| `target` | ally / creature / object |
| `range` | shield reach |
| `area` | single protected target |
| `duration` | instant |
| `cost` | Rhythm 4; Attrition 1 |
| `saving_roll` | contextual - resolved through the hostile attack or movement-linked strike that the Technique intercepts |
| `tags` | defense, interception, support, mitigation |

**Fantasy:** The user raises the shield before the blow finishes its course, not as a wall for themselves but as a dike for someone or something that must not be reached. The attack still has force, but the force meets the prepared surface instead of the intended target.

**Effect:** Contest the triggering attack or movement-linked strike with a shield response. If the Technique resolves successfully, the attack does not affect its intended target. The shield-bearing user becomes the point of contact for the hostile force; the attack is blocked, redirected, or resolved against the user's shield defense as the scene requires.

If the intercepted attack carries a non-damage rider, such as forced movement, a condition, or a grab, that rider does not transfer automatically to the protected target. The Narrator resolves whether the rider can affect the shield-bearing user based on the fiction of the contact.

**Restrictions:**

- requires a clear physical path for the shield to enter the attack line
- protects one target from one triggering threat only
- cannot intercept effects that do not travel through a blockable line, surface, body, projectile, or contact path
- cannot protect a target already separated from the user by sealed terrain, a closed barrier, or an occupied route the shield cannot cross
- should not become persistent bodyguard coverage without a higher-rank Technique

### Romper el Caudal

| Field | Value |
| --- | --- |
| `name` | Romper el Caudal |
| `name_en` | Break the Flow |
| `origin` | Shield |
| `world_origin` | Species: Sauri; seed: Release At The Correct Gate / Tail Keeps The Channel; transmission: river-warden breach drills and temple guard interruption forms; availability: Restricted |
| `category` | attack |
| `type` | reactive |
| `trigger` | An enemy within shield reach begins a Technique, heavy action, telegraphed action, or movement-linked execution that requires visible commitment before it resolves. |
| `requirements` | Minimum rank: Novice; weapon profile: Interruption; equipment: shield; user must have a ready weapon, natural weapon, or shield item with explicit attack stats to deliver the counter; the enemy's action must have a readable physical line, windup, focus point, or route of execution the shield can strike or jam |
| `target` | enemy |
| `range` | shield reach |
| `area` | single enemy |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 1 |
| `saving_roll` | D.R. contest; counter requires clean defensive margin |
| `tags` | attack, defense, disruption, counter_positioning |

**Fantasy:** The user does not wait behind the shield. They drive the shield into the moment where the enemy's action has begun but has not yet become inevitable. If the current breaks completely against the shield, the user's answering strike lands before the enemy can rebuild the flow.

**Effect:** Contest the triggering execution with a shield-based `D.R.`. If the enemy's attack or execution still beats your `D.R.`, the Technique fails and the enemy resolves normally.

If your `D.R.` equals or exceeds the enemy's relevant attack or execution roll, the shield breaks the execution cleanly. The enemy's action still consumes its declared Rhythm and any declared cost, but it does not damage you through that contact.

If your `D.R.` exceeds the enemy's roll by **3 or more**, you may immediately make one counterattack against that enemy with one ready manufactured weapon, one natural weapon, or a shield item that has explicit attack stats. Resolve the counterattack normally with its own `A.R.` and `I.R.`. This counterattack does not add another Rhythm cost, but it cannot include movement, a second Technique, or a follow-up window.

If the triggering action was a telegraphed action rather than a direct attack, the Narrator uses the same margin logic against the action's relevant execution roll, fixed threat value, or declared interruption threshold. If no such value exists, this Technique can spoil the setup but cannot produce the counterattack.

**Restrictions:**

- requires a readable committed execution; cannot be used against trivial, instant, hidden, or purely mental actions with no blockable line
- requires shield reach and a credible contact point to jam, strike, or break
- counterattack requires a ready weapon, natural weapon, or shield item with explicit attack stats
- affects one enemy action only
- should not cancel an entire boss or champion subsystem unless that subsystem explicitly exposes a vulnerable interruption window
- shield-only damage should not be assumed unless shields later receive explicit offensive stats or the specific shield item says it can attack

### Asentar la Piedra

| Field | Value |
| --- | --- |
| `name` | Asentar la Piedra |
| `name_en` | Settle the Stone |
| `origin` | Shield |
| `world_origin` | Species: Sauri; seed: Vessel Under Pressure / Sovereign Weight; transmission: temple bastion stances and sovereign guard anchoring rites; availability: Restricted |
| `category` | utility |
| `type` | active stance |
| `trigger` | You plant yourself with a shield to hold a point, line, doorway, flank, formation gap, or protected space. |
| `requirements` | Minimum rank: Novice; weapon profile: Bastion; equipment: shield; user must be standing, able to brace, and able to keep the shield oriented toward the pressure being held |
| `target` | self |
| `range` | self |
| `area` | anchored point |
| `duration` | sustained while anchored |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | none |
| `tags` | defense, stability, mitigation, anti_displacement |

**Fantasy:** The user settles into the ground like fitted stone. They are not doing nothing. They are making one place harder to take from them.

**Effect:** Choose the point or small space you are anchoring. While the stance remains active, you gain a bonus equal to your Shield rank to:

- `D.R.` against attacks that come through your shield line or the anchored front
- `R.R.` against forced movement, knockdown, shove, drag, destabilization, crushing pressure, and physical Alterations caused by impact or bodily displacement

You may still attack, use Techniques, intercept, speak, pressure enemies, and defend while the stance is active, as long as those actions do not make you abandon the anchored point or break shield posture.

**Restrictions:**

- ends if you voluntarily move more than 1 meter from the anchored point
- ends if forced movement, knockdown, loss of footing, or another effect breaks your posture
- ends if you turn the shield away from the pressure being held or no longer have the shield ready
- does not apply against poison, fear, curses, sensory effects, mental influence, or Alterations not caused by physical impact/displacement
- does not create a protected route by itself; use `Cerrar la Compuerta` for route pressure
- does not intercept attacks against others by itself; use `Levantar el Dique` for interception

### Cerrar el Juicio

| Field | Value |
| --- | --- |
| `name` | Cerrar el Juicio |
| `name_en` | Close the Judgment |
| `origin` | Impact |
| `world_origin` | Species: Sauri; seed: Jaw As Judgment / Vessel Under Pressure; transmission: jaw-closing rites, execution drills, and temple predator discipline; availability: Restricted |
| `category` | attack |
| `type` | active |
| `trigger` | You make a committed Impact-profile attack against a declared breakable target within reach. |
| `requirements` | Minimum rank: Novice; weapon profile: Impact; equipment or anatomy: Sauri bite, mace, heavy blunt weapon, or another credible Impact surface capable of closing force into the target |
| `target` | enemy |
| `range` | weapon or natural weapon reach |
| `area` | single enemy |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 2 |
| `saving_roll` | D.R. resolves normally against the attack |
| `tags` | attack, pressure, disruption, setup |

**Fantasy:** The user does not strike and withdraw. They close force into the target like a verdict. Whether the surface is jaw, mace, or another heavy Impact tool, the blow does not merely hurt flesh; it asks whether the struck structure can remain whole.

**Effect:** Before rolling, declare one breakable target that your attack can plausibly reach: a weapon, shield, armor piece, carried object, exposed natural armor, limb, jaw, horn, shell edge, tail segment, or other creature part the encounter has made targetable.

Make an active Impact-profile attack against that target. Resolve damage normally if the attack hits.

For this attack only, reduce the Impact Roll result needed to validate a break by `1` per rank in the competency used for the attack.

Example: if the attack uses a `d12` Impact die and break validation normally occurs only on `12`, a rank 3 user validates break on `9-12` while using this Technique.

If the Impact Roll lands inside that expanded break-validation range, resolve the break validation using the target's Durability and the Breaking Parts formula:

`Critical Potency > target Durability`

This Technique does not increase Potency; it only expands the Impact die results that permit break validation.

**Restrictions:**

- requires a valid Impact-profile surface and a target with a body or structure the impact can meaningfully affect
- the breakable target must be declared before the attack roll
- cannot target an abstract creature as a whole; it must target a piece, object, exposed body part, natural armor section, or defined vital point
- cannot force break validation on purely soft tissue unless that creature part has been established as a targetable structure or vital point
- does not increase Potency by itself; it only expands the Impact Roll range that permits break validation
- does not create a grapple, restraint, or sustained hold by itself
- should not replace dedicated called-shot or vital-point rules once those are formally defined

### Abrir la Vasija

| Field | Value |
| --- | --- |
| `name` | Abrir la Vasija |
| `name_en` | Open the Vessel |
| `origin` | Rend |
| `world_origin` | Species: Sauri; seed: Jaw As Judgment / Vessel Under Pressure; transmission: predator restraint drills, execution tearing rites, and wound-reading practice; availability: Restricted |
| `category` | attack |
| `type` | active |
| `trigger` | You make a committed Rend-profile attack against a target with flesh, hide, natural armor, bindings, or worn protection that can be torn open. |
| `requirements` | Minimum rank: Novice; weapon profile: Rend; equipment or anatomy: Sauri bite, axe, hooked blade, serrated natural weapon, tearing edge, or another credible Rend surface capable of opening and worsening a contact wound |
| `target` | enemy |
| `range` | weapon or natural weapon reach |
| `area` | single enemy |
| `duration` | until Lacerado is removed |
| `cost` | Rhythm 5; Attrition 2 |
| `saving_roll` | On hit, the target makes an Alteration Resistance Roll against Lacerado |
| `tags` | attack, pressure, disruption, wound_pressure |

**Fantasy:** The user does not simply cut. They open the target like a vessel under pressure. The wound is not important because it bleeds prettily; it matters because movement, effort, and resistance now have to pass through damaged material.

**World origin:** Sauri predator discipline treats a closed jaw as a decision, but `Abrir la Vasija` is the lesson that follows: once the vessel opens, every careless motion spills something. Executioners, hunters, and wound-readers learn to make the body account for the opening.

**Why this is not a base Rend attack:** A base Rend attack tears and damages. `Abrir la Vasija` creates tactical wound pressure through `Lacerado`: the target must respect the opened contact instead of treating the hit as damage only. It is not a permanent bleed engine, and it does not stack repeated damage just because the user keeps pressing the same button.

**Primary interaction surface:** wound pressure.

**Secondary interaction surface:** Rhythm pressure through wound-stressed physical actions.

**Cost note:** `Rhythm 5 / Attrition 2` is intentional. The Technique is a committed tearing attack that asks the user to maintain contact angle and follow-through long enough to open a meaningful wound. It should cost more than a normal strike because the reward is a future decision forced onto the target.

**Effect:** Make an active Rend-profile attack against the target. If the attack hits, resolve damage normally. Then the target makes an Alteration Resistance Roll against `Lacerado`.

The `Lacerado` severity is determined by the competency rank used for the attack:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe
- Higher ranks continue this progression if the system later defines higher severity bands.

On a failed R.R., the target gains `Lacerado` at that severity.

While `Lacerado` is active, strenuous physical actions that stress the wound cost additional Rhythm according to severity:

- Minor: `+1` Rhythm
- Moderate: `+2` Rhythm
- Severe: `+3` Rhythm

Strenuous physical actions include attacks, movement bursts, weapon Techniques, forced movement attempts, grapples, heavy defenses, or similar actions that clearly put pressure through the opened wound.

`Lacerado` ends when the target spends a suitable action to bind, brace, close, harden, or otherwise stabilize the wound pressure; when treatment removes it; or when the wound is no longer functionally stressed by the scene.

On a successful R.R., `Lacerado` is not applied, but the attack still resolves its normal damage if it hit.

**Restrictions:**

- requires a valid Rend-profile surface and a target with material, flesh, protection, binding, hide, or natural armor that can be meaningfully torn
- does not apply to targets without a credible tearable body or structure
- applies `Lacerado`, a generic Alteration, not a Sauri-only condition
- cannot stack multiple copies of `Lacerado` on the same target; a stronger application replaces a weaker one, and an equal application usually refreshes persistence
- does not create ongoing automatic damage by itself
- does not bypass armor or Durability unless the attack already has rules that allow that
- should not replace formal bleeding, wound, or injury subsystems if those are later defined

**Authoring note:** This Technique is Sauri-origin but not Sauri-locked. Sauri bite explains the vessel logic, while axes, hooked blades, serrated natural weapons, and tearing tools reproduce the same method through edge, hook, and follow-through. It should feel like forcing the enemy to respect the wound, not like adding another flat damage rider.

### La Corriente No Retrocede

| Field | Value |
| --- | --- |
| `name` | La Corriente No Retrocede |
| `name_en` | The Current Does Not Recede |
| `origin` | Unstoppable |
| `world_origin` | Species: Sauri; seed: Release At The Correct Gate / Jaw As Judgment; transmission: breach rites, mace processions, and jaw commitment drills; availability: Restricted |
| `category` | attack |
| `type` | active |
| `trigger` | You make a committed Unstoppable-profile attack against an enemy that is guarding, bracing, blocking, or trying to hold a defensive line. |
| `requirements` | Minimum rank: Novice; weapon profile: Unstoppable; equipment or anatomy: Sauri bite, mace, heavy blunt weapon, or another credible Unstoppable surface capable of carrying force through resistance |
| `target` | enemy |
| `range` | weapon or natural weapon reach |
| `area` | single enemy |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 2 |
| `saving_roll` | On hit, the target makes an Alteration Resistance Roll against the forced displacement severity |
| `tags` | attack, pressure, forced_movement, posture_break |

**Fantasy:** The user commits force like released water through a gate. The target can meet it, but cannot make it disappear by merely bracing. If the attack lands cleanly, the defensive line gives ground.

**World origin:** Sauri doctrine treats release as dangerous because stored pressure must go somewhere. Mace carriers and jaw-trained executioners learn to commit through the first answer rather than recoil from it. The lesson is simple: once the gate opens, the current does not apologize.

**Why this is not a base Unstoppable attack:** A base heavy attack tries to overpower the target. `La Corriente No Retrocede` specifically attacks a held defense. It does not reward hitting an open target; it rewards choosing the moment when the enemy believes a guard, block, brace, shield, active armor posture, or held line is enough.

**Primary interaction surface:** defensive-line pressure.

**Secondary interaction surface:** posture breaking.

**Cost note:** `Rhythm 5 / Attrition 2` is intentional. The Technique does not add movement or create a persistent state, but it asks the user to commit force through resistance. The higher Attrition reflects body commitment against a prepared answer.

**Effect:** Make an active Unstoppable-profile attack against the target.

If the target is not guarding, bracing, blocking, holding a line, using a shield defense, using an active armor posture, or otherwise relying on a defensive posture, resolve the attack as a normal hit with no additional effect.

If the target is relying on a defensive posture and the attack hits, the target must make an Alteration Resistance Roll against forced displacement.

The forced displacement severity and distance are determined by the competency rank used for the attack:

- Ranks 1-2: Minor; pushed up to 1 meter
- Ranks 3-4: Moderate; pushed up to 2 meters
- Ranks 5-6: Severe; pushed up to 3 meters
- Higher ranks continue this progression if the system later defines higher severity bands.

On a failed R.R., the target is pushed away from the held line according to the distance above. If that displacement happens, the target also loses the benefit of any active guard, brace, stance, shield-line effect, active armor posture, or similar posture effect that depended on holding that position.

On a successful R.R., the target holds its position and keeps its posture benefits, but the attack still resolves its normal damage if it hit.

**Restrictions:**

- requires a valid Unstoppable-profile surface and enough space or contact logic to carry force through resistance
- only creates its additional effect against a target relying on a defensive posture, held line, shield, guard, brace, active armor posture, or similar resistance
- cannot push a target through a solid barrier or into an impossible position
- cannot remove passive armor values or permanent equipment benefits
- should not cancel boss/champion defensive subsystems unless that subsystem exposes a normal guard, brace, or posture layer the Technique can attack

**Authoring note:** This Technique is Sauri-origin but not Sauri-locked. Sauri bite explains closure through living force; maces and heavy weapons reproduce the same doctrine through mass and follow-through. The Technique should feel like breaking trust in a defense, not like generic bonus damage.

**System note:** This Technique assumes the system should eventually formalize `stance` / `posture` as a Technique type or state category distinct from generic active utility. This would let effects like `La Corriente No Retrocede` cleanly identify what they can break without touching passive armor, permanent equipment values, or unrelated defensive bonuses.

### Recuperar la Distancia

| Field | Value |
| --- | --- |
| `name` | Recuperar la Distancia |
| `name_en` | Recover the Distance |
| `origin` | Spear |
| `world_origin` | Species: Naghii; seed: Preserved Distance; transmission: archive guard range discipline; availability: Restricted |
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

**World origin:** Naghii technique traditions treat proper distance as a condition for reading, control, and safe response. This method restores the distance where the user can interpret the threat before it becomes uncontrolled contact.

**Why this is not a base attack:** A base spear attack simply strikes. `Recuperar la Distancia` is specifically about restoring the weapon's ideal fighting space when the line is being compressed. It is not generic offense. It is active reassertion of reach discipline through committed forward control.

**Primary interaction surface:** position and lane state.

**Secondary interaction surface:** setup conversion, because the Technique restores a cleaner line for the spear user instead of only resolving one hostile moment.

**Cost note:** `Rhythm 5 / Attrition 1` is intentional. The Technique is broader than `Cerrar la Línea` because it is not tied to a single narrow reactive window and it actively tries to reclaim the encounter geometry, so its main increase is in timing commitment. At `Novice`, it does not yet need to punish repetition through heavier strain.

**Effect:** Make an active attack against the target. The thrust and the step are one committed action — you drive the point to cover your own displacement as you move approximately 1 meter in any direction to re-establish your spear's preferred reach. If the Technique resolves successfully, the repositioning completes without yielding a reaction opportunity: the target is now outside close-pressure range and must spend movement to close again before they can threaten you in melee.

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
| `world_origin` | Species: Naghii; seed: Committed Compression; transmission: Kha enforcement and breach-response drills; availability: Restricted |
| `category` | attack |
| `type` | active |
| `trigger` | You want to close distance and attack in a single committed action, pressing into the enemy's space without spending a separate movement action first. |
| `requirements` | Minimum rank: Novice; weapon profile: Perforation; equipment: a spear or other weapon that credibly sustains a committed piercing line |
| `target` | enemy |
| `range` | weapon reach |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 2 |
| `saving_roll` | contextual — resolved through the hostile exchange created by the committed thrust |
| `tags` | attack, pressure, precision, disruption |

**Fantasy:** The user does not wait for the enemy to be in range. They close the gap and attack in one explosive committed action, pressing into the enemy's space before the moment resolves into a standard exchange.

**World origin:** This is the Naghii answer for the moment when waiting becomes more dangerous than commitment. It is especially associated with Kha enforcement and archive breach response: observation ends, the interval collapses, and the user accepts the cost of being committed forward.

**Why this is not a base attack:** A base spear attack assumes you are already in range. `Clavar el Paso` is specifically about compressing movement and attack into a single action — closing up to 2 meters and striking from the new position without the delay or telegraph of a separate movement. Its identity is aggressive range compression at body cost.

**Primary interaction surface:** range and position — the Technique collapses the gap between the user and the target in one committed action.

**Secondary interaction surface:** timing, because the compressed action is harder to react to than a telegraphed move-then-attack sequence.

**Cost note:** `Rhythm 5 / Attrition 2` is intentional. The Technique packages movement and attack into a single action, which justifies the higher strain. The 2-meter close combined with the spear's 2-meter reach means the effective threat range is up to 4 meters — that disguised reach is part of the Technique's tactical value and part of why the body cost is real.

**Effect:** Close up to 2 meters toward the target as part of this action — no separate movement action required — then make an active attack from your new position at full weapon reach. You are left committed forward after the exchange.

**Restrictions:**

- requires enough space and posture to drive the spear with committed alignment
- should not function as broad zone control or as a free answer to multiple enemies
- should leave the user meaningfully committed if the exchange goes poorly

**Comparison note:** `Recuperar la Distancia` at `5 / 1` moves the user back to re-establish distance. `Clavar el Paso` stays at the same timing band but moves the user forward and packs movement into the attack — that combined action is what pushes the strain to `Attrition 2`.

### Anudar el Paso

| Field | Value |
| --- | --- |
| `name` | Anudar el Paso |
| `name_en` | Knot the Step |
| `origin` | Flexible Weapons |
| `world_origin` | Species: Naghii; seed: Coiled Readiness; transmission: temple guard torsion drills; availability: Common |
| `category` | utility |
| `type` | reactive |
| `trigger` | An enemy already inside your flexible reach tries to withdraw, circle to a better angle, disengage from a contested position, or turn partial contact into clean separation. |
| `requirements` | Minimum rank: Novice; weapon profile: Torsion; equipment: a flexible weapon, functional tail/tendril, or other credible torsion contact surface |
| `target` | enemy |
| `range` | flexible reach |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 4; Attrition 1 |
| `saving_roll` | contextual — resolved through the hostile movement exchange that the Technique catches |
| `tags` | control, disruption, counter_positioning, setup |

**Fantasy:** The user waits with still, coiled threat. When the opponent tries to leave or improve position after entering the flexible reach, the curve releases and knots the escape route before it becomes clean separation.

**World origin:** Naghii training treats stillness as stored action. In tail and flexible-weapon practice, that becomes a method for punishing premature movement around a guarded body without relying on heavy force or rigid blocking.

**Why this is not a base attack:** A base flexible-weapon attack strikes along an angle. `Anudar el Paso` exists to solve a specific movement moment after the enemy is already inside flexible reach: they try to withdraw, disengage, flank, or turn partial contact into clean position. Its identity is not damage through reach, but denying clean separation through curved contact.

**Primary interaction surface:** counter-positioning and anti-disengagement.

**Secondary interaction surface:** setup, because the target remains in a contested position instead of gaining a clean escape route or superior angle.

**Cost note:** `Rhythm 4 / Attrition 1` is intentional. The Technique is a narrow reactive anti-disengagement window. Unlike `Cerrar la Línea`, it does not stop an enemy from entering; it punishes an enemy who is already inside flexible reach and tries to leave, circle, or cleanly improve position.

**Effect:** Make a reactive Torsion check against the triggering enemy. If the Technique resolves successfully, the flexible contact catches the enemy's step, wrist, weapon line, or lower body before separation completes. The triggering movement does not create clean withdrawal, a clean flank, or a superior angle. The enemy remains in their current contested position or in the nearest position that still leaves them inside the user's flexible reach, and must spend a later movement commitment or action to clear the contact before treating that path as open.

**Restrictions:**

- requires a flexible contact surface that can credibly catch the step or line
- cannot be used against an enemy entering from outside flexible reach
- cannot be used if the user has no credible held contact or coiled threat
- cannot create full immobilization or grappling control by itself
- should not function as broad zone control or multi-target denial

### Robar el Ángulo

| Field | Value |
| --- | --- |
| `name` | Robar el Ángulo |
| `name_en` | Steal the Angle |
| `origin` | Flexible Weapons |
| `world_origin` | Species: Naghii; seed: Controlled Misreading; transmission: tail feint and flexible line drills; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user attacks a creature that can perceive the visible flexible line and is close enough for the user's curve, wrap, or snap to threaten an off-angle contact. |
| `requirements` | Minimum rank: Novice; weapon profile: Unpredictability; equipment: flexible weapon, functional tail/tendril, or other credible flexible false-line surface; target can perceive the visible line; user has space to resolve from a different angle |
| `target` | creature |
| `range` | flexible reach |
| `area` | single |
| `duration` | until the false-line consequence resolves, the target re-centers without answering the user, or immediate exchange tracking ends |
| `cost` | Rhythm 5; Attrition 1 |
| `saving_roll` | contextual — resolved through the hostile exchange created by the false line |
| `tags` | attack, disruption, mobility, false_read |

**Fantasy:** The user shows one curve and resolves through another, making the target answer the visible line while the real contact steals the useful angle.

**World origin:** Naghii politics and combat both teach controlled misreading: if others are reading you, decide what evidence they receive. In tail and flexible-weapon practice, that becomes a visible curve that makes the target defend the wrong path.

**Why this is not a base Flexible Weapons attack:** A base flexible-weapon attack uses reach or angle to strike. `Robar el Ángulo` specifically creates a false read and converts it into either a small positional shift or a spoiled immediate answer. Its identity is not extra damage; it is making the target answer the wrong line.

**Primary interaction surface:** false-line attack.

**Secondary interaction surface:** mobility or disruption, depending on which consequence the user chooses.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique is broader than a narrow reactive catch: it is an active attack that creates either a small positional conversion or a bounded response penalty. It should not be as cheap as a pure quick strike, but it does not carry enough control or persistence to require higher strain.

**Effect:** Make a Flexible Weapons attack or equivalent tail/tendril Technique check against the target. If the Technique resolves successfully, choose one false-line consequence:

- **Steal position:** the user shifts up to 1 meter around the target within flexible reach without provoking a reaction from that target
- **Spoil response:** the target takes a situational penalty equal to the user's Flexible Weapons rank bonus on its next immediate reaction, counterattack, or opposed exchange against the user before it re-centers

| Flexible Weapons rank | Penalty |
| --- | --- |
| Novice | `-1` |
| Adept | `-2` |
| Expert | `-3` |
| Master | `-4` |
| Consummate | `-5` |
| Transcendent | `-6` |

This does not force the target to move, immobilize it, or create broad zone control.

**Restrictions:**

- requires a flexible surface that can present one line and resolve through another
- requires the target to perceive the visible line
- requires space to resolve from a different angle
- applies to one creature only
- choose one false-line consequence only
- does not force target movement
- does not immobilize or grapple by itself
- does not create broad zone control
- does not function against targets that cannot be misled by visible contact geometry

### Leer el Calor del Paso

| Field | Value |
| --- | --- |
| `name` | Leer el Calor del Paso |
| `name_en` | Read the Heat of the Step |
| `origin` | Perception |
| `world_origin` | Species: Naghii; seed: Layered Sensing; transmission: ruin scout trace-reading drills; availability: Common |
| `category` | utility |
| `type` | active |
| `trigger` | The user can observe or sense a living creature's immediate physical signs: heat shift, breath, scent, pressure, vibration, posture, blood, tremor, or movement residue. |
| `requirements` | Minimum rank: Novice; state: living creature present or immediate living trace available |
| `target` | creature |
| `range` | sensory reach |
| `area` | single creature or trace |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | contextual — only if the target is actively masking its state or movement |
| `tags` | utility, counter_read, survival_window |

**Fantasy:** The user reads heat, breath, scent, vibration, posture, and pressure as one living signal. For a moment, the body gives itself away.

**World origin:** Naghii perception treats the visible world as only one layer of evidence. Ruin scouts and archive guards developed this method to read whether a creature is wounded, fleeing, bracing, hiding, or about to move before the sign becomes obvious.

**Why this is not a base Perception check:** A base Perception check notices that something is present. `Leer el Calor del Paso` extracts one immediate truth from layered living signs. Its identity is not "see better"; it is "the body reveals what it is doing right now."

**Primary interaction surface:** immediate tactical information.

**Secondary interaction surface:** counter-read, because the Technique can cut through concealment, darkness, crowding, or misleading posture if living signs remain available.

**Cost note:** `Rhythm 3 / Attrition 1` is intentional under pressure. The Technique takes a quick but focused read and produces information immediately. These costs apply only during ATB or another active-threat scene; in normal exploration, where Rhythm and Attrition are not active costs, the Technique resolves as the user's Perception action. It does not add a bonus to another roll by itself, and it does not sustain a tracking state.

**Effect:** Make a Perception-based Technique check against one living creature or one immediate living trace within sensory reach. On success, the Narrator provides one immediate truth about what the creature is doing or about to do — such as whether the target is moving toward, away from, or around a protected point; whether the target is wounded, exhausted, poisoned, or physically impaired; whether the target is preparing immediate movement, attack, withdrawal, or concealment; or which of several fresh exits or hiding places the living signal most likely continued through. These are examples of the kind of truth this Technique produces, not a closed list: the Narrator chooses whichever truth is most immediately relevant and may provide other truths of the same quality and immediacy that the signs support.

The read is concrete and immediate, but not exhaustive: it does not identify exact statistics, reveal full intention, diagnose precise conditions, or track a target beyond the signs currently present.

**Restrictions:**

- requires a living creature or immediate living trace within sensory reach
- cannot be used without physical signs to read
- reveals one immediate truth only
- does not reveal exact statistics, full intent, or precise condition names
- does not create a bonus to another roll by itself
- does not create persistent tracking or detection
- does not bypass active masking without contextual opposition

### Pesar el Umbral

| Field | Value |
| --- | --- |
| `name` | Pesar el Umbral |
| `name_en` | Weigh the Threshold |
| `origin` | Intimidation |
| `world_origin` | Species: Naghii; seed: Ritualized Access; transmission: gatekeeper challenge protocols; availability: Common |
| `category` | utility |
| `type` | reactive |
| `trigger` | A creature that can perceive the user's challenge and read basic threat attempts to cross a guarded boundary, enter a protected place, push past the user, ignore a stated prohibition, or attack as the way of violating that boundary. |
| `requirements` | Minimum rank: Novice; state: visible boundary or declared prohibition; target can perceive the challenge and read basic threat |
| `target` | creature |
| `range` | line of sight or clear hearing |
| `area` | single |
| `duration` | until the target halts/acknowledges the challenge, completes the challenged action despite the pressure, or the boundary stops mattering |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | opposed `Containment` / `Contención` |
| `tags` | utility, pressure, control, disruption |

**Fantasy:** The user makes the next step feel heavy. A door, line, warning, rank, silence, or held posture becomes a threshold the target must consciously violate rather than casually cross.

**World origin:** Naghii archive society treats access as procedure. Gatekeepers, guards, and priestly examiners developed this method to make improper entry feel immediately consequential before force is required.

**Why this is not a base Intimidation check:** A base Intimidation check applies general pressure. `Pesar el Umbral` is tied to a boundary moment: the target is about to cross, ignore, push past, attack through, or force access. It does not make the target afraid in general; it makes the boundary violation costly right now.

**Primary interaction surface:** pressure on a boundary-violating action.

**Secondary interaction surface:** disruption, because the target may halt or acknowledge the challenge instead of completing the attempted action cleanly.

**Saving roll note:** The target resists with `Containment` / `Contención`. The pressure of the Technique is not about looking calm; it is about keeping the decision intact when the boundary is made threatening. Creatures without formal specializations should use their closest NPC composure/instinct resistance as a Containment equivalent.

**Cost note:** `Rhythm 3 / Attrition 1` is intentional. This is a quick challenge window that creates one immediate choice: stop cleanly or proceed under pressure. These costs apply only during ATB or another active-threat scene; in normal social or exploration scenes, where Rhythm and Attrition are not active costs, the Technique resolves as the user's Intimidation action. It does not physically restrain the target, redirect aggression, or prevent action by itself.

**Effect:** Make an Intimidation-based Technique check against the triggering target. If the Technique resolves successfully, the target must choose before completing the triggering action:

- halt or acknowledge the challenge, ending the current attempt to force access cleanly
- proceed through the challenge and take a situational penalty equal to the user's Intimidation rank bonus on the immediate roll or opposed exchange used to cross the boundary, push past, enter the protected place, attack as the boundary violation, force entry, or ignore the prohibition

| Intimidation rank | Penalty |
| --- | --- |
| Novice | `-1` |
| Adept | `-2` |
| Expert | `-3` |
| Master | `-4` |
| Consummate | `-5` |
| Transcendent | `-6` |

The penalty applies only to the action that violates the challenged boundary. This is not a taunt that forces the target to attack the user or redirect aggression; it pressures the attempted violation.

**Restrictions:**

- requires a visible boundary or declared prohibition
- requires the target to perceive the challenge and read basic threat
- does not work on mindless targets or targets with no relevant self-preservation instinct or social read
- does not force obedience or prevent the target from acting
- does not redirect attacks or force the target to attack the user
- penalty only applies to the immediate boundary-violating action
- cannot be used as a general penalty to all actions in the scene

### Leer la Línea Ausente

| Field | Value |
| --- | --- |
| `name` | Leer la Línea Ausente |
| `name_en` | Read the Absent Line |
| `origin` | Interpretation |
| `world_origin` | Species: Naghii; seed: Absence As Evidence; transmission: outer archive gap-reading drills; availability: Restricted |
| `category` | utility |
| `type` | active |
| `trigger` | The user is examining an incomplete pattern, record, route, ritual, scene, testimony, formation, or sequence where something appears missing, interrupted, removed, or too clean. |
| `requirements` | Minimum rank: Novice; state: incomplete or suspicious pattern present |
| `target` | site |
| `range` | observed evidence |
| `area` | single pattern or scene |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | contextual — only if another creature deliberately falsified, staged, or concealed the absence |
| `tags` | utility, counter_read, pattern_exploitation |

**Fantasy:** The user studies what is not there: a missing mark, a broken step, a silence in testimony, a route with no return trace, a ritual sequence with one gesture absent.

**World origin:** Naghii archive practice is built around incomplete records and damaged translations. This method teaches initiates to treat absence as evidence without filling it too quickly.

**Why this is not a base Interpretation check:** A base Interpretation check tries to understand what the evidence means. `Leer la Línea Ausente` identifies what kind of missing evidence is shaping the situation and which immediate conclusion is unsafe.

**Primary interaction surface:** immediate negative information.

**Secondary interaction surface:** counter-read, because the Technique helps resist staged continuity, false completeness, or misleadingly clean evidence.

**Cost note:** `Rhythm 3 / Attrition 1` is intentional under pressure. The Technique produces information immediately: it tells the user what kind of absence matters and what conclusion is unsafe. These costs apply only during ATB or another active-threat scene; in normal exploration, the Technique resolves as the user's Interpretation action.

**Effect:** Make an Interpretation-based Technique check against one incomplete or suspicious pattern. On success, the Narrator reveals one absence category relevant to the current pattern — such as a missing actor, missing route, missing object or tool, missing step in a sequence, missing warning or sign, or missing consequence that should have followed. These are examples of the kind of absence this Technique surfaces, not a closed list: the Narrator chooses whichever absence is most structurally significant and may identify other absence types of the same quality that the evidence supports.

The read tells the user what kind of absence matters and what immediate conclusion is unsafe. It does not reveal the full missing content, name the responsible party, reconstruct the entire event, or prove intent by itself.

**Restrictions:**

- requires an incomplete or suspicious pattern to read
- reveals one absence category only
- does not reveal the full missing content
- does not identify the responsible party by itself
- does not reconstruct the entire event
- does not create a bonus to another roll by itself
- does not bypass deliberate staging without contextual opposition

### Marcar la Lectura

| Field | Value |
| --- | --- |
| `name` | Marcar la Lectura |
| `name_en` | Mark the Reading |
| `origin` | Ranged Weapons |
| `world_origin` | Species: Naghii; seed: Projection Of Interpretation; transmission: Saa projection and archive scout marking drills; availability: Restricted |
| `category` | attack |
| `type` | active |
| `trigger` | The user has a ranged line to a creature whose movement, concealment, or immediate route must remain readable. |
| `requirements` | Minimum rank: Novice; weapon profile: Precision; equipment: ranged weapon with prepared marking ammunition or natural fluid projection; readable marking delivery such as pigment, scent, phosphorescent residue, or tracer; target can be physically marked |
| `target` | creature |
| `range` | weapon or projection range |
| `area` | single |
| `duration` | until the target completes its next movement or concealment attempt, clears the mark, leaves sensory reach behind a sealed barrier, or immediate position stops mattering |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the mark |
| `tags` | attack, precision, marking, counter_concealment |

**Fantasy:** The user does not simply shoot where the target is. They place a visible, scented, irritating, or phosphorescent mark where the target's next movement will reveal the line it is trying to make disappear.

**World origin:** Saa-Naghii projection practice treats distance as a place where interpretation must become consequence. Archive scouts and projection wardens developed this method so a creature's next route remains readable after the moment of contact. Non-Naghii users reproduce the method with prepared marking ammunition, pigment darts, chemical tracers, marked arrows, or a similar kit-based delivery.

**Why this is not a base Ranged Weapons attack:** A base ranged attack tries to hit or harm the target. `Marcar la Lectura` uses the hit to preserve the target's immediate route as readable information. Its value is not extra damage or accuracy; it prevents the next movement or concealment attempt from becoming cleanly ambiguous to the user.

**Primary interaction surface:** ranged precision contact.

**Secondary interaction surface:** counter-concealment, because the mark keeps one immediate route, cover choice, doorway, or hiding line readable.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique combines a ranged attack with a short-lived tracking consequence, giving it one strong surface and one secondary information-control surface. These costs apply only during ATB or another active-threat scene; in normal exploration, the Technique resolves as the user's ranged marking action without Attrition.

**Effect:** Make a Ranged Weapons attack with prepared marking ammunition, a marking kit delivery, or an equivalent natural fluid-projection Technique check against the target. If the Technique resolves successfully, the target becomes read-marked until the duration ends.

While read-marked, ordinary movement, partial cover, darkness, smoke, crowding, or a quick attempt to duck out of sight cannot make the target's immediate route ambiguous to the user. If the target moves or tries to conceal itself, the user knows which route, cover, doorway, or hiding line the marked target used, provided the mark remains within sensory reach.

The Technique does not grant an attack bonus, ignore cover, reveal exact statistics, make the target visible through sealed barriers, or share the read with allies who cannot perceive the mark.

**Restrictions:**

- requires a ranged delivery that can leave a readable physical mark
- non-natural users need prepared marking ammunition or a marking kit delivery
- requires the target to be physically markable
- applies to one creature only
- preserves the immediate route read only
- does not grant an attack bonus
- does not ignore cover or defense benefits
- does not reveal exact statistics or full intent
- does not reveal through sealed barriers or impossible sensory blocks
- does not share the read with allies who cannot perceive the mark

### Nublar la Señal

| Field | Value |
| --- | --- |
| `name` | Nublar la Señal |
| `name_en` | Blur the Signal |
| `origin` | Ranged Weapons |
| `world_origin` | Species: Naghii; seed: Venom As Commitment; transmission: Saa irritant projection and warden suppression drills; availability: Restricted |
| `category` | attack |
| `type` | active |
| `trigger` | The user has a ranged line to a creature that relies on a clean sensory read to aim, react, pursue, identify, or maintain pressure. |
| `requirements` | Minimum rank: Novice; weapon profile: Corrosion; equipment: ranged weapon with prepared residue ammunition or natural fluid projection; irritating, venomous, caustic, dusty, or sensory-residue delivery; target has a relevant sensory surface or exposed reading channel |
| `target` | creature |
| `range` | weapon or projection range |
| `area` | single |
| `duration` | until the target clears the residue, resolves one affected sight/read-dependent action, loses the residue environmentally, or immediate sensory pressure stops mattering |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the residue |
| `tags` | attack, corrosion, sensory_pressure, disruption |

**Fantasy:** The user projects venom, dust, caustic residue, or another hostile trace across the target's reading surface, making the next clean look, aim, or pursuit decision arrive through irritation and false signal.

**World origin:** Kha-Naghii hold venom as consequence attached to contact; Saa-Naghii project that same logic outward. `Nublar la Señal` comes from the projected side: the contact matters because it degrades the target's next clean decision. Non-Naghii users reproduce the method with prepared residue ammunition, irritant dust, venom capsules, caustic darts, or a similar kit-based delivery.

**Why this is not a base Ranged Weapons attack:** A base ranged attack tries to hit or harm. `Nublar la Señal` uses contact to create a bounded sensory-pressure choice: clear the residue or act through a compromised read. It is not a poison damage rider and not general blindness.

**Primary interaction surface:** ranged corrosive or irritating contact.

**Secondary interaction surface:** disruption, because the target's next clean sensory action becomes costly unless they clear the residue.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique is an attack that also creates a bounded sensory-pressure choice, giving it one strong surface and one secondary disruption surface. These costs apply only during ATB or another active-threat scene; in normal exploration, the Technique resolves as the user's ranged residue action without Attrition.

**Effect:** Make a Ranged Weapons attack with prepared residue ammunition, a residue kit delivery, or an equivalent natural fluid-projection Technique check against the target. If the Technique resolves successfully, the target becomes signal-blurred until the duration ends.

Before resolving its next action or reaction that depends on clean sight, scent, aim, identification, pursuit, or precise read, the target must choose:

- spend that opportunity clearing or neutralizing the residue, ending the effect
- act through it and take a situational penalty equal to the user's Ranged Weapons rank bonus on that one affected roll or opposed exchange

| Ranged Weapons rank | Penalty |
| --- | --- |
| Novice | `-1` |
| Adept | `-2` |
| Expert | `-3` |
| Master | `-4` |
| Consummate | `-5` |
| Transcendent | `-6` |

The penalty applies only to that single sight/read-dependent action. The Technique does not blind the target completely, prevent movement, or impose a general scene-wide penalty.

**Restrictions:**

- requires a ranged delivery that can leave irritating or degrading residue
- non-natural users need prepared residue ammunition or a residue kit delivery
- requires a relevant sensory surface or reading channel
- applies to one creature only
- affects one sight/read-dependent action only
- does not blind the target completely
- does not prevent movement
- does not create a general scene-wide penalty
- does not stack with itself on the same target
- sealed protection or irritant immunity may prevent the effect

### Doblar el Tiro

| Field | Value |
| --- | --- |
| `name` | Doblar el Tiro |
| `name_en` | Bend the Shot |
| `origin` | Ranged Weapons |
| `world_origin` | Species: Naghii; seed: Projection Of Interpretation; transmission: ruin geometry and projection angle drills; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user has a ranged line to a usable surface that can redirect, rebound, skip, or carry the projectile toward a creature that is not cleanly available through the direct line. |
| `requirements` | Minimum rank: Novice; weapon profile: Ricochet; equipment: ranged weapon with rebound-capable projectile or natural hardened projection; usable rebound surface; physically plausible indirect path |
| `target` | creature |
| `range` | weapon or projection range via surface |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` resolves normally against the final incoming path |
| `tags` | attack, ricochet, geometry, cover_denial |

**Fantasy:** The user reads a wall, step, pillar, tablet, shield edge, or other hard surface as part of the shot, striking the surface so the projectile bends into a line the target did not fully own.

**World origin:** Naghii archive and ruin practice teaches that built surfaces are evidence. In projection training, that becomes a material combat method: the wall, step, or doorway is read as part of the shot rather than treated as inert scenery.

**Why this is not a base Ranged Weapons attack:** A base ranged attack follows the direct line. `Doblar el Tiro` deliberately uses a declared surface to create a physically plausible indirect line. Its identity is not better aim or more damage; it is making the environment carry the shot.

**Primary interaction surface:** indirect ranged attack geometry.

**Secondary interaction surface:** cover denial, but only against the original direct-line edge that the rebound path genuinely bypasses.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique is a standard active attack with an indirect-line permission. It changes the attack geometry, but it does not add persistent state, deny future action, or bypass defense wholesale.

**Effect:** Make a Ranged Weapons attack through one declared rebound or skip surface. If the Technique resolves successfully, the attack may reach a target that has partial cover, an offset doorway, an angled corner, or a blocked direct line, as long as a physically plausible indirect path exists.

The target still receives any defense that makes sense against the final incoming path, but cannot claim protection from the original direct-line cover if the declared rebound path genuinely bypasses that edge.

This does not hit through sealed barriers, ignore total cover, curve freely in open air, or seek a target the user cannot reasonably locate.

**Restrictions:**

- requires one usable rebound or skip surface
- requires a projectile or projection that can physically rebound, skip, or continue
- requires a physically plausible indirect path
- one rebound or skip surface only at Novice
- does not ignore total cover or sealed barriers
- does not curve freely in open air
- does not seek targets the user cannot reasonably locate
- does not remove defense against the final incoming path

### Clavar la Cadencia

| Field | Value |
| --- | --- |
| `name` | Clavar la Cadencia |
| `name_en` | Pin the Cadence |
| `origin` | Ranged Weapons |
| `world_origin` | Species: Naghii; seed: Preserved Distance; transmission: archive warden cadence drills; availability: Common |
| `category` | attack |
| `type` | reactive |
| `trigger` | A creature within ranged line declares or begins a movement action, approach, withdrawal, cover change, line break, or other action that physically moves it before the immediate exchange settles. |
| `requirements` | Minimum rank: Novice; weapon profile: Volley; equipment: ranged weapon or natural projection capable of controlled repeated release; target within ranged line; user can sustain a short cadence |
| `target` | creature |
| `range` | weapon or projection range |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | contextual — the target may answer with appropriate defense, movement timing, cover use, or balance |
| `tags` | attack, volley, movement_control, pressure |

**Fantasy:** The user lays a measured sequence of shots, spits, or projected pulses into a moving creature's next steps, forcing it to break rhythm, guard its body, or correct its footing before the movement completes.

**World origin:** Naghii archive wardens do not treat movement as empty space. An approach, withdrawal, cover shift, or line break is a procedure in motion. `Clavar la Cadencia` turns repeated projection into a way of preserving distance by breaking the cadence of hostile movement.

**Why this is not a base Ranged Weapons attack:** A base ranged attack tries to hit or harm the target on the user's action. `Clavar la Cadencia` is a reactive interruption against declared movement: the impact matters because it cuts distance from that movement. It is not volume fire, extra damage, or a multi-target attack.

**Primary interaction surface:** reactive ranged cadence against movement.

**Secondary interaction surface:** movement disruption, because a successful cadence can leave the target short of cover, short of melee contact, or short of a clean line break.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique is a ranged reactive attack that can also cut distance from one declared movement. It does not create a persistent slow, make multiple attacks, or sustain broad suppression.

**Effect:** Make a reactive Ranged Weapons attack or Technique check against the moving target before the triggering movement finishes.

If the Technique resolves successfully, the attack resolves normally and the target's remaining distance for that triggering movement is reduced by 1 meter per Ranged Weapons rank bonus.

| Ranged Weapons rank | Movement reduction |
| --- | --- |
| Novice | `3m` |
| Adept | `4m` |
| Expert | `5m` |
| Master | `6m` |
| Consummate | `7m` |
| Transcendent | `8m` |

If the reduction prevents the target from reaching its declared position, it stops at the last legal position it can still reach. This can leave the target short of cover, short of melee contact, or short of a clean line break if the lost distance matters.

The Technique affects only that triggering movement. It does not reduce the target's speed for the rest of the round, attack multiple targets, or create area suppression.

**Restrictions:**

- requires line of effect to one target
- requires a ranged tool or projection capable of controlled repeated release
- affects one target only
- affects the triggering movement only
- movement reduction is 1 meter per Ranged Weapons rank bonus
- does not deal extra damage beyond the reactive attack
- does not attack multiple targets
- does not reduce speed after the triggering movement resolves
- does not create broad suppression or area denial
- does not force a choice between stopping and accepting consequence

### Plantar la Guardia

| Field | Value |
| --- | --- |
| `name` | Plantar la Guardia |
| `name_en` | Stand Guard |
| `origin` | Spear |
| `world_origin` | Species: Naghii; seed: Coiled Readiness; transmission: archive guard ward formation drills; availability: Restricted |
| `category` | utility |
| `type` | active |
| `trigger` | The user chooses to establish a spear ward zone around their current position, declaring the area as contested space and holding the posture rather than advancing away from it. |
| `requirements` | Minimum rank: Novice; weapon profile: Ward; equipment: a spear or other committed reach weapon capable of sustained threat posture; state: stable footing and ability to hold the position |
| `target` | zone |
| `range` | self |
| `area` | self-zone |
| `duration` | until the user moves more than a negligible distance from the declared position, turns the ward away, or is forced off position by a hostile action |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | none |
| `tags` | utility, control, stability, setup |

**Fantasy:** The user plants the spear and holds. The point is already where the enemy needs to pass. There is no strike yet — only the declared condition that acting in this space will cost more than acting outside it. Stillness here is not patience. It is stored threat made spatial.

**World origin:** Naghii archive guard doctrine treats stillness held at a threshold as stored threat. A planted position with a spear declares the surrounding space as contested before any entry is attempted. Non-Naghii can learn it with any committed reach weapon that can credibly present a sustained threat posture across a zone.

**Why this is not a base attack:** A base spear attack strikes at a target. `Plantar la Guardia` declares the space as contested and taxes any enemy who acts within it over time. The user can still fight from the planted point, but the Technique's identity is zone ownership through held posture, not a single hostile exchange.

**Primary interaction surface:** zone control — the ward zone creates a sustained Rhythm tax on enemy actions.

**Secondary interaction surface:** setup, because an enemy paying extra Rhythm for every action inside the zone falls behind on tempo relative to the user and any allies outside the zone.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique produces no immediate attack or movement — its value is entirely in the Rhythm tax it imposes on enemy actions over time. The posture persists while the user fights from the planted point, but ends when the user abandons the point or turns the ward away. This keeps the Technique tactical: the user can act, but must decide whether holding that space remains worth the positional commitment and repeated Attrition.

**Effect:** Establish a ward zone centered on the user extending to weapon reach plus 1 meter. While the zone is active, any enemy that performs an active action within the zone — including entering the zone through movement, attacking from within it, or using a Technique inside it — pays an additional Rhythm cost on top of that action's normal cost equal to 1 plus the user's Spear competency rank bonus.

| Spear rank | Zone Rhythm cost |
| --- | --- |
| Novice | `+2` |
| Adept | `+3` |
| Expert | `+4` |
| Master | `+5` |
| Consummate | `+6` |
| Transcendent | `+7` |

Allies within or passing through the zone do not pay this cost. Enemies may leave the zone freely without penalty — the cost applies only to active actions performed within or through the zone, not to clean withdrawal.

The user may attack, use Techniques, defend, speak, or pressure enemies while holding the zone if those actions do not abandon the position or turn the ward away from the contested space.

**Restrictions:**

- requires stable footing to hold the ward position
- ends when the user moves more than a negligible distance from the declared position
- ends when the user turns the ward away from the contested space or can no longer present the threat posture
- ends when the user is forced off position by knockdown or displacement
- does not affect allies within the zone
- does not prevent enemies from leaving the zone freely
- Rhythm cost applies only to active actions within or through the zone
- cannot be maintained while suffering Derribado or Desequilibrado

### Tocar y Ceder

| Field | Value |
| --- | --- |
| `name` | Tocar y Ceder |
| `name_en` | Touch and Yield |
| `origin` | Flexible Weapons |
| `world_origin` | Species: Naghii; seed: Preserved Distance; transmission: archive warden skirmish contact drills; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user wants to make contact with a target at or within 1 meter outside flexible reach and return to a preferred position in a single trained sequence — entering, striking, and withdrawing before the target can convert the contact into a stable close exchange. |
| `requirements` | Minimum rank: Novice; weapon profile: Skirmish; equipment: flexible weapon, functional tail/tendril, or other credible skirmish flexible surface |
| `target` | enemy |
| `range` | flexible reach |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 1 |
| `saving_roll` | contextual — resolved through the hostile exchange created by the approach and contact; if the target answers successfully, the attack does not land and the return movement does not complete |
| `tags` | attack, mobility, pressure, reposition |

**Fantasy:** The user enters briefly, places contact, and withdraws to their preferred geometry before the target can build a response on it. The withdrawal is not retreat — it is the completion of the technique. The distance the user returns to is the distance they chose to fight from.

**World origin:** Naghii guard and scout practice treats correct distance as a condition of safety and interpretation. Brief contact that restores that distance is not hesitation but trained completion. A skirmisher who rushes into contact and does not restore the line has only half-trained the method.

**Why this is not a base Flexible Weapons attack:** A base flexible-weapon attack delivers a strike and remains where the user is. `Tocar y Ceder` packages a brief approach and a conditional return into a single action — the withdrawal is part of what is being executed, not something the user simply decides to do afterward.

**Primary interaction surface:** skirmish attack with built-in repositioning.

**Secondary interaction surface:** mobility, because the approach and return together deny the target an established close exchange without requiring a separate movement action.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique packages a brief approach and a conditional return into a single active attack. It does not create persistent control, deny the target future movement, or allow the user to attack multiple targets.

**Effect:** As part of this action, approach up to 1 meter toward the target — no separate movement action required. Then make a Flexible Weapons attack or equivalent tail or tendril Technique check against the target. If the Technique resolves successfully, immediately reposition up to 1 meter in any direction as part of the same action. This repositioning does not grant the target a reaction opportunity. The user returns to their preferred distance before the target can convert the brief contact into a stable close exchange.

**Restrictions:**

- approach is up to 1 meter only, not a full movement action
- return repositioning is contingent on a successful attack
- does not create zone control or deny target movement
- applies to one target only
- should not function if terrain prevents credible approach and withdrawal
- return movement does not grant a reaction opportunity on success

### Trabar el Gesto

| Field | Value |
| --- | --- |
| `name` | Trabar el Gesto |
| `name_en` | Snare the Stroke |
| `origin` | Flexible Weapons |
| `world_origin` | Species: Naghii; seed: Threshold Denial; transmission: temple guard execution break drills; availability: Restricted |
| `category` | utility |
| `type` | reactive |
| `trigger` | An enemy within flexible reach declares or begins a weapon-rooted attack or Technique — the commitment arc of the action is visible and within reach. |
| `requirements` | Minimum rank: Novice; weapon profile: Interruption; equipment: flexible weapon, functional tail/tendril, or other credible interruption flexible surface; target within flexible reach; user has a credible flexible contact line to the target's weapon or weapon arm |
| `target` | enemy |
| `range` | flexible reach |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 1 |
| `saving_roll` | `R.R.` reduces — on a successful Alteration Resistance Roll, Impedido is not applied and the triggering action resolves normally |
| `tags` | utility, control, disruption, pressure |

**Fantasy:** The user reads the commitment arc of the enemy's weapon action and sends the flexible weapon into that line before the stroke can lock in. The catch lands on the arm, the grip, or the execution line — not to hold, but to break the moment the action needed to become unstoppable.

**World origin:** Naghii archive guard training treats every committed action as having a threshold moment where it is locked in and most interruptible. In confined archive spaces where full parrying guards are not available, this method of catching a weapon arm or execution line before the stroke completes is a specific taught discipline.

**Why this is not a base Flexible Weapons attack:** A base flexible-weapon attack strikes the target's body on the user's turn. `Trabar el Gesto` intercepts a weapon commitment arc on the enemy's turn and applies a disabling condition if the catch lands — its identity is not dealing harm but breaking the enemy's ability to complete a weapon action.

**Primary interaction surface:** reactive weapon-arc interruption.

**Secondary interaction surface:** condition application — Impedido on a failed Alteration R.R., preventing weapon-rooted Techniques until cleared by Enfoque.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique is a reactive action with a condition-application surface. The condition is recoverable through Enfoque, the trigger is narrow (weapon execution only), and the target has an R.R. window to resist. These constraints prevent the cost from rising above the standard anchor despite the condition output.

**Effect:** Make a reactive Flexible Weapons check or equivalent tail or tendril Technique check against the triggering enemy. If the Technique resolves successfully, the target immediately makes an Alteration Resistance Roll.

The `Impedido` severity is determined by the competency rank used for the Technique:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe
- Higher ranks continue this progression if the system later defines higher severity bands.

On a failed R.R., the target becomes `Impedido` at that severity: the triggering weapon action does not complete, and the target cannot use weapon-rooted Techniques until it succeeds on an Enfoque Specialization Roll against the original severity. On a successful R.R., `Impedido` is not applied and the triggering action resolves normally.

**Restrictions:**

- target must be within flexible reach
- user must have a credible contact line to the target's weapon or weapon arm
- applies to one target only
- does not create full restraint or movement restriction
- does not apply to non-weapon actions or purely social commitments
- does not prevent the target from taking non-weapon actions while Impedido
- Impedido is removed by a successful Enfoque S.R. against the original severity

### Cruzar la Punta

| Field | Value |
| --- | --- |
| `name` | Cruzar la Punta |
| `name_en` | Cross the Point |
| `origin` | Evasion |
| `world_origin` | Species: Naghii; seed: Ritualized Access; transmission: archive guard threshold-crossing drills; availability: Restricted |
| `category` | utility |
| `type` | reactive |
| `trigger` | An enemy commits a single-target physical attack or physical Technique against the user with a discernible forward vector. |
| `requirements` | Minimum rank: Novice; state: not fully restrained or immobilized; enough space to close toward the attacker |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | contextual — if the attacker anticipated the close, they may contest with the relevant Technique or roll; on success, the closing movement does not deny the attack's angle |
| `tags` | defense, mobility, counter_positioning, survival_window |

**Fantasy:** The attacker commits forward. The expected answer is to yield. The Naghii enters instead — flowing into the committed path at the exact moment it cannot redirect. Inside now, the attacker's position is no longer what they planned.

**World origin:** Naghii archive-guard training teaches controlled threshold crossing — passing through a guarded line without hesitation at the exact right moment — as a deliberate, disciplined act. In combat, the same doctrine applies to committed attacks: the user crosses into the attack rather than away from it.

**Why this is not a base Evasion check:** A base Evasion check moves away from or resists an incoming attack. `Cruzar la Punta` closes toward the attack instead — denying the attacker their optimal range and raising the threshold for their triggering strike. Its identity is entering the danger, not escaping it.

**Primary interaction surface:** reactive close into a committed attack, denying the attacker their planned striking geometry.

**Secondary interaction surface:** threshold pressure on the triggering attack, because the user's new inside position forces the attacker's A.R. against a raised threshold.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique is a narrow reactive close — its value is denying the attacker their planned range and raising their threshold, not damage or conditions. Attrition reflects the genuine body effort of closing into a committed attack rather than away from it.

**Effect:** Make an Evasion check. On success, close up to 2 meters toward the attacker as the strike arrives — entering rather than yielding. The attack resolves against the user's new position, inside the attacker's committed range and angle. The attacker's A.R. for the triggering attack is contested at raised threshold. Closing does not disarm or neutralize the attacker — a skilled opponent will adjust grip, use the butt end of a reach weapon, or reorient their body. What the user has gained is denying the attacker their preferred range, leaving them with the burden of re-establishing it. The user does not attack as part of this Technique.

**Restrictions:**

- functions only against committed single-target physical attacks with a forward vector
- does not function against area effects or attacks that track user movement
- does not function when the user is fully restrained or immobilized
- does not grant an attack or apply a condition
- attacker retains all other action options from the new close-range position
- closing into an anticipated attack can be countered

### Vaciar el Blanco

| Field | Value |
| --- | --- |
| `name` | Vaciar el Blanco |
| `name_en` | Empty the Target |
| `origin` | Evasion |
| `world_origin` | Species: Naghii; seed: Absence As Evidence; transmission: outer archive countertracking and displacement doctrine; availability: Restricted |
| `category` | utility |
| `type` | reactive |
| `trigger` | An enemy commits a single-target physical attack or physical Technique against the user. |
| `requirements` | Minimum rank: Novice; state: not fully restrained or immobilized; enough space to move 2 meters |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | until the user makes a D.R., C.R., or R.R. in response to a hostile action after this Technique resolves |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | none |
| `tags` | defense, mobility, counter_positioning, reposition |

**Fantasy:** The body leaves the readable position before the attacker settles their read. No block. No contest. The target has moved, and for a moment the new position is not yet fully mapped in the attacker's tracking. That moment is the window.

**World origin:** Naghii archival doctrine holds that what is not present cannot be struck, and that deliberate displacement is a form of denial, not retreat. This method expresses the same logic in body movement: removing the body from an acquired target lock is a form of control, not merely escape.

**Why this is not a base Evasion check:** A base Evasion check tests whether the user avoids a specific incoming attack. `Vaciar el Blanco` repositions without reactions and opens a bounded defensive window tied to the new position being unsettled in the attacker's tracking — a mechanical state distinct from a single dodge roll.

**Primary interaction surface:** proactive displacement that opens a brief defensive/resistance bonus window.

**Secondary interaction surface:** mobility, because the 2-meter move without reaction opportunities allows the user to create spacing or reach terrain without paying a normal movement cost on their turn.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique is a quick bounded repositioning with a single defensive window that closes when the user must answer hostile pressure. Attrition reflects that deliberate full-body displacement under pressure is a real physical effort, not a passive stance shift.

**Effect:** Move up to 2 meters in any direction without granting reaction opportunities. The next time you must make a `D.R.`, `C.R.`, or `R.R.` in response to a hostile action after this Technique resolves, you gain a bonus to that roll equal to your Evasion competency rank.

| Evasion rank | Roll bonus |
| --- | --- |
| Novice | `+1` |
| Adept | `+2` |
| Expert | `+3` |
| Master | `+4` |
| Consummate | `+5` |
| Transcendent | `+6` |

This bonus reflects that the new position has not yet settled in the hostile actor's tracking. Once that defensive or resistance roll resolves, the window closes regardless of outcome.

**Restrictions:**

- requires enough space to move 2 meters in the chosen direction
- does not function when the user is fully restrained or immobilized
- bonus applies to the first `D.R.`, `C.R.`, or `R.R.` made in response to a hostile action, then closes
- does not grant an attack or produce damage

### Leer el Arco

| Field | Value |
| --- | --- |
| `name` | Leer el Arco |
| `name_en` | Read the Arc |
| `origin` | Astronomía |
| `world_origin` | Species: Naghii; seed: Projection Of Interpretation; transmission: outer archive trajectory and projection drills; availability: Restricted |
| `category` | utility |
| `type` | active |
| `trigger` | A creature or object within observable range is in movement, about to act, or has a discernible vector that can be projected to a next position or endpoint. |
| `requirements` | Minimum rank: Novice; state: target has a discernible movement vector or imminent declared action |
| `target` | creature |
| `range` | line of sight |
| `area` | single |
| `duration` | until the target completes the revealed action, significantly changes their intent before executing it, or the scene no longer tracks the projected trajectory |
| `cost` | Rhythm 3; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | contextual — if the target is actively feinting or concealing movement intent, they may oppose with the relevant Technique; on success, the read is inaccurate or reveals only that the visible vector is not the real one |
| `tags` | utility, support, counter_read, setup |

**Fantasy:** The astronomer does not look at where the object is. They look at the arc. Every vector has an endpoint, and the discipline of projecting celestial movement — tracing where something must be, not just where it appears — applies to anything in motion. The user reads the arc and declares where it ends.

**World origin:** Naghii astronomical training teaches projection as a primary cognitive tool: not identifying what is visible but projecting where it will be. The same tools — arc reading, vector extension, endpoint calculation — transfer directly to tracking the movement of any creature or object in the field.

**Why this is not a base Astronomía check:** A base Astronomía check answers what the user can observe or reason about the target's current state. `Leer el Arco` forces the Narrator to declare a specific trajectory truth — a projected endpoint — before the target's next action executes. The base check cannot produce a guaranteed pre-execution declaration that is also made available to allies.

**Primary interaction surface:** immediate trajectory information that must be declared before the target acts.

**Secondary interaction surface:** support, because the declared truth is available to all allies within clear hearing range, giving the team a window between the user's turn and the target's execution to act on what is coming.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique is a quick read under pressure that produces one concrete trajectory truth. Its value is entirely in the information and the window it creates before the target's action executes. These costs apply only during ATB or active-threat scenes; in exploration, the Technique resolves as the user's Astronomía action without Attrition.

**Effect:** Make an Astronomía Specialization Roll against one target in motion or about to act. On success, the Narrator must declare one trajectory truth about the target's next action or movement before it executes — such as where the target will be at the end of their next movement; the landing destination or path of a ranged attack they are about to make; what cover, position, or creature the target's current movement vector leads them toward; or whether the target's current direction brings them into reach of an ally, a hazard, or a dead end. These are examples of the kind of truth this Technique produces, not a closed list: the Narrator chooses whichever truth is most structurally meaningful and may declare other trajectory truths of the same quality and specificity that the vector supports.

This declared truth is available to the user and any ally within clear hearing range before the target's action executes. The technique does not prevent the target from acting, does not grant any roll bonus against the target, and does not reveal more than one trajectory truth at Novice.

**Restrictions:**

- requires an observable target with a discernible movement vector or imminent action
- reveals one trajectory truth only
- does not prevent the target from acting
- does not grant roll bonuses against the target
- does not reveal statistics, conditions, or intent beyond movement trajectory
- accuracy depends on target not dramatically changing intent before execution
- shared only with allies within clear hearing range

### Leer el Propósito

| Field | Value |
| --- | --- |
| `name` | Leer el Propósito |
| `name_en` | Read the Purpose |
| `origin` | Architecture |
| `world_origin` | Species: Naghii; seed: The Archive Must Continue; transmission: outer archive structural intent reading drills; availability: Restricted |
| `category` | utility |
| `type` | active |
| `trigger` | The user is present in or adjacent to a built space with enough legible architectural features — walls, passages, volumes, thresholds, constructed surfaces — to read the original design intent rather than just the current condition. |
| `requirements` | Minimum rank: Novice; state: built space with legible architectural features present |
| `target` | structure |
| `range` | present space |
| `area` | single structure or zone |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | contextual — if the space has been deliberately altered to mislead a reader, another character may oppose with Architecture or the relevant masking Technique; on success, the user identifies that the space does not read cleanly but does not receive the intended truth |
| `tags` | utility, setup, counter_positioning, pattern_exploitation |

**Fantasy:** The builder always left a record. The user reads it: where the space was designed to move people, what it was designed to hide, which volumes were built to carry meaning and which to carry nothing. Design intent is structural grammar — it does not disappear when the builders do.

**World origin:** Naghii archive training teaches that every built space is a record of intent: where the builders needed people to go, what they needed to hide, and what the structure was designed to protect. Reading that grammar is a practical discipline before deeper archive access is permitted — it is how you find where things were hidden, which exits were made deliberate, and which thresholds were built to be controlled.

**Why this is not a base Architecture check:** A base Architecture check lets the user answer factual questions about the built form and takes time under normal conditions. `Leer el Propósito` forces the Narrator to declare one specific structural intent truth — what the space was designed to do — immediately during an active scene, producing a guaranteed declaration that the raw S.R. cannot compel.

**Primary interaction surface:** immediate structural intent information — the Narrator must declare one design truth about the space before the user acts on it.

**Secondary interaction surface:** counter-positioning and setup, because knowing where the space was built to lead, conceal, or control directly informs tactical movement and routing decisions.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique is a fast structural read under pressure that produces one concrete intent truth. Its value is entirely in the information — where the space was built to lead or hide. These costs apply only during ATB or active-threat scenes; in exploration, the Technique resolves as the user's Architecture action without Attrition.

**Effect:** Make an Architecture Specialization Roll against the built space. On success, the Narrator provides one structural intent truth about how the space was designed — such as where the original circulation was built to lead; whether a volume, passage, threshold, or exit was intentionally concealed in the design; which structural feature was built for observation, controlled access, or defense rather than habitation; or which part of the structure was designed as load-bearing and permanent versus decorative or removable. These are examples of the kind of truth this Technique produces, not a closed list: the Narrator chooses whichever truth is most immediately relevant and may declare other structural intent truths of the same quality that the built form supports.

The read concerns original design intent, not current state: it does not reveal present occupants, post-construction modifications, current traps, or contents placed after the structure was built.

**Restrictions:**

- requires built space with legible architectural features
- reveals one structural intent truth only
- concerns original design intent, not current state
- does not reveal current occupants, traps, or post-construction modifications
- does not function against natural formations or fully collapsed rubble with no readable design
- does not create roll bonuses by itself
- does not reconstruct the full building history or builder identity

### Templar el Veneno

| Field | Value |
| --- | --- |
| `name` | Templar el Veneno |
| `name_en` | Temper the Venom |
| `origin` | Tolerancia + Venom Resistance |
| `world_origin` | Species: Naghii (Kha); seed: Venom As Commitment; transmission: kha venom conditioning and endurance drills; availability: Restricted |
| `category` | utility |
| `type` | passive |
| `trigger` | none — always active while requirements are met |
| `requirements` | Minimum rank: Novice; Tolerancia at Novice or higher; Venom Resistance at Novice or higher; mentor-gated acquisition |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | permanent while both Tolerancia and Venom Resistance remain at Novice or higher |
| `cost` | Rhythm 0; Attrition 0 — cost was paid in conditioning and training, not in the ATB |
| `saving_roll` | none |
| `tags` | utility, mitigation, condition_reduction, stability |

**Fantasy:** The body does not fight what it already carries. A Kha-Naghii who has trained under their own venom — and trained the discipline to hold adverse physical states without losing function — reaches a point where external venom finds familiar terms. The metabolic adjustment is not a decision. It is the body's response to a known adversary.

**World origin:** Kha-Naghii biological conditioning gives them systemic tolerance to their own venom. Formal initiation training teaches the practitioner to channel that tolerance through disciplined endurance: the body has been tempered by years of controlled exposure, and Tolerancia training gives shape to what would otherwise be raw biological luck.

**Why this is not raw Venom Resistance:** Raw Venom Resistance improves the R.R. against venom application. `Templar el Veneno` fires after the R.R. resolves — a second floor modifier that reduces the settled severity by one additional step regardless of what the roll produced. A Kha-Naghii who fails their R.R. with this Technique still settles at a lower severity than an untrained character who fails the same roll.

**Primary interaction surface:** passive severity reduction on Veneno family ailment application.

**Secondary interaction surface:** stability — by reliably capping venom severity at a lower tier, the Technique keeps the character functional under conditions that would remove others from effective action.

**Cost note:** `Rhythm 0 / Attrition 0` is correct and deliberate. This is a passive Technique — no ATB action, no declared use, no Rhythm or Attrition expenditure in the field. The cost of this Technique was paid during the conditioning process: it is mentor-gated, cannot be self-studied, and requires documented systematic venom exposure combined with Tolerancia training. That acquisition process is the cost.

**Effect:** When a Veneno family ailment settles on the user after all R.R. processing, reduce the final settled severity by one step automatically: Severe becomes Moderate, Moderate becomes Minor, Minor does not settle. This reduction requires no check, no declared action, and no Rhythm or Attrition cost. It applies after the standard Alteration Resistance Roll resolves — the R.R. processes normally, and then this passive floor modifier reduces the result by one additional step.

**Restrictions:**

- applies to Veneno family ailments only
- requires Venom Resistance at Novice rank or higher
- requires Tolerancia at Novice rank or higher
- does not negate Veneno ailments completely by itself
- does not apply to Alteration, Affliction, or other family effects from venom sources
- does not stack with other automatic severity-reduction passives of the same type
- outsiders require documented systematic conditioning — improvised exposure does not qualify

### Sostener el Canal

| Field | Value |
| --- | --- |
| `name` | Sostener el Canal |
| `name_en` | Hold the Channel |
| `origin` | Meditación + Contención + Mental Resistance (Abzu) |
| `world_origin` | Species: Naghii; seed: Holding Dangerous Knowledge; transmission: igi-an channel management and containment drills; availability: Restricted |
| `category` | utility |
| `type` | passive |
| `trigger` | The user performs a meditation action specifically directed at reducing the intensity of an active Abzu-origin or mental Affliction. |
| `requirements` | Minimum rank: Novice; Meditación at Novice or higher; Contención at Novice or higher; Mental Resistance (Abzu) at Novice or higher; active Abzu-origin or mental Affliction present |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | permanent while all three prerequisites remain at Novice or higher |
| `cost` | no additional cost beyond the meditation action itself |
| `saving_roll` | none |
| `tags` | utility, recovery, condition_reduction, stability |

**Fantasy:** The igi-an practice was never about closing the channel. Closing it would mean losing the capacity to read the sky, sense the Abzu's movements, hear what the records mean in the present. What the deepest practitioners learn is not closure — it is management. The channel is held at the threshold. What enters can be acknowledged without being absorbed. And when it has absorbed too much, Contención gives it a route out — not through force, but through the practiced discipline of knowing where the boundary is and returning to it.

**World origin:** The Naghii's Abzu susceptibility is the inherited cost of generations of igi-an practice. The priesthood does not try to eliminate it — doing so would sever the capacity that makes their astronomical and theological work possible. Inner archive training instead teaches the practitioner to distinguish between absorption and holding: the channel is open, but the practitioner is not identical to what passes through it.

**Why this is not raw Meditación or raw Mental Resistance:** Raw Mental Resistance improves the initial R.R. against mental or Abzu-origin effects. Raw Meditación produces recovery from Afflictions without specific calibration to the Abzu channel. `Sostener el Canal` produces a better meditation outcome specifically for Abzu-origin and mental Afflictions — the practitioner's trained channel management turns the act of recovery into a more efficient passage back to stability.

**Primary interaction surface:** improved meditation recovery for Abzu-origin and mental Afflictions.

**Secondary interaction surface:** stability — by recovering faster from the Afflictions the Naghii is most susceptible to, the technique partially compensates for the biological openness rather than merely enduring it.

**Cost note:** No additional cost beyond the meditation action itself. Like Templar el Veneno, the cost was paid in training: mentor-gated at its deepest layer, requires documented susceptibility and recovery experience, and demands concurrent development of Meditación, Contención, and Mental Resistance (Abzu). The meditation session that activates the bonus carries its own cost in time and focus — this Technique does not add to it.

**Effect:** When the user meditates specifically to reduce the intensity of an active Abzu-origin or mental Affliction, add a bonus to the Meditación roll equal to the user's Contención competency rank bonus.

| Contención rank | Bonus |
| --- | --- |
| Novice | `+1` |
| Adept | `+2` |
| Expert | `+3` |
| Master | `+4` |
| Consummate | `+5` |
| Transcendent | `+6` |

This bonus applies only when the meditation is directed at an Abzu-origin or mental Affliction — general meditation or meditation aimed at other purposes does not benefit. The technique does not change what the meditation action costs in time or focus; it improves the quality of the recovery that action produces.

**Restrictions:**

- applies only to meditation directed at Abzu-origin or mental Afflictions
- requires Meditación, Contención, and Mental Resistance (Abzu) each at Novice or higher
- does not apply to physical, Alteration, or Veneno family Afflictions
- does not change what the meditation action costs
- does not reduce Affliction intensity outside a dedicated meditation action
- general meditation does not receive the bonus

### Marcar la Grieta

| Field | Value |
| --- | --- |
| `name` | Marcar la Grieta |
| `name_en` | Mark the Crack |
| `origin` | Arqueología |
| `world_origin` | Species: Naghii; seed: The Archive Must Continue; transmission: igi-an ruin field reading and Firstborn remnant cataloguing; availability: Restricted |
| `category` | utility |
| `type` | active |
| `trigger` | The user observes an enemy at close range to read construction faults or wear patterns on their armor or equipment — or exposed joints, previous injury patterns, or anatomical gaps on an unarmored target — or examines a static structural element in exploration. |
| `requirements` | Minimum rank: Novice; Arqueología at Novice or higher; combat use: close range with line of sight to the target; exploration use: physical access to the structural element |
| `target` | enemy / structure |
| `range` | close (combat); touch (exploration) |
| `area` | single |
| `duration` | until mark is used or end of scene (combat); retained (exploration) |
| `cost` | Rhythm 3; Attrition 1 (ATB only — no Attrition cost in exploration without active threat) |
| `saving_roll` | none |
| `tags` | utility, pattern_exploitation, setup, counter_read |

**Fantasy:** Everything has a point where it gives. Armor: the dent never fully hammered out, the joint re-riveted too tight, the section where two plates meet at an angle the maker compromised on. Unarmored: the joint that absorbed a previous blow and never fully recovered, the gap between scale plates at maximum extension, the ridge of scar tissue that sits over bone rather than muscle. Not where to hit — where the material has already decided it will give.

**World origin:** Naghii ruin field training treats structural failure reading as a survival discipline: a practitioner who cannot identify which stone will give way cannot safely work in active ruins. The combat application transfers the same discipline to any material surface — worn armor, exposed joints, previous injury sites — because all of them carry the same evidence of stress, repair history, and previous force.

**Why this is not raw Arqueología:** Raw Arqueología produces narrative context — "the armor shows heavy use, there's an older repair on the left shoulder, the creature's right knee took a bad blow" — without a defined mechanical benefit. `Marcar la Grieta` produces a specific, bounded output: a 1-step difficulty reduction on a committed follow-up attack (combat) or a precise structural vulnerability location (exploration).

**Primary interaction surface (combat):** setup — identify one material fault zone on the target → difficulty of next attack on that zone reduced by 1 step. Applies to armored and unarmored targets alike.

**Primary interaction surface (exploration):** information — identify the most structurally vulnerable point of an examined element.

**Cost note:** `Rhythm 3 / Attrition 1` matches the established Naghii information technique anchor. The combat benefit requires a setup action before it applies — the user pays 3 rhythm to read, then pays the attack cost separately. The exploration surface has no Attrition cost outside active threat.

**Effect:** Make an Arqueología check at difficulty set by the Narrator based on the target's protective complexity, wear or injury state, and observation conditions.

*Combat:* On success, identify one zone of the target where material structure creates a fault — for armored targets: a construction gap, wear point, or repair compromise in fabricated protection; for unarmored or naturally protected targets: an exposed joint, a previous injury site, or an anatomical gap where protection is thinnest. The difficulty of the user's next attack against the identified zone is reduced by 1 step. The mark expires when the attack is made or at the end of the scene.

*Exploration:* On success, the Narrator identifies the most structurally vulnerable point of the examined element — such as: the stone block with the widest joint gap, the pillar base showing the deepest erosion, or the floor section covering a hollow beneath. The Narrator chooses the specific fact — the examples above are illustrative, not a closed menu.

On a failed check in either surface: no fault is identified.

**Restrictions:**

- combat use requires close range with line of sight to the target
- combat mark applies to one zone of one target only
- combat mark expires on use or end of scene
- does not function against targets with no readable material structure (purely fluid or incorporeal forms)
- exploration use requires physical access to the structural element
- failed check yields no benefit in either surface

---

### Sentar el Tercer Punto

| Field | Value |
| --- | --- |
| `name` | Sentar el Tercer Punto |
| `name_en` | Set the Third Point |
| `origin` | Equilibrio |
| `world_origin` | Species: Naghii; seed: Ziggurat Body Logic; transmission: archive survey and ruin-reading field training; availability: Restricted |
| `category` | utility |
| `type` | reactive |
| `trigger` | The user attempts to move through terrain that would impose a speed penalty, difficulty increase, or mandatory Balance check due to unstable, angled, collapsed, or damaged footing. |
| `requirements` | Minimum rank: Novice; Equilibrio at Novice or higher; at least one stable anchor point reachable along the movement path |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | none |
| `tags` | defense, stability, mobility, terrain |

**Fantasy:** The floor shifts. Everyone else slows or stops to reassess. The practitioner finds the third point — tail against a broken block, weapon butt on the lower step, a hand to the wall — and moves through the broken surface as if it were level. The instability never reaches the upper body. Two steps cross terrain that should have cost three.

**World origin:** Naghii archive survey training prepares practitioners for environments where floor integrity cannot be assumed — partially collapsed ziggurats, flooded antechambers, rubble-covered record vaults. The Naghii method uses the tail as a third contact point against low surfaces along the movement path. Non-Naghii learn an equivalent reflex through any tradition that trains deliberate third-contact navigation on bad terrain: a weapon or staff used as a low brace, a hand placed against a wall, or another trained weight-redistribution method.

**Why this is not raw Equilibrio:** Raw Equilibrio use produces narrative stability — the character does not fall, looks composed, is not slowed obviously — without a defined mechanical benefit. `Sentar el Tercer Punto` converts 2 spaces of difficult terrain into free movement through the Equilibrio check: terrain speed penalties, difficulty increases, and mandatory Balance checks do not apply to those 2 spaces on a successful roll.

**Primary interaction surface:** terrain traversal — 2 spaces of free movement through difficult terrain on a successful Equilibrio check.

**Secondary interaction surface:** positional continuity — maintains tactical engagement range and approach options across surfaces that would otherwise disrupt them.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique grants 2 spaces of free terrain movement — enough to cross meaningful obstacles and engage or reposition from terrain that would penalize other combatants. The Equilibrio check is its own gate; the effect is purely positional with no condition output on an opponent. One extra rhythm over a simple one-action negation reflects that the benefit applies over 2 spaces of movement rather than a single action moment.

**Effect:** Make an Equilibrio check. On success, identify and use a stable anchor point along the movement path — extending the tail, bracing a weapon, placing a hand, or using whatever contact surface is available — and move up to 2 spaces through the triggering terrain as if on stable ground. Terrain speed penalties, difficulty increases, and mandatory Balance checks do not apply to those 2 spaces. On failure, terrain effects apply normally.

**Restrictions:**

- requires at least one stable anchor point reachable along the movement path
- grants free movement for 2 spaces only — terrain effects apply normally beyond those 2 spaces
- does not negate non-terrain instability sources at Novice tier
- failed Equilibrio check provides no benefit

---

### Fijar el Umbral

| Field | Value |
| --- | --- |
| `name` | Fijar el Umbral |
| `name_en` | Fix the Threshold |
| `origin` | Agarre |
| `world_origin` | Species: Naghii; seed: Archive Arrest; transmission: temple guard hold and access point drills; availability: Restricted |
| `category` | utility |
| `type` | reactive |
| `trigger` | An enemy at close range attempts to move away, disengage, withdraw, or pass through the user's position — fires even when the movement explicitly declares it does not provoke reactions. |
| `requirements` | Minimum rank: Novice; Agarre at Novice or higher; user at close range with the target; user has a free gripping limb, tail, or coiled body segment; user is not fully restrained or immobilized |
| `target` | enemy |
| `range` | close |
| `area` | single |
| `duration` | until Atrapado is removed |
| `cost` | Rhythm 4; Attrition 1 |
| `saving_roll` | `R.R.` reduces — on a successful Alteration Resistance Roll, Atrapado is not applied and the movement proceeds normally |
| `tags` | utility, control, hold, pressure |

**Fantasy:** The target shifts weight to leave. The Naghii has already decided they are not going. The grip closes at the point of departure — before the exit is complete, before the safe window opens — and holds. The motion stops where the hold lands.

**World origin:** Naghii archive guard training treats exit control as a formal discipline: a guard does not pursue an escaping target, they hold the point of consequence. The specific skill taught is grip application at the exit moment — not during the movement but at its departure threshold, before the step is committed. This is why the technique fires even on exits that would ordinarily deny a reaction window: the hold is already placed when the movement begins.

**Why this is not raw Agarre:** Raw Agarre use produces narrative hold and positioning control without a defined mechanical condition. `Fijar el Umbral` applies `Atrapado` through the Alteration R.R. system — a gated condition with defined recovery mechanics — and uniquely fires against movement that explicitly does not provoke reactions.

**Primary interaction surface:** reactive hold application at the moment of exit — Atrapado on a failed Alteration R.R.

**Secondary interaction surface:** override permission — fires against declared no-reaction movement, denying a class of safe exits that most reactives cannot reach.

**Cost note:** `Rhythm 4 / Attrition 1` is deliberate. Trabar el Gesto (Rhythm 5) negates the triggering action outright on a failed R.R. Fijar el Umbral applies `Atrapado` — a condition the target can clear on subsequent turns through an Agarre S.R. or an action spent. The narrower outcome justifies the lower cost. The override permission prevents further reduction: firing against declared no-reaction movement is a meaningful advantage the R.R. gate and the condition's recoverable nature balance against.

**Effect:** Make an Agarre check against the triggering enemy. On success, the target must make an Alteration Resistance Roll.

The `Atrapado` severity is determined by the Agarre rank used for the Technique:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe
- Higher ranks continue this progression if the system later defines higher severity bands.

On a failed R.R., the target gains `Atrapado` at that severity: movement is reduced to 0 and the target suffers the normal Atrapado penalties for that severity. `Atrapado` persists until the target succeeds on an Agarre Specialization Roll against the original severity at the start of its turn or spends an action to break free. On a successful R.R., the movement proceeds normally and `Atrapado` is not applied.

This Technique may be declared against movement that explicitly states it does not provoke reactions — the grip is placed at the departure threshold before the safe-exit window opens.

**Restrictions:**

- user must be at close range with the target when the trigger occurs
- user must have a free gripping limb, tail, or coiled body segment
- applies to one target only
- does not deal damage
- does not prevent the target from using non-movement actions while Atrapado
- does not function when user is fully restrained or immobilized
- does not function against targets with no grippable anatomy (fluid forms, incorporeal entities)
- Atrapado is removed by a successful Agarre S.R. against the original severity at the start of the target's turn or by spending an action

---

## Next Design Layer

This document defines the Technique skeleton.

The next required layer is:

- **competency technique domains**

That layer defines what kinds of Techniques each competency is structurally suited to produce.

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

### Nothing from nothing

No Technique should survive authoring as a purely mechanical outcome with no
clear material or functional cause.

Every finished Technique should let the reader answer:

- what body part, weapon, tool, kit, residue, angle, or carried object is
  doing the work;
- what trained handling or timing makes that effect possible right now;
- and why that result belongs to a live exchange instead of a vague narrative
  assumption.

This matters especially for effects involving:

- marks;
- residues;
- contamination;
- route alteration;
- sensory tagging;
- improvised barriers;
- projectile payloads;
- or any result that could otherwise read like “the rule says so.”

If the author cannot point cleanly to the cause, the Technique is not ready
yet.

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
6. What specifically is doing the work: body, weapon, kit, residue, terrain, angle, or trained handling?
7. If this effect looks like preparation rather than live exchange, does it actually belong somewhere else?

If the answer to `3`, `4`, `5`, `6`, or `7` is no, the Technique is drifting out of bounds.

### Trap boundary rule

Do not keep a concept in Techniques if its strongest version is really:

- a prepared hazard;
- a delayed crossing punishment;
- a pre-placed route denial;
- a baited step-trigger;
- or any other effect that works better as setup than as live trained action.

If the concept becomes more convincing when authored as:

- trap placement;
- trap arming;
- battlefield preparation;
- route conditioning before contact;
- or other delayed hazard logic

then it should usually move to **Traps**, scene preparation, or another setup
layer instead of staying in the Technique catalog.

Techniques may still punish:

- an entry happening right now;
- a process already in motion;
- a live crossing attempt inside the current exchange;
- or a bad immediate choice under pressure.

But they should not become disguised trap diagrams.

### Procedural states are not automatically Ailments

Not every temporary mechanical state created by a Technique should become an
`Ailment`.

Use a **procedural state** when the Technique is primarily changing:

- an object;
- a tool;
- a held piece;
- a route;
- a declared line;
- a sensory channel;
- a mark;
- a residue;
- a read;
- or a short tactical relation between two actors.

These are usually not bodywide conditions. They are:

- bounded;
- local;
- materially caused;
- and dependent on one exact thing still being true.

Good procedural-state examples include:

- `read-marked`
- `signal-blurred`
- `wound-fouled`
- `badly-seated`
- `displaced`
- `read-spoiled`
- `wrong-answered`
- `step-checked`

Use an **Ailment** when the Technique establishes a real ongoing condition in
the target's body, nervous system, posture, perception, or operational
capacity, such as:

- fear;
- imbalance;
- knockdown;
- restraint;
- impaired weapon execution;
- blindness;
- overload;
- concussion;
- freezing;
- or another state the body is now actually suffering.

As a rule of thumb:

- if the effect stops mattering because one exact piece, line, channel, or mark
  is no longer relevant, it is probably a procedural state;
- if the effect continues because the target's body or operative condition has
  been altered, it is probably an `Ailment`.

Do not migrate a procedural state into `Ailments` just because it has a
penalty. Migrate it only when the fiction has crossed from:

- object/process/read disruption

into:

- actual bodily or operational alteration.

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

## Defense Families

Pure defensive Techniques in Transcendence should be authored from only two
mechanical families:

- `evasion`
- `mitigation`

This matters more than treating every defensive competency as if it were a
separate school.

### Evasion family

The evasion family includes:

- `Evasion`
- `Light Armor`

`Light Armor` belongs here on purpose.

Light armor is not a smaller version of medium or heavy mitigation. Its job is
to preserve:

- `D.R.`
- mobility
- angle change
- peel-outs
- recovery into another action

while still contributing some `Bloqueo` if a defended line is not fully
avoided.

So a `Light Armor` Technique should usually feel like:

- slipping the line
- denying clean purchase
- changing angle
- keeping movement alive
- or converting a successful defense into better immediate position

not like:

- bracing to absorb
- turning the body into a wall
- or trusting the armor to hold the impact directly

### Mitigation family

The mitigation family includes:

- `Medium Armor`
- `Heavy Armor`

These Techniques are about surviving contact through:

- `Bloqueo`
- posture
- weight
- impact correction
- seam management
- reduced wound severity
- and preserving structure under pressure

So a mitigation Technique should usually feel like:

- receiving better
- presenting the right plate
- reducing what gets through
- preventing breakage
- or staying whole under force

not like a last-second evasive peel.

### Authoring rule

When writing a pure defense Technique:

1. decide whether the Technique wins by `avoiding` or by `receiving better`
2. if it avoids, place it in the `Evasion / Light Armor` family
3. if it receives better, place it in the `Medium Armor / Heavy Armor` family

Do not author `Light Armor` as a mini-mitigation school.
Do not author `Medium` or `Heavy` as disguised evasive tricks.

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

### Optimization rule

Base actions are allowed to remain:

- reliable
- simple
- broadly available
- sometimes the correct conservative choice

But they should almost never be the **most efficient learned answer** once a
character has a relevant authored Technique for the same moment.

In practice:

- a base attack should not be the superior repeated choice over a learned attack Technique that targets the same tactical problem;
- a base defensive answer should not outshine a learned reactive Technique meant for that threat family;
- and a base utility action should not solve a specialized pressure problem more cleanly than the Technique written to own that space.

This does **not** mean every Technique must strictly outdamage or outvalue the
base action in every scene.

It means a learned Technique should usually provide at least one of the
following over the base action:

- better tactical shaping
- stronger thematic identity
- clearer permission
- narrower but more decisive answer quality
- better conversion of a specific trigger into an outcome
- superior follow-up leverage

If a Technique is less expressive **and** less efficient than the base action it
competes with, it is probably under-authored, under-costed, or solving the
wrong problem.

### Calibration against base actions

Base actions therefore **do** matter when judging `Rhythm` and `Attrition`, but
they should be used as a **floor calibration**, not as a parallel optimization
track.

Use them to ask:

- is this Technique asking the player to pay more than a base action while giving too little differentiation back?
- is this Technique so cheap that it makes the base action irrelevant in every normal case?
- is this Technique occupying the same tactical space as a base action without earning its extra identity?

Do **not** use them to ask:

- should every Technique be only a small numerical upgrade over Attack?
- should base actions and Techniques compete for the same “best DPR” slot?

The intended relationship is:

- base actions = common floor
- Techniques = authored reward language

### Pending core sync

The current base-action costs in the corebook remain usable for play, but this
document now treats them as a calibration reference that may need later
realignment.

Pending follow-up:

- review `01-actions` in the corebook so base-action cost presentation matches the intended “fallback, not optimal line” doctrine.

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

## Specialization Technique Rule

Specialization Techniques should not be written as generic uses of the specialization plus a name and some numbers.

They should be authored by extracting the **trained capabilities** that the specialization actually develops, then translating those capabilities into a bounded thematic mechanical expression.

For the current species-novice authoring pass, those expressions should usually land in:

- combat
- exploration

not in pure abstract social-scene resolution unless a species concept explicitly requires that exception.

Examples:

- `Nadar` should usually become propulsion, flotation, orientation under pressure, breath timing, yielding without losing control, or recovering through a resisting medium
- `Tolerancia` should usually become ordered function under pain, wound pressure, poison burden, or Fatigue strain rather than passive toughness
- `Arquitectura` should usually become threshold logic, structural intent, fault reading, or controlled access rather than a generic knowledge bonus

The question is not:

- can this specialization be rolled here?

The question is:

- what specific trained method from this specialization becomes a Technique?

If the answer is only "it does the specialization better," the Technique is not ready yet.

### Required authoring order

For any Specialization Technique, follow this order:

1. Identify the specialization.
2. Extract the concrete trained capabilities that the specialization develops.
3. Choose one capability, or one tightly coherent pair, as the Technique root.
4. Translate that root into a bounded combat or exploration mechanic.
5. Validate the mechanic against existing system surfaces, Ailments, costs, and action vocabulary.

Do not skip step 2.

If the author cannot name the extracted capability before writing the effect text, the Technique is not ready.

### Specialization Extraction Catalog

This catalog exists so that Specialization Techniques are authored from trained methods rather than from the superficial theme of the specialization.

Each entry lists the kinds of capabilities that can be extracted and turned into Techniques.

These extracted capabilities should usually be understood as:

- transferable trained patterns
- not literal profession actions
- usable outside the original trade or scene type
- still bounded by the kind of objects, bodies, materials, or pressures that the specialization actually trains

The key distinction is:

- bad extraction: "this Technique is about doing Minería"
- good extraction: "this Technique uses a transferable precision or material-reading habit learned through Minería"

### Transferability rule

An extracted capability should usually be broader than the profession itself.

It should describe a trained way of:

- noticing
- timing
- shaping
- reading
- controlling
- preserving
- extracting
- stabilizing
- interpreting

not merely the profession's headline task.

### Domain-boundary rule

Transferable does **not** mean universal.

A capability may travel outside its original profession, but only into situations where the training still makes sense.

Examples:

- a `Minería`-derived material-reading capability may apply to stone, packed earth, masonry, ore, or other mineral-bearing structures
- that same capability should not automatically read anatomy, social tells, or aura patterns, because Minería does not train those surfaces
- a `Medicina`-derived stabilization capability may apply to bodies, wounds, and physical trauma
- that same capability should not automatically apply to walls, rituals, or mining seams

When authoring, always ask:

- what is the transferable trained pattern here?
- what surfaces did this specialization actually train that pattern on?
- what surfaces are outside that training and therefore off-limits?

#### Fuerza

- `Saltar`: explosive release, force-to-space conversion, launch-window commitment, clearance judgment, short-burst body projection
- `Trepar`: support testing, progressive load transfer, body-weight distribution, sustained traction sequencing, hanging recovery
- `Lanzamiento`: body-to-object force transfer, release discipline, trajectory framing, timed delivery, remote placement by projection
- `Nadar`: propulsion, flotation, orientation under pressure, respiratory pacing, yielding without losing control, escape through resisting flow
- `Agarre`: contact anchoring, pressure retention, leverage finding, slip correction, escape closure

#### Agilidad

- `Acrobacias`: momentum redirection, continuous-body sequencing, inversion recovery, obstacle threading, dynamic recovery through motion
- `Destreza`: micro-placement control, fine-pressure calibration, sequence-clean manipulation, constrained-access handling, error-minimizing handwork
- `Equilibrio`: posture correction, center-line recovery, unstable-base adaptation, anti-overcommit stabilization, narrow-support continuity
- `Equitación`: moving-platform synchronization, distributed control through reins and weight, mounted line correction, shared turn timing, stability through another body's motion

#### Tenacidad

- `Marcha`: sustained pacing, load distribution, distance efficiency, cadence preservation, recovery while advancing
- `Aclimatación`: exposure normalization, physiological adjustment under hostile conditions, environmental strain dampening, breathable continuity in bad air or climate, adaptation carryover
- `Tolerancia`: pain ordering, function preservation under active burden, degradation partitioning, shock resistance, physiological continuation under failure pressure

#### Astucia

- `Orientación`: bearing reconstruction, route-option pruning, reference anchoring, directional correction under uncertainty, spatial fallback selection
- `Rastreo`: disturbance isolation, continuity reconstruction, freshness discrimination, passage-pattern reading, likely-route continuation
- `Intuición`: latent-pattern calling, concealed-intent suspicion, threshold-of-danger recognition, incomplete-signal commitment, wrongness discrimination
- `Engaño`: false-frame construction, selective truth shaping, expectation steering, confidence borrowing, reaction baiting
- `Improvisación`: function recovery from bad resources, ad-hoc method assembly, constraint inversion, stopgap conversion, tempo-first solutioning
- `Hurto`: opportunity extraction, unnoticed transfer, access-window exploitation, possession redirection, withdrawal before registration

#### Sabiduría

- `Percepción`: signal segregation, anomaly discrimination, attention reindexing, partial-pattern completion, early-contact registration
- `Supervivencia`: viable-option discrimination under adversity, pressure-prioritized decision sequencing, low-infrastructure continuity, scarcity budgeting, fallback-line selection
- `Medicina`: instability triage, function-preserving intervention, bodily-state discrimination under pressure, escalation-threshold recognition, timed stabilization entry
- `Herboristería`: living-source property discrimination, safe extraction from organic material, effect-to-need matching, crude field preparation, contamination avoidance
- `Alquimia`: reactive balance control, staged combination sequencing, volatility-window judgment, effect stabilization under mix pressure, transformation containment
- `Trampas`: trigger-path reading, response-chain anticipation, concealed placement logic, disarm-sequence isolation, zone-commitment shaping
- `Minería`: material detail discrimination, stress-signature reading, fault-line isolation, force-entry precision, load-path judgment
- `Herrería`: heat-state discrimination, force-shaped correction, structural joining discipline, fatigue-point reading, stress-repair sequencing
- `Sastrería`: tension-line management, layered-fit calibration, seam-path planning, reinforcement placement, silent-profile preparation
- `Joyería`: micro-secure placement, small-scale force discipline, component-seating precision, fine-material discrimination, concealment through ornament
- `Ingeniería`: mechanism-state reading, load-path modeling, sequence-dependent assembly, failure-cascade anticipation, function reassignment through structure

#### Intelecto

- `Identificación`: feature-to-class mapping, category narrowing through exclusion, known-unknown discrimination, specimen comparison, recognition under incomplete evidence
- `Interpretación`: implication extraction, pattern linkage, structural inference, meaning reconstruction from arrangement, context-weighted resolution
- `Lingüística`: grammar-state recognition, script-pattern decoding, root-family comparison, formal-message reconstruction, language transfer through structural similarity
- `Taumaturgia`: tauma-law reading, manifestation-state classification, arcane-pattern inference, interaction forecasting, instability recognition under exposure
- `Historia`: precedent retrieval, era-signature discrimination, continuity reconstruction across events, institutional-pattern recognition, present-case comparison to known past structures
- `Geografía`: region-scale spatial modeling, terrain-system linkage, climate-pressure projection, route-network inference, place-relationship reconstruction
- `Astronomía`: celestial-pattern fixing, cycle-state timing, sky-reference anchoring, long-cycle projection, anomaly discrimination in celestial motion
- `Teología`: doctrine-structure reading, ritual-role inference, sacred-protocol sequencing, symbol-authority discrimination, devotion-frame reconstruction
- `Criptología`: encoded-pattern isolation, transformation-rule inference, substitution-chain detection, hidden-message reconstruction, signal masking through formal structure
- `Arqueología`: deposition-sequence reading, fragment-context reconstruction, disturbance discrimination, layer-to-event inference, site-use continuity modeling
- `Arquitectura`: threshold-function reading, structural-intent inference, circulation-path modeling, load-path discrimination, access-control logic reconstruction
- `Belicología`: force-role composition reading, engagement-phase modeling, doctrine-signature discrimination, threat-ordering under conflict pressure, battle-pattern projection

#### Compostura

- `Enfoque`: attention-channel narrowing, task-line retention, interruption filtering, precision continuity under pressure, target-lock persistence
- `Contención`: internal surge partitioning, breakdown-threshold holding, impulse-output gating, escalation arrest, functional continuity under emotional overload
- `Meditación`: state-baseline restoration, breath-led regulation, internal noise settling, recovery-entry sequencing, long-cycle self-stabilization
- `Aplomo`: visible-strain suppression, bearing-line preservation, pressure-sign leak control, external steadiness projection, read-denial through posture discipline

#### Aura

- `Instinto`: preconscious threat registration, essence-led orientation, immediate choice before analysis, nonrational salience discrimination, survival-line commitment
- `Resonancia`: active aura reach, signal attunement, affinity-discrimination through contact, field-state sampling, nonverbal force-reading
- `Vínculo`: bonded-state awareness, tether persistence across separation, relational direction-finding, shared-pressure registration, connection-stability management
- `Domesticación`: response-state calming, cue-to-response imprinting, trust-window shaping, instinct-channel redirection, creature-state reading under agitation

#### Presencia

- `Liderazgo`: authority-line projection, group-tempo synchronization, directive clarity under pressure, role-pressure distribution, cohesion restoration through command
- `Negociación`: leverage-surface mapping, concession-window shaping, term-pressure calibration, interest-line alignment, agreement-path structuring
- `Intimidación`: threat-weight projection, consequence salience forcing, will-pressure concentration, space-claim enforcement, hesitation induction
- `Imitación`: identity-pattern copying, vocal-and-behavioral mirroring, social-rhythm reproduction, borrowed-mannerism control, role-presence adoption
- `Sigilo`: attention-threshold reduction, profile suppression, registration-window timing, line-of-notice disruption, trace-sign minimization

### Catalog use rule

The catalog is not a generator of free bonuses.

It is a constraint:

- pick the specialization
- pick the extracted capability
- build the Technique from that capability
- preserve its trained domain boundary

If a proposed Technique cannot point to one of these extracted capabilities, or to a clearly adjacent capability that should be added here first, the Technique should not be authored yet.

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

### Discovery rule

Techniques are **not** a free-pick catalog.

A character does not gain access to a Technique merely because:

- the player knows it exists;
- the Technique appears somewhere in the authored corpus;
- or the character now meets its rank, competency, or equipment prerequisites.

Those prerequisites determine whether the character **could** learn and use the
Technique correctly. They do **not** place the Technique in the character's
hands automatically.

To become learnable, a Technique must first be encountered through the world.

Valid encounter paths include:

- a living teacher, order, school, or training body;
- a manual, scroll, archive record, or technical document;
- observation of a real execution that the character can later study;
- ritual, doctrinal, or factional initiation;
- rediscovery through ruins, fragments, inscriptions, or preserved remains;
- exchange, purchase, barter, or political access to someone who holds it.

This means the full authored catalog is part of worldbuilding, not a player
menu. Many Techniques in the setting may be:

- inaccessible to the current group;
- discoverable only through exploration;
- legible but unusable until the right competency is trained;
- usable but culturally, politically, or materially difficult to obtain;
- or valuable as trade, leverage, scholarship, or factional currency even if
  the current character cannot execute them.

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
- `focus`: the functional sphere the Technique serves inside that front, broad enough to stay reusable across different institutions
- `source`: the people, doctrine, order, region, or tradition that created it
- `holder`: optional but strongly recommended; the concrete order, lineage, patrol, archive, shrine, crew, caste, or community that currently transmits it
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

If a Technique affects a creature's body, pressure, position, visibility, or ongoing function, always validate the existing system first:

- `docs/system/ailments.md`
- `data/system/ailments.yaml`
- `docs/system/mechanics-overview.md`
- `Transcendence-publications/canon/glossary.md`

Do not leave creature-affecting effects as vague statements like:

- "the target is hindered"
- "the enemy is pressured"
- "the creature is slowed somehow"

when the real effect should be carried by an existing named mechanic such as:

- an Ailment
- Fatigue pressure
- Wound pressure
- Cover / Concealment
- forced movement
- rhythm change
- a named roll penalty

If the system lacks the needed state, create that mechanic in the proper system layer first and register it before treating it as Technique text.

Species-origin Techniques may explain why the method exists, but the condition name should remain generic if the state can be caused by many sources.

When a Technique applies an Ailment through an `R.R.`, its default scaling should usually increase Ailment severity by competency rank bands:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe

Some Ailments use severity mainly to determine application pressure or recovery difficulty rather than changing the ongoing effect. That is still valid scaling.

### System validation rule

Before finalizing a Technique, validate that it is actually using the system's named mechanics rather than collapsing into generic action language.

Always check:

- `Transcendence-publications/canon/glossary.md`
- `docs/system/mechanics-overview.md`
- `docs/system/technique-interaction-framework.md`

Ask:

1. Which named system surfaces does this Technique touch?
2. Which existing roll, state, cost, condition, or timing vocabulary is carrying the effect?
3. If this reads like move / attack / dodge / intercept, what specific system layer makes it distinct here?

If the answer is "none yet," the Technique is still underdefined.

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

- `Armor + fire-origin Vulnerability/Resistance trait` is valid
- `Tolerance + Poison Resistance` is valid
- `Resonance + Affliction Resistance` is valid
- a standalone fire-resistance Technique with no other trained origin is not valid

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

### Weapon profile requirement rule

For Weapon Techniques, the profile is the primary access gate.

If a Technique requires `weapon profile: X`, every weapon competency, natural attack form, or specific item that grants profile `X` can use that Technique unless the Technique or item explicitly narrows access.

Equipment, anatomy, ammunition, delivery method, or body-position language should not replace the profile requirement. Those details belong as state constraints or narrowed-access clauses.

Use narrowed access only when the Technique needs something the profile does not guarantee by itself.

Examples:

- A normal `Impact` Technique should require `weapon profile: Impact`, not "mace, tail, club, hammer."
- A marking shot can require `weapon profile: Precision`, then narrow access to attacks that can leave a readable physical mark.
- A restraint Technique can require `weapon profile: Interruption`, then narrow access to surfaces that can actually catch, bind, or restrain movement.

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

### Procedural countermeasure standard

Some Techniques do not mainly pressure through direct damage, raw denial, or a
named Alteration severity. Instead, they create a **procedural problem** that
must be answered before the target can recover a clean operating state.

Typical examples:

- residue that must be cleaned
- a wound that must be bound or flushed
- a line that must be inspected before safe passage
- a restraint that must be disentangled
- an irritant that must be cleared
- a signal or mark that must be identified before the right response is possible

When a Technique uses this kind of pressure, it should not invent a bespoke
mini-action every time. It should usually resolve through the existing base
actions framework:

- **Interact** when the answer is mostly physical and immediate
- **Use Specialization** when the answer needs trained reading, treatment, or handling

Then it should point to one of the standard countermeasure patterns below and narrow:

- who can perform it
- what specialization or roll it uses
- what tools are needed
- whether self-use is allowed
- whether the source must also be removed

Do not leave all countermeasure routes implicitly open by default. The authored
Technique should declare which route actually clears the state:

- one exact route
- or one primary route plus one clearly justified secondary route

If no separate substance, diagnosis layer, or technical handling requirement is
present in the fiction, prefer the narrower route.

#### Countermeasure patterns

| Pattern | Typical use | Default cost under active threat |
| --- | --- | --- |
| `self_clear` | The affected target spends time cleaning, bracing, scraping, flushing, disentangling, or otherwise restoring its own immediate function | `Rhythm 3 / Attrition 1` |
| `aided_treatment` | Another creature, or the target with proper tools and careful handling, treats the problem in a more reliable or technical way | `Rhythm 6 / Attrition 1` |
| `quick_identification` | A fast read to learn what kind of countermeasure is needed before acting blindly | `Rhythm 3 / Attrition 1` |

These are defaults, not hard locks. A specific Technique may narrow, exclude, or
raise them when the fiction clearly earns it.

#### Authoring rule

Use a procedural countermeasure when all of the following are true:

1. the target still has a believable way out
2. the Technique's value comes partly from forcing time, care, or attention
3. the state should not be treated as full passive persistence with no answer
4. the answer is practical, medical, positional, sensory, or technical rather than purely mental

#### Default cost guidance

- Use `self_clear` when the answer is quick, local, and mostly about stopping to
  deal with the problem.
- Use `aided_treatment` when the answer needs tools, help, technique, or careful
  handling on a real target.
- Use `quick_identification` when the problem is not simply "remove it" but
  "understand what this is before acting."

Outside `ATB` or another active-threat scene, these usually stop costing
`Attrition` and resolve as ordinary bounded scene actions unless the specific
Technique or condition says otherwise.

#### Why this exists

Without this standard, authored Techniques tend to drift into:

- vague "spend some time fixing it" prose
- effects with no clean exit
- or custom micro-rules that all do the same kind of timing tax differently

This standard keeps those Techniques legible and reusable while still letting
the actual fiction decide whether the answer is `Medicina`, `Destreza`,
`Contención`, `Agarre`, `Rastreo`, or something else.

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
| `category` | defense |
| `type` | reactive |
| `trigger` | An enemy advances into your line or tries to convert forward movement into immediate melee contact against you. |
| `requirements` | Minimum rank: Novice; weapon profile: Perforation; any weapon competency, natural attack form, or specific item that grants Perforation access can use this Technique unless the Technique or item says otherwise; user must be able to sustain a committed piercing line |
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
| `trigger` | The user declares a protective stance, holding ground to cover nearby allies. |
| `requirements` | Minimum rank: Novice; weapon profile: Line Control; profile-bearing weapon with a defined reach; user must remain stationary while the stance is active |
| `target` | self |
| `range` | self |
| `area` | allies within weapon reach + 1 |
| `duration` | until the user moves |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | none |
| `tags` | defense, stance, taunt, zone_protection, control |

**Fantasy:** The user does not wait for the enemy to choose a target. They set the shield like a stone gate in a canal, making one route costly to ignore. The enemy can still force the issue, but no longer treats the protected side as open water.

**World origin:** Sauri river-wardens and temple guards train with the same logic their architects use in canals and sealed chambers: pressure must meet the correct gate before it becomes flood. In shield practice, that doctrine becomes an active claim over the route.

**Why this is not a base profile-bearing defense:** A base profile-bearing defense protects against a strike aimed at the user after the strike is declared. `Cerrar la Compuerta` claims a zone around the user and taxes attacks against allies within it — a different surface: not personal interception, but zone taunt.

**Primary interaction surface:** zone taunt — holding ground makes targeting allies in the zone a worse decision than attacking the user directly.

**Secondary interaction surface:** ally protection, because the penalty degrades enemy efficiency against nearby targets without fully blocking access.

**Cost note:** `Rhythm 3 / Attrition 1`. Declared stance with no roll and no route selection. The low cost reflects that its benefit is conditional: it only activates when enemies choose to attack allies through the zone rather than the user.

**Effect:** Declare the stance. While active, all attacks targeting allies within [weapon reach + 1] of the user suffer a penalty to their Attack Roll equal to the user's rank in the competency used for this Technique. This makes targeting the user directly the more efficient option. The stance ends when the user moves.

**Zone radius:** weapon reach + 1 (fixed — does not scale with rank). A shield with melee reach covers allies within short reach; a weapon with short reach covers allies within medium reach.

**Penalty:** equal to the user's competency rank — at Novice: −1 T.A.; at Adept: −2 T.A.; up to Transcendent: −6 T.A.

**Restrictions:**

- requires a profile-bearing weapon with a defined reach
- zone radius is weapon reach + 1 and does not scale with rank
- penalty applies only to attacks targeting allies, not the user
- ends immediately when the user takes a movement action
- does not prevent enemies from attacking allies through the zone
- does not stack with another copy of the same stance

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
| `trigger` | An enemy attack or movement-linked strike would reach an ally, protected creature, carried witness, relic, or designated charge within your profile-bearing surface reach. |
| `requirements` | Minimum rank: Novice; weapon profile: Interception; any weapon competency, natural attack form, or specific item that grants Interception access can use this Technique unless the Technique or item says otherwise; user must have a clear physical path to place the profile-bearing surface between the threat and the protected target |
| `target` | ally / creature / object |
| `range` | profile-bearing surface reach |
| `area` | single protected target |
| `duration` | instant |
| `cost` | Rhythm 4; Attrition 1 |
| `saving_roll` | contextual - resolved through the hostile attack or movement-linked strike that the Technique intercepts |
| `tags` | defense, interception, support, mitigation |

**Fantasy:** The user raises the shield before the blow finishes its course, not as a wall for themselves but as a dike for someone or something that must not be reached. The attack still has force, but the force meets the prepared surface instead of the intended target.

**Effect:** Contest the triggering attack or movement-linked strike with a shield response. If the Technique resolves successfully, the attack does not affect its intended target. The profile-bearing user becomes the point of contact for the hostile force; the attack is blocked, redirected, or resolved against the user's profile-bearing defense as the scene requires.

If the intercepted attack carries a non-damage rider, such as forced movement, a condition, or a grab, that rider does not transfer automatically to the protected target. The Narrator resolves whether the rider can affect the profile-bearing user based on the fiction of the contact.

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
| `category` | defense |
| `type` | reactive |
| `trigger` | An enemy within profile-bearing surface reach begins a Technique, heavy action, telegraphed action, or movement-linked execution that requires visible commitment before it resolves. |
| `requirements` | Minimum rank: Novice; weapon profile: Interruption; any weapon competency, natural attack form, or specific item that grants Interruption access can use this Technique unless the Technique or item says otherwise; user must have a ready weapon, natural weapon, or item with explicit attack stats to deliver the counter; the enemy's action must have a readable physical line, windup, focus point, or route of execution the profile-bearing surface can strike or jam |
| `target` | enemy |
| `range` | profile-bearing surface reach |
| `area` | single enemy |
| `duration` | instant |
| `cost` | Rhythm 6; Attrition 2 |
| `saving_roll` | D.R. contest; counter requires clean defensive margin |
| `tags` | attack, defense, disruption, counter_positioning |

**Fantasy:** The user does not wait behind the shield. They drive the shield into the moment where the enemy's action has begun but has not yet become inevitable. If the current breaks completely against the shield, the user's answering strike lands before the enemy can rebuild the flow.

**Effect:** Contest the triggering execution with a shield-based `D.R.`. If the enemy's attack or execution still beats your `D.R.`, the Technique fails and the enemy resolves normally.

If your `D.R.` equals or exceeds the enemy's relevant attack or execution roll, the shield breaks the execution cleanly. The enemy's action still consumes its declared Rhythm and any declared cost, but it does not damage you through that contact.

If your `D.R.` exceeds the enemy's roll by **3 or more**, you may immediately make one counterattack against that enemy with one ready manufactured weapon, one natural weapon, or a shield item that has explicit attack stats. Resolve the counterattack normally with its own `A.R.` and `I.R.`. This counterattack does not add another Rhythm cost, but it cannot include movement, a second Technique, or a follow-up window.

If the triggering action was a telegraphed action rather than a direct attack, the Narrator uses the same margin logic against the action's relevant execution roll, fixed threat value, or declared interruption threshold. If no such value exists, this Technique can spoil the setup but cannot produce the counterattack.

**Restrictions:**

- requires a readable committed execution; cannot be used against trivial, instant, hidden, or purely mental actions with no blockable line
- requires profile-bearing surface reach and a credible contact point to jam, strike, or break
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
| `requirements` | Minimum rank: Novice; weapon profile: Bastion; any weapon competency, natural attack form, or specific item that grants Bastion access can use this Technique unless the Technique or item says otherwise; user must be standing, able to brace, and able to keep the profile-bearing surface oriented toward the pressure being held |
| `target` | self |
| `range` | self |
| `area` | anchored point |
| `duration` | sustained while anchored |
| `cost` | Rhythm 7; Attrition 2 |
| `saving_roll` | none |
| `tags` | defense, stability, mitigation, anti_displacement |

**Fantasy:** The user settles into the ground like fitted stone. They are not doing nothing. They are making one place harder to take from them.

**Effect:** Choose the point or small space you are anchoring. While the stance remains active, you gain a bonus equal to the rank bonus of the competency used for this Technique to:

- `D.R.` against attacks that come through your profile-bearing line or the anchored front
- `R.R.` against forced movement, knockdown, shove, drag, destabilization, crushing pressure, and physical Alterations caused by impact or bodily displacement

You may still attack, use Techniques, intercept, speak, pressure enemies, and defend while the stance is active, as long as those actions do not make you abandon the anchored point or break profile-bearing posture.

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
| `requirements` | Minimum rank: Novice; weapon profile: Impact; any weapon competency, natural attack form, or specific item that grants Impact access can use this Technique unless the Technique or item says otherwise; user must be able to close force into the target through a credible Impact surface |
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

### Barrer la Orilla

| Field | Value |
| --- | --- |
| `name` | Barrer la Orilla |
| `name_en` | Sweep the Bank |
| `origin` | Impact |
| `world_origin` | Species: Sauri; seed: Tail Keeps The Channel / Procession Of Force; transmission: riverbank impact drills, corridor breach punishment, and canal-guard body-line training; availability: Restricted |
| `category` | attack |
| `type` | active |
| `trigger` | You make a committed Impact-profile tail or heavy lateral strike against a target within reach whose posture can be disrupted by blunt side force. |
| `requirements` | Minimum rank: Novice; weapon profile: Impact; any weapon competency, natural attack form, or specific item that grants Impact access can use this Technique unless the Technique or item says otherwise; current manufactured access: Maces; current natural examples: tail slam, shell slam, forelimb smash, headbutt; user must have enough space to swing, pivot, or drive blunt lateral force through the target's stance |
| `target` | enemy |
| `range` | Impact weapon or natural weapon reach |
| `area` | single enemy |
| `duration` | until Desequilibrado is removed |
| `cost` | Rhythm 5; Attrition 2 |
| `saving_roll` | On hit, the target makes an Alteration Resistance Roll against Desequilibrado |
| `tags` | attack, disruption, pressure, stability_break |

**Fantasy:** The user does not chase the enemy's center. The blow crosses the edge of their stance and makes the body remember that it was standing on a bank, not on open ground. The hit is not a clean knockdown and not a hold. It is a blunt lateral shock that ruins balance long enough for the exchange to tilt.

**World origin:** Riverbank drills teach Sauri guards to punish the moment a body trusts the edge beside them. In canals and temple corridors, the tail is trained like a moving wall: not to shove everything away, but to make a step, guard, or recovery arrive crooked.

**Why this is not `Sellar la Presa`:** `Sellar la Presa` drives force downward and applies `Derribado`. `Barrer la Orilla` drives force sideways and applies `Desequilibrado`. It does not put the target on the ground and does not claim the fallen point. The pressure is balance damage, not grounded execution.

**Why this is not `Devolver al Cauce`:** `Devolver al Cauce` is reactive and catches movement to apply `Atrapado`. `Barrer la Orilla` is active and hits posture to apply `Desequilibrado`. It does not restrain the target or reduce movement to `0`.

**Primary interaction surface:** blunt lateral impact.

**Secondary interaction surface:** Alteration application through `Desequilibrado`.

**Cost note:** `Rhythm 5 / Attrition 2` is intentional. The Technique is an active attack that resolves normal impact and can apply a persistent stability condition. The Attrition reflects the heavy body commitment needed to swing or drive an Impact-bearing surface through the target's stance without overbalancing the user.

**Effect:** Make an active Impact-profile attack against the target. If the attack hits, resolve damage normally. Then the target makes an Alteration Resistance Roll against `Desequilibrado`.

Use the default Ailment severity bands by rank:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe
- Higher ranks continue this progression if the system later defines higher severity bands.

On a failed R.R., the target gains `Desequilibrado` at that severity.

On a successful R.R., `Desequilibrado` is not applied, but the attack still resolves its normal damage if it hit.

**Restrictions:**

- requires a valid Impact-profile surface capable of blunt lateral shock
- requires enough room, body angle, or contact path to sweep or drive force across the target's stance
- cannot be used with a weapon, natural attack, or item that lacks Impact access unless a specific rule grants that access
- cannot be used with precision piercers, light blades, thrown projectiles, flexible wrapping tools, bites, claws, or other surfaces whose main identity is not blunt structural shock, unless that specific item or anatomy explicitly carries the Impact profile
- does not apply `Derribado`, `Atrapado`, forced displacement, disarm, or rupture by itself
- cannot affect targets whose body plan, anchoring, scale, flight, terrain position, or fiction makes lateral balance disruption impossible
- affects one target only
- applies `Desequilibrado`, a generic Alteration, not a Sauri-only condition

**Authoring note:** This Technique is Sauri-origin but not Sauri-locked. Sauri tail explains the lateral bank-breaking doctrine, while maces and other Impact-profile surfaces can reproduce the same result through blunt side force. It should feel like breaking the enemy's stance sideways, not like a second knockdown Technique.

### Anclar el Contrapeso

| Field | Value |
| --- | --- |
| `name` | Anclar el Contrapeso |
| `name_en` | Anchor the Counterweight |
| `origin` | Line Control |
| `world_origin` | Species: Sauri; seed: Tail Keeps The Channel / Stone Remembers Pressure; transmission: riverbank stance drills, flooded-floor balance practice, and temple threshold holding; availability: Restricted |
| `category` | defense |
| `type` | reactive |
| `trigger` | You would be pushed, pulled, shoved, dragged, knocked off a held point, displaced by a physical effect, or forced to resist `Derribado` or `Desequilibrado` from impact, sweep, collision, footing loss, momentum loss, or unstable ground that your tail or profile-bearing surface can oppose. |
| `requirements` | Minimum rank: Novice; weapon profile: Line Control; any weapon competency, natural attack form, or specific item that grants Line Control access can use this Technique unless the Technique or item says otherwise; narrowed access: the profile-bearing surface must be able to brace, hook, plant, sweep back, or counterweight the user's own body against displacement |
| `target` | self |
| `range` | self |
| `area` | user's occupied space |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | none |
| `tags` | defense, anti_displacement, stability, control |

**Fantasy:** The Sauri is struck, shoved, or dragged, and the tail answers before the body gives way. It does not grab the enemy and it does not declare a lane. It becomes the weight behind the stance: the third point that tells the floor where the body will remain.

**World origin:** Riverbank guards train on wet stone because dry ground lies. A Sauri who can only stand on perfect footing has learned nothing. Tail drills teach the body to make its own bank: when pressure arrives, the tail lowers, hooks, sweeps back, or plants so the body does not leave the place it chose to hold.

**Why this is not `Trazar la Ribera`:** The discarded version taxed enemy movement through a route, which duplicated existing Naghii-style lane control. `Anclar el Contrapeso` does not tax routes at all. It answers forced movement against the user.

**Why this is not `Asentar la Piedra`:** `Asentar la Piedra` is an active Bastion stance that improves anchored defense while it lasts. `Anclar el Contrapeso` is a reactive Line Control answer to a specific displacement event. It does not create a stance, protected route, or ongoing defensive bonus.

**Primary interaction surface:** resisting forced displacement and physical stability loss.

**Secondary interaction surface:** maintaining a held point under physical pressure.

**Cost note:** `Rhythm 3 / Attrition 1` is intentional. The Technique reacts to one physical stability event and can meaningfully preserve position, but it does not damage, apply a condition, protect allies, counterattack, or create persistent control. It is cheaper than full interruption because it only protects the user's own body and only against effects the profile-bearing surface can physically oppose.

**Effect:** When the trigger occurs, reduce the forced movement distance by `1 meter + the rank bonus of the competency used for this Technique`.

If this reduction brings the forced movement to `0`, you remain in your current space and keep any held-point, guard, stance, route, or body-position effect that would have ended only because you were displaced.

If the forced movement is only partially reduced, you are still moved by the remaining distance. You may choose the nearest legal space along the forced movement path that preserves your footing, if more than one legal space is equally valid.

If the same triggering effect would apply `Derribado` or `Desequilibrado` through physical posture loss, impact, sweep, collision, unstable ground, or momentum loss, gain a bonus equal to the rank bonus of the competency used for this Technique to the Alteration R.R. against that `Derribado` or `Desequilibrado`.

If the triggering effect would apply both forced movement and one of those states, apply both parts of this Technique: reduce the movement and add the R.R. bonus.

This Technique can also oppose a physical attempt to knock you off a ledge, pull you out of cover, drag you away from a protected object, or break your position through body displacement. It does not stop non-physical relocation.

**Restrictions:**

- requires a physical displacement or stability-loss effect: push, pull, drag, shove, sweep, collision, forced slide, knockback, impact knockdown, footing loss, momentum loss, unstable ground, or similar body movement
- requires a profile-bearing surface that can credibly brace, hook, plant, sweep back, or counterweight the user's body
- cannot be used against teleportation, spatial transposition, incorporeal movement, mind control, fear movement, voluntary movement, or effects that do not physically move the body
- does not help against `Derribado` or `Desequilibrado` caused by non-physical sources, mental influence, magical command, internal paralysis, sensory overload, or a source the profile-bearing surface cannot physically oppose
- does not help against `Atrapado` once the target is already restrained; it may only oppose the physical drag, shove, pull, or displacement that would put the user into a restraint if that movement is the trigger
- cannot protect another creature by itself
- cannot move the enemy, apply `Atrapado`, apply `Desequilibrado`, apply `Derribado`, deal damage, disarm, or rupture by itself
- cannot preserve a stance, guard, or held-point effect if that effect ended for a reason other than displacement
- cannot reduce forced movement below `0`
- affects the user only

**Authoring note:** This is the tail's Line Control expression: not lane taxation, not spear geometry, and not a shield gate. The Sauri tail governs the user's own body as part of the terrain. Other Line Control surfaces can learn similar anti-displacement methods, but the Sauri version should feel like a living counterweight, not like an abstract movement penalty.

### Cerrar el Flanco

| Field | Value |
| --- | --- |
| `name` | Cerrar el Flanco |
| `name_en` | Close the Flank |
| `origin` | Interception |
| `world_origin` | Species: Sauri; seed: Tail Keeps The Channel / Procession Of Force; transmission: flank-guard tail drills, temple corridor escort forms, and canal-bank body-adjacent defense; availability: Restricted |
| `category` | defense |
| `type` | reactive |
| `trigger` | An enemy within your tail or Interception-surface reach makes a physical attack against you or against a creature/object within that same reach. |
| `requirements` | Minimum rank: Novice; weapon profile: Interception; any weapon competency, natural attack form, or specific item that grants Interception access can use this Technique unless this Technique narrows that access; narrowed access: the profile-bearing surface must have enough reach and striking authority to hit the attacker before their attack reaches the protected target; if protecting a willing creature, that creature must accept that this Technique replaces their T.D. against the triggering attack |
| `target` | attacking enemy |
| `range` | tail or Interception surface reach |
| `area` | one attacking enemy and one protected target |
| `duration` | instant |
| `cost` | Rhythm 6; Attrition 2 |
| `saving_roll` | opposed by the triggering attack roll |
| `tags` | defense, interception, counterattack, protection |

**Fantasy:** The enemy commits to a body beside the Sauri, and the tail arrives first. It is not a shield wall and not a grab. It is a heavy answer across the channel: the attacker reaches for one target and finds the Sauri's tail already crossing the line with enough force to punish the attempt.

**World origin:** Sauri escorts learn that a protected body is not only what stands in front of them. In corridors, along riverbanks, and around temple thresholds, danger often enters through the side. Tail drills teach the flank as a living boundary: the body faces one pressure while the tail strikes the line that tries to pass behind judgment.

**Why this is not `Levantar el Dique`:** `Levantar el Dique` is shield interception: the shield enters the line and can absorb or redirect the hostile force. `Cerrar el Flanco` is offensive interception. The Sauri does not become the defended target. The tail strikes the attacker before the attack lands, replacing the protected target's T.D. with the Sauri's own T.A.

**Why this is not `Devolver al Cauce`:** `Devolver al Cauce` interrupts movement and can apply `Atrapado`. `Cerrar el Flanco` intercepts an attack by striking the attacker. It does not restrain the enemy, stop their movement, or reduce their movement to `0`.

**Primary interaction surface:** replacing a protected target's T.D. with a reactive T.A. from an Interception surface.

**Secondary interaction surface:** counter-damage if the interception succeeds.

**Cost note:** `Rhythm 6 / Attrition 2` is deliberate. The Technique is reactive, can protect another target, and can deal normal damage if the user's attack roll beats the hostile attack. That is stronger than a standard-anchor reactive, but narrower than full heavy scene control, so it sits cleanly at the bridge value between `5` and `7`.

**Effect:** When the trigger occurs, declare whether this Technique is replacing your own T.D. or the protected target's T.D. against the triggering attack.

Make a reactive T.A. with the tail or Interception-profile surface against the attacking enemy. Compare your T.A. to the triggering attacker's T.A.

If your T.A. equals or exceeds the attacker's T.A., the interception succeeds:

- the triggering attack does not hit the protected target
- resolve your attack's damage normally against the attacking enemy
- any non-damage rider on the triggering attack fails to affect the protected target unless a specific rule says it survives failed interception

If your T.A. is lower than the attacker's T.A., the interception fails. The triggering attack resolves against the protected target as if that target's T.D. had failed. The protected target does not make a separate T.D. against that attack.

If the protected target is a willing creature, it must accept the interception before the roll. If it refuses, this Technique cannot replace its T.D. Objects, unconscious creatures, restrained creatures, carried creatures, or creatures unable to defend may be protected if the fiction allows the Sauri to cover the line.

**Restrictions:**

- requires a physical attack or movement-linked strike from an enemy within tail or Interception-surface reach
- requires a profile-bearing surface that can credibly strike the attacker before the triggering attack reaches the protected target
- cannot be used against purely mental, social, aura, curse, poison, infection, area, teleportation, or non-contact effects
- cannot be used against an attack line the user cannot perceive, anticipate, or physically reach
- cannot protect an unwilling creature that is able to defend itself and refuses the replacement
- cannot be used if the protected target already rolled T.D. against the triggering attack
- does not stop enemy movement, apply `Atrapado`, apply `Desequilibrado`, apply `Derribado`, deal damage, disarm, or rupture by itself
- does not automatically make the user the target of the triggering attack
- affects one triggering attack only
- cannot stack with another copy of itself on the same triggering attack; use only the strongest applicable Interception

**Authoring note:** This completes the Sauri tail's novice surface across its four profiles: `Interruption` catches exposed movement, `Impact` breaks posture sideways, `Line Control` anchors the user's body, and `Interception` answers an attack within tail reach by striking first. It should feel like the tail making the side of the body dangerous to attack through, not like a second shield Technique.

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
| `requirements` | Minimum rank: Novice; weapon profile: Rend; any weapon competency, natural attack form, or specific item that grants Rend access can use this Technique unless the Technique or item says otherwise; user must have a tearing edge, hook, bite, claw, or other Rend-bearing surface capable of opening and worsening a contact wound |
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

Use the default Ailment severity bands by rank:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe
- Higher ranks continue this progression if the system later defines higher severity bands.

On a failed R.R., the target gains `Lacerado` at that severity.

On a successful R.R., `Lacerado` is not applied, but the attack still resolves its normal damage if it hit.

**Restrictions:**

- requires a valid Rend-profile surface and a target with material, flesh, protection, binding, hide, or natural armor that can be meaningfully torn
- does not apply to targets without a credible tearable body or structure
- applies `Lacerado`, a generic Alteration, not a Sauri-only condition
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
| `requirements` | Minimum rank: Novice; weapon profile: Unstoppable; any weapon competency, natural attack form, or specific item that grants Unstoppable access can use this Technique unless the Technique or item says otherwise; user must be able to carry force through resistance with the profile-bearing surface |
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

If the target is not guarding, bracing, blocking, holding a line, using a profile-bearing defense, using an active armor posture, or otherwise relying on a defensive posture, resolve the attack as a normal hit with no additional effect.

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

## Bastion Validation Pass

These entries use the Sauri `Mordisco / Bite` species expression as their origin logic, but they are authored through shared Weapon Technique Profiles. A Technique in this section should be executable by any credible weapon or natural weapon with the required `Bastion` profile, such as Sauri bite, mace, weighted haft, heavy striking head, or another Bastion-profile attack surface capable of converting impact/contact into a grounded fall.

### Sellar la Presa

| Field | Value |
| --- | --- |
| `name` | Sellar la Presa |
| `name_en` | Seal the Hold |
| `origin` | Bastion |
| `world_origin` | Species: Sauri; seed: Jaw As Judgment / Sovereign Weight; transmission: jaw-drop drills, mace grounding forms, and temple execution practice; availability: Restricted |
| `category` | attack |
| `type` | active |
| `trigger` | You make a committed Bastion-profile attack against a target whose footing or bodily posture can be broken by grounded force. |
| `requirements` | Minimum rank: Novice; weapon profile: Bastion; any weapon competency, natural attack form, or specific item that grants Bastion access can use this Technique unless the Technique or item says otherwise; user must be able to drive force downward or pin posture into the ground with the profile-bearing surface |
| `target` | enemy |
| `range` | weapon or natural weapon reach |
| `area` | single enemy |
| `duration` | until Derribado is removed |
| `cost` | Rhythm 5; Attrition 2 |
| `saving_roll` | On hit, the target makes an Alteration Resistance Roll against Derribado |
| `tags` | attack, control, stability, knockdown |

**Fantasy:** The user closes force downward and makes the target's posture fail. The important part is not that the target is trapped in a grip; it is that the ground becomes the sealed point. The target is not merely struck. It is made to fall where the user's weight says the exchange ends.

**World origin:** Sauri jaw discipline treats judgment as something that descends. In temple practice, executioners and mace-bearers learn to close a body into the floor the way a stone door closes into its threshold: not by chasing the target, but by making their posture unable to remain upright.

**Why this is not `Fijar el Umbral`:** `Fijar el Umbral` is a Naghii reactive hold that stops departure by applying `Atrapado`. `Sellar la Presa` is an active Bastion attack that breaks posture by applying `Derribado`. It does not keep the target restrained after the fall. The control comes from making the target spend its next movement recovery from the ground, not from holding them in place.

**Primary interaction surface:** grounded knockdown.

**Secondary interaction surface:** positional dominance after a fall.

**Cost note:** `Rhythm 5 / Attrition 2` is intentional. The Technique is a committed attack that redirects force into the target's posture rather than simply trying to hurt them. The higher Attrition reflects the body commitment needed to drive through balance and settle the result into the ground.

**Effect:** Make an active Bastion-profile attack against the target. If the attack hits, resolve damage normally. Then the target makes an Alteration Resistance Roll against `Derribado`.

Use the default Ailment severity bands by rank:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe
- Higher ranks continue this progression if the system later defines higher severity bands.

On a failed R.R., the target gains `Derribado` at that severity.

After applying `Derribado`, you may choose to remain within reach and claim the fallen point. If you do, you gain a bonus equal to your competency rank to the first `D.R.` or physical `R.R.` you make against that target before it stands, but you lose this bonus if you voluntarily move more than 1 meter away, attack a different target, or turn the Bastion surface away from the fallen target.

On a successful R.R., `Derribado` is not applied, but the attack still resolves its normal damage if it hit.

**Restrictions:**

- requires a valid Bastion-profile weapon or natural weapon capable of driving force into posture, balance, or the ground
- cannot be used with shields, armor, or passive defensive surfaces unless those objects are separately defined as weapons with the Bastion profile
- cannot be used with a surface that cannot plausibly knock the target down through grounded force
- affects one target only
- does not restrain, grapple, pin, drag, carry, suffocate, disarm, or create automatic damage over time by itself
- cannot knock down targets whose scale, body plan, state, anchoring, or fiction makes knockdown impossible
- applies `Derribado`, a generic Alteration, not a Sauri-only condition

**Authoring note:** This Technique is Sauri-origin but not Sauri-locked. Sauri bite explains the doctrine through jaw closure and weight, while maces and other Bastion-profile weapons reproduce the same method through grounded mass and follow-through. It should feel like sealing the target into the floor for a moment, not like a generic grapple with a crocodile name.

## Interruption Validation Pass

These entries validate Techniques that break an enemy's process while it is happening. In this section, `Devolver al Cauce` uses the Sauri `Cola / Tail Strike` species expression as its origin logic, but the mechanical surface is the shared `Interruption` profile. It should be executable by any credible restraining surface that can catch movement in the moment it commits: Sauri tail, flexible weapon, hook line, restraining thrown tool, or a shield explicitly designed or trained to trap movement.

### Devolver al Cauce

| Field | Value |
| --- | --- |
| `name` | Devolver al Cauce |
| `name_en` | Return to the Channel |
| `origin` | Interruption |
| `world_origin` | Species: Sauri; seed: Tail Keeps The Channel / Release At The Correct Gate; transmission: river-warden flank drills, canal-guard forms, and temple corridor defense; availability: Restricted |
| `category` | defense |
| `type` | reactive |
| `trigger` | An enemy within tail or interrupting-surface reach attempts to move past your flank, leave your reach through a route you can cover, circle behind you, cross a guarded passage, or complete a movement-linked action through your body-adjacent channel. |
| `requirements` | Minimum rank: Novice; weapon profile: Interruption; any weapon competency, natural attack form, or specific item that grants Interruption access can use this Technique unless this Technique narrows that access; narrowed access: the profile-bearing surface must plausibly restrain or redirect movement, such as a functional Sauri tail, prehensile natural weapon, flexible weapon, hooked line, restraining thrown weapon, or shield with explicit hook/catch/bind permission; user must have a credible contact line to the moving body or limb |
| `target` | moving enemy |
| `range` | tail, flexible, hook, or shield-catch reach |
| `area` | single enemy using the covered passage |
| `duration` | until Atrapado is removed |
| `cost` | Rhythm 4; Attrition 1 |
| `saving_roll` | On successful interruption, the target makes an Alteration Resistance Roll against Atrapado |
| `tags` | defense, control, interruption, movement_denial |

**Fantasy:** The enemy thinks the side is open. The Sauri's tail closes across the passage and returns the body to the channel. This is not a strike for damage; it is a heavy catch at the moment movement becomes exposed. The target is stopped because their path has been taken by the tail.

**World origin:** Sauri guards learn that a canal is only useful if the water cannot choose its own exit. Tail drills teach the same rule around the body: a flank, doorway, bank edge, or corridor side is not empty space if the tail has already claimed the route.

**Why this is not a base tail attack:** A base tail attack hits a target. `Devolver al Cauce` interrupts movement and applies `Atrapado` only when the user's surface can plausibly catch, bind, hook, sweep across, or pin the target's passage. It is not damage and it is not generic lane tax.

**Primary interaction surface:** movement interruption.

**Secondary interaction surface:** Alteration application through `Atrapado`.

**Cost note:** `Rhythm 4 / Attrition 1` is intentional. The Technique is reactive and can stop movement, but it requires a real movement trigger, a credible restraining surface, and an Alteration Resistance Roll. It costs less than a committed disabling attack because it does not deal damage by itself and only fires when the enemy exposes their route.

**Effect:** When the trigger occurs, make a reactive Interruption check using the relevant competency or natural-weapon competency. If the check fails, the enemy completes the movement or movement-linked action normally.

If the check succeeds, the target immediately makes an Alteration Resistance Roll against `Atrapado`.

Use the default Ailment severity bands by rank:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe
- Higher ranks continue this progression if the system later defines higher severity bands.

On a failed R.R., the target gains `Atrapado` at that severity, and the movement or movement-linked action that triggered the Technique stops at the point where the restraint catches them.

On a successful R.R., `Atrapado` is not applied. The target may complete the movement if it still has a legal route, but it does not gain any clean-flank, rear-position, or passage advantage from the triggering movement against the user unless another rule explicitly grants it.

`Atrapado` then follows its normal recovery rules, but if the restraining source no longer physically holds, the condition ends.

**Restrictions:**

- requires a real movement, flank, escape, circling, passage, or movement-linked action to interrupt
- requires a credible restraining or redirecting surface; ordinary swords, maces, daggers, simple spears, axes, armor, and bites do not qualify unless a specific item, anatomy, or Technique grants hook/catch/bind permission
- thrown weapons qualify only when the thrown object can actually restrain, catch, or bind movement, such as a net, bola, weighted cord, hooked line, harpoon-line, or similar tool; a thrown knife, dart, stone, or simple projectile does not qualify
- shield use is allowed only when the shield or shield Technique can plausibly hook, pin, catch, or trap the target's movement; a plain blocking shield does not qualify by itself
- cannot be used if the tail, weapon, shield hook, or restraining surface is already occupied, restrained, pinned, or unable to reach the moving target
- does not affect teleportation, incorporeal movement, flight that clears the restraining surface, or movement that never crosses the user's covered passage
- affects one target only
- does not deal damage, apply Derribado, disarm, or force displacement by itself
- cannot create `Atrapado` without a physical or structural source that continues to restrain the target
- does not stack multiple copies of `Atrapado`; stronger restraint replaces weaker restraint, and equal restraint usually refreshes persistence

**Authoring note:** This Technique is Sauri-origin but not Sauri-locked. Flexible weapons, restraining thrown tools, and some hooked shields can learn the same method, but the Sauri origin explains why the movement is treated as a channel rather than as a simple grab.

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
| `requirements` | Minimum rank: Novice; weapon profile: Perforation; any weapon competency, natural attack form, or specific item that grants Perforation access can use this Technique unless the Technique or item says otherwise; user must be able to sustain a committed piercing line |
| `target` | enemy |
| `range` | weapon reach |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 4; Attrition 1 |
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
| `requirements` | Minimum rank: Novice; weapon profile: Perforation; any weapon competency, natural attack form, or specific item that grants Perforation access can use this Technique unless the Technique or item says otherwise; user must be able to sustain a committed piercing line |
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
| `trigger` | An enemy already inside your profile-bearing reach tries to withdraw, circle to a better angle, disengage from a contested position, or turn partial contact into clean separation. |
| `requirements` | Minimum rank: Novice; weapon profile: Torsion; any weapon competency, natural attack form, or specific item that grants Torsion access can use this Technique unless the Technique or item says otherwise; user must have a credible torsion contact surface |
| `target` | enemy |
| `range` | profile-bearing reach |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 4; Attrition 1 |
| `saving_roll` | contextual — resolved through the hostile movement exchange that the Technique catches |
| `tags` | control, disruption, counter_positioning, setup |

**Fantasy:** The user waits with still, coiled threat. When the opponent tries to leave or improve position after entering the profile-bearing reach, the curve releases and knots the escape route before it becomes clean separation.

**World origin:** Naghii training treats stillness as stored action. In tail and flexible-weapon practice, that becomes a method for punishing premature movement around a guarded body without relying on heavy force or rigid blocking.

**Why this is not a base attack:** A base flexible-weapon attack strikes along an angle. `Anudar el Paso` exists to solve a specific movement moment after the enemy is already inside profile-bearing reach: they try to withdraw, disengage, flank, or turn partial contact into clean position. Its identity is not damage through reach, but denying clean separation through curved contact.

**Primary interaction surface:** counter-positioning and anti-disengagement.

**Secondary interaction surface:** setup, because the target remains in a contested position instead of gaining a clean escape route or superior angle.

**Cost note:** `Rhythm 4 / Attrition 1` is intentional. The Technique is a narrow reactive anti-disengagement window. Unlike `Cerrar la Línea`, it does not stop an enemy from entering; it punishes an enemy who is already inside profile-bearing reach and tries to leave, circle, or cleanly improve position.

**Effect:** Make a reactive Torsion check against the triggering enemy. If the Technique resolves successfully, the flexible contact catches the enemy's step, wrist, weapon line, or lower body before separation completes. The triggering movement does not create clean withdrawal, a clean flank, or a superior angle. The enemy remains in their current contested position or in the nearest position that still leaves them inside the user's profile-bearing reach, and must spend a later movement commitment or action to clear the contact before treating that path as open.

**Restrictions:**

- requires a flexible contact surface that can credibly catch the step or line
- cannot be used against an enemy entering from outside profile-bearing reach
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
| `requirements` | Minimum rank: Novice; weapon profile: Unpredictability; any weapon competency, natural attack form, or specific item that grants Unpredictability access can use this Technique unless the Technique or item says otherwise; target can perceive the visible line; user has space to resolve from a different angle |
| `target` | creature |
| `range` | profile-bearing reach |
| `area` | single |
| `duration` | until the false-line consequence resolves, the target re-centers without answering the user, or immediate exchange tracking ends |
| `cost` | Rhythm 5; Attrition 1 |
| `saving_roll` | contextual — resolved through the hostile exchange created by the false line |
| `tags` | attack, disruption, mobility, false_read |

**Fantasy:** The user shows one curve and resolves through another, making the target answer the visible line while the real contact steals the useful angle.

**World origin:** Naghii politics and combat both teach controlled misreading: if others are reading you, decide what evidence they receive. In tail and flexible-weapon practice, that becomes a visible curve that makes the target defend the wrong path.

**Why this is not a base Flexible Weapons attack:** A base flexible-weapon attack uses reach or angle to strike. `Robar el Ángulo` specifically creates a false read and converts it into positional theft plus a spoiled immediate answer. Its identity is not extra damage; it is making the target answer the wrong line.

**Primary interaction surface:** false-line attack.

**Secondary interaction surface:** mobility and disruption, because the Technique steals position while also spoiling the target's immediate answer.

**Cost note:** `Rhythm 4 / Attrition 1` is deliberate. The Technique is broader than a narrow reactive catch, but its payoff remains tightly bounded: one target, one small positional conversion, one short response penalty, and no lasting control once the immediate exchange settles.

**Effect:** Make a Flexible Weapons attack or equivalent tail/tendril Technique check against the target. If the Technique resolves successfully, both false-line consequences apply:

- **Steal position:** the user shifts up to 1 meter around the target within profile-bearing reach without provoking a reaction from that target
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
| `saving_roll` | `T.E. (Sigilo)` — only if the target is actively suppressing its physical signal; if the target's Sigilo check succeeds, the read does not confirm |
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
| `origin` | Sigilo |
| `world_origin` | Species: Naghii; seed: Preserved Distance / Ritualized Access; transmission: threshold-stalking drills, ambush patience protocols, and hidden guardian presence practice; availability: Common |
| `category` | utility |
| `type` | active |
| `trigger` | The user is in a real hidden position — cover, concealment, darkness, broken sightline, or another credible hidden-guardian position — and a creature within 4 meters can register signs of a nearby unseen or half-seen threat. |
| `requirements` | Minimum rank: Novice; the user must be in a real hidden position; the target must be within 4 meters and able to register the possibility of a nearby unseen or half-seen threat. |
| `target` | creature |
| `range` | 4 meters from hidden position |
| `area` | single |
| `duration` | instant application |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | on success, the target makes an Alteration `R.R.` against `Aterrorizado` |
| `tags` | utility, stealth, pressure, fear, hidden_presence, ailment_application |

**Fantasy:** The target does not see a guard barring the way. It feels that something has been waiting here long enough to know exactly when to close. The fear is not "someone shouted stop." The fear is "if I take the next step, the thing that has been tracking me from cover will act first."

**World origin:** Naghii do not always contest access by standing in the doorway. Many threshold-keepers are taught to hold the dangerous line from just out of clear registration: behind stone, around a shelf turn, under broken light, along a wall line where movement reads before the body does. `Pesar el Umbral` comes from that stalking discipline, where the intruder begins to fear the held line before the guardian fully reveals themselves.

**Why this is not a base Sigilo check:** A base `Sigilo` check helps the user remain unnoticed, suppress profile, or pass through attention cleanly. `Pesar el Umbral` turns hidden presence into a fear application surface: the target is not just failing to spot the user, it is being made to bodily accept the next step as unsafe.

**Primary interaction surface:** hidden-presence pressure on one crossing or approach line.

**Secondary interaction surface:** Alteration application through `Aterrorizado`.

**Saving roll note:** If the hidden pressure lands, the target resists with Alteration `R.R.` against `Aterrorizado`. The fear line is the unseen or half-seen nearby predator/guardian presence holding that crossing line.

**Cost note:** `Rhythm 3 / Attrition 1` is intentional. The Technique still requires a real hidden position, a meaningful crossing line, and an Alteration `R.R.` to settle. It does not become a generic stealth bonus or a free panic button in open ground.

**Effect:** Make a `Sigilo`-based Technique check against the triggering target from the hidden position that is holding the relevant line.

If the Technique fails, the target does not bodily accept the hidden threat as urgent enough to settle fear.

If the Technique succeeds, the target immediately makes an Alteration `R.R.` against `Aterrorizado`.

Use the default Ailment severity bands by rank:

- ranks `1-2` -> `Minor`
- ranks `3-4` -> `Moderate`
- ranks `5-6` -> `Severe`

On a failed `R.R.`, the target gains `Aterrorizado` at that severity. The feared line is the hidden nearby predator/guardian presence controlling the crossing line.

On a successful `R.R.`, `Aterrorizado` does not settle.

**Restrictions:**

- requires a real hidden position: cover, concealment, darkness, broken sightline, or equivalent
- requires a meaningful held line or crossing moment
- applies the generic Alteration `Aterrorizado`, not a Naghii-only condition
- does not function in open exposure where the user is plainly registered and no hidden-presence line exists
- does not work on mindless targets or targets with no relevant self-preservation instinct
- if the target cannot register the possibility of a nearby unseen or half-seen threat, the Technique does not apply

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
| `requirements` | Minimum rank: Novice; weapon profile: Precision; any weapon competency, natural attack form, or specific item that grants Precision access can use this Technique unless this Technique narrows that access; narrowed access: the attack must deliver a readable physical mark such as pigment, scent, phosphorescent residue, tracer, or equivalent marking fluid; target can be physically marked |
| `target` | creature |
| `range` | weapon or projection range |
| `area` | single |
| `duration` | until the target completes its next movement or concealment attempt, clears the mark, leaves sensory reach behind a sealed barrier, or immediate position stops mattering |
| `cost` | Rhythm 4; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the mark |
| `tags` | attack, precision, marking, counter_concealment |

**Fantasy:** The user does not simply shoot where the target is. They place a visible, scented, irritating, or phosphorescent mark where the target's next movement will reveal the line it is trying to make disappear.

**World origin:** Saa-Naghii projection practice treats distance as a place where interpretation must become consequence. Archive scouts and projection wardens developed this method so a creature's next route remains readable after the moment of contact. Non-Naghii users reproduce the method with prepared marking ammunition, pigment darts, chemical tracers, marked arrows, or a similar kit-based delivery.

**Why this is not a base Ranged Weapons attack:** A base ranged attack tries to hit or harm the target. `Marcar la Lectura` uses the hit to preserve the target's immediate route as readable information. Its value is not extra damage or accuracy; it prevents the next movement or concealment attempt from becoming cleanly ambiguous to the user.

**Primary interaction surface:** ranged precision contact.

**Secondary interaction surface:** counter-concealment, because the mark keeps one immediate route, cover choice, doorway, or hiding line readable.

**Cost note:** `Rhythm 4 / Attrition 1` is deliberate. The Technique combines a ranged attack with a short-lived tracking consequence, giving it one strong surface and one secondary information-control surface. These costs apply only during ATB or another active-threat scene; in normal exploration, the Technique resolves as the user's ranged marking action without Attrition.

**Effect:** Make a profile-bearing attack with prepared marking ammunition, a marking kit delivery, or an equivalent natural fluid-projection Technique check against the target. If the Technique resolves successfully, the target becomes read-marked until the duration ends.

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
| `requirements` | Minimum rank: Novice; weapon profile: Corrosion; any weapon competency, natural attack form, or specific item that grants Corrosion access can use this Technique unless this Technique narrows that access; narrowed access: non-natural users need a Munition Kit that can prepare irritating, venomous, caustic, dusty, or sensory residue; target has a relevant sensory surface or exposed reading channel |
| `target` | creature |
| `range` | weapon or projection range |
| `area` | single |
| `duration` | until the target clears the residue, resolves one affected sight/read-dependent action, loses the residue environmentally, or immediate sensory pressure stops mattering |
| `cost` | Rhythm 4; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the residue |
| `tags` | attack, corrosion, sensory_pressure, disruption |

**Fantasy:** The user projects venom, dust, caustic residue, or another hostile trace across one exact exposed sensory channel, making the next clean read through that channel arrive through irritation and false signal.

**World origin:** Kha-Naghii hold venom as consequence attached to contact; Saa-Naghii project that same logic outward. `Nublar la Señal` comes from the projected side: the contact matters because it degrades the target's next clean decision. Non-Naghii users reproduce the method with irritant dust, venom capsules, caustic darts, or similar deliveries prepared through a Munition Kit.

**Why this is not a base Ranged Weapons attack:** A base ranged attack tries to hit or harm. `Nublar la Señal` spends precision to foul one declared sensory channel and create a bounded sensory-pressure choice: clear the residue or act through a compromised read. It is not a poison damage rider and not full `Cegado`.

**Primary interaction surface:** ranged corrosive or irritating contact.

**Secondary interaction surface:** disruption, because the target's next clean sensory action through that declared channel becomes costly unless they clear the residue.

**Cost note:** `Rhythm 4 / Attrition 1` is deliberate. The Technique is an attack that also creates a bounded sensory-pressure choice, but only for one target, one declared channel, and one dependent action. The shot also carries a precision tax because it must hit a small exposed read-point rather than just the body. These costs apply only during ATB or another active-threat scene; in normal exploration, the Technique resolves as the user's ranged residue action without Attrition.

**Effect:** Declare one exact exposed sensory channel or read-point the delivery is trying to foul: eyes, nostrils, heat pits, whiskers, a tasting fork, an exposed arcane read organ, or another similarly small channel the fiction supports. Make the attack with `-2` because the shot is targeting that exact point rather than simply landing on the body.

If the attack still resolves successfully, the target becomes `signal-blurred` for that declared channel until the duration ends.

Before resolving its next action or reaction that depends primarily on that same declared channel, the target must choose:

- spend `Interactuar` clearing the residue, ending the effect
- act through it and take a situational penalty equal to the rank bonus of the competency used for this Technique on that one affected roll or opposed exchange

| Competency rank used | Penalty |
| --- | --- |
| Novice | `-1` |
| Adept | `-2` |
| Expert | `-3` |
| Master | `-4` |
| Consummate | `-5` |
| Transcendent | `-6` |

The penalty applies only to that single channel-dependent action. If the declared channel is not actually one the target is using to make that decision, the effect gives no practical burden. The Technique does not blind the target completely, suppress all senses, prevent movement, or impose a general scene-wide penalty.

**Restrictions:**

- requires a ranged delivery that can leave irritating or degrading residue
- non-natural users need a Munition Kit that can prepare the residue delivery
- requires a relevant exposed sensory channel or reading surface
- applies to one creature only
- affects one declared channel-dependent action only
- the attack suffers `-2` for called channel placement
- does not blind the target completely
- does not disable all sensory channels
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
| `requirements` | Minimum rank: Novice; weapon profile: Ricochet; any weapon competency, natural attack form, or specific item that grants Ricochet access can use this Technique unless this Technique narrows that access; narrowed access: the attack must use a rebound-capable projectile or natural hardened projection; usable rebound surface; physically plausible indirect path |
| `target` | creature |
| `range` | weapon or projection range via surface |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 4; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` resolves normally against the final incoming path |
| `tags` | attack, ricochet, geometry, cover_denial |

**Fantasy:** The user reads a wall, step, pillar, tablet, shield edge, or other hard surface as part of the shot, striking the surface so the projectile bends into a line the target did not fully own.

**World origin:** Naghii archive and ruin practice teaches that built surfaces are evidence. In projection training, that becomes a material combat method: the wall, step, or doorway is read as part of the shot rather than treated as inert scenery.

**Why this is not a base Ranged Weapons attack:** A base ranged attack follows the direct line. `Doblar el Tiro` deliberately uses a declared surface to create a physically plausible indirect line. Its identity is not better aim or more damage; it is making the environment carry the shot.

**Primary interaction surface:** indirect ranged attack geometry.

**Secondary interaction surface:** cover denial, but only against the original direct-line edge that the rebound path genuinely bypasses.

**Cost note:** `Rhythm 4 / Attrition 1` is deliberate. The Technique grants one exact indirect-line permission, but it does not add persistent state, deny future action, or bypass defense wholesale. Its value lives in one geometry change, not in a lasting control surface.

**Effect:** Make a profile-bearing attack through one declared rebound or skip surface. If the Technique resolves successfully, the attack may reach a target that has partial cover, an offset doorway, an angled corner, or a blocked direct line, as long as a physically plausible indirect path exists.

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
| `requirements` | Minimum rank: Novice; weapon profile: Volley; any weapon competency, natural attack form, or specific item that grants Volley access can use this Technique unless the Technique or item says otherwise; target within ranged line; user can sustain a short cadence |
| `target` | creature |
| `range` | weapon or projection range |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 4; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | contextual — the target may answer with appropriate defense, movement timing, cover use, or balance |
| `tags` | attack, volley, movement_control, pressure |

**Fantasy:** The user lays a measured sequence of shots, spits, or projected pulses into a moving creature's next steps, forcing it to break rhythm, guard its body, or correct its footing before the movement completes.

**World origin:** Naghii archive wardens do not treat movement as empty space. An approach, withdrawal, cover shift, or line break is a procedure in motion. `Clavar la Cadencia` turns repeated projection into a way of preserving distance by breaking the cadence of hostile movement.

**Why this is not a base Ranged Weapons attack:** A base ranged attack tries to hit or harm the target on the user's action. `Clavar la Cadencia` is a reactive interruption against declared movement: the impact matters because it cuts distance from that movement. It is not volume fire, extra damage, or a multi-target attack.

**Primary interaction surface:** reactive ranged cadence against movement.

**Secondary interaction surface:** movement disruption, because a successful cadence can leave the target short of cover, short of melee contact, or short of a clean line break.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique is a ranged reactive attack that can also cut distance from one declared movement. It does not create a persistent slow, make multiple attacks, or sustain broad suppression.

**Effect:** Make a reactive profile-bearing attack or Technique check against the moving target before the triggering movement finishes.

If the Technique resolves successfully, the attack resolves normally and the target's remaining distance for that triggering movement is reduced by 1 meter per rank bonus of the competency used for this Technique.

| Competency rank used | Movement reduction |
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
- movement reduction is 1 meter per rank bonus of the competency used for this Technique
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
| `requirements` | Minimum rank: Novice; weapon profile: Ward; any weapon competency, natural attack form, or specific item that grants Ward access can use this Technique unless the Technique or item says otherwise; state: stable footing and ability to hold the position |
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

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The zone produces no immediate hit — its real cost is the movement restriction: if the user moves, the zone collapses and the investment is lost. A higher Rhythm cost would push the user too far ahead in the ATB queue to hold position while still reacting and acting, defeating the technique's identity. R=3 keeps the user in the ATB window where holding a zone is viable. Pending sim validation.

**Effect:** Establish a ward zone centered on the user extending to weapon reach plus 1 meter. While the zone is active, any enemy that performs an active action within the zone — including entering the zone through movement, attacking from within it, or using a Technique inside it — pays an additional Rhythm cost on top of that action's normal cost equal to 1 plus the rank bonus of the competency used for this Technique.

| Competency rank used | Zone Rhythm cost |
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
| `trigger` | The user wants to make contact with a target at or within 1 meter outside profile-bearing reach and return to a preferred position in a single trained sequence — entering, striking, and withdrawing before the target can convert the contact into a stable close exchange. |
| `requirements` | Minimum rank: Novice; weapon profile: Skirmish; any weapon competency, natural attack form, or specific item that grants Skirmish access can use this Technique unless the Technique or item says otherwise; user must have enough spacing to touch and withdraw |
| `target` | enemy |
| `range` | profile-bearing reach |
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
| `category` | attack |
| `type` | reactive |
| `trigger` | The user is targeted by a weapon-rooted attack from an enemy within weapon reach — the attacker's commitment arc is visible and interceptable. |
| `requirements` | Minimum rank: Novice; weapon profile: Interruption; any weapon competency, natural attack form, or specific item that grants Interruption access can use this Technique; user must be the declared target of the triggering attack; enemy must be within weapon reach; user has a credible flexible contact line to the target's weapon arm or execution line |
| `target` | enemy |
| `range` | weapon reach |
| `area` | single |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 1 |
| `saving_roll` | `R.R.` reduces — on a successful Alteration Resistance Roll, Impedido is not applied |
| `tags` | attack, control, disruption, counter |

**Fantasy:** The attacker commits their stroke. The expected answer is to defend. Instead the Naghii sends the flexible weapon into the commitment arc — catching the arm, the grip, or the execution line at the exact moment it is locked in. The counter-strike lands during the enemy's own action. The attacker absorbs damage from the thing they were swinging at, and their weapon arm is no longer reliable.

**World origin:** Naghii archive guard training treats every committed action as having a threshold moment where it is locked in and most interruptible. In confined archive spaces where full parrying guards are not available, this method of catching a weapon arm or execution line at the threshold and turning it into a counter-strike is a specific taught discipline.

**Why this is not a base Flexible Weapons attack:** A base flexible-weapon attack requires the user's own activation turn. `Trabar el Gesto` fires on the enemy's turn, when the enemy has already committed to an attack — the user substitutes their normal defense roll with an attack roll, turning the committed stroke into an opportunity for counter-damage and condition application.

**Primary interaction surface:** reactive counter-exchange — the user's T.A. replaces their T.D. in the incoming exchange.

**Secondary interaction surface:** condition application — Impedido on a failed Alteration R.R. after taking the counter-hit.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique is a reactive attack that simultaneously defends and deals damage, with a condition surface on top. The trigger is narrow (user must be the declared target), the attacker has an R.R. window against Impedido, and the counter can still fail if T.A. does not exceed the attacker's roll. These constraints prevent the cost from rising above the standard anchor despite the dual output.

**Effect:** Substitute your normal T.D. with a T.A. against the triggering attacker.

If your T.A. exceeds the attacker's T.A., you take no damage from the triggering attack and resolve T.I. normally against the attacker. The attacker then immediately makes an Alteration Resistance Roll against `Impedido`.

Use the default Ailment severity bands by rank:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe
- Higher ranks continue this progression if the system later defines higher severity bands.

On a failed R.R., the attacker becomes `Impedido` at that severity. On a successful R.R., `Impedido` is not applied.

If your T.A. does not exceed the attacker's T.A., the counter fails and the attack resolves normally against you.

**Restrictions:**

- user must be the declared target of the triggering attack
- attacker must be within weapon reach
- user must have a credible flexible contact line to the attacker's weapon arm or execution line
- applies to one attacker only
- does not grant an additional action — the T.A. replaces T.D., not supplements it
- does not create full restraint or movement restriction
- does not prevent the attacker from taking non-weapon actions while Impedido
- Impedido is removed by a successful Enfoque S.R. against the original severity

### Cruzar la Punta

| Field | Value |
| --- | --- |
| `name` | Cruzar la Punta |
| `name_en` | Cross the Point |
| `origin` | Evasion |
| `world_origin` | Species: Naghii; seed: Ritualized Access; transmission: archive guard threshold-crossing drills; availability: Restricted |
| `category` | defense |
| `type` | reactive |
| `trigger` | An enemy commits a single-target physical attack or physical Technique against the user with a discernible forward vector. |
| `requirements` | Minimum rank: Novice; defensive competency: Evasion; state: not fully restrained or immobilized; enough space to close toward the attacker |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | `D.R.` gates the Technique; if the attacker anticipated the close, they may contest the inside reposition with the relevant Technique or roll |
| `tags` | defense, mobility, counter_positioning, survival_window |

**Fantasy:** The attacker commits forward. The expected answer is to yield. The Naghii enters instead — flowing into the committed path at the exact moment it cannot redirect. Inside now, the attacker's position is no longer what they planned.

**World origin:** Naghii archive-guard training teaches controlled threshold crossing — passing through a guarded line without hesitation at the exact right moment — as a deliberate, disciplined act. In combat, the same doctrine applies to committed attacks: the user crosses into the attack rather than away from it.

**Why this is not raw `Evasion`:** A normal `D.R.` with `Evasion` only answers whether the hit lands. `Cruzar la Punta` uses that same successful defense as the entry gate for something more specific: crossing into the committed path so the attacker loses the range and angle they had just spent the action to claim.

**Primary interaction surface:** reactive close into a committed attack, denying the attacker their planned striking geometry.

**Secondary interaction surface:** immediate angle theft after a successful defense, because the user's new inside position denies the attacker the geometry they had committed to.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique is a narrow reactive close — its value is denying the attacker their planned range and raising their threshold, not damage or conditions. Attrition reflects the genuine body effort of closing into a committed attack rather than away from it.

**Effect:** Make your `D.R.` against the triggering attack using `Evasion`.

If that `D.R.` fails, the Technique fails and the attack resolves normally.

If that `D.R.` succeeds, close up to 2 meters toward the attacker as the strike arrives — entering rather than yielding. The attack has already failed to land, but the user's new position is now inside the attacker's committed range and angle. Closing does not disarm or neutralize the attacker — a skilled opponent will adjust grip, use the butt end of a reach weapon, or reorient their body. What the user has gained is denying the attacker their preferred range, leaving them with the burden of re-establishing it. The user does not attack as part of this Technique.

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
| `category` | defense |
| `type` | reactive |
| `trigger` | An enemy commits a single-target physical attack or physical Technique against the user. |
| `requirements` | Minimum rank: Novice; defensive competency: Evasion; state: not fully restrained or immobilized; enough space to move 2 meters |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | until the user makes a T.A., T.C., T.R., or T.E. against the triggering enemy after this Technique resolves |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | `D.R.` gates the Technique |
| `tags` | defense, counter_positioning, reposition |

**Fantasy:** The body leaves the readable position before the attacker settles their read. No block. No contest. The target has moved — and the attacker's acquired lock is momentarily void. That moment is the window to answer.

**World origin:** Naghii archival doctrine holds that what is not present cannot be struck, and that deliberate displacement is a form of denial, not retreat. The evasion is not an escape — it is the entry condition for an answer from a position the attacker no longer controls.

**Why this is not raw `Evasion`:** A normal `D.R.` with `Evasion` only answers whether the strike lands. `Vaciar el Blanco` uses that successful defense as the gate for a second payoff: a brief offensive window while the attacker's tracking has not yet re-acquired the new position.

**Primary interaction surface:** reactive evasion that opens a brief offensive bonus window against the triggering enemy.

**Secondary interaction surface:** counter-positioning — the bonus applies to the user's next action against that enemy, rewarding immediate follow-through.

**Cost note:** `Rhythm 3 / Attrition 1` matches `Cruzar la Punta`. Both are Novice Evasion reactive Techniques; Cruzar la Punta closes into the attack, Vaciar el Blanco converts the evasion into an offensive window. Neither produces damage directly.

**Effect:** Make your `D.R.` against the triggering attack using `Evasion`.

If that `D.R.` fails, the Technique fails and the attack resolves normally.

If that `D.R.` succeeds, the next time the user makes a `T.A.`, `T.C.`, `T.R.`, or `T.E.` against the triggering enemy after this Technique resolves, they gain a bonus to that roll equal to their Evasion competency rank.

| Evasion rank | Roll bonus |
| --- | --- |
| Novice | `+1` |
| Adept | `+2` |
| Expert | `+3` |
| Master | `+4` |
| Consummate | `+5` |
| Transcendent | `+6` |

Once that roll resolves, the window closes regardless of outcome.

**Restrictions:**

- does not function when the user is fully restrained or immobilized
- bonus applies to the first `T.A.`, `T.C.`, `T.R.`, or `T.E.` made against the triggering enemy, then closes
- bonus applies against the triggering enemy only — not against other enemies
- does not grant movement or produce damage directly

### Medir el Ciclo

| Field | Value |
| --- | --- |
| `name` | Medir el Ciclo |
| `name_en` | Measure the Cycle |
| `origin` | Astronomía |
| `world_origin` | Species: Naghii; seed: Celestial Order As Precision Tool; transmission: outer archive celestial calculation drills; availability: Restricted |
| `category` | utility |
| `type` | active |
| `trigger` | One or more ciclos autónomos are present and visible in the ATB — an independent cycle belonging to a creature, a body part, or an environmental effect that has its own Rhythm and activates outside the creature's main turn. |
| `requirements` | Minimum rank: Novice; state: at least one ciclo autónomo visible in the ATB |
| `target` | ciclo autónomo |
| `range` | visual range |
| `area` | one ciclo autónomo |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | difficulty threshold — set by the number of active ciclos autónomos in the ATB at the moment of the roll: 1 = Fundamental, 2–3 = Desafiante, 4–5 = Rigurosa, 6–7 = Exigente, 8+ = Extrema |
| `tags` | utility, setup, pattern_exploitation |

**Fantasy:** The astronomer does not wait to see what the cycle does. They measure it. Every cycle has a Rhythm, and the discipline of reading formal patterns — the same discipline that tracks moons, tides, and celestial return intervals — applies to anything that fires on a schedule. The user reads the cycle before it fires.

**World origin:** Naghii outer archive training teaches initiates to extract timing from observed patterns before being permitted to study deeper celestial doctrine. The cognitive tool is positional mathematics and pattern recognition, not intuition. The same discipline applied to tracking where a moon will be next applies to tracking when a cycle will next activate.

**Why this is not a base Astronomía check:** A base Astronomía check produces an estimate. `Medir el Ciclo` forces the Narrator to declare the specific Rhythm cost of the next activation — not "soon" but "in 2 Rhythm" — precise enough to coordinate an action around it.

**Primary interaction surface:** ATB setup — knowing exactly when a ciclo autónomo will fire changes what the group can safely do before it arrives.

**Secondary interaction surface:** pattern_exploitation — at higher Astronomía ranks, the user reads further ahead into the same cycle, turning a single read into a multi-step tactical map.

**Difficulty note:** The difficulty of isolating one cycle increases with the total number of active ciclos autónomos in the ATB at the moment of the roll. When many independent cycles are running simultaneously, separating the pattern of one from the noise of the others becomes progressively harder — regardless of creature category. A common creature with many active cycles can be harder to read than an elite creature with only one.

| Active cycles | Difficulty |
| --- | --- |
| 1 | Fundamental |
| 2–3 | Desafiante |
| 4–5 | Rigurosa |
| 6–7 | Exigente |
| 8+ | Extrema |

**Cost note:** `Rhythm 3 / Attrition 1` matches all Novice Naghii specialization information techniques. The output is immediate: one Narrator-declared Rhythm value that closes the uncertainty around the identified cycle's next activation. These costs apply only during ATB or active-threat scenes.

**Effect:** Make an Astronomía-based Technique check targeting one visible ciclo autónomo in the ATB. The difficulty is set by the total number of active ciclos autónomos present at the moment of the roll (see difficulty table). On success, the Narrator declares the Rhythm cost of that cycle's next N activations, where N equals the user's current Astronomía rank: at rank 1, one step ahead; at rank 2, two steps ahead; and so on for the same cycle.

The user and all allies within clear hearing range receive this information before the cycle fires — giving the group the exact window between now and the next activation to act, reposition, or protect.

The user gains a bonus equal to their current Astronomía rank on all saving rolls produced by the measured cycle's effects during the declared N activations.

On failure, no information is revealed about that cycle and no bonus is granted.

The information does not alter the cycle's activation and does not prevent its effect from occurring.

**Restrictions:**

- requires at least one ciclo autónomo visible in the ATB
- targets one ciclo autónomo only
- difficulty is set by total active ciclos autónomos at the moment of the roll, not by creature category
- reveals the Rhythm cost of the next N activations, where N equals the user's current Astronomía rank
- saving roll bonus applies to the user only — not shared with allies
- saving roll bonus applies only during the declared N activations of the measured cycle
- bonus does not apply to attack, specialization, or influence rolls
- does not alter the cycle or delay its activation
- does not prevent the cycle's effect from occurring

### Leer el Propósito

| Field | Value |
| --- | --- |
| `name` | Leer el Propósito |
| `name_en` | Read the Purpose |
| `origin` | Architecture |
| `world_origin` | Species: Naghii; seed: Structural Grammar Is Universal; transmission: outer archive vital structure reading drills; availability: Restricted |
| `category` | utility |
| `type` | active |
| `trigger` | A creature is present and visible in the scene with at least one Punto Vital not yet identified by the user. |
| `requirements` | Minimum rank: Novice; state: creature visible with at least one unidentified Punto Vital |
| `target` | creature |
| `range` | visual range |
| `area` | one Punto Vital |
| `duration` | indefinite — until the identified Punto Vital is destroyed or the creature relocates its vital points |
| `cost` | Rhythm 3; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | difficulty set by creature category — Común = Desafiante, Campeona = Rigurosa, Elite = Exigente |
| `tags` | utility, setup, targeting, structural_analysis |

**Fantasy:** The architecture of a living body is no less readable than a vault. The user applies the same structural grammar — access hierarchy, load distribution, vital mass concentration — to the creature's organization, identifying where the critical biology is held. The location, not the function.

**World origin:** Naghii outer archive training teaches that any organized system has readable structural grammar: where the load concentrates, what controls access to critical nodes, what was built — or grown, or evolved — to be weight-bearing and permanent. The discipline that identifies which threshold bears the structural weight of an archive complex is the same discipline applied to a living body.

**Why this is not a base Architecture check:** A base Architecture check produces qualitative impressions — "that part looks structurally significant." `Leer el Propósito` forces the Narrator to declare one specific Punto Vital's location: binary, actionable, precise enough to target. The raw Architecture roll cannot compel that declaration.

**Primary interaction surface:** ATB targeting — knowing exactly where one Punto Vital is located enables focused fire. Destroying a Punto Vital interrupts the cycles and techniques linked to it.

**Secondary interaction surface:** setup — the persistent T.A and T.E bonus converts identification into sustained targeting precision for the rest of the encounter.

**Difficulty note:** Difficulty scales with creature category. Vital point count is approximately equal across all creature categories (~5 per creature) and is not the determining factor — structural complexity of the organism is.

| Creature category | Difficulty |
| --- | --- |
| Común | Desafiante |
| Campeona | Rigurosa |
| Elite | Exigente |

**Cost note:** `Rhythm 3 / Attrition 1` matches all Novice Naghii specialization information Techniques. The output is immediate and combat-persistent: one Narrator-declared vital location plus a targeting bonus that holds until the vital point is destroyed.

**Effect:** Make an Architecture Specialization Roll targeting one visible creature. The difficulty is set by the creature's category (see difficulty table). On success, the Narrator declares the location of one specific Punto Vital on the creature. The user gains a bonus equal to their current Architecture rank on all T.A and T.E rolls targeting that Punto Vital.

The bonus applies to the user only — not shared with allies — and persists until the identified Punto Vital is destroyed or the creature relocates its vital points (a rare creature ability).

On failure, no Punto Vital is identified and no bonus is granted.

The technique does not reveal what the vital point controls, which cycles it governs, or which techniques it enables.

**Restrictions:**

- requires at least one creature visible with an unidentified Punto Vital
- targets one creature only
- identifies one Punto Vital only
- difficulty set by creature category, not vital point count
- does not reveal what the vital point controls, which cycles it governs, or which techniques it enables
- bonus applies to user only — not shared with allies
- bonus applies to T.A and T.E only — not T.D, T.R, or other rolls
- bonus persists until the Punto Vital is destroyed or the creature relocates its vital points

### Templar el Veneno

| Field | Value |
| --- | --- |
| `name` | Templar el Veneno |
| `name_en` | Temper the Venom |
| `origin` | Tolerancia + Poison Resistance |
| `world_origin` | Species: Naghii (Kha); seed: Venom As Commitment; transmission: kha venom conditioning and endurance drills; availability: Restricted |
| `category` | utility |
| `type` | passive |
| `trigger` | none — always active while requirements are met |
| `requirements` | Minimum rank: Novice; Tolerancia at Novice or higher; Poison Resistance at Novice or higher; mentor-gated acquisition |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | permanent while both Tolerancia and Poison Resistance remain at Novice or higher |
| `cost` | Rhythm 0; Attrition 0 — cost was paid in conditioning and training, not in the ATB |
| `saving_roll` | none |
| `tags` | utility, mitigation, condition_reduction, stability |

**Fantasy:** The body does not fight what it already carries. A Kha-Naghii who has trained under their own venom — and trained the discipline to hold adverse physical states without losing function — reaches a point where external venom finds familiar terms. The metabolic adjustment is not a decision. It is the body's response to a known adversary.

**World origin:** Kha-Naghii biological conditioning gives them systemic tolerance to their own venom. Formal initiation training teaches the practitioner to channel that tolerance through disciplined endurance: the body has been tempered by years of controlled exposure, and Tolerancia training gives shape to what would otherwise be raw biological luck.

**Why this is not raw Poison Resistance:** Raw `Poison Resistance` improves the `R.R.` against poison application. `Templar el Veneno` fires separately as a `T.E. (Tolerancia)` roll against the settled severity — a second chance to reduce the outcome by one step. A Kha-Naghii who fails their `R.R.` can still reduce the severity if their Tolerancia roll succeeds.

**Primary interaction surface:** passive-trigger Tolerancia roll that reduces Veneno family ailment severity by one step on success.

**Secondary interaction surface:** stability — by reliably capping venom severity at a lower tier, the Technique keeps the character functional under conditions that would remove others from effective action.

**Cost note:** `Rhythm 0 / Attrition 0` is correct and deliberate. The Technique triggers without a declared ATB action — no Rhythm or Attrition expenditure in the field. The cost was paid in conditioning: mentor-gated, cannot be self-studied, requires documented systematic venom exposure combined with Tolerancia training.

**Effect:** When a Veneno family ailment settles on the user, make a `T.E. (Tolerancia)` roll. The difficulty is set by the severity of the venom. On success, reduce the final settled severity by one step: Severe becomes Moderate, Moderate becomes Minor, Minor does not settle. On failure, the severity settles normally. The roll requires no declared action and no Rhythm or Attrition cost.

**Restrictions:**

- applies to Veneno family ailments only
- requires Poison Resistance at Novice rank or higher
- requires Tolerancia at Novice rank or higher
- does not negate Veneno ailments completely by itself
- does not apply to Alteration, Affliction, or other family effects from venom sources
- outsiders require documented systematic conditioning — improvised exposure does not qualify

### Sostener el Canal

| Field | Value |
| --- | --- |
| `name` | Sostener el Canal |
| `name_en` | Hold the Channel |
| `origin` | Meditación + Contención + Affliction Resistance |
| `world_origin` | Species: Naghii; seed: Holding Dangerous Knowledge; transmission: igi-an channel management and containment drills; availability: Restricted |
| `category` | utility |
| `type` | passive |
| `trigger` | The user performs a meditation action specifically directed at reducing the intensity of an active Abzu-origin or mental Affliction. |
| `requirements` | Minimum rank: Novice; Meditación at Novice or higher; Contención at Novice or higher; Affliction Resistance at Novice or higher; active Abzu-origin or mental Affliction present |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | permanent while all three prerequisites remain at Novice or higher |
| `cost` | no additional cost beyond the meditation action itself |
| `saving_roll` | none |
| `tags` | utility, recovery, condition_reduction, stability |

**Fantasy:** The igi-an practice was never about closing the channel. Closing it would mean losing the capacity to read the sky, sense the Abzu's movements, hear what the records mean in the present. What the deepest practitioners learn is not closure — it is management. The channel is held at the threshold. What enters can be acknowledged without being absorbed. And when it has absorbed too much, Contención gives it a route out — not through force, but through the practiced discipline of knowing where the boundary is and returning to it.

**World origin:** The Naghii's Abzu susceptibility is the inherited cost of generations of igi-an practice. The priesthood does not try to eliminate it — doing so would sever the capacity that makes their astronomical and theological work possible. Inner archive training instead teaches the practitioner to distinguish between absorption and holding: the channel is open, but the practitioner is not identical to what passes through it.

**Why this is not raw Meditación or raw Affliction Resistance:** Raw `Affliction Resistance` improves the initial `R.R.` against Afflictions, including the Naghii's Abzu-colored exposure logic. Raw Meditación produces recovery from Afflictions without specific calibration to the Abzu channel. `Sostener el Canal` produces a better meditation outcome specifically for Abzu-origin and mental Afflictions — the practitioner's trained channel management turns the act of recovery into a more efficient passage back to stability.

**Primary interaction surface:** improved meditation recovery for Abzu-origin and mental Afflictions.

**Secondary interaction surface:** stability — by recovering faster from the Afflictions the Naghii is most susceptible to, the technique partially compensates for the biological openness rather than merely enduring it.

**Cost note:** No additional cost beyond the meditation action itself. Like Templar el Veneno, the cost was paid in training: mentor-gated at its deepest layer, requires documented susceptibility and recovery experience, and demands concurrent development of Meditación, Contención, and Affliction Resistance. The meditation session that activates the bonus carries its own cost in time and focus — this Technique does not add to it.

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
- requires Meditación, Contención, and Affliction Resistance each at Novice or higher
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
| `trigger` | The user observes an enemy at close range to read construction faults or wear patterns on their armor or equipment — or exposed joints, previous injury patterns, or anatomical gaps on an unarmored target. |
| `requirements` | Minimum rank: Novice; Arqueología at Novice or higher; close range with line of sight to the target |
| `target` | enemy |
| `range` | close |
| `area` | single |
| `duration` | until mark is used or end of scene |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | none |
| `tags` | utility, pattern_exploitation, setup, die_advancement, counter_read |

**Fantasy:** Everything has a point where it gives. Armor: the dent never fully hammered out, the joint re-riveted too tight, the section where two plates meet at an angle the maker compromised on. Unarmored: the joint that absorbed a previous blow and never fully recovered, the gap between scale plates at maximum extension, the ridge of scar tissue that sits over bone rather than muscle. Not where to hit — where the material has already decided it will give.

**World origin:** Naghii ruin field training treats structural failure reading as a survival discipline: a practitioner who cannot identify which stone will give way cannot safely work in active ruins. The combat application transfers the same discipline to any material surface — worn armor, exposed joints, previous injury sites — because all of them carry the same evidence of stress, repair history, and previous force.

**Why this is not raw Arqueología:** Raw Arqueología produces narrative context — "the armor shows heavy use, there's an older repair on the left shoulder, the creature's right knee took a bad blow" — without a defined mechanical benefit. `Marcar la Grieta` produces a specific, bounded output: one die advancement on a committed follow-up attack against the identified fault zone.

**Primary interaction surface:** setup — identify one material fault zone on the target → next attack against that zone adds [Arqueología rank]d2 to the Impact roll. The bonus dice are not the designated critical die and do not affect critical probability. Applies to armored and unarmored targets alike.

**Cost note:** `Rhythm 3 / Attrition 1` matches the established Naghii setup technique anchor. The combat benefit requires a setup action before it applies — the user pays 3 rhythm to read, then pays the attack cost separately.

**Difficulty scale:** set by creature category or armor grade of the target.

| Category / Armor Grade | Difficulty |
| --- | --- |
| Common / Grade 1 | Challenging |
| Champion / Grade 2 | Rigorous |
| Elite / Grade 3 | Exacting |

**Effect:** Make an Arqueología check at difficulty set by the table above.

On success, identify one zone of the target where material structure creates a fault — for armored targets: a construction gap, wear point, or repair compromise in fabricated protection; for unarmored or naturally protected targets: an exposed joint, a previous injury site, or an anatomical gap where protection is thinnest.

The user's next attack against the identified zone adds [Arqueología rank]d2 to the Impact roll. These dice are not the designated critical die and do not affect critical probability. The mark expires when the attack is made or at the end of the scene.

On a failed check: no fault is identified.

**Restrictions:**

- requires close range with line of sight to the target
- mark applies to one zone of one target only
- mark expires on use or end of scene
- does not function against targets with no readable material structure (purely fluid or incorporeal forms)
- failed check yields no benefit

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
| `cost` | Rhythm 5; Attrition 1 |
| `saving_roll` | `R.R.` reduces — on a successful Alteration Resistance Roll, Atrapado is not applied and the movement proceeds normally |
| `tags` | utility, control, hold, pressure |

**Fantasy:** The target shifts weight to leave. The Naghii has already decided they are not going. The grip closes at the point of departure — before the exit is complete, before the safe window opens — and holds. The motion stops where the hold lands.

**World origin:** Naghii archive guard training treats exit control as a formal discipline: a guard does not pursue an escaping target, they hold the point of consequence. The specific skill taught is grip application at the exit moment — not during the movement but at its departure threshold, before the step is committed. This is why the technique fires even on exits that would ordinarily deny a reaction window: the hold is already placed when the movement begins.

**Why this is not raw Agarre:** Raw Agarre use produces narrative hold and positioning control without a defined mechanical condition. `Fijar el Umbral` applies `Atrapado` through the Alteration R.R. system — a gated condition with defined recovery mechanics — and uniquely fires against movement that explicitly does not provoke reactions.

**Primary interaction surface:** reactive hold application at the moment of exit — Atrapado on a failed Alteration R.R.

**Secondary interaction surface:** override permission — fires against declared no-reaction movement, denying a class of safe exits that most reactives cannot reach.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The condition remains narrower than `Trabar el Gesto`, but the Technique's defining permission is that it fires even against movement that would normally deny reactions. That override is large enough to place it at the standard anchor despite the recoverable outcome.

**Effect:** Make an Agarre check against the triggering enemy. On success, the target must make an Alteration Resistance Roll against `Atrapado`.

Use the default Ailment severity bands by rank:

- Ranks 1-2: Minor
- Ranks 3-4: Moderate
- Ranks 5-6: Severe
- Higher ranks continue this progression if the system later defines higher severity bands.

On a failed R.R., the target gains `Atrapado` at that severity. On a successful R.R., the movement proceeds normally and `Atrapado` is not applied.

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

### Tomar la Corriente

| Field | Value |
| --- | --- |
| `name` | Tomar la Corriente |
| `name_en` | Take the Current |
| `origin` | Nadar |
| `world_origin` | Species: Sauri; seed: Tail Keeps The Channel / Vessel Under Pressure; transmission: riverbank crossing drills, flooded corridor training, and temple-cistern recovery forms; availability: Restricted |
| `category` | utility |
| `type` | reactive |
| `trigger` | A physical force, moving surface, crowd, unstable terrain, current-like pressure, collision, shove, pull, slide, collapse, or other moving environment would displace you, carry you, spin you off line, or make you lose functional orientation. |
| `requirements` | Minimum rank: Novice; Nadar at Novice or higher; user must have enough freedom of movement to yield, turn, brace, breathe, or redirect the body; no specific anatomy required |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | Nadar Specialization Roll against the triggering force, environmental threshold, or opposed movement effect |
| `tags` | movement, recovery, anti_displacement, exploration, defense |

**Fantasy:** The user does not fight the current head-on. They enter it correctly. The same discipline used to stay alive in water — breath timing, yield, propulsion, orientation, and recovery through resistance — applies to any force that tries to carry the body somewhere it did not choose to go.

**World origin:** Sauri river training teaches that a body dies when it treats every current as a wall. Temple-cistern drills, floodgate crossings, marsh recovery, and submerged corridor training all teach the same lesson: first find the direction of the force, then become the part of the body that can survive passing through it.

**What `Nadar` contributes:** This Technique is not about water access. It comes from the trained components of swimming:

- yielding to a resisting medium without surrendering orientation
- timing breath and effort under pressure
- converting a push, pull, or drag into controlled movement
- recovering posture after the body is carried, spun, or partially submerged in force
- choosing an exit line instead of opposing the whole current

**Why this is not a base Nadar check:** A base `Nadar` check moves the body through water. `Tomar la Corriente` turns Nadar training into an immediate recovery method against any current-like physical displacement. It creates a mechanical choice during the displacement instead of only determining whether the user swims successfully.

**Primary interaction surface:** convert forced movement or loss of orientation into controlled repositioning.

**Secondary interaction surface:** exploration safety, because the same method can keep the user functional in flood, mudslide, crowd pressure, collapsing slope, broken bridge, moving platform, or other current-like hazards.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique does not negate the triggering force outright, does not damage the source, and does not protect another creature. Its value is recovery and route choice. In exploration, it is simply the user's specialized response to a current-like hazard and should not add Attrition unless the scene is already tracking active pressure.

**Effect:** Make a Nadar Specialization Roll against the triggering force or environmental threshold.

On success, choose one:

- reduce the forced movement affecting you by `1 meter + your Nadar rank bonus`
- convert up to `1 meter + your Nadar rank bonus` of the forced movement into controlled repositioning along a legal path touched by the triggering force
- avoid one secondary consequence caused only by losing orientation during that movement, such as falling prone, striking a minor obstacle, losing held direction, or being turned away from the intended exit line

The Technique does not erase the source of danger. If the force is too large to fully escape, the user still moves, but does so through a controlled line chosen from the available path rather than being carried blindly.

In exploration, the same effect can define how the user exits a current-like hazard: where they surface, what edge they reach, which side of a collapsing passage they roll toward, or which safe point they catch after being carried by pressure.

**Restrictions:**

- requires a physical force or environment that can be treated as a current: water, mud, crowd pressure, sliding ground, collapsing debris, moving platform, strong wind against footing, impact carry, shove, pull, drag, or similar movement pressure
- cannot be used against teleportation, fear movement, command effects, mental control, social pressure, poison, curse, infection, or purely internal paralysis
- cannot be used while fully immobilized, bound, unconscious, or unable to move the body enough to yield or redirect
- does not protect another creature
- does not stop the source, damage the source, apply a condition, or create a counterattack
- cannot move the user through sealed barriers, occupied spaces, impossible angles, or routes the triggering force could not plausibly carry the body through
- if the triggering effect explicitly states that displacement cannot be reduced or redirected, this Technique cannot override that rule unless a later upgrade says otherwise

---

### Guardar el Pulso

| Field | Value |
| --- | --- |
| `name` | Guardar el Pulso |
| `name_en` | Keep the Pulse |
| `origin` | Tolerancia |
| `world_origin` | Species: Sauri; seed: Vessel Under Pressure / Preserved Witness; transmission: ordeal chambers, wound-bearing rites, and preservation guard drills; availability: Restricted |
| `category` | utility |
| `type` | reactive |
| `trigger` | You are about to resolve a physical action, maintain a held duty, or finish a short exploration beat while already suffering one concrete bodily penalty source that would slow, penalize, or interrupt that function. |
| `requirements` | Minimum rank: Novice; Tolerancia at Novice or higher; the burden must be bodily or physiological, not emotional, social, mental, or purely supernatural; the user must still be conscious and physically capable of attempting the protected function. |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | one immediate action, one held duty until the user's next activation, or one short exploration beat |
| `cost` | Rhythm 0; Attrition 1 + optional extra Attrition |
| `saving_roll` | none |
| `tags` | utility, mitigation, survival_window, exploration |

**Fantasy:** The body wants to spill the action. The Sauri closes around it. Breath, weight, pain, pulse, and posture are put back into order long enough for one necessary thing to happen: the hand does not open, the body does not drop, the step completes, the witness is carried out, the strike is not lost to pain.

**World origin:** Sauri ordeal rites do not teach indifference to pain. They teach sequence. In hot chambers, after ritual cuts, under weight, during long stillness, the initiate learns which part of the body may fail and which part must remain available. A vessel does not survive because it feels nothing. It survives because it knows what cannot be allowed to spill first.

**What `Tolerancia` contributes:** This Technique is not generic toughness. It comes from trained physiological discipline:

- separating pain from the next necessary function
- breathing through a spike of damage without losing posture
- redistributing weight away from a compromised limb or wound
- keeping grip, stance, voice, or movement available under bodily stress
- prioritizing one function while the rest of the body pays the cost

**Why this is not a base Tolerancia check:** A base `Tolerancia` check determines whether the character remains functional under suffering. `Guardar el Pulso` lets the user spend immediate bodily strain to keep one necessary function from spilling right now, without delaying the action itself on the ATB.

**Primary interaction surface:** temporary mitigation of one existing bodily penalty source.

**Secondary interaction surface:** exploration continuity, because the same method can keep a character carrying a body, holding a gate, crossing a hazardous stretch, or finishing a rescue beat while injured or poisoned.

**Cost note:** `Rhythm 0 / Attrition 1 + optional extra Attrition` is deliberate. The Technique should not compete with the action it is preserving. The user is not spending time to answer an external threat; they are spending body to keep the action from spilling. The real price is extra strain, not ATB delay. Any extra mitigation beyond the base is purchased directly with more Attrition.

**Effect:** Choose one existing bodily penalty source that is currently affecting the declared action, held duty, or short exploration beat.

If the burden already has a named system definition, use that definition as the authority for what is being preserved:

- if it is an **Ailment**, use the existing Ailment entry and its severity
- if it is **Fatigue**, preserve one immediate function against the concrete Fatigue penalty currently defined in the scene
- if it is **wound pressure**, preserve one immediate function against the concrete penalty, interruption risk, or execution burden that the wound is already imposing

`Guardar el Pulso` does not invent a new burden and does not replace the source's normal application, duration, recovery, or removal rules.

When you activate this Technique, pay the base `Attrition 1`. You may then pay additional Attrition before resolution.

Each additional `1 Attrition` increases the preserved mitigation by `1`, on a strict `1:1` basis.

For this one resolution, choose one:

- reduce one stepped bodily penalty source by `1 + extra Attrition paid` steps for this action or duty, to a minimum of `none`
- if the source does not use severity steps, ignore up to `1 + extra Attrition paid` points of a single concrete penalty from that source for this resolution
- prevent one already declared physical action from being interrupted by that bodily burden, as long as the action remains physically possible
- maintain one held duty until your next activation or until the immediate exploration beat resolves: carrying a body, holding a gate, keeping a grip, remaining standing, staying braced, or continuing a short forced movement

The Technique does not remove the burden. After the preserved function resolves, all wounds, Fatigue, ailments, penalties, and consequences continue normally.

**Restrictions:**

- applies only to bodily or physiological pressure: pain, wound pressure, Fatigue, poison, infection, `Lacerado`, physical Ailments, exhaustion spike, or similar body degradation
- cannot be used against fear, command, social pressure, deception, curse logic, mental control, loss of will, confusion, or purely emotional collapse
- if the burden is an Ailment, that Ailment must already exist in the system or be defined before this Technique can reference it
- only affects one penalty source per use
- extra Attrition paid for this Technique only increases mitigation on the chosen source; it does not extend duration or protect multiple functions
- cannot heal, stabilize, treat, cure, remove wound slots, reduce Fatigue, or clear an ailment
- cannot allow an action that is physically impossible, such as walking on a destroyed leg if the scene has already established total loss of that function
- cannot override `Atrapado`, full paralysis, total immobilization, unconsciousness, or another state that removes the relevant bodily function entirely
- cannot prevent death, unconsciousness, or collapse if another rule says the character is already beyond action
- preserves one function only
- cannot be stacked with itself on the same action or burden; use only the strongest applicable preservation

---

### Sellar la Grieta

| Field | Value |
| --- | --- |
| `name` | Sellar la Grieta |
| `name_en` | Seal the Crack |
| `origin` | Aplomo |
| `world_origin` | Species: Sauri; seed: Sovereign Weight / Vessel Under Pressure; transmission: court bearing drills, temple witness rites, and sovereign-guard stillness training; availability: Restricted |
| `category` | utility |
| `type` | reactive |
| `trigger` | During combat or exploration under pressure, one creature or group under real scrutiny attempts to read, expose, exploit, or convert the user's visible pain, fear, fatigue, hesitation, or instability into actionable tactical truth, pursuit pressure, or a conditional hostile rider. |
| `requirements` | Minimum rank: Novice; Aplomo at Novice or higher; there must be an observer or audience capable of reading the user; the user must still be presenting a functional outward bearing. |
| `target` | self |
| `range` | self |
| `area` | one observing creature or group involved in the triggering resolution |
| `duration` | one triggering read / pressure resolution, or until the user's next activation if the same scrutiny continues without breaking |
| `cost` | Rhythm 4; Attrition 1 |
| `saving_roll` | Aplomo Specialization Roll opposed by the triggering read / pressure action, or against a Narrator-set scrutiny threshold when no explicit hostile roll exists |
| `tags` | utility, counter_read, control, pressure |

**Fantasy:** The crack exists. The witness does not get to see it open. Pain remains inside the jaw, fear remains behind the eyes, fatigue remains in the limbs, but the line that others can read stays unbroken long enough for the moment to pass without surrendering tactical leverage.

**World origin:** Sauri courts, ordeals, and funerary disputes teach that fracture becomes dangerous the moment it is seen by the wrong witness. A sovereign, guard, or ritual speaker is trained not merely to endure, but to prevent pain, exhaustion, or fear from becoming public evidence at the wrong instant.

**What `Aplomo` contributes:** This Technique is not internal calm and it is not a lie. It comes from trained exterior control:

- hiding pain before it reaches the face, stance, or voice
- preventing fatigue from becoming visible collapse
- controlling which signs of fear, strain, or hesitation escape the body
- holding a readable line of authority under hostile observation
- denying others the moment when visible fracture becomes leverage

**Why this is not a base Aplomo check:** A base `Aplomo` check determines whether the user keeps outward composure under scrutiny. `Sellar la Grieta` creates a defined anti-read result: the observer may continue acting, but does not get to convert the user's visible fracture into one immediate tactical truth or one read-dependent pressure rider.

**Primary interaction surface:** threshold / roll pressure against a hostile read based on visible fracture.

**Secondary interaction surface:** deny one conditional hostile rider that explicitly depends on that read.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique is a narrow reactive answer, but it does more than "stay calm": it makes the hostile read harder right now and can cancel one dependent rider if the read still lands. The cost reflects real visible strain under scrutiny without turning the Technique into a full social shield.

**Effect:** Make an Aplomo Specialization Roll opposed by the triggering read / pressure action, or against a Narrator-set scrutiny threshold when no hostile roll exists.

On success, choose one observing creature or one coherent observing group involved in the trigger. Apply both of the following to that resolution:

- if the triggering read uses a roll, it takes a penalty based on the user's `Aplomo` rank; if it uses a fixed threshold, raise that threshold by the listed tier shift
- if the triggering action or Technique still succeeds, it loses a number of read-dependent riders based on the user's `Aplomo` rank

`Aplomo` scaling for this Technique:

- Ranks `1-2`: `-2` to the read roll or `+1` difficulty tier; deny `1` read-dependent rider
- Ranks `3-4`: `-3` to the read roll or `+1` difficulty tier; deny up to `2` read-dependent riders from the same triggering action or Technique
- Ranks `5-6`: `-4` to the read roll or `+2` difficulty tiers; deny up to `2` read-dependent riders from the same triggering action or Technique

The base action may still continue if it does not require the denied leverage to exist. `Sellar la Grieta` does not turn the user invisible, healthy, or fearless. It only makes one visible crack harder to use as field evidence right now.

On failure, the read or pressure proceeds normally.

**Scaling:** Higher `Aplomo` does not just broaden permission here; it increases the concrete pressure the Technique applies to the hostile read and the amount of dependent leverage it can strip.

**Restrictions:**

- only works against leverage that depends on the user's visible outward fracture, not against evidence from wounds already examined directly, written records, material traces, or third-party testimony
- does not create a false narrative; it suppresses legible fracture rather than inventing a new story
- does not remove wounds, Fatigue, fear, Ailments, or other burdens from the user
- does not negate a hostile action wholesale; it only pressures the read and denies the rank-based number of read-dependent riders
- only affects one observing creature or one coherent observing group per use
- if the observer already has non-visible proof of the truth being protected, this Technique cannot erase that proof

### Tomar el Resguardo

| Field | Value |
| --- | --- |
| `name` | Tomar el Resguardo |
| `name_en` | Take Shelter |
| `origin` | Supervivencia |
| `world_origin` | Species: Sauri; seed: Tail Keeps The Channel / Stone Remembers Pressure; transmission: marsh patrol drills, flood-bank labor practice, ruin-entry field doctrine, and heat-shelter instruction; availability: Restricted |
| `category` | utility |
| `type` | active |
| `trigger` | You are about to move through, work inside, or hold position against a declared environmental hazard while a real partial shelter, cover edge, dry seam, stone lip, bank cut, shadow line, or other less-exposed point still exists nearby. |
| `requirements` | Minimum rank: Novice; Supervivencia at Novice or higher; there must be a real environmental hazard already affecting the scene; there must be a real usable shelter feature, not open empty ground. |
| `target` | shelter point |
| `range` | self / nearby reachable shelter feature |
| `area` | one chosen shelter point or working edge |
| `duration` | until your next activation, or until you abandon the chosen shelter point |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | Supervivencia Specialization Roll against the declared environmental hazard threshold |
| `tags` | utility, setup, terrain, hazard, cover |

**Fantasy:** The field is hostile, but not evenly hostile. The Sauri sees the lip of stone that breaks the heat, the dry seam that keeps a foot from sinking, the bank cut that turns spray aside, the low angle where debris will glance instead of crush. The shelter was already there. The Technique is claiming it in time.

**World origin:** Sauri laborers, marsh wardens, ruin crews, and floodline patrols learn that survival often depends less on speed than on choosing the right side of matter before pressure reaches it. Stone, mud, bank, and shadow are read as unequal carriers of danger.

**What `Supervivencia` contributes:** This Technique is built from extracted field capacities, not from generic "being good at survival":

- shelter selection
- hazard triage
- emergency prioritization
- field sustainment under pressure

**Why this is not a base Supervivencia check:** A base `Supervivencia` check decides whether the character can generally make sound field judgments. `Tomar el Resguardo` converts shelter selection into a bounded mechanical setup that changes one immediate hazardous position, movement, or work window.

**Primary interaction surface:** cover / position against one declared environmental hazard.

**Secondary interaction surface:** threshold pressure from exposure to that hazard.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. A full field read would normally cost the equivalent of a broader `Supervivencia` action. `Tomar el Resguardo` is cheaper because it does one narrower thing only: identify one immediately usable refuge point and let the user capitalize on it now.

**Effect:** Choose one real shelter point, cover edge, dry seam, stone lip, bank cut, shadow line, or other less-exposed working feature that the user can immediately occupy, work from, or move through during this activation. Make a `Supervivencia` Specialization Roll against the declared environmental hazard threshold.

On success, the Narrator identifies one real refuge point in the current scene that the user can immediately reach, occupy, work from, or pass through. That point remains valid until the end of the user's next activation, or until the fiction clearly changes enough that the refuge is lost.

The refuge may take one of two concrete forms:

- **cover refuge:** while the user remains there, they gain the normal automatic `T.D.` benefit of using real cover from that point, and the same point counts as a better position for cover-dependent concealment, hiding, or line-breaking attempts if the fiction supports it
- **environmental refuge:** while the user remains there, the declared environmental hazard treats the user as sheltered by that point for its normal resolution, using the scene's existing environmental rules rather than any extra Technique-specific bonus

`Tomar el Resguardo` does not create cover or safety from nothing. It reveals which already-existing point in the map or environment is the correct place to use right now.

On failure, the chosen point was misread, too weak, or claimed too late; the hazard resolves normally.

**Scaling:** This Technique does not scale by changing its output. Its value scales indirectly because a higher `Supervivencia` rank makes the required roll more reliable, which makes the refuge easier to identify under harsher conditions.

**Restrictions:**

- requires a real environmental hazard and a real shelter feature already present in the fiction
- does not create cover or shelter where none exists
- does not grant free movement or repositioning by itself
- only protects against one declared environmental hazard per use
- only benefits the user at Novice tier
- ends early if the chosen shelter point breaks, becomes occupied, is bypassed by the hazard's fiction, or the user abandons it
- does not stop direct attacks, conditions, or Ailments unless those are riders of the declared environmental hazard and depend on exposure through the chosen point

### Anudar la Vasija

| Field | Value |
| --- | --- |
| `name` | Anudar la Vasija |
| `name_en` | Knot the Vessel |
| `origin` | Medicina |
| `world_origin` | Species: Sauri; seed: Vessel Under Pressure / Preserved Witness; transmission: funerary preparation drills, floodline field medicine, temple attendant trauma practice, and marshal triage instruction; availability: Restricted |
| `category` | utility |
| `type` | active |
| `trigger` | An adjacent creature has active physical trauma that is still spilling, worsening, or threatening immediate collapse, and you have one short intervention window to bind, brace, seal, or pin it before the next break in function. |
| `requirements` | Minimum rank: Novice; Medicina at Novice or higher; access to the target's injured body zone; one free hand plus cloth, binding, splint material, field kit, or another plausible means of rapid stabilization. |
| `target` | self or adjacent creature |
| `range` | touch / adjacent |
| `area` | one creature |
| `duration` | immediate; any stabilization result persists by its normal system rule |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | Medicina Specialization Roll against a threshold set by the severity and instability of the target's current trauma |
| `tags` | utility, support, stabilization, recovery, medical |

**Fantasy:** The body is opening where it should stay closed. The Sauri does not heal it. They stop the loss from becoming a flood. A strap, knot, brace, pressure wrap, jaw-pin, or splint turns panic into one more minute of structure.

**World origin:** Sauri medicine grows out of preservation as much as cure. Temple attendants, body-bearers, and floodline medics are taught that the first duty is not to restore the whole body, but to stop a vessel from spilling beyond recall.

**What `Medicina` contributes:** This Technique is built from extracted medical capacities, not from generic healing:

- stabilization
- trauma triage
- bodily intervention timing

**Why this is not a base Medicina check:** A base `Medicina` check covers broad treatment, diagnosis, or field care. `Anudar la Vasija` compresses one specific emergency intervention into a combat-usable action: stop immediate worsening now, without pretending the target is cured.

**Primary interaction surface:** `Estabilizar` and immediate wound-pressure control.

**Secondary interaction surface:** removal of one existing trauma rider when that rider exists only because the injury remains unbound or unstabilized.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique is faster and narrower than full treatment. It does not recover wound slots, heal damage, or perform long care. It buys immediate continuity by locking one trauma point down under pressure.

**Effect:** Choose one self or adjacent creature suffering current physical trauma that is still actively worsening, spilling, or threatening immediate collapse. Make a `Medicina` Specialization Roll against a threshold set by the target's current trauma severity and scene pressure.

On success, choose one:

- if the target is in `Agonía`, immediately apply `Estabilizar` to that target
- if the target is suffering `Lacerado`, end `Lacerado` by binding, bracing, sealing, or otherwise stabilizing the stressed wound
- if the target is suffering another already-declared wound-pressure rider that exists because the injury remains physically unstabilized, remove that one rider until the fiction creates it again through renewed stress, reopened trauma, or further injury

`Anudar la Vasija` does not heal, treat, or cure the trauma. It only stops the immediate spill. Any wound slots, lasting damage, untreated zones, Ailments, Fatigue, and follow-up care requirements remain in place.

On failure, the intervention is too slow, slips, or cannot hold under current pressure; the trauma continues normally.

**Scaling:** This Technique does not scale by changing its output. Its value scales indirectly because higher `Medicina` makes the emergency intervention more reliable against worse trauma and tighter pressure windows.

**Restrictions:**

- only works on current physical trauma, not curses, fear, command effects, pure pain without a stabilizable bodily source, or abstract morale collapse
- if the target's problem is an Ailment, that Ailment must already have a physical logic that can plausibly be braced, bound, or stabilized; otherwise this Technique does not apply
- cannot free wound slots, restore lost HP-equivalent resources, or count as `Tratar` or `Curar`
- cannot remove more than one current trauma output per use
- requires actual bodily access and plausible stabilizing means
- does not prevent future worsening if the wound is reopened, stressed again, or the fiction makes the temporary stabilization fail

### Tomar la Costura

| Field | Value |
| --- | --- |
| `name` | Tomar la Costura |
| `name_en` | Take the Seam |
| `origin` | Minería |
| `world_origin` | Species: Sauri; seed: Stone Remembers Pressure / The Seam Tells Which Face Holds; transmission: quarry reading drills, floodgate maintenance, tomb-opening labor, and defensive masonry practice; availability: Restricted |
| `category` | setup |
| `type` | active |
| `trigger` | A stone, packed-earth, mudbrick, ore-bearing, masonry, or similarly mineral feature is relevant to the current position, line, or obstacle, and the user has a short window to read which face protects and which seam gives. |
| `requirements` | Minimum rank: Novice; Minería at Novice or higher; line of sight or physical access to the relevant material feature; enough visibility, contact, or prior exposure to actually judge the surface. |
| `target` | object / cover / structure segment |
| `range` | short range / adjacent |
| `area` | one local material segment |
| `duration` | mode-dependent; enemy cover reduction lasts while that creature keeps using the same mineral cover on the same line, self-cover lasts until the user leaves that position, and break setup lasts through the next valid break attempt; all modes end early if the scene materially changes |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | Minería Specialization Roll against a threshold set by material hardness, packing, stability, and scene pressure |
| `tags` | setup, structure, cover, break, terrain |

**Fantasy:** Stone always tells the truth if you know where to look. One face carries load cleanly. Another has already begun to separate. The Sauri does not need to move the wall yet. They only need to know which side to trust and which side to strike.

**World origin:** Sauri quarry workers, gate tenders, and tomb laborers learn to read where mineral surfaces truly hold and where they are already preparing to fail. In conflict, that same discipline becomes immediate tactical judgment: the correct face becomes shelter; the correct seam becomes an opening.

**What `Minería` contributes:** This Technique is built from extracted material capacities, not from generic earth knowledge:

- material detail discrimination
- fault-line isolation
- load-path judgment

**Why this is not a base Minería check:** A base `Minería` check judges excavation, material value, or underground stability. `Tomar la Costura` compresses that training into one immediate combat or exploration setup: identify the exact face of a mineral feature that best protects use now, or the exact seam that best yields to the next break.

**Primary interaction surface:** `Cobertura` and `critical_breaking_parts` against mineral structure.

**Secondary interaction surface:** local terrain or obstacle use through a material face that is already present in the scene.

**Cost note:** `Rhythm 4 / Attrition 1` is deliberate. The Technique still does not move or break the material by itself, but one read can become enemy-cover reduction, self-cover improvement, or a prepared break seam. That multi-mode setup is broader than a pure quick informational read.

**Effect:** Choose one stone, packed-earth, mudbrick, ore-bearing, masonry, or similarly mineral feature within short range that is currently relevant as cover, barrier, lip, bank, broken face, threshold, or local obstacle. Make a `Minería` Specialization Roll against a threshold set by the material's hardness, packing, stability, and the scene's current pressure.

On success, choose one:

- if one enemy is currently using the chosen mineral feature as `Cobertura` on a declared attack line, reduce that enemy's `Cobertura` by one step on that line, to a minimum of no cover, while that enemy continues using that same feature on that same line; this ends if the enemy changes position, switches to different cover, loses the line, or the feature materially changes
- if the chosen feature can plausibly shield part of the user's body or working angle, treat it as `Cobertura Ligera` for the user against declared attack lines until the user leaves that position, stops holding that face, or the feature materially changes
- if the chosen feature contains a plausible mineral seam, stress line, or weak face, declare one exact segment for the next valid break attempt against that segment; for that attempt only, the designated critical die counts one result below its normal maximum as enough to validate the break attempt against that segment. This expanded threshold does not grant other critical options unless the die actually rolls its normal maximum, and the read ends whether the attempt succeeds or fails

`Tomar la Costura` does not create new stone, move structures, or cause damage by itself. It only turns an existing mineral truth into one immediate mechanical advantage.

On failure, the read is too slow, the surface is too deceptive, or the pressure of the moment prevents a clean judgment; the feature grants no improved use and no marked break seam.

**Scaling:** This Technique does not scale by changing its output. Its value scales indirectly because higher `Minería` makes the correct protective face or break seam easier to identify under harder material and more dangerous pressure.

**Restrictions:**

- only works on stone, packed earth, mudbrick, masonry, ore-bearing, excavated, or similarly mineral material where seam and load reading apply
- does not function on anatomy, pure metal mechanisms, cloth, wood joinery, social posture, aura states, or broad architectural logic whose key issue is layout rather than mineral surface behavior
- cannot affect more than one declared cover line or mark more than one break seam per use
- cannot reduce enemy `Cobertura` by more than one step
- cannot grant better than `Cobertura Ligera` to the user
- the expanded critical threshold only applies to validating one break attempt against the declared mineral segment; it does not broaden other critical outputs unless the weapon rolls its normal true critical
- if the feature has no meaningful protective face and no meaningful mineral seam, this Technique does not apply
- if the feature is too large, too uniform, too ruined, or too visually obscured for a Novice read to isolate one useful face or seam, the Technique only reveals that limitation through failure or refusal of effect

### Tomar el Eco

| Field | Value |
| --- | --- |
| `name` | Tomar el Eco |
| `name_en` | Take the Echo |
| `origin` | Resonancia |
| `world_origin` | Species: Sauri; seed: Stone Remembers Pressure / Preserved Witness; transmission: temple readers, cistern wardens, funerary signal practice, and ruin-entry resonance drills; availability: Restricted |
| `category` | information |
| `type` | active |
| `trigger` | A creature, object, place, or manifestation nearby is carrying an active aura, taumatic, or essential signal that matters now, and the user has a short window to catch its echo before it disperses into the scene. |
| `requirements` | Minimum rank: Novice; Resonancia at Novice or higher; an active signal must actually be present; the user must have plausible resonant reach to the source and no fully sealed barrier between them. |
| `target` | one creature / object / place / manifestation |
| `range` | short sensory reach / same immediate scene |
| `area` | one active signal |
| `duration` | mode-dependent; exact-position read lasts until the source changes zone, fully suppresses its signal, crosses a sealed barrier, or the scene stops tracking immediate location; route truth lasts until the source commits to its next movement or signal pattern changes; state truth is immediate |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | Resonancia Specialization Roll against a threshold set by signal strength, interference, distance, and scene pressure; if a creature is actively hiding or suppressing its signal, oppose with the relevant concealment or suppression roll instead |
| `tags` | information, detection, anti_concealment, aura, tauma |

**Fantasy:** The Sauri does not need to see the whole body to know something is there. What touched the place leaves a pulse. What carries force does not stay silent. The user catches the echo before it fades and takes the truth that still remains in it.

**World origin:** Sauri temple readers and funerary attendants are trained to trust what continues to answer after contact. In cistern halls, burial chambers, and ruin corridors, they learn that some presences do not need to be seen to be followed; they only need to keep sounding inside the place.

**What `Resonancia` contributes:** This Technique is built from extracted aura capacities, not from generic tauma knowledge:

- active aura reach
- signal attunement
- field-state sampling

**Why this is not a base Resonancia check:** A base `Resonancia` check determines whether the user can generally sense or contact an active essential signal. `Tomar el Eco` compresses that into one immediate tactical read: where the signal is, which route still carries it, or what state it is in right now.

**Primary interaction surface:** immediate `information`, `visibility_concealment`, and `manifestation`.

**Secondary interaction surface:** counter-concealment against sources that are hidden visually but still carrying an active essential or taumatic trace.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique is a fast read under pressure that produces one actionable truth now. It does not damage, bind, or suppress the target by itself; it only prevents the signal from staying tactically ambiguous.

**Effect:** Choose one creature, object, place, or manifestation within short sensory reach that is carrying an active aura, taumatic, or essential signal. Make a `Resonancia` Specialization Roll against a threshold set by signal strength, interference, distance, and scene pressure.

On success, choose one:

- if the source is present but visually hidden, obscured, or positionally uncertain, you detect its exact current position for yourself; while the read lasts, that source cannot rely on purely visual concealment against you
- if the source is moving, about to move, or has just passed through multiple plausible routes, the Narrator reveals which current route, doorway, bank, corridor, or adjacent zone still carries the true signal; this lasts until the source commits to its next movement or the signal pattern changes
- if the source is an object, place, creature, or manifestation whose state matters more than its exact location, the Narrator reveals one immediate state truth supported by the signal, such as whether it is active, dormant, unstable, recently disturbed, anchored, or already fading; this truth is immediate and does not persist as a mark

`Tomar el Eco` does not identify exact statistics, full intent, full spell logic, hidden history, or every signal in the area. It takes one active echo and turns it into one actionable truth.

On failure, the signal is too weak, too crowded, too distant, or too entangled with other presences; the user gets no reliable read from that attempt.

**Restrictions:**

- only works on active aura, taumatic, or essential signals that are actually present in the scene
- does not reveal through fully sealed barriers, total sensory isolation, or sources whose signal has genuinely ended
- does not grant universal revelation to allies; they still need their own senses, communication, or Techniques
- does not reveal full intention, exact mechanics, exact statistics, or complete causal history
- if the target is hidden only by mundane distance without any readable signal reaching the user, this Technique does not apply
- if multiple signals are perfectly merged and the fiction offers no basis to isolate one of them at Novice scale, the Technique only reveals that entanglement through failure or refusal of effect

**Scaling:** This Technique does not scale by changing its output. Its value scales indirectly because higher `Resonancia` makes it easier to isolate the correct signal under heavier interference, denser presence, or weaker echo.

### Tomar la Secuencia

| Field | Value |
| --- | --- |
| `name` | Tomar la Secuencia |
| `name_en` | Take the Sequence |
| `origin` | Taumaturgia |
| `world_origin` | Species: Sauri; seed: Stone Remembers Pressure / Release At The Correct Gate; transmission: temple doctrine, archive instruction, ritual maintenance, and controlled-contact tauma drills; availability: Restricted |
| `category` | setup |
| `type` | active |
| `trigger` | An active taumatic object, place, manifestation, seal, residue pattern, or unstable effect must be crossed, handled, contained, or manipulated before the scene can advance safely. |
| `requirements` | Minimum rank: Novice; Taumaturgia at Novice or higher; a real taumatic structure or manifestation must be present; the user must have enough access, observation, or prior contact to study its current operation. |
| `target` | one taumatic source / manifestation / ritual structure |
| `range` | short study reach / same immediate scene |
| `area` | one active taumatic pattern |
| `duration` | mode-dependent; revealed state truth is immediate, while the handling forecast lasts through the next valid action that follows the declared law or until the target's pattern materially changes |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | Taumaturgia Specialization Roll against a threshold set by pattern complexity, instability, interference, and scene pressure |
| `tags` | setup, information, tauma, manifestation, handling |

**Fantasy:** The Sauri scholar does not reach for the force first. They read its sequence. Every taumatic thing opens somewhere, closes somewhere, spills somewhere, and holds somewhere. The trick is not to overpower it, but to know which step comes next and where the vessel survives the contact.

**World origin:** Sauri ritual keepers and temple readers are trained to treat taumatic structures as pressure systems with lawful openings. Their doctrine is not raw magical command. It is disciplined reading of how a manifestation is currently behaving, what interaction it will accept, and which wrong contact will make it spill.

**What `Taumaturgia` contributes:** This Technique is built from extracted formal tauma capacities, not from generic aura sensing:

- tauma-law reading
- interaction forecasting
- instability recognition under exposure

**Why this is not a base Taumaturgia check:** A base `Taumaturgia` check determines whether the user understands the phenomenon in formal terms. `Tomar la Secuencia` turns that understanding into one immediate operational forecast that changes the next valid handling, crossing, or containment attempt.

**Primary interaction surface:** `manifestation`, `information`, and `thresholds`.

**Secondary interaction surface:** safe or unsafe handling of taumatic environments, residues, and contact structures.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique is a fast doctrinal read under pressure. It does not suppress the manifestation or complete the solution by itself; it gives one lawful way to interact with the phenomenon better than blind contact would allow.

**Effect:** Choose one active taumatic object, place, manifestation, seal, residue pattern, or unstable effect within short study reach. Make a `Taumaturgia` Specialization Roll against a threshold set by pattern complexity, instability, interference, and scene pressure.

On success, choose one:

- reveal one current state truth about the target's operation, such as whether it is stable, unstable, cycling, anchored, draining, primed, or already collapsing; this truth is immediate and does not persist as a mark
- declare one lawful handling sequence for the next valid action to cross, touch, move, inspect, disable, contain, or disengage from that exact target; the threshold of that next valid action is reduced by 1 step if it follows the revealed sequence
- declare one specific unsafe interaction that would provoke, worsen, discharge, or prematurely shift the target; any ally within clear hearing who avoids that declared mistake is treated as not having triggered that specific escalation path during the next immediate handling window

`Tomar la Secuencia` does not reveal full doctrine, complete hidden history, exact statistics, all future states, or universal safety from the phenomenon. It gives one lawful read that matters now.

On failure, the pattern is too incomplete, too unstable, too alien, or too pressured to parse cleanly; the user gets no reliable forecast from that attempt.

**Restrictions:**

- only works on active taumatic structures, manifestations, residues, seals, or effects that are actually operating in the scene
- does not function on purely mundane mechanisms, ordinary weather, bodily wounds, social pressure, or non-taumatic mystery by itself
- does not suppress, dispel, or deactivate the target on its own
- only reduces the threshold of one next valid action that genuinely follows the declared lawful sequence
- if the target materially changes state before that next action resolves, the forecast ends
- if the phenomenon is so alien, sealed, or overbuilt that Novice Taumaturgia cannot isolate a lawful interaction window, the Technique only reveals that limitation through failure or refusal of effect

**Scaling:** This Technique does not scale by changing its output. Its value scales indirectly because higher `Taumaturgia` makes it easier to isolate a correct law under denser interference, stranger doctrine, or more unstable taumatic behavior.

### Cerrar la Coraza

| Field | Value |
| --- | --- |
| `name` | Cerrar la Coraza |
| `name_en` | Close the Carapace |
| `origin` | Armadura intermedia / Armadura pesada |
| `world_origin` | Species: Sauri; seed: Vessel Under Pressure / Procession Of Force; transmission: temple armor drills, floodgate guard posture training, and sovereign escort procession discipline; availability: Restricted |
| `category` | defense |
| `type` | active stance |
| `trigger` | You deliberately set your body to receive incoming pressure through the part of your armor that was built to hold it. |
| `requirements` | Minimum rank: Novice; defensive competency: Armadura intermedia or Armadura pesada; the user must be wearing a functional piece of that armor on the line they intend to present, must be standing or otherwise able to hold posture, and must be able to keep the declared armored facing toward the pressure being received. |
| `target` | self |
| `range` | self |
| `area` | one declared armored facing / pressure line |
| `duration` | sustained while the user keeps the declared armored facing and posture |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | none |
| `tags` | defense, mitigation, stability, survival_window |

**Fantasy:** The armor is not trusted because it exists. It is trusted because the body closes it correctly. Plates, scales, straps, and weight all have an angle where they hold and an angle where they open. The Sauri turns the body until the pressure meets the vessel where it was meant to survive.

**World origin:** Sauri temple guards and floodgate escorts are taught that armor is a prepared surface, not a passive blessing. Ritual processions, canal defenses, and sovereign escort drills all repeat the same lesson: if the body presents the wrong seam, the armor becomes a lie. Proper weight, proper angle, and proper sequence make it hold.

**Why this is not raw armor competency:** Raw armor competency already contributes `CD` when the correct piece actually absorbs the hit. `Cerrar la Coraza` goes further: it declares one armored line, turns that preparation into an active armor posture, and improves the protection only while the body keeps that exact presentation under pressure.

**Why this is not `Asentar la Piedra`:** `Asentar la Piedra` is a shield-rooted Bastion stance that improves `D.R.` and physical `R.R.` through a held profile-bearing surface. `Cerrar la Coraza` does not help you avoid the hit and does not require a shield. It makes a declared armored line harder to open after contact by improving `Bloqueo` where the armor actually receives the force.

**Primary interaction surface:** `Bloqueo` on a declared armored facing.

**Secondary interaction surface:** physical stability against the same declared pressure line.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. Entering the posture is quick, but holding the correct weight, seam, and angle under live pressure is real body work. The Technique does not damage, move, intercept for allies, or create broad protection; it only prepares one armored line to survive contact better while the posture is maintained.

**Effect:** Choose one forward or otherwise clearly declared pressure line that your current body-facing and armor can credibly present.

While the stance remains active, you are considered to be using an `active armor posture`.

If an attack or physical impact comes through that declared line, hits a zone where the chosen medium or heavy armor actually participates in absorbing the impact, and does not bypass the armor entirely, add a bonus equal to the rank bonus of the armor competency used for this Technique to that zone's `Bloqueo`.

If that same triggering effect would also force physical displacement or require an `R.R.` against `Derribado` or `Desequilibrado` through impact, shove, posture loss, or bodily collision coming through that same declared line, add the same rank bonus to that `R.R.`.

If the pressure comes from a different line, strikes an unarmored or lightly armored zone, reaches a gap the declared posture is not actually covering, or bypasses armor entirely, this Technique gives no benefit against that effect.

**Restrictions:**

- only works with `Armadura intermedia` or `Armadura pesada`
- only applies when the declared armor really participates in absorbing the impact on the struck zone
- does not improve `T.D.`, interception, ally protection, or cover by itself
- does not help against poison, fear, curses, taumatic pressure, sensory overload, mental influence, social pressure, or other non-physical effects
- does not help against attacks or effects that explicitly bypass armor, strike from outside the declared line, or hit a zone the declared posture was not actually covering
- ends if the user voluntarily moves more than 1 meter from the held posture, turns away from the declared line, falls, loses footing, or otherwise breaks the presented armored facing
- ends for any struck zone whose relevant armor piece is broken and no longer contributes `Bloqueo`
- does not stack with another active armor posture unless a later rule explicitly says otherwise

### Volver la Placa

| Field | Value |
| --- | --- |
| `name` | Volver la Placa |
| `name_en` | Turn the Plate |
| `origin` | Armadura intermedia / Armadura pesada |
| `world_origin` | Species: Sauri; seed: Release At The Correct Gate / Vessel Under Pressure; transmission: escort impact drills, last-angle armor correction practice, and canal-gate body-turn discipline; availability: Restricted |
| `category` | defense |
| `type` | reactive |
| `trigger` | A physical attack or impact is about to connect against a zone protected by your medium or heavy armor, and you still have time to turn that contact onto the armor's holding face instead of receiving it through a worse seam or angle. |
| `requirements` | Minimum rank: Novice; defensive competency: Armadura intermedia or Armadura pesada; the struck zone must be protected by a functional piece of that armor; the user must not be fully restrained or immobilized and must still be physically capable of making the last-angle correction. |
| `target` | self |
| `range` | self |
| `area` | one incoming hit / one struck zone |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | none |
| `tags` | defense, mitigation, stability, counter |

**Fantasy:** The Sauri does not outrun the hit. They correct it. A shoulder turns half a handspan, the ribs settle, the weight drops, the seam disappears, and the strike lands on what was meant to survive it.

**World origin:** Sauri armor teaching does not stop at standing correctly. Temple escorts and gate guards are drilled to make one last correction when pressure arrives badly: not enough to become untouchable, only enough to make the vessel receive the force through plate instead of opening through weakness.

**Why this is not `Cerrar la Coraza`:** `Cerrar la Coraza` is the prepared posture you hold before pressure arrives. `Volver la Placa` is the emergency correction when the line was not already fully set or when the incoming angle shifts at the last moment. It protects one hit only and creates no sustained armor posture afterward.

**Primary interaction surface:** one-hit `Bloqueo` correction on an armored zone.

**Secondary interaction surface:** one-hit physical stability against the same impact.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique is narrower than a sustained stance, but it still asks for a real armored body correction under live pressure. It protects only one incoming hit, does not move the user, does not intercept for allies, and does not create an ongoing line bonus.

**Effect:** When the trigger occurs, declare the struck zone and the armor competency you are using for this Technique.

If the triggering hit does not explicitly bypass armor and the declared armor piece on that zone still functions, add a bonus equal to the rank bonus of that armor competency to that zone's `Bloqueo` against that one hit.

If that same hit would also force an `R.R.` against `Derribado` or `Desequilibrado` through bodily impact, shove, collision, or posture-breaking force, add the same rank bonus to that `R.R.` as well.

`Volver la Placa` only changes how this one hit is received. It does not remain active after resolution and does not create an `active armor posture`.

**Restrictions:**

- only works with `Armadura intermedia` or `Armadura pesada`
- only works if the struck zone is actually protected by the declared armor and that armor still functions
- does not function if the attack or effect explicitly bypasses armor entirely
- does not improve `T.D.`, intercept for allies, create cover, or establish a sustained defensive line
- does not help against poison, fear, curses, taumatic pressure, sensory overload, mental influence, social pressure, or other non-physical effects
- does not reduce forced movement distance by itself and does not preserve a held point beyond the one-hit `R.R.` bonus; use other Techniques for anti-displacement or anchored defense
- does not stack with `Cerrar la Coraza` on the same hit unless a later rule explicitly says otherwise

### Bajar el Núcleo

| Field | Value |
| --- | --- |
| `name` | Bajar el Núcleo |
| `name_en` | Lower the Core |
| `origin` | Aclimatación + Heat Resistance |
| `world_origin` | Species: Sauri; seed: Vessel Under Pressure / Stone Remembers Pressure; transmission: kiln-court endurance drills, exposed labor under heat load, and desert-edge crossing discipline; availability: Restricted |
| `category` | utility |
| `type` | passive |
| `trigger` | The user makes an `Aclimatación` Specialization Roll to resist a declared heat-origin environmental hazard that could impose Fatigue, exposure degradation, or similar thermal burden. |
| `requirements` | Minimum rank: Novice; Aclimatación at Novice or higher; Heat Resistance at Novice or higher; the roll must be specifically resisting a heat-origin environmental hazard rather than a weapon, spell, or non-thermal source. |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | permanent while both prerequisites remain at Novice or higher |
| `cost` | Rhythm 0; Attrition 0 — cost was paid in acclimation and exposure training, not in the ATB |
| `saving_roll` | none |
| `tags` | utility, hazard, mitigation, endurance, stability |

**Fantasy:** The body does not become cool. It becomes ordered. Breath shortens, blood slows, effort narrows, and the worst of the heat is kept away from the core long enough to finish the crossing, the lift, the hold, or the duty that cannot wait for shade.

**World origin:** Sauri who work exposed terraces, kiln courts, reservoir stone, and desert-edge crossings are taught that heat kills the unprepared twice: once through the body, and once through panic. Proper acclimation teaches the body to accept the outer burden without letting the inner function spill first.

**Why this is not raw Aclimatación:** Raw `Aclimatación` already governs whether the body can function under hostile climate or exposure. `Bajar el Núcleo` makes one class of those rolls better in a specific way: when the pressure is thermal, the user's trained heat tolerance becomes an extra bonus rather than just background fiction.

**Why this is not raw Heat Resistance:** Raw `Heat Resistance` is the body's native or conditioned tolerance to heat. `Bajar el Núcleo` hybridizes that tolerance with practiced `Aclimatación`, letting the resistance contribute directly to the exposure roll instead of existing only as background susceptibility logic.

**Primary interaction surface:** improved `Aclimatación` rolls against heat-origin environmental hazards.

**Secondary interaction surface:** Fatigue and exposure stability, because better thermal survival rolls make heat-driven degradation less likely to settle.

**Cost note:** `Rhythm 0 / Attrition 0` is correct and deliberate. This is a passive hybrid like the Naghii resistance models. The cost was paid in exposure, acclimation, and training long before the scene began; no declared action is needed when the body is already trained to answer heat better.

**Effect:** When you make an `Aclimatación` Specialization Roll specifically to resist a declared heat-origin environmental hazard — such as sun-baked exposure, radiant stone, kiln wash, furnace-side heat, steam-adjacent thermal load, or similar non-weapon heat pressure — add a bonus to that roll equal to your `Heat Resistance` rank bonus.

| Heat Resistance rank | Bonus |
| --- | --- |
| Novice | `+1` |
| Adept | `+2` |
| Expert | `+3` |
| Master | `+4` |
| Consummate | `+5` |
| Transcendent | `+6` |

This bonus applies only to `Aclimatación` rolls against heat-origin environmental hazards. It does not create shelter, remove existing Fatigue, protect allies, or change what those hazards do on success or failure; it only improves the user's chance to resist them cleanly.

**Restrictions:**

- requires `Aclimatación` at Novice or higher
- requires `Heat Resistance` at Novice or higher
- applies only to `Aclimatación` rolls against declared heat-origin environmental hazards already present in the scene
- does not help against weapon hits, direct fire attacks, explosions, poison, curses, taumatic pressure, mental influence, or non-heat hazards by itself
- does not create a refuge point, cover, line protection, or separate shelter window
- affects the user only
- does not reduce or clear Fatigue after it has already settled; it only improves the qualifying roll that may prevent that outcome

### Nombrar el Umbral

| Field | Value |
| --- | --- |
| `name` | Nombrar el Umbral |
| `name_en` | Name the Threshold |
| `origin` | Teología + Affliction Resistance |
| `world_origin` | Species: Sauri; seed: Preserved Witness / The Failed Vessel; transmission: funerary doctrine, vestige-handling liturgy, and temple instruction on naming what passes through the vessel; availability: Restricted |
| `category` | utility |
| `type` | passive |
| `trigger` | The user interacts with a `Vestigio` or `Vínculo` and must make an `Affliction R.R.` to avoid increasing by `1` the intensity of an already-settled extranatural sensory Affliction. |
| `requirements` | Minimum rank: Novice; Teología at Novice or higher; Affliction Resistance at Novice or higher; an extranatural sensory Affliction must already be present; the triggering escalation must come specifically from interaction with a `Vestigio` or `Vínculo`. |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | permanent while both prerequisites remain at Novice or higher |
| `cost` | Rhythm 0; Attrition 0 — cost was paid in doctrinal training and repeated exposed contact, not in the ATB |
| `saving_roll` | none |
| `tags` | utility, corruption, condition_reduction, stability, doctrinal |

**Fantasy:** The contact still opens the world. The difference is that the Sauri does not meet it as raw intrusion. The doctrine gives the phenomenon a place, a lineage, a boundary, a name. What enters is still dangerous, but it no longer arrives as shapeless flood.

**World origin:** Sauri vestige doctrine teaches that a dangerous contact becomes worse when it is taken as undifferentiated force. Temple readers, funerary handlers, and vessel-keepers are trained to classify what kind of intrusion is happening and what boundary it is trying to cross. The doctrine does not seal the opening. It prevents the opening from widening as easily.

**Why this is not raw Teología:** Raw `Teología` interprets the doctrine, symbols, lineage, or doctrinal frame of the contact. `Nombrar el Umbral` turns that doctrinal literacy into a defensive effect: when the user already carries the sensory fracture, naming the kind of intrusion helps keep the next contact from driving it deeper.

**Why this is not raw Affliction Resistance:** Raw `Affliction Resistance` is the being's capacity to withstand the destabilizing pressure that would deepen an extranatural sensory Affliction. `Nombrar el Umbral` hybridizes that resistance with doctrine: the body resists better because the mind and ritual frame have correctly identified what is crossing into it.

**Primary interaction surface:** resisting `+1 intensity` escalation on extranatural sensory Afflictions caused by `Vestigio` or `Vínculo` contact.

**Secondary interaction surface:** stability, because the Technique makes repeated controlled contact less likely to push the user into worse sensory distortion.

**Cost note:** `Rhythm 0 / Attrition 0` is correct and deliberate. This is a passive hybrid like the other resistance models. The cost was paid in doctrine, repeated contact, and learning to survive naming what should not be touched.

**Effect:** When you interact with a `Vestigio` or `Vínculo` and must make an `Affliction R.R.` to avoid increasing by `1` the intensity of an already-settled extranatural sensory Affliction, add a bonus to that `R.R.` equal to your `Affliction Resistance` rank bonus.

| Affliction Resistance rank | Bonus |
| --- | --- |
| Novice | `+1` |
| Adept | `+2` |
| Expert | `+3` |
| Master | `+4` |
| Consummate | `+5` |
| Transcendent | `+6` |

This bonus applies only to intensity-escalation `Affliction R.R.` caused by `Vestigio` or `Vínculo` interaction. It does not prevent the initial contact, remove the Affliction, erase its extranatural perception benefit, or protect against unrelated Alterations.

**Restrictions:**

- requires `Teología` at Novice or higher
- requires `Affliction Resistance` at Novice or higher
- applies only when a `Vestigio` or `Vínculo` interaction would increase by `1` the intensity of an already-settled extranatural sensory Affliction
- does not help against mundane sensory disorders, weapon hits, poison, curses unrelated to `Vestigios`/`Vínculos`, or non-extranatural Alterations
- does not prevent the initial settling of an Affliction unless a later system explicitly says those same rolls also count as intensity escalation from zero
- does not reduce, clear, or recover intensity after it has already increased; it only improves the qualifying `Alteration R.R.` that may prevent the increase
- affects the user only

### Hacer Esperar la Podredumbre

| Field | Value |
| --- | --- |
| `name` | Hacer Esperar la Podredumbre |
| `name_en` | Make the Rot Wait |
| `origin` | Tolerancia + Infection Resistance |
| `world_origin` | Species: Zarnag; seed: Distinguish the Survivable from the Corrupting; transmission: plague-line labor, corpse-side endurance drills, and infection discipline under foul exposure; availability: Restricted |
| `category` | utility |
| `type` | passive |
| `trigger` | A mundane Infection settles on the user after a qualifying exposure and that Infection has a declared incubation period. |
| `requirements` | Minimum rank: Novice; `Tolerancia` at Novice or higher; `Infection Resistance` at Novice or higher; the source must be a real infection-family contamination rather than poison, curse, Affliction, or purely taumatic corruption. |
| `target` | self |
| `range` | self |
| `area` | self |
| `duration` | permanent while both prerequisites remain at Novice or higher |
| `cost` | Rhythm 0; Attrition 0 — cost was paid in exposure, foul-work conditioning, and learned bodily discipline, not in the ATB |
| `saving_roll` | none |
| `tags` | utility, mitigation, endurance, contamination, incubation |

**Fantasy:** The body does not win by staying untouched. It wins by making the rot arrive slower. Fever, swelling, black streak, bad breath, and organ-fail pressure are still coming, but not on the same clock they would claim from cleaner flesh.

**World origin:** Zarnag corpse-haulers, trench clearers, foul-water workers, and plague-line walkers learn early that the first task after exposure is not panic. It is timing. Their endurance discipline teaches the body not to open itself wider through bad strain, bad scratching, bad breathing, bad exertion, or frightened overreaction. The Infection may still take hold, but it is forced to work on a slower timetable before symptoms surface.

**Why this is not raw `Infection Resistance`:** Raw `Infection Resistance` decides whether the Infection settles at all. `Hacer Esperar la Podredumbre` does nothing until after that question is already answered. If the Infection gets in, the Technique forces it to reveal symptoms more slowly.

**Why this is not raw `Tolerancia`:** Raw `Tolerancia` helps the body keep functioning under burden. `Hacer Esperar la Podredumbre` uses that same discipline earlier in the infection cycle: not to erase the burden, but to delay the point where the burden starts showing itself as active symptoms.

**Primary interaction surface:** incubation delay on already-settled mundane Infections.

**Secondary interaction surface:** survival window, because more incubation time means more opportunity to isolate, warn others, seek treatment, or finish necessary labor before the Infection becomes active.

**Cost note:** `Rhythm 0 / Attrition 0` is correct and deliberate. This is a passive hybrid like the other resistance models. The cost was paid in repeated foul exposure, hard instruction, and learning how not to spend the body's time badly in the first moments after contamination.

**Effect:** When a mundane Infection with a declared incubation period settles on you after all qualifying `Infection R.R.` processing, extend that Infection's incubation by one additional interval equal to its own listed incubation period before symptoms become active.

If an Infection normally incubates for:

- hours, it takes those hours again before symptoms manifest
- days, it takes those days again before symptoms manifest
- another declared period, repeat that same period once before the Infection becomes active

This Technique does not cancel the Infection, reduce its severity, or prevent later propagation once the Infection becomes active. It only delays symptom onset by making the incubation last longer.

**Restrictions:**

- requires `Tolerancia` at Novice or higher
- requires `Infection Resistance` at Novice or higher
- applies only after a mundane Infection has already settled
- applies only to Infections that actually have a declared incubation period
- does not help against poison, curse, Affliction, Alteration, fear, command pressure, or purely taumatic corruption
- does not remove or reduce an Infection after it has already settled
- does not prevent later propagation once the Infection becomes active
- affects the user only

### Mantener Cerrada la Línea de Contagio

| Field | Value |
| --- | --- |
| `name` | Mantener Cerrada la Línea de Contagio |
| `name_en` | Keep the Contagion Line Closed |
| `origin` | Medicina + Infection Resistance |
| `world_origin` | Species: Zarnag; seed: Distinguish the Survivable from the Corrupting; transmission: corpse-side triage, plague-front wound sorting, and septic handling discipline; availability: Restricted |
| `category` | utility |
| `type` | passive |
| `trigger` | The user makes a `Medicina` Specialization Roll specifically to isolate, wrap, bind, mask, drain, or otherwise keep an already active mundane Infection from propagating through valid contact from one self or adjacent carrier. |
| `requirements` | Minimum rank: Novice; `Medicina` at Novice or higher; `Infection Resistance` at Novice or higher; the target problem must be a real mundane infection-family contamination rather than poison, curse, Affliction, or purely taumatic rot. |
| `target` | self or adjacent creature |
| `range` | touch / adjacent |
| `area` | one active infected carrier and the treatment line being contained |
| `duration` | permanent while both prerequisites remain at Novice or higher |
| `cost` | Rhythm 0; Attrition 0 — cost was paid in supervised foul triage and infection-handling practice, not in the ATB |
| `saving_roll` | none |
| `tags` | utility, mitigation, triage, contamination, containment |

**Fantasy:** The sickness is already inside. The question now is whether it gets out through the same hands, cloth, fluid, breath, or seepage that kept the carrier alive long enough to be treated. The Zarnag closes that line before the sick body becomes the next source.

**World origin:** Zarnag plague-front medicine is not only about saving the present body. It is also about preventing the present body from becoming the next open source. Corpse-side attendants, trench medics, and foul-water binders are trained to wrap, isolate, drain, mask, and handle active Infection in ways that keep care from becoming propagation.

**Why this is not raw `Medicina`:** Raw `Medicina` can already treat wounds and perform broad field care. `Mantener Cerrada la Línea de Contagio` is narrower: it is specifically about keeping an already active Infection from using treatment contact, wrapped seepage, or ordinary handling as its next propagation route.

**Why this is not raw `Infection Resistance`:** Raw `Infection Resistance` helps a body resist becoming infected. `Mantener Cerrada la Línea de Contagio` does not alter that body's resistance roll directly. It improves the practitioner's ability to keep an active carrier from spreading the Infection outward during the current treatment window.

**Primary interaction surface:** improved `Medicina` rolls that specifically establish non-propagating treatment containment on an already active mundane Infection.

**Secondary interaction surface:** contact containment, because successful treatment can keep one active carrier from infecting the next body through ordinary handling.

**Cost note:** `Rhythm 0 / Attrition 0` is correct and deliberate. This is a passive hybrid like the other resistance models. The cost was paid in supervised foul triage, plague-front handling, and repeated practice keeping infected care from becoming fresh spread.

**Effect:** When you make a `Medicina` Specialization Roll specifically to isolate, wrap, bind, mask, drain, or otherwise keep an already active mundane Infection from propagating through ordinary physical contact from one self or adjacent carrier, add a bonus to that roll equal to your `Infection Resistance` rank bonus.

| `Infection Resistance` rank | Bonus |
| --- | --- |
| Novice | `+1` |
| Adept | `+2` |
| Expert | `+3` |
| Master | `+4` |
| Consummate | `+5` |
| Transcendent | `+6` |

If that qualifying `Medicina` roll succeeds, the treated Infection does not propagate through ordinary physical contact from that carrier while the containment remains materially intact, up to the end of the current scene.

This does not stop other vectors the Infection entry still defines, does not cure the carrier, and does not survive torn wrappings, removed seals, burst drainage, or other clear containment failure.

**Restrictions:**

- requires `Medicina` at Novice or higher
- requires `Infection Resistance` at Novice or higher
- applies only to `Medicina` rolls addressing an already active mundane Infection that could validly propagate through contact
- does not help against poison, curse, Affliction, Alteration, fear, command pressure, or purely taumatic corruption
- does not remove or reduce the Infection by itself
- does not block non-contact vectors the Infection entry still defines
- ends if the containment is materially broken, removed, or no longer intact
- affects one current treatment target only

### Ensuciar la Herida

| Field | Value |
| --- | --- |
| `name` | Ensuciar la Herida |
| `name_en` | Foul the Wound |
| `origin` | Bite |
| `world_origin` | Species: Zarnag; seed: Carrion Contact Changes The Exchange; transmission: carrion bite discipline and foul-contact work; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user has close contact against a creature whose next clean bodily action can still be spoiled by foul residue, pain, or contamination pressure left at the wound site. |
| `requirements` | Minimum rank: Novice; weapon profile: Corrosion; any weapon competency, natural attack form, or specific item that grants Corrosion access can use this Technique unless this Technique narrows that access; narrowed access: the attack must deliver bite or other close hostile-residue contact; the target must have a plausible wound surface or breach point |
| `target` | creature |
| `range` | close contact |
| `area` | single |
| `duration` | until the wound is cleared with `Interact`, or no longer tracked as a meaningful treatment problem |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the hostile residue |
| `tags` | attack, corrosion, disruption, foul_contact |

**Fantasy:** The first wound is not the whole problem. The Zarnag leaves the contact dirty enough that anyone trying to treat it now has to work through debris, filth, and hostile residue before the wound can be handled cleanly.

**World origin:** Zarnag carrion labor teaches that some contact keeps working after the bite, cut, or tear is already over. A bad wound attracts filth, compromises movement, and changes judgment. `Ensuciar la Herida` comes from that practical truth: once the body is opened wrongly, the next decision is no longer clean.

**Why this is not a base Bite attack:** A base bite only tries to hit and injure. `Ensuciar la Herida` turns the contact into a treatment problem. The target is pressured not because the hit did more damage, but because the wound is now materially harder to stabilize or clean until the fouling is actually removed.

**Primary interaction surface:** close corrosive or contaminating contact.

**Secondary interaction surface:** treatment denial, because the wound becomes harder to address cleanly until the hostile residue is removed.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique is an attack that also creates a persistent treatment problem around hostile residue. These costs apply only during ATB or another active-threat scene; in normal exploration, the Technique resolves as the user's foul-contact action without Attrition.

**Effect:** Make a profile-bearing close attack with a bite or another narrowed-access foul-contact delivery. If the Technique resolves successfully, the target becomes wound-fouled until the duration ends.

While the wound remains fouled, any `Medicina` Specialization Roll or `Medicine`-origin Technique check that directly treats, stabilizes, binds, cleans, or prevents worsening of that wound takes a situational penalty equal to the rank bonus of the competency used for this Technique until the wound has first been cleared through the specific procedural response below.

| Competency rank used | Treatment penalty |
| --- | --- |
| Novice | `-1` |
| Adept | `-2` |
| Expert | `-3` |
| Master | `-4` |
| Consummate | `-5` |
| Transcendent | `-6` |

Valid procedural response:

- `self_clear`: the fouled target uses `Interact` under pressure to wipe, flush, scrape, or otherwise clear the wound enough to stop the treatment penalty

This Technique does not normally call for `quick_identification`. The pressure is usually obvious: the wound is materially foul and must be cleaned before clean treatment can proceed.

`Medicina` still matters after that step. It stabilizes, treats, or heals the wound once the fouling has been cleared, but it is not itself the step that removes this Technique's state.

This Technique does not apply a generic disease, does not increase direct damage by itself, and does not create a permanent infection track on its own. It makes the wound materially dirtier and therefore harder to treat cleanly until that fouling is actually removed.

**Restrictions:**

- requires real close contact that can leave hostile residue
- non-natural users need a credible foul-contact tool or delivery method
- target must have a plausible wound surface or breach point
- applies to one creature only
- only penalizes `Medicina` rolls or `Medicine`-origin Techniques that directly address the fouled wound
- does not penalize unrelated actions or unrelated treatment
- does not stack with itself on the same target
- does not replace real disease, infection, or Affliction rules by itself

### Reír en la Brecha

| Field | Value |
| --- | --- |
| `name` | Reír en la Brecha |
| `name_en` | Laugh in the Gap |
| `origin` | Evasion |
| `world_origin` | Species: Zarnag; seed: The Laugh Breaks Nerve First; transmission: close mockery pressure and wrong-angle entry; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user can make close hostile contact and immediately crowd the target's read with laughter, body pressure, or wrong-angle follow-in before the target restores clean orientation. |
| `requirements` | Minimum rank: Novice; weapon profile: Shadow Pressure; any weapon competency, natural attack form, or specific item that grants Shadow Pressure access can use this Technique unless this Technique narrows that access; narrowed access: the attack must deliver close predatory contact and let the user maintain immediate pressure after contact |
| `target` | creature |
| `range` | close contact |
| `area` | single |
| `duration` | until the target resolves the first penalized roll, or reaches the end of its next activation |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the spoiled read |
| `tags` | attack, shadow_pressure, pressure, close_disruption |

**Fantasy:** The Zarnag does not win this moment by making the wound worse. It wins it by becoming the wrong thing to answer cleanly: too close, too ugly, too loud, too immediate. The laugh lands in the gap before the target's next clean choice does.

**World origin:** Zarnag fear discipline teaches that morale often breaks one beat before flesh does. Carrion outriders, trench harriers, and grave-line enforcers learn how to turn a snap of laughter, a crooked shoulder entry, or a bad-angle follow-in into a pressure moment that steals the enemy's clean read.

**Why this is not raw Intimidación:** Raw `Intimidación` pressures resolve through will, authority, nerve, or social force. `Reír en la Brecha` is weaponized close-contact confusion. The target is not being convinced of anything. Its next answer is being made worse because the Zarnag is suddenly in the wrong place, at the wrong angle, at the wrong distance.

**Primary interaction surface:** close `Shadow Pressure` that spoils the target's next clean answer.

**Secondary interaction surface:** near-term answer pressure, because the tax only applies to the target's first direct answer against the user and then expires.

**Cost note:** `Rhythm 4 / Attrition 1` is deliberate. The Technique converts contact into a bounded tactical tax on one near-term direct answer. That is meaningful pressure, but it stays tightly constrained to one target, one follow-up roll, and only against the user who created the pressure.

**Effect:** Make a profile-bearing close attack with claws, bite, or another narrowed-access intimate pressure surface. If the Technique resolves successfully, the target becomes `read-spoiled` until the duration ends.

While `read-spoiled`, the first `D.R.` or `A.R.` the target makes directly against the user takes a situational penalty equal to the rank bonus of the competency used for this Technique.

| Competency rank used | Roll penalty |
| --- | --- |
| Novice | `-1` |
| Adept | `-2` |
| Expert | `-3` |
| Master | `-4` |
| Consummate | `-5` |
| Transcendent | `-6` |

This Technique does not require `quick_identification`, cleansing, or technical handling. It also does not need a separate clearing route: the effect is already bounded to one target and one near-term `D.R.` or `A.R.` against the user.

**Restrictions:**

- requires real close contact and immediate follow-in pressure
- non-natural users need a credible close surface for `Shadow Pressure`
- only penalizes the first `D.R.` or `A.R.` the target makes directly against the user
- applies to one creature only
- does not stack with itself on the same target
- does not penalize unrelated rolls against other creatures
- does not create fear magic, compulsion, or long-form morale damage by itself

### Abrir la Costura

| Field | Value |
| --- | --- |
| `name` | Abrir la Costura |
| `name_en` | Open the Seam |
| `origin` | Evasion |
| `world_origin` | Species: Zarnag; seed: The Scavenger Follows The Weak Line; transmission: body-line reading and close rip follow-up; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user can make close tearing contact against a creature whose posture, wound line, or protective body angle is already weak enough to be opened further by follow-through. |
| `requirements` | Minimum rank: Novice; weapon profile: Rend; any weapon competency, natural attack form, or specific item that grants Rend access can use this Technique unless this Technique narrows that access; narrowed access: the attack must deliver tearing close contact and the target must have a plausible body line or protection line to open |
| `target` | creature |
| `range` | close contact |
| `area` | single |
| `duration` | until the first qualifying `Impact Roll` benefits from the opened seam, or until the end of the user's next activation |
| `cost` | Rhythm 4; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the opened seam |
| `tags` | attack, rend, setup, tearing |

**Fantasy:** The Zarnag does not always need to win by tearing hardest in the first instant. Sometimes the correct answer is to open the line that was already beginning to fail, then come through it properly on the next committed entry.

**World origin:** Zarnag route readers and close skirmishers survive by seeing where a wall, trench edge, scavenger path, or body line is already giving way. `Abrir la Costura` brings that logic into flesh: first contact does not just hurt, it makes the next true entry cleaner by opening what was already weakening.

**Why this is not raw damage:** A base tearing strike just tries to injure. `Abrir la Costura` is about follow-through value. The first contact matters because it leaves the target worse for the user's next Impact, not because it immediately adds more damage by itself.

**Primary interaction surface:** `Rend` through tearing contact that opens the target's line.

**Secondary interaction surface:** bounded self-setup, because the benefit only applies to the user's next qualifying `Impact Roll` against the same target.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique is an attack that turns first contact into a delayed material opening. The payoff is real, but it is limited to one target, one follow-up `Impact Roll`, and a short timing window.

**Effect:** Make a profile-bearing close attack with claws, bite, or another narrowed-access tearing surface. If the Technique resolves successfully, the target becomes `seam-opened` until the duration ends.

While `seam-opened`, the first `Impact Roll` made by the user against that same target ignores `Block` equal to the rank bonus of the competency used for this Technique.

| Competency rank used | Block ignored |
| --- | --- |
| Novice | `1` |
| Adept | `2` |
| Expert | `3` |
| Master | `4` |
| Consummate | `5` |
| Transcendent | `6` |

This Technique does not require cleansing, diagnosis, or a separate clearing route. It is already bounded to one target, one follow-up `Impact Roll` from the same user, and one short timing window.

**Restrictions:**

- requires real close tearing contact
- non-natural users need a credible rending surface or tool
- only benefits the first `Impact Roll` made by the same user against the same target
- applies to one creature only
- does not stack with itself on the same target
- does not help allies or unrelated attacks
- does not ignore `Defense`, only `Block`
- does not create persistent bleed, infection, or open-ended vulnerability by itself

### Atajar el Brote

| Field | Value |
| --- | --- |
| `name` | Atajar el Brote |
| `name_en` | Cut Off the Spread |
| `origin` | Bite |
| `world_origin` | Species: Zarnag; seed: Better To Strike Before Rot Spreads; transmission: committed rush before worsening contact; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user judges that waiting is worse than committing and can enter close contact immediately after real forward movement toward the target. |
| `requirements` | Minimum rank: Novice; weapon profile: Charge; any weapon competency, natural attack form, or specific item that grants Charge access can use this Technique unless this Technique narrows that access; narrowed access: the attack must follow real forward movement toward the target and end in close contact |
| `target` | creature |
| `range` | close contact |
| `area` | single |
| `duration` | immediate |
| `cost` | Rhythm 7; Attrition 2 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the breakthrough Impact benefit |
| `tags` | attack, charge, breakthrough, committed_entry |

**Fantasy:** The Zarnag does not wait for the line to get cleaner. It judges that waiting is how rot spreads, panic hardens, or the route gets worse. The answer is ugly commitment now, before the target or the field has time to become a bigger problem.

**World origin:** Plague breakers, hard-use hunting parties, and breach-line followers learn that some dangers should not be given another breath, another step, or another moment to reorganize. `Atajar el Brote` turns that judgment into action: forward entry first, clean recovery later if there is still time.

**Why this is not raw movement plus bite:** A normal rush into a bite only changes distance. `Atajar el Brote` converts that committed entry into immediate breakthrough value on the same hit. The point is not just arriving. It is arriving hard enough that the target's `Block` fails to answer cleanly in that instant.

**Primary interaction surface:** `Charge` through committed close entry and same-hit breakthrough.

**Secondary interaction surface:** timing pressure, because the Technique only exists when the user accepts that delay is mechanically worse than costly commitment.

**Cost note:** `Rhythm 7 / Attrition 2` is deliberate. This is heavier than the earlier Zarnag novice attacks because it includes real forward entry plus immediate Block-breaking value on the same strike. It should feel like an expensive but correct answer when hesitation is judged worse.

**Effect:** Move into close contact with the target as part of the same committed action, then make a profile-bearing close attack with bite or another narrowed-access breakthrough surface.

If the Technique resolves successfully, the `Impact Roll` of that same attack ignores `Block` equal to the rank bonus of the competency used for this Technique.

| Competency rank used | Block ignored |
| --- | --- |
| Novice | `1` |
| Adept | `2` |
| Expert | `3` |
| Master | `4` |
| Consummate | `5` |
| Transcendent | `6` |

This Technique does not create a lasting state, a follow-up setup, or a clearing route. Its value is immediate: strike before worsening has time to multiply.

**Restrictions:**

- requires real forward movement toward the target before the attack
- non-natural users need a credible breakthrough surface or tool
- only benefits the `Impact Roll` of the same attack that carried the rush
- applies to one creature only
- does not stack with other instances of itself on the same attack
- does not ignore `Defense`, only `Block`
- does not grant free displacement or extra movement beyond the committed entry
- does not create persistent opening or follow-up state by itself

### Robar la Orilla

| Field | Value |
| --- | --- |
| `name` | Robar la Orilla |
| `name_en` | Steal the Edge |
| `origin` | Claws |
| `world_origin` | Species: Zarnag; seed: The Scavenger Follows The Weak Line; transmission: short entry, cut, and exit timing; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user can enter close enough to cut the target's edge and still keep enough body freedom to slip back out before becoming fully committed. |
| `requirements` | Minimum rank: Novice; weapon profile: Skirmish; any weapon competency, natural attack form, or specific item that grants Skirmish access can use this Technique unless this Technique narrows that access; narrowed access: the attack must use a light close surface and the user must have room to exit after contact |
| `target` | creature |
| `range` | close contact |
| `area` | single |
| `duration` | immediate |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the reposition benefit |
| `tags` | attack, skirmish, mobility, edge_theft |

**Fantasy:** The Zarnag does not stay where the exchange is thickest. It takes the edge, cuts once, and slips out before the body line closes around it.

**World origin:** Flank-runners, ruin pickers, and bad-ground harriers survive by stealing the dangerous outer edge of a line instead of contesting its center. `Robar la Orilla` applies that field truth to combat: first contact is useful because it creates a safe peel-off, not because it demands a held struggle.

**Why this is not raw movement after an attack:** A normal attack followed by later movement leaves a tempo gap and pays for the reposition separately. `Robar la Orilla` binds the cut and the exit into one trained action, but only in a light skirmish form and only when the attack truly lands.

**Primary interaction surface:** `Skirmish` through light contact plus immediate slip-out.

**Secondary interaction surface:** mobility, because the reward is controlled exit timing rather than direct damage conversion or line-breaking force.

**Cost note:** `Rhythm 4 / Attrition 1` is deliberate. The Technique is a full attack, but its payoff is only a light slip-out. It should feel agile and useful without pricing itself like the heavier setup, breakthrough, or shared disruption attacks in the same species set.

**Effect:** Make a profile-bearing close attack with claws or another narrowed-access light skirmish surface.

If the Technique resolves successfully, after the attack the user may immediately reposition up to half of its normal `Movement` distance without paying an additional `Rhythm` cost.

This reposition must remain physically plausible, must not pass through an occupied hostile body space the user could not normally cross, and must represent a real slip-out, lateral peel, or retreating edge step rather than a second engagement burst.

**Restrictions:**

- requires a light close surface with `Skirmish` access
- user must have real room to reposition after contact
- reposition occurs only if the attack successfully resolves
- reposition is limited to half normal `Movement` distance
- reposition does not ignore terrain or occupation limits
- applies to one creature only
- does not grant a second attack
- does not create long-duration pressure or follow-up state by itself

### Quebrar la Vuelta

| Field | Value |
| --- | --- |
| `name` | Quebrar la Vuelta |
| `name_en` | Break the Turn |
| `origin` | Evasion |
| `world_origin` | Species: Zarnag; seed: The Scavenger Follows The Weak Line; transmission: wrong-side recovery and close-line break; availability: Common |
| `category` | defense |
| `type` | reactive |
| `trigger` | An enemy in close contact makes a physical attack against the user and the user still has enough body freedom to slip to the wrong side of the attack line before the hit fully settles. |
| `requirements` | Minimum rank: Novice; defensive competency: Evasion; user and attacker must already be in close contact; the user must still have enough freedom to shift angle inside that contact |
| `target` | attacking enemy |
| `range` | close contact |
| `area` | self and one attacking enemy |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` gates the Technique |
| `tags` | defense, evasion, reaction, angle_break |

**Fantasy:** The attacker turns into the place they thought the Zarnag would still occupy and finds the body already broken off that line. The answer was committed to something real, but no longer to something present.

**World origin:** Harriers, carcass-circle duelists, and wrong-line cutters learn that close exchanges are lost by the fighter who remains where the enemy expects. `Quebrar la Vuelta` expresses that habit reactively: let the attacker finish choosing the line, then make that line wrong at the last useful instant.

**Why this is not raw movement or generic Evasion:** A normal reposition does not automatically spoil an attack that is already turning in, and base `Evasion` alone does not explain the specifically false-angle close logic. `Quebrar la Vuelta` is about making the attacker commit to the wrong turn inside an already-settled close exchange.

**Primary interaction surface:** `Evasion` through false read and late angle break.

**Secondary interaction surface:** light close reposition, because a successful defended break lets the user settle on a different immediate angle without paying a second action.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. This is a narrow reactive defense: one close attack, one defended angle break, and one light reposition only if the defense succeeds. It should feel sharp and useful without becoming a universal escape or a full interception technique.

**Effect:** When the triggering close attack is declared, make your `D.R.` against it with an additional situational bonus equal to the rank bonus of your `Evasion` competency.

| Evasion rank used | Additional `D.R.` bonus |
| --- | --- |
| Novice | `+1` |
| Adept | `+2` |
| Expert | `+3` |
| Master | `+4` |
| Consummate | `+5` |
| Transcendent | `+6` |

If that `D.R.` succeeds, after the exchange resolves you may immediately reposition to another physically plausible close angle around the attacker without paying additional `Rhythm`, as long as you remain in close contact.

This Technique does not create lasting pressure, a follow-up attack bonus, or a clearing route. Its value is immediate: the attacker answered the wrong line, and you are no longer where that answer expected.

**Restrictions:**

- requires existing close contact with the attacker
- requires enough bodily freedom to support a real late angle shift
- only applies against the triggering close attack
- reposition occurs only if the `D.R.` succeeds
- reposition must remain within close contact against the attacker
- does not grant free disengagement or long reposition
- does not replace the user's `Attack Roll` or create a counterattack
- does not create persistent confusion, social fear, or follow-up bonus by itself

### Soltar la Capa Muerta

| Field | Value |
| --- | --- |
| `name` | Soltar la Capa Muerta |
| `name_en` | Shed the Dead Layer |
| `origin` | Light Armor |
| `world_origin` | Species: Zarnag; seed: Distinguish the Survivable from the Corrupting; transmission: outer-wrap shedding drills, carrion apron release work, and bad-contact escape practice; availability: Common |
| `category` | defense |
| `type` | reactive |
| `trigger` | A physical attack, grab, or contact-dependent Technique is about to land on a zone protected by your functional light armor or expendable outer layer, and you still have enough body freedom to let that outer layer take the line instead of the body. |
| `requirements` | Minimum rank: Novice; defensive competency: Light Armor; the struck zone must be covered by functional light armor or an expendable outer layer, and the user must not be fully restrained or immobilized |
| `target` | self |
| `range` | self |
| `area` | one incoming hit or contact line |
| `duration` | instant |
| `cost` | Rhythm 3; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` gates the Technique |
| `tags` | defense, light_armor, reaction, contact_denial |

**Fantasy:** The body is already slipping free when the bad hand closes. If there is a loose apron, wrap, or hanging layer, it is what gets caught instead of the real line.

**World origin:** Zarnag foul-work elders and pit-edge runners learn early that a cheap outer layer is worth less than a clean hold on the body. Aprons, wraps, slings, tied hides, and ragged layers are not only for weather or filth; they are also something you can afford to lose when a bad hand, bad tooth, or bad hook comes in wrong. `Soltar la Capa Muerta` is that lesson under pressure.

**Why this is not raw `Light Armor`:** Raw `Light Armor` already supports a good `D.R.` while preserving mobility. `Soltar la Capa Muerta` pushes that evasive logic further by converting one successful defense into an immediate peel-out, and, when a loose outer layer exists, into a spoiled grip on the wrong thing.

**Primary interaction surface:** `D.R.` through `Light Armor` as evasive peel and false purchase denial.

**Secondary interaction surface:** immediate angle recovery, because a successful evasive peel leaves the user in a better short position instead of held contact.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. This is a narrow reactive evasive defense: one defended contact line and one short peel-out if the defense succeeds. It should feel practical and sharp without turning light armor into mitigation, universal escape, or full anti-grapple immunity.

**Effect:** Make your `D.R.` against the triggering attack using `Light Armor`.

If that `D.R.` fails, the Technique fails and the attack resolves normally.

If that `D.R.` succeeds, you may immediately reposition 1 meter to a legal adjacent space without paying additional `Rhythm`.

This Technique does not improve `Bloqueo`, does not protect another creature, and does not require sacrificing equipment to gain the peel-out. Its value is the evasive exit itself.

**Restrictions:**

- requires functional light armor or an expendable outer layer on the struck zone
- only applies against the triggering physical attack or contact line
- reposition occurs only if the `D.R.` succeeds
- reposition is limited to 1 meter and must end in a legal adjacent space
- does not help against area effects, mental pressure, non-physical effects, or attacks that never needed contact purchase
- does not protect another creature

### Cortar la Mano Tarde

| Field | Value |
| --- | --- |
| `name` | Cortar la Mano Tarde |
| `name_en` | Cut the Late Hand |
| `origin` | Claws + Bite |
| `world_origin` | Species: Zarnag; seed: Quarantine Is Force With A Moral Cost; transmission: no-touch line reaction drills; availability: Common |
| `category` | attack |
| `type` | reactive |
| `trigger` | An enemy within close contact begins a physical action that would grab, use, open, cross, pick up, or otherwise commit through a line, object, or body space the user is actively contesting at close range. |
| `requirements` | Minimum rank: Novice; weapon profile: Interruption; any weapon competency, natural attack form, or specific item that grants Interruption access can use this Technique unless this Technique narrows that access; the user must already be contesting the relevant line, object, or body space and have a fast close surface capable of spoiling the process |
| `target` | attacking enemy |
| `range` | close contact |
| `area` | self and one attacking enemy |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | replace normal `D.R.` with opposed `A.R.` against the triggering hostile roll |
| `tags` | attack, interruption, reaction, quarantine |

**Fantasy:** The enemy did not merely attack. They put a hand, tool, or body line where it should not have gone. The Zarnag does not answer after the process is complete. It answers at the exact late moment when that process can still be ruined.

**World origin:** Trench wardens, plague-line cutters, and carcass-route keepers learn that some lines must not be crossed cleanly, some seals must not be opened, and some objects must not be touched once the field has turned bad. `Cortar la Mano Tarde` is the combat form of that rule: spoil the process before the breach becomes real.

**Why this is not raw reaction damage:** A reactive strike by itself does not necessarily ruin what the enemy was trying to do. `Cortar la Mano Tarde` is a counterattack whose damage only matters if the timing actually tears the process apart.

**Primary interaction surface:** `Interruption` through late-hand process spoil.

**Secondary interaction surface:** quarantine pressure, because the Technique protects a contested bad line, object, or body space without needing a full persistent control state.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. This is not just a spoil; it replaces the normal defensive answer with a reactive counterattack that can both ruin the hostile process and deal damage on the same resolution. That permission belongs at the standard anchor even with its narrow trigger.

**Effect:** When the trigger occurs, the user may replace its normal `D.R.` against that one hostile attack or process with a reactive `Attack Roll` using claws, bite, or another narrowed-access interruptive close surface.

If the user's reactive `Attack Roll` equals or exceeds the triggering hostile roll, the hostile action is interrupted and does not resolve cleanly, and the user's interruptive contact deals normal damage.

If the user's reactive `Attack Roll` is lower, the hostile action resolves normally and this Technique deals no damage.

This Technique does not hold the enemy in place, create a lasting state, or replace broader lane denial. Its value is timing: the enemy reached in too late and lost the process.

**Restrictions:**

- requires a real contested line, object, or close body space
- non-natural users need a credible interruptive close surface or tool
- only applies to the triggering enemy and the triggering action
- the user must already be close enough to spoil the process
- does not create a persistent grapple or hold
- does not replace full `Line Control` or quarantine structure by itself
- applies to one creature only
- does not stack with itself on the same trigger

### Encontrar la Parte Blanda

| Field | Value |
| --- | --- |
| `name` | Encontrar la Parte Blanda |
| `name_en` | Find the Soft Part |
| `origin` | Bite + Claws |
| `world_origin` | Species: Zarnag; seed: The Scavenger Follows The Weak Line; transmission: compromised body read and exact finish work; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The target is already bodily compromised in a way that exposes a soft line: an existing wound, failed posture, collapse, pinned limb, open breath line, or another plausible finishing vulnerability. |
| `requirements` | Minimum rank: Novice; weapon profile: Lethality; any weapon competency, natural attack form, or specific item that grants Lethality access can use this Technique unless this Technique narrows that access; the target must already have a plausible soft line or vital opening, and the attack must be close and precise enough to exploit it |
| `target` | creature |
| `range` | close contact |
| `area` | single |
| `duration` | immediate |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the finishing benefit |
| `tags` | attack, lethality, finishing, precision |

**Fantasy:** The Zarnag does not attack the whole body. It attacks the part that has already stopped being equally alive, equally guarded, or equally able to resist.

**World origin:** Carrion judges, flank-cutters, and finishing knife keepers learn how to read the point where a body has become easier to end than to fight honestly. `Encontrar la Parte Blanda` is not about inventing a miracle opening. It is about recognizing the one that already exists and finishing through it cleanly.

**Why this is not raw damage:** A normal attack just tries to hit hard enough. `Encontrar la Parte Blanda` only gains value when the target is already compromised. Its value is not abstract damage inflation or hidden Block reduction. It is the ability to turn a real existing weak line into a cleaner chance of decisive contact.

**Primary interaction surface:** `Lethality` through exact finishing exploitation of an already exposed line.

**Secondary interaction surface:** judgment pressure, because the Technique only works when the user correctly identifies that the target has crossed from “hard to fight” into “possible to finish.”

**Cost note:** `Rhythm 4 / Attrition 1` is deliberate. This is a selective finishing strike, not a broad opener or heavy breakthrough. Its payoff is real, but it only exists when the target already presents a true vulnerable line and the user can exploit it in one exact finishing attempt.

**Effect:** Make a profile-bearing close attack with bite, claws, or another narrowed-access finishing surface against a target that already has a plausible soft line or vital opening.

If the attack connects and proceeds to `Impact`, the designated critical die for that `Impact Roll` counts one result below its normal maximum as enough to validate an `Impacto Crítico` for this attack only.

| Impact die | Normal critical | `Encontrar la Parte Blanda` critical |
| --- | --- | --- |
| `d4` | `4` | `3-4` |
| `d6` | `6` | `5-6` |
| `d8` | `8` | `7-8` |
| `d10` | `10` | `9-10` |
| `d12` | `12` | `11-12` |

This expanded threshold applies only to validating the `Impacto Crítico` of this one attack. It does not increase base `Impact`, does not reduce `Block`, and does not broaden other critical options unless the attack actually resolves through a real pre-existing vulnerable line.

**Restrictions:**

- requires a real existing soft line, wound, or vital opening on the target
- non-natural users need a credible close finishing surface or tool
- applies to one creature only
- does not increase base `Impact` or reduce `Block` by itself
- does not create its own opening or count a normal healthy body as already compromised
- does not stack with itself on the same attack
- does not create long-form bleed or condition tracks by itself
- the expanded critical threshold only applies to this one attack's designated critical die

### Hacer Ceder el Resguardo

| Field | Value |
| --- | --- |
| `name` | Hacer Ceder el Resguardo |
| `name_en` | Make the Shelter Give |
| `origin` | Axe / Cleaver |
| `world_origin` | Species: Zarnag; seed: Quarantine Is Force With A Moral Cost; transmission: breaker-cleaver drills, corpse-gate labor, shield-splitting work, and bad-barrier breach practice; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | A local hard structure, carried protective piece, or nearby resisting segment is currently protecting, stabilizing, or screening the target, and the user has a Sunder-bearing surface capable of forcing that thing to stop doing its job. |
| `requirements` | Minimum rank: Novice; weapon profile: Sunder; any weapon competency, natural attack form, or specific item that grants Sunder access can use this Technique unless this Technique narrows that access; the declared target must be a real breakable piece, object, or cover segment the attack can plausibly reach |
| `target` | one declared protective or resisting structure |
| `range` | weapon reach / adjacent |
| `area` | single declared structure or piece |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 2 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` still resolves against the attack if the declared structure is being protected or carried by a creature |
| `tags` | attack, sunder, break, anti-protection |

**Fantasy:** The point is not to wound the creature first. The point is to make the thing it is trusting stop being trustworthy.

**World origin:** Zarnag labor around bad dead, trench barriers, corpse-gates, and makeshift shields teaches a brutal practical lesson: some things are more dangerous half-functional than whole. `Hacer Ceder el Resguardo` turns that lesson into combat form. The user does not wait for a critical miracle. It commits to the piece itself and forces the question of whether that protection can still hold.

**Why this is not raw damage:** A normal hard hit may damage the creature or rattle the line, but it does not necessarily turn a protection piece, shield, cover lip, or carrying structure into a valid break problem right now. `Hacer Ceder el Resguardo` is about making structure the target instead of treating structure as incidental.

**Primary interaction surface:** `Sunder` through direct structural punishment of a declared protective or resisting piece.

**Secondary interaction surface:** anti-protection pressure, because the Technique matters when something between the user and the consequence is still doing too much work.

**Cost note:** `Rhythm 5 / Attrition 2` is deliberate. This Technique bypasses the normal need for `Impacto Crítico` to make a valid break attempt, but only against one declared reachable structure and without pretending every hit becomes a break.

**Effect:** Before rolling, declare one real breakable target the attack can plausibly reach: a shield, armor piece, carried tool, door bar, corpse-gate slat, cover edge, brace, cart lip, or another local hard structure that is actively protecting, screening, or stabilizing the target's line.

Make a Sunder-bearing attack against that declared target. If the attack fails to connect, nothing further happens.

If the attack connects, this Technique creates a valid break attempt against the declared target **without requiring `Impacto Crítico`**. Resolve the break using the normal `Durabilidad` and `Potencia` rules for Breaking Parts or object rupture.

If the declared target breaks, cracks open, or stops functioning, it immediately loses the protective, screening, or stabilizing benefit it was providing in the fiction. If it does not break, apply the normal failed break result for a valid break attempt.

This Technique does not increase `Potencia`, does not broaden critical thresholds, and does not count the whole creature as a legal break target by itself.

**Restrictions:**

- the declared target must be a real breakable piece, object, or local hard structure rather than the creature as a whole
- does not apply to purely soft tissue unless that tissue is already established as a breakable structure
- non-natural users need a credible Sunder-bearing surface such as an axe, cleaver, breaker head, or similar tool
- does not increase `Potencia` by itself
- does not expand critical ranges or grant critical effects by itself
- does not create a grapple, trap, or persistent lane denial
- if no breakable structure is actually present on the line, this Technique does not apply
- applies to one declared target only

### Darle a la Pieza Útil

| Field | Value |
| --- | --- |
| `name` | Darle a la Pieza Útil |
| `name_en` | Hit the Useful Piece |
| `origin` | Thrown Tool |
| `world_origin` | Species: Zarnag; seed: The Necessary Hand Must Stay Steady; transmission: warning-throw drills, carcass-line enforcement, and exact object-spoil practice; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The target is actively relying on one visible carried or worn piece to work cleanly right now, and the user has one exact thrown line to spoil how that piece settles or moves. |
| `requirements` | Minimum rank: Novice; weapon profile: Precision; any weapon competency, natural attack form, or specific item that grants Precision access can use this Technique unless this Technique narrows that access; requires a direct-line projectile or thrown surface capable of exact placement against a visible small target |
| `target` | one creature and one declared carried or worn piece |
| `range` | short range |
| `area` | single |
| `duration` | until the marked piece is corrected or the end of the target's next activation |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the placement effect |
| `tags` | attack, precision, object_spoil, ranged |

**Fantasy:** The shot is not for the body first. It is for the buckle, strap, grip, rim, sling, hinge, or hanging piece the body is about to trust.

**World origin:** Zarnag line workers and warning throwers learn that sometimes the cleanest way to stop a bad process is not to maim the carrier, but to spoil the exact piece they are about to depend on. `Darle a la Pieza Útil` comes from that discipline: hit the useful part precisely enough that the next use is no longer clean.

**Why this is not raw ranged damage:** A normal projectile hit may wound or rattle the target, but it does not necessarily make one exact carried or worn piece stop functioning cleanly. `Darle a la Pieza Útil` is about exact placement on the thing being used, not just on the person carrying it.

**Primary interaction surface:** `Precision` through exact projectile placement on one declared useful piece.

**Secondary interaction surface:** disruption, because the Technique makes the next use of that exact piece worse unless the target first corrects it.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The spoil is bounded to one piece, but it still combines an attack with a persistent functional penalty that any later actor can exploit. That shared disruption surface is stronger than a quick anchor attack.

**Effect:** Before rolling, declare one visible carried or worn piece the target is plausibly relying on: a weapon grip, shield rim, sling, strap, lantern hook, satchel tie, mask fastening, brace cord, hanging tool, or similar small functional point.

Make a Precision-bearing ranged or thrown attack against the target. If the attack fails to connect, nothing further happens.

If the attack connects, the declared piece becomes `badly-seated`. The first `A.R.`, `D.R.`, or `S.R.` the target makes that directly depends on that exact piece takes a situational penalty equal to the rank bonus of the competency used for this Technique.

| Competency rank used | Penalty to the first dependent roll |
| --- | --- |
| Novice | `-1` |
| Adept | `-2` |
| Expert | `-3` |
| Master | `-4` |
| Consummate | `-5` |
| Transcendent | `-6` |

The target may remove `badly-seated` before that roll by spending `Interactuar` to reseat, free, tighten, or regrip the declared piece if the fiction allows it. If the target never uses that exact piece before the end of its next activation, the effect ends.

This Technique does not break the piece, does not disarm by itself, and does not create a trap or environmental mark.

**Restrictions:**

- requires one visible small carried or worn piece rather than a whole body zone
- requires a direct-line thrown or projectile surface capable of exact placement
- the penalty applies only to the first `A.R.`, `D.R.`, or `S.R.` that directly depends on the declared piece
- the target may clear the effect with `Interactuar` if the declared piece can realistically be corrected
- does not function on creatures with no readable or relevant carried/worn piece on the line
- does not break, disarm, or trap by itself
- applies to one creature and one declared piece only

### Sostener la Mano Necesaria

| Field | Value |
| --- | --- |
| `name` | Sostener la Mano Necesaria |
| `name_en` | Hold the Necessary Hand |
| `origin` | Contención |
| `world_origin` | Species: Zarnag; seed: The Necessary Hand Must Stay Steady; transmission: plague-camp discipline, corpse-team instruction, and horror-labor steadiness drills; availability: Common |
| `category` | utility |
| `type` | reactive |
| `trigger` | You or one adjacent ally is targeted by one immediate attempt of horror, disgust, taboo dread, or contamination pressure that would impose a concrete penalty, interruption, or collapse risk on one necessary task being declared right now. |
| `requirements` | Minimum rank: Novice; Contención at Novice or higher; the declared task must be immediate and necessary, and the pressure must come from a real horrifying or contaminating source rather than a generic inconvenience |
| `target` | self or one adjacent ally |
| `range` | self / adjacent |
| `area` | single creature |
| `duration` | one declared task or short held duty |
| `cost` | Rhythm 3; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration unless the scene is under active pressure |
| `saving_roll` | opposed `Contención S.R.` against the triggering pressure roll or against a threshold set by the scene when no hostile roll exists |
| `tags` | utility, containment, survival_window, support |

**Fantasy:** The hand starts to go. The Zarnag answers before it does. Sometimes it is breath. Sometimes it is a snapped command. Sometimes it is the crooked laugh that says the foul thing has not won yet. The task holds because the breaking moment is denied in time.

**World origin:** Zarnag children learn early that someone must keep touching what others recoil from. In plague camps, grave lines, butcher pits, and corpse-wagons, survival depends on the person who can keep one needed action alive while everyone else is fighting the urge to flinch, gag, pray badly, or run. `Sostener la Mano Necesaria` is that discipline under immediate pressure.

**Why this is not raw Contención:** A base `Contención` roll decides whether the character mentally breaks. `Sostener la Mano Necesaria` is narrower and more tactical: it answers one specific attempt to break function at the exact moment that attempt would spoil a necessary task.

**Primary interaction surface:** `Contención` through preserving one necessary task against immediate internal breakdown.

**Secondary interaction surface:** support, because the user can steady an adjacent ally through one short task instead of only preserving self-function.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. This is not broad morale support. It is one immediate reactive denial of one collapse attempt against one necessary task for self or adjacent ally.

**Effect:** Choose yourself or one adjacent ally who is declaring one necessary immediate task under pressure. The task must be specific and practical: `Interactuar`, `Usar Especialización`, lifting or dragging a body, tying a seal, sealing a container, cutting something free, holding a gate, or another short duty the fiction clearly makes necessary.

When horror, disgust, taboo dread, contamination pressure, or a comparable inward-collapse source attempts to impose a concrete penalty, interruption, or spoil on that task, make a reactive `Contención` Specialization Roll.

If the source already uses an opposed roll, your `Contención S.R.` must equal or exceed that triggering roll. If the source does not use an opposed roll, roll against a threshold set by the scene's psychological and sensory pressure.

On success, that one triggering collapse attempt does not apply to the declared task: the penalty, interruption, or inward break it would have caused is denied for this one resolution, and the task continues normally if it is still physically possible.

On failure, the triggering pressure resolves normally.

This Technique does not remove the source, cure panic broadly, or protect against bodily pain, command effects, deception, or long-form social pressure. It only says: not this break, not on this task, not yet.

**Restrictions:**

- only applies when the source of failure is horror, disgust, taboo dread, contamination pressure, or similar inward collapse pressure
- does not apply to bodily pain, wound penalties, Fatigue, poison, or other physiological burden; those belong to `Tolerancia`
- does not apply to leadership pressure, negotiation, deception, or ordinary fear from a merely dangerous opponent with no horror or contamination logic
- only answers one triggering collapse attempt against one declared task or held duty per use
- cannot make an impossible task physically possible
- cannot remove a lasting condition, clear an Ailment, or grant broad morale immunity
- if no real collapse pressure is present, this Technique does not apply

### Tomar la Parte Útil

| Field | Value |
| --- | --- |
| `name` | Tomar la Parte Útil |
| `name_en` | Take the Useful Part |
| `origin` | Destreza |
| `world_origin` | Species: Zarnag; seed: Distinguish the Survivable from the Corrupting; transmission: corpse-side sorting drills, foul-kit handling, and exact-hand work under contamination pressure; availability: Common |
| `category` | utility |
| `type` | reactive |
| `trigger` | You fail one immediate `C.R.` or `S.R.` involving fine handwork on a small useful point — knot, seal edge, wrapped opening, sample point, tag, clasp, fastener, grip, tool edge, wound lip, or another similarly exact handling line — and the failure has not yet fully spilled into an irreversible outcome. |
| `requirements` | Minimum rank: Novice; Destreza at Novice or higher; line of sight or hand access to the declared point; one free hand plus cloth, pick, hook, forceps, knife point, or another plausible fine-handling means. |
| `target` | one declared exact point / small useful item / handling line |
| `range` | touch / adjacent |
| `area` | one exact local point |
| `duration` | immediate |
| `cost` | Rhythm 0; Attrition 3 |
| `saving_roll` | immediate `Destreza S.R.` replacing the failed handling result |
| `tags` | utility, reaction, exact_handling, contamination, second_attempt |

**Fantasy:** The first hand goes wrong. The second hand arrives before the mistake finishes becoming disaster. The Zarnag does not start over cleanly; they seize the one useful point in the middle of the slip and force the exact correction through anyway.

**World origin:** Zarnag labor around bodies, spoilage, trench kits, quarantine gear, and damaged containers teaches one ruthless lesson: the first miss is often survivable, the second is not. Children sorting refuse, plague-camp workers opening wraps, and corpse-line judges checking remains all learn how to correct a slipping hand in the same breath before snag, spill, burst, or contamination fully opens.

**What `Destreza` contributes:** This Technique is built from extracted `Destreza` capacities, not from generic “carefulness”:

- constrained-access handling
- micro-placement control
- exact-touch isolation
- error-minimizing handwork

**Why this is not a base Destreza check:** A base `Destreza` check resolves whether the fine handling succeeds or fails. `Tomar la Parte Útil` is the ugly corrective answer after that failure, when the hand still has one last exact chance to grab the right thing before the mistake becomes final.

**Primary interaction surface:** reactive re-attempt on failed exact handwork.

**Secondary interaction surface:** contamination and clutter control, because the corrective handwork happens before spill, snag, or broad handling fully blooms into a worse result.

**Cost note:** `Rhythm 0 / Attrition 3` is deliberate. The value here is immediacy: you do not lose tempo, you just pay for the brutal hand correction with real bodily strain. This should feel expensive enough that it is used to save a moment that matters, not to casually fish for better outcomes.

**Effect:** After you fail one immediate `C.R.` or one relevant `S.R.` involving fine handwork on one exact local point, you may immediately invoke `Tomar la Parte Útil` before the failure fully resolves into its worst consequence.

Make an immediate `Destreza` Specialization Roll against the same threshold or opposed result that the failed action just used.

If the `Destreza S.R.` succeeds, replace the failed result with this new success. The action is treated as if the exact useful point was recovered in time by hand correction rather than broad retry.

If the `Destreza S.R.` fails, the original failure stands and the Technique buys nothing except the right to have tried.

`Tomar la Parte Útil` does not roll the whole scene back. It only allows one exact second attempt before the missed touch becomes final.

**Restrictions:**

- only works on one exact local point, not a whole corpse, container, trap, kit, or wound
- requires plausible fine access and handling means
- only applies if the failed action was about fine handwork and the failure has not yet fully become irreversible
- the replacement roll must still be physically plausible in the current fiction
- does not grant a third attempt if the `Destreza` correction also fails
- does not itself solve tasks that were impossible even on success
- does not remove a settled Ailment or purify contamination by itself
- cannot be used after the source has already burst, spilled, snapped, infected, fallen, or otherwise moved past the recoverable moment

### Tirar la Advertencia

| Field | Value |
| --- | --- |
| `name` | Tirar la Advertencia |
| `name_en` | Throw the Warning |
| `origin` | Lanzamiento |
| `world_origin` | Species: Zarnag; seed: The Waste Draws Predators / Distinguish the Survivable from the Corrupting; transmission: warning-throw drills, bad-ground signaling, and quarantine-line distance work; availability: Common |
| `category` | utility |
| `type` | active |
| `trigger` | You or one ally within `12 meters` is about to commit to one short local line — a step, crossing, descent, climb start, approach lane, or contamination edge — and a small thrown object can still land exactly where that line becomes dangerous or useful. |
| `requirements` | Minimum rank: Novice; Lanzamiento at Novice or higher; one small throwable object, shard, tag, stone, bone chip, wrapped marker, or similarly light warning piece; clear enough line to place the throw meaningfully. |
| `target` | self or one ally, and one exact local line / point of commitment |
| `range` | `12 meters` |
| `area` | one exact local point |
| `duration` | one immediate movement, crossing, or local handling decision |
| `cost` | Rhythm 2; Attrition 1 |
| `saving_roll` | `Lanzamiento S.R.` against a threshold set by distance, visibility, clutter, speed, and scene pressure |
| `tags` | utility, thrown_warning, distance_control, route_read, support |

**Fantasy:** The throw lands before the foot does. Not to wound. To say: there. One shard in the right place can buy one clean step where the line was about to go bad.

**World origin:** Zarnag scouts, corpse-wagon runners, and quarantine hands do not always shout. In bad wind, panic, smell, dark, or crowd noise, a thrown marker is often faster than a command. Stones, bone chips, wraps, hooks, and refuse tags become a live signaling language for bad ground, wrong approach, and don't-step-there warning.

**What `Lanzamiento` contributes:** This Technique is built from extracted `Lanzamiento` capacities, not from generic “being able to throw”:

- release discipline
- exact landing control
- route-point placement
- timing a warning before commitment finishes

**Why this is not a base Lanzamiento check:** A base `Lanzamiento` check can tell us whether the user hits or lands a thrown object well. `Tirar la Advertencia` turns that throw into one immediate line decision that changes how a creature may commit to one exact point right now.

**Primary interaction surface:** thrown exact placement on one live route or commitment point.

**Secondary interaction surface:** route guidance, because the value lies in making one short local decision cleaner rather than causing damage.

**Cost note:** `Rhythm 2 / Attrition 1` is deliberate. This is lighter than most full utility Techniques because it only improves one immediate local commitment for self or an ally. It does not damage, persist, or broadly reshape the terrain.

**Effect:** Declare one exact local point within `12 meters` where you or one ally are about to commit: a step edge, descent lip, climb start, crossing seam, contamination boundary, corpse-slick patch, or another similarly small route point.

Make a `Lanzamiento` Specialization Roll against a threshold set by distance, visibility, clutter, speed, and scene pressure.

On success, the target creature's next immediate `Movement`, `C.R.`, or relevant `S.R.` through that exact point treats its threshold as **one difficulty band lower**, to a minimum of `Fundamental`.

That means:

- `Extreme` becomes `Demanding`
- `Demanding` becomes `Rigorous`
- `Rigorous` becomes `Challenging`
- `Challenging` becomes `Fundamental`
- `Fundamental` does not reduce further

The warning ends as soon as that one immediate decision resolves. It does not remain as a standing mark, trap, or general terrain modifier.

On failure, the throw lands late, wrong, unseen, or unconvincingly, and creates no mechanical change.

**Restrictions:**

- only works on one exact local point, not a whole zone or broad area
- requires a real throwable marker and a plausible thrown line
- only affects one immediate movement, crossing, or local handling decision by the warned creature
- does not deal damage, create a trap, or create a lasting terrain mark
- does not override forced movement or teleportation

### Leer lo que Siguió

| Field | Value |
| --- | --- |
| `name` | Leer lo que Siguió |
| `name_en` | Read What Followed |
| `origin` | Rastreo |
| `world_origin` | Species: Zarnag; seed: The Scavenger Follows the Weak Line / Distinguish the Survivable from the Corrupting; transmission: wound-trace reading drills, continuity-of-force judgment, and fresh-damage exploitation practice; availability: Common |
| `category` | utility |
| `type` | active |
| `trigger` | A creature within sight bears a fresh visible wound, torn seam, leaking wrap, failed plate edge, dragged limb, blood line, or another readable recent damage pattern on one specific operative zone, and the user wants to read how that zone is still failing. |
| `requirements` | Minimum rank: Novice; Rastreo at Novice or higher; the target must show a fresh readable damage line or very recent physical failure pattern on one specific zone; that zone must still be operative or still matter to the creature's function; the line must be visible enough to study under current scene conditions. |
| `target` | one specific wounded or freshly damaged zone on one creature |
| `range` | within sight |
| `area` | one zone |
| `duration` | persistent on that zone until it is no longer readable, no longer operative, or materially altered beyond the original read |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | Rastreo Specialization Roll against a threshold set by wound freshness, visibility, armor obstruction, target movement, and scene pressure |
| `tags` | utility, tracking, wound_read, continuity_read, attack_setup, field_judgment |

**Fantasy:** The Zarnag does not just see blood. They see where force kept traveling after the first break: which side took weight badly, which seam is still opening, which limb is lying to the rest of the body, which wrap is holding too late. The wound does not merely mark the creature. It marks the failing zone.

**World origin:** Zarnag corpse-watchers and scavenger hands learn that a fresh wound is not an isolated point. It leaves a continuity line through posture, weight, drag, blood direction, flinch timing, and failing restraint. Veteran readers are taught to identify not just where something was hurt, but where that hurt is still making the rest of the body late, weak, or badly supported.

**What `Rastreo` contributes:** This Technique is built from extracted `Rastreo` capacities, not from generic observation:

- continuity reconstruction
- freshness discrimination
- force-line continuation
- aftermath pattern reading
- failure-point correlation

**Why this is not a base Rastreo check:** A base `Rastreo` check can tell us whether a user notices damage, follows spoor, or identifies traces. `Leer lo que Siguió` turns a fresh readable damage pattern into a persistent zone-read: not "what happened here in general," but "how this specific part is still failing, and how to keep exploiting it."

**Primary interaction surface:** fresh wound-line reading on one living target's specific operative zone.

**Secondary interaction surface:** repeated attack shaping against that same zone, because the value lies in converting a readable continuity failure into a durable exploit until the zone stops mattering.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. This is not a fleeting hunch. It is a committed technical read on one wounded zone. The cost buys durable targeting knowledge, but only on that one line and only while that line still exists as a readable problem.

**Effect:** Choose one specific zone on one creature within sight that currently bears a fresh visible wound, torn seam, fresh blood line, dragged limb, failed wrap, or another readable recent damage pattern. Make a `Rastreo` Specialization Roll against a threshold set by wound freshness, visibility, armor obstruction, target movement, and scene pressure.

On success, you identify where that fresh failure is still propagating through that zone's structure, supports, and connected lines. While that zone remains readable and still matters to the target's operation, your attacks that specifically target that same zone gain a bonus to their `A.R.` equal to `+1` per technique rank, as long as the attack plausibly exploits the same line or a directly connected one.

Examples of valid follow-through include:

- driving back into the same torn line on that zone
- cutting the structure now compensating for that zone's first wound
- striking the fastening, plate edge, joint, membrane, or support now carrying the bad load for that zone
- attacking the connected side that zone is overusing to keep from collapsing further

The read ends on that zone if the zone is fully destroyed, loses the relevant function, is thoroughly treated or rebuilt, is fully concealed from further reading, or changes so much that the original continuity line no longer describes its failure.

On failure, the line is too obscured, too old, too well-compensated, too covered, or too visually noisy to turn into a reliable exploit.

**Restrictions:**

- requires a real fresh readable damage pattern on one specific zone
- only benefits attacks that intentionally target that same zone
- does not bypass reach, line of effect, or other normal attack requirements
- does not stack with another active instance of `Leer lo que Siguió` on the same zone from the same user; reading a new zone replaces the old read
- does not function if the target is fully concealed, the zone is fully covered, or the observed failure is too old to read as current continuity

### Oír la Costura Mala

| Field | Value |
| --- | --- |
| `name` | Oír la Costura Mala |
| `name_en` | Hear the Bad Seam |
| `origin` | Resonancia |
| `world_origin` | Species: Zarnag; seed: Distinguish the Survivable from the Corrupting / Keep Working Where Death Has Not Settled; transmission: corpse-pressure listening drills, quarantine seam reading, and bad-presence handling practice; availability: Common |
| `category` | utility |
| `type` | active |
| `trigger` | A corpse, wound, object, bundle, doorway, pit, cache, or other exact source nearby may be carrying active unhealthy aura, taumatic residue, essential disturbance, or another bad sympathetic pressure, and the next decision depends on touching, moving, opening, treating, or resisting that source correctly. |
| `requirements` | Minimum rank: Novice; Resonancia at Novice or higher; a real active disturbed signal must be present on one exact source; that source must not be completely sealed away from resonant reach. |
| `target` | one exact disturbed source |
| `range` | within sight or plausible resonant reach |
| `area` | one source |
| `duration` | persistent on that source until it is sealed, quieted, emptied, or materially altered beyond the original read |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | Resonancia Specialization Roll against a threshold set by signal strength, contamination overlap, sealing, interference, and scene pressure |
| `tags` | utility, resonance, contamination_read, handling_line, source_judgment, pressure_control |

**Fantasy:** The Zarnag does not ask whether a thing feels wrong. They ask where the wrongness is still leaking from. A corpse is not just dangerous. A wrapped object is not just tainted. A doorway is not just bad. Each has one seam that is still speaking louder than the rest.

**World origin:** Zarnag who work around graves, quarantines, plague bundles, disturbed remains, and bad thresholds learn to separate a whole ugly source from the one part of it that is still carrying the live pressure. Experienced readers listen for the seam that still calls, leaks, binds, or answers back, because that is the seam that decides whether handling becomes work or disaster.

**What `Resonancia` contributes:** This Technique is built from extracted `Resonancia` capacities, not from vague sensitivity:

- signal isolation
- unhealthy-pressure discrimination
- active-seam localization
- contaminated-face judgment
- bad-presence handling order

**Why this is not a base Resonancia check:** A base `Resonancia` check can tell us whether a source carries aura, taumatic residue, or disturbed presence. `Oír la Costura Mala` turns that into one persistent operational read: which exact seam of the source is still active, and which handling line is less wrong.

**Primary interaction surface:** one exact disturbed source carrying active unhealthy pressure.

**Secondary interaction surface:** handling, treatment, containment, or resistance against that same source, because the value lies in not meeting the active seam head-on when another line is available.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. This is not broad detection. It is a focused read on one exact source that can keep paying off while that source remains materially the same.

**Effect:** Choose one exact disturbed source within sight or plausible resonant reach: a corpse, wound, wrapped object, pit edge, threshold, tool, bundle, container, altar face, or another similarly exact source carrying active unhealthy pressure. Make a `Resonancia` Specialization Roll against a threshold set by signal strength, contamination overlap, sealing, interference, and scene pressure.

On success, you isolate one **bad seam** and one **less-wrong handling line** on that source. While the source remains materially the same, the user or one ally directly briefed by the user gains a bonus equal to `+1` per technique rank on the next qualifying `C.R.`, `S.R.`, or `R.R.` that deals directly with that same source through the declared handling line.

Qualifying uses include:

- opening, moving, or securing the source without touching its active seam
- treating or containing the specific pressure the read identified
- resisting an emanation, contact pressure, or backlash that comes from that exact source

The read persists on that source until it is sealed, quieted, emptied, treated past the relevant disturbance, or altered so much that the original seam no longer describes the danger correctly.

On failure, the source is too overlapped, too noisy, too sealed, too deceptive, or too unstable to separate one active seam from the rest in a reliable way.

**Restrictions:**

- requires one exact source carrying real active unhealthy pressure
- only benefits one next qualifying `C.R.`, `S.R.`, or `R.R.` against that same source through the declared handling line
- does not bless a whole room, battlefield, or category of objects
- does not identify full history, exact identities, or every property of the source by itself
- does not function if the source is fully insulated from resonant reach or if no meaningful less-wrong handling line exists

### Reír Donde Más Suena

| Field | Value |
| --- | --- |
| `name` | Reír Donde Más Suena |
| `name_en` | Laugh Where It Rings Loudest |
| `origin` | Intimidación |
| `world_origin` | Species: Zarnag; seed: The Laugh Breaks Nerve First / Keep Working Where Death Has Not Settled; transmission: carrion-line authority drills, bad-scene pressure calls, and laugh-timing practice; availability: Common |
| `category` | utility |
| `type` | active |
| `trigger` | One creature nearby is already under disgust, uncertainty, taboo pressure, corpse-pressure, contamination fear, or another strain of visible nerve, and the user wants to push exactly where that strain is already ringing. |
| `requirements` | Minimum rank: Novice; Intimidación at Novice or higher; the target must be able to perceive the user clearly enough to register the pressure; there must already be a plausible fear, disgust, taboo, or collapse line to exploit. |
| `target` | one creature already under visible nerve strain |
| `range` | voice / clear sensory presence |
| `area` | one creature |
| `duration` | until the end of the target's next activation, or until the pressure is answered by one qualifying roll |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | Intimidación Specialization Roll opposed by the target's relevant nerve-holding line, or against a threshold set by discipline, context, and current psychological pressure |
| `tags` | utility, intimidation, nerve_pressure, taboo, laugh_pressure, response_spoil |

**Fantasy:** The Zarnag does not need to invent a nightmare whole. They make the body's next worst conclusion feel immediate. The laugh lands on the seam where disgust, taboo, contamination, predator pressure, or bad death already points, and the target's body starts treating that line as urgent danger.

**World origin:** Zarnag who work among bad deaths, rotting lines, and frightened labor do not waste breath trying to terrify the fearless. They learn to hear which worker, hunter, guard, mourner, or scavenger is one interpretation away from bodily panic, then press that exact seam until the body itself starts refusing the line.

**What `Intimidación` contributes:** This Technique is built from extracted `Intimidación` capacities, not from generic shouting:

- visible-nerve reading
- pressure timing
- taboo exploitation
- authority through composure inside ugliness
- terror-line activation through precisely placed social pressure

**Why this is not a base Intimidación check:** A base `Intimidación` check can threaten, pressure, or impose presence. `Reír Donde Más Suena` does not stop at pressure. If the laugh lands, it can apply the named Alteration `Aterrorizado`.

**Primary interaction surface:** one target facing a plausible immediate terror line.

**Secondary interaction surface:** Alteration application through `Aterrorizado`.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. The Technique still requires a believable terror line and an Alteration `R.R.` to settle. It does not create guaranteed fear from nothing, but it does carry a real named state when the pressure lands cleanly.

**Effect:** Choose one creature within voice or clear sensory presence that is facing a plausible immediate terror line: contamination, corpse-pressure, taboo breach, predator display, grotesque revelation, hostile presence, or another fictionally credible urgent fear source. Make an `Intimidación` Specialization Roll opposed by that target's relevant nerve-holding line, or against a threshold set by discipline, context, and current psychological pressure.

If the Technique fails, the laugh lands wrong, too early, or against a target whose body does not actually accept the terror line.

If the Technique succeeds, the target immediately makes an Alteration `R.R.` against `Aterrorizado`.

Use the default Ailment severity bands by rank:

- ranks `1-2` -> `Minor`
- ranks `3-4` -> `Moderate`
- ranks `5-6` -> `Severe`

On a failed `R.R.`, the target gains `Aterrorizado` at that severity. The feared line is the one the user just made immediate.

On a successful `R.R.`, `Aterrorizado` does not settle.

**Restrictions:**

- requires a plausible immediate terror line in the fiction
- applies the generic Alteration `Aterrorizado`, not a Zarnag-only condition
- the feared line must be declared clearly enough that `Aterrorizado` knows what source or line it is about
- does not function on targets that cannot perceive the user or cannot meaningfully register the exploited pressure
- if no credible urgent fear line exists, the Technique does not apply

### Pasar Como Parte del Fondo

| Field | Value |
| --- | --- |
| `name` | Pasar Como Parte del Fondo |
| `name_en` | Pass as Part of the Background |
| `origin` | Sigilo |
| `world_origin` | Species: Zarnag; seed: Work The Bad Ground Without Becoming The New Problem; transmission: corpse-line crossing drills, ruin-scavenge patience, and foul-settlement profile suppression practice; availability: Common |
| `category` | utility |
| `type` | active |
| `trigger` | The user wants to cross up to `4 meters` of watched space without being cleanly registered as the new threat on that line. |
| `requirements` | Minimum rank: Novice; `Sigilo` at Novice or higher; the declared path must already be under watch, notice, or perception by one or more creatures, but the user must not already be cleanly identified as the hostile subject of that line; the crossed space must not be totally empty, featureless, and clean, and must contain enough background disturbance, clutter, traffic, smoke, foul labor, ruin noise, hanging material, debris, or other believable ambient explanation for the user's passage. |
| `target` | one watch line, observer, or small observing cluster |
| `range` | one declared crossed space up to `4 meters` long |
| `area` | one declared crossing line |
| `duration` | until the crossing resolves, the observing line localizes the user cleanly, or the user breaks the borrowed pattern |
| `cost` | Rhythm 3; Attrition 1 |
| `saving_roll` | `Sigilo` Specialization Roll opposed by the relevant alertness / registration line, or against a threshold set by distance, clutter, smell, light, ambient panic, and how credibly the user can be mistaken for part of what was already there |
| `tags` | utility, stealth, hidden_state, bad_ground, profile_suppression |

**Fantasy:** The Zarnag does not disappear. They become one more expected ugliness: another moving tarp, another corpse-hand, another bad smell, another bent figure in the ruin, another shape that does not yet deserve alarm.

**World origin:** Zarnag who live around pits, bad camps, plague wagons, frightened labor, ruined streets, and death-sites learn that being unseen is only one way to survive. Often the better answer is to be seen wrongly: as labor, refuse, routine movement, or part of the same foul background nobody wants to study too closely.

**What `Sigilo` contributes:** This Technique is built from extracted `Sigilo` capacities, not from generic crouching:

- profile suppression inside ambient clutter
- timing a registration window
- moving like expected labor or expected ruin movement
- reducing the urgency of notice
- passing one watched line without becoming the new focus

**Why this is not a base Sigilo check:** A base `Sigilo` check helps the user stay quiet, reduce profile, or avoid notice. `Pasar Como Parte del Fondo` does something narrower and more technical: it lets the user obtain the same formal state, `Oculto`, **while already crossing watched space**, because the watchers are reading that short passage as routine filth, labor, or background disturbance instead of as a new threat.

**Primary interaction surface:** one watched crossing of up to `4 meters` through a non-empty, dirty, cluttered, or otherwise explainable background.

**Secondary interaction surface:** altered access to `Oculto`, because the observing line is given just enough wrong context that the user's next passage can still register as hidden rather than as clean hostile presence.

**Cost note:** `Rhythm 3 / Attrition 1` is deliberate. This Technique does not create invisibility, broad stealth immunity, or perfect disguise. It only buys one bounded way to gain `Oculto` against one relevant observing line, and it collapses if the user gives the watchers a clearer story.

**Effect:** Choose one declared crossed space of up to `4 meters` that is already being watched, noticed, or loosely perceived: a corpse cart edge, ruin threshold, trench lip, smoke line, pit perimeter, tarp gap, foul alley, camp handoff, or another similarly local bad-ground passage.

Make a `Sigilo` Specialization Roll opposed by the relevant alertness / registration line, or against a threshold set by distance, clutter, smell, light, ambient panic, and how credibly the user can be mistaken for part of what was already there.

If the Technique fails, the user becomes the new point of notice too cleanly, and the observing line may answer normally.

If the Technique succeeds, the user gains `Oculto` **against that observer, watch line, or small observing cluster only**, using this Technique's successful `Sigilo` result as the active value of the `Oculto` state for that line, even though the user is already crossing watched space and would not normally be able to gain `Oculto` there through the base `Ocultarse` action alone.

That limited `Oculto` lasts until one of these happens:

- the user completes one next `Movement` through that same declared crossed space;
- the observing line localizes the user cleanly through Percepción, another applicable sense, or a Technique that beats that active `Oculto` value;
- or the user does something abrupt, clean, loud, or obviously out of pattern that breaks the bad-background read.

While that limited `Oculto` holds, the observing line must treat the user under the normal rules of `Oculto`: it cannot choose the user as the target of direct single-creature attacks without first localizing them cleanly, though it may still attack a suspected area, search actively, or react to obvious signals if the fiction supports it.

This Technique does not make the user invisible, does not fool every observer in the scene, does not create scene-wide concealment, and does not survive once the user stops matching the background pattern they exploited.

**Restrictions:**

- requires believable ambient ugliness, clutter, labor, disorder, ruin noise, foul traffic, or another bad-background pattern to blend into
- applies to one declared crossed space of up to `4 meters` only
- applies to one observer, watch line, or small observing cluster only
- requires that the space not be totally empty, clean, and featureless
- requires incomplete observation, not clean hostile identification
- grants no benefit once the user clearly breaks the borrowed pattern
- does not create full disguise, invisibility, or scene-wide stealth immunity
- grants only one limited `Oculto` state tied to one declared crossed space
- does not help if the observer already has clean, focused, and unambiguous attention on the user before the Technique begins

### Ceder Antes del Disparo

| Field | Value |
| --- | --- |
| `name` | Ceder Antes del Disparo |
| `name_en` | Give Before the Trigger Bites |
| `origin` | Trampas |
| `world_origin` | Species: Zarnag; seed: Distinguish the Survivable from the Corrupting / Quarantine Is Force; transmission: trigger-response reading drills, spring-yield practice, and bad-threshold survival teaching; availability: Common |
| `category` | utility |
| `type` | reactive |
| `trigger` | A trap, warning system, or other condition-triggered mechanism has already activated against the user or an adjacent ally. |
| `requirements` | Minimum rank: Novice; `Trampas` at Novice or higher; the user must be the target of the activation or adjacent to the target and able to shout, pull, brace, spoil, release, flatten, or redirect in time; the danger must be something whose response can still be minimized by understanding how traps answer: spring, hook, snap line, drop, latch, shard burst, noise line, pressure release, or similar trigger logic. |
| `target` | self or one adjacent creature caught in a trap activation |
| `range` | self or adjacent |
| `area` | one triggering trap response |
| `duration` | one triggering resolution |
| `cost` | Rhythm 0; Attrition 2 |
| `saving_roll` | `Trampas` Specialization Roll made immediately after the trap activates and before its full consequences finish resolving |
| `tags` | utility, traps, reaction, trap_response, quarantine |

**Fantasy:** The Zarnag does not beat the trap by strength. They know when to go limp, when to turn with the pull, when to let cloth tear, when to flatten instead of recoil, when to lose a tool instead of a hand. The answer is not “avoid all effect.” It is “give the mechanism less of you than it wanted.”

**World origin:** Zarnag who work plague lines, grave routes, bad camps, and improvised warning grounds learn early that knowing how traps are made also teaches how they bite. Springs want resistance, hooks want panic, latches want weight in the wrong direction, and noise lines want a full committed body. Veterans teach survival by response logic, not by perfect avoidance.

**What `Trampas` contributes:** This Technique is built from extracted `Trampas` capacities, not from generic clutter use:

- trigger-path reading
- response-chain anticipation
- collapse-point recognition
- knowing what part of the mechanism actually matters
- minimizing what the answer gets to take

**Why this is not a base `Trampas` check:** A base `Trampas` check builds, identifies, prepares, or disarms a condition-triggered system. `Ceder Antes del Disparo` happens **after activation has already begun**. It is not trap setup or disarm. It is expert survival inside the first instant of a triggered response.

**Primary interaction surface:** one triggered trap response that has not fully finished resolving.

**Secondary interaction surface:** consequence reduction, because the value is not escaping all danger but making the mechanism take less than it would have taken from a body that answered wrong.

**Cost note:** `Rhythm 0 / Attrition 2` is deliberate. This is a true emergency reaction that can interrupt disaster timing without spending Rhythm, but it only applies when a trap has already fired and it costs enough Attrition that it cannot be treated as free insurance.

**Effect:** When a trap, warning system, or other condition-triggered mechanism activates against you or one adjacent ally, immediately make a `Trampas` Specialization Roll before the full response resolves.

If the Technique fails, the trap resolves normally.

If the Technique succeeds, choose one relevant roll in that resolution:

- the triggering `C.R.`
- the triggering `S.R.`
- or the triggering `R.R.`

That chosen roll gains a bonus equal to the `rank bonus` of `Trampas` for that one resolution.

If the trap's outcome does not call for one of those rolls, the Narrator may instead let the Technique reduce one immediate trap consequence to its next less severe believable outcome:

- a hard pull becomes a bad stumble
- a full hook catch becomes a scrape or partial catch
- a loud warning line reports late or weak
- a falling response clips instead of fully pinning
- or another similarly narrower mitigation that fits the mechanism

This Technique does not untrigger the trap, does not disarm the whole system, and does not guarantee safety. It only minimizes one active response because the user understands how traps typically answer a body.

It cannot help after the full consequences have already resolved.

**Restrictions:**

- only works after the trap has already activated
- only affects one triggering resolution
- requires the mechanism to still be in the part of resolution that can be answered physically or mentally in time
- does not disarm or destroy the whole system
- does not create a new trap
- does not apply `Atrapado`, `Desequilibrado`, or `Derribado`
- does not help after the outcome is already fully settled

### Cortar el Paso Dos Veces

| Field | Value |
| --- | --- |
| `name` | Cortar el Paso Dos Veces |
| `name_en` | Cut the Step Twice |
| `origin` | Thrown Tool |
| `world_origin` | Doctrine: Transferable Skirmisher Fieldcraft; seed: Shorten Arrival Before It Lands Clean; transmission: warning-throw cadence, route enforcement, and chase-shortening drills; availability: Common |
| `category` | attack |
| `type` | reactive |
| `trigger` | One creature within thrown range begins a committed movement through a line the user can still answer with repeated direct throws before the movement finishes. |
| `requirements` | Minimum rank: Novice; weapon profile: Volley; any weapon competency, natural attack form, or specific item that grants Volley access can use this Technique unless this Technique narrows that access; requires a repeated-throw set, spare thrown pieces, or another believable means of short release cadence |
| `target` | moving creature |
| `range` | thrown range |
| `area` | single creature |
| `duration` | one triggering movement |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` resolves normally against the reactive attack |
| `tags` | attack, volley, reaction, movement_pressure |

**Fantasy:** The first throw says stop. The second says stop now. The target may still move, but not as far or as cleanly as they meant to.

**World origin:** This Technique now sits provisionally under shared fieldcraft instead of one species. Route enforcers, chase hands, and warning throwers across multiple harsh traditions learn that a rushing body is easier to shorten than to fully stop. `Cortar el Paso Dos Veces` is not elegant archery cadence. It is practical repeated release into the next few steps of a creature that should not arrive cleanly where it meant to go.

**Why this is not raw thrown damage:** A normal thrown hit may wound, but it does not necessarily make the target arrive short. `Cortar el Paso Dos Veces` is about maintaining just enough ranged cadence that the target has to check body, footing, or line before the movement completes.

**Primary interaction surface:** `Volley` through reactive repeated release against one triggering movement.

**Secondary interaction surface:** movement pressure, because the Technique shortens one committed approach, retreat, or crossing instead of creating a lasting slow.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. This is a reactive ranged attack that can also cut distance from one declared movement. It does not create area denial, does not attack multiple targets, and does not reduce speed after the movement ends.

**Effect:** Make a reactive Volley-bearing thrown attack against the moving target before the triggering movement finishes.

If the attack fails to connect, the movement resolves normally.

If the attack connects, the attack resolves normally and the target's remaining distance for that triggering movement is reduced by `1 meter` per rank bonus of the competency used for this Technique.

| Competency rank used | Distance removed from the remaining triggering movement |
| --- | --- |
| Novice | `1 m` |
| Adept | `2 m` |
| Expert | `3 m` |
| Master | `4 m` |
| Consummate | `5 m` |
| Transcendent | `6 m` |

If this reduction prevents the target from reaching its declared position, it stops at the last legal position it can still reach.

This Technique affects only that one movement. It does not create a persistent slow, broad suppression, or a second attack.

**Restrictions:**

- requires line of effect to one moving target
- requires a believable means of repeated direct thrown release, not one single heavy throw with no follow cadence
- affects one target only
- affects the triggering movement only
- does not create a persistent speed penalty after the movement ends
- does not attack multiple targets
- does not create a trap, environmental mark, or broad no-cross zone

### Hacer que el Ángulo Muerda

| Field | Value |
| --- | --- |
| `name` | Hacer que el Ángulo Muerda |
| `name_en` | Make the Angle Bite |
| `origin` | Thrown Tool |
| `world_origin` | Doctrine: Transferable Skirmisher Fieldcraft; seed: Keep the Threat Alive Past the Obvious Line; transmission: stone-skip warning drills, cart-rim rebound practice, and bad-corner pursuit work; availability: Uncommon |
| `category` | attack |
| `type` | active |
| `trigger` | A target is not fully owned on a direct line, but one nearby hard surface could realistically carry a short rebound, skip, or angled continuation into their position. |
| `requirements` | Minimum rank: Novice; weapon profile: Ricochet; any weapon competency, natural attack form, or specific item that grants Ricochet access can use this Technique unless this Technique narrows that access; requires one real rebound-capable surface and one projectile or thrown piece that can credibly skip, glance, or continue through that angle |
| `target` | creature |
| `range` | short range / rebound line |
| `area` | single creature |
| `duration` | instant |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` resolves normally, but the target does not gain the full benefit of treating the line as purely direct |
| `tags` | attack, ricochet, indirect_line, disruption |

**Fantasy:** The target trusted the obvious line. The throw was not for the obvious line.

**World origin:** This Technique now sits provisionally under shared fieldcraft instead of one species. Corner workers, chase throwers, and other practical skirmishers learn that rims, stone lips, and iron fittings can continue a threat that should have ended on first contact. `Hacer que el Ángulo Muerda` is not trick-shot vanity. It is practical hostile geometry for bodies that think a bad corner already made them safe.

**Why this is not raw thrown damage:** A normal throw asks whether the direct line is open. `Hacer que el Ángulo Muerda` asks whether the environment can keep the threat alive past the direct line the target thought they had solved.

**Primary interaction surface:** `Ricochet` through one short, materially plausible rebound or skip line.

**Secondary interaction surface:** disruption, because the Technique pressures targets who think a corner, lip, or partial obstruction already settled the line cleanly.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. The Technique is still narrower than broad suppression, but it combines a real indirect line with same-attack degradation of partial cover or angle advantage. That geometry shift is stronger than a quick projectile rider.

**Effect:** Declare one real hard surface near the target or between you and the target that can plausibly carry a short rebound, skip, or angled continuation: a stone lip, wall edge, cart rim, shield edge, metal fitting, gate frame, slab corner, or similar rebound-capable point.

Make a Ricochet-bearing ranged or thrown attack against the target through that declared angle.

If the attack fails to connect, nothing further happens.

If the attack connects, it resolves normally, and the target treats any one partial line advantage that depended only on the direct line as `1 step worse` for this resolution:

- `Cobertura Ligera` becomes no cover
- `Cobertura Media` becomes `Cobertura Ligera`
- or an equivalent single-line partial protection loses one step of benefit for this attack only

This Technique does not ignore total solid cover, does not bend around a fully sealed barrier, and does not chain into multiple rebounds.

**Restrictions:**

- requires one real rebound-capable surface already present in the fiction
- requires a believable projectile or thrown piece that can skip, glance, or continue through a short rebound line
- only reduces one partial direct-line advantage by one step for this one attack
- does not ignore total cover, sealed barriers, or full loss of line of effect
- does not create homing behavior, multi-target threat, or chained rebounds
- applies to one creature only

### Dar de Comer a la Segunda Mano

| Field | Value |
| --- | --- |
| `name` | Dar de Comer a la Segunda Mano |
| `name_en` | Feed the Second Hand |
| `origin` | Claws + Dagger; alternate surfaces: Dagger + Hooked Sidearm, Two Short Blades |
| `world_origin` | Species: Zarnag; seed: The Scavenger Follows The Weak Line; transmission: false-hand pairing drills, off-hand fouling work, and close side-sequence practice; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user is already in close contact with one target and has two ready light close surfaces on different hands that can threaten the same body before the answer fully resets. |
| `requirements` | Minimum rank: Novice; no single weapon profile gate; requires two ready light close surfaces on different hands and a believable off-hand follow-through on the same target |
| `target` | creature |
| `range` | close contact |
| `area` | single |
| `duration` | until the end of the target's next activation or the first use of the displaced piece |
| `cost` | Rhythm 6; Attrition 2 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | Each attack in the sequence resolves against the target's normal `D.R.` separately |
| `tags` | attack, dual_wield, close_sequence, paired_surfaces |

**Fantasy:** One hand keeps the answer busy. The other hand spoils what the answer needed to keep working.

**World origin:** Zarnag side-pair cutters, carcass-openers, and tunnel-close fighters learn that one hand does not always kill the body, but it can keep the answer occupied long enough for the second hand to foul something useful before the body fully resets. `Dar de Comer a la Segunda Mano` is not flourish. It is ugly practical sequencing in close quarters where the opening disappears if you treat the two hands as separate thoughts.

**Why this is not just the basic two-weapon action:** The basic two-weapon action is broader and slower. `Dar de Comer a la Segunda Mano` is narrower and faster, but if both contacts land it also leaves one useful piece fouled or out of place. That makes it more than throughput, and it is why this version now pays heavier `Attrition`.

**Primary interaction surface:** paired close surfaces used as one short same-body sequence rather than as two disconnected swings.

**Secondary interaction surface:** false-hand fouling, because the first contact occupies the answer long enough for the off-hand to spoil one practical piece before the defense fully resets.

**Cost note:** `Rhythm 6 / Attrition 2` is deliberate. The Technique is cheaper than the broad basic two-weapon action only because it gives up flexibility: no retargeting, no movement, no heavy paired weapons, and no second attack if the first line fails to land. But if both contacts land, it also fouls one useful piece and can tax its first dependent roll, so the `Attrition` rises to 2.

**Effect:** Declare two ready light close surfaces on different hands: claw and dagger, dagger and hooked sidearm, two short blades, or another believable same-target pairing.

Make one close attack against the target with the first declared surface.

If the first attack fails to connect, the sequence ends there.

If the first attack connects, resolve it normally. Then immediately make one second close attack against the same target with the second declared off-hand surface at no additional `Rhythm` cost.

If the second attack also connects, choose one useful piece on that same target that one of the two contacts plausibly fouled, displaced, or partially stripped: a shield edge, wrist guard, hanging tool, mask tie, belt-fastened item, sling position, sheath mouth, grip wrap, hand-held implement, or another nearby practical piece.

That piece becomes `displaced` until the end of the target's next activation or until the target spends `Interactuar` to set it right, whichever comes first.

While `displaced`, the first `A.R.`, `D.R.`, or `S.R.` that directly depends on that exact piece suffers a penalty of `1` per rank bonus of the competency used for this Technique. Once such a roll resolves, the `displaced` state ends whether the target corrected it or not.

The second attack is part of the same Technique use. It cannot target a different creature, cannot include movement, and cannot be replaced by a second Technique, free grapple, or other extra process.

This Technique does not create broad multi-target pressure. It is one short same-body close sequence that also leaves one practical piece fouled or out of place if both contacts land.

**Restrictions:**

- requires two ready light close surfaces on different hands
- both attacks must target the same creature
- the second attack only happens if the first attack connects
- the displaced-piece effect only happens if both attacks connect
- the user must name one real piece that the two contacts could have plausibly fouled or partially stripped
- only the first roll that depends on that exact piece is penalized
- does not grant movement, retargeting, or multi-target pressure
- the second attack cannot be replaced by another Technique, grapple, or extra process
- does not bypass normal `Defense` or armor

### Cerrar la Salida a Dos Manos

| Field | Value |
| --- | --- |
| `name` | Cerrar la Salida a Dos Manos |
| `name_en` | Close the Exit with Both Hands |
| `origin` | Claws + Dagger; alternate surfaces: Dagger + Hooked Sidearm, Two Short Blades |
| `world_origin` | Species: Zarnag; seed: Quarantine Is Force; transmission: paired-hand exit-denial drills, close chase work, and crowding sequences; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user is already in close contact with one target and has two ready light close surfaces on different hands that can keep the target crowded through one short withdrawal line. |
| `requirements` | Minimum rank: Novice; no single weapon profile gate; requires two ready light close surfaces on different hands and a believable crowding line that can tax one immediate retreat |
| `target` | creature |
| `range` | close contact |
| `area` | single |
| `duration` | until the end of the target's next activation or its first attempt to use `Movement` to increase distance from you |
| `cost` | Rhythm 7; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | Each attack in the sequence resolves against the target's normal `D.R.` separately |
| `tags` | attack, dual_wield, close_sequence, exit_pressure |

**Fantasy:** One hand crowds the turn. The second hand makes the clean exit disappear.

**World origin:** Zarnag quarantine chasers, trench-pair fighters, and pit-close enforcers learn that two hands are sometimes less about killing fast and more about keeping one dangerous body from peeling away cleanly. `Cerrar la Salida a Dos Manos` is not a flourish combo. It is ugly practical crowding: the first hand keeps the turn dirty, the second hand makes retreat cost real time.

**Why this is not just the basic two-weapon action:** The basic two-weapon action is only broad offensive throughput. `Cerrar la Salida a Dos Manos` is narrower and costlier than `Dar de Comer a la Segunda Mano`, but if both contacts land it also taxes one breakaway attempt from the same body.

**Primary interaction surface:** paired close surfaces used as one short same-body sequence that ends in exit pressure.

**Secondary interaction surface:** crowding and quarantine pressure, because the sequence does not merely wound; it makes the target's next clean disengagement harder to afford.

**Cost note:** `Rhythm 7 / Attrition 1` is deliberate. This is still narrower than the generic two-weapon action, but if both attacks connect it also taxes one breakaway attempt. That positional pressure is stronger than a simple same-target two-hand sequence.

**Effect:** Declare two ready light close surfaces on different hands: claw and dagger, dagger and hooked sidearm, two short blades, or another believable same-target pairing.

Make one close attack against the target with the first declared surface.

If the first attack fails to connect, the sequence ends there.

If the first attack connects, resolve it normally. Then immediately make one second close attack against the same target with the second declared off-hand surface at no additional `Rhythm` cost.

If the second attack fails to connect, nothing further happens beyond its normal resolution.

If both attacks connect, the target becomes `step-checked` against you until the end of its next activation or until it first attempts to use `Movement` to increase distance from you, whichever comes first.

While `step-checked` is active, the target's first `Movement` that would break from your close contact costs `+2 Rhythm`. If the target does not pay that extra `Rhythm`, that `Movement` cannot increase distance from you and must instead stay in place or reposition without opening range if the fiction allows it.

This Technique does not root the target, does not stop all movement, and does not affect creatures other than the struck target. It only makes one immediate breakaway attempt dirtier and more expensive.

**Restrictions:**

- requires two ready light close surfaces on different hands
- both attacks must target the same creature
- the second attack only happens if the first attack connects
- the exit tax only happens if both attacks connect
- only affects the target's first `Movement` that would increase distance from you
- does not root, stop all movement, or create broad zone control
- does not grant movement, retargeting, or multi-target pressure
- the second attack cannot be replaced by another Technique, grapple, or extra process
- does not bypass normal `Defense` or armor

### Esconder la Segunda Línea

| Field | Value |
| --- | --- |
| `name` | Esconder la Segunda Línea |
| `name_en` | Hide the Second Line |
| `origin` | Claws + Dagger |
| `world_origin` | Species: Zarnag; seed: The Scavenger Follows The Weak Line; transmission: false-hand drills, low-line feints, and side-switch close work; availability: Common |
| `category` | attack |
| `type` | active |
| `trigger` | The user can present one obvious close line strongly enough that the target answers it, while still holding a second plausible line of contact in reserve. |
| `requirements` | Minimum rank: Novice; weapon profile: Unpredictability; any weapon competency, natural attack form, or specific item that grants Unpredictability access can use this Technique unless this Technique narrows that access; requires a close deceptive surface such as claws, dagger, hooked hand tool, or another odd-angle sidearm |
| `target` | creature |
| `range` | close contact |
| `area` | single |
| `duration` | until the user's next successful attack against that target or the end of the user's next activation |
| `cost` | Rhythm 5; Attrition 1 when used during ATB or active threat; no Attrition cost in normal exploration |
| `saving_roll` | `D.R.` negates contact and prevents the hidden-line setup |
| `tags` | attack, unpredictability, setup, false_read |

**Fantasy:** The target answered the hand they saw. The dangerous hand was the one they did not finish accounting for.

**World origin:** Zarnag close workers learn that some lines are shown only so the enemy commits to answering them. `Esconder la Segunda Línea` is not flourish. It is ugly practical deception inside contact: make the defense settle on the first threat so the second one arrives through the answer itself.

**Why this is not raw attack bonus:** A normal feint bonus just says the next attack is easier. `Esconder la Segunda Línea` is narrower and more physical: the target has prepared one item, guard, or defensive surface for the wrong line, and that exact prepared answer is worse on the follow-up.

**Primary interaction surface:** `Unpredictability` through false first-line presentation and hidden second-line follow-through.

**Secondary interaction surface:** setup, because the first successful contact changes how the target can answer the user's next attack.

**Cost note:** `Rhythm 5 / Attrition 1` is deliberate. This is a full attack that can also seed one short deceptive follow-up window, but only against the same target and only for the user's next attack.

**Effect:** Make a close `Unpredictability` attack with claws, dagger, or another narrowed-access deceptive close surface.

If the attack fails to connect, nothing further happens.

If the attack connects, the target becomes `wrong-answered` against you until your next successful attack against that target or the end of your next activation, whichever comes first.

While `wrong-answered` is active, the target's next `D.R.` against your next attack treats one declared line-dependent defensive answer as unavailable for that one roll:

- one shield-facing or guard-angle rider
- one parry-like weapon rider
- or one equivalent declared defensive surface that only works because the target answered the obvious first line

The target still makes its normal `D.R.`. This Technique does not remove `Defense` entirely, does not bypass armor, and does not deny all defensive bonuses at once. It only makes one wrong prepared answer fail to help on the follow-up.

**Restrictions:**

- requires a deceptive close surface and believable false-line presentation
- only affects the same target hit by the setup attack
- only affects the target's next `D.R.` against the user's next attack
- only suppresses one declared line-dependent defensive answer for that one roll
- does not remove base `Defense`, armor, or unrelated defensive bonuses
- does not stack with itself on the same target
- ends unused at the end of the user's next activation


## Next Design Layer

This document defines the Technique skeleton.

The next required layer is:

- **competency technique domains**

That layer defines what kinds of Techniques each competency is structurally suited to produce.

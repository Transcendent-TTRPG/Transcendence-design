# Ailments

**Authority data:** `data/system/ailments.yaml`
**Related docs:** `docs/system/roll-types.md`, `docs/system/difficulty-thresholds.md`, `docs/system/environmental-conditions.md`, `docs/system/attrition-fatigue.md`, `docs/system/general-rules.md`

---

## Purpose

This document defines the structural model for **Ailments** in Transcendence.

An Ailment is a harmful altered state that settles on a creature and changes how it functions until it is removed, relieved, or naturally ends.

The source of an Ailment does **not** define its category.

An Ailment may come from:

- a creature
- a weapon
- the environment
- prolonged exposure
- a scene hazard
- a curse
- or any other valid fictional cause

What matters is the nature of the harmful state once it exists on the target.

---

## Core Taxonomy

The umbrella category is:

- **ES:** Agravios
- **EN:** Ailments

Core Ailment families:

- `Alterations`
- `Infections`
- `Afflictions`
- `Poisons`
- `Curses`

This document begins with **Alterations**, the physiological disruption family.

---

## Universal Severity Rule

All Ailments use the same three severity levels:

- `Leve / Minor`
- `Moderado / Moderate`
- `Grave / Severe`

Severity is universal.

What severity **does** depends on the specific Ailment.

Severity may scale:

- penalties
- restrictions
- resistance pressure
- removal difficulty
- or persistence burden

But the three-level structure remains the same across all Ailment families.

### Default application pressure

Unless a specific Ailment entry says otherwise, the default resistance
pressure for Ailment severity is:

- `Minor / Leve` = `8 + NR`
- `Moderate / Moderado` = `13 + NR`
- `Severe / Grave` = `17 + NR`

Severity does **not** always mean that the ongoing penalty must increase.

Some Ailments use severity mainly to define:

- how hard they are to apply
- how hard they are to resist
- how hard they are to remove

while the settled functional result remains the same once the state is already on the body or mind.

### Ongoing effect scaling note

When an Ailment's main ongoing burden is a **numeric penalty**, prefer the
penalty value to come from the **rank bonus** of the source that applied it,
not from severity alone.

In those cases, severity should usually decide things such as:

- which extra restrictions activate
- whether new layers of consequence appear
- how hard the state is to break
- how much fictional commitment the state demands

This keeps source strength and settled state structure separate.

By contrast, more binary or structural Ailments such as blindness, paralysis,
knockdown, or full restraint do **not** need rank-bonus numeric scaling in the
same way. Their severity often matters more for:

- application pressure
- recovery difficulty
- persistence
- or additional state burdens

than for changing a numeric penalty band.

---

## Duration Rule

Because Transcendence uses ATB instead of round-based combat, Ailments should **not** default to round counts.

Prefer duration models such as:

- `until_removed`
- `until_trigger`
- `scene`
- `while_source_persists`
- `while_condition_persists`
- `sustained_by_environment`

Duration and recovery should stay separate.

- `duration` answers how long the Ailment remains
- `recovery` answers what must happen to end or relieve it

---

## Shared Condition Rule

Ailments follow the system's general **Strongest Condition** rule.

That means:

- equal effects never stack
- if a new application is stronger, it replaces the weaker one
- if a new application is equal but lasts longer or is harder to remove, it refreshes or resets the existing one

The system should not create parallel copies of the same harmful effect just because the source changed.

---

## Minimum Authoring Fields

Each Ailment entry should declare at minimum:

| Field | Purpose |
| --- | --- |
| `name` | Canonical name |
| `family` | Alteration, Infection, Affliction, Poison, or Curse |
| `description` | What the Ailment is in the fiction |
| `severity_levels` | Minor / Moderate / Severe effects |
| `application_requirements` | What fictional conditions allow it to be applied |
| `effect` | Mechanical outcome |
| `duration` | Persistence model |
| `recovery` | How it is removed, relieved, or ends |
| `resistance_or_escape` | What roll, action, or condition can oppose or break it |
| `stacking_rule` | Whether severity escalates, refreshes, or is replaced under the Strongest Condition rule |

Optional fields may include:

- source notes
- environment notes
- treatment notes
- escalation notes

---

## Alterations

Alterations are physiological disruptions.

They affect the body's normal function directly and may be caused by:

- temperature
- electricity
- impact
- entanglement
- internal destabilization
- or environmental exposure

They are classified by what they do to the body, not by whether the source was natural, hostile, ambient, or supernatural.

In practice, Alterations are also the main **combat-facing bodily state layer** of the system.

That means Alterations include states such as:

- loss of posture
- blindness
- deafness
- paralysis
- choking
- bodily imbalance
- sensory overload when it is functioning as a direct body-state disruption

The source may be:

- physical
- environmental
- mental
- creature-driven
- anomalous

but if the result is a direct operational disruption of the body during play, it still belongs here.

### Resistance Rule

Alterations use the Alteration resistance formula:

`R.R. = 1d10 + Resilience + Resistances + Bonuses`

If a specific Alteration is better escaped through direct action rather than pure resistance, that should be written explicitly in `recovery` or `resistance_or_escape`.

---

## Afflictions

Afflictions are mental, perceptual, or inner-state disruptions that compromise
judgment, clarity, emotional stability, or sensory coherence without being
defined primarily by direct bodily dysfunction.

### Resistance Rule

Afflictions use the Affliction resistance formula:

`R.R. = 1d10 + Composure + Resistances + Bonuses`

### Scope note

Afflictions are **not** just short-lived fear or confusion states.

They are a deeper subsystem tied to:

- trauma
- prolonged anomalous exposure
- misuse of certain objects
- altered perception of what lies beyond ordinary reality

They should usually include:

- a negative everyday effect
- an anomalous positive perception channel
- internal progression or treatment logic

Because of that, transient states such as:

- `Aterrorizado`
- `Desorientado`
- `Confundido`
- `Sobrecargado`

should not be treated as Afflictions by themselves.

They are better modeled as **transient bodily states or downstream effects**
that an Affliction, Alteration, encounter, or Technique may cause.

### Vestige / Link progression rule

For the current horror-facing model, the main recurring source of Affliction
pressure is interaction with:

- `Vestigios`
- `Vínculos`

Each meaningful interaction with a `Vestigio` or `Vínculo` may call for an
Affliction `R.R.`.

If the user fails that roll:

- the relevant sensory Affliction intensity increases by `1`
- if no Affliction has manifested yet, the pressure still accumulates on the
  relevant sensory track

The source itself determines which sense or sensory channel is being stressed.

### Intensity and manifestation

Afflictions use a pressure track before and after manifestation.

- intensity `0–4`: latent pressure; no full Affliction is manifested yet
- intensity `5`: the first Affliction on that linked sensory track manifests at
  `Minor / Leve`
- intensity `10`: that manifested Affliction reaches `Moderate / Moderado`
- intensity `15`: that manifested Affliction reaches `Severe / Grave`

If a character would gain more intensity on a sensory Affliction that is
already at `Severe / Grave`, the next increase should usually manifest a **new
Affliction** on the same sense or source-linked channel rather than pushing the
same entry beyond Severe.

### Recovery and worsening

Default Affliction pressure changes should follow:

- `+1` intensity after a failed qualifying `Vestigio` or `Vínculo` interaction
- `+1` intensity per night without adequate rest
- `-1` intensity per night of good sleep
- `-1` intensity per effective meditation session

Specific Afflictions may add narrower triggers, treatment routes, or worsening
conditions, but these are the current baseline rules.

### Structure note

An Affliction should usually include both:

- a negative terrestrial effect that impairs ordinary function
- a positive extranatural perception channel that reveals something ordinary
  senses do not

The resistance or treatment model should usually reduce the destabilizing cost
without automatically erasing that anomalous perception channel.

---

## Infections

Infections are biological or contaminant-driven Ailments that settle in the
body, remain present through time, and may spread to other creatures.

### Resistance Rule

Infections use the Infection resistance formula:

`R.R. = 1d10 + Tenacity + Resistances + Bonuses`

### Contagion

`Contagion / Contagio` is the difficulty of contracting the Infection when the
target is first exposed.

Each Infection should declare the qualifying exposure vectors and the
difficulty used for that initial Infection `R.R.`.

### Incubation

An Infection may have an incubation period.

During incubation:

- the Infection is already present in the organism
- no visible symptoms are required yet
- the target may still be carrying the condition before its functional effects
  fully appear

Once incubation ends, the Infection begins manifesting symptoms and can then be
treated, worsen, or spread according to its entry.

### Propagation

Once an Infection has passed incubation and is active, it may spread through
valid physical contact or another vector defined by the Infection.

A creature exposed to an active carrier must make the Infection `R.R.` defined
by that Infection to avoid becoming infected.

### Design note

Infections are not short combat riders by default.

They should usually define:

- exposure vector
- contagion difficulty
- incubation
- propagation conditions
- treatment route
- persistence inside the organism

---

## Poisons

Poisons are toxic Ailments introduced into the body through a delivery method.

### Resistance Rule

Poisons use the Poison resistance formula:

`R.R. = 1d10 + Tenacity + Resistances + Bonuses`

### Delivery methods

Common poison delivery families include:

- inoculation
- ingestion
- inhalation
- contact

Each Poison entry should define which delivery methods it supports.

### Persistence

Poisons should not default to an arbitrary round timer.

By base doctrine, a Poison remains active until:

- it is neutralized
- it leaves the system
- or its own entry states another end condition

### Handling note

Manipulating poisons should usually require the proper kit, tools, or trained
procedure. Identification, application, neutralization, and contamination risk
belong to the Poison's handling logic, not to generic freeform narration.

---

## Curses

Curses are extranatural Ailments attached to beings, objects, places, vows, or
other binding structures.

### Resistance Rule

Curses normally use the Curse resistance formula or detection/resistance route
defined by the specific curse.

### Scope note

Curses are not the same thing as Afflictions.

- `Afflictions` distort mind, perception, and inner coherence
- `Curses` bind a hostile extranatural rule onto a target, object, place, or
  relation

Some Curses may cause Afflictions downstream, but the two families should not
be collapsed into one.

---

## Initial Alteration Examples

### Electrizado

- **Family:** Alteration
- **Description:** Electrical disruption causes muscular loss of continuity, involuntary shock response, and unstable motor execution.
- **Application requirements:** Valid when the target suffers meaningful electrical discharge, prolonged conductive exposure, or another fictionally credible source of bodily shock.
- **Severity effects:**
  - All severities: attacks, movement, and Techniques tied to attacks or movement cost additional `Rhythm` equal to the **rank bonus of the source** that applied `Electrizado`; physical `S.R.` also suffer a penalty equal to that same **rank bonus**
  - Moderate and Severe: the target cannot use precise reactive physical answers such as movement-dependent reactions, tight interception, or other timing-sensitive physical responses unless it first succeeds on a `Tolerancia` `S.R.` against the original severity for that attempt
  - Severe: the **first** time on each activation the target attempts movement, an attack, or a Technique tied to attacks or movement, it must first attempt that `Tolerancia` `S.R.`; on a failure, the attempted action does not resolve and is lost to lock, spasm, or discharge recoil as the fiction requires
- **Duration:** `while_condition_persists`
- **Recovery:** Usually ends when the discharge is grounded, discharged, or otherwise interrupted long enough for the body to recover continuity. Once the source is no longer actively shocking the target, a successful `Tolerancia` `S.R.` against the original severity usually ends the state.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied; once active, recovery is primarily governed by bodily recovery rather than precision or mental control.
- **Stacking rule:** The same effect never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Lacerado

- **Family:** Alteration
- **Description:** The target has been torn, cut open, or otherwise wounded in a way that makes strenuous physical execution slower because movement must protect, compensate for, or push through the damaged tissue.
- **Application requirements:** Valid when the target suffers a deep cut, tearing bite, claw wound, hooked or serrated weapon contact, open wound under physical pressure, or another fictionally credible source of painful tissue disruption.
- **Severity effects:**
  - All severities: strenuous physical actions that directly stress the wound cost additional `Rhythm` equal to the **rank bonus of the source** that applied `Lacerado`
  - Moderate and Severe: actions that explosively drive force, weight, leverage, or full-body motion through the wounded line require a `Tolerancia` `S.R.` against the original severity for that attempt
  - Severe: the **first** time on each activation the target attempts one of those strenuous wound-stressing physical actions, it must first attempt that `Tolerancia` `S.R.`; on a failure, the attempted action or roll does not resolve and is lost to recoil, guarded movement, protective collapse, or pain break as the fiction requires
- **Duration:** `until_removed`
- **Recovery:** Ends when the target spends a suitable action to bind, brace, close, harden, or otherwise stabilize the wound pressure. `Medicina` can end the state when treatment is part of the fiction; some natural armor, regeneration, or hardening effects may provide their own recovery route.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied. Once active, recovery is usually practical or medical rather than mental: stabilize the wound, change how the body is moving, or receive treatment.
- **Stacking rule:** The same lacerated state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Atrapado

- **Family:** Alteration
- **Description:** The body is physically restrained or structurally impeded from moving freely.
- **Application requirements:** Valid when a creature, net, mechanism, adhesive hazard, collapsing surface, or similar source credibly restrains the target's bodily freedom.
- **Severity effects:**
  - All severities: movement becomes `0`
  - All severities: `A.R.`, `I.R.`, `D.R.`, and physical `S.R.` suffer a penalty equal to the **rank bonus of the source** that applied `Atrapado` whenever those rolls are made through the active restraint
  - Moderate and Severe: the target cannot use large-body, full-extension, or heavily leveraged actions through the restrained line unless it first succeeds on an `Agarre` `S.R.` against the original severity for that attempt
  - Severe: the **first** time on each activation the target attempts to attack, intercept, or break free through the restrained line, it must first attempt that `Agarre` `S.R.`; on a failure, the attempted action does not resolve and is lost to bind, catch, twist, or restraint drag as the fiction requires
- **Duration:** `until_removed`
- **Recovery:** Ends when the target breaks free, is released, or the restraining source stops holding them. The preferred self-recovery is an `Agarre` `S.R.` against a living hold, or another physical `S.R.` if the fiction is more about slipping out or disentangling than overpowering contact.
- **Resistance or escape:** Usually broken with an `Agarre` `S.R.`, though some sources may instead call for another physical `S.R.` or a Strength `C.R.` if no trained bodily technique clearly applies.
- **Stacking rule:** The restrained effect never creates parallel copies. Stronger restraint replaces the weaker state; equal restraint usually refreshes persistence.

### Congelado

- **Family:** Alteration
- **Description:** Body temperature and motor response are compromised by cold settling into the body itself.
- **Application requirements:** Valid when the target suffers prolonged freezing exposure, an ice-based hostile effect, or any other source that fictionally drives the body into functional cold impairment.
- **Severity effects:**
  - All severities: Agility `C.R.` and Agility `S.R.` suffer a penalty equal to the **rank bonus of the source** that applied `Congelado`; movement is reduced by half
  - Moderate and Severe: the target cannot voluntarily sprint, leap, climb, or use another clearly explosive mobility line unless it first succeeds on an `Aclimatación` `S.R.` against the original severity for that attempt
  - Severe: the **first** time on each activation the target attempts a movement action or Agility-based committed action through the cold-impaired line, it must first attempt that `Aclimatación` `S.R.`; on a failure, the attempted action does not resolve and is lost to stiffness, cold lock, or slipping motor response as the fiction requires
- **Duration:** `while_condition_persists`
- **Recovery:** Ends when body temperature is raised and the target is no longer functionally compromised by the cold. If the cold source is no longer actively forcing the state, a successful `Aclimatación` `S.R.` against the original severity usually ends the Alteration; `Medicina` can assist when treatment is part of the fiction.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied; once active, recovery is mainly environmental or physiological rather than positional.
- **Stacking rule:** The same cold impairment never creates separate copies. Repeated pressure usually escalates severity or refreshes persistence instead.

### Derribado

- **Family:** Alteration
- **Description:** The target loses stable footing or bodily posture and is brought to the ground.
- **Application requirements:** Valid when impact, sweep, force transfer, terrain failure, collision, or another fictionally credible cause knocks the target down.
- **Severity effects:**
  - All severities: `-3` to all rolls; the target's first movement action is spent getting up
- **Severity note:** Severity here mainly governs how hard the knockdown is to resist or avoid, not how much worse the ongoing state becomes once the target is already down.
- **Duration:** `until_removed`
- **Recovery:** Ends when the target stands up.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied; once suffered, removal is usually achieved by spending the first movement action to rise.
- **Stacking rule:** The knocked-down effect never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes the state.

### Conmocionado

- **Family:** Alteration
- **Description:** A destabilizing blow or shock has compromised the target's clarity, mental steadiness, and cognitive continuity.
- **Application requirements:** Valid when impact, internal shock, blast force, collision, or another fictionally credible cause produces a concussion-like destabilization.
- **Severity effects:**
  - All severities: Composure and Intellect `C.R.` and `S.R.` suffer a penalty equal to the **rank bonus of the source** that applied `Conmocionado`
  - Moderate and Severe: `Preparation` becomes `0`
  - Severe: the **first** time on each activation the target attempts a Composure- or Intellect-based `C.R.` or `S.R.`, it must first succeed on a `Contención` `S.R.` against the original severity for that attempt; on a failure, the attempted action or roll does not resolve and is lost to cognitive break, drift, or mental stall as the fiction requires
- **Duration:** `until_removed`
- **Recovery:** Ends when the target regains enough internal steadiness to restore clarity. The preferred self-recovery is a `Contención` `S.R.` against the original severity; `Medicina` can also end the state through treatment, and full rest may clear it between scenes if the fiction supports it.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied. Once suffered, recovery is mainly about regaining internal steadiness or receiving treatment rather than simply enduring pain.
- **Stacking rule:** The same cognitive destabilization never creates parallel copies. Stronger application replaces a weaker one; equal application usually refreshes persistence.

### Paralizado

- **Family:** Alteration
- **Description:** The body loses the ability to execute meaningful action through neuromuscular shutdown, rigid lock, or equivalent bodily arrest.
- **Application requirements:** Valid when electricity, venom, cold lock, bodily shock, forceful suppression, or another fictionally credible cause fully arrests meaningful action.
- **Severity effects:**
  - All severities: the target cannot perform meaningful actions
- **Severity note:** Severity here mainly governs how hard the state is to apply, resist, or break. Once fully paralyzed, the functional result is the same. Use `Paralizado` only when meaningful bodily action is actually arrested; use `Atrapado` for restraint, `Aturdido` for lost activation, and `Impedido` for execution breakdown that still leaves the body meaningfully active.
- **Duration:** `until_removed`
- **Recovery:** Ends when bodily control returns. The preferred self-recovery is a `Tolerancia` `S.R.` against the original severity once the source is no longer fully locking the body; some sources may instead require their own release condition before any roll is possible.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied. If already suffered, recovery is mainly physiological unless a specific source overrides it.
- **Stacking rule:** The paralyzed state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Ensordecido

- **Family:** Alteration
- **Description:** The target's hearing is functionally impaired or lost.
- **Application requirements:** Valid when sonic trauma, internal pressure shock, blast force, environmental overload, or another fictionally credible cause disrupts auditory function strongly enough that hearing is no longer a usable primary sense. If a source only muddies one auditory line, one ear, one echo path, or one bounded read channel, use a procedural state instead of `Ensordecido`.
- **Severity effects:**
  - All severities: the target cannot perform `C.R.` or `S.R.` that require hearing; the target also cannot rely on auditory cues for responses to threats they did not see
- **Severity note:** Severity here mainly governs application and recovery difficulty rather than adding different penalty bands once hearing is impaired. `Ensordecido` is for real functional hearing loss, not for temporary channel-noise, residue, masking, or one bounded sensory interference.
- **Duration:** `until_removed`
- **Recovery:** Ends when auditory function returns or the target is no longer functionally deafened. If the source is no longer actively deafening the target, a `Medicina` `S.R.` is the preferred way to restore function; otherwise the state lasts until time, treatment, or source removal make recovery credible.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied. Recovery is primarily medical or source-dependent rather than a matter of concentration.
- **Stacking rule:** The deafened state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Cegado

- **Family:** Alteration
- **Description:** The target cannot see.
- **Application requirements:** Valid when light, trauma, debris, darkness imposed as a body-state, ocular damage, or another fictionally credible source functionally removes sight strongly enough that vision is no longer a usable primary sense. If a source only fouls one eye-line, one read-point, or one bounded visual channel, use a procedural state instead of `Cegado`.
- **Severity effects:**
  - All severities: `-5` to all `A.R.`, `D.R.`, `I.R.`, and `S.R.`
- **Severity note:** Severity here mainly governs application and recovery difficulty rather than changing the lived result once the target is functionally blind. `Cegado` is for real functional sight loss, not for residue on one read channel, partial obscuration, or one bounded visual interference.
- **Duration:** `until_removed`
- **Recovery:** Usually ends when the blinding source dissipates, is removed, or vision is restored through treatment, cleansing, or time as appropriate to the source. When actual bodily restoration is needed, `Medicina` is the preferred recovery `S.R.`.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The blinded state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Confundido

- **Family:** Alteration
- **Description:** The target loses clean judgment and cannot reliably distinguish friend, foe, or intent in the immediate scene.
- **Application requirements:** Valid when bodily shock, sensory overload, neural disruption, concussion, toxins, or another fictionally credible source destabilizes immediate operational judgment.
- **Severity effects:**
  - All severities: `A.R.`, `I.R.`, and mental `S.R.` that require clean friend-foe discrimination, target identification, or intent reading suffer a penalty equal to the **rank bonus of the source** that applied `Confundido`
  - Moderate and Severe: before the target can deliberately choose a specific creature, side, or operative line in a crowded, ambiguous, or fast-changing scene, it must first succeed on an `Enfoque` `S.R.` against the original severity for that attempt
  - Severe: the **first** time on each activation the target attempts such a directed choice, it must first attempt that `Enfoque` `S.R.`; on a failure, the attempted action or roll does not resolve cleanly and the target must either hesitate, choose the nearest obvious line, or misdirect toward the wrong creature or priority as the fiction requires
- **Severity note:** `Confundido` is for real target-discrimination and operational-judgment break, not simple fear, spatial loss, or one noisy sensory channel.
- **Duration:** `until_removed`
- **Recovery:** Ends with a successful `Enfoque` `S.R.` against the original severity once enough operational clarity returns. `Medicina` or removal of the destabilizing source may also end it if the fiction supports that route.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied. Once active, recovery is mainly about regaining judgment continuity rather than simply waiting out one random moment.
- **Stacking rule:** The confused state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Desequilibrado

- **Family:** Alteration
- **Description:** The target's posture and bodily stability are compromised.
- **Application requirements:** Valid when footing, momentum, bodily shock, unstable ground, or another fictionally credible source compromises stable movement and defense.
- **Severity effects:**
  - All severities: `D.R.` and physical `S.R.` suffer a penalty equal to the **rank bonus of the source** that applied `Desequilibrado`
  - Moderate and Severe: the target cannot voluntarily rush, force movement, commit to unstable repositioning, or use posture-demanding mobility lines unless it first succeeds on an `Equilibrio` `S.R.` against the original severity for that attempt
  - Severe: if the target fails that required `Equilibrio` `S.R.` while trying to commit bodily weight through the unstable line, it immediately becomes `Derribado` at the same severity instead of merely losing the attempt
- **Duration:** `until_removed`
- **Recovery:** Ends with a successful `Equilibrio` `S.R.` against the original severity.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The unbalanced state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Aturdido

- **Family:** Alteration
- **Description:** The target is stunned badly enough to lose its next meaningful activation.
- **Application requirements:** Valid when impact, neural shock, concussive force, overload, or another fictionally credible source briefly shuts down clean action.
- **Severity effects:**
  - All severities: `R.R.` and `C.R.` suffer a penalty equal to the **rank bonus of the source** that applied `Aturdido`
  - All severities: the next time the target becomes leftmost on the ATB track, it cannot take meaningful actions and may only take free actions
  - Moderate and Severe: while `Aturdido` remains active, `Preparation` becomes `0`
  - Moderate and Severe: after each lost activation is consumed, the target must succeed on a `Tolerancia` `S.R.` against the original severity or `Aturdido` remains active and will consume the next meaningful activation as well
  - Severe: while `Aturdido` remains active, the target cannot voluntarily use timing-sensitive reactive lines unless it first succeeds on a `Tolerancia` `S.R.` against the original severity for that attempt
- **Duration:** `until_removed`
- **Recovery:** `Minor` ends after the first lost activation is consumed. `Moderate` and `Severe` end with a successful `Tolerancia` `S.R.` against the original severity after a lost activation, or when treatment, bodily stabilization, or source removal restores operational continuity. `Medicina` can also end the state if the fiction supports direct intervention.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The stunned state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence and which upcoming activation is threatened next.

### Desorientado

- **Family:** Alteration
- **Description:** The target loses directional certainty and mental orientation.
- **Application requirements:** Valid when spatial disruption, sensory scramble, dizziness, unstable perspective, or another fictionally credible source breaks the target's sense of direction.
- **Severity effects:**
  - All severities: mental `S.R.` suffer a penalty equal to the **rank bonus of the source** that applied `Desorientado`
  - Moderate and Severe: `Preparation` becomes `0`
  - Severe: the **first** time on each activation the target attempts to choose route, facing, target priority, or another orientation-dependent line, it must first succeed on an `Orientación` `S.R.` against the original severity for that attempt; on a failure, the attempted choice does not resolve and the target must either hesitate or take the simpler legal alternative the fiction supports
- **Duration:** `until_removed`
- **Recovery:** Ends with a successful `Orientación` `S.R.` against the original severity.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The disoriented state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Asfixiado

- **Family:** Alteration
- **Description:** The target cannot breathe properly and is fighting to remain operational.
- **Application requirements:** Valid when choking, drowning, smoke inhalation, crushing pressure, vacuum, or another fictionally credible source prevents proper breathing.
- **Severity effects:**
  - All severities: at the start of each activation, the target must make a `Tolerancia` `S.R.` against the original severity to avoid becoming incapacitated for that activation
  - All severities: the target suffers a cumulative `-1` penalty to all rolls for each activation spent while `Asfixiado` remains active
  - Moderate and Severe: while `Asfixiado` remains active, `Preparation` becomes `0`, and the target cannot voluntarily sprint, shout forcefully, maintain long strain, or use another clearly breath-hungry line unless it first succeeds on a `Tolerancia` `S.R.` against the original severity for that attempt
  - Severe: if the target fails the start-of-activation `Tolerancia` `S.R.`, the lost activation also drops held breath-dependent lines, spoken coordination, maintained grips, or equivalent sustained effort as the fiction requires
- **Duration:** `while_source_persists`
- **Recovery:** Ends when the choking, drowning, crushing, smoke, or other asphyxiating source no longer prevents breathing. The cumulative penalty resets when the condition ends.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The asphyxiated state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Impedido

- **Family:** Alteration
- **Description:** The target cannot execute weapon-rooted Techniques cleanly.
- **Application requirements:** Valid when bodily disruption, neural interference, pain lock, unstable grip, or another fictionally credible source prevents weapon-technique execution without fully paralyzing the creature.
- **Severity effects:**
  - All severities: the target cannot use Techniques tied to weapon competencies
  - Moderate and Severe: weapon-based `A.R.`, `I.R.`, and hand-critical physical `S.R.` suffer a penalty equal to the **rank bonus of the source** that applied `Impedido`
  - Severe: before the target can deliberately make a weapon-rooted attack, intercept, reload, re-ready, or other precise armed execution line, it must first succeed on an `Enfoque` `S.R.` against the original severity for that attempt
- **Severity note:** `Impedido` is for broken execution continuity in armed or hand-critical lines, not for full bodily arrest. Use `Paralizado` when meaningful bodily action is gone entirely.
- **Duration:** `until_removed`
- **Recovery:** Ends with a successful `Enfoque` `S.R.` against the original severity once the target can re-establish a clean execution line, or when the source preventing clean execution no longer applies.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The impaired state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Sobrecargado

- **Family:** Alteration
- **Description:** The target is overloaded by excessive sensory, neural, or internal pressure.
- **Application requirements:** Valid when sensory saturation, internal overload, psychic spillover expressed through the body, or another fictionally credible source overwhelms functional regulation.
- **Severity effects:**
  - All severities: `R.R.` suffer a penalty equal to the **rank bonus of the source** that applied `Sobrecargado`
  - Moderate and Severe: the target cannot voluntarily use inner-regulation or sensory-ordering lines such as `Contención`, `Enfoque`, `Resonancia`, or another directly comparable self-ordering `S.R.` without first succeeding on a `Contención` `S.R.` against the original severity for that attempt
  - Severe: the **first** time on each activation the target is forced to make an `R.R.` or attempts a self-ordering `S.R.` under pressure, it must first attempt that `Contención` `S.R.`; on a failure, the attempted self-ordering action does not resolve, or the forced `R.R.` is made without external bonuses, guidance, or aid as the fiction requires
- **Duration:** `until_removed`
- **Recovery:** Ends with a successful `Contención` `S.R.` against the original severity, or when the overloading source ends and the target regains enough internal regulation to stop being overloaded.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The overloaded state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Aterrorizado

- **Family:** Alteration
- **Description:** The target's body and immediate operational judgment are seized by acute terror. The state is not long-term trauma or deep anomalous distortion; it is a live bodily fear response that makes direct opposition, approach, and steady execution against the feared line harder.
- **Application requirements:** Valid when a creature, Technique, scene revelation, hostile presence, grotesque display, contamination threat, predator display, or another fictionally credible source creates an immediate terror line the body treats as urgent danger.
- **Severity effects:**
  - All severities: `A.R.`, `D.R.`, `C.R.`, and `S.R.` that directly oppose, approach, handle, or commit toward the feared source or feared line suffer a penalty equal to the **rank bonus of the source that applied `Aterrorizado`**
  - Moderate and Severe: the target cannot voluntarily reduce distance to the feared source or deliberately commit into the feared line unless it first succeeds on a `Contención` `S.R.` against the original severity for that attempt
  - Severe: the **first** time on each activation the target tries to directly oppose, approach, handle, or commit toward the feared line, it must first attempt that `Contención` `S.R.`; on a failure, the attempted action does not resolve and is lost to hesitation, recoil, or aborted commitment as the fiction requires
- **Duration:** `while_condition_persists`
- **Recovery:** Ends when the terror line is materially broken, disproved, removed, contained, or no longer functionally relevant; or when the target succeeds on a `Contención` `S.R.` against the original severity to regain enough inward control that the feared line no longer governs immediate bodily response.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied. Once active, the preferred self-recovery is `Contención`, because the problem is not pain tolerance or medical treatment but restoring enough internal control to act against the fear line.
- **Stacking rule:** The terrified state never creates parallel copies. A stronger terror line replaces a weaker one; an equal application usually refreshes persistence while the same feared line remains active.

---

## Design Rule

Alterations should not be defined by source flavor alone.

For example:

- a freezing cave
- an ice creature's breath
- a cursed winter relic

may all produce `Congelado`, even though the source fiction differs.

The source matters for:

- application
- difficulty
- removal
- resistance context

The Alteration name matters for:

- what the body is suffering
- what penalties apply
- what recovery the target needs

### Current alteration review buckets

Using the current doctrine, the existing Alterations fall into two main
authoring families.

**1. Rank-bonus penalty states**

These are the best candidates for:

- numeric penalty = **rank bonus of the source**
- severity = added restrictions, deeper consequence layers, harder recovery,
  or stronger commitment burdens

Current members:

- `Electrizado`
- `Lacerado`
- `Conmocionado`
- `Congelado`
- `Desequilibrado`
- `Desorientado`
- `Sobrecargado`
- `Aterrorizado`

`Congelado` is slightly mixed because it also halves movement, but its
Agility-facing degradation still reads more like a scalable penalty state than
like a purely binary lock.

**2. Structural / binary states**

These are better kept in the model where severity mainly governs:

- application pressure
- resistance or escape difficulty
- persistence
- extra state burdens

and **not** the size of a numeric penalty driven by source rank.

Current members:

- `Atrapado`
- `Derribado`
- `Paralizado`
- `Ensordecido`
- `Cegado`
- `Confundido`
- `Aturdido`
- `Asfixiado`
- `Impedido`

`Atrapado` is the biggest mixed case in this bucket, because it currently has
both a structural lock (`movement becomes 0`) and a severity-scaled numeric
penalty. It likely needs a later cleanup pass to decide whether that penalty
should become rank-bonus-based or whether the state should stay mostly
structural with severity-driven side burdens instead.

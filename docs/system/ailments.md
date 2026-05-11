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
  - Minor: `+1` Rhythm cost to attacks, movement, and Techniques tied to attacks or movement; `-1` to physical `S.R.`
  - Moderate: `+2` Rhythm cost to attacks, movement, and Techniques tied to attacks or movement; `-2` to physical `S.R.`
  - Severe: `+3` Rhythm cost to attacks, movement, and Techniques tied to attacks or movement; `-3` to physical `S.R.`
- **Duration:** `while_condition_persists`
- **Recovery:** Usually ends when the discharge is grounded, discharged, or otherwise interrupted long enough for the body to recover continuity. Once the source is no longer actively shocking the target, a successful `Tolerancia` `S.R.` against the original severity usually ends the state.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied; once active, recovery is primarily governed by bodily recovery rather than precision or mental control.
- **Stacking rule:** The same effect never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Lacerado

- **Family:** Alteration
- **Description:** The target has been torn, cut open, or otherwise wounded in a way that makes strenuous physical execution slower because movement must protect, compensate for, or push through the damaged tissue.
- **Application requirements:** Valid when the target suffers a deep cut, tearing bite, claw wound, hooked or serrated weapon contact, open wound under physical pressure, or another fictionally credible source of painful tissue disruption.
- **Severity effects:**
  - Minor: `+1` Rhythm cost to strenuous physical actions that stress the wound
  - Moderate: `+2` Rhythm cost to strenuous physical actions that stress the wound
  - Severe: `+3` Rhythm cost to strenuous physical actions that stress the wound
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
  - Minor: `-1` to `A.R.`, `I.R.`, `D.R.`, and physical `S.R.`
  - Moderate: `-2` to `A.R.`, `I.R.`, `D.R.`, and physical `S.R.`
  - Severe: `-3` to `A.R.`, `I.R.`, `D.R.`, and physical `S.R.`
- **Duration:** `until_removed`
- **Recovery:** Ends when the target breaks free, is released, or the restraining source stops holding them. The preferred self-recovery is an `Agarre` `S.R.` against a living hold, or another physical `S.R.` if the fiction is more about slipping out or disentangling than overpowering contact.
- **Resistance or escape:** Usually broken with an `Agarre` `S.R.`, though some sources may instead call for another physical `S.R.` or a Strength `C.R.` if no trained bodily technique clearly applies.
- **Stacking rule:** The restrained effect never creates parallel copies. Stronger restraint replaces the weaker state; equal restraint usually refreshes persistence.

### Congelado

- **Family:** Alteration
- **Description:** Body temperature and motor response are compromised by cold settling into the body itself.
- **Application requirements:** Valid when the target suffers prolonged freezing exposure, an ice-based hostile effect, or any other source that fictionally drives the body into functional cold impairment.
- **Severity effects:**
  - Minor: `-1` to Agility `C.R.` and Agility `S.R.`; movement reduced by half
  - Moderate: `-2` to Agility `C.R.` and Agility `S.R.`; movement reduced by half
  - Severe: `-3` to Agility `C.R.` and Agility `S.R.`; movement reduced by half
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
  - Minor: `-1` to Composure and Intellect `C.R.` and `S.R.`
  - Moderate: `-2` to Composure and Intellect `C.R.` and `S.R.`
  - Severe: `-3` to Composure and Intellect `C.R.` and `S.R.`
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
- **Severity note:** Severity here mainly governs how hard the state is to apply, resist, or break. Once fully paralyzed, the functional result is the same.
- **Duration:** `until_removed`
- **Recovery:** Ends when bodily control returns. The preferred self-recovery is a `Tolerancia` `S.R.` against the original severity once the source is no longer fully locking the body; some sources may instead require their own release condition before any roll is possible.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied. If already suffered, recovery is mainly physiological unless a specific source overrides it.
- **Stacking rule:** The paralyzed state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Ensordecido

- **Family:** Alteration
- **Description:** The target's hearing is functionally impaired or lost.
- **Application requirements:** Valid when sonic trauma, internal pressure shock, blast force, environmental overload, or another fictionally credible cause disrupts auditory function.
- **Severity effects:**
  - All severities: the target cannot perform `C.R.` or `S.R.` that require hearing; the target also cannot rely on auditory cues for responses to threats they did not see
- **Severity note:** Severity here mainly governs application and recovery difficulty rather than adding different penalty bands once hearing is impaired.
- **Duration:** `until_removed`
- **Recovery:** Ends when auditory function returns or the target is no longer functionally deafened. If the source is no longer actively deafening the target, a `Medicina` `S.R.` is the preferred way to restore function; otherwise the state lasts until time, treatment, or source removal make recovery credible.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied. Recovery is primarily medical or source-dependent rather than a matter of concentration.
- **Stacking rule:** The deafened state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Cegado

- **Family:** Alteration
- **Description:** The target cannot see.
- **Application requirements:** Valid when light, trauma, debris, darkness imposed as a body-state, ocular damage, or another fictionally credible source functionally removes sight.
- **Severity effects:**
  - All severities: `-5` to all `A.R.`, `D.R.`, `I.R.`, and `S.R.`
- **Severity note:** Severity here mainly governs application and recovery difficulty rather than changing the lived result once the target is functionally blind.
- **Duration:** `until_removed`
- **Recovery:** Usually ends when the blinding source dissipates, is removed, or vision is restored through treatment, cleansing, or time as appropriate to the source. When actual bodily restoration is needed, `Medicina` is the preferred recovery `S.R.`.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The blinded state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Confundido

- **Family:** Alteration
- **Description:** The target loses clean judgment and cannot reliably distinguish friend, foe, or intent in the immediate scene.
- **Application requirements:** Valid when bodily shock, sensory overload, neural disruption, concussion, toxins, or another fictionally credible source destabilizes immediate operational judgment.
- **Severity effects:**
  - All severities: at the start of each ATB activation, roll `1d100`; on a result greater than `50`, the target attempts to attack the nearest enemy even if that creature is actually an ally
- **Severity note:** Severity here should usually govern application pressure or recovery difficulty unless a specific source states otherwise.
- **Duration:** `until_removed`
- **Recovery:** At the start of each activation, before the confusion roll, the target may attempt an `Enfoque` `S.R.` against the original severity. On success, the condition ends.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The confused state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Desequilibrado

- **Family:** Alteration
- **Description:** The target's posture and bodily stability are compromised.
- **Application requirements:** Valid when footing, momentum, bodily shock, unstable ground, or another fictionally credible source compromises stable movement and defense.
- **Severity effects:**
  - Minor: `-1` to `D.R.` and physical `S.R.`
  - Moderate: `-2` to `D.R.` and physical `S.R.`
  - Severe: `-3` to `D.R.` and physical `S.R.`
- **Duration:** `until_removed`
- **Recovery:** Ends with a successful `Equilibrio` `S.R.` against the original severity.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The unbalanced state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Aturdido

- **Family:** Alteration
- **Description:** The target is stunned badly enough to lose its next meaningful activation.
- **Application requirements:** Valid when impact, neural shock, concussive force, overload, or another fictionally credible source briefly shuts down clean action.
- **Severity effects:**
  - Minor: `-1` to `R.R.` and `C.R.`
  - Moderate: `-2` to `R.R.` and `C.R.`
  - Severe: `-3` to `R.R.` and `C.R.`
  - All severities: the next time the target becomes leftmost on the ATB track, it cannot take meaningful actions and may only take free actions; after that lost activation, `Aturdido` ends
- **Duration:** `until_next_activation_resolves`
- **Recovery:** Ends immediately after the skipped activation is consumed.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The stunned state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes which upcoming activation is lost.

### Desorientado

- **Family:** Alteration
- **Description:** The target loses directional certainty and mental orientation.
- **Application requirements:** Valid when spatial disruption, sensory scramble, dizziness, unstable perspective, or another fictionally credible source breaks the target's sense of direction.
- **Severity effects:**
  - Minor: `-1` to mental `S.R.` and `-1` Preparation
  - Moderate: `-2` to mental `S.R.` and `-2` Preparation
  - Severe: `-3` to mental `S.R.` and `-3` Preparation
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
- **Severity note:** Severity here should usually govern how hard the state is to apply, resist, or remove unless a specific source says otherwise.
- **Duration:** `until_removed`
- **Recovery:** Ends with a successful `Enfoque` `S.R.` against the original severity once the target can re-establish a clean execution line, or when the source preventing clean execution no longer applies.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The impaired state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

### Sobrecargado

- **Family:** Alteration
- **Description:** The target is overloaded by excessive sensory, neural, or internal pressure.
- **Application requirements:** Valid when sensory saturation, internal overload, psychic spillover expressed through the body, or another fictionally credible source overwhelms functional regulation.
- **Severity effects:**
  - Minor: `-1` to `R.R.`
  - Moderate: `-2` to `R.R.`
  - Severe: `-3` to `R.R.`
- **Duration:** `until_removed`
- **Recovery:** Ends with a successful `Contención` `S.R.` against the original severity, or when the overloading source ends and the target regains enough internal regulation to stop being overloaded.
- **Resistance or escape:** Normally resisted with `R.R.` against Alterations when first applied.
- **Stacking rule:** The overloaded state never creates parallel copies. A stronger application replaces a weaker one; an equal application usually refreshes persistence.

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

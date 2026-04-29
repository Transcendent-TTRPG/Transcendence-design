# Technique Interaction Framework

**Primary references:** `docs/system/techniques.md`, `docs/system/mechanics-overview.md`
**Related docs:** `docs/system/roll-types.md`, `docs/system/atb-reference.md`, `docs/system/attrition-fatigue.md`, `docs/system/ailments.md`, `docs/system/environmental-conditions.md`, `docs/system/equipment-overview.md`, `docs/system/specializations.md`

---

## Purpose

This document defines how Techniques should interact with the rest of the game.

Its scope is primarily:

- exploration under pressure
- conflict and combat
- scene-level tactical or investigative action

It is **not** meant to be the main authoring framework for:

- long-form interlude systems
- crafting economies
- extraction loops
- language acquisition
- personality-trait expression

In Transcendence, a Technique is not meant to be:

- flavor text plus damage
- flavor text plus a Rhythm discount
- a disconnected named attack

A good Technique should produce a **functional interaction** with one or more real systems in the game, whenever that interaction makes thematic sense.

The goal is to keep Techniques:

- spectacular
- thematic
- mechanically meaningful
- connected to the full rules ecosystem

without turning them into arbitrary bundles of bonuses.

---

## Core Rule

Every Technique should interact with at least one real system surface.

Strong Techniques will often interact with:

- `2` surfaces cleanly
- sometimes `3` surfaces cleanly

More than that is possible, but should be treated carefully so the Technique does not become overloaded or incoherent.

The interaction should come from the Technique's fiction.

That means:

- the motion
- the pressure pattern
- the trained domain
- the equipment
- the bodily logic
- the target logic
- the environmental logic

should explain **why** the Technique touches that system.

If the interaction cannot be explained by the Technique's real fictional cause, it should not be there.

This interaction should usually matter inside an active scene:

- a hostile scene
- a pressured exploration scene
- a tactical or investigative moment where time, danger, or uncertainty matter

Techniques are not the default layer for resolving broad downtime or open-ended interlude development.

---

## Design Priority

When authoring a Technique, use this order:

1. Define the Technique's thematic and functional identity.
2. Identify which system surfaces that identity naturally touches.
3. Choose the smallest number of interactions needed to make the Technique mechanically alive.
4. Reject extra interactions that exist only to make the Technique look richer on paper.

This keeps the Technique expressive without becoming bloated.

---

## Valid Interaction Surfaces

### 1. Roll Interaction

The Technique can modify:

- the roll used
- a bonus or penalty on the roll
- a reroll condition
- what kind of opposition is used

Good uses:

- improved `A.R.` window through angle or setup
- modified `D.R.` contest through spoil timing
- changed `R.R.` pressure because of invasive contact
- temporary `S.R.` support because the Technique creates ideal conditions for the specialization

Bad uses:

- arbitrary flat bonuses with no fictional cause
- stacking roll inflation as the primary identity of the Technique

### 2. Threshold Interaction

The Technique can affect:

- difficulty tier
- effective threshold
- `NR` pressure
- access to a fixed-threshold task under better or worse conditions

Good uses:

- lowering a fabrication or field-treatment threshold by stabilizing the situation
- raising the threshold to resist a follow-up because the target is off-balance or compromised

### 3. ATB Interaction

The Technique can affect:

- Rhythm cost
- timing windows
- reaction access
- follow-up windows
- initial position in very bounded cases
- who can act safely next

Good uses:

- creating a punish window
- shifting who can react cleanly
- making a follow-up cheaper because the current Technique prepared it

Bad uses:

- generic Rhythm discounts with no combat logic
- turning every Technique into tempo manipulation

### 4. Attrition and Fatigue Interaction

The Technique can affect:

- Attrition cost
- projected pressure
- Fatigue acceleration
- recovery of control under exhaustion

Good uses:

- a Bastion Technique that reduces incoming strain but costs stability
- a Skirmish Technique that preserves tempo at lower bodily demand
- an Unstoppable Technique that works under pain but increases Attrition

### 5. Condition Interaction

The Technique can:

- apply a condition
- worsen a condition
- exploit a condition
- suspend or remove a condition
- change how a condition spreads or settles

Good uses:

- `Corrosion` worsening a degrading state
- `Interruption` breaking a state that depends on active execution
- `Meditation`-rooted Technique reducing a mental condition

### 6. Resistance Interaction

The Technique can:

- call for an `R.R.`
- reduce or increase resistance pressure
- transform what kind of resistance is relevant
- pair with a hybrid resistance origin

Important rule:

- Resistances should not be a sole Technique origin
- resistance-rooted Techniques must remain hybrid

### 7. Position and Zone Interaction

The Technique can affect:

- spacing
- line
- lane ownership
- target zone
- cover logic
- movement permission

This is especially important for:

- `Interception`
- `Line Control`
- `Ward`
- `Skirmish`
- `Ricochet`

### 8. Equipment Interaction

The Technique can affect:

- weapon handling
- shield use
- armor function
- block surfaces
- off-hand logic
- natural attack logic

Good uses:

- a Technique that is stronger with heavy shields because of actual mass
- a Technique that needs flexible weapons because its path geometry depends on them

Bad uses:

- item-specific gimmicks that should really live in the item itself

### 9. Competency and Specialization Interaction

The Technique can:

- require one competency
- require two roots
- treat a domain as a support surface
- unlock additional value when paired with a profile or specialization

Good uses:

- `Shield + Leadership`
- `Short Blades + Stealth`
- `Engineering + Traps`
- `Tolerance + Poison Resistance`

### 10. Recovery and Rest Interaction

This is a secondary surface, not a primary authoring pillar.

The Technique can affect:

- short-term recovery
- ability to continue after scene pressure
- stabilization after conflict

This should remain rarer than combat-state interaction, and should usually stay tied to:

- immediate post-scene stabilization
- preserving function during a pressured expedition
- bounded recovery consequences

It should not become a gateway to full interlude subsystems by default.

### 11. Environment Interaction

The Technique can interact with:

- natural vs. extranatural conditions
- severity stage
- acceleration of strain
- cover, terrain, surfaces, weather, heat, cold, and elemental logic

Good uses:

- `Ricochet` needing hard surfaces
- `Aclimatación`-rooted Technique resisting environmental escalation
- `Flow` losing value in poor footing

### 12. Manifestation Interaction

For now this should be rare and conservative.

Techniques may interact with:

- detection
- reading a manifestation
- safely approaching or handling a manifestation-linked scene

They should not cross into full Limbo or magic behavior.

---

## Out Of Scope

The following are not good default Technique pillars:

- personality trait expression through `P.R.`
- broad downtime crafting progression
- extraction and resource-economy loops
- language learning as a primary Technique output
- open-ended social identity simulation detached from scene pressure

These may still matter elsewhere in the game, but they should not define the main authoring logic of Techniques.

---

## Interaction Weight

Not all interactions are equal.

Use this rough hierarchy:

### Primary interaction

The system surface that defines what the Technique really does.

Examples:

- `Interception` -> line protection and reactive timing
- `Corrosion` -> degrading contact and persistence
- `Ward` -> spacing and pre-contact denial

### Secondary interaction

A system surface that supports the primary one and deepens it.

Examples:

- an `R.R.` rider
- minor Attrition effect
- threshold pressure on a follow-up action

### Rare interaction

A valid but tightly limited extra layer that should not take over the Technique's identity.

Examples:

- very small recovery effect
- narrow condition suspension
- bounded durability or gear clause

---

## Good Technique Pattern

A strong Technique usually looks like this:

- one clear fantasy
- one primary system interaction
- one secondary interaction that deepens it
- a clear cost or restriction

Example shape:

- fantasy: break the enemy's process while they commit
- primary interaction: `Interruption` on timing window
- secondary interaction: increases threshold on immediate follow-up or applies a short destabilized state
- cost: reactive Rhythm + Attrition

---

## Bad Technique Pattern

Avoid Techniques that:

- add damage, mobility, control, defense, recovery, and condition logic all at once
- modify too many rolls at the same time
- touch a system only because it was available
- have no real cost, limitation, or tactical profile
- feel like mini-spell lists disguised as martial actions

If a Technique starts reading like a shopping list of bonuses, it needs compression.

---

## Authoring Questions

When writing a Technique, ask:

1. What real system surface does this Technique primarily alter?
2. What secondary surface naturally follows from that same fiction?
3. Is the interaction caused by the Technique's actual bodily, technical, social, or tactical logic?
4. Would the Technique still feel alive if I removed one unnecessary bonus?
5. Is this using the game's systems, or just decorating the Technique with them?

If `5` is unclear, the Technique probably needs tightening.

---

## Current Design Standard

In Transcendence, Techniques should aim to be:

- thematically vivid
- mechanically specific
- system-aware
- cross-system when justified
- restrained when not justified

The game should reward players for learning how Techniques interact with:

- timing
- pressure
- conditions
- resistances
- space
- equipment
- fatigue
- thresholds
- trained domains

not just for collecting bigger numbers.

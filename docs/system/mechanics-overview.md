# Mechanics Overview

This document provides a horizontal view of all mechanical systems in Transcendence, organized for ability design. Use it when designing an ability to see every system it can interact with and every surface it can modify.

For the explicit doctrine of how Techniques should touch those systems, see [technique-interaction-framework.md](/Users/juangomez/Transcendence-workspace/Transcendence-design/docs/system/technique-interaction-framework.md).

For authoritative numeric values, see [`data/system/`](../../data/system/).
For detailed system descriptions, see the individual files in this folder.

---

## Systems at a glance

| System | Authority | Ability surfaces |
| --- | --- | --- |
| Characteristics | `characteristics.yaml` | Bonus to characteristic, bonus to derived attribute |
| Roll types | `roll-types.yaml` | Bonus to specific roll, conditional reroll, formula modifier |
| Difficulty Thresholds | `difficulty-thresholds.yaml` | Tier selection, base modifier, NR contribution |
| Environmental Conditions | `environmental-conditions.yaml` | Severity tier, natural vs. extranatural, element combinations, effect model |
| Limbo Manifestations | `limbo-manifestations.yaml` | Manifestation type (flow/vestige/link), detection method, proximity to link |
| Competencies & Progression | `competencies.yaml` | Effective level/rank bonus, maneuver access, progression unlock |
| Specializations | `specializations.yaml` | S.R. bonus, Technique access, Synapsis path unlock |
| Attrition & Fatigue | `attrition-fatigue.yaml` | Attrition cost reduction, Endurance increase, recovery amount |
| Rest & Recovery | `attrition-fatigue.yaml` | Recovery amount modifier, additional task access, favorable condition criteria |
| ATB combat timeline | `combat-atb-timeline.md` (ADR) | Rhythm cost reduction, initial position bonus, reaction access |
| Conditions & Resistances | `attrition-fatigue.yaml` | R.R. bonus by type, condition immunity, progression block |
| General Rules | `general-rules.md` | Specific-over-general priority, strongest-condition replacement, rounding, tool dependency |
| Action Structure | `atb-combat.yaml` + `atb-reference.md` | Action type gating, trigger windows, free/active/reactive classification |
| Equipment | `equipment.yaml` | Weapon assignment, shield role, armor interaction, zone-based defense surfaces |
| NPC / Creature Logic | `general-rules.md` | Trait-based exceptions, subsystem timing, encounter-layer pressure |

---

## Design Rule For Techniques

Techniques in Transcendence should not be authored as:

- flavor text plus damage
- flavor text plus Rhythm discount
- isolated named actions with no systemic consequences

A good Technique should interact with at least one real system surface.

Their main scope is:

- exploration under pressure
- combat and conflict
- scene-level tactical or investigative action

They are not the main design layer for:

- broad interlude subsystems
- personality-trait expression
- long-form crafting or extraction loops

Strong Techniques usually interact with:

- `1` primary surface
- `1` secondary surface

and sometimes a third bounded surface if the fiction clearly supports it.

The important point is that the interaction must come from the Technique's actual logic:

- motion
- pressure
- equipment
- trained method
- bodily structure
- timing
- environment
- social or perceptual leverage

If a Technique cannot explain why it touches a system, it should not touch it.

### Common Technique interaction surfaces

| Surface | Typical use |
| --- | --- |
| Roll | Bonus, penalty, reroll gate, altered opposition |
| Threshold | Raise/lower effective difficulty, change task pressure |
| ATB | Rhythm, timing windows, reaction access, follow-up windows |
| Attrition / Fatigue | Cost increase/reduction, strain acceleration, endurance pressure |
| Conditions | Apply, worsen, suspend, exploit, or remove states |
| Resistances | Call or modify `R.R.` logic through hybrid or delivery-based effects |
| Position / Zone | Reposition, deny movement, expose lane, alter target zone logic |
| Equipment | Change how weapon, shield, armor, or natural form matters |
| Competency / Specialization | Require, amplify, or combine trained domains |
| Recovery | Secondary surface: stabilize, restore, or extend post-scene function |
| Environment | Use terrain, surfaces, weather, elements, or severity stage |
| Manifestation | Rare and bounded: support detection or safe handling without becoming magic |

### Good default pattern

A strong Technique usually has:

- one clear fantasy
- one primary system interaction
- one secondary interaction
- one real cost, limitation, or access condition

That gives the Technique identity without turning it into an arbitrary stack of modifiers.

### System hygiene rule

Not every valid interaction is a good interaction.

When a Technique touches a system, also check:

- whether a more specific rule should override a general one
- whether it replaces or stacks with an existing effect
- whether it depends on tools, equipment, or a valid physical interface
- whether it changes what kind of action the user is actually taking

This prevents good Technique ideas from becoming bad rules text.

---

## General Rules

**Authority:** `docs/system/general-rules.md`

These rules are not just editorial background. They are active design constraints for Techniques.

### Core principles

| Principle | Meaning for Technique design |
| --- | --- |
| Specific over general | A Technique may override a baseline rule, but only inside its own clearly bounded scope |
| Round up | Any derived Technique value using fractions should assume upward rounding unless its own text says otherwise |
| Strongest condition | A Technique should usually replace, refresh, or fail to stack against a stronger same-type effect |
| Tool handling | Some Techniques should explicitly require valid tools, implements, or interfaces to function properly |
| Narrative flexibility | Not a blank check for vagueness; Techniques still need stable default resolution |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Override a baseline rule in a narrow case | Specific-rule exception |
| Refresh or replace an existing effect | Effect handling |
| Require exact or substitute tools | Access and feasibility |
| Create a bounded exception to rounding or timing | Technical override |

---

## Characteristics

9 base characteristics — all start at 0. Final value = species bonus + Synapsis.

### Physical

| Abbrev | Name | Description | Feeds |
| --- | --- | --- | --- |
| STR | Strength | Physical power, force application, grappling, striking | AR (melee), IR |
| AGI | Agility | Coordination, reaction speed, bodily precision, dodging | DR, AR (light), Preparation |
| TEN | Tenacity | Endurance, pain resistance, recovery, sustained effort | Endurance, RR (TEN variant) |

### Mental

| Abbrev | Name | Description | Feeds |
| --- | --- | --- | --- |
| INT | Intellect | Reasoning, memory, academic knowledge, structured problem-solving | CR, SR |
| CUN | Cunning | Improvisation, deception, reading intentions, adaptability | CR, SR, Preparation |
| WIS | Wisdom | Perception, intuition, judgment, interpreting nuance | CR, SR, Resilience |

### Social

| Abbrev | Name | Description | Feeds |
| --- | --- | --- | --- |
| CMP | Composure | Self-control, emotional stability, resistance to manipulation | RR (affliction), Preparation, Resilience |
| AUR | Aura | Passive involuntary impression projected onto others | CR (social) |
| PRE | Presence | Active intentional projection; imposing, persuading, inspiring | CR (social), SR |

### Derived attributes

| Attribute | Formula | Components | What it governs |
| --- | --- | --- | --- |
| Preparation | (AGI + CUN + CMP) / 3 ↑ | AGI, CUN, CMP | Initial ATB position; reaction readiness |
| Resilience | (TEN + WIS + CMP) / 3 ↑ | TEN, WIS, CMP | RR (alteration variant) |

---

## Roll types

Base die: **d10**. Evolutionary Advantage: roll 2d10, choose execution (take higher) or learning (take lower, use higher for learning check).

| Roll | Code | Formula | Used for |
| --- | --- | --- | --- |
| Attack Roll | A.R. | 1d10 + competency level + characteristic | Landing an effective strike |
| Defense Roll | D.R. | 1d10 + evasion level + applicable Agility + defense bonuses | Avoiding an incoming attack |
| Impact Roll | I.R. | (competency rank × weapon damage) + (characteristic × weapon grade) | Damage after AR beats DR |
| Characteristic Roll | C.R. | 1d10 + characteristic + Reference Level + bonuses | General aptitude without specific training |
| Resistance Roll | R.R. | Varies by threat type (see below) | Withstanding harmful effects |
| Specialization Roll | S.R. | 1d10 + specialization level + competency rank + characteristic + bonuses | Mastery in a specific skill |
| Personality Roll | P.R. | 2d10 | Narrative pressure surface, but not a primary Technique-authoring target |

### R.R. variants by threat type

| Threat type | Formula |
| --- | --- |
| Poison / infection | 1d10 + TEN + resistances + bonuses |
| Affliction / curses | 1d10 + CMP + resistances + bonuses |
| Alteration | 1d10 + Resilience + resistances + bonuses |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Flat bonus or penalty to a named roll | Direct roll pressure |
| Conditional reroll | Reliability shift |
| Change which roll opposes the effect | Resolution change |
| Convert direct opposition into threshold logic or the reverse | Contest structure change |

---

## Difficulty Thresholds

**Authority:** `data/system/difficulty-thresholds.yaml`

Five tiers apply to all roll-based systems (S.R., C.R., R.R., fabrication, ailments, etc.).

```text
Threshold = Base + NR
```

**NR** = Nivel de Referencia of the opposing creature, environmental condition, or task complexity (Narrator-assigned when no creature is directly opposing).

| Tier | Name (ES / EN) | Base | Formula |
| --- | --- | --- | --- |
| 1 | Fundamentos / Fundamental | 5 | 5 + NR |
| 2 | Desafiante / Challenging | 8 | 8 + NR |
| 3 | Rigurosa / Rigorous | 11 | 11 + NR |
| 4 | Exigente / Demanding | 14 | 14 + NR |
| 5 | Extrema / Extreme | 17 | 17 + NR |

When the challenge is a direct opposed roll (another character), both sides roll and compare — no fixed threshold is used.

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Shift tier up or down | Difficulty pressure |
| Modify effective `NR` | Scales task or environmental threat |
| Reduce threshold for a narrow action family | Specialist access |
| Increase threshold for a follow-up resisted action | Set-up pressure |

---

## Environmental Conditions

**Authority:** `data/system/environmental-conditions.yaml`

Environmental Conditions are a major Technique surface because they govern scene pressure when no narrower subsystem already owns the resolution.

### Key structure

| Layer | What it does |
| --- | --- |
| Natural vs. extranatural | Distinguishes world-consistent pressure from Limbo-derived distortion |
| Severity | Sets the difficulty tier family |
| `NR` | Scales the specific intensity of the current scene |
| Hinder / Restrict / Accelerate | Changes what is penalized, limited, or made more exhausting |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Ignore or reduce a severity expression | Environmental mitigation |
| Change whether a condition only hinders or fully restricts | Access preservation |
| Prevent or trigger acceleration | Attrition pressure control |
| Function differently in natural vs. extranatural scenes | World-logic interaction |
| Require terrain, weather, heat, cold, water, darkness, or unstable footing | Context gating |

---

## Limbo Manifestations

**Authority:** `data/system/limbo-manifestations.yaml`

Techniques should stay non-magical, but some may still interact with manifestation logic in cautious, bounded ways.

### Allowed interaction space

| Surface | Effect type |
| --- | --- |
| Detection support | Help identify flow, vestige, or link presence |
| Safe approach or handling | Improve interaction with manifestation-linked scenes |
| Interpretation aid | Clarify what kind of manifestation is present |

### Out of bounds for standard Techniques

| Surface | Why not here |
| --- | --- |
| Creating supernatural energy or effects from nothing | Belongs to later Limbo / magic design |
| Full manifestation control | Too far beyond trained non-magical Technique scope |

---

## Equipment

**Authority:** `data/system/equipment.yaml`

Equipment is not just a prerequisite list. It changes what kinds of Technique interactions make sense.

### Key equipment surfaces

| Surface | Meaning |
| --- | --- |
| Weapon assignment | Primary vs. auxiliary shapes cadence and sequence logic |
| Armor type | Changes how Agility contributes to `D.R.` and what defended Techniques look like |
| Shield role | Shared defensive equipment surface plus its own Technique identity |
| Zone-based defense | Changes how attacks and defended reactions matter per body area |
| Natural weapons | Use the same combat authoring layer through shared profiles |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Interact with a specific armor type | Defense expression |
| Reward auxiliary/off-hand use | Sequence or support logic |
| Change zone pressure | Body-area interaction |
| Use shield value or block surfaces indirectly | Guard logic |
| Require or exploit natural attack form | Shared profile access |

---

## Competencies & Progression

### Rank structure

2 levels per rank. Progress points earned through the learning advantage option (not execution).
Synapsis triggers on reaching the threshold level of each new rank (specializations only).

| Rank | Name (ES / EN) | Level range | Threshold level | Synapsis |
| --- | --- | --- | --- | --- |
| 0 | No entrenado / Untrained | 0 | — | — |
| 1 | Novato / Novice | 1–2 | 1 | +1 characteristic |
| 2 | Adepto / Adept | 3–4 | 3 | +1 characteristic |
| 3 | Experto / Expert | 5–6 | 5 | +1 characteristic |
| 4 | Maestro / Master | 7–8 | 7 | +1 characteristic |
| 5 | Consumado / Consummate | 9–10 | 9 | +1 characteristic |
| 6 | Trascendente / Transcendent | 11+ | 11 | +1 characteristic |

Cost per level: 10 pts (5 pts if major affinity). Major affinity determined by background.
Untrained characters can still roll any specialization: formula = 1d10 + characteristic only.

`D.R.` uses a hybrid defensive model. For `NPC -> PC`, hit zone is determined first; that zone determines which armor type constrains Agility and which zone block applies if defense fails.

### Competency types and bonuses

| Type | Per level bonus | Per rank bonus | Progression trigger |
| --- | --- | --- | --- |
| Weapons | +1 A.R. | +1 A.R. + 1 damage die | Successful `A.R.` with Learning Advantage, if the attack hits and deals damage |
| Armors | +1 zone block (relevant type) | No passive per-rank block bonus | Failed `D.R.` with Learning Advantage, if armor in the resolved zone absorbs impact |
| Shields | — | Access to additional shield maneuvers; Master reduces equipped shield movement penalty by grade | Successful shield Techniques or shield maneuvers |
| Evasion | +1 D.R. | +1 D.R. | Successful `D.R.` with Learning Advantage |
| Specialization | +1 S.R. | +1 S.R.; on entering a new rank, +1 characteristic via Synapsis | Successful `S.R.` with Learning Advantage |
| Resistances | +1 R.R. (specific type) | (see resistance subtypes) | Failed `R.R.` with Learning Advantage, if the effect is actually suffered |

### Resistance subtypes

| Subtype | Bonus |
| --- | --- |
| Physical | +1 R.R. vs broad physical resistance cases |
| Elemental | +1 R.R. vs elemental effects |
| Poison | +1 R.R. vs poisons |
| Infection | +1 R.R. vs infections |
| Affliction | +1 R.R. vs afflictions; +1 per rank during meditation |
| Alteration | +1 R.R. vs alterations |
| Curses | +1 to detect or resist curses |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Treat a competency as effectively higher for one Technique | Temporary expertise |
| Unlock a Technique only with dual-root competency logic | Hybrid access |
| Change what counts as the relevant competency in a narrow case | Resolution remapping |
| Interact with progression trigger conditions | Growth-facing design |

### NPC / Creature note

Not all hostile entities use player-style progression.

Creature Traits and encounter subsystems are valid Technique targets or interaction points when the fiction supports it.

| Surface | Effect type |
| --- | --- |
| Delay or weaken a hostile subsystem | Encounter interaction |
| Disable a creature Trait window | Targeted disruption |
| Force a phase or behavior shift | Encounter pacing change |

---

## Specializations

**Authority:** `data/system/specializations.yaml`
**Full framework:** `docs/system/specializations.md`

A specialization is a trainable technical, practical, or methodological domain tied to one attribute. Raw use produces a narrative effect only. Mechanical effects require follow-up actions or a specific Technique.

### Specialization Roll

```text
S.R. = 1d10 + Specialization Level + Competency Rank + Associated Characteristic + Bonuses
```

### Starting specializations

4 at Level 1 / Novice: 3 from background + 1 universal Tenacity choice (+1 TEN via Synapsis).

### Design clauses (all four must pass)

| Clause | Rule |
| --- | --- |
| Raw Attribute | A situation fully resolvable by raw attribute roll alone should not become a specialization |
| Technique | Must be broad enough to generate multiple Techniques |
| Differentiation | Two characters with the same attribute must feel different if only one has it |
| Trainability | Must represent a domain that can be practiced, failed, refined, and improved |

### Attribute distribution notes

| Attribute | Distribution guidance |
| --- | --- |
| Wisdom, Intellect | May carry more specializations — absorb crafts, knowledge, field interpretation |
| Tenacity | Keep smaller — broadly exercised by most characters; overloading makes it too easy to raise |
| Aura | Careful framing needed — partly passive/involuntary; domains should reflect resonance and attunement, not generic social skills |
| Composure | Focus on practiced regulation (concentration, containment, poise) — not abstract virtues |

### Specialization ability surfaces

| Surface | Effect type |
| --- | --- |
| +N to S.R. (specific specialization) | Skill mastery |
| Reduce S.R. difficulty threshold for Technique unlock | Access expansion |
| Treat specialization as one rank higher for Technique prerequisites | Effective rank bonus |
| Unlock cross-specialization Technique (requires two specializations) | Multi-domain access |

---

## Attrition & Fatigue

**Endurance formula:** 3 + (TEN × 2) (minimum 7 at creation after initial Tenacity Synapsis)

Endurance is the character's. Attrition belongs to the scene. Fatigue is the consequence of excess.

### Attrition cost scale

| Cost | Label | Description |
| --- | --- | --- |
| 0 | Trivial | No real scene demand |
| 1 | Standard | Standard meaningful action under pressure |
| 2 | High demand | Significant exertion; alters scene rhythm or absorbs serious pressure |
| 3 | Extreme | Beyond character's normal operating margin |

Reactions: not more costly because they are reactions — more costly because they execute under pressure. Typical cost: 1 (simple), 2 (demanding), 3 (limit).

### Fatigue thresholds

| State | Condition |
| --- | --- |
| No Fatigue | Attrition < Endurance |
| Fatigue 1 | Attrition ≥ Endurance |
| Fatigue 2 | Attrition ≥ 2 × Endurance |
| Fatigue 3 | Attrition ≥ 3 × Endurance |

**Projected vs Settled Fatigue:** During an active hostile scene, Fatigue is visible but not applied (projected). When the scene ends or drops in intensity, Fatigue settles and penalties apply.

### Conditions and environment

Conditions accelerate Fatigue but do not replace Attrition. Three stages:

| Stage | Effect |
| --- | --- |
| Hinder | Penalties; no Attrition cost added |
| Restrict | Limits available actions or adds difficulty |
| Accelerate | Adds +1 Attrition cost to relevant actions |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Reduce or increase Attrition cost | Strain manipulation |
| Delay, project, or settle pressure differently | Scene pacing |
| Function while under Fatigue pressure | Endurance expression |
| Make hostile scene pressure matter sooner or later | Tempo through exhaustion |

---

## Rest & Recovery

**Authoritative values:** `attrition-fatigue.yaml`

For Techniques, this is a secondary surface only. It supports scene continuity and short-term stabilization, not full interlude-system authoring.

### Short Rest

Brief pause after a hostile scene. Only the first Short Rest reduces Attrition normally.

| Duration | Attrition recovered | Tasks |
| --- | --- | --- |
| 15 minutes | 1 | 1 brief task |
| 30 minutes | 2 | 1 significant task |
| 60 minutes | 3 (+1 if conditions favorable) | 2 significant tasks |

### Full Rest

8-hour recovery. Requires reasonably adequate conditions.

| Component | Effect |
| --- | --- |
| Attrition recovery | 2 × Endurance |
| Affliction progression | −1 intensity per active affliction |
| Equipment durability | +5 per relevant item (on successful roll) |
| Daily resources | All "per day" or "after full rest" abilities recovered |

Fatigue levels automatically drop when Attrition recovery pushes the total below the relevant thresholds.

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| +N Attrition recovered during Short Rest | Recovery boost |
| Expand favorable condition criteria | Condition flexibility |
| Reduce Attrition recovery threshold for Full Rest | Efficiency boost |
| Reduce interruption risk during rest | Safety extension |

---

## ATB Combat Timeline

**Authoritative reference:** `docs/adr/combat-atb-timeline.md`

No fixed rounds. The leftmost marker on the track acts first. After acting, the marker moves right by the action's rhythm cost.

### Initial position

Derived in three steps:

1. **Opening Value** = Preparation + situational modifiers
2. **Reference Point** = highest Opening Value among all participants
3. **Initial Position** = Reference Point − Opening Value

Highest Opening Value → Initial Position 0 → acts first.

| Situation | Modifier |
| --- | --- |
| Ambushing | +2 |
| Weapon ready / prepared stance | +1 |
| Cover or dominant position | +1 |
| Target exposed or distracted | +1 |
| Surprised | −2 |
| Drawing weapon / reorganizing | −1 |
| Poor immediate terrain | −1 |
| Asleep, wounded, disoriented, or poorly positioned | −1 to −3 |

Tiebreak: raw Preparation before situational modifiers. If still tied: Narrator or table uses a fixed secondary criterion.

### Action bands

**Authoritative values:** `data/system/atb-combat.yaml`

| Band | Cost | Effect on tempo |
| --- | ---: | --- |
| Free | 0 | Does not advance the marker |
| Quick | 3 | Marker returns soonest |
| Standard | 5 | Normal delay |
| Heavy | 7 | Others act before you recover |
| Extreme | 9 | Reserved for major abilities; not used at base layer |

### Base action costs

| Base Action | Rhythm Cost | Attrition |
| --- | ---: | ---: |
| Free action (Drop, Speak) | 0 | 0 |
| Interact | 3 | 1 * |
| Move | 5 | 1 |
| Specialization | 5 | 1 |
| Attack with One-Handed Weapon | 5 | 1 |
| Attack with Two-Handed Weapon | 7 | 1 |
| Attack with Two One-Handed Weapons | 7 | 1 |

\* Only under meaningful scene pressure.

### Reactions

A reaction intervenes outside normal activation at a trigger (incoming attack, tactical opening, threat entering range). Costs:

- Rhythm cost: same as the equivalent action band
- Attrition cost: higher than the equivalent proactive action — executed under pressure with little margin
- Consequence: marker advances; future ATB position shifts accordingly

### Action structure surfaces

The corebook's action taxonomy matters for Technique design.

| Action type | Design implication |
| --- | --- |
| Active | Uses normal activation space and standard timing assumptions |
| Reactive | Needs a trigger and changes future ATB position |
| Free | Must remain small enough not to replace a real action |

| Surface | Effect type |
| --- | --- |
| Change an action from active to reactive in a narrow case | Triggered access |
| Turn a meaningful act into a free action only with strong restriction | Tempo exception |
| Add or remove trigger windows | Reaction design |
| Make a free action stop being free under pressure | Scene escalation |

---

## Backgrounds

Starting point for all characters: 4 specializations at Level 1 / Novice (3 from background + 1 universal Tenacity choice).

| Background | Major affinity | Starting specializations |
| --- | --- | --- |
| Martial Artist | Physical | 2 physical + 1 mental |
| Artisan | Arts & Crafts | 2 arts/crafts + 1 lore or social |
| Wanderer | Mental | 2 mental + 1 physical |
| Custodian | Lore | 2 lore + 1 social or mental |
| Noble | Social | 1 social + 2 any |

Universal Tenacity choice: +1 TEN at creation. Stacks with species bonuses.

---

## Ability design surfaces

This section is the primary reference for ability design. Each row is a surface an ability can touch.

Abilities should cross systems where it serves the thematic concept. A bonus that touches only one surface (e.g. "+1 AR") is generic. A bonus that crosses two or more systems with a thematic logic is differential.

### Single-system surfaces

| Surface | System | Effect type | Rolls affected |
| --- | --- | --- | --- |
| +N to A.R. | Rolls | Offensive accuracy | A.R. |
| +N to D.R. | Rolls | Defensive evasion | D.R. |
| +N to I.R. (damage dice) | Rolls | Damage output | I.R. |
| +N to C.R. (specific context) | Rolls | Situational aptitude | C.R. |
| +N to R.R. (specific type) | Rolls | Specific resistance | R.R. |
| +N to S.R. (specific skill) | Rolls | Skill mastery | S.R. |
| +N to characteristic | Characteristics | Attribute increase | All rolls that use that characteristic |
| +N to Preparation | Characteristics (derived) | Reaction speed / ATB position | Preparation → ATB initial position |
| +N to Resilience | Characteristics (derived) | Alteration resistance | R.R. (alteration) |
| +N to Endurance | Attrition | Larger Attrition pool | Fatigue thresholds |
| Reduce Attrition cost of action X by N | Attrition | Efficiency | Attrition accumulation rate |
| Recover N Attrition | Attrition | In-scene recovery | Current Attrition total |
| +N to initial ATB position | ATB | Combat readiness | ATB timeline position at scene start |
| Reduce rhythm cost of action X | ATB | Tempo control | ATB timeline position after action |
| Enable or reduce cost of specific reaction | ATB | Reactive access | ATB position + Attrition |
| Unlock maneuver or technique | Competencies | Access | New action available |
| +effective level in competency X | Competencies | Training bonus | A.R. / D.R. / S.R. depending on type |

### Cross-system surfaces (higher design value)

| Surface | Systems crossed | Thematic logic |
| --- | --- | --- |
| Reduce rhythm cost of actions when Attrition < Endurance | ATB + Attrition | Fresh fighter — efficiency while in margin |
| Reduce Attrition cost of reactions | ATB + Attrition | Reactive specialist — punish overcommitment cheaply |
| +A.R. when Fatigue ≥ 1 | Rolls + Fatigue | Fueled by pressure — dangerous when pushed |
| +D.R. and reduce rhythm cost of same action | Rolls + ATB | Fluid defense — blocks without losing tempo |
| Reduce Attrition cost of action X when characteristic ≥ N | Attrition + Characteristics | Conditioned specialist — high stat pays off in efficiency |
| Recover Attrition on successful D.R. | Attrition + Rolls | Second wind on evasion — mobile, cautious fighter |
| +Preparation when ambushing | ATB + Characteristics | Ambush specialist — translates situational awareness into tempo |
| +R.R. and reduce settled Fatigue threshold by N | Conditions + Fatigue | Resilience focus — shrug off conditions before they settle |
| Reduce rhythm cost of reactions when Preparation > attacker's | ATB + Characteristics | Anticipation — faster read means faster counter |
| Enable a reaction that also recovers N Attrition | ATB + Attrition | Reactive recovery — reward for well-timed defense |

---

## Design notes

**What makes a bonus thematic:** It follows a cause-effect logic that is specific to a character archetype or concept. "+1 AR" is not thematic. "+1 AR when the target has not yet acted this timeline" is thematic (it rewards acting before pressure settles).

**What makes a bonus differential:** It interacts with a system in a way that changes how a character plays, not just how much they deal or absorb. Rhythm cost reductions change the cadence of play. Attrition cost reductions change how long you can sustain output.

**Cross-system abilities are stronger by design:** An ability that touches two systems should typically be more restricted in its trigger condition to compensate for its broader effect. The restriction itself can carry thematic weight.

# Mechanics Overview

This document provides a horizontal view of all mechanical systems in Transcendence, organized for ability design. Use it when designing an ability to see every system it can interact with and every surface it can modify.

For the explicit doctrine of how Techniques should touch those systems, see [technique-interaction-framework.md](/Users/juangomez/Transcendence-workspace/Transcendence-design/docs/system/technique-interaction-framework.md).

For the machine-readable surface catalog used during Technique authoring, see [`data/system/technique-interaction-surfaces.yaml`](../../data/system/technique-interaction-surfaces.yaml).

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
| Materials & Fabrication | `materials-and-fabrication.yaml` | Material family, durability, base potency, accessibility, conservation, extraction, fabrication, refinement |
| Faction Reputation & Alliances | `faction-reputation-and-alliances.yaml` | Standing state, renown profile, alliance status, availability ceiling, trade access, price pressure |
| Attrition & Fatigue | `attrition-fatigue.yaml` | Attrition cost reduction, Endurance increase, recovery amount |
| Rest & Recovery | `attrition-fatigue.yaml` | Recovery amount modifier, additional task access, favorable condition criteria |
| ATB combat timeline | `combat-atb-timeline.md` (ADR) | Rhythm cost reduction, initial position bonus, reaction access |
| Conditions & Resistances | `attrition-fatigue.yaml` | R.R. bonus by type, condition immunity, progression block |
| General Rules | `general-rules.md` | Specific-over-general priority, strongest-condition replacement, rounding, tool dependency |
| Action Structure | `atb-combat.yaml` + `atb-reference.md` | Action type gating, trigger windows, free/active/reactive classification |
| Equipment | `equipment.yaml` | Weapon assignment, shield role, armor interaction, zone-based defense surfaces |
| Combat Equipment Catalog | `combat-equipment-catalog.yaml` | Named weapon items, shield class entries, item damage/range/weight/assignment, armor composition permissions |
| Mundane Equipment & Objects | `mundane-equipment-and-objects.yaml` | Ordinary carried goods, load categories, availability tier, price baseline, weight/load reference |
| Weapon Technique Profiles | `weapon-technique-profiles.yaml` | Combat expression profile, compatible effect family, access gate, shared weapon/natural-attack language |
| Natural Attack Forms | `natural-attack-forms.yaml` | Anatomy contact logic, compatible profiles, restricted profiles, species-level combat expression |
| Backgrounds | `backgrounds.md` | Starting specialization package, major affinity, creation-time Synapsis spread |
| Technique Origins | `technique-origins.md` | Origin front, transmission, availability, world-grounded access to Techniques |
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

## Faction Reputation & Alliances

This layer governs how the social world remembers the group beyond one immediate scene.

It is made of four linked but separate parts:

- `Faction Standing`
- `Public Renown`
- `Alliance Status`
- `Commerce & Availability`

Use this system when an authored element needs to touch:

- trust from a specific organized group;
- political or factional access;
- public social pattern or notoriety;
- alliance benefits and obligations;
- sourcing pressure, trade gates, or restricted inventory access.

### Main ability surfaces

| Surface | Typical use |
| --- | --- |
| Standing | Shift one faction up or down a bounded relationship ladder |
| Renown | Add, suppress, reinterpret, or redirect public action pattern |
| Alliance | Form, reinforce, strain, or break a formal relationship |
| Access | Open or close faction goods, information, services, or infrastructure |
| Availability | Raise or bypass a local sourcing ceiling |
| Trade terms | Apply discounts, surcharges, waiting time, or service priority |

### Design rule

Do not use this layer as a personality or moral-alignment system.

It should answer:

- who trusts us;
- who has reason to fear or welcome us;
- what doors are open;
- what this settlement can normally provide;
- and what faction relationships override that baseline.

It should not answer:

- what kind of soul the character has;
- whether one scene-level persuasion roll should auto-resolve all future consequences;
- or whether all factions interpret the same act identically.

---

## Mundane Equipment & Objects

This layer covers the ordinary carried goods and practical field objects that players interact with constantly but that do not need a unique subsystem each.

Use it when an authored element needs to touch:

- routine gear access;
- carried object category;
- simple price and load reference;
- mundane ammunition baseline;
- travel, camp, writing, medical, or utility object availability.

### Main ability surfaces

| Surface | Typical use |
| --- | --- |
| Object category | Distinguish travel gear, light source, recordkeeping, utility, medical, or mundane ammunition |
| Availability | Judge whether a mundane object is plausibly on hand in a place |
| Price baseline | Provide default cost before social, factional, or scarcity modifiers |
| Weight / load | Inform how much practical field support the group can carry |
| Bundle / loadout | Fast-start ordinary equipment package |

### Design rule

Do not overload this layer with:

- armor slot logic;
- weapon profile logic;
- unique magical item logic;
- or full fabrication/refinement procedures.

Use it as the fast baseline for ordinary physical play, then hand off to the more specific system when the object becomes mechanically deeper.

---

## Combat Equipment Catalog

This layer instantiates the combat-equipment structure into concrete authored entries.

Use it when an authored element needs to touch:

- a named weapon item rather than only a weapon family;
- shield class entries as catalog objects;
- item-specific damage, range, weight, associated characteristic, or assignment;
- or the rule that armor is composed from slot, category, material, and grade rather than from giant suit lists.

### Main ability surfaces

| Surface | Typical use |
| --- | --- |
| Named weapon item | Reference a concrete weapon instead of only a broad family |
| Item bonus text | Tie a weapon's special baseline incentive to a tactic or target condition |
| Assignment | Distinguish `Primary` from `Auxiliary` item structure |
| Shield class | Apply class-authored cover, armor, and movement logic |
| Armor composition | Check what part of an armor piece comes from slot/category vs. material |

### Design rule

Do not use this catalog to override the structural rules in `equipment-overview.md`.

The correct hierarchy is:

1. `equipment-overview` defines the stable logic
2. `combat-equipment-catalog` defines concrete combat items
3. `materials-and-fabrication` defines what those items are made from and how they survive material pressure

---

## General Rules

**Authority:** `docs/system/general-rules.md`

These rules are not just editorial background. They are active design constraints for Techniques.

### Core principles

| Principle | Meaning for Technique design |
| --- | --- |
| Specific over general | A Technique may override a baseline rule, but only inside its own clearly bounded scope |
| Thematic-mechanical synthesis | First ask what the fiction most credibly supports, then test what the numbers most safely support, and keep the strongest middle ground between both |
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

Base die: **d10**. Evolutionary Advantage applies to active execution rolls (`A.R.`, `D.R.`, `S.R.`): roll 2d10, choose execution (take higher) or learning (take lower, use higher for learning check). `R.R.`, `C.R.`, and `P.R.` do not use Evolutionary Advantage by default.

| Roll | Code | Formula | Used for |
| --- | --- | --- | --- |
| Attack Roll | A.R. | 1d10 + competency level + competency rank + characteristic + bonuses | Landing an effective strike |
| Defense Roll | D.R. | 1d10 + applicable Evasion + applicable Agility + defense bonuses | Avoiding an incoming attack |
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
| Discovery gate | Determine whether a vestige can be intentionally used |
| Medium requirement | Check whether light, sound, vibration, heat, or another valid carrier exists |
| Affliction pressure | Track whether use raises sensory Affliction intensity |
| Link qualification | Check whether the bearer has the required linked Affliction severity |

### Out of bounds for standard Techniques

| Surface | Why not here |
| --- | --- |
| Creating supernatural energy or effects from nothing | Belongs to later Limbo / magic design |
| Full manifestation control | Too far beyond trained non-magical Technique scope |

---

## Ailments

**Authority:** `data/system/ailments.yaml`

Ailments are one of the main cross-system surfaces for Techniques because they
carry named ongoing consequences instead of vague penalties.

### Core taxonomy

| Family | Main logic |
| --- | --- |
| Alterations | Direct bodily or operational disruption |
| Infections | Biological / contaminant state with contagion and incubation logic |
| Afflictions | Sensory, perceptual, or inner-state distortion with intensity logic |
| Poisons | Toxic states resolved through delivery method and persistence in the organism |
| Curses | Extranatural binding rules attached to a target, object, place, or relation |

### Key Technique surfaces

| Surface | Effect type |
| --- | --- |
| Apply a named Ailment | Direct ongoing state pressure |
| Escalate or downgrade severity | Ailment pressure by tier |
| Modify the qualifying `R.R.` | Delivery or resistance logic |
| Suppress, stabilize, or shorten persistence | Relief without erasing the whole subsystem |
| Interact with Affliction intensity | Vestigio / Vínculo pressure and recovery logic |

### Design rule

If a Technique wants to create an ongoing state, first check whether a named
Ailment already owns that effect. If not, the missing mechanic should be
defined in the Ailment layer before the Technique treats it as freeform text.

---

## Wounds & Damage

**Authority:** `data/system/wounds-and-damage.yaml`

Wounds and damage are not just "lose HP." This layer distinguishes impact,
zone block, wound slots, collapse, durability, and break logic.

### Key structure

| Layer | What it does |
| --- | --- |
| Impact vs. Block | Determines whether harm penetrates protection |
| Wound slots by zone | Tracks bodily saturation and collapse on PCs |
| NPC / creature surfaces | Uses parts, HP, durability, and linked functions |
| Critical break logic | Resolves whether a valid critical can break a part or object |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Add or reduce Impact pressure | Damage-facing attack shaping |
| Change how Block matters in one narrow case | Protection interaction |
| Stabilize or preserve a wounded target | Medical or endurance continuity |
| Mark a part, zone, or structural weakness | Break setup or follow-up pressure |
| Modify valid break attempts | Potency, critical range, or durability interaction |

### Design rule

Techniques should not collapse all physical consequences into generic damage.
If the fiction is about bodily spill, wound continuity, broken parts, or zone
failure, this layer should be the real authority.

---

## Cover / Visibility / Concealment

**Authority:** `data/system/cover-visibility-concealment.yaml`

This layer owns protection by line, what can be seen, how hidden states work,
and what it takes to recover a target's position or reading surface.

### Key structure

| Layer | What it does |
| --- | --- |
| Cover | Interferes with attack lines and direct targeting |
| Visibility | Defines how far and how clearly details can be perceived |
| Concealment | Governs hidden state, approximate location, and re-detection |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Raise or lower effective cover | Attack-line pressure |
| Create or deny a refuge point | Position-based protection |
| Alter visibility tier or readable range | Scene perception pressure |
| Reveal, blur, or preserve position | Hidden-state control |
| Break physical cover | Durability and structure interaction |

### Design rule

Techniques should not say "the target is harder to hit" or "the user is hidden"
if the real effect is cover, concealment, or visibility loss. Use the named
system instead.

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

## Materials & Fabrication

**Authority:** `data/system/materials-and-fabrication.yaml`

This layer owns the logic of what materials are, how they are extracted,
preserved, transformed, and refined into authored outputs.

### Key structure

| Layer | What it does |
| --- | --- |
| Material family | Groups materials by shared handling and processing logic |
| Grade | Tracks quality band of the material itself |
| Accessibility | Sets how demanding extraction, identification, or work should be |
| Conservation | Determines whether a material is stable, perishable, or volatile |
| Fabrication domain | Identifies which specialization actually owns the work |
| Refinement path | Defines how a valid object can gain an additional authored property |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Read or exploit a material property | Material-facing setup |
| Reduce a bounded extraction or work threshold | Specialist efficiency |
| Preserve a volatile input | Continuity under pressure |
| Accelerate one authored work interval | Limited production pressure |
| Mark a valid refinement interface | Upgrade permission rather than freeform bonus creation |

### Design rule

Techniques may touch this layer, but they should not replace whole crafting,
extraction, or production loops. They should usually set up, preserve, exploit,
or accelerate one bounded interaction that the material system already owns.

---

## Weapon Technique Profiles

**Authority:** `data/system/weapon-technique-profiles.yaml`

Weapon Technique Profiles are the shared combat-expression layer between a
weapon competency, a natural attack form, and a concrete Technique.

### Core role

| Layer | What it answers |
| --- | --- |
| Weapon competency | What the character can wield effectively |
| Weapon Technique Profile | What style of combat pressure the action belongs to |
| Technique | What happens right now, with what cost and effect |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Grant access through a specific profile | Combat identity gate |
| Restrict effect families by profile | Keep weapon fantasy coherent |
| Build follow-up logic inside one profile family | Sequencing without global combo rules |
| Share the same combat language across weapons and natural forms | Unified Technique ecosystem |

### Design rule

Profiles are not standalone Techniques and not item-by-item trees. They are the
bridge that lets spear thrust, tail sweep, claw rake, or shield catch live in
the same combat authoring language when the contact logic matches.

---

## Natural Attack Forms

**Authority:** `data/system/natural-attack-forms.yaml`

Natural attack forms are the inverse compatibility layer for natural combat.
They do not create a separate Technique school; they map anatomy to existing
Weapon Technique Profiles.

### Core role

| Layer | What it answers |
| --- | --- |
| Natural attack form | What kind of contact the body creates |
| Compatible profiles | Which shared combat expressions that anatomy can inherit |
| Restricted profiles | Which expressions would be a stretch or require special justification |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Access shared profiles through anatomy | Natural combat integration |
| Restrict poor-fit profiles | Keep body logic credible |
| Override generic form access at species level | Species-specific combat identity |
| Use anatomy as a valid interface for interception, control, puncture, impact, or delivery | Shared combat permission |

### Design rule

Natural forms should inherit from the same shared profile layer used by
manufactured weapons whenever possible. If a claw, bite, horn, shell, or tail
cannot map cleanly to existing profiles, that may justify a new profile or a
species exception, but not a duplicate natural-only subsystem by default.

---

## Technique Origins

**Authority:** `docs/system/technique-origins.md`

Technique Origins ground authored Techniques in the world instead of treating
them as abstract unlocks granted automatically by progression.

Use this layer when an authored element needs to touch:

- where a Technique comes from;
- who plausibly teaches, preserves, or restricts it;
- what transmission path makes it available;
- and what part of the world gives the Technique its identity.

### Core role

| Layer | What it answers |
| --- | --- |
| Competency | Whether the character can understand and execute this kind of method |
| Technique origin | Why the method exists in the setting and what front produced it |
| Transmission | How the character actually encounters or learns it |
| Availability | How widely the method circulates in the world |

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Origin front | Species, doctrine, or region as the primary source of a Technique |
| Origin focus | The functional sphere the Technique serves inside that front, such as reconnaissance, triage, threshold control, containment, surveying, or escort discipline |
| Holder | The concrete body that currently teaches, guards, sells, restricts, or preserves the Technique |
| Transmission path | Teacher, order, battlefield inheritance, manuscript, ritual, or local tradition |
| Availability | How easy the Technique is to encounter, buy, inherit, or be initiated into |
| Discovery path | Whether the Technique enters play through exploration, faction access, observation, trade, archive recovery, or rediscovery |
| Adaptation | Whether a non-native user can learn an analogous form through a credible substitute |

### Design rule

Progression grants capability, not spontaneous knowledge.

If a Technique matters enough to be authored, it should normally answer:

- who developed it;
- under what pressure or need;
- how it survived;
- and why the current character can access it at all.

The full authored catalog is part of the world's knowledge ecology, not a free
player pick list.

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

Cost per level: 10 pts. Specializations with major affinity from background cost 5 pts. Resistances do not use major affinity by base rule.
Untrained characters can still roll any specialization: formula = 1d10 + characteristic only.

`D.R.` uses a hybrid defensive model. For `NPC -> PC`, hit zone is determined first; that zone determines which armor type constrains Evasion and Agility, and which zone block applies if defense fails.

### Competency types and bonuses

| Type | Per level bonus | Per rank bonus | Progression trigger |
| --- | --- | --- | --- |
| Weapons | +1 A.R. | +1 A.R. + 1 damage die | Successful `A.R.` with Learning Advantage, if the attack hits and deals damage |
| Armors | +1 zone block (relevant type) | No passive per-rank block bonus | Failed `D.R.`, if armor in the resolved zone absorbs impact |
| Shields | — | Access to additional shield maneuvers; Master reduces equipped shield movement penalty by grade | Successful shield Techniques or shield maneuvers |
| Evasion | +1 D.R. | +1 D.R. | Successful `D.R.` with Learning Advantage |
| Specialization | +1 S.R. | +1 S.R.; on entering a new rank, +1 characteristic via Synapsis | Successful `S.R.` with Learning Advantage |
| Resistances | +1 R.R. (specific type) | (see resistance subtypes) | Exposure progress: failed `R.R.` or partial consequence from a relevant danger, if the character survives |

### Resistance subtypes

| Subtype | Bonus |
| --- | --- |
| Poison | +1 R.R. vs poisons |
| Infection | +1 R.R. vs infections |
| Affliction | +1 R.R. vs afflictions; +1 per rank during meditation |
| Alteration | +1 R.R. vs alterations |
| Curses | +1 to detect or resist curses |

Resistances do not reduce Impact, elemental damage, wounds, or HP damage. Elemental origin is handled by creature, material, object, or effect traits.

| Elemental trait | Damage effect |
| --- | --- |
| Minor Resistance | 50% damage from that origin |
| Major Resistance | 0 damage from that origin |
| Minor Vulnerability | 150% damage from that origin |
| Major Vulnerability | 200% damage from that origin |

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
| Fatigue 4 | Attrition ≥ 4 × Endurance |
| Fatigue 5 | Attrition ≥ 5 × Endurance |

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

### Ability surfaces

| Surface | Effect type |
| --- | --- |
| Major affinity | Reduced progress cost inside one specialization family |
| Starting package | Opening access to a limited set of trained domains |
| Creation Synapsis spread | Early characteristic distribution through starting ranks |
| Background gate | Narrative justification for certain early contacts, training paths, or world access |

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

**When theme and balance disagree:** Resolve in three steps. First ask what is most thematically credible. Then ask what creates the healthiest play pattern and numeric pressure. Finalize the rule at the strongest middle point that preserves identity without creating a dominant or degenerate option.

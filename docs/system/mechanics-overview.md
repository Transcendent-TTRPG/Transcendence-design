# Mechanics Overview

This document provides a horizontal view of all mechanical systems in Transcendence, organized for ability design. Use it when designing an ability to see every system it can interact with and every surface it can modify.

For authoritative numeric values, see [`data/system/`](../../data/system/).
For detailed system descriptions, see the individual files in this folder.

---

## Systems at a glance

| System | Authority | Ability surfaces |
| --- | --- | --- |
| Characteristics | `characteristics.yaml` | Bonus to characteristic, bonus to derived attribute |
| Roll types | `roll-types.yaml` | Bonus to specific roll, conditional reroll, formula modifier |
| Competencies & Progression | `competencies.yaml` | Effective level/rank bonus, maneuver access, progression unlock |
| Attrition & Fatigue | `attrition-fatigue.yaml` | Attrition cost reduction, Endurance increase, recovery amount |
| Rest & Recovery | `attrition-fatigue.yaml` | Recovery amount modifier, additional task access, favorable condition criteria |
| ATB combat timeline | `combat-atb-timeline.md` (ADR) | Rhythm cost reduction, initial position bonus, reaction access |
| Conditions & Resistances | `attrition-fatigue.yaml` | R.R. bonus by type, condition immunity, progression block |

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
| Defense Roll | D.R. | 1d10 + evasion level + AGI + armor | Avoiding an incoming attack |
| Impact Roll | I.R. | (competency rank × weapon damage) + (characteristic × weapon grade) | Damage after AR beats DR |
| Characteristic Roll | C.R. | 1d10 + characteristic + Reference Level + bonuses | General aptitude without specific training |
| Resistance Roll | R.R. | Varies by threat type (see below) | Withstanding harmful effects |
| Specialization Roll | S.R. | 1d10 + specialization level + competency rank + characteristic + bonuses | Mastery in a specific skill |
| Personality Roll | P.R. | 2d10 | When a personality trait decisively influences a situation |

### R.R. variants by threat type

| Threat type | Formula |
| --- | --- |
| Poison / infection | 1d10 + TEN + resistances + bonuses |
| Affliction / curses | 1d10 + CMP + resistances + bonuses |
| Alteration | 1d10 + Resilience + resistances + bonuses |

---

## Competencies & Progression

### Rank structure

| Rank | Level range | Progression cost |
| --- | --- | --- |
| Untrained | 0 | — |
| Novice | 1–3 | 10 pts (5 pts if major affinity) |
| Adept | 4–6 | 10 pts (5 pts if major affinity) |
| Expert | 7–9 | 10 pts (5 pts if major affinity) |
| Master | 10+ | 10 pts (5 pts if major affinity) |

3 levels per rank. Progress points earned through the learning advantage option (not execution).

### Competency types and bonuses

| Type | Per level bonus | Per rank bonus | Progression trigger |
| --- | --- | --- | --- |
| Weapons | +1 A.R. | +1 A.R. + 1 damage die | Hit and deal damage with weapon in relevant encounter |
| Armors | block +1 | Expert: reduce movement penalty; Master: reduce further | Receive hit where armor reduces damage |
| Shields | — | Access to additional shield maneuvers (type-dependent) | Use martial shield maneuvers successfully |
| Evasion | +1 D.R. | — | Successfully avoid relevant attacks |
| Specialization | +1 S.R. | +1 S.R. | Overcome tests appropriate to current rank |
| Resistances | +1 R.R. (specific type) | (see resistance subtypes) | Various — threat exposure |

### Resistance subtypes

| Subtype | Bonus |
| --- | --- |
| Elemental | +1 R.R. vs elemental effects |
| Poison | +1 R.R. vs poisons |
| Infection | +1 R.R. vs infections |
| Affliction | +1 R.R. vs afflictions; +1 per rank during meditation |
| Alteration | +1 R.R. vs alterations |
| Curses | +1 to detect or resist curses |

---

## Attrition & Fatigue

**Endurance formula:** 3 + TEN + Vigor rank (minimum 5 at creation)

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

---

## Rest & Recovery

**Authoritative values:** `attrition-fatigue.yaml`

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
| Unlock additional tasks during rest | Access expansion |
| Expand favorable condition criteria | Condition flexibility |
| Reduce Attrition recovery threshold for Full Rest | Efficiency boost |

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

---

## Backgrounds

Starting point for all characters: 4 specializations at Level 1 / Novice (3 from background + 1 universal: Vigor).

| Background | Major affinity | Starting specializations |
| --- | --- | --- |
| Martial Artist | Physical | 2 physical + 1 mental |
| Artisan | Arts & Crafts | 2 arts/crafts + 1 lore or social |
| Wanderer | Mental | 2 mental + 1 physical |
| Custodian | Lore | 2 lore + 1 social or mental |
| Noble | Social | 1 social + 2 any |

Vigor (universal): +1 TEN at creation. Stacks with species bonuses.

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

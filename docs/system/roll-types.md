# Roll Types

All checks use a `d10` base modified by characteristics, competencies, equipment, and circumstances.

## Summary Table

| Code | Name                  | Formula | Uses Competency |
|---|---|---|---|
| A.R. | Attack Roll           | 1d10 + Competency Level + Competency Rank + Associated Characteristic + Bonuses | Yes — weapon/object |
| D.R. | Defense Roll          | 1d10 + Applicable Evasion + Applicable Agility + Defense Bonuses | Yes — Evasion |
| I.R. | Impact Roll           | (Competency Rank × Weapon Damage) + (Associated Characteristic × Weapon Grade) | Yes — weapon rank |
| C.R. | Characteristic Roll   | 1d10 + Characteristic + Reference Level + Bonuses | No (unless specific rule) |
| R.R. | Resistance Roll       | varies by threat type (see below) | Yes — Resistances |
| S.R. | Specialization Roll   | 1d10 + Specialization Level + Rank + Associated Characteristic + Bonuses | Yes — specialization |
| P.R. | Personality Trait Roll| 2d10 | No |

## Detail

### A.R. — Attack Roll
Represents ability to land an effective strike with a weapon, maneuver, or object.

`A.R. = 1d10 + Competency Level + Competency Rank + Associated Characteristic + Additional Bonuses`

### D.R. — Defense Roll
Represents ability to avoid an incoming attack through reflexes, mobility, and armor.

`D.R. = 1d10 + Applicable Evasion + Applicable Agility + Defense Bonuses`

`Applicable Evasion = applicable Evasion level + applicable Evasion rank`

`Applicable Evasion` and `Applicable Agility` depend on the armor type of the resolved hit zone:

| Armor in resolved zone | Applicable Evasion | Applicable Agility |
|---|---|---|
| Unarmored | full Evasion | full `AGI` |
| Light armor | full Evasion | full `AGI` |
| Medium armor | half Evasion, rounded up, minimum 1 | half `AGI`, rounded up, minimum 1 |
| Heavy armor | 0 | 0 |

For `NPC -> PC`, hit location is rolled first. That resolved zone determines which armor type constrains Evasion and Agility in `D.R.`. If defense fails, the zone's block value still mitigates the impact.

### I.R. — Impact Roll
Determines real damage dealt after an attack surpasses defense.

`I.R. = (Competency Rank × Weapon Damage) + (Associated Characteristic × Weapon Grade)`

**Untrained weapon:** `I.R. = ((1 × Weapon Damage) + (Associated Characteristic × Grade)) / 2`

Weapon damage dice: d4, d6, d8, d10, d12

### C.R. — Characteristic Roll
Used when an action depends on a general aptitude, without specific training.

`C.R. = 1d10 + Characteristic + Reference Level + Additional Bonuses`

### R.R. — Resistance Roll
Represents ability to withstand harmful effects.

A Resistance Roll is not voluntary execution. It is the body, mind, or essence responding to a hostile effect. For that reason, it uses a single `d10` by default and does **not** use Evolutionary Advantage.

| Threat Type             | Formula |
|---|---|
| Poison / Infection      | 1d10 + TEN + Resistances + Bonuses |
| Affliction / Curses     | 1d10 + CMP + Resistances + Bonuses |
| Alterations             | 1d10 + Resilience + Resistances + Bonuses |

### S.R. — Specialization Roll
Reflects mastery in a specific skill (climbing, swimming, trap disarming, etc.).

`S.R. = 1d10 + Specialization Level + Competency Rank + Associated Characteristic + Bonuses`

### P.R. — Personality Trait Roll
Used when a personality trait decisively influences a situation (Narrator must accept justification).

`P.R. = 2d10`

No competencies involved. Purely narrative/psychological.

## Evolutionary Advantage

Applies to A.R., D.R., and S.R. Player chooses one approach before rolling:

| Option | Mechanic | Trade-off |
|---|---|---|
| Execution Advantage | Roll 2d10, take the **higher** | No learning opportunity |
| Learning Advantage  | Roll 2d10, take the **lower** for the action; higher die used for learning check | Risk of failure, potential competency progress |

**Learning condition:** if the higher die exceeds (lower die + the rank of the competency designated by that roll's progression rule), mark 1 progress point in that competency.

Evolutionary Advantage does not apply to R.R., C.R., or P.R. Resistances can still progress, but they do so through exposure, consequence, and survival after the effect resolves.

## Roll → Competency Relationship

| Roll | Competency used | Progression |
|---|---|---|
| A.R. | Weapon or object competency | Weapon/object competency, on successful attack resolution |
| D.R. | Evasion competency | Evasion on successful defense with Learning Advantage; armor type in resolved zone on failed defense where armor absorbs impact |
| I.R. | Weapon competency rank | None directly |
| C.R. | None (unless specific rule) | None |
| R.R. | Resistance matching threat type | Does not use Learning Advantage. Matching resistance progresses when the character fails or suffers a partial consequence from a relevant danger and survives |
| S.R. | Specialization competency | Used specialization, on successful roll |
| P.R. | None | None |

Shield value contributes generally to `D.R.` as equipment. Shield competency does not progress from generic `D.R.` alone; it progresses through explicit shield Techniques and shield-specific defensive actions.

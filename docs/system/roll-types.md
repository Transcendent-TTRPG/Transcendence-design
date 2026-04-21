# Roll Types

All checks use a `d10` base modified by characteristics, competencies, equipment, and circumstances.

## Summary Table

| Code | Name                  | Formula | Uses Competency |
|---|---|---|---|
| A.R. | Attack Roll           | 1d10 + Competency Level + Associated Characteristic | Yes — weapon/object |
| D.R. | Defense Roll          | 1d10 + Evasion Level + Applicable Agility + Defense Bonuses | Yes — Evasion |
| I.R. | Impact Roll           | (Competency Rank × Weapon Damage) + (Associated Characteristic × Weapon Grade) | Yes — weapon rank |
| C.R. | Characteristic Roll   | 1d10 + Characteristic + Reference Level + Bonuses | No (unless specific rule) |
| R.R. | Resistance Roll       | varies by threat type (see below) | Yes — Resistances |
| S.R. | Specialization Roll   | 1d10 + Specialization Level + Rank + Associated Characteristic + Bonuses | Yes — specialization |
| P.R. | Personality Trait Roll| 2d10 | No |

## Detail

### A.R. — Attack Roll
Represents ability to land an effective strike with a weapon, maneuver, or object.

`A.R. = 1d10 + Competency Level (weapon/object) + Associated Characteristic`

### D.R. — Defense Roll
Represents ability to avoid an incoming attack through reflexes, mobility, and armor.

`D.R. = 1d10 + Evasion Competency Level + Applicable Agility + Defense Bonuses`

`Applicable Agility` depends on the armor type of the resolved hit zone:

- Light armor zone -> full `AGI`
- Medium armor zone -> `floor(AGI / 2)`, minimum 1
- Heavy armor zone -> no `AGI`
- Unarmored zone -> full `AGI`

For `NPC -> PC`, hit location is rolled first. That resolved zone determines which armor type constrains Agility in `D.R.`. If defense fails, the zone's block value still mitigates the impact.

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

Applies to A.R., D.R., R.R., and S.R. Player chooses one approach before rolling:

| Option | Mechanic | Trade-off |
|---|---|---|
| Execution Advantage | Roll 2d10, take the **higher** | No learning opportunity |
| Learning Advantage  | Roll 2d10, take the **lower** for the action; higher die used for learning check | Risk of failure, potential competency progress |

**Learning condition:** if the higher die exceeds (lower die + the rank of the competency designated by that roll's progression rule), mark 1 progress point in that competency.

## Roll → Competency Relationship

| Roll | Competency used | Progression target with Learning Advantage |
|---|---|---|
| A.R. | Weapon or object competency | Weapon/object competency, on successful attack resolution |
| D.R. | Evasion competency | Evasion on successful defense; armor type in resolved zone on failed defense where armor absorbs impact |
| I.R. | Weapon competency rank | None directly |
| C.R. | None (unless specific rule) | None |
| R.R. | Resistance matching threat type | Matching resistance, on failed resistance where the effect is actually suffered |
| S.R. | Specialization competency | Used specialization, on successful roll |
| P.R. | None | None |

Shield value contributes generally to `D.R.` as equipment. Shield competency does not progress from generic `D.R.` alone; it progresses through explicit shield Techniques and shield-specific defensive actions.

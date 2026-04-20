# Difficulty Thresholds

**Authority:** `data/system/difficulty-thresholds.yaml`

Five universal difficulty tiers apply to every roll-based system in Transcendence — Specialization Rolls, Characteristic Rolls, Resistance Rolls, fabrication, afflictions, and any other system that requires beating a fixed number. The tiers are not system-specific. The same table is always the same table.

---

## Formula

```text
Threshold = Base + NR
```

**Base** is fixed by the chosen difficulty tier.

**NR** (Nivel de Referencia) is the Reference Level of the challenge:

- When the challenge comes from a creature or entity: NR = that creature's Nivel de Referencia
- When the challenge is environmental: NR = Narrator-assigned equivalent for the condition's intensity
- When the challenge is the intrinsic complexity of a task: NR = Narrator-assigned or system-assigned equivalent

The Narrator declares the difficulty tier before the roll is made. The player knows the threshold before deciding whether to use Execution Advantage or Learning Advantage.

---

## Tiers

| Tier | Name (ES / EN) | Base | Formula | Context |
| --- | --- | --- | --- | --- |
| 1 | Fundamentos / Fundamental | 5 | 5 + NR | Standard conditions, few disruptive factors |
| 2 | Desafiante / Challenging | 8 | 8 + NR | Minor challenges, partial disruptions, impredictable but manageable |
| 3 | Rigurosa / Rigorous | 11 | 11 + NR | Significant factors — active storm, difficult terrain, real technical complexity |
| 4 | Exigente / Demanding | 14 | 14 + NR | Near-disabling conditions or high intrinsic complexity; multiple simultaneous adverse factors |
| 5 | Extrema / Extreme | 17 | 17 + NR | Limit of what is executable; reserved for the most extreme moments in the game |

---

## Opposed Rolls vs. Fixed Threshold

These tiers apply to **fixed threshold** tests. When the challenge is directly another creature or character, both parties roll and results are compared — no fixed threshold is set. The NR difference between characters is already embedded in the roll formulas through level, rank, and characteristic.

Fixed threshold cases:
- No active agent is directly opposing (environmental resistance, task complexity)
- A system explicitly calls for a fixed threshold (fabrication, certain affliction triggers)
- The Narrator judges that an opposed roll is not narratively grounded

---

## Sources of NR

### Creature NR
When a creature's ability sets the difficulty without a direct opposed roll — such as detecting a Sigilo roll result rather than rolling Perception against it — the creature's NR contributes to the threshold.

### Environmental NR
The intensity of environmental conditions can be expressed as an NR equivalent. A mild forest path may have NR 0. A hurricane at sea may have NR 4. The Narrator assigns this.

This is the foundation of the **dificultad del entorno** system. Environmental conditions are classified by tier, and the NR equivalent reflects how demanding those conditions are relative to the characters present.

### Task NR
For knowledge rolls, crafting, and investigative systems, the task itself has inherent complexity. An ancient text of standard scholarly depth might be Challenging at NR 1. A corrupted cipher in a dead language might be Extreme at NR 3. The system or the Narrator sets the NR.

---

## Relationship to Competency Ranks

The minimum difficulty appropriate for each competency rank establishes which tier a roll must reach before it can generate meaningful progress:

| Rank | Minimum meaningful difficulty |
| --- | --- |
| Untrained | Any |
| Novice | Any |
| Adept | Fundamental (5 + NR) |
| Expert | Challenging (8 + NR) |
| Master | Rigorous (11 + NR) |
| Consummate | Demanding (14 + NR) |
| Transcendent | Extreme (17 + NR) |

A Transcendent-level character is not challenged by a Fundamental test. This does not prevent untrained characters from rolling — it means the test does not represent a meaningful challenge at that rank. The Narrator uses this table to calibrate when progress is earned.

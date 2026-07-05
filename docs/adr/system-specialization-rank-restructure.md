# ADR — Specialization Rank Restructure

**Status:** Adopted (historical — documents the 2025 rank restructure rationale; current structure is the adopted system)
**Scope:** All competency types — specializations, weapons, armors, shields, evasion, resistances
**Related:** `competencies.yaml`, `specializations.yaml`, `docs/system/mechanics-overview.md`

---

## Historical Problem (resolved)

The following problem no longer exists — it is documented here to explain why the restructure was adopted.

Under the original rank structure (3 levels per rank, 4 ranks: Novice 1–3, Adept 4–6, Expert 7–9, Master 10+), real playtesting across approximately 20 sessions showed that no character ever advanced past Novice rank.

The root causes:

- Reaching Novice required 30 progress points (15 with major affinity), which demanded 6+ uses of the learning advantage in a single domain before reaching the first rank threshold
- Characters in normal play spread their rolls across many domains, making it rare to accumulate 30 points in any single specialization
- The 4-rank ceiling also left no room for long-term aspiration beyond Master

The result was a flat, stagnant competency experience where progression was mathematically possible but practically invisible at the table.

---

## Decision

Two simultaneous changes were adopted:

### 1. Reduce levels per rank from 3 to 2

Each rank now spans 2 levels instead of 3. Rank thresholds fall at odd levels:

| Rank | Name (ES / EN) | Level range | Threshold level |
| --- | --- | --- | --- |
| 0 | No entrenado / Untrained | 0 | — |
| 1 | Novato / Novice | 1–2 | 1 |
| 2 | Adepto / Adept | 3–4 | 3 |
| 3 | Experto / Expert | 5–6 | 5 |
| 4 | Maestro / Master | 7–8 | 7 |
| 5 | Consumado / Consummate | 9–10 | 9 |
| 6 | Trascendente / Transcendent | 11+ | 11 |

Reaching Novice from Untrained now requires 10 progress points (5 with major affinity) — a single learning-advantage use with major affinity, or 2 uses without.

### 2. Extend the ceiling to 6 ranks

Two new ranks were added beyond Master: Consummate (rank 5) and Transcendent (rank 6).

This serves two purposes:
- Provides long-term character aspiration that the old 4-rank structure lacked
- Gives the setting a way to represent true legendary mastery without inflating Novice-level numbers

---

## Major Affinity

Major affinity (5 pts per level vs. 10 pts default) was introduced alongside the restructure.

Major affinity is determined by background:
- Characters have major affinity in the specialization categories associated with their background
- A character can develop any specialization regardless of affinity, but affinity halves the progress cost

Together, the rank restructure and major affinity ensure that characters with relevant backgrounds reach Novice in 1–2 uses of learning advantage, while characters without affinity still reach Novice after 2 uses — both meaningful within normal play tempo.

---

## Breadth vs. Depth Tension

Synapsis (+1 to the associated characteristic) triggers once per rank reached, per specialization.

This creates a deliberate strategic tension:
- **Breadth:** reaching Rank 1 in many specializations generates Synapsis points quickly across multiple characteristics
- **Depth:** reaching Rank 6 in one specialization generates a high S.R. bonus and unlocks advanced Techniques, but at high opportunity cost

Neither path is strictly better. The choice reflects the character's identity and intended role.

---

## Untrained Use

Any character can roll any specialization even without training. The untrained formula is:

```
1d10 + associated characteristic (no level or rank bonus)
```

High difficulty thresholds naturally gatekeep what untrained characters can achieve. Training exists not to allow the attempt, but to make meaningful outcomes reachable.

---

## What Did Not Change

- Progress points per level: 10 default / 5 with major affinity
- Method: learning advantage (lower die result for progress)
- Narrator validates narrative fit before allowing a domain roll to generate progress
- The S.R. formula: `1d10 + level + rank + characteristic + bonuses`

# System Reference Index

This folder contains the mechanical source of truth for the Transcendence TTRPG system.
All content here is extracted from and must remain consistent with `transcendence-publications`.

## Files

| File | Contents |
| --- | --- |
| [characteristics.md](characteristics.md) | All 9 characteristics, groups, abbreviations, derived attributes, Synapsis rule |
| [roll-types.md](roll-types.md) | All 7 roll types with formulas, Evolutionary Advantage, roll→competency map |
| [competencies.md](competencies.md) | Ranks, progression requirements, all competency types and bonuses |
| [specializations.md](specializations.md) | Specialization categories with associated characteristics |
| [backgrounds.md](backgrounds.md) | All 5 backgrounds with major affinity and starting specialization rules |
| [general-rules.md](general-rules.md) | Core rules, dice, Adventure Cycle phases, Conflict flow |
| [attrition-fatigue.md](attrition-fatigue.md) | Desgaste, Aguante y Fatiga — attrition model, Endurance formula, Fatigue thresholds, action cost scale |
| [atb-reference.md](atb-reference.md) | ATB quick reference — timeline model, rhythm cost, reactions, subsystem tracks, encounter layers, table prompts |
| [mechanics-overview.md](mechanics-overview.md) | Horizontal view of all systems organized by ability design surfaces — use this when designing abilities |

## Structured Data (`/data/system/`)

| File | Use |
| --- | --- |
| `characteristics.yaml` | Characteristic definitions, derived attribute formulas |
| `roll-types.yaml` | Roll formulas, Evolutionary Advantage, roll→competency map |
| `competencies.yaml` | Ranks, progression costs, competency type bonuses |
| `backgrounds.yaml` | Background definitions with affinity and specialization rules |
| `attrition-fatigue.yaml` | Endurance formula, Fatigue thresholds, Attrition cost scale, Vigor definition, condition interaction model |

## Key Numbers

| Concept | Value |
| --- | --- |
| Base die | d10 |
| Characteristics start at | 0 |
| Levels per competency rank | 3 |
| Progress points (affinity) | 5 |
| Progress points (default) | 10 |
| Starting specializations | 4 at Level 1 / Rank 1 (3 from background + 1 universal: Vigor) |
| Universal starting specialization | Vigor → +1 Tenacity (stacks with species bonuses) |
| Endurance base | 3 (body + mind + composure) |
| Endurance formula | 3 + Tenacity + Vigor Rank |
| Starting Endurance (min) | 5 (Tenacity 1 + Vigor Rank 1) |
| Fatigue 1 threshold | Attrition ≥ Endurance |
| Fatigue 2 threshold | Attrition ≥ 2 × Endurance |
| Fatigue 3 threshold | Attrition ≥ 3 × Endurance |
| Action cost scale | 0 (trivial) / 1 (standard) / 2 (high demand) / 3 (extreme) |
| Personality trait factors | 5 (Big Five) |
| Roll types | 7 (AR, DR, IR, CR, RR, SR, PR) |
| Competency types | 6 (Weapons, Armors, Shields, Evasion, Specialization, Resistances) |

## Source Documents

Extracted from:

- `transcendence-publications/core-books/transcendence-corebook/03-character-creation/`
- `transcendence-publications/core-books/transcendence-corebook/09-core-rules/`

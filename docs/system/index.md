# System Reference Index

This folder contains the mechanical source of truth for the Transcendence TTRPG system.
All content here is extracted from and must remain consistent with `transcendence-publications`.

## Files

| File | Contents |
| --- | --- |
| [characteristics.md](characteristics.md) | All 9 characteristics, groups, abbreviations, derived attributes, Synapsis rule |
| [roll-types.md](roll-types.md) | All 7 roll types with formulas, Evolutionary Advantage, roll→competency map |
| [competencies.md](competencies.md) | Ranks, progression requirements, all competency types and bonuses |
| [difficulty-thresholds.md](difficulty-thresholds.md) | 5 universal difficulty tiers (Fundamentos–Extrema), base values, formula (Base + NR), opposed roll vs. fixed threshold distinction |
| [ailments.md](ailments.md) | Agravios framework: universal severity model, duration doctrine, and initial Alteration entries |
| [environmental-conditions.md](environmental-conditions.md) | Two condition types (natural/extranatural), 6 elements + combinations, 5 severity levels with examples, Hinder/Restrict/Accelerate model, Narrator NR guidance |
| [limbo-manifestations.md](limbo-manifestations.md) | Three Limbo manifestation types (ambient flow / vestige / link), detection methods, relationships between types, open design questions (D-09–D-11) |
| [specializations.md](specializations.md) | Full specialization framework: definition, four design clauses, structural relationship (attribute→specialization→technique), S.R. formula, starting specs, distribution notes per attribute |
| [techniques.md](techniques.md) | Technique taxonomy: canonical fields, cost model, timing, duration, resistance, scaling, and authoring rules |
| [technique-interaction-framework.md](technique-interaction-framework.md) | Cross-system doctrine for Techniques — what systems they should touch, how they should touch them, and how to avoid arbitrary bonus-stacking |
| [technique-origins.md](technique-origins.md) | World-grounding framework for Techniques — origin fronts (Species, Doctrine, Region), transmission logic, access levels, and design checklist |
| [weapon-technique-profiles.md](weapon-technique-profiles.md) | Combat profile layer between weapon competency and concrete Techniques — shared by weapon families and natural attack forms |
| [natural-attack-forms.md](natural-attack-forms.md) | Inverse mapping for natural combat — attack forms, contact logic, and compatible Weapon Technique Profiles |
| [competency-technique-domains.md](competency-technique-domains.md) | Technique domain matrix by competency type — primary, secondary, and limited effect families |
| [specialization-technique-domains.md](specialization-technique-domains.md) | Technique identity by individual specialization — fantasy core, primary tags, targets, timing, and design limits |
| [backgrounds.md](backgrounds.md) | All 5 backgrounds with major affinity and starting specialization rules |
| [general-rules.md](general-rules.md) | Core rules, dice, Adventure Cycle phases, Conflict flow |
| [attrition-fatigue.md](attrition-fatigue.md) | Desgaste, Aguante y Fatiga — attrition model, Endurance formula, Fatigue thresholds, action cost scale |
| [atb-reference.md](atb-reference.md) | ATB quick reference — timeline model, rhythm cost, reactions, subsystem tracks, encounter layers, table prompts |
| [equipment-overview.md](equipment-overview.md) | Equipment structure: armor slots and types, zone block formula, shield role, weapon assignment, NPC→PC hit table |
| [mechanics-overview.md](mechanics-overview.md) | Horizontal view of all systems organized by ability design surfaces — use this when designing abilities |

## Structured Data (`/data/system/`)

| File | Use |
| --- | --- |
| `characteristics.yaml` | Characteristic definitions, derived attribute formulas |
| `roll-types.yaml` | Roll formulas, Evolutionary Advantage, roll→competency map |
| `competencies.yaml` | Ranks, progression costs, competency type bonuses |
| `backgrounds.yaml` | Background definitions with affinity and specialization rules |
| `attrition-fatigue.yaml` | Endurance formula, Fatigue thresholds, Attrition cost scale, Tenacity-specialization interaction model |
| `atb-combat.yaml` | Rhythm scale (0/3/5/7/9), base action families with rhythm and Attrition costs, initial position formula and situational modifiers, competency-rhythm interaction model |
| `equipment.yaml` | Equipment slots, armor types, zone block formula, shield formulas, hit-location table, slot effects |
| `difficulty-thresholds.yaml` | 5 difficulty tiers with base values and formula — applies to all roll-based systems |
| `ailments.yaml` | Agravios taxonomy, universal severity model, and initial Alteration entries |
| `environmental-conditions.yaml` | Two condition types, 6 elements and combinations, 5 severity levels with NR guidance |
| `limbo-manifestations.yaml` | El Limbo definition, three manifestation types with characteristics and detection, inter-manifestation relationships |
| `techniques.yaml` | Technique taxonomy, template, cost fields, duration models, and competency-domain matrix |
| `weapon-technique-profiles.yaml` | Weapon-profile authoring layer — combat families, compatible origins, natural weapon compatibility, and ATB timing identity |
| `natural-attack-forms.yaml` | Natural-form mapping layer — bodily contact logic, combat role, and profile compatibility for natural attacks |
| `specialization-technique-domains.yaml` | Technique identity space by specialization — primary/secondary tags, target profile, timing, and limits |

## Key Numbers

| Concept | Value |
| --- | --- |
| Base die | d10 |
| Characteristics start at | 0 |
| Levels per competency rank | 2 |
| Difficulty tier 1 — Fundamentos | 5 + NR |
| Difficulty tier 2 — Desafiante | 8 + NR |
| Difficulty tier 3 — Rigurosa | 11 + NR |
| Difficulty tier 4 — Exigente | 14 + NR |
| Difficulty tier 5 — Extrema | 17 + NR |
| Progress points (affinity) | 5 |
| Progress points (default) | 10 |
| Starting specializations | 4 at Level 1 / Rank 1 (3 from background + 1 universal Tenacity choice) |
| Universal starting specialization | one Tenacity specialization of choice → +1 Tenacity (stacks with species bonuses) |
| Endurance base | 3 (body + mind + composure) |
| Endurance formula | 3 + (Tenacity × 2) |
| Starting Endurance (min) | 7 (after initial Tenacity Synapsis) |
| Fatigue 1 threshold | Attrition ≥ Endurance |
| Fatigue 2 threshold | Attrition ≥ 2 × Endurance |
| Fatigue 3 threshold | Attrition ≥ 3 × Endurance |
| Action cost scale | 0 (trivial) / 1 (standard) / 2 (high demand) / 3 (extreme) |
| Personality trait factors | 5 (Big Five) |
| Roll types | 7 (AR, DR, IR, CR, RR, SR, PR) |
| Competency types | 6 (Weapons, Armors, Shields, Evasion, Specialization, Resistances) |
| Armor slots | 5 (Helmet, Chestpiece, Bracers, Trousers, Boots) |

## Source Documents

Extracted from:

- `transcendence-publications/core-books/transcendence-corebook/03-character-creation/`
- `transcendence-publications/core-books/transcendence-corebook/09-core-rules/`

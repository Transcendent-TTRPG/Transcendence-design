# Competencies

Competencies represent degree of mastery, training, or adaptation in a specific field. They modify rolls and allow progression when the character faces pressure that is meaningful for their current rank.

Characteristics express potential. Competencies express how much that potential has been trained and refined.

## Ranks

A new rank is gained every 2 competency levels.

| Rank        | Level Range | Notes |
|---|---|---|
| Untrained   | 0           | Starting level for most competencies |
| Novice      | 1–2         | Starting trained competencies begin at level 1 |
| Adept       | 3–4         | |
| Expert      | 5–6         | |
| Master      | 7–8         | |
| Consummate  | 9–10        | |
| Transcendent| 11+         | |

## Starting Weapon Competencies

Every character begins with **two distinct weapon competencies at level 1 / Novice**, regardless of species, background, or the number of natural weapons. Choose from the character's anatomically available natural weapons and manufactured weapon types, justified by prior experience.

The two choices cannot be combined to start one competency at level 2. Weapon competencies not chosen begin at level 0. An untrained natural weapon remains anatomically available and follows the untrained weapon rules; anatomy does not grant additional trained competencies.

This allocation is separate from starting specializations. Weapon competencies do not grant Synapsis or equipment. Armor, shield, and Evasion competencies are separate types and do not consume these two weapon choices.

Example: a Panin can start with Bite 1 and one manufactured weapon competency 1, or with two distinct manufactured weapon competencies 1 and Bite 0. A character with two natural weapons can choose both at level 1, choose one natural and one manufactured weapon competency, or choose two manufactured weapon competencies. None of these choices grants carried weapons.

Authority: `data/system/competencies.yaml` → `character_creation.starting_weapon_competencies`; decision: `docs/adr/system-initial-weapon-competencies.md`.

## Progression Requirements

| Competency case | Progress points to level up |
|---|---|
| Specialization with major affinity from background | 5 points |
| All other competencies | 10 points |

Not all competencies progress the same way.

| Competency type | Progress method |
|---|---|
| Weapons, Evasion, Specializations | Learning Advantage |
| Armors | Failed D.R. where armor absorbs impact |
| Shields | Successful shield Techniques, interceptions, or dedicated shield maneuvers |
| Resistances | Exposure, consequence, and survival |

Resistances do not use major affinity by base rule, unless a specific rule says otherwise.

### Appropriate test difficulty by rank

| Rank        | Minimum test difficulty |
|---|---|
| Novice      | Any |
| Adept       | Fundamental or higher |
| Expert      | Challenging or higher |
| Master      | Rigorous or higher |
| Consummate  | Demanding or higher |
| Transcendent| Extreme |

## Competency Types

### Weapons
Mastery with a specific weapon type.

- Each **level**: +1 to A.R.
- Each **rank**: +1 to A.R. + one additional die to I.R.
- Weapon-rooted Techniques should normally pass through shared **Weapon Technique Profiles** rather than requiring a separate Technique tree for every individual item
- Progression: successful `A.R.` with Learning Advantage, when the attack hits and deals damage using that weapon or object competency.

### Armors
Efficient use of armor by type.

- Split into **Light Armor**, **Medium Armor**, and **Heavy Armor**
- Each **level**: +1 to zone block when that armor type is present in the resolved hit zone
- Armor competency does **not** gain a passive per-rank block bonus; block already stacks with base category, material, and grade
- Progression: failed `D.R.`, when the hit resolves through an armored zone and that armor actually reduces impact

### Shields
Technical mastery of shield use.

- Each **rank**: access to additional shield maneuvers (type-dependent)
- Reaching **Master**: reduce the movement penalty imposed by the equipped shield by `grade` (minimum 0)
- Progression: successfully use shield Techniques, interceptions, or dedicated shield maneuvers

### Evasion
Anticipating and avoiding attacks.

- Each **level**: +1 to D.R.
- Each **rank**: +1 to D.R.
- Progression: successful `D.R.` with Learning Advantage through mobility and reflexes

### Specialization
Technical mastery in a specific skill.

- Each **level**: +1 to S.R.
- Each **rank**: +1 to S.R.
- Each new **rank** also grants Synapsis: +1 to the associated characteristic.
- Progression: successful `S.R.` with Learning Advantage in tests appropriate to current rank.

### Resistances
Withstanding specific harmful conditions and effects. Resistances do not reduce Impact, elemental damage, or wounds. Damage is resolved through Impact versus Block and the wound or HP rules.

| Resistance type   | Bonus per level |
|---|---|
| Poison            | +1 to R.R. against poisons |
| Infection         | +1 to R.R. against infections |
| Affliction        | +1 to R.R. against afflictions; +1 to Affliction R.R. per rank during meditation |
| Alteration        | +1 to R.R. against alterations |
| Curses            | +1 to detect or resist curses |

Resistances are added to the corresponding `R.R.`, but they do not use Evolutionary Advantage.

These are the **Ailment-family Resistances**.

They are not the same thing as:

- elemental traits such as heat, cold, fire, or lightning resistance/vulnerability
- species wording such as "venom tolerance" or "Abzu mental hardening"

Those concepts may explain the fiction of a Technique, species trait, or
environmental interaction, but the competency layer still resolves through the
canonical Resistance families above unless a future system explicitly adds a
new subtype.

## Learning Through Exposure

Resistances increase when the character is exposed to a real danger, suffers it, and survives its consequences.

A Resistance can gain progress if all of the following conditions are met:

- the character makes an `R.R.` against the corresponding danger
- the danger is relevant for the character's current rank
- the character fails the `R.R.` or suffers a partial consequence from the effect
- the character survives the exposure

If these conditions are met, the character marks `1` progress point in the corresponding Resistance.

Completely resisting a danger does not generate progress by base rule. Resistance improves when the character is forced to adapt, not when they avoid all consequence.

The Narrator can deny progress if the exposure is trivial, controlled without real risk, repeated artificially, or insufficient to challenge the character's current rank.

Elemental identity is handled by traits on creatures, materials, objects, or specific effects rather than by player resistance competencies.

| Trait | Damage effect |
|---|---|
| Minor Resistance | Takes 50% damage from that elemental origin |
| Major Resistance | Takes 0 damage from that elemental origin |
| Minor Vulnerability | Takes 150% damage from that elemental origin |
| Major Vulnerability | Takes 200% damage from that elemental origin |

## Progression Map by Roll

| Roll or trigger | Progress event | Competency that progresses |
|---|---|---|
| `A.R.` with Learning Advantage | success | weapon or object competency used |
| `D.R.` with Learning Advantage | success | evasion |
| Failed `D.R.` | armor absorbs impact | armor competency of the resolved armored zone |
| `S.R.` with Learning Advantage | success | specialization used |
| `R.R.` | exposure | matching resistance, if the effect is suffered or partially suffered and the character survives |
| shield Technique / shield action | success | shield competency |

`I.R.`, `C.R.`, and `P.R.` do not directly generate competency progress under the current model.

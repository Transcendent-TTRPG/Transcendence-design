# Competency Technique Domains

**Related docs:** `docs/system/competencies.md`, `docs/system/techniques.md`, `docs/system/specializations.md`, `docs/system/equipment-overview.md`

---

## Purpose

This document defines the main Technique domains that each competency type can generate.

The goal is not to list Techniques yet, but to establish:

- what each competency mainly produces
- what it may produce secondarily
- what it should rarely or never produce

This prevents drift when the actual Technique catalog is written.

---

## Reading Rule

Each competency has:

- **primary tags**: the main effect tags its Techniques should generate most often
- **secondary tags**: valid but less frequent effect tags
- **outer limits**: effect tags or result families that should be rare, tightly justified, or usually belong elsewhere

This document should prefer the controlled vocabulary defined in [techniques.md](/Users/juangomez/Transcendence-workspace/Transcendence-design/docs/system/techniques.md).

When a nuance cannot be expressed cleanly with canonical tags, keep it in prose here instead of inventing a weak tag.

---

## Weapons

### Primary tags

- attack
- setup
- pressure

### Secondary tags

- mobility
- disruption
- precision

### Outer limits

- strong recovery effects
- broad party support
- persistent non-physical control without a clear fiction bridge

Weapons should mainly create Techniques that open, punish, pressure, or capitalize on timing windows.

---

## Armors

### Primary tags

- defense
- mitigation
- stability

### Secondary tags

- anti_displacement
- survival_window
- control

### Outer limits

- attack
- high mobility
- abstract control detached from bodily protection

Armor Techniques should feel like trained use of mass, plate, padding, and impact survival — not generic powers.

---

## Shields

### Primary tags

- defense
- interception
- control

### Secondary tags

- disruption
- anti_displacement
- setup

### Outer limits

- attack
- support
- broad utility unrelated to protection or interception

Shield Techniques should mainly answer the question: how does the shield alter contact, lanes, and incoming force?

---

## Evasion

### Primary tags

- mobility
- defense
- counter_positioning

### Secondary tags

- setup
- disruption
- survival_window

### Outer limits

- hard mitigation
- attack
- support effects with no positional logic

Evasion Techniques should feel like timing, angle, spacing, and not-being-there.

---

## Specializations

Specializations are the broadest origin pool. Their domains vary by specialization, but some structure still applies.

### Primary tags

- setup
- control
- recovery
- disruption

### Secondary tags

- utility
- attack
- defense
- mobility
- support

### Outer limits

- pressure
- effects with no connection to the domain's trained practice

Specialization-rooted Techniques should encode a domain's advanced application, not merely make raw use stronger.

---

## Resistances

### Primary tags

- defense
- recovery
- condition_reduction
- survival_window

### Secondary tags

- mitigation
- control

### Outer limits

- attack without a survivability bridge
- wide-area support unless strongly justified

Resistance-rooted Techniques should feel like trained survival expression under a specific kind of threat.

Resistances are a special case:

- they are not a standalone Technique school
- they do not produce pure Techniques by themselves
- they should mainly appear as a second origin layered onto another chosen domain

That means the normal output is:

- `Armor + fire-origin Vulnerability/Resistance trait`
- `Tolerance + Poison Resistance`
- `Resonance + Affliction Resistance`

and not:

- a standalone fire-resistance Technique with no other trained origin
- `Poison Resistance` alone

Pure Resistance Techniques are prohibited.

---

## Specialization Domain Notes

Because specializations are diverse, they need an extra filter.

### Physical specializations

Often produce:

- mobility
- setup
- attack
- anti_displacement

### Mental specializations

Often produce:

- utility
- counter_read
- disruption
- setup

### Social specializations

Often produce:

- control
- pressure
- disruption
- support

### Arts and Crafts

Often produce:

- utility
- setup
- recovery
- control
- mitigation

### Knowledge

Often produce:

- setup
- utility
- counter_read
- disruption

---

## Tag Matrix

| Competency | Primary tags | Secondary tags | Rare / Limited |
| --- | --- | --- | --- |
| Weapons | attack, setup, pressure | mobility, disruption, precision | recovery, support |
| Armors | defense, mitigation, stability | anti_displacement, survival_window, control | attack, mobility |
| Shields | defense, interception, control | disruption, anti_displacement, setup | attack, support |
| Evasion | mobility, defense, counter_positioning | setup, disruption, survival_window | mitigation, attack |
| Specializations | setup, control, recovery, disruption | utility, attack, defense, mobility, support | pressure |
| Resistances | defense, recovery, condition_reduction, survival_window | mitigation, control | attack, support |

---

## Authoring Rule

When a proposed Technique feels wrong, test it here first.

Questions:

1. Does this effect belong to the competency's primary or secondary tags?
2. If it belongs to an outer limit zone, what fiction justifies the exception?
3. Would another competency produce this more naturally?
4. Is this Technique expressing the competency, or bypassing it?
5. If Resistance is involved, what is the other origin carrying the character's agency?

If the answer points elsewhere, the Technique origin is wrong.

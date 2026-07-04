# Environmental Conditions

**Authority:** `data/system/environmental-conditions.yaml`

Environmental conditions give the Narrator a framework for assigning difficulty when the challenge comes from pressure external to the actor — terrain, weather, atmospheric pressure, a dominant hostile presence, or the threat level of the overall situation. The severity level determines the difficulty tier and NR. Beyond that, the Narrator has two tools (Restrict and Accelerate) to apply when the narrative warrants it — neither is automatic.

---

## Two types

**Natural** conditions follow the physical laws of the world. They can be extreme — a hurricane, a volcanic field, a cave-in — but they operate within coherent rules.

**Extranatural** conditions are phenomena in the perceptible world that involve Limbo energy. Tauma does not generate phenomena from nothing: it transforms, modifies, amplifies what already exists in the material world. What distinguishes an extranatural condition from a natural one is not intensity or element combination, but origin — any reaction that does not follow the natural logic of the world, produced by the imperceptible dimension filtering into the perceptible one. Observable markers (physically contradictory states, Light and Darkness simultaneously active) are signs of Limbo presence, not its definition. Not every extranatural condition produces visible contradictions; it may manifest as amplification or transformation of something natural. Normal environmental adaptation may not apply to extranatural conditions — open design question (D-08).

Hostile presence may belong to either group. Mortal creatures and material predators create natural pressure. Anomalous entities, primordial presences, or visible manifestations made of Limbo energy create extranatural pressure.

---

Environmental conditions can be described with elemental language in setting or lore documents, but that taxonomy is not part of the mechanical definition of this system. This document only defines how the Narrator classifies pressure, sets thresholds, and distinguishes natural from extranatural origin.

---

## Severity levels

Each severity level maps directly to one difficulty tier. The Narrator sets the environmental NR within that tier based on the specific intensity of the condition.

| Severity | Difficulty tier | Base | NR range | Type |
| --- | --- | --- | --- | --- |
| Mild | Fundamental | 5 | 1 | Natural |
| Moderate | Challenging | 8 | 1–3 | Natural |
| Severe | Rigorous | 11 | 3–6 | Natural or extranatural |
| Disastrous | Demanding | 14 | 6–9 | Natural or extranatural |
| Extreme | Extreme | 17 | 9–12 | Natural or extranatural |

---

### Mild (Fundamental — 5 + NR)

Few disruptive factors. Manageable with basic attention.

**Natural:** light rain with gentle wind; irregular but familiar terrain; reduced visibility (light fog); uncomfortable but tolerable temperature; ambient noise (nearby river, wind through trees).

**Effect model:** None — threshold (5 + NR) expresses the difficulty directly.

---

### Moderate (Challenging — 8 + NR)

Active disruption. Requires adaptation. Affects concentration, coordination, or communication.

**Natural:** moderate storm with reduced visibility; very irregular or marshy terrain; intense but not extreme heat or cold; noise that prevents verbal coordination; partial darkness (insufficient torches, covered moon).

**Effect model:** Narrator may Restrict if the context justifies it.

---

### Severe (Rigorous — 11 + NR)

Significant factors. Actions demand greater effort. Some tactical options are actively limited.

**Natural:** strong storm with wind that prevents light projectiles and impedes movement; very rough terrain with fall risk; sustained extreme temperature; near-total darkness with minimal visibility; combat in water or on unstable surface.

**Effect model:** Narrator may Restrict.

---

### Disastrous (Demanding — 14 + NR)

Near-disabling conditions. May be natural phenomena at their extreme, or the first manifestation of extranatural influence. At this level the distinction between natural and extranatural begins to matter mechanically.

**Natural:** active earthquake with collapses; maximum-intensity hurricane; active wildfire with unpredictable direction; maritime storm with waves overwhelming structures.

**Extranatural (early):** two elements in active conflict (extreme heat with simultaneous snow); actively shifting terrain; darkness with a visible light source that produces no illumination; temperature varying several degrees in seconds.

**Effect model:** Narrator may Restrict and/or Accelerate.

---

### Extreme (Extreme — 17 + NR)

Limit of what is survivable or executable. Extranatural conditions are common at this range. Three or more elements in active conflict, or phenomena the environment cannot sustain under natural logic.

**Natural:** maritime storm with simultaneous boarding and structure collapse; earthquake combined with nearby volcanic eruption.

**Extranatural:** complete elemental storm (all elements in simultaneous active conflict); light and darkness with simultaneous physical effects; environment in active dimensional collapse (the Limbo filtering directly into the physical plane); unstable physical rules — irregular gravity, perceptible time distortion.

**Effect model:** Narrator may Accelerate — probable at this range; may generate passive Attrition.

---

## Effect model

The environmental NR expresses difficulty through the threshold (Base + NR) — that is the only fixed mechanical rule. Beyond the threshold, the Narrator has two narrative tools that can be applied when the situation justifies it. There is no automatic trigger; the Narrator decides when and whether to use them.

| Tool | What it does |
| --- | --- |
| **Restrict** (Limitar) | Eliminates available actions — not harder, unavailable |
| **Accelerate** (Acelerar) | Adds +1 Attrition cost to all non-free actions |

Severity is a guide: Extreme conditions make it likely the Narrator uses both; Mild conditions make it unlikely they use either. Not every scenario at a given severity requires either tool.

Full model: `data/system/attrition-fatigue.yaml (conditions_and_environment)`

---

## Narrator guidance for NR assignment

The environmental NR reflects how much a specific instance of a condition presses beyond the baseline for its severity level.

| Environmental NR | Meaning |
| --- | --- |
| 1 | Condition at its minimum expression for the severity level |
| 3 | Notable condition within its level; some compound factors |
| 5 | Intense condition; multiple simultaneous factors or extended duration |
| 7 | Condition at its peak, or first confirmed extranatural marker |
| 9 | Clear extranatural influence; reserved for Extreme severity |

### When multiple sources of difficulty combine

Identify the dominant source — the one that defines the tier. Secondary sources (a second environmental factor, a dominant hostile presence, an extranatural marker) can add NR up to a maximum of +2 on top of the dominant tier. Do not stack NR from more than two sources.

Example: a Disastrous storm (14 + NR) combined with a secondary severe terrain factor → 14 + 2 = 16. Not 14 + 4.

### When a specific system already defines the difficulty

If another system provides a defined DC or mechanic for the action, use that. Environmental conditions are the fallback — the Narrator's tool for situations that have no rule of their own. The specific rule always takes precedence.

---

## Specializations and environmental conditions

The following specializations interact directly with environmental conditions:

| Specialization | Condition type | Context |
| --- | --- | --- |
| Aclimatación (Tenacity) | Natural — environmental | Adapting to hostile or extreme environments |
| Tolerancia (Tenacity) | Natural — physiological | Enduring pain and physical strain from conditions |
| Equilibrio (Agility) | Natural — terrain | Reactive response to involuntary balance loss |
| Supervivencia (Cunning) | Natural — field | Practical decision-making in hostile environments |

**Open design question (D-08):** Whether Aclimatación and other natural specializations apply equally to extranatural conditions. A combined elemental storm is not simply "extreme cold" — it may require different capacities (Instinct, Resonance, Thaumaturgy). Cannot be resolved without designing the full Limbo manifestation system.

Provisional rule: Aclimatación applies to Disastrous-level conditions with an extranatural component. Its effectiveness in Extreme conditions of taumatic origin is undefined.

# Environmental Conditions

**Authority:** `data/system/environmental-conditions.yaml`

Environmental conditions set the NR the Narrator assigns to fixed-threshold tests when the challenge comes from the world itself — terrain, weather, atmospheric pressure — rather than from an active opponent. They do not replace the Attrition system. They contribute pressure that accelerates Fatigue and constrains action.

---

## Two types

**Natural** conditions follow the physical laws of the world. They can be extreme — a hurricane, a volcanic field, a cave-in — but they operate within coherent rules.

**Extranatural** conditions do not. They occur when Kaodis — deity of the Void, born of Lampsi (Light) and Nytha (Darkness) — touches the environment. Their defining marker is not the combination of elements but the **simultaneous coexistence of contradictory states** in the same space: fire and ice at the same point, not fire and water producing steam (which is natural). Light and Darkness both active with distinct effects is the primary marker of Kaodis's direct presence. Normal environmental adaptation may not apply to extranatural conditions — this is an open design question (D-08).

---

## Elements

Six base elements produce all environmental conditions, natural and extranatural.

| Element | Natural manifestations |
| --- | --- |
| **Water** | Rain, flood, snow, ice, rough sea, dense fog |
| **Wind** | Strong wind, storm, tornado, hurricane, high-altitude currents |
| **Fire** | Extreme heat, active wildfire, volcanic field, burning structures |
| **Earth** | Earthquake, avalanche, cave-in, very rough terrain, quicksand |
| **Light** | Extreme solar glare on snow or water; continuous lightning breaking night vision |
| **Darkness** | Moonless night, unlighted cave, impenetrable fog, heavy smoke |

**Natural combinations** correspond to the minor deity pantheon — physically possible phenomena the elemental religion recognizes by name:

| Elements | Natural result | Minor deity |
| --- | --- | --- |
| Water + Wind | Storm, hurricane, fog | Nefos |
| Fire + Wind | Lightning, electrical storm | Brontios |
| Fire + Water | Steam, geyser, volcano meeting sea | Atmos |
| Fire + Earth | Eruption, lava field, ash | Pilysis / Fakos |
| Earth + Water | Flood, mud, marshy terrain | Philos |
| Earth + Darkness | Deep cave, light-absorbing cracks | Petra |
| Darkness + Water | Acid rain, corrosive water | Oxy |
| Fire + Light | Blinding radiance, plasma, radiant heat | Helios |
| Wind + Light | Aurora, sky light phenomena | Eos |

**Extranatural conditions** are not defined by element combinations but by **contradictory simultaneous states** — what no natural phenomenon can sustain. Their source is Kaodis (Void, son of Lampsi + Nytha):

| Contradictory state | Effect | Note |
| --- | --- | --- |
| Fire + Ice (same point) | Incoherent temperature — burns and freezes | Fire+Water → steam is natural (Atmos). Fire+Ice is not. |
| Light + Darkness (simultaneous) | Luminosity that does not illuminate; shadows without absent light | **Primary Kaodis marker** |
| Earth (solid) that does not support weight | Terrain behaves like liquid without being liquid | |
| Light + Darkness + Water | Rain that does not reflect light; sky with both unresolved | |
| Three or more elements in active conflict | Extranatural by definition — Kaodis present | |

Characters can recognize extranatural conditions through:

- **Perception** — notices something is not behaving as expected
- **Instinct** — primal non-rational response to the Void's presence
- **Thaumaturgy** — identifies the taumatic origin and structure of the phenomenon
- **Theology** — recognizes Kaodis's presence through the canonical signs of the Void cult

---

## Severity levels

Each severity level maps directly to one difficulty tier. The Narrator sets the environmental NR within that tier based on the specific intensity of the condition.

| Severity | Difficulty tier | Base | NR range | Type |
| --- | --- | --- | --- | --- |
| Mild | Fundamental | 5 | 0 | Natural |
| Moderate | Challenging | 8 | 0–1 | Natural |
| Severe | Rigorous | 11 | 1–2 | Natural |
| Disastrous | Demanding | 14 | 2–3 | Natural or early extranatural |
| Extreme | Extreme | 17 | 3–5 | Natural or extranatural |

---

### Mild (Fundamental — 5 + NR)

Few disruptive factors. Manageable with basic attention.

**Natural:** light rain with gentle wind; irregular but familiar terrain; reduced visibility (light fog); uncomfortable but tolerable temperature; ambient noise (nearby river, wind through trees).

**Effect model:** Hinder — penalties without added Attrition cost.

---

### Moderate (Challenging — 8 + NR)

Active disruption. Requires adaptation. Affects concentration, coordination, or communication.

**Natural:** moderate storm with reduced visibility; very irregular or marshy terrain; intense but not extreme heat or cold; noise that prevents verbal coordination; partial darkness (insufficient torches, covered moon).

**Effect model:** Hinder, escalating to Restrict in specific contexts.

---

### Severe (Rigorous — 11 + NR)

Significant factors. Actions demand greater effort. Some tactical options are actively limited.

**Natural:** strong storm with wind that prevents light projectiles and impedes movement; very rough terrain with fall risk; sustained extreme temperature; near-total darkness with minimal visibility; combat in water or on unstable surface.

**Effect model:** Restrict.

---

### Disastrous (Demanding — 14 + NR)

Near-disabling conditions. May be natural phenomena at their extreme, or the first manifestation of extranatural influence. At this level the distinction between natural and extranatural begins to matter mechanically.

**Natural:** active earthquake with collapses; maximum-intensity hurricane; active wildfire with unpredictable direction; maritime storm with waves overwhelming structures.

**Extranatural (early):** two elements in active conflict (extreme heat with simultaneous snow); actively shifting terrain; darkness with a visible light source that produces no illumination; temperature varying several degrees in seconds.

**Effect model:** Restrict → Accelerate.

---

### Extreme (Extreme — 17 + NR)

Limit of what is survivable or executable. Extranatural conditions are common at this range. Three or more elements in active conflict, or phenomena the environment cannot sustain under natural logic.

**Natural:** maritime storm with simultaneous boarding and structure collapse; earthquake combined with nearby volcanic eruption.

**Extranatural:** complete elemental storm (all elements in simultaneous active conflict); light and darkness with simultaneous physical effects; environment in active dimensional collapse (the Void touching directly); unstable physical rules — irregular gravity, perceptible time distortion.

**Effect model:** Accelerate — may generate passive Attrition.

---

## Effect model

Environmental conditions apply pressure through three stages. A single condition may escalate between stages during an encounter if not mitigated.

| Stage | Mechanical effect |
| --- | --- |
| **Hinder** (Entorpecer) | Penalties on affected rolls; no additional Attrition cost |
| **Restrict** (Limitar) | Limits available actions or imposes difficulty modifiers |
| **Accelerate** (Acelerar) | Adds +1 to the Attrition cost of relevant actions |

Full model: `data/system/attrition-fatigue.yaml (conditions_and_environment)`

---

## Narrator guidance for NR assignment

The environmental NR reflects how much a specific instance of a condition presses beyond the baseline for its severity level.

| Environmental NR | Meaning |
| --- | --- |
| 0 | Condition at its minimum expression for the severity level |
| 1 | Notable condition within its level; some compound factors |
| 2 | Intense condition; multiple simultaneous factors or extended duration |
| 3 | Condition at its peak, or first confirmed extranatural marker |
| 4–5 | Clear extranatural influence; reserved for Extreme severity |

---

## Specializations and environmental conditions

The following specializations interact directly with environmental conditions:

| Specialization | Condition type | Context |
| --- | --- | --- |
| Aclimatación (Tenacity) | Natural — environmental | Adapting to hostile or extreme environments |
| Tolerancia (Tenacity) | Natural — physiological | Enduring pain and physical strain from conditions |
| Vigor (Tenacity) | Natural — sustained effort | Maintaining function under physical load |
| Equilibrio (Agility) | Natural — terrain | Reactive response to involuntary balance loss |
| Supervivencia (Wisdom) | Natural — field | Practical decision-making in hostile environments |

**Open design question (D-08):** Whether Aclimatación and other natural specializations apply equally to extranatural conditions. A combined elemental storm is not simply "extreme cold" — it may require different capacities (Instinct, Resonance, Thaumaturgy). Cannot be resolved without designing the Void system.

Provisional rule: Aclimatación applies to Disastrous-level conditions with an extranatural component. Its effectiveness in Extreme conditions of vacual origin is undefined.

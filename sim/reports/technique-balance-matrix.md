# Technique Balance Matrix

This report is a **general game-wide balance matrix**, not a species-isolated
report.

Its purpose is to make current `sim_defined` Techniques easier to compare
across:

- `Rhythm`
- `Attrition`
- immediate vs persistent value
- positional vs ailment vs geometry vs stealth pressure
- current runtime maturity

It is not a final balance verdict.

It also does **not** define a new cost baseline.

The canonical cost spectrum remains the design authority in:

- [combat-atb-rhythm-costs.md](../../docs/adr/combat-atb-rhythm-costs.md)

At the current phase of the simulator, this matrix is best read as:

- a shared cost map
- an early warning table for cost drift
- a place to spot suspiciously cheap or suspiciously expensive Techniques
- a bridge between authority intent and simulation coverage

---

## Reading rule

Three ideas matter more than raw cost alone:

1. `Rhythm` should track **tempo burden**
2. `Attrition` should track **pressure / commitment / repeatability burden**
3. duration and denial matter as much as hit payload

That means:

- a `Rhythm 4 / Attrition 1` attack is not automatically equal to another
  `Rhythm 4 / Attrition 1` utility Technique
- a Technique with state persistence or repeat denial may deserve a similar or
  higher cost than a direct damage line
- a Technique that only changes one geometry permission may deserve to stay
  relatively cheap even if it feels clever

---

## Canonical system spectrum

The cost spectrum already adopted by authority is broader than the currently
ported simulator cluster.

### Rhythm bands

From the ADR:

- `0` = Free
- `3` = Quick
- `5` = Standard
- `7` = Heavy
- `9` = Extreme

Important:

- this is a **band system**
- it is not a statement that every valid Technique must sit exactly on `3`, `5`,
  `7`, or `9`
- intermediate values like `4` or `6` are still meaningful as tuned positions
  between bands

### Attrition bands

From the ADR:

- standard meaningful actions under pressure -> `1`
- heavy or strongly committed actions -> `2`
- extreme actions -> `3`

Important:

- `1` is structurally common on purpose
- `2` marks stronger commitment
- `3` is available for exceptional pressure lines
- nothing in the ADR says a Technique family must cluster at one exact pair

---

## Observed current cluster

The simulator does **not** yet represent the full system cost distribution.

It currently overrepresents:

- novice Techniques
- one-exchange lines
- bounded tactical permissions
- first-pass ports from Zarnag and Naghii

That means the current cluster leaning toward:

- `Rhythm 4 / Attrition 1`
- `Rhythm 5 / Attrition 1`

does **not** mean those are the game's true universal center.

It more likely means:

- many currently ported novice Techniques live between `Quick` and `Standard`
- many of them still count as standard meaningful pressure rather than heavy
  commitment
- the simulator has not yet ported enough extreme, passive, defensive, support,
  or higher-tier lines to show the full spectrum honestly

So yes: the large number of `4 / 1` and `5 / 1` entries is probably a real
signal of the **current observed cluster**, but not proof of the final global
balance center.

---

## Current observed anchors

These are not permanent laws. They are only the strongest **observed anchors**
inside the currently ported simulator subset.

### `Rhythm 3 / Attrition 1`

Current meaning:

- low-cost tactical access
- utility with strong constraints
- value comes from enabling a narrow line rather than forcing a broad swing

Current example:

- `Pasar Como Parte del Fondo`

### `Rhythm 4 / Attrition 1`

Current meaning:

- the densest currently observed novice Technique bucket
- one meaningful attack, utility, pressure, or reactive permission
- usually one exchange, one tactical denial, one state application, or one
  bounded positional change

This is the **main observed comparison bucket** right now.

### `Rhythm 5 / Attrition 1`

Current meaning:

- often reads stronger than the densest `4 / 1` bucket in either:
  - positional swing
  - follow-up permission
  - cleaner recovery
  - better conversion of an exchange into advantage

### `Rhythm 5 / Attrition 2`

Current meaning:

- medium-high commitment
- usually a more forceful or committed offensive line
- should feel noticeably more demanding than the common `4 / 1` cluster

### `Rhythm 7 / Attrition 2`

Current meaning:

- heavy spike or hard-conversion attack
- should represent a much stronger exchange event than the rest of the novice
  field

---

## Matrix

| Technique | Species | Origin | Role | Rhythm | Attrition | Duration model | Current state | Provisional balance read |
| --- | --- | --- | --- | ---: | ---: | --- | --- | --- |
| `Pasar Como Parte del Fondo` | `Zarnag` | `Sigilo` | active utility / concealment crossing | `3` | `1` | `until_crossing_or_detection` | `question_ready` | Cheapest current line; makes sense only if concealment access stays narrow and watched crossings keep real risk. |
| `Reír en la Brecha` | `Zarnag` | `Evasion` | active attack / read pressure | `4` | `1` | `one_direct_answer_or_next_activation_end` | `runtime_supported` | Strong observed anchor for one-exchange pressure plus bounded procedural follow-up. |
| `Robar la Orilla` | `Zarnag` | `Claws` | active attack / post-hit reposition | `4` | `1` | `immediate` | `runtime_supported` | Strong reference point for “hit plus small reposition” staying inside the common observed bucket. |
| `Reír Donde Más Suena` | `Zarnag` | `Intimidacion` | active pressure / ailment | `4` | `1` | `ailment_persistence` | `question_ready` | Potentially very efficient if ailment pressure dominates; needs repeated question coverage to confirm. |
| `Doblar el Tiro` | `Naghii` | `Ranged Weapons` | active attack / indirect geometry | `4` | `1` | `immediate` | `runtime_supported` | Reads coherent in the common observed bucket if novice use stays limited to one honest rebound surface with normal final defense. |
| `Marcar la Lectura` | `Naghii` | `Ranged Weapons` | active utility / route readability | `4` | `1` | `until_next_movement_or_concealment_or_mark_clear` | `runtime_supported` | Still plausible at `4 / 1` because runtime cleanup is easy and the mark does not grant raw attack conversion by itself. |
| `Nublar la Señal` | `Naghii` | `Ranged Weapons` | active utility / sensory burden | `4` | `1` | `until_cleanup_or_next_channel_dependent_action` | `runtime_supported` | Most likely efficient current Naghii ranged utility; one-answer spoil at `4 / 1` is believable, but worth dedicated question coverage. |
| `Robar el Ángulo` | `Naghii` | `Flexible Weapons` | active attack / reposition + spoil | `4` | `1` | `until_immediate_response_or_recenter` | `runtime_supported` | The sharpest novice efficiency candidate in the current set; probably acceptable only because its spatial theft remains short and local. |
| `Anudar el Paso` | `Naghii` | `Flexible Weapons` | reactive utility / anti-disengage denial | `4` | `1` | `immediate` | `runtime_supported` | Looks coherent if it stays denial of clean exit rather than broad hold or immobilization. |
| `Cerrar la Línea` | `Naghii` | `Spear` | reactive attack / movement entry denial | `4` | `1` | `immediate` | `runtime_supported` | Looks coherent as a narrow reactive lane punish; would become suspicious only if the entry window broadens beyond committed movement. |
| `Abrir la Costura` | `Zarnag` | `Evasion` | active attack / seam setup | `5` | `1` | `one_followup_impact_or_user_next_activation_end` | `runtime_supported` | Strong reference for a setup attack that asks more tempo than the common `4 / 1` cluster without extra Attrition. |
| `Recuperar la Distancia` | `Naghii` | `Spear` | active attack / post-hit recovery | `5` | `1` | `immediate` | `runtime_supported` | A clean novice reference for “attack plus one-meter distance recovery” costing above the common cluster but below heavy commitment. |
| `Clavar el Paso` | `Naghii` | `Spear` | active attack / committed entry | `5` | `2` | `immediate` | `runtime_supported` | Current benchmark for committed novice forward pressure; should feel materially heavier than `Recuperar la Distancia`. |
| `Atajar el Brote` | `Zarnag` | `Bite` | active attack / same-exchange block bypass | `7` | `2` | `immediate` | `runtime_supported` | The high-spike novice outlier; useful as the upper reference for heavy exchange conversion. |
| `Tocar y Ceder` | `Naghii` | `Flexible Weapons` | active attack / advance-strike-retreat | `5` | `1` | `immediate` | `runtime_supported` | hit 71.2%, damage/activation 2.33 (kusari_fundo, base_potency 6). ηR=0.52. Lower absolute efficiency than Clavar el Paso at same cost, but the advance+retreat cycle buys meaningful safety not captured in raw value. n=500. |
| `Clavar la Cadencia` | `Naghii` | `Ranged Weapons` | reactive attack / movement disruption | `4` | `1` | `immediate` | `runtime_supported` | hit 62.6%, damage/activation 0.39 (marking_dart_launcher, base_potency 5). ηR=0.10 — low because low weapon potency and movement disruption is untracked. On-hit movement disruption rate ≈ hit_rate (62.6%) via reduce_target_movement_rank_bonus. Authority discrepancy: cost_note references R=5 but structured field is R=4; needs editorial resolution. n=500. |
| `Pesar el Umbral` | `Naghii` | `Sigilo` | active utility / hidden-presence fear | `3` | `1` | `ailment_persistence` | `runtime_supported` | aterrorizado application rate 62.6% from hidden position (two-stage: Sigilo wins + target fails Alteration R.R.). ηR effective ≈ 0.21 on fear value scoring. Requires valid hidden position — precondition justifies Quick band. Comparable to Reír Donde Más Suena (Zarnag R=4 direct fear) in application rate but cheaper because precondition is binding. n=500. |
| `Leer el Calor del Paso` | `Naghii` | `Percepcion` | active utility / information read | `3` | `1` | `immediate` | `runtime_supported` | Always resolves (no opposition, opposed_by=null). All question metrics 0.0 — information output is Narrator-side, no mechanical sim state. Resolution rate 100%. R=3 is consistent with Quick band for guaranteed-success narrow utility. n=500. |

---

## Early Risk Flags

These are not conclusions. They are the first places worth testing harder.

### Likely efficient for cost

- `Robar el Ángulo`
- `Marcar la Lectura`
- `Nublar la Señal`
- `Cerrar la Línea`

Why:

- all sit in the `4 / 1` band
- all can create value beyond raw damage
- all may influence future movement, reads, or answer quality

### Naghii novice closure read

After the current runtime-closure pass, the twelve published novice Naghii
Techniques split into balance groups:

- likely coherent now
  - `Cerrar la Línea`
  - `Anudar el Paso`
  - `Recuperar la Distancia`
  - `Clavar el Paso`
  - `Doblar el Tiro`
  - `Tocar y Ceder`
  - `Leer el Calor del Paso`
  - `Pesar el Umbral`
- coherent but worth routine confirmation
  - `Marcar la Lectura`
  - `Clavar la Cadencia` (authority R=5 vs sim R=4 discrepancy must be resolved)
- most in need of focused question coverage
  - `Robar el Ángulo`
  - `Nublar la Señal`

Why:

- the spear ladder remains internally clean:
  - `Cerrar la Línea` at `4 / 1`
  - `Recuperar la Distancia` at `5 / 1`
  - `Clavar el Paso` at `5 / 2`
- `Anudar el Paso` remains narrow enough to live inside `4 / 1`
- `Doblar el Tiro` stays honest at `4 / 1` only while rebound geometry remains
  tightly bounded
- `Marcar la Lectura` is not obviously cheap, but its real value depends on how
  often preserving route readability matters in scenario play
- `Robar el Ángulo` and `Nublar la Señal` both buy more than one simple number:
  they distort the target's next answer, so they are the two best candidates
  for saved balance questions before any rebalance
- `Tocar y Ceder` at `5 / 1` reads plausible: hit 71.2%, lower per-activation
  value than spear techniques but the advance+retreat cycle buys safety not
  captured in the metric
- `Clavar la Cadencia` at `4 / 1` shows low ηR (0.10) because weapon potency
  is low and movement disruption is untracked; the authority cost_note references
  R=5 — this discrepancy should be resolved before treating the cost as settled
- `Leer el Calor del Paso` at `3 / 1` is a guaranteed-success information read;
  technique_value is always 0.0 in the sim (output is Narrator-side), R=3 is
  consistent with the Quick band for narrow, no-fail utility
- `Pesar el Umbral` at `3 / 1` shows 62.6% fear application from hidden
  position — the binding precondition (real concealment required) justifies the
  Quick band; comparable to single-stage fear techniques at `4 / 1`

### Likely fair anchors

- `Reír en la Brecha`
- `Robar la Orilla`
- `Recuperar la Distancia`
- `Clavar el Paso`

Why:

- each has a clear and bounded tactical return
- each is easier to reason about in one exchange
- they already provide useful novice comparison anchors inside the current sample

### Likely outlier checks

- `Pasar Como Parte del Fondo`
  - could be too cheap if concealment persistence is too forgiving
- `Atajar el Brote`
  - could be correct as a spike, but should remain exceptional and not become
    the true damage benchmark for novice Techniques

---

## Best Next Balance Questions

If we want this matrix to become more than a static table, these are the best
next questions to save and run:

1. `Rhythm 4 / Attrition 1` novice comparison
   - compare:
     - `Robar el Ángulo`
     - `Cerrar la Línea`
     - `Marcar la Lectura`
     - `Nublar la Señal`
     - `Reír en la Brecha`

2. `Spear novice attack ladder`
   - compare:
     - `Cerrar la Línea`
     - `Recuperar la Distancia`
     - `Clavar el Paso`

3. `Persistent utility vs immediate attack`
   - compare:
     - `Marcar la Lectura`
     - `Nublar la Señal`
     - a plain novice ranged attack baseline

4. `Committed attack pricing`
   - compare:
     - `Clavar el Paso`
     - `Atajar el Brote`
     - other one-exchange conversion lines

---

## Current Limits

This matrix is still limited by runtime maturity.

Several Naghii Techniques are only `sim_defined`, not honestly
`runtime_supported` yet:

- `Doblar el Tiro`
- `Marcar la Lectura`
- `Nublar la Señal`
- `Robar el Ángulo`
- `Anudar el Paso`
- `Cerrar la Línea`

So the matrix is already useful for:

- spotting cost drift
- spotting suspicious buckets
- defining question order

But it is **not yet enough** to settle final cost on those lines without
scenario or question evidence.

---

## Working takeaway

Right now the safest reading is:

- the **canonical** spectrum is the ADR:
  - `Rhythm 0–9` through named bands
  - `Attrition 1–3+` through structural commitment bands
- the **observed** simulator cluster currently leans toward:
  - `4 / 1`
  - `5 / 1`
- that likely happens because:
  - novice ports dominate the sample
  - many current lines are meaningful but not yet heavy
  - broad-spectrum coverage is still incomplete

So the matrix should help answer:

- is this Technique priced coherently inside the current sample?
- does it sit plausibly inside the canonical ADR spectrum?

not:

- what single universal baseline should all future Techniques copy?

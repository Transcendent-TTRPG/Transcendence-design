# Combat Playtest — Ice Wolf (v3 · First Runnable Version)

> **Iteration:** 3
> **Purpose:** First version with concrete mechanical values. Friction system validated across three simulated group compositions (mixed, martial-heavy, specialist-heavy). This version is ready to run with a live group.
> **Status:** Ready to run — validate mechanical values and Narrator signal clarity in a real session.
> **Changes from v2:** All TBD items resolved. Bite gesture formalized as Narrator signal. Cold condition fully defined. Bestiary Lore reading rule codified with explicit tiers and difficulties. Wolf stats provided as Traits. Environmental cold given mechanical presence.
> **What remains open after this run:** Final numerical tuning of Cold condition difficulty targets, vital point box counts, and Fatigue timing under real play conditions.

---

## 1. Enemy Role
**Category:** Common

**Function within the system:**
First calibration reference for a common but genuinely dangerous creature. Validated across three simulated group compositions: mixed, martial-heavy, and specialist-heavy. The friction-learning system is confirmed to work; this version tests whether the proposed mechanical values support it correctly under real play conditions.

**What this iteration should put to the test:**
- [ ] Whether the proposed vital point box counts (throat: 3, legs: 2) produce the right phase pacing
- [ ] Whether Cold condition level thresholds feel proportionate to exposure
- [ ] Whether the Bestiary Lore reading difficulty tiers correctly limit early confirmation without making the specialization feel useless
- [ ] Whether Fatigue 1 arrives after at least one exchange of operating with knowledge, not simultaneously with discovery
- [ ] Whether the ambient Cold I at encounter start is felt as meaningful but not punishing

---

## 2. Playtest Objective
This run exists to verify whether:

- [ ] the throat is found before or clearly at Fatigue 1, not after — across any group composition
- [ ] the bite gesture is registered as a meaningful signal by at least one player in melee range without being prompted
- [ ] the targeted strike rules (declared intent, +2 difficulty) feel fair rather than punishing
- [ ] Cold condition levels I–III create escalating pressure without overwhelming a group that responds correctly
- [ ] the Bestiary Lore reading tiers function as designed — direction at L1, partial confirmation at L2, full confirmation at L3 (only after both abilities observed)
- [ ] the wolf's behavioral shift in Phase 3 reads as a consequence of throat damage, not as arbitrary escalation
- [ ] the Narrator can deploy abilities in any order and the friction path remains valid

---

## 3. Encounter Context

**Location:**
Frozen terrain — open ground with limited cover. Visibility is clear but footing is difficult.

**Environmental conditions:**

- **Ambient Cold (Cold I):** Every character begins the encounter at Cold I. The ground, wind, and exposed terrain are sufficient to establish the minimum cold condition from the moment the wolf is engaged. This is the environment's mechanical floor — it guarantees that even a group that avoids every wolf ability pays some attrition cost.
- **Ice underfoot:** Movement at speed on ice requires a Characteristic Roll (AGI, difficulty 10). On failure: movement is halved for that exchange or character is knocked prone (Narrator's choice based on context).
- **Low wind:** The wolf can be heard approaching before it is seen. Players have one brief moment of warning before the wolf enters visual range.

**What players know before the combat:**
- [ ] There is a wolf-like creature in the area
- [ ] It has been reported attacking travelers
- [ ] It leaves frozen bite marks

**What they do not yet know:**
- [ ] It has a breath weapon linked to its mouth/throat
- [ ] Targeting the throat limits both its bite and its breath
- [ ] It becomes more aggressive when injured — does not retreat easily

---

## 4. Enemy Stats

> *NPCs and monsters use Traits rather than competency progression. The values below are proposed for this playtest and should be adjusted after the first real session.*

**Name:** Ice Wolf

**Brief description:**
A large predatory wolf with pale grey-white fur, exhaling cold vapor with each breath. Its eyes are pale and fixed. It moves in short explosive bursts rather than a sustained lope.

**Health pool:** 2d20 *(roll at session start; re-roll each iteration to check if pool size affects phase pacing)*

**Trait — Bite:**
Attack: 1d10 + 4
Damage on hit: 1d8 physical + Cold condition Level I applied to target (see section on Cold condition)
Special: before each bite, a **throat contraction is visible** — a brief muscular pulse in the neck, cold vapor concentrating just below the jaws, observable to any character at close range. This is a Narrator signal, not a mechanical telegraph.

**Trait — Aggressive Rush:**
Attack: same as Bite
The wolf covers full distance to its target in the same action as a bite. Can pass through or past a character's position. If it passes through: target makes a C.R. (AGI, difficulty 10) or takes the bite as a partial hit (half damage, no Cold application).
Triggers: any exchange in which the wolf is not already adjacent to its target.
Telegraph: head lowered, weight shifts visibly to hindquarters. Occurs one beat before resolution — a character who is observing (not attacking) can act on this before the rush resolves.

**Trait — Icy Breath:**
No attack roll — area effect. Short forward cone (roughly the length of the wolf from head to tail, 90-degree arc).
Direct hit: Cold condition Level II applied to each target in the cone.
Edge of cone: Cold condition Level I applied.
Recovery: 1 exchange cooldown after use. During recovery the wolf's vapor is visibly thinner.
Telegraph: head orients toward targets + vapor noticeably increases + jaws begin to part. A character who has seen this before can act before it resolves; on first exposure, reaction is after the fact.
Narrator note: deploy with narrative intent. There is no required frequency. The friction path does not depend on this ability being used early.

**Combat style:**
- [x] aggressive
- [x] territorial
- [ ] ambusher
- [ ] controller
- [ ] adaptive — *the wolf becomes less predictable after Phase 2, see section 10*
- [ ] coordinator
- [ ] other

**Pressure it exerts on the group:**
- [ ] Forces melee or near-melee range through aggressive movement
- [ ] Icy breath punishes clustering — players must spread or face Cold II
- [ ] Constant repositioning denies easy kiting or ranged dominance
- [ ] Environmental Cold I is the baseline — the encounter is already costing the group from the first exchange

---

## 5. Cold Condition

> *Cold is an elemental alteration. It has three levels of severity. Multiple applications escalate the level — they do not apply separately (Strongest Condition rule applies within a level, but sources from different origins can escalate to higher levels).*

### Levels

**Cold I — Leve:**
Numb extremities, shortened breath, muscles slow to respond.
Mechanical effect: +1 difficulty to all physical precision actions (targeted strikes, fine manipulation, rapid movement).
Narrative: "Your fingers are going numb. The cold is already inside you."

**Cold II — Moderado:**
Sensation leaving the extremities, reactions dulled, grip weakening.
Mechanical effect: +1 difficulty to all physical actions (not just precision). Movement speed reduced — cannot sprint or dash.
Narrative: "The cold has settled into your joints. Moving fast feels like pushing through mud."

**Cold III — Severo:**
Shaking, loss of fine motor control, coordination failing.
Mechanical effect: +2 difficulty to all physical actions. Movement reduced to half. Every significant action under Cold III counts as 1.5 actions toward Fatigue threshold.
Narrative: "Your body is turning on you. Each movement requires a decision."

### Sources and application

| Source | Cold level applied |
|---|---|
| Ambient terrain (at encounter start) | Cold I |
| Bite | Cold I |
| Icy Breath (direct hit) | Cold II |
| Icy Breath (edge of cone) | Cold I |
| Remaining in breath-affected area 2+ exchanges | Escalate current level by 1 |

If a character already has Cold I and receives a bite: escalates to Cold II.
If a character already has Cold II and receives a breath direct hit: escalates to Cold III.
Strongest Condition applies: if two simultaneous sources would give the same level, it does not stack — only the strongest applies.

### Resistance and recovery

**Resisting Cold application:**
When Cold is applied by the wolf (bite or breath), the target may attempt a Resistance Roll:
`R.R. = 1d10 + TEN + Elemental Resistance competency level`

| Incoming Cold level | Difficulty |
|---|---|
| Cold I | 8 |
| Cold II | 12 |
| Cold III | 16 |

On success: Cold level is reduced by one (Cold II becomes Cold I; Cold I is negated).
On failure: full Cold level applies.
The ambient Cold I at encounter start does not allow a resistance roll — it is environmental and unavoidable.

**Recovery:**
One full exchange spent out of direct combat and away from the wolf or breath effects: reduce current Cold level by 1.
Recovery from Cold III to Cold II requires two exchanges of rest, not one.

---

## 6. Vital Points

### Vital Point 1 — Mouth / Throat

**Related to:** Both Bite and Icy Breath. Unified source.

**Damage track:** □ □ □ *(3 boxes)*

**Targeting:**
Declaring a targeted strike at the throat costs +2 to the attack difficulty. The throat is a narrow, moving target in a large aggressive animal.
On success: normal damage applies AND mark one box.

**Primary friction signal (independent of Icy Breath being used):**
Before each bite, a brief throat contraction is visible at close range — a muscular pulse, cold vapor concentrating in the neck just before the jaws close. A character in melee range who is not in their own action may notice this without a roll. A character who is actively observing (not attacking) notices it automatically.

**Thresholds:**

*1 box filled — Superficial:*
The wolf recoils its head involuntarily — a brief, sharp movement it did not choose. A short, dry sound in the throat. The vapor of its next exhale is noticeably thinner for one exchange.
Mechanical: Bite damage reduced by 1d4. Icy Breath range reduced by half.
Narrator cue: "Something in that hit landed differently — the wolf felt it."

*2 boxes filled — Effective:*
Bite applies no secondary Cold condition (still deals physical damage). Icy Breath requires an additional exchange of recovery before reuse.
Mechanical: Bite deals physical damage only, no Cold application. Breath cooldown becomes 2 exchanges.
Narrator cue: "The bite still has teeth — but the cold is fading from it."

*3 boxes filled — Neutralized:*
Bite becomes a basic strike with no special properties. Icy Breath is disabled entirely. The wolf shifts to pure physical aggression.
Mechanical: Bite is 1d6 physical only. Icy Breath is unavailable for the remainder of the encounter.
Narrator cue: "It's still dangerous — but that cold is gone."

---

### Vital Point 2 — Legs / Hindquarters

**Related to:** Aggressive Rush and repositioning.

**Damage track:** □ □ *(2 boxes)*

**Targeting:**
+1 to attack difficulty (larger zone than throat, but low and fast-moving). On success: normal damage AND mark one box.

**Thresholds:**

*1 box filled — Superficial:*
Rush covers less distance — the wolf can no longer close from long range in one action. Cannot pass through a character's position.
Narrator cue: "It's limping slightly — the burst of speed it had before isn't quite there."

*2 boxes filled — Neutralized:*
Rush is disabled entirely. The wolf can only attack adjacent targets. Becomes significantly more readable — it cannot reposition after attacking.
Narrator cue: "Its movement is short and direct now. It's losing the ability to circle."

---

## 7. Enemy Reading Paths

### 7.1 Friction-Based Reading

**Clues from the bite (primary independent path — does not require Icy Breath to have been used):**
- [ ] Before each bite: throat contraction visible at close range — the cold is being drawn from the throat toward the jaws
- [ ] Bite leaves cold residue in the wound — the cold entered through the jaws, not from the body
- [ ] Together, these are sufficient to form the hypothesis "the throat is the source" without the breath weapon

**Clues from impact:**
- [ ] First throat hit: involuntary behavioral response (head recoil, dry sound, vapor thinner) — clearly different from body hits, readable by any player in direct combat
- [ ] Leg damage: visible limp, shorter rush range
- [ ] Body hits: no behavioral change — the negative signal that something specific matters

**Clues from behavior:**
- [ ] Rush is telegraphed by weight shift to hindquarters — one beat before resolution
- [ ] Head orients toward breath targets before the attack — readable after first exposure
- [ ] Recovery pause after Icy Breath — observable as a window

**Clues from receiving or witnessing abilities:**
- [ ] Icy Breath clearly emanates from the mouth — not from the body
- [ ] Cold from the bite and cold from the breath feel like the same cold, from the same source

---

### 7.2 Deliberate Reading — Bestiary Lore

> **Reading tier rule:** The Bestiary Lore specialization can confirm the mechanism of an ability using observational data from that same ability. It cannot infer the mechanism of an ability that has not yet been observed. This is a specific rule that overrides the general "any knowledge roll gives full information" interpretation.

**Specialization Roll:**
`S.R. = 1d10 + Specialization Level + Competency Rank + INT`

**Tier 1 — No observational data (wolf only seen, no abilities witnessed):**
Difficulty: 18
Result on success: *"Cold predators of this type concentrate thermal energy in a localized region — not the body generally. The source is somewhere in the head or neck."*
What it gives: direction (zone: head/neck region). No mechanism, no confirmation.
Advantage over friction: group knows where to look before the first hit. Skips initial trial-and-error on the body.

**Tier 2 — One ability observed (bite witnessed, or Icy Breath witnessed, but not both):**
Difficulty: 14
Result on success: *"The [observed ability] is powered by a thermal gland in the throat — the cold is generated there and delivered through the jaws [or exhaled from the same structure]. Damaging it would affect this ability."*
What it gives: exact zone (throat) + mechanism of the observed ability. Does not confirm unified control of both abilities.
Advantage over friction: skips 1–2 exchanges of targeted trial-and-error. Group can attack the throat with intent from the next exchange.

**Tier 3 — Both abilities observed (bite AND Icy Breath both witnessed or received):**
Difficulty: 10
Result on success: *"Both the bite and the breath share the same thermal gland. The throat is the unified source — damaging it interrupts both simultaneously."*
What it gives: full confirmation. Group knows exactly what targeting the throat accomplishes.
Advantage over friction: compresses Phase 2 entirely. The group can act with complete tactical clarity.
Restriction: Tier 3 is only available if both abilities have been observed. A deep knowledge roll without this data cannot reach this result regardless of roll value.

**Partial success (any tier, roll within 3 of difficulty):**
The Narrator gives a vaguer version of the result — directional but incomplete. For example at Tier 2: "Something in the throat is involved — you're not certain whether it's the source or just one pathway."

---

## 8. Expected Group Actions

- [x] attack by trial and error — produces useful friction through bite gesture and negative body-hit feedback
- [x] observe first — rewarded but not mandatory
- [x] analyze during combat — the wolf's behavior is consistent and learnable mid-fight
- [x] neutralize a dangerous part — targeting the throat is the key decision point
- [x] change target based on clues — body feedback drives target switching
- [ ] divide roles within the group
- [x] control the terrain — spreading reduces Cold II exposure from breath
- [x] hold out until discovering the enemy's logic
- [ ] other

---

## 9. Attrition Pressure

**Actions that should feel costly:**
- [ ] Taking Icy Breath without repositioning — Cold II escalates quickly to Cold III if the group clusters
- [ ] Ignoring the rush telegraph and taking full hits repeatedly
- [ ] Reaching Cold II or III without attempting to reduce it

**Actions that should not feel too costly:**
- [ ] Attempting to read the wolf — observing should not feel like a wasted action
- [ ] Repositioning — movement should remain a real option despite ice underfoot
- [ ] Attempting a Bestiary Lore reading — even a failed read should produce something useful (Narrator interprets partial success)

**Dominant attrition type:**
- [x] physical
- [ ] cognitive
- [ ] emotional / social
- [x] mixed — Cold condition and environment create a secondary layer that is active from the first exchange

**Fatigue trigger:**
Fatigue 1 should arrive after the group has at minimum one full exchange of operating on the correct knowledge (throat identified and targeted). It should not arrive simultaneously with discovery, and never before it.

*Proposed Fatigue threshold for reference:*
Base threshold ≈ Resilience × 2 + 3 significant actions.
For a starting character (TEN=1, WIS=0, CMP=0 → Resilience=1): threshold ≈ 5 significant actions.
Under Cold II: each action counts as 1.5 toward threshold.
Under Cold III: each action counts as 2 toward threshold.

*What this means for pacing:* a character who takes a bite plus a direct breath hit (Cold I → Cold II) reaches threshold faster. A character who avoids the breath entirely has more margin. This is the correct incentive structure — spread and avoid, or pay accelerated Fatigue.

---

## 10. Expected Combat Phases

### Phase 1 — Approach and Assessment
**What happens:**
The wolf appears and closes distance. First rush. Players encounter the bite and observe the throat contraction gesture, possibly for the first time.

**What players should perceive:**
Something in the wolf's throat moves before each bite. The cold element is localized — not from the whole body.

**Phase 1 ends when:** at least one player has formed a hypothesis about the throat, whether through the bite gesture, the cold residue on a wound, or a Bestiary Lore reading.

### Phase 2 — Pattern Recognition and Hypothesis
**What happens:**
The bite gesture has been noticed. The cold residue has been compared to the Icy Breath (if used). The group begins to focus on the throat.

**What changes:**
The first deliberate throat strike happens. The behavioral response (head recoil, dry sound, vapor change) makes the vital point unambiguous.

**Phase 2 ends when:** the group is consciously targeting the throat — not just hitting it accidentally.

### Phase 3 — Exploitation or Attrition
**What happens:**
The throat takes sustained damage. At 2 boxes the bite loses cold application; at 3 boxes the breath is disabled.

**What changes:** The wolf enters its erratic phase. The Narrator connects this explicitly to the throat damage.

> *Narrator note: when the wolf's behavior becomes more direct and less telegraphed, name the cause in your description. "Something in that damage changed it — the wide circles are gone. It just comes straight now." This must read as consequence, not as escalation.*

**What's at stake:**
Can the group finish the wolf before Cold III forces a harder choice? If the throat is neutralized — does the fight feel clearly winnable now despite the accumulated attrition?

---

## 11. Narrative Signals for the Narrator

> **Independence principle:** Each signal below functions independently of what other abilities have been shown. The friction path does not require a specific deployment order. A Narrator who withholds the breath for three exchanges has not broken the encounter — the throat is still discoverable through the bite alone. Deploy abilities with narrative intent.

### On the bite (every use)
- [ ] Just before the jaws close: throat contraction visible at close range — brief muscular pulse, cold vapor concentrates in the neck. *Describe this every time the bite is used.*
- [ ] After the bite: cold residue visible in the wound — "the cold didn't come from the air. It came through the teeth."

### On the Icy Breath (every use)
- [ ] The breath emanates from the mouth — not from the body. Short forward cone. "It's coming from the jaws — not from the whole creature."
- [ ] After the breath: vapor from the wolf's exhale is noticeably thinner. A brief pause. *This is the recovery window.*

### If the group attacks the body (no vital points)
- [ ] The wolf shakes off hits without changing behavior
- [ ] "It keeps moving exactly as it did before — nothing seems to slow it"
- [ ] Cold vapor from its breath remains dense and consistent

### If the group hits the throat insufficiently (1st hit, superficial)
- [ ] The wolf recoils its head — a brief involuntary movement it didn't choose
- [ ] A short, dry sound in the throat, different from anything before
- [ ] The next exhale is visibly thinner for one beat
- [ ] *"Something in that hit landed differently — the wolf felt it."* Say this out loud. Make it unambiguous.

### If the group hits the throat effectively (2nd–3rd hit)
- [ ] The bite no longer leaves cold residue — "just teeth now"
- [ ] Icy Breath either fails or produces only a weak, short gust
- [ ] *"It's still dangerous — but that cold is gone."*

### If the wolf enters the erratic phase (throat at 2+ boxes)
- [ ] Wide repositioning arcs disappear — movement becomes shorter and more direct
- [ ] The wolf focuses on whoever last damaged its throat
- [ ] *Name the cause explicitly: "Something in that hit changed it. The circles are gone. It just comes straight now."*

### Environmental cold (use in any exchange where no direct damage lands)
- [ ] Extremities grow numb — fingers, toes, exposed skin
- [ ] Breath becomes visible and shortened between actions
- [ ] The ground pulls warmth upward through boots
- [ ] *"The cold here doesn't wait for the wolf to touch you."*

---

## 12. What Should Happen if the Group Plays "Without Analyzing"
- [ ] The throat contraction before each bite is visible at close range — after 1–2 bites a character in melee range can form the hypothesis without deliberate analysis
- [ ] The body-hit negative feedback pushes trial-and-error toward different zones
- [ ] The first throat-hit behavioral response is immediate and unambiguous — they learn through result, not intent
- [ ] Cold attrition builds naturally — even without understanding the system, the pressure is felt from the ambient Cold I baseline

---

## 13. What Should Happen if the Group Does Analyze
- [ ] The throat contraction is identifiable in Phase 1 — a character actively watching can name the hypothesis before the first throat strike
- [ ] Bestiary Lore Tier 1 gives direction in Phase 1, Tier 2 gives confirmation after one ability is observed
- [ ] Cold attrition is managed — group spreads to avoid breath, uses recovery exchanges efficiently
- [ ] Fatigue arrives later for the group that spreads and manages Cold, earlier for the group that clusters

---

## 14. Playtest Success Criteria

The encounter works well if:
- [ ] At least one character targets the throat before the end of Phase 2, without being told to
- [ ] The throat contraction is mentioned or acted on by at least one player independently
- [ ] First Fatigue arrives after the group is operating with knowledge of the throat — not before, not simultaneously
- [ ] Cold condition levels create meaningful pressure without overwhelming a responsive group
- [ ] The wolf's Phase 3 behavior shift is read as earned, not as arbitrary
- [ ] The Narrator did not need to deploy abilities in a specific order to keep the encounter readable

---

## 15. Poor Calibration Signals

### Too opaque
- [ ] Group reaches Phase 3 without anyone targeting the throat
- [ ] The throat contraction is described but no player connects it to anything
- [ ] Body-hit negative feedback is not distinct enough to drive target switching

### Too obvious
- [ ] Group targets throat on turn 1 without any friction
- [ ] Vital point is neutralized before Phase 2
- [ ] Bestiary Lore Tier 1 read already gives too much — adjust Tier 1 wording or raise difficulty

### Too costly
- [ ] Cold III reached before the group finds the throat
- [ ] Fatigue 1 arrives before Phase 2 is complete
- [ ] Cold condition stacks faster than a reactive group can respond

### Too flat
- [ ] Wolf is killed by raw damage before any phase transition
- [ ] Throat damage produces no visible behavioral change players can act on
- [ ] Phase 3 behavior shift feels like escalation, not consequence

### Bestiary Lore miscalibration
- [ ] Tier 3 result was reached without both abilities being observed — reading trivializes discovery
- [ ] Tier 1 result gave full confirmation — adjust wording or raise difficulty
- [ ] All three tiers felt identical in usefulness — tiers are not meaningfully differentiated

### Narrator dependency (carried from v2)
- [ ] Throat was only found because the Narrator happened to use the breath early — bite gesture alone was insufficient

---

## 16. Playtest Log
**Test group:**
[ ]

**Number of players:**
[ ]

**Group level / state:**
[ ]

**Wolf health rolled (2d20):**
[ ]

**Actual combat duration:**
[ ]

**Approximate moment of first Fatigue:**
[ ]

**How many significant actions did an average character perform before Fatigue 1:**
[ ]

**Was the throat contraction noticed independently (without being prompted):**
[ ]

**At what exchange / phase did the group first target the throat:**
[ ]

**Path to throat discovery:**
- [ ] bite gesture observed
- [ ] cold residue compared to breath
- [ ] body-hit negative feedback → target switching
- [ ] Bestiary Lore reading (which tier)
- [ ] accidental throat hit → behavioral response

**Was Icy Breath used before the throat was identified:**
[ ]

**Cold condition levels reached (per character):**
[ ]

**What the group learned through friction:**
[ ]

**What the group learned through specializations:**
[ ]

**Which vital point did they discover first:**
[ ]

**Which enemy ability did they neutralize first:**
[ ]

**How the combat was ultimately resolved:**
[ ]

**Did the ambient Cold I feel present as passive pressure:**
[ ]

**Did Phase 3 behavior shift read as consequence or escalation:**
[ ]

---

## 17. Post-Playtest Adjustments
After the playtest, what should be modified?

- [ ] throat contraction visibility — too subtle / too obvious
- [ ] throat-hit behavioral response — not unambiguous enough / correctly calibrated
- [ ] throat vital point box count — too few / too many (proposed: 3)
- [ ] leg vital point box count — too few / too many (proposed: 2)
- [ ] Cold I difficulty threshold — 8 too easy / too hard
- [ ] Cold II difficulty threshold — 12 too easy / too hard
- [ ] Cold III difficulty threshold — 16 too easy / too hard
- [ ] cold escalation speed — Cold III reached too fast / too slow
- [ ] wolf health pool — 2d20 too high / too low
- [ ] wolf Bite A.R. bonus — +4 too strong / too weak for starting group
- [ ] Bestiary Lore Tier 1 difficulty — 18 too punishing / correctly limiting
- [ ] Bestiary Lore Tier 2 difficulty — 14 correctly calibrated / needs adjustment
- [ ] Bestiary Lore Tier 3 restriction — Tier 3 without both abilities observed occurred / restriction held
- [ ] Fatigue timing — arrived correctly / too early / too late
- [ ] Phase 3 erratic behavior — read as consequence / read as escalation
- [ ] environmental cold presence — felt / invisible
- [ ] Narrator dependency — throat found without breath / only found after breath used
- [ ] overall difficulty
- [ ] other: [ ]

**Mechanical values to prioritize for adjustment:**
[ ]

**Designer notes:**
[ ]

---

> **Next iteration:** `combat-ice-wolf-v4.md` — apply numerical adjustments from section 17. If Cold condition thresholds, vital point box counts, and Fatigue timing all hold, v4 can be considered the final calibrated version for this enemy.

# Combat Enemy Readability, Vital Points, Specialization Boundaries, and Fatigue Timing

**Status:** Adopted (structural findings) — numerical calibration open
**Scope:** Common-enemy combat design
**Case study:** Ice Wolf
**Related systems:** Combat, Vital Points, Enemy Reading, Specializations, Attrition, Fatigue
**Related files:**
- `playtests/combat/common-enemy-readability-v1.md`
- `playtests/combat/common-enemy-readability-v2.md`
- `playtests/combat/common-enemy-readability-v3.md`
- `docs/adr/combat-champion-encounter.md`

---

## Purpose

This document records the official design findings extracted from the Ice Wolf playtest series. Its purpose is not to define final numeric values, but to formalize the structural conclusions that emerged from testing a common enemy with linked vital points, friction-based discovery, specialization-assisted reading, and meaningful attrition pressure.

The findings here are now adopted design principles. They apply beyond the Ice Wolf to any common enemy with similar architecture.

---

## Case Study Context

The Ice Wolf was chosen as the first calibration reference for a **common** enemy: dangerous, stronger than an individual player in direct terms, but intended to be understandable from inside the encounter rather than through prior investigation. Its primary offensive structure links both bite and icy breath to the mouth/throat vital point, with legs/hindquarters acting as a secondary tactical target through mobility reduction.

The original playtest questions were:
- Can the Ice Wolf be read through friction alone?
- Does targeting the throat meaningfully change the encounter?
- Do specializations accelerate reading without becoming mandatory?
- Does Fatigue appear at the right moment in the fight?

---

## Tested Iterations

Three diagnostic simulations were run before the first real session:

**1. Mixed group** — Martial, Tactical, Specialist, Conservative. Validated the intended healthy version of the encounter. The group converged on the throat through different independent routes. Fatigue 1 appeared after the enemy's logic had become actionable, not before.

**2. Martial-skewed group** — No Specialist, no Conservative spacing behavior. Tested whether the encounter remained readable through pure friction, impact feedback, trial-and-error, and opportunistic play. Result: the throat still emerged, but Fatigue 1 arrived almost simultaneously with collective discovery rather than after it. The encounter was on the edge of being too costly for non-analytic groups.

**3. Deep Specialist group** — Tested the upper edge of knowledge-driven acceleration. Identified the exact threshold where specialization stops accelerating reading and starts replacing discovery. Trivialization begins not when the Specialist identifies the correct region, but when they can confirm the functional relationship between multiple enemy abilities before both have been observed in play.

---

## Core Findings

### 1. Common enemies must be readable from inside the encounter

A common enemy may still be stronger than an individual player, but its logic must be understandable through the fight itself. The Ice Wolf passed this test in every iteration. Behavior, impact, visible telegraphs, and post-hit changes were sufficient for players to identify that some body zones mattered more than others — without external information.

**Adopted principle:**
A common enemy must be solvable through at least one of: direct observation, impact feedback, behavior reading, or trial and error. Relevant specializations may improve the path but must not gate it completely.

---

### 2. Friction-based discovery is sufficient and valid

The martial iteration demonstrated that the encounter does not depend on formal analysis to function. The group found the throat through three independent friction routes:
- The Protector connected bite-cold and breath-cold as the same source through direct comparison
- The Opportunist found the throat through timing — an exposed zone during the wolf's recovery pause
- The Impatient player discovered that body hits produced no meaningful behavioral change and changed targets by trial and error

This confirms an important system identity: **all characters can attempt any relevant line of play**, even without specialized investment. The difference is not access, but speed of comprehension, certainty of interpretation, and tactical efficiency.

**Adopted principle:**
Enemy-reading systems must preserve at least one valid friction path that does not require specialized build investment.

---

### 3. Specializations must accelerate or deepen reading, not replace it

The mixed and deep-specialist iterations together define a healthy boundary.

A specialization is working correctly when it:
- identifies a likely region sooner than friction would
- confirms the mechanism of an observed behavior with fewer trial exchanges
- reduces error-cost for the group without eliminating error as a learning mechanism

A specialization is working incorrectly when it:
- eliminates the discovery phases for the whole party
- confirms unobserved functional relationships by theory alone
- turns "read and act" into "execute a solved plan" before the enemy has meaningfully revealed itself

**Adopted principle:**
Specializations may accelerate or deepen enemy reading. They must not fully replace the discovery phase.

---

### 4. Reading depth is bounded by what has been observed

This is the most operationally precise finding from the specialist iteration.

**Adopted rule:**
A specialization may confirm the mechanism of an ability using observational data from that same ability. It may not infer the mechanism of an ability that has not yet been observed.

This means the "unified source" confirmation — that the throat controls both the bite's cold element and the breath simultaneously — is only available to a character who has encountered both abilities in play. Deep theoretical knowledge does not bypass this requirement.

---

## The Reading Depth Model

The Ice Wolf tests support a formal three-level reading model applicable to any enemy with vital points and specialization-readable mechanics.

### L1 — Direction
The specialization provides a likely relevant region, a probable threat type, and a strong clue about where to look. It does not confirm exact mechanism or total solution.

Example result: *"The neck/throat region is likely important."*

Typical specialization difficulty: high (no observational data required, but reward is limited).

### L2 — Partial Confirmation
The specialization confirms the exact zone and the mechanism of one already-observed ability. It provides a strong actionable hypothesis but not the full picture.

Example result: *"The throat channels the cold used in the bite."*

This is the upper acceptable edge of early information — before both abilities have been observed. The deep-specialist run confirmed this level does not trivialize discovery.

Typical specialization difficulty: moderate (requires having witnessed the ability being read).

### L3 — Full Confirmation
The specialization confirms the link between multiple enemy abilities, the unified vital point, and the expected result of neutralizing it.

This level is only appropriate if all relevant abilities have already been observed or concretely established in scene. Granting L3 before that converts the encounter from a reading encounter to a mere execution encounter.

Example result: *"The throat is the unified source — damaging it stops both the bite's cold and the breath simultaneously."*

Typical specialization difficulty: low (the character has observed everything; the roll just formalizes synthesis).

**Mechanical reference (Ice Wolf v3 implementation):**
- L1: S.R. difficulty 18, no observational prerequisite
- L2: S.R. difficulty 14, one ability observed
- L3: S.R. difficulty 10, both abilities observed — unavailable otherwise regardless of roll result

---

## Narrator Deployment Independence

This finding emerged from the comparison between the mixed and martial simulations and shaped a significant design constraint.

In the mixed group simulation, the discovery path worked in part because the Narrator happened to use the breath early, establishing "the mouth is the source of the cold." When tested with a martial group, this dependency became visible: if the Narrator withheld the breath for narrative reasons, the friction path to the throat became weaker.

This is a structural problem. The Narrator is not a neutral algorithm with a fixed ability sequence. They deploy enemy capabilities with narrative intent — to establish fear, to punish complacency, to create pressure when the scene calls for it, to reward aggressive play when it should succeed. An encounter whose readability depends on the Narrator using a specific ability in a specific window creates an implicit restriction on Narrator judgment.

**Adopted principle:**
Each friction signal must function independently of what other abilities have been shown. The discovery path cannot require the Narrator to have deployed specific abilities in a specific order. Signals are parallel discovery paths, not a sequential chain.

**Practical implication for enemy design:**
Every ability must carry its own readable signal. The bite must suggest the throat as its source even if the breath weapon has never been used. The breath must establish the mouth as origin even if the bite has not yet been analyzed. No single signal should be the only bridge between player observation and vital point identification.

This is why the throat contraction gesture was introduced as a primary signal in v2/v3: it gives the bite its own independent bridge to the throat, making the discovery path valid regardless of Narrator pacing.

---

## Shared Information vs. Personal Mechanical Benefit

The deep-specialist test revealed an important distinction: knowledge can be shared faster than mechanical advantage should propagate. A player who relays "the throat is the unified source" enables the whole group to change targets. But the group then essentially executes the specialist's conclusions without having developed their own reading of the enemy.

This is not inherently wrong, but it creates design pressure: if all specialist-derived mechanical benefits transfer instantly and completely, the reading layer becomes collective and nearly costless.

### Adopted distinction

**A. Shareable information**
May be communicated freely, no mechanical cost:
- "the throat matters"
- "the breath comes from the mouth"
- "the legs affect mobility"

**B. Personal interpretive advantage**
Should primarily benefit the character who did the reading:
- certainty of hypothesis (confidence to act without further validation)
- reduced difficulty on a targeted follow-up
- cleaner timing window from having read a telegraph correctly
- better ability to distinguish weak cues from strong ones

**C. Personal tactical opening**
Should usually belong to the character who created it:
- the exact timing of an interrupt
- an immediate opening caused by their read
- a vulnerability window only they are positioned to exploit in that exchange

**D. Real enemy-state changes**
Affect everyone because the enemy itself changed:
- throat damage weakening the breath
- bite losing its cold property
- leg damage reducing rush range
- a trait being disabled entirely

**Adopted principle:**
Communicative information — what the character understood, observed, or concluded — may be shared freely. Mechanical bonuses derived from that understanding belong to the character who developed it, because those bonuses represent a depth of knowledge that cannot be fully transmitted through words in a combat context.

The test for whether something is shared is not whether the Specialist chose to say it, but whether the other character could actually act on it at the same level of precision. "Hit the throat" is communicable. "I understand the exact anatomical location well enough to hit it with reduced difficulty" is not — not because the Specialist withheld it, but because the other player lacks the same underlying comprehension.

**Exception — transversal effects:**
Some enemy properties are transversal by nature: once known, they affect how the enemy is engaged by anyone. Traits fall in this category. Knowing that a trait exists and how it can be disabled gives every player the same information in the same form — there is no asymmetry of comprehension. Enemy-state changes (vital point damage reducing a trait's effect) also fall here: they affect everyone because the enemy itself changed, not because knowledge was distributed.

**Transversal effects are world-state changes, not player-held knowledge.**
This distinction is critical. A transversal effect does not exist because a player knows about it — it exists because the encounter's reality changed. If a territorial enemy is lured out of its territory and the Territorial trait is disabled, that trait remains disabled for the rest of the encounter regardless of what happens to the characters who executed the strategy. If the character who dealt the throat damage is incapacitated, the throat is still damaged. Transversal effects are facts about the world, not facts stored in individual character awareness. They persist independently of any character's survival, presence, or state.

**Group knowledge does not disappear when individual characters are lost.**
Communicative information — what was discovered and shared within the group — belongs to the group's collective state once it has been communicated, not to the individual who first discovered it. If a character who said "hit the throat" is incapacitated in the next exchange, the remaining characters still know to hit the throat. Group knowledge, once distributed, is permanent for the remainder of the encounter. This applies equally to discovered friction knowledge and to verbally shared specialization conclusions.

What *is* lost when a character is lost: their personal mechanical bonuses — interpretive advantages, reduced difficulty from deep reading, timing windows only they were positioned to exploit. These belong to the character's internal comprehension and cannot be inherited by other characters. The information behind the bonus survives; the bonus itself does not.

**The distinction in practice:**

| Type | Who benefits | Example |
| --- | --- | --- |
| Verbal information ("hit the throat") | Anyone who hears it | No mechanical effect, but enables new intent |
| Interpretive bonus (reduced difficulty from deep read) | Acting character only | The Specialist gets +X to hit the throat; allies do not |
| Trait-disabling knowledge | Everyone | "Rush is nullified if the legs are effectively damaged" — anyone can act on this |
| Enemy-state changes | Everyone | Throat neutralized → breath disabled for all targets |

**Open door — explicit coordination:**
Some personal benefits may become partially shareable through explicit coordination actions or maneuvers. For example: a declared "assist" that transfers a timing window to an ally at the cost of the acting character's own action. This is not defined yet, but it is a meaningful design space — particularly relevant for champion-tier encounters and group tactics where coordinated play should feel meaningfully different from uncoordinated individual action. See Open Design Questions.

---

## Negative Signals Matter as Much as Positive Signals

The martial iteration exposed a structural truth that applies beyond this encounter: the group converged on the throat not only because it produced special feedback, but because the body produced no meaningful behavioral change at all. The Impatient player changed targets because hitting the body kept returning "real damage, no tactical shift." That negative feedback was essential.

If body hits had produced visible pseudo-value — the wolf slowing slightly, appearing hurt without changing behavior — the group would have remained on the wrong target far longer.

**Adopted principle:**
Encounters must communicate both when a player found something meaningful and when a player's action was tactically irrelevant to the enemy's real logic.

Narrator narration should reliably support three categories of impact feedback:
1. **Ineffective** — the enemy does not change, the approach is wrong
2. **Partially disruptive** — something reacted, but not in the way that matters
3. **Functionally important** — behavior changed, a threshold was crossed, something shifted

---

## Combat Phase Structure

Across all three iterations, the encounter consistently resolved into recognizable phases regardless of group composition:

1. Approach / first contact
2. Behavioral friction
3. Threat hypothesis
4. Vital-point identification
5. Threat neutralization
6. Resolution under pressure

This confirms that the encounter is not functioning as linear HP depletion. The enemy moves from "dangerous but unclear" to "understood but still dangerous" to "degraded but still capable." That is the intended structure.

**Adopted principle:**
A well-designed encounter should transition visibly through discovery, exploitation, and pressured resolution — not only through raw damage exchange.

---

## Fatigue Timing and Attrition Pressure

The Ice Wolf tests established a structural benchmark for Fatigue timing but did not converge on a final number. The 5–7 significant actions range was a working hypothesis used to evaluate the simulations — it is a starting point for calibration, not a design target. The actual threshold must be agreed upon through further design work that accounts for enemy category, encounter intent, and character baseline resilience.

What the tests did establish is the **structural rule** for when Fatigue should arrive relative to encounter phases — independent of the specific number.

**Mixed group result:**
Fatigue 1 appeared after useful discovery and before total neutralization. This is the intended window. Players had time to understand the enemy and then operate with that knowledge before the first Fatigue arrived.

**Martial group result:**
Fatigue 1 arrived almost simultaneously with collective discovery. This is not a failure, but it leaves insufficient room for the "operate with knowledge" phase. It marks the edge of acceptable calibration for non-analytic groups in compact formation.

**Deep Specialist result:**
Fatigue timing remained healthy. Total attrition paid by the group was lower because correct information arrived earlier and positioning became more efficient. This is acceptable — specialization should produce advantage — but it warns that information cannot be allowed to erase minimum pressure entirely.

**Adopted principle:**
Fatigue 1 should arrive after the enemy's main logic has become actionable, but before that logic has been fully exploited and the threat has already collapsed. Informed groups may delay Fatigue, but cannot eliminate it.

---

## General Design Rules Derived from This Case

The Ice Wolf findings are specific, but the architecture they validate is general. Any enemy designed with vital points and friction-readable mechanics should follow the same structural constraints.

**For common enemies specifically:**
- At least one vital point should be discoverable through friction alone in under 3 exchanges of observation or combat
- Body damage should produce clearly distinguishable feedback from vital-point damage
- The most important vital point should be linked to the enemy's most threatening ability — discovering it should visibly change the encounter, not just add HP reduction
- Environmental factors should contribute active attrition pressure, not just narrative color

**For enemy ability design:**
- Each ability should carry its own readable signal, independent of other abilities
- Telegraphs should be observable by players who are paying attention, not only by characters with relevant specializations
- Cooldowns, recovery pauses, and behavioral changes after ability use are essential for pacing — they create windows that reward attention without demanding it

**For specialization interaction:**
- The L1/L2/L3 reading model scales to any enemy where a character might have relevant lore or observational skills
- The "observed ability" prerequisite for L2 and L3 applies universally — no specialization should theorize the full architecture of an unseen threat

---

## Official Decisions Adopted

1. Common enemies must be readable within the encounter itself.
2. Friction-based discovery is a valid and sufficient path — specialization cannot be the only route.
3. Specializations accelerate or deepen reading; they do not replace it.
4. A specialization may confirm the mechanism of an observed ability, but not the mechanism of an unobserved one.
5. Each friction signal must function independently of Narrator ability deployment order.
6. Communicative information may be shared freely. Mechanical bonuses derived from a character's depth of understanding belong to that character alone — they do not transfer to allies by default, because they represent comprehension that cannot be fully transmitted through words in a combat context.
7. Some enemy properties are transversal: trait-disabling knowledge and enemy-state changes (vital point damage, trait neutralization) benefit all characters because the enemy itself changed, not because knowledge was distributed.
8. Negative signals (no behavioral change from body hits) are as important as positive signals (throat hit changes behavior).
9. Fatigue should arrive after useful discovery, not before it and not only after the encounter is already solved. The specific threshold per encounter type remains open.
10. Encounters should resolve through visible phases, not only linear depletion.
11. Transversal effects are world-state changes. They persist independently of any character's survival or presence — the encounter's reality changed, not the players' knowledge. A disabled trait stays disabled even if the character who disabled it is lost.
12. Group knowledge does not disappear when individual characters are lost. Communicative information shared within the group is part of the group's collective state for the rest of the encounter. What is lost when a character is lost is their personal mechanical bonus — not the underlying information they communicated.

---

## Open Design Questions

Ordered by estimated priority for the next design phase.

**High priority:**

1. What is the correct Fatigue 1 threshold per encounter category — common, champion, elite, singular? The structural rule is settled; the specific numbers need to be agreed upon.
2. What is the minimum unavoidable attrition floor for fully informed groups? How is that floor enforced if information neutralizes most direct threats?
3. How does environmental pressure scale relative to enemy pressure in common encounters? Is there a ratio or a separate budget?

**Medium priority:**

1. What happens to the reading model when an enemy has more than two linked vital points? Does the discovery path need to change shape, or does the same L1/L2/L3 model hold?
2. Are there enemy properties that are neither fully transversal nor fully personal — for example, a tactical window that can be shared through explicit coordination but is not shared passively?

**Lower priority / longer horizon:**

1. Does the L1/L2/L3 reading model apply to social and exploration encounters, or does it require a different shape there?
2. Should NPCs or creatures ever have abilities that are permanently unreadable — not opaque, but genuinely beyond normal friction or specialization scope?

---

## Use in Future Encounter Design

Use the following as a design checklist when creating any enemy with vital points and friction-readable mechanics.

- **Reading model:** Apply L1/L2/L3. Define what each level reveals and what observational prerequisites gate L2 and L3. L3 must require both abilities to have been observed.
- **Signal independence:** Each ability must carry its own discoverable signal. Confirm the vital point is findable through the primary ability alone, without requiring other abilities to have been demonstrated first.
- **Friction path:** Design at least one valid discovery route that does not require specialization. Identify the negative signal (what wrong-target hits communicate) and the positive signal (what vital-point hits communicate). Both must be unambiguous.
- **Information scope:** Decide explicitly which enemy properties are transversal (trait knowledge, enemy-state changes), which are personal (interpretive bonuses, timing windows), and whether any could become partially shareable through explicit coordination.
- **Fatigue alignment:** Set the intended phase at which Fatigue 1 should arrive relative to discovery and neutralization. Verify the encounter is not too costly for non-analytic groups or too cheap for fully informed ones.
- **Phase structure:** Name the expected phases and what drives the transition between them. At least one phase change should be driven by player knowledge, not only by damage output.

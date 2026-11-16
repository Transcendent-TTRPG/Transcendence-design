# El rastro ofrecido — authored, ID 164

**English title:** The Offered Trail  
**Structured record:** `data/system/techniques.yaml`, `pilot_examples`, ID 164  
**Work card:** `docs/work-runs/2026-10-13-bufoni-03-impredecible.md` in the workspace  
**Approval:** project creator, 2026-10-13; complete name, entry and costs approved after discussion.

## Registration boundary

Registered as `authored`, not simulator support or empirical balance closure. ES and EN remain editorial drafts, `canonical: false`. The glossary records the creator-approved name without changing previous definitions. No domain, lineage, school, specific teacher or availability is fixed. No assignment to Chei or another character is made.

## Approved rule

- Bufoni origin, not a species restriction; reactive utility, Unpredictability, Novice weapon competency.
- Be Hidden from the relevant detector. Before learning that detector's Perception result, declare the intervention and a false point different from your real position.
- The weapon must be able to produce a physically plausible signal at that point for the detector's sense. Weapon reach limits the signal point, not the detector's distance; normal detection eligibility still applies.
- Oppose weapon A.R. by the detector's Perception S.R. Use that same Perception result against the existing active Hidden value. No reroll, replacement or improvement of that value; no second Perception roll.
- Perception strictly greater than Hidden always locates the real position, regardless of intervention A.R.
- Otherwise, A.R. strictly greater than Perception supplies the predeclared false point instead of the normal 1d8 clue. If A.R. does not exceed Perception, use normal false localization. A tie in the normal detection check favors Hidden; a tie in the intervention does not direct the clue.
- One detector and one localization attempt per use, one intervention attempt against it. Instantaneous; the selected clue is information, not a new state or forced behavior. Future searches remain available.
- Other observers resolve normally, and the signal can compromise concealment from them. Other-sense information and automatic detection are not erased.
- No own impact, weapon effects, Opening Advantage or protection against areas covering the real position.
- Rhythm 2 / Attrition 1, paid even if the clue is not directed, including successful real detection.

The corebook's preserved active Hidden value is part of this explicit contract. The older `cover-visibility-concealment.yaml` procedure still describes rerolling concealment for the hidden-player case; that existing upstream discrepancy is recorded, not silently repaired or imported into this Technique.

## Origin and comparison

This method extends Bufoni patience and terrain reading into control over what an intruder thinks they perceived. It uses a real signal, not Tauma, hallucination or control of the detector's decisions. Compatible manufactured weapons can support the method without Bufoni biology.

Published Unpredictability Techniques 6, 73 and 139 respectively cover positional theft, two-weapon sequencing and suppressing the signal used for defensive competency. The proposed method adds no equivalent damage, movement or defensive-rank denial. Cross-surface 111 Golpe Sin Eco suppresses a signal and denies Perception; 114 Depredador Umbrío repositions to preserve Hidden; 132 El Ángulo Muerto grants Hidden under specific observation limits; 8 Nublar la Señal degrades a sensory channel. This method leaves ordinary detection intact and controls only its already-false clue. Older structured variants of 6 and Esconder la Segunda Línea differ from their published counterparts; both versions were checked, not overwritten.

## Cost question

The approved 2/1 is an authoring starting point for one immediate information conversion. A physical signal and timed execution rule out Rhythm 0; two comparisons do not constitute two independent outputs requiring Attrition 2. Compare 2/1 and 3/1 with ordinary random false localization under equivalent physically plausible layouts, measuring actual localizations, intervention failures, repeat opportunities, other-observer exposure, route/area consequences and actions the detector really chooses. No movement or wasted action should be counted as guaranteed. This is a saved question seed, not an executable experiment or result.

## Runtime gap

Classification: `new_subsystem` for the missing localization/information-resolution pipeline, a conservative porting estimate, not a new game state. The existing `sim/models/concealment_state.py` stores observer-relative Hidden and its active value, and `effects.py` can grant it. However, `engine/concealment.py` contains only a stub. `activations.py` supports an opposed specialization/Perception roll but does not implement this pre-detection reaction, preserve a single detector result through both comparisons, or emit a chosen false clue. `reactions.py` handles attack-defense reactions, not localization attempts. Existing hidden-crossing experiments test detection rates; they do not establish this event/false-position pipeline.

Required support: eligible localization-attempt events, pre-result declaration, physically/sensorily valid signal points, single reusable Perception results, strict comparison priority, ordinary false-position fallback, observer-specific clue output, once-per-attempt guards and reaction costs on every valid execution. Policies must act on perceived clues rather than actual positions. No simulator data, handler or coverage is added in this authoring pass. The YAML `false_location_control` object records a contract, not executable runtime support.

Scenario seeds: success/failure/ties at both comparisons; real localization despite a higher A.R.; invalid/unreachable signal points; unaffected senses and automatic detection; multiple observers; later searches; detector refuses the clue; area over real position; attack detection versus localization; repeated intervention denial; declaration before hidden results are known.

## Verification boundary

Check editorial parity, numeric fields, references, HTML structure and print-sheet identity. These checks do not execute the game rule. Browser local-file access was previously denied: do not bypass it with another browser or local server. Visual overflow, print layout and loaded fonts remain pending permitted visual review. Do not label the card print-ready, the runtime supported, or the costs balance-closed.

Focused checks passed: ID 164 is unique; all required catalog fields exist; the complete 2/1 contract matches the approved rule; ES effect wording matches the approved entry; references and bilingual fields agree; HTML nesting, SVG IDs, icon/CSS references and standalone/print article identity are valid. All three existing printed cards are unchanged. After excluding 164, the semantic SHA-256 of all 139 previous records and metadata remains `e41ad76857b609e847662ac5010797e04f6d732333e37801372a9da1e4a370b4`.

The central validator reports the same 66 pre-existing errors and zero warnings, with no errors for 164. The editorial indexer adds a false positive for the ES bilingual pair because it hardcodes the corebook directory and rejects the independent Techniques directory. Real ES/EN links exist; no fictitious link or unrelated pipeline change is used to force a pass. Global validators are not reported as passing.

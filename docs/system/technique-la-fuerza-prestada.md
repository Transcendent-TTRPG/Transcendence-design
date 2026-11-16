# La fuerza prestada — authored, ID 163

**English title:** Borrowed Force  
**Structured record:** `data/system/techniques.yaml`, `pilot_examples`, ID 163  
**Work card:** `docs/work-runs/2026-10-13-bufoni-02-torsion.md` in the workspace  
**Approval:** project creator, 2026-10-13

## Registration boundary

The creator approved the complete entry and its title after approving contact reach, resolution, costs and chaining limits. Registration is `authored`, not simulator support or balance closure. ES and EN entries remain editorial drafts, `canonical: false`. The glossary records the approved name without changing existing rule definitions. No domain, lineage, school, teacher or availability is fixed. Neither this Technique nor its transmission is assigned to Chei.

## Approved rule

- Origin: Bufoni practice; no species restriction.
- Reactive utility; minimum weapon competency Novice; Torsion profile.
- Instantaneous; Rhythm 3 / Attrition 1, paid even on failure. No own impact or weapon effects.
- Trigger: one declared physical attack against one creature, before its defense resolves. The practitioner's weapon must reach the attacking weapon or limb at the contact point being altered. The attack need not target the practitioner; the aggressor's body need not be within that reach.
- No projectiles or area attacks. Choose another creature reachable by the same attack along a physically legal trajectory, without extending reach or crossing obstacles.
- Intervention weapon A.R. opposed by the aggressor's A.R.; strict greater-than succeeds. Failure or tie leaves the original recipient's normal defense intact.
- Success redirects that one attack. Preserve the aggressor's attack die; recalculate only modifiers dependent on the new recipient. Resolve that A.R. against the new recipient's D.R.
- If the attack connects, the aggressor resolves its impact and contact effects against the new recipient's protection. Check their requirements, margins and resistance rolls against the actual recipient; do not grant effects merely because redirection succeeded.
- One attack per use, not a whole sequence, movement or additional attacks. One attempt per practitioner per attack. An attack successfully redirected by this Technique cannot be redirected again through it. The new recipient retains other permitted reactions.

The utility adds no strike from the user's weapon: no natural poison, critical impact or other on-contact effect is inherited from the practitioner's contact. Conversely, the original aggressor's contact payload is not erased. The term “another creature” adds no blanket exclusion of the practitioner or aggressor: physical legality of the original attack decides eligibility.

## Comparison and cost question

Published Torsion Techniques 5, 75, 79 and 138 cover stopping withdrawal, repositioning, disarming and destabilizing. Cross-profile 27 Levantar el Dique (4/1) transfers reception to the practitioner; 146 El Plano Interpuesto (3/1) cancels an attack against an ally; 154 Invertir la Carga (3/1) cancels and displaces. Techniques 12 and 141 cancel and counterattack. This method instead redirects the existing attack to a legal recipient and preserves its hostile payload. These are comparison points, not proof of uniqueness or balance.

The creator approved 3/1 as an authoring starting point. A failed second defense is not required for the original recipient to benefit: successful redirection already protects them. Conversely, an aggressor's powerful impact or poison may make a successful intervention very valuable. Compare 3/1 with 2/1 and 4/1 under equivalent encounter conditions, controlling alternative-recipient frequency, failed interventions, successful new defenses, hostile payload strength, repeated attacks and net costs. This is a saved question seed, not an executable experiment or result.

## Runtime gap and verification boundary

Classification: `small_runtime_extension` as a porting estimate; not implemented. Inspection of `sim/engine/reactions.py` shows a defender-selected defensive reaction yielding a defense bonus and timeline costs, not a third-party attack redirection. `sim/engine/activations.py` fixes the target before resolving the weapon exchange and does not preserve a rolled attack for a newly selected recipient. It also omits the defensive reaction hook when the incoming intent itself is reactive.

Required support: a pre-defense attack declaration window, intervention by a third party, explicit physical-contact and alternative-trajectory validation, reusable attack die and recipient-dependent modifiers, actual-recipient impact/effect resolution, failed-intervention costs, per-practitioner attempt tracking and per-attack successful-redirection guards. Support valid incoming reactive attacks as well as active attacks, without inventing a new restriction. Preserve other permitted reactions. The `attack_redirection` YAML object documents the contract; it is not a runtime handler.

Scenario seeds: success/failure/tie; self versus third-party protection; aggressor body outside reach but contact reachable; illegal new trajectory, obstacles, projectiles and area attacks; target-dependent modifier changes; new defense succeeds/fails; original poison or contact effects with margins and resistances checked against the actual recipient; no own-weapon effects; multiple attacks paid separately; no repeat attempt by the same practitioner; no second successful redirection through this Technique; other permitted reactions remain available.

HTML structure and parity with the print sheet can be verified statically. Visual overflow, print layout and loaded fonts remain unverified because the browser refused local-file navigation; do not bypass that restriction with another browser or a local server. Do not label the card visually approved or print-ready until a permitted visual review is completed.

## Integration checks

Focused checks passed: ID 163 is unique; all 138 prior records and central metadata have the same semantic SHA-256 after excluding 163; ES effect wording matches the creator-approved entry; numeric fields and bilingual references agree; HTML is structurally balanced with resolved SVG/CSS references; the card article equals the print-sheet article; both previous printed cards are unchanged. These checks do not execute the combat rule or certify visual layout.

The central validator still reports the same 66 pre-existing metadata errors and zero warnings; the new record introduces none. The editorial indexer reports one new false positive because its bilingual-pair check only accepts links under `core-books/transcendence-corebook/`, not the actual independent `core-books/transcendence-techniques/` directory. Both real bilingual links exist. That pipeline limitation is recorded, not bypassed with a fictitious reference or silently repaired in this Technique's scope.

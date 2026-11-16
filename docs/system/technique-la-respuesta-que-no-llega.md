# La respuesta que no llega — authored, ID 162

**Structured record:** `data/system/techniques.yaml`, `pilot_examples`, ID 162  
**Work card:** `docs/work-runs/2026-10-13-bufoni-01-aprovechamiento.md` in the workspace  
**Approval:** project creator, 2026-10-13

## Registration boundary

The approved Technique is registered in the central catalog as `authored`, not implemented in the simulator. ID 162 is unique and follows the highest currently published ID. Publications remain editorial drafts; creator approval of the rule does not imply runtime or balance validation. Domain, lineage, teacher and availability have not been fixed.

With creator authorization, 29 pre-existing records were indentation-normalized before insertion. All non-whitespace characters and the parsed content of all 137 existing records were preserved. No existing duplicate IDs were found. The central validator then reported 66 pre-existing missing-field errors; these were not repaired by inventing content. The temporary standalone YAML was consolidated into the central catalog, not retained as a second authority.

## Approved rule

- Origin: Bufoni, without a species restriction.
- Type: reactive utility; minimum weapon competency rank Novice.
- Profile: Interruption.
- Support: the exact Poison Entorpecido, at any of its three severities; any source may have applied it.
- Trigger: a target within weapon reach declares a Reaction containing a physical attack or movement, before that Reaction starts resolving. The response need not be directed at the user.
- Resolution: weapon A.R. opposed by target D.R.; strict greater-than succeeds, a tie fails.
- Success: cancel the entire declared Reaction. The target retains that Reaction's Rhythm and Attrition costs.
- Failure: the original Reaction proceeds normally.
- Rhythm 4; Attrition 1; instant; no damage, weapon effects, or poison modification.
- One attempt per declared Reaction. Cannot target this same Technique, an Active Action, or an ordinary D.R.

Entorpecido is not a synonym for general hindrance. It increases action costs and does not inherently disable reactions. The Technique grants a separately trained intervention; it does not turn the poison's Rhythm penalty into an extra preparation phase or an automatic cancellation.

## Comparison and costs

Compare with published 148 Reconocer el Gesto (active-Technique cancellation) and 157 La Transición (personal movement continuity against a hostile reaction). The support condition and third-party intervention are material differences, but require scenario comparison before claiming balance closure. Published 37 Devolver al Cauce and the cost master table support 4/1 as a conditional utility starting point. The creator approved those costs; no runtime test has validated them.

The method is contact used to spoil an action, not a full damaging hit. No natural-weapon effect is inherited. Its function remains available with a manufactured weapon of the correct profile.

## Pending validation

- Runtime gap: `small_runtime_extension`, with an upstream Entorpecido port. Existing `sim/engine/reactions.py` resolves defensive reactions to incoming attacks and spends their timeline costs; it does not expose a pre-resolution third-party interception window. `sim/engine/activations.py` skips that defensive hook when executing a reaction. Add declared-reaction interception, once-per-reaction/self-exclusion guards, opposed weapon resolution without impact, and retained cancellation costs before claiming support. This classification is a porting estimate, not implemented coverage.
- Entorpecido is defined in authority but absent from `sim/data/ailments`; port its three severities and cost effects before testing this requirement. Do not replace it with a different ailment.
- Save and run a minimum cost question comparing this method with 148 and 157.
- Test all severities, other poisons, ties, failed checks, range denial, self-targeted technique chains, ordinary D.R., and third-party intervention.
- No Technique or language is assigned to Chei by this addition.

# La mancha que vuelve — authored, ID 165

**English title:** The Returning Stain  
**Structured record:** `data/system/techniques.yaml`, `pilot_examples`, ID 165  
**Work card:** `docs/work-runs/2026-10-13-bufoni-04-corrosion.md` in the workspace  
**Approval:** project creator, 2026-10-14; name, Novice rank, costs, procedural limits and complete ES entry approved after discussion.

## Registration boundary

Registered as `authored`, not simulator support or empirical balance closure. ES and EN remain editorial drafts, `canonical: false`. Only the creator-approved Technique name is added to the glossary; previous definitions remain unchanged. No domain, lineage, school, specific teacher or availability is fixed. No assignment to Chei or another character is made.

This is a Technique-local reactive permission, not a change to ordinary application, poison routes, medical treatment, all Interact actions or a new universal residue catalog. No macro-system ADR or ability-surface redefinition is introduced.

## Approved rule

- Bufoni origin, not a species restriction. Reactive utility; Corrosion weapon; Novice or higher weapon competency.
- Declare before a deliberate action removes an external chemical residue from a creature within weapon reach. The target may clean itself or receive help. The reapplication target remains the contaminated creature, not the helper.
- Resolve removal normally first, then make a fresh weapon A.R. against the target's current D.R. Reach and all original application requirements must hold at that time.
- Reapply the same residue at the same affected point. Know its application procedure; if sourced from a Technique, know that Technique. Have material available for a fresh application and satisfy its weapon/kit/application requirements.
- Keep specific original application modifiers and resistances. Removed residue no longer penalizes the target's new defense.
- A.R. must strictly exceed D.R.; failure or tie does not reapply. Success resolves the material's residual effect, including any required resistance. No automatic exposure or resistance bypass is granted.
- Severity, persistence, consumption and removal follow the original procedure with the practitioner's applicable competency, not the previous applicator's rating. This Technique grants no independent severity bonus.
- No damage, weapon effects or other outputs from the originating Technique. Utility omits the Hereda Efectos / No Hereda Efectos keyword.
- If the original residue remains, do not stack its penalties or automatically increase severity. Original cleanup costs and result are preserved.
- Rhythm 3 / Attrition 2 for this reaction, not an additional full activation charge from the originating Technique. Costs do not disappear when the application fails.
- One attempt per practitioner per removal action. Reapplication itself is not a removal action and cannot generate another use of this same permission.
- Exclude internal poison, infection and wound treatments, repair of material damage and removal caused solely by the environment.
- Instantaneous resolution in the same exchange. The residue's own persistence is unchanged; no future-action promise or new maintained state is created.

## Material and application boundary

The concrete published example is ES Technique 8, Nublar la Señal / Blur the Signal: external alchemical sensory residue, Kit de Munición / Ammunition Kit, identified exposed channel and A.R. modifier −2. A practitioner cannot omit those gates merely by using this reaction. The fresh application uses that practitioner's applicable competency and the same affected channel.

The ES source and older central/simulator variants of 8 differ: the published ES rule assigns a channel-specific Alteration until cleanup; older records model one channel-dependent penalty with limited uses. This registration does not rewrite 8 or import its older runtime payload as the published effect.

Ensuciar la Herida (52) describes cleaning/alignment of damaged tissues rather than a removable external chemical residue. La Capa Que Cede (140) has a structured residue/cleanup description but ES prose lacks those explicit boundaries. Neither is automatically treated as eligible because its profile is Corrosion. Their existing discrepancies remain out of scope.

The general poison framework admits several administration routes, but all five current ES catalog poisons require inoculation. This reaction does not convert them to skin-contact agents, reproduce natural-weapon poisons or allow renewed internal poisoning during medical treatment. It does not define a new chemical formula, dose size or consumption rule absent from the source procedure; applying any future residue requires its own defined material, exposure and cleanup procedure.

## Origin and comparison

The method grows from Bufoni empirical knowledge of secretions, observation of a prey's response and patience in choosing the exact moment to act. It is a physical combat intervention, not a prepared environmental trap, magic or exclusively infiltration practice. A manufactured Corrosion weapon and compatible material can support it.

Same-profile 8 supplies sensory obstruction, 52 complicates wound treatment and 140 weakens a defensive surface. This Technique creates none of those payloads itself: it opens a narrow reactive window to renew an already-defined external application. It does not grant the originating procedure without training or requirements.

Cross-surface 7 marks a target; 106 supplies a venomous counter-sting after receiving a hit; 110 creates a territorial web; 128 reads contamination and improves resistance; 162 cancels a physical Reaction under Entorpecido. This method does not mark, create a trap, counter-hit, grant resistance or cancel cleanup. Its trigger and output are deliberate external cleanup followed by a fresh opposed application.

Natural-weapon precheck covered Kha-Naghii bite, Saa-Naghii breath, Zarnag bite, Chelicer sting, Arakhel bite, Bufoni tongue, Soricin fangs and Yacani bile. None of their intrinsic effects is granted through this no-impact utility contact.

## Cost question

Approved authoring cost: 3/2. Rhythm pays for a short physical intervention in a narrow timing window; Attrition reflects renewal of residual degradation that can affect multiple later exchanges, not a surcharge for the word Permanent. Comparables: 8 at 4/2, 162 at 4/1 and 164 at 2/1.

Saved minimum question, not an executed experiment: at 3/2 versus 4/2, does repeated renewal of Blur the Signal make cleanup within weapon reach systematically useless, or do fresh D.R., the original −2 application modifier, finite available material and practitioner ATB cost retain meaningful counterplay? Compare ordinary active reapplication, cleanup out of reach and environmental removal. Include hit, miss, tie, successful/failed cleanup, helper cleanup, source requirements not met and material exhaustion. Examine future residual payloads separately before extending this cost conclusion to all of them.

## Runtime gap

Classification: `new_state_family`, a conservative porting estimate for typed external residue provenance and reapplication metadata, not a new game ailment. Small associated engine extensions are also needed for this ordered reaction window.

Existing `sim/engine/procedural_states.py` supports generic procedural-state installation, refresh and expiry on fiction events. `effects.py` has a `blur_declared_sensory_channel` handler with `interact_cleanup`/channel-cleared expiry. However, that handler installs the older one-use penalty rather than the published sensory Alteration. Generic state source identity/rank and fiction-event strings do not establish the required material, affected point, delivery procedure, kits, remaining dose and known-source-Technique contract. The current reaction handler is incoming-attack/defense-oriented, not a before-cleanup declaration followed by post-cleanup reapplication.

Required support: eligible removal events and a retained declared reaction; targeted cleanup completion before the new defense; residue application provenance and affected point; procedure/Technique knowledge checks; material and kit availability/consumption according to the source; same-procedure modifiers and resistances; source-specific persistence without stacking; helper versus target identity; one attempt per practitioner/removal action; reaction timeline costs without charging the source activation as well. Do not blindly reuse old source 8 payloads or generic summing penalties as if they were this approved rule.

No simulator data, handler, policy or coverage is added. The YAML `residue_reapplication` object records a contract, not an executable handler.

## Verification boundary

Focused checks cover approved-text parity, fields/costs, real bilingual and authority links, HTML nesting, icon/CSS references, standalone/print article identity and preservation of previous records/cards. They do not execute combat or demonstrate balance.

Browser local-file access was previously denied; do not bypass it with another browser, local server or headless route. Visual overflow, loaded fonts and print layout remain pending permitted visual review. Do not label the card print-ready or the runtime supported.

Global validators have unrelated existing failures. Report their results separately from focused checks; do not change older records or pipeline links to manufacture a green result.

Focused checks passed: ES effect equals the creator-approved entry; bilingual cost/field parity, real references and content checks pass; ID 165 is unique and all central required fields exist; HTML nesting, SVG IDs, icon/CSS references and standalone/print article identity pass. All four previous print articles retain their exact hashes. After excluding 165, the semantic SHA-256 of all 140 prior records and metadata remains `d736620c81eee430e1312b5821341b65f67b7d9489c78bfe4432e943c031c031`.

The global technique validator reports the same 66 prior errors and zero warnings (141 central / 21 sim records); none concern 165. The editorial indexer reports 609 errors versus 607 before this addition: the two added notices are false bilingual-pair failures caused by its hardcoded `transcendence-corebook` prefix, despite actual ES/EN pairs in the independent Techniques directory. Both new files pass content validation without warnings. No fictitious links or unrelated metadata repairs are introduced.

The editorial CLI's `--validate` also regenerated workspace `pipeline/manifest.json`, which was already dirty before the run. This generated-index side effect was disclosed; do not reset the user's previous changes from HEAD. Global checks are not claimed as passing.

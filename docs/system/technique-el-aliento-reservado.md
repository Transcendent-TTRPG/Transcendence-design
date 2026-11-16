# El aliento reservado — authored, ID 168

**English title:** The Reserved Breath  
**Structured record:** `data/system/techniques.yaml`, `pilot_examples`, ID 168  
**Work card:** `docs/work-runs/2026-10-16-bufoni-07-nadar.md` in the workspace  
**Approval:** project creator accepted the complete ES entry after approving the hybrid prerequisites and 0/1 cost; registration authorized 2026-10-16.

## Registration boundary

State: `authored`, not runtime-supported or empirically balance-closed.
ES/EN entries remain `draft`, `canonical: false`. Bufoni is the cultural
origin, not an access gate. No character, including Chei, learns the Technique
through this registration. No particular school, domain, teacher or ritual is
established. No new poison, ailment, posture or maintained state is created.

## Approved rule

- Reactive utility, Novice rank; **Rhythm 0 / Attrition 1**, even on failure.
- Require both **Swimming and Poison Resistance at Novice or higher**.
  Swimming supplies respiratory control; Poison Resistance supplies prior
  exposure experience. Do not add the resistance competency to the S.R. or
  award resistance progress for making this activation roll.
- Perceive an imminent **discrete poison application by inhalation** and react
  before inhaling and before its Resistance Roll. No automatic detection or
  identification is granted; identifying the compound is not required.
- Make a **Swimming S.R.** The Narrator sets difficulty before the roll based
  on the speed of exposure and circumstances impeding respiratory control.
  This is a self-directed execution check, not a test against a creature's
  Nature, a chemical-identification check, or a copy of the poison R.R.
- Success prevents that application by inhalation. On failure resolve normal
  exposure and its R.R.; a failed S.R. does not automatically poison you.
- One attempt per practitioner per application. No continuous exposure,
  other routes, active-poison treatment, Suffocation protection or coverage of
  future applications. A persistent cloud cannot be sliced into repeated
  instant exposures to bypass the exclusion. Other effects resolve normally.

## Domain and dependency review

The Swimming domain explicitly transfers breath control, orientation and
pressure management to problems other than swimming. This Technique applies
that learned control under combat pressure; it does not improve swimming,
grant a longer dive or replace prepared ordinary breath-holding. Poison
experience is not Alchemy and does not identify a substance by itself.
Piel Permeable remains effective against applicable exposures; this is
avoidance of one entry route, not a resistance bonus or immunity.

The actual same-specialization pool is **38 Tomar la Corriente**, which reacts
to forced movement. The old catalogue row listed 36 Sellar la Presa, now a
Bastion weapon Technique. Correct only the affected Swimming row.

Cross-surface comparisons against published ES: 21 Templar el Veneno reduces
an already-settled poison's severity; 39 Guardar el Pulso mitigates an existing
Alteration during an action; 115 Tórax de Forja purges a respiratory agent
after a failed R.R.; 128 Lo Que el Cuerpo Delata identifies contamination;
167 La dosis perdida uses a consumable on an attacking poisoned weapon.
None grants the same pre-inhalation, discrete personal prevention.

Chapter 11 defines four poison entry routes and distinguishes poisoning from
Asfixiado. This Technique owns only the pre-entry exception for inhalation.
It does not rewrite exposure, poison severity, treatment, oxygen supply or
the separate consequences of contact, injection, ingestion and suffocation.
Contextual difficulty is creator-approved for self-directed execution, not a
new general exception to creature-targeting difficulty rules.

## Cost and saved questions

The approved **0/1** is deliberate: an internal breathing adjustment without
displacement or material manipulation, but with conscious effort under
pressure. The dual prerequisite does not turn a declared reaction into a
passive 0/0 hybrid. One prevented application is the only output.

Comparables: 38 at 3/1 physically manages displacement; 39 at 0/1+ mitigates
ongoing bodily consequences; 115 at 0/1 purges after failed resistance; 167
at 3/1 plus a dose physically neutralizes a chemical payload. These are
authoring comparisons, not an experimental verdict that 0/1 is balanced.

Saved minimum cost question, **not an executed experiment**: does 0/1 remain a
useful situational option rather than a dominant replacement for ordinary
resistance, considering both Novice prerequisites, prior perception,
contextual S.R. and continuous-exposure exclusion? Contrast 1/1 and 0/2.
Measure attempts, successes, applications prevented, remaining R.R., Attrition
and survival. Do not count other routes, physical attack effects or persistent
cloud exposure as prevented.

Derived questions: no retroactive intervention after inhalation/R.R.; unknown
compound versus imperceptible threat; one attempt per application; mixed
routes; independent later applications; persistent atmosphere; preexisting
poison and simultaneous Asfixiado; no automatic resistance progress.

## Runtime gap

Classification: **new_subsystem**. Existing simulator ailment definitions,
application handling and Technique engine do not provide a typed pipeline for
perceived discrete inhalation events, pre-entry reactions and per-route
payload prevention. Porting would need to represent timing/perception,
discrete versus continuous sources, contextual S.R., poison-route delivery,
per-event attempt limits and preservation of ordinary R.R. on failure.
No simulator definitions, policies, handlers or scenarios are added here.
This is not `data_only` or runtime-supported because the authoring YAML exists.

## Publication and validation boundary

Core ES preserves the approved effect verbatim and adds a separate example.
EN translates the same fields, gates and consequences. The ES card preserves
the complete effect rather than relying on inferred restrictions. The print
sheet grows from 6+1 to **6+2**; all seven earlier articles must remain intact.

Focused validation covers registration, hybrid requirements, self-directed
contextual activation, cost even in failure, timing, route boundaries,
continuous-source exclusion, exact approved ES wording, bilingual references,
HTML structure, local CSS/SVG links and source/print identity. Tests validate
registration, not physiological realism, runtime outcomes or empirical balance.

Visual access to local browser files was previously denied. Do not bypass
through another browser, local server or renderer. Visual overflow, fonts and
printed layout remain unverified. Preexisting central validation errors and
the indexer's corebook-only bilingual-pair path mismatch remain out of scope.
The already-dirty workspace manifest is not regenerated.

## Recorded verification — 2026-10-16

**41 static registration tests pass**: 15 focal checks for 168, the 12 existing
167 checks and 14 neutralizer checks. The 167 pagination expectation changes
to 6+2 without changing its mechanical tests. The seven modern cards match
their print copies exactly. The legacy Golpe Sin Eco source already differs
from its compressed print text; that inherited discrepancy is preserved.

Removing only 168 leaves the prior 143 records and all metadata semantically
unchanged (SHA-256 `c89d755ff900858055ae3bac08e971ec0e521715bff35317e3f5dbb0b5e1ffc5`).
All seven prior print articles retain their hashes. The manifest remains
unchanged, and `git diff --check` passes in all three repositories.

Central validator: 144 authoring / 21 simulator records; **66 inherited
errors, zero warnings**, none concerning 168. This is not a global pass.
Read-only editorial scan: 309 files, 615 errors, 220 warnings. The two
additional diagnostics are the known corebook-prefix bilingual-pair error;
both actual pair paths exist. Both new entries pass content-rule validation
without errors or warnings. Visual and runtime validation remain pending.

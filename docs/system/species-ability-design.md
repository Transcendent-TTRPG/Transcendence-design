# Species Ability Design — Herencia and Legado

This document governs the design of species biological constraints (Herencia) and
scaling bonuses (Legado). Read it before setting any mechanical values for a
species entry.

For full system reference (roll types, ATB, Attrition, Wounds, Ailments, etc.),
see [`mechanics-overview.md`](mechanics-overview.md).

---

## The core problem: S.R. bonus inflation

The failure mode for species ability design is treating every Herencia and Legado
as a bonus or penalty to a specialization roll (S.R.). This produces species that
feel identical at the table: different flavor text over the same mechanical shape.

If a player could swap species without changing how they interact with game
systems, the design has failed.

The test: does this ability change which systems the character engages with, or
does it only change the number on a roll?

---

## What Herencia is

Herencia is a biological constraint the species cannot turn off. It is not a
penalty for flavor — it is the systemic cost of what the body is.

**Herencia must touch a system.** A Herencia that only reduces a roll type is
acceptable when the reduction follows directly from the biology. A Herencia that
touches a structural system (wounds, ATB position, action availability) is
stronger design.

**Herencia examples by system touched:**

| Species | Herencia | System touched |
| --- | --- | --- |
| Drak'kai | Percepción Interferida | S.R. (Instinct/Intuition) — penalty from sensory calibration |
| Loxod | Firma Sísmica | S.R. (Stealth) — infrasonic emission always-on |
| Ceratox | Ruido de Calibración | S.R. (Perception) — signal overload in dense environments |
| Chelicer | Mandato del Veredicto | **T.D. + Wound slots** — sacred zone loses defense, ranuras saturation triggers the ability |

Chelicer is the standard. The Herencia does not just penalize a roll — it
restructures how damage arrives and creates a second trigger layer from the
wound system.

---

## What Legado is

Legado is a set of NR-scaling bonuses that reinforce the species' identity in
play. Two to three entries per species.

**At least one Legado per species must cross systems.** A cross-system Legado
changes which game systems the character engages with, not just the magnitude
of a number. Single-system Legados (S.R. bonuses) are permitted but should not
be the majority.

**Legado examples by design quality:**

| Design level | Example | Why |
| --- | --- | --- |
| Single-system | +1/4NR to S.R. Perception | Changes only a number on one roll |
| Single-system (appropriate) | +1/4NR to R.R. Poison | Still one system, but tightly grounded in biology |
| Cross-system | Transmutación del Dolor: +Desgaste capacity per wound zone saturation | Connects Wounds system to Attrition/Fatigue — two separate systems |
| Cross-system | Cicatrización Acelerada: extra ranuras freed on treatment success, conditioned on heat | Connects Wound slots to Rest & Recovery with a biological gate |
| Cross-system | Veneno Consagrado: venom applies Ailment with confirmed mechanic | Connects natural weapon to Ailments system |

---

## Biology → system mapping

When setting Herencia and Legado values, start from the biology. What does this
body actually do, and which game system owns that function?

| Biological trait | Primary system | Secondary system |
| --- | --- | --- |
| Exoskeleton / carapace | Wounds (Bloqueo per zone) | Equipment (armor equivalence) |
| Venom / toxin delivery | Ailments (Poison family) | R.R. (resistance roll forced on target) |
| Accelerated healing / regeneration | Wounds (ranura release) | Rest & Recovery (treatment conditions) |
| Extreme thermic dependency | Rest & Recovery (condition gate) | Wounds (healing efficiency) |
| Infrasound / vibration emission | S.R. (Stealth penalty — always-on) | ATB (proximity detection, if applicable) |
| Signal-dense sensory organ | S.R. penalty in noise | Cover / Visibility (detection range) |
| Large size / mass | Wounds (zone capacity) | ATB (rhythm cost on certain actions) |
| Pain-to-endurance conversion | Attrition / Fatigue (Desgaste expansion) | Wounds (trigger condition) |
| Chemical sensing | S.R. (Perception / Tracking) | Cover / Visibility (bypasses visual concealment) |
| Neural redundancy / distributed nervous system | R.R. (Alteration resistance) | Wounds (function under collapse) |
| Prehensile secondary limb | S.R. (Climbing / Grip) | Equipment (off-hand manipulation) |
| Magnetoreception | S.R. (Orientation / Survival) | Cover / Visibility (navigation without line of sight) |
| UV / infrared / non-visible spectrum vision | S.R. (Perception in darkness) | Cover / Visibility (concealment bypass) |

---

## Culture → system mapping

Cultural traits produce Legados when the practice shapes how the species engages
with game systems — not just which skills they are better at.

| Cultural trait | Primary system | Secondary system |
| --- | --- | --- |
| Trial-by-ordeal / pain theology | Attrition / Fatigue | Wounds |
| Archive / accumulated knowledge | S.R. (knowledge specializations) | — |
| Territorial long-range monitoring | S.R. (Survival / Orientation) | Cover / Visibility |
| Pack / swarm coordination | ATB (reaction windows) | Ailments (delivery via numbers) |
| Chemical communication | S.R. (Perception / Intuition) | Ailments (chemical state detection) |
| Itinerant collector culture | S.R. (History / Geography / Identification) | — |
| Thermal-ritual recovery culture | Rest & Recovery (condition criteria) | Wounds |
| Sonic / infrasonic cultural practice | S.R. (Perception at range) | ATB (initial position via acoustic warning) |
| Endurance-over-speed fighting doctrine | Attrition / Fatigue | ATB (rhythm on sustained actions) |

---

## Design checks before finalizing species abilities

Before writing the stats block into the corebook entry, verify:

| Check | Question |
| --- | --- |
| Herencia system | Does the Herencia touch a structural game system, not just a roll penalty? |
| Legado variety | Is at least one Legado crossing two game systems? |
| T.E. saturation | Are more than two Legados simple S.R. bonuses with no cross-system link? |
| Biology grounding | Can each Herencia and Legado be explained from the species' body without appeal to lore? |
| Culture grounding | If a Legado comes from culture, does it touch the system that culture actually uses at the table? |
| No-stacking check | Do any Legado bonuses stack with identical bonuses from Técnicas or equipment in a way that breaks the no-stacking doctrine? |
| Existing species contrast | Is there an existing species with the same primary system touched by the same ability type? If yes, differentiate. |

---

## The Chelicer as reference

Chelicer is the current gold standard for species ability design. Use it as the
reference when evaluating new species.

| Ability | Type | Systems crossed |
| --- | --- | --- |
| Mandato del Veredicto (Herencia) | Biological constraint | T.D. reduction in one zone + Wound slot saturation as trigger |
| Señal Consagrada (Legado) | S.R. bonus | S.R. (Perception, Intuition) — single system, acceptable |
| Veneno Consagrado (Legado) | Cross-system | Natural weapon (delivery) + Ailments (Poison) |
| Transmutación del Dolor (Legado) | Cross-system | Wounds (saturation state) + Attrition/Fatigue (Desgaste capacity) |

One of the four abilities is a pure S.R. bonus. The other three cross structural
systems. That ratio is the target.

---

## Reference map

| Resource | Path |
| --- | --- |
| Full system surfaces | `docs/system/mechanics-overview.md` |
| Ailments catalog | `data/system/ailments.yaml` |
| Wounds & damage | `docs/system/wounds-and-damage.md` |
| Attrition & Fatigue | `docs/system/attrition-fatigue.md` |
| Corebook authoring skill | `skills/species-corebook-authoring/SKILL.md` |

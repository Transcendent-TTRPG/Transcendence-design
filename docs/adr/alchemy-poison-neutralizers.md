# ADR — Specific Poison Neutralizers

**Status:** Accepted by the project creator, 2026-10-15
**Scope:** Alchemy products, poison treatment, and Technique delivery boundaries
**Authority:** `data/system/materials-and-fabrication.yaml`, `alchemy.poison_neutralizers`

## Decision

A specific poison neutralizer is a prepared consumable for one named compatible
poison formula. Its quality caps the compatible preparation qualities it can
neutralize: Common covers Common; Rare covers Common and Rare; Exceptional
covers all three. Quality is not Ailment severity. Similar symptoms or delivery
routes do not establish compatibility, and unknown poison quality is not
silently inferred from severity.

The product supplies chemical capacity. Medicine, patient access, valid
administration, and the poison's required kit and procedure resolve clinical
treatment. One administered dose is spent per valid attempt, including failure.
Success ends only that poisoning and its ongoing effects, not wounds or effects
from other sources. Medicine's retry rules remain in force. Existing authorized
alternative treatments and poison-specific recovery exceptions remain available.

## Product versus Technique

The creator explicitly rejected giving the product two autonomous use modes.
The product does not authorize neutralizing a dose on an attacking weapon.
That reactive, pre-exposure application belongs to the separately authored
Technique **La dosis perdida**. This registration does not register the
Technique, assign its ID, or grant it to a narrative character.

Higher product quality does not lower a Medicine difficulty, replace a kit,
raise the kit needed for the same poison, or grant immunity to new exposure.

## First formula family

The **Confusion Poison Neutralizer** uses ingestion and liquid doses in sealed
containers. Its three qualities have the following production values:

| Quality | Creature reagent | Botanical units | Minimum botanical index | Progress hours | Dose yield | Alchemy difficulty |
| --- | --- | --- | --- | --- | --- | --- |
| Common | Fluid ×1 | 2 | 8 | 12 | 1d4 | Challenging |
| Rare | Gland ×1 | 3 | 15 | 24 | 1d3 | Demanding |
| Exceptional | Nervous system ×1 | 4 | 24 | 36 | 1d2 | Extreme |

The creator accepted the new reagent and botanical-index values; times and
yields reuse the existing rarity ladder. Each formula requires a fixed alembic
or furnace. For this authored process, successful hourly Alchemy rolls add
progress; failed hours add none and leave reagents intact. This is not a return
to generic hourly Focus taxes or a change to unrelated fabrication processes.

Finished products are stable when sealed, uncontaminated, and normally stored.
Raw ingredients retain their own preservation requirements. This grants no
immunity to container damage or destructive exposure.

## Bounded treatment profile

The currently published **Common Confusion Poison** is treated with a Basic
medical kit and a Challenging Medicine S.R., using ordinary scene modifiers.
Under ATB pressure, treatment is an active technical action costing **Rhythm 6 /
Attrition 1**, paid even on failure. A superior neutralizer used on the same
Common poison keeps that profile. Calm treatment outside ATB does not acquire
automatic stress costs.

The local kit, difficulty, and cost were separately approved. They are not
universal poison defaults and are not derived from the botanical index.
The neutralizer variants do not create Rare or Exceptional Confusion Poisons.

## Ownership and synchronization

- Product, formula, compatibility, conservation, and local treatment profile:
  `materials-and-fabrication.yaml` and the matching reference document.
- General Poison lifecycle and existing exceptions: `ailments.yaml` / `ailments.md`.
- Spanish reader surface: chapter 10 Alchemy, linked from chapter 11 Poisons.
- English publication: deferred because chapter 10 currently contains only a
  README, not an English Alchemy manuscript. No partial substitute chapter is
  created by this bounded integration.
- Runtime: typed consumables and clinical resolution require a separate port;
  registering data is not simulator implementation or balance validation.

## Unchanged or deferred

Other poison formulas and their discrepancies are not rewritten. Formula prices
are not product dose prices; no fixed sale prices or output-family surcharge
are invented here. Broad reagent conservation, all other poison treatments, and
the Technique's eventual core/card/YAML review order remain unchanged.

## Example

A Rare neutralizer used on the published Common Confusion Poison still needs
the Basic kit and Challenging Medicine roll. A failed ATB treatment spends a
dose and 6/1, leaves the poison active, and does not grant an unchanged retry.
No outcome permits a reactive weapon application without the separate Technique.

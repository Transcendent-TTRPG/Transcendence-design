# Materials and Fabrication

**Authority data:** `data/system/materials-and-fabrication.yaml`
**Related docs:** `docs/system/equipment-overview.md`, `docs/system/wounds-and-damage.md`, `docs/system/specializations.md`, `docs/system/difficulty-thresholds.md`

---

## Purpose

This system defines how Transcendence treats:

- materials as mechanical objects;
- extraction as a trained process;
- conservation as a time and condition problem;
- fabrication as a specialization-driven production loop;
- refinement as a separate upgrade layer;
- alchemy, plants, traps, and plans as related authored subsystems.

This is a **framework layer**, not the full catalog.

It establishes the stable rules that later catalogs must obey.
Exact material entries, full recipes, complete plant lists, and item-by-item production tables belong in later data.

---

## Core Rule

Materials are not just flavor.

They matter because they change one or more real mechanical surfaces:

- `Durability`
- `Base Potency`
- valid equipment category
- valid processing path
- accessibility
- conservation pressure
- refinement compatibility

If a material does not change any real surface, it should not be tracked as a distinct material entry.

---

## Material Taxonomy

Transcendence should not try to become memorable by multiplying material names alone.

The world should feel rich because materials follow different **logics**.
For that reason, the framework distinguishes between:

- natural materials;
- processed materials;
- living materials.

This keeps the game legible while still leaving room for a world that does not behave like Earth.

### Natural materials

Natural materials are the baseline resource layer of the world.

They are recognizable, broadly understandable, and should carry most routine extraction, trade, fabrication, and survival play.

They usually include:

- creature parts;
- metals;
- minerals and stone;
- woods;
- fibers and textiles;
- leather and hide;
- plants and fungi;
- biological fluids, organs, and glands.

These are the materials players should expect to encounter first and understand most easily.

### Processed materials

Processed materials are not separate worlds of matter.
They are transformed outputs produced from natural materials through a valid fabrication domain.

Examples of processed-material logic include:

- hide turned into leather;
- scale or shell worked into protective composite;
- ore turned into alloy;
- fiber turned into cloth;
- sand or mineral feed turned into glass.

Processed materials should therefore define:

- their source material or source family;
- the specialization that produces them;
- whether they inherit, replace, or modify the source material's surfaces.

### Living materials

Living materials are the main extraordinary material layer of the setting.

They are not defined by being merely organic.
They are defined by continuing to **behave**.

A living material is any material that retains active response, growth, adaptation, or ongoing internal logic after it becomes a usable world material.

It may be:

- biological;
- mineral;
- fungal;
- composite;
- or another authored family.

What makes it living is not the family.
What makes it living is that it still reacts as though it has ongoing life, pattern, or self-adjusting structure.

This allows the setting to introduce extraordinary materials without replacing the whole natural-material layer.

---

## Material Model

Every authored material should eventually define at least:

| Field | Meaning |
| --- | --- |
| `family` | Broad material class |
| `grade` | Quality band of the material itself |
| `accessibility` | How hard it is to extract, identify, or work correctly |
| `durability` | Structural resistance against breaking |
| `base_potency` | Structural offensive / breaking contribution before weapon multipliers |
| `processing_state` | Raw, processed, refined, alchemical, or another defined state |
| `valid_domains` | Which specializations can extract, process, or fabricate with it |
| `conservation_profile` | Whether it decays, how quickly, and what preservation is required |
| `material_state` | Whether the material is inert, organic, living, or another authored state |

### Material families

At the framework level, materials should usually belong to one of these broad families:

- creature parts
- metals
- minerals and stone
- woods
- fibers and textiles
- leather and processed hide
- fluids and glands
- organs and sensitive biological components
- plants and fungi
- precious stones and fine-setting materials

Sub-families and named catalogs can expand later, but authored materials should still inherit from a stable family.

### Material state

Family tells us **what** the material broadly is.
State tells us **how it behaves**.

At the framework level, materials should usually be authored through a stable state model.

Recommended core states:

| State | Meaning |
| --- | --- |
| `inert` | Structurally meaningful, but not actively self-changing |
| `organic` | Derived from living matter or biological tissue, but not itself behaviorally active |
| `living` | Actively responsive, adaptive, growing, self-adjusting, or still behaviorally alive as material |
| `tauma_reactive` | Changes behavior when exposed to Tauma, Limbo pressure, or another defined extranatural carrier |
| `tauma_impregnated` | Holds residual extranatural charge or memory without necessarily being alive |

Not every catalog needs all states immediately, but the distinction between `natural / processed / living` and `family / state` should remain stable.

### Why state matters

Two materials may belong to the same family and still behave very differently.

For example:

- a normal mineral wall may be `minerals_and_stone + inert`
- a bone plate may be `creature_parts + organic`
- a resonant fungal cord may be `plants_and_fungi + living`
- a reactive crystal seam may be `precious_stones_and_fine_setting_materials + tauma_reactive`

This is the main tool that allows the setting to feel different without requiring a unique authored subsystem for every strange material.

### Grade

Material grade is the quality band of the material instance, not the same thing as accessibility.

The base framework assumes three common authored grades:

- `1` — common
- `2` — rare
- `3` — exceptional

### Grade determination

Grade is determined at the moment of extraction and depends on the source type.

**Natural materials (Minería, Herboristería):** Roll 1d100 after a successful extraction.

| Roll | Grade |
| --- | --- |
| 01–60 | 1 — common |
| 61–85 | 2 — rare |
| 86–100 | 3 — exceptional |

**Creature parts (Medicina):** Grade is fixed by the creature's category — not rolled.

| Creature category | Part grade |
| --- | --- |
| Común | 1 — common |
| Campeón | 2 — rare |
| Elite | 3 — exceptional |

### Accessibility

Accessibility expresses how difficult the material is to correctly extract, process, identify, or work under pressure.

| Accessibility | Meaning | Default difficulty band |
| --- | --- | --- |
| `general` | Commonly worked, broadly available, or structurally forgiving | `Challenging` |
| `limited` | Less available, more delicate, or more demanding to work | `Demanding` |
| `singular` | Rare, dangerous, highly unstable, or technically extreme | `Extreme` |

Use the universal threshold table from `difficulty-thresholds.md`.
Accessibility sets the **base band**; `NR` still scales the actual task.

---

## Living Material Behaviors

Living materials should not be authored just by name.
They should be authored by what they actually do.

At the framework level, a living material should usually define one or more behavior tags.

### Common living-material behaviors

| Behavior | Meaning |
| --- | --- |
| `growth` | Expands, spreads, thickens, or accumulates over time |
| `regeneration` | Recovers integrity after damage or after a rest period |
| `shedding` | Loses layers, fragments, or outer casing as part of its normal cycle |
| `adhesion` | Clings to surfaces, bodies, seams, or tools |
| `contraction` | Tightens, folds, curls, seals, or closes when triggered |
| `pulse` | Beats, vibrates, hums, or transmits internal rhythm |
| `filtering` | Selectively passes, catches, separates, or refines a medium |
| `attunement` | Changes according to proximity, bearer state, species, or known input |
| `tauma_reactivity` | Responds when exposed to Tauma, Vestigio pressure, Vínculo logic, or Limbo-adjacent environments |
| `dependency` | Requires feeding, moisture, temperature, darkness, resonance, or another maintenance condition |

### Design rule for living materials

Living materials should feel extraordinary because they create different maintenance, extraction, fabrication, or tactical problems.

They should not automatically mean:

- stronger than all natural materials;
- always magical;
- always better equipment.

A living material may instead be:

- harder to preserve;
- easier to grow than to mine;
- self-repairing but unstable;
- useful only in one climate;
- responsive to Tauma but vulnerable outside it.

That tradeoff is what keeps them interesting.

---

## Extraction

Extraction is always resolved through the **relevant specialization**, never through `Enfoque` as a generic progress tax.

That means:

- biological extraction uses the trained domain that actually owns the operation;
- mineral extraction uses `Minería`;
- plant extraction uses `Herboristería`;
- later special cases may name another specialization explicitly if the source truly requires it.

### Extraction domains

| Source | Usual specialization |
| --- | --- |
| creature tissues, hides, organs, glands, fluids | `Medicina` |
| mineral seams, ore, stone, compacted structural earth | `Minería` |
| plants, fungi, botanical reagents | `Herboristería` |

### Extraction requirements

Extraction normally needs all of the following:

- valid physical access to the source;
- a relevant tool or kit;
- enough remaining integrity in the source;
- the relevant specialization at a credible rank;
- a task threshold based on accessibility, source condition, and pressure.

### Tool grades

Tools and kits gate what can be extracted safely and efficiently.

At the framework level, tools should usually come in three broad bands:

- `basic`
- `advanced`
- `specialized`

Higher-grade tools may do one or more of the following when a catalog or subsystem says so:

- permit working higher-grade material safely;
- reduce extraction time;
- increase reliable yield;
- reduce spoilage or self-contamination risk.

### Extraction outputs

An extraction procedure should define:

- what unit it produces (`kg`, `unit`, `vial`, `sample`, etc.);
- what damages or ruins the source;
- how source size or body size scales yield;
- whether failure costs time only, damages yield, or creates danger.

The exact numeric yields belong to later catalogs, not to this framework.

---

## Creature Parts

Creature parts are one of the clearest natural-material layers in the game.

They already carry:

- extraction pressure;
- biological contamination risk;
- poison exposure risk;
- conservation demands;
- and later refinement or alchemical value.

### Base creature-part catalog

The baseline creature-part catalog uses `q` as the material grade of the extracted part.

| Material | Unit | Durability | Base Potency | Cost / unit at grade 1 |
| --- | --- | --- | --- | --- |
| Pelaje | kg | `4 × q` | `2 × q` | `10 × q` |
| Escamas | kg | `16 × q` | `4 × q` | `20 × q` |
| Caparazón | kg | `22 × q` | `5 × q` | `30 × q` |
| Plumaje | kg | `3 × q` | `1 × q` | `10 × q` |
| Huesos | kg | `10 × q` | `8 × q` | `16 × q` |
| Cuernos | kg | `12 × q` | `14 × q` | `16 × q` |
| Garras | kg | `8 × q` | `16 × q` | `16 × q` |
| Colmillos | kg | `10 × q` | `18 × q` | `16 × q` |
| Glándulas | unit | `2` | `0` | `30 × q` |
| Órganos | unit | `2` | `0` | `40 × q` |
| Fluidos | liter | `2` | `0` | `20 × q` |
| Sistema nervioso | unit | `1` | `0` | `150 × q` |

### Sensitivity groups

Creature parts should be split into two extraction groups:

| Group | Parts | Extraction logic |
| --- | --- | --- |
| `non_sensitive` | pelaje, escamas, caparazón, plumaje, huesos, cuernos, garras, colmillos | bulk structural extraction; usually measured in `kg` |
| `sensitive` | glándulas, órganos, fluidos, sistema nervioso | precision extraction; usually measured in `units` or `liters` |

### Extraction specialization

The default extraction specialization for creature parts is `Medicina`.

This is not because the process is “healing,” but because the trained domain is anatomical access, safe cutting, separation, preservation-aware handling, and damage control while opening a body.

### Tool requirement

Creature-part extraction normally requires a valid extraction kit.

Tool grade controls:

- which material grades can be extracted safely;
- time reduction;
- extraction-roll bonus.

| Tool grade | Can safely extract up to | Time reduction | Roll bonus |
| --- | --- | --- | --- |
| `basic` | grade `1` | `0%` | `+0` |
| `advanced` | grade `2` | `25%` | `+1` |
| `specialized` | grade `3` | `50%` | `+2` |

A `basic` kit should not safely extract rare or exceptional creature-part material by default.

### Extraction time and yield

#### Sensitive parts

| Creature size | Base time | Base yield |
| --- | --- | --- |
| Small | `120 min` | `1 unit` |
| Medium | `240 min` | `2 units` |
| Large | `360 min` | `3 units` |
| Huge | `480 min` | `4 units` |
| Gigantic | `600 min` | `5 units` |

#### Non-sensitive parts

| Creature size | Base time | Base yield |
| --- | --- | --- |
| Small | `60 min` | `2 kg` |
| Medium | `120 min` | `4 kg` |
| Large | `240 min` | `8 kg` |
| Huge | `360 min` | `15 kg` |
| Gigantic | `480 min` | `25 kg` |

### Extraction threshold

For creature parts, the default extraction threshold should be:

```text
accessibility base + creature level / NR pressure
```

Use the material's accessibility as the base band, then scale the actual threshold by the creature's level or equivalent encounter pressure.

### Extraction risk

Creature-part extraction is one of the main natural interfaces for `Infection` and `Poison` pressure.

It should therefore use risk by part family rather than by bespoke infection name at the framework layer.

#### Infection-facing extraction

These parts usually expose the extractor to biological contamination, parasites, rot, residue, or internal filth:

- pelaje
- escamas
- plumaje
- órganos
- fluidos

Default risk rule:

| Extracted grade | Default Infection pressure |
| --- | --- |
| common | `Minor` |
| rare | `Moderate` |
| exceptional | `Severe` |

This pressure calls for an `Infection R.R.` when the fiction supports real contamination risk.

#### Poison-facing extraction

These parts usually expose the extractor to venom, toxin sacs, contaminated edges, or active delivery structures:

- colmillos
- glándulas
- garras

Default risk rule:

| Extracted grade | Default Poison pressure |
| --- | --- |
| common | `Minor` |
| rare | `Moderate` |
| exceptional | `Severe` |

This pressure calls for a `Poison R.R.` when the fiction supports real toxin exposure.

### Failure guidance

On failed extraction, the default framework outcomes should usually be one or more of:

- time spent with no valid yield;
- reduced yield;
- reduced grade;
- spoiled sample;
- triggered Infection pressure;
- triggered Poison pressure;
- damage to a later-use-sensitive part.

The exact mix can be set by later catalogs or creature entries.

---

## Natural Craft Materials

Beyond creature parts, the world needs a stable craft-material layer that supports ordinary fabrication.

These materials should remain legible, familiar, and mechanically useful before the game asks players to learn stranger living-material cases.

### Core craft domains

At the framework level, the ordinary craft-material layer is mainly distributed through:

| Specialization | Usual material space |
| --- | --- |
| `Minería` | ores, raw stone, coal, quarry materials, and extractable mineral-bearing sources |
| `Herrería` | metals, alloys, forged plate, worked mineral feed such as glass, and some armor-grade creature composites |
| `Sastrería` | fibers, cloth, leather, hide-derived materials, and flexible protective composites |
| `Joyería` | precious stones, fine-setting materials, and precision decorative or symbolic craft matter |
| `Ingeniería` | structural use of already-worked materials rather than primary extraction of them |

### Base natural-material catalog

The baseline natural-material catalog uses `q` as the material grade when the material scales by grade.

#### Metals

| Material | Durability | Base Potency | Cost / kg at grade 1 |
| --- | --- | --- | --- |
| Hierro | `14` | `12` | `10 × q` |
| Bronce | `12` | `11` | `15 × q` |
| Cobre | `8` | `8` | `10 × q` |
| Estaño | `5` | `5` | `20 × q` |
| Acero | `20` | `18` | `30 × q` |
| Peltre | `8` | `7` | `12 × q` |
| Plata | `10` | `9` | `40 × q` |
| Platino | `12` | `14` | `120 × q` |
| Oro | `6` | `10` | `100 × q` |
| Cromo | `22` | `12` | `60 × q` |
| Plomo | `6` | `14` | `15 × q` |
| Titanio | `32` | `18` | `200 × q` |
| Mithril | `28` | `45` | `500 × q` |
| Adamantium | `30` | `50` | `1000 × q` |
| Oricalco | `25` | `40` | `800 × q` |

#### Stone and precious materials

| Material | Type | Durability | Base Potency | Cost / kg at grade 1 |
| --- | --- | --- | --- | --- |
| Piedra | rock | `10` | `10` | `5 × q` |
| Roca | rock | `10` | `10` | `5 × q` |
| Carbón | rock | `5` | `10` | `5 × q` |
| Ámbar | rock | `4` | `8` | `20 × q` |
| Coral | rock | `6` | `10` | `20 × q` |
| Obsidiana | rock | `6` | `22` | `40 × q` |
| Vidrio | rock | `3` | `8` | `8 × q` |
| Lapislázuli | precious_stone | `8` | `7` | `30 × q` |
| Cuarzo | precious_stone | `10` | `10` | `20 × q` |
| Cristales | precious_stone | `10` | `9` | `30 × q` |
| Jade | precious_stone | `20` | `8` | `150 × q` |
| Topacio | precious_stone | `13` | `13` | `120 × q` |
| Esmeralda | precious_stone | `13` | `12` | `170 × q` |
| Corindón | precious_stone | `16` | `16` | `140 × q` |
| Diamante | precious_stone | `12` | `26` | `250 × q` |
| Marfil | precious_material | `7` | `13` | `40 × q` |

#### Woods

| Material | Durability | Base Potency | Cost / kg at grade 1 |
| --- | --- | --- | --- |
| Pino | `7` | `4` | `5 × q` |
| Roble | `12` | `7` | `10 × q` |
| Arce | `10` | `6` | `12 × q` |
| Caoba | `9` | `6` | `15 × q` |
| Ébano | `16` | `8` | `20 × q` |
| Secoya | `22` | `7` | `60 × q` |

#### Fibers and hide-derived materials

| Material | Type | Durability | Base Potency | Cost / kg at grade 1 |
| --- | --- | --- | --- | --- |
| Lana | fiber | `3 × q` | `1 × q` | `12 × q` |
| Lino | fiber | `4 × q` | `2 × q` | `10 × q` |
| Algodón | fiber | `2 × q` | `1 × q` | `8 × q` |
| Seda | fiber | `6 × q` | `2 × q` | `20 × q` |
| Yute | fiber | `4 × q` | `2 × q` | `6 × q` |
| Seda de Arakhel | fiber | `18 × q` | `5 × q` | `120 × q` |
| Tela | fiber | `4 × q` | `1 × q` | `8 × q` |
| Cuero | leather | `10 × q` | `3 × q` | `18 × q` |
| Cuero escamado | leather | `14 × q` | `4 × q` | `30 × q` |
| Cuero acorazado | leather | `9 × q` | `10 × q` | `35 × q` |

### Processed materials

Processed materials are the ordinary conversion layer between raw inputs and finished gear.

| Processed material | Source | Domain | Durability | Base Potency | Cost logic |
| --- | --- | --- | --- | --- | --- |
| Cuero | pelaje | `Sastrería` | `10 × q` | `3 × q` | `18 × q × qty` |
| Escamado | escamas | `Herrería` | `14 × q` | `4 × q` | `30 × q × qty` |
| Acorazado | caparazón | `Herrería` | `11 × q` | `7 × q` | `35 × q × qty` |
| Tela | fiber source | `Sastrería` | `material + q` | `material + q` | `material × 0.2 × q × qty` |
| Bronce | cobre + estaño | `Herrería` | `12` | `20` | `20 × q × qty` |
| Acero | hierro + carbón | `Herrería` | `18` | `30` | `30 × q × qty` |
| Peltre | estaño | `Herrería` | `8` | `15` | `15 × q × qty` |
| Vidrio | mineral / sand feed | `Herrería` | `5` | `10` | `8 × q × qty` |

These entries define the ordinary processed layer.
They do not prevent later living-material or tauma-reactive processed variants.

### Accessibility

Accessibility is one of the most important balancing surfaces in the material system because it affects:

- extraction difficulty;
- fabrication difficulty;
- labor cost;
- work time;
- minimum credible kit.

#### Accessibility tiers

| Tier | Label | Base threshold model | Difficulty band | Labor cost / kg | Default fabrication time | Minimum kit |
| --- | --- | --- | --- | --- | --- | --- |
| `general` | High | `8 + creature level / NR pressure` | `Challenging` | `15 × grade` | `1 week` | `basic` |
| `limited` | Medium | `13 + creature level / NR pressure` | `Demanding` | `45 × grade` | `2 weeks` | `advanced` |
| `singular` | Low | `17 + creature level / NR pressure` | `Extreme` | `150 × grade` | `3 weeks` | `specialized` |

The exact threshold still follows the universal system.
The table above establishes the baseline authored expectation for material work.

#### Baseline accessibility by material

##### General

- Bronce
- Hierro
- Cobre
- Estaño
- Vidrio
- Ámbar
- Pino
- Plomo
- Roble
- Caoba
- Arce
- Piedra
- Roca
- Carbón
- Coral
- Peltre
- Oro
- Pelaje
- Plumaje
- Cuernos
- Garras
- Fluidos
- Tela
- Seda
- Lana
- Algodón
- Lino
- Yute

##### Limited

- Cromo
- Acero
- Plata
- Platino
- Cristales
- Ébano
- Marfil
- Lapislázuli
- Cuarzo
- Escamas
- Caparazón
- Huesos
- Colmillos
- Glándulas
- Órganos
- Cuero
- Escamado
- Acorazado

##### Singular

- Secoya
- Mithril
- Adamantium
- Titanio
- Oricalco
- Obsidiana
- Seda de Arakhel
- Jade
- Corindón
- Esmeralda
- Diamante
- Topacio
- Sistema nervioso

### Domain note

`Minería` extracts much of this raw layer.
`Herrería`, `Sastrería`, and `Joyería` transform it.
`Ingeniería` more often uses already-worked material in structural or functional assembly rather than owning the base raw catalog by itself.

---

## Conservation

Not all materials persist equally once extracted.

### Conservation rule

Every material should belong to one of three conservation classes:

| Class | Meaning |
| --- | --- |
| `stable` | Does not meaningfully decay in normal storage |
| `perishable` | Decays over time unless preserved correctly |
| `volatile` | Decays quickly, destabilizes, or becomes unsafe without immediate handling |

### General guidance

- minerals, stone, and most metals are usually `stable`
- hides, fluids, organs, glands, and many plant reagents are usually `perishable`
- nerve tissue, unstable glands, fresh venoms, and similar materials are often `volatile`

Preservation should require the correct kit, medium, or storage condition when the catalog says so.

Living materials may also require **maintenance** rather than simple storage.
Maintenance can include:

- moisture;
- darkness;
- circulation;
- feeding medium;
- resonance exposure;
- taumatic quiet or taumatic charge;
- species-specific handling.

Without valid preservation, the material should eventually:

- lose usable time;
- drop in grade;
- become invalid for a specific process;
- or become unsafe to handle.

### Creature-part conservation profiles

Creature parts are one of the places where conservation matters most.

At the framework level, the following profiles are the default baseline:

| Part | Kit | Conservation time in favorable conditions | Baseline requirement |
| --- | --- | --- | --- |
| Pelaje / Plumaje | `basic` | `1 month` | dry, cool storage away from humidity |
| Escamas / Caparazón | `advanced` | `2 months` | clean organic residue and store dry |
| Colmillos / Garras | `basic` | `6 weeks` | dry fully and keep at low humidity |
| Huesos / Cuernos | `advanced` | `2 months` | remove soft tissue and treat with preservative |
| Glándulas / Órganos | `specialized` | `1 week` | preserve in saline, alcohol, or equivalent medium |
| Fluidos | `basic` | `2 weeks` for blood, `1 month` for venom-class fluids | sealed isolated containers |
| Sistema nervioso | `specialized` | `3 days` | controlled preservation in specialized medium |

These are default framework expectations, not yet the full biological catalog.
Individual creatures, living-material cases, or tauma-reactive tissues may override them.

---

## Fabrication

Fabrication is the process of turning valid materials into usable equipment, structures, or authored objects.

It is never governed by `Enfoque` as the primary production roll.
The qualifying roll is always the specialization that actually owns the work.

Natural materials should carry most standard fabrication.
Processed materials define the ordinary transformation layer.
Living materials should usually require one of these extra authored constraints:

- special handling rule;
- maintenance condition during fabrication;
- narrower valid domains;
- narrower valid outputs;
- or a specific environmental requirement.

### Fabrication domains

| Output family | Usual specialization |
| --- | --- |
| forged weapons, metal armor, worked plate, structural metal parts | `Herrería` |
| cloth armor, garments, leatherwork, flexible gear | `Sastrería` |
| fine-setting, gemstone work, ornaments, precision adornment | `Joyería` |
| kits and tools for all other specializations; creature harnesses and riding equipment; exploration tools; equipment for operating on gigantic-scale creatures | `Ingeniería` |
| prepared compounds, elixirs, poisons, alchemical products | `Alquimia` |

### Fabrication requirements

A fabrication process should normally define:

- valid plan, design, or known recipe;
- valid material inputs;
- valid tools, workshop, or kit;
- responsible specialization;
- work time;
- labor cost;
- difficulty band.

### Work intervals

Fabrication should be resolved in **work intervals** owned by the relevant specialization.

The framework does not force hourly rolls.
Instead, each authored process should define its own meaningful interval, such as:

- one stage;
- one session;
- one workday;
- one formula cycle;
- one structural pass.

On a failed roll, the default outcome should usually be:

- time is spent;
- no meaningful progress is made;
- and optional material stress or waste may occur if the authored process says so.

### Complexity and plans

Plans, diagrams, and recipes should define the expected complexity of the work.

At the framework level, complexity usually belongs to one of three bands:

- `simple`
- `complex`
- `advanced`

Complexity changes:

- total work required;
- threshold band;
- tool expectations;
- and whether the process can be improvised at all.

### Equipment material requirements

#### Weapons

Each weapon type has required components with specific material families and weight.
A component classified as `metal` may use any valid metallic material. A component classified as `wood` may use any valid wood. A component classified as `fiber` may use any valid fiber or leather.

| Weapon type | Component | Material | kg required |
| --- | --- | --- | --- |
| **Polearm** | Shaft | Wood | 5 |
| | Blade | Metal | 2 |
| **Two-handed spear** | Shaft | Wood | 4 |
| | Point | Metal | 2 |
| **One-handed spear** | Shaft | Wood | 2 |
| | Point | Metal | 1 |
| **Two-handed axe** | Handle | Wood | 3 |
| | Blade | Metal | 2 |
| **One-handed axe** | Handle | Wood | 2 |
| | Blade | Metal | 1 |
| **Two-handed mace** | Handle | Wood or metal | 3 |
| | Head | Metal | 3 |
| **One-handed mace** | Handle | Wood or metal | 1 |
| | Head | Metal | 1 |
| **Two-handed longsword** | — | Metal | 3 |
| **One-handed longsword** | — | Metal | 2 |
| **Shortsword** | — | Metal | 1 |
| **Dagger** | — | Metal | 1 |
| **Kunai / Shuriken (×3)** | — | Metal | 1 |
| **Pilum / Francisca** | Handle | Wood | 1 |
| | Blade | Metal | 2 |
| **Bow / Blowgun** | Body | Wood | 1 |
| **Sling (balearic)** | Body | Fiber | 1 |
| **Kusarigama / Kusari Fundo** | — | Metal | 2 |
| **Nekode (×2)** | — | Metal | 1 |
| **Whip (scourge)** | — | Fiber | 3 |

#### Armor

Armor is fabricated piece by piece. Total material depends on how many pieces are produced and their class.

**kg of material per piece and class:**

| Piece | Light | Medium | Heavy |
| --- | --- | --- | --- |
| Helmet | 1 kg | 2 kg | 3 kg |
| Chest | 3 kg | 6 kg | 9 kg |
| Legs | 2 kg | 4 kg | 6 kg |
| Bracers | 2 kg | 3 kg | 4 kg |
| Boots | 1 kg | 2 kg | 3 kg |
| **Full set total** | **9 kg** | **17 kg** | **25 kg** |

**Valid materials by armor class:**

| Class | Valid materials |
| --- | --- |
| Light | Leather, cloth, creature leather, titanium |
| Medium | Iron, copper, bronze, pewter, obsidian, scaled leather |
| Heavy | Steel, lead, silver, gold, platinum |

Tauma-impregnated materials of any category may be valid according to their structural equivalent — the Narrator evaluates case by case.

#### Shields

| Class | kg of material | Valid materials |
| --- | --- | --- |
| Light | 3 kg | Leather, oak, pine, mahogany, maple, titanium |
| Medium | 7 kg | Iron, copper, bronze, pewter, scaled leather |
| Heavy | 11 kg | Steel, lead, silver, gold, platinum |

---

## Refinement

Refinement is **not** the same thing as base fabrication.

Fabrication creates the object.
Refinement modifies a finished or at least already-valid object by adding another material layer, usually to grant a specific authored property.

### Refinement rule

Refinement should always define:

- the base object it can modify;
- the extra material it consumes;
- the specialization that performs the refinement;
- the time requirement;
- the difficulty band;
- and the exact granted property.

### Allowed refinement outputs

A refinement may alter one or more of these surfaces if the authored entry says so:

- durability
- base potency
- critical break behavior
- resistance or vulnerability trait
- protection profile
- delivery profile
- named equipment property

Refinement should not become a freeform “add any monster part to get any bonus” layer.
Each valid refinement needs its own authored rule.

---

## Alchemy and Plants

Alchemy is a fabrication-adjacent system, but it should stay distinct because its output is not generic gear.

### Alchemy

Alchemy should be authored through:

- a formula or recipe;
- reagent requirements;
- plant or biological inputs;
- an alchemical index or complexity measure;
- a delivery route if the output is ingested, inhaled, inoculated, or applied by contact.

The qualifying roll is `Alquimia`, not a generic concentration check.

### Two-stage production

Alchemical production has two distinct stages with different infrastructure requirements.

**Stage 1 — Index preparation (field):** Grinding glands, isolating toxins, and stabilizing raw biological material before it spoils. This can be done in the field with a portable alchemical kit. A character may prepare their indices during an expedition and complete synthesis on return.

**Stage 2 — Compound synthesis (fixed workshop):** Combining and reacting the prepared indices into a finished compound. Always requires a fixed installation — a still, a furnace, or an equivalent alchemical workbench. Cannot be performed in the field.

### Fabrication difficulty by reagent

The difficulty of the synthesis roll is set by the creature reagent the formula requires.

| Creature reagent | Accessibility | Fabrication difficulty |
| --- | --- | --- |
| Fluids | General | Challenging |
| Glands | Limited | Demanding |
| Organs | Limited | Demanding |
| Nervous system | Singular | Extreme |

### Plants

Plants are sourcing inputs, not just item flavor.

Plant entries should eventually define:

- accessibility;
- extraction time;
- alchemical index contribution if relevant;
- primary use family;
- conservation behavior.

The qualifying extraction roll is `Herboristería`.

### Plant accessibility

At the framework level, plant extraction should use a compact accessibility model parallel to other material sourcing.

| Accessibility | Extraction difficulty band | Base extraction time | Minimum kit |
| --- | --- | --- | --- |
| `high` | `Fundamental` | `15 min` | `basic` |
| `medium` | `Rigorous` | `30 min` | `advanced` |
| `low` | `Extreme` | `60 min` | `specialized` |

This accessibility expresses how difficult the plant is to correctly identify, reach, and harvest without ruining the useful part.

### Alchemical Index

Plants and fungi that matter to `Alquimia` should usually define an **Alchemical Index**.

The Alchemical Index is not just rarity.
It is a compact way to express how much alchemical weight, complexity, or catalytic value an input contributes when used in a formula.

At the framework level, lower values should usually represent:

- simpler extraction;
- more common herbal or restorative use;
- lower-complexity compounds.

Higher values should usually represent:

- stronger toxic or transformative potential;
- rarer preparation logic;
- more demanding formula work;
- greater risk if mishandled.

### Baseline plant catalog

The plant layer should remain mostly natural and reality-readable at baseline.
That gives players something graspable before the setting asks them to learn stranger living botanical cases.

#### High accessibility plants

| Plant | Alchemical Index | Cost / unit | Base extraction time |
| --- | --- | --- | --- |
| Lavanda | `2` | `4` | `15 min` |
| Orégano | `2` | `4` | `15 min` |
| Ortiga | `3` | `6` | `15 min` |
| Melisa | `3` | `6` | `15 min` |
| Consuelda | `4` | `8` | `15 min` |
| Verbena | `4` | `8` | `15 min` |
| Achillea | `4` | `8` | `15 min` |
| Matricaria | `4` | `8` | `15 min` |
| Hypericum | `4` | `8` | `15 min` |
| Echinacea | `4` | `8` | `15 min` |
| Enebro | `4` | `8` | `15 min` |
| Borraja | `4` | `8` | `15 min` |
| Equisetum | `4` | `8` | `15 min` |

#### Medium accessibility plants

| Plant | Alchemical Index | Main use | Cost / unit |
| --- | --- | --- | --- |
| Pasiflora | `4` | elixir | `8` |
| Escutelaria | `4` | elixir | `8` |
| Pleurotus | `4` | elixir | `8` |
| Ajenjo | `5` | elixir | `10` |
| Silybum | `5` | elixir | `10` |
| Smilax | `5` | elixir | `10` |
| Cúrcuma | `5` | elixir | `10` |
| Tricholoma | `5` | elixir | `10` |
| Lactarius | `5` | elixir | `10` |
| Divinorum | `6` | both | `12` |
| Rhodiola | `6` | elixir | `12` |
| Chaga | `6` | elixir | `12` |
| Dealbata | `6` | poison | `12` |
| Gyromitra | `6` | poison | `12` |
| Dedalera | `7` | poison | `12` |
| Papaver | `7` | elixir | `14` |
| Amanita muscaria | `7` | both | `14` |
| Psilocybe | `7` | both | `14` |

#### Low accessibility plants

| Plant | Alchemical Index | Main use | Cost / unit |
| --- | --- | --- | --- |
| Artemisa | `5` | elixir | `10` |
| Cordyceps | `8` | elixir | `16` |
| Acónito | `8` | poison | `15` |
| Estramonio | `8` | both | `16` |
| Mandragora | `9` | both | `18` |
| Boletus | `9` | poison | `18` |
| Belladona | `9` | poison | `18` |
| Ricino | `9` | poison | `18` |
| Cicuta | `10` | poison | `20` |
| Adelfa | `10` | poison | `20` |
| Taxus | `10` | poison | `20` |

### Design rule for plant use

`Herboristería` owns:

- identification;
- harvesting;
- basic preparation;
- field-safe handling;
- judging whether a plant is useful for a medicinal or material purpose.

`Alquimia` owns:

- transformation into compounds;
- formula execution;
- concentration, distillation, and reaction logic;
- final alchemical product.

That means the same plant may belong to both systems without collapsing them into one skill.

---

## Tools, Kits, and Work Infrastructure

Fabrication does not happen in an abstract void.
It depends on the physical interface between an artisan and the material.

At the framework level, that interface should be split into:

- tools;
- kits;
- heavy work infrastructure;
- plans and diagrams.

### Objects

Objects are tangible made things.
They may be utilitarian, symbolic, structural, or precision-focused.

For fabrication purposes, the important distinction is not “is it an object,” but what kind of production support it provides:

- portable tool;
- consumable kit;
- fixed work infrastructure;
- specialized device.

### Artifacts

Artifacts are not the baseline assumption of the production system.
They are exceptional made things that combine matter, authored construction, and a powered elemental or extranatural function.

For this layer, the important rule is simple:

- ordinary fabrication should assume `objects`, not `artifacts`;
- an artifact version of a tool family may exist later as an upgrade or exceptional variant;
- and an artifact should never replace the need to define the ordinary tool, kit, or infrastructure it is derived from.

That keeps the everyday economy readable while still leaving room for extraordinary workshop technology later.

### Tools

Tools are reusable implements that let a trained specialization act on matter with control.

They should usually be divided into:

| Tool class | Meaning |
| --- | --- |
| `light_tool` | Portable, routine, low-scale, and broadly usable within the owning specialization |
| `heavy_tool` | Larger, more stable, more precise, or more force-capable equipment for demanding work |
| `specialized_tool` | Narrow-purpose precision implement that enables one exact type of work |

### Kits

Kits are compact, domain-specific, partially consumable work bundles.

They matter because they combine:

- portability;
- domain access;
- limited uses;
- and lower setup demands than fixed infrastructure.

#### Kit rule

A kit should usually define:

- owning specialization or action family;
- grade;
- uses;
- portability;
- whether it is enough by itself or only for field work and minor jobs.

#### Kit grades

| Grade | Meaning |
| --- | --- |
| `1` | basic |
| `2` | advanced |
| `3` | specialized |

#### Kit rank bands

All kit families use the same three-grade ladder.
At the framework level, those grades map to competency-rank bands as follows:

| Kit grade | Competency-rank expectation | Typical rank bands |
| --- | --- | --- |
| `1` | baseline field and apprentice-professional work | `Novice` / `Adept` |
| `2` | advanced professional work | `Expert` / `Master` |
| `3` | peak or near-peak specialized work | `Consummate` / `Transcendent` |

This mapping is global.
It applies to all kit-governed processes, whether they belong to a specialization directly or to a narrower support practice such as extraction or conservation.

Unless a more specific subsystem rule says otherwise:

- cost scales with grade;
- uses scale with grade;
- portability stays roughly constant;
- grade determines the ceiling of safe or credible work;
- `basic` kits normally support `Novice` and `Adept` work;
- `advanced` kits normally support `Expert` and `Master` work;
- and `specialized` kits normally support `Consummate` and `Transcendent` work.

This does not mean lower-rank characters are forbidden from touching a better kit.
It means the system should assume that high-rank work normally requires the matching kit band unless a narrower process rule explicitly relaxes that requirement.

#### Kit allocation rule

Every production-facing discipline that routinely acts on matter should normally have a kit family.

That includes two different cases:

- a full specialization whose domain regularly requires physical handling, preparation, shaping, treatment, assembly, or measurement;
- a support practice that is not broad enough to stand alone as a specialization, but still needs dedicated tools to be used safely or credibly in play.

This means the system should not only author kits for the major arts and crafts.
It should also author kits for narrower support practices when those practices create a meaningful handling gate.

#### Specialization-owned kit families

At baseline, the following production-facing specializations should each have a graded kit family:

| Discipline | Baseline kit family |
| --- | --- |
| `Medicina` | medical kits |
| `Herboristería` | herboristry kits |
| `Alquimia` | alchemical kits |
| `Trampas` | trapmaking kits |
| `Minería` | mining kits |
| `Herrería` | smithing kits |
| `Sastrería` | tailoring kits |
| `Joyería` | jeweler's kits |
| `Ingeniería` | engineering kits |

These kits express portable access to the domain.
They do not automatically replace the need for heavy work infrastructure when the scale, precision, or throughput of the job is too large for field tools.

#### Support-practice kit families

Some practices are better treated as kit families than as standalone specializations.

Good baseline examples include:

- extraction kits;
- conservation kits;
- poison-handling kits;
- repair kits;
- mineral-refinement kits;
- fiber-refinement kits;
- surveying and appraisal kits;
- cartography kits;
- and projectile-fletching kits for arrow, bolt, and other ammunition adjustment, recovery, maintenance, and payload fitting.

These support-practice kits should usually be rolled through the owning or nearest credible specialization for the actual work:

- `Medicina` for extraction and some preservation-sensitive biological handling;
- `Herboristería` or `Alquimia` for botanical and compound-sensitive handling;
- `Herrería`, `Sastrería`, `Joyería`, or `Ingeniería` for repair and refinement depending on the material;
- `Identificación`, `Geografía`, or another future knowledge domain when surveying, appraisal, or cartographic interpretation is the real skill being tested;
- and the most relevant projectile or crafting domain when fitting arrows, bolts, or other ammunition.

#### Baseline kit families

Before authoring named products, the system should assume a small set of common kit families:

- medical kits;
- herboristry kits;
- alchemical kits;
- trapmaking kits;
- mining kits;
- smithing kits;
- tailoring kits;
- jeweler's kits;
- engineering kits;
- extraction kits;
- conservation kits;
- poison-handling kits;
- repair kits;
- mineral-refinement kits;
- fiber-refinement kits;
- dye and finishing kits;
- surveying and appraisal kits;
- cartography kits;
- projectile-fletching kits.

These are enough to support most field and workshop play before the catalog grows into specific regional or factional variants.

### Heavy work infrastructure

Some processes should require more than a portable kit.

Heavy work infrastructure covers things like:

- forge bodies;
- anvils;
- cutting tables;
- leather presses;
- alchemical distillation apparatus;
- jewelry furnaces;
- fixed precision benches;
- structural engineering work surfaces.

These are usually:

- non-consumable;
- fixed or semi-fixed;
- harder to transport;
- and better suited for long work, complex work, or high-throughput work.

#### Baseline infrastructure families

Common authored families should usually include:

- forge assemblies;
- anvils and shaping surfaces;
- cutting and measuring tables;
- leather presses and stretching frames;
- furnaces and kilns;
- distillation and reaction benches;
- precision setting benches;
- and larger structural work surfaces.

### Specialized objects

Some objects are not broad workshop tools, but purpose-built devices for one narrow class of work.

Examples of framework roles:

- extraction support;
- conservation support;
- poison handling;
- repair support;
- surveying / appraisal;
- cartography;
- trap assembly;
- refinement support.

These should be authored as tool families or kit families before they are authored as hundreds of individual named products.

### Creature harnesses and riding equipment

Harnesses and riding equipment are `Ingeniería`-produced systems for controlling, transporting, or operating on captured or domesticated creatures. They are not personal-use tools — they are purpose-built for a specific creature size.

Creature harness scope:

- **Control harnesses** — head, neck, and body harnesses for directing the creature during movement
- **Load systems** — saddles, platforms, and containers for transporting weight on the creature
- **Restraint equipment** — mechanisms for immobilizing a creature during Medicina procedures or extraction

Creature size determines minimum harness complexity:

| Creature size | Minimum harness complexity |
| --- | --- |
| Small | Simple |
| Medium | Simple |
| Large | Complex |
| Huge | Complex |
| Gigantic | Advanced |

### Equipment for operation on gigantic-scale creatures

A gigantic-scale creature is not just a large enemy — it is a hostile environment in motion. Its body surface may be the terrain for entire missions. `Ingeniería` produces the specialized systems that make this possible:

- **Anchor hooks and cables** — for securing position while scaling thick skin, membranes, or chitin plates
- **Portable work platforms** — collapsible structures that deploy at anchor points for stable work without constant grip
- **Traction systems** — mechanisms for ascending or moving along the creature's exterior surface without constant effort expenditure
- **Assisted drilling instruments** — for reaching internal zones without generic extraction tools

Each system requires its own authored Plan. The Narrator determines which are available in the world and at what cost.

---

## Plans, Diagrams, and Recipes

The production system should distinguish between:

- plans;
- trap diagrams;
- formulas.

They are related, but they do not solve the same problem.

### Plans

Plans govern the fabrication of physical tools, structures, and manufactured objects.

At the framework level, a plan should usually define:

- output class;
- complexity;
- required domains;
- required materials;
- expected labor;
- expected work time;
- availability.

#### Plan complexity (infrastructure and tools)

Plans for infrastructure, tools, and kits use this cost structure:

| Complexity | Difficulty band | Base market cost |
| --- | --- | --- |
| `simple` | `Fundamental` | `50 Shekels` |
| `complex` | `Rigorous` | `200 Shekels` |
| `advanced` | `Extreme` | `600 Shekels` |

#### Fabrication time for plans

Work time for a plan-governed object follows this formula:

> **Hours = Object weight (kg) × Maximum material grade × Complexity factor**

| Complexity | Factor |
| --- | --- |
| Simple | × 1 |
| Complex | × 1.5 |
| Advanced | × 2 |

**Example:** An alchemical still weighs 10 kg, uses grade-2 materials, complex complexity: 10 × 2 × 1.5 = **30 hours**.

**Example:** A tailoring kit weighs 2 kg, grade-1 materials, simple complexity: 2 × 1 × 1 = **2 hours**.

#### Availability surcharge

| Availability | Added cost |
| --- | --- |
| `common` | `0` |
| `moderate` | `100` |
| `specialized` | `200` |
| `rare` | `300` |
| `exceptional` | `400` |

#### Equipment designs

Equipment designs (weapons, armor, shields, jewelry) use a separate, lower cost structure than infrastructure plans. They are authored and used by the crafting specialization that produces the object, not by Ingeniería.

| Complexity | Difficulty band | Base market cost |
| --- | --- | --- |
| `simple` | `Fundamental` | `50 Shekels` |
| `complex` | `Rigorous` | `80 Shekels` |
| `advanced` | `Extreme` | `100 Shekels` |

Equipment design availability uses the same surcharge table as infrastructure plans.

#### Design families

Some plans are not one-off blueprints but reusable design families.
These are especially useful for equipment that shares a common production grammar but differs in visual identity or battlefield profile.

Good baseline examples include:

- thrown and ranged weapon designs;
- hafted weapon designs;
- flexible weapon designs;
- light, medium, and heavy armor designs;
- light, medium, and heavy shield designs;
- and jewelry design families such as pendants, amulets, and insignia.

This lets the system distinguish between:

- the right to fabricate a class of object;
- the specific profile or visual design being used;
- and the material choice used for that fabrication.

### Trap diagrams

Trap diagrams are the plan-equivalent layer for traps.

They should usually define:

- trap type;
- rarity / complexity;
- construction time;
- build difficulty;
- detection difficulty;
- disarm difficulty;
- and whether a specialized reagent or subsystem is required.

#### Trap diagram rarity

| Rarity | Build time | Build difficulty | Detect difficulty | Disarm difficulty | Labor cost | Material cost |
| --- | --- | --- | --- | --- | --- | --- |
| `common` | `4 hours` | `Challenging` | `Challenging` | `Challenging` | `200 S` | `50 S` |
| `rare` | `10 hours` | `Demanding` | `Demanding` | `Demanding` | `500 S` | `150 S` |
| `exceptional` | `24 hours` | `Extreme` | `Demanding` | `Demanding` | `1,200 S` | `400 S` |

#### Trap diagram type surcharge

| Trap type | Added cost | Notes |
| --- | --- | --- |
| `mechanism` | `0` | Physical trigger, pressure plate, tensioned release |
| `illusory` | `50` | Tricks perception through natural means: perspective, camouflage, misalignment, shadow |
| `environmental` | `50` | Exploits terrain: flooding, collapse, heat, fall |
| `living` | `100` | Incorporates a living component (spore sacs, parasite nests, manipulated flora) as part of the trap logic |
| `threshold` | `250` | Tauma-impregnated materials with fixed extranatural properties; only available at rare or exceptional rarity |

### Formulas

Formulas are the recipe layer for `Alquimia`.

They should define:

- output family (`elixir`, `poison`, etc.);
- rarity;
- reagents;
- plant inputs;
- required Alchemical Index;
- and final dose logic.

At the framework level, formula rarity should usually determine baseline time and output quantity.

| Formula rarity | Build time | Default doses | Difficulty band |
| --- | --- | --- | --- |
| `common` | `12 hours` | `1d4` | `Challenging` |
| `rare` | `24 hours` | `1d3` | `Demanding` |
| `exceptional` | `36 hours` | `1d2` | `Extreme` |

#### Formula market cost

When formulas are traded as authored documents, their market value should usually be built from:

- rarity;
- output family;
- and availability.

##### Formula rarity cost

| Rarity | Base market cost |
| --- | --- |
| `common` | `50` |
| `rare` | `200` |
| `exceptional` | `600` |

##### Formula output-family surcharge

| Output family | Added cost |
| --- | --- |
| `elixir` | `50` |
| `poison` | `100` |

Use the same availability surcharge table defined for plans unless a later subsystem says otherwise.

### Authoring rule

Use:

- `plans` for tools, structures, and manufactured objects;
- `trap diagrams` for traps;
- `formulas` for alchemical compounds.

Do not collapse all three into one generic recipe object.

---

## Work Logic

The old model of “start with the main craft roll, then pay hourly Focus taxes” should not remain the default.

### Start condition

To begin meaningful work, the actor normally needs:

- the right specialization;
- the right material inputs;
- the right tools or infrastructure;
- and the relevant plan, diagram, or formula when the process is not improvised.

### Support rule

Portable kits should normally be enough for:

- field extraction;
- first-pass preservation;
- minor repairs;
- low-scale preparation;
- and other short, localized jobs.

Heavy infrastructure should normally be expected for:

- long fabrication;
- high-output processing;
- high-precision shaping;
- large objects;
- or any work whose scale would be implausible from a handheld kit alone.

### Progress rule

Progress should be tracked in meaningful work intervals owned by the relevant specialization, not by generic hourly `Enfoque` checks.

That means:

- `Herrería` advances forge work;
- `Sastrería` advances textile and leather work;
- `Joyería` advances fine-setting work;
- `Ingeniería` advances structural and mechanism work;
- `Alquimia` advances compounds;
- `Trampas` advances trap assembly;
- `Herboristería` advances plant harvesting and preparation;
- `Medicina` advances creature-part extraction and preservation-aware anatomical work.

### Failure rule

On a failed work roll, the default framework result should usually be one or more of:

- time spent with no meaningful progress;
- material stress or waste;
- reduced final yield or stability;
- contamination or handling danger if the process is biologically or chemically risky;
- blocked continuation until conditions improve.

This preserves pressure without forcing an extra universal concentration subsystem on top of every craft scene.

---

## Traps

Traps are authored objects and should usually combine:

- `Trampas` for trap logic, placement, concealment, triggering, and disarming identity;
- another specialization when the construction materially depends on that domain.

Typical pairings:

- `Trampas + Ingeniería` for mechanisms;
- `Trampas + Herrería` for forged trigger bodies or pressure devices;
- `Trampas + Alquimia` for chemical delivery traps.

The crafting framework should therefore treat trap construction as a valid fabrication branch, not as a separate reality with no material logic.

---

## Design Rule For Techniques

Techniques may interact with materials and fabrication, but this system is **not**
their primary home.

Good Technique interactions here usually look like:

- identifying the right extraction point;
- preserving volatile material under pressure;
- forcing one fast refinement step that already exists in authored rules;
- exploiting a material weakness;
- accelerating one bounded fabrication or repair window.

Bad Technique interactions here usually look like:

- replacing an entire crafting loop with one action;
- inventing material properties not defined anywhere;
- creating permanent equipment without material, tool, or plan requirements.

---

## Future Catalog Layers

This framework intentionally leaves later catalogs to define:

- exact material entries and stat tables;
- exact extraction yields by creature size or vein richness;
- exact conservation durations by material;
- exact recipes and labor costs;
- exact plant catalogs;
- exact alchemical formulas;
- exact trap diagrams;
- exact world-specific production materials and regional variants.

Those catalogs should plug into this framework rather than redefining it.

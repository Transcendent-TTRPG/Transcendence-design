# Mundane Equipment and Objects

**Authority data:** `data/system/mundane-equipment-and-objects.yaml`
**Related docs:** `docs/system/equipment-overview.md`, `docs/system/faction-reputation-and-alliances.md`, `docs/system/materials-and-fabrication.md`

---

## Purpose

This document provides the first broad catalog layer for ordinary non-magical carried goods, travel equipment, field support objects, and simple market-ready practical items.

It exists so the system can answer questions like:

- what kinds of mundane objects are normal to buy or carry;
- what category an item belongs to;
- how heavy it is;
- what its baseline price is;
- and how rare it is before faction, alliance, or regional modifiers apply.

This is **not** the full weapon and armor catalog.
Combat-facing equipment with deeper block, durability, slot, and profile logic still belongs primarily to the equipment and materials layers.

---

## Core Rule

Use this catalog for:

- ordinary adventuring gear;
- travel goods;
- basic field support items;
- mundane ammunition;
- writing, navigation, storage, and upkeep objects;
- and practical objects that do not need their own authored subsystem.

Do not use this catalog for:

- full weapon families with profile logic;
- armor pieces with slot/block logic;
- living materials;
- Vestigios or Vínculos;
- or high-identity faction-specific goods unless they are being treated as simple local variants of a mundane base object.

---

## Category Model

At the framework level, mundane objects should usually be organized into:

- `Travel Gear`
- `Camp and Sustenance`
- `Light and Observation`
- `Writing and Recordkeeping`
- `Field Utility`
- `Climbing and Access`
- `Medical and Sanitary`
- `Alchemical and Sample Handling`
- `Mundane Ammunition`
- `Packages and Loadouts`

These are catalog categories, not special mechanics by themselves.

---

## Travel Gear

| Item | Price | Availability | Weight | Notes |
| --- | --- | --- | --- | --- |
| `Travel backpack` | `30 Shekels` | `Common` | `1 kg` | Durable pack with routine travel compartments |
| `Waterskin / canteen` | `12 Shekels` | `Common` | `1 kg empty` | Standard carried water container |
| `Rain poncho` | `12 Shekels` | `Common` | `0.5 kg` | Weather protection for ordinary rain exposure |
| `Compass` | `35 Shekels` | `Moderate` | `0.3 kg` | Practical direction reference |
| `Reading glasses` | `25 Shekels` | `Common` | `0.1 kg` | Close-work aid for documents, maps, or detail tasks |

## Camp and Sustenance

| Item | Price | Availability | Weight | Notes |
| --- | --- | --- | --- | --- |
| `Bedroll` | `25 Shekels` | `Common` | `2 kg` | Standard sleep gear for moderate conditions |
| `Travel rations (1 day)` | `10 Shekels` | `Common` | `0.5 kg` | Preserved daily field food |
| `Field cook set` | `30 Shekels` | `Common` | `2 kg` | Pot, small pan, and simple cooking implements |

## Light and Observation

| Item | Price | Availability | Weight | Notes |
| --- | --- | --- | --- | --- |
| `Torch` | `10 Shekels` | `Common` | `1 kg` | Routine mobile light source |
| `Wax candles (10)` | `5 Shekels` | `Common` | `0.2 kg` | Small interior or camp light source |
| `Oil lamp` | `20 Shekels` | `Moderate` | `1 kg` | Directed and more stable light source |
| `Camouflage cloth` | `30 Shekels` | `Moderate` | `1 kg` | Mundane concealment aid for camp, stash, or equipment |

## Writing and Recordkeeping

| Item | Price | Availability | Weight | Notes |
| --- | --- | --- | --- | --- |
| `Writing kit` | `10 Shekels` | `Common` | `0.2 kg` | Ink and basic writing implements |
| `Blank journal` | `20 Shekels` | `Common` | `0.5 kg` | General record book |
| `Local territory map` | `60 Shekels` | `Moderate` | `0.1 kg` | Region-specific authored document |

## Field Utility

| Item | Price | Availability | Weight | Notes |
| --- | --- | --- | --- | --- |
| `Rope (10 m)` | `120 Shekels` | `Common` | `1.5 kg` | Standard utility rope |
| `Basic repair box` | `35 Shekels` | `Common` | `3 kg` | General minor-repair implements |
| `Whetstone` | `15 Shekels` | `Common` | `0.5 kg` | Edge upkeep and simple sharpening |
| `Mortar and pestle` | `30 Shekels` | `Moderate` | `1.5 kg` | Crushing and mixing dry or soft matter |

## Climbing and Access

| Item | Price | Availability | Weight | Notes |
| --- | --- | --- | --- | --- |
| `Climbing hooks set` | `30 Shekels` | `Specialized` | `0.8 kg` | Anchor support for ascent or secured rope work |

## Medical and Sanitary

| Item | Price | Availability | Weight | Notes |
| --- | --- | --- | --- | --- |
| `Bandages (10)` | `8 Shekels` | `Common` | `0.2 kg` | Wound covering and binding material |
| `Antiseptic bottle` | `20 Shekels` | `Common` | `0.3 kg` | Basic cleansing agent for routine treatment |

## Alchemical and Sample Handling

| Item | Price | Availability | Weight | Notes |
| --- | --- | --- | --- | --- |
| `Test tubes (5)` | `15 Shekels` | `Specialized` | `0.5 kg` | Basic liquid or specimen handling |

## Mundane Ammunition

| Item | Price | Availability | Weight | Notes |
| --- | --- | --- | --- | --- |
| `Steel arrows (20)` | `20 Shekels` | `Common` | `1 kg` | Baseline bow ammunition |
| `Darts (10)` | `10 Shekels` | `Common` | `0.3 kg` | Simple light-thrown ammunition |
| `Sling stones (10)` | `15 Shekels` | `Common` | `2 kg` | Routine sling ammunition |

Specialty ammunition such as observation arrows, signal darts, or unusual heads should usually begin at `Specialized` or higher unless the setting clearly normalizes them.

---

## Packages and Loadouts

Packages are convenience bundles.
They do not create new mechanics by themselves; they simply save lookup time when a table wants a ready-made mundane loadout.

### Adventure Pack

| Bundle | Price | Availability | Weight | Contains |
| --- | --- | --- | --- | --- |
| `Adventure pack` | `150 Shekels` | `Moderate` | `12 kg` | bedroll, waterskin, field cook set, rope, basic light, and general travel basics |

### Dungeon Pack

| Bundle | Price | Availability | Weight | Contains |
| --- | --- | --- | --- | --- |
| `Dungeon pack` | `120 Shekels` | `Specialized` | `10 kg` | rope, torches, basic repair tools, first-pass medical basics, compact rations, and confined-space support goods |

---

## Catalog Use Rule

Use this catalog when:

- the object is mundane;
- the object is bought, carried, stored, consumed, or replaced as part of ordinary play;
- the table does not need a full subsystem or bespoke authored item entry;
- and the market question is more about access, price, or load than about unique powers.

If the object becomes culturally unique, faction-locked, materially exceptional, or mechanically deep enough to change combat or authored process logic, move it to the more specific system layer instead of keeping it here as a generic object.

---

## Relationship To Other Systems

- `Faction Reputation, Public Renown, Alliances, and Commerce` determines how easy these objects are to source, at what price, and through whose channels.
- `Materials and Fabrication` determines how more complex goods are made, refined, repaired, or commissioned.
- `Equipment Overview` governs the structural combat rules for armor, shields, and deeper combat equipment.

---

## Summary

1. This is the baseline catalog for ordinary carried goods.
2. It is broad, practical, and intentionally non-magical.
3. It should answer mundane inventory questions quickly.
4. It should hand off to other systems when an object becomes mechanically deep enough to deserve it.

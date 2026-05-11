# Combat Equipment Catalog

**Authority data:** `data/system/combat-equipment-catalog.yaml`
**Related docs:** `docs/system/equipment-overview.md`, `docs/system/materials-and-fabrication.md`, `docs/system/weapon-technique-profiles.md`

---

## Purpose

This document is the first concrete catalog layer for combat-facing equipment:

- named weapon items;
- shield classes;
- and the compositional rule for armor pieces.

It exists to answer:

- what a concrete weapon item is;
- what its damage, range, weight, associated characteristic, and assignment are;
- what shield classes look like in authored catalog form;
- and how armor should be treated as assembled slot pieces rather than as a giant list of separate full suits.

This document does **not** replace the structural rules in `equipment-overview.md`.
It instantiates them.

---

## Core Rule

Combat equipment uses three different authoring models:

- `Weapons` are usually authored as named items.
- `Shields` are usually authored as category-based items with grade-sensitive formulas.
- `Armor` is usually authored compositionally through `slot + armor category + material + grade`, not as a massive list of separate named suits.

---

## Armor Authoring Rule

Armor is already structurally defined by:

- slot;
- armor category (`Light`, `Medium`, `Heavy`);
- material;
- and piece grade.

That means a pair of `Light Boots` made from `Leather` and a pair of `Light Boots` made from `Titanium` share the same slot effect and armor-category behavior.

What changes with material is primarily:

- durability;
- potency;
- and how the piece survives pressure against other material layers.

The category still determines:

- base block;
- how Agility interacts with `D.R.`;
- and the passive slot bonus.

So armor should usually be cataloged as valid combinations and production rules, not as hundreds of separate pseudo-unique items.

### Armor slots

- `Helmet`
- `Chestpiece`
- `Bracers`
- `Trousers`
- `Boots`

### Armor categories

- `Light`
- `Medium`
- `Heavy`

### Valid material families by category

Use the material permissions already defined in `materials-and-fabrication.md` when authoring actual pieces.

---

## Shields

Shields are authored by class.
The exact passive value and movement penalty still come from `grade` and shield type.
As in `equipment-overview.md`, that value is treated as a general bonus to `D.R.`, not as a separate shield-only armor track.

| Shield class | Cover bonus | `D.R.` bonus | Movement penalty | Weight |
| --- | --- | --- | --- | --- |
| `Light` | none | `grade` | none | `2 kg` |
| `Medium` | `Light Cover` | `grade` | `grade` | `5 kg` |
| `Heavy` | `Medium Cover` | `grade + 1` | `grade * 2` | `10 kg` |

These class entries should be treated as the default authored layer unless a future shield has a special exception.

---

## Weapons

### Spears

| Weapon | Damage category | Type | Hands | Damage | Range | Weight | Characteristic | Assignment | Bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Lancea` | `Piercing (Pf)` | `Spear` | `2` | `d12` | `2 m` | `4 kg` | `Strength` | `Primary` | `+1 per competency rank to A.R. against mounted or large enemies` |
| `Partisana` | `Piercing (Pf) or Cutting (Ct)` | `Spear` | `2` | `d10` | `2 m` | `4.5 kg` | `Tenacity` | `Primary` | `+1 per competency rank to I.R. when attacking at maximum reach` |
| `Kontos` | `Piercing (Pf)` | `Spear` | `2` | `d12` | `2 m` | `5 kg` | `Agility` | `Primary` | `+1 per competency rank to damage against enemies without shields` |
| `Yari` | `Piercing (Pf)` | `Spear` | `2` | `d12` | `2 m` | `4.2 kg` | `Cunning` | `Primary` | `Ignores 1 point of Block per competency rank` |
| `Hasta` | `Piercing (Pf)` | `Spear` | `1` | `d8` | `1 m` | `2.5 kg` | `Cunning` | `Primary` | `+1 per competency rank to D.R. when used to block at close range` |
| `Dory` | `Piercing (Pf)` | `Spear` | `1` | `d8` | `1 m` | `2.3 kg` | `Agility` | `Primary` | `Increase die tier when used as a thrown weapon` |
| `Ranseur` | `Piercing (Pf)` | `Spear` | `2` | `d10` | `2 m` | `5.2 kg` | `Strength` | `Primary` | `+1 per competency rank to A.R. during a charge` |

### Axes

| Weapon | Damage category | Type | Hands | Damage | Range | Weight | Characteristic | Assignment | Bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Guja` | `Ct or Pf` | `Axe` | `2` | `d10` | `2 m` | `5 kg` | `Strength` | `Primary` | `Ignores 1 point of armor per competency rank if the enemy is not in heavy armor` |
| `Alabarda` | `Ct or Pf` | `Axe` | `2` | `d10` | `2 m` | `4.5 kg` | `Tenacity` | `Primary` | `+1 per competency rank to I.R. at maximum reach` |
| `Naginata` | `Cutting (Ct)` | `Axe` | `2` | `d12` | `2 m` | `4.5 kg` | `Cunning` | `Primary` | `+1 per competency rank to I.R. when used for reactions` |
| `Voulge` | `Cutting (Ct)` | `Axe` | `2` | `d12` | `2 m` | `5.5 kg` | `Agility` | `Primary` | `+1 to I.R. against enemies without shields` |
| `Bec de Corbin` | `Blunt (Cd)` | `Axe` | `2` | `d10` | `2 m` | `4.8 kg` | `Strength` | `Primary` | `+1 per competency rank to I.R. against enemies in heavy armor` |
| `Pudao` | `Cutting (Ct)` | `Axe` | `2` | `d12` | `2 m` | `5.3 kg` | `Wisdom` | `Primary` | `+1 per competency rank to A.R. per adjacent enemy, maximum +3` |
| `Sagaris` | `Cutting (Ct)` | `Axe` | `1` | `d8` | `1 m` | `2 kg` | `Strength` | `Primary` | `+1 per competency rank to I.R. against enemies in light armor` |
| `Skeggox` | `Cutting (Ct)` | `Axe` | `1` | `d8` | `1 m` | `2 kg` | `Strength` | `Primary` | `+1 per competency rank to A.R. in two-weapon fighting` |
| `Labrys` | `Cutting (Ct)` | `Axe` | `2` | `d12` | `2 m` | `3.5 kg` | `Tenacity` | `Primary` | `Ignores 1 point of armor per competency rank when used in a two-handed attack` |
| `Dolabra` | `Blunt (Cd)` | `Axe` | `1` | `d6` | `1 m` | `2.5 kg` | `Tenacity` | `Primary` | `+3 per competency rank to I.R. when used to break objects` |

### Maces

| Weapon | Damage category | Type | Hands | Damage | Range | Weight | Characteristic | Assignment | Bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Morgenstern` | `Blunt (Cd)` | `Mace` | `1` | `d8` | `1 m` | `2 kg` | `Strength` | `Primary` | `+1 per competency rank to I.R. against enemies in medium armor` |
| `Nekhakha` | `Blunt (Cd)` | `Mace` | `1` | `d8` | `1 m` | `2 kg` | `Agility` | `Primary` | `+1 per competency rank to A.R. in reactions or counterattacks` |
| `Kanabo` | `Blunt (Cd)` | `Mace` | `2` | `d10` | `2 m` | `5 kg` | `Tenacity` | `Primary` | `Reduces break threshold by 1 when testing parts, not only critical hits` |
| `Shillelagh` | `Blunt (Cd)` | `Mace` | `1` | `d6` | `1 m` | `1.5 kg` | `Wisdom` | `Primary` | `+1 per competency rank to A.R. in defensive maneuvers or disarms` |
| `Shishpar` | `Blunt (Cd)` | `Mace` | `1` | `d8` | `1 m` | `2.5 kg` | `Cunning` | `Primary` | `Ignores 2 points of Block per competency rank against off-balance, staggered, or prone enemies` |

### Long Blades

| Weapon | Damage category | Type | Hands | Damage | Range | Weight | Characteristic | Assignment | Bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Katana` | `Cutting (Ct)` | `Long Blade` | `1` | `d8` | `1 m` | `1.2 kg` | `Agility` | `Primary` | `+1 per competency rank to I.R. when used with both hands` |
| `Spatha` | `Cutting (Ct)` | `Long Blade` | `1` | `d8` | `1 m` | `1 kg` | `Strength` | `Primary` | `+1 per competency rank to I.R. when used with a shield` |
| `Khopesh` | `Cutting (Ct)` | `Long Blade` | `1` | `d8` | `1 m` | `1.5 kg` | `Tenacity` | `Primary` | `Ignores 1 point of armor per competency rank against shields` |
| `Shamshir` | `Cutting (Ct)` | `Long Blade` | `1` | `d8` | `1 m` | `1 kg` | `Agility` | `Primary` | `+1 per competency rank to A.R. if the user moved this turn` |
| `Claymore` | `Cutting (Ct)` | `Long Blade` | `2` | `d12` | `2 m` | `2.5 kg` | `Tenacity` | `Primary` | `+1 per competency rank to I.R. against multiple enemies` |
| `Mandoble` | `Cutting (Ct)` | `Long Blade` | `2` | `d10` | `2 m` | `2 kg` | `Strength` | `Primary` | `+1 per competency rank to A.R. on a charge attack` |
| `Estoque` | `Piercing (Pf)` | `Long Blade` | `1` | `d8` | `1 m` | `1.1 kg` | `Cunning` | `Primary` | `Ignores 2 points of Block per competency rank when striking vital points` |
| `Schiavona` | `Cutting (Ct)` | `Long Blade` | `1` | `d8` | `1 m` | `1.3 kg` | `Wisdom` | `Primary` | `+1 per competency rank to A.R. when used with Deception or Acrobatics maneuvers` |

### Daggers

| Weapon | Damage category | Type | Hands | Damage | Range | Weight | Characteristic | Assignment | Bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Sai` | `Piercing (Pf)` | `Dagger` | `1` | `d4` | `1 m` | `0.7 kg` | `Agility` | `Auxiliary` | `+1 per competency rank to D.R. when deflecting or blocking melee attacks` |
| `Jutte` | `Blunt (Cd)` | `Dagger` | `1` | `d4` | `1 m` | `0.6 kg` | `Wisdom` | `Auxiliary` | `+2 per competency rank to A.R. for disarms or immobilizations` |
| `Scian` | `Piercing (Pf)` | `Dagger` | `1` | `d4` | `1 m` | `0.5 kg` | `Agility` | `Auxiliary` | `+2 per competency rank to I.R. from hidden or stealth position` |
| `Kris` | `Cutting (Ct)` | `Dagger` | `1` | `d4` | `1 m` | `0.6 kg` | `Cunning` | `Auxiliary` | `+1 per competency rank to A.R. against wounded enemies` |

### Short Blades

| Weapon | Damage category | Type | Hands | Damage | Range | Weight | Characteristic | Assignment | Bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Wakizashi` | `Cutting (Ct)` | `Short Blade` | `1` | `d6` | `1 m` | `0.9 kg` | `Agility` | `Auxiliary` | `+1 per competency rank to A.R. when used with another weapon in two-weapon fighting` |
| `Tanto` | `Cutting (Ct)` | `Short Blade` | `1` | `d4` | `1 m` | `0.6 kg` | `Agility` | `Auxiliary` | `+1 per competency rank to I.R. from hidden or stealth position` |
| `Kama` | `Cutting (Ct)` | `Short Blade` | `1` | `d6` | `1 m` | `0.7 kg` | `Agility` | `Auxiliary` | `+1 per competency rank to I.R. on the second attack you make in the round` |
| `Claideamh` | `Piercing (Pf)` | `Short Blade` | `1` | `d6` | `1 m` | `0.8 kg` | `Strength` | `Auxiliary` | `+1 per competency rank to A.R. against enemies in light armor` |
| `Seax` | `Cutting (Ct)` | `Short Blade` | `1` | `d4` | `1 m` | `0.7 kg` | `Strength` | `Auxiliary` | `+1 per competency rank to A.R. in single-target area maneuvers` |
| `Cimitarra` | `Cutting (Ct)` | `Short Blade` | `1` | `d6` | `1 m` | `0.8 kg` | `Agility` | `Primary` | `d2 extra damage per competency rank when the enemy fails its D.R.` |
| `Akinakes` | `Cutting (Ct)` | `Short Blade` | `1` | `d4` | `1 m` | `0.7 kg` | `Agility` | `Primary` | `You may make one additional off-hand attack per round during two-weapon fighting` |
| `Xiphos` | `Cutting (Ct)` | `Short Blade` | `1` | `d4` | `1 m` | `0.8 kg` | `Agility` | `Auxiliary` | `+1 per competency rank to Destreza S.R. during two-weapon fighting` |

### Thrown Weapons

| Weapon | Damage category | Type | Hands | Damage | Range | Weight | Characteristic | Assignment | Bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Kunai` | `Piercing (Pf)` | `Thrown` | `1` | `d4` | `10 m` | `0.3 kg` | `Agility` | `Auxiliary` | `+1 per competency rank to A.R. at half maximum range` |
| `Shuriken` | `Piercing (Pf)` | `Thrown` | `1` | `d4` | `10 m` | `0.2 kg` | `Agility` | `Auxiliary` | `+1 per competency rank to A.R. when used in series` |
| `Pilum` | `Piercing (Pf)` | `Thrown Spear` | `1` | `d6` | `10 m` | `1.5 kg` | `Strength` | `Primary` | `+2 per competency rank to I.R. when thrown to pierce shields or defenses` |
| `Francisca` | `Cutting (Ct)` | `Thrown Axe` | `1` | `d6` | `10 m` | `1.4 kg` | `Strength` | `Primary` | `+1 per competency rank to I.R. on charges or rush attacks` |
| `Chakram` | `Cutting (Ct)` | `Thrown` | `1` | `d4` | `12 m` | `0.4 kg` | `Cunning` | `Auxiliary` | `+1 per competency rank to A.R. when used against more than one creature` |

### Ranged Weapons

| Weapon | Damage category | Type | Hands | Damage | Range | Weight | Characteristic | Assignment | Bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Yumi` | `By projectile` | `Ranged` | `2` | `d8` | `30 m` | `1 kg` | `Agility` | `Primary` | `+1 per competency rank to A.R. against targets beyond 15 meters` |
| `Gakgung` | `By projectile` | `Ranged` | `2` | `d6` | `20 m` | `1 kg` | `Agility` | `Primary` | `+1 per competency rank to A.R. from hidden or stealth position` |
| `Fukiya` | `By projectile` | `Ranged` | `1` | `d4` | `20 m` | `0.5 kg` | `Agility` | `Primary` | `+1 per competency rank to I.R. on precision attacks against vital points` |
| `Scythian` | `By projectile` | `Ranged` | `2` | `d8` | `30 m` | `1 kg` | `Strength` | `Primary` | `+1 per competency rank to A.R. when fired from a mount` |
| `Balearic` | `By projectile` | `Ranged` | `1` | `d4` | `20 m` | `0.7 kg` | `Agility` | `Primary` | `+1 per competency rank to A.R. per consecutive attack in the same turn` |
| `Sumpit` | `By projectile` | `Ranged` | `1` | `d4` | `20 m` | `0.5 kg` | `Agility` | `Primary` | `+1 per competency rank to I.R. when applying poison or disease delivery` |

### Flexible Weapons

| Weapon | Damage category | Type | Hands | Damage | Range | Weight | Characteristic | Assignment | Bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Kusarigama` | `Sickle (Ct), Chain (Cd)` | `Flexible` | `2` | `Sickle d6, Chain d4` | `1 m / 3 m` | `1.5 kg` | `Agility` | `Primary` | `+1 per competency rank to A.R. during multiple-attack sequences when alternating between sickle and chain as if using two weapons` |
| `Scourge` | `Blunt (Cd)` | `Flexible` | `1` | `d4` | `1–3 m` | `1 kg` | `Strength` | `Auxiliary` | `+1 per competency rank to A.R. against enemies beyond 1 m` |
| `Nekode` | `Cutting (Ct)` | `Flexible` | `1` | `d4` | `1 m` | `0.5 kg` | `Agility` | `Auxiliary` | `+1 per competency rank to A.R. in Techniques from the Interruption or Unpredictability profiles` |
| `Kusari Fundo` | `Blunt (Cd)` | `Flexible` | `2` | `d6` | `1–3 m` | `1.2 kg` | `Cunning` | `Primary` | `+1 per competency rank to I.R. when the target is already off-balance, staggered, or prone` |
| `Spider Gloves` | `Cutting (Ct)` | `Flexible` | `1` | `d4` | `1–3 m` | `0.4 kg` | `Agility` | `Auxiliary` | `+1 per competency rank to Trepar or Agarre S.R. when used for climbing, grappling, or entangling close-pressure actions` |
| `Urumi` | `Cutting (Ct)` | `Flexible` | `1` | `d6` | `1–4 m` | `1.6 kg` | `Agility` | `Primary` | `Ignores 1 point of Block per competency rank when attacking from beyond 1 m` |

---

## Catalog Use Rule

Use this catalog when:

- the group needs a concrete combat item rather than only a family or profile;
- the object is still mundane enough to be handled as equipment rather than a supernatural item;
- and the table needs a stable baseline for damage, reach, weight, associated characteristic, assignment, and item bonus.

If an item's identity is mostly:

- material exception;
- living-material behavior;
- vestigial or link power;
- or highly regional ritual construction,

then author it as a more specific derived item on top of this catalog instead of replacing this baseline.

---

## Summary

1. Weapons are named items.
2. Shields are class-authored with grade formulas.
3. Armor is compositional by slot, category, material, and grade.
4. Material changes durability and potency pressure; category still determines armor behavior.

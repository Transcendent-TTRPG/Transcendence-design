# Natural Attack Forms

**Authority data:** `data/system/natural-attack-forms.yaml`
**Related docs:** `docs/system/weapon-technique-profiles.md`, `docs/system/techniques.md`, `docs/system/equipment-overview.md`

---

## Purpose

This document defines the inverse navigation layer for natural combat:

- natural attack form
- combat identity
- compatible Weapon Technique Profiles
- restricted or poor-fit profiles

The goal is to stop natural compatibility from living only inside profile documents.

---

## Core Rule

A natural attack form does **not** create a separate Technique school by itself.

Instead, each form declares:

- what kind of contact it creates
- what combat fantasies it supports
- which Weapon Technique Profiles it can access naturally
- which profiles should normally remain restricted

This keeps natural combat inside the same Technique ecosystem as fabricated weapons.

Each natural attack form should map to **four** compatible Weapon Technique Profiles whenever possible. Those four profiles may come from different manufactured weapon families, because anatomy inherits combat logic by contact, not by item category. A tail, claw, horn, or tusk is not pretending to be one weapon family; it is borrowing the profiles that its body logic can credibly express.

Natural attack forms are **not** profiles.

They are an inverse compatibility layer:

- fabricated weapon families -> shared Weapon Technique Profiles
- natural attack forms -> those **same shared Weapon Technique Profiles**

So a form such as `Claw`, `Horn`, or `Tail` does not add a new family of Techniques.
It only states which existing profiles can be inherited by that anatomy.

This matters because scaling, balance logic, and future sub-systems should continue to live on the shared profiles, not on a duplicate natural-only track.

---

## Reading Rule

Each form should answer:

1. What kind of body logic does this attack create?
2. Which existing profiles express that logic naturally?
3. Which profiles would be a stretch or should remain restricted?

If a form cannot map cleanly to existing profiles, that may justify:

- a new profile
- a species-specific exception
- or a custom restriction note

but not a whole isolated subsystem by default.

---

## Canonical Fields

Each natural attack form should declare:

| Field | Purpose |
| --- | --- |
| `name` | Canonical form name |
| `contact_logic` | What kind of bodily contact it creates |
| `combat_role` | Main offensive or defensive role |
| `damage_identity` | What kind of harm or pressure it tends to produce |
| `compatible_profiles` | Profiles the form can access naturally |
| `restricted_profiles` | Profiles that are possible only with strong justification or should usually remain unavailable |
| `identity_notes` | Clarifies why those mappings make sense |

Optional fields may include:

- species
- species profile expressions
- species notes
- delivery notes
- environmental dependence
- profile-specific caveats

### Species Expression Rule

The form-level profile list is a generic default. It is useful when a species has not yet received a focused natural-weapon pass.

When a species has a defined expression for the same anatomical form, the species expression overrides the generic profile list for species-origin Technique authoring. This prevents a `Bite`, `Tail`, or `Claw` from behaving identically across species whose anatomy and combat logic are meaningfully different.

Examples:

- a Naghii bite is fang insertion and venom delivery
- a Sauri bite is jaw closure, clamp, and crushing pressure
- a Naghii tail is prehensile restraint and torsion
- a Sauri tail is heavy lateral sweep and lane denial

---

## Initial Forms

### Bite

- **Spanish name:** Mordisco
- **Species:** Naghii, Sauri, Zarnag, Drak'kai, Formix, Panin, Luphran, Ursari, Arakhel, Vesper, Manto, Telpi, Myo
- **Contact logic:** close puncture, clamp, tearing bite, or bite-driven hold
- **Combat role:** committed close threat
- **Damage identity:** puncture, tear, pressure, invasive contact
- **Compatible profiles:** `Perforation`, `Charge`, `Rend`, `Shadow Pressure`
- **Restricted profiles:** `Bastion`, `Ricochet`, `Precision`
- **Identity notes:** Bite supports deep entry, brutal close pressure, and predatory commitment. It maps well to piercing or tearing profiles, but usually not to stationary defense or ranged geometry.

#### Species profile expressions

| Species | Expression | Availability | Compatible profiles | Identity |
| --- | --- | --- | --- | --- |
| Naghii | Fang Bite | Kha-Naghii only | `Perforation`, `Corrosion`, `Shadow Pressure`, `Precision` | Retractable fang entry, controlled venom delivery, exact contact, and punishment of hesitation. |
| Sauri | Jaw Closure | All Sauri | `Impact`, `Bastion`, `Rend`, `Unstoppable` | Heavy jaw closure, clamp, crush, drag, and sustained pressure. |

### Tail

- **Spanish name:** Cola
- **Species:** Naghii, Sauri
- **Contact logic:** sweep, push, spoil, off-line collision, or flexible redirection depending on anatomy
- **Combat role:** space denial, interruption, repositioning
- **Damage identity:** displacement, disruption, side-angle impact
- **Compatible profiles:** `Interception`, `Line Control`, `Torsion`, `Interruption`
- **Restricted profiles:** `Precision`, `Ricochet`, `Bastion`
- **Identity notes:** Tail forms are excellent at changing lanes and angles. Some tails can also slam, but most are better at control and spoil than at precise or ballistic delivery.

#### Species profile expressions

| Species | Expression | Availability | Compatible profiles | Identity |
| --- | --- | --- | --- | --- |
| Naghii | Prehensile Tail | All Naghii | `Interception`, `Line Control`, `Torsion`, `Interruption` | Restraint, curved contact, angle theft, and crossing disruption without relying on raw mass. |
| Sauri | Heavy Tail | All Sauri | `Impact`, `Line Control`, `Interception`, `Interruption` | Heavy side pressure, sweeping disruption, and preventing clean passage around the body. |

### Claw

- **Spanish name:** Garra
- **Species:** Zarnag, Rokhart, Chelicer, Luphran, Ursari, Vesper, Lupinni, Erin, Talpi, Myo
- **Contact logic:** rake, hook, slash, tear, or fast contact from short reach
- **Combat role:** aggressive close pressure
- **Damage identity:** cut, tear, opportunistic opening
- **Compatible profiles:** `Flow`, `Shadow Pressure`, `Rend`, `Skirmish`
- **Restricted profiles:** `Bastion`, `Precision`, `Ricochet`
- **Identity notes:** Claws sit naturally between light predation and tearing offense. They map strongly to mobile and invasive profiles.

### Shell

- **Spanish name:** Caparazon
- **Species:** Drak'kai
- **Contact logic:** brace, cover, absorb, slam, or hold through mass and structure
- **Combat role:** anchor, protect, absorb, occasional impact
- **Damage identity:** protected endurance, blunt contact, defended collision
- **Compatible profiles:** `Bastion`, `Interception`, `Impact`, `Line Control`
- **Restricted profiles:** `Shadow Pressure`, `Precision`, `Torsion`
- **Identity notes:** Shells are structural. They naturally support holding, covering, and body-first impact, not deceptive or highly flexible play.

### Beak

- **Spanish name:** Pico
- **Species:** Rokhart
- **Contact logic:** puncture, snap, peck, or hooked edge contact depending on form
- **Combat role:** precise strike or tearing pick
- **Damage identity:** puncture, cut, invasive point pressure
- **Compatible profiles:** `Perforation`, `Deflection`, `Rend`, `Precision`
- **Restricted profiles:** `Bastion`, `Torsion`, `Volley`
- **Identity notes:** Beaks can behave like points or sharp edges. They fit accuracy and tearing better than anchoring or flexible redirection.

### Trunk

- **Spanish name:** Trompa
- **Species:** Loxod
- **Contact logic:** grab, push, sweep, wrap, and short-range structural manipulation
- **Combat role:** control, interruption, positional dominance
- **Damage identity:** displacement, crush, redirection
- **Compatible profiles:** `Line Control`, `Torsion`, `Interruption`, `Bastion`
- **Restricted profiles:** `Precision`, `Ricochet`, `Shadow Pressure`
- **Identity notes:** Trunks excel at spatial authority and manipulative contact. They are poor fits for stealthy or ballistic profiles.

### Tusk

- **Spanish name:** Colmillos
- **Species:** Loxod
- **Contact logic:** committed forward puncture with body follow-through
- **Combat role:** breakthrough, brutal entry
- **Damage identity:** puncture, wedge force, structural opening
- **Compatible profiles:** `Perforation`, `Charge`, `Sunder`, `Unstoppable`
- **Restricted profiles:** `Torsion`, `Ricochet`, `Bastion`
- **Identity notes:** Tusks are excellent at forcing entry and breaking resistant lines, but they do not support flexible or ranged logic well.

### Horn

- **Spanish name:** Cuerno
- **Species:** Ceratox
- **Contact logic:** forward-drive wedge, puncture, or heavy committed impact
- **Combat role:** breakthrough, collision, structural breach
- **Damage identity:** puncture, impact, breaking force
- **Compatible profiles:** `Perforation`, `Charge`, `Sunder`, `Impact`
- **Restricted profiles:** `Shadow Pressure`, `Ricochet`, `Torsion`
- **Identity notes:** Horns naturally bridge piercing and crashing entries. They are one of the clearest natural matches for committed assault profiles.

### Stinger

- **Spanish name:** Aguijon
- **Species:** Formix, Chelicer
- **Contact logic:** fast puncture delivery of invasive or degrading contact
- **Combat role:** inject, weaken, punish brief openings
- **Damage identity:** puncture, toxin, persistence
- **Compatible profiles:** `Perforation`, `Corrosion`, `Shadow Pressure`, `Precision`
- **Restricted profiles:** `Bastion`, `Impact`, `Line Control`
- **Identity notes:** Stingers are ideal for puncture plus hostile residue. They are usually too small or specialized for anchoring or blunt-force roles.

### Spines

- **Spanish name:** Puas
- **Species:** Erin
- **Contact logic:** projected shard, repeated spine release, or embedded puncture
- **Combat role:** ranged harassment or pressure
- **Damage identity:** puncture, persistence, repeated ranged threat
- **Compatible profiles:** `Precision`, `Volley`, `Ricochet`, `Corrosion`
- **Restricted profiles:** `Bastion`, `Torsion`, `Charge`
- **Identity notes:** Quills and spines sit naturally in the ranged family. If they carry toxin or residue, `Corrosion` also fits well.

### Tongue

- **Spanish name:** Lengua
- **Species:** Bufoni
- **Contact logic:** lash, wrap, snap, redirect, fake line, or off-axis contact
- **Combat role:** disruption, unusual angle entry, control
- **Damage identity:** flexible contact, interference, angle theft
- **Compatible profiles:** `Torsion`, `Interruption`, `Unpredictability`, `Skirmish`
- **Restricted profiles:** `Bastion`, `Perforation`, `Sunder`
- **Identity notes:** Tongues and tendrils are ideal for weird contact geometry and timing spoils, but generally poor for rigid force-through profiles.

### Fluid Projection

- **Spanish name:** Fluidos Proyectados
- **Species:** Naghii, Formix, Chelicer
- **Contact logic:** projected spit, acid, toxin, or pressurized biological discharge
- **Combat role:** ranged weakening, harassment, residue delivery
- **Damage identity:** precision hit, persistent degradation, repeated pressure
- **Compatible profiles:** `Precision`, `Volley`, `Ricochet`, `Corrosion`
- **Restricted profiles:** `Bastion`, `Charge`, `Flow`
- **Identity notes:** Fluid projection covers both clean targeted shots and degrading residues. Its profile spread depends on whether the biology emphasizes aim, cadence, rebound logic, or hostile substance.

### Pincers

- **Spanish name:** Tenazas
- **Species:** Manto
- **Contact logic:** seize, clamp, crush, pin, or punish escape through rigid opposing force
- **Combat role:** capture, hold, positional punishment
- **Damage identity:** crush, retention, trap pressure
- **Compatible profiles:** `Interruption`, `Line Control`, `Impact`, `Sunder`
- **Restricted profiles:** `Ricochet`, `Precision`, `Skirmish`
- **Identity notes:** Pincers and crushing mandibles excel at committing to a target and denying clean escape. They are strong fits for stop-and-hold combat, not for light mobility or ballistic logic.

# Weapon Technique Profiles

**Authority data:** `data/system/weapon-technique-profiles.yaml`
**Related docs:** `docs/system/techniques.md`, `docs/system/competencies.md`, `docs/system/equipment-overview.md`, `docs/system/atb-reference.md`, `docs/system/natural-attack-forms.md`

---

## Purpose

This document defines the **profile layer** that sits between:

- weapon competency
- concrete Techniques
- natural attack forms

Weapon Technique Profiles exist so the system does **not** need:

- a full Technique tree for every individual weapon item
- a separate isolated combat school for natural attacks
- old action-point combo logic imported into the ATB model

Instead, Techniques can be authored through a shared thematic and functional layer.

---

## Core Role

A **Weapon Technique Profile** is a thematic sub-domain that groups Techniques by:

- combat fantasy
- functional pressure pattern
- typical effect family
- compatible weapon families or natural attack forms

It is **not**:

- a single Technique
- a weapon item
- a raw competency
- a species feature by itself

It is a reusable bridge between equipment identity and actual Technique authoring.

---

## Why This Layer Exists

Without profiles, the system tends to drift toward one of two bad extremes:

1. a separate Technique catalog for every weapon item
2. a flat weapon competency that cannot express enough identity

Profiles solve that by letting Techniques emerge from:

- a weapon competency or weapon family
- one combat profile
- sometimes a second origin such as Evasion, Shield, Specialization, or Resistance

This keeps the system expressive without exploding in volume.

---

## Relationship To Other Layers

### Weapon competency

Weapon competency remains the main technical gate.

It answers:

- what the character can wield effectively
- what rank and level they have in that family
- what baseline offensive competence they bring

### Weapon Technique Profile

The profile answers:

- what style of Technique expression the attack belongs to
- what kinds of effects feel natural for that combat mode
- what thematic line connects different Techniques in the same family

### Technique

The actual Technique answers:

- what happens right now
- what it costs
- what it targets
- what effect it creates

---

## Not Per Weapon Item

Profiles should normally attach to:

- weapon families
- attack modes
- natural attack forms
- stable equipment roles

They should **not** be written for every single manufactured item variant.

Good profile anchors:

- spear thrust / perforation
- long-blade flow
- short-blade shadow pressure
- shield interception
- thrown ricochet
- flexible torsion

Bad profile anchors:

- iron militia spear pattern #3
- merchant dagger variant B
- noble cavalry sabre from one region only

Specific items may modify access, cost, range, or restrictions, but they should not each demand their own full profile lattice.

---

## Natural Weapons

Natural weapons should use this same profile layer.

That means a claw, fang, horn, tail, tongue, or shell attack does **not** need its own separate Technique school if it can map cleanly to an existing combat profile.

This is an inheritance model, not a parallel taxonomy:

- fabricated weapon families define access to shared Weapon Technique Profiles
- natural attack forms also define access to those **same shared profiles**
- natural combat does **not** create a second catalog of profiles with separate scaling logic

In practice, a natural form may inherit profile access from several fabricated families at once if the body logic supports it.

Examples:

- a claw may inherit profiles that also belong to short blades, long blades, or light skirmish weapons
- a horn may inherit profiles that also belong to spears, heavy impact weapons, or breaching tools
- a tail may inherit profiles that also belong to shields or flexible weapons

The shared profile remains the scaling and authoring surface. The natural form only explains **why** that profile access makes sense for the anatomy.

Natural attack forms should define:

- attack form
- damage identity
- role
- compatible profiles
- restricted profiles

This lets natural combatants stay fully inside the Technique ecosystem without forcing fabricated weapons to be the only path to advanced combat identity.

### Design rule

Natural weapons may:

- share profiles with manufactured weapons
- gain profile access through anatomy or species traits
- have a few anatomy-specific restrictions or bonuses

Natural weapons should not:

- require a full standalone authoring framework unless they truly break normal combat logic

---

## Relation To ATB

The old action-point idea of chaining repeated maneuvers by descriptor does **not** carry over directly.

Under the current ATB model, Profiles are **not** a combo engine by themselves.

They should shape:

- timing identity
- rhythm pressure
- what kinds of follow-up Techniques feel natural
- what tags, triggers, and cost patterns cluster together

They should **not** create a generic rule that lets characters repeat same-profile Techniques for stacking bonuses just because they share a descriptor.

If a future Technique references a follow-up window, chain condition, or linked execution, that must be authored inside the Technique itself or in a tightly bounded subgroup rule.

No global combo-by-profile rule should be assumed.

---

## Weapon Access Balance

Manufactured weapon competencies use a uniform core access model: each weapon competency grants access to **four** core Weapon Technique Profiles.

Specific weapon items may modify range, damage, requirements, or narrow Technique permissions, but they do not create extra profile access by default. `Yari`, `Lancea`, `Labrys`, `Urumi`, and similar item names matter as equipment, not as separate Technique trees.

The older combo-descriptor model is not carried forward mechanically. Only the names and combat concepts survive as identity anchors. Old names that implied magic or planar behavior are treated as retired labels, not as Technique permissions.

| Weapon competency | Core profiles | Old concept anchors |
| --- | --- | --- |
| `Spear` | `Perforation`, `Ward`, `Charge`, `Skirmish` | Perforador, Defensivo, Carga, Agil |
| `Axes` | `Rend`, `Sunder`, `Unstoppable`, `Line Control` | Desgarrador, Demoledor, Impulso, Barredor |
| `Maces` | `Impact`, `Sunder`, `Unstoppable`, `Bastion` | Aplastante, Imparable, Golpe Sordo, Fortificado |
| `Long Blades` | `Flow`, `Rend`, `Lethality`, `Deflection` | Fluyente, Cortante, Letal, Deflectante |
| `Short Blades` | `Shadow Pressure`, `Corrosion`, `Lethality`, `Skirmish` | Sombrio, Erosivo, Implacable, Veloz |
| `Daggers` | `Unpredictability`, `Shadow Pressure`, `Lethality`, `Deflection` | Enganoso, Brumoso, Penetrante, Disruptivo |
| `Thrown Weapons` | `Precision`, `Ricochet`, `Volley`, `Interruption` | Preciso, Ricochete, Propulsion, Intercepcion |
| `Ranged Weapons` | `Precision`, `Ricochet`, `Volley`, `Corrosion` | Aguijon, Ricochete, Rafaga, Desgaste |
| `Flexible Weapons` | `Torsion`, `Unpredictability`, `Skirmish`, `Interruption` | Torsion, Impredecible, Fluctuante, Persistente |
| `Shield` | `Interception`, `Interruption`, `Line Control`, `Bastion` | Interceptacion, Interrupcion, Control de Campo, Bastion |

Natural attack forms inherit from these same shared profiles through anatomy and species logic. They do not use this table as a rigid count requirement, because a natural form may be narrower or broader depending on its body logic.

---

## Canonical Fields

Each Weapon Technique Profile should declare at minimum:

| Field | Purpose |
| --- | --- |
| `name` | Canonical profile name |
| `family` | Broad combat family it belongs to |
| `fantasy_core` | Central combat identity |
| `compatible_origins` | Weapon competencies, weapon families, or attack forms that can use it |
| `natural_weapon_compatibility` | Whether natural forms can access it and under what logic |
| `primary_tags` | Main Technique outputs expected from the profile |
| `secondary_tags` | Less frequent but valid outputs |
| `rare_or_limited_tags` | Outputs that should remain constrained |
| `typical_types` | Active / Reactive / Passive patterns that fit this profile |
| `usual_cost_profile` | Rhythm and Attrition tendencies |
| `timing_identity` | How the profile tends to live inside ATB windows |
| `identity_notes` | Clarifies what the profile should feel like |
| `should_not_do` | Prevents drift into other profiles |

Optional fields may include:

- compatible equipment notes
- follow-up logic
- anatomy restrictions
- line / reach tendencies
- defensive bridge notes

---

## Source of Differentiation

Profiles are meant to generate differentiation at three levels:

1. between weapon families
2. between Techniques under the same weapon competency
3. between fabricated and natural combatants using different compatible profiles

The player still chooses:

- weapon competency
- armor strategy
- shield or Evasion emphasis
- specializations

Profiles simply stop that choice from collapsing into a flat list of attacks.

---

## First Authoring Rule

When proposing a new combat Technique, ask:

1. Does this belong to an existing profile?
2. If not, is the missing piece truly a new profile and not just a new Technique?
3. Could a natural weapon or attack form use this profile too?
4. Does this profile shape timing and identity without creating a global combo rule?

If the answer to `2` is weak, do not create a new profile yet.

---

## Initial Profiles

### Perforation

- **Family:** Spear / thrusting reach / piercing natural impact
- **Fantasy core:** driving force through a narrow line to break distance, threaten entry, and punish exposed forward commitment
- **Compatible origins:**
  - weapon competencies: Spear
  - weapon families: thrusting polearms, long thrusting weapons, dedicated piercing reach weapons
  - natural attack forms: horn, tusk, fang, beak, stinger
  - secondary requirements: may pair well with Evasion, Shield, Tracking, or Tolerance depending on Technique identity
- **Natural weapon compatibility:** allowed
  - Natural forms can access this profile when they create a committed piercing line rather than broad tearing, blunt crashing, or flexible constriction.
- **Primary tags:** `attack`, `pressure`, `precision`
- **Secondary tags:** `setup`, `mobility`, `disruption`
- **Rare or limited tags:** `control`, `defense`, `recovery`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low-to-medium rhythm, low Attrition when used as disciplined threat projection, medium Attrition when built around repeated committed drives or harsh body-weight transfer
- **Timing identity:** lives best in entry denial, lane control, decisive extension, and punish windows created by enemy advance, overreach, or exposed line
- **Identity notes:** Perforation Techniques should feel linear, committed, and exact. They are about reach discipline, point-first pressure, body alignment, and decisive forward authority. They should create the sense that the user wins by claiming the line before the opponent can safely cross it.
- **Should not do:**
  - wide_sweeping_multi_target_control
  - heavy_blunt_impact_identity
  - concealment_or_shadow_play
  - abstract_condition_removal
  - purely_defensive_bastion_play

### Interception

- **Family:** Shield interception / line denial / protective redirection
- **Fantasy core:** stepping into the hostile line at the last moment to catch, divert, absorb, or spoil what was meant for someone else or for a more vulnerable opening
- **Compatible origins:**
  - weapon competencies: Shield
  - weapon families: shields, guard tools, dedicated protective off-hand structures
  - natural attack forms: tail, shell, heavy forelimb, plated crest
  - secondary requirements: may pair well with Armor, Evasion, Leadership, or Tolerance depending on whether the Technique protects, redirects, stabilizes, or endures impact
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when anatomy can meaningfully cover, catch, block, or spoil a hostile line. It should not be used by natural attacks whose identity is only tearing, piercing, or pure offense.
- **Primary tags:** `defense`, `interception`, `control`
- **Secondary tags:** `setup`, `disruption`, `anti_displacement`
- **Rare or limited tags:** `attack`, `mobility`, `recovery`
- **Typical types:** `reactive`, sometimes `active`, rarely `passive`
- **Usual cost profile:** medium rhythm, low-to-medium Attrition when used as disciplined coverage, medium Attrition when repeatedly absorbing force or protecting others under heavy pressure
- **Timing identity:** lives in reaction windows, ally coverage, lane denial, body-first protection, and spoil timing against incoming strikes, charges, or hostile entry attempts
- **Identity notes:** Interception Techniques should feel protective without becoming static. They are about reading the line early enough to occupy it, turning defense into spatial control, and making hostile momentum hit the wrong surface, angle, or timing. The user should feel like someone who alters what reaches the target, not just someone who passively endures it.
- **Should not do:**
  - stealth_or_concealment_identity
  - pure_ranged_pressure
  - long_form_recovery_as_primary_role
  - wide_offensive_sweeping_damage
  - abstract_nonspatial_condition_cleansing

### Flow

- **Family:** Long-blade flow / continuous edge control / elegant offensive transition
- **Fantasy core:** maintaining dangerous continuity through stance, edge, and movement so that one action naturally opens the next without losing authority over spacing
- **Compatible origins:**
  - weapon competencies: Long Blades
  - weapon families: swords, sabres, curved long blades, balanced cutting weapons
  - natural attack forms: claw, forelimb blade, elongated edge-like appendage
  - secondary requirements: may pair well with Evasion, Balance, Focus, or Leadership depending on whether the Technique emphasizes movement, stance discipline, tempo control, or commanding presence in the fight
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when they sustain controlled cutting continuity or edge-like directional pressure. It should not be used by forms whose identity is only blunt crashing, constriction, or committed piercing.
- **Primary tags:** `attack`, `mobility`, `setup`
- **Secondary tags:** `pressure`, `defense`, `disruption`
- **Rare or limited tags:** `recovery`, `interception`, `control`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** medium rhythm, low-to-medium Attrition when movement stays clean, medium Attrition when the user keeps chaining transitions under hard pressure or extended commitment
- **Timing identity:** lives in tempo carry, repositioning between exchanges, angle-taking, continuation after contact, and techniques that turn a successful movement or cut into the next advantageous state
- **Identity notes:** Flow Techniques should feel graceful without becoming decorative. They are about continuity, edge authority, and the ability to keep a blade alive through transitions so that the opponent keeps answering the previous threat while the next one is already forming. The user should feel mobile, composed, and dangerous in motion.
- **Should not do:**
  - static_bastion_identity
  - heavy_impact_breaking_play
  - concealment_or_assassination_identity
  - pure_ranged_projection
  - abstract_condition_removal

### Shadow Pressure

- **Family:** Short-blade shadow pressure / opportunistic close-range exploitation
- **Fantasy core:** staying close, hard to read, and immediately dangerous by turning concealment, distraction, angle, or hesitation into fast pressure before the opponent can reset
- **Compatible origins:**
  - weapon competencies: Short Blades, Daggers
  - weapon families: knives, daggers, short stabbing blades, concealment-ready close weapons
  - natural attack forms: fang, claw, small stinger, hooked beak
  - secondary requirements: may pair well with Stealth, Deception, Imitation, Intuition, or Evasion depending on whether the Technique enters through concealment, misread, identity break, anticipation, or angle theft
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when they create opportunistic close pressure through speed, angle, concealment, or sudden insertion. It should not be used by natural forms whose identity is broad tearing, heavy impact, or open frontal domination.
- **Primary tags:** `attack`, `stealth`, `pressure`
- **Secondary tags:** `mobility`, `setup`, `disruption`
- **Rare or limited tags:** `defense`, `control`, `recovery`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-medium rhythm, low Attrition for short opportunistic bursts, medium Attrition when repeatedly forcing entry, concealment transitions, or unstable close pressure under heavy awareness
- **Timing identity:** lives in surprise windows, blind-side entry, post-distraction pressure, punishment of hesitation, and rapid close exchanges where the user strikes before the enemy reorients
- **Identity notes:** Shadow Pressure Techniques should feel predatory, intimate, and immediate. They are about owning the moment when the opponent loses clean read, not about long duels of visible dominance. The user should feel like a threat that appears from the wrong angle, exploits a tiny lapse, and keeps the pressure too close to comfortably answer.
- **Should not do:**
  - open_line_reach_dueling
  - static_guardian_play
  - heavy_blast_or_impact_identity
  - broad_multi_target_sweeps
  - abstract_noncontact_support

### Line Control

- **Family:** Line control / spatial denial / forced repositioning
- **Fantasy core:** deciding where bodies can safely stand, pass, or commit by shaping lanes, edges, and collision points through pressure applied to space rather than to damage alone
- **Compatible origins:**
  - weapon competencies: Shield, Axes
  - weapon families: shields, broad control surfaces, push-oriented defensive tools
  - natural attack forms: tail, heavy forelimb, shell, trunk
  - secondary requirements: may pair well with Armor, Strength, Balance, Interception, or Engineering depending on whether the Technique leans toward push control, body positioning, stable occupation, or environmental shaping
- **Natural weapon compatibility:** allowed
  - Natural forms can access this profile when anatomy can push, redirect, block passage, sweep space, or create enforced movement without relying on pure damage as the main identity.
- **Primary tags:** `control`, `anti_displacement`, `disruption`
- **Secondary tags:** `defense`, `setup`, `pressure`
- **Rare or limited tags:** `attack`, `recovery`, `stealth`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** medium rhythm, medium Attrition when repeatedly contesting space, shifting bodies, or holding denial under pressure
- **Timing identity:** lives in choke points, ally protection geometry, hostile path denial, trap shaping, push timing, and moments where one forced step or blocked lane changes the whole exchange
- **Identity notes:** Line Control Techniques should feel territorial and positional. They are about making the battlefield narrower, worse, or more dangerous for the opponent and safer or more useful for allies. The user should feel like someone who governs movement and commitment, not like someone who merely tanks hits.
- **Should not do:**
  - pure_stationary_bastion_identity
  - concealment_or_assassination_play
  - long_range_projectile_pressure
  - abstract_condition_cleansing
  - high_precision_dueling_as_primary_identity

### Ricochet

- **Family:** Thrown ricochet / angled projection / rebound pressure
- **Fantasy core:** using angle, impact surface, and projectile behavior to create pressure that does not follow the most obvious direct line
- **Compatible origins:**
  - weapon competencies: Thrown Weapons, Ranged Weapons
  - weapon families: throwing blades, throwing spikes, rebound-capable projectiles, hard small missiles
  - natural attack forms: projected quill, shard burst, hardened fluid shot
  - secondary requirements: may pair well with Precision, Focus, Engineering, Perception, or Intuition depending on whether the Technique leans toward trajectory reading, planned rebound, environmental use, or anticipatory targeting
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when the projectile or expelled attack can realistically skip, rebound, fragment in a controlled line, or continue through shaped impact logic. It should not be used by natural attacks whose identity is only spray, mist, or pure magical-seeming spread.
- **Primary tags:** `attack`, `setup`, `disruption`
- **Secondary tags:** `pressure`, `precision`, `control`
- **Rare or limited tags:** `defense`, `recovery`, `stealth`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** medium rhythm, low-to-medium Attrition when geometry is favorable, medium Attrition when repeated angle calculation, environmental exploitation, or chained projection is forced under pressure
- **Timing identity:** lives in indirect lines, cover-denial, rebound setups, multi-angle threat, and moments where the environment itself becomes part of the hostile trajectory
- **Identity notes:** Ricochet Techniques should feel clever, sharp, and materially grounded. They are about weaponizing surfaces, rebounds, skips, and continuation paths so that the enemy is threatened from a line they did not fully own or expect. The user should feel like someone who sees the battlefield as geometry, not just as straight-line range.
- **Should not do:**
  - pure_volume_fire_identity
  - magical_homing_behavior
  - concealment_or_melee_assassination_identity
  - massive_area_blast_as_primary_mode
  - abstract_condition_removal

### Precision

- **Family:** Precision shot / selective impact / exact ranged pressure
- **Fantasy core:** placing force exactly where it matters by reading distance, movement, exposure, and target structure better than the opponent can deny it
- **Compatible origins:**
  - weapon competencies: Ranged Weapons, Thrown Weapons
  - weapon families: bows, crossbows, firearms if later present, precise thrown weapons, direct-line projectile systems
  - natural attack forms: spine shot, needle spit, focused fluid jet
  - secondary requirements: may pair well with Focus, Perception, Identification, Intuition, or Tracking depending on whether the Technique leans toward calm execution, target read, weak-point knowledge, anticipatory aim, or pursuit pressure
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when they produce a direct, aimable, repeatable projectile or projected strike. It should not be used by diffuse sprays, broad clouds, or uncontrolled scatter attacks.
- **Primary tags:** `attack`, `precision`, `pressure`
- **Secondary tags:** `setup`, `disruption`, `control`
- **Rare or limited tags:** `mobility`, `defense`, `recovery`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** medium rhythm, low Attrition for disciplined single-shot execution, low-to-medium Attrition when repeated under movement, range distortion, or hard target read pressure
- **Timing identity:** lives in exposed moments, weak-point lines, punish shots after movement errors, and any exchange where one exact impact can alter the next state more than raw volume would
- **Identity notes:** Precision Techniques should feel calm, exact, and surgically decisive. They are about certainty of placement, not volume of fire. The user should feel like someone who understands distance, angle, and target vulnerability well enough to make one shot matter more than several careless ones.
- **Should not do:**
  - chaotic_multi_angle_rebound_identity
  - broad_suppression_fire_as_primary_mode
  - concealment_melee_entry_play
  - wide_area_blast_logic
  - abstract_condition_removal

### Charge

- **Family:** Charge / committed entry / momentum impact
- **Fantasy core:** converting movement, mass, and forward commitment into a decisive collision that breaks position, forces reaction, or overwhelms the line before the enemy can stabilize
- **Compatible origins:**
  - weapon competencies: Spear
  - weapon families: spears, lances, heavy impact weapons, mounted charge weapons, committed rush tools
  - natural attack forms: horn, tusk, headbutt crest, trampling forebody
  - secondary requirements: may pair well with Balance, Tolerance, Armor, Mount handling, or Line Control depending on whether the Technique leans toward impact integrity, pain endurance, mounted delivery, or post-impact occupation
- **Natural weapon compatibility:** allowed
  - Natural forms can access this profile when anatomy can deliver meaningful forward-drive impact through mass, speed, leverage, or body-first commitment. It should not be used by light opportunistic attacks whose identity is only angle theft or concealment.
- **Primary tags:** `attack`, `pressure`, `anti_displacement`
- **Secondary tags:** `disruption`, `mobility`, `control`
- **Rare or limited tags:** `defense`, `recovery`, `stealth`
- **Typical types:** `active`, rarely `reactive`
- **Usual cost profile:** medium-to-high rhythm, medium Attrition by default, and potentially high Attrition when repeated under terrain resistance, body contact, or failed breakthrough conditions
- **Timing identity:** lives in engagement openings, rush windows, committed approach, mounted entry, and moments where breaking the opponent's line or posture matters more than clean sustained exchange
- **Identity notes:** Charge Techniques should feel forceful, committed, and difficult to ignore. They are about arriving with enough momentum that the opponent must yield space, absorb impact, or be structurally disrupted. The user should feel like a dangerous advancing mass, not a delicate duelist extending a line.
- **Should not do:**
  - static_defensive_guardian_play
  - concealment_or_shadow_identity
  - fine_precision_targeting_as_primary_mode
  - indirect_ranged_geometry
  - abstract_condition_removal

### Bastion

- **Family:** Bastion / anchored defense / protected endurance
- **Fantasy core:** becoming the point that does not easily yield, using structure, stance, shield mass, and disciplined endurance to hold a line that others would lose
- **Compatible origins:**
  - weapon competencies: Shield, Maces, Armor
  - weapon families: tower shields, heavy shields, defensive guard assemblies, fixed protection structures
  - natural attack forms: shell, plated crest, heavy forelimb, braced body frame
  - secondary requirements: may pair well with Tolerance, Armor, Containment, Interception, or Leadership depending on whether the Technique leans toward sustained hold, pain endurance, formation stability, protected reaction, or allied confidence
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when anatomy can genuinely brace, cover, endure, and protect through mass or structure. It should not be used by purely agile or opportunistic forms with no credible holding surface.
- **Primary tags:** `defense`, `stability`, `mitigation`
- **Secondary tags:** `control`, `support`, `survival_window`
- **Rare or limited tags:** `attack`, `mobility`, `stealth`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** medium rhythm, low-to-medium Attrition for disciplined holding, medium Attrition when repeatedly absorbing force, guarding others, or maintaining posture under concentrated pressure
- **Timing identity:** lives in hold-the-line moments, ally shelter, attritional exchanges, last-stand windows, and phases where surviving the next impact matters more than taking the next step
- **Identity notes:** Bastion Techniques should feel weighty, disciplined, and reassuring to allies. They are about becoming a defended point in the field, not just blocking one strike. The user should feel like someone who can anchor pressure, hold formation, and keep collapse from spreading.
- **Should not do:**
  - fast_skirmish_mobility_identity
  - concealment_or_assassination_play
  - precise_dueling_as_primary_mode
  - indirect_ranged_geometry
  - abstract_condition_cleansing

### Torsion

- **Family:** Torsion / flexible reach / angular redirection
- **Fantasy core:** using bend, wrap, whip, or redirection of trajectory to threaten from difficult angles and reshape how force travels through contact
- **Compatible origins:**
  - weapon competencies: Flexible Weapons
  - weapon families: whips, chains, segmented weapons, rope-dart analogues, flexible striking tools
  - natural attack forms: tongue, tentacle, tail, flexible tendril
  - secondary requirements: may pair well with Balance, Dexterity, Control, Intuition, or Line Control depending on whether the Technique leans toward angle creation, entangling pressure, spatial bending, or off-line redirection
- **Natural weapon compatibility:** allowed
  - Natural forms can access this profile when anatomy can bend, wrap, lash, coil, or redirect contact through flexible motion. It should not be used by rigid forms whose identity depends on straight-line impact or fixed guarding surfaces.
- **Primary tags:** `control`, `mobility`, `disruption`
- **Secondary tags:** `attack`, `setup`, `pressure`
- **Rare or limited tags:** `mitigation`, `recovery`, `stability`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** medium rhythm, low-to-medium Attrition for clean flexible handling, medium Attrition when repeated under unstable spacing, wrapping strain, or multi-angle commitment
- **Timing identity:** lives in off-line entries, wraparound pressure, angular redirection, space-bending attacks, and exchanges where the attack path matters as much as the impact itself
- **Identity notes:** Torsion Techniques should feel strange, difficult to map, and materially believable. They are about curvature, wrap, and unexpected contact geometry, not supernatural extension. The user should feel like someone who attacks through the path itself, making straight defensive assumptions unreliable.
- **Should not do:**
  - rigid_line_dueling_identity
  - heavy_static_bastion_play
  - clean_ballistic_projection
  - abstract_condition_removal
  - pure_blunt_collision_as_primary_mode

### Impact

- **Family:** Impact / blunt trauma / structural shock
- **Fantasy core:** delivering force so heavily and cleanly that posture, guard, breath, or body structure absorbs the hit before intent can recover
- **Compatible origins:**
  - weapon competencies: Maces
  - weapon families: maces, hammers, clubs, crushing poles, impact-first striking tools
  - natural attack forms: shell slam, forelimb smash, headbutt, tail slam
  - secondary requirements: may pair well with Strength, Tolerance, Balance, Line Control, or Bastion depending on whether the Technique leans toward break force, body commitment, stance integrity, forced displacement, or defended collision
- **Natural weapon compatibility:** allowed
  - Natural forms can access this profile when anatomy can deliver meaningful blunt collision through mass, leverage, or hardened structure. It should not be used by forms whose identity is precision puncture, concealment, or flexible redirection.
- **Primary tags:** `attack`, `disruption`, `pressure`
- **Secondary tags:** `anti_displacement`, `control`, `setup`
- **Rare or limited tags:** `stealth`, `recovery`, `precision`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** medium rhythm, medium Attrition by default, and medium-to-high Attrition when repeated under heavy body commitment, recoil, or armored resistance
- **Timing identity:** lives in break moments, posture collapse, shield punishment, guard cracking, and exchanges where one hard impact can ruin the enemy's structure even without fine placement
- **Identity notes:** Impact Techniques should feel brutal, grounded, and physically undeniable. They are about shock transfer, not elegance. The user should feel like someone who can break the body's organization or the enemy's confidence through one heavy committed hit.
- **Should not do:**
  - fine_line_precision_dueling
  - concealment_or_shadow_entry
  - indirect_projectile_geometry
  - flexible_wrap_identity
  - abstract_condition_removal

### Rend

- **Family:** Rend / tearing force / persistent bodily degradation
- **Fantasy core:** opening flesh, structure, or protection in a way that does not end at contact, leaving the target worse after the strike than the immediate impact alone would suggest
- **Compatible origins:**
  - weapon competencies: Axes, Long Blades
  - weapon families: axes, hooked blades, tearing edges, ripping tools
  - natural attack forms: claw, fang, hooked beak, serrated mandible
  - secondary requirements: may pair well with Strength, Precision, Tracking, Tolerance, or Shadow Pressure depending on whether the Technique leans toward brutal tearing, weak-point opening, pursuit damage, pain endurance, or close predatory follow-through
- **Natural weapon compatibility:** allowed
  - Natural forms can access this profile when anatomy can rip, tear, shred, or leave persistent bodily compromise through edge, hook, or bite structure. It should not be used by blunt forms or by attacks whose identity is clean puncture without tearing follow-through.
- **Primary tags:** `attack`, `pressure`, `disruption`
- **Secondary tags:** `setup`, `precision`, `control`
- **Rare or limited tags:** `defense`, `recovery`, `stealth`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** medium rhythm, medium Attrition when repeated aggressively, especially if the user keeps committing to close bodily follow-through or target mauling
- **Timing identity:** lives in finish pressure, wound-opening moments, prey-tracking continuation, armor gap exploitation, and exchanges where damage quality matters more than single-hit force
- **Identity notes:** Rend Techniques should feel savage, invasive, and hard to ignore after the fact. They are about damage that keeps mattering because something was torn open, destabilized, or left exposed. The user should feel like someone who makes the enemy progressively worse to inhabit.
- **Should not do:**
  - clean_linear_dueling_identity
  - pure_blunt_collision_play
  - indirect_projectile_geometry
  - static_guardian_defense
  - abstract_condition_removal

### Sunder

- **Family:** Sunder / breaking force / material opening
- **Fantasy core:** attacking structure itself so that armor, guard, cover, weapon integrity, or bodily stability give way under targeted destructive force
- **Compatible origins:**
  - weapon competencies: Axes, Maces
  - weapon families: axes, splitting tools, cleaving weapons, breaker heads, armor-opening implements
  - natural attack forms: horn, tusk, crushing mandible, wedge skull
  - secondary requirements: may pair well with Strength, Engineering, Identification, Impact, or Line Control depending on whether the Technique leans toward material break, weak-point reading, structural punishment, or opening a lane by destroying what held it
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when anatomy can crack, split, wedge, or break through resistant material or guarded structure. It should not be used by light tearing attacks whose identity is only flesh damage without structural breach.
- **Primary tags:** `attack`, `disruption`, `control`
- **Secondary tags:** `pressure`, `anti_displacement`, `setup`
- **Rare or limited tags:** `stealth`, `recovery`, `mobility`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** medium-to-high rhythm, medium-to-high Attrition when repeatedly committed against armor, shields, hard cover, or resistant bodies
- **Timing identity:** lives in armor-breaking moments, guard collapse, cover denial, weapon punishment, and exchanges where opening the structure matters more than landing the cleanest wound
- **Identity notes:** Sunder Techniques should feel destructive in a material sense, not just painful. They are about making something that was protecting, stabilizing, or resisting stop doing that job. The user should feel like someone who forces entry by breaking what made resistance possible.
- **Should not do:**
  - elegant_precision_dueling
  - concealment_or_shadow_entry
  - indirect_projectile_geometry
  - soft_flexible_wrap_identity
  - abstract_condition_removal

### Volley

- **Family:** Volley / sustained ranged pressure / repeated release
- **Fantasy core:** maintaining ranged initiative through cadence, repeated release, and pressure accumulation so the opponent has to keep answering the next shot instead of reclaiming tempo
- **Compatible origins:**
  - weapon competencies: Ranged Weapons, Thrown Weapons
  - weapon families: bows, slings, light crossbows, repeated-throw sets, fast-release projectile systems
  - natural attack forms: quill volley, repeated spine shot, rapid fluid spit
  - secondary requirements: may pair well with Focus, Rhythm control, Tracking, Precision, or Ricochet depending on whether the Technique leans toward cadence discipline, target continuation, selective follow-up, or environmental sequencing
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when anatomy can repeatedly project aimed attacks in meaningful sequence. It should not be used by single-shot anatomies with long reset or by diffuse area emission that is not truly repeat-fire pressure.
- **Primary tags:** `attack`, `pressure`, `setup`
- **Secondary tags:** `disruption`, `control`, `precision`
- **Rare or limited tags:** `defense`, `recovery`, `stealth`
- **Typical types:** `active`, rarely `reactive`
- **Usual cost profile:** medium rhythm, medium Attrition when maintaining release cadence, and medium-to-high Attrition when pressure is sustained through movement, unstable footing, or target-rich exchanges
- **Timing identity:** lives in repeated firing windows, pursuit pressure, suppressive exchanges, forced cover, and sequences where keeping initiative at range matters more than any single perfect shot
- **Identity notes:** Volley Techniques should feel relentless and rhythmic rather than chaotic. They are about making the enemy live under the next release, not just the current one. The user should feel like someone who controls ranged tempo through cadence and persistence.
- **Should not do:**
  - single_shot_surgical_identity
  - rebound_geometry_as_primary_mode
  - concealment_melee_entry
  - wide_blast_logic
  - abstract_condition_removal

### Deflection

- **Family:** Deflection / redirection by edge / active off-line defense
- **Fantasy core:** spoiling hostile force through angle, timing, and contact redirection so the incoming line fails to land cleanly and may open a countering advantage
- **Compatible origins:**
  - weapon competencies: Long Blades, Daggers
  - weapon families: swords, sabres, side blades, defensive knives, parrying-capable edges
  - natural attack forms: forelimb blade, hooked claw, rigid beak edge
  - secondary requirements: may pair well with Evasion, Balance, Flow, Intuition, or Interception depending on whether the Technique leans toward contact redirection, evasive angle, rhythm spoil, or protective response
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when anatomy can meaningfully catch, glance, guide away, or spoil a hostile line through rigid edge or precise contact. It should not be used by soft flexible forms or blunt structures whose identity is absorption rather than redirection.
- **Primary tags:** `defense`, `disruption`, `precision`
- **Secondary tags:** `setup`, `mobility`, `attack`
- **Rare or limited tags:** `mitigation`, `support`, `recovery`
- **Typical types:** `reactive`, sometimes `active`
- **Usual cost profile:** low-to-medium rhythm, low Attrition for clean single spoils, medium Attrition when repeatedly contesting incoming lines under heavy tempo pressure
- **Timing identity:** lives in contact windows, hostile overreach, parry moments, angle steals, and exchanges where turning the line a few degrees is enough to save the body and open the reply
- **Identity notes:** Deflection Techniques should feel sharp, disciplined, and responsive. They are not about enduring impact like a bastion or occupying space like a shield wall. They are about making the hostile line miss its clean purpose through edge, angle, and timing. The user should feel like someone who survives by changing where force goes.
- **Should not do:**
  - static_guardian_anchor_play
  - pure_body_absorption_identity
  - broad_spatial_denial_as_primary_mode
  - indirect_projectile_geometry
  - abstract_condition_removal

### Interruption

- **Family:** Interruption / execution break / hostile action spoil
- **Fantasy core:** breaking the enemy's process before it resolves cleanly by striking timing, focus, structure, or commitment at the vulnerable moment of execution
- **Compatible origins:**
  - weapon competencies: Shield, Flexible Weapons, Thrown Weapons
  - weapon families: shields, interruptive off-hand tools, fast sidearms, hooking weapons, quick thrown counters
  - natural attack forms: tail, tongue, hooked claw, snapping mandible
  - secondary requirements: may pair well with Intuition, Focus, Interception, Torsion, or Deflection depending on whether the Technique leans toward timing read, execution spoil, wrap interruption, or contact redirection into failure
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when anatomy can quickly spoil, jab, hook, snap, or disrupt an enemy's active process in a believable timing window. It should not be used by slow mass-dominant forms whose identity is only impact or endurance.
- **Primary tags:** `disruption`, `control`, `setup`
- **Secondary tags:** `attack`, `defense`, `pressure`
- **Rare or limited tags:** `recovery`, `stealth`, `mitigation`
- **Typical types:** `reactive`, sometimes `active`
- **Usual cost profile:** low-to-medium rhythm, low-to-medium Attrition for clean spoils, medium Attrition when repeatedly contesting enemy execution under dense timing pressure
- **Timing identity:** lives in cast breaks, action spoil windows, long-motion punishment, readied-action denial, and moments where stopping the enemy matters more than damaging them directly
- **Identity notes:** Interruption Techniques should feel sharp, intrusive, and opportunistic. They are not about guarding space in the abstract, but about ruining a process while it is happening. The user should feel like someone who senses the vulnerable instant in another's action and tears it apart before it resolves.
- **Should not do:**
  - static_line_holding_identity
  - pure_endurance_absorption
  - long_form_attrition_without_timing
  - indirect_projectile_geometry_as_primary_mode
  - abstract_condition_removal

### Corrosion

- **Family:** Corrosion / degrading contact / persistent hostile residue
- **Fantasy core:** applying a contact that keeps making the target worse after impact through poison, acid, toxin, caustic residue, or another materially grounded degrading agent
- **Compatible origins:**
  - weapon competencies: Short Blades, Ranged Weapons
  - weapon families: venom-bearing light weapons, delivery weapons, acid carriers, residue-applying projectiles
  - natural attack forms: stinger, venom fang, acid spit, corrosive fluid jet
  - secondary requirements: may pair well with Tolerance, Resistance hybrids, Precision, Rend, or Tracking depending on whether the Technique leans toward delivery, persistence, prey weakening, or sustained deterioration after contact
- **Natural weapon compatibility:** allowed
  - Natural forms can access this profile when anatomy or secretion can credibly deliver a degrading substance or residue that continues to matter after impact. It should not be used for purely magical decay or for clean physical damage with no degrading follow-through.
- **Primary tags:** `pressure`, `disruption`, `control`
- **Secondary tags:** `attack`, `setup`, `condition_reduction`
- **Rare or limited tags:** `defense`, `recovery`, `mobility`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** medium rhythm, low-to-medium Attrition for prepared delivery, medium Attrition when repeated under pressure or when maintaining hostile persistence through multiple contacts
- **Timing identity:** lives in weakening contact, delayed consequence, follow-up pressure, pursuit degradation, and exchanges where making the enemy progressively worse matters more than immediate burst
- **Identity notes:** Corrosion Techniques should feel invasive, lingering, and materially ugly. They are about making a contact remain relevant because something is now inside, on, or against the target that continues to degrade function. The user should feel like someone who wins by worsening the enemy over time through real hostile residue, not by invoking unexplained magical decay.
- **Should not do:**
  - pure_clean_precision_identity
  - blunt_collision_identity
  - abstract_curse_or_magic_decay
  - broad_instant_blast_logic
  - condition_removal_as_primary_mode

### Unpredictability

- **Family:** Unpredictability / false read / non-obvious attack logic
- **Fantasy core:** defeating the opponent's expectation by making the next line, angle, rhythm, or mode of contact resolve from the wrong assumption
- **Compatible origins:**
  - weapon competencies: Daggers, Flexible Weapons
  - weapon families: deceptive sidearms, flexible trick weapons, feint-capable close weapons, odd-angle tools
  - natural attack forms: tongue, hooked claw, feinting tail, snapping beak
  - secondary requirements: may pair well with Intuition, Deception, Imitation, Torsion, or Deflection depending on whether the Technique leans toward false read, expectation break, off-line contact, or deceptive redirection
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when anatomy can credibly fake line, alter angle late, present false rhythm, or resolve from a non-obvious contact path. It should not be used by purely straightforward mass-impact forms.
- **Primary tags:** `disruption`, `setup`, `mobility`
- **Secondary tags:** `attack`, `control`, `pressure`
- **Rare or limited tags:** `mitigation`, `recovery`, `support`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-medium rhythm, low-to-medium Attrition for isolated read breaks, medium Attrition when repeated under high cognitive pressure or multi-step deceptive sequencing
- **Timing identity:** lives in feints, expectation traps, late angle shifts, read breaks, and exchanges where winning the interpretation layer matters more than brute force
- **Identity notes:** Unpredictability Techniques should feel slippery, intelligent, and hard to map in the moment. They are not random; they are deliberately hard to read. The user should feel like someone who makes the enemy commit to the wrong answer and then resolves through that mistake.
- **Should not do:**
  - pure_brutal_collision_identity
  - static_guardian_anchor_play
  - clean_straight_line_precision_as_primary_mode
  - broad_ranged_suppression
  - abstract_condition_removal

### Skirmish

- **Family:** Skirmish / light engagement / hit-and-reposition
- **Fantasy core:** entering fast, striking in a meaningful but limited window, and changing position before the enemy can convert contact into stable control
- **Compatible origins:**
  - weapon competencies: Short Blades, Spear, Flexible Weapons
  - weapon families: light sidearms, agile reach weapons, mobile skirmish tools, light flexible weapons
  - natural attack forms: claw, fang, light tail, quick forelimb
  - secondary requirements: may pair well with Evasion, Balance, Flow, Shadow Pressure, or Line Control depending on whether the Technique leans toward mobility, tempo theft, brief pressure, or short positional denial
- **Natural weapon compatibility:** allowed
  - Natural forms can access this profile when anatomy supports fast entry, light contact, repositioning, and repeated engagement without relying on static hold or pure brute collision.
- **Primary tags:** `mobility`, `attack`, `setup`
- **Secondary tags:** `pressure`, `disruption`, `defense`
- **Rare or limited tags:** `mitigation`, `recovery`, `stability`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-medium rhythm, low Attrition for clean light engagements, medium Attrition when repeatedly forcing entry and exit under heavy attention or broken terrain
- **Timing identity:** lives in touch-and-go exchanges, approach-and-break windows, tempo theft, brief lane entry, and sequences where changing position matters as much as landing the hit
- **Identity notes:** Skirmish Techniques should feel agile, opportunistic, and tactically light. They are not about standing and winning a sustained exchange, but about touching the fight at the right moment and leaving it changed before the opponent settles. The user should feel difficult to pin down, but not invisible or magical.
- **Should not do:**
  - static_line_holding_identity
  - heavy_collision_break_play
  - prolonged_attritional_anchor
  - broad_ranged_suppression
  - abstract_condition_removal

### Ward

- **Family:** Ward / reach discipline / pre-contact denial
- **Fantasy core:** keeping hostile entry uncomfortable by maintaining a dangerous ready line that punishes overstep before full contact ever settles
- **Compatible origins:**
  - weapon competencies: Spear
  - weapon families: spears, polearms, stance-disciplined long blades, guard-reach weapons
  - natural attack forms: horn, beak, tusk
  - secondary requirements: may pair well with Balance, Focus, Perception, Deflection, or Line Control depending on whether the Technique leans toward poised denial, patient timing, angle read, or lane preservation
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when anatomy can credibly hold a threatening forward line and punish entry before full body commitment. It should not be used by soft flexible forms or purely brute-impact attacks.
- **Primary tags:** `defense`, `pressure`, `control`
- **Secondary tags:** `setup`, `precision`, `anti_displacement`
- **Rare or limited tags:** `mobility`, `recovery`, `stealth`
- **Typical types:** `reactive`, sometimes `active`
- **Usual cost profile:** low-to-medium rhythm, low Attrition for disciplined ready-line play, medium Attrition when maintaining denial under repeated committed entry or shifting angles
- **Timing identity:** lives in first-step punish, measured denial, keep-out exchanges, lane preservation, and moments where threatening the answer matters more than taking the initiative first
- **Identity notes:** Ward Techniques should feel calm, exact, and structurally disciplined. They are about preserving a line the opponent does not want to cross, not about crashing through it. The user should feel like someone who wins by making approach costly before the exchange fully begins.
- **Should not do:**
  - shield_cover_interception_identity
  - concealment_or_assassination_play
  - heavy_collision_break_play
  - indirect_projectile_geometry
  - abstract_condition_removal

### Lethality

- **Family:** Lethality / vital exploitation / finishing authority
- **Fantasy core:** turning one clean opening into a decisive end-state through anatomical targeting, committed finishing mechanics, and exact exploitation of vulnerability
- **Compatible origins:**
  - weapon competencies: Long Blades, Daggers, Short Blades
  - weapon families: dueling swords, killing blades, stilettos, execution edges, vital-target sidearms
  - natural attack forms: fang, beak, stinger, hooked claw
  - secondary requirements: may pair well with Precision, Identification, Intuition, Shadow Pressure, or Focus depending on whether the Technique leans toward target read, timing certainty, or close finishing access
- **Natural weapon compatibility:** allowed with restrictions
  - Natural forms can access this profile when anatomy can credibly resolve through a precise kill line, vital puncture, or decisive finishing cut. It should not be used by broad smashing forms or diffuse degrading attacks.
- **Primary tags:** `attack`, `precision`, `pressure`
- **Secondary tags:** `setup`, `disruption`, `mobility`
- **Rare or limited tags:** `defense`, `recovery`, `control`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** medium rhythm, low-to-medium Attrition when used as selective finish pressure, medium Attrition when repeatedly forced through guarded or collapsing openings
- **Timing identity:** lives in exposed vitals, finishing windows, punishment of decisive mistakes, and exchanges where one exact close-range resolution matters more than prolonged pressure
- **Identity notes:** Lethality Techniques should feel final, surgical, and dangerous in a way distinct from ranged `Precision`. They are about ending the fight because the right opening was exploited at the right depth and angle. The user should feel like someone who recognizes when one exact committed strike can decide everything.
- **Should not do:**
  - broad_attritional_mauling
  - blunt_collision_identity
  - static_guardian_anchor_play
  - indirect_projectile_geometry
  - abstract_condition_removal

### Unstoppable

- **Family:** Unstoppable / drive-through commitment / refusal to stall
- **Fantasy core:** continuing offense through partial contact, resistance, obstruction, or pain so that the first collision fails to halt the advance
- **Compatible origins:**
  - weapon competencies: Maces, Axes
  - weapon families: heavy axes, breaker weapons, driving spears, mass-forward assault tools
  - natural attack forms: horn, tusk, forelimb smash, hoof trample
  - secondary requirements: may pair well with Tolerance, Armor, Charge, Bastion, or Balance depending on whether the Technique leans toward endurance-through-contact, advancing structure, or relentless follow-through
- **Natural weapon compatibility:** allowed
  - Natural forms can access this profile when anatomy can keep driving through contact, resistance, or stagger without losing offensive structure. It should not be used by light opportunistic forms whose identity depends on quick withdrawal or deceptive spacing.
- **Primary tags:** `attack`, `pressure`, `stability`
- **Secondary tags:** `anti_displacement`, `disruption`, `mitigation`
- **Rare or limited tags:** `stealth`, `recovery`, `precision`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** medium-to-high rhythm, medium Attrition by default, and high Attrition when repeatedly maintained through dense obstruction, armor, or pain-heavy exchanges
- **Timing identity:** lives after first impact, during stalled breakthrough, under body-check resistance, and in exchanges where not being stopped matters more than clean first contact
- **Identity notes:** Unstoppable Techniques should feel relentless rather than explosive. They are not about the opening crash itself, but about what happens when the crash fails to end the matter and the user keeps coming anyway. The user should feel like forward commitment remains dangerous even after collision.
- **Should not do:**
  - light_touch_skirmish_identity
  - concealment_or_shadow_entry
  - elegant_dueling_precision
  - indirect_projectile_geometry
  - abstract_condition_removal

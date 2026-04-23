# Specialization Technique Domains

**Authority data:** `data/system/specialization-technique-domains.yaml`
**Related docs:** `docs/system/specializations.md`, `docs/system/specializations-catalog.md` (authority in YAML), `docs/system/techniques.md`, `docs/system/competency-technique-domains.md`

---

## Purpose

This document defines the Technique identity of each specialization.

The previous layer established broad Technique domains by competency type. That is useful, but insufficient for Transcendence, because the real differentiation of characters comes from **individual practiced domains**.

This layer answers:

- what each specialization is best at producing as Techniques
- what it may produce secondarily
- what it should rarely or never do
- how its Techniques usually behave in terms of timing, target, and cost profile

This is the design bridge between:

- specialization identity
- Technique writing
- character differentiation

---

## Use Rule

Each specialization domain entry should define:

- `fantasy_core`
- `primary_tags`
- `secondary_tags`
- `rare_or_limited_tags`
- `typical_targets`
- `typical_types`
- `usual_cost_profile`
- `identity_notes`
- `should_not_do`

This is not a Technique list.
It is the **authoring boundary** for future Techniques.

### Tag rule

`primary_tags` and `secondary_tags` should prefer the controlled vocabulary from [techniques.md](/Users/juangomez/Transcendence-workspace/Transcendence-design/docs/system/techniques.md).

If a specialization needs a nuance that does not fit the canonical tag set cleanly, prefer putting that nuance into:

- `fantasy_core`
- `identity_notes`
- `should_not_do`

rather than introducing a weak or overly editorial tag.

### Target rule

`typical_targets` should also prefer the canonical target vocabulary from `techniques.md`.

Some entries below still use exploratory shorthand such as `scene`, `route`, `presence`, or `task`.
Those should be read as **domain notes**, not as final Technique data fields.

---

## Design Rule

If two specializations would generate nearly identical Technique spaces, one of them is too broad, too weak, or badly separated.

This file exists to force differentiation at the domain level before actual Technique authoring begins.

---

## Force

### Jumping

- **Fantasy core:** explosive projection, forced gap-crossing, sudden entry through bodily launch
- **Primary tags:** `mobility`, `setup`, `pressure`
- **Secondary tags:** `attack`, `escape`, `reposition`
- **Rare or limited tags:** `control`, `recovery`, `support`
- **Typical targets:** `self`, `route`, `enemy`
- **Typical types:** `active`
- **Usual cost profile:** moderate rhythm, low-to-medium Attrition, occasionally high if used for overextension
- **Identity notes:** Jumping Techniques should feel like commitment, angle, entry, or violent repositioning through impulse. They should begin from the launch, not from in-air refinement.
- **Should not do:** sustained balance, subtle concealment, broad control, prolonged defense

### Climbing

- **Fantasy core:** vertical progress, sustained body placement, controlled ascent or descent under pressure
- **Primary tags:** `mobility`, `escape`, `setup`
- **Secondary tags:** `stability`, `reposition`, `utility`
- **Rare or limited tags:** `attack`, `support`, `pressure`
- **Typical targets:** `self`, `route`, `object`, `environment`
- **Typical types:** `active`, rarely `reactive`
- **Usual cost profile:** moderate rhythm, low-to-medium Attrition, often shaped by environment more than by hostility
- **Identity notes:** Climbing Techniques should reward verticality, route access, anchor use, or controlled suspension. They should feel like progress against a surface, not generic grip control.
- **Should not do:** direct immobilization, broad enemy control, ranged pressure, social utility

### Throwing

- **Fantasy core:** projecting objects with trained force, angle, and timing to create distance pressure or utility
- **Primary tags:** `attack`, `pressure`, `setup`
- **Secondary tags:** `disruption`, `utility`, `precision`
- **Rare or limited tags:** `defense`, `recovery`, `support`
- **Typical targets:** `enemy`, `object`, `route`, `zone`
- **Typical types:** `active`
- **Usual cost profile:** low-to-medium rhythm, low Attrition for standard projection, higher when the throw alters the scene significantly
- **Identity notes:** Throwing Techniques should feel like physical projection mastery. They may open angles, disarm by distance, pin routes, or trigger objects, but should remain tied to bodily launch rather than device-driven shooting.
- **Should not do:** constant passive defense, sustained mitigation, non-physical control with no projectile logic

### Swimming

- **Fantasy core:** maintaining agency in water, crossing hostile water space, and staying functional where others lose movement
- **Primary tags:** `mobility`, `survival_window`, `escape`
- **Secondary tags:** `reposition`, `setup`, `stability`
- **Rare or limited tags:** `attack`, `support`, `control`
- **Typical targets:** `self`, `route`, `environment`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** medium rhythm, medium Attrition, highly scene-dependent
- **Identity notes:** Swimming Techniques should feel like command of an aquatic medium: staying on route, diving, surfacing, using water as approach or escape space.
- **Should not do:** generic environmental resistance, direct mitigation without water logic, long-range offense

### Gripping

- **Fantasy core:** contact dominance, hold retention, immobilizing or stabilizing through trained force at close range
- **Primary tags:** `control`, `interception`, `anti_displacement`
- **Secondary tags:** `defense`, `setup`, `pressure`
- **Rare or limited tags:** `mobility`, `recovery`, `support`
- **Typical targets:** `enemy`, `ally`, `object`, `self`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-medium rhythm, medium Attrition when sustaining contact under resistance
- **Identity notes:** Gripping Techniques should feel like point-of-contact mastery. They should dominate hands, limbs, leverage, retention, and immediate physical denial.
- **Should not do:** ranged pressure, broad battlefield control, abstract mobility bonuses

---

## Agility

### Acrobatics

- **Fantasy core:** dynamic bodily redirection, rolling, recovery, and fluid traversal through unstable movement
- **Primary tags:** `mobility`, `escape`, `reposition`
- **Secondary tags:** `defense`, `setup`, `spacing`
- **Rare or limited tags:** `control`, `support`, `recovery`
- **Typical targets:** `self`, `route`, `zone`, `enemy`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** moderate rhythm, low-to-medium Attrition, higher when chained under pressure
- **Identity notes:** Acrobatics Techniques should feel like continuity of motion. They begin where simple movement stops: redirection, recovery from bad angles, traversal through danger, and elegant evasion through dynamic body control.
- **Should not do:** static balance, fine hand manipulation, mounted command, pure force projection

### Dexterity

- **Fantasy core:** fine technical manipulation through precise hand and body control under real pressure
- **Primary tags:** `utility`, `setup`, `precision`
- **Secondary tags:** `control`, `disruption`, `support`
- **Rare or limited tags:** `attack`, `mobility`, `pressure`
- **Typical targets:** `object`, `self`, `ally`, `enemy`
- **Typical types:** `active`, rarely `reactive`
- **Usual cost profile:** low-to-medium rhythm, low Attrition for controlled work, medium when performed under danger or extreme precision pressure
- **Identity notes:** Dexterity Techniques should express exactness, careful placement, delicate manipulation, and technical execution. They should feel hand-driven, not whole-body acrobatic or opportunistic like Theft.
- **Should not do:** broad locomotion, generic stealth, brute-force control, social influence

### Balance

- **Fantasy core:** maintaining operational posture when footing, support, or external force tries to break bodily stability
- **Primary tags:** `defense`, `stability`, `anti_displacement`
- **Secondary tags:** `mobility`, `setup`, `reposition`
- **Rare or limited tags:** `attack`, `support`, `pressure`
- **Typical targets:** `self`, `route`, `enemy`, `environment`
- **Typical types:** `reactive`, occasionally `active`
- **Usual cost profile:** low rhythm, low-to-medium Attrition, often triggered by hostile force or unstable terrain
- **Identity notes:** Balance Techniques should feel like staying functional on bad footing, resisting forced loss of posture, and preserving tactical continuity where others would fall or yield space.
- **Should not do:** complex dynamic traversal, fine manipulation, mounted control, inner emotional stability

### Riding

- **Fantasy core:** turning mount and rider into a single tactical system under speed, pressure, and unstable positioning
- **Primary tags:** `mobility`, `setup`, `pressure`
- **Secondary tags:** `reposition`, `escape`, `control`
- **Rare or limited tags:** `recovery`, `support`, `precision`
- **Typical targets:** `self`, `creature`, `route`, `enemy`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** moderate rhythm, medium Attrition when maneuvering hard or fighting for mounted control
- **Identity notes:** Riding Techniques should express mounted line control, charge angles, mounted repositioning, and maintaining rider-mount integrity under threat. They should feel like tactical mounted use, not animal bonding or broad handling.
- **Should not do:** aura bonding, animal training in general, broad party support, static defense with no mount logic

---

## Tenacity

### March

- **Fantasy core:** sustained forward progress, route endurance, and keeping operational pace across long exertion
- **Primary tags:** `survival_window`, `mobility`, `stability`
- **Secondary tags:** `recovery`, `setup`, `escape`
- **Rare or limited tags:** `attack`, `control`, `support`
- **Typical targets:** `self`, `ally`, `route`, `environment`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-moderate rhythm, medium Attrition, often escalating over long scenes or journeys
- **Identity notes:** March Techniques should feel like preserving movement continuity over time. They are about keeping pace, extending travel function, or refusing collapse during prolonged displacement, not about resisting pain already inside the body.
- **Should not do:** direct pain resistance, environmental adaptation without travel logic, burst offense, static defense

### Acclimation

- **Fantasy core:** maintaining bodily function under hostile climate, altitude, exposure, or environmental pressure
- **Primary tags:** `defense`, `mitigation`, `survival_window`
- **Secondary tags:** `recovery`, `stability`, `utility`
- **Rare or limited tags:** `attack`, `mobility`, `control`
- **Typical targets:** `self`, `ally`, `environment`, `zone`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low rhythm, low-to-medium Attrition, often passive or triggered by exposure thresholds
- **Identity notes:** Acclimation Techniques should feel like resisting what the environment is doing to the body: heat, cold, thin air, corrosive atmosphere, pressure, or exposure. They should not drift into generic toughness once the suffering is already internalized.
- **Should not do:** prolonged locomotion support, direct offensive pressure, emotional stabilization, generic healing

### Tolerance

- **Fantasy core:** remaining functional while pain, poison, wounds, or active physiological degradation are already inside the body
- **Primary tags:** `defense`, `mitigation`, `condition_reduction`
- **Secondary tags:** `survival_window`, `stability`, `recovery`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `self`, rarely `ally`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low rhythm, low-to-medium Attrition, sometimes high when Techniques override severe bodily collapse windows
- **Identity notes:** Tolerance Techniques should feel like refusing physiological shutdown under suffering already in progress. They belong to pain endurance, poison resistance, wound function, and bodily persistence under internal damage, not to travel pacing or climate adaptation.
- **Should not do:** travel acceleration, environmental adjustment before harm lands, mental composure, broad ally support

---

## Cunning

### Orientation

- **Fantasy core:** constructing usable direction from uncertain terrain, incomplete references, and shifting positional information
- **Primary tags:** `utility`, `setup`, `survival_window`
- **Secondary tags:** `mobility`, `reposition`, `stability`
- **Rare or limited tags:** `attack`, `control`, `support`
- **Typical targets:** `self`, `ally`, `route`, `environment`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low rhythm, low Attrition, usually shaped by uncertainty rather than hostility
- **Identity notes:** Orientation Techniques should feel like restoring direction, securing route sense, avoiding disorientation, or converting confusing space into actionable movement logic. They should not feel like following another creature's trail.
- **Should not do:** pursuit_reading, deception, broad offensive pressure, direct environmental resistance

### Tracking

- **Fantasy core:** reconstructing another being's path from marks, disturbances, and residual traces left in the world
- **Primary tags:** `utility`, `pressure`, `setup`
- **Secondary tags:** `survival_window`, `reposition`, `control`
- **Rare or limited tags:** `attack`, `recovery`, `support`
- **Typical targets:** `enemy`, `route`, `environment`, `object`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, often escalating over distance or degraded traces
- **Identity notes:** Tracking Techniques should feel like converting remnants into pursuit logic: holding a trail, reading movement history, predicting route continuation, or preventing escape through trace reading. They should not become generic navigation.
- **Should not do:** self_navigation_without_traces, broad_social_manipulation, direct_damage, abstract deduction_without_world_signs

### Intuition

- **Fantasy core:** reaching useful conclusions before evidence becomes explicit by reading dissonance, pattern tension, and incomplete signals
- **Primary tags:** `utility`, `counter_read`, `setup`
- **Secondary tags:** `defense`, `survival_window`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `self`, `enemy`, `ally`, `zone`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low rhythm, low Attrition, often triggered by ambiguity, hidden intent, or unseen danger
- **Identity notes:** Intuition Techniques should feel like catching structure before it fully appears: reading motive, sensing a trap, anticipating an angle, or exploiting a pattern not yet visible in full. They should not drift into raw sensory detection or mystical instinct.
- **Should not do:** direct_perception, bodily_survival, overt_social_pressure, formal_scholarship

### Deception

- **Fantasy core:** imposing a false frame on another mind through convincing lies, omissions, and deliberate narrative control
- **Primary tags:** `utility`, `control`, `setup`
- **Secondary tags:** `pressure`, `disruption`, `counter_read`
- **Rare or limited tags:** `attack`, `recovery`, `mobility`
- **Typical targets:** `enemy`, `ally`, `group`, `zone`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, rising when layered or sustained under suspicion
- **Identity notes:** Deception Techniques should feel like making a false version of events function long enough to alter action, trust, or tempo. They should manipulate belief, not fear, disguise, or bodily concealment.
- **Should not do:** identity_replication, direct_terror_pressure, generic_stealth, precision_theft

### Improvisation

- **Fantasy core:** producing a workable answer under immediate pressure with poor tools, incomplete plans, and whatever the scene allows
- **Primary tags:** `utility`, `setup`, `disruption`
- **Secondary tags:** `survival_window`, `control`, `recovery`
- **Rare or limited tags:** `attack`, `support`, `precision`
- **Typical targets:** `self`, `ally`, `object`, `environment`, `zone`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** moderate rhythm, low-to-medium Attrition, often paid through risk, fragility, or resource consumption
- **Identity notes:** Improvisation Techniques should feel like making something usable out of the wrong conditions. They should create temporary answers, unstable fixes, opportunistic tools, or scene-level turns without becoming formal engineering or fine manual mastery.
- **Should not do:** robust_long_term_construction, exact_handcraft, pure_social_manipulation, reliable_healing

### Theft

- **Fantasy core:** taking control of something that is not yours through opportunity, timing, distraction, and exit before response closes
- **Primary tags:** `utility`, `setup`, `pressure`
- **Secondary tags:** `control`, `disruption`, `escape`
- **Rare or limited tags:** `attack`, `support`, `recovery`
- **Typical targets:** `enemy`, `object`, `zone`, `self`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low rhythm, low Attrition, but often high exposure if the window closes or alert rises
- **Identity notes:** Theft Techniques should feel like opportunistic acquisition under risk: lift, slip, remove, transfer, or strip access without open confrontation. They should not become generic fine manipulation or broad stealth identity.
- **Should not do:** pure_manual_precision_without_acquisition, open_combat_pressure, identity_deception, broad_navigation

---

## Wisdom

### Perception

- **Fantasy core:** extracting actionable detail from what is already present in the scene before it slips away or stays unnoticed
- **Primary tags:** `utility`, `counter_read`, `setup`
- **Secondary tags:** `defense`, `survival_window`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `recovery`, `support`
- **Typical targets:** `self`, `enemy`, `environment`, `object`, `zone`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low rhythm, low Attrition, usually paid through timing and line of exposure rather than bodily strain
- **Identity notes:** Perception Techniques should feel like catching what is there before it is lost: exposed detail, hidden motion, faint signal, or dangerous presence. They should not drift into inference, formal interpretation, or trace-based pursuit.
- **Should not do:** abstract_deduction, historical_analysis, environmental_resistance, deception

### Survival

- **Fantasy core:** making the right practical decision to keep people alive and functional in hostile terrain or natural pressure
- **Primary tags:** `survival_window`, `utility`, `setup`
- **Secondary tags:** `recovery`, `mitigation`, `stability`
- **Rare or limited tags:** `attack`, `control`, `pressure`
- **Typical targets:** `self`, `ally`, `route`, `environment`, `zone`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-moderate rhythm, low-to-medium Attrition, often extended over scenes of scarcity or exposure
- **Identity notes:** Survival Techniques should feel like field judgment: shelter choice, water logic, immediate resource use, route safety, and practical adaptation to natural threat. They should not become internal bodily resistance or clinical treatment.
- **Should not do:** direct_body_adaptation, formal_healing, abstract_navigation_without_field_logic, broad_offense

### Medicine

- **Fantasy core:** intervening on bodily harm with trained care to stabilize, restore function, or buy time before collapse
- **Primary tags:** `recovery`, `mitigation`, `survival_window`
- **Secondary tags:** `utility`, `condition_reduction`, `stability`
- **Rare or limited tags:** `attack`, `mobility`, `pressure`
- **Typical targets:** `self`, `ally`, rarely `enemy`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** moderate rhythm, low-to-medium Attrition, often constrained by tools, time, and patient state
- **Identity notes:** Medicine Techniques should feel like practiced intervention on damage already present: stabilizing, treating, reducing consequences, or restoring immediate bodily function. They should not become pain endurance, ingredient identification, or compound production by themselves.
- **Should not do:** passive_toughness, environmental_adaptation, raw_ingredient_recognition, broad_mechanical_control

### Herbalism

- **Fantasy core:** recognizing, gathering, and putting plant matter to practical use before it spoils, is misread, or goes unfound
- **Primary tags:** `utility`, `setup`, `recovery`
- **Secondary tags:** `mitigation`, `survival_window`, `support`
- **Rare or limited tags:** `attack`, `control`, `precision`
- **Typical targets:** `self`, `ally`, `object`, `environment`, `ingredient`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low rhythm, low Attrition, usually shaped by access, season, and specimen quality
- **Identity notes:** Herbalism Techniques should feel like plant-resource mastery: finding, classifying, preserving, and preparing flora for use. They should not drift into clinical treatment or elaborate compound engineering.
- **Should not do:** direct_surgery, complex_reagent_transformation, structural_mechanics, pure_sensory_detection

### Alchemy

- **Fantasy core:** transforming ingredients into functional compounds through process, preparation, and controlled reaction
- **Primary tags:** `utility`, `setup`, `condition_reduction`
- **Secondary tags:** `recovery`, `attack`, `mitigation`
- **Rare or limited tags:** `mobility`, `pressure`, `support`
- **Typical targets:** `self`, `ally`, `enemy`, `object`, `ingredient`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** moderate rhythm, low-to-medium Attrition, often paid through ingredient value, preparation time, and failure risk
- **Identity notes:** Alchemy Techniques should feel like making effects through compounds: antitoxins, toxins, reactive agents, extracts, and prepared responses. They should not become ingredient gathering, direct healing procedure, or structural engineering.
- **Should not do:** raw_resource_identification, clinical_body_work, terrain_navigation, broad_social_control

### Traps

- **Fantasy core:** shaping a delayed or conditional response that turns space, passage, or interaction into a controlled danger or lock
- **Primary tags:** `control`, `setup`, `pressure`
- **Secondary tags:** `disruption`, `utility`, `counter_positioning`
- **Rare or limited tags:** `recovery`, `support`, `mobility`
- **Typical targets:** `enemy`, `route`, `zone`, `object`, `environment`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** moderate rhythm, low-to-medium Attrition, often paid through preparation, material, and placement constraints
- **Identity notes:** Traps Techniques should feel like conditional mechanism logic: arming, disarming, redirecting triggers, weaponizing passage, or securing an approach. They should not become broad engineering or mere fine-hand execution.
- **Should not do:** generic_precision_work, long_term_architecture, direct_healing, open_melee_pressure

### Mining

- **Fantasy core:** reading and extracting the earth without losing the material, the route, or the stability that makes extraction possible
- **Primary tags:** `utility`, `setup`, `stability`
- **Secondary tags:** `survival_window`, `recovery`, `control`
- **Rare or limited tags:** `attack`, `mobility`, `pressure`
- **Typical targets:** `environment`, `object`, `route`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** moderate rhythm, medium Attrition, strongly shaped by tool load, collapse risk, and extraction duration
- **Identity notes:** Mining Techniques should feel like subsurface judgment and extraction discipline: reading seams, preserving tunnels, securing access, and recovering material from stone. They should not become forging, general engineering, or broad exploration logic.
- **Should not do:** metal_shaping, abstract_system_design, direct_social_influence, bodily_resistance

### Smithing

- **Fantasy core:** shaping or restoring functional metal through heat, force, timing, and material judgment
- **Primary tags:** `utility`, `recovery`, `setup`
- **Secondary tags:** `mitigation`, `attack`, `stability`
- **Rare or limited tags:** `mobility`, `pressure`, `counter_read`
- **Typical targets:** `object`
- **Typical types:** `active`
- **Usual cost profile:** moderate rhythm, medium Attrition, often paid through labor load, heat access, and material stakes
- **Identity notes:** Smithing Techniques should feel like functional metalwork: repair, reinforcement, reshaping, stress reading, or forging under pressure. They should not become fine luxury detail work or general system design.
- **Should not do:** jewel_precision, broad_mechanical_architecture, terrain_survival, deception

### Tailoring

- **Fantasy core:** restoring or configuring flexible material so it keeps function, fit, and integrity under use
- **Primary tags:** `utility`, `recovery`, `mitigation`
- **Secondary tags:** `setup`, `support`, `stability`
- **Rare or limited tags:** `attack`, `pressure`, `control`
- **Typical targets:** `object`, `ally`, `self`
- **Typical types:** `active`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, shaped by material quality, time, and precision of adjustment
- **Identity notes:** Tailoring Techniques should feel like practical textile mastery: fit correction, fabric restoration, strap or seam function, and flexible gear readiness. They should not drift into jewelry-scale finesse or metalwork.
- **Should not do:** fine_gem_work, structural_mechanics, direct_damage, pursuit_logic

### Jewelry

- **Fantasy core:** preserving value and function in small, delicate, high-precision crafted pieces
- **Primary tags:** `utility`, `precision`, `setup`
- **Secondary tags:** `recovery`, `support`, `control`
- **Rare or limited tags:** `attack`, `mobility`, `survival_window`
- **Typical targets:** `object`
- **Typical types:** `active`
- **Usual cost profile:** low rhythm, low Attrition, but high consequence on mistakes because of scale and value
- **Identity notes:** Jewelry Techniques should feel like exact fine-scale craft: setting, separating, restoring, concealing detail in precious work, or manipulating small high-value pieces without ruining them. They should not become heavy forge labor or broad engineering.
- **Should not do:** structural_forging, field_survival, large_scale_repair, open_combat_pressure

### Engineering

- **Fantasy core:** understanding and altering how a complex physical system functions as a whole under load, access, and failure pressure
- **Primary tags:** `utility`, `control`, `setup`
- **Secondary tags:** `mitigation`, `disruption`, `recovery`
- **Rare or limited tags:** `attack`, `pressure`, `stealth`
- **Typical targets:** `object`, `device`, `structure`, `route`, `environment`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** moderate rhythm, medium Attrition, often paid through complexity, tool demands, and cascade-failure risk
- **Identity notes:** Engineering Techniques should feel like system logic under intervention: understanding load paths, bypassing mechanisms, stabilizing or redirecting function, and altering structure as a coherent whole. They should not become improvisation, trap logic alone, or single-material craft.
- **Should not do:** fragile_temporary_fix_as_identity, fine_manual_pickwork, botanical_resource_work, broad_party_leadership

---

## Intellect

### Identification

- **Fantasy core:** naming exactly what something is before action misfires through category error or false assumption
- **Primary tags:** `utility`, `counter_read`, `setup`
- **Secondary tags:** `survival_window`, `disruption`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `object`, `enemy`, `creature`, `phenomenon`, `zone`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low rhythm, low Attrition, usually paid through access to sample quality and observation time
- **Identity notes:** Identification Techniques should feel like precise classification under uncertainty: knowing what stands before you, what category it belongs to, and what framework applies next. They should not become interpretive meaning-making or pure detection.
- **Should not do:** symbolic_analysis_as_primary, sensory_search, direct_healing, route_navigation

### Interpretation

- **Fantasy core:** extracting implication, structure, and meaning from information that is already present but not yet understood
- **Primary tags:** `utility`, `pattern_exploitation`, `setup`
- **Secondary tags:** `counter_read`, `disruption`, `survival_window`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `zone`, `object`, `text`, `enemy`, `structure`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, often constrained by ambiguity and analysis time
- **Identity notes:** Interpretation Techniques should feel like turning evidence into implication: what the pattern means, what the layout implies, what the sign points toward. They should not become raw intuition, linguistic decoding, or mere classification.
- **Should not do:** direct_classification_without_meaning, pure_detection, social_deception, bodily_resistance

### Linguistics

- **Fantasy core:** opening real language systems so speech, text, or inscription becomes legible enough to act on
- **Primary tags:** `utility`, `setup`, `counter_read`
- **Secondary tags:** `disruption`, `support`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `mobility`, `mitigation`
- **Typical targets:** `text`, `creature`, `message`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low rhythm, low Attrition, usually shaped by exposure length, language distance, and text quality
- **Identity notes:** Linguistics Techniques should feel like unlocking language as language: grammar, register, structure, semantic pattern, and translation opening. They should not become cryptographic breakwork or social rhetoric.
- **Should not do:** deliberate_codebreaking_as_primary, negotiation_pressure, battlefield_command, direct_damage

### Thaumaturgy

- **Fantasy core:** understanding thaumic logic as a formal system before manifestation, distortion, or contact becomes uncontrollable
- **Primary tags:** `utility`, `mitigation`, `condition_reduction`
- **Secondary tags:** `counter_read`, `setup`, `disruption`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `phenomenon`, `object`, `zone`, `structure`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** moderate rhythm, low-to-medium Attrition, often raised by instability, contamination, or volatility of the phenomenon
- **Identity notes:** Thaumaturgy Techniques should feel like formal contact-through-understanding: reading laws, identifying distortion patterns, suppressing or redirecting thaumic behavior through knowledge. They should not become resonance, doctrine, or instinctive aura response.
- **Should not do:** faith_interpretation, emotional_alignment, raw_aura_contact, mundane_navigation

### History

- **Fantasy core:** bringing organized precedent to bear so present action benefits from what similar systems, peoples, or crises have already done
- **Primary tags:** `utility`, `setup`, `pattern_exploitation`
- **Secondary tags:** `counter_read`, `support`, `disruption`
- **Rare or limited tags:** `attack`, `mobility`, `recovery`
- **Typical targets:** `zone`, `group`, `object`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low rhythm, low Attrition, usually dependent on contextual fit rather than pressure cost
- **Identity notes:** History Techniques should feel like using precedent as leverage: recognizing cycles, recalling prior methods, anticipating inherited patterns, or exposing continuity with the past. They should not become archaeology or immediate tactical reading.
- **Should not do:** material_site_excavation, direct_social_command, physical_repair, live_tracking

### Geography

- **Fantasy core:** using organized knowledge of regions, terrain systems, and large-scale spatial relations to shape present movement or strategy
- **Primary tags:** `utility`, `setup`, `survival_window`
- **Secondary tags:** `mobility`, `support`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `recovery`, `control`
- **Typical targets:** `route`, `environment`, `group`, `zone`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low rhythm, low Attrition, mostly paid through precision demands and incomplete references
- **Identity notes:** Geography Techniques should feel like macro-spatial knowledge becoming actionable: regional layout, chokepoints, territorial logic, and broad terrain structure. They should not become immediate route finding or field survival judgment.
- **Should not do:** real_time_navigation_without_knowledge_base, subsurface_extraction, direct_healing, deception

### Astronomy

- **Fantasy core:** reading celestial order as a stable information system for timing, orientation, and large-cycle inference
- **Primary tags:** `utility`, `setup`, `pattern_exploitation`
- **Secondary tags:** `survival_window`, `counter_read`, `support`
- **Rare or limited tags:** `attack`, `mobility`, `control`
- **Typical targets:** `environment`, `phenomenon`, `route`, `zone`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low rhythm, low Attrition, often constrained by visibility, timing, and precision of observation
- **Identity notes:** Astronomy Techniques should feel like extracting usable order from the sky: timing windows, celestial correlation, macro-pattern reading, or night-based orientation by formal knowledge. They should not become theology or immediate instinctive sky-reading.
- **Should not do:** doctrinal_meaning_as_primary, bodily_resistance, direct_combat_pressure, raw_language_decoding

### Theology

- **Fantasy core:** understanding religious systems, doctrines, rites, and sacred authority as structured knowledge that shapes behavior and interpretation
- **Primary tags:** `utility`, `counter_read`, `setup`
- **Secondary tags:** `support`, `disruption`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `mobility`, `mitigation`
- **Typical targets:** `ritual`, `symbol`, `group`, `zone`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low rhythm, low Attrition, shaped mostly by obscurity, syncretism, and doctrinal depth
- **Identity notes:** Theology Techniques should feel like doctrinal literacy becoming leverage: recognizing authority structures, ritual implications, symbolic consistency, and sacred logic. They should not become thaumic science or aura-born response.
- **Should not do:** direct_taumic_analysis, resonance_contact, battlefield_force_projection, practical_crafting

### Cryptology

- **Fantasy core:** breaking systems intentionally designed to deny access, using structure, repetition, and concealed order against themselves
- **Primary tags:** `utility`, `counter_read`, `disruption`
- **Secondary tags:** `setup`, `pattern_exploitation`, `control`
- **Rare or limited tags:** `attack`, `mobility`, `recovery`
- **Typical targets:** `message`, `device`, `text`, `phenomenon`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, often paid through sample scarcity, urgency, and cognitive load
- **Identity notes:** Cryptology Techniques should feel like opening what was deliberately sealed: code, cipher, obfuscation, or patterned concealment. They should not become ordinary language work or broad interpretation after the code is already open.
- **Should not do:** natural_language_translation_as_primary, doctrinal_analysis, route_planning, direct_damage

### Archaeology

- **Fantasy core:** reading material remains as evidence of lost use, culture, sequence, and intent
- **Primary tags:** `utility`, `pattern_exploitation`, `counter_read`
- **Secondary tags:** `setup`, `support`, `survival_window`
- **Rare or limited tags:** `attack`, `mobility`, `recovery`
- **Typical targets:** `site`, `object`, `structure`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, usually shaped by access, preservation state, and sample breadth
- **Identity notes:** Archaeology Techniques should feel like reconstructing vanished life from physical remainder: sequence, usage, maker, culture, and loss. They should not become document-based history or structural engineering.
- **Should not do:** text_only_historical_analysis, mechanism_override, direct_social_pressure, clinical_restoration

### Architecture

- **Fantasy core:** reading built space as intention, flow, concealment, and structural habitability
- **Primary tags:** `utility`, `setup`, `control`
- **Secondary tags:** `mitigation`, `pattern_exploitation`, `counter_positioning`
- **Rare or limited tags:** `attack`, `recovery`, `pressure`
- **Typical targets:** `structure`, `route`, `zone`, `site`, `environment`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, often paid through access limits and complexity of the built form
- **Identity notes:** Architecture Techniques should feel like understanding how built space wants movement, concealment, and habitation to happen: hidden volumes, intended circulation, structural logic, and design intent. They should not become engineering of mechanisms or archaeological culture reading.
- **Should not do:** device_level_mechanics, excavation_logic, direct_offense, botanical_resource_handling

### Belicology

- **Fantasy core:** understanding conflict as doctrine, deployment, logistics, and war-system rather than isolated combat moments
- **Primary tags:** `utility`, `setup`, `pattern_exploitation`
- **Secondary tags:** `control`, `pressure`, `counter_read`
- **Rare or limited tags:** `recovery`, `mobility`, `attack`
- **Typical targets:** `enemy`, `group`, `zone`, `formation`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, usually paid through information gaps and scale complexity
- **Identity notes:** Belicology Techniques should feel like formal war literacy becoming tactical leverage: reading deployment, anticipating doctrine, understanding logistical posture, or identifying systemic weakness in organized conflict. They should not become live leadership or raw weapon execution.
- **Should not do:** real_time_command_as_primary, direct_weapon_mastery, healing_work, stealth_infiltration

---

## Composure

### Focus

- **Fantasy core:** keeping the mind fixed on one necessary line of action while distraction, danger, or overload tries to break it
- **Primary tags:** `utility`, `setup`, `stability`
- **Secondary tags:** `counter_read`, `mitigation`, `survival_window`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `self`, `object`, `zone`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low rhythm, low Attrition, often paid through sustained cognitive strain under pressure
- **Identity notes:** Focus Techniques should feel like directed continuity of attention: holding the thread, ignoring noise, locking onto one operational line until it is done. They should not become emotional recovery or social façade control.
- **Should not do:** emotional_restoration, visible_social_masking, direct_damage, broad_group_support

### Containment

- **Fantasy core:** preventing internal breakage from panic, horror, or emotional overload before action collapses from within
- **Primary tags:** `mitigation`, `survival_window`, `condition_reduction`
- **Secondary tags:** `stability`, `utility`, `counter_read`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `self`, rarely `ally`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low rhythm, low-to-medium Attrition, higher when Techniques suppress severe internal rupture windows
- **Identity notes:** Containment Techniques should feel like holding the inside together under mental or emotional threat: not panicking, not collapsing, not losing agency to inner rupture. They should not become bodily toughness, calm restoration, or outward acting.
- **Should not do:** physical_pain_endurance, slow_restorative_practice, social_deception, travel_support

### Meditation

- **Fantasy core:** deliberately restoring clarity and inner balance through pause, practice, and cultivated return to center
- **Primary tags:** `recovery`, `condition_reduction`, `stability`
- **Secondary tags:** `mitigation`, `utility`, `support`
- **Rare or limited tags:** `attack`, `pressure`, `mobility`
- **Typical targets:** `self`, `ally`, `zone`
- **Typical types:** `active`, `passive`
- **Usual cost profile:** low rhythm, low Attrition, but strongly dependent on time, calm window, and environmental safety
- **Identity notes:** Meditation Techniques should feel like deliberate inward recomposition: quieting noise, reducing internal residue, regaining clarity, and preparing the self to act cleanly again. They should not become emergency panic resistance or mere concentration locking.
- **Should not do:** immediate_crisis_hold_as_primary, visible_status_management, direct_offense, trap_logic

### Poise

- **Fantasy core:** preserving outward composure so pressure, pain, shock, or fear do not become legible to others at the wrong moment
- **Primary tags:** `utility`, `control`, `counter_read`
- **Secondary tags:** `mitigation`, `setup`, `pressure`
- **Rare or limited tags:** `attack`, `recovery`, `mobility`
- **Typical targets:** `self`, `enemy`, `group`, `zone`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low rhythm, low Attrition, often paid through sustained visible strain under scrutiny
- **Identity notes:** Poise Techniques should feel like controlling what escapes outward: expression, bearing, tension, and visible fracture under pressure. They should not become the inner work of not breaking, nor full false-narrative deception.
- **Should not do:** internal_emotional_repair, deliberate_lie_construction, direct_weapon_pressure, structural_analysis

---

## Aura

### Instinct

- **Fantasy core:** responding from the deepest layer of self before analysis finishes or conscious certainty exists
- **Primary tags:** `counter_read`, `survival_window`, `setup`
- **Secondary tags:** `utility`, `mitigation`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `support`, `pressure`
- **Typical targets:** `self`, `enemy`, `zone`, `phenomenon`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low rhythm, low Attrition, usually triggered by exposure rather than deliberate exertion
- **Identity notes:** Instinct Techniques should feel like primary essential response: recoil, pull, recognition, refusal, or readiness before reason. They should not become trained inference, formal analysis, or deliberate attunement rituals.
- **Should not do:** structured_deduction, doctrinal_reading, explicit_social_control, mechanical_repair

### Resonance

- **Fantasy core:** actively tuning the aura toward a force, place, presence, or state until contact becomes meaningful
- **Primary tags:** `utility`, `counter_read`, `condition_reduction`
- **Secondary tags:** `setup`, `mitigation`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `phenomenon`, `zone`, `self`, `object`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low-to-moderate rhythm, low-to-medium Attrition, often paid through exposure to dissonance, interference, or intensity
- **Identity notes:** Resonance Techniques should feel like deliberate aura contact: tuning, sensing, aligning, or gently pushing into essential fields or beings. They should not become formal thaumic theory, involuntary instinct alone, or social persuasion.
- **Should not do:** academic_taumic_analysis, pure_reflex_response, direct_command_of_groups, brute_force_damage

### Bond

- **Fantasy core:** operating through a real sustained essential link that already exists between the self and a specific being
- **Primary tags:** `support`, `setup`, `counter_read`
- **Secondary tags:** `utility`, `mitigation`, `survival_window`
- **Rare or limited tags:** `attack`, `pressure`, `mobility`
- **Typical targets:** `self`, `ally`, `creature`
- **Typical types:** `active`, `passive`, sometimes `reactive`
- **Usual cost profile:** low rhythm, low Attrition, usually shaped by distance, strain on the bond, and the state of the linked being
- **Identity notes:** Bond Techniques should feel like leveraging continuity of connection: sensing across distance, stabilizing relation, sharing warning, or acting through a deep established tie. They should not become broad leadership, generic animal handling, or momentary aura touch.
- **Should not do:** crowd_influence, practical_beast_management, instant_contact_without_prior_link, direct_weapon_pressure

### Domestication

- **Fantasy core:** entering the response logic of an instinctive creature well enough to calm, guide, train, or prevent escalation
- **Primary tags:** `control`, `support`, `mitigation`
- **Secondary tags:** `setup`, `utility`, `survival_window`
- **Rare or limited tags:** `attack`, `pattern_exploitation`, `pressure`
- **Typical targets:** `creature`, `mount`, `self`, `zone`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, often paid through exposure risk, emotional agitation, and repeated handling pressure
- **Identity notes:** Domestication Techniques should feel like practical creature handling through instinctive communication and response shaping: calming, directing, familiarizing, and preventing a break into chaos. They should not become mounted technique, deep essential link by itself, or abstract social authority.
- **Should not do:** mounted_line_control, bond_depth_as_primary, doctrinal_understanding, battlefield_command

---

## Presence

### Leadership

- **Fantasy core:** turning your presence into recognized direction so multiple others move under a common line instead of fragmenting
- **Primary tags:** `support`, `control`, `setup`
- **Secondary tags:** `pressure`, `mitigation`, `survival_window`
- **Rare or limited tags:** `attack`, `stealth`, `recovery`
- **Typical targets:** `ally`, `group`, `formation`, `zone`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, often paid through sustained command strain and responsibility pressure
- **Identity notes:** Leadership Techniques should feel like authority becoming structure: rallying, re-centering, assigning, synchronizing, and preserving cohesion under stress. They should not become coercion by fear or abstract war scholarship.
- **Should not do:** terror_submission, doctrinal_analysis, identity_disguise, hidden_presence

### Negotiation

- **Fantasy core:** reshaping a contested social situation into an acceptable exchange before the window for agreement collapses
- **Primary tags:** `utility`, `control`, `support`
- **Secondary tags:** `setup`, `disruption`, `counter_read`
- **Rare or limited tags:** `attack`, `stealth`, `direct_mitigation`
- **Typical targets:** `enemy`, `ally`, `group`, `zone`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low rhythm, low Attrition, shaped by leverage, urgency, and how much position is exposed during the exchange
- **Identity notes:** Negotiation Techniques should feel like building agreement through structured exchange: concession, leverage, framing of terms, and converting hostility into deal-space. They should not become lies, intimidation, or command.
- **Should not do:** false_narrative_as_primary, fear_coercion, battlefield_leadership, stealth_entry

### Intimidation

- **Fantasy core:** making consequences feel immediate and credible enough that another party yields under your projected threat
- **Primary tags:** `pressure`, `control`, `disruption`
- **Secondary tags:** `setup`, `counter_read`, `survival_window`
- **Rare or limited tags:** `recovery`, `stealth`, `support`
- **Typical targets:** `enemy`, `group`, `zone`, `self`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low rhythm, low Attrition, but often high exposure if the threat fails or must be sustained
- **Identity notes:** Intimidation Techniques should feel like coercive presence: credible menace, dominance display, immediate pressure, and collapse of resistance through fear. They should not become voluntary coordination or negotiated reciprocity.
- **Should not do:** mutual_agreement_building, doctrine_reading, identity_performance, quiet_concealment

### Imitation

- **Fantasy core:** reproducing a recognizable person or social pattern convincingly enough to be treated as that thing instead of yourself
- **Primary tags:** `utility`, `setup`, `counter_read`
- **Secondary tags:** `control`, `disruption`, `pressure`
- **Rare or limited tags:** `attack`, `recovery`, `mobility`
- **Typical targets:** `self`, `group`, `creature`, `zone`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-moderate rhythm, low Attrition, increasing with scrutiny, exposure time, and fidelity demands
- **Identity notes:** Imitation Techniques should feel like embodied substitution: voice, manner, timing, and social pattern becoming persuasive enough to pass. They should not become broad lying without embodiment or simple invisibility to attention.
- **Should not do:** pure_verbal_deception_without_embodiment, hidden_presence_without_role, coercive_command, physical_damage

### Stealth

- **Fantasy core:** reducing how much the social and perceptual field registers you until you stop becoming a meaningful point of attention
- **Primary tags:** `stealth`, `setup`, `counter_read`
- **Secondary tags:** `mobility`, `survival_window`, `disruption`
- **Rare or limited tags:** `attack`, `support`, `recovery`
- **Typical targets:** `self`, `creature`, `route`, `zone`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low rhythm, low Attrition, often paid through sustained restraint, timing, and exposure management
- **Identity notes:** Stealth Techniques should feel like shrinking your perceptual footprint: softening presence, controlling rhythm, avoiding fixation, and sliding beneath active notice. They should not become impersonation, verbal deceit, or pure physical dexterity alone.
- **Should not do:** identity_substitution, explicit_bargaining, open_threat_projection, fine_manual_acquisition

---

## Next Blocks

Planned order:

No remaining planned blocks in this pass.

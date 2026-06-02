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

### Reading the invalid list

The **Invalid or overlapping techniques** section in each domain entry blocks three distinct problems — not one:

1. **Same-specialization upgrades.** Techniques that simply make the character better at the base specialization itself: jump farther, throw harder, track more accurately. This is the core invalid category.
2. **Domain trespass.** Techniques that reproduce what another specialization is specifically supposed to do — Deception replacing Stealth, Riding replacing Balance.
3. **Logic bypass.** Techniques that claim broad effects without using the specialization's actual logic — gaining general defense from Jumping without any impulse, landing, or impact mechanism.

A technique that **transfers** the specialization's underlying capabilities to a different problem is always valid. The invalid list does not block legitimate capability transfers. When reading an invalid entry, ask: *Is this blocked because it IS the base specialization done better, because it trespasses another specialization's core territory, or because it bypasses the specialization's logic requirements entirely?* If none of those apply, the technique is valid.

---

## Force — Derived Technique Domains

Techniques are not direct upgrades to the base specialization. A technique should not simply make the character jump farther, climb better, throw harder, swim faster, or grip harder.

Instead, each technique should express a transferable capability developed by that specialization and apply it to a different tactical, defensive, positional, or narrative problem.

### Jumping

- **Base specialization:** jumping, leaping, landing, crossing gaps, projecting the body through impulse.
- **Transferable capabilities:** explosive start, loaded momentum, impact absorption, landing control, angle change, body commitment, short-burst projection.
- **Technique identity:** Jumping Techniques do not need to involve an actual jump. They should express the body logic of jumping: impulse, launch, commitment, landing, recovery from impact, or converting stored force into sudden movement.
- **Primary tags:** `mobility`, `setup`, `pressure`
- **Secondary tags:** `attack`, `escape`, `reposition`, `recovery`
- **Rare or limited tags:** `control`, `defense`, `support`
- **Typical targets:** `self`, `enemy`, `route`, `zone`
- **Typical types:** `active`, rarely `reactive`
- **Usual cost profile:** moderate Rhythm, low-to-medium Attrition; higher when the technique commits the user into danger, absorbs heavy force, or overextends their position.
- **Design boundary:** A Jumping Technique should not make the character better at the basic act of jumping. It should use the physical lessons of jumping to solve another tactical problem.

#### Valid derived techniques

- Use explosive impulse to enter melee range without treating the technique as a normal movement action.
- Absorb part of a fall, shove, impact, or forced landing through trained landing control.
- Convert a short burst of momentum into pressure against an enemy’s position.
- Recover from being knocked off balance by redirecting the body into a controlled landing.
- Launch out of a threatened position before the enemy can fully close.
- Use a committed body entry to break through a narrow opening or unstable formation.
- Turn vertical drop, stumble, or uneven footing into an immediate reposition.
- Brace the body before impact, reducing the consequence of being thrown, slammed, or dropped.

#### Invalid or overlapping techniques

- Jump farther.
- Jump higher.
- Cross a gap without a check.
- Ignore difficult jump terrain.
- Gain a flat, passive bonus to all movement checks, unconnected from impulse, landing, commitment, or impact logic.
- Stay balanced indefinitely in the air.
- Avoid all fall damage without impact or landing logic.
- Move silently because the character is “good at jumping.”
- Gain broad defense without launch, landing, impulse, or impact logic.

---

### Climbing

- **Base specialization:** climbing, ascending, descending, hanging, holding position on vertical or unstable surfaces.
- **Transferable capabilities:** traction, anchoring, weight distribution, body tension, surface reading, controlled suspension, resisting pull through contact points.
- **Technique identity:** Climbing Techniques do not need to involve ascending or descending. They should express the body logic of climbing: finding purchase, anchoring the body, distributing weight, resisting loss of position, or acting from unstable support.
- **Primary tags:** `stability`, `mobility`, `escape`
- **Secondary tags:** `setup`, `reposition`, `defense`, `utility`
- **Rare or limited tags:** `attack`, `support`, `pressure`
- **Typical targets:** `self`, `object`, `route`, `environment`, `ally`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** moderate Rhythm, low-to-medium Attrition; higher when resisting force through poor support, hanging weight, unstable footing, or exposed terrain.
- **Design boundary:** A Climbing Technique should not make the character better at the basic act of climbing. It should use the physical lessons of climbing to solve another problem involving anchoring, tension, support, or unstable footing.

#### Valid derived techniques

- Resist forced movement by anchoring through nearby surfaces, edges, objects, or terrain.
- Keep footing on unstable ground by distributing weight like a climber on poor holds.
- Catch yourself on a ledge, railing, branch, wall, or object after being pushed or dropped.
- Use a wall, column, tree, or large object as a brace to change direction.
- Remain functional while hanging, crouched, braced, or supported from an awkward angle.
- Reduce the penalty for acting while suspended, prone against a slope, or balanced on narrow support.
- Hold an ally from falling by turning your body into an anchor.
- Use environmental purchase to avoid being dragged, pulled, or knocked loose.

#### Invalid or overlapping techniques

- Climb faster.
- Climb without a check.
- Ignore the difficulty of a wall.
- Automatically climb any surface.
- Gain vertical movement with no surface, anchor, or support.
- Immobilize an enemy without contact, leverage, or an anchoring point.
- Gain generic defense because the character is “good at climbing.”
- Provide ranged pressure unrelated to surfaces, anchors, or body tension.
- Replace Gripping by turning every hand contact into full control.

---

### Throwing

- **Base specialization:** throwing handheld objects, judging weight, projecting force, controlling release, shaping trajectory.
- **Transferable capabilities:** force transfer, release timing, weight reading, rotational power, trajectory control, impact reading, object commitment.
- **Technique identity:** Throwing Techniques may involve throwing, but they should not be limited to “throw object farther or harder.” They should express the body logic of throwing: judging weight, timing release, creating arcs, redirecting force, or turning objects into extensions of bodily pressure.
- **Primary tags:** `attack`, `pressure`, `setup`
- **Secondary tags:** `disruption`, `utility`, `precision`, `control`
- **Rare or limited tags:** `defense`, `recovery`, `support`
- **Typical targets:** `enemy`, `object`, `route`, `zone`, `environment`
- **Typical types:** `active`, rarely `reactive`
- **Usual cost profile:** low-to-medium Rhythm, low Attrition for simple projection; higher when the technique changes the scene, manipulates terrain, redirects force, or uses awkward objects.
- **Design boundary:** A Throwing Technique should not replace ranged weapons or make every object into a perfect weapon. It should use the physical lessons of throwing to solve problems of timing, angle, weight, distance, or impact.

#### Valid derived techniques

- Throw an object to interrupt a movement route, forcing an enemy to adjust their path.
- Strike a held object, tool, rope, lever, lantern, latch, or weak point from a short distance.
- Use a thrown object to create noise, distraction, pressure, or a brief opening.
- Redirect a loose object already in motion by reading its weight and trajectory.
- Use rotational force to disarm, pull, or unbalance through a thrown cord, hook, weight, or attached object.
- Bounce or angle a thrown object off a nearby surface to reach a difficult line.
- Create a temporary hazard by throwing debris, sand, powder, fragments, or caltrop-like objects.
- Use a thrown object to pin cloth, rope, paper, hide, or light material to a surface.

#### Invalid or overlapping techniques

- Throw farther.
- Throw more accurately with no specific tactical application.
- Treat any object as a full weapon without limitation.
- Replace bows, slings, crossbows, or other projectile weapons.
- Make constant passive ranged attacks.
- Apply non-physical control with no object, force, trajectory, or impact logic.
- Gain broad defense against attacks using trajectory expertise as the only justification, without specific projectile interception, arc deflection, or direct impact redirection logic.
- Create broad area control without enough material or projectile logic.
- Inflict complex conditions without a clear impact, object, or delivery method.

---

### Swimming

- **Base specialization:** swimming, diving, surfacing, floating, staying functional in water, moving through aquatic resistance.
- **Transferable capabilities:** resisting drag, recovering body axis, breath control, moving through resistance, maintaining orientation without firm ground, conserving effort under pressure.
- **Technique identity:** Swimming Techniques do not need to occur in water. They should express the body logic of swimming: resisting current, recovering orientation, controlling breath, moving through resistance, or staying functional when footing and rhythm are compromised.
- **Primary tags:** `stability`, `recovery`, `escape`
- **Secondary tags:** `mobility`, `survival_window`, `reposition`, `defense`
- **Rare or limited tags:** `attack`, `support`, `control`
- **Typical targets:** `self`, `route`, `environment`, `enemy`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** medium Rhythm, medium Attrition; highly dependent on pressure, resistance, lack of footing, armor, current, panic, or hostile terrain.
- **Design boundary:** A Swimming Technique should not make the character better at the basic act of swimming. It should use the physical lessons of swimming to solve another problem involving drag, breath, current, pressure, or loss of stable footing.

#### Valid derived techniques

- Reduce forced movement by treating a shove, pull, or drag like a current.
- Recover posture after being displaced, spun, knocked prone, or moved involuntarily.
- Control breathing in smoke, dust, panic, water, tight spaces, or physical pressure.
- Move through mud, snow, crowds, vegetation, rubble, or other resisting terrain.
- Keep orientation while sliding, falling into water, tumbling downhill, or being carried by force.
- Surface, rise, or regain footing after being submerged, buried, dragged, or overwhelmed.
- Conserve effort during a long physical struggle by pacing breath and movement.
- Resist panic when deprived of stable ground, clear direction, or normal rhythm.

#### Invalid or overlapping techniques

- Swim faster.
- Swim without a check.
- Cross water automatically.
- Ignore currents without resistance logic.
- Avoid drowning automatically.
- Gain generic environmental resistance.
- Ignore all difficult terrain.
- Move better in any terrain without drag, breath, current, or orientation logic.
- Gain long-range offense unrelated to water, pressure, or movement through resistance.

---

### Gripping

- **Base specialization:** gripping, holding, retaining, grabbing, keeping contact, controlling an object or body through the hands.
- **Transferable capabilities:** retention, friction control, contact reading, anchoring through the hands, pressure through fingers and palms, denying removal, maintaining a contested point of contact.
- **Technique identity:** Gripping Techniques do not need to be full grapples. They should express the body logic of gripping: keeping hold, denying escape, reading tension through contact, stabilizing another body, or controlling an object at the moment of contest.
- **Primary tags:** `control`, `interception`, `anti_displacement`
- **Secondary tags:** `defense`, `setup`, `pressure`, `stability`, `utility`
- **Rare or limited tags:** `mobility`, `recovery`, `support`
- **Typical targets:** `enemy`, `ally`, `object`, `self`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-medium Rhythm; medium Attrition when sustaining contact, resisting force, preventing loss, or contesting movement.
- **Design boundary:** A Gripping Technique should not turn every contact into full immobilization. It should use the physical lessons of gripping to solve another problem involving retention, contact, friction, or contested control.

#### Valid derived techniques

- Prevent being disarmed by maintaining retention under pressure.
- Keep hold of a rope, ledge, weapon, shield, tool, or carried object during impact.
- Grab an ally before they fall, slide, or get pulled away.
- Hold a door, chain, lever, wheel, harness, or mechanism in place under resistance.
- Read tension through contact to anticipate whether a creature is pulling, twisting, retreating, or striking.
- Briefly deny forced movement by catching a limb, strap, clothing, handle, or edge.
- Maintain contact with an enemy long enough to set up another action.
- Stop an object from being taken, opened, drawn, dropped, or removed.

#### Invalid or overlapping techniques

- Grip harder.
- Automatically grapple a creature.
- Fully immobilize an enemy without established contact.
- Control an enemy’s whole body from a minor touch.
- Apply ranged pressure.
- Gain generic melee advantage.
- Prevent all movement in a broad area.
- Replace Climbing by turning all surface contact into full anchoring.
- Replace Throwing by controlling objects at distance without contact, attachment, or trajectory logic.

---

## Agility — Derived Technique Domains

Techniques are not direct upgrades to the base specialization. A technique should not simply make the character tumble better, manipulate objects faster, balance more easily, or ride faster.

Instead, each technique should express a transferable capability developed by that specialization and apply it to a different tactical, defensive, positional, or narrative problem.

---

### Acrobatics

- **Base specialization:** tumbling, rolling, vaulting, recovering through motion, traversing danger with dynamic body control.
- **Transferable capabilities:** redirection of momentum, fall recovery, rolling through impact, fluid transition, evasive body shaping, movement continuity, spatial threading.
- **Technique identity:** Acrobatics Techniques do not need to be simple flips or tumbles. They should express the body logic of acrobatics: redirecting bad momentum, passing through narrow danger, recovering through motion, avoiding hard stops, or turning unstable movement into continued agency.
- **Primary tags:** `mobility`, `escape`, `reposition`
- **Secondary tags:** `defense`, `setup`, `spacing`, `recovery`
- **Rare or limited tags:** `control`, `support`, `pressure`
- **Typical targets:** `self`, `route`, `zone`, `enemy`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** moderate Rhythm, low-to-medium Attrition; higher when chained under pressure, used after impact, or performed through hostile spaces.
- **Design boundary:** An Acrobatics Technique should not make the character better at the basic act of performing acrobatics. It should use the physical lessons of acrobatics to solve problems of momentum, evasion, recovery, or movement continuity.

#### Valid derived techniques

- Roll with a hit to reposition instead of stopping in place.
- Convert a failed movement angle into a partial escape route.
- Pass through a narrow threatened space by folding, ducking, or turning the body.
- Recover from being knocked prone by continuing the motion into a new stance.
- Reduce the consequence of falling, sliding, or being thrown by rolling through the impact.
- Avoid being surrounded by using continuous movement to slip through a closing gap.
- Turn a dodge into a setup for a later attack or escape.
- Move through cluttered terrain without losing all tactical rhythm, as long as the motion remains dynamic.

#### Invalid or overlapping techniques

- Perform a generic acrobatic stunt with no tactical consequence.
- Gain a flat, passive bonus to all movement checks, unconnected from momentum redirection, evasion, recovery, or movement continuity logic.
- Maintain static balance on a narrow surface.
- Pick locks, tie knots, or manipulate small mechanisms.
- Command a mount through difficult terrain.
- Resist emotional pressure because the character is “flexible.”
- Push, shove, or break through obstacles by force.
- Gain broad defense without motion, redirection, evasion, or recovery logic.
- Become invisible or stealthy because the movement is graceful.

---

### Dexterity

- **Base specialization:** precise hand work, fine object manipulation, delicate adjustment, technical execution under pressure.
- **Transferable capabilities:** fine motor control, careful placement, tension control, micro-adjustment, tool handling, timing of small movements, tactile precision.
- **Technique identity:** Dexterity Techniques should not simply make the character “better with hands.” They should express precise manipulation under pressure: placing, adjusting, loosening, tightening, threading, disabling, catching, preparing, or altering something at the exact point of contact.
- **Primary tags:** `utility`, `setup`, `precision`
- **Secondary tags:** `control`, `disruption`, `support`
- **Rare or limited tags:** `attack`, `mobility`, `pressure`
- **Typical targets:** `object`, `self`, `ally`, `enemy`
- **Typical types:** `active`, rarely `reactive`
- **Usual cost profile:** low-to-medium Rhythm, low Attrition for controlled work; medium Attrition when performed under danger, time pressure, or extreme precision requirements.
- **Design boundary:** A Dexterity Technique should not replace Theft, Stealth, Acrobatics, or brute force. It should use the physical lessons of precise manipulation to solve problems involving objects, tools, contact points, mechanisms, bindings, preparations, or delicate timing.

#### Valid derived techniques

- Adjust a strap, buckle, clasp, knot, or fastening during combat without fully stopping.
- Prepare a small object, tool, vial, wire, hook, or mechanism as part of another action.
- Loosen or disable a simple object already within reach.
- Catch or secure a small falling object before it is lost or broken.
- Apply a substance, residue, poison, pigment, resin, or mark with controlled placement.
- Sabotage a visible tool, weapon component, hinge, latch, cord, or exposed mechanism.
- Stabilize a fragile object or wound dressing with careful hand pressure.
- Make a precise hand movement while threatened, moving, restrained, or under observation.

#### Invalid or overlapping techniques

- Pickpocket someone unnoticed without Theft or concealment logic.
- Sneak past enemies because the character has precise hands.
- Perform broad locomotion or acrobatic traversal.
- Force open a door, break a restraint, or overpower a mechanism by strength.
- Create social influence through delicate gestures alone.
- Automatically solve complex mechanisms without information or time.
- Gain generic attack bonuses because the character is “precise.”
- Replace crafting, medicine, sabotage, or lockpicking specializations entirely.
- Control an enemy’s whole body through a minor touch.

---

### Balance

- **Base specialization:** maintaining posture, footing, center of gravity, and bodily control under unstable support or external force.
- **Transferable capabilities:** centerline recovery, weight correction, posture preservation, anti-displacement, controlled stillness, pressure distribution, resisting loss of footing.
- **Technique identity:** Balance Techniques should not simply mean “the character does not fall.” They should express the body logic of balance: preserving action while unstable, correcting posture under force, resisting displacement, turning poor footing into usable footing, or keeping tactical continuity when the body should be interrupted.
- **Primary tags:** `defense`, `stability`, `anti_displacement`
- **Secondary tags:** `mobility`, `setup`, `reposition`, `recovery`
- **Rare or limited tags:** `attack`, `support`, `pressure`
- **Typical targets:** `self`, `route`, `enemy`, `environment`
- **Typical types:** `reactive`, occasionally `active`
- **Usual cost profile:** low Rhythm, low-to-medium Attrition; often triggered by hostile force, unstable terrain, narrow support, impact, or sudden movement.
- **Design boundary:** A Balance Technique should not replace Acrobatics or Climbing. It should use the physical lessons of balance to solve problems of posture, footing, displacement, or interrupted stance.

#### Valid derived techniques

- Resist being knocked prone by correcting posture at the moment of impact.
- Reduce forced movement by shifting weight into the pressure.
- Keep agency on ice, mud, loose stones, wet ground, slopes, narrow beams, or unstable platforms.
- Maintain your stance after attacking from poor footing.
- Avoid losing an action when the ground shifts, collapses, tilts, or trembles.
- Turn a stumble into a controlled step instead of a fall.
- Hold a defensive line while being pushed, pulled, or crowded.
- Keep a weapon, shield, or body posture aligned despite unstable terrain.

#### Invalid or overlapping techniques

- Perform flips, rolls, vaults, or dynamic evasive movement.
- Climb a wall or hang from a surface.
- Manipulate small objects with precision.
- Command or stabilize a mount.
- Resist fear, confusion, or emotional pressure.
- Ignore all difficult terrain without footing or posture logic.
- Gain broad defense against ranged attacks without stability logic.
- Move through enemy spaces by acrobatic redirection.
- Become immovable in all situations without cost, stance, or surface logic.

---

### Riding

- **Base specialization:** riding, mounted maneuvering, staying mounted, directing a mount under speed, pressure, or unstable conditions.
- **Transferable capabilities:** shared rhythm, weight signaling, mounted balance, line control through another body, speed management, mounted recovery, rider-mount coordination.
- **Technique identity:** Riding Techniques should not simply make the mount faster or better trained. They should express the tactical system formed by rider and mount: shared movement, charge angle, mounted repositioning, pressure through speed, preserving control under threat, or using the mount’s body as part of the rider’s action.
- **Primary tags:** `mobility`, `setup`, `pressure`
- **Secondary tags:** `reposition`, `escape`, `control`, `stability`
- **Rare or limited tags:** `recovery`, `support`, `precision`
- **Typical targets:** `self`, `creature`, `route`, `enemy`, `zone`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** moderate Rhythm, medium Attrition when maneuvering hard, fighting for control, changing speed abruptly, or acting under mounted pressure.
- **Design boundary:** A Riding Technique should not become animal training, animal bonding, or general creature command. It should use the physical and tactical lessons of riding to solve problems of speed, mounted control, shared positioning, charge lines, or rider-mount integrity.

#### Valid derived techniques

- Redirect a mount’s movement without fully losing speed.
- Keep your seat when struck, shoved, startled, or forced through unstable terrain.
- Convert a mounted approach into pressure against an enemy’s position.
- Use the mount’s body to block, screen, or open a route.
- Shift weight to help the mount turn, stop, brace, or recover.
- Preserve control when the mount panics, slips, rears, or is partially obstructed.
- Attack, defend, or interact while maintaining mounted rhythm.
- Reposition an ally or enemy through mounted movement, if the mount’s body and route support it.

#### Invalid or overlapping techniques

- Train an animal faster.
- Calm any beast through emotional connection.
- Give broad party support because the rider is inspiring.
- Gain static defense without mount movement, position, or body logic.
- Command animals that are not being ridden or directly handled.
- Make the mount ignore all terrain, fear, pain, or exhaustion.
- Replace Balance for non-mounted posture problems.
- Replace Animal Handling, bonding, or training systems.
- Apply mounted pressure when there is no mount, route, speed, or shared movement involved.

---

## Tenacity — Derived Technique Domains

Techniques are not direct upgrades to the base specialization. A technique should not simply make the character march longer, ignore climate, or endure pain better.

Instead, each technique should express a transferable capability developed by that specialization and apply it to a different tactical, defensive, positional, survival, or narrative problem.

---

### March

- **Base specialization:** marching, sustained travel, long-distance movement, keeping pace, carrying load across distance, preserving route function over time.
- **Transferable capabilities:** pace discipline, exertion pacing, route endurance, load management, breath cadence, long-scene momentum, refusal of travel collapse, operational rhythm.
- **Technique identity:** March Techniques do not need to be literal travel actions. They should express the body logic of marching: keeping forward function under prolonged exertion, preserving pace through fatigue, distributing effort over time, maintaining route cohesion, or refusing to lose operational rhythm during extended movement.
- **Primary tags:** `survival_window`, `mobility`, `stability`
- **Secondary tags:** `recovery`, `setup`, `escape`, `support`
- **Rare or limited tags:** `attack`, `control`, `pressure`
- **Typical targets:** `self`, `ally`, `route`, `environment`, `group`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-moderate Rhythm, medium Attrition; often escalates over long scenes, journeys, pursuits, retreats, or forced movement sequences.
- **Design boundary:** A March Technique should not make the character better at the basic act of traveling. It should use the physical lessons of marching to solve problems of pacing, endurance over time, route continuity, group movement, or sustained operational function.

#### Valid derived techniques

- Maintain functional pace during a long chase, retreat, forced march, evacuation, or pursuit.
- Reduce the penalty of carrying weight across a scene by distributing effort over time.
- Help an ally keep moving without turning the technique into healing.
- Preserve group cohesion during travel through exhaustion, darkness, difficult terrain, or pressure.
- Delay fatigue consequences until the group reaches a safer route point.
- Keep moving after a failed travel segment, but at increased Attrition or later cost.
- Convert steady breathing and foot cadence into resistance against panic during a prolonged escape.
- Maintain route discipline when the path becomes confusing, repetitive, exhausting, or demoralizing.
- Recover limited operational function during a march without requiring a full rest.
- Push through a long environmental crossing where stopping would be more dangerous than continuing.

#### Invalid or overlapping techniques

- Walk farther with no cost.
- Ignore all travel fatigue automatically.
- Heal wounds by marching.
- Resist poison, bleeding, pain, or internal injury.
- Ignore heat, cold, altitude, or exposure without travel pacing logic.
- Gain burst speed or explosive movement.
- Gain static defense while standing still.
- Attack harder because the character has endurance.
- Provide broad party support unrelated to route, pace, exertion, or travel continuity.
- Replace Acclimation by ignoring hostile environments in general.
- Replace Tolerance by resisting suffering already inside the body.

---

### Acclimation

- **Base specialization:** adapting to hostile climate, altitude, pressure, exposure, temperature, humidity, thin air, toxic atmosphere, or environmental stress.
- **Transferable capabilities:** exposure regulation, thermal discipline, breathing adjustment, pressure adaptation, hydration discipline, environmental pacing, bodily conservation under hostile conditions.
- **Technique identity:** Acclimation Techniques do not need to be passive resistance only. They should express the body logic of acclimation: maintaining function while the environment presses against the body, adjusting before exposure becomes collapse, regulating breath, temperature, hydration, or pressure, and making hostile surroundings less immediately disabling.
- **Primary tags:** `defense`, `mitigation`, `survival_window`
- **Secondary tags:** `recovery`, `stability`, `utility`, `setup`
- **Rare or limited tags:** `attack`, `mobility`, `control`, `support`
- **Typical targets:** `self`, `ally`, `environment`, `zone`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low Rhythm, low-to-medium Attrition; often passive or triggered by exposure thresholds, but may become costly under extreme environments.
- **Design boundary:** An Acclimation Technique should not become generic toughness. It should use the physical lessons of environmental adaptation to solve problems of climate, air, pressure, exposure, temperature, or hostile surroundings before they become internal collapse.

#### Valid derived techniques

- Delay the first harmful effect of heat, cold, altitude, pressure, or thin air.
- Reduce penalties caused by hostile weather or exposure during a scene.
- Maintain breathing function in smoke, ash, dust, humidity, altitude, or suffocating air.
- Help an ally endure an environmental threshold through pacing, covering, positioning, or exposure management.
- Stabilize body temperature before exhaustion, numbness, overheating, or shivering becomes severe.
- Cross a hostile zone by managing exposure windows instead of ignoring the hazard.
- Remain functional in corrosive mist, freezing rain, desert heat, swamp humidity, or volcanic air for a limited time.
- Use environmental knowledge to choose when to move, pause, cover, breathe, or conserve effort.
- Recover partial function after leaving an exposed zone, without treating wounds or poisons directly.
- Prevent environmental pressure from disrupting a delicate action, guard, march, or observation.

#### Invalid or overlapping techniques

- Ignore all environmental damage.
- Heal internal damage, wounds, poison, or bleeding.
- Resist pain once injury has already landed.
- March longer with no exposure logic.
- Gain generic resistance to all conditions.
- Calm fear, panic, grief, or mental stress.
- Provide offensive pressure without using environmental exposure as part of the logic.
- Adapt instantly to any impossible environment with no limit.
- Replace March by solving travel endurance.
- Replace Tolerance by resisting suffering already internalized.
- Grant immunity to heat, cold, altitude, toxins, or pressure without cost, threshold, or duration.

---

### Tolerance

- **Base specialization:** enduring pain, poison, wounds, sickness, physiological degradation, and bodily shutdown once suffering is already inside the body.
- **Transferable capabilities:** pain compartmentalization, poison endurance, wound function, delayed collapse, bodily persistence, controlled suffering, survival under internal degradation.
- **Technique identity:** Tolerance Techniques do not need to simply reduce damage. They should express the body logic of tolerance: remaining functional while compromised, delaying collapse, narrowing the effect of pain, resisting poison progression, acting through wounds, or preserving agency when the body is already failing.
- **Primary tags:** `defense`, `mitigation`, `condition_reduction`
- **Secondary tags:** `survival_window`, `stability`, `recovery`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `self`, rarely `ally`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low Rhythm, low-to-medium Attrition; high when overriding severe collapse windows, acting through serious wounds, or delaying major physiological consequences.
- **Design boundary:** A Tolerance Technique should not prevent every source of harm before it lands. It should use the physical lessons of enduring internal suffering to solve problems of pain, poison, wounds, illness, or bodily degradation already in progress.

#### Valid derived techniques

- Act once before a wound penalty fully applies.
- Reduce the immediate penalty of pain without removing the injury.
- Delay the progression of poison, infection, bleeding, sickness, or internal degradation.
- Remain conscious for a short window after reaching a collapse threshold.
- Continue holding, crawling, speaking, defending, or moving despite serious bodily distress.
- Narrow the effect of a condition to one action, limb, zone, or moment instead of letting it disable the whole body.
- Resist vomiting, trembling, dizziness, numbness, shock, or weakness long enough to complete a critical action.
- Treat pain as a cost paid in Attrition rather than immediate loss of function.
- Keep grip, posture, or breath despite injury, venom, blood loss, or exhaustion already affecting the body.
- Convert suffering into a limited survival window rather than true recovery.

#### Invalid or overlapping techniques

- Prevent environmental exposure before it affects the body.
- March longer or maintain travel pace.
- Heal wounds completely.
- Remove poison, disease, or bleeding without treatment.
- Ignore all pain or injury without cost.
- Resist fear, despair, confusion, or emotional pressure.
- Gain generic armor or damage reduction against everything.
- Protect allies broadly from their own suffering.
- Move faster because the character is tough.
- Replace Acclimation by ignoring hostile climates.
- Replace March by solving route endurance.
- Turn every wound into offensive power without a clear pain, collapse, or degradation cost.

---

## Cunning — Derived Technique Domains

Techniques are not direct upgrades to the base specialization. A technique should not simply make the character navigate better, follow tracks better, guess better, lie better, improvise better, or steal better.

Instead, each technique should express a transferable mental process developed by that specialization and apply it to a different tactical, investigative, social, positional, or narrative problem.

---

### Orientation

- **Base specialization:** navigation, route sense, direction keeping, landmark use, spatial recovery, avoiding disorientation.
- **Transferable capabilities:** mental mapping, direction anchoring, route reconstruction, landmark hierarchy, spatial correction, path continuity, disorientation recovery.
- **Technique identity:** Orientation Techniques should not simply make the character better at finding a path. They should express the mental logic of orientation: restoring direction, maintaining route sense under confusion, identifying usable reference points, preserving group position, or turning uncertain space into actionable movement logic.
- **Primary tags:** `utility`, `setup`, `survival_window`
- **Secondary tags:** `mobility`, `reposition`, `stability`, `recovery`
- **Rare or limited tags:** `attack`, `control`, `support`
- **Typical targets:** `self`, `ally`, `route`, `environment`, `group`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low Rhythm, low Attrition; shaped more by uncertainty, pressure, distance, and environmental confusion than direct hostility.
- **Design boundary:** An Orientation Technique should not become Tracking. It should not follow another creature’s trail unless the problem is about route logic rather than trace reading.

#### Valid derived techniques

- Detect that a space is designed to disorient rather than simply being complex.
- Prevent an ally from breaking formation when the route becomes confusing.
- Anchor the group’s next movement to a reliable reference point before visibility collapses.
- Identify which route choice would most likely separate the group, without revealing the correct route.
- Turn a known landmark into a temporary fallback point for retreat, regrouping, or defense.
- Notice that forced movement has changed your tactical relation to the scene, even if you do not know the full map.
- Reduce the penalty of acting after spatial confusion by reestablishing a usable reference.
- Call out a directional correction that prevents an enemy from exploiting confusion or false layout.

#### Invalid or overlapping techniques

- Follow footprints, blood, scent, broken branches, or residue left by a creature.
- Identify who passed through an area by reading traces.
- Detect invisible enemies through “direction sense.”
- Resist poison, cold, heat, or altitude.
- Lie convincingly about where the group went.
- Create a perfect map with no observation.
- Gain a flat, passive bonus to all movement checks, unconnected from spatial recovery, reference anchoring, or direction logic.
- Predict enemy strategy without spatial or route logic.
- Replace Tracking by reconstructing another creature’s path from marks.
- Replace Perception by noticing hidden details with no directional relevance.

---

### Tracking

- **Base specialization:** following trails, reading footprints, marks, disturbances, residue, broken terrain, scent signs, and movement history left by another being.
- **Transferable capabilities:** trace interpretation, path reconstruction, residue reading, disturbance comparison, movement inference, pursuit continuity, escape denial through evidence.
- **Technique identity:** Tracking Techniques should not simply make the character better at following tracks. They should express the mental logic of tracking: converting remnants into pursuit pressure, reconstructing movement from signs, predicting continuation, detecting trail breaks, or denying escape through trace awareness.
- **Primary tags:** `utility`, `pressure`, `setup`
- **Secondary tags:** `survival_window`, `reposition`, `control`, `counter_read`
- **Rare or limited tags:** `attack`, `recovery`, `support`
- **Typical targets:** `enemy`, `route`, `environment`, `object`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; often escalates over distance, degraded evidence, hostile weather, old traces, or deliberate concealment.
- **Design boundary:** A Tracking Technique should not become generic navigation or abstract deduction. It must depend on traces, disturbances, residue, or world signs left by passage.

#### Valid derived techniques

- Notice that an enemy’s escape route has a weak point because their trace pattern narrows or repeats.
- Use a fresh disturbance to pressure a fleeing creature before the trail fully degrades.
- Detect that a scene has been staged because the traces serve a story too cleanly.
- Mark the last reliable trace so the group does not waste actions on false pursuit.
- Infer which exit an enemy wanted you to ignore, without revealing their full path.
- Deny an enemy the benefit of a clean escape if they leave a trace during the same scene.
- Recognize that an object, body, or obstacle was moved to alter pursuit logic.
- Turn a partial trail into advantage on the next search, chase, or interception action.

#### Invalid or overlapping techniques

- Navigate an unknown region without traces.
- Know where to go because of “instinct.”
- Detect lies in conversation.
- Read motives without physical signs.
- Find hidden doors with no trace, disturbance, or passage evidence.
- Deal direct damage through tracking.
- Calm allies or inspire pursuit.
- Replace Orientation by solving route sense with no trail.
- Replace Intuition by sensing danger with no signs.
- Replace formal investigation by reconstructing a full event from one minor mark.

---

### Intuition

- **Base specialization:** reading dissonance, tension, incomplete signals, suspicious timing, hidden intent, and patterns before evidence becomes explicit.
- **Transferable capabilities:** pattern tension reading, anomaly detection, motive pressure, preconscious comparison, danger anticipation, incomplete-signal synthesis, conclusion restraint.
- **Technique identity:** Intuition Techniques should not simply let the character “guess correctly.” They should express the mental logic of intuition: catching tension before proof, recognizing that something is wrong, anticipating an angle, identifying unsafe conclusions, or exploiting a pattern that has not fully revealed itself.
- **Primary tags:** `utility`, `counter_read`, `setup`
- **Secondary tags:** `defense`, `survival_window`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `self`, `enemy`, `ally`, `zone`, `scene`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low Rhythm, low Attrition; often triggered by ambiguity, hidden intent, incomplete information, suspicious timing, or unseen danger.
- **Design boundary:** An Intuition Technique should not become raw sensory detection, divination, mystical instinct, or formal scholarship. It should reveal tension, risk, contradiction, or unsafe certainty, not complete truth.

#### Valid derived techniques

- Recognize that the current conclusion is unsafe, even if the evidence appears complete.
- Detect that a pattern has tension, contradiction, or missing consequence.
- Act before a threat fully reveals itself, without identifying its exact source.
- Notice that someone is waiting for your reaction rather than acting naturally.
- Identify which part of a scene deserves caution, without learning what is hidden there.
- Refuse a false certainty imposed by clean evidence, rehearsed behavior, or perfect timing.
- Gain a narrow defensive window against a feint, trap, or baited response.
- Ask the Narrator which assumption in the scene is most dangerous to trust.

#### Invalid or overlapping techniques

- See hidden creatures directly.
- Hear, smell, or notice details that require Perception.
- Know the correct answer with no ambiguity.
- Identify the exact culprit without evidence.
- Read books, rituals, or technical systems like formal scholarship.
- Resist poison, pain, fear, or exhaustion.
- Force others to believe something.
- Navigate terrain through instinct with no pattern tension.
- Follow tracks without traces.
- Become supernatural foresight unless the system explicitly allows it.

---

### Deception

- **Base specialization:** lying, omission, misdirection, framing, false narratives, controlled disclosure, and manipulation of belief.
- **Transferable capabilities:** false framing, attention steering, narrative control, omission discipline, plausible contradiction management, timing of disclosure, suspicion management.
- **Technique identity:** Deception Techniques should not simply make the character lie better. They should express the mental logic of deception: making a false version of events function long enough to alter action, trust, tempo, attention, or decision-making.
- **Primary tags:** `utility`, `control`, `setup`
- **Secondary tags:** `pressure`, `disruption`, `counter_read`
- **Rare or limited tags:** `attack`, `recovery`, `mobility`
- **Typical targets:** `enemy`, `ally`, `group`, `zone`, `scene`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; rises when the lie is layered, sustained, contested, or performed under suspicion.
- **Design boundary:** A Deception Technique should not become disguise, stealth, fear, persuasion, or identity replication. It manipulates belief through false framing, not physical concealment or emotional domination.

#### Valid derived techniques

- Make an enemy commit to defending against the wrong next action.
- Delay an enemy reaction by giving them two plausible readings of your intent.
- Turn a visible mistake into a false setup that the opponent must respect.
- Make a truthful detail look like bait, reducing how confidently others act on it.
- Force a target to spend their next read checking a false frame instead of advancing their plan.
- Protect an ally’s real action by making your own action appear to be the threat.
- Collapse suspicion onto a harmless detail before it reaches the actual weakness.
- Create a false tempo in negotiation or combat, making the next exchange harder to read.

#### Invalid or overlapping techniques

- Become physically hidden.
- Copy another person’s identity perfectly.
- Create a full disguise through words alone.
- Terrify a target into obedience.
- Inspire loyalty through charisma.
- Pick pockets or remove objects unnoticed.
- Perform fine manual manipulation.
- Navigate social hierarchy through genuine rapport.
- Control minds.
- Make a lie impossible to detect forever.
- Replace Stealth, Disguise, Theft, or Persuasion entirely.

---

### Improvisation

- **Base specialization:** producing workable solutions under pressure with poor tools, incomplete plans, unstable conditions, and available scene resources.
- **Transferable capabilities:** constraint use, rapid reframing, unstable assembly, opportunistic tool creation, risk conversion, temporary repair, scene adaptation, functional compromise.
- **Technique identity:** Improvisation Techniques should not simply let the character “do anything.” They should express the mental logic of improvisation: making something usable out of wrong conditions, creating temporary answers, exploiting available materials, accepting fragility, or turning a bad situation into a narrow opening.
- **Primary tags:** `utility`, `setup`, `disruption`
- **Secondary tags:** `survival_window`, `control`, `recovery`, `support`
- **Rare or limited tags:** `attack`, `precision`, `mobility`
- **Typical targets:** `self`, `ally`, `object`, `environment`, `zone`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** moderate Rhythm, low-to-medium Attrition; often paid through risk, fragility, resource consumption, temporary duration, or later complication.
- **Design boundary:** An Improvisation Technique should not become formal engineering, crafting, medicine, precise handwork, or universal problem-solving. It creates temporary, unstable, scene-bound answers.

#### Valid derived techniques

- Convert a failed plan into a temporary advantage instead of a complete loss.
- Turn an enemy’s environmental advantage into an unstable liability for one exchange.
- Create a one-use opening from a broken, missing, or unsuitable resource.
- Accept a future complication to solve the immediate problem now.
- Reframe a scene element so it counts as cover, leverage, distraction, signal, or obstruction for one action.
- Let an ally act without the proper tool by creating a fragile workaround with a clear risk.
- Change the function of an object already in play without making it a proper crafted item.
- Interrupt an enemy’s plan by making the current scene less predictable for one exchange.

#### Invalid or overlapping techniques

- Build a robust long-term structure.
- Craft high-quality equipment.
- Perform exact handwork that belongs to Dexterity.
- Heal wounds reliably.
- Manufacture complex devices without tools, time, or materials.
- Solve social problems by “winging it.”
- Create resources from nothing.
- Replace all other specializations in emergencies.
- Produce permanent repairs.
- Ignore consequences, fragility, or resource cost.
- Make an improvised weapon equivalent to a proper weapon without limitation.

---

### Theft

- **Base specialization:** stealing, lifting, slipping, removing, transferring, stripping access, and taking control of something under risk before response closes.
- **Transferable capabilities:** opportunity timing, attention gap use, exit planning, access denial, object transfer, risk reading, possession shift, response-window exploitation.
- **Technique identity:** Theft Techniques should not simply make the character better at stealing. They should express the mental logic of theft: identifying a window, taking control of an object or access point, removing options, transferring possession, or exiting before retaliation or detection closes.
- **Primary tags:** `utility`, `setup`, `pressure`
- **Secondary tags:** `control`, `disruption`, `escape`
- **Rare or limited tags:** `attack`, `support`, `recovery`
- **Typical targets:** `enemy`, `object`, `zone`, `self`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low Rhythm, low Attrition; exposure becomes high if the window closes, alert rises, or the target contests possession.
- **Design boundary:** A Theft Technique should not become generic Dexterity, Stealth, or Deception. It must involve acquisition, removal, transfer, access denial, or possession control under opportunity and risk.

#### Valid derived techniques

- Deny an enemy access to a prepared resource for one exchange without necessarily taking it.
- Turn a possession gap into pressure: the target must choose between acting or securing the object.
- Exploit a moment of distraction to change who controls an object’s position, not ownership.
- Create an escape window after contesting possession of a minor object.
- Force an enemy to reveal what they value by threatening access to it.
- Convert a failed grab, stumble, or crowded movement into a brief possession shift.
- Make an object temporarily unavailable by moving it just outside immediate use.
- Use the logic of theft to identify the weakest access point in a guarded object, route, or resource.

#### Invalid or overlapping techniques

- Manipulate an object precisely with no acquisition or possession shift.
- Sneak through an area without taking, removing, or transferring anything.
- Lie about ownership without changing possession or access.
- Openly overpower someone in combat and call it theft.
- Copy someone’s identity.
- Pick a lock as pure fine manipulation with no theft pressure.
- Gain broad stealth benefits.
- Deal direct damage without object removal or access denial.
- Steal impossible objects with no window, contact, route, or risk.
- Replace Dexterity, Stealth, Deception, or open Disarm mechanics entirely.

---

## Wisdom — Derived Technique Domains

Techniques are not direct upgrades to the base specialization. A technique should not simply make the character see better, survive better, heal better, gather herbs better, brew better, place traps better, mine better, forge better, sew better, set jewels better, or engineer better.

Instead, each technique should express a transferable practical judgment developed by that specialization and apply it to a different tactical, investigative, material, survival, or narrative problem.

---

### Perception

- **Base specialization:** noticing present details, exposed signals, faint motion, sensory cues, visible danger, and information available in the current scene.
- **Transferable capabilities:** exposure timing, signal prioritization, sensory discrimination, fleeting-detail retention, attention shifting, immediate threat recognition, detail anchoring.
- **Technique identity:** Perception Techniques should not simply make the character notice more. They should express the practical logic of perception: catching a present signal before it disappears, anchoring attention to an exposed detail, denying a hidden change its full advantage, or turning visible information into immediate tactical response.
- **Primary tags:** `utility`, `counter_read`, `setup`
- **Secondary tags:** `defense`, `survival_window`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `recovery`, `support`
- **Typical targets:** `self`, `enemy`, `environment`, `object`, `zone`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low Rhythm, low Attrition; usually paid through timing, exposure, line of sight, attention limits, or sensory risk.
- **Design boundary:** A Perception Technique should not become abstract deduction, historical reconstruction, tracking, intuition, or formal interpretation. It must depend on something presently observable.

#### Valid derived techniques

- Turn a visible tell into a narrow defensive window against the next action.
- Preserve one fleeting detail from a scene before smoke, darkness, movement, or distance obscures it.
- Call out a visible hazard so an ally can avoid acting as if the space were safe.
- Deny an enemy the full benefit of concealment if they expose movement, sound, silhouette, reflection, or disturbed cover.
- Identify which visible object, creature, or zone is changing right now, without explaining why.
- Lock attention onto a dangerous signal, reducing the penalty from distraction during the next exchange.
- Notice that a visible detail contradicts the immediate appearance of safety, without reconstructing the full event.
- Mark the last confirmed position of a moving threat before it leaves sight.
- Convert a momentary exposure into setup for a later attack, warning, chase, or investigation.
- Recognize that a threat is present because something in the scene is visibly reacting to it.

#### Invalid or overlapping techniques

- See hidden things with no exposed signal.
- Reconstruct what happened in the past from evidence.
- Follow footprints, scent, blood, or residue as a trail.
- Know what someone intends without a present tell.
- Detect lies through conversation alone.
- Interpret rituals, records, or symbols through scholarship.
- Resist environmental harm.
- Gain a generic bonus to all awareness.
- Automatically avoid surprise in every situation.
- Replace Intuition by sensing danger without observable detail.
- Replace Tracking by reading passage history.
- Replace Interpretation by drawing abstract conclusions from patterns.

---

### Survival

- **Base specialization:** practical field judgment, shelter choice, water logic, route safety, immediate resource use, natural hazard response, and staying functional in hostile terrain.
- **Transferable capabilities:** scarcity judgment, hazard triage, field prioritization, exposure planning, practical adaptation, resource rationing, route risk assessment, shelter logic.
- **Technique identity:** Survival Techniques should not simply make the character better at surviving wilderness. They should express the practical logic of survival: choosing what matters first, using limited natural resources, preventing exposure from becoming collapse, or making field decisions under pressure.
- **Primary tags:** `survival_window`, `utility`, `setup`
- **Secondary tags:** `recovery`, `mitigation`, `stability`
- **Rare or limited tags:** `attack`, `control`, `pressure`
- **Typical targets:** `self`, `ally`, `route`, `environment`, `zone`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-moderate Rhythm, low-to-medium Attrition; often extended over scenes of scarcity, exposure, hostile terrain, or limited resources.
- **Design boundary:** A Survival Technique should not become internal bodily resistance, medical treatment, generic navigation, or combat offense. It should use field judgment to manage external threat, scarcity, terrain, exposure, or practical risk.

#### Valid derived techniques

- Decide which environmental threat must be addressed first before the group loses function.
- Turn limited field materials into temporary shelter, cover, insulation, signal, or route safety.
- Reduce the consequence of a hostile zone by choosing when to move, wait, cover, or conserve.
- Prevent an ally from making an immediately dangerous field choice, such as drinking unsafe water or stepping into unstable ground.
- Identify the safest use of scarce resources during a scene without producing new supplies.
- Convert natural terrain into a short-term advantage against exposure, pursuit, or visibility.
- Keep a group functional through one survival interval by rationing effort, heat, water, or shelter.
- Recognize that a route is dangerous because of field conditions, not because of abstract direction.
- Create a temporary survival window before heat, cold, hunger, thirst, insects, weather, or terrain becomes severe.
- Use practical field judgment to turn a bad campsite, crossing, or rest point into a barely usable one.

#### Invalid or overlapping techniques

- Ignore heat, cold, hunger, thirst, or exposure automatically.
- Heal wounds clinically.
- Treat poison, infection, bleeding, or broken bones as Medicine.
- Navigate complex terrain with no field hazard logic.
- Track a creature by signs of passage.
- Gather or classify plants as Herbalism.
- Brew antitoxins or compounds as Alchemy.
- Gain generic combat bonuses from “knowing the wild.”
- Create unlimited food, water, shelter, or equipment.
- Replace Acclimation by adapting the body directly.
- Replace March by sustaining long-distance pace.
- Replace Medicine by treating bodily harm.

---

### Medicine

- **Base specialization:** stabilizing bodily harm, treating injury, reducing consequences, restoring immediate function, and buying time before collapse.
- **Transferable capabilities:** triage, wound prioritization, functional stabilization, collapse timing, symptom reading, pressure application, care sequencing, risk containment.
- **Technique identity:** Medicine Techniques should not simply heal more. They should express the practical logic of medical care: identifying what will fail first, stabilizing function, delaying collapse, reducing secondary harm, or buying time through trained intervention.
- **Primary tags:** `recovery`, `mitigation`, `survival_window`
- **Secondary tags:** `utility`, `condition_reduction`, `stability`
- **Rare or limited tags:** `attack`, `mobility`, `pressure`
- **Typical targets:** `self`, `ally`, rarely `enemy`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** moderate Rhythm, low-to-medium Attrition; constrained by tools, time, access to the patient, safety, and severity.
- **Design boundary:** A Medicine Technique should not become passive toughness, environmental adaptation, herbal gathering, or compound production. It must intervene on bodily harm already present or imminent through trained care.

#### Valid derived techniques

- Identify which injury, symptom, or condition will cause the next collapse if ignored.
- Stabilize one body function long enough for the target to complete a critical action.
- Delay worsening from bleeding, shock, poison progression, infection, or trauma without curing it.
- Reduce the immediate penalty of a wound by bracing, binding, compressing, splinting, or clearing obstruction.
- Convert a severe consequence into a temporary survival window that requires later treatment.
- Prevent a failed recovery attempt from becoming worse by applying triage discipline.
- Restore limited use of a limb, breath, sight, grip, or posture for one scene.
- Keep a patient conscious, breathing, or responsive long enough to move, speak, or be evacuated.
- Recognize that a visible symptom is not the real danger, redirecting treatment priority.
- Help an ally act safely despite injury by stabilizing the specific function that action requires.

#### Invalid or overlapping techniques

- Endure pain personally with no treatment.
- Ignore poison, wounds, or bleeding through toughness.
- Heal completely without time, tools, or care.
- Identify plants or ingredients.
- Brew medicine, antitoxin, or chemical compounds.
- Resist cold, heat, altitude, or exposure.
- Repair armor, tools, or equipment.
- Gain offensive pressure from anatomy alone.
- Treat emotional distress as clinical body harm unless the system explicitly supports it.
- Replace Tolerance by refusing suffering.
- Replace Herbalism by finding remedies.
- Replace Alchemy by producing compounds.

---

### Herbalism

- **Base specialization:** recognizing, gathering, preserving, classifying, and preparing useful plant matter.
- **Transferable capabilities:** plant-resource judgment, specimen quality reading, preservation timing, seasonal awareness, toxicity recognition, preparation restraint, natural material use.
- **Technique identity:** Herbalism Techniques should not simply make the character find better plants. They should express the practical logic of plant-resource mastery: knowing when plant matter is useful, dangerous, spoiled, misread, underprepared, or fit for immediate practical use.
- **Primary tags:** `utility`, `setup`, `recovery`
- **Secondary tags:** `mitigation`, `survival_window`, `support`
- **Rare or limited tags:** `attack`, `control`, `precision`
- **Typical targets:** `self`, `ally`, `object`, `environment`, `ingredient`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low Rhythm, low Attrition; shaped by access, season, freshness, specimen quality, preparation limits, and storage.
- **Design boundary:** A Herbalism Technique should not become clinical treatment, complex reagent transformation, or pure sensory detection. It should use plant knowledge to create practical, limited effects through natural material.

#### Valid derived techniques

- Recognize that a plant-based resource is unsafe, spoiled, misidentified, or contaminated before use.
- Preserve a gathered specimen long enough to remain useful for later Medicine, Alchemy, or Survival.
- Prepare simple plant matter for immediate field use without turning it into a full compound.
- Use plant material as insulation, scent cover, irritant, binding, poultice base, signal, dye, or temporary filter.
- Identify which available plant resource is least risky for a specific immediate purpose.
- Prevent an ally from using a harmful natural substitute by recognizing its plant logic.
- Convert gathered flora into a temporary mitigation aid, not a full medical cure.
- Use knowledge of local vegetation to infer immediate environmental risk, such as water quality, poison presence, soil change, or animal pressure.
- Stabilize the value of an ingredient before it spoils, wilts, ferments, dries, or loses potency.
- Use plant traits to support another specialization’s action without replacing it.

#### Invalid or overlapping techniques

- Heal wounds directly as Medicine.
- Brew antitoxins, elixirs, poisons, or reactive compounds as Alchemy.
- Identify any hidden object through smell or sight alone.
- Gather perfect ingredients anywhere.
- Create complex reagents instantly.
- Perform surgery or clinical stabilization.
- Replace Survival by solving all field scarcity.
- Replace Perception by noticing all natural details.
- Create broad combat control without plant material, preparation, or delivery.
- Turn every plant into a reliable cure or weapon.

---

### Alchemy

- **Base specialization:** transforming ingredients into functional compounds through process, preparation, controlled reaction, dosage, and failure management.
- **Transferable capabilities:** reaction control, dosage logic, ingredient transformation, preparation sequencing, volatility management, contamination control, delivery design, compound stability.
- **Technique identity:** Alchemy Techniques should not simply produce better potions. They should express the practical logic of controlled transformation: changing material behavior, preparing reactive responses, managing dosage, reducing contamination, or creating temporary compound-based effects.
- **Primary tags:** `utility`, `setup`, `condition_reduction`
- **Secondary tags:** `recovery`, `attack`, `mitigation`
- **Rare or limited tags:** `mobility`, `pressure`, `support`
- **Typical targets:** `self`, `ally`, `enemy`, `object`, `ingredient`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** moderate Rhythm, low-to-medium Attrition; paid through ingredient value, preparation time, instability, failure risk, dosage limits, or storage constraints.
- **Design boundary:** An Alchemy Technique should not become raw ingredient gathering, direct medical procedure, structural engineering, or herbal identification. It must involve prepared substances, transformation, reaction, dosage, or compound delivery.

#### Valid derived techniques

- Stabilize an unstable compound long enough for one safe use.
- Convert a prepared reagent into a different delivery form with reduced strength or added risk.
- Reduce the immediate effect of a toxin, acid, irritant, sedative, or contaminant through counter-reaction.
- Prepare a reactive substance that triggers under a specific contact, heat, air, moisture, or timing condition.
- Alter an object’s surface briefly through oil, resin, acid, powder, adhesive, smoke, pigment, or solvent.
- Create a controlled failure that weakens a compound instead of causing full backlash.
- Use dosage knowledge to make a limited supply affect one extra target at reduced potency.
- Identify that a compound was tampered with because its reaction profile is wrong.
- Turn an ingredient flaw into a predictable side effect instead of unusable waste.
- Prepare a compound-based response for a known condition without treating the body directly.

#### Invalid or overlapping techniques

- Find herbs or raw ingredients in the wild.
- Perform clinical healing or surgery.
- Treat wounds through hands-on Medicine without compound logic.
- Build machines, structures, or mechanisms.
- Create permanent magical substances if the system does not allow them.
- Produce infinite compounds without ingredients.
- Ignore dosage, delivery, preparation, or instability.
- Replace Herbalism by classifying plants.
- Replace Traps by making every vial a complex mechanism.
- Replace Smithing or Engineering by altering structural metal or devices through “chemistry” alone.

---

### Traps

- **Base specialization:** setting, arming, disarming, redirecting, reading, and weaponizing conditional mechanisms, triggers, passages, and interaction points.
- **Transferable capabilities:** trigger logic, delayed consequence design, conditional response, passage control, bait reading, pressure placement, mechanical suspicion, response timing.
- **Technique identity:** Traps Techniques should not simply make the character place better traps. They should express the practical logic of conditional danger: recognizing trigger relationships, forcing caution, redirecting response, weaponizing passage, or turning interaction into risk.
- **Primary tags:** `control`, `setup`, `pressure`
- **Secondary tags:** `disruption`, `utility`, `counter_positioning`
- **Rare or limited tags:** `recovery`, `support`, `mobility`
- **Typical targets:** `enemy`, `route`, `zone`, `object`, `environment`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** moderate Rhythm, low-to-medium Attrition; paid through preparation, material, placement, visibility, trigger limits, and scene constraints.
- **Design boundary:** A Traps Technique should not become broad engineering, generic precision work, or open melee pressure. It must involve conditional response, trigger logic, passage control, or delayed consequence.

#### Valid derived techniques

- Identify which interaction point in a scene is most likely to be used as a trigger.
- Turn an enemy’s chosen route into a risky route by placing or threatening a conditional response.
- Redirect an existing trigger toward a safer or less damaging result.
- Disarm only the immediate trigger without understanding the entire mechanism.
- Mark a zone as dangerous enough that enemies must spend tempo to test, avoid, or clear it.
- Convert a door, rope, latch, stone, container, floor section, or object into a conditional hazard.
- Notice that a trap is meant to control movement rather than cause injury.
- Use a false trigger to make an enemy hesitate, reroute, or waste an interaction.
- Create a temporary lock, snare, alarm, obstruction, or warning through conditional placement.
- Preserve a trap’s function while changing who it responds to, if the mechanism allows it.

#### Invalid or overlapping techniques

- Build a complex machine as Engineering.
- Pick a lock through fine manipulation alone.
- Deal direct melee damage without trigger or conditional logic.
- Create permanent fortifications.
- Heal or stabilize injuries.
- Make any space dangerous without material, trigger, or preparation.
- Replace Perception by detecting all hidden dangers automatically.
- Replace Improvisation by making every object a perfect trap instantly.
- Replace Engineering by solving system-level mechanics.
- Control enemies broadly with no passage, trigger, or interaction point.

---

### Mining

- **Base specialization:** reading stone, soil, seams, tunnels, extraction points, collapse risk, tool pressure, and material recovery from the earth.
- **Transferable capabilities:** subsurface judgment, load reading, fracture awareness, extraction discipline, collapse prediction, material preservation, tunnel stability, pressure direction.
- **Technique identity:** Mining Techniques should not simply make the character mine faster. They should express the practical logic of mining: reading hidden pressure in earth or stone, extracting without destroying value, preserving access, or preventing collapse.
- **Primary tags:** `utility`, `setup`, `stability`
- **Secondary tags:** `survival_window`, `recovery`, `control`
- **Rare or limited tags:** `attack`, `mobility`, `pressure`
- **Typical targets:** `environment`, `object`, `route`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** moderate Rhythm, medium Attrition; shaped by tool load, material hardness, collapse risk, extraction duration, dust, depth, and tunnel conditions.
- **Design boundary:** A Mining Technique should not become forging, general engineering, broad exploration, or bodily resistance. It must involve earth, stone, mineral, tunnel, seam, extraction, fracture, or subsurface stability logic.

#### Valid derived techniques

- Identify which part of a stone, wall, tunnel, or floor is most likely to fail under pressure.
- Preserve a usable route through unstable stone long enough to pass or retreat.
- Extract a fragile material, embedded object, or mineral sample without ruining it.
- Redirect effort toward a weak seam instead of wasting time on hard stone.
- Detect that a tunnel, cave, ruin, or mine is unstable because of load, fracture, dust, sound, or pressure.
- Create a temporary brace, wedge, or warning point based on collapse logic.
- Open a small passage, handhold, or access point without causing full structural failure.
- Use knowledge of stone fracture to make a controlled break in an object or surface.
- Recognize whether a blockage is natural, collapsed, cut, excavated, or intentionally placed.
- Delay a collapse consequence by reducing stress on a specific support or seam.

#### Invalid or overlapping techniques

- Forge, reshape, or repair metal.
- Build broad structural systems as Engineering.
- Navigate caves with no stone, seam, or route-stability logic.
- Resist dust, suffocation, exhaustion, or injury as bodily endurance.
- Extract material instantly with no tools or effort.
- Detect hidden creatures with no subsurface sign.
- Create direct combat damage unrelated to fracture, stone, or material pressure.
- Replace Survival by handling every underground hazard.
- Replace Perception by noticing all environmental details.
- Replace Smithing by understanding metal as worked material.

---

### Smithing

- **Base specialization:** shaping, repairing, reinforcing, tempering, and reading functional metal through heat, force, timing, and material judgment.
- **Transferable capabilities:** stress reading, heat discipline, reinforcement logic, edge maintenance, impact distribution, material fatigue recognition, functional repair, metal failure control.
- **Technique identity:** Smithing Techniques should not simply make the character forge better items. They should express the practical logic of metalwork: preserving function under stress, reading metal failure, reinforcing a weak point, restoring usability, or exploiting material fatigue.
- **Primary tags:** `utility`, `recovery`, `setup`
- **Secondary tags:** `mitigation`, `attack`, `stability`
- **Rare or limited tags:** `mobility`, `pressure`, `counter_read`
- **Typical targets:** `object`
- **Typical types:** `active`
- **Usual cost profile:** moderate Rhythm, medium Attrition; paid through labor load, heat access, tool access, material stakes, time, and risk of weakening the object.
- **Design boundary:** A Smithing Technique should not become fine jewelry, broad engineering, terrain survival, or deception. It must involve worked metal, functional repair, stress, reinforcement, heat, edge, or material fatigue.

#### Valid derived techniques

- Identify the weakest functional point in a metal weapon, tool, hinge, chain, plate, shield, or mechanism.
- Reinforce a metal object just long enough to survive one scene or exchange.
- Restore limited function to a damaged metal object without fully repairing it.
- Reduce the consequence of a metal object breaking by controlling where the failure occurs.
- Prepare an edge, point, hook, ring, clasp, or plate for a specific immediate use.
- Exploit visible metal fatigue to disable an object with the least necessary force.
- Prevent armor, weapon, or tool degradation from worsening during one scene.
- Adjust weight, balance, or fit of a metal object enough to remove a penalty, not improve quality.
- Use heat, pressure, or impact knowledge to judge whether a metal object is safe to use.
- Convert scrap metal into a temporary reinforcement, wedge, brace, spike, or repair piece.

#### Invalid or overlapping techniques

- Forge high-quality weapons instantly.
- Create permanent superior gear without time and forge conditions.
- Set gems or preserve delicate luxury value.
- Repair cloth, leather, straps, or flexible material.
- Design complex machines or structures as Engineering.
- Mine ore or identify seams underground.
- Gain direct combat power with no metal object involved.
- Treat wounds using metalwork logic.
- Replace Jewelry with fine-scale precision.
- Replace Engineering by solving system-level mechanical function.

---

### Tailoring

- **Base specialization:** repairing, fitting, adjusting, reinforcing, and configuring flexible material, fabric, straps, seams, padding, and worn gear.
- **Transferable capabilities:** fit correction, tension distribution, seam logic, flexible reinforcement, garment function, strap routing, movement allowance, material preservation.
- **Technique identity:** Tailoring Techniques should not simply make the character sew better. They should express the practical logic of flexible material: preserving fit, preventing tearing, distributing strain, keeping gear usable, or configuring worn equipment under pressure.
- **Primary tags:** `utility`, `recovery`, `mitigation`
- **Secondary tags:** `setup`, `support`, `stability`
- **Rare or limited tags:** `attack`, `pressure`, `control`
- **Typical targets:** `object`, `ally`, `self`
- **Typical types:** `active`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; shaped by material quality, time, access, tension, wear, and precision of adjustment.
- **Design boundary:** A Tailoring Technique should not become jewelry-scale finesse, metalwork, direct damage, or pursuit logic. It must involve flexible material, fit, seams, straps, padding, clothing, soft armor, or carried gear.

#### Valid derived techniques

- Adjust a strap, harness, cloak, pack, sleeve, glove, boot, or armor layer so it no longer interferes with one action.
- Reinforce a seam, binding, sling, pouch, or strap before it fails under strain.
- Restore limited function to torn clothing, soft armor, ropework, cloth cover, or carrying gear.
- Convert fabric into temporary cover, sling, bandage support, signal, restraint, padding, or insulation.
- Reduce the penalty from ill-fitting gear during one scene.
- Distribute load across clothing or harness points to prevent immediate fatigue or tearing.
- Prevent an object from being dropped, exposed, tangled, or snagged through better fastening.
- Prepare flexible material to resist weather, friction, heat, cold, or abrasion briefly.
- Make an ally’s gear usable after damage without fully repairing it.
- Use fabric tension to create a temporary brace, screen, bundle, wrap, or anchor point.

#### Invalid or overlapping techniques

- Repair metal armor, weapons, chains, hinges, or tools.
- Set gems or manipulate tiny luxury pieces.
- Heal wounds clinically.
- Create perfect disguises through clothing alone.
- Pick pockets or steal objects.
- Build structural mechanisms.
- Deal direct damage without cloth, strap, tension, or flexible material logic.
- Replace Medicine by treating injuries.
- Replace Smithing by repairing armor plates.
- Replace Jewelry by doing fine precious work.

---

### Jewelry

- **Base specialization:** preserving, setting, separating, valuing, repairing, concealing, and manipulating small delicate crafted pieces without ruining value or function.
- **Transferable capabilities:** fine-scale judgment, value preservation, delicate separation, micro-setting, hidden compartment logic, precious-material handling, damage avoidance, small-object integrity.
- **Technique identity:** Jewelry Techniques should not simply make the character craft better jewelry. They should express the practical logic of fine valuable work: preserving value, manipulating tiny components, separating delicate pieces, concealing detail, or preventing small high-stakes damage.
- **Primary tags:** `utility`, `precision`, `setup`
- **Secondary tags:** `recovery`, `support`, `control`
- **Rare or limited tags:** `attack`, `mobility`, `survival_window`
- **Typical targets:** `object`
- **Typical types:** `active`
- **Usual cost profile:** low Rhythm, low Attrition; high consequence on mistakes because of scale, fragility, value, and fine tolerances.
- **Design boundary:** A Jewelry Technique should not become heavy forging, field survival, large-scale repair, or open combat pressure. It must involve small, delicate, valuable, concealed, or fine-scale crafted objects.

#### Valid derived techniques

- Remove, secure, or separate a tiny valuable component without damaging the larger object.
- Detect that a small object was altered because its setting, symmetry, weight, or finish is wrong.
- Preserve the value of a delicate object during transport, impact, theft, inspection, or concealment.
- Conceal a tiny mark, message, powder, needle, key, charm, or mechanism inside a decorative piece.
- Restore limited function to a clasp, setting, pin, chain, ring, seal, lens frame, or fine fitting.
- Identify the safest point to apply pressure on a fragile object without breaking it.
- Prevent a small valuable object from becoming unusable after damage.
- Use fine-scale craft logic to reveal tampering, forgery, substitution, or hidden compartments.
- Convert a decorative piece into a temporary anchor, signal, seal, marker, or access token.
- Split one high-value component into usable parts while minimizing loss.

#### Invalid or overlapping techniques

- Forge weapons, armor, or heavy metal tools.
- Repair large mechanisms or structures.
- Sew flexible gear or clothing.
- Survive hostile terrain through craft knowledge.
- Deal direct combat damage with no fine object involved.
- Build traps or machines at full scale.
- Pick pockets or steal items through opportunity.
- Create wealth from nothing.
- Replace Dexterity by handling all fine manipulation.
- Replace Smithing by treating all metalwork as jewelry.

---

### Engineering

- **Base specialization:** understanding, stabilizing, altering, bypassing, repairing, or disrupting complex physical systems under load, access limits, and failure pressure.
- **Transferable capabilities:** system modeling, load-path reading, cascade prediction, mechanism bypass, structural diagnosis, function redirection, failure containment, component relationship mapping.
- **Technique identity:** Engineering Techniques should not simply make the character build better machines. They should express the practical logic of systems: identifying how parts affect the whole, stabilizing or redirecting function, preventing cascade failure, or altering a mechanism without treating it as a single object.
- **Primary tags:** `utility`, `control`, `setup`
- **Secondary tags:** `mitigation`, `disruption`, `recovery`
- **Rare or limited tags:** `attack`, `pressure`, `stealth`
- **Typical targets:** `object`, `device`, `structure`, `route`, `environment`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** moderate Rhythm, medium Attrition; paid through complexity, tool demands, partial information, access restrictions, time pressure, and cascade-failure risk.
- **Design boundary:** An Engineering Technique should not become improvisation, trap logic alone, fine manual pickwork, single-material craft, or broad leadership. It must involve system-level function, structure, load, mechanism, or component interaction.

#### Valid derived techniques

- Identify which component of a system controls the next failure.
- Stabilize a damaged mechanism or structure long enough for one scene.
- Redirect a machine, gate, bridge, lift, pulley, engine, lock system, or pressure system into a safer state.
- Disable a device by interrupting the relationship between parts rather than destroying it.
- Prevent a cascade failure by isolating one component.
- Bypass a mechanism at the system level without picking, forcing, or fully repairing it.
- Recognize that a structure is unsafe because its load path has changed.
- Convert a complex object’s function into a simpler temporary function.
- Use system logic to predict what will happen if a lever, support, valve, gear, rope, counterweight, or pressure point is altered.
- Create a temporary stabilizing brace, redirect, vent, bypass, or fail-safe with limited duration.

#### Invalid or overlapping techniques

- Improvise a fragile fix with random materials as the main identity.
- Pick locks through fine handwork alone.
- Build full machines instantly.
- Place simple conditional hazards as Traps.
- Repair metal, cloth, or jewelry when only single-material craft is involved.
- Gather plants, minerals, or ingredients.
- Heal bodily harm.
- Lead a group through charisma or command.
- Make any structure safe with no tools, time, access, or system understanding.
- Replace Mining by reading stone alone.
- Replace Smithing, Tailoring, or Jewelry by handling all repairs.
- Replace Traps by treating every trigger as full engineering.

---

## Intellect — Derived Technique Domains

Techniques are not direct upgrades to the base specialization. A technique should not simply make the character identify better, interpret better, translate better, analyze thaumaturgy better, remember history better, understand geography better, read the sky better, know doctrine better, break codes better, read ruins better, understand buildings better, or study war better.

Instead, each technique should express a transferable formal process developed by that specialization and apply it to a different tactical, investigative, social, positional, or narrative problem.

---

### Identification

- **Base specialization:** precise classification, naming what something is, recognizing category, type, family, class, material, creature, phenomenon, or applicable framework.
- **Transferable capabilities:** category discipline, false-assumption prevention, framework selection, type comparison, exclusion logic, sample-quality judgment, error containment.
- **Technique identity:** Identification Techniques should not simply reveal what something is. They should express the formal logic of classification: preventing category error, choosing the right response framework, excluding wrong assumptions, or identifying which kind of knowledge applies next.
- **Primary tags:** `utility`, `counter_read`, `setup`
- **Secondary tags:** `survival_window`, `disruption`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `object`, `enemy`, `creature`, `phenomenon`, `zone`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low Rhythm, low Attrition; usually paid through sample quality, observation time, access, and uncertainty.
- **Design boundary:** An Identification Technique should not become sensory detection, symbolic interpretation, historical analysis, or full explanation. It tells you what category you are dealing with, not the full truth behind it.

#### Valid derived techniques

- Prevent a failed action caused by treating the target as the wrong category.
- Identify which response framework applies: creature, mechanism, substance, ritual, structure, tool, disease, or phenomenon.
- Exclude one dangerous false assumption before the group commits to an action.
- Recognize that two similar-looking targets belong to different functional categories.
- Determine whether a known technique, tool, reagent, or procedure is applicable to this target type.
- Mark a target as “not what it appears to be” without revealing its full nature.
- Reduce risk on the next action by identifying what kind of thing must be tested first.
- Recognize that an object or phenomenon has been misclassified by someone else.
- Prevent waste of a resource that would not work on this category of target.
- Reveal that the current problem requires another specialization before further progress is possible.

#### Invalid or overlapping techniques

- Notice hidden details with no available sample or exposure.
- Interpret symbolic meaning, motive, or implication.
- Reconstruct the history of an object.
- Translate text or speech.
- Heal, repair, disable, or counter something directly.
- Know the full weakness of a creature from classification alone.
- Identify every property of an unknown phenomenon instantly.
- Replace Perception by detecting what is not observable.
- Replace Interpretation by explaining what the classification means.
- Replace Thaumaturgy, Medicine, Alchemy, or Engineering by solving the whole domain after naming the type.

---

### Interpretation

- **Base specialization:** extracting implication, structure, meaning, or consequence from information that is already present but not yet understood.
- **Transferable capabilities:** implication reading, structural inference, conclusion testing, pattern meaning, unsafe assumption detection, context assembly, ambiguity management.
- **Technique identity:** Interpretation Techniques should not simply explain information. They should express the formal logic of meaning-making: turning present evidence into limited implication, identifying what a pattern points toward, or showing which conclusion is unsafe.
- **Primary tags:** `utility`, `pattern_exploitation`, `setup`
- **Secondary tags:** `counter_read`, `disruption`, `survival_window`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `zone`, `object`, `text`, `enemy`, `structure`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; constrained by ambiguity, available evidence, analysis time, and context.
- **Design boundary:** An Interpretation Technique should not classify, detect, translate, or intuit. It works only after information is present and asks what that information implies.

#### Valid derived techniques

- Reveal which conclusion the visible evidence does not support.
- Identify the practical implication of a pattern without reconstructing the entire event.
- Turn a partial sign, layout, record, or sequence into one actionable question.
- Detect that a scene is arranged to imply the wrong conclusion.
- Identify which element of a pattern carries the most meaning for the next action.
- Reveal what kind of consequence should exist if the apparent story were true.
- Prevent the group from acting on a misleading interpretation of visible evidence.
- Convert a confusing symbol, formation, scene, or layout into a limited tactical warning.
- Identify whether a message is descriptive, instructional, ceremonial, threatening, or prohibitive.
- Ask the Narrator what immediate inference would be unsafe.

#### Invalid or overlapping techniques

- Classify what an unknown object is.
- Notice hidden evidence that was not already present.
- Translate unknown language.
- Read intent without evidence.
- Follow physical traces as Tracking.
- Break deliberate codes as Cryptology.
- Recall precedent as History.
- Treat bodily harm, repair objects, or resist conditions.
- Produce the full correct answer from one clue.
- Replace Intuition by sensing tension before evidence exists.

---

### Linguistics

- **Base specialization:** understanding language systems, grammar, register, syntax, semantic structure, translation, inscription, speech, and communicative form.
- **Transferable capabilities:** grammatical parsing, register recognition, semantic constraint reading, translation discipline, ambiguity management, dialect comparison, message-form awareness.
- **Technique identity:** Linguistics Techniques should not simply translate better. They should express the formal logic of language: detecting ambiguity, register mismatch, hidden constraint, mistranslation risk, or how wording shapes action.
- **Primary tags:** `utility`, `setup`, `counter_read`
- **Secondary tags:** `disruption`, `support`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `mobility`, `mitigation`
- **Typical targets:** `text`, `creature`, `message`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low Rhythm, low Attrition; shaped by exposure length, language distance, dialect, inscription quality, and context.
- **Design boundary:** A Linguistics Technique should not become persuasion, deception, cryptology, theology, or battlefield command. It opens or manipulates language as language.

#### Valid derived techniques

- Detect that a translation is unsafe because one word carries multiple possible functions.
- Identify whether a phrase is command, warning, oath, title, insult, prayer, instruction, or record.
- Reveal that a speaker is using the wrong register for their claimed role.
- Prevent a social mistake caused by literal translation of an idiom, title, taboo, or honorific.
- Identify which part of a message has been mistranslated, omitted, or softened.
- Convert partial language knowledge into one safe action, not full fluency.
- Detect that two inscriptions were written by different linguistic traditions.
- Use grammatical structure to determine what object, person, or action a sentence refers to.
- Reduce ambiguity in a command or warning before the group acts on it.
- Recognize that a message is meant to be read aloud, memorized, performed, sealed, or obeyed.

#### Invalid or overlapping techniques

- Break a cipher intentionally designed to hide meaning.
- Persuade, intimidate, or negotiate through rhetoric alone.
- Deceive someone socially.
- Understand doctrine just because the text is religious.
- Interpret symbolic meaning beyond language structure.
- Detect lies without linguistic evidence.
- Command allies in battle as leadership.
- Translate every unknown language instantly.
- Replace Cryptology by opening encoded messages.
- Replace Theology, Interpretation, or Deception entirely.

---

### Thaumaturgy

- **Base specialization:** formal understanding of thaumic systems, laws, distortions, manifestations, contamination, resonance behavior, and controlled interaction.
- **Transferable capabilities:** formal anomaly reading, instability mapping, distortion containment, manifestation timing, contact safety, pattern suppression, reaction prediction.
- **Technique identity:** Thaumaturgy Techniques should not simply identify magic better. They should express formal contact-through-understanding: choosing safe interaction, limiting volatility, redirecting behavior, or recognizing which law of the phenomenon is being violated.
- **Primary tags:** `utility`, `mitigation`, `condition_reduction`
- **Secondary tags:** `counter_read`, `setup`, `disruption`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `phenomenon`, `object`, `zone`, `structure`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** moderate Rhythm, low-to-medium Attrition; raised by instability, contamination, volatility, exposure, or poor understanding.
- **Design boundary:** A Thaumaturgy Technique should not become faith, emotional resonance, instinctive aura response, or mundane navigation. It must involve formal thaumic logic.

#### Valid derived techniques

- Identify which part of a thaumic phenomenon is unstable enough to avoid first.
- Reduce the consequence of contact by choosing the safest interaction point.
- Delay a manifestation by interrupting the formal condition it requires.
- Recognize that a distortion is repeating a rule rather than acting randomly.
- Redirect a minor thaumic reaction into a less harmful expression.
- Detect that an object or zone has been contaminated by a mismatched thaumic pattern.
- Prevent a technique from escalating because you recognize the failure condition early.
- Convert a volatile phenomenon into a limited warning, barrier, signal, or hazard.
- Identify which action would worsen the thaumic behavior without explaining the whole system.
- Suppress a minor effect briefly by denying it the condition it needs to continue.

#### Invalid or overlapping techniques

- Commune with an entity through faith.
- Sense aura by instinct.
- Interpret sacred doctrine.
- Navigate terrain with magical knowledge.
- Produce free supernatural effects without phenomenon, rule, or contact.
- Heal, repair, or resist harm without thaumic logic.
- Replace Theology by explaining rituals as faith systems.
- Replace Identification by naming every phenomenon completely.
- Replace Alchemy or Engineering with generic “energy manipulation.”
- Become magic casting unless the system explicitly allows it.

---

### History

- **Base specialization:** organized precedent, records, cycles, prior crises, peoples, institutions, wars, methods, failures, and continuity with the past.
- **Transferable capabilities:** precedent application, cycle recognition, institutional memory, continuity reading, inherited-pattern detection, prior-method comparison, historical risk framing.
- **Technique identity:** History Techniques should not simply recall lore. They should express the formal logic of precedent: using what happened before to frame what is likely repeating, what method already failed, or what inherited pattern shapes the present.
- **Primary tags:** `utility`, `setup`, `pattern_exploitation`
- **Secondary tags:** `counter_read`, `support`, `disruption`
- **Rare or limited tags:** `attack`, `mobility`, `recovery`
- **Typical targets:** `zone`, `group`, `object`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low Rhythm, low Attrition; dependent on contextual fit, records, cultural continuity, and relevance.
- **Design boundary:** A History Technique should not become archaeology, live tracking, social command, or physical repair. It uses precedent, not direct observation alone.

#### Valid derived techniques

- Identify that a present crisis resembles a known historical pattern.
- Reveal one method that historically failed in a similar situation.
- Recognize that a group is repeating an inherited institutional behavior.
- Use precedent to warn which decision will likely escalate conflict.
- Identify what kind of authority, law, taboo, or memory may still shape current behavior.
- Reveal that an object, symbol, or practice belongs to a known historical continuity.
- Prevent the group from treating a recurring crisis as unprecedented.
- Identify which past solution might apply imperfectly, with stated risk.
- Expose that a claim about tradition contradicts known precedent.
- Use a historical parallel to create setup for negotiation, investigation, or strategic planning.

#### Invalid or overlapping techniques

- Excavate or read material remains as Archaeology.
- Track a live target.
- Command allies through authority.
- Repair objects or structures.
- Predict the future perfectly.
- Know private events with no record or continuity.
- Replace Theology by explaining doctrine internally.
- Replace Belicology by reading live deployment.
- Replace Interpretation by analyzing a present pattern with no historical frame.
- Solve current social problems just by citing history.

---

### Geography

- **Base specialization:** organized knowledge of regions, terrain systems, large-scale spatial relations, chokepoints, climate zones, borders, resources, and territorial logic.
- **Transferable capabilities:** macro-spatial modeling, terrain-system awareness, regional constraint reading, chokepoint recognition, route implication, territorial patterning, logistical geography.
- **Technique identity:** Geography Techniques should not simply navigate better. They should express macro-spatial knowledge: using regional structure, terrain systems, territorial relation, or large-scale layout to shape present decisions.
- **Primary tags:** `utility`, `setup`, `survival_window`
- **Secondary tags:** `mobility`, `support`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `recovery`, `control`
- **Typical targets:** `route`, `environment`, `group`, `zone`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low Rhythm, low Attrition; paid through incomplete references, outdated maps, scale, and precision demands.
- **Design boundary:** A Geography Technique should not become immediate route finding, tracking, field survival, mining, or deception. It works through large-scale spatial knowledge.

#### Valid derived techniques

- Identify which broad terrain feature most likely controls movement in this region.
- Predict where chokepoints, settlements, water sources, passes, or borders are likely to exist.
- Recognize that a route is strategically bad because of regional layout, not immediate danger.
- Use macro-terrain knowledge to choose between pursuit, retreat, concealment, or detour.
- Reveal which nearby zone is likely connected to another by geography, not by visible path.
- Identify where an enemy group would need supplies, crossings, or staging points.
- Prevent the party from choosing a route that violates known regional constraints.
- Recognize that a map, testimony, or route description is geographically inconsistent.
- Use territorial logic to predict where conflict, patrols, tolls, or claims may concentrate.
- Convert regional knowledge into a limited advantage before a travel, search, or strategy scene.

#### Invalid or overlapping techniques

- Find the exact path in real time with no map or reference.
- Follow tracks or signs of passage.
- Survive exposure, hunger, or field hazards.
- Read underground seams or mineral deposits.
- Identify plants, animals, or weather by field signs alone.
- Deceive someone about a route.
- Replace Orientation by solving immediate disorientation.
- Replace Survival by making practical field decisions.
- Replace Mining by reading subsurface material.
- Replace Belicology by reading doctrine or deployment.

---

### Astronomy

- **Base specialization:** celestial order, stars, moons, cycles, timing, calendars, sky-based orientation, large-scale celestial inference.
- **Transferable capabilities:** cycle reading, timing-window calculation, celestial correlation, night-order anchoring, long-pattern inference, calendar logic, precision observation.
- **Technique identity:** Astronomy Techniques should not simply read the sky better. They should express the formal logic of celestial order: using cycles, timing, visibility, alignment, or celestial regularity to create limited action.
- **Primary tags:** `utility`, `setup`, `pattern_exploitation`
- **Secondary tags:** `survival_window`, `counter_read`, `support`
- **Rare or limited tags:** `attack`, `mobility`, `control`
- **Typical targets:** `environment`, `phenomenon`, `route`, `zone`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low Rhythm, low Attrition; constrained by visibility, timing, precision, calendar knowledge, and observation quality.
- **Design boundary:** An Astronomy Technique should not become theology, instinctive sky-reading, direct combat pressure, or raw navigation without celestial logic.

#### Valid derived techniques

- Establish a reliable time window when normal timekeeping is uncertain.
- Detect that a testimony, ritual, route, or record has impossible timing.
- Use celestial cycles to predict when visibility, tide, temperature, shadow, or exposure will change.
- Anchor the group’s timing during night travel, watch rotations, rituals, or long waits.
- Identify that a phenomenon is tied to a cycle rather than a random event.
- Choose the safest moment to move based on light, shadow, moon, tide, or celestial position.
- Reveal whether a map, inscription, or plan assumes a different season, latitude, or celestial order.
- Create setup for navigation, ritual analysis, agriculture, travel, or observation through timing.
- Prevent the group from acting during a known bad celestial window.
- Use the sky to verify whether the environment itself is behaving incorrectly.

#### Invalid or overlapping techniques

- Interpret divine will from the stars.
- Navigate any route instantly.
- Resist cold, heat, hunger, or fatigue.
- Deal direct combat damage.
- Translate celestial inscriptions as Linguistics.
- Explain religious calendars as Theology unless doctrine is involved.
- Read hidden motives through astrology unless the system explicitly allows it.
- Replace Orientation by solving immediate spatial confusion.
- Replace Geography by knowing regional terrain.
- Replace Thaumaturgy by explaining supernatural sky phenomena without formal thaumic logic.

---

### Theology

- **Base specialization:** religious systems, doctrines, rites, sacred authority, ritual structure, symbols, taboos, mythic logic, and institutional faith.
- **Transferable capabilities:** doctrinal literacy, ritual implication reading, sacred hierarchy awareness, taboo recognition, symbolic consistency, authority mapping, heresy detection.
- **Technique identity:** Theology Techniques should not simply know religion better. They should express doctrinal literacy as leverage: identifying what a rite demands, what authority structure implies, what taboo is active, or what symbolic inconsistency matters.
- **Primary tags:** `utility`, `counter_read`, `setup`
- **Secondary tags:** `support`, `disruption`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `mobility`, `mitigation`
- **Typical targets:** `ritual`, `symbol`, `group`, `zone`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low Rhythm, low Attrition; shaped by obscurity, syncretism, doctrinal depth, sectarian variation, and ritual access.
- **Design boundary:** A Theology Technique should not become thaumic science, aura response, social command, or practical crafting. It works through doctrine, rite, symbol, and sacred authority.

#### Valid derived techniques

- Identify which part of a ritual is doctrinally necessary and which part is decorative.
- Recognize that a sacred symbol is being used outside its proper authority.
- Predict how a religious group will respond to oath-breaking, impurity, taboo, hierarchy, or trespass.
- Reveal that a rite is incomplete, inverted, syncretic, heretical, or politically staged.
- Prevent the group from violating a sacred rule that would escalate the scene.
- Identify which figure in a religious space likely holds authority, without commanding them.
- Use doctrinal knowledge to choose a respectful, disruptive, or neutral action.
- Detect that a religious explanation is masking a non-religious motive.
- Convert sacred etiquette into setup for negotiation, entry, delay, or investigation.
- Identify what a religious object permits, forbids, protects, or legitimizes.

#### Invalid or overlapping techniques

- Analyze thaumic energy as a formal system.
- Commune with gods or spirits automatically.
- Command believers through faith.
- Inspire allies through charisma.
- Perform magic because doctrine is known.
- Translate sacred language without Linguistics.
- Break codes in sacred texts without Cryptology.
- Repair ritual objects through craft.
- Replace History by recalling all religious events.
- Replace Thaumaturgy by explaining supernatural effects as doctrine.

---

### Cryptology

- **Base specialization:** breaking, reading, constructing, or resisting systems intentionally designed to deny access: codes, ciphers, obfuscation, concealed order, and patterned secrecy.
- **Transferable capabilities:** concealed-structure detection, repetition exploitation, key-space reduction, sample economy, pattern isolation, false-signal rejection, access denial logic.
- **Technique identity:** Cryptology Techniques should not simply decode better. They should express the formal logic of concealed systems: reducing uncertainty, detecting deliberate obfuscation, exploiting repetition, or forcing a sealed system to expose structure.
- **Primary tags:** `utility`, `counter_read`, `disruption`
- **Secondary tags:** `setup`, `pattern_exploitation`, `control`
- **Rare or limited tags:** `attack`, `mobility`, `recovery`
- **Typical targets:** `message`, `device`, `text`, `phenomenon`
- **Typical types:** `active`, sometimes `reactive`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; paid through sample scarcity, urgency, cognitive load, and deliberate resistance.
- **Design boundary:** A Cryptology Technique should not become ordinary language work, doctrinal analysis, route planning, or direct damage. It only applies when something was deliberately concealed or structured to deny access.

#### Valid derived techniques

- Determine whether a message is encoded, disguised, corrupted, or merely unfamiliar.
- Reduce a coded problem to one missing key, pattern, symbol, or repeated unit.
- Identify which part of a sealed message is safest to test first.
- Detect that a code is meant to waste time rather than hide content.
- Create a partial opening that reveals function, urgency, target, or constraint without full translation.
- Recognize that two messages share the same hidden system.
- Prevent a false decoded result from misleading the group.
- Use repetition to expose the shape of a concealed command, name, route, or warning.
- Identify whether an enemy is communicating through fixed code, rotating code, misdirection, or noise.
- Disrupt an encoded signal by targeting its structure, not its content.

#### Invalid or overlapping techniques

- Translate normal language.
- Interpret symbolism after the code is already open.
- Understand doctrine because a sacred text is encoded.
- Navigate a route from ordinary map knowledge.
- Detect hidden objects with no encoded structure.
- Deal direct damage.
- Pick locks through manual precision unless the lock is treated as an encoded system.
- Replace Linguistics by treating all foreign language as code.
- Replace Interpretation by explaining all meaning after decoding.
- Replace Theology, History, or Geography by solving their content domains.

---

### Archaeology

- **Base specialization:** reading material remains, ruins, artifacts, use-wear, cultural residue, site sequence, lost practice, maker evidence, and abandoned structures.
- **Transferable capabilities:** material sequence reconstruction, vanished-use reading, cultural residue analysis, layer logic, preservation judgment, artifact-context relation, loss-pattern recognition.
- **Technique identity:** Archaeology Techniques should not simply reveal the past. They should express the formal logic of material remains: reading what use, sequence, abandonment, alteration, or cultural habit the physical remainder implies.
- **Primary tags:** `utility`, `pattern_exploitation`, `counter_read`
- **Secondary tags:** `setup`, `support`, `survival_window`
- **Rare or limited tags:** `attack`, `mobility`, `recovery`
- **Typical targets:** `site`, `object`, `structure`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; shaped by access, preservation state, sample breadth, disturbance, and contamination.
- **Design boundary:** An Archaeology Technique should not become document-based history, engineering, excavation labor, or social pressure. It must involve material remains and lost use.

#### Valid derived techniques

- Identify whether a site was abandoned, destroyed, sealed, repurposed, looted, or ritually closed.
- Reveal which part of a ruin still reflects original use and which part was later alteration.
- Detect that an artifact is out of place within its material context.
- Infer what kind of activity a room, object, layer, or structure once supported.
- Identify the safest area to disturb without destroying contextual evidence.
- Recognize that a ruin’s current layout hides an older circulation pattern.
- Distinguish between wear from use, violence, ritual, weather, collapse, or later occupation.
- Convert material remains into setup for History, Architecture, Theology, or Engineering.
- Prevent the group from misreading a site because of later contamination.
- Identify what evidence has been removed by looking at the material gap it left.

#### Invalid or overlapping techniques

- Recall written historical precedent without material remains.
- Repair or stabilize a structure as Engineering.
- Design buildings as Architecture.
- Excavate large areas instantly.
- Track a living creature through fresh signs.
- Translate inscriptions as Linguistics.
- Identify sacred meaning as Theology.
- Detect traps automatically.
- Restore artifacts clinically or mechanically.
- Replace History by knowing all past events.

---

### Architecture

- **Base specialization:** reading built space, circulation, structural habitability, hidden volume, design intent, spatial hierarchy, access logic, and how buildings shape behavior.
- **Transferable capabilities:** built-flow reading, intended-use inference, hidden-volume suspicion, structural habitability judgment, circulation mapping, access hierarchy, space-behavior relation.
- **Technique identity:** Architecture Techniques should not simply understand buildings better. They should express the formal logic of built space: how a structure wants movement, concealment, access, defense, hierarchy, or habitation to function.
- **Primary tags:** `utility`, `setup`, `control`
- **Secondary tags:** `mitigation`, `pattern_exploitation`, `counter_positioning`
- **Rare or limited tags:** `attack`, `recovery`, `pressure`
- **Typical targets:** `structure`, `route`, `zone`, `site`, `environment`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; paid through access limits, complexity, visibility, modification, and unfamiliar design tradition.
- **Design boundary:** An Architecture Technique should not become engineering of mechanisms, archaeological culture reading, botanical resource handling, or direct offense. It works through built form and spatial intent.

#### Valid derived techniques

- Identify which route through a building is meant for public, private, service, ritual, defensive, or hidden movement.
- Detect that a wall, floor, stair, room, or corridor implies unused volume nearby.
- Predict where exits, storage, guards, vantage points, bottlenecks, or service paths are likely to exist.
- Recognize that a space is designed to delay, expose, compress, isolate, or impress visitors.
- Use built-flow logic to choose a safer retreat, ambush, search, or negotiation position.
- Reveal which part of a structure has been modified against its original design.
- Identify where a building’s design makes concealment or surveillance most likely.
- Prevent the group from treating a ceremonial, defensive, domestic, or industrial space as the wrong type.
- Convert architectural layout into setup for movement, defense, search, or social positioning.
- Recognize that a route is suspicious because it violates the structure’s intended circulation.

#### Invalid or overlapping techniques

- Repair a mechanism as Engineering.
- Read ancient cultural remains as Archaeology.
- Build or design a structure from scratch during a scene.
- Detect traps automatically.
- Navigate wilderness terrain.
- Excavate hidden rooms physically.
- Deal direct damage.
- Command people through spatial authority.
- Replace Perception by noticing every hidden door without architectural evidence.
- Replace Engineering by solving load and device mechanics.

---

### Belicology

- **Base specialization:** formal study of war, doctrine, deployment, logistics, formations, campaigns, force posture, military systems, and organized conflict.
- **Transferable capabilities:** doctrine reading, deployment analysis, logistics inference, formation weakness recognition, escalation framing, command-pattern prediction, systemic conflict modeling.
- **Technique identity:** Belicology Techniques should not simply make the character better at fighting. They should express formal war literacy: reading organized violence as a system, identifying doctrine, predicting deployment logic, or exposing logistical and formation weaknesses.
- **Primary tags:** `utility`, `setup`, `pattern_exploitation`
- **Secondary tags:** `control`, `pressure`, `counter_read`
- **Rare or limited tags:** `recovery`, `mobility`, `attack`
- **Typical targets:** `enemy`, `group`, `zone`, `formation`
- **Typical types:** `active`, sometimes `passive`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; paid through information gaps, scale complexity, fog of war, and doctrine familiarity.
- **Design boundary:** A Belicology Technique should not become live leadership, weapon mastery, stealth infiltration, or healing. It studies conflict as doctrine and system, not individual combat execution.

#### Valid derived techniques

- Identify what doctrine a formation or deployment appears to follow.
- Reveal which part of an enemy posture is logistical rather than tactical.
- Predict which route, objective, or asset an organized force must protect next.
- Recognize that an enemy unit is bait, reserve, screen, vanguard, escort, or delaying force.
- Identify a formation’s systemic weakness without granting a direct attack bonus by itself.
- Prevent the group from misreading a retreat, feint, rotation, or regrouping.
- Use doctrine knowledge to create setup for ambush, negotiation, avoidance, or disruption.
- Detect when a battlefield layout favors attrition, encirclement, shock, harassment, or defense-in-depth.
- Identify which enemy action would indicate a shift in command intent.
- Reveal that a conflict is constrained by supply, morale, command delay, terrain, or doctrine.

#### Invalid or overlapping techniques

- Command allies in real time as leadership.
- Attack better with a weapon.
- Duel better because you know war theory.
- Heal or recover allies.
- Sneak into enemy camps.
- Read individual emotional intent.
- Predict every enemy action perfectly.
- Replace Perception by seeing hidden troops with no evidence.
- Replace History by recalling old wars without present doctrine.
- Replace Strategy/Tactics if those exist as separate live-command systems.

---

## Composure — Derived Technique Domains

Techniques are not direct upgrades to the base specialization. A technique should not simply make the character focus harder, resist panic better, meditate faster, or look calmer.

Instead, each technique should express a transferable composure process developed by that specialization and apply it to a different tactical, emotional, social, investigative, or narrative problem.

---

### Focus

- **Base specialization:** sustained attention, concentration, task fixation, ignoring distraction, holding a mental thread under pressure.
- **Transferable capabilities:** attention locking, distraction filtering, task continuity, cognitive thread retention, overload narrowing, operational fixation, interruption resistance.
- **Technique identity:** Focus Techniques should not simply make the character concentrate better. They should express the mental logic of focus: preserving one necessary line of action, refusing distraction, holding a sequence together, or completing a task while pressure tries to fracture attention.
- **Primary tags:** `utility`, `setup`, `stability`
- **Secondary tags:** `counter_read`, `mitigation`, `survival_window`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `self`, `object`, `zone`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low Rhythm, low Attrition; often paid through sustained cognitive strain, tunnel vision, reduced flexibility, or vulnerability to ignored context.
- **Design boundary:** A Focus Technique should not become emotional healing, social masking, mystical clarity, or broad resistance to all pressure. It must be tied to preserving attention on a defined task, line, object, sequence, or threat.

#### Valid derived techniques

- Maintain a delicate action while nearby danger, noise, pain, or movement would normally interrupt it.
- Hold the sequence of a ritual, repair, treatment, aim, reading, or interaction despite distraction.
- Ignore one declared distraction source for the next exchange, but become less responsive to other changes.
- Prevent a task from resetting after a minor interruption.
- Keep attention locked on a hidden, moving, unstable, or fading detail long enough to act on it.
- Continue a prepared action after being startled, shouted at, jostled, or pressured.
- Narrow attention to one operational priority, gaining reliability there while sacrificing awareness elsewhere.
- Resist having your attention redirected by bait, feint, spectacle, insult, or sensory overload.
- Preserve the exact step you were on in a complex procedure after the scene changes.
- Delay cognitive overload by reducing the scene to one necessary line of action.

#### Invalid or overlapping techniques

- Recover emotionally from fear, grief, horror, or despair.
- Prevent panic as a broad internal rupture.
- Look calm to observers.
- Deceive someone about your intentions.
- Heal mental conditions through concentration alone.
- Support the whole party with general encouragement.
- Gain a broad bonus to all mental actions.
- Ignore all sensory penalties.
- Resist physical pain as bodily toughness.
- Replace Meditation by restoring clarity through pause.
- Replace Containment by suppressing panic or horror directly.
- Replace Poise by controlling outward expression.

---

### Containment

- **Base specialization:** holding internal rupture, preventing panic, horror, emotional overload, shock, or psychic fracture from collapsing action.
- **Transferable capabilities:** panic suppression, rupture bracing, emotional compartmentalization, agency preservation, crisis containment, internal pressure sealing, collapse delay.
- **Technique identity:** Containment Techniques should not simply make the character “braver.” They should express the mental logic of containment: keeping the inside from breaking long enough to act, delaying collapse, narrowing emotional damage, or preventing internal overload from taking control.
- **Primary tags:** `mitigation`, `survival_window`, `condition_reduction`
- **Secondary tags:** `stability`, `utility`, `counter_read`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `self`, rarely `ally`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low Rhythm, low-to-medium Attrition; higher when suppressing severe fear, horror, grief, panic, or internal rupture windows.
- **Design boundary:** A Containment Technique should not become physical pain endurance, calm restoration, meditation, social acting, or deception. It does not make the character healed or serene; it keeps them functional while something inside is trying to break.

#### Valid derived techniques

- Delay the effect of panic, horror, grief, shock, or emotional overload for one critical action.
- Narrow an emotional condition so it affects one choice, sense, or exchange instead of the whole turn.
- Stay functional after witnessing something that would normally break agency.
- Prevent a fear response from forcing immediate retreat, freezing, screaming, or collapse.
- Convert emotional rupture into Attrition or later consequence instead of immediate loss of control.
- Hold a traumatic realization internally until the scene’s immediate danger passes.
- Keep acting while under a mental pressure that demands surrender, panic, confession, or paralysis.
- Prevent a failed composure check from escalating into a worse condition immediately.
- Resist an attempt to force an involuntary emotional reaction from you.
- Keep one part of yourself sealed away long enough to finish a necessary action.

#### Invalid or overlapping techniques

- Heal trauma completely.
- Become calm, centered, or restored.
- Meditate in the middle of immediate panic as the main effect.
- Ignore physical pain, poison, wounds, or fatigue.
- Hide your fear from observers as the primary effect.
- Lie convincingly about your emotional state.
- Encourage the whole group broadly.
- Gain immunity to fear or horror.
- Resist all mental effects without cost or limit.
- Replace Tolerance by enduring bodily suffering.
- Replace Meditation by restoring inner balance.
- Replace Poise by controlling visible expression.

---

### Meditation

- **Base specialization:** deliberate inward recomposition, cultivated return to center, quieting mental noise, reducing internal residue, restoring clarity through pause and practice.
- **Transferable capabilities:** mental reset, residue clearing, breath ritual, attention cleansing, emotional digestion, clarity recovery, deliberate stillness, inner preparation.
- **Technique identity:** Meditation Techniques should not simply make the character rest better. They should express the mental logic of meditation: using a pause, ritual, breath, posture, or cultivated practice to reduce internal noise, recover clarity, prepare the mind, or release accumulated pressure.
- **Primary tags:** `recovery`, `condition_reduction`, `stability`
- **Secondary tags:** `mitigation`, `utility`, `support`
- **Rare or limited tags:** `attack`, `pressure`, `mobility`
- **Typical targets:** `self`, `ally`, `zone`
- **Typical types:** `active`, `passive`
- **Usual cost profile:** low Rhythm, low Attrition; strongly dependent on time, safety, posture, silence, repetition, or a calm window.
- **Design boundary:** A Meditation Technique should not become emergency panic resistance, task concentration, social masking, or direct offense. It requires some form of deliberate inward practice and usually needs a pause or protected window.

#### Valid derived techniques

- Reduce lingering mental residue after fear, horror, overload, or disturbing contact.
- Prepare the mind before entering a dangerous scene, reducing the first disruption that targets clarity.
- Help an ally regain enough clarity to choose their next action, without controlling their emotions.
- Convert a short pause into recovery from confusion, intrusive noise, fixation, or emotional residue.
- Clear one accumulated mental penalty if the character has a safe moment to breathe and center.
- Establish a calm anchor that can be invoked later during the scene at reduced effect.
- Reduce the cost of later Containment by preparing the mind before exposure.
- Recenter after a failed mental exchange, preventing the failure from contaminating the next action.
- Use breath, posture, repetition, or ritual to regain clean attention after overload.
- Create a quiet zone of conduct where allies can recover composure if they also pause and participate.

#### Invalid or overlapping techniques

- Stop immediate panic without a pause.
- Maintain concentration on a complex task under attack.
- Hide fear, pain, or tension from observers.
- Lie convincingly by appearing calm.
- Heal wounds or physical conditions.
- Remove all trauma permanently.
- Attack enemies through inner peace.
- Grant broad group immunity to fear.
- Work while sprinting, fighting, drowning, or actively collapsing unless the technique explicitly creates a pause.
- Replace Focus by sustaining task attention.
- Replace Containment by holding rupture during the crisis itself.
- Replace Poise by managing outward appearance.

---

### Poise

- **Base specialization:** preserving outward composure, controlling expression, posture, voice, tension, tells, and visible fracture under pressure.
- **Transferable capabilities:** tell suppression, visible tension control, bearing discipline, expression management, social surface control, readable-state denial, controlled presentation.
- **Technique identity:** Poise Techniques should not simply make the character “look cool.” They should express the social-visible logic of poise: controlling what escapes outward, denying enemies a read, preserving status under scrutiny, or making pressure fail to become visible leverage.
- **Primary tags:** `utility`, `control`, `counter_read`
- **Secondary tags:** `mitigation`, `setup`, `pressure`
- **Rare or limited tags:** `attack`, `recovery`, `mobility`
- **Typical targets:** `self`, `enemy`, `group`, `zone`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low Rhythm, low Attrition; often paid through sustained visible strain, scrutiny, social stakes, or the risk of later fracture.
- **Design boundary:** A Poise Technique should not become internal emotional healing, deliberate lie construction, intimidation, persuasion, or deception by narrative. It controls visible leakage, not truth itself.

#### Valid derived techniques

- Deny an enemy the benefit of reading your fear, pain, hesitation, or surprise.
- Prevent a visible reaction from escalating a social, tactical, or hostile exchange.
- Keep your voice, posture, or expression steady while under scrutiny.
- Make an injury, shock, insult, or revelation less legible to observers for one exchange.
- Preserve apparent authority or control long enough to avoid immediate challenge.
- Reduce the effectiveness of an opponent’s attempt to provoke a visible response.
- Hide which option, threat, ally, object, or statement affected you most.
- Maintain ceremonial, diplomatic, or command bearing despite internal pressure.
- Prevent a failed internal reaction from becoming public leverage.
- Force an observer to rely on evidence rather than your visible tells.

#### Invalid or overlapping techniques

- Actually remove fear, grief, panic, or horror.
- Resist internal collapse as the main effect.
- Lie by constructing a false story.
- Persuade, intimidate, or inspire through charisma alone.
- Hide physically from sight.
- Disguise identity.
- Endure physical pain as bodily resistance.
- Maintain concentration on a task.
- Meditate or recover clarity.
- Replace Deception by creating false narratives.
- Replace Containment by preventing emotional rupture internally.
- Replace Focus by sustaining operational attention.

---

## Aura — Derived Technique Domains

Techniques are not direct upgrades to the base specialization. A technique should not simply make the character react better, resonate harder, bond more deeply, or handle creatures more easily.

Instead, each technique should express a transferable essential process developed by that specialization and apply it to a different tactical, emotional, creature-based, spiritual, or narrative problem.

---

### Instinct

- **Base specialization:** primary response, preconscious recoil, essential recognition, immediate refusal, readiness before analysis, and action before conscious certainty.
- **Transferable capabilities:** preconscious warning, essential mismatch recognition, danger recoil, hesitation bypass, primal readiness, refusal before explanation, exposure-triggered response.
- **Technique identity:** Instinct Techniques should not simply let the character guess correctly. They should express the aura logic of instinct: reacting before analysis finishes, refusing what feels fundamentally wrong, recognizing threat before form, or preserving agency through primary response.
- **Primary tags:** `counter_read`, `survival_window`, `setup`
- **Secondary tags:** `utility`, `mitigation`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `support`, `pressure`
- **Typical targets:** `self`, `enemy`, `zone`, `phenomenon`
- **Typical types:** `reactive`, `passive`, sometimes `active`
- **Usual cost profile:** low Rhythm, low Attrition; usually triggered by exposure, contact, threat, dissonance, or sudden pressure rather than deliberate exertion.
- **Design boundary:** An Instinct Technique should not become structured deduction, formal analysis, doctrine, social control, or mechanical understanding. It reveals urgency, recoil, readiness, or refusal, not full explanation.

#### Valid derived techniques

- React before a threat becomes fully understood, gaining a narrow window to move, brace, refuse, or prepare.
- Recognize that something in the scene is wrong for you before you can explain why.
- Refuse an action that would expose you to immediate essential danger, without learning the full nature of the danger.
- Recoil from a phenomenon, creature, object, or zone that carries harmful dissonance.
- Act through hesitation when conscious analysis would delay the necessary response.
- Detect that a choice is fundamentally unsafe, without identifying the correct choice.
- Preserve agency when something tries to override your first response with confusion, awe, lure, or paralysis.
- Treat a sudden internal pull as a warning that one immediate interaction should be avoided or delayed.
- Convert an instinctive flinch into a defensive setup rather than wasted movement.
- Sense that an enemy, place, or phenomenon is about to cross a threshold of danger, without knowing the mechanism.

#### Invalid or overlapping techniques

- Solve a mystery through instinct alone.
- Identify exactly what a creature, object, ritual, or phenomenon is.
- Analyze thaumic laws or formal supernatural systems.
- Read doctrine, symbolism, or sacred meaning.
- Persuade, intimidate, or command others.
- Repair, disable, or understand mechanisms.
- Predict every enemy action perfectly.
- Gain a broad bonus to all reactions.
- Replace Intuition by drawing structured conclusions from pattern tension.
- Replace Thaumaturgy by explaining aura or energy formally.
- Replace Resonance by tuning deliberately into a force or presence.
- Replace Bond by sensing someone without an established link.

---

### Resonance

- **Base specialization:** deliberate aura tuning, meaningful contact with forces, places, presences, states, phenomena, or essential fields.
- **Transferable capabilities:** attunement, dissonance reading, harmonic adjustment, contact safety, gentle pressure, essential alignment, interference management, resonance stabilization.
- **Technique identity:** Resonance Techniques should not simply make the character “sense aura better.” They should express the aura logic of resonance: tuning toward contact, aligning with a presence, reducing dissonance, stabilizing interaction, or making an essential field meaningful enough to act on.
- **Primary tags:** `utility`, `counter_read`, `condition_reduction`
- **Secondary tags:** `setup`, `mitigation`, `pattern_exploitation`
- **Rare or limited tags:** `attack`, `mobility`, `support`
- **Typical targets:** `phenomenon`, `zone`, `self`, `object`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low-to-moderate Rhythm, low-to-medium Attrition; often paid through exposure to dissonance, interference, intensity, instability, or unwanted feedback.
- **Design boundary:** A Resonance Technique should not become academic thaumic analysis, pure reflex, social persuasion, doctrine, or brute-force aura damage. It must involve deliberate tuning, contact, alignment, interference, or essential field response.

#### Valid derived techniques

- Tune yourself to a place, object, creature, or phenomenon enough to understand whether contact is safe.
- Detect dissonance between a presence and the zone, object, body, or state it occupies.
- Reduce the penalty of interacting with an unstable aura field by aligning before contact.
- Stabilize a minor resonance long enough for another action to be attempted.
- Recognize whether a force is inviting contact, resisting contact, echoing, contaminating, or interfering.
- Create a temporary point of alignment that helps you withstand feedback from a phenomenon.
- Gently push against a dissonant presence to reveal its direction, boundary, or intensity.
- Separate your own aura response from surrounding interference for one exchange.
- Convert overwhelming resonance into a limited signal: safe, unsafe, unstable, familiar, hostile, or hollow.
- Prepare yourself or an object to receive contact without immediately worsening the dissonance.

#### Invalid or overlapping techniques

- Analyze supernatural laws as formal Thaumaturgy.
- React automatically with no deliberate tuning.
- Command a spirit, creature, crowd, or group.
- Deal direct damage by “resonating harder.”
- Create a bond instantly.
- Calm animals through handling.
- Interpret religious meaning or sacred doctrine.
- Identify all properties of a phenomenon.
- Become immune to aura feedback without cost.
- Replace Instinct by turning all reflexes into resonance.
- Replace Bond by sensing a specific being without a sustained link.
- Replace Theology or Thaumaturgy by explaining all spiritual phenomena.

---

### Bond

- **Base specialization:** sustained essential link between the self and a specific being, usually formed before the technique is used.
- **Transferable capabilities:** link continuity, distance sensitivity, shared warning, relational stabilization, strain reading, mutual state awareness, connection preservation, essential trust.
- **Technique identity:** Bond Techniques should not simply create connection whenever needed. They should express the aura logic of an existing link: sensing strain, sharing warning, preserving connection, stabilizing relation, or acting through continuity with a specific being.
- **Primary tags:** `support`, `setup`, `counter_read`
- **Secondary tags:** `utility`, `mitigation`, `survival_window`
- **Rare or limited tags:** `attack`, `pressure`, `mobility`
- **Typical targets:** `self`, `ally`, `creature`
- **Typical types:** `active`, `passive`, sometimes `reactive`
- **Usual cost profile:** low Rhythm, low Attrition; shaped by distance, strain on the bond, harm, emotional state, interference, and the linked being’s condition.
- **Design boundary:** A Bond Technique should not become broad leadership, generic animal handling, instant aura contact, social influence, or party-wide support. It only works through a real sustained link that already exists.

#### Valid derived techniques

- Sense that a bonded being is in danger, distressed, severed, hidden, nearby, or under strain.
- Share a simple warning, emotional pressure, or direction through an existing bond.
- Stabilize a bonded ally or creature long enough for them to resist panic, confusion, or separation.
- Preserve connection when distance, fear, pain, or interference would normally disrupt coordination.
- Recognize whether a bonded being is acting against its usual state or under outside pressure.
- Take on a small portion of bond strain to prevent immediate collapse of the connection.
- Use the bond as an anchor to locate the general direction of the linked being, not their exact path.
- Help a bonded creature or ally recognize you through fear, confusion, pain, or transformation.
- Prevent a hostile force from fully isolating the bonded being for one exchange.
- Turn shared familiarity into setup for coordinated action, warning, retreat, or recovery.

#### Invalid or overlapping techniques

- Create a deep bond instantly.
- Affect strangers, crowds, or the whole party without prior connection.
- Command allies through authority.
- Train animals through repetition and handling.
- Calm any creature with no established link.
- Read exact thoughts.
- Know precise location across any distance without limits.
- Deal direct weapon pressure through the bond.
- Replace Domestication by handling creatures in general.
- Replace Resonance by contacting any presence temporarily.
- Replace Instinct by sensing danger with no linked being.
- Replace social skills by making people trust you because of “bond.”

---

### Domestication

- **Base specialization:** calming, guiding, familiarizing, training, reading, and preventing escalation in instinctive creatures through practical handling.
- **Transferable capabilities:** response shaping, threshold reading, habituation, nonverbal cue use, escalation prevention, creature pacing, trust-building through repetition, safe handling windows.
- **Technique identity:** Domestication Techniques should not simply make the character better at handling animals or creatures. They should express the practical aura logic of creature response: reading instinctive thresholds, preventing panic, shaping reaction, guiding behavior, or creating a safe window before chaos breaks open.
- **Primary tags:** `control`, `support`, `mitigation`
- **Secondary tags:** `setup`, `utility`, `survival_window`
- **Rare or limited tags:** `attack`, `pattern_exploitation`, `pressure`
- **Typical targets:** `creature`, `mount`, `self`, `zone`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; paid through exposure risk, agitation, repeated handling pressure, proximity, trust, and the creature’s current state.
- **Design boundary:** A Domestication Technique should not become mounted line control, deep essential bonding, abstract social authority, or doctrinal understanding. It must involve a creature’s instinctive response, handling threshold, familiarity, or escalation state.

#### Valid derived techniques

- Prevent a creature from escalating from agitation into panic, attack, flight, or frenzy.
- Read which stimulus is driving a creature’s current response: pain, fear, hunger, territory, confusion, protection, or habit.
- Create a brief safe-handling window to approach, lead, restrain, calm, feed, free, or redirect a creature.
- Guide a familiar creature through a dangerous space without turning it into mounted technique.
- Reduce the risk of handling a wounded, frightened, trapped, or overstimulated creature.
- Shift a creature’s attention away from a trigger before it commits to violence or escape.
- Use repeated cues to make a creature tolerate one uncomfortable action.
- Stop an ally from provoking a creature by identifying the wrong movement, sound, posture, or distance.
- Recognize that a creature is not hostile but overwhelmed, trained, injured, territorial, or conditioned.
- Turn creature behavior into a temporary warning system, obstruction, distraction, or route opening.

#### Invalid or overlapping techniques

- Control a creature like a machine.
- Command a mount through battle lines as Riding.
- Create a deep essential link as Bond.
- Calm any intelligent group through authority.
- Persuade people socially.
- Read doctrine, symbols, or sacred behavior.
- Deal direct damage through creature handling.
- Train a creature instantly with no repetition or exposure.
- Make all animals friendly.
- Replace Survival by handling all wilderness problems.
- Replace Poise or Deception by controlling social presentation.
- Replace Resonance by treating every creature as an aura field.

---

## Presence — Derived Technique Domains

Techniques are not direct upgrades to the base specialization. A technique should not simply make the character lead better, negotiate better, intimidate harder, imitate more accurately, or hide better.

Instead, each technique should express a transferable presence process developed by that specialization and apply it to a different tactical, social, investigative, positional, or narrative problem.

---

### Leadership

- **Base specialization:** directing allies, preserving cohesion, assigning priorities, rallying action, maintaining group structure, and turning presence into recognized direction.
- **Transferable capabilities:** command framing, cohesion preservation, priority assignment, group re-centering, responsibility anchoring, synchronized timing, morale structure, fragmentation prevention.
- **Technique identity:** Leadership Techniques should not simply make the character “give better orders.” They should express the social logic of leadership: turning presence into structure, preventing fragmentation, creating shared timing, assigning a common line, or making a group act as one under pressure.
- **Primary tags:** `support`, `control`, `setup`
- **Secondary tags:** `pressure`, `mitigation`, `survival_window`
- **Rare or limited tags:** `attack`, `stealth`, `recovery`
- **Typical targets:** `ally`, `group`, `formation`, `zone`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; often paid through command strain, responsibility pressure, visibility, and the risk of blame if the line fails.
- **Design boundary:** A Leadership Technique should not become fear coercion, war scholarship, deception, disguise, or hidden presence. It works through recognized direction among those able or willing to follow.

#### Valid derived techniques

- Prevent a group from fragmenting when danger, confusion, fear, or conflicting priorities would split them.
- Assign one shared priority so allies can act under the same tactical line for the next exchange.
- Re-center allies after a failed plan without restoring them emotionally or healing them.
- Turn scattered allied actions into a coordinated opening, retreat, defense, or regroup.
- Preserve formation integrity when enemies try to isolate, bait, or pull allies out of position.
- Create a clear chain of action so one ally’s success sets up another ally’s response.
- Make hesitation costly by giving the group a visible decision point to rally around.
- Anchor a zone around your command presence, making allies less likely to waste actions on panic or contradiction.
- Convert responsibility into tempo: allies know who moves, who covers, who withdraws, or who holds.
- Reduce the penalty of acting in a chaotic group scene by establishing a temporary command structure.

#### Invalid or overlapping techniques

- Terrify enemies into submission.
- Negotiate mutual terms.
- Lie about the situation through false narrative.
- Disguise yourself as someone else.
- Hide your presence.
- Analyze military doctrine as Belicology.
- Command strangers with no authority, trust, pressure, or recognized role.
- Heal emotional or physical harm through encouragement alone.
- Grant broad bonuses to all allies without a shared line of action.
- Replace Negotiation by forcing agreement.
- Replace Intimidation by using fear as the main tool.
- Replace Poise by merely looking composed.
- Replace Strategy or Belicology if those exist as separate systems.

---

### Negotiation

- **Base specialization:** bargaining, concession, leverage, terms, exchange framing, de-escalation through deal-space, and agreement under contested interests.
- **Transferable capabilities:** concession framing, leverage recognition, acceptable-loss calculation, term structuring, reciprocity pressure, exchange preservation, escalation control, deal-space creation.
- **Technique identity:** Negotiation Techniques should not simply make the character “talk someone into it.” They should express the social logic of negotiation: turning conflict into terms, exposing leverage, creating acceptable exchange, delaying collapse, or making both sides act through a shared bargain frame.
- **Primary tags:** `utility`, `control`, `support`
- **Secondary tags:** `setup`, `disruption`, `counter_read`
- **Rare or limited tags:** `attack`, `stealth`, `direct_mitigation`
- **Typical targets:** `enemy`, `ally`, `group`, `zone`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low Rhythm, low Attrition; shaped by leverage, urgency, exposed position, trust, stakes, and whether either side can afford to walk away.
- **Design boundary:** A Negotiation Technique should not become deception, intimidation, leadership, or stealth. It requires terms, leverage, concession, exchange, or mutually legible stakes.

#### Valid derived techniques

- Convert immediate hostility into a temporary exchange window before violence resumes.
- Force both sides to name what they are risking, making reckless escalation harder.
- Reveal which concession would actually matter, without forcing the target to accept it.
- Delay an enemy’s action by making refusal carry an explicit cost.
- Turn a demand into structured terms that can be accepted, rejected, or countered.
- Preserve a fragile agreement for one exchange by clarifying what breaks it.
- Use leverage to make a target choose between progress and escalation.
- Protect an ally from immediate retaliation by placing their action inside negotiated terms.
- Create a narrow safe-conduct window for speaking, moving, trading, surrendering, or retreating.
- Identify when the other side is negotiating from fear, pride, need, duty, or lack of alternatives.

#### Invalid or overlapping techniques

- Make someone believe a false story as the main effect.
- Terrify someone into obedience.
- Command allies through authority.
- Disguise yourself as another role or person.
- Sneak past scrutiny.
- Force agreement with no leverage.
- Make hostile parties instantly friendly.
- Remove consequences from broken terms.
- Replace Leadership by coordinating allies.
- Replace Intimidation by relying on threat alone.
- Replace Deception by hiding the truth through lies.
- Replace Poise by merely appearing calm during talks.

---

### Intimidation

- **Base specialization:** threat projection, coercive presence, dominance display, credible consequence, fear pressure, and forcing hesitation through menace.
- **Transferable capabilities:** consequence framing, fear leverage, dominance assertion, resistance collapse, threat credibility, escalation pressure, visible danger control, submission window creation.
- **Technique identity:** Intimidation Techniques should not simply make the character “scarier.” They should express the social logic of intimidation: making consequence feel immediate, forcing hesitation, collapsing resistance, or making another party yield because the cost of defiance becomes visible.
- **Primary tags:** `pressure`, `control`, `disruption`
- **Secondary tags:** `setup`, `counter_read`, `survival_window`
- **Rare or limited tags:** `recovery`, `stealth`, `support`
- **Typical targets:** `enemy`, `group`, `zone`, `self`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low Rhythm, low Attrition; exposure becomes high if the threat fails, is challenged, or must be sustained.
- **Design boundary:** An Intimidation Technique should not become negotiation, leadership, deception, disguise, or quiet concealment. It works through credible threat, not mutual agreement or false identity.

#### Valid derived techniques

- Make an enemy hesitate before advancing because the consequence of doing so is visibly credible.
- Force a target to choose between continuing an action and exposing themselves to immediate retaliation.
- Collapse a weak group’s coordination by making one member’s fear visible to the others.
- Turn a successful display of force into control over the next exchange’s tempo.
- Prevent a target from taking a minor advantage because claiming it would invite direct consequence.
- Make refusal costly enough that the target must spend tempo proving they are not afraid.
- Break a fragile morale line without giving tactical orders or making a bargain.
- Deny an opponent the comfort of safety, cover, numbers, rank, or distance for one exchange.
- Use silence, posture, weapon position, or proximity to make the threat clearer than speech.
- Make a hostile party reveal whether they are truly committed or only testing resistance.

#### Invalid or overlapping techniques

- Build mutual agreement.
- Lead allies through recognized authority.
- Trick someone with a false narrative.
- Impersonate someone else.
- Hide from attention.
- Inspire loyalty or trust.
- Analyze doctrine or military posture.
- Deal direct damage through fear alone.
- Make all enemies flee automatically.
- Replace Negotiation by treating threats as deals.
- Replace Leadership by commanding through fear.
- Replace Deception by bluffing without credible consequence.
- Replace Poise by looking composed under pressure.

---

### Imitation

- **Base specialization:** reproducing voice, manner, posture, timing, role, social pattern, or recognizable personhood well enough to be treated as that thing instead of yourself.
- **Transferable capabilities:** embodied substitution, role mimicry, behavioral rhythm copying, voice shaping, social pattern reproduction, expectation hijacking, scrutiny management, performed familiarity.
- **Technique identity:** Imitation Techniques should not simply make the character “copy someone better.” They should express the social logic of imitation: being read through a borrowed role, causing others to apply the wrong expectations, passing through social pattern, or making embodied performance alter response.
- **Primary tags:** `utility`, `setup`, `counter_read`
- **Secondary tags:** `control`, `disruption`, `pressure`
- **Rare or limited tags:** `attack`, `recovery`, `mobility`
- **Typical targets:** `self`, `group`, `creature`, `zone`
- **Typical types:** `active`, `reactive`
- **Usual cost profile:** low-to-moderate Rhythm, low Attrition; increases with scrutiny, duration, familiarity of observers, fidelity demands, and contradiction risk.
- **Design boundary:** An Imitation Technique should not become broad verbal deception, stealth, coercive command, or physical damage. It must involve embodied role, recognizable pattern, mimicry, or social substitution.

#### Valid derived techniques

- Borrow a role’s expected behavior so observers delay questioning your presence.
- Reproduce a familiar gesture, phrase, rhythm, or posture to pass one layer of scrutiny.
- Make a group respond to you according to the role you are performing, not your true identity.
- Hide an action inside a copied routine, ceremony, duty, accent, habit, or social script.
- Imitate a superior, servant, guard, patient, messenger, local, priest, worker, or captive well enough to alter immediate response.
- Make an enemy hesitate because your movement resembles an ally, superior, victim, or expected contact.
- Copy a creature’s nonverbal pattern enough to avoid immediate escalation, without controlling it.
- Use mimicry to create a false opening, mistaken permission, delayed alarm, or social misread.
- Preserve an imitation after a minor contradiction by adjusting behavior before scrutiny sharpens.
- Identify which part of the role must be performed correctly for the scene to accept it.

#### Invalid or overlapping techniques

- Lie convincingly without embodied performance.
- Become physically invisible.
- Hide in shadows or move silently as the main effect.
- Command others through real authority.
- Terrify targets through threat.
- Negotiate terms.
- Perfectly copy a person with no study, exposure, or risk.
- Gain another person’s memories, rights, or relationships automatically.
- Deal direct damage through performance.
- Replace Deception by making all lies imitation.
- Replace Stealth by being unnoticed without a role.
- Replace Leadership by issuing real command through borrowed authority.

---

### Stealth

- **Base specialization:** reducing presence, avoiding fixation, controlling exposure, moving beneath attention, softening perceptual footprint, and becoming socially or sensorially unimportant.
- **Transferable capabilities:** attention avoidance, footprint reduction, exposure timing, rhythm suppression, presence softening, fixation denial, notice-window reading, low-signal movement.
- **Technique identity:** Stealth Techniques should not simply make the character “hide better.” They should express the presence logic of stealth: becoming less meaningful to attention, avoiding fixation, passing beneath active notice, or managing exposure before others decide you matter.
- **Primary tags:** `stealth`, `setup`, `counter_read`
- **Secondary tags:** `mobility`, `survival_window`, `disruption`
- **Rare or limited tags:** `attack`, `support`, `recovery`
- **Typical targets:** `self`, `creature`, `route`, `zone`
- **Typical types:** `active`, `reactive`, sometimes `passive`
- **Usual cost profile:** low Rhythm, low Attrition; paid through restraint, timing, route choice, limited speed, exposure management, and the risk of sudden fixation.
- **Design boundary:** A Stealth Technique should not become identity substitution, verbal deceit, explicit bargaining, threat projection, or fine manual theft. It works by reducing registration, not by becoming someone else or convincing someone of a claim.

#### Valid derived techniques

- Delay being treated as important by blending into background motion, noise, crowd, routine, or clutter.
- Move through a watched space during a moment when attention is committed elsewhere.
- Prevent a minor exposure from becoming full detection by reducing immediate significance.
- Break fixation after being noticed briefly, forcing observers to spend effort confirming you.
- Pass near a threat by matching the scene’s rhythm instead of hiding behind cover alone.
- Reduce the attention drawn by an ally, object, movement, or mistake for one exchange.
- Cross a short exposed route by timing movement through distraction, repetition, or visual noise.
- Deny an enemy a clean target read if they only partially registered your presence.
- Turn stillness, silence, crowd behavior, dimness, or routine into temporary non-importance.
- Make a zone harder to search because your presence leaves fewer meaningful cues.

#### Invalid or overlapping techniques

- Impersonate a guard, servant, priest, or local.
- Lie about why you are present.
- Negotiate passage.
- Threaten observers into ignoring you.
- Pick pockets or acquire objects as the main effect.
- Become impossible to perceive.
- Hide allies broadly without scene logic.
- Move at full speed with no exposure cost.
- Replace Imitation by using role performance.
- Replace Deception by explaining away suspicion.
- Replace Theft by removing objects unnoticed.
- Replace Poise by merely controlling visible emotion.

---

## Next Blocks

Planned order:

No remaining planned blocks in this pass.

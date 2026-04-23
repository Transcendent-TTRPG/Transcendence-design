# Specializations

**Authority data:** `data/system/specializations.yaml`
**Related ADR:** `docs/adr/system-abilities-and-specializations.md`
**Related docs:** `docs/system/competencies.md`, `docs/system/characteristics.md`

---

## Purpose

This document defines what specializations are in Transcendence, what they are for, what they are **not**, and how they relate to the rest of the system.

Specializations are one of the central pillars of character identity. Since the game does not rely on traditional classes, the main way characters differentiate themselves is through **what they practice, how they solve problems, and which domains they develop**.

Specializations are also the primary path through which characters improve their **attributes**, since Synapsis is tied to the growth of practiced domains rather than to level-based point assignment.

This document exists to prevent conceptual drift. A specialization is not just "something you can roll," nor a catch-all category for maneuvers, actions, or core mechanics. It must obey a stricter structural logic.

---

## Core Principle

A **specialization** is a **trainable technical, practical, or methodological domain**.

It represents something that:

- can be practiced repeatedly
- can improve over time
- can generate multiple techniques or advanced uses
- cannot be fully replaced by a raw attribute roll alone
- meaningfully differentiates two characters who may share the same base attribute

A specialization is not simply "an action."
It is the **domain that makes certain actions, techniques, or solutions possible**.

---

## Why Specializations Exist

Specializations fulfill four major roles in the system.

### 1. Character differentiation

Because the game does not use classes, the main distinction between characters comes from:

- what they know how to do
- how they approach danger, travel, conflict, craft, and interpretation
- which practical or technical domains they have developed

### 2. Technique enablement

Specializations are the **enablers of Techniques**.
A Technique is not a specialization. A Technique is something that emerges from a specialization.

Example:

- a character may have **Lanzamiento** as a specialization
- from that domain, they may later develop multiple throwing-related Techniques

This is different from treating "throw hard," "throw accurately," or "disarm by throwing" as specializations themselves.

### 3. Synapsis and attribute growth

Specializations are the main route through which characters improve attributes.

This means:

- attributes are not upgraded freely or abstractly
- characters improve their attributes by repeatedly practicing domains linked to those attributes
- a specialization is therefore not just a roll; it is a structural growth path

### 4. World logic and role identity

Specializations help support the game's fiction. In a world without classes, identity emerges from practice.

A character becomes recognizable not because the sheet says "fighter" or "rogue," but because they are someone who tracks, someone who negotiates, someone who survives in the wilderness, someone who practices alchemy, someone who reads architecture, someone who keeps control under pressure.

---

## What a Specialization Is Not

A specialization is **not**:

- a raw expression of an attribute
- a universal system mechanic
- a single maneuver
- a narrow trick
- a temporary state
- a one-off combat option
- an effect that already belongs to another core rule

This is especially important because some things may look skill-like at first glance but structurally belong elsewhere.

---

## The Four Design Clauses

Every specialization must pass all four clauses. Failure on any one is grounds to reject or restructure the candidate.

### Raw Attribute Clause

> If a situation can be resolved in a complete and satisfying way through a raw attribute test alone, it should not become a specialization.

Examples of things that often belong to raw attribute logic:

- direct contest of strength
- immediate physical resistance
- direct composure check
- brute force endurance in a non-technical situation

This does not mean specializations never interact with those moments. It means the specialization must represent something beyond the attribute itself.

### Technique Clause

> If a candidate cannot realistically support several Techniques, it is probably not a specialization.

This removes problematic candidates from the list:

- actions that are too narrow
- single combat maneuvers
- cases that are really just one trick
- mechanics that belong inside a specialization instead of being one

Things that fail this clause should be treated as Techniques, maneuvers, combat options, or derived uses rather than specializations.

### Differentiation Clause

> A specialization must create practical distinction between characters who share the same attribute but have developed different domains.

Fine distinctions matter because identity is built from practice. For example:

- two characters with similar Wisdom may still feel very different if one has **Medicina** and the other has **Supervivencia**
- two characters with similar Cunning may differ strongly through **Rastreo**, **Improvisación**, or **Engaño**
- two characters with similar Tenacity may not become identical if their growth paths diverge through **Marcha**, **Aclimatación**, or **Tolerancia**

### Trainability Clause

> A specialization must be something a character can practice as a discipline — not just a condition of being alive or a passive state of existence.

This is especially relevant when dealing with:

- body-based domains
- emotional stability
- instinctive qualities
- aura-linked domains

Some concepts must be carefully framed so that they remain trainable without losing their narrative identity.

---

## Structural Relationship: Attribute → Specialization → Technique

These three layers must remain distinct.

| Layer | What it represents | Scope |
| --- | --- | --- |
| **Attribute** | Broad natural capacity | How strong, fast, perceptive, steady, present you are |
| **Specialization** | Trainable domain tied to one attribute | Practiced growth path through repeated use |
| **Technique** | Advanced application enabled by a specialization | Narrow, costed, mechanically-defined; requires competency prerequisite |

> Attribute = capacity. Specialization = trainable domain. Technique = specific advanced expression of that domain.

---

## Specialization Roll

```text
S.R. = 1d10 + Specialization Level + Competency Rank + Associated Characteristic + Bonuses
```

**Authority:** `data/system/specializations.yaml`

A specialization does not mean a character is the only one allowed to attempt something. A character may still attempt many actions outside a specialization when the system permits it. However, the specialization represents the trained path, the greater depth of use, the method behind advanced application, and the route to Techniques.

---

## Starting Specializations

Every character begins with **4 specializations at Level 1 / Novice**:

- 3 from background (according to background category restrictions)
- 1 universal choice from **Tenacity**: **Marcha**, **Aclimatación**, or **Tolerancia**

The same specialization cannot be chosen twice at creation. All others begin at Level 0 (Untrained).

### Universal Starting Tenacity Specialization

| Property | Value |
| --- | --- |
| Associated characteristic | Tenacity |
| Starting level | 1 / Novice |
| Synapsis at creation | +1 Tenacity |
| Allowed choices | Marcha, Aclimatación, Tolerancia |
| Stacks with | Species bonuses to Tenacity |

Every playable character begins with one Tenacity specialization at Rank 1. This reflects a basic truth of the setting: surviving in the world always requires some trained relation to effort, pain, endurance, or adverse conditions, but not every life expresses that resilience in the same way.

This choice does not replace species bonuses to Tenacity — both accumulate. Because all eligible options are linked to Tenacity, every character still gains at least +1 Tenacity through starting Synapsis, but the expression of that resilience now differs by history.

---

## Categories

The catalog uses broad content categories for organization. These are secondary to the structural truth — the primary truth of every specialization is which **attribute** it belongs to and whether it passes all four design clauses.

| Category | Primary attributes | Domain type |
| --- | --- | --- |
| Physical | STR, AGI, TEN | Bodily technique, movement, exertion, practical bodily control |
| Mental | CUN, WIS, INT | Interpretation, cunning, attention, reading, situational reasoning |
| Social | CMP, AUR, PRE | Influence, expression, projection, deception, interpersonal control |
| Arts and Crafts | WIS | Making, repairing, preparing, extracting, applied practical work, and concrete arts such as performance, music, dance, juggling, or puppetry |
| Knowledge | INT | Formal study, academic interpretation, structured lore, technical intellectual understanding |

### Artistic Domains Inside Arts and Crafts

Artistic disciplines belong inside **Arts and Crafts**, not inside Presence by default.

In the current model they should be treated as Wisdom-linked trainable practices, not as pure charisma expressions. Typical examples include:

- `Performance`
- `Music`
- `Dance`
- `Juggling`
- `Puppetry`

This preserves the distinction between:

- **Presence** as social weight, projection, command, or suppression of attention
- **Arts and Crafts** as practiced production, execution, rehearsal, and applied technique

### Artistic and Craft Downtime Activity

Characters may dedicate a `4-hour` block to producing an artistic or crafted piece.

- The acting specialization must belong to **Arts and Crafts**
- The chosen specialization must match the actual work produced
- Minimum tools and materials are required
- Each `4-hour` block grants one attempt
- Failure grants no payout for that block

The player chooses a named difficulty tier representing the complexity of the piece:

| Difficulty | Reward |
| --- | --- |
| Foundational | `2d4` Obsidian Shekels |
| Challenging | `2d6` Obsidian Shekels |
| Rigorous | `2d8` Obsidian Shekels |
| Demanding | `2d10` Obsidian Shekels |
| Extreme | `2d12` Jade Shekels |

The exact money chapter can later define how those currencies circulate, but this table already establishes the specialization-side procedure for downtime artistic and craft production.

---

## Distribution Across Attributes

Not every attribute must have the same number of specializations. The system does not require perfect numerical symmetry.

Distribution should reflect two realities:

**Practical need** — some attributes naturally support more technical or interpretive domains. This is why Wisdom and Intellect may legitimately carry more specializations: they absorb crafts, knowledge systems, and field interpretation.

**Synapsis balance** — some attributes should not receive too many easy or universal routes to growth. If they receive too many general-use specializations, they become too easy to raise through normal play.

### Special note on Tenacity

Tenacity-linked domains tend to be broad, global, and frequently exercised by many characters. Tenacity should not be overloaded with too many specializations. A smaller set of well-separated domains is preferable.

### Special note on Aura

Aura is not fully active or fully voluntary. It reflects something innate, projected, resonant, or reacted to as much as consciously performed.

Aura-linked specializations should:

- remain trainable
- enable Techniques
- preserve the passive or involuntary nature of Aura
- avoid becoming generic social skills or magical power categories

Aura domains should tend to reflect instinct, resonance, link, attunement, involuntary influence, or presence felt rather than consciously performed.

### Special note on Composure

Composure should not be filled with abstract virtues or vague personality ideals.

Composure-linked specializations should focus on: concentration, containment, meditation, poise under visible strain.

It should not become a bucket for every word that sounds like "being calm."

---

## Design Test for New Specializations

When a new specialization is proposed, apply these six questions:

1. Can this be resolved sufficiently with a raw attribute roll? → If yes, probably not a specialization.
2. Does this represent a trainable domain? → If no, not a specialization.
3. Can this generate several Techniques? → If no, likely too narrow.
4. Would two characters with the same base attribute feel different if only one had this? → If no, may not be meaningful enough.
5. Is this actually a maneuver, Technique, or core mechanic disguised as a specialization? → If yes, belongs elsewhere.
6. Does this specialization create a valid path for Synapsis? → If no, its structural purpose is weak.

---

## Relationship with Combat

Specializations are not inherently combat actions. Some may support combat Techniques or reactions. Others may matter more outside combat.

What matters is that a specialization remains a **domain**, not a combat button. Combat options may be born from specializations but should not be confused with them.

---

## Relationship with ATB

Specializations may later affect rhythm cost, Attrition, or both — but only through specific Techniques, friction reduction, advanced mastery, or explicit design rules.

A specialization itself is not automatically a faster or cheaper action. The specialization is the domain. The timing change comes later through what that domain unlocks.

---

## Structural Conclusions

1. Specializations are trainable technical, practical, or methodological domains.
2. Specializations are the primary enablers of Techniques.
3. Specializations are the main route through which characters improve attributes via Synapsis.
4. A specialization must not be reducible to a raw attribute roll alone.
5. A specialization must be broad enough to support multiple Techniques.
6. A specialization must differentiate characters who share the same base attribute.
7. A specialization must be trainable and repeatedly usable in play.
8. Not every attribute needs the same number of specializations.
9. Wisdom and Intellect may legitimately have larger catalogs.
10. Tenacity should remain more controlled because its domains are broadly exercised.
11. Aura-linked domains require special care because Aura is partly passive or involuntary.
12. Composure-linked domains should focus on practiced inner regulation, not vague virtues.

---

## Current Catalog

Each entry shows the specialization name, content category, core domain, and boundaries (what it covers and what belongs elsewhere). Attribute identity lines are included for context.

This catalog establishes working identities and design boundaries. Full player-facing descriptions, Techniques, ATB interactions, and Synapsis notes are later-stage work.

---

### Strength

**Attribute identity:** raw power, explosive output, physical leverage, bodily force applied with intent.

**Saltar** · Physical

- **Core domain:** using force to project the body through vertical or horizontal space
- **Covers:** leaps, explosive takeoff, forced crossing, jump-based movement
- **Does not cover:** aerial control, graceful landing, evasive body redirection

**Trepar** · Physical

- **Core domain:** ascending or descending surfaces through strength-based bodily placement
- **Covers:** climbing, hanging, hauling oneself upward, descending under control
- **Does not cover:** balance on unstable surfaces, acrobatic repositioning, jumping

**Lanzamiento** · Physical

- **Core domain:** throwing with trained force, angle, and projection
- **Covers:** thrown objects, thrown weapons, distance projection through technique
- **Does not cover:** ranged weapon systems that rely on separate mechanics, brute shoving, raw grip contests

**Nadar** · Physical

- **Core domain:** moving the body through water through trained propulsion and control
- **Covers:** swimming, staying afloat, crossing water, underwater bodily movement
- **Does not cover:** breath control as a separate abstract system, climate adaptation, survival at sea in a broad sense

**Agarre** · Physical

- **Core domain:** trained grip, hold, retention, and force application through contact
- **Covers:** holding, restraining, wrenching, controlling through grip, stabilizing weight through the hands/body
- **Does not cover:** general wrestling as a universal combat category, raw force contests with no technical handling

---

### Agility

**Attribute identity:** bodily finesse, coordination, clean execution, controlled motion, responsive balance.

**Acrobacias** · Physical

- **Core domain:** complex body movement through trained coordination
- **Covers:** flips, rolls, evasive movement, dynamic body redirection
- **Does not cover:** simple balance, quiet concealment, horseback technique

**Destreza** · Physical

- **Core domain:** fine motor precision and delicate bodily control
- **Covers:** small precise manipulations, technical hand use, delicate execution under pressure
- **Does not cover:** full-body acrobatics, stealth as concealment, broad athletic motion

**Equilibrio** · Physical

- **Core domain:** maintaining bodily stability and controlled footing
- **Covers:** unstable surfaces, narrow supports, resisting loss of balance, controlled stance
- **Does not cover:** emotional steadiness, silence, mounted control

**Equitación** · Physical

- **Core domain:** controlling and acting through a mount with trained bodily coordination
- **Covers:** mounted movement, mounted stability, mounted maneuvering, mounted combat positioning
- **Does not cover:** bond with animals as such, broad animal handling, leadership over companions

---

### Tenacity

**Attribute identity:** bodily endurance, sustained functioning, persistence through stress, survival of internal or external strain.

**Marcha** · Physical

- **Core domain:** sustained locomotion over time
- **Covers:** travel rhythm, prolonged movement, carrying oneself over distance, maintaining pace
- **Does not cover:** raw exertion bursts, climate adaptation, enduring severe pain or physiological shock

**Aclimatación** · Physical

- **Core domain:** adapting the body to hostile or extreme environments
- **Covers:** functioning in cold, heat, altitude, humidity, harsh atmosphere, sustained environmental adaptation
- **Does not cover:** travel pacing itself, raw exertion, pain endurance unrelated to environment

**Tolerancia** · Physical

- **Core domain:** enduring pain, internal strain, physiological punishment, and accumulated bodily aggravation
- **Covers:** enduring pain, resisting collapse, staying functional with physical afflictions, bearing multiple bodily burdens
- **Does not cover:** emotional breakdown, panic control, calm under social pressure

---

### Cunning

**Attribute identity:** opportunism, adaptive intelligence, quick inference, situational exploitation, indirect problem solving.

**Orientación** · Mental

- **Core domain:** understanding direction, position, and route structure
- **Covers:** navigation, route choice, avoiding becoming lost, spatial direction
- **Does not cover:** tracking traces, survival logistics, deep environmental interpretation

**Rastreo** · Mental

- **Core domain:** following traces, signs, and passage through the world
- **Covers:** footprints, trails, disturbance signs, movement history
- **Does not cover:** general route orientation, broad wilderness survival, pure intuition

**Intuición** · Mental

- **Core domain:** rapid inferential sense about hidden motives, danger, or unseen structure
- **Covers:** gut-level reading, indirect suspicion, sensing when something is wrong
- **Does not cover:** formal perception, academic interpretation, emotional empathy

**Engaño** · Social

- **Core domain:** misleading others through falsehood, omission, framing, or manipulation of appearances
- **Covers:** lying, bluffing, misdirection, false implication
- **Does not cover:** social blending, public performance, direct coercive pressure

**Improvisación** · Mental

- **Core domain:** solving immediate problems through adaptive invention
- **Covers:** quick solutions, makeshift method, opportunistic use of available means
- **Does not cover:** deep academic reasoning, craft mastery, stable planned procedure

**Hurto** · Social

- **Core domain:** acquiring objects or resources through stealth, misdirection, or opportunistic removal
- **Covers:** pickpocketing, light theft, unnoticed taking, opportunistic acquisition
- **Does not cover:** fine manual technique in general, broad stealth movement, forced seizure

---

### Wisdom

**Attribute identity:** attentive understanding of the real, practical judgment, field awareness, applied reading of life and environment.

**Percepción** · Mental

- **Core domain:** active noticing of meaningful details
- **Covers:** observing, detecting, recognizing relevant sensory input
- **Does not cover:** deep interpretation, tracking, intuitive suspicion

**Supervivencia** · Mental

- **Core domain:** practical living and decision-making in hostile or uncertain environments
- **Covers:** shelter choice, food/water judgment, hazard response, keeping people alive in the field
- **Does not cover:** precise tracking, navigation as a separate skill, medicine as treatment science

**Medicina** · Arts and Crafts

- **Core domain:** treating bodily harm through trained healing practice
- **Covers:** stabilization, care, treatment, diagnosis in a healing sense
- **Does not cover:** herb gathering itself, alchemical preparation, pure tolerance or endurance

**Herboristería** · Arts and Crafts

- **Core domain:** identifying, gathering, and using plants in a practical medicinal or material way
- **Covers:** herbs, roots, plant properties, plant preparation
- **Does not cover:** full medicine, full alchemy, broad wilderness survival

**Alquimia** · Arts and Crafts

- **Core domain:** preparing compounds through learned transformation of ingredients
- **Covers:** potions, toxins, extracts, reactive mixtures
- **Does not cover:** herb gathering by itself, healing treatment by itself, engineering devices

**Trampas** · Arts and Crafts

- **Core domain:** constructing, identifying, preparing, and handling trap systems
- **Covers:** trap logic, trap placement, trap maintenance, trap interaction
- **Does not cover:** general manual dexterity, broader engineering, simple object use

**Minería** · Arts and Crafts

- **Core domain:** extracting and understanding material from the earth in practical terms
- **Covers:** veins, excavation logic, practical extraction judgment
- **Does not cover:** geology as broad knowledge, smithing, architecture

**Herrería** · Arts and Crafts

- **Core domain:** shaping and working metal for practical function
- **Covers:** forging, repairing metal goods, practical metalwork
- **Does not cover:** jewelry detail work, architecture theory, general engineering logic

**Sastrería** · Arts and Crafts

- **Core domain:** making and repairing garments and flexible material wear
- **Covers:** sewing, fitting, textile work, garment function
- **Does not cover:** armor smithing, disguise performance, decorative jewelry work

**Joyería** · Arts and Crafts

- **Core domain:** fine material work in small precious or intricate crafted objects
- **Covers:** gems, delicate settings, small-value crafted pieces
- **Does not cover:** blacksmithing, broad engineering, textile work

**Note on artistic domains**

- Performative arts are not Presence specializations by default.
- Artistic domains belong inside **Arts and Crafts**. Typical examples include `Interpretation/Performance`, `Music`, `Dance`, `Juggling`, and `Puppetry`.

**Ingeniería** · Knowledge

- **Core domain:** structured design and practical logic of mechanisms, structures, or complex functional devices
- **Covers:** mechanisms, technical planning, structural design logic
- **Does not cover:** trap specialization in particular, smithing, architecture as cultural/building analysis

---

### Intellect

**Attribute identity:** formal understanding, learned systems, structured interpretation, memory and organized knowledge.

**Identificación** · Mental

- **Core domain:** recognizing what something is through informed analysis
- **Covers:** object recognition, creature type recognition, identifying known classes of things
- **Does not cover:** deeper meaning, symbolic interpretation, intuitive reading

**Interpretación** · Mental

- **Core domain:** extracting meaning from signs, context, patterns, or structures
- **Covers:** understanding significance, reading implications, connecting meaning
- **Does not cover:** raw noticing, gut instinct, language decoding by itself

**Lingüística** · Knowledge

- **Core domain:** language structure, use, decoding, and formal communication systems
- **Covers:** language analysis, scripts, grammar, linguistic interpretation
- **Does not cover:** social persuasion, performance, symbolic context beyond language itself

**Taumaturgia** · Knowledge

- **Core domain:** formal understanding of tauma and its laws, manifestations, and systems
- **Covers:** tauma theory, taumatic structure, arcane understanding
- **Does not cover:** raw aura resonance, broad theology, physical endurance of taumatic exposure

**Historia** · Knowledge

- **Core domain:** formal knowledge of past events, periods, peoples, and developments
- **Covers:** chronology, historical precedent, known past structures
- **Does not cover:** archaeology in the field, theology, geography

**Geografía** · Knowledge

- **Core domain:** formal understanding of regions, terrain, places, and their broader structure
- **Covers:** mapped regions, climate zones, land divisions, known place logic
- **Does not cover:** route navigation in practice, tracking, survival movement

**Astronomía** · Knowledge

- **Core domain:** formal understanding of stars, celestial bodies, cycles, and sky logic
- **Covers:** celestial reading, astronomical systems, sky-based interpretation
- **Does not cover:** religion, geography, omen-like instinct

**Teología** · Knowledge

- **Core domain:** formal understanding of gods, doctrine, sacred systems, and theological structures
- **Covers:** religious knowledge, doctrine, divine interpretation in structured form
- **Does not cover:** instinctive aura response, persuasion, general history

**Criptología** · Knowledge

- **Core domain:** encoded language, hidden structure, cipher logic
- **Covers:** codebreaking, cipher recognition, encrypted systems
- **Does not cover:** general language fluency, social deception, symbolism in broad cultural terms

**Arqueología** · Knowledge

- **Core domain:** formal understanding of ruins, material past, lost cultures, and physical remnants
- **Covers:** excavation interpretation, old remains, cultural remnants
- **Does not cover:** pure history as text, architecture as structure alone, geology or mining

**Arquitectura** · Knowledge

- **Core domain:** formal understanding of constructed spaces, structural form, and built environments
- **Covers:** buildings, layout logic, construction patterns, structural reading
- **Does not cover:** engineering mechanisms broadly, smithing, geography

**Belicología** · Knowledge

- **Core domain:** formal understanding of war, conflict systems, military doctrine, and combat organization
- **Covers:** battle structure, military logic, war patterns, conflict method
- **Does not cover:** leadership as social command, raw weapon use, direct tactical improvisation

---

### Composure

**Attribute identity:** inner regulation, maintained clarity, control under pressure, deliberate steadiness.

**Enfoque** · Mental

- **Core domain:** sustaining attention on a chosen target or task
- **Covers:** concentration, fixation, deliberate mental narrowing
- **Does not cover:** emotional containment, meditative reset, maintaining visible composure

**Contención** · Mental

- **Core domain:** keeping emotional, mental, or volitional breakdown from spilling outward
- **Covers:** not panicking, not breaking, not losing internal control
- **Does not cover:** bodily pain tolerance, broad concentration, socially projecting calm

**Meditación** · Mental

- **Core domain:** practiced inner regulation through deliberate centering and mental stilling
- **Covers:** centering, regulation, controlled breathing/settling, cultivated inward steadiness
- **Does not cover:** attention fixation alone, outward poise alone, pain endurance

**Aplomo** · Social

- **Core domain:** maintaining outward steadiness, poise, and visible control under strain
- **Covers:** not showing fear, not revealing pain, preserving bearing under pressure
- **Does not cover:** social deception in general, raw emotional suppression alone, internal meditative regulation

---

### Aura

**Attribute identity:** innate projection, instinctive resonance, involuntary presence of essence, felt connection.

**Instinto** · Mental

- **Core domain:** deep instinctive response tied to innate nature rather than learned inference
- **Covers:** primal knowing, natural pull, immediate non-rational response
- **Does not cover:** structured reasoning, formal perception, social empathy

**Resonancia** · Mental

- **Core domain:** sensing or entering meaningful harmony with beings, forces, places, or states
- **Covers:** affinity detection, sympathetic response, energetic or essential attunement
- **Does not cover:** formal tauma theory, theology, performance of presence

**Vínculo** · Social

- **Core domain:** sustaining a meaningful tie of essence, instinctive trust, or deep connection
- **Covers:** bonded relation, enduring spiritual or essential connection, non-verbal affinity
- **Does not cover:** leadership, negotiation, general social projection

**Domesticación** · Social

- **Core domain:** relating to beasts or instinct-driven creatures through trained handling rooted in aura and response
- **Covers:** taming, calming, bonding in practical terms, handling living instinctive beings
- **Does not cover:** mounted technique, general leadership, broad social persuasion

---

### Presence

**Attribute identity:** outward projection, influence, command of attention, performed or imposed selfhood.

**Liderazgo** · Social

- **Core domain:** directing others through authority, structure, and force of command
- **Covers:** guidance, command, rallying, directing coordinated action
- **Does not cover:** pure empathy, personal acting, hidden blending

**Negociación** · Social

- **Core domain:** shaping agreement through exchange, leverage, and controlled social balance
- **Covers:** bargaining, compromise, settlement, persuasive exchange
- **Does not cover:** intimidation, deception, performance identity

**Intimidación** · Social

- **Core domain:** imposing pressure through threat, force of presence, or fear
- **Covers:** coercive pressure, fear projection, domination through presence
- **Does not cover:** leadership structure, deceptive manipulation, calm blending

**Imitación** · Social

- **Core domain:** reproducing behavior, voice, manner, or social patterning
- **Covers:** mimicry, copying mannerisms, false behavioral reproduction
- **Does not cover:** full acting as expressive performance, concealment as stealth, raw deception as lying

**Sigilo** · Social

- **Core domain:** reducing how much attention and perceptual registration the character generates in a scene
- **Covers:** going unnoticed, minimizing visible or audible presence, slipping beneath active notice
- **Does not cover:** false identity, explicit lying, fine motor execution by itself

---

## Catalog Depth Requirement

The specialization catalog should not remain only a list of names and boundary notes.

Each specialization entry in the authority catalog should eventually carry enough detail to support:

- reader-facing prose in the corebook
- consistent Narrator adjudication
- clear differentiation from adjacent domains
- later Technique prerequisite writing

At minimum, each entry should define:

- short functional description
- full narrative / design description
- usage fantasy
- scope boundary
- taxonomic placement
- relationship to nearby domains
- criterion of use for the Narrator
- brief example situations

Technique lists may remain empty until the Techniques chapter exists, but the specialization should already be rich enough to stand on its own as a trainable domain.

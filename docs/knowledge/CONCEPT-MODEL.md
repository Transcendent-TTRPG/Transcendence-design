# Concept Model

## Purpose

This document defines the main concept families used across the design repository.

It exists to reduce ambiguity when creating new rules, techniques, ailments, states, and simulator objects.

## Major Concept Families

### Rules

Rules are canonical gameplay statements and system procedures.

They usually live in:

- `docs/system/`
- `data/system/`

### States

States are persistent or semi-persistent conditions that matter in resolution.

The project now recognizes that not all formal states belong to the same family.

Current broad state families:

- ailments
- concealment states
- procedural states

### Ailments

Ailments are harmful states that alter body function, perception, cognition, execution, or physiological operation.

Examples:

- `Aterrorizado`
- `Atrapado`
- `Conmocionado`
- `Lacerado`

### Concealment States

Concealment states alter how a creature is located, tracked, or perceived by other creatures.

They are relational, observer-sensitive, and governed by concealment rules rather than ailment rules.

Current canonical example:

- `Oculto`

### Procedural States

Procedural states capture narrower tactical or interaction conditions that should not become full ailments.

They often describe:

- marks
- spoil conditions
- read openings
- disrupted lines
- localized sensor interference

Examples already used in techniques include concepts like:

- `signal-blurred`
- `read-marked`
- `displaced`
- `step-checked`

### Actions

Actions are baseline system moves available through combat structure.

They provide the common floor of the game, not the ideal differentiated ceiling.

### Techniques

Techniques are authored moves that exceed or specialize beyond the common floor.

They should:

- justify their cost
- respect rule families they depend on
- inherit ailment behavior from canonical ailments instead of re-describing it

### Competencies

Competencies supply rank, rank bonus, and access.

They also influence:

- legality
- scaling
- resistance and recovery handling
- simulator profiles

## Important Boundaries

### Ailment vs Concealment State

If a condition primarily changes body or operational function, it belongs closer to ailments.

If it changes whether or how a creature is localized by others, it belongs closer to concealment.

### Ailment vs Procedural State

If a condition should persist because the target's operative state changed, it is a better ailment candidate.

If it only describes a narrow local interaction, tag, residue, spoil line, or temporary tactical relation, it is often procedural.

### Action vs Technique

If the effect is the ordinary floor of the system, it belongs to an action.

If the effect represents trained, costly, or unusually efficient execution, it belongs to a technique.

## Simulation Relevance

This concept model should directly inform simulator object design.

In particular:

- `Ailment` and `ConcealmentState` must remain distinct objects
- `Technique` should not duplicate ailment logic
- procedural states may need a lighter representation than ailments

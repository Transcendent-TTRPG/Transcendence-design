"""Damage-model definitions and runtime state."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class CreatureZoneDefinition:
    """One authored creature zone or breakable subsystem."""

    id: str
    max_hp: int
    block: int
    dr_bonus: int = 0
    durability: int = 0
    linked_abilities: tuple[str, ...] = ()
    vital: bool = False
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class DamageModelDefinition:
    """Authored damage model for one combatant profile."""

    kind: str = "player_wounds"
    creature_zones: tuple[CreatureZoneDefinition, ...] = ()
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class CreatureZoneState:
    """Runtime state for one creature part/zone under a creature damage model."""

    id: str
    max_hp: int
    current_hp: int
    block: int
    dr_bonus: int
    max_durability: int
    durability: int
    linked_abilities: tuple[str, ...] = ()
    vital: bool = False
    broken: bool = False
    disabled: bool = False
    notes: tuple[str, ...] = ()

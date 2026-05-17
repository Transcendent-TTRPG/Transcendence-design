"""Combatant profile definition models."""

from __future__ import annotations

from dataclasses import dataclass, field

from .damage_model import DamageModelDefinition
from .competency import CompetencyRating
from .equipment_state import ArmorZoneLoadout, ShieldLoadout, WeaponLoadout


@dataclass(frozen=True)
class CombatantProfileDefinition:
    """Simulation-ready combatant baseline or archetype."""

    id: str
    species: str
    preparation: int
    movement_meters: int
    damage_model: DamageModelDefinition = field(default_factory=DamageModelDefinition)
    characteristics: dict[str, int] = field(default_factory=dict)
    competencies: dict[str, CompetencyRating] = field(default_factory=dict)
    armor_zones: tuple[ArmorZoneLoadout, ...] = ()
    shield: ShieldLoadout | None = None
    weapons: tuple[WeaponLoadout, ...] = ()
    techniques: tuple[str, ...] = ()
    equipment: tuple[str, ...] = ()
    zones: tuple[str, ...] = ()
    policy_defaults: dict[str, str] = field(default_factory=dict)
    notes: tuple[str, ...] = ()

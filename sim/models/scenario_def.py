"""Scenario definition models."""

from __future__ import annotations

from dataclasses import dataclass, field

from .combatant import GridPosition


@dataclass(frozen=True)
class MapDefinition:
    """Basic map geometry for a scenario."""

    width_m: int
    height_m: int
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ScenarioActorSlot:
    """Placement and slot metadata for a scenario actor."""

    slot: str
    position: GridPosition
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ScenarioDefinition:
    """Reusable tactical setup definition."""

    id: str
    environment_id: str | None = None
    map: MapDefinition | None = None
    actor_slots: tuple[ScenarioActorSlot, ...] = ()
    conditions: tuple[str, ...] = ()
    observer_relations: tuple[str, ...] = ()
    roll_modifiers: dict[str, dict[str, int]] = field(default_factory=dict)
    notes: tuple[str, ...] = ()

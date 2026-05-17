"""Action definition models."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class RollDefinition:
    """Declarative roll description used by actions and techniques."""

    family: str
    competency: str | None = None
    opposed_by: str | None = None
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class EffectDefinition:
    """Declarative effect description."""

    id: str
    parameters: dict[str, object] = field(default_factory=dict)
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ActionDefinition:
    """Simulation-facing base action definition."""

    id: str
    name: str
    category: str
    rhythm: int
    attrition: int
    trigger_type: str
    roll: RollDefinition | None = None
    legal_when: tuple[str, ...] = ()
    effects: tuple[EffectDefinition, ...] = ()
    notes: tuple[str, ...] = ()

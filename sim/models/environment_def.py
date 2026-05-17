"""Environment definition models."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class EnvironmentDefinition:
    """Reusable environment assumptions for scenarios."""

    id: str
    description: str
    roll_modifiers: dict[str, int] = field(default_factory=dict)
    notes: tuple[str, ...] = ()

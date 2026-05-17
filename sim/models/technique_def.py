"""Technique definition models."""

from __future__ import annotations

from dataclasses import dataclass, field

from .action_def import EffectDefinition, RollDefinition


@dataclass(frozen=True)
class TechniqueRequirements:
    """Legality and access requirements for a technique."""

    competencies: tuple[str, ...] = ()
    states: tuple[str, ...] = ()
    equipment: tuple[str, ...] = ()
    tags: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class TechniqueDefinition:
    """Simulation-facing technique definition."""

    id: str
    name: str
    species: str | None
    category: str
    type: str
    origin: str
    rhythm: int
    attrition: int
    trigger: str
    roll: RollDefinition | None = None
    requirements: TechniqueRequirements = field(default_factory=TechniqueRequirements)
    effects: tuple[EffectDefinition, ...] = ()
    restrictions: tuple[str, ...] = ()
    duration_model: str | None = None
    scaling: dict[str, object] = field(default_factory=dict)
    notes: tuple[str, ...] = ()

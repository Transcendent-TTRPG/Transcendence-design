"""Question definition models."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ActorAssignment:
    """Mapping from scenario slot or role to a profile or entity id."""

    slot: str
    profile_id: str


@dataclass(frozen=True)
class QuestionDefinition:
    """One design question and its experiment framing."""

    id: str
    prompt: str
    scenario_id: str
    profile_id: str | None = None
    domains: tuple[str, ...] = ()
    actor_assignments: tuple[ActorAssignment, ...] = ()
    policy_assignments: dict[str, str] = field(default_factory=dict)
    metrics: tuple[str, ...] = ()
    iterations: int | None = None
    comparisons: dict[str, str] = field(default_factory=dict)
    notes: tuple[str, ...] = ()

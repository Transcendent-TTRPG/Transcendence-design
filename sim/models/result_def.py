"""Result definition models."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class RollOutcome:
    """One resolved roll event."""

    family: str
    actor_id: str
    source_id: str | None
    success: bool
    target_value: int | float | None = None
    rolled_value: int | float | None = None
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class AggregateMetric:
    """Aggregated metric entry for an experiment result."""

    id: str
    value: float
    unit: str | None = None
    notes: tuple[str, ...] = ()


@dataclass
class IterationResult:
    """One simulation iteration result."""

    iteration_index: int
    question_id: str
    scenario_id: str
    roll_log: list[RollOutcome] = field(default_factory=list)
    state_changes: list[str] = field(default_factory=list)
    metrics: dict[str, float] = field(default_factory=dict)
    notes: tuple[str, ...] = ()


@dataclass
class ExperimentResult:
    """Summary result for a complete experiment run."""

    question_id: str
    scenario_id: str
    iterations: int
    aggregates: list[AggregateMetric] = field(default_factory=list)
    comparisons: dict[str, float] = field(default_factory=dict)
    notes: tuple[str, ...] = ()

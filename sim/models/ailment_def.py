"""Ailment definition models."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class RecoveryDefinition:
    """Recovery route for an ailment."""

    type: str
    competency: str | None = None
    threshold_model: str | None = None
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class AilmentTimingDefinition:
    """Timing, reevaluation, and expiry semantics for one ailment."""

    activation_start: tuple[str, ...] = ()
    action_gate: tuple[str, ...] = ()
    reevaluation_points: tuple[str, ...] = ()
    expiry_mode: str | None = None
    fiction_release_events: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class NumericBurdenDefinition:
    """Numeric burden model for an ailment."""

    source: str
    applies_to: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class AilmentDefinition:
    """Simulation-facing ailment definition."""

    id: str
    family: str
    severity_model: str
    numeric_burden: NumericBurdenDefinition | None = None
    qualitative_burden: dict[str, tuple[str, ...]] = field(default_factory=dict)
    recovery: RecoveryDefinition | None = None
    timing: AilmentTimingDefinition | None = None
    persistence_rule: str | None = None
    application_notes: tuple[str, ...] = ()
    replacement_rules: tuple[str, ...] = ()

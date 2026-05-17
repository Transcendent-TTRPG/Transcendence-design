"""Concealment runtime models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ConcealmentState:
    """Observer-relative hidden relationship."""

    owner_id: str
    observer_id: str
    state_id: str = "hidden_state"
    active_value: int | float | None = None
    acquisition_source: str | None = None
    valid: bool = True
    break_conditions: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()

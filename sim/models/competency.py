"""Competency rating models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompetencyRating:
    """One competency's current level and rank for simulation purposes."""

    level: int = 0
    rank: str | None = None

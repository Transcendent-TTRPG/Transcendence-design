"""Outcome normalization and result packaging."""

from __future__ import annotations

from models import ExperimentResult


def empty_experiment_result(*, question_id: str, scenario_id: str) -> ExperimentResult:
    """Create an empty result shell for a question before execution fills it."""

    return ExperimentResult(
        question_id=question_id,
        scenario_id=scenario_id,
        iterations=0,
    )

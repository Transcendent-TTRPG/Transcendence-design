import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from experiments.monte_carlo import (
    run_hidden_crossing_experiment,
    run_hidden_crossing_iteration,
)


def test_hidden_crossing_iteration_produces_expected_metric_keys() -> None:
    result = run_hidden_crossing_iteration(seed=1)

    assert result.question_id == "hidden_gain_crossing_4m"
    assert set(result.metrics.keys()) == {"hidden_gain", "detection", "crossing_success"}
    assert len(result.roll_log) == 2


def test_hidden_crossing_experiment_aggregates_rates() -> None:
    result = run_hidden_crossing_experiment(iterations=10, base_seed=1)

    assert result.question_id == "hidden_gain_crossing_4m"
    assert result.iterations == 10
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {"hidden_gain_rate", "detection_rate", "crossing_success_rate"}

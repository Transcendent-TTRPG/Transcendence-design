"""Monte Carlo experiment runners."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

from engine.dice import (
    associated_characteristic,
    characteristic_value,
    resolve_opposed,
    specialization_roll,
)
from engine.entities import ExperimentContext
from engine.resolver import instantiate_question_context
from engine.rng import SimulationRNG
from models import AggregateMetric, ExperimentResult, IterationResult, RollOutcome


@dataclass(frozen=True)
class HiddenCrossingAggregate:
    """Aggregate metrics for the seed hidden-crossing experiment."""

    hidden_gain_rate: float
    detection_rate: float
    crossing_success_rate: float


@dataclass(frozen=True)
class HiddenCrossingRuntime:
    """Resolved static runtime data for the hidden crossing seed."""

    question_id: str
    scenario_id: str
    mover_id: str
    watcher_id: str
    mover_level: int
    mover_rank: str | None
    watcher_level: int
    watcher_rank: str | None
    mover_characteristic_modifier: int
    watcher_characteristic_modifier: int
    mover_scene_bonus: int
    mover_scene_penalty: int
    watcher_scene_bonus: int
    watcher_scene_penalty: int


def _combine_scene_modifiers(*modifiers: int) -> tuple[int, int]:
    """Combine scene modifiers with one positive bonus cap and stacked penalties."""

    positives = [value for value in modifiers if value > 0]
    negatives = [value for value in modifiers if value < 0]
    bonus = max(positives, default=0)
    penalty = abs(sum(negatives))
    return bonus, penalty


def _build_hidden_crossing_runtime(context: ExperimentContext) -> HiddenCrossingRuntime:
    """Compile static question/scenario data once for repeated Monte Carlo iteration."""

    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant

    mover_rating = mover.competencies.get("Sigilo")
    watcher_rating = watcher.competencies.get("Percepcion")
    mover_characteristic = associated_characteristic("Sigilo")
    watcher_characteristic = associated_characteristic("Percepcion")
    mover_characteristic_modifier = characteristic_value(mover.characteristics, mover_characteristic) if mover_characteristic else 0
    watcher_characteristic_modifier = characteristic_value(watcher.characteristics, watcher_characteristic) if watcher_characteristic else 0

    mover_environment_modifier = 0
    watcher_environment_modifier = 0
    if context.environment is not None:
        mover_environment_modifier += context.environment.roll_modifiers.get("Sigilo", 0)
        watcher_environment_modifier += context.environment.roll_modifiers.get("Percepcion", 0)
    mover_scenario_modifier = context.scenario.roll_modifiers.get("mover", {}).get("Sigilo", 0)
    watcher_scenario_modifier = context.scenario.roll_modifiers.get("watcher", {}).get("Percepcion", 0)
    mover_bonus, mover_penalty = _combine_scene_modifiers(mover_environment_modifier, mover_scenario_modifier)
    watcher_bonus, watcher_penalty = _combine_scene_modifiers(watcher_environment_modifier, watcher_scenario_modifier)

    return HiddenCrossingRuntime(
        question_id=context.question.id,
        scenario_id=context.scenario.id,
        mover_id=mover.id,
        watcher_id=watcher.id,
        mover_level=0 if mover_rating is None else mover_rating.level,
        mover_rank=None if mover_rating is None else mover_rating.rank,
        watcher_level=0 if watcher_rating is None else watcher_rating.level,
        watcher_rank=None if watcher_rating is None else watcher_rating.rank,
        mover_characteristic_modifier=mover_characteristic_modifier,
        watcher_characteristic_modifier=watcher_characteristic_modifier,
        mover_scene_bonus=mover_bonus,
        mover_scene_penalty=mover_penalty,
        watcher_scene_bonus=watcher_bonus,
        watcher_scene_penalty=watcher_penalty,
    )


@lru_cache(maxsize=1)
def _default_hidden_crossing_runtime() -> HiddenCrossingRuntime:
    """Return the default compiled runtime for the seed hidden crossing question."""

    context = instantiate_question_context("hidden_gain_crossing_4m")
    return _build_hidden_crossing_runtime(context)


def run_hidden_crossing_iteration(
    *,
    seed: int,
    runtime: HiddenCrossingRuntime | None = None,
) -> IterationResult:
    """Run one seed concealment iteration for the hidden crossing question."""

    runtime = runtime or _default_hidden_crossing_runtime()
    rng = SimulationRNG(seed=seed)

    mover_roll = specialization_roll(
        competency="Sigilo",
        level=runtime.mover_level,
        rank=runtime.mover_rank,
        rng=rng,
        characteristic_modifier=runtime.mover_characteristic_modifier,
        bonus_modifier=runtime.mover_scene_bonus,
        penalty_modifier=runtime.mover_scene_penalty,
    )
    watcher_roll = specialization_roll(
        competency="Percepcion",
        level=runtime.watcher_level,
        rank=runtime.watcher_rank,
        rng=rng,
        characteristic_modifier=runtime.watcher_characteristic_modifier,
        bonus_modifier=runtime.watcher_scene_bonus,
        penalty_modifier=runtime.watcher_scene_penalty,
    )

    opposed = resolve_opposed(mover_roll, watcher_roll)
    hidden_gain = opposed.attacker_wins
    detection = not hidden_gain
    crossing_success = hidden_gain

    return IterationResult(
        iteration_index=seed,
        question_id=runtime.question_id,
        scenario_id=runtime.scenario_id,
        roll_log=[
            RollOutcome(
                family="specialization",
                actor_id=runtime.mover_id,
                source_id="Sigilo",
                success=hidden_gain,
                target_value=watcher_roll.total,
                rolled_value=mover_roll.total,
                notes=(
                    "watched_crossing_attempt",
                    f"margin:{opposed.margin}",
                    f"characteristic_modifier:{runtime.mover_characteristic_modifier}",
                    f"scene_bonus:{runtime.mover_scene_bonus}",
                    f"scene_penalty:{runtime.mover_scene_penalty}",
                ),
            ),
            RollOutcome(
                family="specialization",
                actor_id=runtime.watcher_id,
                source_id="Percepcion",
                success=detection,
                target_value=mover_roll.total,
                rolled_value=watcher_roll.total,
                notes=(
                    "opposed_detection_read",
                    f"characteristic_modifier:{runtime.watcher_characteristic_modifier}",
                    f"scene_bonus:{runtime.watcher_scene_bonus}",
                    f"scene_penalty:{runtime.watcher_scene_penalty}",
                ),
            ),
        ],
        state_changes=["grant_hidden_state" if hidden_gain else "clean_detection"],
        metrics={
            "hidden_gain": 1.0 if hidden_gain else 0.0,
            "detection": 1.0 if detection else 0.0,
            "crossing_success": 1.0 if crossing_success else 0.0,
        },
        notes=("seed_hidden_crossing_runner",),
    )


def run_hidden_crossing_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    """Run the seed Monte Carlo experiment for the watched hidden crossing question."""

    runtime = _default_hidden_crossing_runtime()
    results = [
        run_hidden_crossing_iteration(seed=base_seed + index, runtime=runtime)
        for index in range(iterations)
    ]

    hidden_gain_total = sum(result.metrics["hidden_gain"] for result in results)
    detection_total = sum(result.metrics["detection"] for result in results)
    crossing_success_total = sum(result.metrics["crossing_success"] for result in results)

    return ExperimentResult(
        question_id="hidden_gain_crossing_4m",
        scenario_id="hidden_crossing",
        iterations=iterations,
        aggregates=[
            AggregateMetric(id="hidden_gain_rate", value=hidden_gain_total / iterations),
            AggregateMetric(id="detection_rate", value=detection_total / iterations),
            AggregateMetric(id="crossing_success_rate", value=crossing_success_total / iterations),
        ],
        comparisons={},
        notes=("seed_concealment_monte_carlo_runner",),
    )

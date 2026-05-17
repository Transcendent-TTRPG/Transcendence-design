import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.resolver import instantiate_question_context
from experiments.atb_tempo import apply_tempo_step, initialize_context_timeline


def test_initialize_context_timeline_uses_slot_based_modifiers() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")

    snapshot = initialize_context_timeline(
        context,
        situational_modifiers_by_slot={
            "mover": 1,
            "watcher": -1,
        },
    )

    assert snapshot.positions["mover"] == 0
    assert snapshot.positions["watcher"] == 3
    assert snapshot.next_ready_actor_id == context.actors_by_slot["mover"].combatant.id


def test_apply_tempo_step_updates_initialized_actor() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    initialize_context_timeline(
        context,
        situational_modifiers_by_slot={
            "mover": 1,
            "watcher": -1,
        },
    )

    result = apply_tempo_step(
        context,
        acting_slot="mover",
        rhythm_cost=6,
        attrition_cost=1,
    )

    mover = context.actors_by_slot["mover"].combatant
    assert result.track_after == 6
    assert mover.timeline.track_position == 6
    assert mover.attrition_spent == 1

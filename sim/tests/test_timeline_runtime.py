import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.resolver import instantiate_question_context
from engine.timeline import initialize_timeline, mark_pending_activation, next_ready_combatant, spend_timeline_cost
from models import Combatant, GridPosition, TimelineState


def _dummy_combatant(*, actor_id: str, preparation: int) -> Combatant:
    return Combatant(
        id=actor_id,
        name=actor_id,
        side="actor",
        position=GridPosition(0, 0),
        preparation=preparation,
        timeline=TimelineState(preparation=preparation),
    )


def test_initialize_timeline_uses_preparation_and_situational_modifiers() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant

    result = initialize_timeline(
        combatants=(mover, watcher),
        situational_modifiers={
            mover.id: 1,
            watcher.id: -1,
        },
    )

    assert result.reference_point == 6
    assert mover.timeline.track_position == 0
    assert watcher.timeline.track_position == 3
    assert result.ordered_actor_ids == (mover.id, watcher.id)


def test_next_ready_combatant_uses_raw_preparation_as_tiebreak() -> None:
    fast = _dummy_combatant(actor_id="fast", preparation=5)
    slow = _dummy_combatant(actor_id="slow", preparation=4)

    initialize_timeline(
        combatants=(fast, slow),
        situational_modifiers={
            fast.id: -1,
            slow.id: 0,
        },
    )

    ready = next_ready_combatant((fast, slow))

    assert fast.timeline.track_position == 0
    assert slow.timeline.track_position == 0
    assert ready.id == "fast"


def test_spend_timeline_cost_advances_track_and_attrition_for_activation() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    initialize_timeline(
        combatants=(mover, watcher),
        situational_modifiers={mover.id: 1, watcher.id: -1},
    )

    result = spend_timeline_cost(
        combatant=mover,
        rhythm_cost=6,
        attrition_cost=1,
    )

    assert result.track_before == 0
    assert result.track_after == 6
    assert result.attrition_after == 1
    assert result.as_reaction is False
    assert mover.timeline.activations_taken == 1
    assert mover.timeline.reactions_taken == 0
    assert next_ready_combatant((mover, watcher)).id == watcher.id


def test_spend_timeline_cost_can_model_zero_rhythm_reaction() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    initialize_timeline(
        combatants=(mover, watcher),
        situational_modifiers={mover.id: 1, watcher.id: -1},
    )

    result = spend_timeline_cost(
        combatant=watcher,
        rhythm_cost=0,
        attrition_cost=2,
        as_reaction=True,
    )

    assert result.track_before == 3
    assert result.track_after == 3
    assert result.attrition_after == 2
    assert watcher.timeline.activations_taken == 0
    assert watcher.timeline.reactions_taken == 1


def test_mark_pending_activation_sets_ready_flag() -> None:
    combatant = _dummy_combatant(actor_id="actor", preparation=4)

    initialize_timeline(combatants=(combatant,))
    mark_pending_activation(combatant=combatant, pending=True)
    assert combatant.timeline.pending_activation is True

    mark_pending_activation(combatant=combatant, pending=False)
    assert combatant.timeline.pending_activation is False

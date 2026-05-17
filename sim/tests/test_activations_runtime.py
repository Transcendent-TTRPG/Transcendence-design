import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.activations import ActivationIntent, execute_activation_intent
from engine.resolver import instantiate_question_context
from engine.rng import SimulationRNG
from experiments.atb_tempo import initialize_context_timeline
from models import ActiveAilment, CompetencyRating


def _initialized_hidden_crossing_context():
    context = instantiate_question_context("hidden_gain_crossing_4m")
    initialize_context_timeline(
        context,
        situational_modifiers_by_slot={
            "mover": 1,
            "watcher": -1,
        },
    )
    return context


def test_hide_action_executes_inside_atb_and_advances_timeline() -> None:
    context = _initialized_hidden_crossing_context()

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="hide",
            observer_slot="watcher",
        ),
        rng=SimulationRNG(seed=11),
    )

    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    assert result.succeeded is True
    assert result.blocked_by_ailment is False
    assert result.timeline_result.track_after == 6
    assert mover.attrition_spent == 1
    assert mover.concealment_states[0].observer_id == watcher.id
    assert mover.timeline.activations_taken == 1


def test_attack_action_executes_exchange_inside_atb() -> None:
    context = _initialized_hidden_crossing_context()
    execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="hide",
            observer_slot="watcher",
        ),
        rng=SimulationRNG(seed=11),
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="watcher",
            mode="action",
            definition_id="attack_one_handed",
            target_slot="mover",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    watcher = context.actors_by_slot["watcher"].combatant
    assert result.succeeded is True
    assert result.exchange_result is not None
    assert result.exchange_result.defender_id == context.actors_by_slot["mover"].combatant.id
    assert result.timeline_result.track_after == 9
    assert watcher.attrition_spent == 1
    assert watcher.timeline.activations_taken == 1


def test_technique_can_apply_ailment_inside_atb_loop() -> None:
    context = _initialized_hidden_crossing_context()

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="reir_donde_mas_suena",
            target_slot="watcher",
        ),
        rng=SimulationRNG(seed=5),
    )

    watcher = context.actors_by_slot["watcher"].combatant
    assert result.succeeded is True
    assert result.effect_results
    assert watcher.ailments[0].ailment_id == "aterrorizado"
    assert watcher.ailments[0].severity == "moderate"


def test_aturdido_blocks_meaningful_action_and_spends_lost_activation_window() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    initialize_context_timeline(
        context,
        situational_modifiers_by_slot={
            "mover": -1,
            "watcher": 1,
        },
    )
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.ailments.append(
        ActiveAilment(
            ailment_id="aturdido",
            severity="minor",
            original_severity="minor",
            source_rank_bonus=1,
            active=True,
            threatened_next_activation=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="watcher",
            mode="action",
            definition_id="attack_one_handed",
            target_slot="mover",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.blocked_by_ailment is True
    assert result.timeline_result.track_after == 3
    assert watcher.timeline.activations_taken == 1


def test_recovery_activation_can_clear_ailment_inside_atb_loop() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.competencies["Contencion"] = CompetencyRating(level=8, rank="adept")
    mover.ailments.append(
        ActiveAilment(
            ailment_id="aterrorizado",
            severity="moderate",
            original_severity="moderate",
            source_rank_bonus=2,
            active=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="recovery",
            definition_id="recover",
            ailment_id="aterrorizado",
        ),
        rng=SimulationRNG(seed=2),
    )

    assert result.succeeded is True
    assert result.recovery_result is not None
    assert result.recovery_result.cleared is True
    assert result.timeline_result.track_after == 6
    assert mover.attrition_spent == 1
    assert mover.ailments == []


def test_recovery_activation_failure_still_spends_atb_costs() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.ailments.append(
        ActiveAilment(
            ailment_id="aterrorizado",
            severity="moderate",
            original_severity="moderate",
            source_rank_bonus=2,
            active=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="recovery",
            definition_id="recover",
            ailment_id="aterrorizado",
        ),
        rng=SimulationRNG(seed=2),
    )

    assert result.succeeded is False
    assert result.recovery_result is not None
    assert result.recovery_result.cleared is False
    assert result.timeline_result.track_after == 6
    assert mover.attrition_spent == 1
    assert mover.ailments[0].ailment_id == "aterrorizado"


def test_conmocionado_severe_aborts_first_focus_attempt_each_activation() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.ailments.append(
        ActiveAilment(
            ailment_id="conmocionado",
            severity="severe",
            original_severity="severe",
            source_rank_bonus=2,
            active=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="focus_task",
        ),
        rng=SimulationRNG(seed=4),
    )

    assert result.succeeded is False
    assert result.blocked_by_ailment is True
    assert result.timeline_result.track_after == 6
    assert mover.attrition_spent == 1
    assert result.notes == ("activation_aborted_by_ailment_gate",)


def test_aterrorizado_severe_aborts_first_feared_line_attempt_each_activation() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.ailments.append(
        ActiveAilment(
            ailment_id="aterrorizado",
            severity="severe",
            original_severity="severe",
            source_rank_bonus=2,
            active=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="attack_one_handed",
            target_slot="watcher",
            zone="torso",
            against_feared_line=True,
        ),
        rng=SimulationRNG(seed=7),
    )

    assert result.succeeded is False
    assert result.blocked_by_ailment is True
    assert result.exchange_result is None
    assert result.timeline_result.track_after == 6
    assert mover.attrition_spent == 1
    assert result.notes == ("activation_aborted_by_ailment_gate",)


def test_activation_end_can_clear_aterrorizado_when_fiction_event_changes_line() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.ailments.append(
        ActiveAilment(
            ailment_id="aterrorizado",
            severity="moderate",
            original_severity="moderate",
            source_rank_bonus=2,
            active=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="focus_task",
            fiction_events=("feared_line_changed",),
        ),
        rng=SimulationRNG(seed=4),
    )

    assert result.succeeded is True
    assert "ailment_expired_on_fiction_change" in result.notes
    assert mover.ailments == []

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.policy_loop import run_policy_step
from engine.resolver import instantiate_question_context
from engine.rng import SimulationRNG
from experiments.atb_tempo import initialize_context_timeline


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


def test_policy_step_uses_stealth_crosser_for_ready_mover() -> None:
    context = _initialized_hidden_crossing_context()

    result = run_policy_step(
        context=context,
        rng=SimulationRNG(seed=11),
    )

    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    assert result.ready_actor_slot == "mover"
    assert result.execution.definition_id == "pasar_como_parte_del_fondo"
    assert result.execution.mode == "technique"
    assert mover.concealment_states[0].observer_id == watcher.id


def test_policy_loop_advances_until_conservative_watcher_gets_a_ready_window() -> None:
    context = _initialized_hidden_crossing_context()

    run_policy_step(
        context=context,
        rng=SimulationRNG(seed=11),
    )
    second = run_policy_step(
        context=context,
        rng=SimulationRNG(seed=7),
    )
    third = run_policy_step(
        context=context,
        rng=SimulationRNG(seed=9),
    )

    assert second.ready_actor_slot == "mover"
    assert second.execution.definition_id == "reir_donde_mas_suena"
    assert second.execution.mode == "technique"
    assert third.ready_actor_slot == "watcher"
    assert third.execution.definition_id == "aterrorizado"
    assert third.execution.mode == "recovery"

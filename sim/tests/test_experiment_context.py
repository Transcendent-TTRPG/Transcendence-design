import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.entities import build_experiment_context
from engine.resolver import instantiate_question_context, load_simulation_inputs


def test_loaded_simulation_inputs_include_seed_ids() -> None:
    inputs = load_simulation_inputs()

    assert "zarnag_novice_skirmisher" in inputs.profiles_by_id
    assert "hidden_crossing" in inputs.scenarios_by_id
    assert "hidden_gain_crossing_4m" in inputs.questions_by_id


def test_instantiate_question_context_builds_runtime_actors() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")

    assert context.question.id == "hidden_gain_crossing_4m"
    assert context.scenario.id == "hidden_crossing"
    assert len(context.actors) == 2
    assert set(context.actors_by_slot.keys()) == {"mover", "watcher"}

    mover = context.actors_by_slot["mover"]
    watcher = context.actors_by_slot["watcher"]
    assert mover.combatant.profile_id == "zarnag_novice_skirmisher"
    assert watcher.combatant.profile_id == "common_guard_observer"
    assert mover.combatant.position.x == 1
    assert watcher.combatant.position.x == 7
    assert context.environment is not None
    assert context.environment.id == "smoke_crossing"


def test_build_experiment_context_uses_question_policies_when_present() -> None:
    inputs = load_simulation_inputs()
    question = inputs.questions_by_id["hidden_gain_crossing_4m"]
    scenario = inputs.scenarios_by_id["hidden_crossing"]
    context = build_experiment_context(
        question=question,
        scenario=scenario,
        environment=inputs.environments_by_id.get(scenario.environment_id),
        profiles_by_id=inputs.profiles_by_id,
    )

    assert context.actors_by_slot["mover"].policy_id == "stealth_crosser"
    assert context.actors_by_slot["watcher"].policy_id == "conservative"

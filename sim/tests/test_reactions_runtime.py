import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.activations import ActivationIntent, execute_activation_intent
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


def test_conservative_defender_uses_brace_for_impact_reaction() -> None:
    context = _initialized_hidden_crossing_context()

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="attack_one_handed",
            target_slot="watcher",
            zone="torso",
        ),
        rng=SimulationRNG(seed=7),
    )

    watcher = context.actors_by_slot["watcher"].combatant
    assert result.reaction_results
    reaction = result.reaction_results[0]
    assert reaction.definition_id == "brace_for_impact"
    assert reaction.applied is True
    assert reaction.defense_bonus == 2
    assert watcher.timeline.reactions_taken == 1
    assert watcher.attrition_spent == 2

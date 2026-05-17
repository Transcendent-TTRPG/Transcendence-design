import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from experiments.atb_tempo import initialize_context_timeline
from engine.resolver import instantiate_question_context
from models import ActiveAilment, CompetencyRating, ConcealmentState
from policies import AttackReactionQuery, get_policy


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


def test_tempo_first_prefers_recovery_under_severe_recoverable_pressure() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.competencies["Contencion"] = CompetencyRating(level=8, rank="adept")
    mover.ailments.append(
        ActiveAilment(
            ailment_id="aterrorizado",
            severity="severe",
            original_severity="severe",
            source_rank_bonus=2,
            active=True,
        )
    )

    policy = get_policy("tempo_first")
    intent = policy.choose_activation_intent(context=context, actor_slot="mover")

    assert intent.mode == "recovery"
    assert intent.ailment_id == "aterrorizado"


def test_stealth_crosser_upgrades_from_hidden_to_fear_technique_before_attack() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    mover.concealment_states.append(
        ConcealmentState(
            owner_id=mover.id,
            observer_id=watcher.id,
            state_id="hidden_state",
            active_value=12,
            acquisition_source="seed",
            valid=True,
        )
    )

    policy = get_policy("stealth_crosser")
    intent = policy.choose_activation_intent(context=context, actor_slot="mover")

    assert intent.mode == "technique"
    assert intent.definition_id == "reir_donde_mas_suena"
    assert intent.target_slot == "watcher"


def test_conservative_declines_reaction_when_attrition_is_already_high() -> None:
    context = _initialized_hidden_crossing_context()
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.attrition_spent = 4

    policy = get_policy("conservative")
    intent = policy.choose_attack_reaction(
        context=context,
        query=AttackReactionQuery(
            defender_slot="watcher",
            attacker_slot="mover",
            zone="torso",
        ),
    )

    assert intent is None

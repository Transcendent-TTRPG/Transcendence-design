import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.resistance import build_resistance_context, resistance_roll_for_family
from engine.resolver import instantiate_question_context
from engine.rng import SimulationRNG


def test_build_resistance_context_uses_tenacity_for_infection() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant

    resistance_context = build_resistance_context(combatant=mover, family="infection")

    assert resistance_context.family == "infection"
    assert resistance_context.base_characteristic == "Tenacity"
    assert resistance_context.characteristic_modifier == 1
    assert resistance_context.resistance_level == 1
    assert resistance_context.resistance_rank == "novice"


def test_build_resistance_context_uses_resilience_for_alteration() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant

    resistance_context = build_resistance_context(combatant=mover, family="alteration")

    assert resistance_context.base_characteristic == "Resilience"
    assert resistance_context.characteristic_modifier == 1
    assert resistance_context.resistance_level == 1
    assert resistance_context.resistance_rank == "novice"


def test_resistance_roll_for_family_uses_canonical_rr_structure() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant

    roll = resistance_roll_for_family(
        combatant=mover,
        family="infection",
        rng=SimulationRNG(seed=11),
        bonus_modifier=1,
        penalty_modifier=1,
    )

    assert roll.family == "resistance"
    assert roll.competency == "infection"
    assert roll.level == 1
    assert roll.rank == "novice"
    assert roll.modifier == 3

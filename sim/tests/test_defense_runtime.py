import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.defense import build_defense_context, defense_roll_for_zone, shield_defense_bonus
from engine.resolver import instantiate_question_context
from engine.rng import SimulationRNG


def test_shield_defense_bonus_follows_canonical_type_rules() -> None:
    assert shield_defense_bonus("light", 1) == 1
    assert shield_defense_bonus("medium", 2) == 2
    assert shield_defense_bonus("heavy", 2) == 3


def test_build_defense_context_uses_zone_armor_and_shield() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    watcher = context.actors_by_slot["watcher"].combatant

    defense_context = build_defense_context(combatant=watcher, zone="torso")

    assert defense_context.armor_type == "medium"
    assert defense_context.applicable_evasion == 2
    assert defense_context.applicable_agility == 1
    assert defense_context.shield_bonus == 1
    assert defense_context.bonus_modifier == 1


def test_defense_roll_for_zone_resolves_zone_aware_dr() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant

    roll = defense_roll_for_zone(combatant=mover, zone="torso", rng=SimulationRNG(seed=11))

    assert roll.family == "defense"
    assert roll.competency == "Evasion"
    assert roll.modifier == 3

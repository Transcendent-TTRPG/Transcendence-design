import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.dice import (
    applicable_defense_values,
    attack_roll,
    associated_characteristic,
    canonical_characteristic_name,
    characteristic_roll,
    characteristic_value,
    difficulty_target,
    rank_bonus,
    resistance_characteristic,
    resolve_opposed,
    resolve_threshold,
    specialization_roll,
    untrained_specialization_roll,
)
from engine.rng import SimulationRNG


def test_rank_bonus_uses_canonical_rank_numbers() -> None:
    assert rank_bonus("untrained") == 0
    assert rank_bonus("novice") == 1
    assert rank_bonus("adept") == 2


def test_specialization_roll_is_repeatable_with_seed() -> None:
    roll_a = specialization_roll(competency="Sigilo", level=1, rank="novice", rng=SimulationRNG(seed=11))
    roll_b = specialization_roll(competency="Sigilo", level=1, rank="novice", rng=SimulationRNG(seed=11))

    assert roll_a.total == roll_b.total
    assert roll_a.modifier == 2


def test_specialization_roll_uses_characteristic_level_rank_bonus_and_penalty() -> None:
    roll = specialization_roll(
        competency="Sigilo",
        level=3,
        rank="adept",
        rng=SimulationRNG(seed=11),
        characteristic_modifier=2,
        bonus_modifier=1,
        penalty_modifier=2,
    )

    assert roll.modifier == 6


def test_difficulty_target_uses_canonical_base_plus_reference_level() -> None:
    assert difficulty_target("fundamental", reference_level=0) == 5
    assert difficulty_target("challenging", reference_level=2) == 10


def test_characteristic_roll_adds_reference_level_to_modifier() -> None:
    roll = characteristic_roll(
        characteristic="Agility",
        rng=SimulationRNG(seed=3),
        characteristic_modifier=2,
        reference_level=1,
    )

    assert roll.family == "characteristic"
    assert roll.modifier == 3


def test_associated_characteristic_reads_canonical_specialization_mapping() -> None:
    assert associated_characteristic("Sigilo") == "Presencia"
    assert associated_characteristic("Percepcion") == "Sabiduría"


def test_canonical_characteristic_name_supports_spanish_english_and_ids() -> None:
    assert canonical_characteristic_name("Presencia") == "Presence"
    assert canonical_characteristic_name("Wisdom") == "Wisdom"
    assert canonical_characteristic_name("CMP") == "Composure"


def test_characteristic_value_resolves_direct_and_derived_values() -> None:
    characteristics = {
        "Tenacidad": 2,
        "Sabiduría": 1,
        "Compostura": 3,
        "Presencia": 2,
    }

    assert characteristic_value(characteristics, "Presencia") == 2
    assert characteristic_value(characteristics, "Presence") == 2
    assert characteristic_value(characteristics, "Resilience") == 2


def test_resistance_characteristic_uses_canonical_effect_family_mapping() -> None:
    assert resistance_characteristic("poison") == "Tenacity"
    assert resistance_characteristic("infection") == "Tenacity"
    assert resistance_characteristic("affliction") == "Composure"
    assert resistance_characteristic("curses") == "Composure"
    assert resistance_characteristic("alteration") == "Resilience"


def test_attack_roll_uses_same_trained_roll_structure() -> None:
    roll = attack_roll(
        competency="Dagger",
        level=3,
        rank="adept",
        rng=SimulationRNG(seed=11),
        characteristic_modifier=2,
        bonus_modifier=1,
        penalty_modifier=2,
    )

    assert roll.family == "attack"
    assert roll.modifier == 6


def test_untrained_specialization_roll_uses_only_characteristic_and_scene_modifiers() -> None:
    roll = untrained_specialization_roll(
        competency="Sigilo",
        rng=SimulationRNG(seed=11),
        characteristic_modifier=2,
        bonus_modifier=1,
        penalty_modifier=1,
    )

    assert roll.family == "specialization"
    assert roll.level == 0
    assert roll.rank == "untrained"
    assert roll.modifier == 2


def test_applicable_defense_values_follow_armor_rules() -> None:
    assert applicable_defense_values(armor_type="light", evasion_level=3, evasion_rank="novice", agility_modifier=4) == (4, 4)
    assert applicable_defense_values(armor_type="medium", evasion_level=3, evasion_rank="novice", agility_modifier=3) == (4, 2)
    assert applicable_defense_values(armor_type="heavy", evasion_level=3, evasion_rank="novice", agility_modifier=3) == (2, 0)


def test_resolve_opposed_returns_margin_and_winner() -> None:
    attacker = specialization_roll(competency="Sigilo", level=0, rank="adept", rng=SimulationRNG(seed=5))
    defender = specialization_roll(competency="Percepcion", level=1, rank="novice", rng=SimulationRNG(seed=5))
    outcome = resolve_opposed(attacker, defender)

    assert outcome.attacker.total == attacker.total
    assert outcome.defender.total == defender.total
    assert outcome.margin == attacker.total - defender.total


def test_resolve_threshold_compares_roll_against_canonical_target() -> None:
    roll = specialization_roll(competency="Sigilo", level=1, rank="novice", rng=SimulationRNG(seed=7))
    outcome = resolve_threshold(roll, threshold_id="fundamental", reference_level=0)

    assert outcome.target == 5
    assert outcome.margin == roll.total - 5

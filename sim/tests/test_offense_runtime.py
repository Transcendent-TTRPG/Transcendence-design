import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.offense import attack_roll_for_weapon, build_offense_context, impact_roll_for_weapon
from engine.resolver import instantiate_question_context
from engine.rng import SimulationRNG
from engine.weapons import get_weapon_definition


def test_weapon_catalog_reads_seed_weapon_data() -> None:
    weapon = get_weapon_definition("kris")

    assert weapon.weapon_type == "Dagger"
    assert weapon.damage_die == "d4"
    assert weapon.characteristic == "Cunning"


def test_build_offense_context_uses_weapon_characteristic_and_competency() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant

    offense_context = build_offense_context(combatant=mover, slot="primary")

    assert offense_context.weapon_id == "kris"
    assert offense_context.competency == "Dagger"
    assert offense_context.weapon.characteristic == "Cunning"
    assert offense_context.characteristic_modifier == 1
    assert offense_context.competency_level == 3
    assert offense_context.competency_rank == "adept"
    assert offense_context.weapon_grade == 1
    assert offense_context.base_potency == 8


def test_attack_roll_for_weapon_uses_canonical_ar_structure() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant

    roll = attack_roll_for_weapon(
        combatant=mover,
        rng=SimulationRNG(seed=11),
        slot="primary",
        bonus_modifier=1,
        penalty_modifier=1,
    )

    assert roll.family == "attack"
    assert roll.competency == "Dagger"
    assert roll.level == 3
    assert roll.rank == "adept"
    assert roll.modifier == 6


def test_impact_roll_for_weapon_uses_rank_number_damage_and_grade() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant

    impact = impact_roll_for_weapon(combatant=mover, rng=SimulationRNG(seed=11), slot="primary")

    assert impact.weapon_die == "d4"
    assert impact.rank_number == 2
    assert impact.characteristic_modifier == 1
    assert impact.weapon_grade == 1
    assert len(impact.rolls) == 2
    assert impact.total == sum(impact.rolls) + 1
    assert impact.critical_roll == impact.rolls[0]
    assert impact.critical_face == 4
    assert impact.critical_impact is (impact.critical_roll == 4)
    assert impact.untrained is False

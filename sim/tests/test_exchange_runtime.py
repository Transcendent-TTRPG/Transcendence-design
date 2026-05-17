import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.block import zone_block_for_combatant
from engine.exchange import resolve_weapon_exchange
from engine.resolver import instantiate_question_context
from engine.rng import SimulationRNG


def test_zone_block_uses_armor_base_competency_level_and_grade() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant

    mover_block = zone_block_for_combatant(combatant=mover, zone="torso")
    watcher_block = zone_block_for_combatant(combatant=watcher, zone="torso")

    assert mover_block.armor_type == "light"
    assert mover_block.total_block == 4
    assert watcher_block.armor_type == "medium"
    assert watcher_block.total_block == 6


def test_exchange_returns_no_impact_when_defense_holds() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    attacker = context.actors_by_slot["watcher"].combatant
    defender = context.actors_by_slot["mover"].combatant

    result = resolve_weapon_exchange(
        attacker=attacker,
        defender=defender,
        zone="torso",
        rng=SimulationRNG(seed=11),
    )

    assert result.attack_connected is False
    assert result.impact_roll is None
    assert result.effective_damage == 0


def test_exchange_applies_impact_and_block_when_attack_connects() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    attacker = context.actors_by_slot["mover"].combatant
    defender = context.actors_by_slot["watcher"].combatant

    result = resolve_weapon_exchange(
        attacker=attacker,
        defender=defender,
        zone="torso",
        rng=SimulationRNG(seed=11),
    )

    assert result.attack_connected is True
    assert result.impact_roll is not None
    assert result.block_context.total_block == 6
    assert result.effective_damage == max(0, result.impact_roll.total - result.block_context.total_block)

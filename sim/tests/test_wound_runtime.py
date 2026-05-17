import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.exchange import resolve_weapon_exchange
from engine.resolver import instantiate_question_context
from engine.rng import SimulationRNG
from engine.wounds import apply_exchange_wound, wound_band_from_impact


def test_wound_band_uses_canonical_impact_vs_block_thresholds() -> None:
    assert wound_band_from_impact(impact=4, block=4).severity == "none"
    assert wound_band_from_impact(impact=5, block=4).severity == "light"
    assert wound_band_from_impact(impact=8, block=4).severity == "grave"
    assert wound_band_from_impact(impact=12, block=4).severity == "critical"


def test_wound_band_uses_minimum_threshold_for_unarmored_zone() -> None:
    assert wound_band_from_impact(impact=1, block=0).severity == "none"
    assert wound_band_from_impact(impact=2, block=0).severity == "grave"


def test_apply_exchange_wound_marks_slots_on_connected_hit() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    attacker = context.actors_by_slot["mover"].combatant
    defender = context.actors_by_slot["watcher"].combatant
    exchange = resolve_weapon_exchange(
        attacker=attacker,
        defender=defender,
        zone="torso",
        rng=SimulationRNG(seed=11),
    )

    wound = apply_exchange_wound(defender=defender, exchange=exchange)

    assert wound.severity == "light"
    assert wound.slots_applied == 1
    assert wound.overflow_slots == 0
    assert wound.occupied_after == 1
    assert wound.collapsed is False


def test_apply_exchange_wound_collapses_saturated_vital_zone_on_overflow() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    defender = context.actors_by_slot["watcher"].combatant
    for index, zone_state in enumerate(defender.zones):
        if zone_state.id == "head":
            defender.zones[index] = type(zone_state)(
                id=zone_state.id,
                capacity=zone_state.capacity,
                occupied_slots=zone_state.capacity,
                operational=True,
                saturated=True,
                collapsed=False,
                tags=zone_state.tags,
                notes=zone_state.notes,
            )
            break

    attacker = context.actors_by_slot["mover"].combatant
    exchange = resolve_weapon_exchange(
        attacker=attacker,
        defender=defender,
        zone="head",
        rng=SimulationRNG(seed=11),
        attack_bonus=3,
    )

    wound = apply_exchange_wound(defender=defender, exchange=exchange)

    assert wound.severity in {"light", "grave", "critical"}
    assert wound.collapsed is True
    assert wound.vital_collapse_rr_required is True

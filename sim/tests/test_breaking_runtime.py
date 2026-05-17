import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.block import zone_block_for_combatant
from engine.breaking import attempt_creature_zone_break, critical_potency_for_exchange
from engine.creature_parts import creature_supports_ability
from engine.defense import build_defense_context
from engine.dice import OpposedOutcome, RollValue
from engine.entities import instantiate_combatant
from engine.exchange import ExchangeResult
from engine.offense import ImpactRollValue, build_offense_context
from loaders.framing import load_species_profile_definitions
from models import ScenarioDefinition


def _instantiate_profile(profile_id: str):
    profiles = {profile.id: profile for profile in load_species_profile_definitions()}
    profile = profiles[profile_id]
    return instantiate_combatant(
        slot="actor",
        profile=profile,
        scenario=ScenarioDefinition(id="unit_test"),
        side="actor",
    ).combatant


def _exchange_against_wolf(*, zone: str, critical_impact: bool) -> tuple[object, object]:
    attacker = _instantiate_profile("zarnag_novice_skirmisher")
    defender = _instantiate_profile("ice_wolf_elder")
    attacker_roll = RollValue(raw=8, modifier=6, total=14, family="attack", competency="Dagger", level=3, rank="adept")
    defender_roll = RollValue(raw=4, modifier=5, total=9, family="defense", competency="Evasion", level=1, rank="novice")
    impact_roll = ImpactRollValue(
        rolls=(4, 2),
        weapon_die="d4",
        rank_number=2,
        characteristic_modifier=1,
        weapon_grade=1,
        total=7,
        critical_roll=4 if critical_impact else 3,
        critical_face=4,
        critical_impact=critical_impact,
        untrained=False,
    )
    exchange = ExchangeResult(
        attacker_id=attacker.id,
        defender_id=defender.id,
        zone=zone,
        offense_context=build_offense_context(combatant=attacker),
        defense_context=build_defense_context(combatant=defender, zone=zone),
        block_context=zone_block_for_combatant(combatant=defender, zone=zone),
        attack_roll=attacker_roll,
        defense_roll=defender_roll,
        opposed=OpposedOutcome(attacker=attacker_roll, defender=defender_roll, attacker_wins=True, margin=5),
        impact_roll=impact_roll,
        attack_connected=True,
        effective_damage=3,
    )
    return defender, exchange


def test_critical_potency_uses_base_potency_and_weapon_multiplier() -> None:
    defender, exchange = _exchange_against_wolf(zone="jaw", critical_impact=True)

    assert defender.id
    assert critical_potency_for_exchange(exchange) == 4


def test_break_attempt_breaks_zone_when_potency_meets_durability() -> None:
    defender, exchange = _exchange_against_wolf(zone="jaw", critical_impact=True)

    result = attempt_creature_zone_break(defender=defender, exchange=exchange)

    assert result.allowed is True
    assert result.critical_available is True
    assert result.critical_potency == 4
    assert result.durability_before == 4
    assert result.durability_after == 0
    assert result.broke is True
    assert result.disabled is True
    assert "frost_breath" in result.disabled_abilities
    assert creature_supports_ability(defender, "frost_breath") is False


def test_break_attempt_degrades_durability_when_potency_is_too_low() -> None:
    defender, exchange = _exchange_against_wolf(zone="torso", critical_impact=True)

    result = attempt_creature_zone_break(defender=defender, exchange=exchange)

    assert result.allowed is True
    assert result.broke is False
    assert result.durability_before == 5
    assert result.durability_after == 4
    assert result.disabled is False


def test_break_attempt_requires_critical_unless_explicitly_allowed() -> None:
    defender, exchange = _exchange_against_wolf(zone="jaw", critical_impact=False)

    result = attempt_creature_zone_break(defender=defender, exchange=exchange)

    assert result.attempted is False
    assert result.allowed is False
    assert result.critical_available is False
    assert result.durability_before == 4
    assert result.durability_after == 4


def test_break_attempt_can_be_allowed_without_critical_by_specific_rule() -> None:
    defender, exchange = _exchange_against_wolf(zone="jaw", critical_impact=False)

    result = attempt_creature_zone_break(
        defender=defender,
        exchange=exchange,
        allow_without_critical=True,
    )

    assert result.attempted is True
    assert result.allowed is True
    assert result.critical_required is False
    assert result.broke is True

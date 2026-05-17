import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.block import zone_block_for_combatant
from engine.creature_damage import apply_exchange_to_creature_zone
from engine.creature_parts import creature_supports_ability
from engine.defense import build_defense_context
from engine.exchange import ExchangeResult
from engine.offense import build_offense_context
from engine.entities import instantiate_combatant
from engine.dice import OpposedOutcome, RollValue
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


def _forced_exchange(*, attacker_id: str, defender_id: str, zone: str, effective_damage: int) -> ExchangeResult:
    attacker_roll = RollValue(raw=8, modifier=4, total=12, family="attack", competency="Dagger", level=3, rank="adept")
    defender_roll = RollValue(raw=4, modifier=3, total=7, family="defense", competency="Evasion", level=1, rank="novice")
    return ExchangeResult(
        attacker_id=attacker_id,
        defender_id=defender_id,
        zone=zone,
        offense_context=build_offense_context(combatant=_instantiate_profile("zarnag_novice_skirmisher")),
        defense_context=build_defense_context(combatant=_instantiate_profile("ice_wolf_elder"), zone=zone),
        block_context=zone_block_for_combatant(combatant=_instantiate_profile("ice_wolf_elder"), zone=zone),
        attack_roll=attacker_roll,
        defense_roll=defender_roll,
        opposed=OpposedOutcome(attacker=attacker_roll, defender=defender_roll, attacker_wins=True, margin=5),
        impact_roll=None,
        attack_connected=True,
        effective_damage=effective_damage,
    )


def test_creature_zone_defense_uses_zone_dr_bonus() -> None:
    creature = _instantiate_profile("ice_wolf_elder")

    jaw = build_defense_context(combatant=creature, zone="jaw")
    torso = build_defense_context(combatant=creature, zone="torso")

    assert jaw.armor_type == "creature_zone"
    assert jaw.applicable_evasion == 2
    assert jaw.applicable_agility == 2
    assert jaw.bonus_modifier == 1
    assert torso.bonus_modifier == 2


def test_creature_zone_block_uses_authored_zone_block() -> None:
    creature = _instantiate_profile("ice_wolf_elder")

    jaw = zone_block_for_combatant(combatant=creature, zone="jaw")
    torso = zone_block_for_combatant(combatant=creature, zone="torso")

    assert jaw.armor_type == "creature_zone"
    assert jaw.total_block == 2
    assert torso.total_block == 4


def test_creature_zone_damage_disables_linked_abilities_when_zone_falls() -> None:
    creature = _instantiate_profile("ice_wolf_elder")
    exchange = _forced_exchange(
        attacker_id="actor:zarnag_novice_skirmisher",
        defender_id=creature.id,
        zone="jaw",
        effective_damage=8,
    )

    assert creature_supports_ability(creature, "frost_breath") is True

    resolution = apply_exchange_to_creature_zone(defender=creature, exchange=exchange)

    assert resolution.hp_before == 8
    assert resolution.hp_after == 0
    assert resolution.disabled is True
    assert resolution.broken is True
    assert "frost_breath" in resolution.disabled_abilities
    assert "bite" in resolution.disabled_abilities
    assert creature_supports_ability(creature, "frost_breath") is False


def test_creature_zone_damage_marks_vital_shutdown_when_vital_zone_falls() -> None:
    creature = _instantiate_profile("ice_wolf_elder")
    exchange = _forced_exchange(
        attacker_id="actor:zarnag_novice_skirmisher",
        defender_id=creature.id,
        zone="torso",
        effective_damage=14,
    )

    resolution = apply_exchange_to_creature_zone(defender=creature, exchange=exchange)

    assert resolution.hp_before == 14
    assert resolution.hp_after == 0
    assert resolution.vital_shutdown is True


def test_creature_zone_damage_noops_when_attack_does_not_connect() -> None:
    creature = _instantiate_profile("ice_wolf_elder")
    attacker_roll = RollValue(raw=2, modifier=1, total=3, family="attack")
    defender_roll = RollValue(raw=7, modifier=4, total=11, family="defense")
    exchange = ExchangeResult(
        attacker_id="actor:zarnag_novice_skirmisher",
        defender_id=creature.id,
        zone="jaw",
        offense_context=build_offense_context(combatant=_instantiate_profile("zarnag_novice_skirmisher")),
        defense_context=build_defense_context(combatant=creature, zone="jaw"),
        block_context=zone_block_for_combatant(combatant=creature, zone="jaw"),
        attack_roll=attacker_roll,
        defense_roll=defender_roll,
        opposed=OpposedOutcome(attacker=attacker_roll, defender=defender_roll, attacker_wins=False, margin=-8),
        impact_roll=None,
        attack_connected=False,
        effective_damage=0,
    )

    resolution = apply_exchange_to_creature_zone(defender=creature, exchange=exchange)

    assert resolution.hp_before == 8
    assert resolution.hp_after == 8
    assert resolution.disabled is False
    assert resolution.disabled_abilities == ()

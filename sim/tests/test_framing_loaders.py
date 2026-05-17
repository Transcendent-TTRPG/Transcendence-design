import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

SIM_ROOT = Path(__file__).resolve().parents[1]

from loaders.framing import (
    build_framing_load_context,
    load_question_definitions,
    load_scenario_definitions,
    load_species_profile_definitions,
)


def test_framing_context_uses_species_completion_bundle() -> None:
    context = build_framing_load_context()

    assert context.knowledge_bundle.profile.id == "species_completion_audit"


def test_species_profile_loader_reads_seed_profiles() -> None:
    profiles = load_species_profile_definitions()

    assert profiles
    ids = {profile.id for profile in profiles}
    assert "zarnag_novice_skirmisher" in ids
    assert "common_guard_observer" in ids
    zarnag = next(profile for profile in profiles if profile.id == "zarnag_novice_skirmisher")
    assert zarnag.damage_model.kind == "player_wounds"
    assert zarnag.characteristics["Presencia"] == 2
    assert zarnag.characteristics["Tenacidad"] == 1
    assert zarnag.competencies["infection"].rank == "novice"
    assert any(entry.zone == "torso" and entry.armor_type == "light" for entry in zarnag.armor_zones)
    assert any(entry.slot == "primary" and entry.weapon_id == "kris" for entry in zarnag.weapons)
    guard = next(profile for profile in profiles if profile.id == "common_guard_observer")
    assert guard.damage_model.kind == "player_wounds"
    assert guard.shield is not None
    assert guard.shield.shield_type == "medium"
    assert guard.shield.grade == 1
    assert any(entry.slot == "primary" and entry.weapon_id == "hasta" for entry in guard.weapons)

    wolf = next(profile for profile in profiles if profile.id == "ice_wolf_elder")
    assert wolf.damage_model.kind == "creature_zones"
    assert len(wolf.damage_model.creature_zones) == 5
    jaw = next(zone for zone in wolf.damage_model.creature_zones if zone.id == "jaw")
    assert "frost_breath" in jaw.linked_abilities


def test_scenario_loader_reads_hidden_crossing_seed() -> None:
    scenarios = load_scenario_definitions(path=SIM_ROOT / "scenarios" / "micro" / "hidden_crossing.yaml")

    assert len(scenarios) == 1
    scenario = scenarios[0]
    assert scenario.id == "hidden_crossing"
    assert scenario.environment_id == "smoke_crossing"
    assert scenario.map is not None
    assert scenario.map.width_m == 12
    assert len(scenario.actor_slots) == 2
    assert scenario.roll_modifiers == {}


def test_question_loader_reads_hidden_crossing_question_seed() -> None:
    questions = load_question_definitions(
        path=SIM_ROOT / "questions" / "concealment" / "hidden_gain_crossing_4m.yaml"
    )

    assert len(questions) == 1
    question = questions[0]
    assert question.id == "hidden_gain_crossing_4m"
    assert question.scenario_id == "hidden_crossing"
    assert question.profile_id == "concealment_rule_lookup"
    assert {assignment.slot for assignment in question.actor_assignments} == {"mover", "watcher"}

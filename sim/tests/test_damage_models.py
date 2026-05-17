import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.creature_parts import active_linked_abilities, creature_supports_ability
from engine.entities import instantiate_combatant
from loaders.framing import load_species_profile_definitions
from models import ScenarioDefinition


def test_player_profile_instantiates_wound_zones_by_default() -> None:
    profiles = {profile.id: profile for profile in load_species_profile_definitions()}
    profile = profiles["zarnag_novice_skirmisher"]

    combatant = instantiate_combatant(
        slot="actor",
        profile=profile,
        scenario=ScenarioDefinition(id="unit_test"),
        side="actor",
    ).combatant

    assert combatant.damage_model_kind == "player_wounds"
    assert len(combatant.zones) == 5
    assert combatant.creature_zones == []


def test_creature_profile_instantiates_creature_zones_and_linked_abilities() -> None:
    profiles = {profile.id: profile for profile in load_species_profile_definitions()}
    profile = profiles["ice_wolf_elder"]

    combatant = instantiate_combatant(
        slot="actor",
        profile=profile,
        scenario=ScenarioDefinition(id="unit_test"),
        side="actor",
    ).combatant

    assert combatant.damage_model_kind == "creature_zones"
    assert combatant.zones == []
    assert len(combatant.creature_zones) == 5
    assert creature_supports_ability(combatant, "frost_breath") is True
    assert "bite" in active_linked_abilities(combatant)

"""Weapon catalog helpers for simulator offense resolution."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class WeaponDefinition:
    """Minimal weapon definition required by simulator offense helpers."""

    id: str
    weapon_type: str
    damage_die: str
    characteristic: str
    assignment: str
    bonus_text: str | None = None


def _workspace_root() -> Path:
    return Path(__file__).resolve().parents[3]


@lru_cache(maxsize=1)
def load_weapon_catalog() -> dict[str, WeaponDefinition]:
    """Load a reduced weapon lookup from the authority combat equipment catalog."""

    path = _workspace_root() / "Transcendence-design" / "data" / "system" / "combat-equipment-catalog.yaml"
    with path.open("r", encoding="utf-8") as handle:
        data: dict[str, Any] = yaml.safe_load(handle)

    definitions: dict[str, WeaponDefinition] = {}
    for category_entries in data.get("weapons", {}).values():
        for weapon_id, weapon_data in dict(category_entries).items():
            definitions[str(weapon_id)] = WeaponDefinition(
                id=str(weapon_id),
                weapon_type=str(weapon_data["type"]),
                damage_die=str(weapon_data["damage"]),
                characteristic=str(weapon_data["characteristic"]),
                assignment=str(weapon_data["assignment"]),
                bonus_text=weapon_data.get("bonus"),
            )
    if "marking_dart_launcher" not in definitions:
        # The current authority catalog does not yet list the seed Naghii marker
        # launcher explicitly, but simulator projection profiles already use it.
        definitions["marking_dart_launcher"] = WeaponDefinition(
            id="marking_dart_launcher",
            weapon_type="Ranged",
            damage_die="d4",
            characteristic="Agility",
            assignment="Primary",
            bonus_text="seed_projection_marker_runtime_profile",
        )
    return definitions


def get_weapon_definition(weapon_id: str) -> WeaponDefinition:
    """Return the reduced simulator-facing weapon definition."""

    try:
        return load_weapon_catalog()[weapon_id]
    except KeyError as exc:
        raise KeyError(f"Unknown weapon id: {weapon_id}") from exc

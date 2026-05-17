"""Load simulation-facing species profiles, scenarios, and questions."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from knowledge_access import for_species_completion_audit
from models import (
    ActorAssignment,
    ArmorZoneLoadout,
    CombatantProfileDefinition,
    CompetencyRating,
    CreatureZoneDefinition,
    DamageModelDefinition,
    EnvironmentDefinition,
    GridPosition,
    MapDefinition,
    QuestionDefinition,
    ScenarioActorSlot,
    ScenarioDefinition,
    ShieldLoadout,
    WeaponLoadout,
)


@dataclass(frozen=True)
class FramingLoadContext:
    """Shared context for framing-layer loading."""

    knowledge_bundle: object
    sim_root: Path


def _sim_root() -> Path:
    return Path(__file__).resolve().parents[1]


def build_framing_load_context() -> FramingLoadContext:
    """Build default context for scenario/question/profile loading."""

    return FramingLoadContext(
        knowledge_bundle=for_species_completion_audit(),
        sim_root=_sim_root(),
    )


def _load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    if not isinstance(loaded, dict):
        raise ValueError(f"Expected mapping at top level of {path}")
    return loaded


def _as_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        raise ValueError(f"Expected list, got {type(value)!r}")
    return tuple(str(item) for item in value)


def _iter_yaml_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(path.rglob("*.yaml"))


def _parse_competencies(data: dict[str, Any]) -> dict[str, CompetencyRating]:
    parsed: dict[str, CompetencyRating] = {}
    for competency_id, value in data.items():
        if isinstance(value, str):
            parsed[str(competency_id)] = CompetencyRating(level=0, rank=str(value))
            continue
        if isinstance(value, dict):
            parsed[str(competency_id)] = CompetencyRating(
                level=int(value.get("level", 0)),
                rank=value.get("rank"),
            )
            continue
        raise ValueError(f"Unsupported competency payload for {competency_id!r}: {type(value)!r}")
    return parsed


def _parse_armor_zones(data: list[dict[str, Any]] | None) -> tuple[ArmorZoneLoadout, ...]:
    if data is None:
        return ()
    parsed: list[ArmorZoneLoadout] = []
    for entry in data:
        parsed.append(
            ArmorZoneLoadout(
                zone=str(entry["zone"]),
                armor_type=str(entry["armor_type"]),
                grade=int(entry.get("grade", 1)),
                material_bonus=int(entry.get("material_bonus", 0)),
                notes=_as_tuple(entry.get("notes")),
            )
        )
    return tuple(parsed)


def _parse_shield(data: dict[str, Any] | None) -> ShieldLoadout | None:
    if data is None:
        return None
    return ShieldLoadout(
        shield_type=str(data["type"]),
        grade=int(data["grade"]),
        notes=_as_tuple(data.get("notes")),
    )


def _parse_weapons(data: list[dict[str, Any]] | None) -> tuple[WeaponLoadout, ...]:
    if data is None:
        return ()
    parsed: list[WeaponLoadout] = []
    for entry in data:
        parsed.append(
            WeaponLoadout(
                slot=str(entry["slot"]),
                weapon_id=str(entry["weapon_id"]),
                competency=str(entry["competency"]),
                grade=int(entry.get("grade", 1)),
                base_potency=int(entry.get("base_potency", 0)),
                notes=_as_tuple(entry.get("notes")),
            )
        )
    return tuple(parsed)


def _parse_damage_model(data: dict[str, Any] | None) -> DamageModelDefinition:
    if data is None:
        return DamageModelDefinition(kind="player_wounds")

    creature_zones_data = data.get("creature_zones", [])
    creature_zones = tuple(
        CreatureZoneDefinition(
            id=str(entry["id"]),
            max_hp=int(entry["max_hp"]),
            block=int(entry["block"]),
            dr_bonus=int(entry.get("dr_bonus", 0)),
            durability=int(entry.get("durability", 0)),
            linked_abilities=_as_tuple(entry.get("linked_abilities")),
            vital=bool(entry.get("vital", False)),
            notes=_as_tuple(entry.get("notes")),
        )
        for entry in creature_zones_data
    )
    return DamageModelDefinition(
        kind=str(data.get("kind", "player_wounds")),
        creature_zones=creature_zones,
        notes=_as_tuple(data.get("notes")),
    )


def load_species_profile_definitions(
    *,
    path: Path | None = None,
    context: FramingLoadContext | None = None,
) -> tuple[CombatantProfileDefinition, ...]:
    """Load simulation-ready combatant profile definitions."""

    context = context or build_framing_load_context()
    path = path or (context.sim_root / "data" / "species")

    profiles: list[CombatantProfileDefinition] = []
    for file_path in _iter_yaml_files(path):
        data = _load_yaml(file_path)
        for entry in data.get("profiles", []):
            profiles.append(
                CombatantProfileDefinition(
                    id=str(entry["id"]),
                    species=str(entry["species"]),
                    preparation=int(entry["preparation"]),
                    movement_meters=int(entry["movement_meters"]),
                    damage_model=_parse_damage_model(entry.get("damage_model")),
                    characteristics={str(key): int(value) for key, value in dict(entry.get("characteristics", {})).items()},
                    competencies=_parse_competencies(dict(entry.get("competencies", {}))),
                    armor_zones=_parse_armor_zones(entry.get("armor_zones")),
                    shield=_parse_shield(entry.get("shield")),
                    weapons=_parse_weapons(entry.get("weapons")),
                    techniques=_as_tuple(entry.get("techniques")),
                    equipment=_as_tuple(entry.get("equipment")),
                    zones=_as_tuple(entry.get("zones")),
                    policy_defaults={str(key): str(value) for key, value in dict(entry.get("policy_defaults", {})).items()},
                    notes=_as_tuple(entry.get("notes")),
                )
            )
    return tuple(profiles)


def load_environment_definitions(
    *,
    path: Path | None = None,
    context: FramingLoadContext | None = None,
) -> tuple[EnvironmentDefinition, ...]:
    """Load reusable environment definitions."""

    context = context or build_framing_load_context()
    path = path or (context.sim_root / "data" / "environments")

    environments: list[EnvironmentDefinition] = []
    for file_path in _iter_yaml_files(path):
        data = _load_yaml(file_path)
        environment_data = data.get("environment")
        if not environment_data:
            continue

        environments.append(
            EnvironmentDefinition(
                id=str(environment_data["id"]),
                description=str(environment_data.get("description", "")),
                roll_modifiers={str(key): int(value) for key, value in dict(environment_data.get("roll_modifiers", {})).items()},
                notes=_as_tuple(environment_data.get("notes")),
            )
        )
    return tuple(environments)


def load_scenario_definitions(
    *,
    path: Path | None = None,
    context: FramingLoadContext | None = None,
) -> tuple[ScenarioDefinition, ...]:
    """Load scenario definitions from one file or a scenario tree."""

    context = context or build_framing_load_context()
    path = path or (context.sim_root / "scenarios")

    scenarios: list[ScenarioDefinition] = []
    for file_path in _iter_yaml_files(path):
        data = _load_yaml(file_path)
        scenario_data = data.get("scenario")
        if not scenario_data:
            continue

        map_data = scenario_data.get("map")
        map_definition = None
        if map_data:
            map_definition = MapDefinition(
                width_m=int(map_data["width_m"]),
                height_m=int(map_data["height_m"]),
                notes=_as_tuple(map_data.get("notes")),
            )

        actor_slots = []
        for slot in scenario_data.get("actors", []):
            actor_slots.append(
                ScenarioActorSlot(
                    slot=str(slot["slot"]),
                    position=GridPosition(x=int(slot["position"][0]), y=int(slot["position"][1])),
                    notes=_as_tuple(slot.get("notes")),
                )
            )

        scenarios.append(
            ScenarioDefinition(
                id=str(scenario_data["id"]),
                environment_id=scenario_data.get("environment"),
                map=map_definition,
                actor_slots=tuple(actor_slots),
                conditions=_as_tuple(scenario_data.get("conditions")),
                observer_relations=_as_tuple(scenario_data.get("observer_relations")),
                roll_modifiers={
                    str(slot): {str(key): int(value) for key, value in dict(modifiers).items()}
                    for slot, modifiers in dict(scenario_data.get("roll_modifiers", {})).items()
                },
                notes=_as_tuple(scenario_data.get("notes")),
            )
        )
    return tuple(scenarios)


def load_question_definitions(
    *,
    path: Path | None = None,
    context: FramingLoadContext | None = None,
) -> tuple[QuestionDefinition, ...]:
    """Load question definitions from one file or a question tree."""

    context = context or build_framing_load_context()
    path = path or (context.sim_root / "questions")

    questions: list[QuestionDefinition] = []
    for file_path in _iter_yaml_files(path):
        data = _load_yaml(file_path)
        if "id" not in data or "question" not in data or "scenario" not in data:
            continue

        actor_assignments = []
        for slot, profile_id in dict(data.get("actors", {})).items():
            actor_assignments.append(ActorAssignment(slot=str(slot), profile_id=str(profile_id)))

        questions.append(
            QuestionDefinition(
                id=str(data["id"]),
                prompt=str(data["question"]),
                scenario_id=str(data["scenario"]),
                profile_id=data.get("retrieval_profile"),
                domains=_as_tuple(data.get("domains")),
                actor_assignments=tuple(actor_assignments),
                policy_assignments={str(key): str(value) for key, value in dict(data.get("policies", {})).items()},
                metrics=_as_tuple(data.get("measurements")),
                iterations=int(data["iterations"]) if data.get("iterations") is not None else None,
                comparisons={str(key): str(value) for key, value in dict(data.get("compare", {})).items()},
                notes=_as_tuple(data.get("notes")),
            )
        )
    return tuple(questions)

"""Load simulation-facing action, technique, and ailment definitions."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from knowledge_access import for_simulator_domain_modeling
from knowledge_access.types import RetrievalBundle
from models import (
    ActionDefinition,
    AilmentDefinition,
    AilmentTimingDefinition,
    EffectDefinition,
    NumericBurdenDefinition,
    RecoveryDefinition,
    RollDefinition,
    TechniqueDefinition,
    TechniqueRequirements,
)


@dataclass(frozen=True)
class DefinitionLoadContext:
    """Shared context for loading simulator-facing definitions."""

    knowledge_bundle: RetrievalBundle
    design_root: Path
    sim_root: Path


def _sim_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _design_root() -> Path:
    return Path(__file__).resolve().parents[2]


def build_simulator_definition_context() -> DefinitionLoadContext:
    """Build the default loader context for simulator definition work."""

    return DefinitionLoadContext(
        knowledge_bundle=for_simulator_domain_modeling(),
        design_root=_design_root(),
        sim_root=_sim_root(),
    )


def _load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    if not isinstance(loaded, dict):
        raise ValueError(f"Expected mapping at top level of {path}")
    return loaded


def _iter_yaml_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(path.rglob("*.yaml"))


def _as_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        raise ValueError(f"Expected list, got {type(value)!r}")
    return tuple(str(item) for item in value)


def _roll_from_data(data: dict[str, Any] | None) -> RollDefinition | None:
    if not data:
        return None
    return RollDefinition(
        family=str(data["family"]),
        competency=data.get("competency"),
        opposed_by=data.get("opposed_by"),
        notes=_as_tuple(data.get("notes")),
    )


def _effects_from_data(entries: list[dict[str, Any]] | None) -> tuple[EffectDefinition, ...]:
    if not entries:
        return ()
    return tuple(
        EffectDefinition(
            id=str(entry["id"]),
            parameters=dict(entry.get("parameters", {})),
            notes=_as_tuple(entry.get("notes")),
        )
        for entry in entries
    )


def load_action_definitions(
    *,
    path: Path | None = None,
    context: DefinitionLoadContext | None = None,
) -> tuple[ActionDefinition, ...]:
    """Load simulation-facing base action definitions."""

    context = context or build_simulator_definition_context()
    path = path or (context.sim_root / "data" / "actions" / "base_actions.yaml")
    data = _load_yaml(path)
    entries = data.get("actions", [])

    definitions = []
    for entry in entries:
        definitions.append(
            ActionDefinition(
                id=str(entry["id"]),
                name=str(entry["name"]),
                category=str(entry["category"]),
                rhythm=int(entry["rhythm"]),
                attrition=int(entry["attrition"]),
                trigger_type=str(entry["trigger_type"]),
                roll=_roll_from_data(entry.get("roll")),
                legal_when=_as_tuple(entry.get("legal_when")),
                effects=_effects_from_data(entry.get("effects")),
                notes=_as_tuple(entry.get("notes")),
            )
        )
    return tuple(definitions)


def load_technique_definitions(
    *,
    path: Path | None = None,
    context: DefinitionLoadContext | None = None,
) -> tuple[TechniqueDefinition, ...]:
    """Load simulation-facing technique definitions."""

    context = context or build_simulator_definition_context()
    definitions = []
    path = path or (context.sim_root / "data" / "techniques")
    for file_path in _iter_yaml_files(path):
        data = _load_yaml(file_path)
        entries = data.get("techniques", [])
        for entry in entries:
            requirements_data = dict(entry.get("requirements", {}))
            requirements = TechniqueRequirements(
                competencies=_as_tuple(requirements_data.get("competencies")),
                states=_as_tuple(requirements_data.get("states")),
                equipment=_as_tuple(requirements_data.get("equipment")),
                tags=_as_tuple(requirements_data.get("tags")),
                notes=_as_tuple(requirements_data.get("notes")),
            )
            definitions.append(
                TechniqueDefinition(
                    id=str(entry["id"]),
                    name=str(entry["name"]),
                    species=entry.get("species"),
                    category=str(entry["category"]),
                    type=str(entry["type"]),
                    origin=str(entry["origin"]),
                    rhythm=int(entry["rhythm"]),
                    attrition=int(entry["attrition"]),
                    trigger=str(entry["trigger"]),
                    roll=_roll_from_data(entry.get("roll")),
                    requirements=requirements,
                    effects=_effects_from_data(entry.get("effects")),
                    restrictions=_as_tuple(entry.get("restrictions")),
                    duration_model=entry.get("duration_model"),
                    scaling=dict(entry.get("scaling", {})),
                    notes=_as_tuple(entry.get("notes")),
                )
            )
    return tuple(definitions)


def load_ailment_definitions(
    *,
    path: Path | None = None,
    context: DefinitionLoadContext | None = None,
) -> tuple[AilmentDefinition, ...]:
    """Load simulation-facing ailment definitions."""

    context = context or build_simulator_definition_context()
    path = path or (context.sim_root / "data" / "ailments" / "ailments.yaml")
    data = _load_yaml(path)
    entries = data.get("ailments", [])

    definitions = []
    for entry in entries:
        numeric_burden_data = entry.get("numeric_burden")
        numeric_burden = None
        if numeric_burden_data:
            numeric_burden = NumericBurdenDefinition(
                source=str(numeric_burden_data["source"]),
                applies_to=_as_tuple(numeric_burden_data.get("applies_to")),
                notes=_as_tuple(numeric_burden_data.get("notes")),
            )

        recovery_data = entry.get("recovery")
        recovery = None
        if recovery_data:
            recovery = RecoveryDefinition(
                type=str(recovery_data["type"]),
                competency=recovery_data.get("competency"),
                threshold_model=recovery_data.get("threshold_model"),
                notes=_as_tuple(recovery_data.get("notes")),
            )

        timing_data = entry.get("timing")
        timing = None
        if timing_data:
            timing = AilmentTimingDefinition(
                activation_start=_as_tuple(timing_data.get("activation_start")),
                action_gate=_as_tuple(timing_data.get("action_gate")),
                reevaluation_points=_as_tuple(timing_data.get("reevaluation_points")),
                expiry_mode=timing_data.get("expiry_mode"),
                fiction_release_events=_as_tuple(timing_data.get("fiction_release_events")),
                notes=_as_tuple(timing_data.get("notes")),
            )

        qualitative_burden = {
            str(key): _as_tuple(value) for key, value in dict(entry.get("qualitative_burden", {})).items()
        }

        definitions.append(
            AilmentDefinition(
                id=str(entry["id"]),
                family=str(entry["family"]),
                severity_model=str(entry["severity_model"]),
                numeric_burden=numeric_burden,
                qualitative_burden=qualitative_burden,
                recovery=recovery,
                timing=timing,
                persistence_rule=entry.get("persistence_rule"),
                application_notes=_as_tuple(entry.get("application_notes")),
                replacement_rules=_as_tuple(entry.get("replacement_rules")),
            )
        )
    return tuple(definitions)

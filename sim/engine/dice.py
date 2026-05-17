"""Dice helpers and probability-facing roll utilities."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from math import ceil
from typing import Any, Mapping
import unicodedata

import yaml

from .rng import SimulationRNG


@dataclass(frozen=True)
class RollValue:
    """One resolved roll value."""

    raw: int
    modifier: int
    total: int
    family: str = "generic"
    competency: str | None = None
    level: int = 0
    rank: str | None = None


@dataclass(frozen=True)
class OpposedOutcome:
    """Result of comparing two rolled values directly."""

    attacker: RollValue
    defender: RollValue
    attacker_wins: bool
    margin: int


@dataclass(frozen=True)
class ThresholdOutcome:
    """Result of checking one roll against a canonical threshold."""

    roll: RollValue
    threshold_id: str
    reference_level: int
    target: int
    success: bool
    margin: int


def _workspace_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _normalize_label(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch)).casefold()


CHARACTERISTIC_ALIASES: dict[str, tuple[str, ...]] = {
    "Strength": ("Strength", "Fuerza", "STR"),
    "Agility": ("Agility", "Agilidad", "AGI"),
    "Tenacity": ("Tenacity", "Tenacidad", "TEN"),
    "Intellect": ("Intellect", "Intelecto", "INT"),
    "Cunning": ("Cunning", "Astucia", "CUN"),
    "Wisdom": ("Wisdom", "Sabiduría", "Sabiduria", "WIS"),
    "Composure": ("Composure", "Compostura", "CMP"),
    "Aura": ("Aura", "AUR"),
    "Presence": ("Presence", "Presencia", "PRE"),
    "Preparation": ("Preparation", "Preparación", "Preparacion"),
    "Resilience": ("Resilience", "Resiliencia"),
}


RESISTANCE_CHARACTERISTICS: dict[str, str] = {
    "poison": "Tenacity",
    "infection": "Tenacity",
    "affliction": "Composure",
    "curse": "Composure",
    "curses": "Composure",
    "alteration": "Resilience",
}


@lru_cache(maxsize=1)
def _rank_numbers() -> dict[str, int]:
    path = _workspace_root() / "Transcendence-design" / "data" / "system" / "competencies.yaml"
    with path.open("r", encoding="utf-8") as handle:
        data: dict[str, Any] = yaml.safe_load(handle)

    ranks = data.get("ranks", [])
    return {str(entry["id"]): int(entry["rank_number"]) for entry in ranks}


@lru_cache(maxsize=1)
def _characteristic_alias_map() -> dict[str, str]:
    alias_map: dict[str, str] = {}
    for canonical_name, aliases in CHARACTERISTIC_ALIASES.items():
        alias_map[_normalize_label(canonical_name)] = canonical_name
        for alias in aliases:
            alias_map[_normalize_label(alias)] = canonical_name
    return alias_map


@lru_cache(maxsize=1)
def _difficulty_bases() -> dict[str, int]:
    path = _workspace_root() / "Transcendence-design" / "data" / "system" / "difficulty-thresholds.yaml"
    with path.open("r", encoding="utf-8") as handle:
        data: dict[str, Any] = yaml.safe_load(handle)

    tiers = data.get("tiers", [])
    return {str(entry["id"]): int(entry["base"]) for entry in tiers}


@lru_cache(maxsize=1)
def _specialization_characteristics() -> dict[str, str]:
    path = _workspace_root() / "Transcendence-design" / "data" / "system" / "specializations-catalog.yaml"
    with path.open("r", encoding="utf-8") as handle:
        data: dict[str, Any] = yaml.safe_load(handle)

    entries = data.get("especializaciones", data.get("specializations", []))
    mapping: dict[str, str] = {}
    for entry in entries:
        name = entry.get("nombre") or entry.get("name")
        characteristic = entry.get("característica_asociada") or entry.get("caracteristica_asociada") or entry.get("associated_characteristic")
        if name and characteristic:
            mapping[_normalize_label(str(name))] = str(characteristic)
    return mapping


def rank_bonus(rank: str | None) -> int:
    """Return canonical rank bonus from the authority competency ranks."""

    if rank is None:
        return 0
    return _rank_numbers().get(rank, 0)


def difficulty_target(threshold_id: str, *, reference_level: int = 0) -> int:
    """Return canonical threshold target as base + reference level."""

    try:
        base = _difficulty_bases()[threshold_id]
    except KeyError as exc:
        raise KeyError(f"Unknown difficulty threshold id: {threshold_id}") from exc
    return base + reference_level


def associated_characteristic(competency: str) -> str | None:
    """Return the canonical associated characteristic for a specialization-like competency."""

    return _specialization_characteristics().get(_normalize_label(competency))


def canonical_characteristic_name(characteristic: str) -> str:
    """Return the canonical characteristic label used by the simulator."""

    normalized = _normalize_label(characteristic)
    try:
        return _characteristic_alias_map()[normalized]
    except KeyError as exc:
        raise KeyError(f"Unknown characteristic label: {characteristic}") from exc


def characteristic_value(characteristics: Mapping[str, int], characteristic: str) -> int:
    """Resolve one direct or derived characteristic value from a runtime characteristic map."""

    canonical = canonical_characteristic_name(characteristic)
    normalized_values = {
        canonical_characteristic_name(name): int(value)
        for name, value in characteristics.items()
        if _normalize_label(name) in _characteristic_alias_map()
    }

    if canonical in normalized_values:
        return normalized_values[canonical]

    if canonical == "Resilience":
        tenacity = normalized_values.get("Tenacity", 0)
        wisdom = normalized_values.get("Wisdom", 0)
        composure = normalized_values.get("Composure", 0)
        return ceil((tenacity + wisdom + composure) / 3)

    if canonical == "Preparation":
        agility = normalized_values.get("Agility", 0)
        cunning = normalized_values.get("Cunning", 0)
        composure = normalized_values.get("Composure", 0)
        return ceil((agility + cunning + composure) / 3)

    return 0


def resistance_characteristic(effect_family: str) -> str:
    """Return the base characteristic used by a resistance roll family."""

    normalized = _normalize_label(effect_family)
    try:
        return RESISTANCE_CHARACTERISTICS[normalized]
    except KeyError as exc:
        raise KeyError(f"Unknown resistance family: {effect_family}") from exc


def competency_roll(
    *,
    family: str,
    competency: str | None,
    level: int,
    rank: str | None,
    rng: SimulationRNG,
    characteristic_modifier: int = 0,
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
) -> RollValue:
    """Resolve a simplified d10-based competency roll.

    Formula:
    1d10 + characteristic_modifier + competency level + rank bonus + bonus_modifier - penalty_modifier
    """

    raw = rng.d10()
    modifier = characteristic_modifier + level + rank_bonus(rank) + bonus_modifier - penalty_modifier
    return RollValue(
        raw=raw,
        modifier=modifier,
        total=raw + modifier,
        family=family,
        competency=competency,
        level=level,
        rank=rank,
    )


def attack_roll(
    *,
    competency: str | None,
    level: int,
    rank: str | None,
    rng: SimulationRNG,
    characteristic_modifier: int = 0,
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
) -> RollValue:
    """Resolve a canonical Attack Roll.

    Formula:
    1d10 + associated characteristic + competency level + competency rank bonus + bonuses - penalties
    """

    return competency_roll(
        family="attack",
        competency=competency,
        level=level,
        rank=rank,
        rng=rng,
        characteristic_modifier=characteristic_modifier,
        bonus_modifier=bonus_modifier,
        penalty_modifier=penalty_modifier,
    )


def characteristic_roll(
    *,
    characteristic: str,
    rng: SimulationRNG,
    characteristic_modifier: int = 0,
    reference_level: int = 0,
) -> RollValue:
    """Resolve a canonical Characteristic Roll.

    Formula:
    1d10 + characteristic + reference level + bonuses - penalties
    """

    raw = rng.d10()
    modifier = characteristic_modifier + reference_level
    return RollValue(
        raw=raw,
        modifier=modifier,
        total=raw + modifier,
        family="characteristic",
        competency=characteristic,
        level=0,
        rank=None,
    )


def specialization_roll(
    *,
    competency: str,
    level: int,
    rank: str | None,
    rng: SimulationRNG,
    characteristic_modifier: int = 0,
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
) -> RollValue:
    """Resolve a simplified specialization roll.

    Formula:
    1d10 + associated characteristic + competency level + competency rank bonus + bonuses - penalties
    """

    return competency_roll(
        family="specialization",
        competency=competency,
        level=level,
        rank=rank,
        rng=rng,
        characteristic_modifier=characteristic_modifier,
        bonus_modifier=bonus_modifier,
        penalty_modifier=penalty_modifier,
    )


def untrained_specialization_roll(
    *,
    competency: str,
    rng: SimulationRNG,
    characteristic_modifier: int = 0,
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
) -> RollValue:
    """Resolve an untrained Specialization Roll.

    Formula:
    1d10 + associated characteristic + bonuses - penalties
    """

    return competency_roll(
        family="specialization",
        competency=competency,
        level=0,
        rank="untrained",
        rng=rng,
        characteristic_modifier=characteristic_modifier,
        bonus_modifier=bonus_modifier,
        penalty_modifier=penalty_modifier,
    )


def applicable_defense_values(
    *,
    armor_type: str,
    evasion_level: int,
    evasion_rank: str | None,
    agility_modifier: int,
) -> tuple[int, int]:
    """Resolve armor-constrained evasion and agility contributions for D.R."""

    normalized = _normalize_label(armor_type)
    evasion_total = evasion_level + rank_bonus(evasion_rank)
    if normalized in {"unarmored", "light"}:
        return evasion_total, agility_modifier
    if normalized == "medium":
        return evasion_total, max(1, ceil(agility_modifier / 2))
    if normalized == "heavy":
        return max(1, ceil(evasion_total / 2)), 0
    raise KeyError(f"Unknown armor type for defense applicability: {armor_type}")


def defense_roll(
    *,
    competency: str = "Evasion",
    level: int,
    rank: str | None,
    rng: SimulationRNG,
    characteristic_modifier: int = 0,
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
) -> RollValue:
    """Resolve a canonical Defense Roll.

    Formula:
    1d10 + applicable evasion contribution + applicable agility + defensive bonuses - penalties
    """

    return competency_roll(
        family="defense",
        competency=competency,
        level=level,
        rank=rank,
        rng=rng,
        characteristic_modifier=characteristic_modifier,
        bonus_modifier=bonus_modifier,
        penalty_modifier=penalty_modifier,
    )


def resistance_roll(
    *,
    competency: str,
    level: int,
    rank: str | None,
    rng: SimulationRNG,
    characteristic_modifier: int = 0,
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
) -> RollValue:
    """Resolve a canonical Resistance Roll.

    Formula:
    1d10 + relevant base characteristic + resistance level + resistance rank bonus + bonuses - penalties
    """

    return competency_roll(
        family="resistance",
        competency=competency,
        level=level,
        rank=rank,
        rng=rng,
        characteristic_modifier=characteristic_modifier,
        bonus_modifier=bonus_modifier,
        penalty_modifier=penalty_modifier,
    )


def resolve_opposed(attacker: RollValue, defender: RollValue) -> OpposedOutcome:
    """Resolve a direct opposed comparison."""

    margin = attacker.total - defender.total
    return OpposedOutcome(
        attacker=attacker,
        defender=defender,
        attacker_wins=margin > 0,
        margin=margin,
    )


def resolve_threshold(
    roll: RollValue,
    *,
    threshold_id: str,
    reference_level: int = 0,
) -> ThresholdOutcome:
    """Resolve a roll against a canonical threshold tier."""

    target = difficulty_target(threshold_id, reference_level=reference_level)
    margin = roll.total - target
    return ThresholdOutcome(
        roll=roll,
        threshold_id=threshold_id,
        reference_level=reference_level,
        target=target,
        success=margin >= 0,
        margin=margin,
    )

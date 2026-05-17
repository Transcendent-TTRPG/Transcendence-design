"""Critical-potency break attempts against breakable creature zones."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any
import unicodedata

import yaml

from models import Combatant, CreatureZoneState

from .exchange import ExchangeResult


def _workspace_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _normalize_label(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch)).casefold()


@lru_cache(maxsize=1)
def _weapon_potency_multipliers() -> dict[str, float]:
    path = _workspace_root() / "Transcendence-design" / "data" / "system" / "wounds-and-damage.yaml"
    with path.open("r", encoding="utf-8") as handle:
        data: dict[str, Any] = yaml.safe_load(handle)

    multipliers: dict[str, float] = {}
    entries = data.get("critical_potency", {}).get("weapon_multipliers", {})
    for key, value in dict(entries).items():
        multipliers[_normalize_label(str(key))] = float(value["multiplier"])
    return multipliers


WEAPON_TYPE_TO_POTENCY_KEY: dict[str, str] = {
    "spear": "spear",
    "axe": "axe",
    "mace": "mace",
    "long_blade": "long_blade",
    "long blade": "long_blade",
    "dagger": "dagger",
    "short_blade": "short_blade",
    "short blade": "short_blade",
    "thrown": "thrown",
    "ranged": "ranged",
    "flexible": "flexible",
}


@dataclass(frozen=True)
class CreatureBreakAttemptResult:
    """Result of one valid or invalid break attempt against a creature zone."""

    zone: str
    attempted: bool
    allowed: bool
    critical_required: bool
    critical_available: bool
    critical_potency: int
    durability_before: int
    durability_after: int
    broke: bool
    disabled: bool
    broken: bool
    vital_shutdown: bool
    disabled_abilities: tuple[str, ...]


def critical_potency_multiplier(weapon_type: str) -> float:
    """Return canonical critical-potency multiplier for a weapon type."""

    normalized = _normalize_label(weapon_type)
    mapped = WEAPON_TYPE_TO_POTENCY_KEY.get(normalized, normalized)
    try:
        return _weapon_potency_multipliers()[mapped]
    except KeyError as exc:
        raise KeyError(f"Unknown weapon type for critical potency: {weapon_type}") from exc


def critical_potency_for_exchange(exchange: ExchangeResult) -> int:
    """Resolve integer critical potency for one exchange's offensive context."""

    return int(exchange.offense_context.base_potency * critical_potency_multiplier(exchange.offense_context.weapon.weapon_type))


def _find_creature_zone(combatant: Combatant, zone: str) -> tuple[int, CreatureZoneState]:
    for index, zone_state in enumerate(combatant.creature_zones):
        if zone_state.id == zone:
            return index, zone_state
    raise KeyError(f"Combatant '{combatant.id}' has no creature zone '{zone}'.")


def attempt_creature_zone_break(
    *,
    defender: Combatant,
    exchange: ExchangeResult,
    allow_without_critical: bool = False,
) -> CreatureBreakAttemptResult:
    """Resolve one break attempt against a creature zone using critical potency."""

    if defender.damage_model_kind != "creature_zones":
        raise ValueError(f"Combatant '{defender.id}' does not use creature_zones damage model.")

    index, zone_state = _find_creature_zone(defender, exchange.zone)
    critical_available = bool(exchange.impact_roll and exchange.impact_roll.critical_impact)
    allowed = exchange.attack_connected and (critical_available or allow_without_critical)
    durability_before = zone_state.durability
    if not allowed:
        return CreatureBreakAttemptResult(
            zone=exchange.zone,
            attempted=False,
            allowed=False,
            critical_required=not allow_without_critical,
            critical_available=critical_available,
            critical_potency=0,
            durability_before=durability_before,
            durability_after=durability_before,
            broke=False,
            disabled=zone_state.disabled,
            broken=zone_state.broken,
            vital_shutdown=False,
            disabled_abilities=(),
        )

    potency = critical_potency_for_exchange(exchange)
    if zone_state.broken or zone_state.disabled:
        return CreatureBreakAttemptResult(
            zone=exchange.zone,
            attempted=True,
            allowed=True,
            critical_required=not allow_without_critical,
            critical_available=critical_available,
            critical_potency=potency,
            durability_before=durability_before,
            durability_after=durability_before,
            broke=False,
            disabled=zone_state.disabled,
            broken=zone_state.broken,
            vital_shutdown=zone_state.vital and zone_state.disabled,
            disabled_abilities=zone_state.linked_abilities if zone_state.disabled else (),
        )

    if potency >= durability_before:
        durability_after = 0
        broke = True
        disabled = True
        broken = True
        disabled_abilities = zone_state.linked_abilities
    else:
        durability_after = max(0, durability_before - 1)
        broke = False
        disabled = zone_state.disabled
        broken = zone_state.broken
        disabled_abilities = ()

    defender.creature_zones[index] = CreatureZoneState(
        id=zone_state.id,
        max_hp=zone_state.max_hp,
        current_hp=zone_state.current_hp,
        block=zone_state.block,
        dr_bonus=zone_state.dr_bonus,
        max_durability=zone_state.max_durability,
        durability=durability_after,
        linked_abilities=zone_state.linked_abilities,
        vital=zone_state.vital,
        broken=broken,
        disabled=disabled,
        notes=zone_state.notes,
    )

    vital_shutdown = broke and zone_state.vital
    return CreatureBreakAttemptResult(
        zone=exchange.zone,
        attempted=True,
        allowed=True,
        critical_required=not allow_without_critical,
        critical_available=critical_available,
        critical_potency=potency,
        durability_before=durability_before,
        durability_after=durability_after,
        broke=broke,
        disabled=disabled,
        broken=broken,
        vital_shutdown=vital_shutdown,
        disabled_abilities=disabled_abilities,
    )

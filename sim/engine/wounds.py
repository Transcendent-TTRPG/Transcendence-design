"""Localized wound resolution for player-like combatants."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from models import Combatant, ZoneState

from .exchange import ExchangeResult


WoundSeverity = Literal["none", "light", "grave", "critical"]


@dataclass(frozen=True)
class WoundBand:
    """Resolved wound severity band from one connected hit."""

    severity: WoundSeverity
    slots: int


@dataclass(frozen=True)
class WoundResolutionResult:
    """Result of applying one hit to one localized player zone."""

    zone: str
    severity: WoundSeverity
    slots_applied: int
    overflow_slots: int
    occupied_before: int
    occupied_after: int
    capacity: int
    saturated: bool
    collapsed: bool
    vital_collapse_rr_required: bool


def wound_band_from_impact(*, impact: int, block: int) -> WoundBand:
    """Resolve wound severity from the canonical impact-vs-block comparison."""

    if block < 0:
        raise ValueError("Block cannot be negative.")
    threshold = max(1, block)
    if impact <= threshold:
        return WoundBand(severity="none", slots=0)
    if impact < threshold * 2:
        return WoundBand(severity="light", slots=1)
    if impact < threshold * 3:
        return WoundBand(severity="grave", slots=2)
    return WoundBand(severity="critical", slots=3)


def _find_zone_state(combatant: Combatant, zone: str) -> tuple[int, ZoneState]:
    for index, zone_state in enumerate(combatant.zones):
        if zone_state.id == zone:
            return index, zone_state
    raise KeyError(f"Combatant '{combatant.id}' has no zone '{zone}'.")


def apply_exchange_wound(
    *,
    defender: Combatant,
    exchange: ExchangeResult,
) -> WoundResolutionResult:
    """Apply a connected exchange to the defender's localized wound state."""

    if not exchange.attack_connected or exchange.impact_roll is None:
        index, zone_state = _find_zone_state(defender, exchange.zone)
        return WoundResolutionResult(
            zone=exchange.zone,
            severity="none",
            slots_applied=0,
            overflow_slots=0,
            occupied_before=zone_state.occupied_slots,
            occupied_after=zone_state.occupied_slots,
            capacity=zone_state.capacity,
            saturated=zone_state.saturated,
            collapsed=zone_state.collapsed,
            vital_collapse_rr_required=False,
        )

    band = wound_band_from_impact(
        impact=exchange.impact_roll.total,
        block=exchange.block_context.total_block,
    )
    index, zone_state = _find_zone_state(defender, exchange.zone)
    occupied_before = zone_state.occupied_slots
    capacity = zone_state.capacity

    if band.slots == 0:
        return WoundResolutionResult(
            zone=exchange.zone,
            severity="none",
            slots_applied=0,
            overflow_slots=0,
            occupied_before=occupied_before,
            occupied_after=occupied_before,
            capacity=capacity,
            saturated=zone_state.saturated,
            collapsed=zone_state.collapsed,
            vital_collapse_rr_required=False,
        )

    free_slots = max(0, capacity - occupied_before)
    slots_applied = min(band.slots, free_slots)
    overflow_slots = max(0, band.slots - free_slots)
    occupied_after = min(capacity, occupied_before + band.slots)
    collapsed = zone_state.collapsed or overflow_slots > 0 or zone_state.saturated
    saturated = occupied_after == capacity and not collapsed
    vital_collapse_rr_required = collapsed and exchange.zone in {"head", "torso"}

    defender.zones[index] = ZoneState(
        id=zone_state.id,
        capacity=zone_state.capacity,
        occupied_slots=occupied_after,
        operational=not collapsed,
        saturated=saturated,
        collapsed=collapsed,
        tags=zone_state.tags,
        notes=zone_state.notes,
    )

    return WoundResolutionResult(
        zone=exchange.zone,
        severity=band.severity,
        slots_applied=slots_applied,
        overflow_slots=overflow_slots,
        occupied_before=occupied_before,
        occupied_after=occupied_after,
        capacity=capacity,
        saturated=saturated,
        collapsed=collapsed,
        vital_collapse_rr_required=vital_collapse_rr_required,
    )

"""Creature-zone damage application and linked-ability disablement."""

from __future__ import annotations

from dataclasses import dataclass

from models import Combatant, CreatureZoneState

from .exchange import ExchangeResult


@dataclass(frozen=True)
class CreatureDamageResolutionResult:
    """Result of applying one exchange to one creature zone."""

    zone: str
    effective_damage: int
    hp_before: int
    hp_after: int
    disabled: bool
    broken: bool
    vital_shutdown: bool
    disabled_abilities: tuple[str, ...]


def _find_creature_zone(combatant: Combatant, zone: str) -> tuple[int, CreatureZoneState]:
    for index, zone_state in enumerate(combatant.creature_zones):
        if zone_state.id == zone:
            return index, zone_state
    raise KeyError(f"Combatant '{combatant.id}' has no creature zone '{zone}'.")


def apply_exchange_to_creature_zone(
    *,
    defender: Combatant,
    exchange: ExchangeResult,
) -> CreatureDamageResolutionResult:
    """Apply effective damage from one exchange to a creature-zone model."""

    if defender.damage_model_kind != "creature_zones":
        raise ValueError(f"Combatant '{defender.id}' does not use creature_zones damage model.")

    index, zone_state = _find_creature_zone(defender, exchange.zone)
    hp_before = zone_state.current_hp
    if not exchange.attack_connected or exchange.effective_damage <= 0:
        return CreatureDamageResolutionResult(
            zone=exchange.zone,
            effective_damage=0,
            hp_before=hp_before,
            hp_after=hp_before,
            disabled=zone_state.disabled,
            broken=zone_state.broken,
            vital_shutdown=False,
            disabled_abilities=(),
        )

    hp_after = max(0, hp_before - exchange.effective_damage)
    disabled = zone_state.disabled or hp_after <= 0
    broken = zone_state.broken or hp_after <= 0
    vital_shutdown = disabled and zone_state.vital
    disabled_abilities = zone_state.linked_abilities if disabled else ()

    defender.creature_zones[index] = CreatureZoneState(
        id=zone_state.id,
        max_hp=zone_state.max_hp,
        current_hp=hp_after,
        block=zone_state.block,
        dr_bonus=zone_state.dr_bonus,
        max_durability=zone_state.max_durability,
        durability=zone_state.durability,
        linked_abilities=zone_state.linked_abilities,
        vital=zone_state.vital,
        broken=broken,
        disabled=disabled,
        notes=zone_state.notes,
    )

    return CreatureDamageResolutionResult(
        zone=exchange.zone,
        effective_damage=exchange.effective_damage,
        hp_before=hp_before,
        hp_after=hp_after,
        disabled=disabled,
        broken=broken,
        vital_shutdown=vital_shutdown,
        disabled_abilities=disabled_abilities,
    )

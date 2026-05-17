"""Helpers for creature-zone damage models and linked abilities."""

from __future__ import annotations

from models import Combatant


def active_linked_abilities(combatant: Combatant) -> set[str]:
    """Return linked abilities still supported by non-disabled creature zones."""

    abilities: set[str] = set()
    for zone in combatant.creature_zones:
        if zone.disabled or zone.broken or zone.current_hp <= 0:
            continue
        abilities.update(zone.linked_abilities)
    return abilities


def creature_supports_ability(combatant: Combatant, ability_id: str) -> bool:
    """Return whether the creature still supports one linked ability."""

    return ability_id in active_linked_abilities(combatant)

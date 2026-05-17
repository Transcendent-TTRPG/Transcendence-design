"""Equipment-facing simulation models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArmorZoneLoadout:
    """Armor type present in one defended zone."""

    zone: str
    armor_type: str
    grade: int = 1
    material_bonus: int = 0
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ShieldLoadout:
    """Shield configuration that can add passive D.R. bonus."""

    shield_type: str
    grade: int
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class WeaponLoadout:
    """Weapon configuration used to resolve A.R. and I.R."""

    slot: str
    weapon_id: str
    competency: str
    grade: int
    base_potency: int = 0
    notes: tuple[str, ...] = ()

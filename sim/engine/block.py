"""Zone block helpers for post-defense mitigation."""

from __future__ import annotations

from dataclasses import dataclass

from models import Combatant


BASE_BLOCK_BY_ARMOR: dict[str, int] = {
    "light": 2,
    "medium": 4,
    "heavy": 6,
}

ARMOR_COMPETENCY_BY_TYPE: dict[str, str] = {
    "light": "light_armor",
    "medium": "medium_armor",
    "heavy": "heavy_armor",
}


@dataclass(frozen=True)
class ZoneBlockContext:
    """Resolved block context for one struck zone."""

    zone: str
    armor_type: str
    base_block: int
    material_bonus: int
    competency_level: int
    piece_grade: int
    total_block: int


def zone_block_for_combatant(*, combatant: Combatant, zone: str) -> ZoneBlockContext:
    """Resolve the struck zone's block contribution."""

    creature_zone = next((entry for entry in combatant.creature_zones if entry.id == zone), None)
    if combatant.damage_model_kind == "creature_zones" and creature_zone is not None:
        return ZoneBlockContext(
            zone=zone,
            armor_type="creature_zone",
            base_block=creature_zone.block,
            material_bonus=0,
            competency_level=0,
            piece_grade=0,
            total_block=creature_zone.block,
        )

    armor_loadout = combatant.armor_zones.get(zone)
    if armor_loadout is None:
        return ZoneBlockContext(
            zone=zone,
            armor_type="unarmored",
            base_block=0,
            material_bonus=0,
            competency_level=0,
            piece_grade=0,
            total_block=0,
        )

    armor_type = armor_loadout.armor_type
    base_block = BASE_BLOCK_BY_ARMOR.get(armor_type, 0)
    competency_id = ARMOR_COMPETENCY_BY_TYPE.get(armor_type)
    rating = None if competency_id is None else combatant.competencies.get(competency_id)
    competency_level = 0 if rating is None else rating.level
    piece_grade = armor_loadout.grade
    material_bonus = armor_loadout.material_bonus
    total_block = base_block + material_bonus + competency_level + piece_grade
    return ZoneBlockContext(
        zone=zone,
        armor_type=armor_type,
        base_block=base_block,
        material_bonus=material_bonus,
        competency_level=competency_level,
        piece_grade=piece_grade,
        total_block=total_block,
    )

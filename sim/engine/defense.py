"""Zone-aware defense helpers."""

from __future__ import annotations

from dataclasses import dataclass

from models import Combatant

from .dice import applicable_defense_values, characteristic_value, defense_roll
from .rng import SimulationRNG


@dataclass(frozen=True)
class DefenseContext:
    """Resolved defensive context for one zone on one combatant."""

    zone: str
    armor_type: str
    evasion_level: int
    evasion_rank: str | None
    applicable_evasion: int
    applicable_agility: int
    shield_bonus: int
    bonus_modifier: int
    penalty_modifier: int


def shield_defense_bonus(shield_type: str, grade: int) -> int:
    """Return the passive D.R. shield bonus from shield type and grade."""

    normalized = shield_type.casefold()
    if normalized == "light":
        return grade
    if normalized == "medium":
        return grade
    if normalized == "heavy":
        return grade + 1
    raise KeyError(f"Unknown shield type: {shield_type}")


def build_defense_context(
    *,
    combatant: Combatant,
    zone: str,
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
) -> DefenseContext:
    """Resolve armor, agility, evasion, and shield context for one defended zone."""

    creature_zone = next((entry for entry in combatant.creature_zones if entry.id == zone), None)
    if combatant.damage_model_kind == "creature_zones" and creature_zone is not None:
        evasion_rating = combatant.competencies.get("Evasion")
        evasion_level = 0 if evasion_rating is None else evasion_rating.level
        evasion_rank = None if evasion_rating is None else evasion_rating.rank
        agility_modifier = characteristic_value(combatant.characteristics, "Agility")
        applicable_evasion, applicable_agility = applicable_defense_values(
            armor_type="unarmored",
            evasion_level=evasion_level,
            evasion_rank=evasion_rank,
            agility_modifier=agility_modifier,
        )
        return DefenseContext(
            zone=zone,
            armor_type="creature_zone",
            evasion_level=evasion_level,
            evasion_rank=evasion_rank,
            applicable_evasion=applicable_evasion,
            applicable_agility=applicable_agility,
            shield_bonus=0,
            bonus_modifier=bonus_modifier + creature_zone.dr_bonus,
            penalty_modifier=penalty_modifier,
        )

    armor_loadout = combatant.armor_zones.get(zone)
    armor_type = "unarmored" if armor_loadout is None else armor_loadout.armor_type
    evasion_rating = combatant.competencies.get("Evasion")
    evasion_level = 0 if evasion_rating is None else evasion_rating.level
    evasion_rank = None if evasion_rating is None else evasion_rating.rank
    agility_modifier = characteristic_value(combatant.characteristics, "Agility")
    applicable_evasion, applicable_agility = applicable_defense_values(
        armor_type=armor_type,
        evasion_level=evasion_level,
        evasion_rank=evasion_rank,
        agility_modifier=agility_modifier,
    )
    shield_bonus = 0
    if combatant.shield is not None:
        shield_bonus = shield_defense_bonus(combatant.shield.shield_type, combatant.shield.grade)

    return DefenseContext(
        zone=zone,
        armor_type=armor_type,
        evasion_level=evasion_level,
        evasion_rank=evasion_rank,
        applicable_evasion=applicable_evasion,
        applicable_agility=applicable_agility,
        shield_bonus=shield_bonus,
        bonus_modifier=bonus_modifier + shield_bonus,
        penalty_modifier=penalty_modifier,
    )


def defense_roll_for_zone(
    *,
    combatant: Combatant,
    zone: str,
    rng: SimulationRNG,
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
):
    """Resolve a canonical D.R. for one concrete defended zone."""

    context = build_defense_context(
        combatant=combatant,
        zone=zone,
        bonus_modifier=bonus_modifier,
        penalty_modifier=penalty_modifier,
    )
    return defense_roll(
        competency="Evasion",
        level=0,
        rank="untrained",
        rng=rng,
        characteristic_modifier=context.applicable_evasion + context.applicable_agility,
        bonus_modifier=context.bonus_modifier,
        penalty_modifier=context.penalty_modifier,
    )

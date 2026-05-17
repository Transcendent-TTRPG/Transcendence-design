"""Weapon-aware offense helpers for A.R. and I.R."""

from __future__ import annotations

from dataclasses import dataclass

from models import Combatant

from .dice import attack_roll, characteristic_value, rank_bonus
from .rng import SimulationRNG
from .weapons import WeaponDefinition, get_weapon_definition


@dataclass(frozen=True)
class OffenseContext:
    """Resolved offensive context for one weapon slot."""

    slot: str
    weapon_id: str
    competency: str
    weapon: WeaponDefinition
    characteristic_modifier: int
    competency_level: int
    competency_rank: str | None
    weapon_grade: int
    base_potency: int
    bonus_modifier: int
    penalty_modifier: int


@dataclass(frozen=True)
class ImpactRollValue:
    """Resolved Impact Roll value."""

    rolls: tuple[int, ...]
    weapon_die: str
    rank_number: int
    characteristic_modifier: int
    weapon_grade: int
    total: int
    critical_roll: int
    critical_face: int
    critical_impact: bool
    untrained: bool = False


def _die_size(die_code: str) -> int:
    try:
        return int(die_code.removeprefix("d"))
    except ValueError as exc:
        raise ValueError(f"Unsupported damage die code: {die_code}") from exc


def build_offense_context(
    *,
    combatant: Combatant,
    slot: str = "primary",
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
) -> OffenseContext:
    """Resolve weapon, competency, and characteristic context for one attack slot."""

    try:
        loadout = combatant.weapons[slot]
    except KeyError as exc:
        raise KeyError(f"Combatant '{combatant.id}' has no weapon in slot '{slot}'.") from exc

    weapon = get_weapon_definition(loadout.weapon_id)
    rating = combatant.competencies.get(loadout.competency)
    return OffenseContext(
        slot=slot,
        weapon_id=loadout.weapon_id,
        competency=loadout.competency,
        weapon=weapon,
        characteristic_modifier=characteristic_value(combatant.characteristics, weapon.characteristic),
        competency_level=0 if rating is None else rating.level,
        competency_rank=None if rating is None else rating.rank,
        weapon_grade=loadout.grade,
        base_potency=loadout.base_potency,
        bonus_modifier=bonus_modifier,
        penalty_modifier=penalty_modifier,
    )


def attack_roll_for_weapon(
    *,
    combatant: Combatant,
    rng: SimulationRNG,
    slot: str = "primary",
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
):
    """Resolve a canonical A.R. from one equipped weapon slot."""

    context = build_offense_context(
        combatant=combatant,
        slot=slot,
        bonus_modifier=bonus_modifier,
        penalty_modifier=penalty_modifier,
    )
    return attack_roll(
        competency=context.competency,
        level=context.competency_level,
        rank=context.competency_rank,
        rng=rng,
        characteristic_modifier=context.characteristic_modifier,
        bonus_modifier=context.bonus_modifier,
        penalty_modifier=context.penalty_modifier,
    )


def impact_roll_for_weapon(
    *,
    combatant: Combatant,
    rng: SimulationRNG,
    slot: str = "primary",
) -> ImpactRollValue:
    """Resolve a canonical trained or untrained I.R. from one equipped weapon slot."""

    context = build_offense_context(combatant=combatant, slot=slot)
    rank_number = rank_bonus(context.competency_rank)
    die_size = _die_size(context.weapon.damage_die)
    if rank_number <= 0:
        roll = rng.randint(1, die_size)
        total = (roll + (context.characteristic_modifier * context.weapon_grade)) / 2
        return ImpactRollValue(
            rolls=(roll,),
            weapon_die=context.weapon.damage_die,
            rank_number=1,
            characteristic_modifier=context.characteristic_modifier,
            weapon_grade=context.weapon_grade,
            total=int(total),
            critical_roll=roll,
            critical_face=die_size,
            critical_impact=roll == die_size,
            untrained=True,
        )

    rolls = tuple(rng.randint(1, die_size) for _ in range(rank_number))
    critical_roll = rolls[0]
    total = sum(rolls) + (context.characteristic_modifier * context.weapon_grade)
    return ImpactRollValue(
        rolls=rolls,
        weapon_die=context.weapon.damage_die,
        rank_number=rank_number,
        characteristic_modifier=context.characteristic_modifier,
        weapon_grade=context.weapon_grade,
        total=total,
        critical_roll=critical_roll,
        critical_face=die_size,
        critical_impact=critical_roll == die_size,
        untrained=False,
    )

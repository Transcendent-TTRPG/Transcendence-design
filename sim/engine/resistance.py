"""Resistance-family runtime helpers."""

from __future__ import annotations

from dataclasses import dataclass

from models import Combatant

from .dice import characteristic_value, resistance_characteristic, resistance_roll
from .rng import SimulationRNG


@dataclass(frozen=True)
class ResistanceContext:
    """Resolved runtime context for one resistance family on one combatant."""

    family: str
    base_characteristic: str
    characteristic_modifier: int
    resistance_level: int
    resistance_rank: str | None
    bonus_modifier: int
    penalty_modifier: int


def build_resistance_context(
    *,
    combatant: Combatant,
    family: str,
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
) -> ResistanceContext:
    """Resolve one resistance family into its base characteristic and trained contribution."""

    base_characteristic = resistance_characteristic(family)
    rating = combatant.competencies.get(family)
    return ResistanceContext(
        family=family,
        base_characteristic=base_characteristic,
        characteristic_modifier=characteristic_value(combatant.characteristics, base_characteristic),
        resistance_level=0 if rating is None else rating.level,
        resistance_rank=None if rating is None else rating.rank,
        bonus_modifier=bonus_modifier,
        penalty_modifier=penalty_modifier,
    )


def resistance_roll_for_family(
    *,
    combatant: Combatant,
    family: str,
    rng: SimulationRNG,
    bonus_modifier: int = 0,
    penalty_modifier: int = 0,
):
    """Resolve a canonical R.R. for one resistance family."""

    context = build_resistance_context(
        combatant=combatant,
        family=family,
        bonus_modifier=bonus_modifier,
        penalty_modifier=penalty_modifier,
    )
    return resistance_roll(
        competency=context.family,
        level=context.resistance_level,
        rank=context.resistance_rank,
        rng=rng,
        characteristic_modifier=context.characteristic_modifier,
        bonus_modifier=context.bonus_modifier,
        penalty_modifier=context.penalty_modifier,
    )

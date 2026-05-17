"""Minimal combat exchange runner for weapon attack vs defended zone."""

from __future__ import annotations

from dataclasses import dataclass

from models import Combatant

from .block import ZoneBlockContext, zone_block_for_combatant
from .defense import DefenseContext, defense_roll_for_zone, build_defense_context
from .dice import OpposedOutcome, RollValue, resolve_opposed
from .offense import ImpactRollValue, OffenseContext, attack_roll_for_weapon, build_offense_context, impact_roll_for_weapon
from .rng import SimulationRNG


@dataclass(frozen=True)
class ExchangeResult:
    """Resolved minimal exchange result."""

    attacker_id: str
    defender_id: str
    zone: str
    offense_context: OffenseContext
    defense_context: DefenseContext
    block_context: ZoneBlockContext
    attack_roll: RollValue
    defense_roll: RollValue
    opposed: OpposedOutcome
    impact_roll: ImpactRollValue | None
    attack_connected: bool
    effective_damage: int


def resolve_weapon_exchange(
    *,
    attacker: Combatant,
    defender: Combatant,
    zone: str,
    rng: SimulationRNG,
    attack_slot: str = "primary",
    attack_bonus: int = 0,
    attack_penalty: int = 0,
    defense_bonus: int = 0,
    defense_penalty: int = 0,
) -> ExchangeResult:
    """Resolve A.R. -> D.R. -> I.R. -> Block -> effective damage."""

    offense_context = build_offense_context(
        combatant=attacker,
        slot=attack_slot,
        bonus_modifier=attack_bonus,
        penalty_modifier=attack_penalty,
    )
    defense_context = build_defense_context(
        combatant=defender,
        zone=zone,
        bonus_modifier=defense_bonus,
        penalty_modifier=defense_penalty,
    )
    block_context = zone_block_for_combatant(combatant=defender, zone=zone)

    ar = attack_roll_for_weapon(
        combatant=attacker,
        rng=rng,
        slot=attack_slot,
        bonus_modifier=attack_bonus,
        penalty_modifier=attack_penalty,
    )
    dr = defense_roll_for_zone(
        combatant=defender,
        zone=zone,
        rng=rng,
        bonus_modifier=defense_bonus,
        penalty_modifier=defense_penalty,
    )
    opposed = resolve_opposed(ar, dr)
    if not opposed.attacker_wins:
        return ExchangeResult(
            attacker_id=attacker.id,
            defender_id=defender.id,
            zone=zone,
            offense_context=offense_context,
            defense_context=defense_context,
            block_context=block_context,
            attack_roll=ar,
            defense_roll=dr,
            opposed=opposed,
            impact_roll=None,
            attack_connected=False,
            effective_damage=0,
        )

    ir = impact_roll_for_weapon(combatant=attacker, rng=rng, slot=attack_slot)
    effective_damage = max(0, ir.total - block_context.total_block)
    return ExchangeResult(
        attacker_id=attacker.id,
        defender_id=defender.id,
        zone=zone,
        offense_context=offense_context,
        defense_context=defense_context,
        block_context=block_context,
        attack_roll=ar,
        defense_roll=dr,
        opposed=opposed,
        impact_roll=ir,
        attack_connected=True,
        effective_damage=effective_damage,
    )

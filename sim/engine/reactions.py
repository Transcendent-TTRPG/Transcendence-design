"""Runtime reaction handling for incoming combat exchanges."""

from __future__ import annotations

from dataclasses import dataclass

from loaders import load_action_definitions
from models import ActionDefinition
from policies import AttackReactionQuery, get_policy

from .ailments_runtime import reaction_gate
from .entities import ExperimentContext
from .timeline import TimelineAdvanceResult, spend_timeline_cost


@dataclass(frozen=True)
class ReactionExecutionResult:
    """Resolved runtime reaction to one incoming attack."""

    actor_id: str
    actor_slot: str
    definition_id: str
    applied: bool
    defense_bonus: int = 0
    timeline_result: TimelineAdvanceResult | None = None
    notes: tuple[str, ...] = ()


def _actions_by_id() -> dict[str, ActionDefinition]:
    return {entry.id: entry for entry in load_action_definitions()}


def resolve_attack_reaction(
    *,
    context: ExperimentContext,
    attacker_slot: str,
    defender_slot: str,
    zone: str,
) -> ReactionExecutionResult | None:
    """Resolve one policy-driven defensive reaction to an incoming attack."""

    defender_entry = context.actors_by_slot[defender_slot]
    policy = get_policy(defender_entry.policy_id)
    if policy is None:
        return None

    intent = policy.choose_attack_reaction(
        context=context,
        query=AttackReactionQuery(
            defender_slot=defender_slot,
            attacker_slot=attacker_slot,
            zone=zone,
        ),
    )
    if intent is None:
        return None

    definition = _actions_by_id()[intent.definition_id]
    if definition.trigger_type != "reactive":
        raise ValueError(f"Action '{definition.id}' is not reactive and cannot be used as a reaction.")

    gate = reaction_gate(
        combatant=defender_entry.combatant,
        timing_sensitive=True,
    )
    if not gate.allowed:
        return ReactionExecutionResult(
            actor_id=defender_entry.combatant.id,
            actor_slot=defender_slot,
            definition_id=definition.id,
            applied=False,
            notes=gate.notes,
        )

    defense_bonus = 0
    for effect in definition.effects:
        if effect.id == "reaction_defense_bonus":
            defense_bonus += int(effect.parameters.get("bonus", 0))

    timeline_result = spend_timeline_cost(
        combatant=defender_entry.combatant,
        rhythm_cost=definition.rhythm,
        attrition_cost=definition.attrition,
        as_reaction=True,
    )
    return ReactionExecutionResult(
        actor_id=defender_entry.combatant.id,
        actor_slot=defender_slot,
        definition_id=definition.id,
        applied=True,
        defense_bonus=defense_bonus,
        timeline_result=timeline_result,
        notes=("defensive_reaction_applied",),
    )

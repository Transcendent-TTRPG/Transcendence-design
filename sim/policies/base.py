"""Base policy interfaces and registry for ATB action/reaction selection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class AttackReactionQuery:
    """Minimal query context for deciding a reaction to one incoming attack."""

    defender_slot: str
    attacker_slot: str
    zone: str


class Policy(Protocol):
    """Decision surface for one simulation policy."""

    id: str

    def choose_activation_intent(self, *, context, actor_slot: str):
        """Return the next activation intent for this actor."""

    def choose_attack_reaction(self, *, context, query: AttackReactionQuery):
        """Return the next reaction intent for an incoming attack, or None."""


_POLICY_REGISTRY: dict[str, Policy] = {}


def first_enemy_slot(context, actor_slot: str) -> str | None:
    """Return the first enemy slot visible to a policy."""

    actor_side = context.actors_by_slot[actor_slot].combatant.side
    for entry in context.actors:
        if entry.slot != actor_slot and entry.combatant.side != actor_side:
            return entry.slot
    return None


def has_active_ailment(combatant, ailment_id: str) -> bool:
    """Check whether one ailment is currently active."""

    return any(ailment.ailment_id == ailment_id and ailment.active for ailment in combatant.ailments)


def highest_priority_recovery_ailment(combatant) -> str | None:
    """Choose the most urgent recoverable ailment for policy use."""

    severity_weight = {
        "severe": 3,
        "moderate": 2,
        "minor": 1,
    }
    priority_weight = {
        "aturdido": 30,
        "conmocionado": 20,
        "aterrorizado": 10,
    }
    ranked: list[tuple[int, str]] = []
    for ailment in combatant.ailments:
        if not ailment.active:
            continue
        if ailment.ailment_id not in priority_weight:
            continue
        ranked.append(
            (
                priority_weight[ailment.ailment_id] + severity_weight.get(ailment.severity.casefold(), 0),
                ailment.ailment_id,
            )
        )
    if not ranked:
        return None
    ranked.sort(reverse=True)
    return ranked[0][1]


def should_attempt_recovery(combatant) -> bool:
    """Return whether a policy should spend an activation on recovery."""

    if combatant.attrition_spent >= 6:
        return False
    for ailment in combatant.ailments:
        if not ailment.active:
            continue
        if ailment.severity.casefold() in {"severe", "moderate"} and ailment.ailment_id in {"aturdido", "conmocionado", "aterrorizado"}:
            return True
    return False


def has_hidden_against_slot(context, *, actor_slot: str, observer_slot: str) -> bool:
    """Check whether actor currently has Hidden against one observer slot."""

    actor = context.actors_by_slot[actor_slot].combatant
    observer_id = context.actors_by_slot[observer_slot].combatant.id
    return any(
        state.observer_id == observer_id and state.valid
        for state in actor.concealment_states
    )


def register_policy(policy: Policy) -> Policy:
    """Register one policy instance for runtime lookup."""

    _POLICY_REGISTRY[policy.id] = policy
    return policy


def get_policy(policy_id: str | None) -> Policy | None:
    """Return one registered policy instance by id."""

    if policy_id is None:
        return None
    return _POLICY_REGISTRY.get(policy_id)

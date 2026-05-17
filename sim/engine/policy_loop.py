"""Policy-driven ATB loop helpers."""

from __future__ import annotations

from dataclasses import dataclass

from policies import get_policy

from .activations import ActivationExecutionResult, execute_activation_intent
from .entities import ExperimentContext
from .rng import SimulationRNG
from .timeline import next_ready_combatant


@dataclass(frozen=True)
class PolicyStepResult:
    """One policy-selected ATB step."""

    ready_actor_id: str
    ready_actor_slot: str
    execution: ActivationExecutionResult


def run_policy_step(
    *,
    context: ExperimentContext,
    rng: SimulationRNG,
) -> PolicyStepResult:
    """Resolve one ATB step by asking the ready actor's policy for an intent."""

    ready = next_ready_combatant(tuple(entry.combatant for entry in context.actors))
    ready_entry = next(entry for entry in context.actors if entry.combatant.id == ready.id)
    policy = get_policy(ready_entry.policy_id)
    if policy is None:
        raise ValueError(f"Actor slot '{ready_entry.slot}' has no registered policy '{ready_entry.policy_id}'.")

    intent = policy.choose_activation_intent(
        context=context,
        actor_slot=ready_entry.slot,
    )
    execution = execute_activation_intent(
        context=context,
        intent=intent,
        rng=rng,
    )
    return PolicyStepResult(
        ready_actor_id=ready.id,
        ready_actor_slot=ready_entry.slot,
        execution=execution,
    )

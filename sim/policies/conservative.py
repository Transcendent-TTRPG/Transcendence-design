"""Conservative policy."""

from __future__ import annotations

from dataclasses import dataclass

from .base import AttackReactionQuery, first_enemy_slot, highest_priority_recovery_ailment, register_policy, should_attempt_recovery


@dataclass(frozen=True)
class ConservativePolicy:
    """Prefer ordinary attacks on activation and defensive reactions on intake."""

    id: str = "conservative"

    def choose_activation_intent(self, *, context, actor_slot: str):
        from engine.activations import ActivationIntent

        actor = context.actors_by_slot[actor_slot].combatant
        if should_attempt_recovery(actor):
            ailment_id = highest_priority_recovery_ailment(actor)
            if ailment_id is not None:
                return ActivationIntent(
                    actor_slot=actor_slot,
                    mode="recovery",
                    definition_id="recover",
                    ailment_id=ailment_id,
                )

        target_slot = first_enemy_slot(context, actor_slot)
        if target_slot is not None:
            return ActivationIntent(
                actor_slot=actor_slot,
                mode="action",
                definition_id="attack_one_handed",
                target_slot=target_slot,
                zone="torso",
            )
        return ActivationIntent(
            actor_slot=actor_slot,
            mode="action",
            definition_id="focus_task",
        )

    def choose_attack_reaction(self, *, context, query: AttackReactionQuery):
        from engine.activations import ActivationIntent

        defender = context.actors_by_slot[query.defender_slot].combatant
        if defender.attrition_spent >= 4:
            return None
        if should_attempt_recovery(defender):
            return None
        return ActivationIntent(
            actor_slot=query.defender_slot,
            mode="action",
            definition_id="brace_for_impact",
        )


register_policy(ConservativePolicy())

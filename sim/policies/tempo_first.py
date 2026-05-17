"""Tempo-first policy."""

from __future__ import annotations

from dataclasses import dataclass

from .base import (
    AttackReactionQuery,
    first_enemy_slot,
    has_active_ailment,
    highest_priority_recovery_ailment,
    register_policy,
    should_attempt_recovery,
)


@dataclass(frozen=True)
class TempoFirstPolicy:
    """Prefer immediate tempo-positive progress over defensive holds."""

    id: str = "tempo_first"

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
            target = context.actors_by_slot[target_slot].combatant
            if "reir_donde_mas_suena" in actor.techniques and not has_active_ailment(target, "aterrorizado"):
                return ActivationIntent(
                    actor_slot=actor_slot,
                    mode="technique",
                    definition_id="reir_donde_mas_suena",
                    target_slot=target_slot,
                )
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
        return None


register_policy(TempoFirstPolicy())

"""Stealth-crossing policy."""

from __future__ import annotations

from dataclasses import dataclass

from .base import (
    AttackReactionQuery,
    first_enemy_slot,
    has_active_ailment,
    has_hidden_against_slot,
    highest_priority_recovery_ailment,
    register_policy,
    should_attempt_recovery,
)


@dataclass(frozen=True)
class StealthCrosserPolicy:
    """Try to gain Hidden first, then shift into direct action."""

    id: str = "stealth_crosser"

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

        observer_slot = first_enemy_slot(context, actor_slot)
        if observer_slot is not None:
            target = context.actors_by_slot[observer_slot].combatant
            has_hidden = has_hidden_against_slot(
                context,
                actor_slot=actor_slot,
                observer_slot=observer_slot,
            )
            if "pasar_como_parte_del_fondo" in actor.techniques and not has_hidden:
                return ActivationIntent(
                    actor_slot=actor_slot,
                    mode="technique",
                    definition_id="pasar_como_parte_del_fondo",
                    observer_slot=observer_slot,
                )
            if has_hidden and "reir_donde_mas_suena" in actor.techniques and not has_active_ailment(target, "aterrorizado"):
                return ActivationIntent(
                    actor_slot=actor_slot,
                    mode="technique",
                    definition_id="reir_donde_mas_suena",
                    target_slot=observer_slot,
                )
            return ActivationIntent(
                actor_slot=actor_slot,
                mode="action",
                definition_id="attack_one_handed",
                target_slot=observer_slot,
                zone="torso",
            )
        return ActivationIntent(
            actor_slot=actor_slot,
            mode="action",
            definition_id="focus_task",
        )

    def choose_attack_reaction(self, *, context, query: AttackReactionQuery):
        return None


register_policy(StealthCrosserPolicy())

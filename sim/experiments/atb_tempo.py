"""ATB tempo helpers built on top of the timeline runtime."""

from __future__ import annotations

from dataclasses import dataclass

from engine.entities import ExperimentContext
from engine.timeline import TimelineAdvanceResult, TimelineInitializationResult, initialize_timeline, next_ready_combatant, spend_timeline_cost


@dataclass(frozen=True)
class ATBTempoSnapshot:
    """Minimal reusable view of one initialized ATB slice."""

    initialization: TimelineInitializationResult
    next_ready_actor_id: str
    positions: dict[str, int]


def initialize_context_timeline(
    context: ExperimentContext,
    *,
    situational_modifiers_by_slot: dict[str, int] | None = None,
) -> ATBTempoSnapshot:
    """Initialize ATB positions for one instantiated experiment context."""

    situational_modifiers_by_slot = situational_modifiers_by_slot or {}
    modifiers_by_actor_id = {
        actor.combatant.id: situational_modifiers_by_slot.get(actor.slot, 0)
        for actor in context.actors
    }
    combatants = tuple(actor.combatant for actor in context.actors)
    initialization = initialize_timeline(
        combatants=combatants,
        situational_modifiers=modifiers_by_actor_id,
    )
    next_ready = next_ready_combatant(combatants)
    return ATBTempoSnapshot(
        initialization=initialization,
        next_ready_actor_id=next_ready.id,
        positions={
            actor.slot: actor.combatant.timeline.track_position or 0
            for actor in context.actors
        },
    )


def apply_tempo_step(
    context: ExperimentContext,
    *,
    acting_slot: str,
    rhythm_cost: int,
    attrition_cost: int = 0,
    as_reaction: bool = False,
) -> TimelineAdvanceResult:
    """Advance one actor already present in an initialized ATB context."""

    actor = context.actors_by_slot[acting_slot]
    return spend_timeline_cost(
        combatant=actor.combatant,
        rhythm_cost=rhythm_cost,
        attrition_cost=attrition_cost,
        as_reaction=as_reaction,
    )

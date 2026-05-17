"""ATB timeline initialization and progression helpers."""

from __future__ import annotations

from dataclasses import dataclass

from models import Combatant, TimelineState
from .ailments_runtime import effective_preparation


@dataclass(frozen=True)
class TimelineOpeningEntry:
    """Opening-value and initial-position data for one combatant."""

    actor_id: str
    raw_preparation: int
    situational_modifier: int
    opening_value: int
    initial_position: int


@dataclass(frozen=True)
class TimelineInitializationResult:
    """Resolved initial ATB placement for one encounter slice."""

    reference_point: int
    entries: tuple[TimelineOpeningEntry, ...]

    @property
    def ordered_actor_ids(self) -> tuple[str, ...]:
        return tuple(
            entry.actor_id
            for entry in sorted(
                self.entries,
                key=lambda entry: (entry.initial_position, -entry.raw_preparation, entry.actor_id),
            )
        )


@dataclass(frozen=True)
class TimelineAdvanceResult:
    """Result of spending rhythm/attrition on the ATB track."""

    actor_id: str
    track_before: int
    track_after: int
    rhythm_cost: int
    attrition_before: int
    attrition_after: int
    as_reaction: bool
    activation_count: int
    reaction_count: int


def opening_value(*, preparation: int, situational_modifier: int = 0) -> int:
    """Return canonical opening value for initial ATB placement."""

    return preparation + situational_modifier


def initialize_timeline(
    *,
    combatants: tuple[Combatant, ...] | list[Combatant],
    situational_modifiers: dict[str, int] | None = None,
) -> TimelineInitializationResult:
    """Assign canonical initial track positions from preparation and situation."""

    situational_modifiers = situational_modifiers or {}
    entries: list[TimelineOpeningEntry] = []
    reference_point = 0
    opening_values: dict[str, int] = {}

    for combatant in combatants:
        modifier = situational_modifiers.get(combatant.id, 0)
        value = opening_value(
            preparation=effective_preparation(combatant),
            situational_modifier=modifier,
        )
        opening_values[combatant.id] = value
        reference_point = max(reference_point, value)

    for combatant in combatants:
        modifier = situational_modifiers.get(combatant.id, 0)
        value = opening_values[combatant.id]
        initial_position = reference_point - value
        combatant.timeline = TimelineState(
            preparation=combatant.timeline.preparation,
            track_position=initial_position,
            pending_activation=False,
            lost_activation=combatant.timeline.lost_activation,
            activations_taken=combatant.timeline.activations_taken,
            reactions_taken=combatant.timeline.reactions_taken,
            last_rhythm_cost=combatant.timeline.last_rhythm_cost,
            notes=combatant.timeline.notes,
        )
        entries.append(
            TimelineOpeningEntry(
                actor_id=combatant.id,
                raw_preparation=effective_preparation(combatant),
                situational_modifier=modifier,
                opening_value=value,
                initial_position=initial_position,
            )
        )

    return TimelineInitializationResult(
        reference_point=reference_point,
        entries=tuple(entries),
    )


def next_ready_combatant(
    combatants: tuple[Combatant, ...] | list[Combatant],
) -> Combatant:
    """Return the leftmost combatant, using raw Preparation as ATB tiebreak."""

    initialized = [combatant for combatant in combatants if combatant.timeline.track_position is not None]
    if not initialized:
        raise ValueError("No combatants have initialized ATB track positions.")

    return min(
        initialized,
        key=lambda combatant: (
            combatant.timeline.track_position,
            -combatant.timeline.preparation,
            combatant.id,
        ),
    )


def spend_timeline_cost(
    *,
    combatant: Combatant,
    rhythm_cost: int,
    attrition_cost: int = 0,
    as_reaction: bool = False,
) -> TimelineAdvanceResult:
    """Advance one combatant on the ATB track after an action or reaction."""

    if combatant.timeline.track_position is None:
        raise ValueError(f"Combatant '{combatant.id}' has no initialized ATB position.")

    track_before = combatant.timeline.track_position
    attrition_before = combatant.attrition_spent
    activation_count = combatant.timeline.activations_taken + (0 if as_reaction else 1)
    reaction_count = combatant.timeline.reactions_taken + (1 if as_reaction else 0)
    combatant.attrition_spent += attrition_cost
    combatant.timeline = TimelineState(
        preparation=combatant.timeline.preparation,
        track_position=track_before + rhythm_cost,
        pending_activation=False,
        lost_activation=combatant.timeline.lost_activation,
        activations_taken=activation_count,
        reactions_taken=reaction_count,
        last_rhythm_cost=rhythm_cost,
        notes=combatant.timeline.notes,
    )

    return TimelineAdvanceResult(
        actor_id=combatant.id,
        track_before=track_before,
        track_after=track_before + rhythm_cost,
        rhythm_cost=rhythm_cost,
        attrition_before=attrition_before,
        attrition_after=combatant.attrition_spent,
        as_reaction=as_reaction,
        activation_count=activation_count,
        reaction_count=reaction_count,
    )


def mark_pending_activation(*, combatant: Combatant, pending: bool = True) -> None:
    """Mark whether a combatant is currently the ready entity in the ATB flow."""

    combatant.timeline = TimelineState(
        preparation=combatant.timeline.preparation,
        track_position=combatant.timeline.track_position,
        pending_activation=pending,
        lost_activation=combatant.timeline.lost_activation,
        activations_taken=combatant.timeline.activations_taken,
        reactions_taken=combatant.timeline.reactions_taken,
        last_rhythm_cost=combatant.timeline.last_rhythm_cost,
        notes=combatant.timeline.notes,
    )

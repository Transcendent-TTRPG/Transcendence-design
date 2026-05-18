"""Runtime support for non-ailment procedural states."""

from __future__ import annotations

from dataclasses import dataclass

from models import Combatant, ProceduralState


@dataclass(frozen=True)
class ProceduralStateApplicationResult:
    """Result of applying one procedural state."""

    state_id: str
    applied: bool


@dataclass(frozen=True)
class ProceduralStateExpiryResult:
    """Result of expiring procedural states after one activation end."""

    cleared_states: tuple[str, ...]
    remaining_states: tuple[str, ...]


def apply_procedural_state(
    *,
    target: Combatant,
    source_id: str | None,
    state_id: str,
    source_rank_bonus: int,
    applies_to: tuple[str, ...] = (),
    remaining_uses: int | None = None,
    expires_on_owner_activation_end: int | None = None,
    expires_on_source_activation_end: int | None = None,
    notes: tuple[str, ...] = (),
) -> ProceduralStateApplicationResult:
    """Apply or refresh one procedural state on a combatant."""

    new_state = ProceduralState(
        state_id=state_id,
        source_id=source_id,
        source_rank_bonus=source_rank_bonus,
        active=True,
        applies_to=applies_to,
        remaining_uses=remaining_uses,
        expires_on_owner_activation_end=expires_on_owner_activation_end,
        expires_on_source_activation_end=expires_on_source_activation_end,
        notes=notes,
    )
    for index, current in enumerate(target.procedural_states):
        if current.state_id == state_id and current.source_id == source_id:
            target.procedural_states[index] = new_state
            return ProceduralStateApplicationResult(state_id=state_id, applied=True)

    target.procedural_states.append(new_state)
    return ProceduralStateApplicationResult(state_id=state_id, applied=True)


def procedural_roll_penalty(
    *,
    combatant: Combatant,
    roll_tag: str,
    against_source_id: str | None,
) -> int:
    """Return and consume procedural penalties for one direct opposed roll."""

    total = 0
    updated: list[ProceduralState] = []
    for state in combatant.procedural_states:
        if not state.active:
            updated.append(state)
            continue
        if against_source_id is not None and state.source_id != against_source_id:
            updated.append(state)
            continue
        if roll_tag not in state.applies_to:
            updated.append(state)
            continue

        total += state.source_rank_bonus
        if state.remaining_uses is None:
            updated.append(state)
            continue
        remaining = state.remaining_uses - 1
        if remaining > 0:
            updated.append(
                ProceduralState(
                    state_id=state.state_id,
                    source_id=state.source_id,
                    source_rank_bonus=state.source_rank_bonus,
                    active=True,
                    applies_to=state.applies_to,
                    remaining_uses=remaining,
                    expires_on_owner_activation_end=state.expires_on_owner_activation_end,
                    expires_on_source_activation_end=state.expires_on_source_activation_end,
                    notes=state.notes,
                )
            )

    combatant.procedural_states = updated
    return total


def procedural_block_ignore(
    *,
    attacker: Combatant,
    defender: Combatant,
) -> int:
    """Return and consume block-ignore states authored on the defender against this attacker."""

    total = 0
    updated: list[ProceduralState] = []
    for state in defender.procedural_states:
        if not state.active or state.source_id != attacker.id or state.state_id != "seam_opened":
            updated.append(state)
            continue
        total += state.source_rank_bonus
        if state.remaining_uses is None:
            updated.append(state)
            continue
        remaining = state.remaining_uses - 1
        if remaining > 0:
            updated.append(
                ProceduralState(
                    state_id=state.state_id,
                    source_id=state.source_id,
                    source_rank_bonus=state.source_rank_bonus,
                    active=True,
                    applies_to=state.applies_to,
                    remaining_uses=remaining,
                    expires_on_owner_activation_end=state.expires_on_owner_activation_end,
                    expires_on_source_activation_end=state.expires_on_source_activation_end,
                    notes=state.notes,
                )
            )

    defender.procedural_states = updated
    return total


def resolve_procedural_state_expiry(
    *,
    combatants: tuple[Combatant, ...] | list[Combatant],
    actor: Combatant,
) -> ProceduralStateExpiryResult:
    """Expire owner- and source-timed procedural states at one activation end."""

    cleared: list[str] = []
    remaining: list[str] = []
    for combatant in combatants:
        updated: list[ProceduralState] = []
        for state in combatant.procedural_states:
            owner_expired = (
                combatant.id == actor.id
                and state.expires_on_owner_activation_end is not None
                and actor.timeline.activations_taken >= state.expires_on_owner_activation_end
            )
            source_expired = (
                state.source_id == actor.id
                and state.expires_on_source_activation_end is not None
                and actor.timeline.activations_taken >= state.expires_on_source_activation_end
            )
            if owner_expired or source_expired:
                cleared.append(state.state_id)
                continue
            updated.append(state)
            remaining.append(state.state_id)
        combatant.procedural_states = updated

    return ProceduralStateExpiryResult(
        cleared_states=tuple(cleared),
        remaining_states=tuple(remaining),
    )

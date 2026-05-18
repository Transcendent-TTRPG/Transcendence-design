"""Declarative effect application helpers for actions, techniques, and exchanges."""

from __future__ import annotations

from dataclasses import dataclass

from models import Combatant, ConcealmentState, EffectDefinition

from .ailments_runtime import apply_ailment
from .dice import rank_bonus
from .procedural_states import apply_procedural_state


@dataclass(frozen=True)
class EffectApplicationResult:
    """Resolved result of one declarative effect application."""

    effect_id: str
    applied: bool
    state_changes: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()


def _upsert_concealment_state(
    *,
    owner: Combatant,
    observer_id: str,
    state_id: str,
    active_value: int | float | None,
    acquisition_source: str | None,
    break_conditions: tuple[str, ...] = (),
) -> None:
    for index, state in enumerate(owner.concealment_states):
        if state.owner_id == owner.id and state.observer_id == observer_id and state.state_id == state_id:
            owner.concealment_states[index] = ConcealmentState(
                owner_id=owner.id,
                observer_id=observer_id,
                state_id=state_id,
                active_value=active_value,
                acquisition_source=acquisition_source,
                valid=True,
                break_conditions=break_conditions,
                notes=state.notes,
            )
            return

    owner.concealment_states.append(
        ConcealmentState(
            owner_id=owner.id,
            observer_id=observer_id,
            state_id=state_id,
            active_value=active_value,
            acquisition_source=acquisition_source,
            valid=True,
            break_conditions=break_conditions,
        )
    )


def apply_effect_definition(
    *,
    effect: EffectDefinition,
    source: Combatant,
    target: Combatant,
    source_competency: str | None = None,
    source_rank_bonus_override: int | None = None,
    activation_index: int | None = None,
    observer_id: str | None = None,
    active_value: int | float | None = None,
) -> EffectApplicationResult:
    """Apply one declarative effect to the relevant runtime target."""

    if effect.id in {"grant_hidden_state", "grant_hidden_state_limited"}:
        if observer_id is None:
            raise ValueError(f"Effect '{effect.id}' requires observer_id.")
        state_id = str(effect.parameters.get("state_id", "hidden_state"))
        break_conditions = ()
        model = effect.parameters.get("model") or effect.parameters.get("scope")
        if model is not None:
            break_conditions = (str(model),)
        _upsert_concealment_state(
            owner=target,
            observer_id=observer_id,
            state_id=state_id,
            active_value=active_value,
            acquisition_source=effect.id,
            break_conditions=break_conditions,
        )
        return EffectApplicationResult(
            effect_id=effect.id,
            applied=True,
            state_changes=(f"grant:{state_id}",),
        )

    if effect.id == "apply_ailment":
        ailment_id = str(effect.parameters["ailment_id"])
        severity = str(effect.parameters["severity"])
        source_rank_bonus = source_rank_bonus_override
        if source_rank_bonus is None:
            competency_id = effect.parameters.get("source_competency") or source_competency
            if competency_id is None:
                source_rank_bonus = 0
            else:
                rating = source.competencies.get(str(competency_id))
                source_rank_bonus = 0 if rating is None else rank_bonus(rating.rank)
        result = apply_ailment(
            combatant=target,
            ailment_id=ailment_id,
            severity=severity,
            source_id=source.id,
            source_rank_bonus=source_rank_bonus,
            applied_on_activation=activation_index,
        )
        return EffectApplicationResult(
            effect_id=effect.id,
            applied=result.applied_new or result.replaced_existing or result.refreshed_existing,
            state_changes=(f"ailment:{ailment_id}:{severity}",),
            notes=(
                "applied_new" if result.applied_new else "replaced_existing" if result.replaced_existing else "refreshed_existing" if result.refreshed_existing else "ignored_weaker_application",
            ),
        )

    if effect.id == "apply_procedural_state":
        state_id = str(effect.parameters["state_id"])
        source_rank_bonus = source_rank_bonus_override
        if source_rank_bonus is None:
            competency_id = effect.parameters.get("source_competency") or source_competency
            if competency_id is None:
                source_rank_bonus = 0
            else:
                rating = source.competencies.get(str(competency_id))
                source_rank_bonus = 0 if rating is None else rank_bonus(rating.rank)
        owner_expiry_delta = effect.parameters.get("expires_on_owner_activation_end_after")
        source_expiry_delta = effect.parameters.get("expires_on_source_activation_end_after")
        owner_expiry = None if owner_expiry_delta is None else target.timeline.activations_taken + int(owner_expiry_delta)
        source_expiry = None if source_expiry_delta is None else source.timeline.activations_taken + int(source_expiry_delta)
        result = apply_procedural_state(
            target=target,
            source_id=source.id,
            state_id=state_id,
            source_rank_bonus=source_rank_bonus,
            applies_to=tuple(str(entry) for entry in effect.parameters.get("applies_to", ())),
            remaining_uses=effect.parameters.get("remaining_uses"),
            expires_on_owner_activation_end=owner_expiry,
            expires_on_source_activation_end=source_expiry,
        )
        return EffectApplicationResult(
            effect_id=effect.id,
            applied=result.applied,
            state_changes=(f"procedural:{state_id}",),
        )

    return EffectApplicationResult(
        effect_id=effect.id,
        applied=False,
        notes=("unsupported_effect_id",),
    )


def apply_effects(
    *,
    effects: tuple[EffectDefinition, ...] | list[EffectDefinition],
    source: Combatant,
    target: Combatant,
    source_competency: str | None = None,
    source_rank_bonus_override: int | None = None,
    activation_index: int | None = None,
    observer_id: str | None = None,
    active_value: int | float | None = None,
) -> tuple[EffectApplicationResult, ...]:
    """Apply a batch of declarative effects."""

    return tuple(
        apply_effect_definition(
            effect=effect,
            source=source,
            target=target,
            source_competency=source_competency,
            source_rank_bonus_override=source_rank_bonus_override,
            activation_index=activation_index,
            observer_id=observer_id,
            active_value=active_value,
        )
        for effect in effects
    )

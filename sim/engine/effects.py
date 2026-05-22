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


SUPPORTED_EFFECT_IDS: frozenset[str] = frozenset({
    # Handled here by apply_effect_definition
    "grant_hidden_state",
    "grant_hidden_state_limited",
    "apply_ailment",
    "apply_procedural_state",
    "mark_immediate_route_readable",
    "blur_declared_sensory_channel",
    "deny_clean_separation_if_check_succeeds",
    # Handled at exchange/activation level in engine/activations.py
    "weapon_exchange_primary",
    "indirect_surface_ranged_attack",
    "false_line_combined_resolution",
    "utility_check_primary",
    "same_exchange_ignore_block_rank_bonus",
    "reposition_after_hit_half_move",
    "reposition_after_hit_distance",
    "advance_before_exchange_distance",
    "reduce_target_movement_rank_bonus",
})


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
            expires_on_fiction_events=tuple(str(entry) for entry in effect.parameters.get("expires_on_fiction_events", ())),
        )
        return EffectApplicationResult(
            effect_id=effect.id,
            applied=result.applied,
            state_changes=(f"procedural:{state_id}",),
        )

    if effect.id == "mark_immediate_route_readable":
        state_id = str(effect.parameters.get("state_id", "read_marked"))
        source_rank_bonus = source_rank_bonus_override
        if source_rank_bonus is None:
            competency_id = source_competency
            if competency_id is None:
                source_rank_bonus = 0
            else:
                rating = source.competencies.get(str(competency_id))
                source_rank_bonus = 0 if rating is None else rank_bonus(rating.rank)
        result = apply_procedural_state(
            target=target,
            source_id=source.id,
            state_id=state_id,
            source_rank_bonus=source_rank_bonus,
            expires_on_fiction_events=("movement_resolved", "concealment_resolved", "mark_cleared", "interact_cleanup"),
            notes=("route_readability_preserved",),
        )
        return EffectApplicationResult(
            effect_id=effect.id,
            applied=result.applied,
            state_changes=(f"procedural:{state_id}",),
            notes=("route_readability_state_installed",),
        )

    if effect.id == "blur_declared_sensory_channel":
        state_id = str(effect.parameters.get("state_id", "signal_blurred"))
        source_rank_bonus = source_rank_bonus_override
        if source_rank_bonus is None:
            competency_id = source_competency
            if competency_id is None:
                source_rank_bonus = 0
            else:
                rating = source.competencies.get(str(competency_id))
                source_rank_bonus = 0 if rating is None else rank_bonus(rating.rank)
        cleanup_path = str(effect.parameters.get("cleanup_path", "interact"))
        result = apply_procedural_state(
            target=target,
            source_id=source.id,
            state_id=state_id,
            source_rank_bonus=source_rank_bonus,
            applies_to=("ar_against_source", "dr_against_source"),
            remaining_uses=1,
            expires_on_fiction_events=(f"{cleanup_path}_cleanup", "channel_cleared"),
            notes=("next_channel_dependent_answer_blurred",),
        )
        return EffectApplicationResult(
            effect_id=effect.id,
            applied=result.applied,
            state_changes=(f"procedural:{state_id}",),
            notes=("bounded_sensory_residue_installed",),
        )

    if effect.id == "deny_clean_separation_if_check_succeeds":
        state_id = str(effect.parameters.get("state_id", "clean_separation_denied"))
        source_rank_bonus = source_rank_bonus_override
        if source_rank_bonus is None:
            competency_id = source_competency
            if competency_id is None:
                source_rank_bonus = 0
            else:
                rating = source.competencies.get(str(competency_id))
                source_rank_bonus = 0 if rating is None else rank_bonus(rating.rank)
        result = apply_procedural_state(
            target=target,
            source_id=source.id,
            state_id=state_id,
            source_rank_bonus=source_rank_bonus,
            remaining_uses=1,
            expires_on_fiction_events=("separation_resolved", "position_recentered"),
            notes=("clean_withdrawal_denied",),
        )
        return EffectApplicationResult(
            effect_id=effect.id,
            applied=result.applied,
            state_changes=(f"procedural:{state_id}",),
            notes=("anti_disengagement_state_installed",),
        )

    raise ValueError(
        f"Unsupported effect_id '{effect.id}'. "
        "Add a handler in engine/effects.py or engine/activations.py, "
        "then add the ID to SUPPORTED_EFFECT_IDS."
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

"""Integrated ATB activation execution for actions and techniques."""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass

from loaders import load_action_definitions, load_technique_definitions
from models import ActionDefinition, EffectDefinition, ExperimentResult, TechniqueDefinition

from .ailments_runtime import (
    ActivationAilmentResult,
    AilmentRecoveryRollResult,
    action_gate,
    ailment_definitions_by_id,
    attempt_ailment_recovery,
    reaction_gate,
    resolve_activation_end,
    resolve_activation_start,
)
from .dice import (
    associated_characteristic,
    characteristic_value,
    rank_bonus,
    resistance_characteristic,
    resolve_opposed,
    specialization_roll,
    resistance_roll,
)
from .effects import EffectApplicationResult, apply_effects
from .entities import ExperimentContext
from .exchange import ExchangeResult, resolve_weapon_exchange
from .procedural_states import (
    apply_procedural_state,
    procedural_block_ignore,
    procedural_roll_penalty,
    resolve_procedural_state_expiry,
)
from .reactions import ReactionExecutionResult, resolve_attack_reaction
from .rng import SimulationRNG
from .timeline import TimelineAdvanceResult, mark_pending_activation, next_ready_combatant, spend_timeline_cost


LOST_ACTIVATION_RHYTHM_COST = 3


@dataclass(frozen=True)
class ActivationIntent:
    """One chosen action or technique to execute when a slot becomes ready."""

    actor_slot: str
    mode: str
    definition_id: str
    target_slot: str | None = None
    observer_slot: str | None = None
    zone: str | None = None
    attack_slot: str = "primary"
    ailment_id: str | None = None
    against_feared_line: bool = False
    as_reaction: bool = False
    fiction_events: tuple[str, ...] = ()


@dataclass(frozen=True)
class ActivationExecutionResult:
    """Resolved ATB execution result for one activation intent."""

    actor_id: str
    actor_slot: str
    mode: str
    definition_id: str
    succeeded: bool
    blocked_by_ailment: bool
    activation_result: ActivationAilmentResult
    timeline_result: TimelineAdvanceResult
    recovery_result: AilmentRecoveryRollResult | None = None
    effect_results: tuple[EffectApplicationResult, ...] = ()
    exchange_result: ExchangeResult | None = None
    reaction_results: tuple[ReactionExecutionResult, ...] = ()
    notes: tuple[str, ...] = ()


def _combine_scene_modifiers(*modifiers: int) -> tuple[int, int]:
    positives = [value for value in modifiers if value > 0]
    negatives = [value for value in modifiers if value < 0]
    bonus = max(positives, default=0)
    penalty = abs(sum(negatives))
    return bonus, penalty


def _scene_bonus_penalty(
    *,
    context: ExperimentContext,
    actor_slot: str,
    competency: str,
) -> tuple[int, int]:
    environment_modifier = 0 if context.environment is None else context.environment.roll_modifiers.get(competency, 0)
    scenario_modifier = context.scenario.roll_modifiers.get(actor_slot, {}).get(competency, 0)
    return _combine_scene_modifiers(environment_modifier, scenario_modifier)


def _actions_by_id() -> dict[str, ActionDefinition]:
    return {entry.id: entry for entry in load_action_definitions()}


def _techniques_by_id() -> dict[str, TechniqueDefinition]:
    return {entry.id: entry for entry in load_technique_definitions()}


def _exchange_block_ignore_from_effects(
    *,
    definition: ActionDefinition | TechniqueDefinition,
    actor,
) -> int:
    total = 0
    for effect in definition.effects:
        if effect.id != "same_exchange_ignore_block_rank_bonus":
            continue
        competency_id = str(effect.parameters.get("source_competency", definition.origin if isinstance(definition, TechniqueDefinition) else ""))
        if not competency_id:
            continue
        rating = actor.competencies.get(competency_id)
        if rating is None:
            continue
        total += 0 if rating.rank is None else rank_bonus(rating.rank)
    return total


def _apply_post_exchange_effects(
    *,
    definition: ActionDefinition | TechniqueDefinition,
    actor,
    target,
    actor_slot: str,
    observer_slot: str | None,
) -> tuple[EffectApplicationResult, ...]:
    effect_results: list[EffectApplicationResult] = []
    source_competency = definition.origin if isinstance(definition, TechniqueDefinition) else None
    filtered_effects = [
        effect
        for effect in definition.effects
        if effect.id not in {
            "weapon_exchange_primary",
            "indirect_surface_ranged_attack",
            "false_line_combined_resolution",
            "utility_check_primary",
            "same_exchange_ignore_block_rank_bonus",
            "reposition_after_hit_half_move",
            "reposition_after_hit_distance",
            "advance_before_exchange_distance",
            "reduce_target_movement_rank_bonus",
        }
    ]
    if filtered_effects:
        effect_results.extend(
            apply_effects(
                effects=filtered_effects,
                source=actor,
                target=target,
                source_competency=source_competency,
                activation_index=actor.timeline.activations_taken + 1,
                observer_id=observer_slot,
            )
        )
    reposition_distance: int | None = None
    reposition_effect_id: str | None = None
    for effect in definition.effects:
        if effect.id == "reposition_after_hit_half_move":
            reposition_distance = max(1, actor.movement_meters // 2)
            reposition_effect_id = effect.id
            break
        if effect.id == "reposition_after_hit_distance":
            reposition_distance = max(1, int(effect.parameters.get("meters", 1)))
            reposition_effect_id = effect.id
            break
    if reposition_distance is not None and reposition_effect_id is not None:
        direction = -1 if actor.position.x <= target.position.x else 1
        actor.position = actor.position.__class__(actor.position.x + (direction * reposition_distance), actor.position.y)
        effect_results.append(
            EffectApplicationResult(
                effect_id=reposition_effect_id,
                applied=True,
                state_changes=(f"reposition:{reposition_distance}m",),
            )
        )
    for effect in definition.effects:
        if effect.id != "reduce_target_movement_rank_bonus":
            continue
        competency_id = str(effect.parameters.get("competency", definition.origin if isinstance(definition, TechniqueDefinition) else ""))
        rating = actor.competencies.get(competency_id)
        rb = 0 if rating is None else rank_bonus(rating.rank)
        if rb > 0:
            direction = 1 if actor.position.x <= target.position.x else -1
            target.position = target.position.__class__(target.position.x + (direction * rb), target.position.y)
            effect_results.append(
                EffectApplicationResult(
                    effect_id=effect.id,
                    applied=True,
                    state_changes=(f"target_movement_reduced:{rb}m",),
                )
            )
        else:
            effect_results.append(
                EffectApplicationResult(
                    effect_id=effect.id,
                    applied=False,
                    notes=("zero_rank_bonus_no_movement_reduction",),
                )
            )
        break
    for effect in definition.effects:
        if effect.id == "indirect_surface_ranged_attack":
            declared_surface_count = max(1, int(effect.parameters.get("declared_surface_count", 1)))
            effect_results.append(
                EffectApplicationResult(
                    effect_id=effect.id,
                    applied=True,
                    state_changes=(f"indirect_surface:{declared_surface_count}",),
                    notes=("declared_indirect_line_resolved",),
                )
            )
            continue
        if effect.id != "false_line_combined_resolution":
            continue
        reposition_meters = max(1, int(effect.parameters.get("reposition_meters", 1)))
        direction = -1 if actor.position.x <= target.position.x else 1
        actor.position = actor.position.__class__(target.position.x + (direction * reposition_meters), actor.position.y)
        rating = actor.competencies.get(definition.origin if isinstance(definition, TechniqueDefinition) else "")
        source_rank = 0 if rating is None else rank_bonus(rating.rank)
        state_result = apply_procedural_state(
            target=target,
            source_id=actor.id,
            state_id="read_spoiled",
            source_rank_bonus=source_rank,
            applies_to=("dr_against_source", "ar_against_source"),
            remaining_uses=1,
            expires_on_owner_activation_end=target.timeline.activations_taken + 1,
            notes=("false_line_spoil",),
        )
        effect_results.append(
            EffectApplicationResult(
                effect_id=effect.id,
                applied=state_result.applied,
                state_changes=(f"reposition:{reposition_meters}m", "procedural:read_spoiled"),
                notes=("position_stolen_and_response_spoiled",),
            )
        )
    return tuple(effect_results)


_DAMAGE_EXCHANGE_EFFECTS = frozenset({
    "weapon_exchange_primary",
    "indirect_surface_ranged_attack",
    "false_line_combined_resolution",
})


def _definition_uses_exchange(
    definition: ActionDefinition | TechniqueDefinition,
) -> bool:
    return any(
        effect.id in _DAMAGE_EXCHANGE_EFFECTS or effect.id == "utility_check_primary"
        for effect in definition.effects
    )


def _definition_suppresses_weapon_damage(
    definition: ActionDefinition | TechniqueDefinition,
) -> bool:
    """True when the only exchange driver is utility_check_primary (no weapon damage dealt)."""
    has_utility_check = any(e.id == "utility_check_primary" for e in definition.effects)
    has_damage_effect = any(e.id in _DAMAGE_EXCHANGE_EFFECTS for e in definition.effects)
    return has_utility_check and not has_damage_effect


def _apply_pre_exchange_effects(
    *,
    definition: ActionDefinition | TechniqueDefinition,
    actor,
    target,
) -> tuple[EffectApplicationResult, ...]:
    effect_results: list[EffectApplicationResult] = []
    for effect in definition.effects:
        if effect.id != "advance_before_exchange_distance":
            continue
        advance_distance = max(1, int(effect.parameters.get("meters", 1)))
        direction = 1 if actor.position.x <= target.position.x else -1
        actor.position = actor.position.__class__(actor.position.x + (direction * advance_distance), actor.position.y)
        effect_results.append(
            EffectApplicationResult(
                effect_id="advance_before_exchange_distance",
                applied=True,
                state_changes=(f"advance:{advance_distance}m",),
            )
        )
    return tuple(effect_results)


def _resolve_specialization_opposed(
    *,
    context: ExperimentContext,
    actor_slot: str,
    competency: str,
    opposed_by: str | None,
    target_slot: str | None,
    observer_slot: str | None,
    rng: SimulationRNG,
) -> tuple[bool, int]:
    actor = context.actors_by_slot[actor_slot].combatant
    actor_rating = actor.competencies.get(competency)
    characteristic = associated_characteristic(competency)
    actor_bonus, actor_penalty = _scene_bonus_penalty(
        context=context,
        actor_slot=actor_slot,
        competency=competency,
    )
    actor_roll = specialization_roll(
        competency=competency,
        level=0 if actor_rating is None else actor_rating.level,
        rank=None if actor_rating is None else actor_rating.rank,
        rng=rng,
        characteristic_modifier=0 if characteristic is None else characteristic_value(actor.characteristics, characteristic),
        bonus_modifier=actor_bonus,
        penalty_modifier=actor_penalty,
    )

    if opposed_by == "perception_or_threshold":
        if observer_slot is None:
            raise ValueError("perception_or_threshold requires observer_slot in the activation intent.")
        observer = context.actors_by_slot[observer_slot].combatant
        observer_rating = observer.competencies.get("Percepcion")
        observer_characteristic = associated_characteristic("Percepcion")
        observer_bonus, observer_penalty = _scene_bonus_penalty(
            context=context,
            actor_slot=observer_slot,
            competency="Percepcion",
        )
        observer_roll = specialization_roll(
            competency="Percepcion",
            level=0 if observer_rating is None else observer_rating.level,
            rank=None if observer_rating is None else observer_rating.rank,
            rng=rng,
            characteristic_modifier=0 if observer_characteristic is None else characteristic_value(observer.characteristics, observer_characteristic),
            bonus_modifier=observer_bonus,
            penalty_modifier=observer_penalty,
        )
        opposed = resolve_opposed(actor_roll, observer_roll)
        return opposed.attacker_wins, actor_roll.total

    if opposed_by == "alteration_resistance":
        if target_slot is None:
            raise ValueError("alteration_resistance requires target_slot in the activation intent.")
        target = context.actors_by_slot[target_slot].combatant
        resistance_competency = "alteration"
        resistance_rating = target.competencies.get(resistance_competency)
        rr_characteristic = resistance_characteristic("alteration")
        target_bonus, target_penalty = _scene_bonus_penalty(
            context=context,
            actor_slot=target_slot,
            competency=resistance_competency,
        )
        target_roll = resistance_roll(
            competency=resistance_competency,
            level=0 if resistance_rating is None else resistance_rating.level,
            rank=None if resistance_rating is None else resistance_rating.rank,
            rng=rng,
            characteristic_modifier=characteristic_value(target.characteristics, rr_characteristic),
            bonus_modifier=target_bonus,
            penalty_modifier=target_penalty,
        )
        opposed = resolve_opposed(actor_roll, target_roll)
        return opposed.attacker_wins, actor_roll.total

    if opposed_by == "attacker_ta":
        if target_slot is None:
            raise ValueError("attacker_ta requires target_slot in the activation intent.")
        target = context.actors_by_slot[target_slot].combatant
        target_weapon = target.weapons.get("primary")
        if target_weapon is None:
            return True, actor_roll.total
        target_competency = target_weapon.competency
        target_rating = target.competencies.get(target_competency)
        target_characteristic = associated_characteristic(target_competency)
        target_bonus, target_penalty = _scene_bonus_penalty(
            context=context,
            actor_slot=target_slot,
            competency=target_competency,
        )
        target_roll = specialization_roll(
            competency=target_competency,
            level=0 if target_rating is None else target_rating.level,
            rank=None if target_rating is None else target_rating.rank,
            rng=rng,
            characteristic_modifier=0 if target_characteristic is None else characteristic_value(target.characteristics, target_characteristic),
            bonus_modifier=target_bonus,
            penalty_modifier=target_penalty,
        )
        opposed = resolve_opposed(actor_roll, target_roll)
        return opposed.attacker_wins, actor_roll.total

    return True, actor_roll.total


def _resolve_definition_success(
    *,
    context: ExperimentContext,
    actor_slot: str,
    roll,
    target_slot: str | None,
    observer_slot: str | None,
    rng: SimulationRNG,
) -> tuple[bool, int | float | None]:
    if roll is None:
        return True, None
    if roll.family == "specialization" and roll.competency is not None:
        return _resolve_specialization_opposed(
            context=context,
            actor_slot=actor_slot,
            competency=roll.competency,
            opposed_by=roll.opposed_by,
            target_slot=target_slot,
            observer_slot=observer_slot,
            rng=rng,
        )
    return True, None


def execute_activation_intent(
    *,
    context: ExperimentContext,
    intent: ActivationIntent,
    rng: SimulationRNG,
    recovery_success_by_ailment: dict[str, bool] | None = None,
) -> ActivationExecutionResult:
    """Execute one ready actor's chosen action or technique inside the ATB."""

    recovery_success_by_ailment = recovery_success_by_ailment or {}
    actor_entry = context.actors_by_slot[intent.actor_slot]
    actor = actor_entry.combatant
    if not intent.as_reaction:
        ready = next_ready_combatant(tuple(entry.combatant for entry in context.actors))
        if ready.id != actor.id:
            raise ValueError(f"Actor slot '{intent.actor_slot}' is not currently leftmost on the ATB track.")

        mark_pending_activation(combatant=actor, pending=True)
        activation_result = resolve_activation_start(
            combatant=actor,
            recovery_success_by_ailment=recovery_success_by_ailment,
        )
        if not activation_result.meaningful_activation_allowed:
            timeline_result = spend_timeline_cost(
                combatant=actor,
                rhythm_cost=LOST_ACTIVATION_RHYTHM_COST,
                attrition_cost=0,
            )
            end_result = resolve_activation_end(
                combatant=actor,
                fiction_events=intent.fiction_events,
            )
            procedural_end = resolve_procedural_state_expiry(
                combatants=tuple(entry.combatant for entry in context.actors),
                actor=actor,
                fiction_events=intent.fiction_events,
            )
            mark_pending_activation(combatant=actor, pending=False)
            return ActivationExecutionResult(
                actor_id=actor.id,
                actor_slot=intent.actor_slot,
                mode=intent.mode,
                definition_id=intent.definition_id,
                succeeded=False,
                blocked_by_ailment=True,
                activation_result=activation_result,
                timeline_result=timeline_result,
                notes=("lost_meaningful_activation",)
                + end_result.notes
                + (() if not procedural_end.cleared_states else ("procedural_state_expired",)),
            )
    else:
        activation_result = ActivationAilmentResult(
            meaningful_activation_allowed=True,
            lost_activation_consumed=False,
            cleared_ailments=(),
            remaining_ailments=tuple(ailment.ailment_id for ailment in actor.ailments if ailment.active),
        )

    if intent.mode == "recovery":
        if intent.ailment_id is None:
            raise ValueError("Recovery mode requires ailment_id.")
        recovery_definition = ailment_definitions_by_id()[intent.ailment_id].recovery
        recovery_competency = None if recovery_definition is None else recovery_definition.competency
        recovery_gate = action_gate(
            combatant=actor,
            competency=recovery_competency,
            against_feared_line=False,
            is_recovery_attempt=True,
            recovery_success_by_ailment=recovery_success_by_ailment,
        )
        if not recovery_gate.allowed:
            timeline_result = spend_timeline_cost(
                combatant=actor,
                rhythm_cost=6,
                attrition_cost=1,
            )
            end_result = resolve_activation_end(
                combatant=actor,
                fiction_events=intent.fiction_events,
            )
            procedural_end = resolve_procedural_state_expiry(
                combatants=tuple(entry.combatant for entry in context.actors),
                actor=actor,
                fiction_events=intent.fiction_events,
            )
            mark_pending_activation(combatant=actor, pending=False)
            return ActivationExecutionResult(
                actor_id=actor.id,
                actor_slot=intent.actor_slot,
                mode=intent.mode,
                definition_id=intent.ailment_id,
                succeeded=False,
                blocked_by_ailment=True,
                activation_result=activation_result,
                timeline_result=timeline_result,
                notes=recovery_gate.notes
                + end_result.notes
                + (() if not procedural_end.cleared_states else ("procedural_state_expired",)),
            )
        recovery_result = attempt_ailment_recovery(
            combatant=actor,
            ailment_id=intent.ailment_id,
            rng=rng,
        )
        timeline_result = spend_timeline_cost(
            combatant=actor,
            rhythm_cost=6,
            attrition_cost=1,
        )
        end_result = resolve_activation_end(
            combatant=actor,
            fiction_events=intent.fiction_events,
        )
        procedural_end = resolve_procedural_state_expiry(
            combatants=tuple(entry.combatant for entry in context.actors),
            actor=actor,
            fiction_events=intent.fiction_events,
        )
        mark_pending_activation(combatant=actor, pending=False)
        return ActivationExecutionResult(
            actor_id=actor.id,
            actor_slot=intent.actor_slot,
            mode=intent.mode,
            definition_id=intent.ailment_id,
            succeeded=recovery_result.success,
            blocked_by_ailment=False,
            activation_result=activation_result,
            timeline_result=timeline_result,
            recovery_result=recovery_result,
            notes=("explicit_recovery_attempt",)
            + end_result.notes
            + (() if not procedural_end.cleared_states else ("procedural_state_expired",)),
        )

    if intent.mode == "action":
        definition = _actions_by_id()[intent.definition_id]
    elif intent.mode == "technique":
        definition = _techniques_by_id()[intent.definition_id]
    else:
        raise ValueError(f"Unsupported activation mode: {intent.mode}")

    if intent.as_reaction:
        if intent.mode == "action" and definition.trigger_type != "reactive":
            raise ValueError(f"Action '{definition.id}' cannot execute as a reaction.")
        if intent.mode == "technique" and definition.type != "reactive":
            raise ValueError(f"Technique '{definition.id}' cannot execute as a reaction.")
        reaction_result = reaction_gate(
            combatant=actor,
            timing_sensitive=True,
            recovery_success_by_ailment=recovery_success_by_ailment,
        )
        if not reaction_result.allowed:
            timeline_result = spend_timeline_cost(
                combatant=actor,
                rhythm_cost=0,
                attrition_cost=0,
                as_reaction=True,
            )
            return ActivationExecutionResult(
                actor_id=actor.id,
                actor_slot=intent.actor_slot,
                mode=intent.mode,
                definition_id=intent.definition_id,
                succeeded=False,
                blocked_by_ailment=True,
                activation_result=activation_result,
                timeline_result=timeline_result,
                notes=reaction_result.notes,
            )

    intent_competency = None
    if definition.roll is not None and definition.roll.competency is not None:
        intent_competency = definition.roll.competency
    elif intent.mode == "technique":
        intent_competency = definition.origin

    gate_result = None
    if not intent.as_reaction:
        gate_result = action_gate(
            combatant=actor,
            competency=intent_competency,
            against_feared_line=intent.against_feared_line,
            recovery_success_by_ailment=recovery_success_by_ailment,
        )
    if gate_result is not None and not gate_result.allowed:
        timeline_result = spend_timeline_cost(
            combatant=actor,
            rhythm_cost=definition.rhythm,
            attrition_cost=definition.attrition,
        )
        end_result = resolve_activation_end(
            combatant=actor,
            fiction_events=intent.fiction_events,
        )
        procedural_end = resolve_procedural_state_expiry(
            combatants=tuple(entry.combatant for entry in context.actors),
            actor=actor,
            fiction_events=intent.fiction_events,
        )
        mark_pending_activation(combatant=actor, pending=False)
        return ActivationExecutionResult(
            actor_id=actor.id,
            actor_slot=intent.actor_slot,
            mode=intent.mode,
            definition_id=intent.definition_id,
            succeeded=False,
            blocked_by_ailment=True,
            activation_result=activation_result,
            timeline_result=timeline_result,
            notes=gate_result.notes
            + end_result.notes
            + (() if not procedural_end.cleared_states else ("procedural_state_expired",)),
        )

    success, active_value = _resolve_definition_success(
        context=context,
        actor_slot=intent.actor_slot,
        roll=definition.roll,
        target_slot=intent.target_slot,
        observer_slot=intent.observer_slot,
        rng=rng,
    )

    exchange_result = None
    effect_results: tuple[EffectApplicationResult, ...] = ()
    reaction_results: tuple[ReactionExecutionResult, ...] = ()
    if success:
        if _definition_uses_exchange(definition):
            if intent.target_slot is None or intent.zone is None:
                raise ValueError("Exchange-bearing techniques require target_slot and zone.")
            target = context.actors_by_slot[intent.target_slot].combatant
            effect_results = _apply_pre_exchange_effects(
                definition=definition,
                actor=actor,
                target=target,
            )
            attack_penalty = procedural_roll_penalty(
                combatant=actor,
                roll_tag="ar_against_source",
                against_source_id=target.id,
            )
            defense_penalty = procedural_roll_penalty(
                combatant=target,
                roll_tag="dr_against_source",
                against_source_id=actor.id,
            )
            reaction_result = None
            if not intent.as_reaction:
                reaction_result = resolve_attack_reaction(
                    context=context,
                    attacker_slot=intent.actor_slot,
                    defender_slot=intent.target_slot,
                    zone=intent.zone,
                )
            defense_bonus = 0
            if reaction_result is not None:
                reaction_results = (reaction_result,)
                if reaction_result.applied:
                    defense_bonus = reaction_result.defense_bonus
            block_ignore = _exchange_block_ignore_from_effects(
                definition=definition,
                actor=actor,
            ) + procedural_block_ignore(
                attacker=actor,
                defender=target,
            )
            exchange_result = resolve_weapon_exchange(
                attacker=actor,
                defender=target,
                zone=intent.zone,
                rng=rng,
                attack_slot=intent.attack_slot,
                attack_penalty=attack_penalty,
                defense_bonus=defense_bonus,
                defense_penalty=defense_penalty,
                block_ignore=block_ignore,
            )
            if _definition_suppresses_weapon_damage(definition):
                exchange_result = dataclasses.replace(exchange_result, effective_damage=0)
            if exchange_result.attack_connected:
                observer_id = None if intent.observer_slot is None else context.actors_by_slot[intent.observer_slot].combatant.id
                effect_results = effect_results + _apply_post_exchange_effects(
                    definition=definition,
                    actor=actor,
                    target=target,
                    actor_slot=intent.actor_slot,
                    observer_slot=observer_id,
                )
        else:
            target = actor if intent.target_slot is None else context.actors_by_slot[intent.target_slot].combatant
            observer_id = None if intent.observer_slot is None else context.actors_by_slot[intent.observer_slot].combatant.id
            source_competency = None
            if intent.mode == "technique":
                source_competency = definition.origin
            effect_results = apply_effects(
                effects=definition.effects,
                source=actor,
                target=target,
                source_competency=source_competency,
                activation_index=actor.timeline.activations_taken + 1,
                observer_id=observer_id,
                active_value=active_value,
            )

    timeline_result = spend_timeline_cost(
        combatant=actor,
        rhythm_cost=definition.rhythm,
        attrition_cost=definition.attrition,
        as_reaction=intent.as_reaction,
    )
    end_result = resolve_activation_end(
        combatant=actor,
        fiction_events=intent.fiction_events,
    )
    procedural_end = resolve_procedural_state_expiry(
        combatants=tuple(entry.combatant for entry in context.actors),
        actor=actor,
        fiction_events=intent.fiction_events,
    )
    if not intent.as_reaction:
        mark_pending_activation(combatant=actor, pending=False)
    return ActivationExecutionResult(
        actor_id=actor.id,
        actor_slot=intent.actor_slot,
        mode=intent.mode,
        definition_id=intent.definition_id,
        succeeded=success,
        blocked_by_ailment=False,
        activation_result=activation_result,
        timeline_result=timeline_result,
        effect_results=effect_results,
        exchange_result=exchange_result,
        reaction_results=reaction_results,
        notes=end_result.notes + (() if not procedural_end.cleared_states else ("procedural_state_expired",)),
    )

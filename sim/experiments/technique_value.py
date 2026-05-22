"""Technique value experiment runners."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

from engine.activations import ActivationIntent, execute_activation_intent
from engine.resolver import instantiate_question_context, load_simulation_inputs
from engine.rng import SimulationRNG
from experiments.atb_tempo import initialize_context_timeline
from loaders import load_technique_definitions
from models import AggregateMetric, ExperimentResult, IterationResult


_DAMAGE_EXCHANGE_EFFECT_IDS = frozenset({
    "weapon_exchange_primary",
    "indirect_surface_ranged_attack",
    "false_line_combined_resolution",
})


@dataclass(frozen=True)
class TechniqueCostRuntime:
    """Static compiled runtime for one technique-cost question."""

    question_id: str
    scenario_id: str
    technique_id: str
    baseline_action_id: str | None
    actor_slot: str
    target_slot: str
    zone: str
    rhythm: int
    attrition: int
    as_reaction: bool
    has_weapon_damage: bool
    metric_ids: tuple[str, ...]
    question_notes: tuple[str, ...]


def _techniques_by_id():
    return {entry.id: entry for entry in load_technique_definitions()}


def _value_score(
    *,
    effective_damage: int,
    position_theft: bool,
    spoiled_answer: bool,
    clean_separation_denied: bool = False,
    residue_applied: bool = False,
    spoiled_channel: bool = False,
    distance_recovered: bool = False,
    indirect_surface_resolved: bool = False,
    read_mark_applied: bool = False,
    ailment_applied: bool = False,
) -> float:
    return float(
        effective_damage
        + (1 if position_theft else 0)
        + (1 if spoiled_answer else 0)
        + (1 if clean_separation_denied else 0)
        + (1 if spoiled_channel else 0)
        + (1 if distance_recovered else 0)
        + (1 if indirect_surface_resolved else 0)
        + (1 if read_mark_applied else 0)
        + (0.5 if residue_applied else 0)
        + (1 if ailment_applied else 0)
    )


def _build_technique_cost_runtime(question_id: str) -> TechniqueCostRuntime:
    inputs = load_simulation_inputs()
    question = inputs.questions_by_id[question_id]
    technique_id = question.comparisons.get("technique")
    if technique_id is None:
        for suffix in (
            "_cost",
            "_effectiveness",
            "_reposition_value",
        ):
            if question.id.endswith(suffix) and question.id.startswith("naghii_"):
                technique_id = question.id.removeprefix("naghii_").removesuffix(suffix)
                break
    if technique_id is None:
        raise ValueError(f"Technique value question '{question_id}' is missing compare.technique.")
    # Baseline is optional — None means no intra-run comparison, use consistency analysis instead
    baseline_action_id = question.comparisons.get("baseline_action") or None
    technique = _techniques_by_id()[technique_id]
    has_weapon_damage = any(e.id in _DAMAGE_EXCHANGE_EFFECT_IDS for e in technique.effects)
    actor_slots = [assignment.slot for assignment in question.actor_assignments]
    if len(actor_slots) < 2:
        raise ValueError(f"Technique cost question '{question_id}' requires at least two actor slots.")
    actor_slot = "mover" if "mover" in actor_slots else actor_slots[0]
    target_slot = "watcher" if "watcher" in actor_slots else next(slot for slot in actor_slots if slot != actor_slot)
    return TechniqueCostRuntime(
        question_id=question.id,
        scenario_id=question.scenario_id,
        technique_id=technique_id,
        baseline_action_id=baseline_action_id,
        actor_slot=actor_slot,
        target_slot=target_slot,
        zone="torso",
        rhythm=technique.rhythm,
        attrition=technique.attrition,
        as_reaction=technique.type == "reactive",
        has_weapon_damage=has_weapon_damage,
        metric_ids=question.metrics,
        question_notes=question.notes,
    )


@lru_cache(maxsize=16)
def _cached_technique_cost_runtime(question_id: str) -> TechniqueCostRuntime:
    return _build_technique_cost_runtime(question_id)


def run_technique_cost_iteration(
    *,
    question_id: str,
    seed: int,
    runtime: TechniqueCostRuntime | None = None,
) -> IterationResult:
    """Run one technique-cost iteration. Baseline comparison is skipped when no baseline_action_id."""

    runtime = runtime or _cached_technique_cost_runtime(question_id)
    inputs = load_simulation_inputs()

    technique_context = instantiate_question_context(question_id, inputs=inputs)
    initialize_context_timeline(technique_context)
    technique_actor = technique_context.actors_by_slot[runtime.actor_slot].combatant
    technique_target = technique_context.actors_by_slot[runtime.target_slot].combatant
    technique_target.attrition_spent = 4
    technique_before_x = technique_actor.position.x
    technique_before_target_x = technique_target.position.x

    technique_result = execute_activation_intent(
        context=technique_context,
        intent=ActivationIntent(
            actor_slot=runtime.actor_slot,
            mode="technique",
            definition_id=runtime.technique_id,
            target_slot=runtime.target_slot,
            zone=runtime.zone,
            as_reaction=runtime.as_reaction,
        ),
        rng=SimulationRNG(seed=seed),
    )

    technique_hit = bool(technique_result.exchange_result and technique_result.exchange_result.attack_connected)
    technique_damage = 0 if technique_result.exchange_result is None else technique_result.exchange_result.effective_damage
    technique_position_delta = abs(technique_actor.position.x - technique_before_x)
    target_distance_before = abs(technique_before_target_x - technique_before_x)
    target_distance_after = abs(technique_target.position.x - technique_actor.position.x)
    technique_spoiled_answer = any(state.state_id == "read_spoiled" for state in technique_target.procedural_states)
    clean_separation_denied = any(state.state_id == "clean_separation_denied" for state in technique_target.procedural_states)
    residue_applied = any(state.state_id == "signal_blurred" for state in technique_target.procedural_states)
    read_mark_applied = any(state.state_id == "read_marked" for state in technique_target.procedural_states)
    advance_before_exchange = any(
        effect.effect_id == "advance_before_exchange_distance" and effect.applied
        for effect in technique_result.effect_results
    )
    indirect_surface_resolved = any(
        effect.effect_id == "indirect_surface_ranged_attack" and effect.applied
        for effect in technique_result.effect_results
    )
    ailment_applied = any(
        effect.effect_id == "apply_ailment" and effect.applied
        for effect in technique_result.effect_results
    )
    # distance_recovered and position_theft are mutually exclusive:
    # retreat repositioning (distance increases) counts as distance_recovered only,
    # offensive repositioning (distance does not increase) counts as position_theft only.
    distance_recovered = technique_position_delta > 0 and target_distance_after > target_distance_before
    technique_position_theft = technique_position_delta > 0 and not distance_recovered
    technique_value = _value_score(
        effective_damage=technique_damage,
        position_theft=technique_position_theft,
        spoiled_answer=technique_spoiled_answer,
        clean_separation_denied=clean_separation_denied,
        residue_applied=residue_applied,
        distance_recovered=distance_recovered,
        indirect_surface_resolved=indirect_surface_resolved,
        read_mark_applied=read_mark_applied,
        ailment_applied=ailment_applied,
    )

    followup_spoiled_channel = False
    route_readability_preserved = False
    if residue_applied or read_mark_applied:
        followup_result = execute_activation_intent(
            context=technique_context,
            intent=ActivationIntent(
                actor_slot=runtime.target_slot,
                mode="action",
                definition_id="attack_one_handed",
                target_slot=runtime.actor_slot,
                zone=runtime.zone,
            ),
            rng=SimulationRNG(seed=seed + 100_000),
        )
        if followup_result.succeeded:
            remaining_state_ids = {state.state_id for state in technique_target.procedural_states}
            if residue_applied and "signal_blurred" not in remaining_state_ids:
                followup_spoiled_channel = True
            if read_mark_applied and "read_marked" in remaining_state_ids:
                route_readability_preserved = True
    if followup_spoiled_channel:
        technique_value += 1.0
    if route_readability_preserved:
        # Mark survived the opponent's next action — future benefit still active
        technique_value += 0.5

    metrics: dict[str, float] = {
        "hit_rate": 1.0 if technique_hit else 0.0,
        "effective_damage_rate": float(technique_damage),
        "position_theft_rate": 1.0 if technique_position_theft else 0.0,
        "spoiled_answer_rate": 1.0 if technique_spoiled_answer else 0.0,
        "combined_swing_rate": 1.0 if technique_position_theft and technique_spoiled_answer else 0.0,
        "mark_application_rate": 1.0 if read_mark_applied else 0.0,
        "route_readability_preserved_rate": 1.0 if route_readability_preserved else 0.0,
        "residue_application_rate": 1.0 if residue_applied else 0.0,
        "spoiled_channel_answer_rate": 1.0 if followup_spoiled_channel else 0.0,
        "cleanup_before_use_rate": 0.0,
        "burden_conversion_rate": 1.0 if residue_applied and followup_spoiled_channel else 0.0,
        "trigger_opportunity_rate": 1.0 if runtime.as_reaction else 0.0,
        "reaction_use_rate": 1.0 if runtime.as_reaction and technique_result.timeline_result.as_reaction else 0.0,
        "clean_separation_denial_rate": 1.0 if clean_separation_denied else 0.0,
        "distance_recovery_rate": 1.0 if distance_recovered else 0.0,
        "followup_pressure_relief_rate": 1.0 if distance_recovered else 0.0,
        "enemy_reengage_requirement_rate": 1.0 if distance_recovered else 0.0,
        "recovered_meter_value": float(technique_position_delta),
        "entry_success_rate": 1.0 if advance_before_exchange else 0.0,
        "forward_commitment_value": float(technique_position_delta),
        "indirect_line_success_rate": 1.0 if indirect_surface_resolved else 0.0,
        "cover_edge_bypass_value": 1.0 if indirect_surface_resolved else 0.0,
        "nontrivial_geometry_value_rate": 1.0 if indirect_surface_resolved else 0.0,
        "damage_conversion_rate": float(technique_damage),
        "rhythm_efficiency": technique_value / runtime.rhythm,
        "attrition_efficiency": technique_value / max(1, runtime.attrition),
        "technique_value": technique_value,
        "ailment_application_rate": 1.0 if ailment_applied else 0.0,
        "aterrorizado_application_rate": 1.0 if ailment_applied else 0.0,
        "rr_failure_rate_in_target": 1.0 if ailment_applied else 0.0,
        "resolution_rate": 1.0 if technique_result.succeeded else 0.0,
        "trigger_rate": 1.0 if technique_result.succeeded else 0.0,
        "condition_application_rate": 1.0 if ailment_applied else 0.0,
        "rr_failure_rate": 1.0 if ailment_applied else 0.0,
        "cost_efficiency_vs_utility_median": technique_value / runtime.rhythm,
    }

    # Baseline comparison — only when a baseline action is specified
    if runtime.baseline_action_id is not None:
        baseline_context = instantiate_question_context(question_id, inputs=inputs)
        initialize_context_timeline(baseline_context)
        baseline_target = baseline_context.actors_by_slot[runtime.target_slot].combatant
        baseline_target.attrition_spent = 4

        baseline_result = execute_activation_intent(
            context=baseline_context,
            intent=ActivationIntent(
                actor_slot=runtime.actor_slot,
                mode="action",
                definition_id=runtime.baseline_action_id,
                target_slot=runtime.target_slot,
                zone=runtime.zone,
            ),
            rng=SimulationRNG(seed=seed),
        )
        baseline_hit = bool(baseline_result.exchange_result and baseline_result.exchange_result.attack_connected)
        baseline_damage = 0 if baseline_result.exchange_result is None else baseline_result.exchange_result.effective_damage
        baseline_value = float(baseline_damage)
        metrics["baseline_hit_rate"] = 1.0 if baseline_hit else 0.0
        metrics["baseline_effective_damage_rate"] = float(baseline_damage)
        metrics["baseline_rhythm_efficiency"] = baseline_value / 5.0
        metrics["baseline_attrition_efficiency"] = baseline_value / 1.0
        metrics["delta_value_score"] = technique_value - baseline_value

    return IterationResult(
        iteration_index=seed,
        question_id=runtime.question_id,
        scenario_id=runtime.scenario_id,
        metrics=metrics,
        state_changes=[
            f"technique:{runtime.technique_id}",
            *([] if runtime.baseline_action_id is None else [f"baseline:{runtime.baseline_action_id}"]),
        ],
        notes=("technique_cost_runner",),
    )


def run_technique_cost_experiment(
    *,
    question_id: str,
    iterations: int | None = None,
    base_seed: int = 1,
) -> ExperimentResult:
    """Run one saved technique-cost question. No baseline comparison unless question specifies baseline_action."""

    runtime = _cached_technique_cost_runtime(question_id)
    actual_iterations = 20000 if iterations is None else iterations
    results = [
        run_technique_cost_iteration(
            question_id=question_id,
            seed=base_seed + index,
            runtime=runtime,
        )
        for index in range(actual_iterations)
    ]

    requested_metrics = runtime.metric_ids
    aggregates = []
    for metric_id in requested_metrics:
        total = sum(result.metrics.get(metric_id, 0.0) for result in results)
        aggregates.append(AggregateMetric(id=metric_id, value=total / actual_iterations))

    comparisons: dict[str, float] = {}
    if runtime.baseline_action_id is not None:
        for key in ("baseline_hit_rate", "baseline_effective_damage_rate", "baseline_rhythm_efficiency", "baseline_attrition_efficiency", "delta_value_score"):
            comparisons[key] = sum(result.metrics.get(key, 0.0) for result in results) / actual_iterations

    return ExperimentResult(
        question_id=runtime.question_id,
        scenario_id=runtime.scenario_id,
        iterations=actual_iterations,
        aggregates=aggregates,
        comparisons=comparisons,
        notes=("technique_cost_experiment", runtime.technique_id),
    )


def run_robar_el_angulo_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_robar_el_angulo_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_nublar_la_senal_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_nublar_la_senal_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_recuperar_la_distancia_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_recuperar_la_distancia_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_doblar_el_tiro_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_doblar_el_tiro_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_recuperar_la_distancia_reposition_value_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_recuperar_la_distancia_reposition_value",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_nublar_la_senal_effectiveness_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_nublar_la_senal_effectiveness",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_doblar_el_tiro_effectiveness_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_doblar_el_tiro_effectiveness",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_marcar_la_lectura_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_marcar_la_lectura_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_cerrar_la_linea_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_cerrar_la_linea_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_clavar_el_paso_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_clavar_el_paso_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_anudar_el_paso_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_anudar_el_paso_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_clavar_la_cadencia_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_clavar_la_cadencia_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_tocar_y_ceder_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_tocar_y_ceder_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_leer_el_calor_del_paso_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_leer_el_calor_del_paso_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_pesar_el_umbral_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_pesar_el_umbral_cost",
        iterations=iterations,
        base_seed=base_seed,
    )


def run_trabar_el_gesto_cost_experiment(
    *,
    iterations: int = 20000,
    base_seed: int = 1,
) -> ExperimentResult:
    return run_technique_cost_experiment(
        question_id="naghii_trabar_el_gesto_cost",
        iterations=iterations,
        base_seed=base_seed,
    )

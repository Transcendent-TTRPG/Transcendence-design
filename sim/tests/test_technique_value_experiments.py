import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from experiments.technique_value import (
    run_anudar_el_paso_cost_experiment,
    run_cerrar_la_linea_cost_experiment,
    run_clavar_el_paso_cost_experiment,
    run_clavar_la_cadencia_cost_experiment,
    run_doblar_el_tiro_cost_experiment,
    run_doblar_el_tiro_effectiveness_experiment,
    run_leer_el_calor_del_paso_cost_experiment,
    run_marcar_la_lectura_cost_experiment,
    run_nublar_la_senal_cost_experiment,
    run_nublar_la_senal_effectiveness_experiment,
    run_pesar_el_umbral_cost_experiment,
    run_recuperar_la_distancia_cost_experiment,
    run_recuperar_la_distancia_reposition_value_experiment,
    run_robar_el_angulo_cost_experiment,
    run_technique_cost_iteration,
    run_tocar_y_ceder_cost_experiment,
    run_trabar_el_gesto_cost_experiment,
)


def test_robar_el_angulo_cost_iteration_produces_expected_metric_keys() -> None:
    result = run_technique_cost_iteration(
        question_id="naghii_robar_el_angulo_cost",
        seed=1,
    )

    assert result.question_id == "naghii_robar_el_angulo_cost"
    assert result.scenario_id == "naghii_flexible_pressure_2m"
    assert {
        "hit_rate",
        "effective_damage_rate",
        "position_theft_rate",
        "spoiled_answer_rate",
        "combined_swing_rate",
        "rhythm_efficiency",
        "attrition_efficiency",
        "technique_value",
    }.issubset(set(result.metrics.keys()))
    # Baseline metrics are absent when no baseline_action is specified in the question
    assert "baseline_hit_rate" not in result.metrics
    assert "delta_value_score" not in result.metrics


def test_robar_el_angulo_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_robar_el_angulo_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_robar_el_angulo_cost"
    assert result.iterations == 10
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "hit_rate",
        "position_theft_rate",
        "spoiled_answer_rate",
        "combined_swing_rate",
        "rhythm_efficiency",
        "attrition_efficiency",
    }
    # No baseline comparison — techniques are evaluated via intra-set consistency analysis
    assert result.comparisons == {}


def test_nublar_la_senal_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_nublar_la_senal_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_nublar_la_senal_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "hit_rate",
        "residue_application_rate",
        "spoiled_channel_answer_rate",
        "rhythm_efficiency",
        "attrition_efficiency",
    }


def test_recuperar_la_distancia_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_recuperar_la_distancia_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_recuperar_la_distancia_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "hit_rate",
        "effective_damage_rate",
        "distance_recovery_rate",
        "followup_pressure_relief_rate",
        "rhythm_efficiency",
        "attrition_efficiency",
    }


def test_doblar_el_tiro_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_doblar_el_tiro_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_doblar_el_tiro_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "hit_rate",
        "indirect_line_success_rate",
        "cover_edge_bypass_value",
        "rhythm_efficiency",
        "attrition_efficiency",
    }


def test_recuperar_la_distancia_reposition_value_question_runs() -> None:
    result = run_recuperar_la_distancia_reposition_value_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_recuperar_la_distancia_reposition_value"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "distance_recovery_rate",
        "enemy_reengage_requirement_rate",
        "followup_pressure_relief_rate",
        "recovered_meter_value",
    }


def test_nublar_la_senal_effectiveness_question_runs() -> None:
    result = run_nublar_la_senal_effectiveness_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_nublar_la_senal_effectiveness"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "residue_application_rate",
        "spoiled_channel_answer_rate",
        "cleanup_before_use_rate",
        "burden_conversion_rate",
    }


def test_doblar_el_tiro_effectiveness_question_runs() -> None:
    result = run_doblar_el_tiro_effectiveness_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_doblar_el_tiro_effectiveness"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "indirect_line_success_rate",
        "cover_edge_bypass_value",
        "nontrivial_geometry_value_rate",
        "damage_conversion_rate",
    }


def test_marcar_la_lectura_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_marcar_la_lectura_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_marcar_la_lectura_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "hit_rate",
        "mark_application_rate",
        "route_readability_preserved_rate",
        "rhythm_efficiency",
        "attrition_efficiency",
    }


def test_cerrar_la_linea_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_cerrar_la_linea_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_cerrar_la_linea_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "trigger_opportunity_rate",
        "reaction_use_rate",
        "hit_rate",
        "effective_damage_rate",
        "rhythm_efficiency",
        "attrition_efficiency",
    }


def test_clavar_el_paso_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_clavar_el_paso_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_clavar_el_paso_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "hit_rate",
        "effective_damage_rate",
        "entry_success_rate",
        "forward_commitment_value",
        "rhythm_efficiency",
        "attrition_efficiency",
    }


def test_anudar_el_paso_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_anudar_el_paso_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_anudar_el_paso_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "trigger_opportunity_rate",
        "reaction_use_rate",
        "clean_separation_denial_rate",
        "rhythm_efficiency",
        "attrition_efficiency",
    }


def test_clavar_la_cadencia_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_clavar_la_cadencia_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_clavar_la_cadencia_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "hit_rate",
        "effective_damage_rate",
        "movement_disruption_rate",
        "rhythm_efficiency",
        "attrition_efficiency",
    }


def test_tocar_y_ceder_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_tocar_y_ceder_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_tocar_y_ceder_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "hit_rate",
        "effective_damage_rate",
        "return_rate",
        "rhythm_efficiency",
        "attrition_efficiency",
    }


def test_leer_el_calor_del_paso_cost_experiment_resolves() -> None:
    result = run_leer_el_calor_del_paso_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_leer_el_calor_del_paso_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "user_atb_position_after_technique",
        "activations_before_target_acts_again",
        "technique_use_rate_in_open_engagement",
        "rhythm_investment_vs_activation_window",
    }
    # Info-only technique always resolves — resolution_rate in full metrics dict
    iteration_result = run_technique_cost_iteration(
        question_id="naghii_leer_el_calor_del_paso_cost",
        seed=1,
    )
    assert iteration_result.metrics["resolution_rate"] == 1.0


def test_pesar_el_umbral_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_pesar_el_umbral_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_pesar_el_umbral_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "user_atb_position_after_technique",
        "aterrorizado_application_rate",
        "rr_failure_rate_in_target",
        "technique_use_rate_in_concealment_engagement",
    }
    # Verify ailment_application_rate is present in full metrics dict
    iteration_result = run_technique_cost_iteration(
        question_id="naghii_pesar_el_umbral_cost",
        seed=1,
    )
    assert "ailment_application_rate" in iteration_result.metrics


def test_trabar_el_gesto_cost_experiment_aggregates_requested_metrics() -> None:
    result = run_trabar_el_gesto_cost_experiment(iterations=10, base_seed=1)

    assert result.question_id == "naghii_trabar_el_gesto_cost"
    aggregate_ids = {metric.id for metric in result.aggregates}
    assert aggregate_ids == {
        "trigger_rate",
        "condition_application_rate",
        "rr_failure_rate",
        "cost_efficiency_vs_utility_median",
    }
    # trigger_rate is the specialization opposed roll success rate
    iteration_result = run_technique_cost_iteration(
        question_id="naghii_trabar_el_gesto_cost",
        seed=1,
    )
    assert "trigger_rate" in iteration_result.metrics
    assert "condition_application_rate" in iteration_result.metrics

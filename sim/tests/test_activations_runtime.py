import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.activations import ActivationIntent, execute_activation_intent
from engine.entities import build_experiment_context
from engine.resolver import instantiate_question_context, load_simulation_inputs
from engine.rng import SimulationRNG
from experiments.atb_tempo import initialize_context_timeline
from models import ActiveAilment, ActorAssignment, CompetencyRating, GridPosition, QuestionDefinition, ScenarioActorSlot, ScenarioDefinition


def _initialized_hidden_crossing_context():
    context = instantiate_question_context("hidden_gain_crossing_4m")
    initialize_context_timeline(
        context,
        situational_modifiers_by_slot={
            "mover": 1,
            "watcher": -1,
        },
    )
    return context


def _initialized_naghii_range_recovery_context():
    inputs = load_simulation_inputs()
    scenario = ScenarioDefinition(
        id="naghii_range_recovery_seed",
        actor_slots=(
            ScenarioActorSlot(slot="mover", position=GridPosition(2, 0)),
            ScenarioActorSlot(slot="watcher", position=GridPosition(4, 0)),
        ),
        notes=("Minimal seed scenario for Recuperar la Distancia.",),
    )
    question = QuestionDefinition(
        id="naghii_range_recovery_seed",
        prompt="Can Recuperar la Distancia recover one meter of space after a successful thrust?",
        scenario_id=scenario.id,
        actor_assignments=(
            ActorAssignment(slot="mover", profile_id="naghii_novice_range_warden"),
            ActorAssignment(slot="watcher", profile_id="common_guard_observer"),
        ),
        policy_assignments={
            "mover": "tempo_first",
            "watcher": "conservative",
        },
    )
    context = build_experiment_context(
        question=question,
        scenario=scenario,
        environment=None,
        profiles_by_id=inputs.profiles_by_id,
    )
    initialize_context_timeline(context)
    return context


def _initialized_naghii_projection_context(*, profile_id: str = "naghii_novice_projection_scout"):
    inputs = load_simulation_inputs()
    scenario = ScenarioDefinition(
        id=f"{profile_id}_seed",
        actor_slots=(
            ScenarioActorSlot(slot="mover", position=GridPosition(2, 0)),
            ScenarioActorSlot(slot="watcher", position=GridPosition(5, 0)),
        ),
        notes=("Minimal seed scenario for Naghii projection techniques.",),
    )
    question = QuestionDefinition(
        id=f"{profile_id}_seed",
        prompt="Can the seeded Naghii projection technique resolve inside the ATB loop?",
        scenario_id=scenario.id,
        actor_assignments=(
            ActorAssignment(slot="mover", profile_id=profile_id),
            ActorAssignment(slot="watcher", profile_id="common_guard_observer"),
        ),
        policy_assignments={
            "mover": "tempo_first",
            "watcher": "conservative",
        },
    )
    context = build_experiment_context(
        question=question,
        scenario=scenario,
        environment=None,
        profiles_by_id=inputs.profiles_by_id,
    )
    initialize_context_timeline(context)
    return context


def _initialized_naghii_flexible_context(*, profile_id: str):
    inputs = load_simulation_inputs()
    scenario = ScenarioDefinition(
        id=f"{profile_id}_seed",
        actor_slots=(
            ScenarioActorSlot(slot="mover", position=GridPosition(2, 0)),
            ScenarioActorSlot(slot="watcher", position=GridPosition(4, 0)),
        ),
        notes=("Minimal seed scenario for Naghii flexible-weapon techniques.",),
    )
    question = QuestionDefinition(
        id=f"{profile_id}_seed",
        prompt="Can the seeded Naghii flexible-weapon technique resolve inside the ATB loop?",
        scenario_id=scenario.id,
        actor_assignments=(
            ActorAssignment(slot="mover", profile_id=profile_id),
            ActorAssignment(slot="watcher", profile_id="common_guard_observer"),
        ),
        policy_assignments={
            "mover": "tempo_first",
            "watcher": "conservative",
        },
    )
    context = build_experiment_context(
        question=question,
        scenario=scenario,
        environment=None,
        profiles_by_id=inputs.profiles_by_id,
    )
    initialize_context_timeline(context)
    return context


def test_hide_action_executes_inside_atb_and_advances_timeline() -> None:
    context = _initialized_hidden_crossing_context()

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="hide",
            observer_slot="watcher",
        ),
        rng=SimulationRNG(seed=11),
    )

    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    assert result.succeeded is True
    assert result.blocked_by_ailment is False
    assert result.timeline_result.track_after == 6
    assert mover.attrition_spent == 1
    assert mover.concealment_states[0].observer_id == watcher.id
    assert mover.timeline.activations_taken == 1


def test_attack_action_executes_exchange_inside_atb() -> None:
    context = _initialized_hidden_crossing_context()
    execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="hide",
            observer_slot="watcher",
        ),
        rng=SimulationRNG(seed=11),
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="watcher",
            mode="action",
            definition_id="attack_one_handed",
            target_slot="mover",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    watcher = context.actors_by_slot["watcher"].combatant
    assert result.succeeded is True
    assert result.exchange_result is not None
    assert result.exchange_result.defender_id == context.actors_by_slot["mover"].combatant.id
    assert result.timeline_result.track_after == 9
    assert watcher.attrition_spent == 1
    assert watcher.timeline.activations_taken == 1


def test_technique_can_apply_ailment_inside_atb_loop() -> None:
    context = _initialized_hidden_crossing_context()

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="reir_donde_mas_suena",
            target_slot="watcher",
        ),
        rng=SimulationRNG(seed=5),
    )

    watcher = context.actors_by_slot["watcher"].combatant
    assert result.succeeded is True
    assert result.effect_results
    assert watcher.ailments[0].ailment_id == "aterrorizado"
    assert watcher.ailments[0].severity == "moderate"


def test_reir_en_la_brecha_applies_read_spoiled_on_successful_hit() -> None:
    context = _initialized_hidden_crossing_context()
    context.actors_by_slot["watcher"].combatant.attrition_spent = 4

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="reir_en_la_brecha",
            target_slot="watcher",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    watcher = context.actors_by_slot["watcher"].combatant
    assert result.succeeded is True
    assert result.exchange_result is not None
    assert result.exchange_result.attack_connected is True
    assert any(state.state_id == "read_spoiled" for state in watcher.procedural_states)


def test_atajar_el_brote_ignores_block_on_same_hit() -> None:
    context = _initialized_hidden_crossing_context()
    context.actors_by_slot["watcher"].combatant.attrition_spent = 4

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="atajar_el_brote",
            target_slot="watcher",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.succeeded is True
    assert result.exchange_result is not None
    assert result.exchange_result.attack_connected is True
    assert result.exchange_result.block_ignored == 2


def test_robar_la_orilla_repositions_user_after_successful_hit() -> None:
    context = _initialized_hidden_crossing_context()
    context.actors_by_slot["watcher"].combatant.attrition_spent = 4
    mover = context.actors_by_slot["mover"].combatant
    before_x = mover.position.x

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="robar_la_orilla",
            target_slot="watcher",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.succeeded is True
    assert result.exchange_result is not None
    assert result.exchange_result.attack_connected is True
    assert mover.position.x < before_x
    assert any(effect.effect_id == "reposition_after_hit_half_move" for effect in result.effect_results)


def test_recuperar_la_distancia_repositions_user_one_meter_after_successful_hit() -> None:
    context = _initialized_naghii_range_recovery_context()
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.attrition_spent = 4
    before_x = mover.position.x

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="recuperar_la_distancia",
            target_slot="watcher",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.succeeded is True
    assert result.exchange_result is not None
    assert result.exchange_result.attack_connected is True
    assert mover.position.x == before_x - 1
    assert any(effect.effect_id == "reposition_after_hit_distance" for effect in result.effect_results)


def test_clavar_el_paso_advances_user_two_meters_before_exchange() -> None:
    context = _initialized_naghii_range_recovery_context()
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.attrition_spent = 4
    before_x = mover.position.x

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="clavar_el_paso",
            target_slot="watcher",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.succeeded is True
    assert result.exchange_result is not None
    assert mover.position.x == before_x + 2
    assert any(effect.effect_id == "advance_before_exchange_distance" for effect in result.effect_results)


def test_doblar_el_tiro_resolves_indirect_surface_exchange() -> None:
    context = _initialized_naghii_projection_context()
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.attrition_spent = 4

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="doblar_el_tiro",
            target_slot="watcher",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.succeeded is True
    assert result.exchange_result is not None
    assert any(effect.effect_id == "indirect_surface_ranged_attack" for effect in result.effect_results)


def test_marcar_la_lectura_installs_read_marked_and_clears_on_mark_clear_event() -> None:
    context = _initialized_naghii_projection_context()
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.attrition_spent = 4

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="marcar_la_lectura",
            target_slot="watcher",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.succeeded is True
    assert any(state.state_id == "read_marked" for state in watcher.procedural_states)

    followup = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="watcher",
            mode="action",
            definition_id="attack_one_handed",
            target_slot="mover",
            zone="torso",
            fiction_events=("mark_cleared",),
        ),
        rng=SimulationRNG(seed=13),
    )

    assert followup.succeeded is True
    assert all(state.state_id != "read_marked" for state in watcher.procedural_states)


def test_nublar_la_senal_installs_signal_blurred_and_consumes_next_direct_answer() -> None:
    context = _initialized_naghii_projection_context()
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.attrition_spent = 4

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="nublar_la_senal",
            target_slot="watcher",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.succeeded is True
    assert any(state.state_id == "signal_blurred" for state in watcher.procedural_states)

    followup = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="watcher",
            mode="action",
            definition_id="attack_one_handed",
            target_slot="mover",
            zone="torso",
        ),
        rng=SimulationRNG(seed=13),
    )

    assert followup.succeeded is True
    assert all(state.state_id != "signal_blurred" for state in watcher.procedural_states)


def test_robar_el_angulo_repositions_user_and_spoils_direct_answer() -> None:
    context = _initialized_naghii_flexible_context(profile_id="naghii_novice_false_line_skirmisher")
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.attrition_spent = 4
    before_x = mover.position.x

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="robar_el_angulo",
            target_slot="watcher",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.succeeded is True
    assert result.exchange_result is not None
    assert mover.position.x != before_x
    assert any(state.state_id == "read_spoiled" for state in watcher.procedural_states)


def test_anudar_el_paso_executes_as_reaction_and_denies_clean_separation() -> None:
    context = _initialized_naghii_flexible_context(profile_id="naghii_novice_torsion_keeper")
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.attrition_spent = 4

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="anudar_el_paso",
            target_slot="watcher",
            zone="torso",
            as_reaction=True,
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.succeeded is True
    assert result.timeline_result.as_reaction is True
    assert mover.timeline.reactions_taken == 1
    assert any(state.state_id == "clean_separation_denied" for state in watcher.procedural_states)


def test_cerrar_la_linea_executes_as_reaction_and_resolves_exchange() -> None:
    context = _initialized_naghii_range_recovery_context()
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.attrition_spent = 4

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="technique",
            definition_id="cerrar_la_linea",
            target_slot="watcher",
            zone="torso",
            as_reaction=True,
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.succeeded is True
    assert result.exchange_result is not None
    assert result.timeline_result.as_reaction is True
    assert mover.timeline.reactions_taken == 1


def test_aturdido_blocks_meaningful_action_and_spends_lost_activation_window() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    initialize_context_timeline(
        context,
        situational_modifiers_by_slot={
            "mover": -1,
            "watcher": 1,
        },
    )
    watcher = context.actors_by_slot["watcher"].combatant
    watcher.ailments.append(
        ActiveAilment(
            ailment_id="aturdido",
            severity="minor",
            original_severity="minor",
            source_rank_bonus=1,
            active=True,
            threatened_next_activation=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="watcher",
            mode="action",
            definition_id="attack_one_handed",
            target_slot="mover",
            zone="torso",
        ),
        rng=SimulationRNG(seed=11),
    )

    assert result.blocked_by_ailment is True
    assert result.timeline_result.track_after == 3
    assert watcher.timeline.activations_taken == 1


def test_recovery_activation_can_clear_ailment_inside_atb_loop() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.competencies["Contencion"] = CompetencyRating(level=8, rank="adept")
    mover.ailments.append(
        ActiveAilment(
            ailment_id="aterrorizado",
            severity="moderate",
            original_severity="moderate",
            source_rank_bonus=2,
            active=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="recovery",
            definition_id="recover",
            ailment_id="aterrorizado",
        ),
        rng=SimulationRNG(seed=2),
    )

    assert result.succeeded is True
    assert result.recovery_result is not None
    assert result.recovery_result.cleared is True
    assert result.timeline_result.track_after == 6
    assert mover.attrition_spent == 1
    assert mover.ailments == []


def test_recovery_activation_failure_still_spends_atb_costs() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.ailments.append(
        ActiveAilment(
            ailment_id="aterrorizado",
            severity="moderate",
            original_severity="moderate",
            source_rank_bonus=2,
            active=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="recovery",
            definition_id="recover",
            ailment_id="aterrorizado",
        ),
        rng=SimulationRNG(seed=2),
    )

    assert result.succeeded is False
    assert result.recovery_result is not None
    assert result.recovery_result.cleared is False
    assert result.timeline_result.track_after == 6
    assert mover.attrition_spent == 1
    assert mover.ailments[0].ailment_id == "aterrorizado"


def test_conmocionado_severe_aborts_first_focus_attempt_each_activation() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.ailments.append(
        ActiveAilment(
            ailment_id="conmocionado",
            severity="severe",
            original_severity="severe",
            source_rank_bonus=2,
            active=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="focus_task",
        ),
        rng=SimulationRNG(seed=4),
    )

    assert result.succeeded is False
    assert result.blocked_by_ailment is True
    assert result.timeline_result.track_after == 6
    assert mover.attrition_spent == 1
    assert result.notes == ("activation_aborted_by_ailment_gate",)


def test_aterrorizado_severe_aborts_first_feared_line_attempt_each_activation() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.ailments.append(
        ActiveAilment(
            ailment_id="aterrorizado",
            severity="severe",
            original_severity="severe",
            source_rank_bonus=2,
            active=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="attack_one_handed",
            target_slot="watcher",
            zone="torso",
            against_feared_line=True,
        ),
        rng=SimulationRNG(seed=7),
    )

    assert result.succeeded is False
    assert result.blocked_by_ailment is True
    assert result.exchange_result is None
    assert result.timeline_result.track_after == 6
    assert mover.attrition_spent == 1
    assert result.notes == ("activation_aborted_by_ailment_gate",)


def test_activation_end_can_clear_aterrorizado_when_fiction_event_changes_line() -> None:
    context = _initialized_hidden_crossing_context()
    mover = context.actors_by_slot["mover"].combatant
    mover.ailments.append(
        ActiveAilment(
            ailment_id="aterrorizado",
            severity="moderate",
            original_severity="moderate",
            source_rank_bonus=2,
            active=True,
        )
    )

    result = execute_activation_intent(
        context=context,
        intent=ActivationIntent(
            actor_slot="mover",
            mode="action",
            definition_id="focus_task",
            fiction_events=("feared_line_changed",),
        ),
        rng=SimulationRNG(seed=4),
    )

    assert result.succeeded is True
    assert "ailment_expired_on_fiction_change" in result.notes
    assert mover.ailments == []

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.ailments_runtime import numeric_ailment_penalty, resolve_activation_start
from engine.effects import apply_effect_definition, apply_effects
from engine.resolver import instantiate_question_context
from loaders import load_technique_definitions
from models import EffectDefinition


def test_grant_hidden_state_limited_effect_creates_observer_relative_state() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    technique = {entry.id: entry for entry in load_technique_definitions()}["pasar_como_parte_del_fondo"]

    results = apply_effects(
        effects=technique.effects,
        source=mover,
        target=mover,
        observer_id=watcher.id,
        active_value=12,
    )

    assert results[0].applied is True
    assert mover.concealment_states[0].owner_id == mover.id
    assert mover.concealment_states[0].observer_id == watcher.id
    assert mover.concealment_states[0].active_value == 12


def test_technique_apply_ailment_effect_installs_aterrorizado_using_source_rank_bonus() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    technique = {entry.id: entry for entry in load_technique_definitions()}["reir_donde_mas_suena"]

    results = apply_effects(
        effects=technique.effects,
        source=mover,
        target=watcher,
        source_competency=technique.origin,
    )

    assert results[0].applied is True
    assert watcher.ailments[0].ailment_id == "aterrorizado"
    assert watcher.ailments[0].severity == "moderate"
    assert watcher.ailments[0].source_rank_bonus == 1
    assert numeric_ailment_penalty(combatant=watcher, roll_tag="dr_against_feared_line") == 1


def test_apply_procedural_state_effect_installs_read_spoiled_using_weapon_rank_bonus() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant
    technique = {entry.id: entry for entry in load_technique_definitions()}["reir_en_la_brecha"]

    results = apply_effects(
        effects=technique.effects[1:],
        source=mover,
        target=watcher,
        source_competency=technique.origin,
        activation_index=mover.timeline.activations_taken + 1,
    )

    assert results[0].applied is True
    assert watcher.procedural_states[0].state_id == "read_spoiled"
    assert watcher.procedural_states[0].source_rank_bonus == 2
    assert watcher.procedural_states[0].applies_to == ("dr_against_source", "ar_against_source")


def test_combat_exchange_style_effect_can_apply_aturdido_and_atb_feels_it() -> None:
    context = instantiate_question_context("hidden_gain_crossing_4m")
    mover = context.actors_by_slot["mover"].combatant
    watcher = context.actors_by_slot["watcher"].combatant

    result = apply_effect_definition(
        effect=EffectDefinition(
            id="apply_ailment",
            parameters={
                "ailment_id": "aturdido",
                "severity": "minor",
                "source_competency": "Dagger",
            },
        ),
        source=mover,
        target=watcher,
    )

    assert result.applied is True
    assert watcher.ailments[0].ailment_id == "aturdido"
    activation = resolve_activation_start(combatant=watcher)
    assert activation.meaningful_activation_allowed is False
    assert activation.cleared_ailments == ("aturdido",)

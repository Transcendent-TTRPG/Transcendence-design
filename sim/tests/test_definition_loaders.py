import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from loaders import (
    build_simulator_definition_context,
    load_action_definitions,
    load_ailment_definitions,
    load_technique_definitions,
)


def test_definition_context_uses_simulator_modeling_bundle() -> None:
    context = build_simulator_definition_context()

    assert context.knowledge_bundle.profile.id == "simulator_domain_modeling"
    assert {domain.id for domain in context.knowledge_bundle.domains} >= {"simulation", "techniques", "ailments", "concealment"}


def test_action_loader_reads_seed_action_data() -> None:
    definitions = load_action_definitions()

    assert definitions
    actions = {entry.id: entry for entry in definitions}
    hide = actions["hide"]
    assert hide.id == "hide"
    assert hide.roll is not None
    assert hide.roll.competency == "Sigilo"
    assert hide.effects[0].id == "grant_hidden_state"
    assert actions["focus_task"].roll is not None
    assert actions["focus_task"].roll.competency == "Enfoque"
    assert actions["brace_for_impact"].trigger_type == "reactive"
    assert actions["brace_for_impact"].effects[0].id == "reaction_defense_bonus"


def test_technique_loader_reads_seed_technique_data() -> None:
    definitions = load_technique_definitions()

    assert definitions
    techniques = {entry.id: entry for entry in definitions}
    gap = techniques["reir_en_la_brecha"]
    assert gap.origin == "Evasion"
    assert gap.effects[0].id == "weapon_exchange_primary"
    assert gap.effects[1].id == "apply_procedural_state"

    seam = techniques["abrir_la_costura"]
    assert seam.effects[1].parameters["state_id"] == "seam_opened"

    spread = techniques["atajar_el_brote"]
    assert spread.rhythm == 7
    assert spread.effects[1].id == "same_exchange_ignore_block_rank_bonus"

    edge = techniques["robar_la_orilla"]
    assert edge.effects[1].id == "reposition_after_hit_half_move"

    stealth = techniques["pasar_como_parte_del_fondo"]
    assert stealth.origin == "Sigilo"
    assert stealth.effects[0].id == "grant_hidden_state_limited"
    assert stealth.duration_model == "until_crossing_or_detection"

    fear = techniques["reir_donde_mas_suena"]
    assert fear.origin == "Intimidacion"
    assert fear.effects[0].id == "apply_ailment"
    assert fear.effects[0].parameters["ailment_id"] == "aterrorizado"

    angle = techniques["robar_el_angulo"]
    assert angle.origin == "Flexible Weapons"
    assert angle.category == "attack"
    assert angle.rhythm == 4
    assert angle.effects[0].id == "false_line_combined_resolution"
    assert angle.effects[0].parameters["reposition_meters"] == 1
    assert angle.effects[0].parameters["spoil_response"] == "rank_bonus"

    knot = techniques["anudar_el_paso"]
    assert knot.origin == "Flexible Weapons"
    assert knot.category == "attack"
    assert knot.roll is not None
    assert knot.roll.family == "specialization"
    assert knot.roll.competency == "Flexible Weapons"
    assert knot.effects[0].id == "weapon_exchange_primary"
    assert knot.effects[1].id == "deny_clean_separation_if_check_succeeds"

    pin = techniques["clavar_el_paso"]
    assert pin.origin == "Spear"
    assert pin.attrition == 1
    assert pin.effects[0].id == "advance_before_exchange_distance"
    assert pin.effects[0].parameters["meters"] == 2

    recover = techniques["recuperar_la_distancia"]
    assert recover.origin == "Spear"
    assert recover.rhythm == 5
    assert recover.effects[1].id == "reposition_after_hit_distance"
    assert recover.effects[1].parameters["meters"] == 1

    mark = techniques["marcar_la_lectura"]
    assert mark.origin == "Ranged Weapons"
    assert mark.category == "attack"
    assert mark.roll is not None
    assert mark.roll.competency == "Ranged Weapons"
    assert mark.effects[0].id == "utility_check_primary"
    assert mark.effects[1].id == "mark_immediate_route_readable"
    assert mark.effects[1].parameters["state_id"] == "read_marked"

    blur = techniques["nublar_la_senal"]
    assert blur.origin == "Ranged Weapons"
    assert blur.category == "utility"
    assert blur.roll is not None
    assert blur.roll.competency == "Ranged Weapons"
    assert blur.effects[0].id == "utility_check_primary"
    assert blur.effects[1].id == "blur_declared_sensory_channel"
    assert blur.effects[1].parameters["state_id"] == "signal_blurred"

    bend = techniques["doblar_el_tiro"]
    assert bend.origin == "Ranged Weapons"
    assert bend.category == "attack"
    assert bend.roll is not None
    assert bend.roll.competency == "Ranged Weapons"
    assert bend.effects[0].id == "indirect_surface_ranged_attack"
    assert bend.effects[0].parameters["declared_surface_count"] == 1


def test_ailment_loader_reads_seed_ailment_data() -> None:
    definitions = load_ailment_definitions()

    assert definitions
    ailments = {entry.id: entry for entry in definitions}
    assert {"aterrorizado", "aturdido", "conmocionado"} <= set(ailments)
    ailment = ailments["aterrorizado"]
    assert ailment.numeric_burden is not None
    assert ailment.numeric_burden.source == "rank_bonus"
    assert ailment.recovery is not None
    assert ailment.recovery.competency == "Contencion"
    assert ailment.timing is not None
    assert ailment.timing.expiry_mode == "fiction_change_or_recovery"
    assert ailment.timing.fiction_release_events == ("feared_line_changed",)

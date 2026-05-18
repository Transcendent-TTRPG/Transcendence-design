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

    recover = techniques["recuperar_la_distancia"]
    assert recover.origin == "Spear"
    assert recover.rhythm == 5
    assert recover.effects[1].id == "reposition_after_hit_distance"
    assert recover.effects[1].parameters["meters"] == 1


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

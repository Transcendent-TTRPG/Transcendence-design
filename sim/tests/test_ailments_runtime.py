import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.ailments_runtime import (
    action_gate,
    ailment_timing,
    apply_ailment,
    attempt_ailment_recovery,
    effective_preparation,
    numeric_ailment_penalty,
    reaction_gate,
    resolve_activation_end,
    resolve_activation_start,
)
from engine.entities import instantiate_combatant
from engine.rng import SimulationRNG
from engine.timeline import initialize_timeline
from loaders.framing import load_species_profile_definitions
from models import CompetencyRating, ScenarioDefinition


def _instantiate_profile(profile_id: str):
    profiles = {profile.id: profile for profile in load_species_profile_definitions()}
    profile = profiles[profile_id]
    return instantiate_combatant(
        slot="actor",
        profile=profile,
        scenario=ScenarioDefinition(id="unit_test"),
        side="actor",
    ).combatant


def test_apply_ailment_replaces_weaker_and_refreshes_equal() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")

    first = apply_ailment(combatant=combatant, ailment_id="aterrorizado", severity="minor", source_rank_bonus=1)
    second = apply_ailment(combatant=combatant, ailment_id="aterrorizado", severity="severe", source_rank_bonus=2)
    third = apply_ailment(combatant=combatant, ailment_id="aterrorizado", severity="severe", source_rank_bonus=3)

    assert first.applied_new is True
    assert second.replaced_existing is True
    assert third.refreshed_existing is True
    assert combatant.ailments[0].severity == "severe"
    assert combatant.ailments[0].source_rank_bonus == 3


def test_conmocionado_moderate_sets_effective_preparation_to_zero() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")

    apply_ailment(combatant=combatant, ailment_id="conmocionado", severity="moderate", source_rank_bonus=1)

    assert effective_preparation(combatant) == 0


def test_timeline_initialization_uses_effective_preparation_under_ailments() -> None:
    mover = _instantiate_profile("zarnag_novice_skirmisher")
    watcher = _instantiate_profile("common_guard_observer")
    apply_ailment(combatant=mover, ailment_id="conmocionado", severity="moderate", source_rank_bonus=1)

    result = initialize_timeline(
        combatants=(mover, watcher),
        situational_modifiers={},
    )

    assert result.reference_point == 4
    assert mover.timeline.track_position == 4
    assert watcher.timeline.track_position == 0


def test_aturdido_minor_consumes_next_activation_and_then_clears() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")
    apply_ailment(combatant=combatant, ailment_id="aturdido", severity="minor", source_rank_bonus=1)

    result = resolve_activation_start(combatant=combatant)

    assert result.meaningful_activation_allowed is False
    assert result.lost_activation_consumed is True
    assert result.cleared_ailments == ("aturdido",)
    assert combatant.ailments == []


def test_aturdido_moderate_can_persist_across_lost_activations() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")
    apply_ailment(combatant=combatant, ailment_id="aturdido", severity="moderate", source_rank_bonus=1)

    result = resolve_activation_start(combatant=combatant, recovery_success_by_ailment={"aturdido": False})

    assert result.meaningful_activation_allowed is False
    assert "aturdido" in result.remaining_ailments
    assert combatant.ailments[0].threatened_next_activation is True


def test_aturdido_severe_blocks_timing_sensitive_reactions_without_recovery() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")
    apply_ailment(combatant=combatant, ailment_id="aturdido", severity="severe", source_rank_bonus=1)

    blocked = reaction_gate(combatant=combatant, timing_sensitive=True)
    allowed = reaction_gate(
        combatant=combatant,
        timing_sensitive=True,
        recovery_success_by_ailment={"aturdido": True},
    )

    assert blocked.allowed is False
    assert blocked.blocking_ailments == ("aturdido",)
    assert allowed.allowed is True


def test_numeric_ailment_penalty_uses_rank_bonus_for_matching_roll_tags() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")
    apply_ailment(combatant=combatant, ailment_id="aturdido", severity="minor", source_rank_bonus=2)

    assert numeric_ailment_penalty(combatant=combatant, roll_tag="rr") == 2
    assert numeric_ailment_penalty(combatant=combatant, roll_tag="cr") == 2
    assert numeric_ailment_penalty(combatant=combatant, roll_tag="sr_against_feared_line") == 0


def test_attempt_ailment_recovery_clears_active_ailment_on_success() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")
    combatant.competencies["Contencion"] = CompetencyRating(level=8, rank="adept")
    apply_ailment(combatant=combatant, ailment_id="aterrorizado", severity="moderate", source_rank_bonus=2)

    result = attempt_ailment_recovery(
        combatant=combatant,
        ailment_id="aterrorizado",
        rng=SimulationRNG(seed=2),
    )

    assert result.success is True
    assert result.cleared is True
    assert result.threshold_id == "rigorous"
    assert combatant.ailments == []


def test_attempt_ailment_recovery_keeps_active_ailment_on_failure() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")
    apply_ailment(combatant=combatant, ailment_id="aterrorizado", severity="moderate", source_rank_bonus=2)

    result = attempt_ailment_recovery(
        combatant=combatant,
        ailment_id="aterrorizado",
        rng=SimulationRNG(seed=2),
    )

    assert result.success is False
    assert result.cleared is False
    assert combatant.ailments[0].ailment_id == "aterrorizado"


def test_action_gate_blocks_first_intellect_or_composure_attempt_under_severe_conmocionado() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")
    apply_ailment(combatant=combatant, ailment_id="conmocionado", severity="severe", source_rank_bonus=2)

    blocked = action_gate(
        combatant=combatant,
        competency="Enfoque",
    )
    allowed_again_same_activation = action_gate(
        combatant=combatant,
        competency="Enfoque",
    )

    assert blocked.allowed is False
    assert blocked.blocking_ailments == ("conmocionado",)
    assert combatant.ailments[0].first_gate_spent_on_activation == 1
    assert allowed_again_same_activation.allowed is True


def test_action_gate_blocks_first_feared_line_attempt_under_severe_aterrorizado() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")
    apply_ailment(combatant=combatant, ailment_id="aterrorizado", severity="severe", source_rank_bonus=2)

    blocked = action_gate(
        combatant=combatant,
        competency=None,
        against_feared_line=True,
    )
    allowed_again_same_activation = action_gate(
        combatant=combatant,
        competency=None,
        against_feared_line=True,
    )

    assert blocked.allowed is False
    assert blocked.blocking_ailments == ("aterrorizado",)
    assert combatant.ailments[0].first_gate_spent_on_activation == 1
    assert allowed_again_same_activation.allowed is True


def test_ailment_timing_profile_exposes_authored_expiry_semantics() -> None:
    timing = ailment_timing("aterrorizado")

    assert timing is not None
    assert timing.expiry_mode == "fiction_change_or_recovery"
    assert timing.fiction_release_events == ("feared_line_changed",)


def test_resolve_activation_end_clears_fiction_released_aterrorizado() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")
    apply_ailment(combatant=combatant, ailment_id="aterrorizado", severity="moderate", source_rank_bonus=2)

    result = resolve_activation_end(
        combatant=combatant,
        fiction_events=("feared_line_changed",),
    )

    assert result.cleared_ailments == ("aterrorizado",)
    assert combatant.ailments == []


def test_resolve_activation_end_does_not_clear_until_removed_ailment_without_recovery() -> None:
    combatant = _instantiate_profile("zarnag_novice_skirmisher")
    apply_ailment(combatant=combatant, ailment_id="conmocionado", severity="moderate", source_rank_bonus=2)

    result = resolve_activation_end(
        combatant=combatant,
        fiction_events=("feared_line_changed",),
    )

    assert result.cleared_ailments == ()
    assert combatant.ailments[0].ailment_id == "conmocionado"

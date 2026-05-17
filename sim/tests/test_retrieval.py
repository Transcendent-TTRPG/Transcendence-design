import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from knowledge_access import (
    for_species_completion_audit,
    for_technique_balance_audit,
    load_catalog,
    resolve_domain,
    resolve_profile,
)


def test_catalog_loads_core_retrieval_assets() -> None:
    catalog = load_catalog()

    assert "hidden_state" in catalog.concepts
    assert "hidden_roll_persistence" in catalog.decisions
    assert "concealment" in catalog.domains
    assert "simulator_domain_modeling" in catalog.profiles
    assert "knowledge_data" in catalog.source_map


def test_concealment_bundle_prefers_knowledge_then_authority() -> None:
    bundle = resolve_domain("concealment", profile_id="concealment_rule_lookup")

    assert bundle.sources
    assert "hidden_state" in bundle.concept_ids
    assert "hidden_roll_persistence" in bundle.decision_ids
    assert bundle.source_paths[0].endswith("Transcendence-design/data/knowledge/concept-registry.yaml")
    assert any(path.endswith("Transcendence-design/docs/system/cover-visibility-concealment.md") for path in bundle.source_paths)


def test_fallback_publication_sources_are_only_included_when_requested() -> None:
    without_fallback = resolve_domain("concealment", profile_id="concealment_rule_lookup", include_fallback=False)
    with_fallback = resolve_domain("concealment", profile_id="concealment_rule_lookup", include_fallback=True)

    assert all("Transcendence-publications/" not in path for path in without_fallback.source_paths)
    assert any("Transcendence-publications/" in path for path in with_fallback.source_paths)


def test_profile_can_drive_domain_resolution_without_manual_domain_input() -> None:
    bundle = resolve_profile("species_completion_audit")

    assert bundle.domains
    assert bundle.domains[0].id == "zarnag_species"
    assert "zarnag_novice_species_pass_complete" in bundle.decision_ids


def test_intent_entrypoints_return_expected_profiles_and_domains() -> None:
    species_bundle = for_species_completion_audit()
    technique_bundle = for_technique_balance_audit()

    assert species_bundle.profile.id == "species_completion_audit"
    assert species_bundle.domains[0].id == "zarnag_species"
    assert technique_bundle.profile.id == "technique_balance_audit"
    assert {domain.id for domain in technique_bundle.domains} == {"techniques", "ailments"}

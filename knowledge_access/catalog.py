"""Manifest and retrieval-profile loading."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .types import (
    ConceptRecord,
    DecisionRecord,
    KnowledgeDomain,
    RetrievalCatalog,
    RetrievalProfile,
    SourceMapEntry,
)


def _design_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_knowledge_manifest_path() -> Path:
    return _design_root() / "data" / "knowledge" / "knowledge-manifest.yaml"


def default_retrieval_profiles_path() -> Path:
    return _design_root() / "data" / "knowledge" / "retrieval-profiles.yaml"


def default_source_map_path() -> Path:
    return _design_root() / "data" / "knowledge" / "source-map.yaml"


def default_concept_registry_path() -> Path:
    return _design_root() / "data" / "knowledge" / "concept-registry.yaml"


def default_decision_registry_path() -> Path:
    return _design_root() / "data" / "knowledge" / "decision-registry.yaml"


def _load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    if not isinstance(loaded, dict):
        raise ValueError(f"Expected mapping at top level of {path}")
    return loaded


def _normalize_str_list(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        raise ValueError(f"Expected list of strings, got: {type(value)!r}")
    return tuple(str(item) for item in value)


def load_catalog(
    *,
    manifest_path: Path | None = None,
    profiles_path: Path | None = None,
    source_map_path: Path | None = None,
    concept_registry_path: Path | None = None,
    decision_registry_path: Path | None = None,
) -> RetrievalCatalog:
    """Load the retrieval catalog from default or explicit paths."""

    manifest_path = manifest_path or default_knowledge_manifest_path()
    profiles_path = profiles_path or default_retrieval_profiles_path()
    source_map_path = source_map_path or default_source_map_path()
    concept_registry_path = concept_registry_path or default_concept_registry_path()
    decision_registry_path = decision_registry_path or default_decision_registry_path()

    manifest_data = _load_yaml(manifest_path)
    profiles_data = _load_yaml(profiles_path)
    source_map_data = _load_yaml(source_map_path)
    concept_data = _load_yaml(concept_registry_path)
    decision_data = _load_yaml(decision_registry_path)

    domain_entries = manifest_data.get("knowledge_manifest", {}).get("domains", [])
    profile_entries = profiles_data.get("retrieval_profiles", [])
    source_entries = source_map_data.get("sources", [])
    concept_entries = concept_data.get("concepts", [])
    decision_entries = decision_data.get("decisions", [])

    concepts: dict[str, ConceptRecord] = {}
    for entry in concept_entries:
        concept = ConceptRecord(
            id=str(entry["id"]),
            label=str(entry["label"]),
            family=str(entry["family"]),
            canonical_terms={str(key): str(value) for key, value in dict(entry.get("canonical_terms", {})).items()},
            summary=str(entry["summary"]),
            authority_paths=_normalize_str_list(entry.get("authority_paths")),
            key_notes=_normalize_str_list(entry.get("key_notes")),
        )
        concepts[concept.id] = concept

    decisions: dict[str, DecisionRecord] = {}
    for entry in decision_entries:
        decision = DecisionRecord(
            id=str(entry["id"]),
            title=str(entry["title"]),
            status=str(entry["status"]),
            summary=str(entry["summary"]),
            authority_paths=_normalize_str_list(entry.get("authority_paths")),
            related_concepts=_normalize_str_list(entry.get("related_concepts")),
        )
        decisions[decision.id] = decision

    domains: dict[str, KnowledgeDomain] = {}
    for entry in domain_entries:
        domain = KnowledgeDomain(
            id=str(entry["id"]),
            concepts=_normalize_str_list(entry.get("concepts")),
            decisions=_normalize_str_list(entry.get("decisions")),
            preferred_sources=_normalize_str_list(entry.get("preferred_sources")),
            fallback_sources=_normalize_str_list(entry.get("fallback_sources")),
        )
        domains[domain.id] = domain

    profiles: dict[str, RetrievalProfile] = {}
    for entry in profile_entries:
        profile = RetrievalProfile(
            id=str(entry["id"]),
            purpose=str(entry["purpose"]),
            lookup_order=_normalize_str_list(entry.get("lookup_order")),
            preferred_domains=_normalize_str_list(entry.get("preferred_domains")),
            fallback_sources=_normalize_str_list(entry.get("fallback_sources")),
            notes=entry.get("notes"),
        )
        profiles[profile.id] = profile

    source_map: dict[str, SourceMapEntry] = {}
    for entry in source_entries:
        source = SourceMapEntry(
            id=str(entry["id"]),
            owner=str(entry["owner"]),
            paths=_normalize_str_list(entry.get("paths")),
            preferred_for=_normalize_str_list(entry.get("preferred_for")),
        )
        source_map[source.id] = source

    return RetrievalCatalog(
        concepts=concepts,
        decisions=decisions,
        domains=domains,
        profiles=profiles,
        source_map=source_map,
    )

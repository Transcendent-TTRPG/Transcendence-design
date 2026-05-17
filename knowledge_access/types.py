"""Typed retrieval-layer structures."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ConceptRecord:
    """One concept-registry entry."""

    id: str
    label: str
    family: str
    canonical_terms: dict[str, str]
    summary: str
    authority_paths: tuple[str, ...]
    key_notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class DecisionRecord:
    """One decision-registry entry."""

    id: str
    title: str
    status: str
    summary: str
    authority_paths: tuple[str, ...]
    related_concepts: tuple[str, ...] = ()


@dataclass(frozen=True)
class KnowledgeDomain:
    """One knowledge-manifest domain entry."""

    id: str
    concepts: tuple[str, ...]
    decisions: tuple[str, ...]
    preferred_sources: tuple[str, ...]
    fallback_sources: tuple[str, ...] = ()


@dataclass(frozen=True)
class RetrievalProfile:
    """One retrieval profile entry."""

    id: str
    purpose: str
    lookup_order: tuple[str, ...]
    preferred_domains: tuple[str, ...] = ()
    fallback_sources: tuple[str, ...] = ()
    notes: str | None = None


@dataclass(frozen=True)
class SourceMapEntry:
    """One source-map category entry."""

    id: str
    owner: str
    paths: tuple[str, ...]
    preferred_for: tuple[str, ...] = ()


@dataclass(frozen=True)
class RetrievalCatalog:
    """Loaded retrieval metadata."""

    concepts: dict[str, ConceptRecord]
    decisions: dict[str, DecisionRecord]
    domains: dict[str, KnowledgeDomain]
    profiles: dict[str, RetrievalProfile]
    source_map: dict[str, SourceMapEntry]


@dataclass(frozen=True)
class RetrievalSource:
    """One resolved source path within a retrieval bundle."""

    path: str
    category: str
    priority: int
    role: str
    domain_id: str


@dataclass(frozen=True)
class RetrievalBundle:
    """Ordered retrieval result for one or more domains."""

    profile: RetrievalProfile
    domains: tuple[KnowledgeDomain, ...]
    concepts: tuple[ConceptRecord, ...]
    decisions: tuple[DecisionRecord, ...]
    sources: tuple[RetrievalSource, ...]
    unknown_paths: tuple[str, ...] = ()

    @property
    def source_paths(self) -> tuple[str, ...]:
        return tuple(source.path for source in self.sources)

    @property
    def concept_ids(self) -> tuple[str, ...]:
        return tuple(record.id for record in self.concepts)

    @property
    def decision_ids(self) -> tuple[str, ...]:
        return tuple(record.id for record in self.decisions)


@dataclass(frozen=True, kw_only=True)
class RetrievalQuery:
    """High-level retrieval request."""

    domains: tuple[str, ...] = ()
    profile_id: str
    include_fallback: bool = False
    notes: str | None = None

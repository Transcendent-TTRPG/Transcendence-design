"""Retrieval bundle assembly."""

from __future__ import annotations

from .selector import classify_source_path, get_domain, get_profile
from .types import RetrievalBundle, RetrievalCatalog, RetrievalSource


def build_bundle(
    catalog: RetrievalCatalog,
    *,
    domain_ids: list[str] | tuple[str, ...],
    profile_id: str,
    include_fallback: bool = False,
) -> RetrievalBundle:
    """Build an ordered retrieval bundle for the given domains and profile."""

    profile = get_profile(catalog, profile_id)
    domains = tuple(get_domain(catalog, domain_id) for domain_id in domain_ids)
    concept_records = []
    decision_records = []
    seen_concepts: set[str] = set()
    seen_decisions: set[str] = set()

    category_priority = {category: index for index, category in enumerate(profile.lookup_order)}
    resolved_sources: list[RetrievalSource] = []
    unknown_paths: list[str] = []
    seen_paths: set[str] = set()

    for domain in domains:
        for concept_id in domain.concepts:
            if concept_id in seen_concepts:
                continue
            seen_concepts.add(concept_id)
            concept_records.append(catalog.concepts[concept_id])

        for decision_id in domain.decisions:
            if decision_id in seen_decisions:
                continue
            seen_decisions.add(decision_id)
            decision_records.append(catalog.decisions[decision_id])

        domain_paths = list(domain.preferred_sources)
        if include_fallback:
            domain_paths.extend(domain.fallback_sources)

        for path in domain_paths:
            if path in seen_paths:
                continue
            seen_paths.add(path)

            category = classify_source_path(catalog, path)
            if category is None:
                unknown_paths.append(path)
                continue

            resolved_sources.append(
                RetrievalSource(
                    path=path,
                    category=category,
                    priority=category_priority.get(category, len(category_priority) + 100),
                    role="fallback" if path in domain.fallback_sources else "preferred",
                    domain_id=domain.id,
                )
            )

    resolved_sources.sort(key=lambda source: (source.priority, source.domain_id, source.path))

    return RetrievalBundle(
        profile=profile,
        domains=domains,
        concepts=tuple(concept_records),
        decisions=tuple(decision_records),
        sources=tuple(resolved_sources),
        unknown_paths=tuple(unknown_paths),
    )

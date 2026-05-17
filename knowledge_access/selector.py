"""Domain and source selection logic."""

from __future__ import annotations

from pathlib import Path

from .types import KnowledgeDomain, RetrievalCatalog, RetrievalProfile


def get_domain(catalog: RetrievalCatalog, domain_id: str) -> KnowledgeDomain:
    try:
        return catalog.domains[domain_id]
    except KeyError as exc:
        raise KeyError(f"Unknown knowledge domain: {domain_id}") from exc


def get_profile(catalog: RetrievalCatalog, profile_id: str) -> RetrievalProfile:
    try:
        return catalog.profiles[profile_id]
    except KeyError as exc:
        raise KeyError(f"Unknown retrieval profile: {profile_id}") from exc


def classify_source_path(catalog: RetrievalCatalog, path: str) -> str | None:
    """Return the source-map category id that best matches the path."""

    normalized = Path(path).as_posix()
    best_match: tuple[int, str] | None = None

    for category_id, entry in catalog.source_map.items():
        for base_path in entry.paths:
            normalized_base = Path(base_path).as_posix()
            if normalized.startswith(normalized_base):
                score = len(normalized_base)
                if best_match is None or score > best_match[0]:
                    best_match = (score, category_id)

    return None if best_match is None else best_match[1]

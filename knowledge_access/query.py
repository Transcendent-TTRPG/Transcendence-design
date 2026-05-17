"""High-level retrieval query interface."""

from __future__ import annotations

from .catalog import load_catalog
from .resolver import build_bundle
from .selector import get_profile
from .types import RetrievalBundle, RetrievalCatalog, RetrievalQuery


def _resolve_effective_domains(
    *,
    query: RetrievalQuery,
    catalog: RetrievalCatalog,
) -> tuple[str, ...]:
    if query.domains:
        return query.domains

    profile = get_profile(catalog, query.profile_id)
    if profile.preferred_domains:
        return profile.preferred_domains

    raise ValueError(
        f"Query for profile '{query.profile_id}' did not provide domains and the "
        "profile has no preferred_domains."
    )


def resolve_query(
    query: RetrievalQuery,
    *,
    catalog: RetrievalCatalog | None = None,
) -> RetrievalBundle:
    """Resolve one retrieval query against the local knowledge catalog."""

    catalog = catalog or load_catalog()
    effective_domains = _resolve_effective_domains(query=query, catalog=catalog)
    return build_bundle(
        catalog,
        domain_ids=effective_domains,
        profile_id=query.profile_id,
        include_fallback=query.include_fallback,
    )


def resolve_domain(
    domain_id: str,
    *,
    profile_id: str,
    include_fallback: bool = False,
    catalog: RetrievalCatalog | None = None,
) -> RetrievalBundle:
    """Convenience helper for a single-domain retrieval request."""

    query = RetrievalQuery(
        domains=(domain_id,),
        profile_id=profile_id,
        include_fallback=include_fallback,
    )
    return resolve_query(query, catalog=catalog)


def resolve_profile(
    profile_id: str,
    *,
    include_fallback: bool = False,
    catalog: RetrievalCatalog | None = None,
    domains: tuple[str, ...] | None = None,
    notes: str | None = None,
) -> RetrievalBundle:
    """Resolve retrieval using a work-profile first, optionally overriding domains."""

    query = RetrievalQuery(
        domains=domains or (),
        profile_id=profile_id,
        include_fallback=include_fallback,
        notes=notes,
    )
    return resolve_query(query, catalog=catalog)

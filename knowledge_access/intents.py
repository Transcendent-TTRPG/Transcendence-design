"""Task-oriented entrypoints for common project knowledge workflows."""

from __future__ import annotations

from .query import resolve_profile
from .types import RetrievalBundle, RetrievalCatalog


def for_simulator_domain_modeling(
    *,
    include_fallback: bool = False,
    catalog: RetrievalCatalog | None = None,
) -> RetrievalBundle:
    """Resolve the bundle used to design simulator domain objects."""

    return resolve_profile(
        "simulator_domain_modeling",
        include_fallback=include_fallback,
        catalog=catalog,
    )


def for_concealment_rule_lookup(
    *,
    include_fallback: bool = False,
    catalog: RetrievalCatalog | None = None,
) -> RetrievalBundle:
    """Resolve the bundle used for concealment rule work."""

    return resolve_profile(
        "concealment_rule_lookup",
        include_fallback=include_fallback,
        catalog=catalog,
    )


def for_ailment_doctrine_lookup(
    *,
    include_fallback: bool = False,
    catalog: RetrievalCatalog | None = None,
) -> RetrievalBundle:
    """Resolve the bundle used for ailment doctrine and taxonomy review."""

    return resolve_profile(
        "ailment_doctrine_lookup",
        include_fallback=include_fallback,
        catalog=catalog,
    )


def for_technique_balance_audit(
    *,
    include_fallback: bool = False,
    catalog: RetrievalCatalog | None = None,
) -> RetrievalBundle:
    """Resolve the bundle used for technique identity and balance review."""

    return resolve_profile(
        "technique_balance_audit",
        include_fallback=include_fallback,
        catalog=catalog,
    )


def for_species_completion_audit(
    *,
    include_fallback: bool = False,
    catalog: RetrievalCatalog | None = None,
) -> RetrievalBundle:
    """Resolve the bundle used for species coverage and completion review."""

    return resolve_profile(
        "species_completion_audit",
        include_fallback=include_fallback,
        catalog=catalog,
    )

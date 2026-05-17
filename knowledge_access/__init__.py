"""Project-wide local retrieval layer for knowledge and authority sources."""

from .catalog import load_catalog
from .intents import (
    for_ailment_doctrine_lookup,
    for_concealment_rule_lookup,
    for_simulator_domain_modeling,
    for_species_completion_audit,
    for_technique_balance_audit,
)
from .query import resolve_domain, resolve_profile, resolve_query
from .types import (
    ConceptRecord,
    DecisionRecord,
    KnowledgeDomain,
    RetrievalBundle,
    RetrievalCatalog,
    RetrievalProfile,
    RetrievalQuery,
    RetrievalSource,
    SourceMapEntry,
)

__all__ = [
    "KnowledgeDomain",
    "ConceptRecord",
    "DecisionRecord",
    "RetrievalBundle",
    "RetrievalCatalog",
    "RetrievalProfile",
    "RetrievalQuery",
    "RetrievalSource",
    "SourceMapEntry",
    "load_catalog",
    "for_ailment_doctrine_lookup",
    "for_concealment_rule_lookup",
    "for_simulator_domain_modeling",
    "for_species_completion_audit",
    "for_technique_balance_audit",
    "resolve_domain",
    "resolve_profile",
    "resolve_query",
]

"""Typed simulation domain models."""

from .action_def import ActionDefinition, EffectDefinition, RollDefinition
from .ailment_def import (
    AilmentDefinition,
    AilmentTimingDefinition,
    NumericBurdenDefinition,
    RecoveryDefinition,
)
from .combatant import ActiveAilment, Combatant, GridPosition, TimelineState, ZoneState
from .competency import CompetencyRating
from .concealment_state import ConcealmentState
from .damage_model import CreatureZoneDefinition, CreatureZoneState, DamageModelDefinition
from .equipment_state import ArmorZoneLoadout, ShieldLoadout, WeaponLoadout
from .environment_def import EnvironmentDefinition
from .profile_def import CombatantProfileDefinition
from .question_def import ActorAssignment, QuestionDefinition
from .result_def import AggregateMetric, ExperimentResult, IterationResult, RollOutcome
from .scenario_def import MapDefinition, ScenarioActorSlot, ScenarioDefinition
from .technique_def import TechniqueDefinition, TechniqueRequirements

__all__ = [
    "ActionDefinition",
    "ActiveAilment",
    "ActorAssignment",
    "AggregateMetric",
    "ArmorZoneLoadout",
    "AilmentDefinition",
    "AilmentTimingDefinition",
    "Combatant",
    "CompetencyRating",
    "CombatantProfileDefinition",
    "ConcealmentState",
    "CreatureZoneDefinition",
    "CreatureZoneState",
    "EnvironmentDefinition",
    "EffectDefinition",
    "ExperimentResult",
    "GridPosition",
    "IterationResult",
    "DamageModelDefinition",
    "MapDefinition",
    "NumericBurdenDefinition",
    "QuestionDefinition",
    "RecoveryDefinition",
    "RollDefinition",
    "RollOutcome",
    "ScenarioActorSlot",
    "ScenarioDefinition",
    "ShieldLoadout",
    "WeaponLoadout",
    "TechniqueDefinition",
    "TechniqueRequirements",
    "TimelineState",
    "ZoneState",
]

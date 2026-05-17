"""Combatant state containers and experiment instantiation helpers."""

from __future__ import annotations

from dataclasses import dataclass, field

from models import (
    Combatant,
    CombatantProfileDefinition,
    CreatureZoneState,
    EnvironmentDefinition,
    GridPosition,
    QuestionDefinition,
    ScenarioActorSlot,
    ScenarioDefinition,
    TimelineState,
)
from .zones import default_zone_states


@dataclass(frozen=True)
class InstantiatedActor:
    """Runtime combatant plus the framing metadata that placed it in the context."""

    slot: str
    profile: CombatantProfileDefinition
    combatant: Combatant
    policy_id: str | None = None


@dataclass(frozen=True)
class ExperimentContext:
    """Fully instantiated runtime context for one question and one scenario."""

    question: QuestionDefinition
    scenario: ScenarioDefinition
    environment: EnvironmentDefinition | None
    actors: tuple[InstantiatedActor, ...]
    conditions: tuple[str, ...] = ()
    observer_relations: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()

    @property
    def actors_by_slot(self) -> dict[str, InstantiatedActor]:
        return {actor.slot: actor for actor in self.actors}


def _slot_position(slot: str, actor_slots: tuple[ScenarioActorSlot, ...]) -> GridPosition:
    for actor_slot in actor_slots:
        if actor_slot.slot == slot:
            return actor_slot.position
    return GridPosition(0, 0)


def instantiate_combatant(
    *,
    slot: str,
    profile: CombatantProfileDefinition,
    scenario: ScenarioDefinition,
    side: str,
    policy_id: str | None = None,
) -> InstantiatedActor:
    """Instantiate one combatant from a profile inside a scenario slot."""

    position = _slot_position(slot, scenario.actor_slots)
    primary_policy = policy_id or profile.policy_defaults.get("primary")
    combatant = Combatant(
        id=f"{slot}:{profile.id}",
        name=profile.id,
        side=side,
        species=profile.species,
        profile_id=profile.id,
        damage_model_kind=profile.damage_model.kind,
        position=position,
        movement_meters=profile.movement_meters,
        preparation=profile.preparation,
        characteristics=dict(profile.characteristics),
        competencies=dict(profile.competencies),
        armor_zones={entry.zone: entry for entry in profile.armor_zones},
        shield=profile.shield,
        weapons={entry.slot: entry for entry in profile.weapons},
        techniques=profile.techniques,
        timeline=TimelineState(preparation=profile.preparation),
        zones=default_zone_states() if profile.damage_model.kind == "player_wounds" else [],
        creature_zones=[
            CreatureZoneState(
                id=entry.id,
                max_hp=entry.max_hp,
                current_hp=entry.max_hp,
                block=entry.block,
                dr_bonus=entry.dr_bonus,
                max_durability=entry.durability,
                durability=entry.durability,
                linked_abilities=entry.linked_abilities,
                vital=entry.vital,
                notes=entry.notes,
            )
            for entry in profile.damage_model.creature_zones
        ],
        tags=profile.zones,
        notes=profile.notes,
    )
    return InstantiatedActor(
        slot=slot,
        profile=profile,
        combatant=combatant,
        policy_id=primary_policy,
    )


def build_experiment_context(
    *,
    question: QuestionDefinition,
    scenario: ScenarioDefinition,
    environment: EnvironmentDefinition | None,
    profiles_by_id: dict[str, CombatantProfileDefinition],
) -> ExperimentContext:
    """Build a runtime experiment context from a question, scenario, and profile map."""

    actors: list[InstantiatedActor] = []
    for assignment in question.actor_assignments:
        try:
            profile = profiles_by_id[assignment.profile_id]
        except KeyError as exc:
            raise KeyError(
                f"Question '{question.id}' references unknown profile '{assignment.profile_id}'."
            ) from exc

        side = "observer" if "watch" in assignment.slot or "source" in assignment.slot else "actor"
        instantiated = instantiate_combatant(
            slot=assignment.slot,
            profile=profile,
            scenario=scenario,
            side=side,
            policy_id=question.policy_assignments.get(assignment.slot),
        )
        actors.append(instantiated)

    return ExperimentContext(
        question=question,
        scenario=scenario,
        environment=environment,
        actors=tuple(actors),
        conditions=scenario.conditions,
        observer_relations=scenario.observer_relations,
    )

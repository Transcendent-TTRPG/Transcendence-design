"""Top-level instantiation and future resolution coordinator."""

from __future__ import annotations

from dataclasses import dataclass

from loaders import (
    load_environment_definitions,
    load_question_definitions,
    load_scenario_definitions,
    load_species_profile_definitions,
)
from models import (
    CombatantProfileDefinition,
    EnvironmentDefinition,
    QuestionDefinition,
    ScenarioDefinition,
)

from .entities import ExperimentContext, build_experiment_context


@dataclass(frozen=True)
class LoadedSimulationInputs:
    """Loaded simulator-facing definitions required for experiment instantiation."""

    profiles: tuple[CombatantProfileDefinition, ...]
    environments: tuple[EnvironmentDefinition, ...]
    scenarios: tuple[ScenarioDefinition, ...]
    questions: tuple[QuestionDefinition, ...]

    @property
    def profiles_by_id(self) -> dict[str, CombatantProfileDefinition]:
        return {profile.id: profile for profile in self.profiles}

    @property
    def scenarios_by_id(self) -> dict[str, ScenarioDefinition]:
        return {scenario.id: scenario for scenario in self.scenarios}

    @property
    def environments_by_id(self) -> dict[str, EnvironmentDefinition]:
        return {environment.id: environment for environment in self.environments}

    @property
    def questions_by_id(self) -> dict[str, QuestionDefinition]:
        return {question.id: question for question in self.questions}


def load_simulation_inputs() -> LoadedSimulationInputs:
    """Load the current seed framing inputs needed to instantiate contexts."""

    return LoadedSimulationInputs(
        profiles=load_species_profile_definitions(),
        environments=load_environment_definitions(),
        scenarios=load_scenario_definitions(),
        questions=load_question_definitions(),
    )


def instantiate_question_context(
    question_id: str,
    *,
    inputs: LoadedSimulationInputs | None = None,
) -> ExperimentContext:
    """Instantiate one question into a runtime experiment context."""

    inputs = inputs or load_simulation_inputs()
    try:
        question = inputs.questions_by_id[question_id]
    except KeyError as exc:
        raise KeyError(f"Unknown question id: {question_id}") from exc

    try:
        scenario = inputs.scenarios_by_id[question.scenario_id]
    except KeyError as exc:
        raise KeyError(
            f"Question '{question.id}' references unknown scenario '{question.scenario_id}'."
        ) from exc

    environment = None
    if scenario.environment_id is not None:
        environment = inputs.environments_by_id.get(scenario.environment_id)

    return build_experiment_context(
        question=question,
        scenario=scenario,
        environment=environment,
        profiles_by_id=inputs.profiles_by_id,
    )

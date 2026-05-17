"""Runtime application and ATB-facing interpretation of ailments."""

from __future__ import annotations

from dataclasses import dataclass

from loaders import load_ailment_definitions
from models import ActiveAilment, AilmentDefinition, Combatant
from .dice import (
    associated_characteristic,
    canonical_characteristic_name,
    characteristic_value,
    difficulty_target,
    resolve_threshold,
    specialization_roll,
)
from .rng import SimulationRNG


SEVERITY_ORDER: dict[str, int] = {
    "minor": 1,
    "moderate": 2,
    "severe": 3,
}


@dataclass(frozen=True)
class AilmentApplicationResult:
    """Result of applying or refreshing one ailment instance."""

    ailment_id: str
    severity: str
    replaced_existing: bool
    refreshed_existing: bool
    applied_new: bool


@dataclass(frozen=True)
class ActivationAilmentResult:
    """ATB-facing result of processing ailments at activation start."""

    meaningful_activation_allowed: bool
    lost_activation_consumed: bool
    cleared_ailments: tuple[str, ...]
    remaining_ailments: tuple[str, ...]
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class AilmentReactionGateResult:
    """Whether a timing-sensitive reaction is currently legal under ailments."""

    allowed: bool
    blocking_ailments: tuple[str, ...]
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class AilmentRecoveryRollResult:
    """Result of one explicit or implicit ailment recovery attempt."""

    ailment_id: str
    competency: str
    threshold_id: str
    success: bool
    rolled_total: int
    target: int
    cleared: bool


@dataclass(frozen=True)
class AilmentExpiryResult:
    """Result of processing end-of-activation persistence and expiry hooks."""

    cleared_ailments: tuple[str, ...]
    remaining_ailments: tuple[str, ...]
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class AilmentActionGateResult:
    """Whether an activation attempt is allowed to proceed under active ailments."""

    allowed: bool
    blocking_ailments: tuple[str, ...]
    consumed_first_gate: tuple[str, ...]
    notes: tuple[str, ...] = ()


SEVERITY_THRESHOLD_BY_NAME: dict[str, str] = {
    "minor": "challenging",
    "moderate": "rigorous",
    "severe": "demanding",
}


def ailment_definitions_by_id() -> dict[str, AilmentDefinition]:
    """Load simulation-facing ailment definitions into an id map."""

    return {entry.id: entry for entry in load_ailment_definitions()}


def ailment_timing(ailment_id: str):
    """Return the timing definition for one ailment if authored."""

    return ailment_definitions_by_id()[ailment_id].timing


def severity_threshold_id(severity: str) -> str:
    """Map ailment severity to the canonical recovery threshold band."""

    try:
        return SEVERITY_THRESHOLD_BY_NAME[severity.casefold()]
    except KeyError as exc:
        raise KeyError(f"Unknown ailment severity for threshold mapping: {severity}") from exc


def _severity_value(severity: str) -> int:
    try:
        return SEVERITY_ORDER[severity.casefold()]
    except KeyError as exc:
        raise KeyError(f"Unknown ailment severity: {severity}") from exc


def get_active_ailment(combatant: Combatant, ailment_id: str) -> ActiveAilment | None:
    """Return the current active instance of one ailment if present."""

    for ailment in combatant.ailments:
        if ailment.ailment_id == ailment_id and ailment.active:
            return ailment
    return None


def apply_ailment(
    *,
    combatant: Combatant,
    ailment_id: str,
    severity: str,
    source_id: str | None = None,
    source_rank_bonus: int = 0,
    applied_on_activation: int | None = None,
) -> AilmentApplicationResult:
    """Apply one ailment, replacing weaker copies and refreshing equal ones."""

    existing_index = next(
        (index for index, ailment in enumerate(combatant.ailments) if ailment.ailment_id == ailment_id),
        None,
    )
    threatened_next_activation = ailment_id == "aturdido"
    new_ailment = ActiveAilment(
        ailment_id=ailment_id,
        severity=severity,
        original_severity=severity,
        source_id=source_id,
        source_rank_bonus=source_rank_bonus,
        active=True,
        applied_on_activation=applied_on_activation,
        threatened_next_activation=threatened_next_activation,
    )

    if existing_index is None:
        combatant.ailments.append(new_ailment)
        return AilmentApplicationResult(
            ailment_id=ailment_id,
            severity=severity,
            replaced_existing=False,
            refreshed_existing=False,
            applied_new=True,
        )

    existing = combatant.ailments[existing_index]
    if _severity_value(severity) >= _severity_value(existing.severity):
        refreshed = _severity_value(severity) == _severity_value(existing.severity)
        combatant.ailments[existing_index] = new_ailment
        return AilmentApplicationResult(
            ailment_id=ailment_id,
            severity=severity,
            replaced_existing=not refreshed,
            refreshed_existing=refreshed,
            applied_new=False,
        )

    return AilmentApplicationResult(
        ailment_id=ailment_id,
        severity=existing.severity,
        replaced_existing=False,
        refreshed_existing=False,
        applied_new=False,
    )


def effective_preparation(combatant: Combatant) -> int:
    """Return the preparation value currently usable under active ailments."""

    for ailment in combatant.ailments:
        if not ailment.active:
            continue
        severity = ailment.severity.casefold()
        if ailment.ailment_id in {"aturdido", "conmocionado"} and severity in {"moderate", "severe"}:
            return 0
    return combatant.preparation


def numeric_ailment_penalty(
    *,
    combatant: Combatant,
    roll_tag: str,
) -> int:
    """Return the total numeric ailment burden currently relevant to one roll tag."""

    definitions = ailment_definitions_by_id()
    total = 0
    for ailment in combatant.ailments:
        if not ailment.active:
            continue
        definition = definitions.get(ailment.ailment_id)
        if definition is None or definition.numeric_burden is None:
            continue
        if roll_tag in definition.numeric_burden.applies_to:
            total += ailment.source_rank_bonus
    return total


def resolve_activation_start(
    *,
    combatant: Combatant,
    recovery_success_by_ailment: dict[str, bool] | None = None,
) -> ActivationAilmentResult:
    """Process ailment effects that trigger when a combatant becomes leftmost on the ATB."""

    recovery_success_by_ailment = recovery_success_by_ailment or {}
    meaningful_activation_allowed = True
    lost_activation_consumed = False
    cleared_ailments: list[str] = []
    remaining_ailments: list[str] = []
    updated: list[ActiveAilment] = []

    current_activation = combatant.timeline.activations_taken + 1
    for ailment in combatant.ailments:
        if not ailment.active:
            updated.append(ailment)
            continue

        if ailment.ailment_id == "aturdido" and ailment.threatened_next_activation:
            meaningful_activation_allowed = False
            lost_activation_consumed = True
            severity = ailment.severity.casefold()
            if severity == "minor":
                cleared_ailments.append("aturdido")
                continue

            recovery_success = recovery_success_by_ailment.get("aturdido", False)
            if recovery_success:
                cleared_ailments.append("aturdido")
                continue

            updated.append(
                ActiveAilment(
                    ailment_id=ailment.ailment_id,
                    severity=ailment.severity,
                    original_severity=ailment.original_severity,
                    source_id=ailment.source_id,
                    source_rank_bonus=ailment.source_rank_bonus,
                    active=True,
                    applied_on_activation=ailment.applied_on_activation,
                    threatened_next_activation=True,
                    last_activation_processed=current_activation,
                    first_gate_spent_on_activation=ailment.first_gate_spent_on_activation,
                    notes=ailment.notes,
                )
            )
            remaining_ailments.append("aturdido")
            continue

        updated.append(
            ActiveAilment(
                ailment_id=ailment.ailment_id,
                severity=ailment.severity,
                original_severity=ailment.original_severity,
                source_id=ailment.source_id,
                source_rank_bonus=ailment.source_rank_bonus,
                active=ailment.active,
                applied_on_activation=ailment.applied_on_activation,
                threatened_next_activation=ailment.threatened_next_activation,
                last_activation_processed=current_activation,
                first_gate_spent_on_activation=ailment.first_gate_spent_on_activation,
                notes=ailment.notes,
            )
        )
        remaining_ailments.append(ailment.ailment_id)

    combatant.ailments = updated
    return ActivationAilmentResult(
        meaningful_activation_allowed=meaningful_activation_allowed,
        lost_activation_consumed=lost_activation_consumed,
        cleared_ailments=tuple(cleared_ailments),
        remaining_ailments=tuple(remaining_ailments),
        notes=(
            ("meaningful_activation_blocked_by_aturdido",)
            if lost_activation_consumed
            else ()
        ),
    )


def reaction_gate(
    *,
    combatant: Combatant,
    timing_sensitive: bool,
    recovery_success_by_ailment: dict[str, bool] | None = None,
) -> AilmentReactionGateResult:
    """Check whether timing-sensitive reactions are legal under active ailments."""

    if not timing_sensitive:
        return AilmentReactionGateResult(allowed=True, blocking_ailments=())

    recovery_success_by_ailment = recovery_success_by_ailment or {}
    blocking: list[str] = []
    for ailment in combatant.ailments:
        if not ailment.active:
            continue
        if ailment.ailment_id == "aturdido" and ailment.severity.casefold() == "severe":
            if not recovery_success_by_ailment.get("aturdido", False):
                blocking.append("aturdido")

    return AilmentReactionGateResult(
        allowed=not blocking,
        blocking_ailments=tuple(blocking),
        notes=("timing_sensitive_reaction_blocked",) if blocking else (),
    )


def _replace_active_ailment(
    *,
    combatant: Combatant,
    updated_ailment: ActiveAilment,
) -> None:
    combatant.ailments = [
        updated_ailment
        if current.ailment_id == updated_ailment.ailment_id and current.active
        else current
        for current in combatant.ailments
    ]


def action_gate(
    *,
    combatant: Combatant,
    competency: str | None,
    against_feared_line: bool = False,
    is_recovery_attempt: bool = False,
    recovery_success_by_ailment: dict[str, bool] | None = None,
) -> AilmentActionGateResult:
    """Check whether an activation attempt is aborted by first-gate ailment pressure."""

    recovery_success_by_ailment = recovery_success_by_ailment or {}
    blocking: list[str] = []
    consumed: list[str] = []
    current_activation = combatant.timeline.activations_taken + 1
    associated = None if competency is None else associated_characteristic(competency)
    canonical_associated = None if associated is None else canonical_characteristic_name(associated)

    for ailment in list(combatant.ailments):
        if not ailment.active:
            continue
        if ailment.first_gate_spent_on_activation == current_activation:
            continue

        if ailment.ailment_id == "conmocionado" and ailment.severity.casefold() == "severe":
            if is_recovery_attempt:
                continue
            if canonical_associated in {"Composure", "Intellect"} and not recovery_success_by_ailment.get("conmocionado", False):
                blocking.append("conmocionado")
                consumed.append("conmocionado")
                _replace_active_ailment(
                    combatant=combatant,
                    updated_ailment=ActiveAilment(
                        ailment_id=ailment.ailment_id,
                        severity=ailment.severity,
                        original_severity=ailment.original_severity,
                        source_id=ailment.source_id,
                        source_rank_bonus=ailment.source_rank_bonus,
                        active=True,
                        applied_on_activation=ailment.applied_on_activation,
                        threatened_next_activation=ailment.threatened_next_activation,
                        last_activation_processed=ailment.last_activation_processed,
                        first_gate_spent_on_activation=current_activation,
                        notes=ailment.notes,
                    ),
                )
                continue

        if ailment.ailment_id == "aterrorizado" and ailment.severity.casefold() == "severe":
            if against_feared_line and not recovery_success_by_ailment.get("aterrorizado", False):
                blocking.append("aterrorizado")
                consumed.append("aterrorizado")
                _replace_active_ailment(
                    combatant=combatant,
                    updated_ailment=ActiveAilment(
                        ailment_id=ailment.ailment_id,
                        severity=ailment.severity,
                        original_severity=ailment.original_severity,
                        source_id=ailment.source_id,
                        source_rank_bonus=ailment.source_rank_bonus,
                        active=True,
                        applied_on_activation=ailment.applied_on_activation,
                        threatened_next_activation=ailment.threatened_next_activation,
                        last_activation_processed=ailment.last_activation_processed,
                        first_gate_spent_on_activation=current_activation,
                        notes=ailment.notes,
                    ),
                )
                continue

    return AilmentActionGateResult(
        allowed=not blocking,
        blocking_ailments=tuple(blocking),
        consumed_first_gate=tuple(consumed),
        notes=("activation_aborted_by_ailment_gate",) if blocking else (),
    )


def attempt_ailment_recovery(
    *,
    combatant: Combatant,
    ailment_id: str,
    rng: SimulationRNG,
    scene_bonus: int = 0,
    scene_penalty: int = 0,
) -> AilmentRecoveryRollResult:
    """Attempt an explicit recovery roll for one active ailment."""

    active = get_active_ailment(combatant, ailment_id)
    if active is None:
        raise KeyError(f"Combatant '{combatant.id}' has no active ailment '{ailment_id}'.")

    definition = ailment_definitions_by_id()[ailment_id]
    if definition.recovery is None or definition.recovery.type != "specialization_roll":
        raise ValueError(f"Ailment '{ailment_id}' has no specialization-roll recovery path.")
    if definition.recovery.competency is None:
        raise ValueError(f"Ailment '{ailment_id}' recovery is missing competency.")

    competency = definition.recovery.competency
    rating = combatant.competencies.get(competency)
    characteristic_name = competency
    associated = associated_characteristic(competency)
    if associated is not None:
        characteristic_name = associated
    roll = specialization_roll(
        competency=competency,
        level=0 if rating is None else rating.level,
        rank=None if rating is None else rating.rank,
        rng=rng,
        characteristic_modifier=characteristic_value(combatant.characteristics, characteristic_name),
        bonus_modifier=scene_bonus,
        penalty_modifier=scene_penalty,
    )

    threshold_id = severity_threshold_id(active.original_severity or active.severity)
    threshold = difficulty_target(threshold_id, reference_level=0)
    outcome = resolve_threshold(roll, threshold_id=threshold_id, reference_level=0)

    cleared = False
    if outcome.success:
        combatant.ailments = [
            ailment
            for ailment in combatant.ailments
            if not (ailment.ailment_id == ailment_id and ailment.active)
        ]
        cleared = True

    return AilmentRecoveryRollResult(
        ailment_id=ailment_id,
        competency=competency,
        threshold_id=threshold_id,
        success=outcome.success,
        rolled_total=roll.total,
        target=threshold,
        cleared=cleared,
    )


def resolve_activation_end(
    *,
    combatant: Combatant,
    fiction_events: tuple[str, ...] = (),
) -> AilmentExpiryResult:
    """Process ailment expiry hooks that are evaluated after one activation resolves."""

    definitions = ailment_definitions_by_id()
    active_events = set(fiction_events)
    cleared: list[str] = []
    remaining: list[str] = []
    updated: list[ActiveAilment] = []

    for ailment in combatant.ailments:
        if not ailment.active:
            updated.append(ailment)
            continue

        definition = definitions.get(ailment.ailment_id)
        timing = None if definition is None else definition.timing
        expiry_mode = None if timing is None else timing.expiry_mode
        release_events = set(() if timing is None else timing.fiction_release_events)

        if expiry_mode == "fiction_change_or_recovery" and active_events.intersection(release_events):
            cleared.append(ailment.ailment_id)
            continue

        updated.append(ailment)
        remaining.append(ailment.ailment_id)

    combatant.ailments = updated
    return AilmentExpiryResult(
        cleared_ailments=tuple(cleared),
        remaining_ailments=tuple(remaining),
        notes=("ailment_expired_on_fiction_change",) if cleared else (),
    )

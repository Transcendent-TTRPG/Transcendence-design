"""Combatant runtime models."""

from __future__ import annotations

from dataclasses import dataclass, field

from .competency import CompetencyRating
from .concealment_state import ConcealmentState
from .damage_model import CreatureZoneState
from .equipment_state import ArmorZoneLoadout, ShieldLoadout, WeaponLoadout


@dataclass(frozen=True)
class GridPosition:
    """Meter-based grid position."""

    x: int
    y: int


@dataclass(frozen=True)
class TimelineState:
    """ATB and activation runtime state."""

    preparation: int
    track_position: int | None = None
    pending_activation: bool = False
    lost_activation: bool = False
    activations_taken: int = 0
    reactions_taken: int = 0
    last_rhythm_cost: int | None = None
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ZoneState:
    """Runtime state for one body zone or operational subsystem."""

    id: str
    capacity: int = 0
    occupied_slots: int = 0
    operational: bool = True
    saturated: bool = False
    collapsed: bool = False
    tags: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ActiveAilment:
    """Applied ailment instance on a combatant."""

    ailment_id: str
    severity: str
    source_id: str | None = None
    source_rank_bonus: int = 0
    original_severity: str | None = None
    active: bool = True
    applied_on_activation: int | None = None
    threatened_next_activation: bool = False
    last_activation_processed: int | None = None
    first_gate_spent_on_activation: int | None = None
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ProceduralState:
    """Applied non-ailment procedural state on a combatant."""

    state_id: str
    source_id: str | None = None
    source_rank_bonus: int = 0
    active: bool = True
    applies_to: tuple[str, ...] = ()
    remaining_uses: int | None = None
    expires_on_owner_activation_end: int | None = None
    expires_on_source_activation_end: int | None = None
    notes: tuple[str, ...] = ()


@dataclass
class Combatant:
    """One instantiated actor in simulation runtime."""

    id: str
    name: str
    side: str
    species: str | None = None
    profile_id: str | None = None
    damage_model_kind: str = "player_wounds"
    position: GridPosition = field(default_factory=lambda: GridPosition(0, 0))
    movement_meters: int = 0
    preparation: int = 0
    attrition_spent: int = 0
    characteristics: dict[str, int] = field(default_factory=dict)
    competencies: dict[str, CompetencyRating] = field(default_factory=dict)
    armor_zones: dict[str, ArmorZoneLoadout] = field(default_factory=dict)
    shield: ShieldLoadout | None = None
    weapons: dict[str, WeaponLoadout] = field(default_factory=dict)
    techniques: tuple[str, ...] = ()
    ailments: list[ActiveAilment] = field(default_factory=list)
    procedural_states: list[ProceduralState] = field(default_factory=list)
    concealment_states: list[ConcealmentState] = field(default_factory=list)
    zones: list[ZoneState] = field(default_factory=list)
    creature_zones: list[CreatureZoneState] = field(default_factory=list)
    body_state: str = "operative"
    timeline: TimelineState = field(default_factory=lambda: TimelineState(preparation=0))
    tags: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()

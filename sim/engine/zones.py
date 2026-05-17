"""Zone-capacity helpers for localized wound resolution."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from models import ZoneState


def _workspace_root() -> Path:
    return Path(__file__).resolve().parents[3]


@lru_cache(maxsize=1)
def _zone_capacities() -> dict[str, int]:
    path = _workspace_root() / "Transcendence-design" / "data" / "system" / "wounds-and-damage.yaml"
    with path.open("r", encoding="utf-8") as handle:
        data: dict[str, Any] = yaml.safe_load(handle)
    zones = data.get("wound_slots", {}).get("zones", {})
    return {str(zone_id): int(zone_data["slots"]) for zone_id, zone_data in dict(zones).items()}


def default_zone_states() -> list[ZoneState]:
    """Return canonical default runtime zones for a player-like combatant."""

    return [
        ZoneState(id=zone_id, capacity=capacity)
        for zone_id, capacity in _zone_capacities().items()
    ]

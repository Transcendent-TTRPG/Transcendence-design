"""Random number generator helpers for repeatable simulation runs."""

from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class SimulationRNG:
    """Small deterministic RNG wrapper for simulation runs."""

    seed: int | None = None

    def __post_init__(self) -> None:
        self._random = random.Random(self.seed)

    def randint(self, low: int, high: int) -> int:
        return self._random.randint(low, high)

    def d10(self) -> int:
        return self.randint(1, 10)

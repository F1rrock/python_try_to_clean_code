from dataclasses import dataclass
from typing import Tuple

from overrides import overrides

from feature.domain.entities.power_entity import PowerEntity


@dataclass
class PowerModel(PowerEntity):
    @classmethod
    def from_tuple(cls, nums: Tuple[int, int]):
        return cls(base=nums[0], extent=nums[1])

    @overrides(PowerEntity)
    def __init__(self, base: int, extent: int):
        super().__init__(base, extent)

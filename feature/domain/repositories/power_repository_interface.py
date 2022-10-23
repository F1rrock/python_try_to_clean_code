from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple

from core.errors.failure import Failure
from feature.domain.entities.power_entity import PowerEntity


@dataclass
class PowerRepositoryInterface(ABC):
    @abstractmethod
    def get_power(self, nums: Tuple[int, int]) -> PowerEntity | Failure:
        pass
